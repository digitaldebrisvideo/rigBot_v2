# -*- rigBot: part  -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import env
from rigBot import utils
from rigBot import control
from rigBot import spline
from rigBot import spaces
from rigBot import pickWalk
from rigBot import constraint
from rigBot import rivet
from rigBot.partsLibrary import standardPart

import os

class SplineChain(standardPart.StandardPart):
    """Spline chain part that can be used for tails and tentacles.
        Uses cmSplineChain plugin node. You also have the option to build as
        a vanilla maya rig without plugin nodes.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "myPart".
            :parent: (str) Parent. Defaults to "C_hip_JNT".
            :numberJoints: (int) Number joints. Defaults to 30.
            :numberPriCtrls: (int) Number of primary controls Defaults to 8.
            :numberSecCtrls: (int) Number of secondary controls Defaults to 8.
            :numberFkCtrls: (int) Number of FK tip controls Defaults to 8.
            :squashStretch: (bool) Add Squash and stretch Defaults to True.
            :createTipCtrl: (bool) Create a tip control for wrapping and grabbing. Defaults to True.
            :makeDynamic: (bool) Create a blendsable dynamic spline curve. Defaults to False."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        # declare variables for this part.
        self.add_option('side', default='C')
        self.add_option('name', required=True, default='tail')
        self.add_option('parent', data_type='hook', default='C_hip_JNT')

        self.add_option('numberJoints',
                    data_type='int',
                    default=30,
                    min=3,
                    max=None,
                    rebuild_to_modify=True)

        self.add_option('numberPriCtrls',
                    tool_tip='Number of primary controls',
                    data_type='int',
                    default=8,
                    min=4,
                    max=None,
                    rebuild_to_modify=True)

        self.add_option('numberSecCtrls',
                    tool_tip='Number of secondary controls',
                    data_type='int',
                    default=8,
                    min=0,
                    max=None,
                    rebuild_to_modify=True)

        self.add_option('numberFkCtrls',
                    tool_tip='Number of FK tip controls',
                    data_type='int',
                    default=8,
                    min=0,
                    max=None,
                    rebuild_to_modify=True)

        self.add_option('createTipCtrl',
                tool_tip='Create a tip control for wrapping and grabbing.',
                data_type='bool',
                default=True,
                rebuild_to_modify=True)

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
           


        '''self.add_option('makeDynamic',
                tool_tip='Create a blendsable dynamic spline curve.',
                data_type='bool',
                default=False,
                rebuild_to_modify=False)'''

        self.add_option('pickWalkParent',
                        data_type='string',
                        default = 'C_cog_CTL',
                        selectable=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

        self.add_option('shiftJoints', data_type='float', hidden=True, min=-1, max=1, default=0)
        self.add_option('shiftPrimaryCtrls', data_type='float', hidden=True, min=-1, max=1, default=0)
        self.add_option('shiftSecondaryCtrls', data_type='float', hidden=True, min=-1, max=1, default=0)

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
        num_pri_ctrls = options.get('numberPriCtrls')
        num_sec_ctrls = options.get('numberSecCtrls')
        num_fk_ctrls = options.get('numberFkCtrls')
        tip_ctrl = options.get('createTipCtrl')

        if num_fk_ctrls > num_joints:
            num_fk_ctrls = num_joints

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
        pri_zeros, ctrls = self.guide_ctrl_chain('pri', axis='X', flat_hierarchy=True,
                                length=length, shape='square', color='yellow', scale=[1,1,1],
                                create_pivot=False,  num_ctrls=num_pri_ctrls)

        # Create secondary ctrls
        sec_ctrls, sec_zeros = [], []
        if num_sec_ctrls:
            sec_zeros, sec_ctrls = self.guide_ctrl_chain('secondary',num_ctrls=num_sec_ctrls,
                                    axis='X', length=length, shape='semi_circle', color='pink',
                                    scale=[1,1,1], create_pivot=False, flat_hierarchy=True)

            cvs = [c+'.cv[*]' for c in sec_ctrls]
            mc.xform(cvs, r=1, ro=[90,0,0])

        # Create fk tip ctrls
        fk_zeros, fk_ctrls = [], []
        if num_fk_ctrls:
            fk_jnt_drivers = jnts[-num_fk_ctrls:]
            fk_zeros, fk_ctrls = self.guide_ctrl_chain('FK',num_ctrls=num_fk_ctrls, allow_offset_ctrls=False,
                                    drivers=fk_jnt_drivers, axis='X', length=length, flat_hierarchy=True,
                                    shape='pin_circle', color='light_blue', scale=[1,1,1], create_pivot=False)

            for c in fk_ctrls:
                mc.xform(c+'.cv[*]', r=1, ro=[0,0,90])

        ##############################################
        #  Create ribbons and connect ctrls and joints

        width = utils.get_distance(ctrls[0], ctrls[1]) * 0.1

        # create spline ribbon and connect primary ctrls
        spline_crv = spline.create_curve_mtx(spline_plcs,
            name=prefix+'_splinePlc',
            axis='Z',
            degree=2,
            parent=noxform_grp)

        spline_surf = spline.create_surface_mtx(spline_plcs,
            name=prefix+'_splinePlc',
            axis='Z',
            degree=2,
            width = width,
            parent=noxform_grp)

        # p_param_nodes = spline.connect_param_node(spline_crv, spline_surf, pri_zeros)
        spline.create_stretch_crv (spline_crv)
        rivet.surface_mtx(spline_surf, jnt_zeros, noxform_grp)

        # Create primary ribbon and connect secndary ctrls
        pri_crv = spline.create_curve_mtx(pri_zeros,
            name=self.prefix+'_primary',
            axis='Z',
            degree=2,
            parent=noxform_grp)

        pri_surf = spline.create_surface_mtx(pri_zeros,
            name=self.prefix+'_primary',
            axis='Z',
            degree=2,
            width=width,
            parent=noxform_grp)

        # connect sec ctrls to primary ribbon
        if num_sec_ctrls:
            sec_crv = spline.create_curve_mtx(sec_zeros,
                name=self.prefix+'_secondary',
                axis='Z',
                degree=2,
                parent=noxform_grp)

            sec_surf = spline.create_surface_mtx(sec_zeros,
                name=self.prefix+'_secondary',
                axis='Z',
                degree=2,
                width=width,
                parent=noxform_grp)

            # s_param_nodes = spline.connect_param_node(pri_crv, pri_surf, sec_zeros)
            # j_param_nodes = spline.connect_param_node(sec_crv, sec_surf, jnt_zeros)

            spline.create_stretch_crv(pri_crv)
            rivet.surface_mtx(pri_surf, jnt_zeros, noxform_grp)

            # s_param_nodes = spline.connect_param_node(pri_crv, pri_surf, sec_zeros)
            # j_param_nodes = spline.connect_param_node(sec_crv, sec_surf, jnt_zeros)

        # OR connect jnts to primary ribbon IF sec ctrls dont exist
        else:
            # s_param_nodes = []
            # j_param_nodes = spline.connect_param_node(pri_crv, pri_surf, jnt_zeros)
            # mc.setAttr(self.guide_master+'.shiftSecondaryCtrls', k=0)
            #
            spline.create_stretch_crv(pri_crv)
            rivet.surface_mtx(pri_surf, jnt_zeros, noxform_grp)

        # for pn in p_param_nodes+s_param_nodes+j_param_nodes:
        #     mc.setAttr(pn+'.stretch', 1)
        #     mc.setAttr(pn+'.uniformStretch', 1)

        # shift joints
        # driver = self.guide_master+'.shiftJoints'
        # spline.connect_shift(driver, j_param_nodes, length, param_attr='paramLength')
        #
        # # shift primaries
        # driver = self.guide_master+'.shiftPrimaryCtrls'
        # spline.connect_shift(driver, p_param_nodes, length, param_attr='paramLength')
        #
        # # shift secondaries
        # if num_sec_ctrls:
        #     driver = self.guide_master+'.shiftSecondaryCtrls'
        #     spline.connect_shift(driver, s_param_nodes, length, param_attr='paramLength')

        # tip ctrl
        if tip_ctrl:
            tip_zero, tip_ctrl = self.guide_ctrl('tip', shape='jack_thin', color='red', scale=[2,2,2])
            mc.pointConstraint(jnts[-1], tip_zero)

        settings_ctrl = self.guide_ctrl('splineSettings', shape='pin_gear', driver=jnts[-1], color='cyan', scale=[2,2,2], create_pivot=0, allow_offset_ctrls=0)
        mc.xform(settings_ctrl[1]+'Shape*.cv[*]', r=1, ro=[0,0,-90])

        utils.set_attrs(plcs, l=1, k=0)
        mc.xform(spline_zeros, r=1, t=[-self.mirror_value,0,0])
        mc.setAttr(self.guide_master+'.offsetTranslateX', -0.5*self.mirror_value)
        mc.setAttr(self.guide_master+'.ry', 90)

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


        # get options to build
        side = options.get('side')
        name = options.get('name')
        parent = options.get('parent')
        add_volume = options.get('addVolumeControls')
        add_curl = options.get('addCurl')
        make_dynamic = options.get('makeDynamic')
        pickWalk_parent = options.get('pickWalkParent')

        mc.parent(jnts, jnt_grps[0])

        # decalre stuff
        pri_zeros, pri_ctrls, pri_offsets, pri_last_nodes = [],[],[],[]
        sec_zeros, sec_ctrls, sef_offsets, sec_last_nodes = [],[],[],[]
        fk_zeros, fk_ctrls, fk_offsets, fk_last_nodes = [],[],[],[]
        tip_zero, tip_ctrl, tip_offsets, tip_last_node = [], [], [], []
        settings_zero, settings_ctrl, settings_offsets, settings_last_node = [], [], [], []

        for node in ctrls:
            if 'splineSettings' in node:
                settings_zero, settings_ctrl, settings_offsets, settings_last_node = self.anim_ctrl(node)
                mc.parent(settings_zero, ctrl_grps[0])

            if 'tip' in node:
                tip_zero, tip_ctrl, tip_offsets, tip_last_node = self.anim_ctrl(node)
                mc.parent(tip_zero, ctrl_grps[0])

            elif 'pri' in node and 'FK' not in node:
                zero, ctrl, off_ctrls, last_node = self.anim_ctrl(node)

                if pri_ctrls:
                    mc.parent(zero, pri_ctrls[-1])
                else:
                    mc.parent(zero, ctrl_grps[0])

                pri_zeros.append(zero)
                pri_ctrls.append(ctrl)
                pri_offsets.extend(off_ctrls)
                pri_last_nodes.append(last_node)

            elif 'secondary' in node:
                zero, ctrl, off_ctrls, last_node = self.anim_ctrl(node)

                if sec_ctrls:
                    mc.parent(zero, sec_ctrls[-1])
                else:
                    mc.parent(zero, ctrl_grps[0])

                sec_zeros.append(zero)
                sec_ctrls.append(ctrl)
                sef_offsets.extend(off_ctrls)
                sec_last_nodes.append(last_node)

            elif 'FK' in node:
                zero, ctrl, off_ctrls, last_node = self.anim_ctrl(node)

                if fk_ctrls:
                    mc.parent(zero, fk_ctrls[-1])
                else:
                    mc.parent(zero, ctrl_grps[0])

                fk_zeros.append(zero)
                fk_ctrls.append(ctrl)
                fk_offsets.extend(off_ctrls)
                fk_last_nodes.append(last_node)

        #add attrs
        if not settings_ctrl:
            settings_ctrl = pri_ctrls[0]
        else:
            constraint.constraint_mtx(jnts[-1], settings_zero, s=0)

        mc.addAttr(settings_ctrl, ln='stretch', k=1, min=0, max=1)
        mc.addAttr(settings_ctrl, ln='uniformStretch', k=1, min=0, max=1)
        mc.addAttr(settings_ctrl, ln='reverseRoot', k=1, min=0, max=1)
        mc.addAttr(settings_ctrl, ln='offset', k=1)

        # create spline ribbon and connect primary ctrls
        width = utils.get_distance(pri_last_nodes[0], pri_last_nodes[1]) * 0.1

        pri_crv = spline.create_curve_mtx(pri_last_nodes,
            name=self.prefix+'_primary',
            axis='Z',
            degree=2,
            parent=noxform_grp)

        pri_surf = spline.create_surface_mtx(pri_last_nodes,
            name=self.prefix+'_primary',
            axis='Z',
            degree=2,
            width=width,
            stretch=1,
            parent=noxform_grp)

        if sec_ctrls:
            sec_crv = spline.create_curve_mtx(sec_last_nodes,
                name=self.prefix+'_secondary',
                axis='Z',
                degree=2,
                parent=noxform_grp)

            sec_surf = spline.create_surface_mtx(sec_last_nodes,
                name=self.prefix+'_secondary',
                axis='Z',
                degree=2,
                width=width,
                parent=noxform_grp)

        else:
            sec_crv, sec_surf = None, None

        # setup curl nodes
        mm.eval('move -r -os -wd 0.001 0 0 '+jnts[0])

        curl_zeros = []
        curl_grps = []

        numberFkCtrls = len(fk_ctrls)
        if numberFkCtrls == 0:
            non_fk_jnts = jnts
        else:
            non_fk_jnts = jnts[:-(numberFkCtrls)]

        for j in non_fk_jnts:
            zero = mc.createNode('transform', p=j, n=j.replace('_JNT','_curl_ZERO'))
            ctrl = mc.createNode('transform', p=zero, n=j.replace('_JNT','_curl_GRP'))

            if curl_grps:
                mc.parent(zero, curl_grps[-1])
            else:
                mc.parent(zero, ctrl_grps[0])

            curl_grps.append(ctrl)
            curl_zeros.append(zero)

        if fk_zeros and curl_grps:
            mc.parent(fk_zeros[0], curl_grps[-1])

        # constrain nodes to surfaces
        if use_plugin:
            if sec_zeros:
                params = spline.connect_param_node(pri_crv, pri_surf, sec_zeros, world_scale_attr=hooks[0]+'.worldScale')
                for p in params:
                    for a in ['stretch','uniformStretch','reverseRoot', 'offset']:
                            mc.connectAttr(settings_ctrl+'.'+a, p+'.'+a)

        else:
            mc.delete(pri_crv)

            if sec_crv:
                mc.delete(sec_crv)
                s_crvs = utils.get_children(pri_surf)
                mc.parent(s_crvs, noxform_grp)

                for i, node in enumerate(sec_zeros):
                    mc.parent(node, w=1)
                    rivet.surface_mtx2(pri_surf, node, percentage=True)
                    if i:
                        mc.parent(node, sec_zeros[i-1])
                    else:
                        mc.parent(node, ctrl_grps[0])


                for a in ['stretch','uniformStretch','reverseRoot']:
                    mc.connectAttr(settings_ctrl+'.'+a, pri_surf+'.'+a)

        fkcurl_drvs = []
        fkcurl_zeros = curl_zeros+fk_zeros
        fkcurl_grps = curl_grps+[c+'_OFF' for c in fk_ctrls]

        mc.makeIdentity(jnts, apply=1, t=1, r=1, s=1, n=0, pn=1)

        for i, jnt in enumerate(jnts):
            constraint.freeze_joint_orient(jnt)
            mc.setAttr(jnt+'.segmentScaleCompensate', 0)

            drv = mc.createNode('transform', p=fkcurl_zeros[i], n=fkcurl_zeros[i]+'_ATT')
            mc.parent(drv, w=1)

            fkcurl_drvs.append(drv)

            # need an offset node to eat some precision errors
            if sec_surf:
                rivet.surface_mtx2(sec_surf, drv)
            else:
                if use_plugin:
                    params = spline.connect_param_node(pri_crv, pri_surf, drv, world_scale_attr=hooks[0]+'.worldScale')
                    for p in params:
                        for a in ['stretch','uniformStretch','reverseRoot']:
                            mc.connectAttr(settings_ctrl+'.'+a, p+'.'+a)

                else:
                    rivet.surface_mtx2(pri_surf, drv, percentage=1)

            constraint.constraint_mtx(fkcurl_grps[i], jnt, s=0)

        for i, drv in enumerate(fkcurl_drvs):
            if i > 0:
                mc.parent(drv, fkcurl_drvs[i-1])
        mc.parent(fkcurl_drvs[0], ctrl_grps[0])

        for i, jnt in enumerate(jnts):
            mc.connectAttr(fkcurl_zeros[i]+'_ATT.t', fkcurl_zeros[i]+'.t')
            mc.connectAttr(fkcurl_zeros[i]+'_ATT.r', fkcurl_zeros[i]+'.r')

        # # setup ramp scale and volume preservation
        # if add_volume:
        #     spline.ramp_scale(pri_ctrls, jnts, secondary_ctrls=sec_ctrls, interpolation=4, driver_attr='sectionScale')
        #     spline.preserve_volume(fkcurl_grps, jnts, settings_ctrl)
        #
        # # setup curl
        # if add_curl:
        #     spline.curl_sdk(fkcurl_grps, settings_ctrl, curl_attr='rz', curl_side_attr='ry')

        # spaces tags
        for ctrl in pri_ctrls:
            spc = spaces.Space(ctrl)
            spc.append_space('IK', parent)
            spc.append_space('FK', ctrl+'_ZERO')

            if tip_ctrl:
                spc.append_space('tipCtrl', tip_ctrl)

            spc.add_default_spaces()
            spc.set_default_value('FK')

        for ctrl in sec_ctrls:
            spc = spaces.Space(ctrl)
            spc.append_space('spline', ctrl+'_ZERO')
            spc.append_space('FK', utils.get_parent(ctrl+'_ZERO'))

            if tip_ctrl:
                spc.append_space('tipCtrl', tip_ctrl)

            spc.add_default_spaces()
            spc.set_default_value('spline')

        for ctrl in fk_ctrls:
            spc = spaces.Space(ctrl)

            spc.append_space('spline', ctrl+'_ZERO')
            spc.append_space('FK', utils.get_parent(ctrl+'_ZERO'))

            if tip_ctrl:
                spc.append_space('tipCtrl', tip_ctrl)

            spc.add_default_spaces()
            spc.set_default_value('spline')

        #Set up pick walking parent setup
        for i, ctrl in enumerate(pri_ctrls):
            if i:
                pickWalk.attribute_tag(ctrl, pri_ctrls[i-1])
            else:
                pickWalk.attribute_tag(ctrl, pickWalk_parent)

        for i, ctrl in enumerate(sec_ctrls):
            if i:
                pickWalk.attribute_tag(ctrl, sec_ctrls[i-1])
            else:
                pickWalk.attribute_tag(ctrl, pickWalk_parent)

        for i, ctrl in enumerate(fk_ctrls):
            if i:
                pickWalk.attribute_tag(ctrl, fk_ctrls[i-1])
            else:
                pickWalk.attribute_tag(ctrl, pickWalk_parent)

        if tip_ctrl:
            pickWalk.attribute_tag(tip_ctrl, pickWalk_parent)

        if settings_ctrl not in pri_ctrls:
            pickWalk.attribute_tag(settings_ctrl, pickWalk_parent)

        # sets
        self.create_ctrl_set('primary', pri_ctrls)

        if sec_ctrls:
            self.create_ctrl_set('secondary', sec_ctrls)

        if fk_ctrls:
            self.create_ctrl_set('FK', fk_ctrls)

        # fx curves
        #utils.create_cfx_curves(self.bind_joints, self.prefix+'_'+self.part_type)

        utils.set_attrs(pri_ctrls+sec_ctrls, 's', k=0, l=1)
        if settings_ctrl:
            utils.set_attrs([settings_ctrl, settings_ctrl+'_OFF'], 't v r s', k=0, l=1)

        utils.set_attrs([c+'_OFF' for c in fk_ctrls], 't v r s', k=0, l=1)

        self.finalize_part()

    def rebuild_guide_post(self):

        ctrl_suffix = utils.get_suffix('animCtrl')
        jnt_suffix = utils.get_suffix('joint')

        prefix = self.prefix
        num_joints = self.options.get('numberFkCtrls')
        chest_jnt = prefix+'_chest_'+jnt_suffix

        ctrls = mc.ls(prefix+'_FK_*_'+ctrl_suffix)
        mc.xform(ctrls, a=1, t=[0,0,0], ro=[0,0,0])

        ctrls = mc.ls(prefix+'_sec_*_'+ctrl_suffix,
                      prefix+'_pri_*_'+ctrl_suffix)
        mc.xform(ctrls, a=1, t=[0,0,0], ro=[0,0,0])
