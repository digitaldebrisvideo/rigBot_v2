# -*- rigBot: part -*-
import maya.cmds as mc
import maya.mel as mm
import pymel.core as pm
import os
import sys
from rigBot import constraint
from rigBot import control
from rigBot import env
from rigBot import pickWalk
from rigBot import rivet
from rigBot import spaces
from rigBot import spline
from rigBot import utils
from rigBot.partsLibrary import standardPart

ppp=env.get_parts_paths()[-1]
pp=ppp.split('rigBot')[0]
x=os.path.join(pp, 'enc')

if x not in sys.path:
	sys.path.insert(0, x)
import enc
from enc import encLib
from enc import autoRig

from autoRig import setupIKLegs
reload (setupIKLegs)
from autoRig import setupFKLegs
reload (setupFKLegs)
from autoRig import setupIKFKBlendLeg
reload (setupIKFKBlendLeg)
from autoRig import setupStretchIKLeg
reload (setupStretchIKLeg)
from autoRig import setupRibbons
reload (setupRibbons)



class EncBipedLeg(standardPart.StandardPart):
    """Biped leg module. Includes FK/ IK, twist, stretch, bendy and soft IK.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_hip_JNT".
            :ikHandleParent: (str) Optional IK handle parent for connecting to a foot part. Will default to it's own IK control if the node doesnt exist. Defaults to "L_foot_IK_handle_driver_JNT".
            :numberTwistJoints: (int) Number of twist joints PER upper and lower leg. Defaults to 4.
            :makeBendy: (bool) Add bendy controls. Defaults to False.

        Note:
            If using the bendy feature you will need enough twist joints to allow for proper spline deformation."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('parent', data_type='hook', default='hips_Mid_bind')

        # self.add_option('ikHandleParent',
        #                 data_type='hook',
        #                 default='L_foot_IK_handle_driver_JNT',
        #                 hidden=True,
        #                 tool_tip="Optional IK handle parent for connecting to a "+\
        #                          "foot part. Will default to it's own IK control "+\
        #                          "if the node doesnt exist.")
        #
        # self.add_option('fkAnkleJoint',
        #                 data_type='hook',
        #                 default='L_ankle_JNT',
        #                 hidden=True,
        #                 tool_tip="Optional FK ankle joint to drive lower leg twist.")
        #
        # self.add_option('numberTwistJoints',
        #                 data_type='int',
        #                 rebuild_to_modify=True,
        #                 default=4,
        #                 min=0,
        #                 hidden=True,
        #                 tool_tip='Number of twist joints PER upper and lower leg.')
        #
        # self.add_option('flipJoints',
        #                 data_type='bool',
        #                 default=False,
        #                 hidden=True,
        #                 tool_tip='Flip the up axis of the bind joints. '+\
        #                          '(Useful when the knee points backwards.)')
        #
        # self.add_option('makeBendy',
        #          data_type='bool',
        #          default=False,
        #          rebuild_to_modify=True,
        #          hidden=True,
        #          tool_tip='Add bendy controls.')
        #
        # self.add_option('transOrientiation',
        #          data_type='enum',
        #          default='world',
        #          enum='world:downBone',
        #          hidden=True,
        #          tool_tip='Orient the translates on IK control to the world OR down the bone.')

        self.add_option('pickWalkParent',
                        data_type='string',
                        default = 'C_hip_CTL',
                        selectable=True,
                        hidden=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")


    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        prefix, options = self.create_guide_master(**kwargs)

        prefix       = self.prefix
        options      = self.options
        mirror_value = self.mirror_value


        noxform_grp = self.guide_master + '_NOX'

        if mc.objExists ('hips_Mid_jnt'):
            mc.delete ('hips_Mid_jnt')


        pp = env.get_parts_paths()[-1]
        branch = r'BidepAutoRig\part_joints\legs_skel.mb'
        import_path = pp.replace('partsLibrary', branch)
        mc.file(import_path, i=1)

        snaps=[u'heel_Rt_plc', u'tiltIn_Rt_plc', u'tiltOut_Rt_plc', u'toeTip_Rt_plc', u'heel_Lt_plc', u'tiltOut_Lt_plc',
         u'tiltIn_Lt_plc', u'toeTip_Lt_plc', u'hips_Mid_jnt', u'legBase_Lt_jnt',
         u'thigh_Lt_jnt', u'knee_Lt_jnt', u'legEnd_Lt_jnt', u'foot_Lt_bind', u'toe_Lt_bind', u'toeEnd_Lt_jnt',
         u'knee_Lt_VJ_bind', u'uprKnee_Lt_jnt', u'lwrKnee_Lt_jnt', u'legBase_Rt_jnt', u'thigh_Rt_jnt', u'knee_Rt_jnt',
         u'legEnd_Rt_jnt', u'foot_Rt_bind', u'toe_Rt_bind', u'toeEnd_Rt_jnt', u'knee_Rt_VJ_bind', u'uprKnee_Rt_jnt',
         u'lwrKnee_Rt_jnt']
        for snap in snaps:
            target='snap_'+snap
            if mc.objExists (target):
                mc.delete (mc.parentConstraint (target, snap, mo=0))

        if mc.objExists ('snap_root_Mid_jnt'):
            mc.delete (mc.parentConstraint('snap_root_Mid_jnt', 'drivenLeg_root03_Mid_anim', mo=0))


        # This finalizes your guide.
        self.finalize_guide()
        jnts_grp = self.guide_master + '_JNTS'
        foot_plcrs=['drivenLeg_root03_Mid_anim', u'heel_Rt_plc', u'tiltIn_Rt_plc', u'tiltOut_Rt_plc', u'toeTip_Rt_plc', u'heel_Lt_plc', u'tiltOut_Lt_plc', u'tiltIn_Lt_plc', u'toeTip_Lt_plc']

        mc.parent ('hips_Mid_jnt', foot_plcrs, jnts_grp)

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
        noxform_grp = self.noxform_grp

        setupIKLegs.setup_ik()
        setupFKLegs.setup_fk()
        setupIKFKBlendLeg.setup_ik_fk_blend()
        setupStretchIKLeg.setup_stretch_ik()
        setupRibbons.setup_ribbons(key='leg')

        # nox_grp = self.part_master.replace ('_GRP', '_NOX')
        # print nox_grp

        xx = mc.getAttr('legEnd_Rt_ik.tx')
        mc.setAttr('legEnd_Rt_ik.tx', (-1 * xx))
        xx = mc.getAttr('legEnd_Rt_jnt.tx')
        mc.setAttr('legEnd_Rt_jnt.tx', (-1 * xx))

        y_val = mc.getAttr("legIKFK_Lt_a0.translateY")
        mc.setAttr("legIKFK_Rt_a0.translateY", y_val)

        t=mc.getAttr ('legEnd_Rt_ik.tx')
        v=(t*-1)
        mc.setAttr ('legEnd_Rt_ik.tx' ,v)

        t=mc.getAttr ('legEnd_Rt_jnt.tx')
        v = (t * -1)
        mc.setAttr ('legEnd_Rt_jnt.tx',v)

        # jnts=[u'legRig_Lt_grp', u'legRig_Rt_grp']
        # ctrls=[ u'thigh_Lt_a0', u'thigh_Rt_a0', u'legIKFK_Rt_a0', u'legIKFK_Lt_a0',
        #  u'legShaper_Lt_grp', u'legShaper_Rt_grp',
        #  u'legIk_Lt_a0', u'kneeUpVectorIk_Lt_a0', u'legIk_Rt_a0', u'kneeUpVectorIk_Rt_a0']
        # mc.parent (jnts, nox_grp)
        # mc.parent (ctrls, ctrl_grps[0])
        #
        # nox_name=ctrl_grps[0].replace ('_parent_CTLS', '_CTLS_NOX')
        #
        # nox_ctrls=[u'kneePV_Lt_a0', u'kneePV_Rt_a0',u'legRibbonCtrl_Lt_grp', u'legRibbonCtrl_Rt_grp']
        # nox=mc.createNode ('transform', name=nox_name, p=ctrl_grps[0])
        # mc.parent (nox_ctrls, nox)
        # mc.setAttr (nox+'.inheritsTransform', 0)
        #
        # mc.select ('*_ikh')
        # mc.hide()
        # mc.delete ('rig_XXX_grp')