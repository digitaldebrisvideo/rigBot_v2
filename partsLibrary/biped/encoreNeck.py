# -*- rigBot: part -*-

import maya.cmds as mc
import maya.mel as mm
import pymel.core as pm

from rigBot import constraint
from rigBot import control
from rigBot import env
from rigBot import pickWalk
from rigBot import rivet
from rigBot import spaces
from rigBot import spline
from rigBot import utils
from rigBot.partsLibrary import standardPart


class EncoreNeck(standardPart.StandardPart):
    """Neck rig build part for standard biped and long neck creatures.


        Note:


        Build Options:
            :side: (str) Side token for this rig part. Defaults to "C".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_chest_end_JNT".
            :numberJoints: (int) Numder of neck joints. Defaults to 4.
            :create surface from spline: (bool) False
            :numberMidCtrls: (int) Number of mid neck IK ctrls. Defaults to 1.
            :fkShpers: (bool) if true shaper controls will be set up as fk chain that follows ik and can be peeled off the spline crv or surface.
                              if false, shapers ctrls are flattened with normal setup driven by each spline joint . Defaults to False.
            :createBckFixJoints: (bool) Create back helper joint with set driven keys that push out the back of neck when head is rotated back to fix divot caused by spline IK
            :createJaw: (bool) Create jaw joint and control. Defaults to True.
            :createReverseJaw: (bool) Create reverse jaw ctrl for the upper head. Defaults to True."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('side', default='C')
        self.add_option('parent', data_type='hook', default='C_chest_end_JNT')

        self.add_option('numberJoints',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=4,
                        tool_tip='Numder of neck joints.',
                        min=2)

        self.add_option('numberMidCtrls',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=1,
                        min=1,
                        tool_tip='Number of mid neck IK ctrls.')

        self.add_option('createJaw',
                        data_type='bool',
                        rebuild_to_modify=True,
                        default=True,
                        tool_tip='Create jaw joint and control.')

        self.add_option('createReverseJaw',
                        data_type='bool',
                        rebuild_to_modify=True,
                        default=False,
                        tool_tip='Create reverse jaw ctrl for the upper head.')

        self.add_option('createSurfaceDriver',
                        data_type='bool',
                        rebuild_to_modify=False,
                        default=False,
                        tool_tip='Create surface from crvs that drive controls using decomposeMatrix constraints')

        self.add_option('createFKShaperCtrls',
                        data_type='bool',
                        rebuild_to_modify=True,
                        default=False,
                        tool_tip='Create shaper controls as fk chain that can peel off IK spline')

        self.add_option('pickWalkParent',
                        data_type='string',
                        default='C_chest_CTL',
                        selectable=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix
        options = self.options
        mirror_value = self.mirror_value

        number_mid_ctrl = options.get('numberMidCtrls')
        num_joints = options.get('numberJoints')
        create_jaw = options.get('createJaw')
        create_skull = options.get('createReverseJaw')
        surface = options.get('createSurfaceDriver')
        create_fk_ctrls = options.get('createFKShaperCtrls')

        noxform_grp = self.guide_master + '_NOX'
        length = 2

        if number_mid_ctrl == 1:
            num_spl_jnts = 4
        else:
            num_spl_jnts = number_mid_ctrl + 2

        # layout spline placers and jnts
        jnt_zeros, plcs, jnts = self.guide_joint_chain('neck', num_joints=num_joints, length=length)
        spline_zeros, spline_plcs = self.guide_joint_chain('neckSpline', num_joints=num_spl_jnts,
                                                           flat_plc_hierarchy=True,
                                                           flat_jnt_hierarchy=True,
                                                           placer_only=True,
                                                           length=length)

        self.tag_as_ref(spline_plcs)

        # Constraint center spline nodes
        div = 1.0 / (num_spl_jnts - 1)
        for i in range(1, len(spline_zeros[:-1])):
            zero = spline_zeros[i]
            mc.pointConstraint(spline_plcs[-1], zero, w=div * i)
            mc.pointConstraint(spline_plcs[0], zero, w=1.0 - div * i)

        # rotate to face up
        jnt_grp = utils.get_parent(jnt_zeros[0])
        grp = mc.group(jnt_zeros + spline_zeros)
        mc.xform(grp, piv=[0, 0, 0])
        mc.xform(grp, r=1, ro=[0, 0, 90])

        mc.parent(jnt_zeros + spline_zeros, jnt_grp)
        mc.delete(grp)

        # Create spline and bind
        spline_crv = spline.create_curve_mtx(spline_plcs,
                                             name=prefix + '_neckSplinePlc',
                                             axis='Y',
                                             degree=2,
                                             parent=noxform_grp)

        spline_surf = spline.create_surface_mtx(spline_plcs,
                                                name=prefix + '_neckSplinePlc',
                                                axis='Y',
                                                degree=2,
                                                parent=noxform_grp)

        # param_nodes = spline.connect_param_node(spline_crv, spline_surf, jnt_zeros)
        # param_nodes=rivet.surface_fll(nodes=jnt_zeros, surf=spline_surf, noxform_grp=noxform_grp)
        spline.create_stretch_crv(spline_crv)
        rivet.surface_mtx(spline_surf, jnt_zeros, noxform_grp)

        # for p in param_nodes:
        #     mc.setAttr(p+'.stretch', 1)
        #     mc.setAttr(p+'.uniformStretch', 1)

        # create head
        head_zero, head_plc, head_jnt = self.guide_joint('head_end', constraint_type='point')
        pos = mc.xform(plcs[-1], q=1, ws=1, t=1)
        mc.xform(head_zero, ws=1, t=pos)
        mc.xform(head_zero, r=1, t=[0, 3, 0])
        mc.parent(head_jnt, jnts[-1])
        mc.parent(head_zero, spline_plcs[-1])

        mc.setAttr(head_jnt + '.jo', 0, 0, 0)

        mc.aimConstraint(head_plc, jnts[-1],
                         aim=[1, 0, 0], u=[0, 1, 0], wu=[0, 1, 0],
                         wut='objectRotation', wuo=spline_plcs[-1])

        # Create head ctrl
        head_ct_zero, head_ctrl = self.guide_ctrl('head', shape='square_head', axis='Z', color='yellow',
                                                  scale=[.25] * 3)
        mc.delete(mc.pointConstraint(jnts[-1], head_ct_zero, mo=0))
        mc.parentConstraint(jnts[-1], head_ct_zero, mo=1)

        aim_grp = mc.createNode('transform', p=spline_plcs[0], n=spline_plcs[0] + '_aim_GRP')
        mc.aimConstraint(spline_plcs[-1], aim_grp, aim=[0, 1, 0], u=[1, 0, 0], wu=[0, -1, 0], wut='objectRotation',
                         wuo=spline_plcs[0])

        # Create neck base
        neck_base_ct_zero, neck_base_ctrl = self.guide_ctrl('neckBase', shape='square_neck', color='yellow_green',
                                                            scale=[.25] * 3)
        mc.delete(mc.pointConstraint(jnts[0], neck_base_ct_zero))
        mc.pointConstraint(jnts[0], neck_base_ct_zero, mo=1)
        mc.orientConstraint(aim_grp, neck_base_ct_zero, mo=1)

        ctrl = utils.get_parent(head_ctrl)
        mc.setAttr(ctrl + '.rx', -90)
        utils.set_attrs(ctrl, 't s ', l=1, k=0)
        # mc.xform (head_ctrl+'.cv[*]', r=1, ro=[0, 0, 90])

        ctrl = utils.get_parent(neck_base_ctrl)
        utils.set_attrs(ctrl, 't s ', l=1, k=0)

        # Create neck mid ctrls
        if number_mid_ctrl > 0:
            mid_ctrl_range = range(1, len(spline_zeros[:-1]))
            if number_mid_ctrl == 1:
                mid_ctrl_range = range(1)

            for i in mid_ctrl_range:
                spl_drv = spline_plcs[i]
                ltr = utils.letters[i - 1]
                ct_name = 'midNeck_' + ltr

                if number_mid_ctrl == 1:
                    ct_name = 'midNeck'
                    spl_drv = spline_plcs[1:3]

                mid_ct_zero, mid_ctrl = self.guide_ctrl(ct_name, shape='circle', color='pink', scale=[3.6, 3, 3])
                mc.pointConstraint(spl_drv, mid_ct_zero)
                mc.orientConstraint(aim_grp, mid_ct_zero)

                utils.set_attrs(utils.get_parent(mid_ctrl), 't', l=1, k=0)

                piv_ctrl = utils.get_parent(mid_ctrl)
                utils.set_attrs(piv_ctrl, 't s', l=1, k=0)

        fk_zeros = []
        fk_ctrls = []
        jnt_suffix = utils.get_suffix('joint')
        zero_suffix = utils.get_suffix('animCtrlZero')

        if create_fk_ctrls:
            for i, jnt in enumerate(jnts[:-1]):
                fk_name = 'neck_FK_' + utils.letters[i]
                fk_zero, fk_ctrl = self.guide_ctrl(fk_name, driver=jnt, create_pivot=0, allow_offset_ctrls=0,
                                                   shape='pin_circle', color='dark_magenta', scale=[2] * 3)
                fk_zeros.append(fk_zero)
                fk_ctrls.append(fk_ctrl)
        else:
            for i, jnt in enumerate(jnts):
                fk_name = 'neck_FK_' + utils.letters[i]
                fk_zero, fk_ctrl = self.guide_ctrl(fk_name, driver=jnt, create_pivot=0, allow_offset_ctrls=0,
                                                   shape='pin_circle',
                                                   color='dark_magenta', scale=[2] * 3)
                # mc.xform(fk_ctrl + '.cv[*]', r=1, ro=[-90, 0, 0])
                fk_zeros.append(fk_zero)
                fk_ctrls.append(fk_ctrl)

        # Create jaw
        if create_jaw:

            jaw_zero, jaw_plc, jaw_jnt = self.guide_joint('jaw', constraint_type='point')
            pos = mc.xform(plcs[-1], q=1, ws=1, t=1)
            mc.xform(jaw_zero, ws=1, t=pos)
            mc.xform(jaw_zero, r=1, t=[0, 0, 0.5])
            mc.parent(jaw_jnt, jnts[-1])
            mc.parent(jaw_zero, spline_plcs[-1])

            jaw_end_zero, jaw_end_plc, jaw_end_jnt = self.guide_joint('jaw_end', constraint_type='point')
            pos = mc.xform(jaw_jnt, q=1, ws=1, t=1)
            mc.xform(jaw_end_zero, ws=1, t=pos)
            mc.xform(jaw_end_zero, r=1, t=[0, 0, 2])
            mc.parent(jaw_end_jnt, jaw_jnt)
            mc.parent(jaw_end_zero, jaw_plc)

            mc.aimConstraint(jaw_end_plc, jaw_jnt, aim=[1, 0, 0], u=[0, 0, -1], wu=[1, 0, 0], wut='objectRotation',
                             wuo=jaw_plc)
            mc.setAttr(jaw_end_jnt + '.jo', 0, 0, 0)

            utils.set_attrs([jaw_end_plc], 'r ', l=1, k=0)

            # Create jaw ctrl
            jaw_ct_zero, jaw_ctrl = self.guide_ctrl('jaw', shape='semi_circle', allow_offset_ctrls=False, color='cyan',
                                                    scale=[2, 2, 2])
            mc.parentConstraint(jaw_jnt, jaw_ct_zero)

            mc.xform(jaw_ctrl + '.cv[*]', r=1, ro=[0, -90, 0])
            mc.xform(jaw_ctrl + '.cv[*]', r=1, s=[2.5, 1, 1])

            jaw_piv = utils.get_parent(jaw_ctrl)
            utils.set_attrs(jaw_piv, 't s', l=1, k=0)

            # Create skull ctrl
            if create_skull:
                rev_jaw_zero, rev_jaw_plc, rev_jaw_jnt = self.guide_joint('reverseJaw', constraint_type='parent')
                mc.parentConstraint(jaw_jnt, rev_jaw_zero)
                try:
                    mc.setAttr(rev_jaw_plc + 'Shape.offsetTranslateY', 0.25)
                except:
                    pass

                mc.parent(rev_jaw_jnt, jnts[-1])

                skull_ct_zero, skull_ctrl = self.guide_ctrl('reverseJaw', driver=rev_jaw_jnt, axis='Y',
                                                            shape='pin_circle', allow_offset_ctrls=False, color='cyan',
                                                            scale=[4, 4, 4])
                mc.xform(skull_ctrl, r=1, ro=[0, 90, 0])
                mc.makeIdentity(skull_ctrl, apply=1, t=1, r=1, s=1, n=0, pn=1)

                piv_ctrl = utils.get_parent(skull_ctrl)
                utils.set_attrs(piv_ctrl, 't s', l=1, k=0)
                utils.set_attrs(rev_jaw_plc, l=1, k=0)

        # lock stuff
        utils.set_attrs(plcs[:-1], 't r', l=1, k=0)

        utils.set_attrs(spline_plcs[:-1], 'r', l=1, k=0)
        utils.set_attrs(head_plc, 'r', l=1, k=0)

        utils.set_attrs(plcs, l=1, k=0)

        jnt_suffix = 'JNT'
        zero_suffix = 'ZERO'
        head_name = prefix + '_head_' + jnt_suffix
        mc.rename(jnt_zeros[-1], head_name + '_' + zero_suffix)
        mc.rename(jnts[-1], head_name)
        mc.rename(plcs[0], plcs[0] + '_DUMMY')
        mc.rename(plcs[-1], plcs[-1] + '_DUMMY')

        mc.rename(spline_plcs[0], plcs[0])
        mc.rename(spline_plcs[-1], head_name + '_PLC')

        fk_name = 'head_FK'
        fk_zero, fk_ctrl = self.guide_ctrl(fk_name, driver=head_name, allow_offset_ctrls=0, create_pivot=0,
                                           shape='pin_circle', color='dark_magenta', scale=[2] * 3)
        # mc.xform(fk_ctrl+'.cv[*]', r=1, ro=[-90,0,0])
        fk_zeros.append(fk_zero)
        fk_ctrls.append(fk_ctrl)

        # add head top and side joints

        head_top_jnt_zero, head_top_plc, head_top_jnt = self.guide_joint('head_top')
        head_top_zero, head_top_ctrl = self.guide_ctrl('head_top', driver=head_top_plc, allow_offset_ctrls=0,
                                                       create_pivot=0,
                                                       shape='cube', color='yellow', scale=[.5] * 3)

        mc.setAttr(head_top_jnt_zero + '.ty', 5)
        mc.parentConstraint(head_plc, head_top_jnt_zero, mo=1)

        head_left_jnt_zero, head_left_plc, head_left_jnt = self.guide_joint('head_left')
        head_left_zero, head_left_ctrl = self.guide_ctrl('head_left', driver=head_left_plc, allow_offset_ctrls=0,
                                                         create_pivot=0,
                                                         shape='cube', color='blue', scale=[.5] * 3)

        mc.setAttr(head_left_jnt_zero + '.t', 2, 5, -1)
        mc.parentConstraint(head_plc, head_left_jnt_zero, mo=1)

        head_right_jnt_zero, head_right_plc, head_right_jnt = self.guide_joint('head_right')
        head_left_zero, head_left_ctrl = self.guide_ctrl('head_right', driver=head_right_plc, allow_offset_ctrls=0,
                                                         create_pivot=0,
                                                         shape='cube', color='red', scale=[.5] * 3)

        mc.setAttr(head_right_jnt_zero + '.t', -2, 5, -1)
        mc.parentConstraint(head_plc, head_right_jnt_zero, mo=1)

        # This finalizes your guide.
        mc.setAttr(head_ctrl + '.numOffsetCtrls', 1)
        mc.setAttr(neck_base_ctrl + '.numOffsetCtrls', 1)

        # mc.xform (head_ctrl+'.cv[*]', r=1, ro=[0, 0, 90])

        mc.xform(spline_zeros, r=1, t=[0, -self.mirror_value, 0])
        mc.setAttr(self.guide_master + '.offsetTranslateZ', -0.5 * self.mirror_value)

        self.finalize_guide()

    def build_rig(self):
        """This builds your anim rig."""

        # create rig part top nodes
        self.create_part_master()

        # Get all the relevant part info
        prefix = self.prefix
        options = self.options
        anim_ctrls = self.anim_ctrls
        bind_jnts = self.bind_joints
        hooks = self.hooks
        ctrl_grps = self.ctrl_grps
        jnt_grps = self.jnt_grps
        noxform_grp = self.noxform_grp
        world_scale_attr = self.hooks[0] + '.worldScale'

        num_joints = options.get('numberJoints')
        number_mid_ctrl = options.get('numberMidCtrls')
        create_jaw = options.get('createJaw')
        create_skull = options.get('createReverseJaw')
        pickWalk_parent = options.get('pickWalkParent')
        create_surface = options.get('createSurfaceDriver')
        create_fk_ctrls = options.get('createFKShaperCtrls')

        ctrl_suffix = 'CTL'
        jnt_suffix = 'JNT'
        zero_suffix = 'CTL_ZERO'

        create_fk_ctrls = options.get('createFKShaperCtrls')

        # find all jnts
        jaw_jnt = prefix + '_jaw_' + jnt_suffix
        head_jnt = prefix + '_head_' + jnt_suffix
        head_end_jnt = prefix + '_head_end_' + jnt_suffix
        rev_jaw_jnt = prefix + '_reverseJaw_' + jnt_suffix

        neck_jnts = []
        ik_jnts = []
        for i in range(num_joints - 1):
            letter = utils.letters[i]
            jnt_name = ('{0}_neck_{1}_{2}'.format(prefix, letter, jnt_suffix))
            neck_jnts.append(jnt_name)

        # ik_name =  ('{0}_neckIK_{1}_{2}'.format(prefix, letter, jnt_suffix))

        crv_jnts = neck_jnts + [head_jnt, head_end_jnt]

        spline_jnts = [neck_jnts[0] + '_PLC_REF']
        for i in range(1, 3):
            letter = utils.letters[i]
            spline_jnts.append('{0}_neckSpline_{1}_{2}_PLC_REF'.format(prefix, letter, jnt_suffix))

        spline_jnts.append(head_jnt + '_PLC_REF')

        # create ctrls
        ct_name = prefix + '_head_' + ctrl_suffix
        head_zero, head_ctrl, head_offsets, head_last_node = self.anim_ctrl(ct_name)

        ct_name = prefix + '_neckBase_' + ctrl_suffix
        neck_base_zero, neck_base_ctrl, neck_base_offsets, neck_base_last_node = self.anim_ctrl(ct_name)

        fk_zeros, fk_ctrls, fk_offsets, fk_last_nodes = [], [], [], []
        for i, jnt in enumerate(neck_jnts + [head_jnt]):
            ltr = utils.letters[i]
            fk_name = '{0}_neck_FK_{1}_{2}'.format(prefix, ltr, ctrl_suffix)

            if jnt == head_jnt:
                fk_name = '{0}_head_FK_{2}'.format(prefix, ltr, ctrl_suffix)

            zero, ctrl, offsets, last_node = self.anim_ctrl(fk_name)

            if create_fk_ctrls:
                if fk_ctrls:
                    mc.parent(zero, fk_ctrls[-1])
            else:
                mc.parent(zero, ctrl_grps[0])

            fk_zeros.append(zero)
            fk_ctrls.append(ctrl)
            fk_offsets.append(offsets)
            fk_last_nodes.append(last_node)

        if create_surface:
            # create MID neck ctrls
            mid_zeros, mid_ctrls, mid_offsets, mid_last_nodes = [], [], [], []
            div = 1.0 / (number_mid_ctrl + 1)

            for i in range(number_mid_ctrl):
                if number_mid_ctrl == 1:
                    ct_name = '{0}_midNeck_{1}'.format(prefix, ctrl_suffix)

                else:
                    ltr = utils.letters[i]
                    ct_name = '{0}_midNeck_{1}_{2}'.format(prefix, ltr, ctrl_suffix)

                mid_zero, mid_ctrl, mid_off, mid_last = self.anim_ctrl(ct_name)

                mid_zeros.append(mid_zero)
                mid_ctrls.append(mid_ctrl)
                mid_offsets.append(mid_off)
                mid_last_nodes.append(mid_last)

                # Create orient contraionts
                aim_amount = div * (i + 1)
                aim_grp = mid_ctrl + '_CONST'
                aim_head = mc.duplicate(mid_ctrl + '_CONST', n=mid_ctrl + '_aim_head_GRP', po=1)[0]
                aim_hip = mc.duplicate(mid_ctrl + '_CONST', n=mid_ctrl + '_aim_hip_GRP', po=1)[0]

                mc.parent(mid_ctrl + '_MOCAP', mid_zero)
                mc.aimConstraint(head_last_node, aim_head, aim=[0, 1, 0], u=[1, 0, 0], wu=[1, 0, 0],
                                 wut='objectRotation', wuo=head_ctrl, mo=1)
                mc.aimConstraint(neck_base_zero, aim_hip, aim=[0, -1, 0], u=[1, 0, 0], wu=[1, 0, 0],
                                 wut='objectRotation', wuo=neck_base_zero, mo=1)

                mc.parent(mid_ctrl + '_MOCAP', aim_grp)
                mc.parent(aim_grp, aim_head, aim_hip, w=1)

                mc.pointConstraint(head_last_node, mid_zero, weight=aim_amount)
                mc.pointConstraint(neck_base_zero, mid_zero, weight=1.0 - aim_amount)
                mc.parent(aim_grp, aim_head, aim_hip, mid_zero)

                oc = mc.orientConstraint(aim_head, aim_grp, weight=aim_amount)
                oc = mc.orientConstraint(aim_hip, aim_grp, weight=1.0 - aim_amount)

                mc.setAttr(oc[0] + '.interpType', 2)

        # Create jaw
        if create_jaw:
            ct_name = prefix + '_jaw_' + ctrl_suffix
            jaw_zero, jaw_ctrl, jaw_offsets, jaw_last_node = self.anim_ctrl(ct_name)
            mc.parent(jaw_zero, head_last_node)

            if create_skull:
                ct_name = prefix + '_reverseJaw_' + ctrl_suffix
                skull_zero, skull_ctrl, skull_offsets, skull_last_node = self.anim_ctrl(ct_name)
                mc.parent(skull_zero, head_last_node)

        # parent ctrls
        if create_surface:
            mc.parent(mid_zeros, ctrl_grps[0])
        mc.parent(neck_base_zero, ctrl_grps[0])
        mc.parent(head_zero, neck_base_last_node)

        # now create spline
        spline_driver_nodes = []
        for i, sj in enumerate(spline_jnts):
            g = mc.createNode('transform', n=prefix + '_neckSplineDrv' + utils.letters[i] + '_GRP')
            mc.delete(mc.pointConstraint(sj, g))
            spline_driver_nodes.append(g)

        mc.parent(spline_driver_nodes[0], neck_base_zero)
        mc.parent(spline_driver_nodes[-1], head_last_node)

        # now parent and  create spline
        if create_surface:
            if number_mid_ctrl == 1:
                mc.parent(spline_driver_nodes[1:3], mid_ctrls[0])

            else:
                for i in range(len(mid_ctrls)):
                    mc.parent(spline_driver_nodes[i + 1], mid_ctrls[i])
        else:
            tmp_spline_drivers = [spline_driver_nodes[0], spline_driver_nodes[-1]]
            spline_driver_nodes.remove(spline_driver_nodes[0])
            spline_driver_nodes.remove(spline_driver_nodes[-1])
            mc.delete(spline_driver_nodes)
            spline_driver_nodes = tmp_spline_drivers

        # flatten neck joints
        mc.parent(neck_jnts, head_jnt, jnt_grps[0])
        jnts = neck_jnts + [head_jnt]
        ik_jnts = []
        if not create_surface:
            for i, jnt in enumerate(jnts):
                dup = mc.duplicate(jnt, n=jnt.replace('JNT', 'ik_jnt'))
                if i > 0:
                    mc.parent(dup[0], ik_jnts[-1])
                if jnt == head_jnt:
                    head_end = utils.get_children(dup[0])
                    if head_end:
                        mc.delete(head_end)
                ik_jnts.append(dup[0])
                constraint.constraint_mtx(dup[0], fk_zeros[i])

        width = utils.get_distance(jnts[0], jnts[1]) * 0.4
        if create_surface:
            crv = spline.create_curve_mtx(spline_driver_nodes, degree=2, name=prefix + '_neck', parent=noxform_grp)
            surf = spline.create_surface_mtx(spline_driver_nodes, name=prefix + '_neck', parent=noxform_grp,
                                             width=width, stretch=1)

            mc.addAttr(head_ctrl, ln='stretch', k=1, min=0, max=1)
            mc.addAttr(head_ctrl, ln='uniformStretch', k=1, min=0, max=1)

        else:

            # if not deforming by surface create top and bottom neck joints to drive ik curve, then move joints back by width
            if not create_surface:
                top_crv_jnt_name = '{0}_neckSpline_top_dvr_jnt'.format(prefix)
                btm_crv_jnt_name = '{0}_neckSpline_btm_dvr_jnt'.format(prefix)
                btm_jnt = mc.createNode('joint', n=btm_crv_jnt_name, p=spline_driver_nodes[0])
                # mc.setAttr (btm_jnt+'.tz', (width*-4))
                top_jnt = mc.createNode('joint', n=top_crv_jnt_name, p=spline_driver_nodes[-1])
                # mc.setAttr (top_jnt+'.tz', (width*-4))

            # create spline ik handle and stretch
            name = prefix + '_neckSpline'
            ik_build = mc.ikHandle(sj=ik_jnts[0], ee=ik_jnts[-1], n=name + '_ikh', sol='ikSplineSolver', pcv=1, ns=3)
            crv_inf = mc.createNode('curveInfo', n=name + '_crvinf')
            curve_shape = mc.listRelatives(ik_build[2], s=1)
            md = mc.createNode('multiplyDivide', n=name + '_md')
            md_global = mc.createNode('multiplyDivide', n=name + '_md_global')
            mc.connectAttr((curve_shape[0] + '.worldSpace[0]'), (crv_inf + '.inputCurve'))
            mc.connectAttr((crv_inf + '.arcLength'), (md + '.input1X'))
            mc.setAttr(md + '.operation', 2)
            mc.setAttr(md_global + '.input1X', (mc.getAttr(crv_inf + '.arcLength')))
            mc.connectAttr(md_global + '.outputX', (md + '.input2X'))
            mc.rebuildCurve(ik_build[2], ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kep=1, kt=0, s=1, d=3, tol=0.01)
            for jnt in ik_jnts:
                mc.setAttr(jnt + '.segmentScaleCompensate', 1)
                # mc.connectAttr(md + '.outputX', jnt + '.sx')
            mc.select(cl=1)
            bs_curve = mc.duplicate(ik_build[2], rr=1, n=name + '_crv_bs')
            bs = mc.blendShape(bs_curve[0], ik_build[2], o='local', n=name + 'bend_bs')
            mc.setAttr(bs[0] + '.' + bs_curve[0], 1)
            # calculate the twist factor and feed into ik handle twist attr
            # constraint.constraint_mtx (head_last_node, spline_driver_nodes[-1], t=0, o=1)
            # mc.connectAttr (spline_driver_nodes[-1]+'.rz', ik_build[0]+'.twist')

            # skin cluster spline driver joints to bs curve
            sc = mc.skinCluster(bs_curve, btm_crv_jnt_name, top_crv_jnt_name, tsb=1)
            mc.parent(ik_build[0], noxform_grp)
            mc.parent(bs_curve[0], noxform_grp)
            # mc.parent(ik_jnts[0], jnt_grps[0])
            mc.parent(ik_build[2], noxform_grp)

        # connect to spline
        fkcurl_drvs = []

        for i, jnt in enumerate(jnts):
            constraint.freeze_joint_orient(jnt)
            mc.setAttr(jnt + '.segmentScaleCompensate', 0)
            drv = mc.createNode('transform', p=fk_zeros[i], n=fk_zeros[i] + '_ATT')
            mc.parent(drv, w=1)
            fkcurl_drvs.append(drv)
            constraint.constraint_mtx(fk_ctrls[i], jnt, s=0)
            if not create_surface:
                constraint.constraint_mtx(ik_jnts[i], drv, s=0)

        if create_surface:
            mc.delete(crv)
            for zero in fk_zeros:
                att = zero + '_ATT'
                rivet.surface_mtx2(surf, att, percentage=1)

            for a in ['stretch']:
                mc.connectAttr(head_ctrl + '.' + a, surf + '.' + a)
        else:
            for i, zero in enumerate(fk_zeros):
                att = zero + '_ATT'
                constraint.constraint_mtx(ik_jnts[i], att, mo=1)

        # if build option set to create fk chain control, parent fk ctrls as fk chain
        for i, drv in enumerate(fkcurl_drvs):
            if create_fk_ctrls:
                if i > 0:
                    mc.parent(drv, fkcurl_drvs[i - 1])
            else:
                grp_name = '{0}_neckShaper_CTLS'.format(prefix)
                if not mc.objExists(grp_name):
                    grp = mc.createNode('transform', n=grp_name, p=ctrl_grps[0])
                mc.parent(drv, fkcurl_drvs[i])
                att_grp = '{0}_neckShaper_ATT_DVRS'.format(prefix)
                if not mc.objExists(grp_name):
                    att_grp = mc.createNode('transform', n=att_grp, p=ctrl_grps[0])

        if create_fk_ctrls:
            for i, ik_jnt in enumerate(ik_jnts):
                mc.connectAttr(fk_zeros[i] + '_ATT.t', fk_zeros[i] + '.t')
                mc.connectAttr(fk_zeros[i] + '_ATT.r', fk_zeros[i] + '.r')

            try:
                mc.parent(fk_zeros[0], ctrl_grps[0])
            except:
                pass

            # scales and preserve volume
            if len(neck_jnts) > 1:
                spline.ramp_scale([neck_base_ctrl] + mid_ctrls + [head_ctrl], jnts[:-1], interpolation=4,
                                  driver_attr='neckScale')

            spline.preserve_volume(fk_ctrls, jnts[:-1], head_ctrl)

            constraint.constraint_mtx(head_last_node, fk_zeros[-1], t=1, o=1, s=1)

        # connect head jaw and reverse jaw jnts
        if create_jaw:
            constraint.freeze_joint_orient(jaw_jnt)
            constraint.constraint_mtx(jaw_last_node, jaw_jnt)
            constraint.constraint_mtx(head_jnt, jaw_zero)

            if create_skull:
                constraint.freeze_joint_orient(rev_jaw_jnt)
                constraint.constraint_mtx(skull_last_node, rev_jaw_jnt)
                constraint.constraint_mtx(head_jnt, skull_zero)

        # connect gsc
        # control.create_movable_pivot(neck_base_ctrl)
        # control.create_movable_pivot(head_ctrl)

        # mm.eval('transformLimits -sz 0.001 1 -esz 1 0 %s ;' % head_ctrl)
        # mm.eval('transformLimits -sy 0.001 1 -esy 1 0 %s ;' % head_ctrl)
        # mm.eval('transformLimits -sx 0.001 1 -esx 1 0 %s ;' % head_ctrl)

        # lock stuff
        if create_surface:
            all_mid_offsets = []
            for moff in mid_offsets:
                all_mid_offsets.extend(moff)
            utils.set_attrs(all_mid_offsets, ' s v', l=1, k=0)

        utils.set_attrs(fk_ctrls, 's v', l=1, k=0)
        utils.set_attrs(head_offsets + neck_base_offsets, ' s v', l=1, k=0)

        spaces.tag(head_ctrl, arg='neckBase:' + neck_base_last_node, default=1)

        # Setup pickwalking
        if create_jaw:
            pickWalk.attribute_tag(jaw_ctrl, head_ctrl)

            if create_skull:
                pickWalk.attribute_tag(skull_ctrl, head_ctrl)

        pickWalk.attribute_tag(head_ctrl, neck_base_ctrl)
        pickWalk.attribute_tag(neck_base_ctrl, pickWalk_parent)

        if create_fk_ctrls:
            self.create_ctrl_set('FK', fk_ctrls)

            # Setup pickwaliking attributes for the fingers
            i = 0

            fk_ctrls.reverse()
            pickWalk.attribute_tag(head_ctrl, fk_ctrls[0])
            for ctrl in fk_ctrls:

                if i + 1 < len(fk_ctrls):

                    pickWalk.attribute_tag(fk_ctrls[i], fk_ctrls[i + 1])
                else:
                    pickWalk.attribute_tag(fk_ctrls[i], neck_base_ctrl)
                    break

                i += 1
            fk_ctrls.reverse()

        self.finalize_part()
