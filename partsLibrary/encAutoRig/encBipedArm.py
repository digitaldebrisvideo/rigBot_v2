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

from autoRig import setupIKArms
reload (setupIKArms)
from autoRig import setupFKArms
reload (setupFKArms)
from autoRig import setupIKFKBlendArm
reload (setupIKFKBlendArm)
from autoRig import setupStretchIKArm
reload (setupStretchIKArm)
from autoRig import setupWrists
reload (setupWrists)
from autoRig import setupRibbons
reload (setupRibbons)
from autoRig import setupClavicle
reload (setupClavicle)
from autoRig import setupScapula
reload (setupScapula)
from autoRig import setupTrapezius
reload (setupTrapezius)


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


        noxform_grp = self.guide_master + '_NOX'

        if mc.objExists ('drivenArm_chest_Mid_bind'):
            mc.delete ('drivenArm_chest_Mid_bind')


        pp = env.get_parts_paths()[-1]
        branch = r'BidepAutoRig\part_joints\arms_skel.mb'
        import_path = pp.replace('partsLibrary', branch)
        mc.file(import_path, i=1)

        drivens=[u'drivenArm_chest_Mid_bind', u'driven_neck03_Mid_bind']

        if mc.objExists ('snap_chest_Mid_bind'):
            mc.delete (mc.parentConstraint ('snap_chest_Mid_bind', drivens[0], mo=0))
        if mc.objExists('snap_neck03_Mid_bind'):
            mc.delete(mc.parentConstraint('snap_neck03_Mid_bind', drivens[1], mo=0))

        snaps=[ u'clavicle_Lt_bind', u'clavicleEnd_Lt_jnt', u'scapulaAim_Lt_jnt', u'scapulaEnd_Lt_jnt',
         u'armBase_Lt_jnt', u'shoulder_Lt_jnt', u'elbow_Lt_jnt', u'hand_Lt_jnt', u'handEnd_Lt_jnt', u'scapulaTarget_jnt',
         u'clavicle_Rt_bind', u'clavicleEnd_Rt_jnt', u'scapulaAim_Rt_jnt', u'scapulaEnd_Rt_jnt', u'armBase_Rt_jnt',
         u'shoulder_Rt_jnt', u'elbow_Rt_jnt', u'hand_Rt_jnt', u'handEnd_Rt_jnt']
        for snap in snaps:
            target='snap_'+snap
            if mc.objExists (target):
                mc.delete (mc.delete (mc.parentConstraint(target, snap, mo=0)))




        # This finalizes your guide.
        self.finalize_guide()
        jnts_grp = self.guide_master + '_JNTS'
        mc.parent ('drivenArm_chest_Mid_bind', jnts_grp)

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


        setupIKArms.setup_ik()
        setupFKArms.setup_fk()
        setupIKFKBlendArm.setup_ik_fk_blend()
        setupStretchIKArm.setup_stretch_ik()
        setupWrists.setup_wrists()
        setupClavicle.setup_clavicle()
        setupScapula.setup_scapula()
        setupTrapezius.setup_trapezius()
        setupRibbons.setup_ribbons('arm')

        # to_parent = [u'elbowPV_Lt_a0', u'elbowPV_Rt_a0', u'shoulder_Lt_a0', u'shoulder_Rt_a0', u'armIKFK_Rt_a0', u'armIKFK_Lt_a0',
        #  u'armRibbonCtrl_Lt_grp', u'armRibbonCtrl_Rt_grp', u'armShaper_Lt_grp', u'armShaper_Rt_grp', u'armBase_Rt_loc',
        #  u'armBase_Lt_loc', u'clavicle_Lt_a0', u'clavicle_Rt_a0', u'scapulaCtrl_Lt_grp', u'scapulaCtrl_Rt_grp',
        #  u'trapezius_Lt_offsetGrp', u'trapezius_Rt_offsetGrp']
        #
        # mc.parent (to_parent, ctrl_grps[0])

        mc.parent ([u'armRig_Rt_grp', u'armRig_Lt_grp'], jnt_grps[0])
        if mc.objExists ('armRollVector_Rt_jnt_aimConstraint1'):
            mc.setAttr ("armRollVector_Rt_jnt_aimConstraint1.upVectorY" ,-1  )

        # mc.parent (u'armRibbonRig_Rt_grp', u'armRibbonRig_Lt_grp', noxform_grp)

        fkiks=[u'armIKFK_Rt_a0', u'armIKFK_Lt_a0']
        for fkik in fkiks:
            if mc.objExists (fkik):
                mc.setAttr (fkik+'.ty', 175)

        tt=mc.getAttr ('armRollReaderUpObj_Lt_loc.t')
        mc.setAttr ('armRollReaderUpObj_Rt_loc.t', tt[0][0], tt[0][1], tt[0][2]*-1)

        # ctrls=[u'handIk_Lt_a0', u'elbowUpVectorIk_Lt_a0', u'handIk_Rt_a0', u'elbowUpVectorIk_Rt_a0']
        # mc.parent (ctrls, ctrl_grps[0])
        #
        mc.select ('lwrLegTwist_Lt_anim.cv[*]', 'lwrLegTwist_Rt_anim.cv[*]')
        mc.xform (a=1, r=1, ro=(0, 0, -90))
        mc.select (cl=1)
        #
        # mc.delete ('rig_XXX_grp')