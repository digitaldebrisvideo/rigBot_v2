# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import ikChain
from rigBot import pickWalk
from rigBot import spaces
from rigBot.partsLibrary import standardPart

class BipedArm(standardPart.StandardPart):
    """Biped arm module. Includes FK/ IK, twist, stretch and soft IK. There is also bendy, and auto clavicle functionality

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_chest_JNT".
            :ikHandleParent: (str) Optional IK handle parent for connecting to a foot part. Will default to it's own IK control if the node doesnt exist. Defaults to "".
            :numberTwistJoints: (int) Number of twist joints for the upper and lower arms Defaults to 4.
            :makeBendy: (bool) Add bendy controls. Defaults to False.

        Note:
            If using the bendy feature you will need enough twist joints to allow for proper spline deformation."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('parent', data_type='hook', default='C_chest_JNT')
        self.add_option('ikHandleParent',
                        data_type='hook',
                        default = '',
                        tool_tip="Optional IK handle parent for connecting to a "+\
                                    "foot part. Will default to it's own IK control "+\
                                    "if the node doesnt exist.")

        self.add_option('numberTwistJoints',
                        data_type='int',
                        min=0,
                        default = 4,
                        tool_tip = 'Number of twist joints for the upper and lower arms',
                        rebuild_to_modify=True)

        self.add_option('makeBendy',
                 data_type='bool',
                 default=False,
                 rebuild_to_modify=True,
                 tool_tip='Add bendy controls.')

        self.add_option('transOrientiation',
                 data_type='enum',
                 default='world',
                 enum='world:downBone',
                 tool_tip='Orient the translates on IK control to the world OR down the bone.')


        self.add_option('doubleClavicle',
                 data_type='bool',
                 default=False,
                 rebuild_to_modify=True,
                 tool_tip='Creates a second clavicle joint.')


        self.add_option('pickWalkParent',
                        data_type='string',
                        default = 'C_chest_CTL',
                        selectable=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")




    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix       = self.prefix
        options      = self.options
        mirror_value = self.mirror_value

        number_twist_jnts = options.get('numberTwistJoints')
        make_bendy = options.get('makeBendy')
        double_clav = options.get('doubleClavicle')

        # draw joints

        if double_clav:
            shoulderBase_zero, shoulderBase_plc, shoulderBase_jnt = self.guide_joint('shoulderBase', constraint_type='point')
        shoulder_zero, shoulder_plc, shoulder_jnt = self.guide_joint('shoulder', constraint_type='point')
        up_arm_zero, up_arm_plc, up_arm_jnt = self.guide_joint('upArm', constraint_type='point')
        lo_arm_zero, lo_arm_plc, lo_arm_jnt = self.guide_joint('loArm', constraint_type='point')
        wrist_zero, wrist_plc, wrist_jnt = self.guide_joint('wrist', constraint_type='point')
        wrist_end_zero, wrist_end_plc, wrist_end_jnt = self.guide_joint('wrist_end', constraint_type='point')

        ik_driver_plc_zero, ik_driver_plc = self.guide_joint('arm_IK_handle_driver', placer_only=1)

        mc.setAttr(ik_driver_plc+'.radius', 1)
        mc.setAttr(ik_driver_plc+'.color', 0.96, 0.71, .01)
        mc.setAttr(ik_driver_plc+'.otherType',  'Leg IK Driver', type='string');
        mc.setAttr(ik_driver_plc+'.type', 18)

        mc.parentConstraint(wrist_jnt, ik_driver_plc_zero)
        mc.setAttr(ik_driver_plc+'.offsetTranslateX', self.mirror_value*0.25)

        utils.set_attrs(ik_driver_plc, l=1, k=0)

        # position
        if double_clav:
            mc.setAttr(shoulderBase_zero+'.tx', -0.5)
        mc.setAttr(shoulder_zero+'.tx', 0.5)
        mc.setAttr(up_arm_zero+'.tx', 2)
        mc.setAttr(lo_arm_zero+'.tx', 4)
        mc.setAttr(lo_arm_zero+'.tz', -0.5)
        mc.setAttr(wrist_zero+'.tx', 6)
        mc.setAttr(wrist_end_zero+'.tx', 6.5)

        # Constraint clavicle


        # Constraint clavicle
        if double_clav:
            mc.aimConstraint(shoulder_plc,
                             shoulderBase_jnt,
                             n=shoulderBase_jnt+'_ac',
                             aim=[mirror_value,0,0],
                             u=[0,1,0],
                             wu=[0,1,0],
                             wut='objectRotation',
                             wuo=shoulderBase_plc)

        # Constraint shoulder
        mc.aimConstraint(up_arm_plc,
                         shoulder_jnt,
                         n=shoulder_jnt+'_ac',
                         aim=[mirror_value,0,0],
                         u=[0,1,0],
                         wu=[0,1,0],
                         wut='objectRotation',
                         wuo=shoulder_plc)

        # Constraint upArm
        mc.aimConstraint(lo_arm_plc,
                         up_arm_jnt,
                         n=up_arm_jnt+'_ac',
                         aim=[mirror_value,0,0],
                         u=[0,0,mirror_value],
                         wut='object',
                         wuo=wrist_plc)

        # Constraint loArm
        mc.aimConstraint(wrist_plc,
                         lo_arm_jnt,
                         n=lo_arm_jnt+'_ac',
                         aim=[mirror_value,0,0],
                         u=[0,0,mirror_value],
                         wut='object',
                         wuo=up_arm_plc)

        mc.aimConstraint(wrist_end_plc,
                         wrist_jnt,
                         n=wrist_jnt+'_ac',
                         aim=[mirror_value,0,0],
                         u=[0,1,0],
                         wu=[0,1,0],
                         wut='objectRotation',
                         wuo=wrist_plc)

        # parent jnts
        if double_clav:
            mc.parent(shoulder_jnt, shoulderBase_jnt)
        mc.parent(up_arm_jnt, shoulder_jnt)
        mc.parent(lo_arm_jnt, up_arm_jnt)
        mc.parent(wrist_jnt, lo_arm_jnt)
        mc.parent(wrist_end_jnt, wrist_jnt)

        mc.xform(wrist_end_jnt, a=1, ro=[0,0,0])
        mc.setAttr(wrist_end_jnt+'.jo', 0,0,0)

        # Create twist jnts
        div = 1.0 / (number_twist_jnts+1)

        up_twist_zeros, up_twist_plcs, up_twist_jnts = [], [], []
        lo_twist_zeros, lo_twist_plcs, lo_twist_jnts = [], [], []

        for i in range(number_twist_jnts):

            # setup upper arm jnts
            letter = utils.letters[i]
            zero, plc, jnt = self.guide_joint('upArm_twist_'+letter, constraint_type='point')

            if up_twist_jnts:
                mc.parent(jnt, up_twist_jnts[-1])
            else:
                mc.parent(jnt, up_arm_jnt)

            up_twist_jnts.append(jnt)
            up_twist_plcs.append(plc)
            up_twist_zeros.append(zero)

            mc.pointConstraint(up_arm_plc, plc, weight=1.0-(div*(i+1)))
            mc.pointConstraint(lo_arm_plc, plc, weight=(div*(i+1)))
            mc.orientConstraint(up_arm_jnt, plc)

            mc.xform(jnt, a=1, ro=[0,0,0])
            mc.setAttr(jnt+'.jo', 0,0,0)

            utils.set_attrs(plc, 't r s', l=1, k=0)

            # setup uplowerper arm jnts
            letter = utils.letters[i]
            zero, plc, jnt = self.guide_joint('loArm_twist_'+letter, constraint_type='point')

            if lo_twist_jnts:
                mc.parent(jnt, lo_twist_jnts[-1])
            else:
                mc.parent(jnt, lo_arm_jnt)

            lo_twist_jnts.append(jnt)
            lo_twist_plcs.append(plc)
            lo_twist_zeros.append(zero)

            mc.pointConstraint(lo_arm_plc, plc, weight=1.0-(div*(i+1)))
            mc.pointConstraint(wrist_plc, plc, weight=(div*(i+1)))
            mc.orientConstraint(lo_arm_jnt, plc)

            mc.xform(jnt, a=1, ro=[0,0,0])
            mc.setAttr(jnt+'.jo', 0,0,0)

            utils.set_attrs(plc, 't r s', l=1, k=0)

        if up_twist_jnts:
            mc.parent(lo_arm_jnt, up_twist_jnts[-1])
            for plc in up_twist_plcs:
                mc.setAttr(plc+'.radius', 0.7)

        if lo_twist_jnts:
            mc.parent(wrist_jnt, lo_twist_jnts[-1])
            for plc in lo_twist_plcs:
                mc.setAttr(plc+'.radius', 0.7)

        #lock plcs
        utils.set_attrs([up_arm_plc, lo_arm_plc], 'r s', l=1, k=0)

        # Create ctrls
        up_arm_fk_zero, up_arm_fk_ctrl = self.guide_ctrl(name='upArm_FK',
            shape='circle',
            color='light_blue',
            driver=up_arm_jnt,
            allow_offset_ctrls=False,
            axis='X')

        lo_arm_fk_zero, lo_arm_fk_ctrl = self.guide_ctrl(name='loArm_FK',
            shape='circle',
            color='light_blue',
            driver=lo_arm_jnt,
            allow_offset_ctrls=False,
            axis='X')

        wrist_fk_zero, wrist_fk_ctrl = self.guide_ctrl(name='wrist_FK',
            shape='circle',
            color='light_blue',
            driver=wrist_jnt,
            allow_offset_ctrls=False,
            axis='X')

        mc.xform(wrist_fk_ctrl+'.cv[*]', r=1, t=[mirror_value*0.25,0,0])

        color = 'green'
        if mirror_value < 0:
            color = 'red'

        arm_ik_zero, arm_ik_ctrl = self.guide_ctrl('arm_IK',
            shape='cube',
            color=color,
            scale=[0.8]*3,
            driver=wrist_jnt)

        wrist_ik_zero, wrist_ik_ctrl = self.guide_ctrl(name='wrist_IK',
            shape='circle',
            color=color,
            driver=wrist_jnt,
            axis='X')

        mc.xform(wrist_ik_ctrl+'.cv[*]', r=1, t=[mirror_value*0.5,0,0])

        pv_zero, pv_ctrl = self.guide_ctrl('arm_PV', shape='cube', color=color, scale=[0.2]*3, allow_offset_ctrls=0, create_pivot=0)
        pv_pivot = utils.get_parent(pv_ctrl)
        utils.set_attrs(pv_pivot, 't', l=0)

        grp = utils.get_parent(pv_pivot)
        noxform = utils.get_parent(pv_zero).replace('CTLS', 'NOX')

        # Constraint pv
        mc.pointConstraint(up_arm_jnt, pv_zero, n=pv_zero+'_pc')
        mc.aimConstraint(wrist_jnt,
                         pv_zero,
                         n=pv_zero+'_ac',
                         aim=[mirror_value,0,0],
                         u=[0,0,-mirror_value],
                         wut='object',
                         wuo=lo_arm_jnt)

        mc.pointConstraint(lo_arm_jnt, grp, n=grp+'_pc')
        mc.setAttr(pv_pivot+'.tz', -10)
        mc.orientConstraint(noxform, pv_ctrl, n=pv_ctrl+'_pc')

        utils.set_attrs([pv_ctrl, pv_zero, grp, pv_pivot], 'r t s v', l=1, k=0)
        utils.set_attrs(pv_ctrl, 'tx tz s ', l=0, k=1)

        shoulder_fk_zero, shoulder_fk_ctrl = self.guide_ctrl(name='shoulder',
            shape='semi_circle',
            color=color,
            scale=[1.5,1.5,3],
            driver=shoulder_jnt,
            axis='Y')

        mc.xform(shoulder_fk_ctrl+'.cv[*]', r=1, ro=[0,-90,0])

        if double_clav:
            clavA_zero, clavA_ctrl = self.guide_ctrl(name='clavicleA',
                shape='cube',
                color=color,
                scale=[0.5,0.5,2],
                driver=shoulderBase_jnt,
                axis='Y')

            #mc.xform(clavA_ctrl+'.cv[*]', r=1, ro=[0,-90,0])

            clavB_zero, clavB_ctrl = self.guide_ctrl(name='clavicleB',
                shape='cube',
                color=color,
                scale=[0.5,0.5,2],
                driver=shoulder_jnt,
                axis='Y')





        if make_bendy:
            baCtrl = self.guide_ctrl(name='bendyArm_A', shape='star', color='pink', axis='X')
            bbCtrl = self.guide_ctrl(name='bendyArm_B', shape='star', color='pink', axis='X')
            bcCtrl = self.guide_ctrl(name='bendyArm_C', shape='star', color='pink', axis='X')

            mc.parentConstraint(up_arm_jnt, baCtrl[0], n=baCtrl[0]+'_prc')
            mc.parentConstraint(lo_arm_jnt, bbCtrl[0], n=bbCtrl[0]+'_prc')
            mc.parentConstraint(lo_arm_jnt, bcCtrl[0], n=bcCtrl[0]+'_prc')

            mc.pointConstraint(up_arm_jnt, lo_arm_jnt, baCtrl[1]+'_CONST', n=baCtrl[1]+'_CONST_pc')
            mc.pointConstraint(wrist_jnt, lo_arm_jnt, bcCtrl[1]+'_CONST', n=bcCtrl[1]+'_CONST_pc')
            oc = mc.orientConstraint(up_arm_jnt, lo_arm_jnt, bbCtrl[1]+'_CONST', n=bbCtrl[1]+'_CONST_oc')
            mc.setAttr(oc[0]+'.interpType', 2)

            utils.set_attrs(baCtrl+bbCtrl+bcCtrl)
            utils.set_attrs([baCtrl[-1], bbCtrl[-1], bcCtrl[-1]], 't r s', k=1, l=0)

        # ik fk switch ctrl
        switch_zero, switch_ctrl = self.guide_ctrl(name='arm_IK_switch', shape='pin_gear', color='lavendar', driver=wrist_jnt)
        mc.setAttr(arm_ik_ctrl+'.numOffsetCtrls', 1)

        line = mc.createNode('transform', n=pv_ctrl+'_line_REF', p=utils.get_parent(pv_zero))
        control.create_driven_shape(line, [pv_ctrl, lo_arm_jnt])
        utils.set_draw_override(line, 1)

        # This finalizes your guide.
        self.finalize_guide()

    def build_rig(self):
        """This builds your anim rig."""

        # create rig part top nodes
        self.create_part_master()

        # Get all the relevant part info
        prefix            = self.prefix
        options           = self.options
        anim_ctrls        = self.anim_ctrls
        bind_joints       = self.bind_joints
        world_scale_attr  = self.hooks[0]+'.worldScale'
        hooks             = self.hooks
        ctrl_grps         = self.ctrl_grps
        jnt_grps          = self.jnt_grps

        number_twist_jnts = options.get('numberTwistJoints')
        parent = options.get('parent')
        make_bendy = options.get('makeBendy')
        pickWalk_parent = options.get('pickWalkParent')
        double_clav = options.get('doubleClavicle')

        world_orient_trans=options.get('transOrientiation')


        shoulderBase_jnt = prefix+'_shoulderBase_JNT'
        shoulder_jnt = prefix+'_shoulder_JNT'
        up_arm_jnt = prefix+'_upArm_JNT'
        lo_arm_jnt = prefix+'_loArm_JNT'
        wrist_jnt = prefix+'_wrist_JNT'
        wrist_end_jnt = prefix+'_wrist_end_JNT'

        up_arm_twist_jnts = mc.ls(prefix+'_upArm_twist_*JNT')
        lo_arm_twist_jnts = mc.ls(prefix+'_loArm_twist_*JNT')

        # Create FK ctrls
        if double_clav:
            name = prefix+'_clavicleA_CTL'
            clavA_zero, clavA_ctrl, clavA_offsets, clavA_last_node = self.anim_ctrl(name)

            name = prefix+'_clavicleB_CTL'
            clavB_zero, clavB_ctrl, clavB_offsets, clavB_last_node = self.anim_ctrl(name)

        name = prefix+'_shoulder_CTL'
        shoulder_zero, shoulder_ctrl, shoulder_offsets, shoulder_last_node = self.anim_ctrl(name)

        name = prefix+'_upArm_FK_CTL'
        up_arm_fk_zero, up_arm_fk_ctrl, up_arm_fk_offsets, up_arm_fk_last_node = self.anim_ctrl(name)

        name = prefix+'_loArm_FK_CTL'
        lo_arm_fk_zero, lo_arm_fk_ctrl, lo_arm_fk_offsets, lo_arm_fk_last_node = self.anim_ctrl(name)

        name = prefix+'_wrist_FK_CTL'
        wrist_fk_zero, wrist_fk_ctrl, wrist_fk_offsets, wrist_fk_last_node = self.anim_ctrl(name)

        # Create IK ctrls
        name = prefix+'_arm_IK_CTL'
        arm_ik_zero, arm_ik_ctrl, arm_ik_offsets, arm_ik_last_node = self.anim_ctrl(name, node_type='joint')

        arm_ik_last_node = mc.createNode('transform', p=arm_ik_last_node, n=prefix+'_arm_IK_handle_driver_JNT')

        name = prefix+'_wrist_IK_CTL'
        wrist_ik_zero, wrist_ik_ctrl, wrist_ik_offsets, wrist_ik_last_node = self.anim_ctrl(name)

        name = prefix+'_arm_PV_CTL'
        loc = utils.snap_locator(name+'_REF')
        mc.setAttr(loc+'.sx', self.mirror_value)
        pv_zero, pv_ctrl, pv_offsets, pv_last_node = self.anim_ctrl(name, match_position=loc)

        name = prefix+'_arm_IK_switch_CTL'
        switch_zero, switch_ctrl, switch_offsets, switch_last_node = self.anim_ctrl(name)

        mc.delete(loc)

        up_arm_grp = mc.createNode('transform', n=up_arm_jnt+'_GRP', p=shoulder_jnt)
        mc.delete(mc.parentConstraint(up_arm_jnt, up_arm_grp))
        mc.parent(up_arm_jnt, up_arm_grp)

        if make_bendy:
            bendyArmACtrl = self.anim_ctrl(prefix+'_bendyArm_A_CTL')
            bendyArmBCtrl = self.anim_ctrl(prefix+'_bendyArm_B_CTL')
            bendyArmCCtrl = self.anim_ctrl(prefix+'_bendyArm_C_CTL')
            mc.parent(bendyArmACtrl[0], bendyArmBCtrl[0], bendyArmCCtrl[0], ctrl_grps[0])

        #  here --------
        if double_clav:
            mc.parent(shoulder_zero, shoulderBase_jnt)
            mc.select(shoulder_zero, shoulder_ctrl+'_OFF', shoulder_ctrl+'_MOCAP', shoulder_ctrl+'_CONST', shoulder_ctrl, shoulder_offsets)
            utils.set_attrs(l=0, k=1)
            mc.makeIdentity(apply=1, t=1, r=1, s=1, n=0, pn=1)
            mc.xform(piv=[0,0,0])
            mc.parent(shoulder_zero ,w = True)


        # orient arm ik ctrl

        tmp_grp = mc.group(arm_ik_ctrl)
        mc.parent(tmp_grp, w=1)

        mc.xform(arm_ik_zero, a=1, ro=[0,0,0])
        mc.setAttr(arm_ik_zero+'.s', self.mirror_value,1,1)

        utils.set_attrs(arm_ik_ctrl, 'jo', l=0)
        mc.parent(arm_ik_ctrl, arm_ik_ctrl+'_OFF')
        mc.delete(tmp_grp)

        if world_orient_trans == 'downBone':
            utils.set_attrs(arm_ik_ctrl+'_ZERO', 'ry', k=1, l=0)
            utils.set_attrs(arm_ik_ctrl, 'joy', k=1, l=0)
            mc.setAttr(arm_ik_ctrl+'_ZERO.ry', mc.getAttr(arm_ik_ctrl+'.joy'))

            utils.set_attrs(arm_ik_ctrl+'_ZERO', 'ry', k=0, l=1)
            utils.set_attrs(arm_ik_ctrl, 'joy', k=0, l=1)

        # parent fk ctrls
        if double_clav:
            mc.parent(clavB_zero, clavA_ctrl)
            mc.parent(up_arm_fk_zero, clavB_ctrl)
            mc.parent(lo_arm_fk_zero, up_arm_fk_ctrl)
            mc.parent(wrist_fk_zero, lo_arm_fk_ctrl)
        else:
            mc.parent(up_arm_fk_zero, shoulder_ctrl)
            mc.parent(lo_arm_fk_zero, up_arm_fk_ctrl)
            mc.parent(wrist_fk_zero, lo_arm_fk_ctrl)

        # parent ik ctrls
        mc.parent(wrist_ik_zero, arm_ik_last_node)

        # NOW create ik fk chain setup
        up_arm_ik_jnt = mc.duplicate(up_arm_jnt, po=1, n=up_arm_jnt.replace('upArm', 'upArm_IK'))[0]
        lo_arm_ik_jnt = mc.duplicate(lo_arm_jnt, po=1, n=lo_arm_jnt.replace('loArm', 'loArm_IK'))[0]
        wrist_ik_jnt = mc.duplicate(wrist_jnt, po=1, n=wrist_jnt.replace('wrist', 'wrist_IK'))[0]

        mc.parent(lo_arm_ik_jnt, up_arm_ik_jnt)
        mc.parent(wrist_ik_jnt, lo_arm_ik_jnt)

        mc.orientConstraint(up_arm_fk_last_node, up_arm_ik_jnt, mo=1)
        mc.orientConstraint(wrist_fk_last_node, wrist_ik_jnt, mo=1)

        ori_par = mc.createNode('transform', p=lo_arm_ik_jnt, n=lo_arm_ik_jnt+'_orient_drv_GRP')
        ori = mc.createNode('transform', p=ori_par, n=lo_arm_ik_jnt+'_orient_DRV')
        mc.parent(ori_par, lo_arm_fk_zero)

        mc.orientConstraint(lo_arm_fk_ctrl, ori, mo=1)
        mc.connectAttr(ori+'.r', lo_arm_ik_jnt+'.r')

        ik_handle = mc.ikHandle(sj=up_arm_ik_jnt, ee=wrist_ik_jnt, s='sticky', n=prefix+'_arm_IK')[0]
        mc.poleVectorConstraint(pv_ctrl, ik_handle)

        ikChain.create_fk_ik_switch(switch_ctrl, ik_handle, up_arm_fk_zero, [arm_ik_zero, pv_zero])
        mc.parent(ik_handle, arm_ik_last_node)
        mc.setAttr(switch_ctrl+'.IK', 1)
        mc.hide(ik_handle)

        mc.addAttr(arm_ik_ctrl, ln='twist', k=1)

        mc.connectAttr(arm_ik_ctrl+'.twist', ik_handle+'.twist')
        if self.mirror_value < 0.0:
            utils.connect_negative(arm_ik_ctrl+'.twist', ik_handle+'.twist')

        # Create soft ik

        # new case for new hook
        ik_handle_grp = mc.createNode('transform', p=arm_ik_last_node, n=ik_handle+'_GRP')
        mc.parent(ik_handle_grp, jnt_grps[1])
        mc.parent(ik_handle, ik_handle_grp)
        mc.parentConstraint(arm_ik_last_node, hooks[1], mo=1)

        ik_joints = [up_arm_ik_jnt, lo_arm_ik_jnt, wrist_ik_jnt]
        ik_ctrl = arm_ik_ctrl

        ik_handle_parent = ikChain.create_soft_ik(ik_ctrl, ik_joints, ik_handle )

        # Create IK wrist orient switch
        jnt_follow_par = mc.duplicate(wrist_ik_ctrl+'_OFF', po=1, n=wrist_ik_zero+'_jnt_follow_par')[0]
        ctrl_follow_par = mc.duplicate(wrist_ik_ctrl+'_OFF', po=1, n=wrist_ik_zero+'_ikCtrl_follow_par')[0]

        jnt_follow = mc.duplicate(wrist_ik_ctrl+'_OFF', po=1, n=wrist_ik_zero+'_jnt_follow')[0]
        ctrl_follow = mc.duplicate(wrist_ik_ctrl+'_OFF', po=1, n=wrist_ik_zero+'_ikCtrl_follow')[0]

        mc.parent(ctrl_follow, ctrl_follow_par)
        mc.parent(jnt_follow, jnt_follow_par)
        mc.parent(jnt_follow_par, lo_arm_ik_jnt)

        oc = mc.orientConstraint(jnt_follow, ctrl_follow, wrist_ik_ctrl+'_OFF')[0]
        mc.setAttr(oc+'.interpType', 2)

        mc.addAttr(arm_ik_ctrl, ln='isolateWristOrientation', min=0, max=1, k=1)

        mdl = mc.createNode('multDoubleLinear', n=oc+'_mdl')
        mc.connectAttr(switch_ctrl+'.IK', mdl+'.input1', f=1)
        mc.connectAttr(arm_ik_ctrl+'.isolateWristOrientation', mdl+'.input2', f=1)

        mc.connectAttr(mdl+'.output', oc+'.w0')
        utils.connect_reverse(oc+'.w0', oc+'.w1')

        # connect ik blend to wrist orientConstraint
        oc = mc.orientConstraint(wrist_ik_last_node, wrist_ik_jnt, mo=1)[0]
        mc.setAttr(oc+'.interpType', 2)

        mc.connectAttr(switch_ctrl+'.IK', oc+'.w1')
        utils.connect_reverse(switch_ctrl+'.IK', oc+'.w0')

        # setup uparm FK orient
        up_arm_fk_orient_grp = up_arm_fk_ctrl+'_CONST'
        iso_follow_par = mc.duplicate(up_arm_fk_orient_grp, po=1, n=up_arm_fk_orient_grp+'_isolate_par')[0]
        iso_follow = mc.duplicate(up_arm_fk_orient_grp, po=1, n=up_arm_fk_orient_grp+'_isolate')[0]

        mc.parent(iso_follow, iso_follow_par)
        mc.parent(iso_follow_par, shoulder_zero)

        oc = mc.orientConstraint(up_arm_fk_zero, up_arm_fk_orient_grp, mo=1)[0]
        oc = mc.orientConstraint(iso_follow, up_arm_fk_orient_grp, mo=1)[0]
        mc.setAttr(oc+'.interpType', 2)

        mc.addAttr(up_arm_fk_ctrl, ln='isolateArmOrientation', min=0, max=1, k=1)
        mc.connectAttr(up_arm_fk_ctrl+'.isolateArmOrientation', oc+'.w1')
        utils.connect_reverse(oc+'.w1', oc+'.w0')

        # constraint the clavicle joint to the
        if double_clav:
            mc.parentConstraint(clavB_last_node, shoulder_jnt, mo=1)
            mc.parentConstraint(clavA_last_node, shoulderBase_jnt, mo = 1)
        else:
            mc.parentConstraint(shoulder_last_node, shoulder_jnt, mo=1)

        # Create twist
        if up_arm_twist_jnts:
            ikChain.upper_twist(utils.get_parent(up_arm_ik_jnt), up_arm_ik_jnt, lo_arm_ik_jnt, up_arm_jnt, lo_arm_jnt, up_arm_twist_jnts)
            ikChain.lower_twist(lo_arm_ik_jnt, wrist_ik_jnt, lo_arm_jnt, lo_arm_twist_jnts, wrist_jnt)

            ikChain.stretch_twist_jnts(up_arm_ik_jnt, lo_arm_ik_jnt, up_arm_twist_jnts)
            ikChain.stretch_twist_jnts(lo_arm_ik_jnt, wrist_ik_jnt, lo_arm_twist_jnts)

        else:
            mc.parentConstraint(up_arm_ik_jnt, up_arm_jnt ,mo=1)
            mc.parentConstraint(lo_arm_ik_jnt, lo_arm_jnt ,mo=1)
            mc.parentConstraint(wrist_ik_jnt, wrist_jnt ,mo=1)

        # create stretch
        ikChain.biped_stretch(arm_ik_ctrl,
                      arm_ik_last_node,
                      pv_ctrl,
                      switch_ctrl,
                      up_arm_fk_ctrl,
                      lo_arm_fk_ctrl,
                      wrist_fk_ctrl,
                      up_arm_ik_jnt,
                      lo_arm_ik_jnt,
                      wrist_ik_jnt,
                      ik_handle,
                      pin_attr_name='pinElbow',
                      shift_attr_name='shiftElbow')

        control.create_driven_shape(pv_ctrl, lo_arm_ik_jnt, replace=False)

        # lastly set up auto clavicle
        if double_clav:
            mc.parent(shoulderBase_jnt, jnt_grps[0])
        else:
            mc.parent(shoulder_jnt, jnt_grps[0])

        # Create all joints
        if double_clav:
            auto_shoulerBase = mc.duplicate(shoulderBase_jnt, po=1, n=shoulderBase_jnt+'_AUTO')[0]
        auto_shoulder = mc.duplicate(shoulder_jnt, po=1, n=shoulder_jnt+'_AUTO')[0]
        auto_lo_arm = mc.duplicate(lo_arm_jnt, po=1, n=lo_arm_jnt+'_AUTO')[0]
        auto_wrist = mc.duplicate(wrist_jnt, po=1, n=wrist_jnt+'_AUTO')[0]

        up_auto_shoulder = mc.duplicate(shoulder_jnt, po=1, n=shoulder_jnt+'_upper_AUTO')[0]
        up_auto_lo_arm = mc.duplicate(lo_arm_jnt, po=1, n=lo_arm_jnt+'_upper_AUTO')[0]

        mc.parent(auto_lo_arm, auto_shoulder)
        mc.parent(auto_wrist, auto_lo_arm)
        mc.parent(up_auto_lo_arm, up_auto_shoulder)


        # Create ik
        up_auto_ik_handle = mc.ikHandle(sj=up_auto_shoulder, ee=up_auto_lo_arm, s='sticky', n=prefix+'_arm_auto_clav_upper_IK')[0]
        auto_ik_handle = mc.ikHandle(sj=auto_shoulder, ee=auto_wrist, s='sticky', n=prefix+'_arm_auto_clav_IK')[0]

        mc.parent(auto_ik_handle, ik_handle_grp)
        mc.parent(up_auto_ik_handle, auto_shoulder)
        mc.setAttr(up_auto_ik_handle+'.poleVector', 0,0,0)

        mc.poleVectorConstraint(pv_ctrl, auto_ik_handle)
        mc.connectAttr(arm_ik_ctrl+'.twist', auto_ik_handle+'.twist')
        if self.mirror_value < 0.0:
            utils.connect_negative(arm_ik_ctrl+'.twist', auto_ik_handle+'.twist')

        # Create attrs
        if double_clav:
            mc.addAttr(shoulder_ctrl, ln = 'shoulderInfluence', min = 0, max = 10, k = 1)
            mc.addAttr(shoulder_ctrl, ln = 'shoulderBaseInfluence', min = 0, max = 10, k = 1)

        mc.addAttr(shoulder_ctrl, ln='autoClavicle', min=0, max=1, k=1)

        mc.addAttr(shoulder_ctrl, ln='clavUpLimit', min=0, dv=90, k=1)
        mc.addAttr(shoulder_ctrl, ln='clavDownLimit', min=0, dv=45, k=1)
        mc.addAttr(shoulder_ctrl, ln='clavFrontLimit', min=0, dv=90, k=1)
        mc.addAttr(shoulder_ctrl, ln='clavBackLimit', min=0, dv=90, k=1)

        mc.connectAttr(shoulder_ctrl+'.clavUpLimit', up_auto_shoulder+'.maxRotZLimit')
        mc.connectAttr(shoulder_ctrl+'.clavBackLimit', up_auto_shoulder+'.maxRotYLimit')
        utils.connect_negative(shoulder_ctrl+'.clavDownLimit', up_auto_shoulder+'.minRotZLimit')
        utils.connect_negative(shoulder_ctrl+'.clavFrontLimit', up_auto_shoulder+'.minRotYLimit')

        mc.setAttr(up_auto_shoulder+'.maxRotYLimitEnable', 1)
        mc.setAttr(up_auto_shoulder+'.minRotYLimitEnable', 1)
        mc.setAttr(up_auto_shoulder+'.maxRotZLimitEnable', 1)
        mc.setAttr(up_auto_shoulder+'.minRotZLimitEnable', 1)

        mc.hide(auto_shoulder, up_auto_shoulder, up_auto_ik_handle, auto_ik_handle)

        #adding double clavicle control influence
        if double_clav:
            pma = mc.createNode('plusMinusAverage', name = shoulder_ctrl + '_pma')
            mc.setAttr(pma + '.operation', 2)
            mc.setAttr(pma + '.input2D[0].input2Dx', 10)
            mc.connectAttr(shoulder_ctrl +'.shoulderInfluence' , pma + '.input2D[1].input2Dx')
            mc.connectAttr(pma + '.output2D.output2Dx', shoulder_ctrl +'.shoulderBaseInfluence')
            mc.setAttr(shoulder_ctrl + '.shoulderBaseInfluence', l = True)
            mc.setAttr(shoulder_ctrl + '.shoulderInfluence', 6)

            fract = mc.createNode('multiplyDivide', n = clavB_ctrl + '.md')
            mc.setAttr(fract+ '.input2', .1, .1, .1)
            mc.connectAttr(shoulder_ctrl +'.shoulderInfluence',fract + '.input1X')
            mc.connectAttr(shoulder_ctrl +'.shoulderInfluence',fract + '.input1Y')
            mc.connectAttr(shoulder_ctrl +'.shoulderInfluence',fract + '.input1Z')
            md = mc.createNode('multiplyDivide', n = clavB_ctrl+ 'Rotation.md')
            mc.connectAttr(shoulder_ctrl +'.rotate', md + '.input1')
            mc.connectAttr(fract + '.output', md + '.input2')
            mc.connectAttr( md + '.output', clavB_ctrl + '_MOCAP.rotate')


            fract = mc.createNode('multiplyDivide', n = clavA_ctrl +'.md')
            mc.setAttr(fract+ '.input2', .1, .1, .1)
            mc.connectAttr(shoulder_ctrl +'.shoulderBaseInfluence',fract + '.input1X')
            mc.connectAttr(shoulder_ctrl +'.shoulderBaseInfluence',fract + '.input1Y')
            mc.connectAttr(shoulder_ctrl +'.shoulderBaseInfluence',fract + '.input1Z')
            md = mc.createNode('multiplyDivide', n = clavA_ctrl + 'Rotation.md')
            mc.connectAttr(shoulder_ctrl +'.rotate', md + '.input1')
            mc.connectAttr(fract + '.output', md + '.input2')
            mc.connectAttr( md + '.output', clavA_ctrl + '_MOCAP.rotate')

        auto_follow_grp = mc.duplicate(shoulder_ctrl+'_CONST', po=1, n=shoulder_ctrl+'_AUTO_GRP')[0]
        auto_follow = mc.duplicate(shoulder_ctrl+'_CONST', po=1, n=shoulder_ctrl+'_AUTO')[0]
        stable = mc.duplicate(shoulder_ctrl+'_CONST', po=1, n=shoulder_ctrl+'_STABLE')[0]

        mc.parent(auto_follow, auto_follow_grp)
        mc.parent(auto_follow_grp, up_auto_shoulder)

        oc = mc.orientConstraint(stable, auto_follow, shoulder_ctrl+'_CONST')[0]
        mc.connectAttr(shoulder_ctrl+'.autoClavicle', oc+'.w1')
        utils.connect_reverse(shoulder_ctrl+'.autoClavicle', oc+'.w0')

        mc.setAttr(oc+'.interpType', 2)

        if make_bendy:

            mc.parentConstraint(up_arm_ik_jnt, bendyArmACtrl[0], mo=1, n=bendyArmACtrl[0]+'_prc')
            mc.pointConstraint(up_arm_ik_jnt, lo_arm_ik_jnt, bendyArmACtrl[1]+'_CONST', mo=1, n=bendyArmACtrl[1]+'_CONST_pc')

            mc.parentConstraint(lo_arm_ik_jnt, bendyArmCCtrl[0], mo=1, n=bendyArmCCtrl[0]+'_prc')
            mc.pointConstraint(lo_arm_ik_jnt, wrist_ik_jnt, bendyArmCCtrl[1]+'_CONST', mo=1, n=bendyArmCCtrl[1]+'_CONST_pc')

            mc.parentConstraint(lo_arm_ik_jnt, bendyArmBCtrl[0], mo=1, n=bendyArmBCtrl[0]+'_prc')
            oc = mc.orientConstraint(up_arm_ik_jnt, lo_arm_ik_jnt, bendyArmBCtrl[1]+'_CONST', mo=1, n=bendyArmBCtrl[1]+'_CONST_pc')[0]
            mc.setAttr(oc+'.interpType', 2)

            bendy_joints_drivers = [up_arm_jnt]+up_arm_twist_jnts + [lo_arm_jnt]+lo_arm_twist_jnts+[wrist_jnt]
            bendy_ctrls = [bendyArmACtrl[-1], bendyArmBCtrl[-1], bendyArmCCtrl[-1]]
            noxform_grp = self.noxform_grp

            ikChain.biped_bendy(bendy_joints_drivers, bendy_ctrls, False, noxform_grp, ctrl_driver=bendyArmBCtrl[1])


        # clean shit up now
        mc.hide(up_arm_ik_jnt)

        mc.parentConstraint(wrist_jnt, switch_zero, mo=1)
        if double_clav:
            mc.parent(clavA_zero, ctrl_grps[0])
        mc.parent(shoulder_zero, arm_ik_zero, pv_zero, switch_zero, ctrl_grps[0])

        utils.set_attrs([up_arm_fk_ctrl, wrist_ik_ctrl, lo_arm_fk_ctrl, wrist_fk_ctrl], 't s v', l=1, k=0)
        utils.set_attrs(lo_arm_fk_ctrl, 'ro', l=1, k=0)
        utils.set_attrs(pv_ctrl, 'r s v ro', l=1, k=0)
        utils.set_attrs(lo_arm_fk_ctrl, 'ro', l=1, k=0)
        utils.set_attrs(switch_ctrl, 't r s v ro', l=1, k=0)
        utils.set_attrs(shoulder_ctrl, 's', l=1, k=0)

        utils.set_attrs(arm_ik_offsets+[arm_ik_ctrl], ' s v ro jo radius', l=1, k=0, cb=0)
        for c in arm_ik_offsets+[arm_ik_ctrl]:
            mc.setAttr(c+'.radius', k=0, cb=0)

        # create pv aim at space
        aim_drv = mc.duplicate(up_arm_ik_jnt, n=pv_ctrl+'_AIM_DRV', po=1)[0]
        aim_drv_end = mc.duplicate(lo_arm_ik_jnt, n=pv_ctrl+'_AIM_DRV_end', po=1)[0]
        aim_drv_ik = mc.duplicate(wrist_ik_jnt, n=pv_ctrl+'_IK_DRV_end', po=1)[0]

        pos = mc.createNode('transform', n=aim_drv+'_POS', p=aim_drv)
        mc.parent(pos, shoulder_zero)
        mc.parent(aim_drv, jnt_grps[0])
        mc.parent(aim_drv_end, aim_drv)
        mc.setAttr(aim_drv_end+'.tx', mc.getAttr(aim_drv_end+'.tx')*0.05)
        mc.pointConstraint(pos, aim_drv)

        aim_ik = mc.ikHandle(sj=aim_drv, ee=aim_drv_end, n=aim_drv+'_IK', sol='ikSCsolver', s='sticky')[0]
        mc.pointConstraint(aim_drv_ik, aim_ik)

        mc.parent(aim_drv_ik ,jnt_grps[1])
        mc.parent(aim_ik, utils.get_parent(aim_drv))

        mc.hide(aim_drv, aim_drv_end, aim_ik, aim_drv_ik)

        # spaces
        spaces.tag(arm_ik_ctrl, default=0)
        spaces.tag(pv_ctrl, 'arm:'+aim_drv, default=1)

        jnts = [shoulder_jnt, up_arm_jnt]+up_arm_twist_jnts+[lo_arm_jnt]+lo_arm_twist_jnts+[wrist_jnt, wrist_end_jnt]
        #utils.create_cfx_curves(jnts, self.prefix+'_'+self.part_type)

        # movable pivot
        control.create_movable_pivot(arm_ik_ctrl, ctrl_type='joint')
        mc.parent(self.prefix+'_arm_IK_PIV_CTL_GRP', arm_ik_ctrl+'_MOCAP')

        mc.setAttr(shoulder_ctrl+'.clavUpLimit', k=0, cb=1)
        mc.setAttr(shoulder_ctrl+'.clavDownLimit', k=0, cb=1)
        mc.setAttr(shoulder_ctrl+'.clavFrontLimit', k=0, cb=1)
        mc.setAttr(shoulder_ctrl+'.clavBackLimit', k=0, cb=1)

        # This finalizes guide and creates rig sets
        nodes = [up_arm_fk_ctrl, lo_arm_fk_ctrl, wrist_fk_ctrl]
        self.create_ctrl_set('FK', nodes)

        # This sets up the pickwalk hierarchy the animators will work with. Subject to change.
        # attribute_tag(ctrl, parent)
        ikChain.tag_match_function(switch_ctrl, 'bipedarm')
        ikChain.create_snapto_node(pv_ctrl, lo_arm_ik_jnt)
        ikChain.create_snapto_node(arm_ik_ctrl, wrist_ik_jnt)

        pickWalk.attribute_tag(up_arm_fk_ctrl,shoulder_ctrl)
        pickWalk.attribute_tag(wrist_fk_ctrl,lo_arm_fk_ctrl)

        pickWalk.attribute_tag(arm_ik_ctrl,pv_ctrl)
        pickWalk.attribute_tag(pv_ctrl, shoulder_ctrl)

        pickWalk.attribute_tag(shoulder_ctrl, pickWalk_parent)
        pickWalk.attribute_tag(switch_ctrl, arm_ik_ctrl)

        if make_bendy:
            pickWalk.attribute_tag(bendyArmCCtrl[-1], bendyArmBCtrl[-1])
            pickWalk.attribute_tag(bendyArmBCtrl[-1], bendyArmACtrl[-1])
            pickWalk.attribute_tag(bendyArmACtrl[-1], shoulder_ctrl)


        self.finalize_part()

