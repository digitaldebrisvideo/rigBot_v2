# -*- rigBot: part -*-
import maya.cmds as mc
import maya.mel as mm
import pymel.core as pm
import os
from rigBot import constraint
from rigBot import control
from rigBot import env
from rigBot import pickWalk
from rigBot import rivet
from rigBot import spaces
from rigBot import spline
from rigBot import utils
from rigBot.partsLibrary import standardPart

import sys
from rigBot import env
pp=env.get_parts_paths()[-1]
branch=r'BidepAutoRig'
branch_a=r'BidepAutoRig\encAssets\rig'
x=pp.replace ('partsLibrary', branch)
y=pp.replace ('partsLibrary', branch_a)
if x not in sys.path:
	sys.path.insert(0, x)
import encAssets
if y not in sys.path:
	sys.path.insert(0, y)
import autoRig
from autoRig import setupNeck
from autoRig import autoRig



class EncNeck(standardPart.StandardPart):

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('side', default='C')
        self.add_option('parent', data_type='hook', default='C_chest_end_JNT')

        self.add_option('numberJoints',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=4,
                        tool_tip='Numder of neck joints.',
                        hidden=True,
                        min=2)

        self.add_option('numberMidCtrls',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=1,
                        min=1,
                        hidden=True,
                        tool_tip='Number of mid neck IK ctrls.')

        self.add_option('createJaw',
                        data_type='bool',
                        rebuild_to_modify=True,
                        default=True,
                        hidden=True,
                        tool_tip='Create jaw joint and control.')

        self.add_option('createReverseJaw',
                        data_type='bool',
                        rebuild_to_modify=True,
                        default=False,
                        hidden=True,
                        tool_tip='Create reverse jaw ctrl for the upper head.')

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

        if mc.objExists ('chestDriven_Mid_jnt'):
            mc.delete ('chestDriven_Mid_jnt')


        pp = env.get_parts_paths()[-1]
        branch = r'BidepAutoRig\part_joints\neck_skel.mb'
        import_path = pp.replace('partsLibrary', branch)
        mc.file(import_path, i=1)

        # This finalizes your guide.
        self.finalize_guide()
        jnts_grp = self.guide_master + '_JNTS'
        mc.parent ('chestDriven_Mid_jnt', jnts_grp)

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

        # num_joints = options.get('numberJoints')
        # number_mid_ctrl = options.get('numberMidCtrls')
        # create_jaw = options.get('createJaw')
        # create_skull = options.get('createReverseJaw')
        # pickWalk_parent = options.get('pickWalkParent')
        # create_surface = options.get('createSurfaceDriver')
        # create_fk_ctrls = options.get('createFKShaperCtrls')

        setupNeck.setup_neck()
        setupNeck.setup_head()