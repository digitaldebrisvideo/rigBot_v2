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
from autoRig import setupNeck
reload (setupNeck)
from autoRig import autoRig
reload (autoRig)


class EncNeck(standardPart.StandardPart):

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('side', default='C')
        self.add_option('parent', data_type='hook', default='chest_Mid_bind')


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

        if mc.objExists ('drivenArm_chest_Mid_bind'):
            mc.delete ('drivenArm_chest_Mid_bind')


        pp = env.get_parts_paths()[-1]
        branch = r'BidepAutoRig\part_joints\neck_skel.mb'
        import_path = pp.replace('partsLibrary', branch)
        mc.file(import_path, i=1)

        if mc.objExists ('snap_chest_Mid_jnt'):
            mc.delete (mc.parentConstraint ('snap_chest_Mid_bind', 'drivenNeck_chest_Mid_bind'))


        snaps=[u'head_Mid_bind', u'headEnd_Mid_jnt', u'eye_Lt_bind', u'eye_Rt_bind', u'headTop_Mid_bind',
         u'headRear_Mid_bind', u'headSide_Lt_bind', u'headSide_Rt_bind', u'neck01_Mid_bind', u'neck02_Mid_bind',
         u'neck03_Mid_bind', u'neckEnd_Mid_jnt']

        for snap in snaps:
            target='snap_'+snap
            if mc.objExists (target):
                mc.delete (mc.parentConstraint (target, snap))




        # This finalizes your guide.
        self.finalize_guide()
        jnts_grp = self.guide_master + '_JNTS'
        mc.parent ('drivenNeck_chest_Mid_bind', jnts_grp)

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


        setupNeck.setup_neck()
        setupNeck.setup_head()
        autoRig.apply_shapes()


        #
        # mc.parent ('bottomNeckSkin_Mid_jnt', 'topNeckSkin_Mid_jnt', jnt_grps[0])
        # mc.parent ('neck_rig', noxform_grp)
        # mc.parent ('neck_ctrls', ctrl_grps[0])
        # mc.parent ('rotateReader_grp', jnt_grps[0])
        #
        # mc.parent ('drivenArm_chest_Mid_bind', jnt_grps[0])
        #
        # scales = [u'neck01_Mid_bind', u'neck02_Mid_bind', u'neck03_Mid_bind', u'neckEnd_Mid_jnt',u'headTop_Mid_bind', u'headRear_Mid_bind', u'headSide_Lt_bind', u'headSide_Rt_bind']
        # utils.break_connections(nodes=scales, attrs='s')