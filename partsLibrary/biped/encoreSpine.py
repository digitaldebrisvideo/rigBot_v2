# -*- rigBot: part -*-
import maya.cmds as mc
import maya.mel as mm
import pymel.core as pm

from rigBot import spline
from rigBot import utils

reload(spline)
from rigBot import control
from rigBot import rivet
from rigBot import spaces
from rigBot import pickWalk
from rigBot import env
from rigBot import constraint
from rigBot.partsLibrary import standardPart

class EncoreSpine(standardPart.StandardPart):
    """Biped or quad FK / IK spine. Uses cmSplineChain plugin node.
        You also have the option to build as a vanila maya rig with no plugin nodes.

        Note:
            The option to build as vanilla maya rig is set per asset in the ${ASSET}_buildList.py
            Guide rig parts will always build with cmRigNodes plugin nodes.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "c".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_root_JNT".
            :numberJoints: (int) Numder of spine joints. Defaults to 5.
            :numberMidCtrls: (int) Number of mid spine IK ctrls. Defaults to 1.
            :createFkCtrls: (bool) Create FK offset ctrls that can peel off the spline. Defaults to True."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('side', default='C')
        self.add_option('parent', data_type='hook', default='C_root_JNT')

        self.add_option('numberJoints',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=5,
                        tool_tip='Numder of spine joints.',
                        min=0)

        self.add_option('numberMidCtrls',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=1,
                        min=1,
                        tool_tip='Number of mid spine IK and FK ctrls.')

        self.add_option('makeReverseFk',
                        data_type='bool',
                        default=True,
                        rebuild_to_modify=True,
                        tool_tip='Add Reverse fk rig.')

        self.add_option('pickWalkParent',
                        data_type='string',
                        default='world_anim',
                        selectable=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix
        options = self.options
        mirror_value = self.mirror_value

        number_ctrl = options.get('numberMidCtrls')
        num_joints = options.get('numberJoints')
        rev_spine = options.get('makeReverseFk')
        noxform_grp = self.guide_master + '_NOX'
        length = 5

        # if number_ctrl == 1:
        #     num_spl_jnts = 4
        # else:
        num_spl_jnts = number_ctrl + 2

        # layout spline placers and jnts

        jnt_zeros, plcs, jnts = self.guide_joint_chain('spine', num_joints=num_joints, length=length)
        spline_zeros, spline_plcs = self.guide_joint_chain('spineSpline', num_joints=num_spl_jnts,
                                                           flat_plc_hierarchy=True,
                                                           flat_jnt_hierarchy=True,
                                                           placer_only=True,
                                                           length=length)

        # mc.delete(plcs[0]+'Shape', plcs[-1]+'Shape')
        self.tag_as_ref(spline_plcs)

        # Constraint center spline nodes
        if num_spl_jnts == 3:
            mc.pointConstraint(spline_plcs[0], spline_plcs[-1], spline_zeros[1], w=.5)
        else:
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
                                             name=prefix + '_spineSplinePlc',
                                             axis='Y',
                                             degree=2,
                                             parent=noxform_grp)

        spline_surf = spline.create_surface_mtx(spline_plcs,
                                                name=prefix + '_spineSplinePlc',
                                                axis='Y',
                                                degree=2,
                                                parent=noxform_grp)

        # param_nodes = spline.connect_param_node(spline_crv, spline_surf, jnt_zeros)
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
        # mc.xform(hip_zero, r=1, t=[0,-0.5,0])
        mc.delete(mc.orientConstraint(jnts[0], hip_zero))

        mc.parent(jnts[0], hip_jnt)
        mc.parent(hip_zero, spline_plcs[0])

        # Create cog
        cog_zero, cog_plc, cog_jnt = self.guide_joint('cog')
        cog_ct_zero, cog_ctrl = self.guide_ctrl('cog', driver=cog_plc, shape='square', color='yellow', scale=[6, 6, 6])
        # mc.delete(mc.pointConstraint(hip_jnt, cog_ct_zero))
        mc.xform(cog_zero, r=1, t=[0, -0.5, 0])
        mc.orientConstraint(noxform_grp, cog_zero, mo=1)
        mc.setAttr(cog_ctrl + '.numOffsetCtrls', 3)

        # Create ctrls
        chest_ct_zero, chest_ctrl = self.guide_ctrl('chest', shape='chest', color='yellow', scale=[3.6, 3, 3])
        mc.delete(mc.pointConstraint(jnts[-1], chest_ct_zero))
        mc.parentConstraint(jnts[-1], chest_ct_zero, mo=1)

        # Create spine mid ctrls
        aim_grp = mc.createNode('transform', p=spline_plcs[0], n=spline_plcs[0] + '_aim_GRP')
        mc.aimConstraint(spline_plcs[-1], aim_grp, aim=[0, 1, 0], u=[1, 0, 0], wu=[0, -1, 0], wut='objectRotation',
                         wuo=spline_plcs[0])

        # Create hip
        hip_ct_zero, hip_ctrl = self.guide_ctrl('hip', shape='hip', color='yellow', scale=[3.6, 3, 3])
        mc.delete(mc.pointConstraint(hip_jnt, hip_ct_zero))
        mc.pointConstraint(hip_jnt, hip_ct_zero, mo=1)
        mc.orientConstraint(aim_grp, hip_ct_zero, mo=1)

        # Create spine mid ctrls
        mid_ctrl_range = range(1, len(spline_zeros[:-1]))
        if number_ctrl == 1:
            mid_ctrl_range = range(1)

        # create first and last fk and revfk ctrls

        fk_zeros = []
        fk_ctrls = []
        rev_fk_zeros = []
        rev_fk_ctrls = []

        fk_zero, fk_ctrl = self.guide_ctrl('spine_FK_0', driver=jnts[0], create_pivot=0, allow_offset_ctrls=0,
                                           shape='square', color='light_blue', scale=[2] * 3)
        mc.xform(fk_ctrl + '.cv[*]', r=1, ro=[0, 0, 90])
        fk_zeros.append(fk_zero)
        fk_ctrls.append(fk_ctrl)

        fk_zero, fk_ctrl = self.guide_ctrl('spine_FK_chest', driver=jnts[-1], create_pivot=0, allow_offset_ctrls=0,
                                           shape='square', color='light_blue', scale=[2] * 3)
        mc.xform(fk_ctrl + '.cv[*]', r=1, ro=[0, 0, 90])
        fk_zeros.append(fk_zero)
        fk_ctrls.append(fk_ctrl)

        rev_fk_zero, rev_fk_ctrl = self.guide_ctrl('revSpine_chest', driver=jnts[-1], create_pivot=0,
                                                   allow_offset_ctrls=0, shape='tear_drop', color='dark_magenta',
                                                   scale=[3] * 3)
        mc.xform(rev_fk_ctrl + '.cv[*]', r=1, ro=[-90, 0, 0])
        rev_fk_zeros.append(rev_fk_zero)
        rev_fk_ctrls.append(rev_fk_ctrl)

        rev_fk_zero, rev_fk_ctrl = self.guide_ctrl('revSpine_0', driver=jnts[0], create_pivot=0,
                                                   allow_offset_ctrls=0, shape='tear_drop', color='dark_magenta',
                                                   scale=[3] * 3)

        mc.xform(rev_fk_ctrl + '.cv[*]', r=1, ro=[-90, 0, 0])
        rev_fk_zeros.append(rev_fk_zero)
        rev_fk_ctrls.append(rev_fk_ctrl)

        for i in mid_ctrl_range:
            spl_drv = spline_plcs[i]
            ltr = utils.letters[i - 1]
            numltr = str(i)
            ct_name = 'midSpine_' + ltr
            fk_name = 'spine_FK_' + numltr
            rev_fk_name = 'revSpine_' + numltr

            if number_ctrl == 1:
                ct_name = 'midSpine'
                fk_name = 'spine_FK_1'
                rev_fk_name = 'revSpine_1'
                spl_drv = spline_plcs[1]

            mid_ct_zero, mid_ctrl = self.guide_ctrl(ct_name, shape='circle', color='pink', scale=[3.6, 3, 3])
            mc.pointConstraint(spl_drv, mid_ct_zero)
            mc.orientConstraint(aim_grp, mid_ct_zero)
            utils.set_attrs(utils.get_parent(mid_ctrl), 't', l=1, k=0)
            piv_ctrl = utils.get_parent(mid_ctrl)
            utils.set_attrs(piv_ctrl, 't s', l=1, k=0)

            fk_zero, fk_ctrl = self.guide_ctrl(fk_name, driver=mid_ctrl, create_pivot=0, allow_offset_ctrls=0,
                                               shape='square', color='light_blue', scale=[2] * 3)
            # mc.xform(fk_ctrl + '.cv[*]', r=1, ro=[-90, 0, 0])
            fk_zeros.append(fk_zero)
            fk_ctrls.append(fk_ctrl)

            rev_fk_zero, rev_fk_ctrl = self.guide_ctrl(rev_fk_name, driver=mid_ctrl, create_pivot=0,
                                                       allow_offset_ctrls=0, shape='tear_drop', color='dark_magenta',
                                                       scale=[3] * 3)
            mc.xform(rev_fk_ctrl + '.cv[*]', r=1, ro=[0, 0, 90])
            mc.xform(rev_fk_ctrl + '.cv[*]', r=1, ro=[0, -90, 0])
            rev_fk_zeros.append(rev_fk_zero)
            rev_fk_ctrls.append(rev_fk_ctrl)

        # now create shaper ctrls
        shpr_zeros = []
        shpr_ctrls = []
        for i, jnt in enumerate(jnts):
            shpr_name = 'spineShaper_' + str(i + 1)
            shpr_zero, shpr_ctrl = self.guide_ctrl(shpr_name, driver=jnt, create_pivot=0, allow_offset_ctrls=0,
                                                   shape='pin_circle', color='dark_magenta', scale=[3] * 3)
            mc.xform(shpr_ctrl + '.cv[*]', r=1, ro=[-90, 0, 0])
            shpr_zeros.append(shpr_zero)
            shpr_ctrls.append(shpr_ctrl)

        # lock stuff
        utils.set_attrs(spline_plcs[:-1], 'r ', l=1, k=0)
        utils.set_attrs(chest_plc, 'R', l=1, k=0)

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
                                           shape='square', color='light_blue', scale=[2] * 3)
        mc.xform(fk_ctrl + '.cv[*]', r=1, ro=[0, 0, 90])
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
        rev_spine = options.get('makeReverseFk')

        # find all jnts
        chest_jnt = prefix + '_chest_JNT'
        chest_end_jnt = prefix + '_chest_end_JNT'
        hip_jnt = prefix + '_hip_JNT'

        spine_jnts = []
        for i in range(num_joints - 1):
            letter = utils.letters[i]
            spine_jnts.append('{0}_spine_{1}_JNT'.format(prefix, letter))

        spline_jnts = [spine_jnts[0] + '_PLC_REF']
        num_mids = number_mid_ctrl + 1
        for i in range(1, num_mids):
            letter = utils.letters[i]
            spline_jnts.append('{0}_spineSpline_{1}_JNT_PLC_REF'.format(prefix, letter))
        spline_jnts.append(chest_jnt + '_PLC_REF')
        print
        spline_jnts

        # now create  chest hip and cog ctrls

        ct_name = prefix + '_chest_CTL'
        chest_zero, chest_ctrl, chest_offsets, chest_last_node = self.anim_ctrl(ct_name)

        ct_name = prefix + '_hip_CTL'
        hip_zero, hip_ctrl, hip_offsets, hip_last_node = self.anim_ctrl(ct_name)

        ct_name = prefix + '_cog_CTL'
        cog_zero, cog_ctrl, cog_offsets, cog_last_node = self.anim_ctrl(ct_name)
        mc.parent(cog_zero, ctrl_grps[0])

        # now create MID torso, fk, and reverse spine ctrls
        div = 1.0 / (number_mid_ctrl + 1)
        if number_mid_ctrl == 1:
            div = 1.0
        fk_mids_zeros, fk_mids_ctrls, fk_mids_offsets, fk_mids_last_nodes = [], [], [], []
        rev_mids_zeros, rev_mids_ctrls, rev_mids_offsets, rev_mids_last_nodes = [], [], [], []
        mid_zeros, mid_ctrls, mid_offsets, mid_last_nodes = [], [], [], []

        for i in range(number_mid_ctrl):
            if number_mid_ctrl == 1:
                ct_name = '{0}_midSpine_CTL'.format(prefix)
                fk_name = '{0}_spine_FK_1_CTL'.format(prefix)
                rev_name = '{0}_revSpine_1_CTL'.format(prefix)
            else:
                ltr = utils.letters[i]
                numltr = str(i + 1)
                ct_name = '{0}_midSpine_{1}_CTL'.format(prefix, ltr)
                fk_name = '{0}_spine_FK_{1}_CTL'.format(prefix, numltr)
                rev_name = '{0}_revSpine_{1}_CTL'.format(prefix, numltr)

            mid_zero, mid_ctrl, mid_off, mid_last = self.anim_ctrl(ct_name)

            mid_zeros.append(mid_zero)
            mid_ctrls.append(mid_ctrl)
            mid_offsets.append(mid_off)
            mid_last_nodes.append(mid_last)

            fk_zero, fk_ctrl, fk_off, fk_last = self.anim_ctrl(fk_name)

            fk_mids_zeros.append(fk_zero)
            fk_mids_ctrls.append(fk_ctrl)
            fk_mids_offsets.append(fk_off)
            fk_mids_last_nodes.append(fk_last)

            rev_zero, rev_ctrl, rev_off, rev_last = self.anim_ctrl(rev_name)

            rev_mids_zeros.append(rev_zero)
            rev_mids_ctrls.append(rev_ctrl)
            rev_mids_offsets.append(rev_off)
            rev_mids_last_nodes.append(rev_last)

            # Next, create all orient contraints and aims for chest and hips

            aim_amount = div * (i + 1)
            aim_grp = mid_ctrl + '_CONST'

            aim_chest = mc.duplicate(aim_grp, po=1, n=mid_ctrl + '_aim_chest_GRP')[0]
            aim_hip = mc.duplicate(aim_grp, po=1, n=mid_ctrl + '_aim_hip_GRP')[0]
            mc.parent(aim_chest, chest_last_node)
            mc.parent(aim_hip, hip_last_node)

            prc = mc.parentConstraint(chest_last_node, aim_grp, weight=aim_amount, mo=1)
            prc = mc.parentConstraint(hip_last_node, aim_grp, weight=1.0 - aim_amount, mo=1)
            mc.setAttr(prc[0] + '.interpType', 2)

        # Now create the base and chest end fk and reverse ctrls

        names = ['0', 'chest']
        fk_ends_zeros, fk_ends_ctrls, fk_ends_offsets, fk_ends_last_nodes = [], [], [], []
        rev_ends_zeros, rev_ends_ctrls, rev_ends_offsets, rev_ends_last_nodes = [], [], [], []
        for i, jnt in enumerate(names):
            fk_name = '{0}_spine_FK_{1}_CTL'.format(prefix, names[i])
            rev_name = '{0}_revSpine_{1}_CTL'.format(prefix, names[i])
            # fk ctrls
            fk_zero, fk_ctrl, fk_offsets, fk_last_node = self.anim_ctrl(fk_name)
            fk_ends_zeros.append(fk_zero)
            fk_ends_ctrls.append(fk_ctrl)
            fk_ends_offsets.append(fk_offsets)
            fk_ends_last_nodes.append(fk_last_node)

            rev_zero, rev_ctrl, rev_offsets, rev_last_node = self.anim_ctrl(rev_name)
            rev_ends_zeros.append(rev_zero)
            rev_ends_ctrls.append(rev_ctrl)
            rev_ends_offsets.append(rev_offsets)
            rev_ends_last_nodes.append(rev_last_node)

        # Now consolidate into one array each for fk and reverse spine ctrls

        fk_zeros = [fk_ends_zeros[0]] + fk_mids_zeros + [fk_ends_zeros[-1]]
        fk_ctrls = [fk_ends_ctrls[0]] + fk_mids_ctrls + [fk_ends_ctrls[-1]]

        rev_mids_zeros.reverse()
        rev_mids_ctrls.reverse()
        rev_zeros = [rev_ends_zeros[-1]] + rev_mids_zeros + [rev_ends_zeros[0]]
        rev_ctrls = [rev_ends_ctrls[1]] + rev_mids_ctrls + [rev_ends_ctrls[0]]

        # parent hips, chest, fk, and reverse controls

        num_ctrls = len(fk_ctrls)

        mc.parent(fk_zeros[1], fk_ctrls[0])
        mc.parent(fk_zeros[0], cog_last_node)
        mc.parent(mid_zeros[0], fk_ctrls[1])
        mc.parent(fk_zeros[-1], chest_last_node)

        for i in range(0, num_ctrls):
            if i > 0:
                mc.parent(rev_zeros[i], rev_ctrls[i - 1])
            if i > 1:
                mc.parent(fk_zeros[i], fk_ctrls[i - 1])

        mc.parent(rev_zeros[0], cog_last_node)
        mc.parent(chest_zero, fk_ctrls[-2])
        mc.parent(hip_zero, rev_ctrls[-1])

        # Now create spine shaper ctrls
        shpr_grp = mc.createNode('transform', p=ctrl_grps[0], n='{0}_spineShapers_grp'.format(prefix))
        shpr_zeros, shpr_ctrls, shpr_offsets, shpr_last_nodes = [], [], [], []
        for i, jnt in enumerate(spine_jnts + [chest_jnt]):
            num = str(i + 1)
            shpr_name = '{0}_spineShaper_{1}_CTL'.format(prefix, num)
            zero, ctrl, offsets, last_node = self.anim_ctrl(shpr_name)
            mc.parent(zero, shpr_grp)
            shpr_zeros.append(zero)
            shpr_ctrls.append(ctrl)
            shpr_offsets.append(offsets)
            shpr_last_nodes.append(last_node)

        # other ctrls
        mc.parent(mid_zeros, cog_last_node)

        # flatten joints
        mc.parent(spine_jnts, chest_jnt, hip_jnt, jnt_grps[0])
        nodes_to_connect = spine_jnts + [chest_jnt]
        ik_jnts = []
        for i, node in enumerate(nodes_to_connect):
            dup = mc.duplicate(node, n=node.replace('JNT', 'ik_jnt'))
            ik_jnts.append(dup[0])
            if i > 0:
                mc.parent(dup[0], ik_jnts[-1])
            if node == chest_jnt:
                chest_end = utils.get_children(dup[0])
                if chest_end:
                    mc.delete(chest_end)

        # now create spline driver nodes and drive with curve we just created and upv placer
        spline_driver_nodes = []
        for i, sj in enumerate(spline_jnts):
            g = mc.createNode('joint', n=prefix + '_spineSplineDrv' + utils.letters[i] + '_GRP')
            mc.delete(mc.pointConstraint(sj, g))
            spline_driver_nodes.append(g)

        # now parent the spline driver nodes
        mc.parent(spline_driver_nodes[0], hip_last_node)
        mc.parent(spline_driver_nodes[-1], chest_last_node)
        if number_mid_ctrl == 1:
            mc.parent(spline_driver_nodes[1], mid_ctrls[0])
        else:
            for i in range(len(mid_ctrls)):
                mc.parent(spline_driver_nodes[i + 1], mid_ctrls[i])

        # create spline ik handle and stretch
        name = prefix + '_spineSpline'
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
        # mc.parent (ik_build, bs_curve[0], noxform_grp)

        # skin cluster spline driver joints to bs curve
        sc = mc.skinCluster(bs_curve, spline_driver_nodes, tsb=1)
        mc.parent(ik_build[0], noxform_grp)
        mc.parent(bs_curve[0], noxform_grp)
        # mc.parent (ik_jnts[0], jnt_grps[0])
        mc.parent(ik_build[2], noxform_grp)
        # Create spline and surf
        jnts = spine_jnts + [chest_jnt]

        stretch = 1
        width = utils.get_distance(jnts[0], jnts[1]) * 0.4

        # crv=ik_build[2]
        # crv = spline.create_curve_mtx(ik_jnts, degree=2, name=prefix+'_spine', parent=noxform_grp)
        # surf = spline.create_surface_mtx(ik_jnts, name=prefix+'_spine', parent=noxform_grp, width=width, stretch=stretch)

        # mc.addAttr(chest_ctrl, ln='stretch', k=1, min=0, max=1, dv=1)
        # mc.addAttr(chest_ctrl, ln='reverseRoot', k=1, min=0, max=1)

        # connect to spline
        fkcurl_drvs = []
        mc.makeIdentity(jnts, apply=1, t=1, r=1, s=1, n=0, pn=1)

        for i, jnt in enumerate(jnts):
            constraint.freeze_joint_orient(jnt)
            mc.setAttr(jnt + '.segmentScaleCompensate', 0)
            drv = mc.createNode('transform', p=shpr_zeros[i], n=shpr_zeros[i] + '_ATT')
            mc.parent(drv, w=1)
            mc.parent(drv, shpr_grp)
            fkcurl_drvs.append(drv)
            constraint.constraint_mtx(shpr_zeros[i], jnt, s=0)

        # mc.delete(crv)
        for i, zero in enumerate(shpr_zeros[:-1]):
            att = zero + '_ATT'
            constraint.constraint_mtx(ik_jnts[i], att)

        # mc.setAttr(surf + '.uniformStretch', 1)
        # for a in ['stretch', 'reverseRoot']:
        #     mc.connectAttr(chest_ctrl + '.' + a, surf + '.' + a)
        # mc.setAttr(chest_ctrl + '.stretch', 1)

        for i, jnt in enumerate(shpr_zeros):
            mc.connectAttr(shpr_zeros[i] + '_ATT.t', shpr_zeros[i] + '.t')
            mc.connectAttr(shpr_zeros[i] + '_ATT.r', shpr_zeros[i] + '.r')

        # constrain chest jnt and hip jnt
        mc.parent(hip_jnt, spine_jnts[0])
        constraint.constraint_mtx(spline_driver_nodes[-1], shpr_zeros[-1])

        pos = mc.createNode('transform', n=hip_jnt + '_POS', p=hip_last_node)
        # mc.parent (pos, hip_last_node)

        mc.pointConstraint(spine_jnts[0], pos)
        mc.parentConstraint(pos, hip_jnt, mo=1)

        # setup ramp scale and volume preservation
        # spline.ramp_scale([hip_ctrl]+mid_ctrls+[chest_ctrl], [hip_jnt]+jnts, interpolation=4, driver_attr='spineScale')
        # spline.preserve_volume(fk_ctrls, jnts, chest_ctrl)

        # movable pivots
        # control.create_movable_pivot(cog_ctrl)
        # control.create_movable_pivot(chest_ctrl)
        # control.create_movable_pivot(hip_ctrl)

        # lock and parent stuff
        # mc.parent(fk_zeros[0], cog_last_node)
        # mc.parent(cog_zero, ctrl_grps[0])

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

        jnts = [hip_jnt] + spine_jnts + [chest_jnt, chest_end_jnt]

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
