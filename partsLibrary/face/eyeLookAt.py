# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import pickWalk
from rigBot.partsLibrary import standardPart

class EyeLookAt(standardPart.StandardPart):
    """Center eye look at module. This builds just a single center sided control to drive the Left and Right look at controls.
        The control will have head and worlds spaces.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "C".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_head_JNT"."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('side', default='C')
        self.add_option('parent', data_type='hook', default='C_head_JNT')

        self.add_option('pickWalkParent',
                        data_type='string',
                        default = 'C_head_CTL',
                        selectable=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide. Use KWARGS to update any options at build time."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix              # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options = self.options            # Build options
        mirror_value = self.mirror_value  # 1.0 for left and center sided parts and -1.0 for right sided part.

        # Start coding suckka !!
        self.guide_ctrl('lookAt', shape='jack_thin', axis='Z', create_pivot=False)

        # This finalizes your guide.
        self.finalize_guide()

    def build_rig(self):
        """This builds your anim rig."""

        # create rig part top nodes
        self.create_part_master()

        prefix            = self.prefix                 # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options           = self.options                # Build options
        anim_ctrls        = self.anim_ctrls             # Anim controls in this part
        bind_joints       = self.bind_joints            # Bind joints in this rig part
        world_scale_attr  = self.hooks[0]+'.worldScale' # World scale multiplier (Each hooks has it's own world scale)
        hooks             = self.hooks                  # A hook grp is created per hook attribute.
        ctrl_grps         = self.ctrl_grps              # A ctrl group is created per hook. Parent controls here.
        jnt_grps          = self.jnt_grps               # A joint groupd is created per hook. Parent joints here.
        noxform_grp       = self.noxform_grp            # No scale, no transform group for this rig part.
        mirror_value      = self.mirror_value           # 1.0 for left and center sided parts and -1.0 for right sided part.

        look_loc = utils.snap_locator(prefix+'_lookAt_CTL_REF')
        pickWalk_parent = options.get('pickWalkParent')
        # Create ctrls
        look_at_zero, look_at_ctrl, look_at_offsets, look_at_last = self.anim_ctrl(prefix+'_lookAt_CTL', match_position=look_loc)
        mc.parent(look_at_zero, ctrl_grps[0])

        mc.delete(look_loc)
        utils.set_attrs(look_at_ctrl, 's', l=1, k=0)

        spaces.tag(look_at_ctrl)
        pickWalk.attribute_tag(look_at_ctrl, pickWalk_parent)
        # This finalizes the rig and creates rig sets
        self.finalize_part()
