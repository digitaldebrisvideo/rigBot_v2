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
from rigBot import constraint
from rigBot import env
from rigBot.partsLibrary import standardPart

class Tongue(standardPart.StandardPart):
    """Tongue rig build part for standard biped tongues and long tongue creatures.
        Uses cmSplineChain plugin node. You also have the option to build as a
        vanilla maya rig without plugin nodes.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "C".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_jaw_JNT".
            :numberJoints: (int) Numder of tongue joints. Defaults to 8.
            :numberCtrls: (int) Number ctrls. Defaults to 5.
            :createFkCtrls: (bool) Create FK offset ctrls that can peel off the spline. Defaults to True.
            :squashStretch: (bool) Squash stretch. Defaults to True.
            :AddCurlAttr: (bool) Add an empty curl attribute to drive deformers. Defaults to True."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('side', default='C')
        self.add_option('parent', data_type='hook', default='C_jaw_JNT')

        self.add_option('numberJoints',
                        data_type='int',
                        rebuild_to_modify=True,
                        default = 8,
                        tool_tip='Numder of tongue joints.',
                        min=0)

        self.add_option('numberCtrls',
                        data_type='int',
                        default=5,
                        min=4,
                        max=None,
                        rebuild_to_modify=True)

        self.add_option('createFkCtrls',
                        data_type='bool',
                        rebuild_to_modify=True,
                        default = True,
                        tool_tip='Create FK offset ctrls that can peel off the spline.')

        self.add_option('addCurl',
                tool_tip='Add curling functionality',
                data_type='bool',
                default=True,
                rebuild_to_modify=False,
            hidden=True)

        self.add_option('addVolumeControls',
            tool_tip='Add scale and volume preservation control',
            data_type='bool',
            default=True,
            rebuild_to_modify=False,
            hidden=True)

        self.add_option('shiftCtrls', data_type='float', hidden=True, min=-1, max=1, default=0)
        self.add_option('shiftJoints', data_type='float', hidden=True, min=-1, max=1, default=0)

        self.add_option('pickWalkParent',
                        data_type='string',
                        default="C_jaw_CTL",
                        selectable=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix       = self.prefix
        options      = self.options
        mirror_value = self.mirror_value
        noxform_grp = self.guide_master+'_NOX'

        # START CODING SUCKKA !!
        num_joints = options.get('numberJoints')
        num_pri_ctrls = options.get('numberCtrls')
        add_fk_ctrls = options.get('createFkCtrls')

        length = 10
        num_plcs = num_pri_ctrls

        ##############################################
        #  Create plcs joints and ctrls

        # Create joint chain
        jnt_zeros, plcs, jnts = self.guide_joint_chain('', num_joints=num_joints, length=length)

        #Create spline placers
        spline_zeros, spline_plcs = self.guide_joint_chain('spline', num_joints=num_plcs,
                                                    flat_plc_hierarchy=True,
                                                    placer_only=True,
                                                    constraint_type='parent',
                                                    length=length)

        # Create primary ctrls
        pri_zeros, ctrls = self.guide_ctrl_chain('tongue_IK', axis='X', flat_hierarchy=True,
                                length=length, shape='circle', color='pink', scale=[1,1,1],
                                create_pivot=False,  num_ctrls=num_pri_ctrls)


        # Create fk tip ctrls
        fk_zeros, fk_ctrls = [], []
        if add_fk_ctrls:
            fk_zeros, fk_ctrls = self.guide_ctrl_chain('tongue_FK',num_ctrls=num_joints, allow_offset_ctrls=False,
                                    drivers=jnts, axis='X', length=length, flat_hierarchy=True,
                                    shape='pin_circle', color='light_blue', scale=[1,1,1], create_pivot=False)

            for c in fk_ctrls:
                mc.xform(c+'.cv[*]', r=1, ro=[0,0,90])

        ##############################################
        #  Create ribbons and connect ctrls and joints

        width = utils.get_distance(ctrls[0], ctrls[1]) * 0.1

        # create spline ribbon and connect primary ctrls
        spline_crv = spline.create_curve_mtx(spline_plcs,
            name=prefix+'_tongeSplinePlc',
            axis='Z',
            degree=2,
            parent=noxform_grp)

        spline_surf = spline.create_surface_mtx(spline_plcs,
            name=prefix+'_tongeSplinePlc',
            axis='Z',
            degree=2,
            width = width,
            parent=noxform_grp)

        # p_param_nodes = spline.connect_param_node(spline_crv, spline_surf, pri_zeros)

        spline.create_stretch_crv (spline_crv)
        rivet.surface_mtx(spline_surf, jnt_zeros, noxform_grp)

        # Create primary ribbon and connect secndary ctrls
        pri_crv = spline.create_curve_mtx(pri_zeros,
            name=self.prefix+'_tongue',
            axis='Z',
            degree=2,
            parent=noxform_grp)

        pri_surf = spline.create_surface_mtx(pri_zeros,
            name=self.prefix+'_tongue',
            axis='Z',
            degree=2,
            width=width,
            parent=noxform_grp)


        spline.create_stretch_crv(pri_crv)
        rivet.surface_mtx(pri_surf, jnt_zeros, noxform_grp)


        # s_param_nodes = []
        # j_param_nodes = spline.connect_param_node(pri_crv, pri_surf, jnt_zeros)
        #
        # for pn in p_param_nodes+s_param_nodes+j_param_nodes:
        #     mc.setAttr(pn+'.stretch', 1)
        #     mc.setAttr(pn+'.uniformStretch', 1)

        # shift joints
        # driver = self.guide_master+'.shiftJoints'
        # spline.connect_shift(driver, j_param_nodes, length, param_attr='paramLength')

        # shift primaries
        # driver = self.guide_master+'.shiftCtrls'
        # spline.connect_shift(driver, p_param_nodes, length, param_attr='paramLength')

        utils.set_attrs(plcs, l=1, k=0)
        mc.xform(spline_zeros, r=1, t=[-self.mirror_value,0,0])
        mc.setAttr(self.guide_master+'.offsetTranslateX', -0.5*self.mirror_value)
        mc.setAttr(self.guide_master+'.ry', -90)

        # This finalizes your guide.
        self.finalize_guide()


    def build_rig(self):
        """This builds your anim rig."""

        self.create_part_master()

        # Get all the relevant part info
        prefix            = self.prefix
        options           = self.options
        ctrls             = self.anim_ctrls
        jnts              = self.bind_joints
        hooks             = self.hooks
        ctrl_grps         = self.ctrl_grps
        jnt_grps          = self.jnt_grps
        noxform_grp      = self.noxform_grp
        world_scale_attr  = self.hooks[0]+'.worldScale'

        use_plugin = False

        # get options to build
        side = options.get('side')
        name = options.get('name')
        parent = options.get('parent')
        add_volume = options.get('addVolumeControls')
        add_curl = options.get('addCurl')
        pickWalk_parent = options.get('pickWalkParent')

        mc.parent(jnts, jnt_grps[0])

        # decalre stuff
        pri_zeros, pri_ctrls, pri_offsets, pri_last_nodes = [],[],[],[]
        fk_zeros, fk_ctrls, fk_offsets, fk_last_nodes = [],[],[],[]

        for node in ctrls:
            if 'FK' in node:
                zero, ctrl, off_ctrls, last_node = self.anim_ctrl(node)

                if fk_ctrls:
                    mc.parent(zero, fk_ctrls[-1])
                else:
                    mc.parent(zero, ctrl_grps[0])

                fk_zeros.append(zero)
                fk_ctrls.append(ctrl)
                fk_offsets.extend(off_ctrls)
                fk_last_nodes.append(last_node)

            else:
                zero, ctrl, off_ctrls, last_node = self.anim_ctrl(node)

                if pri_ctrls:
                    mc.parent(zero, pri_ctrls[-1])
                else:
                    mc.parent(zero, ctrl_grps[0])

                pri_zeros.append(zero)
                pri_ctrls.append(ctrl)
                pri_offsets.extend(off_ctrls)
                pri_last_nodes.append(last_node)

        settings_ctrl = pri_ctrls[-1]
        mc.addAttr(settings_ctrl, ln='stretch', k=1, min=0, max=1)
        mc.addAttr(settings_ctrl, ln='uniformStretch', k=1, min=0, max=1)

        # create spline ribbon and connect primary ctrls
        inverse_plugin = not use_plugin
        width = utils.get_distance(pri_last_nodes[0], pri_last_nodes[1]) * 0.1

        pri_crv = spline.create_curve_mtx(pri_last_nodes,
            name=self.prefix+'_tongue',
            axis='Z',
            degree=2,
            parent=noxform_grp)

        pri_surf = spline.create_surface_mtx(pri_last_nodes,
            name=self.prefix+'_tongue',
            axis='Z',
            degree=2,
            width=width,
            stretch=inverse_plugin,
            parent=noxform_grp)

        if not use_plugin:
            mc.connectAttr(settings_ctrl+'.stretch', pri_surf+'.stretch')
            mc.connectAttr(settings_ctrl+'.uniformStretch', pri_surf+'.uniformStretch')

        mm.eval('move -r -os -wd 0.001 0 0 '+jnts[0])
        fkcurl_drvs = []
        fkcurl_zeros = fk_zeros
        fkcurl_grps = [c+'_OFF' for c in fk_ctrls]

        if not fk_zeros:
            for j in jnts:
                zero = mc.createNode('transform', p=j, n=j.replace('_JNT','_curl_ZERO'))
                ctrl = mc.createNode('transform', p=zero, n=j.replace('_JNT','_curl_GRP'))

                if fkcurl_grps:
                    mc.parent(zero, fkcurl_grps[-1])
                else:
                    mc.parent(zero, ctrl_grps[0])

                fkcurl_grps.append(ctrl)
                fkcurl_zeros.append(zero)

        mc.makeIdentity(jnts, apply=1, t=1, r=1, s=1, n=0, pn=1)

        for i, jnt in enumerate(jnts):
            constraint.freeze_joint_orient(jnt)
            mc.setAttr(jnt+'.segmentScaleCompensate', 0)

            drv = mc.createNode('transform', p=fkcurl_zeros[i], n=fkcurl_zeros[i]+'_ATT')
            mc.parent(drv, w=1)

            fkcurl_drvs.append(drv)

            # need an offset node to eat some precision errors
            if use_plugin:
                params = spline.connect_param_node(pri_crv, pri_surf, drv, world_scale_attr=hooks[0]+'.worldScale')
                for p in params:
                    for a in ['stretch','uniformStretch']:
                        mc.connectAttr(settings_ctrl+'.'+a, p+'.'+a)

            else:
                rivet.surface_mtx2(pri_surf, drv, percentage=inverse_plugin)
            constraint.constraint_mtx(fkcurl_grps[i], jnt, s=0)

        for i, drv in enumerate(fkcurl_drvs):
            if i > 0:
                mc.parent(drv, fkcurl_drvs[i-1])
        mc.parent(fkcurl_drvs[0], ctrl_grps[0])

        for i, jnt in enumerate(jnts):
            mc.connectAttr(fkcurl_zeros[i]+'_ATT.t', fkcurl_zeros[i]+'.t')
            mc.connectAttr(fkcurl_zeros[i]+'_ATT.r', fkcurl_zeros[i]+'.r')

        # setup ramp scale and volume preservation
        if add_volume:
            spline.ramp_scale(pri_ctrls, jnts, interpolation=4, driver_attr='sectionScale')
            spline.preserve_volume(fkcurl_grps, jnts, settings_ctrl)

        # setup curl
        if add_curl:
            spline.curl_sdk(fkcurl_grps, settings_ctrl, curl_attr='rz', curl_side_attr='ry')

        # spaces tags
        for ctrl in pri_ctrls:
            spc = spaces.Space(ctrl)
            spc.append_space('IK', parent)
            spc.append_space('FK', ctrl+'_ZERO')

            spc.add_default_spaces()
            spc.set_default_value('FK')

        for ctrl in fk_ctrls:
            spc = spaces.Space(ctrl)

            spc.append_space('spline', ctrl+'_ZERO')
            spc.append_space('FK', utils.get_parent(ctrl+'_ZERO'))

            spc.add_default_spaces()
            spc.set_default_value('spline')

        #Set up pick walking parent setup
        for i, ctrl in enumerate(pri_ctrls):
            if i:
                pickWalk.attribute_tag(ctrl, pri_ctrls[i-1])
            else:
                pickWalk.attribute_tag(ctrl, pickWalk_parent)

        for i, ctrl in enumerate(fk_ctrls):
            if i:
                pickWalk.attribute_tag(ctrl, fk_ctrls[i-1])
            else:
                pickWalk.attribute_tag(ctrl, pickWalk_parent)


        # sets
        self.create_ctrl_set('primary', pri_ctrls)

        if fk_ctrls:
            self.create_ctrl_set('FK', fk_ctrls)

        # fx curves
        #utils.create_cfx_curves(self.bind_joints, self.prefix+'_'+self.part_type)

        utils.set_attrs(pri_ctrls, 's', k=0, l=1)
        utils.set_attrs([c+'_OFF' for c in fk_ctrls], 't v r s', k=0, l=1)

        self.finalize_part()
