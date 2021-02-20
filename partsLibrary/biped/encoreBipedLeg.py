# -*- rigBot: part -*-

import maya.cmds as mc
import maya.mel as mm
import pymel.core as pm

from rigBot import constraint
from rigBot import control
from rigBot import ikChain
from rigBot import pickWalk
from rigBot import rivet
from rigBot import spaces
from rigBot import spline
from rigBot import utils
from rigBot.partsLibrary import standardPart

reload(ikChain)


class EncoreBipedLeg(standardPart.StandardPart):
    """Biped leg module. Includes FK/ IK, twist, stretch, bendy and soft IK.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_hip_JNT".
            :ikHandleParent: (str) Optional IK handle parent for connecting to a foot part. Will default to it's own IK control if the node doesnt exist. Defaults to "L_foot_IK_handle_driver_JNT".
            :numberTwistJoints: (int) Number of twist joints PER upper and lower leg. Defaults to 4.
            :makeBendy: (bool) Add bendy controls. Defaults to False.

        Note:
            If using the bendy feature you will need enough twist joints to allow for proper spline deformation."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('parent', data_type='hook', default='C_hip_JNT')

        self.add_option('ikHandleParent',
                        data_type='hook',
                        default='L_foot_IK_handle_driver_JNT',
                        tool_tip="Optional IK handle parent for connecting to a " + \
                                 "foot part. Will default to it's own IK control " + \
                                 "if the node doesnt exist.")

        self.add_option('fkAnkleJoint',
                        data_type='hook',
                        default='L_ankle_JNT',
                        tool_tip="Optional FK ankle joint to drive lower leg twist.")

        self.add_option('numberTwistJoints',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=4,
                        min=0,
                        tool_tip='Number of twist joints PER upper and lower leg.')

        self.add_option('flipJoints',
                        data_type='bool',
                        default=False,
                        hidden=True,
                        tool_tip='Flip the up axis of the bind joints. ' + \
                                 '(Useful when the knee points backwards.)')

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

        self.add_option('pickWalkParent',
                        data_type='string',
                        default='C_hip_CTL',
                        selectable=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        prefix, options = self.create_guide_master(**kwargs)

        prefix = self.prefix
        options = self.options
        mirror_value = self.mirror_value

        number_twist_jnts = options.get('numberTwistJoints')
        make_bendy = options.get('makeBendy')

        # draw joints
        up_leg_zero, up_leg_plc, up_leg_jnt = self.guide_joint('upLeg', constraint_type='point')
        lo_leg_zero, lo_leg_plc, lo_leg_jnt = self.guide_joint('loLeg', constraint_type='point')
        leg_end_zero, leg_end_plc, leg_end_jnt = self.guide_joint('leg_end', constraint_type='point')

        ik_driver_plc_zero, ik_driver_plc = self.guide_joint('leg_IK_handle_driver', placer_only=1)

        mc.setAttr(ik_driver_plc + '.radius', 1)
        mc.setAttr(ik_driver_plc + '.color', 0.96, 0.71, .01)
        mc.setAttr(ik_driver_plc + '.otherType', 'Leg IK Driver', type='string');
        mc.setAttr(ik_driver_plc + '.type', 18)

        mc.parentConstraint(leg_end_jnt, ik_driver_plc_zero)
        mc.setAttr(ik_driver_plc + '.offsetTranslateX', self.mirror_value * -0.25)

        # position
        mc.setAttr(up_leg_zero + '.tx', 0)
        mc.setAttr(lo_leg_zero + '.tx', 0)
        mc.setAttr(lo_leg_zero + '.ty', -4)
        mc.setAttr(lo_leg_zero + '.tz', 0.5)
        mc.setAttr(leg_end_zero + '.tx', 0)
        mc.setAttr(leg_end_zero + '.ty', -8)

        # Constraint upLeg
        up_ac = mc.aimConstraint(lo_leg_plc,
                                 up_leg_jnt,
                                 n=up_leg_jnt + '_ac',
                                 aim=[mirror_value, 0, 0],
                                 u=[0, 0, mirror_value],
                                 wut='object',
                                 wuo=leg_end_plc)[0]

        # Constraint loLeg
        lo_ac = mc.aimConstraint(leg_end_plc,
                                 lo_leg_jnt,
                                 n=lo_leg_jnt + '_ac',
                                 aim=[mirror_value, 0, 0],
                                 u=[0, 0, mirror_value],
                                 wut='object',
                                 wuo=up_leg_plc)[0]

        mc.setDrivenKeyframe(up_ac + '.upVectorZ', cd=self.guide_master + '.flipJoints', dv=0, v=self.mirror_value)
        mc.setDrivenKeyframe(up_ac + '.upVectorZ', cd=self.guide_master + '.flipJoints', dv=1, v=-self.mirror_value)
        mc.setDrivenKeyframe(lo_ac + '.upVectorZ', cd=self.guide_master + '.flipJoints', dv=0, v=self.mirror_value)
        mc.setDrivenKeyframe(lo_ac + '.upVectorZ', cd=self.guide_master + '.flipJoints', dv=1, v=-self.mirror_value)

        # parent jnts
        mc.parent(lo_leg_jnt, up_leg_jnt)
        mc.parent(leg_end_jnt, lo_leg_jnt)

        mc.xform(leg_end_jnt, a=1, ro=[0, 0, 0])
        mc.setAttr(leg_end_jnt + '.jo', 0, 0, 0)

        # Create twist jnts
        div = 1.0 / (number_twist_jnts + 1)

        up_twist_zeros, up_twist_plcs, up_twist_jnts = [], [], []
        lo_twist_zeros, lo_twist_plcs, lo_twist_jnts = [], [], []

        up_shpr_zeros, up_shpr_plcs, up_shpr_jnts = [], [], []
        lo_shpr_zeros, lo_shpr_plcs, lo_shpr_jnts = [], [], []

        for i in range(number_twist_jnts):

            # setup upper leg jnts
            letter = utils.letters[i]
            zero, plc, jnt = self.guide_joint('upLeg_twist_' + letter, constraint_type='point')

            if up_twist_jnts:
                mc.parent(jnt, up_twist_jnts[-1])
            else:
                mc.parent(jnt, up_leg_jnt)

            up_twist_jnts.append(jnt)
            up_twist_plcs.append(plc)
            up_twist_zeros.append(zero)

            mc.pointConstraint(up_leg_plc, plc, weight=1.0 - (div * (i + 1)))
            mc.pointConstraint(lo_leg_plc, plc, weight=(div * (i + 1)))
            mc.orientConstraint(up_leg_jnt, plc)

            mc.xform(jnt, a=1, ro=[0, 0, 0])
            mc.setAttr(jnt + '.jo', 0, 0, 0)
            # utils.set_attrs(plc, 't r s', l=1, k=0)

            # #jnts and control to follow twist joints

            up_shpr_name = 'upLeg_shaper_' + letter
            up_shpr_zero, up_shpr_plc, up_shpr_jnt = self.guide_joint(up_shpr_name, constraint_type='point')
            # mc.parent(up_shpr_jnt, up_leg_jnt)
            up_shpr_jnts.append(up_shpr_jnt)
            up_shpr_plcs.append(up_shpr_plc)
            up_shpr_zeros.append(up_shpr_zero)
            mc.delete(mc.parentConstraint(jnt, up_shpr_jnt, mo=0))
            mc.parentConstraint(jnt, up_shpr_zero)
            up_shpr_ctl_zero, up_shpr_ctrl = self.guide_ctrl(up_shpr_name, shape='pin_circle', color='dark_magenta',
                                                             driver=up_shpr_jnt, scale=[mirror_value + 3, 3, 3],
                                                             allow_offset_ctrls=False)
            mc.setAttr(up_shpr_ctrl.replace('CTL', 'PIV_CTL') + '.rx', 180)

            # setup uplowerper leg jnts
            letter = utils.letters[i]
            zero, plc, jnt = self.guide_joint('loLeg_twist_' + letter, constraint_type='point')

            if lo_twist_jnts:
                mc.parent(jnt, lo_twist_jnts[-1])
            else:
                mc.parent(jnt, lo_leg_jnt)

            lo_twist_jnts.append(jnt)
            lo_twist_plcs.append(plc)
            lo_twist_zeros.append(zero)

            mc.pointConstraint(lo_leg_plc, plc, weight=1.0 - (div * (i + 1)))
            mc.pointConstraint(leg_end_plc, plc, weight=(div * (i + 1)))
            mc.orientConstraint(lo_leg_jnt, plc)

            # mc.xform(jnt, a=1, ro=[0, 0, 0])
            mc.setAttr(jnt + '.jo', 0, 0, 0)

            utils.set_attrs(plc, 't r s', l=1, k=0)

            lo_shr_name = 'loLeg_shaper_' + letter
            lo_shpr_zero, lo_shpr_plc, lo_shpr_jnt = self.guide_joint(lo_shr_name, constraint_type='point')
            # mc.parent (lo_shpr_jnt, lo_leg_jnt)
            lo_shpr_jnts.append(lo_shpr_jnt)
            lo_shpr_plcs.append(lo_shpr_plc)
            lo_shpr_zeros.append(lo_shpr_zero)
            mc.delete(mc.parentConstraint(jnt, lo_shpr_jnt, mo=0))
            mc.parentConstraint(jnt, lo_shpr_zero)
            lo_shp_ctl_zero, lo_shp_ctrl = self.guide_ctrl(lo_shr_name, shape='pin_circle', color='dark_magenta',
                                                           driver=lo_shpr_jnt, scale=[mirror_value + 3, 3, 3],
                                                           allow_offset_ctrls=False)
            mc.setAttr(lo_shp_ctrl.replace('CTL', 'PIV_CTL') + '.rx', 180)

        if up_twist_jnts:
            mc.parent(lo_leg_jnt, up_twist_jnts[-1])
            for plc in up_twist_plcs:
                mc.setAttr(plc + '.radius', .4)
        #
        #
        if lo_twist_jnts:
            mc.parent(leg_end_jnt, lo_twist_jnts[-1])
            for plc in lo_twist_plcs:
                mc.setAttr(plc + '.radius', .4)

        # lock plcs
        utils.set_attrs([up_leg_plc, lo_leg_plc], 'r s', l=1, k=0)

        # create controls

        up_leg_fk_zero, up_leg_fk_ctrl = self.guide_ctrl(name='upLeg_FK',
                                                         shape='cube',
                                                         color='light_blue',
                                                         driver=up_leg_jnt,
                                                         allow_offset_ctrls=False,
                                                         axis='X')

        lo_leg_fk_zero, lo_leg_fk_ctrl = self.guide_ctrl(name='loLeg_FK',
                                                         shape='cube',
                                                         color='light_blue',
                                                         driver=lo_leg_jnt,
                                                         allow_offset_ctrls=False,
                                                         axis='X')

        leg_end_fk_zero, leg_end_fk_ctrl = self.guide_ctrl(name='legEnd_FK',
                                                           shape='cube',
                                                           color='light_blue',
                                                           driver=leg_end_jnt,
                                                           allow_offset_ctrls=False,
                                                           axis='X')

        color = 'green'
        if mirror_value < 0:
            color = 'red'

        leg_ik_zero, leg_ik_ctrl = self.guide_ctrl('leg_IK',
                                                   shape='circle',
                                                   axis='X',
                                                   color=color,
                                                   create_pivot=False,
                                                   scale=[1.5, 1.5, 2.5])

        orient_loc = mc.createNode('transform', p=leg_end_jnt, n=leg_end_jnt + '_orient')
        mc.parent(orient_loc, w=1)
        mc.xform(orient_loc, r=1, t=[0, 1, 0])
        mc.pointConstraint(leg_end_jnt, orient_loc, mo=1)
        mc.parent(orient_loc, self.guide_master + '_CTLS')

        mc.pointConstraint(leg_end_jnt, leg_ik_zero)
        mc.aimConstraint(orient_loc, leg_ik_zero, aim=[mirror_value, 0, 0], u=[0, 1, 0], wu=[0, 1, 0],
                         wut='objectRotation', wuo=leg_end_jnt)

        pv_zero, pv_ctrl = self.guide_ctrl('leg_PV', shape='cube', color=color, scale=[0.2] * 3, allow_offset_ctrls=0,
                                           create_pivot=0)
        pv_pivot = utils.get_parent(pv_ctrl)
        utils.set_attrs(pv_pivot, 't', l=0)

        grp = utils.get_parent(pv_pivot)
        noxform = utils.get_parent(pv_zero).replace('CTLS', 'NOX')

        # Constraint pv
        mc.pointConstraint(up_leg_jnt, pv_zero, n=pv_zero + '_pc')
        mc.aimConstraint(leg_end_jnt,
                         pv_zero,
                         n=pv_zero + '_ac',
                         aim=[mirror_value, 0, 0],
                         u=[0, 0, -mirror_value],
                         wut='object',
                         wuo=lo_leg_jnt)

        mc.pointConstraint(lo_leg_jnt, grp, n=grp + '_pc')
        mc.setAttr(pv_pivot + '.tz', -10)
        mc.orientConstraint(noxform, pv_ctrl, n=pv_ctrl + '_pc')

        utils.set_attrs([pv_ctrl, pv_zero, grp, pv_pivot], 'r t s v', l=1, k=0)
        utils.set_attrs(pv_ctrl, 'tx tz s ', l=0, k=1)

        leg_base_fk_zero, leg_base_fk_ctrl = self.guide_ctrl(name='legBase',
                                                             shape='semi_circle',
                                                             color=color,
                                                             scale=[1.5, 1.5, 3],
                                                             driver=up_leg_jnt,
                                                             axis='Y')

        mc.xform(leg_base_fk_ctrl + '.cv[*]', r=1, ro=[0, 90, 90])

        # ik fk switch ctrl
        switch_zero, switch_ctrl = self.guide_ctrl(name='leg_IK_switch', shape='pin_switch', color='black',
                                                   driver=leg_end_jnt, axis='Z', scale=[3, 3, 3])
        mc.xform(switch_ctrl, r=1, ro=[-90, 0, -90])
        mc.makeIdentity(switch_ctrl, apply=1, t=1, r=1, s=1, n=0, pn=1)
        mc.setAttr(leg_ik_ctrl + '.numOffsetCtrls', 1)

        # Create driven shapes for pv for reference
        line = mc.createNode('transform', n=pv_ctrl + '_line_REF', p=utils.get_parent(pv_zero))
        control.create_driven_shape(line, [pv_ctrl, lo_leg_jnt])
        utils.set_draw_override(line, 1)

        if make_bendy:
            baCtrl = self.guide_ctrl(name='bendyLeg_A', shape='arrow_quad', color='yellow', axis='X')
            bbCtrl = self.guide_ctrl(name='bendyLeg_B', shape='arrow_quad', color='yellow', axis='X')
            bcCtrl = self.guide_ctrl(name='bendyLeg_C', shape='arrow_quad', color='yellow', axis='X')

            mc.parentConstraint(up_leg_jnt, baCtrl[0], n=baCtrl[0] + '_prc')
            mc.parentConstraint(lo_leg_jnt, bbCtrl[0], n=bbCtrl[0] + '_prc')
            mc.parentConstraint(lo_leg_jnt, bcCtrl[0], n=bcCtrl[0] + '_prc')

            mc.pointConstraint(up_leg_jnt, lo_leg_jnt, baCtrl[1] + '_CONST', n=baCtrl[1] + '_CONST_pc')
            mc.pointConstraint(leg_end_jnt, lo_leg_jnt, bcCtrl[1] + '_CONST', n=bcCtrl[1] + '_CONST_pc')
            oc = mc.orientConstraint(up_leg_jnt, lo_leg_jnt, bbCtrl[1] + '_CONST', n=bbCtrl[1] + '_CONST_oc')
            mc.setAttr(oc[0] + '.interpType', 2)

            utils.set_attrs(baCtrl + bbCtrl + bcCtrl)
            utils.set_attrs([baCtrl[-1], bbCtrl[-1], bcCtrl[-1]], 't r s', k=1, l=0)

        # This finalizes your guide.
        utils.set_attrs(ik_driver_plc, l=1, k=0)
        # mc.setAttr (ik_driver_plc+'.visibility', 0)

        mc.setAttr(self.guide_master + '.tx', self.mirror_value)
        mc.setAttr(self.guide_master + '.offsetTranslateY', self.mirror_value * 0.5)

        self.finalize_guide()

    def build_rig(self):
        """This builds your anim rig."""

        # create rig part top nodes
        self.create_part_master()

        # Get all the relevant part info
        prefix = self.prefix
        options = self.options
        anim_ctrls = self.anim_ctrls
        bind_joints = self.bind_joints
        world_scale_attr = self.hooks[0] + '.worldScale'
        hooks = self.hooks
        ctrl_grps = self.ctrl_grps
        jnt_grps = self.jnt_grps

        number_twist_jnts = options.get('numberTwistJoints')
        parent = options.get('parent')

        world_orient_trans = options.get('transOrientiation')

        up_leg_jnt = prefix + '_upLeg_JNT'
        lo_leg_jnt = prefix + '_loLeg_JNT'
        leg_end_jnt = prefix + '_leg_end_JNT'

        up_leg_twist_jnts = mc.ls(prefix + '_upLeg_twist_*_JNT')
        lo_leg_twist_jnts = mc.ls(prefix + '_loLeg_twist_*_JNT')
        make_bendy = options.get('makeBendy')
        pickWalk_parent = options.get('pickWalkParent')

        up_leg_shaper_jnts = mc.ls(prefix + '_upLeg_shaper_*_JNT')
        lo_leg_shaper_jnts = mc.ls(prefix + '_loLeg_shaper_*_JNT')

        # Create FK ctrls
        name = prefix + '_legBase_CTL'
        leg_base_zero, leg_base_ctrl, leg_base_offsets, leg_base_last_node = self.anim_ctrl(name)

        name = prefix + '_upLeg_FK_CTL'
        up_leg_fk_zero, up_leg_fk_ctrl, up_leg_fk_offsets, up_leg_fk_last_node = self.anim_ctrl(name)

        name = prefix + '_loLeg_FK_CTL'
        lo_leg_fk_zero, lo_leg_fk_ctrl, lo_leg_fk_offsets, lo_leg_fk_last_node = self.anim_ctrl(name)

        name = prefix + '_legEnd_FK_CTL'
        leg_end_fk_zero, leg_end_fk_ctrl, leg_end_fk_offsets, leg_end_fk_last_node = self.anim_ctrl(name)

        if make_bendy:
            bendyLegACtrl = self.anim_ctrl(prefix + '_bendyLeg_A_CTL')
            bendyLegBCtrl = self.anim_ctrl(prefix + '_bendyLeg_B_CTL')
            bendyLegCCtrl = self.anim_ctrl(prefix + '_bendyLeg_C_CTL')
            mc.parent(bendyLegACtrl[0], bendyLegBCtrl[0], bendyLegCCtrl[0], ctrl_grps[0])

        # Comment this IF you want the foot tp up vector to the ankle position
        orient_loc = utils.snap_locator(leg_end_jnt)
        tmp_aim = utils.snap_locator(leg_end_jnt)
        mc.xform(tmp_aim, r=1, t=[0, 1, 0])

        if self.mirror_value < 0:
            mc.xform(orient_loc, r=1, s=[-1, 0, 0])

        mc.delete(mc.aimConstraint(tmp_aim, orient_loc,
                                   u=[0, 0, 1],
                                   wu=[0, 0, -1],
                                   aim=[0, self.mirror_value, 0],
                                   wuo=leg_end_jnt,
                                   wut='objectRotation'))

        # Create IK ctrls
        name = prefix + '_leg_IK_CTL'
        leg_ik_zero, leg_ik_ctrl, leg_ik_offsets, leg_ik_last_node = self.anim_ctrl(name, node_type='joint',
                                                                                    match_position=orient_loc)

        leg_ik_last_node = mc.createNode('transform', p=leg_ik_last_node, n=prefix + '_leg_IK_handle_driver_JNT')

        utils.set_attrs(leg_ik_ctrl, 'jo', l=0, k=1)

        grp = mc.group(leg_ik_ctrl)
        mc.parent(grp, w=1)

        mc.xform(leg_ik_zero, ws=1, ro=[0, 0, 0])

        mc.parent(leg_ik_ctrl, leg_ik_zero)
        mc.delete(orient_loc, tmp_aim, grp)

        mc.setAttr(leg_ik_ctrl + '.jox', 0)
        mc.setAttr(leg_ik_ctrl + '.joz', 0)

        for ctrl in [leg_ik_ctrl] + leg_ik_offsets:
            control.copy_shape(ctrl + '_REF', ctrl)

        name = prefix + '_leg_PV_CTL'
        loc = utils.snap_locator(name + '_REF')
        mc.setAttr(loc + '.sx', self.mirror_value)
        pv_zero, pv_ctrl, pv_offsets, pv_last_node = self.anim_ctrl(name, match_position=loc)

        name = prefix + '_leg_IK_switch_CTL'
        switch_zero, switch_ctrl, switch_offsets, switch_last_node = self.anim_ctrl(name)
        # ikChain.make_fkikSwitch_connection_attrs

        mc.delete(loc)

        up_leg_grp = mc.createNode('transform', n=up_leg_jnt + '_GRP', p=up_leg_jnt)
        mc.parent(up_leg_grp, jnt_grps[0])
        mc.parent(up_leg_jnt, up_leg_grp)

        # orient leg ik ctrl
        tmp_grp = mc.createNode('transform', p=leg_ik_ctrl)
        mc.parent(tmp_grp, w=1)

        mc.xform(leg_ik_zero, a=1, ro=[0, 0, 0])
        mc.setAttr(leg_ik_zero + '.s', self.mirror_value, 1, 1)

        utils.set_attrs(leg_ik_ctrl, 'jo', l=0)
        mc.parent(leg_ik_ctrl, leg_ik_ctrl + '_OFF')
        mc.delete(tmp_grp)

        if world_orient_trans == 'downBone':
            utils.set_attrs(leg_ik_ctrl + '_ZERO', 'ry', k=1, l=0)
            utils.set_attrs(leg_ik_ctrl, 'joy', k=1, l=0)
            mc.setAttr(leg_ik_ctrl + '_ZERO.ry', mc.getAttr(leg_ik_ctrl + '.joy'))

            utils.set_attrs(leg_ik_ctrl + '_ZERO', 'ry', k=0, l=1)
            utils.set_attrs(leg_ik_ctrl, 'joy', k=0, l=1)

        # parent fk ctrls
        mc.parent(up_leg_fk_zero, leg_base_ctrl)
        mc.parent(lo_leg_fk_zero, up_leg_fk_ctrl)
        mc.parent(leg_end_fk_zero, lo_leg_fk_ctrl)

        # NOW create ik fk chain setup
        up_leg_ik_jnt = mc.duplicate(up_leg_jnt, po=1, n=up_leg_jnt.replace('upLeg', 'upLeg_IK'))[0]
        lo_leg_ik_jnt = mc.duplicate(lo_leg_jnt, po=1, n=lo_leg_jnt.replace('loLeg', 'loLeg_IK'))[0]
        leg_end_ik_jnt = mc.duplicate(leg_end_jnt, po=1, n=leg_end_jnt.replace('leg_end', 'leg_end_IK'))[0]

        mc.parent(lo_leg_ik_jnt, up_leg_ik_jnt)
        mc.parent(leg_end_ik_jnt, lo_leg_ik_jnt)

        mc.orientConstraint(up_leg_fk_last_node, up_leg_ik_jnt, mo=1)

        ori_par = mc.createNode('transform', p=lo_leg_jnt, n=lo_leg_jnt + '_orient_DRV_PAR')
        ori = mc.createNode('transform', p=ori_par, n=lo_leg_jnt + '_orient_DRV')
        mc.parent(ori_par, lo_leg_fk_zero)

        mc.orientConstraint(lo_leg_fk_ctrl, ori, mo=1)
        mc.connectAttr(ori + '.r', lo_leg_ik_jnt + '.r')

        ik_handle = mc.ikHandle(sj=up_leg_ik_jnt, ee=leg_end_ik_jnt, s='sticky', n=prefix + '_leg_IK')[0]
        mc.poleVectorConstraint(pv_ctrl, ik_handle)

        ikChain.create_fk_ik_switch(switch_ctrl, ik_handle, up_leg_fk_zero, [leg_ik_zero, pv_zero])
        mc.parent(ik_handle, leg_ik_last_node)
        mc.setAttr(switch_ctrl + '.IK', 1)
        mc.hide(ik_handle)

        mc.addAttr(leg_ik_ctrl, ln='twist', k=1)

        mc.connectAttr(leg_ik_ctrl + '.twist', ik_handle + '.twist')
        if self.mirror_value < 0.0:
            utils.connect_negative(leg_ik_ctrl + '.twist', ik_handle + '.twist')

        # Create soft ik
        ik_joints = [up_leg_ik_jnt, lo_leg_ik_jnt, leg_end_ik_jnt]
        ik_ctrl = leg_ik_ctrl

        # new case for new hook
        ik_handle_grp = mc.createNode('transform', p=leg_ik_last_node, n=ik_handle + '_GRP')
        mc.parent(ik_handle_grp, jnt_grps[1])
        mc.parent(ik_handle, ik_handle_grp)
        mc.parentConstraint(leg_ik_last_node, hooks[1], mo=1)

        ik_handle_parent = ikChain.create_soft_ik(ik_ctrl, ik_joints, ik_handle)

        # Create IK wrist orient switch
        ik_ctrl_follow_par = mc.createNode('transform', n=leg_end_ik_jnt + '_ik_follow_PAR', p=leg_end_ik_jnt)
        fk_ctrl_follow_par = mc.createNode('transform', n=leg_end_ik_jnt + '_fk_follow_PAR', p=leg_end_ik_jnt)

        ik_ctrl_follow = mc.createNode('transform', n=leg_end_ik_jnt + '_ik_follow', p=leg_end_ik_jnt)
        fk_ctrl_follow = mc.createNode('transform', n=leg_end_ik_jnt + '_fk_follow', p=leg_end_ik_jnt)

        mc.parent(fk_ctrl_follow, fk_ctrl_follow_par)
        mc.parent(ik_ctrl_follow, ik_ctrl_follow_par)
        mc.parent(fk_ctrl_follow_par, leg_end_fk_ctrl)
        mc.parent(ik_ctrl_follow_par, leg_ik_last_node)

        oc = mc.orientConstraint(fk_ctrl_follow, ik_ctrl_follow, leg_end_ik_jnt)[0]
        mc.setAttr(oc + '.interpType', 2)
        mc.connectAttr(switch_ctrl + '.IK', oc + '.w1', f=1)
        utils.connect_reverse(oc + '.w1', oc + '.w0')

        # setup autoclav
        mc.parentConstraint(leg_base_last_node, up_leg_grp, mo=1)

        shaper_ctrls = []
        shaper_zeros = []

        # Create twist
        if up_leg_twist_jnts:

            lo_twist_drv = mc.duplicate(leg_end_ik_jnt, n=leg_end_ik_jnt + '_twist_DRV', po=1)[0]
            mc.parent(lo_twist_drv, jnt_grps[2])

            ikChain.upper_twist(utils.get_parent(up_leg_ik_jnt), up_leg_ik_jnt, lo_leg_ik_jnt, up_leg_jnt, lo_leg_jnt,
                                up_leg_twist_jnts)
            ikChain.lower_twist(lo_leg_ik_jnt, lo_twist_drv, lo_leg_jnt, lo_leg_twist_jnts, leg_end_jnt)
            ikChain.stretch_twist_jnts(up_leg_ik_jnt, lo_leg_ik_jnt, up_leg_twist_jnts)
            ikChain.stretch_twist_jnts(lo_leg_ik_jnt, leg_end_ik_jnt, lo_leg_twist_jnts)

            mc.pointConstraint(leg_end_ik_jnt, prefix + '_leg_end_IK_JNT_twist_DRV')

            if up_leg_shaper_jnts:
                shapers = up_leg_shaper_jnts + lo_leg_shaper_jnts
                for shaper in shapers:
                    name = shaper.replace('JNT', 'CTL')
                    shaper_fk_zero, shaper_fk_ctrl, shaper_fk_offsets, shaper_fk_last_node = self.anim_ctrl(name)
                    mc.parentConstraint(shaper_fk_ctrl, shaper)
                    driver = shaper.replace('shaper', 'twist')
                    if mc.objExists(driver):
                        mc.parentConstraint(driver, shaper_fk_zero)
                    shaper_ctrls.append(shaper_fk_ctrl)
                    shaper_zeros.append(shaper_fk_zero)
                shpr_grp = mc.createNode('transform', name=prefix + '_shaper_CTL_GRP', p=ctrl_grps[0])
                mc.parent(shaper_zeros, shpr_grp)

        else:
            mc.parentConstraint(up_leg_ik_jnt, up_leg_jnt, mo=1)
            mc.parentConstraint(lo_leg_ik_jnt, lo_leg_jnt, mo=1)
            mc.parentConstraint(leg_end_ik_jnt, leg_end_jnt, mo=1)

        # #make knee joint VJ joint

        x_off = 2
        knee = lo_leg_jnt
        knee_vj_name = "{0}_knee_VJ_bind".format(prefix)
        knee_vj_jnt = mc.createNode('joint', name=knee_vj_name, p=knee)
        mc.pointConstraint(lo_leg_jnt, knee_vj_jnt)
        md = mc.createNode('multiplyDivide', name=prefix + '_knee_md')
        mc.connectAttr(up_leg_jnt + '.r', md + '.input1')
        mc.setAttr(md + '.input2', 2, 2, 2)
        mc.setAttr(md + '.operation', 2)
        mc.connectAttr(md + '.output', knee_vj_jnt + '.r')

        for p in ["up", "lo"]:
            jnt_name = "{0}_{1}_knee_jnt".format(prefix, p)
            jnt = mc.createNode('joint', name=jnt_name, p=knee_vj_jnt)
            yo = (-.5 * self.mirror_value)
            xo = -2 * (yo / 2)
            if p == 'up':
                xo = 2 * (yo / 2)
            mc.setAttr(jnt + '.translate', xo, 0, yo)

        # mc.orientConstraint (up_leg_jnt, lo_leg_jnt, knee_vj_jnt )

        # #create kneeFix surf and joint
        knee_fix_dvrs = up_leg_twist_jnts[-2], lo_leg_twist_jnts[1]
        width = utils.get_distance(knee_fix_dvrs[0], knee_fix_dvrs[1]) * 0.4
        nox_grp = '{0}_bipedLeg_NOX'.format(prefix)
        knee_fix_surf = spline.create_surface_mtx(knee_fix_dvrs, name=prefix + '_knee_fix', degree=1, axis='Z',
                                                  width=width, parent=nox_grp, stretch=True)
        knee_fix_jnt = mc.createNode('joint', p=knee_vj_jnt, n='{0}_knee_fix_JNT'.format(prefix))
        mc.setAttr(knee_fix_jnt + '.tz', (width / 2))
        mc.parent(knee_fix_jnt, jnt_grps[0])
        nodes = rivet.surface_mtx(knee_fix_surf, knee_fix_jnt, self.noxform_grp)
        mc.parent(knee_fix_surf, self.noxform_grp)

        # mc.delete(utils.get_constraints(leg_end_jnt))
        # mc.parentConstraint(leg_end_ik_jnt, leg_end_jnt, mo=1)

        # create stretch
        ikChain.biped_stretch(leg_ik_ctrl,
                              ik_handle_grp,
                              pv_ctrl,
                              switch_ctrl,
                              up_leg_fk_ctrl,
                              lo_leg_fk_ctrl,
                              leg_end_fk_ctrl,
                              up_leg_ik_jnt,
                              lo_leg_ik_jnt,
                              leg_end_ik_jnt,
                              ik_handle,
                              pin_attr_name='pinKnee',
                              shift_attr_name='shiftKnee')

        control.create_driven_shape(pv_ctrl, lo_leg_ik_jnt, replace=False)

        if make_bendy:
            mc.parentConstraint(up_leg_ik_jnt, bendyLegACtrl[0], mo=1, n=bendyLegACtrl[0] + '_prc')
            mc.pointConstraint(up_leg_ik_jnt, lo_leg_ik_jnt, bendyLegACtrl[1] + '_CONST', mo=1,
                               n=bendyLegACtrl[1] + '_CONST_pc')

            mc.parentConstraint(lo_leg_ik_jnt, bendyLegCCtrl[0], mo=1, n=bendyLegCCtrl[0] + '_prc')
            mc.pointConstraint(lo_leg_ik_jnt, leg_end_ik_jnt, bendyLegCCtrl[1] + '_CONST', mo=1,
                               n=bendyLegCCtrl[1] + '_CONST_pc')

            mc.parentConstraint(lo_leg_ik_jnt, bendyLegBCtrl[0], mo=1, n=bendyLegBCtrl[0] + '_prc')
            oc = mc.orientConstraint(up_leg_ik_jnt, lo_leg_ik_jnt, bendyLegBCtrl[1] + '_CONST', mo=1,
                                     n=bendyLegBCtrl[1] + '_CONST_pc')[0]
            mc.setAttr(oc + '.interpType', 2)

            bendy_joints_drivers = [up_leg_jnt] + up_leg_twist_jnts + [lo_leg_jnt] + lo_leg_twist_jnts + [leg_end_jnt]
            bendy_ctrls = [bendyLegACtrl[-1], bendyLegBCtrl[-1], bendyLegCCtrl[-1]]
            noxform_grp = self.noxform_grp

            ikChain.biped_bendy(bendy_joints_drivers, bendy_ctrls, False, noxform_grp, 'smoothKnee',
                                ctrl_driver=bendyLegBCtrl[1])

        # clean up now
        mc.hide(up_leg_ik_jnt)
        mc.parentConstraint(leg_end_jnt, switch_zero, mo=1)
        mc.parent(leg_base_zero, leg_ik_zero, pv_zero, switch_zero, ctrl_grps[0])

        utils.set_attrs([up_leg_fk_ctrl, lo_leg_fk_ctrl], 't s v', l=1, k=0)
        utils.set_attrs(lo_leg_fk_ctrl, 'ro', l=1, k=0)
        utils.set_attrs(pv_ctrl, 'r s v ro', l=1, k=0)
        utils.set_attrs(switch_ctrl, 't r s v ro', l=1, k=0)
        utils.set_attrs(leg_base_ctrl, 's', l=1, k=0)

        utils.set_attrs(leg_ik_offsets + [leg_ik_ctrl], ' s v ro jo radius', l=1, k=0, cb=0)
        for c in leg_ik_offsets + [leg_ik_ctrl]:
            mc.setAttr(c + '.radius', k=0, cb=0)

        # create pv aim at space
        aim_drv = mc.duplicate(up_leg_ik_jnt, n=pv_ctrl + '_AIM_DRV', po=1)[0]
        aim_drv_end = mc.duplicate(lo_leg_ik_jnt, n=pv_ctrl + '_AIM_DRV_end', po=1)[0]
        aim_drv_ik = mc.duplicate(leg_end_ik_jnt, n=pv_ctrl + '_IK_DRV_end', po=1)[0]

        mc.parent(aim_drv_end, aim_drv)
        mc.setAttr(aim_drv_end + '.tx', mc.getAttr(aim_drv_end + '.tx') * 0.05)

        aim_ik = mc.ikHandle(sj=aim_drv, ee=aim_drv_end, n=aim_drv + '_IK', sol='ikSCsolver', s='sticky')[0]
        mc.pointConstraint(aim_drv_ik, aim_ik)

        mc.parent(aim_drv_ik, jnt_grps[1])
        mc.parent(aim_ik, aim_drv_ik)

        mc.hide(aim_drv, aim_drv_end, aim_ik, aim_drv_ik)

        # spaces
        spaces.tag(leg_ik_ctrl, default=2)
        spaces.tag(pv_ctrl, 'foot:' + aim_drv, default=1)

        jnts = [up_leg_jnt] + up_leg_twist_jnts + [lo_leg_jnt] + lo_leg_twist_jnts + [leg_end_jnt] + shapers
        # utils.create_cfx_curves(jnts, self.prefix+'_'+self.part_type)

        # movable pivot
        control.create_movable_pivot(leg_ik_ctrl, ctrl_type='joint')
        mc.parent(self.prefix + '_leg_IK_PIV_CTL_GRP', leg_ik_ctrl + '_MOCAP')

        # This finalizes guide and creates rig sets
        nodes = [up_leg_fk_ctrl, lo_leg_fk_ctrl, leg_end_fk_ctrl]
        self.create_ctrl_set('FK', nodes)

        # This sets up the pickwalk hierarchy the animators will work with. Subject to change.
        # attribute_tag(ctrl, parent)
        ikChain.tag_match_function(switch_ctrl, 'bipedleg')
        ikChain.create_snapto_node(pv_ctrl, lo_leg_ik_jnt)
        ikChain.create_snapto_node(leg_ik_ctrl, leg_end_jnt)
        ikChain.create_snapto_node(leg_end_fk_ctrl, jnt_grps[1])

        pickWalk.attribute_tag(leg_end_fk_ctrl, lo_leg_fk_ctrl)

        pickWalk.attribute_tag(leg_ik_ctrl, pv_ctrl)
        pickWalk.attribute_tag(pv_ctrl, leg_base_ctrl)

        pickWalk.attribute_tag(leg_base_ctrl, pickWalk_parent)
        pickWalk.attribute_tag(switch_ctrl, leg_ik_ctrl)

        if make_bendy:
            pickWalk.attribute_tag(bendyLegCCtrl[-1], bendyLegBCtrl[-1])
            pickWalk.attribute_tag(bendyLegBCtrl[-1], bendyLegACtrl[-1])
            pickWalk.attribute_tag(bendyLegACtrl[-1], leg_base_ctrl)

        self.finalize_part()
