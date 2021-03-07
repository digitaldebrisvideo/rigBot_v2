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

class MovablePivot(standardPart.StandardPart):
    """ movable pivot just to mimic the global control from rigBot
        upvectored to their respective ctrl. Optionally just use a parent constraint, rather than aiming.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "myPart".
            :parent: (str) Parent. Defaults to "C_hip_JNT ".
            :singleJoint: (bool) Single joint. Defaults to False.
            """

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('name', required=True)
        self.add_option('parent', data_type='hook', default='C_hip_JNT')

        '''self.add_option('singleJoint',
                    data_type='bool',
                    default=False,
                    rebuild_to_modify=True)
        '''

        self.add_option('pickWalkParent',
                        data_type='string',
                        selectable=True,
                        default="world_A_CTL",
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide."""
        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix       = self.prefix
        options      = self.options
        mirror_value = self.mirror_value

        single_joint = True
        pickWalk_parent = options.get('pickWalkParent')
        #pickWalk_parent = "world_A_CTL"



        jnt_zero, plc, jnt = self.guide_joint(constraint_type='parent')
        zero, ctrl = self.guide_ctrl(shape='circle', color='light_blue', driver=jnt, axis='X')
        ctrls = [ctrl]
        zeros = [zero]




        MPA_zero, MPA_ctrl = self.guide_ctrl(shape='cog', color='teal', driver=jnt, axis='X')
        ctrls.append(MPA_ctrl)
        zeros.append(MPA_zero)
        mc.setAttr((MPA_ctrl +'.' + 'rz'), 90)
        mc.makeIdentity(MPA_ctrl, apply = True, rotate = True)

        MPB_zero, MPB_ctrl = self.guide_ctrl(shape='cog', color='cyan', driver=jnt, axis='X')
        ctrls.append(MPB_ctrl)
        zeros.append(MPB_zero)
        mc.setAttr((MPB_ctrl +'.' + 'rz'), 90)
        mc.setAttr( (MPB_ctrl + "." + "scale") , .75,.75,.75)
        mc.makeIdentity(MPB_ctrl, apply = True, rotate = True, scale=  True)

        mc.parent(MPB_zero, MPA_ctrl)
        mc.parent(zero, MPB_ctrl)

        # lock stuff
        pivots = [mc.listRelatives(c, p=1)[0] for c in ctrls]
        utils.set_attrs(zeros, l=1, k=0)
        utils.set_attrs(pivots, 't s', l=1, k=0)

        mc.setAttr(self.guide_master +'.offsetTranslateX', -0.5*self.mirror_value)


        # This finalizes your guide.
        self.finalize_guide()

    def build_rig(self):
        """This builds your anim rig."""

        # create rig part top nodes
        self.create_part_master()

        # Get all the relevant part info
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

        parent = options.get('parent')
        single_joint = True  # now hard coded..
        #number_joints = options.get('numberJoints')
        #pickWalk_parent = options.get('pickWalkParent')
        pickWalk_parent = 'world_A_CTL'

        # Create ctrls
        zeros, ctrls, offsets, last_nodes = [], [], [], []

        for i, ctrl_name in enumerate(anim_ctrls):
            zero, ctrl, offCtrls, last_node = self.anim_ctrl(ctrl_name)
            zeros.append(zero)
            ctrls.append(ctrl)
            offsets.append(offCtrls)
            last_nodes.append(last_node)

            #Setup pickwalking attributes
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

        if len(ctrls) > 1:
            for i in range(1, len(ctrls), 1):
                ctrl_parent =  mc.listRelatives(last_nodes[i-1] , p = True)[0]

                loc = mc.spaceLocator(name = (last_nodes[i-1] + "_offsetLOC"))[0]
                mc.parent(loc,ctrl_parent )
                mc.connectAttr((last_nodes[i-1] + "." + "translateX"), (loc+ "." + "rotatePivotX"))
                mc.connectAttr((last_nodes[i-1] + "." + "translateY"), (loc + "." + "rotatePivotY"))
                mc.connectAttr((last_nodes[i-1] + "." + "translateZ"), (loc + "." + "rotatePivotZ"))

                mc.connectAttr((last_nodes[i-1] + "." + "translateX"), (loc + "." + "scalePivotX"))
                mc.connectAttr((last_nodes[i-1] + "." + "translateY"), (loc + "." + "scalePivotY"))
                mc.connectAttr((last_nodes[i-1] + "." + "translateZ"), (loc + "." + "scalePivotZ"))

                mc.connectAttr((last_nodes[i-1] + "." + "rotateX"), (loc + "." + "rotateX"))
                mc.connectAttr((last_nodes[i-1] + "." + "rotateY"), (loc + "." + "rotateY"))
                mc.connectAttr((last_nodes[i-1] + "." + "rotateZ"), (loc + "." + "rotateZ"))

                mc.parent(zeros[i], loc)




        # parentCon/scaleCon the joint to the last control
        mc.parentConstraint(ctrls[-1], bind_joints[0], mo=1, n=bind_joints[0] + '_prc')
        mc.scaleConstraint(ctrls[-1], bind_joints[0], mo=1, n=bind_joints[0] + '_sc')


        mc.parent(zeros[0], ctrl_grps[0])
        mc.parent(bind_joints, jnt_grps[0])


        #utils.create_cfx_curves(self.bind_joints, self.prefix+'_'+self.part_type)

        if len(ctrls) > 1:
            spaces.tag(ctrls, arg='partParent:'+self.options.get('parent'))
        else:
            spaces.tag(ctrls)

        self.finalize_part()
