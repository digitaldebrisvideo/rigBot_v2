# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import env
from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import pickWalk
from rigBot import collision

from rigBot.partsLibrary import standardPart

class RearSuspension(standardPart.StandardPart):
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
        self.add_option('name', default='rear', required=True)
        self.add_option('chassisWorld', data_type='hook', default='C_chassisWorld_JNT')
        self.add_option('chassis', data_type='hook', default='C_chassis_JNT')
        self.add_option('steeringControl', data_type='hook', default='C_steering_CTL', tool_tip='Control to drive steering.')
        self.add_option('hubCenter', data_type='selection', tool_tip='Center point for the wheel hub.')
        self.add_option('hubEndCenter', data_type='selection', tool_tip='Optional Center end point for the  wheel hub.')
        self.add_option('axleType', data_type='enum', enum='trailingArm:rigidAxle', default='trailingArm', tool_tip='Type of axle.', rebuild_to_modify=True)

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

        orig_prefix = str(prefix)
        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)

        mirror_values = [1, -1]

        for mi, prefix in enumerate([l_prefix, r_prefix]):

            mirror_value = mirror_values[mi]

            l_main_zero, l_main_plc = self.guide_joint('main', alt_prefix=prefix, placer_only=1)

            # create hub
            hub_zero, hub_plc, hub_jnt = self.guide_joint('wheelhub', alt_prefix=prefix, constraint_type='point')
            hub_end_zero, hub_end_plc, hub_end_jnt = self.guide_joint('wheelhub_end', alt_prefix=prefix, constraint_type='point')

            mc.xform(hub_end_zero, r=1, t=[1,0,0])
            mc.parent(hub_end_jnt, hub_jnt)
            mc.aimConstraint(hub_end_plc, hub_jnt, aim=[mirror_value,0,0], u=[0,1,0], wu=[0,1,0], wut='vector')
            mc.parentConstraint(hub_plc, hub_end_zero , mo=1)

            # Create steering arm
            steer_zero, steer_plc, steer_jnt = self.guide_joint('steeringArm', alt_prefix=prefix, constraint_type='point')
            mc.xform(steer_zero, r=1, t=[-1,0,0])
            mc.parent(hub_jnt, steer_jnt)

            # Create  shocks
            shock_a_zero, shock_a_plc, shock_a_jnt = self.guide_joint('shock_A', alt_prefix=prefix, constraint_type='point')
            shock_b_zero, shock_b_plc, shock_b_jnt = self.guide_joint('shock_B', alt_prefix=prefix, constraint_type='point')
            shock_a_end_zero, shock_a_end_plc, shock_a_end_jnt = self.guide_joint('shock_A_end', alt_prefix=prefix, constraint_type='point')
            shock_b_end_zero, shock_b_end_plc, shock_b_end_jnt = self.guide_joint('shock_B_end', alt_prefix=prefix, constraint_type='point')

            mc.xform(shock_a_zero, ws=1, t=[-2,2,0])
            mc.xform(shock_b_zero, ws=1, t=[-0.5,0.25,0])

            mc.parent(shock_a_end_jnt, shock_a_jnt)
            mc.parent(shock_b_end_jnt, shock_b_jnt)

            mc.aimConstraint(shock_b_plc, shock_a_jnt, aim=[mirror_value,0,0], u=[0,0,1], wu=[0,0,1], wut='vector')
            mc.aimConstraint(shock_a_plc, shock_b_jnt, aim=[-mirror_value,0,0], u=[0,0,1], wu=[0,0,1], wut='vector')

            mc.delete(shock_b_end_zero)
            mc.pointConstraint(shock_a_plc, shock_b_plc, shock_a_end_zero)
            mc.pointConstraint(shock_a_plc, shock_b_plc, shock_b_end_jnt)
            utils.set_attrs(shock_a_end_plc, k=0, l=1)

            # lower arm
            lo_arm_zero, lo_arm_plc, lo_arm_jnt = self.guide_joint('lowerArm', alt_prefix=prefix, constraint_type='point')
            lo_arm_end_zero, lo_arm_end_plc, lo_arm_end_jnt = self.guide_joint('lowerArm_end', alt_prefix=prefix, constraint_type='point')

            mc.xform(lo_arm_zero, r=1, t=[-1,-0.5,4], ro=[0,90,0])
            mc.xform(lo_arm_end_zero, r=1, t=[-1,-0.5,0])
            mc.parent(lo_arm_end_jnt, lo_arm_jnt)
            mc.aimConstraint(lo_arm_end_plc, lo_arm_jnt, aim=[mirror_value,0,0], u=[0,0,1], wu=[0,0,mirror_value], wut='objectRotation', wuo=lo_arm_plc)

            # axle
            axle_a_zero, axle_a_plc, axle_a_jnt = self.guide_joint('axle_A', alt_prefix=prefix, constraint_type='point')
            axle_b_zero, axle_b_plc, axle_b_jnt = self.guide_joint('axle_B', alt_prefix=prefix, constraint_type='point')

            mc.xform(axle_b_zero, r=1, t=[-1.5,0,0])
            mc.xform(axle_a_zero, r=1, t=[-4,0,0])

            mc.parent(axle_b_jnt, axle_a_jnt)
            mc.aimConstraint(axle_b_plc, axle_a_jnt, aim=[mirror_value,0,0], u=[0,0,1], wu=[0,0,1], wut='vector')

            mc.parentConstraint(steer_plc, axle_b_zero, mo=1)

            # Create control
            zero, ctrl = self.guide_ctrl('wheel', alt_prefix=prefix, driver=hub_end_jnt, color='green', shape='circle', axis='X', scale=[3]*3, create_pivot=0)
            mc.setAttr(ctrl+'.numOffsetCtrls', 1)
            mc.addAttr(ctrl+'.numOffsetCtrls', e=1, min=1)

            control.create_shape('wheel', ctrl, axis='X', scale=[3]*3)

            # constraint to placer
            childs = [prefix+'_wheelhub_JNT_PLC_ZERO',
                      prefix+'_steeringArm_JNT_PLC_ZERO',
                      prefix+'_shock_A_JNT_PLC_ZERO',
                      prefix+'_axle_A_JNT_PLC_ZERO',
                      prefix+'_shock_B_JNT_PLC_ZERO',
                      prefix+'_lowerArm_JNT_PLC_ZERO',
                      prefix+'_lowerArm_end_JNT_PLC_ZERO']

            for c in childs:
                mc.parentConstraint(l_main_plc, c, mo=1)

            mc.setAttr(l_main_plc+'.offsetTranslateY', mirror_value*0.5)

            # ################3
            # Place it all
            hub_pos = mc.ls(options.get('hubCenter') or [])
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
                mc.xform(self.guide_master, ws=1, t=[0,2,-10])
                mc.xform(l_main_plc, a=1, t=[mirror_value*6,0,0])

            mc.setAttr(self.guide_master+'.jointAxisVis', 1)

        # axle
        if options.get('axleType') == 'rigidAxle':
            cons = utils.get_constraints(l_prefix+'_axle_A_JNT_PLC_ZERO')
            if cons:
                mc.delete(cons)

            mc.pointConstraint(l_prefix+'_axle_B_JNT_PLC', r_prefix+'_axle_B_JNT_PLC', l_prefix+'_axle_A_JNT_PLC_ZERO')
            mc.xform(l_prefix+'_axle_A_JNT_PLC', a=1, t=[0,0,0], ro=[0,0,0])

            cons = utils.get_constraints(r_prefix+'_axle_A_JNT_PLC_ZERO')
            if cons:
                mc.delete(cons)

            mc.pointConstraint( l_prefix+'_axle_A_JNT_PLC', r_prefix+'_axle_A_JNT_PLC_ZERO')
            mc.pointConstraint( l_prefix+'_axle_A_JNT_PLC', r_prefix+'_axle_A_JNT_PLC')
            mc.xform(r_prefix+'_axle_A_JNT_PLC', a=1, t=[0,0,0], ro=[0,0,0])

            utils.set_attrs([r_prefix+'_axle_A_JNT_PLC', l_prefix+'_axle_A_JNT_PLC'], l=1, k=0)

        # drive shaft
        drive_zero, drive_plc, drive_jnt = self.guide_joint('propShaft', constraint_type='point')
        drive_end_zero, drive_end_plc, drive_end_jnt = self.guide_joint('propShaft_end', constraint_type='point')

        mc.pointConstraint( l_prefix+'_axle_B_JNT_PLC', r_prefix+'_axle_B_JNT_PLC', drive_zero)
        mc.delete(mc.pointConstraint( l_prefix+'_axle_B_JNT_PLC', r_prefix+'_axle_B_JNT_PLC', drive_end_zero))
        mc.xform(drive_zero, drive_end_zero, r=1, ro=[0,-90,0])

        mc.setAttr(drive_end_zero+'.tx' ,0)
        mc.parent(drive_end_jnt, drive_jnt)

        mc.aimConstraint(drive_end_plc, drive_jnt, aim=[1,0,0], u=[0,1,0], wu=[0,1,0], wut='objectRotation', wuo=self.guide_master)

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
        chassis_grp = hooks[1]
        steering_grp = hooks[2]

        mc.addAttr(steering_grp, ln='camber', k=1)
        mc.addAttr(steering_grp, ln='toe', k=1)
        mc.addAttr(steering_grp, ln='maxSteeringAngle', min=0, dv=45, k=1)
        mc.addAttr(steering_grp, ln='suspensionLimit', min=0, dv=45, k=1)
        mc.addAttr(steering_grp, ln='autoSteering', min=0, max=1, k=1)
        mc.addAttr(steering_grp, ln='autoWheel', min=0, max=1, k=1)
        mc.addAttr(steering_grp, ln='groundCollision', min=0, max=1, k=1)
        mc.addAttr(steering_grp, ln='connectXforms', at='message')

        mirror_values = [1, -1]

        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)

        orig_prefix = str(prefix)

        plane = mc.polyPlane(ch=0)[0]
        mc.parent(plane, noxform_grp)

        for mi, prefix in enumerate([l_prefix, r_prefix]):

            mirror_value = mirror_values[mi]

            # Create ctrls
            zero, ctrl, offsets, last_node = self.anim_ctrl(prefix+'_wheel_CTL')

            mc.addAttr(ctrl, ln='lift', k=1)
            mc.addAttr(ctrl, ln='spin', k=1)
            mc.addAttr(ctrl, ln='steer', k=1)
            mc.addAttr(ctrl, ln='camber', k=1)

            # set up joint constraints
            hub_jnt = prefix+'_wheelhub_JNT'
            hub_end_jnt = prefix+'_wheelhub_end_JNT'
            steer_jnt = prefix+'_steeringArm_JNT'
            lo_arm_jnt = prefix+'_lowerArm_JNT'
            lo_arm_end_jnt = prefix+'_lowerArm_end_JNT'
            shock_a_jnt = prefix+'_shock_A_JNT'
            shock_b_jnt = prefix+'_shock_B_JNT'
            shock_a_end_jnt = prefix+'_shock_A_end_JNT'
            shock_b_end_jnt = prefix+'_shock_B_end_JNT'

            #######################
            # Ground plane node
            ground_drv = utils.snap_locator(hub_jnt, name=prefix+'_ground_DRV', node_type='transform')
            ground_off = utils.snap_locator(hub_jnt, name=prefix+'_ground_OFF', node_type='transform')
            ground_col = utils.snap_locator(hub_jnt, name=prefix+'_ground_COLLIDE', node_type='transform')
            ground = utils.snap_locator(hub_jnt, name=prefix+'_ground', node_type='transform')

            mc.setAttr(ground_col+'.ty', 0.001)
            mc.parent(ground_col, ground_off)
            mc.parent(ground, ground_col)

            mc.pointConstraint(ground_drv, ground_off, skip='y')
            mc.parent(ground_off, jnt_grps[0])
            mc.parent(ground_drv, jnt_grps[1])

            ground_ori = mc.duplicate(ground_off, po=1, n=ground+'_ORIENT')[0]
            ground_aim = mc.createNode('transform', p=ground_ori, n=ground+'_AIM')

            mc.pointConstraint(ground_off, ground_ori)
            mc.setAttr(ground_aim+'.ty', 1)

            mc.aimConstraint(ground_aim, ground_off, aim=[0,1,0], u=[0,0,1], wu=[0,0,1], wut='objectRotation', wuo=jnt_grps[1])

            if env.use_plugin():
                result = collision.create(ground_col)
                utils.break_connections(result[0], 'r')
                mc.parent(ground, result[0])
                mc.connectAttr(steering_grp+'.groundCollision', ground_col+'.collisionEnvelope')

            #############################
            # Lower A Arm
            lo_grp_par = utils.snap_locator(lo_arm_jnt, name=prefix+'_lowerArm_drv_PAR', node_type='transform')
            lo_grp = utils.snap_locator(lo_arm_jnt, name=prefix+'_lowerArm_drv_GRP', node_type='transform')
            mc.parent(lo_grp, lo_grp_par)

            mc.delete(mc.orientConstraint(lo_arm_jnt, lo_grp_par))

            lo_upv_grp = utils.snap_locator(lo_arm_end_jnt, name=prefix+'_lowerArm_upvec_GRP', node_type='transform')
            lo_aim_grp = utils.snap_locator(lo_arm_jnt, name=prefix+'_lowerArm_aim_GRP', node_type='transform')

            mc.parent(lo_aim_grp, lo_arm_jnt)

            mc.xform(lo_aim_grp, r=1, t=[0,0,1])
            mc.parent(lo_upv_grp, ground)

            mc.parent(lo_aim_grp, lo_arm_jnt, lo_grp_par, jnt_grps[1])

            mc.aimConstraint(lo_aim_grp, lo_grp, aim=[0,0,1], u=[mirror_value,0,0], wut='object', wuo=ground)
            arm_drv = mc.duplicate(lo_arm_jnt, n=lo_arm_jnt+'_DRV', po=1)[0]
            mc.orientConstraint(lo_grp, arm_drv, mo=1)

            # suspension limit
            cl = mc.createNode('clamp')
            mc.connectAttr(arm_drv+'.rz', cl+'.inputR',f=1)

            utils.connect_negative(steering_grp+'.suspensionLimit', cl+'.minR')
            mc.connectAttr(steering_grp+'.suspensionLimit', cl+'.maxR')

            adl = mc.createNode('addDoubleLinear')
            mc.connectAttr(cl+'.outputR', adl+'.i1')
            mc.connectAttr(adl+'.o', lo_arm_jnt+'.rz')

            # lift attr
            mc.connectAttr(ctrl+'.lift', adl+'.i2')

            #############################
            # Shocks
            mc.parent(shock_a_jnt, jnt_grps[1])
            mc.parent(shock_b_jnt, lo_arm_end_jnt)

            mc.aimConstraint(shock_b_jnt, shock_a_jnt, aim=[mirror_value,0,0], u=[0,0,1], wu=[0,0,1], wuo=chassis_grp, wut='objectRotation')
            mc.aimConstraint(shock_a_jnt, shock_b_jnt, aim=[-mirror_value,0,0], u=[0,0,1], wu=[0,0,1], wuo=chassis_grp, wut='objectRotation')

            mc.pointConstraint(shock_a_jnt, shock_b_jnt, shock_a_end_jnt)
            mc.pointConstraint(shock_a_jnt, shock_b_jnt, shock_b_end_jnt)
            mc.hide(shock_b_end_jnt)

            ########################
            # steering & camber

            camber_off = utils.snap_locator(lo_arm_end_jnt, name=prefix+'_camber_OFF', node_type='transform')
            camber_par = utils.snap_locator(lo_arm_end_jnt, name=prefix+'_camber_PAR', node_type='transform')
            camber_grp = utils.snap_locator(lo_arm_end_jnt, name=prefix+'_camber_GRP', node_type='transform')

            mc.parent(camber_par, camber_off)
            mc.parent(camber_grp, camber_par)

            if options.get('axleType') == 'trailingArm':
                mc.orientConstraint(ground, camber_par, mo=0)

            mc.setAttr(camber_grp+'.rotateOrder', 1)
            mc.setAttr(camber_par+'.rotateOrder', 1)

            mc.parent(camber_off, lo_arm_jnt)
            mc.parent(steer_jnt, camber_grp )

            #axles
            axle_end = prefix+'_axle_B_JNT'
            axle = prefix+'_axle_A_JNT'

            loc = utils.snap_locator(axle_end, name=axle+'_AIM', node_type='transform')
            mc.parent(loc, camber_grp)

            mc.aimConstraint(loc, axle, aim=[mirror_value,0,0], u=[0,0,1], wu=[0,0,1], wuo=chassis_grp, wut='objectRotation')
            mc.pointConstraint (loc, axle_end)

            mc.parent(axle, jnt_grps[1])

            # Camber
            adl = mc.createNode('addDoubleLinear')
            mc.connectAttr(adl+'.o', camber_grp+'.rz')

            if mirror_value == -1:
                mc.connectAttr(ctrl+'.camber', adl+'.i1')
                mc.connectAttr(steering_grp+'.camber', adl+'.i2')

            else:
                utils.connect_negative(ctrl+'.camber', adl+'.i1')
                utils.connect_negative(steering_grp+'.camber', adl+'.i2')

            # Wheel SPIN and prep for auto wheeel
            adl = mc.createNode('addDoubleLinear')
            auto_wheel = mc.rename(ctrl+'_MOCAP', ctrl+'_AUTO')
            mc.addAttr(auto_wheel, ln='autoSpin', k=1)
            mc.connectAttr(ctrl+'.spin', adl+'.i1')
            mc.connectAttr(auto_wheel+'.autoSpin', adl+'.i2')
            mc.connectAttr(adl+'.o', hub_jnt+'.rx')

            # offset
            mc.parentConstraint(hub_jnt, zero, mo=1)
            mc.parentConstraint(last_node, hub_end_jnt, mo=1)

            #ceanup
            mc.parent(zero, ctrl_grps[0])
            utils.set_attrs(ctrl, 't r s', l=1, k=0)
            utils.set_attrs(offsets, 's', l=1, k=0)

            # autowheel
            driver = utils.snap_locator(hub_jnt, name=prefix+'_autoWheel_DRV', node_type='transform')
            mc.parent(driver, steer_jnt)
            connect(driver, steering_grp, ctrl+'_AUTO.autoSpin')

            pickWalk.attribute_tag(ctrl, pickWalk_parent)

            if options.get('axleType') == 'rigidAxle':
                mc.parentConstraint(axle_end, steer_jnt, mo=1)

        if mc.ls(prefix+'*', type='cmCollision'):
            mc.delete(plane)

        if options.get('axleType') == 'rigidAxle':
            mc.pointConstraint(l_prefix+'_axle_A_JNT_AIM', r_prefix+'_axle_A_JNT_AIM', l_prefix+'_axle_A_JNT')
            mc.pointConstraint(l_prefix+'_axle_A_JNT_AIM', r_prefix+'_axle_A_JNT_AIM', r_prefix+'_axle_A_JNT')

        loc = utils.snap_locator(orig_prefix+'_propShaft_end_JNT', name=orig_prefix+'propShaft_AIM', node_type='transform')
        mc.parent(loc, jnt_grps[1])
        mc.pointConstraint(l_prefix+'_axle_A_JNT', r_prefix+'_axle_A_JNT', orig_prefix+'_propShaft_JNT')
        mc.aimConstraint(loc,  orig_prefix+'_propShaft_JNT', aim=[1,0,0], u=[0,1,0], wu=[0,1,0], wuo=chassis_grp, wut='objectRotation')

        # This finalizes the rig and creates rig sets
        self.finalize_part()

def connect(driver, ctrl, spin_attr, forwardDirection=[0,0,1], radius=0.0):

    if not radius:
        radius = utils.decompose_matrix(driver)[0][1]

    if radius < 0.001:
        radius  = 0.001

    wheel_node = mc.createNode('cmAutoWheel')
    time = mc.ls(type='time')[0]

    mc.connectAttr(driver+'.worldMatrix', wheel_node+'.postitionMatrix')
    mc.connectAttr(time+'.outTime', wheel_node+'.time')
    mc.setAttr(wheel_node+'.forwardDirection', *forwardDirection)
    mc.setAttr(wheel_node+'.radius', radius)

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





