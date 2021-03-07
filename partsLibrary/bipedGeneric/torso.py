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


class Torso(standardPart.StandardPart):
    """Biped or quad FK / IK torso.

    Note:
    The difference between this module and the spine module has to do with the way the controls and joints are setup and parented
    This module drives a live lofted surface with two curves driven by spline ik jnts
    The other main difference is this module creates a true fk chain for each joint that will follow IK spine surface.
     FK control is created for each joint and will peel or curl off from surface.
    This setup is good if you need a true fk/ik setup for each joint and do not need a reverse fk setup


     Build Options:
            :side: (str) Side token for this rig part. Defaults to "C".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_root_JNT".
            :numberJoints: (int) Numder of torso joints. Defaults to 6.
            :numberMidCtrls: (int) Number of mid torso IK ctrls. Defaults to 1.
            :createFkCtrls: (bool) Create FK offset ctrls that can peel off the spline. Defaults to True."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('side', default='C')
        self.add_option('parent', data_type='hook', default='C_root_JNT')

        self.add_option('numberJoints',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=6,
                        tool_tip='Number of torso joints.',
                        min=0)

        self.add_option('numberMidCtrls',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=1,
                        min=1,
                        tool_tip='Number of mid torso IK ctrls.')

        self.add_option('pickWalkParent',
                        data_type='string',
                        default='world_CTL',
                        selectable=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix
        options = self.options
        mirror_value = self.mirror_value
        # noxform_grp      = self.noxform_grp

        number_mid_ctrl = options.get('numberMidCtrls')
        num_joints = options.get('numberJoints')
        noxform_grp = self.guide_master + '_NOX'
        length = 5

        if number_mid_ctrl == 1:
            num_spl_jnts = 4
        else:
            num_spl_jnts = number_mid_ctrl + 2

        # layout spline placers and jnts
        jnt_zeros, plcs, jnts = self.guide_joint_chain('torso', num_joints=num_joints, length=length)
        spline_zeros, spline_plcs = self.guide_joint_chain('torsoSpline', num_joints=num_spl_jnts,
                                                           flat_plc_hierarchy=True,
                                                           flat_jnt_hierarchy=True,
                                                           placer_only=True,
                                                           length=length)

        # mc.delete(plcs[0]+'Shape', plcs[-1]+'Shape')
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
                                             name=prefix + '_torsoSplinePlc',
                                             axis='Y',
                                             degree=2,
                                             parent=noxform_grp)

        spline_surf = spline.create_surface_mtx(spline_plcs,
                                                name=prefix + '_torsoSplinePlc',
                                                axis='Y',
                                                degree=2,
                                                parent=noxform_grp)

        # spline.create_stretch_crv(spline_crv, globalScale='world_CTL.worldScale')
        # param_nodes = spline.connect_param_node(spline_crv, spline_surf, jnt_zeros)
        # param_nodes=rivet.surface_fll(nodes=jnt_zeros, surf=spline_surf, noxform_grp=noxform_grp)
        spline.create_stretch_crv(spline_crv)
        rivet.surface_mtx(spline_surf, jnt_zeros, noxform_grp)

        # for p in param_nodes:
        #     mc.setAttr(p+'.stretch', 1)
        #     mc.setAttr(p+'.uniformStretch', 1)

        # create chest
        chest_zero, chest_plc, chest_jnt = self.guide_joint('chest_end')
        pos = mc.xform(plcs[-1], q=1, ws=1, t=1)
        mc.xform(chest_zero, ws=1, t=pos)
        mc.xform(chest_zero, r=1, t=[0, 3, 0])
        mc.parent(chest_jnt, jnts[-1])
        mc.parent(chest_zero, spline_plcs[-1])

        mc.aimConstraint(chest_plc, jnts[-1],
                         aim=[1, 0, 0], u=[0, 1, 0], wu=[0, 1, 0],
                         wut='objectRotation', wuo=spline_plcs[-1])

        # create hip
        hip_zero, hip_plc, hip_jnt = self.guide_joint('hip')
        pos = mc.xform(plcs[0], q=1, ws=1, t=1)
        mc.xform(hip_zero, ws=1, t=pos)
        mc.xform(hip_zero, r=1, t=[0, -0.5, 0])
        mc.delete(mc.orientConstraint(jnts[0], hip_zero))

        mc.parent(jnts[0], hip_jnt)
        mc.parent(hip_zero, spline_plcs[0])

        # Create cog
        cog_ct_zero, cog_ctrl = self.guide_ctrl('cog', shape='cog', color='yellow', scale=[6, 6, 6], axis='X')
        mc.delete(mc.pointConstraint(hip_jnt, cog_ct_zero))
        mc.pointConstraint(hip_jnt, cog_ct_zero, mo=1)
        mc.orientConstraint(noxform_grp, cog_ct_zero, mo=1)
        mc.setAttr(cog_ctrl + '.numOffsetCtrls', 1)

        # Create ctrlas
        chest_ct_zero, chest_ctrl = self.guide_ctrl('chest', shape='chest', color='yellow', scale=[3.6, 3, 3])
        mc.delete(mc.pointConstraint(jnts[-1], chest_ct_zero))
        mc.parentConstraint(jnts[-1], chest_ct_zero, mo=1)

        # Create torso mid ctrls
        aim_grp = mc.createNode('transform', p=spline_plcs[0], n=spline_plcs[0] + '_aim_GRP')
        mc.aimConstraint(spline_plcs[-1], aim_grp, aim=[0, 1, 0], u=[1, 0, 0], wu=[0, -1, 0], wut='objectRotation',
                         wuo=spline_plcs[0])

        # Create hip
        hip_ct_zero, hip_ctrl = self.guide_ctrl('hip', shape='hip', color='yellow', scale=[3.6, 3, 3])
        mc.delete(mc.pointConstraint(hip_jnt, hip_ct_zero))
        mc.pointConstraint(hip_jnt, hip_ct_zero, mo=1)
        mc.orientConstraint(aim_grp, hip_ct_zero, mo=1)

        # Create neck mid ctrls
        mid_ctrl_range = range(1, len(spline_zeros[:-1]))
        if number_mid_ctrl == 1:
            mid_ctrl_range = range(1)

        for i in mid_ctrl_range:
            spl_drv = spline_plcs[i]
            ltr = utils.letters[i - 1]
            ct_name = 'midTorso_' + ltr

            if number_mid_ctrl == 1:
                ct_name = 'midTorso'
                spl_drv = spline_plcs[1:3]

            mid_ct_zero, mid_ctrl = self.guide_ctrl(ct_name, shape='circle', color='pink', scale=[3.6, 3, 3])
            mc.pointConstraint(spl_drv, mid_ct_zero)
            mc.orientConstraint(aim_grp, mid_ct_zero)

            utils.set_attrs(utils.get_parent(mid_ctrl), 't', l=1, k=0)

            piv_ctrl = utils.get_parent(mid_ctrl)
            utils.set_attrs(piv_ctrl, 't s', l=1, k=0)

        fk_zeros = []
        fk_ctrls = []
        for i, jnt in enumerate(jnts[:-1]):
            fk_name = 'torso_FK_' + utils.letters[i]
            fk_zero, fk_ctrl = self.guide_ctrl(fk_name, driver=jnt, create_pivot=0, allow_offset_ctrls=0,
                                               shape='pin_circle', color='light_blue', scale=[2] * 3)
            mc.xform(fk_ctrl + '.cv[*]', r=1, ro=[-90, 0, 0])
            fk_zeros.append(fk_zero)
            fk_ctrls.append(fk_ctrl)

        # lock stuff
        utils.set_attrs(spline_plcs[:-1], 'r ', l=1, k=0)
        utils.set_attrs(chest_plc, 'r', l=1, k=0)

        utils.set_attrs(plcs, l=1, k=0)

        chest_name = prefix + '_chest_JNT'
        mc.rename(jnt_zeros[-1], chest_name + '_ZERO')
        mc.rename(jnts[-1], chest_name)

        mc.rename(plcs[0], plcs[0] + '_DUMMY')
        mc.rename(plcs[-1], plcs[-1] + '_DUMMY')

        mc.rename(spline_plcs[0], plcs[0])
        mc.rename(spline_plcs[-1], chest_name + '_PLC')

        fk_name = 'chest_FK'
        fk_zero, fk_ctrl = self.guide_ctrl(fk_name, driver=chest_name, allow_offset_ctrls=0, create_pivot=0,
                                           shape='pin_circle', color='light_blue', scale=[2] * 3)
        mc.xform(fk_ctrl + '.cv[*]', r=1, ro=[-90, 0, 0])
        fk_zeros.append(fk_zero)
        fk_ctrls.append(fk_ctrl)

        ctrl = utils.get_parent(chest_ctrl)
        utils.set_attrs(ctrl, 's', l=1, k=0)

        ctrl = utils.get_parent(hip_ctrl)
        utils.set_attrs(ctrl, 's', l=1, k=0)

        ctrl = utils.get_parent(cog_ctrl)
        utils.set_attrs(ctrl, 's', l=1, k=0)

        mc.xform(spline_zeros, r=1, t=[0, -self.mirror_value, 0])
        mc.setAttr(self.guide_master + '.offsetTranslateZ', -0.5 * self.mirror_value)

        mc.setAttr(chest_ctrl + '.numOffsetCtrls', 1)
        mc.setAttr(hip_ctrl + '.numOffsetCtrls', 1)

        # This finalizes your guide.
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

        pickWalk_parent = options.get('pickWalkParent')

        num_joints = options.get('numberJoints')
        number_mid_ctrl = options.get('numberMidCtrls')

        # finda all jnts
        chest_jnt = prefix + '_chest_JNT'
        chest_end_jnt = prefix + '_chest_end_JNT'
        hip_jnt = prefix + '_hip_JNT'

        torso_jnts = []
        for i in range(num_joints - 1):
            letter = utils.letters[i]
            torso_jnts.append('{0}_torso_{1}_JNT'.format(prefix, letter))

        spline_jnts = [torso_jnts[0] + '_PLC_REF']
        for i in range(1, 3):
            letter = utils.letters[i]
            spline_jnts.append('{0}_torsoSpline_{1}_JNT_PLC_REF'.format(prefix, letter))
        spline_jnts.append(chest_jnt + '_PLC_REF')

        # create ctrls
        ct_name = prefix + '_chest_CTL'
        chest_zero, chest_ctrl, chest_offsets, chest_last_node = self.anim_ctrl(ct_name)

        ct_name = prefix + '_hip_CTL'
        hip_zero, hip_ctrl, hip_offsets, hip_last_node = self.anim_ctrl(ct_name)

        ct_name = prefix + '_cog_CTL'
        cog_zero, cog_ctrl, cog_offsets, cog_last_node = self.anim_ctrl(ct_name)

        fk_zeros, fk_ctrls, fk_offsets, fk_last_nodes = [], [], [], []
        for i, jnt in enumerate(torso_jnts + [chest_jnt]):
            ltr = utils.letters[i]
            fk_name = '{0}_torso_FK_{1}_CTL'.format(prefix, ltr)

            if jnt == chest_jnt:
                fk_name = '{0}_chest_FK_CTL'.format(prefix, ltr)
            zero, ctrl, offsets, last_node = self.anim_ctrl(fk_name)

            if fk_ctrls:
                mc.parent(zero, fk_ctrls[-1])
            fk_zeros.append(zero)
            fk_ctrls.append(ctrl)
            fk_offsets.append(offsets)
            fk_last_nodes.append(last_node)

        # create MID torso ctrls
        mid_zeros, mid_ctrls, mid_offsets, mid_last_nodes = [], [], [], []
        div = 1.0 / (number_mid_ctrl + 1)

        for i in range(number_mid_ctrl):
            if number_mid_ctrl == 1:
                ct_name = '{0}_midTorso_CTL'.format(prefix)

            else:
                ltr = utils.letters[i]
                ct_name = '{0}_midTorso_{1}_CTL'.format(prefix, ltr)

            mid_zero, mid_ctrl, mid_off, mid_last = self.anim_ctrl(ct_name)

            mid_zeros.append(mid_zero)
            mid_ctrls.append(mid_ctrl)
            mid_offsets.append(mid_off)
            mid_last_nodes.append(mid_last)

            # Create orient contraionts
            aim_amount = div * (i + 1)
            aim_grp = mid_ctrl + '_CONST'

            aim_chest = mc.duplicate(aim_grp, po=1, n=mid_ctrl + '_aim_chest_GRP')[0]
            aim_hip = mc.duplicate(aim_grp, po=1, n=mid_ctrl + '_aim_hip_GRP')[0]
            mc.parent(aim_chest, chest_last_node)
            mc.parent(aim_hip, hip_last_node)

            prc = mc.parentConstraint(chest_last_node, aim_grp, weight=aim_amount, mo=1)
            prc = mc.parentConstraint(hip_last_node, aim_grp, weight=1.0 - aim_amount, mo=1)
            mc.setAttr(prc[0] + '.interpType', 2)

        # parent ctrls
        mc.parent(chest_zero, mid_zeros, hip_zero, cog_last_node)

        spline_driver_nodes = []
        for i, sj in enumerate(spline_jnts):
            g = mc.createNode('transform', n=prefix + '_torsoSplineDrv' + utils.letters[i] + '_GRP')
            mc.delete(mc.pointConstraint(sj, g))
            spline_driver_nodes.append(g)

        # mc.delete(mc.pointConstraint(hip_ctrl, spline_driver_nodes[0]))

        mc.parent(spline_driver_nodes[0], hip_last_node)
        mc.parent(spline_driver_nodes[-1], chest_last_node)

        # now create spline
        if number_mid_ctrl == 1:
            mc.parent(spline_driver_nodes[1:3], mid_ctrls[0])

        else:
            for i in range(len(mid_ctrls)):
                mc.parent(spline_driver_nodes[i + 1], mid_ctrls[i])

        # flatten torso joints
        mc.parent(torso_jnts, chest_jnt, hip_jnt, jnt_grps[0])
        nodes_to_connect = torso_jnts + [chest_jnt]

        # Create spline ands surf
        jnts = torso_jnts + [chest_jnt]

        width = utils.get_distance(jnts[0], jnts[1]) * 0.4

        crv = spline.create_curve_mtx(spline_driver_nodes, degree=2, name=prefix + '_torso', parent=noxform_grp)
        surf = spline.create_surface_mtx(spline_driver_nodes, name=prefix + '_torso', parent=noxform_grp, width=width,
                                         stretch=True)

        mc.addAttr(chest_ctrl, ln='stretch', k=1, min=0, max=1)
        mc.addAttr(chest_ctrl, ln='reverseRoot', k=1, min=0, max=1)

        # connect to spline
        fkcurl_drvs = []
        mc.makeIdentity(jnts, apply=1, t=1, r=1, s=1, n=0, pn=1)

        for i, jnt in enumerate(jnts):
            constraint.freeze_joint_orient(jnt)
            mc.setAttr(jnt + '.segmentScaleCompensate', 0)

            drv = mc.createNode('transform', p=fk_zeros[i], n=fk_zeros[i] + '_ATT')
            mc.parent(drv, w=1)

            fkcurl_drvs.append(drv)

            # need an offset node to eat some precision errors
            constraint.constraint_mtx(fk_ctrls[i], jnt, s=0)

        mc.delete(crv)
        for i, zero in enumerate(fk_zeros):
            att = zero + '_ATT'
            rivet.surface_mtx2(surf, att, percentage=1)

        mc.setAttr(surf + '.uniformStretch', 1)
        for a in ['stretch', 'reverseRoot']:
            mc.connectAttr(chest_ctrl + '.' + a, surf + '.' + a)

        for i, drv in enumerate(fkcurl_drvs):
            if i > 0:
                mc.parent(drv, fkcurl_drvs[i - 1])
        mc.parent(fkcurl_drvs[0], ctrl_grps[0])

        for i, jnt in enumerate(jnts):
            mc.connectAttr(fk_zeros[i] + '_ATT.t', fk_zeros[i] + '.t')
            mc.connectAttr(fk_zeros[i] + '_ATT.r', fk_zeros[i] + '.r')

        # constrain chest jnt and hip jnt
        mc.parent(hip_jnt, torso_jnts[0])
        constraint.constraint_mtx(chest_last_node, fk_zeros[-1], t=0, s=0)

        pos = mc.createNode('transform', n=hip_jnt + '_POS', p=hip_last_node)

        mc.pointConstraint(torso_jnts[0], pos)
        mc.parentConstraint(pos, hip_jnt, mo=1)

        # setup ramp scale and volume preservation
        spline.ramp_scale([hip_ctrl] + mid_ctrls + [chest_ctrl], [hip_jnt] + jnts, interpolation=4,
                          driver_attr='torsoScale')
        spline.preserve_volume(fk_ctrls, jnts, chest_ctrl)

        # movable pivots
        control.create_movable_pivot(cog_ctrl)
        control.create_movable_pivot(chest_ctrl)
        control.create_movable_pivot(hip_ctrl)

        # lock and parent stuff
        mc.parent(fk_zeros[0], ctrl_grps[0])
        mc.parent(cog_zero, ctrl_grps[0])

        all_mid_offsets = []
        for moff in mid_offsets:
            all_mid_offsets.extend(moff)

        utils.set_attrs(fk_ctrls, ' s v', l=1, k=0)
        utils.set_attrs(chest_offsets + hip_offsets + all_mid_offsets + cog_offsets, ' s v', l=1, k=0)
        utils.set_attrs(cog_ctrl, 's v', l=1, k=0)

        utils.set_attrs([chest_ctrl, hip_ctrl] + mid_ctrls, ' s v', l=1, k=0)

        # node for cog space
        spc = mc.createNode('transform', p=cog_last_node, n=prefix + '_cog_space_GRP')
        utils.set_attrs(spc, l=1, k=0)

        # tag spaces
        spaces.tag(chest_ctrl, add_parent_space=False)
        spaces.tag(hip_ctrl, add_parent_space=False)

        jnts = [hip_jnt] + torso_jnts + [chest_jnt, chest_end_jnt]
        # #utils.create_cfx_curves(jnts, self.prefix+'_'+self.part_type)

        # Setup pick walking for mid ik ctrls
        pickWalk.attribute_tag(chest_ctrl, mid_ctrls[-1])

        i = 0
        mid_ctrls.reverse()
        for ctrl in mid_ctrls:

            if i + 1 < len(mid_ctrls):

                pickWalk.attribute_tag(mid_ctrls[i], mid_ctrls[i + 1])
                print
                mid_ctrls[i], mid_ctrls[i + 1]
            else:
                pickWalk.attribute_tag(mid_ctrls[i], hip_ctrl)
                break
            i += 1

        pickWalk.attribute_tag(hip_ctrl, cog_ctrl)  # There may be multiple ik chains
        pickWalk.attribute_tag(cog_ctrl, pickWalk_parent)

        # This finalizes guide and creates rig sets
        self.create_ctrl_set('FK', fk_ctrls)

        fk_ctrls.reverse()
        i = 0
        for ctrl in fk_ctrls:

            if i + 1 < len(fk_ctrls):

                pickWalk.attribute_tag(fk_ctrls[i], fk_ctrls[i + 1])
            else:
                pickWalk.attribute_tag(fk_ctrls[i], hip_ctrl)
                break

            i += 1
        fk_ctrls.reverse()

        self.finalize_part()

    def rebuild_guide_post(self):

        prefix = self.prefix
        num_joints = self.options.get('numberJoints')
        chest_jnt = prefix + '_chest_JNT'

        torso_jnts = []
        for i in range(num_joints - 1):
            letter = utils.letters[i]
            torso_jnts.append('{0}_{1}_JNT'.format(prefix, letter))

        ctrls = []
        for i, jnt in enumerate(torso_jnts[:-1] + [chest_jnt]):
            ltr = utils.letters[i]
            fk_name = '{0}_torso_FK_{1}_CTL'.format(prefix, ltr)
            ctrls.append(fk_name)

        mc.xform(ctrls, a=1, t=[0, 0, 0], ro=[0, 0, 0])
