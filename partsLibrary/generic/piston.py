# -*- rigBot: part  -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import control
from rigBot import utils
from rigBot.partsLibrary import standardPart

class Piston(standardPart.StandardPart):
    """Create a piston setup of two joints, with two different parents that aim at each other.
        Both joints are upvectors to main parent. A center joints is also created.

        Piston module. Auto doc.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Name token for this rig part. Defaults to "myPart".
            :startParent: (str) Start parent. Defaults to "L_shoulder_JNT".
            :endParent: (str) End parent. Defaults to "C_chest_JNT".
            :startPosition: (list) Start position. Defaults to [].
            :endPosition: (list) End position. Defaults to []."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('name', required=True)
        self.add_option('startParent', data_type='hook', default='L_shoulder_JNT')
        self.add_option('endParent', data_type='hook', default='C_chest_JNT')
        self.add_option('startPosition', data_type='selection')
        self.add_option('endPosition', data_type='selection')

    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix       = self.prefix
        options      = self.options
        mirror_value = self.mirror_value

        start_position = options.get('startPosition')
        end_position = options.get('endPosition')

        start_pos = [0, 1, 0]
        end_pos = [0, -1, 0]

        start_position = mc.ls(start_position)
        end_position = mc.ls(end_position)

        if start_position:
            l = utils.snap_locator(start_position)
            start_pos = mc.xform(l, ws=1, q=1, t=1)
            mc.delete(l)

        if end_position:
            l = utils.snap_locator(end_position)
            end_pos = mc.xform(l, ws=1, q=1, t=1)
            mc.delete(l)

        # Create joints
        start_zero, start_plc, start_jnt = self.guide_joint('start', constraint_type='point')
        mid_zero, mid_plc, mid_jnt = self.guide_joint('startMid', constraint_type='point')
        mid_b_zero, mid_b_plc, mid_b_jnt = self.guide_joint('endMid', constraint_type='point')
        end_zero, end_plc, end_jnt = self.guide_joint('end', constraint_type='point')

        mirror = self.mirror_value

        # constraint
        mc.aimConstraint(start_jnt, end_jnt, aim=[mirror,0,0], u=[0, mirror,0], wu=[mirror,0,0], wut='objectRotation', wuo=start_plc)
        mc.aimConstraint(end_jnt, start_jnt, aim=[-mirror,0,0], u=[0, mirror,0],wu=[mirror,0,0],  wut='objectRotation', wuo=start_plc)

        mc.delete(mid_zero)
        mc.pointConstraint(start_jnt, end_jnt, mid_jnt)

        mc.delete(mid_b_zero)
        mc.pointConstraint(start_jnt, end_jnt, mid_b_jnt)

        mc.parent(mid_b_jnt, end_jnt)
        mc.parent(mid_jnt, start_jnt)

        mc.setAttr(end_jnt+'.jo', 0,0,0)
        mc.setAttr(start_jnt+'.jo', 0,0,0)
        mc.setAttr(mid_jnt+'.jo', 0,0,0)
        mc.setAttr(mid_b_jnt+'.jo', 0,0,0)

        # place guide rig
        tmp1 = mc.createNode('transform')
        tmp2 = mc.createNode('transform')
        tmp3 = mc.createNode('transform')

        mc.xform(tmp1, ws=1, t=start_pos)
        mc.xform(tmp2, ws=1, t=end_pos)
        mc.delete(mc.pointConstraint(tmp1, tmp2, tmp3))
        mc.delete(mc.pointConstraint(tmp3, self.guide_master))
        mc.delete(tmp1, tmp2, tmp3)

        mc.xform(start_zero, ws=1, t=[0,1,0])
        mc.xform(end_zero, ws=1, t=[0,-1,0])

        utils.set_attrs([start_plc, end_plc], 'r s', l=1, k=0)
        mc.xform(start_zero, ws=1, t=start_pos)
        mc.xform(end_zero, ws=1, t=end_pos)

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
        bind_jnts       = self.bind_joints
        hooks             = self.hooks
        ctrl_grps         = self.ctrl_grps
        jnt_grps          = self.jnt_grps

        jnt_suffix = utils.get_suffix('joint')

        # group start jnt
        start_jnt = prefix+'_start_'+jnt_suffix
        start_child_jnt = prefix+'_startMid_'+jnt_suffix
        end_jnt = prefix+'_end_'+jnt_suffix
        end_child_jnt = prefix+'_endMid_'+jnt_suffix

        start_grp = mc.createNode('transform', n=start_jnt+'_GRP', p=start_jnt)
        end_grp = mc.createNode('transform', n=end_jnt+'_GRP', p=end_jnt)

        mc.parent(start_grp, jnt_grps[0])
        mc.parent(end_grp, jnt_grps[1])

        mc.parent(start_jnt, start_grp)
        mc.parent(end_jnt, end_grp)

        # constraint
        mirror = self.mirror_value
        mc.aimConstraint(start_jnt, end_jnt, aim=[mirror,0,0], u=[0,1,0], wu=[0,1,0], wut='objectRotation', wuo=start_grp, mo=1)
        mc.aimConstraint(end_jnt, start_jnt, aim=[-mirror,0,0], u=[0,1,0],wu=[0,1, 0],  wut='objectRotation', wuo=end_grp, mo=1)

        mc.pointConstraint(start_jnt, end_jnt, start_child_jnt)
        mc.pointConstraint(start_child_jnt, end_child_jnt)
        mc.hide(end_child_jnt)

        # This finalizes guide and creates rig sets
        self.finalize_part()



