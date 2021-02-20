# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import pickWalk
from rigBot.partsLibrary import standardPart

class FrontSuspension(standardPart.StandardPart):
    """This is an empty part. It only builds a guide master and empty rig hooks.
        Format your options in the docs as follows for proper auto-documentation.
        OR Generate auto doc strings.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_hip_JNT".

        Note:
            AFTER you've added your options and their values. You can automatically generate doc strings using:
                ``from rigBot import guide``
                ``guide.generate_doc_string('MODULE_NAME')``."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)
        self.add_option('side', lock=1, default='C')
        self.add_option('name', default='front', required=True)

        self.add_option('chassisWorld', data_type='hook', default='C_chassisWorld_JNT', tool_tip='Chassis world root joint.')
        self.add_option('chassisRoll', data_type='hook', default='C_chassisRoll_JNT', tool_tip='Chassis roll joint.')
        self.add_option('suspensionDriver', data_type='hook', default='C_suspension_driver_JNT', tool_tip='Chassis joint.')
        self.add_option('steeringControl', data_type='hook', default='C_steering_CTL', tool_tip='Control to drive steering.')

        self.add_option('hubCenter', data_type='selection', tool_tip='Center point for the wheel hub.')
        self.add_option('hubEndCenter', data_type='selection', tool_tip='Optional Center end point for the  wheel hub.')
        self.add_option('enableSteering',rebuild_to_modify=1, data_type='bool', default=True)

        self.add_option('pickWalkParent',
            data_type='string',
            default="C_chassisRoll_CTL",
            selectable=True,
            tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide. Use Keyword to update any options at build time."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix              # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options = self.options            # Build options
        mirror_value = self.mirror_value  # 1.0 for left and center sided parts and -1.0 for right sided part.

        mc.setAttr(self.guide_master+'.offsetTranslateY', -0.2)

        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)
        mirror_values = [1, -1]
        enable_steering = options.get('enableSteering')

        colors = ['green', 'red']

        for mi, prefix in enumerate([l_prefix, r_prefix]):

            mirror_value = mirror_values[mi]
            color = colors[mi]

            l_main_zero, l_main_plc = self.guide_joint('main', alt_prefix=prefix, placer_only=1)

            # create hub
            hub_zero, hub_plc, hub_jnt = self.guide_joint('wheelhub', alt_prefix=prefix, constraint_type='point')
            hub_end_zero, hub_end_plc, hub_end_jnt = self.guide_joint('wheelhub_end', alt_prefix=prefix, constraint_type='point')

            mc.xform(hub_end_zero, r=1, t=[1,0,0])
            mc.parent(hub_end_jnt, hub_jnt)
            mc.aimConstraint(hub_end_plc, hub_jnt, aim=[mirror_value,0,0], u=[0,1,0], wu=[0,1,0], wut='vector')
            mc.parentConstraint(hub_plc, hub_end_zero , mo=1)

            # Create steering arm
            steer_zero, steer_plc, steer_jnt = self.guide_joint('steeringArm', alt_prefix=prefix, constraint_type='parent')
            mc.xform(steer_zero, r=1, t=[-1,0,0])
            mc.parent(hub_jnt, steer_jnt)

            # Create  shocks
            shock_a_zero, shock_a_plc, shock_a_jnt = self.guide_joint('shock_A', alt_prefix=prefix, constraint_type='point')
            shock_b_zero, shock_b_plc, shock_b_jnt = self.guide_joint('shock_B', alt_prefix=prefix, constraint_type='point')

            mc.xform(shock_a_zero, ws=1, t=[-2,2,0])
            mc.xform(shock_b_zero, ws=1, t=[-0.5,0.25,0])

            mc.parent(shock_b_jnt, shock_a_jnt)

            mc.aimConstraint(shock_b_plc, shock_a_jnt, aim=[mirror_value,0,0], u=[0,0,1], wu=[0,0,1], wut='vector')
            mc.aimConstraint(shock_a_plc, shock_b_jnt, aim=[-mirror_value,0,0], u=[0,0,1], wu=[0,0,1], wut='vector')

            # upper arm
            up_arm_zero, up_arm_plc, up_arm_jnt = self.guide_joint('upperArm', alt_prefix=prefix, constraint_type='point')
            up_arm_end_zero, up_arm_end_plc, up_arm_end_jnt = self.guide_joint('upperArm_end', alt_prefix=prefix, constraint_type='point')

            mc.xform(up_arm_end_zero, r=1, t=[-3.5,1,0])
            mc.xform(up_arm_zero, r=1, t=[-1,0.5,0])
            mc.parent(up_arm_end_jnt, up_arm_jnt)
            mc.aimConstraint(up_arm_end_plc, up_arm_jnt, aim=[mirror_value,0,0], u=[0,0,1], wu=[0,0,mirror_value], wut='objectRotation', wuo=up_arm_plc)

            # lower arm
            lo_arm_zero, lo_arm_plc, lo_arm_jnt = self.guide_joint('lowerArm', alt_prefix=prefix, constraint_type='point')
            lo_arm_end_zero, lo_arm_end_plc, lo_arm_end_jnt = self.guide_joint('lowerArm_end', alt_prefix=prefix, constraint_type='point')

            mc.xform(lo_arm_end_zero, r=1, t=[-4,-0.5,0])
            mc.xform(lo_arm_zero, r=1, t=[-1,-0.5,0])
            mc.parent(lo_arm_end_jnt, lo_arm_jnt)
            mc.aimConstraint(lo_arm_end_plc, lo_arm_jnt, aim=[mirror_value,0,0], u=[0,0,1], wu=[0,0,mirror_value], wut='objectRotation', wuo=lo_arm_plc)

            # steeringArm
            if enable_steering:
                steeringArm_a_zero, steeringArm_a_plc, steeringArm_a_jnt = self.guide_joint('steeringArm_A', alt_prefix=prefix, constraint_type='point')
                steeringArm_b_zero, steeringArm_b_plc, steeringArm_b_jnt = self.guide_joint('steeringArm_B', alt_prefix=prefix, constraint_type='point')

                mc.xform(steeringArm_b_zero, r=1, t=[-1.5,0,1])
                mc.xform(steeringArm_a_zero, r=1, t=[-4,0,1])

                mc.parent(steeringArm_b_jnt, steeringArm_a_jnt)
                mc.aimConstraint(steeringArm_b_plc, steeringArm_a_jnt, aim=[mirror_value,0,0], u=[0,0,1], wu=[0,0,1], wut='vector')

            # Create control
            zero, ctrl = self.guide_ctrl('wheel', alt_prefix=prefix, driver=hub_end_jnt, color=color, shape='circle', axis='X', scale=[3]*3, create_pivot=0)
            mc.setAttr(ctrl+'.numOffsetCtrls', 1)
            mc.addAttr(ctrl+'.numOffsetCtrls', e=1, min=1)
            mc.xform(ctrl.replace('_CTL','_A_OFF_CTL.cv[*]'), r=1, s=[0.8]*3)

            control.create_shape('wheel', ctrl, axis='X', scale=[3]*3)

            #suspension_zero, suspension_ctrl = self.guide_ctrl('suspension', create_pivot=0, driver=shock_a_jnt, axis='X', shape='pyramid', color=color, scale=[1.5,1,1], alt_prefix=prefix)
            ground_zero, ground_ctrl = self.guide_ctrl('ground', create_pivot=0, shape='square', color='grass', alt_prefix=prefix)
            mc.delete(mc.pointConstraint(hub_jnt, ground_zero))

            # constraint to placer
            childs = [prefix+'_wheelhub_JNT_PLC_ZERO',
                      prefix+'_steeringArm_JNT_PLC_ZERO',
                      prefix+'_shock_A_JNT_PLC_ZERO',
                      prefix+'_shock_B_JNT_PLC_ZERO',
                      prefix+'_upperArm_JNT_PLC_ZERO',
                      prefix+'_upperArm_end_JNT_PLC_ZERO',
                      prefix+'_lowerArm_JNT_PLC_ZERO',
                      prefix+'_lowerArm_end_JNT_PLC_ZERO']

            for c in childs:
                mc.parentConstraint(l_main_plc, c, mo=1)

            mc.setAttr(l_main_plc+'.offsetTranslateY', mirror_value*0.5)

            # ################3
            # Place it all
            hub_pos = mc.ls(options.get('hubCenter') or '')
            if hub_pos:
                loc = utils.snap_locator(hub_pos)
                mc.delete(mc.pointConstraint(loc, self.guide_master))
                mc.setAttr(self.guide_master+'.tx', 0)
                mc.delete(mc.pointConstraint(loc, l_main_plc), loc)

                hub_end_pos = mc.ls(options.get('hubEndCenter') or '')
                if hub_end_pos:
                    loc = utils.snap_locator(hub_end_pos)
                    mc.delete(mc.pointConstraint(loc, hub_end_plc), loc)

            else:
                mc.xform(self.guide_master, ws=1, t=[0,2,10])
                mc.xform(l_main_plc, r=1, t=[mirror_value*6,0,0])

            mc.setAttr(self.guide_master+'.jointAxisVis', 1)

            l = utils.snap_locator(hub_jnt)
            mc.setAttr(l+'.ty', 0)
            mc.delete(mc.pointConstraint(l, ground_zero), l)

        chassis_plc_zero, chassis_plc = self.guide_joint('chassis_driver', placer_only=1)
        mc.setAttr(chassis_plc+'.radius', 1)
        mc.setAttr(chassis_plc+'.color', 0.96, 0.71, .01)
        mc.setAttr(chassis_plc+'.otherType',  'Leg IK Driver', type='string');
        mc.setAttr(chassis_plc+'.type', 18)

        mc.pointConstraint(l_prefix+'_lowerArm_end_JNT_PLC', r_prefix+'_lowerArm_end_JNT_PLC', chassis_plc_zero)
        utils.set_attrs(chassis_plc, l=1, k=0)

        # This finalizes your guide.
        self.finalize_guide()
        self.mirror_guide()

    def build_rig(self):
        """This builds your anim rig."""


        # create rig part top nodes
        self.create_part_master()

        prefix            = self.prefix                 # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options           = self.options                # Build options
        anim_ctrls        = self.anim_ctrls             # Anim controls in this part
        bind_joints       = self.bind_joints            # Bind joints in this rig part
        world_scale_attr  = self.hooks[0]+'.worldScale' # World scale multiplier (Each hooks has it's own world scale)
        hooks             = self.hooks                  # A hook grp is created per hook attribute.
        ctrl_grps         = self.ctrl_grps              # A ctrl group is created per hook. Parent controls here.
        jnt_grps          = self.jnt_grps               # A joint groupd is created per hook. Parent joints here.
        noxform_grp       = self.noxform_grp            # No scale, no transform group for this rig part.
        mirror_value      = self.mirror_value           # 1.0 for left and center sided parts and -1.0 for right sided part.

        pickWalk_parent = options.get('pickWalkParent')

        world_grp = hooks[0]
        steering_grp = hooks[3]

        mc.addAttr(steering_grp, ln='camber', k=1, min=-10, max=10)
        mc.addAttr(steering_grp, ln='toe', min=-10, max=10, k=1)

        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)

        default_lock_value = utils.get_distance(l_prefix+'_shock_A_JNT', l_prefix+'_shock_B_JNT') * 0.333

        mc.addAttr(steering_grp, ln='suspensionExtensionMax', k=1, min=0,dv= default_lock_value)
        mc.addAttr(steering_grp, ln='suspensionCompressionMax', k=1, min=0,dv= default_lock_value)
        mc.addAttr(steering_grp, ln='steeringAngleMax', min=0, dv=45, k=1)

        mc.addAttr(steering_grp, ln='autoSteering', min=0, max=1, k=1)
        mc.addAttr(steering_grp, ln='autoWheel', min=0, max=1, k=1)
        mc.addAttr(steering_grp, ln='autoSteerAmount', k=0)

        mc.addAttr(steering_grp, ln='connectXforms', at='message')

        driver_jnt = mc.createNode('joint', n=prefix+'_chassis_driver_JNT', p=jnt_grps[2])
        mc.pointConstraint(l_prefix+'_lowerArm_end_JNT', r_prefix+'_lowerArm_end_JNT', driver_jnt)

        mirror_values = [1, -1]
        for mi, prefix in enumerate([l_prefix, r_prefix]):

            mirror_value = mirror_values[mi]

            # Create ctrls
            chassis_ctrl = hooks[1]

            up_strut = prefix+'_shock_A_JNT'
            lo_strut = prefix+'_shock_B_JNT'
            up_strut_end = prefix+'_shock_A_end_JNT'
            lo_strut_end = prefix+'_shock_B_end_JNT'
            steer_jnt = prefix+'_steeringArm_JNT'
            up_control_arm = prefix+'_upperArm_JNT'
            up_control_arm_end = prefix+'_upperArm_end_JNT'

            lo_control_arm = prefix+'_lowerArm_JNT'
            lo_control_arm_end = prefix+'_lowerArm_end_JNT'

            spindle =  prefix+'_wheelhub_JNT'
            wheel_hub = prefix+'_wheelhub_end_JNT'
            steering_assembly = prefix+'_steeringArm_JNT'

            # Create ctrls
            loc = utils.snap_locator(steering_assembly )
            mc.delete(mc.aimConstraint(up_control_arm, loc, aim=[0,1,0], u=[0,0,1], wu=[0,0,1], wut='vector'))
            wheel_zero, wheel_ctrl, wheel_offsets, wheel_last_node = self.anim_ctrl(prefix+'_wheel_CTL', match_position=loc, node_type='transform')
            mc.delete(loc)

            loc = utils.snap_locator(prefix+'_ground_CTL_REF')
            ground_zero, ground_ctrl, ground_offsets, ground_last_node = self.anim_ctrl(prefix+'_ground_CTL', match_position=loc, node_type='transform')
            mc.delete(loc)

            mc.setAttr(wheel_ctrl+'.ro', 2)

            # wheel spin
            auto_wheel_off = mc.createNode('transform', p=spindle, n=wheel_ctrl+'_AUTO_OFF')
            auto_wheel = mc.createNode('transform', p=auto_wheel_off, n=wheel_ctrl+'_AUTO')
            mc.parent(auto_wheel_off, wheel_ctrl)

            mc.parent(wheel_offsets[0], auto_wheel)
            mc.makeIdentity(wheel_offsets[0], apply=1, t=1, r=1, s=1, n=0, pn=1)
            mc.xform(wheel_offsets[0], piv=(0,0,0))

            mc.orientConstraint(wheel_offsets[0], spindle)

            # wheel ctrl limits
            ctrls = [wheel_ctrl+'_CONST', wheel_ctrl+'_MOCAP', wheel_ctrl+'_OFF', wheel_ctrl]
            for ct in ctrls:
                mc.transformLimits(ct, tx=[0,0], ty=[0,0], etx=[1,1], ety=[1,1], tz=[0,0], etz=[1,1])
                mc.connectAttr(steering_grp+'.suspensionCompressionMax', ct+'.maxTransXLimit')
                utils.connect_negative(steering_grp+'.suspensionExtensionMax', ct+'.minTransXLimit')

                mc.connectAttr(steering_grp+'.suspensionCompressionMax', ct+'.maxTransYLimit')
                utils.connect_negative(steering_grp+'.suspensionExtensionMax', ct+'.minTransYLimit')

                mc.connectAttr(steering_grp+'.suspensionCompressionMax', ct+'.maxTransZLimit')
                utils.connect_negative(steering_grp+'.suspensionExtensionMax', ct+'.minTransZLimit')

            # wheel and ground
            mc.parent(wheel_zero, ground_zero, ctrl_grps[1])
            mc.pointConstraint(ground_last_node, wheel_ctrl+'_CONST', mo=1, skip=['x','z'])

            # lower control arm
            ik = mc.ikHandle(sj=lo_control_arm, ee=lo_control_arm_end)[0]
            mc.parent(ik, jnt_grps[2])
            mc.hide(ik)

            mc.parentConstraint(wheel_ctrl, lo_control_arm, mo=1)

            # up ctrl arm
            ik = mc.ikHandle(sj=up_control_arm, ee=up_control_arm_end)[0]
            mc.parent(ik, driver_jnt)
            mc.parentConstraint(wheel_ctrl, up_control_arm, mo=1)
            mc.hide(ik)

            # orient chassis loc

            # strut
            mc.parent(up_strut, driver_jnt)
            sloc = utils.snap_locator(lo_strut, name=up_strut+'_AIM_GRP', node_type='transform')
            mc.aimConstraint(sloc, up_strut, aim=[mirror_value,0,0], u=[0,0,1], wu=[0,0,1], wut='objectRotation', wuo=driver_jnt)
            mc.parent(sloc, lo_control_arm)
            mc.pointConstraint(sloc, lo_strut)

            # streering assembly orientation   ############################################
            mc.parent(steer_jnt, lo_control_arm)
            mc.parentConstraint(wheel_ctrl, steer_jnt, mo=1)

            # streering assembly orientation, steering and toe ############################################
            for ct in ctrls:
                mc.transformLimits(ct, rx=[0,0], ry=[0,0], erx=[1,1], ery=[1,1], rz=[0,0], erz=[1,1])
                mc.connectAttr(steering_grp+'.steeringAngleMax', ct+'.maxRotXLimit')
                utils.connect_negative(steering_grp+'.steeringAngleMax', ct+'.minRotXLimit')

                mc.connectAttr(steering_grp+'.steeringAngleMax', ct+'.maxRotYLimit')
                utils.connect_negative(steering_grp+'.steeringAngleMax', ct+'.minRotYLimit')

                mc.connectAttr(steering_grp+'.steeringAngleMax', ct+'.maxRotZLimit')
                utils.connect_negative(steering_grp+'.steeringAngleMax', ct+'.minRotZLimit')

            # steering
            pma = mc.createNode('plusMinusAverage')
            if options.get('enableSteering'):

                aim = mc.createNode('transform', p=wheel_ctrl+'_CONST', n =wheel_ctrl+'_MOCAP_AIM')
                mc.setAttr(aim+'.ty', 10)
                mc.aimConstraint(aim, wheel_ctrl+'_MOCAP', aim=[0,1,0], u=[1,0,0], wu=[1,0,0], wuo=world_grp, wut='objectRotation')

                sr = mc.createNode('setRange')
                mc.connectAttr(steering_grp+'.tx', sr+'.vx')
                mc.connectAttr(steering_grp+'.steeringAngleMax', sr+'.maxX', f=1)
                utils.connect_negative(steering_grp+'.steeringAngleMax', sr+'.minX')
                mc.setAttr(sr+'.oldMinX', -10)
                mc.setAttr(sr+'.oldMaxX', 10)

                mc.connectAttr(sr+'.outValueX', pma+'.input1D[0]')

                # toe
                sr = mc.createNode('setRange')
                mc.connectAttr(steering_grp+'.toe', sr+'.vx')
                mc.connectAttr(steering_grp+'.steeringAngleMax', sr+'.maxX', f=1)
                utils.connect_negative(steering_grp+'.steeringAngleMax', sr+'.minX')
                mc.setAttr(sr+'.oldMinX', -10)
                mc.setAttr(sr+'.oldMaxX', 10)

                if mirror_value == 1:
                    utils.connect_negative(sr+'.outValueX', pma+'.input1D[1]')
                else:
                    mc.connectAttr(sr+'.outValueX', pma+'.input1D[1]')

                mc.connectAttr(pma+'.output1D', wheel_ctrl+'_OFF.ry')

                # autp steering setup
                cl = mc.createNode('clamp')
                mdl = mc.createNode('multDoubleLinear')
                utils.connect_negative(steering_grp+'.steeringAngleMax', cl+'.minR')
                mc.connectAttr(steering_grp+'.steeringAngleMax', cl+'.maxR')
                mc.connectAttr(steering_grp+'.autoSteerAmount', cl+'.inputR')

                mc.connectAttr(cl+'.outputR', mdl+'.i1')
                mc.connectAttr(steering_grp+'.autoSteering', mdl+'.i2')

                mc.connectAttr(mdl+'.o', pma+'.input1D[2]')

                # steering arm piston
                aim = utils.snap_locator(prefix+'_steeringArm_B_JNT', name=prefix+'_steering_A_AIM', node_type='transform')
                mc.parent(aim, steer_jnt)
                mc.parent(prefix+'_steeringArm_A_JNT', driver_jnt)
                mc.pointConstraint(aim, prefix+'_steeringArm_B_JNT')
                mc.aimConstraint(aim, prefix+'_steeringArm_A_JNT', aim=[mirror_value, 0,0], u=[0,1,0], wu=[0,1,0], wuo=driver_jnt, wut='objectRotation')

            # camber
            sr = mc.createNode('setRange')
            mc.connectAttr(steering_grp+'.camber', sr+'.vx')
            mc.connectAttr(steering_grp+'.steeringAngleMax', sr+'.maxX', f=1)
            utils.connect_negative(steering_grp+'.steeringAngleMax', sr+'.minX')
            mc.setAttr(sr+'.oldMinX', -10)
            mc.setAttr(sr+'.oldMaxX', 10)

            if mirror_value == 1:
                utils.connect_negative(sr+'.outValueX', wheel_ctrl+'_OFF.rz')
            else:
                mc.connectAttr(sr+'.outValueX', wheel_ctrl+'_OFF.rz')

            # autowheel
            mc.addAttr(auto_wheel, ln='autoSpin', k=1)
            mc.connectAttr(auto_wheel+'.autoSpin', auto_wheel+'.rx')

            driver = utils.snap_locator(spindle, name=prefix+'_autoWheel_DRV', node_type='transform')
            mc.parent(driver, steer_jnt)
            connect_auto_wheel(driver, steering_grp, auto_wheel+'.autoSpin', world_scale_node=hooks[0])

            utils.set_attrs(wheel_ctrl, 'rx s', l=1, k=0)
            if not options.get('enableSteering'):
                utils.set_attrs(wheel_ctrl, 'ry', l=1, k=0)


def connect_auto_wheel(driver, ctrl, spin_attr, forwardDirection=[0,0,1], radius=0.0, world_scale_node=''):

    if not radius:
        radius = utils.decompose_matrix(driver)[0][1]

    if radius < 0.001:
        radius  = 0.001

    wheel_node = mc.createNode('cmAutoWheel')
    time = mc.ls(type='time')[0]

    mc.connectAttr(driver+'.worldMatrix', wheel_node+'.postitionMatrix')
    mc.connectAttr(time+'.outTime', wheel_node+'.time')
    mc.setAttr(wheel_node+'.forwardDirection', *forwardDirection)

    mdl = mc.createNode('multDoubleLinear')
    mc.setAttr(mdl+'.i1', radius)
    mc.connectAttr(world_scale_node+'.worldScale', mdl+'.i2')
    mc.connectAttr(mdl+'.o', wheel_node+'.radius')

    if not mc.objExists(ctrl+'.autoWheel'):
        mc.addAttr(ctrl, ln='autoWheel', min=0, max=1, k=1)

    mc.connectAttr(ctrl+'.autoWheel', wheel_node+'.envelope')

    try:
        mc.setAttr(spin_attr, l=0, k=1)
    except:
        pass

    mc.connectAttr(wheel_node+'.outputSpin', spin_attr)

    return wheel_node


def get_radius(vert=None):

    if not vert:
        vert = mc.ls(sl=1)

    if not vert:
        mc.warning('Select an outtermost vert to calulate radius.')
        return

    vert = mc.ls(vert)
    if not vert:
        mc.warning('Select an outtermost vert to calulate radius.')
        return

    vert = vert[0]
    if not '.vtx[' in vert:
        mc.warning('Select an outtermost vert to calulate radius.')
        return

    mesh = vert.split('.')[0]

    l0 = utils.snap_locator(vert)
    l1 = utils.snap_locator(mesh)

    radius = utils.get_distance(l0, l1)

    return radius


