# -*- rigBot: assembly -*-
from rigBot import guide
from rigBot.data import controlShapes
import maya.cmds as mc

class EncoreBiped():
	"""Generated assembly build."""

	def __init__(self):
		pass

	def build_guide(self):
		"""Build Assembly guide parts"""

		guide.build("worldRoot", **{'side': u'C', 'name': u''})
		guide.build("encoreHand", **{'createIkCtrls': False, 'parent': u'R_wrist_end_JNT', 'numberFingers': 4, 'createThumb': True, 'pickWalkParent': u'R_arm_IK_CTL', 'numberThumbJoints': 3, 'numberJoints': 4, 'side': u'R', 'name': u''})
		guide.build("encoreFoot", **{'name': u'', 'parent': u'R_leg_end_JNT', 'switchCtrlDriver': u'R_leg_IK_switch_CTL', 'attrCtrlDriver': u'R_leg_IK_CTL', 'ikCtrlParent': u'R_leg_IK_handle_driver_JNT', 'pickWalkParent': u'R_leg_PV_CTL', 'fkCtrlParent': u'R_legEnd_FK_CTL', 'side': u'R'})
		guide.build("encoreBipedLeg", **{'flipJoints': False, 'name': u'', 'parent': u'C_hip_JNT', 'transOrientiation': u'world', 'fkAnkleJoint': u'R_ankle_JNT', 'side': u'R', 'pickWalkParent': u'C_hip_CTL', 'ikHandleParent': u'R_foot_IK_handle_driver_JNT', 'numberTwistJoints': 5, 'makeBendy': True})
		guide.build("encoreBipedArm", **{'name': u'', 'parent': u'C_world_JNT', 'transOrientiation': u'world', 'numberTwistJoints': 5, 'pickWalkParent': u'chest_Mid_bind', 'ikHandleParent': u'', 'side': u'R'})
		guide.build("encoreHand", **{'createIkCtrls': False, 'parent': u'L_wrist_end_JNT', 'numberFingers': 4, 'createThumb': True, 'pickWalkParent': u'L_arm_IK_CTL', 'numberThumbJoints': 3, 'numberJoints': 4, 'side': u'L', 'name': u''})
		guide.build("encoreFoot", **{'name': u'', 'parent': u'L_leg_end_JNT', 'switchCtrlDriver': u'L_leg_IK_switch_CTL', 'attrCtrlDriver': u'L_leg_IK_CTL', 'ikCtrlParent': u'L_leg_IK_handle_driver_JNT', 'pickWalkParent': u'L_leg_PV_CTL', 'fkCtrlParent': u'L_legEnd_FK_CTL', 'side': u'L'})
		guide.build("encoreBipedLeg", **{'flipJoints': False, 'name': u'', 'parent': u'C_hip_JNT', 'transOrientiation': u'world', 'fkAnkleJoint': u'L_ankle_JNT', 'side': u'L', 'pickWalkParent': u'C_hip_CTL', 'ikHandleParent': u'L_foot_IK_handle_driver_JNT', 'numberTwistJoints': 5, 'makeBendy': True})
		guide.build("encoreBipedArm", **{'name': u'', 'parent': u'C_world_JNT', 'transOrientiation': u'world', 'numberTwistJoints': 5, 'pickWalkParent': u'chest_Mid_bind', 'ikHandleParent': u'', 'side': u'L'})
		guide.build("encoreSpine", **{'makeReverseFk': True, 'numberMidCtrls': 1, 'parent': u'C_root_JNT', 'pickWalkParent': u'world_anim', 'numberJoints': 5, 'side': u'C', 'name': u''})
		guide.build("encoreNeck", **{'createSurfaceDriver': False, 'numberMidCtrls': 1, 'parent': u'C_chest_end_JNT', 'pickWalkParent': u'C_chest_CTL', 'createReverseJaw': False, 'name': u'', 'createFKShaperCtrls': False, 'numberJoints': 4, 'side': u'C', 'createJaw': True})

		#Position nodes
		if mc.objExists("R_encoreHand_guide"):
			if not mc.getAttr("R_encoreHand_guide.rotateOrder", l=1):
				mc.setAttr("R_encoreHand_guide.rotateOrder", 0)

			mc.xform("R_encoreHand_guide", a=1, t=[-60.0, 91.8502, 3.944300000000001e-31])
			mc.xform("R_encoreHand_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_encoreHand_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("R_encoreFoot_guide"):
			if not mc.getAttr("R_encoreFoot_guide.rotateOrder", l=1):
				mc.setAttr("R_encoreFoot_guide.rotateOrder", 0)

			mc.xform("R_encoreFoot_guide", a=1, t=[-5.0, 2.77598, 0.0])
			mc.xform("R_encoreFoot_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_encoreFoot_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("R_encoreBipedLeg_guide"):
			if not mc.getAttr("R_encoreBipedLeg_guide.rotateOrder", l=1):
				mc.setAttr("R_encoreBipedLeg_guide.rotateOrder", 0)

			mc.xform("R_encoreBipedLeg_guide", a=1, t=[-5.0, 44.276, 0.0])
			mc.xform("R_encoreBipedLeg_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_encoreBipedLeg_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("R_encoreBipedArm_guide"):
			if not mc.getAttr("R_encoreBipedArm_guide.rotateOrder", l=1):
				mc.setAttr("R_encoreBipedArm_guide.rotateOrder", 0)

			mc.xform("R_encoreBipedArm_guide", a=1, t=[0.0, 91.8502, 0.0])
			mc.xform("R_encoreBipedArm_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_encoreBipedArm_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_encoreHand_guide"):
			if not mc.getAttr("L_encoreHand_guide.rotateOrder", l=1):
				mc.setAttr("L_encoreHand_guide.rotateOrder", 0)

			mc.xform("L_encoreHand_guide", a=1, t=[60.0, 91.85016632080078, 3.94430452610506e-31])
			mc.xform("L_encoreHand_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_encoreHand_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("L_encoreFoot_guide"):
			if not mc.getAttr("L_encoreFoot_guide.rotateOrder", l=1):
				mc.setAttr("L_encoreFoot_guide.rotateOrder", 0)

			mc.xform("L_encoreFoot_guide", a=1, t=[5.0, 2.7759790420532218, 0.0])
			mc.xform("L_encoreFoot_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_encoreFoot_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("L_encoreBipedLeg_guide"):
			if not mc.getAttr("L_encoreBipedLeg_guide.rotateOrder", l=1):
				mc.setAttr("L_encoreBipedLeg_guide.rotateOrder", 0)

			mc.xform("L_encoreBipedLeg_guide", a=1, t=[5.0, 44.27597896362961, 0.0])
			mc.xform("L_encoreBipedLeg_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_encoreBipedLeg_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("L_encoreBipedArm_guide"):
			if not mc.getAttr("L_encoreBipedArm_guide.rotateOrder", l=1):
				mc.setAttr("L_encoreBipedArm_guide.rotateOrder", 0)

			mc.xform("L_encoreBipedArm_guide", a=1, t=[0.0, 91.85016632080078, 0.0])
			mc.xform("L_encoreBipedArm_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_encoreBipedArm_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_worldRoot_guide"):
			if not mc.getAttr("C_worldRoot_guide.rotateOrder", l=1):
				mc.setAttr("C_worldRoot_guide.rotateOrder", 0)

			mc.xform("C_worldRoot_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_encoreSpine_guide"):
			if not mc.getAttr("C_encoreSpine_guide.rotateOrder", l=1):
				mc.setAttr("C_encoreSpine_guide.rotateOrder", 0)

			mc.xform("C_encoreSpine_guide", a=1, t=[0.0, 51.85016601066431, 0.0])
			mc.xform("C_encoreSpine_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_encoreSpine_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("C_encoreNeck_guide"):
			if not mc.getAttr("C_encoreNeck_guide.rotateOrder", l=1):
				mc.setAttr("C_encoreNeck_guide.rotateOrder", 0)

			mc.xform("C_encoreNeck_guide", a=1, t=[0.0, 91.85016632080078, 0.0])
			mc.xform("C_encoreNeck_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_encoreNeck_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("C_root_JNT_PLC"):
			mc.xform("C_root_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_root_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_root_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_JNT_PLC"):
			if not mc.getAttr("L_upLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_JNT_PLC"):
			if not mc.getAttr("L_loLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_end_JNT_PLC"):
			if not mc.getAttr("L_leg_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_leg_end_JNT_PLC.rotateOrder", 0)

			mc.xform("L_leg_end_JNT_PLC", a=1, t=[0.0, -0.2999999843152782, 0.0])
			mc.xform("L_leg_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_handle_driver_JNT_PLC"):
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_A_JNT_PLC", a=1, t=[0.0, -0.6666666666666643, 0.08333333333333333])
			mc.xform("L_upLeg_twist_A_JNT_PLC", a=1, ro=[179.99999999999997, -7.125016348901798, -90.0])
			mc.xform("L_upLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_A_JNT_PLC", a=1, t=[0.0, -4.7166666640525445, 0.41666666666666674])
			mc.xform("L_loLeg_twist_A_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 173.36748536088427, 90.0])
			mc.xform("L_loLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_B_JNT_PLC", a=1, t=[0.0, -1.3333333333333304, 0.16666666666666666])
			mc.xform("L_upLeg_twist_B_JNT_PLC", a=1, ro=[179.99999999999997, -7.125016348901798, -90.0])
			mc.xform("L_upLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_B_JNT_PLC", a=1, t=[0.0, -5.43333332810509, 0.3333333333333334])
			mc.xform("L_loLeg_twist_B_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 173.36748536088427, 90.0])
			mc.xform("L_loLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_C_JNT_PLC", a=1, t=[0.0, -1.9999999999999982, 0.25])
			mc.xform("L_upLeg_twist_C_JNT_PLC", a=1, ro=[179.99999999999997, -7.125016348901798, -90.0])
			mc.xform("L_upLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_C_JNT_PLC", a=1, t=[0.0, -6.149999992157637, 0.25])
			mc.xform("L_loLeg_twist_C_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 173.36748536088427, 90.0])
			mc.xform("L_loLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_D_JNT_PLC", a=1, t=[0.0, -2.6666666666666643, 0.3333333333333333])
			mc.xform("L_upLeg_twist_D_JNT_PLC", a=1, ro=[179.99999999999997, -7.125016348901798, -90.0])
			mc.xform("L_upLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_D_JNT_PLC", a=1, t=[0.0, -6.8666666562101835, 0.1666666666666667])
			mc.xform("L_loLeg_twist_D_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 173.36748536088427, 90.0])
			mc.xform("L_loLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_E_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_E_JNT_PLC", a=1, t=[0.0, -3.3333333333333313, 0.41666666666666663])
			mc.xform("L_upLeg_twist_E_JNT_PLC", a=1, ro=[179.99999999999997, -7.125016348901798, -90.0])
			mc.xform("L_upLeg_twist_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_E_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_E_JNT_PLC", a=1, t=[0.0, -7.58333332026273, 0.08333333333333337])
			mc.xform("L_loLeg_twist_E_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 173.36748536088427, 90.0])
			mc.xform("L_loLeg_twist_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_scapulaAim_JNT_PLC"):
			if not mc.getAttr("L_scapulaAim_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_scapulaAim_JNT_PLC.rotateOrder", 0)

			mc.xform("L_scapulaAim_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaAim_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaAim_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_scapulaCtrl_JNT_PLC"):
			if not mc.getAttr("L_scapulaCtrl_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_scapulaCtrl_JNT_PLC.rotateOrder", 0)

			mc.xform("L_scapulaCtrl_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaCtrl_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaCtrl_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_scapulaEnd_JNT_PLC"):
			if not mc.getAttr("L_scapulaEnd_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_scapulaEnd_JNT_PLC.rotateOrder", 0)

			mc.xform("L_scapulaEnd_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaEnd_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaEnd_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_scapulaTarget_JNT_PLC"):
			if not mc.getAttr("L_scapulaTarget_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_scapulaTarget_JNT_PLC.rotateOrder", 0)

			mc.xform("L_scapulaTarget_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaTarget_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaTarget_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_scapulaChest_JNT_PLC"):
			if not mc.getAttr("L_scapulaChest_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_scapulaChest_JNT_PLC.rotateOrder", 0)

			mc.xform("L_scapulaChest_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaChest_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaChest_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_clavicle_JNT_PLC"):
			if not mc.getAttr("L_clavicle_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_clavicle_JNT_PLC.rotateOrder", 0)

			mc.xform("L_clavicle_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_clavicleEnd_JNT_PLC"):
			if not mc.getAttr("L_clavicleEnd_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_clavicleEnd_JNT_PLC.rotateOrder", 0)

			mc.xform("L_clavicleEnd_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_clavicleEnd_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_clavicleEnd_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_JNT_PLC"):
			if not mc.getAttr("L_shoulder_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_shoulder_JNT_PLC.rotateOrder", 0)

			mc.xform("L_shoulder_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_JNT_PLC"):
			if not mc.getAttr("L_elbow_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_elbow_JNT_PLC.rotateOrder", 0)

			mc.xform("L_elbow_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_JNT_PLC"):
			if not mc.getAttr("L_wrist_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_wrist_JNT_PLC.rotateOrder", 0)

			mc.xform("L_wrist_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_end_JNT_PLC"):
			if not mc.getAttr("L_wrist_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_wrist_end_JNT_PLC.rotateOrder", 0)

			mc.xform("L_wrist_end_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_handIk_handle_driver_JNT_PLC"):
			mc.xform("L_handIk_handle_driver_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_twist_A_JNT_PLC"):
			if not mc.getAttr("L_shoulder_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_shoulder_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_shoulder_twist_A_JNT_PLC", a=1, t=[20.9, 0.0, -0.25])
			mc.xform("L_shoulder_twist_A_JNT_PLC", a=1, ro=[0.0, 15.52411099675426, 0.0])
			mc.xform("L_shoulder_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_twist_A_JNT_PLC"):
			if not mc.getAttr("L_elbow_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_elbow_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_elbow_twist_A_JNT_PLC", a=1, t=[38.85, 0.0, -4.75])
			mc.xform("L_elbow_twist_A_JNT_PLC", a=1, ro=[0.0, -16.389540334034784, 0.0])
			mc.xform("L_elbow_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_twist_B_JNT_PLC"):
			if not mc.getAttr("L_shoulder_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_shoulder_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_shoulder_twist_B_JNT_PLC", a=1, t=[24.5, 0.0, -1.25])
			mc.xform("L_shoulder_twist_B_JNT_PLC", a=1, ro=[0.0, 15.52411099675426, 0.0])
			mc.xform("L_shoulder_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_twist_B_JNT_PLC"):
			if not mc.getAttr("L_elbow_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_elbow_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_elbow_twist_B_JNT_PLC", a=1, t=[42.25, 0.0, -3.75])
			mc.xform("L_elbow_twist_B_JNT_PLC", a=1, ro=[0.0, -16.389540334034784, 0.0])
			mc.xform("L_elbow_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_twist_C_JNT_PLC"):
			if not mc.getAttr("L_shoulder_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_shoulder_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_shoulder_twist_C_JNT_PLC", a=1, t=[29.0, 0.0, -2.5])
			mc.xform("L_shoulder_twist_C_JNT_PLC", a=1, ro=[0.0, 15.52411099675426, 0.0])
			mc.xform("L_shoulder_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_twist_C_JNT_PLC"):
			if not mc.getAttr("L_elbow_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_elbow_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_elbow_twist_C_JNT_PLC", a=1, t=[46.5, 0.0, -2.5])
			mc.xform("L_elbow_twist_C_JNT_PLC", a=1, ro=[0.0, -16.389540334034784, 0.0])
			mc.xform("L_elbow_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_twist_D_JNT_PLC"):
			if not mc.getAttr("L_shoulder_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_shoulder_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_shoulder_twist_D_JNT_PLC", a=1, t=[33.5, 0.0, -3.75])
			mc.xform("L_shoulder_twist_D_JNT_PLC", a=1, ro=[0.0, 15.52411099675426, 0.0])
			mc.xform("L_shoulder_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_twist_D_JNT_PLC"):
			if not mc.getAttr("L_elbow_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_elbow_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_elbow_twist_D_JNT_PLC", a=1, t=[50.75, 0.0, -1.25])
			mc.xform("L_elbow_twist_D_JNT_PLC", a=1, ro=[0.0, -16.389540334034784, 0.0])
			mc.xform("L_elbow_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_twist_E_JNT_PLC"):
			if not mc.getAttr("L_shoulder_twist_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_shoulder_twist_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_shoulder_twist_E_JNT_PLC", a=1, t=[37.1, 0.0, -4.75])
			mc.xform("L_shoulder_twist_E_JNT_PLC", a=1, ro=[0.0, 15.52411099675426, 0.0])
			mc.xform("L_shoulder_twist_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_twist_E_JNT_PLC"):
			if not mc.getAttr("L_elbow_twist_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_elbow_twist_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_elbow_twist_E_JNT_PLC", a=1, t=[54.15, 0.0, -0.25])
			mc.xform("L_elbow_twist_E_JNT_PLC", a=1, ro=[0.0, -16.389540334034784, 0.0])
			mc.xform("L_elbow_twist_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_heel_JNT_PLC"):
			if not mc.getAttr("L_heel_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_heel_JNT_PLC.rotateOrder", 0)

			mc.xform("L_heel_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_heel_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_heel_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_innerBall_JNT_PLC"):
			if not mc.getAttr("L_innerBall_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_innerBall_JNT_PLC.rotateOrder", 0)

			mc.xform("L_innerBall_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_innerBall_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_innerBall_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterBall_JNT_PLC"):
			if not mc.getAttr("L_outterBall_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_outterBall_JNT_PLC.rotateOrder", 0)

			mc.xform("L_outterBall_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterBall_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_outterBall_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_foot_IK_handle_driver_JNT_PLC"):
			mc.xform("L_foot_IK_handle_driver_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_foot_IK_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_foot_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ankle_JNT_PLC"):
			if not mc.getAttr("L_ankle_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ankle_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ankle_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ankle_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ankle_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ball_JNT_PLC"):
			if not mc.getAttr("L_ball_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ball_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ball_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ball_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ball_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_JNT_PLC"):
			if not mc.getAttr("L_toe_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_toe_JNT_PLC.rotateOrder", 0)

			mc.xform("L_toe_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_toe_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spine_B_JNT_PLC"):
			mc.xform("C_spine_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spine_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spine_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spine_C_JNT_PLC"):
			mc.xform("C_spine_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spine_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spine_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spine_D_JNT_PLC"):
			mc.xform("C_spine_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spine_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spine_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_hip_JNT_PLC"):
			if not mc.getAttr("C_hip_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_hip_JNT_PLC.rotateOrder", 0)

			mc.xform("C_hip_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_hip_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_hip_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spine_A_JNT_PLC"):
			if not mc.getAttr("C_spine_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_spine_A_JNT_PLC.rotateOrder", 0)

			mc.xform("C_spine_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spine_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spine_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spineSpline_B_JNT_PLC"):
			if not mc.getAttr("C_spineSpline_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_spineSpline_B_JNT_PLC.rotateOrder", 0)

			mc.xform("C_spineSpline_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spineSpline_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spineSpline_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_end_JNT_PLC"):
			if not mc.getAttr("C_chest_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_chest_end_JNT_PLC.rotateOrder", 0)

			mc.xform("C_chest_end_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_JNT_PLC"):
			if not mc.getAttr("C_chest_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_chest_JNT_PLC.rotateOrder", 0)

			mc.xform("C_chest_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_cog_JNT_PLC"):
			if not mc.getAttr("C_cog_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_cog_JNT_PLC.rotateOrder", 0)

			mc.xform("C_cog_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_cog_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_cog_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_B_JNT_PLC"):
			if not mc.getAttr("L_thumb_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_C_JNT_PLC"):
			if not mc.getAttr("L_thumb_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_D_JNT_PLC"):
			if not mc.getAttr("L_thumb_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_A_JNT_PLC"):
			if not mc.getAttr("L_thumb_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_B_JNT_PLC"):
			if not mc.getAttr("L_index_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_C_JNT_PLC"):
			if not mc.getAttr("L_index_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_D_JNT_PLC"):
			if not mc.getAttr("L_index_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_E_JNT_PLC"):
			if not mc.getAttr("L_index_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_E_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_A_JNT_PLC"):
			if not mc.getAttr("L_index_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_B_JNT_PLC"):
			if not mc.getAttr("L_middle_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_C_JNT_PLC"):
			if not mc.getAttr("L_middle_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_D_JNT_PLC"):
			if not mc.getAttr("L_middle_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_E_JNT_PLC"):
			if not mc.getAttr("L_middle_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_E_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_A_JNT_PLC"):
			if not mc.getAttr("L_middle_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_B_JNT_PLC"):
			if not mc.getAttr("L_ring_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_C_JNT_PLC"):
			if not mc.getAttr("L_ring_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_D_JNT_PLC"):
			if not mc.getAttr("L_ring_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_E_JNT_PLC"):
			if not mc.getAttr("L_ring_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_E_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_A_JNT_PLC"):
			if not mc.getAttr("L_ring_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_B_JNT_PLC"):
			if not mc.getAttr("L_pinky_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_C_JNT_PLC"):
			if not mc.getAttr("L_pinky_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_D_JNT_PLC"):
			if not mc.getAttr("L_pinky_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_E_JNT_PLC"):
			if not mc.getAttr("L_pinky_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_E_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_A_JNT_PLC"):
			if not mc.getAttr("L_pinky_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_B_JNT_PLC"):
			mc.xform("C_neck_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neck_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_C_JNT_PLC"):
			mc.xform("C_neck_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neck_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_A_JNT_PLC"):
			if not mc.getAttr("C_neck_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_neck_A_JNT_PLC.rotateOrder", 0)

			mc.xform("C_neck_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neck_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neckSpline_B_JNT_PLC"):
			if not mc.getAttr("C_neckSpline_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_neckSpline_B_JNT_PLC.rotateOrder", 0)

			mc.xform("C_neckSpline_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neckSpline_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neckSpline_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neckSpline_C_JNT_PLC"):
			if not mc.getAttr("C_neckSpline_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_neckSpline_C_JNT_PLC.rotateOrder", 0)

			mc.xform("C_neckSpline_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neckSpline_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neckSpline_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_end_JNT_PLC"):
			if not mc.getAttr("C_head_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_head_end_JNT_PLC.rotateOrder", 0)

			mc.xform("C_head_end_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_jaw_end_JNT_PLC"):
			if not mc.getAttr("C_jaw_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_jaw_end_JNT_PLC.rotateOrder", 0)

			mc.xform("C_jaw_end_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_jaw_JNT_PLC"):
			if not mc.getAttr("C_jaw_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_jaw_JNT_PLC.rotateOrder", 0)

			mc.xform("C_jaw_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_JNT_PLC"):
			if not mc.getAttr("C_head_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_head_JNT_PLC.rotateOrder", 0)

			mc.xform("C_head_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_top_JNT_PLC"):
			if not mc.getAttr("C_head_top_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_head_top_JNT_PLC.rotateOrder", 0)

			mc.xform("C_head_top_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_top_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_top_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_left_JNT_PLC"):
			if not mc.getAttr("C_head_left_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_head_left_JNT_PLC.rotateOrder", 0)

			mc.xform("C_head_left_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_left_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_left_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_right_JNT_PLC"):
			if not mc.getAttr("C_head_right_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_head_right_JNT_PLC.rotateOrder", 0)

			mc.xform("C_head_right_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_right_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_right_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_scapulaAim_JNT_PLC"):
			if not mc.getAttr("R_scapulaAim_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_scapulaAim_JNT_PLC.rotateOrder", 0)

			mc.xform("R_scapulaAim_JNT_PLC", a=1, t=[-26.0, 0.0, 28.0])
			mc.xform("R_scapulaAim_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_scapulaAim_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_scapulaCtrl_JNT_PLC"):
			if not mc.getAttr("R_scapulaCtrl_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_scapulaCtrl_JNT_PLC.rotateOrder", 0)

			mc.xform("R_scapulaCtrl_JNT_PLC", a=1, t=[-26.0, 0.0, 28.0])
			mc.xform("R_scapulaCtrl_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_scapulaCtrl_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_scapulaEnd_JNT_PLC"):
			if not mc.getAttr("R_scapulaEnd_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_scapulaEnd_JNT_PLC.rotateOrder", 0)

			mc.xform("R_scapulaEnd_JNT_PLC", a=1, t=[-7.0, 0.0, -2.0])
			mc.xform("R_scapulaEnd_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_scapulaEnd_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_scapulaTarget_JNT_PLC"):
			if not mc.getAttr("R_scapulaTarget_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_scapulaTarget_JNT_PLC.rotateOrder", 0)

			mc.xform("R_scapulaTarget_JNT_PLC", a=1, t=[0.0, 0.0, 30.0])
			mc.xform("R_scapulaTarget_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_scapulaTarget_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_scapulaChest_JNT_PLC"):
			if not mc.getAttr("R_scapulaChest_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_scapulaChest_JNT_PLC.rotateOrder", 0)

			mc.xform("R_scapulaChest_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_scapulaChest_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_scapulaChest_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_clavicle_JNT_PLC"):
			if not mc.getAttr("R_clavicle_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_clavicle_JNT_PLC.rotateOrder", 0)

			mc.xform("R_clavicle_JNT_PLC", a=1, t=[-8.5, 0.0, 0.0])
			mc.xform("R_clavicle_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_clavicle_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_clavicleEnd_JNT_PLC"):
			if not mc.getAttr("R_clavicleEnd_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_clavicleEnd_JNT_PLC.rotateOrder", 0)

			mc.xform("R_clavicleEnd_JNT_PLC", a=1, t=[-26.0, 0.0, 6.0])
			mc.xform("R_clavicleEnd_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_clavicleEnd_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_JNT_PLC"):
			if not mc.getAttr("R_shoulder_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_shoulder_JNT_PLC.rotateOrder", 0)

			mc.xform("R_shoulder_JNT_PLC", a=1, t=[-40.0, 0.0, 0.0])
			mc.xform("R_shoulder_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_shoulder_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_JNT_PLC"):
			if not mc.getAttr("R_elbow_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_elbow_JNT_PLC.rotateOrder", 0)

			mc.xform("R_elbow_JNT_PLC", a=1, t=[-76.0, 0.0, 10.0])
			mc.xform("R_elbow_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_JNT_PLC"):
			if not mc.getAttr("R_wrist_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_wrist_JNT_PLC.rotateOrder", 0)

			mc.xform("R_wrist_JNT_PLC", a=1, t=[-110.0, 0.0, 0.0])
			mc.xform("R_wrist_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_wrist_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_end_JNT_PLC"):
			if not mc.getAttr("R_wrist_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_wrist_end_JNT_PLC.rotateOrder", 0)

			mc.xform("R_wrist_end_JNT_PLC", a=1, t=[-120.0, 0.0, 0.0])
			mc.xform("R_wrist_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_wrist_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_handIk_handle_driver_JNT_PLC"):
			mc.xform("R_handIk_handle_driver_JNT_PLC", a=1, t=[0.0, -1.4210854715202004e-14, -3.4416902930940253e-15])
			mc.xform("R_handIk_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_handIk_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_twist_A_JNT_PLC"):
			if not mc.getAttr("R_shoulder_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_shoulder_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_shoulder_twist_A_JNT_PLC", a=1, t=[-20.9, 0.0, 0.25])
			mc.xform("R_shoulder_twist_A_JNT_PLC", a=1, ro=[-2.656766627492179e-16, 15.524110996754251, -1.9490859162596872e-15])
			mc.xform("R_shoulder_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_twist_A_JNT_PLC"):
			if not mc.getAttr("R_elbow_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_elbow_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_elbow_twist_A_JNT_PLC", a=1, t=[-38.85, 0.0, 4.75])
			mc.xform("R_elbow_twist_A_JNT_PLC", a=1, ro=[-2.9719691035292586e-16, -16.389540334034784, 2.063738028980846e-15])
			mc.xform("R_elbow_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_twist_B_JNT_PLC"):
			if not mc.getAttr("R_shoulder_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_shoulder_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_shoulder_twist_B_JNT_PLC", a=1, t=[-24.5, 0.0, 1.25])
			mc.xform("R_shoulder_twist_B_JNT_PLC", a=1, ro=[-2.656766627492179e-16, 15.524110996754251, -1.9490859162596872e-15])
			mc.xform("R_shoulder_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_twist_B_JNT_PLC"):
			if not mc.getAttr("R_elbow_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_elbow_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_elbow_twist_B_JNT_PLC", a=1, t=[-42.25, 0.0, 3.75])
			mc.xform("R_elbow_twist_B_JNT_PLC", a=1, ro=[-2.9719691035292586e-16, -16.389540334034784, 2.063738028980846e-15])
			mc.xform("R_elbow_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_twist_C_JNT_PLC"):
			if not mc.getAttr("R_shoulder_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_shoulder_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_shoulder_twist_C_JNT_PLC", a=1, t=[-29.0, 0.0, 2.5])
			mc.xform("R_shoulder_twist_C_JNT_PLC", a=1, ro=[-2.656766627492179e-16, 15.524110996754251, -1.9490859162596872e-15])
			mc.xform("R_shoulder_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_twist_C_JNT_PLC"):
			if not mc.getAttr("R_elbow_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_elbow_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_elbow_twist_C_JNT_PLC", a=1, t=[-46.5, 0.0, 2.5])
			mc.xform("R_elbow_twist_C_JNT_PLC", a=1, ro=[-2.9719691035292586e-16, -16.389540334034784, 2.063738028980846e-15])
			mc.xform("R_elbow_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_twist_D_JNT_PLC"):
			if not mc.getAttr("R_shoulder_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_shoulder_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_shoulder_twist_D_JNT_PLC", a=1, t=[-33.5, 0.0, 3.75])
			mc.xform("R_shoulder_twist_D_JNT_PLC", a=1, ro=[-2.656766627492179e-16, 15.524110996754251, -1.9490859162596872e-15])
			mc.xform("R_shoulder_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_twist_D_JNT_PLC"):
			if not mc.getAttr("R_elbow_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_elbow_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_elbow_twist_D_JNT_PLC", a=1, t=[-50.75, 0.0, 1.25])
			mc.xform("R_elbow_twist_D_JNT_PLC", a=1, ro=[-2.9719691035292586e-16, -16.389540334034784, 2.063738028980846e-15])
			mc.xform("R_elbow_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_twist_E_JNT_PLC"):
			if not mc.getAttr("R_shoulder_twist_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_shoulder_twist_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_shoulder_twist_E_JNT_PLC", a=1, t=[-37.1, 0.0, 4.75])
			mc.xform("R_shoulder_twist_E_JNT_PLC", a=1, ro=[-2.656766627492179e-16, 15.524110996754251, -1.9490859162596872e-15])
			mc.xform("R_shoulder_twist_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_twist_E_JNT_PLC"):
			if not mc.getAttr("R_elbow_twist_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_elbow_twist_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_elbow_twist_E_JNT_PLC", a=1, t=[-54.15, 0.0, 0.25])
			mc.xform("R_elbow_twist_E_JNT_PLC", a=1, ro=[-2.9719691035292586e-16, -16.389540334034784, 2.063738028980846e-15])
			mc.xform("R_elbow_twist_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_heel_JNT_PLC"):
			if not mc.getAttr("R_heel_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_heel_JNT_PLC.rotateOrder", 0)

			mc.xform("R_heel_JNT_PLC", a=1, t=[0.0, 1.0000002000000003, 0.4999999999999999])
			mc.xform("R_heel_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_heel_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_innerBall_JNT_PLC"):
			if not mc.getAttr("R_innerBall_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_innerBall_JNT_PLC.rotateOrder", 0)

			mc.xform("R_innerBall_JNT_PLC", a=1, t=[1.0, 1.0000002, -2.0])
			mc.xform("R_innerBall_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_innerBall_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_outterBall_JNT_PLC"):
			if not mc.getAttr("R_outterBall_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_outterBall_JNT_PLC.rotateOrder", 0)

			mc.xform("R_outterBall_JNT_PLC", a=1, t=[-1.0, 1.0000002, -2.0])
			mc.xform("R_outterBall_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_outterBall_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_foot_IK_handle_driver_JNT_PLC"):
			mc.xform("R_foot_IK_handle_driver_JNT_PLC", a=1, t=[2.7755575615628914e-17, 1.1102230246251565e-16, 0.0])
			mc.xform("R_foot_IK_handle_driver_JNT_PLC", a=1, ro=[4.134721085902612e-14, 9.167323944393119e-06, 3.307776588110433e-21])
			mc.xform("R_foot_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ankle_JNT_PLC"):
			if not mc.getAttr("R_ankle_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ankle_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ankle_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_ankle_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_ankle_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ball_JNT_PLC"):
			if not mc.getAttr("R_ball_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ball_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ball_JNT_PLC", a=1, t=[2.0, 0.0, 1.0000002])
			mc.xform("R_ball_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_ball_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_JNT_PLC"):
			if not mc.getAttr("R_toe_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_toe_JNT_PLC.rotateOrder", 0)

			mc.xform("R_toe_JNT_PLC", a=1, t=[4.0, 0.0, 1.0000002000000001])
			mc.xform("R_toe_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_toe_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_JNT_PLC"):
			if not mc.getAttr("R_upLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_JNT_PLC"):
			if not mc.getAttr("R_loLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_JNT_PLC", a=1, t=[0.0, 8.000000000000004, -1.0000000000000004])
			mc.xform("R_loLeg_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_loLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_end_JNT_PLC"):
			if not mc.getAttr("R_leg_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_leg_end_JNT_PLC.rotateOrder", 0)

			mc.xform("R_leg_end_JNT_PLC", a=1, t=[0.0, 16.300004, -1.016457333151023e-15])
			mc.xform("R_leg_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_leg_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_handle_driver_JNT_PLC"):
			mc.xform("R_leg_IK_handle_driver_JNT_PLC", a=1, t=[5.551115123125783e-16, 0.0, 1.3877787807814457e-17])
			mc.xform("R_leg_IK_handle_driver_JNT_PLC", a=1, ro=[6.758678718077049e-15, -6.138782743640525e-06, -3.727216138030859e-16])
			mc.xform("R_leg_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_A_JNT_PLC", a=1, t=[0.0, 0.6666800000000013, -0.08333340000000009])
			mc.xform("R_upLeg_twist_A_JNT_PLC", a=1, ro=[180.0, -7.125016348901798, -90.0])
			mc.xform("R_upLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_A_JNT_PLC", a=1, t=[0.0, 4.716680000000002, -0.41666600000000065])
			mc.xform("R_loLeg_twist_A_JNT_PLC", a=1, ro=[0.0, 173.367491499667, 90.0])
			mc.xform("R_loLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_B_JNT_PLC", a=1, t=[0.0, 1.3333400000000015, -0.16666660000000016])
			mc.xform("R_upLeg_twist_B_JNT_PLC", a=1, ro=[180.0, -7.125016348901798, -90.0])
			mc.xform("R_upLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_B_JNT_PLC", a=1, t=[0.0, 5.433340000000001, -0.3333340000000007])
			mc.xform("R_loLeg_twist_B_JNT_PLC", a=1, ro=[0.0, 173.367491499667, 90.0])
			mc.xform("R_loLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_C_JNT_PLC", a=1, t=[0.0, 2.000000000000001, -0.2500000000000003])
			mc.xform("R_upLeg_twist_C_JNT_PLC", a=1, ro=[180.0, -7.125016348901798, -90.0])
			mc.xform("R_upLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_C_JNT_PLC", a=1, t=[0.0, 6.150000000000002, -0.2500000000000008])
			mc.xform("R_loLeg_twist_C_JNT_PLC", a=1, ro=[0.0, 173.367491499667, 90.0])
			mc.xform("R_loLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_D_JNT_PLC", a=1, t=[0.0, 2.6666800000000013, -0.33333400000000035])
			mc.xform("R_upLeg_twist_D_JNT_PLC", a=1, ro=[180.0, -7.125016348901798, -90.0])
			mc.xform("R_upLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_D_JNT_PLC", a=1, t=[0.0, 6.866670000000002, -0.16666660000000083])
			mc.xform("R_loLeg_twist_D_JNT_PLC", a=1, ro=[0.0, 173.367491499667, 90.0])
			mc.xform("R_loLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_E_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_E_JNT_PLC", a=1, t=[0.0, 3.3333400000000015, -0.4166660000000005])
			mc.xform("R_upLeg_twist_E_JNT_PLC", a=1, ro=[180.0, -7.125016348901798, -90.0])
			mc.xform("R_upLeg_twist_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_E_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_E_JNT_PLC", a=1, t=[0.0, 7.583338000000001, -0.08333340000000093])
			mc.xform("R_loLeg_twist_E_JNT_PLC", a=1, ro=[0.0, 173.367491499667, 90.0])
			mc.xform("R_loLeg_twist_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_B_JNT_PLC"):
			if not mc.getAttr("R_thumb_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_B_JNT_PLC", a=1, t=[4.230014813089156e-06, -1.4483407397847259e-06, -8.361999199735237e-07])
			mc.xform("R_thumb_B_JNT_PLC", a=1, ro=[2.7034714792439888e-14, 3.1805546814635176e-15, -4.7708320221952736e-15])
			mc.xform("R_thumb_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_C_JNT_PLC"):
			if not mc.getAttr("R_thumb_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_C_JNT_PLC", a=1, t=[-6.502163465427202e-07, -3.415584908239566e-07, -1.9719889365887866e-07])
			mc.xform("R_thumb_C_JNT_PLC", a=1, ro=[2.7034714792439888e-14, 3.1805546814635176e-15, -4.7708320221952736e-15])
			mc.xform("R_thumb_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_D_JNT_PLC"):
			if not mc.getAttr("R_thumb_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_D_JNT_PLC", a=1, t=[4.679814598063103e-06, -2.3399072990315517e-06, -1.3509461140870371e-06])
			mc.xform("R_thumb_D_JNT_PLC", a=1, ro=[2.7034714792439888e-14, 3.1805546814635176e-15, -4.7708320221952736e-15])
			mc.xform("R_thumb_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_A_JNT_PLC"):
			if not mc.getAttr("R_thumb_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_A_JNT_PLC", a=1, t=[0.933012701892217, 0.5334936490538906, -0.30801270189221697])
			mc.xform("R_thumb_A_JNT_PLC", a=1, ro=[2.6637145457256954e-14, 2.3854160110976368e-15, -180.0])
			mc.xform("R_thumb_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_B_JNT_PLC"):
			if not mc.getAttr("R_index_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_B_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, 0.0])
			mc.xform("R_index_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_index_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_C_JNT_PLC"):
			if not mc.getAttr("R_index_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_C_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, -2.7755575615628914e-17])
			mc.xform("R_index_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_index_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_D_JNT_PLC"):
			if not mc.getAttr("R_index_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_D_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, 0.0])
			mc.xform("R_index_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_index_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_E_JNT_PLC"):
			if not mc.getAttr("R_index_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_E_JNT_PLC", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, 0.0])
			mc.xform("R_index_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_index_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_A_JNT_PLC"):
			if not mc.getAttr("R_index_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_A_JNT_PLC", a=1, t=[0.5, 0.0, -0.5])
			mc.xform("R_index_A_JNT_PLC", a=1, ro=[7.016709298534876e-15, -7.016709298534876e-15, 180.0])
			mc.xform("R_index_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_B_JNT_PLC"):
			if not mc.getAttr("R_middle_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_B_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, 6.1232339957366785e-18])
			mc.xform("R_middle_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_middle_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_C_JNT_PLC"):
			if not mc.getAttr("R_middle_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_C_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, 9.797174393178607e-18])
			mc.xform("R_middle_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_middle_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_D_JNT_PLC"):
			if not mc.getAttr("R_middle_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_D_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, 6.1232339957366785e-18])
			mc.xform("R_middle_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_middle_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_E_JNT_PLC"):
			if not mc.getAttr("R_middle_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_E_JNT_PLC", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, 0.0])
			mc.xform("R_middle_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_middle_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_A_JNT_PLC"):
			if not mc.getAttr("R_middle_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_A_JNT_PLC", a=1, t=[0.5, 0.0, 0.0])
			mc.xform("R_middle_A_JNT_PLC", a=1, ro=[7.016709298534876e-15, -7.016709298534876e-15, 180.0])
			mc.xform("R_middle_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_B_JNT_PLC"):
			if not mc.getAttr("R_ring_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_B_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, 0.0])
			mc.xform("R_ring_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_ring_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_C_JNT_PLC"):
			if not mc.getAttr("R_ring_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_C_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, 0.0])
			mc.xform("R_ring_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_ring_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_D_JNT_PLC"):
			if not mc.getAttr("R_ring_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_D_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, 0.0])
			mc.xform("R_ring_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_ring_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_E_JNT_PLC"):
			if not mc.getAttr("R_ring_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_E_JNT_PLC", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, 0.0])
			mc.xform("R_ring_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_ring_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_A_JNT_PLC"):
			if not mc.getAttr("R_ring_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_A_JNT_PLC", a=1, t=[0.5, 0.0, 0.5])
			mc.xform("R_ring_A_JNT_PLC", a=1, ro=[7.016709298534876e-15, -7.016709298534876e-15, 180.0])
			mc.xform("R_ring_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_B_JNT_PLC"):
			if not mc.getAttr("R_pinky_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_B_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, -1.1102230246251565e-16])
			mc.xform("R_pinky_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_C_JNT_PLC"):
			if not mc.getAttr("R_pinky_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_C_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, -1.1102230246251565e-16])
			mc.xform("R_pinky_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_D_JNT_PLC"):
			if not mc.getAttr("R_pinky_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_D_JNT_PLC", a=1, t=[1.7763568394002505e-15, 0.0, -1.1102230246251565e-16])
			mc.xform("R_pinky_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_E_JNT_PLC"):
			if not mc.getAttr("R_pinky_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_E_JNT_PLC", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, -1.1102230246251565e-16])
			mc.xform("R_pinky_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_A_JNT_PLC"):
			if not mc.getAttr("R_pinky_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_A_JNT_PLC", a=1, t=[0.5, 0.0, 1.0])
			mc.xform("R_pinky_A_JNT_PLC", a=1, ro=[7.016709298534876e-15, -7.016709298534876e-15, 180.0])
			mc.xform("R_pinky_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_world_PIV_CTL"):
			mc.xform("C_world_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_world_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_world_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_visibility_PIV_CTL"):
			mc.xform("C_visibility_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_visibility_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_visibility_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_01_PIV_CTL"):
			if not mc.getAttr("L_upLeg_shaper_01_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_01_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_01_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_01_PIV_CTL"):
			if not mc.getAttr("L_loLeg_shaper_01_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_01_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_01_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_02_PIV_CTL"):
			if not mc.getAttr("L_upLeg_shaper_02_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_02_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_02_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_02_PIV_CTL"):
			if not mc.getAttr("L_loLeg_shaper_02_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_02_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_02_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_03_PIV_CTL"):
			if not mc.getAttr("L_upLeg_shaper_03_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_03_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_03_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_03_PIV_CTL"):
			if not mc.getAttr("L_loLeg_shaper_03_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_03_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_03_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_04_PIV_CTL"):
			if not mc.getAttr("L_upLeg_shaper_04_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_04_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_04_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_04_PIV_CTL"):
			if not mc.getAttr("L_loLeg_shaper_04_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_04_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_04_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_05_PIV_CTL"):
			if not mc.getAttr("L_upLeg_shaper_05_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_05_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_05_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_05_PIV_CTL"):
			if not mc.getAttr("L_loLeg_shaper_05_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_05_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_05_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_FK_PIV_CTL"):
			if not mc.getAttr("L_upLeg_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_FK_PIV_CTL"):
			if not mc.getAttr("L_loLeg_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_legEnd_FK_PIV_CTL"):
			if not mc.getAttr("L_legEnd_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_legEnd_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("L_legEnd_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legEnd_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legEnd_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_PIV_CTL"):
			mc.xform("L_leg_IK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_PV_PIV_CTL"):
			mc.xform("L_leg_PV_PIV_CTL", a=1, t=[0.0, 0.0, -10.0])
			mc.xform("L_leg_PV_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_PV_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_legBase_PIV_CTL"):
			if not mc.getAttr("L_legBase_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_legBase_PIV_CTL.rotateOrder", 0)

			mc.xform("L_legBase_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_switch_PIV_CTL"):
			if not mc.getAttr("L_leg_IK_switch_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_IK_switch_PIV_CTL.rotateOrder", 0)

			mc.xform("L_leg_IK_switch_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_A_PIV_CTL"):
			if not mc.getAttr("L_bendyLeg_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_B_PIV_CTL"):
			if not mc.getAttr("L_bendyLeg_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_C_PIV_CTL"):
			if not mc.getAttr("L_bendyLeg_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_01_PIV_CTL"):
			if not mc.getAttr("L_shoulder_shaper_01_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_01_PIV_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_01_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_01_PIV_CTL"):
			if not mc.getAttr("L_elbow_shaper_01_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_01_PIV_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_01_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_02_PIV_CTL"):
			if not mc.getAttr("L_shoulder_shaper_02_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_02_PIV_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_02_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_02_PIV_CTL"):
			if not mc.getAttr("L_elbow_shaper_02_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_02_PIV_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_02_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_03_PIV_CTL"):
			if not mc.getAttr("L_shoulder_shaper_03_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_03_PIV_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_03_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_03_PIV_CTL"):
			if not mc.getAttr("L_elbow_shaper_03_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_03_PIV_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_03_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_04_PIV_CTL"):
			if not mc.getAttr("L_shoulder_shaper_04_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_04_PIV_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_04_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_04_PIV_CTL"):
			if not mc.getAttr("L_elbow_shaper_04_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_04_PIV_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_04_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_05_PIV_CTL"):
			if not mc.getAttr("L_shoulder_shaper_05_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_05_PIV_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_05_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_05_PIV_CTL"):
			if not mc.getAttr("L_elbow_shaper_05_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_05_PIV_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_05_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_scapulaCtrl_PIV_CTL"):
			if not mc.getAttr("L_scapulaCtrl_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_scapulaCtrl_PIV_CTL.rotateOrder", 0)

			mc.xform("L_scapulaCtrl_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaCtrl_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaCtrl_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_scapulaTarget_PIV_CTL"):
			if not mc.getAttr("L_scapulaTarget_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_scapulaTarget_PIV_CTL.rotateOrder", 0)

			mc.xform("L_scapulaTarget_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaTarget_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaTarget_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_scapulaChest_PIV_CTL"):
			if not mc.getAttr("L_scapulaChest_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_scapulaChest_PIV_CTL.rotateOrder", 0)

			mc.xform("L_scapulaChest_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaChest_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaChest_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulderFk_PIV_CTL"):
			if not mc.getAttr("L_shoulderFk_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulderFk_PIV_CTL.rotateOrder", 0)

			mc.xform("L_shoulderFk_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulderFk_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulderFk_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbowFk_PIV_CTL"):
			if not mc.getAttr("L_elbowFk_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbowFk_PIV_CTL.rotateOrder", 0)

			mc.xform("L_elbowFk_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbowFk_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbowFk_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wristFk_PIV_CTL"):
			if not mc.getAttr("L_wristFk_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_wristFk_PIV_CTL.rotateOrder", 0)

			mc.xform("L_wristFk_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wristFk_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wristFk_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_handIk_PIV_CTL"):
			if not mc.getAttr("L_handIk_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_handIk_PIV_CTL.rotateOrder", 0)

			mc.xform("L_handIk_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmTwist_PIV_CTL"):
			if not mc.getAttr("L_lwrArmTwist_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmTwist_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmTwist_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbowUpVectorIk_PIV_CTL"):
			mc.xform("L_elbowUpVectorIk_PIV_CTL", a=1, t=[0.0, 0.0, -20.0])
			mc.xform("L_elbowUpVectorIk_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbowUpVectorIk_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_clavicle_PIV_CTL"):
			if not mc.getAttr("L_clavicle_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_clavicle_PIV_CTL.rotateOrder", 0)

			mc.xform("L_clavicle_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_uprArmRibbonMid_PIV_CTL"):
			if not mc.getAttr("L_uprArmRibbonMid_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_uprArmRibbonMid_PIV_CTL.rotateOrder", 0)

			mc.xform("L_uprArmRibbonMid_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbowRibbon_PIV_CTL"):
			if not mc.getAttr("L_elbowRibbon_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbowRibbon_PIV_CTL.rotateOrder", 0)

			mc.xform("L_elbowRibbon_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmRibbonMid_PIV_CTL"):
			if not mc.getAttr("L_lwrArmRibbonMid_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmRibbonMid_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmRibbonMid_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_switch_PIV_CTL"):
			if not mc.getAttr("L_arm_IK_switch_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_switch_PIV_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_switch_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_innerBall_PIV_CTL"):
			mc.xform("L_innerBall_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_innerBall_PIV_CTL", a=1, ro=[0.0, -1.2722218725854067e-14, 0.0])
			mc.xform("L_innerBall_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterBall_PIV_CTL"):
			mc.xform("L_outterBall_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterBall_PIV_CTL", a=1, ro=[0.0, -1.2722218725854067e-14, 0.0])
			mc.xform("L_outterBall_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_heel_PIV_CTL"):
			mc.xform("L_heel_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_heel_PIV_CTL", a=1, ro=[0.0, -1.2722218725854067e-14, 0.0])
			mc.xform("L_heel_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toeTip_PIV_CTL"):
			mc.xform("L_toeTip_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_toeTip_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toeTip_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_reverseBall_PIV_CTL"):
			mc.xform("L_reverseBall_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_reverseBall_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_reverseBall_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ankleOffset_PIV_CTL"):
			mc.xform("L_ankleOffset_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ankleOffset_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ankleOffset_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_IK_PIV_CTL"):
			mc.xform("L_toe_IK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_FK_PIV_CTL"):
			if not mc.getAttr("L_toe_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_toe_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("L_toe_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_toe_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_cog_PIV_CTL"):
			if not mc.getAttr("C_cog_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_cog_PIV_CTL.rotateOrder", 0)

			mc.xform("C_cog_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_cog_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_cog_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_PIV_CTL"):
			if not mc.getAttr("C_chest_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_chest_PIV_CTL.rotateOrder", 0)

			mc.xform("C_chest_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_hip_PIV_CTL"):
			if not mc.getAttr("C_hip_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_hip_PIV_CTL.rotateOrder", 0)

			mc.xform("C_hip_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_hip_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_hip_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spine_FK_0_PIV_CTL"):
			mc.xform("C_spine_FK_0_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_0_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_0_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spine_FK_chest_PIV_CTL"):
			mc.xform("C_spine_FK_chest_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_chest_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_chest_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_revSpine_chest_PIV_CTL"):
			mc.xform("C_revSpine_chest_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_chest_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_chest_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_revSpine_0_PIV_CTL"):
			mc.xform("C_revSpine_0_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_0_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_0_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midSpine_PIV_CTL"):
			if not mc.getAttr("C_midSpine_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_midSpine_PIV_CTL.rotateOrder", 0)

			mc.xform("C_midSpine_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spine_FK_1_PIV_CTL"):
			mc.xform("C_spine_FK_1_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_1_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_1_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_revSpine_1_PIV_CTL"):
			mc.xform("C_revSpine_1_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_1_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_1_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spineShaper_1_PIV_CTL"):
			mc.xform("C_spineShaper_1_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_1_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_1_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spineShaper_2_PIV_CTL"):
			mc.xform("C_spineShaper_2_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_2_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_2_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spineShaper_3_PIV_CTL"):
			mc.xform("C_spineShaper_3_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_3_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_3_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spineShaper_4_PIV_CTL"):
			mc.xform("C_spineShaper_4_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_4_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_4_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spineShaper_5_PIV_CTL"):
			mc.xform("C_spineShaper_5_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_5_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_5_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_FK_PIV_CTL"):
			mc.xform("C_chest_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_A_PIV_CTL"):
			if not mc.getAttr("L_thumb_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_thumb_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_thumb_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_B_PIV_CTL"):
			if not mc.getAttr("L_thumb_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_thumb_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_thumb_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_C_PIV_CTL"):
			if not mc.getAttr("L_thumb_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_thumb_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_thumb_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_A_PIV_CTL"):
			if not mc.getAttr("L_index_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_index_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_B_PIV_CTL"):
			if not mc.getAttr("L_index_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_index_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_C_PIV_CTL"):
			if not mc.getAttr("L_index_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_index_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_D_PIV_CTL"):
			if not mc.getAttr("L_index_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_D_PIV_CTL.rotateOrder", 0)

			mc.xform("L_index_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_A_PIV_CTL"):
			if not mc.getAttr("L_middle_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_middle_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_B_PIV_CTL"):
			if not mc.getAttr("L_middle_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_middle_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_C_PIV_CTL"):
			if not mc.getAttr("L_middle_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_middle_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_D_PIV_CTL"):
			if not mc.getAttr("L_middle_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_D_PIV_CTL.rotateOrder", 0)

			mc.xform("L_middle_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_A_PIV_CTL"):
			if not mc.getAttr("L_ring_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_ring_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_B_PIV_CTL"):
			if not mc.getAttr("L_ring_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_ring_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_C_PIV_CTL"):
			if not mc.getAttr("L_ring_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_ring_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_D_PIV_CTL"):
			if not mc.getAttr("L_ring_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_D_PIV_CTL.rotateOrder", 0)

			mc.xform("L_ring_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_A_PIV_CTL"):
			if not mc.getAttr("L_pinky_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_pinky_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_B_PIV_CTL"):
			if not mc.getAttr("L_pinky_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_pinky_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_C_PIV_CTL"):
			if not mc.getAttr("L_pinky_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_pinky_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_D_PIV_CTL"):
			if not mc.getAttr("L_pinky_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_D_PIV_CTL.rotateOrder", 0)

			mc.xform("L_pinky_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_hand_PIV_CTL"):
			mc.xform("L_hand_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_hand_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_hand_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_PIV_CTL"):
			if not mc.getAttr("C_head_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_head_PIV_CTL.rotateOrder", 0)

			mc.xform("C_head_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_PIV_CTL", a=1, ro=[-90.0, 0.0, 0.0])
			mc.xform("C_head_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neckBase_PIV_CTL"):
			if not mc.getAttr("C_neckBase_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_neckBase_PIV_CTL.rotateOrder", 0)

			mc.xform("C_neckBase_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midNeck_PIV_CTL"):
			if not mc.getAttr("C_midNeck_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_midNeck_PIV_CTL.rotateOrder", 0)

			mc.xform("C_midNeck_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_FK_A_PIV_CTL"):
			mc.xform("C_neck_FK_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_FK_B_PIV_CTL"):
			mc.xform("C_neck_FK_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_FK_C_PIV_CTL"):
			mc.xform("C_neck_FK_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_FK_D_PIV_CTL"):
			mc.xform("C_neck_FK_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_jaw_PIV_CTL"):
			if not mc.getAttr("C_jaw_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_jaw_PIV_CTL.rotateOrder", 0)

			mc.xform("C_jaw_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_FK_PIV_CTL"):
			mc.xform("C_head_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_top_PIV_CTL"):
			mc.xform("C_head_top_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_top_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_top_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_left_PIV_CTL"):
			mc.xform("C_head_left_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_left_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_left_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_right_PIV_CTL"):
			mc.xform("C_head_right_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_right_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_right_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_01_PIV_CTL"):
			if not mc.getAttr("R_shoulder_shaper_01_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_01_PIV_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_01_PIV_CTL", a=1, t=[-7.105427357601002e-15, 3.367919924812668e-05, -1.7763568394002505e-15])
			mc.xform("R_shoulder_shaper_01_PIV_CTL", a=1, ro=[1.5911397784793446e-14, 3.1805546814635156e-15, -180.0])
			mc.xform("R_shoulder_shaper_01_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0000000000000002])

		if mc.objExists("R_elbow_shaper_01_PIV_CTL"):
			if not mc.getAttr("R_elbow_shaper_01_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_01_PIV_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_01_PIV_CTL", a=1, t=[-1.4210854715202004e-14, 3.367919924812668e-05, 0.0])
			mc.xform("R_elbow_shaper_01_PIV_CTL", a=1, ro=[1.6013297666354668e-14, 9.406882732685294e-31, 180.0])
			mc.xform("R_elbow_shaper_01_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_shoulder_shaper_02_PIV_CTL"):
			if not mc.getAttr("R_shoulder_shaper_02_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_02_PIV_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_02_PIV_CTL", a=1, t=[0.0, 3.367919924812668e-05, 0.0])
			mc.xform("R_shoulder_shaper_02_PIV_CTL", a=1, ro=[1.5911397784793446e-14, 3.1805546814635156e-15, -180.0])
			mc.xform("R_shoulder_shaper_02_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0000000000000002])

		if mc.objExists("R_elbow_shaper_02_PIV_CTL"):
			if not mc.getAttr("R_elbow_shaper_02_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_02_PIV_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_02_PIV_CTL", a=1, t=[-1.4210854715202004e-14, 3.367919924812668e-05, 0.0])
			mc.xform("R_elbow_shaper_02_PIV_CTL", a=1, ro=[1.6013297666354668e-14, 9.406882732685294e-31, 180.0])
			mc.xform("R_elbow_shaper_02_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_shoulder_shaper_03_PIV_CTL"):
			if not mc.getAttr("R_shoulder_shaper_03_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_03_PIV_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_03_PIV_CTL", a=1, t=[7.105427357601002e-15, 3.367919924812668e-05, -8.881784197001252e-16])
			mc.xform("R_shoulder_shaper_03_PIV_CTL", a=1, ro=[1.5911397784793446e-14, 3.1805546814635156e-15, -180.0])
			mc.xform("R_shoulder_shaper_03_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0000000000000002])

		if mc.objExists("R_elbow_shaper_03_PIV_CTL"):
			if not mc.getAttr("R_elbow_shaper_03_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_03_PIV_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_03_PIV_CTL", a=1, t=[-1.4210854715202004e-14, 3.367919924812668e-05, -1.7763568394002505e-15])
			mc.xform("R_elbow_shaper_03_PIV_CTL", a=1, ro=[1.6013297666354668e-14, 9.406882732685294e-31, 180.0])
			mc.xform("R_elbow_shaper_03_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_shoulder_shaper_04_PIV_CTL"):
			if not mc.getAttr("R_shoulder_shaper_04_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_04_PIV_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_04_PIV_CTL", a=1, t=[0.0, 3.367919924812668e-05, 8.881784197001252e-16])
			mc.xform("R_shoulder_shaper_04_PIV_CTL", a=1, ro=[1.5911397784793446e-14, 3.1805546814635156e-15, -180.0])
			mc.xform("R_shoulder_shaper_04_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0000000000000002])

		if mc.objExists("R_elbow_shaper_04_PIV_CTL"):
			if not mc.getAttr("R_elbow_shaper_04_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_04_PIV_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_04_PIV_CTL", a=1, t=[0.0, 3.367919924812668e-05, -3.552713678800501e-15])
			mc.xform("R_elbow_shaper_04_PIV_CTL", a=1, ro=[1.6013297666354668e-14, 9.406882732685294e-31, 180.0])
			mc.xform("R_elbow_shaper_04_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_shoulder_shaper_05_PIV_CTL"):
			if not mc.getAttr("R_shoulder_shaper_05_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_05_PIV_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_05_PIV_CTL", a=1, t=[0.0, 3.367919924812668e-05, -3.552713678800501e-15])
			mc.xform("R_shoulder_shaper_05_PIV_CTL", a=1, ro=[1.5911397784793446e-14, 3.1805546814635156e-15, -180.0])
			mc.xform("R_shoulder_shaper_05_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0000000000000002])

		if mc.objExists("R_elbow_shaper_05_PIV_CTL"):
			if not mc.getAttr("R_elbow_shaper_05_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_05_PIV_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_05_PIV_CTL", a=1, t=[0.0, 3.367919924812668e-05, -3.552713678800501e-15])
			mc.xform("R_elbow_shaper_05_PIV_CTL", a=1, ro=[1.6013297666354668e-14, 9.406882732685294e-31, 180.0])
			mc.xform("R_elbow_shaper_05_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_scapulaCtrl_PIV_CTL"):
			if not mc.getAttr("R_scapulaCtrl_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_scapulaCtrl_PIV_CTL.rotateOrder", 0)

			mc.xform("R_scapulaCtrl_PIV_CTL", a=1, t=[0.0, 3.367919921970497e-05, 0.0])
			mc.xform("R_scapulaCtrl_PIV_CTL", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_scapulaCtrl_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_scapulaTarget_PIV_CTL"):
			if not mc.getAttr("R_scapulaTarget_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_scapulaTarget_PIV_CTL.rotateOrder", 0)

			mc.xform("R_scapulaTarget_PIV_CTL", a=1, t=[0.0, -3.367919921970497e-05, 0.0])
			mc.xform("R_scapulaTarget_PIV_CTL", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_scapulaTarget_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_scapulaChest_PIV_CTL"):
			if not mc.getAttr("R_scapulaChest_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_scapulaChest_PIV_CTL.rotateOrder", 0)

			mc.xform("R_scapulaChest_PIV_CTL", a=1, t=[0.0, -3.367919921970497e-05, 0.0])
			mc.xform("R_scapulaChest_PIV_CTL", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_scapulaChest_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_shoulderFk_PIV_CTL"):
			if not mc.getAttr("R_shoulderFk_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulderFk_PIV_CTL.rotateOrder", 0)

			mc.xform("R_shoulderFk_PIV_CTL", a=1, t=[-3.552713678800501e-15, 3.3679199262337534e-05, -8.881784197001252e-16])
			mc.xform("R_shoulderFk_PIV_CTL", a=1, ro=[1.591139778479345e-14, 3.1805546814635156e-15, -180.0])
			mc.xform("R_shoulderFk_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0000000000000002])

		if mc.objExists("R_elbowFk_PIV_CTL"):
			if not mc.getAttr("R_elbowFk_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbowFk_PIV_CTL.rotateOrder", 0)

			mc.xform("R_elbowFk_PIV_CTL", a=1, t=[7.105427357601002e-15, 3.367919921970497e-05, -3.552713678800501e-15])
			mc.xform("R_elbowFk_PIV_CTL", a=1, ro=[1.601329766635467e-14, 9.406882732685297e-31, 180.0])
			mc.xform("R_elbowFk_PIV_CTL", r=1, s=[0.9999999999999999, 1.0, -0.9999999999999999])

		if mc.objExists("R_wristFk_PIV_CTL"):
			if not mc.getAttr("R_wristFk_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_wristFk_PIV_CTL.rotateOrder", 0)

			mc.xform("R_wristFk_PIV_CTL", a=1, t=[-7.105427357601002e-15, 3.367919921970497e-05, -3.4416955008503415e-15])
			mc.xform("R_wristFk_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_wristFk_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_handIk_PIV_CTL"):
			if not mc.getAttr("R_handIk_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_handIk_PIV_CTL.rotateOrder", 0)

			mc.xform("R_handIk_PIV_CTL", a=1, t=[-7.105427357601002e-15, 3.367919921970497e-05, -3.4416955008503415e-15])
			mc.xform("R_handIk_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_handIk_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_lwrArmTwist_PIV_CTL"):
			if not mc.getAttr("R_lwrArmTwist_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmTwist_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmTwist_PIV_CTL", a=1, t=[-7.105427357601002e-15, 3.367919921970497e-05, -3.4416955008503415e-15])
			mc.xform("R_lwrArmTwist_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_lwrArmTwist_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_elbowUpVectorIk_PIV_CTL"):
			mc.xform("R_elbowUpVectorIk_PIV_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 20.0])
			mc.xform("R_elbowUpVectorIk_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_elbowUpVectorIk_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_clavicle_PIV_CTL"):
			if not mc.getAttr("R_clavicle_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_clavicle_PIV_CTL.rotateOrder", 0)

			mc.xform("R_clavicle_PIV_CTL", a=1, t=[0.0, 3.367919921970497e-05, 0.0])
			mc.xform("R_clavicle_PIV_CTL", a=1, ro=[1.6309108099297284e-14, 3.1805546814635156e-15, -180.0])
			mc.xform("R_clavicle_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0000000000000002])

		if mc.objExists("R_uprArmRibbonMid_PIV_CTL"):
			if not mc.getAttr("R_uprArmRibbonMid_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_uprArmRibbonMid_PIV_CTL.rotateOrder", 0)

			mc.xform("R_uprArmRibbonMid_PIV_CTL", a=1, t=[3.552713678800501e-15, 3.3679199233915824e-05, 0.0])
			mc.xform("R_uprArmRibbonMid_PIV_CTL", a=1, ro=[1.591139778479345e-14, 3.1805546814635156e-15, -180.0])
			mc.xform("R_uprArmRibbonMid_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0000000000000002])

		if mc.objExists("R_elbowRibbon_PIV_CTL"):
			if not mc.getAttr("R_elbowRibbon_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbowRibbon_PIV_CTL.rotateOrder", 0)

			mc.xform("R_elbowRibbon_PIV_CTL", a=1, t=[7.105427357601002e-15, 3.367919919128326e-05, -8.881784197001252e-16])
			mc.xform("R_elbowRibbon_PIV_CTL", a=1, ro=[1.4086410356705834e-14, 8.625192693270288e-31, 180.0])
			mc.xform("R_elbowRibbon_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_lwrArmRibbonMid_PIV_CTL"):
			if not mc.getAttr("R_lwrArmRibbonMid_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmRibbonMid_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmRibbonMid_PIV_CTL", a=1, t=[7.105427357601002e-15, 3.3679199233915824e-05, -5.329070518200751e-15])
			mc.xform("R_lwrArmRibbonMid_PIV_CTL", a=1, ro=[1.601329766635467e-14, 9.406882732685297e-31, 180.0])
			mc.xform("R_lwrArmRibbonMid_PIV_CTL", r=1, s=[0.9999999999999999, 1.0, -0.9999999999999999])

		if mc.objExists("R_arm_IK_switch_PIV_CTL"):
			if not mc.getAttr("R_arm_IK_switch_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_PIV_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_PIV_CTL", a=1, t=[-7.105427357601002e-15, 3.367919921970497e-05, -3.4416955008503415e-15])
			mc.xform("R_arm_IK_switch_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_arm_IK_switch_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_innerBall_PIV_CTL"):
			mc.xform("R_innerBall_PIV_CTL", a=1, t=[0.0, 1.734723475976807e-16, 0.0])
			mc.xform("R_innerBall_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_innerBall_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_outterBall_PIV_CTL"):
			mc.xform("R_outterBall_PIV_CTL", a=1, t=[0.0, 1.734723475976807e-16, 0.0])
			mc.xform("R_outterBall_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_outterBall_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_heel_PIV_CTL"):
			mc.xform("R_heel_PIV_CTL", a=1, t=[0.0, -3.5388358909926865e-16, 2.7755575615628914e-17])
			mc.xform("R_heel_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_heel_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_toeTip_PIV_CTL"):
			mc.xform("R_toeTip_PIV_CTL", a=1, t=[0.0, -4.371503159461554e-16, 0.0])
			mc.xform("R_toeTip_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_toeTip_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_reverseBall_PIV_CTL"):
			mc.xform("R_reverseBall_PIV_CTL", a=1, t=[2.220446049250313e-16, 1.734723475976807e-16, -1.1102230246251565e-16])
			mc.xform("R_reverseBall_PIV_CTL", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_reverseBall_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_ankleOffset_PIV_CTL"):
			mc.xform("R_ankleOffset_PIV_CTL", a=1, t=[0.0, -1.1102230246251565e-16, -1.3234889800848443e-23])
			mc.xform("R_ankleOffset_PIV_CTL", a=1, ro=[9.167323953934774e-06, 180.0, 0.0])
			mc.xform("R_ankleOffset_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_toe_IK_PIV_CTL"):
			mc.xform("R_toe_IK_PIV_CTL", a=1, t=[2.220446049250313e-16, 1.1102230246251565e-16, -1.8041124150158794e-16])
			mc.xform("R_toe_IK_PIV_CTL", a=1, ro=[1.1476156374930413e-30, 3.1805546814635168e-15, -179.99999999999997])
			mc.xform("R_toe_IK_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_toe_FK_PIV_CTL"):
			if not mc.getAttr("R_toe_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_toe_FK_PIV_CTL", a=1, t=[2.220446049250313e-16, 1.1102230246251565e-16, 8.410644090905972e-09])
			mc.xform("R_toe_FK_PIV_CTL", a=1, ro=[1.1476156374930413e-30, 3.1805546814635168e-15, -179.99999999999997])
			mc.xform("R_toe_FK_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_upLeg_shaper_01_PIV_CTL"):
			if not mc.getAttr("R_upLeg_shaper_01_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_01_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_01_PIV_CTL", a=1, t=[9.063855687330147e-06, -3.3306690738754696e-16, 1.065796480181902e-06])
			mc.xform("R_upLeg_shaper_01_PIV_CTL", a=1, ro=[0.0, 0.0, 180.0])
			mc.xform("R_upLeg_shaper_01_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999998, -0.9999999999999999])

		if mc.objExists("R_loLeg_shaper_01_PIV_CTL"):
			if not mc.getAttr("R_loLeg_shaper_01_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_01_PIV_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_01_PIV_CTL", a=1, t=[9.144579254716234e-06, 0.0, -3.921637134196576e-07])
			mc.xform("R_loLeg_shaper_01_PIV_CTL", a=1, ro=[1.1927073240070309e-15, 6.138782731315875e-06, 180.0])
			mc.xform("R_loLeg_shaper_01_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_upLeg_shaper_02_PIV_CTL"):
			if not mc.getAttr("R_upLeg_shaper_02_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_02_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_02_PIV_CTL", a=1, t=[2.43213188078073e-06, -3.3306690738754696e-16, 3.7120196649809145e-07])
			mc.xform("R_upLeg_shaper_02_PIV_CTL", a=1, ro=[0.0, 0.0, 180.0])
			mc.xform("R_upLeg_shaper_02_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999998, -0.9999999999999999])

		if mc.objExists("R_loLeg_shaper_02_PIV_CTL"):
			if not mc.getAttr("R_loLeg_shaper_02_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_02_PIV_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_02_PIV_CTL", a=1, t=[2.371125595868051e-06, 0.0, -9.468704887383161e-07])
			mc.xform("R_loLeg_shaper_02_PIV_CTL", a=1, ro=[1.1927073240070309e-15, 6.138782731315875e-06, 180.0])
			mc.xform("R_loLeg_shaper_02_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_upLeg_shaper_03_PIV_CTL"):
			if not mc.getAttr("R_upLeg_shaper_03_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_03_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_03_PIV_CTL", a=1, t=[-4.174784984378732e-06, -3.3306690738754696e-16, -5.218481231583638e-07])
			mc.xform("R_upLeg_shaper_03_PIV_CTL", a=1, ro=[0.0, 0.0, 180.0])
			mc.xform("R_upLeg_shaper_03_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999998, -0.9999999999999999])

		if mc.objExists("R_loLeg_shaper_03_PIV_CTL"):
			if not mc.getAttr("R_loLeg_shaper_03_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_03_PIV_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_03_PIV_CTL", a=1, t=[-4.171326563273681e-06, 0.0, 4.850375211751246e-07])
			mc.xform("R_loLeg_shaper_03_PIV_CTL", a=1, ro=[1.1927073240070309e-15, 6.138782731315875e-06, 180.0])
			mc.xform("R_loLeg_shaper_03_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_upLeg_shaper_04_PIV_CTL"):
			if not mc.getAttr("R_upLeg_shaper_04_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_04_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_04_PIV_CTL", a=1, t=[9.138276527487221e-06, -3.3306690738754696e-16, 4.704297535962354e-07])
			mc.xform("R_upLeg_shaper_04_PIV_CTL", a=1, ro=[0.0, 0.0, 180.0])
			mc.xform("R_upLeg_shaper_04_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999998, -0.9999999999999999])

		if mc.objExists("R_loLeg_shaper_04_PIV_CTL"):
			if not mc.getAttr("R_loLeg_shaper_04_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_04_PIV_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_04_PIV_CTL", a=1, t=[-8.500052472992792e-07, 0.0, 1.6595357431314905e-07])
			mc.xform("R_loLeg_shaper_04_PIV_CTL", a=1, ro=[1.1927073240070309e-15, 6.138782731315875e-06, 180.0])
			mc.xform("R_loLeg_shaper_04_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_upLeg_shaper_05_PIV_CTL"):
			if not mc.getAttr("R_upLeg_shaper_05_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_05_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_05_PIV_CTL", a=1, t=[2.357711037070942e-06, -3.3306690738754696e-16, 9.665686924176242e-07])
			mc.xform("R_upLeg_shaper_05_PIV_CTL", a=1, ro=[0.0, 0.0, 180.0])
			mc.xform("R_upLeg_shaper_05_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999998, -0.9999999999999999])

		if mc.objExists("R_loLeg_shaper_05_PIV_CTL"):
			if not mc.getAttr("R_loLeg_shaper_05_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_05_PIV_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_05_PIV_CTL", a=1, t=[4.6160113420512516e-07, 0.0, -1.20790347168942e-07])
			mc.xform("R_loLeg_shaper_05_PIV_CTL", a=1, ro=[1.1927073240070309e-15, 6.138782731315875e-06, 180.0])
			mc.xform("R_loLeg_shaper_05_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_upLeg_FK_PIV_CTL"):
			if not mc.getAttr("R_upLeg_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_FK_PIV_CTL", a=1, t=[-4.174784990595981e-06, -2.220446049250313e-16, -5.21848123602453e-07])
			mc.xform("R_upLeg_FK_PIV_CTL", a=1, ro=[-1.1927080055488188e-15, -1.1927080055488188e-15, 180.0])
			mc.xform("R_upLeg_FK_PIV_CTL", r=1, s=[1.0, 0.9999999999999999, -1.0])

		if mc.objExists("R_loLeg_FK_PIV_CTL"):
			if not mc.getAttr("R_loLeg_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_FK_PIV_CTL", a=1, t=[-4.179116440461428e-06, 0.0, 4.859433202636376e-07])
			mc.xform("R_loLeg_FK_PIV_CTL", a=1, ro=[1.1927073240070309e-15, 6.138782731315875e-06, 180.0])
			mc.xform("R_loLeg_FK_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_legEnd_FK_PIV_CTL"):
			if not mc.getAttr("R_legEnd_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_legEnd_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_legEnd_FK_PIV_CTL", a=1, t=[-1.903071212838725e-07, 0.0, 2.2128714527447357e-08])
			mc.xform("R_legEnd_FK_PIV_CTL", a=1, ro=[-3.578122653562886e-15, 6.138782732906153e-06, -179.99999999999997])
			mc.xform("R_legEnd_FK_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_leg_IK_PIV_CTL"):
			mc.xform("R_leg_IK_PIV_CTL", a=1, t=[7.771561172376096e-16, -2.220446049250313e-16, 7.771566049250324e-17])
			mc.xform("R_leg_IK_PIV_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("R_leg_IK_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, -1.0])

		if mc.objExists("R_leg_PV_PIV_CTL"):
			mc.xform("R_leg_PV_PIV_CTL", a=1, t=[3.552713678800501e-15, 1.3322676295501878e-15, 10.000000000000002])
			mc.xform("R_leg_PV_PIV_CTL", a=1, ro=[0.0, 0.0, 180.0])
			mc.xform("R_leg_PV_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_legBase_PIV_CTL"):
			if not mc.getAttr("R_legBase_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_PIV_CTL.rotateOrder", 0)

			mc.xform("R_legBase_PIV_CTL", a=1, t=[-4.174784990595981e-06, -2.220446049250313e-16, -5.21848123602453e-07])
			mc.xform("R_legBase_PIV_CTL", a=1, ro=[-1.1927080055488188e-15, -1.1927080055488188e-15, 180.0])
			mc.xform("R_legBase_PIV_CTL", r=1, s=[1.0, 0.9999999999999999, -1.0])

		if mc.objExists("R_leg_IK_switch_PIV_CTL"):
			if not mc.getAttr("R_leg_IK_switch_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_PIV_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_PIV_CTL", a=1, t=[-1.903071212838725e-07, 0.0, 2.2128714527447357e-08])
			mc.xform("R_leg_IK_switch_PIV_CTL", a=1, ro=[-3.578122653562886e-15, 6.138782732906153e-06, -179.99999999999997])
			mc.xform("R_leg_IK_switch_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_bendyLeg_A_PIV_CTL"):
			if not mc.getAttr("R_bendyLeg_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_A_PIV_CTL", a=1, t=[-4.174784986155089e-06, 0.0, -5.218481231583638e-07])
			mc.xform("R_bendyLeg_A_PIV_CTL", a=1, ro=[-1.1927080055488188e-15, -1.1927080055488188e-15, 180.0])
			mc.xform("R_bendyLeg_A_PIV_CTL", r=1, s=[1.0, 0.9999999999999999, -1.0])

		if mc.objExists("R_bendyLeg_B_PIV_CTL"):
			if not mc.getAttr("R_bendyLeg_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_B_PIV_CTL", a=1, t=[-4.207235215325511e-06, 0.0, -1.8082563113530625e-08])
			mc.xform("R_bendyLeg_B_PIV_CTL", a=1, ro=[-7.454459111769697e-17, 3.0693913576568542e-06, 180.0])
			mc.xform("R_bendyLeg_B_PIV_CTL", r=1, s=[1.0, 0.9999999999999999, -1.0])

		if mc.objExists("R_bendyLeg_C_PIV_CTL"):
			if not mc.getAttr("R_bendyLeg_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_C_PIV_CTL", a=1, t=[-2.1847117843698527e-06, 0.0, 2.540360179298373e-07])
			mc.xform("R_bendyLeg_C_PIV_CTL", a=1, ro=[1.1927073240070309e-15, 6.138782731315875e-06, 180.0])
			mc.xform("R_bendyLeg_C_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_thumb_A_PIV_CTL"):
			if not mc.getAttr("R_thumb_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_A_PIV_CTL", a=1, t=[-1.7763568394002505e-15, -2.220446049250313e-15, -3.552713678800501e-15])
			mc.xform("R_thumb_A_PIV_CTL", a=1, ro=[-2.1321567064411918e-05, -0.00014214378031500175, 179.9996498596633])
			mc.xform("R_thumb_A_PIV_CTL", r=1, s=[0.9999999999999998, 1.0, -0.9999999999999999])

		if mc.objExists("R_thumb_B_PIV_CTL"):
			if not mc.getAttr("R_thumb_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_B_PIV_CTL", a=1, t=[-5.329070518200751e-15, 5.329070518200751e-15, -3.552713678800501e-15])
			mc.xform("R_thumb_B_PIV_CTL", a=1, ro=[-1.8912216224616067e-05, 0.00010983464098501666, -179.99980976096643])
			mc.xform("R_thumb_B_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999998])

		if mc.objExists("R_thumb_C_PIV_CTL"):
			if not mc.getAttr("R_thumb_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_C_PIV_CTL", a=1, t=[3.552713678800501e-15, -1.7763568394002505e-15, 7.105427357601002e-15])
			mc.xform("R_thumb_C_PIV_CTL", a=1, ro=[-1.2476503221881395e-05, -0.0001961237397846275, 179.99979846504297])
			mc.xform("R_thumb_C_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999996, -0.9999999999999996])

		if mc.objExists("R_index_A_PIV_CTL"):
			if not mc.getAttr("R_index_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_A_PIV_CTL", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, -5.551115123125783e-17])
			mc.xform("R_index_A_PIV_CTL", a=1, ro=[1.4033418597069752e-14, 7.984865025843222e-30, 179.99999999999994])
			mc.xform("R_index_A_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000002])

		if mc.objExists("R_index_B_PIV_CTL"):
			if not mc.getAttr("R_index_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_B_PIV_CTL", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, -2.7755575615628914e-17])
			mc.xform("R_index_B_PIV_CTL", a=1, ro=[1.4033418597069752e-14, 6.684435135235184e-29, 179.99999999999946])
			mc.xform("R_index_B_PIV_CTL", r=1, s=[1.0, 1.0, -0.9999999999999999])

		if mc.objExists("R_index_C_PIV_CTL"):
			if not mc.getAttr("R_index_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_C_PIV_CTL", a=1, t=[-5.329070518200751e-15, -3.552713678800501e-15, 2.7755575615628914e-17])
			mc.xform("R_index_C_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -1.002976948368112e-28, -179.99999999999918])
			mc.xform("R_index_C_PIV_CTL", r=1, s=[1.0, 1.0, -0.9999999999999999])

		if mc.objExists("R_index_D_PIV_CTL"):
			if not mc.getAttr("R_index_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_D_PIV_CTL", a=1, t=[0.0, 0.0, -5.551115123125783e-17])
			mc.xform("R_index_D_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -4.0420305419780217e-29, -179.99999999999966])
			mc.xform("R_index_D_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -1.0])

		if mc.objExists("R_middle_A_PIV_CTL"):
			if not mc.getAttr("R_middle_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_A_PIV_CTL", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, -3.94430452610506e-31])
			mc.xform("R_middle_A_PIV_CTL", a=1, ro=[1.4033418597069752e-14, 7.984865025843222e-30, 179.99999999999994])
			mc.xform("R_middle_A_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000002])

		if mc.objExists("R_middle_B_PIV_CTL"):
			if not mc.getAttr("R_middle_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_B_PIV_CTL", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, 7.888609052210118e-31])
			mc.xform("R_middle_B_PIV_CTL", a=1, ro=[1.4033418597069752e-14, 6.684435135235184e-29, 179.99999999999946])
			mc.xform("R_middle_B_PIV_CTL", r=1, s=[1.0, 1.0, -0.9999999999999999])

		if mc.objExists("R_middle_C_PIV_CTL"):
			if not mc.getAttr("R_middle_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_C_PIV_CTL", a=1, t=[-5.329070518200751e-15, 3.552713678800501e-15, 3.94430452610506e-31])
			mc.xform("R_middle_C_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -1.002976948368112e-28, -179.99999999999918])
			mc.xform("R_middle_C_PIV_CTL", r=1, s=[1.0, 1.0, -0.9999999999999999])

		if mc.objExists("R_middle_D_PIV_CTL"):
			if not mc.getAttr("R_middle_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_D_PIV_CTL", a=1, t=[0.0, 0.0, 1.1832913578315177e-30])
			mc.xform("R_middle_D_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -4.0420305419780217e-29, -179.99999999999966])
			mc.xform("R_middle_D_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -1.0])

		if mc.objExists("R_ring_A_PIV_CTL"):
			if not mc.getAttr("R_ring_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_A_PIV_CTL", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, 5.551115123125783e-17])
			mc.xform("R_ring_A_PIV_CTL", a=1, ro=[1.4033418597069752e-14, 7.984865025843222e-30, 179.99999999999994])
			mc.xform("R_ring_A_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000002])

		if mc.objExists("R_ring_B_PIV_CTL"):
			if not mc.getAttr("R_ring_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_B_PIV_CTL", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, 0.0])
			mc.xform("R_ring_B_PIV_CTL", a=1, ro=[1.4033418597069752e-14, 6.684435135235184e-29, 179.99999999999946])
			mc.xform("R_ring_B_PIV_CTL", r=1, s=[1.0, 1.0, -0.9999999999999999])

		if mc.objExists("R_ring_C_PIV_CTL"):
			if not mc.getAttr("R_ring_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_C_PIV_CTL", a=1, t=[-5.329070518200751e-15, 3.552713678800501e-15, 0.0])
			mc.xform("R_ring_C_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -1.002976948368112e-28, -179.99999999999918])
			mc.xform("R_ring_C_PIV_CTL", r=1, s=[1.0, 1.0, -0.9999999999999999])

		if mc.objExists("R_ring_D_PIV_CTL"):
			if not mc.getAttr("R_ring_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_D_PIV_CTL", a=1, t=[0.0, 0.0, 5.551115123125783e-17])
			mc.xform("R_ring_D_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -4.0420305419780217e-29, -179.99999999999966])
			mc.xform("R_ring_D_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -1.0])

		if mc.objExists("R_pinky_A_PIV_CTL"):
			if not mc.getAttr("R_pinky_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_A_PIV_CTL", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, 1.1102230246251565e-16])
			mc.xform("R_pinky_A_PIV_CTL", a=1, ro=[1.4033418597069752e-14, 7.984865025843222e-30, 179.99999999999994])
			mc.xform("R_pinky_A_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000002])

		if mc.objExists("R_pinky_B_PIV_CTL"):
			if not mc.getAttr("R_pinky_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_B_PIV_CTL", a=1, t=[1.7763568394002505e-15, 3.552713678800501e-15, 1.1102230246251565e-16])
			mc.xform("R_pinky_B_PIV_CTL", a=1, ro=[1.4033418597069752e-14, 6.684435135235184e-29, 179.99999999999946])
			mc.xform("R_pinky_B_PIV_CTL", r=1, s=[1.0, 1.0, -0.9999999999999999])

		if mc.objExists("R_pinky_C_PIV_CTL"):
			if not mc.getAttr("R_pinky_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_C_PIV_CTL", a=1, t=[-5.329070518200751e-15, 3.552713678800501e-15, 0.0])
			mc.xform("R_pinky_C_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -1.002976948368112e-28, -179.99999999999918])
			mc.xform("R_pinky_C_PIV_CTL", r=1, s=[1.0, 1.0, -0.9999999999999999])

		if mc.objExists("R_pinky_D_PIV_CTL"):
			if not mc.getAttr("R_pinky_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_D_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -4.0420305419780217e-29, -179.99999999999966])
			mc.xform("R_pinky_D_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -1.0])

		if mc.objExists("R_hand_PIV_CTL"):
			mc.xform("R_hand_PIV_CTL", a=1, t=[-0.5, -2.0000000000000036, 1.2246467991473515e-16])
			mc.xform("R_hand_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_hand_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("world_D_OFF_CTL"):
			if not mc.getAttr("world_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("world_D_OFF_CTL.rotateOrder", 0)

			mc.xform("world_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("world_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("world_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("world_C_OFF_CTL"):
			if not mc.getAttr("world_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("world_C_OFF_CTL.rotateOrder", 0)

			mc.xform("world_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("world_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("world_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("world_B_OFF_CTL"):
			if not mc.getAttr("world_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("world_B_OFF_CTL.rotateOrder", 0)

			mc.xform("world_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("world_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("world_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("world_A_OFF_CTL"):
			if not mc.getAttr("world_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("world_A_OFF_CTL.rotateOrder", 0)

			mc.xform("world_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("world_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("world_A_OFF_CTL", r=1, s=[0.25, 0.25, 0.25])

		if mc.objExists("world_CTL"):
			if not mc.getAttr("world_CTL.numOffsetCtrls", l=1):
				mc.setAttr("world_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("world_CTL.mirrorMode", l=1):
				mc.setAttr("world_CTL.mirrorMode", 0)

			if not mc.getAttr("world_CTL.rotateOrder", l=1):
				mc.setAttr("world_CTL.rotateOrder", 0)

			mc.xform("world_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("world_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("world_CTL", r=1, s=[0.25, 0.25, 0.25])

		if mc.objExists("visibility_CTL"):
			if not mc.getAttr("visibility_CTL.mirrorMode", l=1):
				mc.setAttr("visibility_CTL.mirrorMode", 0)

			if not mc.getAttr("visibility_CTL.rotateOrder", l=1):
				mc.setAttr("visibility_CTL.rotateOrder", 0)

			mc.xform("visibility_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("visibility_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("visibility_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_01_D_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_01_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_01_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_01_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_01_C_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_01_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_01_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_01_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_01_B_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_01_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_01_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_01_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_01_A_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_01_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_01_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_01_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_01_CTL"):
			if not mc.getAttr("L_upLeg_shaper_01_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upLeg_shaper_01_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upLeg_shaper_01_CTL.mirrorMode", l=1):
				mc.setAttr("L_upLeg_shaper_01_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upLeg_shaper_01_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_01_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_01_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_01_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_01_D_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_01_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_01_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_01_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_01_C_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_01_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_01_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_01_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_01_B_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_01_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_01_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_01_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_01_A_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_01_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_01_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_01_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_01_CTL"):
			if not mc.getAttr("L_loLeg_shaper_01_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_loLeg_shaper_01_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_loLeg_shaper_01_CTL.mirrorMode", l=1):
				mc.setAttr("L_loLeg_shaper_01_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loLeg_shaper_01_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_01_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_01_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_01_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_02_D_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_02_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_02_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_02_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_02_C_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_02_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_02_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_02_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_02_B_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_02_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_02_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_02_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_02_A_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_02_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_02_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_02_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_02_CTL"):
			if not mc.getAttr("L_upLeg_shaper_02_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upLeg_shaper_02_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upLeg_shaper_02_CTL.mirrorMode", l=1):
				mc.setAttr("L_upLeg_shaper_02_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upLeg_shaper_02_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_02_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_02_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_02_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_02_D_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_02_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_02_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_02_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_02_C_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_02_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_02_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_02_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_02_B_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_02_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_02_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_02_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_02_A_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_02_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_02_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_02_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_02_CTL"):
			if not mc.getAttr("L_loLeg_shaper_02_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_loLeg_shaper_02_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_loLeg_shaper_02_CTL.mirrorMode", l=1):
				mc.setAttr("L_loLeg_shaper_02_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loLeg_shaper_02_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_02_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_02_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_02_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_03_D_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_03_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_03_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_03_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_03_C_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_03_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_03_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_03_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_03_B_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_03_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_03_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_03_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_03_A_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_03_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_03_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_03_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_03_CTL"):
			if not mc.getAttr("L_upLeg_shaper_03_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upLeg_shaper_03_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upLeg_shaper_03_CTL.mirrorMode", l=1):
				mc.setAttr("L_upLeg_shaper_03_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upLeg_shaper_03_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_03_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_03_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_03_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_03_D_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_03_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_03_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_03_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_03_C_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_03_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_03_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_03_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_03_B_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_03_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_03_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_03_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_03_A_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_03_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_03_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_03_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_03_CTL"):
			if not mc.getAttr("L_loLeg_shaper_03_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_loLeg_shaper_03_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_loLeg_shaper_03_CTL.mirrorMode", l=1):
				mc.setAttr("L_loLeg_shaper_03_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loLeg_shaper_03_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_03_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_03_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_03_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_04_D_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_04_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_04_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_04_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_04_C_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_04_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_04_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_04_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_04_B_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_04_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_04_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_04_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_04_A_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_04_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_04_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_04_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_04_CTL"):
			if not mc.getAttr("L_upLeg_shaper_04_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upLeg_shaper_04_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upLeg_shaper_04_CTL.mirrorMode", l=1):
				mc.setAttr("L_upLeg_shaper_04_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upLeg_shaper_04_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_04_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_04_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_04_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_04_D_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_04_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_04_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_04_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_04_C_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_04_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_04_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_04_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_04_B_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_04_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_04_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_04_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_04_A_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_04_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_04_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_04_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_04_CTL"):
			if not mc.getAttr("L_loLeg_shaper_04_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_loLeg_shaper_04_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_loLeg_shaper_04_CTL.mirrorMode", l=1):
				mc.setAttr("L_loLeg_shaper_04_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loLeg_shaper_04_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_04_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_04_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_04_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_05_D_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_05_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_05_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_05_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_05_C_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_05_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_05_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_05_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_05_B_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_05_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_05_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_05_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_05_A_OFF_CTL"):
			if not mc.getAttr("L_upLeg_shaper_05_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_05_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_05_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_05_CTL"):
			if not mc.getAttr("L_upLeg_shaper_05_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upLeg_shaper_05_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upLeg_shaper_05_CTL.mirrorMode", l=1):
				mc.setAttr("L_upLeg_shaper_05_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upLeg_shaper_05_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_05_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_05_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_05_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_05_D_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_05_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_05_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_05_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_05_C_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_05_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_05_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_05_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_05_B_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_05_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_05_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_05_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_05_A_OFF_CTL"):
			if not mc.getAttr("L_loLeg_shaper_05_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_05_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_05_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_05_CTL"):
			if not mc.getAttr("L_loLeg_shaper_05_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_loLeg_shaper_05_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_loLeg_shaper_05_CTL.mirrorMode", l=1):
				mc.setAttr("L_loLeg_shaper_05_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loLeg_shaper_05_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_05_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_05_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_05_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_FK_CTL"):
			if not mc.getAttr("L_upLeg_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_upLeg_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upLeg_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_FK_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_FK_CTL"):
			if not mc.getAttr("L_loLeg_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_loLeg_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loLeg_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_FK_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_legEnd_FK_CTL"):
			if not mc.getAttr("L_legEnd_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_legEnd_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_legEnd_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_legEnd_FK_CTL.rotateOrder", 0)

			mc.xform("L_legEnd_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legEnd_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legEnd_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_D_OFF_CTL"):
			if not mc.getAttr("L_leg_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_leg_IK_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_C_OFF_CTL"):
			if not mc.getAttr("L_leg_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_leg_IK_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_B_OFF_CTL"):
			if not mc.getAttr("L_leg_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_leg_IK_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_A_OFF_CTL"):
			if not mc.getAttr("L_leg_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_leg_IK_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_CTL"):
			if not mc.getAttr("L_leg_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_leg_IK_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("L_leg_IK_CTL.mirrorMode", l=1):
				mc.setAttr("L_leg_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_leg_IK_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_IK_CTL.rotateOrder", 0)

			mc.xform("L_leg_IK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_PV_CTL"):
			if not mc.getAttr("L_leg_PV_CTL.mirrorMode", l=1):
				mc.setAttr("L_leg_PV_CTL.mirrorMode", 0)

			if not mc.getAttr("L_leg_PV_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_PV_CTL.rotateOrder", 0)

			mc.xform("L_leg_PV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_PV_CTL", a=1, ro=[180.0, 0.0, -90.0])
			mc.xform("L_leg_PV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_legBase_D_OFF_CTL"):
			if not mc.getAttr("L_legBase_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_legBase_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_legBase_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_D_OFF_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0000000000000002])

		if mc.objExists("L_legBase_C_OFF_CTL"):
			if not mc.getAttr("L_legBase_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_legBase_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_legBase_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_C_OFF_CTL", r=1, s=[0.9999999999999998, 1.0, 0.9999999999999998])

		if mc.objExists("L_legBase_B_OFF_CTL"):
			if not mc.getAttr("L_legBase_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_legBase_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_legBase_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_B_OFF_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0000000000000002])

		if mc.objExists("L_legBase_A_OFF_CTL"):
			if not mc.getAttr("L_legBase_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_legBase_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_legBase_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_A_OFF_CTL", r=1, s=[0.9999999999999999, 1.0, 0.9999999999999999])

		if mc.objExists("L_legBase_CTL"):
			if not mc.getAttr("L_legBase_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_legBase_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_legBase_CTL.mirrorMode", l=1):
				mc.setAttr("L_legBase_CTL.mirrorMode", 0)

			if not mc.getAttr("L_legBase_CTL.rotateOrder", l=1):
				mc.setAttr("L_legBase_CTL.rotateOrder", 0)

			mc.xform("L_legBase_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_switch_D_OFF_CTL"):
			if not mc.getAttr("L_leg_IK_switch_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_IK_switch_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_leg_IK_switch_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_switch_C_OFF_CTL"):
			if not mc.getAttr("L_leg_IK_switch_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_IK_switch_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_leg_IK_switch_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_switch_B_OFF_CTL"):
			if not mc.getAttr("L_leg_IK_switch_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_IK_switch_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_leg_IK_switch_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_switch_A_OFF_CTL"):
			if not mc.getAttr("L_leg_IK_switch_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_IK_switch_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_leg_IK_switch_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_switch_CTL"):
			if not mc.getAttr("L_leg_IK_switch_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_leg_IK_switch_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_leg_IK_switch_CTL.mirrorMode", l=1):
				mc.setAttr("L_leg_IK_switch_CTL.mirrorMode", 0)

			if not mc.getAttr("L_leg_IK_switch_CTL.rotateOrder", l=1):
				mc.setAttr("L_leg_IK_switch_CTL.rotateOrder", 0)

			mc.xform("L_leg_IK_switch_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_switch_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_A_D_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_A_C_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_A_B_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_A_A_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_A_CTL"):
			if not mc.getAttr("L_bendyLeg_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_bendyLeg_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_bendyLeg_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_bendyLeg_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_bendyLeg_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_A_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_B_D_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_B_C_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_B_B_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_B_A_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_B_CTL"):
			if not mc.getAttr("L_bendyLeg_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_bendyLeg_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_bendyLeg_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_bendyLeg_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_bendyLeg_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_B_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_C_D_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_C_C_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_C_B_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_C_A_OFF_CTL"):
			if not mc.getAttr("L_bendyLeg_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyLeg_C_CTL"):
			if not mc.getAttr("L_bendyLeg_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_bendyLeg_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_bendyLeg_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_bendyLeg_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_bendyLeg_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyLeg_C_CTL.rotateOrder", 0)

			mc.xform("L_bendyLeg_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyLeg_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_01_D_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_01_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_01_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_01_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_01_C_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_01_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_01_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_01_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_01_B_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_01_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_01_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_01_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_01_A_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_01_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_01_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_01_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_01_CTL"):
			if not mc.getAttr("L_shoulder_shaper_01_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_shoulder_shaper_01_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_shoulder_shaper_01_CTL.mirrorMode", l=1):
				mc.setAttr("L_shoulder_shaper_01_CTL.mirrorMode", 0)

			if not mc.getAttr("L_shoulder_shaper_01_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_01_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_01_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_01_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_01_D_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_01_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_01_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_01_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_01_C_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_01_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_01_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_01_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_01_B_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_01_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_01_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_01_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_01_A_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_01_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_01_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_01_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_01_CTL"):
			if not mc.getAttr("L_elbow_shaper_01_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_elbow_shaper_01_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_elbow_shaper_01_CTL.mirrorMode", l=1):
				mc.setAttr("L_elbow_shaper_01_CTL.mirrorMode", 0)

			if not mc.getAttr("L_elbow_shaper_01_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_01_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_01_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_01_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_02_D_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_02_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_02_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_02_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_02_C_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_02_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_02_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_02_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_02_B_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_02_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_02_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_02_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_02_A_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_02_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_02_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_02_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_02_CTL"):
			if not mc.getAttr("L_shoulder_shaper_02_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_shoulder_shaper_02_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_shoulder_shaper_02_CTL.mirrorMode", l=1):
				mc.setAttr("L_shoulder_shaper_02_CTL.mirrorMode", 0)

			if not mc.getAttr("L_shoulder_shaper_02_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_02_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_02_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_02_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_02_D_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_02_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_02_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_02_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_02_C_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_02_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_02_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_02_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_02_B_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_02_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_02_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_02_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_02_A_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_02_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_02_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_02_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_02_CTL"):
			if not mc.getAttr("L_elbow_shaper_02_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_elbow_shaper_02_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_elbow_shaper_02_CTL.mirrorMode", l=1):
				mc.setAttr("L_elbow_shaper_02_CTL.mirrorMode", 0)

			if not mc.getAttr("L_elbow_shaper_02_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_02_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_02_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_02_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_03_D_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_03_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_03_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_03_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_03_C_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_03_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_03_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_03_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_03_B_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_03_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_03_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_03_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_03_A_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_03_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_03_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_03_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_03_CTL"):
			if not mc.getAttr("L_shoulder_shaper_03_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_shoulder_shaper_03_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_shoulder_shaper_03_CTL.mirrorMode", l=1):
				mc.setAttr("L_shoulder_shaper_03_CTL.mirrorMode", 0)

			if not mc.getAttr("L_shoulder_shaper_03_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_03_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_03_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_03_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_03_D_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_03_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_03_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_03_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_03_C_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_03_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_03_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_03_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_03_B_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_03_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_03_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_03_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_03_A_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_03_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_03_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_03_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_03_CTL"):
			if not mc.getAttr("L_elbow_shaper_03_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_elbow_shaper_03_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_elbow_shaper_03_CTL.mirrorMode", l=1):
				mc.setAttr("L_elbow_shaper_03_CTL.mirrorMode", 0)

			if not mc.getAttr("L_elbow_shaper_03_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_03_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_03_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_03_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_04_D_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_04_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_04_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_04_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_04_C_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_04_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_04_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_04_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_04_B_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_04_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_04_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_04_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_04_A_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_04_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_04_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_04_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_04_CTL"):
			if not mc.getAttr("L_shoulder_shaper_04_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_shoulder_shaper_04_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_shoulder_shaper_04_CTL.mirrorMode", l=1):
				mc.setAttr("L_shoulder_shaper_04_CTL.mirrorMode", 0)

			if not mc.getAttr("L_shoulder_shaper_04_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_04_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_04_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_04_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_04_D_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_04_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_04_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_04_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_04_C_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_04_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_04_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_04_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_04_B_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_04_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_04_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_04_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_04_A_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_04_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_04_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_04_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_04_CTL"):
			if not mc.getAttr("L_elbow_shaper_04_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_elbow_shaper_04_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_elbow_shaper_04_CTL.mirrorMode", l=1):
				mc.setAttr("L_elbow_shaper_04_CTL.mirrorMode", 0)

			if not mc.getAttr("L_elbow_shaper_04_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_04_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_04_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_04_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_05_D_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_05_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_05_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_05_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_05_C_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_05_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_05_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_05_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_05_B_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_05_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_05_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_05_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_05_A_OFF_CTL"):
			if not mc.getAttr("L_shoulder_shaper_05_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_05_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_05_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_shaper_05_CTL"):
			if not mc.getAttr("L_shoulder_shaper_05_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_shoulder_shaper_05_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_shoulder_shaper_05_CTL.mirrorMode", l=1):
				mc.setAttr("L_shoulder_shaper_05_CTL.mirrorMode", 0)

			if not mc.getAttr("L_shoulder_shaper_05_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_shaper_05_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_shaper_05_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_shaper_05_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_05_D_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_05_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_05_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_05_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_05_C_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_05_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_05_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_05_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_05_B_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_05_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_05_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_05_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_05_A_OFF_CTL"):
			if not mc.getAttr("L_elbow_shaper_05_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_05_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_05_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbow_shaper_05_CTL"):
			if not mc.getAttr("L_elbow_shaper_05_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_elbow_shaper_05_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_elbow_shaper_05_CTL.mirrorMode", l=1):
				mc.setAttr("L_elbow_shaper_05_CTL.mirrorMode", 0)

			if not mc.getAttr("L_elbow_shaper_05_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbow_shaper_05_CTL.rotateOrder", 0)

			mc.xform("L_elbow_shaper_05_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbow_shaper_05_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_scapulaCtrl_CTL"):
			if not mc.getAttr("L_scapulaCtrl_CTL.mirrorMode", l=1):
				mc.setAttr("L_scapulaCtrl_CTL.mirrorMode", 0)

			if not mc.getAttr("L_scapulaCtrl_CTL.rotateOrder", l=1):
				mc.setAttr("L_scapulaCtrl_CTL.rotateOrder", 0)

			mc.xform("L_scapulaCtrl_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaCtrl_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaCtrl_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_scapulaTarget_CTL"):
			if not mc.getAttr("L_scapulaTarget_CTL.mirrorMode", l=1):
				mc.setAttr("L_scapulaTarget_CTL.mirrorMode", 0)

			if not mc.getAttr("L_scapulaTarget_CTL.rotateOrder", l=1):
				mc.setAttr("L_scapulaTarget_CTL.rotateOrder", 0)

			mc.xform("L_scapulaTarget_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaTarget_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaTarget_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_scapulaChest_CTL"):
			if not mc.getAttr("L_scapulaChest_CTL.mirrorMode", l=1):
				mc.setAttr("L_scapulaChest_CTL.mirrorMode", 0)

			if not mc.getAttr("L_scapulaChest_CTL.rotateOrder", l=1):
				mc.setAttr("L_scapulaChest_CTL.rotateOrder", 0)

			mc.xform("L_scapulaChest_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaChest_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_scapulaChest_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulderFk_CTL"):
			if not mc.getAttr("L_shoulderFk_CTL.mirrorMode", l=1):
				mc.setAttr("L_shoulderFk_CTL.mirrorMode", 0)

			if not mc.getAttr("L_shoulderFk_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulderFk_CTL.rotateOrder", 0)

			mc.xform("L_shoulderFk_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulderFk_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulderFk_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbowFk_CTL"):
			if not mc.getAttr("L_elbowFk_CTL.mirrorMode", l=1):
				mc.setAttr("L_elbowFk_CTL.mirrorMode", 0)

			if not mc.getAttr("L_elbowFk_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbowFk_CTL.rotateOrder", 0)

			mc.xform("L_elbowFk_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbowFk_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbowFk_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wristFk_CTL"):
			if not mc.getAttr("L_wristFk_CTL.mirrorMode", l=1):
				mc.setAttr("L_wristFk_CTL.mirrorMode", 0)

			if not mc.getAttr("L_wristFk_CTL.rotateOrder", l=1):
				mc.setAttr("L_wristFk_CTL.rotateOrder", 0)

			mc.xform("L_wristFk_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wristFk_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wristFk_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_handIk_D_OFF_CTL"):
			if not mc.getAttr("L_handIk_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_handIk_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_handIk_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_handIk_C_OFF_CTL"):
			if not mc.getAttr("L_handIk_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_handIk_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_handIk_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_handIk_B_OFF_CTL"):
			if not mc.getAttr("L_handIk_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_handIk_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_handIk_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_handIk_A_OFF_CTL"):
			if not mc.getAttr("L_handIk_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_handIk_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_handIk_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_handIk_CTL"):
			if not mc.getAttr("L_handIk_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_handIk_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("L_handIk_CTL.mirrorMode", l=1):
				mc.setAttr("L_handIk_CTL.mirrorMode", 0)

			if not mc.getAttr("L_handIk_CTL.rotateOrder", l=1):
				mc.setAttr("L_handIk_CTL.rotateOrder", 0)

			mc.xform("L_handIk_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_handIk_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmTwist_D_OFF_CTL"):
			if not mc.getAttr("L_lwrArmTwist_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmTwist_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmTwist_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmTwist_C_OFF_CTL"):
			if not mc.getAttr("L_lwrArmTwist_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmTwist_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmTwist_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmTwist_B_OFF_CTL"):
			if not mc.getAttr("L_lwrArmTwist_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmTwist_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmTwist_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmTwist_A_OFF_CTL"):
			if not mc.getAttr("L_lwrArmTwist_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmTwist_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmTwist_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmTwist_CTL"):
			if not mc.getAttr("L_lwrArmTwist_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lwrArmTwist_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lwrArmTwist_CTL.mirrorMode", l=1):
				mc.setAttr("L_lwrArmTwist_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lwrArmTwist_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmTwist_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmTwist_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmTwist_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbowUpVectorIk_CTL"):
			if not mc.getAttr("L_elbowUpVectorIk_CTL.mirrorMode", l=1):
				mc.setAttr("L_elbowUpVectorIk_CTL.mirrorMode", 0)

			if not mc.getAttr("L_elbowUpVectorIk_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbowUpVectorIk_CTL.rotateOrder", 0)

			mc.xform("L_elbowUpVectorIk_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbowUpVectorIk_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbowUpVectorIk_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_clavicle_D_OFF_CTL"):
			if not mc.getAttr("L_clavicle_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_clavicle_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_clavicle_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_clavicle_C_OFF_CTL"):
			if not mc.getAttr("L_clavicle_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_clavicle_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_clavicle_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_clavicle_B_OFF_CTL"):
			if not mc.getAttr("L_clavicle_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_clavicle_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_clavicle_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_clavicle_A_OFF_CTL"):
			if not mc.getAttr("L_clavicle_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_clavicle_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_clavicle_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_clavicle_CTL"):
			if not mc.getAttr("L_clavicle_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_clavicle_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_clavicle_CTL.mirrorMode", l=1):
				mc.setAttr("L_clavicle_CTL.mirrorMode", 0)

			if not mc.getAttr("L_clavicle_CTL.rotateOrder", l=1):
				mc.setAttr("L_clavicle_CTL.rotateOrder", 0)

			mc.xform("L_clavicle_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_uprArmRibbonMid_D_OFF_CTL"):
			if not mc.getAttr("L_uprArmRibbonMid_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_uprArmRibbonMid_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_uprArmRibbonMid_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_uprArmRibbonMid_C_OFF_CTL"):
			if not mc.getAttr("L_uprArmRibbonMid_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_uprArmRibbonMid_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_uprArmRibbonMid_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_uprArmRibbonMid_B_OFF_CTL"):
			if not mc.getAttr("L_uprArmRibbonMid_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_uprArmRibbonMid_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_uprArmRibbonMid_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_uprArmRibbonMid_A_OFF_CTL"):
			if not mc.getAttr("L_uprArmRibbonMid_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_uprArmRibbonMid_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_uprArmRibbonMid_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_uprArmRibbonMid_CTL"):
			if not mc.getAttr("L_uprArmRibbonMid_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_uprArmRibbonMid_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_uprArmRibbonMid_CTL.mirrorMode", l=1):
				mc.setAttr("L_uprArmRibbonMid_CTL.mirrorMode", 0)

			if not mc.getAttr("L_uprArmRibbonMid_CTL.rotateOrder", l=1):
				mc.setAttr("L_uprArmRibbonMid_CTL.rotateOrder", 0)

			mc.xform("L_uprArmRibbonMid_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_uprArmRibbonMid_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbowRibbon_D_OFF_CTL"):
			if not mc.getAttr("L_elbowRibbon_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbowRibbon_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbowRibbon_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbowRibbon_C_OFF_CTL"):
			if not mc.getAttr("L_elbowRibbon_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbowRibbon_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbowRibbon_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbowRibbon_B_OFF_CTL"):
			if not mc.getAttr("L_elbowRibbon_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbowRibbon_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbowRibbon_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbowRibbon_A_OFF_CTL"):
			if not mc.getAttr("L_elbowRibbon_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbowRibbon_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_elbowRibbon_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_elbowRibbon_CTL"):
			if not mc.getAttr("L_elbowRibbon_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_elbowRibbon_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_elbowRibbon_CTL.mirrorMode", l=1):
				mc.setAttr("L_elbowRibbon_CTL.mirrorMode", 0)

			if not mc.getAttr("L_elbowRibbon_CTL.rotateOrder", l=1):
				mc.setAttr("L_elbowRibbon_CTL.rotateOrder", 0)

			mc.xform("L_elbowRibbon_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_elbowRibbon_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmRibbonMid_D_OFF_CTL"):
			if not mc.getAttr("L_lwrArmRibbonMid_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmRibbonMid_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmRibbonMid_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmRibbonMid_C_OFF_CTL"):
			if not mc.getAttr("L_lwrArmRibbonMid_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmRibbonMid_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmRibbonMid_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmRibbonMid_B_OFF_CTL"):
			if not mc.getAttr("L_lwrArmRibbonMid_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmRibbonMid_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmRibbonMid_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmRibbonMid_A_OFF_CTL"):
			if not mc.getAttr("L_lwrArmRibbonMid_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmRibbonMid_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmRibbonMid_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lwrArmRibbonMid_CTL"):
			if not mc.getAttr("L_lwrArmRibbonMid_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lwrArmRibbonMid_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lwrArmRibbonMid_CTL.mirrorMode", l=1):
				mc.setAttr("L_lwrArmRibbonMid_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lwrArmRibbonMid_CTL.rotateOrder", l=1):
				mc.setAttr("L_lwrArmRibbonMid_CTL.rotateOrder", 0)

			mc.xform("L_lwrArmRibbonMid_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lwrArmRibbonMid_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_switch_D_OFF_CTL"):
			if not mc.getAttr("L_arm_IK_switch_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_switch_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_switch_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_switch_C_OFF_CTL"):
			if not mc.getAttr("L_arm_IK_switch_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_switch_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_switch_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_switch_B_OFF_CTL"):
			if not mc.getAttr("L_arm_IK_switch_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_switch_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_switch_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_switch_A_OFF_CTL"):
			if not mc.getAttr("L_arm_IK_switch_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_switch_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_switch_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_switch_CTL"):
			if not mc.getAttr("L_arm_IK_switch_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_arm_IK_switch_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_arm_IK_switch_CTL.mirrorMode", l=1):
				mc.setAttr("L_arm_IK_switch_CTL.mirrorMode", 0)

			if not mc.getAttr("L_arm_IK_switch_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_switch_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_switch_CTL", a=1, t=[-20.0, 10.0, 0.0])
			mc.xform("L_arm_IK_switch_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_innerBall_CTL"):
			if not mc.getAttr("L_innerBall_CTL.mirrorMode", l=1):
				mc.setAttr("L_innerBall_CTL.mirrorMode", 0)

			if not mc.getAttr("L_innerBall_CTL.rotateOrder", l=1):
				mc.setAttr("L_innerBall_CTL.rotateOrder", 0)

			mc.xform("L_innerBall_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_innerBall_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_innerBall_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterBall_CTL"):
			if not mc.getAttr("L_outterBall_CTL.mirrorMode", l=1):
				mc.setAttr("L_outterBall_CTL.mirrorMode", 0)

			if not mc.getAttr("L_outterBall_CTL.rotateOrder", l=1):
				mc.setAttr("L_outterBall_CTL.rotateOrder", 0)

			mc.xform("L_outterBall_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterBall_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_outterBall_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_heel_CTL"):
			if not mc.getAttr("L_heel_CTL.mirrorMode", l=1):
				mc.setAttr("L_heel_CTL.mirrorMode", 0)

			if not mc.getAttr("L_heel_CTL.rotateOrder", l=1):
				mc.setAttr("L_heel_CTL.rotateOrder", 0)

			mc.xform("L_heel_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_heel_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_heel_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toeTip_CTL"):
			if not mc.getAttr("L_toeTip_CTL.mirrorMode", l=1):
				mc.setAttr("L_toeTip_CTL.mirrorMode", 0)

			if not mc.getAttr("L_toeTip_CTL.rotateOrder", l=1):
				mc.setAttr("L_toeTip_CTL.rotateOrder", 0)

			mc.xform("L_toeTip_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_toeTip_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toeTip_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_reverseBall_CTL"):
			if not mc.getAttr("L_reverseBall_CTL.mirrorMode", l=1):
				mc.setAttr("L_reverseBall_CTL.mirrorMode", 0)

			if not mc.getAttr("L_reverseBall_CTL.rotateOrder", l=1):
				mc.setAttr("L_reverseBall_CTL.rotateOrder", 0)

			mc.xform("L_reverseBall_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_reverseBall_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_reverseBall_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ankleOffset_CTL"):
			if not mc.getAttr("L_ankleOffset_CTL.mirrorMode", l=1):
				mc.setAttr("L_ankleOffset_CTL.mirrorMode", 0)

			if not mc.getAttr("L_ankleOffset_CTL.rotateOrder", l=1):
				mc.setAttr("L_ankleOffset_CTL.rotateOrder", 0)

			mc.xform("L_ankleOffset_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ankleOffset_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ankleOffset_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_IK_D_OFF_CTL"):
			if not mc.getAttr("L_toe_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_toe_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_toe_IK_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_IK_C_OFF_CTL"):
			if not mc.getAttr("L_toe_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_toe_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_toe_IK_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_IK_B_OFF_CTL"):
			if not mc.getAttr("L_toe_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_toe_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_toe_IK_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_IK_A_OFF_CTL"):
			if not mc.getAttr("L_toe_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_toe_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_toe_IK_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_IK_CTL"):
			if not mc.getAttr("L_toe_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_toe_IK_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_toe_IK_CTL.mirrorMode", l=1):
				mc.setAttr("L_toe_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_toe_IK_CTL.rotateOrder", l=1):
				mc.setAttr("L_toe_IK_CTL.rotateOrder", 0)

			mc.xform("L_toe_IK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_IK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_FK_CTL"):
			if not mc.getAttr("L_toe_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_toe_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_toe_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_toe_FK_CTL.rotateOrder", 0)

			mc.xform("L_toe_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_toe_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_cog_D_OFF_CTL"):
			if not mc.getAttr("C_cog_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_cog_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_cog_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_cog_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_cog_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_cog_C_OFF_CTL"):
			if not mc.getAttr("C_cog_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_cog_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_cog_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_cog_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_cog_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_cog_B_OFF_CTL"):
			if not mc.getAttr("C_cog_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_cog_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_cog_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_cog_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_cog_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_cog_A_OFF_CTL"):
			if not mc.getAttr("C_cog_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_cog_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_cog_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_cog_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_cog_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_cog_CTL"):
			if not mc.getAttr("C_cog_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_cog_CTL.numOffsetCtrls", 3)

			if not mc.getAttr("C_cog_CTL.mirrorMode", l=1):
				mc.setAttr("C_cog_CTL.mirrorMode", 0)

			if not mc.getAttr("C_cog_CTL.rotateOrder", l=1):
				mc.setAttr("C_cog_CTL.rotateOrder", 0)

			mc.xform("C_cog_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_cog_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_cog_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_D_OFF_CTL"):
			if not mc.getAttr("C_chest_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_chest_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_chest_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_C_OFF_CTL"):
			if not mc.getAttr("C_chest_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_chest_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_chest_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_B_OFF_CTL"):
			if not mc.getAttr("C_chest_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_chest_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_chest_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_A_OFF_CTL"):
			if not mc.getAttr("C_chest_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_chest_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_chest_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_CTL"):
			if not mc.getAttr("C_chest_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_chest_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("C_chest_CTL.mirrorMode", l=1):
				mc.setAttr("C_chest_CTL.mirrorMode", 0)

			if not mc.getAttr("C_chest_CTL.rotateOrder", l=1):
				mc.setAttr("C_chest_CTL.rotateOrder", 0)

			mc.xform("C_chest_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_hip_D_OFF_CTL"):
			if not mc.getAttr("C_hip_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_hip_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_hip_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_hip_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_hip_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_hip_C_OFF_CTL"):
			if not mc.getAttr("C_hip_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_hip_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_hip_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_hip_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_hip_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_hip_B_OFF_CTL"):
			if not mc.getAttr("C_hip_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_hip_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_hip_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_hip_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_hip_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_hip_A_OFF_CTL"):
			if not mc.getAttr("C_hip_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_hip_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_hip_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_hip_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_hip_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_hip_CTL"):
			if not mc.getAttr("C_hip_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_hip_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("C_hip_CTL.mirrorMode", l=1):
				mc.setAttr("C_hip_CTL.mirrorMode", 0)

			if not mc.getAttr("C_hip_CTL.rotateOrder", l=1):
				mc.setAttr("C_hip_CTL.rotateOrder", 0)

			mc.xform("C_hip_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_hip_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_hip_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spine_FK_0_CTL"):
			if not mc.getAttr("C_spine_FK_0_CTL.mirrorMode", l=1):
				mc.setAttr("C_spine_FK_0_CTL.mirrorMode", 0)

			if not mc.getAttr("C_spine_FK_0_CTL.rotateOrder", l=1):
				mc.setAttr("C_spine_FK_0_CTL.rotateOrder", 0)

			mc.xform("C_spine_FK_0_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_0_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_0_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spine_FK_chest_CTL"):
			if not mc.getAttr("C_spine_FK_chest_CTL.mirrorMode", l=1):
				mc.setAttr("C_spine_FK_chest_CTL.mirrorMode", 0)

			if not mc.getAttr("C_spine_FK_chest_CTL.rotateOrder", l=1):
				mc.setAttr("C_spine_FK_chest_CTL.rotateOrder", 0)

			mc.xform("C_spine_FK_chest_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_chest_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_chest_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_revSpine_chest_CTL"):
			if not mc.getAttr("C_revSpine_chest_CTL.mirrorMode", l=1):
				mc.setAttr("C_revSpine_chest_CTL.mirrorMode", 0)

			if not mc.getAttr("C_revSpine_chest_CTL.rotateOrder", l=1):
				mc.setAttr("C_revSpine_chest_CTL.rotateOrder", 0)

			mc.xform("C_revSpine_chest_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_chest_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_chest_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_revSpine_0_CTL"):
			if not mc.getAttr("C_revSpine_0_CTL.mirrorMode", l=1):
				mc.setAttr("C_revSpine_0_CTL.mirrorMode", 0)

			if not mc.getAttr("C_revSpine_0_CTL.rotateOrder", l=1):
				mc.setAttr("C_revSpine_0_CTL.rotateOrder", 0)

			mc.xform("C_revSpine_0_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_0_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_0_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midSpine_D_OFF_CTL"):
			if not mc.getAttr("C_midSpine_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midSpine_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midSpine_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midSpine_C_OFF_CTL"):
			if not mc.getAttr("C_midSpine_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midSpine_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midSpine_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midSpine_B_OFF_CTL"):
			if not mc.getAttr("C_midSpine_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midSpine_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midSpine_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midSpine_A_OFF_CTL"):
			if not mc.getAttr("C_midSpine_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midSpine_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midSpine_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midSpine_CTL"):
			if not mc.getAttr("C_midSpine_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_midSpine_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_midSpine_CTL.mirrorMode", l=1):
				mc.setAttr("C_midSpine_CTL.mirrorMode", 0)

			if not mc.getAttr("C_midSpine_CTL.rotateOrder", l=1):
				mc.setAttr("C_midSpine_CTL.rotateOrder", 0)

			mc.xform("C_midSpine_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midSpine_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spine_FK_1_CTL"):
			if not mc.getAttr("C_spine_FK_1_CTL.mirrorMode", l=1):
				mc.setAttr("C_spine_FK_1_CTL.mirrorMode", 0)

			if not mc.getAttr("C_spine_FK_1_CTL.rotateOrder", l=1):
				mc.setAttr("C_spine_FK_1_CTL.rotateOrder", 0)

			mc.xform("C_spine_FK_1_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_1_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spine_FK_1_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_revSpine_1_CTL"):
			if not mc.getAttr("C_revSpine_1_CTL.mirrorMode", l=1):
				mc.setAttr("C_revSpine_1_CTL.mirrorMode", 0)

			if not mc.getAttr("C_revSpine_1_CTL.rotateOrder", l=1):
				mc.setAttr("C_revSpine_1_CTL.rotateOrder", 0)

			mc.xform("C_revSpine_1_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_1_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_revSpine_1_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spineShaper_1_CTL"):
			if not mc.getAttr("C_spineShaper_1_CTL.mirrorMode", l=1):
				mc.setAttr("C_spineShaper_1_CTL.mirrorMode", 0)

			if not mc.getAttr("C_spineShaper_1_CTL.rotateOrder", l=1):
				mc.setAttr("C_spineShaper_1_CTL.rotateOrder", 0)

			mc.xform("C_spineShaper_1_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_1_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_1_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spineShaper_2_CTL"):
			if not mc.getAttr("C_spineShaper_2_CTL.mirrorMode", l=1):
				mc.setAttr("C_spineShaper_2_CTL.mirrorMode", 0)

			if not mc.getAttr("C_spineShaper_2_CTL.rotateOrder", l=1):
				mc.setAttr("C_spineShaper_2_CTL.rotateOrder", 0)

			mc.xform("C_spineShaper_2_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_2_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_2_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spineShaper_3_CTL"):
			if not mc.getAttr("C_spineShaper_3_CTL.mirrorMode", l=1):
				mc.setAttr("C_spineShaper_3_CTL.mirrorMode", 0)

			if not mc.getAttr("C_spineShaper_3_CTL.rotateOrder", l=1):
				mc.setAttr("C_spineShaper_3_CTL.rotateOrder", 0)

			mc.xform("C_spineShaper_3_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_3_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_3_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spineShaper_4_CTL"):
			if not mc.getAttr("C_spineShaper_4_CTL.mirrorMode", l=1):
				mc.setAttr("C_spineShaper_4_CTL.mirrorMode", 0)

			if not mc.getAttr("C_spineShaper_4_CTL.rotateOrder", l=1):
				mc.setAttr("C_spineShaper_4_CTL.rotateOrder", 0)

			mc.xform("C_spineShaper_4_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_4_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_4_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spineShaper_5_CTL"):
			if not mc.getAttr("C_spineShaper_5_CTL.mirrorMode", l=1):
				mc.setAttr("C_spineShaper_5_CTL.mirrorMode", 0)

			if not mc.getAttr("C_spineShaper_5_CTL.rotateOrder", l=1):
				mc.setAttr("C_spineShaper_5_CTL.rotateOrder", 0)

			mc.xform("C_spineShaper_5_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_5_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spineShaper_5_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_FK_CTL"):
			if not mc.getAttr("C_chest_FK_CTL.mirrorMode", l=1):
				mc.setAttr("C_chest_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("C_chest_FK_CTL.rotateOrder", l=1):
				mc.setAttr("C_chest_FK_CTL.rotateOrder", 0)

			mc.xform("C_chest_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_A_CTL"):
			if not mc.getAttr("L_thumb_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_thumb_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_thumb_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_thumb_A_CTL.rotateOrder", 0)

			mc.xform("L_thumb_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_B_CTL"):
			if not mc.getAttr("L_thumb_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_thumb_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_thumb_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_thumb_B_CTL.rotateOrder", 0)

			mc.xform("L_thumb_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_C_CTL"):
			if not mc.getAttr("L_thumb_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_thumb_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_thumb_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_thumb_C_CTL.rotateOrder", 0)

			mc.xform("L_thumb_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_A_CTL"):
			if not mc.getAttr("L_index_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_index_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_index_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_A_CTL.rotateOrder", 0)

			mc.xform("L_index_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_B_CTL"):
			if not mc.getAttr("L_index_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_index_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_index_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_B_CTL.rotateOrder", 0)

			mc.xform("L_index_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_C_CTL"):
			if not mc.getAttr("L_index_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_index_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_index_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_C_CTL.rotateOrder", 0)

			mc.xform("L_index_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_D_CTL"):
			if not mc.getAttr("L_index_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_index_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_index_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_D_CTL.rotateOrder", 0)

			mc.xform("L_index_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_A_CTL"):
			if not mc.getAttr("L_middle_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_middle_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_middle_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_A_CTL.rotateOrder", 0)

			mc.xform("L_middle_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_B_CTL"):
			if not mc.getAttr("L_middle_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_middle_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_middle_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_B_CTL.rotateOrder", 0)

			mc.xform("L_middle_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_C_CTL"):
			if not mc.getAttr("L_middle_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_middle_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_middle_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_C_CTL.rotateOrder", 0)

			mc.xform("L_middle_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_D_CTL"):
			if not mc.getAttr("L_middle_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_middle_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_middle_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_D_CTL.rotateOrder", 0)

			mc.xform("L_middle_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_A_CTL"):
			if not mc.getAttr("L_ring_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_ring_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_ring_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_A_CTL.rotateOrder", 0)

			mc.xform("L_ring_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_B_CTL"):
			if not mc.getAttr("L_ring_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_ring_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_ring_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_B_CTL.rotateOrder", 0)

			mc.xform("L_ring_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_C_CTL"):
			if not mc.getAttr("L_ring_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_ring_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_ring_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_C_CTL.rotateOrder", 0)

			mc.xform("L_ring_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_D_CTL"):
			if not mc.getAttr("L_ring_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_ring_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_ring_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_D_CTL.rotateOrder", 0)

			mc.xform("L_ring_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_A_CTL"):
			if not mc.getAttr("L_pinky_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_pinky_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_pinky_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_A_CTL.rotateOrder", 0)

			mc.xform("L_pinky_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_B_CTL"):
			if not mc.getAttr("L_pinky_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_pinky_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_pinky_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_B_CTL.rotateOrder", 0)

			mc.xform("L_pinky_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_C_CTL"):
			if not mc.getAttr("L_pinky_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_pinky_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_pinky_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_C_CTL.rotateOrder", 0)

			mc.xform("L_pinky_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_D_CTL"):
			if not mc.getAttr("L_pinky_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_pinky_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_pinky_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_D_CTL.rotateOrder", 0)

			mc.xform("L_pinky_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_hand_CTL"):
			if not mc.getAttr("L_hand_CTL.mirrorMode", l=1):
				mc.setAttr("L_hand_CTL.mirrorMode", 0)

			if not mc.getAttr("L_hand_CTL.rotateOrder", l=1):
				mc.setAttr("L_hand_CTL.rotateOrder", 0)

			mc.xform("L_hand_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_hand_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_hand_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_D_OFF_CTL"):
			if not mc.getAttr("C_head_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_head_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_head_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_C_OFF_CTL"):
			if not mc.getAttr("C_head_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_head_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_head_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_B_OFF_CTL"):
			if not mc.getAttr("C_head_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_head_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_head_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_A_OFF_CTL"):
			if not mc.getAttr("C_head_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_head_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_head_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_CTL"):
			if not mc.getAttr("C_head_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_head_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("C_head_CTL.mirrorMode", l=1):
				mc.setAttr("C_head_CTL.mirrorMode", 0)

			if not mc.getAttr("C_head_CTL.rotateOrder", l=1):
				mc.setAttr("C_head_CTL.rotateOrder", 0)

			mc.xform("C_head_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neckBase_D_OFF_CTL"):
			if not mc.getAttr("C_neckBase_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_neckBase_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_neckBase_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neckBase_C_OFF_CTL"):
			if not mc.getAttr("C_neckBase_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_neckBase_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_neckBase_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neckBase_B_OFF_CTL"):
			if not mc.getAttr("C_neckBase_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_neckBase_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_neckBase_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neckBase_A_OFF_CTL"):
			if not mc.getAttr("C_neckBase_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_neckBase_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_neckBase_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neckBase_CTL"):
			if not mc.getAttr("C_neckBase_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_neckBase_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("C_neckBase_CTL.mirrorMode", l=1):
				mc.setAttr("C_neckBase_CTL.mirrorMode", 0)

			if not mc.getAttr("C_neckBase_CTL.rotateOrder", l=1):
				mc.setAttr("C_neckBase_CTL.rotateOrder", 0)

			mc.xform("C_neckBase_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neckBase_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midNeck_D_OFF_CTL"):
			if not mc.getAttr("C_midNeck_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midNeck_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midNeck_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midNeck_C_OFF_CTL"):
			if not mc.getAttr("C_midNeck_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midNeck_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midNeck_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midNeck_B_OFF_CTL"):
			if not mc.getAttr("C_midNeck_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midNeck_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midNeck_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midNeck_A_OFF_CTL"):
			if not mc.getAttr("C_midNeck_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midNeck_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midNeck_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midNeck_CTL"):
			if not mc.getAttr("C_midNeck_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_midNeck_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_midNeck_CTL.mirrorMode", l=1):
				mc.setAttr("C_midNeck_CTL.mirrorMode", 0)

			if not mc.getAttr("C_midNeck_CTL.rotateOrder", l=1):
				mc.setAttr("C_midNeck_CTL.rotateOrder", 0)

			mc.xform("C_midNeck_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midNeck_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_FK_A_CTL"):
			if not mc.getAttr("C_neck_FK_A_CTL.mirrorMode", l=1):
				mc.setAttr("C_neck_FK_A_CTL.mirrorMode", 0)

			if not mc.getAttr("C_neck_FK_A_CTL.rotateOrder", l=1):
				mc.setAttr("C_neck_FK_A_CTL.rotateOrder", 0)

			mc.xform("C_neck_FK_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_FK_B_CTL"):
			if not mc.getAttr("C_neck_FK_B_CTL.mirrorMode", l=1):
				mc.setAttr("C_neck_FK_B_CTL.mirrorMode", 0)

			if not mc.getAttr("C_neck_FK_B_CTL.rotateOrder", l=1):
				mc.setAttr("C_neck_FK_B_CTL.rotateOrder", 0)

			mc.xform("C_neck_FK_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_FK_C_CTL"):
			if not mc.getAttr("C_neck_FK_C_CTL.mirrorMode", l=1):
				mc.setAttr("C_neck_FK_C_CTL.mirrorMode", 0)

			if not mc.getAttr("C_neck_FK_C_CTL.rotateOrder", l=1):
				mc.setAttr("C_neck_FK_C_CTL.rotateOrder", 0)

			mc.xform("C_neck_FK_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_FK_D_CTL"):
			if not mc.getAttr("C_neck_FK_D_CTL.mirrorMode", l=1):
				mc.setAttr("C_neck_FK_D_CTL.mirrorMode", 0)

			if not mc.getAttr("C_neck_FK_D_CTL.rotateOrder", l=1):
				mc.setAttr("C_neck_FK_D_CTL.rotateOrder", 0)

			mc.xform("C_neck_FK_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_FK_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_jaw_CTL"):
			if not mc.getAttr("C_jaw_CTL.mirrorMode", l=1):
				mc.setAttr("C_jaw_CTL.mirrorMode", 0)

			if not mc.getAttr("C_jaw_CTL.rotateOrder", l=1):
				mc.setAttr("C_jaw_CTL.rotateOrder", 0)

			mc.xform("C_jaw_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_FK_CTL"):
			if not mc.getAttr("C_head_FK_CTL.mirrorMode", l=1):
				mc.setAttr("C_head_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("C_head_FK_CTL.rotateOrder", l=1):
				mc.setAttr("C_head_FK_CTL.rotateOrder", 0)

			mc.xform("C_head_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_top_CTL"):
			if not mc.getAttr("C_head_top_CTL.mirrorMode", l=1):
				mc.setAttr("C_head_top_CTL.mirrorMode", 0)

			if not mc.getAttr("C_head_top_CTL.rotateOrder", l=1):
				mc.setAttr("C_head_top_CTL.rotateOrder", 0)

			mc.xform("C_head_top_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_top_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_top_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_left_CTL"):
			if not mc.getAttr("C_head_left_CTL.mirrorMode", l=1):
				mc.setAttr("C_head_left_CTL.mirrorMode", 0)

			if not mc.getAttr("C_head_left_CTL.rotateOrder", l=1):
				mc.setAttr("C_head_left_CTL.rotateOrder", 0)

			mc.xform("C_head_left_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_left_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_left_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_right_CTL"):
			if not mc.getAttr("C_head_right_CTL.mirrorMode", l=1):
				mc.setAttr("C_head_right_CTL.mirrorMode", 0)

			if not mc.getAttr("C_head_right_CTL.rotateOrder", l=1):
				mc.setAttr("C_head_right_CTL.rotateOrder", 0)

			mc.xform("C_head_right_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_right_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_right_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_01_D_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_01_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_01_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_01_D_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_01_D_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_01_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_01_C_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_01_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_01_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_01_C_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_01_C_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_01_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_01_B_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_01_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_01_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_01_B_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_01_B_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_01_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_01_A_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_01_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_01_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_01_A_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_01_A_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_01_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_01_CTL"):
			if not mc.getAttr("R_shoulder_shaper_01_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_shoulder_shaper_01_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_shoulder_shaper_01_CTL.mirrorMode", l=1):
				mc.setAttr("R_shoulder_shaper_01_CTL.mirrorMode", 0)

			if not mc.getAttr("R_shoulder_shaper_01_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_01_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_01_CTL", a=1, t=[-1.4210854715202004e-14, 2.842170943040401e-14, 0.0])
			mc.xform("R_shoulder_shaper_01_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_shoulder_shaper_01_CTL", r=1, s=[0.9999999999999997, 1.0, 0.9999999999999996])

		if mc.objExists("R_elbow_shaper_01_D_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_01_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_01_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_01_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_01_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_01_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_01_C_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_01_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_01_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_01_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_01_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_01_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_01_B_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_01_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_01_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_01_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_01_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_01_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_01_A_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_01_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_01_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_01_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_01_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_01_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_01_CTL"):
			if not mc.getAttr("R_elbow_shaper_01_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_elbow_shaper_01_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_elbow_shaper_01_CTL.mirrorMode", l=1):
				mc.setAttr("R_elbow_shaper_01_CTL.mirrorMode", 0)

			if not mc.getAttr("R_elbow_shaper_01_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_01_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_01_CTL", a=1, t=[-1.4210854715202004e-14, 0.0, -1.7763568394002505e-15])
			mc.xform("R_elbow_shaper_01_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_01_CTL", r=1, s=[0.9999999999999999, 1.0, 0.9999999999999998])

		if mc.objExists("R_shoulder_shaper_02_D_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_02_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_02_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_02_D_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_02_D_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_02_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_02_C_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_02_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_02_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_02_C_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_02_C_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_02_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_02_B_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_02_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_02_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_02_B_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_02_B_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_02_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_02_A_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_02_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_02_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_02_A_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_02_A_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_02_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_02_CTL"):
			if not mc.getAttr("R_shoulder_shaper_02_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_shoulder_shaper_02_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_shoulder_shaper_02_CTL.mirrorMode", l=1):
				mc.setAttr("R_shoulder_shaper_02_CTL.mirrorMode", 0)

			if not mc.getAttr("R_shoulder_shaper_02_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_02_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_02_CTL", a=1, t=[-7.105427357601002e-15, 2.842170943040401e-14, -1.7763568394002505e-15])
			mc.xform("R_shoulder_shaper_02_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_shoulder_shaper_02_CTL", r=1, s=[0.9999999999999996, 1.0000000000000002, 0.9999999999999998])

		if mc.objExists("R_elbow_shaper_02_D_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_02_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_02_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_02_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_02_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_02_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_02_C_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_02_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_02_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_02_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_02_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_02_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_02_B_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_02_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_02_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_02_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_02_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_02_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_02_A_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_02_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_02_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_02_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_02_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_02_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_02_CTL"):
			if not mc.getAttr("R_elbow_shaper_02_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_elbow_shaper_02_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_elbow_shaper_02_CTL.mirrorMode", l=1):
				mc.setAttr("R_elbow_shaper_02_CTL.mirrorMode", 0)

			if not mc.getAttr("R_elbow_shaper_02_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_02_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_02_CTL", a=1, t=[-1.4210854715202004e-14, 2.842170943040401e-14, 1.7763568394002505e-15])
			mc.xform("R_elbow_shaper_02_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_02_CTL", r=1, s=[0.9999999999999998, 1.0, 0.9999999999999998])

		if mc.objExists("R_shoulder_shaper_03_D_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_03_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_03_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_03_D_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_03_D_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_03_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_03_C_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_03_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_03_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_03_C_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_03_C_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_03_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_03_B_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_03_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_03_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_03_B_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_03_B_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_03_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_03_A_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_03_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_03_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_03_A_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_03_A_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_03_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_03_CTL"):
			if not mc.getAttr("R_shoulder_shaper_03_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_shoulder_shaper_03_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_shoulder_shaper_03_CTL.mirrorMode", l=1):
				mc.setAttr("R_shoulder_shaper_03_CTL.mirrorMode", 0)

			if not mc.getAttr("R_shoulder_shaper_03_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_03_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_03_CTL", a=1, t=[1.4210854715202004e-14, 2.842170943040401e-14, -8.881784197001252e-16])
			mc.xform("R_shoulder_shaper_03_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_shoulder_shaper_03_CTL", r=1, s=[0.9999999999999998, 0.9999999999999999, 0.9999999999999998])

		if mc.objExists("R_elbow_shaper_03_D_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_03_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_03_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_03_D_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_03_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_03_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_03_C_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_03_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_03_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_03_C_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_03_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_03_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_03_B_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_03_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_03_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_03_B_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_03_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_03_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_03_A_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_03_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_03_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_03_A_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_03_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_03_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_03_CTL"):
			if not mc.getAttr("R_elbow_shaper_03_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_elbow_shaper_03_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_elbow_shaper_03_CTL.mirrorMode", l=1):
				mc.setAttr("R_elbow_shaper_03_CTL.mirrorMode", 0)

			if not mc.getAttr("R_elbow_shaper_03_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_03_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_03_CTL", a=1, t=[-1.4210854715202004e-14, 2.842170943040401e-14, -5.329070518200751e-15])
			mc.xform("R_elbow_shaper_03_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_03_CTL", r=1, s=[0.9999999999999998, 1.0, 0.9999999999999998])

		if mc.objExists("R_shoulder_shaper_04_D_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_04_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_04_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_04_D_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, -8.881784197001252e-16])
			mc.xform("R_shoulder_shaper_04_D_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_04_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_04_C_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_04_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_04_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_04_C_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 8.881784197001252e-16])
			mc.xform("R_shoulder_shaper_04_C_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_04_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_04_B_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_04_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_04_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_04_B_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, -8.881784197001252e-16])
			mc.xform("R_shoulder_shaper_04_B_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_04_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_04_A_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_04_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_04_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_04_A_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 8.881784197001252e-16])
			mc.xform("R_shoulder_shaper_04_A_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_04_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_04_CTL"):
			if not mc.getAttr("R_shoulder_shaper_04_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_shoulder_shaper_04_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_shoulder_shaper_04_CTL.mirrorMode", l=1):
				mc.setAttr("R_shoulder_shaper_04_CTL.mirrorMode", 0)

			if not mc.getAttr("R_shoulder_shaper_04_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_04_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_04_CTL", a=1, t=[0.0, 0.0, 2.6645352591003757e-15])
			mc.xform("R_shoulder_shaper_04_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_shoulder_shaper_04_CTL", r=1, s=[0.9999999999999997, 1.0, 0.9999999999999996])

		if mc.objExists("R_elbow_shaper_04_D_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_04_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_04_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_04_D_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_04_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_04_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_04_C_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_04_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_04_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_04_C_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_04_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_04_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_04_B_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_04_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_04_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_04_B_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_04_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_04_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_04_A_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_04_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_04_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_04_A_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_04_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_04_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_04_CTL"):
			if not mc.getAttr("R_elbow_shaper_04_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_elbow_shaper_04_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_elbow_shaper_04_CTL.mirrorMode", l=1):
				mc.setAttr("R_elbow_shaper_04_CTL.mirrorMode", 0)

			if not mc.getAttr("R_elbow_shaper_04_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_04_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_04_CTL", a=1, t=[-1.4210854715202004e-14, 2.842170943040401e-14, -1.0658141036401503e-14])
			mc.xform("R_elbow_shaper_04_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_04_CTL", r=1, s=[0.9999999999999998, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_05_D_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_05_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_05_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_05_D_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_05_D_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_05_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_05_C_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_05_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_05_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_05_C_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_05_C_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_05_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_05_B_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_05_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_05_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_05_B_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_05_B_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_05_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_05_A_OFF_CTL"):
			if not mc.getAttr("R_shoulder_shaper_05_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_05_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_05_A_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_shoulder_shaper_05_A_OFF_CTL", a=1, ro=[-1.4701261201899824e-47, 3.1805546814635168e-15, -5.29668755766019e-31])
			mc.xform("R_shoulder_shaper_05_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_shaper_05_CTL"):
			if not mc.getAttr("R_shoulder_shaper_05_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_shoulder_shaper_05_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_shoulder_shaper_05_CTL.mirrorMode", l=1):
				mc.setAttr("R_shoulder_shaper_05_CTL.mirrorMode", 0)

			if not mc.getAttr("R_shoulder_shaper_05_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_shaper_05_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_shaper_05_CTL", a=1, t=[1.4210854715202004e-14, 2.842170943040401e-14, -7.105427357601002e-15])
			mc.xform("R_shoulder_shaper_05_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_shoulder_shaper_05_CTL", r=1, s=[0.9999999999999998, 1.0, 0.9999999999999996])

		if mc.objExists("R_elbow_shaper_05_D_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_05_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_05_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_05_D_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_05_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_05_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_05_C_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_05_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_05_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_05_C_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_05_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_05_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_05_B_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_05_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_05_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_05_B_OFF_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_05_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_05_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_05_A_OFF_CTL"):
			if not mc.getAttr("R_elbow_shaper_05_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_05_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_05_A_OFF_CTL", a=1, t=[0.0, 1.4210854715202004e-14, 0.0])
			mc.xform("R_elbow_shaper_05_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_05_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbow_shaper_05_CTL"):
			if not mc.getAttr("R_elbow_shaper_05_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_elbow_shaper_05_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_elbow_shaper_05_CTL.mirrorMode", l=1):
				mc.setAttr("R_elbow_shaper_05_CTL.mirrorMode", 0)

			if not mc.getAttr("R_elbow_shaper_05_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbow_shaper_05_CTL.rotateOrder", 0)

			mc.xform("R_elbow_shaper_05_CTL", a=1, t=[-1.4210854715202004e-14, 2.842170943040401e-14, 0.0])
			mc.xform("R_elbow_shaper_05_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbow_shaper_05_CTL", r=1, s=[0.9999999999999998, 1.0, 1.0])

		if mc.objExists("R_scapulaCtrl_CTL"):
			if not mc.getAttr("R_scapulaCtrl_CTL.mirrorMode", l=1):
				mc.setAttr("R_scapulaCtrl_CTL.mirrorMode", 0)

			if not mc.getAttr("R_scapulaCtrl_CTL.rotateOrder", l=1):
				mc.setAttr("R_scapulaCtrl_CTL.rotateOrder", 0)

			mc.xform("R_scapulaCtrl_CTL", a=1, t=[-3.552713678800501e-15, 0.0, 3.552713678800501e-15])
			mc.xform("R_scapulaCtrl_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_scapulaCtrl_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_scapulaTarget_CTL"):
			if not mc.getAttr("R_scapulaTarget_CTL.mirrorMode", l=1):
				mc.setAttr("R_scapulaTarget_CTL.mirrorMode", 0)

			if not mc.getAttr("R_scapulaTarget_CTL.rotateOrder", l=1):
				mc.setAttr("R_scapulaTarget_CTL.rotateOrder", 0)

			mc.xform("R_scapulaTarget_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_scapulaTarget_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_scapulaTarget_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_scapulaChest_CTL"):
			if not mc.getAttr("R_scapulaChest_CTL.mirrorMode", l=1):
				mc.setAttr("R_scapulaChest_CTL.mirrorMode", 0)

			if not mc.getAttr("R_scapulaChest_CTL.rotateOrder", l=1):
				mc.setAttr("R_scapulaChest_CTL.rotateOrder", 0)

			mc.xform("R_scapulaChest_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_scapulaChest_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_scapulaChest_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulderFk_CTL"):
			if not mc.getAttr("R_shoulderFk_CTL.mirrorMode", l=1):
				mc.setAttr("R_shoulderFk_CTL.mirrorMode", 0)

			if not mc.getAttr("R_shoulderFk_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulderFk_CTL.rotateOrder", 0)

			mc.xform("R_shoulderFk_CTL", a=1, t=[0.0, 0.0, 1.7763568394002505e-15])
			mc.xform("R_shoulderFk_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_shoulderFk_CTL", r=1, s=[0.9999999999999998, 1.0, 0.9999999999999997])

		if mc.objExists("R_elbowFk_CTL"):
			if not mc.getAttr("R_elbowFk_CTL.mirrorMode", l=1):
				mc.setAttr("R_elbowFk_CTL.mirrorMode", 0)

			if not mc.getAttr("R_elbowFk_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbowFk_CTL.rotateOrder", 0)

			mc.xform("R_elbowFk_CTL", a=1, t=[0.0, -2.842170943040401e-14, -1.7763568394002505e-15])
			mc.xform("R_elbowFk_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbowFk_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, 1.0])

		if mc.objExists("R_wristFk_CTL"):
			if not mc.getAttr("R_wristFk_CTL.mirrorMode", l=1):
				mc.setAttr("R_wristFk_CTL.mirrorMode", 0)

			if not mc.getAttr("R_wristFk_CTL.rotateOrder", l=1):
				mc.setAttr("R_wristFk_CTL.rotateOrder", 0)

			mc.xform("R_wristFk_CTL", a=1, t=[0.0, 0.0, -1.262177448353619e-29])
			mc.xform("R_wristFk_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_wristFk_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_handIk_D_OFF_CTL"):
			if not mc.getAttr("R_handIk_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_handIk_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_handIk_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_handIk_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_handIk_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_handIk_C_OFF_CTL"):
			if not mc.getAttr("R_handIk_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_handIk_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_handIk_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_handIk_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_handIk_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_handIk_B_OFF_CTL"):
			if not mc.getAttr("R_handIk_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_handIk_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_handIk_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_handIk_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_handIk_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_handIk_A_OFF_CTL"):
			if not mc.getAttr("R_handIk_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_handIk_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_handIk_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_handIk_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_handIk_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_handIk_CTL"):
			if not mc.getAttr("R_handIk_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_handIk_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("R_handIk_CTL.mirrorMode", l=1):
				mc.setAttr("R_handIk_CTL.mirrorMode", 0)

			if not mc.getAttr("R_handIk_CTL.rotateOrder", l=1):
				mc.setAttr("R_handIk_CTL.rotateOrder", 0)

			mc.xform("R_handIk_CTL", a=1, t=[0.0, 0.0, -1.262177448353619e-29])
			mc.xform("R_handIk_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_handIk_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lwrArmTwist_D_OFF_CTL"):
			if not mc.getAttr("R_lwrArmTwist_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmTwist_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmTwist_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmTwist_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmTwist_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lwrArmTwist_C_OFF_CTL"):
			if not mc.getAttr("R_lwrArmTwist_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmTwist_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmTwist_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmTwist_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmTwist_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lwrArmTwist_B_OFF_CTL"):
			if not mc.getAttr("R_lwrArmTwist_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmTwist_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmTwist_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmTwist_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmTwist_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lwrArmTwist_A_OFF_CTL"):
			if not mc.getAttr("R_lwrArmTwist_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmTwist_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmTwist_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmTwist_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmTwist_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lwrArmTwist_CTL"):
			if not mc.getAttr("R_lwrArmTwist_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lwrArmTwist_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lwrArmTwist_CTL.mirrorMode", l=1):
				mc.setAttr("R_lwrArmTwist_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lwrArmTwist_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmTwist_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmTwist_CTL", a=1, t=[0.0, 0.0, -1.262177448353619e-29])
			mc.xform("R_lwrArmTwist_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmTwist_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbowUpVectorIk_CTL"):
			if not mc.getAttr("R_elbowUpVectorIk_CTL.mirrorMode", l=1):
				mc.setAttr("R_elbowUpVectorIk_CTL.mirrorMode", 0)

			if not mc.getAttr("R_elbowUpVectorIk_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbowUpVectorIk_CTL.rotateOrder", 0)

			mc.xform("R_elbowUpVectorIk_CTL", a=1, t=[-2.1316282072803006e-14, 0.0, 0.0])
			mc.xform("R_elbowUpVectorIk_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("R_elbowUpVectorIk_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_clavicle_D_OFF_CTL"):
			if not mc.getAttr("R_clavicle_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_clavicle_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_clavicle_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_clavicle_D_OFF_CTL", a=1, ro=[-8.3797188850829e-46, -2.8624992133171654e-14, 3.3545687865181204e-30])
			mc.xform("R_clavicle_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_clavicle_C_OFF_CTL"):
			if not mc.getAttr("R_clavicle_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_clavicle_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_clavicle_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_clavicle_C_OFF_CTL", a=1, ro=[-8.3797188850829e-46, -2.8624992133171654e-14, 3.3545687865181204e-30])
			mc.xform("R_clavicle_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_clavicle_B_OFF_CTL"):
			if not mc.getAttr("R_clavicle_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_clavicle_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_clavicle_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_clavicle_B_OFF_CTL", a=1, ro=[-8.3797188850829e-46, -2.8624992133171654e-14, 3.3545687865181204e-30])
			mc.xform("R_clavicle_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_clavicle_A_OFF_CTL"):
			if not mc.getAttr("R_clavicle_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_clavicle_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_clavicle_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_clavicle_A_OFF_CTL", a=1, ro=[-8.3797188850829e-46, -2.8624992133171654e-14, 3.3545687865181204e-30])
			mc.xform("R_clavicle_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_clavicle_CTL"):
			if not mc.getAttr("R_clavicle_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_clavicle_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_clavicle_CTL.mirrorMode", l=1):
				mc.setAttr("R_clavicle_CTL.mirrorMode", 0)

			if not mc.getAttr("R_clavicle_CTL.rotateOrder", l=1):
				mc.setAttr("R_clavicle_CTL.rotateOrder", 0)

			mc.xform("R_clavicle_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_clavicle_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_clavicle_CTL", r=1, s=[0.9999999999999998, 1.0, 0.9999999999999998])

		if mc.objExists("R_uprArmRibbonMid_D_OFF_CTL"):
			if not mc.getAttr("R_uprArmRibbonMid_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_uprArmRibbonMid_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_uprArmRibbonMid_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_uprArmRibbonMid_D_OFF_CTL", a=1, ro=[2.2069531490249009e-32, -4.134721085902572e-14, 4.943575053816178e-30])
			mc.xform("R_uprArmRibbonMid_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_uprArmRibbonMid_C_OFF_CTL"):
			if not mc.getAttr("R_uprArmRibbonMid_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_uprArmRibbonMid_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_uprArmRibbonMid_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_uprArmRibbonMid_C_OFF_CTL", a=1, ro=[2.2069531490249009e-32, -4.134721085902572e-14, 4.943575053816178e-30])
			mc.xform("R_uprArmRibbonMid_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_uprArmRibbonMid_B_OFF_CTL"):
			if not mc.getAttr("R_uprArmRibbonMid_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_uprArmRibbonMid_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_uprArmRibbonMid_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_uprArmRibbonMid_B_OFF_CTL", a=1, ro=[2.2069531490249009e-32, -4.134721085902572e-14, 4.943575053816178e-30])
			mc.xform("R_uprArmRibbonMid_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_uprArmRibbonMid_A_OFF_CTL"):
			if not mc.getAttr("R_uprArmRibbonMid_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_uprArmRibbonMid_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_uprArmRibbonMid_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_uprArmRibbonMid_A_OFF_CTL", a=1, ro=[2.2069531490249009e-32, -4.134721085902572e-14, 4.943575053816178e-30])
			mc.xform("R_uprArmRibbonMid_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_uprArmRibbonMid_CTL"):
			if not mc.getAttr("R_uprArmRibbonMid_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_uprArmRibbonMid_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_uprArmRibbonMid_CTL.mirrorMode", l=1):
				mc.setAttr("R_uprArmRibbonMid_CTL.mirrorMode", 0)

			if not mc.getAttr("R_uprArmRibbonMid_CTL.rotateOrder", l=1):
				mc.setAttr("R_uprArmRibbonMid_CTL.rotateOrder", 0)

			mc.xform("R_uprArmRibbonMid_CTL", a=1, t=[0.0, 2.842170943040401e-14, -8.881784197001252e-16])
			mc.xform("R_uprArmRibbonMid_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_uprArmRibbonMid_CTL", r=1, s=[0.9999999999999998, 0.9999999999999999, 0.9999999999999997])

		if mc.objExists("R_elbowRibbon_D_OFF_CTL"):
			if not mc.getAttr("R_elbowRibbon_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbowRibbon_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbowRibbon_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbowRibbon_D_OFF_CTL", a=1, ro=[-4.2543688829716624e-47, -6.311413196029167e-15, 7.724336021587777e-31])
			mc.xform("R_elbowRibbon_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbowRibbon_C_OFF_CTL"):
			if not mc.getAttr("R_elbowRibbon_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbowRibbon_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbowRibbon_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbowRibbon_C_OFF_CTL", a=1, ro=[-4.2543688829716624e-47, -6.311413196029167e-15, 7.724336021587777e-31])
			mc.xform("R_elbowRibbon_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbowRibbon_B_OFF_CTL"):
			if not mc.getAttr("R_elbowRibbon_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbowRibbon_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbowRibbon_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbowRibbon_B_OFF_CTL", a=1, ro=[-4.2543688829716624e-47, -6.311413196029167e-15, 7.724336021587777e-31])
			mc.xform("R_elbowRibbon_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbowRibbon_A_OFF_CTL"):
			if not mc.getAttr("R_elbowRibbon_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbowRibbon_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_elbowRibbon_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_elbowRibbon_A_OFF_CTL", a=1, ro=[-4.2543688829716624e-47, -6.311413196029167e-15, 7.724336021587777e-31])
			mc.xform("R_elbowRibbon_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_elbowRibbon_CTL"):
			if not mc.getAttr("R_elbowRibbon_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_elbowRibbon_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_elbowRibbon_CTL.mirrorMode", l=1):
				mc.setAttr("R_elbowRibbon_CTL.mirrorMode", 0)

			if not mc.getAttr("R_elbowRibbon_CTL.rotateOrder", l=1):
				mc.setAttr("R_elbowRibbon_CTL.rotateOrder", 0)

			mc.xform("R_elbowRibbon_CTL", a=1, t=[0.0, -2.842170943040401e-14, 1.7763568394002505e-15])
			mc.xform("R_elbowRibbon_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_elbowRibbon_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lwrArmRibbonMid_D_OFF_CTL"):
			if not mc.getAttr("R_lwrArmRibbonMid_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmRibbonMid_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmRibbonMid_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmRibbonMid_D_OFF_CTL", a=1, ro=[-5.488470848709268e-46, 2.2263882770244617e-14, -2.8249000307521015e-30])
			mc.xform("R_lwrArmRibbonMid_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lwrArmRibbonMid_C_OFF_CTL"):
			if not mc.getAttr("R_lwrArmRibbonMid_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmRibbonMid_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmRibbonMid_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmRibbonMid_C_OFF_CTL", a=1, ro=[-5.488470848709268e-46, 2.2263882770244617e-14, -2.8249000307521015e-30])
			mc.xform("R_lwrArmRibbonMid_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lwrArmRibbonMid_B_OFF_CTL"):
			if not mc.getAttr("R_lwrArmRibbonMid_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmRibbonMid_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmRibbonMid_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmRibbonMid_B_OFF_CTL", a=1, ro=[-5.488470848709268e-46, 2.2263882770244617e-14, -2.8249000307521015e-30])
			mc.xform("R_lwrArmRibbonMid_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lwrArmRibbonMid_A_OFF_CTL"):
			if not mc.getAttr("R_lwrArmRibbonMid_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmRibbonMid_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmRibbonMid_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmRibbonMid_A_OFF_CTL", a=1, ro=[-5.488470848709268e-46, 2.2263882770244617e-14, -2.8249000307521015e-30])
			mc.xform("R_lwrArmRibbonMid_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lwrArmRibbonMid_CTL"):
			if not mc.getAttr("R_lwrArmRibbonMid_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lwrArmRibbonMid_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lwrArmRibbonMid_CTL.mirrorMode", l=1):
				mc.setAttr("R_lwrArmRibbonMid_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lwrArmRibbonMid_CTL.rotateOrder", l=1):
				mc.setAttr("R_lwrArmRibbonMid_CTL.rotateOrder", 0)

			mc.xform("R_lwrArmRibbonMid_CTL", a=1, t=[2.842170943040401e-14, 0.0, -3.552713678800501e-15])
			mc.xform("R_lwrArmRibbonMid_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lwrArmRibbonMid_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0000000000000002])

		if mc.objExists("R_arm_IK_switch_D_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_arm_IK_switch_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_arm_IK_switch_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_C_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_arm_IK_switch_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_arm_IK_switch_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_B_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_arm_IK_switch_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_arm_IK_switch_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_A_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_arm_IK_switch_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_arm_IK_switch_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_CTL"):
			if not mc.getAttr("R_arm_IK_switch_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_arm_IK_switch_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_arm_IK_switch_CTL.mirrorMode", l=1):
				mc.setAttr("R_arm_IK_switch_CTL.mirrorMode", 0)

			if not mc.getAttr("R_arm_IK_switch_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_CTL", a=1, t=[-19.999999999999986, 10.0, 3.673940397442051e-15])
			mc.xform("R_arm_IK_switch_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_arm_IK_switch_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_innerBall_CTL"):
			if not mc.getAttr("R_innerBall_CTL.mirrorMode", l=1):
				mc.setAttr("R_innerBall_CTL.mirrorMode", 0)

			if not mc.getAttr("R_innerBall_CTL.rotateOrder", l=1):
				mc.setAttr("R_innerBall_CTL.rotateOrder", 0)

			mc.xform("R_innerBall_CTL", a=1, t=[0.0, 8.410644271317214e-09, 0.0])
			mc.xform("R_innerBall_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_innerBall_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_outterBall_CTL"):
			if not mc.getAttr("R_outterBall_CTL.mirrorMode", l=1):
				mc.setAttr("R_outterBall_CTL.mirrorMode", 0)

			if not mc.getAttr("R_outterBall_CTL.rotateOrder", l=1):
				mc.setAttr("R_outterBall_CTL.rotateOrder", 0)

			mc.xform("R_outterBall_CTL", a=1, t=[0.0, 8.410644292133895e-09, 0.0])
			mc.xform("R_outterBall_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_outterBall_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_heel_CTL"):
			if not mc.getAttr("R_heel_CTL.mirrorMode", l=1):
				mc.setAttr("R_heel_CTL.mirrorMode", 0)

			if not mc.getAttr("R_heel_CTL.rotateOrder", l=1):
				mc.setAttr("R_heel_CTL.rotateOrder", 0)

			mc.xform("R_heel_CTL", a=1, t=[0.0, 8.41064426437832e-09, 0.0])
			mc.xform("R_heel_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_heel_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toeTip_CTL"):
			if not mc.getAttr("R_toeTip_CTL.mirrorMode", l=1):
				mc.setAttr("R_toeTip_CTL.mirrorMode", 0)

			if not mc.getAttr("R_toeTip_CTL.rotateOrder", l=1):
				mc.setAttr("R_toeTip_CTL.rotateOrder", 0)

			mc.xform("R_toeTip_CTL", a=1, t=[-1.1102230246251565e-16, 8.410644278256107e-09, 0.0])
			mc.xform("R_toeTip_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_toeTip_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_reverseBall_CTL"):
			if not mc.getAttr("R_reverseBall_CTL.mirrorMode", l=1):
				mc.setAttr("R_reverseBall_CTL.mirrorMode", 0)

			if not mc.getAttr("R_reverseBall_CTL.rotateOrder", l=1):
				mc.setAttr("R_reverseBall_CTL.rotateOrder", 0)

			mc.xform("R_reverseBall_CTL", a=1, t=[0.0, 8.410644271317214e-09, 0.0])
			mc.xform("R_reverseBall_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_reverseBall_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ankleOffset_CTL"):
			if not mc.getAttr("R_ankleOffset_CTL.mirrorMode", l=1):
				mc.setAttr("R_ankleOffset_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ankleOffset_CTL.rotateOrder", l=1):
				mc.setAttr("R_ankleOffset_CTL.rotateOrder", 0)

			mc.xform("R_ankleOffset_CTL", a=1, t=[0.0, -1.9158935549157263e-07, 3.0998460773950835e-23])
			mc.xform("R_ankleOffset_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_ankleOffset_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_D_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_toe_IK_D_OFF_CTL", a=1, ro=[9.54166404439055e-15, -2.6483437788300953e-30, 3.180554681463517e-14])
			mc.xform("R_toe_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_C_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_toe_IK_C_OFF_CTL", a=1, ro=[9.54166404439055e-15, -2.6483437788300953e-30, 3.180554681463517e-14])
			mc.xform("R_toe_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_B_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_toe_IK_B_OFF_CTL", a=1, ro=[9.54166404439055e-15, -2.6483437788300953e-30, 3.180554681463517e-14])
			mc.xform("R_toe_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_A_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_toe_IK_A_OFF_CTL", a=1, ro=[9.54166404439055e-15, -2.6483437788300953e-30, 3.180554681463517e-14])
			mc.xform("R_toe_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_CTL"):
			if not mc.getAttr("R_toe_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_toe_IK_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_toe_IK_CTL.mirrorMode", l=1):
				mc.setAttr("R_toe_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_toe_IK_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_CTL", a=1, t=[0.0, 0.0, -8.410644271317214e-09])
			mc.xform("R_toe_IK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_toe_IK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_FK_CTL"):
			if not mc.getAttr("R_toe_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_toe_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_toe_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_FK_CTL.rotateOrder", 0)

			mc.xform("R_toe_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_toe_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_toe_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_01_D_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_01_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_01_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_01_D_OFF_CTL", a=1, t=[1.7763568394002505e-15, -1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_01_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_01_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_01_C_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_01_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_01_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_01_C_OFF_CTL", a=1, t=[-1.7763568394002505e-15, 1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_01_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_01_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_01_B_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_01_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_01_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_01_B_OFF_CTL", a=1, t=[1.7763568394002505e-15, -1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_01_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_01_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_01_A_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_01_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_01_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_01_A_OFF_CTL", a=1, t=[-1.7763568394002505e-15, 1.1102230246251565e-16, 2.220446049250313e-16])
			mc.xform("R_upLeg_shaper_01_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_01_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_01_CTL"):
			if not mc.getAttr("R_upLeg_shaper_01_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upLeg_shaper_01_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upLeg_shaper_01_CTL.mirrorMode", l=1):
				mc.setAttr("R_upLeg_shaper_01_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upLeg_shaper_01_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_01_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_01_CTL", a=1, t=[0.0, -4.440892098500626e-16, 8.881784197001252e-16])
			mc.xform("R_upLeg_shaper_01_CTL", a=1, ro=[-180.0, -2.7586914362813492e-31, 3.975693351829396e-15])
			mc.xform("R_upLeg_shaper_01_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_loLeg_shaper_01_D_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_01_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_01_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_01_D_OFF_CTL", a=1, t=[0.0, 0.0, -4.163336342344337e-17])
			mc.xform("R_loLeg_shaper_01_D_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_01_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_01_C_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_01_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_01_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_01_C_OFF_CTL", a=1, t=[0.0, 0.0, -4.163336342344337e-17])
			mc.xform("R_loLeg_shaper_01_C_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_01_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_01_B_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_01_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_01_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_01_B_OFF_CTL", a=1, t=[0.0, 0.0, -4.163336342344337e-17])
			mc.xform("R_loLeg_shaper_01_B_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_01_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_01_A_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_01_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_01_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_01_A_OFF_CTL", a=1, t=[0.0, 2.220446049250313e-16, -4.163336342344337e-17])
			mc.xform("R_loLeg_shaper_01_A_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_01_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_01_CTL"):
			if not mc.getAttr("R_loLeg_shaper_01_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_loLeg_shaper_01_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_loLeg_shaper_01_CTL.mirrorMode", l=1):
				mc.setAttr("R_loLeg_shaper_01_CTL.mirrorMode", 0)

			if not mc.getAttr("R_loLeg_shaper_01_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_01_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_01_CTL", a=1, t=[-8.881784197001252e-16, -4.440892098500626e-16, -1.5265566588595902e-16])
			mc.xform("R_loLeg_shaper_01_CTL", a=1, ro=[-180.0, 1.1927080055488186e-15, 1.8387581752210955e-15])
			mc.xform("R_loLeg_shaper_01_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_upLeg_shaper_02_D_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_02_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_02_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_02_D_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_02_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_02_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_02_C_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_02_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_02_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_02_C_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_02_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_02_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_02_B_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_02_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_02_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_02_B_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_02_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_02_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_02_A_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_02_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_02_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_02_A_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_02_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_02_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_02_CTL"):
			if not mc.getAttr("R_upLeg_shaper_02_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upLeg_shaper_02_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upLeg_shaper_02_CTL.mirrorMode", l=1):
				mc.setAttr("R_upLeg_shaper_02_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upLeg_shaper_02_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_02_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_02_CTL", a=1, t=[0.0, 0.0, 2.220446049250313e-16])
			mc.xform("R_upLeg_shaper_02_CTL", a=1, ro=[-180.0, -2.7586914362813492e-31, 3.975693351829396e-15])
			mc.xform("R_upLeg_shaper_02_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_loLeg_shaper_02_D_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_02_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_02_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_02_D_OFF_CTL", a=1, t=[1.3322676295501878e-15, 0.0, 1.1102230246251565e-16])
			mc.xform("R_loLeg_shaper_02_D_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_02_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_02_C_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_02_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_02_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_02_C_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, -5.551115123125783e-17])
			mc.xform("R_loLeg_shaper_02_C_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_02_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_02_B_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_02_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_02_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_02_B_OFF_CTL", a=1, t=[-8.881784197001252e-16, 0.0, -5.551115123125783e-17])
			mc.xform("R_loLeg_shaper_02_B_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_02_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_02_A_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_02_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_02_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_02_A_OFF_CTL", a=1, t=[1.3322676295501878e-15, 2.220446049250313e-16, 1.6653345369377348e-16])
			mc.xform("R_loLeg_shaper_02_A_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_02_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_02_CTL"):
			if not mc.getAttr("R_loLeg_shaper_02_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_loLeg_shaper_02_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_loLeg_shaper_02_CTL.mirrorMode", l=1):
				mc.setAttr("R_loLeg_shaper_02_CTL.mirrorMode", 0)

			if not mc.getAttr("R_loLeg_shaper_02_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_02_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_02_CTL", a=1, t=[8.881784197001252e-16, -4.440892098500626e-16, -1.5265566588595902e-16])
			mc.xform("R_loLeg_shaper_02_CTL", a=1, ro=[-180.0, 1.1927080055488186e-15, 1.8387581752210955e-15])
			mc.xform("R_loLeg_shaper_02_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_upLeg_shaper_03_D_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_03_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_03_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_03_D_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_03_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_03_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_03_C_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_03_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_03_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_03_C_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_03_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_03_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_03_B_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_03_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_03_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_03_B_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_03_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_03_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_03_A_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_03_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_03_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_03_A_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_03_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_03_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_03_CTL"):
			if not mc.getAttr("R_upLeg_shaper_03_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upLeg_shaper_03_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upLeg_shaper_03_CTL.mirrorMode", l=1):
				mc.setAttr("R_upLeg_shaper_03_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upLeg_shaper_03_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_03_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_03_CTL", a=1, t=[0.0, -4.440892098500626e-16, 0.0])
			mc.xform("R_upLeg_shaper_03_CTL", a=1, ro=[-180.0, -2.7586914362813492e-31, 3.975693351829396e-15])
			mc.xform("R_upLeg_shaper_03_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_loLeg_shaper_03_D_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_03_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_03_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_03_D_OFF_CTL", a=1, t=[4.440892098500626e-16, 0.0, 0.0])
			mc.xform("R_loLeg_shaper_03_D_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_03_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_03_C_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_03_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_03_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_03_C_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 0.0])
			mc.xform("R_loLeg_shaper_03_C_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_03_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_03_B_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_03_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_03_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_03_B_OFF_CTL", a=1, t=[4.440892098500626e-16, 0.0, 0.0])
			mc.xform("R_loLeg_shaper_03_B_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_03_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_03_A_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_03_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_03_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_03_A_OFF_CTL", a=1, t=[-4.440892098500626e-16, 2.220446049250313e-16, 0.0])
			mc.xform("R_loLeg_shaper_03_A_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_03_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_03_CTL"):
			if not mc.getAttr("R_loLeg_shaper_03_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_loLeg_shaper_03_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_loLeg_shaper_03_CTL.mirrorMode", l=1):
				mc.setAttr("R_loLeg_shaper_03_CTL.mirrorMode", 0)

			if not mc.getAttr("R_loLeg_shaper_03_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_03_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_03_CTL", a=1, t=[-8.881784197001252e-16, 0.0, 2.7755575615628914e-17])
			mc.xform("R_loLeg_shaper_03_CTL", a=1, ro=[180.0, 1.1927080055488188e-15, 1.4411888400381565e-15])
			mc.xform("R_loLeg_shaper_03_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0])

		if mc.objExists("R_upLeg_shaper_04_D_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_04_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_04_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_04_D_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_04_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_04_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_04_C_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_04_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_04_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_04_C_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_04_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_04_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_04_B_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_04_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_04_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_04_B_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_04_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_04_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_04_A_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_04_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_04_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_04_A_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_upLeg_shaper_04_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_04_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_04_CTL"):
			if not mc.getAttr("R_upLeg_shaper_04_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upLeg_shaper_04_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upLeg_shaper_04_CTL.mirrorMode", l=1):
				mc.setAttr("R_upLeg_shaper_04_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upLeg_shaper_04_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_04_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_04_CTL", a=1, t=[-8.881784197001252e-16, -4.440892098500626e-16, 0.0])
			mc.xform("R_upLeg_shaper_04_CTL", a=1, ro=[-180.0, -2.7586914362813492e-31, 3.975693351829396e-15])
			mc.xform("R_upLeg_shaper_04_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_loLeg_shaper_04_D_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_04_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_04_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_04_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_loLeg_shaper_04_D_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_04_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_04_C_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_04_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_04_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_04_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_loLeg_shaper_04_C_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_04_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_04_B_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_04_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_04_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_04_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_loLeg_shaper_04_B_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_04_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_04_A_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_04_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_04_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_04_A_OFF_CTL", a=1, t=[0.0, 0.0, -2.7755575615628914e-17])
			mc.xform("R_loLeg_shaper_04_A_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_04_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_04_CTL"):
			if not mc.getAttr("R_loLeg_shaper_04_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_loLeg_shaper_04_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_loLeg_shaper_04_CTL.mirrorMode", l=1):
				mc.setAttr("R_loLeg_shaper_04_CTL.mirrorMode", 0)

			if not mc.getAttr("R_loLeg_shaper_04_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_04_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_04_CTL", a=1, t=[6.661338147750939e-16, -4.440892098500626e-16, -1.3877787807814457e-17])
			mc.xform("R_loLeg_shaper_04_CTL", a=1, ro=[180.0, 1.1927080055488188e-15, 1.4411888400381565e-15])
			mc.xform("R_loLeg_shaper_04_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_upLeg_shaper_05_D_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_05_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_05_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_05_D_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 2.220446049250313e-16])
			mc.xform("R_upLeg_shaper_05_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_05_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_05_C_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_05_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_05_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_05_C_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, -2.220446049250313e-16])
			mc.xform("R_upLeg_shaper_05_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_05_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_05_B_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_05_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_05_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_05_B_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 2.220446049250313e-16])
			mc.xform("R_upLeg_shaper_05_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_05_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_05_A_OFF_CTL"):
			if not mc.getAttr("R_upLeg_shaper_05_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_05_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_05_A_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, -2.220446049250313e-16])
			mc.xform("R_upLeg_shaper_05_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upLeg_shaper_05_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_shaper_05_CTL"):
			if not mc.getAttr("R_upLeg_shaper_05_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upLeg_shaper_05_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upLeg_shaper_05_CTL.mirrorMode", l=1):
				mc.setAttr("R_upLeg_shaper_05_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upLeg_shaper_05_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_shaper_05_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_shaper_05_CTL", a=1, t=[8.881784197001252e-16, -4.440892098500626e-16, 4.440892098500626e-16])
			mc.xform("R_upLeg_shaper_05_CTL", a=1, ro=[-180.0, -2.7586914362813492e-31, 3.975693351829396e-15])
			mc.xform("R_upLeg_shaper_05_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_loLeg_shaper_05_D_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_05_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_05_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_05_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_loLeg_shaper_05_D_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_05_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_05_C_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_05_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_05_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_05_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_loLeg_shaper_05_C_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_05_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_05_B_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_05_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_05_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_05_B_OFF_CTL", a=1, t=[0.0, 0.0, 1.3877787807814457e-17])
			mc.xform("R_loLeg_shaper_05_B_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_05_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_05_A_OFF_CTL"):
			if not mc.getAttr("R_loLeg_shaper_05_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_05_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_05_A_OFF_CTL", a=1, t=[0.0, 0.0, 2.7755575615628914e-17])
			mc.xform("R_loLeg_shaper_05_A_OFF_CTL", a=1, ro=[1.3517357396219947e-14, -3.1805546814635168e-15, -3.7518203533426355e-31])
			mc.xform("R_loLeg_shaper_05_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_shaper_05_CTL"):
			if not mc.getAttr("R_loLeg_shaper_05_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_loLeg_shaper_05_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_loLeg_shaper_05_CTL.mirrorMode", l=1):
				mc.setAttr("R_loLeg_shaper_05_CTL.mirrorMode", 0)

			if not mc.getAttr("R_loLeg_shaper_05_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_shaper_05_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_shaper_05_CTL", a=1, t=[0.0, -2.220446049250313e-16, 1.3877787807814457e-17])
			mc.xform("R_loLeg_shaper_05_CTL", a=1, ro=[-180.0, 1.1927080055488186e-15, 1.8387581752210955e-15])
			mc.xform("R_loLeg_shaper_05_CTL", r=1, s=[1.0, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_upLeg_FK_CTL"):
			if not mc.getAttr("R_upLeg_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_upLeg_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upLeg_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_FK_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_FK_CTL", a=1, t=[0.0, -2.220446049250313e-16, 2.220446049250313e-16])
			mc.xform("R_upLeg_FK_CTL", a=1, ro=[1.1927080055488188e-15, -1.1927080055488188e-15, 6.311413196029166e-15])
			mc.xform("R_upLeg_FK_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0])

		if mc.objExists("R_loLeg_FK_CTL"):
			if not mc.getAttr("R_loLeg_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_loLeg_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_loLeg_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_FK_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_FK_CTL", a=1, t=[0.0, 0.0, -5.551115123125783e-17])
			mc.xform("R_loLeg_FK_CTL", a=1, ro=[0.0, 7.951386703658792e-16, 0.0])
			mc.xform("R_loLeg_FK_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0])

		if mc.objExists("R_legEnd_FK_CTL"):
			if not mc.getAttr("R_legEnd_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_legEnd_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_legEnd_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_legEnd_FK_CTL.rotateOrder", 0)

			mc.xform("R_legEnd_FK_CTL", a=1, t=[-3.3306690738754696e-16, 2.220446049250313e-16, 2.7755575615628914e-17])
			mc.xform("R_legEnd_FK_CTL", a=1, ro=[-3.975693351829396e-16, 7.951386703658792e-16, -2.758691436281349e-33])
			mc.xform("R_legEnd_FK_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0000000000000002])

		if mc.objExists("R_leg_IK_D_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_leg_IK_D_OFF_CTL", a=1, ro=[7.016709298534885e-15, 3.246114675024302e-14, 1.272221872585407e-14])
			mc.xform("R_leg_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_C_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_C_OFF_CTL", a=1, t=[0.0, 0.0, -2.465190328815662e-32])
			mc.xform("R_leg_IK_C_OFF_CTL", a=1, ro=[7.016709298534885e-15, 3.246114675024302e-14, 1.272221872585407e-14])
			mc.xform("R_leg_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_B_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_B_OFF_CTL", a=1, t=[0.0, 0.0, -2.465190328815662e-32])
			mc.xform("R_leg_IK_B_OFF_CTL", a=1, ro=[7.016709298534885e-15, 3.246114675024302e-14, 1.272221872585407e-14])
			mc.xform("R_leg_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_A_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_A_OFF_CTL", a=1, t=[1.1102230246251565e-16, 0.0, 2.465190328815662e-32])
			mc.xform("R_leg_IK_A_OFF_CTL", a=1, ro=[7.016709298534885e-15, 3.246114675024302e-14, 1.272221872585407e-14])
			mc.xform("R_leg_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_CTL"):
			if not mc.getAttr("R_leg_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_leg_IK_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("R_leg_IK_CTL.mirrorMode", l=1):
				mc.setAttr("R_leg_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_leg_IK_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_CTL", a=1, t=[-1.915893542703273e-07, 0.0, -2.5305813245253735e-23])
			mc.xform("R_leg_IK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_leg_IK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_PV_CTL"):
			if not mc.getAttr("R_leg_PV_CTL.mirrorMode", l=1):
				mc.setAttr("R_leg_PV_CTL.mirrorMode", 0)

			if not mc.getAttr("R_leg_PV_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_PV_CTL.rotateOrder", 0)

			mc.xform("R_leg_PV_CTL", a=1, t=[4.2072740784604434e-06, 0.0, 5.329070518200751e-15])
			mc.xform("R_leg_PV_CTL", a=1, ro=[0.0, 0.0, -89.99999999999993])
			mc.xform("R_leg_PV_CTL", r=1, s=[0.9999999999999999, 1.0, 1.0])

		if mc.objExists("R_legBase_D_OFF_CTL"):
			if not mc.getAttr("R_legBase_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_D_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_legBase_D_OFF_CTL", a=1, ro=[7.951386703658793e-15, -3.260068548500105e-14, -5.9138438608462284e-15])
			mc.xform("R_legBase_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_C_OFF_CTL"):
			if not mc.getAttr("R_legBase_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_C_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_legBase_C_OFF_CTL", a=1, ro=[7.951386703658793e-15, -3.260068548500105e-14, -5.9138438608462284e-15])
			mc.xform("R_legBase_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_B_OFF_CTL"):
			if not mc.getAttr("R_legBase_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_B_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_legBase_B_OFF_CTL", a=1, ro=[7.951386703658793e-15, -3.260068548500105e-14, -5.9138438608462284e-15])
			mc.xform("R_legBase_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_A_OFF_CTL"):
			if not mc.getAttr("R_legBase_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_A_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_legBase_A_OFF_CTL", a=1, ro=[7.951386703658793e-15, -3.260068548500105e-14, -5.9138438608462284e-15])
			mc.xform("R_legBase_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_CTL"):
			if not mc.getAttr("R_legBase_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_legBase_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_legBase_CTL.mirrorMode", l=1):
				mc.setAttr("R_legBase_CTL.mirrorMode", 0)

			if not mc.getAttr("R_legBase_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_CTL.rotateOrder", 0)

			mc.xform("R_legBase_CTL", a=1, t=[0.0, -2.220446049250313e-16, 2.220446049250313e-16])
			mc.xform("R_legBase_CTL", a=1, ro=[1.1927080055488188e-15, -1.1927080055488188e-15, 6.311413196029166e-15])
			mc.xform("R_legBase_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0])

		if mc.objExists("R_leg_IK_switch_D_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_leg_IK_switch_D_OFF_CTL", a=1, ro=[6.7586786981099735e-15, -1.987846675914698e-15, -3.975693351829397e-16])
			mc.xform("R_leg_IK_switch_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_C_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_leg_IK_switch_C_OFF_CTL", a=1, ro=[6.7586786981099735e-15, -1.987846675914698e-15, -3.975693351829397e-16])
			mc.xform("R_leg_IK_switch_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_B_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_B_OFF_CTL", a=1, t=[0.0, 0.0, -1.3877787807814457e-17])
			mc.xform("R_leg_IK_switch_B_OFF_CTL", a=1, ro=[6.7586786981099735e-15, -1.987846675914698e-15, -3.975693351829397e-16])
			mc.xform("R_leg_IK_switch_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_A_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_A_OFF_CTL", a=1, t=[1.1102230246251565e-16, 0.0, 0.0])
			mc.xform("R_leg_IK_switch_A_OFF_CTL", a=1, ro=[6.7586786981099735e-15, -1.987846675914698e-15, -3.975693351829397e-16])
			mc.xform("R_leg_IK_switch_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_CTL"):
			if not mc.getAttr("R_leg_IK_switch_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_leg_IK_switch_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_leg_IK_switch_CTL.mirrorMode", l=1):
				mc.setAttr("R_leg_IK_switch_CTL.mirrorMode", 0)

			if not mc.getAttr("R_leg_IK_switch_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_CTL", a=1, t=[-3.3306690738754696e-16, 2.220446049250313e-16, 2.7755575615628914e-17])
			mc.xform("R_leg_IK_switch_CTL", a=1, ro=[-3.975693351829396e-16, 7.951386703658792e-16, -2.758691436281349e-33])
			mc.xform("R_leg_IK_switch_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0000000000000002])

		if mc.objExists("R_bendyLeg_A_D_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_A_D_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_bendyLeg_A_D_OFF_CTL", a=1, ro=[7.951386703658793e-15, -3.260068548500105e-14, -5.9138438608462284e-15])
			mc.xform("R_bendyLeg_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_A_C_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_A_C_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_bendyLeg_A_C_OFF_CTL", a=1, ro=[7.951386703658793e-15, -3.260068548500105e-14, -5.9138438608462284e-15])
			mc.xform("R_bendyLeg_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_A_B_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_A_B_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_bendyLeg_A_B_OFF_CTL", a=1, ro=[7.951386703658793e-15, -3.260068548500105e-14, -5.9138438608462284e-15])
			mc.xform("R_bendyLeg_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_A_A_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_A_A_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_bendyLeg_A_A_OFF_CTL", a=1, ro=[7.951386703658793e-15, -3.260068548500105e-14, -5.9138438608462284e-15])
			mc.xform("R_bendyLeg_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_A_CTL"):
			if not mc.getAttr("R_bendyLeg_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_bendyLeg_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_bendyLeg_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_bendyLeg_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_bendyLeg_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_A_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_A_CTL", a=1, t=[-1.7763568394002505e-15, 0.0, 0.0])
			mc.xform("R_bendyLeg_A_CTL", a=1, ro=[1.1927080055488188e-15, -1.1927080055488188e-15, 6.311413196029166e-15])
			mc.xform("R_bendyLeg_A_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0])

		if mc.objExists("R_bendyLeg_B_D_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_B_D_OFF_CTL", a=1, t=[-8.881784197001252e-16, 0.0, 0.0])
			mc.xform("R_bendyLeg_B_D_OFF_CTL", a=1, ro=[7.056855699497179e-15, -9.939233379573413e-17, -1.2707076925002378e-14])
			mc.xform("R_bendyLeg_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_B_C_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_B_C_OFF_CTL", a=1, t=[8.881784197001252e-16, 0.0, 0.0])
			mc.xform("R_bendyLeg_B_C_OFF_CTL", a=1, ro=[7.056855699497179e-15, -9.939233379573413e-17, -1.2707076925002378e-14])
			mc.xform("R_bendyLeg_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_B_B_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_B_B_OFF_CTL", a=1, t=[-8.881784197001252e-16, 0.0, 0.0])
			mc.xform("R_bendyLeg_B_B_OFF_CTL", a=1, ro=[7.056855699497179e-15, -9.939233379573413e-17, -1.2707076925002378e-14])
			mc.xform("R_bendyLeg_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_B_A_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_B_A_OFF_CTL", a=1, t=[8.881784197001252e-16, 0.0, 0.0])
			mc.xform("R_bendyLeg_B_A_OFF_CTL", a=1, ro=[7.056855699497179e-15, -9.939233379573413e-17, -1.2707076925002378e-14])
			mc.xform("R_bendyLeg_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_B_CTL"):
			if not mc.getAttr("R_bendyLeg_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_bendyLeg_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_bendyLeg_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_bendyLeg_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_bendyLeg_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_B_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_B_CTL", a=1, t=[8.881784197001252e-16, 0.0, 0.0])
			mc.xform("R_bendyLeg_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_bendyLeg_B_CTL", r=1, s=[0.9999999999999998, 1.0000000000000002, 1.0])

		if mc.objExists("R_bendyLeg_C_D_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_C_D_OFF_CTL", a=1, t=[4.440892098500626e-16, 0.0, -1.3877787807814457e-17])
			mc.xform("R_bendyLeg_C_D_OFF_CTL", a=1, ro=[5.565970692561155e-15, -2.385416011097637e-15, -1.3070091894139143e-14])
			mc.xform("R_bendyLeg_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_C_C_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_C_C_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 1.3877787807814457e-17])
			mc.xform("R_bendyLeg_C_C_OFF_CTL", a=1, ro=[5.565970692561155e-15, -2.385416011097637e-15, -1.3070091894139143e-14])
			mc.xform("R_bendyLeg_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_C_B_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_C_B_OFF_CTL", a=1, t=[4.440892098500626e-16, 0.0, -1.3877787807814457e-17])
			mc.xform("R_bendyLeg_C_B_OFF_CTL", a=1, ro=[5.565970692561155e-15, -2.385416011097637e-15, -1.3070091894139143e-14])
			mc.xform("R_bendyLeg_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_C_A_OFF_CTL"):
			if not mc.getAttr("R_bendyLeg_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_C_A_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 1.3877787807814457e-17])
			mc.xform("R_bendyLeg_C_A_OFF_CTL", a=1, ro=[5.565970692561155e-15, -2.385416011097637e-15, -1.3070091894139143e-14])
			mc.xform("R_bendyLeg_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_bendyLeg_C_CTL"):
			if not mc.getAttr("R_bendyLeg_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_bendyLeg_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_bendyLeg_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_bendyLeg_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_bendyLeg_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_bendyLeg_C_CTL.rotateOrder", 0)

			mc.xform("R_bendyLeg_C_CTL", a=1, t=[-1.3322676295501878e-15, -2.220446049250313e-16, 2.0816681711721685e-16])
			mc.xform("R_bendyLeg_C_CTL", a=1, ro=[0.0, 7.951386703658792e-16, 0.0])
			mc.xform("R_bendyLeg_C_CTL", r=1, s=[1.0, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_thumb_A_CTL"):
			if not mc.getAttr("R_thumb_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_CTL.rotateOrder", 0)

			mc.xform("R_thumb_A_CTL", a=1, t=[-4.995987694655923e-07, -3.3306584485970347e-06, 5.833408412314611e-06])
			mc.xform("R_thumb_A_CTL", a=1, ro=[0.0, 0.0, -6.3611093629270335e-15])
			mc.xform("R_thumb_A_CTL", r=1, s=[1.0000000000000002, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_thumb_B_CTL"):
			if not mc.getAttr("R_thumb_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_CTL.rotateOrder", 0)

			mc.xform("R_thumb_B_CTL", a=1, t=[4.230014807760085e-06, -4.816260659623595e-06, 4.997208510104656e-06])
			mc.xform("R_thumb_B_CTL", a=1, ro=[3.97251566824514e-31, -4.770832022195273e-15, -9.541664044390546e-15])
			mc.xform("R_thumb_B_CTL", r=1, s=[1.0, 0.9999999999999998, 1.0000000000000002])

		if mc.objExists("R_thumb_C_CTL"):
			if not mc.getAttr("R_thumb_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_CTL.rotateOrder", 0)

			mc.xform("R_thumb_C_CTL", a=1, t=[-9.275687062881843e-08, -3.764891444824059e-06, 5.636209543524728e-06])
			mc.xform("R_thumb_C_CTL", a=1, ro=[1.90833280887811e-14, -1.590277340731758e-15, -2.385416011097638e-15])
			mc.xform("R_thumb_C_CTL", r=1, s=[1.0000000000000004, 1.0000000000000007, 1.0000000000000002])

		if mc.objExists("R_index_A_CTL"):
			if not mc.getAttr("R_index_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_A_CTL.rotateOrder", 0)

			mc.xform("R_index_A_CTL", a=1, t=[-8.902336539051703e-07, -6.676752384748852e-06, -5.551115123125783e-17])
			mc.xform("R_index_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_index_A_CTL", r=1, s=[1.0, 1.0000000000000002, 0.9999999999999998])

		if mc.objExists("R_index_B_CTL"):
			if not mc.getAttr("R_index_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_B_CTL.rotateOrder", 0)

			mc.xform("R_index_B_CTL", a=1, t=[-5.371510471974261e-07, -6.714388067763366e-06, 5.551115123125783e-17])
			mc.xform("R_index_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_index_B_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_index_C_CTL"):
			if not mc.getAttr("R_index_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_C_CTL.rotateOrder", 0)

			mc.xform("R_index_C_CTL", a=1, t=[5.371510471974261e-07, -6.714388078421507e-06, -5.551115123125783e-17])
			mc.xform("R_index_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_index_C_CTL", r=1, s=[1.0000000000000002, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_index_D_CTL"):
			if not mc.getAttr("R_index_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_D_CTL.rotateOrder", 0)

			mc.xform("R_index_D_CTL", a=1, t=[8.902336556815271e-07, -6.676752395406993e-06, -2.7755575615628914e-17])
			mc.xform("R_index_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_index_D_CTL", r=1, s=[1.0000000000000004, 1.0, 1.0])

		if mc.objExists("R_middle_A_CTL"):
			if not mc.getAttr("R_middle_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_A_CTL.rotateOrder", 0)

			mc.xform("R_middle_A_CTL", a=1, t=[-8.902336539051703e-07, -6.676752384748852e-06, 8.249024694278794e-22])
			mc.xform("R_middle_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_middle_A_CTL", r=1, s=[1.0, 1.0000000000000002, 0.9999999999999998])

		if mc.objExists("R_middle_B_CTL"):
			if not mc.getAttr("R_middle_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_B_CTL.rotateOrder", 0)

			mc.xform("R_middle_B_CTL", a=1, t=[-5.371510471974261e-07, -6.714388067763366e-06, 8.249024706111708e-22])
			mc.xform("R_middle_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_middle_B_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_middle_C_CTL"):
			if not mc.getAttr("R_middle_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_C_CTL.rotateOrder", 0)

			mc.xform("R_middle_C_CTL", a=1, t=[5.371510436447124e-07, -6.714388074868793e-06, 8.249024717944621e-22])
			mc.xform("R_middle_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_middle_C_CTL", r=1, s=[1.0, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_middle_D_CTL"):
			if not mc.getAttr("R_middle_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_D_CTL.rotateOrder", 0)

			mc.xform("R_middle_D_CTL", a=1, t=[8.902336556815271e-07, -6.676752395406993e-06, 8.249024717944621e-22])
			mc.xform("R_middle_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_middle_D_CTL", r=1, s=[1.0000000000000004, 1.0, 1.0])

		if mc.objExists("R_ring_A_CTL"):
			if not mc.getAttr("R_ring_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_A_CTL.rotateOrder", 0)

			mc.xform("R_ring_A_CTL", a=1, t=[-8.902336539051703e-07, -6.676752384748852e-06, -5.551115123125783e-17])
			mc.xform("R_ring_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_ring_A_CTL", r=1, s=[1.0, 1.0000000000000002, 0.9999999999999998])

		if mc.objExists("R_ring_B_CTL"):
			if not mc.getAttr("R_ring_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_B_CTL.rotateOrder", 0)

			mc.xform("R_ring_B_CTL", a=1, t=[-5.371510471974261e-07, -6.714388067763366e-06, 1.1102230246251565e-16])
			mc.xform("R_ring_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_ring_B_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_ring_C_CTL"):
			if not mc.getAttr("R_ring_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_C_CTL.rotateOrder", 0)

			mc.xform("R_ring_C_CTL", a=1, t=[5.371510436447124e-07, -6.714388074868793e-06, 0.0])
			mc.xform("R_ring_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_ring_C_CTL", r=1, s=[1.0, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_ring_D_CTL"):
			if not mc.getAttr("R_ring_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_D_CTL.rotateOrder", 0)

			mc.xform("R_ring_D_CTL", a=1, t=[8.902336556815271e-07, -6.676752395406993e-06, 5.551115123125783e-17])
			mc.xform("R_ring_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_ring_D_CTL", r=1, s=[1.0000000000000004, 1.0, 1.0])

		if mc.objExists("R_pinky_A_CTL"):
			if not mc.getAttr("R_pinky_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_CTL.rotateOrder", 0)

			mc.xform("R_pinky_A_CTL", a=1, t=[-8.902336539051703e-07, -6.676752384748852e-06, -2.220446049250313e-16])
			mc.xform("R_pinky_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_A_CTL", r=1, s=[1.0, 1.0000000000000002, 0.9999999999999998])

		if mc.objExists("R_pinky_B_CTL"):
			if not mc.getAttr("R_pinky_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_CTL.rotateOrder", 0)

			mc.xform("R_pinky_B_CTL", a=1, t=[-5.371510471974261e-07, -6.714388067763366e-06, 0.0])
			mc.xform("R_pinky_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_B_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_pinky_C_CTL"):
			if not mc.getAttr("R_pinky_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_CTL.rotateOrder", 0)

			mc.xform("R_pinky_C_CTL", a=1, t=[5.371510436447124e-07, -6.714388074868793e-06, 1.1102230246251565e-16])
			mc.xform("R_pinky_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_C_CTL", r=1, s=[1.0, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_pinky_D_CTL"):
			if not mc.getAttr("R_pinky_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_CTL.rotateOrder", 0)

			mc.xform("R_pinky_D_CTL", a=1, t=[8.902336556815271e-07, -6.676752395406993e-06, 2.220446049250313e-16])
			mc.xform("R_pinky_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_D_CTL", r=1, s=[1.0000000000000004, 1.0, 1.0])

		if mc.objExists("R_hand_CTL"):
			if not mc.getAttr("R_hand_CTL.mirrorMode", l=1):
				mc.setAttr("R_hand_CTL.mirrorMode", 0)

			if not mc.getAttr("R_hand_CTL.rotateOrder", l=1):
				mc.setAttr("R_hand_CTL.rotateOrder", 0)

			mc.xform("R_hand_CTL", a=1, t=[-1.7763568394002505e-15, -6.735839846783165e-06, 8.249024702167403e-22])
			mc.xform("R_hand_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_hand_CTL", r=1, s=[0.9999999999999999, 0.9999999999999998, 1.0])

		# Apply contro shapes data
		data = {
			"C_cog_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_CTLShape", "degree": 1, "form": 0, "points": [[-15.0, 49.350166, -15.0], [-15.0, 49.350166, 15.0], [15.0, 49.350166, 15.0], [15.0, 49.350166, -15.0], [-15.0, 49.350166, -15.0]]}]},
			"R_loLeg_shaper_03_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_03_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.25, 13.525979, 1.25], [-16.335635, 13.012819, 1.19033], [-16.579512, 12.577783, 1.139745], [-16.944485, 12.287088, 1.105943], [-17.375, 12.185014, 1.094074], [-17.805515, 12.287088, 1.105943], [-18.170488, 12.577783, 1.139745], [-18.414365, 13.012819, 1.19033], [-18.5, 13.525979, 1.25], [-18.414365, 14.039139, 1.30967], [-18.170488, 14.474175, 1.360255], [-17.805515, 14.76487, 1.394057], [-17.375, 14.866944, 1.405926], [-16.944485, 14.76487, 1.394057], [-16.579512, 14.474175, 1.360255], [-16.335635, 14.039139, 1.30967], [-16.25, 13.525979, 1.25], [-5.0, 13.525979, 1.25]]}]},
			"R_elbow_shaper_02_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_02_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-42.25, 94.100166, -3.75], [-42.332604, 94.117293, -3.725705], [-42.402633, 94.166069, -3.705108], [-42.449426, 94.239063, -3.691345], [-42.465857, 94.325166, -3.686513], [-42.449426, 94.411269, -3.691345], [-42.402633, 94.484264, -3.705108], [-42.332604, 94.533039, -3.725705], [-42.25, 94.550166, -3.75], [-42.167396, 94.533039, -3.774295], [-42.097367, 94.484264, -3.794892], [-42.050574, 94.411269, -3.808655], [-42.034143, 94.325166, -3.813487], [-42.050574, 94.239063, -3.808655], [-42.097367, 94.166069, -3.794892], [-42.167396, 94.117293, -3.774295], [-42.25, 94.100166, -3.75], [-42.25, 91.850166, -3.75]]}]},
			"R_elbow_shaper_02_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_02_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-42.25, 93.850166, -3.75], [-42.323426, 93.86539, -3.728404], [-42.385673, 93.908746, -3.710096], [-42.427268, 93.97363, -3.697862], [-42.441873, 94.050166, -3.693567], [-42.427268, 94.126702, -3.697862], [-42.385673, 94.191586, -3.710096], [-42.323426, 94.234942, -3.728404], [-42.25, 94.250166, -3.75], [-42.176574, 94.234942, -3.771596], [-42.114327, 94.191586, -3.789904], [-42.072732, 94.126702, -3.802138], [-42.058127, 94.050166, -3.806433], [-42.072732, 93.97363, -3.802138], [-42.114327, 93.908746, -3.789904], [-42.176574, 93.86539, -3.771596], [-42.25, 93.850166, -3.75], [-42.25, 91.850166, -3.75]]}]},
			"R_shoulderFk_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulderFk_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-20.983421, 91.850166, -0.284434], [-20.986325, 91.861017, -0.273979], [-20.98923, 91.850166, -0.263524], [-20.986325, 91.839315, -0.273979], [-20.983421, 91.850166, -0.284434], [-20.99678, 91.850166, -0.276883], [-20.98923, 91.850166, -0.263524], [-20.97587, 91.850166, -0.271075], [-20.986325, 91.861017, -0.273979], [-20.99678, 91.850166, -0.276883], [-20.986325, 91.839315, -0.273979], [-20.97587, 91.850166, -0.271075], [-20.983421, 91.850166, -0.284434], [-20.99678, 91.850166, -0.276883], [-20.0, 91.850166, -0.0]]}, {"shapeName": "R_shoulderFk_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-19.997096, 92.873837, -0.010455], [-19.989545, 92.873837, 0.002904], [-20.002904, 92.873837, 0.010455], [-20.010455, 92.873837, -0.002904], [-19.997096, 92.873837, -0.010455], [-20.0, 92.884687, -0.0], [-20.002904, 92.873837, 0.010455], [-20.0, 92.862986, -0.0], [-19.989545, 92.873837, 0.002904], [-20.0, 92.884687, -0.0], [-20.010455, 92.873837, -0.002904], [-20.0, 92.862986, -0.0], [-19.997096, 92.873837, -0.010455], [-20.0, 92.884687, -0.0], [-20.0, 91.850166, -0.0]]}, {"shapeName": "R_shoulderFk_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-20.273979, 91.861017, 0.986325], [-20.263524, 91.850166, 0.98923], [-20.273979, 91.839315, 0.986325], [-20.284434, 91.850166, 0.983421], [-20.273979, 91.861017, 0.986325], [-20.276883, 91.850166, 0.99678], [-20.273979, 91.839315, 0.986325], [-20.271075, 91.850166, 0.97587], [-20.263524, 91.850166, 0.98923], [-20.276883, 91.850166, 0.99678], [-20.284434, 91.850166, 0.983421], [-20.271075, 91.850166, 0.97587], [-20.273979, 91.861017, 0.986325], [-20.276883, 91.850166, 0.99678], [-20.0, 91.850166, -0.0]]}]},
			"R_upLeg_shaper_02_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upLeg_shaper_02_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 32.537211, 1.522023], [-4.945745, 32.530482, 1.468187], [-5.0, 32.523752, 1.414351], [-5.054255, 32.530482, 1.468187], [-5.0, 32.537211, 1.522023], [-5.0, 32.476651, 1.474916], [-5.0, 32.523752, 1.414351], [-5.0, 32.584318, 1.461458], [-4.945745, 32.530482, 1.468187], [-5.0, 32.476651, 1.474916], [-5.054255, 32.530482, 1.468187], [-5.0, 32.584318, 1.461458], [-5.0, 32.537211, 1.522023], [-5.0, 32.476651, 1.474916], [-5.0, 37.609312, 0.833333]]}, {"shapeName": "R_upLeg_shaper_02_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 37.616042, 0.887169], [0.118355, 37.663148, 0.826604], [0.118355, 37.602583, 0.779497], [0.118355, 37.555476, 0.840063], [0.118355, 37.616042, 0.887169], [0.172605, 37.609312, 0.833333], [0.118355, 37.602583, 0.779497], [0.0641, 37.609312, 0.833333], [0.118355, 37.663148, 0.826604], [0.172605, 37.609312, 0.833333], [0.118355, 37.555476, 0.840063], [0.0641, 37.609312, 0.833333], [0.118355, 37.616042, 0.887169], [0.172605, 37.609312, 0.833333], [-5.0, 37.609312, 0.833333]]}, {"shapeName": "R_upLeg_shaper_02_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 36.974458, -4.245497], [-5.0, 37.028295, -4.252227], [-5.054255, 36.974458, -4.245497], [-5.0, 36.920622, -4.238768], [-4.945745, 36.974458, -4.245497], [-5.0, 36.96773, -4.299328], [-5.054255, 36.974458, -4.245497], [-5.0, 36.981188, -4.191661], [-5.0, 37.028295, -4.252227], [-5.0, 36.96773, -4.299328], [-5.0, 36.920622, -4.238768], [-5.0, 36.981188, -4.191661], [-4.945745, 36.974458, -4.245497], [-5.0, 36.96773, -4.299328], [-5.0, 37.609312, 0.833333]]}]},
			"R_scapulaChest_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_scapulaChest_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.023671, 91.850166, -0.010851], [-1.023671, 91.861017, -0.0], [-1.023671, 91.850166, 0.010851], [-1.023671, 91.839315, -0.0], [-1.023671, 91.850166, -0.010851], [-1.034521, 91.850166, -0.0], [-1.023671, 91.850166, 0.010851], [-1.01282, 91.850166, -0.0], [-1.023671, 91.861017, -0.0], [-1.034521, 91.850166, -0.0], [-1.023671, 91.839315, -0.0], [-1.01282, 91.850166, -0.0], [-1.023671, 91.850166, -0.010851], [-1.034521, 91.850166, -0.0], [0.0, 91.850166, 0.0]]}, {"shapeName": "R_scapulaChest_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 92.873837, -0.010851], [0.010851, 92.873837, 0.0], [-0.0, 92.873837, 0.010851], [-0.010851, 92.873837, -0.0], [0.0, 92.873837, -0.010851], [0.0, 92.884687, 0.0], [-0.0, 92.873837, 0.010851], [0.0, 92.862986, 0.0], [0.010851, 92.873837, 0.0], [0.0, 92.884687, 0.0], [-0.010851, 92.873837, -0.0], [0.0, 92.862986, 0.0], [0.0, 92.873837, -0.010851], [0.0, 92.884687, 0.0], [0.0, 91.850166, 0.0]]}, {"shapeName": "R_scapulaChest_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.0, 91.861017, 1.023671], [0.010851, 91.850166, 1.023671], [-0.0, 91.839315, 1.023671], [-0.010851, 91.850166, 1.023671], [-0.0, 91.861017, 1.023671], [-0.0, 91.850166, 1.034521], [-0.0, 91.839315, 1.023671], [-0.0, 91.850166, 1.01282], [0.010851, 91.850166, 1.023671], [-0.0, 91.850166, 1.034521], [-0.010851, 91.850166, 1.023671], [-0.0, 91.850166, 1.01282], [-0.0, 91.861017, 1.023671], [-0.0, 91.850166, 1.034521], [0.0, 91.850166, 0.0]]}]},
			"L_handIk_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_handIk_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[55.0, 89.107524, -2.742642], [55.0, 91.850166, -3.878679], [55.0, 94.592808, -2.742642], [55.0, 95.728845, 0.0], [55.0, 94.592808, 2.742642], [55.0, 91.850166, 3.878679], [55.0, 89.107524, 2.742642], [55.0, 87.971487, 0.0]]}]},
			"R_scapulaTarget_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_scapulaTarget_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.023671, 91.850166, -15.010851], [-1.023671, 91.861017, -15.0], [-1.023671, 91.850166, -14.989149], [-1.023671, 91.839315, -15.0], [-1.023671, 91.850166, -15.010851], [-1.034521, 91.850166, -15.0], [-1.023671, 91.850166, -14.989149], [-1.01282, 91.850166, -15.0], [-1.023671, 91.861017, -15.0], [-1.034521, 91.850166, -15.0], [-1.023671, 91.839315, -15.0], [-1.01282, 91.850166, -15.0], [-1.023671, 91.850166, -15.010851], [-1.034521, 91.850166, -15.0], [0.0, 91.850166, -15.0]]}, {"shapeName": "R_scapulaTarget_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 92.873837, -15.010851], [0.010851, 92.873837, -15.0], [-0.0, 92.873837, -14.989149], [-0.010851, 92.873837, -15.0], [0.0, 92.873837, -15.010851], [0.0, 92.884687, -15.0], [-0.0, 92.873837, -14.989149], [0.0, 92.862986, -15.0], [0.010851, 92.873837, -15.0], [0.0, 92.884687, -15.0], [-0.010851, 92.873837, -15.0], [0.0, 92.862986, -15.0], [0.0, 92.873837, -15.010851], [0.0, 92.884687, -15.0], [0.0, 91.850166, -15.0]]}, {"shapeName": "R_scapulaTarget_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.0, 91.861017, -13.976329], [0.010851, 91.850166, -13.976329], [-0.0, 91.839315, -13.976329], [-0.010851, 91.850166, -13.976329], [-0.0, 91.861017, -13.976329], [-0.0, 91.850166, -13.965479], [-0.0, 91.839315, -13.976329], [-0.0, 91.850166, -13.98718], [0.010851, 91.850166, -13.976329], [-0.0, 91.850166, -13.965479], [-0.010851, 91.850166, -13.976329], [-0.0, 91.850166, -13.98718], [-0.0, 91.861017, -13.976329], [-0.0, 91.850166, -13.965479], [0.0, 91.850166, -15.0]]}]},
			"C_head_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_CTLShape", "degree": 1, "form": 0, "points": [[5.412659, 101.850166, -3.125], [0.0, 101.850166, -6.25], [-5.412659, 101.850166, -3.125], [-7.102101, 109.424646, 3.719831], [0.0, 109.424646, 9.492691], [7.102101, 109.424646, 3.719831], [5.412659, 101.850166, -3.125]]}]},
			"L_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[71.948456, 91.423705, 1.195745], [71.955627, 91.477485, 1.25], [71.948456, 91.423705, 1.304255], [71.941286, 91.369926, 1.25], [71.948456, 91.423705, 1.195745], [72.00223, 91.416536, 1.25], [71.948456, 91.423705, 1.304255], [71.894677, 91.430876, 1.25], [71.955627, 91.477485, 1.25], [72.00223, 91.416536, 1.25], [71.941286, 91.369926, 1.25], [71.894677, 91.430876, 1.25], [71.948456, 91.423705, 1.195745], [72.00223, 91.416536, 1.25], [66.875, 92.100166, 1.25]]}, {"shapeName": "L_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.551461, 97.173623, 1.195745], [67.497682, 97.180793, 1.25], [67.551461, 97.173623, 1.304255], [67.60524, 97.166452, 1.25], [67.551461, 97.173623, 1.195745], [67.558631, 97.227397, 1.25], [67.551461, 97.173623, 1.304255], [67.54429, 97.119844, 1.25], [67.497682, 97.180793, 1.25], [67.558631, 97.227397, 1.25], [67.60524, 97.166452, 1.25], [67.54429, 97.119844, 1.25], [67.551461, 97.173623, 1.195745], [67.558631, 97.227397, 1.25], [66.875, 92.100166, 1.25]]}, {"shapeName": "L_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[66.882171, 92.153945, 6.368355], [66.821221, 92.107337, 6.368355], [66.867829, 92.046387, 6.368355], [66.928779, 92.092996, 6.368355], [66.882171, 92.153945, 6.368355], [66.875, 92.100166, 6.422605], [66.867829, 92.046387, 6.368355], [66.875, 92.100166, 6.3141], [66.821221, 92.107337, 6.368355], [66.875, 92.100166, 6.422605], [66.928779, 92.092996, 6.368355], [66.875, 92.100166, 6.3141], [66.882171, 92.153945, 6.368355], [66.875, 92.100166, 6.422605], [66.875, 92.100166, 1.25]]}]},
			"C_revSpine_1_CTL": {"color": 4, "shapes": [{"shapeName": "C_revSpine_1_CTLShape", "degree": 3, "form": 2, "points": [[5.87709, 64.350166, 5.87709], [8.311455, 64.350166, 0.0], [6e-05, 64.350166, -5.87709], [0.0, 64.350166, -8.311455], [-6e-05, 64.350166, -5.87709], [-8.311455, 64.350166, 0.0], [-5.87709, 64.350166, 5.87709], [0.0, 64.350166, 8.311455]]}]},
			"R_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_D_CTLShape", "degree": 1, "form": 0, "points": [[-67.717544, 92.744464, 2.0], [-66.230702, 92.94271, 2.0], [-66.230702, 92.94271, 0.5], [-67.717544, 92.744464, 0.5], [-67.519298, 91.257623, 0.5], [-66.032456, 91.455868, 0.5], [-66.032456, 91.455868, 2.0], [-67.519298, 91.257623, 2.0], [-67.717544, 92.744464, 2.0], [-67.717544, 92.744464, 0.5], [-66.230702, 92.94271, 0.5], [-66.032456, 91.455868, 0.5], [-67.519298, 91.257623, 0.5], [-67.519298, 91.257623, 2.0], [-66.032456, 91.455868, 2.0], [-66.230702, 92.94271, 2.0]]}]},
			"L_shoulder_shaper_04_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_04_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[33.5, 93.350166, -3.75], [33.555308, 93.361584, -3.765363], [33.602196, 93.394101, -3.778388], [33.633526, 93.442764, -3.787091], [33.644528, 93.500166, -3.790147], [33.633526, 93.557568, -3.787091], [33.602196, 93.606231, -3.778388], [33.555308, 93.638748, -3.765363], [33.5, 93.650166, -3.75], [33.444692, 93.638748, -3.734637], [33.397804, 93.606231, -3.721612], [33.366474, 93.557568, -3.712909], [33.355472, 93.500166, -3.709853], [33.366474, 93.442764, -3.712909], [33.397804, 93.394101, -3.721612], [33.444692, 93.361584, -3.734637], [33.5, 93.350166, -3.75], [33.5, 91.850166, -3.75]]}]},
			"R_handIk_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_handIk_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-55.0, 89.107524, -2.742642], [-55.0, 91.850166, -3.878679], [-55.0, 94.592808, -2.742642], [-55.0, 95.728845, -0.0], [-55.0, 94.592808, 2.742642], [-55.0, 91.850166, 3.878679], [-55.0, 89.107524, 2.742642], [-55.0, 87.971487, 0.0]]}]},
			"L_scapulaChest_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_scapulaChest_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 91.850166, -0.010851], [1.023671, 91.861017, 0.0], [1.023671, 91.850166, 0.010851], [1.023671, 91.839315, 0.0], [1.023671, 91.850166, -0.010851], [1.034521, 91.850166, 0.0], [1.023671, 91.850166, 0.010851], [1.01282, 91.850166, 0.0], [1.023671, 91.861017, 0.0], [1.034521, 91.850166, 0.0], [1.023671, 91.839315, 0.0], [1.01282, 91.850166, 0.0], [1.023671, 91.850166, -0.010851], [1.034521, 91.850166, 0.0], [0.0, 91.850166, 0.0]]}, {"shapeName": "L_scapulaChest_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 92.873837, -0.010851], [-0.010851, 92.873837, 0.0], [0.0, 92.873837, 0.010851], [0.010851, 92.873837, 0.0], [0.0, 92.873837, -0.010851], [0.0, 92.884687, 0.0], [0.0, 92.873837, 0.010851], [0.0, 92.862986, 0.0], [-0.010851, 92.873837, 0.0], [0.0, 92.884687, 0.0], [0.010851, 92.873837, 0.0], [0.0, 92.862986, 0.0], [0.0, 92.873837, -0.010851], [0.0, 92.884687, 0.0], [0.0, 91.850166, 0.0]]}, {"shapeName": "L_scapulaChest_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 91.861017, 1.023671], [-0.010851, 91.850166, 1.023671], [0.0, 91.839315, 1.023671], [0.010851, 91.850166, 1.023671], [0.0, 91.861017, 1.023671], [0.0, 91.850166, 1.034521], [0.0, 91.839315, 1.023671], [0.0, 91.850166, 1.01282], [-0.010851, 91.850166, 1.023671], [0.0, 91.850166, 1.034521], [0.010851, 91.850166, 1.023671], [0.0, 91.850166, 1.01282], [0.0, 91.861017, 1.023671], [0.0, 91.850166, 1.034521], [0.0, 91.850166, 0.0]]}]},
			"L_shoulder_shaper_01_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_01_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[20.9, 93.350166, -0.25], [20.955308, 93.361584, -0.265363], [21.002196, 93.394101, -0.278388], [21.033526, 93.442764, -0.287091], [21.044528, 93.500166, -0.290147], [21.033526, 93.557568, -0.287091], [21.002196, 93.606231, -0.278388], [20.955308, 93.638748, -0.265363], [20.9, 93.650166, -0.25], [20.844692, 93.638748, -0.234637], [20.797804, 93.606231, -0.221612], [20.766474, 93.557568, -0.212909], [20.755472, 93.500166, -0.209853], [20.766474, 93.442764, -0.212909], [20.797804, 93.394101, -0.221612], [20.844692, 93.361584, -0.234637], [20.9, 93.350166, -0.25], [20.9, 91.850166, -0.25]]}]},
			"L_shoulder_shaper_01_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_01_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[20.9, 94.100166, -0.25], [20.982962, 94.117293, -0.273045], [21.053293, 94.166069, -0.292581], [21.100289, 94.239063, -0.305636], [21.116792, 94.325166, -0.31022], [21.100289, 94.411269, -0.305636], [21.053293, 94.484264, -0.292581], [20.982962, 94.533039, -0.273045], [20.9, 94.550166, -0.25], [20.817038, 94.533039, -0.226955], [20.746707, 94.484264, -0.207419], [20.699711, 94.411269, -0.194364], [20.683208, 94.325166, -0.18978], [20.699711, 94.239063, -0.194364], [20.746707, 94.166069, -0.207419], [20.817038, 94.117293, -0.226955], [20.9, 94.100166, -0.25], [20.9, 91.850166, -0.25]]}]},
			"L_loLeg_shaper_05_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_05_CTLShape", "degree": 1, "form": 0, "points": [[17.5, 6.359312, 0.416667], [17.59515, 5.789134, 0.350367], [17.866125, 5.305761, 0.294161], [18.27165, 4.982767, 0.256603], [18.75, 4.869351, 0.243415], [19.22835, 4.982767, 0.256603], [19.633875, 5.305761, 0.294161], [19.90485, 5.789134, 0.350367], [20.0, 6.359312, 0.416667], [19.90485, 6.929491, 0.482966], [19.633875, 7.412864, 0.539173], [19.22835, 7.735858, 0.57673], [18.75, 7.849273, 0.589918], [18.27165, 7.735858, 0.57673], [17.866125, 7.412864, 0.539173], [17.59515, 6.929491, 0.482966], [17.5, 6.359312, 0.416667], [5.0, 6.359312, 0.416667]]}]},
			"L_loLeg_shaper_05_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_05_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[12.5, 6.359312, 0.416667], [12.55709, 6.017205, 0.376887], [12.719675, 5.727181, 0.343163], [12.96299, 5.533385, 0.320629], [13.25, 5.465336, 0.312716], [13.53701, 5.533385, 0.320629], [13.780325, 5.727181, 0.343163], [13.94291, 6.017205, 0.376887], [14.0, 6.359312, 0.416667], [13.94291, 6.701419, 0.456447], [13.780325, 6.991443, 0.49017], [13.53701, 7.18524, 0.512705], [13.25, 7.253289, 0.520617], [12.96299, 7.18524, 0.512705], [12.719675, 6.991443, 0.49017], [12.55709, 6.701419, 0.456447], [12.5, 6.359312, 0.416667], [5.0, 6.359312, 0.416667]]}]},
			"R_elbow_shaper_04_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_04_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-50.75, 93.350166, -1.25], [-50.805069, 93.361584, -1.233803], [-50.851755, 93.394101, -1.220072], [-50.882951, 93.442764, -1.210897], [-50.893905, 93.500166, -1.207675], [-50.882951, 93.557568, -1.210897], [-50.851755, 93.606231, -1.220072], [-50.805069, 93.638748, -1.233803], [-50.75, 93.650166, -1.25], [-50.694931, 93.638748, -1.266197], [-50.648245, 93.606231, -1.279928], [-50.617049, 93.557568, -1.289103], [-50.606095, 93.500166, -1.292325], [-50.617049, 93.442764, -1.289103], [-50.648245, 93.394101, -1.279928], [-50.694931, 93.361584, -1.266197], [-50.75, 93.350166, -1.25], [-50.75, 91.850166, -1.25]]}]},
			"R_leg_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[-8.90939, 3.360282, 0.067942], [-8.750215, 3.360282, 0.067942], [-8.72007, 3.19804, 0.049077], [-8.60696, 3.151489, 0.043664], [-8.47014, 3.245039, 0.054542], [-8.357585, 3.133237, 0.041542], [-8.45176, 2.997348, 0.025741], [-8.404915, 2.88498, 0.012674], [-8.241565, 2.855036, 0.009193], [-8.241565, 2.696922, -0.009193], [-8.404915, 2.666978, -0.012674], [-8.45176, 2.554625, -0.025739], [-8.357585, 2.418721, -0.041542], [-8.47014, 2.306919, -0.054542], [-8.60696, 2.400469, -0.043664], [-8.72007, 2.353918, -0.049077], [-8.750215, 2.191676, -0.067942], [-8.90939, 2.191676, -0.067942], [-8.93955, 2.353918, -0.049077], [-9.05266, 2.400469, -0.043664], [-9.18948, 2.306919, -0.054542], [-9.302025, 2.418721, -0.041542], [-9.20786, 2.554625, -0.025739], [-9.254705, 2.666978, -0.012674], [-9.41804, 2.696922, -0.009193], [-9.41804, 2.855036, 0.009193], [-9.254705, 2.88498, 0.012674], [-9.20786, 2.997348, 0.025741], [-9.302025, 3.133237, 0.041542], [-9.18948, 3.245039, 0.054542], [-9.05266, 3.151489, 0.043664], [-8.93955, 3.19804, 0.049077], [-8.90939, 3.360282, 0.067942]]}, {"shapeName": "R_leg_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[-9.00258, 2.947603, 0.019956], [-9.07415, 2.775979, -0.0], [-9.00258, 2.604355, -0.019956], [-8.829805, 2.533279, -0.028221], [-8.65704, 2.604355, -0.019956], [-8.58547, 2.775979, -0.0], [-8.65704, 2.947603, 0.019956], [-8.829805, 3.018679, 0.028221]]}, {"shapeName": "R_leg_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[-8.241565, 2.775979, -0.0], [-5.0, 2.775979, -0.0]]}]},
			"R_handIk_CTL": {"color": 13, "shapes": [{"shapeName": "R_handIk_CTLShape", "degree": 3, "form": 2, "points": [[-55.0, 87.932106, -3.91806], [-55.0, 91.850166, -5.54097], [-55.0, 95.768226, -3.91806], [-55.0, 97.391136, 0.0], [-55.0, 95.768226, 3.91806], [-55.0, 91.850166, 5.54097], [-55.0, 87.932106, 3.91806], [-55.0, 86.309196, 0.0]]}]},
			"L_loLeg_shaper_03_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_03_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[13.75, 13.525979, 1.25], [13.816605, 13.126854, 1.20359], [14.006287, 12.788493, 1.164246], [14.290155, 12.562397, 1.137956], [14.625, 12.483006, 1.128724], [14.959845, 12.562397, 1.137956], [15.243712, 12.788493, 1.164246], [15.433395, 13.126854, 1.20359], [15.5, 13.525979, 1.25], [15.433395, 13.925104, 1.29641], [15.243712, 14.263465, 1.335754], [14.959845, 14.489561, 1.362044], [14.625, 14.568952, 1.371276], [14.290155, 14.489561, 1.362044], [14.006287, 14.263465, 1.335754], [13.816605, 13.925104, 1.29641], [13.75, 13.525979, 1.25], [5.0, 13.525979, 1.25]]}]},
			"C_spine_FK_0_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_spine_FK_0_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 56.988521, -0.054255], [-0.054255, 56.988521, 0.0], [0.0, 56.988521, 0.054255], [0.054255, 56.988521, 0.0], [0.0, 56.988521, -0.054255], [0.0, 57.042771, 0.0], [0.0, 56.988521, 0.054255], [0.0, 56.934266, 0.0], [-0.054255, 56.988521, 0.0], [0.0, 57.042771, 0.0], [0.054255, 56.988521, 0.0], [0.0, 56.934266, 0.0], [0.0, 56.988521, -0.054255], [0.0, 57.042771, 0.0], [0.0, 51.870166, 0.0]]}, {"shapeName": "C_spine_FK_0_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 51.870166, -0.054255], [-5.118355, 51.815911, 0.0], [-5.118355, 51.870166, 0.054255], [-5.118355, 51.924421, 0.0], [-5.118355, 51.870166, -0.054255], [-5.172605, 51.870166, 0.0], [-5.118355, 51.870166, 0.054255], [-5.0641, 51.870166, 0.0], [-5.118355, 51.815911, 0.0], [-5.172605, 51.870166, 0.0], [-5.118355, 51.924421, 0.0], [-5.0641, 51.870166, 0.0], [-5.118355, 51.870166, -0.054255], [-5.172605, 51.870166, 0.0], [0.0, 51.870166, 0.0]]}, {"shapeName": "C_spine_FK_0_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 51.870166, 5.118355], [0.0, 51.815911, 5.118355], [0.054255, 51.870166, 5.118355], [0.0, 51.924421, 5.118355], [-0.054255, 51.870166, 5.118355], [0.0, 51.870166, 5.172605], [0.054255, 51.870166, 5.118355], [0.0, 51.870166, 5.0641], [0.0, 51.815911, 5.118355], [0.0, 51.870166, 5.172605], [0.0, 51.924421, 5.118355], [0.0, 51.870166, 5.0641], [-0.054255, 51.870166, 5.118355], [0.0, 51.870166, 5.172605], [0.0, 51.870166, 0.0]]}]},
			"L_loLeg_shaper_04_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_04_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[13.75, 9.942646, 0.833333], [13.816605, 9.543521, 0.786923], [14.006287, 9.20516, 0.747579], [14.290155, 8.979064, 0.721289], [14.625, 8.899673, 0.712057], [14.959845, 8.979064, 0.721289], [15.243712, 9.20516, 0.747579], [15.433395, 9.543521, 0.786923], [15.5, 9.942646, 0.833333], [15.433395, 10.34177, 0.879743], [15.243712, 10.680132, 0.919088], [14.959845, 10.906227, 0.945378], [14.625, 10.985618, 0.954609], [14.290155, 10.906227, 0.945378], [14.006287, 10.680132, 0.919088], [13.816605, 10.34177, 0.879743], [13.75, 9.942646, 0.833333], [5.0, 9.942646, 0.833333]]}]},
			"R_elbow_shaper_02_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_02_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-42.25, 93.350166, -3.75], [-42.305069, 93.361584, -3.733803], [-42.351755, 93.394101, -3.720072], [-42.382951, 93.442764, -3.710897], [-42.393905, 93.500166, -3.707675], [-42.382951, 93.557568, -3.710897], [-42.351755, 93.606231, -3.720072], [-42.305069, 93.638748, -3.733803], [-42.25, 93.650166, -3.75], [-42.194931, 93.638748, -3.766197], [-42.148245, 93.606231, -3.779928], [-42.117049, 93.557568, -3.789103], [-42.106095, 93.500166, -3.792325], [-42.117049, 93.442764, -3.789103], [-42.148245, 93.394101, -3.779928], [-42.194931, 93.361584, -3.766197], [-42.25, 93.350166, -3.75], [-42.25, 91.850166, -3.75]]}]},
			"R_loLeg_shaper_04_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_04_CTLShape", "degree": 1, "form": 0, "points": [[-17.5, 9.942646, 0.833333], [-17.59515, 9.372467, 0.767034], [-17.866125, 8.889094, 0.710827], [-18.27165, 8.5661, 0.67327], [-18.75, 8.452685, 0.660082], [-19.22835, 8.5661, 0.67327], [-19.633875, 8.889094, 0.710827], [-19.90485, 9.372467, 0.767034], [-20.0, 9.942646, 0.833333], [-19.90485, 10.512824, 0.899633], [-19.633875, 10.996197, 0.955839], [-19.22835, 11.319191, 0.993397], [-18.75, 11.432607, 1.006585], [-18.27165, 11.319191, 0.993397], [-17.866125, 10.996197, 0.955839], [-17.59515, 10.512824, 0.899633], [-17.5, 9.942646, 0.833333], [-5.0, 9.942646, 0.833333]]}]},
			"R_loLeg_shaper_04_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_04_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-13.75, 9.942646, 0.833333], [-13.816605, 9.543521, 0.786923], [-14.006287, 9.20516, 0.747579], [-14.290155, 8.979064, 0.721289], [-14.625, 8.899673, 0.712057], [-14.959845, 8.979064, 0.721289], [-15.243712, 9.20516, 0.747579], [-15.433395, 9.543521, 0.786923], [-15.5, 9.942646, 0.833333], [-15.433395, 10.34177, 0.879743], [-15.243712, 10.680132, 0.919088], [-14.959845, 10.906227, 0.945378], [-14.625, 10.985618, 0.954609], [-14.290155, 10.906227, 0.945378], [-14.006287, 10.680132, 0.919088], [-13.816605, 10.34177, 0.879743], [-13.75, 9.942646, 0.833333], [-5.0, 9.942646, 0.833333]]}]},
			"L_shoulder_shaper_04_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_shoulder_shaper_04_PIV_CTLShape", "degree": 1, "form": 0, "points": [[34.483421, 91.850166, -4.034434], [34.486325, 91.861017, -4.023979], [34.48923, 91.850166, -4.013524], [34.486325, 91.839315, -4.023979], [34.483421, 91.850166, -4.034434], [34.49678, 91.850166, -4.026883], [34.48923, 91.850166, -4.013524], [34.47587, 91.850166, -4.021075], [34.486325, 91.861017, -4.023979], [34.49678, 91.850166, -4.026883], [34.486325, 91.839315, -4.023979], [34.47587, 91.850166, -4.021075], [34.483421, 91.850166, -4.034434], [34.49678, 91.850166, -4.026883], [33.5, 91.850166, -3.75]]}, {"shapeName": "L_shoulder_shaper_04_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[33.497096, 92.873837, -3.760455], [33.489545, 92.873837, -3.747096], [33.502904, 92.873837, -3.739545], [33.510455, 92.873837, -3.752904], [33.497096, 92.873837, -3.760455], [33.5, 92.884687, -3.75], [33.502904, 92.873837, -3.739545], [33.5, 92.862986, -3.75], [33.489545, 92.873837, -3.747096], [33.5, 92.884687, -3.75], [33.510455, 92.873837, -3.752904], [33.5, 92.862986, -3.75], [33.497096, 92.873837, -3.760455], [33.5, 92.884687, -3.75], [33.5, 91.850166, -3.75]]}, {"shapeName": "L_shoulder_shaper_04_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[33.773979, 91.861017, -2.763675], [33.763524, 91.850166, -2.76077], [33.773979, 91.839315, -2.763675], [33.784434, 91.850166, -2.766579], [33.773979, 91.861017, -2.763675], [33.776883, 91.850166, -2.75322], [33.773979, 91.839315, -2.763675], [33.771075, 91.850166, -2.77413], [33.763524, 91.850166, -2.76077], [33.776883, 91.850166, -2.75322], [33.784434, 91.850166, -2.766579], [33.771075, 91.850166, -2.77413], [33.773979, 91.861017, -2.763675], [33.776883, 91.850166, -2.75322], [33.5, 91.850166, -3.75]]}]},
			"C_midNeck_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_midNeck_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 96.850166, -0.054255], [5.118355, 96.904421, 0.0], [5.118355, 96.850166, 0.054255], [5.118355, 96.795911, 0.0], [5.118355, 96.850166, -0.054255], [5.172605, 96.850166, 0.0], [5.118355, 96.850166, 0.054255], [5.0641, 96.850166, 0.0], [5.118355, 96.904421, 0.0], [5.172605, 96.850166, 0.0], [5.118355, 96.795911, 0.0], [5.0641, 96.850166, 0.0], [5.118355, 96.850166, -0.054255], [5.172605, 96.850166, 0.0], [0.0, 96.850166, 0.0]]}, {"shapeName": "C_midNeck_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 101.968521, -0.054255], [-0.054255, 101.968521, 0.0], [0.0, 101.968521, 0.054255], [0.054255, 101.968521, 0.0], [0.0, 101.968521, -0.054255], [0.0, 102.022771, 0.0], [0.0, 101.968521, 0.054255], [0.0, 101.914266, 0.0], [-0.054255, 101.968521, 0.0], [0.0, 102.022771, 0.0], [0.054255, 101.968521, 0.0], [0.0, 101.914266, 0.0], [0.0, 101.968521, -0.054255], [0.0, 102.022771, 0.0], [0.0, 96.850166, 0.0]]}, {"shapeName": "C_midNeck_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 96.904421, 5.118355], [-0.054255, 96.850166, 5.118355], [0.0, 96.795911, 5.118355], [0.054255, 96.850166, 5.118355], [0.0, 96.904421, 5.118355], [0.0, 96.850166, 5.172605], [0.0, 96.795911, 5.118355], [0.0, 96.850166, 5.0641], [-0.054255, 96.850166, 5.118355], [0.0, 96.850166, 5.172605], [0.054255, 96.850166, 5.118355], [0.0, 96.850166, 5.0641], [0.0, 96.904421, 5.118355], [0.0, 96.850166, 5.172605], [0.0, 96.850166, 0.0]]}]},
			"C_neck_FK_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 106.968521, -0.054255], [-0.054255, 106.968521, 0.0], [0.0, 106.968521, 0.054255], [0.054255, 106.968521, 0.0], [0.0, 106.968521, -0.054255], [0.0, 107.022771, 0.0], [0.0, 106.968521, 0.054255], [0.0, 106.914266, 0.0], [-0.054255, 106.968521, 0.0], [0.0, 107.022771, 0.0], [0.054255, 106.968521, 0.0], [0.0, 106.914266, 0.0], [0.0, 106.968521, -0.054255], [0.0, 107.022771, 0.0], [0.0, 101.850166, 0.0]]}, {"shapeName": "C_neck_FK_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 101.850166, -0.054255], [-5.118355, 101.795911, 0.0], [-5.118355, 101.850166, 0.054255], [-5.118355, 101.904421, 0.0], [-5.118355, 101.850166, -0.054255], [-5.172605, 101.850166, 0.0], [-5.118355, 101.850166, 0.054255], [-5.0641, 101.850166, 0.0], [-5.118355, 101.795911, 0.0], [-5.172605, 101.850166, 0.0], [-5.118355, 101.904421, 0.0], [-5.0641, 101.850166, 0.0], [-5.118355, 101.850166, -0.054255], [-5.172605, 101.850166, 0.0], [0.0, 101.850166, 0.0]]}, {"shapeName": "C_neck_FK_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 101.850166, 5.118355], [0.0, 101.795911, 5.118355], [0.054255, 101.850166, 5.118355], [0.0, 101.904421, 5.118355], [-0.054255, 101.850166, 5.118355], [0.0, 101.850166, 5.172605], [0.054255, 101.850166, 5.118355], [0.0, 101.850166, 5.0641], [0.0, 101.795911, 5.118355], [0.0, 101.850166, 5.172605], [0.0, 101.904421, 5.118355], [0.0, 101.850166, 5.0641], [-0.054255, 101.850166, 5.118355], [0.0, 101.850166, 5.172605], [0.0, 101.850166, 0.0]]}]},
			"R_shoulder_shaper_05_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_05_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-37.1, 93.350166, -4.75], [-37.155308, 93.361584, -4.765363], [-37.202196, 93.394101, -4.778388], [-37.233526, 93.442764, -4.787091], [-37.244528, 93.500166, -4.790147], [-37.233526, 93.557568, -4.787091], [-37.202196, 93.606231, -4.778388], [-37.155308, 93.638748, -4.765363], [-37.1, 93.650166, -4.75], [-37.044692, 93.638748, -4.734637], [-36.997804, 93.606231, -4.721612], [-36.966474, 93.557568, -4.712909], [-36.955472, 93.500166, -4.709853], [-36.966474, 93.442764, -4.712909], [-36.997804, 93.394101, -4.721612], [-37.044692, 93.361584, -4.734637], [-37.1, 93.350166, -4.75], [-37.1, 91.850166, -4.75]]}]},
			"C_chest_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[5.642006, 76.850166, -4.701672], [0.0, 79.250166, -6.649164], [-5.642006, 76.850166, -4.701672], [-7.978997, 74.450166, 0.0], [-5.642006, 76.850166, 4.701672], [0.0, 79.250166, 6.649164], [5.642006, 76.850166, 4.701672], [7.978997, 74.450166, 0.0]]}]},
			"L_heel_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_heel_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.118355, 0.275979, -1.304255], [10.118355, 0.330234, -1.25], [10.118355, 0.275979, -1.195745], [10.118355, 0.221724, -1.25], [10.118355, 0.275979, -1.304255], [10.172605, 0.275979, -1.25], [10.118355, 0.275979, -1.195745], [10.0641, 0.275979, -1.25], [10.118355, 0.330234, -1.25], [10.172605, 0.275979, -1.25], [10.118355, 0.221724, -1.25], [10.0641, 0.275979, -1.25], [10.118355, 0.275979, -1.304255], [10.172605, 0.275979, -1.25], [5.0, 0.275979, -1.25]]}, {"shapeName": "L_heel_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[5.0, 5.394334, -1.304255], [4.945745, 5.394334, -1.25], [5.0, 5.394334, -1.195745], [5.054255, 5.394334, -1.25], [5.0, 5.394334, -1.304255], [5.0, 5.448584, -1.25], [5.0, 5.394334, -1.195745], [5.0, 5.340079, -1.25], [4.945745, 5.394334, -1.25], [5.0, 5.448584, -1.25], [5.054255, 5.394334, -1.25], [5.0, 5.340079, -1.25], [5.0, 5.394334, -1.304255], [5.0, 5.448584, -1.25], [5.0, 0.275979, -1.25]]}, {"shapeName": "L_heel_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[5.0, 0.330234, 3.868355], [4.945745, 0.275979, 3.868355], [5.0, 0.221724, 3.868355], [5.054255, 0.275979, 3.868355], [5.0, 0.330234, 3.868355], [5.0, 0.275979, 3.922605], [5.0, 0.221724, 3.868355], [5.0, 0.275979, 3.8141], [4.945745, 0.275979, 3.868355], [5.0, 0.275979, 3.922605], [5.054255, 0.275979, 3.868355], [5.0, 0.275979, 3.8141], [5.0, 0.330234, 3.868355], [5.0, 0.275979, 3.922605], [5.0, 0.275979, -1.25]]}]},
			"L_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_D_CTLShape", "degree": 1, "form": 0, "points": [[67.717544, 92.744464, 0.75], [66.230702, 92.94271, 0.75], [66.230702, 92.94271, -0.75], [67.717544, 92.744464, -0.75], [67.519298, 91.257623, -0.75], [66.032456, 91.455868, -0.75], [66.032456, 91.455868, 0.75], [67.519298, 91.257623, 0.75], [67.717544, 92.744464, 0.75], [67.717544, 92.744464, -0.75], [66.230702, 92.94271, -0.75], [66.032456, 91.455868, -0.75], [67.519298, 91.257623, -0.75], [67.519298, 91.257623, 0.75], [66.032456, 91.455868, 0.75], [66.230702, 92.94271, 0.75]]}]},
			"R_loLeg_shaper_05_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_05_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.25, 6.359312, 0.416667], [-16.335635, 5.846152, 0.356997], [-16.579512, 5.411116, 0.306411], [-16.944485, 5.120422, 0.27261], [-17.375, 5.018347, 0.260741], [-17.805515, 5.120422, 0.27261], [-18.170488, 5.411116, 0.306411], [-18.414365, 5.846152, 0.356997], [-18.5, 6.359312, 0.416667], [-18.414365, 6.872473, 0.476336], [-18.170488, 7.307509, 0.526922], [-17.805515, 7.598203, 0.560724], [-17.375, 7.700277, 0.572593], [-16.944485, 7.598203, 0.560724], [-16.579512, 7.307509, 0.526922], [-16.335635, 6.872473, 0.476336], [-16.25, 6.359312, 0.416667], [-5.0, 6.359312, 0.416667]]}]},
			"R_loLeg_shaper_02_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_loLeg_shaper_02_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 12.018946, 1.129384], [-4.945745, 12.025213, 1.075492], [-5.0, 12.031479, 1.0216], [-5.054255, 12.025213, 1.075492], [-5.0, 12.018946, 1.129384], [-5.0, 11.971326, 1.069226], [-5.0, 12.031479, 1.0216], [-5.0, 12.079104, 1.081759], [-4.945745, 12.025213, 1.075492], [-5.0, 11.971326, 1.069226], [-5.054255, 12.025213, 1.075492], [-5.0, 12.079104, 1.081759], [-5.0, 12.018946, 1.129384], [-5.0, 11.971326, 1.069226], [-5.0, 17.109312, 1.666667]]}, {"shapeName": "R_loLeg_shaper_02_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 17.103046, 1.720559], [0.118355, 17.163204, 1.672933], [0.118355, 17.115579, 1.612775], [0.118355, 17.05542, 1.6604], [0.118355, 17.103046, 1.720559], [0.172605, 17.109312, 1.666667], [0.118355, 17.115579, 1.612775], [0.0641, 17.109312, 1.666667], [0.118355, 17.163204, 1.672933], [0.172605, 17.109312, 1.666667], [0.118355, 17.05542, 1.6604], [0.0641, 17.109312, 1.666667], [0.118355, 17.103046, 1.720559], [0.172605, 17.109312, 1.666667], [-5.0, 17.109312, 1.666667]]}, {"shapeName": "R_loLeg_shaper_02_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 17.700487, -3.417433], [-5.0, 17.754379, -3.411167], [-5.054255, 17.700487, -3.417433], [-5.0, 17.646595, -3.4237], [-4.945745, 17.700487, -3.417433], [-5.0, 17.706753, -3.47132], [-5.054255, 17.700487, -3.417433], [-5.0, 17.69422, -3.363541], [-5.0, 17.754379, -3.411167], [-5.0, 17.706753, -3.47132], [-5.0, 17.646595, -3.4237], [-5.0, 17.69422, -3.363541], [-4.945745, 17.700487, -3.417433], [-5.0, 17.706753, -3.47132], [-5.0, 17.109312, 1.666667]]}]},
			"R_lwrArmRibbonMid_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lwrArmRibbonMid_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-47.769748, 93.350169, -6.817145], [-47.769748, 94.250169, -6.817145], [-48.404623, 91.850166, -8.975717], [-47.769748, 89.450163, -6.817145], [-47.769748, 90.350163, -6.817145], [-46.92325, 90.350163, -3.939051], [-46.92325, 87.350166, -3.939051], [-47.1772, 87.350166, -4.80248], [-46.5, 85.100166, -2.5], [-45.8228, 87.350166, -0.19752], [-46.07675, 87.350166, -1.060949], [-46.07675, 90.350163, -1.060949], [-45.230252, 90.350163, 1.817145], [-45.230252, 89.450163, 1.817145], [-44.595377, 91.850166, 3.975717], [-45.230252, 94.250169, 1.817145], [-45.230252, 93.350169, 1.817145], [-46.07675, 93.350169, -1.060949], [-46.07675, 96.350166, -1.060949], [-45.8228, 96.350166, -0.19752], [-46.5, 98.600166, -2.5], [-47.1772, 96.350166, -4.80248], [-46.92325, 96.350166, -3.939051], [-46.92325, 93.350169, -3.939051], [-47.769748, 93.350169, -6.817145]]}]},
			"R_loLeg_shaper_03_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_03_CTLShape", "degree": 1, "form": 0, "points": [[-17.5, 13.525979, 1.25], [-17.59515, 12.955801, 1.1837], [-17.866125, 12.472428, 1.127494], [-18.27165, 12.149434, 1.089937], [-18.75, 12.036018, 1.076749], [-19.22835, 12.149434, 1.089937], [-19.633875, 12.472428, 1.127494], [-19.90485, 12.955801, 1.1837], [-20.0, 13.525979, 1.25], [-19.90485, 14.096157, 1.3163], [-19.633875, 14.57953, 1.372506], [-19.22835, 14.902524, 1.410063], [-18.75, 15.01594, 1.423251], [-18.27165, 14.902524, 1.410063], [-17.866125, 14.57953, 1.372506], [-17.59515, 14.096157, 1.3163], [-17.5, 13.525979, 1.25], [-5.0, 13.525979, 1.25]]}]},
			"R_elbow_shaper_03_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_03_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-46.5, 93.350166, -2.5], [-46.555069, 93.361584, -2.483803], [-46.601755, 93.394101, -2.470072], [-46.632951, 93.442764, -2.460897], [-46.643905, 93.500166, -2.457675], [-46.632951, 93.557568, -2.460897], [-46.601755, 93.606231, -2.470072], [-46.555069, 93.638748, -2.483803], [-46.5, 93.650166, -2.5], [-46.444931, 93.638748, -2.516197], [-46.398245, 93.606231, -2.529928], [-46.367049, 93.557568, -2.539103], [-46.356095, 93.500166, -2.542325], [-46.367049, 93.442764, -2.539103], [-46.398245, 93.394101, -2.529928], [-46.444931, 93.361584, -2.516197], [-46.5, 93.350166, -2.5], [-46.5, 91.850166, -2.5]]}]},
			"R_upLeg_shaper_01_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_01_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.25, 40.942646, 0.416667], [-16.335635, 40.430017, 0.480745], [-16.579512, 39.995432, 0.535068], [-16.944485, 39.705039, 0.571368], [-17.375, 39.60307, 0.584114], [-17.805515, 39.705039, 0.571368], [-18.170488, 39.995432, 0.535068], [-18.414365, 40.430017, 0.480745], [-18.5, 40.942646, 0.416667], [-18.414365, 41.455274, 0.352588], [-18.170488, 41.889859, 0.298265], [-17.805515, 42.180252, 0.261966], [-17.375, 42.282221, 0.24922], [-16.944485, 42.180252, 0.261966], [-16.579512, 41.889859, 0.298265], [-16.335635, 41.455274, 0.352588], [-16.25, 40.942646, 0.416667], [-5.0, 40.942646, 0.416667]]}]},
			"R_loLeg_shaper_03_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_03_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-13.75, 13.525979, 1.25], [-13.816605, 13.126854, 1.20359], [-14.006287, 12.788493, 1.164246], [-14.290155, 12.562397, 1.137956], [-14.625, 12.483006, 1.128724], [-14.959845, 12.562397, 1.137956], [-15.243712, 12.788493, 1.164246], [-15.433395, 13.126854, 1.20359], [-15.5, 13.525979, 1.25], [-15.433395, 13.925104, 1.29641], [-15.243712, 14.263465, 1.335754], [-14.959845, 14.489561, 1.362044], [-14.625, 14.568952, 1.371276], [-14.290155, 14.489561, 1.362044], [-14.006287, 14.263465, 1.335754], [-13.816605, 13.925104, 1.29641], [-13.75, 13.525979, 1.25], [-5.0, 13.525979, 1.25]]}]},
			"R_upLeg_shaper_04_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_04_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-12.5, 30.942646, 1.666667], [-12.55709, 30.600893, 1.709386], [-12.719675, 30.31117, 1.745601], [-12.96299, 30.117575, 1.769801], [-13.25, 30.049596, 1.778298], [-13.53701, 30.117575, 1.769801], [-13.780325, 30.31117, 1.745601], [-13.94291, 30.600893, 1.709386], [-14.0, 30.942646, 1.666667], [-13.94291, 31.284398, 1.623948], [-13.780325, 31.574121, 1.587732], [-13.53701, 31.767717, 1.563533], [-13.25, 31.835696, 1.555035], [-12.96299, 31.767717, 1.563533], [-12.719675, 31.574121, 1.587732], [-12.55709, 31.284398, 1.623948], [-12.5, 30.942646, 1.666667], [-5.0, 30.942646, 1.666667]]}]},
			"L_upLeg_shaper_04_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_shaper_04_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 25.870545, 2.355357], [4.945745, 25.863815, 2.30152], [5.0, 25.857086, 2.247684], [5.054255, 25.863815, 2.30152], [5.0, 25.870545, 2.355357], [5.0, 25.809984, 2.308249], [5.0, 25.857086, 2.247684], [5.0, 25.917651, 2.294791], [4.945745, 25.863815, 2.30152], [5.0, 25.809984, 2.308249], [5.054255, 25.863815, 2.30152], [5.0, 25.917651, 2.294791], [5.0, 25.870545, 2.355357], [5.0, 25.809984, 2.308249], [5.0, 30.942646, 1.666667]]}, {"shapeName": "L_upLeg_shaper_04_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 30.949375, 1.720503], [-0.118355, 30.996482, 1.659937], [-0.118355, 30.935916, 1.612831], [-0.118355, 30.88881, 1.673396], [-0.118355, 30.949375, 1.720503], [-0.172605, 30.942646, 1.666667], [-0.118355, 30.935916, 1.612831], [-0.0641, 30.942646, 1.666667], [-0.118355, 30.996482, 1.659937], [-0.172605, 30.942646, 1.666667], [-0.118355, 30.88881, 1.673396], [-0.0641, 30.942646, 1.666667], [-0.118355, 30.949375, 1.720503], [-0.172605, 30.942646, 1.666667], [5.0, 30.942646, 1.666667]]}, {"shapeName": "L_upLeg_shaper_04_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 30.307792, -3.412164], [5.0, 30.361628, -3.418893], [5.054255, 30.307792, -3.412164], [5.0, 30.253956, -3.405434], [4.945745, 30.307792, -3.412164], [5.0, 30.301063, -3.465995], [5.054255, 30.307792, -3.412164], [5.0, 30.314521, -3.358328], [5.0, 30.361628, -3.418893], [5.0, 30.301063, -3.465995], [5.0, 30.253956, -3.405434], [5.0, 30.314521, -3.358328], [4.945745, 30.307792, -3.412164], [5.0, 30.301063, -3.465995], [5.0, 30.942646, 1.666667]]}]},
			"L_upLeg_shaper_01_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_01_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[13.75, 40.942646, 0.416667], [13.816605, 40.543934, 0.466506], [14.006287, 40.205924, 0.508757], [14.290155, 39.980063, 0.53699], [14.625, 39.900754, 0.546903], [14.959845, 39.980063, 0.53699], [15.243712, 40.205924, 0.508757], [15.433395, 40.543934, 0.466506], [15.5, 40.942646, 0.416667], [15.433395, 41.341357, 0.366828], [15.243712, 41.679367, 0.324576], [14.959845, 41.905229, 0.296344], [14.625, 41.984537, 0.28643], [14.290155, 41.905229, 0.296344], [14.006287, 41.679367, 0.324576], [13.816605, 41.341357, 0.366828], [13.75, 40.942646, 0.416667], [5.0, 40.942646, 0.416667]]}]},
			"R_leg_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-7.345634, 3.126561, 0.040765], [-7.250129, 3.126561, 0.040765], [-7.232042, 3.029216, 0.029446], [-7.164176, 3.001285, 0.026198], [-7.082084, 3.057415, 0.032725], [-7.014551, 2.990334, 0.024925], [-7.071056, 2.9088, 0.015444], [-7.042949, 2.841379, 0.007605], [-6.944939, 2.823413, 0.005516], [-6.944939, 2.728545, -0.005516], [-7.042949, 2.710579, -0.007605], [-7.071056, 2.643167, -0.015443], [-7.014551, 2.561624, -0.024925], [-7.082084, 2.494543, -0.032725], [-7.164176, 2.550673, -0.026198], [-7.232042, 2.522742, -0.029446], [-7.250129, 2.425397, -0.040765], [-7.345634, 2.425397, -0.040765], [-7.36373, 2.522742, -0.029446], [-7.431596, 2.550673, -0.026198], [-7.513688, 2.494543, -0.032725], [-7.581215, 2.561624, -0.024925], [-7.524716, 2.643167, -0.015443], [-7.552823, 2.710579, -0.007605], [-7.650824, 2.728545, -0.005516], [-7.650824, 2.823413, 0.005516], [-7.552823, 2.841379, 0.007605], [-7.524716, 2.9088, 0.015444], [-7.581215, 2.990334, 0.024925], [-7.513688, 3.057415, 0.032725], [-7.431596, 3.001285, 0.026198], [-7.36373, 3.029216, 0.029446], [-7.345634, 3.126561, 0.040765]]}, {"shapeName": "R_leg_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-7.401548, 2.878953, 0.011974], [-7.44449, 2.775979, 0.0], [-7.401548, 2.673005, -0.011974], [-7.297883, 2.630359, -0.016933], [-7.194224, 2.673005, -0.011974], [-7.151282, 2.775979, -0.0], [-7.194224, 2.878953, 0.011974], [-7.297883, 2.921599, 0.016933]]}, {"shapeName": "R_leg_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-6.944939, 2.775979, -0.0], [-5.0, 2.775979, -0.0]]}]},
			"R_shoulder_shaper_01_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_01_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-20.9, 93.600166, -0.25], [-20.964526, 93.613487, -0.267924], [-21.019228, 93.651424, -0.283119], [-21.055781, 93.708197, -0.293272], [-21.068616, 93.775166, -0.296838], [-21.055781, 93.842135, -0.293272], [-21.019228, 93.898909, -0.283119], [-20.964526, 93.936845, -0.267924], [-20.9, 93.950166, -0.25], [-20.835474, 93.936845, -0.232076], [-20.780772, 93.898909, -0.216881], [-20.744219, 93.842135, -0.206728], [-20.731384, 93.775166, -0.203162], [-20.744219, 93.708197, -0.206728], [-20.780772, 93.651424, -0.216881], [-20.835474, 93.613487, -0.232076], [-20.9, 93.600166, -0.25], [-20.9, 91.850166, -0.25]]}]},
			"L_loLeg_shaper_04_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_04_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.25, 9.942646, 0.833333], [16.335635, 9.429485, 0.773664], [16.579512, 8.994449, 0.723078], [16.944485, 8.703755, 0.689276], [17.375, 8.601681, 0.677407], [17.805515, 8.703755, 0.689276], [18.170488, 8.994449, 0.723078], [18.414365, 9.429485, 0.773664], [18.5, 9.942646, 0.833333], [18.414365, 10.455806, 0.893003], [18.170488, 10.890842, 0.943589], [17.805515, 11.181536, 0.97739], [17.375, 11.283611, 0.989259], [16.944485, 11.181536, 0.97739], [16.579512, 10.890842, 0.943589], [16.335635, 10.455806, 0.893003], [16.25, 9.942646, 0.833333], [5.0, 9.942646, 0.833333]]}]},
			"L_upLeg_shaper_03_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_03_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[15.0, 34.275979, 1.25], [15.07612, 33.820309, 1.306959], [15.2929, 33.434011, 1.355246], [15.61732, 33.175884, 1.387512], [16.0, 33.085246, 1.398842], [16.38268, 33.175884, 1.387512], [16.7071, 33.434011, 1.355246], [16.92388, 33.820309, 1.306959], [17.0, 34.275979, 1.25], [16.92388, 34.731649, 1.193041], [16.7071, 35.117947, 1.144754], [16.38268, 35.376074, 1.112488], [16.0, 35.466712, 1.101158], [15.61732, 35.376074, 1.112488], [15.2929, 35.117947, 1.144754], [15.07612, 34.731649, 1.193041], [15.0, 34.275979, 1.25], [5.0, 34.275979, 1.25]]}]},
			"R_loLeg_shaper_03_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_03_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-12.5, 13.525979, 1.25], [-12.55709, 13.183872, 1.21022], [-12.719675, 12.893848, 1.176496], [-12.96299, 12.700052, 1.153962], [-13.25, 12.632002, 1.146049], [-13.53701, 12.700052, 1.153962], [-13.780325, 12.893848, 1.176496], [-13.94291, 13.183872, 1.21022], [-14.0, 13.525979, 1.25], [-13.94291, 13.868086, 1.28978], [-13.780325, 14.15811, 1.323504], [-13.53701, 14.351906, 1.346038], [-13.25, 14.419956, 1.353951], [-12.96299, 14.351906, 1.346038], [-12.719675, 14.15811, 1.323504], [-12.55709, 13.868086, 1.28978], [-12.5, 13.525979, 1.25], [-5.0, 13.525979, 1.25]]}]},
			"C_head_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.871393, 101.850166, -2.8125], [0.0, 101.850166, -5.625], [-4.871393, 101.850166, -2.8125], [-6.391891, 108.667198, 3.347848], [0.0, 108.667198, 8.543422], [6.391891, 108.667198, 3.347848], [4.871393, 101.850166, -2.8125]]}]},
			"C_chest_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[4.231505, 76.850166, -3.526254], [0.0, 78.650166, -4.986873], [-4.231505, 76.850166, -3.526254], [-5.984248, 75.050166, 0.0], [-4.231505, 76.850166, 3.526254], [0.0, 78.650166, 4.986873], [4.231505, 76.850166, 3.526254], [5.984248, 75.050166, 0.0]]}]},
			"R_shoulder_shaper_05_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_05_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-37.1, 93.850166, -4.75], [-37.173744, 93.86539, -4.770484], [-37.236261, 93.908746, -4.78785], [-37.278035, 93.97363, -4.799454], [-37.292704, 94.050166, -4.803529], [-37.278035, 94.126702, -4.799454], [-37.236261, 94.191586, -4.78785], [-37.173744, 94.234942, -4.770484], [-37.1, 94.250166, -4.75], [-37.026256, 94.234942, -4.729516], [-36.963739, 94.191586, -4.71215], [-36.921965, 94.126702, -4.700546], [-36.907296, 94.050166, -4.696471], [-36.921965, 93.97363, -4.700546], [-36.963739, 93.908746, -4.71215], [-37.026256, 93.86539, -4.729516], [-37.1, 93.850166, -4.75], [-37.1, 91.850166, -4.75]]}]},
			"L_elbow_shaper_04_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_04_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[50.75, 93.850166, -1.25], [50.823426, 93.86539, -1.228404], [50.885673, 93.908746, -1.210096], [50.927268, 93.97363, -1.197862], [50.941873, 94.050166, -1.193567], [50.927268, 94.126702, -1.197862], [50.885673, 94.191586, -1.210096], [50.823426, 94.234942, -1.228404], [50.75, 94.250166, -1.25], [50.676574, 94.234942, -1.271596], [50.614327, 94.191586, -1.289904], [50.572732, 94.126702, -1.302138], [50.558127, 94.050166, -1.306433], [50.572732, 93.97363, -1.302138], [50.614327, 93.908746, -1.289904], [50.676574, 93.86539, -1.271596], [50.75, 93.850166, -1.25], [50.75, 91.850166, -1.25]]}]},
			"R_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_C_CTLShape", "degree": 1, "form": 0, "points": [[-65.80742, 92.937969, -1.75], [-64.312197, 93.057587, -1.75], [-64.312197, 93.057587, -3.25], [-65.80742, 92.937969, -3.25], [-65.687803, 91.442746, -3.25], [-64.19258, 91.562364, -3.25], [-64.19258, 91.562364, -1.75], [-65.687803, 91.442746, -1.75], [-65.80742, 92.937969, -1.75], [-65.80742, 92.937969, -3.25], [-64.312197, 93.057587, -3.25], [-64.19258, 91.562364, -3.25], [-65.687803, 91.442746, -3.25], [-65.687803, 91.442746, -1.75], [-64.19258, 91.562364, -1.75], [-64.312197, 93.057587, -1.75]]}]},
			"R_arm_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-35.0, 101.850166, 0.349834], [-35.0, 101.850166, -0.349834], [-35.0, 101.850166, -0.0], [-34.650166, 101.850166, -0.0], [-35.349834, 101.850166, -0.0], [-35.0, 101.850166, -0.0], [-35.0, 102.2, -0.0], [-35.0, 101.500332, -0.0]]}]},
			"R_wristFk_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_wristFk_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-56.023671, 91.850166, -0.010851], [-56.023671, 91.861017, 0.0], [-56.023671, 91.850166, 0.010851], [-56.023671, 91.839315, -0.0], [-56.023671, 91.850166, -0.010851], [-56.034521, 91.850166, -0.0], [-56.023671, 91.850166, 0.010851], [-56.01282, 91.850166, -0.0], [-56.023671, 91.861017, 0.0], [-56.034521, 91.850166, -0.0], [-56.023671, 91.839315, -0.0], [-56.01282, 91.850166, -0.0], [-56.023671, 91.850166, -0.010851], [-56.034521, 91.850166, -0.0], [-55.0, 91.850166, -0.0]]}, {"shapeName": "R_wristFk_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-55.0, 92.873837, -0.010851], [-54.989149, 92.873837, 0.0], [-55.0, 92.873837, 0.010851], [-55.010851, 92.873837, 0.0], [-55.0, 92.873837, -0.010851], [-55.0, 92.884687, 0.0], [-55.0, 92.873837, 0.010851], [-55.0, 92.862986, 0.0], [-54.989149, 92.873837, 0.0], [-55.0, 92.884687, 0.0], [-55.010851, 92.873837, 0.0], [-55.0, 92.862986, 0.0], [-55.0, 92.873837, -0.010851], [-55.0, 92.884687, 0.0], [-55.0, 91.850166, -0.0]]}, {"shapeName": "R_wristFk_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-55.0, 91.861017, 1.023671], [-54.989149, 91.850166, 1.023671], [-55.0, 91.839315, 1.023671], [-55.010851, 91.850166, 1.023671], [-55.0, 91.861017, 1.023671], [-55.0, 91.850166, 1.034521], [-55.0, 91.839315, 1.023671], [-55.0, 91.850166, 1.01282], [-54.989149, 91.850166, 1.023671], [-55.0, 91.850166, 1.034521], [-55.010851, 91.850166, 1.023671], [-55.0, 91.850166, 1.01282], [-55.0, 91.861017, 1.023671], [-55.0, 91.850166, 1.034521], [-55.0, 91.850166, -0.0]]}]},
			"C_chest_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_chest_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 76.850166, -0.054255], [5.118355, 76.904421, 0.0], [5.118355, 76.850166, 0.054255], [5.118355, 76.795911, 0.0], [5.118355, 76.850166, -0.054255], [5.172605, 76.850166, 0.0], [5.118355, 76.850166, 0.054255], [5.0641, 76.850166, 0.0], [5.118355, 76.904421, 0.0], [5.172605, 76.850166, 0.0], [5.118355, 76.795911, 0.0], [5.0641, 76.850166, 0.0], [5.118355, 76.850166, -0.054255], [5.172605, 76.850166, 0.0], [0.0, 76.850166, 0.0]]}, {"shapeName": "C_chest_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 81.968521, -0.054255], [-0.054255, 81.968521, 0.0], [0.0, 81.968521, 0.054255], [0.054255, 81.968521, 0.0], [0.0, 81.968521, -0.054255], [0.0, 82.022771, 0.0], [0.0, 81.968521, 0.054255], [0.0, 81.914266, 0.0], [-0.054255, 81.968521, 0.0], [0.0, 82.022771, 0.0], [0.054255, 81.968521, 0.0], [0.0, 81.914266, 0.0], [0.0, 81.968521, -0.054255], [0.0, 82.022771, 0.0], [0.0, 76.850166, 0.0]]}, {"shapeName": "C_chest_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 76.904421, 5.118355], [-0.054255, 76.850166, 5.118355], [0.0, 76.795911, 5.118355], [0.054255, 76.850166, 5.118355], [0.0, 76.904421, 5.118355], [0.0, 76.850166, 5.172605], [0.0, 76.795911, 5.118355], [0.0, 76.850166, 5.0641], [-0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.172605], [0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.0641], [0.0, 76.904421, 5.118355], [0.0, 76.850166, 5.172605], [0.0, 76.850166, 0.0]]}]},
			"L_uprArmRibbonMid_CTL": {"color": 17, "shapes": [{"shapeName": "L_uprArmRibbonMid_CTLShape", "degree": 1, "form": 0, "points": [[27.661781, 93.516836, -7.31759], [27.661781, 94.516836, -7.31759], [26.992671, 91.850166, -9.726384], [27.661781, 89.183496, -7.31759], [27.661781, 90.183496, -7.31759], [28.553926, 90.183496, -4.105866], [28.553926, 86.850166, -4.105866], [28.286282, 86.850166, -5.069384], [29.0, 84.350166, -2.5], [29.713718, 86.850166, 0.069384], [29.446074, 86.850166, -0.894134], [29.446074, 90.183496, -0.894134], [30.338219, 90.183496, 2.31759], [30.338219, 89.183496, 2.31759], [31.007329, 91.850166, 4.726384], [30.338219, 94.516836, 2.31759], [30.338219, 93.516836, 2.31759], [29.446074, 93.516836, -0.894134], [29.446074, 96.850166, -0.894134], [29.713718, 96.850166, 0.069384], [29.0, 99.350166, -2.5], [28.286282, 96.850166, -5.069384], [28.553926, 96.850166, -4.105866], [28.553926, 93.516836, -4.105866], [27.661781, 93.516836, -7.31759]]}]},
			"L_scapulaCtrl_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_scapulaCtrl_CTLShape", "degree": 1, "form": 0, "points": [[11.5, 91.850166, -12.5], [14.5, 91.850166, -12.5], [14.5, 91.850166, -15.5], [11.5, 91.850166, -15.5], [11.5, 91.850166, -12.5]]}]},
			"L_elbow_shaper_05_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_05_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[54.15, 93.850166, -0.25], [54.223426, 93.86539, -0.228404], [54.285673, 93.908746, -0.210096], [54.327268, 93.97363, -0.197862], [54.341873, 94.050166, -0.193567], [54.327268, 94.126702, -0.197862], [54.285673, 94.191586, -0.210096], [54.223426, 94.234942, -0.228404], [54.15, 94.250166, -0.25], [54.076574, 94.234942, -0.271596], [54.014327, 94.191586, -0.289904], [53.972732, 94.126702, -0.302138], [53.958127, 94.050166, -0.306433], [53.972732, 93.97363, -0.302138], [54.014327, 93.908746, -0.289904], [54.076574, 93.86539, -0.271596], [54.15, 93.850166, -0.25], [54.15, 91.850166, -0.25]]}]},
			"R_wristFk_CTL": {"color": 6, "shapes": [{"shapeName": "R_wristFk_CTLShape", "degree": 1, "form": 0, "points": [[-57.75, 94.350166, 2.5], [-52.75, 94.350166, 2.5], [-52.75, 94.350166, -2.5], [-57.75, 94.350166, -2.5], [-57.75, 89.350166, -2.5], [-52.75, 89.350166, -2.5], [-52.75, 89.350166, 2.5], [-57.75, 89.350166, 2.5], [-57.75, 94.350166, 2.5], [-57.75, 94.350166, -2.5], [-52.75, 94.350166, -2.5], [-52.75, 89.350166, -2.5], [-57.75, 89.350166, -2.5], [-57.75, 89.350166, 2.5], [-52.75, 89.350166, 2.5], [-52.75, 94.350166, 2.5]]}]},
			"R_loLeg_shaper_03_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_loLeg_shaper_03_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 8.435613, 0.712717], [-4.945745, 8.441879, 0.658826], [-5.0, 8.448146, 0.604934], [-5.054255, 8.441879, 0.658826], [-5.0, 8.435613, 0.712717], [-5.0, 8.387992, 0.65256], [-5.0, 8.448146, 0.604934], [-5.0, 8.495771, 0.665092], [-4.945745, 8.441879, 0.658826], [-5.0, 8.387992, 0.65256], [-5.054255, 8.441879, 0.658826], [-5.0, 8.495771, 0.665092], [-5.0, 8.435613, 0.712717], [-5.0, 8.387992, 0.65256], [-5.0, 13.525979, 1.25]]}, {"shapeName": "R_loLeg_shaper_03_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 13.519713, 1.303892], [0.118355, 13.579871, 1.256266], [0.118355, 13.532246, 1.196108], [0.118355, 13.472087, 1.243734], [0.118355, 13.519713, 1.303892], [0.172605, 13.525979, 1.25], [0.118355, 13.532246, 1.196108], [0.0641, 13.525979, 1.25], [0.118355, 13.579871, 1.256266], [0.172605, 13.525979, 1.25], [0.118355, 13.472087, 1.243734], [0.0641, 13.525979, 1.25], [0.118355, 13.519713, 1.303892], [0.172605, 13.525979, 1.25], [-5.0, 13.525979, 1.25]]}, {"shapeName": "R_loLeg_shaper_03_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 14.117153, -3.8341], [-5.0, 14.171045, -3.827833], [-5.054255, 14.117153, -3.8341], [-5.0, 14.063262, -3.840366], [-4.945745, 14.117153, -3.8341], [-5.0, 14.123419, -3.887987], [-5.054255, 14.117153, -3.8341], [-5.0, 14.110887, -3.780208], [-5.0, 14.171045, -3.827833], [-5.0, 14.123419, -3.887987], [-5.0, 14.063262, -3.840366], [-5.0, 14.110887, -3.780208], [-4.945745, 14.117153, -3.8341], [-5.0, 14.123419, -3.887987], [-5.0, 13.525979, 1.25]]}]},
			"R_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_D_CTLShape", "degree": 1, "form": 0, "points": [[-67.717544, 92.744464, 0.75], [-66.230702, 92.94271, 0.75], [-66.230702, 92.94271, -0.75], [-67.717544, 92.744464, -0.75], [-67.519298, 91.257623, -0.75], [-66.032456, 91.455868, -0.75], [-66.032456, 91.455868, 0.75], [-67.519298, 91.257623, 0.75], [-67.717544, 92.744464, 0.75], [-67.717544, 92.744464, -0.75], [-66.230702, 92.94271, -0.75], [-66.032456, 91.455868, -0.75], [-67.519298, 91.257623, -0.75], [-67.519298, 91.257623, 0.75], [-66.032456, 91.455868, 0.75], [-66.230702, 92.94271, 0.75]]}]},
			"C_head_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 106.968521, -0.054255], [-0.054255, 106.968521, 0.0], [0.0, 106.968521, 0.054255], [0.054255, 106.968521, 0.0], [0.0, 106.968521, -0.054255], [0.0, 107.022771, 0.0], [0.0, 106.968521, 0.054255], [0.0, 106.914266, 0.0], [-0.054255, 106.968521, 0.0], [0.0, 107.022771, 0.0], [0.054255, 106.968521, 0.0], [0.0, 106.914266, 0.0], [0.0, 106.968521, -0.054255], [0.0, 107.022771, 0.0], [0.0, 101.850166, 0.0]]}, {"shapeName": "C_head_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 101.850166, -0.054255], [-5.118355, 101.795911, 0.0], [-5.118355, 101.850166, 0.054255], [-5.118355, 101.904421, 0.0], [-5.118355, 101.850166, -0.054255], [-5.172605, 101.850166, 0.0], [-5.118355, 101.850166, 0.054255], [-5.0641, 101.850166, 0.0], [-5.118355, 101.795911, 0.0], [-5.172605, 101.850166, 0.0], [-5.118355, 101.904421, 0.0], [-5.0641, 101.850166, 0.0], [-5.118355, 101.850166, -0.054255], [-5.172605, 101.850166, 0.0], [0.0, 101.850166, 0.0]]}, {"shapeName": "C_head_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 101.850166, 5.118355], [0.0, 101.795911, 5.118355], [0.054255, 101.850166, 5.118355], [0.0, 101.904421, 5.118355], [-0.054255, 101.850166, 5.118355], [0.0, 101.850166, 5.172605], [0.054255, 101.850166, 5.118355], [0.0, 101.850166, 5.0641], [0.0, 101.795911, 5.118355], [0.0, 101.850166, 5.172605], [0.0, 101.904421, 5.118355], [0.0, 101.850166, 5.0641], [-0.054255, 101.850166, 5.118355], [0.0, 101.850166, 5.172605], [0.0, 101.850166, 0.0]]}]},
			"R_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_C_CTLShape", "degree": 1, "form": 0, "points": [[-65.80742, 92.937969, -0.5], [-64.312197, 93.057587, -0.5], [-64.312197, 93.057587, -2.0], [-65.80742, 92.937969, -2.0], [-65.687803, 91.442746, -2.0], [-64.19258, 91.562364, -2.0], [-64.19258, 91.562364, -0.5], [-65.687803, 91.442746, -0.5], [-65.80742, 92.937969, -0.5], [-65.80742, 92.937969, -2.0], [-64.312197, 93.057587, -2.0], [-64.19258, 91.562364, -2.0], [-65.687803, 91.442746, -2.0], [-65.687803, 91.442746, -0.5], [-64.19258, 91.562364, -0.5], [-64.312197, 93.057587, -0.5]]}]},
			"R_clavicle_CTL": {"color": 13, "shapes": [{"shapeName": "R_clavicle_CTLShape", "degree": 3, "form": 0, "points": [[-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-2.831885, 91.850166, -4.136168], [-0.537339, 91.850166, -10.828593], [0.339102, 91.850166, -13.38488], [-0.537339, 100.167156, -10.828593], [-2.831885, 105.307346, -4.136168], [-5.668115, 105.307346, 4.136168], [-7.962661, 100.167156, 10.828593], [-8.839102, 91.850166, 13.38488], [-7.962661, 91.850166, 10.828593], [-5.668115, 91.850166, 4.136168], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0]]}]},
			"L_upLeg_shaper_01_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_01_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.25, 40.942646, 0.416667], [16.335635, 40.430017, 0.480745], [16.579512, 39.995432, 0.535068], [16.944485, 39.705039, 0.571368], [17.375, 39.60307, 0.584114], [17.805515, 39.705039, 0.571368], [18.170488, 39.995432, 0.535068], [18.414365, 40.430017, 0.480745], [18.5, 40.942646, 0.416667], [18.414365, 41.455274, 0.352588], [18.170488, 41.889859, 0.298265], [17.805515, 42.180252, 0.261966], [17.375, 42.282221, 0.24922], [16.944485, 42.180252, 0.261966], [16.579512, 41.889859, 0.298265], [16.335635, 41.455274, 0.352588], [16.25, 40.942646, 0.416667], [5.0, 40.942646, 0.416667]]}]},
			"C_midSpine_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midSpine_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[4.936756, 64.350166, -4.113963], [0.0, 64.350166, -5.818018], [-4.936756, 64.350166, -4.113963], [-6.981622, 64.350166, 0.0], [-4.936756, 64.350166, 4.113963], [0.0, 64.350166, 5.818018], [4.936756, 64.350166, 4.113963], [6.981622, 64.350166, 0.0]]}]},
			"L_elbowUpVectorIk_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_elbowUpVectorIk_PIV_CTLShape", "degree": 1, "form": 0, "points": [[39.023671, 91.850166, -25.010851], [39.023671, 91.861017, -25.0], [39.023671, 91.850166, -24.989149], [39.023671, 91.839315, -25.0], [39.023671, 91.850166, -25.010851], [39.034521, 91.850166, -25.0], [39.023671, 91.850166, -24.989149], [39.01282, 91.850166, -25.0], [39.023671, 91.861017, -25.0], [39.034521, 91.850166, -25.0], [39.023671, 91.839315, -25.0], [39.01282, 91.850166, -25.0], [39.023671, 91.850166, -25.010851], [39.034521, 91.850166, -25.0], [38.0, 91.850166, -25.0]]}, {"shapeName": "L_elbowUpVectorIk_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[38.0, 92.873837, -25.010851], [37.989149, 92.873837, -25.0], [38.0, 92.873837, -24.989149], [38.010851, 92.873837, -25.0], [38.0, 92.873837, -25.010851], [38.0, 92.884687, -25.0], [38.0, 92.873837, -24.989149], [38.0, 92.862986, -25.0], [37.989149, 92.873837, -25.0], [38.0, 92.884687, -25.0], [38.010851, 92.873837, -25.0], [38.0, 92.862986, -25.0], [38.0, 92.873837, -25.010851], [38.0, 92.884687, -25.0], [38.0, 91.850166, -25.0]]}, {"shapeName": "L_elbowUpVectorIk_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[38.0, 91.861017, -23.976329], [37.989149, 91.850166, -23.976329], [38.0, 91.839315, -23.976329], [38.010851, 91.850166, -23.976329], [38.0, 91.861017, -23.976329], [38.0, 91.850166, -23.965479], [38.0, 91.839315, -23.976329], [38.0, 91.850166, -23.98718], [37.989149, 91.850166, -23.976329], [38.0, 91.850166, -23.965479], [38.010851, 91.850166, -23.976329], [38.0, 91.850166, -23.98718], [38.0, 91.861017, -23.976329], [38.0, 91.850166, -23.965479], [38.0, 91.850166, -25.0]]}]},
			"R_upLeg_shaper_03_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_03_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.25, 34.275979, 1.25], [-16.335635, 33.76335, 1.314079], [-16.579512, 33.328765, 1.368402], [-16.944485, 33.038372, 1.404701], [-17.375, 32.936404, 1.417447], [-17.805515, 33.038372, 1.404701], [-18.170488, 33.328765, 1.368402], [-18.414365, 33.76335, 1.314079], [-18.5, 34.275979, 1.25], [-18.414365, 34.788608, 1.185921], [-18.170488, 35.223193, 1.131598], [-17.805515, 35.513586, 1.095299], [-17.375, 35.615554, 1.082553], [-16.944485, 35.513586, 1.095299], [-16.579512, 35.223193, 1.131598], [-16.335635, 34.788608, 1.185921], [-16.25, 34.275979, 1.25], [-5.0, 34.275979, 1.25]]}]},
			"L_leg_IK_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_leg_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.763127, 2.775979, -2.938545], [5.0, 2.775979, -4.155728], [3.236873, 2.775979, -2.938545], [2.506564, 2.775979, 0.0], [3.236873, 2.775979, 2.938545], [5.0, 2.775979, 4.155728], [6.763127, 2.775979, 2.938545], [7.493436, 2.775979, 0.0]]}]},
			"L_shoulder_shaper_03_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_03_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[29.0, 93.850166, -2.5], [29.073744, 93.86539, -2.520484], [29.136261, 93.908746, -2.53785], [29.178035, 93.97363, -2.549454], [29.192704, 94.050166, -2.553529], [29.178035, 94.126702, -2.549454], [29.136261, 94.191586, -2.53785], [29.073744, 94.234942, -2.520484], [29.0, 94.250166, -2.5], [28.926256, 94.234942, -2.479516], [28.863739, 94.191586, -2.46215], [28.821965, 94.126702, -2.450546], [28.807296, 94.050166, -2.446471], [28.821965, 93.97363, -2.450546], [28.863739, 93.908746, -2.46215], [28.926256, 93.86539, -2.479516], [29.0, 93.850166, -2.5], [29.0, 91.850166, -2.5]]}]},
			"L_arm_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[35.0, 101.850166, 0.39981], [35.0, 101.850166, -0.39981], [35.0, 101.850166, 0.0], [34.60019, 101.850166, 0.0], [35.39981, 101.850166, 0.0], [35.0, 101.850166, 0.0], [35.0, 102.249977, 0.0], [35.0, 101.450356, 0.0]]}]},
			"R_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-71.948456, 91.423739, -1.304255], [-71.955627, 91.477519, -1.25], [-71.948456, 91.423739, -1.195745], [-71.941286, 91.36996, -1.25], [-71.948456, 91.423739, -1.304255], [-72.00223, 91.41657, -1.25], [-71.948456, 91.423739, -1.195745], [-71.894677, 91.43091, -1.25], [-71.955627, 91.477519, -1.25], [-72.00223, 91.41657, -1.25], [-71.941286, 91.36996, -1.25], [-71.894677, 91.43091, -1.25], [-71.948456, 91.423739, -1.304255], [-72.00223, 91.41657, -1.25], [-66.875, 92.1002, -1.25]]}, {"shapeName": "R_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.551461, 97.173657, -1.304255], [-67.497682, 97.180827, -1.25], [-67.551461, 97.173657, -1.195745], [-67.60524, 97.166486, -1.25], [-67.551461, 97.173657, -1.304255], [-67.558631, 97.227431, -1.25], [-67.551461, 97.173657, -1.195745], [-67.54429, 97.119878, -1.25], [-67.497682, 97.180827, -1.25], [-67.558631, 97.227431, -1.25], [-67.60524, 97.166486, -1.25], [-67.54429, 97.119878, -1.25], [-67.551461, 97.173657, -1.304255], [-67.558631, 97.227431, -1.25], [-66.875, 92.1002, -1.25]]}, {"shapeName": "R_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-66.882171, 92.153979, 3.868355], [-66.821221, 92.107371, 3.868355], [-66.867829, 92.046421, 3.868355], [-66.928779, 92.09303, 3.868355], [-66.882171, 92.153979, 3.868355], [-66.875, 92.1002, 3.922605], [-66.867829, 92.046421, 3.868355], [-66.875, 92.1002, 3.8141], [-66.821221, 92.107371, 3.868355], [-66.875, 92.1002, 3.922605], [-66.928779, 92.09303, 3.868355], [-66.875, 92.1002, 3.8141], [-66.882171, 92.153979, 3.868355], [-66.875, 92.1002, 3.922605], [-66.875, 92.1002, -1.25]]}]},
			"L_lwrArmTwist_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lwrArmTwist_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[51.512573, 91.897761, -2.825383], [50.292941, 91.897761, -3.697006], [51.367124, 91.897761, -4.829456], [52.701536, 91.897761, -5.649254], [54.198141, 91.897761, -6.099791], [55.759997, 91.897761, -6.158218], [57.282541, 91.897761, -5.807134], [58.657959, 91.897761, -5.089042], [59.790409, 91.897761, -4.014859], [60.610208, 91.897761, -2.680447], [61.060745, 91.897761, -1.183843], [61.119171, 91.897761, 0.378013], [60.768087, 91.897761, 1.900558], [60.049996, 91.897761, 3.275976], [58.975813, 91.897761, 4.408426], [57.6414, 91.897761, 5.228225], [56.144796, 91.897761, 5.678761], [54.582941, 91.897761, 5.737188], [53.060396, 91.897761, 5.386104], [51.684977, 91.897761, 4.668013], [50.764326, 91.897761, 5.956249], [48.298564, 91.897761, 1.269023], [53.515385, 91.897761, 2.106785], [52.5566, 91.897761, 3.448381], [53.586802, 91.897761, 3.988855], [54.724899, 91.897761, 4.249444], [55.90119, 91.897761, 4.214883], [57.02528, 91.897761, 3.866634], [58.02527, 91.897761, 3.256958], [58.830364, 91.897761, 2.404354], [59.370838, 91.897761, 1.374151], [59.631428, 91.897761, 0.236054], [59.596866, 91.897761, -0.940237], [59.248617, 91.897761, -2.064326], [58.638942, 91.897761, -3.064317], [57.786337, 91.897761, -3.869411], [56.756135, 91.897761, -4.409885], [55.618038, 91.897761, -4.670474], [54.441747, 91.897761, -4.635913], [53.317658, 91.897761, -4.287664], [52.317666, 91.897761, -3.677988], [51.512573, 91.897761, -2.825383]]}]},
			"R_leg_IK_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-7.644691, 2.775979, -4.407818], [-5.0, 2.775979, -6.233591], [-2.355309, 2.775979, -4.407818], [-1.259845, 2.775979, -0.0], [-2.355309, 2.775979, 4.407818], [-5.0, 2.775979, 6.233591], [-7.644691, 2.775979, 4.407818], [-8.740155, 2.775979, 0.0]]}]},
			"L_lwrArmTwist_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lwrArmTwist_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[50.350097, 91.913626, -3.767178], [48.723922, 91.913626, -4.929342], [50.156166, 91.913626, -6.439274], [51.935382, 91.913626, -7.532339], [53.930854, 91.913626, -8.133055], [56.013329, 91.913626, -8.210957], [58.043388, 91.913626, -7.742845], [59.877279, 91.913626, -6.78539], [61.387212, 91.913626, -5.353146], [62.480278, 91.913626, -3.57393], [63.080993, 91.913626, -1.578457], [63.158895, 91.913626, 0.504018], [62.690783, 91.913626, 2.534077], [61.733328, 91.913626, 4.367968], [60.301084, 91.913626, 5.877901], [58.521867, 91.913626, 6.970966], [56.526395, 91.913626, 7.571682], [54.443921, 91.913626, 7.649584], [52.413861, 91.913626, 7.181472], [50.57997, 91.913626, 6.224017], [49.352434, 91.913626, 7.941665], [46.064752, 91.913626, 1.692031], [53.020514, 91.913626, 2.809047], [51.742134, 91.913626, 4.597841], [53.115736, 91.913626, 5.318473], [54.633199, 91.913626, 5.665926], [56.201586, 91.913626, 5.619844], [57.700373, 91.913626, 5.155512], [59.033694, 91.913626, 4.342611], [60.107152, 91.913626, 3.205805], [60.827784, 91.913626, 1.832202], [61.175237, 91.913626, 0.314739], [61.129155, 91.913626, -1.253649], [60.664823, 91.913626, -2.752434], [59.851922, 91.913626, -4.085756], [58.715116, 91.913626, -5.159214], [57.341513, 91.913626, -5.879846], [55.82405, 91.913626, -6.227298], [54.255662, 91.913626, -6.181218], [52.756877, 91.913626, -5.716886], [51.423555, 91.913626, -4.903984], [50.350097, 91.913626, -3.767178]]}]},
			"L_uprArmRibbonMid_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_uprArmRibbonMid_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[27.929425, 93.183502, -6.354072], [27.929425, 93.983502, -6.354072], [27.394137, 91.850166, -8.281107], [27.929425, 89.71683, -6.354072], [27.929425, 90.51683, -6.354072], [28.643141, 90.51683, -3.784693], [28.643141, 87.850166, -3.784693], [28.429026, 87.850166, -4.555507], [29.0, 85.850166, -2.5], [29.570974, 87.850166, -0.444493], [29.356859, 87.850166, -1.215307], [29.356859, 90.51683, -1.215307], [30.070575, 90.51683, 1.354072], [30.070575, 89.71683, 1.354072], [30.605863, 91.850166, 3.281107], [30.070575, 93.983502, 1.354072], [30.070575, 93.183502, 1.354072], [29.356859, 93.183502, -1.215307], [29.356859, 95.850166, -1.215307], [29.570974, 95.850166, -0.444493], [29.0, 97.850166, -2.5], [28.429026, 95.850166, -4.555507], [28.643141, 95.850166, -3.784693], [28.643141, 93.183502, -3.784693], [27.929425, 93.183502, -6.354072]]}]},
			"L_elbow_shaper_02_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_02_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[42.25, 93.850166, -3.75], [42.323426, 93.86539, -3.728404], [42.385673, 93.908746, -3.710096], [42.427268, 93.97363, -3.697862], [42.441873, 94.050166, -3.693567], [42.427268, 94.126702, -3.697862], [42.385673, 94.191586, -3.710096], [42.323426, 94.234942, -3.728404], [42.25, 94.250166, -3.75], [42.176574, 94.234942, -3.771596], [42.114327, 94.191586, -3.789904], [42.072732, 94.126702, -3.802138], [42.058127, 94.050166, -3.806433], [42.072732, 93.97363, -3.802138], [42.114327, 93.908746, -3.789904], [42.176574, 93.86539, -3.771596], [42.25, 93.850166, -3.75], [42.25, 91.850166, -3.75]]}]},
			"R_arm_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[-35.0, 101.850166, 0.499763], [-35.0, 101.850166, -0.499763], [-35.0, 101.850166, -0.0], [-34.500237, 101.850166, -0.0], [-35.499763, 101.850166, 0.0], [-35.0, 101.850166, -0.0], [-35.0, 102.349929, -0.0], [-35.0, 101.350403, -0.0]]}]},
			"L_uprArmRibbonMid_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_uprArmRibbonMid_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[28.197068, 92.850168, -5.390554], [28.197068, 93.450168, -5.390554], [27.795603, 91.850166, -6.835831], [28.197068, 90.250164, -5.390554], [28.197068, 90.850164, -5.390554], [28.732356, 90.850164, -3.46352], [28.732356, 88.850166, -3.46352], [28.571769, 88.850166, -4.041631], [29.0, 87.350166, -2.5], [29.428231, 88.850166, -0.958369], [29.267644, 88.850166, -1.53648], [29.267644, 90.850164, -1.53648], [29.802932, 90.850164, 0.390554], [29.802932, 90.250164, 0.390554], [30.204397, 91.850166, 1.835831], [29.802932, 93.450168, 0.390554], [29.802932, 92.850168, 0.390554], [29.267644, 92.850168, -1.53648], [29.267644, 94.850166, -1.53648], [29.428231, 94.850166, -0.958369], [29.0, 96.350166, -2.5], [28.571769, 94.850166, -4.041631], [28.732356, 94.850166, -3.46352], [28.732356, 92.850168, -3.46352], [28.197068, 92.850168, -5.390554]]}]},
			"L_bendyLeg_A_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.249999, 34.555057, 3.482625], [3.799999, 34.555057, 3.482625], [5.0, 34.694596, 4.598938], [6.200002, 34.555057, 3.482625], [5.750002, 34.555057, 3.482625], [5.750001, 34.369005, 1.99421], [7.25, 34.369005, 1.99421], [7.25, 34.424821, 2.440735], [8.375, 34.275979, 1.25], [7.25, 34.127137, 0.059265], [7.25, 34.182953, 0.50579], [5.750001, 34.182953, 0.50579], [5.750001, 33.996901, -0.982625], [6.200001, 33.996901, -0.982625], [5.0, 33.857362, -2.098938], [3.799998, 33.996901, -0.982625], [4.249998, 33.996901, -0.982625], [4.249998, 34.182953, 0.50579], [2.75, 34.182953, 0.50579], [2.75, 34.127137, 0.059265], [1.625, 34.275979, 1.25], [2.75, 34.424821, 2.440735], [2.75, 34.369005, 1.99421], [4.249998, 34.369005, 1.99421], [4.249999, 34.555057, 3.482625]]}]},
			"C_neckBase_CTL": {"color": 25, "shapes": [{"shapeName": "C_neckBase_CTLShape", "degree": 1, "form": 0, "points": [[6.492909, 95.587526, -5.221035], [-0.09519, 92.503638, -6.379919], [-7.158219, 94.200031, -5.158312], [-7.129524, 94.38476, 5.173304], [0.136296, 90.981938, 10.339684], [6.521604, 95.772255, 5.110581], [6.492909, 95.587526, -5.221035]]}]},
			"R_shoulder_shaper_01_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_01_CTLShape", "degree": 1, "form": 0, "points": [[-20.9, 94.350166, -0.25], [-20.99218, 94.369196, -0.275605], [-21.070326, 94.423391, -0.297313], [-21.122544, 94.504496, -0.311818], [-21.140879, 94.600166, -0.316911], [-21.122544, 94.695836, -0.311818], [-21.070326, 94.776941, -0.297313], [-20.99218, 94.831136, -0.275605], [-20.9, 94.850166, -0.25], [-20.80782, 94.831136, -0.224395], [-20.729674, 94.776941, -0.202687], [-20.677456, 94.695836, -0.188182], [-20.659121, 94.600166, -0.183089], [-20.677456, 94.504496, -0.188182], [-20.729674, 94.423391, -0.202687], [-20.80782, 94.369196, -0.224395], [-20.9, 94.350166, -0.25], [-20.9, 91.850166, -0.25]]}]},
			"R_elbowUpVectorIk_CTL": {"color": 13, "shapes": [{"shapeName": "R_elbowUpVectorIk_CTLShape", "degree": 1, "form": 0, "points": [[-36.5, 91.850166, -26.5], [-36.5, 91.850166, -23.5], [-39.5, 91.850166, -23.5], [-39.5, 91.850166, -26.5], [-36.5, 91.850166, -26.5], [-38.0, 93.350166, -25.0], [-39.5, 91.850166, -26.5], [-39.5, 91.850166, -23.5], [-38.0, 93.350166, -25.0], [-36.5, 91.850166, -23.5]]}]},
			"L_leg_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[7.345634, 3.126561, 0.040765], [7.250129, 3.126561, 0.040765], [7.232042, 3.029216, 0.029446], [7.164176, 3.001285, 0.026198], [7.082084, 3.057415, 0.032725], [7.014551, 2.990334, 0.024925], [7.071056, 2.9088, 0.015444], [7.042949, 2.841379, 0.007605], [6.944939, 2.823413, 0.005516], [6.944939, 2.728545, -0.005516], [7.042949, 2.710579, -0.007605], [7.071056, 2.643167, -0.015443], [7.014551, 2.561624, -0.024925], [7.082084, 2.494543, -0.032725], [7.164176, 2.550673, -0.026198], [7.232042, 2.522742, -0.029446], [7.250129, 2.425397, -0.040765], [7.345634, 2.425397, -0.040765], [7.36373, 2.522742, -0.029446], [7.431596, 2.550673, -0.026198], [7.513688, 2.494543, -0.032725], [7.581215, 2.561624, -0.024925], [7.524716, 2.643167, -0.015443], [7.552823, 2.710579, -0.007605], [7.650824, 2.728545, -0.005516], [7.650824, 2.823413, 0.005516], [7.552823, 2.841379, 0.007605], [7.524716, 2.9088, 0.015444], [7.581215, 2.990334, 0.024925], [7.513688, 3.057415, 0.032725], [7.431596, 3.001285, 0.026198], [7.36373, 3.029216, 0.029446], [7.345634, 3.126561, 0.040765]]}, {"shapeName": "L_leg_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[7.401548, 2.878953, 0.011974], [7.44449, 2.775979, 0.0], [7.401548, 2.673005, -0.011974], [7.297883, 2.630359, -0.016933], [7.194224, 2.673005, -0.011974], [7.151282, 2.775979, 0.0], [7.194224, 2.878953, 0.011974], [7.297883, 2.921599, 0.016933]]}, {"shapeName": "L_leg_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[6.944939, 2.775979, 0.0], [5.0, 2.775979, 0.0]]}]},
			"L_upLeg_shaper_04_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_04_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.25, 30.942646, 1.666667], [16.335635, 30.430017, 1.730745], [16.579512, 29.995432, 1.785068], [16.944485, 29.705039, 1.821368], [17.375, 29.60307, 1.834114], [17.805515, 29.705039, 1.821368], [18.170488, 29.995432, 1.785068], [18.414365, 30.430017, 1.730745], [18.5, 30.942646, 1.666667], [18.414365, 31.455274, 1.602588], [18.170488, 31.889859, 1.548265], [17.805515, 32.180252, 1.511966], [17.375, 32.282221, 1.49922], [16.944485, 32.180252, 1.511966], [16.579512, 31.889859, 1.548265], [16.335635, 31.455274, 1.602588], [16.25, 30.942646, 1.666667], [5.0, 30.942646, 1.666667]]}]},
			"L_arm_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[35.0, 101.850166, 0.299858], [35.0, 101.850166, -0.299858], [35.0, 101.850166, 0.0], [34.700142, 101.850166, 0.0], [35.299858, 101.850166, 0.0], [35.0, 101.850166, 0.0], [35.0, 102.150024, 0.0], [35.0, 101.550309, 0.0]]}]},
			"L_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[70.102054, 91.842002, 1.195745], [70.106381, 91.896084, 1.25], [70.102054, 91.842002, 1.304255], [70.097728, 91.78792, 1.25], [70.102054, 91.842002, 1.195745], [70.156132, 91.837676, 1.25], [70.102054, 91.842002, 1.304255], [70.047972, 91.846329, 1.25], [70.106381, 91.896084, 1.25], [70.156132, 91.837676, 1.25], [70.097728, 91.78792, 1.25], [70.047972, 91.846329, 1.25], [70.102054, 91.842002, 1.195745], [70.156132, 91.837676, 1.25], [65.0, 92.250166, 1.25]]}, {"shapeName": "L_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.408164, 97.352221, 1.195745], [65.354082, 97.356547, 1.25], [65.408164, 97.352221, 1.304255], [65.462247, 97.347894, 1.25], [65.408164, 97.352221, 1.195745], [65.412491, 97.406298, 1.25], [65.408164, 97.352221, 1.304255], [65.403838, 97.298139, 1.25], [65.354082, 97.356547, 1.25], [65.412491, 97.406298, 1.25], [65.462247, 97.347894, 1.25], [65.403838, 97.298139, 1.25], [65.408164, 97.352221, 1.195745], [65.412491, 97.406298, 1.25], [65.0, 92.250166, 1.25]]}, {"shapeName": "L_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.004327, 92.304249, 6.368355], [64.945918, 92.254493, 6.368355], [64.995673, 92.196084, 6.368355], [65.054082, 92.24584, 6.368355], [65.004327, 92.304249, 6.368355], [65.0, 92.250166, 6.422605], [64.995673, 92.196084, 6.368355], [65.0, 92.250166, 6.3141], [64.945918, 92.254493, 6.368355], [65.0, 92.250166, 6.422605], [65.054082, 92.24584, 6.368355], [65.0, 92.250166, 6.3141], [65.004327, 92.304249, 6.368355], [65.0, 92.250166, 6.422605], [65.0, 92.250166, 1.25]]}]},
			"L_elbowRibbon_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_elbowRibbon_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[38.022657, 92.850168, -7.999914], [38.022657, 93.450168, -7.999914], [38.033985, 91.850166, -9.499872], [38.022657, 90.250164, -7.999914], [38.022657, 90.850164, -7.999914], [38.007552, 90.850164, -5.999973], [38.007552, 88.850166, -5.999973], [38.012084, 88.850166, -6.599956], [38.0, 87.350166, -5.0], [37.987916, 88.850166, -3.400044], [37.992448, 88.850166, -4.000027], [37.992448, 90.850164, -4.000027], [37.977343, 90.850164, -2.000086], [37.977343, 90.250164, -2.000086], [37.966015, 91.850166, -0.500128], [37.977343, 93.450168, -2.000086], [37.977343, 92.850168, -2.000086], [37.992448, 92.850168, -4.000027], [37.992448, 94.850166, -4.000027], [37.987916, 94.850166, -3.400044], [38.0, 96.350166, -5.0], [38.012084, 94.850166, -6.599956], [38.007552, 94.850166, -5.999973], [38.007552, 92.850168, -5.999973], [38.022657, 92.850168, -7.999914]]}]},
			"C_chest_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[4.936756, 76.850166, -4.113963], [0.0, 78.950166, -5.818018], [-4.936756, 76.850166, -4.113963], [-6.981622, 74.750166, 0.0], [-4.936756, 76.850166, 4.113963], [0.0, 78.950166, 5.818018], [4.936756, 76.850166, 4.113963], [6.981622, 74.750166, 0.0]]}]},
			"L_bendyLeg_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_bendyLeg_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 19.157904, 2.576253], [4.945745, 19.157671, 2.521998], [5.0, 19.157438, 2.467744], [5.054255, 19.157671, 2.521998], [5.0, 19.157904, 2.576253], [5.0, 19.103422, 2.522231], [5.0, 19.157438, 2.467744], [5.0, 19.211926, 2.521765], [4.945745, 19.157671, 2.521998], [5.0, 19.103422, 2.522231], [5.054255, 19.157671, 2.521998], [5.0, 19.211926, 2.521765], [5.0, 19.157904, 2.576253], [5.0, 19.103422, 2.522231], [5.0, 24.275979, 2.5]]}, {"shapeName": "L_bendyLeg_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 24.276212, 2.554254], [-0.118355, 24.330233, 2.499767], [-0.118355, 24.275746, 2.445746], [-0.118355, 24.221724, 2.500233], [-0.118355, 24.276212, 2.554254], [-0.172605, 24.275979, 2.5], [-0.118355, 24.275746, 2.445746], [-0.0641, 24.275979, 2.5], [-0.118355, 24.330233, 2.499767], [-0.172605, 24.275979, 2.5], [-0.118355, 24.221724, 2.500233], [-0.0641, 24.275979, 2.5], [-0.118355, 24.276212, 2.554254], [-0.172605, 24.275979, 2.5], [5.0, 24.275979, 2.5]]}, {"shapeName": "L_bendyLeg_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 24.253981, -2.618308], [5.0, 24.308235, -2.618541], [5.054255, 24.253981, -2.618308], [5.0, 24.199726, -2.618075], [4.945745, 24.253981, -2.618308], [5.0, 24.253748, -2.672557], [5.054255, 24.253981, -2.618308], [5.0, 24.254214, -2.564053], [5.0, 24.308235, -2.618541], [5.0, 24.253748, -2.672557], [5.0, 24.199726, -2.618075], [5.0, 24.254214, -2.564053], [4.945745, 24.253981, -2.618308], [5.0, 24.253748, -2.672557], [5.0, 24.275979, 2.5]]}]},
			"C_head_right_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_right_CTLShape", "degree": 1, "form": 0, "points": [[-11.25, 113.100166, -3.75], [-11.25, 110.600166, -3.75], [-11.25, 110.600166, -6.25], [-11.25, 113.100166, -6.25], [-8.75, 113.100166, -6.25], [-8.75, 110.600166, -6.25], [-8.75, 110.600166, -3.75], [-8.75, 113.100166, -3.75], [-11.25, 113.100166, -3.75], [-11.25, 113.100166, -6.25], [-11.25, 110.600166, -6.25], [-8.75, 110.600166, -6.25], [-8.75, 113.100166, -6.25], [-8.75, 113.100166, -3.75], [-8.75, 110.600166, -3.75], [-11.25, 110.600166, -3.75]]}]},
			"R_elbow_shaper_05_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_05_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-54.15, 93.350166, -0.25], [-54.205069, 93.361584, -0.233803], [-54.251755, 93.394101, -0.220072], [-54.282951, 93.442764, -0.210897], [-54.293905, 93.500166, -0.207675], [-54.282951, 93.557568, -0.210897], [-54.251755, 93.606231, -0.220072], [-54.205069, 93.638748, -0.233803], [-54.15, 93.650166, -0.25], [-54.094931, 93.638748, -0.266197], [-54.048245, 93.606231, -0.279928], [-54.017049, 93.557568, -0.289103], [-54.006095, 93.500166, -0.292325], [-54.017049, 93.442764, -0.289103], [-54.048245, 93.394101, -0.279928], [-54.094931, 93.361584, -0.266197], [-54.15, 93.350166, -0.25], [-54.15, 91.850166, -0.25]]}]},
			"L_upLeg_shaper_01_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_shaper_01_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 35.870545, 1.105357], [4.945745, 35.863815, 1.05152], [5.0, 35.857086, 0.997684], [5.054255, 35.863815, 1.05152], [5.0, 35.870545, 1.105357], [5.0, 35.809984, 1.058249], [5.0, 35.857086, 0.997684], [5.0, 35.917651, 1.044791], [4.945745, 35.863815, 1.05152], [5.0, 35.809984, 1.058249], [5.054255, 35.863815, 1.05152], [5.0, 35.917651, 1.044791], [5.0, 35.870545, 1.105357], [5.0, 35.809984, 1.058249], [5.0, 40.942646, 0.416667]]}, {"shapeName": "L_upLeg_shaper_01_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 40.949375, 0.470503], [-0.118355, 40.996482, 0.409937], [-0.118355, 40.935916, 0.362831], [-0.118355, 40.88881, 0.423396], [-0.118355, 40.949375, 0.470503], [-0.172605, 40.942646, 0.416667], [-0.118355, 40.935916, 0.362831], [-0.0641, 40.942646, 0.416667], [-0.118355, 40.996482, 0.409937], [-0.172605, 40.942646, 0.416667], [-0.118355, 40.88881, 0.423396], [-0.0641, 40.942646, 0.416667], [-0.118355, 40.949375, 0.470503], [-0.172605, 40.942646, 0.416667], [5.0, 40.942646, 0.416667]]}, {"shapeName": "L_upLeg_shaper_01_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 40.307792, -4.662164], [5.0, 40.361628, -4.668893], [5.054255, 40.307792, -4.662164], [5.0, 40.253956, -4.655434], [4.945745, 40.307792, -4.662164], [5.0, 40.301063, -4.715995], [5.054255, 40.307792, -4.662164], [5.0, 40.314521, -4.608328], [5.0, 40.361628, -4.668893], [5.0, 40.301063, -4.715995], [5.0, 40.253956, -4.655434], [5.0, 40.314521, -4.608328], [4.945745, 40.307792, -4.662164], [5.0, 40.301063, -4.715995], [5.0, 40.942646, 0.416667]]}]},
			"L_elbow_shaper_01_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_01_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[38.85, 93.600166, -4.75], [38.914248, 93.613487, -4.731104], [38.968714, 93.651424, -4.715084], [39.005109, 93.708197, -4.70438], [39.017889, 93.775166, -4.700621], [39.005109, 93.842135, -4.70438], [38.968714, 93.898909, -4.715084], [38.914248, 93.936845, -4.731104], [38.85, 93.950166, -4.75], [38.785752, 93.936845, -4.768896], [38.731286, 93.898909, -4.784916], [38.694891, 93.842135, -4.79562], [38.682111, 93.775166, -4.799379], [38.694891, 93.708197, -4.79562], [38.731286, 93.651424, -4.784916], [38.785752, 93.613487, -4.768896], [38.85, 93.600166, -4.75], [38.85, 91.850166, -4.75]]}]},
			"L_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_C_CTLShape", "degree": 1, "form": 0, "points": [[65.80742, 92.937969, 2.0], [64.312197, 93.057587, 2.0], [64.312197, 93.057587, 0.5], [65.80742, 92.937969, 0.5], [65.687803, 91.442746, 0.5], [64.19258, 91.562364, 0.5], [64.19258, 91.562364, 2.0], [65.687803, 91.442746, 2.0], [65.80742, 92.937969, 2.0], [65.80742, 92.937969, 0.5], [64.312197, 93.057587, 0.5], [64.19258, 91.562364, 0.5], [65.687803, 91.442746, 0.5], [65.687803, 91.442746, 2.0], [64.19258, 91.562364, 2.0], [64.312197, 93.057587, 2.0]]}]},
			"L_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[71.948456, 91.423705, -1.304255], [71.955627, 91.477485, -1.25], [71.948456, 91.423705, -1.195745], [71.941286, 91.369926, -1.25], [71.948456, 91.423705, -1.304255], [72.00223, 91.416536, -1.25], [71.948456, 91.423705, -1.195745], [71.894677, 91.430876, -1.25], [71.955627, 91.477485, -1.25], [72.00223, 91.416536, -1.25], [71.941286, 91.369926, -1.25], [71.894677, 91.430876, -1.25], [71.948456, 91.423705, -1.304255], [72.00223, 91.416536, -1.25], [66.875, 92.100166, -1.25]]}, {"shapeName": "L_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.551461, 97.173623, -1.304255], [67.497682, 97.180793, -1.25], [67.551461, 97.173623, -1.195745], [67.60524, 97.166452, -1.25], [67.551461, 97.173623, -1.304255], [67.558631, 97.227397, -1.25], [67.551461, 97.173623, -1.195745], [67.54429, 97.119844, -1.25], [67.497682, 97.180793, -1.25], [67.558631, 97.227397, -1.25], [67.60524, 97.166452, -1.25], [67.54429, 97.119844, -1.25], [67.551461, 97.173623, -1.304255], [67.558631, 97.227397, -1.25], [66.875, 92.100166, -1.25]]}, {"shapeName": "L_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[66.882171, 92.153945, 3.868355], [66.821221, 92.107337, 3.868355], [66.867829, 92.046387, 3.868355], [66.928779, 92.092996, 3.868355], [66.882171, 92.153945, 3.868355], [66.875, 92.100166, 3.922605], [66.867829, 92.046387, 3.868355], [66.875, 92.100166, 3.8141], [66.821221, 92.107337, 3.868355], [66.875, 92.100166, 3.922605], [66.928779, 92.092996, 3.868355], [66.875, 92.100166, 3.8141], [66.882171, 92.153945, 3.868355], [66.875, 92.100166, 3.922605], [66.875, 92.100166, -1.25]]}]},
			"L_loLeg_shaper_01_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_01_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[12.5, 20.692646, 2.083333], [12.55709, 20.350539, 2.043553], [12.719675, 20.060515, 2.00983], [12.96299, 19.866719, 1.987295], [13.25, 19.798669, 1.979383], [13.53701, 19.866719, 1.987295], [13.780325, 20.060515, 2.00983], [13.94291, 20.350539, 2.043553], [14.0, 20.692646, 2.083333], [13.94291, 21.034753, 2.123113], [13.780325, 21.324777, 2.156837], [13.53701, 21.518573, 2.179371], [13.25, 21.586622, 2.187284], [12.96299, 21.518573, 2.179371], [12.719675, 21.324777, 2.156837], [12.55709, 21.034753, 2.123113], [12.5, 20.692646, 2.083333], [5.0, 20.692646, 2.083333]]}]},
			"R_lwrArmTwist_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lwrArmTwist_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-56.023671, 91.850166, -0.010851], [-56.023671, 91.861017, 0.0], [-56.023671, 91.850166, 0.010851], [-56.023671, 91.839315, -0.0], [-56.023671, 91.850166, -0.010851], [-56.034521, 91.850166, -0.0], [-56.023671, 91.850166, 0.010851], [-56.01282, 91.850166, -0.0], [-56.023671, 91.861017, 0.0], [-56.034521, 91.850166, -0.0], [-56.023671, 91.839315, -0.0], [-56.01282, 91.850166, -0.0], [-56.023671, 91.850166, -0.010851], [-56.034521, 91.850166, -0.0], [-55.0, 91.850166, -0.0]]}, {"shapeName": "R_lwrArmTwist_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-55.0, 92.873837, -0.010851], [-54.989149, 92.873837, 0.0], [-55.0, 92.873837, 0.010851], [-55.010851, 92.873837, 0.0], [-55.0, 92.873837, -0.010851], [-55.0, 92.884687, 0.0], [-55.0, 92.873837, 0.010851], [-55.0, 92.862986, 0.0], [-54.989149, 92.873837, 0.0], [-55.0, 92.884687, 0.0], [-55.010851, 92.873837, 0.0], [-55.0, 92.862986, 0.0], [-55.0, 92.873837, -0.010851], [-55.0, 92.884687, 0.0], [-55.0, 91.850166, -0.0]]}, {"shapeName": "R_lwrArmTwist_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-55.0, 91.861017, 1.023671], [-54.989149, 91.850166, 1.023671], [-55.0, 91.839315, 1.023671], [-55.010851, 91.850166, 1.023671], [-55.0, 91.861017, 1.023671], [-55.0, 91.850166, 1.034521], [-55.0, 91.839315, 1.023671], [-55.0, 91.850166, 1.01282], [-54.989149, 91.850166, 1.023671], [-55.0, 91.850166, 1.034521], [-55.010851, 91.850166, 1.023671], [-55.0, 91.850166, 1.01282], [-55.0, 91.861017, 1.023671], [-55.0, 91.850166, 1.034521], [-55.0, 91.850166, -0.0]]}]},
			"L_arm_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[35.0, 101.850166, 0.349834], [35.0, 101.850166, -0.349834], [35.0, 101.850166, 0.0], [34.650166, 101.850166, 0.0], [35.349834, 101.850166, 0.0], [35.0, 101.850166, 0.0], [35.0, 102.2, 0.0], [35.0, 101.500332, 0.0]]}]},
			"R_upLeg_shaper_01_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_01_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-12.5, 40.942646, 0.416667], [-12.55709, 40.600893, 0.459386], [-12.719675, 40.31117, 0.495601], [-12.96299, 40.117575, 0.519801], [-13.25, 40.049596, 0.528298], [-13.53701, 40.117575, 0.519801], [-13.780325, 40.31117, 0.495601], [-13.94291, 40.600893, 0.459386], [-14.0, 40.942646, 0.416667], [-13.94291, 41.284398, 0.373948], [-13.780325, 41.574121, 0.337732], [-13.53701, 41.767717, 0.313533], [-13.25, 41.835696, 0.305035], [-12.96299, 41.767717, 0.313533], [-12.719675, 41.574121, 0.337732], [-12.55709, 41.284398, 0.373948], [-12.5, 40.942646, 0.416667], [-5.0, 40.942646, 0.416667]]}]},
			"L_lwrArmRibbonMid_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lwrArmRibbonMid_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[47.769748, 93.350169, -6.817145], [47.769748, 94.250169, -6.817145], [48.404623, 91.850166, -8.975717], [47.769748, 89.450163, -6.817145], [47.769748, 90.350163, -6.817145], [46.92325, 90.350163, -3.939051], [46.92325, 87.350166, -3.939051], [47.1772, 87.350166, -4.80248], [46.5, 85.100166, -2.5], [45.8228, 87.350166, -0.19752], [46.07675, 87.350166, -1.060949], [46.07675, 90.350163, -1.060949], [45.230252, 90.350163, 1.817145], [45.230252, 89.450163, 1.817145], [44.595377, 91.850166, 3.975717], [45.230252, 94.250169, 1.817145], [45.230252, 93.350169, 1.817145], [46.07675, 93.350169, -1.060949], [46.07675, 96.350166, -1.060949], [45.8228, 96.350166, -0.19752], [46.5, 98.600166, -2.5], [47.1772, 96.350166, -4.80248], [46.92325, 96.350166, -3.939051], [46.92325, 93.350169, -3.939051], [47.769748, 93.350169, -6.817145]]}]},
			"L_leg_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 7.894334, -0.054255], [4.945745, 7.894334, 0.0], [5.0, 7.894334, 0.054255], [5.054255, 7.894334, 0.0], [5.0, 7.894334, -0.054255], [5.0, 7.948584, 0.0], [5.0, 7.894334, 0.054255], [5.0, 7.840079, 0.0], [4.945745, 7.894334, 0.0], [5.0, 7.948584, 0.0], [5.054255, 7.894334, 0.0], [5.0, 7.840079, 0.0], [5.0, 7.894334, -0.054255], [5.0, 7.948584, 0.0], [5.0, 2.775979, 0.0]]}, {"shapeName": "L_leg_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 2.775979, -0.054255], [-0.118355, 2.721724, 0.0], [-0.118355, 2.775979, 0.054255], [-0.118355, 2.830234, 0.0], [-0.118355, 2.775979, -0.054255], [-0.172605, 2.775979, 0.0], [-0.118355, 2.775979, 0.054255], [-0.0641, 2.775979, 0.0], [-0.118355, 2.721724, 0.0], [-0.172605, 2.775979, 0.0], [-0.118355, 2.830234, 0.0], [-0.0641, 2.775979, 0.0], [-0.118355, 2.775979, -0.054255], [-0.172605, 2.775979, 0.0], [5.0, 2.775979, 0.0]]}, {"shapeName": "L_leg_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 2.775979, 5.118355], [5.0, 2.721724, 5.118355], [5.054255, 2.775979, 5.118355], [5.0, 2.830234, 5.118355], [4.945745, 2.775979, 5.118355], [5.0, 2.775979, 5.172605], [5.054255, 2.775979, 5.118355], [5.0, 2.775979, 5.0641], [5.0, 2.721724, 5.118355], [5.0, 2.775979, 5.172605], [5.0, 2.830234, 5.118355], [5.0, 2.775979, 5.0641], [4.945745, 2.775979, 5.118355], [5.0, 2.775979, 5.172605], [5.0, 2.775979, 0.0]]}]},
			"L_shoulder_shaper_05_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_05_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[37.1, 93.600166, -4.75], [37.164526, 93.613487, -4.767924], [37.219228, 93.651424, -4.783119], [37.255781, 93.708197, -4.793272], [37.268616, 93.775166, -4.796838], [37.255781, 93.842135, -4.793272], [37.219228, 93.898909, -4.783119], [37.164526, 93.936845, -4.767924], [37.1, 93.950166, -4.75], [37.035474, 93.936845, -4.732076], [36.980772, 93.898909, -4.716881], [36.944219, 93.842135, -4.706728], [36.931384, 93.775166, -4.703162], [36.944219, 93.708197, -4.706728], [36.980772, 93.651424, -4.716881], [37.035474, 93.613487, -4.732076], [37.1, 93.600166, -4.75], [37.1, 91.850166, -4.75]]}]},
			"R_upLeg_shaper_01_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_01_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-13.75, 40.942646, 0.416667], [-13.816605, 40.543934, 0.466506], [-14.006287, 40.205924, 0.508757], [-14.290155, 39.980063, 0.53699], [-14.625, 39.900754, 0.546903], [-14.959845, 39.980063, 0.53699], [-15.243712, 40.205924, 0.508757], [-15.433395, 40.543934, 0.466506], [-15.5, 40.942646, 0.416667], [-15.433395, 41.341357, 0.366828], [-15.243712, 41.679367, 0.324576], [-14.959845, 41.905229, 0.296344], [-14.625, 41.984537, 0.28643], [-14.290155, 41.905229, 0.296344], [-14.006287, 41.679367, 0.324576], [-13.816605, 41.341357, 0.366828], [-13.75, 40.942646, 0.416667], [-5.0, 40.942646, 0.416667]]}]},
			"R_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_B_CTLShape", "degree": 1, "form": 0, "points": [[-63.812803, 92.907587, -1.75], [-62.31758, 92.787969, -1.75], [-62.31758, 92.787969, -3.25], [-63.812803, 92.907587, -3.25], [-63.93242, 91.412364, -3.25], [-62.437197, 91.292746, -3.25], [-62.437197, 91.292746, -1.75], [-63.93242, 91.412364, -1.75], [-63.812803, 92.907587, -1.75], [-63.812803, 92.907587, -3.25], [-62.31758, 92.787969, -3.25], [-62.437197, 91.292746, -3.25], [-63.93242, 91.412364, -3.25], [-63.93242, 91.412364, -1.75], [-62.437197, 91.292746, -1.75], [-62.31758, 92.787969, -1.75]]}]},
			"R_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_A_CTLShape", "degree": 1, "form": 0, "points": [[-61.239142, 91.627126, 3.779701], [-60.050826, 91.515871, 2.871116], [-60.425826, 92.814909, 2.221597], [-61.614142, 92.926164, 3.130182], [-62.449174, 92.184462, 2.128884], [-61.260858, 92.073207, 1.220299], [-60.885858, 90.774168, 1.869818], [-62.074174, 90.885424, 2.778403], [-61.239142, 91.627126, 3.779701], [-61.614142, 92.926164, 3.130182], [-60.425826, 92.814909, 2.221597], [-61.260858, 92.073207, 1.220299], [-62.449174, 92.184462, 2.128884], [-62.074174, 90.885424, 2.778403], [-60.885858, 90.774168, 1.869818], [-60.050826, 91.515871, 2.871116]]}]},
			"R_toe_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 0.330234, 10.118355], [-4.945745, 0.275979, 10.118355], [-5.0, 0.221724, 10.118355], [-5.054255, 0.275979, 10.118355], [-5.0, 0.330234, 10.118355], [-5.0, 0.275979, 10.172605], [-5.0, 0.221724, 10.118355], [-5.0, 0.275979, 10.0641], [-4.945745, 0.275979, 10.118355], [-5.0, 0.275979, 10.172605], [-5.054255, 0.275979, 10.118355], [-5.0, 0.275979, 10.0641], [-5.0, 0.330234, 10.118355], [-5.0, 0.275979, 10.172605], [-5.0, 0.275979, 5.0]]}, {"shapeName": "R_toe_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 0.330234, 5.0], [0.118355, 0.275979, 4.945745], [0.118355, 0.221724, 5.0], [0.118355, 0.275979, 5.054255], [0.118355, 0.330234, 5.0], [0.172605, 0.275979, 5.0], [0.118355, 0.221724, 5.0], [0.0641, 0.275979, 5.0], [0.118355, 0.275979, 4.945745], [0.172605, 0.275979, 5.0], [0.118355, 0.275979, 5.054255], [0.0641, 0.275979, 5.0], [0.118355, 0.330234, 5.0], [0.172605, 0.275979, 5.0], [-5.0, 0.275979, 5.0]]}, {"shapeName": "R_toe_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, -4.842376, 5.0], [-5.0, -4.842376, 4.945745], [-5.054255, -4.842376, 5.0], [-5.0, -4.842376, 5.054255], [-4.945745, -4.842376, 5.0], [-5.0, -4.896626, 5.0], [-5.054255, -4.842376, 5.0], [-5.0, -4.788121, 5.0], [-5.0, -4.842376, 4.945745], [-5.0, -4.896626, 5.0], [-5.0, -4.842376, 5.054255], [-5.0, -4.788121, 5.0], [-4.945745, -4.842376, 5.0], [-5.0, -4.896626, 5.0], [-5.0, 0.275979, 5.0]]}]},
			"R_elbow_shaper_01_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_01_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-38.85, 93.350166, -4.75], [-38.905069, 93.361584, -4.733803], [-38.951755, 93.394101, -4.720072], [-38.982951, 93.442764, -4.710897], [-38.993905, 93.500166, -4.707675], [-38.982951, 93.557568, -4.710897], [-38.951755, 93.606231, -4.720072], [-38.905069, 93.638748, -4.733803], [-38.85, 93.650166, -4.75], [-38.794931, 93.638748, -4.766197], [-38.748245, 93.606231, -4.779928], [-38.717049, 93.557568, -4.789103], [-38.706095, 93.500166, -4.792325], [-38.717049, 93.442764, -4.789103], [-38.748245, 93.394101, -4.779928], [-38.794931, 93.361584, -4.766197], [-38.85, 93.350166, -4.75], [-38.85, 91.850166, -4.75]]}]},
			"C_spine_FK_0_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_spine_FK_0_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 51.870166, -5.0], [5.0, 51.870166, 5.0], [-5.0, 51.870166, 5.0], [-5.0, 51.870166, -5.0], [5.0, 51.870166, -5.0]]}]},
			"R_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-70.102054, 91.842036, -2.554255], [-70.106381, 91.896118, -2.5], [-70.102054, 91.842036, -2.445745], [-70.097728, 91.787954, -2.5], [-70.102054, 91.842036, -2.554255], [-70.156132, 91.83771, -2.5], [-70.102054, 91.842036, -2.445745], [-70.047972, 91.846363, -2.5], [-70.106381, 91.896118, -2.5], [-70.156132, 91.83771, -2.5], [-70.097728, 91.787954, -2.5], [-70.047972, 91.846363, -2.5], [-70.102054, 91.842036, -2.554255], [-70.156132, 91.83771, -2.5], [-65.0, 92.2502, -2.5]]}, {"shapeName": "R_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.408164, 97.352255, -2.554255], [-65.354082, 97.356581, -2.5], [-65.408164, 97.352255, -2.445745], [-65.462247, 97.347928, -2.5], [-65.408164, 97.352255, -2.554255], [-65.412491, 97.406332, -2.5], [-65.408164, 97.352255, -2.445745], [-65.403838, 97.298173, -2.5], [-65.354082, 97.356581, -2.5], [-65.412491, 97.406332, -2.5], [-65.462247, 97.347928, -2.5], [-65.403838, 97.298173, -2.5], [-65.408164, 97.352255, -2.554255], [-65.412491, 97.406332, -2.5], [-65.0, 92.2502, -2.5]]}, {"shapeName": "R_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-65.004327, 92.304283, 2.618355], [-64.945918, 92.254527, 2.618355], [-64.995673, 92.196118, 2.618355], [-65.054082, 92.245874, 2.618355], [-65.004327, 92.304283, 2.618355], [-65.0, 92.2502, 2.672605], [-64.995673, 92.196118, 2.618355], [-65.0, 92.2502, 2.5641], [-64.945918, 92.254527, 2.618355], [-65.0, 92.2502, 2.672605], [-65.054082, 92.245874, 2.618355], [-65.0, 92.2502, 2.5641], [-65.004327, 92.304283, 2.618355], [-65.0, 92.2502, 2.672605], [-65.0, 92.2502, -2.5]]}]},
			"R_bendyLeg_A_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_A_CTLShape", "degree": 1, "form": 0, "points": [[-4.166665, 34.586066, 3.730695], [-3.666665, 34.586066, 3.730695], [-5.0, 34.741109, 4.971042], [-6.333335, 34.586066, 3.730695], [-5.833335, 34.586066, 3.730695], [-5.833335, 34.379341, 2.0769], [-7.5, 34.379341, 2.0769], [-7.5, 34.441359, 2.573039], [-8.75, 34.275979, 1.25], [-7.5, 34.110599, -0.073039], [-7.5, 34.172616, 0.4231], [-5.833335, 34.172616, 0.4231], [-5.833335, 33.965892, -1.230695], [-6.333335, 33.965892, -1.230695], [-5.0, 33.810849, -2.471042], [-3.666665, 33.965892, -1.230695], [-4.166665, 33.965892, -1.230695], [-4.166665, 34.172616, 0.4231], [-2.5, 34.172616, 0.4231], [-2.5, 34.110599, -0.073039], [-1.25, 34.275979, 1.25], [-2.5, 34.441359, 2.573039], [-2.5, 34.379341, 2.0769], [-4.166665, 34.379341, 2.0769], [-4.166665, 34.586066, 3.730695]]}]},
			"L_shoulder_shaper_01_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_01_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[20.9, 93.850166, -0.25], [20.973744, 93.86539, -0.270484], [21.036261, 93.908746, -0.28785], [21.078035, 93.97363, -0.299454], [21.092704, 94.050166, -0.303529], [21.078035, 94.126702, -0.299454], [21.036261, 94.191586, -0.28785], [20.973744, 94.234942, -0.270484], [20.9, 94.250166, -0.25], [20.826256, 94.234942, -0.229516], [20.763739, 94.191586, -0.21215], [20.721965, 94.126702, -0.200546], [20.707296, 94.050166, -0.196471], [20.721965, 93.97363, -0.200546], [20.763739, 93.908746, -0.21215], [20.826256, 93.86539, -0.229516], [20.9, 93.850166, -0.25], [20.9, 91.850166, -0.25]]}]},
			"L_upLeg_shaper_05_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_05_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[13.75, 27.609312, 2.083333], [13.816605, 27.210601, 2.133172], [14.006287, 26.872591, 2.175424], [14.290155, 26.646729, 2.203656], [14.625, 26.567421, 2.21357], [14.959845, 26.646729, 2.203656], [15.243712, 26.872591, 2.175424], [15.433395, 27.210601, 2.133172], [15.5, 27.609312, 2.083333], [15.433395, 28.008023, 2.033494], [15.243712, 28.346034, 1.991243], [14.959845, 28.571895, 1.96301], [14.625, 28.651204, 1.953097], [14.290155, 28.571895, 1.96301], [14.006287, 28.346034, 1.991243], [13.816605, 28.008023, 2.033494], [13.75, 27.609312, 2.083333], [5.0, 27.609312, 2.083333]]}]},
			"R_shoulder_shaper_01_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_01_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-20.9, 94.100166, -0.25], [-20.982962, 94.117293, -0.273045], [-21.053293, 94.166069, -0.292581], [-21.100289, 94.239063, -0.305636], [-21.116792, 94.325166, -0.31022], [-21.100289, 94.411269, -0.305636], [-21.053293, 94.484264, -0.292581], [-20.982962, 94.533039, -0.273045], [-20.9, 94.550166, -0.25], [-20.817038, 94.533039, -0.226955], [-20.746707, 94.484264, -0.207419], [-20.699711, 94.411269, -0.194364], [-20.683208, 94.325166, -0.18978], [-20.699711, 94.239063, -0.194364], [-20.746707, 94.166069, -0.207419], [-20.817038, 94.117293, -0.226955], [-20.9, 94.100166, -0.25], [-20.9, 91.850166, -0.25]]}]},
			"R_arm_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-35.0, 101.850166, 0.299858], [-35.0, 101.850166, -0.299858], [-35.0, 101.850166, -0.0], [-34.700142, 101.850166, -0.0], [-35.299858, 101.850166, 0.0], [-35.0, 101.850166, -0.0], [-35.0, 102.150024, -0.0], [-35.0, 101.550309, -0.0]]}]},
			"R_arm_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-35.0, 101.850166, 0.449787], [-35.0, 101.850166, -0.449787], [-35.0, 101.850166, -0.0], [-34.550213, 101.850166, -0.0], [-35.449787, 101.850166, -0.0], [-35.0, 101.850166, -0.0], [-35.0, 102.299953, -0.0], [-35.0, 101.40038, 0.0]]}]},
			"L_lwrArmRibbonMid_CTL": {"color": 17, "shapes": [{"shapeName": "L_lwrArmRibbonMid_CTLShape", "degree": 1, "form": 0, "points": [[47.910832, 93.516836, -7.296828], [47.910832, 94.516836, -7.296828], [48.616247, 91.850166, -9.695241], [47.910832, 89.183496, -7.296828], [47.910832, 90.183496, -7.296828], [46.970278, 90.183496, -4.098946], [46.970278, 86.850166, -4.098946], [47.252444, 86.850166, -5.058311], [46.5, 84.350166, -2.5], [45.747556, 86.850166, 0.058311], [46.029722, 86.850166, -0.901054], [46.029722, 90.183496, -0.901054], [45.089168, 90.183496, 2.296828], [45.089168, 89.183496, 2.296828], [44.383753, 91.850166, 4.695241], [45.089168, 94.516836, 2.296828], [45.089168, 93.516836, 2.296828], [46.029722, 93.516836, -0.901054], [46.029722, 96.850166, -0.901054], [45.747556, 96.850166, 0.058311], [46.5, 99.350166, -2.5], [47.252444, 96.850166, -5.058311], [46.970278, 96.850166, -4.098946], [46.970278, 93.516836, -4.098946], [47.910832, 93.516836, -7.296828]]}]},
			"R_elbow_shaper_02_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_elbow_shaper_02_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-43.235136, 91.850166, -3.471565], [-43.232075, 91.861017, -3.461155], [-43.229013, 91.850166, -3.450744], [-43.232075, 91.839315, -3.461155], [-43.235136, 91.850166, -3.471565], [-43.242484, 91.850166, -3.458093], [-43.229013, 91.850166, -3.450744], [-43.221665, 91.850166, -3.464216], [-43.232075, 91.861017, -3.461155], [-43.242484, 91.850166, -3.458093], [-43.232075, 91.839315, -3.461155], [-43.221665, 91.850166, -3.464216], [-43.235136, 91.850166, -3.471565], [-43.242484, 91.850166, -3.458093], [-42.25, 91.850166, -3.75]]}, {"shapeName": "R_elbow_shaper_02_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-42.253062, 92.873837, -3.76041], [-42.23959, 92.873837, -3.753062], [-42.246938, 92.873837, -3.73959], [-42.26041, 92.873837, -3.746938], [-42.253062, 92.873837, -3.76041], [-42.25, 92.884687, -3.75], [-42.246938, 92.873837, -3.73959], [-42.25, 92.862986, -3.75], [-42.23959, 92.873837, -3.753062], [-42.25, 92.884687, -3.75], [-42.26041, 92.873837, -3.746938], [-42.25, 92.862986, -3.75], [-42.253062, 92.873837, -3.76041], [-42.25, 92.884687, -3.75], [-42.25, 91.850166, -3.75]]}, {"shapeName": "R_elbow_shaper_02_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-41.961155, 91.861017, -2.767925], [-41.950744, 91.850166, -2.770987], [-41.961155, 91.839315, -2.767925], [-41.971565, 91.850166, -2.764864], [-41.961155, 91.861017, -2.767925], [-41.958093, 91.850166, -2.757516], [-41.961155, 91.839315, -2.767925], [-41.964216, 91.850166, -2.778335], [-41.950744, 91.850166, -2.770987], [-41.958093, 91.850166, -2.757516], [-41.971565, 91.850166, -2.764864], [-41.964216, 91.850166, -2.778335], [-41.961155, 91.861017, -2.767925], [-41.958093, 91.850166, -2.757516], [-42.25, 91.850166, -3.75]]}]},
			"L_elbow_shaper_02_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_02_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[42.25, 94.100166, -3.75], [42.332604, 94.117293, -3.725705], [42.402633, 94.166069, -3.705108], [42.449426, 94.239063, -3.691345], [42.465857, 94.325166, -3.686513], [42.449426, 94.411269, -3.691345], [42.402633, 94.484264, -3.705108], [42.332604, 94.533039, -3.725705], [42.25, 94.550166, -3.75], [42.167396, 94.533039, -3.774295], [42.097367, 94.484264, -3.794892], [42.050574, 94.411269, -3.808655], [42.034143, 94.325166, -3.813487], [42.050574, 94.239063, -3.808655], [42.097367, 94.166069, -3.794892], [42.167396, 94.117293, -3.774295], [42.25, 94.100166, -3.75], [42.25, 91.850166, -3.75]]}]},
			"world_CTL": {"color": 1, "shapes": [{"shapeName": "world_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -144.425], [64.1625, 0.0, -80.2], [48.1, 0.0, -80.2], [48.1, 0.0, -48.0875], [80.2125, 0.0, -48.0875], [80.2125, 0.0, -64.15], [144.425, 0.0, 0.0], [80.2, 0.0, 64.1625], [80.2, 0.0, 48.1], [48.0875, 0.0, 48.1], [48.0875, 0.0, 80.2125], [64.15, 0.0, 80.2125], [0.0, 0.0, 144.425], [-64.1625, 0.0, 80.2], [-48.1, 0.0, 80.2], [-48.1, 0.0, 48.0875], [-80.2125, 0.0, 48.0875], [-80.2125, 0.0, 64.15], [-144.425, 0.0, 0.0], [-80.2, 0.0, -64.1625], [-80.2, 0.0, -48.1], [-48.0875, 0.0, -48.1], [-48.0875, 0.0, -80.2125], [-64.15, 0.0, -80.2125], [0.0, 0.0, -144.425], [12.575, 0.175, -132.075], [11.475, 0.0, -130.9], [11.475, 0.0, -126.1], [10.475, 0.0, -126.1], [10.5375, 0.0, -130.9375], [9.825, 0.0, -130.575], [9.85, 0.0, -128.475], [8.8375, 0.0, -128.475], [8.8375, 0.0, -130.575], [8.2125, 0.0, -130.9375], [8.2125, 0.0, -126.025], [7.2, 0.0, -126.025], [7.2, 0.0, -131.0625], [8.0125, 0.0, -131.875], [9.2625, 0.0, -131.25], [10.6375, 0.0, -131.875], [11.475, 0.0, -130.925], [10.6375, 0.0, -131.875], [9.275, 0.0, -131.2625], [8.0125, 0.0, -131.8625], [5.575, 0.0, -131.875], [6.4, 0.0, -131.0625], [6.4, 0.0, -126.85], [5.575, 0.0, -126.025], [2.9375, 0.0, -126.025], [2.125, 0.0, -126.85], [2.125, 0.0, -131.0625], [2.9375, 0.0, -131.875], [5.575, 0.0, -131.875], [5.2625, 0.0, -130.9375], [5.3875, 0.0, -127.0625], [3.125, 0.0, -127.0875], [3.1375, 0.0, -130.9375], [5.275, 0.0, -130.9625], [5.575, 0.0, -131.875], [2.9375, 0.0, -131.875], [1.25, 0.0, -131.875], [1.3125, 0.0, -126.025], [-1.5375, 0.0, -126.025], [-2.3625, 0.0, -126.85], [-2.3625, 0.0, -128.6125], [-1.525, 0.0, -129.425], [-1.475, 0.0, -129.4875], [-3.1125, 0.0, -131.85], [-3.1125, 0.0, -131.875], [-1.9375, 0.0, -131.875], [-0.3, 0.0, -129.5], [0.3125, 0.0, -129.5], [0.3125, 0.0, -127.0], [-1.2625, 0.0, -127.0], [-1.275, 0.0, -128.4875], [0.3125, 0.0, -128.4875], [0.3125, 0.0, -131.875], [1.25, 0.0, -131.875], [-8.0375, 0.0, -131.875], [-8.0375, 0.0, -130.9375], [-4.7625, 0.0, -130.925], [-4.7625, 0.0, -126.025], [-3.75, 0.0, -126.025], [-3.75, 0.0, -131.875], [-12.3, 0.0, -131.875], [-13.05, 0.0, -131.0625], [-13.1125, 0.0, -126.85], [-12.3, 0.0, -126.025], [-8.8375, 0.0, -126.025], [-8.8375, 0.0, -131.875], [-9.8625, 0.0, -130.9375], [-9.8375, 0.0, -126.975], [-11.975, 0.0, -126.975], [-11.95, 0.0, -130.9125], [-9.825, 0.0, -130.9625], [-8.8125, 0.0, -131.875]]}]},
			"R_shoulder_shaper_04_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_04_CTLShape", "degree": 1, "form": 0, "points": [[-33.5, 94.350166, -3.75], [-33.59218, 94.369196, -3.775605], [-33.670326, 94.423391, -3.797313], [-33.722544, 94.504496, -3.811818], [-33.740879, 94.600166, -3.816911], [-33.722544, 94.695836, -3.811818], [-33.670326, 94.776941, -3.797313], [-33.59218, 94.831136, -3.775605], [-33.5, 94.850166, -3.75], [-33.40782, 94.831136, -3.724395], [-33.329674, 94.776941, -3.702687], [-33.277456, 94.695836, -3.688182], [-33.259121, 94.600166, -3.683089], [-33.277456, 94.504496, -3.688182], [-33.329674, 94.423391, -3.702687], [-33.40782, 94.369196, -3.724395], [-33.5, 94.350166, -3.75], [-33.5, 91.850166, -3.75]]}]},
			"R_loLeg_shaper_02_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_02_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-13.75, 17.109312, 1.666667], [-13.816605, 16.710188, 1.620257], [-14.006287, 16.371826, 1.580912], [-14.290155, 16.145731, 1.554622], [-14.625, 16.06634, 1.545391], [-14.959845, 16.145731, 1.554622], [-15.243712, 16.371826, 1.580912], [-15.433395, 16.710188, 1.620257], [-15.5, 17.109312, 1.666667], [-15.433395, 17.508437, 1.713077], [-15.243712, 17.846798, 1.752421], [-14.959845, 18.072894, 1.778711], [-14.625, 18.152285, 1.787943], [-14.290155, 18.072894, 1.778711], [-14.006287, 17.846798, 1.752421], [-13.816605, 17.508437, 1.713077], [-13.75, 17.109312, 1.666667], [-5.0, 17.109312, 1.666667]]}]},
			"C_cog_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-12.0, 49.350166, -12.0], [-12.0, 49.350166, 12.0], [12.0, 49.350166, 12.0], [12.0, 49.350166, -12.0], [-12.0, 49.350166, -12.0]]}]},
			"L_leg_PV_CTL": {"color": 6, "shapes": [{"shapeName": "L_leg_PV_CTLShape", "degree": 1, "form": 0, "points": [[4.5, 24.775979, 53.0], [4.5, 23.775979, 53.0], [4.5, 23.775979, 52.0], [4.5, 24.775979, 52.0], [5.5, 24.775979, 52.0], [5.5, 23.775979, 52.0], [5.5, 23.775979, 53.0], [5.5, 24.775979, 53.0], [4.5, 24.775979, 53.0], [4.5, 24.775979, 52.0], [4.5, 23.775979, 52.0], [5.5, 23.775979, 52.0], [5.5, 24.775979, 52.0], [5.5, 24.775979, 53.0], [5.5, 23.775979, 53.0], [4.5, 23.775979, 53.0]]}]},
			"R_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.323456, 92.526661, -2.554255], [-66.316286, 92.58044, -2.5], [-66.323456, 92.526661, -2.445745], [-66.330627, 92.472882, -2.5], [-66.323456, 92.526661, -2.554255], [-66.37723, 92.533831, -2.5], [-66.323456, 92.526661, -2.445745], [-66.269677, 92.519491, -2.5], [-66.316286, 92.58044, -2.5], [-66.37723, 92.533831, -2.5], [-66.330627, 92.472882, -2.5], [-66.269677, 92.519491, -2.5], [-66.323456, 92.526661, -2.554255], [-66.37723, 92.533831, -2.5], [-61.25, 91.8502, -2.5]]}, {"shapeName": "R_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-60.573539, 96.923657, -2.554255], [-60.51976, 96.916486, -2.5], [-60.573539, 96.923657, -2.445745], [-60.627318, 96.930827, -2.5], [-60.573539, 96.923657, -2.554255], [-60.566369, 96.977431, -2.5], [-60.573539, 96.923657, -2.445745], [-60.58071, 96.869878, -2.5], [-60.51976, 96.916486, -2.5], [-60.566369, 96.977431, -2.5], [-60.627318, 96.930827, -2.5], [-60.58071, 96.869878, -2.5], [-60.573539, 96.923657, -2.554255], [-60.566369, 96.977431, -2.5], [-61.25, 91.8502, -2.5]]}, {"shapeName": "R_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.242829, 91.903979, 2.618355], [-61.196221, 91.84303, 2.618355], [-61.257171, 91.796421, 2.618355], [-61.303779, 91.857371, 2.618355], [-61.242829, 91.903979, 2.618355], [-61.25, 91.8502, 2.672605], [-61.257171, 91.796421, 2.618355], [-61.25, 91.8502, 2.5641], [-61.196221, 91.84303, 2.618355], [-61.25, 91.8502, 2.672605], [-61.303779, 91.857371, 2.618355], [-61.25, 91.8502, 2.5641], [-61.242829, 91.903979, 2.618355], [-61.25, 91.8502, 2.672605], [-61.25, 91.8502, -2.5]]}]},
			"R_shoulder_shaper_03_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_03_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-29.0, 94.100166, -2.5], [-29.082962, 94.117293, -2.523045], [-29.153293, 94.166069, -2.542581], [-29.200289, 94.239063, -2.555636], [-29.216792, 94.325166, -2.56022], [-29.200289, 94.411269, -2.555636], [-29.153293, 94.484264, -2.542581], [-29.082962, 94.533039, -2.523045], [-29.0, 94.550166, -2.5], [-28.917038, 94.533039, -2.476955], [-28.846707, 94.484264, -2.457419], [-28.799711, 94.411269, -2.444364], [-28.783208, 94.325166, -2.43978], [-28.799711, 94.239063, -2.444364], [-28.846707, 94.166069, -2.457419], [-28.917038, 94.117293, -2.476955], [-29.0, 94.100166, -2.5], [-29.0, 91.850166, -2.5]]}]},
			"C_hip_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[4.936756, 51.850166, -4.113963], [0.0, 49.750166, -5.818018], [-4.936756, 51.850166, -4.113963], [-6.981622, 53.950166, 0.0], [-4.936756, 51.850166, 4.113963], [0.0, 49.750166, 5.818018], [4.936756, 51.850166, 4.113963], [6.981622, 53.950166, 0.0]]}]},
			"L_upLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 39.203878, 0.68869], [4.945745, 39.197149, 0.634854], [5.0, 39.190419, 0.581018], [5.054255, 39.197149, 0.634854], [5.0, 39.203878, 0.68869], [5.0, 39.143317, 0.641583], [5.0, 39.190419, 0.581018], [5.0, 39.250985, 0.628124], [4.945745, 39.197149, 0.634854], [5.0, 39.143317, 0.641583], [5.054255, 39.197149, 0.634854], [5.0, 39.250985, 0.628124], [5.0, 39.203878, 0.68869], [5.0, 39.143317, 0.641583], [5.0, 44.275979, 0.0]]}, {"shapeName": "L_upLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 44.282708, 0.053836], [-0.118355, 44.329815, -0.00673], [-0.118355, 44.269249, -0.053836], [-0.118355, 44.222143, 0.00673], [-0.118355, 44.282708, 0.053836], [-0.172605, 44.275979, 0.0], [-0.118355, 44.269249, -0.053836], [-0.0641, 44.275979, 0.0], [-0.118355, 44.329815, -0.00673], [-0.172605, 44.275979, 0.0], [-0.118355, 44.222143, 0.00673], [-0.0641, 44.275979, 0.0], [-0.118355, 44.282708, 0.053836], [-0.172605, 44.275979, 0.0], [5.0, 44.275979, 0.0]]}, {"shapeName": "L_upLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 43.641125, -5.07883], [5.0, 43.694961, -5.08556], [5.054255, 43.641125, -5.07883], [5.0, 43.587289, -5.072101], [4.945745, 43.641125, -5.07883], [5.0, 43.634396, -5.132662], [5.054255, 43.641125, -5.07883], [5.0, 43.647855, -5.024994], [5.0, 43.694961, -5.08556], [5.0, 43.634396, -5.132662], [5.0, 43.587289, -5.072101], [5.0, 43.647855, -5.024994], [4.945745, 43.641125, -5.07883], [5.0, 43.634396, -5.132662], [5.0, 44.275979, 0.0]]}]},
			"L_elbow_shaper_04_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_04_CTLShape", "degree": 1, "form": 0, "points": [[50.75, 94.350166, -1.25], [50.841782, 94.369196, -1.223005], [50.919592, 94.423391, -1.20012], [50.971585, 94.504496, -1.184828], [50.989841, 94.600166, -1.179458], [50.971585, 94.695836, -1.184828], [50.919592, 94.776941, -1.20012], [50.841782, 94.831136, -1.223005], [50.75, 94.850166, -1.25], [50.658218, 94.831136, -1.276995], [50.580408, 94.776941, -1.29988], [50.528415, 94.695836, -1.315172], [50.510159, 94.600166, -1.320542], [50.528415, 94.504496, -1.315172], [50.580408, 94.423391, -1.29988], [50.658218, 94.369196, -1.276995], [50.75, 94.350166, -1.25], [50.75, 91.850166, -1.25]]}]},
			"R_shoulder_shaper_03_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_03_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-29.0, 93.350166, -2.5], [-29.055308, 93.361584, -2.515363], [-29.102196, 93.394101, -2.528388], [-29.133526, 93.442764, -2.537091], [-29.144528, 93.500166, -2.540147], [-29.133526, 93.557568, -2.537091], [-29.102196, 93.606231, -2.528388], [-29.055308, 93.638748, -2.515363], [-29.0, 93.650166, -2.5], [-28.944692, 93.638748, -2.484637], [-28.897804, 93.606231, -2.471612], [-28.866474, 93.557568, -2.462909], [-28.855472, 93.500166, -2.459853], [-28.866474, 93.442764, -2.462909], [-28.897804, 93.394101, -2.471612], [-28.944692, 93.361584, -2.484637], [-29.0, 93.350166, -2.5], [-29.0, 91.850166, -2.5]]}]},
			"L_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.323456, 92.526627, 1.195745], [66.316286, 92.580406, 1.25], [66.323456, 92.526627, 1.304255], [66.330627, 92.472848, 1.25], [66.323456, 92.526627, 1.195745], [66.37723, 92.533797, 1.25], [66.323456, 92.526627, 1.304255], [66.269677, 92.519457, 1.25], [66.316286, 92.580406, 1.25], [66.37723, 92.533797, 1.25], [66.330627, 92.472848, 1.25], [66.269677, 92.519457, 1.25], [66.323456, 92.526627, 1.195745], [66.37723, 92.533797, 1.25], [61.25, 91.850166, 1.25]]}, {"shapeName": "L_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[60.573539, 96.923623, 1.195745], [60.51976, 96.916452, 1.25], [60.573539, 96.923623, 1.304255], [60.627318, 96.930793, 1.25], [60.573539, 96.923623, 1.195745], [60.566369, 96.977397, 1.25], [60.573539, 96.923623, 1.304255], [60.58071, 96.869844, 1.25], [60.51976, 96.916452, 1.25], [60.566369, 96.977397, 1.25], [60.627318, 96.930793, 1.25], [60.58071, 96.869844, 1.25], [60.573539, 96.923623, 1.195745], [60.566369, 96.977397, 1.25], [61.25, 91.850166, 1.25]]}, {"shapeName": "L_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.242829, 91.903945, 6.368355], [61.196221, 91.842996, 6.368355], [61.257171, 91.796387, 6.368355], [61.303779, 91.857337, 6.368355], [61.242829, 91.903945, 6.368355], [61.25, 91.850166, 6.422605], [61.257171, 91.796387, 6.368355], [61.25, 91.850166, 6.3141], [61.196221, 91.842996, 6.368355], [61.25, 91.850166, 6.422605], [61.303779, 91.857337, 6.368355], [61.25, 91.850166, 6.3141], [61.242829, 91.903945, 6.368355], [61.25, 91.850166, 6.422605], [61.25, 91.850166, 1.25]]}]},
			"R_upLeg_shaper_04_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_04_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-13.75, 30.942646, 1.666667], [-13.816605, 30.543934, 1.716506], [-14.006287, 30.205924, 1.758757], [-14.290155, 29.980063, 1.78699], [-14.625, 29.900754, 1.796903], [-14.959845, 29.980063, 1.78699], [-15.243712, 30.205924, 1.758757], [-15.433395, 30.543934, 1.716506], [-15.5, 30.942646, 1.666667], [-15.433395, 31.341357, 1.616828], [-15.243712, 31.679367, 1.574576], [-14.959845, 31.905229, 1.546344], [-14.625, 31.984537, 1.53643], [-14.290155, 31.905229, 1.546344], [-14.006287, 31.679367, 1.574576], [-13.816605, 31.341357, 1.616828], [-13.75, 30.942646, 1.666667], [-5.0, 30.942646, 1.666667]]}]},
			"R_loLeg_shaper_03_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_03_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-15.0, 13.525979, 1.25], [-15.07612, 13.069836, 1.19696], [-15.2929, 12.683138, 1.151995], [-15.61732, 12.424743, 1.121949], [-16.0, 12.33401, 1.111399], [-16.38268, 12.424743, 1.121949], [-16.7071, 12.683138, 1.151995], [-16.92388, 13.069836, 1.19696], [-17.0, 13.525979, 1.25], [-16.92388, 13.982122, 1.30304], [-16.7071, 14.36882, 1.348005], [-16.38268, 14.627215, 1.378051], [-16.0, 14.717948, 1.388601], [-15.61732, 14.627215, 1.378051], [-15.2929, 14.36882, 1.348005], [-15.07612, 13.982122, 1.30304], [-15.0, 13.525979, 1.25], [-5.0, 13.525979, 1.25]]}]},
			"C_midNeck_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.347257, 96.850166, -5.289381], [0.0, 96.850166, -7.480309], [-6.347257, 96.850166, -5.289381], [-8.976371, 96.850166, 0.0], [-6.347257, 96.850166, 5.289381], [0.0, 96.850166, 7.480309], [6.347257, 96.850166, 5.289381], [8.976371, 96.850166, 0.0]]}]},
			"R_loLeg_FK_CTL": {"color": 13, "shapes": [{"shapeName": "R_loLeg_FK_CTLShape", "degree": 1, "form": 0, "points": [[-2.5, 22.081463, -0.272021], [-2.5, 27.048, 0.305484], [-2.5, 26.470495, 5.272021], [-2.5, 21.503958, 4.694516], [-7.5, 21.503958, 4.694516], [-7.5, 26.470495, 5.272021], [-7.5, 27.048, 0.305484], [-7.5, 22.081463, -0.272021], [-2.5, 22.081463, -0.272021], [-2.5, 21.503958, 4.694516], [-2.5, 26.470495, 5.272021], [-7.5, 26.470495, 5.272021], [-7.5, 21.503958, 4.694516], [-7.5, 22.081463, -0.272021], [-7.5, 27.048, 0.305484], [-2.5, 27.048, 0.305484]]}]},
			"L_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_C_CTLShape", "degree": 1, "form": 0, "points": [[65.80742, 92.937969, -1.75], [64.312197, 93.057587, -1.75], [64.312197, 93.057587, -3.25], [65.80742, 92.937969, -3.25], [65.687803, 91.442746, -3.25], [64.19258, 91.562364, -3.25], [64.19258, 91.562364, -1.75], [65.687803, 91.442746, -1.75], [65.80742, 92.937969, -1.75], [65.80742, 92.937969, -3.25], [64.312197, 93.057587, -3.25], [64.19258, 91.562364, -3.25], [65.687803, 91.442746, -3.25], [65.687803, 91.442746, -1.75], [64.19258, 91.562364, -1.75], [64.312197, 93.057587, -1.75]]}]},
			"L_leg_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[8.518451, 3.301852, 0.061148], [8.375193, 3.301852, 0.061148], [8.348063, 3.155834, 0.044169], [8.246264, 3.113938, 0.039298], [8.123126, 3.198133, 0.049088], [8.021826, 3.097511, 0.037387], [8.106584, 2.975211, 0.023166], [8.064424, 2.87408, 0.011407], [7.917409, 2.847131, 0.008273], [7.917409, 2.704827, -0.008273], [8.064424, 2.677879, -0.011407], [8.106584, 2.576761, -0.023165], [8.021826, 2.454447, -0.037387], [8.123126, 2.353825, -0.049088], [8.246264, 2.43802, -0.039298], [8.348063, 2.396124, -0.044169], [8.375193, 2.250106, -0.061148], [8.518451, 2.250106, -0.061148], [8.545595, 2.396124, -0.044169], [8.647394, 2.43802, -0.039298], [8.770532, 2.353825, -0.049088], [8.871823, 2.454447, -0.037387], [8.787074, 2.576761, -0.023165], [8.829235, 2.677879, -0.011407], [8.976236, 2.704827, -0.008273], [8.976236, 2.847131, 0.008273], [8.829235, 2.87408, 0.011407], [8.787074, 2.975211, 0.023166], [8.871823, 3.097511, 0.037387], [8.770532, 3.198133, 0.049088], [8.647394, 3.113938, 0.039298], [8.545595, 3.155834, 0.044169], [8.518451, 3.301852, 0.061148]]}, {"shapeName": "L_leg_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[8.602322, 2.93044, 0.017961], [8.666735, 2.775979, 0.0], [8.602322, 2.621518, -0.017961], [8.446824, 2.557549, -0.025399], [8.291336, 2.621518, -0.017961], [8.226923, 2.775979, 0.0], [8.291336, 2.93044, 0.017961], [8.446824, 2.994409, 0.025399]]}, {"shapeName": "L_leg_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[7.917409, 2.775979, 0.0], [5.0, 2.775979, 0.0]]}]},
			"L_uprArmRibbonMid_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_uprArmRibbonMid_PIV_CTLShape", "degree": 1, "form": 0, "points": [[29.983421, 91.850166, -2.784434], [29.986325, 91.861017, -2.773979], [29.98923, 91.850166, -2.763524], [29.986325, 91.839315, -2.773979], [29.983421, 91.850166, -2.784434], [29.99678, 91.850166, -2.776883], [29.98923, 91.850166, -2.763524], [29.97587, 91.850166, -2.771075], [29.986325, 91.861017, -2.773979], [29.99678, 91.850166, -2.776883], [29.986325, 91.839315, -2.773979], [29.97587, 91.850166, -2.771075], [29.983421, 91.850166, -2.784434], [29.99678, 91.850166, -2.776883], [29.0, 91.850166, -2.5]]}, {"shapeName": "L_uprArmRibbonMid_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[28.997096, 92.873837, -2.510455], [28.989545, 92.873837, -2.497096], [29.002904, 92.873837, -2.489545], [29.010455, 92.873837, -2.502904], [28.997096, 92.873837, -2.510455], [29.0, 92.884687, -2.5], [29.002904, 92.873837, -2.489545], [29.0, 92.862986, -2.5], [28.989545, 92.873837, -2.497096], [29.0, 92.884687, -2.5], [29.010455, 92.873837, -2.502904], [29.0, 92.862986, -2.5], [28.997096, 92.873837, -2.510455], [29.0, 92.884687, -2.5], [29.0, 91.850166, -2.5]]}, {"shapeName": "L_uprArmRibbonMid_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[29.273979, 91.861017, -1.513675], [29.263524, 91.850166, -1.51077], [29.273979, 91.839315, -1.513675], [29.284434, 91.850166, -1.516579], [29.273979, 91.861017, -1.513675], [29.276883, 91.850166, -1.50322], [29.273979, 91.839315, -1.513675], [29.271075, 91.850166, -1.52413], [29.263524, 91.850166, -1.51077], [29.276883, 91.850166, -1.50322], [29.284434, 91.850166, -1.516579], [29.271075, 91.850166, -1.52413], [29.273979, 91.861017, -1.513675], [29.276883, 91.850166, -1.50322], [29.0, 91.850166, -2.5]]}]},
			"L_upLeg_shaper_04_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_04_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[12.5, 30.942646, 1.666667], [12.55709, 30.600893, 1.709386], [12.719675, 30.31117, 1.745601], [12.96299, 30.117575, 1.769801], [13.25, 30.049596, 1.778298], [13.53701, 30.117575, 1.769801], [13.780325, 30.31117, 1.745601], [13.94291, 30.600893, 1.709386], [14.0, 30.942646, 1.666667], [13.94291, 31.284398, 1.623948], [13.780325, 31.574121, 1.587732], [13.53701, 31.767717, 1.563533], [13.25, 31.835696, 1.555035], [12.96299, 31.767717, 1.563533], [12.719675, 31.574121, 1.587732], [12.55709, 31.284398, 1.623948], [12.5, 30.942646, 1.666667], [5.0, 30.942646, 1.666667]]}]},
			"L_leg_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 19.157624, 52.554255], [4.945745, 19.157624, 52.5], [5.0, 19.157624, 52.445745], [5.054255, 19.157624, 52.5], [5.0, 19.157624, 52.554255], [5.0, 19.103374, 52.5], [5.0, 19.157624, 52.445745], [5.0, 19.211879, 52.5], [4.945745, 19.157624, 52.5], [5.0, 19.103374, 52.5], [5.054255, 19.157624, 52.5], [5.0, 19.211879, 52.5], [5.0, 19.157624, 52.554255], [5.0, 19.103374, 52.5], [5.0, 24.275979, 52.5]]}, {"shapeName": "L_leg_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 24.275979, 52.554255], [-0.118355, 24.330234, 52.5], [-0.118355, 24.275979, 52.445745], [-0.118355, 24.221724, 52.5], [-0.118355, 24.275979, 52.554255], [-0.172605, 24.275979, 52.5], [-0.118355, 24.275979, 52.445745], [-0.0641, 24.275979, 52.5], [-0.118355, 24.330234, 52.5], [-0.172605, 24.275979, 52.5], [-0.118355, 24.221724, 52.5], [-0.0641, 24.275979, 52.5], [-0.118355, 24.275979, 52.554255], [-0.172605, 24.275979, 52.5], [5.0, 24.275979, 52.5]]}, {"shapeName": "L_leg_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 24.275979, 47.381645], [5.0, 24.330234, 47.381645], [5.054255, 24.275979, 47.381645], [5.0, 24.221724, 47.381645], [4.945745, 24.275979, 47.381645], [5.0, 24.275979, 47.327395], [5.054255, 24.275979, 47.381645], [5.0, 24.275979, 47.4359], [5.0, 24.330234, 47.381645], [5.0, 24.275979, 47.327395], [5.0, 24.221724, 47.381645], [5.0, 24.275979, 47.4359], [4.945745, 24.275979, 47.381645], [5.0, 24.275979, 47.327395], [5.0, 24.275979, 52.5]]}]},
			"L_bendyLeg_C_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.249999, 13.266102, 3.484942], [3.799999, 13.266102, 3.484942], [5.0, 13.136164, 4.602412], [6.200001, 13.266102, 3.484942], [5.750001, 13.266102, 3.484942], [5.750001, 13.439353, 1.994982], [7.25, 13.439353, 1.994982], [7.25, 13.387378, 2.44197], [8.375, 13.525979, 1.25], [7.25, 13.66458, 0.05803], [7.25, 13.612605, 0.505018], [5.750001, 13.612605, 0.505018], [5.750001, 13.785856, -0.984942], [6.200001, 13.785856, -0.984942], [5.0, 13.915794, -2.102412], [3.799999, 13.785856, -0.984942], [4.249999, 13.785856, -0.984942], [4.249999, 13.612605, 0.505018], [2.75, 13.612605, 0.505018], [2.75, 13.66458, 0.05803], [1.625, 13.525979, 1.25], [2.75, 13.387378, 2.44197], [2.75, 13.439353, 1.994982], [4.249999, 13.439353, 1.994982], [4.249999, 13.266102, 3.484942]]}]},
			"R_lwrArmRibbonMid_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lwrArmRibbonMid_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-47.487582, 93.016835, -5.857779], [-47.487582, 93.716835, -5.857779], [-47.981373, 91.850166, -7.536669], [-47.487582, 89.983497, -5.857779], [-47.487582, 90.683497, -5.857779], [-46.829195, 90.683497, -3.619262], [-46.829195, 88.350166, -3.619262], [-47.026711, 88.350166, -4.290818], [-46.5, 86.600166, -2.5], [-45.973289, 88.350166, -0.709182], [-46.170805, 88.350166, -1.380738], [-46.170805, 90.683497, -1.380738], [-45.512418, 90.683497, 0.857779], [-45.512418, 89.983497, 0.857779], [-45.018627, 91.850166, 2.536669], [-45.512418, 93.716835, 0.857779], [-45.512418, 93.016835, 0.857779], [-46.170805, 93.016835, -1.380738], [-46.170805, 95.350166, -1.380738], [-45.973289, 95.350166, -0.709182], [-46.5, 97.100166, -2.5], [-47.026711, 95.350166, -4.290818], [-46.829195, 95.350166, -3.619262], [-46.829195, 93.016835, -3.619262], [-47.487582, 93.016835, -5.857779]]}]},
			"L_toe_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.763127, 2.039106, 5.0], [5.0, 2.769416, 5.0], [3.236873, 2.039106, 5.0], [2.506564, 0.275979, 5.0], [3.236873, -1.487148, 5.0], [5.0, -2.217457, 5.0], [6.763127, -1.487148, 5.0], [7.493436, 0.275979, 5.0]]}]},
			"R_leg_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-8.127512, 3.243422, 0.054354], [-8.000172, 3.243422, 0.054354], [-7.976056, 3.113628, 0.039262], [-7.885568, 3.076387, 0.034931], [-7.776112, 3.151227, 0.043633], [-7.686068, 3.061785, 0.033233], [-7.761408, 2.953074, 0.020592], [-7.723932, 2.86318, 0.01014], [-7.593252, 2.839225, 0.007354], [-7.593252, 2.712733, -0.007354], [-7.723932, 2.688779, -0.01014], [-7.761408, 2.598896, -0.020591], [-7.686068, 2.490173, -0.033233], [-7.776112, 2.400731, -0.043633], [-7.885568, 2.475571, -0.034931], [-7.976056, 2.43833, -0.039262], [-8.000172, 2.308537, -0.054354], [-8.127512, 2.308537, -0.054354], [-8.15164, 2.43833, -0.039262], [-8.242128, 2.475571, -0.034931], [-8.351584, 2.400731, -0.043633], [-8.44162, 2.490173, -0.033233], [-8.366288, 2.598896, -0.020591], [-8.403764, 2.688779, -0.01014], [-8.534432, 2.712733, -0.007354], [-8.534432, 2.839225, 0.007354], [-8.403764, 2.86318, 0.01014], [-8.366288, 2.953074, 0.020592], [-8.44162, 3.061785, 0.033233], [-8.351584, 3.151227, 0.043633], [-8.242128, 3.076387, 0.034931], [-8.15164, 3.113628, 0.039262], [-8.127512, 3.243422, 0.054354]]}, {"shapeName": "R_leg_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-8.202064, 2.913278, 0.015965], [-8.25932, 2.775979, -0.0], [-8.202064, 2.63868, -0.015965], [-8.063844, 2.581819, -0.022577], [-7.925632, 2.63868, -0.015965], [-7.868376, 2.775979, -0.0], [-7.925632, 2.913278, 0.015965], [-8.063844, 2.970139, 0.022577]]}, {"shapeName": "R_leg_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-7.593252, 2.775979, 0.0], [-5.0, 2.775979, -0.0]]}]},
			"L_wristFk_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_wristFk_PIV_CTLShape", "degree": 1, "form": 0, "points": [[56.023671, 91.850166, -0.010851], [56.023671, 91.861017, 0.0], [56.023671, 91.850166, 0.010851], [56.023671, 91.839315, 0.0], [56.023671, 91.850166, -0.010851], [56.034521, 91.850166, 0.0], [56.023671, 91.850166, 0.010851], [56.01282, 91.850166, 0.0], [56.023671, 91.861017, 0.0], [56.034521, 91.850166, 0.0], [56.023671, 91.839315, 0.0], [56.01282, 91.850166, 0.0], [56.023671, 91.850166, -0.010851], [56.034521, 91.850166, 0.0], [55.0, 91.850166, 0.0]]}, {"shapeName": "L_wristFk_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[55.0, 92.873837, -0.010851], [54.989149, 92.873837, 0.0], [55.0, 92.873837, 0.010851], [55.010851, 92.873837, 0.0], [55.0, 92.873837, -0.010851], [55.0, 92.884687, 0.0], [55.0, 92.873837, 0.010851], [55.0, 92.862986, 0.0], [54.989149, 92.873837, 0.0], [55.0, 92.884687, 0.0], [55.010851, 92.873837, 0.0], [55.0, 92.862986, 0.0], [55.0, 92.873837, -0.010851], [55.0, 92.884687, 0.0], [55.0, 91.850166, 0.0]]}, {"shapeName": "L_wristFk_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[55.0, 91.861017, 1.023671], [54.989149, 91.850166, 1.023671], [55.0, 91.839315, 1.023671], [55.010851, 91.850166, 1.023671], [55.0, 91.861017, 1.023671], [55.0, 91.850166, 1.034521], [55.0, 91.839315, 1.023671], [55.0, 91.850166, 1.01282], [54.989149, 91.850166, 1.023671], [55.0, 91.850166, 1.034521], [55.010851, 91.850166, 1.023671], [55.0, 91.850166, 1.01282], [55.0, 91.861017, 1.023671], [55.0, 91.850166, 1.034521], [55.0, 91.850166, 0.0]]}]},
			"R_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_C_CTLShape", "degree": 1, "form": 0, "points": [[-65.80742, 92.937969, 0.75], [-64.312197, 93.057587, 0.75], [-64.312197, 93.057587, -0.75], [-65.80742, 92.937969, -0.75], [-65.687803, 91.442746, -0.75], [-64.19258, 91.562364, -0.75], [-64.19258, 91.562364, 0.75], [-65.687803, 91.442746, 0.75], [-65.80742, 92.937969, 0.75], [-65.80742, 92.937969, -0.75], [-64.312197, 93.057587, -0.75], [-64.19258, 91.562364, -0.75], [-65.687803, 91.442746, -0.75], [-65.687803, 91.442746, 0.75], [-64.19258, 91.562364, 0.75], [-64.312197, 93.057587, 0.75]]}]},
			"L_shoulder_shaper_03_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_03_CTLShape", "degree": 1, "form": 0, "points": [[29.0, 94.350166, -2.5], [29.09218, 94.369196, -2.525605], [29.170326, 94.423391, -2.547313], [29.222544, 94.504496, -2.561818], [29.240879, 94.600166, -2.566911], [29.222544, 94.695836, -2.561818], [29.170326, 94.776941, -2.547313], [29.09218, 94.831136, -2.525605], [29.0, 94.850166, -2.5], [28.90782, 94.831136, -2.474395], [28.829674, 94.776941, -2.452687], [28.777456, 94.695836, -2.438182], [28.759121, 94.600166, -2.433089], [28.777456, 94.504496, -2.438182], [28.829674, 94.423391, -2.452687], [28.90782, 94.369196, -2.474395], [29.0, 94.350166, -2.5], [29.0, 91.850166, -2.5]]}]},
			"L_bendyLeg_B_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.416665, 24.2835, 4.249984], [4.066666, 24.2835, 4.249984], [5.0, 24.287261, 5.124976], [5.933334, 24.2835, 4.249984], [5.583335, 24.2835, 4.249984], [5.583335, 24.278486, 3.083329], [6.75, 24.278486, 3.083329], [6.75, 24.27999, 3.433326], [7.625, 24.275979, 2.5], [6.75, 24.271968, 1.566674], [6.75, 24.273472, 1.916671], [5.583335, 24.273472, 1.916671], [5.583335, 24.268458, 0.750016], [5.933334, 24.268458, 0.750016], [5.0, 24.264697, -0.124976], [4.066666, 24.268458, 0.750016], [4.416665, 24.268458, 0.750016], [4.416665, 24.273472, 1.916671], [3.25, 24.273472, 1.916671], [3.25, 24.271968, 1.566674], [2.375, 24.275979, 2.5], [3.25, 24.27999, 3.433326], [3.25, 24.278486, 3.083329], [4.416665, 24.278486, 3.083329], [4.416665, 24.2835, 4.249984]]}]},
			"L_bendyLeg_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_bendyLeg_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 8.435613, 0.712717], [4.945745, 8.441879, 0.658826], [5.0, 8.448146, 0.604934], [5.054255, 8.441879, 0.658826], [5.0, 8.435613, 0.712717], [5.0, 8.387992, 0.65256], [5.0, 8.448146, 0.604934], [5.0, 8.495771, 0.665092], [4.945745, 8.441879, 0.658826], [5.0, 8.387992, 0.65256], [5.054255, 8.441879, 0.658826], [5.0, 8.495771, 0.665092], [5.0, 8.435613, 0.712717], [5.0, 8.387992, 0.65256], [5.0, 13.525979, 1.25]]}, {"shapeName": "L_bendyLeg_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 13.519713, 1.303892], [-0.118355, 13.579871, 1.256266], [-0.118355, 13.532246, 1.196108], [-0.118355, 13.472087, 1.243734], [-0.118355, 13.519713, 1.303892], [-0.172605, 13.525979, 1.25], [-0.118355, 13.532246, 1.196108], [-0.0641, 13.525979, 1.25], [-0.118355, 13.579871, 1.256266], [-0.172605, 13.525979, 1.25], [-0.118355, 13.472087, 1.243734], [-0.0641, 13.525979, 1.25], [-0.118355, 13.519713, 1.303892], [-0.172605, 13.525979, 1.25], [5.0, 13.525979, 1.25]]}, {"shapeName": "L_bendyLeg_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 14.117153, -3.8341], [5.0, 14.171045, -3.827833], [5.054255, 14.117153, -3.8341], [5.0, 14.063262, -3.840366], [4.945745, 14.117153, -3.8341], [5.0, 14.123419, -3.887987], [5.054255, 14.117153, -3.8341], [5.0, 14.110887, -3.780208], [5.0, 14.171045, -3.827833], [5.0, 14.123419, -3.887987], [5.0, 14.063262, -3.840366], [5.0, 14.110887, -3.780208], [4.945745, 14.117153, -3.8341], [5.0, 14.123419, -3.887987], [5.0, 13.525979, 1.25]]}]},
			"L_shoulderFk_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_shoulderFk_PIV_CTLShape", "degree": 1, "form": 0, "points": [[20.983421, 91.850166, -0.284434], [20.986325, 91.861017, -0.273979], [20.98923, 91.850166, -0.263524], [20.986325, 91.839315, -0.273979], [20.983421, 91.850166, -0.284434], [20.99678, 91.850166, -0.276883], [20.98923, 91.850166, -0.263524], [20.97587, 91.850166, -0.271075], [20.986325, 91.861017, -0.273979], [20.99678, 91.850166, -0.276883], [20.986325, 91.839315, -0.273979], [20.97587, 91.850166, -0.271075], [20.983421, 91.850166, -0.284434], [20.99678, 91.850166, -0.276883], [20.0, 91.850166, 0.0]]}, {"shapeName": "L_shoulderFk_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[19.997096, 92.873837, -0.010455], [19.989545, 92.873837, 0.002904], [20.002904, 92.873837, 0.010455], [20.010455, 92.873837, -0.002904], [19.997096, 92.873837, -0.010455], [20.0, 92.884687, 0.0], [20.002904, 92.873837, 0.010455], [20.0, 92.862986, 0.0], [19.989545, 92.873837, 0.002904], [20.0, 92.884687, 0.0], [20.010455, 92.873837, -0.002904], [20.0, 92.862986, 0.0], [19.997096, 92.873837, -0.010455], [20.0, 92.884687, 0.0], [20.0, 91.850166, 0.0]]}, {"shapeName": "L_shoulderFk_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[20.273979, 91.861017, 0.986325], [20.263524, 91.850166, 0.98923], [20.273979, 91.839315, 0.986325], [20.284434, 91.850166, 0.983421], [20.273979, 91.861017, 0.986325], [20.276883, 91.850166, 0.99678], [20.273979, 91.839315, 0.986325], [20.271075, 91.850166, 0.97587], [20.263524, 91.850166, 0.98923], [20.276883, 91.850166, 0.99678], [20.284434, 91.850166, 0.983421], [20.271075, 91.850166, 0.97587], [20.273979, 91.861017, 0.986325], [20.276883, 91.850166, 0.99678], [20.0, 91.850166, 0.0]]}]},
			"L_elbow_shaper_05_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_elbow_shaper_05_PIV_CTLShape", "degree": 1, "form": 0, "points": [[55.135136, 91.850166, 0.028435], [55.132075, 91.861017, 0.038845], [55.129013, 91.850166, 0.049256], [55.132075, 91.839315, 0.038845], [55.135136, 91.850166, 0.028435], [55.142484, 91.850166, 0.041907], [55.129013, 91.850166, 0.049256], [55.121665, 91.850166, 0.035784], [55.132075, 91.861017, 0.038845], [55.142484, 91.850166, 0.041907], [55.132075, 91.839315, 0.038845], [55.121665, 91.850166, 0.035784], [55.135136, 91.850166, 0.028435], [55.142484, 91.850166, 0.041907], [54.15, 91.850166, -0.25]]}, {"shapeName": "L_elbow_shaper_05_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[54.153062, 92.873837, -0.26041], [54.13959, 92.873837, -0.253062], [54.146938, 92.873837, -0.23959], [54.16041, 92.873837, -0.246938], [54.153062, 92.873837, -0.26041], [54.15, 92.884687, -0.25], [54.146938, 92.873837, -0.23959], [54.15, 92.862986, -0.25], [54.13959, 92.873837, -0.253062], [54.15, 92.884687, -0.25], [54.16041, 92.873837, -0.246938], [54.15, 92.862986, -0.25], [54.153062, 92.873837, -0.26041], [54.15, 92.884687, -0.25], [54.15, 91.850166, -0.25]]}, {"shapeName": "L_elbow_shaper_05_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[53.861155, 91.861017, 0.732075], [53.850744, 91.850166, 0.729013], [53.861155, 91.839315, 0.732075], [53.871565, 91.850166, 0.735136], [53.861155, 91.861017, 0.732075], [53.858093, 91.850166, 0.742484], [53.861155, 91.839315, 0.732075], [53.864216, 91.850166, 0.721665], [53.850744, 91.850166, 0.729013], [53.858093, 91.850166, 0.742484], [53.871565, 91.850166, 0.735136], [53.864216, 91.850166, 0.721665], [53.861155, 91.861017, 0.732075], [53.858093, 91.850166, 0.742484], [54.15, 91.850166, -0.25]]}]},
			"L_legBase_CTL": {"color": 6, "shapes": [{"shapeName": "L_legBase_CTLShape", "degree": 3, "form": 0, "points": [[5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 44.429485, 1.228048], [5.0, 44.677862, 3.215062], [5.0, 44.772733, 3.974036], [9.70811, 44.677862, 3.215062], [12.617885, 44.429485, 1.228048], [12.617885, 44.122473, -1.228048], [9.70811, 43.874096, -3.215062], [5.0, 43.779225, -3.974036], [5.0, 43.874096, -3.215062], [5.0, 44.122473, -1.228048], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0]]}]},
			"R_bendyLeg_A_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.333332, 34.524048, 3.234556], [-3.933332, 34.524048, 3.234556], [-5.0, 34.648083, 4.226834], [-6.066668, 34.524048, 3.234556], [-5.666668, 34.524048, 3.234556], [-5.666668, 34.358669, 1.91152], [-7.0, 34.358669, 1.91152], [-7.0, 34.408283, 2.308431], [-8.0, 34.275979, 1.25], [-7.0, 34.143675, 0.191569], [-7.0, 34.193289, 0.58848], [-5.666668, 34.193289, 0.58848], [-5.666668, 34.027909, -0.734556], [-6.066668, 34.027909, -0.734556], [-5.0, 33.903875, -1.726834], [-3.933332, 34.027909, -0.734556], [-4.333332, 34.027909, -0.734556], [-4.333332, 34.193289, 0.58848], [-3.0, 34.193289, 0.58848], [-3.0, 34.143675, 0.191569], [-2.0, 34.275979, 1.25], [-3.0, 34.408283, 2.308431], [-3.0, 34.358669, 1.91152], [-4.333332, 34.358669, 1.91152], [-4.333332, 34.524048, 3.234556]]}]},
			"L_shoulder_shaper_02_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_02_CTLShape", "degree": 1, "form": 0, "points": [[24.5, 94.350166, -1.25], [24.59218, 94.369196, -1.275605], [24.670326, 94.423391, -1.297313], [24.722544, 94.504496, -1.311818], [24.740879, 94.600166, -1.316911], [24.722544, 94.695836, -1.311818], [24.670326, 94.776941, -1.297313], [24.59218, 94.831136, -1.275605], [24.5, 94.850166, -1.25], [24.40782, 94.831136, -1.224395], [24.329674, 94.776941, -1.202687], [24.277456, 94.695836, -1.188182], [24.259121, 94.600166, -1.183089], [24.277456, 94.504496, -1.188182], [24.329674, 94.423391, -1.202687], [24.40782, 94.369196, -1.224395], [24.5, 94.350166, -1.25], [24.5, 91.850166, -1.25]]}]},
			"L_bendyLeg_B_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.249999, 24.285649, 4.749979], [3.799999, 24.285649, 4.749979], [5.0, 24.290484, 5.874969], [6.200001, 24.285649, 4.749979], [5.750001, 24.285649, 4.749979], [5.750001, 24.279202, 3.249995], [7.25, 24.279202, 3.249995], [7.25, 24.281136, 3.69999], [8.375, 24.275979, 2.5], [7.25, 24.270822, 1.30001], [7.25, 24.272756, 1.750005], [5.750001, 24.272756, 1.750005], [5.750001, 24.266309, 0.250021], [6.200001, 24.266309, 0.250021], [5.0, 24.261474, -0.874969], [3.799999, 24.266309, 0.250021], [4.249999, 24.266309, 0.250021], [4.249999, 24.272756, 1.750005], [2.75, 24.272756, 1.750005], [2.75, 24.270822, 1.30001], [1.625, 24.275979, 2.5], [2.75, 24.281136, 3.69999], [2.75, 24.279202, 3.249995], [4.249999, 24.279202, 3.249995], [4.249999, 24.285649, 4.749979]]}]},
			"L_toe_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toe_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 0.330234, 10.118355], [4.945745, 0.275979, 10.118355], [5.0, 0.221724, 10.118355], [5.054255, 0.275979, 10.118355], [5.0, 0.330234, 10.118355], [5.0, 0.275979, 10.172605], [5.0, 0.221724, 10.118355], [5.0, 0.275979, 10.0641], [4.945745, 0.275979, 10.118355], [5.0, 0.275979, 10.172605], [5.054255, 0.275979, 10.118355], [5.0, 0.275979, 10.0641], [5.0, 0.330234, 10.118355], [5.0, 0.275979, 10.172605], [5.0, 0.275979, 5.0]]}, {"shapeName": "L_toe_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 0.330234, 5.0], [-0.118355, 0.275979, 4.945745], [-0.118355, 0.221724, 5.0], [-0.118355, 0.275979, 5.054255], [-0.118355, 0.330234, 5.0], [-0.172605, 0.275979, 5.0], [-0.118355, 0.221724, 5.0], [-0.0641, 0.275979, 5.0], [-0.118355, 0.275979, 4.945745], [-0.172605, 0.275979, 5.0], [-0.118355, 0.275979, 5.054255], [-0.0641, 0.275979, 5.0], [-0.118355, 0.330234, 5.0], [-0.172605, 0.275979, 5.0], [5.0, 0.275979, 5.0]]}, {"shapeName": "L_toe_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, -4.842376, 5.0], [5.0, -4.842376, 4.945745], [5.054255, -4.842376, 5.0], [5.0, -4.842376, 5.054255], [4.945745, -4.842376, 5.0], [5.0, -4.896626, 5.0], [5.054255, -4.842376, 5.0], [5.0, -4.788121, 5.0], [5.0, -4.842376, 4.945745], [5.0, -4.896626, 5.0], [5.0, -4.842376, 5.054255], [5.0, -4.788121, 5.0], [4.945745, -4.842376, 5.0], [5.0, -4.896626, 5.0], [5.0, 0.275979, 5.0]]}]},
			"R_upLeg_shaper_01_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upLeg_shaper_01_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 35.870545, 1.105357], [-4.945745, 35.863815, 1.05152], [-5.0, 35.857086, 0.997684], [-5.054255, 35.863815, 1.05152], [-5.0, 35.870545, 1.105357], [-5.0, 35.809984, 1.058249], [-5.0, 35.857086, 0.997684], [-5.0, 35.917651, 1.044791], [-4.945745, 35.863815, 1.05152], [-5.0, 35.809984, 1.058249], [-5.054255, 35.863815, 1.05152], [-5.0, 35.917651, 1.044791], [-5.0, 35.870545, 1.105357], [-5.0, 35.809984, 1.058249], [-5.0, 40.942646, 0.416667]]}, {"shapeName": "R_upLeg_shaper_01_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 40.949375, 0.470503], [0.118355, 40.996482, 0.409937], [0.118355, 40.935916, 0.362831], [0.118355, 40.88881, 0.423396], [0.118355, 40.949375, 0.470503], [0.172605, 40.942646, 0.416667], [0.118355, 40.935916, 0.362831], [0.0641, 40.942646, 0.416667], [0.118355, 40.996482, 0.409937], [0.172605, 40.942646, 0.416667], [0.118355, 40.88881, 0.423396], [0.0641, 40.942646, 0.416667], [0.118355, 40.949375, 0.470503], [0.172605, 40.942646, 0.416667], [-5.0, 40.942646, 0.416667]]}, {"shapeName": "R_upLeg_shaper_01_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 40.307792, -4.662164], [-5.0, 40.361628, -4.668893], [-5.054255, 40.307792, -4.662164], [-5.0, 40.253956, -4.655434], [-4.945745, 40.307792, -4.662164], [-5.0, 40.301063, -4.715995], [-5.054255, 40.307792, -4.662164], [-5.0, 40.314521, -4.608328], [-5.0, 40.361628, -4.668893], [-5.0, 40.301063, -4.715995], [-5.0, 40.253956, -4.655434], [-5.0, 40.314521, -4.608328], [-4.945745, 40.307792, -4.662164], [-5.0, 40.301063, -4.715995], [-5.0, 40.942646, 0.416667]]}]},
			"R_elbow_shaper_01_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_01_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-38.85, 93.850166, -4.75], [-38.923426, 93.86539, -4.728404], [-38.985673, 93.908746, -4.710096], [-39.027268, 93.97363, -4.697862], [-39.041873, 94.050166, -4.693567], [-39.027268, 94.126702, -4.697862], [-38.985673, 94.191586, -4.710096], [-38.923426, 94.234942, -4.728404], [-38.85, 94.250166, -4.75], [-38.776574, 94.234942, -4.771596], [-38.714327, 94.191586, -4.789904], [-38.672732, 94.126702, -4.802138], [-38.658127, 94.050166, -4.806433], [-38.672732, 93.97363, -4.802138], [-38.714327, 93.908746, -4.789904], [-38.776574, 93.86539, -4.771596], [-38.85, 93.850166, -4.75], [-38.85, 91.850166, -4.75]]}]},
			"R_shoulder_shaper_02_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_shaper_02_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-25.483421, 91.850166, -1.534434], [-25.486325, 91.861017, -1.523979], [-25.48923, 91.850166, -1.513524], [-25.486325, 91.839315, -1.523979], [-25.483421, 91.850166, -1.534434], [-25.49678, 91.850166, -1.526883], [-25.48923, 91.850166, -1.513524], [-25.47587, 91.850166, -1.521075], [-25.486325, 91.861017, -1.523979], [-25.49678, 91.850166, -1.526883], [-25.486325, 91.839315, -1.523979], [-25.47587, 91.850166, -1.521075], [-25.483421, 91.850166, -1.534434], [-25.49678, 91.850166, -1.526883], [-24.5, 91.850166, -1.25]]}, {"shapeName": "R_shoulder_shaper_02_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-24.497096, 92.873837, -1.260455], [-24.489545, 92.873837, -1.247096], [-24.502904, 92.873837, -1.239545], [-24.510455, 92.873837, -1.252904], [-24.497096, 92.873837, -1.260455], [-24.5, 92.884687, -1.25], [-24.502904, 92.873837, -1.239545], [-24.5, 92.862986, -1.25], [-24.489545, 92.873837, -1.247096], [-24.5, 92.884687, -1.25], [-24.510455, 92.873837, -1.252904], [-24.5, 92.862986, -1.25], [-24.497096, 92.873837, -1.260455], [-24.5, 92.884687, -1.25], [-24.5, 91.850166, -1.25]]}, {"shapeName": "R_shoulder_shaper_02_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-24.773979, 91.861017, -0.263675], [-24.763524, 91.850166, -0.26077], [-24.773979, 91.839315, -0.263675], [-24.784434, 91.850166, -0.266579], [-24.773979, 91.861017, -0.263675], [-24.776883, 91.850166, -0.25322], [-24.773979, 91.839315, -0.263675], [-24.771075, 91.850166, -0.27413], [-24.763524, 91.850166, -0.26077], [-24.776883, 91.850166, -0.25322], [-24.784434, 91.850166, -0.266579], [-24.771075, 91.850166, -0.27413], [-24.773979, 91.861017, -0.263675], [-24.776883, 91.850166, -0.25322], [-24.5, 91.850166, -1.25]]}]},
			"R_toe_IK_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_CTLShape", "degree": 3, "form": 2, "points": [[-6.95903, 2.235009, 6.25], [-5.0, 3.046464, 6.25], [-3.04097, 2.235009, 6.25], [-2.229515, 0.275979, 6.25], [-3.04097, -1.683051, 6.25], [-5.0, -2.494506, 6.25], [-6.95903, -1.683051, 6.25], [-7.770485, 0.275979, 6.25]]}]},
			"L_shoulder_shaper_02_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_02_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[24.5, 93.850166, -1.25], [24.573744, 93.86539, -1.270484], [24.636261, 93.908746, -1.28785], [24.678035, 93.97363, -1.299454], [24.692704, 94.050166, -1.303529], [24.678035, 94.126702, -1.299454], [24.636261, 94.191586, -1.28785], [24.573744, 94.234942, -1.270484], [24.5, 94.250166, -1.25], [24.426256, 94.234942, -1.229516], [24.363739, 94.191586, -1.21215], [24.321965, 94.126702, -1.200546], [24.307296, 94.050166, -1.196471], [24.321965, 93.97363, -1.200546], [24.363739, 93.908746, -1.21215], [24.426256, 93.86539, -1.229516], [24.5, 93.850166, -1.25], [24.5, 91.850166, -1.25]]}]},
			"R_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-70.102054, 91.842036, 1.195745], [-70.106381, 91.896118, 1.25], [-70.102054, 91.842036, 1.304255], [-70.097728, 91.787954, 1.25], [-70.102054, 91.842036, 1.195745], [-70.156132, 91.83771, 1.25], [-70.102054, 91.842036, 1.304255], [-70.047972, 91.846363, 1.25], [-70.106381, 91.896118, 1.25], [-70.156132, 91.83771, 1.25], [-70.097728, 91.787954, 1.25], [-70.047972, 91.846363, 1.25], [-70.102054, 91.842036, 1.195745], [-70.156132, 91.83771, 1.25], [-65.0, 92.2502, 1.25]]}, {"shapeName": "R_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.408164, 97.352255, 1.195745], [-65.354082, 97.356581, 1.25], [-65.408164, 97.352255, 1.304255], [-65.462247, 97.347928, 1.25], [-65.408164, 97.352255, 1.195745], [-65.412491, 97.406332, 1.25], [-65.408164, 97.352255, 1.304255], [-65.403838, 97.298173, 1.25], [-65.354082, 97.356581, 1.25], [-65.412491, 97.406332, 1.25], [-65.462247, 97.347928, 1.25], [-65.403838, 97.298173, 1.25], [-65.408164, 97.352255, 1.195745], [-65.412491, 97.406332, 1.25], [-65.0, 92.2502, 1.25]]}, {"shapeName": "R_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-65.004327, 92.304283, 6.368355], [-64.945918, 92.254527, 6.368355], [-64.995673, 92.196118, 6.368355], [-65.054082, 92.245874, 6.368355], [-65.004327, 92.304283, 6.368355], [-65.0, 92.2502, 6.422605], [-64.995673, 92.196118, 6.368355], [-65.0, 92.2502, 6.3141], [-64.945918, 92.254527, 6.368355], [-65.0, 92.2502, 6.422605], [-65.054082, 92.245874, 6.368355], [-65.0, 92.2502, 6.3141], [-65.004327, 92.304283, 6.368355], [-65.0, 92.2502, 6.422605], [-65.0, 92.2502, 1.25]]}]},
			"L_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[70.102054, 91.842002, -1.304255], [70.106381, 91.896084, -1.25], [70.102054, 91.842002, -1.195745], [70.097728, 91.78792, -1.25], [70.102054, 91.842002, -1.304255], [70.156132, 91.837676, -1.25], [70.102054, 91.842002, -1.195745], [70.047972, 91.846329, -1.25], [70.106381, 91.896084, -1.25], [70.156132, 91.837676, -1.25], [70.097728, 91.78792, -1.25], [70.047972, 91.846329, -1.25], [70.102054, 91.842002, -1.304255], [70.156132, 91.837676, -1.25], [65.0, 92.250166, -1.25]]}, {"shapeName": "L_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.408164, 97.352221, -1.304255], [65.354082, 97.356547, -1.25], [65.408164, 97.352221, -1.195745], [65.462247, 97.347894, -1.25], [65.408164, 97.352221, -1.304255], [65.412491, 97.406298, -1.25], [65.408164, 97.352221, -1.195745], [65.403838, 97.298139, -1.25], [65.354082, 97.356547, -1.25], [65.412491, 97.406298, -1.25], [65.462247, 97.347894, -1.25], [65.403838, 97.298139, -1.25], [65.408164, 97.352221, -1.304255], [65.412491, 97.406298, -1.25], [65.0, 92.250166, -1.25]]}, {"shapeName": "L_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.004327, 92.304249, 3.868355], [64.945918, 92.254493, 3.868355], [64.995673, 92.196084, 3.868355], [65.054082, 92.24584, 3.868355], [65.004327, 92.304249, 3.868355], [65.0, 92.250166, 3.922605], [64.995673, 92.196084, 3.868355], [65.0, 92.250166, 3.8141], [64.945918, 92.254493, 3.868355], [65.0, 92.250166, 3.922605], [65.054082, 92.24584, 3.868355], [65.0, 92.250166, 3.8141], [65.004327, 92.304249, 3.868355], [65.0, 92.250166, 3.922605], [65.0, 92.250166, -1.25]]}]},
			"L_loLeg_shaper_04_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_04_CTLShape", "degree": 1, "form": 0, "points": [[17.5, 9.942646, 0.833333], [17.59515, 9.372467, 0.767034], [17.866125, 8.889094, 0.710827], [18.27165, 8.5661, 0.67327], [18.75, 8.452685, 0.660082], [19.22835, 8.5661, 0.67327], [19.633875, 8.889094, 0.710827], [19.90485, 9.372467, 0.767034], [20.0, 9.942646, 0.833333], [19.90485, 10.512824, 0.899633], [19.633875, 10.996197, 0.955839], [19.22835, 11.319191, 0.993397], [18.75, 11.432607, 1.006585], [18.27165, 11.319191, 0.993397], [17.866125, 10.996197, 0.955839], [17.59515, 10.512824, 0.899633], [17.5, 9.942646, 0.833333], [5.0, 9.942646, 0.833333]]}]},
			"L_leg_IK_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_leg_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[7.644691, 2.775979, -4.407818], [5.0, 2.775979, -6.233591], [2.355309, 2.775979, -4.407818], [1.259845, 2.775979, 0.0], [2.355309, 2.775979, 4.407818], [5.0, 2.775979, 6.233591], [7.644691, 2.775979, 4.407818], [8.740155, 2.775979, 0.0]]}]},
			"L_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_C_CTLShape", "degree": 1, "form": 0, "points": [[65.80742, 92.937969, -0.5], [64.312197, 93.057587, -0.5], [64.312197, 93.057587, -2.0], [65.80742, 92.937969, -2.0], [65.687803, 91.442746, -2.0], [64.19258, 91.562364, -2.0], [64.19258, 91.562364, -0.5], [65.687803, 91.442746, -0.5], [65.80742, 92.937969, -0.5], [65.80742, 92.937969, -2.0], [64.312197, 93.057587, -2.0], [64.19258, 91.562364, -2.0], [65.687803, 91.442746, -2.0], [65.687803, 91.442746, -0.5], [64.19258, 91.562364, -0.5], [64.312197, 93.057587, -0.5]]}]},
			"R_shoulder_shaper_02_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_02_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-24.5, 94.100166, -1.25], [-24.582962, 94.117293, -1.273045], [-24.653293, 94.166069, -1.292581], [-24.700289, 94.239063, -1.305636], [-24.716792, 94.325166, -1.31022], [-24.700289, 94.411269, -1.305636], [-24.653293, 94.484264, -1.292581], [-24.582962, 94.533039, -1.273045], [-24.5, 94.550166, -1.25], [-24.417038, 94.533039, -1.226955], [-24.346707, 94.484264, -1.207419], [-24.299711, 94.411269, -1.194364], [-24.283208, 94.325166, -1.18978], [-24.299711, 94.239063, -1.194364], [-24.346707, 94.166069, -1.207419], [-24.417038, 94.117293, -1.226955], [-24.5, 94.100166, -1.25], [-24.5, 91.850166, -1.25]]}]},
			"L_elbow_shaper_01_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_01_CTLShape", "degree": 1, "form": 0, "points": [[38.85, 94.350166, -4.75], [38.941782, 94.369196, -4.723005], [39.019592, 94.423391, -4.70012], [39.071585, 94.504496, -4.684828], [39.089841, 94.600166, -4.679458], [39.071585, 94.695836, -4.684828], [39.019592, 94.776941, -4.70012], [38.941782, 94.831136, -4.723005], [38.85, 94.850166, -4.75], [38.758218, 94.831136, -4.776995], [38.680408, 94.776941, -4.79988], [38.628415, 94.695836, -4.815172], [38.610159, 94.600166, -4.820542], [38.628415, 94.504496, -4.815172], [38.680408, 94.423391, -4.79988], [38.758218, 94.369196, -4.776995], [38.85, 94.350166, -4.75], [38.85, 91.850166, -4.75]]}]},
			"C_hip_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.347257, 51.850166, -5.289381], [0.0, 49.150166, -7.480309], [-6.347257, 51.850166, -5.289381], [-8.976371, 54.550166, 0.0], [-6.347257, 51.850166, 5.289381], [0.0, 49.150166, 7.480309], [6.347257, 51.850166, 5.289381], [8.976371, 54.550166, 0.0]]}]},
			"L_loLeg_shaper_03_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_03_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.25, 13.525979, 1.25], [16.335635, 13.012819, 1.19033], [16.579512, 12.577783, 1.139745], [16.944485, 12.287088, 1.105943], [17.375, 12.185014, 1.094074], [17.805515, 12.287088, 1.105943], [18.170488, 12.577783, 1.139745], [18.414365, 13.012819, 1.19033], [18.5, 13.525979, 1.25], [18.414365, 14.039139, 1.30967], [18.170488, 14.474175, 1.360255], [17.805515, 14.76487, 1.394057], [17.375, 14.866944, 1.405926], [16.944485, 14.76487, 1.394057], [16.579512, 14.474175, 1.360255], [16.335635, 14.039139, 1.30967], [16.25, 13.525979, 1.25], [5.0, 13.525979, 1.25]]}]},
			"R_lwrArmRibbonMid_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lwrArmRibbonMid_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-47.346499, 92.850168, -5.378097], [-47.346499, 93.450168, -5.378097], [-47.769748, 91.850166, -6.817145], [-47.346499, 90.250164, -5.378097], [-47.346499, 90.850164, -5.378097], [-46.782167, 90.850164, -3.459367], [-46.782167, 88.850166, -3.459367], [-46.951467, 88.850166, -4.034987], [-46.5, 87.350166, -2.5], [-46.048533, 88.850166, -0.965013], [-46.217833, 88.850166, -1.540633], [-46.217833, 90.850164, -1.540633], [-45.653501, 90.850164, 0.378097], [-45.653501, 90.250164, 0.378097], [-45.230252, 91.850166, 1.817145], [-45.653501, 93.450168, 0.378097], [-45.653501, 92.850168, 0.378097], [-46.217833, 92.850168, -1.540633], [-46.217833, 94.850166, -1.540633], [-46.048533, 94.850166, -0.965013], [-46.5, 96.350166, -2.5], [-46.951467, 94.850166, -4.034987], [-46.782167, 94.850166, -3.459367], [-46.782167, 92.850168, -3.459367], [-47.346499, 92.850168, -5.378097]]}]},
			"L_clavicle_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_clavicle_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.214818, 91.850166, -0.342266], [5.218337, 91.861017, -0.332001], [5.221857, 91.850166, -0.321737], [5.218337, 91.839315, -0.332001], [5.214818, 91.850166, -0.342266], [5.228601, 91.850166, -0.33552], [5.221857, 91.850166, -0.321737], [5.208073, 91.850166, -0.328482], [5.218337, 91.861017, -0.332001], [5.228601, 91.850166, -0.33552], [5.218337, 91.839315, -0.332001], [5.208073, 91.850166, -0.328482], [5.214818, 91.850166, -0.342266], [5.228601, 91.850166, -0.33552], [4.25, 91.850166, 0.0]]}, {"shapeName": "L_clavicle_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[4.246481, 92.873837, -0.010264], [4.239736, 92.873837, 0.003519], [4.253519, 92.873837, 0.010264], [4.260264, 92.873837, -0.003519], [4.246481, 92.873837, -0.010264], [4.25, 92.884687, 0.0], [4.253519, 92.873837, 0.010264], [4.25, 92.862986, 0.0], [4.239736, 92.873837, 0.003519], [4.25, 92.884687, 0.0], [4.260264, 92.873837, -0.003519], [4.25, 92.862986, 0.0], [4.246481, 92.873837, -0.010264], [4.25, 92.884687, 0.0], [4.25, 91.850166, 0.0]]}, {"shapeName": "L_clavicle_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.582001, 91.861017, 0.968337], [4.571737, 91.850166, 0.971857], [4.582001, 91.839315, 0.968337], [4.592266, 91.850166, 0.964818], [4.582001, 91.861017, 0.968337], [4.58552, 91.850166, 0.978601], [4.582001, 91.839315, 0.968337], [4.578482, 91.850166, 0.958073], [4.571737, 91.850166, 0.971857], [4.58552, 91.850166, 0.978601], [4.592266, 91.850166, 0.964818], [4.578482, 91.850166, 0.958073], [4.582001, 91.861017, 0.968337], [4.58552, 91.850166, 0.978601], [4.25, 91.850166, 0.0]]}]},
			"C_spineShaper_4_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_spineShaper_4_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 75.718521, -0.054255], [-0.054255, 75.718521, 0.0], [0.0, 75.718521, 0.054255], [0.054255, 75.718521, 0.0], [0.0, 75.718521, -0.054255], [0.0, 75.772771, 0.0], [0.0, 75.718521, 0.054255], [0.0, 75.664266, 0.0], [-0.054255, 75.718521, 0.0], [0.0, 75.772771, 0.0], [0.054255, 75.718521, 0.0], [0.0, 75.664266, 0.0], [0.0, 75.718521, -0.054255], [0.0, 75.772771, 0.0], [0.0, 70.600166, 0.0]]}, {"shapeName": "C_spineShaper_4_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 70.600166, -0.054255], [-5.118355, 70.545911, 0.0], [-5.118355, 70.600166, 0.054255], [-5.118355, 70.654421, 0.0], [-5.118355, 70.600166, -0.054255], [-5.172605, 70.600166, 0.0], [-5.118355, 70.600166, 0.054255], [-5.0641, 70.600166, 0.0], [-5.118355, 70.545911, 0.0], [-5.172605, 70.600166, 0.0], [-5.118355, 70.654421, 0.0], [-5.0641, 70.600166, 0.0], [-5.118355, 70.600166, -0.054255], [-5.172605, 70.600166, 0.0], [0.0, 70.600166, 0.0]]}, {"shapeName": "C_spineShaper_4_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 70.600166, 5.118355], [0.0, 70.545911, 5.118355], [0.054255, 70.600166, 5.118355], [0.0, 70.654421, 5.118355], [-0.054255, 70.600166, 5.118355], [0.0, 70.600166, 5.172605], [0.054255, 70.600166, 5.118355], [0.0, 70.600166, 5.0641], [0.0, 70.545911, 5.118355], [0.0, 70.600166, 5.172605], [0.0, 70.654421, 5.118355], [0.0, 70.600166, 5.0641], [-0.054255, 70.600166, 5.118355], [0.0, 70.600166, 5.172605], [0.0, 70.600166, 0.0]]}]},
			"L_scapulaChest_CTL": {"color": 17, "shapes": [{"shapeName": "L_scapulaChest_CTLShape", "degree": 3, "form": 2, "points": [[0.0, 90.674748, -1.175418], [0.0, 91.850166, -1.662291], [0.0, 93.025584, -1.175418], [0.0, 93.512457, 0.0], [0.0, 93.025584, 1.175418], [0.0, 91.850166, 1.662291], [0.0, 90.674748, 1.175418], [0.0, 90.187875, 0.0]]}, {"shapeName": "L_scapulaChest_CTLShape1", "degree": 3, "form": 2, "points": [[1.175418, 91.850166, -1.175418], [0.0, 91.850166, -1.662291], [-1.175418, 91.850166, -1.175418], [-1.662291, 91.850166, 0.0], [-1.175418, 91.850166, 1.175418], [0.0, 91.850166, 1.662291], [1.175418, 91.850166, 1.175418], [1.662291, 91.850166, 0.0]]}, {"shapeName": "L_scapulaChest_CTLShape2", "degree": 3, "form": 2, "points": [[1.175418, 93.025584, 0.0], [0.0, 93.512457, 0.0], [-1.175418, 93.025584, 0.0], [-1.662291, 91.850166, 0.0], [-1.175418, 90.674748, 0.0], [0.0, 90.187875, 0.0], [1.175418, 90.674748, 0.0], [1.662291, 91.850166, 0.0]]}]},
			"R_heel_CTL": {"color": 20, "shapes": [{"shapeName": "R_heel_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 0.275979, -1.75], [-5.0, -0.224021, -2.25], [-5.5, 0.275979, -2.25], [-5.0, 0.275979, -1.75], [-4.5, 0.275979, -2.25], [-5.0, -0.224021, -2.25], [-5.0, 0.275979, -2.75], [-4.5, 0.275979, -2.25], [-5.0, 0.775979, -2.25], [-5.0, 0.275979, -1.75], [-5.5, 0.275979, -2.25], [-5.0, 0.275979, -2.75], [-5.0, 0.775979, -2.25], [-5.5, 0.275979, -2.25]]}]},
			"C_midSpine_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midSpine_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[4.231505, 64.350166, -3.526254], [0.0, 64.350166, -4.986873], [-4.231505, 64.350166, -3.526254], [-5.984248, 64.350166, 0.0], [-4.231505, 64.350166, 3.526254], [0.0, 64.350166, 4.986873], [4.231505, 64.350166, 3.526254], [5.984248, 64.350166, 0.0]]}]},
			"R_bendyLeg_B_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.499999, 24.282426, 3.999986], [-4.199999, 24.282426, 3.999986], [-5.0, 24.285649, 4.749979], [-5.800001, 24.282426, 3.999986], [-5.500001, 24.282426, 3.999986], [-5.500001, 24.278128, 2.999996], [-6.5, 24.278128, 2.999996], [-6.5, 24.279417, 3.299994], [-7.25, 24.275979, 2.5], [-6.5, 24.272541, 1.700006], [-6.5, 24.27383, 2.000004], [-5.500001, 24.27383, 2.000004], [-5.500001, 24.269532, 1.000014], [-5.800001, 24.269532, 1.000014], [-5.0, 24.266309, 0.250021], [-4.199999, 24.269532, 1.000014], [-4.499999, 24.269532, 1.000014], [-4.499999, 24.27383, 2.000004], [-3.5, 24.27383, 2.000004], [-3.5, 24.272541, 1.700006], [-2.75, 24.275979, 2.5], [-3.5, 24.279417, 3.299994], [-3.5, 24.278128, 2.999996], [-4.499999, 24.278128, 2.999996], [-4.499999, 24.282426, 3.999986]]}]},
			"R_shoulder_shaper_04_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_04_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-33.5, 93.350166, -3.75], [-33.555308, 93.361584, -3.765363], [-33.602196, 93.394101, -3.778388], [-33.633526, 93.442764, -3.787091], [-33.644528, 93.500166, -3.790147], [-33.633526, 93.557568, -3.787091], [-33.602196, 93.606231, -3.778388], [-33.555308, 93.638748, -3.765363], [-33.5, 93.650166, -3.75], [-33.444692, 93.638748, -3.734637], [-33.397804, 93.606231, -3.721612], [-33.366474, 93.557568, -3.712909], [-33.355472, 93.500166, -3.709853], [-33.366474, 93.442764, -3.712909], [-33.397804, 93.394101, -3.721612], [-33.444692, 93.361584, -3.734637], [-33.5, 93.350166, -3.75], [-33.5, 91.850166, -3.75]]}]},
			"L_elbowRibbon_CTL": {"color": 17, "shapes": [{"shapeName": "L_elbowRibbon_CTLShape", "degree": 1, "form": 0, "points": [[38.037761, 93.516836, -9.999857], [38.037761, 94.516836, -9.999857], [38.056642, 91.850166, -12.499786], [38.037761, 89.183496, -9.999857], [38.037761, 90.183496, -9.999857], [38.012587, 90.183496, -6.666622], [38.012587, 86.850166, -6.666622], [38.020139, 86.850166, -7.666594], [38.0, 84.350166, -5.0], [37.979861, 86.850166, -2.333406], [37.987413, 86.850166, -3.333378], [37.987413, 90.183496, -3.333378], [37.962239, 90.183496, -0.000143], [37.962239, 89.183496, -0.000143], [37.943358, 91.850166, 2.499786], [37.962239, 94.516836, -0.000143], [37.962239, 93.516836, -0.000143], [37.987413, 93.516836, -3.333378], [37.987413, 96.850166, -3.333378], [37.979861, 96.850166, -2.333406], [38.0, 99.350166, -5.0], [38.020139, 96.850166, -7.666594], [38.012587, 96.850166, -6.666622], [38.012587, 93.516836, -6.666622], [38.037761, 93.516836, -9.999857]]}]},
			"R_leg_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, -2.314387, -0.537283], [-4.945745, -2.308121, -0.591174], [-5.0, -2.301854, -0.645066], [-5.054255, -2.308121, -0.591174], [-5.0, -2.314387, -0.537283], [-5.0, -2.362008, -0.59744], [-5.0, -2.301854, -0.645066], [-5.0, -2.254229, -0.584908], [-4.945745, -2.308121, -0.591174], [-5.0, -2.362008, -0.59744], [-5.054255, -2.308121, -0.591174], [-5.0, -2.254229, -0.584908], [-5.0, -2.314387, -0.537283], [-5.0, -2.362008, -0.59744], [-5.0, 2.775979, -0.0]]}, {"shapeName": "R_leg_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 2.769713, 0.053892], [0.118355, 2.829871, 0.006266], [0.118355, 2.782246, -0.053892], [0.118355, 2.722087, -0.006266], [0.118355, 2.769713, 0.053892], [0.172605, 2.775979, 0.0], [0.118355, 2.782246, -0.053892], [0.0641, 2.775979, 0.0], [0.118355, 2.829871, 0.006266], [0.172605, 2.775979, 0.0], [0.118355, 2.722087, -0.006266], [0.0641, 2.775979, 0.0], [0.118355, 2.769713, 0.053892], [0.172605, 2.775979, 0.0], [-5.0, 2.775979, -0.0]]}, {"shapeName": "R_leg_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 3.367153, -5.0841], [-5.0, 3.421045, -5.077833], [-5.054255, 3.367153, -5.0841], [-5.0, 3.313262, -5.090366], [-4.945745, 3.367153, -5.0841], [-5.0, 3.373419, -5.137987], [-5.054255, 3.367153, -5.0841], [-5.0, 3.360887, -5.030208], [-5.0, 3.421045, -5.077833], [-5.0, 3.373419, -5.137987], [-5.0, 3.313262, -5.090366], [-5.0, 3.360887, -5.030208], [-4.945745, 3.367153, -5.0841], [-5.0, 3.373419, -5.137987], [-5.0, 2.775979, -0.0]]}]},
			"L_legBase_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_legBase_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 43.416345, 0.107454], [5.0, 42.025435, 0.281318], [5.0, 41.494154, 0.347728], [5.0, 42.434214, 3.551545], [5.0, 44.077763, 5.398795], [5.0, 45.79703, 5.183887], [5.0, 46.935301, 2.988909], [5.0, 47.057804, -0.347728], [5.0, 46.526522, -0.281318], [5.0, 45.135613, -0.107454], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0]]}]},
			"R_elbowRibbon_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_elbowRibbon_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-39.023724, 91.850166, -5.00312], [-39.023642, 91.861017, -4.992269], [-39.02356, 91.850166, -4.981418], [-39.023642, 91.839315, -4.992269], [-39.023724, 91.850166, -5.00312], [-39.034491, 91.850166, -4.992187], [-39.02356, 91.850166, -4.981418], [-39.012791, 91.850166, -4.992351], [-39.023642, 91.861017, -4.992269], [-39.034491, 91.850166, -4.992187], [-39.023642, 91.839315, -4.992269], [-39.012791, 91.850166, -4.992351], [-39.023724, 91.850166, -5.00312], [-39.034491, 91.850166, -4.992187], [-38.0, 91.850166, -5.0]]}, {"shapeName": "R_elbowRibbon_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-38.000082, 92.873837, -5.010851], [-37.989149, 92.873837, -5.000082], [-37.999918, 92.873837, -4.989149], [-38.010851, 92.873837, -4.999918], [-38.000082, 92.873837, -5.010851], [-38.0, 92.884687, -5.0], [-37.999918, 92.873837, -4.989149], [-38.0, 92.862986, -5.0], [-37.989149, 92.873837, -5.000082], [-38.0, 92.884687, -5.0], [-38.010851, 92.873837, -4.999918], [-38.0, 92.862986, -5.0], [-38.000082, 92.873837, -5.010851], [-38.0, 92.884687, -5.0], [-38.0, 91.850166, -5.0]]}, {"shapeName": "R_elbowRibbon_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-37.992269, 91.861017, -3.976358], [-37.981418, 91.850166, -3.97644], [-37.992269, 91.839315, -3.976358], [-38.00312, 91.850166, -3.976276], [-37.992269, 91.861017, -3.976358], [-37.992187, 91.850166, -3.965509], [-37.992269, 91.839315, -3.976358], [-37.992351, 91.850166, -3.987209], [-37.981418, 91.850166, -3.97644], [-37.992187, 91.850166, -3.965509], [-38.00312, 91.850166, -3.976276], [-37.992351, 91.850166, -3.987209], [-37.992269, 91.861017, -3.976358], [-37.992187, 91.850166, -3.965509], [-38.0, 91.850166, -5.0]]}]},
			"R_elbowFk_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_elbowFk_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-38.985136, 91.850166, -4.721565], [-38.982075, 91.861017, -4.711155], [-38.979013, 91.850166, -4.700744], [-38.982075, 91.839315, -4.711155], [-38.985136, 91.850166, -4.721565], [-38.992484, 91.850166, -4.708093], [-38.979013, 91.850166, -4.700744], [-38.971665, 91.850166, -4.714216], [-38.982075, 91.861017, -4.711155], [-38.992484, 91.850166, -4.708093], [-38.982075, 91.839315, -4.711155], [-38.971665, 91.850166, -4.714216], [-38.985136, 91.850166, -4.721565], [-38.992484, 91.850166, -4.708093], [-38.0, 91.850166, -5.0]]}, {"shapeName": "R_elbowFk_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-38.003062, 92.873837, -5.01041], [-37.98959, 92.873837, -5.003062], [-37.996938, 92.873837, -4.98959], [-38.01041, 92.873837, -4.996938], [-38.003062, 92.873837, -5.01041], [-38.0, 92.884687, -5.0], [-37.996938, 92.873837, -4.98959], [-38.0, 92.862986, -5.0], [-37.98959, 92.873837, -5.003062], [-38.0, 92.884687, -5.0], [-38.01041, 92.873837, -4.996938], [-38.0, 92.862986, -5.0], [-38.003062, 92.873837, -5.01041], [-38.0, 92.884687, -5.0], [-38.0, 91.850166, -5.0]]}, {"shapeName": "R_elbowFk_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-37.711155, 91.861017, -4.017925], [-37.700744, 91.850166, -4.020987], [-37.711155, 91.839315, -4.017925], [-37.721565, 91.850166, -4.014864], [-37.711155, 91.861017, -4.017925], [-37.708093, 91.850166, -4.007516], [-37.711155, 91.839315, -4.017925], [-37.714216, 91.850166, -4.028335], [-37.700744, 91.850166, -4.020987], [-37.708093, 91.850166, -4.007516], [-37.721565, 91.850166, -4.014864], [-37.714216, 91.850166, -4.028335], [-37.711155, 91.861017, -4.017925], [-37.708093, 91.850166, -4.007516], [-38.0, 91.850166, -5.0]]}]},
			"L_loLeg_shaper_05_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_shaper_05_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 1.268946, -0.120616], [4.945745, 1.275213, -0.174508], [5.0, 1.281479, -0.2284], [5.054255, 1.275213, -0.174508], [5.0, 1.268946, -0.120616], [5.0, 1.221326, -0.180774], [5.0, 1.281479, -0.2284], [5.0, 1.329104, -0.168241], [4.945745, 1.275213, -0.174508], [5.0, 1.221326, -0.180774], [5.054255, 1.275213, -0.174508], [5.0, 1.329104, -0.168241], [5.0, 1.268946, -0.120616], [5.0, 1.221326, -0.180774], [5.0, 6.359312, 0.416667]]}, {"shapeName": "L_loLeg_shaper_05_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 6.353046, 0.470559], [-0.118355, 6.413204, 0.422933], [-0.118355, 6.365579, 0.362775], [-0.118355, 6.30542, 0.4104], [-0.118355, 6.353046, 0.470559], [-0.172605, 6.359312, 0.416667], [-0.118355, 6.365579, 0.362775], [-0.0641, 6.359312, 0.416667], [-0.118355, 6.413204, 0.422933], [-0.172605, 6.359312, 0.416667], [-0.118355, 6.30542, 0.4104], [-0.0641, 6.359312, 0.416667], [-0.118355, 6.353046, 0.470559], [-0.172605, 6.359312, 0.416667], [5.0, 6.359312, 0.416667]]}, {"shapeName": "L_loLeg_shaper_05_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 6.950487, -4.667433], [5.0, 7.004379, -4.661167], [5.054255, 6.950487, -4.667433], [5.0, 6.896595, -4.6737], [4.945745, 6.950487, -4.667433], [5.0, 6.956753, -4.72132], [5.054255, 6.950487, -4.667433], [5.0, 6.94422, -4.613541], [5.0, 7.004379, -4.661167], [5.0, 6.956753, -4.72132], [5.0, 6.896595, -4.6737], [5.0, 6.94422, -4.613541], [4.945745, 6.950487, -4.667433], [5.0, 6.956753, -4.72132], [5.0, 6.359312, 0.416667]]}]},
			"R_loLeg_shaper_02_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_02_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.25, 17.109312, 1.666667], [-16.335635, 16.596152, 1.606997], [-16.579512, 16.161116, 1.556411], [-16.944485, 15.870422, 1.52261], [-17.375, 15.768347, 1.510741], [-17.805515, 15.870422, 1.52261], [-18.170488, 16.161116, 1.556411], [-18.414365, 16.596152, 1.606997], [-18.5, 17.109312, 1.666667], [-18.414365, 17.622473, 1.726336], [-18.170488, 18.057509, 1.776922], [-17.805515, 18.348203, 1.810724], [-17.375, 18.450277, 1.822593], [-16.944485, 18.348203, 1.810724], [-16.579512, 18.057509, 1.776922], [-16.335635, 17.622473, 1.726336], [-16.25, 17.109312, 1.666667], [-5.0, 17.109312, 1.666667]]}]},
			"R_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_A_CTLShape", "degree": 1, "form": 0, "points": [[-61.894298, 92.69271, -0.5], [-60.407456, 92.494464, -0.5], [-60.407456, 92.494464, -2.0], [-61.894298, 92.69271, -2.0], [-62.092544, 91.205868, -2.0], [-60.605702, 91.007623, -2.0], [-60.605702, 91.007623, -0.5], [-62.092544, 91.205868, -0.5], [-61.894298, 92.69271, -0.5], [-61.894298, 92.69271, -2.0], [-60.407456, 92.494464, -2.0], [-60.605702, 91.007623, -2.0], [-62.092544, 91.205868, -2.0], [-62.092544, 91.205868, -0.5], [-60.605702, 91.007623, -0.5], [-60.407456, 92.494464, -0.5]]}]},
			"R_leg_IK_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-7.350836, 2.775979, -3.91806], [-5.0, 2.775979, -5.54097], [-2.649164, 2.775979, -3.91806], [-1.675418, 2.775979, 0.0], [-2.649164, 2.775979, 3.91806], [-5.0, 2.775979, 5.54097], [-7.350836, 2.775979, 3.91806], [-8.324582, 2.775979, -0.0]]}]},
			"C_head_top_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_top_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 111.850166, -0.054255], [5.118355, 111.904421, 0.0], [5.118355, 111.850166, 0.054255], [5.118355, 111.795911, 0.0], [5.118355, 111.850166, -0.054255], [5.172605, 111.850166, 0.0], [5.118355, 111.850166, 0.054255], [5.0641, 111.850166, 0.0], [5.118355, 111.904421, 0.0], [5.172605, 111.850166, 0.0], [5.118355, 111.795911, 0.0], [5.0641, 111.850166, 0.0], [5.118355, 111.850166, -0.054255], [5.172605, 111.850166, 0.0], [0.0, 111.850166, 0.0]]}, {"shapeName": "C_head_top_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 116.968521, -0.054255], [-0.054255, 116.968521, 0.0], [0.0, 116.968521, 0.054255], [0.054255, 116.968521, 0.0], [0.0, 116.968521, -0.054255], [0.0, 117.022771, 0.0], [0.0, 116.968521, 0.054255], [0.0, 116.914266, 0.0], [-0.054255, 116.968521, 0.0], [0.0, 117.022771, 0.0], [0.054255, 116.968521, 0.0], [0.0, 116.914266, 0.0], [0.0, 116.968521, -0.054255], [0.0, 117.022771, 0.0], [0.0, 111.850166, 0.0]]}, {"shapeName": "C_head_top_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 111.904421, 5.118355], [-0.054255, 111.850166, 5.118355], [0.0, 111.795911, 5.118355], [0.054255, 111.850166, 5.118355], [0.0, 111.904421, 5.118355], [0.0, 111.850166, 5.172605], [0.0, 111.795911, 5.118355], [0.0, 111.850166, 5.0641], [-0.054255, 111.850166, 5.118355], [0.0, 111.850166, 5.172605], [0.054255, 111.850166, 5.118355], [0.0, 111.850166, 5.0641], [0.0, 111.904421, 5.118355], [0.0, 111.850166, 5.172605], [0.0, 111.850166, 0.0]]}]},
			"R_outterBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_outterBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.381645, 0.275979, 5.054255], [-2.381645, 0.330234, 5.0], [-2.381645, 0.275979, 4.945745], [-2.381645, 0.221724, 5.0], [-2.381645, 0.275979, 5.054255], [-2.327395, 0.275979, 5.0], [-2.381645, 0.275979, 4.945745], [-2.4359, 0.275979, 5.0], [-2.381645, 0.330234, 5.0], [-2.327395, 0.275979, 5.0], [-2.381645, 0.221724, 5.0], [-2.4359, 0.275979, 5.0], [-2.381645, 0.275979, 5.054255], [-2.327395, 0.275979, 5.0], [-7.5, 0.275979, 5.0]]}, {"shapeName": "R_outterBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-7.5, 5.394334, 5.054255], [-7.554255, 5.394334, 5.0], [-7.5, 5.394334, 4.945745], [-7.445745, 5.394334, 5.0], [-7.5, 5.394334, 5.054255], [-7.5, 5.448584, 5.0], [-7.5, 5.394334, 4.945745], [-7.5, 5.340079, 5.0], [-7.554255, 5.394334, 5.0], [-7.5, 5.448584, 5.0], [-7.445745, 5.394334, 5.0], [-7.5, 5.340079, 5.0], [-7.5, 5.394334, 5.054255], [-7.5, 5.448584, 5.0], [-7.5, 0.275979, 5.0]]}, {"shapeName": "R_outterBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-7.5, 0.330234, -0.118355], [-7.554255, 0.275979, -0.118355], [-7.5, 0.221724, -0.118355], [-7.445745, 0.275979, -0.118355], [-7.5, 0.330234, -0.118355], [-7.5, 0.275979, -0.172605], [-7.5, 0.221724, -0.118355], [-7.5, 0.275979, -0.0641], [-7.554255, 0.275979, -0.118355], [-7.5, 0.275979, -0.172605], [-7.445745, 0.275979, -0.118355], [-7.5, 0.275979, -0.0641], [-7.5, 0.330234, -0.118355], [-7.5, 0.275979, -0.172605], [-7.5, 0.275979, 5.0]]}]},
			"C_neck_FK_C_CTL": {"color": 4, "shapes": [{"shapeName": "C_neck_FK_C_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 98.516833, 0.0], [-5.03806, 98.708173, 0.0], [-5.14645, 98.870383, 0.0], [-5.30866, 98.978773, 0.0], [-5.5, 99.016833, 0.0], [-5.69134, 98.978773, 0.0], [-5.85355, 98.870383, 0.0], [-5.96194, 98.708173, 0.0], [-6.0, 98.516833, 0.0], [-5.96194, 98.325493, 0.0], [-5.85355, 98.163283, 0.0], [-5.69134, 98.054893, 0.0], [-5.5, 98.016833, 0.0], [-5.30866, 98.054893, 0.0], [-5.14645, 98.163283, 0.0], [-5.03806, 98.325493, 0.0], [-5.0, 98.516833, 0.0], [0.0, 98.516833, 0.0]]}]},
			"C_spineShaper_2_CTL": {"color": 4, "shapes": [{"shapeName": "C_spineShaper_2_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 58.100166, -7.5], [0.0, 58.387176, -7.55709], [0.0, 58.630491, -7.719675], [0.0, 58.793076, -7.96299], [0.0, 58.850166, -8.25], [0.0, 58.793076, -8.53701], [0.0, 58.630491, -8.780325], [0.0, 58.387176, -8.94291], [0.0, 58.100166, -9.0], [0.0, 57.813156, -8.94291], [0.0, 57.569841, -8.780325], [0.0, 57.407256, -8.53701], [0.0, 57.350166, -8.25], [0.0, 57.407256, -7.96299], [0.0, 57.569841, -7.719675], [0.0, 57.813156, -7.55709], [0.0, 58.100166, -7.5], [0.0, 58.100166, 0.0]]}]},
			"L_legBase_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_legBase_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 43.170736, 0.138155], [5.0, 41.382423, 0.361694], [5.0, 40.699347, 0.447079], [5.0, 41.907995, 4.566273], [5.0, 44.02113, 6.941308], [5.0, 46.231616, 6.664997], [5.0, 47.695107, 3.842884], [5.0, 47.852611, -0.447079], [5.0, 47.169535, -0.361694], [5.0, 45.381222, -0.138155], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0]]}]},
			"C_neckBase_A_OFF_CTL": {"color": 25, "shapes": [{"shapeName": "C_neckBase_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[5.843618, 95.214323, -4.698932], [-0.085671, 92.438824, -5.741927], [-6.442397, 93.965578, -4.642481], [-6.416571, 94.131833, 4.655973], [0.122667, 91.069294, 9.305715], [5.869443, 95.380579, 4.599523], [5.843618, 95.214323, -4.698932]]}]},
			"L_bendyLeg_B_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.333332, 24.284575, 4.499982], [3.933332, 24.284575, 4.499982], [5.0, 24.288873, 5.499972], [6.066668, 24.284575, 4.499982], [5.666668, 24.284575, 4.499982], [5.666668, 24.278844, 3.166662], [7.0, 24.278844, 3.166662], [7.0, 24.280563, 3.566658], [8.0, 24.275979, 2.5], [7.0, 24.271395, 1.433342], [7.0, 24.273114, 1.833338], [5.666668, 24.273114, 1.833338], [5.666668, 24.267383, 0.500018], [6.066668, 24.267383, 0.500018], [5.0, 24.263085, -0.499972], [3.933332, 24.267383, 0.500018], [4.333332, 24.267383, 0.500018], [4.333332, 24.273114, 1.833338], [3.0, 24.273114, 1.833338], [3.0, 24.271395, 1.433342], [2.0, 24.275979, 2.5], [3.0, 24.280563, 3.566658], [3.0, 24.278844, 3.166662], [4.333332, 24.278844, 3.166662], [4.333332, 24.284575, 4.499982]]}]},
			"L_upLeg_shaper_03_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_03_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.25, 34.275979, 1.25], [16.335635, 33.76335, 1.314079], [16.579512, 33.328765, 1.368402], [16.944485, 33.038372, 1.404701], [17.375, 32.936404, 1.417447], [17.805515, 33.038372, 1.404701], [18.170488, 33.328765, 1.368402], [18.414365, 33.76335, 1.314079], [18.5, 34.275979, 1.25], [18.414365, 34.788608, 1.185921], [18.170488, 35.223193, 1.131598], [17.805515, 35.513586, 1.095299], [17.375, 35.615554, 1.082553], [16.944485, 35.513586, 1.095299], [16.579512, 35.223193, 1.131598], [16.335635, 34.788608, 1.185921], [16.25, 34.275979, 1.25], [5.0, 34.275979, 1.25]]}]},
			"C_cog_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-10.5, 49.350166, -10.5], [-10.5, 49.350166, 10.5], [10.5, 49.350166, 10.5], [10.5, 49.350166, -10.5], [-10.5, 49.350166, -10.5]]}]},
			"L_bendyLeg_C_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_C_CTLShape", "degree": 1, "form": 0, "points": [[4.166665, 13.237227, 3.733268], [3.666665, 13.237227, 3.733268], [5.0, 13.092851, 4.974903], [6.333335, 13.237227, 3.733268], [5.833335, 13.237227, 3.733268], [5.833335, 13.429728, 2.077758], [7.5, 13.429728, 2.077758], [7.5, 13.371978, 2.574411], [8.75, 13.525979, 1.25], [7.5, 13.67998, -0.074411], [7.5, 13.62223, 0.422242], [5.833335, 13.62223, 0.422242], [5.833335, 13.814731, -1.233268], [6.333335, 13.814731, -1.233268], [5.0, 13.959107, -2.474903], [3.666665, 13.814731, -1.233268], [4.166665, 13.814731, -1.233268], [4.166665, 13.62223, 0.422242], [2.5, 13.62223, 0.422242], [2.5, 13.67998, -0.074411], [1.25, 13.525979, 1.25], [2.5, 13.371978, 2.574411], [2.5, 13.429728, 2.077758], [4.166665, 13.429728, 2.077758], [4.166665, 13.237227, 3.733268]]}]},
			"R_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.323456, 92.526661, 1.195745], [-66.316286, 92.58044, 1.25], [-66.323456, 92.526661, 1.304255], [-66.330627, 92.472882, 1.25], [-66.323456, 92.526661, 1.195745], [-66.37723, 92.533831, 1.25], [-66.323456, 92.526661, 1.304255], [-66.269677, 92.519491, 1.25], [-66.316286, 92.58044, 1.25], [-66.37723, 92.533831, 1.25], [-66.330627, 92.472882, 1.25], [-66.269677, 92.519491, 1.25], [-66.323456, 92.526661, 1.195745], [-66.37723, 92.533831, 1.25], [-61.25, 91.8502, 1.25]]}, {"shapeName": "R_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-60.573539, 96.923657, 1.195745], [-60.51976, 96.916486, 1.25], [-60.573539, 96.923657, 1.304255], [-60.627318, 96.930827, 1.25], [-60.573539, 96.923657, 1.195745], [-60.566369, 96.977431, 1.25], [-60.573539, 96.923657, 1.304255], [-60.58071, 96.869878, 1.25], [-60.51976, 96.916486, 1.25], [-60.566369, 96.977431, 1.25], [-60.627318, 96.930827, 1.25], [-60.58071, 96.869878, 1.25], [-60.573539, 96.923657, 1.195745], [-60.566369, 96.977431, 1.25], [-61.25, 91.8502, 1.25]]}, {"shapeName": "R_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.242829, 91.903979, 6.368355], [-61.196221, 91.84303, 6.368355], [-61.257171, 91.796421, 6.368355], [-61.303779, 91.857371, 6.368355], [-61.242829, 91.903979, 6.368355], [-61.25, 91.8502, 6.422605], [-61.257171, 91.796421, 6.368355], [-61.25, 91.8502, 6.3141], [-61.196221, 91.84303, 6.368355], [-61.25, 91.8502, 6.422605], [-61.303779, 91.857371, 6.368355], [-61.25, 91.8502, 6.3141], [-61.242829, 91.903979, 6.368355], [-61.25, 91.8502, 6.422605], [-61.25, 91.8502, 1.25]]}]},
			"L_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.323456, 92.526627, -1.304255], [66.316286, 92.580406, -1.25], [66.323456, 92.526627, -1.195745], [66.330627, 92.472848, -1.25], [66.323456, 92.526627, -1.304255], [66.37723, 92.533797, -1.25], [66.323456, 92.526627, -1.195745], [66.269677, 92.519457, -1.25], [66.316286, 92.580406, -1.25], [66.37723, 92.533797, -1.25], [66.330627, 92.472848, -1.25], [66.269677, 92.519457, -1.25], [66.323456, 92.526627, -1.304255], [66.37723, 92.533797, -1.25], [61.25, 91.850166, -1.25]]}, {"shapeName": "L_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[60.573539, 96.923623, -1.304255], [60.51976, 96.916452, -1.25], [60.573539, 96.923623, -1.195745], [60.627318, 96.930793, -1.25], [60.573539, 96.923623, -1.304255], [60.566369, 96.977397, -1.25], [60.573539, 96.923623, -1.195745], [60.58071, 96.869844, -1.25], [60.51976, 96.916452, -1.25], [60.566369, 96.977397, -1.25], [60.627318, 96.930793, -1.25], [60.58071, 96.869844, -1.25], [60.573539, 96.923623, -1.304255], [60.566369, 96.977397, -1.25], [61.25, 91.850166, -1.25]]}, {"shapeName": "L_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.242829, 91.903945, 3.868355], [61.196221, 91.842996, 3.868355], [61.257171, 91.796387, 3.868355], [61.303779, 91.857337, 3.868355], [61.242829, 91.903945, 3.868355], [61.25, 91.850166, 3.922605], [61.257171, 91.796387, 3.868355], [61.25, 91.850166, 3.8141], [61.196221, 91.842996, 3.868355], [61.25, 91.850166, 3.922605], [61.303779, 91.857337, 3.868355], [61.25, 91.850166, 3.8141], [61.242829, 91.903945, 3.868355], [61.25, 91.850166, 3.922605], [61.25, 91.850166, -1.25]]}]},
			"R_upLeg_shaper_05_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_05_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-15.0, 27.609312, 2.083333], [-15.07612, 27.153642, 2.140292], [-15.2929, 26.767345, 2.188579], [-15.61732, 26.509217, 2.220845], [-16.0, 26.418579, 2.232175], [-16.38268, 26.509217, 2.220845], [-16.7071, 26.767345, 2.188579], [-16.92388, 27.153642, 2.140292], [-17.0, 27.609312, 2.083333], [-16.92388, 28.064982, 2.026375], [-16.7071, 28.45128, 1.978087], [-16.38268, 28.709407, 1.945821], [-16.0, 28.800046, 1.934492], [-15.61732, 28.709407, 1.945821], [-15.2929, 28.45128, 1.978087], [-15.07612, 28.064982, 2.026375], [-15.0, 27.609312, 2.083333], [-5.0, 27.609312, 2.083333]]}]},
			"R_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_A_CTLShape", "degree": 1, "form": 0, "points": [[-61.894298, 92.69271, 2.0], [-60.407456, 92.494464, 2.0], [-60.407456, 92.494464, 0.5], [-61.894298, 92.69271, 0.5], [-62.092544, 91.205868, 0.5], [-60.605702, 91.007623, 0.5], [-60.605702, 91.007623, 2.0], [-62.092544, 91.205868, 2.0], [-61.894298, 92.69271, 2.0], [-61.894298, 92.69271, 0.5], [-60.407456, 92.494464, 0.5], [-60.605702, 91.007623, 0.5], [-62.092544, 91.205868, 0.5], [-62.092544, 91.205868, 2.0], [-60.605702, 91.007623, 2.0], [-60.407456, 92.494464, 2.0]]}]},
			"L_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_A_CTLShape", "degree": 1, "form": 0, "points": [[61.894298, 92.69271, 0.75], [60.407456, 92.494464, 0.75], [60.407456, 92.494464, -0.75], [61.894298, 92.69271, -0.75], [62.092544, 91.205868, -0.75], [60.605702, 91.007623, -0.75], [60.605702, 91.007623, 0.75], [62.092544, 91.205868, 0.75], [61.894298, 92.69271, 0.75], [61.894298, 92.69271, -0.75], [60.407456, 92.494464, -0.75], [60.605702, 91.007623, -0.75], [62.092544, 91.205868, -0.75], [62.092544, 91.205868, 0.75], [60.605702, 91.007623, 0.75], [60.407456, 92.494464, 0.75]]}]},
			"L_loLeg_shaper_01_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_01_CTLShape", "degree": 1, "form": 0, "points": [[17.5, 20.692646, 2.083333], [17.59515, 20.122467, 2.017034], [17.866125, 19.639094, 1.960827], [18.27165, 19.3161, 1.92327], [18.75, 19.202685, 1.910082], [19.22835, 19.3161, 1.92327], [19.633875, 19.639094, 1.960827], [19.90485, 20.122467, 2.017034], [20.0, 20.692646, 2.083333], [19.90485, 21.262824, 2.149633], [19.633875, 21.746197, 2.205839], [19.22835, 22.069191, 2.243397], [18.75, 22.182607, 2.256585], [18.27165, 22.069191, 2.243397], [17.866125, 21.746197, 2.205839], [17.59515, 21.262824, 2.149633], [17.5, 20.692646, 2.083333], [5.0, 20.692646, 2.083333]]}]},
			"L_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_D_CTLShape", "degree": 1, "form": 0, "points": [[67.717544, 92.744464, -1.75], [66.230702, 92.94271, -1.75], [66.230702, 92.94271, -3.25], [67.717544, 92.744464, -3.25], [67.519298, 91.257623, -3.25], [66.032456, 91.455868, -3.25], [66.032456, 91.455868, -1.75], [67.519298, 91.257623, -1.75], [67.717544, 92.744464, -1.75], [67.717544, 92.744464, -3.25], [66.230702, 92.94271, -3.25], [66.032456, 91.455868, -3.25], [67.519298, 91.257623, -3.25], [67.519298, 91.257623, -1.75], [66.032456, 91.455868, -1.75], [66.230702, 92.94271, -1.75]]}]},
			"L_shoulder_shaper_05_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_05_CTLShape", "degree": 1, "form": 0, "points": [[37.1, 94.350166, -4.75], [37.19218, 94.369196, -4.775605], [37.270326, 94.423391, -4.797313], [37.322544, 94.504496, -4.811818], [37.340879, 94.600166, -4.816911], [37.322544, 94.695836, -4.811818], [37.270326, 94.776941, -4.797313], [37.19218, 94.831136, -4.775605], [37.1, 94.850166, -4.75], [37.00782, 94.831136, -4.724395], [36.929674, 94.776941, -4.702687], [36.877456, 94.695836, -4.688182], [36.859121, 94.600166, -4.683089], [36.877456, 94.504496, -4.688182], [36.929674, 94.423391, -4.702687], [37.00782, 94.369196, -4.724395], [37.1, 94.350166, -4.75], [37.1, 91.850166, -4.75]]}]},
			"L_clavicle_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_clavicle_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [3.115508, 91.850166, -3.308934], [1.279872, 91.850166, -8.662875], [0.578719, 91.850166, -10.707904], [1.279872, 98.503758, -8.662875], [3.115508, 102.61591, -3.308934], [5.384492, 102.61591, 3.308934], [7.220128, 98.503758, 8.662875], [7.921281, 91.850166, 10.707904], [7.220128, 91.850166, 8.662875], [5.384492, 91.850166, 3.308934], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0]]}]},
			"L_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.227054, 92.508331, -2.554255], [68.222728, 92.562413, -2.5], [68.227054, 92.508331, -2.445745], [68.231381, 92.454248, -2.5], [68.227054, 92.508331, -2.554255], [68.281132, 92.512657, -2.5], [68.227054, 92.508331, -2.445745], [68.172972, 92.504004, -2.5], [68.222728, 92.562413, -2.5], [68.281132, 92.512657, -2.5], [68.231381, 92.454248, -2.5], [68.172972, 92.504004, -2.5], [68.227054, 92.508331, -2.554255], [68.281132, 92.512657, -2.5], [63.125, 92.100166, -2.5]]}, {"shapeName": "L_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[62.716836, 97.202221, -2.554255], [62.662753, 97.197894, -2.5], [62.716836, 97.202221, -2.445745], [62.770918, 97.206547, -2.5], [62.716836, 97.202221, -2.554255], [62.712509, 97.256298, -2.5], [62.716836, 97.202221, -2.445745], [62.721162, 97.148139, -2.5], [62.662753, 97.197894, -2.5], [62.712509, 97.256298, -2.5], [62.770918, 97.206547, -2.5], [62.721162, 97.148139, -2.5], [62.716836, 97.202221, -2.554255], [62.712509, 97.256298, -2.5], [63.125, 92.100166, -2.5]]}, {"shapeName": "L_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[63.120673, 92.154249, 2.618355], [63.070918, 92.09584, 2.618355], [63.129327, 92.046084, 2.618355], [63.179082, 92.104493, 2.618355], [63.120673, 92.154249, 2.618355], [63.125, 92.100166, 2.672605], [63.129327, 92.046084, 2.618355], [63.125, 92.100166, 2.5641], [63.070918, 92.09584, 2.618355], [63.125, 92.100166, 2.672605], [63.179082, 92.104493, 2.618355], [63.125, 92.100166, 2.5641], [63.120673, 92.154249, 2.618355], [63.125, 92.100166, 2.672605], [63.125, 92.100166, -2.5]]}]},
			"L_elbow_shaper_02_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_02_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[42.25, 93.350166, -3.75], [42.305069, 93.361584, -3.733803], [42.351755, 93.394101, -3.720072], [42.382951, 93.442764, -3.710897], [42.393905, 93.500166, -3.707675], [42.382951, 93.557568, -3.710897], [42.351755, 93.606231, -3.720072], [42.305069, 93.638748, -3.733803], [42.25, 93.650166, -3.75], [42.194931, 93.638748, -3.766197], [42.148245, 93.606231, -3.779928], [42.117049, 93.557568, -3.789103], [42.106095, 93.500166, -3.792325], [42.117049, 93.442764, -3.789103], [42.148245, 93.394101, -3.779928], [42.194931, 93.361584, -3.766197], [42.25, 93.350166, -3.75], [42.25, 91.850166, -3.75]]}]},
			"C_chest_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_CTLShape", "degree": 3, "form": 2, "points": [[7.052508, 76.850166, -5.87709], [0.0, 79.850166, -8.311455], [-7.052508, 76.850166, -5.87709], [-9.973746, 73.850166, 0.0], [-7.052508, 76.850166, 5.87709], [0.0, 79.850166, 8.311455], [7.052508, 76.850166, 5.87709], [9.973746, 73.850166, 0.0]]}]},
			"R_upLeg_shaper_03_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_03_CTLShape", "degree": 1, "form": 0, "points": [[-17.5, 34.275979, 1.25], [-17.59515, 33.706392, 1.321198], [-17.866125, 33.223519, 1.381557], [-18.27165, 32.90086, 1.42189], [-18.75, 32.787562, 1.436052], [-19.22835, 32.90086, 1.42189], [-19.633875, 33.223519, 1.381557], [-19.90485, 33.706392, 1.321198], [-20.0, 34.275979, 1.25], [-19.90485, 34.845566, 1.178802], [-19.633875, 35.328438, 1.118443], [-19.22835, 35.651097, 1.07811], [-18.75, 35.764396, 1.063948], [-18.27165, 35.651097, 1.07811], [-17.866125, 35.328438, 1.118443], [-17.59515, 34.845566, 1.178802], [-17.5, 34.275979, 1.25], [-5.0, 34.275979, 1.25]]}]},
			"L_loLeg_shaper_05_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_05_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[13.75, 6.359312, 0.416667], [13.816605, 5.960188, 0.370257], [14.006287, 5.621826, 0.330912], [14.290155, 5.395731, 0.304622], [14.625, 5.31634, 0.295391], [14.959845, 5.395731, 0.304622], [15.243712, 5.621826, 0.330912], [15.433395, 5.960188, 0.370257], [15.5, 6.359312, 0.416667], [15.433395, 6.758437, 0.463077], [15.243712, 7.096798, 0.502421], [14.959845, 7.322894, 0.528711], [14.625, 7.402285, 0.537943], [14.290155, 7.322894, 0.528711], [14.006287, 7.096798, 0.502421], [13.816605, 6.758437, 0.463077], [13.75, 6.359312, 0.416667], [5.0, 6.359312, 0.416667]]}]},
			"R_upLeg_shaper_02_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_02_CTLShape", "degree": 1, "form": 0, "points": [[-17.5, 37.609312, 0.833333], [-17.59515, 37.039725, 0.904532], [-17.866125, 36.556853, 0.964891], [-18.27165, 36.234194, 1.005223], [-18.75, 36.120895, 1.019385], [-19.22835, 36.234194, 1.005223], [-19.633875, 36.556853, 0.964891], [-19.90485, 37.039725, 0.904532], [-20.0, 37.609312, 0.833333], [-19.90485, 38.1789, 0.762135], [-19.633875, 38.661772, 0.701776], [-19.22835, 38.984431, 0.661444], [-18.75, 39.097729, 0.647281], [-18.27165, 38.984431, 0.661444], [-17.866125, 38.661772, 0.701776], [-17.59515, 38.1789, 0.762135], [-17.5, 37.609312, 0.833333], [-5.0, 37.609312, 0.833333]]}]},
			"R_uprArmRibbonMid_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_uprArmRibbonMid_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-29.983421, 91.850166, -2.784434], [-29.986325, 91.861017, -2.773979], [-29.98923, 91.850166, -2.763524], [-29.986325, 91.839315, -2.773979], [-29.983421, 91.850166, -2.784434], [-29.99678, 91.850166, -2.776883], [-29.98923, 91.850166, -2.763524], [-29.97587, 91.850166, -2.771075], [-29.986325, 91.861017, -2.773979], [-29.99678, 91.850166, -2.776883], [-29.986325, 91.839315, -2.773979], [-29.97587, 91.850166, -2.771075], [-29.983421, 91.850166, -2.784434], [-29.99678, 91.850166, -2.776883], [-29.0, 91.850166, -2.5]]}, {"shapeName": "R_uprArmRibbonMid_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-28.997096, 92.873837, -2.510455], [-28.989545, 92.873837, -2.497096], [-29.002904, 92.873837, -2.489545], [-29.010455, 92.873837, -2.502904], [-28.997096, 92.873837, -2.510455], [-29.0, 92.884687, -2.5], [-29.002904, 92.873837, -2.489545], [-29.0, 92.862986, -2.5], [-28.989545, 92.873837, -2.497096], [-29.0, 92.884687, -2.5], [-29.010455, 92.873837, -2.502904], [-29.0, 92.862986, -2.5], [-28.997096, 92.873837, -2.510455], [-29.0, 92.884687, -2.5], [-29.0, 91.850166, -2.5]]}, {"shapeName": "R_uprArmRibbonMid_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-29.273979, 91.861017, -1.513675], [-29.263524, 91.850166, -1.51077], [-29.273979, 91.839315, -1.513675], [-29.284434, 91.850166, -1.516579], [-29.273979, 91.861017, -1.513675], [-29.276883, 91.850166, -1.50322], [-29.273979, 91.839315, -1.513675], [-29.271075, 91.850166, -1.52413], [-29.263524, 91.850166, -1.51077], [-29.276883, 91.850166, -1.50322], [-29.284434, 91.850166, -1.516579], [-29.271075, 91.850166, -1.52413], [-29.273979, 91.861017, -1.513675], [-29.276883, 91.850166, -1.50322], [-29.0, 91.850166, -2.5]]}]},
			"R_loLeg_shaper_05_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_05_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-15.0, 6.359312, 0.416667], [-15.07612, 5.90317, 0.363627], [-15.2929, 5.516471, 0.318662], [-15.61732, 5.258076, 0.288616], [-16.0, 5.167344, 0.278066], [-16.38268, 5.258076, 0.288616], [-16.7071, 5.516471, 0.318662], [-16.92388, 5.90317, 0.363627], [-17.0, 6.359312, 0.416667], [-16.92388, 6.815455, 0.469707], [-16.7071, 7.202154, 0.514671], [-16.38268, 7.460549, 0.544717], [-16.0, 7.551281, 0.555268], [-15.61732, 7.460549, 0.544717], [-15.2929, 7.202154, 0.514671], [-15.07612, 6.815455, 0.469707], [-15.0, 6.359312, 0.416667], [-5.0, 6.359312, 0.416667]]}]},
			"R_leg_IK_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-6.763127, 2.775979, -2.938545], [-5.0, 2.775979, -4.155728], [-3.236873, 2.775979, -2.938545], [-2.506564, 2.775979, 0.0], [-3.236873, 2.775979, 2.938545], [-5.0, 2.775979, 4.155728], [-6.763127, 2.775979, 2.938545], [-7.493436, 2.775979, 0.0]]}]},
			"C_neckBase_C_OFF_CTL": {"color": 25, "shapes": [{"shapeName": "C_neckBase_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.545036, 94.467918, -3.654724], [-0.066633, 92.309196, -4.465943], [-5.010753, 93.496671, -3.610819], [-4.990667, 93.625981, 3.621313], [0.095407, 91.244006, 7.237779], [4.565123, 94.597228, 3.577407], [4.545036, 94.467918, -3.654724]]}]},
			"C_midNeck_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_CTLShape", "degree": 3, "form": 2, "points": [[7.052508, 96.850166, -5.87709], [0.0, 96.850166, -8.311455], [-7.052508, 96.850166, -5.87709], [-9.973746, 96.850166, 0.0], [-7.052508, 96.850166, 5.87709], [0.0, 96.850166, 8.311455], [7.052508, 96.850166, 5.87709], [9.973746, 96.850166, 0.0]]}]},
			"R_uprArmRibbonMid_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_uprArmRibbonMid_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-28.197068, 92.850168, -5.390554], [-28.197068, 93.450168, -5.390554], [-27.795603, 91.850166, -6.835831], [-28.197068, 90.250164, -5.390554], [-28.197068, 90.850164, -5.390554], [-28.732356, 90.850164, -3.46352], [-28.732356, 88.850166, -3.46352], [-28.571769, 88.850166, -4.041631], [-29.0, 87.350166, -2.5], [-29.428231, 88.850166, -0.958369], [-29.267644, 88.850166, -1.53648], [-29.267644, 90.850164, -1.53648], [-29.802932, 90.850164, 0.390554], [-29.802932, 90.250164, 0.390554], [-30.204397, 91.850166, 1.835831], [-29.802932, 93.450168, 0.390554], [-29.802932, 92.850168, 0.390554], [-29.267644, 92.850168, -1.53648], [-29.267644, 94.850166, -1.53648], [-29.428231, 94.850166, -0.958369], [-29.0, 96.350166, -2.5], [-28.571769, 94.850166, -4.041631], [-28.732356, 94.850166, -3.46352], [-28.732356, 92.850168, -3.46352], [-28.197068, 92.850168, -5.390554]]}]},
			"R_elbow_shaper_01_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_01_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-38.85, 94.100166, -4.75], [-38.932604, 94.117293, -4.725705], [-39.002633, 94.166069, -4.705108], [-39.049426, 94.239063, -4.691345], [-39.065857, 94.325166, -4.686513], [-39.049426, 94.411269, -4.691345], [-39.002633, 94.484264, -4.705108], [-38.932604, 94.533039, -4.725705], [-38.85, 94.550166, -4.75], [-38.767396, 94.533039, -4.774295], [-38.697367, 94.484264, -4.794892], [-38.650574, 94.411269, -4.808655], [-38.634143, 94.325166, -4.813487], [-38.650574, 94.239063, -4.808655], [-38.697367, 94.166069, -4.794892], [-38.767396, 94.117293, -4.774295], [-38.85, 94.100166, -4.75], [-38.85, 91.850166, -4.75]]}]},
			"R_shoulder_shaper_02_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_02_CTLShape", "degree": 1, "form": 0, "points": [[-24.5, 94.350166, -1.25], [-24.59218, 94.369196, -1.275605], [-24.670326, 94.423391, -1.297313], [-24.722544, 94.504496, -1.311818], [-24.740879, 94.600166, -1.316911], [-24.722544, 94.695836, -1.311818], [-24.670326, 94.776941, -1.297313], [-24.59218, 94.831136, -1.275605], [-24.5, 94.850166, -1.25], [-24.40782, 94.831136, -1.224395], [-24.329674, 94.776941, -1.202687], [-24.277456, 94.695836, -1.188182], [-24.259121, 94.600166, -1.183089], [-24.277456, 94.504496, -1.188182], [-24.329674, 94.423391, -1.202687], [-24.40782, 94.369196, -1.224395], [-24.5, 94.350166, -1.25], [-24.5, 91.850166, -1.25]]}]},
			"R_uprArmRibbonMid_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_uprArmRibbonMid_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-27.795603, 93.350169, -6.835831], [-27.795603, 94.250169, -6.835831], [-27.193404, 91.850166, -9.003746], [-27.795603, 89.450163, -6.835831], [-27.795603, 90.350163, -6.835831], [-28.598533, 90.350163, -3.94528], [-28.598533, 87.350166, -3.94528], [-28.357654, 87.350166, -4.812446], [-29.0, 85.100166, -2.5], [-29.642346, 87.350166, -0.187554], [-29.401467, 87.350166, -1.05472], [-29.401467, 90.350163, -1.05472], [-30.204397, 90.350163, 1.835831], [-30.204397, 89.450163, 1.835831], [-30.806596, 91.850166, 4.003746], [-30.204397, 94.250169, 1.835831], [-30.204397, 93.350169, 1.835831], [-29.401467, 93.350169, -1.05472], [-29.401467, 96.350166, -1.05472], [-29.642346, 96.350166, -0.187554], [-29.0, 98.600166, -2.5], [-28.357654, 96.350166, -4.812446], [-28.598533, 96.350166, -3.94528], [-28.598533, 93.350169, -3.94528], [-27.795603, 93.350169, -6.835831]]}]},
			"R_upLeg_shaper_03_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_03_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-15.0, 34.275979, 1.25], [-15.07612, 33.820309, 1.306959], [-15.2929, 33.434011, 1.355246], [-15.61732, 33.175884, 1.387512], [-16.0, 33.085246, 1.398842], [-16.38268, 33.175884, 1.387512], [-16.7071, 33.434011, 1.355246], [-16.92388, 33.820309, 1.306959], [-17.0, 34.275979, 1.25], [-16.92388, 34.731649, 1.193041], [-16.7071, 35.117947, 1.144754], [-16.38268, 35.376074, 1.112488], [-16.0, 35.466712, 1.101158], [-15.61732, 35.376074, 1.112488], [-15.2929, 35.117947, 1.144754], [-15.07612, 34.731649, 1.193041], [-15.0, 34.275979, 1.25], [-5.0, 34.275979, 1.25]]}]},
			"L_bendyLeg_C_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.499999, 13.352728, 2.739961], [4.199999, 13.352728, 2.739961], [5.0, 13.266102, 3.484942], [5.800001, 13.352728, 2.739961], [5.500001, 13.352728, 2.739961], [5.500001, 13.468228, 1.746655], [6.5, 13.468228, 1.746655], [6.5, 13.433578, 2.044647], [7.25, 13.525979, 1.25], [6.5, 13.61838, 0.455353], [6.5, 13.58373, 0.753345], [5.500001, 13.58373, 0.753345], [5.500001, 13.69923, -0.239961], [5.800001, 13.69923, -0.239961], [5.0, 13.785856, -0.984942], [4.199999, 13.69923, -0.239961], [4.499999, 13.69923, -0.239961], [4.499999, 13.58373, 0.753345], [3.5, 13.58373, 0.753345], [3.5, 13.61838, 0.455353], [2.75, 13.525979, 1.25], [3.5, 13.433578, 2.044647], [3.5, 13.468228, 1.746655], [4.499999, 13.468228, 1.746655], [4.499999, 13.352728, 2.739961]]}]},
			"R_elbow_shaper_01_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_01_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-38.85, 93.600166, -4.75], [-38.914248, 93.613487, -4.731104], [-38.968714, 93.651424, -4.715084], [-39.005109, 93.708197, -4.70438], [-39.017889, 93.775166, -4.700621], [-39.005109, 93.842135, -4.70438], [-38.968714, 93.898909, -4.715084], [-38.914248, 93.936845, -4.731104], [-38.85, 93.950166, -4.75], [-38.785752, 93.936845, -4.768896], [-38.731286, 93.898909, -4.784916], [-38.694891, 93.842135, -4.79562], [-38.682111, 93.775166, -4.799379], [-38.694891, 93.708197, -4.79562], [-38.731286, 93.651424, -4.784916], [-38.785752, 93.613487, -4.768896], [-38.85, 93.600166, -4.75], [-38.85, 91.850166, -4.75]]}]},
			"L_elbow_shaper_03_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_03_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[46.5, 93.350166, -2.5], [46.555069, 93.361584, -2.483803], [46.601755, 93.394101, -2.470072], [46.632951, 93.442764, -2.460897], [46.643905, 93.500166, -2.457675], [46.632951, 93.557568, -2.460897], [46.601755, 93.606231, -2.470072], [46.555069, 93.638748, -2.483803], [46.5, 93.650166, -2.5], [46.444931, 93.638748, -2.516197], [46.398245, 93.606231, -2.529928], [46.367049, 93.557568, -2.539103], [46.356095, 93.500166, -2.542325], [46.367049, 93.442764, -2.539103], [46.398245, 93.394101, -2.529928], [46.444931, 93.361584, -2.516197], [46.5, 93.350166, -2.5], [46.5, 91.850166, -2.5]]}]},
			"L_shoulder_shaper_05_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_05_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[37.1, 93.350166, -4.75], [37.155308, 93.361584, -4.765363], [37.202196, 93.394101, -4.778388], [37.233526, 93.442764, -4.787091], [37.244528, 93.500166, -4.790147], [37.233526, 93.557568, -4.787091], [37.202196, 93.606231, -4.778388], [37.155308, 93.638748, -4.765363], [37.1, 93.650166, -4.75], [37.044692, 93.638748, -4.734637], [36.997804, 93.606231, -4.721612], [36.966474, 93.557568, -4.712909], [36.955472, 93.500166, -4.709853], [36.966474, 93.442764, -4.712909], [36.997804, 93.394101, -4.721612], [37.044692, 93.361584, -4.734637], [37.1, 93.350166, -4.75], [37.1, 91.850166, -4.75]]}]},
			"L_shoulder_shaper_02_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_02_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[24.5, 93.350166, -1.25], [24.555308, 93.361584, -1.265363], [24.602196, 93.394101, -1.278388], [24.633526, 93.442764, -1.287091], [24.644528, 93.500166, -1.290147], [24.633526, 93.557568, -1.287091], [24.602196, 93.606231, -1.278388], [24.555308, 93.638748, -1.265363], [24.5, 93.650166, -1.25], [24.444692, 93.638748, -1.234637], [24.397804, 93.606231, -1.221612], [24.366474, 93.557568, -1.212909], [24.355472, 93.500166, -1.209853], [24.366474, 93.442764, -1.212909], [24.397804, 93.394101, -1.221612], [24.444692, 93.361584, -1.234637], [24.5, 93.350166, -1.25], [24.5, 91.850166, -1.25]]}]},
			"R_shoulder_shaper_01_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_01_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-20.9, 93.850166, -0.25], [-20.973744, 93.86539, -0.270484], [-21.036261, 93.908746, -0.28785], [-21.078035, 93.97363, -0.299454], [-21.092704, 94.050166, -0.303529], [-21.078035, 94.126702, -0.299454], [-21.036261, 94.191586, -0.28785], [-20.973744, 94.234942, -0.270484], [-20.9, 94.250166, -0.25], [-20.826256, 94.234942, -0.229516], [-20.763739, 94.191586, -0.21215], [-20.721965, 94.126702, -0.200546], [-20.707296, 94.050166, -0.196471], [-20.721965, 93.97363, -0.200546], [-20.763739, 93.908746, -0.21215], [-20.826256, 93.86539, -0.229516], [-20.9, 93.850166, -0.25], [-20.9, 91.850166, -0.25]]}]},
			"L_bendyLeg_A_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.333332, 34.524048, 3.234556], [3.933332, 34.524048, 3.234556], [5.0, 34.648083, 4.226834], [6.066668, 34.524048, 3.234556], [5.666668, 34.524048, 3.234556], [5.666668, 34.358669, 1.91152], [7.0, 34.358669, 1.91152], [7.0, 34.408283, 2.308431], [8.0, 34.275979, 1.25], [7.0, 34.143675, 0.191569], [7.0, 34.193289, 0.58848], [5.666668, 34.193289, 0.58848], [5.666668, 34.027909, -0.734556], [6.066668, 34.027909, -0.734556], [5.0, 33.903875, -1.726834], [3.933332, 34.027909, -0.734556], [4.333332, 34.027909, -0.734556], [4.333332, 34.193289, 0.58848], [3.0, 34.193289, 0.58848], [3.0, 34.143675, 0.191569], [2.0, 34.275979, 1.25], [3.0, 34.408283, 2.308431], [3.0, 34.358669, 1.91152], [4.333332, 34.358669, 1.91152], [4.333332, 34.524048, 3.234556]]}]},
			"R_toe_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_toe_FK_CTLShape", "degree": 3, "form": 2, "points": [[-6.95903, 2.235009, 5.0], [-5.0, 3.046464, 5.0], [-3.04097, 2.235009, 5.0], [-2.229515, 0.275979, 5.0], [-3.04097, -1.683051, 5.0], [-5.0, -2.494506, 5.0], [-6.95903, -1.683051, 5.0], [-7.770485, 0.275979, 5.0]]}]},
			"R_shoulder_shaper_05_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_05_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-37.1, 94.100166, -4.75], [-37.182962, 94.117293, -4.773045], [-37.253293, 94.166069, -4.792581], [-37.300289, 94.239063, -4.805636], [-37.316792, 94.325166, -4.81022], [-37.300289, 94.411269, -4.805636], [-37.253293, 94.484264, -4.792581], [-37.182962, 94.533039, -4.773045], [-37.1, 94.550166, -4.75], [-37.017038, 94.533039, -4.726955], [-36.946707, 94.484264, -4.707419], [-36.899711, 94.411269, -4.694364], [-36.883208, 94.325166, -4.68978], [-36.899711, 94.239063, -4.694364], [-36.946707, 94.166069, -4.707419], [-37.017038, 94.117293, -4.726955], [-37.1, 94.100166, -4.75], [-37.1, 91.850166, -4.75]]}]},
			"C_midSpine_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midSpine_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[5.642006, 64.350166, -4.701672], [0.0, 64.350166, -6.649164], [-5.642006, 64.350166, -4.701672], [-7.978997, 64.350166, 0.0], [-5.642006, 64.350166, 4.701672], [0.0, 64.350166, 6.649164], [5.642006, 64.350166, 4.701672], [7.978997, 64.350166, 0.0]]}]},
			"R_shoulder_shaper_05_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_05_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-37.1, 93.600166, -4.75], [-37.164526, 93.613487, -4.767924], [-37.219228, 93.651424, -4.783119], [-37.255781, 93.708197, -4.793272], [-37.268616, 93.775166, -4.796838], [-37.255781, 93.842135, -4.793272], [-37.219228, 93.898909, -4.783119], [-37.164526, 93.936845, -4.767924], [-37.1, 93.950166, -4.75], [-37.035474, 93.936845, -4.732076], [-36.980772, 93.898909, -4.716881], [-36.944219, 93.842135, -4.706728], [-36.931384, 93.775166, -4.703162], [-36.944219, 93.708197, -4.706728], [-36.980772, 93.651424, -4.716881], [-37.035474, 93.613487, -4.732076], [-37.1, 93.600166, -4.75], [-37.1, 91.850166, -4.75]]}]},
			"L_elbow_shaper_01_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_01_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[38.85, 93.850166, -4.75], [38.923426, 93.86539, -4.728404], [38.985673, 93.908746, -4.710096], [39.027268, 93.97363, -4.697862], [39.041873, 94.050166, -4.693567], [39.027268, 94.126702, -4.697862], [38.985673, 94.191586, -4.710096], [38.923426, 94.234942, -4.728404], [38.85, 94.250166, -4.75], [38.776574, 94.234942, -4.771596], [38.714327, 94.191586, -4.789904], [38.672732, 94.126702, -4.802138], [38.658127, 94.050166, -4.806433], [38.672732, 93.97363, -4.802138], [38.714327, 93.908746, -4.789904], [38.776574, 93.86539, -4.771596], [38.85, 93.850166, -4.75], [38.85, 91.850166, -4.75]]}]},
			"R_shoulder_shaper_05_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_05_CTLShape", "degree": 1, "form": 0, "points": [[-37.1, 94.350166, -4.75], [-37.19218, 94.369196, -4.775605], [-37.270326, 94.423391, -4.797313], [-37.322544, 94.504496, -4.811818], [-37.340879, 94.600166, -4.816911], [-37.322544, 94.695836, -4.811818], [-37.270326, 94.776941, -4.797313], [-37.19218, 94.831136, -4.775605], [-37.1, 94.850166, -4.75], [-37.00782, 94.831136, -4.724395], [-36.929674, 94.776941, -4.702687], [-36.877456, 94.695836, -4.688182], [-36.859121, 94.600166, -4.683089], [-36.877456, 94.504496, -4.688182], [-36.929674, 94.423391, -4.702687], [-37.00782, 94.369196, -4.724395], [-37.1, 94.350166, -4.75], [-37.1, 91.850166, -4.75]]}]},
			"L_upLeg_shaper_04_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_04_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[15.0, 30.942646, 1.666667], [15.07612, 30.486976, 1.723625], [15.2929, 30.100678, 1.771913], [15.61732, 29.842551, 1.804179], [16.0, 29.751912, 1.815508], [16.38268, 29.842551, 1.804179], [16.7071, 30.100678, 1.771913], [16.92388, 30.486976, 1.723625], [17.0, 30.942646, 1.666667], [16.92388, 31.398316, 1.609708], [16.7071, 31.784613, 1.561421], [16.38268, 32.04274, 1.529155], [16.0, 32.133379, 1.517825], [15.61732, 32.04274, 1.529155], [15.2929, 31.784613, 1.561421], [15.07612, 31.398316, 1.609708], [15.0, 30.942646, 1.666667], [5.0, 30.942646, 1.666667]]}]},
			"L_shoulder_shaper_03_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_03_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[29.0, 93.600166, -2.5], [29.064526, 93.613487, -2.517924], [29.119228, 93.651424, -2.533119], [29.155781, 93.708197, -2.543272], [29.168616, 93.775166, -2.546838], [29.155781, 93.842135, -2.543272], [29.119228, 93.898909, -2.533119], [29.064526, 93.936845, -2.517924], [29.0, 93.950166, -2.5], [28.935474, 93.936845, -2.482076], [28.880772, 93.898909, -2.466881], [28.844219, 93.842135, -2.456728], [28.831384, 93.775166, -2.453162], [28.844219, 93.708197, -2.456728], [28.880772, 93.651424, -2.466881], [28.935474, 93.613487, -2.482076], [29.0, 93.600166, -2.5], [29.0, 91.850166, -2.5]]}]},
			"L_loLeg_shaper_05_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_05_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.25, 6.359312, 0.416667], [16.335635, 5.846152, 0.356997], [16.579512, 5.411116, 0.306411], [16.944485, 5.120422, 0.27261], [17.375, 5.018347, 0.260741], [17.805515, 5.120422, 0.27261], [18.170488, 5.411116, 0.306411], [18.414365, 5.846152, 0.356997], [18.5, 6.359312, 0.416667], [18.414365, 6.872473, 0.476336], [18.170488, 7.307509, 0.526922], [17.805515, 7.598203, 0.560724], [17.375, 7.700277, 0.572593], [16.944485, 7.598203, 0.560724], [16.579512, 7.307509, 0.526922], [16.335635, 6.872473, 0.476336], [16.25, 6.359312, 0.416667], [5.0, 6.359312, 0.416667]]}]},
			"L_handIk_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_handIk_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[55.0, 88.323912, -3.526254], [55.0, 91.850166, -4.986873], [55.0, 95.37642, -3.526254], [55.0, 96.837039, 0.0], [55.0, 95.37642, 3.526254], [55.0, 91.850166, 4.986873], [55.0, 88.323912, 3.526254], [55.0, 86.863293, 0.0]]}]},
			"R_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-71.948456, 91.423739, 1.195745], [-71.955627, 91.477519, 1.25], [-71.948456, 91.423739, 1.304255], [-71.941286, 91.36996, 1.25], [-71.948456, 91.423739, 1.195745], [-72.00223, 91.41657, 1.25], [-71.948456, 91.423739, 1.304255], [-71.894677, 91.43091, 1.25], [-71.955627, 91.477519, 1.25], [-72.00223, 91.41657, 1.25], [-71.941286, 91.36996, 1.25], [-71.894677, 91.43091, 1.25], [-71.948456, 91.423739, 1.195745], [-72.00223, 91.41657, 1.25], [-66.875, 92.1002, 1.25]]}, {"shapeName": "R_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.551461, 97.173657, 1.195745], [-67.497682, 97.180827, 1.25], [-67.551461, 97.173657, 1.304255], [-67.60524, 97.166486, 1.25], [-67.551461, 97.173657, 1.195745], [-67.558631, 97.227431, 1.25], [-67.551461, 97.173657, 1.304255], [-67.54429, 97.119878, 1.25], [-67.497682, 97.180827, 1.25], [-67.558631, 97.227431, 1.25], [-67.60524, 97.166486, 1.25], [-67.54429, 97.119878, 1.25], [-67.551461, 97.173657, 1.195745], [-67.558631, 97.227431, 1.25], [-66.875, 92.1002, 1.25]]}, {"shapeName": "R_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-66.882171, 92.153979, 6.368355], [-66.821221, 92.107371, 6.368355], [-66.867829, 92.046421, 6.368355], [-66.928779, 92.09303, 6.368355], [-66.882171, 92.153979, 6.368355], [-66.875, 92.1002, 6.422605], [-66.867829, 92.046421, 6.368355], [-66.875, 92.1002, 6.3141], [-66.821221, 92.107371, 6.368355], [-66.875, 92.1002, 6.422605], [-66.928779, 92.09303, 6.368355], [-66.875, 92.1002, 6.3141], [-66.882171, 92.153979, 6.368355], [-66.875, 92.1002, 6.422605], [-66.875, 92.1002, 1.25]]}]},
			"R_toeTip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_toeTip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.118355, 0.275979, 10.054255], [0.118355, 0.330234, 10.0], [0.118355, 0.275979, 9.945745], [0.118355, 0.221724, 10.0], [0.118355, 0.275979, 10.054255], [0.172605, 0.275979, 10.0], [0.118355, 0.275979, 9.945745], [0.0641, 0.275979, 10.0], [0.118355, 0.330234, 10.0], [0.172605, 0.275979, 10.0], [0.118355, 0.221724, 10.0], [0.0641, 0.275979, 10.0], [0.118355, 0.275979, 10.054255], [0.172605, 0.275979, 10.0], [-5.0, 0.275979, 10.0]]}, {"shapeName": "R_toeTip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.0, 5.394334, 10.054255], [-5.054255, 5.394334, 10.0], [-5.0, 5.394334, 9.945745], [-4.945745, 5.394334, 10.0], [-5.0, 5.394334, 10.054255], [-5.0, 5.448584, 10.0], [-5.0, 5.394334, 9.945745], [-5.0, 5.340079, 10.0], [-5.054255, 5.394334, 10.0], [-5.0, 5.448584, 10.0], [-4.945745, 5.394334, 10.0], [-5.0, 5.340079, 10.0], [-5.0, 5.394334, 10.054255], [-5.0, 5.448584, 10.0], [-5.0, 0.275979, 10.0]]}, {"shapeName": "R_toeTip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-5.0, 0.330234, 4.881645], [-5.054255, 0.275979, 4.881645], [-5.0, 0.221724, 4.881645], [-4.945745, 0.275979, 4.881645], [-5.0, 0.330234, 4.881645], [-5.0, 0.275979, 4.827395], [-5.0, 0.221724, 4.881645], [-5.0, 0.275979, 4.9359], [-5.054255, 0.275979, 4.881645], [-5.0, 0.275979, 4.827395], [-4.945745, 0.275979, 4.881645], [-5.0, 0.275979, 4.9359], [-5.0, 0.330234, 4.881645], [-5.0, 0.275979, 4.827395], [-5.0, 0.275979, 10.0]]}]},
			"C_head_left_CTL": {"color": 6, "shapes": [{"shapeName": "C_head_left_CTLShape", "degree": 1, "form": 0, "points": [[8.75, 113.100166, -3.75], [8.75, 110.600166, -3.75], [8.75, 110.600166, -6.25], [8.75, 113.100166, -6.25], [11.25, 113.100166, -6.25], [11.25, 110.600166, -6.25], [11.25, 110.600166, -3.75], [11.25, 113.100166, -3.75], [8.75, 113.100166, -3.75], [8.75, 113.100166, -6.25], [8.75, 110.600166, -6.25], [11.25, 110.600166, -6.25], [11.25, 113.100166, -6.25], [11.25, 113.100166, -3.75], [11.25, 110.600166, -3.75], [8.75, 110.600166, -3.75]]}]},
			"L_lwrArmTwist_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lwrArmTwist_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[49.768859, 91.921558, -4.238075], [47.939412, 91.921558, -5.545509], [49.550686, 91.921558, -7.244184], [51.552304, 91.921558, -8.473882], [53.797211, 91.921558, -9.149687], [56.139995, 91.921558, -9.237326], [58.423812, 91.921558, -8.7107], [60.486939, 91.921558, -7.633563], [62.185614, 91.921558, -6.022289], [63.415312, 91.921558, -4.020671], [64.091117, 91.921558, -1.775764], [64.178757, 91.921558, 0.56702], [63.652131, 91.921558, 2.850836], [62.574994, 91.921558, 4.913964], [60.96372, 91.921558, 6.612638], [58.962101, 91.921558, 7.842337], [56.717195, 91.921558, 8.518142], [54.374411, 91.921558, 8.605782], [52.090593, 91.921558, 8.079156], [50.027466, 91.921558, 7.002019], [48.646489, 91.921558, 8.934373], [44.947846, 91.921558, 1.903535], [52.773078, 91.921558, 3.160178], [51.3349, 91.921558, 5.172571], [52.880203, 91.921558, 5.983282], [54.587349, 91.921558, 6.374166], [56.351785, 91.921558, 6.322325], [58.037919, 91.921558, 5.799951], [59.537905, 91.921558, 4.885438], [60.745546, 91.921558, 3.60653], [61.556257, 91.921558, 2.061227], [61.947141, 91.921558, 0.354082], [61.8953, 91.921558, -1.410355], [61.372926, 91.921558, -3.096489], [60.458413, 91.921558, -4.596475], [59.179506, 91.921558, -5.804116], [57.634202, 91.921558, -6.614827], [55.927057, 91.921558, -7.005711], [54.16262, 91.921558, -6.95387], [52.476486, 91.921558, -6.431496], [50.9765, 91.921558, -5.516982], [49.768859, 91.921558, -4.238075]]}]},
			"L_shoulder_shaper_01_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_01_CTLShape", "degree": 1, "form": 0, "points": [[20.9, 94.350166, -0.25], [20.99218, 94.369196, -0.275605], [21.070326, 94.423391, -0.297313], [21.122544, 94.504496, -0.311818], [21.140879, 94.600166, -0.316911], [21.122544, 94.695836, -0.311818], [21.070326, 94.776941, -0.297313], [20.99218, 94.831136, -0.275605], [20.9, 94.850166, -0.25], [20.80782, 94.831136, -0.224395], [20.729674, 94.776941, -0.202687], [20.677456, 94.695836, -0.188182], [20.659121, 94.600166, -0.183089], [20.677456, 94.504496, -0.188182], [20.729674, 94.423391, -0.202687], [20.80782, 94.369196, -0.224395], [20.9, 94.350166, -0.25], [20.9, 91.850166, -0.25]]}]},
			"R_bendyLeg_A_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.249999, 34.555057, 3.482625], [-3.799999, 34.555057, 3.482625], [-5.0, 34.694596, 4.598938], [-6.200002, 34.555057, 3.482625], [-5.750002, 34.555057, 3.482625], [-5.750001, 34.369005, 1.99421], [-7.25, 34.369005, 1.99421], [-7.25, 34.424821, 2.440735], [-8.375, 34.275979, 1.25], [-7.25, 34.127137, 0.059265], [-7.25, 34.182953, 0.50579], [-5.750001, 34.182953, 0.50579], [-5.750001, 33.996901, -0.982625], [-6.200001, 33.996901, -0.982625], [-5.0, 33.857362, -2.098938], [-3.799998, 33.996901, -0.982625], [-4.249998, 33.996901, -0.982625], [-4.249998, 34.182953, 0.50579], [-2.75, 34.182953, 0.50579], [-2.75, 34.127137, 0.059265], [-1.625, 34.275979, 1.25], [-2.75, 34.424821, 2.440735], [-2.75, 34.369005, 1.99421], [-4.249998, 34.369005, 1.99421], [-4.249999, 34.555057, 3.482625]]}]},
			"R_loLeg_shaper_01_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_01_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.25, 20.692646, 2.083333], [-16.335635, 20.179485, 2.023664], [-16.579512, 19.744449, 1.973078], [-16.944485, 19.453755, 1.939276], [-17.375, 19.351681, 1.927407], [-17.805515, 19.453755, 1.939276], [-18.170488, 19.744449, 1.973078], [-18.414365, 20.179485, 2.023664], [-18.5, 20.692646, 2.083333], [-18.414365, 21.205806, 2.143003], [-18.170488, 21.640842, 2.193589], [-17.805515, 21.931536, 2.22739], [-17.375, 22.033611, 2.239259], [-16.944485, 21.931536, 2.22739], [-16.579512, 21.640842, 2.193589], [-16.335635, 21.205806, 2.143003], [-16.25, 20.692646, 2.083333], [-5.0, 20.692646, 2.083333]]}]},
			"L_leg_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[7.736573, 3.184991, 0.04756], [7.625151, 3.184991, 0.04756], [7.604049, 3.071422, 0.034354], [7.524872, 3.038836, 0.030565], [7.429098, 3.104321, 0.038179], [7.350309, 3.02606, 0.029079], [7.416232, 2.930937, 0.018018], [7.38344, 2.852279, 0.008872], [7.269095, 2.831319, 0.006435], [7.269095, 2.720639, -0.006435], [7.38344, 2.699679, -0.008872], [7.416232, 2.621032, -0.018017], [7.350309, 2.525899, -0.029079], [7.429098, 2.447637, -0.038179], [7.524872, 2.513122, -0.030565], [7.604049, 2.480536, -0.034354], [7.625151, 2.366967, -0.04756], [7.736573, 2.366967, -0.04756], [7.757685, 2.480536, -0.034354], [7.836862, 2.513122, -0.030565], [7.932636, 2.447637, -0.038179], [8.011418, 2.525899, -0.029079], [7.945502, 2.621032, -0.018017], [7.978293, 2.699679, -0.008872], [8.092628, 2.720639, -0.006435], [8.092628, 2.831319, 0.006435], [7.978293, 2.852279, 0.008872], [7.945502, 2.930937, 0.018018], [8.011418, 3.02606, 0.029079], [7.932636, 3.104321, 0.038179], [7.836862, 3.038836, 0.030565], [7.757685, 3.071422, 0.034354], [7.736573, 3.184991, 0.04756]]}, {"shapeName": "L_leg_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[7.801806, 2.896116, 0.013969], [7.851905, 2.775979, 0.0], [7.801806, 2.655842, -0.013969], [7.680863, 2.606089, -0.019755], [7.559928, 2.655842, -0.013969], [7.509829, 2.775979, 0.0], [7.559928, 2.896116, 0.013969], [7.680863, 2.945869, 0.019755]]}, {"shapeName": "L_leg_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[7.269095, 2.775979, 0.0], [5.0, 2.775979, 0.0]]}]},
			"R_elbowRibbon_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_elbowRibbon_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-38.030209, 93.183502, -8.999886], [-38.030209, 93.983502, -8.999886], [-38.045313, 91.850166, -10.999829], [-38.030209, 89.71683, -8.999886], [-38.030209, 90.51683, -8.999886], [-38.01007, 90.51683, -6.333298], [-38.01007, 87.850166, -6.333298], [-38.016111, 87.850166, -7.133275], [-38.0, 85.850166, -5.0], [-37.983889, 87.850166, -2.866725], [-37.98993, 87.850166, -3.666702], [-37.98993, 90.51683, -3.666702], [-37.969791, 90.51683, -1.000114], [-37.969791, 89.71683, -1.000114], [-37.954687, 91.850166, 0.999829], [-37.969791, 93.983502, -1.000114], [-37.969791, 93.183502, -1.000114], [-37.98993, 93.183502, -3.666702], [-37.98993, 95.850166, -3.666702], [-37.983889, 95.850166, -2.866725], [-38.0, 97.850166, -5.0], [-38.016111, 95.850166, -7.133275], [-38.01007, 95.850166, -6.333298], [-38.01007, 93.183502, -6.333298], [-38.030209, 93.183502, -8.999886]]}]},
			"R_handIk_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_handIk_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-55.0, 89.49933, -2.350836], [-55.0, 91.850166, -3.324582], [-55.0, 94.201002, -2.350836], [-55.0, 95.174748, 0.0], [-55.0, 94.201002, 2.350836], [-55.0, 91.850166, 3.324582], [-55.0, 89.49933, 2.350836], [-55.0, 88.525584, -0.0]]}]},
			"L_shoulder_shaper_01_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_01_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[20.9, 93.600166, -0.25], [20.964526, 93.613487, -0.267924], [21.019228, 93.651424, -0.283119], [21.055781, 93.708197, -0.293272], [21.068616, 93.775166, -0.296838], [21.055781, 93.842135, -0.293272], [21.019228, 93.898909, -0.283119], [20.964526, 93.936845, -0.267924], [20.9, 93.950166, -0.25], [20.835474, 93.936845, -0.232076], [20.780772, 93.898909, -0.216881], [20.744219, 93.842135, -0.206728], [20.731384, 93.775166, -0.203162], [20.744219, 93.708197, -0.206728], [20.780772, 93.651424, -0.216881], [20.835474, 93.613487, -0.232076], [20.9, 93.600166, -0.25], [20.9, 91.850166, -0.25]]}]},
			"L_scapulaTarget_CTL": {"color": 17, "shapes": [{"shapeName": "L_scapulaTarget_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 91.850166, -13.5], [-1.5, 91.850166, -15.0], [0.0, 90.350166, -15.0], [0.0, 91.850166, -13.5], [0.0, 93.350166, -15.0], [-1.5, 91.850166, -15.0], [0.0, 91.850166, -16.5], [0.0, 93.350166, -15.0], [1.5, 91.850166, -15.0], [0.0, 91.850166, -13.5], [0.0, 90.350166, -15.0], [0.0, 91.850166, -16.5], [1.5, 91.850166, -15.0], [0.0, 90.350166, -15.0]]}]},
			"L_elbow_shaper_01_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_01_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[38.85, 94.100166, -4.75], [38.932604, 94.117293, -4.725705], [39.002633, 94.166069, -4.705108], [39.049426, 94.239063, -4.691345], [39.065857, 94.325166, -4.686513], [39.049426, 94.411269, -4.691345], [39.002633, 94.484264, -4.705108], [38.932604, 94.533039, -4.725705], [38.85, 94.550166, -4.75], [38.767396, 94.533039, -4.774295], [38.697367, 94.484264, -4.794892], [38.650574, 94.411269, -4.808655], [38.634143, 94.325166, -4.813487], [38.650574, 94.239063, -4.808655], [38.697367, 94.166069, -4.794892], [38.767396, 94.117293, -4.774295], [38.85, 94.100166, -4.75], [38.85, 91.850166, -4.75]]}]},
			"L_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_B_CTLShape", "degree": 1, "form": 0, "points": [[62.722382, 91.700647, 4.783093], [61.423344, 91.700647, 4.033093], [61.798344, 92.999685, 3.383574], [63.097382, 92.999685, 4.133574], [63.746901, 92.249685, 3.008574], [62.447863, 92.249685, 2.258574], [62.072863, 90.950647, 2.908093], [63.371901, 90.950647, 3.658093], [62.722382, 91.700647, 4.783093], [63.097382, 92.999685, 4.133574], [61.798344, 92.999685, 3.383574], [62.447863, 92.249685, 2.258574], [63.746901, 92.249685, 3.008574], [63.371901, 90.950647, 3.658093], [62.072863, 90.950647, 2.908093], [61.423344, 91.700647, 4.033093]]}]},
			"R_lwrArmTwist_CTL": {"color": 13, "shapes": [{"shapeName": "R_lwrArmTwist_CTLShape", "degree": 1, "form": 0, "points": [[-54.920676, 86.037787, -4.708972], [-54.920676, 84.005068, -6.161677], [-54.920676, 85.795373, -8.049093], [-54.920676, 88.019393, -9.415424], [-54.920676, 90.513734, -10.166319], [-54.920676, 93.116827, -10.263696], [-54.920676, 95.654401, -9.678556], [-54.920676, 97.946765, -8.481737], [-54.920676, 99.834181, -6.691432], [-54.920676, 101.200513, -4.467412], [-54.920676, 101.951407, -1.973071], [-54.920676, 102.048785, 0.630022], [-54.920676, 101.463645, 3.167596], [-54.920676, 100.266826, 5.45996], [-54.920676, 98.476521, 7.347376], [-54.920676, 96.2525, 8.713708], [-54.920676, 93.75816, 9.464602], [-54.920676, 91.155067, 9.56198], [-54.920676, 88.617492, 8.97684], [-54.920676, 86.325128, 7.780021], [-54.920676, 84.790709, 9.927081], [-54.920676, 80.681106, 2.115039], [-54.920676, 89.375808, 3.511309], [-54.920676, 87.777833, 5.747301], [-54.920676, 89.494836, 6.648091], [-54.920676, 91.391665, 7.082407], [-54.920676, 93.352149, 7.024805], [-54.920676, 95.225632, 6.44439], [-54.920676, 96.892283, 5.428264], [-54.920676, 98.234106, 4.007256], [-54.920676, 99.134896, 2.290252], [-54.920676, 99.569212, 0.393424], [-54.920676, 99.51161, -1.567061], [-54.920676, 98.931195, -3.440543], [-54.920676, 97.915069, -5.107195], [-54.920676, 96.494061, -6.449018], [-54.920676, 94.777057, -7.349808], [-54.920676, 92.880229, -7.784123], [-54.920676, 90.919744, -7.726522], [-54.920676, 89.046262, -7.146107], [-54.920676, 87.37961, -6.12998], [-54.920676, 86.037787, -4.708972]]}]},
			"R_bendyLeg_C_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_C_CTLShape", "degree": 1, "form": 0, "points": [[-4.166665, 13.237227, 3.733268], [-3.666665, 13.237227, 3.733268], [-5.0, 13.092851, 4.974903], [-6.333335, 13.237227, 3.733268], [-5.833335, 13.237227, 3.733268], [-5.833335, 13.429728, 2.077758], [-7.5, 13.429728, 2.077758], [-7.5, 13.371978, 2.574411], [-8.75, 13.525979, 1.25], [-7.5, 13.67998, -0.074411], [-7.5, 13.62223, 0.422242], [-5.833335, 13.62223, 0.422242], [-5.833335, 13.814731, -1.233268], [-6.333335, 13.814731, -1.233268], [-5.0, 13.959107, -2.474903], [-3.666665, 13.814731, -1.233268], [-4.166665, 13.814731, -1.233268], [-4.166665, 13.62223, 0.422242], [-2.5, 13.62223, 0.422242], [-2.5, 13.67998, -0.074411], [-1.25, 13.525979, 1.25], [-2.5, 13.371978, 2.574411], [-2.5, 13.429728, 2.077758], [-4.166665, 13.429728, 2.077758], [-4.166665, 13.237227, 3.733268]]}]},
			"R_lwrArmTwist_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_lwrArmTwist_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-50.931335, 91.905693, -3.29628], [-49.508431, 91.905693, -4.313174], [-50.761645, 91.905693, -5.634365], [-52.318459, 91.905693, -6.590797], [-54.064498, 91.905693, -7.116423], [-55.886663, 91.905693, -7.184587], [-57.662965, 91.905693, -6.774989], [-59.267619, 91.905693, -5.937216], [-60.588811, 91.905693, -4.684002], [-61.545243, 91.905693, -3.127188], [-62.070869, 91.905693, -1.38115], [-62.139033, 91.905693, 0.441015], [-61.729435, 91.905693, 2.217317], [-60.891662, 91.905693, 3.821972], [-59.638449, 91.905693, 5.143163], [-58.081634, 91.905693, 6.099596], [-56.335596, 91.905693, 6.625221], [-54.513431, 91.905693, 6.693386], [-52.737128, 91.905693, 6.283788], [-51.132473, 91.905693, 5.446015], [-50.05838, 91.905693, 6.948957], [-47.181658, 91.905693, 1.480527], [-53.267949, 91.905693, 2.457916], [-52.149367, 91.905693, 4.023111], [-53.351269, 91.905693, 4.653664], [-54.679049, 91.905693, 4.957685], [-56.051388, 91.905693, 4.917364], [-57.362826, 91.905693, 4.511073], [-58.529482, 91.905693, 3.799785], [-59.468758, 91.905693, 2.805079], [-60.099311, 91.905693, 1.603176], [-60.403332, 91.905693, 0.275397], [-60.363011, 91.905693, -1.096943], [-59.95672, 91.905693, -2.40838], [-59.245432, 91.905693, -3.575036], [-58.250727, 91.905693, -4.514313], [-57.048824, 91.905693, -5.144866], [-55.721044, 91.905693, -5.448886], [-54.348705, 91.905693, -5.408565], [-53.037267, 91.905693, -5.002275], [-51.870611, 91.905693, -4.290986], [-50.931335, 91.905693, -3.29628]]}]},
			"L_uprArmRibbonMid_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_uprArmRibbonMid_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[28.063246, 93.016835, -5.872313], [28.063246, 93.716835, -5.872313], [27.59487, 91.850166, -7.558469], [28.063246, 89.983497, -5.872313], [28.063246, 90.683497, -5.872313], [28.687748, 90.683497, -3.624106], [28.687748, 88.350166, -3.624106], [28.500397, 88.350166, -4.298569], [29.0, 86.600166, -2.5], [29.499603, 88.350166, -0.701431], [29.312252, 88.350166, -1.375894], [29.312252, 90.683497, -1.375894], [29.936754, 90.683497, 0.872313], [29.936754, 89.983497, 0.872313], [30.40513, 91.850166, 2.558469], [29.936754, 93.716835, 0.872313], [29.936754, 93.016835, 0.872313], [29.312252, 93.016835, -1.375894], [29.312252, 95.350166, -1.375894], [29.499603, 95.350166, -0.701431], [29.0, 97.100166, -2.5], [28.500397, 95.350166, -4.298569], [28.687748, 95.350166, -3.624106], [28.687748, 93.016835, -3.624106], [28.063246, 93.016835, -5.872313]]}]},
			"R_leg_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-8.518451, 3.301852, 0.061148], [-8.375193, 3.301852, 0.061148], [-8.348063, 3.155834, 0.044169], [-8.246264, 3.113938, 0.039298], [-8.123126, 3.198133, 0.049088], [-8.021826, 3.097511, 0.037387], [-8.106584, 2.975211, 0.023166], [-8.064424, 2.87408, 0.011407], [-7.917409, 2.847131, 0.008273], [-7.917409, 2.704827, -0.008273], [-8.064424, 2.677879, -0.011407], [-8.106584, 2.576761, -0.023165], [-8.021826, 2.454447, -0.037387], [-8.123126, 2.353825, -0.049088], [-8.246264, 2.43802, -0.039298], [-8.348063, 2.396124, -0.044169], [-8.375193, 2.250106, -0.061148], [-8.518451, 2.250106, -0.061148], [-8.545595, 2.396124, -0.044169], [-8.647394, 2.43802, -0.039298], [-8.770532, 2.353825, -0.049088], [-8.871823, 2.454447, -0.037387], [-8.787074, 2.576761, -0.023165], [-8.829235, 2.677879, -0.011407], [-8.976236, 2.704827, -0.008273], [-8.976236, 2.847131, 0.008273], [-8.829235, 2.87408, 0.011407], [-8.787074, 2.975211, 0.023166], [-8.871823, 3.097511, 0.037387], [-8.770532, 3.198133, 0.049088], [-8.647394, 3.113938, 0.039298], [-8.545595, 3.155834, 0.044169], [-8.518451, 3.301852, 0.061148]]}, {"shapeName": "R_leg_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-8.602322, 2.93044, 0.017961], [-8.666735, 2.775979, -0.0], [-8.602322, 2.621518, -0.017961], [-8.446824, 2.557549, -0.025399], [-8.291336, 2.621518, -0.017961], [-8.226923, 2.775979, -0.0], [-8.291336, 2.93044, 0.017961], [-8.446824, 2.994409, 0.025399]]}, {"shapeName": "R_leg_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-7.917409, 2.775979, -0.0], [-5.0, 2.775979, -0.0]]}]},
			"L_bendyLeg_B_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.499999, 24.282426, 3.999986], [4.199999, 24.282426, 3.999986], [5.0, 24.285649, 4.749979], [5.800001, 24.282426, 3.999986], [5.500001, 24.282426, 3.999986], [5.500001, 24.278128, 2.999996], [6.5, 24.278128, 2.999996], [6.5, 24.279417, 3.299994], [7.25, 24.275979, 2.5], [6.5, 24.272541, 1.700006], [6.5, 24.27383, 2.000004], [5.500001, 24.27383, 2.000004], [5.500001, 24.269532, 1.000014], [5.800001, 24.269532, 1.000014], [5.0, 24.266309, 0.250021], [4.199999, 24.269532, 1.000014], [4.499999, 24.269532, 1.000014], [4.499999, 24.27383, 2.000004], [3.5, 24.27383, 2.000004], [3.5, 24.272541, 1.700006], [2.75, 24.275979, 2.5], [3.5, 24.279417, 3.299994], [3.5, 24.278128, 2.999996], [4.499999, 24.278128, 2.999996], [4.499999, 24.282426, 3.999986]]}]},
			"L_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_A_CTLShape", "degree": 1, "form": 0, "points": [[61.239142, 91.627126, 3.779701], [60.050826, 91.515871, 2.871116], [60.425826, 92.814909, 2.221597], [61.614142, 92.926164, 3.130182], [62.449174, 92.184462, 2.128884], [61.260858, 92.073207, 1.220299], [60.885858, 90.774168, 1.869818], [62.074174, 90.885424, 2.778403], [61.239142, 91.627126, 3.779701], [61.614142, 92.926164, 3.130182], [60.425826, 92.814909, 2.221597], [61.260858, 92.073207, 1.220299], [62.449174, 92.184462, 2.128884], [62.074174, 90.885424, 2.778403], [60.885858, 90.774168, 1.869818], [60.050826, 91.515871, 2.871116]]}]},
			"L_shoulder_shaper_03_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_03_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[29.0, 94.100166, -2.5], [29.082962, 94.117293, -2.523045], [29.153293, 94.166069, -2.542581], [29.200289, 94.239063, -2.555636], [29.216792, 94.325166, -2.56022], [29.200289, 94.411269, -2.555636], [29.153293, 94.484264, -2.542581], [29.082962, 94.533039, -2.523045], [29.0, 94.550166, -2.5], [28.917038, 94.533039, -2.476955], [28.846707, 94.484264, -2.457419], [28.799711, 94.411269, -2.444364], [28.783208, 94.325166, -2.43978], [28.799711, 94.239063, -2.444364], [28.846707, 94.166069, -2.457419], [28.917038, 94.117293, -2.476955], [29.0, 94.100166, -2.5], [29.0, 91.850166, -2.5]]}]},
			"L_reverseBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_reverseBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.118355, 0.275979, 4.945745], [10.118355, 0.330234, 5.0], [10.118355, 0.275979, 5.054255], [10.118355, 0.221724, 5.0], [10.118355, 0.275979, 4.945745], [10.172605, 0.275979, 5.0], [10.118355, 0.275979, 5.054255], [10.0641, 0.275979, 5.0], [10.118355, 0.330234, 5.0], [10.172605, 0.275979, 5.0], [10.118355, 0.221724, 5.0], [10.0641, 0.275979, 5.0], [10.118355, 0.275979, 4.945745], [10.172605, 0.275979, 5.0], [5.0, 0.275979, 5.0]]}, {"shapeName": "L_reverseBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[5.0, 5.394334, 4.945745], [4.945745, 5.394334, 5.0], [5.0, 5.394334, 5.054255], [5.054255, 5.394334, 5.0], [5.0, 5.394334, 4.945745], [5.0, 5.448584, 5.0], [5.0, 5.394334, 5.054255], [5.0, 5.340079, 5.0], [4.945745, 5.394334, 5.0], [5.0, 5.448584, 5.0], [5.054255, 5.394334, 5.0], [5.0, 5.340079, 5.0], [5.0, 5.394334, 4.945745], [5.0, 5.448584, 5.0], [5.0, 0.275979, 5.0]]}, {"shapeName": "L_reverseBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[5.0, 0.330234, 10.118355], [4.945745, 0.275979, 10.118355], [5.0, 0.221724, 10.118355], [5.054255, 0.275979, 10.118355], [5.0, 0.330234, 10.118355], [5.0, 0.275979, 10.172605], [5.0, 0.221724, 10.118355], [5.0, 0.275979, 10.0641], [4.945745, 0.275979, 10.118355], [5.0, 0.275979, 10.172605], [5.054255, 0.275979, 10.118355], [5.0, 0.275979, 10.0641], [5.0, 0.330234, 10.118355], [5.0, 0.275979, 10.172605], [5.0, 0.275979, 5.0]]}]},
			"R_elbow_shaper_05_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_elbow_shaper_05_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-55.135136, 91.850166, 0.028435], [-55.132075, 91.861017, 0.038845], [-55.129013, 91.850166, 0.049256], [-55.132075, 91.839315, 0.038845], [-55.135136, 91.850166, 0.028435], [-55.142484, 91.850166, 0.041907], [-55.129013, 91.850166, 0.049256], [-55.121665, 91.850166, 0.035784], [-55.132075, 91.861017, 0.038845], [-55.142484, 91.850166, 0.041907], [-55.132075, 91.839315, 0.038845], [-55.121665, 91.850166, 0.035784], [-55.135136, 91.850166, 0.028435], [-55.142484, 91.850166, 0.041907], [-54.15, 91.850166, -0.25]]}, {"shapeName": "R_elbow_shaper_05_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-54.153062, 92.873837, -0.26041], [-54.13959, 92.873837, -0.253062], [-54.146938, 92.873837, -0.23959], [-54.16041, 92.873837, -0.246938], [-54.153062, 92.873837, -0.26041], [-54.15, 92.884687, -0.25], [-54.146938, 92.873837, -0.23959], [-54.15, 92.862986, -0.25], [-54.13959, 92.873837, -0.253062], [-54.15, 92.884687, -0.25], [-54.16041, 92.873837, -0.246938], [-54.15, 92.862986, -0.25], [-54.153062, 92.873837, -0.26041], [-54.15, 92.884687, -0.25], [-54.15, 91.850166, -0.25]]}, {"shapeName": "R_elbow_shaper_05_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-53.861155, 91.861017, 0.732075], [-53.850744, 91.850166, 0.729013], [-53.861155, 91.839315, 0.732075], [-53.871565, 91.850166, 0.735136], [-53.861155, 91.861017, 0.732075], [-53.858093, 91.850166, 0.742484], [-53.861155, 91.839315, 0.732075], [-53.864216, 91.850166, 0.721665], [-53.850744, 91.850166, 0.729013], [-53.858093, 91.850166, 0.742484], [-53.871565, 91.850166, 0.735136], [-53.864216, 91.850166, 0.721665], [-53.861155, 91.861017, 0.732075], [-53.858093, 91.850166, 0.742484], [-54.15, 91.850166, -0.25]]}]},
			"R_lwrArmTwist_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_lwrArmTwist_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-51.512573, 91.897761, -2.825383], [-50.292941, 91.897761, -3.697006], [-51.367124, 91.897761, -4.829456], [-52.701536, 91.897761, -5.649254], [-54.198141, 91.897761, -6.099791], [-55.759997, 91.897761, -6.158218], [-57.282541, 91.897761, -5.807134], [-58.657959, 91.897761, -5.089042], [-59.790409, 91.897761, -4.014859], [-60.610208, 91.897761, -2.680447], [-61.060745, 91.897761, -1.183843], [-61.119171, 91.897761, 0.378013], [-60.768087, 91.897761, 1.900558], [-60.049996, 91.897761, 3.275976], [-58.975813, 91.897761, 4.408426], [-57.6414, 91.897761, 5.228225], [-56.144796, 91.897761, 5.678761], [-54.582941, 91.897761, 5.737188], [-53.060396, 91.897761, 5.386104], [-51.684977, 91.897761, 4.668013], [-50.764326, 91.897761, 5.956249], [-48.298564, 91.897761, 1.269023], [-53.515385, 91.897761, 2.106785], [-52.5566, 91.897761, 3.448381], [-53.586802, 91.897761, 3.988855], [-54.724899, 91.897761, 4.249444], [-55.90119, 91.897761, 4.214883], [-57.02528, 91.897761, 3.866634], [-58.02527, 91.897761, 3.256958], [-58.830364, 91.897761, 2.404354], [-59.370838, 91.897761, 1.374151], [-59.631428, 91.897761, 0.236054], [-59.596866, 91.897761, -0.940237], [-59.248617, 91.897761, -2.064326], [-58.638942, 91.897761, -3.064317], [-57.786337, 91.897761, -3.869411], [-56.756135, 91.897761, -4.409885], [-55.618038, 91.897761, -4.670474], [-54.441747, 91.897761, -4.635913], [-53.317658, 91.897761, -4.287664], [-52.317666, 91.897761, -3.677988], [-51.512573, 91.897761, -2.825383]]}]},
			"C_midSpine_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midSpine_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.347257, 64.350166, -5.289381], [0.0, 64.350166, -7.480309], [-6.347257, 64.350166, -5.289381], [-8.976371, 64.350166, 0.0], [-6.347257, 64.350166, 5.289381], [0.0, 64.350166, 7.480309], [6.347257, 64.350166, 5.289381], [8.976371, 64.350166, 0.0]]}]},
			"L_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.323456, 92.526627, -0.054255], [66.316286, 92.580406, 0.0], [66.323456, 92.526627, 0.054255], [66.330627, 92.472848, 0.0], [66.323456, 92.526627, -0.054255], [66.37723, 92.533797, 0.0], [66.323456, 92.526627, 0.054255], [66.269677, 92.519457, 0.0], [66.316286, 92.580406, 0.0], [66.37723, 92.533797, 0.0], [66.330627, 92.472848, 0.0], [66.269677, 92.519457, 0.0], [66.323456, 92.526627, -0.054255], [66.37723, 92.533797, 0.0], [61.25, 91.850166, 0.0]]}, {"shapeName": "L_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[60.573539, 96.923623, -0.054255], [60.51976, 96.916452, 0.0], [60.573539, 96.923623, 0.054255], [60.627318, 96.930793, 0.0], [60.573539, 96.923623, -0.054255], [60.566369, 96.977397, 0.0], [60.573539, 96.923623, 0.054255], [60.58071, 96.869844, 0.0], [60.51976, 96.916452, 0.0], [60.566369, 96.977397, 0.0], [60.627318, 96.930793, 0.0], [60.58071, 96.869844, 0.0], [60.573539, 96.923623, -0.054255], [60.566369, 96.977397, 0.0], [61.25, 91.850166, 0.0]]}, {"shapeName": "L_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.242829, 91.903945, 5.118355], [61.196221, 91.842996, 5.118355], [61.257171, 91.796387, 5.118355], [61.303779, 91.857337, 5.118355], [61.242829, 91.903945, 5.118355], [61.25, 91.850166, 5.172605], [61.257171, 91.796387, 5.118355], [61.25, 91.850166, 5.0641], [61.196221, 91.842996, 5.118355], [61.25, 91.850166, 5.172605], [61.303779, 91.857337, 5.118355], [61.25, 91.850166, 5.0641], [61.242829, 91.903945, 5.118355], [61.25, 91.850166, 5.172605], [61.25, 91.850166, 0.0]]}]},
			"R_elbow_shaper_03_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_03_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-46.5, 94.100166, -2.5], [-46.582604, 94.117293, -2.475705], [-46.652633, 94.166069, -2.455108], [-46.699426, 94.239063, -2.441345], [-46.715857, 94.325166, -2.436513], [-46.699426, 94.411269, -2.441345], [-46.652633, 94.484264, -2.455108], [-46.582604, 94.533039, -2.475705], [-46.5, 94.550166, -2.5], [-46.417396, 94.533039, -2.524295], [-46.347367, 94.484264, -2.544892], [-46.300574, 94.411269, -2.558655], [-46.284143, 94.325166, -2.563487], [-46.300574, 94.239063, -2.558655], [-46.347367, 94.166069, -2.544892], [-46.417396, 94.117293, -2.524295], [-46.5, 94.100166, -2.5], [-46.5, 91.850166, -2.5]]}]},
			"R_heel_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_heel_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.118355, 0.275979, -1.195745], [0.118355, 0.330234, -1.25], [0.118355, 0.275979, -1.304255], [0.118355, 0.221724, -1.25], [0.118355, 0.275979, -1.195745], [0.172605, 0.275979, -1.25], [0.118355, 0.275979, -1.304255], [0.0641, 0.275979, -1.25], [0.118355, 0.330234, -1.25], [0.172605, 0.275979, -1.25], [0.118355, 0.221724, -1.25], [0.0641, 0.275979, -1.25], [0.118355, 0.275979, -1.195745], [0.172605, 0.275979, -1.25], [-5.0, 0.275979, -1.25]]}, {"shapeName": "R_heel_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.0, 5.394334, -1.195745], [-5.054255, 5.394334, -1.25], [-5.0, 5.394334, -1.304255], [-4.945745, 5.394334, -1.25], [-5.0, 5.394334, -1.195745], [-5.0, 5.448584, -1.25], [-5.0, 5.394334, -1.304255], [-5.0, 5.340079, -1.25], [-5.054255, 5.394334, -1.25], [-5.0, 5.448584, -1.25], [-4.945745, 5.394334, -1.25], [-5.0, 5.340079, -1.25], [-5.0, 5.394334, -1.195745], [-5.0, 5.448584, -1.25], [-5.0, 0.275979, -1.25]]}, {"shapeName": "R_heel_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-5.0, 0.330234, -6.368355], [-5.054255, 0.275979, -6.368355], [-5.0, 0.221724, -6.368355], [-4.945745, 0.275979, -6.368355], [-5.0, 0.330234, -6.368355], [-5.0, 0.275979, -6.422605], [-5.0, 0.221724, -6.368355], [-5.0, 0.275979, -6.3141], [-5.054255, 0.275979, -6.368355], [-5.0, 0.275979, -6.422605], [-4.945745, 0.275979, -6.368355], [-5.0, 0.275979, -6.3141], [-5.0, 0.330234, -6.368355], [-5.0, 0.275979, -6.422605], [-5.0, 0.275979, -1.25]]}]},
			"R_loLeg_shaper_04_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_04_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-12.5, 9.942646, 0.833333], [-12.55709, 9.600539, 0.793553], [-12.719675, 9.310515, 0.75983], [-12.96299, 9.116719, 0.737295], [-13.25, 9.048669, 0.729383], [-13.53701, 9.116719, 0.737295], [-13.780325, 9.310515, 0.75983], [-13.94291, 9.600539, 0.793553], [-14.0, 9.942646, 0.833333], [-13.94291, 10.284753, 0.873113], [-13.780325, 10.574777, 0.906837], [-13.53701, 10.768573, 0.929371], [-13.25, 10.836622, 0.937284], [-12.96299, 10.768573, 0.929371], [-12.719675, 10.574777, 0.906837], [-12.55709, 10.284753, 0.873113], [-12.5, 9.942646, 0.833333], [-5.0, 9.942646, 0.833333]]}]},
			"R_toe_IK_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-6.371321, 1.6473, 5.0], [-5.0, 2.215319, 5.0], [-3.628679, 1.6473, 5.0], [-3.060661, 0.275979, 5.0], [-3.628679, -1.095342, 5.0], [-5.0, -1.66336, 5.0], [-6.371321, -1.095342, 5.0], [-6.939339, 0.275979, 5.0]]}]},
			"L_legEnd_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_legEnd_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, -2.314387, -0.537283], [4.945745, -2.308121, -0.591174], [5.0, -2.301854, -0.645066], [5.054255, -2.308121, -0.591174], [5.0, -2.314387, -0.537283], [5.0, -2.362008, -0.59744], [5.0, -2.301854, -0.645066], [5.0, -2.254229, -0.584908], [4.945745, -2.308121, -0.591174], [5.0, -2.362008, -0.59744], [5.054255, -2.308121, -0.591174], [5.0, -2.254229, -0.584908], [5.0, -2.314387, -0.537283], [5.0, -2.362008, -0.59744], [5.0, 2.775979, 0.0]]}, {"shapeName": "L_legEnd_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 2.769713, 0.053892], [-0.118355, 2.829871, 0.006266], [-0.118355, 2.782246, -0.053892], [-0.118355, 2.722087, -0.006266], [-0.118355, 2.769713, 0.053892], [-0.172605, 2.775979, 0.0], [-0.118355, 2.782246, -0.053892], [-0.0641, 2.775979, 0.0], [-0.118355, 2.829871, 0.006266], [-0.172605, 2.775979, 0.0], [-0.118355, 2.722087, -0.006266], [-0.0641, 2.775979, 0.0], [-0.118355, 2.769713, 0.053892], [-0.172605, 2.775979, 0.0], [5.0, 2.775979, 0.0]]}, {"shapeName": "L_legEnd_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 3.367153, -5.0841], [5.0, 3.421045, -5.077833], [5.054255, 3.367153, -5.0841], [5.0, 3.313262, -5.090366], [4.945745, 3.367153, -5.0841], [5.0, 3.373419, -5.137987], [5.054255, 3.367153, -5.0841], [5.0, 3.360887, -5.030208], [5.0, 3.421045, -5.077833], [5.0, 3.373419, -5.137987], [5.0, 3.313262, -5.090366], [5.0, 3.360887, -5.030208], [4.945745, 3.367153, -5.0841], [5.0, 3.373419, -5.137987], [5.0, 2.775979, 0.0]]}]},
			"R_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_B_CTLShape", "degree": 1, "form": 0, "points": [[-63.812803, 92.907587, 0.75], [-62.31758, 92.787969, 0.75], [-62.31758, 92.787969, -0.75], [-63.812803, 92.907587, -0.75], [-63.93242, 91.412364, -0.75], [-62.437197, 91.292746, -0.75], [-62.437197, 91.292746, 0.75], [-63.93242, 91.412364, 0.75], [-63.812803, 92.907587, 0.75], [-63.812803, 92.907587, -0.75], [-62.31758, 92.787969, -0.75], [-62.437197, 91.292746, -0.75], [-63.93242, 91.412364, -0.75], [-63.93242, 91.412364, 0.75], [-62.437197, 91.292746, 0.75], [-62.31758, 92.787969, 0.75]]}]},
			"L_shoulder_shaper_04_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_04_CTLShape", "degree": 1, "form": 0, "points": [[33.5, 94.350166, -3.75], [33.59218, 94.369196, -3.775605], [33.670326, 94.423391, -3.797313], [33.722544, 94.504496, -3.811818], [33.740879, 94.600166, -3.816911], [33.722544, 94.695836, -3.811818], [33.670326, 94.776941, -3.797313], [33.59218, 94.831136, -3.775605], [33.5, 94.850166, -3.75], [33.40782, 94.831136, -3.724395], [33.329674, 94.776941, -3.702687], [33.277456, 94.695836, -3.688182], [33.259121, 94.600166, -3.683089], [33.277456, 94.504496, -3.688182], [33.329674, 94.423391, -3.702687], [33.40782, 94.369196, -3.724395], [33.5, 94.350166, -3.75], [33.5, 91.850166, -3.75]]}]},
			"L_clavicle_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_clavicle_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [3.399131, 91.850166, -2.481701], [2.022404, 91.850166, -6.497156], [1.496539, 91.850166, -8.030928], [2.022404, 96.84036, -6.497156], [3.399131, 99.924474, -2.481701], [5.100869, 99.924474, 2.481701], [6.477596, 96.84036, 6.497156], [7.003461, 91.850166, 8.030928], [6.477596, 91.850166, 6.497156], [5.100869, 91.850166, 2.481701], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0]]}]},
			"R_shoulder_shaper_04_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_04_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-33.5, 94.100166, -3.75], [-33.582962, 94.117293, -3.773045], [-33.653293, 94.166069, -3.792581], [-33.700289, 94.239063, -3.805636], [-33.716792, 94.325166, -3.81022], [-33.700289, 94.411269, -3.805636], [-33.653293, 94.484264, -3.792581], [-33.582962, 94.533039, -3.773045], [-33.5, 94.550166, -3.75], [-33.417038, 94.533039, -3.726955], [-33.346707, 94.484264, -3.707419], [-33.299711, 94.411269, -3.694364], [-33.283208, 94.325166, -3.68978], [-33.299711, 94.239063, -3.694364], [-33.346707, 94.166069, -3.707419], [-33.417038, 94.117293, -3.726955], [-33.5, 94.100166, -3.75], [-33.5, 91.850166, -3.75]]}]},
			"C_neck_FK_B_CTL": {"color": 4, "shapes": [{"shapeName": "C_neck_FK_B_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 95.1835, 0.0], [-5.03806, 95.37484, 0.0], [-5.14645, 95.53705, 0.0], [-5.30866, 95.64544, 0.0], [-5.5, 95.6835, 0.0], [-5.69134, 95.64544, 0.0], [-5.85355, 95.53705, 0.0], [-5.96194, 95.37484, 0.0], [-6.0, 95.1835, 0.0], [-5.96194, 94.99216, 0.0], [-5.85355, 94.82995, 0.0], [-5.69134, 94.72156, 0.0], [-5.5, 94.6835, 0.0], [-5.30866, 94.72156, 0.0], [-5.14645, 94.82995, 0.0], [-5.03806, 94.99216, 0.0], [-5.0, 95.1835, 0.0], [0.0, 95.1835, 0.0]]}]},
			"R_bendyLeg_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_bendyLeg_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 19.157904, 2.576253], [-4.945745, 19.157671, 2.521998], [-5.0, 19.157438, 2.467744], [-5.054255, 19.157671, 2.521998], [-5.0, 19.157904, 2.576253], [-5.0, 19.103422, 2.522231], [-5.0, 19.157438, 2.467744], [-5.0, 19.211926, 2.521765], [-4.945745, 19.157671, 2.521998], [-5.0, 19.103422, 2.522231], [-5.054255, 19.157671, 2.521998], [-5.0, 19.211926, 2.521765], [-5.0, 19.157904, 2.576253], [-5.0, 19.103422, 2.522231], [-5.0, 24.275979, 2.5]]}, {"shapeName": "R_bendyLeg_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 24.276212, 2.554254], [0.118355, 24.330233, 2.499767], [0.118355, 24.275746, 2.445746], [0.118355, 24.221724, 2.500233], [0.118355, 24.276212, 2.554254], [0.172605, 24.275979, 2.5], [0.118355, 24.275746, 2.445746], [0.0641, 24.275979, 2.5], [0.118355, 24.330233, 2.499767], [0.172605, 24.275979, 2.5], [0.118355, 24.221724, 2.500233], [0.0641, 24.275979, 2.5], [0.118355, 24.276212, 2.554254], [0.172605, 24.275979, 2.5], [-5.0, 24.275979, 2.5]]}, {"shapeName": "R_bendyLeg_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 24.253981, -2.618308], [-5.0, 24.308235, -2.618541], [-5.054255, 24.253981, -2.618308], [-5.0, 24.199726, -2.618075], [-4.945745, 24.253981, -2.618308], [-5.0, 24.253748, -2.672557], [-5.054255, 24.253981, -2.618308], [-5.0, 24.254214, -2.564053], [-5.0, 24.308235, -2.618541], [-5.0, 24.253748, -2.672557], [-5.0, 24.199726, -2.618075], [-5.0, 24.254214, -2.564053], [-4.945745, 24.253981, -2.618308], [-5.0, 24.253748, -2.672557], [-5.0, 24.275979, 2.5]]}]},
			"C_jaw_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_jaw_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.054255, 101.850166, 7.618355], [0.0, 101.904421, 7.618355], [-0.054255, 101.850166, 7.618355], [0.0, 101.795911, 7.618355], [0.054255, 101.850166, 7.618355], [0.0, 101.850166, 7.672605], [-0.054255, 101.850166, 7.618355], [0.0, 101.850166, 7.5641], [0.0, 101.904421, 7.618355], [0.0, 101.850166, 7.672605], [0.0, 101.795911, 7.618355], [0.0, 101.850166, 7.5641], [0.054255, 101.850166, 7.618355], [0.0, 101.850166, 7.672605], [0.0, 101.850166, 2.5]]}, {"shapeName": "C_jaw_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.054255, 106.968521, 2.5], [0.0, 106.968521, 2.445745], [-0.054255, 106.968521, 2.5], [0.0, 106.968521, 2.554255], [0.054255, 106.968521, 2.5], [0.0, 107.022771, 2.5], [-0.054255, 106.968521, 2.5], [0.0, 106.914266, 2.5], [0.0, 106.968521, 2.445745], [0.0, 107.022771, 2.5], [0.0, 106.968521, 2.554255], [0.0, 106.914266, 2.5], [0.054255, 106.968521, 2.5], [0.0, 107.022771, 2.5], [0.0, 101.850166, 2.5]]}, {"shapeName": "C_jaw_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-5.118355, 101.904421, 2.5], [-5.118355, 101.850166, 2.445745], [-5.118355, 101.795911, 2.5], [-5.118355, 101.850166, 2.554255], [-5.118355, 101.904421, 2.5], [-5.172605, 101.850166, 2.5], [-5.118355, 101.795911, 2.5], [-5.0641, 101.850166, 2.5], [-5.118355, 101.850166, 2.445745], [-5.172605, 101.850166, 2.5], [-5.118355, 101.850166, 2.554255], [-5.0641, 101.850166, 2.5], [-5.118355, 101.904421, 2.5], [-5.172605, 101.850166, 2.5], [0.0, 101.850166, 2.5]]}]},
			"R_bendyLeg_C_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.499999, 13.352728, 2.739961], [-4.199999, 13.352728, 2.739961], [-5.0, 13.266102, 3.484942], [-5.800001, 13.352728, 2.739961], [-5.500001, 13.352728, 2.739961], [-5.500001, 13.468228, 1.746655], [-6.5, 13.468228, 1.746655], [-6.5, 13.433578, 2.044647], [-7.25, 13.525979, 1.25], [-6.5, 13.61838, 0.455353], [-6.5, 13.58373, 0.753345], [-5.500001, 13.58373, 0.753345], [-5.500001, 13.69923, -0.239961], [-5.800001, 13.69923, -0.239961], [-5.0, 13.785856, -0.984942], [-4.199999, 13.69923, -0.239961], [-4.499999, 13.69923, -0.239961], [-4.499999, 13.58373, 0.753345], [-3.5, 13.58373, 0.753345], [-3.5, 13.61838, 0.455353], [-2.75, 13.525979, 1.25], [-3.5, 13.433578, 2.044647], [-3.5, 13.468228, 1.746655], [-4.499999, 13.468228, 1.746655], [-4.499999, 13.352728, 2.739961]]}]},
			"R_legEnd_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_legEnd_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, -2.314387, -0.537283], [-4.945745, -2.308121, -0.591174], [-5.0, -2.301854, -0.645066], [-5.054255, -2.308121, -0.591174], [-5.0, -2.314387, -0.537283], [-5.0, -2.362008, -0.59744], [-5.0, -2.301854, -0.645066], [-5.0, -2.254229, -0.584908], [-4.945745, -2.308121, -0.591174], [-5.0, -2.362008, -0.59744], [-5.054255, -2.308121, -0.591174], [-5.0, -2.254229, -0.584908], [-5.0, -2.314387, -0.537283], [-5.0, -2.362008, -0.59744], [-5.0, 2.775979, -0.0]]}, {"shapeName": "R_legEnd_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 2.769713, 0.053892], [0.118355, 2.829871, 0.006266], [0.118355, 2.782246, -0.053892], [0.118355, 2.722087, -0.006266], [0.118355, 2.769713, 0.053892], [0.172605, 2.775979, 0.0], [0.118355, 2.782246, -0.053892], [0.0641, 2.775979, 0.0], [0.118355, 2.829871, 0.006266], [0.172605, 2.775979, 0.0], [0.118355, 2.722087, -0.006266], [0.0641, 2.775979, 0.0], [0.118355, 2.769713, 0.053892], [0.172605, 2.775979, 0.0], [-5.0, 2.775979, -0.0]]}, {"shapeName": "R_legEnd_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 3.367153, -5.0841], [-5.0, 3.421045, -5.077833], [-5.054255, 3.367153, -5.0841], [-5.0, 3.313262, -5.090366], [-4.945745, 3.367153, -5.0841], [-5.0, 3.373419, -5.137987], [-5.054255, 3.367153, -5.0841], [-5.0, 3.360887, -5.030208], [-5.0, 3.421045, -5.077833], [-5.0, 3.373419, -5.137987], [-5.0, 3.313262, -5.090366], [-5.0, 3.360887, -5.030208], [-4.945745, 3.367153, -5.0841], [-5.0, 3.373419, -5.137987], [-5.0, 2.775979, -0.0]]}]},
			"R_upLeg_shaper_03_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_03_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-12.5, 34.275979, 1.25], [-12.55709, 33.934227, 1.292719], [-12.719675, 33.644503, 1.328934], [-12.96299, 33.450908, 1.353134], [-13.25, 33.382929, 1.361631], [-13.53701, 33.450908, 1.353134], [-13.780325, 33.644503, 1.328934], [-13.94291, 33.934227, 1.292719], [-14.0, 34.275979, 1.25], [-13.94291, 34.617731, 1.207281], [-13.780325, 34.907455, 1.171066], [-13.53701, 35.10105, 1.146866], [-13.25, 35.169029, 1.138369], [-12.96299, 35.10105, 1.146866], [-12.719675, 34.907455, 1.171066], [-12.55709, 34.617731, 1.207281], [-12.5, 34.275979, 1.25], [-5.0, 34.275979, 1.25]]}]},
			"C_neck_FK_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 103.635188, -0.054255], [-0.054255, 103.635188, 0.0], [0.0, 103.635188, 0.054255], [0.054255, 103.635188, 0.0], [0.0, 103.635188, -0.054255], [0.0, 103.689438, 0.0], [0.0, 103.635188, 0.054255], [0.0, 103.580933, 0.0], [-0.054255, 103.635188, 0.0], [0.0, 103.689438, 0.0], [0.054255, 103.635188, 0.0], [0.0, 103.580933, 0.0], [0.0, 103.635188, -0.054255], [0.0, 103.689438, 0.0], [0.0, 98.516833, 0.0]]}, {"shapeName": "C_neck_FK_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 98.516833, -0.054255], [-5.118355, 98.462578, 0.0], [-5.118355, 98.516833, 0.054255], [-5.118355, 98.571088, 0.0], [-5.118355, 98.516833, -0.054255], [-5.172605, 98.516833, 0.0], [-5.118355, 98.516833, 0.054255], [-5.0641, 98.516833, 0.0], [-5.118355, 98.462578, 0.0], [-5.172605, 98.516833, 0.0], [-5.118355, 98.571088, 0.0], [-5.0641, 98.516833, 0.0], [-5.118355, 98.516833, -0.054255], [-5.172605, 98.516833, 0.0], [0.0, 98.516833, 0.0]]}, {"shapeName": "C_neck_FK_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 98.516833, 5.118355], [0.0, 98.462578, 5.118355], [0.054255, 98.516833, 5.118355], [0.0, 98.571088, 5.118355], [-0.054255, 98.516833, 5.118355], [0.0, 98.516833, 5.172605], [0.054255, 98.516833, 5.118355], [0.0, 98.516833, 5.0641], [0.0, 98.462578, 5.118355], [0.0, 98.516833, 5.172605], [0.0, 98.571088, 5.118355], [0.0, 98.516833, 5.0641], [-0.054255, 98.516833, 5.118355], [0.0, 98.516833, 5.172605], [0.0, 98.516833, 0.0]]}]},
			"R_leg_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-7.736573, 3.184991, 0.04756], [-7.625151, 3.184991, 0.04756], [-7.604049, 3.071422, 0.034354], [-7.524872, 3.038836, 0.030565], [-7.429098, 3.104321, 0.038179], [-7.350309, 3.02606, 0.029079], [-7.416232, 2.930937, 0.018018], [-7.38344, 2.852279, 0.008872], [-7.269095, 2.831319, 0.006435], [-7.269095, 2.720639, -0.006435], [-7.38344, 2.699679, -0.008872], [-7.416232, 2.621032, -0.018017], [-7.350309, 2.525899, -0.029079], [-7.429098, 2.447637, -0.038179], [-7.524872, 2.513122, -0.030565], [-7.604049, 2.480536, -0.034354], [-7.625151, 2.366967, -0.04756], [-7.736573, 2.366967, -0.04756], [-7.757685, 2.480536, -0.034354], [-7.836862, 2.513122, -0.030565], [-7.932636, 2.447637, -0.038179], [-8.011418, 2.525899, -0.029079], [-7.945502, 2.621032, -0.018017], [-7.978293, 2.699679, -0.008872], [-8.092628, 2.720639, -0.006435], [-8.092628, 2.831319, 0.006435], [-7.978293, 2.852279, 0.008872], [-7.945502, 2.930937, 0.018018], [-8.011418, 3.02606, 0.029079], [-7.932636, 3.104321, 0.038179], [-7.836862, 3.038836, 0.030565], [-7.757685, 3.071422, 0.034354], [-7.736573, 3.184991, 0.04756]]}, {"shapeName": "R_leg_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-7.801806, 2.896116, 0.013969], [-7.851905, 2.775979, -0.0], [-7.801806, 2.655842, -0.013969], [-7.680863, 2.606089, -0.019755], [-7.559928, 2.655842, -0.013969], [-7.509829, 2.775979, 0.0], [-7.559928, 2.896116, 0.013969], [-7.680863, 2.945869, 0.019755]]}, {"shapeName": "R_leg_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-7.269095, 2.775979, -0.0], [-5.0, 2.775979, -0.0]]}]},
			"R_elbowRibbon_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_elbowRibbon_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-38.026433, 93.016835, -8.4999], [-38.026433, 93.716835, -8.4999], [-38.039649, 91.850166, -10.24985], [-38.026433, 89.983497, -8.4999], [-38.026433, 90.683497, -8.4999], [-38.008811, 90.683497, -6.166636], [-38.008811, 88.350166, -6.166636], [-38.014098, 88.350166, -6.866616], [-38.0, 86.600166, -5.0], [-37.985902, 88.350166, -3.133384], [-37.991189, 88.350166, -3.833364], [-37.991189, 90.683497, -3.833364], [-37.973567, 90.683497, -1.5001], [-37.973567, 89.983497, -1.5001], [-37.960351, 91.850166, 0.24985], [-37.973567, 93.716835, -1.5001], [-37.973567, 93.016835, -1.5001], [-37.991189, 93.016835, -3.833364], [-37.991189, 95.350166, -3.833364], [-37.985902, 95.350166, -3.133384], [-38.0, 97.100166, -5.0], [-38.014098, 95.350166, -6.866616], [-38.008811, 95.350166, -6.166636], [-38.008811, 93.016835, -6.166636], [-38.026433, 93.016835, -8.4999]]}]},
			"C_spineShaper_3_CTL": {"color": 4, "shapes": [{"shapeName": "C_spineShaper_3_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 64.350166, -7.5], [0.0, 64.637176, -7.55709], [0.0, 64.880491, -7.719675], [0.0, 65.043076, -7.96299], [0.0, 65.100166, -8.25], [0.0, 65.043076, -8.53701], [0.0, 64.880491, -8.780325], [0.0, 64.637176, -8.94291], [0.0, 64.350166, -9.0], [0.0, 64.063156, -8.94291], [0.0, 63.819841, -8.780325], [0.0, 63.657256, -8.53701], [0.0, 63.600166, -8.25], [0.0, 63.657256, -7.96299], [0.0, 63.819841, -7.719675], [0.0, 64.063156, -7.55709], [0.0, 64.350166, -7.5], [0.0, 64.350166, 0.0]]}]},
			"L_loLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 19.185613, 1.962717], [4.945745, 19.191879, 1.908826], [5.0, 19.198146, 1.854934], [5.054255, 19.191879, 1.908826], [5.0, 19.185613, 1.962717], [5.0, 19.137992, 1.90256], [5.0, 19.198146, 1.854934], [5.0, 19.245771, 1.915092], [4.945745, 19.191879, 1.908826], [5.0, 19.137992, 1.90256], [5.054255, 19.191879, 1.908826], [5.0, 19.245771, 1.915092], [5.0, 19.185613, 1.962717], [5.0, 19.137992, 1.90256], [5.0, 24.275979, 2.5]]}, {"shapeName": "L_loLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 24.269712, 2.553892], [-0.118355, 24.329871, 2.506266], [-0.118355, 24.282245, 2.446108], [-0.118355, 24.222087, 2.493734], [-0.118355, 24.269712, 2.553892], [-0.172605, 24.275979, 2.5], [-0.118355, 24.282245, 2.446108], [-0.0641, 24.275979, 2.5], [-0.118355, 24.329871, 2.506266], [-0.172605, 24.275979, 2.5], [-0.118355, 24.222087, 2.493734], [-0.0641, 24.275979, 2.5], [-0.118355, 24.269712, 2.553892], [-0.172605, 24.275979, 2.5], [5.0, 24.275979, 2.5]]}, {"shapeName": "L_loLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 24.867153, -2.5841], [5.0, 24.921045, -2.577833], [5.054255, 24.867153, -2.5841], [5.0, 24.813261, -2.590366], [4.945745, 24.867153, -2.5841], [5.0, 24.873419, -2.637987], [5.054255, 24.867153, -2.5841], [5.0, 24.860887, -2.530208], [5.0, 24.921045, -2.577833], [5.0, 24.873419, -2.637987], [5.0, 24.813261, -2.590366], [5.0, 24.860887, -2.530208], [4.945745, 24.867153, -2.5841], [5.0, 24.873419, -2.637987], [5.0, 24.275979, 2.5]]}]},
			"R_elbowRibbon_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_elbowRibbon_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-38.033985, 93.350169, -9.499872], [-38.033985, 94.250169, -9.499872], [-38.050978, 91.850166, -11.749808], [-38.033985, 89.450163, -9.499872], [-38.033985, 90.350163, -9.499872], [-38.011328, 90.350163, -6.49996], [-38.011328, 87.350166, -6.49996], [-38.018125, 87.350166, -7.399935], [-38.0, 85.100166, -5.0], [-37.981875, 87.350166, -2.600065], [-37.988672, 87.350166, -3.50004], [-37.988672, 90.350163, -3.50004], [-37.966015, 90.350163, -0.500128], [-37.966015, 89.450163, -0.500128], [-37.949022, 91.850166, 1.749808], [-37.966015, 94.250169, -0.500128], [-37.966015, 93.350169, -0.500128], [-37.988672, 93.350169, -3.50004], [-37.988672, 96.350166, -3.50004], [-37.981875, 96.350166, -2.600065], [-38.0, 98.600166, -5.0], [-38.018125, 96.350166, -7.399935], [-38.011328, 96.350166, -6.49996], [-38.011328, 93.350169, -6.49996], [-38.033985, 93.350169, -9.499872]]}]},
			"C_hip_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_CTLShape", "degree": 3, "form": 2, "points": [[7.052508, 51.850166, -5.87709], [0.0, 48.850166, -8.311455], [-7.052508, 51.850166, -5.87709], [-9.973746, 54.850166, 0.0], [-7.052508, 51.850166, 5.87709], [0.0, 48.850166, 8.311455], [7.052508, 51.850166, 5.87709], [9.973746, 54.850166, 0.0]]}]},
			"L_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[70.102054, 91.842002, -0.054255], [70.106381, 91.896084, 0.0], [70.102054, 91.842002, 0.054255], [70.097728, 91.78792, 0.0], [70.102054, 91.842002, -0.054255], [70.156132, 91.837676, 0.0], [70.102054, 91.842002, 0.054255], [70.047972, 91.846329, 0.0], [70.106381, 91.896084, 0.0], [70.156132, 91.837676, 0.0], [70.097728, 91.78792, 0.0], [70.047972, 91.846329, 0.0], [70.102054, 91.842002, -0.054255], [70.156132, 91.837676, 0.0], [65.0, 92.250166, 0.0]]}, {"shapeName": "L_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.408164, 97.352221, -0.054255], [65.354082, 97.356547, 0.0], [65.408164, 97.352221, 0.054255], [65.462247, 97.347894, 0.0], [65.408164, 97.352221, -0.054255], [65.412491, 97.406298, 0.0], [65.408164, 97.352221, 0.054255], [65.403838, 97.298139, 0.0], [65.354082, 97.356547, 0.0], [65.412491, 97.406298, 0.0], [65.462247, 97.347894, 0.0], [65.403838, 97.298139, 0.0], [65.408164, 97.352221, -0.054255], [65.412491, 97.406298, 0.0], [65.0, 92.250166, 0.0]]}, {"shapeName": "L_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.004327, 92.304249, 5.118355], [64.945918, 92.254493, 5.118355], [64.995673, 92.196084, 5.118355], [65.054082, 92.24584, 5.118355], [65.004327, 92.304249, 5.118355], [65.0, 92.250166, 5.172605], [64.995673, 92.196084, 5.118355], [65.0, 92.250166, 5.0641], [64.945918, 92.254493, 5.118355], [65.0, 92.250166, 5.172605], [65.054082, 92.24584, 5.118355], [65.0, 92.250166, 5.0641], [65.004327, 92.304249, 5.118355], [65.0, 92.250166, 5.172605], [65.0, 92.250166, 0.0]]}]},
			"R_leg_IK_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-7.056982, 2.775979, -3.428302], [-5.0, 2.775979, -4.848349], [-2.943018, 2.775979, -3.428302], [-2.090991, 2.775979, 0.0], [-2.943018, 2.775979, 3.428303], [-5.0, 2.775979, 4.848349], [-7.056982, 2.775979, 3.428303], [-7.909009, 2.775979, 0.0]]}]},
			"R_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_D_CTLShape", "degree": 1, "form": 0, "points": [[-67.717544, 92.744464, -1.75], [-66.230702, 92.94271, -1.75], [-66.230702, 92.94271, -3.25], [-67.717544, 92.744464, -3.25], [-67.519298, 91.257623, -3.25], [-66.032456, 91.455868, -3.25], [-66.032456, 91.455868, -1.75], [-67.519298, 91.257623, -1.75], [-67.717544, 92.744464, -1.75], [-67.717544, 92.744464, -3.25], [-66.230702, 92.94271, -3.25], [-66.032456, 91.455868, -3.25], [-67.519298, 91.257623, -3.25], [-67.519298, 91.257623, -1.75], [-66.032456, 91.455868, -1.75], [-66.230702, 92.94271, -1.75]]}]},
			"R_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-70.102054, 91.842036, -0.054255], [-70.106381, 91.896118, -0.0], [-70.102054, 91.842036, 0.054255], [-70.097728, 91.787954, -0.0], [-70.102054, 91.842036, -0.054255], [-70.156132, 91.83771, -0.0], [-70.102054, 91.842036, 0.054255], [-70.047972, 91.846363, -0.0], [-70.106381, 91.896118, -0.0], [-70.156132, 91.83771, -0.0], [-70.097728, 91.787954, -0.0], [-70.047972, 91.846363, -0.0], [-70.102054, 91.842036, -0.054255], [-70.156132, 91.83771, -0.0], [-65.0, 92.2502, -0.0]]}, {"shapeName": "R_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.408164, 97.352255, -0.054255], [-65.354082, 97.356581, 0.0], [-65.408164, 97.352255, 0.054255], [-65.462247, 97.347928, 0.0], [-65.408164, 97.352255, -0.054255], [-65.412491, 97.406332, 0.0], [-65.408164, 97.352255, 0.054255], [-65.403838, 97.298173, 0.0], [-65.354082, 97.356581, 0.0], [-65.412491, 97.406332, 0.0], [-65.462247, 97.347928, 0.0], [-65.403838, 97.298173, 0.0], [-65.408164, 97.352255, -0.054255], [-65.412491, 97.406332, 0.0], [-65.0, 92.2502, -0.0]]}, {"shapeName": "R_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-65.004327, 92.304283, 5.118355], [-64.945918, 92.254527, 5.118355], [-64.995673, 92.196118, 5.118355], [-65.054082, 92.245874, 5.118355], [-65.004327, 92.304283, 5.118355], [-65.0, 92.2502, 5.172605], [-64.995673, 92.196118, 5.118355], [-65.0, 92.2502, 5.0641], [-64.945918, 92.254527, 5.118355], [-65.0, 92.2502, 5.172605], [-65.054082, 92.245874, 5.118355], [-65.0, 92.2502, 5.0641], [-65.004327, 92.304283, 5.118355], [-65.0, 92.2502, 5.172605], [-65.0, 92.2502, -0.0]]}]},
			"R_clavicle_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_clavicle_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-3.25732, 91.850166, -2.895317], [-1.651138, 91.850166, -7.580015], [-1.037629, 91.850166, -9.369416], [-1.651138, 97.672059, -7.580015], [-3.25732, 101.270192, -2.895317], [-5.24268, 101.270192, 2.895317], [-6.848862, 97.672059, 7.580015], [-7.462371, 91.850166, 9.369416], [-6.848862, 91.850166, 7.580015], [-5.24268, 91.850166, 2.895317], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0]]}]},
			"L_bendyLeg_A_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.499999, 34.462031, 2.738417], [4.199999, 34.462031, 2.738417], [5.0, 34.555057, 3.482625], [5.800001, 34.462031, 2.738417], [5.500001, 34.462031, 2.738417], [5.500001, 34.337996, 1.74614], [6.5, 34.337996, 1.74614], [6.5, 34.375207, 2.043823], [7.25, 34.275979, 1.25], [6.5, 34.176751, 0.456177], [6.5, 34.213961, 0.75386], [5.500001, 34.213961, 0.75386], [5.500001, 34.089927, -0.238417], [5.800001, 34.089927, -0.238417], [5.0, 33.996901, -0.982625], [4.199999, 34.089927, -0.238417], [4.499999, 34.089927, -0.238417], [4.499999, 34.213961, 0.75386], [3.5, 34.213961, 0.75386], [3.5, 34.176751, 0.456177], [2.75, 34.275979, 1.25], [3.5, 34.375207, 2.043823], [3.5, 34.337996, 1.74614], [4.499999, 34.337996, 1.74614], [4.499999, 34.462031, 2.738417]]}]},
			"R_upLeg_shaper_03_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upLeg_shaper_03_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 29.203878, 1.93869], [-4.945745, 29.197149, 1.884854], [-5.0, 29.190419, 1.831018], [-5.054255, 29.197149, 1.884854], [-5.0, 29.203878, 1.93869], [-5.0, 29.143317, 1.891583], [-5.0, 29.190419, 1.831018], [-5.0, 29.250985, 1.878124], [-4.945745, 29.197149, 1.884854], [-5.0, 29.143317, 1.891583], [-5.054255, 29.197149, 1.884854], [-5.0, 29.250985, 1.878124], [-5.0, 29.203878, 1.93869], [-5.0, 29.143317, 1.891583], [-5.0, 34.275979, 1.25]]}, {"shapeName": "R_upLeg_shaper_03_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 34.282708, 1.303836], [0.118355, 34.329815, 1.24327], [0.118355, 34.269249, 1.196164], [0.118355, 34.222143, 1.25673], [0.118355, 34.282708, 1.303836], [0.172605, 34.275979, 1.25], [0.118355, 34.269249, 1.196164], [0.0641, 34.275979, 1.25], [0.118355, 34.329815, 1.24327], [0.172605, 34.275979, 1.25], [0.118355, 34.222143, 1.25673], [0.0641, 34.275979, 1.25], [0.118355, 34.282708, 1.303836], [0.172605, 34.275979, 1.25], [-5.0, 34.275979, 1.25]]}, {"shapeName": "R_upLeg_shaper_03_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 33.641125, -3.82883], [-5.0, 33.694961, -3.83556], [-5.054255, 33.641125, -3.82883], [-5.0, 33.587289, -3.822101], [-4.945745, 33.641125, -3.82883], [-5.0, 33.634396, -3.882662], [-5.054255, 33.641125, -3.82883], [-5.0, 33.647855, -3.774994], [-5.0, 33.694961, -3.83556], [-5.0, 33.634396, -3.882662], [-5.0, 33.587289, -3.822101], [-5.0, 33.647855, -3.774994], [-4.945745, 33.641125, -3.82883], [-5.0, 33.634396, -3.882662], [-5.0, 34.275979, 1.25]]}]},
			"L_elbow_shaper_05_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_05_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[54.15, 93.350166, -0.25], [54.205069, 93.361584, -0.233803], [54.251755, 93.394101, -0.220072], [54.282951, 93.442764, -0.210897], [54.293905, 93.500166, -0.207675], [54.282951, 93.557568, -0.210897], [54.251755, 93.606231, -0.220072], [54.205069, 93.638748, -0.233803], [54.15, 93.650166, -0.25], [54.094931, 93.638748, -0.266197], [54.048245, 93.606231, -0.279928], [54.017049, 93.557568, -0.289103], [54.006095, 93.500166, -0.292325], [54.017049, 93.442764, -0.289103], [54.048245, 93.394101, -0.279928], [54.094931, 93.361584, -0.266197], [54.15, 93.350166, -0.25], [54.15, 91.850166, -0.25]]}]},
			"R_elbow_shaper_04_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_elbow_shaper_04_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-51.735136, 91.850166, -0.971565], [-51.732075, 91.861017, -0.961155], [-51.729013, 91.850166, -0.950744], [-51.732075, 91.839315, -0.961155], [-51.735136, 91.850166, -0.971565], [-51.742484, 91.850166, -0.958093], [-51.729013, 91.850166, -0.950744], [-51.721665, 91.850166, -0.964216], [-51.732075, 91.861017, -0.961155], [-51.742484, 91.850166, -0.958093], [-51.732075, 91.839315, -0.961155], [-51.721665, 91.850166, -0.964216], [-51.735136, 91.850166, -0.971565], [-51.742484, 91.850166, -0.958093], [-50.75, 91.850166, -1.25]]}, {"shapeName": "R_elbow_shaper_04_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-50.753062, 92.873837, -1.26041], [-50.73959, 92.873837, -1.253062], [-50.746938, 92.873837, -1.23959], [-50.76041, 92.873837, -1.246938], [-50.753062, 92.873837, -1.26041], [-50.75, 92.884687, -1.25], [-50.746938, 92.873837, -1.23959], [-50.75, 92.862986, -1.25], [-50.73959, 92.873837, -1.253062], [-50.75, 92.884687, -1.25], [-50.76041, 92.873837, -1.246938], [-50.75, 92.862986, -1.25], [-50.753062, 92.873837, -1.26041], [-50.75, 92.884687, -1.25], [-50.75, 91.850166, -1.25]]}, {"shapeName": "R_elbow_shaper_04_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-50.461155, 91.861017, -0.267925], [-50.450744, 91.850166, -0.270987], [-50.461155, 91.839315, -0.267925], [-50.471565, 91.850166, -0.264864], [-50.461155, 91.861017, -0.267925], [-50.458093, 91.850166, -0.257516], [-50.461155, 91.839315, -0.267925], [-50.464216, 91.850166, -0.278335], [-50.450744, 91.850166, -0.270987], [-50.458093, 91.850166, -0.257516], [-50.471565, 91.850166, -0.264864], [-50.464216, 91.850166, -0.278335], [-50.461155, 91.861017, -0.267925], [-50.458093, 91.850166, -0.257516], [-50.75, 91.850166, -1.25]]}]},
			"L_shoulder_shaper_05_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_05_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[37.1, 94.100166, -4.75], [37.182962, 94.117293, -4.773045], [37.253293, 94.166069, -4.792581], [37.300289, 94.239063, -4.805636], [37.316792, 94.325166, -4.81022], [37.300289, 94.411269, -4.805636], [37.253293, 94.484264, -4.792581], [37.182962, 94.533039, -4.773045], [37.1, 94.550166, -4.75], [37.017038, 94.533039, -4.726955], [36.946707, 94.484264, -4.707419], [36.899711, 94.411269, -4.694364], [36.883208, 94.325166, -4.68978], [36.899711, 94.239063, -4.694364], [36.946707, 94.166069, -4.707419], [37.017038, 94.117293, -4.726955], [37.1, 94.100166, -4.75], [37.1, 91.850166, -4.75]]}]},
			"L_shoulder_shaper_01_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_shoulder_shaper_01_PIV_CTLShape", "degree": 1, "form": 0, "points": [[21.883421, 91.850166, -0.534434], [21.886325, 91.861017, -0.523979], [21.88923, 91.850166, -0.513524], [21.886325, 91.839315, -0.523979], [21.883421, 91.850166, -0.534434], [21.89678, 91.850166, -0.526883], [21.88923, 91.850166, -0.513524], [21.87587, 91.850166, -0.521075], [21.886325, 91.861017, -0.523979], [21.89678, 91.850166, -0.526883], [21.886325, 91.839315, -0.523979], [21.87587, 91.850166, -0.521075], [21.883421, 91.850166, -0.534434], [21.89678, 91.850166, -0.526883], [20.9, 91.850166, -0.25]]}, {"shapeName": "L_shoulder_shaper_01_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[20.897096, 92.873837, -0.260455], [20.889545, 92.873837, -0.247096], [20.902904, 92.873837, -0.239545], [20.910455, 92.873837, -0.252904], [20.897096, 92.873837, -0.260455], [20.9, 92.884687, -0.25], [20.902904, 92.873837, -0.239545], [20.9, 92.862986, -0.25], [20.889545, 92.873837, -0.247096], [20.9, 92.884687, -0.25], [20.910455, 92.873837, -0.252904], [20.9, 92.862986, -0.25], [20.897096, 92.873837, -0.260455], [20.9, 92.884687, -0.25], [20.9, 91.850166, -0.25]]}, {"shapeName": "L_shoulder_shaper_01_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[21.173979, 91.861017, 0.736325], [21.163524, 91.850166, 0.73923], [21.173979, 91.839315, 0.736325], [21.184434, 91.850166, 0.733421], [21.173979, 91.861017, 0.736325], [21.176883, 91.850166, 0.74678], [21.173979, 91.839315, 0.736325], [21.171075, 91.850166, 0.72587], [21.163524, 91.850166, 0.73923], [21.176883, 91.850166, 0.74678], [21.184434, 91.850166, 0.733421], [21.171075, 91.850166, 0.72587], [21.173979, 91.861017, 0.736325], [21.176883, 91.850166, 0.74678], [20.9, 91.850166, -0.25]]}]},
			"R_lwrArmTwist_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_lwrArmTwist_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-49.768859, 91.921558, -4.238075], [-47.939412, 91.921558, -5.545509], [-49.550686, 91.921558, -7.244184], [-51.552304, 91.921558, -8.473882], [-53.797211, 91.921558, -9.149687], [-56.139995, 91.921558, -9.237326], [-58.423812, 91.921558, -8.7107], [-60.486939, 91.921558, -7.633563], [-62.185614, 91.921558, -6.022289], [-63.415312, 91.921558, -4.020671], [-64.091117, 91.921558, -1.775764], [-64.178757, 91.921558, 0.56702], [-63.652131, 91.921558, 2.850836], [-62.574994, 91.921558, 4.913964], [-60.96372, 91.921558, 6.612638], [-58.962101, 91.921558, 7.842337], [-56.717195, 91.921558, 8.518142], [-54.374411, 91.921558, 8.605782], [-52.090593, 91.921558, 8.079156], [-50.027466, 91.921558, 7.002019], [-48.646489, 91.921558, 8.934373], [-44.947846, 91.921558, 1.903535], [-52.773078, 91.921558, 3.160178], [-51.3349, 91.921558, 5.172571], [-52.880203, 91.921558, 5.983282], [-54.587349, 91.921558, 6.374166], [-56.351785, 91.921558, 6.322325], [-58.037919, 91.921558, 5.799951], [-59.537905, 91.921558, 4.885438], [-60.745546, 91.921558, 3.60653], [-61.556257, 91.921558, 2.061227], [-61.947141, 91.921558, 0.354082], [-61.8953, 91.921558, -1.410355], [-61.372926, 91.921558, -3.096489], [-60.458413, 91.921558, -4.596475], [-59.179506, 91.921558, -5.804116], [-57.634202, 91.921558, -6.614827], [-55.927057, 91.921558, -7.005711], [-54.16262, 91.921558, -6.95387], [-52.476486, 91.921558, -6.431496], [-50.9765, 91.921558, -5.516982], [-49.768859, 91.921558, -4.238075]]}]},
			"L_elbow_shaper_03_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_03_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[46.5, 93.600166, -2.5], [46.564248, 93.613487, -2.481104], [46.618714, 93.651424, -2.465084], [46.655109, 93.708197, -2.45438], [46.667889, 93.775166, -2.450621], [46.655109, 93.842135, -2.45438], [46.618714, 93.898909, -2.465084], [46.564248, 93.936845, -2.481104], [46.5, 93.950166, -2.5], [46.435752, 93.936845, -2.518896], [46.381286, 93.898909, -2.534916], [46.344891, 93.842135, -2.54562], [46.332111, 93.775166, -2.549379], [46.344891, 93.708197, -2.54562], [46.381286, 93.651424, -2.534916], [46.435752, 93.613487, -2.518896], [46.5, 93.600166, -2.5], [46.5, 91.850166, -2.5]]}]},
			"L_elbow_shaper_04_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_04_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[50.75, 93.600166, -1.25], [50.814248, 93.613487, -1.231104], [50.868714, 93.651424, -1.215084], [50.905109, 93.708197, -1.20438], [50.917889, 93.775166, -1.200621], [50.905109, 93.842135, -1.20438], [50.868714, 93.898909, -1.215084], [50.814248, 93.936845, -1.231104], [50.75, 93.950166, -1.25], [50.685752, 93.936845, -1.268896], [50.631286, 93.898909, -1.284916], [50.594891, 93.842135, -1.29562], [50.582111, 93.775166, -1.299379], [50.594891, 93.708197, -1.29562], [50.631286, 93.651424, -1.284916], [50.685752, 93.613487, -1.268896], [50.75, 93.600166, -1.25], [50.75, 91.850166, -1.25]]}]},
			"L_legBase_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_legBase_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 43.53915, 0.092104], [5.0, 42.346942, 0.24113], [5.0, 41.891558, 0.298053], [5.0, 42.697323, 3.044182], [5.0, 44.10608, 4.627539], [5.0, 45.579737, 4.443332], [5.0, 46.555398, 2.561922], [5.0, 46.6604, -0.298053], [5.0, 46.205016, -0.24113], [5.0, 45.012808, -0.092104], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0]]}]},
			"L_shoulder_shaper_03_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_03_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[29.0, 93.350166, -2.5], [29.055308, 93.361584, -2.515363], [29.102196, 93.394101, -2.528388], [29.133526, 93.442764, -2.537091], [29.144528, 93.500166, -2.540147], [29.133526, 93.557568, -2.537091], [29.102196, 93.606231, -2.528388], [29.055308, 93.638748, -2.515363], [29.0, 93.650166, -2.5], [28.944692, 93.638748, -2.484637], [28.897804, 93.606231, -2.471612], [28.866474, 93.557568, -2.462909], [28.855472, 93.500166, -2.459853], [28.866474, 93.442764, -2.462909], [28.897804, 93.394101, -2.471612], [28.944692, 93.361584, -2.484637], [29.0, 93.350166, -2.5], [29.0, 91.850166, -2.5]]}]},
			"R_lwrArmRibbonMid_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lwrArmRibbonMid_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-47.628665, 93.183502, -6.337462], [-47.628665, 93.983502, -6.337462], [-48.192998, 91.850166, -8.256193], [-47.628665, 89.71683, -6.337462], [-47.628665, 90.51683, -6.337462], [-46.876223, 90.51683, -3.779157], [-46.876223, 87.850166, -3.779157], [-47.101956, 87.850166, -4.546649], [-46.5, 85.850166, -2.5], [-45.898044, 87.850166, -0.453351], [-46.123777, 87.850166, -1.220843], [-46.123777, 90.51683, -1.220843], [-45.371335, 90.51683, 1.337462], [-45.371335, 89.71683, 1.337462], [-44.807002, 91.850166, 3.256193], [-45.371335, 93.983502, 1.337462], [-45.371335, 93.183502, 1.337462], [-46.123777, 93.183502, -1.220843], [-46.123777, 95.850166, -1.220843], [-45.898044, 95.850166, -0.453351], [-46.5, 97.850166, -2.5], [-47.101956, 95.850166, -4.546649], [-46.876223, 95.850166, -3.779157], [-46.876223, 93.183502, -3.779157], [-47.628665, 93.183502, -6.337462]]}]},
			"R_elbow_shaper_01_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_01_CTLShape", "degree": 1, "form": 0, "points": [[-38.85, 94.350166, -4.75], [-38.941782, 94.369196, -4.723005], [-39.019592, 94.423391, -4.70012], [-39.071585, 94.504496, -4.684828], [-39.089841, 94.600166, -4.679458], [-39.071585, 94.695836, -4.684828], [-39.019592, 94.776941, -4.70012], [-38.941782, 94.831136, -4.723005], [-38.85, 94.850166, -4.75], [-38.758218, 94.831136, -4.776995], [-38.680408, 94.776941, -4.79988], [-38.628415, 94.695836, -4.815172], [-38.610159, 94.600166, -4.820542], [-38.628415, 94.504496, -4.815172], [-38.680408, 94.423391, -4.79988], [-38.758218, 94.369196, -4.776995], [-38.85, 94.350166, -4.75], [-38.85, 91.850166, -4.75]]}]},
			"L_elbowFk_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_elbowFk_PIV_CTLShape", "degree": 1, "form": 0, "points": [[38.985136, 91.850166, -4.721565], [38.982075, 91.861017, -4.711155], [38.979013, 91.850166, -4.700744], [38.982075, 91.839315, -4.711155], [38.985136, 91.850166, -4.721565], [38.992484, 91.850166, -4.708093], [38.979013, 91.850166, -4.700744], [38.971665, 91.850166, -4.714216], [38.982075, 91.861017, -4.711155], [38.992484, 91.850166, -4.708093], [38.982075, 91.839315, -4.711155], [38.971665, 91.850166, -4.714216], [38.985136, 91.850166, -4.721565], [38.992484, 91.850166, -4.708093], [38.0, 91.850166, -5.0]]}, {"shapeName": "L_elbowFk_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[38.003062, 92.873837, -5.01041], [37.98959, 92.873837, -5.003062], [37.996938, 92.873837, -4.98959], [38.01041, 92.873837, -4.996938], [38.003062, 92.873837, -5.01041], [38.0, 92.884687, -5.0], [37.996938, 92.873837, -4.98959], [38.0, 92.862986, -5.0], [37.98959, 92.873837, -5.003062], [38.0, 92.884687, -5.0], [38.01041, 92.873837, -4.996938], [38.0, 92.862986, -5.0], [38.003062, 92.873837, -5.01041], [38.0, 92.884687, -5.0], [38.0, 91.850166, -5.0]]}, {"shapeName": "L_elbowFk_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[37.711155, 91.861017, -4.017925], [37.700744, 91.850166, -4.020987], [37.711155, 91.839315, -4.017925], [37.721565, 91.850166, -4.014864], [37.711155, 91.861017, -4.017925], [37.708093, 91.850166, -4.007516], [37.711155, 91.839315, -4.017925], [37.714216, 91.850166, -4.028335], [37.700744, 91.850166, -4.020987], [37.708093, 91.850166, -4.007516], [37.721565, 91.850166, -4.014864], [37.714216, 91.850166, -4.028335], [37.711155, 91.861017, -4.017925], [37.708093, 91.850166, -4.007516], [38.0, 91.850166, -5.0]]}]},
			"R_legBase_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 43.170736, 0.138155], [-5.0, 41.382423, 0.361694], [-5.0, 40.699347, 0.447079], [-5.0, 41.907995, 4.566273], [-5.0, 44.02113, 6.941308], [-5.0, 46.231616, 6.664997], [-5.0, 47.695107, 3.842884], [-5.0, 47.852611, -0.447079], [-5.0, 47.169535, -0.361694], [-5.0, 45.381222, -0.138155], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0]]}]},
			"L_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.323456, 92.526627, -2.554255], [66.316286, 92.580406, -2.5], [66.323456, 92.526627, -2.445745], [66.330627, 92.472848, -2.5], [66.323456, 92.526627, -2.554255], [66.37723, 92.533797, -2.5], [66.323456, 92.526627, -2.445745], [66.269677, 92.519457, -2.5], [66.316286, 92.580406, -2.5], [66.37723, 92.533797, -2.5], [66.330627, 92.472848, -2.5], [66.269677, 92.519457, -2.5], [66.323456, 92.526627, -2.554255], [66.37723, 92.533797, -2.5], [61.25, 91.850166, -2.5]]}, {"shapeName": "L_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[60.573539, 96.923623, -2.554255], [60.51976, 96.916452, -2.5], [60.573539, 96.923623, -2.445745], [60.627318, 96.930793, -2.5], [60.573539, 96.923623, -2.554255], [60.566369, 96.977397, -2.5], [60.573539, 96.923623, -2.445745], [60.58071, 96.869844, -2.5], [60.51976, 96.916452, -2.5], [60.566369, 96.977397, -2.5], [60.627318, 96.930793, -2.5], [60.58071, 96.869844, -2.5], [60.573539, 96.923623, -2.554255], [60.566369, 96.977397, -2.5], [61.25, 91.850166, -2.5]]}, {"shapeName": "L_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.242829, 91.903945, 2.618355], [61.196221, 91.842996, 2.618355], [61.257171, 91.796387, 2.618355], [61.303779, 91.857337, 2.618355], [61.242829, 91.903945, 2.618355], [61.25, 91.850166, 2.672605], [61.257171, 91.796387, 2.618355], [61.25, 91.850166, 2.5641], [61.196221, 91.842996, 2.618355], [61.25, 91.850166, 2.672605], [61.303779, 91.857337, 2.618355], [61.25, 91.850166, 2.5641], [61.242829, 91.903945, 2.618355], [61.25, 91.850166, 2.672605], [61.25, 91.850166, -2.5]]}]},
			"R_upLeg_shaper_05_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_05_CTLShape", "degree": 1, "form": 0, "points": [[-17.5, 27.609312, 2.083333], [-17.59515, 27.039725, 2.154532], [-17.866125, 26.556853, 2.214891], [-18.27165, 26.234194, 2.255223], [-18.75, 26.120895, 2.269385], [-19.22835, 26.234194, 2.255223], [-19.633875, 26.556853, 2.214891], [-19.90485, 27.039725, 2.154532], [-20.0, 27.609312, 2.083333], [-19.90485, 28.1789, 2.012135], [-19.633875, 28.661772, 1.951776], [-19.22835, 28.984431, 1.911444], [-18.75, 29.097729, 1.897281], [-18.27165, 28.984431, 1.911444], [-17.866125, 28.661772, 1.951776], [-17.59515, 28.1789, 2.012135], [-17.5, 27.609312, 2.083333], [-5.0, 27.609312, 2.083333]]}]},
			"L_clavicle_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_clavicle_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [2.973697, 91.850166, -3.722551], [0.908606, 91.850166, -9.745734], [0.119809, 91.850166, -12.046392], [0.908606, 99.335457, -9.745734], [2.973697, 103.961628, -3.722551], [5.526303, 103.961628, 3.722551], [7.591394, 99.335457, 9.745734], [8.380191, 91.850166, 12.046392], [7.591394, 91.850166, 9.745734], [5.526303, 91.850166, 3.722551], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0]]}]},
			"C_jaw_CTL": {"color": 18, "shapes": [{"shapeName": "C_jaw_CTLShape", "degree": 3, "form": 0, "points": [[0.0, 101.850166, 2.5], [0.0, 101.850166, 2.5], [0.0, 101.850166, 2.5], [-1.65014, 101.850166, 2.5], [-4.32011, 101.850166, 2.5], [-5.33995, 101.850166, 2.5], [-4.32011, 101.850166, 10.34685], [-1.65014, 101.850166, 15.196475], [1.65014, 101.850166, 15.196475], [4.32011, 101.850166, 10.34685], [5.33995, 101.850166, 2.5], [4.32011, 101.850166, 2.5], [1.65014, 101.850166, 2.5], [0.0, 101.850166, 2.5], [0.0, 101.850166, 2.5], [0.0, 101.850166, 2.5]]}]},
			"L_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[71.948456, 91.423705, -0.054255], [71.955627, 91.477485, 0.0], [71.948456, 91.423705, 0.054255], [71.941286, 91.369926, 0.0], [71.948456, 91.423705, -0.054255], [72.00223, 91.416536, 0.0], [71.948456, 91.423705, 0.054255], [71.894677, 91.430876, 0.0], [71.955627, 91.477485, 0.0], [72.00223, 91.416536, 0.0], [71.941286, 91.369926, 0.0], [71.894677, 91.430876, 0.0], [71.948456, 91.423705, -0.054255], [72.00223, 91.416536, 0.0], [66.875, 92.100166, 0.0]]}, {"shapeName": "L_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.551461, 97.173623, -0.054255], [67.497682, 97.180793, 0.0], [67.551461, 97.173623, 0.054255], [67.60524, 97.166452, 0.0], [67.551461, 97.173623, -0.054255], [67.558631, 97.227397, 0.0], [67.551461, 97.173623, 0.054255], [67.54429, 97.119844, 0.0], [67.497682, 97.180793, 0.0], [67.558631, 97.227397, 0.0], [67.60524, 97.166452, 0.0], [67.54429, 97.119844, 0.0], [67.551461, 97.173623, -0.054255], [67.558631, 97.227397, 0.0], [66.875, 92.100166, 0.0]]}, {"shapeName": "L_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[66.882171, 92.153945, 5.118355], [66.821221, 92.107337, 5.118355], [66.867829, 92.046387, 5.118355], [66.928779, 92.092996, 5.118355], [66.882171, 92.153945, 5.118355], [66.875, 92.100166, 5.172605], [66.867829, 92.046387, 5.118355], [66.875, 92.100166, 5.0641], [66.821221, 92.107337, 5.118355], [66.875, 92.100166, 5.172605], [66.928779, 92.092996, 5.118355], [66.875, 92.100166, 5.0641], [66.882171, 92.153945, 5.118355], [66.875, 92.100166, 5.172605], [66.875, 92.100166, 0.0]]}]},
			"R_shoulderFk_CTL": {"color": 6, "shapes": [{"shapeName": "R_shoulderFk_CTLShape", "degree": 1, "form": 0, "points": [[-18.260315, 94.350166, 3.077904], [-18.260315, 89.350166, 3.077904], [-16.922096, 89.350166, -1.739685], [-16.922096, 94.350166, -1.739685], [-21.739685, 94.350166, -3.077904], [-21.739685, 89.350166, -3.077904], [-23.077904, 89.350166, 1.739685], [-23.077904, 94.350166, 1.739685], [-18.260315, 94.350166, 3.077904], [-16.922096, 94.350166, -1.739685], [-16.922096, 89.350166, -1.739685], [-21.739685, 89.350166, -3.077904], [-21.739685, 94.350166, -3.077904], [-23.077904, 94.350166, 1.739685], [-23.077904, 89.350166, 1.739685], [-18.260315, 89.350166, 3.077904]]}]},
			"R_loLeg_shaper_02_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_02_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-15.0, 17.109312, 1.666667], [-15.07612, 16.65317, 1.613627], [-15.2929, 16.266471, 1.568662], [-15.61732, 16.008076, 1.538616], [-16.0, 15.917343, 1.528066], [-16.38268, 16.008076, 1.538616], [-16.7071, 16.266471, 1.568662], [-16.92388, 16.65317, 1.613627], [-17.0, 17.109312, 1.666667], [-16.92388, 17.565455, 1.719707], [-16.7071, 17.952154, 1.764671], [-16.38268, 18.210549, 1.794717], [-16.0, 18.301281, 1.805268], [-15.61732, 18.210549, 1.794717], [-15.2929, 17.952154, 1.764671], [-15.07612, 17.565455, 1.719707], [-15.0, 17.109312, 1.666667], [-5.0, 17.109312, 1.666667]]}]},
			"R_shoulder_shaper_02_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_02_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-24.5, 93.850166, -1.25], [-24.573744, 93.86539, -1.270484], [-24.636261, 93.908746, -1.28785], [-24.678035, 93.97363, -1.299454], [-24.692704, 94.050166, -1.303529], [-24.678035, 94.126702, -1.299454], [-24.636261, 94.191586, -1.28785], [-24.573744, 94.234942, -1.270484], [-24.5, 94.250166, -1.25], [-24.426256, 94.234942, -1.229516], [-24.363739, 94.191586, -1.21215], [-24.321965, 94.126702, -1.200546], [-24.307296, 94.050166, -1.196471], [-24.321965, 93.97363, -1.200546], [-24.363739, 93.908746, -1.21215], [-24.426256, 93.86539, -1.229516], [-24.5, 93.850166, -1.25], [-24.5, 91.850166, -1.25]]}]},
			"R_loLeg_shaper_01_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_loLeg_shaper_01_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 15.602279, 1.546051], [-4.945745, 15.608546, 1.492159], [-5.0, 15.614812, 1.438267], [-5.054255, 15.608546, 1.492159], [-5.0, 15.602279, 1.546051], [-5.0, 15.554659, 1.485893], [-5.0, 15.614812, 1.438267], [-5.0, 15.662438, 1.498425], [-4.945745, 15.608546, 1.492159], [-5.0, 15.554659, 1.485893], [-5.054255, 15.608546, 1.492159], [-5.0, 15.662438, 1.498425], [-5.0, 15.602279, 1.546051], [-5.0, 15.554659, 1.485893], [-5.0, 20.692646, 2.083333]]}, {"shapeName": "R_loLeg_shaper_01_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 20.686379, 2.137225], [0.118355, 20.746538, 2.0896], [0.118355, 20.698912, 2.029441], [0.118355, 20.638754, 2.077067], [0.118355, 20.686379, 2.137225], [0.172605, 20.692646, 2.083333], [0.118355, 20.698912, 2.029441], [0.0641, 20.692646, 2.083333], [0.118355, 20.746538, 2.0896], [0.172605, 20.692646, 2.083333], [0.118355, 20.638754, 2.077067], [0.0641, 20.692646, 2.083333], [0.118355, 20.686379, 2.137225], [0.172605, 20.692646, 2.083333], [-5.0, 20.692646, 2.083333]]}, {"shapeName": "R_loLeg_shaper_01_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 21.28382, -3.000766], [-5.0, 21.337712, -2.9945], [-5.054255, 21.28382, -3.000766], [-5.0, 21.229928, -3.007033], [-4.945745, 21.28382, -3.000766], [-5.0, 21.290086, -3.054653], [-5.054255, 21.28382, -3.000766], [-5.0, 21.277554, -2.946875], [-5.0, 21.337712, -2.9945], [-5.0, 21.290086, -3.054653], [-5.0, 21.229928, -3.007033], [-5.0, 21.277554, -2.946875], [-4.945745, 21.28382, -3.000766], [-5.0, 21.290086, -3.054653], [-5.0, 20.692646, 2.083333]]}]},
			"L_elbow_shaper_04_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_04_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[50.75, 94.100166, -1.25], [50.832604, 94.117293, -1.225705], [50.902633, 94.166069, -1.205108], [50.949426, 94.239063, -1.191345], [50.965857, 94.325166, -1.186513], [50.949426, 94.411269, -1.191345], [50.902633, 94.484264, -1.205108], [50.832604, 94.533039, -1.225705], [50.75, 94.550166, -1.25], [50.667396, 94.533039, -1.274295], [50.597367, 94.484264, -1.294892], [50.550574, 94.411269, -1.308655], [50.534143, 94.325166, -1.313487], [50.550574, 94.239063, -1.308655], [50.597367, 94.166069, -1.294892], [50.667396, 94.117293, -1.274295], [50.75, 94.100166, -1.25], [50.75, 91.850166, -1.25]]}]},
			"L_elbowUpVectorIk_CTL": {"color": 6, "shapes": [{"shapeName": "L_elbowUpVectorIk_CTLShape", "degree": 1, "form": 0, "points": [[36.5, 91.850166, -26.5], [36.5, 91.850166, -23.5], [39.5, 91.850166, -23.5], [39.5, 91.850166, -26.5], [36.5, 91.850166, -26.5], [38.0, 93.350166, -25.0], [39.5, 91.850166, -26.5], [39.5, 91.850166, -23.5], [38.0, 93.350166, -25.0], [36.5, 91.850166, -23.5]]}]},
			"L_leg_IK_CTL": {"color": 6, "shapes": [{"shapeName": "L_leg_IK_CTLShape", "degree": 3, "form": 2, "points": [[7.938545, 2.775979, -4.897575], [5.0, 2.775979, -6.926213], [2.061455, 2.775979, -4.897575], [0.844273, 2.775979, 0.0], [2.061455, 2.775979, 4.897575], [5.0, 2.775979, 6.926213], [7.938545, 2.775979, 4.897575], [9.155727, 2.775979, 0.0]]}]},
			"L_loLeg_shaper_03_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_03_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[15.0, 13.525979, 1.25], [15.07612, 13.069836, 1.19696], [15.2929, 12.683138, 1.151995], [15.61732, 12.424743, 1.121949], [16.0, 12.33401, 1.111399], [16.38268, 12.424743, 1.121949], [16.7071, 12.683138, 1.151995], [16.92388, 13.069836, 1.19696], [17.0, 13.525979, 1.25], [16.92388, 13.982122, 1.30304], [16.7071, 14.36882, 1.348005], [16.38268, 14.627215, 1.378051], [16.0, 14.717948, 1.388601], [15.61732, 14.627215, 1.378051], [15.2929, 14.36882, 1.348005], [15.07612, 13.982122, 1.30304], [15.0, 13.525979, 1.25], [5.0, 13.525979, 1.25]]}]},
			"L_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_A_CTLShape", "degree": 1, "form": 0, "points": [[61.894298, 92.69271, 2.0], [60.407456, 92.494464, 2.0], [60.407456, 92.494464, 0.5], [61.894298, 92.69271, 0.5], [62.092544, 91.205868, 0.5], [60.605702, 91.007623, 0.5], [60.605702, 91.007623, 2.0], [62.092544, 91.205868, 2.0], [61.894298, 92.69271, 2.0], [61.894298, 92.69271, 0.5], [60.407456, 92.494464, 0.5], [60.605702, 91.007623, 0.5], [62.092544, 91.205868, 0.5], [62.092544, 91.205868, 2.0], [60.605702, 91.007623, 2.0], [60.407456, 92.494464, 2.0]]}]},
			"L_toe_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toe_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 0.330234, 10.118355], [4.945745, 0.275979, 10.118355], [5.0, 0.221724, 10.118355], [5.054255, 0.275979, 10.118355], [5.0, 0.330234, 10.118355], [5.0, 0.275979, 10.172605], [5.0, 0.221724, 10.118355], [5.0, 0.275979, 10.0641], [4.945745, 0.275979, 10.118355], [5.0, 0.275979, 10.172605], [5.054255, 0.275979, 10.118355], [5.0, 0.275979, 10.0641], [5.0, 0.330234, 10.118355], [5.0, 0.275979, 10.172605], [5.0, 0.275979, 5.0]]}, {"shapeName": "L_toe_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 0.330234, 5.0], [-0.118355, 0.275979, 4.945745], [-0.118355, 0.221724, 5.0], [-0.118355, 0.275979, 5.054255], [-0.118355, 0.330234, 5.0], [-0.172605, 0.275979, 5.0], [-0.118355, 0.221724, 5.0], [-0.0641, 0.275979, 5.0], [-0.118355, 0.275979, 4.945745], [-0.172605, 0.275979, 5.0], [-0.118355, 0.275979, 5.054255], [-0.0641, 0.275979, 5.0], [-0.118355, 0.330234, 5.0], [-0.172605, 0.275979, 5.0], [5.0, 0.275979, 5.0]]}, {"shapeName": "L_toe_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, -4.842376, 5.0], [5.0, -4.842376, 4.945745], [5.054255, -4.842376, 5.0], [5.0, -4.842376, 5.054255], [4.945745, -4.842376, 5.0], [5.0, -4.896626, 5.0], [5.054255, -4.842376, 5.0], [5.0, -4.788121, 5.0], [5.0, -4.842376, 4.945745], [5.0, -4.896626, 5.0], [5.0, -4.842376, 5.054255], [5.0, -4.788121, 5.0], [4.945745, -4.842376, 5.0], [5.0, -4.896626, 5.0], [5.0, 0.275979, 5.0]]}]},
			"L_loLeg_shaper_04_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_04_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[12.5, 9.942646, 0.833333], [12.55709, 9.600539, 0.793553], [12.719675, 9.310515, 0.75983], [12.96299, 9.116719, 0.737295], [13.25, 9.048669, 0.729383], [13.53701, 9.116719, 0.737295], [13.780325, 9.310515, 0.75983], [13.94291, 9.600539, 0.793553], [14.0, 9.942646, 0.833333], [13.94291, 10.284753, 0.873113], [13.780325, 10.574777, 0.906837], [13.53701, 10.768573, 0.929371], [13.25, 10.836622, 0.937284], [12.96299, 10.768573, 0.929371], [12.719675, 10.574777, 0.906837], [12.55709, 10.284753, 0.873113], [12.5, 9.942646, 0.833333], [5.0, 9.942646, 0.833333]]}]},
			"R_legBase_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 43.293541, 0.122805], [-5.0, 41.703929, 0.321506], [-5.0, 41.09675, 0.397404], [-5.0, 42.171105, 4.058909], [-5.0, 44.049446, 6.170052], [-5.0, 46.014323, 5.924442], [-5.0, 47.315204, 3.415896], [-5.0, 47.455208, -0.397404], [-5.0, 46.848029, -0.321506], [-5.0, 45.258417, -0.122805], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0]]}]},
			"C_revSpine_0_CTL": {"color": 4, "shapes": [{"shapeName": "C_revSpine_0_CTLShape", "degree": 3, "form": 2, "points": [[5.87709, 51.870166, 5.87709], [8.311455, 51.870166, 0.0], [6e-05, 51.870166, -5.87709], [0.0, 51.870166, -8.311455], [-6e-05, 51.870166, -5.87709], [-8.311455, 51.870166, 0.0], [-5.87709, 51.870166, 5.87709], [0.0, 51.870166, 8.311455]]}]},
			"L_upLeg_shaper_03_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_03_CTLShape", "degree": 1, "form": 0, "points": [[17.5, 34.275979, 1.25], [17.59515, 33.706392, 1.321198], [17.866125, 33.223519, 1.381557], [18.27165, 32.90086, 1.42189], [18.75, 32.787562, 1.436052], [19.22835, 32.90086, 1.42189], [19.633875, 33.223519, 1.381557], [19.90485, 33.706392, 1.321198], [20.0, 34.275979, 1.25], [19.90485, 34.845566, 1.178802], [19.633875, 35.328438, 1.118443], [19.22835, 35.651097, 1.07811], [18.75, 35.764396, 1.063948], [18.27165, 35.651097, 1.07811], [17.866125, 35.328438, 1.118443], [17.59515, 34.845566, 1.178802], [17.5, 34.275979, 1.25], [5.0, 34.275979, 1.25]]}]},
			"L_lwrArmRibbonMid_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lwrArmRibbonMid_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[47.628665, 93.183502, -6.337462], [47.628665, 93.983502, -6.337462], [48.192998, 91.850166, -8.256193], [47.628665, 89.71683, -6.337462], [47.628665, 90.51683, -6.337462], [46.876223, 90.51683, -3.779157], [46.876223, 87.850166, -3.779157], [47.101956, 87.850166, -4.546649], [46.5, 85.850166, -2.5], [45.898044, 87.850166, -0.453351], [46.123777, 87.850166, -1.220843], [46.123777, 90.51683, -1.220843], [45.371335, 90.51683, 1.337462], [45.371335, 89.71683, 1.337462], [44.807002, 91.850166, 3.256193], [45.371335, 93.983502, 1.337462], [45.371335, 93.183502, 1.337462], [46.123777, 93.183502, -1.220843], [46.123777, 95.850166, -1.220843], [45.898044, 95.850166, -0.453351], [46.5, 97.850166, -2.5], [47.101956, 95.850166, -4.546649], [46.876223, 95.850166, -3.779157], [46.876223, 93.183502, -3.779157], [47.628665, 93.183502, -6.337462]]}]},
			"L_upLeg_shaper_05_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_shaper_05_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 22.537211, 2.772023], [4.945745, 22.530482, 2.718187], [5.0, 22.523752, 2.664351], [5.054255, 22.530482, 2.718187], [5.0, 22.537211, 2.772023], [5.0, 22.476651, 2.724916], [5.0, 22.523752, 2.664351], [5.0, 22.584318, 2.711458], [4.945745, 22.530482, 2.718187], [5.0, 22.476651, 2.724916], [5.054255, 22.530482, 2.718187], [5.0, 22.584318, 2.711458], [5.0, 22.537211, 2.772023], [5.0, 22.476651, 2.724916], [5.0, 27.609312, 2.083333]]}, {"shapeName": "L_upLeg_shaper_05_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 27.616042, 2.137169], [-0.118355, 27.663148, 2.076604], [-0.118355, 27.602583, 2.029497], [-0.118355, 27.555476, 2.090063], [-0.118355, 27.616042, 2.137169], [-0.172605, 27.609312, 2.083333], [-0.118355, 27.602583, 2.029497], [-0.0641, 27.609312, 2.083333], [-0.118355, 27.663148, 2.076604], [-0.172605, 27.609312, 2.083333], [-0.118355, 27.555476, 2.090063], [-0.0641, 27.609312, 2.083333], [-0.118355, 27.616042, 2.137169], [-0.172605, 27.609312, 2.083333], [5.0, 27.609312, 2.083333]]}, {"shapeName": "L_upLeg_shaper_05_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 26.974458, -2.995497], [5.0, 27.028295, -3.002227], [5.054255, 26.974458, -2.995497], [5.0, 26.920622, -2.988768], [4.945745, 26.974458, -2.995497], [5.0, 26.96773, -3.049328], [5.054255, 26.974458, -2.995497], [5.0, 26.981188, -2.941661], [5.0, 27.028295, -3.002227], [5.0, 26.96773, -3.049328], [5.0, 26.920622, -2.988768], [5.0, 26.981188, -2.941661], [4.945745, 26.974458, -2.995497], [5.0, 26.96773, -3.049328], [5.0, 27.609312, 2.083333]]}]},
			"L_bendyLeg_A_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.416666, 34.49304, 2.986486], [4.066666, 34.49304, 2.986486], [5.0, 34.60157, 3.854729], [5.933334, 34.49304, 2.986486], [5.583335, 34.49304, 2.986486], [5.583334, 34.348333, 1.82883], [6.75, 34.348333, 1.82883], [6.75, 34.391745, 2.176127], [7.625, 34.275979, 1.25], [6.75, 34.160213, 0.323873], [6.75, 34.203625, 0.67117], [5.583334, 34.203625, 0.67117], [5.583334, 34.058918, -0.486486], [5.933334, 34.058918, -0.486486], [5.0, 33.950388, -1.354729], [4.066665, 34.058918, -0.486486], [4.416665, 34.058918, -0.486486], [4.416665, 34.203625, 0.67117], [3.25, 34.203625, 0.67117], [3.25, 34.160213, 0.323873], [2.375, 34.275979, 1.25], [3.25, 34.391745, 2.176127], [3.25, 34.348333, 1.82883], [4.416665, 34.348333, 1.82883], [4.416666, 34.49304, 2.986486]]}]},
			"C_revSpine_0_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_revSpine_0_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 56.988521, -0.054255], [-0.054255, 56.988521, 0.0], [0.0, 56.988521, 0.054255], [0.054255, 56.988521, 0.0], [0.0, 56.988521, -0.054255], [0.0, 57.042771, 0.0], [0.0, 56.988521, 0.054255], [0.0, 56.934266, 0.0], [-0.054255, 56.988521, 0.0], [0.0, 57.042771, 0.0], [0.054255, 56.988521, 0.0], [0.0, 56.934266, 0.0], [0.0, 56.988521, -0.054255], [0.0, 57.042771, 0.0], [0.0, 51.870166, 0.0]]}, {"shapeName": "C_revSpine_0_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 51.870166, -0.054255], [-5.118355, 51.815911, 0.0], [-5.118355, 51.870166, 0.054255], [-5.118355, 51.924421, 0.0], [-5.118355, 51.870166, -0.054255], [-5.172605, 51.870166, 0.0], [-5.118355, 51.870166, 0.054255], [-5.0641, 51.870166, 0.0], [-5.118355, 51.815911, 0.0], [-5.172605, 51.870166, 0.0], [-5.118355, 51.924421, 0.0], [-5.0641, 51.870166, 0.0], [-5.118355, 51.870166, -0.054255], [-5.172605, 51.870166, 0.0], [0.0, 51.870166, 0.0]]}, {"shapeName": "C_revSpine_0_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 51.870166, 5.118355], [0.0, 51.815911, 5.118355], [0.054255, 51.870166, 5.118355], [0.0, 51.924421, 5.118355], [-0.054255, 51.870166, 5.118355], [0.0, 51.870166, 5.172605], [0.054255, 51.870166, 5.118355], [0.0, 51.870166, 5.0641], [0.0, 51.815911, 5.118355], [0.0, 51.870166, 5.172605], [0.0, 51.924421, 5.118355], [0.0, 51.870166, 5.0641], [-0.054255, 51.870166, 5.118355], [0.0, 51.870166, 5.172605], [0.0, 51.870166, 0.0]]}]},
			"L_upLeg_shaper_02_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_02_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.25, 37.609312, 0.833333], [16.335635, 37.096684, 0.897412], [16.579512, 36.662099, 0.951735], [16.944485, 36.371706, 0.988034], [17.375, 36.269737, 1.00078], [17.805515, 36.371706, 0.988034], [18.170488, 36.662099, 0.951735], [18.414365, 37.096684, 0.897412], [18.5, 37.609312, 0.833333], [18.414365, 38.121941, 0.769255], [18.170488, 38.556526, 0.714932], [17.805515, 38.846919, 0.678632], [17.375, 38.948887, 0.665886], [16.944485, 38.846919, 0.678632], [16.579512, 38.556526, 0.714932], [16.335635, 38.121941, 0.769255], [16.25, 37.609312, 0.833333], [5.0, 37.609312, 0.833333]]}]},
			"L_upLeg_shaper_02_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_02_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[12.5, 37.609312, 0.833333], [12.55709, 37.26756, 0.876052], [12.719675, 36.977837, 0.912268], [12.96299, 36.784241, 0.936467], [13.25, 36.716262, 0.944965], [13.53701, 36.784241, 0.936467], [13.780325, 36.977837, 0.912268], [13.94291, 37.26756, 0.876052], [14.0, 37.609312, 0.833333], [13.94291, 37.951065, 0.790614], [13.780325, 38.240788, 0.754399], [13.53701, 38.434383, 0.730199], [13.25, 38.502362, 0.721702], [12.96299, 38.434383, 0.730199], [12.719675, 38.240788, 0.754399], [12.55709, 37.951065, 0.790614], [12.5, 37.609312, 0.833333], [5.0, 37.609312, 0.833333]]}]},
			"R_bendyLeg_B_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_B_CTLShape", "degree": 1, "form": 0, "points": [[-4.166665, 24.286724, 4.999977], [-3.666665, 24.286724, 4.999977], [-5.0, 24.292096, 6.249965], [-6.333335, 24.286724, 4.999977], [-5.833335, 24.286724, 4.999977], [-5.833335, 24.279561, 3.333327], [-7.5, 24.279561, 3.333327], [-7.5, 24.281709, 3.833323], [-8.75, 24.275979, 2.5], [-7.5, 24.270248, 1.166677], [-7.5, 24.272397, 1.666673], [-5.833335, 24.272397, 1.666673], [-5.833335, 24.265234, 2.3e-05], [-6.333335, 24.265234, 2.3e-05], [-5.0, 24.259862, -1.249965], [-3.666665, 24.265234, 2.3e-05], [-4.166665, 24.265234, 2.3e-05], [-4.166665, 24.272397, 1.666673], [-2.5, 24.272397, 1.666673], [-2.5, 24.270248, 1.166677], [-1.25, 24.275979, 2.5], [-2.5, 24.281709, 3.833323], [-2.5, 24.279561, 3.333327], [-4.166665, 24.279561, 3.333327], [-4.166665, 24.286724, 4.999977]]}]},
			"R_upLeg_shaper_05_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upLeg_shaper_05_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 22.537211, 2.772023], [-4.945745, 22.530482, 2.718187], [-5.0, 22.523752, 2.664351], [-5.054255, 22.530482, 2.718187], [-5.0, 22.537211, 2.772023], [-5.0, 22.476651, 2.724916], [-5.0, 22.523752, 2.664351], [-5.0, 22.584318, 2.711458], [-4.945745, 22.530482, 2.718187], [-5.0, 22.476651, 2.724916], [-5.054255, 22.530482, 2.718187], [-5.0, 22.584318, 2.711458], [-5.0, 22.537211, 2.772023], [-5.0, 22.476651, 2.724916], [-5.0, 27.609312, 2.083333]]}, {"shapeName": "R_upLeg_shaper_05_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 27.616042, 2.137169], [0.118355, 27.663148, 2.076604], [0.118355, 27.602583, 2.029497], [0.118355, 27.555476, 2.090063], [0.118355, 27.616042, 2.137169], [0.172605, 27.609312, 2.083333], [0.118355, 27.602583, 2.029497], [0.0641, 27.609312, 2.083333], [0.118355, 27.663148, 2.076604], [0.172605, 27.609312, 2.083333], [0.118355, 27.555476, 2.090063], [0.0641, 27.609312, 2.083333], [0.118355, 27.616042, 2.137169], [0.172605, 27.609312, 2.083333], [-5.0, 27.609312, 2.083333]]}, {"shapeName": "R_upLeg_shaper_05_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 26.974458, -2.995497], [-5.0, 27.028295, -3.002227], [-5.054255, 26.974458, -2.995497], [-5.0, 26.920622, -2.988768], [-4.945745, 26.974458, -2.995497], [-5.0, 26.96773, -3.049328], [-5.054255, 26.974458, -2.995497], [-5.0, 26.981188, -2.941661], [-5.0, 27.028295, -3.002227], [-5.0, 26.96773, -3.049328], [-5.0, 26.920622, -2.988768], [-5.0, 26.981188, -2.941661], [-4.945745, 26.974458, -2.995497], [-5.0, 26.96773, -3.049328], [-5.0, 27.609312, 2.083333]]}]},
			"C_neckBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neckBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 91.855498, -0.054255], [5.118355, 91.909753, 0.0], [5.118355, 91.855498, 0.054255], [5.118355, 91.801243, 0.0], [5.118355, 91.855498, -0.054255], [5.172605, 91.855498, 0.0], [5.118355, 91.855498, 0.054255], [5.0641, 91.855498, 0.0], [5.118355, 91.909753, 0.0], [5.172605, 91.855498, 0.0], [5.118355, 91.801243, 0.0], [5.0641, 91.855498, 0.0], [5.118355, 91.855498, -0.054255], [5.172605, 91.855498, 0.0], [0.0, 91.855498, 0.0]]}, {"shapeName": "C_neckBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 96.973853, -0.054255], [-0.054255, 96.973853, 0.0], [0.0, 96.973853, 0.054255], [0.054255, 96.973853, 0.0], [0.0, 96.973853, -0.054255], [0.0, 97.028103, 0.0], [0.0, 96.973853, 0.054255], [0.0, 96.919598, 0.0], [-0.054255, 96.973853, 0.0], [0.0, 97.028103, 0.0], [0.054255, 96.973853, 0.0], [0.0, 96.919598, 0.0], [0.0, 96.973853, -0.054255], [0.0, 97.028103, 0.0], [0.0, 91.855498, 0.0]]}, {"shapeName": "C_neckBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 91.909753, 5.118355], [-0.054255, 91.855498, 5.118355], [0.0, 91.801243, 5.118355], [0.054255, 91.855498, 5.118355], [0.0, 91.909753, 5.118355], [0.0, 91.855498, 5.172605], [0.0, 91.801243, 5.118355], [0.0, 91.855498, 5.0641], [-0.054255, 91.855498, 5.118355], [0.0, 91.855498, 5.172605], [0.054255, 91.855498, 5.118355], [0.0, 91.855498, 5.0641], [0.0, 91.909753, 5.118355], [0.0, 91.855498, 5.172605], [0.0, 91.855498, 0.0]]}]},
			"C_chest_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_chest_FK_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 76.850166, -5.0], [5.0, 76.850166, 5.0], [-5.0, 76.850166, 5.0], [-5.0, 76.850166, -5.0], [5.0, 76.850166, -5.0]]}]},
			"C_spineShaper_2_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_spineShaper_2_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 63.218521, -0.054255], [-0.054255, 63.218521, 0.0], [0.0, 63.218521, 0.054255], [0.054255, 63.218521, 0.0], [0.0, 63.218521, -0.054255], [0.0, 63.272771, 0.0], [0.0, 63.218521, 0.054255], [0.0, 63.164266, 0.0], [-0.054255, 63.218521, 0.0], [0.0, 63.272771, 0.0], [0.054255, 63.218521, 0.0], [0.0, 63.164266, 0.0], [0.0, 63.218521, -0.054255], [0.0, 63.272771, 0.0], [0.0, 58.100166, 0.0]]}, {"shapeName": "C_spineShaper_2_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 58.100166, -0.054255], [-5.118355, 58.045911, 0.0], [-5.118355, 58.100166, 0.054255], [-5.118355, 58.154421, 0.0], [-5.118355, 58.100166, -0.054255], [-5.172605, 58.100166, 0.0], [-5.118355, 58.100166, 0.054255], [-5.0641, 58.100166, 0.0], [-5.118355, 58.045911, 0.0], [-5.172605, 58.100166, 0.0], [-5.118355, 58.154421, 0.0], [-5.0641, 58.100166, 0.0], [-5.118355, 58.100166, -0.054255], [-5.172605, 58.100166, 0.0], [0.0, 58.100166, 0.0]]}, {"shapeName": "C_spineShaper_2_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 58.100166, 5.118355], [0.0, 58.045911, 5.118355], [0.054255, 58.100166, 5.118355], [0.0, 58.154421, 5.118355], [-0.054255, 58.100166, 5.118355], [0.0, 58.100166, 5.172605], [0.054255, 58.100166, 5.118355], [0.0, 58.100166, 5.0641], [0.0, 58.045911, 5.118355], [0.0, 58.100166, 5.172605], [0.0, 58.154421, 5.118355], [0.0, 58.100166, 5.0641], [-0.054255, 58.100166, 5.118355], [0.0, 58.100166, 5.172605], [0.0, 58.100166, 0.0]]}]},
			"C_head_right_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_right_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-4.881645, 111.850166, -5.054255], [-4.881645, 111.904421, -5.0], [-4.881645, 111.850166, -4.945745], [-4.881645, 111.795911, -5.0], [-4.881645, 111.850166, -5.054255], [-4.827395, 111.850166, -5.0], [-4.881645, 111.850166, -4.945745], [-4.9359, 111.850166, -5.0], [-4.881645, 111.904421, -5.0], [-4.827395, 111.850166, -5.0], [-4.881645, 111.795911, -5.0], [-4.9359, 111.850166, -5.0], [-4.881645, 111.850166, -5.054255], [-4.827395, 111.850166, -5.0], [-10.0, 111.850166, -5.0]]}, {"shapeName": "C_head_right_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-10.0, 116.968521, -5.054255], [-10.054255, 116.968521, -5.0], [-10.0, 116.968521, -4.945745], [-9.945745, 116.968521, -5.0], [-10.0, 116.968521, -5.054255], [-10.0, 117.022771, -5.0], [-10.0, 116.968521, -4.945745], [-10.0, 116.914266, -5.0], [-10.054255, 116.968521, -5.0], [-10.0, 117.022771, -5.0], [-9.945745, 116.968521, -5.0], [-10.0, 116.914266, -5.0], [-10.0, 116.968521, -5.054255], [-10.0, 117.022771, -5.0], [-10.0, 111.850166, -5.0]]}, {"shapeName": "C_head_right_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-10.0, 111.904421, 0.118355], [-10.054255, 111.850166, 0.118355], [-10.0, 111.795911, 0.118355], [-9.945745, 111.850166, 0.118355], [-10.0, 111.904421, 0.118355], [-10.0, 111.850166, 0.172605], [-10.0, 111.795911, 0.118355], [-10.0, 111.850166, 0.0641], [-10.054255, 111.850166, 0.118355], [-10.0, 111.850166, 0.172605], [-9.945745, 111.850166, 0.118355], [-10.0, 111.850166, 0.0641], [-10.0, 111.904421, 0.118355], [-10.0, 111.850166, 0.172605], [-10.0, 111.850166, -5.0]]}]},
			"R_shoulder_shaper_02_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_02_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-24.5, 93.600166, -1.25], [-24.564526, 93.613487, -1.267924], [-24.619228, 93.651424, -1.283119], [-24.655781, 93.708197, -1.293272], [-24.668616, 93.775166, -1.296838], [-24.655781, 93.842135, -1.293272], [-24.619228, 93.898909, -1.283119], [-24.564526, 93.936845, -1.267924], [-24.5, 93.950166, -1.25], [-24.435474, 93.936845, -1.232076], [-24.380772, 93.898909, -1.216881], [-24.344219, 93.842135, -1.206728], [-24.331384, 93.775166, -1.203162], [-24.344219, 93.708197, -1.206728], [-24.380772, 93.651424, -1.216881], [-24.435474, 93.613487, -1.232076], [-24.5, 93.600166, -1.25], [-24.5, 91.850166, -1.25]]}]},
			"C_revSpine_chest_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_revSpine_chest_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 81.968521, -0.054255], [-0.054255, 81.968521, 0.0], [0.0, 81.968521, 0.054255], [0.054255, 81.968521, 0.0], [0.0, 81.968521, -0.054255], [0.0, 82.022771, 0.0], [0.0, 81.968521, 0.054255], [0.0, 81.914266, 0.0], [-0.054255, 81.968521, 0.0], [0.0, 82.022771, 0.0], [0.054255, 81.968521, 0.0], [0.0, 81.914266, 0.0], [0.0, 81.968521, -0.054255], [0.0, 82.022771, 0.0], [0.0, 76.850166, 0.0]]}, {"shapeName": "C_revSpine_chest_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 76.850166, -0.054255], [-5.118355, 76.795911, 0.0], [-5.118355, 76.850166, 0.054255], [-5.118355, 76.904421, 0.0], [-5.118355, 76.850166, -0.054255], [-5.172605, 76.850166, 0.0], [-5.118355, 76.850166, 0.054255], [-5.0641, 76.850166, 0.0], [-5.118355, 76.795911, 0.0], [-5.172605, 76.850166, 0.0], [-5.118355, 76.904421, 0.0], [-5.0641, 76.850166, 0.0], [-5.118355, 76.850166, -0.054255], [-5.172605, 76.850166, 0.0], [0.0, 76.850166, 0.0]]}, {"shapeName": "C_revSpine_chest_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 76.850166, 5.118355], [0.0, 76.795911, 5.118355], [0.054255, 76.850166, 5.118355], [0.0, 76.904421, 5.118355], [-0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.172605], [0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.0641], [0.0, 76.795911, 5.118355], [0.0, 76.850166, 5.172605], [0.0, 76.904421, 5.118355], [0.0, 76.850166, 5.0641], [-0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.172605], [0.0, 76.850166, 0.0]]}]},
			"R_elbow_shaper_01_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_elbow_shaper_01_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-39.835136, 91.850166, -4.471565], [-39.832075, 91.861017, -4.461155], [-39.829013, 91.850166, -4.450744], [-39.832075, 91.839315, -4.461155], [-39.835136, 91.850166, -4.471565], [-39.842484, 91.850166, -4.458093], [-39.829013, 91.850166, -4.450744], [-39.821665, 91.850166, -4.464216], [-39.832075, 91.861017, -4.461155], [-39.842484, 91.850166, -4.458093], [-39.832075, 91.839315, -4.461155], [-39.821665, 91.850166, -4.464216], [-39.835136, 91.850166, -4.471565], [-39.842484, 91.850166, -4.458093], [-38.85, 91.850166, -4.75]]}, {"shapeName": "R_elbow_shaper_01_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-38.853062, 92.873837, -4.76041], [-38.83959, 92.873837, -4.753062], [-38.846938, 92.873837, -4.73959], [-38.86041, 92.873837, -4.746938], [-38.853062, 92.873837, -4.76041], [-38.85, 92.884687, -4.75], [-38.846938, 92.873837, -4.73959], [-38.85, 92.862986, -4.75], [-38.83959, 92.873837, -4.753062], [-38.85, 92.884687, -4.75], [-38.86041, 92.873837, -4.746938], [-38.85, 92.862986, -4.75], [-38.853062, 92.873837, -4.76041], [-38.85, 92.884687, -4.75], [-38.85, 91.850166, -4.75]]}, {"shapeName": "R_elbow_shaper_01_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-38.561155, 91.861017, -3.767925], [-38.550744, 91.850166, -3.770987], [-38.561155, 91.839315, -3.767925], [-38.571565, 91.850166, -3.764864], [-38.561155, 91.861017, -3.767925], [-38.558093, 91.850166, -3.757516], [-38.561155, 91.839315, -3.767925], [-38.564216, 91.850166, -3.778335], [-38.550744, 91.850166, -3.770987], [-38.558093, 91.850166, -3.757516], [-38.571565, 91.850166, -3.764864], [-38.564216, 91.850166, -3.778335], [-38.561155, 91.861017, -3.767925], [-38.558093, 91.850166, -3.757516], [-38.85, 91.850166, -4.75]]}]},
			"R_elbow_shaper_02_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_02_CTLShape", "degree": 1, "form": 0, "points": [[-42.25, 94.350166, -3.75], [-42.341782, 94.369196, -3.723005], [-42.419592, 94.423391, -3.70012], [-42.471585, 94.504496, -3.684828], [-42.489841, 94.600166, -3.679458], [-42.471585, 94.695836, -3.684828], [-42.419592, 94.776941, -3.70012], [-42.341782, 94.831136, -3.723005], [-42.25, 94.850166, -3.75], [-42.158218, 94.831136, -3.776995], [-42.080408, 94.776941, -3.79988], [-42.028415, 94.695836, -3.815172], [-42.010159, 94.600166, -3.820542], [-42.028415, 94.504496, -3.815172], [-42.080408, 94.423391, -3.79988], [-42.158218, 94.369196, -3.776995], [-42.25, 94.350166, -3.75], [-42.25, 91.850166, -3.75]]}]},
			"L_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.227054, 92.508331, -0.054255], [68.222728, 92.562413, 0.0], [68.227054, 92.508331, 0.054255], [68.231381, 92.454248, 0.0], [68.227054, 92.508331, -0.054255], [68.281132, 92.512657, 0.0], [68.227054, 92.508331, 0.054255], [68.172972, 92.504004, 0.0], [68.222728, 92.562413, 0.0], [68.281132, 92.512657, 0.0], [68.231381, 92.454248, 0.0], [68.172972, 92.504004, 0.0], [68.227054, 92.508331, -0.054255], [68.281132, 92.512657, 0.0], [63.125, 92.100166, 0.0]]}, {"shapeName": "L_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[62.716836, 97.202221, -0.054255], [62.662753, 97.197894, 0.0], [62.716836, 97.202221, 0.054255], [62.770918, 97.206547, 0.0], [62.716836, 97.202221, -0.054255], [62.712509, 97.256298, 0.0], [62.716836, 97.202221, 0.054255], [62.721162, 97.148139, 0.0], [62.662753, 97.197894, 0.0], [62.712509, 97.256298, 0.0], [62.770918, 97.206547, 0.0], [62.721162, 97.148139, 0.0], [62.716836, 97.202221, -0.054255], [62.712509, 97.256298, 0.0], [63.125, 92.100166, 0.0]]}, {"shapeName": "L_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[63.120673, 92.154249, 5.118355], [63.070918, 92.09584, 5.118355], [63.129327, 92.046084, 5.118355], [63.179082, 92.104493, 5.118355], [63.120673, 92.154249, 5.118355], [63.125, 92.100166, 5.172605], [63.129327, 92.046084, 5.118355], [63.125, 92.100166, 5.0641], [63.070918, 92.09584, 5.118355], [63.125, 92.100166, 5.172605], [63.179082, 92.104493, 5.118355], [63.125, 92.100166, 5.0641], [63.120673, 92.154249, 5.118355], [63.125, 92.100166, 5.172605], [63.125, 92.100166, 0.0]]}]},
			"R_innerBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_innerBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.618355, 0.275979, 5.054255], [2.618355, 0.330234, 5.0], [2.618355, 0.275979, 4.945745], [2.618355, 0.221724, 5.0], [2.618355, 0.275979, 5.054255], [2.672605, 0.275979, 5.0], [2.618355, 0.275979, 4.945745], [2.5641, 0.275979, 5.0], [2.618355, 0.330234, 5.0], [2.672605, 0.275979, 5.0], [2.618355, 0.221724, 5.0], [2.5641, 0.275979, 5.0], [2.618355, 0.275979, 5.054255], [2.672605, 0.275979, 5.0], [-2.5, 0.275979, 5.0]]}, {"shapeName": "R_innerBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-2.5, 5.394334, 5.054255], [-2.554255, 5.394334, 5.0], [-2.5, 5.394334, 4.945745], [-2.445745, 5.394334, 5.0], [-2.5, 5.394334, 5.054255], [-2.5, 5.448584, 5.0], [-2.5, 5.394334, 4.945745], [-2.5, 5.340079, 5.0], [-2.554255, 5.394334, 5.0], [-2.5, 5.448584, 5.0], [-2.445745, 5.394334, 5.0], [-2.5, 5.340079, 5.0], [-2.5, 5.394334, 5.054255], [-2.5, 5.448584, 5.0], [-2.5, 0.275979, 5.0]]}, {"shapeName": "R_innerBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.5, 0.330234, -0.118355], [-2.554255, 0.275979, -0.118355], [-2.5, 0.221724, -0.118355], [-2.445745, 0.275979, -0.118355], [-2.5, 0.330234, -0.118355], [-2.5, 0.275979, -0.172605], [-2.5, 0.221724, -0.118355], [-2.5, 0.275979, -0.0641], [-2.554255, 0.275979, -0.118355], [-2.5, 0.275979, -0.172605], [-2.445745, 0.275979, -0.118355], [-2.5, 0.275979, -0.0641], [-2.5, 0.330234, -0.118355], [-2.5, 0.275979, -0.172605], [-2.5, 0.275979, 5.0]]}]},
			"R_clavicle_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_clavicle_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-3.115508, 91.850166, -3.308934], [-1.279872, 91.850166, -8.662875], [-0.578719, 91.850166, -10.707904], [-1.279872, 98.503758, -8.662875], [-3.115508, 102.61591, -3.308934], [-5.384492, 102.61591, 3.308934], [-7.220128, 98.503758, 8.662875], [-7.921281, 91.850166, 10.707904], [-7.220128, 91.850166, 8.662875], [-5.384492, 91.850166, 3.308934], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0]]}]},
			"L_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_B_CTLShape", "degree": 1, "form": 0, "points": [[63.812803, 92.907587, 0.75], [62.31758, 92.787969, 0.75], [62.31758, 92.787969, -0.75], [63.812803, 92.907587, -0.75], [63.93242, 91.412364, -0.75], [62.437197, 91.292746, -0.75], [62.437197, 91.292746, 0.75], [63.93242, 91.412364, 0.75], [63.812803, 92.907587, 0.75], [63.812803, 92.907587, -0.75], [62.31758, 92.787969, -0.75], [62.437197, 91.292746, -0.75], [63.93242, 91.412364, -0.75], [63.93242, 91.412364, 0.75], [62.437197, 91.292746, 0.75], [62.31758, 92.787969, 0.75]]}]},
			"C_spineShaper_5_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_spineShaper_5_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 81.968521, -0.054255], [-0.054255, 81.968521, 0.0], [0.0, 81.968521, 0.054255], [0.054255, 81.968521, 0.0], [0.0, 81.968521, -0.054255], [0.0, 82.022771, 0.0], [0.0, 81.968521, 0.054255], [0.0, 81.914266, 0.0], [-0.054255, 81.968521, 0.0], [0.0, 82.022771, 0.0], [0.054255, 81.968521, 0.0], [0.0, 81.914266, 0.0], [0.0, 81.968521, -0.054255], [0.0, 82.022771, 0.0], [0.0, 76.850166, 0.0]]}, {"shapeName": "C_spineShaper_5_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 76.850166, -0.054255], [-5.118355, 76.795911, 0.0], [-5.118355, 76.850166, 0.054255], [-5.118355, 76.904421, 0.0], [-5.118355, 76.850166, -0.054255], [-5.172605, 76.850166, 0.0], [-5.118355, 76.850166, 0.054255], [-5.0641, 76.850166, 0.0], [-5.118355, 76.795911, 0.0], [-5.172605, 76.850166, 0.0], [-5.118355, 76.904421, 0.0], [-5.0641, 76.850166, 0.0], [-5.118355, 76.850166, -0.054255], [-5.172605, 76.850166, 0.0], [0.0, 76.850166, 0.0]]}, {"shapeName": "C_spineShaper_5_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 76.850166, 5.118355], [0.0, 76.795911, 5.118355], [0.054255, 76.850166, 5.118355], [0.0, 76.904421, 5.118355], [-0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.172605], [0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.0641], [0.0, 76.795911, 5.118355], [0.0, 76.850166, 5.172605], [0.0, 76.904421, 5.118355], [0.0, 76.850166, 5.0641], [-0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.172605], [0.0, 76.850166, 0.0]]}]},
			"R_loLeg_shaper_01_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_01_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-12.5, 20.692646, 2.083333], [-12.55709, 20.350539, 2.043553], [-12.719675, 20.060515, 2.00983], [-12.96299, 19.866719, 1.987295], [-13.25, 19.798669, 1.979383], [-13.53701, 19.866719, 1.987295], [-13.780325, 20.060515, 2.00983], [-13.94291, 20.350539, 2.043553], [-14.0, 20.692646, 2.083333], [-13.94291, 21.034753, 2.123113], [-13.780325, 21.324777, 2.156837], [-13.53701, 21.518573, 2.179371], [-13.25, 21.586622, 2.187284], [-12.96299, 21.518573, 2.179371], [-12.719675, 21.324777, 2.156837], [-12.55709, 21.034753, 2.123113], [-12.5, 20.692646, 2.083333], [-5.0, 20.692646, 2.083333]]}]},
			"R_loLeg_shaper_02_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_02_CTLShape", "degree": 1, "form": 0, "points": [[-17.5, 17.109312, 1.666667], [-17.59515, 16.539134, 1.600367], [-17.866125, 16.055761, 1.544161], [-18.27165, 15.732767, 1.506603], [-18.75, 15.619351, 1.493415], [-19.22835, 15.732767, 1.506603], [-19.633875, 16.055761, 1.544161], [-19.90485, 16.539134, 1.600367], [-20.0, 17.109312, 1.666667], [-19.90485, 17.679491, 1.732966], [-19.633875, 18.162864, 1.789173], [-19.22835, 18.485858, 1.82673], [-18.75, 18.599273, 1.839918], [-18.27165, 18.485858, 1.82673], [-17.866125, 18.162864, 1.789173], [-17.59515, 17.679491, 1.732966], [-17.5, 17.109312, 1.666667], [-5.0, 17.109312, 1.666667]]}]},
			"L_loLeg_shaper_03_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_03_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[12.5, 13.525979, 1.25], [12.55709, 13.183872, 1.21022], [12.719675, 12.893848, 1.176496], [12.96299, 12.700052, 1.153962], [13.25, 12.632002, 1.146049], [13.53701, 12.700052, 1.153962], [13.780325, 12.893848, 1.176496], [13.94291, 13.183872, 1.21022], [14.0, 13.525979, 1.25], [13.94291, 13.868086, 1.28978], [13.780325, 14.15811, 1.323504], [13.53701, 14.351906, 1.346038], [13.25, 14.419956, 1.353951], [12.96299, 14.351906, 1.346038], [12.719675, 14.15811, 1.323504], [12.55709, 13.868086, 1.28978], [12.5, 13.525979, 1.25], [5.0, 13.525979, 1.25]]}]},
			"R_shoulder_shaper_02_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_02_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-24.5, 93.350166, -1.25], [-24.555308, 93.361584, -1.265363], [-24.602196, 93.394101, -1.278388], [-24.633526, 93.442764, -1.287091], [-24.644528, 93.500166, -1.290147], [-24.633526, 93.557568, -1.287091], [-24.602196, 93.606231, -1.278388], [-24.555308, 93.638748, -1.265363], [-24.5, 93.650166, -1.25], [-24.444692, 93.638748, -1.234637], [-24.397804, 93.606231, -1.221612], [-24.366474, 93.557568, -1.212909], [-24.355472, 93.500166, -1.209853], [-24.366474, 93.442764, -1.212909], [-24.397804, 93.394101, -1.221612], [-24.444692, 93.361584, -1.234637], [-24.5, 93.350166, -1.25], [-24.5, 91.850166, -1.25]]}]},
			"R_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.227054, 92.508365, -0.054255], [-68.222728, 92.562447, -0.0], [-68.227054, 92.508365, 0.054255], [-68.231381, 92.454282, -0.0], [-68.227054, 92.508365, -0.054255], [-68.281132, 92.512691, -0.0], [-68.227054, 92.508365, 0.054255], [-68.172972, 92.504038, -0.0], [-68.222728, 92.562447, -0.0], [-68.281132, 92.512691, -0.0], [-68.231381, 92.454282, -0.0], [-68.172972, 92.504038, -0.0], [-68.227054, 92.508365, -0.054255], [-68.281132, 92.512691, -0.0], [-63.125, 92.1002, -0.0]]}, {"shapeName": "R_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-62.716836, 97.202255, -0.054255], [-62.662753, 97.197928, 0.0], [-62.716836, 97.202255, 0.054255], [-62.770918, 97.206581, 0.0], [-62.716836, 97.202255, -0.054255], [-62.712509, 97.256332, 0.0], [-62.716836, 97.202255, 0.054255], [-62.721162, 97.148173, 0.0], [-62.662753, 97.197928, 0.0], [-62.712509, 97.256332, 0.0], [-62.770918, 97.206581, 0.0], [-62.721162, 97.148173, 0.0], [-62.716836, 97.202255, -0.054255], [-62.712509, 97.256332, 0.0], [-63.125, 92.1002, -0.0]]}, {"shapeName": "R_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-63.120673, 92.154283, 5.118355], [-63.070918, 92.095874, 5.118355], [-63.129327, 92.046118, 5.118355], [-63.179082, 92.104527, 5.118355], [-63.120673, 92.154283, 5.118355], [-63.125, 92.1002, 5.172605], [-63.129327, 92.046118, 5.118355], [-63.125, 92.1002, 5.0641], [-63.070918, 92.095874, 5.118355], [-63.125, 92.1002, 5.172605], [-63.179082, 92.104527, 5.118355], [-63.125, 92.1002, 5.0641], [-63.120673, 92.154283, 5.118355], [-63.125, 92.1002, 5.172605], [-63.125, 92.1002, -0.0]]}]},
			"L_loLeg_shaper_02_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_02_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[13.75, 17.109312, 1.666667], [13.816605, 16.710188, 1.620257], [14.006287, 16.371826, 1.580912], [14.290155, 16.145731, 1.554622], [14.625, 16.06634, 1.545391], [14.959845, 16.145731, 1.554622], [15.243712, 16.371826, 1.580912], [15.433395, 16.710188, 1.620257], [15.5, 17.109312, 1.666667], [15.433395, 17.508437, 1.713077], [15.243712, 17.846798, 1.752421], [14.959845, 18.072894, 1.778711], [14.625, 18.152285, 1.787943], [14.290155, 18.072894, 1.778711], [14.006287, 17.846798, 1.752421], [13.816605, 17.508437, 1.713077], [13.75, 17.109312, 1.666667], [5.0, 17.109312, 1.666667]]}]},
			"L_shoulder_shaper_02_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_02_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[24.5, 93.600166, -1.25], [24.564526, 93.613487, -1.267924], [24.619228, 93.651424, -1.283119], [24.655781, 93.708197, -1.293272], [24.668616, 93.775166, -1.296838], [24.655781, 93.842135, -1.293272], [24.619228, 93.898909, -1.283119], [24.564526, 93.936845, -1.267924], [24.5, 93.950166, -1.25], [24.435474, 93.936845, -1.232076], [24.380772, 93.898909, -1.216881], [24.344219, 93.842135, -1.206728], [24.331384, 93.775166, -1.203162], [24.344219, 93.708197, -1.206728], [24.380772, 93.651424, -1.216881], [24.435474, 93.613487, -1.232076], [24.5, 93.600166, -1.25], [24.5, 91.850166, -1.25]]}]},
			"R_reverseBall_CTL": {"color": 20, "shapes": [{"shapeName": "R_reverseBall_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, -1.099021, 5.0], [-5.0, 2.525979, 5.0], [-5.0, 3.025979, 4.5], [-5.5, 3.025979, 5.0], [-5.0, 3.525979, 5.0], [-5.0, 3.025979, 4.5], [-4.5, 3.025979, 5.0], [-5.0, 2.525979, 5.0], [-5.0, 3.025979, 5.5], [-4.5, 3.025979, 5.0], [-5.0, 3.525979, 5.0], [-5.0, 3.025979, 5.5], [-5.5, 3.025979, 5.0], [-5.0, 2.525979, 5.0]]}]},
			"L_innerBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_innerBall_CTLShape", "degree": 1, "form": 0, "points": [[1.5, 0.275979, 5.5], [1.5, -0.224021, 5.0], [2.0, 0.275979, 5.0], [1.5, 0.275979, 5.5], [1.0, 0.275979, 5.0], [1.5, -0.224021, 5.0], [1.5, 0.275979, 4.5], [1.0, 0.275979, 5.0], [1.5, 0.775979, 5.0], [1.5, 0.275979, 5.5], [2.0, 0.275979, 5.0], [1.5, 0.275979, 4.5], [1.5, 0.775979, 5.0], [2.0, 0.275979, 5.0]]}]},
			"R_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_B_CTLShape", "degree": 1, "form": 0, "points": [[-62.722382, 91.700647, 4.783093], [-61.423344, 91.700647, 4.033093], [-61.798344, 92.999685, 3.383574], [-63.097382, 92.999685, 4.133574], [-63.746901, 92.249685, 3.008574], [-62.447863, 92.249685, 2.258574], [-62.072863, 90.950647, 2.908093], [-63.371901, 90.950647, 3.658093], [-62.722382, 91.700647, 4.783093], [-63.097382, 92.999685, 4.133574], [-61.798344, 92.999685, 3.383574], [-62.447863, 92.249685, 2.258574], [-63.746901, 92.249685, 3.008574], [-63.371901, 90.950647, 3.658093], [-62.072863, 90.950647, 2.908093], [-61.423344, 91.700647, 4.033093]]}]},
			"C_world_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_world_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 0.0, -0.054255], [5.118355, 0.054255, 0.0], [5.118355, 0.0, 0.054255], [5.118355, -0.054255, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [5.118355, 0.0, 0.054255], [5.0641, 0.0, 0.0], [5.118355, 0.054255, 0.0], [5.172605, 0.0, 0.0], [5.118355, -0.054255, 0.0], [5.0641, 0.0, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 5.118355, -0.054255], [-0.054255, 5.118355, 0.0], [0.0, 5.118355, 0.054255], [0.054255, 5.118355, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 5.118355, 0.054255], [0.0, 5.0641, 0.0], [-0.054255, 5.118355, 0.0], [0.0, 5.172605, 0.0], [0.054255, 5.118355, 0.0], [0.0, 5.0641, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 0.054255, 5.118355], [-0.054255, 0.0, 5.118355], [0.0, -0.054255, 5.118355], [0.054255, 0.0, 5.118355], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, -0.054255, 5.118355], [0.0, 0.0, 5.0641], [-0.054255, 0.0, 5.118355], [0.0, 0.0, 5.172605], [0.054255, 0.0, 5.118355], [0.0, 0.0, 5.0641], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, 0.0, 0.0]]}]},
			"R_shoulder_shaper_03_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_03_CTLShape", "degree": 1, "form": 0, "points": [[-29.0, 94.350166, -2.5], [-29.09218, 94.369196, -2.525605], [-29.170326, 94.423391, -2.547313], [-29.222544, 94.504496, -2.561818], [-29.240879, 94.600166, -2.566911], [-29.222544, 94.695836, -2.561818], [-29.170326, 94.776941, -2.547313], [-29.09218, 94.831136, -2.525605], [-29.0, 94.850166, -2.5], [-28.90782, 94.831136, -2.474395], [-28.829674, 94.776941, -2.452687], [-28.777456, 94.695836, -2.438182], [-28.759121, 94.600166, -2.433089], [-28.777456, 94.504496, -2.438182], [-28.829674, 94.423391, -2.452687], [-28.90782, 94.369196, -2.474395], [-29.0, 94.350166, -2.5], [-29.0, 91.850166, -2.5]]}]},
			"R_lwrArmTwist_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_lwrArmTwist_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-50.350097, 91.913626, -3.767178], [-48.723922, 91.913626, -4.929342], [-50.156166, 91.913626, -6.439274], [-51.935382, 91.913626, -7.532339], [-53.930854, 91.913626, -8.133055], [-56.013329, 91.913626, -8.210957], [-58.043388, 91.913626, -7.742845], [-59.877279, 91.913626, -6.78539], [-61.387212, 91.913626, -5.353146], [-62.480278, 91.913626, -3.57393], [-63.080993, 91.913626, -1.578457], [-63.158895, 91.913626, 0.504018], [-62.690783, 91.913626, 2.534077], [-61.733328, 91.913626, 4.367968], [-60.301084, 91.913626, 5.877901], [-58.521867, 91.913626, 6.970966], [-56.526395, 91.913626, 7.571682], [-54.443921, 91.913626, 7.649584], [-52.413861, 91.913626, 7.181472], [-50.57997, 91.913626, 6.224017], [-49.352434, 91.913626, 7.941665], [-46.064752, 91.913626, 1.692031], [-53.020514, 91.913626, 2.809047], [-51.742134, 91.913626, 4.597841], [-53.115736, 91.913626, 5.318473], [-54.633199, 91.913626, 5.665926], [-56.201586, 91.913626, 5.619844], [-57.700373, 91.913626, 5.155512], [-59.033694, 91.913626, 4.342611], [-60.107152, 91.913626, 3.205805], [-60.827784, 91.913626, 1.832202], [-61.175237, 91.913626, 0.314739], [-61.129155, 91.913626, -1.253649], [-60.664823, 91.913626, -2.752434], [-59.851922, 91.913626, -4.085756], [-58.715116, 91.913626, -5.159214], [-57.341513, 91.913626, -5.879846], [-55.82405, 91.913626, -6.227298], [-54.255662, 91.913626, -6.181218], [-52.756877, 91.913626, -5.716886], [-51.423555, 91.913626, -4.903984], [-50.350097, 91.913626, -3.767178]]}]},
			"C_neck_FK_A_CTL": {"color": 4, "shapes": [{"shapeName": "C_neck_FK_A_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 91.855498, 0.0], [-5.03806, 92.046838, 0.0], [-5.14645, 92.209048, 0.0], [-5.30866, 92.317438, 0.0], [-5.5, 92.355498, 0.0], [-5.69134, 92.317438, 0.0], [-5.85355, 92.209048, 0.0], [-5.96194, 92.046838, 0.0], [-6.0, 91.855498, 0.0], [-5.96194, 91.664158, 0.0], [-5.85355, 91.501948, 0.0], [-5.69134, 91.393558, 0.0], [-5.5, 91.355498, 0.0], [-5.30866, 91.393558, 0.0], [-5.14645, 91.501948, 0.0], [-5.03806, 91.664158, 0.0], [-5.0, 91.855498, 0.0], [0.0, 91.855498, 0.0]]}]},
			"R_upLeg_shaper_04_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_04_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-15.0, 30.942646, 1.666667], [-15.07612, 30.486976, 1.723625], [-15.2929, 30.100678, 1.771913], [-15.61732, 29.842551, 1.804179], [-16.0, 29.751912, 1.815508], [-16.38268, 29.842551, 1.804179], [-16.7071, 30.100678, 1.771913], [-16.92388, 30.486976, 1.723625], [-17.0, 30.942646, 1.666667], [-16.92388, 31.398316, 1.609708], [-16.7071, 31.784613, 1.561421], [-16.38268, 32.04274, 1.529155], [-16.0, 32.133379, 1.517825], [-15.61732, 32.04274, 1.529155], [-15.2929, 31.784613, 1.561421], [-15.07612, 31.398316, 1.609708], [-15.0, 30.942646, 1.666667], [-5.0, 30.942646, 1.666667]]}]},
			"C_spine_FK_1_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_spine_FK_1_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 64.350166, -5.0], [-5.0, 64.350166, 5.0], [5.0, 64.350166, 5.0], [5.0, 64.350166, -5.0], [-5.0, 64.350166, -5.0]]}]},
			"R_upLeg_shaper_02_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_02_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-12.5, 37.609312, 0.833333], [-12.55709, 37.26756, 0.876052], [-12.719675, 36.977837, 0.912268], [-12.96299, 36.784241, 0.936467], [-13.25, 36.716262, 0.944965], [-13.53701, 36.784241, 0.936467], [-13.780325, 36.977837, 0.912268], [-13.94291, 37.26756, 0.876052], [-14.0, 37.609312, 0.833333], [-13.94291, 37.951065, 0.790614], [-13.780325, 38.240788, 0.754399], [-13.53701, 38.434383, 0.730199], [-13.25, 38.502362, 0.721702], [-12.96299, 38.434383, 0.730199], [-12.719675, 38.240788, 0.754399], [-12.55709, 37.951065, 0.790614], [-12.5, 37.609312, 0.833333], [-5.0, 37.609312, 0.833333]]}]},
			"R_upLeg_FK_CTL": {"color": 13, "shapes": [{"shapeName": "R_upLeg_FK_CTLShape", "degree": 1, "form": 0, "points": [[-2.5, 41.485197, -2.170608], [-2.5, 46.446587, -2.790782], [-2.5, 47.06676, 2.170608], [-2.5, 42.105371, 2.790782], [-7.5, 42.105371, 2.790782], [-7.5, 47.06676, 2.170608], [-7.5, 46.446587, -2.790782], [-7.5, 41.485197, -2.170608], [-2.5, 41.485197, -2.170608], [-2.5, 42.105371, 2.790782], [-2.5, 47.06676, 2.170608], [-7.5, 47.06676, 2.170608], [-7.5, 42.105371, 2.790782], [-7.5, 41.485197, -2.170608], [-7.5, 46.446587, -2.790782], [-2.5, 46.446587, -2.790782]]}]},
			"L_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_A_CTLShape", "degree": 1, "form": 0, "points": [[61.894298, 92.69271, -1.75], [60.407456, 92.494464, -1.75], [60.407456, 92.494464, -3.25], [61.894298, 92.69271, -3.25], [62.092544, 91.205868, -3.25], [60.605702, 91.007623, -3.25], [60.605702, 91.007623, -1.75], [62.092544, 91.205868, -1.75], [61.894298, 92.69271, -1.75], [61.894298, 92.69271, -3.25], [60.407456, 92.494464, -3.25], [60.605702, 91.007623, -3.25], [62.092544, 91.205868, -3.25], [62.092544, 91.205868, -1.75], [60.605702, 91.007623, -1.75], [60.407456, 92.494464, -1.75]]}]},
			"L_elbow_shaper_01_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_01_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[38.85, 93.350166, -4.75], [38.905069, 93.361584, -4.733803], [38.951755, 93.394101, -4.720072], [38.982951, 93.442764, -4.710897], [38.993905, 93.500166, -4.707675], [38.982951, 93.557568, -4.710897], [38.951755, 93.606231, -4.720072], [38.905069, 93.638748, -4.733803], [38.85, 93.650166, -4.75], [38.794931, 93.638748, -4.766197], [38.748245, 93.606231, -4.779928], [38.717049, 93.557568, -4.789103], [38.706095, 93.500166, -4.792325], [38.717049, 93.442764, -4.789103], [38.748245, 93.394101, -4.779928], [38.794931, 93.361584, -4.766197], [38.85, 93.350166, -4.75], [38.85, 91.850166, -4.75]]}]},
			"R_leg_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, -2.342375, 0.054255], [-4.945745, -2.342375, -0.0], [-5.0, -2.342375, -0.054255], [-5.054255, -2.342375, -0.0], [-5.0, -2.342375, 0.054255], [-5.0, -2.396625, -0.0], [-5.0, -2.342375, -0.054255], [-5.0, -2.28812, -0.0], [-4.945745, -2.342375, -0.0], [-5.0, -2.396625, -0.0], [-5.054255, -2.342375, -0.0], [-5.0, -2.28812, -0.0], [-5.0, -2.342375, 0.054255], [-5.0, -2.396625, -0.0], [-5.0, 2.77598, 0.0]]}, {"shapeName": "R_leg_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 2.77598, 0.054255], [0.118355, 2.830235, -0.0], [0.118355, 2.77598, -0.054255], [0.118355, 2.721725, -0.0], [0.118355, 2.77598, 0.054255], [0.172605, 2.77598, -0.0], [0.118355, 2.77598, -0.054255], [0.0641, 2.77598, -0.0], [0.118355, 2.830235, -0.0], [0.172605, 2.77598, -0.0], [0.118355, 2.721725, -0.0], [0.0641, 2.77598, -0.0], [0.118355, 2.77598, 0.054255], [0.172605, 2.77598, -0.0], [-5.0, 2.77598, 0.0]]}, {"shapeName": "R_leg_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 2.77598, -5.118355], [-5.0, 2.830235, -5.118355], [-5.054255, 2.77598, -5.118355], [-5.0, 2.721725, -5.118355], [-4.945745, 2.77598, -5.118355], [-5.0, 2.77598, -5.172605], [-5.054255, 2.77598, -5.118355], [-5.0, 2.77598, -5.0641], [-5.0, 2.830235, -5.118355], [-5.0, 2.77598, -5.172605], [-5.0, 2.721725, -5.118355], [-5.0, 2.77598, -5.0641], [-4.945745, 2.77598, -5.118355], [-5.0, 2.77598, -5.172605], [-5.0, 2.77598, 0.0]]}]},
			"L_elbowRibbon_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_elbowRibbon_PIV_CTLShape", "degree": 1, "form": 0, "points": [[39.023724, 91.850166, -5.00312], [39.023642, 91.861017, -4.992269], [39.02356, 91.850166, -4.981418], [39.023642, 91.839315, -4.992269], [39.023724, 91.850166, -5.00312], [39.034491, 91.850166, -4.992187], [39.02356, 91.850166, -4.981418], [39.012791, 91.850166, -4.992351], [39.023642, 91.861017, -4.992269], [39.034491, 91.850166, -4.992187], [39.023642, 91.839315, -4.992269], [39.012791, 91.850166, -4.992351], [39.023724, 91.850166, -5.00312], [39.034491, 91.850166, -4.992187], [38.0, 91.850166, -5.0]]}, {"shapeName": "L_elbowRibbon_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[38.000082, 92.873837, -5.010851], [37.989149, 92.873837, -5.000082], [37.999918, 92.873837, -4.989149], [38.010851, 92.873837, -4.999918], [38.000082, 92.873837, -5.010851], [38.0, 92.884687, -5.0], [37.999918, 92.873837, -4.989149], [38.0, 92.862986, -5.0], [37.989149, 92.873837, -5.000082], [38.0, 92.884687, -5.0], [38.010851, 92.873837, -4.999918], [38.0, 92.862986, -5.0], [38.000082, 92.873837, -5.010851], [38.0, 92.884687, -5.0], [38.0, 91.850166, -5.0]]}, {"shapeName": "L_elbowRibbon_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[37.992269, 91.861017, -3.976358], [37.981418, 91.850166, -3.97644], [37.992269, 91.839315, -3.976358], [38.00312, 91.850166, -3.976276], [37.992269, 91.861017, -3.976358], [37.992187, 91.850166, -3.965509], [37.992269, 91.839315, -3.976358], [37.992351, 91.850166, -3.987209], [37.981418, 91.850166, -3.97644], [37.992187, 91.850166, -3.965509], [38.00312, 91.850166, -3.976276], [37.992351, 91.850166, -3.987209], [37.992269, 91.861017, -3.976358], [37.992187, 91.850166, -3.965509], [38.0, 91.850166, -5.0]]}]},
			"L_legBase_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_legBase_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 43.293541, 0.122805], [5.0, 41.703929, 0.321506], [5.0, 41.09675, 0.397404], [5.0, 42.171105, 4.058909], [5.0, 44.049446, 6.170052], [5.0, 46.014323, 5.924442], [5.0, 47.315204, 3.415896], [5.0, 47.455208, -0.397404], [5.0, 46.848029, -0.321506], [5.0, 45.258417, -0.122805], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0], [5.0, 44.275979, 0.0]]}]},
			"visibility_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "visibility_CTLShape", "degree": 3, "form": 2, "points": [[1.001108, 252.93298, 0.0], [0.5, 253.334774, 0.0], [-0.001108, 252.93298, 0.0], [0.000208, 252.93298, 0.0], [-0.001108, 252.93298, 0.0], [0.5, 252.531186, 0.0], [1.001108, 252.93298, 0.0], [1.001108, 252.93298, 0.0]]}, {"shapeName": "visibility_CTLShape1", "degree": 3, "form": 2, "points": [[0.709736, 253.142716, 0.0], [0.5, 253.229591, 0.0], [0.290264, 253.142716, 0.0], [0.203389, 252.93298, 0.0], [0.290264, 252.723244, 0.0], [0.5, 252.636369, 0.0], [0.709736, 252.723244, 0.0], [0.796611, 252.93298, 0.0]]}]},
			"L_lwrArmRibbonMid_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lwrArmRibbonMid_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[47.346499, 92.850168, -5.378097], [47.346499, 93.450168, -5.378097], [47.769748, 91.850166, -6.817145], [47.346499, 90.250164, -5.378097], [47.346499, 90.850164, -5.378097], [46.782167, 90.850164, -3.459367], [46.782167, 88.850166, -3.459367], [46.951467, 88.850166, -4.034987], [46.5, 87.350166, -2.5], [46.048533, 88.850166, -0.965013], [46.217833, 88.850166, -1.540633], [46.217833, 90.850164, -1.540633], [45.653501, 90.850164, 0.378097], [45.653501, 90.250164, 0.378097], [45.230252, 91.850166, 1.817145], [45.653501, 93.450168, 0.378097], [45.653501, 92.850168, 0.378097], [46.217833, 92.850168, -1.540633], [46.217833, 94.850166, -1.540633], [46.048533, 94.850166, -0.965013], [46.5, 96.350166, -2.5], [46.951467, 94.850166, -4.034987], [46.782167, 94.850166, -3.459367], [46.782167, 92.850168, -3.459367], [47.346499, 92.850168, -5.378097]]}]},
			"R_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-71.948456, 91.423739, -2.554255], [-71.955627, 91.477519, -2.5], [-71.948456, 91.423739, -2.445745], [-71.941286, 91.36996, -2.5], [-71.948456, 91.423739, -2.554255], [-72.00223, 91.41657, -2.5], [-71.948456, 91.423739, -2.445745], [-71.894677, 91.43091, -2.5], [-71.955627, 91.477519, -2.5], [-72.00223, 91.41657, -2.5], [-71.941286, 91.36996, -2.5], [-71.894677, 91.43091, -2.5], [-71.948456, 91.423739, -2.554255], [-72.00223, 91.41657, -2.5], [-66.875, 92.1002, -2.5]]}, {"shapeName": "R_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.551461, 97.173657, -2.554255], [-67.497682, 97.180827, -2.5], [-67.551461, 97.173657, -2.445745], [-67.60524, 97.166486, -2.5], [-67.551461, 97.173657, -2.554255], [-67.558631, 97.227431, -2.5], [-67.551461, 97.173657, -2.445745], [-67.54429, 97.119878, -2.5], [-67.497682, 97.180827, -2.5], [-67.558631, 97.227431, -2.5], [-67.60524, 97.166486, -2.5], [-67.54429, 97.119878, -2.5], [-67.551461, 97.173657, -2.554255], [-67.558631, 97.227431, -2.5], [-66.875, 92.1002, -2.5]]}, {"shapeName": "R_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-66.882171, 92.153979, 2.618355], [-66.821221, 92.107371, 2.618355], [-66.867829, 92.046421, 2.618355], [-66.928779, 92.09303, 2.618355], [-66.882171, 92.153979, 2.618355], [-66.875, 92.1002, 2.672605], [-66.867829, 92.046421, 2.618355], [-66.875, 92.1002, 2.5641], [-66.821221, 92.107371, 2.618355], [-66.875, 92.1002, 2.672605], [-66.928779, 92.09303, 2.618355], [-66.875, 92.1002, 2.5641], [-66.882171, 92.153979, 2.618355], [-66.875, 92.1002, 2.672605], [-66.875, 92.1002, -2.5]]}]},
			"R_elbow_shaper_04_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_04_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-50.75, 94.100166, -1.25], [-50.832604, 94.117293, -1.225705], [-50.902633, 94.166069, -1.205108], [-50.949426, 94.239063, -1.191345], [-50.965857, 94.325166, -1.186513], [-50.949426, 94.411269, -1.191345], [-50.902633, 94.484264, -1.205108], [-50.832604, 94.533039, -1.225705], [-50.75, 94.550166, -1.25], [-50.667396, 94.533039, -1.274295], [-50.597367, 94.484264, -1.294892], [-50.550574, 94.411269, -1.308655], [-50.534143, 94.325166, -1.313487], [-50.550574, 94.239063, -1.308655], [-50.597367, 94.166069, -1.294892], [-50.667396, 94.117293, -1.274295], [-50.75, 94.100166, -1.25], [-50.75, 91.850166, -1.25]]}]},
			"R_legBase_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 43.416345, 0.107454], [-5.0, 42.025435, 0.281318], [-5.0, 41.494154, 0.347728], [-5.0, 42.434214, 3.551545], [-5.0, 44.077763, 5.398795], [-5.0, 45.79703, 5.183887], [-5.0, 46.935301, 2.988909], [-5.0, 47.057804, -0.347728], [-5.0, 46.526522, -0.281318], [-5.0, 45.135613, -0.107454], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0]]}]},
			"L_hand_CTL": {"color": 1, "shapes": [{"shapeName": "L_hand_CTLShape", "degree": 1, "form": 0, "points": [[61.50484, 96.769691, 0.0], [61.309959, 96.804341, 0.0], [61.108885, 96.812251, 0.0], [60.918309, 96.807841, 0.0], [60.728715, 96.811936, 0.0], [60.601524, 96.821561, 0.0], [60.502054, 96.886731, 0.0], [60.419105, 97.038421, 0.0], [60.330205, 97.235506, 0.0], [60.259189, 97.455446, 0.0], [60.19234, 97.767191, 0.0], [60.159124, 98.083101, 0.0], [60.144284, 98.329011, 0.0], [60.13984, 98.522386, 0.0], [60.118595, 98.644886, 0.0], [60.096125, 98.794931, 0.0], [60.051359, 98.961146, 0.0], [60.023255, 99.109721, 0.0], [59.993294, 99.230086, 0.0], [59.94818, 99.371801, 0.0], [59.899949, 99.554816, 0.0], [59.89904, 99.696426, 0.0], [59.956685, 99.808461, 0.0], [60.02532, 99.830371, 0.0], [60.116039, 99.788861, 0.0], [60.15034, 99.681131, 0.0], [60.191114, 99.542181, 0.0], [60.244979, 99.405751, 0.0], [60.29923, 99.263511, 0.0], [60.355719, 99.090996, 0.0], [60.42089, 98.950926, 0.0], [60.47878, 98.892056, 0.0], [60.50566, 98.887436, 0.0], [60.550354, 98.974516, 0.0], [60.555219, 99.100166, 0.0], [60.522705, 99.245206, 0.0], [60.502054, 99.341981, 0.0], [60.48718, 99.488561, 0.0], [60.476329, 99.621071, 0.0], [60.453474, 99.760161, 0.0], [60.438285, 99.878251, 0.0], [60.423269, 99.978701, 0.0], [60.393974, 100.125946, 0.0], [60.369335, 100.242601, 0.0], [60.358869, 100.355686, 0.0], [60.393135, 100.460056, 0.0], [60.460124, 100.527676, 0.0], [60.55802, 100.531176, 0.0], [60.641669, 100.480461, 0.0], [60.684055, 100.368496, 0.0], [60.710794, 100.236546, 0.0], [60.736869, 100.119611, 0.0], [60.769315, 99.981921, 0.0], [60.798609, 99.854206, 0.0], [60.82045, 99.732336, 0.0], [60.837179, 99.600666, 0.0], [60.872074, 99.444496, 0.0], [60.897869, 99.338236, 0.0], [60.918974, 99.213391, 0.0], [60.98341, 99.116056, 0.0], [61.026879, 99.181996, 0.0], [61.052709, 99.355281, 0.0], [61.05845, 99.485586, 0.0], [61.054355, 99.654356, 0.0], [61.061565, 99.804576, 0.0], [61.069859, 99.936526, 0.0], [61.070839, 100.088811, 0.0], [61.06328, 100.233256, 0.0], [61.063665, 100.438356, 0.0], [61.069229, 100.587806, 0.0], [61.089495, 100.715101, 0.0], [61.164254, 100.769141, 0.0], [61.262605, 100.798086, 0.0], [61.349685, 100.768686, 0.0], [61.394835, 100.677126, 0.0], [61.406594, 100.526276, 0.0], [61.417515, 100.376791, 0.0], [61.423535, 100.252716, 0.0], [61.41272, 100.090456, 0.0], [61.411074, 99.941531, 0.0], [61.431689, 99.781861, 0.0], [61.44478, 99.703531, 0.0], [61.44128, 99.597761, 0.0], [61.446635, 99.479391, 0.0], [61.456154, 99.336031, 0.0], [61.46459, 99.164776, 0.0], [61.48538, 99.125471, 0.0], [61.53613, 99.172861, 0.0], [61.56028, 99.291791, 0.0], [61.594265, 99.448451, 0.0], [61.637104, 99.633251, 0.0], [61.665909, 99.794041, 0.0], [61.695765, 99.936386, 0.0], [61.740739, 100.069106, 0.0], [61.78918, 100.226711, 0.0], [61.827329, 100.390231, 0.0], [61.867404, 100.515951, 0.0], [61.913184, 100.615036, 0.0], [61.987665, 100.690566, 0.0], [62.044399, 100.678281, 0.0], [62.1445, 100.613321, 0.0], [62.180689, 100.464081, 0.0], [62.158045, 100.314526, 0.0], [62.139879, 100.211941, 0.0], [62.123919, 100.084121, 0.0], [62.099595, 99.948391, 0.0], [62.051609, 99.799956, 0.0], [62.030645, 99.705491, 0.0], [62.020669, 99.536406, 0.0], [62.014755, 99.426751, 0.0], [61.990884, 99.287381, 0.0], [61.970059, 99.161556, 0.0], [61.960085, 99.022221, 0.0], [61.942864, 98.811766, 0.0], [61.96166, 98.510731, 0.0], [61.998059, 98.356101, 0.0], [62.056125, 98.258031, 0.0], [62.130184, 98.151841, 0.0], [62.191015, 98.281306, 0.0], [62.288314, 98.425926, 0.0], [62.33903, 98.529421, 0.0], [62.362479, 98.646951, 0.0], [62.42009, 98.766021, 0.0], [62.51424, 98.886526, 0.0], [62.639784, 98.976686, 0.0], [62.72858, 99.003636, 0.0], [62.81447, 98.949351, 0.0], [62.829695, 98.863811, 0.0], [62.807645, 98.718911, 0.0], [62.760954, 98.625671, 0.0], [62.75448, 98.541181, 0.0], [62.751329, 98.378746, 0.0], [62.700195, 98.279311, 0.0], [62.63772, 98.199161, 0.0], [62.620255, 98.122266, 0.0], [62.60685, 98.023426, 0.0], [62.545915, 97.866486, 0.0], [62.46797, 97.528246, 0.0], [62.372875, 97.360561, 0.0], [62.24929, 97.170861, 0.0], [62.127209, 97.005661, 0.0], [62.0311, 96.883791, 0.0], [61.859355, 96.789011, 0.0], [61.702134, 96.758806, 0.0], [61.507604, 96.769446, 0.0]]}]},
			"R_legBase_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 43.53915, 0.092104], [-5.0, 42.346942, 0.24113], [-5.0, 41.891558, 0.298053], [-5.0, 42.697323, 3.044182], [-5.0, 44.10608, 4.627539], [-5.0, 45.579737, 4.443332], [-5.0, 46.555398, 2.561922], [-5.0, 46.6604, -0.298053], [-5.0, 46.205016, -0.24113], [-5.0, 45.012808, -0.092104], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0]]}]},
			"R_reverseBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_reverseBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-10.118355, 0.275979, 4.945745], [-10.118355, 0.330234, 5.0], [-10.118355, 0.275979, 5.054255], [-10.118355, 0.221724, 5.0], [-10.118355, 0.275979, 4.945745], [-10.172605, 0.275979, 5.0], [-10.118355, 0.275979, 5.054255], [-10.0641, 0.275979, 5.0], [-10.118355, 0.330234, 5.0], [-10.172605, 0.275979, 5.0], [-10.118355, 0.221724, 5.0], [-10.0641, 0.275979, 5.0], [-10.118355, 0.275979, 4.945745], [-10.172605, 0.275979, 5.0], [-5.0, 0.275979, 5.0]]}, {"shapeName": "R_reverseBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.0, 5.394334, 4.945745], [-4.945745, 5.394334, 5.0], [-5.0, 5.394334, 5.054255], [-5.054255, 5.394334, 5.0], [-5.0, 5.394334, 4.945745], [-5.0, 5.448584, 5.0], [-5.0, 5.394334, 5.054255], [-5.0, 5.340079, 5.0], [-4.945745, 5.394334, 5.0], [-5.0, 5.448584, 5.0], [-5.054255, 5.394334, 5.0], [-5.0, 5.340079, 5.0], [-5.0, 5.394334, 4.945745], [-5.0, 5.448584, 5.0], [-5.0, 0.275979, 5.0]]}, {"shapeName": "R_reverseBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-5.0, 0.330234, 10.118355], [-4.945745, 0.275979, 10.118355], [-5.0, 0.221724, 10.118355], [-5.054255, 0.275979, 10.118355], [-5.0, 0.330234, 10.118355], [-5.0, 0.275979, 10.172605], [-5.0, 0.221724, 10.118355], [-5.0, 0.275979, 10.0641], [-4.945745, 0.275979, 10.118355], [-5.0, 0.275979, 10.172605], [-5.054255, 0.275979, 10.118355], [-5.0, 0.275979, 10.0641], [-5.0, 0.330234, 10.118355], [-5.0, 0.275979, 10.172605], [-5.0, 0.275979, 5.0]]}]},
			"R_bendyLeg_C_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.416665, 13.323853, 2.988288], [-4.066666, 13.323853, 2.988288], [-5.0, 13.222789, 3.857432], [-5.933334, 13.323853, 2.988288], [-5.583335, 13.323853, 2.988288], [-5.583335, 13.458603, 1.82943], [-6.75, 13.458603, 1.82943], [-6.75, 13.418178, 2.177088], [-7.625, 13.525979, 1.25], [-6.75, 13.63378, 0.322912], [-6.75, 13.593355, 0.67057], [-5.583335, 13.593355, 0.67057], [-5.583335, 13.728106, -0.488288], [-5.933334, 13.728106, -0.488288], [-5.0, 13.829169, -1.357432], [-4.066666, 13.728106, -0.488288], [-4.416665, 13.728106, -0.488288], [-4.416665, 13.593355, 0.67057], [-3.25, 13.593355, 0.67057], [-3.25, 13.63378, 0.322912], [-2.375, 13.525979, 1.25], [-3.25, 13.418178, 2.177088], [-3.25, 13.458603, 1.82943], [-4.416665, 13.458603, 1.82943], [-4.416665, 13.323853, 2.988288]]}]},
			"L_toeTip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toeTip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.118355, 0.275979, 9.945745], [10.118355, 0.330234, 10.0], [10.118355, 0.275979, 10.054255], [10.118355, 0.221724, 10.0], [10.118355, 0.275979, 9.945745], [10.172605, 0.275979, 10.0], [10.118355, 0.275979, 10.054255], [10.0641, 0.275979, 10.0], [10.118355, 0.330234, 10.0], [10.172605, 0.275979, 10.0], [10.118355, 0.221724, 10.0], [10.0641, 0.275979, 10.0], [10.118355, 0.275979, 9.945745], [10.172605, 0.275979, 10.0], [5.0, 0.275979, 10.0]]}, {"shapeName": "L_toeTip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[5.0, 5.394334, 9.945745], [4.945745, 5.394334, 10.0], [5.0, 5.394334, 10.054255], [5.054255, 5.394334, 10.0], [5.0, 5.394334, 9.945745], [5.0, 5.448584, 10.0], [5.0, 5.394334, 10.054255], [5.0, 5.340079, 10.0], [4.945745, 5.394334, 10.0], [5.0, 5.448584, 10.0], [5.054255, 5.394334, 10.0], [5.0, 5.340079, 10.0], [5.0, 5.394334, 9.945745], [5.0, 5.448584, 10.0], [5.0, 0.275979, 10.0]]}, {"shapeName": "L_toeTip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[5.0, 0.330234, 15.118355], [4.945745, 0.275979, 15.118355], [5.0, 0.221724, 15.118355], [5.054255, 0.275979, 15.118355], [5.0, 0.330234, 15.118355], [5.0, 0.275979, 15.172605], [5.0, 0.221724, 15.118355], [5.0, 0.275979, 15.0641], [4.945745, 0.275979, 15.118355], [5.0, 0.275979, 15.172605], [5.054255, 0.275979, 15.118355], [5.0, 0.275979, 15.0641], [5.0, 0.330234, 15.118355], [5.0, 0.275979, 15.172605], [5.0, 0.275979, 10.0]]}]},
			"R_elbow_shaper_05_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_05_CTLShape", "degree": 1, "form": 0, "points": [[-54.15, 94.350166, -0.25], [-54.241782, 94.369196, -0.223005], [-54.319592, 94.423391, -0.20012], [-54.371585, 94.504496, -0.184828], [-54.389841, 94.600166, -0.179458], [-54.371585, 94.695836, -0.184828], [-54.319592, 94.776941, -0.20012], [-54.241782, 94.831136, -0.223005], [-54.15, 94.850166, -0.25], [-54.058218, 94.831136, -0.276995], [-53.980408, 94.776941, -0.29988], [-53.928415, 94.695836, -0.315172], [-53.910159, 94.600166, -0.320542], [-53.928415, 94.504496, -0.315172], [-53.980408, 94.423391, -0.29988], [-54.058218, 94.369196, -0.276995], [-54.15, 94.350166, -0.25], [-54.15, 91.850166, -0.25]]}]},
			"L_upLeg_shaper_04_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_04_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[13.75, 30.942646, 1.666667], [13.816605, 30.543934, 1.716506], [14.006287, 30.205924, 1.758757], [14.290155, 29.980063, 1.78699], [14.625, 29.900754, 1.796903], [14.959845, 29.980063, 1.78699], [15.243712, 30.205924, 1.758757], [15.433395, 30.543934, 1.716506], [15.5, 30.942646, 1.666667], [15.433395, 31.341357, 1.616828], [15.243712, 31.679367, 1.574576], [14.959845, 31.905229, 1.546344], [14.625, 31.984537, 1.53643], [14.290155, 31.905229, 1.546344], [14.006287, 31.679367, 1.574576], [13.816605, 31.341357, 1.616828], [13.75, 30.942646, 1.666667], [5.0, 30.942646, 1.666667]]}]},
			"L_shoulder_shaper_02_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_02_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[24.5, 94.100166, -1.25], [24.582962, 94.117293, -1.273045], [24.653293, 94.166069, -1.292581], [24.700289, 94.239063, -1.305636], [24.716792, 94.325166, -1.31022], [24.700289, 94.411269, -1.305636], [24.653293, 94.484264, -1.292581], [24.582962, 94.533039, -1.273045], [24.5, 94.550166, -1.25], [24.417038, 94.533039, -1.226955], [24.346707, 94.484264, -1.207419], [24.299711, 94.411269, -1.194364], [24.283208, 94.325166, -1.18978], [24.299711, 94.239063, -1.194364], [24.346707, 94.166069, -1.207419], [24.417038, 94.117293, -1.226955], [24.5, 94.100166, -1.25], [24.5, 91.850166, -1.25]]}]},
			"R_handIk_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_handIk_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-55.0, 88.323912, -3.526254], [-55.0, 91.850166, -4.986873], [-55.0, 95.37642, -3.526254], [-55.0, 96.837039, 0.0], [-55.0, 95.37642, 3.526254], [-55.0, 91.850166, 4.986873], [-55.0, 88.323912, 3.526254], [-55.0, 86.863293, -0.0]]}]},
			"C_spine_FK_chest_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_spine_FK_chest_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 76.850166, -5.0], [5.0, 76.850166, 5.0], [-5.0, 76.850166, 5.0], [-5.0, 76.850166, -5.0], [5.0, 76.850166, -5.0]]}]},
			"C_chest_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.347257, 76.850166, -5.289381], [0.0, 79.550166, -7.480309], [-6.347257, 76.850166, -5.289381], [-8.976371, 74.150166, 0.0], [-6.347257, 76.850166, 5.289381], [0.0, 79.550166, 7.480309], [6.347257, 76.850166, 5.289381], [8.976371, 74.150166, 0.0]]}]},
			"C_head_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[3.247595, 101.850166, -1.875], [0.0, 101.850166, -3.75], [-3.247595, 101.850166, -1.875], [-4.261261, 106.394854, 2.231899], [0.0, 106.394854, 5.695615], [4.261261, 106.394854, 2.231899], [3.247595, 101.850166, -1.875]]}]},
			"L_shoulder_shaper_04_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_04_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[33.5, 93.850166, -3.75], [33.573744, 93.86539, -3.770484], [33.636261, 93.908746, -3.78785], [33.678035, 93.97363, -3.799454], [33.692704, 94.050166, -3.803529], [33.678035, 94.126702, -3.799454], [33.636261, 94.191586, -3.78785], [33.573744, 94.234942, -3.770484], [33.5, 94.250166, -3.75], [33.426256, 94.234942, -3.729516], [33.363739, 94.191586, -3.71215], [33.321965, 94.126702, -3.700546], [33.307296, 94.050166, -3.696471], [33.321965, 93.97363, -3.700546], [33.363739, 93.908746, -3.71215], [33.426256, 93.86539, -3.729516], [33.5, 93.850166, -3.75], [33.5, 91.850166, -3.75]]}]},
			"R_shoulder_shaper_04_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_04_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-33.5, 93.850166, -3.75], [-33.573744, 93.86539, -3.770484], [-33.636261, 93.908746, -3.78785], [-33.678035, 93.97363, -3.799454], [-33.692704, 94.050166, -3.803529], [-33.678035, 94.126702, -3.799454], [-33.636261, 94.191586, -3.78785], [-33.573744, 94.234942, -3.770484], [-33.5, 94.250166, -3.75], [-33.426256, 94.234942, -3.729516], [-33.363739, 94.191586, -3.71215], [-33.321965, 94.126702, -3.700546], [-33.307296, 94.050166, -3.696471], [-33.321965, 93.97363, -3.700546], [-33.363739, 93.908746, -3.71215], [-33.426256, 93.86539, -3.729516], [-33.5, 93.850166, -3.75], [-33.5, 91.850166, -3.75]]}]},
			"L_reverseBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_reverseBall_CTLShape", "degree": 1, "form": 0, "points": [[5.0, -1.099021, 5.0], [5.0, 2.525979, 5.0], [5.0, 3.025979, 4.5], [5.5, 3.025979, 5.0], [5.0, 3.525979, 5.0], [5.0, 3.025979, 4.5], [4.5, 3.025979, 5.0], [5.0, 2.525979, 5.0], [5.0, 3.025979, 5.5], [4.5, 3.025979, 5.0], [5.0, 3.525979, 5.0], [5.0, 3.025979, 5.5], [5.5, 3.025979, 5.0], [5.0, 2.525979, 5.0]]}]},
			"L_scapulaTarget_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_scapulaTarget_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 91.850166, -15.010851], [1.023671, 91.861017, -15.0], [1.023671, 91.850166, -14.989149], [1.023671, 91.839315, -15.0], [1.023671, 91.850166, -15.010851], [1.034521, 91.850166, -15.0], [1.023671, 91.850166, -14.989149], [1.01282, 91.850166, -15.0], [1.023671, 91.861017, -15.0], [1.034521, 91.850166, -15.0], [1.023671, 91.839315, -15.0], [1.01282, 91.850166, -15.0], [1.023671, 91.850166, -15.010851], [1.034521, 91.850166, -15.0], [0.0, 91.850166, -15.0]]}, {"shapeName": "L_scapulaTarget_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 92.873837, -15.010851], [-0.010851, 92.873837, -15.0], [0.0, 92.873837, -14.989149], [0.010851, 92.873837, -15.0], [0.0, 92.873837, -15.010851], [0.0, 92.884687, -15.0], [0.0, 92.873837, -14.989149], [0.0, 92.862986, -15.0], [-0.010851, 92.873837, -15.0], [0.0, 92.884687, -15.0], [0.010851, 92.873837, -15.0], [0.0, 92.862986, -15.0], [0.0, 92.873837, -15.010851], [0.0, 92.884687, -15.0], [0.0, 91.850166, -15.0]]}, {"shapeName": "L_scapulaTarget_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 91.861017, -13.976329], [-0.010851, 91.850166, -13.976329], [0.0, 91.839315, -13.976329], [0.010851, 91.850166, -13.976329], [0.0, 91.861017, -13.976329], [0.0, 91.850166, -13.965479], [0.0, 91.839315, -13.976329], [0.0, 91.850166, -13.98718], [-0.010851, 91.850166, -13.976329], [0.0, 91.850166, -13.965479], [0.010851, 91.850166, -13.976329], [0.0, 91.850166, -13.98718], [0.0, 91.861017, -13.976329], [0.0, 91.850166, -13.965479], [0.0, 91.850166, -15.0]]}]},
			"R_elbow_shaper_04_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_04_CTLShape", "degree": 1, "form": 0, "points": [[-50.75, 94.350166, -1.25], [-50.841782, 94.369196, -1.223005], [-50.919592, 94.423391, -1.20012], [-50.971585, 94.504496, -1.184828], [-50.989841, 94.600166, -1.179458], [-50.971585, 94.695836, -1.184828], [-50.919592, 94.776941, -1.20012], [-50.841782, 94.831136, -1.223005], [-50.75, 94.850166, -1.25], [-50.658218, 94.831136, -1.276995], [-50.580408, 94.776941, -1.29988], [-50.528415, 94.695836, -1.315172], [-50.510159, 94.600166, -1.320542], [-50.528415, 94.504496, -1.315172], [-50.580408, 94.423391, -1.29988], [-50.658218, 94.369196, -1.276995], [-50.75, 94.350166, -1.25], [-50.75, 91.850166, -1.25]]}]},
			"L_clavicle_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_clavicle_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [3.25732, 91.850166, -2.895317], [1.651138, 91.850166, -7.580015], [1.037629, 91.850166, -9.369416], [1.651138, 97.672059, -7.580015], [3.25732, 101.270192, -2.895317], [5.24268, 101.270192, 2.895317], [6.848862, 97.672059, 7.580015], [7.462371, 91.850166, 9.369416], [6.848862, 91.850166, 7.580015], [5.24268, 91.850166, 2.895317], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0]]}]},
			"L_elbowFk_CTL": {"color": 6, "shapes": [{"shapeName": "L_elbowFk_CTLShape", "degree": 1, "form": 0, "points": [[39.692998, 94.350166, -1.89617], [34.89617, 94.350166, -3.307002], [36.307002, 94.350166, -8.10383], [41.10383, 94.350166, -6.692998], [41.10383, 89.350166, -6.692998], [36.307002, 89.350166, -8.10383], [34.89617, 89.350166, -3.307002], [39.692998, 89.350166, -1.89617], [39.692998, 94.350166, -1.89617], [41.10383, 94.350166, -6.692998], [36.307002, 94.350166, -8.10383], [36.307002, 89.350166, -8.10383], [41.10383, 89.350166, -6.692998], [39.692998, 89.350166, -1.89617], [34.89617, 89.350166, -3.307002], [34.89617, 94.350166, -3.307002]]}]},
			"C_midNeck_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[5.642006, 96.850166, -4.701672], [0.0, 96.850166, -6.649164], [-5.642006, 96.850166, -4.701672], [-7.978997, 96.850166, 0.0], [-5.642006, 96.850166, 4.701672], [0.0, 96.850166, 6.649164], [5.642006, 96.850166, 4.701672], [7.978997, 96.850166, 0.0]]}]},
			"L_loLeg_shaper_01_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_01_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[15.0, 20.692646, 2.083333], [15.07612, 20.236503, 2.030293], [15.2929, 19.849804, 1.985329], [15.61732, 19.591409, 1.955283], [16.0, 19.500677, 1.944732], [16.38268, 19.591409, 1.955283], [16.7071, 19.849804, 1.985329], [16.92388, 20.236503, 2.030293], [17.0, 20.692646, 2.083333], [16.92388, 21.148788, 2.136373], [16.7071, 21.535487, 2.181338], [16.38268, 21.793882, 2.211384], [16.0, 21.884614, 2.221934], [15.61732, 21.793882, 2.211384], [15.2929, 21.535487, 2.181338], [15.07612, 21.148788, 2.136373], [15.0, 20.692646, 2.083333], [5.0, 20.692646, 2.083333]]}]},
			"L_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[65.318379, 92.276782, 5.576815], [65.274612, 92.256623, 5.636525], [65.291252, 92.18281, 5.623801], [65.335019, 92.202968, 5.564091], [65.318379, 92.276782, 5.576815], [65.347793, 92.23382, 5.633168], [65.291252, 92.18281, 5.623801], [65.261834, 92.225772, 5.567444], [65.274612, 92.256623, 5.636525], [65.347793, 92.23382, 5.633168], [65.335019, 92.202968, 5.564091], [65.261834, 92.225772, 5.567444], [65.318379, 92.276782, 5.576815], [65.347793, 92.23382, 5.633168], [61.25, 91.850166, 2.5]]}, {"shapeName": "L_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[58.414234, 94.428016, 5.893173], [58.357689, 94.377006, 5.883802], [58.387106, 94.334044, 5.940159], [58.443651, 94.385054, 5.949529], [58.414234, 94.428016, 5.893173], [58.37047, 94.407855, 5.95288], [58.387106, 94.334044, 5.940159], [58.430873, 94.354203, 5.880449], [58.357689, 94.377006, 5.883802], [58.37047, 94.407855, 5.95288], [58.443651, 94.385054, 5.949529], [58.430873, 94.354203, 5.880449], [58.414234, 94.428016, 5.893173], [58.37047, 94.407855, 5.95288], [61.25, 91.850166, 2.5]]}, {"shapeName": "L_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[59.940208, 87.444368, 4.75253], [59.92743, 87.413517, 4.683449], [60.000614, 87.390713, 4.680096], [60.013393, 87.421565, 4.749176], [59.940208, 87.444368, 4.75253], [59.956849, 87.370559, 4.739804], [60.000614, 87.390713, 4.680096], [59.983975, 87.464527, 4.69282], [59.92743, 87.413517, 4.683449], [59.956849, 87.370559, 4.739804], [60.013393, 87.421565, 4.749176], [59.983975, 87.464527, 4.69282], [59.940208, 87.444368, 4.75253], [59.956849, 87.370559, 4.739804], [61.25, 91.850166, 2.5]]}]},
			"L_outterBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_outterBall_CTLShape", "degree": 1, "form": 0, "points": [[8.5, 0.275979, 5.5], [8.5, -0.224021, 5.0], [9.0, 0.275979, 5.0], [8.5, 0.275979, 5.5], [8.0, 0.275979, 5.0], [8.5, -0.224021, 5.0], [8.5, 0.275979, 4.5], [8.0, 0.275979, 5.0], [8.5, 0.775979, 5.0], [8.5, 0.275979, 5.5], [9.0, 0.275979, 5.0], [8.5, 0.275979, 4.5], [8.5, 0.775979, 5.0], [9.0, 0.275979, 5.0]]}]},
			"L_shoulderFk_CTL": {"color": 6, "shapes": [{"shapeName": "L_shoulderFk_CTLShape", "degree": 1, "form": 0, "points": [[18.260315, 94.350166, 3.077904], [18.260315, 89.350166, 3.077904], [16.922096, 89.350166, -1.739685], [16.922096, 94.350166, -1.739685], [21.739685, 94.350166, -3.077904], [21.739685, 89.350166, -3.077904], [23.077904, 89.350166, 1.739685], [23.077904, 94.350166, 1.739685], [18.260315, 94.350166, 3.077904], [16.922096, 94.350166, -1.739685], [16.922096, 89.350166, -1.739685], [21.739685, 89.350166, -3.077904], [21.739685, 94.350166, -3.077904], [23.077904, 94.350166, 1.739685], [23.077904, 89.350166, 1.739685], [18.260315, 89.350166, 3.077904]]}]},
			"C_spineShaper_5_CTL": {"color": 4, "shapes": [{"shapeName": "C_spineShaper_5_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 76.850166, -7.5], [0.0, 77.137176, -7.55709], [0.0, 77.380491, -7.719675], [0.0, 77.543076, -7.96299], [0.0, 77.600166, -8.25], [0.0, 77.543076, -8.53701], [0.0, 77.380491, -8.780325], [0.0, 77.137176, -8.94291], [0.0, 76.850166, -9.0], [0.0, 76.563156, -8.94291], [0.0, 76.319841, -8.780325], [0.0, 76.157256, -8.53701], [0.0, 76.100166, -8.25], [0.0, 76.157256, -7.96299], [0.0, 76.319841, -7.719675], [0.0, 76.563156, -7.55709], [0.0, 76.850166, -7.5], [0.0, 76.850166, 0.0]]}]},
			"R_elbowUpVectorIk_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_elbowUpVectorIk_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-36.976329, 91.8502, 15.010851], [-36.976329, 91.861051, 15.0], [-36.976329, 91.8502, 14.989149], [-36.976329, 91.839349, 15.0], [-36.976329, 91.8502, 15.010851], [-36.965479, 91.8502, 15.0], [-36.976329, 91.8502, 14.989149], [-36.98718, 91.8502, 15.0], [-36.976329, 91.861051, 15.0], [-36.965479, 91.8502, 15.0], [-36.976329, 91.839349, 15.0], [-36.98718, 91.8502, 15.0], [-36.976329, 91.8502, 15.010851], [-36.965479, 91.8502, 15.0], [-38.0, 91.8502, 15.0]]}, {"shapeName": "R_elbowUpVectorIk_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-38.0, 92.873871, 15.010851], [-38.010851, 92.873871, 15.0], [-38.0, 92.873871, 14.989149], [-37.989149, 92.873871, 15.0], [-38.0, 92.873871, 15.010851], [-38.0, 92.884721, 15.0], [-38.0, 92.873871, 14.989149], [-38.0, 92.86302, 15.0], [-38.010851, 92.873871, 15.0], [-38.0, 92.884721, 15.0], [-37.989149, 92.873871, 15.0], [-38.0, 92.86302, 15.0], [-38.0, 92.873871, 15.010851], [-38.0, 92.884721, 15.0], [-38.0, 91.8502, 15.0]]}, {"shapeName": "R_elbowUpVectorIk_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-38.0, 91.861051, 13.976329], [-38.010851, 91.8502, 13.976329], [-38.0, 91.839349, 13.976329], [-37.989149, 91.8502, 13.976329], [-38.0, 91.861051, 13.976329], [-38.0, 91.8502, 13.965479], [-38.0, 91.839349, 13.976329], [-38.0, 91.8502, 13.98718], [-38.010851, 91.8502, 13.976329], [-38.0, 91.8502, 13.965479], [-37.989149, 91.8502, 13.976329], [-38.0, 91.8502, 13.98718], [-38.0, 91.861051, 13.976329], [-38.0, 91.8502, 13.965479], [-38.0, 91.8502, 15.0]]}]},
			"C_cog_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-13.5, 49.350166, -13.5], [-13.5, 49.350166, 13.5], [13.5, 49.350166, 13.5], [13.5, 49.350166, -13.5], [-13.5, 49.350166, -13.5]]}]},
			"L_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_A_CTLShape", "degree": 1, "form": 0, "points": [[61.894298, 92.69271, -0.5], [60.407456, 92.494464, -0.5], [60.407456, 92.494464, -2.0], [61.894298, 92.69271, -2.0], [62.092544, 91.205868, -2.0], [60.605702, 91.007623, -2.0], [60.605702, 91.007623, -0.5], [62.092544, 91.205868, -0.5], [61.894298, 92.69271, -0.5], [61.894298, 92.69271, -2.0], [60.407456, 92.494464, -2.0], [60.605702, 91.007623, -2.0], [62.092544, 91.205868, -2.0], [62.092544, 91.205868, -0.5], [60.605702, 91.007623, -0.5], [60.407456, 92.494464, -0.5]]}]},
			"R_shoulder_shaper_01_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_01_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-20.9, 93.350166, -0.25], [-20.955308, 93.361584, -0.265363], [-21.002196, 93.394101, -0.278388], [-21.033526, 93.442764, -0.287091], [-21.044528, 93.500166, -0.290147], [-21.033526, 93.557568, -0.287091], [-21.002196, 93.606231, -0.278388], [-20.955308, 93.638748, -0.265363], [-20.9, 93.650166, -0.25], [-20.844692, 93.638748, -0.234637], [-20.797804, 93.606231, -0.221612], [-20.766474, 93.557568, -0.212909], [-20.755472, 93.500166, -0.209853], [-20.766474, 93.442764, -0.212909], [-20.797804, 93.394101, -0.221612], [-20.844692, 93.361584, -0.234637], [-20.9, 93.350166, -0.25], [-20.9, 91.850166, -0.25]]}]},
			"L_shoulder_shaper_02_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_shoulder_shaper_02_PIV_CTLShape", "degree": 1, "form": 0, "points": [[25.483421, 91.850166, -1.534434], [25.486325, 91.861017, -1.523979], [25.48923, 91.850166, -1.513524], [25.486325, 91.839315, -1.523979], [25.483421, 91.850166, -1.534434], [25.49678, 91.850166, -1.526883], [25.48923, 91.850166, -1.513524], [25.47587, 91.850166, -1.521075], [25.486325, 91.861017, -1.523979], [25.49678, 91.850166, -1.526883], [25.486325, 91.839315, -1.523979], [25.47587, 91.850166, -1.521075], [25.483421, 91.850166, -1.534434], [25.49678, 91.850166, -1.526883], [24.5, 91.850166, -1.25]]}, {"shapeName": "L_shoulder_shaper_02_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[24.497096, 92.873837, -1.260455], [24.489545, 92.873837, -1.247096], [24.502904, 92.873837, -1.239545], [24.510455, 92.873837, -1.252904], [24.497096, 92.873837, -1.260455], [24.5, 92.884687, -1.25], [24.502904, 92.873837, -1.239545], [24.5, 92.862986, -1.25], [24.489545, 92.873837, -1.247096], [24.5, 92.884687, -1.25], [24.510455, 92.873837, -1.252904], [24.5, 92.862986, -1.25], [24.497096, 92.873837, -1.260455], [24.5, 92.884687, -1.25], [24.5, 91.850166, -1.25]]}, {"shapeName": "L_shoulder_shaper_02_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[24.773979, 91.861017, -0.263675], [24.763524, 91.850166, -0.26077], [24.773979, 91.839315, -0.263675], [24.784434, 91.850166, -0.266579], [24.773979, 91.861017, -0.263675], [24.776883, 91.850166, -0.25322], [24.773979, 91.839315, -0.263675], [24.771075, 91.850166, -0.27413], [24.763524, 91.850166, -0.26077], [24.776883, 91.850166, -0.25322], [24.784434, 91.850166, -0.266579], [24.771075, 91.850166, -0.27413], [24.773979, 91.861017, -0.263675], [24.776883, 91.850166, -0.25322], [24.5, 91.850166, -1.25]]}]},
			"L_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_C_CTLShape", "degree": 1, "form": 0, "points": [[64.30669, 91.640871, 5.57824], [62.925674, 91.752126, 5.003421], [63.300674, 93.051164, 4.353902], [64.68169, 92.939909, 4.928721], [65.131323, 92.198207, 3.704912], [63.750307, 92.309462, 3.130093], [63.375307, 91.010424, 3.779612], [64.756323, 90.899168, 4.354431], [64.30669, 91.640871, 5.57824], [64.68169, 92.939909, 4.928721], [63.300674, 93.051164, 4.353902], [63.750307, 92.309462, 3.130093], [65.131323, 92.198207, 3.704912], [64.756323, 90.899168, 4.354431], [63.375307, 91.010424, 3.779612], [62.925674, 91.752126, 5.003421]]}]},
			"R_legEnd_FK_CTL": {"color": 13, "shapes": [{"shapeName": "R_legEnd_FK_CTLShape", "degree": 1, "form": 0, "points": [[-2.5, 0.581463, -2.772021], [-2.5, 5.548, -2.194516], [-2.5, 4.970495, 2.772021], [-2.5, 0.003958, 2.194516], [-7.5, 0.003958, 2.194516], [-7.5, 4.970495, 2.772021], [-7.5, 5.548, -2.194516], [-7.5, 0.581463, -2.772021], [-2.5, 0.581463, -2.772021], [-2.5, 0.003958, 2.194516], [-2.5, 4.970495, 2.772021], [-7.5, 4.970495, 2.772021], [-7.5, 0.003958, 2.194516], [-7.5, 0.581463, -2.772021], [-7.5, 5.548, -2.194516], [-2.5, 5.548, -2.194516]]}]},
			"R_shoulder_shaper_03_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_03_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-29.0, 93.850166, -2.5], [-29.073744, 93.86539, -2.520484], [-29.136261, 93.908746, -2.53785], [-29.178035, 93.97363, -2.549454], [-29.192704, 94.050166, -2.553529], [-29.178035, 94.126702, -2.549454], [-29.136261, 94.191586, -2.53785], [-29.073744, 94.234942, -2.520484], [-29.0, 94.250166, -2.5], [-28.926256, 94.234942, -2.479516], [-28.863739, 94.191586, -2.46215], [-28.821965, 94.126702, -2.450546], [-28.807296, 94.050166, -2.446471], [-28.821965, 93.97363, -2.450546], [-28.863739, 93.908746, -2.46215], [-28.926256, 93.86539, -2.479516], [-29.0, 93.850166, -2.5], [-29.0, 91.850166, -2.5]]}]},
			"L_loLeg_shaper_04_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_04_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[15.0, 9.942646, 0.833333], [15.07612, 9.486503, 0.780293], [15.2929, 9.099805, 0.735329], [15.61732, 8.841409, 0.705283], [16.0, 8.750677, 0.694732], [16.38268, 8.841409, 0.705283], [16.7071, 9.099805, 0.735329], [16.92388, 9.486503, 0.780293], [17.0, 9.942646, 0.833333], [16.92388, 10.398788, 0.886373], [16.7071, 10.785487, 0.931338], [16.38268, 11.043882, 0.961384], [16.0, 11.134615, 0.971934], [15.61732, 11.043882, 0.961384], [15.2929, 10.785487, 0.931338], [15.07612, 10.398788, 0.886373], [15.0, 9.942646, 0.833333], [5.0, 9.942646, 0.833333]]}]},
			"L_shoulder_shaper_05_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_05_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[37.1, 93.850166, -4.75], [37.173744, 93.86539, -4.770484], [37.236261, 93.908746, -4.78785], [37.278035, 93.97363, -4.799454], [37.292704, 94.050166, -4.803529], [37.278035, 94.126702, -4.799454], [37.236261, 94.191586, -4.78785], [37.173744, 94.234942, -4.770484], [37.1, 94.250166, -4.75], [37.026256, 94.234942, -4.729516], [36.963739, 94.191586, -4.71215], [36.921965, 94.126702, -4.700546], [36.907296, 94.050166, -4.696471], [36.921965, 93.97363, -4.700546], [36.963739, 93.908746, -4.71215], [37.026256, 93.86539, -4.729516], [37.1, 93.850166, -4.75], [37.1, 91.850166, -4.75]]}]},
			"world_B_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -28.885], [12.8325, 0.0, -16.04], [9.62, 0.0, -16.04], [9.62, 0.0, -9.6175], [16.0425, 0.0, -9.6175], [16.0425, 0.0, -12.83], [28.885, 0.0, 0.0], [16.04, 0.0, 12.8325], [16.04, 0.0, 9.62], [9.6175, 0.0, 9.62], [9.6175, 0.0, 16.0425], [12.83, 0.0, 16.0425], [0.0, 0.0, 28.885], [-12.8325, 0.0, 16.04], [-9.62, 0.0, 16.04], [-9.62, 0.0, 9.6175], [-16.0425, 0.0, 9.6175], [-16.0425, 0.0, 12.83], [-28.885, 0.0, 0.0], [-16.04, 0.0, -12.8325], [-16.04, 0.0, -9.62], [-9.6175, 0.0, -9.62], [-9.6175, 0.0, -16.0425], [-12.83, 0.0, -16.0425], [0.0, 0.0, -28.885], [2.515, 0.035, -26.415], [2.295, 0.0, -26.18], [2.295, 0.0, -25.22], [2.095, 0.0, -25.22], [2.1075, 0.0, -26.1875], [1.965, 0.0, -26.115], [1.97, 0.0, -25.695], [1.7675, 0.0, -25.695], [1.7675, 0.0, -26.115], [1.6425, 0.0, -26.1875], [1.6425, 0.0, -25.205], [1.44, 0.0, -25.205], [1.44, 0.0, -26.2125], [1.6025, 0.0, -26.375], [1.8525, 0.0, -26.25], [2.1275, 0.0, -26.375], [2.295, 0.0, -26.185], [2.1275, 0.0, -26.375], [1.855, 0.0, -26.2525], [1.6025, 0.0, -26.3725], [1.115, 0.0, -26.375], [1.28, 0.0, -26.2125], [1.28, 0.0, -25.37], [1.115, 0.0, -25.205], [0.5875, 0.0, -25.205], [0.425, 0.0, -25.37], [0.425, 0.0, -26.2125], [0.5875, 0.0, -26.375], [1.115, 0.0, -26.375], [1.0525, 0.0, -26.1875], [1.0775, 0.0, -25.4125], [0.625, 0.0, -25.4175], [0.6275, 0.0, -26.1875], [1.055, 0.0, -26.1925], [1.115, 0.0, -26.375], [0.5875, 0.0, -26.375], [0.25, 0.0, -26.375], [0.2625, 0.0, -25.205], [-0.3075, 0.0, -25.205], [-0.4725, 0.0, -25.37], [-0.4725, 0.0, -25.7225], [-0.305, 0.0, -25.885], [-0.295, 0.0, -25.8975], [-0.6225, 0.0, -26.37], [-0.6225, 0.0, -26.375], [-0.3875, 0.0, -26.375], [-0.06, 0.0, -25.9], [0.0625, 0.0, -25.9], [0.0625, 0.0, -25.4], [-0.2525, 0.0, -25.4], [-0.255, 0.0, -25.6975], [0.0625, 0.0, -25.6975], [0.0625, 0.0, -26.375], [0.25, 0.0, -26.375], [-1.6075, 0.0, -26.375], [-1.6075, 0.0, -26.1875], [-0.9525, 0.0, -26.185], [-0.9525, 0.0, -25.205], [-0.75, 0.0, -25.205], [-0.75, 0.0, -26.375], [-2.46, 0.0, -26.375], [-2.61, 0.0, -26.2125], [-2.6225, 0.0, -25.37], [-2.46, 0.0, -25.205], [-1.7675, 0.0, -25.205], [-1.7675, 0.0, -26.375], [-1.9725, 0.0, -26.1875], [-1.9675, 0.0, -25.395], [-2.395, 0.0, -25.395], [-2.39, 0.0, -26.1825], [-1.965, 0.0, -26.1925], [-1.7625, 0.0, -26.375]]}]},
			"world_C_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -25.274375], [11.228437, 0.0, -14.035], [8.4175, 0.0, -14.035], [8.4175, 0.0, -8.415312], [14.037187, 0.0, -8.415312], [14.037187, 0.0, -11.22625], [25.274375, 0.0, 0.0], [14.035, 0.0, 11.228437], [14.035, 0.0, 8.4175], [8.415312, 0.0, 8.4175], [8.415312, 0.0, 14.037187], [11.22625, 0.0, 14.037187], [0.0, 0.0, 25.274375], [-11.228437, 0.0, 14.035], [-8.4175, 0.0, 14.035], [-8.4175, 0.0, 8.415312], [-14.037187, 0.0, 8.415312], [-14.037187, 0.0, 11.22625], [-25.274375, 0.0, 0.0], [-14.035, 0.0, -11.228437], [-14.035, 0.0, -8.4175], [-8.415312, 0.0, -8.4175], [-8.415312, 0.0, -14.037187], [-11.22625, 0.0, -14.037187], [0.0, 0.0, -25.274375], [2.200625, 0.030625, -23.113125], [2.008125, 0.0, -22.9075], [2.008125, 0.0, -22.0675], [1.833125, 0.0, -22.0675], [1.844062, 0.0, -22.914062], [1.719375, 0.0, -22.850625], [1.72375, 0.0, -22.483125], [1.546562, 0.0, -22.483125], [1.546562, 0.0, -22.850625], [1.437188, 0.0, -22.914062], [1.437188, 0.0, -22.054375], [1.26, 0.0, -22.054375], [1.26, 0.0, -22.935937], [1.402188, 0.0, -23.078125], [1.620937, 0.0, -22.96875], [1.861563, 0.0, -23.078125], [2.008125, 0.0, -22.911875], [1.861563, 0.0, -23.078125], [1.623125, 0.0, -22.970938], [1.402188, 0.0, -23.075937], [0.975625, 0.0, -23.078125], [1.12, 0.0, -22.935937], [1.12, 0.0, -22.19875], [0.975625, 0.0, -22.054375], [0.514062, 0.0, -22.054375], [0.371875, 0.0, -22.19875], [0.371875, 0.0, -22.935937], [0.514062, 0.0, -23.078125], [0.975625, 0.0, -23.078125], [0.920937, 0.0, -22.914062], [0.942812, 0.0, -22.235937], [0.546875, 0.0, -22.240312], [0.549062, 0.0, -22.914062], [0.923125, 0.0, -22.918437], [0.975625, 0.0, -23.078125], [0.514062, 0.0, -23.078125], [0.21875, 0.0, -23.078125], [0.229687, 0.0, -22.054375], [-0.269062, 0.0, -22.054375], [-0.413438, 0.0, -22.19875], [-0.413438, 0.0, -22.507188], [-0.266875, 0.0, -22.649375], [-0.258125, 0.0, -22.660312], [-0.544687, 0.0, -23.07375], [-0.544687, 0.0, -23.078125], [-0.339062, 0.0, -23.078125], [-0.0525, 0.0, -22.6625], [0.054688, 0.0, -22.6625], [0.054688, 0.0, -22.225], [-0.220937, 0.0, -22.225], [-0.223125, 0.0, -22.485312], [0.054688, 0.0, -22.485312], [0.054688, 0.0, -23.078125], [0.21875, 0.0, -23.078125], [-1.406562, 0.0, -23.078125], [-1.406562, 0.0, -22.914062], [-0.833437, 0.0, -22.911875], [-0.833437, 0.0, -22.054375], [-0.65625, 0.0, -22.054375], [-0.65625, 0.0, -23.078125], [-2.1525, 0.0, -23.078125], [-2.28375, 0.0, -22.935937], [-2.294688, 0.0, -22.19875], [-2.1525, 0.0, -22.054375], [-1.546562, 0.0, -22.054375], [-1.546562, 0.0, -23.078125], [-1.725937, 0.0, -22.914062], [-1.721562, 0.0, -22.220625], [-2.095625, 0.0, -22.220625], [-2.09125, 0.0, -22.909687], [-1.719375, 0.0, -22.918437], [-1.542187, 0.0, -23.078125]]}]},
			"L_arm_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[56.023671, 91.850166, -0.010851], [56.023671, 91.861017, 0.0], [56.023671, 91.850166, 0.010851], [56.023671, 91.839315, 0.0], [56.023671, 91.850166, -0.010851], [56.034521, 91.850166, 0.0], [56.023671, 91.850166, 0.010851], [56.01282, 91.850166, 0.0], [56.023671, 91.861017, 0.0], [56.034521, 91.850166, 0.0], [56.023671, 91.839315, 0.0], [56.01282, 91.850166, 0.0], [56.023671, 91.850166, -0.010851], [56.034521, 91.850166, 0.0], [55.0, 91.850166, 0.0]]}, {"shapeName": "L_arm_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[55.0, 92.873837, -0.010851], [54.989149, 92.873837, 0.0], [55.0, 92.873837, 0.010851], [55.010851, 92.873837, 0.0], [55.0, 92.873837, -0.010851], [55.0, 92.884687, 0.0], [55.0, 92.873837, 0.010851], [55.0, 92.862986, 0.0], [54.989149, 92.873837, 0.0], [55.0, 92.884687, 0.0], [55.010851, 92.873837, 0.0], [55.0, 92.862986, 0.0], [55.0, 92.873837, -0.010851], [55.0, 92.884687, 0.0], [55.0, 91.850166, 0.0]]}, {"shapeName": "L_arm_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[55.0, 91.861017, 1.023671], [54.989149, 91.850166, 1.023671], [55.0, 91.839315, 1.023671], [55.010851, 91.850166, 1.023671], [55.0, 91.861017, 1.023671], [55.0, 91.850166, 1.034521], [55.0, 91.839315, 1.023671], [55.0, 91.850166, 1.01282], [54.989149, 91.850166, 1.023671], [55.0, 91.850166, 1.034521], [55.010851, 91.850166, 1.023671], [55.0, 91.850166, 1.01282], [55.0, 91.861017, 1.023671], [55.0, 91.850166, 1.034521], [55.0, 91.850166, 0.0]]}]},
			"R_loLeg_shaper_04_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_04_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.25, 9.942646, 0.833333], [-16.335635, 9.429485, 0.773664], [-16.579512, 8.994449, 0.723078], [-16.944485, 8.703755, 0.689276], [-17.375, 8.601681, 0.677407], [-17.805515, 8.703755, 0.689276], [-18.170488, 8.994449, 0.723078], [-18.414365, 9.429485, 0.773664], [-18.5, 9.942646, 0.833333], [-18.414365, 10.455806, 0.893003], [-18.170488, 10.890842, 0.943589], [-17.805515, 11.181536, 0.97739], [-17.375, 11.283611, 0.989259], [-16.944485, 11.181536, 0.97739], [-16.579512, 10.890842, 0.943589], [-16.335635, 10.455806, 0.893003], [-16.25, 9.942646, 0.833333], [-5.0, 9.942646, 0.833333]]}]},
			"R_loLeg_shaper_01_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_01_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-13.75, 20.692646, 2.083333], [-13.816605, 20.293521, 2.036923], [-14.006287, 19.95516, 1.997579], [-14.290155, 19.729064, 1.971289], [-14.625, 19.649673, 1.962057], [-14.959845, 19.729064, 1.971289], [-15.243712, 19.95516, 1.997579], [-15.433395, 20.293521, 2.036923], [-15.5, 20.692646, 2.083333], [-15.433395, 21.09177, 2.129743], [-15.243712, 21.430132, 2.169088], [-14.959845, 21.656227, 2.195378], [-14.625, 21.735618, 2.204609], [-14.290155, 21.656227, 2.195378], [-14.006287, 21.430132, 2.169088], [-13.816605, 21.09177, 2.129743], [-13.75, 20.692646, 2.083333], [-5.0, 20.692646, 2.083333]]}]},
			"R_toe_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 0.221724, -0.118355], [-4.945745, 0.275979, -0.118355], [-5.0, 0.330234, -0.118355], [-5.054255, 0.275979, -0.118355], [-5.0, 0.221724, -0.118355], [-5.0, 0.275979, -0.172605], [-5.0, 0.330234, -0.118355], [-5.0, 0.275979, -0.0641], [-4.945745, 0.275979, -0.118355], [-5.0, 0.275979, -0.172605], [-5.054255, 0.275979, -0.118355], [-5.0, 0.275979, -0.0641], [-5.0, 0.221724, -0.118355], [-5.0, 0.275979, -0.172605], [-5.0, 0.275979, 5.0]]}, {"shapeName": "R_toe_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 0.221724, 5.0], [0.118355, 0.275979, 5.054255], [0.118355, 0.330234, 5.0], [0.118355, 0.275979, 4.945745], [0.118355, 0.221724, 5.0], [0.172605, 0.275979, 5.0], [0.118355, 0.330234, 5.0], [0.0641, 0.275979, 5.0], [0.118355, 0.275979, 5.054255], [0.172605, 0.275979, 5.0], [0.118355, 0.275979, 4.945745], [0.0641, 0.275979, 5.0], [0.118355, 0.221724, 5.0], [0.172605, 0.275979, 5.0], [-5.0, 0.275979, 5.0]]}, {"shapeName": "R_toe_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 5.394334, 5.0], [-5.0, 5.394334, 5.054255], [-5.054255, 5.394334, 5.0], [-5.0, 5.394334, 4.945745], [-4.945745, 5.394334, 5.0], [-5.0, 5.448584, 5.0], [-5.054255, 5.394334, 5.0], [-5.0, 5.340079, 5.0], [-5.0, 5.394334, 5.054255], [-5.0, 5.448584, 5.0], [-5.0, 5.394334, 4.945745], [-5.0, 5.340079, 5.0], [-4.945745, 5.394334, 5.0], [-5.0, 5.448584, 5.0], [-5.0, 0.275979, 5.0]]}]},
			"L_loLeg_shaper_05_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_05_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[15.0, 6.359312, 0.416667], [15.07612, 5.90317, 0.363627], [15.2929, 5.516471, 0.318662], [15.61732, 5.258076, 0.288616], [16.0, 5.167344, 0.278066], [16.38268, 5.258076, 0.288616], [16.7071, 5.516471, 0.318662], [16.92388, 5.90317, 0.363627], [17.0, 6.359312, 0.416667], [16.92388, 6.815455, 0.469707], [16.7071, 7.202154, 0.514671], [16.38268, 7.460549, 0.544717], [16.0, 7.551281, 0.555268], [15.61732, 7.460549, 0.544717], [15.2929, 7.202154, 0.514671], [15.07612, 6.815455, 0.469707], [15.0, 6.359312, 0.416667], [5.0, 6.359312, 0.416667]]}]},
			"R_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_B_CTLShape", "degree": 1, "form": 0, "points": [[-63.812803, 92.907587, -0.5], [-62.31758, 92.787969, -0.5], [-62.31758, 92.787969, -2.0], [-63.812803, 92.907587, -2.0], [-63.93242, 91.412364, -2.0], [-62.437197, 91.292746, -2.0], [-62.437197, 91.292746, -0.5], [-63.93242, 91.412364, -0.5], [-63.812803, 92.907587, -0.5], [-63.812803, 92.907587, -2.0], [-62.31758, 92.787969, -2.0], [-62.437197, 91.292746, -2.0], [-63.93242, 91.412364, -2.0], [-63.93242, 91.412364, -0.5], [-62.437197, 91.292746, -0.5], [-62.31758, 92.787969, -0.5]]}]},
			"R_upLeg_shaper_03_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_03_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-13.75, 34.275979, 1.25], [-13.816605, 33.877268, 1.299839], [-14.006287, 33.539257, 1.34209], [-14.290155, 33.313396, 1.370323], [-14.625, 33.234087, 1.380236], [-14.959845, 33.313396, 1.370323], [-15.243712, 33.539257, 1.34209], [-15.433395, 33.877268, 1.299839], [-15.5, 34.275979, 1.25], [-15.433395, 34.67469, 1.200161], [-15.243712, 35.012701, 1.15791], [-14.959845, 35.238562, 1.129677], [-14.625, 35.317871, 1.119764], [-14.290155, 35.238562, 1.129677], [-14.006287, 35.012701, 1.15791], [-13.816605, 34.67469, 1.200161], [-13.75, 34.275979, 1.25], [-5.0, 34.275979, 1.25]]}]},
			"L_bendyLeg_B_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_B_CTLShape", "degree": 1, "form": 0, "points": [[4.166665, 24.286724, 4.999977], [3.666665, 24.286724, 4.999977], [5.0, 24.292096, 6.249965], [6.333335, 24.286724, 4.999977], [5.833335, 24.286724, 4.999977], [5.833335, 24.279561, 3.333327], [7.5, 24.279561, 3.333327], [7.5, 24.281709, 3.833323], [8.75, 24.275979, 2.5], [7.5, 24.270248, 1.166677], [7.5, 24.272397, 1.666673], [5.833335, 24.272397, 1.666673], [5.833335, 24.265234, 2.3e-05], [6.333335, 24.265234, 2.3e-05], [5.0, 24.259862, -1.249965], [3.666665, 24.265234, 2.3e-05], [4.166665, 24.265234, 2.3e-05], [4.166665, 24.272397, 1.666673], [2.5, 24.272397, 1.666673], [2.5, 24.270248, 1.166677], [1.25, 24.275979, 2.5], [2.5, 24.281709, 3.833323], [2.5, 24.279561, 3.333327], [4.166665, 24.279561, 3.333327], [4.166665, 24.286724, 4.999977]]}]},
			"L_arm_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[35.0, 101.850166, 0.449787], [35.0, 101.850166, -0.449787], [35.0, 101.850166, 0.0], [34.550213, 101.850166, 0.0], [35.449787, 101.850166, 0.0], [35.0, 101.850166, 0.0], [35.0, 102.299953, 0.0], [35.0, 101.40038, 0.0]]}]},
			"R_bendyLeg_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_bendyLeg_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 8.435613, 0.712717], [-4.945745, 8.441879, 0.658826], [-5.0, 8.448146, 0.604934], [-5.054255, 8.441879, 0.658826], [-5.0, 8.435613, 0.712717], [-5.0, 8.387992, 0.65256], [-5.0, 8.448146, 0.604934], [-5.0, 8.495771, 0.665092], [-4.945745, 8.441879, 0.658826], [-5.0, 8.387992, 0.65256], [-5.054255, 8.441879, 0.658826], [-5.0, 8.495771, 0.665092], [-5.0, 8.435613, 0.712717], [-5.0, 8.387992, 0.65256], [-5.0, 13.525979, 1.25]]}, {"shapeName": "R_bendyLeg_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 13.519713, 1.303892], [0.118355, 13.579871, 1.256266], [0.118355, 13.532246, 1.196108], [0.118355, 13.472087, 1.243734], [0.118355, 13.519713, 1.303892], [0.172605, 13.525979, 1.25], [0.118355, 13.532246, 1.196108], [0.0641, 13.525979, 1.25], [0.118355, 13.579871, 1.256266], [0.172605, 13.525979, 1.25], [0.118355, 13.472087, 1.243734], [0.0641, 13.525979, 1.25], [0.118355, 13.519713, 1.303892], [0.172605, 13.525979, 1.25], [-5.0, 13.525979, 1.25]]}, {"shapeName": "R_bendyLeg_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 14.117153, -3.8341], [-5.0, 14.171045, -3.827833], [-5.054255, 14.117153, -3.8341], [-5.0, 14.063262, -3.840366], [-4.945745, 14.117153, -3.8341], [-5.0, 14.123419, -3.887987], [-5.054255, 14.117153, -3.8341], [-5.0, 14.110887, -3.780208], [-5.0, 14.171045, -3.827833], [-5.0, 14.123419, -3.887987], [-5.0, 14.063262, -3.840366], [-5.0, 14.110887, -3.780208], [-4.945745, 14.117153, -3.8341], [-5.0, 14.123419, -3.887987], [-5.0, 13.525979, 1.25]]}]},
			"C_spineShaper_4_CTL": {"color": 4, "shapes": [{"shapeName": "C_spineShaper_4_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 70.600166, -7.5], [0.0, 70.887176, -7.55709], [0.0, 71.130491, -7.719675], [0.0, 71.293076, -7.96299], [0.0, 71.350166, -8.25], [0.0, 71.293076, -8.53701], [0.0, 71.130491, -8.780325], [0.0, 70.887176, -8.94291], [0.0, 70.600166, -9.0], [0.0, 70.313156, -8.94291], [0.0, 70.069841, -8.780325], [0.0, 69.907256, -8.53701], [0.0, 69.850166, -8.25], [0.0, 69.907256, -7.96299], [0.0, 70.069841, -7.719675], [0.0, 70.313156, -7.55709], [0.0, 70.600166, -7.5], [0.0, 70.600166, 0.0]]}]},
			"R_outterBall_CTL": {"color": 20, "shapes": [{"shapeName": "R_outterBall_CTLShape", "degree": 1, "form": 0, "points": [[-8.5, 0.275979, 5.5], [-8.5, -0.224021, 5.0], [-9.0, 0.275979, 5.0], [-8.5, 0.275979, 5.5], [-8.0, 0.275979, 5.0], [-8.5, -0.224021, 5.0], [-8.5, 0.275979, 4.5], [-8.0, 0.275979, 5.0], [-8.5, 0.775979, 5.0], [-8.5, 0.275979, 5.5], [-9.0, 0.275979, 5.0], [-8.5, 0.275979, 4.5], [-8.5, 0.775979, 5.0], [-9.0, 0.275979, 5.0]]}]},
			"L_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.227054, 92.508331, 1.195745], [68.222728, 92.562413, 1.25], [68.227054, 92.508331, 1.304255], [68.231381, 92.454248, 1.25], [68.227054, 92.508331, 1.195745], [68.281132, 92.512657, 1.25], [68.227054, 92.508331, 1.304255], [68.172972, 92.504004, 1.25], [68.222728, 92.562413, 1.25], [68.281132, 92.512657, 1.25], [68.231381, 92.454248, 1.25], [68.172972, 92.504004, 1.25], [68.227054, 92.508331, 1.195745], [68.281132, 92.512657, 1.25], [63.125, 92.100166, 1.25]]}, {"shapeName": "L_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[62.716836, 97.202221, 1.195745], [62.662753, 97.197894, 1.25], [62.716836, 97.202221, 1.304255], [62.770918, 97.206547, 1.25], [62.716836, 97.202221, 1.195745], [62.712509, 97.256298, 1.25], [62.716836, 97.202221, 1.304255], [62.721162, 97.148139, 1.25], [62.662753, 97.197894, 1.25], [62.712509, 97.256298, 1.25], [62.770918, 97.206547, 1.25], [62.721162, 97.148139, 1.25], [62.716836, 97.202221, 1.195745], [62.712509, 97.256298, 1.25], [63.125, 92.100166, 1.25]]}, {"shapeName": "L_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[63.120673, 92.154249, 6.368355], [63.070918, 92.09584, 6.368355], [63.129327, 92.046084, 6.368355], [63.179082, 92.104493, 6.368355], [63.120673, 92.154249, 6.368355], [63.125, 92.100166, 6.422605], [63.129327, 92.046084, 6.368355], [63.125, 92.100166, 6.3141], [63.070918, 92.09584, 6.368355], [63.125, 92.100166, 6.422605], [63.179082, 92.104493, 6.368355], [63.125, 92.100166, 6.3141], [63.120673, 92.154249, 6.368355], [63.125, 92.100166, 6.422605], [63.125, 92.100166, 1.25]]}]},
			"R_upLeg_shaper_01_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_01_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-15.0, 40.942646, 0.416667], [-15.07612, 40.486976, 0.473625], [-15.2929, 40.100678, 0.521913], [-15.61732, 39.842551, 0.554179], [-16.0, 39.751912, 0.565508], [-16.38268, 39.842551, 0.554179], [-16.7071, 40.100678, 0.521913], [-16.92388, 40.486976, 0.473625], [-17.0, 40.942646, 0.416667], [-16.92388, 41.398316, 0.359708], [-16.7071, 41.784613, 0.311421], [-16.38268, 42.04274, 0.279155], [-16.0, 42.133379, 0.267825], [-15.61732, 42.04274, 0.279155], [-15.2929, 41.784613, 0.311421], [-15.07612, 41.398316, 0.359708], [-15.0, 40.942646, 0.416667], [-5.0, 40.942646, 0.416667]]}]},
			"L_bendyLeg_C_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.333332, 13.294977, 3.236615], [3.933332, 13.294977, 3.236615], [5.0, 13.179476, 4.229922], [6.066668, 13.294977, 3.236615], [5.666668, 13.294977, 3.236615], [5.666668, 13.448978, 1.912206], [7.0, 13.448978, 1.912206], [7.0, 13.402778, 2.309529], [8.0, 13.525979, 1.25], [7.0, 13.64918, 0.190471], [7.0, 13.60298, 0.587794], [5.666668, 13.60298, 0.587794], [5.666668, 13.756981, -0.736615], [6.066668, 13.756981, -0.736615], [5.0, 13.872482, -1.729922], [3.933332, 13.756981, -0.736615], [4.333332, 13.756981, -0.736615], [4.333332, 13.60298, 0.587794], [3.0, 13.60298, 0.587794], [3.0, 13.64918, 0.190471], [2.0, 13.525979, 1.25], [3.0, 13.402778, 2.309529], [3.0, 13.448978, 1.912206], [4.333332, 13.448978, 1.912206], [4.333332, 13.294977, 3.236615]]}]},
			"L_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.031312, 92.022153, 6.056518], [66.994255, 92.002294, 6.120702], [67.004184, 91.92818, 6.103504], [67.041241, 91.948039, 6.03932], [67.031312, 92.022153, 6.056518], [67.06473, 91.975166, 6.107136], [67.004184, 91.92818, 6.103504], [66.970762, 91.975166, 6.052883], [66.994255, 92.002294, 6.120702], [67.06473, 91.975166, 6.107136], [67.041241, 91.948039, 6.03932], [66.970762, 91.975166, 6.052883], [67.031312, 92.022153, 6.056518], [67.06473, 91.975166, 6.107136], [62.585122, 91.975166, 3.520833]]}, {"shapeName": "L_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[60.382374, 94.58133, 7.336106], [60.321824, 94.534344, 7.332472], [60.355246, 94.487358, 7.383093], [60.415796, 94.534344, 7.386727], [60.382374, 94.58133, 7.336106], [60.345319, 94.561469, 7.400287], [60.355246, 94.487358, 7.383093], [60.392303, 94.507216, 7.318908], [60.321824, 94.534344, 7.332472], [60.345319, 94.561469, 7.400287], [60.415796, 94.534344, 7.386727], [60.392303, 94.507216, 7.318908], [60.382374, 94.58133, 7.336106], [60.345319, 94.561469, 7.400287], [62.585122, 91.975166, 3.520833]]}, {"shapeName": "L_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.282041, 87.569668, 5.777837], [61.258548, 87.542541, 5.710019], [61.329027, 87.515413, 5.696455], [61.35252, 87.542541, 5.764274], [61.282041, 87.569668, 5.777837], [61.291971, 87.495559, 5.760637], [61.329027, 87.515413, 5.696455], [61.319097, 87.589527, 5.713653], [61.258548, 87.542541, 5.710019], [61.291971, 87.495559, 5.760637], [61.35252, 87.542541, 5.764274], [61.319097, 87.589527, 5.713653], [61.282041, 87.569668, 5.777837], [61.291971, 87.495559, 5.760637], [62.585122, 91.975166, 3.520833]]}]},
			"C_hip_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[4.231505, 51.850166, -3.526254], [0.0, 50.050166, -4.986873], [-4.231505, 51.850166, -3.526254], [-5.984248, 53.650166, 0.0], [-4.231505, 51.850166, 3.526254], [0.0, 50.050166, 4.986873], [4.231505, 51.850166, 3.526254], [5.984248, 53.650166, 0.0]]}]},
			"L_upLeg_shaper_05_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_05_CTLShape", "degree": 1, "form": 0, "points": [[17.5, 27.609312, 2.083333], [17.59515, 27.039725, 2.154532], [17.866125, 26.556853, 2.214891], [18.27165, 26.234194, 2.255223], [18.75, 26.120895, 2.269385], [19.22835, 26.234194, 2.255223], [19.633875, 26.556853, 2.214891], [19.90485, 27.039725, 2.154532], [20.0, 27.609312, 2.083333], [19.90485, 28.1789, 2.012135], [19.633875, 28.661772, 1.951776], [19.22835, 28.984431, 1.911444], [18.75, 29.097729, 1.897281], [18.27165, 28.984431, 1.911444], [17.866125, 28.661772, 1.951776], [17.59515, 28.1789, 2.012135], [17.5, 27.609312, 2.083333], [5.0, 27.609312, 2.083333]]}]},
			"C_head_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.330127, 101.850166, -2.5], [0.0, 101.850166, -5.0], [-4.330127, 101.850166, -2.5], [-5.681681, 107.90975, 2.975865], [0.0, 107.90975, 7.594153], [5.681681, 107.90975, 2.975865], [4.330127, 101.850166, -2.5]]}]},
			"L_loLeg_shaper_02_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_02_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[15.0, 17.109312, 1.666667], [15.07612, 16.65317, 1.613627], [15.2929, 16.266471, 1.568662], [15.61732, 16.008076, 1.538616], [16.0, 15.917343, 1.528066], [16.38268, 16.008076, 1.538616], [16.7071, 16.266471, 1.568662], [16.92388, 16.65317, 1.613627], [17.0, 17.109312, 1.666667], [16.92388, 17.565455, 1.719707], [16.7071, 17.952154, 1.764671], [16.38268, 18.210549, 1.794717], [16.0, 18.301281, 1.805268], [15.61732, 18.210549, 1.794717], [15.2929, 17.952154, 1.764671], [15.07612, 17.565455, 1.719707], [15.0, 17.109312, 1.666667], [5.0, 17.109312, 1.666667]]}]},
			"L_lwrArmRibbonMid_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lwrArmRibbonMid_PIV_CTLShape", "degree": 1, "form": 0, "points": [[47.485136, 91.850166, -2.221565], [47.482075, 91.861017, -2.211155], [47.479013, 91.850166, -2.200744], [47.482075, 91.839315, -2.211155], [47.485136, 91.850166, -2.221565], [47.492484, 91.850166, -2.208093], [47.479013, 91.850166, -2.200744], [47.471665, 91.850166, -2.214216], [47.482075, 91.861017, -2.211155], [47.492484, 91.850166, -2.208093], [47.482075, 91.839315, -2.211155], [47.471665, 91.850166, -2.214216], [47.485136, 91.850166, -2.221565], [47.492484, 91.850166, -2.208093], [46.5, 91.850166, -2.5]]}, {"shapeName": "L_lwrArmRibbonMid_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[46.503062, 92.873837, -2.51041], [46.48959, 92.873837, -2.503062], [46.496938, 92.873837, -2.48959], [46.51041, 92.873837, -2.496938], [46.503062, 92.873837, -2.51041], [46.5, 92.884687, -2.5], [46.496938, 92.873837, -2.48959], [46.5, 92.862986, -2.5], [46.48959, 92.873837, -2.503062], [46.5, 92.884687, -2.5], [46.51041, 92.873837, -2.496938], [46.5, 92.862986, -2.5], [46.503062, 92.873837, -2.51041], [46.5, 92.884687, -2.5], [46.5, 91.850166, -2.5]]}, {"shapeName": "L_lwrArmRibbonMid_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[46.211155, 91.861017, -1.517925], [46.200744, 91.850166, -1.520987], [46.211155, 91.839315, -1.517925], [46.221565, 91.850166, -1.514864], [46.211155, 91.861017, -1.517925], [46.208093, 91.850166, -1.507516], [46.211155, 91.839315, -1.517925], [46.214216, 91.850166, -1.528335], [46.200744, 91.850166, -1.520987], [46.208093, 91.850166, -1.507516], [46.221565, 91.850166, -1.514864], [46.214216, 91.850166, -1.528335], [46.211155, 91.861017, -1.517925], [46.208093, 91.850166, -1.507516], [46.5, 91.850166, -2.5]]}]},
			"L_upLeg_shaper_05_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_05_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.25, 27.609312, 2.083333], [16.335635, 27.096684, 2.147412], [16.579512, 26.662099, 2.201735], [16.944485, 26.371706, 2.238034], [17.375, 26.269737, 2.25078], [17.805515, 26.371706, 2.238034], [18.170488, 26.662099, 2.201735], [18.414365, 27.096684, 2.147412], [18.5, 27.609312, 2.083333], [18.414365, 28.121941, 2.019255], [18.170488, 28.556526, 1.964932], [17.805515, 28.846919, 1.928632], [17.375, 28.948887, 1.915886], [16.944485, 28.846919, 1.928632], [16.579512, 28.556526, 1.964932], [16.335635, 28.121941, 2.019255], [16.25, 27.609312, 2.083333], [5.0, 27.609312, 2.083333]]}]},
			"R_loLeg_shaper_05_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_loLeg_shaper_05_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 1.268946, -0.120616], [-4.945745, 1.275213, -0.174508], [-5.0, 1.281479, -0.2284], [-5.054255, 1.275213, -0.174508], [-5.0, 1.268946, -0.120616], [-5.0, 1.221326, -0.180774], [-5.0, 1.281479, -0.2284], [-5.0, 1.329104, -0.168241], [-4.945745, 1.275213, -0.174508], [-5.0, 1.221326, -0.180774], [-5.054255, 1.275213, -0.174508], [-5.0, 1.329104, -0.168241], [-5.0, 1.268946, -0.120616], [-5.0, 1.221326, -0.180774], [-5.0, 6.359312, 0.416667]]}, {"shapeName": "R_loLeg_shaper_05_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 6.353046, 0.470559], [0.118355, 6.413204, 0.422933], [0.118355, 6.365579, 0.362775], [0.118355, 6.30542, 0.4104], [0.118355, 6.353046, 0.470559], [0.172605, 6.359312, 0.416667], [0.118355, 6.365579, 0.362775], [0.0641, 6.359312, 0.416667], [0.118355, 6.413204, 0.422933], [0.172605, 6.359312, 0.416667], [0.118355, 6.30542, 0.4104], [0.0641, 6.359312, 0.416667], [0.118355, 6.353046, 0.470559], [0.172605, 6.359312, 0.416667], [-5.0, 6.359312, 0.416667]]}, {"shapeName": "R_loLeg_shaper_05_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 6.950487, -4.667433], [-5.0, 7.004379, -4.661167], [-5.054255, 6.950487, -4.667433], [-5.0, 6.896595, -4.6737], [-4.945745, 6.950487, -4.667433], [-5.0, 6.956753, -4.72132], [-5.054255, 6.950487, -4.667433], [-5.0, 6.94422, -4.613541], [-5.0, 7.004379, -4.661167], [-5.0, 6.956753, -4.72132], [-5.0, 6.896595, -4.6737], [-5.0, 6.94422, -4.613541], [-4.945745, 6.950487, -4.667433], [-5.0, 6.956753, -4.72132], [-5.0, 6.359312, 0.416667]]}]},
			"L_leg_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[8.90939, 3.360282, 0.067942], [8.750215, 3.360282, 0.067942], [8.72007, 3.19804, 0.049077], [8.60696, 3.151489, 0.043664], [8.47014, 3.245039, 0.054542], [8.357585, 3.133237, 0.041542], [8.45176, 2.997348, 0.025741], [8.404915, 2.88498, 0.012674], [8.241565, 2.855036, 0.009193], [8.241565, 2.696922, -0.009193], [8.404915, 2.666978, -0.012674], [8.45176, 2.554625, -0.025739], [8.357585, 2.418721, -0.041542], [8.47014, 2.306919, -0.054542], [8.60696, 2.400469, -0.043664], [8.72007, 2.353918, -0.049077], [8.750215, 2.191676, -0.067942], [8.90939, 2.191676, -0.067942], [8.93955, 2.353918, -0.049077], [9.05266, 2.400469, -0.043664], [9.18948, 2.306919, -0.054542], [9.302025, 2.418721, -0.041542], [9.20786, 2.554625, -0.025739], [9.254705, 2.666978, -0.012674], [9.41804, 2.696922, -0.009193], [9.41804, 2.855036, 0.009193], [9.254705, 2.88498, 0.012674], [9.20786, 2.997348, 0.025741], [9.302025, 3.133237, 0.041542], [9.18948, 3.245039, 0.054542], [9.05266, 3.151489, 0.043664], [8.93955, 3.19804, 0.049077], [8.90939, 3.360282, 0.067942]]}, {"shapeName": "L_leg_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[9.00258, 2.947603, 0.019956], [9.07415, 2.775979, 0.0], [9.00258, 2.604355, -0.019956], [8.829805, 2.533279, -0.028221], [8.65704, 2.604355, -0.019956], [8.58547, 2.775979, 0.0], [8.65704, 2.947603, 0.019956], [8.829805, 3.018679, 0.028221]]}, {"shapeName": "L_leg_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[8.241565, 2.775979, 0.0], [5.0, 2.775979, 0.0]]}]},
			"C_visibility_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_visibility_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.523671, 252.93298, -0.010851], [1.523671, 252.943831, 0.0], [1.523671, 252.93298, 0.010851], [1.523671, 252.922129, 0.0], [1.523671, 252.93298, -0.010851], [1.534521, 252.93298, 0.0], [1.523671, 252.93298, 0.010851], [1.51282, 252.93298, 0.0], [1.523671, 252.943831, 0.0], [1.534521, 252.93298, 0.0], [1.523671, 252.922129, 0.0], [1.51282, 252.93298, 0.0], [1.523671, 252.93298, -0.010851], [1.534521, 252.93298, 0.0], [0.5, 252.93298, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.5, 253.956651, -0.010851], [0.489149, 253.956651, 0.0], [0.5, 253.956651, 0.010851], [0.510851, 253.956651, 0.0], [0.5, 253.956651, -0.010851], [0.5, 253.967501, 0.0], [0.5, 253.956651, 0.010851], [0.5, 253.9458, 0.0], [0.489149, 253.956651, 0.0], [0.5, 253.967501, 0.0], [0.510851, 253.956651, 0.0], [0.5, 253.9458, 0.0], [0.5, 253.956651, -0.010851], [0.5, 253.967501, 0.0], [0.5, 252.93298, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.5, 252.943831, 1.023671], [0.489149, 252.93298, 1.023671], [0.5, 252.922129, 1.023671], [0.510851, 252.93298, 1.023671], [0.5, 252.943831, 1.023671], [0.5, 252.93298, 1.034521], [0.5, 252.922129, 1.023671], [0.5, 252.93298, 1.01282], [0.489149, 252.93298, 1.023671], [0.5, 252.93298, 1.034521], [0.510851, 252.93298, 1.023671], [0.5, 252.93298, 1.01282], [0.5, 252.943831, 1.023671], [0.5, 252.93298, 1.034521], [0.5, 252.93298, 0.0]]}]},
			"R_arm_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-35.0, 101.850166, 0.39981], [-35.0, 101.850166, -0.39981], [-35.0, 101.850166, -0.0], [-34.60019, 101.850166, -0.0], [-35.39981, 101.850166, 0.0], [-35.0, 101.850166, -0.0], [-35.0, 102.249977, -0.0], [-35.0, 101.450356, -0.0]]}]},
			"L_leg_IK_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_leg_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[7.350836, 2.775979, -3.91806], [5.0, 2.775979, -5.54097], [2.649164, 2.775979, -3.91806], [1.675418, 2.775979, 0.0], [2.649164, 2.775979, 3.91806], [5.0, 2.775979, 5.54097], [7.350836, 2.775979, 3.91806], [8.324582, 2.775979, 0.0]]}]},
			"R_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_C_CTLShape", "degree": 1, "form": 0, "points": [[-65.80742, 92.937969, 2.0], [-64.312197, 93.057587, 2.0], [-64.312197, 93.057587, 0.5], [-65.80742, 92.937969, 0.5], [-65.687803, 91.442746, 0.5], [-64.19258, 91.562364, 0.5], [-64.19258, 91.562364, 2.0], [-65.687803, 91.442746, 2.0], [-65.80742, 92.937969, 2.0], [-65.80742, 92.937969, 0.5], [-64.312197, 93.057587, 0.5], [-64.19258, 91.562364, 0.5], [-65.687803, 91.442746, 0.5], [-65.687803, 91.442746, 2.0], [-64.19258, 91.562364, 2.0], [-64.312197, 93.057587, 2.0]]}]},
			"R_toe_IK_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-6.763127, 2.039106, 5.0], [-5.0, 2.769416, 5.0], [-3.236873, 2.039106, 5.0], [-2.506564, 0.275979, 5.0], [-3.236873, -1.487148, 5.0], [-5.0, -2.217457, 5.0], [-6.763127, -1.487148, 5.0], [-7.493436, 0.275979, 5.0]]}]},
			"C_hip_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[5.642006, 51.850166, -4.701672], [0.0, 49.450166, -6.649164], [-5.642006, 51.850166, -4.701672], [-7.978997, 54.250166, 0.0], [-5.642006, 51.850166, 4.701672], [0.0, 49.450166, 6.649164], [5.642006, 51.850166, 4.701672], [7.978997, 54.250166, 0.0]]}]},
			"L_upLeg_shaper_03_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_shaper_03_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 29.203878, 1.93869], [4.945745, 29.197149, 1.884854], [5.0, 29.190419, 1.831018], [5.054255, 29.197149, 1.884854], [5.0, 29.203878, 1.93869], [5.0, 29.143317, 1.891583], [5.0, 29.190419, 1.831018], [5.0, 29.250985, 1.878124], [4.945745, 29.197149, 1.884854], [5.0, 29.143317, 1.891583], [5.054255, 29.197149, 1.884854], [5.0, 29.250985, 1.878124], [5.0, 29.203878, 1.93869], [5.0, 29.143317, 1.891583], [5.0, 34.275979, 1.25]]}, {"shapeName": "L_upLeg_shaper_03_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 34.282708, 1.303836], [-0.118355, 34.329815, 1.24327], [-0.118355, 34.269249, 1.196164], [-0.118355, 34.222143, 1.25673], [-0.118355, 34.282708, 1.303836], [-0.172605, 34.275979, 1.25], [-0.118355, 34.269249, 1.196164], [-0.0641, 34.275979, 1.25], [-0.118355, 34.329815, 1.24327], [-0.172605, 34.275979, 1.25], [-0.118355, 34.222143, 1.25673], [-0.0641, 34.275979, 1.25], [-0.118355, 34.282708, 1.303836], [-0.172605, 34.275979, 1.25], [5.0, 34.275979, 1.25]]}, {"shapeName": "L_upLeg_shaper_03_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 33.641125, -3.82883], [5.0, 33.694961, -3.83556], [5.054255, 33.641125, -3.82883], [5.0, 33.587289, -3.822101], [4.945745, 33.641125, -3.82883], [5.0, 33.634396, -3.882662], [5.054255, 33.641125, -3.82883], [5.0, 33.647855, -3.774994], [5.0, 33.694961, -3.83556], [5.0, 33.634396, -3.882662], [5.0, 33.587289, -3.822101], [5.0, 33.647855, -3.774994], [4.945745, 33.641125, -3.82883], [5.0, 33.634396, -3.882662], [5.0, 34.275979, 1.25]]}]},
			"R_scapulaTarget_CTL": {"color": 17, "shapes": [{"shapeName": "R_scapulaTarget_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 91.850166, -13.5], [1.5, 91.850166, -15.0], [0.0, 90.350166, -15.0], [0.0, 91.850166, -13.5], [0.0, 93.350166, -15.0], [1.5, 91.850166, -15.0], [0.0, 91.850166, -16.5], [0.0, 93.350166, -15.0], [-1.5, 91.850166, -15.0], [0.0, 91.850166, -13.5], [0.0, 90.350166, -15.0], [0.0, 91.850166, -16.5], [-1.5, 91.850166, -15.0], [0.0, 90.350166, -15.0]]}]},
			"L_legBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_legBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 39.203878, 0.68869], [4.945745, 39.197149, 0.634854], [5.0, 39.190419, 0.581018], [5.054255, 39.197149, 0.634854], [5.0, 39.203878, 0.68869], [5.0, 39.143317, 0.641583], [5.0, 39.190419, 0.581018], [5.0, 39.250985, 0.628124], [4.945745, 39.197149, 0.634854], [5.0, 39.143317, 0.641583], [5.054255, 39.197149, 0.634854], [5.0, 39.250985, 0.628124], [5.0, 39.203878, 0.68869], [5.0, 39.143317, 0.641583], [5.0, 44.275979, 0.0]]}, {"shapeName": "L_legBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 44.282708, 0.053836], [-0.118355, 44.329815, -0.00673], [-0.118355, 44.269249, -0.053836], [-0.118355, 44.222143, 0.00673], [-0.118355, 44.282708, 0.053836], [-0.172605, 44.275979, 0.0], [-0.118355, 44.269249, -0.053836], [-0.0641, 44.275979, 0.0], [-0.118355, 44.329815, -0.00673], [-0.172605, 44.275979, 0.0], [-0.118355, 44.222143, 0.00673], [-0.0641, 44.275979, 0.0], [-0.118355, 44.282708, 0.053836], [-0.172605, 44.275979, 0.0], [5.0, 44.275979, 0.0]]}, {"shapeName": "L_legBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 43.641125, -5.07883], [5.0, 43.694961, -5.08556], [5.054255, 43.641125, -5.07883], [5.0, 43.587289, -5.072101], [4.945745, 43.641125, -5.07883], [5.0, 43.634396, -5.132662], [5.054255, 43.641125, -5.07883], [5.0, 43.647855, -5.024994], [5.0, 43.694961, -5.08556], [5.0, 43.634396, -5.132662], [5.0, 43.587289, -5.072101], [5.0, 43.647855, -5.024994], [4.945745, 43.641125, -5.07883], [5.0, 43.634396, -5.132662], [5.0, 44.275979, 0.0]]}]},
			"C_head_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[3.788861, 101.850166, -2.1875], [0.0, 101.850166, -4.375], [-3.788861, 101.850166, -2.1875], [-4.971471, 107.152302, 2.603882], [0.0, 107.152302, 6.644884], [4.971471, 107.152302, 2.603882], [3.788861, 101.850166, -2.1875]]}]},
			"L_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.368355, 96.850166, -0.054255], [66.368355, 96.904421, 0.0], [66.368355, 96.850166, 0.054255], [66.368355, 96.795911, 0.0], [66.368355, 96.850166, -0.054255], [66.422605, 96.850166, 0.0], [66.368355, 96.850166, 0.054255], [66.3141, 96.850166, 0.0], [66.368355, 96.904421, 0.0], [66.422605, 96.850166, 0.0], [66.368355, 96.795911, 0.0], [66.3141, 96.850166, 0.0], [66.368355, 96.850166, -0.054255], [66.422605, 96.850166, 0.0], [61.25, 96.850166, 0.0]]}, {"shapeName": "L_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[61.25, 101.968521, -0.054255], [61.195745, 101.968521, 0.0], [61.25, 101.968521, 0.054255], [61.304255, 101.968521, 0.0], [61.25, 101.968521, -0.054255], [61.25, 102.022771, 0.0], [61.25, 101.968521, 0.054255], [61.25, 101.914266, 0.0], [61.195745, 101.968521, 0.0], [61.25, 102.022771, 0.0], [61.304255, 101.968521, 0.0], [61.25, 101.914266, 0.0], [61.25, 101.968521, -0.054255], [61.25, 102.022771, 0.0], [61.25, 96.850166, 0.0]]}, {"shapeName": "L_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.25, 96.904421, 5.118355], [61.195745, 96.850166, 5.118355], [61.25, 96.795911, 5.118355], [61.304255, 96.850166, 5.118355], [61.25, 96.904421, 5.118355], [61.25, 96.850166, 5.172605], [61.25, 96.795911, 5.118355], [61.25, 96.850166, 5.0641], [61.195745, 96.850166, 5.118355], [61.25, 96.850166, 5.172605], [61.304255, 96.850166, 5.118355], [61.25, 96.850166, 5.0641], [61.25, 96.904421, 5.118355], [61.25, 96.850166, 5.172605], [61.25, 96.850166, 0.0]]}]},
			"L_loLeg_shaper_01_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_01_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[13.75, 20.692646, 2.083333], [13.816605, 20.293521, 2.036923], [14.006287, 19.95516, 1.997579], [14.290155, 19.729064, 1.971289], [14.625, 19.649673, 1.962057], [14.959845, 19.729064, 1.971289], [15.243712, 19.95516, 1.997579], [15.433395, 20.293521, 2.036923], [15.5, 20.692646, 2.083333], [15.433395, 21.09177, 2.129743], [15.243712, 21.430132, 2.169088], [14.959845, 21.656227, 2.195378], [14.625, 21.735618, 2.204609], [14.290155, 21.656227, 2.195378], [14.006287, 21.430132, 2.169088], [13.816605, 21.09177, 2.129743], [13.75, 20.692646, 2.083333], [5.0, 20.692646, 2.083333]]}]},
			"L_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_B_CTLShape", "degree": 1, "form": 0, "points": [[63.812803, 92.907587, 2.0], [62.31758, 92.787969, 2.0], [62.31758, 92.787969, 0.5], [63.812803, 92.907587, 0.5], [63.93242, 91.412364, 0.5], [62.437197, 91.292746, 0.5], [62.437197, 91.292746, 2.0], [63.93242, 91.412364, 2.0], [63.812803, 92.907587, 2.0], [63.812803, 92.907587, 0.5], [62.31758, 92.787969, 0.5], [62.437197, 91.292746, 0.5], [63.93242, 91.412364, 0.5], [63.93242, 91.412364, 2.0], [62.437197, 91.292746, 2.0], [62.31758, 92.787969, 2.0]]}]},
			"L_shoulder_shaper_05_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_shoulder_shaper_05_PIV_CTLShape", "degree": 1, "form": 0, "points": [[38.083421, 91.850166, -5.034434], [38.086325, 91.861017, -5.023979], [38.08923, 91.850166, -5.013524], [38.086325, 91.839315, -5.023979], [38.083421, 91.850166, -5.034434], [38.09678, 91.850166, -5.026883], [38.08923, 91.850166, -5.013524], [38.07587, 91.850166, -5.021075], [38.086325, 91.861017, -5.023979], [38.09678, 91.850166, -5.026883], [38.086325, 91.839315, -5.023979], [38.07587, 91.850166, -5.021075], [38.083421, 91.850166, -5.034434], [38.09678, 91.850166, -5.026883], [37.1, 91.850166, -4.75]]}, {"shapeName": "L_shoulder_shaper_05_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[37.097096, 92.873837, -4.760455], [37.089545, 92.873837, -4.747096], [37.102904, 92.873837, -4.739545], [37.110455, 92.873837, -4.752904], [37.097096, 92.873837, -4.760455], [37.1, 92.884687, -4.75], [37.102904, 92.873837, -4.739545], [37.1, 92.862986, -4.75], [37.089545, 92.873837, -4.747096], [37.1, 92.884687, -4.75], [37.110455, 92.873837, -4.752904], [37.1, 92.862986, -4.75], [37.097096, 92.873837, -4.760455], [37.1, 92.884687, -4.75], [37.1, 91.850166, -4.75]]}, {"shapeName": "L_shoulder_shaper_05_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[37.373979, 91.861017, -3.763675], [37.363524, 91.850166, -3.76077], [37.373979, 91.839315, -3.763675], [37.384434, 91.850166, -3.766579], [37.373979, 91.861017, -3.763675], [37.376883, 91.850166, -3.75322], [37.373979, 91.839315, -3.763675], [37.371075, 91.850166, -3.77413], [37.363524, 91.850166, -3.76077], [37.376883, 91.850166, -3.75322], [37.384434, 91.850166, -3.766579], [37.371075, 91.850166, -3.77413], [37.373979, 91.861017, -3.763675], [37.376883, 91.850166, -3.75322], [37.1, 91.850166, -4.75]]}]},
			"R_elbow_shaper_05_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_05_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-54.15, 93.600166, -0.25], [-54.214248, 93.613487, -0.231104], [-54.268714, 93.651424, -0.215084], [-54.305109, 93.708197, -0.20438], [-54.317889, 93.775166, -0.200621], [-54.305109, 93.842135, -0.20438], [-54.268714, 93.898909, -0.215084], [-54.214248, 93.936845, -0.231104], [-54.15, 93.950166, -0.25], [-54.085752, 93.936845, -0.268896], [-54.031286, 93.898909, -0.284916], [-53.994891, 93.842135, -0.29562], [-53.982111, 93.775166, -0.299379], [-53.994891, 93.708197, -0.29562], [-54.031286, 93.651424, -0.284916], [-54.085752, 93.613487, -0.268896], [-54.15, 93.600166, -0.25], [-54.15, 91.850166, -0.25]]}]},
			"L_elbowRibbon_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_elbowRibbon_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[38.030209, 93.183502, -8.999886], [38.030209, 93.983502, -8.999886], [38.045313, 91.850166, -10.999829], [38.030209, 89.71683, -8.999886], [38.030209, 90.51683, -8.999886], [38.01007, 90.51683, -6.333298], [38.01007, 87.850166, -6.333298], [38.016111, 87.850166, -7.133275], [38.0, 85.850166, -5.0], [37.983889, 87.850166, -2.866725], [37.98993, 87.850166, -3.666702], [37.98993, 90.51683, -3.666702], [37.969791, 90.51683, -1.000114], [37.969791, 89.71683, -1.000114], [37.954687, 91.850166, 0.999829], [37.969791, 93.983502, -1.000114], [37.969791, 93.183502, -1.000114], [37.98993, 93.183502, -3.666702], [37.98993, 95.850166, -3.666702], [37.983889, 95.850166, -2.866725], [38.0, 97.850166, -5.0], [38.016111, 95.850166, -7.133275], [38.01007, 95.850166, -6.333298], [38.01007, 93.183502, -6.333298], [38.030209, 93.183502, -8.999886]]}]},
			"R_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.368355, 96.8502, -0.054255], [-66.368355, 96.904455, 0.0], [-66.368355, 96.8502, 0.054255], [-66.368355, 96.795945, -0.0], [-66.368355, 96.8502, -0.054255], [-66.422605, 96.8502, -0.0], [-66.368355, 96.8502, 0.054255], [-66.3141, 96.8502, -0.0], [-66.368355, 96.904455, 0.0], [-66.422605, 96.8502, -0.0], [-66.368355, 96.795945, -0.0], [-66.3141, 96.8502, -0.0], [-66.368355, 96.8502, -0.054255], [-66.422605, 96.8502, -0.0], [-61.25, 96.8502, -0.0]]}, {"shapeName": "R_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-61.25, 101.968555, -0.054255], [-61.195745, 101.968555, 0.0], [-61.25, 101.968555, 0.054255], [-61.304255, 101.968555, 0.0], [-61.25, 101.968555, -0.054255], [-61.25, 102.022805, 0.0], [-61.25, 101.968555, 0.054255], [-61.25, 101.9143, 0.0], [-61.195745, 101.968555, 0.0], [-61.25, 102.022805, 0.0], [-61.304255, 101.968555, 0.0], [-61.25, 101.9143, 0.0], [-61.25, 101.968555, -0.054255], [-61.25, 102.022805, 0.0], [-61.25, 96.8502, -0.0]]}, {"shapeName": "R_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.25, 96.904455, 5.118355], [-61.195745, 96.8502, 5.118355], [-61.25, 96.795945, 5.118355], [-61.304255, 96.8502, 5.118355], [-61.25, 96.904455, 5.118355], [-61.25, 96.8502, 5.172605], [-61.25, 96.795945, 5.118355], [-61.25, 96.8502, 5.0641], [-61.195745, 96.8502, 5.118355], [-61.25, 96.8502, 5.172605], [-61.304255, 96.8502, 5.118355], [-61.25, 96.8502, 5.0641], [-61.25, 96.904455, 5.118355], [-61.25, 96.8502, 5.172605], [-61.25, 96.8502, -0.0]]}]},
			"L_elbow_shaper_03_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_03_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[46.5, 94.100166, -2.5], [46.582604, 94.117293, -2.475705], [46.652633, 94.166069, -2.455108], [46.699426, 94.239063, -2.441345], [46.715857, 94.325166, -2.436513], [46.699426, 94.411269, -2.441345], [46.652633, 94.484264, -2.455108], [46.582604, 94.533039, -2.475705], [46.5, 94.550166, -2.5], [46.417396, 94.533039, -2.524295], [46.347367, 94.484264, -2.544892], [46.300574, 94.411269, -2.558655], [46.284143, 94.325166, -2.563487], [46.300574, 94.239063, -2.558655], [46.347367, 94.166069, -2.544892], [46.417396, 94.117293, -2.524295], [46.5, 94.100166, -2.5], [46.5, 91.850166, -2.5]]}]},
			"R_upLeg_shaper_02_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_02_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.25, 37.609312, 0.833333], [-16.335635, 37.096684, 0.897412], [-16.579512, 36.662099, 0.951735], [-16.944485, 36.371706, 0.988034], [-17.375, 36.269737, 1.00078], [-17.805515, 36.371706, 0.988034], [-18.170488, 36.662099, 0.951735], [-18.414365, 37.096684, 0.897412], [-18.5, 37.609312, 0.833333], [-18.414365, 38.121941, 0.769255], [-18.170488, 38.556526, 0.714932], [-17.805515, 38.846919, 0.678632], [-17.375, 38.948887, 0.665886], [-16.944485, 38.846919, 0.678632], [-16.579512, 38.556526, 0.714932], [-16.335635, 38.121941, 0.769255], [-16.25, 37.609312, 0.833333], [-5.0, 37.609312, 0.833333]]}]},
			"C_midNeck_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[4.231505, 96.850166, -3.526254], [0.0, 96.850166, -4.986873], [-4.231505, 96.850166, -3.526254], [-5.984248, 96.850166, 0.0], [-4.231505, 96.850166, 3.526254], [0.0, 96.850166, 4.986873], [4.231505, 96.850166, 3.526254], [5.984248, 96.850166, 0.0]]}]},
			"R_lwrArmRibbonMid_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lwrArmRibbonMid_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-47.485136, 91.850166, -2.221565], [-47.482075, 91.861017, -2.211155], [-47.479013, 91.850166, -2.200744], [-47.482075, 91.839315, -2.211155], [-47.485136, 91.850166, -2.221565], [-47.492484, 91.850166, -2.208093], [-47.479013, 91.850166, -2.200744], [-47.471665, 91.850166, -2.214216], [-47.482075, 91.861017, -2.211155], [-47.492484, 91.850166, -2.208093], [-47.482075, 91.839315, -2.211155], [-47.471665, 91.850166, -2.214216], [-47.485136, 91.850166, -2.221565], [-47.492484, 91.850166, -2.208093], [-46.5, 91.850166, -2.5]]}, {"shapeName": "R_lwrArmRibbonMid_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-46.503062, 92.873837, -2.51041], [-46.48959, 92.873837, -2.503062], [-46.496938, 92.873837, -2.48959], [-46.51041, 92.873837, -2.496938], [-46.503062, 92.873837, -2.51041], [-46.5, 92.884687, -2.5], [-46.496938, 92.873837, -2.48959], [-46.5, 92.862986, -2.5], [-46.48959, 92.873837, -2.503062], [-46.5, 92.884687, -2.5], [-46.51041, 92.873837, -2.496938], [-46.5, 92.862986, -2.5], [-46.503062, 92.873837, -2.51041], [-46.5, 92.884687, -2.5], [-46.5, 91.850166, -2.5]]}, {"shapeName": "R_lwrArmRibbonMid_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-46.211155, 91.861017, -1.517925], [-46.200744, 91.850166, -1.520987], [-46.211155, 91.839315, -1.517925], [-46.221565, 91.850166, -1.514864], [-46.211155, 91.861017, -1.517925], [-46.208093, 91.850166, -1.507516], [-46.211155, 91.839315, -1.517925], [-46.214216, 91.850166, -1.528335], [-46.200744, 91.850166, -1.520987], [-46.208093, 91.850166, -1.507516], [-46.221565, 91.850166, -1.514864], [-46.214216, 91.850166, -1.528335], [-46.211155, 91.861017, -1.517925], [-46.208093, 91.850166, -1.507516], [-46.5, 91.850166, -2.5]]}]},
			"R_elbow_shaper_04_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_04_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-50.75, 93.600166, -1.25], [-50.814248, 93.613487, -1.231104], [-50.868714, 93.651424, -1.215084], [-50.905109, 93.708197, -1.20438], [-50.917889, 93.775166, -1.200621], [-50.905109, 93.842135, -1.20438], [-50.868714, 93.898909, -1.215084], [-50.814248, 93.936845, -1.231104], [-50.75, 93.950166, -1.25], [-50.685752, 93.936845, -1.268896], [-50.631286, 93.898909, -1.284916], [-50.594891, 93.842135, -1.29562], [-50.582111, 93.775166, -1.299379], [-50.594891, 93.708197, -1.29562], [-50.631286, 93.651424, -1.284916], [-50.685752, 93.613487, -1.268896], [-50.75, 93.600166, -1.25], [-50.75, 91.850166, -1.25]]}]},
			"R_bendyLeg_B_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.249999, 24.285649, 4.749979], [-3.799999, 24.285649, 4.749979], [-5.0, 24.290484, 5.874969], [-6.200001, 24.285649, 4.749979], [-5.750001, 24.285649, 4.749979], [-5.750001, 24.279202, 3.249995], [-7.25, 24.279202, 3.249995], [-7.25, 24.281136, 3.69999], [-8.375, 24.275979, 2.5], [-7.25, 24.270822, 1.30001], [-7.25, 24.272756, 1.750005], [-5.750001, 24.272756, 1.750005], [-5.750001, 24.266309, 0.250021], [-6.200001, 24.266309, 0.250021], [-5.0, 24.261474, -0.874969], [-3.799999, 24.266309, 0.250021], [-4.249999, 24.266309, 0.250021], [-4.249999, 24.272756, 1.750005], [-2.75, 24.272756, 1.750005], [-2.75, 24.270822, 1.30001], [-1.625, 24.275979, 2.5], [-2.75, 24.281136, 3.69999], [-2.75, 24.279202, 3.249995], [-4.249999, 24.279202, 3.249995], [-4.249999, 24.285649, 4.749979]]}]},
			"L_leg_IK_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_leg_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[7.056982, 2.775979, -3.428302], [5.0, 2.775979, -4.848349], [2.943018, 2.775979, -3.428302], [2.090991, 2.775979, 0.0], [2.943018, 2.775979, 3.428303], [5.0, 2.775979, 4.848349], [7.056982, 2.775979, 3.428303], [7.909009, 2.775979, 0.0]]}]},
			"R_loLeg_shaper_05_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_05_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-13.75, 6.359312, 0.416667], [-13.816605, 5.960188, 0.370257], [-14.006287, 5.621826, 0.330912], [-14.290155, 5.395731, 0.304622], [-14.625, 5.31634, 0.295391], [-14.959845, 5.395731, 0.304622], [-15.243712, 5.621826, 0.330912], [-15.433395, 5.960188, 0.370257], [-15.5, 6.359312, 0.416667], [-15.433395, 6.758437, 0.463077], [-15.243712, 7.096798, 0.502421], [-14.959845, 7.322894, 0.528711], [-14.625, 7.402285, 0.537943], [-14.290155, 7.322894, 0.528711], [-14.006287, 7.096798, 0.502421], [-13.816605, 6.758437, 0.463077], [-13.75, 6.359312, 0.416667], [-5.0, 6.359312, 0.416667]]}]},
			"R_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.03129, 92.022187, 6.056515], [-66.994233, 92.002328, 6.120699], [-67.004162, 91.928214, 6.103501], [-67.041219, 91.948073, 6.039317], [-67.03129, 92.022187, 6.056515], [-67.064708, 91.9752, 6.107133], [-67.004162, 91.928214, 6.103501], [-66.97074, 91.9752, 6.05288], [-66.994233, 92.002328, 6.120699], [-67.064708, 91.9752, 6.107133], [-67.041219, 91.948073, 6.039317], [-66.97074, 91.9752, 6.05288], [-67.03129, 92.022187, 6.056515], [-67.064708, 91.9752, 6.107133], [-62.5851, 91.9752, 3.52083]]}, {"shapeName": "R_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-60.382352, 94.581364, 7.336103], [-60.321802, 94.534378, 7.332469], [-60.355224, 94.487392, 7.38309], [-60.415774, 94.534378, 7.386724], [-60.382352, 94.581364, 7.336103], [-60.345297, 94.561503, 7.400284], [-60.355224, 94.487392, 7.38309], [-60.392281, 94.50725, 7.318905], [-60.321802, 94.534378, 7.332469], [-60.345297, 94.561503, 7.400284], [-60.415774, 94.534378, 7.386724], [-60.392281, 94.50725, 7.318905], [-60.382352, 94.581364, 7.336103], [-60.345297, 94.561503, 7.400284], [-62.5851, 91.9752, 3.52083]]}, {"shapeName": "R_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.282019, 87.569702, 5.777834], [-61.258526, 87.542575, 5.710016], [-61.329005, 87.515447, 5.696452], [-61.352498, 87.542575, 5.764271], [-61.282019, 87.569702, 5.777834], [-61.291949, 87.495593, 5.760634], [-61.329005, 87.515447, 5.696452], [-61.319075, 87.589561, 5.71365], [-61.258526, 87.542575, 5.710016], [-61.291949, 87.495593, 5.760634], [-61.352498, 87.542575, 5.764271], [-61.319075, 87.589561, 5.71365], [-61.282019, 87.569702, 5.777834], [-61.291949, 87.495593, 5.760634], [-62.5851, 91.9752, 3.52083]]}]},
			"R_upLeg_shaper_04_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_04_CTLShape", "degree": 1, "form": 0, "points": [[-17.5, 30.942646, 1.666667], [-17.59515, 30.373058, 1.737865], [-17.866125, 29.890186, 1.798224], [-18.27165, 29.567527, 1.838556], [-18.75, 29.454229, 1.852719], [-19.22835, 29.567527, 1.838556], [-19.633875, 29.890186, 1.798224], [-19.90485, 30.373058, 1.737865], [-20.0, 30.942646, 1.666667], [-19.90485, 31.512233, 1.595468], [-19.633875, 31.995105, 1.535109], [-19.22835, 32.317764, 1.494777], [-18.75, 32.431062, 1.480615], [-18.27165, 32.317764, 1.494777], [-17.866125, 31.995105, 1.535109], [-17.59515, 31.512233, 1.595468], [-17.5, 30.942646, 1.666667], [-5.0, 30.942646, 1.666667]]}]},
			"R_ankleOffset_CTL": {"color": 20, "shapes": [{"shapeName": "R_ankleOffset_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 1.519363, -0.558159], [-5.0, 4.28446, 1.669426], [-5.0, 4.990662, 1.705192], [-5.5, 4.619678, 2.04041], [-5.0, 4.954896, 2.411394], [-5.0, 4.990662, 1.705192], [-4.5, 4.619678, 2.04041], [-5.0, 4.28446, 1.669426], [-5.0, 4.248695, 2.375628], [-4.5, 4.619678, 2.04041], [-5.0, 4.954896, 2.411394], [-5.0, 4.248695, 2.375628], [-5.5, 4.619678, 2.04041], [-5.0, 4.28446, 1.669426]]}]},
			"L_elbow_shaper_04_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_elbow_shaper_04_PIV_CTLShape", "degree": 1, "form": 0, "points": [[51.735136, 91.850166, -0.971565], [51.732075, 91.861017, -0.961155], [51.729013, 91.850166, -0.950744], [51.732075, 91.839315, -0.961155], [51.735136, 91.850166, -0.971565], [51.742484, 91.850166, -0.958093], [51.729013, 91.850166, -0.950744], [51.721665, 91.850166, -0.964216], [51.732075, 91.861017, -0.961155], [51.742484, 91.850166, -0.958093], [51.732075, 91.839315, -0.961155], [51.721665, 91.850166, -0.964216], [51.735136, 91.850166, -0.971565], [51.742484, 91.850166, -0.958093], [50.75, 91.850166, -1.25]]}, {"shapeName": "L_elbow_shaper_04_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[50.753062, 92.873837, -1.26041], [50.73959, 92.873837, -1.253062], [50.746938, 92.873837, -1.23959], [50.76041, 92.873837, -1.246938], [50.753062, 92.873837, -1.26041], [50.75, 92.884687, -1.25], [50.746938, 92.873837, -1.23959], [50.75, 92.862986, -1.25], [50.73959, 92.873837, -1.253062], [50.75, 92.884687, -1.25], [50.76041, 92.873837, -1.246938], [50.75, 92.862986, -1.25], [50.753062, 92.873837, -1.26041], [50.75, 92.884687, -1.25], [50.75, 91.850166, -1.25]]}, {"shapeName": "L_elbow_shaper_04_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[50.461155, 91.861017, -0.267925], [50.450744, 91.850166, -0.270987], [50.461155, 91.839315, -0.267925], [50.471565, 91.850166, -0.264864], [50.461155, 91.861017, -0.267925], [50.458093, 91.850166, -0.257516], [50.461155, 91.839315, -0.267925], [50.464216, 91.850166, -0.278335], [50.450744, 91.850166, -0.270987], [50.458093, 91.850166, -0.257516], [50.471565, 91.850166, -0.264864], [50.464216, 91.850166, -0.278335], [50.461155, 91.861017, -0.267925], [50.458093, 91.850166, -0.257516], [50.75, 91.850166, -1.25]]}]},
			"R_arm_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-56.023671, 91.850166, -0.010851], [-56.023671, 91.861017, 0.0], [-56.023671, 91.850166, 0.010851], [-56.023671, 91.839315, -0.0], [-56.023671, 91.850166, -0.010851], [-56.034521, 91.850166, -0.0], [-56.023671, 91.850166, 0.010851], [-56.01282, 91.850166, -0.0], [-56.023671, 91.861017, 0.0], [-56.034521, 91.850166, -0.0], [-56.023671, 91.839315, -0.0], [-56.01282, 91.850166, -0.0], [-56.023671, 91.850166, -0.010851], [-56.034521, 91.850166, -0.0], [-55.0, 91.850166, -0.0]]}, {"shapeName": "R_arm_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-55.0, 92.873837, -0.010851], [-54.989149, 92.873837, 0.0], [-55.0, 92.873837, 0.010851], [-55.010851, 92.873837, 0.0], [-55.0, 92.873837, -0.010851], [-55.0, 92.884687, 0.0], [-55.0, 92.873837, 0.010851], [-55.0, 92.862986, 0.0], [-54.989149, 92.873837, 0.0], [-55.0, 92.884687, 0.0], [-55.010851, 92.873837, 0.0], [-55.0, 92.862986, 0.0], [-55.0, 92.873837, -0.010851], [-55.0, 92.884687, 0.0], [-55.0, 91.850166, -0.0]]}, {"shapeName": "R_arm_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-55.0, 91.861017, 1.023671], [-54.989149, 91.850166, 1.023671], [-55.0, 91.839315, 1.023671], [-55.010851, 91.850166, 1.023671], [-55.0, 91.861017, 1.023671], [-55.0, 91.850166, 1.034521], [-55.0, 91.839315, 1.023671], [-55.0, 91.850166, 1.01282], [-54.989149, 91.850166, 1.023671], [-55.0, 91.850166, 1.034521], [-55.010851, 91.850166, 1.023671], [-55.0, 91.850166, 1.01282], [-55.0, 91.861017, 1.023671], [-55.0, 91.850166, 1.034521], [-55.0, 91.850166, -0.0]]}]},
			"R_elbowRibbon_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_elbowRibbon_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-38.022657, 92.850168, -7.999914], [-38.022657, 93.450168, -7.999914], [-38.033985, 91.850166, -9.499872], [-38.022657, 90.250164, -7.999914], [-38.022657, 90.850164, -7.999914], [-38.007552, 90.850164, -5.999973], [-38.007552, 88.850166, -5.999973], [-38.012084, 88.850166, -6.599956], [-38.0, 87.350166, -5.0], [-37.987916, 88.850166, -3.400044], [-37.992448, 88.850166, -4.000027], [-37.992448, 90.850164, -4.000027], [-37.977343, 90.850164, -2.000086], [-37.977343, 90.250164, -2.000086], [-37.966015, 91.850166, -0.500128], [-37.977343, 93.450168, -2.000086], [-37.977343, 92.850168, -2.000086], [-37.992448, 92.850168, -4.000027], [-37.992448, 94.850166, -4.000027], [-37.987916, 94.850166, -3.400044], [-38.0, 96.350166, -5.0], [-38.012084, 94.850166, -6.599956], [-38.007552, 94.850166, -5.999973], [-38.007552, 92.850168, -5.999973], [-38.022657, 92.850168, -7.999914]]}]},
			"R_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_A_CTLShape", "degree": 1, "form": 0, "points": [[-61.894298, 92.69271, -1.75], [-60.407456, 92.494464, -1.75], [-60.407456, 92.494464, -3.25], [-61.894298, 92.69271, -3.25], [-62.092544, 91.205868, -3.25], [-60.605702, 91.007623, -3.25], [-60.605702, 91.007623, -1.75], [-62.092544, 91.205868, -1.75], [-61.894298, 92.69271, -1.75], [-61.894298, 92.69271, -3.25], [-60.407456, 92.494464, -3.25], [-60.605702, 91.007623, -3.25], [-62.092544, 91.205868, -3.25], [-62.092544, 91.205868, -1.75], [-60.605702, 91.007623, -1.75], [-60.407456, 92.494464, -1.75]]}]},
			"L_handIk_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_handIk_PIV_CTLShape", "degree": 1, "form": 0, "points": [[56.023671, 91.850166, -0.010851], [56.023671, 91.861017, 0.0], [56.023671, 91.850166, 0.010851], [56.023671, 91.839315, 0.0], [56.023671, 91.850166, -0.010851], [56.034521, 91.850166, 0.0], [56.023671, 91.850166, 0.010851], [56.01282, 91.850166, 0.0], [56.023671, 91.861017, 0.0], [56.034521, 91.850166, 0.0], [56.023671, 91.839315, 0.0], [56.01282, 91.850166, 0.0], [56.023671, 91.850166, -0.010851], [56.034521, 91.850166, 0.0], [55.0, 91.850166, 0.0]]}, {"shapeName": "L_handIk_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[55.0, 92.873837, -0.010851], [54.989149, 92.873837, 0.0], [55.0, 92.873837, 0.010851], [55.010851, 92.873837, 0.0], [55.0, 92.873837, -0.010851], [55.0, 92.884687, 0.0], [55.0, 92.873837, 0.010851], [55.0, 92.862986, 0.0], [54.989149, 92.873837, 0.0], [55.0, 92.884687, 0.0], [55.010851, 92.873837, 0.0], [55.0, 92.862986, 0.0], [55.0, 92.873837, -0.010851], [55.0, 92.884687, 0.0], [55.0, 91.850166, 0.0]]}, {"shapeName": "L_handIk_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[55.0, 91.861017, 1.023671], [54.989149, 91.850166, 1.023671], [55.0, 91.839315, 1.023671], [55.010851, 91.850166, 1.023671], [55.0, 91.861017, 1.023671], [55.0, 91.850166, 1.034521], [55.0, 91.839315, 1.023671], [55.0, 91.850166, 1.01282], [54.989149, 91.850166, 1.023671], [55.0, 91.850166, 1.034521], [55.010851, 91.850166, 1.023671], [55.0, 91.850166, 1.01282], [55.0, 91.861017, 1.023671], [55.0, 91.850166, 1.034521], [55.0, 91.850166, 0.0]]}]},
			"L_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_D_CTLShape", "degree": 1, "form": 0, "points": [[67.717544, 92.744464, 2.0], [66.230702, 92.94271, 2.0], [66.230702, 92.94271, 0.5], [67.717544, 92.744464, 0.5], [67.519298, 91.257623, 0.5], [66.032456, 91.455868, 0.5], [66.032456, 91.455868, 2.0], [67.519298, 91.257623, 2.0], [67.717544, 92.744464, 2.0], [67.717544, 92.744464, 0.5], [66.230702, 92.94271, 0.5], [66.032456, 91.455868, 0.5], [67.519298, 91.257623, 0.5], [67.519298, 91.257623, 2.0], [66.032456, 91.455868, 2.0], [66.230702, 92.94271, 2.0]]}]},
			"R_loLeg_shaper_01_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_01_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-15.0, 20.692646, 2.083333], [-15.07612, 20.236503, 2.030293], [-15.2929, 19.849804, 1.985329], [-15.61732, 19.591409, 1.955283], [-16.0, 19.500677, 1.944732], [-16.38268, 19.591409, 1.955283], [-16.7071, 19.849804, 1.985329], [-16.92388, 20.236503, 2.030293], [-17.0, 20.692646, 2.083333], [-16.92388, 21.148788, 2.136373], [-16.7071, 21.535487, 2.181338], [-16.38268, 21.793882, 2.211384], [-16.0, 21.884614, 2.221934], [-15.61732, 21.793882, 2.211384], [-15.2929, 21.535487, 2.181338], [-15.07612, 21.148788, 2.136373], [-15.0, 20.692646, 2.083333], [-5.0, 20.692646, 2.083333]]}]},
			"L_upLeg_shaper_01_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_01_CTLShape", "degree": 1, "form": 0, "points": [[17.5, 40.942646, 0.416667], [17.59515, 40.373058, 0.487865], [17.866125, 39.890186, 0.548224], [18.27165, 39.567527, 0.588556], [18.75, 39.454229, 0.602719], [19.22835, 39.567527, 0.588556], [19.633875, 39.890186, 0.548224], [19.90485, 40.373058, 0.487865], [20.0, 40.942646, 0.416667], [19.90485, 41.512233, 0.345468], [19.633875, 41.995105, 0.285109], [19.22835, 42.317764, 0.244777], [18.75, 42.431062, 0.230615], [18.27165, 42.317764, 0.244777], [17.866125, 41.995105, 0.285109], [17.59515, 41.512233, 0.345468], [17.5, 40.942646, 0.416667], [5.0, 40.942646, 0.416667]]}]},
			"R_upLeg_shaper_05_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_05_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-12.5, 27.609312, 2.083333], [-12.55709, 27.26756, 2.126052], [-12.719675, 26.977837, 2.162268], [-12.96299, 26.784241, 2.186467], [-13.25, 26.716262, 2.194965], [-13.53701, 26.784241, 2.186467], [-13.780325, 26.977837, 2.162268], [-13.94291, 27.26756, 2.126052], [-14.0, 27.609312, 2.083333], [-13.94291, 27.951065, 2.040614], [-13.780325, 28.240788, 2.004399], [-13.53701, 28.434383, 1.980199], [-13.25, 28.502362, 1.971702], [-12.96299, 28.434383, 1.980199], [-12.719675, 28.240788, 2.004399], [-12.55709, 27.951065, 2.040614], [-12.5, 27.609312, 2.083333], [-5.0, 27.609312, 2.083333]]}]},
			"L_loLeg_shaper_02_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_02_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.25, 17.109312, 1.666667], [16.335635, 16.596152, 1.606997], [16.579512, 16.161116, 1.556411], [16.944485, 15.870422, 1.52261], [17.375, 15.768347, 1.510741], [17.805515, 15.870422, 1.52261], [18.170488, 16.161116, 1.556411], [18.414365, 16.596152, 1.606997], [18.5, 17.109312, 1.666667], [18.414365, 17.622473, 1.726336], [18.170488, 18.057509, 1.776922], [17.805515, 18.348203, 1.810724], [17.375, 18.450277, 1.822593], [16.944485, 18.348203, 1.810724], [16.579512, 18.057509, 1.776922], [16.335635, 17.622473, 1.726336], [16.25, 17.109312, 1.666667], [5.0, 17.109312, 1.666667]]}]},
			"R_legBase_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_CTLShape", "degree": 3, "form": 0, "points": [[-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 44.429485, 1.228048], [-5.0, 44.677862, 3.215062], [-5.0, 44.772733, 3.974036], [-9.70811, 44.677862, 3.215062], [-12.617885, 44.429485, 1.228048], [-12.617885, 44.122473, -1.228048], [-9.70811, 43.874096, -3.215062], [-5.0, 43.779225, -3.974036], [-5.0, 43.874096, -3.215062], [-5.0, 44.122473, -1.228048], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0], [-5.0, 44.275979, 0.0]]}]},
			"C_neckBase_D_OFF_CTL": {"color": 25, "shapes": [{"shapeName": "C_neckBase_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[3.895745, 94.094715, -3.132621], [-0.057114, 92.244382, -3.827951], [-4.294931, 93.262218, -3.094987], [-4.277714, 93.373055, 3.103982], [0.081778, 91.331362, 6.20381], [3.912962, 94.205552, 3.066349], [3.895745, 94.094715, -3.132621]]}]},
			"L_upLeg_shaper_01_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_01_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[15.0, 40.942646, 0.416667], [15.07612, 40.486976, 0.473625], [15.2929, 40.100678, 0.521913], [15.61732, 39.842551, 0.554179], [16.0, 39.751912, 0.565508], [16.38268, 39.842551, 0.554179], [16.7071, 40.100678, 0.521913], [16.92388, 40.486976, 0.473625], [17.0, 40.942646, 0.416667], [16.92388, 41.398316, 0.359708], [16.7071, 41.784613, 0.311421], [16.38268, 42.04274, 0.279155], [16.0, 42.133379, 0.267825], [15.61732, 42.04274, 0.279155], [15.2929, 41.784613, 0.311421], [15.07612, 41.398316, 0.359708], [15.0, 40.942646, 0.416667], [5.0, 40.942646, 0.416667]]}]},
			"R_shoulder_shaper_04_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_shaper_04_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-34.483421, 91.850166, -4.034434], [-34.486325, 91.861017, -4.023979], [-34.48923, 91.850166, -4.013524], [-34.486325, 91.839315, -4.023979], [-34.483421, 91.850166, -4.034434], [-34.49678, 91.850166, -4.026883], [-34.48923, 91.850166, -4.013524], [-34.47587, 91.850166, -4.021075], [-34.486325, 91.861017, -4.023979], [-34.49678, 91.850166, -4.026883], [-34.486325, 91.839315, -4.023979], [-34.47587, 91.850166, -4.021075], [-34.483421, 91.850166, -4.034434], [-34.49678, 91.850166, -4.026883], [-33.5, 91.850166, -3.75]]}, {"shapeName": "R_shoulder_shaper_04_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-33.497096, 92.873837, -3.760455], [-33.489545, 92.873837, -3.747096], [-33.502904, 92.873837, -3.739545], [-33.510455, 92.873837, -3.752904], [-33.497096, 92.873837, -3.760455], [-33.5, 92.884687, -3.75], [-33.502904, 92.873837, -3.739545], [-33.5, 92.862986, -3.75], [-33.489545, 92.873837, -3.747096], [-33.5, 92.884687, -3.75], [-33.510455, 92.873837, -3.752904], [-33.5, 92.862986, -3.75], [-33.497096, 92.873837, -3.760455], [-33.5, 92.884687, -3.75], [-33.5, 91.850166, -3.75]]}, {"shapeName": "R_shoulder_shaper_04_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-33.773979, 91.861017, -2.763675], [-33.763524, 91.850166, -2.76077], [-33.773979, 91.839315, -2.763675], [-33.784434, 91.850166, -2.766579], [-33.773979, 91.861017, -2.763675], [-33.776883, 91.850166, -2.75322], [-33.773979, 91.839315, -2.763675], [-33.771075, 91.850166, -2.77413], [-33.763524, 91.850166, -2.76077], [-33.776883, 91.850166, -2.75322], [-33.784434, 91.850166, -2.766579], [-33.771075, 91.850166, -2.77413], [-33.773979, 91.861017, -2.763675], [-33.776883, 91.850166, -2.75322], [-33.5, 91.850166, -3.75]]}]},
			"R_bendyLeg_B_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.416665, 24.2835, 4.249984], [-4.066666, 24.2835, 4.249984], [-5.0, 24.287261, 5.124976], [-5.933334, 24.2835, 4.249984], [-5.583335, 24.2835, 4.249984], [-5.583335, 24.278486, 3.083329], [-6.75, 24.278486, 3.083329], [-6.75, 24.27999, 3.433326], [-7.625, 24.275979, 2.5], [-6.75, 24.271968, 1.566674], [-6.75, 24.273472, 1.916671], [-5.583335, 24.273472, 1.916671], [-5.583335, 24.268458, 0.750016], [-5.933334, 24.268458, 0.750016], [-5.0, 24.264697, -0.124976], [-4.066666, 24.268458, 0.750016], [-4.416665, 24.268458, 0.750016], [-4.416665, 24.273472, 1.916671], [-3.25, 24.273472, 1.916671], [-3.25, 24.271968, 1.566674], [-2.375, 24.275979, 2.5], [-3.25, 24.27999, 3.433326], [-3.25, 24.278486, 3.083329], [-4.416665, 24.278486, 3.083329], [-4.416665, 24.2835, 4.249984]]}]},
			"R_elbow_shaper_03_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_03_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-46.5, 93.600166, -2.5], [-46.564248, 93.613487, -2.481104], [-46.618714, 93.651424, -2.465084], [-46.655109, 93.708197, -2.45438], [-46.667889, 93.775166, -2.450621], [-46.655109, 93.842135, -2.45438], [-46.618714, 93.898909, -2.465084], [-46.564248, 93.936845, -2.481104], [-46.5, 93.950166, -2.5], [-46.435752, 93.936845, -2.518896], [-46.381286, 93.898909, -2.534916], [-46.344891, 93.842135, -2.54562], [-46.332111, 93.775166, -2.549379], [-46.344891, 93.708197, -2.54562], [-46.381286, 93.651424, -2.534916], [-46.435752, 93.613487, -2.518896], [-46.5, 93.600166, -2.5], [-46.5, 91.850166, -2.5]]}]},
			"R_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.227054, 92.508365, -1.304255], [-68.222728, 92.562447, -1.25], [-68.227054, 92.508365, -1.195745], [-68.231381, 92.454282, -1.25], [-68.227054, 92.508365, -1.304255], [-68.281132, 92.512691, -1.25], [-68.227054, 92.508365, -1.195745], [-68.172972, 92.504038, -1.25], [-68.222728, 92.562447, -1.25], [-68.281132, 92.512691, -1.25], [-68.231381, 92.454282, -1.25], [-68.172972, 92.504038, -1.25], [-68.227054, 92.508365, -1.304255], [-68.281132, 92.512691, -1.25], [-63.125, 92.1002, -1.25]]}, {"shapeName": "R_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-62.716836, 97.202255, -1.304255], [-62.662753, 97.197928, -1.25], [-62.716836, 97.202255, -1.195745], [-62.770918, 97.206581, -1.25], [-62.716836, 97.202255, -1.304255], [-62.712509, 97.256332, -1.25], [-62.716836, 97.202255, -1.195745], [-62.721162, 97.148173, -1.25], [-62.662753, 97.197928, -1.25], [-62.712509, 97.256332, -1.25], [-62.770918, 97.206581, -1.25], [-62.721162, 97.148173, -1.25], [-62.716836, 97.202255, -1.304255], [-62.712509, 97.256332, -1.25], [-63.125, 92.1002, -1.25]]}, {"shapeName": "R_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-63.120673, 92.154283, 3.868355], [-63.070918, 92.095874, 3.868355], [-63.129327, 92.046118, 3.868355], [-63.179082, 92.104527, 3.868355], [-63.120673, 92.154283, 3.868355], [-63.125, 92.1002, 3.922605], [-63.129327, 92.046118, 3.868355], [-63.125, 92.1002, 3.8141], [-63.070918, 92.095874, 3.868355], [-63.125, 92.1002, 3.922605], [-63.179082, 92.104527, 3.868355], [-63.125, 92.1002, 3.8141], [-63.120673, 92.154283, 3.868355], [-63.125, 92.1002, 3.922605], [-63.125, 92.1002, -1.25]]}]},
			"L_outterBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_outterBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[12.618355, 0.275979, 4.945745], [12.618355, 0.330234, 5.0], [12.618355, 0.275979, 5.054255], [12.618355, 0.221724, 5.0], [12.618355, 0.275979, 4.945745], [12.672605, 0.275979, 5.0], [12.618355, 0.275979, 5.054255], [12.5641, 0.275979, 5.0], [12.618355, 0.330234, 5.0], [12.672605, 0.275979, 5.0], [12.618355, 0.221724, 5.0], [12.5641, 0.275979, 5.0], [12.618355, 0.275979, 4.945745], [12.672605, 0.275979, 5.0], [7.5, 0.275979, 5.0]]}, {"shapeName": "L_outterBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.5, 5.394334, 4.945745], [7.445745, 5.394334, 5.0], [7.5, 5.394334, 5.054255], [7.554255, 5.394334, 5.0], [7.5, 5.394334, 4.945745], [7.5, 5.448584, 5.0], [7.5, 5.394334, 5.054255], [7.5, 5.340079, 5.0], [7.445745, 5.394334, 5.0], [7.5, 5.448584, 5.0], [7.554255, 5.394334, 5.0], [7.5, 5.340079, 5.0], [7.5, 5.394334, 4.945745], [7.5, 5.448584, 5.0], [7.5, 0.275979, 5.0]]}, {"shapeName": "L_outterBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.5, 0.330234, 10.118355], [7.445745, 0.275979, 10.118355], [7.5, 0.221724, 10.118355], [7.554255, 0.275979, 10.118355], [7.5, 0.330234, 10.118355], [7.5, 0.275979, 10.172605], [7.5, 0.221724, 10.118355], [7.5, 0.275979, 10.0641], [7.445745, 0.275979, 10.118355], [7.5, 0.275979, 10.172605], [7.554255, 0.275979, 10.118355], [7.5, 0.275979, 10.0641], [7.5, 0.330234, 10.118355], [7.5, 0.275979, 10.172605], [7.5, 0.275979, 5.0]]}]},
			"R_loLeg_shaper_02_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_02_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-12.5, 17.109312, 1.666667], [-12.55709, 16.767205, 1.626887], [-12.719675, 16.477181, 1.593163], [-12.96299, 16.283385, 1.570629], [-13.25, 16.215336, 1.562716], [-13.53701, 16.283385, 1.570629], [-13.780325, 16.477181, 1.593163], [-13.94291, 16.767205, 1.626887], [-14.0, 17.109312, 1.666667], [-13.94291, 17.451419, 1.706447], [-13.780325, 17.741443, 1.74017], [-13.53701, 17.935239, 1.762705], [-13.25, 18.003289, 1.770617], [-12.96299, 17.935239, 1.762705], [-12.719675, 17.741443, 1.74017], [-12.55709, 17.451419, 1.706447], [-12.5, 17.109312, 1.666667], [-5.0, 17.109312, 1.666667]]}]},
			"R_elbowFk_CTL": {"color": 6, "shapes": [{"shapeName": "R_elbowFk_CTLShape", "degree": 1, "form": 0, "points": [[-39.692998, 94.350166, -1.89617], [-34.89617, 94.350166, -3.307002], [-36.307002, 94.350166, -8.10383], [-41.10383, 94.350166, -6.692998], [-41.10383, 89.350166, -6.692998], [-36.307002, 89.350166, -8.10383], [-34.89617, 89.350166, -3.307002], [-39.692998, 89.350166, -1.89617], [-39.692998, 94.350166, -1.89617], [-41.10383, 94.350166, -6.692998], [-36.307002, 94.350166, -8.10383], [-36.307002, 89.350166, -8.10383], [-41.10383, 89.350166, -6.692998], [-39.692998, 89.350166, -1.89617], [-34.89617, 89.350166, -3.307002], [-34.89617, 94.350166, -3.307002]]}]},
			"R_shoulder_shaper_04_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_04_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-33.5, 93.600166, -3.75], [-33.564526, 93.613487, -3.767924], [-33.619228, 93.651424, -3.783119], [-33.655781, 93.708197, -3.793272], [-33.668616, 93.775166, -3.796838], [-33.655781, 93.842135, -3.793272], [-33.619228, 93.898909, -3.783119], [-33.564526, 93.936845, -3.767924], [-33.5, 93.950166, -3.75], [-33.435474, 93.936845, -3.732076], [-33.380772, 93.898909, -3.716881], [-33.344219, 93.842135, -3.706728], [-33.331384, 93.775166, -3.703162], [-33.344219, 93.708197, -3.706728], [-33.380772, 93.651424, -3.716881], [-33.435474, 93.613487, -3.732076], [-33.5, 93.600166, -3.75], [-33.5, 91.850166, -3.75]]}]},
			"R_clavicle_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_clavicle_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-3.399131, 91.850166, -2.481701], [-2.022404, 91.850166, -6.497156], [-1.496539, 91.850166, -8.030928], [-2.022404, 96.84036, -6.497156], [-3.399131, 99.924474, -2.481701], [-5.100869, 99.924474, 2.481701], [-6.477596, 96.84036, 6.497156], [-7.003461, 91.850166, 8.030928], [-6.477596, 91.850166, 6.497156], [-5.100869, 91.850166, 2.481701], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0]]}]},
			"world_A_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -32.495625], [14.436563, 0.0, -18.045], [10.8225, 0.0, -18.045], [10.8225, 0.0, -10.819687], [18.047812, 0.0, -10.819687], [18.047812, 0.0, -14.43375], [32.495625, 0.0, 0.0], [18.045, 0.0, 14.436563], [18.045, 0.0, 10.8225], [10.819687, 0.0, 10.8225], [10.819687, 0.0, 18.047812], [14.43375, 0.0, 18.047812], [0.0, 0.0, 32.495625], [-14.436563, 0.0, 18.045], [-10.8225, 0.0, 18.045], [-10.8225, 0.0, 10.819687], [-18.047812, 0.0, 10.819687], [-18.047812, 0.0, 14.43375], [-32.495625, 0.0, 0.0], [-18.045, 0.0, -14.436563], [-18.045, 0.0, -10.8225], [-10.819687, 0.0, -10.8225], [-10.819687, 0.0, -18.047812], [-14.43375, 0.0, -18.047812], [0.0, 0.0, -32.495625], [2.829375, 0.039375, -29.716875], [2.581875, 0.0, -29.4525], [2.581875, 0.0, -28.3725], [2.356875, 0.0, -28.3725], [2.370938, 0.0, -29.460938], [2.210625, 0.0, -29.379375], [2.21625, 0.0, -28.906875], [1.988438, 0.0, -28.906875], [1.988438, 0.0, -29.379375], [1.847813, 0.0, -29.460938], [1.847813, 0.0, -28.355625], [1.62, 0.0, -28.355625], [1.62, 0.0, -29.489062], [1.802812, 0.0, -29.671875], [2.084062, 0.0, -29.53125], [2.393438, 0.0, -29.671875], [2.581875, 0.0, -29.458125], [2.393438, 0.0, -29.671875], [2.086875, 0.0, -29.534063], [1.802812, 0.0, -29.669063], [1.254375, 0.0, -29.671875], [1.44, 0.0, -29.489062], [1.44, 0.0, -28.54125], [1.254375, 0.0, -28.355625], [0.660938, 0.0, -28.355625], [0.478125, 0.0, -28.54125], [0.478125, 0.0, -29.489062], [0.660938, 0.0, -29.671875], [1.254375, 0.0, -29.671875], [1.184063, 0.0, -29.460938], [1.212187, 0.0, -28.589063], [0.703125, 0.0, -28.594687], [0.705937, 0.0, -29.460938], [1.186875, 0.0, -29.466562], [1.254375, 0.0, -29.671875], [0.660938, 0.0, -29.671875], [0.28125, 0.0, -29.671875], [0.295313, 0.0, -28.355625], [-0.345938, 0.0, -28.355625], [-0.531562, 0.0, -28.54125], [-0.531562, 0.0, -28.937812], [-0.343125, 0.0, -29.120625], [-0.331875, 0.0, -29.134688], [-0.700313, 0.0, -29.66625], [-0.700313, 0.0, -29.671875], [-0.435937, 0.0, -29.671875], [-0.0675, 0.0, -29.1375], [0.070313, 0.0, -29.1375], [0.070313, 0.0, -28.575], [-0.284062, 0.0, -28.575], [-0.286875, 0.0, -28.909688], [0.070313, 0.0, -28.909688], [0.070313, 0.0, -29.671875], [0.28125, 0.0, -29.671875], [-1.808437, 0.0, -29.671875], [-1.808437, 0.0, -29.460938], [-1.071563, 0.0, -29.458125], [-1.071563, 0.0, -28.355625], [-0.84375, 0.0, -28.355625], [-0.84375, 0.0, -29.671875], [-2.7675, 0.0, -29.671875], [-2.93625, 0.0, -29.489062], [-2.950313, 0.0, -28.54125], [-2.7675, 0.0, -28.355625], [-1.988438, 0.0, -28.355625], [-1.988438, 0.0, -29.671875], [-2.219063, 0.0, -29.460938], [-2.213437, 0.0, -28.569375], [-2.694375, 0.0, -28.569375], [-2.68875, 0.0, -29.455313], [-2.210625, 0.0, -29.466562], [-1.982812, 0.0, -29.671875]]}]},
			"C_cog_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_cog_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 49.350166, -0.054255], [5.118355, 49.404421, 0.0], [5.118355, 49.350166, 0.054255], [5.118355, 49.295911, 0.0], [5.118355, 49.350166, -0.054255], [5.172605, 49.350166, 0.0], [5.118355, 49.350166, 0.054255], [5.0641, 49.350166, 0.0], [5.118355, 49.404421, 0.0], [5.172605, 49.350166, 0.0], [5.118355, 49.295911, 0.0], [5.0641, 49.350166, 0.0], [5.118355, 49.350166, -0.054255], [5.172605, 49.350166, 0.0], [0.0, 49.350166, 0.0]]}, {"shapeName": "C_cog_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 54.468521, -0.054255], [-0.054255, 54.468521, 0.0], [0.0, 54.468521, 0.054255], [0.054255, 54.468521, 0.0], [0.0, 54.468521, -0.054255], [0.0, 54.522771, 0.0], [0.0, 54.468521, 0.054255], [0.0, 54.414266, 0.0], [-0.054255, 54.468521, 0.0], [0.0, 54.522771, 0.0], [0.054255, 54.468521, 0.0], [0.0, 54.414266, 0.0], [0.0, 54.468521, -0.054255], [0.0, 54.522771, 0.0], [0.0, 49.350166, 0.0]]}, {"shapeName": "C_cog_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 49.404421, 5.118355], [-0.054255, 49.350166, 5.118355], [0.0, 49.295911, 5.118355], [0.054255, 49.350166, 5.118355], [0.0, 49.404421, 5.118355], [0.0, 49.350166, 5.172605], [0.0, 49.295911, 5.118355], [0.0, 49.350166, 5.0641], [-0.054255, 49.350166, 5.118355], [0.0, 49.350166, 5.172605], [0.054255, 49.350166, 5.118355], [0.0, 49.350166, 5.0641], [0.0, 49.404421, 5.118355], [0.0, 49.350166, 5.172605], [0.0, 49.350166, 0.0]]}]},
			"L_elbow_shaper_03_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_03_CTLShape", "degree": 1, "form": 0, "points": [[46.5, 94.350166, -2.5], [46.591782, 94.369196, -2.473005], [46.669592, 94.423391, -2.45012], [46.721585, 94.504496, -2.434828], [46.739841, 94.600166, -2.429458], [46.721585, 94.695836, -2.434828], [46.669592, 94.776941, -2.45012], [46.591782, 94.831136, -2.473005], [46.5, 94.850166, -2.5], [46.408218, 94.831136, -2.526995], [46.330408, 94.776941, -2.54988], [46.278415, 94.695836, -2.565172], [46.260159, 94.600166, -2.570542], [46.278415, 94.504496, -2.565172], [46.330408, 94.423391, -2.54988], [46.408218, 94.369196, -2.526995], [46.5, 94.350166, -2.5], [46.5, 91.850166, -2.5]]}]},
			"C_midNeck_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[4.936756, 96.850166, -4.113963], [0.0, 96.850166, -5.818018], [-4.936756, 96.850166, -4.113963], [-6.981622, 96.850166, 0.0], [-4.936756, 96.850166, 4.113963], [0.0, 96.850166, 5.818018], [4.936756, 96.850166, 4.113963], [6.981622, 96.850166, 0.0]]}]},
			"R_upLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 39.203878, 0.68869], [-4.945745, 39.197149, 0.634854], [-5.0, 39.190419, 0.581018], [-5.054255, 39.197149, 0.634854], [-5.0, 39.203878, 0.68869], [-5.0, 39.143317, 0.641583], [-5.0, 39.190419, 0.581018], [-5.0, 39.250985, 0.628124], [-4.945745, 39.197149, 0.634854], [-5.0, 39.143317, 0.641583], [-5.054255, 39.197149, 0.634854], [-5.0, 39.250985, 0.628124], [-5.0, 39.203878, 0.68869], [-5.0, 39.143317, 0.641583], [-5.0, 44.275979, 0.0]]}, {"shapeName": "R_upLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 44.282708, 0.053836], [0.118355, 44.329815, -0.00673], [0.118355, 44.269249, -0.053836], [0.118355, 44.222143, 0.00673], [0.118355, 44.282708, 0.053836], [0.172605, 44.275979, 0.0], [0.118355, 44.269249, -0.053836], [0.0641, 44.275979, 0.0], [0.118355, 44.329815, -0.00673], [0.172605, 44.275979, 0.0], [0.118355, 44.222143, 0.00673], [0.0641, 44.275979, 0.0], [0.118355, 44.282708, 0.053836], [0.172605, 44.275979, 0.0], [-5.0, 44.275979, 0.0]]}, {"shapeName": "R_upLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 43.641125, -5.07883], [-5.0, 43.694961, -5.08556], [-5.054255, 43.641125, -5.07883], [-5.0, 43.587289, -5.072101], [-4.945745, 43.641125, -5.07883], [-5.0, 43.634396, -5.132662], [-5.054255, 43.641125, -5.07883], [-5.0, 43.647855, -5.024994], [-5.0, 43.694961, -5.08556], [-5.0, 43.634396, -5.132662], [-5.0, 43.587289, -5.072101], [-5.0, 43.647855, -5.024994], [-4.945745, 43.641125, -5.07883], [-5.0, 43.634396, -5.132662], [-5.0, 44.275979, 0.0]]}]},
			"R_elbow_shaper_05_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_05_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-54.15, 93.850166, -0.25], [-54.223426, 93.86539, -0.228404], [-54.285673, 93.908746, -0.210096], [-54.327268, 93.97363, -0.197862], [-54.341873, 94.050166, -0.193567], [-54.327268, 94.126702, -0.197862], [-54.285673, 94.191586, -0.210096], [-54.223426, 94.234942, -0.228404], [-54.15, 94.250166, -0.25], [-54.076574, 94.234942, -0.271596], [-54.014327, 94.191586, -0.289904], [-53.972732, 94.126702, -0.302138], [-53.958127, 94.050166, -0.306433], [-53.972732, 93.97363, -0.302138], [-54.014327, 93.908746, -0.289904], [-54.076574, 93.86539, -0.271596], [-54.15, 93.850166, -0.25], [-54.15, 91.850166, -0.25]]}]},
			"L_elbow_shaper_05_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_05_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[54.15, 93.600166, -0.25], [54.214248, 93.613487, -0.231104], [54.268714, 93.651424, -0.215084], [54.305109, 93.708197, -0.20438], [54.317889, 93.775166, -0.200621], [54.305109, 93.842135, -0.20438], [54.268714, 93.898909, -0.215084], [54.214248, 93.936845, -0.231104], [54.15, 93.950166, -0.25], [54.085752, 93.936845, -0.268896], [54.031286, 93.898909, -0.284916], [53.994891, 93.842135, -0.29562], [53.982111, 93.775166, -0.299379], [53.994891, 93.708197, -0.29562], [54.031286, 93.651424, -0.284916], [54.085752, 93.613487, -0.268896], [54.15, 93.600166, -0.25], [54.15, 91.850166, -0.25]]}]},
			"L_ankleOffset_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ankleOffset_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.118355, 2.775979, -0.054255], [10.118355, 2.830234, 0.0], [10.118355, 2.775979, 0.054255], [10.118355, 2.721724, 0.0], [10.118355, 2.775979, -0.054255], [10.172605, 2.775979, 0.0], [10.118355, 2.775979, 0.054255], [10.0641, 2.775979, 0.0], [10.118355, 2.830234, 0.0], [10.172605, 2.775979, 0.0], [10.118355, 2.721724, 0.0], [10.0641, 2.775979, 0.0], [10.118355, 2.775979, -0.054255], [10.172605, 2.775979, 0.0], [5.0, 2.775979, 0.0]]}, {"shapeName": "L_ankleOffset_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[5.0, 7.894334, -0.054255], [4.945745, 7.894334, -0.0], [5.0, 7.894334, 0.054255], [5.054255, 7.894334, -0.0], [5.0, 7.894334, -0.054255], [5.0, 7.948584, -0.0], [5.0, 7.894334, 0.054255], [5.0, 7.840079, -0.0], [4.945745, 7.894334, -0.0], [5.0, 7.948584, -0.0], [5.054255, 7.894334, -0.0], [5.0, 7.840079, -0.0], [5.0, 7.894334, -0.054255], [5.0, 7.948584, -0.0], [5.0, 2.775979, 0.0]]}, {"shapeName": "L_ankleOffset_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[5.0, 2.830234, 5.118355], [4.945745, 2.775979, 5.118355], [5.0, 2.721724, 5.118355], [5.054255, 2.775979, 5.118355], [5.0, 2.830234, 5.118355], [5.0, 2.775979, 5.172605], [5.0, 2.721724, 5.118355], [5.0, 2.775979, 5.0641], [4.945745, 2.775979, 5.118355], [5.0, 2.775979, 5.172605], [5.054255, 2.775979, 5.118355], [5.0, 2.775979, 5.0641], [5.0, 2.830234, 5.118355], [5.0, 2.775979, 5.172605], [5.0, 2.775979, 0.0]]}]},
			"C_spineShaper_3_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_spineShaper_3_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 69.468521, -0.054255], [-0.054255, 69.468521, 0.0], [0.0, 69.468521, 0.054255], [0.054255, 69.468521, 0.0], [0.0, 69.468521, -0.054255], [0.0, 69.522771, 0.0], [0.0, 69.468521, 0.054255], [0.0, 69.414266, 0.0], [-0.054255, 69.468521, 0.0], [0.0, 69.522771, 0.0], [0.054255, 69.468521, 0.0], [0.0, 69.414266, 0.0], [0.0, 69.468521, -0.054255], [0.0, 69.522771, 0.0], [0.0, 64.350166, 0.0]]}, {"shapeName": "C_spineShaper_3_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 64.350166, -0.054255], [-5.118355, 64.295911, 0.0], [-5.118355, 64.350166, 0.054255], [-5.118355, 64.404421, 0.0], [-5.118355, 64.350166, -0.054255], [-5.172605, 64.350166, 0.0], [-5.118355, 64.350166, 0.054255], [-5.0641, 64.350166, 0.0], [-5.118355, 64.295911, 0.0], [-5.172605, 64.350166, 0.0], [-5.118355, 64.404421, 0.0], [-5.0641, 64.350166, 0.0], [-5.118355, 64.350166, -0.054255], [-5.172605, 64.350166, 0.0], [0.0, 64.350166, 0.0]]}, {"shapeName": "C_spineShaper_3_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 64.350166, 5.118355], [0.0, 64.295911, 5.118355], [0.054255, 64.350166, 5.118355], [0.0, 64.404421, 5.118355], [-0.054255, 64.350166, 5.118355], [0.0, 64.350166, 5.172605], [0.054255, 64.350166, 5.118355], [0.0, 64.350166, 5.0641], [0.0, 64.295911, 5.118355], [0.0, 64.350166, 5.172605], [0.0, 64.404421, 5.118355], [0.0, 64.350166, 5.0641], [-0.054255, 64.350166, 5.118355], [0.0, 64.350166, 5.172605], [0.0, 64.350166, 0.0]]}]},
			"R_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.323456, 92.526661, -1.304255], [-66.316286, 92.58044, -1.25], [-66.323456, 92.526661, -1.195745], [-66.330627, 92.472882, -1.25], [-66.323456, 92.526661, -1.304255], [-66.37723, 92.533831, -1.25], [-66.323456, 92.526661, -1.195745], [-66.269677, 92.519491, -1.25], [-66.316286, 92.58044, -1.25], [-66.37723, 92.533831, -1.25], [-66.330627, 92.472882, -1.25], [-66.269677, 92.519491, -1.25], [-66.323456, 92.526661, -1.304255], [-66.37723, 92.533831, -1.25], [-61.25, 91.8502, -1.25]]}, {"shapeName": "R_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-60.573539, 96.923657, -1.304255], [-60.51976, 96.916486, -1.25], [-60.573539, 96.923657, -1.195745], [-60.627318, 96.930827, -1.25], [-60.573539, 96.923657, -1.304255], [-60.566369, 96.977431, -1.25], [-60.573539, 96.923657, -1.195745], [-60.58071, 96.869878, -1.25], [-60.51976, 96.916486, -1.25], [-60.566369, 96.977431, -1.25], [-60.627318, 96.930827, -1.25], [-60.58071, 96.869878, -1.25], [-60.573539, 96.923657, -1.304255], [-60.566369, 96.977431, -1.25], [-61.25, 91.8502, -1.25]]}, {"shapeName": "R_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.242829, 91.903979, 3.868355], [-61.196221, 91.84303, 3.868355], [-61.257171, 91.796421, 3.868355], [-61.303779, 91.857371, 3.868355], [-61.242829, 91.903979, 3.868355], [-61.25, 91.8502, 3.922605], [-61.257171, 91.796421, 3.868355], [-61.25, 91.8502, 3.8141], [-61.196221, 91.84303, 3.868355], [-61.25, 91.8502, 3.922605], [-61.303779, 91.857371, 3.868355], [-61.25, 91.8502, 3.8141], [-61.242829, 91.903979, 3.868355], [-61.25, 91.8502, 3.922605], [-61.25, 91.8502, -1.25]]}]},
			"R_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.754417, 91.642557, 6.292096], [-68.72459, 91.622398, 6.359854], [-68.72729, 91.548585, 6.339082], [-68.757117, 91.568743, 6.271324], [-68.754417, 91.642557, 6.292096], [-68.7908, 91.591547, 6.336378], [-68.72729, 91.548585, 6.339082], [-68.690902, 91.599595, 6.294798], [-68.72459, 91.622398, 6.359854], [-68.7908, 91.591547, 6.336378], [-68.757117, 91.568743, 6.271324], [-68.690902, 91.599595, 6.294798], [-68.754417, 91.642557, 6.292096], [-68.7908, 91.591547, 6.336378], [-64.0285, 91.9752, 4.35417]]}, {"shapeName": "R_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-62.507809, 94.55305, 8.506602], [-62.444294, 94.510088, 8.509303], [-62.480682, 94.459078, 8.553588], [-62.544197, 94.50204, 8.550886], [-62.507809, 94.55305, 8.506602], [-62.477984, 94.532889, 8.574356], [-62.480682, 94.459078, 8.553588], [-62.510509, 94.479237, 8.48583], [-62.444294, 94.510088, 8.509303], [-62.477984, 94.532889, 8.574356], [-62.544197, 94.50204, 8.550886], [-62.510509, 94.479237, 8.48583], [-62.507809, 94.55305, 8.506602], [-62.477984, 94.532889, 8.574356], [-64.0285, 91.9752, 4.35417]]}, {"shapeName": "R_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-62.732648, 87.569402, 6.614748], [-62.69896, 87.546599, 6.549691], [-62.765175, 87.515747, 6.526217], [-62.798863, 87.538551, 6.591274], [-62.732648, 87.569402, 6.614748], [-62.735349, 87.495593, 6.593973], [-62.765175, 87.515747, 6.526217], [-62.762475, 87.589561, 6.546989], [-62.69896, 87.546599, 6.549691], [-62.735349, 87.495593, 6.593973], [-62.798863, 87.538551, 6.591274], [-62.762475, 87.589561, 6.546989], [-62.732648, 87.569402, 6.614748], [-62.735349, 87.495593, 6.593973], [-64.0285, 91.9752, 4.35417]]}]},
			"R_scapulaCtrl_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_scapulaCtrl_CTLShape", "degree": 1, "form": 0, "points": [[-11.5, 91.850166, -12.5], [-14.5, 91.850166, -12.5], [-14.5, 91.850166, -15.5], [-11.5, 91.850166, -15.5], [-11.5, 91.850166, -12.5]]}]},
			"C_head_FK_CTL": {"color": 4, "shapes": [{"shapeName": "C_head_FK_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 101.850166, 0.0], [-5.03806, 102.041506, 0.0], [-5.14645, 102.203716, 0.0], [-5.30866, 102.312106, 0.0], [-5.5, 102.350166, 0.0], [-5.69134, 102.312106, 0.0], [-5.85355, 102.203716, 0.0], [-5.96194, 102.041506, 0.0], [-6.0, 101.850166, 0.0], [-5.96194, 101.658826, 0.0], [-5.85355, 101.496616, 0.0], [-5.69134, 101.388226, 0.0], [-5.5, 101.350166, 0.0], [-5.30866, 101.388226, 0.0], [-5.14645, 101.496616, 0.0], [-5.03806, 101.658826, 0.0], [-5.0, 101.850166, 0.0], [0.0, 101.850166, 0.0]]}]},
			"L_bendyLeg_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_bendyLeg_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 29.203878, 1.93869], [4.945745, 29.197149, 1.884854], [5.0, 29.190419, 1.831018], [5.054255, 29.197149, 1.884854], [5.0, 29.203878, 1.93869], [5.0, 29.143317, 1.891583], [5.0, 29.190419, 1.831018], [5.0, 29.250985, 1.878124], [4.945745, 29.197149, 1.884854], [5.0, 29.143317, 1.891583], [5.054255, 29.197149, 1.884854], [5.0, 29.250985, 1.878124], [5.0, 29.203878, 1.93869], [5.0, 29.143317, 1.891583], [5.0, 34.275979, 1.25]]}, {"shapeName": "L_bendyLeg_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 34.282708, 1.303836], [-0.118355, 34.329815, 1.24327], [-0.118355, 34.269249, 1.196164], [-0.118355, 34.222143, 1.25673], [-0.118355, 34.282708, 1.303836], [-0.172605, 34.275979, 1.25], [-0.118355, 34.269249, 1.196164], [-0.0641, 34.275979, 1.25], [-0.118355, 34.329815, 1.24327], [-0.172605, 34.275979, 1.25], [-0.118355, 34.222143, 1.25673], [-0.0641, 34.275979, 1.25], [-0.118355, 34.282708, 1.303836], [-0.172605, 34.275979, 1.25], [5.0, 34.275979, 1.25]]}, {"shapeName": "L_bendyLeg_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 33.641125, -3.82883], [5.0, 33.694961, -3.83556], [5.054255, 33.641125, -3.82883], [5.0, 33.587289, -3.822101], [4.945745, 33.641125, -3.82883], [5.0, 33.634396, -3.882662], [5.054255, 33.641125, -3.82883], [5.0, 33.647855, -3.774994], [5.0, 33.694961, -3.83556], [5.0, 33.634396, -3.882662], [5.0, 33.587289, -3.822101], [5.0, 33.647855, -3.774994], [4.945745, 33.641125, -3.82883], [5.0, 33.634396, -3.882662], [5.0, 34.275979, 1.25]]}]},
			"R_scapulaCtrl_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_scapulaCtrl_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-14.023671, 91.850166, -14.010851], [-14.023671, 91.861017, -14.0], [-14.023671, 91.850166, -13.989149], [-14.023671, 91.839315, -14.0], [-14.023671, 91.850166, -14.010851], [-14.034521, 91.850166, -14.0], [-14.023671, 91.850166, -13.989149], [-14.01282, 91.850166, -14.0], [-14.023671, 91.861017, -14.0], [-14.034521, 91.850166, -14.0], [-14.023671, 91.839315, -14.0], [-14.01282, 91.850166, -14.0], [-14.023671, 91.850166, -14.010851], [-14.034521, 91.850166, -14.0], [-13.0, 91.850166, -14.0]]}, {"shapeName": "R_scapulaCtrl_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-13.0, 92.873837, -14.010851], [-12.989149, 92.873837, -14.0], [-13.0, 92.873837, -13.989149], [-13.010851, 92.873837, -14.0], [-13.0, 92.873837, -14.010851], [-13.0, 92.884687, -14.0], [-13.0, 92.873837, -13.989149], [-13.0, 92.862986, -14.0], [-12.989149, 92.873837, -14.0], [-13.0, 92.884687, -14.0], [-13.010851, 92.873837, -14.0], [-13.0, 92.862986, -14.0], [-13.0, 92.873837, -14.010851], [-13.0, 92.884687, -14.0], [-13.0, 91.850166, -14.0]]}, {"shapeName": "R_scapulaCtrl_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-13.0, 91.861017, -12.976329], [-12.989149, 91.850166, -12.976329], [-13.0, 91.839315, -12.976329], [-13.010851, 91.850166, -12.976329], [-13.0, 91.861017, -12.976329], [-13.0, 91.850166, -12.965479], [-13.0, 91.839315, -12.976329], [-13.0, 91.850166, -12.98718], [-12.989149, 91.850166, -12.976329], [-13.0, 91.850166, -12.965479], [-13.010851, 91.850166, -12.976329], [-13.0, 91.850166, -12.98718], [-13.0, 91.861017, -12.976329], [-13.0, 91.850166, -12.965479], [-13.0, 91.850166, -14.0]]}]},
			"R_bendyLeg_C_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.249999, 13.266102, 3.484942], [-3.799999, 13.266102, 3.484942], [-5.0, 13.136164, 4.602412], [-6.200001, 13.266102, 3.484942], [-5.750001, 13.266102, 3.484942], [-5.750001, 13.439353, 1.994982], [-7.25, 13.439353, 1.994982], [-7.25, 13.387378, 2.44197], [-8.375, 13.525979, 1.25], [-7.25, 13.66458, 0.05803], [-7.25, 13.612605, 0.505018], [-5.750001, 13.612605, 0.505018], [-5.750001, 13.785856, -0.984942], [-6.200001, 13.785856, -0.984942], [-5.0, 13.915794, -2.102412], [-3.799999, 13.785856, -0.984942], [-4.249999, 13.785856, -0.984942], [-4.249999, 13.612605, 0.505018], [-2.75, 13.612605, 0.505018], [-2.75, 13.66458, 0.05803], [-1.625, 13.525979, 1.25], [-2.75, 13.387378, 2.44197], [-2.75, 13.439353, 1.994982], [-4.249999, 13.439353, 1.994982], [-4.249999, 13.266102, 3.484942]]}]},
			"L_toeTip_CTL": {"color": 20, "shapes": [{"shapeName": "L_toeTip_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 0.275979, 11.5], [5.0, -0.224021, 11.0], [5.5, 0.275979, 11.0], [5.0, 0.275979, 11.5], [4.5, 0.275979, 11.0], [5.0, -0.224021, 11.0], [5.0, 0.275979, 10.5], [4.5, 0.275979, 11.0], [5.0, 0.775979, 11.0], [5.0, 0.275979, 11.5], [5.5, 0.275979, 11.0], [5.0, 0.275979, 10.5], [5.0, 0.775979, 11.0], [5.5, 0.275979, 11.0]]}]},
			"R_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-70.102054, 91.842036, -1.304255], [-70.106381, 91.896118, -1.25], [-70.102054, 91.842036, -1.195745], [-70.097728, 91.787954, -1.25], [-70.102054, 91.842036, -1.304255], [-70.156132, 91.83771, -1.25], [-70.102054, 91.842036, -1.195745], [-70.047972, 91.846363, -1.25], [-70.106381, 91.896118, -1.25], [-70.156132, 91.83771, -1.25], [-70.097728, 91.787954, -1.25], [-70.047972, 91.846363, -1.25], [-70.102054, 91.842036, -1.304255], [-70.156132, 91.83771, -1.25], [-65.0, 92.2502, -1.25]]}, {"shapeName": "R_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.408164, 97.352255, -1.304255], [-65.354082, 97.356581, -1.25], [-65.408164, 97.352255, -1.195745], [-65.462247, 97.347928, -1.25], [-65.408164, 97.352255, -1.304255], [-65.412491, 97.406332, -1.25], [-65.408164, 97.352255, -1.195745], [-65.403838, 97.298173, -1.25], [-65.354082, 97.356581, -1.25], [-65.412491, 97.406332, -1.25], [-65.462247, 97.347928, -1.25], [-65.403838, 97.298173, -1.25], [-65.408164, 97.352255, -1.304255], [-65.412491, 97.406332, -1.25], [-65.0, 92.2502, -1.25]]}, {"shapeName": "R_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-65.004327, 92.304283, 3.868355], [-64.945918, 92.254527, 3.868355], [-64.995673, 92.196118, 3.868355], [-65.054082, 92.245874, 3.868355], [-65.004327, 92.304283, 3.868355], [-65.0, 92.2502, 3.922605], [-64.995673, 92.196118, 3.868355], [-65.0, 92.2502, 3.8141], [-64.945918, 92.254527, 3.868355], [-65.0, 92.2502, 3.922605], [-65.054082, 92.245874, 3.868355], [-65.0, 92.2502, 3.8141], [-65.004327, 92.304283, 3.868355], [-65.0, 92.2502, 3.922605], [-65.0, 92.2502, -1.25]]}]},
			"L_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.227054, 92.508331, -1.304255], [68.222728, 92.562413, -1.25], [68.227054, 92.508331, -1.195745], [68.231381, 92.454248, -1.25], [68.227054, 92.508331, -1.304255], [68.281132, 92.512657, -1.25], [68.227054, 92.508331, -1.195745], [68.172972, 92.504004, -1.25], [68.222728, 92.562413, -1.25], [68.281132, 92.512657, -1.25], [68.231381, 92.454248, -1.25], [68.172972, 92.504004, -1.25], [68.227054, 92.508331, -1.304255], [68.281132, 92.512657, -1.25], [63.125, 92.100166, -1.25]]}, {"shapeName": "L_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[62.716836, 97.202221, -1.304255], [62.662753, 97.197894, -1.25], [62.716836, 97.202221, -1.195745], [62.770918, 97.206547, -1.25], [62.716836, 97.202221, -1.304255], [62.712509, 97.256298, -1.25], [62.716836, 97.202221, -1.195745], [62.721162, 97.148139, -1.25], [62.662753, 97.197894, -1.25], [62.712509, 97.256298, -1.25], [62.770918, 97.206547, -1.25], [62.721162, 97.148139, -1.25], [62.716836, 97.202221, -1.304255], [62.712509, 97.256298, -1.25], [63.125, 92.100166, -1.25]]}, {"shapeName": "L_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[63.120673, 92.154249, 3.868355], [63.070918, 92.09584, 3.868355], [63.129327, 92.046084, 3.868355], [63.179082, 92.104493, 3.868355], [63.120673, 92.154249, 3.868355], [63.125, 92.100166, 3.922605], [63.129327, 92.046084, 3.868355], [63.125, 92.100166, 3.8141], [63.070918, 92.09584, 3.868355], [63.125, 92.100166, 3.922605], [63.179082, 92.104493, 3.868355], [63.125, 92.100166, 3.8141], [63.120673, 92.154249, 3.868355], [63.125, 92.100166, 3.922605], [63.125, 92.100166, -1.25]]}]},
			"R_bendyLeg_A_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.499999, 34.462031, 2.738417], [-4.199999, 34.462031, 2.738417], [-5.0, 34.555057, 3.482625], [-5.800001, 34.462031, 2.738417], [-5.500001, 34.462031, 2.738417], [-5.500001, 34.337996, 1.74614], [-6.5, 34.337996, 1.74614], [-6.5, 34.375207, 2.043823], [-7.25, 34.275979, 1.25], [-6.5, 34.176751, 0.456177], [-6.5, 34.213961, 0.75386], [-5.500001, 34.213961, 0.75386], [-5.500001, 34.089927, -0.238417], [-5.800001, 34.089927, -0.238417], [-5.0, 33.996901, -0.982625], [-4.199999, 34.089927, -0.238417], [-4.499999, 34.089927, -0.238417], [-4.499999, 34.213961, 0.75386], [-3.5, 34.213961, 0.75386], [-3.5, 34.176751, 0.456177], [-2.75, 34.275979, 1.25], [-3.5, 34.375207, 2.043823], [-3.5, 34.337996, 1.74614], [-4.499999, 34.337996, 1.74614], [-4.499999, 34.462031, 2.738417]]}]},
			"R_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-71.948456, 91.423739, -0.054255], [-71.955627, 91.477519, -0.0], [-71.948456, 91.423739, 0.054255], [-71.941286, 91.36996, -0.0], [-71.948456, 91.423739, -0.054255], [-72.00223, 91.41657, -0.0], [-71.948456, 91.423739, 0.054255], [-71.894677, 91.43091, -0.0], [-71.955627, 91.477519, -0.0], [-72.00223, 91.41657, -0.0], [-71.941286, 91.36996, -0.0], [-71.894677, 91.43091, -0.0], [-71.948456, 91.423739, -0.054255], [-72.00223, 91.41657, -0.0], [-66.875, 92.1002, -0.0]]}, {"shapeName": "R_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.551461, 97.173657, -0.054255], [-67.497682, 97.180827, 0.0], [-67.551461, 97.173657, 0.054255], [-67.60524, 97.166486, 0.0], [-67.551461, 97.173657, -0.054255], [-67.558631, 97.227431, 0.0], [-67.551461, 97.173657, 0.054255], [-67.54429, 97.119878, 0.0], [-67.497682, 97.180827, 0.0], [-67.558631, 97.227431, 0.0], [-67.60524, 97.166486, 0.0], [-67.54429, 97.119878, 0.0], [-67.551461, 97.173657, -0.054255], [-67.558631, 97.227431, 0.0], [-66.875, 92.1002, -0.0]]}, {"shapeName": "R_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-66.882171, 92.153979, 5.118355], [-66.821221, 92.107371, 5.118355], [-66.867829, 92.046421, 5.118355], [-66.928779, 92.09303, 5.118355], [-66.882171, 92.153979, 5.118355], [-66.875, 92.1002, 5.172605], [-66.867829, 92.046421, 5.118355], [-66.875, 92.1002, 5.0641], [-66.821221, 92.107371, 5.118355], [-66.875, 92.1002, 5.172605], [-66.928779, 92.09303, 5.118355], [-66.875, 92.1002, 5.0641], [-66.882171, 92.153979, 5.118355], [-66.875, 92.1002, 5.172605], [-66.875, 92.1002, -0.0]]}]},
			"L_loLeg_shaper_04_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_shaper_04_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 4.852279, 0.296051], [4.945745, 4.858546, 0.242159], [5.0, 4.864812, 0.188267], [5.054255, 4.858546, 0.242159], [5.0, 4.852279, 0.296051], [5.0, 4.804659, 0.235893], [5.0, 4.864812, 0.188267], [5.0, 4.912438, 0.248425], [4.945745, 4.858546, 0.242159], [5.0, 4.804659, 0.235893], [5.054255, 4.858546, 0.242159], [5.0, 4.912438, 0.248425], [5.0, 4.852279, 0.296051], [5.0, 4.804659, 0.235893], [5.0, 9.942646, 0.833333]]}, {"shapeName": "L_loLeg_shaper_04_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 9.936379, 0.887225], [-0.118355, 9.996538, 0.8396], [-0.118355, 9.948912, 0.779441], [-0.118355, 9.888754, 0.827067], [-0.118355, 9.936379, 0.887225], [-0.172605, 9.942646, 0.833333], [-0.118355, 9.948912, 0.779441], [-0.0641, 9.942646, 0.833333], [-0.118355, 9.996538, 0.8396], [-0.172605, 9.942646, 0.833333], [-0.118355, 9.888754, 0.827067], [-0.0641, 9.942646, 0.833333], [-0.118355, 9.936379, 0.887225], [-0.172605, 9.942646, 0.833333], [5.0, 9.942646, 0.833333]]}, {"shapeName": "L_loLeg_shaper_04_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 10.53382, -4.250766], [5.0, 10.587712, -4.2445], [5.054255, 10.53382, -4.250766], [5.0, 10.479928, -4.257033], [4.945745, 10.53382, -4.250766], [5.0, 10.540086, -4.304653], [5.054255, 10.53382, -4.250766], [5.0, 10.527554, -4.196875], [5.0, 10.587712, -4.2445], [5.0, 10.540086, -4.304653], [5.0, 10.479928, -4.257033], [5.0, 10.527554, -4.196875], [4.945745, 10.53382, -4.250766], [5.0, 10.540086, -4.304653], [5.0, 9.942646, 0.833333]]}]},
			"L_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[70.102054, 91.842002, -2.554255], [70.106381, 91.896084, -2.5], [70.102054, 91.842002, -2.445745], [70.097728, 91.78792, -2.5], [70.102054, 91.842002, -2.554255], [70.156132, 91.837676, -2.5], [70.102054, 91.842002, -2.445745], [70.047972, 91.846329, -2.5], [70.106381, 91.896084, -2.5], [70.156132, 91.837676, -2.5], [70.097728, 91.78792, -2.5], [70.047972, 91.846329, -2.5], [70.102054, 91.842002, -2.554255], [70.156132, 91.837676, -2.5], [65.0, 92.250166, -2.5]]}, {"shapeName": "L_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.408164, 97.352221, -2.554255], [65.354082, 97.356547, -2.5], [65.408164, 97.352221, -2.445745], [65.462247, 97.347894, -2.5], [65.408164, 97.352221, -2.554255], [65.412491, 97.406298, -2.5], [65.408164, 97.352221, -2.445745], [65.403838, 97.298139, -2.5], [65.354082, 97.356547, -2.5], [65.412491, 97.406298, -2.5], [65.462247, 97.347894, -2.5], [65.403838, 97.298139, -2.5], [65.408164, 97.352221, -2.554255], [65.412491, 97.406298, -2.5], [65.0, 92.250166, -2.5]]}, {"shapeName": "L_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.004327, 92.304249, 2.618355], [64.945918, 92.254493, 2.618355], [64.995673, 92.196084, 2.618355], [65.054082, 92.24584, 2.618355], [65.004327, 92.304249, 2.618355], [65.0, 92.250166, 2.672605], [64.995673, 92.196084, 2.618355], [65.0, 92.250166, 2.5641], [64.945918, 92.254493, 2.618355], [65.0, 92.250166, 2.672605], [65.054082, 92.24584, 2.618355], [65.0, 92.250166, 2.5641], [65.004327, 92.304249, 2.618355], [65.0, 92.250166, 2.672605], [65.0, 92.250166, -2.5]]}]},
			"R_handIk_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_handIk_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-55.0, 88.715718, -3.134448], [-55.0, 91.850166, -4.432776], [-55.0, 94.984614, -3.134448], [-55.0, 96.282942, -0.0], [-55.0, 94.984614, 3.134448], [-55.0, 91.850166, 4.432776], [-55.0, 88.715718, 3.134448], [-55.0, 87.41739, 0.0]]}]},
			"C_midSpine_CTL": {"color": 20, "shapes": [{"shapeName": "C_midSpine_CTLShape", "degree": 3, "form": 2, "points": [[7.052508, 64.350166, -5.87709], [0.0, 64.350166, -8.311455], [-7.052508, 64.350166, -5.87709], [-9.973746, 64.350166, 0.0], [-7.052508, 64.350166, 5.87709], [0.0, 64.350166, 8.311455], [7.052508, 64.350166, 5.87709], [9.973746, 64.350166, 0.0]]}]},
			"R_upLeg_shaper_04_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upLeg_shaper_04_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 25.870545, 2.355357], [-4.945745, 25.863815, 2.30152], [-5.0, 25.857086, 2.247684], [-5.054255, 25.863815, 2.30152], [-5.0, 25.870545, 2.355357], [-5.0, 25.809984, 2.308249], [-5.0, 25.857086, 2.247684], [-5.0, 25.917651, 2.294791], [-4.945745, 25.863815, 2.30152], [-5.0, 25.809984, 2.308249], [-5.054255, 25.863815, 2.30152], [-5.0, 25.917651, 2.294791], [-5.0, 25.870545, 2.355357], [-5.0, 25.809984, 2.308249], [-5.0, 30.942646, 1.666667]]}, {"shapeName": "R_upLeg_shaper_04_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 30.949375, 1.720503], [0.118355, 30.996482, 1.659937], [0.118355, 30.935916, 1.612831], [0.118355, 30.88881, 1.673396], [0.118355, 30.949375, 1.720503], [0.172605, 30.942646, 1.666667], [0.118355, 30.935916, 1.612831], [0.0641, 30.942646, 1.666667], [0.118355, 30.996482, 1.659937], [0.172605, 30.942646, 1.666667], [0.118355, 30.88881, 1.673396], [0.0641, 30.942646, 1.666667], [0.118355, 30.949375, 1.720503], [0.172605, 30.942646, 1.666667], [-5.0, 30.942646, 1.666667]]}, {"shapeName": "R_upLeg_shaper_04_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 30.307792, -3.412164], [-5.0, 30.361628, -3.418893], [-5.054255, 30.307792, -3.412164], [-5.0, 30.253956, -3.405434], [-4.945745, 30.307792, -3.412164], [-5.0, 30.301063, -3.465995], [-5.054255, 30.307792, -3.412164], [-5.0, 30.314521, -3.358328], [-5.0, 30.361628, -3.418893], [-5.0, 30.301063, -3.465995], [-5.0, 30.253956, -3.405434], [-5.0, 30.314521, -3.358328], [-4.945745, 30.307792, -3.412164], [-5.0, 30.301063, -3.465995], [-5.0, 30.942646, 1.666667]]}]},
			"R_bendyLeg_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_bendyLeg_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 29.203878, 1.93869], [-4.945745, 29.197149, 1.884854], [-5.0, 29.190419, 1.831018], [-5.054255, 29.197149, 1.884854], [-5.0, 29.203878, 1.93869], [-5.0, 29.143317, 1.891583], [-5.0, 29.190419, 1.831018], [-5.0, 29.250985, 1.878124], [-4.945745, 29.197149, 1.884854], [-5.0, 29.143317, 1.891583], [-5.054255, 29.197149, 1.884854], [-5.0, 29.250985, 1.878124], [-5.0, 29.203878, 1.93869], [-5.0, 29.143317, 1.891583], [-5.0, 34.275979, 1.25]]}, {"shapeName": "R_bendyLeg_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 34.282708, 1.303836], [0.118355, 34.329815, 1.24327], [0.118355, 34.269249, 1.196164], [0.118355, 34.222143, 1.25673], [0.118355, 34.282708, 1.303836], [0.172605, 34.275979, 1.25], [0.118355, 34.269249, 1.196164], [0.0641, 34.275979, 1.25], [0.118355, 34.329815, 1.24327], [0.172605, 34.275979, 1.25], [0.118355, 34.222143, 1.25673], [0.0641, 34.275979, 1.25], [0.118355, 34.282708, 1.303836], [0.172605, 34.275979, 1.25], [-5.0, 34.275979, 1.25]]}, {"shapeName": "R_bendyLeg_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 33.641125, -3.82883], [-5.0, 33.694961, -3.83556], [-5.054255, 33.641125, -3.82883], [-5.0, 33.587289, -3.822101], [-4.945745, 33.641125, -3.82883], [-5.0, 33.634396, -3.882662], [-5.054255, 33.641125, -3.82883], [-5.0, 33.647855, -3.774994], [-5.0, 33.694961, -3.83556], [-5.0, 33.634396, -3.882662], [-5.0, 33.587289, -3.822101], [-5.0, 33.647855, -3.774994], [-4.945745, 33.641125, -3.82883], [-5.0, 33.634396, -3.882662], [-5.0, 34.275979, 1.25]]}]},
			"R_upLeg_shaper_01_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_01_CTLShape", "degree": 1, "form": 0, "points": [[-17.5, 40.942646, 0.416667], [-17.59515, 40.373058, 0.487865], [-17.866125, 39.890186, 0.548224], [-18.27165, 39.567527, 0.588556], [-18.75, 39.454229, 0.602719], [-19.22835, 39.567527, 0.588556], [-19.633875, 39.890186, 0.548224], [-19.90485, 40.373058, 0.487865], [-20.0, 40.942646, 0.416667], [-19.90485, 41.512233, 0.345468], [-19.633875, 41.995105, 0.285109], [-19.22835, 42.317764, 0.244777], [-18.75, 42.431062, 0.230615], [-18.27165, 42.317764, 0.244777], [-17.866125, 41.995105, 0.285109], [-17.59515, 41.512233, 0.345468], [-17.5, 40.942646, 0.416667], [-5.0, 40.942646, 0.416667]]}]},
			"C_hip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_hip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 51.850166, -0.054255], [5.118355, 51.904421, 0.0], [5.118355, 51.850166, 0.054255], [5.118355, 51.795911, 0.0], [5.118355, 51.850166, -0.054255], [5.172605, 51.850166, 0.0], [5.118355, 51.850166, 0.054255], [5.0641, 51.850166, 0.0], [5.118355, 51.904421, 0.0], [5.172605, 51.850166, 0.0], [5.118355, 51.795911, 0.0], [5.0641, 51.850166, 0.0], [5.118355, 51.850166, -0.054255], [5.172605, 51.850166, 0.0], [0.0, 51.850166, 0.0]]}, {"shapeName": "C_hip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 56.968521, -0.054255], [-0.054255, 56.968521, 0.0], [0.0, 56.968521, 0.054255], [0.054255, 56.968521, 0.0], [0.0, 56.968521, -0.054255], [0.0, 57.022771, 0.0], [0.0, 56.968521, 0.054255], [0.0, 56.914266, 0.0], [-0.054255, 56.968521, 0.0], [0.0, 57.022771, 0.0], [0.054255, 56.968521, 0.0], [0.0, 56.914266, 0.0], [0.0, 56.968521, -0.054255], [0.0, 57.022771, 0.0], [0.0, 51.850166, 0.0]]}, {"shapeName": "C_hip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 51.904421, 5.118355], [-0.054255, 51.850166, 5.118355], [0.0, 51.795911, 5.118355], [0.054255, 51.850166, 5.118355], [0.0, 51.904421, 5.118355], [0.0, 51.850166, 5.172605], [0.0, 51.795911, 5.118355], [0.0, 51.850166, 5.0641], [-0.054255, 51.850166, 5.118355], [0.0, 51.850166, 5.172605], [0.054255, 51.850166, 5.118355], [0.0, 51.850166, 5.0641], [0.0, 51.904421, 5.118355], [0.0, 51.850166, 5.172605], [0.0, 51.850166, 0.0]]}]},
			"C_spineShaper_1_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_spineShaper_1_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 56.988521, -0.054255], [-0.054255, 56.988521, 0.0], [0.0, 56.988521, 0.054255], [0.054255, 56.988521, 0.0], [0.0, 56.988521, -0.054255], [0.0, 57.042771, 0.0], [0.0, 56.988521, 0.054255], [0.0, 56.934266, 0.0], [-0.054255, 56.988521, 0.0], [0.0, 57.042771, 0.0], [0.054255, 56.988521, 0.0], [0.0, 56.934266, 0.0], [0.0, 56.988521, -0.054255], [0.0, 57.042771, 0.0], [0.0, 51.870166, 0.0]]}, {"shapeName": "C_spineShaper_1_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 51.870166, -0.054255], [-5.118355, 51.815911, 0.0], [-5.118355, 51.870166, 0.054255], [-5.118355, 51.924421, 0.0], [-5.118355, 51.870166, -0.054255], [-5.172605, 51.870166, 0.0], [-5.118355, 51.870166, 0.054255], [-5.0641, 51.870166, 0.0], [-5.118355, 51.815911, 0.0], [-5.172605, 51.870166, 0.0], [-5.118355, 51.924421, 0.0], [-5.0641, 51.870166, 0.0], [-5.118355, 51.870166, -0.054255], [-5.172605, 51.870166, 0.0], [0.0, 51.870166, 0.0]]}, {"shapeName": "C_spineShaper_1_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 51.870166, 5.118355], [0.0, 51.815911, 5.118355], [0.054255, 51.870166, 5.118355], [0.0, 51.924421, 5.118355], [-0.054255, 51.870166, 5.118355], [0.0, 51.870166, 5.172605], [0.054255, 51.870166, 5.118355], [0.0, 51.870166, 5.0641], [0.0, 51.815911, 5.118355], [0.0, 51.870166, 5.172605], [0.0, 51.924421, 5.118355], [0.0, 51.870166, 5.0641], [-0.054255, 51.870166, 5.118355], [0.0, 51.870166, 5.172605], [0.0, 51.870166, 0.0]]}]},
			"R_clavicle_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_clavicle_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.214818, 91.850166, -0.342266], [-5.218337, 91.861017, -0.332001], [-5.221857, 91.850166, -0.321737], [-5.218337, 91.839315, -0.332001], [-5.214818, 91.850166, -0.342266], [-5.228601, 91.850166, -0.33552], [-5.221857, 91.850166, -0.321737], [-5.208073, 91.850166, -0.328482], [-5.218337, 91.861017, -0.332001], [-5.228601, 91.850166, -0.33552], [-5.218337, 91.839315, -0.332001], [-5.208073, 91.850166, -0.328482], [-5.214818, 91.850166, -0.342266], [-5.228601, 91.850166, -0.33552], [-4.25, 91.850166, -0.0]]}, {"shapeName": "R_clavicle_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-4.246481, 92.873837, -0.010264], [-4.239736, 92.873837, 0.003519], [-4.253519, 92.873837, 0.010264], [-4.260264, 92.873837, -0.003519], [-4.246481, 92.873837, -0.010264], [-4.25, 92.884687, 0.0], [-4.253519, 92.873837, 0.010264], [-4.25, 92.862986, 0.0], [-4.239736, 92.873837, 0.003519], [-4.25, 92.884687, 0.0], [-4.260264, 92.873837, -0.003519], [-4.25, 92.862986, 0.0], [-4.246481, 92.873837, -0.010264], [-4.25, 92.884687, 0.0], [-4.25, 91.850166, -0.0]]}, {"shapeName": "R_clavicle_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.582001, 91.861017, 0.968337], [-4.571737, 91.850166, 0.971857], [-4.582001, 91.839315, 0.968337], [-4.592266, 91.850166, 0.964818], [-4.582001, 91.861017, 0.968337], [-4.58552, 91.850166, 0.978601], [-4.582001, 91.839315, 0.968337], [-4.578482, 91.850166, 0.958073], [-4.571737, 91.850166, 0.971857], [-4.58552, 91.850166, 0.978601], [-4.592266, 91.850166, 0.964818], [-4.578482, 91.850166, 0.958073], [-4.582001, 91.861017, 0.968337], [-4.58552, 91.850166, 0.978601], [-4.25, 91.850166, -0.0]]}]},
			"R_loLeg_shaper_04_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_04_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-15.0, 9.942646, 0.833333], [-15.07612, 9.486503, 0.780293], [-15.2929, 9.099805, 0.735329], [-15.61732, 8.841409, 0.705283], [-16.0, 8.750677, 0.694732], [-16.38268, 8.841409, 0.705283], [-16.7071, 9.099805, 0.735329], [-16.92388, 9.486503, 0.780293], [-17.0, 9.942646, 0.833333], [-16.92388, 10.398788, 0.886373], [-16.7071, 10.785487, 0.931338], [-16.38268, 11.043882, 0.961384], [-16.0, 11.134615, 0.971934], [-15.61732, 11.043882, 0.961384], [-15.2929, 10.785487, 0.931338], [-15.07612, 10.398788, 0.886373], [-15.0, 9.942646, 0.833333], [-5.0, 9.942646, 0.833333]]}]},
			"R_hand_CTL": {"color": 1, "shapes": [{"shapeName": "R_hand_CTLShape", "degree": 1, "form": 0, "points": [[-61.50484, 96.769691, -0.0], [-61.309959, 96.804341, 0.0], [-61.108885, 96.812251, 0.0], [-60.918309, 96.807841, 0.0], [-60.728715, 96.811936, -0.0], [-60.601524, 96.821561, 0.0], [-60.502054, 96.886731, -0.0], [-60.419105, 97.038421, -0.0], [-60.330205, 97.235506, -0.0], [-60.259189, 97.455446, -0.0], [-60.19234, 97.767191, -0.0], [-60.159124, 98.083101, 0.0], [-60.144284, 98.329011, -0.0], [-60.13984, 98.522386, 0.0], [-60.118595, 98.644886, 0.0], [-60.096125, 98.794931, 0.0], [-60.051359, 98.961146, 0.0], [-60.023255, 99.109721, -0.0], [-59.993294, 99.230086, -0.0], [-59.94818, 99.371801, 0.0], [-59.899949, 99.554816, 0.0], [-59.89904, 99.696426, 0.0], [-59.956685, 99.808461, -0.0], [-60.02532, 99.830371, 0.0], [-60.116039, 99.788861, 0.0], [-60.15034, 99.681131, 0.0], [-60.191114, 99.542181, -0.0], [-60.244979, 99.405751, 0.0], [-60.29923, 99.263511, 0.0], [-60.355719, 99.090996, 0.0], [-60.42089, 98.950926, 0.0], [-60.47878, 98.892056, 0.0], [-60.50566, 98.887436, 0.0], [-60.550354, 98.974516, 0.0], [-60.555219, 99.100166, 0.0], [-60.522705, 99.245206, -0.0], [-60.502054, 99.341981, -0.0], [-60.48718, 99.488561, -0.0], [-60.476329, 99.621071, 0.0], [-60.453474, 99.760161, -0.0], [-60.438285, 99.878251, 0.0], [-60.423269, 99.978701, 0.0], [-60.393974, 100.125946, -0.0], [-60.369335, 100.242601, -0.0], [-60.358869, 100.355686, 0.0], [-60.393135, 100.460056, -0.0], [-60.460124, 100.527676, -0.0], [-60.55802, 100.531176, -0.0], [-60.641669, 100.480461, 0.0], [-60.684055, 100.368496, -0.0], [-60.710794, 100.236546, -0.0], [-60.736869, 100.119611, 0.0], [-60.769315, 99.981921, 0.0], [-60.798609, 99.854206, 0.0], [-60.82045, 99.732336, -0.0], [-60.837179, 99.600666, 0.0], [-60.872074, 99.444496, -0.0], [-60.897869, 99.338236, -0.0], [-60.918974, 99.213391, 0.0], [-60.98341, 99.116056, -0.0], [-61.026879, 99.181996, -0.0], [-61.052709, 99.355281, -0.0], [-61.05845, 99.485586, 0.0], [-61.054355, 99.654356, 0.0], [-61.061565, 99.804576, -0.0], [-61.069859, 99.936526, 0.0], [-61.070839, 100.088811, -0.0], [-61.06328, 100.233256, 0.0], [-61.063665, 100.438356, -0.0], [-61.069229, 100.587806, 0.0], [-61.089495, 100.715101, 0.0], [-61.164254, 100.769141, 0.0], [-61.262605, 100.798086, 0.0], [-61.349685, 100.768686, -0.0], [-61.394835, 100.677126, -0.0], [-61.406594, 100.526276, -0.0], [-61.417515, 100.376791, 0.0], [-61.423535, 100.252716, -0.0], [-61.41272, 100.090456, 0.0], [-61.411074, 99.941531, 0.0], [-61.431689, 99.781861, -0.0], [-61.44478, 99.703531, 0.0], [-61.44128, 99.597761, 0.0], [-61.446635, 99.479391, 0.0], [-61.456154, 99.336031, -0.0], [-61.46459, 99.164776, 0.0], [-61.48538, 99.125471, 0.0], [-61.53613, 99.172861, 0.0], [-61.56028, 99.291791, -0.0], [-61.594265, 99.448451, -0.0], [-61.637104, 99.633251, 0.0], [-61.665909, 99.794041, -0.0], [-61.695765, 99.936386, -0.0], [-61.740739, 100.069106, 0.0], [-61.78918, 100.226711, 0.0], [-61.827329, 100.390231, -0.0], [-61.867404, 100.515951, -0.0], [-61.913184, 100.615036, 0.0], [-61.987665, 100.690566, 0.0], [-62.044399, 100.678281, -0.0], [-62.1445, 100.613321, -0.0], [-62.180689, 100.464081, -0.0], [-62.158045, 100.314526, 0.0], [-62.139879, 100.211941, -0.0], [-62.123919, 100.084121, -0.0], [-62.099595, 99.948391, -0.0], [-62.051609, 99.799956, -0.0], [-62.030645, 99.705491, 0.0], [-62.020669, 99.536406, 0.0], [-62.014755, 99.426751, -0.0], [-61.990884, 99.287381, 0.0], [-61.970059, 99.161556, -0.0], [-61.960085, 99.022221, -0.0], [-61.942864, 98.811766, -0.0], [-61.96166, 98.510731, -0.0], [-61.998059, 98.356101, -0.0], [-62.056125, 98.258031, -0.0], [-62.130184, 98.151841, -0.0], [-62.191015, 98.281306, -0.0], [-62.288314, 98.425926, -0.0], [-62.33903, 98.529421, 0.0], [-62.362479, 98.646951, 0.0], [-62.42009, 98.766021, -0.0], [-62.51424, 98.886526, -0.0], [-62.639784, 98.976686, -0.0], [-62.72858, 99.003636, 0.0], [-62.81447, 98.949351, 0.0], [-62.829695, 98.863811, -0.0], [-62.807645, 98.718911, -0.0], [-62.760954, 98.625671, 0.0], [-62.75448, 98.541181, -0.0], [-62.751329, 98.378746, 0.0], [-62.700195, 98.279311, -0.0], [-62.63772, 98.199161, -0.0], [-62.620255, 98.122266, -0.0], [-62.60685, 98.023426, -0.0], [-62.545915, 97.866486, -0.0], [-62.46797, 97.528246, 0.0], [-62.372875, 97.360561, 0.0], [-62.24929, 97.170861, -0.0], [-62.127209, 97.005661, -0.0], [-62.0311, 96.883791, 0.0], [-61.859355, 96.789011, -0.0], [-61.702134, 96.758806, -0.0], [-61.507604, 96.769446, 0.0]]}]},
			"R_upLeg_shaper_05_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_05_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-13.75, 27.609312, 2.083333], [-13.816605, 27.210601, 2.133172], [-14.006287, 26.872591, 2.175424], [-14.290155, 26.646729, 2.203656], [-14.625, 26.567421, 2.21357], [-14.959845, 26.646729, 2.203656], [-15.243712, 26.872591, 2.175424], [-15.433395, 27.210601, 2.133172], [-15.5, 27.609312, 2.083333], [-15.433395, 28.008023, 2.033494], [-15.243712, 28.346034, 1.991243], [-14.959845, 28.571895, 1.96301], [-14.625, 28.651204, 1.953097], [-14.290155, 28.571895, 1.96301], [-14.006287, 28.346034, 1.991243], [-13.816605, 28.008023, 2.033494], [-13.75, 27.609312, 2.083333], [-5.0, 27.609312, 2.083333]]}]},
			"R_elbow_shaper_03_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_03_CTLShape", "degree": 1, "form": 0, "points": [[-46.5, 94.350166, -2.5], [-46.591782, 94.369196, -2.473005], [-46.669592, 94.423391, -2.45012], [-46.721585, 94.504496, -2.434828], [-46.739841, 94.600166, -2.429458], [-46.721585, 94.695836, -2.434828], [-46.669592, 94.776941, -2.45012], [-46.591782, 94.831136, -2.473005], [-46.5, 94.850166, -2.5], [-46.408218, 94.831136, -2.526995], [-46.330408, 94.776941, -2.54988], [-46.278415, 94.695836, -2.565172], [-46.260159, 94.600166, -2.570542], [-46.278415, 94.504496, -2.565172], [-46.330408, 94.423391, -2.54988], [-46.408218, 94.369196, -2.526995], [-46.5, 94.350166, -2.5], [-46.5, 91.850166, -2.5]]}]},
			"R_upLeg_shaper_02_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_02_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-13.75, 37.609312, 0.833333], [-13.816605, 37.210601, 0.883172], [-14.006287, 36.872591, 0.925424], [-14.290155, 36.646729, 0.953656], [-14.625, 36.567421, 0.96357], [-14.959845, 36.646729, 0.953656], [-15.243712, 36.872591, 0.925424], [-15.433395, 37.210601, 0.883172], [-15.5, 37.609312, 0.833333], [-15.433395, 38.008023, 0.783494], [-15.243712, 38.346034, 0.741243], [-14.959845, 38.571895, 0.71301], [-14.625, 38.651204, 0.703097], [-14.290155, 38.571895, 0.71301], [-14.006287, 38.346034, 0.741243], [-13.816605, 38.008023, 0.783494], [-13.75, 37.609312, 0.833333], [-5.0, 37.609312, 0.833333]]}]},
			"L_toe_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_toe_FK_CTLShape", "degree": 3, "form": 2, "points": [[6.95903, 2.235009, 5.0], [5.0, 3.046464, 5.0], [3.04097, 2.235009, 5.0], [2.229515, 0.275979, 5.0], [3.04097, -1.683051, 5.0], [5.0, -2.494506, 5.0], [6.95903, -1.683051, 5.0], [7.770485, 0.275979, 5.0]]}]},
			"L_elbow_shaper_05_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_05_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[54.15, 94.100166, -0.25], [54.232604, 94.117293, -0.225705], [54.302633, 94.166069, -0.205108], [54.349426, 94.239063, -0.191345], [54.365857, 94.325166, -0.186513], [54.349426, 94.411269, -0.191345], [54.302633, 94.484264, -0.205108], [54.232604, 94.533039, -0.225705], [54.15, 94.550166, -0.25], [54.067396, 94.533039, -0.274295], [53.997367, 94.484264, -0.294892], [53.950574, 94.411269, -0.308655], [53.934143, 94.325166, -0.313487], [53.950574, 94.239063, -0.308655], [53.997367, 94.166069, -0.294892], [54.067396, 94.117293, -0.274295], [54.15, 94.100166, -0.25], [54.15, 91.850166, -0.25]]}]},
			"L_upLeg_FK_CTL": {"color": 6, "shapes": [{"shapeName": "L_upLeg_FK_CTLShape", "degree": 1, "form": 0, "points": [[2.5, 41.485197, -2.170608], [2.5, 46.446587, -2.790782], [2.5, 47.06676, 2.170608], [2.5, 42.105371, 2.790782], [7.5, 42.105371, 2.790782], [7.5, 47.06676, 2.170608], [7.5, 46.446587, -2.790782], [7.5, 41.485197, -2.170608], [2.5, 41.485197, -2.170608], [2.5, 42.105371, 2.790782], [2.5, 47.06676, 2.170608], [7.5, 47.06676, 2.170608], [7.5, 42.105371, 2.790782], [7.5, 41.485197, -2.170608], [7.5, 46.446587, -2.790782], [2.5, 46.446587, -2.790782]]}]},
			"C_spine_FK_chest_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_spine_FK_chest_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 81.968521, -0.054255], [-0.054255, 81.968521, 0.0], [0.0, 81.968521, 0.054255], [0.054255, 81.968521, 0.0], [0.0, 81.968521, -0.054255], [0.0, 82.022771, 0.0], [0.0, 81.968521, 0.054255], [0.0, 81.914266, 0.0], [-0.054255, 81.968521, 0.0], [0.0, 82.022771, 0.0], [0.054255, 81.968521, 0.0], [0.0, 81.914266, 0.0], [0.0, 81.968521, -0.054255], [0.0, 82.022771, 0.0], [0.0, 76.850166, 0.0]]}, {"shapeName": "C_spine_FK_chest_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 76.850166, -0.054255], [-5.118355, 76.795911, 0.0], [-5.118355, 76.850166, 0.054255], [-5.118355, 76.904421, 0.0], [-5.118355, 76.850166, -0.054255], [-5.172605, 76.850166, 0.0], [-5.118355, 76.850166, 0.054255], [-5.0641, 76.850166, 0.0], [-5.118355, 76.795911, 0.0], [-5.172605, 76.850166, 0.0], [-5.118355, 76.904421, 0.0], [-5.0641, 76.850166, 0.0], [-5.118355, 76.850166, -0.054255], [-5.172605, 76.850166, 0.0], [0.0, 76.850166, 0.0]]}, {"shapeName": "C_spine_FK_chest_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 76.850166, 5.118355], [0.0, 76.795911, 5.118355], [0.054255, 76.850166, 5.118355], [0.0, 76.904421, 5.118355], [-0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.172605], [0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.0641], [0.0, 76.795911, 5.118355], [0.0, 76.850166, 5.172605], [0.0, 76.904421, 5.118355], [0.0, 76.850166, 5.0641], [-0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.172605], [0.0, 76.850166, 0.0]]}]},
			"L_elbow_shaper_02_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_02_CTLShape", "degree": 1, "form": 0, "points": [[42.25, 94.350166, -3.75], [42.341782, 94.369196, -3.723005], [42.419592, 94.423391, -3.70012], [42.471585, 94.504496, -3.684828], [42.489841, 94.600166, -3.679458], [42.471585, 94.695836, -3.684828], [42.419592, 94.776941, -3.70012], [42.341782, 94.831136, -3.723005], [42.25, 94.850166, -3.75], [42.158218, 94.831136, -3.776995], [42.080408, 94.776941, -3.79988], [42.028415, 94.695836, -3.815172], [42.010159, 94.600166, -3.820542], [42.028415, 94.504496, -3.815172], [42.080408, 94.423391, -3.79988], [42.158218, 94.369196, -3.776995], [42.25, 94.350166, -3.75], [42.25, 91.850166, -3.75]]}]},
			"world_D_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -21.66375], [9.624375, 0.0, -12.03], [7.215, 0.0, -12.03], [7.215, 0.0, -7.213125], [12.031875, 0.0, -7.213125], [12.031875, 0.0, -9.6225], [21.66375, 0.0, 0.0], [12.03, 0.0, 9.624375], [12.03, 0.0, 7.215], [7.213125, 0.0, 7.215], [7.213125, 0.0, 12.031875], [9.6225, 0.0, 12.031875], [0.0, 0.0, 21.66375], [-9.624375, 0.0, 12.03], [-7.215, 0.0, 12.03], [-7.215, 0.0, 7.213125], [-12.031875, 0.0, 7.213125], [-12.031875, 0.0, 9.6225], [-21.66375, 0.0, 0.0], [-12.03, 0.0, -9.624375], [-12.03, 0.0, -7.215], [-7.213125, 0.0, -7.215], [-7.213125, 0.0, -12.031875], [-9.6225, 0.0, -12.031875], [0.0, 0.0, -21.66375], [1.88625, 0.02625, -19.81125], [1.72125, 0.0, -19.635], [1.72125, 0.0, -18.915], [1.57125, 0.0, -18.915], [1.580625, 0.0, -19.640625], [1.47375, 0.0, -19.58625], [1.4775, 0.0, -19.27125], [1.325625, 0.0, -19.27125], [1.325625, 0.0, -19.58625], [1.231875, 0.0, -19.640625], [1.231875, 0.0, -18.90375], [1.08, 0.0, -18.90375], [1.08, 0.0, -19.659375], [1.201875, 0.0, -19.78125], [1.389375, 0.0, -19.6875], [1.595625, 0.0, -19.78125], [1.72125, 0.0, -19.63875], [1.595625, 0.0, -19.78125], [1.39125, 0.0, -19.689375], [1.201875, 0.0, -19.779375], [0.83625, 0.0, -19.78125], [0.96, 0.0, -19.659375], [0.96, 0.0, -19.0275], [0.83625, 0.0, -18.90375], [0.440625, 0.0, -18.90375], [0.31875, 0.0, -19.0275], [0.31875, 0.0, -19.659375], [0.440625, 0.0, -19.78125], [0.83625, 0.0, -19.78125], [0.789375, 0.0, -19.640625], [0.808125, 0.0, -19.059375], [0.46875, 0.0, -19.063125], [0.470625, 0.0, -19.640625], [0.79125, 0.0, -19.644375], [0.83625, 0.0, -19.78125], [0.440625, 0.0, -19.78125], [0.1875, 0.0, -19.78125], [0.196875, 0.0, -18.90375], [-0.230625, 0.0, -18.90375], [-0.354375, 0.0, -19.0275], [-0.354375, 0.0, -19.291875], [-0.22875, 0.0, -19.41375], [-0.22125, 0.0, -19.423125], [-0.466875, 0.0, -19.7775], [-0.466875, 0.0, -19.78125], [-0.290625, 0.0, -19.78125], [-0.045, 0.0, -19.425], [0.046875, 0.0, -19.425], [0.046875, 0.0, -19.05], [-0.189375, 0.0, -19.05], [-0.19125, 0.0, -19.273125], [0.046875, 0.0, -19.273125], [0.046875, 0.0, -19.78125], [0.1875, 0.0, -19.78125], [-1.205625, 0.0, -19.78125], [-1.205625, 0.0, -19.640625], [-0.714375, 0.0, -19.63875], [-0.714375, 0.0, -18.90375], [-0.5625, 0.0, -18.90375], [-0.5625, 0.0, -19.78125], [-1.845, 0.0, -19.78125], [-1.9575, 0.0, -19.659375], [-1.966875, 0.0, -19.0275], [-1.845, 0.0, -18.90375], [-1.325625, 0.0, -18.90375], [-1.325625, 0.0, -19.78125], [-1.479375, 0.0, -19.640625], [-1.475625, 0.0, -19.04625], [-1.79625, 0.0, -19.04625], [-1.7925, 0.0, -19.636875], [-1.47375, 0.0, -19.644375], [-1.321875, 0.0, -19.78125]]}]},
			"L_legEnd_FK_CTL": {"color": 6, "shapes": [{"shapeName": "L_legEnd_FK_CTLShape", "degree": 1, "form": 0, "points": [[2.5, 0.581463, -2.772021], [2.5, 5.548, -2.194516], [2.5, 4.970495, 2.772021], [2.5, 0.003958, 2.194516], [7.5, 0.003958, 2.194516], [7.5, 4.970495, 2.772021], [7.5, 5.548, -2.194516], [7.5, 0.581463, -2.772021], [2.5, 0.581463, -2.772021], [2.5, 0.003958, 2.194516], [2.5, 4.970495, 2.772021], [7.5, 4.970495, 2.772021], [7.5, 0.003958, 2.194516], [7.5, 0.581463, -2.772021], [7.5, 5.548, -2.194516], [2.5, 5.548, -2.194516]]}]},
			"L_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_B_CTLShape", "degree": 1, "form": 0, "points": [[63.812803, 92.907587, -0.5], [62.31758, 92.787969, -0.5], [62.31758, 92.787969, -2.0], [63.812803, 92.907587, -2.0], [63.93242, 91.412364, -2.0], [62.437197, 91.292746, -2.0], [62.437197, 91.292746, -0.5], [63.93242, 91.412364, -0.5], [63.812803, 92.907587, -0.5], [63.812803, 92.907587, -2.0], [62.31758, 92.787969, -2.0], [62.437197, 91.292746, -2.0], [63.93242, 91.412364, -2.0], [63.93242, 91.412364, -0.5], [62.437197, 91.292746, -0.5], [62.31758, 92.787969, -0.5]]}]},
			"L_handIk_CTL": {"color": 6, "shapes": [{"shapeName": "L_handIk_CTLShape", "degree": 3, "form": 2, "points": [[55.0, 87.932106, -3.91806], [55.0, 91.850166, -5.54097], [55.0, 95.768226, -3.91806], [55.0, 97.391136, 0.0], [55.0, 95.768226, 3.91806], [55.0, 91.850166, 5.54097], [55.0, 87.932106, 3.91806], [55.0, 86.309196, 0.0]]}]},
			"R_scapulaChest_CTL": {"color": 17, "shapes": [{"shapeName": "R_scapulaChest_CTLShape", "degree": 3, "form": 2, "points": [[0.0, 90.674748, -1.175418], [0.0, 91.850166, -1.662291], [0.0, 93.025584, -1.175418], [0.0, 93.512457, 0.0], [0.0, 93.025584, 1.175418], [0.0, 91.850166, 1.662291], [0.0, 90.674748, 1.175418], [0.0, 90.187875, 0.0]]}, {"shapeName": "R_scapulaChest_CTLShape1", "degree": 3, "form": 2, "points": [[-1.175418, 91.850166, -1.175418], [0.0, 91.850166, -1.662291], [1.175418, 91.850166, -1.175418], [1.662291, 91.850166, 0.0], [1.175418, 91.850166, 1.175418], [0.0, 91.850166, 1.662291], [-1.175418, 91.850166, 1.175418], [-1.662291, 91.850166, 0.0]]}, {"shapeName": "R_scapulaChest_CTLShape2", "degree": 3, "form": 2, "points": [[-1.175418, 93.025584, 0.0], [0.0, 93.512457, 0.0], [1.175418, 93.025584, 0.0], [1.662291, 91.850166, 0.0], [1.175418, 90.674748, 0.0], [0.0, 90.187875, 0.0], [-1.175418, 90.674748, 0.0], [-1.662291, 91.850166, 0.0]]}]},
			"L_loLeg_shaper_03_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_03_CTLShape", "degree": 1, "form": 0, "points": [[17.5, 13.525979, 1.25], [17.59515, 12.955801, 1.1837], [17.866125, 12.472428, 1.127494], [18.27165, 12.149434, 1.089937], [18.75, 12.036018, 1.076749], [19.22835, 12.149434, 1.089937], [19.633875, 12.472428, 1.127494], [19.90485, 12.955801, 1.1837], [20.0, 13.525979, 1.25], [19.90485, 14.096157, 1.3163], [19.633875, 14.57953, 1.372506], [19.22835, 14.902524, 1.410063], [18.75, 15.01594, 1.423251], [18.27165, 14.902524, 1.410063], [17.866125, 14.57953, 1.372506], [17.59515, 14.096157, 1.3163], [17.5, 13.525979, 1.25], [5.0, 13.525979, 1.25]]}]},
			"L_scapulaCtrl_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_scapulaCtrl_PIV_CTLShape", "degree": 1, "form": 0, "points": [[14.023671, 91.850166, -14.010851], [14.023671, 91.861017, -14.0], [14.023671, 91.850166, -13.989149], [14.023671, 91.839315, -14.0], [14.023671, 91.850166, -14.010851], [14.034521, 91.850166, -14.0], [14.023671, 91.850166, -13.989149], [14.01282, 91.850166, -14.0], [14.023671, 91.861017, -14.0], [14.034521, 91.850166, -14.0], [14.023671, 91.839315, -14.0], [14.01282, 91.850166, -14.0], [14.023671, 91.850166, -14.010851], [14.034521, 91.850166, -14.0], [13.0, 91.850166, -14.0]]}, {"shapeName": "L_scapulaCtrl_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[13.0, 92.873837, -14.010851], [12.989149, 92.873837, -14.0], [13.0, 92.873837, -13.989149], [13.010851, 92.873837, -14.0], [13.0, 92.873837, -14.010851], [13.0, 92.884687, -14.0], [13.0, 92.873837, -13.989149], [13.0, 92.862986, -14.0], [12.989149, 92.873837, -14.0], [13.0, 92.884687, -14.0], [13.010851, 92.873837, -14.0], [13.0, 92.862986, -14.0], [13.0, 92.873837, -14.010851], [13.0, 92.884687, -14.0], [13.0, 91.850166, -14.0]]}, {"shapeName": "L_scapulaCtrl_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[13.0, 91.861017, -12.976329], [12.989149, 91.850166, -12.976329], [13.0, 91.839315, -12.976329], [13.010851, 91.850166, -12.976329], [13.0, 91.861017, -12.976329], [13.0, 91.850166, -12.965479], [13.0, 91.839315, -12.976329], [13.0, 91.850166, -12.98718], [12.989149, 91.850166, -12.976329], [13.0, 91.850166, -12.965479], [13.010851, 91.850166, -12.976329], [13.0, 91.850166, -12.98718], [13.0, 91.861017, -12.976329], [13.0, 91.850166, -12.965479], [13.0, 91.850166, -14.0]]}]},
			"C_neck_FK_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 96.973853, -0.054255], [-0.054255, 96.973853, 0.0], [0.0, 96.973853, 0.054255], [0.054255, 96.973853, 0.0], [0.0, 96.973853, -0.054255], [0.0, 97.028103, 0.0], [0.0, 96.973853, 0.054255], [0.0, 96.919598, 0.0], [-0.054255, 96.973853, 0.0], [0.0, 97.028103, 0.0], [0.054255, 96.973853, 0.0], [0.0, 96.919598, 0.0], [0.0, 96.973853, -0.054255], [0.0, 97.028103, 0.0], [0.0, 91.855498, 0.0]]}, {"shapeName": "C_neck_FK_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 91.855498, -0.054255], [-5.118355, 91.801243, 0.0], [-5.118355, 91.855498, 0.054255], [-5.118355, 91.909753, 0.0], [-5.118355, 91.855498, -0.054255], [-5.172605, 91.855498, 0.0], [-5.118355, 91.855498, 0.054255], [-5.0641, 91.855498, 0.0], [-5.118355, 91.801243, 0.0], [-5.172605, 91.855498, 0.0], [-5.118355, 91.909753, 0.0], [-5.0641, 91.855498, 0.0], [-5.118355, 91.855498, -0.054255], [-5.172605, 91.855498, 0.0], [0.0, 91.855498, 0.0]]}, {"shapeName": "C_neck_FK_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 91.855498, 5.118355], [0.0, 91.801243, 5.118355], [0.054255, 91.855498, 5.118355], [0.0, 91.909753, 5.118355], [-0.054255, 91.855498, 5.118355], [0.0, 91.855498, 5.172605], [0.054255, 91.855498, 5.118355], [0.0, 91.855498, 5.0641], [0.0, 91.801243, 5.118355], [0.0, 91.855498, 5.172605], [0.0, 91.909753, 5.118355], [0.0, 91.855498, 5.0641], [-0.054255, 91.855498, 5.118355], [0.0, 91.855498, 5.172605], [0.0, 91.855498, 0.0]]}]},
			"R_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_D_CTLShape", "degree": 1, "form": 0, "points": [[-67.717544, 92.744464, -0.5], [-66.230702, 92.94271, -0.5], [-66.230702, 92.94271, -2.0], [-67.717544, 92.744464, -2.0], [-67.519298, 91.257623, -2.0], [-66.032456, 91.455868, -2.0], [-66.032456, 91.455868, -0.5], [-67.519298, 91.257623, -0.5], [-67.717544, 92.744464, -0.5], [-67.717544, 92.744464, -2.0], [-66.230702, 92.94271, -2.0], [-66.032456, 91.455868, -2.0], [-67.519298, 91.257623, -2.0], [-67.519298, 91.257623, -0.5], [-66.032456, 91.455868, -0.5], [-66.230702, 92.94271, -0.5]]}]},
			"C_neck_FK_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 100.301855, -0.054255], [-0.054255, 100.301855, 0.0], [0.0, 100.301855, 0.054255], [0.054255, 100.301855, 0.0], [0.0, 100.301855, -0.054255], [0.0, 100.356105, 0.0], [0.0, 100.301855, 0.054255], [0.0, 100.2476, 0.0], [-0.054255, 100.301855, 0.0], [0.0, 100.356105, 0.0], [0.054255, 100.301855, 0.0], [0.0, 100.2476, 0.0], [0.0, 100.301855, -0.054255], [0.0, 100.356105, 0.0], [0.0, 95.1835, 0.0]]}, {"shapeName": "C_neck_FK_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 95.1835, -0.054255], [-5.118355, 95.129245, 0.0], [-5.118355, 95.1835, 0.054255], [-5.118355, 95.237755, 0.0], [-5.118355, 95.1835, -0.054255], [-5.172605, 95.1835, 0.0], [-5.118355, 95.1835, 0.054255], [-5.0641, 95.1835, 0.0], [-5.118355, 95.129245, 0.0], [-5.172605, 95.1835, 0.0], [-5.118355, 95.237755, 0.0], [-5.0641, 95.1835, 0.0], [-5.118355, 95.1835, -0.054255], [-5.172605, 95.1835, 0.0], [0.0, 95.1835, 0.0]]}, {"shapeName": "C_neck_FK_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 95.1835, 5.118355], [0.0, 95.129245, 5.118355], [0.054255, 95.1835, 5.118355], [0.0, 95.237755, 5.118355], [-0.054255, 95.1835, 5.118355], [0.0, 95.1835, 5.172605], [0.054255, 95.1835, 5.118355], [0.0, 95.1835, 5.0641], [0.0, 95.129245, 5.118355], [0.0, 95.1835, 5.172605], [0.0, 95.237755, 5.118355], [0.0, 95.1835, 5.0641], [-0.054255, 95.1835, 5.118355], [0.0, 95.1835, 5.172605], [0.0, 95.1835, 0.0]]}]},
			"R_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.323456, 92.526661, -0.054255], [-66.316286, 92.58044, -0.0], [-66.323456, 92.526661, 0.054255], [-66.330627, 92.472882, -0.0], [-66.323456, 92.526661, -0.054255], [-66.37723, 92.533831, -0.0], [-66.323456, 92.526661, 0.054255], [-66.269677, 92.519491, -0.0], [-66.316286, 92.58044, -0.0], [-66.37723, 92.533831, -0.0], [-66.330627, 92.472882, -0.0], [-66.269677, 92.519491, -0.0], [-66.323456, 92.526661, -0.054255], [-66.37723, 92.533831, -0.0], [-61.25, 91.8502, -0.0]]}, {"shapeName": "R_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-60.573539, 96.923657, -0.054255], [-60.51976, 96.916486, 0.0], [-60.573539, 96.923657, 0.054255], [-60.627318, 96.930827, 0.0], [-60.573539, 96.923657, -0.054255], [-60.566369, 96.977431, 0.0], [-60.573539, 96.923657, 0.054255], [-60.58071, 96.869878, 0.0], [-60.51976, 96.916486, 0.0], [-60.566369, 96.977431, 0.0], [-60.627318, 96.930827, 0.0], [-60.58071, 96.869878, 0.0], [-60.573539, 96.923657, -0.054255], [-60.566369, 96.977431, 0.0], [-61.25, 91.8502, -0.0]]}, {"shapeName": "R_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.242829, 91.903979, 5.118355], [-61.196221, 91.84303, 5.118355], [-61.257171, 91.796421, 5.118355], [-61.303779, 91.857371, 5.118355], [-61.242829, 91.903979, 5.118355], [-61.25, 91.8502, 5.172605], [-61.257171, 91.796421, 5.118355], [-61.25, 91.8502, 5.0641], [-61.196221, 91.84303, 5.118355], [-61.25, 91.8502, 5.172605], [-61.303779, 91.857371, 5.118355], [-61.25, 91.8502, 5.0641], [-61.242829, 91.903979, 5.118355], [-61.25, 91.8502, 5.172605], [-61.25, 91.8502, -0.0]]}]},
			"R_bendyLeg_C_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.333332, 13.294977, 3.236615], [-3.933332, 13.294977, 3.236615], [-5.0, 13.179476, 4.229922], [-6.066668, 13.294977, 3.236615], [-5.666668, 13.294977, 3.236615], [-5.666668, 13.448978, 1.912206], [-7.0, 13.448978, 1.912206], [-7.0, 13.402778, 2.309529], [-8.0, 13.525979, 1.25], [-7.0, 13.64918, 0.190471], [-7.0, 13.60298, 0.587794], [-5.666668, 13.60298, 0.587794], [-5.666668, 13.756981, -0.736615], [-6.066668, 13.756981, -0.736615], [-5.0, 13.872482, -1.729922], [-3.933332, 13.756981, -0.736615], [-4.333332, 13.756981, -0.736615], [-4.333332, 13.60298, 0.587794], [-3.0, 13.60298, 0.587794], [-3.0, 13.64918, 0.190471], [-2.0, 13.525979, 1.25], [-3.0, 13.402778, 2.309529], [-3.0, 13.448978, 1.912206], [-4.333332, 13.448978, 1.912206], [-4.333332, 13.294977, 3.236615]]}]},
			"R_upLeg_shaper_04_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_04_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.25, 30.942646, 1.666667], [-16.335635, 30.430017, 1.730745], [-16.579512, 29.995432, 1.785068], [-16.944485, 29.705039, 1.821368], [-17.375, 29.60307, 1.834114], [-17.805515, 29.705039, 1.821368], [-18.170488, 29.995432, 1.785068], [-18.414365, 30.430017, 1.730745], [-18.5, 30.942646, 1.666667], [-18.414365, 31.455274, 1.602588], [-18.170488, 31.889859, 1.548265], [-17.805515, 32.180252, 1.511966], [-17.375, 32.282221, 1.49922], [-16.944485, 32.180252, 1.511966], [-16.579512, 31.889859, 1.548265], [-16.335635, 31.455274, 1.602588], [-16.25, 30.942646, 1.666667], [-5.0, 30.942646, 1.666667]]}]},
			"R_uprArmRibbonMid_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_uprArmRibbonMid_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-27.929425, 93.183502, -6.354072], [-27.929425, 93.983502, -6.354072], [-27.394137, 91.850166, -8.281107], [-27.929425, 89.71683, -6.354072], [-27.929425, 90.51683, -6.354072], [-28.643141, 90.51683, -3.784693], [-28.643141, 87.850166, -3.784693], [-28.429026, 87.850166, -4.555507], [-29.0, 85.850166, -2.5], [-29.570974, 87.850166, -0.444493], [-29.356859, 87.850166, -1.215307], [-29.356859, 90.51683, -1.215307], [-30.070575, 90.51683, 1.354072], [-30.070575, 89.71683, 1.354072], [-30.605863, 91.850166, 3.281107], [-30.070575, 93.983502, 1.354072], [-30.070575, 93.183502, 1.354072], [-29.356859, 93.183502, -1.215307], [-29.356859, 95.850166, -1.215307], [-29.570974, 95.850166, -0.444493], [-29.0, 97.850166, -2.5], [-28.429026, 95.850166, -4.555507], [-28.643141, 95.850166, -3.784693], [-28.643141, 93.183502, -3.784693], [-27.929425, 93.183502, -6.354072]]}]},
			"L_bendyLeg_A_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_A_CTLShape", "degree": 1, "form": 0, "points": [[4.166665, 34.586066, 3.730695], [3.666665, 34.586066, 3.730695], [5.0, 34.741109, 4.971042], [6.333335, 34.586066, 3.730695], [5.833335, 34.586066, 3.730695], [5.833335, 34.379341, 2.0769], [7.5, 34.379341, 2.0769], [7.5, 34.441359, 2.573039], [8.75, 34.275979, 1.25], [7.5, 34.110599, -0.073039], [7.5, 34.172616, 0.4231], [5.833335, 34.172616, 0.4231], [5.833335, 33.965892, -1.230695], [6.333335, 33.965892, -1.230695], [5.0, 33.810849, -2.471042], [3.666665, 33.965892, -1.230695], [4.166665, 33.965892, -1.230695], [4.166665, 34.172616, 0.4231], [2.5, 34.172616, 0.4231], [2.5, 34.110599, -0.073039], [1.25, 34.275979, 1.25], [2.5, 34.441359, 2.573039], [2.5, 34.379341, 2.0769], [4.166665, 34.379341, 2.0769], [4.166665, 34.586066, 3.730695]]}]},
			"R_shoulder_shaper_03_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_shoulder_shaper_03_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-29.0, 93.600166, -2.5], [-29.064526, 93.613487, -2.517924], [-29.119228, 93.651424, -2.533119], [-29.155781, 93.708197, -2.543272], [-29.168616, 93.775166, -2.546838], [-29.155781, 93.842135, -2.543272], [-29.119228, 93.898909, -2.533119], [-29.064526, 93.936845, -2.517924], [-29.0, 93.950166, -2.5], [-28.935474, 93.936845, -2.482076], [-28.880772, 93.898909, -2.466881], [-28.844219, 93.842135, -2.456728], [-28.831384, 93.775166, -2.453162], [-28.844219, 93.708197, -2.456728], [-28.880772, 93.651424, -2.466881], [-28.935474, 93.613487, -2.482076], [-29.0, 93.600166, -2.5], [-29.0, 91.850166, -2.5]]}]},
			"L_upLeg_shaper_03_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_03_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[12.5, 34.275979, 1.25], [12.55709, 33.934227, 1.292719], [12.719675, 33.644503, 1.328934], [12.96299, 33.450908, 1.353134], [13.25, 33.382929, 1.361631], [13.53701, 33.450908, 1.353134], [13.780325, 33.644503, 1.328934], [13.94291, 33.934227, 1.292719], [14.0, 34.275979, 1.25], [13.94291, 34.617731, 1.207281], [13.780325, 34.907455, 1.171066], [13.53701, 35.10105, 1.146866], [13.25, 35.169029, 1.138369], [12.96299, 35.10105, 1.146866], [12.719675, 34.907455, 1.171066], [12.55709, 34.617731, 1.207281], [12.5, 34.275979, 1.25], [5.0, 34.275979, 1.25]]}]},
			"R_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.227054, 92.508365, -2.554255], [-68.222728, 92.562447, -2.5], [-68.227054, 92.508365, -2.445745], [-68.231381, 92.454282, -2.5], [-68.227054, 92.508365, -2.554255], [-68.281132, 92.512691, -2.5], [-68.227054, 92.508365, -2.445745], [-68.172972, 92.504038, -2.5], [-68.222728, 92.562447, -2.5], [-68.281132, 92.512691, -2.5], [-68.231381, 92.454282, -2.5], [-68.172972, 92.504038, -2.5], [-68.227054, 92.508365, -2.554255], [-68.281132, 92.512691, -2.5], [-63.125, 92.1002, -2.5]]}, {"shapeName": "R_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-62.716836, 97.202255, -2.554255], [-62.662753, 97.197928, -2.5], [-62.716836, 97.202255, -2.445745], [-62.770918, 97.206581, -2.5], [-62.716836, 97.202255, -2.554255], [-62.712509, 97.256332, -2.5], [-62.716836, 97.202255, -2.445745], [-62.721162, 97.148173, -2.5], [-62.662753, 97.197928, -2.5], [-62.712509, 97.256332, -2.5], [-62.770918, 97.206581, -2.5], [-62.721162, 97.148173, -2.5], [-62.716836, 97.202255, -2.554255], [-62.712509, 97.256332, -2.5], [-63.125, 92.1002, -2.5]]}, {"shapeName": "R_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-63.120673, 92.154283, 2.618355], [-63.070918, 92.095874, 2.618355], [-63.129327, 92.046118, 2.618355], [-63.179082, 92.104527, 2.618355], [-63.120673, 92.154283, 2.618355], [-63.125, 92.1002, 2.672605], [-63.129327, 92.046118, 2.618355], [-63.125, 92.1002, 2.5641], [-63.070918, 92.095874, 2.618355], [-63.125, 92.1002, 2.672605], [-63.179082, 92.104527, 2.618355], [-63.125, 92.1002, 2.5641], [-63.120673, 92.154283, 2.618355], [-63.125, 92.1002, 2.672605], [-63.125, 92.1002, -2.5]]}]},
			"R_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-65.318379, 92.276816, 5.576815], [-65.274612, 92.256657, 5.636525], [-65.291252, 92.182844, 5.623801], [-65.335019, 92.203002, 5.564091], [-65.318379, 92.276816, 5.576815], [-65.347793, 92.233854, 5.633168], [-65.291252, 92.182844, 5.623801], [-65.261834, 92.225806, 5.567444], [-65.274612, 92.256657, 5.636525], [-65.347793, 92.233854, 5.633168], [-65.335019, 92.203002, 5.564091], [-65.261834, 92.225806, 5.567444], [-65.318379, 92.276816, 5.576815], [-65.347793, 92.233854, 5.633168], [-61.25, 91.8502, 2.5]]}, {"shapeName": "R_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-58.414234, 94.42805, 5.893173], [-58.357689, 94.37704, 5.883802], [-58.387106, 94.334078, 5.940159], [-58.443651, 94.385088, 5.949529], [-58.414234, 94.42805, 5.893173], [-58.37047, 94.407889, 5.95288], [-58.387106, 94.334078, 5.940159], [-58.430873, 94.354237, 5.880449], [-58.357689, 94.37704, 5.883802], [-58.37047, 94.407889, 5.95288], [-58.443651, 94.385088, 5.949529], [-58.430873, 94.354237, 5.880449], [-58.414234, 94.42805, 5.893173], [-58.37047, 94.407889, 5.95288], [-61.25, 91.8502, 2.5]]}, {"shapeName": "R_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-59.940208, 87.444402, 4.75253], [-59.92743, 87.413551, 4.683449], [-60.000614, 87.390747, 4.680096], [-60.013393, 87.421599, 4.749176], [-59.940208, 87.444402, 4.75253], [-59.956849, 87.370593, 4.739804], [-60.000614, 87.390747, 4.680096], [-59.983975, 87.464561, 4.69282], [-59.92743, 87.413551, 4.683449], [-59.956849, 87.370593, 4.739804], [-60.013393, 87.421599, 4.749176], [-59.983975, 87.464561, 4.69282], [-59.940208, 87.444402, 4.75253], [-59.956849, 87.370593, 4.739804], [-61.25, 91.8502, 2.5]]}]},
			"L_loLeg_FK_CTL": {"color": 6, "shapes": [{"shapeName": "L_loLeg_FK_CTLShape", "degree": 1, "form": 0, "points": [[2.5, 22.081463, -0.272021], [2.5, 27.048, 0.305484], [2.5, 26.470495, 5.272021], [2.5, 21.503958, 4.694516], [7.5, 21.503958, 4.694516], [7.5, 26.470495, 5.272021], [7.5, 27.048, 0.305484], [7.5, 22.081463, -0.272021], [2.5, 22.081463, -0.272021], [2.5, 21.503958, 4.694516], [2.5, 26.470495, 5.272021], [7.5, 26.470495, 5.272021], [7.5, 21.503958, 4.694516], [7.5, 22.081463, -0.272021], [7.5, 27.048, 0.305484], [2.5, 27.048, 0.305484]]}]},
			"L_uprArmRibbonMid_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_uprArmRibbonMid_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[27.795603, 93.350169, -6.835831], [27.795603, 94.250169, -6.835831], [27.193404, 91.850166, -9.003746], [27.795603, 89.450163, -6.835831], [27.795603, 90.350163, -6.835831], [28.598533, 90.350163, -3.94528], [28.598533, 87.350166, -3.94528], [28.357654, 87.350166, -4.812446], [29.0, 85.100166, -2.5], [29.642346, 87.350166, -0.187554], [29.401467, 87.350166, -1.05472], [29.401467, 90.350163, -1.05472], [30.204397, 90.350163, 1.835831], [30.204397, 89.450163, 1.835831], [30.806596, 91.850166, 4.003746], [30.204397, 94.250169, 1.835831], [30.204397, 93.350169, 1.835831], [29.401467, 93.350169, -1.05472], [29.401467, 96.350166, -1.05472], [29.642346, 96.350166, -0.187554], [29.0, 98.600166, -2.5], [28.357654, 96.350166, -4.812446], [28.598533, 96.350166, -3.94528], [28.598533, 93.350169, -3.94528], [27.795603, 93.350169, -6.835831]]}]},
			"L_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[71.948456, 91.423705, -2.554255], [71.955627, 91.477485, -2.5], [71.948456, 91.423705, -2.445745], [71.941286, 91.369926, -2.5], [71.948456, 91.423705, -2.554255], [72.00223, 91.416536, -2.5], [71.948456, 91.423705, -2.445745], [71.894677, 91.430876, -2.5], [71.955627, 91.477485, -2.5], [72.00223, 91.416536, -2.5], [71.941286, 91.369926, -2.5], [71.894677, 91.430876, -2.5], [71.948456, 91.423705, -2.554255], [72.00223, 91.416536, -2.5], [66.875, 92.100166, -2.5]]}, {"shapeName": "L_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.551461, 97.173623, -2.554255], [67.497682, 97.180793, -2.5], [67.551461, 97.173623, -2.445745], [67.60524, 97.166452, -2.5], [67.551461, 97.173623, -2.554255], [67.558631, 97.227397, -2.5], [67.551461, 97.173623, -2.445745], [67.54429, 97.119844, -2.5], [67.497682, 97.180793, -2.5], [67.558631, 97.227397, -2.5], [67.60524, 97.166452, -2.5], [67.54429, 97.119844, -2.5], [67.551461, 97.173623, -2.554255], [67.558631, 97.227397, -2.5], [66.875, 92.100166, -2.5]]}, {"shapeName": "L_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[66.882171, 92.153945, 2.618355], [66.821221, 92.107337, 2.618355], [66.867829, 92.046387, 2.618355], [66.928779, 92.092996, 2.618355], [66.882171, 92.153945, 2.618355], [66.875, 92.100166, 2.672605], [66.867829, 92.046387, 2.618355], [66.875, 92.100166, 2.5641], [66.821221, 92.107337, 2.618355], [66.875, 92.100166, 2.672605], [66.928779, 92.092996, 2.618355], [66.875, 92.100166, 2.5641], [66.882171, 92.153945, 2.618355], [66.875, 92.100166, 2.672605], [66.875, 92.100166, -2.5]]}]},
			"L_bendyLeg_C_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyLeg_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.416665, 13.323853, 2.988288], [4.066666, 13.323853, 2.988288], [5.0, 13.222789, 3.857432], [5.933334, 13.323853, 2.988288], [5.583335, 13.323853, 2.988288], [5.583335, 13.458603, 1.82943], [6.75, 13.458603, 1.82943], [6.75, 13.418178, 2.177088], [7.625, 13.525979, 1.25], [6.75, 13.63378, 0.322912], [6.75, 13.593355, 0.67057], [5.583335, 13.593355, 0.67057], [5.583335, 13.728106, -0.488288], [5.933334, 13.728106, -0.488288], [5.0, 13.829169, -1.357432], [4.066666, 13.728106, -0.488288], [4.416665, 13.728106, -0.488288], [4.416665, 13.593355, 0.67057], [3.25, 13.593355, 0.67057], [3.25, 13.63378, 0.322912], [2.375, 13.525979, 1.25], [3.25, 13.418178, 2.177088], [3.25, 13.458603, 1.82943], [4.416665, 13.458603, 1.82943], [4.416665, 13.323853, 2.988288]]}]},
			"L_lwrArmTwist_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lwrArmTwist_PIV_CTLShape", "degree": 1, "form": 0, "points": [[56.023671, 91.850166, -0.010851], [56.023671, 91.861017, 0.0], [56.023671, 91.850166, 0.010851], [56.023671, 91.839315, 0.0], [56.023671, 91.850166, -0.010851], [56.034521, 91.850166, 0.0], [56.023671, 91.850166, 0.010851], [56.01282, 91.850166, 0.0], [56.023671, 91.861017, 0.0], [56.034521, 91.850166, 0.0], [56.023671, 91.839315, 0.0], [56.01282, 91.850166, 0.0], [56.023671, 91.850166, -0.010851], [56.034521, 91.850166, 0.0], [55.0, 91.850166, 0.0]]}, {"shapeName": "L_lwrArmTwist_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[55.0, 92.873837, -0.010851], [54.989149, 92.873837, 0.0], [55.0, 92.873837, 0.010851], [55.010851, 92.873837, 0.0], [55.0, 92.873837, -0.010851], [55.0, 92.884687, 0.0], [55.0, 92.873837, 0.010851], [55.0, 92.862986, 0.0], [54.989149, 92.873837, 0.0], [55.0, 92.884687, 0.0], [55.010851, 92.873837, 0.0], [55.0, 92.862986, 0.0], [55.0, 92.873837, -0.010851], [55.0, 92.884687, 0.0], [55.0, 91.850166, 0.0]]}, {"shapeName": "L_lwrArmTwist_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[55.0, 91.861017, 1.023671], [54.989149, 91.850166, 1.023671], [55.0, 91.839315, 1.023671], [55.010851, 91.850166, 1.023671], [55.0, 91.861017, 1.023671], [55.0, 91.850166, 1.034521], [55.0, 91.839315, 1.023671], [55.0, 91.850166, 1.01282], [54.989149, 91.850166, 1.023671], [55.0, 91.850166, 1.034521], [55.010851, 91.850166, 1.023671], [55.0, 91.850166, 1.01282], [55.0, 91.861017, 1.023671], [55.0, 91.850166, 1.034521], [55.0, 91.850166, 0.0]]}]},
			"L_upLeg_shaper_02_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_02_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[15.0, 37.609312, 0.833333], [15.07612, 37.153642, 0.890292], [15.2929, 36.767345, 0.938579], [15.61732, 36.509217, 0.970845], [16.0, 36.418579, 0.982175], [16.38268, 36.509217, 0.970845], [16.7071, 36.767345, 0.938579], [16.92388, 37.153642, 0.890292], [17.0, 37.609312, 0.833333], [16.92388, 38.064982, 0.776375], [16.7071, 38.45128, 0.728087], [16.38268, 38.709407, 0.695821], [16.0, 38.800046, 0.684492], [15.61732, 38.709407, 0.695821], [15.2929, 38.45128, 0.728087], [15.07612, 38.064982, 0.776375], [15.0, 37.609312, 0.833333], [5.0, 37.609312, 0.833333]]}]},
			"R_uprArmRibbonMid_CTL": {"color": 17, "shapes": [{"shapeName": "R_uprArmRibbonMid_CTLShape", "degree": 1, "form": 0, "points": [[-27.661781, 93.516836, -7.31759], [-27.661781, 94.516836, -7.31759], [-26.992671, 91.850166, -9.726384], [-27.661781, 89.183496, -7.31759], [-27.661781, 90.183496, -7.31759], [-28.553926, 90.183496, -4.105866], [-28.553926, 86.850166, -4.105866], [-28.286282, 86.850166, -5.069384], [-29.0, 84.350166, -2.5], [-29.713718, 86.850166, 0.069384], [-29.446074, 86.850166, -0.894134], [-29.446074, 90.183496, -0.894134], [-30.338219, 90.183496, 2.31759], [-30.338219, 89.183496, 2.31759], [-31.007329, 91.850166, 4.726384], [-30.338219, 94.516836, 2.31759], [-30.338219, 93.516836, 2.31759], [-29.446074, 93.516836, -0.894134], [-29.446074, 96.850166, -0.894134], [-29.713718, 96.850166, 0.069384], [-29.0, 99.350166, -2.5], [-28.286282, 96.850166, -5.069384], [-28.553926, 96.850166, -4.105866], [-28.553926, 93.516836, -4.105866], [-27.661781, 93.516836, -7.31759]]}]},
			"R_toe_IK_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-6.175418, 1.451397, 5.0], [-5.0, 1.93827, 5.0], [-3.824582, 1.451397, 5.0], [-3.337709, 0.275979, 5.0], [-3.824582, -0.899439, 5.0], [-5.0, -1.386312, 5.0], [-6.175418, -0.899439, 5.0], [-6.662291, 0.275979, 5.0]]}]},
			"L_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_D_CTLShape", "degree": 1, "form": 0, "points": [[67.717544, 92.744464, -0.5], [66.230702, 92.94271, -0.5], [66.230702, 92.94271, -2.0], [67.717544, 92.744464, -2.0], [67.519298, 91.257623, -2.0], [66.032456, 91.455868, -2.0], [66.032456, 91.455868, -0.5], [67.519298, 91.257623, -0.5], [67.717544, 92.744464, -0.5], [67.717544, 92.744464, -2.0], [66.230702, 92.94271, -2.0], [66.032456, 91.455868, -2.0], [67.519298, 91.257623, -2.0], [67.519298, 91.257623, -0.5], [66.032456, 91.455868, -0.5], [66.230702, 92.94271, -0.5]]}]},
			"R_legBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 39.203878, 0.68869], [-4.945745, 39.197149, 0.634854], [-5.0, 39.190419, 0.581018], [-5.054255, 39.197149, 0.634854], [-5.0, 39.203878, 0.68869], [-5.0, 39.143317, 0.641583], [-5.0, 39.190419, 0.581018], [-5.0, 39.250985, 0.628124], [-4.945745, 39.197149, 0.634854], [-5.0, 39.143317, 0.641583], [-5.054255, 39.197149, 0.634854], [-5.0, 39.250985, 0.628124], [-5.0, 39.203878, 0.68869], [-5.0, 39.143317, 0.641583], [-5.0, 44.275979, 0.0]]}, {"shapeName": "R_legBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 44.282708, 0.053836], [0.118355, 44.329815, -0.00673], [0.118355, 44.269249, -0.053836], [0.118355, 44.222143, 0.00673], [0.118355, 44.282708, 0.053836], [0.172605, 44.275979, 0.0], [0.118355, 44.269249, -0.053836], [0.0641, 44.275979, 0.0], [0.118355, 44.329815, -0.00673], [0.172605, 44.275979, 0.0], [0.118355, 44.222143, 0.00673], [0.0641, 44.275979, 0.0], [0.118355, 44.282708, 0.053836], [0.172605, 44.275979, 0.0], [-5.0, 44.275979, 0.0]]}, {"shapeName": "R_legBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 43.641125, -5.07883], [-5.0, 43.694961, -5.08556], [-5.054255, 43.641125, -5.07883], [-5.0, 43.587289, -5.072101], [-4.945745, 43.641125, -5.07883], [-5.0, 43.634396, -5.132662], [-5.054255, 43.641125, -5.07883], [-5.0, 43.647855, -5.024994], [-5.0, 43.694961, -5.08556], [-5.0, 43.634396, -5.132662], [-5.0, 43.587289, -5.072101], [-5.0, 43.647855, -5.024994], [-4.945745, 43.641125, -5.07883], [-5.0, 43.634396, -5.132662], [-5.0, 44.275979, 0.0]]}]},
			"L_loLeg_shaper_02_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_02_CTLShape", "degree": 1, "form": 0, "points": [[17.5, 17.109312, 1.666667], [17.59515, 16.539134, 1.600367], [17.866125, 16.055761, 1.544161], [18.27165, 15.732767, 1.506603], [18.75, 15.619351, 1.493415], [19.22835, 15.732767, 1.506603], [19.633875, 16.055761, 1.544161], [19.90485, 16.539134, 1.600367], [20.0, 17.109312, 1.666667], [19.90485, 17.679491, 1.732966], [19.633875, 18.162864, 1.789173], [19.22835, 18.485858, 1.82673], [18.75, 18.599273, 1.839918], [18.27165, 18.485858, 1.82673], [17.866125, 18.162864, 1.789173], [17.59515, 17.679491, 1.732966], [17.5, 17.109312, 1.666667], [5.0, 17.109312, 1.666667]]}]},
			"R_upLeg_shaper_05_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_05_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.25, 27.609312, 2.083333], [-16.335635, 27.096684, 2.147412], [-16.579512, 26.662099, 2.201735], [-16.944485, 26.371706, 2.238034], [-17.375, 26.269737, 2.25078], [-17.805515, 26.371706, 2.238034], [-18.170488, 26.662099, 2.201735], [-18.414365, 27.096684, 2.147412], [-18.5, 27.609312, 2.083333], [-18.414365, 28.121941, 2.019255], [-18.170488, 28.556526, 1.964932], [-17.805515, 28.846919, 1.928632], [-17.375, 28.948887, 1.915886], [-16.944485, 28.846919, 1.928632], [-16.579512, 28.556526, 1.964932], [-16.335635, 28.121941, 2.019255], [-16.25, 27.609312, 2.083333], [-5.0, 27.609312, 2.083333]]}]},
			"C_head_top_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_top_CTLShape", "degree": 1, "form": 0, "points": [[-1.25, 113.100166, 1.25], [-1.25, 110.600166, 1.25], [-1.25, 110.600166, -1.25], [-1.25, 113.100166, -1.25], [1.25, 113.100166, -1.25], [1.25, 110.600166, -1.25], [1.25, 110.600166, 1.25], [1.25, 113.100166, 1.25], [-1.25, 113.100166, 1.25], [-1.25, 113.100166, -1.25], [-1.25, 110.600166, -1.25], [1.25, 110.600166, -1.25], [1.25, 113.100166, -1.25], [1.25, 113.100166, 1.25], [1.25, 110.600166, 1.25], [-1.25, 110.600166, 1.25]]}]},
			"R_uprArmRibbonMid_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_uprArmRibbonMid_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-28.063246, 93.016835, -5.872313], [-28.063246, 93.716835, -5.872313], [-27.59487, 91.850166, -7.558469], [-28.063246, 89.983497, -5.872313], [-28.063246, 90.683497, -5.872313], [-28.687748, 90.683497, -3.624106], [-28.687748, 88.350166, -3.624106], [-28.500397, 88.350166, -4.298569], [-29.0, 86.600166, -2.5], [-29.499603, 88.350166, -0.701431], [-29.312252, 88.350166, -1.375894], [-29.312252, 90.683497, -1.375894], [-29.936754, 90.683497, 0.872313], [-29.936754, 89.983497, 0.872313], [-30.40513, 91.850166, 2.558469], [-29.936754, 93.716835, 0.872313], [-29.936754, 93.016835, 0.872313], [-29.312252, 93.016835, -1.375894], [-29.312252, 95.350166, -1.375894], [-29.499603, 95.350166, -0.701431], [-29.0, 97.100166, -2.5], [-28.500397, 95.350166, -4.298569], [-28.687748, 95.350166, -3.624106], [-28.687748, 93.016835, -3.624106], [-28.063246, 93.016835, -5.872313]]}]},
			"L_toe_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.175418, 1.451397, 5.0], [5.0, 1.93827, 5.0], [3.824582, 1.451397, 5.0], [3.337709, 0.275979, 5.0], [3.824582, -0.899439, 5.0], [5.0, -1.386312, 5.0], [6.175418, -0.899439, 5.0], [6.662291, 0.275979, 5.0]]}]},
			"L_upLeg_shaper_01_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_01_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[12.5, 40.942646, 0.416667], [12.55709, 40.600893, 0.459386], [12.719675, 40.31117, 0.495601], [12.96299, 40.117575, 0.519801], [13.25, 40.049596, 0.528298], [13.53701, 40.117575, 0.519801], [13.780325, 40.31117, 0.495601], [13.94291, 40.600893, 0.459386], [14.0, 40.942646, 0.416667], [13.94291, 41.284398, 0.373948], [13.780325, 41.574121, 0.337732], [13.53701, 41.767717, 0.313533], [13.25, 41.835696, 0.305035], [12.96299, 41.767717, 0.313533], [12.719675, 41.574121, 0.337732], [12.55709, 41.284398, 0.373948], [12.5, 40.942646, 0.416667], [5.0, 40.942646, 0.416667]]}]},
			"R_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_A_CTLShape", "degree": 1, "form": 0, "points": [[-61.894298, 92.69271, 0.75], [-60.407456, 92.494464, 0.75], [-60.407456, 92.494464, -0.75], [-61.894298, 92.69271, -0.75], [-62.092544, 91.205868, -0.75], [-60.605702, 91.007623, -0.75], [-60.605702, 91.007623, 0.75], [-62.092544, 91.205868, 0.75], [-61.894298, 92.69271, 0.75], [-61.894298, 92.69271, -0.75], [-60.407456, 92.494464, -0.75], [-60.605702, 91.007623, -0.75], [-62.092544, 91.205868, -0.75], [-62.092544, 91.205868, 0.75], [-60.605702, 91.007623, 0.75], [-60.407456, 92.494464, 0.75]]}]},
			"L_shoulder_shaper_04_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_04_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[33.5, 93.600166, -3.75], [33.564526, 93.613487, -3.767924], [33.619228, 93.651424, -3.783119], [33.655781, 93.708197, -3.793272], [33.668616, 93.775166, -3.796838], [33.655781, 93.842135, -3.793272], [33.619228, 93.898909, -3.783119], [33.564526, 93.936845, -3.767924], [33.5, 93.950166, -3.75], [33.435474, 93.936845, -3.732076], [33.380772, 93.898909, -3.716881], [33.344219, 93.842135, -3.706728], [33.331384, 93.775166, -3.703162], [33.344219, 93.708197, -3.706728], [33.380772, 93.651424, -3.716881], [33.435474, 93.613487, -3.732076], [33.5, 93.600166, -3.75], [33.5, 91.850166, -3.75]]}]},
			"R_ankleOffset_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ankleOffset_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-10.118355, 2.77598, -0.054255], [-10.118355, 2.830235, -0.0], [-10.118355, 2.77598, 0.054255], [-10.118355, 2.721725, -0.0], [-10.118355, 2.77598, -0.054255], [-10.172605, 2.77598, -0.0], [-10.118355, 2.77598, 0.054255], [-10.0641, 2.77598, -0.0], [-10.118355, 2.830235, -0.0], [-10.172605, 2.77598, -0.0], [-10.118355, 2.721725, -0.0], [-10.0641, 2.77598, -0.0], [-10.118355, 2.77598, -0.054255], [-10.172605, 2.77598, -0.0], [-5.0, 2.77598, -0.0]]}, {"shapeName": "R_ankleOffset_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.0, 7.894335, -0.054255], [-4.945745, 7.894335, 0.0], [-5.0, 7.894335, 0.054255], [-5.054255, 7.894335, -0.0], [-5.0, 7.894335, -0.054255], [-5.0, 7.948585, -0.0], [-5.0, 7.894335, 0.054255], [-5.0, 7.84008, -0.0], [-4.945745, 7.894335, 0.0], [-5.0, 7.948585, -0.0], [-5.054255, 7.894335, -0.0], [-5.0, 7.84008, -0.0], [-5.0, 7.894335, -0.054255], [-5.0, 7.948585, -0.0], [-5.0, 2.77598, -0.0]]}, {"shapeName": "R_ankleOffset_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-5.0, 2.830235, 5.118355], [-4.945745, 2.77598, 5.118355], [-5.0, 2.721725, 5.118355], [-5.054255, 2.77598, 5.118355], [-5.0, 2.830235, 5.118355], [-5.0, 2.77598, 5.172605], [-5.0, 2.721725, 5.118355], [-5.0, 2.77598, 5.0641], [-4.945745, 2.77598, 5.118355], [-5.0, 2.77598, 5.172605], [-5.054255, 2.77598, 5.118355], [-5.0, 2.77598, 5.0641], [-5.0, 2.830235, 5.118355], [-5.0, 2.77598, 5.172605], [-5.0, 2.77598, -0.0]]}]},
			"R_leg_IK_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_CTLShape", "degree": 3, "form": 2, "points": [[-7.938545, 2.775979, -4.897575], [-5.0, 2.775979, -6.926213], [-2.061455, 2.775979, -4.897575], [-0.844273, 2.775979, 0.0], [-2.061455, 2.775979, 4.897575], [-5.0, 2.775979, 6.926213], [-7.938545, 2.775979, 4.897575], [-9.155727, 2.775979, 0.0]]}]},
			"L_clavicle_CTL": {"color": 6, "shapes": [{"shapeName": "L_clavicle_CTLShape", "degree": 3, "form": 0, "points": [[4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [2.831885, 91.850166, -4.136168], [0.537339, 91.850166, -10.828593], [-0.339102, 91.850166, -13.38488], [0.537339, 100.167156, -10.828593], [2.831885, 105.307346, -4.136168], [5.668115, 105.307346, 4.136168], [7.962661, 100.167156, 10.828593], [8.839102, 91.850166, 13.38488], [7.962661, 91.850166, 10.828593], [5.668115, 91.850166, 4.136168], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0], [4.25, 91.850166, 0.0]]}]},
			"R_elbow_shaper_03_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_elbow_shaper_03_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-47.485136, 91.850166, -2.221565], [-47.482075, 91.861017, -2.211155], [-47.479013, 91.850166, -2.200744], [-47.482075, 91.839315, -2.211155], [-47.485136, 91.850166, -2.221565], [-47.492484, 91.850166, -2.208093], [-47.479013, 91.850166, -2.200744], [-47.471665, 91.850166, -2.214216], [-47.482075, 91.861017, -2.211155], [-47.492484, 91.850166, -2.208093], [-47.482075, 91.839315, -2.211155], [-47.471665, 91.850166, -2.214216], [-47.485136, 91.850166, -2.221565], [-47.492484, 91.850166, -2.208093], [-46.5, 91.850166, -2.5]]}, {"shapeName": "R_elbow_shaper_03_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-46.503062, 92.873837, -2.51041], [-46.48959, 92.873837, -2.503062], [-46.496938, 92.873837, -2.48959], [-46.51041, 92.873837, -2.496938], [-46.503062, 92.873837, -2.51041], [-46.5, 92.884687, -2.5], [-46.496938, 92.873837, -2.48959], [-46.5, 92.862986, -2.5], [-46.48959, 92.873837, -2.503062], [-46.5, 92.884687, -2.5], [-46.51041, 92.873837, -2.496938], [-46.5, 92.862986, -2.5], [-46.503062, 92.873837, -2.51041], [-46.5, 92.884687, -2.5], [-46.5, 91.850166, -2.5]]}, {"shapeName": "R_elbow_shaper_03_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-46.211155, 91.861017, -1.517925], [-46.200744, 91.850166, -1.520987], [-46.211155, 91.839315, -1.517925], [-46.221565, 91.850166, -1.514864], [-46.211155, 91.861017, -1.517925], [-46.208093, 91.850166, -1.507516], [-46.211155, 91.839315, -1.517925], [-46.214216, 91.850166, -1.528335], [-46.200744, 91.850166, -1.520987], [-46.208093, 91.850166, -1.507516], [-46.221565, 91.850166, -1.514864], [-46.214216, 91.850166, -1.528335], [-46.211155, 91.861017, -1.517925], [-46.208093, 91.850166, -1.507516], [-46.5, 91.850166, -2.5]]}]},
			"C_head_left_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_left_PIV_CTLShape", "degree": 1, "form": 0, "points": [[15.118355, 111.850166, -5.054255], [15.118355, 111.904421, -5.0], [15.118355, 111.850166, -4.945745], [15.118355, 111.795911, -5.0], [15.118355, 111.850166, -5.054255], [15.172605, 111.850166, -5.0], [15.118355, 111.850166, -4.945745], [15.0641, 111.850166, -5.0], [15.118355, 111.904421, -5.0], [15.172605, 111.850166, -5.0], [15.118355, 111.795911, -5.0], [15.0641, 111.850166, -5.0], [15.118355, 111.850166, -5.054255], [15.172605, 111.850166, -5.0], [10.0, 111.850166, -5.0]]}, {"shapeName": "C_head_left_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[10.0, 116.968521, -5.054255], [9.945745, 116.968521, -5.0], [10.0, 116.968521, -4.945745], [10.054255, 116.968521, -5.0], [10.0, 116.968521, -5.054255], [10.0, 117.022771, -5.0], [10.0, 116.968521, -4.945745], [10.0, 116.914266, -5.0], [9.945745, 116.968521, -5.0], [10.0, 117.022771, -5.0], [10.054255, 116.968521, -5.0], [10.0, 116.914266, -5.0], [10.0, 116.968521, -5.054255], [10.0, 117.022771, -5.0], [10.0, 111.850166, -5.0]]}, {"shapeName": "C_head_left_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[10.0, 111.904421, 0.118355], [9.945745, 111.850166, 0.118355], [10.0, 111.795911, 0.118355], [10.054255, 111.850166, 0.118355], [10.0, 111.904421, 0.118355], [10.0, 111.850166, 0.172605], [10.0, 111.795911, 0.118355], [10.0, 111.850166, 0.0641], [9.945745, 111.850166, 0.118355], [10.0, 111.850166, 0.172605], [10.054255, 111.850166, 0.118355], [10.0, 111.850166, 0.0641], [10.0, 111.904421, 0.118355], [10.0, 111.850166, 0.172605], [10.0, 111.850166, -5.0]]}]},
			"L_elbow_shaper_03_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_elbow_shaper_03_PIV_CTLShape", "degree": 1, "form": 0, "points": [[47.485136, 91.850166, -2.221565], [47.482075, 91.861017, -2.211155], [47.479013, 91.850166, -2.200744], [47.482075, 91.839315, -2.211155], [47.485136, 91.850166, -2.221565], [47.492484, 91.850166, -2.208093], [47.479013, 91.850166, -2.200744], [47.471665, 91.850166, -2.214216], [47.482075, 91.861017, -2.211155], [47.492484, 91.850166, -2.208093], [47.482075, 91.839315, -2.211155], [47.471665, 91.850166, -2.214216], [47.485136, 91.850166, -2.221565], [47.492484, 91.850166, -2.208093], [46.5, 91.850166, -2.5]]}, {"shapeName": "L_elbow_shaper_03_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[46.503062, 92.873837, -2.51041], [46.48959, 92.873837, -2.503062], [46.496938, 92.873837, -2.48959], [46.51041, 92.873837, -2.496938], [46.503062, 92.873837, -2.51041], [46.5, 92.884687, -2.5], [46.496938, 92.873837, -2.48959], [46.5, 92.862986, -2.5], [46.48959, 92.873837, -2.503062], [46.5, 92.884687, -2.5], [46.51041, 92.873837, -2.496938], [46.5, 92.862986, -2.5], [46.503062, 92.873837, -2.51041], [46.5, 92.884687, -2.5], [46.5, 91.850166, -2.5]]}, {"shapeName": "L_elbow_shaper_03_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[46.211155, 91.861017, -1.517925], [46.200744, 91.850166, -1.520987], [46.211155, 91.839315, -1.517925], [46.221565, 91.850166, -1.514864], [46.211155, 91.861017, -1.517925], [46.208093, 91.850166, -1.507516], [46.211155, 91.839315, -1.517925], [46.214216, 91.850166, -1.528335], [46.200744, 91.850166, -1.520987], [46.208093, 91.850166, -1.507516], [46.221565, 91.850166, -1.514864], [46.214216, 91.850166, -1.528335], [46.211155, 91.861017, -1.517925], [46.208093, 91.850166, -1.507516], [46.5, 91.850166, -2.5]]}]},
			"C_chest_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_chest_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 81.968521, -0.054255], [-0.054255, 81.968521, 0.0], [0.0, 81.968521, 0.054255], [0.054255, 81.968521, 0.0], [0.0, 81.968521, -0.054255], [0.0, 82.022771, 0.0], [0.0, 81.968521, 0.054255], [0.0, 81.914266, 0.0], [-0.054255, 81.968521, 0.0], [0.0, 82.022771, 0.0], [0.054255, 81.968521, 0.0], [0.0, 81.914266, 0.0], [0.0, 81.968521, -0.054255], [0.0, 82.022771, 0.0], [0.0, 76.850166, 0.0]]}, {"shapeName": "C_chest_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 76.850166, -0.054255], [-5.118355, 76.795911, 0.0], [-5.118355, 76.850166, 0.054255], [-5.118355, 76.904421, 0.0], [-5.118355, 76.850166, -0.054255], [-5.172605, 76.850166, 0.0], [-5.118355, 76.850166, 0.054255], [-5.0641, 76.850166, 0.0], [-5.118355, 76.795911, 0.0], [-5.172605, 76.850166, 0.0], [-5.118355, 76.904421, 0.0], [-5.0641, 76.850166, 0.0], [-5.118355, 76.850166, -0.054255], [-5.172605, 76.850166, 0.0], [0.0, 76.850166, 0.0]]}, {"shapeName": "C_chest_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 76.850166, 5.118355], [0.0, 76.795911, 5.118355], [0.054255, 76.850166, 5.118355], [0.0, 76.904421, 5.118355], [-0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.172605], [0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.0641], [0.0, 76.795911, 5.118355], [0.0, 76.850166, 5.172605], [0.0, 76.904421, 5.118355], [0.0, 76.850166, 5.0641], [-0.054255, 76.850166, 5.118355], [0.0, 76.850166, 5.172605], [0.0, 76.850166, 0.0]]}]},
			"R_lwrArmRibbonMid_CTL": {"color": 17, "shapes": [{"shapeName": "R_lwrArmRibbonMid_CTLShape", "degree": 1, "form": 0, "points": [[-47.910832, 93.516836, -7.296828], [-47.910832, 94.516836, -7.296828], [-48.616247, 91.850166, -9.695241], [-47.910832, 89.183496, -7.296828], [-47.910832, 90.183496, -7.296828], [-46.970278, 90.183496, -4.098946], [-46.970278, 86.850166, -4.098946], [-47.252444, 86.850166, -5.058311], [-46.5, 84.350166, -2.5], [-45.747556, 86.850166, 0.058311], [-46.029722, 86.850166, -0.901054], [-46.029722, 90.183496, -0.901054], [-45.089168, 90.183496, 2.296828], [-45.089168, 89.183496, 2.296828], [-44.383753, 91.850166, 4.695241], [-45.089168, 94.516836, 2.296828], [-45.089168, 93.516836, 2.296828], [-46.029722, 93.516836, -0.901054], [-46.029722, 96.850166, -0.901054], [-45.747556, 96.850166, 0.058311], [-46.5, 99.350166, -2.5], [-47.252444, 96.850166, -5.058311], [-46.970278, 96.850166, -4.098946], [-46.970278, 93.516836, -4.098946], [-47.910832, 93.516836, -7.296828]]}]},
			"R_bendyLeg_B_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.333332, 24.284575, 4.499982], [-3.933332, 24.284575, 4.499982], [-5.0, 24.288873, 5.499972], [-6.066668, 24.284575, 4.499982], [-5.666668, 24.284575, 4.499982], [-5.666668, 24.278844, 3.166662], [-7.0, 24.278844, 3.166662], [-7.0, 24.280563, 3.566658], [-8.0, 24.275979, 2.5], [-7.0, 24.271395, 1.433342], [-7.0, 24.273114, 1.833338], [-5.666668, 24.273114, 1.833338], [-5.666668, 24.267383, 0.500018], [-6.066668, 24.267383, 0.500018], [-5.0, 24.263085, -0.499972], [-3.933332, 24.267383, 0.500018], [-4.333332, 24.267383, 0.500018], [-4.333332, 24.273114, 1.833338], [-3.0, 24.273114, 1.833338], [-3.0, 24.271395, 1.433342], [-2.0, 24.275979, 2.5], [-3.0, 24.280563, 3.566658], [-3.0, 24.278844, 3.166662], [-4.333332, 24.278844, 3.166662], [-4.333332, 24.284575, 4.499982]]}]},
			"L_upLeg_shaper_02_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_02_CTLShape", "degree": 1, "form": 0, "points": [[17.5, 37.609312, 0.833333], [17.59515, 37.039725, 0.904532], [17.866125, 36.556853, 0.964891], [18.27165, 36.234194, 1.005223], [18.75, 36.120895, 1.019385], [19.22835, 36.234194, 1.005223], [19.633875, 36.556853, 0.964891], [19.90485, 37.039725, 0.904532], [20.0, 37.609312, 0.833333], [19.90485, 38.1789, 0.762135], [19.633875, 38.661772, 0.701776], [19.22835, 38.984431, 0.661444], [18.75, 39.097729, 0.647281], [18.27165, 38.984431, 0.661444], [17.866125, 38.661772, 0.701776], [17.59515, 38.1789, 0.762135], [17.5, 37.609312, 0.833333], [5.0, 37.609312, 0.833333]]}]},
			"R_toe_IK_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-6.567224, 1.843203, 5.0], [-5.0, 2.492367, 5.0], [-3.432776, 1.843203, 5.0], [-2.783612, 0.275979, 5.0], [-3.432776, -1.291245, 5.0], [-5.0, -1.940409, 5.0], [-6.567224, -1.291245, 5.0], [-7.216388, 0.275979, 5.0]]}]},
			"L_shoulder_shaper_03_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_shoulder_shaper_03_PIV_CTLShape", "degree": 1, "form": 0, "points": [[29.983421, 91.850166, -2.784434], [29.986325, 91.861017, -2.773979], [29.98923, 91.850166, -2.763524], [29.986325, 91.839315, -2.773979], [29.983421, 91.850166, -2.784434], [29.99678, 91.850166, -2.776883], [29.98923, 91.850166, -2.763524], [29.97587, 91.850166, -2.771075], [29.986325, 91.861017, -2.773979], [29.99678, 91.850166, -2.776883], [29.986325, 91.839315, -2.773979], [29.97587, 91.850166, -2.771075], [29.983421, 91.850166, -2.784434], [29.99678, 91.850166, -2.776883], [29.0, 91.850166, -2.5]]}, {"shapeName": "L_shoulder_shaper_03_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[28.997096, 92.873837, -2.510455], [28.989545, 92.873837, -2.497096], [29.002904, 92.873837, -2.489545], [29.010455, 92.873837, -2.502904], [28.997096, 92.873837, -2.510455], [29.0, 92.884687, -2.5], [29.002904, 92.873837, -2.489545], [29.0, 92.862986, -2.5], [28.989545, 92.873837, -2.497096], [29.0, 92.884687, -2.5], [29.010455, 92.873837, -2.502904], [29.0, 92.862986, -2.5], [28.997096, 92.873837, -2.510455], [29.0, 92.884687, -2.5], [29.0, 91.850166, -2.5]]}, {"shapeName": "L_shoulder_shaper_03_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[29.273979, 91.861017, -1.513675], [29.263524, 91.850166, -1.51077], [29.273979, 91.839315, -1.513675], [29.284434, 91.850166, -1.516579], [29.273979, 91.861017, -1.513675], [29.276883, 91.850166, -1.50322], [29.273979, 91.839315, -1.513675], [29.271075, 91.850166, -1.52413], [29.263524, 91.850166, -1.51077], [29.276883, 91.850166, -1.50322], [29.284434, 91.850166, -1.516579], [29.271075, 91.850166, -1.52413], [29.273979, 91.861017, -1.513675], [29.276883, 91.850166, -1.50322], [29.0, 91.850166, -2.5]]}]},
			"R_loLeg_shaper_05_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_05_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-12.5, 6.359312, 0.416667], [-12.55709, 6.017205, 0.376887], [-12.719675, 5.727181, 0.343163], [-12.96299, 5.533385, 0.320629], [-13.25, 5.465336, 0.312716], [-13.53701, 5.533385, 0.320629], [-13.780325, 5.727181, 0.343163], [-13.94291, 6.017205, 0.376887], [-14.0, 6.359312, 0.416667], [-13.94291, 6.701419, 0.456447], [-13.780325, 6.991443, 0.49017], [-13.53701, 7.18524, 0.512705], [-13.25, 7.253289, 0.520617], [-12.96299, 7.18524, 0.512705], [-12.719675, 6.991443, 0.49017], [-12.55709, 6.701419, 0.456447], [-12.5, 6.359312, 0.416667], [-5.0, 6.359312, 0.416667]]}]},
			"R_leg_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 29.394355, -47.554255], [-4.945745, 29.394355, -47.5], [-5.0, 29.394355, -47.445745], [-5.054255, 29.394355, -47.5], [-5.0, 29.394355, -47.554255], [-5.0, 29.448605, -47.5], [-5.0, 29.394355, -47.445745], [-5.0, 29.3401, -47.5], [-4.945745, 29.394355, -47.5], [-5.0, 29.448605, -47.5], [-5.054255, 29.394355, -47.5], [-5.0, 29.3401, -47.5], [-5.0, 29.394355, -47.554255], [-5.0, 29.448605, -47.5], [-5.0, 24.276, -47.5]]}, {"shapeName": "R_leg_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 24.276, -47.554255], [0.118355, 24.221745, -47.5], [0.118355, 24.276, -47.445745], [0.118355, 24.330255, -47.5], [0.118355, 24.276, -47.554255], [0.172605, 24.276, -47.5], [0.118355, 24.276, -47.445745], [0.0641, 24.276, -47.5], [0.118355, 24.221745, -47.5], [0.172605, 24.276, -47.5], [0.118355, 24.330255, -47.5], [0.0641, 24.276, -47.5], [0.118355, 24.276, -47.554255], [0.172605, 24.276, -47.5], [-5.0, 24.276, -47.5]]}, {"shapeName": "R_leg_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 24.276, -42.381645], [-5.0, 24.221745, -42.381645], [-5.054255, 24.276, -42.381645], [-5.0, 24.330255, -42.381645], [-4.945745, 24.276, -42.381645], [-5.0, 24.276, -42.327395], [-5.054255, 24.276, -42.381645], [-5.0, 24.276, -42.4359], [-5.0, 24.221745, -42.381645], [-5.0, 24.276, -42.327395], [-5.0, 24.330255, -42.381645], [-5.0, 24.276, -42.4359], [-4.945745, 24.276, -42.381645], [-5.0, 24.276, -42.327395], [-5.0, 24.276, -47.5]]}]},
			"R_loLeg_shaper_01_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_01_CTLShape", "degree": 1, "form": 0, "points": [[-17.5, 20.692646, 2.083333], [-17.59515, 20.122467, 2.017034], [-17.866125, 19.639094, 1.960827], [-18.27165, 19.3161, 1.92327], [-18.75, 19.202685, 1.910082], [-19.22835, 19.3161, 1.92327], [-19.633875, 19.639094, 1.960827], [-19.90485, 20.122467, 2.017034], [-20.0, 20.692646, 2.083333], [-19.90485, 21.262824, 2.149633], [-19.633875, 21.746197, 2.205839], [-19.22835, 22.069191, 2.243397], [-18.75, 22.182607, 2.256585], [-18.27165, 22.069191, 2.243397], [-17.866125, 21.746197, 2.205839], [-17.59515, 21.262824, 2.149633], [-17.5, 20.692646, 2.083333], [-5.0, 20.692646, 2.083333]]}]},
			"C_neck_FK_D_CTL": {"color": 4, "shapes": [{"shapeName": "C_neck_FK_D_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 101.850166, 0.0], [-5.03806, 102.041506, 0.0], [-5.14645, 102.203716, 0.0], [-5.30866, 102.312106, 0.0], [-5.5, 102.350166, 0.0], [-5.69134, 102.312106, 0.0], [-5.85355, 102.203716, 0.0], [-5.96194, 102.041506, 0.0], [-6.0, 101.850166, 0.0], [-5.96194, 101.658826, 0.0], [-5.85355, 101.496616, 0.0], [-5.69134, 101.388226, 0.0], [-5.5, 101.350166, 0.0], [-5.30866, 101.388226, 0.0], [-5.14645, 101.496616, 0.0], [-5.03806, 101.658826, 0.0], [-5.0, 101.850166, 0.0], [0.0, 101.850166, 0.0]]}]},
			"L_loLeg_shaper_02_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_02_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[12.5, 17.109312, 1.666667], [12.55709, 16.767205, 1.626887], [12.719675, 16.477181, 1.593163], [12.96299, 16.283385, 1.570629], [13.25, 16.215336, 1.562716], [13.53701, 16.283385, 1.570629], [13.780325, 16.477181, 1.593163], [13.94291, 16.767205, 1.626887], [14.0, 17.109312, 1.666667], [13.94291, 17.451419, 1.706447], [13.780325, 17.741443, 1.74017], [13.53701, 17.935239, 1.762705], [13.25, 18.003289, 1.770617], [12.96299, 17.935239, 1.762705], [12.719675, 17.741443, 1.74017], [12.55709, 17.451419, 1.706447], [12.5, 17.109312, 1.666667], [5.0, 17.109312, 1.666667]]}]},
			"L_upLeg_shaper_02_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_02_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[13.75, 37.609312, 0.833333], [13.816605, 37.210601, 0.883172], [14.006287, 36.872591, 0.925424], [14.290155, 36.646729, 0.953656], [14.625, 36.567421, 0.96357], [14.959845, 36.646729, 0.953656], [15.243712, 36.872591, 0.925424], [15.433395, 37.210601, 0.883172], [15.5, 37.609312, 0.833333], [15.433395, 38.008023, 0.783494], [15.243712, 38.346034, 0.741243], [14.959845, 38.571895, 0.71301], [14.625, 38.651204, 0.703097], [14.290155, 38.571895, 0.71301], [14.006287, 38.346034, 0.741243], [13.816605, 38.008023, 0.783494], [13.75, 37.609312, 0.833333], [5.0, 37.609312, 0.833333]]}]},
			"C_revSpine_chest_CTL": {"color": 4, "shapes": [{"shapeName": "C_revSpine_chest_CTLShape", "degree": 3, "form": 2, "points": [[5.87709, 76.850166, 5.87709], [8.311455, 76.850166, 0.0], [6e-05, 76.850166, -5.87709], [0.0, 76.850166, -8.311455], [-6e-05, 76.850166, -5.87709], [-8.311455, 76.850166, 0.0], [-5.87709, 76.850166, 5.87709], [0.0, 76.850166, 8.311455]]}]},
			"L_arm_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[35.0, 101.850166, 0.499763], [35.0, 101.850166, -0.499763], [35.0, 101.850166, 0.0], [34.500237, 101.850166, 0.0], [35.499763, 101.850166, 0.0], [35.0, 101.850166, 0.0], [35.0, 102.349929, 0.0], [35.0, 101.350403, 0.0]]}]},
			"C_cog_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-9.0, 49.350166, -9.0], [-9.0, 49.350166, 9.0], [9.0, 49.350166, 9.0], [9.0, 49.350166, -9.0], [-9.0, 49.350166, -9.0]]}]},
			"L_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_B_CTLShape", "degree": 1, "form": 0, "points": [[63.812803, 92.907587, -1.75], [62.31758, 92.787969, -1.75], [62.31758, 92.787969, -3.25], [63.812803, 92.907587, -3.25], [63.93242, 91.412364, -3.25], [62.437197, 91.292746, -3.25], [62.437197, 91.292746, -1.75], [63.93242, 91.412364, -1.75], [63.812803, 92.907587, -1.75], [63.812803, 92.907587, -3.25], [62.31758, 92.787969, -3.25], [62.437197, 91.292746, -3.25], [63.93242, 91.412364, -3.25], [63.93242, 91.412364, -1.75], [62.437197, 91.292746, -1.75], [62.31758, 92.787969, -1.75]]}]},
			"R_loLeg_shaper_04_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_loLeg_shaper_04_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 4.852279, 0.296051], [-4.945745, 4.858546, 0.242159], [-5.0, 4.864812, 0.188267], [-5.054255, 4.858546, 0.242159], [-5.0, 4.852279, 0.296051], [-5.0, 4.804659, 0.235893], [-5.0, 4.864812, 0.188267], [-5.0, 4.912438, 0.248425], [-4.945745, 4.858546, 0.242159], [-5.0, 4.804659, 0.235893], [-5.054255, 4.858546, 0.242159], [-5.0, 4.912438, 0.248425], [-5.0, 4.852279, 0.296051], [-5.0, 4.804659, 0.235893], [-5.0, 9.942646, 0.833333]]}, {"shapeName": "R_loLeg_shaper_04_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 9.936379, 0.887225], [0.118355, 9.996538, 0.8396], [0.118355, 9.948912, 0.779441], [0.118355, 9.888754, 0.827067], [0.118355, 9.936379, 0.887225], [0.172605, 9.942646, 0.833333], [0.118355, 9.948912, 0.779441], [0.0641, 9.942646, 0.833333], [0.118355, 9.996538, 0.8396], [0.172605, 9.942646, 0.833333], [0.118355, 9.888754, 0.827067], [0.0641, 9.942646, 0.833333], [0.118355, 9.936379, 0.887225], [0.172605, 9.942646, 0.833333], [-5.0, 9.942646, 0.833333]]}, {"shapeName": "R_loLeg_shaper_04_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 10.53382, -4.250766], [-5.0, 10.587712, -4.2445], [-5.054255, 10.53382, -4.250766], [-5.0, 10.479928, -4.257033], [-4.945745, 10.53382, -4.250766], [-5.0, 10.540086, -4.304653], [-5.054255, 10.53382, -4.250766], [-5.0, 10.527554, -4.196875], [-5.0, 10.587712, -4.2445], [-5.0, 10.540086, -4.304653], [-5.0, 10.479928, -4.257033], [-5.0, 10.527554, -4.196875], [-4.945745, 10.53382, -4.250766], [-5.0, 10.540086, -4.304653], [-5.0, 9.942646, 0.833333]]}]},
			"C_spineShaper_1_CTL": {"color": 4, "shapes": [{"shapeName": "C_spineShaper_1_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 51.870166, -7.5], [0.0, 52.157176, -7.55709], [0.0, 52.400491, -7.719675], [0.0, 52.563076, -7.96299], [0.0, 52.620166, -8.25], [0.0, 52.563076, -8.53701], [0.0, 52.400491, -8.780325], [0.0, 52.157176, -8.94291], [0.0, 51.870166, -9.0], [0.0, 51.583156, -8.94291], [0.0, 51.339841, -8.780325], [0.0, 51.177256, -8.53701], [0.0, 51.120166, -8.25], [0.0, 51.177256, -7.96299], [0.0, 51.339841, -7.719675], [0.0, 51.583156, -7.55709], [0.0, 51.870166, -7.5], [0.0, 51.870166, 0.0]]}]},
			"L_handIk_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_handIk_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[55.0, 88.715718, -3.134448], [55.0, 91.850166, -4.432776], [55.0, 94.984614, -3.134448], [55.0, 96.282942, 0.0], [55.0, 94.984614, 3.134448], [55.0, 91.850166, 4.432776], [55.0, 88.715718, 3.134448], [55.0, 87.41739, 0.0]]}]},
			"R_elbow_shaper_04_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_04_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-50.75, 93.850166, -1.25], [-50.823426, 93.86539, -1.228404], [-50.885673, 93.908746, -1.210096], [-50.927268, 93.97363, -1.197862], [-50.941873, 94.050166, -1.193567], [-50.927268, 94.126702, -1.197862], [-50.885673, 94.191586, -1.210096], [-50.823426, 94.234942, -1.228404], [-50.75, 94.250166, -1.25], [-50.676574, 94.234942, -1.271596], [-50.614327, 94.191586, -1.289904], [-50.572732, 94.126702, -1.302138], [-50.558127, 94.050166, -1.306433], [-50.572732, 93.97363, -1.302138], [-50.614327, 93.908746, -1.289904], [-50.676574, 93.86539, -1.271596], [-50.75, 93.850166, -1.25], [-50.75, 91.850166, -1.25]]}]},
			"R_elbow_shaper_05_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_05_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-54.15, 94.100166, -0.25], [-54.232604, 94.117293, -0.225705], [-54.302633, 94.166069, -0.205108], [-54.349426, 94.239063, -0.191345], [-54.365857, 94.325166, -0.186513], [-54.349426, 94.411269, -0.191345], [-54.302633, 94.484264, -0.205108], [-54.232604, 94.533039, -0.225705], [-54.15, 94.550166, -0.25], [-54.067396, 94.533039, -0.274295], [-53.997367, 94.484264, -0.294892], [-53.950574, 94.411269, -0.308655], [-53.934143, 94.325166, -0.313487], [-53.950574, 94.239063, -0.308655], [-53.997367, 94.166069, -0.294892], [-54.067396, 94.117293, -0.274295], [-54.15, 94.100166, -0.25], [-54.15, 91.850166, -0.25]]}]},
			"L_handIk_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_handIk_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[55.0, 89.49933, -2.350836], [55.0, 91.850166, -3.324582], [55.0, 94.201002, -2.350836], [55.0, 95.174748, 0.0], [55.0, 94.201002, 2.350836], [55.0, 91.850166, 3.324582], [55.0, 89.49933, 2.350836], [55.0, 88.525584, 0.0]]}]},
			"L_lwrArmTwist_CTL": {"color": 6, "shapes": [{"shapeName": "L_lwrArmTwist_CTLShape", "degree": 1, "form": 0, "points": [[54.920676, 86.037787, -4.708972], [54.920676, 84.005068, -6.161677], [54.920676, 85.795373, -8.049093], [54.920676, 88.019393, -9.415424], [54.920676, 90.513734, -10.166319], [54.920676, 93.116827, -10.263696], [54.920676, 95.654401, -9.678556], [54.920676, 97.946765, -8.481737], [54.920676, 99.834181, -6.691432], [54.920676, 101.200513, -4.467412], [54.920676, 101.951407, -1.973071], [54.920676, 102.048785, 0.630022], [54.920676, 101.463645, 3.167596], [54.920676, 100.266826, 5.45996], [54.920676, 98.476521, 7.347376], [54.920676, 96.2525, 8.713708], [54.920676, 93.75816, 9.464602], [54.920676, 91.155067, 9.56198], [54.920676, 88.617492, 8.97684], [54.920676, 86.325128, 7.780021], [54.920676, 84.790709, 9.927081], [54.920676, 80.681106, 2.115039], [54.920676, 89.375808, 3.511309], [54.920676, 87.777833, 5.747301], [54.920676, 89.494836, 6.648091], [54.920676, 91.391665, 7.082407], [54.920676, 93.352149, 7.024805], [54.920676, 95.225632, 6.44439], [54.920676, 96.892283, 5.428264], [54.920676, 98.234106, 4.007256], [54.920676, 99.134896, 2.290252], [54.920676, 99.569212, 0.393424], [54.920676, 99.51161, -1.567061], [54.920676, 98.931195, -3.440543], [54.920676, 97.915069, -5.107195], [54.920676, 96.494061, -6.449018], [54.920676, 94.777057, -7.349808], [54.920676, 92.880229, -7.784123], [54.920676, 90.919744, -7.726522], [54.920676, 89.046262, -7.146107], [54.920676, 87.37961, -6.12998], [54.920676, 86.037787, -4.708972]]}]},
			"R_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_B_CTLShape", "degree": 1, "form": 0, "points": [[-63.812803, 92.907587, 2.0], [-62.31758, 92.787969, 2.0], [-62.31758, 92.787969, 0.5], [-63.812803, 92.907587, 0.5], [-63.93242, 91.412364, 0.5], [-62.437197, 91.292746, 0.5], [-62.437197, 91.292746, 2.0], [-63.93242, 91.412364, 2.0], [-63.812803, 92.907587, 2.0], [-63.812803, 92.907587, 0.5], [-62.31758, 92.787969, 0.5], [-62.437197, 91.292746, 0.5], [-63.93242, 91.412364, 0.5], [-63.93242, 91.412364, 2.0], [-62.437197, 91.292746, 2.0], [-62.31758, 92.787969, 2.0]]}]},
			"R_innerBall_CTL": {"color": 20, "shapes": [{"shapeName": "R_innerBall_CTLShape", "degree": 1, "form": 0, "points": [[-1.5, 0.275979, 5.5], [-1.5, -0.224021, 5.0], [-2.0, 0.275979, 5.0], [-1.5, 0.275979, 5.5], [-1.0, 0.275979, 5.0], [-1.5, -0.224021, 5.0], [-1.5, 0.275979, 4.5], [-1.0, 0.275979, 5.0], [-1.5, 0.775979, 5.0], [-1.5, 0.275979, 5.5], [-2.0, 0.275979, 5.0], [-1.5, 0.275979, 4.5], [-1.5, 0.775979, 5.0], [-2.0, 0.275979, 5.0]]}]},
			"R_clavicle_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_clavicle_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-2.973697, 91.850166, -3.722551], [-0.908606, 91.850166, -9.745734], [-0.119809, 91.850166, -12.046392], [-0.908606, 99.335457, -9.745734], [-2.973697, 103.961628, -3.722551], [-5.526303, 103.961628, 3.722551], [-7.591394, 99.335457, 9.745734], [-8.380191, 91.850166, 12.046392], [-7.591394, 91.850166, 9.745734], [-5.526303, 91.850166, 3.722551], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0], [-4.25, 91.850166, -0.0]]}]},
			"R_shoulder_shaper_05_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_shaper_05_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-38.083421, 91.850166, -5.034434], [-38.086325, 91.861017, -5.023979], [-38.08923, 91.850166, -5.013524], [-38.086325, 91.839315, -5.023979], [-38.083421, 91.850166, -5.034434], [-38.09678, 91.850166, -5.026883], [-38.08923, 91.850166, -5.013524], [-38.07587, 91.850166, -5.021075], [-38.086325, 91.861017, -5.023979], [-38.09678, 91.850166, -5.026883], [-38.086325, 91.839315, -5.023979], [-38.07587, 91.850166, -5.021075], [-38.083421, 91.850166, -5.034434], [-38.09678, 91.850166, -5.026883], [-37.1, 91.850166, -4.75]]}, {"shapeName": "R_shoulder_shaper_05_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-37.097096, 92.873837, -4.760455], [-37.089545, 92.873837, -4.747096], [-37.102904, 92.873837, -4.739545], [-37.110455, 92.873837, -4.752904], [-37.097096, 92.873837, -4.760455], [-37.1, 92.884687, -4.75], [-37.102904, 92.873837, -4.739545], [-37.1, 92.862986, -4.75], [-37.089545, 92.873837, -4.747096], [-37.1, 92.884687, -4.75], [-37.110455, 92.873837, -4.752904], [-37.1, 92.862986, -4.75], [-37.097096, 92.873837, -4.760455], [-37.1, 92.884687, -4.75], [-37.1, 91.850166, -4.75]]}, {"shapeName": "R_shoulder_shaper_05_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-37.373979, 91.861017, -3.763675], [-37.363524, 91.850166, -3.76077], [-37.373979, 91.839315, -3.763675], [-37.384434, 91.850166, -3.766579], [-37.373979, 91.861017, -3.763675], [-37.376883, 91.850166, -3.75322], [-37.373979, 91.839315, -3.763675], [-37.371075, 91.850166, -3.77413], [-37.363524, 91.850166, -3.76077], [-37.376883, 91.850166, -3.75322], [-37.384434, 91.850166, -3.766579], [-37.371075, 91.850166, -3.77413], [-37.373979, 91.861017, -3.763675], [-37.376883, 91.850166, -3.75322], [-37.1, 91.850166, -4.75]]}]},
			"L_elbow_shaper_02_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_elbow_shaper_02_PIV_CTLShape", "degree": 1, "form": 0, "points": [[43.235136, 91.850166, -3.471565], [43.232075, 91.861017, -3.461155], [43.229013, 91.850166, -3.450744], [43.232075, 91.839315, -3.461155], [43.235136, 91.850166, -3.471565], [43.242484, 91.850166, -3.458093], [43.229013, 91.850166, -3.450744], [43.221665, 91.850166, -3.464216], [43.232075, 91.861017, -3.461155], [43.242484, 91.850166, -3.458093], [43.232075, 91.839315, -3.461155], [43.221665, 91.850166, -3.464216], [43.235136, 91.850166, -3.471565], [43.242484, 91.850166, -3.458093], [42.25, 91.850166, -3.75]]}, {"shapeName": "L_elbow_shaper_02_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[42.253062, 92.873837, -3.76041], [42.23959, 92.873837, -3.753062], [42.246938, 92.873837, -3.73959], [42.26041, 92.873837, -3.746938], [42.253062, 92.873837, -3.76041], [42.25, 92.884687, -3.75], [42.246938, 92.873837, -3.73959], [42.25, 92.862986, -3.75], [42.23959, 92.873837, -3.753062], [42.25, 92.884687, -3.75], [42.26041, 92.873837, -3.746938], [42.25, 92.862986, -3.75], [42.253062, 92.873837, -3.76041], [42.25, 92.884687, -3.75], [42.25, 91.850166, -3.75]]}, {"shapeName": "L_elbow_shaper_02_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[41.961155, 91.861017, -2.767925], [41.950744, 91.850166, -2.770987], [41.961155, 91.839315, -2.767925], [41.971565, 91.850166, -2.764864], [41.961155, 91.861017, -2.767925], [41.958093, 91.850166, -2.757516], [41.961155, 91.839315, -2.767925], [41.964216, 91.850166, -2.778335], [41.950744, 91.850166, -2.770987], [41.958093, 91.850166, -2.757516], [41.971565, 91.850166, -2.764864], [41.964216, 91.850166, -2.778335], [41.961155, 91.861017, -2.767925], [41.958093, 91.850166, -2.757516], [42.25, 91.850166, -3.75]]}]},
			"R_toeTip_CTL": {"color": 20, "shapes": [{"shapeName": "R_toeTip_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 0.275979, 11.5], [-5.0, -0.224021, 11.0], [-5.5, 0.275979, 11.0], [-5.0, 0.275979, 11.5], [-4.5, 0.275979, 11.0], [-5.0, -0.224021, 11.0], [-5.0, 0.275979, 10.5], [-4.5, 0.275979, 11.0], [-5.0, 0.775979, 11.0], [-5.0, 0.275979, 11.5], [-5.5, 0.275979, 11.0], [-5.0, 0.275979, 10.5], [-5.0, 0.775979, 11.0], [-5.5, 0.275979, 11.0]]}]},
			"R_loLeg_shaper_05_CTL": {"color": 4, "shapes": [{"shapeName": "R_loLeg_shaper_05_CTLShape", "degree": 1, "form": 0, "points": [[-17.5, 6.359312, 0.416667], [-17.59515, 5.789134, 0.350367], [-17.866125, 5.305761, 0.294161], [-18.27165, 4.982767, 0.256603], [-18.75, 4.869351, 0.243415], [-19.22835, 4.982767, 0.256603], [-19.633875, 5.305761, 0.294161], [-19.90485, 5.789134, 0.350367], [-20.0, 6.359312, 0.416667], [-19.90485, 6.929491, 0.482966], [-19.633875, 7.412864, 0.539173], [-19.22835, 7.735858, 0.57673], [-18.75, 7.849273, 0.589918], [-18.27165, 7.735858, 0.57673], [-17.866125, 7.412864, 0.539173], [-17.59515, 6.929491, 0.482966], [-17.5, 6.359312, 0.416667], [-5.0, 6.359312, 0.416667]]}]},
			"R_shoulder_shaper_01_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_shaper_01_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-21.883421, 91.850166, -0.534434], [-21.886325, 91.861017, -0.523979], [-21.88923, 91.850166, -0.513524], [-21.886325, 91.839315, -0.523979], [-21.883421, 91.850166, -0.534434], [-21.89678, 91.850166, -0.526883], [-21.88923, 91.850166, -0.513524], [-21.87587, 91.850166, -0.521075], [-21.886325, 91.861017, -0.523979], [-21.89678, 91.850166, -0.526883], [-21.886325, 91.839315, -0.523979], [-21.87587, 91.850166, -0.521075], [-21.883421, 91.850166, -0.534434], [-21.89678, 91.850166, -0.526883], [-20.9, 91.850166, -0.25]]}, {"shapeName": "R_shoulder_shaper_01_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-20.897096, 92.873837, -0.260455], [-20.889545, 92.873837, -0.247096], [-20.902904, 92.873837, -0.239545], [-20.910455, 92.873837, -0.252904], [-20.897096, 92.873837, -0.260455], [-20.9, 92.884687, -0.25], [-20.902904, 92.873837, -0.239545], [-20.9, 92.862986, -0.25], [-20.889545, 92.873837, -0.247096], [-20.9, 92.884687, -0.25], [-20.910455, 92.873837, -0.252904], [-20.9, 92.862986, -0.25], [-20.897096, 92.873837, -0.260455], [-20.9, 92.884687, -0.25], [-20.9, 91.850166, -0.25]]}, {"shapeName": "R_shoulder_shaper_01_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-21.173979, 91.861017, 0.736325], [-21.163524, 91.850166, 0.73923], [-21.173979, 91.839315, 0.736325], [-21.184434, 91.850166, 0.733421], [-21.173979, 91.861017, 0.736325], [-21.176883, 91.850166, 0.74678], [-21.173979, 91.839315, 0.736325], [-21.171075, 91.850166, 0.72587], [-21.163524, 91.850166, 0.73923], [-21.176883, 91.850166, 0.74678], [-21.184434, 91.850166, 0.733421], [-21.171075, 91.850166, 0.72587], [-21.173979, 91.861017, 0.736325], [-21.176883, 91.850166, 0.74678], [-20.9, 91.850166, -0.25]]}]},
			"L_ankleOffset_CTL": {"color": 20, "shapes": [{"shapeName": "L_ankleOffset_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 1.519363, -0.558159], [5.0, 4.28446, 1.669426], [5.0, 4.990662, 1.705192], [5.5, 4.619678, 2.04041], [5.0, 4.954896, 2.411394], [5.0, 4.990662, 1.705192], [4.5, 4.619678, 2.04041], [5.0, 4.28446, 1.669426], [5.0, 4.248695, 2.375628], [4.5, 4.619678, 2.04041], [5.0, 4.954896, 2.411394], [5.0, 4.248695, 2.375628], [5.5, 4.619678, 2.04041], [5.0, 4.28446, 1.669426]]}]},
			"C_revSpine_1_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_revSpine_1_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 64.350166, -0.054255], [5.118355, 64.404421, 0.0], [5.118355, 64.350166, 0.054255], [5.118355, 64.295911, 0.0], [5.118355, 64.350166, -0.054255], [5.172605, 64.350166, 0.0], [5.118355, 64.350166, 0.054255], [5.0641, 64.350166, 0.0], [5.118355, 64.404421, 0.0], [5.172605, 64.350166, 0.0], [5.118355, 64.295911, 0.0], [5.0641, 64.350166, 0.0], [5.118355, 64.350166, -0.054255], [5.172605, 64.350166, 0.0], [0.0, 64.350166, 0.0]]}, {"shapeName": "C_revSpine_1_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 69.468521, -0.054255], [-0.054255, 69.468521, 0.0], [0.0, 69.468521, 0.054255], [0.054255, 69.468521, 0.0], [0.0, 69.468521, -0.054255], [0.0, 69.522771, 0.0], [0.0, 69.468521, 0.054255], [0.0, 69.414266, 0.0], [-0.054255, 69.468521, 0.0], [0.0, 69.522771, 0.0], [0.054255, 69.468521, 0.0], [0.0, 69.414266, 0.0], [0.0, 69.468521, -0.054255], [0.0, 69.522771, 0.0], [0.0, 64.350166, 0.0]]}, {"shapeName": "C_revSpine_1_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 64.404421, 5.118355], [-0.054255, 64.350166, 5.118355], [0.0, 64.295911, 5.118355], [0.054255, 64.350166, 5.118355], [0.0, 64.404421, 5.118355], [0.0, 64.350166, 5.172605], [0.0, 64.295911, 5.118355], [0.0, 64.350166, 5.0641], [-0.054255, 64.350166, 5.118355], [0.0, 64.350166, 5.172605], [0.054255, 64.350166, 5.118355], [0.0, 64.350166, 5.0641], [0.0, 64.404421, 5.118355], [0.0, 64.350166, 5.172605], [0.0, 64.350166, 0.0]]}]},
			"L_elbow_shaper_01_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_elbow_shaper_01_PIV_CTLShape", "degree": 1, "form": 0, "points": [[39.835136, 91.850166, -4.471565], [39.832075, 91.861017, -4.461155], [39.829013, 91.850166, -4.450744], [39.832075, 91.839315, -4.461155], [39.835136, 91.850166, -4.471565], [39.842484, 91.850166, -4.458093], [39.829013, 91.850166, -4.450744], [39.821665, 91.850166, -4.464216], [39.832075, 91.861017, -4.461155], [39.842484, 91.850166, -4.458093], [39.832075, 91.839315, -4.461155], [39.821665, 91.850166, -4.464216], [39.835136, 91.850166, -4.471565], [39.842484, 91.850166, -4.458093], [38.85, 91.850166, -4.75]]}, {"shapeName": "L_elbow_shaper_01_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[38.853062, 92.873837, -4.76041], [38.83959, 92.873837, -4.753062], [38.846938, 92.873837, -4.73959], [38.86041, 92.873837, -4.746938], [38.853062, 92.873837, -4.76041], [38.85, 92.884687, -4.75], [38.846938, 92.873837, -4.73959], [38.85, 92.862986, -4.75], [38.83959, 92.873837, -4.753062], [38.85, 92.884687, -4.75], [38.86041, 92.873837, -4.746938], [38.85, 92.862986, -4.75], [38.853062, 92.873837, -4.76041], [38.85, 92.884687, -4.75], [38.85, 91.850166, -4.75]]}, {"shapeName": "L_elbow_shaper_01_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[38.561155, 91.861017, -3.767925], [38.550744, 91.850166, -3.770987], [38.561155, 91.839315, -3.767925], [38.571565, 91.850166, -3.764864], [38.561155, 91.861017, -3.767925], [38.558093, 91.850166, -3.757516], [38.561155, 91.839315, -3.767925], [38.564216, 91.850166, -3.778335], [38.550744, 91.850166, -3.770987], [38.558093, 91.850166, -3.757516], [38.571565, 91.850166, -3.764864], [38.564216, 91.850166, -3.778335], [38.561155, 91.861017, -3.767925], [38.558093, 91.850166, -3.757516], [38.85, 91.850166, -4.75]]}]},
			"L_leg_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, -2.314387, -0.537283], [4.945745, -2.308121, -0.591174], [5.0, -2.301854, -0.645066], [5.054255, -2.308121, -0.591174], [5.0, -2.314387, -0.537283], [5.0, -2.362008, -0.59744], [5.0, -2.301854, -0.645066], [5.0, -2.254229, -0.584908], [4.945745, -2.308121, -0.591174], [5.0, -2.362008, -0.59744], [5.054255, -2.308121, -0.591174], [5.0, -2.254229, -0.584908], [5.0, -2.314387, -0.537283], [5.0, -2.362008, -0.59744], [5.0, 2.775979, 0.0]]}, {"shapeName": "L_leg_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 2.769713, 0.053892], [-0.118355, 2.829871, 0.006266], [-0.118355, 2.782246, -0.053892], [-0.118355, 2.722087, -0.006266], [-0.118355, 2.769713, 0.053892], [-0.172605, 2.775979, 0.0], [-0.118355, 2.782246, -0.053892], [-0.0641, 2.775979, 0.0], [-0.118355, 2.829871, 0.006266], [-0.172605, 2.775979, 0.0], [-0.118355, 2.722087, -0.006266], [-0.0641, 2.775979, 0.0], [-0.118355, 2.769713, 0.053892], [-0.172605, 2.775979, 0.0], [5.0, 2.775979, 0.0]]}, {"shapeName": "L_leg_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 3.367153, -5.0841], [5.0, 3.421045, -5.077833], [5.054255, 3.367153, -5.0841], [5.0, 3.313262, -5.090366], [4.945745, 3.367153, -5.0841], [5.0, 3.373419, -5.137987], [5.054255, 3.367153, -5.0841], [5.0, 3.360887, -5.030208], [5.0, 3.421045, -5.077833], [5.0, 3.373419, -5.137987], [5.0, 3.313262, -5.090366], [5.0, 3.360887, -5.030208], [4.945745, 3.367153, -5.0841], [5.0, 3.373419, -5.137987], [5.0, 2.775979, 0.0]]}]},
			"R_handIk_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_handIk_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-56.023671, 91.850166, -0.010851], [-56.023671, 91.861017, 0.0], [-56.023671, 91.850166, 0.010851], [-56.023671, 91.839315, -0.0], [-56.023671, 91.850166, -0.010851], [-56.034521, 91.850166, -0.0], [-56.023671, 91.850166, 0.010851], [-56.01282, 91.850166, -0.0], [-56.023671, 91.861017, 0.0], [-56.034521, 91.850166, -0.0], [-56.023671, 91.839315, -0.0], [-56.01282, 91.850166, -0.0], [-56.023671, 91.850166, -0.010851], [-56.034521, 91.850166, -0.0], [-55.0, 91.850166, -0.0]]}, {"shapeName": "R_handIk_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-55.0, 92.873837, -0.010851], [-54.989149, 92.873837, 0.0], [-55.0, 92.873837, 0.010851], [-55.010851, 92.873837, 0.0], [-55.0, 92.873837, -0.010851], [-55.0, 92.884687, 0.0], [-55.0, 92.873837, 0.010851], [-55.0, 92.862986, 0.0], [-54.989149, 92.873837, 0.0], [-55.0, 92.884687, 0.0], [-55.010851, 92.873837, 0.0], [-55.0, 92.862986, 0.0], [-55.0, 92.873837, -0.010851], [-55.0, 92.884687, 0.0], [-55.0, 91.850166, -0.0]]}, {"shapeName": "R_handIk_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-55.0, 91.861017, 1.023671], [-54.989149, 91.850166, 1.023671], [-55.0, 91.839315, 1.023671], [-55.010851, 91.850166, 1.023671], [-55.0, 91.861017, 1.023671], [-55.0, 91.850166, 1.034521], [-55.0, 91.839315, 1.023671], [-55.0, 91.850166, 1.01282], [-54.989149, 91.850166, 1.023671], [-55.0, 91.850166, 1.034521], [-55.010851, 91.850166, 1.023671], [-55.0, 91.850166, 1.01282], [-55.0, 91.861017, 1.023671], [-55.0, 91.850166, 1.034521], [-55.0, 91.850166, -0.0]]}]},
			"L_upLeg_shaper_05_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_05_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[15.0, 27.609312, 2.083333], [15.07612, 27.153642, 2.140292], [15.2929, 26.767345, 2.188579], [15.61732, 26.509217, 2.220845], [16.0, 26.418579, 2.232175], [16.38268, 26.509217, 2.220845], [16.7071, 26.767345, 2.188579], [16.92388, 27.153642, 2.140292], [17.0, 27.609312, 2.083333], [16.92388, 28.064982, 2.026375], [16.7071, 28.45128, 1.978087], [16.38268, 28.709407, 1.945821], [16.0, 28.800046, 1.934492], [15.61732, 28.709407, 1.945821], [15.2929, 28.45128, 1.978087], [15.07612, 28.064982, 2.026375], [15.0, 27.609312, 2.083333], [5.0, 27.609312, 2.083333]]}]},
			"R_leg_PV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_PV_CTLShape", "degree": 1, "form": 0, "points": [[-4.5, 24.775979, 53.0], [-4.5, 23.775979, 53.0], [-4.5, 23.775979, 52.0], [-4.5, 24.775979, 52.0], [-5.5, 24.775979, 52.0], [-5.5, 23.775979, 52.0], [-5.5, 23.775979, 53.0], [-5.5, 24.775979, 53.0], [-4.5, 24.775979, 53.0], [-4.5, 24.775979, 52.0], [-4.5, 23.775979, 52.0], [-5.5, 23.775979, 52.0], [-5.5, 24.775979, 52.0], [-5.5, 24.775979, 53.0], [-5.5, 23.775979, 53.0], [-4.5, 23.775979, 53.0]]}]},
			"C_head_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 101.795911, 0.0], [5.118355, 101.850166, -0.054255], [5.118355, 101.904421, 0.0], [5.118355, 101.850166, 0.054255], [5.118355, 101.795911, 0.0], [5.172605, 101.850166, 0.0], [5.118355, 101.904421, 0.0], [5.0641, 101.850166, 0.0], [5.118355, 101.850166, -0.054255], [5.172605, 101.850166, 0.0], [5.118355, 101.850166, 0.054255], [5.0641, 101.850166, 0.0], [5.118355, 101.795911, 0.0], [5.172605, 101.850166, 0.0], [0.0, 101.850166, 0.0]]}, {"shapeName": "C_head_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 101.795911, -5.118355], [-0.054255, 101.850166, -5.118355], [0.0, 101.904421, -5.118355], [0.054255, 101.850166, -5.118355], [0.0, 101.795911, -5.118355], [0.0, 101.850166, -5.172605], [0.0, 101.904421, -5.118355], [0.0, 101.850166, -5.0641], [-0.054255, 101.850166, -5.118355], [0.0, 101.850166, -5.172605], [0.054255, 101.850166, -5.118355], [0.0, 101.850166, -5.0641], [0.0, 101.795911, -5.118355], [0.0, 101.850166, -5.172605], [0.0, 101.850166, 0.0]]}, {"shapeName": "C_head_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 106.968521, -0.054255], [-0.054255, 106.968521, 0.0], [0.0, 106.968521, 0.054255], [0.054255, 106.968521, 0.0], [0.0, 106.968521, -0.054255], [0.0, 107.022771, 0.0], [0.0, 106.968521, 0.054255], [0.0, 106.914266, 0.0], [-0.054255, 106.968521, 0.0], [0.0, 107.022771, 0.0], [0.054255, 106.968521, 0.0], [0.0, 106.914266, 0.0], [0.0, 106.968521, -0.054255], [0.0, 107.022771, 0.0], [0.0, 101.850166, 0.0]]}]},
			"R_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_C_CTLShape", "degree": 1, "form": 0, "points": [[-64.30669, 91.640871, 5.57824], [-62.925674, 91.752126, 5.003421], [-63.300674, 93.051164, 4.353902], [-64.68169, 92.939909, 4.928721], [-65.131323, 92.198207, 3.704912], [-63.750307, 92.309462, 3.130093], [-63.375307, 91.010424, 3.779612], [-64.756323, 90.899168, 4.354431], [-64.30669, 91.640871, 5.57824], [-64.68169, 92.939909, 4.928721], [-63.300674, 93.051164, 4.353902], [-63.750307, 92.309462, 3.130093], [-65.131323, 92.198207, 3.704912], [-64.756323, 90.899168, 4.354431], [-63.375307, 91.010424, 3.779612], [-62.925674, 91.752126, 5.003421]]}]},
			"C_neckBase_B_OFF_CTL": {"color": 25, "shapes": [{"shapeName": "C_neckBase_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[5.194327, 94.84112, -4.176828], [-0.076152, 92.37401, -5.103935], [-5.726575, 93.731124, -4.12665], [-5.703619, 93.878907, 4.138643], [0.109037, 91.15665, 8.271747], [5.217283, 94.988903, 4.088465], [5.194327, 94.84112, -4.176828]]}]},
			"L_heel_CTL": {"color": 20, "shapes": [{"shapeName": "L_heel_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 0.275979, -1.75], [5.0, -0.224021, -2.25], [5.5, 0.275979, -2.25], [5.0, 0.275979, -1.75], [4.5, 0.275979, -2.25], [5.0, -0.224021, -2.25], [5.0, 0.275979, -2.75], [4.5, 0.275979, -2.25], [5.0, 0.775979, -2.25], [5.0, 0.275979, -1.75], [5.5, 0.275979, -2.25], [5.0, 0.275979, -2.75], [5.0, 0.775979, -2.25], [5.5, 0.275979, -2.25]]}]},
			"L_upLeg_shaper_04_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_04_CTLShape", "degree": 1, "form": 0, "points": [[17.5, 30.942646, 1.666667], [17.59515, 30.373058, 1.737865], [17.866125, 29.890186, 1.798224], [18.27165, 29.567527, 1.838556], [18.75, 29.454229, 1.852719], [19.22835, 29.567527, 1.838556], [19.633875, 29.890186, 1.798224], [19.90485, 30.373058, 1.737865], [20.0, 30.942646, 1.666667], [19.90485, 31.512233, 1.595468], [19.633875, 31.995105, 1.535109], [19.22835, 32.317764, 1.494777], [18.75, 32.431062, 1.480615], [18.27165, 32.317764, 1.494777], [17.866125, 31.995105, 1.535109], [17.59515, 31.512233, 1.595468], [17.5, 30.942646, 1.666667], [5.0, 30.942646, 1.666667]]}]},
			"C_midSpine_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_midSpine_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 64.350166, -0.054255], [5.118355, 64.404421, 0.0], [5.118355, 64.350166, 0.054255], [5.118355, 64.295911, 0.0], [5.118355, 64.350166, -0.054255], [5.172605, 64.350166, 0.0], [5.118355, 64.350166, 0.054255], [5.0641, 64.350166, 0.0], [5.118355, 64.404421, 0.0], [5.172605, 64.350166, 0.0], [5.118355, 64.295911, 0.0], [5.0641, 64.350166, 0.0], [5.118355, 64.350166, -0.054255], [5.172605, 64.350166, 0.0], [0.0, 64.350166, 0.0]]}, {"shapeName": "C_midSpine_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 69.468521, -0.054255], [-0.054255, 69.468521, 0.0], [0.0, 69.468521, 0.054255], [0.054255, 69.468521, 0.0], [0.0, 69.468521, -0.054255], [0.0, 69.522771, 0.0], [0.0, 69.468521, 0.054255], [0.0, 69.414266, 0.0], [-0.054255, 69.468521, 0.0], [0.0, 69.522771, 0.0], [0.054255, 69.468521, 0.0], [0.0, 69.414266, 0.0], [0.0, 69.468521, -0.054255], [0.0, 69.522771, 0.0], [0.0, 64.350166, 0.0]]}, {"shapeName": "C_midSpine_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 64.404421, 5.118355], [-0.054255, 64.350166, 5.118355], [0.0, 64.295911, 5.118355], [0.054255, 64.350166, 5.118355], [0.0, 64.404421, 5.118355], [0.0, 64.350166, 5.172605], [0.0, 64.295911, 5.118355], [0.0, 64.350166, 5.0641], [-0.054255, 64.350166, 5.118355], [0.0, 64.350166, 5.172605], [0.054255, 64.350166, 5.118355], [0.0, 64.350166, 5.0641], [0.0, 64.404421, 5.118355], [0.0, 64.350166, 5.172605], [0.0, 64.350166, 0.0]]}]},
			"L_elbow_shaper_03_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_03_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[46.5, 93.850166, -2.5], [46.573426, 93.86539, -2.478404], [46.635673, 93.908746, -2.460096], [46.677268, 93.97363, -2.447862], [46.691873, 94.050166, -2.443567], [46.677268, 94.126702, -2.447862], [46.635673, 94.191586, -2.460096], [46.573426, 94.234942, -2.478404], [46.5, 94.250166, -2.5], [46.426574, 94.234942, -2.521596], [46.364327, 94.191586, -2.539904], [46.322732, 94.126702, -2.552138], [46.308127, 94.050166, -2.556433], [46.322732, 93.97363, -2.552138], [46.364327, 93.908746, -2.539904], [46.426574, 93.86539, -2.521596], [46.5, 93.850166, -2.5], [46.5, 91.850166, -2.5]]}]},
			"R_shoulder_shaper_03_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_shaper_03_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-29.983421, 91.850166, -2.784434], [-29.986325, 91.861017, -2.773979], [-29.98923, 91.850166, -2.763524], [-29.986325, 91.839315, -2.773979], [-29.983421, 91.850166, -2.784434], [-29.99678, 91.850166, -2.776883], [-29.98923, 91.850166, -2.763524], [-29.97587, 91.850166, -2.771075], [-29.986325, 91.861017, -2.773979], [-29.99678, 91.850166, -2.776883], [-29.986325, 91.839315, -2.773979], [-29.97587, 91.850166, -2.771075], [-29.983421, 91.850166, -2.784434], [-29.99678, 91.850166, -2.776883], [-29.0, 91.850166, -2.5]]}, {"shapeName": "R_shoulder_shaper_03_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-28.997096, 92.873837, -2.510455], [-28.989545, 92.873837, -2.497096], [-29.002904, 92.873837, -2.489545], [-29.010455, 92.873837, -2.502904], [-28.997096, 92.873837, -2.510455], [-29.0, 92.884687, -2.5], [-29.002904, 92.873837, -2.489545], [-29.0, 92.862986, -2.5], [-28.989545, 92.873837, -2.497096], [-29.0, 92.884687, -2.5], [-29.010455, 92.873837, -2.502904], [-29.0, 92.862986, -2.5], [-28.997096, 92.873837, -2.510455], [-29.0, 92.884687, -2.5], [-29.0, 91.850166, -2.5]]}, {"shapeName": "R_shoulder_shaper_03_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-29.273979, 91.861017, -1.513675], [-29.263524, 91.850166, -1.51077], [-29.273979, 91.839315, -1.513675], [-29.284434, 91.850166, -1.516579], [-29.273979, 91.861017, -1.513675], [-29.276883, 91.850166, -1.50322], [-29.273979, 91.839315, -1.513675], [-29.271075, 91.850166, -1.52413], [-29.263524, 91.850166, -1.51077], [-29.276883, 91.850166, -1.50322], [-29.284434, 91.850166, -1.516579], [-29.271075, 91.850166, -1.52413], [-29.273979, 91.861017, -1.513675], [-29.276883, 91.850166, -1.50322], [-29.0, 91.850166, -2.5]]}]},
			"L_loLeg_shaper_03_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_shaper_03_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 8.435613, 0.712717], [4.945745, 8.441879, 0.658826], [5.0, 8.448146, 0.604934], [5.054255, 8.441879, 0.658826], [5.0, 8.435613, 0.712717], [5.0, 8.387992, 0.65256], [5.0, 8.448146, 0.604934], [5.0, 8.495771, 0.665092], [4.945745, 8.441879, 0.658826], [5.0, 8.387992, 0.65256], [5.054255, 8.441879, 0.658826], [5.0, 8.495771, 0.665092], [5.0, 8.435613, 0.712717], [5.0, 8.387992, 0.65256], [5.0, 13.525979, 1.25]]}, {"shapeName": "L_loLeg_shaper_03_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 13.519713, 1.303892], [-0.118355, 13.579871, 1.256266], [-0.118355, 13.532246, 1.196108], [-0.118355, 13.472087, 1.243734], [-0.118355, 13.519713, 1.303892], [-0.172605, 13.525979, 1.25], [-0.118355, 13.532246, 1.196108], [-0.0641, 13.525979, 1.25], [-0.118355, 13.579871, 1.256266], [-0.172605, 13.525979, 1.25], [-0.118355, 13.472087, 1.243734], [-0.0641, 13.525979, 1.25], [-0.118355, 13.519713, 1.303892], [-0.172605, 13.525979, 1.25], [5.0, 13.525979, 1.25]]}, {"shapeName": "L_loLeg_shaper_03_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 14.117153, -3.8341], [5.0, 14.171045, -3.827833], [5.054255, 14.117153, -3.8341], [5.0, 14.063262, -3.840366], [4.945745, 14.117153, -3.8341], [5.0, 14.123419, -3.887987], [5.054255, 14.117153, -3.8341], [5.0, 14.110887, -3.780208], [5.0, 14.171045, -3.827833], [5.0, 14.123419, -3.887987], [5.0, 14.063262, -3.840366], [5.0, 14.110887, -3.780208], [4.945745, 14.117153, -3.8341], [5.0, 14.123419, -3.887987], [5.0, 13.525979, 1.25]]}]},
			"L_elbow_shaper_04_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_04_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[50.75, 93.350166, -1.25], [50.805069, 93.361584, -1.233803], [50.851755, 93.394101, -1.220072], [50.882951, 93.442764, -1.210897], [50.893905, 93.500166, -1.207675], [50.882951, 93.557568, -1.210897], [50.851755, 93.606231, -1.220072], [50.805069, 93.638748, -1.233803], [50.75, 93.650166, -1.25], [50.694931, 93.638748, -1.266197], [50.648245, 93.606231, -1.279928], [50.617049, 93.557568, -1.289103], [50.606095, 93.500166, -1.292325], [50.617049, 93.442764, -1.289103], [50.648245, 93.394101, -1.279928], [50.694931, 93.361584, -1.266197], [50.75, 93.350166, -1.25], [50.75, 91.850166, -1.25]]}]},
			"R_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.227054, 92.508365, 1.195745], [-68.222728, 92.562447, 1.25], [-68.227054, 92.508365, 1.304255], [-68.231381, 92.454282, 1.25], [-68.227054, 92.508365, 1.195745], [-68.281132, 92.512691, 1.25], [-68.227054, 92.508365, 1.304255], [-68.172972, 92.504038, 1.25], [-68.222728, 92.562447, 1.25], [-68.281132, 92.512691, 1.25], [-68.231381, 92.454282, 1.25], [-68.172972, 92.504038, 1.25], [-68.227054, 92.508365, 1.195745], [-68.281132, 92.512691, 1.25], [-63.125, 92.1002, 1.25]]}, {"shapeName": "R_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-62.716836, 97.202255, 1.195745], [-62.662753, 97.197928, 1.25], [-62.716836, 97.202255, 1.304255], [-62.770918, 97.206581, 1.25], [-62.716836, 97.202255, 1.195745], [-62.712509, 97.256332, 1.25], [-62.716836, 97.202255, 1.304255], [-62.721162, 97.148173, 1.25], [-62.662753, 97.197928, 1.25], [-62.712509, 97.256332, 1.25], [-62.770918, 97.206581, 1.25], [-62.721162, 97.148173, 1.25], [-62.716836, 97.202255, 1.195745], [-62.712509, 97.256332, 1.25], [-63.125, 92.1002, 1.25]]}, {"shapeName": "R_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-63.120673, 92.154283, 6.368355], [-63.070918, 92.095874, 6.368355], [-63.129327, 92.046118, 6.368355], [-63.179082, 92.104527, 6.368355], [-63.120673, 92.154283, 6.368355], [-63.125, 92.1002, 6.422605], [-63.129327, 92.046118, 6.368355], [-63.125, 92.1002, 6.3141], [-63.070918, 92.095874, 6.368355], [-63.125, 92.1002, 6.422605], [-63.179082, 92.104527, 6.368355], [-63.125, 92.1002, 6.3141], [-63.120673, 92.154283, 6.368355], [-63.125, 92.1002, 6.422605], [-63.125, 92.1002, 1.25]]}]},
			"L_innerBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_innerBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[7.618355, 0.275979, 4.945745], [7.618355, 0.330234, 5.0], [7.618355, 0.275979, 5.054255], [7.618355, 0.221724, 5.0], [7.618355, 0.275979, 4.945745], [7.672605, 0.275979, 5.0], [7.618355, 0.275979, 5.054255], [7.5641, 0.275979, 5.0], [7.618355, 0.330234, 5.0], [7.672605, 0.275979, 5.0], [7.618355, 0.221724, 5.0], [7.5641, 0.275979, 5.0], [7.618355, 0.275979, 4.945745], [7.672605, 0.275979, 5.0], [2.5, 0.275979, 5.0]]}, {"shapeName": "L_innerBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.5, 5.394334, 4.945745], [2.445745, 5.394334, 5.0], [2.5, 5.394334, 5.054255], [2.554255, 5.394334, 5.0], [2.5, 5.394334, 4.945745], [2.5, 5.448584, 5.0], [2.5, 5.394334, 5.054255], [2.5, 5.340079, 5.0], [2.445745, 5.394334, 5.0], [2.5, 5.448584, 5.0], [2.554255, 5.394334, 5.0], [2.5, 5.340079, 5.0], [2.5, 5.394334, 4.945745], [2.5, 5.448584, 5.0], [2.5, 0.275979, 5.0]]}, {"shapeName": "L_innerBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.5, 0.330234, 10.118355], [2.445745, 0.275979, 10.118355], [2.5, 0.221724, 10.118355], [2.554255, 0.275979, 10.118355], [2.5, 0.330234, 10.118355], [2.5, 0.275979, 10.172605], [2.5, 0.221724, 10.118355], [2.5, 0.275979, 10.0641], [2.445745, 0.275979, 10.118355], [2.5, 0.275979, 10.172605], [2.554255, 0.275979, 10.118355], [2.5, 0.275979, 10.0641], [2.5, 0.330234, 10.118355], [2.5, 0.275979, 10.172605], [2.5, 0.275979, 5.0]]}]},
			"L_toe_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.371321, 1.6473, 5.0], [5.0, 2.215319, 5.0], [3.628679, 1.6473, 5.0], [3.060661, 0.275979, 5.0], [3.628679, -1.095342, 5.0], [5.0, -1.66336, 5.0], [6.371321, -1.095342, 5.0], [6.939339, 0.275979, 5.0]]}]},
			"R_bendyLeg_A_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_bendyLeg_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.416666, 34.49304, 2.986486], [-4.066666, 34.49304, 2.986486], [-5.0, 34.60157, 3.854729], [-5.933334, 34.49304, 2.986486], [-5.583335, 34.49304, 2.986486], [-5.583334, 34.348333, 1.82883], [-6.75, 34.348333, 1.82883], [-6.75, 34.391745, 2.176127], [-7.625, 34.275979, 1.25], [-6.75, 34.160213, 0.323873], [-6.75, 34.203625, 0.67117], [-5.583334, 34.203625, 0.67117], [-5.583334, 34.058918, -0.486486], [-5.933334, 34.058918, -0.486486], [-5.0, 33.950388, -1.354729], [-4.066665, 34.058918, -0.486486], [-4.416665, 34.058918, -0.486486], [-4.416665, 34.203625, 0.67117], [-3.25, 34.203625, 0.67117], [-3.25, 34.160213, 0.323873], [-2.375, 34.275979, 1.25], [-3.25, 34.391745, 2.176127], [-3.25, 34.348333, 1.82883], [-4.416665, 34.348333, 1.82883], [-4.416666, 34.49304, 2.986486]]}]},
			"L_elbow_shaper_05_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_05_CTLShape", "degree": 1, "form": 0, "points": [[54.15, 94.350166, -0.25], [54.241782, 94.369196, -0.223005], [54.319592, 94.423391, -0.20012], [54.371585, 94.504496, -0.184828], [54.389841, 94.600166, -0.179458], [54.371585, 94.695836, -0.184828], [54.319592, 94.776941, -0.20012], [54.241782, 94.831136, -0.223005], [54.15, 94.850166, -0.25], [54.058218, 94.831136, -0.276995], [53.980408, 94.776941, -0.29988], [53.928415, 94.695836, -0.315172], [53.910159, 94.600166, -0.320542], [53.928415, 94.504496, -0.315172], [53.980408, 94.423391, -0.29988], [54.058218, 94.369196, -0.276995], [54.15, 94.350166, -0.25], [54.15, 91.850166, -0.25]]}]},
			"R_elbow_shaper_02_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_02_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-42.25, 93.600166, -3.75], [-42.314248, 93.613487, -3.731104], [-42.368714, 93.651424, -3.715084], [-42.405109, 93.708197, -3.70438], [-42.417889, 93.775166, -3.700621], [-42.405109, 93.842135, -3.70438], [-42.368714, 93.898909, -3.715084], [-42.314248, 93.936845, -3.731104], [-42.25, 93.950166, -3.75], [-42.185752, 93.936845, -3.768896], [-42.131286, 93.898909, -3.784916], [-42.094891, 93.842135, -3.79562], [-42.082111, 93.775166, -3.799379], [-42.094891, 93.708197, -3.79562], [-42.131286, 93.651424, -3.784916], [-42.185752, 93.613487, -3.768896], [-42.25, 93.600166, -3.75], [-42.25, 91.850166, -3.75]]}]},
			"L_loLeg_shaper_01_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_01_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.25, 20.692646, 2.083333], [16.335635, 20.179485, 2.023664], [16.579512, 19.744449, 1.973078], [16.944485, 19.453755, 1.939276], [17.375, 19.351681, 1.927407], [17.805515, 19.453755, 1.939276], [18.170488, 19.744449, 1.973078], [18.414365, 20.179485, 2.023664], [18.5, 20.692646, 2.083333], [18.414365, 21.205806, 2.143003], [18.170488, 21.640842, 2.193589], [17.805515, 21.931536, 2.22739], [17.375, 22.033611, 2.239259], [16.944485, 21.931536, 2.22739], [16.579512, 21.640842, 2.193589], [16.335635, 21.205806, 2.143003], [16.25, 20.692646, 2.083333], [5.0, 20.692646, 2.083333]]}]},
			"L_leg_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[8.127512, 3.243422, 0.054354], [8.000172, 3.243422, 0.054354], [7.976056, 3.113628, 0.039262], [7.885568, 3.076387, 0.034931], [7.776112, 3.151227, 0.043633], [7.686068, 3.061785, 0.033233], [7.761408, 2.953074, 0.020592], [7.723932, 2.86318, 0.01014], [7.593252, 2.839225, 0.007354], [7.593252, 2.712733, -0.007354], [7.723932, 2.688779, -0.01014], [7.761408, 2.598896, -0.020591], [7.686068, 2.490173, -0.033233], [7.776112, 2.400731, -0.043633], [7.885568, 2.475571, -0.034931], [7.976056, 2.43833, -0.039262], [8.000172, 2.308537, -0.054354], [8.127512, 2.308537, -0.054354], [8.15164, 2.43833, -0.039262], [8.242128, 2.475571, -0.034931], [8.351584, 2.400731, -0.043633], [8.44162, 2.490173, -0.033233], [8.366288, 2.598896, -0.020591], [8.403764, 2.688779, -0.01014], [8.534432, 2.712733, -0.007354], [8.534432, 2.839225, 0.007354], [8.403764, 2.86318, 0.01014], [8.366288, 2.953074, 0.020592], [8.44162, 3.061785, 0.033233], [8.351584, 3.151227, 0.043633], [8.242128, 3.076387, 0.034931], [8.15164, 3.113628, 0.039262], [8.127512, 3.243422, 0.054354]]}, {"shapeName": "L_leg_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[8.202064, 2.913278, 0.015965], [8.25932, 2.775979, 0.0], [8.202064, 2.63868, -0.015965], [8.063844, 2.581819, -0.022577], [7.925632, 2.63868, -0.015965], [7.868376, 2.775979, 0.0], [7.925632, 2.913278, 0.015965], [8.063844, 2.970139, 0.022577]]}, {"shapeName": "L_leg_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[7.593252, 2.775979, 0.0], [5.0, 2.775979, 0.0]]}]},
			"C_spine_FK_1_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_spine_FK_1_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 64.350166, -0.054255], [5.118355, 64.404421, 0.0], [5.118355, 64.350166, 0.054255], [5.118355, 64.295911, 0.0], [5.118355, 64.350166, -0.054255], [5.172605, 64.350166, 0.0], [5.118355, 64.350166, 0.054255], [5.0641, 64.350166, 0.0], [5.118355, 64.404421, 0.0], [5.172605, 64.350166, 0.0], [5.118355, 64.295911, 0.0], [5.0641, 64.350166, 0.0], [5.118355, 64.350166, -0.054255], [5.172605, 64.350166, 0.0], [0.0, 64.350166, 0.0]]}, {"shapeName": "C_spine_FK_1_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 69.468521, -0.054255], [-0.054255, 69.468521, 0.0], [0.0, 69.468521, 0.054255], [0.054255, 69.468521, 0.0], [0.0, 69.468521, -0.054255], [0.0, 69.522771, 0.0], [0.0, 69.468521, 0.054255], [0.0, 69.414266, 0.0], [-0.054255, 69.468521, 0.0], [0.0, 69.522771, 0.0], [0.054255, 69.468521, 0.0], [0.0, 69.414266, 0.0], [0.0, 69.468521, -0.054255], [0.0, 69.522771, 0.0], [0.0, 64.350166, 0.0]]}, {"shapeName": "C_spine_FK_1_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 64.404421, 5.118355], [-0.054255, 64.350166, 5.118355], [0.0, 64.295911, 5.118355], [0.054255, 64.350166, 5.118355], [0.0, 64.404421, 5.118355], [0.0, 64.350166, 5.172605], [0.0, 64.295911, 5.118355], [0.0, 64.350166, 5.0641], [-0.054255, 64.350166, 5.118355], [0.0, 64.350166, 5.172605], [0.054255, 64.350166, 5.118355], [0.0, 64.350166, 5.0641], [0.0, 64.404421, 5.118355], [0.0, 64.350166, 5.172605], [0.0, 64.350166, 0.0]]}]},
			"L_upLeg_shaper_02_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_shaper_02_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 32.537211, 1.522023], [4.945745, 32.530482, 1.468187], [5.0, 32.523752, 1.414351], [5.054255, 32.530482, 1.468187], [5.0, 32.537211, 1.522023], [5.0, 32.476651, 1.474916], [5.0, 32.523752, 1.414351], [5.0, 32.584318, 1.461458], [4.945745, 32.530482, 1.468187], [5.0, 32.476651, 1.474916], [5.054255, 32.530482, 1.468187], [5.0, 32.584318, 1.461458], [5.0, 32.537211, 1.522023], [5.0, 32.476651, 1.474916], [5.0, 37.609312, 0.833333]]}, {"shapeName": "L_upLeg_shaper_02_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 37.616042, 0.887169], [-0.118355, 37.663148, 0.826604], [-0.118355, 37.602583, 0.779497], [-0.118355, 37.555476, 0.840063], [-0.118355, 37.616042, 0.887169], [-0.172605, 37.609312, 0.833333], [-0.118355, 37.602583, 0.779497], [-0.0641, 37.609312, 0.833333], [-0.118355, 37.663148, 0.826604], [-0.172605, 37.609312, 0.833333], [-0.118355, 37.555476, 0.840063], [-0.0641, 37.609312, 0.833333], [-0.118355, 37.616042, 0.887169], [-0.172605, 37.609312, 0.833333], [5.0, 37.609312, 0.833333]]}, {"shapeName": "L_upLeg_shaper_02_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 36.974458, -4.245497], [5.0, 37.028295, -4.252227], [5.054255, 36.974458, -4.245497], [5.0, 36.920622, -4.238768], [4.945745, 36.974458, -4.245497], [5.0, 36.96773, -4.299328], [5.054255, 36.974458, -4.245497], [5.0, 36.981188, -4.191661], [5.0, 37.028295, -4.252227], [5.0, 36.96773, -4.299328], [5.0, 36.920622, -4.238768], [5.0, 36.981188, -4.191661], [4.945745, 36.974458, -4.245497], [5.0, 36.96773, -4.299328], [5.0, 37.609312, 0.833333]]}]},
			"R_elbow_shaper_03_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_elbow_shaper_03_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-46.5, 93.850166, -2.5], [-46.573426, 93.86539, -2.478404], [-46.635673, 93.908746, -2.460096], [-46.677268, 93.97363, -2.447862], [-46.691873, 94.050166, -2.443567], [-46.677268, 94.126702, -2.447862], [-46.635673, 94.191586, -2.460096], [-46.573426, 94.234942, -2.478404], [-46.5, 94.250166, -2.5], [-46.426574, 94.234942, -2.521596], [-46.364327, 94.191586, -2.539904], [-46.322732, 94.126702, -2.552138], [-46.308127, 94.050166, -2.556433], [-46.322732, 93.97363, -2.552138], [-46.364327, 93.908746, -2.539904], [-46.426574, 93.86539, -2.521596], [-46.5, 93.850166, -2.5], [-46.5, 91.850166, -2.5]]}]},
			"R_upLeg_shaper_02_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_upLeg_shaper_02_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-15.0, 37.609312, 0.833333], [-15.07612, 37.153642, 0.890292], [-15.2929, 36.767345, 0.938579], [-15.61732, 36.509217, 0.970845], [-16.0, 36.418579, 0.982175], [-16.38268, 36.509217, 0.970845], [-16.7071, 36.767345, 0.938579], [-16.92388, 37.153642, 0.890292], [-17.0, 37.609312, 0.833333], [-16.92388, 38.064982, 0.776375], [-16.7071, 38.45128, 0.728087], [-16.38268, 38.709407, 0.695821], [-16.0, 38.800046, 0.684492], [-15.61732, 38.709407, 0.695821], [-15.2929, 38.45128, 0.728087], [-15.07612, 38.064982, 0.776375], [-15.0, 37.609312, 0.833333], [-5.0, 37.609312, 0.833333]]}]},
			"L_toe_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_CTLShape", "degree": 3, "form": 2, "points": [[6.95903, 2.235009, 6.25], [5.0, 3.046464, 6.25], [3.04097, 2.235009, 6.25], [2.229515, 0.275979, 6.25], [3.04097, -1.683051, 6.25], [5.0, -2.494506, 6.25], [6.95903, -1.683051, 6.25], [7.770485, 0.275979, 6.25]]}]},
			"L_elbowRibbon_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_elbowRibbon_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[38.033985, 93.350169, -9.499872], [38.033985, 94.250169, -9.499872], [38.050978, 91.850166, -11.749808], [38.033985, 89.450163, -9.499872], [38.033985, 90.350163, -9.499872], [38.011328, 90.350163, -6.49996], [38.011328, 87.350166, -6.49996], [38.018125, 87.350166, -7.399935], [38.0, 85.100166, -5.0], [37.981875, 87.350166, -2.600065], [37.988672, 87.350166, -3.50004], [37.988672, 90.350163, -3.50004], [37.966015, 90.350163, -0.500128], [37.966015, 89.450163, -0.500128], [37.949022, 91.850166, 1.749808], [37.966015, 94.250169, -0.500128], [37.966015, 93.350169, -0.500128], [37.988672, 93.350169, -3.50004], [37.988672, 96.350166, -3.50004], [37.981875, 96.350166, -2.600065], [38.0, 98.600166, -5.0], [38.018125, 96.350166, -7.399935], [38.011328, 96.350166, -6.49996], [38.011328, 93.350169, -6.49996], [38.033985, 93.350169, -9.499872]]}]},
			"L_elbowRibbon_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_elbowRibbon_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[38.026433, 93.016835, -8.4999], [38.026433, 93.716835, -8.4999], [38.039649, 91.850166, -10.24985], [38.026433, 89.983497, -8.4999], [38.026433, 90.683497, -8.4999], [38.008811, 90.683497, -6.166636], [38.008811, 88.350166, -6.166636], [38.014098, 88.350166, -6.866616], [38.0, 86.600166, -5.0], [37.985902, 88.350166, -3.133384], [37.991189, 88.350166, -3.833364], [37.991189, 90.683497, -3.833364], [37.973567, 90.683497, -1.5001], [37.973567, 89.983497, -1.5001], [37.960351, 91.850166, 0.24985], [37.973567, 93.716835, -1.5001], [37.973567, 93.016835, -1.5001], [37.991189, 93.016835, -3.833364], [37.991189, 95.350166, -3.833364], [37.985902, 95.350166, -3.133384], [38.0, 97.100166, -5.0], [38.014098, 95.350166, -6.866616], [38.008811, 95.350166, -6.166636], [38.008811, 93.016835, -6.166636], [38.026433, 93.016835, -8.4999]]}]},
			"R_elbowRibbon_CTL": {"color": 17, "shapes": [{"shapeName": "R_elbowRibbon_CTLShape", "degree": 1, "form": 0, "points": [[-38.037761, 93.516836, -9.999857], [-38.037761, 94.516836, -9.999857], [-38.056642, 91.850166, -12.499786], [-38.037761, 89.183496, -9.999857], [-38.037761, 90.183496, -9.999857], [-38.012587, 90.183496, -6.666622], [-38.012587, 86.850166, -6.666622], [-38.020139, 86.850166, -7.666594], [-38.0, 84.350166, -5.0], [-37.979861, 86.850166, -2.333406], [-37.987413, 86.850166, -3.333378], [-37.987413, 90.183496, -3.333378], [-37.962239, 90.183496, -0.000143], [-37.962239, 89.183496, -0.000143], [-37.943358, 91.850166, 2.499786], [-37.962239, 94.516836, -0.000143], [-37.962239, 93.516836, -0.000143], [-37.987413, 93.516836, -3.333378], [-37.987413, 96.850166, -3.333378], [-37.979861, 96.850166, -2.333406], [-38.0, 99.350166, -5.0], [-38.020139, 96.850166, -7.666594], [-38.012587, 96.850166, -6.666622], [-38.012587, 93.516836, -6.666622], [-38.037761, 93.516836, -9.999857]]}]},
			"L_upLeg_shaper_03_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_03_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[13.75, 34.275979, 1.25], [13.816605, 33.877268, 1.299839], [14.006287, 33.539257, 1.34209], [14.290155, 33.313396, 1.370323], [14.625, 33.234087, 1.380236], [14.959845, 33.313396, 1.370323], [15.243712, 33.539257, 1.34209], [15.433395, 33.877268, 1.299839], [15.5, 34.275979, 1.25], [15.433395, 34.67469, 1.200161], [15.243712, 35.012701, 1.15791], [14.959845, 35.238562, 1.129677], [14.625, 35.317871, 1.119764], [14.290155, 35.238562, 1.129677], [14.006287, 35.012701, 1.15791], [13.816605, 34.67469, 1.200161], [13.75, 34.275979, 1.25], [5.0, 34.275979, 1.25]]}]},
			"L_loLeg_shaper_02_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_shaper_02_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 12.018946, 1.129384], [4.945745, 12.025213, 1.075492], [5.0, 12.031479, 1.0216], [5.054255, 12.025213, 1.075492], [5.0, 12.018946, 1.129384], [5.0, 11.971326, 1.069226], [5.0, 12.031479, 1.0216], [5.0, 12.079104, 1.081759], [4.945745, 12.025213, 1.075492], [5.0, 11.971326, 1.069226], [5.054255, 12.025213, 1.075492], [5.0, 12.079104, 1.081759], [5.0, 12.018946, 1.129384], [5.0, 11.971326, 1.069226], [5.0, 17.109312, 1.666667]]}, {"shapeName": "L_loLeg_shaper_02_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 17.103046, 1.720559], [-0.118355, 17.163204, 1.672933], [-0.118355, 17.115579, 1.612775], [-0.118355, 17.05542, 1.6604], [-0.118355, 17.103046, 1.720559], [-0.172605, 17.109312, 1.666667], [-0.118355, 17.115579, 1.612775], [-0.0641, 17.109312, 1.666667], [-0.118355, 17.163204, 1.672933], [-0.172605, 17.109312, 1.666667], [-0.118355, 17.05542, 1.6604], [-0.0641, 17.109312, 1.666667], [-0.118355, 17.103046, 1.720559], [-0.172605, 17.109312, 1.666667], [5.0, 17.109312, 1.666667]]}, {"shapeName": "L_loLeg_shaper_02_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 17.700487, -3.417433], [5.0, 17.754379, -3.411167], [5.054255, 17.700487, -3.417433], [5.0, 17.646595, -3.4237], [4.945745, 17.700487, -3.417433], [5.0, 17.706753, -3.47132], [5.054255, 17.700487, -3.417433], [5.0, 17.69422, -3.363541], [5.0, 17.754379, -3.411167], [5.0, 17.706753, -3.47132], [5.0, 17.646595, -3.4237], [5.0, 17.69422, -3.363541], [4.945745, 17.700487, -3.417433], [5.0, 17.706753, -3.47132], [5.0, 17.109312, 1.666667]]}]},
			"L_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_C_CTLShape", "degree": 1, "form": 0, "points": [[65.80742, 92.937969, 0.75], [64.312197, 93.057587, 0.75], [64.312197, 93.057587, -0.75], [65.80742, 92.937969, -0.75], [65.687803, 91.442746, -0.75], [64.19258, 91.562364, -0.75], [64.19258, 91.562364, 0.75], [65.687803, 91.442746, 0.75], [65.80742, 92.937969, 0.75], [65.80742, 92.937969, -0.75], [64.312197, 93.057587, -0.75], [64.19258, 91.562364, -0.75], [65.687803, 91.442746, -0.75], [65.687803, 91.442746, 0.75], [64.19258, 91.562364, 0.75], [64.312197, 93.057587, 0.75]]}]},
			"L_upLeg_shaper_05_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_05_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[12.5, 27.609312, 2.083333], [12.55709, 27.26756, 2.126052], [12.719675, 26.977837, 2.162268], [12.96299, 26.784241, 2.186467], [13.25, 26.716262, 2.194965], [13.53701, 26.784241, 2.186467], [13.780325, 26.977837, 2.162268], [13.94291, 27.26756, 2.126052], [14.0, 27.609312, 2.083333], [13.94291, 27.951065, 2.040614], [13.780325, 28.240788, 2.004399], [13.53701, 28.434383, 1.980199], [13.25, 28.502362, 1.971702], [12.96299, 28.434383, 1.980199], [12.719675, 28.240788, 2.004399], [12.55709, 27.951065, 2.040614], [12.5, 27.609312, 2.083333], [5.0, 27.609312, 2.083333]]}]},
			"L_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.754415, 91.642523, 6.292093], [68.724588, 91.622364, 6.359851], [68.727288, 91.548551, 6.339079], [68.757115, 91.568709, 6.271321], [68.754415, 91.642523, 6.292093], [68.790798, 91.591513, 6.336375], [68.727288, 91.548551, 6.339079], [68.6909, 91.599561, 6.294795], [68.724588, 91.622364, 6.359851], [68.790798, 91.591513, 6.336375], [68.757115, 91.568709, 6.271321], [68.6909, 91.599561, 6.294795], [68.754415, 91.642523, 6.292093], [68.790798, 91.591513, 6.336375], [64.028498, 91.975166, 4.354167]]}, {"shapeName": "L_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[62.507807, 94.553016, 8.506599], [62.444292, 94.510054, 8.5093], [62.48068, 94.459044, 8.553585], [62.544195, 94.502006, 8.550883], [62.507807, 94.553016, 8.506599], [62.477982, 94.532855, 8.574353], [62.48068, 94.459044, 8.553585], [62.510507, 94.479203, 8.485827], [62.444292, 94.510054, 8.5093], [62.477982, 94.532855, 8.574353], [62.544195, 94.502006, 8.550883], [62.510507, 94.479203, 8.485827], [62.507807, 94.553016, 8.506599], [62.477982, 94.532855, 8.574353], [64.028498, 91.975166, 4.354167]]}, {"shapeName": "L_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[62.732646, 87.569368, 6.614745], [62.698958, 87.546565, 6.549688], [62.765173, 87.515713, 6.526214], [62.798861, 87.538517, 6.591271], [62.732646, 87.569368, 6.614745], [62.735347, 87.495559, 6.59397], [62.765173, 87.515713, 6.526214], [62.762473, 87.589527, 6.546986], [62.698958, 87.546565, 6.549688], [62.735347, 87.495559, 6.59397], [62.798861, 87.538517, 6.591271], [62.762473, 87.589527, 6.546986], [62.732646, 87.569368, 6.614745], [62.735347, 87.495559, 6.59397], [64.028498, 91.975166, 4.354167]]}]},
			"L_shoulder_shaper_04_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_shoulder_shaper_04_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[33.5, 94.100166, -3.75], [33.582962, 94.117293, -3.773045], [33.653293, 94.166069, -3.792581], [33.700289, 94.239063, -3.805636], [33.716792, 94.325166, -3.81022], [33.700289, 94.411269, -3.805636], [33.653293, 94.484264, -3.792581], [33.582962, 94.533039, -3.773045], [33.5, 94.550166, -3.75], [33.417038, 94.533039, -3.726955], [33.346707, 94.484264, -3.707419], [33.299711, 94.411269, -3.694364], [33.283208, 94.325166, -3.68978], [33.299711, 94.239063, -3.694364], [33.346707, 94.166069, -3.707419], [33.417038, 94.117293, -3.726955], [33.5, 94.100166, -3.75], [33.5, 91.850166, -3.75]]}]},
			"L_lwrArmRibbonMid_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lwrArmRibbonMid_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[47.487582, 93.016835, -5.857779], [47.487582, 93.716835, -5.857779], [47.981373, 91.850166, -7.536669], [47.487582, 89.983497, -5.857779], [47.487582, 90.683497, -5.857779], [46.829195, 90.683497, -3.619262], [46.829195, 88.350166, -3.619262], [47.026711, 88.350166, -4.290818], [46.5, 86.600166, -2.5], [45.973289, 88.350166, -0.709182], [46.170805, 88.350166, -1.380738], [46.170805, 90.683497, -1.380738], [45.512418, 90.683497, 0.857779], [45.512418, 89.983497, 0.857779], [45.018627, 91.850166, 2.536669], [45.512418, 93.716835, 0.857779], [45.512418, 93.016835, 0.857779], [46.170805, 93.016835, -1.380738], [46.170805, 95.350166, -1.380738], [45.973289, 95.350166, -0.709182], [46.5, 97.100166, -2.5], [47.026711, 95.350166, -4.290818], [46.829195, 95.350166, -3.619262], [46.829195, 93.016835, -3.619262], [47.487582, 93.016835, -5.857779]]}]},
			"L_elbow_shaper_02_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "L_elbow_shaper_02_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[42.25, 93.600166, -3.75], [42.314248, 93.613487, -3.731104], [42.368714, 93.651424, -3.715084], [42.405109, 93.708197, -3.70438], [42.417889, 93.775166, -3.700621], [42.405109, 93.842135, -3.70438], [42.368714, 93.898909, -3.715084], [42.314248, 93.936845, -3.731104], [42.25, 93.950166, -3.75], [42.185752, 93.936845, -3.768896], [42.131286, 93.898909, -3.784916], [42.094891, 93.842135, -3.79562], [42.082111, 93.775166, -3.799379], [42.094891, 93.708197, -3.79562], [42.131286, 93.651424, -3.784916], [42.185752, 93.613487, -3.768896], [42.25, 93.600166, -3.75], [42.25, 91.850166, -3.75]]}]},
			"L_loLeg_shaper_01_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_shaper_01_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.0, 15.602279, 1.546051], [4.945745, 15.608546, 1.492159], [5.0, 15.614812, 1.438267], [5.054255, 15.608546, 1.492159], [5.0, 15.602279, 1.546051], [5.0, 15.554659, 1.485893], [5.0, 15.614812, 1.438267], [5.0, 15.662438, 1.498425], [4.945745, 15.608546, 1.492159], [5.0, 15.554659, 1.485893], [5.054255, 15.608546, 1.492159], [5.0, 15.662438, 1.498425], [5.0, 15.602279, 1.546051], [5.0, 15.554659, 1.485893], [5.0, 20.692646, 2.083333]]}, {"shapeName": "L_loLeg_shaper_01_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.118355, 20.686379, 2.137225], [-0.118355, 20.746538, 2.0896], [-0.118355, 20.698912, 2.029441], [-0.118355, 20.638754, 2.077067], [-0.118355, 20.686379, 2.137225], [-0.172605, 20.692646, 2.083333], [-0.118355, 20.698912, 2.029441], [-0.0641, 20.692646, 2.083333], [-0.118355, 20.746538, 2.0896], [-0.172605, 20.692646, 2.083333], [-0.118355, 20.638754, 2.077067], [-0.0641, 20.692646, 2.083333], [-0.118355, 20.686379, 2.137225], [-0.172605, 20.692646, 2.083333], [5.0, 20.692646, 2.083333]]}, {"shapeName": "L_loLeg_shaper_01_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.945745, 21.28382, -3.000766], [5.0, 21.337712, -2.9945], [5.054255, 21.28382, -3.000766], [5.0, 21.229928, -3.007033], [4.945745, 21.28382, -3.000766], [5.0, 21.290086, -3.054653], [5.054255, 21.28382, -3.000766], [5.0, 21.277554, -2.946875], [5.0, 21.337712, -2.9945], [5.0, 21.290086, -3.054653], [5.0, 21.229928, -3.007033], [5.0, 21.277554, -2.946875], [4.945745, 21.28382, -3.000766], [5.0, 21.290086, -3.054653], [5.0, 20.692646, 2.083333]]}]},
			"L_lwrArmTwist_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lwrArmTwist_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[50.931335, 91.905693, -3.29628], [49.508431, 91.905693, -4.313174], [50.761645, 91.905693, -5.634365], [52.318459, 91.905693, -6.590797], [54.064498, 91.905693, -7.116423], [55.886663, 91.905693, -7.184587], [57.662965, 91.905693, -6.774989], [59.267619, 91.905693, -5.937216], [60.588811, 91.905693, -4.684002], [61.545243, 91.905693, -3.127188], [62.070869, 91.905693, -1.38115], [62.139033, 91.905693, 0.441015], [61.729435, 91.905693, 2.217317], [60.891662, 91.905693, 3.821972], [59.638449, 91.905693, 5.143163], [58.081634, 91.905693, 6.099596], [56.335596, 91.905693, 6.625221], [54.513431, 91.905693, 6.693386], [52.737128, 91.905693, 6.283788], [51.132473, 91.905693, 5.446015], [50.05838, 91.905693, 6.948957], [47.181658, 91.905693, 1.480527], [53.267949, 91.905693, 2.457916], [52.149367, 91.905693, 4.023111], [53.351269, 91.905693, 4.653664], [54.679049, 91.905693, 4.957685], [56.051388, 91.905693, 4.917364], [57.362826, 91.905693, 4.511073], [58.529482, 91.905693, 3.799785], [59.468758, 91.905693, 2.805079], [60.099311, 91.905693, 1.603176], [60.403332, 91.905693, 0.275397], [60.363011, 91.905693, -1.096943], [59.95672, 91.905693, -2.40838], [59.245432, 91.905693, -3.575036], [58.250727, 91.905693, -4.514313], [57.048824, 91.905693, -5.144866], [55.721044, 91.905693, -5.448886], [54.348705, 91.905693, -5.408565], [53.037267, 91.905693, -5.002275], [51.870611, 91.905693, -4.290986], [50.931335, 91.905693, -3.29628]]}]},
			"R_loLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_loLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-5.0, 19.185613, 1.962717], [-4.945745, 19.191879, 1.908826], [-5.0, 19.198146, 1.854934], [-5.054255, 19.191879, 1.908826], [-5.0, 19.185613, 1.962717], [-5.0, 19.137992, 1.90256], [-5.0, 19.198146, 1.854934], [-5.0, 19.245771, 1.915092], [-4.945745, 19.191879, 1.908826], [-5.0, 19.137992, 1.90256], [-5.054255, 19.191879, 1.908826], [-5.0, 19.245771, 1.915092], [-5.0, 19.185613, 1.962717], [-5.0, 19.137992, 1.90256], [-5.0, 24.275979, 2.5]]}, {"shapeName": "R_loLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.118355, 24.269712, 2.553892], [0.118355, 24.329871, 2.506266], [0.118355, 24.282245, 2.446108], [0.118355, 24.222087, 2.493734], [0.118355, 24.269712, 2.553892], [0.172605, 24.275979, 2.5], [0.118355, 24.282245, 2.446108], [0.0641, 24.275979, 2.5], [0.118355, 24.329871, 2.506266], [0.172605, 24.275979, 2.5], [0.118355, 24.222087, 2.493734], [0.0641, 24.275979, 2.5], [0.118355, 24.269712, 2.553892], [0.172605, 24.275979, 2.5], [-5.0, 24.275979, 2.5]]}, {"shapeName": "R_loLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.945745, 24.867153, -2.5841], [-5.0, 24.921045, -2.577833], [-5.054255, 24.867153, -2.5841], [-5.0, 24.813261, -2.590366], [-4.945745, 24.867153, -2.5841], [-5.0, 24.873419, -2.637987], [-5.054255, 24.867153, -2.5841], [-5.0, 24.860887, -2.530208], [-5.0, 24.921045, -2.577833], [-5.0, 24.873419, -2.637987], [-5.0, 24.813261, -2.590366], [-5.0, 24.860887, -2.530208], [-4.945745, 24.867153, -2.5841], [-5.0, 24.873419, -2.637987], [-5.0, 24.275979, 2.5]]}]},
			"L_toe_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.567224, 1.843203, 5.0], [5.0, 2.492367, 5.0], [3.432776, 1.843203, 5.0], [2.783612, 0.275979, 5.0], [3.432776, -1.291245, 5.0], [5.0, -1.940409, 5.0], [6.567224, -1.291245, 5.0], [7.216388, 0.275979, 5.0]]}]},
			"L_wristFk_CTL": {"color": 6, "shapes": [{"shapeName": "L_wristFk_CTLShape", "degree": 1, "form": 0, "points": [[57.75, 94.350166, 2.5], [52.75, 94.350166, 2.5], [52.75, 94.350166, -2.5], [57.75, 94.350166, -2.5], [57.75, 89.350166, -2.5], [52.75, 89.350166, -2.5], [52.75, 89.350166, 2.5], [57.75, 89.350166, 2.5], [57.75, 94.350166, 2.5], [57.75, 94.350166, -2.5], [52.75, 94.350166, -2.5], [52.75, 89.350166, -2.5], [57.75, 89.350166, -2.5], [57.75, 89.350166, 2.5], [52.75, 89.350166, 2.5], [52.75, 94.350166, 2.5]]}]},
		}

		controlShapes.set_data(data)