# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import spline
from rigBot import control
from rigBot import rivet
from rigBot import spaces
from rigBot import pickWalk
from rigBot import env
from rigBot import constraint
from rigBot.partsLibrary import standardPart

class Neck(standardPart.StandardPart):
    """Neck rig build part for standard biped and long neck creatures.
        Uses cmSplineChain plugin node. You also have the option to build as
        a vanilla maya rig without plugin nodes.

        Note:
            The option to build as vanilla maya rig is set per asset in the ${ASSET}_buildList.py
            Guide rig parts will always build with cmRigNodes plugin nodes.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "C".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_chest_end_JNT".
            :numberJoints: (int) Numder of neck joints. Defaults to 4.
            :numberMidCtrls: (int) Number of mid neck IK ctrls. Defaults to 1.
            :createFkCtrls: (bool) Create FK offset ctrls that can peel off the spline. Defaults to True.
            :createJaw: (bool) Create jaw joint and control. Defaults to True.
            :createReverseJaw: (bool) Create reverse jaw ctrl for the upper head. Defaults to True."""


    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('side', default='C')
        self.add_option('parent', data_type='hook', default='C_chest_end_JNT')

        self.add_option('numberJoints',
                        data_type='int',
                        rebuild_to_modify=True,
                        default = 4,
                        tool_tip='Numder of neck joints.',
                        min=2)

        self.add_option('numberMidCtrls',
                         data_type='int',
                         rebuild_to_modify=True,
                         default = 1,
                         min=1,
                         tool_tip='Number of mid neck IK ctrls.')

        self.add_option('createJaw',
                        data_type='bool',
                        rebuild_to_modify=True,
                        default = True,
                        tool_tip='Create jaw joint and control.')

        self.add_option('createReverseJaw',
                        data_type='bool',
                        rebuild_to_modify=True,
                        default = True,
                        tool_tip='Create reverse jaw ctrl for the upper head.')

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

        number_mid_ctrl = options.get('numberMidCtrls')
        num_joints = options.get('numberJoints')
        create_jaw = options.get('createJaw')
        create_skull = options.get('createReverseJaw')

        noxform_grp = self.guide_master+'_NOX'
        length = 2
        create_fk_ctrls = True

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

        try:
            mc.delete(plcs[0]+'Shape', plcs[-1]+'Shape')
        except:
            pass

        self.tag_as_ref(spline_plcs)

        # Constraint center spline nodes
        div = 1.0 / (num_spl_jnts-1)
        for i in range(1, len(spline_zeros[:-1])):
            zero = spline_zeros[i]
            mc.pointConstraint(spline_plcs[-1], zero, w=div*i)
            mc.pointConstraint(spline_plcs[0], zero, w=1.0-div*i)

        # rotate to face up
        jnt_grp = utils.get_parent(jnt_zeros[0])
        grp = mc.group(jnt_zeros+spline_zeros)
        mc.xform(grp, piv=[0,0,0])
        mc.xform(grp, r=1, ro=[0,0,90])

        mc.parent(jnt_zeros+spline_zeros, jnt_grp)
        mc.delete(grp)

        # Create spline and bind
        spline_crv = spline.create_curve_mtx(spline_plcs,
            name=prefix+'_neckSplinePlc',
            axis='Y',
            degree=2,
            parent=noxform_grp)

        spline_surf = spline.create_surface_mtx(spline_plcs,
            name=prefix+'_neckSplinePlc',
            axis='Y',
            degree=2,
            parent=noxform_grp)

        # param_nodes = spline.connect_param_node(spline_crv, spline_surf, jnt_zeros)
        #
        # for p in param_nodes:
        #     mc.setAttr(p+'.stretch', 1)
        #     mc.setAttr(p+'.uniformStretch', 1)
        spline.create_stretch_crv (spline_crv)
        rivet.surface_mtx(spline_surf, jnt_zeros, noxform_grp)
        # create head
        head_zero, head_plc, head_jnt = self.guide_joint('head_end', constraint_type='point')
        pos = mc.xform(plcs[-1], q=1, ws=1, t=1)
        mc.xform(head_zero, ws=1, t=pos)
        mc.xform(head_zero, r=1, t=[0,3,0])
        mc.parent(head_jnt, jnts[-1])
        mc.parent(head_zero, spline_plcs[-1])

        mc.setAttr(head_jnt+'.jo', 0,0,0)

        mc.aimConstraint(head_plc, jnts[-1],
            aim=[1,0,0], u=[0,1,0], wu=[0,1,0],
            wut='objectRotation', wuo=spline_plcs[-1])

        # Create ctrlas
        head_ct_zero, head_ctrl = self.guide_ctrl('head', shape='circle', axis='Z', color='yellow', scale=[3,3,3])
        mc.delete(mc.pointConstraint(jnts[-1], head_ct_zero))
        mc.parentConstraint(jnts[-1], head_ct_zero, mo=1)

        aim_grp = mc.createNode('transform', p=spline_plcs[0], n=spline_plcs[0]+'_aim_GRP')
        mc.aimConstraint(spline_plcs[-1], aim_grp, aim=[0,1,0], u=[1,0,0], wu=[0,-1,0], wut='objectRotation', wuo=spline_plcs[0])

        # Create hip
        neck_base_ct_zero, neck_base_ctrl = self.guide_ctrl('neckBase', shape='hip', color='lavendar', scale=[3.6,3,3])
        mc.delete(mc.pointConstraint(jnts[0], neck_base_ct_zero))
        mc.pointConstraint(jnts[0], neck_base_ct_zero, mo=1)
        mc.orientConstraint(aim_grp, neck_base_ct_zero, mo=1)

        ctrl = utils.get_parent(head_ctrl)
        utils.set_attrs(ctrl, 't s ', l=1, k=0)

        #ctrl = utils.get_parent(head_rotate_ctrl)
        #utils.set_attrs(ctrl, 't s ', l=1, k=0)

        ctrl = utils.get_parent(neck_base_ctrl)
        utils.set_attrs(ctrl, 't s ', l=1, k=0)

        # Create neck mid ctrls
        mid_ctrl_range = range(1, len(spline_zeros[:-1]))
        if number_mid_ctrl == 1:
            mid_ctrl_range = range(1)

        for i in mid_ctrl_range:
            spl_drv = spline_plcs[i]
            ltr = utils.letters[i-1]
            ct_name = 'midNeck_'+ltr

            if number_mid_ctrl == 1:
                ct_name = 'midNeck'
                spl_drv = spline_plcs[1:3]

            mid_ct_zero, mid_ctrl = self.guide_ctrl(ct_name, shape='circle', color='pink', scale=[3.6,3,3])
            mc.pointConstraint(spl_drv, mid_ct_zero)
            mc.orientConstraint(aim_grp, mid_ct_zero)

            utils.set_attrs(utils.get_parent(mid_ctrl), 't', l=1, k=0)

            piv_ctrl = utils.get_parent(mid_ctrl)
            utils.set_attrs(piv_ctrl, 't s', l=1, k=0)

        fk_zeros = []
        fk_ctrls = []
        jnt_suffix = 'JNT'
        zero_suffix = 'CTL_ZERO'
        if create_fk_ctrls:
            for i, jnt in enumerate(jnts[:-1]):
                fk_name = 'neck_FK_'+utils.letters[i]
                fk_zero, fk_ctrl = self.guide_ctrl(fk_name, driver=jnt, create_pivot=0, allow_offset_ctrls=0, shape='pin_circle', color='light_blue', scale=[2]*3)
                mc.xform(fk_ctrl+'.cv[*]', r=1, ro=[-90,0,0])
                fk_zeros.append(fk_zero)
                fk_ctrls.append(fk_ctrl)

        # Create jaw
        if create_jaw:

            jaw_zero, jaw_plc, jaw_jnt = self.guide_joint('jaw', constraint_type='point')
            pos = mc.xform(plcs[-1], q=1, ws=1, t=1)
            mc.xform(jaw_zero, ws=1, t=pos)
            mc.xform(jaw_zero, r=1, t=[0,0,0.5])
            mc.parent(jaw_jnt, jnts[-1])
            mc.parent(jaw_zero, spline_plcs[-1])

            jaw_end_zero, jaw_end_plc, jaw_end_jnt = self.guide_joint('jaw_end', constraint_type='point')
            pos = mc.xform(jaw_jnt, q=1, ws=1, t=1)
            mc.xform(jaw_end_zero, ws=1, t=pos)
            mc.xform(jaw_end_zero, r=1, t=[0,0,2])
            mc.parent(jaw_end_jnt, jaw_jnt)
            mc.parent(jaw_end_zero, jaw_plc)

            mc.aimConstraint(jaw_end_plc, jaw_jnt, aim=[1,0,0], u=[0,0,-1], wu=[1,0,0], wut='objectRotation', wuo=jaw_plc)
            mc.setAttr(jaw_end_jnt+'.jo', 0,0,0)

            utils.set_attrs([jaw_end_plc], 'r ', l=1, k=0)

            # Create jaw ctrl
            jaw_ct_zero, jaw_ctrl = self.guide_ctrl('jaw', shape='semi_circle', allow_offset_ctrls=False, color='cyan', scale=[2,2,2])
            mc.parentConstraint(jaw_jnt, jaw_ct_zero)

            mc.xform(jaw_ctrl+'.cv[*]', r=1, ro=[0,-90,0])
            mc.xform(jaw_ctrl+'.cv[*]', r=1, s=[2.5,1,1])

            jaw_piv = utils.get_parent(jaw_ctrl)
            utils.set_attrs(jaw_piv, 't s', l=1, k=0)

            # Create skull ctrl
            if create_skull:
                rev_jaw_zero, rev_jaw_plc, rev_jaw_jnt = self.guide_joint('reverseJaw', constraint_type='parent')
                mc.parentConstraint(jaw_jnt, rev_jaw_zero)
                try:
                    mc.setAttr(rev_jaw_plc+'Shape.offsetTranslateY', 0.25)
                except:
                    pass

                mc.parent(rev_jaw_jnt, jnts[-1])

                skull_ct_zero, skull_ctrl = self.guide_ctrl('reverseJaw', driver=rev_jaw_jnt, axis='Y', shape='pin_circle', allow_offset_ctrls=False, color='cyan', scale=[4,4,4])
                mc.xform(skull_ctrl, r=1, ro=[0,90,0])
                mc.makeIdentity(skull_ctrl,apply=1, t=1, r=1, s=1, n=0, pn=1)

                piv_ctrl = utils.get_parent(skull_ctrl)
                utils.set_attrs(piv_ctrl, 't s', l=1, k=0)
                utils.set_attrs(rev_jaw_plc, l=1, k=0)

        # lock stuff
        utils.set_attrs(plcs[:-1], 't r', l=1, k=0)

        utils.set_attrs(spline_plcs[:-1], 'r', l=1, k=0)
        utils.set_attrs(head_plc, 'r', l=1, k=0)

        utils.set_attrs(plcs, l=1, k=0)

        head_name = prefix+'_head_JNT'
        mc.rename(jnt_zeros[-1], head_name+'_'+zero_suffix)
        mc.rename(jnts[-1], head_name)
        mc.rename(plcs[0], plcs[0]+'_DUMMY')
        mc.rename(plcs[-1], plcs[-1]+'_DUMMY')

        mc.rename(spline_plcs[0], plcs[0])
        mc.rename(spline_plcs[-1], head_name+'_PLC')

        if create_fk_ctrls:
            fk_name = 'head_FK'
            fk_zero, fk_ctrl = self.guide_ctrl(fk_name, driver=head_name, allow_offset_ctrls=0, create_pivot=0, shape='pin_circle', color='light_blue', scale=[2]*3)
            mc.xform(fk_ctrl+'.cv[*]', r=1, ro=[-90,0,0])
            fk_zeros.append(fk_zero)
            fk_ctrls.append(fk_ctrl)

        # This finalizes your guide.
        mc.setAttr(head_ctrl+'.numOffsetCtrls', 1)
        mc.setAttr(neck_base_ctrl+'.numOffsetCtrls', 1)

        mc.xform(spline_zeros, r=1, t=[0, -self.mirror_value,0])
        mc.setAttr(self.guide_master+'.offsetTranslateZ', -0.5*self.mirror_value)

        self.finalize_guide()

    def build_rig(self):
        """This builds your anim rig."""

        # create rig part top nodes
        self.create_part_master()

        # Get all the relevant part info
        prefix            = self.prefix
        options           = self.options
        anim_ctrls        = self.anim_ctrls
        bind_jnts       = self.bind_joints
        hooks             = self.hooks
        ctrl_grps         = self.ctrl_grps
        jnt_grps          = self.jnt_grps
        noxform_grp       = self.noxform_grp
        world_scale_attr = self.hooks[0]+'.worldScale'

        num_joints = options.get('numberJoints')
        number_mid_ctrl = options.get('numberMidCtrls')
        create_jaw = options.get('createJaw')
        create_skull = options.get('createReverseJaw')
        pickWalk_parent = options.get('pickWalkParent')

        ctrl_suffix = 'CTL'
        jnt_suffix = 'JNT'
        zero_suffix = 'CTL_ZERO'

        create_fk_ctrls = True

        # finda all jnts
        jaw_jnt = prefix+'_jaw_'+jnt_suffix
        head_jnt = prefix+'_head_'+jnt_suffix
        head_end_jnt = prefix+'_head_end_'+jnt_suffix
        rev_jaw_jnt = prefix+'_reverseJaw_'+jnt_suffix

        neck_jnts = []
        for i in range(num_joints-1):
            letter = utils.letters[i]
            neck_jnts.append('{0}_neck_{1}_{2}'.format(prefix, letter, jnt_suffix))

        crv_jnts = neck_jnts+[head_jnt, head_end_jnt]

        spline_jnts = [neck_jnts[0]+'_PLC_REF']
        for i in range(1, 3):
            letter = utils.letters[i]
            spline_jnts.append('{0}_neckSpline_{1}_{2}_PLC_REF'.format(prefix, letter, jnt_suffix))

        spline_jnts.append(head_jnt+'_PLC_REF')

        # create ctrls
        ct_name = prefix+'_head_CTL'
        head_zero, head_ctrl, head_offsets, head_last_node = self.anim_ctrl(ct_name)

        ct_name = prefix+'_neckBase_CTL'
        neck_base_zero, neck_base_ctrl, neck_base_offsets, neck_base_last_node = self.anim_ctrl(ct_name)

        fk_zeros, fk_ctrls, fk_offsets, fk_last_nodes= [], [], [], []
        for i, jnt in enumerate(neck_jnts+[head_jnt]):
            ltr = utils.letters[i]
            fk_name = '{0}_neck_FK_{1}_{2}'.format(prefix, ltr, ctrl_suffix)

            if jnt == head_jnt:
                fk_name = '{0}_head_FK_{2}'.format(prefix, ltr, ctrl_suffix)
            zero, ctrl, offsets, last_node = self.anim_ctrl(fk_name)

            if fk_ctrls:
                mc.parent(zero, fk_ctrls[-1])

            fk_zeros.append(zero)
            fk_ctrls.append(ctrl)
            fk_offsets.append(offsets)
            fk_last_nodes.append(last_node)

        # create MID neck ctrls
        mid_zeros, mid_ctrls, mid_offsets, mid_last_nodes = [], [], [], []
        div = 1.0 / (number_mid_ctrl+1)

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
            aim_amount = div*(i+1)
            aim_grp = mid_ctrl+'_CONST'
            aim_head = mc.duplicate(mid_ctrl+'_CONST', n=mid_ctrl+'_aim_head_GRP', po=1)[0]
            aim_hip = mc.duplicate(mid_ctrl+'_CONST', n=mid_ctrl+'_aim_hip_GRP', po=1)[0]

            mc.parent(mid_ctrl+'_MOCAP', mid_zero)
            mc.aimConstraint(head_last_node, aim_head, aim=[0,1,0], u=[1,0,0], wu=[1,0,0], wut='objectRotation', wuo=head_ctrl, mo=1)
            mc.aimConstraint(neck_base_zero, aim_hip, aim=[0,-1,0], u=[1,0,0], wu=[1,0,0], wut='objectRotation', wuo=neck_base_zero, mo=1)

            mc.parent(mid_ctrl+'_MOCAP', aim_grp)
            mc.parent(aim_grp, aim_head, aim_hip, w=1)

            mc.pointConstraint(head_last_node, mid_zero, weight=aim_amount)
            mc.pointConstraint(neck_base_zero, mid_zero, weight=1.0-aim_amount)
            mc.parent(aim_grp, aim_head, aim_hip, mid_zero)

            oc = mc.orientConstraint(aim_head, aim_grp, weight=aim_amount)
            oc = mc.orientConstraint(aim_hip, aim_grp, weight=1.0-aim_amount)

            mc.setAttr(oc[0]+'.interpType', 2)

        # Create jaw
        if create_jaw:
            ct_name = prefix+'_jaw_'+ctrl_suffix
            jaw_zero, jaw_ctrl, jaw_offsets, jaw_last_node = self.anim_ctrl(ct_name)
            mc.parent(jaw_zero, head_last_node)

            if create_skull:
                ct_name = prefix+'_reverseJaw_'+ctrl_suffix
                skull_zero, skull_ctrl, skull_offsets, skull_last_node = self.anim_ctrl(ct_name)
                mc.parent(skull_zero, head_last_node)

        # parent ctrls
        mc.parent(mid_zeros, neck_base_zero, ctrl_grps[0])
        mc.parent(head_zero, neck_base_last_node)

        # now create spline
        spline_driver_nodes = []
        for i, sj in enumerate(spline_jnts):
            g = mc.createNode('transform', n=prefix+'_neckSplineDrv'+utils.letters[i]+'_GRP')
            mc.delete(mc.pointConstraint(sj, g))
            spline_driver_nodes.append(g)

        mc.parent(spline_driver_nodes[0], neck_base_zero)
        mc.parent(spline_driver_nodes[-1], head_last_node)

        # now create spline
        if number_mid_ctrl == 1:
            mc.parent(spline_driver_nodes[1:3], mid_ctrls[0])

        else:
            for i in range(len(mid_ctrls)):
                mc.parent(spline_driver_nodes[i+1], mid_ctrls[i])

        # flatten neck joints
        mc.parent(neck_jnts, head_jnt, jnt_grps[0])
        jnts = neck_jnts+[head_jnt]

        use_plugin = env.use_plugin()
        inverse_plugin = not use_plugin
        width = utils.get_distance(jnts[0], jnts[1]) * 0.4

        crv = spline.create_curve_mtx(spline_driver_nodes, degree=2, name=prefix+'_neck', parent=noxform_grp)
        surf = spline.create_surface_mtx(spline_driver_nodes, name=prefix+'_neck', parent=noxform_grp, width=width, stretch=inverse_plugin)

        mc.addAttr(head_ctrl, ln='stretch', k=1, min=0, max=1)
        mc.addAttr(head_ctrl, ln='uniformStretch', k=1, min=0, max=1)

        # connect to spline
        fkcurl_drvs = []

        for i, jnt in enumerate(jnts):
            constraint.freeze_joint_orient(jnt)
            mc.setAttr(jnt+'.segmentScaleCompensate', 0)

            drv = mc.createNode('transform', p=fk_zeros[i], n=fk_zeros[i]+'_ATT')
            mc.parent(drv, w=1)

            fkcurl_drvs.append(drv)

            # need an offset node to eat some precision errors
            if use_plugin:
                params = spline.connect_param_node(crv, surf, drv, world_scale_attr=hooks[0]+'.worldScale')
                for p in params:
                    for a in ['stretch','uniformStretch']:
                        mc.connectAttr(head_ctrl+'.'+a, p+'.'+a)

            constraint.constraint_mtx(fk_ctrls[i], jnt, s=0)

        if not use_plugin:
            mc.delete(crv)
            for zero in fk_zeros:
                att = zero +'_ATT'
                rivet.surface_mtx2(surf, att, percentage=inverse_plugin)

            for a in ['stretch','uniformStretch']:
                mc.connectAttr(head_ctrl+'.'+a, surf+'.'+a)

        for i, drv in enumerate(fkcurl_drvs):
            if i > 0:
                mc.parent(drv, fkcurl_drvs[i-1])
        mc.parent(fkcurl_drvs[0], ctrl_grps[0])

        for i, jnt in enumerate(jnts):
            mc.connectAttr(fk_zeros[i]+'_ATT.t', fk_zeros[i]+'.t')
            mc.connectAttr(fk_zeros[i]+'_ATT.r', fk_zeros[i]+'.r')

        try:
            mc.parent(fk_zeros[0], ctrl_grps[0])
        except:
            pass

        # scales and preserve volume
        if len(neck_jnts) > 1:
            spline.ramp_scale([neck_base_ctrl]+mid_ctrls+[head_ctrl], jnts[:-1], interpolation=4, driver_attr='neckScale')

        spline.preserve_volume(fk_ctrls, jnts[:-1], head_ctrl)

        constraint.constraint_mtx(head_last_node, fk_zeros[-1], t=0, o=1, s=1)

        # connect head jaw and reverse jaw jnts
        if create_jaw:
            constraint.freeze_joint_orient(jaw_jnt)
            constraint.constraint_mtx(jaw_last_node, jaw_jnt)
            constraint.constraint_mtx(head_jnt, jaw_zero)

            if create_skull:
                constraint.freeze_joint_orient(rev_jaw_jnt)
                constraint.constraint_mtx( skull_last_node, rev_jaw_jnt)
                constraint.constraint_mtx(head_jnt, skull_zero)

        # connect gsc
        control.create_movable_pivot(neck_base_ctrl)
        control.create_movable_pivot(head_ctrl)

        mm.eval('transformLimits -sz 0.001 1 -esz 1 0 %s ;' % head_ctrl)
        mm.eval('transformLimits -sy 0.001 1 -esy 1 0 %s ;' % head_ctrl)
        mm.eval('transformLimits -sx 0.001 1 -esx 1 0 %s ;' % head_ctrl)

        # lock stuff
        all_mid_offsets = []
        for moff in mid_offsets:
            all_mid_offsets.extend(moff)

        utils.set_attrs(fk_ctrls, 's v', l=1, k=0)
        utils.set_attrs(head_offsets+neck_base_offsets+all_mid_offsets, ' s v', l=1, k=0)

        spaces.tag(head_ctrl, arg='neckBase:'+neck_base_last_node, default=1)

        # fx_crvs
        #utils.create_cfx_curves(crv_jnts, self.prefix+'_'+self.part_type)

        #Setup pickwalking
        if create_jaw:
            pickWalk.attribute_tag(jaw_ctrl, head_ctrl)

            if create_skull:
                pickWalk.attribute_tag(skull_ctrl, head_ctrl)

        pickWalk.attribute_tag(head_ctrl, neck_base_ctrl)
        pickWalk.attribute_tag(neck_base_ctrl, pickWalk_parent)

        if create_fk_ctrls:
            self.create_ctrl_set('FK', fk_ctrls)

            #Setup pickwaliking attributes for the fingers
            i = 0

            fk_ctrls.reverse()
            pickWalk.attribute_tag(head_ctrl, fk_ctrls[0])
            for ctrl in fk_ctrls:

                if i+1 < len(fk_ctrls):

                    pickWalk.attribute_tag(fk_ctrls[i],fk_ctrls[i+1])
                else:
                    pickWalk.attribute_tag(fk_ctrls[i],neck_base_ctrl)
                    break

                i+=1
            fk_ctrls.reverse()

        self.finalize_part()
