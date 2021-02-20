# -*- rigBot: part -*-
import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import pickWalk
from rigBot.partsLibrary import standardPart

class Chassis(standardPart.StandardPart):
    """Vehicle Chassis module.

    Build Options:
        :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
        :parent: (str) Parent. Defaults to "C_root_JNT".
        :bodyCenter: (list) Center point for the body pivot. Defaults to [].
        :leftFrontHub: (list) Center point for the front wheel hub. Defaults to [].
        :leftRearHub: (list) Center point for the rear wheel hub. Defaults to []."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)
        self.add_option('side', default='C', lock=True)
        self.add_option('parent', data_type='hook', default='C_root_JNT')
        self.add_option('frontChassisDriver', data_type='hook', default='C_front_chassis_driver_JNT', tool_tip='Front suspension chassis driver node.')
        self.add_option('rearChassisDriver', data_type='hook', default='C_rear_chassis_driver_JNT', tool_tip='Front suspension chassis driver node.')

        self.add_option('leftFrontWheelCenter', data_type='selection', tool_tip='Center point for the front wheel hub.')
        self.add_option('leftRearWheelCenter', data_type='selection', tool_tip='Center point for the rear wheel hub.')

        self.add_option('pickWalkParent',
            data_type='string',
            default="world_CTL",
            selectable=True,
            tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide. Use Keyword to update any options at build time."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix              # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options = self.options            # Build options
        mirror_value = self.mirror_value  # 1.0 for left and center sided parts and -1.0 for right sided part.

        front_sus_geo = mc.ls(options.get('leftFrontWheelCenter'))
        rear_sus_geo = mc.ls(options.get('leftRearWheelCenter'))

        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)

        # get pivots
        if front_sus_geo:
            front_sus_loc = utils.snap_locator(front_sus_geo)
        else:
            front_sus_loc = utils.snap_locator()
            mc.xform(front_sus_loc, ws=1, t=[6,2,10])

        if rear_sus_geo:
            rear_sus_loc = utils.snap_locator(rear_sus_geo)
        else:
            rear_sus_loc = utils.snap_locator()
            mc.xform(rear_sus_loc, ws=1, t=[6,2,-10])

        body_loc = utils.snap_locator(front_sus_loc)
        mc.delete(mc.pointConstraint(front_sus_loc, rear_sus_loc, body_loc))
        mc.setAttr(body_loc+'.tx', 0)

        # Create jhoints
        chassisBase_zero, chassisBase_plc, chassisBase_jnt = self.guide_joint('chassisWorld')
        chassisRoll_zero, chassisRoll_plc, chassisRoll_jnt = self.guide_joint('chassisRoll')
        chassis_zero, chassis_plc, chassis_jnt = self.guide_joint('chassis')

        suspension_driver_zero, suspension_driver_plc = self.guide_joint('suspension_driver', placer_only=True)

        # Create pitch and roll joints
        front_bumper_zero, front_bumper_plc = self.guide_joint('front_bumper', placer_only=True)
        rear_bumper_zero, rear_bumper_plc = self.guide_joint('rear_bumper', placer_only=True)

        l_roll_zero, l_roll_plc = self.guide_joint('roll', alt_prefix=l_prefix,  placer_only=True)
        r_roll_zero, r_roll_plc = self.guide_joint('roll', alt_prefix=r_prefix, placer_only=True)

        # Create suspension joints
        l_front_sus_zero, l_front_sus_plc = self.guide_joint('frontSuspension', alt_prefix=l_prefix, placer_only=True)
        l_rear_sus_zero, l_rear_sus_plc = self.guide_joint('rearSuspension', alt_prefix=l_prefix, placer_only=True)
        r_front_sus_zero, r_front_sus_plc = self.guide_joint('frontSuspension', alt_prefix=r_prefix, placer_only=True)
        r_rear_sus_zero, r_rear_sus_plc = self.guide_joint('rearSuspension', alt_prefix=r_prefix, placer_only=True)

        # parent and place chassis
        mc.setAttr(chassisBase_plc+'.offsetTranslateY', -0.5)
        mc.setAttr(chassisRoll_plc+'.offsetTranslateY', 0)
        mc.setAttr(chassis_plc+'.offsetTranslateY', 0.5)

        mc.parentConstraint(chassisRoll_jnt, chassis_zero, mo=1)

        mc.xform(chassisRoll_zero, ws=1, t=mc.xform(body_loc, q=1, ws=1, t=1))
        mc.xform(chassisRoll_zero, ws=1, t=mc.xform(body_loc, q=1, ws=1, t=1))

        mc.xform(l_front_sus_zero, ws=1, t=mc.xform(front_sus_loc, q=1, ws=1, t=1))
        mc.xform(l_rear_sus_zero, ws=1, t=mc.xform(rear_sus_loc, q=1, ws=1, t=1))

        lf_pos = mc.xform(front_sus_loc, q=1, ws=1, t=1)
        lf_pos[0] *= -1
        mc.xform(r_front_sus_zero, ws=1, t=lf_pos)

        lf_pos = mc.xform(rear_sus_loc, q=1, ws=1, t=1)
        lf_pos[0] *= -1
        mc.xform(r_rear_sus_zero, ws=1, t=lf_pos)

        mc.delete(body_loc, front_sus_loc, rear_sus_loc)
        mc.setAttr(r_front_sus_plc+'.radius', 1)
        mc.setAttr(l_front_sus_plc+'.radius', 1)
        mc.setAttr(r_rear_sus_plc+'.radius', 1)
        mc.setAttr(l_rear_sus_plc+'.radius', 1)

        mc.delete(mc.pointConstraint(chassis_zero, chassisBase_zero, skip='y'))

        # place roll and bumber joitns
        mc.delete(mc.pointConstraint(l_front_sus_plc, r_front_sus_plc, front_bumper_zero))
        mc.delete(mc.pointConstraint(l_rear_sus_plc, r_rear_sus_plc, rear_bumper_zero))
        mc.xform(front_bumper_zero, r=1, t=[0,0,4])
        mc.xform(rear_bumper_zero, r=1, t=[0,0,-4])

        mc.delete(mc.pointConstraint(l_front_sus_plc, l_rear_sus_plc, l_roll_zero))
        mc.delete(mc.pointConstraint(r_front_sus_plc, r_rear_sus_plc, r_roll_zero))

        mc.setAttr(l_roll_zero+'.ty', 0)
        mc.setAttr(r_roll_zero+'.ty', 0)
        mc.setAttr(front_bumper_zero+'.ty', 0)
        mc.setAttr(rear_bumper_zero+'.ty', 0)

        self.tag_as_ref([r_front_sus_plc, l_front_sus_plc,
                         r_rear_sus_plc, l_rear_sus_plc, l_roll_plc,
                         r_roll_plc, front_bumper_plc, rear_bumper_plc])

        # Create ctrls
        chassisWorld_zero, chassisWorld_ctrl = self.guide_ctrl('chassisWorld', driver=chassisBase_jnt, create_pivot=0, shape='square', color='lavendar', scale=[25,25,30], axis='Y')
        mc.setAttr(chassisWorld_ctrl+'.numOffsetCtrls', 1)
        mc.addAttr(chassisWorld_ctrl+'.numOffsetCtrls', e=1, min=1)

        front_chassis_zero, front_chassis_ctrl = self.guide_ctrl('frontDrift', driver=front_bumper_plc, create_pivot=0, shape='arrow_double_curved', axis='Z', color='yellow', scale=[12, 8, 10])
        rear_chassis_zero, rear_chassis_ctrl = self.guide_ctrl('rearDrift', driver=rear_bumper_plc, create_pivot=0, shape='arrow_double_curved', axis='-Z', color='yellow', scale=[12, 8, 10])

        '''
        l_roll_zero, l_roll_ctrl = self.guide_ctrl('roll', driver=l_roll_plc, alt_prefix=l_prefix , create_pivot=0, shape='arrow_double_curved', axis='Y', color='yellow', scale=[8, 8, 8])
        r_roll_zero, r_roll_ctrl = self.guide_ctrl('roll', driver=r_roll_plc, alt_prefix=r_prefix, create_pivot=0, shape='arrow_double_curved', axis='-Y', color='yellow', scale=[8, 8, 8])
        mc.xform(l_roll_ctrl+'.cv[*]', r=1, ro=[0,0,-90])
        mc.xform(r_roll_ctrl+'.cv[*]', r=1, ro=[0,0,-90])
        '''

        roll_zero, roll_ctrl = self.guide_ctrl('chassisRoll', driver=chassis_jnt, create_pivot=0, shape='arrow_gimbal', allow_offset_ctrls=0, color='cyan', scale=[10]*3, axis='Y')
        iso_zero, iso_ctrl = self.guide_ctrl('chassisIso', driver=chassisRoll_jnt, create_pivot=0, shape='jack_thin', color='pink', scale=[5]*3, axis='Y')

        # suspension ctrls
        lf_suspension_zero, lf_suspension_ctrl = self.guide_ctrl('frontSuspension', create_pivot=1, driver=l_front_sus_plc, shape='sphere', color='cyan', alt_prefix=l_prefix)
        lr_suspension_zero, lr_suspension_ctrl = self.guide_ctrl('rearSuspension', create_pivot=1, driver=l_rear_sus_plc, shape='sphere', color='cyan', alt_prefix=l_prefix)
        rf_suspension_zero, rf_suspension_ctrl = self.guide_ctrl('frontSuspension', create_pivot=1, driver=r_front_sus_plc, shape='sphere', color='cyan', alt_prefix=r_prefix)
        rr_suspension_zero, rr_suspension_ctrl = self.guide_ctrl('rearSuspension', create_pivot=1, driver=r_rear_sus_plc, shape='sphere', color='cyan', alt_prefix=r_prefix)

        mc.xform(lf_suspension_ctrl+'_CONST', rf_suspension_ctrl+'_CONST', lr_suspension_ctrl+'_CONST', rr_suspension_ctrl+'_CONST', r=1, t=[0,5,0])

        utils.set_attrs([utils.get_parent(lf_suspension_ctrl), utils.get_parent(rf_suspension_ctrl), utils.get_parent(lr_suspension_ctrl), utils.get_parent(rr_suspension_ctrl)], l=1, k=0)
        utils.set_attrs([utils.get_parent(lf_suspension_ctrl), utils.get_parent(rf_suspension_ctrl), utils.get_parent(lr_suspension_ctrl), utils.get_parent(rr_suspension_ctrl)], 'rz', l=0, k=1)

        mc.setAttr(utils.get_parent(lf_suspension_ctrl)+'.rz', 10)
        mc.setAttr(utils.get_parent(rf_suspension_ctrl)+'.rz', 10)
        mc.setAttr(utils.get_parent(lr_suspension_ctrl)+'.rz', 10)
        mc.setAttr(utils.get_parent(rr_suspension_ctrl)+'.rz', 10)

        # cleanup
        utils.set_attrs(l_front_sus_plc, 'r s', l=1, k=0)
        utils.set_attrs(r_front_sus_plc, 'r s', l=1, k=0)
        utils.set_attrs(l_rear_sus_plc, 'r s', l=1, k=0)
        utils.set_attrs(r_rear_sus_plc, 'r s', l=1, k=0)
        utils.set_attrs(chassis_plc, 'r s', l=1, k=0)
        utils.set_attrs(chassisBase_plc, 'r s', l=1, k=0)
        utils.set_attrs(chassisRoll_plc, 'r s', l=1, k=0)

        utils.set_attrs(l_roll_plc, 'r s', l=1, k=0)
        utils.set_attrs(r_roll_plc, 'r s', l=1, k=0)
        utils.set_attrs(rear_bumper_plc, 'r s', l=1, k=0)
        utils.set_attrs(front_bumper_plc, 'r s', l=1, k=0)

        steer_zero, steer_ctrl = self.guide_ctrl('steering', driver=chassis_jnt, shape='arrow_double', axis='Y', color='pink', scale=[4,5,5])
        mc.delete(mc.pointConstraint(l_front_sus_plc, r_front_sus_plc, steer_ctrl+'_CONST'))
        mc.xform(utils.get_parent(steer_ctrl), r=1, t=[0,3,0])

        mc.pointConstraint(l_front_sus_plc, r_front_sus_plc, front_bumper_zero)
        mc.pointConstraint(l_rear_sus_plc, r_rear_sus_plc, rear_bumper_zero)

        mc.parentConstraint(chassis_plc, suspension_driver_zero, mo=0)
        mc.setAttr(suspension_driver_plc+'.radius', 1)
        mc.setAttr(suspension_driver_plc+'.offsetTranslateY', 1)
        mc.setAttr(suspension_driver_plc+'.color', 0.96, 0.71, .01)
        mc.setAttr(suspension_driver_plc+'.otherType',  'Leg IK Driver', type='string');
        mc.setAttr(suspension_driver_plc+'.type', 18)
        utils.set_attrs(suspension_driver_plc, k=0, l=1)

        self.finalize_guide()

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

        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)

        pickWalk_parent = options.get('pickWalkParent')

        # Build ctrls
        chassis_jnt = prefix+'_chassis_JNT'
        chassisWorld_jnt = prefix+'_chassisWorld_JNT'
        chassisRoll_jnt = prefix+'_chassisRoll_JNT'

        lf_plc = l_prefix+'_frontSuspension_JNT_PLC_REF'
        rf_plc = r_prefix+'_frontSuspension_JNT_PLC_REF'
        lr_plc = l_prefix+'_rearSuspension_JNT_PLC_REF'
        rr_plc = r_prefix+'_rearSuspension_JNT_PLC_REF'

        front_bumper_plc = prefix+'_front_bumper_JNT_PLC_REF'
        rear_bumper_plc = prefix+'_rear_bumper_JNT_PLC_REF'

        l_roll_plc = l_prefix+'_roll_JNT_PLC_REF'
        r_roll_plc = r_prefix+'_roll_JNT_PLC_REF'

        name = prefix+'_frontDrift_CTL'
        loc = utils.snap_locator([lf_plc, rf_plc])
        front_drift_zero, front_drift_ctrl, front_drift_offsets, front_drift_last_node = self.anim_ctrl(name, match_position=loc)
        mc.delete(loc)

        name = prefix+'_rearDrift_CTL'
        loc = utils.snap_locator([lr_plc, rr_plc])
        rear_drift_zero, rear_drift_ctrl, rear_drift_offsets, rear_drift_last_node = self.anim_ctrl(name, match_position=loc)
        mc.delete(loc)

        name = l_prefix+'_frontSuspension_CTL'
        loc = utils.snap_locator(name+'_REF')
        mc.parent(loc, name+'_REF')
        mc.xform(loc, a=1, ro=[0,0,0], s=[1,1,1])
        l_front_sus_zero, l_front_sus_ctrl, l_front_sus_offsets, l_front_sus_last_node = self.anim_ctrl(name, match_position=loc)
        mc.delete(loc)

        name = l_prefix+'_rearSuspension_CTL'
        loc = utils.snap_locator(name+'_REF')
        mc.parent(loc, name+'_REF')
        mc.xform(loc, a=1, ro=[0,0,0], s=[1,1,1])
        l_rear_sus_zero, l_rear_sus_ctrl, l_rear_sus_offsets, l_rear_sus_last_node = self.anim_ctrl(name, match_position=loc)
        mc.delete(loc)

        name = r_prefix+'_frontSuspension_CTL'
        loc = utils.snap_locator(name+'_REF')
        mc.parent(loc, name+'_REF')
        mc.xform(loc, a=1, ro=[0,0,0], s=[1,-1,1])
        r_front_sus_zero, r_front_sus_ctrl, r_front_sus_offsets, r_front_sus_last_node = self.anim_ctrl(name, match_position=loc)
        mc.delete(loc)

        name = r_prefix+'_rearSuspension_CTL'
        loc = utils.snap_locator(name+'_REF')
        mc.parent(loc, name+'_REF')
        mc.xform(loc, a=1, ro=[0,0,0], s=[1,-1,1])
        r_rear_sus_zero, r_rear_sus_ctrl, r_rear_sus_offsets, r_rear_sus_last_node = self.anim_ctrl(name, match_position=loc)
        mc.delete(loc)

        name = prefix+'_chassisWorld_CTL'
        loc = utils.snap_locator(chassisWorld_jnt)
        chassisWorld_zero, chassisWorld_ctrl, chassisWorld_offsets, chassisWorld_last_node = self.anim_ctrl(name, match_position=loc)
        mc.delete(loc)

        name = prefix+'_chassisRoll_CTL'
        loc = utils.snap_locator(name+'_REF')
        roll_zero, roll_ctrl, roll_offsets, roll_last_node = self.anim_ctrl(name, match_position=loc)
        mc.delete(loc)

        name = prefix+'_chassisIso_CTL'
        loc = utils.snap_locator(chassis_jnt)
        chassisIso_zero, chassisIso_ctrl, chassisIso_offsets, chassisIso_last_node = self.anim_ctrl(name, match_position=loc)
        mc.delete(loc)

        name = prefix+'_steering_CTL'
        loc = utils.snap_locator(prefix+'_steering_CTL_REF')
        dist = utils.get_distance(lf_plc, rf_plc)*0.05
        mc.xform(loc, r=1, s=[dist*0.5]*3)
        steer_zero, steer_ctrl, steer_offsets, steer_last_node = self.anim_ctrl(name, match_position=loc, inherit_scale=1)
        mc.parentConstraint(chassis_jnt, steer_zero, mo=1)
        mc.delete(loc)

        l_roll_grp = mc.createNode('transform', n=l_prefix+'_roll_GRP')
        r_roll_grp = mc.createNode('transform', n=r_prefix+'_roll_GRP')

        mc.delete(mc.pointConstraint(l_prefix+'_roll_JNT_PLC_REF', l_roll_grp))
        mc.delete(mc.pointConstraint(r_prefix+'_roll_JNT_PLC_REF', r_roll_grp))

        # parent ctrls
        mc.parent(front_drift_zero, chassisWorld_last_node)
        mc.parent(rear_drift_zero, front_drift_last_node)
        mc.parent(l_roll_grp, rear_drift_last_node)
        mc.parent(r_roll_grp, l_roll_grp)

        top_node_off = mc.createNode('transform', n=prefix+'_chassisSuspension_OFF')
        top_node = mc.createNode('transform', n=prefix+'_chassisSuspension_GRP', p=top_node_off)
        mc.parent(top_node_off, r_roll_grp)

        mc.delete(mc.pointConstraint(chassis_jnt, top_node_off))

        mc.parent(
            l_front_sus_zero,
            r_front_sus_zero,
            l_rear_sus_zero,
            r_rear_sus_zero,
            top_node)

        # ik ish suspension
        lfaim = mc.createNode('transform', n=l_front_sus_last_node+'_aim_GRP', p=l_front_sus_last_node)
        lraim = mc.createNode('transform', n=l_rear_sus_last_node+'_aim_GRP', p=l_rear_sus_last_node)
        rfaim = mc.createNode('transform', n=r_front_sus_last_node+'_aim_GRP', p=r_front_sus_last_node)
        rraim = mc.createNode('transform', n=r_rear_sus_last_node+'_aim_GRP', p=r_rear_sus_last_node)

        mc.aimConstraint(r_rear_sus_last_node, lfaim, n=lfaim+'_ac', wuo=r_front_sus_last_node, aim=[0,1,0], u=[1,0,0], wut='object')
        mc.aimConstraint(l_rear_sus_last_node, rfaim, n=rfaim+'_ac', wuo=l_front_sus_last_node, aim=[0,1,0], u=[-1,0,0], wut='object')
        mc.aimConstraint(r_front_sus_last_node, lraim, n=lraim+'_ac', wuo=r_rear_sus_last_node, aim=[0,-1,0], u=[1,0,0], wut='object')
        mc.aimConstraint(l_front_sus_last_node, rraim, n=rraim+'_ac', wuo=l_rear_sus_last_node, aim=[0,-1,0], u=[-1,0,0], wut='object')

        mc.parent (chassisIso_zero, top_node)
        mc.parent(chassisIso_ctrl+'_CONST', w=1)
        prc = mc.parentConstraint(lfaim, rfaim, lraim, rraim, chassisIso_zero, mo=1)
        mc.setAttr(prc[0]+'.interpType', 2)
        mc.parent(chassisIso_ctrl+'_CONST', chassisIso_zero)

        mc.parent(steer_zero, top_node)
        mc.parent(chassisWorld_zero, ctrl_grps[0])

        mc.parentConstraint(chassisWorld_last_node, chassisWorld_jnt, mo=1)
        mc.scaleConstraint(chassisWorld_last_node, chassisWorld_jnt, mo=1)

        mc.parentConstraint(chassisIso_last_node, chassis_jnt, mo=1)
        mc.scaleConstraint(chassisIso_last_node, chassis_jnt, mo=1)

        # path jnts
        base_jnt = mc.createNode('joint', n=prefix+'_path_JNT')
        tip_jnt = mc.createNode('joint', n=prefix+'_path_steer_JNT')
        steer_jnt = mc.createNode('joint', n=prefix+'_path_end_JNT')

        mc.delete(mc.pointConstraint(rear_drift_last_node, base_jnt))
        mc.delete(mc.pointConstraint(front_drift_last_node, tip_jnt))
        mc.delete(mc.pointConstraint(front_drift_last_node, steer_jnt))

        mc.parent(tip_jnt, base_jnt)
        mc.parent(steer_jnt, tip_jnt)

        grp = mc.createNode('transform', n=base_jnt+'_GRP', p=base_jnt)
        mc.parent(chassisWorld_jnt, grp, jnt_grps[0])
        mc.parent(base_jnt, grp)

        mc.parent(chassisRoll_jnt, chassis_jnt, chassisWorld_jnt)

        mc.setAttr(grp+'.ty', 0)
        utils.set_attrs(grp, l=1, k=0)

        mc.select(base_jnt)
        mm.eval('joint -e  -oj xyz -secondaryAxisOrient yup -ch -zso;')

        # Create IK for path
        mc.xform(steer_jnt, ws=1, t=[0,0,mc.xform(front_bumper_plc, q=1, ws=1, t=1)[2]])

        ik = mc.ikHandle(sj=base_jnt, ee=steer_jnt, sol='ikSplineSolver', ccv=0, scv=0, pcv=0, rtm=1, n=prefix+'_path_IK')
        mc.parent(ik[0], jnt_grps[0])

        mc.hide(ik)

        mc.addAttr(chassisWorld_ctrl, ln='pathTravel', min=0, max=100, k=1)
        mc.addAttr(chassisWorld_ctrl, ln='pathRoll', k=1)
        mc.addAttr(chassisWorld_ctrl, ln='pathSpans', k=1)
        mc.addAttr(chassisWorld_ctrl, ln='pathLength', k=1)

        mc.connectAttr(chassisWorld_ctrl+'.pathRoll', ik[0]+'.roll')
        sr = mc.createNode('setRange', n=prefix+'_path_range')

        mc.connectAttr(chassisWorld_ctrl+'.pathLength', sr+'.oldMaxX')
        mc.connectAttr(chassisWorld_ctrl+'.pathSpans', sr+'.maxX')
        mc.connectAttr(chassisWorld_ctrl+'.pathTravel', sr+'.valueX')
        mc.connectAttr(sr+'.outValueX', ik[0]+'.offset')

        mc.parent(ik[0], grp)
        mc.setAttr(ik[0]+'.dTwistControlEnable', 1)

        mc.addAttr(base_jnt, ln='zeroValue')
        mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.tx')
        mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.ty')
        mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.tz')
        mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.rx')
        mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.ry')
        mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.rz')

        mc.connectAttr(base_jnt+'.zeroValue', steer_jnt+'.rx')
        mc.connectAttr(base_jnt+'.zeroValue', steer_jnt+'.ry')
        mc.connectAttr(base_jnt+'.zeroValue', steer_jnt+'.rz')

        mc.connectAttr(base_jnt+'.zeroValue', tip_jnt+'.rx')
        mc.connectAttr(base_jnt+'.zeroValue', tip_jnt+'.ry')
        mc.connectAttr(base_jnt+'.zeroValue', tip_jnt+'.rz')

        # add spaces
        spc = spaces.Space(chassisWorld_ctrl)
        defaults = spc.generate_default_spaces()

        spc.append_space('motionPath', base_jnt)
        spc.append_space(defaults[1][0], defaults[1][1])
        spc.append_space(defaults[2][0], defaults[2][1])
        spc.set_default_value(1)

        ctrls = [chassisIso_ctrl,
                    chassisWorld_ctrl,
                    roll_ctrl,
                    rear_drift_ctrl,
                    front_drift_ctrl,
                    l_front_sus_ctrl,
                    r_front_sus_ctrl,
                    l_rear_sus_ctrl,
                    r_rear_sus_ctrl]

        ctrls += chassisIso_offsets
        ctrls += chassisWorld_offsets
        ctrls += roll_offsets
        ctrls += rear_drift_offsets
        ctrls += front_drift_offsets
        ctrls += l_front_sus_offsets
        ctrls += r_front_sus_offsets
        ctrls += l_rear_sus_offsets
        ctrls += r_rear_sus_offsets

        utils.set_attrs(ctrls, 's', l=1, k=0)
        utils.set_attrs([roll_ctrl, front_drift_ctrl, rear_drift_ctrl]+roll_offsets+front_drift_offsets+rear_drift_offsets, 't', l=1, k=0)
        utils.set_attrs([rear_drift_ctrl, front_drift_ctrl]+front_drift_offsets+rear_drift_offsets, 'rz, rx', l=1, k=0)

        pickWalk.attribute_tag(chassisWorld_ctrl, pickWalk_parent)
        pickWalk.attribute_tag(front_drift_ctrl, chassisWorld_ctrl)
        pickWalk.attribute_tag(rear_drift_ctrl, front_drift_ctrl)
        pickWalk.attribute_tag(roll_ctrl, rear_drift_ctrl)

        pickWalk.attribute_tag(l_front_sus_ctrl, roll_ctrl)
        pickWalk.attribute_tag(r_front_sus_ctrl, roll_ctrl)
        pickWalk.attribute_tag(l_rear_sus_ctrl, roll_ctrl)
        pickWalk.attribute_tag(r_rear_sus_ctrl, roll_ctrl)
        pickWalk.attribute_tag(chassisIso_ctrl, roll_ctrl)

        #auto Steer amount
        mc.addAttr(steer_ctrl, ln='camber', k=1, min=-10, max=10)
        mc.addAttr(steer_ctrl, ln='toe', k=1, min=-10, max=10)

        mc.addAttr(steer_ctrl, ln='autoSteering', min=0, max=1, k=1)
        mc.addAttr(steer_ctrl, ln='autoWheel', min=0, max=1, k=1)
        mc.addAttr(steer_ctrl, ln='steeringAngleMax', min=0, dv=45, k=1)
        mc.addAttr(steer_ctrl, ln='suspensionExtensionMax', k=1, min=0, dv=1)
        mc.addAttr(steer_ctrl, ln='suspensionCompressionMax', k=1, min=0,dv=1)
        mc.addAttr(steer_ctrl, ln='overSteering', min=0, k=0)
        mc.addAttr(steer_ctrl, ln='autoSteerAmount', k=0)

        adl = mc.createNode('addDoubleLinear')
        mc.setAttr(adl+'.i1', mc.getAttr(steer_jnt+'.tz'))
        mc.connectAttr(steer_ctrl+'.overSteering', adl+'.i2')
        mc.connectAttr(adl+'.o', steer_jnt+'.tz')

        mc.connectAttr(tip_jnt+'.ry', steer_ctrl+'.autoSteerAmount')
        utils.set_attrs(roll_ctrl, 'ty',l=0, k=1)
        utils.set_attrs(roll_ctrl, 'ry',l=1, k=0)

        mm.eval('transformLimits -tx -10 10 -etx 1 1 '+steer_ctrl)
        utils.set_attrs(steer_ctrl, 'ty tz r s ',l=1, k=0)

        # animatable pivots
        control.create_movable_pivot(chassisWorld_ctrl)
        for c in chassisWorld_offsets:
            control.create_movable_pivot(c)

        ####################
        # compression limits

        for ct in [l_front_sus_ctrl, r_front_sus_ctrl, l_rear_sus_ctrl, r_rear_sus_ctrl ]:
            mc.transformLimits(ct, ty=[0,0], etx=[1,1], ety=[1,1], tz=[0,0], etz=[1,1])
            mc.connectAttr(steer_ctrl+'.suspensionCompressionMax', ct+'.maxTransYLimit')
            utils.connect_negative(steer_ctrl+'.suspensionExtensionMax', ct+'.minTransYLimit')
            utils.set_attrs(ct, l=1, k=0)
            utils.set_attrs(ct, 'ty', l=0., k=1)

        #########################
        #  rOLL & pitch

        ro = 1
        mc.setAttr(top_node+'.ro', ro)
        mc.setAttr(roll_ctrl+'.ro', ro)
        mc.setAttr(roll_ctrl+'_OFF.ro', ro)

        utils.set_attrs(roll_ctrl, l=1, k=0)
        utils.set_attrs(roll_ctrl, 'ty rx rz' ,l=0, k=1)

        mc.addAttr(roll_ctrl, ln='frontPitchLockout', dv=10, k=1, min=0)
        mc.addAttr(roll_ctrl, ln='rearPitchLockout', dv=10, k=1, min=0)
        mc.addAttr(roll_ctrl, ln='rollLockout', dv=10, k=1, min=0)

        f_pitch_grp = utils.get_parent(front_drift_ctrl)
        r_pitch_grp = utils.get_parent(rear_drift_ctrl)

        # negate ctrl
        mc.parentConstraint(top_node, roll_zero, mo=1)
        mc.connectAttr(roll_ctrl+'.t', roll_ctrl+'_OFF.rotatePivot')

        for a in ['ty', 'rx', 'rz']:
            utils.connect_negative(roll_ctrl+'.'+a, roll_ctrl+'_OFF.'+a)

        # lift
        mc.connectAttr(roll_ctrl+'.ty', top_node+'.ty')

        # center pitch
        cl = mc.createNode('clamp')
        mc.connectAttr(roll_ctrl+'.frontPitchLockout', cl+'.maxR')
        utils.connect_negative(roll_ctrl+'.rearPitchLockout', cl+'.minR')

        mc.connectAttr(roll_ctrl+'.rx', cl+'.inputR')
        mc.connectAttr(cl+'.outputR', top_node+'.rx', f=1)

        # center roll
        cl = mc.createNode('clamp')
        mc.connectAttr(roll_ctrl+'.rollLockout', cl+'.maxR')
        utils.connect_negative(roll_ctrl+'.rollLockout', cl+'.minR')

        mc.connectAttr(roll_ctrl+'.rz', cl+'.inputR')
        mc.connectAttr(cl+'.outputR', top_node+'.rz', f=1)

        # left roll
        cl = mc.createNode('clamp')
        adl = mc.createNode('addDoubleLinear')
        mc.setAttr(cl+'.minR', 0)
        mc.setAttr(cl+'.maxR', 999999)

        utils.connect_negative(roll_ctrl+'.rz', adl+'.i1')
        utils.connect_negative(roll_ctrl+'.rollLockout', adl+'.i2')
        mc.connectAttr(adl+'.o', cl+'.inputR')

        utils.connect_negative(cl+'.outputR', l_roll_grp+'.rz')

        # right roll
        cl = mc.createNode('clamp')
        adl = mc.createNode('addDoubleLinear')

        mc.setAttr(cl+'.minR', 0)
        mc.setAttr(cl+'.maxR', 999999)

        mc.connectAttr(roll_ctrl+'.rz', adl+'.i1')
        utils.connect_negative(roll_ctrl+'.rollLockout', adl+'.i2')
        mc.connectAttr(adl+'.o', cl+'.inputR')
        mc.connectAttr(cl+'.outputR', r_roll_grp+'.rz')

        # front pitch
        cl = mc.createNode('clamp')
        adl = mc.createNode('addDoubleLinear')

        mc.setAttr(cl+'.minR', 0)
        mc.setAttr(cl+'.maxR', 999999)

        mc.connectAttr(roll_ctrl+'.rx', adl+'.i1')
        utils.connect_negative(roll_ctrl+'.frontPitchLockout', adl+'.i2')
        mc.connectAttr(adl+'.o', cl+'.inputR')
        mc.connectAttr(cl+'.outputR', f_pitch_grp+'.rx')

        # rear pitch
        cl = mc.createNode('clamp')
        adl = mc.createNode('addDoubleLinear')
        mc.setAttr(cl+'.minR', 0)
        mc.setAttr(cl+'.maxR', 999999)

        utils.connect_negative(roll_ctrl+'.rx', adl+'.i1')
        utils.connect_negative(roll_ctrl+'.rearPitchLockout', adl+'.i2')
        mc.connectAttr(adl+'.o', cl+'.inputR')

        utils.connect_negative(cl+'.outputR', r_pitch_grp+'.rx')

        # cleanup
        mc.parent(roll_zero, top_node)
        mc.parentConstraint(r_roll_grp, chassisRoll_jnt, mo=1)
        utils.set_attrs([rear_drift_ctrl, front_drift_ctrl], 'rz', l=1, k=0)
        utils.set_attrs(roll_ctrl, 'r', l=0, k=1)

        mc.rename(chassisIso_ctrl+'_CONST', prefix+'_suspension_driver_JNT')

        mc.parentConstraint(hooks[1:], chassisIso_ctrl+'_MOCAP', mo=1)
        mc.hide(chassisRoll_jnt)

        # This finalizes the rig and creates rig sets
        self.finalize_part()
