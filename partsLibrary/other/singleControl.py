# -*- rigBot: part  -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import spline
from rigBot import control
from rigBot import spaces
from rigBot import pickWalk
from rigBot.partsLibrary import standardPart

class SingleControl(standardPart.StandardPart):
    """FK chain rig part. Joints aim at the child jnt and are
        upvectored to their respective ctrl. Optionally just use a parent constraint, rather than aiming.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "myPart".
            :parent: (str) Parent. Defaults to "C_hip_JNT ".
            :numberJoints: (int) Number joints. Defaults to 6.
            :singleJoint: (bool) Single joint. Defaults to False.
            :squashStretch: (bool) Squash stretch. Defaults to True.
            :aimDownBone: (bool) If True use an aim constraint to aim the joint down the bone to the child ctrl. Otherwise, use a parentConstraint. Defaults to True."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('name', required=True)
        self.add_option('parent', data_type='hook', default='C_hip_JNT')

        self.add_option('pickWalkParent',
                        data_type='string',
                        selectable=True,
                        default="",
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix       = self.prefix
        options      = self.options
        mirror_value = self.mirror_value

        jnt_zero, plc, jnt = self.guide_joint(constraint_type='parent')
        zero, ctrl = self.guide_ctrl(shape='sphere', color='pink', driver=jnt, axis='X')
        ctrls = [ctrl]
        zeros = [zero]

        # lock stuff
        pivots = [mc.listRelatives(c, p=1)[0] for c in ctrls]
        utils.set_attrs(zeros, l=1, k=0)
        utils.set_attrs(pivots, 't s', l=1, k=0)

        mc.setAttr(self.guide_master+'.offsetTranslateX', -0.5*self.mirror_value)

        # This finalizes your guide.
        self.finalize_guide()

    def build_rig(self):
        """This builds your anim rig."""

        # create rig part top nodes
        self.create_part_master()

        # Get all the relevant part info
        prefix            = self.prefix
        options           = self.options
        anim_ctrls        = self.anim_ctrls
        bind_jnts         = self.bind_joints
        hooks             = self.hooks
        ctrl_grps         = self.ctrl_grps
        jnt_grps          = self.jnt_grps

        mirror = self.mirror_value
        
        parent = options.get('parent')
        pickWalk_parent = options.get('pickWalkParent')

        # Create ctrls
        zeros, ctrls, offsets, last_nodes = [], [], [], []

        for i, ctrl_name in enumerate(anim_ctrls):
            zero, ctrl, offCtrls, last_node = self.anim_ctrl(ctrl_name)
            zeros.append(zero)
            ctrls.append(ctrl)
            offsets.append(offCtrls)
            last_nodes.append(last_node)

            #Setup pickwaliking attributes for the fingers
            i = 0
            ctrls.reverse()
            for ctrl in ctrls:

                if i+1 < len(ctrls):

                    pickWalk.attribute_tag(ctrls[i],ctrls[i+1])
                else:
                    pickWalk.attribute_tag(ctrls[i],pickWalk_parent)
                    break

                i+=1
            ctrls.reverse()

        mc.parentConstraint(last_nodes[0], bind_jnts[0], mo=1, n=bind_jnts[0]+'_prc')
        mc.scaleConstraint(last_nodes[0], bind_jnts[0], mo=1, n=bind_jnts[0]+'_sc')      
        mc.parent(zeros[0], ctrl_grps[0])
        mc.parent(bind_jnts, jnt_grps[0])
     
        spaces.tag(ctrls)

        self.finalize_part()
