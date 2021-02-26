# -*- rigBot: part -*-
import maya.cmds as mc
import maya.mel as mm
import pymel.core as pm
import os
# from rigBot import constraint
# from rigBot import control
# from rigBot import pickWalk
# from rigBot import rivet
# from rigBot import spaces
# from rigBot import spline
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
from autoRig import setupSpine
reload (setupSpine)
from autoRig import setupTorso
reload (setupTorso)
from autoRig import autoRig
reload (autoRig)
from autoRig import b4AutoRigOptions
reload (b4AutoRigOptions)



class EncTorso(standardPart.StandardPart):
    """Biped or quad FK / IK torso.

    Note:
            Spine Setup
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
                        default=5,
                        tool_tip='Number of torso joints.',
                        hidden=1,
                        min=0,
                        )

        self.add_option('numberMidCtrls',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=1,
                        min=1,
                        hidden=1,
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
        guide_master = self.guide_master


        number_mid_ctrl = options.get('numberMidCtrls')
        num_joints = options.get('numberJoints')
        noxform_grp = self.guide_master + '_NOX'

        length = 5

        if number_mid_ctrl == 1:
            num_spl_jnts = 4
        else:
            num_spl_jnts = number_mid_ctrl + 2

        if mc.objExists ('root_Mid_jnt'):
            mc.delete ('root_Mid_jnt')

        pp = env.get_parts_paths()[-1]
        branch = r'BidepAutoRig\part_joints\spine_skel.mb'
        import_path = pp.replace('partsLibrary', branch)
        mc.file(import_path, i=1)

        # This finalizes your guide.
        self.finalize_guide()
        jnts_grp = self.guide_master + '_JNTS'
        mc.parent ('root_Mid_jnt', jnts_grp)



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
        #

        setupSpine.setup_spine()
        setupSpine.setup_reverse_spine()
        b4AutoRigOptions.makeDistanceWarning(subject="hips_Mid_jnt", distance=80000, parent="root_Mid_anim")
        autoRig.apply_shapes()
        autoRig.prep_spine_ik_fk_vis()
        self.finalize_part()


