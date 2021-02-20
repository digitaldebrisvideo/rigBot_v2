# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import pickWalk
from rigBot.partsLibrary import standardPart

class Nose(standardPart.StandardPart):
    """This is an empty part. It only builds a guide master and empty rig hooks.
        Format your options in the docs as follows for proper auto-documentation.
        OR Generate auto doc strings.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "C".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_reverseJaw_JNT".
            :createBridgeControl: (bool) Create bridge control. Defaults to True.
            :createNoseTipControl: (bool) Create nose tip control. Defaults to True."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('side', default='C', lock=True)
        self.add_option('parent', data_type='hook', default='C_reverseJaw_JNT')
        self.add_option('createBridgeControl', data_type='bool', default=True, rebuild_to_modify=True)
        self.add_option('createNoseTipControl', data_type='bool', default=True, rebuild_to_modify=True)
        self.add_option('createMuzzleControl', data_type='bool', default=False, rebuild_to_modify=True)

        self.add_option('pickWalkParent',
            data_type='string',
            default="C_head_CTL",
            selectable=True,
            tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide. Use Keyword to update any options at build time."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix              # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options = self.options            # Build options
        mirror_value = self.mirror_value  # 1.0 for left and center sided parts and -1.0 for right sided part.

        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)

        jnt_zero, plc, jnt = self.guide_joint('noseBase', constraint_type='parent')
        zero, ctrl = self.guide_ctrl('noseBase', shape='circle', color='yellow', driver=jnt, axis='Z')
        mc.xform(jnt_zero, r=1, t=[0,0,0.5])

        l_jnt_zero, l_plc, l_jnt = self.guide_joint('nostril', constraint_type='parent', alt_prefix=l_prefix)
        l_zero, l_ctrl = self.guide_ctrl('nostril', alt_prefix=l_prefix, shape='circle', color='cyan', driver=l_jnt, axis='Z', scale=[0.5]*3)
        mc.xform(l_jnt_zero, r=1, t=[0.5,0,0])

        r_jnt_zero, r_plc, r_jnt = self.guide_joint('nostril', constraint_type='parent', alt_prefix=r_prefix)
        standardPart.mirror_guide_joint(r_jnt_zero, mirror_behavior=True)
        mc.xform(r_jnt_zero, r=1, t=[-0.5,0,0])

        r_zero, r_ctrl = self.guide_ctrl('nostril', alt_prefix=r_prefix, shape='circle', color='cyan', axis='Z', scale=[0.5]*3)
        mc.xform(r_zero, r=1, t=[-0.5,0,0])
        mc.setAttr(utils.get_parent(r_ctrl)+'.sx', -1)

        if options.get('createBridgeControl'):
            jnt_zero, plc, jnt = self.guide_joint('noseBridge', constraint_type='parent')
            zero, ctrl = self.guide_ctrl('noseBridge', shape='circle', color='yellow', driver=jnt, axis='Z', scale=[0.5]*3)
            mc.xform(jnt_zero, r=1, t=[0,0.6,0.3])

        if options.get('createNoseTipControl'):
            jnt_zero, plc, jnt = self.guide_joint('noseTip', constraint_type='parent')
            zero, ctrl = self.guide_ctrl('noseTip', shape='circle', color='pink', driver=jnt, axis='Z', scale=[0.6]*3)
            mc.xform(jnt_zero, r=1, t=[0,0,0.6])

        if options.get('createMuzzleControl'):
            jnt_zero, plc, jnt = self.guide_joint('noseMuzzle', constraint_type='parent')
            zero, ctrl = self.guide_ctrl('noseMuzzle', shape='cube', color='pink', driver=jnt, axis='Z', scale=[0.6]*3)
            mc.xform(jnt_zero, r=1, t=[0,0,-0.6])

        # This finalizes your guide.
        mc.setAttr(self.guide_master+'.offsetTranslateZ', -0.5)
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

        pickWalk_parent = options.get('pickWalkParent')

        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)

        ctrl_names, zeros, ctrls, offsets, last_nodes = [], [], [], [], []

        ctrl_names.append('{0}_noseBase_CTL'.format(prefix))
        ctrl_names.append('{0}_nostril_CTL'.format(l_prefix))
        ctrl_names.append('{0}_nostril_CTL'.format(r_prefix))

        if options.get('createBridgeControl'):
            ctrl_names.append('{0}_noseBridge_CTL'.format(prefix))

        if options.get('createNoseTipControl'):
            ctrl_names.append('{0}_noseTip_CTL'.format(prefix))

        for name in ctrl_names:
            zero, ctrl, offsets, last_node = self.anim_ctrl(name, inherit_scale=True)
            zeros.append(zero)
            ctrls.append(ctrl)
            offsets.append(offsets)
            last_nodes.append(last_node)

            jnt = name.replace('_CTL', '_JNT')
            mc.parentConstraint(last_node, jnt, mo=1)
            mc.scaleConstraint(last_node, jnt, mo=1)

        pickWalk.attribute_tag( prefix+'_noseBase_CTL',pickWalk_parent)

        if options.get('createBridgeControl'):
            follow = mc.createNode('transform', p=prefix+'_noseBridge_CTL_ZERO', n=prefix+'_noseBridge_follow_GRP')
            mc.parentConstraint(zeros[0], prefix+'_noseBridge_CTL_ZERO', mo=1)
            mc.pointConstraint(last_nodes[0], follow, mo=1)

            pc = mc.pointConstraint(prefix+'_noseBridge_CTL_ZERO', follow, prefix+'_noseBridge_CTL_CONST')[0]
            mc.addAttr(prefix+'_noseBridge_CTL', ln='followNoseBase', min=0, max=1, dv=0.5, k=1)

            mc.connectAttr(prefix+'_noseBridge_CTL.followNoseBase', pc+'.w1')
            utils.connect_reverse(prefix+'_noseBridge_CTL.followNoseBase', pc+'.w0')

            mc.parent(prefix+'_noseBridge_CTL_ZERO', zeros[0])
            pickWalk.attribute_tag(prefix+'_noseBridge_CTL', prefix+'_noseBase_CTL')

        mc.parent(zeros[1:], ctrls[0])
        mc.parent(zeros[0], ctrl_grps[0])

        if options.get('createMuzzleControl'):

            ctrl_names.insert(0,'{0}_noseMuzzle_CTL'.format(prefix))

            zero, ctrl, offsets, last_node = self.anim_ctrl(ctrl_names[0], inherit_scale=True,)

            zeros.insert(0,zero)
            ctrls.insert(0,ctrl)
            offsets.insert(0,offsets)
            last_nodes.insert(0,last_node)

            jnt = ctrl.replace('_CTL', '_JNT')
            mc.parentConstraint(last_node, jnt, mo=1)
            mc.scaleConstraint(last_node, jnt, mo=1)

            mc.parent(prefix+'_noseBase_CTL_ZERO',ctrl)
            mc.parent(zero, prefix+"_nose_parent_CTLS")
            pickWalk.attribute_tag(prefix+'_noseBase_CTL', prefix+'_noseMuzzle_CTL')
            pickWalk.attribute_tag( prefix+'_noseMuzzle_CTL',pickWalk_parent)

        pickWalk.attribute_tag('{0}_nostril_CTL'.format(r_prefix), prefix+'_noseBase_CTL')
        pickWalk.attribute_tag('{0}_nostril_CTL'.format(l_prefix), prefix+'_noseBase_CTL')
        pickWalk.attribute_tag(prefix+'_noseTip_CTL', prefix+'_noseBase_CTL')



        # pickwalk
        pickWalk.attribute_tag('{0}_noseBase_CTL'.format(prefix), pickWalk_parent)
        pickWalk.attribute_tag('{0}_nostril_CTL'.format(l_prefix), '{0}_noseBase_CTL'.format(prefix))
        pickWalk.attribute_tag('{0}_nostril_CTL'.format(r_prefix), '{0}_noseBase_CTL'.format(prefix))

        if options.get('createNoseTipControl'):
            pickWalk.attribute_tag('{0}_noseTip_CTL'.format(prefix), '{0}_noseBase_CTL'.format(prefix))

        if options.get('createBridgeControl'):
            pickWalk.attribute_tag('{0}_noseBridge_CTL'.format(prefix), pickWalk_parent)

        # This finalizes the rig and creates rig sets
        self.finalize_part()
