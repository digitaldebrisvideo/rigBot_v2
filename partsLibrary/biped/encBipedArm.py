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
from autoRig import setupIKArms
reload (setupIKArms)
from autoRig import setupFKArms
reload (setupFKArms)

class EncBipedArm(standardPart.StandardPart):
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
                        default='',
                        tool_tip="Optional IK handle parent for connecting to a " + \
                                 "foot part. Will default to it's own IK control " + \
                                 "if the node doesnt exist.")

        self.add_option('numberTwistJoints',
                        data_type='int',
                        min=0,
                        default=4,
                        tool_tip='Number of twist joints for the upper and lower arms',
                        rebuild_to_modify=True)

        self.add_option('makeBendy',
                        data_type='bool',
                        default=True,
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


        noxform_grp = self.guide_master + '_NOX'

        if mc.objExists ('chest_armDriven_bind'):
            mc.delete ('chest_armDriven_bind')


        pp = env.get_parts_paths()[-1]
        branch = r'BidepAutoRig\part_joints\arms_skel.mb'
        import_path = pp.replace('partsLibrary', branch)
        mc.file(import_path, i=1)

        # This finalizes your guide.
        self.finalize_guide()
        jnts_grp = self.guide_master + '_JNTS'
        mc.parent ('chest_armDriven_bind', jnts_grp)

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

        setupIKArms.setup_ik()
        setupFKArms.setup_fk()