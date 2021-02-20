# -*- rigBot: assembly -*-
from rigBot import guide
from rigBot.data import controlShapes
import maya.cmds as mc

class GenericBiped():
	"""Generated assembly build."""

	def __init__(self):
		pass

	def build_guide(self):
		"""Build Assembly guide parts"""

		guide.build("worldRoot", **{'side': u'C', 'name': u''})
		guide.build("hand", **{'createIkCtrls': False, 'parent': u'R_wrist_end_JNT', 'numberFingers': 4, 'createThumb': True, 'pickWalkParent': u'R_arm_IK_CTL', 'numberThumbJoints': 3, 'numberJoints': 4, 'side': u'R', 'name': u''})
		guide.build("foot", **{'name': u'', 'parent': u'R_leg_end_JNT', 'switchCtrlDriver': u'R_leg_IK_switch_CTL', 'attrCtrlDriver': u'R_leg_IK_CTL', 'ikCtrlParent': u'R_leg_IK_handle_driver_JNT', 'pickWalkParent': u'R_leg_PV_CTL', 'fkCtrlParent': u'R_legEnd_FK_CTL', 'side': u'R'})
		guide.build("bipedLeg", **{'flipJoints': False, 'name': u'', 'parent': u'C_hip_JNT', 'transOrientiation': u'world', 'fkAnkleJoint': u'R_ankle_JNT', 'side': u'R', 'pickWalkParent': u'C_hip_CTL', 'ikHandleParent': u'R_foot_IK_handle_driver_JNT', 'numberTwistJoints': 4, 'makeBendy': False})
		guide.build("bipedArm", **{'name': u'', 'parent': u'C_chest_JNT', 'transOrientiation': u'world', 'numberTwistJoints': 4, 'side': u'R', 'pickWalkParent': u'C_chest_CTL', 'doubleClavicle': False, 'ikHandleParent': u'', 'makeBendy': False})
		guide.build("hand", **{'createIkCtrls': False, 'parent': u'L_wrist_end_JNT', 'numberFingers': 4, 'createThumb': True, 'pickWalkParent': u'L_arm_IK_CTL', 'numberThumbJoints': 3, 'numberJoints': 4, 'side': u'L', 'name': u''})
		guide.build("foot", **{'name': u'', 'parent': u'L_leg_end_JNT', 'switchCtrlDriver': u'L_leg_IK_switch_CTL', 'attrCtrlDriver': u'L_leg_IK_CTL', 'ikCtrlParent': u'L_leg_IK_handle_driver_JNT', 'pickWalkParent': u'L_leg_PV_CTL', 'fkCtrlParent': u'L_legEnd_FK_CTL', 'side': u'L'})
		guide.build("bipedLeg", **{'flipJoints': False, 'name': u'', 'parent': u'C_hip_JNT', 'transOrientiation': u'world', 'fkAnkleJoint': u'L_ankle_JNT', 'side': u'L', 'pickWalkParent': u'C_hip_CTL', 'ikHandleParent': u'L_foot_IK_handle_driver_JNT', 'numberTwistJoints': 4, 'makeBendy': False})
		guide.build("bipedArm", **{'name': u'', 'parent': u'C_chest_JNT', 'transOrientiation': u'world', 'numberTwistJoints': 4, 'side': u'L', 'pickWalkParent': u'C_chest_CTL', 'doubleClavicle': False, 'ikHandleParent': u'', 'makeBendy': False})
		guide.build("torso", **{'numberMidCtrls': 1, 'parent': u'C_root_JNT', 'pickWalkParent': u'world_CTL', 'numberJoints': 6, 'side': u'C', 'name': u''})
		guide.build("neck", **{'numberMidCtrls': 1, 'parent': u'C_chest_end_JNT', 'pickWalkParent': u'C_chest_CTL', 'createReverseJaw': True, 'name': u'', 'numberJoints': 4, 'side': u'C', 'createJaw': True})

		#Position nodes
		if mc.objExists("R_hand_guide"):
			if not mc.getAttr("R_hand_guide.rotateOrder", l=1):
				mc.setAttr("R_hand_guide.rotateOrder", 0)

			mc.xform("R_hand_guide", a=1, t=[-28.859733261823084, 50.74115888405891, -5.190266608043957])
			mc.xform("R_hand_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_hand_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("R_foot_guide"):
			if not mc.getAttr("R_foot_guide.rotateOrder", l=1):
				mc.setAttr("R_foot_guide.rotateOrder", 0)

			mc.xform("R_foot_guide", a=1, t=[-4.917319808751925, 3.6814505266971764, -2.8441600526935944])
			mc.xform("R_foot_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_foot_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("R_bipedLeg_guide"):
			if not mc.getAttr("R_bipedLeg_guide.rotateOrder", l=1):
				mc.setAttr("R_bipedLeg_guide.rotateOrder", 0)

			mc.xform("R_bipedLeg_guide", a=1, t=[-4.917319808751925, 44.851819680009186, -2.6148695633410473])
			mc.xform("R_bipedLeg_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_bipedLeg_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("R_bipedArm_guide"):
			if not mc.getAttr("R_bipedArm_guide.rotateOrder", l=1):
				mc.setAttr("R_bipedArm_guide.rotateOrder", 0)

			mc.xform("R_bipedArm_guide", a=1, t=[-2.07712179163699, 72.20563446859525, -0.6081527497044402])
			mc.xform("R_bipedArm_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_bipedArm_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("L_hand_guide"):
			if not mc.getAttr("L_hand_guide.rotateOrder", l=1):
				mc.setAttr("L_hand_guide.rotateOrder", 0)

			mc.xform("L_hand_guide", a=1, t=[28.859708820810138, 50.74101742936547, -5.1902765419050825])
			mc.xform("L_hand_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_hand_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("L_foot_guide"):
			if not mc.getAttr("L_foot_guide.rotateOrder", l=1):
				mc.setAttr("L_foot_guide.rotateOrder", 0)

			mc.xform("L_foot_guide", a=1, t=[4.917318122755149, 3.6814524830910815, -2.844158254131606])
			mc.xform("L_foot_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_foot_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("L_bipedLeg_guide"):
			if not mc.getAttr("L_bipedLeg_guide.rotateOrder", l=1):
				mc.setAttr("L_bipedLeg_guide.rotateOrder", 0)

			mc.xform("L_bipedLeg_guide", a=1, t=[4.917318122755149, 44.851819108535835, -2.6148710202221257])
			mc.xform("L_bipedLeg_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bipedLeg_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("L_bipedArm_guide"):
			if not mc.getAttr("L_bipedArm_guide.rotateOrder", l=1):
				mc.setAttr("L_bipedArm_guide.rotateOrder", 0)

			mc.xform("L_bipedArm_guide", a=1, t=[2.077120470330445, 72.20574828202497, -0.6081513907633669])
			mc.xform("L_bipedArm_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bipedArm_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("C_worldRoot_guide"):
			if not mc.getAttr("C_worldRoot_guide.rotateOrder", l=1):
				mc.setAttr("C_worldRoot_guide.rotateOrder", 0)

			mc.xform("C_worldRoot_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", r=1, s=[0.49279049485814785, 0.49279049485814785, 0.49279049485814785])

		if mc.objExists("C_torso_guide"):
			if not mc.getAttr("C_torso_guide.rotateOrder", l=1):
				mc.setAttr("C_torso_guide.rotateOrder", 0)

			mc.xform("C_torso_guide", a=1, t=[-7.1008912627598195e-16, 49.862264359577914, -4.254736127513328])
			mc.xform("C_torso_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_guide", r=1, s=[3.0, 3.0, 3.0])

		if mc.objExists("C_neck_guide"):
			if not mc.getAttr("C_neck_guide.rotateOrder", l=1):
				mc.setAttr("C_neck_guide.rotateOrder", 0)

			mc.xform("C_neck_guide", a=1, t=[6.482678256488929e-15, 74.68460417978997, -4.047577507305563])
			mc.xform("C_neck_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("C_root_JNT_PLC"):
			mc.xform("C_root_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_root_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_root_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_B_JNT_PLC"):
			mc.xform("C_torso_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_C_JNT_PLC"):
			mc.xform("C_torso_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_D_JNT_PLC"):
			mc.xform("C_torso_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_E_JNT_PLC"):
			mc.xform("C_torso_E_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_hip_JNT_PLC"):
			if not mc.getAttr("C_hip_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_hip_JNT_PLC.rotateOrder", 0)

			mc.xform("C_hip_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_hip_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_hip_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_A_JNT_PLC"):
			if not mc.getAttr("C_torso_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_torso_A_JNT_PLC.rotateOrder", 0)

			mc.xform("C_torso_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torsoSpline_B_JNT_PLC"):
			if not mc.getAttr("C_torsoSpline_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_torsoSpline_B_JNT_PLC.rotateOrder", 0)

			mc.xform("C_torsoSpline_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torsoSpline_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torsoSpline_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torsoSpline_C_JNT_PLC"):
			if not mc.getAttr("C_torsoSpline_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_torsoSpline_C_JNT_PLC.rotateOrder", 0)

			mc.xform("C_torsoSpline_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torsoSpline_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torsoSpline_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_end_JNT_PLC"):
			if not mc.getAttr("C_chest_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_chest_end_JNT_PLC.rotateOrder", 0)

			mc.xform("C_chest_end_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_JNT_PLC"):
			if not mc.getAttr("C_chest_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_chest_JNT_PLC.rotateOrder", 0)

			mc.xform("C_chest_JNT_PLC", a=1, t=[-0.6596849547266039, -9.880514504974936e-16, 2.220446049250313e-16])
			mc.xform("C_chest_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_JNT_PLC"):
			if not mc.getAttr("L_shoulder_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_shoulder_JNT_PLC.rotateOrder", 0)

			mc.xform("L_shoulder_JNT_PLC", a=1, t=[-0.5000000000000002, -1.7763568394002505e-15, -1.3877787807814457e-17])
			mc.xform("L_shoulder_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_JNT_PLC"):
			if not mc.getAttr("L_upArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_JNT_PLC", a=1, t=[-0.48585710334820176, -0.12598731599957702, -0.8688021255559516])
			mc.xform("L_upArm_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_JNT_PLC"):
			if not mc.getAttr("L_loArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_JNT_PLC", a=1, t=[-0.5903273662622861, -2.1609994115216242, -1.0164574812185836])
			mc.xform("L_loArm_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_JNT_PLC"):
			if not mc.getAttr("L_wrist_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_wrist_JNT_PLC.rotateOrder", 0)

			mc.xform("L_wrist_JNT_PLC", a=1, t=[-0.643482329904062, -4.292946170531902, -0.9164250302283431])
			mc.xform("L_wrist_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_end_JNT_PLC"):
			if not mc.getAttr("L_wrist_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_wrist_end_JNT_PLC.rotateOrder", 0)

			mc.xform("L_wrist_end_JNT_PLC", a=1, t=[-0.7867325704123322, -4.6574010450761385, -0.7698881716317896])
			mc.xform("L_wrist_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_handle_driver_JNT_PLC"):
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_A_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_A_JNT_PLC", a=1, t=[1.8932488440689814, -0.5329897351039872, -0.9983331966884782])
			mc.xform("L_upArm_twist_A_JNT_PLC", a=1, ro=[1.3184189669993067, 13.109417753283854, -47.03239111102201])
			mc.xform("L_upArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_A_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_A_JNT_PLC", a=1, t=[3.7990416410093593, -2.5873887633236805, -1.3964509910205354])
			mc.xform("L_loArm_twist_A_JNT_PLC", a=1, ro=[1.311496672220622, -11.740731295960698, -47.59838608135104])
			mc.xform("L_loArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_B_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_B_JNT_PLC", a=1, t=[2.2723547914861646, -0.9399921542083973, -1.1278642678210045])
			mc.xform("L_upArm_twist_B_JNT_PLC", a=1, ro=[1.3184189669993067, 13.109417753283854, -47.03239111102201])
			mc.xform("L_upArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_B_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_B_JNT_PLC", a=1, t=[4.188410648281004, -3.013778115125737, -1.2764445008224874])
			mc.xform("L_loArm_twist_B_JNT_PLC", a=1, ro=[1.311496672220622, -11.740731295960698, -47.59838608135104])
			mc.xform("L_loArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_C_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_C_JNT_PLC", a=1, t=[2.651460738903348, -1.3469945733128075, -1.2573953389535308])
			mc.xform("L_upArm_twist_C_JNT_PLC", a=1, ro=[1.3184189669993067, 13.109417753283854, -47.03239111102201])
			mc.xform("L_upArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_C_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_C_JNT_PLC", a=1, t=[4.577779655552649, -3.440167466927793, -1.1564380106244392])
			mc.xform("L_loArm_twist_C_JNT_PLC", a=1, ro=[1.311496672220622, -11.740731295960698, -47.59838608135104])
			mc.xform("L_loArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_D_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_D_JNT_PLC", a=1, t=[3.0305666863205314, -1.7539969924172158, -1.3869264100860572])
			mc.xform("L_upArm_twist_D_JNT_PLC", a=1, ro=[1.3184189669993067, 13.109417753283854, -47.03239111102201])
			mc.xform("L_upArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_D_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_D_JNT_PLC", a=1, t=[4.967148662824294, -3.8665568187298494, -1.0364315204263912])
			mc.xform("L_loArm_twist_D_JNT_PLC", a=1, ro=[1.311496672220622, -11.740731295960698, -47.59838608135104])
			mc.xform("L_loArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_JNT_PLC"):
			if not mc.getAttr("L_upLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_JNT_PLC"):
			if not mc.getAttr("L_loLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_JNT_PLC", a=1, t=[0.0, 0.13264695346405464, 0.13176933639498625])
			mc.xform("L_loLeg_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_end_JNT_PLC"):
			if not mc.getAttr("L_leg_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_leg_end_JNT_PLC.rotateOrder", 0)

			mc.xform("L_leg_end_JNT_PLC", a=1, t=[0.0, -0.23407332508895062, -0.04585744678189607])
			mc.xform("L_leg_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_handle_driver_JNT_PLC"):
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_A_JNT_PLC", a=1, t=[3.3306690738754696e-16, -0.773470609307191, 0.12635386727899728])
			mc.xform("L_upLeg_twist_A_JNT_PLC", a=1, ro=[179.99999999999994, -9.277865361801467, -89.99999999999997])
			mc.xform("L_upLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_A_JNT_PLC", a=1, t=[3.3306690738754696e-16, -4.740697102246548, 0.4962439797596099])
			mc.xform("L_loLeg_twist_A_JNT_PLC", a=1, ro=[-5.088887490341627e-14, 171.1792071530017, 90.00000000000001])
			mc.xform("L_loLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_B_JNT_PLC", a=1, t=[1.1102230246251565e-16, -1.5469412186143794, 0.2527077345579946])
			mc.xform("L_upLeg_twist_B_JNT_PLC", a=1, ro=[179.99999999999994, -9.277865361801467, -89.99999999999997])
			mc.xform("L_upLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_B_JNT_PLC", a=1, t=[1.1102230246251565e-16, -5.614041157957149, 0.36071862312423336])
			mc.xform("L_loLeg_twist_B_JNT_PLC", a=1, ro=[-5.088887490341627e-14, 171.1792071530017, 90.00000000000001])
			mc.xform("L_loLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_C_JNT_PLC", a=1, t=[1.1102230246251565e-16, -2.3204118279215686, 0.3790616018369919])
			mc.xform("L_upLeg_twist_C_JNT_PLC", a=1, ro=[179.99999999999994, -9.277865361801467, -89.99999999999997])
			mc.xform("L_upLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_C_JNT_PLC", a=1, t=[1.1102230246251565e-16, -6.487385213667751, 0.22519326648885685])
			mc.xform("L_loLeg_twist_C_JNT_PLC", a=1, ro=[-5.088887490341627e-14, 171.1792071530017, 90.00000000000001])
			mc.xform("L_loLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_D_JNT_PLC", a=1, t=[1.1102230246251565e-16, -3.093882437228758, 0.5054154691159891])
			mc.xform("L_upLeg_twist_D_JNT_PLC", a=1, ro=[179.99999999999994, -9.277865361801467, -89.99999999999997])
			mc.xform("L_upLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_D_JNT_PLC", a=1, t=[1.1102230246251565e-16, -7.360729269378352, 0.08966790985348039])
			mc.xform("L_loLeg_twist_D_JNT_PLC", a=1, ro=[-5.088887490341627e-14, 171.1792071530017, 90.00000000000001])
			mc.xform("L_loLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_heel_JNT_PLC"):
			if not mc.getAttr("L_heel_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_heel_JNT_PLC.rotateOrder", 0)

			mc.xform("L_heel_JNT_PLC", a=1, t=[-0.015697564650681395, -0.13868500988745192, -0.23252253800341505])
			mc.xform("L_heel_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_heel_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_innerBall_JNT_PLC"):
			if not mc.getAttr("L_innerBall_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_innerBall_JNT_PLC.rotateOrder", 0)

			mc.xform("L_innerBall_JNT_PLC", a=1, t=[0.04480497932600061, -0.04704048132995648, 0.3097796082687339])
			mc.xform("L_innerBall_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_innerBall_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterBall_JNT_PLC"):
			if not mc.getAttr("L_outterBall_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_outterBall_JNT_PLC.rotateOrder", 0)

			mc.xform("L_outterBall_JNT_PLC", a=1, t=[0.02271238841571943, -0.09504164637598703, -0.001935983239099992])
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

			mc.xform("L_ball_JNT_PLC", a=1, t=[0.3035925163041486, 1.7763568394002505e-15, 0.07194024733008099])
			mc.xform("L_ball_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ball_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_JNT_PLC"):
			if not mc.getAttr("L_toe_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_toe_JNT_PLC.rotateOrder", 0)

			mc.xform("L_toe_JNT_PLC", a=1, t=[-0.020213801538847692, 0.0024838412508245947, 0.08820502043108616])
			mc.xform("L_toe_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

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

			mc.xform("L_thumb_A_JNT_PLC", a=1, t=[-0.41403273538914576, -0.13288117519071174, 0.10777281553806972])
			mc.xform("L_thumb_A_JNT_PLC", a=1, ro=[-41.9565908023595, -58.80108123374745, 35.139903061139876])
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

			mc.xform("L_index_A_JNT_PLC", a=1, t=[-0.0004704422608465819, -0.1725458861663327, -0.15518767545607526])
			mc.xform("L_index_A_JNT_PLC", a=1, ro=[5.6583928521657105, -16.21319612232616, -48.07312064095242])
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

			mc.xform("L_middle_A_JNT_PLC", a=1, t=[-0.038298440798316236, -0.1478509729739912, 0.2027981303090336])
			mc.xform("L_middle_A_JNT_PLC", a=1, ro=[17.0936718840093, -29.695891256926767, -52.56674322415862])
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

			mc.xform("L_ring_A_JNT_PLC", a=1, t=[0.025670790037010782, -0.19581906763194645, 0.175441035359855])
			mc.xform("L_ring_A_JNT_PLC", a=1, ro=[1.3110939993576882, -8.988731512360912, -46.91605945953415])
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

			mc.xform("L_pinky_A_JNT_PLC", a=1, t=[-2.6645352591003757e-15, -1.7763568394002505e-15, 4.440892098500626e-16])
			mc.xform("L_pinky_A_JNT_PLC", a=1, ro=[7.951386703658794e-16, 3.1805546814635168e-15, 6.410805529824901e-15])
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

			mc.xform("C_head_end_JNT_PLC", a=1, t=[9.48585776191384e-16, -1.2789027284684487, 0.014375139596625841])
			mc.xform("C_head_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_jaw_end_JNT_PLC"):
			if not mc.getAttr("C_jaw_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_jaw_end_JNT_PLC.rotateOrder", 0)

			mc.xform("C_jaw_end_JNT_PLC", a=1, t=[4.549876437874272e-16, -0.6379619560773993, -1.2911528541172712])
			mc.xform("C_jaw_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_jaw_JNT_PLC"):
			if not mc.getAttr("C_jaw_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_jaw_JNT_PLC.rotateOrder", 0)

			mc.xform("C_jaw_JNT_PLC", a=1, t=[-1.552469208887478e-15, 0.14675053232398838, -0.3952540457648552])
			mc.xform("C_jaw_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_JNT_PLC"):
			if not mc.getAttr("C_head_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_head_JNT_PLC.rotateOrder", 0)

			mc.xform("C_head_JNT_PLC", a=1, t=[-0.7560363573537927, -2.5593355758969324e-16, 0.31983775051818264])
			mc.xform("C_head_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_reverseJaw_JNT_PLC"):
			mc.xform("C_reverseJaw_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_B_JNT_PLC"):
			if not mc.getAttr("R_thumb_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_B_JNT_PLC", a=1, t=[-2.4139118876220778e-05, 3.278245156224102e-05, -8.184739626493354e-06])
			mc.xform("R_thumb_B_JNT_PLC", a=1, ro=[7.633331235512438e-14, 3.1805546814635174e-14, -2.862499213317162e-14])
			mc.xform("R_thumb_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_C_JNT_PLC"):
			if not mc.getAttr("R_thumb_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_C_JNT_PLC", a=1, t=[-2.5591455271367636e-05, 3.240036635343557e-05, -1.2416740671206128e-05])
			mc.xform("R_thumb_C_JNT_PLC", a=1, ro=[7.633331235512438e-14, 3.1805546814635174e-14, -2.862499213317162e-14])
			mc.xform("R_thumb_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_D_JNT_PLC"):
			if not mc.getAttr("R_thumb_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_D_JNT_PLC", a=1, t=[-2.5917919188600536e-05, 3.338421064924546e-05, -1.3217015552235978e-05])
			mc.xform("R_thumb_D_JNT_PLC", a=1, ro=[7.633331235512438e-14, 3.1805546814635174e-14, -2.862499213317162e-14])
			mc.xform("R_thumb_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_A_JNT_PLC"):
			if not mc.getAttr("R_thumb_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_A_JNT_PLC", a=1, t=[0.518976938662445, 0.4006181768671997, -0.41577506305604395])
			mc.xform("R_thumb_A_JNT_PLC", a=1, ro=[-41.956590802359585, -58.801081233747446, -144.86009693886007])
			mc.xform("R_thumb_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_B_JNT_PLC"):
			if not mc.getAttr("R_index_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_B_JNT_PLC", a=1, t=[5.083182377241258e-07, -7.694326704665855e-07, -6.152019300653677e-07])
			mc.xform("R_index_B_JNT_PLC", a=1, ro=[-1.9878466759146977e-14, 6.361109362927035e-15, 1.2722218725854064e-14])
			mc.xform("R_index_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_C_JNT_PLC"):
			if not mc.getAttr("R_index_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_C_JNT_PLC", a=1, t=[6.128466750521255e-06, 5.943480550385516e-06, -2.6602977423184626e-06])
			mc.xform("R_index_C_JNT_PLC", a=1, ro=[-1.9878466759146977e-14, 6.361109362927035e-15, 1.2722218725854064e-14])
			mc.xform("R_index_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_D_JNT_PLC"):
			if not mc.getAttr("R_index_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_D_JNT_PLC", a=1, t=[9.64293875416189e-07, 6.360777584646371e-06, -1.6093181718357386e-06])
			mc.xform("R_index_D_JNT_PLC", a=1, ro=[-1.9878466759146977e-14, 6.361109362927035e-15, 1.2722218725854064e-14])
			mc.xform("R_index_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_E_JNT_PLC"):
			if not mc.getAttr("R_index_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_E_JNT_PLC", a=1, t=[1.6294663720550773e-06, 3.8949090175322e-07, -8.235602770856332e-07])
			mc.xform("R_index_E_JNT_PLC", a=1, ro=[-1.9878466759146977e-14, 6.361109362927035e-15, 1.2722218725854064e-14])
			mc.xform("R_index_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_A_JNT_PLC"):
			if not mc.getAttr("R_index_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_A_JNT_PLC", a=1, t=[0.4995293949763724, -0.1725752312993265, -0.3448099344677389])
			mc.xform("R_index_A_JNT_PLC", a=1, ro=[5.658392852165729, -16.213196122326153, 131.92687935904758])
			mc.xform("R_index_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_B_JNT_PLC"):
			if not mc.getAttr("R_middle_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_B_JNT_PLC", a=1, t=[-3.053310724965286e-05, 2.3500988822533486e-05, 1.081077309561529e-05])
			mc.xform("R_middle_B_JNT_PLC", a=1, ro=[-3.657637883683043e-14, -6.361109362927041e-15, -2.5444437451708128e-14])
			mc.xform("R_middle_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_C_JNT_PLC"):
			if not mc.getAttr("R_middle_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_C_JNT_PLC", a=1, t=[-3.396568940416955e-05, 2.5251084444732896e-05, 1.292596689550507e-05])
			mc.xform("R_middle_C_JNT_PLC", a=1, ro=[-3.657637883683043e-14, -6.361109362927041e-15, -2.5444437451708128e-14])
			mc.xform("R_middle_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_D_JNT_PLC"):
			if not mc.getAttr("R_middle_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_D_JNT_PLC", a=1, t=[-3.0748356766086005e-05, 2.3042296394493178e-05, 1.1085359504336978e-05])
			mc.xform("R_middle_D_JNT_PLC", a=1, ro=[-3.657637883683043e-14, -6.361109362927041e-15, -2.5444437451708128e-14])
			mc.xform("R_middle_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_E_JNT_PLC"):
			if not mc.getAttr("R_middle_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_E_JNT_PLC", a=1, t=[-2.7672506711873268e-05, 2.65201777835955e-05, 8.246880771167753e-06])
			mc.xform("R_middle_E_JNT_PLC", a=1, ro=[-3.657637883683043e-14, -6.361109362927041e-15, -2.5444437451708128e-14])
			mc.xform("R_middle_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_A_JNT_PLC"):
			if not mc.getAttr("R_middle_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_A_JNT_PLC", a=1, t=[0.4616929407811634, -0.14783714845744633, -0.20279610118699432])
			mc.xform("R_middle_A_JNT_PLC", a=1, ro=[17.093671884009307, -29.695891256926767, 127.43325677584139])
			mc.xform("R_middle_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_B_JNT_PLC"):
			if not mc.getAttr("R_ring_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_B_JNT_PLC", a=1, t=[-3.011109297901271e-06, 1.018276896935788e-05, 4.013255153534345e-06])
			mc.xform("R_ring_B_JNT_PLC", a=1, ro=[2.385416011097637e-15, -3.9725156682451414e-31, 1.9083328088781097e-14])
			mc.xform("R_ring_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_C_JNT_PLC"):
			if not mc.getAttr("R_ring_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_C_JNT_PLC", a=1, t=[-4.6936845721212705e-06, 7.744465579051507e-06, -4.893983951426151e-07])
			mc.xform("R_ring_C_JNT_PLC", a=1, ro=[2.385416011097637e-15, -3.9725156682451414e-31, 1.9083328088781097e-14])
			mc.xform("R_ring_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_D_JNT_PLC"):
			if not mc.getAttr("R_ring_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_D_JNT_PLC", a=1, t=[-1.24493392483771e-05, 9.547219740113633e-06, 3.025301531622837e-06])
			mc.xform("R_ring_D_JNT_PLC", a=1, ro=[2.385416011097637e-15, -3.9725156682451414e-31, 1.9083328088781097e-14])
			mc.xform("R_ring_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_E_JNT_PLC"):
			if not mc.getAttr("R_ring_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_E_JNT_PLC", a=1, t=[-1.1149026680090657e-05, 6.057096110012594e-06, 3.6203820013014365e-06])
			mc.xform("R_ring_E_JNT_PLC", a=1, ro=[2.385416011097637e-15, -3.9725156682451414e-31, 1.9083328088781097e-14])
			mc.xform("R_ring_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_A_JNT_PLC"):
			if not mc.getAttr("R_ring_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_A_JNT_PLC", a=1, t=[0.5256670028236483, -0.1958349426566297, 0.3245592018720377])
			mc.xform("R_ring_A_JNT_PLC", a=1, ro=[1.3110939993576616, -8.988731512360912, 133.08394054046585])
			mc.xform("R_ring_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_B_JNT_PLC"):
			if not mc.getAttr("R_pinky_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_B_JNT_PLC", a=1, t=[-3.7107771513333887e-06, 3.104382138552353e-05, -2.220446049250313e-16])
			mc.xform("R_pinky_B_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_pinky_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_C_JNT_PLC"):
			if not mc.getAttr("R_pinky_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_C_JNT_PLC", a=1, t=[-7.421554305331313e-06, 6.938173400783398e-05, -2.220446049250313e-16])
			mc.xform("R_pinky_C_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_pinky_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_D_JNT_PLC"):
			if not mc.getAttr("R_pinky_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_D_JNT_PLC", a=1, t=[-1.2765215622323467e-06, 3.104382138552353e-05, -2.220446049250313e-16])
			mc.xform("R_pinky_D_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_pinky_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_E_JNT_PLC"):
			if not mc.getAttr("R_pinky_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_E_JNT_PLC", a=1, t=[-4.987298715342092e-06, 0.0, -2.220446049250313e-16])
			mc.xform("R_pinky_E_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_pinky_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_A_JNT_PLC"):
			if not mc.getAttr("R_pinky_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_A_JNT_PLC", a=1, t=[0.4999926180415386, -1.7763568394002505e-15, 1.0000049477028714])
			mc.xform("R_pinky_A_JNT_PLC", a=1, ro=[7.016709298534876e-15, -7.016709298534876e-15, 180.0])
			mc.xform("R_pinky_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_JNT_PLC"):
			if not mc.getAttr("R_upLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_JNT_PLC", a=1, t=[0.0, 0.0, -2.220446049250313e-16])
			mc.xform("R_upLeg_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_JNT_PLC"):
			if not mc.getAttr("R_loLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_JNT_PLC", a=1, t=[0.0, 7.867350812977464, -1.1317692413800229])
			mc.xform("R_loLeg_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_loLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_end_JNT_PLC"):
			if not mc.getAttr("R_leg_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_leg_end_JNT_PLC.rotateOrder", 0)

			mc.xform("R_leg_end_JNT_PLC", a=1, t=[0.0, 16.234073830662403, 0.04585809787050832])
			mc.xform("R_leg_end_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_leg_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_handle_driver_JNT_PLC"):
			mc.xform("R_leg_IK_handle_driver_JNT_PLC", a=1, t=[4.551914400963142e-15, -1.1102230246251565e-16, -8.881784197001252e-16])
			mc.xform("R_leg_IK_handle_driver_JNT_PLC", a=1, ro=[5.565970498915388e-15, 1.678634365549842e-06, -1.3219180313297687e-14])
			mc.xform("R_leg_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_A_JNT_PLC", a=1, t=[0.0, 0.7734741049194529, -0.12635345404360881])
			mc.xform("R_upLeg_twist_A_JNT_PLC", a=1, ro=[180.0, -9.277865361801464, -89.99999999999997])
			mc.xform("R_upLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_A_JNT_PLC", a=1, t=[0.0, 4.740693839584868, -0.4962436749718176])
			mc.xform("R_loLeg_twist_A_JNT_PLC", a=1, ro=[0.0, -188.82079452563266, 90.0])
			mc.xform("R_loLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_B_JNT_PLC", a=1, t=[0.0, 1.546938354029006, -0.25270789366820723])
			mc.xform("R_upLeg_twist_B_JNT_PLC", a=1, ro=[180.0, -9.277865361801464, -89.99999999999997])
			mc.xform("R_upLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_B_JNT_PLC", a=1, t=[0.0, 5.614036866192272, -0.36071869991220623])
			mc.xform("R_loLeg_twist_B_JNT_PLC", a=1, ro=[0.0, -188.82079452563266, 90.0])
			mc.xform("R_loLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_C_JNT_PLC", a=1, t=[0.0, 2.320412458948459, -0.3790613477118158])
			mc.xform("R_upLeg_twist_C_JNT_PLC", a=1, ro=[180.0, -9.277865361801464, -89.99999999999997])
			mc.xform("R_upLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_C_JNT_PLC", a=1, t=[0.0, 6.487389748609573, -0.225193429178298])
			mc.xform("R_loLeg_twist_C_JNT_PLC", a=1, ro=[0.0, -188.82079452563266, 90.0])
			mc.xform("R_loLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_D_JNT_PLC", a=1, t=[0.0, 3.09388656386791, -0.5054151959878204])
			mc.xform("R_upLeg_twist_D_JNT_PLC", a=1, ro=[180.0, -9.277865361801464, -89.99999999999997])
			mc.xform("R_upLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_D_JNT_PLC", a=1, t=[0.0, 7.360732775216977, -0.08966717286339992])
			mc.xform("R_loLeg_twist_D_JNT_PLC", a=1, ro=[0.0, -188.82079452563266, 90.0])
			mc.xform("R_loLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_heel_JNT_PLC"):
			if not mc.getAttr("R_heel_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_heel_JNT_PLC.rotateOrder", 0)

			mc.xform("R_heel_JNT_PLC", a=1, t=[0.015698334004201064, 1.1386845703943667, 0.7325266544312423])
			mc.xform("R_heel_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_heel_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_innerBall_JNT_PLC"):
			if not mc.getAttr("R_innerBall_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_innerBall_JNT_PLC.rotateOrder", 0)

			mc.xform("R_innerBall_JNT_PLC", a=1, t=[0.9551955080054197, 1.0470398292751018, -2.3097799716355536])
			mc.xform("R_innerBall_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_innerBall_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_outterBall_JNT_PLC"):
			if not mc.getAttr("R_outterBall_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_outterBall_JNT_PLC.rotateOrder", 0)

			mc.xform("R_outterBall_JNT_PLC", a=1, t=[-1.022710762543955, 1.0950415657982444, -1.9980643585320426])
			mc.xform("R_outterBall_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_outterBall_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_foot_IK_handle_driver_JNT_PLC"):
			mc.xform("R_foot_IK_handle_driver_JNT_PLC", a=1, t=[-1.1102230246251565e-16, -1.1102230246251565e-16, 1.1102230246251565e-16])
			mc.xform("R_foot_IK_handle_driver_JNT_PLC", a=1, ro=[-7.31527668529508e-14, -2.5439890632513474e-05, 4.1347227099301365e-14])
			mc.xform("R_foot_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ankle_JNT_PLC"):
			if not mc.getAttr("R_ankle_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ankle_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ankle_JNT_PLC", a=1, t=[-1.1102230246251565e-16, 0.0, 0.0])
			mc.xform("R_ankle_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_ankle_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ball_JNT_PLC"):
			if not mc.getAttr("R_ball_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ball_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ball_JNT_PLC", a=1, t=[2.303592494182115, 0.0, 1.071939547399294])
			mc.xform("R_ball_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_ball_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_JNT_PLC"):
			if not mc.getAttr("R_toe_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_toe_JNT_PLC.rotateOrder", 0)

			mc.xform("R_toe_JNT_PLC", a=1, t=[3.979789755416568, -0.0024846496750746683, 1.0882045904725823])
			mc.xform("R_toe_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_toe_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_JNT_PLC"):
			if not mc.getAttr("R_shoulder_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_shoulder_JNT_PLC.rotateOrder", 0)

			mc.xform("R_shoulder_JNT_PLC", a=1, t=[-0.5, 0.0, 0.0])
			mc.xform("R_shoulder_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_shoulder_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upArm_JNT_PLC"):
			if not mc.getAttr("R_upArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upArm_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upArm_JNT_PLC", a=1, t=[-3.514146103339166, 0.12595725048574202, 0.8687994982448118])
			mc.xform("R_upArm_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loArm_JNT_PLC"):
			if not mc.getAttr("R_loArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loArm_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loArm_JNT_PLC", a=1, t=[-7.409674597620929, 2.1609848780519503, 2.016454334017081])
			mc.xform("R_loArm_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_loArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_JNT_PLC"):
			if not mc.getAttr("R_wrist_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_wrist_JNT_PLC.rotateOrder", 0)

			mc.xform("R_wrist_JNT_PLC", a=1, t=[-11.35652229403722, 4.292895116907269, 0.9164227716679028])
			mc.xform("R_wrist_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_wrist_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_end_JNT_PLC"):
			if not mc.getAttr("R_wrist_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_wrist_end_JNT_PLC.rotateOrder", 0)

			mc.xform("R_wrist_end_JNT_PLC", a=1, t=[-12.21326318907493, 4.657382678524151, 0.7698875756978735])
			mc.xform("R_wrist_end_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_wrist_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_handle_driver_JNT_PLC"):
			mc.xform("R_arm_IK_handle_driver_JNT_PLC", a=1, t=[6.217248937900877e-15, -5.329070518200751e-15, -8.881784197001252e-16])
			mc.xform("R_arm_IK_handle_driver_JNT_PLC", a=1, ro=[-0.00018674258456132816, 0.0001976143667748194, 0.003220103532081711])
			mc.xform("R_arm_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upArm_twist_A_JNT_PLC"):
			if not mc.getAttr("R_upArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upArm_twist_A_JNT_PLC", a=1, t=[-1.8932498310335386, 0.5330021992385721, 0.9983344077232246])
			mc.xform("R_upArm_twist_A_JNT_PLC", a=1, ro=[1.3184189669993065, 13.109417753283848, -47.032391111022015])
			mc.xform("R_upArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loArm_twist_A_JNT_PLC"):
			if not mc.getAttr("R_loArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loArm_twist_A_JNT_PLC", a=1, t=[-3.7990382234182483, 2.58734721420322, 1.3964499927092249])
			mc.xform("R_loArm_twist_A_JNT_PLC", a=1, ro=[1.3097247968060466, 348.25918607785405, -47.59785837487479])
			mc.xform("R_loArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upArm_twist_B_JNT_PLC"):
			if not mc.getAttr("R_upArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upArm_twist_B_JNT_PLC", a=1, t=[-2.272353558727912, 0.9399485898924329, 1.1278594613917399])
			mc.xform("R_upArm_twist_B_JNT_PLC", a=1, ro=[1.3184189669993065, 13.109417753283848, -47.032391111022015])
			mc.xform("R_upArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loArm_twist_B_JNT_PLC"):
			if not mc.getAttr("R_loArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loArm_twist_B_JNT_PLC", a=1, t=[-4.188411705025465, 3.0137095503544895, 1.2764456514013682])
			mc.xform("R_loArm_twist_B_JNT_PLC", a=1, ro=[1.3097247968060466, 348.25918607785405, -47.59785837487479])
			mc.xform("R_loArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upArm_twist_C_JNT_PLC"):
			if not mc.getAttr("R_upArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upArm_twist_C_JNT_PLC", a=1, t=[-2.6514572864222847, 1.346993538645263, 1.2573943708701527])
			mc.xform("R_upArm_twist_C_JNT_PLC", a=1, ro=[1.3184189669993065, 13.109417753283848, -47.032391111022015])
			mc.xform("R_upArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loArm_twist_C_JNT_PLC"):
			if not mc.getAttr("R_loArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loArm_twist_C_JNT_PLC", a=1, t=[-4.577775330822785, 3.44017044460473, 1.1564413100935123])
			mc.xform("R_loArm_twist_C_JNT_PLC", a=1, ro=[1.3097247968060466, 348.25918607785405, -47.59785837487479])
			mc.xform("R_loArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upArm_twist_D_JNT_PLC"):
			if not mc.getAttr("R_upArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upArm_twist_D_JNT_PLC", a=1, t=[-3.030570869926555, 1.7539399292991202, 1.3869292803485653])
			mc.xform("R_upArm_twist_D_JNT_PLC", a=1, ro=[1.3184189669993065, 13.109417753283848, -47.032391111022015])
			mc.xform("R_upArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loArm_twist_D_JNT_PLC"):
			if not mc.getAttr("R_loArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loArm_twist_D_JNT_PLC", a=1, t=[-4.967148812430002, 3.8665327807559997, 1.036427112975759])
			mc.xform("R_loArm_twist_D_JNT_PLC", a=1, ro=[1.3097247968060466, 348.25918607785405, -47.59785837487479])
			mc.xform("R_loArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_world_PIV_CTL"):
			mc.xform("C_world_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_world_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_world_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_visibility_PIV_CTL"):
			mc.xform("C_visibility_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_visibility_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_visibility_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("C_midTorso_PIV_CTL"):
			if not mc.getAttr("C_midTorso_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_midTorso_PIV_CTL.rotateOrder", 0)

			mc.xform("C_midTorso_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_FK_A_PIV_CTL"):
			mc.xform("C_torso_FK_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_FK_B_PIV_CTL"):
			mc.xform("C_torso_FK_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_FK_C_PIV_CTL"):
			mc.xform("C_torso_FK_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_FK_D_PIV_CTL"):
			mc.xform("C_torso_FK_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_FK_E_PIV_CTL"):
			mc.xform("C_torso_FK_E_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_E_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_E_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_FK_PIV_CTL"):
			mc.xform("C_chest_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_FK_PIV_CTL"):
			if not mc.getAttr("L_upArm_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upArm_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upArm_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_FK_PIV_CTL"):
			if not mc.getAttr("L_loArm_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loArm_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loArm_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_FK_PIV_CTL"):
			if not mc.getAttr("L_wrist_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_wrist_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("L_wrist_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_PIV_CTL"):
			if not mc.getAttr("L_arm_IK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_PIV_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_IK_PIV_CTL"):
			if not mc.getAttr("L_wrist_IK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_wrist_IK_PIV_CTL.rotateOrder", 0)

			mc.xform("L_wrist_IK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_PV_PIV_CTL"):
			mc.xform("L_arm_PV_PIV_CTL", a=1, t=[0.0, 0.0, -10.0])
			mc.xform("L_arm_PV_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_PV_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_PIV_CTL"):
			if not mc.getAttr("L_shoulder_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_PIV_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_switch_PIV_CTL"):
			if not mc.getAttr("L_arm_IK_switch_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_switch_PIV_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_switch_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("L_innerBall_PIV_CTL"):
			mc.xform("L_innerBall_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_innerBall_PIV_CTL", a=1, ro=[-1.174443956873162, 0.30746888225771474, -1.2423094673232448e-13])
			mc.xform("L_innerBall_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterBall_PIV_CTL"):
			mc.xform("L_outterBall_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterBall_PIV_CTL", a=1, ro=[-1.174443956873162, 0.30746888225771474, -1.2423094673232448e-13])
			mc.xform("L_outterBall_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_heel_PIV_CTL"):
			mc.xform("L_heel_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_heel_PIV_CTL", a=1, ro=[-1.174443956873162, 0.30746888225771474, -1.2423094673232448e-13])
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
			mc.xform("C_head_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
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

		if mc.objExists("C_jaw_PIV_CTL"):
			if not mc.getAttr("C_jaw_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_jaw_PIV_CTL.rotateOrder", 0)

			mc.xform("C_jaw_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_reverseJaw_PIV_CTL"):
			if not mc.getAttr("C_reverseJaw_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_reverseJaw_PIV_CTL.rotateOrder", 0)

			mc.xform("C_reverseJaw_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_FK_PIV_CTL"):
			mc.xform("C_head_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_A_PIV_CTL"):
			if not mc.getAttr("R_thumb_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_A_PIV_CTL", a=1, t=[-2.6645352591003757e-15, 3.552713678800501e-15, -1.7763568394002505e-15])
			mc.xform("R_thumb_A_PIV_CTL", a=1, ro=[-0.0002086781158524233, -0.00139118743820912, -179.9938807609068])
			mc.xform("R_thumb_A_PIV_CTL", r=1, s=[0.9999999999999999, 1.0, -0.9999999999999999])

		if mc.objExists("R_thumb_B_PIV_CTL"):
			if not mc.getAttr("R_thumb_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_B_PIV_CTL", a=1, t=[0.0, -8.881784197001252e-16, 8.881784197001252e-16])
			mc.xform("R_thumb_B_PIV_CTL", a=1, ro=[-5.0630023479762766e-05, -0.000727424284749828, 179.99993432531917])
			mc.xform("R_thumb_B_PIV_CTL", r=1, s=[1.0, 0.9999999999999999, -1.0])

		if mc.objExists("R_thumb_C_PIV_CTL"):
			if not mc.getAttr("R_thumb_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_C_PIV_CTL", a=1, t=[1.7763568394002505e-15, -2.6645352591003757e-15, 0.0])
			mc.xform("R_thumb_C_PIV_CTL", a=1, ro=[1.3769672919921032e-05, -0.00013603508450974386, -179.99984284316048])
			mc.xform("R_thumb_C_PIV_CTL", r=1, s=[1.0, 1.0000000000000002, -1.0])

		if mc.objExists("R_index_A_PIV_CTL"):
			if not mc.getAttr("R_index_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_A_PIV_CTL", a=1, t=[1.3322676295501878e-15, -1.7763568394002505e-15, -2.220446049250313e-16])
			mc.xform("R_index_A_PIV_CTL", a=1, ro=[-1.2422868701846574e-05, -9.317151583703996e-05, 179.99987431820134])
			mc.xform("R_index_A_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -1.0])

		if mc.objExists("R_index_B_PIV_CTL"):
			if not mc.getAttr("R_index_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_B_PIV_CTL", a=1, t=[-4.440892098500626e-16, -1.7763568394002505e-15, 0.0])
			mc.xform("R_index_B_PIV_CTL", a=1, ro=[-1.7551042632519297e-06, -0.00031147755356184995, -179.9990491081323])
			mc.xform("R_index_B_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_index_C_PIV_CTL"):
			if not mc.getAttr("R_index_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_C_PIV_CTL", a=1, t=[4.884981308350689e-15, 0.0, -4.440892098500626e-16])
			mc.xform("R_index_C_PIV_CTL", a=1, ro=[1.03618698383276e-05, 0.00016006424973296517, -179.9999993679342])
			mc.xform("R_index_C_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999997, -0.9999999999999998])

		if mc.objExists("R_index_D_PIV_CTL"):
			if not mc.getAttr("R_index_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_D_PIV_CTL", a=1, t=[-2.220446049250313e-15, -1.7763568394002505e-15, 6.661338147750939e-16])
			mc.xform("R_index_D_PIV_CTL", a=1, ro=[1.9131843358297346e-06, 0.00011900231401797998, 179.99911690147445])
			mc.xform("R_index_D_PIV_CTL", r=1, s=[0.9999999999999997, 0.9999999999999998, -1.0])

		if mc.objExists("R_middle_A_PIV_CTL"):
			if not mc.getAttr("R_middle_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_A_PIV_CTL", a=1, t=[4.440892098500626e-16, -1.7763568394002505e-15, -4.440892098500626e-16])
			mc.xform("R_middle_A_PIV_CTL", a=1, ro=[0.00021828556416431298, 0.0016371417176069972, -179.99586117325856])
			mc.xform("R_middle_A_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_middle_B_PIV_CTL"):
			if not mc.getAttr("R_middle_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_B_PIV_CTL", a=1, t=[-8.881784197001252e-16, -1.7763568394002505e-15, -4.440892098500626e-16])
			mc.xform("R_middle_B_PIV_CTL", a=1, ro=[0.00016657387166738345, 0.00032214487163743395, -179.99969261729754])
			mc.xform("R_middle_B_PIV_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, -1.0])

		if mc.objExists("R_middle_C_PIV_CTL"):
			if not mc.getAttr("R_middle_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_C_PIV_CTL", a=1, t=[-8.881784197001252e-16, 3.552713678800501e-15, 2.220446049250313e-16])
			mc.xform("R_middle_C_PIV_CTL", a=1, ro=[0.00016322863292735513, -0.00028033015008129084, 179.99970374039896])
			mc.xform("R_middle_C_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0000000000000002])

		if mc.objExists("R_middle_D_PIV_CTL"):
			if not mc.getAttr("R_middle_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_D_PIV_CTL", a=1, t=[-8.881784197001252e-16, 1.7763568394002505e-15, 4.440892098500626e-16])
			mc.xform("R_middle_D_PIV_CTL", a=1, ro=[0.0001819544736650799, -0.000429888048994416, -179.9994163318104])
			mc.xform("R_middle_D_PIV_CTL", r=1, s=[0.9999999999999997, 0.9999999999999999, -0.9999999999999998])

		if mc.objExists("R_ring_A_PIV_CTL"):
			if not mc.getAttr("R_ring_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_A_PIV_CTL", a=1, t=[1.3322676295501878e-15, 0.0, -5.551115123125783e-16])
			mc.xform("R_ring_A_PIV_CTL", a=1, ro=[8.10395282320176e-05, 0.000607796461758207, -179.9984110989508])
			mc.xform("R_ring_A_PIV_CTL", r=1, s=[1.0, 0.9999999999999998, -0.9999999999999998])

		if mc.objExists("R_ring_B_PIV_CTL"):
			if not mc.getAttr("R_ring_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_B_PIV_CTL", a=1, t=[8.881784197001252e-16, 0.0, -1.1102230246251565e-16])
			mc.xform("R_ring_B_PIV_CTL", a=1, ro=[8.308114660715006e-05, -0.000685759923237676, 179.99965026005566])
			mc.xform("R_ring_B_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000002])

		if mc.objExists("R_ring_C_PIV_CTL"):
			if not mc.getAttr("R_ring_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_C_PIV_CTL", a=1, t=[0.0, 0.0, -6.661338147750939e-16])
			mc.xform("R_ring_C_PIV_CTL", a=1, ro=[9.511735770646844e-05, 0.0005352848728788473, -179.9998205092209])
			mc.xform("R_ring_C_PIV_CTL", r=1, s=[0.9999999999999999, 1.0, -1.0])

		if mc.objExists("R_ring_D_PIV_CTL"):
			if not mc.getAttr("R_ring_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_D_PIV_CTL", a=1, t=[0.0, -5.329070518200751e-15, 2.220446049250313e-16])
			mc.xform("R_ring_D_PIV_CTL", a=1, ro=[7.862849646554276e-05, 9.012512521648621e-05, 179.99950208769513])
			mc.xform("R_ring_D_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0])

		if mc.objExists("R_pinky_A_PIV_CTL"):
			if not mc.getAttr("R_pinky_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_A_PIV_CTL", a=1, t=[0.0, -1.7763568394002505e-15, 0.0])
			mc.xform("R_pinky_A_PIV_CTL", a=1, ro=[1.4033418573113405e-14, -5.798184552627175e-19, -179.99526542300745])
			mc.xform("R_pinky_A_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -1.0])

		if mc.objExists("R_pinky_B_PIV_CTL"):
			if not mc.getAttr("R_pinky_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_B_PIV_CTL", a=1, t=[0.0, 0.0, -4.440892098500626e-16])
			mc.xform("R_pinky_B_PIV_CTL", a=1, ro=[1.403341856030302e-14, -7.183055636819874e-19, -179.99413458994513])
			mc.xform("R_pinky_B_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_pinky_C_PIV_CTL"):
			if not mc.getAttr("R_pinky_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_C_PIV_CTL", a=1, t=[0.0, -1.7763568394002505e-15, -4.440892098500626e-16])
			mc.xform("R_pinky_C_PIV_CTL", a=1, ro=[1.4033418561786553e-14, 7.036646428010654e-19, 179.99425414213738])
			mc.xform("R_pinky_C_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, -1.0])

		if mc.objExists("R_pinky_D_PIV_CTL"):
			if not mc.getAttr("R_pinky_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_D_PIV_CTL", a=1, ro=[1.4033418573113408e-14, 5.798184552320349e-19, 179.9952654230077])
			mc.xform("R_pinky_D_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -1.0])

		if mc.objExists("R_hand_PIV_CTL"):
			mc.xform("R_hand_PIV_CTL", a=1, t=[-0.4999926180415386, -1.9999704721661509, 0.0])
			mc.xform("R_hand_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_hand_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_upLeg_FK_PIV_CTL"):
			if not mc.getAttr("R_upLeg_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_FK_PIV_CTL", a=1, t=[-6.58230341343824e-08, -3.3719935477183327e-07, -3.0599133793440814e-07])
			mc.xform("R_upLeg_FK_PIV_CTL", a=1, ro=[-1.590277556897713e-15, 3.89409960002066e-06, 180.0])
			mc.xform("R_upLeg_FK_PIV_CTL", r=1, s=[1.0000000000000004, 1.0000000000000004, -1.0000000000000007])

		if mc.objExists("R_loLeg_FK_PIV_CTL"):
			if not mc.getAttr("R_loLeg_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_FK_PIV_CTL", a=1, t=[-2.350195521749754e-06, -3.3719935443876636e-07, 1.6599149010865233e-07])
			mc.xform("R_loLeg_FK_PIV_CTL", a=1, ro=[2.3854161974634906e-15, -1.678634363164426e-06, 180.0])
			mc.xform("R_loLeg_FK_PIV_CTL", r=1, s=[0.9999999999999998, 1.0, -1.0])

		if mc.objExists("R_legEnd_FK_PIV_CTL"):
			if not mc.getAttr("R_legEnd_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_legEnd_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_legEnd_FK_PIV_CTL", a=1, t=[4.418109605941467e-07, -3.371993551049002e-07, 2.9545756030646686e-07])
			mc.xform("R_legEnd_FK_PIV_CTL", a=1, ro=[2.3854161974634922e-15, -1.6786343758866448e-06, 180.0])
			mc.xform("R_legEnd_FK_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000002])

		if mc.objExists("R_leg_IK_PIV_CTL"):
			mc.xform("R_leg_IK_PIV_CTL", a=1, t=[4.551914400963142e-15, -1.1102230246251565e-16, -2.220446049250313e-16])
			mc.xform("R_leg_IK_PIV_CTL", a=1, ro=[180.0, -0.0, 0.0])
			mc.xform("R_leg_IK_PIV_CTL", r=1, s=[1.0000000000000004, 1.0000000000000004, -1.0])

		if mc.objExists("R_leg_PV_PIV_CTL"):
			mc.xform("R_leg_PV_PIV_CTL", a=1, t=[-3.120317029647879e-06, 0.0, 9.999971191625884])
			mc.xform("R_leg_PV_PIV_CTL", a=1, ro=[-1.987864203842872e-16, -4.5107869014219485e-06, -179.99999999999997])
			mc.xform("R_leg_PV_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999994])

		if mc.objExists("R_legBase_PIV_CTL"):
			if not mc.getAttr("R_legBase_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_PIV_CTL.rotateOrder", 0)

			mc.xform("R_legBase_PIV_CTL", a=1, t=[-6.58230341343824e-08, -3.3719935477183327e-07, -3.0599133793440814e-07])
			mc.xform("R_legBase_PIV_CTL", a=1, ro=[-1.590277556897713e-15, 3.89409960002066e-06, 180.0])
			mc.xform("R_legBase_PIV_CTL", r=1, s=[1.0000000000000004, 1.0000000000000004, -1.0000000000000007])

		if mc.objExists("R_leg_IK_switch_PIV_CTL"):
			if not mc.getAttr("R_leg_IK_switch_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_PIV_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_PIV_CTL", a=1, t=[4.418109605941467e-07, -3.371993551049002e-07, 2.9545756030646686e-07])
			mc.xform("R_leg_IK_switch_PIV_CTL", a=1, ro=[2.3854161974634922e-15, -1.6786343758866448e-06, 180.0])
			mc.xform("R_leg_IK_switch_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000002])

		if mc.objExists("R_innerBall_PIV_CTL"):
			mc.xform("R_innerBall_PIV_CTL", a=1, t=[1.1102230246251565e-16, -2.7755575615628914e-16, 8.881784197001252e-16])
			mc.xform("R_innerBall_PIV_CTL", a=1, ro=[1.1744439568731615, -0.30746888225771457, -180.0])
			mc.xform("R_innerBall_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000002])

		if mc.objExists("R_outterBall_PIV_CTL"):
			mc.xform("R_outterBall_PIV_CTL", a=1, t=[0.0, -1.3877787807814457e-16, 4.440892098500626e-16])
			mc.xform("R_outterBall_PIV_CTL", a=1, ro=[1.1744439568731615, -0.30746888225771457, -180.0])
			mc.xform("R_outterBall_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000002])

		if mc.objExists("R_heel_PIV_CTL"):
			mc.xform("R_heel_PIV_CTL", a=1, t=[1.1102230246251565e-16, 0.0, -2.220446049250313e-16])
			mc.xform("R_heel_PIV_CTL", a=1, ro=[1.1744439568731615, -0.30746888225771457, -180.0])
			mc.xform("R_heel_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000002])

		if mc.objExists("R_toeTip_PIV_CTL"):
			mc.xform("R_toeTip_PIV_CTL", a=1, t=[1.1102230246251565e-16, -3.608224830031759e-16, 1.1102230246251565e-15])
			mc.xform("R_toeTip_PIV_CTL", a=1, ro=[3.880485315590931e-06, -1.8668757841545487e-06, -179.99999996172772])
			mc.xform("R_toeTip_PIV_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, -1.0])

		if mc.objExists("R_reverseBall_PIV_CTL"):
			mc.xform("R_reverseBall_PIV_CTL", a=1, t=[2.220446049250313e-16, -5.551115123125783e-17, -7.771561172376096e-16])
			mc.xform("R_reverseBall_PIV_CTL", a=1, ro=[-179.99999611951463, 1.8668757933051276e-06, -8.823568946316488e-15])
			mc.xform("R_reverseBall_PIV_CTL", r=1, s=[1.0000000000000002, 0.9999999999999999, -1.0])

		if mc.objExists("R_ankleOffset_PIV_CTL"):
			mc.xform("R_ankleOffset_PIV_CTL", a=1, t=[2.220446049250313e-16, 0.0, 2.220446049250313e-16])
			mc.xform("R_ankleOffset_PIV_CTL", a=1, ro=[179.99997456010934, -3.5206263484859256e-16, 180.0])
			mc.xform("R_ankleOffset_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_toe_IK_PIV_CTL"):
			mc.xform("R_toe_IK_PIV_CTL", a=1, t=[5.551115123125783e-16, 2.220446049250313e-16, 0.0])
			mc.xform("R_toe_IK_PIV_CTL", a=1, ro=[-2.1270910011111945e-13, -1.5571741667281952e-05, 179.99993263605614])
			mc.xform("R_toe_IK_PIV_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, -0.9999999999999998])

		if mc.objExists("R_toe_FK_PIV_CTL"):
			if not mc.getAttr("R_toe_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_toe_FK_PIV_CTL", a=1, t=[-3.9038212151787377e-07, -3.357676086057637e-07, -2.9938088103032e-07])
			mc.xform("R_toe_FK_PIV_CTL", a=1, ro=[-2.1270910011111945e-13, -1.5571741667281952e-05, 179.99993263605614])
			mc.xform("R_toe_FK_PIV_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, -0.9999999999999998])

		if mc.objExists("R_upArm_FK_PIV_CTL"):
			if not mc.getAttr("R_upArm_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upArm_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upArm_FK_PIV_CTL", a=1, t=[-3.43469618258041e-06, 7.5525218896643764e-06, 1.445525280807658e-06])
			mc.xform("R_upArm_FK_PIV_CTL", a=1, ro=[-0.001728219089948796, -6.331375130207883e-05, -179.99977072931378])
			mc.xform("R_upArm_FK_PIV_CTL", r=1, s=[1.0, 1.0000000000000002, -1.0])

		if mc.objExists("R_loArm_FK_PIV_CTL"):
			if not mc.getAttr("R_loArm_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_loArm_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_loArm_FK_PIV_CTL", a=1, t=[8.005737486271869e-06, -3.873761331263381e-06, 1.3618995823305724e-06])
			mc.xform("R_loArm_FK_PIV_CTL", a=1, ro=[-0.0016644952301748612, -7.079466959552661e-05, 179.9994815803909])
			mc.xform("R_loArm_FK_PIV_CTL", r=1, s=[1.0000000000000002, 0.9999999999999998, -1.0])

		if mc.objExists("R_wrist_FK_PIV_CTL"):
			if not mc.getAttr("R_wrist_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_wrist_FK_PIV_CTL", a=1, t=[-1.5597409016798736e-05, 2.4185521501962626e-05, -1.952690631412679e-08])
			mc.xform("R_wrist_FK_PIV_CTL", a=1, ro=[0.00018674258458359282, -0.00019761436674937553, -179.99677989646796])
			mc.xform("R_wrist_FK_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, -1.0000000000000002])

		if mc.objExists("R_arm_IK_PIV_CTL"):
			if not mc.getAttr("R_arm_IK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_PIV_CTL", a=1, t=[-1.5597409016798736e-05, 2.4185521501962626e-05, -1.952690631412679e-08])
			mc.xform("R_arm_IK_PIV_CTL", a=1, ro=[0.00018674258458359282, -0.00019761436674937553, -179.99677989646796])
			mc.xform("R_arm_IK_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, -1.0000000000000002])

		if mc.objExists("R_wrist_IK_PIV_CTL"):
			if not mc.getAttr("R_wrist_IK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_PIV_CTL", a=1, t=[-1.5597409016798736e-05, 2.4185521501962626e-05, -1.952690631412679e-08])
			mc.xform("R_wrist_IK_PIV_CTL", a=1, ro=[0.00018674258458359282, -0.00019761436674937553, -179.99677989646796])
			mc.xform("R_wrist_IK_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, -1.0000000000000002])

		if mc.objExists("R_arm_PV_PIV_CTL"):
			mc.xform("R_arm_PV_PIV_CTL", a=1, t=[9.30085606398734e-06, -0.00030592594376344096, 9.999957250553228])
			mc.xform("R_arm_PV_PIV_CTL", a=1, ro=[-0.0017365277191742695, 8.40899601252937e-06, 179.99984580222394])
			mc.xform("R_arm_PV_PIV_CTL", r=1, s=[1.0, 1.0000000000000002, -1.0000000000000002])

		if mc.objExists("R_shoulder_PIV_CTL"):
			if not mc.getAttr("R_shoulder_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_PIV_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_PIV_CTL", a=1, t=[2.001667578022115e-06, -2.267743458084226e-05, -1.042203674750386e-07])
			mc.xform("R_shoulder_PIV_CTL", a=1, ro=[9.154342484223836e-06, -0.00012684351930885592, 179.99901485316326])
			mc.xform("R_shoulder_PIV_CTL", r=1, s=[1.0, 0.9999999999999999, -0.9999999999999998])

		if mc.objExists("R_arm_IK_switch_PIV_CTL"):
			if not mc.getAttr("R_arm_IK_switch_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_PIV_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_PIV_CTL", a=1, t=[-1.5597409016798736e-05, 2.4185521501962626e-05, -1.952690631412679e-08])
			mc.xform("R_arm_IK_switch_PIV_CTL", a=1, ro=[0.00018674258458359282, -0.00019761436674937553, -179.99677989646796])
			mc.xform("R_arm_IK_switch_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, -1.0000000000000002])

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
			mc.xform("world_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("world_CTL"):
			if not mc.getAttr("world_CTL.numOffsetCtrls", l=1):
				mc.setAttr("world_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("world_CTL.mirrorMode", l=1):
				mc.setAttr("world_CTL.mirrorMode", 0)

			if not mc.getAttr("world_CTL.rotateOrder", l=1):
				mc.setAttr("world_CTL.rotateOrder", 0)

			mc.xform("world_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("world_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("world_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("visibility_CTL"):
			if not mc.getAttr("visibility_CTL.mirrorMode", l=1):
				mc.setAttr("visibility_CTL.mirrorMode", 0)

			if not mc.getAttr("visibility_CTL.rotateOrder", l=1):
				mc.setAttr("visibility_CTL.rotateOrder", 0)

			mc.xform("visibility_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("visibility_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("visibility_CTL", r=1, s=[3.5402399476867825, 3.5402399476867825, 3.5402399476867825])

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
				mc.setAttr("C_cog_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("C_cog_CTL.mirrorMode", l=1):
				mc.setAttr("C_cog_CTL.mirrorMode", 0)

			if not mc.getAttr("C_cog_CTL.rotateOrder", l=1):
				mc.setAttr("C_cog_CTL.rotateOrder", 0)

			mc.xform("C_cog_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_cog_CTL", a=1, ro=[0.0, 0.0, -90.0])
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

		if mc.objExists("C_midTorso_D_OFF_CTL"):
			if not mc.getAttr("C_midTorso_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midTorso_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midTorso_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midTorso_C_OFF_CTL"):
			if not mc.getAttr("C_midTorso_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midTorso_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midTorso_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midTorso_B_OFF_CTL"):
			if not mc.getAttr("C_midTorso_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midTorso_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midTorso_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midTorso_A_OFF_CTL"):
			if not mc.getAttr("C_midTorso_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_midTorso_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_midTorso_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_midTorso_CTL"):
			if not mc.getAttr("C_midTorso_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_midTorso_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_midTorso_CTL.mirrorMode", l=1):
				mc.setAttr("C_midTorso_CTL.mirrorMode", 0)

			if not mc.getAttr("C_midTorso_CTL.rotateOrder", l=1):
				mc.setAttr("C_midTorso_CTL.rotateOrder", 0)

			mc.xform("C_midTorso_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_midTorso_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_FK_A_CTL"):
			if not mc.getAttr("C_torso_FK_A_CTL.mirrorMode", l=1):
				mc.setAttr("C_torso_FK_A_CTL.mirrorMode", 0)

			if not mc.getAttr("C_torso_FK_A_CTL.rotateOrder", l=1):
				mc.setAttr("C_torso_FK_A_CTL.rotateOrder", 0)

			mc.xform("C_torso_FK_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_FK_B_CTL"):
			if not mc.getAttr("C_torso_FK_B_CTL.mirrorMode", l=1):
				mc.setAttr("C_torso_FK_B_CTL.mirrorMode", 0)

			if not mc.getAttr("C_torso_FK_B_CTL.rotateOrder", l=1):
				mc.setAttr("C_torso_FK_B_CTL.rotateOrder", 0)

			mc.xform("C_torso_FK_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_FK_C_CTL"):
			if not mc.getAttr("C_torso_FK_C_CTL.mirrorMode", l=1):
				mc.setAttr("C_torso_FK_C_CTL.mirrorMode", 0)

			if not mc.getAttr("C_torso_FK_C_CTL.rotateOrder", l=1):
				mc.setAttr("C_torso_FK_C_CTL.rotateOrder", 0)

			mc.xform("C_torso_FK_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_FK_D_CTL"):
			if not mc.getAttr("C_torso_FK_D_CTL.mirrorMode", l=1):
				mc.setAttr("C_torso_FK_D_CTL.mirrorMode", 0)

			if not mc.getAttr("C_torso_FK_D_CTL.rotateOrder", l=1):
				mc.setAttr("C_torso_FK_D_CTL.rotateOrder", 0)

			mc.xform("C_torso_FK_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_FK_E_CTL"):
			if not mc.getAttr("C_torso_FK_E_CTL.mirrorMode", l=1):
				mc.setAttr("C_torso_FK_E_CTL.mirrorMode", 0)

			if not mc.getAttr("C_torso_FK_E_CTL.rotateOrder", l=1):
				mc.setAttr("C_torso_FK_E_CTL.rotateOrder", 0)

			mc.xform("C_torso_FK_E_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_E_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_FK_E_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_FK_CTL"):
			if not mc.getAttr("C_chest_FK_CTL.mirrorMode", l=1):
				mc.setAttr("C_chest_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("C_chest_FK_CTL.rotateOrder", l=1):
				mc.setAttr("C_chest_FK_CTL.rotateOrder", 0)

			mc.xform("C_chest_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_FK_CTL"):
			if not mc.getAttr("L_upArm_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_upArm_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upArm_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_upArm_FK_CTL.rotateOrder", 0)

			mc.xform("L_upArm_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_FK_CTL"):
			if not mc.getAttr("L_loArm_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_loArm_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loArm_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_loArm_FK_CTL.rotateOrder", 0)

			mc.xform("L_loArm_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_FK_CTL"):
			if not mc.getAttr("L_wrist_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_wrist_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_wrist_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_wrist_FK_CTL.rotateOrder", 0)

			mc.xform("L_wrist_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_D_OFF_CTL"):
			if not mc.getAttr("L_arm_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_C_OFF_CTL"):
			if not mc.getAttr("L_arm_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_B_OFF_CTL"):
			if not mc.getAttr("L_arm_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_A_OFF_CTL"):
			if not mc.getAttr("L_arm_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_CTL"):
			if not mc.getAttr("L_arm_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_arm_IK_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("L_arm_IK_CTL.mirrorMode", l=1):
				mc.setAttr("L_arm_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_arm_IK_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_IK_D_OFF_CTL"):
			if not mc.getAttr("L_wrist_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_wrist_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_wrist_IK_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_IK_C_OFF_CTL"):
			if not mc.getAttr("L_wrist_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_wrist_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_wrist_IK_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_IK_B_OFF_CTL"):
			if not mc.getAttr("L_wrist_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_wrist_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_wrist_IK_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_IK_A_OFF_CTL"):
			if not mc.getAttr("L_wrist_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_wrist_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_wrist_IK_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_IK_CTL"):
			if not mc.getAttr("L_wrist_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_wrist_IK_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_wrist_IK_CTL.mirrorMode", l=1):
				mc.setAttr("L_wrist_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_wrist_IK_CTL.rotateOrder", l=1):
				mc.setAttr("L_wrist_IK_CTL.rotateOrder", 0)

			mc.xform("L_wrist_IK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_IK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_PV_CTL"):
			if not mc.getAttr("L_arm_PV_CTL.mirrorMode", l=1):
				mc.setAttr("L_arm_PV_CTL.mirrorMode", 0)

			if not mc.getAttr("L_arm_PV_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_PV_CTL.rotateOrder", 0)

			mc.xform("L_arm_PV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_PV_CTL", a=1, ro=[-1.224374757658996, 0.6177092716231289, 47.319477550689584])
			mc.xform("L_arm_PV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_D_OFF_CTL"):
			if not mc.getAttr("L_shoulder_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_C_OFF_CTL"):
			if not mc.getAttr("L_shoulder_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_B_OFF_CTL"):
			if not mc.getAttr("L_shoulder_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_A_OFF_CTL"):
			if not mc.getAttr("L_shoulder_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_CTL"):
			if not mc.getAttr("L_shoulder_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_shoulder_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_shoulder_CTL.mirrorMode", l=1):
				mc.setAttr("L_shoulder_CTL.mirrorMode", 0)

			if not mc.getAttr("L_shoulder_CTL.rotateOrder", l=1):
				mc.setAttr("L_shoulder_CTL.rotateOrder", 0)

			mc.xform("L_shoulder_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_CTL", r=1, s=[1.0, 1.0, 1.0])

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

			mc.xform("L_arm_IK_switch_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_switch_CTL", r=1, s=[1.0, 1.0, 1.0])

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
			mc.xform("L_leg_PV_CTL", a=1, ro=[179.68090993459336, -2.4848083448933725e-17, -90.00000000000003])
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

		if mc.objExists("C_jaw_CTL"):
			if not mc.getAttr("C_jaw_CTL.mirrorMode", l=1):
				mc.setAttr("C_jaw_CTL.mirrorMode", 0)

			if not mc.getAttr("C_jaw_CTL.rotateOrder", l=1):
				mc.setAttr("C_jaw_CTL.rotateOrder", 0)

			mc.xform("C_jaw_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_jaw_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_reverseJaw_CTL"):
			if not mc.getAttr("C_reverseJaw_CTL.mirrorMode", l=1):
				mc.setAttr("C_reverseJaw_CTL.mirrorMode", 0)

			if not mc.getAttr("C_reverseJaw_CTL.rotateOrder", l=1):
				mc.setAttr("C_reverseJaw_CTL.rotateOrder", 0)

			mc.xform("C_reverseJaw_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_head_FK_CTL"):
			if not mc.getAttr("C_head_FK_CTL.mirrorMode", l=1):
				mc.setAttr("C_head_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("C_head_FK_CTL.rotateOrder", l=1):
				mc.setAttr("C_head_FK_CTL.rotateOrder", 0)

			mc.xform("C_head_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_head_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_A_CTL"):
			if not mc.getAttr("R_thumb_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_CTL.rotateOrder", 0)

			mc.xform("R_thumb_A_CTL", a=1, t=[1.878620507067552e-05, -3.3491768056670423e-05, 1.2123225654470104e-05])
			mc.xform("R_thumb_A_CTL", a=1, ro=[6.3611093629270335e-15, 2.3854160110976376e-15, -7.95138670365879e-16])
			mc.xform("R_thumb_A_CTL", r=1, s=[0.9999999999999996, 0.9999999999999996, 1.0])

		if mc.objExists("R_thumb_B_CTL"):
			if not mc.getAttr("R_thumb_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_CTL.rotateOrder", 0)

			mc.xform("R_thumb_B_CTL", a=1, t=[-5.925737038836587e-07, 2.4479787770204098e-06, 3.938486032417643e-06])
			mc.xform("R_thumb_B_CTL", a=1, ro=[-1.2722218725854067e-14, -2.4649298781342254e-14, -1.5902773407317556e-15])
			mc.xform("R_thumb_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_C_CTL"):
			if not mc.getAttr("R_thumb_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_CTL.rotateOrder", 0)

			mc.xform("R_thumb_C_CTL", a=1, t=[-2.328741522283906e-06, 1.7396943583491975e-06, -2.935150149596666e-07])
			mc.xform("R_thumb_C_CTL", a=1, ro=[6.361109362927032e-15, -6.361109362927032e-15, 1.5902773407317576e-15])
			mc.xform("R_thumb_C_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, 0.9999999999999999])

		if mc.objExists("R_index_A_CTL"):
			if not mc.getAttr("R_index_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_A_CTL.rotateOrder", 0)

			mc.xform("R_index_A_CTL", a=1, t=[-3.990538821607714e-06, -2.1423167630985063e-06, 1.7577940376600765e-06])
			mc.xform("R_index_A_CTL", a=1, ro=[7.951386703658792e-16, -3.4787316828507214e-15, -2.4138550067461804e-32])
			mc.xform("R_index_A_CTL", r=1, s=[1.0, 0.9999999999999999, 1.0000000000000002])

		if mc.objExists("R_index_B_CTL"):
			if not mc.getAttr("R_index_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_B_CTL.rotateOrder", 0)

			mc.xform("R_index_B_CTL", a=1, t=[-3.426759385138922e-06, -3.1571482210779322e-06, 1.1425921075947088e-06])
			mc.xform("R_index_B_CTL", a=1, ro=[1.6697912077683458e-14, -2.882377680076314e-15, 1.9083328088781097e-14])
			mc.xform("R_index_B_CTL", r=1, s=[0.9999999999999997, 1.0, 0.9999999999999997])

		if mc.objExists("R_index_C_CTL"):
			if not mc.getAttr("R_index_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_C_CTL.rotateOrder", 0)

			mc.xform("R_index_C_CTL", a=1, t=[2.185682702826597e-06, 3.477925920591929e-06, -9.025037044363415e-07])
			mc.xform("R_index_C_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_index_C_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_index_D_CTL"):
			if not mc.getAttr("R_index_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_D_CTL.rotateOrder", 0)

			mc.xform("R_index_D_CTL", a=1, t=[-3.1746546831357136e-06, 3.319392849476799e-06, 1.4847586715660555e-07])
			mc.xform("R_index_D_CTL", a=1, ro=[2.484808344893372e-16, -7.205944200190778e-16, -6.361109362927032e-15])
			mc.xform("R_index_D_CTL", r=1, s=[0.9999999999999998, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_middle_A_CTL"):
			if not mc.getAttr("R_middle_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_A_CTL.rotateOrder", 0)

			mc.xform("R_middle_A_CTL", a=1, t=[2.7223010764743094e-05, -3.06934687035465e-05, -1.0219909623909729e-05])
			mc.xform("R_middle_A_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_middle_A_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000004])

		if mc.objExists("R_middle_B_CTL"):
			if not mc.getAttr("R_middle_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_B_CTL.rotateOrder", 0)

			mc.xform("R_middle_B_CTL", a=1, t=[2.408668793307811e-07, -3.3552328186914337e-06, 5.908634710394267e-07])
			mc.xform("R_middle_B_CTL", a=1, ro=[2.79292457966015e-14, -5.342337941520749e-15, -6.3611093629270335e-15])
			mc.xform("R_middle_B_CTL", r=1, s=[1.0000000000000002, 0.9999999999999999, 1.0])

		if mc.objExists("R_middle_C_CTL"):
			if not mc.getAttr("R_middle_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_C_CTL.rotateOrder", 0)

			mc.xform("R_middle_C_CTL", a=1, t=[-2.789985370732495e-06, -1.803475296213719e-06, 2.7060572735937427e-06])
			mc.xform("R_middle_C_CTL", a=1, ro=[3.02152694739034e-14, -2.186631343506167e-15, -5.7656651018280175e-31])
			mc.xform("R_middle_C_CTL", r=1, s=[0.9999999999999998, 0.9999999999999997, 0.9999999999999998])

		if mc.objExists("R_middle_D_CTL"):
			if not mc.getAttr("R_middle_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_D_CTL.rotateOrder", 0)

			mc.xform("R_middle_D_CTL", a=1, t=[7.899606808692283e-07, -3.7121913436521936e-06, 8.654498830917845e-07])
			mc.xform("R_middle_D_CTL", a=1, ro=[2.266145210542756e-14, -7.951386703658792e-16, -1.5724541186803695e-31])
			mc.xform("R_middle_D_CTL", r=1, s=[0.9999999999999999, 1.0, 1.0000000000000002])

		if mc.objExists("R_ring_A_CTL"):
			if not mc.getAttr("R_ring_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_A_CTL.rotateOrder", 0)

			mc.xform("R_ring_A_CTL", a=1, t=[6.634848269682081e-06, -1.0319284191595557e-05, -2.814098685632871e-06])
			mc.xform("R_ring_A_CTL", a=1, ro=[0.0, -1.3914926731402888e-15, 0.0])
			mc.xform("R_ring_A_CTL", r=1, s=[0.9999999999999999, 1.0, 1.0])

		if mc.objExists("R_ring_B_CTL"):
			if not mc.getAttr("R_ring_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_B_CTL.rotateOrder", 0)

			mc.xform("R_ring_B_CTL", a=1, t=[4.979933460935726e-06, 4.3515273162597623e-07, 1.1991564690116974e-06])
			mc.xform("R_ring_B_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_ring_B_CTL", r=1, s=[0.9999999999999998, 0.9999999999999997, 0.9999999999999998])

		if mc.objExists("R_ring_C_CTL"):
			if not mc.getAttr("R_ring_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_C_CTL.rotateOrder", 0)

			mc.xform("R_ring_C_CTL", a=1, t=[3.364640305925093e-06, -1.343374885109938e-06, -3.3034970806644637e-06])
			mc.xform("R_ring_C_CTL", a=1, ro=[-7.951386703658792e-16, 1.6896696745274934e-15, -1.1724438604195736e-32])
			mc.xform("R_ring_C_CTL", r=1, s=[1.0, 0.9999999999999998, 1.0])

		if mc.objExists("R_ring_D_CTL"):
			if not mc.getAttr("R_ring_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_D_CTL.rotateOrder", 0)

			mc.xform("R_ring_D_CTL", a=1, t=[-4.4951227273770655e-06, -4.0227740072396045e-07, 2.1120284754427843e-07])
			mc.xform("R_ring_D_CTL", a=1, ro=[2.6438360789665484e-14, -8.945310041616126e-16, -6.3611093629270335e-15])
			mc.xform("R_ring_D_CTL", r=1, s=[0.9999999999999999, 1.0, 1.0])

		if mc.objExists("R_pinky_A_CTL"):
			if not mc.getAttr("R_pinky_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_CTL.rotateOrder", 0)

			mc.xform("R_pinky_A_CTL", a=1, t=[-1.26715530424093e-06, -2.8372351813743535e-05, 2.9609306468891816e-06])
			mc.xform("R_pinky_A_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_pinky_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_B_CTL"):
			if not mc.getAttr("R_pinky_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_CTL.rotateOrder", 0)

			mc.xform("R_pinky_B_CTL", a=1, t=[-9.93616166233835e-07, 2.84116716642302e-06, 2.9609306464450924e-06])
			mc.xform("R_pinky_B_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_pinky_B_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0])

		if mc.objExists("R_pinky_C_CTL"):
			if not mc.getAttr("R_pinky_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_CTL.rotateOrder", 0)

			mc.xform("R_pinky_C_CTL", a=1, t=[-8.188899379035774e-06, 4.056696420029482e-05, 2.9609306468891816e-06])
			mc.xform("R_pinky_C_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_pinky_C_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, 1.0])

		if mc.objExists("R_pinky_D_CTL"):
			if not mc.getAttr("R_pinky_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_CTL.rotateOrder", 0)

			mc.xform("R_pinky_D_CTL", a=1, t=[8.427253881393426e-07, 2.8896083552609753e-06, 2.960930646667137e-06])
			mc.xform("R_pinky_D_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_pinky_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_hand_CTL"):
			if not mc.getAttr("R_hand_CTL.mirrorMode", l=1):
				mc.setAttr("R_hand_CTL.mirrorMode", 0)

			if not mc.getAttr("R_hand_CTL.rotateOrder", l=1):
				mc.setAttr("R_hand_CTL.rotateOrder", 0)

			mc.xform("R_hand_CTL", a=1, t=[2.4937558738002963e-06, 1.2368951605168377e-06, -1.9867722249600206e-06])
			mc.xform("R_hand_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_hand_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_FK_CTL"):
			if not mc.getAttr("R_upLeg_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_upLeg_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upLeg_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_FK_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_FK_CTL", a=1, t=[0.0, 0.0, 5.551115123125783e-16])
			mc.xform("R_upLeg_FK_CTL", a=1, ro=[-6.896728590703373e-34, 1.5902773407317584e-15, -4.969616689786745e-17])
			mc.xform("R_upLeg_FK_CTL", r=1, s=[1.0, 0.9999999999999999, 0.9999999999999999])

		if mc.objExists("R_loLeg_FK_CTL"):
			if not mc.getAttr("R_loLeg_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_loLeg_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_loLeg_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_FK_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_FK_CTL", a=1, t=[-1.7763568394002505e-15, 0.0, 0.0])
			mc.xform("R_loLeg_FK_CTL", a=1, ro=[7.951386703658792e-16, 7.951386703658792e-16, 4.969616689786745e-17])
			mc.xform("R_loLeg_FK_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0000000000000002])

		if mc.objExists("R_legEnd_FK_CTL"):
			if not mc.getAttr("R_legEnd_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_legEnd_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_legEnd_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_legEnd_FK_CTL.rotateOrder", 0)

			mc.xform("R_legEnd_FK_CTL", a=1, t=[2.220446049250313e-16, -3.3306690738754696e-16, -2.220446049250313e-16])
			mc.xform("R_legEnd_FK_CTL", a=1, ro=[7.951386703658792e-16, -7.951386703658792e-16, -5.517382872562698e-33])
			mc.xform("R_legEnd_FK_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0])

		if mc.objExists("R_leg_IK_D_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_D_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_leg_IK_D_OFF_CTL", a=1, ro=[1.403341859706975e-14, 1.3949415782257268e-29, -1.0813885916975958e-13])
			mc.xform("R_leg_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_C_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_C_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_leg_IK_C_OFF_CTL", a=1, ro=[1.403341859706975e-14, 1.3949415782257268e-29, -1.0813885916975958e-13])
			mc.xform("R_leg_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_B_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_B_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_leg_IK_B_OFF_CTL", a=1, ro=[1.403341859706975e-14, 1.3949415782257268e-29, -1.0813885916975958e-13])
			mc.xform("R_leg_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_A_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_A_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_leg_IK_A_OFF_CTL", a=1, ro=[1.403341859706975e-14, 1.3949415782257268e-29, -1.0813885916975958e-13])
			mc.xform("R_leg_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_CTL"):
			if not mc.getAttr("R_leg_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_leg_IK_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("R_leg_IK_CTL.mirrorMode", l=1):
				mc.setAttr("R_leg_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_leg_IK_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_CTL", a=1, t=[3.9127877815570145e-07, 3.3719935466081097e-07, 3.597123979792727e-07])
			mc.xform("R_leg_IK_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_leg_IK_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, 1.0])

		if mc.objExists("R_leg_PV_CTL"):
			if not mc.getAttr("R_leg_PV_CTL.mirrorMode", l=1):
				mc.setAttr("R_leg_PV_CTL.mirrorMode", 0)

			if not mc.getAttr("R_leg_PV_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_PV_CTL.rotateOrder", 0)

			mc.xform("R_leg_PV_CTL", a=1, t=[-1.5586852910587368e-06, -1.1102230246251565e-16, -2.8625091708534e-05])
			mc.xform("R_leg_PV_CTL", a=1, ro=[-0.31909006540663704, 0.0, -90.00000000000004])
			mc.xform("R_leg_PV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999998, 0.9999999999999997])

		if mc.objExists("R_legBase_D_OFF_CTL"):
			if not mc.getAttr("R_legBase_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_D_OFF_CTL", a=1, t=[1.7763568394002505e-15, 2.220446049250313e-16, -1.1102230246251565e-16])
			mc.xform("R_legBase_D_OFF_CTL", a=1, ro=[7.951386703658793e-15, 1.5902773407317592e-15, -5.764755360152626e-15])
			mc.xform("R_legBase_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_C_OFF_CTL"):
			if not mc.getAttr("R_legBase_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_C_OFF_CTL", a=1, t=[-1.7763568394002505e-15, -2.220446049250313e-16, 1.1102230246251565e-16])
			mc.xform("R_legBase_C_OFF_CTL", a=1, ro=[7.951386703658793e-15, 1.5902773407317592e-15, -5.764755360152626e-15])
			mc.xform("R_legBase_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_B_OFF_CTL"):
			if not mc.getAttr("R_legBase_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_B_OFF_CTL", a=1, t=[1.7763568394002505e-15, 2.220446049250313e-16, -1.1102230246251565e-16])
			mc.xform("R_legBase_B_OFF_CTL", a=1, ro=[7.951386703658793e-15, 1.5902773407317592e-15, -5.764755360152626e-15])
			mc.xform("R_legBase_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_A_OFF_CTL"):
			if not mc.getAttr("R_legBase_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_A_OFF_CTL", a=1, t=[-1.7763568394002505e-15, -2.220446049250313e-16, 1.1102230246251565e-16])
			mc.xform("R_legBase_A_OFF_CTL", a=1, ro=[7.951386703658793e-15, 1.5902773407317592e-15, -5.764755360152626e-15])
			mc.xform("R_legBase_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_CTL"):
			if not mc.getAttr("R_legBase_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_legBase_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_legBase_CTL.mirrorMode", l=1):
				mc.setAttr("R_legBase_CTL.mirrorMode", 0)

			if not mc.getAttr("R_legBase_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_CTL.rotateOrder", 0)

			mc.xform("R_legBase_CTL", a=1, t=[0.0, 0.0, 5.551115123125783e-16])
			mc.xform("R_legBase_CTL", a=1, ro=[-6.896728590703373e-34, 1.5902773407317584e-15, -4.969616689786745e-17])
			mc.xform("R_legBase_CTL", r=1, s=[1.0, 0.9999999999999999, 0.9999999999999999])

		if mc.objExists("R_leg_IK_switch_D_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_D_OFF_CTL", a=1, t=[0.0, 1.1102230246251565e-16, 0.0])
			mc.xform("R_leg_IK_switch_D_OFF_CTL", a=1, ro=[5.565970692561154e-15, 2.385416011097638e-15, -6.858071031905708e-15])
			mc.xform("R_leg_IK_switch_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_C_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_C_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 0.0])
			mc.xform("R_leg_IK_switch_C_OFF_CTL", a=1, ro=[5.565970692561154e-15, 2.385416011097638e-15, -6.858071031905708e-15])
			mc.xform("R_leg_IK_switch_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_B_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_B_OFF_CTL", a=1, t=[1.1102230246251565e-16, 1.1102230246251565e-16, 0.0])
			mc.xform("R_leg_IK_switch_B_OFF_CTL", a=1, ro=[5.565970692561154e-15, 2.385416011097638e-15, -6.858071031905708e-15])
			mc.xform("R_leg_IK_switch_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_A_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_A_OFF_CTL", a=1, t=[1.1102230246251565e-16, -1.1102230246251565e-16, 0.0])
			mc.xform("R_leg_IK_switch_A_OFF_CTL", a=1, ro=[5.565970692561154e-15, 2.385416011097638e-15, -6.858071031905708e-15])
			mc.xform("R_leg_IK_switch_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_CTL"):
			if not mc.getAttr("R_leg_IK_switch_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_leg_IK_switch_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_leg_IK_switch_CTL.mirrorMode", l=1):
				mc.setAttr("R_leg_IK_switch_CTL.mirrorMode", 0)

			if not mc.getAttr("R_leg_IK_switch_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_CTL", a=1, t=[2.220446049250313e-16, -3.3306690738754696e-16, -2.220446049250313e-16])
			mc.xform("R_leg_IK_switch_CTL", a=1, ro=[7.951386703658792e-16, -7.951386703658792e-16, -5.517382872562698e-33])
			mc.xform("R_leg_IK_switch_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0])

		if mc.objExists("R_innerBall_CTL"):
			if not mc.getAttr("R_innerBall_CTL.mirrorMode", l=1):
				mc.setAttr("R_innerBall_CTL.mirrorMode", 0)

			if not mc.getAttr("R_innerBall_CTL.rotateOrder", l=1):
				mc.setAttr("R_innerBall_CTL.rotateOrder", 0)

			mc.xform("R_innerBall_CTL", a=1, t=[1.5014951448844016e-07, -2.606629026236096e-07, -8.193105083265095e-09])
			mc.xform("R_innerBall_CTL", a=1, ro=[-1.987846675914698e-16, 6.735086514358764e-37, 3.8825130388958945e-19])
			mc.xform("R_innerBall_CTL", r=1, s=[0.9999999999999998, 0.9999999999999997, 0.9999999999999998])

		if mc.objExists("R_outterBall_CTL"):
			if not mc.getAttr("R_outterBall_CTL.mirrorMode", l=1):
				mc.setAttr("R_outterBall_CTL.mirrorMode", 0)

			if not mc.getAttr("R_outterBall_CTL.rotateOrder", l=1):
				mc.setAttr("R_outterBall_CTL.rotateOrder", 0)

			mc.xform("R_outterBall_CTL", a=1, t=[1.2885575753074363e-06, 3.1012629866933317e-07, 3.1219479279531726e-08])
			mc.xform("R_outterBall_CTL", a=1, ro=[-1.987846675914698e-16, 6.735086514358764e-37, 3.8825130388958945e-19])
			mc.xform("R_outterBall_CTL", r=1, s=[0.9999999999999998, 0.9999999999999999, 0.9999999999999996])

		if mc.objExists("R_heel_CTL"):
			if not mc.getAttr("R_heel_CTL.mirrorMode", l=1):
				mc.setAttr("R_heel_CTL.mirrorMode", 0)

			if not mc.getAttr("R_heel_CTL.rotateOrder", l=1):
				mc.setAttr("R_heel_CTL.rotateOrder", 0)

			mc.xform("R_heel_CTL", a=1, t=[4.081275479794755e-07, -1.3999549978993553e-07, 4.476465829350573e-06])
			mc.xform("R_heel_CTL", a=1, ro=[-1.987846675914698e-16, 6.735086514358764e-37, 3.8825130388958945e-19])
			mc.xform("R_heel_CTL", r=1, s=[0.9999999999999998, 0.9999999999999997, 0.9999999999999999])

		if mc.objExists("R_toeTip_CTL"):
			if not mc.getAttr("R_toeTip_CTL.mirrorMode", l=1):
				mc.setAttr("R_toeTip_CTL.mirrorMode", 0)

			if not mc.getAttr("R_toeTip_CTL.rotateOrder", l=1):
				mc.setAttr("R_toeTip_CTL.rotateOrder", 0)

			mc.xform("R_toeTip_CTL", a=1, t=[4.883755351237085e-07, 2.6807851799537374e-08, -3.194789916838303e-06])
			mc.xform("R_toeTip_CTL", a=1, ro=[-1.987846675914698e-16, 6.735086514358764e-37, 3.8825130388958945e-19])
			mc.xform("R_toeTip_CTL", r=1, s=[1.0, 0.9999999999999997, 1.0])

		if mc.objExists("R_reverseBall_CTL"):
			if not mc.getAttr("R_reverseBall_CTL.mirrorMode", l=1):
				mc.setAttr("R_reverseBall_CTL.mirrorMode", 0)

			if not mc.getAttr("R_reverseBall_CTL.rotateOrder", l=1):
				mc.setAttr("R_reverseBall_CTL.rotateOrder", 0)

			mc.xform("R_reverseBall_CTL", a=1, t=[-3.392435462545862e-07, -3.163762255509184e-07, 3.736133032949951e-07])
			mc.xform("R_reverseBall_CTL", a=1, ro=[1.987846675914698e-16, -0.0, 0.0])
			mc.xform("R_reverseBall_CTL", r=1, s=[1.0000000000000002, 1.0, 0.9999999999999999])

		if mc.objExists("R_ankleOffset_CTL"):
			if not mc.getAttr("R_ankleOffset_CTL.mirrorMode", l=1):
				mc.setAttr("R_ankleOffset_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ankleOffset_CTL.rotateOrder", l=1):
				mc.setAttr("R_ankleOffset_CTL.rotateOrder", 0)

			mc.xform("R_ankleOffset_CTL", a=1, t=[-3.3719935466081097e-07, 3.727375822437651e-07, 3.788915260427572e-07])
			mc.xform("R_ankleOffset_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_ankleOffset_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_D_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_D_OFF_CTL", a=1, t=[-1.1102230246251565e-16, -1.1102230246251565e-16, 0.0])
			mc.xform("R_toe_IK_D_OFF_CTL", a=1, ro=[5.7177620286230646e-08, 1.272221872426707e-14, 3.1805546878115077e-15])
			mc.xform("R_toe_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_C_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_C_OFF_CTL", a=1, t=[1.1102230246251565e-16, -1.1102230246251565e-16, 0.0])
			mc.xform("R_toe_IK_C_OFF_CTL", a=1, ro=[5.7177620286230646e-08, 1.272221872426707e-14, 3.1805546878115077e-15])
			mc.xform("R_toe_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_B_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_B_OFF_CTL", a=1, t=[-1.1102230246251565e-16, 3.3306690738754696e-16, -2.7755575615628914e-17])
			mc.xform("R_toe_IK_B_OFF_CTL", a=1, ro=[5.7177620286230646e-08, 1.272221872426707e-14, 3.1805546878115077e-15])
			mc.xform("R_toe_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_A_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_A_OFF_CTL", a=1, t=[-1.1102230246251565e-16, -1.1102230246251565e-16, 2.7755575615628914e-17])
			mc.xform("R_toe_IK_A_OFF_CTL", a=1, ro=[5.7177620286230646e-08, 1.272221872426707e-14, 3.1805546878115077e-15])
			mc.xform("R_toe_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_CTL"):
			if not mc.getAttr("R_toe_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_toe_IK_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_toe_IK_CTL.mirrorMode", l=1):
				mc.setAttr("R_toe_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_toe_IK_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_CTL", a=1, t=[3.903816456762854e-07, 3.357680680160513e-07, 2.9938098708437444e-07])
			mc.xform("R_toe_IK_CTL", a=1, ro=[-4.134721085902572e-14, 2.2952312749860827e-30, 6.3611093629270335e-15])
			mc.xform("R_toe_IK_CTL", r=1, s=[1.0000000000000004, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_toe_FK_CTL"):
			if not mc.getAttr("R_toe_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_toe_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_toe_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_FK_CTL.rotateOrder", 0)

			mc.xform("R_toe_FK_CTL", a=1, t=[0.0, 5.551115123125783e-16, -1.3877787807814457e-16])
			mc.xform("R_toe_FK_CTL", a=1, ro=[-4.134721085902572e-14, 2.2952312749860827e-30, 6.3611093629270335e-15])
			mc.xform("R_toe_FK_CTL", r=1, s=[1.0000000000000004, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_upArm_FK_CTL"):
			if not mc.getAttr("R_upArm_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_upArm_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upArm_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_upArm_FK_CTL.rotateOrder", 0)

			mc.xform("R_upArm_FK_CTL", a=1, t=[-3.552713678800501e-15, -3.552713678800501e-15, 8.881784197001252e-16])
			mc.xform("R_upArm_FK_CTL", a=1, ro=[4.770832022195274e-15, -1.5902773407317588e-15, 1.9083328088781097e-14])
			mc.xform("R_upArm_FK_CTL", r=1, s=[1.0, 0.9999999999999994, 0.9999999999999999])

		if mc.objExists("R_loArm_FK_CTL"):
			if not mc.getAttr("R_loArm_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_loArm_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_loArm_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_loArm_FK_CTL.rotateOrder", 0)

			mc.xform("R_loArm_FK_CTL", a=1, t=[3.552713678800501e-15, 0.0, 1.1102230246251565e-16])
			mc.xform("R_loArm_FK_CTL", a=1, ro=[0.0, 3.578124016646456e-15, 0.0])
			mc.xform("R_loArm_FK_CTL", r=1, s=[0.9999999999999998, 1.0, 1.0])

		if mc.objExists("R_wrist_FK_CTL"):
			if not mc.getAttr("R_wrist_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_wrist_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_wrist_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_FK_CTL.rotateOrder", 0)

			mc.xform("R_wrist_FK_CTL", a=1, t=[2.6645352591003757e-15, -1.0658141036401503e-14, 1.3322676295501878e-15])
			mc.xform("R_wrist_FK_CTL", a=1, ro=[0.0, -3.975693351829396e-16, 0.0])
			mc.xform("R_wrist_FK_CTL", r=1, s=[1.0, 1.0, 0.9999999999999998])

		if mc.objExists("R_arm_IK_D_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_D_OFF_CTL", a=1, t=[0.0, -1.7763568394002505e-15, 4.440892098500626e-16])
			mc.xform("R_arm_IK_D_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_arm_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_C_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_C_OFF_CTL", a=1, t=[0.0, 1.7763568394002505e-15, -4.440892098500626e-16])
			mc.xform("R_arm_IK_C_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_arm_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_B_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_B_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 4.440892098500626e-16])
			mc.xform("R_arm_IK_B_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_arm_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_A_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_A_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 0.0])
			mc.xform("R_arm_IK_A_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_arm_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_CTL"):
			if not mc.getAttr("R_arm_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_arm_IK_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("R_arm_IK_CTL.mirrorMode", l=1):
				mc.setAttr("R_arm_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_arm_IK_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_CTL", a=1, t=[2.6645352591003757e-15, -1.0658141036401503e-14, 1.3322676295501878e-15])
			mc.xform("R_arm_IK_CTL", a=1, ro=[0.0, -3.975693351829396e-16, 0.0])
			mc.xform("R_arm_IK_CTL", r=1, s=[1.0, 1.0, 0.9999999999999998])

		if mc.objExists("R_wrist_IK_D_OFF_CTL"):
			if not mc.getAttr("R_wrist_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_D_OFF_CTL", a=1, t=[0.0, -1.7763568394002505e-15, 4.440892098500626e-16])
			mc.xform("R_wrist_IK_D_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_wrist_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_IK_C_OFF_CTL"):
			if not mc.getAttr("R_wrist_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_C_OFF_CTL", a=1, t=[0.0, 1.7763568394002505e-15, -4.440892098500626e-16])
			mc.xform("R_wrist_IK_C_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_wrist_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_IK_B_OFF_CTL"):
			if not mc.getAttr("R_wrist_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_B_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 4.440892098500626e-16])
			mc.xform("R_wrist_IK_B_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_wrist_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_IK_A_OFF_CTL"):
			if not mc.getAttr("R_wrist_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_A_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 0.0])
			mc.xform("R_wrist_IK_A_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_wrist_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_IK_CTL"):
			if not mc.getAttr("R_wrist_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_wrist_IK_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_wrist_IK_CTL.mirrorMode", l=1):
				mc.setAttr("R_wrist_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_wrist_IK_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_CTL", a=1, t=[2.6645352591003757e-15, -1.0658141036401503e-14, 1.3322676295501878e-15])
			mc.xform("R_wrist_IK_CTL", a=1, ro=[0.0, -3.975693351829396e-16, 0.0])
			mc.xform("R_wrist_IK_CTL", r=1, s=[1.0, 1.0, 0.9999999999999998])

		if mc.objExists("R_arm_PV_CTL"):
			if not mc.getAttr("R_arm_PV_CTL.mirrorMode", l=1):
				mc.setAttr("R_arm_PV_CTL.mirrorMode", 0)

			if not mc.getAttr("R_arm_PV_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_PV_CTL.rotateOrder", 0)

			mc.xform("R_arm_PV_CTL", a=1, t=[3.2335128565819105e-06, -1.7763568394002505e-15, -4.577116709114648e-05])
			mc.xform("R_arm_PV_CTL", a=1, ro=[178.77562524234102, 0.6177092716231222, 47.31947755068954])
			mc.xform("R_arm_PV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999994, 0.9999999999999998])

		if mc.objExists("R_shoulder_D_OFF_CTL"):
			if not mc.getAttr("R_shoulder_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_D_OFF_CTL", a=1, t=[-1.1102230246251565e-16, 0.0, 0.0])
			mc.xform("R_shoulder_D_OFF_CTL", a=1, ro=[-1.172829538789672e-14, -3.1805546814635168e-15, 7.951386703658796e-16])
			mc.xform("R_shoulder_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_C_OFF_CTL"):
			if not mc.getAttr("R_shoulder_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_C_OFF_CTL", a=1, t=[1.1102230246251565e-16, 0.0, -2.7755575615628914e-17])
			mc.xform("R_shoulder_C_OFF_CTL", a=1, ro=[-1.172829538789672e-14, -3.1805546814635168e-15, 7.951386703658796e-16])
			mc.xform("R_shoulder_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_B_OFF_CTL"):
			if not mc.getAttr("R_shoulder_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_B_OFF_CTL", a=1, t=[-1.1102230246251565e-16, 0.0, 0.0])
			mc.xform("R_shoulder_B_OFF_CTL", a=1, ro=[-1.172829538789672e-14, -3.1805546814635168e-15, 7.951386703658796e-16])
			mc.xform("R_shoulder_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_A_OFF_CTL"):
			if not mc.getAttr("R_shoulder_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_A_OFF_CTL", a=1, t=[-1.1102230246251565e-16, 0.0, -5.551115123125783e-17])
			mc.xform("R_shoulder_A_OFF_CTL", a=1, ro=[-1.172829538789672e-14, -3.1805546814635168e-15, 7.951386703658796e-16])
			mc.xform("R_shoulder_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_CTL"):
			if not mc.getAttr("R_shoulder_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_shoulder_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_shoulder_CTL.mirrorMode", l=1):
				mc.setAttr("R_shoulder_CTL.mirrorMode", 0)

			if not mc.getAttr("R_shoulder_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_CTL", a=1, t=[-3.3306690738754696e-16, 0.0, 5.551115123125783e-17])
			mc.xform("R_shoulder_CTL", a=1, ro=[0.0, 3.1805546814635168e-15, 0.0])
			mc.xform("R_shoulder_CTL", r=1, s=[1.0, 1.0, 1.0000000000000002])

		if mc.objExists("R_arm_IK_switch_D_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_D_OFF_CTL", a=1, t=[0.0, -1.7763568394002505e-15, 4.440892098500626e-16])
			mc.xform("R_arm_IK_switch_D_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_arm_IK_switch_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_C_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_C_OFF_CTL", a=1, t=[0.0, 1.7763568394002505e-15, -4.440892098500626e-16])
			mc.xform("R_arm_IK_switch_C_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_arm_IK_switch_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_B_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_B_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 4.440892098500626e-16])
			mc.xform("R_arm_IK_switch_B_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_arm_IK_switch_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_A_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_A_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 0.0])
			mc.xform("R_arm_IK_switch_A_OFF_CTL", a=1, ro=[-1.5902773407317588e-15, 3.1805546814635176e-15, -4.413906298050161e-32])
			mc.xform("R_arm_IK_switch_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_CTL"):
			if not mc.getAttr("R_arm_IK_switch_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_arm_IK_switch_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_arm_IK_switch_CTL.mirrorMode", l=1):
				mc.setAttr("R_arm_IK_switch_CTL.mirrorMode", 0)

			if not mc.getAttr("R_arm_IK_switch_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_CTL", a=1, t=[2.6645352591003757e-15, -1.0658141036401503e-14, 1.3322676295501878e-15])
			mc.xform("R_arm_IK_switch_CTL", a=1, ro=[0.0, -3.975693351829396e-16, 0.0])
			mc.xform("R_arm_IK_switch_CTL", r=1, s=[1.0, 1.0, 0.9999999999999998])

		# Apply contro shapes data
		data = {
			"C_cog_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_CTLShape", "degree": 1, "form": 0, "points": [[36.500891, 98.139605, -6.007186], [36.462392, 98.139605, -11.749509], [26.553836, 98.139605, -15.197408], [25.199756, 98.139605, -19.272178], [31.073793, 98.139605, -27.963555], [27.667425, 98.139605, -32.586554], [17.6231, 98.139605, -29.557981], [14.133523, 98.139605, -32.05878], [13.777607, 98.139605, -42.536641], [8.304413, 98.139605, -44.274543], [1.960935, 98.139605, -35.926261], [-2.331242, 98.139605, -35.89788], [-8.781196, 98.139605, -44.160069], [-14.230575, 98.139605, -42.349003], [-14.450246, 98.139605, -31.869828], [-17.90556, 98.139605, -29.323115], [-27.985864, 98.139605, -32.213726], [-31.329991, 98.139605, -27.545471], [-25.341917, 98.139605, -18.938068], [-26.64055, 98.139605, -14.845802], [-36.500891, 98.139605, -11.260745], [-36.462392, 98.139605, -5.518422], [-26.553836, 98.139605, -2.070523], [-25.199756, 98.139605, 2.004247], [-31.073793, 98.139605, 10.695624], [-27.667425, 98.139605, 15.318623], [-17.6231, 98.139605, 12.29005], [-14.133523, 98.139605, 14.790849], [-13.777607, 98.139605, 25.26871], [-8.304413, 98.139605, 27.006612], [-1.960935, 98.139605, 18.65833], [2.331242, 98.139605, 18.629949], [8.781196, 98.139605, 26.892138], [14.230575, 98.139605, 25.081072], [14.450246, 98.139605, 14.601897], [17.90556, 98.139605, 12.055184], [27.985864, 98.139605, 14.945795], [31.329991, 98.139605, 10.27754], [25.341917, 98.139605, 1.670137], [26.64055, 98.139605, -2.422129], [36.500891, 98.139605, -6.007186]]}]},
			"L_wrist_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[57.75169, 100.655213, -14.304163], [60.27273, 102.966713, -14.692755], [61.792733, 105.278213, -12.644283], [61.421298, 106.235665, -9.358709], [59.376011, 105.278213, -6.760678], [56.854971, 102.966713, -6.372086], [55.334968, 100.655213, -8.420558], [55.706403, 99.697761, -11.706132]]}]},
			"L_leg_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_CTLShape", "degree": 3, "form": 2, "points": [[15.941588, 7.470624, -15.709989], [9.978517, 7.470624, -19.826622], [4.015445, 7.470624, -15.709989], [1.545465, 7.470624, -5.771536], [4.015445, 7.470624, 4.166916], [9.978517, 7.470624, 8.283549], [15.941588, 7.470624, 4.166916], [18.411568, 7.470624, -5.771536]]}]},
			"L_outterBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_outterBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[25.667845, 1.430897, 4.18931], [25.668424, 1.543228, 4.297126], [25.669027, 1.43541, 4.409456], [25.668448, 1.323079, 4.30164], [25.667845, 1.430897, 4.18931], [25.778522, 1.433153, 4.298792], [25.669027, 1.43541, 4.409456], [25.55834, 1.433153, 4.299974], [25.668424, 1.543228, 4.297126], [25.778522, 1.433153, 4.298792], [25.668448, 1.323079, 4.30164], [25.55834, 1.433153, 4.299974], [25.667845, 1.430897, 4.18931], [25.778522, 1.433153, 4.298792], [15.282113, 1.433153, 4.35512]]}, {"shapeName": "L_outterBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[15.28038, 11.815187, 4.032164], [15.170875, 11.817444, 4.142828], [15.281561, 11.8197, 4.25231], [15.391067, 11.817444, 4.141646], [15.28038, 11.815187, 4.032164], [15.280959, 11.927508, 4.139981], [15.281561, 11.8197, 4.25231], [15.280983, 11.70737, 4.144494], [15.170875, 11.817444, 4.142828], [15.280959, 11.927508, 4.139981], [15.391067, 11.817444, 4.141646], [15.280983, 11.70737, 4.144494], [15.28038, 11.815187, 4.032164], [15.280959, 11.927508, 4.139981], [15.282113, 1.433153, 4.35512]]}, {"shapeName": "L_outterBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[15.337826, 1.756114, 14.737005], [15.227743, 1.646039, 14.739852], [15.337851, 1.535965, 14.741518], [15.447934, 1.646039, 14.738671], [15.337826, 1.756114, 14.737005], [15.338429, 1.648296, 14.849324], [15.337851, 1.535965, 14.741518], [15.337248, 1.643783, 14.629189], [15.227743, 1.646039, 14.739852], [15.338429, 1.648296, 14.849324], [15.447934, 1.646039, 14.738671], [15.337248, 1.643783, 14.629189], [15.337826, 1.756114, 14.737005], [15.338429, 1.648296, 14.849324], [15.282113, 1.433153, 4.35512]]}]},
			"C_torso_FK_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 107.429657, -8.700024], [-0.066058, 107.429657, -8.633965], [-0.0, 107.429657, -8.567907], [0.066058, 107.429657, -8.633965], [-0.0, 107.429657, -8.700024], [-0.0, 107.495709, -8.633965], [-0.0, 107.429657, -8.567907], [-0.0, 107.363598, -8.633965], [-0.066058, 107.429657, -8.633965], [-0.0, 107.495709, -8.633965], [0.066058, 107.429657, -8.633965], [-0.0, 107.363598, -8.633965], [-0.0, 107.429657, -8.700024], [-0.0, 107.495709, -8.633965], [-0.0, 101.197773, -8.633965]]}, {"shapeName": "C_torso_FK_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 101.197773, -8.700024], [-6.231884, 101.131714, -8.633965], [-6.231884, 101.197773, -8.567907], [-6.231884, 101.263831, -8.633965], [-6.231884, 101.197773, -8.700024], [-6.297936, 101.197773, -8.633965], [-6.231884, 101.197773, -8.567907], [-6.165825, 101.197773, -8.633965], [-6.231884, 101.131714, -8.633965], [-6.297936, 101.197773, -8.633965], [-6.231884, 101.263831, -8.633965], [-6.165825, 101.197773, -8.633965], [-6.231884, 101.197773, -8.700024], [-6.297936, 101.197773, -8.633965], [-0.0, 101.197773, -8.633965]]}, {"shapeName": "C_torso_FK_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 101.197773, -2.402082], [-0.0, 101.131714, -2.402082], [0.066058, 101.197773, -2.402082], [-0.0, 101.263831, -2.402082], [-0.066058, 101.197773, -2.402082], [-0.0, 101.197773, -2.336029], [0.066058, 101.197773, -2.402082], [-0.0, 101.197773, -2.46814], [-0.0, 101.131714, -2.402082], [-0.0, 101.197773, -2.336029], [-0.0, 101.263831, -2.402082], [-0.0, 101.197773, -2.46814], [-0.066058, 101.197773, -2.402082], [-0.0, 101.197773, -2.336029], [-0.0, 101.197773, -8.633965]]}]},
			"L_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_A_CTLShape", "degree": 3, "form": 2, "points": [[60.652195, 100.12518, -10.777941], [61.532504, 100.978468, -11.182067], [62.156911, 101.970904, -10.642117], [62.159646, 102.521134, -9.474384], [61.539109, 102.306841, -8.362911], [60.658801, 101.453554, -7.958784], [60.034393, 100.461117, -8.498734], [60.031658, 99.910888, -9.666468]]}]},
			"L_toe_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toe_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.940376, 1.527856, 17.841151], [9.830279, 1.4178, 17.838099], [9.940376, 1.307725, 17.835856], [10.050472, 1.417781, 17.838907], [9.940376, 1.527856, 17.841151], [9.939971, 1.415143, 17.948558], [9.940376, 1.307725, 17.835856], [9.94078, 1.420438, 17.728438], [9.830279, 1.4178, 17.838099], [9.939971, 1.415143, 17.948558], [10.050472, 1.417781, 17.838907], [9.94078, 1.420438, 17.728438], [9.940376, 1.527856, 17.841151], [9.939971, 1.415143, 17.948558], [9.978517, 1.667547, 7.455104]]}, {"shapeName": "L_toe_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.407886, 1.77853, 7.419621], [-0.407482, 1.671111, 7.306909], [-0.407886, 1.558398, 7.414326], [-0.40829, 1.665817, 7.527039], [-0.407886, 1.77853, 7.419621], [-0.517973, 1.668474, 7.41657], [-0.407886, 1.558398, 7.414326], [-0.297789, 1.668454, 7.417378], [-0.407482, 1.671111, 7.306909], [-0.517973, 1.668474, 7.41657], [-0.40829, 1.665817, 7.527039], [-0.297789, 1.668454, 7.417378], [-0.407886, 1.77853, 7.419621], [-0.517973, 1.668474, 7.41657], [9.978517, 1.667547, 7.455104]]}, {"shapeName": "L_toe_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.86842, -8.715913, 7.204942], [9.978921, -8.713275, 7.095281], [10.088613, -8.715932, 7.20575], [9.978112, -8.71857, 7.315411], [9.86842, -8.715913, 7.204942], [9.978517, -8.825978, 7.202699], [10.088613, -8.715932, 7.20575], [9.978517, -8.605857, 7.207993], [9.978921, -8.713275, 7.095281], [9.978517, -8.825978, 7.202699], [9.978112, -8.71857, 7.315411], [9.978517, -8.605857, 7.207993], [9.86842, -8.715913, 7.204942], [9.978517, -8.825978, 7.202699], [9.978517, 1.667547, 7.455104]]}]},
			"L_leg_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[15.345281, 7.470624, -14.716144], [9.978517, 7.470624, -18.421113], [4.611752, 7.470624, -14.716144], [2.38877, 7.470624, -5.771536], [4.611752, 7.470624, 3.173071], [9.978517, 7.470624, 6.878041], [15.345281, 7.470624, 3.173071], [17.568263, 7.470624, -5.771536]]}]},
			"L_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[79.063545, 102.950145, -15.715667], [79.072324, 103.059892, -15.60557], [79.063545, 102.950145, -15.495472], [79.054765, 102.840398, -15.60557], [79.063545, 102.950145, -15.715667], [79.173281, 102.941366, -15.60557], [79.063545, 102.950145, -15.495472], [78.953798, 102.958925, -15.60557], [79.072324, 103.059892, -15.60557], [79.173281, 102.941366, -15.60557], [79.054765, 102.840398, -15.60557], [78.953798, 102.958925, -15.60557], [79.063545, 102.950145, -15.715667], [79.173281, 102.941366, -15.60557], [68.71015, 103.778417, -15.60557]]}, {"shapeName": "L_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[69.538422, 114.131812, -15.715667], [69.428675, 114.140591, -15.60557], [69.538422, 114.131812, -15.495472], [69.648168, 114.123032, -15.60557], [69.538422, 114.131812, -15.715667], [69.547201, 114.241548, -15.60557], [69.538422, 114.131812, -15.495472], [69.529642, 114.022065, -15.60557], [69.428675, 114.140591, -15.60557], [69.547201, 114.241548, -15.60557], [69.648168, 114.123032, -15.60557], [69.529642, 114.022065, -15.60557], [69.538422, 114.131812, -15.715667], [69.547201, 114.241548, -15.60557], [68.71015, 103.778417, -15.60557]]}, {"shapeName": "L_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[68.71893, 103.888164, -5.219097], [68.600403, 103.787197, -5.219097], [68.70137, 103.66867, -5.219097], [68.819897, 103.769637, -5.219097], [68.71893, 103.888164, -5.219097], [68.71015, 103.778417, -5.10901], [68.70137, 103.66867, -5.219097], [68.71015, 103.778417, -5.329195], [68.600403, 103.787197, -5.219097], [68.71015, 103.778417, -5.10901], [68.819897, 103.769637, -5.219097], [68.71015, 103.778417, -5.329195], [68.71893, 103.888164, -5.219097], [68.71015, 103.778417, -5.10901], [68.71015, 103.778417, -15.60557]]}]},
			"C_head_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_CTLShape", "degree": 3, "form": 2, "points": [[11.926143, 176.101829, -4.86881], [0.0, 181.041616, -4.827551], [-11.926143, 176.101829, -4.86881], [-16.866103, 164.176102, -4.968417], [-11.926143, 152.250374, -5.068025], [0.0, 147.310587, -5.109283], [11.926143, 152.250374, -5.068025], [16.866103, 164.176102, -4.968417]]}]},
			"world_A_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -519.93], [230.985, 0.0, -288.72], [173.16, 0.0, -288.72], [173.16, 0.0, -173.115], [288.765, 0.0, -173.115], [288.765, 0.0, -230.94], [519.93, 0.0, 0.0], [288.72, 0.0, 230.985], [288.72, 0.0, 173.16], [173.115, 0.0, 173.16], [173.115, 0.0, 288.765], [230.94, 0.0, 288.765], [0.0, 0.0, 519.93], [-230.985, 0.0, 288.72], [-173.16, 0.0, 288.72], [-173.16, 0.0, 173.115], [-288.765, 0.0, 173.115], [-288.765, 0.0, 230.94], [-519.93, 0.0, 0.0], [-288.72, 0.0, -230.985], [-288.72, 0.0, -173.16], [-173.115, 0.0, -173.16], [-173.115, 0.0, -288.765], [-230.94, 0.0, -288.765], [0.0, 0.0, -519.93], [45.27, 0.63, -475.47], [41.31, 0.0, -471.24], [41.31, 0.0, -453.96], [37.71, 0.0, -453.96], [37.935, 0.0, -471.375], [35.37, 0.0, -470.07], [35.46, 0.0, -462.51], [31.815, 0.0, -462.51], [31.815, 0.0, -470.07], [29.565, 0.0, -471.375], [29.565, 0.0, -453.69], [25.92, 0.0, -453.69], [25.92, 0.0, -471.825], [28.845, 0.0, -474.75], [33.345, 0.0, -472.5], [38.295, 0.0, -474.75], [41.31, 0.0, -471.33], [38.295, 0.0, -474.75], [33.39, 0.0, -472.545], [28.845, 0.0, -474.705], [20.07, 0.0, -474.75], [23.04, 0.0, -471.825], [23.04, 0.0, -456.66], [20.07, 0.0, -453.69], [10.575, 0.0, -453.69], [7.65, 0.0, -456.66], [7.65, 0.0, -471.825], [10.575, 0.0, -474.75], [20.07, 0.0, -474.75], [18.945, 0.0, -471.375], [19.395, 0.0, -457.425], [11.25, 0.0, -457.515], [11.295, 0.0, -471.375], [18.99, 0.0, -471.465], [20.07, 0.0, -474.75], [10.575, 0.0, -474.75], [4.5, 0.0, -474.75], [4.725, 0.0, -453.69], [-5.535, 0.0, -453.69], [-8.505, 0.0, -456.66], [-8.505, 0.0, -463.005], [-5.49, 0.0, -465.93], [-5.31, 0.0, -466.155], [-11.205, 0.0, -474.66], [-11.205, 0.0, -474.75], [-6.975, 0.0, -474.75], [-1.08, 0.0, -466.2], [1.125, 0.0, -466.2], [1.125, 0.0, -457.2], [-4.545, 0.0, -457.2], [-4.59, 0.0, -462.555], [1.125, 0.0, -462.555], [1.125, 0.0, -474.75], [4.5, 0.0, -474.75], [-28.935, 0.0, -474.75], [-28.935, 0.0, -471.375], [-17.145, 0.0, -471.33], [-17.145, 0.0, -453.69], [-13.5, 0.0, -453.69], [-13.5, 0.0, -474.75], [-44.28, 0.0, -474.75], [-46.98, 0.0, -471.825], [-47.205, 0.0, -456.66], [-44.28, 0.0, -453.69], [-31.815, 0.0, -453.69], [-31.815, 0.0, -474.75], [-35.505, 0.0, -471.375], [-35.415, 0.0, -457.11], [-43.11, 0.0, -457.11], [-43.02, 0.0, -471.285], [-35.37, 0.0, -471.465], [-31.725, 0.0, -474.75]]}]},
			"C_cog_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_cog_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.231884, 98.139605, -8.700024], [6.231884, 98.205663, -8.633965], [6.231884, 98.139605, -8.567907], [6.231884, 98.073546, -8.633965], [6.231884, 98.139605, -8.700024], [6.297936, 98.139605, -8.633965], [6.231884, 98.139605, -8.567907], [6.165825, 98.139605, -8.633965], [6.231884, 98.205663, -8.633965], [6.297936, 98.139605, -8.633965], [6.231884, 98.073546, -8.633965], [6.165825, 98.139605, -8.633965], [6.231884, 98.139605, -8.700024], [6.297936, 98.139605, -8.633965], [-0.0, 98.139605, -8.633965]]}, {"shapeName": "C_cog_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.0, 104.371488, -8.700024], [-0.066058, 104.371488, -8.633965], [-0.0, 104.371488, -8.567907], [0.066058, 104.371488, -8.633965], [-0.0, 104.371488, -8.700024], [-0.0, 104.437541, -8.633965], [-0.0, 104.371488, -8.567907], [-0.0, 104.30543, -8.633965], [-0.066058, 104.371488, -8.633965], [-0.0, 104.437541, -8.633965], [0.066058, 104.371488, -8.633965], [-0.0, 104.30543, -8.633965], [-0.0, 104.371488, -8.700024], [-0.0, 104.437541, -8.633965], [-0.0, 98.139605, -8.633965]]}, {"shapeName": "C_cog_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.0, 98.205663, -2.402082], [-0.066058, 98.139605, -2.402082], [-0.0, 98.073546, -2.402082], [0.066058, 98.139605, -2.402082], [-0.0, 98.205663, -2.402082], [-0.0, 98.139605, -2.336029], [-0.0, 98.073546, -2.402082], [-0.0, 98.139605, -2.46814], [-0.066058, 98.139605, -2.402082], [-0.0, 98.139605, -2.336029], [0.066058, 98.139605, -2.402082], [-0.0, 98.139605, -2.46814], [-0.0, 98.205663, -2.402082], [-0.0, 98.139605, -2.336029], [-0.0, 98.139605, -8.633965]]}]},
			"L_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_C_CTLShape", "degree": 3, "form": 2, "points": [[66.303599, 95.18302, -11.301014], [67.293852, 95.880712, -11.747089], [68.162182, 96.675675, -11.217561], [68.399931, 97.102227, -10.022618], [67.86783, 96.910504, -8.862242], [66.877577, 96.212811, -8.416167], [66.009247, 95.417849, -8.945695], [65.771498, 94.991296, -10.140638]]}]},
			"L_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[74.428638, 85.097572, -3.695878], [74.488249, 85.177483, -3.576279], [74.371605, 85.128584, -3.485471], [74.311995, 85.048674, -3.605069], [74.428638, 85.097572, -3.695878], [74.459631, 85.025148, -3.561584], [74.371605, 85.128584, -3.485471], [74.340608, 85.201016, -3.619768], [74.488249, 85.177483, -3.576279], [74.459631, 85.025148, -3.561584], [74.311995, 85.048674, -3.605069], [74.340608, 85.201016, -3.619768], [74.428638, 85.097572, -3.695878], [74.459631, 85.025148, -3.561584], [68.785609, 93.409046, -6.335303]]}, {"shapeName": "L_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[77.127897, 99.469381, -5.082505], [77.039866, 99.572825, -5.006395], [77.070864, 99.500393, -4.872098], [77.158895, 99.396949, -4.948208], [77.127897, 99.469381, -5.082505], [77.187499, 99.549286, -4.962908], [77.070864, 99.500393, -4.872098], [77.011254, 99.420483, -4.991697], [77.039866, 99.572825, -5.006395], [77.187499, 99.549286, -4.962908], [77.158895, 99.396949, -4.948208], [77.011254, 99.420483, -4.991697], [77.127897, 99.469381, -5.082505], [77.187499, 99.549286, -4.962908], [68.785609, 93.409046, -6.335303]]}, {"shapeName": "L_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[66.183519, 94.936285, 3.603893], [66.035878, 94.959819, 3.560404], [66.007266, 94.807476, 3.575103], [66.154907, 94.783943, 3.618591], [66.183519, 94.936285, 3.603893], [66.066879, 94.887386, 3.694692], [66.007266, 94.807476, 3.575103], [66.123909, 94.856375, 3.484294], [66.035878, 94.959819, 3.560404], [66.066879, 94.887386, 3.694692], [66.154907, 94.783943, 3.618591], [66.123909, 94.856375, 3.484294], [66.183519, 94.936285, 3.603893], [66.066879, 94.887386, 3.694692], [68.785609, 93.409046, -6.335303]]}]},
			"R_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_D_CTLShape", "degree": 3, "form": 2, "points": [[-68.139891, 92.543426, -7.630837], [-69.222461, 93.171503, -7.946944], [-70.049129, 93.938729, -7.318975], [-70.135643, 94.395673, -6.114783], [-69.431327, 94.274665, -5.039768], [-68.348758, 93.646589, -4.723661], [-67.522089, 92.879363, -5.35163], [-67.435575, 92.422418, -6.555822]]}]},
			"R_arm_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-30.674815, 130.063272, 85.011199], [-30.756935, 130.140225, 84.9036], [-30.677189, 130.067976, 84.791068], [-30.595069, 129.991023, 84.898667], [-30.674815, 130.063272, 85.011199], [-30.601378, 130.146553, 84.902058], [-30.677189, 130.067976, 84.791068], [-30.750634, 129.984688, 84.900208], [-30.756935, 130.140225, 84.9036], [-30.601378, 130.146553, 84.902058], [-30.595069, 129.991023, 84.898667], [-30.750634, 129.984688, 84.900208], [-30.674815, 130.063272, 85.011199], [-30.601378, 130.146553, 84.902058], [-37.716685, 122.430181, 84.81387]]}, {"shapeName": "R_arm_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-45.350618, 129.465554, 85.156688], [-45.426437, 129.38697, 85.045697], [-45.352993, 129.470259, 84.936556], [-45.277174, 129.548842, 85.047547], [-45.350618, 129.465554, 85.156688], [-45.432732, 129.5425, 85.049089], [-45.352993, 129.470259, 84.936556], [-45.270872, 129.393306, 85.044154], [-45.426437, 129.38697, 85.045697], [-45.432732, 129.5425, 85.049089], [-45.277174, 129.548842, 85.047547], [-45.270872, 129.393306, 85.044154], [-45.350618, 129.465554, 85.156688], [-45.432732, 129.5425, 85.049089], [-37.716685, 122.430181, 84.81387]]}, {"shapeName": "R_arm_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-37.909593, 122.726705, 74.432839], [-37.903292, 122.571167, 74.429448], [-37.747727, 122.577503, 74.427906], [-37.754028, 122.73304, 74.431298], [-37.909593, 122.726705, 74.432839], [-37.829847, 122.654456, 74.320317], [-37.747727, 122.577503, 74.427906], [-37.827473, 122.649752, 74.540438], [-37.903292, 122.571167, 74.429448], [-37.829847, 122.654456, 74.320317], [-37.754028, 122.73304, 74.431298], [-37.827473, 122.649752, 74.540438], [-37.909593, 122.726705, 74.432839], [-37.829847, 122.654456, 74.320317], [-37.716685, 122.430181, 84.81387]]}]},
			"R_arm_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-65.588617, 95.83296, -7.765984], [-65.616732, 95.912981, -7.635411], [-65.504953, 95.83296, -7.562302], [-65.476837, 95.75294, -7.692874], [-65.588617, 95.83296, -7.765984], [-65.620798, 95.757349, -7.633742], [-65.504953, 95.83296, -7.562302], [-65.472765, 95.908579, -7.694547], [-65.616732, 95.912981, -7.635411], [-65.620798, 95.757349, -7.633742], [-65.476837, 95.75294, -7.692874], [-65.472765, 95.908579, -7.694547], [-65.588617, 95.83296, -7.765984], [-65.620798, 95.757349, -7.633742], [-58.56385, 102.966713, -10.53242]]}, {"shapeName": "R_arm_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.204449, 110.515778, -7.923782], [-65.088598, 110.591397, -7.852345], [-65.120786, 110.515778, -7.720101], [-65.236637, 110.44016, -7.791537], [-65.204449, 110.515778, -7.923782], [-65.232559, 110.595792, -7.793213], [-65.120786, 110.515778, -7.720101], [-65.09267, 110.435758, -7.850673], [-65.088598, 110.591397, -7.852345], [-65.232559, 110.595792, -7.793213], [-65.236637, 110.44016, -7.791537], [-65.09267, 110.435758, -7.850673], [-65.204449, 110.515778, -7.923782], [-65.232559, 110.595792, -7.793213], [-58.56385, 102.966713, -10.53242]]}, {"shapeName": "R_arm_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-54.687444, 103.046734, -0.896134], [-54.543477, 103.042331, -0.95527], [-54.547549, 102.886692, -0.953597], [-54.691516, 102.891095, -0.894462], [-54.687444, 103.046734, -0.896134], [-54.575669, 102.966713, -0.823034], [-54.547549, 102.886692, -0.953597], [-54.659328, 102.966713, -1.026707], [-54.543477, 103.042331, -0.95527], [-54.575669, 102.966713, -0.823034], [-54.691516, 102.891095, -0.894462], [-54.659328, 102.966713, -1.026707], [-54.687444, 103.046734, -0.896134], [-54.575669, 102.966713, -0.823034], [-58.56385, 102.966713, -10.53242]]}]},
			"R_ankleOffset_CTL": {"color": 20, "shapes": [{"shapeName": "R_ankleOffset_CTLShape", "degree": 1, "form": 0, "points": [[-9.978517, 4.867005, -6.774814], [-9.978517, 10.697845, -2.541692], [-9.978517, 12.132748, -2.541109], [-10.993147, 11.415005, -1.823949], [-9.978517, 12.132165, -1.106206], [-9.978517, 12.132748, -2.541109], [-8.963887, 11.415005, -1.823949], [-9.978517, 10.697845, -2.541692], [-9.978517, 10.697262, -1.106789], [-8.963887, 11.415005, -1.823949], [-9.978517, 12.132165, -1.106206], [-9.978517, 10.697262, -1.106789], [-10.993147, 11.415005, -1.823949], [-9.978517, 10.697845, -2.541692]]}]},
			"L_toeTip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toeTip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[20.339047, 1.500263, 14.150158], [20.339626, 1.612594, 14.257974], [20.340229, 1.504776, 14.370303], [20.33965, 1.392445, 14.262487], [20.339047, 1.500263, 14.150158], [20.449724, 1.50252, 14.25964], [20.340229, 1.504776, 14.370303], [20.229542, 1.50252, 14.260821], [20.339626, 1.612594, 14.257974], [20.449724, 1.50252, 14.25964], [20.33965, 1.392445, 14.262487], [20.229542, 1.50252, 14.260821], [20.339047, 1.500263, 14.150158], [20.449724, 1.50252, 14.25964], [9.953315, 1.50252, 14.315968]]}, {"shapeName": "L_toeTip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[9.951582, 11.884554, 13.993012], [9.842076, 11.88681, 14.103675], [9.952763, 11.889067, 14.213157], [10.062268, 11.88681, 14.102494], [9.951582, 11.884554, 13.993012], [9.95216, 11.996875, 14.100828], [9.952763, 11.889067, 14.213157], [9.952184, 11.776736, 14.105341], [9.842076, 11.88681, 14.103675], [9.95216, 11.996875, 14.100828], [10.062268, 11.88681, 14.102494], [9.952184, 11.776736, 14.105341], [9.951582, 11.884554, 13.993012], [9.95216, 11.996875, 14.100828], [9.953315, 1.50252, 14.315968]]}, {"shapeName": "L_toeTip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[10.009028, 1.82548, 24.697852], [9.898944, 1.715406, 24.7007], [10.009052, 1.605331, 24.702365], [10.119136, 1.715406, 24.699518], [10.009028, 1.82548, 24.697852], [10.009631, 1.717662, 24.810171], [10.009052, 1.605331, 24.702365], [10.008449, 1.713149, 24.590036], [9.898944, 1.715406, 24.7007], [10.009631, 1.717662, 24.810171], [10.119136, 1.715406, 24.699518], [10.008449, 1.713149, 24.590036], [10.009028, 1.82548, 24.697852], [10.009631, 1.717662, 24.810171], [9.953315, 1.50252, 14.315968]]}]},
			"L_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[71.652017, 85.867009, 1.967883], [71.675485, 85.954721, 2.09437], [71.537247, 85.910461, 2.15071], [71.513779, 85.822749, 2.024223], [71.652017, 85.867009, 1.967883], [71.642494, 85.80333, 2.10964], [71.537247, 85.910461, 2.15071], [71.546765, 85.974148, 2.008948], [71.675485, 85.954721, 2.09437], [71.642494, 85.80333, 2.10964], [71.513779, 85.822749, 2.024223], [71.546765, 85.974148, 2.008948], [71.652017, 85.867009, 1.967883], [71.642494, 85.80333, 2.10964], [67.078971, 93.946473, -2.690491]]}, {"shapeName": "L_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[74.763943, 100.149761, 0.526863], [74.658691, 100.2569, 0.567928], [74.649172, 100.193213, 0.70969], [74.754424, 100.086074, 0.668625], [74.763943, 100.149761, 0.526863], [74.787403, 100.237467, 0.653346], [74.649172, 100.193213, 0.70969], [74.625704, 100.105501, 0.583203], [74.658691, 100.2569, 0.567928], [74.787403, 100.237467, 0.653346], [74.754424, 100.086074, 0.668625], [74.625704, 100.105501, 0.583203], [74.763943, 100.149761, 0.526863], [74.787403, 100.237467, 0.653346], [67.078971, 93.946473, -2.690491]]}, {"shapeName": "L_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.746179, 96.062061, 5.968409], [61.61746, 96.081488, 5.882988], [61.584473, 95.93009, 5.898263], [61.713193, 95.910663, 5.983684], [61.746179, 96.062061, 5.968409], [61.607946, 96.0178, 6.024741], [61.584473, 95.93009, 5.898263], [61.722711, 95.97435, 5.841923], [61.61746, 96.081488, 5.882988], [61.607946, 96.0178, 6.024741], [61.713193, 95.910663, 5.983684], [61.722711, 95.97435, 5.841923], [61.746179, 96.062061, 5.968409], [61.607946, 96.0178, 6.024741], [67.078971, 93.946473, -2.690491]]}]},
			"C_midNeck_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[10.01796, 159.944122, -14.676332], [0.0, 160.805201, -18.025378], [-10.01796, 159.944122, -14.676332], [-14.167526, 157.865288, -6.591002], [-10.01796, 155.786454, 1.494328], [0.0, 154.925375, 4.843374], [10.01796, 155.786454, 1.494328], [14.167526, 157.865288, -6.591002]]}]},
			"R_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-69.140394, 92.609241, -1.211215], [-69.151956, 92.713474, -1.09613], [-69.025624, 92.652693, -1.028389], [-69.014062, 92.54846, -1.143474], [-69.140394, 92.609241, -1.211215], [-69.146837, 92.561389, -1.063197], [-69.025624, 92.652693, -1.028389], [-69.019175, 92.700552, -1.176412], [-69.151956, 92.713474, -1.09613], [-69.146837, 92.561389, -1.063197], [-69.014062, 92.54846, -1.143474], [-69.019175, 92.700552, -1.176412], [-69.140394, 92.609241, -1.211215], [-69.146837, 92.561389, -1.063197], [-63.061, 99.1955, -6.46032]]}, {"shapeName": "R_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-69.622743, 106.957401, -4.318509], [-69.501524, 107.048712, -4.283706], [-69.507973, 107.000853, -4.135682], [-69.629192, 106.909543, -4.170486], [-69.622743, 106.957401, -4.318509], [-69.634298, 107.061627, -4.203425], [-69.507973, 107.000853, -4.135682], [-69.496411, 106.89662, -4.250768], [-69.501524, 107.048712, -4.283706], [-69.634298, 107.061627, -4.203425], [-69.629192, 106.909543, -4.170486], [-69.496411, 106.89662, -4.250768], [-69.622743, 106.957401, -4.318509], [-69.634298, 107.061627, -4.203425], [-63.061, 99.1955, -6.46032]]}, {"shapeName": "R_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-57.716302, 101.32761, 2.187179], [-57.583521, 101.314688, 2.106897], [-57.578408, 101.162596, 2.139834], [-57.711189, 101.175518, 2.220117], [-57.716302, 101.32761, 2.187179], [-57.589975, 101.266827, 2.254912], [-57.578408, 101.162596, 2.139834], [-57.70474, 101.223377, 2.072094], [-57.583521, 101.314688, 2.106897], [-57.589975, 101.266827, 2.254912], [-57.711189, 101.175518, 2.220117], [-57.70474, 101.223377, 2.072094], [-57.716302, 101.32761, 2.187179], [-57.589975, 101.266827, 2.254912], [-63.061, 99.1955, -6.46032]]}]},
			"R_leg_IK_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-14.748974, 7.470624, -13.722298], [-9.978517, 7.470624, -17.015605], [-5.208059, 7.470624, -13.722298], [-3.232076, 7.470624, -5.771536], [-5.208059, 7.470624, 2.179226], [-9.978517, 7.470624, 5.472532], [-14.748974, 7.470624, 2.179226], [-16.724958, 7.470624, -5.771536]]}]},
			"R_upLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-9.978517, 80.783151, -3.523062], [-9.868419, 80.765401, -3.631719], [-9.978517, 80.747651, -3.740376], [-10.088614, 80.765401, -3.631719], [-9.978517, 80.783151, -3.523062], [-9.978517, 80.656754, -3.613971], [-9.978517, 80.747651, -3.740376], [-9.978517, 80.874058, -3.649469], [-9.868419, 80.765401, -3.631719], [-9.978517, 80.656754, -3.613971], [-10.088614, 80.765401, -3.631719], [-9.978517, 80.874058, -3.649469], [-9.978517, 80.783151, -3.523062], [-9.978517, 80.656754, -3.613971], [-9.978517, 91.015999, -5.306253]]}, {"shapeName": "R_upLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.407956, 91.033749, -5.197596], [0.407956, 91.124656, -5.324003], [0.407956, 90.998249, -5.41491], [0.407956, 90.907342, -5.288503], [0.407956, 91.033749, -5.197596], [0.518043, 91.015999, -5.306253], [0.407956, 90.998249, -5.41491], [0.297859, 91.015999, -5.306253], [0.407956, 91.124656, -5.324003], [0.518043, 91.015999, -5.306253], [0.407956, 90.907342, -5.288503], [0.297859, 91.015999, -5.306253], [0.407956, 91.033749, -5.197596], [0.518043, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253]]}, {"shapeName": "R_upLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.868419, 89.341465, -15.556851], [-9.978517, 89.450122, -15.574601], [-10.088614, 89.341465, -15.556851], [-9.978517, 89.232808, -15.5391], [-9.868419, 89.341465, -15.556851], [-9.978517, 89.323717, -15.665498], [-10.088614, 89.341465, -15.556851], [-9.978517, 89.359215, -15.448193], [-9.978517, 89.450122, -15.574601], [-9.978517, 89.323717, -15.665498], [-9.978517, 89.232808, -15.5391], [-9.978517, 89.359215, -15.448193], [-9.868419, 89.341465, -15.556851], [-9.978517, 89.323717, -15.665498], [-9.978517, 91.015999, -5.306253]]}]},
			"C_neckBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neckBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.386473, 151.589011, -8.318385], [10.386473, 151.668225, -8.18434], [10.386473, 151.534179, -8.105126], [10.386473, 151.454966, -8.239172], [10.386473, 151.589011, -8.318385], [10.49656, 151.561595, -8.211756], [10.386473, 151.534179, -8.105126], [10.276375, 151.561595, -8.211756], [10.386473, 151.668225, -8.18434], [10.49656, 151.561595, -8.211756], [10.386473, 151.454966, -8.239172], [10.276375, 151.561595, -8.211756], [10.386473, 151.589011, -8.318385], [10.49656, 151.561595, -8.211756], [0.0, 151.561595, -8.211756]]}, {"shapeName": "C_neckBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 161.648312, -5.73202], [-0.110097, 161.620896, -5.625391], [0.0, 161.59348, -5.518761], [0.110097, 161.620896, -5.625391], [0.0, 161.648312, -5.73202], [0.0, 161.727515, -5.597978], [0.0, 161.59348, -5.518761], [0.0, 161.514266, -5.652806], [-0.110097, 161.620896, -5.625391], [0.0, 161.727515, -5.597978], [0.110097, 161.620896, -5.625391], [0.0, 161.514266, -5.652806], [0.0, 161.648312, -5.73202], [0.0, 161.727515, -5.597978], [0.0, 151.561595, -8.211756]]}, {"shapeName": "C_neckBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 149.08186, 1.874961], [-0.110097, 148.97523, 1.847545], [0.0, 148.868601, 1.820129], [0.110097, 148.97523, 1.847545], [0.0, 149.08186, 1.874961], [0.0, 148.947817, 1.954164], [0.0, 148.868601, 1.820129], [0.0, 149.002646, 1.740915], [-0.110097, 148.97523, 1.847545], [0.0, 148.947817, 1.954164], [0.110097, 148.97523, 1.847545], [0.0, 149.002646, 1.740915], [0.0, 149.08186, 1.874961], [0.0, 148.947817, 1.954164], [0.0, 151.561595, -8.211756]]}]},
			"C_chest_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_chest_FK_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 127.606377, -14.721745], [0.0, 127.839344, -14.768085], [0.0, 128.036844, -14.900056], [0.0, 128.168814, -15.097556], [0.0, 128.215155, -15.330523], [0.0, 128.168814, -15.56349], [0.0, 128.036844, -15.76099], [0.0, 127.839344, -15.892961], [0.0, 127.606377, -15.939301], [0.0, 127.373409, -15.892961], [0.0, 127.17591, -15.76099], [0.0, 127.043939, -15.56349], [0.0, 126.997599, -15.330523], [0.0, 127.043939, -15.097556], [0.0, 127.17591, -14.900056], [0.0, 127.373409, -14.768085], [0.0, 127.606377, -14.721745], [0.0, 127.606377, -8.633965]]}]},
			"L_shoulder_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [5.51861, 146.415763, -1.982087], [7.627856, 146.240259, -3.192355], [8.433518, 146.173222, -3.654637], [4.774944, 146.240259, -8.164392], [0.902499, 146.415763, -10.027016], [-1.704686, 146.632699, -8.531036], [-2.050734, 146.808203, -4.247877], [-0.003484, 146.87524, 1.186442], [0.802179, 146.808203, 0.72416], [2.911425, 146.632699, -0.486107], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097]]}]},
			"L_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[73.481783, 87.999364, -8.591448], [73.553985, 88.079102, -8.478879], [73.45461, 88.021043, -8.374014], [73.382408, 87.941306, -8.486583], [73.481783, 87.999364, -8.591448], [73.535845, 87.925023, -8.465784], [73.45461, 88.021043, -8.374014], [73.400542, 88.095392, -8.499679], [73.553985, 88.079102, -8.478879], [73.535845, 87.925023, -8.465784], [73.382408, 87.941306, -8.486583], [73.400542, 88.095392, -8.499679], [73.481783, 87.999364, -8.591448], [73.535845, 87.925023, -8.465784], [67.085714, 96.046762, -10.081628]]}, {"shapeName": "L_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[75.192499, 102.535685, -9.82695], [75.111257, 102.631712, -9.735182], [75.165325, 102.557363, -9.609516], [75.246567, 102.461336, -9.701285], [75.192499, 102.535685, -9.82695], [75.264693, 102.615416, -9.714382], [75.165325, 102.557363, -9.609516], [75.093123, 102.477626, -9.722085], [75.111257, 102.631712, -9.735182], [75.264693, 102.615416, -9.714382], [75.246567, 102.461336, -9.701285], [75.093123, 102.477626, -9.722085], [75.192499, 102.535685, -9.82695], [75.264693, 102.615416, -9.714382], [67.085714, 96.046762, -10.081628]]}, {"shapeName": "L_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.889749, 97.138224, 0.178455], [65.736306, 97.154514, 0.157655], [65.718172, 97.000428, 0.170751], [65.871615, 96.984137, 0.191552], [65.889749, 97.138224, 0.178455], [65.790375, 97.080164, 0.28331], [65.718172, 97.000428, 0.170751], [65.817547, 97.058486, 0.065886], [65.736306, 97.154514, 0.157655], [65.790375, 97.080164, 0.28331], [65.871615, 96.984137, 0.191552], [65.817547, 97.058486, 0.065886], [65.889749, 97.138224, 0.178455], [65.790375, 97.080164, 0.28331], [67.085714, 96.046762, -10.081628]]}]},
			"R_leg_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[-17.911685, 8.650198, -5.58849], [-17.588678, 8.650198, -5.58849], [-17.527506, 8.322669, -5.639316], [-17.297976, 8.228692, -5.653899], [-17.020333, 8.417548, -5.624593], [-16.791929, 8.191846, -5.659617], [-16.983035, 7.917516, -5.702188], [-16.887974, 7.690671, -5.737389], [-16.556495, 7.630223, -5.74677], [-16.556495, 7.311025, -5.796303], [-16.887974, 7.250577, -5.805683], [-16.983035, 7.023762, -5.84088], [-16.791929, 6.749402, -5.883455], [-17.020333, 6.5237, -5.91848], [-17.297976, 6.712556, -5.889173], [-17.527506, 6.618579, -5.903756], [-17.588678, 6.29105, -5.954582], [-17.911685, 6.29105, -5.954582], [-17.972887, 6.618579, -5.903756], [-18.202417, 6.712556, -5.889173], [-18.48006, 6.5237, -5.91848], [-18.708443, 6.749402, -5.883455], [-18.517358, 7.023762, -5.84088], [-18.612419, 7.250577, -5.805683], [-18.943868, 7.311025, -5.796303], [-18.943868, 7.630223, -5.74677], [-18.612419, 7.690671, -5.737389], [-18.517358, 7.917516, -5.702188], [-18.708443, 8.191846, -5.659617], [-18.48006, 8.417548, -5.624593], [-18.202417, 8.228692, -5.653899], [-17.972887, 8.322669, -5.639316], [-17.911685, 8.650198, -5.58849]]}, {"shapeName": "R_leg_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[-18.100792, 7.817093, -5.717771], [-18.246026, 7.470624, -5.771536], [-18.100792, 7.124155, -5.825301], [-17.750186, 6.980669, -5.847567], [-17.399601, 7.124155, -5.825301], [-17.254367, 7.470624, -5.771536], [-17.399601, 7.817093, -5.717771], [-17.750186, 7.960579, -5.695505]]}, {"shapeName": "R_leg_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[-16.556495, 7.470624, -5.771536], [-9.978517, 7.470624, -5.771536]]}]},
			"R_arm_IK_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-57.379343, 106.982836, -7.947672], [-53.769482, 102.853114, -9.430442], [-55.928338, 102.853114, -14.686262], [-59.538199, 106.982836, -13.203492], [-63.358219, 103.080312, -11.634399], [-59.748358, 98.95059, -13.117168], [-57.589502, 98.95059, -7.861348], [-61.199363, 103.080312, -6.378579], [-57.379343, 106.982836, -7.947672], [-59.538199, 106.982836, -13.203492], [-55.928338, 102.853114, -14.686262], [-59.748358, 98.95059, -13.117168], [-63.358219, 103.080312, -11.634399], [-61.199363, 103.080312, -6.378579], [-57.589502, 98.95059, -7.861348], [-53.769482, 102.853114, -9.430442]]}]},
			"L_ankleOffset_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ankleOffset_PIV_CTLShape", "degree": 1, "form": 0, "points": [[20.364989, 7.4651, -5.881495], [20.364989, 7.580583, -5.77706], [20.364989, 7.476148, -5.661578], [20.364989, 7.360665, -5.766012], [20.364989, 7.4651, -5.881495], [20.475077, 7.470624, -5.771536], [20.364989, 7.476148, -5.661578], [20.254892, 7.470624, -5.771536], [20.364989, 7.580583, -5.77706], [20.475077, 7.470624, -5.771536], [20.364989, 7.360665, -5.766012], [20.254892, 7.470624, -5.771536], [20.364989, 7.4651, -5.881495], [20.475077, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_ankleOffset_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[9.978517, 17.83849, -6.402631], [9.868419, 17.844015, -6.292672], [9.978517, 17.849539, -6.182713], [10.088614, 17.844015, -6.292672], [9.978517, 17.83849, -6.402631], [9.978517, 17.953963, -6.298195], [9.978517, 17.849539, -6.182713], [9.978517, 17.734056, -6.287148], [9.868419, 17.844015, -6.292672], [9.978517, 17.953963, -6.298195], [10.088614, 17.844015, -6.292672], [9.978517, 17.734056, -6.287148], [9.978517, 17.83849, -6.402631], [9.978517, 17.953963, -6.298195], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_ankleOffset_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.978517, 8.101718, 4.59633], [9.868419, 7.99176, 4.601854], [9.978517, 7.881801, 4.607378], [10.088614, 7.99176, 4.601854], [9.978517, 8.101718, 4.59633], [9.978517, 7.997283, 4.711803], [9.978517, 7.881801, 4.607378], [9.978517, 7.986235, 4.491895], [9.868419, 7.99176, 4.601854], [9.978517, 7.997283, 4.711803], [10.088614, 7.99176, 4.601854], [9.978517, 7.986235, 4.491895], [9.978517, 8.101718, 4.59633], [9.978517, 7.997283, 4.711803], [9.978517, 7.470624, -5.771536]]}]},
			"L_shoulder_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_shoulder_PIV_CTLShape", "degree": 1, "form": 0, "points": [[13.145654, 145.77658, -6.485353], [13.207321, 145.886392, -6.393804], [13.255241, 145.77658, -6.294365], [13.193573, 145.666768, -6.385915], [13.145654, 145.77658, -6.485353], [13.295685, 145.768656, -6.444506], [13.255241, 145.77658, -6.294365], [13.105201, 145.784505, -6.335208], [13.207321, 145.886392, -6.393804], [13.295685, 145.768656, -6.444506], [13.193573, 145.666768, -6.385915], [13.105201, 145.784505, -6.335208], [13.145654, 145.77658, -6.485353], [13.295685, 145.768656, -6.444506], [4.215017, 146.524231, -1.234097]]}, {"shapeName": "L_shoulder_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[4.808705, 156.88376, -1.701684], [4.768253, 156.891685, -1.551539], [4.918293, 156.88376, -1.510696], [4.958745, 156.875834, -1.660842], [4.808705, 156.88376, -1.701684], [4.870372, 156.993561, -1.610134], [4.918293, 156.88376, -1.510696], [4.856625, 156.773948, -1.602246], [4.768253, 156.891685, -1.551539], [4.870372, 156.993561, -1.610134], [4.958745, 156.875834, -1.660842], [4.856625, 156.773948, -1.602246], [4.808705, 156.88376, -1.701684], [4.870372, 156.993561, -1.610134], [4.215017, 146.524231, -1.234097]]}, {"shapeName": "L_shoulder_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.391063, 146.634043, 7.770759], [9.288943, 146.532156, 7.829354], [9.377315, 146.414419, 7.778647], [9.479435, 146.516306, 7.720051], [9.391063, 146.634043, 7.770759], [9.438978, 146.524231, 7.870188], [9.377315, 146.414419, 7.778647], [9.329395, 146.524231, 7.679209], [9.288943, 146.532156, 7.829354], [9.438978, 146.524231, 7.870188], [9.479435, 146.516306, 7.720051], [9.329395, 146.524231, 7.679209], [9.391063, 146.634043, 7.770759], [9.438978, 146.524231, 7.870188], [4.215017, 146.524231, -1.234097]]}]},
			"R_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_B_CTLShape", "degree": 3, "form": 2, "points": [[-65.000393, 102.285212, -16.798184], [-64.905288, 103.474028, -17.29218], [-64.810182, 104.662844, -16.798184], [-64.770789, 105.155267, -15.60557], [-64.810182, 104.662844, -14.412956], [-64.905288, 103.474028, -13.91896], [-65.000393, 102.285212, -14.412956], [-65.039787, 101.792789, -15.60557]]}]},
			"R_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-69.319518, 94.483246, -9.758044], [-69.375531, 94.579392, -9.649134], [-69.292344, 94.504924, -9.54061], [-69.236331, 94.408778, -9.64952], [-69.319518, 94.483246, -9.758044], [-69.390141, 94.42534, -9.631949], [-69.292344, 94.504924, -9.54061], [-69.221713, 94.562836, -9.666707], [-69.375531, 94.579392, -9.649134], [-69.390141, 94.42534, -9.631949], [-69.236331, 94.408778, -9.64952], [-69.221713, 94.562836, -9.666707], [-69.319518, 94.483246, -9.758044], [-69.390141, 94.42534, -9.631949], [-61.3609, 100.98, -11.2889]]}, {"shapeName": "R_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.94049, 109.016899, -11.379416], [-67.842685, 109.096489, -11.288078], [-67.913316, 109.038577, -11.161982], [-68.011121, 108.958987, -11.253319], [-67.94049, 109.016899, -11.379416], [-67.996497, 109.113037, -11.270506], [-67.913316, 109.038577, -11.161982], [-67.857303, 108.942431, -11.270892], [-67.842685, 109.096489, -11.288078], [-67.996497, 109.113037, -11.270506], [-68.011121, 108.958987, -11.253319], [-67.857303, 108.942431, -11.270892], [-67.94049, 109.016899, -11.379416], [-67.996497, 109.113037, -11.270506], [-61.3609, 100.98, -11.2889]]}, {"shapeName": "R_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-60.148746, 102.087871, -1.032475], [-59.994928, 102.071315, -1.050048], [-60.009546, 101.917257, -1.032861], [-60.163364, 101.933813, -1.015289], [-60.148746, 102.087871, -1.032475], [-60.065561, 102.013402, -0.923961], [-60.009546, 101.917257, -1.032861], [-60.092733, 101.991725, -1.141385], [-59.994928, 102.071315, -1.050048], [-60.065561, 102.013402, -0.923961], [-60.163364, 101.933813, -1.015289], [-60.092733, 101.991725, -1.141385], [-60.148746, 102.087871, -1.032475], [-60.065561, 102.013402, -0.923961], [-61.3609, 100.98, -11.2889]]}]},
			"R_arm_IK_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_CTLShape", "degree": 1, "form": 0, "points": [[-56.871697, 108.704032, -6.839923], [-51.714753, 102.804429, -8.958165], [-54.798833, 102.804429, -16.466479], [-59.955777, 108.704032, -14.348237], [-65.412948, 103.128997, -12.106675], [-60.256004, 97.229394, -14.224917], [-57.171924, 97.229394, -6.716603], [-62.328868, 103.128997, -4.598361], [-56.871697, 108.704032, -6.839923], [-59.955777, 108.704032, -14.348237], [-54.798833, 102.804429, -16.466479], [-60.256004, 97.229394, -14.224917], [-65.412948, 103.128997, -12.106675], [-62.328868, 103.128997, -4.598361], [-57.171924, 97.229394, -6.716603], [-51.714753, 102.804429, -8.958165]]}]},
			"L_wrist_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[57.65017, 100.366276, -14.775631], [60.48634, 102.966713, -15.212796], [62.196343, 105.56715, -12.908266], [61.778478, 106.644284, -9.211995], [59.477531, 105.56715, -6.28921], [56.641361, 102.966713, -5.852044], [54.931357, 100.366276, -8.156575], [55.349222, 99.289142, -11.852846]]}]},
			"L_loArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[45.684849, 117.073958, -14.614821], [45.748818, 117.163398, -14.504588], [45.650922, 117.103638, -14.399289], [45.586952, 117.014197, -14.509522], [45.684849, 117.073958, -14.614821], [45.740567, 117.009206, -14.484654], [45.650922, 117.103638, -14.399289], [45.595197, 117.168397, -14.529458], [45.748818, 117.163398, -14.504588], [45.740567, 117.009206, -14.484654], [45.586952, 117.014197, -14.509522], [45.595197, 117.168397, -14.529458], [45.684849, 117.073958, -14.614821], [45.740567, 117.009206, -14.484654], [38.810577, 124.598083, -16.620529]]}, {"shapeName": "L_loArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[46.462662, 131.620969, -16.495544], [46.37301, 131.715408, -16.410181], [46.428734, 131.650648, -16.280012], [46.518386, 131.556209, -16.365375], [46.462662, 131.620969, -16.495544], [46.526624, 131.710402, -16.385311], [46.428734, 131.650648, -16.280012], [46.364765, 131.561208, -16.390245], [46.37301, 131.715408, -16.410181], [46.526624, 131.710402, -16.385311], [46.518386, 131.556209, -16.365375], [46.364765, 131.561208, -16.390245], [46.462662, 131.620969, -16.495544], [46.526624, 131.710402, -16.385311], [38.810577, 124.598083, -16.620529]]}, {"shapeName": "L_loArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[37.291174, 126.072638, -6.451555], [37.137553, 126.077637, -6.476425], [37.129308, 125.923437, -6.456489], [37.282929, 125.918439, -6.431619], [37.291174, 126.072638, -6.451555], [37.193279, 126.012876, -6.346266], [37.129308, 125.923437, -6.456489], [37.227205, 125.983198, -6.561788], [37.137553, 126.077637, -6.476425], [37.193279, 126.012876, -6.346266], [37.282929, 125.918439, -6.431619], [37.227205, 125.983198, -6.561788], [37.291174, 126.072638, -6.451555], [37.193279, 126.012876, -6.346266], [38.810577, 124.598083, -16.620529]]}]},
			"R_wrist_IK_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_CTLShape", "degree": 3, "form": 2, "points": [[-60.959382, 96.592941, -13.846122], [-64.110682, 99.482316, -14.331862], [-66.010685, 102.371691, -11.771272], [-65.546391, 103.568506, -7.664304], [-62.989783, 102.371691, -4.416766], [-59.838483, 99.482316, -3.931026], [-57.938479, 96.592941, -6.491616], [-58.402773, 95.396126, -10.598583]]}]},
			"L_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_A_CTLShape", "degree": 3, "form": 2, "points": [[60.754131, 99.938387, -12.468667], [61.569027, 100.813825, -12.954379], [62.261998, 101.786531, -12.464487], [62.427111, 102.286708, -11.285962], [61.967646, 102.021361, -10.109168], [61.152751, 101.145923, -9.623457], [60.459779, 100.173217, -10.113348], [60.294667, 99.67304, -11.291873]]}]},
			"R_leg_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-9.978517, -2.809889, -7.255449], [-9.868419, -2.793006, -7.364244], [-9.978517, -2.776123, -7.47304], [-10.088614, -2.793006, -7.364244], [-9.978517, -2.809889, -7.255449], [-9.978517, -2.901791, -7.381126], [-9.978517, -2.776123, -7.47304], [-9.978517, -2.68421, -7.347362], [-9.868419, -2.793006, -7.364244], [-9.978517, -2.901791, -7.381126], [-10.088614, -2.793006, -7.364244], [-9.978517, -2.68421, -7.347362], [-9.978517, -2.809889, -7.255449], [-9.978517, -2.901791, -7.381126], [-9.978517, 7.470624, -5.771536]]}, {"shapeName": "R_leg_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.407956, 7.453741, -5.662741], [0.407956, 7.579419, -5.754654], [0.407956, 7.487507, -5.880332], [0.407956, 7.361829, -5.788419], [0.407956, 7.453741, -5.662741], [0.518043, 7.470624, -5.771536], [0.407956, 7.487507, -5.880332], [0.297859, 7.470624, -5.771536], [0.407956, 7.579419, -5.754654], [0.518043, 7.470624, -5.771536], [0.407956, 7.361829, -5.788419], [0.297859, 7.470624, -5.771536], [0.407956, 7.453741, -5.662741], [0.518043, 7.470624, -5.771536], [-9.978517, 7.470624, -5.771536]]}, {"shapeName": "R_leg_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.868419, 9.063332, -16.035166], [-9.978517, 9.172127, -16.018283], [-10.088614, 9.063332, -16.035166], [-9.978517, 8.954537, -16.052049], [-9.868419, 9.063332, -16.035166], [-9.978517, 9.080213, -16.143951], [-10.088614, 9.063332, -16.035166], [-9.978517, 9.046449, -15.926371], [-9.978517, 9.172127, -16.018283], [-9.978517, 9.080213, -16.143951], [-9.978517, 8.954537, -16.052049], [-9.978517, 9.046449, -15.926371], [-9.868419, 9.063332, -16.035166], [-9.978517, 9.080213, -16.143951], [-9.978517, 7.470624, -5.771536]]}]},
			"R_upArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-26.45757, 137.863802, -12.512194], [-26.553665, 137.918409, -12.402527], [-26.487894, 137.823814, -12.297794], [-26.391799, 137.769208, -12.407461], [-26.45757, 137.863802, -12.512194], [-26.54581, 137.765352, -12.429963], [-26.487894, 137.823814, -12.297794], [-26.399647, 137.922271, -12.380023], [-26.553665, 137.918409, -12.402527], [-26.54581, 137.765352, -12.429963], [-26.391799, 137.769208, -12.407461], [-26.399647, 137.922271, -12.380023], [-26.45757, 137.863802, -12.512194], [-26.54581, 137.765352, -12.429963], [-19.577965, 145.245926, -10.049224]]}, {"shapeName": "R_upArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-27.197923, 152.303645, -9.923672], [-27.14, 152.362114, -9.791501], [-27.228247, 152.263657, -9.709273], [-27.286171, 152.205188, -9.841444], [-27.197923, 152.303645, -9.923672], [-27.294011, 152.358245, -9.814006], [-27.228247, 152.263657, -9.709273], [-27.132152, 152.20905, -9.81894], [-27.14, 152.362114, -9.791501], [-27.294011, 152.358245, -9.814006], [-27.286171, 152.205188, -9.841444], [-27.132152, 152.20905, -9.81894], [-27.197923, 152.303645, -9.923672], [-27.294011, 152.358245, -9.814006], [-19.577965, 145.245926, -10.049224]]}, {"shapeName": "R_upArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-21.089259, 143.434289, 0.066353], [-20.935241, 143.438151, 0.088857], [-20.927393, 143.285088, 0.061419], [-21.081411, 143.281225, 0.038914], [-21.089259, 143.434289, 0.066353], [-21.023487, 143.339696, 0.171076], [-20.927393, 143.285088, 0.061419], [-20.993164, 143.379682, -0.043314], [-20.935241, 143.438151, 0.088857], [-21.023487, 143.339696, 0.171076], [-21.081411, 143.281225, 0.038914], [-20.993164, 143.379682, -0.043314], [-21.089259, 143.434289, 0.066353], [-21.023487, 143.339696, 0.171076], [-19.577965, 145.245926, -10.049224]]}]},
			"L_legBase_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 89.281001, -5.022824], [9.978517, 86.473729, -4.56423], [9.978517, 85.401445, -4.389062], [9.978517, 87.551951, 2.036067], [9.978517, 91.025602, 5.656683], [9.978517, 94.495597, 5.089826], [9.978517, 96.63649, 0.55202], [9.978517, 96.630553, -6.223444], [9.978517, 95.558268, -6.048276], [9.978517, 92.750996, -5.589682], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}]},
			"C_head_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_head_FK_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 164.260844, -15.114363], [0.0, 164.649754, -15.188351], [0.0, 164.980746, -15.405546], [0.0, 165.203439, -15.732863], [0.0, 165.283913, -16.120483], [0.0, 165.209925, -16.509393], [0.0, 164.99273, -16.840385], [0.0, 164.665412, -17.063078], [0.0, 164.277792, -17.143552], [0.0, 163.888882, -17.069564], [0.0, 163.55789, -16.852369], [0.0, 163.335197, -16.525052], [0.0, 163.254723, -16.137432], [0.0, 163.328711, -15.748522], [0.0, 163.545906, -15.41753], [0.0, 163.873224, -15.194837], [0.0, 164.260844, -15.114363], [0.0, 164.176102, -4.968417]]}]},
			"L_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[69.140371, 92.609215, -1.211216], [69.151933, 92.713448, -1.096131], [69.025601, 92.652667, -1.02839], [69.014039, 92.548434, -1.143475], [69.140371, 92.609215, -1.211216], [69.146814, 92.561363, -1.063198], [69.025601, 92.652667, -1.02839], [69.019152, 92.700526, -1.176413], [69.151933, 92.713448, -1.096131], [69.146814, 92.561363, -1.063198], [69.014039, 92.548434, -1.143475], [69.019152, 92.700526, -1.176413], [69.140371, 92.609215, -1.211216], [69.146814, 92.561363, -1.063198], [63.060977, 99.195474, -6.460321]]}, {"shapeName": "L_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[69.62272, 106.957375, -4.31851], [69.501501, 107.048686, -4.283707], [69.50795, 107.000827, -4.135683], [69.629169, 106.909517, -4.170487], [69.62272, 106.957375, -4.31851], [69.634275, 107.061601, -4.203426], [69.50795, 107.000827, -4.135683], [69.496388, 106.896594, -4.250769], [69.501501, 107.048686, -4.283707], [69.634275, 107.061601, -4.203426], [69.629169, 106.909517, -4.170487], [69.496388, 106.896594, -4.250769], [69.62272, 106.957375, -4.31851], [69.634275, 107.061601, -4.203426], [63.060977, 99.195474, -6.460321]]}, {"shapeName": "L_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[57.716279, 101.327584, 2.187178], [57.583498, 101.314662, 2.106896], [57.578385, 101.16257, 2.139833], [57.711166, 101.175492, 2.220116], [57.716279, 101.327584, 2.187178], [57.589952, 101.266801, 2.254911], [57.578385, 101.16257, 2.139833], [57.704717, 101.223351, 2.072093], [57.583498, 101.314662, 2.106896], [57.589952, 101.266801, 2.254911], [57.711166, 101.175492, 2.220116], [57.704717, 101.223351, 2.072093], [57.716279, 101.327584, 2.187178], [57.589952, 101.266801, 2.254911], [63.060977, 99.195474, -6.460321]]}]},
			"R_wrist_IK_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-57.95473, 101.233088, -13.361227], [-59.84551, 102.966713, -13.652671], [-60.985512, 104.700338, -12.116317], [-60.706936, 105.418427, -9.652136], [-59.172971, 104.700338, -7.703613], [-57.282191, 102.966713, -7.412169], [-56.142188, 101.233088, -8.948523], [-56.420765, 100.514999, -11.412704]]}]},
			"R_innerBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_innerBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.025762, 1.922447, 7.68369], [5.026366, 2.030265, 7.571361], [5.026943, 1.917933, 7.463544], [5.026341, 1.810116, 7.575874], [5.025762, 1.922447, 7.68369], [5.136438, 1.92019, 7.574208], [5.026943, 1.917933, 7.463544], [4.916257, 1.92019, 7.573026], [5.026366, 2.030265, 7.571361], [5.136438, 1.92019, 7.574208], [5.026341, 1.810116, 7.575874], [4.916257, 1.92019, 7.573026], [5.025762, 1.922447, 7.68369], [5.136438, 1.92019, 7.574208], [-5.35997, 1.92019, 7.51788]]}, {"shapeName": "R_innerBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.359419, 12.306737, 7.41507], [-5.468924, 12.304481, 7.304406], [-5.358237, 12.302224, 7.194924], [-5.248732, 12.304481, 7.305588], [-5.359419, 12.306737, 7.41507], [-5.358815, 12.414545, 7.30274], [-5.358237, 12.302224, 7.194924], [-5.35884, 12.194407, 7.307254], [-5.468924, 12.304481, 7.304406], [-5.358815, 12.414545, 7.30274], [-5.248732, 12.304481, 7.305588], [-5.35884, 12.194407, 7.307254], [-5.359419, 12.306737, 7.41507], [-5.358815, 12.414545, 7.30274], [-5.35997, 1.92019, 7.51788]]}, {"shapeName": "R_innerBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-5.304232, 1.817378, -2.868518], [-5.414341, 1.707303, -2.866852], [-5.304257, 1.597229, -2.864005], [-5.194149, 1.707303, -2.86567], [-5.304232, 1.817378, -2.868518], [-5.303654, 1.705048, -2.976324], [-5.304257, 1.597229, -2.864005], [-5.304836, 1.709561, -2.756188], [-5.414341, 1.707303, -2.866852], [-5.303654, 1.705048, -2.976324], [-5.194149, 1.707303, -2.86567], [-5.304836, 1.709561, -2.756188], [-5.304232, 1.817378, -2.868518], [-5.303654, 1.705048, -2.976324], [-5.35997, 1.92019, 7.51788]]}]},
			"C_midNeck_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_midNeck_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.386473, 157.892703, -6.697631], [10.386473, 157.971917, -6.563586], [10.386473, 157.837872, -6.484373], [10.386473, 157.758658, -6.618418], [10.386473, 157.892703, -6.697631], [10.49656, 157.865288, -6.591002], [10.386473, 157.837872, -6.484373], [10.276375, 157.865288, -6.591002], [10.386473, 157.971917, -6.563586], [10.49656, 157.865288, -6.591002], [10.386473, 157.758658, -6.618418], [10.276375, 157.865288, -6.591002], [10.386473, 157.892703, -6.697631], [10.49656, 157.865288, -6.591002], [0.0, 157.865288, -6.591002]]}, {"shapeName": "C_midNeck_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 167.952004, -4.111266], [-0.110097, 167.924588, -4.004637], [0.0, 167.897173, -3.898007], [0.110097, 167.924588, -4.004637], [0.0, 167.952004, -4.111266], [0.0, 168.031208, -3.977224], [0.0, 167.897173, -3.898007], [0.0, 167.817959, -4.032053], [-0.110097, 167.924588, -4.004637], [0.0, 168.031208, -3.977224], [0.110097, 167.924588, -4.004637], [0.0, 167.817959, -4.032053], [0.0, 167.952004, -4.111266], [0.0, 168.031208, -3.977224], [0.0, 157.865288, -6.591002]]}, {"shapeName": "C_midNeck_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 155.385552, 3.495714], [-0.110097, 155.278923, 3.468299], [0.0, 155.172293, 3.440883], [0.110097, 155.278923, 3.468299], [0.0, 155.385552, 3.495714], [0.0, 155.25151, 3.574918], [0.0, 155.172293, 3.440883], [0.0, 155.306338, 3.361669], [-0.110097, 155.278923, 3.468299], [0.0, 155.25151, 3.574918], [0.110097, 155.278923, 3.468299], [0.0, 155.306338, 3.361669], [0.0, 155.385552, 3.495714], [0.0, 155.25151, 3.574918], [0.0, 157.865288, -6.591002]]}]},
			"R_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_D_CTLShape", "degree": 3, "form": 2, "points": [[-68.611826, 92.279258, -10.723038], [-69.639408, 92.927285, -11.159496], [-70.545066, 93.672582, -10.620351], [-70.798277, 94.078563, -9.421425], [-70.250715, 93.907411, -8.265032], [-69.223132, 93.259384, -7.828574], [-68.317474, 92.514087, -8.367719], [-68.064264, 92.108106, -9.566645]]}]},
			"L_toeTip_CTL": {"color": 20, "shapes": [{"shapeName": "L_toeTip_CTLShape", "degree": 1, "form": 0, "points": [[9.969646, 1.564909, 17.359174], [9.964314, 0.529695, 16.365568], [10.978817, 1.544112, 16.339327], [9.969646, 1.564909, 17.359174], [8.949587, 1.544112, 16.350217], [9.964314, 0.529695, 16.365568], [9.958758, 1.523316, 15.33037], [8.949587, 1.544112, 16.350217], [9.964091, 2.558529, 16.323976], [9.969646, 1.564909, 17.359174], [10.978817, 1.544112, 16.339327], [9.958758, 1.523316, 15.33037], [9.964091, 2.558529, 16.323976], [10.978817, 1.544112, 16.339327]]}]},
			"C_chest_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.869458, 127.606377, -14.358514], [0.0, 130.528511, -16.729695], [-6.869458, 127.606377, -14.358514], [-9.714875, 124.684242, -8.633965], [-6.869458, 127.606377, -2.909417], [0.0, 130.528511, -0.538236], [6.869458, 127.606377, -2.909417], [9.714875, 124.684242, -8.633965]]}]},
			"L_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[71.898708, 91.671036, -9.155361], [71.959062, 91.76344, -9.045536], [71.871534, 91.692714, -8.937928], [71.811179, 91.60031, -9.047753], [71.898708, 91.671036, -9.155361], [71.965547, 91.608731, -9.029301], [71.871534, 91.692714, -8.937928], [71.804688, 91.755026, -9.06399], [71.959062, 91.76344, -9.045536], [71.965547, 91.608731, -9.029301], [71.811179, 91.60031, -9.047753], [71.804688, 91.755026, -9.06399], [71.898708, 91.671036, -9.155361], [71.965547, 91.608731, -9.029301], [64.297138, 98.582871, -10.68298]]}, {"shapeName": "L_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[71.286285, 106.266798, -10.68712], [71.192265, 106.350789, -10.595749], [71.259112, 106.288477, -10.469687], [71.353132, 106.204487, -10.561058], [71.286285, 106.266798, -10.68712], [71.346633, 106.359195, -10.577295], [71.259112, 106.288477, -10.469687], [71.198757, 106.196072, -10.579512], [71.192265, 106.350789, -10.595749], [71.346633, 106.359195, -10.577295], [71.353132, 106.204487, -10.561058], [71.198757, 106.196072, -10.579512], [71.286285, 106.266798, -10.68712], [71.346633, 106.359195, -10.577295], [64.297138, 98.582871, -10.68298]]}, {"shapeName": "L_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[63.089326, 99.687, -0.42564], [62.934951, 99.678586, -0.444094], [62.941443, 99.52387, -0.427857], [63.095818, 99.532284, -0.409403], [63.089326, 99.687, -0.42564], [63.001799, 99.616273, -0.318042], [62.941443, 99.52387, -0.427857], [63.028971, 99.594596, -0.535465], [62.934951, 99.678586, -0.444094], [63.001799, 99.616273, -0.318042], [63.095818, 99.532284, -0.409403], [63.028971, 99.594596, -0.535465], [63.089326, 99.687, -0.42564], [63.001799, 99.616273, -0.318042], [64.297138, 98.582871, -10.68298]]}]},
			"R_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-72.63744, 88.356132, -4.661676], [-72.693792, 88.440588, -4.54363], [-72.580407, 88.387145, -4.451268], [-72.524056, 88.30269, -4.569314], [-72.63744, 88.356132, -4.661676], [-72.672994, 88.287225, -4.526663], [-72.580407, 88.387145, -4.451268], [-72.544848, 88.45606, -4.586284], [-72.693792, 88.440588, -4.54363], [-72.672994, 88.287225, -4.526663], [-72.524056, 88.30269, -4.569314], [-72.544848, 88.45606, -4.586284], [-72.63744, 88.356132, -4.661676], [-72.672994, 88.287225, -4.526663], [-66.5641, 96.3359, -7.36885]]}, {"shapeName": "R_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-74.598968, 102.824967, -6.262573], [-74.506376, 102.924895, -6.187181], [-74.541935, 102.855979, -6.052166], [-74.634527, 102.756051, -6.127558], [-74.598968, 102.824967, -6.262573], [-74.655312, 102.909416, -6.144529], [-74.541935, 102.855979, -6.052166], [-74.485584, 102.771524, -6.170211], [-74.506376, 102.924895, -6.187181], [-74.655312, 102.909416, -6.144529], [-74.634527, 102.756051, -6.127558], [-74.485584, 102.771524, -6.170211], [-74.598968, 102.824967, -6.262573], [-74.655312, 102.909416, -6.144529], [-66.5641, 96.3359, -7.36885]]}, {"shapeName": "R_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-63.958752, 97.867684, 2.568793], [-63.809808, 97.883157, 2.526139], [-63.789016, 97.729786, 2.543109], [-63.93796, 97.714313, 2.585762], [-63.958752, 97.867684, 2.568793], [-63.84537, 97.81424, 2.661145], [-63.789016, 97.729786, 2.543109], [-63.902401, 97.783229, 2.450747], [-63.809808, 97.883157, 2.526139], [-63.84537, 97.81424, 2.661145], [-63.93796, 97.714313, 2.585762], [-63.902401, 97.783229, 2.450747], [-63.958752, 97.867684, 2.568793], [-63.84537, 97.81424, 2.661145], [-66.5641, 96.3359, -7.36885]]}]},
			"R_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-71.652046, 85.867036, 1.967884], [-71.675514, 85.954748, 2.094371], [-71.537276, 85.910488, 2.150711], [-71.513808, 85.822776, 2.024224], [-71.652046, 85.867036, 1.967884], [-71.642523, 85.803357, 2.109641], [-71.537276, 85.910488, 2.150711], [-71.546794, 85.974175, 2.008949], [-71.675514, 85.954748, 2.094371], [-71.642523, 85.803357, 2.109641], [-71.513808, 85.822776, 2.024224], [-71.546794, 85.974175, 2.008949], [-71.652046, 85.867036, 1.967884], [-71.642523, 85.803357, 2.109641], [-67.079, 93.9465, -2.69049]]}, {"shapeName": "R_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-74.763972, 100.149788, 0.526864], [-74.65872, 100.256927, 0.567929], [-74.649201, 100.19324, 0.709691], [-74.754453, 100.086101, 0.668626], [-74.763972, 100.149788, 0.526864], [-74.787432, 100.237494, 0.653347], [-74.649201, 100.19324, 0.709691], [-74.625733, 100.105528, 0.583204], [-74.65872, 100.256927, 0.567929], [-74.787432, 100.237494, 0.653347], [-74.754453, 100.086101, 0.668626], [-74.625733, 100.105528, 0.583204], [-74.763972, 100.149788, 0.526864], [-74.787432, 100.237494, 0.653347], [-67.079, 93.9465, -2.69049]]}, {"shapeName": "R_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.746208, 96.062088, 5.96841], [-61.617489, 96.081515, 5.882989], [-61.584502, 95.930117, 5.898264], [-61.713222, 95.91069, 5.983685], [-61.746208, 96.062088, 5.96841], [-61.607975, 96.017827, 6.024742], [-61.584502, 95.930117, 5.898264], [-61.72274, 95.974377, 5.841924], [-61.617489, 96.081515, 5.882989], [-61.607975, 96.017827, 6.024742], [-61.713222, 95.91069, 5.983685], [-61.72274, 95.974377, 5.841924], [-61.746208, 96.062088, 5.96841], [-61.607975, 96.017827, 6.024742], [-67.079, 93.9465, -2.69049]]}]},
			"L_heel_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_heel_PIV_CTLShape", "degree": 1, "form": 0, "points": [[20.204977, 0.988078, -10.833164], [20.205555, 1.100409, -10.725348], [20.206158, 0.992591, -10.613019], [20.20558, 0.88026, -10.720835], [20.204977, 0.988078, -10.833164], [20.315653, 0.990335, -10.723682], [20.206158, 0.992591, -10.613019], [20.095472, 0.990335, -10.722501], [20.205555, 1.100409, -10.725348], [20.315653, 0.990335, -10.723682], [20.20558, 0.88026, -10.720835], [20.095472, 0.990335, -10.722501], [20.204977, 0.988078, -10.833164], [20.315653, 0.990335, -10.723682], [9.819244, 0.990335, -10.667355]]}, {"shapeName": "L_heel_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[9.817511, 11.372369, -10.99031], [9.708006, 11.374625, -10.879647], [9.818693, 11.376882, -10.770165], [9.928198, 11.374625, -10.880828], [9.817511, 11.372369, -10.99031], [9.81809, 11.484689, -10.882494], [9.818693, 11.376882, -10.770165], [9.818114, 11.264551, -10.877981], [9.708006, 11.374625, -10.879647], [9.81809, 11.484689, -10.882494], [9.928198, 11.374625, -10.880828], [9.818114, 11.264551, -10.877981], [9.817511, 11.372369, -10.99031], [9.81809, 11.484689, -10.882494], [9.819244, 0.990335, -10.667355]]}, {"shapeName": "L_heel_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.874958, 1.313295, -0.28547], [9.764874, 1.203221, -0.282623], [9.874982, 1.093146, -0.280957], [9.985066, 1.203221, -0.283804], [9.874958, 1.313295, -0.28547], [9.87556, 1.205477, -0.173151], [9.874982, 1.093146, -0.280957], [9.874379, 1.200964, -0.393286], [9.764874, 1.203221, -0.282623], [9.87556, 1.205477, -0.173151], [9.985066, 1.203221, -0.283804], [9.874379, 1.200964, -0.393286], [9.874958, 1.313295, -0.28547], [9.87556, 1.205477, -0.173151], [9.819244, 0.990335, -10.667355]]}]},
			"L_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_D_CTLShape", "degree": 3, "form": 2, "points": [[66.824758, 92.99635, -4.060637], [67.958067, 93.613648, -4.090874], [68.576415, 94.42591, -3.300786], [68.317579, 94.957324, -2.153196], [67.333184, 94.896596, -1.320345], [66.199875, 94.279298, -1.290109], [65.581527, 93.467036, -2.080196], [65.840364, 92.935622, -3.227786]]}]},
			"L_arm_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[57.379343, 106.982836, -7.947672], [53.769482, 102.853114, -9.430442], [55.928338, 102.853114, -14.686262], [59.538199, 106.982836, -13.203492], [63.358219, 103.080312, -11.634399], [59.748358, 98.95059, -13.117168], [57.589502, 98.95059, -7.861348], [61.199363, 103.080312, -6.378579], [57.379343, 106.982836, -7.947672], [59.538199, 106.982836, -13.203492], [55.928338, 102.853114, -14.686262], [59.748358, 98.95059, -13.117168], [63.358219, 103.080312, -11.634399], [61.199363, 103.080312, -6.378579], [57.589502, 98.95059, -7.861348], [53.769482, 102.853114, -9.430442]]}]},
			"L_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_B_CTLShape", "degree": 3, "form": 2, "points": [[62.935737, 98.066385, -7.706969], [63.940073, 98.862649, -7.860704], [64.429447, 99.853877, -7.194114], [64.117189, 100.459421, -6.097678], [63.186217, 100.324563, -5.213673], [62.181881, 99.528299, -5.059939], [61.692507, 98.537072, -5.726528], [62.004765, 97.931528, -6.822964]]}]},
			"R_arm_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-63.237977, 106.923591, -8.612498], [-63.073805, 106.735777, -8.679932], [-62.864445, 106.882328, -8.765928], [-62.696634, 106.801122, -8.834857], [-62.658311, 106.534674, -8.850599], [-62.419377, 106.527368, -8.948742], [-62.367194, 106.791025, -8.970177], [-62.19541, 106.861887, -9.040738], [-61.994031, 106.702759, -9.123455], [-61.820297, 106.880246, -9.194817], [-61.955873, 107.106598, -9.139129], [-61.880736, 107.287989, -9.169992], [-61.634275, 107.329426, -9.271227], [-61.627517, 107.587731, -9.274003], [-61.871423, 107.644157, -9.173817], [-61.936933, 107.829872, -9.146909], [-61.789755, 108.047561, -9.207363], [-61.953926, 108.235374, -9.139929], [-62.163302, 108.088841, -9.053926], [-62.331113, 108.170047, -8.984997], [-62.369436, 108.436495, -8.969256], [-62.60836, 108.44379, -8.871116], [-62.660569, 108.180127, -8.849671], [-62.832337, 108.109282, -8.779117], [-63.0337, 108.268393, -8.696406], [-63.207434, 108.090906, -8.625043], [-63.071874, 107.864572, -8.680726], [-63.147027, 107.683163, -8.649856], [-63.393461, 107.641732, -8.548632], [-63.40023, 107.383438, -8.545852], [-63.156324, 107.327013, -8.646037], [-63.090814, 107.141297, -8.672946], [-63.237977, 106.923591, -8.612498]]}, {"shapeName": "R_arm_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-62.880644, 107.496789, -8.759274], [-62.765883, 107.773886, -8.806413], [-62.503488, 107.88209, -8.914193], [-62.247193, 107.758014, -9.019468], [-62.147102, 107.474381, -9.06058], [-62.261864, 107.197283, -9.013441], [-62.524258, 107.089079, -8.905662], [-62.780544, 107.213143, -8.800391]]}, {"shapeName": "R_arm_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-61.907164, 106.791502, -9.159136], [-58.56385, 102.966713, -10.53242]]}]},
			"C_neck_FK_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_C_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 162.495451, -15.876833], [0.0, 162.890731, -15.854948], [0.0, 163.2643, -15.986004], [0.0, 163.559289, -16.250031], [0.0, 163.730776, -16.606847], [0.0, 163.752662, -17.002127], [0.0, 163.621606, -17.375695], [0.0, 163.357579, -17.670685], [0.0, 163.000763, -17.842172], [0.0, 162.605483, -17.864058], [0.0, 162.231915, -17.733001], [0.0, 161.936925, -17.468974], [0.0, 161.765438, -17.112159], [0.0, 161.743552, -16.716879], [0.0, 161.874609, -16.34331], [0.0, 162.138636, -16.048321], [0.0, 162.495451, -15.876833], [0.0, 159.968892, -6.05014]]}]},
			"R_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-74.428629, 85.097526, -3.695875], [-74.48824, 85.177437, -3.576276], [-74.371596, 85.128538, -3.485468], [-74.311986, 85.048628, -3.605066], [-74.428629, 85.097526, -3.695875], [-74.459622, 85.025102, -3.561581], [-74.371596, 85.128538, -3.485468], [-74.340599, 85.20097, -3.619765], [-74.48824, 85.177437, -3.576276], [-74.459622, 85.025102, -3.561581], [-74.311986, 85.048628, -3.605066], [-74.340599, 85.20097, -3.619765], [-74.428629, 85.097526, -3.695875], [-74.459622, 85.025102, -3.561581], [-68.7856, 93.409, -6.3353]]}, {"shapeName": "R_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-77.127888, 99.469335, -5.082502], [-77.039857, 99.572779, -5.006392], [-77.070855, 99.500347, -4.872095], [-77.158886, 99.396903, -4.948205], [-77.127888, 99.469335, -5.082502], [-77.18749, 99.54924, -4.962905], [-77.070855, 99.500347, -4.872095], [-77.011245, 99.420437, -4.991694], [-77.039857, 99.572779, -5.006392], [-77.18749, 99.54924, -4.962905], [-77.158886, 99.396903, -4.948205], [-77.011245, 99.420437, -4.991694], [-77.127888, 99.469335, -5.082502], [-77.18749, 99.54924, -4.962905], [-68.7856, 93.409, -6.3353]]}, {"shapeName": "R_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-66.18351, 94.936239, 3.603896], [-66.035869, 94.959773, 3.560407], [-66.007257, 94.80743, 3.575106], [-66.154898, 94.783897, 3.618594], [-66.18351, 94.936239, 3.603896], [-66.06687, 94.88734, 3.694695], [-66.007257, 94.80743, 3.575106], [-66.1239, 94.856329, 3.484297], [-66.035869, 94.959773, 3.560407], [-66.06687, 94.88734, 3.694695], [-66.154898, 94.783897, 3.618594], [-66.1239, 94.856329, 3.484297], [-66.18351, 94.936239, 3.603896], [-66.06687, 94.88734, 3.694695], [-68.7856, 93.409, -6.3353]]}]},
			"L_legBase_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 88.785288, -4.941845], [9.978517, 85.175938, -4.352223], [9.978517, 83.797286, -4.127007], [9.978517, 86.562223, 4.133872], [9.978517, 91.028345, 8.788951], [9.978517, 95.489768, 8.060134], [9.978517, 98.242345, 2.225812], [9.978517, 98.234711, -6.485499], [9.978517, 96.856059, -6.260283], [9.978517, 93.24671, -5.670661], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}]},
			"C_hip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_hip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.231884, 98.139605, -8.700024], [6.231884, 98.205663, -8.633965], [6.231884, 98.139605, -8.567907], [6.231884, 98.073546, -8.633965], [6.231884, 98.139605, -8.700024], [6.297936, 98.139605, -8.633965], [6.231884, 98.139605, -8.567907], [6.165825, 98.139605, -8.633965], [6.231884, 98.205663, -8.633965], [6.297936, 98.139605, -8.633965], [6.231884, 98.073546, -8.633965], [6.165825, 98.139605, -8.633965], [6.231884, 98.139605, -8.700024], [6.297936, 98.139605, -8.633965], [-0.0, 98.139605, -8.633965]]}, {"shapeName": "C_hip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.0, 104.371488, -8.700024], [-0.066058, 104.371488, -8.633965], [-0.0, 104.371488, -8.567907], [0.066058, 104.371488, -8.633965], [-0.0, 104.371488, -8.700024], [-0.0, 104.437541, -8.633965], [-0.0, 104.371488, -8.567907], [-0.0, 104.30543, -8.633965], [-0.066058, 104.371488, -8.633965], [-0.0, 104.437541, -8.633965], [0.066058, 104.371488, -8.633965], [-0.0, 104.30543, -8.633965], [-0.0, 104.371488, -8.700024], [-0.0, 104.437541, -8.633965], [-0.0, 98.139605, -8.633965]]}, {"shapeName": "C_hip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.0, 98.205663, -2.402082], [-0.066058, 98.139605, -2.402082], [-0.0, 98.073546, -2.402082], [0.066058, 98.139605, -2.402082], [-0.0, 98.205663, -2.402082], [-0.0, 98.139605, -2.336029], [-0.0, 98.073546, -2.402082], [-0.0, 98.139605, -2.46814], [-0.066058, 98.139605, -2.402082], [-0.0, 98.139605, -2.336029], [0.066058, 98.139605, -2.402082], [-0.0, 98.139605, -2.46814], [-0.0, 98.205663, -2.402082], [-0.0, 98.139605, -2.336029], [-0.0, 98.139605, -8.633965]]}]},
			"L_legEnd_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_legEnd_FK_CTLShape", "degree": 3, "form": 2, "points": [[13.953898, 6.861021, -1.843173], [9.978517, 6.608516, -0.215995], [6.003136, 6.861021, -1.843173], [4.356482, 7.470624, -5.771536], [6.003136, 8.080227, -9.6999], [9.978517, 8.332732, -11.327078], [13.953898, 8.080227, -9.6999], [15.600551, 7.470624, -5.771536]]}]},
			"R_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-73.481769, 87.999402, -8.59142], [-73.553971, 88.07914, -8.478851], [-73.454596, 88.021081, -8.373986], [-73.382394, 87.941344, -8.486555], [-73.481769, 87.999402, -8.59142], [-73.535831, 87.925061, -8.465756], [-73.454596, 88.021081, -8.373986], [-73.400528, 88.09543, -8.499651], [-73.553971, 88.07914, -8.478851], [-73.535831, 87.925061, -8.465756], [-73.382394, 87.941344, -8.486555], [-73.400528, 88.09543, -8.499651], [-73.481769, 87.999402, -8.59142], [-73.535831, 87.925061, -8.465756], [-67.0857, 96.0468, -10.0816]]}, {"shapeName": "R_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-75.192485, 102.535723, -9.826922], [-75.111243, 102.63175, -9.735154], [-75.165311, 102.557401, -9.609488], [-75.246553, 102.461374, -9.701257], [-75.192485, 102.535723, -9.826922], [-75.264679, 102.615454, -9.714354], [-75.165311, 102.557401, -9.609488], [-75.093109, 102.477664, -9.722057], [-75.111243, 102.63175, -9.735154], [-75.264679, 102.615454, -9.714354], [-75.246553, 102.461374, -9.701257], [-75.093109, 102.477664, -9.722057], [-75.192485, 102.535723, -9.826922], [-75.264679, 102.615454, -9.714354], [-67.0857, 96.0468, -10.0816]]}, {"shapeName": "R_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-65.889735, 97.138262, 0.178483], [-65.736292, 97.154552, 0.157683], [-65.718158, 97.000466, 0.170779], [-65.871601, 96.984175, 0.19158], [-65.889735, 97.138262, 0.178483], [-65.790361, 97.080202, 0.283338], [-65.718158, 97.000466, 0.170779], [-65.817533, 97.058524, 0.065914], [-65.736292, 97.154552, 0.157683], [-65.790361, 97.080202, 0.283338], [-65.871601, 96.984175, 0.19158], [-65.817533, 97.058524, 0.065914], [-65.889735, 97.138262, 0.178483], [-65.790361, 97.080202, 0.283338], [-67.0857, 96.0468, -10.0816]]}]},
			"R_shoulder_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_CTLShape", "degree": 3, "form": 0, "points": [[-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-5.46491, 146.524231, 0.944207], [-7.487268, 146.524231, 4.468761], [-8.259742, 146.524231, 5.815024], [-15.752501, 145.836506, -0.273757], [-18.838341, 145.411468, -6.729352], [-16.338557, 145.411468, -11.085962], [-9.207998, 145.836506, -11.679475], [-0.170292, 146.524231, -8.283219], [-0.942766, 146.524231, -6.936956], [-2.965125, 146.524231, -3.412402], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097]]}]},
			"L_innerBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_innerBall_CTLShape", "degree": 1, "form": 0, "points": [[3.336185, 1.940984, 8.543172], [3.330852, 0.905771, 7.549566], [4.345356, 1.920187, 7.523325], [3.336185, 1.940984, 8.543172], [2.316125, 1.920187, 7.534214], [3.330852, 0.905771, 7.549566], [3.325297, 1.899391, 6.514367], [2.316125, 1.920187, 7.534214], [3.330629, 2.934604, 7.507974], [3.336185, 1.940984, 8.543172], [4.345356, 1.920187, 7.523325], [3.325297, 1.899391, 6.514367], [3.330629, 2.934604, 7.507974], [4.345356, 1.920187, 7.523325]]}]},
			"C_neckBase_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[12.880235, 154.234382, -18.607181], [0.0, 150.035069, -24.277439], [-12.880235, 154.234382, -18.607181], [-18.215391, 156.868009, -6.847414], [-12.880235, 148.888809, 2.183669], [0.0, 142.475292, 5.125243], [12.880235, 148.888809, 2.183669], [18.215391, 156.868009, -6.847414]]}]},
			"R_leg_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-14.738418, 8.178368, -5.661709], [-14.544613, 8.178368, -5.661709], [-14.50791, 7.981851, -5.692204], [-14.370192, 7.925465, -5.700954], [-14.203606, 8.038778, -5.68337], [-14.066564, 7.903357, -5.704385], [-14.181228, 7.738759, -5.729927], [-14.124191, 7.602652, -5.751048], [-13.925303, 7.566383, -5.756676], [-13.925303, 7.374865, -5.786396], [-14.124191, 7.338596, -5.792024], [-14.181228, 7.202507, -5.813143], [-14.066564, 7.037891, -5.838688], [-14.203606, 6.90247, -5.859702], [-14.370192, 7.015783, -5.842118], [-14.50791, 6.959397, -5.850868], [-14.544613, 6.76288, -5.881364], [-14.738418, 6.76288, -5.881364], [-14.775139, 6.959397, -5.850868], [-14.912857, 7.015783, -5.842118], [-15.079443, 6.90247, -5.859702], [-15.216473, 7.037891, -5.838688], [-15.101822, 7.202507, -5.813143], [-15.158858, 7.338596, -5.792024], [-15.357727, 7.374865, -5.786396], [-15.357727, 7.566383, -5.756676], [-15.158858, 7.602652, -5.751048], [-15.101822, 7.738759, -5.729927], [-15.216473, 7.903357, -5.704385], [-15.079443, 8.038778, -5.68337], [-14.912857, 7.925465, -5.700954], [-14.775139, 7.981851, -5.692204], [-14.738418, 8.178368, -5.661709]]}, {"shapeName": "R_leg_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-14.851882, 7.678505, -5.739277], [-14.939022, 7.470624, -5.771536], [-14.851882, 7.262743, -5.803795], [-14.641518, 7.176651, -5.817155], [-14.431167, 7.262743, -5.803795], [-14.344027, 7.470624, -5.771536], [-14.431167, 7.678505, -5.739277], [-14.641518, 7.764597, -5.725918]]}, {"shapeName": "R_leg_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-13.925303, 7.470624, -5.771536], [-9.978517, 7.470624, -5.771536]]}]},
			"R_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_B_CTLShape", "degree": 3, "form": 2, "points": [[-59.191712, 99.107888, -5.585468], [-59.325236, 100.144685, -4.828114], [-58.512024, 100.941091, -4.219194], [-57.228443, 101.030583, -4.115405], [-56.226397, 100.360738, -4.577545], [-56.092873, 99.323941, -5.334899], [-56.906085, 98.527534, -5.943819], [-58.189666, 98.438043, -6.047608]]}]},
			"C_world_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_world_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 0.0, -0.054255], [5.118355, 0.054255, 0.0], [5.118355, 0.0, 0.054255], [5.118355, -0.054255, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [5.118355, 0.0, 0.054255], [5.0641, 0.0, 0.0], [5.118355, 0.054255, 0.0], [5.172605, 0.0, 0.0], [5.118355, -0.054255, 0.0], [5.0641, 0.0, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 5.118355, -0.054255], [-0.054255, 5.118355, 0.0], [0.0, 5.118355, 0.054255], [0.054255, 5.118355, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 5.118355, 0.054255], [0.0, 5.0641, 0.0], [-0.054255, 5.118355, 0.0], [0.0, 5.172605, 0.0], [0.054255, 5.118355, 0.0], [0.0, 5.0641, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 0.054255, 5.118355], [-0.054255, 0.0, 5.118355], [0.0, -0.054255, 5.118355], [0.054255, 0.0, 5.118355], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, -0.054255, 5.118355], [0.0, 0.0, 5.0641], [-0.054255, 0.0, 5.118355], [0.0, 0.0, 5.172605], [0.054255, 0.0, 5.118355], [0.0, 0.0, 5.0641], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, 0.0, 0.0]]}]},
			"R_hand_CTL": {"color": 18, "shapes": [{"shapeName": "R_hand_CTLShape", "degree": 3, "form": 2, "points": [[-62.29304, 113.113013, -11.725034], [-61.100425, 113.113013, -12.21903], [-59.907811, 113.113013, -11.725034], [-59.413815, 113.113013, -10.53242], [-59.907811, 113.113013, -9.339806], [-61.100425, 113.113013, -8.84581], [-62.29304, 113.113013, -9.339806], [-62.787036, 113.113013, -10.53242]]}, {"shapeName": "R_hand_CTLShape1", "degree": 3, "form": 2, "points": [[-61.100425, 114.305627, -11.725034], [-61.100425, 113.113013, -12.21903], [-61.100425, 111.920398, -11.725034], [-61.100425, 111.426402, -10.53242], [-61.100425, 111.920398, -9.339806], [-61.100425, 113.113013, -8.84581], [-61.100425, 114.305627, -9.339806], [-61.100425, 114.799623, -10.53242]]}, {"shapeName": "R_hand_CTLShape2", "degree": 3, "form": 2, "points": [[-59.907811, 114.305627, -10.53242], [-59.413815, 113.113013, -10.53242], [-59.907811, 111.920398, -10.53242], [-61.100425, 111.426402, -10.53242], [-62.29304, 111.920398, -10.53242], [-62.787036, 113.113013, -10.53242], [-62.29304, 114.305627, -10.53242], [-61.100425, 114.799623, -10.53242]]}]},
			"R_arm_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[-64.406508, 107.91281, -8.132517], [-64.201294, 107.678043, -8.21681], [-63.939593, 107.861232, -8.324305], [-63.72983, 107.759724, -8.410467], [-63.681926, 107.426664, -8.430143], [-63.383258, 107.417531, -8.552823], [-63.31803, 107.747103, -8.579616], [-63.1033, 107.83568, -8.667817], [-62.851577, 107.63677, -8.771214], [-62.634409, 107.858629, -8.860417], [-62.803879, 108.141569, -8.790806], [-62.709958, 108.368308, -8.829385], [-62.401881, 108.420104, -8.955929], [-62.393433, 108.742986, -8.959399], [-62.698316, 108.813517, -8.834167], [-62.780204, 109.045662, -8.800531], [-62.596231, 109.317772, -8.876098], [-62.801445, 109.55254, -8.791806], [-63.063165, 109.369373, -8.684303], [-63.272928, 109.470881, -8.598141], [-63.320832, 109.803941, -8.578465], [-63.619487, 109.813059, -8.45579], [-63.684749, 109.483481, -8.428984], [-63.899458, 109.394925, -8.340791], [-64.151162, 109.593813, -8.237402], [-64.368331, 109.371954, -8.148199], [-64.19888, 109.089036, -8.217802], [-64.292821, 108.862276, -8.179215], [-64.600864, 108.810486, -8.052685], [-64.609325, 108.487619, -8.049209], [-64.304443, 108.417087, -8.174441], [-64.222555, 108.184943, -8.208077], [-64.406508, 107.91281, -8.132517]]}, {"shapeName": "R_arm_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[-63.959843, 108.629307, -8.315988], [-63.816391, 108.97568, -8.374911], [-63.488398, 109.110935, -8.509636], [-63.168028, 108.955839, -8.64123], [-63.042915, 108.601298, -8.69262], [-63.186367, 108.254925, -8.633697], [-63.51436, 108.11967, -8.498972], [-63.834717, 108.274751, -8.367384]]}, {"shapeName": "R_arm_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[-62.742993, 107.747699, -8.815815], [-58.56385, 102.966713, -10.53242]]}]},
			"L_arm_PV_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_PV_CTLShape", "degree": 1, "form": 0, "points": [[38.889805, 127.780623, -117.039834], [38.889805, 125.751363, -117.039834], [38.889805, 125.751363, -119.069094], [38.889805, 127.780623, -119.069094], [40.919065, 127.780623, -119.069094], [40.919065, 125.751363, -119.069094], [40.919065, 125.751363, -117.039834], [40.919065, 127.780623, -117.039834], [38.889805, 127.780623, -117.039834], [38.889805, 127.780623, -119.069094], [38.889805, 125.751363, -119.069094], [40.919065, 125.751363, -119.069094], [40.919065, 127.780623, -119.069094], [40.919065, 127.780623, -117.039834], [40.919065, 125.751363, -117.039834], [38.889805, 125.751363, -117.039834]]}]},
			"R_legBase_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 89.033144, -4.982335], [-9.978517, 85.824834, -4.458226], [-9.978517, 84.599366, -4.258034], [-9.978517, 87.057087, 3.084969], [-9.978517, 91.026973, 7.222817], [-9.978517, 94.992682, 6.57498], [-9.978517, 97.439417, 1.388916], [-9.978517, 97.432632, -6.354472], [-9.978517, 96.207164, -6.15428], [-9.978517, 92.998853, -5.630171], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253]]}]},
			"C_cog_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[25.550624, 98.139605, -6.79522], [25.523674, 98.139605, -10.814846], [18.587685, 98.139605, -13.228375], [17.639829, 98.139605, -16.080714], [21.751655, 98.139605, -22.164678], [19.367197, 98.139605, -25.400778], [12.33617, 98.139605, -23.280776], [9.893466, 98.139605, -25.031336], [9.644325, 98.139605, -32.365838], [5.813089, 98.139605, -33.58237], [1.372654, 98.139605, -27.738573], [-1.63187, 98.139605, -27.718706], [-6.146837, 98.139605, -33.502238], [-9.961402, 98.139605, -32.234492], [-10.115172, 98.139605, -24.899069], [-12.533892, 98.139605, -23.11637], [-19.590105, 98.139605, -25.139798], [-21.930994, 98.139605, -21.872019], [-17.739342, 98.139605, -15.846838], [-18.648385, 98.139605, -12.982251], [-25.550624, 98.139605, -10.472711], [-25.523674, 98.139605, -6.453085], [-18.587685, 98.139605, -4.039556], [-17.639829, 98.139605, -1.187217], [-21.751655, 98.139605, 4.896747], [-19.367197, 98.139605, 8.132847], [-12.33617, 98.139605, 6.012845], [-9.893466, 98.139605, 7.763405], [-9.644325, 98.139605, 15.097907], [-5.813089, 98.139605, 16.314439], [-1.372654, 98.139605, 10.470642], [1.63187, 98.139605, 10.450775], [6.146837, 98.139605, 16.234307], [9.961402, 98.139605, 14.966561], [10.115172, 98.139605, 7.631138], [12.533892, 98.139605, 5.848439], [19.590105, 98.139605, 7.871867], [21.930994, 98.139605, 4.604088], [17.739342, 98.139605, -1.421093], [18.648385, 98.139605, -4.28568], [25.550624, 98.139605, -6.79522]]}]},
			"R_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.72087, 94.786265, -6.671079], [-68.761808, 94.886966, -6.559606], [-68.663837, 94.817277, -6.460672], [-68.622899, 94.716576, -6.572145], [-68.72087, 94.786265, -6.671079], [-68.772871, 94.733786, -6.53403], [-68.663837, 94.817277, -6.460672], [-68.611828, 94.869763, -6.597724], [-68.761808, 94.886966, -6.559606], [-68.772871, 94.733786, -6.53403], [-68.622899, 94.716576, -6.572145], [-68.611828, 94.869763, -6.597724], [-68.72087, 94.786265, -6.671079], [-68.772871, 94.733786, -6.53403], [-61.0957, 101.216, -9.57043]]}, {"shapeName": "R_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.676499, 109.237695, -9.08419], [-67.567458, 109.321192, -9.010835], [-67.619466, 109.268707, -8.873783], [-67.728508, 109.185209, -8.947138], [-67.676499, 109.237695, -9.08419], [-67.717431, 109.338388, -8.972718], [-67.619466, 109.268707, -8.873783], [-67.578528, 109.168006, -8.985256], [-67.567458, 109.321192, -9.010835], [-67.717431, 109.338388, -8.972718], [-67.728508, 109.185209, -8.947138], [-67.578528, 109.168006, -8.985256], [-67.676499, 109.237695, -9.08419], [-67.717431, 109.338388, -8.972718], [-61.0957, 101.216, -9.57043]]}, {"shapeName": "R_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-58.474938, 102.76403, 0.36064], [-58.324958, 102.746826, 0.322522], [-58.336029, 102.59364, 0.348101], [-58.486009, 102.610844, 0.386219], [-58.474938, 102.76403, 0.36064], [-58.37697, 102.69434, 0.459565], [-58.336029, 102.59364, 0.348101], [-58.434, 102.663329, 0.249167], [-58.324958, 102.746826, 0.322522], [-58.37697, 102.69434, 0.459565], [-58.486009, 102.610844, 0.386219], [-58.434, 102.663329, 0.249167], [-58.474938, 102.76403, 0.36064], [-58.37697, 102.69434, 0.459565], [-61.0957, 101.216, -9.57043]]}]},
			"C_neck_FK_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_A_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 154.088154, -18.038449], [0.0, 154.483434, -18.016563], [0.0, 154.857002, -18.14762], [0.0, 155.151992, -18.411647], [0.0, 155.323479, -18.768462], [0.0, 155.345365, -19.163742], [0.0, 155.214308, -19.537311], [0.0, 154.950282, -19.8323], [0.0, 154.593466, -20.003787], [0.0, 154.198186, -20.025673], [0.0, 153.824617, -19.894617], [0.0, 153.529628, -19.63059], [0.0, 153.358141, -19.273774], [0.0, 153.336255, -18.878494], [0.0, 153.467312, -18.504926], [0.0, 153.731338, -18.209936], [0.0, 154.088154, -18.038449], [0.0, 151.561595, -8.211756]]}]},
			"L_toe_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_toe_FK_CTLShape", "degree": 3, "form": 2, "points": [[13.953871, 5.641427, 7.565292], [9.978517, 7.287955, 7.590294], [6.003162, 5.642129, 7.536104], [4.35652, 1.668043, 7.434465], [6.003162, -2.306334, 7.344916], [9.978517, -3.952862, 7.319914], [13.953871, -2.307036, 7.374104], [15.600513, 1.66705, 7.475743]]}]},
			"C_head_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[10.733529, 174.909256, -4.878771], [0.0, 179.355064, -4.841638], [-10.733529, 174.909256, -4.878771], [-15.179492, 164.176102, -4.968417], [-10.733529, 153.442947, -5.058064], [0.0, 148.997139, -5.095197], [10.733529, 153.442947, -5.058064], [15.179492, 164.176102, -4.968417]]}]},
			"C_chest_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[5.152094, 127.606377, -12.927377], [0.0, 129.797977, -14.705762], [-5.152094, 127.606377, -12.927377], [-7.286156, 125.414776, -8.633965], [-5.152094, 127.606377, -4.340554], [0.0, 129.797977, -2.562169], [5.152094, 127.606377, -4.340554], [7.286156, 125.414776, -8.633965]]}]},
			"L_upLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_upLeg_FK_CTLShape", "degree": 3, "form": 2, "points": [[13.953898, 91.65692, -1.382878], [9.978517, 91.922398, 0.242234], [6.003136, 91.65692, -1.382878], [4.356482, 91.015999, -5.306253], [6.003136, 90.375078, -9.229628], [9.978517, 90.1096, -10.85474], [13.953898, 90.375078, -9.229628], [15.600551, 91.015999, -5.306253]]}]},
			"L_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[69.319507, 94.48312, -9.758062], [69.37552, 94.579266, -9.649152], [69.292333, 94.504798, -9.540628], [69.23632, 94.408652, -9.649538], [69.319507, 94.48312, -9.758062], [69.39013, 94.425214, -9.631967], [69.292333, 94.504798, -9.540628], [69.221702, 94.56271, -9.666725], [69.37552, 94.579266, -9.649152], [69.39013, 94.425214, -9.631967], [69.23632, 94.408652, -9.649538], [69.221702, 94.56271, -9.666725], [69.319507, 94.48312, -9.758062], [69.39013, 94.425214, -9.631967], [61.360889, 100.979874, -11.288918]]}, {"shapeName": "L_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.940479, 109.016773, -11.379434], [67.842674, 109.096363, -11.288096], [67.913305, 109.038451, -11.162], [68.01111, 108.958861, -11.253337], [67.940479, 109.016773, -11.379434], [67.996486, 109.112911, -11.270524], [67.913305, 109.038451, -11.162], [67.857292, 108.942305, -11.27091], [67.842674, 109.096363, -11.288096], [67.996486, 109.112911, -11.270524], [68.01111, 108.958861, -11.253337], [67.857292, 108.942305, -11.27091], [67.940479, 109.016773, -11.379434], [67.996486, 109.112911, -11.270524], [61.360889, 100.979874, -11.288918]]}, {"shapeName": "L_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[60.148735, 102.087745, -1.032493], [59.994917, 102.071189, -1.050066], [60.009535, 101.917131, -1.032879], [60.163353, 101.933687, -1.015307], [60.148735, 102.087745, -1.032493], [60.06555, 102.013276, -0.923979], [60.009535, 101.917131, -1.032879], [60.092722, 101.991599, -1.141403], [59.994917, 102.071189, -1.050066], [60.06555, 102.013276, -0.923979], [60.163353, 101.933687, -1.015307], [60.092722, 101.991599, -1.141403], [60.148735, 102.087745, -1.032493], [60.06555, 102.013276, -0.923979], [61.360889, 100.979874, -11.288918]]}]},
			"C_torso_FK_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_D_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 117.037224, -14.721745], [0.0, 117.270191, -14.768085], [0.0, 117.467691, -14.900056], [0.0, 117.599662, -15.097556], [0.0, 117.646002, -15.330523], [0.0, 117.599662, -15.56349], [0.0, 117.467691, -15.76099], [0.0, 117.270191, -15.892961], [0.0, 117.037224, -15.939301], [0.0, 116.804257, -15.892961], [0.0, 116.606757, -15.76099], [0.0, 116.474786, -15.56349], [0.0, 116.428446, -15.330523], [0.0, 116.474786, -15.097556], [0.0, 116.606757, -14.900056], [0.0, 116.804257, -14.768085], [0.0, 117.037224, -14.721745], [0.0, 117.037224, -8.633965]]}]},
			"L_wrist_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_wrist_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[65.588617, 95.83296, -7.765984], [65.616732, 95.912981, -7.635411], [65.504953, 95.83296, -7.562302], [65.476837, 95.75294, -7.692874], [65.588617, 95.83296, -7.765984], [65.620798, 95.757349, -7.633742], [65.504953, 95.83296, -7.562302], [65.472765, 95.908579, -7.694547], [65.616732, 95.912981, -7.635411], [65.620798, 95.757349, -7.633742], [65.476837, 95.75294, -7.692874], [65.472765, 95.908579, -7.694547], [65.588617, 95.83296, -7.765984], [65.620798, 95.757349, -7.633742], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_wrist_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.204449, 110.515778, -7.923782], [65.088598, 110.591397, -7.852345], [65.120786, 110.515778, -7.720101], [65.236637, 110.44016, -7.791537], [65.204449, 110.515778, -7.923782], [65.232559, 110.595792, -7.793213], [65.120786, 110.515778, -7.720101], [65.09267, 110.435758, -7.850673], [65.088598, 110.591397, -7.852345], [65.232559, 110.595792, -7.793213], [65.236637, 110.44016, -7.791537], [65.09267, 110.435758, -7.850673], [65.204449, 110.515778, -7.923782], [65.232559, 110.595792, -7.793213], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_wrist_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[54.687444, 103.046734, -0.896134], [54.543477, 103.042331, -0.95527], [54.547549, 102.886692, -0.953597], [54.691516, 102.891095, -0.894462], [54.687444, 103.046734, -0.896134], [54.575669, 102.966713, -0.823034], [54.547549, 102.886692, -0.953597], [54.659328, 102.966713, -1.026707], [54.543477, 103.042331, -0.95527], [54.575669, 102.966713, -0.823034], [54.691516, 102.891095, -0.894462], [54.659328, 102.966713, -1.026707], [54.687444, 103.046734, -0.896134], [54.575669, 102.966713, -0.823034], [58.56385, 102.966713, -10.53242]]}]},
			"L_heel_CTL": {"color": 20, "shapes": [{"shapeName": "L_heel_CTLShape", "degree": 1, "form": 0, "points": [[9.813801, 0.969538, -11.681757], [9.808469, -0.065675, -12.675363], [10.822972, 0.948742, -12.701604], [9.813801, 0.969538, -11.681757], [8.793742, 0.948742, -12.690714], [9.808469, -0.065675, -12.675363], [9.802913, 0.927945, -13.710561], [8.793742, 0.948742, -12.690714], [9.808245, 1.963159, -12.716955], [9.813801, 0.969538, -11.681757], [10.822972, 0.948742, -12.701604], [9.802913, 0.927945, -13.710561], [9.808245, 1.963159, -12.716955], [10.822972, 0.948742, -12.701604]]}]},
			"R_legEnd_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_legEnd_FK_CTLShape", "degree": 3, "form": 2, "points": [[-13.953898, 6.861021, -1.843173], [-9.978517, 6.608516, -0.215995], [-6.003136, 6.861021, -1.843173], [-4.356482, 7.470624, -5.771536], [-6.003136, 8.080227, -9.6999], [-9.978517, 8.332732, -11.327078], [-13.953898, 8.080227, -9.6999], [-15.600551, 7.470624, -5.771536]]}]},
			"world_D_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -346.62], [153.99, 0.0, -192.48], [115.44, 0.0, -192.48], [115.44, 0.0, -115.41], [192.51, 0.0, -115.41], [192.51, 0.0, -153.96], [346.62, 0.0, 0.0], [192.48, 0.0, 153.99], [192.48, 0.0, 115.44], [115.41, 0.0, 115.44], [115.41, 0.0, 192.51], [153.96, 0.0, 192.51], [0.0, 0.0, 346.62], [-153.99, 0.0, 192.48], [-115.44, 0.0, 192.48], [-115.44, 0.0, 115.41], [-192.51, 0.0, 115.41], [-192.51, 0.0, 153.96], [-346.62, 0.0, 0.0], [-192.48, 0.0, -153.99], [-192.48, 0.0, -115.44], [-115.41, 0.0, -115.44], [-115.41, 0.0, -192.51], [-153.96, 0.0, -192.51], [0.0, 0.0, -346.62], [30.18, 0.42, -316.98], [27.54, 0.0, -314.16], [27.54, 0.0, -302.64], [25.14, 0.0, -302.64], [25.29, 0.0, -314.25], [23.58, 0.0, -313.38], [23.64, 0.0, -308.34], [21.21, 0.0, -308.34], [21.21, 0.0, -313.38], [19.71, 0.0, -314.25], [19.71, 0.0, -302.46], [17.28, 0.0, -302.46], [17.28, 0.0, -314.55], [19.23, 0.0, -316.5], [22.23, 0.0, -315.0], [25.53, 0.0, -316.5], [27.54, 0.0, -314.22], [25.53, 0.0, -316.5], [22.26, 0.0, -315.03], [19.23, 0.0, -316.47], [13.38, 0.0, -316.5], [15.36, 0.0, -314.55], [15.36, 0.0, -304.44], [13.38, 0.0, -302.46], [7.05, 0.0, -302.46], [5.1, 0.0, -304.44], [5.1, 0.0, -314.55], [7.05, 0.0, -316.5], [13.38, 0.0, -316.5], [12.63, 0.0, -314.25], [12.93, 0.0, -304.95], [7.5, 0.0, -305.01], [7.53, 0.0, -314.25], [12.66, 0.0, -314.31], [13.38, 0.0, -316.5], [7.05, 0.0, -316.5], [3.0, 0.0, -316.5], [3.15, 0.0, -302.46], [-3.69, 0.0, -302.46], [-5.67, 0.0, -304.44], [-5.67, 0.0, -308.67], [-3.66, 0.0, -310.62], [-3.54, 0.0, -310.77], [-7.47, 0.0, -316.44], [-7.47, 0.0, -316.5], [-4.65, 0.0, -316.5], [-0.72, 0.0, -310.8], [0.75, 0.0, -310.8], [0.75, 0.0, -304.8], [-3.03, 0.0, -304.8], [-3.06, 0.0, -308.37], [0.75, 0.0, -308.37], [0.75, 0.0, -316.5], [3.0, 0.0, -316.5], [-19.29, 0.0, -316.5], [-19.29, 0.0, -314.25], [-11.43, 0.0, -314.22], [-11.43, 0.0, -302.46], [-9.0, 0.0, -302.46], [-9.0, 0.0, -316.5], [-29.52, 0.0, -316.5], [-31.32, 0.0, -314.55], [-31.47, 0.0, -304.44], [-29.52, 0.0, -302.46], [-21.21, 0.0, -302.46], [-21.21, 0.0, -316.5], [-23.67, 0.0, -314.25], [-23.61, 0.0, -304.74], [-28.74, 0.0, -304.74], [-28.68, 0.0, -314.19], [-23.58, 0.0, -314.31], [-21.15, 0.0, -316.5]]}]},
			"L_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_B_CTLShape", "degree": 3, "form": 2, "points": [[63.643354, 97.581914, -11.872647], [64.505276, 98.416822, -12.348441], [65.245275, 99.348999, -11.848632], [65.429867, 99.832388, -10.665998], [64.950923, 99.583828, -9.493313], [64.089, 98.74892, -9.017519], [63.349002, 97.816743, -9.517328], [63.16441, 97.333354, -10.699962]]}]},
			"L_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_A_CTLShape", "degree": 3, "form": 2, "points": [[61.258046, 101.78456, -16.798184], [61.100425, 102.966713, -17.29218], [60.942805, 104.148866, -16.798184], [60.877517, 104.638528, -15.60557], [60.942805, 104.148866, -14.412956], [61.100425, 102.966713, -13.91896], [61.258046, 101.78456, -14.412956], [61.323334, 101.294898, -15.60557]]}]},
			"L_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_A_CTLShape", "degree": 3, "form": 2, "points": [[60.624074, 100.299004, -9.688746], [61.590934, 101.133747, -9.875152], [62.042832, 102.163455, -9.241234], [61.71505, 102.784937, -8.158331], [60.799601, 102.634141, -7.260793], [59.832742, 101.799398, -7.074387], [59.380844, 100.769691, -7.708305], [59.708625, 100.148208, -8.791208]]}]},
			"L_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_D_CTLShape", "degree": 3, "form": 2, "points": [[72.357392, 102.291875, -16.798184], [72.515012, 103.474028, -17.29218], [72.672633, 104.656181, -16.798184], [72.737921, 105.145843, -15.60557], [72.672633, 104.656181, -14.412956], [72.515012, 103.474028, -13.91896], [72.357392, 102.291875, -14.412956], [72.292104, 101.802213, -15.60557]]}]},
			"R_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_C_CTLShape", "degree": 3, "form": 2, "points": [[-68.615045, 102.589601, -16.798184], [-68.71015, 103.778417, -17.29218], [-68.805255, 104.967233, -16.798184], [-68.844649, 105.459656, -15.60557], [-68.805255, 104.967233, -14.412956], [-68.71015, 103.778417, -13.91896], [-68.615045, 102.589601, -14.412956], [-68.575651, 102.097178, -15.60557]]}]},
			"L_arm_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[57.040912, 108.1303, -7.209173], [52.399663, 102.820658, -9.115591], [55.175335, 102.820658, -15.873073], [59.816584, 108.1303, -13.966656], [64.728038, 103.112768, -11.94925], [60.086789, 97.803126, -13.855668], [57.311117, 97.803126, -7.098185], [61.952366, 103.112768, -5.191767], [57.040912, 108.1303, -7.209173], [59.816584, 108.1303, -13.966656], [55.175335, 102.820658, -15.873073], [60.086789, 97.803126, -13.855668], [64.728038, 103.112768, -11.94925], [61.952366, 103.112768, -5.191767], [57.311117, 97.803126, -7.098185], [52.399663, 102.820658, -9.115591]]}]},
			"C_torso_FK_E_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_E_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 128.553684, -8.700024], [-0.066058, 128.553684, -8.633965], [0.0, 128.553684, -8.567907], [0.066058, 128.553684, -8.633965], [0.0, 128.553684, -8.700024], [0.0, 128.619736, -8.633965], [0.0, 128.553684, -8.567907], [0.0, 128.487625, -8.633965], [-0.066058, 128.553684, -8.633965], [0.0, 128.619736, -8.633965], [0.066058, 128.553684, -8.633965], [0.0, 128.487625, -8.633965], [0.0, 128.553684, -8.700024], [0.0, 128.619736, -8.633965], [0.0, 122.3218, -8.633965]]}, {"shapeName": "C_torso_FK_E_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 122.3218, -8.700024], [-6.231884, 122.255742, -8.633965], [-6.231884, 122.3218, -8.567907], [-6.231884, 122.387859, -8.633965], [-6.231884, 122.3218, -8.700024], [-6.297936, 122.3218, -8.633965], [-6.231884, 122.3218, -8.567907], [-6.165825, 122.3218, -8.633965], [-6.231884, 122.255742, -8.633965], [-6.297936, 122.3218, -8.633965], [-6.231884, 122.387859, -8.633965], [-6.165825, 122.3218, -8.633965], [-6.231884, 122.3218, -8.700024], [-6.297936, 122.3218, -8.633965], [0.0, 122.3218, -8.633965]]}, {"shapeName": "C_torso_FK_E_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 122.3218, -2.402082], [0.0, 122.255742, -2.402082], [0.066058, 122.3218, -2.402082], [0.0, 122.387859, -2.402082], [-0.066058, 122.3218, -2.402082], [0.0, 122.3218, -2.336029], [0.066058, 122.3218, -2.402082], [0.0, 122.3218, -2.46814], [0.0, 122.255742, -2.402082], [0.0, 122.3218, -2.336029], [0.0, 122.387859, -2.402082], [0.0, 122.3218, -2.46814], [-0.066058, 122.3218, -2.402082], [0.0, 122.3218, -2.336029], [0.0, 122.3218, -8.633965]]}]},
			"R_wrist_IK_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-57.85321, 100.944151, -13.832695], [-60.05912, 102.966713, -14.172713], [-61.389123, 104.989275, -12.3803], [-61.064117, 105.827046, -9.505423], [-59.274491, 104.989275, -7.232145], [-57.068581, 102.966713, -6.892128], [-55.738578, 100.944151, -8.68454], [-56.063584, 100.10638, -11.559418]]}]},
			"L_leg_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[15.531734, 8.296326, -5.643404], [15.305629, 8.296326, -5.643404], [15.262809, 8.067055, -5.678982], [15.102138, 8.001272, -5.689191], [14.907788, 8.133471, -5.668676], [14.747905, 7.975479, -5.693193], [14.881679, 7.783448, -5.722992], [14.815137, 7.624657, -5.747634], [14.583101, 7.582343, -5.7542], [14.583101, 7.358905, -5.788873], [14.815137, 7.316591, -5.795439], [14.881679, 7.157821, -5.820077], [14.747905, 6.965769, -5.84988], [14.907788, 6.807777, -5.874397], [15.102138, 6.939976, -5.853882], [15.262809, 6.874193, -5.86409], [15.305629, 6.644922, -5.899669], [15.531734, 6.644922, -5.899669], [15.574576, 6.874193, -5.86409], [15.735247, 6.939976, -5.853882], [15.929597, 6.807777, -5.874397], [16.089465, 6.965769, -5.84988], [15.955706, 7.157821, -5.820077], [16.022248, 7.316591, -5.795439], [16.254263, 7.358905, -5.788873], [16.254263, 7.582343, -5.7542], [16.022248, 7.624657, -5.747634], [15.955706, 7.783448, -5.722992], [16.089465, 7.975479, -5.693193], [15.929597, 8.133471, -5.668676], [15.735247, 8.001272, -5.689191], [15.574576, 8.067055, -5.678982], [15.531734, 8.296326, -5.643404]]}, {"shapeName": "L_leg_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[15.664109, 7.713152, -5.733901], [15.765773, 7.470624, -5.771536], [15.664109, 7.228096, -5.809172], [15.418685, 7.127655, -5.824758], [15.173276, 7.228096, -5.809172], [15.071612, 7.470624, -5.771536], [15.173276, 7.713152, -5.733901], [15.418685, 7.813593, -5.718315]]}, {"shapeName": "L_leg_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[14.583101, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}]},
			"C_chest_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_CTLShape", "degree": 3, "form": 2, "points": [[8.586823, 127.606377, -15.789651], [0.0, 131.259045, -18.753627], [-8.586823, 127.606377, -15.789651], [-12.143594, 123.953709, -8.633965], [-8.586823, 127.606377, -1.47828], [0.0, 131.259045, 1.485696], [8.586823, 127.606377, -1.47828], [12.143594, 123.953709, -8.633965]]}]},
			"C_neck_FK_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 161.648312, -5.73202], [-0.110097, 161.620896, -5.625391], [0.0, 161.59348, -5.518761], [0.110097, 161.620896, -5.625391], [0.0, 161.648312, -5.73202], [0.0, 161.727515, -5.597978], [0.0, 161.59348, -5.518761], [0.0, 161.514266, -5.652806], [-0.110097, 161.620896, -5.625391], [0.0, 161.727515, -5.597978], [0.110097, 161.620896, -5.625391], [0.0, 161.514266, -5.652806], [0.0, 161.648312, -5.73202], [0.0, 161.727515, -5.597978], [0.0, 151.561595, -8.211756]]}, {"shapeName": "C_neck_FK_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-10.386473, 151.589011, -8.318385], [-10.386473, 151.454966, -8.239172], [-10.386473, 151.534179, -8.105126], [-10.386473, 151.668225, -8.18434], [-10.386473, 151.589011, -8.318385], [-10.49656, 151.561595, -8.211756], [-10.386473, 151.534179, -8.105126], [-10.276375, 151.561595, -8.211756], [-10.386473, 151.454966, -8.239172], [-10.49656, 151.561595, -8.211756], [-10.386473, 151.668225, -8.18434], [-10.276375, 151.561595, -8.211756], [-10.386473, 151.589011, -8.318385], [-10.49656, 151.561595, -8.211756], [0.0, 151.561595, -8.211756]]}, {"shapeName": "C_neck_FK_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.110097, 148.97523, 1.847545], [0.0, 148.868601, 1.820129], [0.110097, 148.97523, 1.847545], [0.0, 149.08186, 1.874961], [-0.110097, 148.97523, 1.847545], [0.0, 148.947817, 1.954164], [0.110097, 148.97523, 1.847545], [0.0, 149.002646, 1.740915], [0.0, 148.868601, 1.820129], [0.0, 148.947817, 1.954164], [0.0, 149.08186, 1.874961], [0.0, 149.002646, 1.740915], [-0.110097, 148.97523, 1.847545], [0.0, 148.947817, 1.954164], [0.0, 151.561595, -8.211756]]}]},
			"C_chest_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_chest_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.231884, 127.606377, -8.700024], [6.231884, 127.672435, -8.633965], [6.231884, 127.606377, -8.567907], [6.231884, 127.540318, -8.633965], [6.231884, 127.606377, -8.700024], [6.297936, 127.606377, -8.633965], [6.231884, 127.606377, -8.567907], [6.165825, 127.606377, -8.633965], [6.231884, 127.672435, -8.633965], [6.297936, 127.606377, -8.633965], [6.231884, 127.540318, -8.633965], [6.165825, 127.606377, -8.633965], [6.231884, 127.606377, -8.700024], [6.297936, 127.606377, -8.633965], [0.0, 127.606377, -8.633965]]}, {"shapeName": "C_chest_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 133.83826, -8.700024], [-0.066058, 133.83826, -8.633965], [0.0, 133.83826, -8.567907], [0.066058, 133.83826, -8.633965], [0.0, 133.83826, -8.700024], [0.0, 133.904313, -8.633965], [0.0, 133.83826, -8.567907], [0.0, 133.772202, -8.633965], [-0.066058, 133.83826, -8.633965], [0.0, 133.904313, -8.633965], [0.066058, 133.83826, -8.633965], [0.0, 133.772202, -8.633965], [0.0, 133.83826, -8.700024], [0.0, 133.904313, -8.633965], [0.0, 127.606377, -8.633965]]}, {"shapeName": "C_chest_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 127.672435, -2.402082], [-0.066058, 127.606377, -2.402082], [0.0, 127.540318, -2.402082], [0.066058, 127.606377, -2.402082], [0.0, 127.672435, -2.402082], [0.0, 127.606377, -2.336029], [0.0, 127.540318, -2.402082], [0.0, 127.606377, -2.46814], [-0.066058, 127.606377, -2.402082], [0.0, 127.606377, -2.336029], [0.066058, 127.606377, -2.402082], [0.0, 127.606377, -2.46814], [0.0, 127.672435, -2.402082], [0.0, 127.606377, -2.336029], [0.0, 127.606377, -8.633965]]}]},
			"L_arm_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[46.946304, 119.132902, -118.251793], [47.02605, 119.20515, -118.13926], [46.94393, 119.128197, -118.031662], [46.864184, 119.055949, -118.144195], [46.946304, 119.132902, -118.251793], [47.019742, 119.049621, -118.142652], [46.94393, 119.128197, -118.031662], [46.870485, 119.211486, -118.140802], [47.02605, 119.20515, -118.13926], [47.019742, 119.049621, -118.142652], [46.864184, 119.055949, -118.144195], [46.870485, 119.211486, -118.140802], [46.946304, 119.132902, -118.251793], [47.019742, 119.049621, -118.142652], [39.904435, 126.765993, -118.054464]]}, {"shapeName": "L_arm_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[47.540743, 133.80607, -117.931779], [47.464924, 133.884654, -117.820788], [47.538369, 133.801366, -117.711647], [47.614187, 133.722782, -117.822638], [47.540743, 133.80607, -117.931779], [47.620481, 133.878312, -117.819246], [47.538369, 133.801366, -117.711647], [47.458623, 133.729117, -117.82418], [47.464924, 133.884654, -117.820788], [47.620481, 133.878312, -117.819246], [47.614187, 133.722782, -117.822638], [47.458623, 133.729117, -117.82418], [47.540743, 133.80607, -117.931779], [47.620481, 133.878312, -117.819246], [39.904435, 126.765993, -118.054464]]}, {"shapeName": "L_arm_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[39.873393, 126.618671, -107.668499], [39.717828, 126.625007, -107.670042], [39.711527, 126.46947, -107.673434], [39.867092, 126.463134, -107.671892], [39.873393, 126.618671, -107.668499], [39.791273, 126.541718, -107.560911], [39.711527, 126.46947, -107.673434], [39.793647, 126.546423, -107.781032], [39.717828, 126.625007, -107.670042], [39.791273, 126.541718, -107.560911], [39.867092, 126.463134, -107.671892], [39.793647, 126.546423, -107.781032], [39.873393, 126.618671, -107.668499], [39.791273, 126.541718, -107.560911], [39.904435, 126.765993, -118.054464]]}]},
			"R_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-82.810362, 102.101285, -15.715697], [-82.824913, 102.210417, -15.6056], [-82.810362, 102.101285, -15.495502], [-82.795811, 101.992153, -15.6056], [-82.810362, 102.101285, -15.715697], [-82.919483, 102.086736, -15.6056], [-82.810362, 102.101285, -15.495502], [-82.70123, 102.115836, -15.6056], [-82.824913, 102.210417, -15.6056], [-82.919483, 102.086736, -15.6056], [-82.795811, 101.992153, -15.6056], [-82.70123, 102.115836, -15.6056], [-82.810362, 102.101285, -15.715697], [-82.919483, 102.086736, -15.6056], [-72.515, 103.474, -15.6056]]}, {"shapeName": "R_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-73.887715, 113.769361, -15.715697], [-73.778584, 113.783912, -15.6056], [-73.887715, 113.769361, -15.495502], [-73.996847, 113.754811, -15.6056], [-73.887715, 113.769361, -15.715697], [-73.902265, 113.878483, -15.6056], [-73.887715, 113.769361, -15.495502], [-73.873164, 113.66023, -15.6056], [-73.778584, 113.783912, -15.6056], [-73.902265, 113.878483, -15.6056], [-73.996847, 113.754811, -15.6056], [-73.873164, 113.66023, -15.6056], [-73.887715, 113.769361, -15.715697], [-73.902265, 113.878483, -15.6056], [-72.515, 103.474, -15.6056]]}, {"shapeName": "R_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-72.529551, 103.583132, -5.219127], [-72.405869, 103.488551, -5.219127], [-72.500449, 103.364868, -5.219127], [-72.624132, 103.459449, -5.219127], [-72.529551, 103.583132, -5.219127], [-72.515, 103.474, -5.10904], [-72.500449, 103.364868, -5.219127], [-72.515, 103.474, -5.329225], [-72.405869, 103.488551, -5.219127], [-72.515, 103.474, -5.10904], [-72.624132, 103.459449, -5.219127], [-72.515, 103.474, -5.329225], [-72.529551, 103.583132, -5.219127], [-72.515, 103.474, -5.10904], [-72.515, 103.474, -15.6056]]}]},
			"C_neck_FK_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 165.8484, -4.652128], [-0.110097, 165.820984, -4.545499], [0.0, 165.793568, -4.438869], [0.110097, 165.820984, -4.545499], [0.0, 165.8484, -4.652128], [0.0, 165.927603, -4.518085], [0.0, 165.793568, -4.438869], [0.0, 165.714354, -4.572914], [-0.110097, 165.820984, -4.545499], [0.0, 165.927603, -4.518085], [0.110097, 165.820984, -4.545499], [0.0, 165.714354, -4.572914], [0.0, 165.8484, -4.652128], [0.0, 165.927603, -4.518085], [0.0, 155.761683, -7.131864]]}, {"shapeName": "C_neck_FK_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-10.386473, 155.789099, -7.238493], [-10.386473, 155.655054, -7.159279], [-10.386473, 155.734267, -7.025234], [-10.386473, 155.868313, -7.104448], [-10.386473, 155.789099, -7.238493], [-10.49656, 155.761683, -7.131864], [-10.386473, 155.734267, -7.025234], [-10.276375, 155.761683, -7.131864], [-10.386473, 155.655054, -7.159279], [-10.49656, 155.761683, -7.131864], [-10.386473, 155.868313, -7.104448], [-10.276375, 155.761683, -7.131864], [-10.386473, 155.789099, -7.238493], [-10.49656, 155.761683, -7.131864], [0.0, 155.761683, -7.131864]]}, {"shapeName": "C_neck_FK_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.110097, 153.175318, 2.927437], [0.0, 153.068689, 2.900021], [0.110097, 153.175318, 2.927437], [0.0, 153.281948, 2.954853], [-0.110097, 153.175318, 2.927437], [0.0, 153.147905, 3.034057], [0.110097, 153.175318, 2.927437], [0.0, 153.202734, 2.820808], [0.0, 153.068689, 2.900021], [0.0, 153.147905, 3.034057], [0.0, 153.281948, 2.954853], [0.0, 153.202734, 2.820808], [-0.110097, 153.175318, 2.927437], [0.0, 153.147905, 3.034057], [0.0, 155.761683, -7.131864]]}]},
			"R_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.125587, 95.300037, -3.115401], [-67.133689, 95.407822, -3.003331], [-67.010817, 95.343489, -2.932574], [-67.002715, 95.235703, -3.044644], [-67.125587, 95.300037, -3.115401], [-67.135575, 95.256629, -2.966214], [-67.010817, 95.343489, -2.932574], [-67.000824, 95.386903, -3.081766], [-67.133689, 95.407822, -3.003331], [-67.135575, 95.256629, -2.966214], [-67.002715, 95.235703, -3.044644], [-67.000824, 95.386903, -3.081766], [-67.125587, 95.300037, -3.115401], [-67.135575, 95.256629, -2.966214], [-60.7118, 101.467, -8.47477]]}, {"shapeName": "R_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-66.947163, 109.564018, -6.617491], [-66.822399, 109.650884, -6.583857], [-66.832393, 109.60747, -6.434665], [-66.957156, 109.520604, -6.468299], [-66.947163, 109.564018, -6.617491], [-66.955259, 109.671795, -6.505424], [-66.832393, 109.60747, -6.434665], [-66.824291, 109.499684, -6.546734], [-66.822399, 109.650884, -6.583857], [-66.955259, 109.671795, -6.505424], [-66.957156, 109.520604, -6.468299], [-66.824291, 109.499684, -6.546734], [-66.947163, 109.564018, -6.617491], [-66.955259, 109.671795, -6.505424], [-60.7118, 101.467, -8.47477]]}, {"shapeName": "R_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-55.363642, 103.602662, 0.169714], [-55.230776, 103.581742, 0.091279], [-55.232668, 103.430543, 0.128401], [-55.365533, 103.451462, 0.206836], [-55.363642, 103.602662, 0.169714], [-55.240775, 103.538326, 0.240462], [-55.232668, 103.430543, 0.128401], [-55.35554, 103.494876, 0.057644], [-55.230776, 103.581742, 0.091279], [-55.240775, 103.538326, 0.240462], [-55.365533, 103.451462, 0.206836], [-55.35554, 103.494876, 0.057644], [-55.363642, 103.602662, 0.169714], [-55.240775, 103.538326, 0.240462], [-60.7118, 101.467, -8.47477]]}]},
			"R_legBase_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 89.281001, -5.022824], [-9.978517, 86.473729, -4.56423], [-9.978517, 85.401445, -4.389062], [-9.978517, 87.551951, 2.036067], [-9.978517, 91.025602, 5.656683], [-9.978517, 94.495597, 5.089826], [-9.978517, 96.63649, 0.55202], [-9.978517, 96.630553, -6.223444], [-9.978517, 95.558268, -6.048276], [-9.978517, 92.750996, -5.589682], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253]]}]},
			"L_hand_CTL": {"color": 18, "shapes": [{"shapeName": "L_hand_CTLShape", "degree": 3, "form": 2, "points": [[62.29304, 113.113013, -11.725034], [61.100425, 113.113013, -12.21903], [59.907811, 113.113013, -11.725034], [59.413815, 113.113013, -10.53242], [59.907811, 113.113013, -9.339806], [61.100425, 113.113013, -8.84581], [62.29304, 113.113013, -9.339806], [62.787036, 113.113013, -10.53242]]}, {"shapeName": "L_hand_CTLShape1", "degree": 3, "form": 2, "points": [[61.100425, 114.305627, -11.725034], [61.100425, 113.113013, -12.21903], [61.100425, 111.920398, -11.725034], [61.100425, 111.426402, -10.53242], [61.100425, 111.920398, -9.339806], [61.100425, 113.113013, -8.84581], [61.100425, 114.305627, -9.339806], [61.100425, 114.799623, -10.53242]]}, {"shapeName": "L_hand_CTLShape2", "degree": 3, "form": 2, "points": [[59.907811, 114.305627, -10.53242], [59.413815, 113.113013, -10.53242], [59.907811, 111.920398, -10.53242], [61.100425, 111.426402, -10.53242], [62.29304, 111.920398, -10.53242], [62.787036, 113.113013, -10.53242], [62.29304, 114.305627, -10.53242], [61.100425, 114.799623, -10.53242]]}]},
			"C_torso_FK_E_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_E_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 122.3218, -14.721745], [0.0, 122.554767, -14.768085], [0.0, 122.752267, -14.900056], [0.0, 122.884238, -15.097556], [0.0, 122.930578, -15.330523], [0.0, 122.884238, -15.56349], [0.0, 122.752267, -15.76099], [0.0, 122.554767, -15.892961], [0.0, 122.3218, -15.939301], [0.0, 122.088833, -15.892961], [0.0, 121.891333, -15.76099], [0.0, 121.759362, -15.56349], [0.0, 121.713022, -15.330523], [0.0, 121.759362, -15.097556], [0.0, 121.891333, -14.900056], [0.0, 122.088833, -14.768085], [0.0, 122.3218, -14.721745], [0.0, 122.3218, -8.633965]]}]},
			"R_legBase_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 89.528858, -5.063314], [-9.978517, 87.122625, -4.670233], [-9.978517, 86.203524, -4.520089], [-9.978517, 88.046815, 0.987164], [-9.978517, 91.02423, 4.09055], [-9.978517, 93.998511, 3.604672], [-9.978517, 95.833563, -0.284876], [-9.978517, 95.828474, -6.092417], [-9.978517, 94.909373, -5.942273], [-9.978517, 92.50314, -5.549192], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253]]}]},
			"R_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-58.579963, 90.498066, 5.054681], [-58.443828, 90.545295, 5.113667], [-58.368963, 90.44449, 5.021599], [-58.505099, 90.39726, 4.962613], [-58.579963, 90.498066, 5.054681], [-58.481719, 90.394309, 5.116513], [-58.368963, 90.44449, 5.021599], [-58.467207, 90.548254, 4.95976], [-58.443828, 90.545295, 5.113667], [-58.481719, 90.394309, 5.116513], [-58.505099, 90.39726, 4.962613], [-58.467207, 90.548254, 4.95976], [-58.579963, 90.498066, 5.054681], [-58.481719, 90.394309, 5.116513], [-57.7899, 97.7331, -2.35619]]}, {"shapeName": "R_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-55.005275, 104.742601, 4.785497], [-54.892519, 104.792788, 4.690576], [-54.794275, 104.689025, 4.752416], [-54.907032, 104.638837, 4.847337], [-55.005275, 104.742601, 4.785497], [-54.869142, 104.789823, 4.844477], [-54.794275, 104.689025, 4.752416], [-54.930411, 104.641795, 4.693429], [-54.892519, 104.792788, 4.690576], [-54.869142, 104.789823, 4.844477], [-54.907032, 104.638837, 4.847337], [-54.930411, 104.641795, 4.693429], [-55.005275, 104.742601, 4.785497], [-54.869142, 104.789823, 4.844477], [-57.7899, 97.7331, -2.35619]]}, {"shapeName": "R_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-47.806508, 95.27997, -3.841103], [-47.829887, 95.282928, -3.995011], [-47.867779, 95.131935, -3.992158], [-47.8444, 95.128976, -3.83825], [-47.806508, 95.27997, -3.841103], [-47.731653, 95.179167, -3.93317], [-47.867779, 95.131935, -3.992158], [-47.942644, 95.23274, -3.90009], [-47.829887, 95.282928, -3.995011], [-47.731653, 95.179167, -3.93317], [-47.8444, 95.128976, -3.83825], [-47.942644, 95.23274, -3.90009], [-47.806508, 95.27997, -3.841103], [-47.731653, 95.179167, -3.93317], [-57.7899, 97.7331, -2.35619]]}]},
			"R_wrist_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-65.588617, 95.83296, -7.765984], [-65.616732, 95.912981, -7.635411], [-65.504953, 95.83296, -7.562302], [-65.476837, 95.75294, -7.692874], [-65.588617, 95.83296, -7.765984], [-65.620798, 95.757349, -7.633742], [-65.504953, 95.83296, -7.562302], [-65.472765, 95.908579, -7.694547], [-65.616732, 95.912981, -7.635411], [-65.620798, 95.757349, -7.633742], [-65.476837, 95.75294, -7.692874], [-65.472765, 95.908579, -7.694547], [-65.588617, 95.83296, -7.765984], [-65.620798, 95.757349, -7.633742], [-58.56385, 102.966713, -10.53242]]}, {"shapeName": "R_wrist_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.204449, 110.515778, -7.923782], [-65.088598, 110.591397, -7.852345], [-65.120786, 110.515778, -7.720101], [-65.236637, 110.44016, -7.791537], [-65.204449, 110.515778, -7.923782], [-65.232559, 110.595792, -7.793213], [-65.120786, 110.515778, -7.720101], [-65.09267, 110.435758, -7.850673], [-65.088598, 110.591397, -7.852345], [-65.232559, 110.595792, -7.793213], [-65.236637, 110.44016, -7.791537], [-65.09267, 110.435758, -7.850673], [-65.204449, 110.515778, -7.923782], [-65.232559, 110.595792, -7.793213], [-58.56385, 102.966713, -10.53242]]}, {"shapeName": "R_wrist_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-54.687444, 103.046734, -0.896134], [-54.543477, 103.042331, -0.95527], [-54.547549, 102.886692, -0.953597], [-54.691516, 102.891095, -0.894462], [-54.687444, 103.046734, -0.896134], [-54.575669, 102.966713, -0.823034], [-54.547549, 102.886692, -0.953597], [-54.659328, 102.966713, -1.026707], [-54.543477, 103.042331, -0.95527], [-54.575669, 102.966713, -0.823034], [-54.691516, 102.891095, -0.894462], [-54.659328, 102.966713, -1.026707], [-54.687444, 103.046734, -0.896134], [-54.575669, 102.966713, -0.823034], [-58.56385, 102.966713, -10.53242]]}]},
			"R_reverseBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_reverseBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-20.364252, 1.665293, 7.28929], [-20.364831, 1.777624, 7.397106], [-20.365433, 1.669806, 7.509436], [-20.364855, 1.557476, 7.401619], [-20.364252, 1.665293, 7.28929], [-20.474928, 1.66755, 7.398772], [-20.365433, 1.669806, 7.509436], [-20.254747, 1.66755, 7.399954], [-20.364831, 1.777624, 7.397106], [-20.474928, 1.66755, 7.398772], [-20.364855, 1.557476, 7.401619], [-20.254747, 1.66755, 7.399954], [-20.364252, 1.665293, 7.28929], [-20.474928, 1.66755, 7.398772], [-9.97852, 1.66755, 7.4551]]}, {"shapeName": "R_reverseBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-9.976786, 12.049584, 7.132144], [-9.867281, 12.051841, 7.242808], [-9.977968, 12.054097, 7.35229], [-10.087473, 12.051841, 7.241626], [-9.976786, 12.049584, 7.132144], [-9.977365, 12.161905, 7.23996], [-9.977968, 12.054097, 7.35229], [-9.977389, 11.941766, 7.244473], [-9.867281, 12.051841, 7.242808], [-9.977365, 12.161905, 7.23996], [-10.087473, 12.051841, 7.241626], [-9.977389, 11.941766, 7.244473], [-9.976786, 12.049584, 7.132144], [-9.977365, 12.161905, 7.23996], [-9.97852, 1.66755, 7.4551]]}, {"shapeName": "R_reverseBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-10.034233, 1.99051, 17.836984], [-9.924149, 1.880436, 17.839832], [-10.034257, 1.770362, 17.841498], [-10.144341, 1.880436, 17.83865], [-10.034233, 1.99051, 17.836984], [-10.034836, 1.882692, 17.949304], [-10.034257, 1.770362, 17.841498], [-10.033654, 1.878179, 17.729168], [-9.924149, 1.880436, 17.839832], [-10.034836, 1.882692, 17.949304], [-10.144341, 1.880436, 17.83865], [-10.033654, 1.878179, 17.729168], [-10.034233, 1.99051, 17.836984], [-10.034836, 1.882692, 17.949304], [-9.97852, 1.66755, 7.4551]]}]},
			"R_leg_IK_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_CTLShape", "degree": 3, "form": 2, "points": [[-15.941588, 7.470624, -15.709989], [-9.978517, 7.470624, -19.826622], [-4.015445, 7.470624, -15.709989], [-1.545465, 7.470624, -5.771536], [-4.015445, 7.470624, 4.166916], [-9.978517, 7.470624, 8.283549], [-15.941588, 7.470624, 4.166916], [-18.411568, 7.470624, -5.771536]]}]},
			"C_neckBase_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[10.01796, 153.640429, -16.297086], [0.0, 150.374297, -20.707287], [-10.01796, 153.640429, -16.297086], [-14.167526, 155.688806, -7.150601], [-10.01796, 149.482761, -0.126426], [0.0, 144.494471, 2.161466], [10.01796, 149.482761, -0.126426], [14.167526, 155.688806, -7.150601]]}]},
			"R_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_D_CTLShape", "degree": 3, "form": 2, "points": [[-66.824758, 92.99635, -4.060637], [-67.958067, 93.613648, -4.090874], [-68.576415, 94.42591, -3.300786], [-68.317579, 94.957324, -2.153196], [-67.333184, 94.896596, -1.320345], [-66.199875, 94.279298, -1.290109], [-65.581527, 93.467036, -2.080196], [-65.840364, 92.935622, -3.227786]]}]},
			"R_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_A_CTLShape", "degree": 3, "form": 2, "points": [[-60.754131, 99.938387, -12.468667], [-61.569027, 100.813825, -12.954379], [-62.261998, 101.786531, -12.464487], [-62.427111, 102.286708, -11.285962], [-61.967646, 102.021361, -10.109168], [-61.152751, 101.145923, -9.623457], [-60.459779, 100.173217, -10.113348], [-60.294667, 99.67304, -11.291873]]}]},
			"C_head_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 174.563132, -4.991763], [-0.110097, 174.562212, -4.881669], [0.0, 174.561293, -4.771575], [0.110097, 174.562212, -4.881669], [0.0, 174.563132, -4.991763], [0.0, 174.672296, -4.88075], [0.0, 174.561293, -4.771575], [0.0, 174.452118, -4.882589], [-0.110097, 174.562212, -4.881669], [0.0, 174.672296, -4.88075], [0.110097, 174.562212, -4.881669], [0.0, 174.452118, -4.882589], [0.0, 174.563132, -4.991763], [0.0, 174.672296, -4.88075], [0.0, 164.176102, -4.968417]]}, {"shapeName": "C_head_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-10.386473, 164.177021, -5.078511], [-10.386473, 164.066008, -4.969337], [-10.386473, 164.175182, -4.858324], [-10.386473, 164.286195, -4.967498], [-10.386473, 164.177021, -5.078511], [-10.49656, 164.176102, -4.968417], [-10.386473, 164.175182, -4.858324], [-10.276375, 164.176102, -4.968417], [-10.386473, 164.066008, -4.969337], [-10.49656, 164.176102, -4.968417], [-10.386473, 164.286195, -4.967498], [-10.276375, 164.176102, -4.968417], [-10.386473, 164.177021, -5.078511], [-10.49656, 164.176102, -4.968417], [0.0, 164.176102, -4.968417]]}, {"shapeName": "C_head_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.110097, 164.089354, 5.417693], [0.0, 163.97926, 5.416774], [0.110097, 164.089354, 5.417693], [0.0, 164.199447, 5.418613], [-0.110097, 164.089354, 5.417693], [0.0, 164.088434, 5.527777], [0.110097, 164.089354, 5.417693], [0.0, 164.090273, 5.3076], [0.0, 163.97926, 5.416774], [0.0, 164.088434, 5.527777], [0.0, 164.199447, 5.418613], [0.0, 164.090273, 5.3076], [-0.110097, 164.089354, 5.417693], [0.0, 164.088434, 5.527777], [0.0, 164.176102, -4.968417]]}]},
			"C_midNeck_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_CTLShape", "degree": 3, "form": 2, "points": [[14.311372, 160.835051, -18.141474], [0.0, 162.065164, -22.925825], [-14.311372, 160.835051, -18.141474], [-20.239323, 157.865288, -6.591002], [-14.311372, 154.895525, 4.95947], [0.0, 153.665412, 9.743821], [14.311372, 154.895525, 4.95947], [20.239323, 157.865288, -6.591002]]}]},
			"C_chest_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[7.728141, 127.606377, -15.074083], [0.0, 130.893778, -17.741661], [-7.728141, 127.606377, -15.074083], [-10.929234, 124.318976, -8.633965], [-7.728141, 127.606377, -2.193848], [0.0, 130.893778, 0.47373], [7.728141, 127.606377, -2.193848], [10.929234, 124.318976, -8.633965]]}]},
			"C_head_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[7.155686, 171.331538, -4.908653], [0.0, 174.29541, -4.883898], [-7.155686, 171.331538, -4.908653], [-10.119662, 164.176102, -4.968417], [-7.155686, 157.020665, -5.028182], [0.0, 154.056793, -5.052937], [7.155686, 157.020665, -5.028182], [10.119662, 164.176102, -4.968417]]}]},
			"R_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-75.258694, 104.302272, -15.715697], [-75.249915, 104.412018, -15.6056], [-75.258694, 104.302272, -15.495502], [-75.267474, 104.192525, -15.6056], [-75.258694, 104.302272, -15.715697], [-75.368431, 104.31105, -15.6056], [-75.258694, 104.302272, -15.495502], [-75.148947, 104.293492, -15.6056], [-75.249915, 104.412018, -15.6056], [-75.368431, 104.31105, -15.6056], [-75.267474, 104.192525, -15.6056], [-75.148947, 104.293492, -15.6056], [-75.258694, 104.302272, -15.715697], [-75.368431, 104.31105, -15.6056], [-64.9053, 103.474, -15.6056]]}, {"shapeName": "R_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-64.077028, 113.827395, -15.715697], [-63.967281, 113.818615, -15.6056], [-64.077028, 113.827395, -15.495502], [-64.186775, 113.836174, -15.6056], [-64.077028, 113.827395, -15.715697], [-64.068249, 113.937131, -15.6056], [-64.077028, 113.827395, -15.495502], [-64.085808, 113.717648, -15.6056], [-63.967281, 113.818615, -15.6056], [-64.068249, 113.937131, -15.6056], [-64.186775, 113.836174, -15.6056], [-64.085808, 113.717648, -15.6056], [-64.077028, 113.827395, -15.715697], [-64.068249, 113.937131, -15.6056], [-64.9053, 103.474, -15.6056]]}, {"shapeName": "R_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-64.89652, 103.583747, -5.219127], [-64.795553, 103.46522, -5.219127], [-64.914079, 103.364253, -5.219127], [-65.015047, 103.48278, -5.219127], [-64.89652, 103.583747, -5.219127], [-64.9053, 103.474, -5.10904], [-64.914079, 103.364253, -5.219127], [-64.9053, 103.474, -5.329225], [-64.795553, 103.46522, -5.219127], [-64.9053, 103.474, -5.10904], [-65.015047, 103.48278, -5.219127], [-64.9053, 103.474, -5.329225], [-64.89652, 103.583747, -5.219127], [-64.9053, 103.474, -5.10904], [-64.9053, 103.474, -15.6056]]}]},
			"L_reverseBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_reverseBall_CTLShape", "degree": 1, "form": 0, "points": [[9.978823, -1.122099, 7.512293], [9.978014, 6.232423, 7.361522], [9.972459, 7.226043, 6.326323], [10.992518, 7.246839, 7.335281], [9.977791, 8.261256, 7.31993], [9.972459, 7.226043, 6.326323], [8.963287, 7.246839, 7.34617], [9.978014, 6.232423, 7.361522], [9.983346, 7.267636, 8.355128], [8.963287, 7.246839, 7.34617], [9.977791, 8.261256, 7.31993], [9.983346, 7.267636, 8.355128], [10.992518, 7.246839, 7.335281], [9.978014, 6.232423, 7.361522]]}]},
			"R_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-57.684776, 96.479274, 1.078546], [-57.54786, 96.545831, 1.111211], [-57.473776, 96.425699, 1.045464], [-57.610693, 96.359142, 1.012798], [-57.684776, 96.479274, 1.078546], [-57.577225, 96.40062, 1.159087], [-57.473776, 96.425699, 1.045464], [-57.581328, 96.504358, 0.964914], [-57.54786, 96.545831, 1.111211], [-57.577225, 96.40062, 1.159087], [-57.610693, 96.359142, 1.012798], [-57.581328, 96.504358, 0.964914], [-57.684776, 96.479274, 1.078546], [-57.577225, 96.40062, 1.159087], [-57.7728, 101.346, -8.09741]]}, {"shapeName": "R_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-54.914519, 110.178801, -3.438784], [-54.81107, 110.203885, -3.552416], [-54.703518, 110.125225, -3.471866], [-54.806967, 110.100141, -3.358235], [-54.914519, 110.178801, -3.438784], [-54.777605, 110.245349, -3.406123], [-54.703518, 110.125225, -3.471866], [-54.840435, 110.058669, -3.504532], [-54.81107, 110.203885, -3.552416], [-54.777605, 110.245349, -3.406123], [-54.806967, 110.100141, -3.358235], [-54.840435, 110.058669, -3.504532], [-54.914519, 110.178801, -3.438784], [-54.777605, 110.245349, -3.406123], [-57.7728, 101.346, -8.09741]]}, {"shapeName": "R_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-47.788627, 98.912197, -9.608644], [-47.822094, 98.870724, -9.754941], [-47.851459, 98.725508, -9.707057], [-47.817992, 98.766981, -9.56076], [-47.788627, 98.912197, -9.608644], [-47.714553, 98.792067, -9.67439], [-47.851459, 98.725508, -9.707057], [-47.925543, 98.84564, -9.64131], [-47.822094, 98.870724, -9.754941], [-47.714553, 98.792067, -9.67439], [-47.817992, 98.766981, -9.56076], [-47.925543, 98.84564, -9.64131], [-47.788627, 98.912197, -9.608644], [-47.714553, 98.792067, -9.67439], [-57.7728, 101.346, -8.09741]]}]},
			"L_loLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_loLeg_FK_CTLShape", "degree": 3, "form": 2, "points": [[13.953898, 51.167074, 5.032231], [9.978517, 50.914568, 6.659409], [6.003136, 51.167074, 5.032231], [4.356482, 51.776676, 1.103868], [6.003136, 52.386279, -2.824495], [9.978517, 52.638784, -4.451673], [13.953898, 52.386279, -2.824495], [15.600551, 51.776676, 1.103868]]}]},
			"C_reverseJaw_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_reverseJaw_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.110097, 158.716896, 3.814574], [0.0, 158.79873, 3.888225], [-0.110097, 158.716896, 3.814574], [0.0, 158.635061, 3.740922], [0.110097, 158.716896, 3.814574], [0.0, 158.643251, 3.896401], [-0.110097, 158.716896, 3.814574], [0.0, 158.790547, 3.732739], [0.0, 158.79873, 3.888225], [0.0, 158.643251, 3.896401], [0.0, 158.635061, 3.740922], [0.0, 158.790547, 3.732739], [0.110097, 158.716896, 3.814574], [0.0, 158.643251, 3.896401], [-0.0, 165.665077, -3.905633]]}, {"shapeName": "C_reverseJaw_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.110097, 173.385283, 3.042548], [-0.0, 173.458935, 2.960713], [-0.110097, 173.385283, 3.042548], [-0.0, 173.311632, 3.124383], [0.110097, 173.385283, 3.042548], [-0.0, 173.467111, 3.116192], [-0.110097, 173.385283, 3.042548], [-0.0, 173.303449, 2.968896], [-0.0, 173.458935, 2.960713], [-0.0, 173.467111, 3.116192], [-0.0, 173.311632, 3.124383], [-0.0, 173.303449, 2.968896], [0.110097, 173.385283, 3.042548], [-0.0, 173.467111, 3.116192], [-0.0, 165.665077, -3.905633]]}, {"shapeName": "C_reverseJaw_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-10.386473, 165.746911, -3.831982], [-10.386473, 165.738728, -3.987468], [-10.386473, 165.583242, -3.979285], [-10.386473, 165.591425, -3.823798], [-10.386473, 165.746911, -3.831982], [-10.49656, 165.665077, -3.905633], [-10.386473, 165.583242, -3.979285], [-10.276375, 165.665077, -3.905633], [-10.386473, 165.738728, -3.987468], [-10.49656, 165.665077, -3.905633], [-10.386473, 165.591425, -3.823798], [-10.276375, 165.665077, -3.905633], [-10.386473, 165.746911, -3.831982], [-10.49656, 165.665077, -3.905633], [-0.0, 165.665077, -3.905633]]}]},
			"L_wrist_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[57.95473, 101.233088, -13.361227], [59.84551, 102.966713, -13.652671], [60.985512, 104.700338, -12.116317], [60.706936, 105.418427, -9.652136], [59.172971, 104.700338, -7.703613], [57.282191, 102.966713, -7.412169], [56.142188, 101.233088, -8.948523], [56.420765, 100.514999, -11.412704]]}]},
			"L_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[82.810374, 102.101313, -15.715667], [82.824925, 102.210445, -15.60557], [82.810374, 102.101313, -15.495472], [82.795823, 101.992181, -15.60557], [82.810374, 102.101313, -15.715667], [82.919495, 102.086764, -15.60557], [82.810374, 102.101313, -15.495472], [82.701242, 102.115864, -15.60557], [82.824925, 102.210445, -15.60557], [82.919495, 102.086764, -15.60557], [82.795823, 101.992181, -15.60557], [82.701242, 102.115864, -15.60557], [82.810374, 102.101313, -15.715667], [82.919495, 102.086764, -15.60557], [72.515012, 103.474028, -15.60557]]}, {"shapeName": "L_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[73.887727, 113.769389, -15.715667], [73.778596, 113.78394, -15.60557], [73.887727, 113.769389, -15.495472], [73.996859, 113.754839, -15.60557], [73.887727, 113.769389, -15.715667], [73.902277, 113.878511, -15.60557], [73.887727, 113.769389, -15.495472], [73.873176, 113.660258, -15.60557], [73.778596, 113.78394, -15.60557], [73.902277, 113.878511, -15.60557], [73.996859, 113.754839, -15.60557], [73.873176, 113.660258, -15.60557], [73.887727, 113.769389, -15.715667], [73.902277, 113.878511, -15.60557], [72.515012, 103.474028, -15.60557]]}, {"shapeName": "L_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[72.529563, 103.58316, -5.219097], [72.405881, 103.488579, -5.219097], [72.500461, 103.364896, -5.219097], [72.624144, 103.459477, -5.219097], [72.529563, 103.58316, -5.219097], [72.515012, 103.474028, -5.10901], [72.500461, 103.364896, -5.219097], [72.515012, 103.474028, -5.329195], [72.405881, 103.488579, -5.219097], [72.515012, 103.474028, -5.10901], [72.624144, 103.459477, -5.219097], [72.515012, 103.474028, -5.329195], [72.529563, 103.58316, -5.219097], [72.515012, 103.474028, -5.10901], [72.515012, 103.474028, -15.60557]]}]},
			"C_neckBase_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[11.449097, 153.937405, -17.452133], [0.0, 150.204683, -22.492363], [-11.449097, 153.937405, -17.452133], [-16.191458, 156.278408, -6.999008], [-11.449097, 149.185785, 1.028622], [0.0, 143.484882, 3.643355], [11.449097, 149.185785, 1.028622], [16.191458, 156.278408, -6.999008]]}]},
			"L_arm_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[63.237977, 106.923591, -8.612498], [63.073805, 106.735777, -8.679932], [62.864445, 106.882328, -8.765928], [62.696634, 106.801122, -8.834857], [62.658311, 106.534674, -8.850599], [62.419377, 106.527368, -8.948742], [62.367194, 106.791025, -8.970177], [62.19541, 106.861887, -9.040738], [61.994031, 106.702759, -9.123455], [61.820297, 106.880246, -9.194817], [61.955873, 107.106598, -9.139129], [61.880736, 107.287989, -9.169992], [61.634275, 107.329426, -9.271227], [61.627517, 107.587731, -9.274003], [61.871423, 107.644157, -9.173817], [61.936933, 107.829872, -9.146909], [61.789755, 108.047561, -9.207363], [61.953926, 108.235374, -9.139929], [62.163302, 108.088841, -9.053926], [62.331113, 108.170047, -8.984997], [62.369436, 108.436495, -8.969256], [62.60836, 108.44379, -8.871116], [62.660569, 108.180127, -8.849671], [62.832337, 108.109282, -8.779117], [63.0337, 108.268393, -8.696406], [63.207434, 108.090906, -8.625043], [63.071874, 107.864572, -8.680726], [63.147027, 107.683163, -8.649856], [63.393461, 107.641732, -8.548632], [63.40023, 107.383438, -8.545852], [63.156324, 107.327013, -8.646037], [63.090814, 107.141297, -8.672946], [63.237977, 106.923591, -8.612498]]}, {"shapeName": "L_arm_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[62.880644, 107.496789, -8.759274], [62.765883, 107.773886, -8.806413], [62.503488, 107.88209, -8.914193], [62.247193, 107.758014, -9.019468], [62.147102, 107.474381, -9.06058], [62.261864, 107.197283, -9.013441], [62.524258, 107.089079, -8.905662], [62.780544, 107.213143, -8.800391]]}, {"shapeName": "L_arm_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[61.907164, 106.791502, -9.159136], [58.56385, 102.966713, -10.53242]]}]},
			"R_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-75.392012, 84.71455, -8.025221], [-75.46766, 84.789702, -7.911764], [-75.364839, 84.736228, -7.807787], [-75.289191, 84.661076, -7.921244], [-75.392012, 84.71455, -8.025221], [-75.44146, 84.636697, -7.899783], [-75.364839, 84.736228, -7.807787], [-75.315386, 84.81409, -7.933226], [-75.46766, 84.789702, -7.911764], [-75.44146, 84.636697, -7.899783], [-75.289191, 84.661076, -7.921244], [-75.315386, 84.81409, -7.933226], [-75.392012, 84.71455, -8.025221], [-75.44146, 84.636697, -7.899783], [-69.4313, 93.0933, -9.49403]]}, {"shapeName": "R_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-77.863178, 99.149688, -9.155599], [-77.786551, 99.249228, -9.063604], [-77.836004, 99.171367, -8.938166], [-77.912631, 99.071827, -9.030161], [-77.863178, 99.149688, -9.155599], [-77.938818, 99.224835, -9.042143], [-77.836004, 99.171367, -8.938166], [-77.760357, 99.096214, -9.051622], [-77.786551, 99.249228, -9.063604], [-77.938818, 99.224835, -9.042143], [-77.912631, 99.071827, -9.030161], [-77.760357, 99.096214, -9.051622], [-77.863178, 99.149688, -9.155599], [-77.938818, 99.224835, -9.042143], [-69.4313, 93.0933, -9.49403]]}, {"shapeName": "R_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-68.238781, 94.180177, 0.766941], [-68.086506, 94.204564, 0.74548], [-68.060312, 94.05155, 0.757462], [-68.212587, 94.027163, 0.778923], [-68.238781, 94.180177, 0.766941], [-68.135961, 94.126702, 0.870908], [-68.060312, 94.05155, 0.757462], [-68.163133, 94.105024, 0.653485], [-68.086506, 94.204564, 0.74548], [-68.135961, 94.126702, 0.870908], [-68.212587, 94.027163, 0.778923], [-68.163133, 94.105024, 0.653485], [-68.238781, 94.180177, 0.766941], [-68.135961, 94.126702, 0.870908], [-69.4313, 93.0933, -9.49403]]}]},
			"L_arm_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[57.548558, 106.409104, -8.316922], [54.454392, 102.869343, -9.587867], [56.30484, 102.869343, -14.092856], [59.399006, 106.409104, -12.82191], [62.673309, 103.064083, -11.476973], [59.579143, 99.524321, -12.747918], [57.728695, 99.524321, -8.24293], [60.822861, 103.064083, -6.971985], [57.548558, 106.409104, -8.316922], [59.399006, 106.409104, -12.82191], [56.30484, 102.869343, -14.092856], [59.579143, 99.524321, -12.747918], [62.673309, 103.064083, -11.476973], [60.822861, 103.064083, -6.971985], [57.728695, 99.524321, -8.24293], [54.454392, 102.869343, -9.587867]]}]},
			"R_leg_IK_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-15.345281, 7.470624, -14.716144], [-9.978517, 7.470624, -18.421113], [-4.611752, 7.470624, -14.716144], [-2.38877, 7.470624, -5.771536], [-4.611752, 7.470624, 3.173071], [-9.978517, 7.470624, 6.878041], [-15.345281, 7.470624, 3.173071], [-17.568263, 7.470624, -5.771536]]}]},
			"C_midTorso_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_CTLShape", "degree": 3, "form": 2, "points": [[8.586823, 114.394936, -15.789651], [0.0, 114.394936, -18.753627], [-8.586823, 114.394936, -15.789651], [-12.143594, 114.394936, -8.633965], [-8.586823, 114.394936, -1.47828], [0.0, 114.394936, 1.485696], [8.586823, 114.394936, -1.47828], [12.143594, 114.394936, -8.633965]]}]},
			"visibility_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "visibility_CTLShape", "degree": 3, "form": 2, "points": [[2.274043, 209.103428, 0.0], [0.5, 210.525876, 0.0], [-1.274043, 209.103428, 0.0], [-1.269384, 209.103428, 0.0], [-1.274043, 209.103428, 0.0], [0.5, 207.680981, 0.0], [2.274043, 209.103428, 0.0], [2.274043, 209.103428, 0.0]]}, {"shapeName": "visibility_CTLShape1", "degree": 3, "form": 2, "points": [[1.242516, 209.845944, 0.0], [0.5, 210.153503, 0.0], [-0.242516, 209.845944, 0.0], [-0.550074, 209.103428, 0.0], [-0.242516, 208.360913, 0.0], [0.5, 208.053354, 0.0], [1.242516, 208.360913, 0.0], [1.550074, 209.103428, 0.0]]}]},
			"R_toe_IK_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-12.363729, 4.051875, 7.521217], [-9.978517, 5.039792, 7.536218], [-7.593304, 4.052296, 7.503704], [-6.605319, 1.667845, 7.44272], [-7.593304, -0.716781, 7.388991], [-9.978517, -1.704698, 7.37399], [-12.363729, -0.717203, 7.406504], [-13.351714, 1.667249, 7.467487]]}]},
			"L_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_D_CTLShape", "degree": 3, "form": 2, "points": [[68.611826, 92.279258, -10.723038], [69.639408, 92.927285, -11.159496], [70.545066, 93.672582, -10.620351], [70.798277, 94.078563, -9.421425], [70.250715, 93.907411, -8.265032], [69.223132, 93.259384, -7.828574], [68.317474, 92.514087, -8.367719], [68.064264, 92.108106, -9.566645]]}]},
			"C_torso_FK_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 117.984531, -8.700024], [-0.066058, 117.984531, -8.633965], [0.0, 117.984531, -8.567907], [0.066058, 117.984531, -8.633965], [0.0, 117.984531, -8.700024], [0.0, 118.050583, -8.633965], [0.0, 117.984531, -8.567907], [0.0, 117.918472, -8.633965], [-0.066058, 117.984531, -8.633965], [0.0, 118.050583, -8.633965], [0.066058, 117.984531, -8.633965], [0.0, 117.918472, -8.633965], [0.0, 117.984531, -8.700024], [0.0, 118.050583, -8.633965], [0.0, 111.752647, -8.633965]]}, {"shapeName": "C_torso_FK_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 111.752647, -8.700024], [-6.231884, 111.686589, -8.633965], [-6.231884, 111.752647, -8.567907], [-6.231884, 111.818706, -8.633965], [-6.231884, 111.752647, -8.700024], [-6.297936, 111.752647, -8.633965], [-6.231884, 111.752647, -8.567907], [-6.165825, 111.752647, -8.633965], [-6.231884, 111.686589, -8.633965], [-6.297936, 111.752647, -8.633965], [-6.231884, 111.818706, -8.633965], [-6.165825, 111.752647, -8.633965], [-6.231884, 111.752647, -8.700024], [-6.297936, 111.752647, -8.633965], [0.0, 111.752647, -8.633965]]}, {"shapeName": "C_torso_FK_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 111.752647, -2.402082], [0.0, 111.686589, -2.402082], [0.066058, 111.752647, -2.402082], [0.0, 111.818706, -2.402082], [-0.066058, 111.752647, -2.402082], [0.0, 111.752647, -2.336029], [0.066058, 111.752647, -2.402082], [0.0, 111.752647, -2.46814], [0.0, 111.686589, -2.402082], [0.0, 111.752647, -2.336029], [0.0, 111.818706, -2.402082], [0.0, 111.752647, -2.46814], [-0.066058, 111.752647, -2.402082], [0.0, 111.752647, -2.336029], [0.0, 111.752647, -8.633965]]}]},
			"L_shoulder_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [5.95314, 146.379607, -2.231417], [8.765469, 146.145601, -3.845107], [9.839685, 146.056219, -4.461483], [4.961586, 146.145601, -10.47449], [-0.201674, 146.379607, -12.957989], [-3.67792, 146.668855, -10.963349], [-4.139317, 146.90286, -5.252471], [-1.409651, 146.992243, 1.993289], [-0.335434, 146.90286, 1.376913], [2.476894, 146.668855, -0.236777], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097]]}]},
			"L_leg_PV_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_PV_CTLShape", "degree": 1, "form": 0, "points": [[8.963887, 52.226244, 103.57992], [8.963887, 50.196984, 103.57992], [8.963887, 50.196984, 101.550661], [8.963887, 52.226244, 101.550661], [10.993147, 52.226244, 101.550661], [10.993147, 50.196984, 101.550661], [10.993147, 50.196984, 103.57992], [10.993147, 52.226244, 103.57992], [8.963887, 52.226244, 103.57992], [8.963887, 52.226244, 101.550661], [8.963887, 50.196984, 101.550661], [10.993147, 50.196984, 101.550661], [10.993147, 52.226244, 101.550661], [10.993147, 52.226244, 103.57992], [10.993147, 50.196984, 103.57992], [8.963887, 50.196984, 103.57992]]}]},
			"R_shoulder_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-5.95314, 146.379607, -2.231417], [-8.765469, 146.145601, -3.845107], [-9.839685, 146.056219, -4.461483], [-4.961586, 146.145601, -10.47449], [0.201674, 146.379607, -12.957989], [3.67792, 146.668855, -10.963349], [4.139317, 146.90286, -5.252471], [1.409651, 146.992243, 1.993289], [0.335434, 146.90286, 1.376913], [-2.476894, 146.668855, -0.236777], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097]]}]},
			"R_legBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-9.978517, 80.783151, -3.523062], [-9.868419, 80.765401, -3.631719], [-9.978517, 80.747651, -3.740376], [-10.088614, 80.765401, -3.631719], [-9.978517, 80.783151, -3.523062], [-9.978517, 80.656754, -3.613971], [-9.978517, 80.747651, -3.740376], [-9.978517, 80.874058, -3.649469], [-9.868419, 80.765401, -3.631719], [-9.978517, 80.656754, -3.613971], [-10.088614, 80.765401, -3.631719], [-9.978517, 80.874058, -3.649469], [-9.978517, 80.783151, -3.523062], [-9.978517, 80.656754, -3.613971], [-9.978517, 91.015999, -5.306253]]}, {"shapeName": "R_legBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.407956, 91.033749, -5.197596], [0.407956, 91.124656, -5.324003], [0.407956, 90.998249, -5.41491], [0.407956, 90.907342, -5.288503], [0.407956, 91.033749, -5.197596], [0.518043, 91.015999, -5.306253], [0.407956, 90.998249, -5.41491], [0.297859, 91.015999, -5.306253], [0.407956, 91.124656, -5.324003], [0.518043, 91.015999, -5.306253], [0.407956, 90.907342, -5.288503], [0.297859, 91.015999, -5.306253], [0.407956, 91.033749, -5.197596], [0.518043, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253]]}, {"shapeName": "R_legBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.868419, 89.341465, -15.556851], [-9.978517, 89.450122, -15.574601], [-10.088614, 89.341465, -15.556851], [-9.978517, 89.232808, -15.5391], [-9.868419, 89.341465, -15.556851], [-9.978517, 89.323717, -15.665498], [-10.088614, 89.341465, -15.556851], [-9.978517, 89.359215, -15.448193], [-9.978517, 89.450122, -15.574601], [-9.978517, 89.323717, -15.665498], [-9.978517, 89.232808, -15.5391], [-9.978517, 89.359215, -15.448193], [-9.868419, 89.341465, -15.556851], [-9.978517, 89.323717, -15.665498], [-9.978517, 91.015999, -5.306253]]}]},
			"C_neckBase_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_CTLShape", "degree": 3, "form": 2, "points": [[14.311372, 154.531358, -19.762228], [0.0, 149.865455, -26.062515], [-14.311372, 154.531358, -19.762228], [-20.239323, 157.457611, -6.695821], [-14.311372, 148.591832, 3.338716], [0.0, 141.465703, 6.607132], [14.311372, 148.591832, 3.338716], [20.239323, 157.457611, -6.695821]]}]},
			"R_wrist_IK_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-57.75169, 100.655213, -14.304163], [-60.27273, 102.966713, -14.692755], [-61.792733, 105.278213, -12.644283], [-61.421298, 106.235665, -9.358709], [-59.376011, 105.278213, -6.760678], [-56.854971, 102.966713, -6.372086], [-55.334968, 100.655213, -8.420558], [-55.706403, 99.697761, -11.706132]]}]},
			"C_midNeck_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[12.880235, 160.538074, -16.986427], [0.0, 161.645176, -21.292343], [-12.880235, 160.538074, -16.986427], [-18.215391, 157.865288, -6.591002], [-12.880235, 155.192501, 3.804423], [0.0, 154.085399, 8.110339], [12.880235, 155.192501, 3.804423], [18.215391, 157.865288, -6.591002]]}]},
			"R_arm_IK_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-57.548558, 106.409104, -8.316922], [-54.454392, 102.869343, -9.587867], [-56.30484, 102.869343, -14.092856], [-59.399006, 106.409104, -12.82191], [-62.673309, 103.064083, -11.476973], [-59.579143, 99.524321, -12.747918], [-57.728695, 99.524321, -8.24293], [-60.822861, 103.064083, -6.971985], [-57.548558, 106.409104, -8.316922], [-59.399006, 106.409104, -12.82191], [-56.30484, 102.869343, -14.092856], [-59.579143, 99.524321, -12.747918], [-62.673309, 103.064083, -11.476973], [-60.822861, 103.064083, -6.971985], [-57.728695, 99.524321, -8.24293], [-54.454392, 102.869343, -9.587867]]}]},
			"L_arm_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[65.588617, 95.83296, -7.765984], [65.616732, 95.912981, -7.635411], [65.504953, 95.83296, -7.562302], [65.476837, 95.75294, -7.692874], [65.588617, 95.83296, -7.765984], [65.620798, 95.757349, -7.633742], [65.504953, 95.83296, -7.562302], [65.472765, 95.908579, -7.694547], [65.616732, 95.912981, -7.635411], [65.620798, 95.757349, -7.633742], [65.476837, 95.75294, -7.692874], [65.472765, 95.908579, -7.694547], [65.588617, 95.83296, -7.765984], [65.620798, 95.757349, -7.633742], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_arm_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.204449, 110.515778, -7.923782], [65.088598, 110.591397, -7.852345], [65.120786, 110.515778, -7.720101], [65.236637, 110.44016, -7.791537], [65.204449, 110.515778, -7.923782], [65.232559, 110.595792, -7.793213], [65.120786, 110.515778, -7.720101], [65.09267, 110.435758, -7.850673], [65.088598, 110.591397, -7.852345], [65.232559, 110.595792, -7.793213], [65.236637, 110.44016, -7.791537], [65.09267, 110.435758, -7.850673], [65.204449, 110.515778, -7.923782], [65.232559, 110.595792, -7.793213], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_arm_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[54.687444, 103.046734, -0.896134], [54.543477, 103.042331, -0.95527], [54.547549, 102.886692, -0.953597], [54.691516, 102.891095, -0.894462], [54.687444, 103.046734, -0.896134], [54.575669, 102.966713, -0.823034], [54.547549, 102.886692, -0.953597], [54.659328, 102.966713, -1.026707], [54.543477, 103.042331, -0.95527], [54.575669, 102.966713, -0.823034], [54.691516, 102.891095, -0.894462], [54.659328, 102.966713, -1.026707], [54.687444, 103.046734, -0.896134], [54.575669, 102.966713, -0.823034], [58.56385, 102.966713, -10.53242]]}]},
			"L_toe_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[12.363729, 4.051875, 7.521217], [9.978517, 5.039792, 7.536218], [7.593304, 4.052296, 7.503704], [6.605319, 1.667845, 7.44272], [7.593304, -0.716781, 7.388991], [9.978517, -1.704698, 7.37399], [12.363729, -0.717203, 7.406504], [13.351714, 1.667249, 7.467487]]}]},
			"C_torso_FK_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_A_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 101.197773, -14.721745], [-0.0, 101.43074, -14.768085], [-0.0, 101.62824, -14.900056], [-0.0, 101.760211, -15.097556], [-0.0, 101.806551, -15.330523], [-0.0, 101.760211, -15.56349], [-0.0, 101.62824, -15.76099], [-0.0, 101.43074, -15.892961], [-0.0, 101.197773, -15.939301], [-0.0, 100.964806, -15.892961], [-0.0, 100.767306, -15.76099], [-0.0, 100.635335, -15.56349], [-0.0, 100.588995, -15.330523], [-0.0, 100.635335, -15.097556], [-0.0, 100.767306, -14.900056], [-0.0, 100.964806, -14.768085], [-0.0, 101.197773, -14.721745], [-0.0, 101.197773, -8.633965]]}]},
			"L_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[57.684752, 96.478866, 1.078544], [57.547836, 96.545423, 1.111209], [57.473752, 96.425291, 1.045462], [57.610669, 96.358734, 1.012796], [57.684752, 96.478866, 1.078544], [57.577201, 96.400212, 1.159085], [57.473752, 96.425291, 1.045462], [57.581304, 96.50395, 0.964912], [57.547836, 96.545423, 1.111209], [57.577201, 96.400212, 1.159085], [57.610669, 96.358734, 1.012796], [57.581304, 96.50395, 0.964912], [57.684752, 96.478866, 1.078544], [57.577201, 96.400212, 1.159085], [57.772776, 101.345592, -8.097412]]}, {"shapeName": "L_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[54.914495, 110.178393, -3.438786], [54.811046, 110.203477, -3.552418], [54.703494, 110.124817, -3.471868], [54.806943, 110.099733, -3.358237], [54.914495, 110.178393, -3.438786], [54.777581, 110.244941, -3.406125], [54.703494, 110.124817, -3.471868], [54.840411, 110.058261, -3.504534], [54.811046, 110.203477, -3.552418], [54.777581, 110.244941, -3.406125], [54.806943, 110.099733, -3.358237], [54.840411, 110.058261, -3.504534], [54.914495, 110.178393, -3.438786], [54.777581, 110.244941, -3.406125], [57.772776, 101.345592, -8.097412]]}, {"shapeName": "L_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[47.788603, 98.911789, -9.608646], [47.82207, 98.870316, -9.754943], [47.851435, 98.7251, -9.707059], [47.817968, 98.766573, -9.560762], [47.788603, 98.911789, -9.608646], [47.714529, 98.791659, -9.674392], [47.851435, 98.7251, -9.707059], [47.925519, 98.845232, -9.641312], [47.82207, 98.870316, -9.754943], [47.714529, 98.791659, -9.674392], [47.817968, 98.766573, -9.560762], [47.925519, 98.845232, -9.641312], [47.788603, 98.911789, -9.608646], [47.714529, 98.791659, -9.674392], [57.772776, 101.345592, -8.097412]]}]},
			"L_leg_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[14.738418, 8.178368, -5.661709], [14.544613, 8.178368, -5.661709], [14.50791, 7.981851, -5.692204], [14.370192, 7.925465, -5.700954], [14.203606, 8.038778, -5.68337], [14.066564, 7.903357, -5.704385], [14.181228, 7.738759, -5.729927], [14.124191, 7.602652, -5.751048], [13.925303, 7.566383, -5.756676], [13.925303, 7.374865, -5.786396], [14.124191, 7.338596, -5.792024], [14.181228, 7.202507, -5.813143], [14.066564, 7.037891, -5.838688], [14.203606, 6.90247, -5.859702], [14.370192, 7.015783, -5.842118], [14.50791, 6.959397, -5.850868], [14.544613, 6.76288, -5.881364], [14.738418, 6.76288, -5.881364], [14.775139, 6.959397, -5.850868], [14.912857, 7.015783, -5.842118], [15.079443, 6.90247, -5.859702], [15.216473, 7.037891, -5.838688], [15.101822, 7.202507, -5.813143], [15.158858, 7.338596, -5.792024], [15.357727, 7.374865, -5.786396], [15.357727, 7.566383, -5.756676], [15.158858, 7.602652, -5.751048], [15.101822, 7.738759, -5.729927], [15.216473, 7.903357, -5.704385], [15.079443, 8.038778, -5.68337], [14.912857, 7.925465, -5.700954], [14.775139, 7.981851, -5.692204], [14.738418, 8.178368, -5.661709]]}, {"shapeName": "L_leg_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[14.851882, 7.678505, -5.739277], [14.939022, 7.470624, -5.771536], [14.851882, 7.262743, -5.803795], [14.641518, 7.176651, -5.817155], [14.431167, 7.262743, -5.803795], [14.344027, 7.470624, -5.771536], [14.431167, 7.678505, -5.739277], [14.641518, 7.764597, -5.725918]]}, {"shapeName": "L_leg_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[13.925303, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}]},
			"L_arm_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_CTLShape", "degree": 1, "form": 0, "points": [[56.871697, 108.704032, -6.839923], [51.714753, 102.804429, -8.958165], [54.798833, 102.804429, -16.466479], [59.955777, 108.704032, -14.348237], [65.412948, 103.128997, -12.106675], [60.256004, 97.229394, -14.224917], [57.171924, 97.229394, -6.716603], [62.328868, 103.128997, -4.598361], [56.871697, 108.704032, -6.839923], [59.955777, 108.704032, -14.348237], [54.798833, 102.804429, -16.466479], [60.256004, 97.229394, -14.224917], [65.412948, 103.128997, -12.106675], [62.328868, 103.128997, -4.598361], [57.171924, 97.229394, -6.716603], [51.714753, 102.804429, -8.958165]]}]},
			"L_legBase_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 89.033144, -4.982335], [9.978517, 85.824834, -4.458226], [9.978517, 84.599366, -4.258034], [9.978517, 87.057087, 3.084969], [9.978517, 91.026973, 7.222817], [9.978517, 94.992682, 6.57498], [9.978517, 97.439417, 1.388916], [9.978517, 97.432632, -6.354472], [9.978517, 96.207164, -6.15428], [9.978517, 92.998853, -5.630171], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}]},
			"L_outterBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_outterBall_CTLShape", "degree": 1, "form": 0, "points": [[17.316787, 1.453949, 5.358633], [17.311455, 0.418736, 4.365027], [18.325959, 1.433153, 4.338786], [17.316787, 1.453949, 5.358633], [16.296728, 1.433153, 4.349675], [17.311455, 0.418736, 4.365027], [17.3059, 1.412357, 3.329828], [16.296728, 1.433153, 4.349675], [17.311232, 2.44757, 4.323434], [17.316787, 1.453949, 5.358633], [18.325959, 1.433153, 4.338786], [17.3059, 1.412357, 3.329828], [17.311232, 2.44757, 4.323434], [18.325959, 1.433153, 4.338786]]}]},
			"R_ankleOffset_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ankleOffset_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-20.364992, 7.465096, -5.881499], [-20.364992, 7.580579, -5.777064], [-20.364992, 7.476144, -5.661582], [-20.364992, 7.360661, -5.766016], [-20.364992, 7.465096, -5.881499], [-20.47508, 7.47062, -5.77154], [-20.364992, 7.476144, -5.661582], [-20.254895, 7.47062, -5.77154], [-20.364992, 7.580579, -5.777064], [-20.47508, 7.47062, -5.77154], [-20.364992, 7.360661, -5.766016], [-20.254895, 7.47062, -5.77154], [-20.364992, 7.465096, -5.881499], [-20.47508, 7.47062, -5.77154], [-9.97852, 7.47062, -5.77154]]}, {"shapeName": "R_ankleOffset_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-9.97852, 17.838486, -6.402635], [-9.868422, 17.844011, -6.292676], [-9.97852, 17.849535, -6.182717], [-10.088617, 17.844011, -6.292676], [-9.97852, 17.838486, -6.402635], [-9.97852, 17.953959, -6.298199], [-9.97852, 17.849535, -6.182717], [-9.97852, 17.734052, -6.287152], [-9.868422, 17.844011, -6.292676], [-9.97852, 17.953959, -6.298199], [-10.088617, 17.844011, -6.292676], [-9.97852, 17.734052, -6.287152], [-9.97852, 17.838486, -6.402635], [-9.97852, 17.953959, -6.298199], [-9.97852, 7.47062, -5.77154]]}, {"shapeName": "R_ankleOffset_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.97852, 8.101714, 4.596326], [-9.868422, 7.991756, 4.60185], [-9.97852, 7.881797, 4.607374], [-10.088617, 7.991756, 4.60185], [-9.97852, 8.101714, 4.596326], [-9.97852, 7.997279, 4.711799], [-9.97852, 7.881797, 4.607374], [-9.97852, 7.986231, 4.491891], [-9.868422, 7.991756, 4.60185], [-9.97852, 7.997279, 4.711799], [-10.088617, 7.991756, 4.60185], [-9.97852, 7.986231, 4.491891], [-9.97852, 8.101714, 4.596326], [-9.97852, 7.997279, 4.711799], [-9.97852, 7.47062, -5.77154]]}]},
			"C_midTorso_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[5.152094, 114.394936, -12.927377], [0.0, 114.394936, -14.705762], [-5.152094, 114.394936, -12.927377], [-7.286156, 114.394936, -8.633965], [-5.152094, 114.394936, -4.340554], [0.0, 114.394936, -2.562169], [5.152094, 114.394936, -4.340554], [7.286156, 114.394936, -8.633965]]}]},
			"L_toe_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[12.761265, 4.449263, 7.532235], [9.978517, 5.601833, 7.549737], [7.195769, 4.449755, 7.511804], [6.043119, 1.667894, 7.440656], [7.195769, -1.114169, 7.377972], [9.978517, -2.266739, 7.360471], [12.761265, -1.114661, 7.398404], [13.913914, 1.667199, 7.469551]]}]},
			"C_cog_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[32.850802, 98.139605, -6.269864], [32.816152, 98.139605, -11.437954], [23.898452, 98.139605, -14.541064], [22.67978, 98.139605, -18.208357], [27.966414, 98.139605, -26.030596], [24.900682, 98.139605, -30.191295], [15.86079, 98.139605, -27.46558], [12.720171, 98.139605, -29.716299], [12.399847, 98.139605, -39.146373], [7.473972, 98.139605, -40.710486], [1.764841, 98.139605, -33.197032], [-2.098118, 98.139605, -33.171489], [-7.903077, 98.139605, -40.607458], [-12.807517, 98.139605, -38.977499], [-13.005222, 98.139605, -29.546241], [-16.115004, 98.139605, -27.2542], [-25.187278, 98.139605, -29.85575], [-28.196992, 98.139605, -25.65432], [-22.807726, 98.139605, -17.907658], [-23.976495, 98.139605, -14.224618], [-32.850802, 98.139605, -10.998067], [-32.816152, 98.139605, -5.829977], [-23.898452, 98.139605, -2.726867], [-22.67978, 98.139605, 0.940426], [-27.966414, 98.139605, 8.762665], [-24.900682, 98.139605, 12.923364], [-15.86079, 98.139605, 10.197649], [-12.720171, 98.139605, 12.448368], [-12.399847, 98.139605, 21.878442], [-7.473972, 98.139605, 23.442555], [-1.764841, 98.139605, 15.929101], [2.098118, 98.139605, 15.903558], [7.903077, 98.139605, 23.339527], [12.807517, 98.139605, 21.709568], [13.005222, 98.139605, 12.27831], [16.115004, 98.139605, 9.986269], [25.187278, 98.139605, 12.587819], [28.196992, 98.139605, 8.386389], [22.807726, 98.139605, 0.639727], [23.976495, 98.139605, -3.043313], [32.850802, 98.139605, -6.269864]]}]},
			"L_arm_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[62.069445, 105.934371, -9.092479], [61.946317, 105.793511, -9.143054], [61.789296, 105.903424, -9.207551], [61.663438, 105.84252, -9.259248], [61.634696, 105.642684, -9.271054], [61.455495, 105.637204, -9.344662], [61.416358, 105.834947, -9.360737], [61.28752, 105.888093, -9.413658], [61.136486, 105.768747, -9.475696], [61.006185, 105.901862, -9.529218], [61.107867, 106.071626, -9.487452], [61.051515, 106.20767, -9.510599], [60.866669, 106.238747, -9.586525], [60.8616, 106.432477, -9.588607], [61.04453, 106.474796, -9.513468], [61.093662, 106.614082, -9.493286], [60.983279, 106.777349, -9.538627], [61.106407, 106.918209, -9.488051], [61.263439, 106.808309, -9.42355], [61.389297, 106.869214, -9.371853], [61.41804, 107.06905, -9.360047], [61.597233, 107.074521, -9.286442], [61.63639, 106.876774, -9.270358], [61.765215, 106.82364, -9.217443], [61.916238, 106.942973, -9.155409], [62.046538, 106.809858, -9.101888], [61.944868, 106.640107, -9.143649], [62.001233, 106.504051, -9.120497], [62.186059, 106.472977, -9.044579], [62.191135, 106.279257, -9.042494], [62.008206, 106.236938, -9.117633], [61.959073, 106.097651, -9.137814], [62.069445, 105.934371, -9.092479]]}, {"shapeName": "L_arm_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[61.801446, 106.36427, -9.202561], [61.715375, 106.572093, -9.237915], [61.518579, 106.653246, -9.31875], [61.326357, 106.560189, -9.397706], [61.251289, 106.347464, -9.42854], [61.337361, 106.13964, -9.393186], [61.534156, 106.058487, -9.312351], [61.72637, 106.151536, -9.233398]]}, {"shapeName": "L_arm_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[61.071336, 105.835305, -9.502457], [58.56385, 102.966713, -10.53242]]}]},
			"C_hip_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[7.728141, 98.139605, -15.074083], [-0.0, 94.852204, -17.741661], [-7.728141, 98.139605, -15.074083], [-10.929234, 101.427006, -8.633965], [-7.728141, 98.139605, -2.193848], [-0.0, 94.852204, 0.47373], [7.728141, 98.139605, -2.193848], [10.929234, 101.427006, -8.633965]]}]},
			"R_arm_IK_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-57.210128, 107.556568, -7.578422], [-53.084573, 102.836886, -9.273016], [-55.551837, 102.836886, -15.279667], [-59.677392, 107.556568, -13.585074], [-64.043128, 103.09654, -11.791824], [-59.917573, 98.376858, -13.486418], [-57.450309, 98.376858, -7.479766], [-61.575864, 103.09654, -5.785173], [-57.210128, 107.556568, -7.578422], [-59.677392, 107.556568, -13.585074], [-55.551837, 102.836886, -15.279667], [-59.917573, 98.376858, -13.486418], [-64.043128, 103.09654, -11.791824], [-61.575864, 103.09654, -5.785173], [-57.450309, 98.376858, -7.479766], [-53.084573, 102.836886, -9.273016]]}]},
			"L_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[72.637482, 88.356136, -4.661675], [72.693834, 88.440592, -4.543629], [72.580449, 88.387149, -4.451267], [72.524098, 88.302694, -4.569313], [72.637482, 88.356136, -4.661675], [72.673036, 88.287229, -4.526662], [72.580449, 88.387149, -4.451267], [72.54489, 88.456064, -4.586283], [72.693834, 88.440592, -4.543629], [72.673036, 88.287229, -4.526662], [72.524098, 88.302694, -4.569313], [72.54489, 88.456064, -4.586283], [72.637482, 88.356136, -4.661675], [72.673036, 88.287229, -4.526662], [66.564142, 96.335904, -7.368849]]}, {"shapeName": "L_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[74.59901, 102.824971, -6.262572], [74.506418, 102.924899, -6.18718], [74.541977, 102.855983, -6.052165], [74.634569, 102.756055, -6.127557], [74.59901, 102.824971, -6.262572], [74.655354, 102.90942, -6.144528], [74.541977, 102.855983, -6.052165], [74.485626, 102.771528, -6.17021], [74.506418, 102.924899, -6.18718], [74.655354, 102.90942, -6.144528], [74.634569, 102.756055, -6.127557], [74.485626, 102.771528, -6.17021], [74.59901, 102.824971, -6.262572], [74.655354, 102.90942, -6.144528], [66.564142, 96.335904, -7.368849]]}, {"shapeName": "L_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[63.958794, 97.867688, 2.568794], [63.80985, 97.883161, 2.52614], [63.789058, 97.72979, 2.54311], [63.938002, 97.714317, 2.585763], [63.958794, 97.867688, 2.568794], [63.845412, 97.814244, 2.661146], [63.789058, 97.72979, 2.54311], [63.902443, 97.783233, 2.450748], [63.80985, 97.883161, 2.52614], [63.845412, 97.814244, 2.661146], [63.938002, 97.714317, 2.585763], [63.902443, 97.783233, 2.450748], [63.958794, 97.867688, 2.568794], [63.845412, 97.814244, 2.661146], [66.564142, 96.335904, -7.368849]]}]},
			"L_leg_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[13.55636, 7.470624, -11.734608], [9.978517, 7.470624, -14.204588], [6.400674, 7.470624, -11.734608], [4.918686, 7.470624, -5.771536], [6.400674, 7.470624, 0.191535], [9.978517, 7.470624, 2.661515], [13.55636, 7.470624, 0.191535], [15.038347, 7.470624, -5.771536]]}]},
			"C_chest_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.010776, 127.606377, -13.642946], [0.0, 130.163244, -15.717729], [-6.010776, 127.606377, -13.642946], [-8.500516, 125.049509, -8.633965], [-6.010776, 127.606377, -3.624985], [0.0, 130.163244, -1.550202], [6.010776, 127.606377, -3.624985], [8.500516, 125.049509, -8.633965]]}]},
			"L_shoulder_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_CTLShape", "degree": 3, "form": 0, "points": [[4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [5.46491, 146.524231, 0.944207], [7.487268, 146.524231, 4.468761], [8.259742, 146.524231, 5.815024], [15.752501, 145.836506, -0.273757], [18.838341, 145.411468, -6.729352], [16.338557, 145.411468, -11.085962], [9.207998, 145.836506, -11.679475], [0.170292, 146.524231, -8.283219], [0.942766, 146.524231, -6.936956], [2.965125, 146.524231, -3.412402], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097]]}]},
			"C_chest_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_chest_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 133.83826, -8.700024], [-0.066058, 133.83826, -8.633965], [0.0, 133.83826, -8.567907], [0.066058, 133.83826, -8.633965], [0.0, 133.83826, -8.700024], [0.0, 133.904313, -8.633965], [0.0, 133.83826, -8.567907], [0.0, 133.772202, -8.633965], [-0.066058, 133.83826, -8.633965], [0.0, 133.904313, -8.633965], [0.066058, 133.83826, -8.633965], [0.0, 133.772202, -8.633965], [0.0, 133.83826, -8.700024], [0.0, 133.904313, -8.633965], [0.0, 127.606377, -8.633965]]}, {"shapeName": "C_chest_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 127.606377, -8.700024], [-6.231884, 127.540318, -8.633965], [-6.231884, 127.606377, -8.567907], [-6.231884, 127.672435, -8.633965], [-6.231884, 127.606377, -8.700024], [-6.297936, 127.606377, -8.633965], [-6.231884, 127.606377, -8.567907], [-6.165825, 127.606377, -8.633965], [-6.231884, 127.540318, -8.633965], [-6.297936, 127.606377, -8.633965], [-6.231884, 127.672435, -8.633965], [-6.165825, 127.606377, -8.633965], [-6.231884, 127.606377, -8.700024], [-6.297936, 127.606377, -8.633965], [0.0, 127.606377, -8.633965]]}, {"shapeName": "C_chest_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 127.606377, -2.402082], [0.0, 127.540318, -2.402082], [0.066058, 127.606377, -2.402082], [0.0, 127.672435, -2.402082], [-0.066058, 127.606377, -2.402082], [0.0, 127.606377, -2.336029], [0.066058, 127.606377, -2.402082], [0.0, 127.606377, -2.46814], [0.0, 127.540318, -2.402082], [0.0, 127.606377, -2.336029], [0.0, 127.672435, -2.402082], [0.0, 127.606377, -2.46814], [-0.066058, 127.606377, -2.402082], [0.0, 127.606377, -2.336029], [0.0, 127.606377, -8.633965]]}]},
			"L_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_C_CTLShape", "degree": 3, "form": 2, "points": [[59.264565, 97.221524, -2.995155], [59.406078, 98.143501, -2.102802], [58.600855, 98.825087, -1.358882], [57.320583, 98.867019, -1.199175], [56.315228, 98.244734, -1.717233], [56.173715, 97.322758, -2.609587], [56.978938, 96.641171, -3.353506], [58.25921, 96.599239, -3.513213]]}]},
			"C_midTorso_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_midTorso_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.231884, 114.394936, -8.700024], [6.231884, 114.460994, -8.633965], [6.231884, 114.394936, -8.567907], [6.231884, 114.328877, -8.633965], [6.231884, 114.394936, -8.700024], [6.297936, 114.394936, -8.633965], [6.231884, 114.394936, -8.567907], [6.165825, 114.394936, -8.633965], [6.231884, 114.460994, -8.633965], [6.297936, 114.394936, -8.633965], [6.231884, 114.328877, -8.633965], [6.165825, 114.394936, -8.633965], [6.231884, 114.394936, -8.700024], [6.297936, 114.394936, -8.633965], [0.0, 114.394936, -8.633965]]}, {"shapeName": "C_midTorso_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 120.626819, -8.700024], [-0.066058, 120.626819, -8.633965], [0.0, 120.626819, -8.567907], [0.066058, 120.626819, -8.633965], [0.0, 120.626819, -8.700024], [0.0, 120.692872, -8.633965], [0.0, 120.626819, -8.567907], [0.0, 120.560761, -8.633965], [-0.066058, 120.626819, -8.633965], [0.0, 120.692872, -8.633965], [0.066058, 120.626819, -8.633965], [0.0, 120.560761, -8.633965], [0.0, 120.626819, -8.700024], [0.0, 120.692872, -8.633965], [0.0, 114.394936, -8.633965]]}, {"shapeName": "C_midTorso_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 114.460994, -2.402082], [-0.066058, 114.394936, -2.402082], [0.0, 114.328877, -2.402082], [0.066058, 114.394936, -2.402082], [0.0, 114.460994, -2.402082], [0.0, 114.394936, -2.336029], [0.0, 114.328877, -2.402082], [0.0, 114.394936, -2.46814], [-0.066058, 114.394936, -2.402082], [0.0, 114.394936, -2.336029], [0.066058, 114.394936, -2.402082], [0.0, 114.394936, -2.46814], [0.0, 114.460994, -2.402082], [0.0, 114.394936, -2.336029], [0.0, 114.394936, -8.633965]]}]},
			"C_visibility_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_visibility_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.523671, 209.103428, -0.010851], [1.523671, 209.114279, 0.0], [1.523671, 209.103428, 0.010851], [1.523671, 209.092577, 0.0], [1.523671, 209.103428, -0.010851], [1.534521, 209.103428, 0.0], [1.523671, 209.103428, 0.010851], [1.51282, 209.103428, 0.0], [1.523671, 209.114279, 0.0], [1.534521, 209.103428, 0.0], [1.523671, 209.092577, 0.0], [1.51282, 209.103428, 0.0], [1.523671, 209.103428, -0.010851], [1.534521, 209.103428, 0.0], [0.5, 209.103428, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.5, 210.127099, -0.010851], [0.489149, 210.127099, 0.0], [0.5, 210.127099, 0.010851], [0.510851, 210.127099, 0.0], [0.5, 210.127099, -0.010851], [0.5, 210.137949, 0.0], [0.5, 210.127099, 0.010851], [0.5, 210.116248, 0.0], [0.489149, 210.127099, 0.0], [0.5, 210.137949, 0.0], [0.510851, 210.127099, 0.0], [0.5, 210.116248, 0.0], [0.5, 210.127099, -0.010851], [0.5, 210.137949, 0.0], [0.5, 209.103428, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.5, 209.114279, 1.023671], [0.489149, 209.103428, 1.023671], [0.5, 209.092577, 1.023671], [0.510851, 209.103428, 1.023671], [0.5, 209.114279, 1.023671], [0.5, 209.103428, 1.034521], [0.5, 209.092577, 1.023671], [0.5, 209.103428, 1.01282], [0.489149, 209.103428, 1.023671], [0.5, 209.103428, 1.034521], [0.510851, 209.103428, 1.023671], [0.5, 209.103428, 1.01282], [0.5, 209.114279, 1.023671], [0.5, 209.103428, 1.034521], [0.5, 209.103428, 0.0]]}]},
			"R_toe_IK_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-13.1588, 4.846651, 7.543254], [-9.978517, 6.163874, 7.563256], [-6.798233, 4.847213, 7.519904], [-5.48092, 1.667944, 7.438593], [-6.798233, -1.511558, 7.366953], [-9.978517, -2.82878, 7.346952], [-13.1588, -1.512119, 7.390304], [-14.476114, 1.66715, 7.471615]]}]},
			"L_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_C_CTLShape", "degree": 3, "form": 2, "points": [[65.953724, 95.421056, -8.647559], [67.000994, 96.098361, -8.98049], [67.792363, 96.914815, -8.369345], [67.864256, 97.392151, -7.172122], [67.174561, 97.250752, -6.090139], [66.127291, 96.573447, -5.757207], [65.335922, 95.756992, -6.368352], [65.264029, 95.279657, -7.565575]]}]},
			"L_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[75.391982, 84.714585, -8.025226], [75.46763, 84.789737, -7.911769], [75.364809, 84.736263, -7.807792], [75.289161, 84.661111, -7.921249], [75.391982, 84.714585, -8.025226], [75.44143, 84.636732, -7.899788], [75.364809, 84.736263, -7.807792], [75.315356, 84.814125, -7.933231], [75.46763, 84.789737, -7.911769], [75.44143, 84.636732, -7.899788], [75.289161, 84.661111, -7.921249], [75.315356, 84.814125, -7.933231], [75.391982, 84.714585, -8.025226], [75.44143, 84.636732, -7.899788], [69.43127, 93.093335, -9.494035]]}, {"shapeName": "L_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[77.863148, 99.149723, -9.155604], [77.786521, 99.249263, -9.063609], [77.835974, 99.171402, -8.938171], [77.912601, 99.071862, -9.030166], [77.863148, 99.149723, -9.155604], [77.938788, 99.22487, -9.042148], [77.835974, 99.171402, -8.938171], [77.760327, 99.096249, -9.051627], [77.786521, 99.249263, -9.063609], [77.938788, 99.22487, -9.042148], [77.912601, 99.071862, -9.030166], [77.760327, 99.096249, -9.051627], [77.863148, 99.149723, -9.155604], [77.938788, 99.22487, -9.042148], [69.43127, 93.093335, -9.494035]]}, {"shapeName": "L_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[68.238751, 94.180212, 0.766936], [68.086476, 94.204599, 0.745475], [68.060282, 94.051585, 0.757457], [68.212557, 94.027198, 0.778918], [68.238751, 94.180212, 0.766936], [68.135931, 94.126737, 0.870903], [68.060282, 94.051585, 0.757457], [68.163103, 94.105059, 0.65348], [68.086476, 94.204599, 0.745475], [68.135931, 94.126737, 0.870903], [68.212557, 94.027198, 0.778918], [68.163103, 94.105059, 0.65348], [68.238751, 94.180212, 0.766936], [68.135931, 94.126737, 0.870903], [69.43127, 93.093335, -9.494035]]}]},
			"R_wrist_IK_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-57.65017, 100.366276, -14.775631], [-60.48634, 102.966713, -15.212796], [-62.196343, 105.56715, -12.908266], [-61.778478, 106.644284, -9.211995], [-59.477531, 105.56715, -6.28921], [-56.641361, 102.966713, -5.852044], [-54.931357, 100.366276, -8.156575], [-55.349222, 99.289142, -11.852846]]}]},
			"R_leg_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-9.97852, 62.728649, -100.410098], [-9.868422, 62.728035, -100.300002], [-9.97852, 62.727422, -100.189906], [-10.088617, 62.728035, -100.300002], [-9.97852, 62.728649, -100.410098], [-9.97852, 62.838121, -100.299389], [-9.97852, 62.727422, -100.189906], [-9.97852, 62.61794, -100.300615], [-9.868422, 62.728035, -100.300002], [-9.97852, 62.838121, -100.299389], [-10.088617, 62.728035, -100.300002], [-9.97852, 62.61794, -100.300615], [-9.97852, 62.728649, -100.410098], [-9.97852, 62.838121, -100.299389], [-9.97852, 52.341724, -100.357846]]}, {"shapeName": "R_leg_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.407953, 52.342337, -100.467941], [0.407953, 52.231628, -100.358459], [0.407953, 52.341111, -100.24775], [0.407953, 52.45182, -100.357232], [0.407953, 52.342337, -100.467941], [0.51804, 52.341724, -100.357846], [0.407953, 52.341111, -100.24775], [0.297856, 52.341724, -100.357846], [0.407953, 52.231628, -100.358459], [0.51804, 52.341724, -100.357846], [0.407953, 52.45182, -100.357232], [0.297856, 52.341724, -100.357846], [0.407953, 52.342337, -100.467941], [0.51804, 52.341724, -100.357846], [-9.97852, 52.341724, -100.357846]]}, {"shapeName": "R_leg_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.868422, 52.28388, -89.971534], [-9.97852, 52.173784, -89.972147], [-10.088617, 52.28388, -89.971534], [-9.97852, 52.393976, -89.970921], [-9.868422, 52.28388, -89.971534], [-9.97852, 52.283267, -89.861448], [-10.088617, 52.28388, -89.971534], [-9.97852, 52.284493, -90.08163], [-9.97852, 52.173784, -89.972147], [-9.97852, 52.283267, -89.861448], [-9.97852, 52.393976, -89.970921], [-9.97852, 52.284493, -90.08163], [-9.868422, 52.28388, -89.971534], [-9.97852, 52.283267, -89.861448], [-9.97852, 52.341724, -100.357846]]}]},
			"R_loLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_loLeg_FK_CTLShape", "degree": 3, "form": 2, "points": [[-13.953898, 51.167074, 5.032231], [-9.978517, 50.914568, 6.659409], [-6.003136, 51.167074, 5.032231], [-4.356482, 51.776676, 1.103868], [-6.003136, 52.386279, -2.824495], [-9.978517, 52.638784, -4.451673], [-13.953898, 52.386279, -2.824495], [-15.600551, 51.776676, 1.103868]]}]},
			"C_torso_FK_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_C_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 111.752647, -14.721745], [0.0, 111.985615, -14.768085], [0.0, 112.183114, -14.900056], [0.0, 112.315085, -15.097556], [0.0, 112.361425, -15.330523], [0.0, 112.315085, -15.56349], [0.0, 112.183114, -15.76099], [0.0, 111.985615, -15.892961], [0.0, 111.752647, -15.939301], [0.0, 111.51968, -15.892961], [0.0, 111.32218, -15.76099], [0.0, 111.19021, -15.56349], [0.0, 111.143869, -15.330523], [0.0, 111.19021, -15.097556], [0.0, 111.32218, -14.900056], [0.0, 111.51968, -14.768085], [0.0, 111.752647, -14.721745], [0.0, 111.752647, -8.633965]]}]},
			"world_B_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -462.16], [205.32, 0.0, -256.64], [153.92, 0.0, -256.64], [153.92, 0.0, -153.88], [256.68, 0.0, -153.88], [256.68, 0.0, -205.28], [462.16, 0.0, 0.0], [256.64, 0.0, 205.32], [256.64, 0.0, 153.92], [153.88, 0.0, 153.92], [153.88, 0.0, 256.68], [205.28, 0.0, 256.68], [0.0, 0.0, 462.16], [-205.32, 0.0, 256.64], [-153.92, 0.0, 256.64], [-153.92, 0.0, 153.88], [-256.68, 0.0, 153.88], [-256.68, 0.0, 205.28], [-462.16, 0.0, 0.0], [-256.64, 0.0, -205.32], [-256.64, 0.0, -153.92], [-153.88, 0.0, -153.92], [-153.88, 0.0, -256.68], [-205.28, 0.0, -256.68], [0.0, 0.0, -462.16], [40.24, 0.56, -422.64], [36.72, 0.0, -418.88], [36.72, 0.0, -403.52], [33.52, 0.0, -403.52], [33.72, 0.0, -419.0], [31.44, 0.0, -417.84], [31.52, 0.0, -411.12], [28.28, 0.0, -411.12], [28.28, 0.0, -417.84], [26.28, 0.0, -419.0], [26.28, 0.0, -403.28], [23.04, 0.0, -403.28], [23.04, 0.0, -419.4], [25.64, 0.0, -422.0], [29.64, 0.0, -420.0], [34.04, 0.0, -422.0], [36.72, 0.0, -418.96], [34.04, 0.0, -422.0], [29.68, 0.0, -420.04], [25.64, 0.0, -421.96], [17.84, 0.0, -422.0], [20.48, 0.0, -419.4], [20.48, 0.0, -405.92], [17.84, 0.0, -403.28], [9.4, 0.0, -403.28], [6.8, 0.0, -405.92], [6.8, 0.0, -419.4], [9.4, 0.0, -422.0], [17.84, 0.0, -422.0], [16.84, 0.0, -419.0], [17.24, 0.0, -406.6], [10.0, 0.0, -406.68], [10.04, 0.0, -419.0], [16.88, 0.0, -419.08], [17.84, 0.0, -422.0], [9.4, 0.0, -422.0], [4.0, 0.0, -422.0], [4.2, 0.0, -403.28], [-4.92, 0.0, -403.28], [-7.56, 0.0, -405.92], [-7.56, 0.0, -411.56], [-4.88, 0.0, -414.16], [-4.72, 0.0, -414.36], [-9.96, 0.0, -421.92], [-9.96, 0.0, -422.0], [-6.2, 0.0, -422.0], [-0.96, 0.0, -414.4], [1.0, 0.0, -414.4], [1.0, 0.0, -406.4], [-4.04, 0.0, -406.4], [-4.08, 0.0, -411.16], [1.0, 0.0, -411.16], [1.0, 0.0, -422.0], [4.0, 0.0, -422.0], [-25.72, 0.0, -422.0], [-25.72, 0.0, -419.0], [-15.24, 0.0, -418.96], [-15.24, 0.0, -403.28], [-12.0, 0.0, -403.28], [-12.0, 0.0, -422.0], [-39.36, 0.0, -422.0], [-41.76, 0.0, -419.4], [-41.96, 0.0, -405.92], [-39.36, 0.0, -403.28], [-28.28, 0.0, -403.28], [-28.28, 0.0, -422.0], [-31.56, 0.0, -419.0], [-31.48, 0.0, -406.32], [-38.32, 0.0, -406.32], [-38.24, 0.0, -418.92], [-31.44, 0.0, -419.08], [-28.2, 0.0, -422.0]]}]},
			"L_upLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 80.783151, -3.523062], [9.868419, 80.765401, -3.631719], [9.978517, 80.747651, -3.740376], [10.088614, 80.765401, -3.631719], [9.978517, 80.783151, -3.523062], [9.978517, 80.656754, -3.613971], [9.978517, 80.747651, -3.740376], [9.978517, 80.874058, -3.649469], [9.868419, 80.765401, -3.631719], [9.978517, 80.656754, -3.613971], [10.088614, 80.765401, -3.631719], [9.978517, 80.874058, -3.649469], [9.978517, 80.783151, -3.523062], [9.978517, 80.656754, -3.613971], [9.978517, 91.015999, -5.306253]]}, {"shapeName": "L_upLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.407956, 91.033749, -5.197596], [-0.407956, 91.124656, -5.324003], [-0.407956, 90.998249, -5.41491], [-0.407956, 90.907342, -5.288503], [-0.407956, 91.033749, -5.197596], [-0.518043, 91.015999, -5.306253], [-0.407956, 90.998249, -5.41491], [-0.297859, 91.015999, -5.306253], [-0.407956, 91.124656, -5.324003], [-0.518043, 91.015999, -5.306253], [-0.407956, 90.907342, -5.288503], [-0.297859, 91.015999, -5.306253], [-0.407956, 91.033749, -5.197596], [-0.518043, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}, {"shapeName": "L_upLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.868419, 89.341465, -15.556851], [9.978517, 89.450122, -15.574601], [10.088614, 89.341465, -15.556851], [9.978517, 89.232808, -15.5391], [9.868419, 89.341465, -15.556851], [9.978517, 89.323717, -15.665498], [10.088614, 89.341465, -15.556851], [9.978517, 89.359215, -15.448193], [9.978517, 89.450122, -15.574601], [9.978517, 89.323717, -15.665498], [9.978517, 89.232808, -15.5391], [9.978517, 89.359215, -15.448193], [9.868419, 89.341465, -15.556851], [9.978517, 89.323717, -15.665498], [9.978517, 91.015999, -5.306253]]}]},
			"world_C_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -404.39], [179.655, 0.0, -224.56], [134.68, 0.0, -224.56], [134.68, 0.0, -134.645], [224.595, 0.0, -134.645], [224.595, 0.0, -179.62], [404.39, 0.0, 0.0], [224.56, 0.0, 179.655], [224.56, 0.0, 134.68], [134.645, 0.0, 134.68], [134.645, 0.0, 224.595], [179.62, 0.0, 224.595], [0.0, 0.0, 404.39], [-179.655, 0.0, 224.56], [-134.68, 0.0, 224.56], [-134.68, 0.0, 134.645], [-224.595, 0.0, 134.645], [-224.595, 0.0, 179.62], [-404.39, 0.0, 0.0], [-224.56, 0.0, -179.655], [-224.56, 0.0, -134.68], [-134.645, 0.0, -134.68], [-134.645, 0.0, -224.595], [-179.62, 0.0, -224.595], [0.0, 0.0, -404.39], [35.21, 0.49, -369.81], [32.13, 0.0, -366.52], [32.13, 0.0, -353.08], [29.33, 0.0, -353.08], [29.505, 0.0, -366.625], [27.51, 0.0, -365.61], [27.58, 0.0, -359.73], [24.745, 0.0, -359.73], [24.745, 0.0, -365.61], [22.995, 0.0, -366.625], [22.995, 0.0, -352.87], [20.16, 0.0, -352.87], [20.16, 0.0, -366.975], [22.435, 0.0, -369.25], [25.935, 0.0, -367.5], [29.785, 0.0, -369.25], [32.13, 0.0, -366.59], [29.785, 0.0, -369.25], [25.97, 0.0, -367.535], [22.435, 0.0, -369.215], [15.61, 0.0, -369.25], [17.92, 0.0, -366.975], [17.92, 0.0, -355.18], [15.61, 0.0, -352.87], [8.225, 0.0, -352.87], [5.95, 0.0, -355.18], [5.95, 0.0, -366.975], [8.225, 0.0, -369.25], [15.61, 0.0, -369.25], [14.735, 0.0, -366.625], [15.085, 0.0, -355.775], [8.75, 0.0, -355.845], [8.785, 0.0, -366.625], [14.77, 0.0, -366.695], [15.61, 0.0, -369.25], [8.225, 0.0, -369.25], [3.5, 0.0, -369.25], [3.675, 0.0, -352.87], [-4.305, 0.0, -352.87], [-6.615, 0.0, -355.18], [-6.615, 0.0, -360.115], [-4.27, 0.0, -362.39], [-4.13, 0.0, -362.565], [-8.715, 0.0, -369.18], [-8.715, 0.0, -369.25], [-5.425, 0.0, -369.25], [-0.84, 0.0, -362.6], [0.875, 0.0, -362.6], [0.875, 0.0, -355.6], [-3.535, 0.0, -355.6], [-3.57, 0.0, -359.765], [0.875, 0.0, -359.765], [0.875, 0.0, -369.25], [3.5, 0.0, -369.25], [-22.505, 0.0, -369.25], [-22.505, 0.0, -366.625], [-13.335, 0.0, -366.59], [-13.335, 0.0, -352.87], [-10.5, 0.0, -352.87], [-10.5, 0.0, -369.25], [-34.44, 0.0, -369.25], [-36.54, 0.0, -366.975], [-36.715, 0.0, -355.18], [-34.44, 0.0, -352.87], [-24.745, 0.0, -352.87], [-24.745, 0.0, -369.25], [-27.615, 0.0, -366.625], [-27.545, 0.0, -355.53], [-33.53, 0.0, -355.53], [-33.46, 0.0, -366.555], [-27.51, 0.0, -366.695], [-24.675, 0.0, -369.25]]}]},
			"C_torso_FK_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 123.269107, -8.700024], [-0.066058, 123.269107, -8.633965], [0.0, 123.269107, -8.567907], [0.066058, 123.269107, -8.633965], [0.0, 123.269107, -8.700024], [0.0, 123.33516, -8.633965], [0.0, 123.269107, -8.567907], [0.0, 123.203049, -8.633965], [-0.066058, 123.269107, -8.633965], [0.0, 123.33516, -8.633965], [0.066058, 123.269107, -8.633965], [0.0, 123.203049, -8.633965], [0.0, 123.269107, -8.700024], [0.0, 123.33516, -8.633965], [0.0, 117.037224, -8.633965]]}, {"shapeName": "C_torso_FK_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 117.037224, -8.700024], [-6.231884, 116.971165, -8.633965], [-6.231884, 117.037224, -8.567907], [-6.231884, 117.103282, -8.633965], [-6.231884, 117.037224, -8.700024], [-6.297936, 117.037224, -8.633965], [-6.231884, 117.037224, -8.567907], [-6.165825, 117.037224, -8.633965], [-6.231884, 116.971165, -8.633965], [-6.297936, 117.037224, -8.633965], [-6.231884, 117.103282, -8.633965], [-6.165825, 117.037224, -8.633965], [-6.231884, 117.037224, -8.700024], [-6.297936, 117.037224, -8.633965], [0.0, 117.037224, -8.633965]]}, {"shapeName": "C_torso_FK_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 117.037224, -2.402082], [0.0, 116.971165, -2.402082], [0.066058, 117.037224, -2.402082], [0.0, 117.103282, -2.402082], [-0.066058, 117.037224, -2.402082], [0.0, 117.037224, -2.336029], [0.066058, 117.037224, -2.402082], [0.0, 117.037224, -2.46814], [0.0, 116.971165, -2.402082], [0.0, 117.037224, -2.336029], [0.0, 117.103282, -2.402082], [0.0, 117.037224, -2.46814], [-0.066058, 117.037224, -2.402082], [0.0, 117.037224, -2.336029], [0.0, 117.037224, -8.633965]]}]},
			"R_toe_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_toe_FK_CTLShape", "degree": 3, "form": 2, "points": [[-13.953871, 5.641427, 7.565292], [-9.978517, 7.287955, 7.590294], [-6.003162, 5.642129, 7.536104], [-4.35652, 1.668043, 7.434465], [-6.003162, -2.306334, 7.344916], [-9.978517, -3.952862, 7.319914], [-13.953871, -2.307036, 7.374104], [-15.600513, 1.66705, 7.475743]]}]},
			"R_upArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_upArm_FK_CTLShape", "degree": 3, "form": 2, "points": [[-16.108188, 143.274215, -14.009061], [-18.803733, 146.266917, -15.523291], [-21.952812, 148.661537, -13.830892], [-23.710735, 149.055336, -9.923239], [-23.047742, 147.217637, -6.089387], [-20.352197, 144.224935, -4.575157], [-17.203118, 141.830315, -6.267556], [-15.445194, 141.436516, -10.175209]]}]},
			"R_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_A_CTLShape", "degree": 3, "form": 2, "points": [[-61.258046, 101.78456, -16.798184], [-61.100425, 102.966713, -17.29218], [-60.942805, 104.148866, -16.798184], [-60.877517, 104.638528, -15.60557], [-60.942805, 104.148866, -14.412956], [-61.100425, 102.966713, -13.91896], [-61.258046, 101.78456, -14.412956], [-61.323334, 101.294898, -15.60557]]}]},
			"L_arm_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[64.406508, 107.91281, -8.132517], [64.201294, 107.678043, -8.21681], [63.939593, 107.861232, -8.324305], [63.72983, 107.759724, -8.410467], [63.681926, 107.426664, -8.430143], [63.383258, 107.417531, -8.552823], [63.31803, 107.747103, -8.579616], [63.1033, 107.83568, -8.667817], [62.851577, 107.63677, -8.771214], [62.634409, 107.858629, -8.860417], [62.803879, 108.141569, -8.790806], [62.709958, 108.368308, -8.829385], [62.401881, 108.420104, -8.955929], [62.393433, 108.742986, -8.959399], [62.698316, 108.813517, -8.834167], [62.780204, 109.045662, -8.800531], [62.596231, 109.317772, -8.876098], [62.801445, 109.55254, -8.791806], [63.063165, 109.369373, -8.684303], [63.272928, 109.470881, -8.598141], [63.320832, 109.803941, -8.578465], [63.619487, 109.813059, -8.45579], [63.684749, 109.483481, -8.428984], [63.899458, 109.394925, -8.340791], [64.151162, 109.593813, -8.237402], [64.368331, 109.371954, -8.148199], [64.19888, 109.089036, -8.217802], [64.292821, 108.862276, -8.179215], [64.600864, 108.810486, -8.052685], [64.609325, 108.487619, -8.049209], [64.304443, 108.417087, -8.174441], [64.222555, 108.184943, -8.208077], [64.406508, 107.91281, -8.132517]]}, {"shapeName": "L_arm_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[63.959843, 108.629307, -8.315988], [63.816391, 108.97568, -8.374911], [63.488398, 109.110935, -8.509636], [63.168028, 108.955839, -8.64123], [63.042915, 108.601298, -8.69262], [63.186367, 108.254925, -8.633697], [63.51436, 108.11967, -8.498972], [63.834717, 108.274751, -8.367384]]}, {"shapeName": "L_arm_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[62.742993, 107.747699, -8.815815], [58.56385, 102.966713, -10.53242]]}]},
			"C_cog_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[21.900534, 98.139605, -7.057898], [21.877435, 98.139605, -10.503291], [15.932302, 98.139605, -12.572031], [15.119853, 98.139605, -15.016893], [18.644276, 98.139605, -20.231719], [16.600455, 98.139605, -23.005519], [10.57386, 98.139605, -21.188375], [8.480114, 98.139605, -22.688854], [8.266564, 98.139605, -28.975571], [4.982648, 98.139605, -30.018312], [1.176561, 98.139605, -25.009343], [-1.398745, 98.139605, -24.992314], [-5.268718, 98.139605, -29.949627], [-8.538345, 98.139605, -28.862988], [-8.670148, 98.139605, -22.575483], [-10.743336, 98.139605, -21.047455], [-16.791519, 98.139605, -22.781822], [-18.797995, 98.139605, -19.980869], [-15.20515, 98.139605, -14.816427], [-15.98433, 98.139605, -12.361067], [-21.900534, 98.139605, -10.210033], [-21.877435, 98.139605, -6.76464], [-15.932302, 98.139605, -4.6959], [-15.119853, 98.139605, -2.251038], [-18.644276, 98.139605, 2.963788], [-16.600455, 98.139605, 5.737588], [-10.57386, 98.139605, 3.920444], [-8.480114, 98.139605, 5.420923], [-8.266564, 98.139605, 11.70764], [-4.982648, 98.139605, 12.750381], [-1.176561, 98.139605, 7.741412], [1.398745, 98.139605, 7.724383], [5.268718, 98.139605, 12.681696], [8.538345, 98.139605, 11.595057], [8.670148, 98.139605, 5.307552], [10.743336, 98.139605, 3.779524], [16.791519, 98.139605, 5.513891], [18.797995, 98.139605, 2.712938], [15.20515, 98.139605, -2.451504], [15.98433, 98.139605, -4.906864], [21.900534, 98.139605, -7.057898]]}]},
			"R_toeTip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_toeTip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.432422, 1.504777, 14.48181], [0.433025, 1.612594, 14.36948], [0.433604, 1.500263, 14.261665], [0.433001, 1.392445, 14.373994], [0.432422, 1.504777, 14.48181], [0.543099, 1.50252, 14.372328], [0.433604, 1.500263, 14.261665], [0.322917, 1.50252, 14.371147], [0.433025, 1.612594, 14.36948], [0.543099, 1.50252, 14.372328], [0.433001, 1.392445, 14.373994], [0.322917, 1.50252, 14.371147], [0.432422, 1.504777, 14.48181], [0.543099, 1.50252, 14.372328], [-9.95331, 1.50252, 14.316]]}, {"shapeName": "R_toeTip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-9.952758, 11.889068, 14.213189], [-10.062264, 11.88681, 14.102526], [-9.951577, 11.884554, 13.993044], [-9.842072, 11.88681, 14.103707], [-9.952758, 11.889068, 14.213189], [-9.952156, 11.996875, 14.100861], [-9.951577, 11.884554, 13.993044], [-9.95218, 11.776736, 14.105374], [-10.062264, 11.88681, 14.102526], [-9.952156, 11.996875, 14.100861], [-9.842072, 11.88681, 14.103707], [-9.95218, 11.776736, 14.105374], [-9.952758, 11.889068, 14.213189], [-9.952156, 11.996875, 14.100861], [-9.95331, 1.50252, 14.316]]}, {"shapeName": "R_toeTip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.897573, 1.399708, 3.929602], [-10.007681, 1.289634, 3.931268], [-9.897597, 1.179559, 3.934116], [-9.787489, 1.289634, 3.93245], [-9.897573, 1.399708, 3.929602], [-9.896994, 1.287377, 3.821797], [-9.897597, 1.179559, 3.934116], [-9.898176, 1.29189, 4.041932], [-10.007681, 1.289634, 3.931268], [-9.896994, 1.287377, 3.821797], [-9.787489, 1.289634, 3.93245], [-9.898176, 1.29189, 4.041932], [-9.897573, 1.399708, 3.929602], [-9.896994, 1.287377, 3.821797], [-9.95331, 1.50252, 14.316]]}]},
			"L_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_B_CTLShape", "degree": 3, "form": 2, "points": [[65.000393, 102.285212, -16.798184], [64.905288, 103.474028, -17.29218], [64.810182, 104.662844, -16.798184], [64.770789, 105.155267, -15.60557], [64.810182, 104.662844, -14.412956], [64.905288, 103.474028, -13.91896], [65.000393, 102.285212, -14.412956], [65.039787, 101.792789, -15.60557]]}]},
			"R_toe_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-10.016661, 1.807241, -2.930947], [-9.906564, 1.917316, -2.928703], [-10.016661, 2.027372, -2.925652], [-10.126757, 1.917296, -2.927895], [-10.016661, 1.807241, -2.930947], [-10.017065, 1.919954, -3.038354], [-10.016661, 2.027372, -2.925652], [-10.016257, 1.914659, -2.818234], [-9.906564, 1.917316, -2.928703], [-10.017065, 1.919954, -3.038354], [-10.126757, 1.917296, -2.927895], [-10.016257, 1.914659, -2.818234], [-10.016661, 1.807241, -2.930947], [-10.017065, 1.919954, -3.038354], [-9.97852, 1.66755, 7.4551]]}, {"shapeName": "R_toe_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.407883, 1.558401, 7.414323], [0.408287, 1.66582, 7.527035], [0.407883, 1.778533, 7.419618], [0.407478, 1.671114, 7.306905], [0.407883, 1.558401, 7.414323], [0.51797, 1.668477, 7.416566], [0.407883, 1.778533, 7.419618], [0.297786, 1.668458, 7.417374], [0.408287, 1.66582, 7.527035], [0.51797, 1.668477, 7.416566], [0.407478, 1.671114, 7.306905], [0.297786, 1.668458, 7.417374], [0.407883, 1.558401, 7.414323], [0.51797, 1.668477, 7.416566], [-9.97852, 1.66755, 7.4551]]}, {"shapeName": "R_toe_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.868423, 12.051029, 7.704454], [-9.978116, 12.048372, 7.814923], [-10.088616, 12.051009, 7.705262], [-9.978924, 12.053667, 7.594793], [-9.868423, 12.051029, 7.704454], [-9.97852, 12.161075, 7.707505], [-10.088616, 12.051009, 7.705262], [-9.97852, 11.940954, 7.702211], [-9.978116, 12.048372, 7.814923], [-9.97852, 12.161075, 7.707505], [-9.978924, 12.053667, 7.594793], [-9.97852, 11.940954, 7.702211], [-9.868423, 12.051029, 7.704454], [-9.97852, 12.161075, 7.707505], [-9.97852, 1.66755, 7.4551]]}]},
			"L_leg_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 17.857097, -5.881634], [9.868419, 17.857097, -5.771536], [9.978517, 17.857097, -5.661439], [10.088614, 17.857097, -5.771536], [9.978517, 17.857097, -5.881634], [9.978517, 17.967184, -5.771536], [9.978517, 17.857097, -5.661439], [9.978517, 17.746999, -5.771536], [9.868419, 17.857097, -5.771536], [9.978517, 17.967184, -5.771536], [10.088614, 17.857097, -5.771536], [9.978517, 17.746999, -5.771536], [9.978517, 17.857097, -5.881634], [9.978517, 17.967184, -5.771536], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_leg_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.407956, 7.470624, -5.881634], [-0.407956, 7.360526, -5.771536], [-0.407956, 7.470624, -5.661439], [-0.407956, 7.580721, -5.771536], [-0.407956, 7.470624, -5.881634], [-0.518043, 7.470624, -5.771536], [-0.407956, 7.470624, -5.661439], [-0.297859, 7.470624, -5.771536], [-0.407956, 7.360526, -5.771536], [-0.518043, 7.470624, -5.771536], [-0.407956, 7.580721, -5.771536], [-0.297859, 7.470624, -5.771536], [-0.407956, 7.470624, -5.881634], [-0.518043, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_leg_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.868419, 7.470624, 4.614936], [9.978517, 7.360526, 4.614936], [10.088614, 7.470624, 4.614936], [9.978517, 7.580721, 4.614936], [9.868419, 7.470624, 4.614936], [9.978517, 7.470624, 4.725024], [10.088614, 7.470624, 4.614936], [9.978517, 7.470624, 4.504839], [9.978517, 7.360526, 4.614936], [9.978517, 7.470624, 4.725024], [9.978517, 7.580721, 4.614936], [9.978517, 7.470624, 4.504839], [9.868419, 7.470624, 4.614936], [9.978517, 7.470624, 4.725024], [9.978517, 7.470624, -5.771536]]}]},
			"L_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_B_CTLShape", "degree": 3, "form": 2, "points": [[59.191712, 99.107888, -5.585468], [59.325236, 100.144685, -4.828114], [58.512024, 100.941091, -4.219194], [57.228443, 101.030583, -4.115405], [56.226397, 100.360738, -4.577545], [56.092873, 99.323941, -5.334899], [56.906085, 98.527534, -5.943819], [58.189666, 98.438043, -6.047608]]}]},
			"R_leg_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-17.118368, 8.53224, -5.606795], [-16.827661, 8.53224, -5.606795], [-16.772607, 8.237464, -5.652538], [-16.56603, 8.152885, -5.665663], [-16.316151, 8.322855, -5.639287], [-16.110588, 8.119723, -5.670809], [-16.282583, 7.872827, -5.709123], [-16.197028, 7.668666, -5.740804], [-15.898697, 7.614263, -5.749247], [-15.898697, 7.326985, -5.793826], [-16.197028, 7.272582, -5.802269], [-16.282583, 7.068448, -5.833946], [-16.110588, 6.821524, -5.872263], [-16.316151, 6.618393, -5.903785], [-16.56603, 6.788363, -5.87741], [-16.772607, 6.703784, -5.890534], [-16.827661, 6.409008, -5.936278], [-17.118368, 6.409008, -5.936278], [-17.17345, 6.703784, -5.890534], [-17.380027, 6.788363, -5.87741], [-17.629906, 6.618393, -5.903785], [-17.835451, 6.821524, -5.872263], [-17.663474, 7.068448, -5.833946], [-17.749029, 7.272582, -5.802269], [-18.047333, 7.326985, -5.793826], [-18.047333, 7.614263, -5.749247], [-17.749029, 7.668666, -5.740804], [-17.663474, 7.872827, -5.709123], [-17.835451, 8.119723, -5.670809], [-17.629906, 8.322855, -5.639287], [-17.380027, 8.152885, -5.665663], [-17.17345, 8.237464, -5.652538], [-17.118368, 8.53224, -5.606795]]}, {"shapeName": "R_leg_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-17.288564, 7.782446, -5.723148], [-17.419275, 7.470624, -5.771536], [-17.288564, 7.158802, -5.819925], [-16.973019, 7.029664, -5.839964], [-16.657493, 7.158802, -5.819925], [-16.526782, 7.470624, -5.771536], [-16.657493, 7.782446, -5.723148], [-16.973019, 7.911584, -5.703108]]}, {"shapeName": "R_leg_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-15.898697, 7.470624, -5.771536], [-9.978517, 7.470624, -5.771536]]}]},
			"L_loLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 41.496164, -0.380045], [9.868419, 41.513046, -0.48884], [9.978517, 41.529929, -0.597635], [10.088614, 41.513046, -0.48884], [9.978517, 41.496164, -0.380045], [9.978517, 41.404261, -0.505721], [9.978517, 41.529929, -0.597635], [9.978517, 41.621842, -0.471957], [9.868419, 41.513046, -0.48884], [9.978517, 41.404261, -0.505721], [10.088614, 41.513046, -0.48884], [9.978517, 41.621842, -0.471957], [9.978517, 41.496164, -0.380045], [9.978517, 41.404261, -0.505721], [9.978517, 51.776676, 1.103868]]}, {"shapeName": "L_loLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.407956, 51.759793, 1.212663], [-0.407956, 51.885472, 1.120751], [-0.407956, 51.793559, 0.995073], [-0.407956, 51.667881, 1.086985], [-0.407956, 51.759793, 1.212663], [-0.518043, 51.776676, 1.103868], [-0.407956, 51.793559, 0.995073], [-0.297859, 51.776676, 1.103868], [-0.407956, 51.885472, 1.120751], [-0.518043, 51.776676, 1.103868], [-0.407956, 51.667881, 1.086985], [-0.297859, 51.776676, 1.103868], [-0.407956, 51.759793, 1.212663], [-0.518043, 51.776676, 1.103868], [9.978517, 51.776676, 1.103868]]}, {"shapeName": "L_loLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.868419, 53.369384, -9.159762], [9.978517, 53.47818, -9.142879], [10.088614, 53.369384, -9.159762], [9.978517, 53.260589, -9.176645], [9.868419, 53.369384, -9.159762], [9.978517, 53.386265, -9.268547], [10.088614, 53.369384, -9.159762], [9.978517, 53.352501, -9.050966], [9.978517, 53.47818, -9.142879], [9.978517, 53.386265, -9.268547], [9.978517, 53.260589, -9.176645], [9.978517, 53.352501, -9.050966], [9.868419, 53.369384, -9.159762], [9.978517, 53.386265, -9.268547], [9.978517, 51.776676, 1.103868]]}]},
			"L_arm_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[63.822242, 107.418201, -8.372508], [63.63755, 107.20691, -8.448371], [63.402019, 107.37178, -8.545117], [63.213232, 107.280423, -8.622662], [63.170118, 106.980669, -8.640371], [62.901317, 106.972449, -8.750783], [62.842612, 107.269064, -8.774896], [62.649355, 107.348784, -8.854277], [62.422804, 107.169764, -8.947334], [62.227353, 107.369437, -9.027617], [62.379876, 107.624083, -8.964967], [62.295347, 107.828149, -8.999688], [62.018078, 107.874765, -9.113578], [62.010475, 108.165358, -9.116701], [62.284869, 108.228837, -9.003992], [62.358568, 108.437767, -8.97372], [62.192993, 108.682666, -9.041731], [62.377686, 108.893957, -8.965867], [62.613234, 108.729107, -8.869114], [62.80202, 108.820464, -8.791569], [62.845134, 109.120218, -8.77386], [63.113924, 109.128424, -8.663453], [63.172659, 108.831804, -8.639327], [63.365898, 108.752103, -8.559954], [63.592431, 108.931103, -8.466904], [63.787882, 108.73143, -8.386621], [63.635377, 108.476804, -8.449264], [63.719924, 108.272719, -8.414536], [63.997163, 108.226109, -8.300658], [64.004778, 107.935529, -8.29753], [63.730383, 107.87205, -8.410239], [63.656684, 107.66312, -8.440512], [63.822242, 107.418201, -8.372508]]}, {"shapeName": "L_arm_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[63.420244, 108.063048, -8.537631], [63.291137, 108.374783, -8.590662], [62.995943, 108.496513, -8.711914], [62.70761, 108.356927, -8.830349], [62.595009, 108.037839, -8.8766], [62.724116, 107.726104, -8.823569], [63.019309, 107.604374, -8.702317], [63.307631, 107.743947, -8.583887]]}, {"shapeName": "L_arm_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[62.325078, 107.269601, -8.987476], [58.56385, 102.966713, -10.53242]]}]},
			"R_loArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_loArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-45.684849, 117.073958, -14.614821], [-45.748818, 117.163398, -14.504588], [-45.650922, 117.103638, -14.399289], [-45.586952, 117.014197, -14.509522], [-45.684849, 117.073958, -14.614821], [-45.740567, 117.009206, -14.484654], [-45.650922, 117.103638, -14.399289], [-45.595197, 117.168397, -14.529458], [-45.748818, 117.163398, -14.504588], [-45.740567, 117.009206, -14.484654], [-45.586952, 117.014197, -14.509522], [-45.595197, 117.168397, -14.529458], [-45.684849, 117.073958, -14.614821], [-45.740567, 117.009206, -14.484654], [-38.810577, 124.598083, -16.620529]]}, {"shapeName": "R_loArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-46.462662, 131.620969, -16.495544], [-46.37301, 131.715408, -16.410181], [-46.428734, 131.650648, -16.280012], [-46.518386, 131.556209, -16.365375], [-46.462662, 131.620969, -16.495544], [-46.526624, 131.710402, -16.385311], [-46.428734, 131.650648, -16.280012], [-46.364765, 131.561208, -16.390245], [-46.37301, 131.715408, -16.410181], [-46.526624, 131.710402, -16.385311], [-46.518386, 131.556209, -16.365375], [-46.364765, 131.561208, -16.390245], [-46.462662, 131.620969, -16.495544], [-46.526624, 131.710402, -16.385311], [-38.810577, 124.598083, -16.620529]]}, {"shapeName": "R_loArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-37.291174, 126.072638, -6.451555], [-37.137553, 126.077637, -6.476425], [-37.129308, 125.923437, -6.456489], [-37.282929, 125.918439, -6.431619], [-37.291174, 126.072638, -6.451555], [-37.193279, 126.012876, -6.346266], [-37.129308, 125.923437, -6.456489], [-37.227205, 125.983198, -6.561788], [-37.137553, 126.077637, -6.476425], [-37.193279, 126.012876, -6.346266], [-37.282929, 125.918439, -6.431619], [-37.227205, 125.983198, -6.561788], [-37.291174, 126.072638, -6.451555], [-37.193279, 126.012876, -6.346266], [-38.810577, 124.598083, -16.620529]]}]},
			"L_reverseBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_reverseBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[20.364249, 1.66529, 7.289294], [20.364828, 1.777621, 7.39711], [20.36543, 1.669803, 7.50944], [20.364852, 1.557473, 7.401623], [20.364249, 1.66529, 7.289294], [20.474925, 1.667547, 7.398776], [20.36543, 1.669803, 7.50944], [20.254744, 1.667547, 7.399958], [20.364828, 1.777621, 7.39711], [20.474925, 1.667547, 7.398776], [20.364852, 1.557473, 7.401623], [20.254744, 1.667547, 7.399958], [20.364249, 1.66529, 7.289294], [20.474925, 1.667547, 7.398776], [9.978517, 1.667547, 7.455104]]}, {"shapeName": "L_reverseBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[9.976783, 12.049581, 7.132148], [9.867278, 12.051838, 7.242812], [9.977965, 12.054094, 7.352294], [10.08747, 12.051838, 7.24163], [9.976783, 12.049581, 7.132148], [9.977362, 12.161902, 7.239964], [9.977965, 12.054094, 7.352294], [9.977386, 11.941763, 7.244477], [9.867278, 12.051838, 7.242812], [9.977362, 12.161902, 7.239964], [10.08747, 12.051838, 7.24163], [9.977386, 11.941763, 7.244477], [9.976783, 12.049581, 7.132148], [9.977362, 12.161902, 7.239964], [9.978517, 1.667547, 7.455104]]}, {"shapeName": "L_reverseBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[10.03423, 1.990507, 17.836988], [9.924146, 1.880433, 17.839836], [10.034254, 1.770359, 17.841502], [10.144338, 1.880433, 17.838654], [10.03423, 1.990507, 17.836988], [10.034833, 1.882689, 17.949308], [10.034254, 1.770359, 17.841502], [10.033651, 1.878176, 17.729172], [9.924146, 1.880433, 17.839836], [10.034833, 1.882689, 17.949308], [10.144338, 1.880433, 17.838654], [10.033651, 1.878176, 17.729172], [10.03423, 1.990507, 17.836988], [10.034833, 1.882689, 17.949308], [9.978517, 1.667547, 7.455104]]}]},
			"R_toe_IK_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-13.556335, 5.244039, 7.554273], [-9.978517, 6.725915, 7.576775], [-6.400698, 5.244671, 7.528004], [-4.91872, 1.667994, 7.436529], [-6.400698, -1.908946, 7.355935], [-9.978517, -3.390821, 7.333433], [-13.556335, -1.909577, 7.382204], [-15.038313, 1.6671, 7.473679]]}]},
			"R_outterBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_outterBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-4.896368, 1.435407, 4.52093], [-4.895765, 1.543225, 4.408601], [-4.895186, 1.430894, 4.300784], [-4.895789, 1.323076, 4.413113], [-4.896368, 1.435407, 4.52093], [-4.785691, 1.43315, 4.411448], [-4.895186, 1.430894, 4.300784], [-5.005873, 1.43315, 4.410266], [-4.895765, 1.543225, 4.408601], [-4.785691, 1.43315, 4.411448], [-4.895789, 1.323076, 4.413113], [-5.005873, 1.43315, 4.410266], [-4.896368, 1.435407, 4.52093], [-4.785691, 1.43315, 4.411448], [-15.2821, 1.43315, 4.35512]]}, {"shapeName": "R_outterBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-15.281548, 11.819697, 4.25231], [-15.391053, 11.817441, 4.141646], [-15.280367, 11.815184, 4.032164], [-15.170861, 11.817441, 4.142828], [-15.281548, 11.819697, 4.25231], [-15.280945, 11.927505, 4.13998], [-15.280367, 11.815184, 4.032164], [-15.280969, 11.707367, 4.144493], [-15.391053, 11.817441, 4.141646], [-15.280945, 11.927505, 4.13998], [-15.170861, 11.817441, 4.142828], [-15.280969, 11.707367, 4.144493], [-15.281548, 11.819697, 4.25231], [-15.280945, 11.927505, 4.13998], [-15.2821, 1.43315, 4.35512]]}, {"shapeName": "R_outterBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-15.226363, 1.330339, -6.031278], [-15.33647, 1.220264, -6.029612], [-15.226386, 1.11019, -6.026765], [-15.116279, 1.220264, -6.028431], [-15.226363, 1.330339, -6.031278], [-15.225784, 1.218008, -6.139084], [-15.226386, 1.11019, -6.026765], [-15.226965, 1.222521, -5.918949], [-15.33647, 1.220264, -6.029612], [-15.225784, 1.218008, -6.139084], [-15.116279, 1.220264, -6.028431], [-15.226965, 1.222521, -5.918949], [-15.226363, 1.330339, -6.031278], [-15.225784, 1.218008, -6.139084], [-15.2821, 1.43315, 4.35512]]}]},
			"R_heel_CTL": {"color": 20, "shapes": [{"shapeName": "R_heel_CTLShape", "degree": 1, "form": 0, "points": [[-9.813801, 0.969538, -11.681757], [-9.808469, -0.065675, -12.675363], [-10.822972, 0.948742, -12.701604], [-9.813801, 0.969538, -11.681757], [-8.793742, 0.948742, -12.690714], [-9.808469, -0.065675, -12.675363], [-9.802913, 0.927945, -13.710561], [-8.793742, 0.948742, -12.690714], [-9.808245, 1.963159, -12.716955], [-9.813801, 0.969538, -11.681757], [-10.822972, 0.948742, -12.701604], [-9.802913, 0.927945, -13.710561], [-9.808245, 1.963159, -12.716955], [-10.822972, 0.948742, -12.701604]]}]},
			"R_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_A_CTLShape", "degree": 3, "form": 2, "points": [[-59.255902, 100.624629, -8.451258], [-59.388957, 101.755964, -7.84402], [-58.575276, 102.646909, -7.385215], [-57.291501, 102.775559, -7.343606], [-56.28965, 102.066555, -7.743566], [-56.156594, 100.935221, -8.350805], [-56.970275, 100.044276, -8.80961], [-58.25405, 99.915625, -8.851219]]}]},
			"R_outterBall_CTL": {"color": 20, "shapes": [{"shapeName": "R_outterBall_CTLShape", "degree": 1, "form": 0, "points": [[-17.316787, 1.453949, 5.358633], [-17.311455, 0.418736, 4.365027], [-18.325959, 1.433153, 4.338786], [-17.316787, 1.453949, 5.358633], [-16.296728, 1.433153, 4.349675], [-17.311455, 0.418736, 4.365027], [-17.3059, 1.412357, 3.329828], [-16.296728, 1.433153, 4.349675], [-17.311232, 2.44757, 4.323434], [-17.316787, 1.453949, 5.358633], [-18.325959, 1.433153, 4.338786], [-17.3059, 1.412357, 3.329828], [-17.311232, 2.44757, 4.323434], [-18.325959, 1.433153, 4.338786]]}]},
			"L_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[75.258682, 104.3023, -15.715667], [75.249903, 104.412046, -15.60557], [75.258682, 104.3023, -15.495472], [75.267462, 104.192553, -15.60557], [75.258682, 104.3023, -15.715667], [75.368419, 104.311078, -15.60557], [75.258682, 104.3023, -15.495472], [75.148935, 104.29352, -15.60557], [75.249903, 104.412046, -15.60557], [75.368419, 104.311078, -15.60557], [75.267462, 104.192553, -15.60557], [75.148935, 104.29352, -15.60557], [75.258682, 104.3023, -15.715667], [75.368419, 104.311078, -15.60557], [64.905288, 103.474028, -15.60557]]}, {"shapeName": "L_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[64.077016, 113.827423, -15.715667], [63.967269, 113.818643, -15.60557], [64.077016, 113.827423, -15.495472], [64.186763, 113.836202, -15.60557], [64.077016, 113.827423, -15.715667], [64.068237, 113.937159, -15.60557], [64.077016, 113.827423, -15.495472], [64.085796, 113.717676, -15.60557], [63.967269, 113.818643, -15.60557], [64.068237, 113.937159, -15.60557], [64.186763, 113.836202, -15.60557], [64.085796, 113.717676, -15.60557], [64.077016, 113.827423, -15.715667], [64.068237, 113.937159, -15.60557], [64.905288, 103.474028, -15.60557]]}, {"shapeName": "L_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[64.896508, 103.583775, -5.219097], [64.795541, 103.465248, -5.219097], [64.914067, 103.364281, -5.219097], [65.015035, 103.482808, -5.219097], [64.896508, 103.583775, -5.219097], [64.905288, 103.474028, -5.10901], [64.914067, 103.364281, -5.219097], [64.905288, 103.474028, -5.329195], [64.795541, 103.465248, -5.219097], [64.905288, 103.474028, -5.10901], [65.015035, 103.482808, -5.219097], [64.905288, 103.474028, -5.329195], [64.896508, 103.583775, -5.219097], [64.905288, 103.474028, -5.10901], [64.905288, 103.474028, -15.60557]]}]},
			"L_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.125625, 95.29961, -3.115401], [67.133727, 95.407395, -3.003331], [67.010855, 95.343062, -2.932574], [67.002753, 95.235276, -3.044644], [67.125625, 95.29961, -3.115401], [67.135613, 95.256202, -2.966214], [67.010855, 95.343062, -2.932574], [67.000862, 95.386476, -3.081766], [67.133727, 95.407395, -3.003331], [67.135613, 95.256202, -2.966214], [67.002753, 95.235276, -3.044644], [67.000862, 95.386476, -3.081766], [67.125625, 95.29961, -3.115401], [67.135613, 95.256202, -2.966214], [60.711838, 101.466573, -8.47477]]}, {"shapeName": "L_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[66.947201, 109.563591, -6.617491], [66.822437, 109.650457, -6.583857], [66.832431, 109.607043, -6.434665], [66.957194, 109.520177, -6.468299], [66.947201, 109.563591, -6.617491], [66.955297, 109.671368, -6.505424], [66.832431, 109.607043, -6.434665], [66.824329, 109.499257, -6.546734], [66.822437, 109.650457, -6.583857], [66.955297, 109.671368, -6.505424], [66.957194, 109.520177, -6.468299], [66.824329, 109.499257, -6.546734], [66.947201, 109.563591, -6.617491], [66.955297, 109.671368, -6.505424], [60.711838, 101.466573, -8.47477]]}, {"shapeName": "L_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[55.36368, 103.602235, 0.169714], [55.230814, 103.581315, 0.091279], [55.232706, 103.430116, 0.128401], [55.365571, 103.451035, 0.206836], [55.36368, 103.602235, 0.169714], [55.240813, 103.537899, 0.240462], [55.232706, 103.430116, 0.128401], [55.355578, 103.494449, 0.057644], [55.230814, 103.581315, 0.091279], [55.240813, 103.537899, 0.240462], [55.365571, 103.451035, 0.206836], [55.355578, 103.494449, 0.057644], [55.36368, 103.602235, 0.169714], [55.240813, 103.537899, 0.240462], [60.711838, 101.466573, -8.47477]]}]},
			"R_shoulder_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-13.145654, 145.77658, -6.485353], [-13.207321, 145.886392, -6.393804], [-13.255241, 145.77658, -6.294365], [-13.193573, 145.666768, -6.385915], [-13.145654, 145.77658, -6.485353], [-13.295685, 145.768656, -6.444506], [-13.255241, 145.77658, -6.294365], [-13.105201, 145.784505, -6.335208], [-13.207321, 145.886392, -6.393804], [-13.295685, 145.768656, -6.444506], [-13.193573, 145.666768, -6.385915], [-13.105201, 145.784505, -6.335208], [-13.145654, 145.77658, -6.485353], [-13.295685, 145.768656, -6.444506], [-4.215017, 146.524231, -1.234097]]}, {"shapeName": "R_shoulder_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-4.808705, 156.88376, -1.701684], [-4.768253, 156.891685, -1.551539], [-4.918293, 156.88376, -1.510696], [-4.958745, 156.875834, -1.660842], [-4.808705, 156.88376, -1.701684], [-4.870372, 156.993561, -1.610134], [-4.918293, 156.88376, -1.510696], [-4.856625, 156.773948, -1.602246], [-4.768253, 156.891685, -1.551539], [-4.870372, 156.993561, -1.610134], [-4.958745, 156.875834, -1.660842], [-4.856625, 156.773948, -1.602246], [-4.808705, 156.88376, -1.701684], [-4.870372, 156.993561, -1.610134], [-4.215017, 146.524231, -1.234097]]}, {"shapeName": "R_shoulder_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.391063, 146.634043, 7.770759], [-9.288943, 146.532156, 7.829354], [-9.377315, 146.414419, 7.778647], [-9.479435, 146.516306, 7.720051], [-9.391063, 146.634043, 7.770759], [-9.438978, 146.524231, 7.870188], [-9.377315, 146.414419, 7.778647], [-9.329395, 146.524231, 7.679209], [-9.288943, 146.532156, 7.829354], [-9.438978, 146.524231, 7.870188], [-9.479435, 146.516306, 7.720051], [-9.329395, 146.524231, 7.679209], [-9.391063, 146.634043, 7.770759], [-9.438978, 146.524231, 7.870188], [-4.215017, 146.524231, -1.234097]]}]},
			"C_torso_FK_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_B_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 106.468071, -14.721745], [-0.0, 106.701038, -14.768085], [-0.0, 106.898538, -14.900056], [-0.0, 107.030509, -15.097556], [-0.0, 107.076849, -15.330523], [-0.0, 107.030509, -15.56349], [-0.0, 106.898538, -15.76099], [-0.0, 106.701038, -15.892961], [-0.0, 106.468071, -15.939301], [-0.0, 106.235104, -15.892961], [-0.0, 106.037604, -15.76099], [-0.0, 105.905633, -15.56349], [-0.0, 105.859293, -15.330523], [-0.0, 105.905633, -15.097556], [-0.0, 106.037604, -14.900056], [-0.0, 106.235104, -14.768085], [-0.0, 106.468071, -14.721745], [-0.0, 106.468071, -8.633965]]}]},
			"R_legBase_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 88.785288, -4.941845], [-9.978517, 85.175938, -4.352223], [-9.978517, 83.797286, -4.127007], [-9.978517, 86.562223, 4.133872], [-9.978517, 91.028345, 8.788951], [-9.978517, 95.489768, 8.060134], [-9.978517, 98.242345, 2.225812], [-9.978517, 98.234711, -6.485499], [-9.978517, 96.856059, -6.260283], [-9.978517, 93.24671, -5.670661], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253]]}]},
			"L_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[71.172479, 92.001141, -5.596023], [71.217565, 92.098141, -5.48288], [71.115446, 92.032153, -5.385615], [71.070361, 91.935154, -5.498758], [71.172479, 92.001141, -5.596023], [71.220709, 91.944267, -5.459348], [71.115446, 92.032153, -5.385615], [71.06721, 92.089034, -5.522293], [71.217565, 92.098141, -5.48288], [71.220709, 91.944267, -5.459348], [71.070361, 91.935154, -5.498758], [71.06721, 92.089034, -5.522293], [71.172479, 92.001141, -5.596023], [71.220709, 91.944267, -5.459348], [63.903151, 98.845501, -8.460031]]}, {"shapeName": "L_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[70.875168, 106.518017, -7.816282], [70.769898, 106.605909, -7.742552], [70.818135, 106.549029, -7.605874], [70.923405, 106.461137, -7.679604], [70.875168, 106.518017, -7.816282], [70.920247, 106.615009, -7.70314], [70.818135, 106.549029, -7.605874], [70.77305, 106.452029, -7.719017], [70.769898, 106.605909, -7.742552], [70.920247, 106.615009, -7.70314], [70.923405, 106.461137, -7.679604], [70.77305, 106.452029, -7.719017], [70.875168, 106.518017, -7.816282], [70.920247, 106.615009, -7.70314], [63.903151, 98.845501, -8.460031]]}, {"shapeName": "L_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.286537, 100.38983, 1.472708], [61.136182, 100.380722, 1.433295], [61.139333, 100.226842, 1.45683], [61.289688, 100.23595, 1.496243], [61.286537, 100.38983, 1.472708], [61.184421, 100.323841, 1.569963], [61.139333, 100.226842, 1.45683], [61.241451, 100.29283, 1.359565], [61.136182, 100.380722, 1.433295], [61.184421, 100.323841, 1.569963], [61.289688, 100.23595, 1.496243], [61.241451, 100.29283, 1.359565], [61.286537, 100.38983, 1.472708], [61.184421, 100.323841, 1.569963], [63.903151, 98.845501, -8.460031]]}]},
			"R_wrist_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_wrist_FK_CTLShape", "degree": 3, "form": 2, "points": [[-59.254016, 98.33514, -14.54661], [-62.405316, 101.224514, -15.03235], [-64.30532, 104.113889, -12.47176], [-63.841025, 105.310705, -8.364793], [-61.284417, 104.113889, -5.117254], [-58.133117, 101.224514, -4.631514], [-56.233113, 98.33514, -7.192104], [-56.697407, 97.138324, -11.299072]]}]},
			"R_heel_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_heel_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.566493, 0.992592, -10.501591], [0.567095, 1.100409, -10.61392], [0.567674, 0.988078, -10.721736], [0.567071, 0.88026, -10.609406], [0.566493, 0.992592, -10.501591], [0.677169, 0.990335, -10.611073], [0.567674, 0.988078, -10.721736], [0.456988, 0.990335, -10.612254], [0.567095, 1.100409, -10.61392], [0.677169, 0.990335, -10.611073], [0.567071, 0.88026, -10.609406], [0.456988, 0.990335, -10.612254], [0.566493, 0.992592, -10.501591], [0.677169, 0.990335, -10.611073], [-9.81924, 0.990336, -10.6674]]}, {"shapeName": "R_heel_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-9.818689, 11.376883, -10.770211], [-9.928194, 11.374625, -10.880874], [-9.817507, 11.372369, -10.990356], [-9.708002, 11.374625, -10.879693], [-9.818689, 11.376883, -10.770211], [-9.818085, 11.484689, -10.882539], [-9.817507, 11.372369, -10.990356], [-9.81811, 11.264551, -10.878027], [-9.928194, 11.374625, -10.880874], [-9.818085, 11.484689, -10.882539], [-9.708002, 11.374625, -10.879693], [-9.81811, 11.264551, -10.878027], [-9.818689, 11.376883, -10.770211], [-9.818085, 11.484689, -10.882539], [-9.81924, 0.990336, -10.6674]]}, {"shapeName": "R_heel_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.763502, 0.887523, -21.053798], [-9.87361, 0.777449, -21.052132], [-9.763527, 0.667374, -21.049284], [-9.653418, 0.777449, -21.050951], [-9.763502, 0.887523, -21.053798], [-9.762924, 0.775192, -21.161604], [-9.763527, 0.667374, -21.049284], [-9.764105, 0.779705, -20.941469], [-9.87361, 0.777449, -21.052132], [-9.762924, 0.775192, -21.161604], [-9.653418, 0.777449, -21.050951], [-9.764105, 0.779705, -20.941469], [-9.763502, 0.887523, -21.053798], [-9.762924, 0.775192, -21.161604], [-9.81924, 0.990336, -10.6674]]}]},
			"R_toeTip_CTL": {"color": 20, "shapes": [{"shapeName": "R_toeTip_CTLShape", "degree": 1, "form": 0, "points": [[-9.969646, 1.564909, 17.359174], [-9.964314, 0.529695, 16.365568], [-10.978817, 1.544112, 16.339327], [-9.969646, 1.564909, 17.359174], [-8.949587, 1.544112, 16.350217], [-9.964314, 0.529695, 16.365568], [-9.958758, 1.523316, 15.33037], [-8.949587, 1.544112, 16.350217], [-9.964091, 2.558529, 16.323976], [-9.969646, 1.564909, 17.359174], [-10.978817, 1.544112, 16.339327], [-9.958758, 1.523316, 15.33037], [-9.964091, 2.558529, 16.323976], [-10.978817, 1.544112, 16.339327]]}]},
			"L_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[58.062821, 93.615439, 3.304504], [57.925948, 93.673269, 3.351028], [57.851821, 93.561863, 3.271422], [57.988694, 93.504034, 3.224898], [58.062821, 93.615439, 3.304504], [57.959952, 93.523513, 3.376672], [57.851821, 93.561863, 3.271422], [57.954689, 93.653796, 3.199246], [57.925948, 93.673269, 3.351028], [57.959952, 93.523513, 3.376672], [57.988694, 93.504034, 3.224898], [57.954689, 93.653796, 3.199246], [58.062821, 93.615439, 3.304504], [57.959952, 93.523513, 3.376672], [57.709054, 99.734313, -5.081507]]}, {"shapeName": "L_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[54.854856, 107.743781, 0.884473], [54.746725, 107.782138, 0.779215], [54.643856, 107.690205, 0.851391], [54.751988, 107.651849, 0.956649], [54.854856, 107.743781, 0.884473], [54.717986, 107.801602, 0.930991], [54.643856, 107.690205, 0.851391], [54.780729, 107.632376, 0.804867], [54.746725, 107.782138, 0.779215], [54.717986, 107.801602, 0.930991], [54.751988, 107.651849, 0.956649], [54.780729, 107.632376, 0.804867], [54.854856, 107.743781, 0.884473], [54.717986, 107.801602, 0.930991], [57.709054, 99.734313, -5.081507]]}, {"shapeName": "L_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[47.724925, 97.291782, -6.578882], [47.753666, 97.27231, -6.730664], [47.787671, 97.122548, -6.705012], [47.758929, 97.142021, -6.55323], [47.724925, 97.291782, -6.578882], [47.650807, 97.18038, -6.658486], [47.787671, 97.122548, -6.705012], [47.861798, 97.233953, -6.625406], [47.753666, 97.27231, -6.730664], [47.650807, 97.18038, -6.658486], [47.758929, 97.142021, -6.55323], [47.861798, 97.233953, -6.625406], [47.724925, 97.291782, -6.578882], [47.650807, 97.18038, -6.658486], [57.709054, 99.734313, -5.081507]]}]},
			"C_hip_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[5.152094, 98.139605, -12.927377], [-0.0, 95.948004, -14.705762], [-5.152094, 98.139605, -12.927377], [-7.286156, 100.331205, -8.633965], [-5.152094, 98.139605, -4.340554], [-0.0, 95.948004, -2.562169], [5.152094, 98.139605, -4.340554], [7.286156, 100.331205, -8.633965]]}]},
			"C_head_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[9.540915, 173.716683, -4.888731], [0.0, 177.668513, -4.855724], [-9.540915, 173.716683, -4.888731], [-13.492882, 164.176102, -4.968417], [-9.540915, 154.63552, -5.048103], [0.0, 150.68369, -5.08111], [9.540915, 154.63552, -5.048103], [13.492882, 164.176102, -4.968417]]}]},
			"R_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_A_CTLShape", "degree": 3, "form": 2, "points": [[-60.624074, 100.299004, -9.688746], [-61.590934, 101.133747, -9.875152], [-62.042832, 102.163455, -9.241234], [-61.71505, 102.784937, -8.158331], [-60.799601, 102.634141, -7.260793], [-59.832742, 101.799398, -7.074387], [-59.380844, 100.769691, -7.708305], [-59.708625, 100.148208, -8.791208]]}]},
			"R_arm_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-63.822242, 107.418201, -8.372508], [-63.63755, 107.20691, -8.448371], [-63.402019, 107.37178, -8.545117], [-63.213232, 107.280423, -8.622662], [-63.170118, 106.980669, -8.640371], [-62.901317, 106.972449, -8.750783], [-62.842612, 107.269064, -8.774896], [-62.649355, 107.348784, -8.854277], [-62.422804, 107.169764, -8.947334], [-62.227353, 107.369437, -9.027617], [-62.379876, 107.624083, -8.964967], [-62.295347, 107.828149, -8.999688], [-62.018078, 107.874765, -9.113578], [-62.010475, 108.165358, -9.116701], [-62.284869, 108.228837, -9.003992], [-62.358568, 108.437767, -8.97372], [-62.192993, 108.682666, -9.041731], [-62.377686, 108.893957, -8.965867], [-62.613234, 108.729107, -8.869114], [-62.80202, 108.820464, -8.791569], [-62.845134, 109.120218, -8.77386], [-63.113924, 109.128424, -8.663453], [-63.172659, 108.831804, -8.639327], [-63.365898, 108.752103, -8.559954], [-63.592431, 108.931103, -8.466904], [-63.787882, 108.73143, -8.386621], [-63.635377, 108.476804, -8.449264], [-63.719924, 108.272719, -8.414536], [-63.997163, 108.226109, -8.300658], [-64.004778, 107.935529, -8.29753], [-63.730383, 107.87205, -8.410239], [-63.656684, 107.66312, -8.440512], [-63.822242, 107.418201, -8.372508]]}, {"shapeName": "R_arm_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-63.420244, 108.063048, -8.537631], [-63.291137, 108.374783, -8.590662], [-62.995943, 108.496513, -8.711914], [-62.70761, 108.356927, -8.830349], [-62.595009, 108.037839, -8.8766], [-62.724116, 107.726104, -8.823569], [-63.019309, 107.604374, -8.702317], [-63.307631, 107.743947, -8.583887]]}, {"shapeName": "R_arm_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-62.325078, 107.269601, -8.987476], [-58.56385, 102.966713, -10.53242]]}]},
			"L_ankleOffset_CTL": {"color": 20, "shapes": [{"shapeName": "L_ankleOffset_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 4.867005, -6.774814], [9.978517, 10.697845, -2.541692], [9.978517, 12.132748, -2.541109], [10.993147, 11.415005, -1.823949], [9.978517, 12.132165, -1.106206], [9.978517, 12.132748, -2.541109], [8.963887, 11.415005, -1.823949], [9.978517, 10.697845, -2.541692], [9.978517, 10.697262, -1.106789], [8.963887, 11.415005, -1.823949], [9.978517, 12.132165, -1.106206], [9.978517, 10.697262, -1.106789], [10.993147, 11.415005, -1.823949], [9.978517, 10.697845, -2.541692]]}]},
			"L_legEnd_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_legEnd_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, -2.809889, -7.255449], [9.868419, -2.793006, -7.364244], [9.978517, -2.776123, -7.47304], [10.088614, -2.793006, -7.364244], [9.978517, -2.809889, -7.255449], [9.978517, -2.901791, -7.381126], [9.978517, -2.776123, -7.47304], [9.978517, -2.68421, -7.347362], [9.868419, -2.793006, -7.364244], [9.978517, -2.901791, -7.381126], [10.088614, -2.793006, -7.364244], [9.978517, -2.68421, -7.347362], [9.978517, -2.809889, -7.255449], [9.978517, -2.901791, -7.381126], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_legEnd_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.407956, 7.453741, -5.662741], [-0.407956, 7.579419, -5.754654], [-0.407956, 7.487507, -5.880332], [-0.407956, 7.361829, -5.788419], [-0.407956, 7.453741, -5.662741], [-0.518043, 7.470624, -5.771536], [-0.407956, 7.487507, -5.880332], [-0.297859, 7.470624, -5.771536], [-0.407956, 7.579419, -5.754654], [-0.518043, 7.470624, -5.771536], [-0.407956, 7.361829, -5.788419], [-0.297859, 7.470624, -5.771536], [-0.407956, 7.453741, -5.662741], [-0.518043, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_legEnd_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.868419, 9.063332, -16.035166], [9.978517, 9.172127, -16.018283], [10.088614, 9.063332, -16.035166], [9.978517, 8.954537, -16.052049], [9.868419, 9.063332, -16.035166], [9.978517, 9.080213, -16.143951], [10.088614, 9.063332, -16.035166], [9.978517, 9.046449, -15.926371], [9.978517, 9.172127, -16.018283], [9.978517, 9.080213, -16.143951], [9.978517, 8.954537, -16.052049], [9.978517, 9.046449, -15.926371], [9.868419, 9.063332, -16.035166], [9.978517, 9.080213, -16.143951], [9.978517, 7.470624, -5.771536]]}]},
			"R_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_B_CTLShape", "degree": 3, "form": 2, "points": [[-62.935737, 98.066385, -7.706969], [-63.940073, 98.862649, -7.860704], [-64.429447, 99.853877, -7.194114], [-64.117189, 100.459421, -6.097678], [-63.186217, 100.324563, -5.213673], [-62.181881, 99.528299, -5.059939], [-61.692507, 98.537072, -5.726528], [-62.004765, 97.931528, -6.822964]]}]},
			"R_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-71.89867, 91.671065, -9.155381], [-71.959024, 91.763469, -9.045556], [-71.871496, 91.692743, -8.937948], [-71.811141, 91.600339, -9.047773], [-71.89867, 91.671065, -9.155381], [-71.965509, 91.60876, -9.029321], [-71.871496, 91.692743, -8.937948], [-71.80465, 91.755055, -9.06401], [-71.959024, 91.763469, -9.045556], [-71.965509, 91.60876, -9.029321], [-71.811141, 91.600339, -9.047773], [-71.80465, 91.755055, -9.06401], [-71.89867, 91.671065, -9.155381], [-71.965509, 91.60876, -9.029321], [-64.2971, 98.5829, -10.683]]}, {"shapeName": "R_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-71.286247, 106.266827, -10.68714], [-71.192227, 106.350818, -10.595769], [-71.259074, 106.288506, -10.469707], [-71.353094, 106.204516, -10.561078], [-71.286247, 106.266827, -10.68714], [-71.346595, 106.359224, -10.577315], [-71.259074, 106.288506, -10.469707], [-71.198719, 106.196101, -10.579532], [-71.192227, 106.350818, -10.595769], [-71.346595, 106.359224, -10.577315], [-71.353094, 106.204516, -10.561078], [-71.198719, 106.196101, -10.579532], [-71.286247, 106.266827, -10.68714], [-71.346595, 106.359224, -10.577315], [-64.2971, 98.5829, -10.683]]}, {"shapeName": "R_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-63.089288, 99.687029, -0.42566], [-62.934913, 99.678615, -0.444114], [-62.941405, 99.523899, -0.427877], [-63.09578, 99.532313, -0.409423], [-63.089288, 99.687029, -0.42566], [-63.001761, 99.616302, -0.318062], [-62.941405, 99.523899, -0.427877], [-63.028933, 99.594625, -0.535485], [-62.934913, 99.678615, -0.444114], [-63.001761, 99.616302, -0.318062], [-63.09578, 99.532313, -0.409423], [-63.028933, 99.594625, -0.535485], [-63.089288, 99.687029, -0.42566], [-63.001761, 99.616302, -0.318062], [-64.2971, 98.5829, -10.683]]}]},
			"L_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[71.395787, 104.339428, -15.715667], [71.381236, 104.44856, -15.60557], [71.395787, 104.339428, -15.495472], [71.410338, 104.230296, -15.60557], [71.395787, 104.339428, -15.715667], [71.504908, 104.353977, -15.60557], [71.395787, 104.339428, -15.495472], [71.286655, 104.324877, -15.60557], [71.381236, 104.44856, -15.60557], [71.504908, 104.353977, -15.60557], [71.410338, 104.230296, -15.60557], [71.286655, 104.324877, -15.60557], [71.395787, 104.339428, -15.715667], [71.504908, 104.353977, -15.60557], [61.100425, 102.966713, -15.60557]]}, {"shapeName": "L_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[59.72771, 113.262074, -15.715667], [59.618579, 113.247524, -15.60557], [59.72771, 113.262074, -15.495472], [59.836842, 113.276625, -15.60557], [59.72771, 113.262074, -15.715667], [59.713161, 113.371196, -15.60557], [59.72771, 113.262074, -15.495472], [59.742261, 113.152943, -15.60557], [59.618579, 113.247524, -15.60557], [59.713161, 113.371196, -15.60557], [59.836842, 113.276625, -15.60557], [59.742261, 113.152943, -15.60557], [59.72771, 113.262074, -15.715667], [59.713161, 113.371196, -15.60557], [61.100425, 102.966713, -15.60557]]}, {"shapeName": "L_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.085874, 103.075845, -5.219097], [60.991294, 102.952162, -5.219097], [61.114976, 102.857581, -5.219097], [61.209557, 102.981264, -5.219097], [61.085874, 103.075845, -5.219097], [61.100425, 102.966713, -5.10901], [61.114976, 102.857581, -5.219097], [61.100425, 102.966713, -5.329195], [60.991294, 102.952162, -5.219097], [61.100425, 102.966713, -5.10901], [61.209557, 102.981264, -5.219097], [61.100425, 102.966713, -5.329195], [61.085874, 103.075845, -5.219097], [61.100425, 102.966713, -5.10901], [61.100425, 102.966713, -15.60557]]}]},
			"C_neck_FK_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_B_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 158.288242, -16.958557], [0.0, 158.683522, -16.936671], [0.0, 159.05709, -17.067727], [0.0, 159.35208, -17.331754], [0.0, 159.523567, -17.68857], [0.0, 159.545453, -18.08385], [0.0, 159.414396, -18.457418], [0.0, 159.15037, -18.752408], [0.0, 158.793554, -18.923895], [0.0, 158.398274, -18.945781], [0.0, 158.024705, -18.814724], [0.0, 157.729716, -18.550698], [0.0, 157.558229, -18.193882], [0.0, 157.536343, -17.798602], [0.0, 157.667399, -17.425033], [0.0, 157.931426, -17.130044], [0.0, 158.288242, -16.958557], [0.0, 155.761683, -7.131864]]}]},
			"R_leg_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-9.97852, -2.915853, -5.661442], [-9.868422, -2.915853, -5.77154], [-9.97852, -2.915853, -5.881637], [-10.088617, -2.915853, -5.77154], [-9.97852, -2.915853, -5.661442], [-9.97852, -3.02594, -5.77154], [-9.97852, -2.915853, -5.881637], [-9.97852, -2.805755, -5.77154], [-9.868422, -2.915853, -5.77154], [-9.97852, -3.02594, -5.77154], [-10.088617, -2.915853, -5.77154], [-9.97852, -2.805755, -5.77154], [-9.97852, -2.915853, -5.661442], [-9.97852, -3.02594, -5.77154], [-9.97852, 7.47062, -5.77154]]}, {"shapeName": "R_leg_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.407953, 7.47062, -5.661442], [0.407953, 7.580718, -5.77154], [0.407953, 7.47062, -5.881637], [0.407953, 7.360523, -5.77154], [0.407953, 7.47062, -5.661442], [0.51804, 7.47062, -5.77154], [0.407953, 7.47062, -5.881637], [0.297856, 7.47062, -5.77154], [0.407953, 7.580718, -5.77154], [0.51804, 7.47062, -5.77154], [0.407953, 7.360523, -5.77154], [0.297856, 7.47062, -5.77154], [0.407953, 7.47062, -5.661442], [0.51804, 7.47062, -5.77154], [-9.97852, 7.47062, -5.77154]]}, {"shapeName": "R_leg_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.868422, 7.47062, -16.158012], [-9.97852, 7.580718, -16.158012], [-10.088617, 7.47062, -16.158012], [-9.97852, 7.360523, -16.158012], [-9.868422, 7.47062, -16.158012], [-9.97852, 7.47062, -16.2681], [-10.088617, 7.47062, -16.158012], [-9.97852, 7.47062, -16.047915], [-9.97852, 7.580718, -16.158012], [-9.97852, 7.47062, -16.2681], [-9.97852, 7.360523, -16.158012], [-9.97852, 7.47062, -16.047915], [-9.868422, 7.47062, -16.158012], [-9.97852, 7.47062, -16.2681], [-9.97852, 7.47062, -5.77154]]}]},
			"R_upLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_upLeg_FK_CTLShape", "degree": 3, "form": 2, "points": [[-13.953898, 91.65692, -1.382878], [-9.978517, 91.922398, 0.242234], [-6.003136, 91.65692, -1.382878], [-4.356482, 91.015999, -5.306253], [-6.003136, 90.375078, -9.229628], [-9.978517, 90.1096, -10.85474], [-13.953898, 90.375078, -9.229628], [-15.600551, 91.015999, -5.306253]]}]},
			"L_leg_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, -2.809889, -7.255449], [9.868419, -2.793006, -7.364244], [9.978517, -2.776123, -7.47304], [10.088614, -2.793006, -7.364244], [9.978517, -2.809889, -7.255449], [9.978517, -2.901791, -7.381126], [9.978517, -2.776123, -7.47304], [9.978517, -2.68421, -7.347362], [9.868419, -2.793006, -7.364244], [9.978517, -2.901791, -7.381126], [10.088614, -2.793006, -7.364244], [9.978517, -2.68421, -7.347362], [9.978517, -2.809889, -7.255449], [9.978517, -2.901791, -7.381126], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_leg_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.407956, 7.453741, -5.662741], [-0.407956, 7.579419, -5.754654], [-0.407956, 7.487507, -5.880332], [-0.407956, 7.361829, -5.788419], [-0.407956, 7.453741, -5.662741], [-0.518043, 7.470624, -5.771536], [-0.407956, 7.487507, -5.880332], [-0.297859, 7.470624, -5.771536], [-0.407956, 7.579419, -5.754654], [-0.518043, 7.470624, -5.771536], [-0.407956, 7.361829, -5.788419], [-0.297859, 7.470624, -5.771536], [-0.407956, 7.453741, -5.662741], [-0.518043, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_leg_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.868419, 9.063332, -16.035166], [9.978517, 9.172127, -16.018283], [10.088614, 9.063332, -16.035166], [9.978517, 8.954537, -16.052049], [9.868419, 9.063332, -16.035166], [9.978517, 9.080213, -16.143951], [10.088614, 9.063332, -16.035166], [9.978517, 9.046449, -15.926371], [9.978517, 9.172127, -16.018283], [9.978517, 9.080213, -16.143951], [9.978517, 8.954537, -16.052049], [9.978517, 9.046449, -15.926371], [9.868419, 9.063332, -16.035166], [9.978517, 9.080213, -16.143951], [9.978517, 7.470624, -5.771536]]}]},
			"C_jaw_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_jaw_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.110097, 158.716896, 3.814574], [0.0, 158.79873, 3.888225], [-0.110097, 158.716896, 3.814574], [0.0, 158.635061, 3.740922], [0.110097, 158.716896, 3.814574], [0.0, 158.643251, 3.896401], [-0.110097, 158.716896, 3.814574], [0.0, 158.790547, 3.732739], [0.0, 158.79873, 3.888225], [0.0, 158.643251, 3.896401], [0.0, 158.635061, 3.740922], [0.0, 158.790547, 3.732739], [0.110097, 158.716896, 3.814574], [0.0, 158.643251, 3.896401], [0.0, 165.665077, -3.905633]]}, {"shapeName": "C_jaw_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.110097, 173.385283, 3.042548], [-0.0, 173.458935, 2.960713], [-0.110097, 173.385283, 3.042548], [-0.0, 173.311632, 3.124383], [0.110097, 173.385283, 3.042548], [-0.0, 173.467111, 3.116192], [-0.110097, 173.385283, 3.042548], [-0.0, 173.303449, 2.968896], [-0.0, 173.458935, 2.960713], [-0.0, 173.467111, 3.116192], [-0.0, 173.311632, 3.124383], [-0.0, 173.303449, 2.968896], [0.110097, 173.385283, 3.042548], [-0.0, 173.467111, 3.116192], [0.0, 165.665077, -3.905633]]}, {"shapeName": "C_jaw_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-10.386473, 165.746911, -3.831982], [-10.386473, 165.738728, -3.987468], [-10.386473, 165.583242, -3.979285], [-10.386473, 165.591425, -3.823798], [-10.386473, 165.746911, -3.831982], [-10.49656, 165.665077, -3.905633], [-10.386473, 165.583242, -3.979285], [-10.276375, 165.665077, -3.905633], [-10.386473, 165.738728, -3.987468], [-10.49656, 165.665077, -3.905633], [-10.386473, 165.591425, -3.823798], [-10.276375, 165.665077, -3.905633], [-10.386473, 165.746911, -3.831982], [-10.49656, 165.665077, -3.905633], [0.0, 165.665077, -3.905633]]}]},
			"R_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_B_CTLShape", "degree": 3, "form": 2, "points": [[-63.643354, 97.581914, -11.872647], [-64.505276, 98.416822, -12.348441], [-65.245275, 99.348999, -11.848632], [-65.429867, 99.832388, -10.665998], [-64.950923, 99.583828, -9.493313], [-64.089, 98.74892, -9.017519], [-63.349002, 97.816743, -9.517328], [-63.16441, 97.333354, -10.699962]]}]},
			"R_leg_PV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_PV_CTLShape", "degree": 1, "form": 0, "points": [[-8.963887, 52.226244, 103.57992], [-8.963887, 50.196984, 103.57992], [-8.963887, 50.196984, 101.550661], [-8.963887, 52.226244, 101.550661], [-10.993147, 52.226244, 101.550661], [-10.993147, 50.196984, 101.550661], [-10.993147, 50.196984, 103.57992], [-10.993147, 52.226244, 103.57992], [-8.963887, 52.226244, 103.57992], [-8.963887, 52.226244, 101.550661], [-8.963887, 50.196984, 101.550661], [-10.993147, 50.196984, 101.550661], [-10.993147, 52.226244, 101.550661], [-10.993147, 52.226244, 103.57992], [-10.993147, 50.196984, 103.57992], [-8.963887, 50.196984, 103.57992]]}]},
			"R_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_C_CTLShape", "degree": 3, "form": 2, "points": [[-66.303599, 95.18302, -11.301014], [-67.293852, 95.880712, -11.747089], [-68.162182, 96.675675, -11.217561], [-68.399931, 97.102227, -10.022618], [-67.86783, 96.910504, -8.862242], [-66.877577, 96.212811, -8.416167], [-66.009247, 95.417849, -8.945695], [-65.771498, 94.991296, -10.140638]]}]},
			"C_head_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.386473, 164.177021, -5.078511], [10.386473, 164.286195, -4.967498], [10.386473, 164.175182, -4.858324], [10.386473, 164.066008, -4.969337], [10.386473, 164.177021, -5.078511], [10.49656, 164.176102, -4.968417], [10.386473, 164.175182, -4.858324], [10.276375, 164.176102, -4.968417], [10.386473, 164.286195, -4.967498], [10.49656, 164.176102, -4.968417], [10.386473, 164.066008, -4.969337], [10.276375, 164.176102, -4.968417], [10.386473, 164.177021, -5.078511], [10.49656, 164.176102, -4.968417], [0.0, 164.176102, -4.968417]]}, {"shapeName": "C_head_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 174.563132, -4.991763], [-0.110097, 174.562212, -4.881669], [0.0, 174.561293, -4.771575], [0.110097, 174.562212, -4.881669], [0.0, 174.563132, -4.991763], [0.0, 174.672296, -4.88075], [0.0, 174.561293, -4.771575], [0.0, 174.452118, -4.882589], [-0.110097, 174.562212, -4.881669], [0.0, 174.672296, -4.88075], [0.110097, 174.562212, -4.881669], [0.0, 174.452118, -4.882589], [0.0, 174.563132, -4.991763], [0.0, 174.672296, -4.88075], [0.0, 164.176102, -4.968417]]}, {"shapeName": "C_head_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 164.199447, 5.418613], [-0.110097, 164.089354, 5.417693], [0.0, 163.97926, 5.416774], [0.110097, 164.089354, 5.417693], [0.0, 164.199447, 5.418613], [0.0, 164.088434, 5.527777], [0.0, 163.97926, 5.416774], [0.0, 164.090273, 5.3076], [-0.110097, 164.089354, 5.417693], [0.0, 164.088434, 5.527777], [0.110097, 164.089354, 5.417693], [0.0, 164.090273, 5.3076], [0.0, 164.199447, 5.418613], [0.0, 164.088434, 5.527777], [0.0, 164.176102, -4.968417]]}]},
			"R_legEnd_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_legEnd_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-9.978517, -2.809889, -7.255449], [-9.868419, -2.793006, -7.364244], [-9.978517, -2.776123, -7.47304], [-10.088614, -2.793006, -7.364244], [-9.978517, -2.809889, -7.255449], [-9.978517, -2.901791, -7.381126], [-9.978517, -2.776123, -7.47304], [-9.978517, -2.68421, -7.347362], [-9.868419, -2.793006, -7.364244], [-9.978517, -2.901791, -7.381126], [-10.088614, -2.793006, -7.364244], [-9.978517, -2.68421, -7.347362], [-9.978517, -2.809889, -7.255449], [-9.978517, -2.901791, -7.381126], [-9.978517, 7.470624, -5.771536]]}, {"shapeName": "R_legEnd_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.407956, 7.453741, -5.662741], [0.407956, 7.579419, -5.754654], [0.407956, 7.487507, -5.880332], [0.407956, 7.361829, -5.788419], [0.407956, 7.453741, -5.662741], [0.518043, 7.470624, -5.771536], [0.407956, 7.487507, -5.880332], [0.297859, 7.470624, -5.771536], [0.407956, 7.579419, -5.754654], [0.518043, 7.470624, -5.771536], [0.407956, 7.361829, -5.788419], [0.297859, 7.470624, -5.771536], [0.407956, 7.453741, -5.662741], [0.518043, 7.470624, -5.771536], [-9.978517, 7.470624, -5.771536]]}, {"shapeName": "R_legEnd_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.868419, 9.063332, -16.035166], [-9.978517, 9.172127, -16.018283], [-10.088614, 9.063332, -16.035166], [-9.978517, 8.954537, -16.052049], [-9.868419, 9.063332, -16.035166], [-9.978517, 9.080213, -16.143951], [-10.088614, 9.063332, -16.035166], [-9.978517, 9.046449, -15.926371], [-9.978517, 9.172127, -16.018283], [-9.978517, 9.080213, -16.143951], [-9.978517, 8.954537, -16.052049], [-9.978517, 9.046449, -15.926371], [-9.868419, 9.063332, -16.035166], [-9.978517, 9.080213, -16.143951], [-9.978517, 7.470624, -5.771536]]}]},
			"R_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_C_CTLShape", "degree": 3, "form": 2, "points": [[-59.264565, 97.221524, -2.995155], [-59.406078, 98.143501, -2.102802], [-58.600855, 98.825087, -1.358882], [-57.320583, 98.867019, -1.199175], [-56.315228, 98.244734, -1.717233], [-56.173715, 97.322758, -2.609587], [-56.978938, 96.641171, -3.353506], [-58.25921, 96.599239, -3.513213]]}]},
			"C_cog_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[29.200713, 98.139605, -6.532542], [29.169913, 98.139605, -11.1264], [21.243069, 98.139605, -13.884719], [20.159804, 98.139605, -17.144535], [24.859035, 98.139605, -24.097637], [22.13394, 98.139605, -27.796036], [14.09848, 98.139605, -25.373178], [11.306819, 98.139605, -27.373817], [11.022086, 98.139605, -35.756106], [6.643531, 98.139605, -37.146428], [1.568748, 98.139605, -30.467802], [-1.864994, 98.139605, -30.445097], [-7.024957, 98.139605, -37.054848], [-11.38446, 98.139605, -35.605995], [-11.560197, 98.139605, -27.222655], [-14.324448, 98.139605, -25.185285], [-22.388692, 98.139605, -27.497774], [-25.063993, 98.139605, -23.76317], [-20.273534, 98.139605, -16.877248], [-21.31244, 98.139605, -13.603435], [-29.200713, 98.139605, -10.735389], [-29.169913, 98.139605, -6.141531], [-21.243069, 98.139605, -3.383212], [-20.159804, 98.139605, -0.123395], [-24.859035, 98.139605, 6.829706], [-22.13394, 98.139605, 10.528105], [-14.09848, 98.139605, 8.105247], [-11.306819, 98.139605, 10.105886], [-11.022086, 98.139605, 18.488175], [-6.643531, 98.139605, 19.878497], [-1.568748, 98.139605, 13.199871], [1.864994, 98.139605, 13.177166], [7.024957, 98.139605, 19.786917], [11.38446, 98.139605, 18.338064], [11.560197, 98.139605, 9.954724], [14.324448, 98.139605, 7.917354], [22.388692, 98.139605, 10.229843], [25.063993, 98.139605, 6.495239], [20.273534, 98.139605, -0.390683], [21.31244, 98.139605, -3.664496], [29.200713, 98.139605, -6.532542]]}]},
			"L_arm_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[65.588617, 95.83296, -7.765984], [65.616732, 95.912981, -7.635411], [65.504953, 95.83296, -7.562302], [65.476837, 95.75294, -7.692874], [65.588617, 95.83296, -7.765984], [65.620798, 95.757349, -7.633742], [65.504953, 95.83296, -7.562302], [65.472765, 95.908579, -7.694547], [65.616732, 95.912981, -7.635411], [65.620798, 95.757349, -7.633742], [65.476837, 95.75294, -7.692874], [65.472765, 95.908579, -7.694547], [65.588617, 95.83296, -7.765984], [65.620798, 95.757349, -7.633742], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_arm_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.204449, 110.515778, -7.923782], [65.088598, 110.591397, -7.852345], [65.120786, 110.515778, -7.720101], [65.236637, 110.44016, -7.791537], [65.204449, 110.515778, -7.923782], [65.232559, 110.595792, -7.793213], [65.120786, 110.515778, -7.720101], [65.09267, 110.435758, -7.850673], [65.088598, 110.591397, -7.852345], [65.232559, 110.595792, -7.793213], [65.236637, 110.44016, -7.791537], [65.09267, 110.435758, -7.850673], [65.204449, 110.515778, -7.923782], [65.232559, 110.595792, -7.793213], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_arm_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[54.687444, 103.046734, -0.896134], [54.543477, 103.042331, -0.95527], [54.547549, 102.886692, -0.953597], [54.691516, 102.891095, -0.894462], [54.687444, 103.046734, -0.896134], [54.575669, 102.966713, -0.823034], [54.547549, 102.886692, -0.953597], [54.659328, 102.966713, -1.026707], [54.543477, 103.042331, -0.95527], [54.575669, 102.966713, -0.823034], [54.691516, 102.891095, -0.894462], [54.659328, 102.966713, -1.026707], [54.687444, 103.046734, -0.896134], [54.575669, 102.966713, -0.823034], [58.56385, 102.966713, -10.53242]]}]},
			"R_shoulder_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-6.170406, 146.361529, -2.356082], [-9.334275, 146.098273, -4.171483], [-10.542769, 145.997718, -4.864906], [-5.054907, 146.098273, -11.62954], [0.75376, 146.361529, -14.423475], [4.664537, 146.686933, -12.179506], [5.183609, 146.950189, -5.754767], [2.112734, 147.050744, 2.396712], [0.904241, 146.950189, 1.703289], [-2.259629, 146.686933, -0.112112], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097]]}]},
			"C_torso_FK_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 112.699955, -8.700024], [-0.066058, 112.699955, -8.633965], [-0.0, 112.699955, -8.567907], [0.066058, 112.699955, -8.633965], [-0.0, 112.699955, -8.700024], [-0.0, 112.766007, -8.633965], [-0.0, 112.699955, -8.567907], [-0.0, 112.633896, -8.633965], [-0.066058, 112.699955, -8.633965], [-0.0, 112.766007, -8.633965], [0.066058, 112.699955, -8.633965], [-0.0, 112.633896, -8.633965], [-0.0, 112.699955, -8.700024], [-0.0, 112.766007, -8.633965], [-0.0, 106.468071, -8.633965]]}, {"shapeName": "C_torso_FK_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 106.468071, -8.700024], [-6.231884, 106.402012, -8.633965], [-6.231884, 106.468071, -8.567907], [-6.231884, 106.534129, -8.633965], [-6.231884, 106.468071, -8.700024], [-6.297936, 106.468071, -8.633965], [-6.231884, 106.468071, -8.567907], [-6.165825, 106.468071, -8.633965], [-6.231884, 106.402012, -8.633965], [-6.297936, 106.468071, -8.633965], [-6.231884, 106.534129, -8.633965], [-6.165825, 106.468071, -8.633965], [-6.231884, 106.468071, -8.700024], [-6.297936, 106.468071, -8.633965], [-0.0, 106.468071, -8.633965]]}, {"shapeName": "C_torso_FK_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 106.468071, -2.402082], [-0.0, 106.402012, -2.402082], [0.066058, 106.468071, -2.402082], [-0.0, 106.534129, -2.402082], [-0.066058, 106.468071, -2.402082], [-0.0, 106.468071, -2.336029], [0.066058, 106.468071, -2.402082], [-0.0, 106.468071, -2.46814], [-0.0, 106.402012, -2.402082], [-0.0, 106.468071, -2.336029], [-0.0, 106.534129, -2.402082], [-0.0, 106.468071, -2.46814], [-0.066058, 106.468071, -2.402082], [-0.0, 106.468071, -2.336029], [-0.0, 106.468071, -8.633965]]}]},
			"R_arm_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-62.069445, 105.934371, -9.092479], [-61.946317, 105.793511, -9.143054], [-61.789296, 105.903424, -9.207551], [-61.663438, 105.84252, -9.259248], [-61.634696, 105.642684, -9.271054], [-61.455495, 105.637204, -9.344662], [-61.416358, 105.834947, -9.360737], [-61.28752, 105.888093, -9.413658], [-61.136486, 105.768747, -9.475696], [-61.006185, 105.901862, -9.529218], [-61.107867, 106.071626, -9.487452], [-61.051515, 106.20767, -9.510599], [-60.866669, 106.238747, -9.586525], [-60.8616, 106.432477, -9.588607], [-61.04453, 106.474796, -9.513468], [-61.093662, 106.614082, -9.493286], [-60.983279, 106.777349, -9.538627], [-61.106407, 106.918209, -9.488051], [-61.263439, 106.808309, -9.42355], [-61.389297, 106.869214, -9.371853], [-61.41804, 107.06905, -9.360047], [-61.597233, 107.074521, -9.286442], [-61.63639, 106.876774, -9.270358], [-61.765215, 106.82364, -9.217443], [-61.916238, 106.942973, -9.155409], [-62.046538, 106.809858, -9.101888], [-61.944868, 106.640107, -9.143649], [-62.001233, 106.504051, -9.120497], [-62.186059, 106.472977, -9.044579], [-62.191135, 106.279257, -9.042494], [-62.008206, 106.236938, -9.117633], [-61.959073, 106.097651, -9.137814], [-62.069445, 105.934371, -9.092479]]}, {"shapeName": "R_arm_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-61.801446, 106.36427, -9.202561], [-61.715375, 106.572093, -9.237915], [-61.518579, 106.653246, -9.31875], [-61.326357, 106.560189, -9.397706], [-61.251289, 106.347464, -9.42854], [-61.337361, 106.13964, -9.393186], [-61.534156, 106.058487, -9.312351], [-61.72637, 106.151536, -9.233398]]}, {"shapeName": "R_arm_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-61.071336, 105.835305, -9.502457], [-58.56385, 102.966713, -10.53242]]}]},
			"C_neck_FK_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 170.055609, -3.570405], [-0.110097, 170.028193, -3.463775], [0.0, 170.000777, -3.357146], [0.110097, 170.028193, -3.463775], [0.0, 170.055609, -3.570405], [0.0, 170.134813, -3.436362], [0.0, 170.000777, -3.357146], [0.0, 169.921564, -3.491191], [-0.110097, 170.028193, -3.463775], [0.0, 170.134813, -3.436362], [0.110097, 170.028193, -3.463775], [0.0, 169.921564, -3.491191], [0.0, 170.055609, -3.570405], [0.0, 170.134813, -3.436362], [0.0, 159.968892, -6.05014]]}, {"shapeName": "C_neck_FK_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-10.386473, 159.996308, -6.15677], [-10.386473, 159.862263, -6.077556], [-10.386473, 159.941477, -5.943511], [-10.386473, 160.075522, -6.022725], [-10.386473, 159.996308, -6.15677], [-10.49656, 159.968892, -6.05014], [-10.386473, 159.941477, -5.943511], [-10.276375, 159.968892, -6.05014], [-10.386473, 159.862263, -6.077556], [-10.49656, 159.968892, -6.05014], [-10.386473, 160.075522, -6.022725], [-10.276375, 159.968892, -6.05014], [-10.386473, 159.996308, -6.15677], [-10.49656, 159.968892, -6.05014], [0.0, 159.968892, -6.05014]]}, {"shapeName": "C_neck_FK_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.110097, 157.382527, 4.00916], [0.0, 157.275898, 3.981745], [0.110097, 157.382527, 4.00916], [0.0, 157.489157, 4.036576], [-0.110097, 157.382527, 4.00916], [0.0, 157.355114, 4.11578], [0.110097, 157.382527, 4.00916], [0.0, 157.409943, 3.902531], [0.0, 157.275898, 3.981745], [0.0, 157.355114, 4.11578], [0.0, 157.489157, 4.036576], [0.0, 157.409943, 3.902531], [-0.110097, 157.382527, 4.00916], [0.0, 157.355114, 4.11578], [0.0, 159.968892, -6.05014]]}]},
			"C_midTorso_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[7.728141, 114.394936, -15.074083], [0.0, 114.394936, -17.741661], [-7.728141, 114.394936, -15.074083], [-10.929234, 114.394936, -8.633965], [-7.728141, 114.394936, -2.193848], [0.0, 114.394936, 0.47373], [7.728141, 114.394936, -2.193848], [10.929234, 114.394936, -8.633965]]}]},
			"R_leg_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-15.531734, 8.296326, -5.643404], [-15.305629, 8.296326, -5.643404], [-15.262809, 8.067055, -5.678982], [-15.102138, 8.001272, -5.689191], [-14.907788, 8.133471, -5.668676], [-14.747905, 7.975479, -5.693193], [-14.881679, 7.783448, -5.722992], [-14.815137, 7.624657, -5.747634], [-14.583101, 7.582343, -5.7542], [-14.583101, 7.358905, -5.788873], [-14.815137, 7.316591, -5.795439], [-14.881679, 7.157821, -5.820077], [-14.747905, 6.965769, -5.84988], [-14.907788, 6.807777, -5.874397], [-15.102138, 6.939976, -5.853882], [-15.262809, 6.874193, -5.86409], [-15.305629, 6.644922, -5.899669], [-15.531734, 6.644922, -5.899669], [-15.574576, 6.874193, -5.86409], [-15.735247, 6.939976, -5.853882], [-15.929597, 6.807777, -5.874397], [-16.089465, 6.965769, -5.84988], [-15.955706, 7.157821, -5.820077], [-16.022248, 7.316591, -5.795439], [-16.254263, 7.358905, -5.788873], [-16.254263, 7.582343, -5.7542], [-16.022248, 7.624657, -5.747634], [-15.955706, 7.783448, -5.722992], [-16.089465, 7.975479, -5.693193], [-15.929597, 8.133471, -5.668676], [-15.735247, 8.001272, -5.689191], [-15.574576, 8.067055, -5.678982], [-15.531734, 8.296326, -5.643404]]}, {"shapeName": "R_leg_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-15.664109, 7.713152, -5.733901], [-15.765773, 7.470624, -5.771536], [-15.664109, 7.228096, -5.809172], [-15.418685, 7.127655, -5.824758], [-15.173276, 7.228096, -5.809172], [-15.071612, 7.470624, -5.771536], [-15.173276, 7.713152, -5.733901], [-15.418685, 7.813593, -5.718315]]}, {"shapeName": "R_leg_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-14.583101, 7.470624, -5.771536], [-9.978517, 7.470624, -5.771536]]}]},
			"C_midTorso_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.010776, 114.394936, -13.642946], [0.0, 114.394936, -15.717729], [-6.010776, 114.394936, -13.642946], [-8.500516, 114.394936, -8.633965], [-6.010776, 114.394936, -3.624985], [0.0, 114.394936, -1.550202], [6.010776, 114.394936, -3.624985], [8.500516, 114.394936, -8.633965]]}]},
			"C_hip_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.010776, 98.139605, -13.642946], [-0.0, 95.582737, -15.717729], [-6.010776, 98.139605, -13.642946], [-8.500516, 100.696472, -8.633965], [-6.010776, 98.139605, -3.624985], [-0.0, 95.582737, -1.550202], [6.010776, 98.139605, -3.624985], [8.500516, 100.696472, -8.633965]]}]},
			"L_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[70.242783, 89.042787, 0.328451], [70.263616, 89.134908, 0.452236], [70.128012, 89.086239, 0.511278], [70.107179, 88.994118, 0.387493], [70.242783, 89.042787, 0.328451], [70.237453, 88.982704, 0.471986], [70.128012, 89.086239, 0.511278], [70.133337, 89.14633, 0.367738], [70.263616, 89.134908, 0.452236], [70.237453, 88.982704, 0.471986], [70.107179, 88.994118, 0.387493], [70.133337, 89.14633, 0.367738], [70.242783, 89.042787, 0.328451], [70.237453, 88.982704, 0.471986], [65.274059, 96.783015, -4.497686]]}, {"shapeName": "L_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[72.71047, 103.402273, -1.535229], [72.601024, 103.505816, -1.495943], [72.5957, 103.445725, -1.352403], [72.705146, 103.342182, -1.39169], [72.71047, 103.402273, -1.535229], [72.731296, 103.494388, -1.411448], [72.5957, 103.445725, -1.352403], [72.574867, 103.353604, -1.476187], [72.601024, 103.505816, -1.495943], [72.731296, 103.494388, -1.411448], [72.705146, 103.342182, -1.39169], [72.574867, 103.353604, -1.476187], [72.71047, 103.402273, -1.535229], [72.731296, 103.494388, -1.411448], [65.274059, 96.783015, -4.497686]]}, {"shapeName": "L_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[59.938633, 98.903013, 4.158512], [59.808354, 98.914434, 4.074014], [59.782196, 98.762223, 4.09377], [59.912475, 98.750801, 4.178267], [59.938633, 98.903013, 4.158512], [59.803035, 98.854341, 4.217546], [59.782196, 98.762223, 4.09377], [59.917799, 98.810892, 4.034728], [59.808354, 98.914434, 4.074014], [59.803035, 98.854341, 4.217546], [59.912475, 98.750801, 4.178267], [59.917799, 98.810892, 4.034728], [59.938633, 98.903013, 4.158512], [59.803035, 98.854341, 4.217546], [65.274059, 96.783015, -4.497686]]}]},
			"L_arm_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[62.653711, 106.428981, -8.852488], [62.510061, 106.264644, -8.911493], [62.32687, 106.392876, -8.98674], [62.180036, 106.321821, -9.047053], [62.146503, 106.088679, -9.060826], [61.937436, 106.082286, -9.146702], [61.891776, 106.312986, -9.165457], [61.741465, 106.37499, -9.227198], [61.565259, 106.235753, -9.299576], [61.413241, 106.391054, -9.362018], [61.53187, 106.589112, -9.31329], [61.466126, 106.74783, -9.340295], [61.250472, 106.784087, -9.428876], [61.244558, 107.010104, -9.431305], [61.457976, 107.059476, -9.343643], [61.515298, 107.221977, -9.320098], [61.386517, 107.412455, -9.372995], [61.530167, 107.576792, -9.31399], [61.713371, 107.448575, -9.238738], [61.860205, 107.51963, -9.178425], [61.893738, 107.752772, -9.164651], [62.102796, 107.759155, -9.078779], [62.148479, 107.52845, -9.060015], [62.298776, 107.466461, -8.99828], [62.474969, 107.605683, -8.925908], [62.626986, 107.450382, -8.863465], [62.508371, 107.252339, -8.912187], [62.57413, 107.093607, -8.885177], [62.78976, 107.057354, -8.796605], [62.795683, 106.831347, -8.794173], [62.582265, 106.781975, -8.881835], [62.524943, 106.619474, -8.90538], [62.653711, 106.428981, -8.852488]]}, {"shapeName": "L_arm_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[62.341045, 106.930529, -8.980917], [62.240629, 107.17299, -9.022164], [62.011034, 107.267668, -9.116471], [61.786775, 107.159101, -9.208587], [61.699196, 106.910922, -9.24456], [61.799612, 106.668462, -9.203314], [62.029207, 106.573783, -9.109006], [62.253457, 106.68234, -9.016895]]}, {"shapeName": "L_arm_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[61.48925, 106.313404, -9.330797], [58.56385, 102.966713, -10.53242]]}]},
			"R_reverseBall_CTL": {"color": 20, "shapes": [{"shapeName": "R_reverseBall_CTLShape", "degree": 1, "form": 0, "points": [[-9.978823, -1.122099, 7.512293], [-9.978014, 6.232423, 7.361522], [-9.972459, 7.226043, 6.326323], [-10.992518, 7.246839, 7.335281], [-9.977791, 8.261256, 7.31993], [-9.972459, 7.226043, 6.326323], [-8.963287, 7.246839, 7.34617], [-9.978014, 6.232423, 7.361522], [-9.983346, 7.267636, 8.355128], [-8.963287, 7.246839, 7.34617], [-9.977791, 8.261256, 7.31993], [-9.983346, 7.267636, 8.355128], [-10.992518, 7.246839, 7.335281], [-9.978014, 6.232423, 7.361522]]}]},
			"R_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-71.395762, 104.339715, -15.715697], [-71.381211, 104.448847, -15.6056], [-71.395762, 104.339715, -15.495502], [-71.410313, 104.230583, -15.6056], [-71.395762, 104.339715, -15.715697], [-71.504883, 104.354264, -15.6056], [-71.395762, 104.339715, -15.495502], [-71.28663, 104.325164, -15.6056], [-71.381211, 104.448847, -15.6056], [-71.504883, 104.354264, -15.6056], [-71.410313, 104.230583, -15.6056], [-71.28663, 104.325164, -15.6056], [-71.395762, 104.339715, -15.715697], [-71.504883, 104.354264, -15.6056], [-61.1004, 102.967, -15.6056]]}, {"shapeName": "R_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-59.727685, 113.262361, -15.715697], [-59.618554, 113.247811, -15.6056], [-59.727685, 113.262361, -15.495502], [-59.836817, 113.276912, -15.6056], [-59.727685, 113.262361, -15.715697], [-59.713136, 113.371483, -15.6056], [-59.727685, 113.262361, -15.495502], [-59.742236, 113.15323, -15.6056], [-59.618554, 113.247811, -15.6056], [-59.713136, 113.371483, -15.6056], [-59.836817, 113.276912, -15.6056], [-59.742236, 113.15323, -15.6056], [-59.727685, 113.262361, -15.715697], [-59.713136, 113.371483, -15.6056], [-61.1004, 102.967, -15.6056]]}, {"shapeName": "R_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.085849, 103.076132, -5.219127], [-60.991269, 102.952449, -5.219127], [-61.114951, 102.857868, -5.219127], [-61.209532, 102.981551, -5.219127], [-61.085849, 103.076132, -5.219127], [-61.1004, 102.967, -5.10904], [-61.114951, 102.857868, -5.219127], [-61.1004, 102.967, -5.329225], [-60.991269, 102.952449, -5.219127], [-61.1004, 102.967, -5.10904], [-61.209532, 102.981551, -5.219127], [-61.1004, 102.967, -5.329225], [-61.085849, 103.076132, -5.219127], [-61.1004, 102.967, -5.10904], [-61.1004, 102.967, -15.6056]]}]},
			"L_leg_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[14.748974, 7.470624, -13.722298], [9.978517, 7.470624, -17.015605], [5.208059, 7.470624, -13.722298], [3.232076, 7.470624, -5.771536], [5.208059, 7.470624, 2.179226], [9.978517, 7.470624, 5.472532], [14.748974, 7.470624, 2.179226], [16.724958, 7.470624, -5.771536]]}]},
			"R_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_C_CTLShape", "degree": 3, "form": 2, "points": [[-65.953724, 95.421056, -8.647559], [-67.000994, 96.098361, -8.98049], [-67.792363, 96.914815, -8.369345], [-67.864256, 97.392151, -7.172122], [-67.174561, 97.250752, -6.090139], [-66.127291, 96.573447, -5.757207], [-65.335922, 95.756992, -6.368352], [-65.264029, 95.279657, -7.565575]]}]},
			"L_upArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_upArm_FK_CTLShape", "degree": 3, "form": 2, "points": [[16.108188, 143.274215, -14.009061], [18.803733, 146.266917, -15.523291], [21.952812, 148.661537, -13.830892], [23.710735, 149.055336, -9.923239], [23.047742, 147.217637, -6.089387], [20.352197, 144.224935, -4.575157], [17.203118, 141.830315, -6.267556], [15.445194, 141.436516, -10.175209]]}]},
			"L_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_A_CTLShape", "degree": 3, "form": 2, "points": [[59.255902, 100.624629, -8.451258], [59.388957, 101.755964, -7.84402], [58.575276, 102.646909, -7.385215], [57.291501, 102.775559, -7.343606], [56.28965, 102.066555, -7.743566], [56.156594, 100.935221, -8.350805], [56.970275, 100.044276, -8.80961], [58.25405, 99.915625, -8.851219]]}]},
			"L_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.720822, 94.786276, -6.671075], [68.76176, 94.886977, -6.559602], [68.663789, 94.817288, -6.460668], [68.622851, 94.716587, -6.572141], [68.720822, 94.786276, -6.671075], [68.772823, 94.733797, -6.534026], [68.663789, 94.817288, -6.460668], [68.61178, 94.869774, -6.59772], [68.76176, 94.886977, -6.559602], [68.772823, 94.733797, -6.534026], [68.622851, 94.716587, -6.572141], [68.61178, 94.869774, -6.59772], [68.720822, 94.786276, -6.671075], [68.772823, 94.733797, -6.534026], [61.095652, 101.216011, -9.570426]]}, {"shapeName": "L_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.676451, 109.237706, -9.084186], [67.56741, 109.321203, -9.010831], [67.619418, 109.268718, -8.873779], [67.72846, 109.18522, -8.947134], [67.676451, 109.237706, -9.084186], [67.717383, 109.338399, -8.972714], [67.619418, 109.268718, -8.873779], [67.57848, 109.168017, -8.985252], [67.56741, 109.321203, -9.010831], [67.717383, 109.338399, -8.972714], [67.72846, 109.18522, -8.947134], [67.57848, 109.168017, -8.985252], [67.676451, 109.237706, -9.084186], [67.717383, 109.338399, -8.972714], [61.095652, 101.216011, -9.570426]]}, {"shapeName": "L_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[58.47489, 102.764041, 0.360644], [58.32491, 102.746837, 0.322526], [58.335981, 102.593651, 0.348105], [58.485961, 102.610855, 0.386223], [58.47489, 102.764041, 0.360644], [58.376922, 102.694351, 0.459569], [58.335981, 102.593651, 0.348105], [58.433952, 102.66334, 0.249171], [58.32491, 102.746837, 0.322526], [58.376922, 102.694351, 0.459569], [58.485961, 102.610855, 0.386223], [58.433952, 102.66334, 0.249171], [58.47489, 102.764041, 0.360644], [58.376922, 102.694351, 0.459569], [61.095652, 101.216011, -9.570426]]}]},
			"C_hip_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.869458, 98.139605, -14.358514], [-0.0, 95.21747, -16.729695], [-6.869458, 98.139605, -14.358514], [-9.714875, 101.061739, -8.633965], [-6.869458, 98.139605, -2.909417], [-0.0, 95.21747, -0.538236], [6.869458, 98.139605, -2.909417], [9.714875, 101.061739, -8.633965]]}]},
			"C_hip_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_CTLShape", "degree": 3, "form": 2, "points": [[8.586823, 98.139605, -15.789651], [-0.0, 94.486937, -18.753627], [-8.586823, 98.139605, -15.789651], [-12.143594, 101.792273, -8.633965], [-8.586823, 98.139605, -1.47828], [-0.0, 94.486937, 1.485696], [8.586823, 98.139605, -1.47828], [12.143594, 101.792273, -8.633965]]}]},
			"R_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-71.172528, 92.00114, -5.596022], [-71.217614, 92.09814, -5.482879], [-71.115495, 92.032152, -5.385614], [-71.07041, 91.935153, -5.498757], [-71.172528, 92.00114, -5.596022], [-71.220758, 91.944266, -5.459347], [-71.115495, 92.032152, -5.385614], [-71.067259, 92.089033, -5.522292], [-71.217614, 92.09814, -5.482879], [-71.220758, 91.944266, -5.459347], [-71.07041, 91.935153, -5.498757], [-71.067259, 92.089033, -5.522292], [-71.172528, 92.00114, -5.596022], [-71.220758, 91.944266, -5.459347], [-63.9032, 98.8455, -8.46003]]}, {"shapeName": "R_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-70.875217, 106.518016, -7.816281], [-70.769947, 106.605908, -7.742551], [-70.818184, 106.549028, -7.605873], [-70.923454, 106.461136, -7.679603], [-70.875217, 106.518016, -7.816281], [-70.920296, 106.615008, -7.703139], [-70.818184, 106.549028, -7.605873], [-70.773099, 106.452028, -7.719016], [-70.769947, 106.605908, -7.742551], [-70.920296, 106.615008, -7.703139], [-70.923454, 106.461136, -7.679603], [-70.773099, 106.452028, -7.719016], [-70.875217, 106.518016, -7.816281], [-70.920296, 106.615008, -7.703139], [-63.9032, 98.8455, -8.46003]]}, {"shapeName": "R_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.286586, 100.389829, 1.472709], [-61.136231, 100.380721, 1.433296], [-61.139382, 100.226841, 1.456831], [-61.289737, 100.235949, 1.496244], [-61.286586, 100.389829, 1.472709], [-61.18447, 100.32384, 1.569964], [-61.139382, 100.226841, 1.456831], [-61.2415, 100.292829, 1.359566], [-61.136231, 100.380721, 1.433296], [-61.18447, 100.32384, 1.569964], [-61.289737, 100.235949, 1.496244], [-61.2415, 100.292829, 1.359566], [-61.286586, 100.389829, 1.472709], [-61.18447, 100.32384, 1.569964], [-63.9032, 98.8455, -8.46003]]}]},
			"L_legBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_legBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 80.783151, -3.523062], [9.868419, 80.765401, -3.631719], [9.978517, 80.747651, -3.740376], [10.088614, 80.765401, -3.631719], [9.978517, 80.783151, -3.523062], [9.978517, 80.656754, -3.613971], [9.978517, 80.747651, -3.740376], [9.978517, 80.874058, -3.649469], [9.868419, 80.765401, -3.631719], [9.978517, 80.656754, -3.613971], [10.088614, 80.765401, -3.631719], [9.978517, 80.874058, -3.649469], [9.978517, 80.783151, -3.523062], [9.978517, 80.656754, -3.613971], [9.978517, 91.015999, -5.306253]]}, {"shapeName": "L_legBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.407956, 91.033749, -5.197596], [-0.407956, 91.124656, -5.324003], [-0.407956, 90.998249, -5.41491], [-0.407956, 90.907342, -5.288503], [-0.407956, 91.033749, -5.197596], [-0.518043, 91.015999, -5.306253], [-0.407956, 90.998249, -5.41491], [-0.297859, 91.015999, -5.306253], [-0.407956, 91.124656, -5.324003], [-0.518043, 91.015999, -5.306253], [-0.407956, 90.907342, -5.288503], [-0.297859, 91.015999, -5.306253], [-0.407956, 91.033749, -5.197596], [-0.518043, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}, {"shapeName": "L_legBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.868419, 89.341465, -15.556851], [9.978517, 89.450122, -15.574601], [10.088614, 89.341465, -15.556851], [9.978517, 89.232808, -15.5391], [9.868419, 89.341465, -15.556851], [9.978517, 89.323717, -15.665498], [10.088614, 89.341465, -15.556851], [9.978517, 89.359215, -15.448193], [9.978517, 89.450122, -15.574601], [9.978517, 89.323717, -15.665498], [9.978517, 89.232808, -15.5391], [9.978517, 89.359215, -15.448193], [9.868419, 89.341465, -15.556851], [9.978517, 89.323717, -15.665498], [9.978517, 91.015999, -5.306253]]}]},
			"C_head_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[8.3483, 172.524111, -4.898692], [0.0, 175.981962, -4.869811], [-8.3483, 172.524111, -4.898692], [-11.806272, 164.176102, -4.968417], [-8.3483, 155.828093, -5.038142], [0.0, 152.370242, -5.067023], [8.3483, 155.828093, -5.038142], [11.806272, 164.176102, -4.968417]]}]},
			"L_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[71.486898, 113.113013, -10.642518], [71.486898, 113.22311, -10.53242], [71.486898, 113.113013, -10.422323], [71.486898, 113.002915, -10.53242], [71.486898, 113.113013, -10.642518], [71.596985, 113.113013, -10.53242], [71.486898, 113.113013, -10.422323], [71.3768, 113.113013, -10.53242], [71.486898, 113.22311, -10.53242], [71.596985, 113.113013, -10.53242], [71.486898, 113.002915, -10.53242], [71.3768, 113.113013, -10.53242], [71.486898, 113.113013, -10.642518], [71.596985, 113.113013, -10.53242], [61.100425, 113.113013, -10.53242]]}, {"shapeName": "L_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[61.100425, 123.499485, -10.642518], [60.990328, 123.499485, -10.53242], [61.100425, 123.499485, -10.422323], [61.210523, 123.499485, -10.53242], [61.100425, 123.499485, -10.642518], [61.100425, 123.609573, -10.53242], [61.100425, 123.499485, -10.422323], [61.100425, 123.389388, -10.53242], [60.990328, 123.499485, -10.53242], [61.100425, 123.609573, -10.53242], [61.210523, 123.499485, -10.53242], [61.100425, 123.389388, -10.53242], [61.100425, 123.499485, -10.642518], [61.100425, 123.609573, -10.53242], [61.100425, 113.113013, -10.53242]]}, {"shapeName": "L_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.100425, 113.22311, -0.145948], [60.990328, 113.113013, -0.145948], [61.100425, 113.002915, -0.145948], [61.210523, 113.113013, -0.145948], [61.100425, 113.22311, -0.145948], [61.100425, 113.113013, -0.03586], [61.100425, 113.002915, -0.145948], [61.100425, 113.113013, -0.256045], [60.990328, 113.113013, -0.145948], [61.100425, 113.113013, -0.03586], [61.210523, 113.113013, -0.145948], [61.100425, 113.113013, -0.256045], [61.100425, 113.22311, -0.145948], [61.100425, 113.113013, -0.03586], [61.100425, 113.113013, -10.53242]]}]},
			"L_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_C_CTLShape", "degree": 3, "form": 2, "points": [[68.615045, 102.589601, -16.798184], [68.71015, 103.778417, -17.29218], [68.805255, 104.967233, -16.798184], [68.844649, 105.459656, -15.60557], [68.805255, 104.967233, -14.412956], [68.71015, 103.778417, -13.91896], [68.615045, 102.589601, -14.412956], [68.575651, 102.097178, -15.60557]]}]},
			"R_leg_IK_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-14.152667, 7.470624, -12.728453], [-9.978517, 7.470624, -15.610096], [-5.804366, 7.470624, -12.728453], [-4.075381, 7.470624, -5.771536], [-5.804366, 7.470624, 1.185381], [-9.978517, 7.470624, 4.067023], [-14.152667, 7.470624, 1.185381], [-15.881652, 7.470624, -5.771536]]}]},
			"L_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_B_CTLShape", "degree": 3, "form": 2, "points": [[63.414773, 97.794765, -9.685632], [64.340003, 98.607958, -10.071673], [65.009331, 99.5603, -9.513637], [65.030674, 100.093922, -8.338412], [64.39153, 99.896237, -7.23443], [63.4663, 99.083044, -6.84839], [62.796971, 98.130701, -7.406425], [62.775629, 97.597079, -8.58165]]}]},
			"L_leg_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[17.118368, 8.53224, -5.606795], [16.827661, 8.53224, -5.606795], [16.772607, 8.237464, -5.652538], [16.56603, 8.152885, -5.665663], [16.316151, 8.322855, -5.639287], [16.110588, 8.119723, -5.670809], [16.282583, 7.872827, -5.709123], [16.197028, 7.668666, -5.740804], [15.898697, 7.614263, -5.749247], [15.898697, 7.326985, -5.793826], [16.197028, 7.272582, -5.802269], [16.282583, 7.068448, -5.833946], [16.110588, 6.821524, -5.872263], [16.316151, 6.618393, -5.903785], [16.56603, 6.788363, -5.87741], [16.772607, 6.703784, -5.890534], [16.827661, 6.409008, -5.936278], [17.118368, 6.409008, -5.936278], [17.17345, 6.703784, -5.890534], [17.380027, 6.788363, -5.87741], [17.629906, 6.618393, -5.903785], [17.835451, 6.821524, -5.872263], [17.663474, 7.068448, -5.833946], [17.749029, 7.272582, -5.802269], [18.047333, 7.326985, -5.793826], [18.047333, 7.614263, -5.749247], [17.749029, 7.668666, -5.740804], [17.663474, 7.872827, -5.709123], [17.835451, 8.119723, -5.670809], [17.629906, 8.322855, -5.639287], [17.380027, 8.152885, -5.665663], [17.17345, 8.237464, -5.652538], [17.118368, 8.53224, -5.606795]]}, {"shapeName": "L_leg_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[17.288564, 7.782446, -5.723148], [17.419275, 7.470624, -5.771536], [17.288564, 7.158802, -5.819925], [16.973019, 7.029664, -5.839964], [16.657493, 7.158802, -5.819925], [16.526782, 7.470624, -5.771536], [16.657493, 7.782446, -5.723148], [16.973019, 7.911584, -5.703108]]}, {"shapeName": "L_leg_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[15.898697, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}]},
			"L_innerBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_innerBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[15.745704, 1.917931, 7.35207], [15.746283, 2.030262, 7.459886], [15.746885, 1.922444, 7.572216], [15.746307, 1.810113, 7.464399], [15.745704, 1.917931, 7.35207], [15.85638, 1.920187, 7.461552], [15.746885, 1.922444, 7.572216], [15.636199, 1.920187, 7.462734], [15.746283, 2.030262, 7.459886], [15.85638, 1.920187, 7.461552], [15.746307, 1.810113, 7.464399], [15.636199, 1.920187, 7.462734], [15.745704, 1.917931, 7.35207], [15.85638, 1.920187, 7.461552], [5.359972, 1.920187, 7.51788]]}, {"shapeName": "L_innerBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[5.358238, 12.302221, 7.194924], [5.248733, 12.304478, 7.305588], [5.35942, 12.306735, 7.41507], [5.468925, 12.304478, 7.304406], [5.358238, 12.302221, 7.194924], [5.358817, 12.414542, 7.302741], [5.35942, 12.306735, 7.41507], [5.358841, 12.194404, 7.307253], [5.248733, 12.304478, 7.305588], [5.358817, 12.414542, 7.302741], [5.468925, 12.304478, 7.304406], [5.358841, 12.194404, 7.307253], [5.358238, 12.302221, 7.194924], [5.358817, 12.414542, 7.302741], [5.359972, 1.920187, 7.51788]]}, {"shapeName": "L_innerBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[5.415685, 2.243148, 17.899765], [5.305601, 2.133073, 17.902612], [5.415709, 2.022999, 17.904278], [5.525793, 2.133073, 17.90143], [5.415685, 2.243148, 17.899765], [5.416288, 2.13533, 18.012084], [5.415709, 2.022999, 17.904278], [5.415106, 2.130817, 17.791948], [5.305601, 2.133073, 17.902612], [5.416288, 2.13533, 18.012084], [5.525793, 2.133073, 17.90143], [5.415106, 2.130817, 17.791948], [5.415685, 2.243148, 17.899765], [5.416288, 2.13533, 18.012084], [5.359972, 1.920187, 7.51788]]}]},
			"R_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_D_CTLShape", "degree": 3, "form": 2, "points": [[-72.357392, 102.291875, -16.798184], [-72.515012, 103.474028, -17.29218], [-72.672633, 104.656181, -16.798184], [-72.737921, 105.145843, -15.60557], [-72.672633, 104.656181, -14.412956], [-72.515012, 103.474028, -13.91896], [-72.357392, 102.291875, -14.412956], [-72.292104, 101.802213, -15.60557]]}]},
			"L_wrist_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_wrist_FK_CTLShape", "degree": 3, "form": 2, "points": [[59.254016, 98.33514, -14.54661], [62.405316, 101.224514, -15.03235], [64.30532, 104.113889, -12.47176], [63.841025, 105.310705, -8.364793], [61.284417, 104.113889, -5.117254], [58.133117, 101.224514, -4.631514], [56.233113, 98.33514, -7.192104], [56.697407, 97.138324, -11.299072]]}]},
			"L_wrist_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_wrist_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[65.588617, 95.83296, -7.765984], [65.616732, 95.912981, -7.635411], [65.504953, 95.83296, -7.562302], [65.476837, 95.75294, -7.692874], [65.588617, 95.83296, -7.765984], [65.620798, 95.757349, -7.633742], [65.504953, 95.83296, -7.562302], [65.472765, 95.908579, -7.694547], [65.616732, 95.912981, -7.635411], [65.620798, 95.757349, -7.633742], [65.476837, 95.75294, -7.692874], [65.472765, 95.908579, -7.694547], [65.588617, 95.83296, -7.765984], [65.620798, 95.757349, -7.633742], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_wrist_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.204449, 110.515778, -7.923782], [65.088598, 110.591397, -7.852345], [65.120786, 110.515778, -7.720101], [65.236637, 110.44016, -7.791537], [65.204449, 110.515778, -7.923782], [65.232559, 110.595792, -7.793213], [65.120786, 110.515778, -7.720101], [65.09267, 110.435758, -7.850673], [65.088598, 110.591397, -7.852345], [65.232559, 110.595792, -7.793213], [65.236637, 110.44016, -7.791537], [65.09267, 110.435758, -7.850673], [65.204449, 110.515778, -7.923782], [65.232559, 110.595792, -7.793213], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_wrist_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[54.687444, 103.046734, -0.896134], [54.543477, 103.042331, -0.95527], [54.547549, 102.886692, -0.953597], [54.691516, 102.891095, -0.894462], [54.687444, 103.046734, -0.896134], [54.575669, 102.966713, -0.823034], [54.547549, 102.886692, -0.953597], [54.659328, 102.966713, -1.026707], [54.543477, 103.042331, -0.95527], [54.575669, 102.966713, -0.823034], [54.691516, 102.891095, -0.894462], [54.659328, 102.966713, -1.026707], [54.687444, 103.046734, -0.896134], [54.575669, 102.966713, -0.823034], [58.56385, 102.966713, -10.53242]]}]},
			"R_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-71.486873, 113.113, -10.642498], [-71.486873, 113.223097, -10.5324], [-71.486873, 113.113, -10.422303], [-71.486873, 113.002902, -10.5324], [-71.486873, 113.113, -10.642498], [-71.59696, 113.113, -10.5324], [-71.486873, 113.113, -10.422303], [-71.376775, 113.113, -10.5324], [-71.486873, 113.223097, -10.5324], [-71.59696, 113.113, -10.5324], [-71.486873, 113.002902, -10.5324], [-71.376775, 113.113, -10.5324], [-71.486873, 113.113, -10.642498], [-71.59696, 113.113, -10.5324], [-61.1004, 113.113, -10.5324]]}, {"shapeName": "R_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-61.1004, 123.499472, -10.642498], [-60.990303, 123.499472, -10.5324], [-61.1004, 123.499472, -10.422303], [-61.210498, 123.499472, -10.5324], [-61.1004, 123.499472, -10.642498], [-61.1004, 123.60956, -10.5324], [-61.1004, 123.499472, -10.422303], [-61.1004, 123.389375, -10.5324], [-60.990303, 123.499472, -10.5324], [-61.1004, 123.60956, -10.5324], [-61.210498, 123.499472, -10.5324], [-61.1004, 123.389375, -10.5324], [-61.1004, 123.499472, -10.642498], [-61.1004, 123.60956, -10.5324], [-61.1004, 113.113, -10.5324]]}, {"shapeName": "R_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.1004, 113.223097, -0.145928], [-60.990303, 113.113, -0.145928], [-61.1004, 113.002902, -0.145928], [-61.210498, 113.113, -0.145928], [-61.1004, 113.223097, -0.145928], [-61.1004, 113.113, -0.03584], [-61.1004, 113.002902, -0.145928], [-61.1004, 113.113, -0.256025], [-60.990303, 113.113, -0.145928], [-61.1004, 113.113, -0.03584], [-61.210498, 113.113, -0.145928], [-61.1004, 113.113, -0.256025], [-61.1004, 113.223097, -0.145928], [-61.1004, 113.113, -0.03584], [-61.1004, 113.113, -10.5324]]}]},
			"C_midNeck_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[11.449097, 160.241098, -15.831379], [0.0, 161.225189, -19.658861], [-11.449097, 160.241098, -15.831379], [-16.191458, 157.865288, -6.591002], [-11.449097, 155.489478, 2.649375], [0.0, 154.505387, 6.476857], [11.449097, 155.489478, 2.649375], [16.191458, 157.865288, -6.591002]]}]},
			"R_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_A_CTLShape", "degree": 3, "form": 2, "points": [[-60.652195, 100.12518, -10.777941], [-61.532504, 100.978468, -11.182067], [-62.156911, 101.970904, -10.642117], [-62.159646, 102.521134, -9.474384], [-61.539109, 102.306841, -8.362911], [-60.658801, 101.453554, -7.958784], [-60.034393, 100.461117, -8.498734], [-60.031658, 99.910888, -9.666468]]}]},
			"world_CTL": {"color": 1, "shapes": [{"shapeName": "world_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -577.7], [256.65, 0.0, -320.8], [192.4, 0.0, -320.8], [192.4, 0.0, -192.35], [320.85, 0.0, -192.35], [320.85, 0.0, -256.6], [577.7, 0.0, 0.0], [320.8, 0.0, 256.65], [320.8, 0.0, 192.4], [192.35, 0.0, 192.4], [192.35, 0.0, 320.85], [256.6, 0.0, 320.85], [0.0, 0.0, 577.7], [-256.65, 0.0, 320.8], [-192.4, 0.0, 320.8], [-192.4, 0.0, 192.35], [-320.85, 0.0, 192.35], [-320.85, 0.0, 256.6], [-577.7, 0.0, 0.0], [-320.8, 0.0, -256.65], [-320.8, 0.0, -192.4], [-192.35, 0.0, -192.4], [-192.35, 0.0, -320.85], [-256.6, 0.0, -320.85], [0.0, 0.0, -577.7], [50.3, 0.7, -528.3], [45.9, 0.0, -523.6], [45.9, 0.0, -504.4], [41.9, 0.0, -504.4], [42.15, 0.0, -523.75], [39.3, 0.0, -522.3], [39.4, 0.0, -513.9], [35.35, 0.0, -513.9], [35.35, 0.0, -522.3], [32.85, 0.0, -523.75], [32.85, 0.0, -504.1], [28.8, 0.0, -504.1], [28.8, 0.0, -524.25], [32.05, 0.0, -527.5], [37.05, 0.0, -525.0], [42.55, 0.0, -527.5], [45.9, 0.0, -523.7], [42.55, 0.0, -527.5], [37.1, 0.0, -525.05], [32.05, 0.0, -527.45], [22.3, 0.0, -527.5], [25.6, 0.0, -524.25], [25.6, 0.0, -507.4], [22.3, 0.0, -504.1], [11.75, 0.0, -504.1], [8.5, 0.0, -507.4], [8.5, 0.0, -524.25], [11.75, 0.0, -527.5], [22.3, 0.0, -527.5], [21.05, 0.0, -523.75], [21.55, 0.0, -508.25], [12.5, 0.0, -508.35], [12.55, 0.0, -523.75], [21.1, 0.0, -523.85], [22.3, 0.0, -527.5], [11.75, 0.0, -527.5], [5.0, 0.0, -527.5], [5.25, 0.0, -504.1], [-6.15, 0.0, -504.1], [-9.45, 0.0, -507.4], [-9.45, 0.0, -514.45], [-6.1, 0.0, -517.7], [-5.9, 0.0, -517.95], [-12.45, 0.0, -527.4], [-12.45, 0.0, -527.5], [-7.75, 0.0, -527.5], [-1.2, 0.0, -518.0], [1.25, 0.0, -518.0], [1.25, 0.0, -508.0], [-5.05, 0.0, -508.0], [-5.1, 0.0, -513.95], [1.25, 0.0, -513.95], [1.25, 0.0, -527.5], [5.0, 0.0, -527.5], [-32.15, 0.0, -527.5], [-32.15, 0.0, -523.75], [-19.05, 0.0, -523.7], [-19.05, 0.0, -504.1], [-15.0, 0.0, -504.1], [-15.0, 0.0, -527.5], [-49.2, 0.0, -527.5], [-52.2, 0.0, -524.25], [-52.45, 0.0, -507.4], [-49.2, 0.0, -504.1], [-35.35, 0.0, -504.1], [-35.35, 0.0, -527.5], [-39.45, 0.0, -523.75], [-39.35, 0.0, -507.9], [-47.9, 0.0, -507.9], [-47.8, 0.0, -523.65], [-39.3, 0.0, -523.85], [-35.25, 0.0, -527.5]]}]},
			"L_leg_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[17.911685, 8.650198, -5.58849], [17.588678, 8.650198, -5.58849], [17.527506, 8.322669, -5.639316], [17.297976, 8.228692, -5.653899], [17.020333, 8.417548, -5.624593], [16.791929, 8.191846, -5.659617], [16.983035, 7.917516, -5.702188], [16.887974, 7.690671, -5.737389], [16.556495, 7.630223, -5.74677], [16.556495, 7.311025, -5.796303], [16.887974, 7.250577, -5.805683], [16.983035, 7.023762, -5.84088], [16.791929, 6.749402, -5.883455], [17.020333, 6.5237, -5.91848], [17.297976, 6.712556, -5.889173], [17.527506, 6.618579, -5.903756], [17.588678, 6.29105, -5.954582], [17.911685, 6.29105, -5.954582], [17.972887, 6.618579, -5.903756], [18.202417, 6.712556, -5.889173], [18.48006, 6.5237, -5.91848], [18.708443, 6.749402, -5.883455], [18.517358, 7.023762, -5.84088], [18.612419, 7.250577, -5.805683], [18.943868, 7.311025, -5.796303], [18.943868, 7.630223, -5.74677], [18.612419, 7.690671, -5.737389], [18.517358, 7.917516, -5.702188], [18.708443, 8.191846, -5.659617], [18.48006, 8.417548, -5.624593], [18.202417, 8.228692, -5.653899], [17.972887, 8.322669, -5.639316], [17.911685, 8.650198, -5.58849]]}, {"shapeName": "L_leg_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[18.100792, 7.817093, -5.717771], [18.246026, 7.470624, -5.771536], [18.100792, 7.124155, -5.825301], [17.750186, 6.980669, -5.847567], [17.399601, 7.124155, -5.825301], [17.254367, 7.470624, -5.771536], [17.399601, 7.817093, -5.717771], [17.750186, 7.960579, -5.695505]]}, {"shapeName": "L_leg_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[16.556495, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}]},
			"R_arm_IK_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-57.040912, 108.1303, -7.209173], [-52.399663, 102.820658, -9.115591], [-55.175335, 102.820658, -15.873073], [-59.816584, 108.1303, -13.966656], [-64.728038, 103.112768, -11.94925], [-60.086789, 97.803126, -13.855668], [-57.311117, 97.803126, -7.098185], [-61.952366, 103.112768, -5.191767], [-57.040912, 108.1303, -7.209173], [-59.816584, 108.1303, -13.966656], [-55.175335, 102.820658, -15.873073], [-60.086789, 97.803126, -13.855668], [-64.728038, 103.112768, -11.94925], [-61.952366, 103.112768, -5.191767], [-57.311117, 97.803126, -7.098185], [-52.399663, 102.820658, -9.115591]]}]},
			"C_midNeck_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[8.586823, 159.647145, -13.521285], [0.0, 160.385213, -16.391896], [-8.586823, 159.647145, -13.521285], [-12.143594, 157.865288, -6.591002], [-8.586823, 156.08343, 0.339281], [0.0, 155.345362, 3.209892], [8.586823, 156.08343, 0.339281], [12.143594, 157.865288, -6.591002]]}]},
			"R_leg_IK_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-13.55636, 7.470624, -11.734608], [-9.978517, 7.470624, -14.204588], [-6.400674, 7.470624, -11.734608], [-4.918686, 7.470624, -5.771536], [-6.400674, 7.470624, 0.191535], [-9.978517, 7.470624, 2.661515], [-13.55636, 7.470624, 0.191535], [-15.038347, 7.470624, -5.771536]]}]},
			"R_legBase_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_CTLShape", "degree": 3, "form": 0, "points": [[-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.420897, -2.827685], [-9.978517, 92.076032, 1.182703], [-9.978517, 92.326272, 2.714539], [-19.532495, 92.076032, 1.182703], [-25.437185, 91.420897, -2.827685], [-25.437185, 90.611101, -7.784821], [-19.532495, 89.955965, -11.795209], [-9.978517, 89.705725, -13.327045], [-9.978517, 89.955965, -11.795209], [-9.978517, 90.611101, -7.784821], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253], [-9.978517, 91.015999, -5.306253]]}]},
			"L_leg_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 40.824689, 102.617543], [9.868419, 40.825303, 102.507447], [9.978517, 40.825916, 102.397351], [10.088614, 40.825303, 102.507447], [9.978517, 40.824689, 102.617543], [9.978517, 40.715217, 102.506834], [9.978517, 40.825916, 102.397351], [9.978517, 40.935398, 102.50806], [9.868419, 40.825303, 102.507447], [9.978517, 40.715217, 102.506834], [10.088614, 40.825303, 102.507447], [9.978517, 40.935398, 102.50806], [9.978517, 40.824689, 102.617543], [9.978517, 40.715217, 102.506834], [9.978517, 51.211614, 102.565291]]}, {"shapeName": "L_leg_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.407956, 51.211001, 102.675386], [-0.407956, 51.32171, 102.565904], [-0.407956, 51.212227, 102.455195], [-0.407956, 51.101518, 102.564677], [-0.407956, 51.211001, 102.675386], [-0.518043, 51.211614, 102.565291], [-0.407956, 51.212227, 102.455195], [-0.297859, 51.211614, 102.565291], [-0.407956, 51.32171, 102.565904], [-0.518043, 51.211614, 102.565291], [-0.407956, 51.101518, 102.564677], [-0.297859, 51.211614, 102.565291], [-0.407956, 51.211001, 102.675386], [-0.518043, 51.211614, 102.565291], [9.978517, 51.211614, 102.565291]]}, {"shapeName": "L_leg_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.868419, 51.269458, 92.178979], [9.978517, 51.379554, 92.179592], [10.088614, 51.269458, 92.178979], [9.978517, 51.159362, 92.178366], [9.868419, 51.269458, 92.178979], [9.978517, 51.270071, 92.068893], [10.088614, 51.269458, 92.178979], [9.978517, 51.268845, 92.289075], [9.978517, 51.379554, 92.179592], [9.978517, 51.270071, 92.068893], [9.978517, 51.159362, 92.178366], [9.978517, 51.268845, 92.289075], [9.868419, 51.269458, 92.178979], [9.978517, 51.270071, 92.068893], [9.978517, 51.211614, 102.565291]]}]},
			"R_leg_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.325051, 8.414283, -5.6251], [-16.066645, 8.414283, -5.6251], [-16.017708, 8.15226, -5.66576], [-15.834084, 8.077079, -5.677427], [-15.611969, 8.228163, -5.653982], [-15.429247, 8.047601, -5.682001], [-15.582131, 7.828138, -5.716057], [-15.506083, 7.646662, -5.744219], [-15.240899, 7.598303, -5.751723], [-15.240899, 7.342945, -5.79135], [-15.506083, 7.294586, -5.798854], [-15.582131, 7.113134, -5.827012], [-15.429247, 6.893647, -5.861072], [-15.611969, 6.713085, -5.889091], [-15.834084, 6.864169, -5.865646], [-16.017708, 6.788988, -5.877312], [-16.066645, 6.526965, -5.917973], [-16.325051, 6.526965, -5.917973], [-16.374013, 6.788988, -5.877312], [-16.557637, 6.864169, -5.865646], [-16.779752, 6.713085, -5.889091], [-16.962458, 6.893647, -5.861072], [-16.80959, 7.113134, -5.827012], [-16.885638, 7.294586, -5.798854], [-17.150798, 7.342945, -5.79135], [-17.150798, 7.598303, -5.751723], [-16.885638, 7.646662, -5.744219], [-16.80959, 7.828138, -5.716057], [-16.962458, 8.047601, -5.682001], [-16.779752, 8.228163, -5.653982], [-16.557637, 8.077079, -5.677427], [-16.374013, 8.15226, -5.66576], [-16.325051, 8.414283, -5.6251]]}, {"shapeName": "R_leg_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-16.476337, 7.747799, -5.728524], [-16.592524, 7.470624, -5.771536], [-16.476337, 7.193449, -5.814548], [-16.195852, 7.07866, -5.832361], [-15.915384, 7.193449, -5.814548], [-15.799197, 7.470624, -5.771536], [-15.915384, 7.747799, -5.728524], [-16.195852, 7.862588, -5.710711]]}, {"shapeName": "R_leg_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-15.240899, 7.470624, -5.771536], [-9.978517, 7.470624, -5.771536]]}]},
			"L_leg_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.325051, 8.414283, -5.6251], [16.066645, 8.414283, -5.6251], [16.017708, 8.15226, -5.66576], [15.834084, 8.077079, -5.677427], [15.611969, 8.228163, -5.653982], [15.429247, 8.047601, -5.682001], [15.582131, 7.828138, -5.716057], [15.506083, 7.646662, -5.744219], [15.240899, 7.598303, -5.751723], [15.240899, 7.342945, -5.79135], [15.506083, 7.294586, -5.798854], [15.582131, 7.113134, -5.827012], [15.429247, 6.893647, -5.861072], [15.611969, 6.713085, -5.889091], [15.834084, 6.864169, -5.865646], [16.017708, 6.788988, -5.877312], [16.066645, 6.526965, -5.917973], [16.325051, 6.526965, -5.917973], [16.374013, 6.788988, -5.877312], [16.557637, 6.864169, -5.865646], [16.779752, 6.713085, -5.889091], [16.962458, 6.893647, -5.861072], [16.80959, 7.113134, -5.827012], [16.885638, 7.294586, -5.798854], [17.150798, 7.342945, -5.79135], [17.150798, 7.598303, -5.751723], [16.885638, 7.646662, -5.744219], [16.80959, 7.828138, -5.716057], [16.962458, 8.047601, -5.682001], [16.779752, 8.228163, -5.653982], [16.557637, 8.077079, -5.677427], [16.374013, 8.15226, -5.66576], [16.325051, 8.414283, -5.6251]]}, {"shapeName": "L_leg_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[16.476337, 7.747799, -5.728524], [16.592524, 7.470624, -5.771536], [16.476337, 7.193449, -5.814548], [16.195852, 7.07866, -5.832361], [15.915384, 7.193449, -5.814548], [15.799197, 7.470624, -5.771536], [15.915384, 7.747799, -5.728524], [16.195852, 7.862588, -5.710711]]}, {"shapeName": "L_leg_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[15.240899, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}]},
			"L_toe_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[13.556335, 5.244039, 7.554273], [9.978517, 6.725915, 7.576775], [6.400698, 5.244671, 7.528004], [4.91872, 1.667994, 7.436529], [6.400698, -1.908946, 7.355935], [9.978517, -3.390821, 7.333433], [13.556335, -1.909577, 7.382204], [15.038313, 1.6671, 7.473679]]}]},
			"L_leg_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[14.152667, 7.470624, -12.728453], [9.978517, 7.470624, -15.610096], [5.804366, 7.470624, -12.728453], [4.075381, 7.470624, -5.771536], [5.804366, 7.470624, 1.185381], [9.978517, 7.470624, 4.067023], [14.152667, 7.470624, 1.185381], [15.881652, 7.470624, -5.771536]]}]},
			"L_wrist_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[57.85321, 100.944151, -13.832695], [60.05912, 102.966713, -14.172713], [61.389123, 104.989275, -12.3803], [61.064117, 105.827046, -9.505423], [59.274491, 104.989275, -7.232145], [57.068581, 102.966713, -6.892128], [55.738578, 100.944151, -8.68454], [56.063584, 100.10638, -11.559418]]}]},
			"R_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_C_CTLShape", "degree": 3, "form": 2, "points": [[-65.048387, 95.785128, -5.838564], [-66.153156, 96.450189, -5.898069], [-66.742962, 97.310215, -5.13725], [-66.472304, 97.861413, -4.001782], [-65.499732, 97.780901, -3.156808], [-64.394963, 97.11584, -3.097303], [-63.805156, 96.255815, -3.858122], [-64.075814, 95.704617, -4.993589]]}]},
			"R_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-58.062867, 93.615426, 3.304501], [-57.925994, 93.673256, 3.351025], [-57.851867, 93.56185, 3.271419], [-57.98874, 93.504021, 3.224895], [-58.062867, 93.615426, 3.304501], [-57.959998, 93.5235, 3.376669], [-57.851867, 93.56185, 3.271419], [-57.954735, 93.653783, 3.199243], [-57.925994, 93.673256, 3.351025], [-57.959998, 93.5235, 3.376669], [-57.98874, 93.504021, 3.224895], [-57.954735, 93.653783, 3.199243], [-58.062867, 93.615426, 3.304501], [-57.959998, 93.5235, 3.376669], [-57.7091, 99.7343, -5.08151]]}, {"shapeName": "R_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-54.854902, 107.743768, 0.88447], [-54.746771, 107.782125, 0.779212], [-54.643902, 107.690192, 0.851388], [-54.752034, 107.651836, 0.956646], [-54.854902, 107.743768, 0.88447], [-54.718032, 107.801589, 0.930988], [-54.643902, 107.690192, 0.851388], [-54.780775, 107.632363, 0.804864], [-54.746771, 107.782125, 0.779212], [-54.718032, 107.801589, 0.930988], [-54.752034, 107.651836, 0.956646], [-54.780775, 107.632363, 0.804864], [-54.854902, 107.743768, 0.88447], [-54.718032, 107.801589, 0.930988], [-57.7091, 99.7343, -5.08151]]}, {"shapeName": "R_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-47.724971, 97.291769, -6.578885], [-47.753712, 97.272297, -6.730667], [-47.787717, 97.122535, -6.705015], [-47.758975, 97.142008, -6.553233], [-47.724971, 97.291769, -6.578885], [-47.650853, 97.180367, -6.658489], [-47.787717, 97.122535, -6.705015], [-47.861844, 97.23394, -6.625409], [-47.753712, 97.272297, -6.730667], [-47.650853, 97.180367, -6.658489], [-47.758975, 97.142008, -6.553233], [-47.861844, 97.23394, -6.625409], [-47.724971, 97.291769, -6.578885], [-47.650853, 97.180367, -6.658489], [-57.7091, 99.7343, -5.08151]]}]},
			"L_legBase_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 89.528858, -5.063314], [9.978517, 87.122625, -4.670233], [9.978517, 86.203524, -4.520089], [9.978517, 88.046815, 0.987164], [9.978517, 91.02423, 4.09055], [9.978517, 93.998511, 3.604672], [9.978517, 95.833563, -0.284876], [9.978517, 95.828474, -6.092417], [9.978517, 94.909373, -5.942273], [9.978517, 92.50314, -5.549192], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}]},
			"R_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-79.063595, 102.949728, -15.715697], [-79.072374, 103.059475, -15.6056], [-79.063595, 102.949728, -15.495502], [-79.054815, 102.839981, -15.6056], [-79.063595, 102.949728, -15.715697], [-79.173331, 102.940949, -15.6056], [-79.063595, 102.949728, -15.495502], [-78.953848, 102.958508, -15.6056], [-79.072374, 103.059475, -15.6056], [-79.173331, 102.940949, -15.6056], [-79.054815, 102.839981, -15.6056], [-78.953848, 102.958508, -15.6056], [-79.063595, 102.949728, -15.715697], [-79.173331, 102.940949, -15.6056], [-68.7102, 103.778, -15.6056]]}, {"shapeName": "R_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-69.538472, 114.131395, -15.715697], [-69.428725, 114.140174, -15.6056], [-69.538472, 114.131395, -15.495502], [-69.648218, 114.122615, -15.6056], [-69.538472, 114.131395, -15.715697], [-69.547251, 114.241131, -15.6056], [-69.538472, 114.131395, -15.495502], [-69.529692, 114.021648, -15.6056], [-69.428725, 114.140174, -15.6056], [-69.547251, 114.241131, -15.6056], [-69.648218, 114.122615, -15.6056], [-69.529692, 114.021648, -15.6056], [-69.538472, 114.131395, -15.715697], [-69.547251, 114.241131, -15.6056], [-68.7102, 103.778, -15.6056]]}, {"shapeName": "R_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-68.71898, 103.887747, -5.219127], [-68.600453, 103.78678, -5.219127], [-68.70142, 103.668253, -5.219127], [-68.819947, 103.76922, -5.219127], [-68.71898, 103.887747, -5.219127], [-68.7102, 103.778, -5.10904], [-68.70142, 103.668253, -5.219127], [-68.7102, 103.778, -5.329225], [-68.600453, 103.78678, -5.219127], [-68.7102, 103.778, -5.10904], [-68.819947, 103.76922, -5.219127], [-68.7102, 103.778, -5.329225], [-68.71898, 103.887747, -5.219127], [-68.7102, 103.778, -5.10904], [-68.7102, 103.778, -15.6056]]}]},
			"L_shoulder_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [6.170406, 146.361529, -2.356082], [9.334275, 146.098273, -4.171483], [10.542769, 145.997718, -4.864906], [5.054907, 146.098273, -11.62954], [-0.75376, 146.361529, -14.423475], [-4.664537, 146.686933, -12.179506], [-5.183609, 146.950189, -5.754767], [-2.112734, 147.050744, 2.396712], [-0.904241, 146.950189, 1.703289], [2.259629, 146.686933, -0.112112], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097]]}]},
			"L_toe_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_CTLShape", "degree": 3, "form": 2, "points": [[13.944556, 5.580432, 10.101116], [9.969202, 7.22696, 10.126118], [5.993848, 5.581134, 10.071928], [4.347206, 1.607048, 9.970289], [5.993848, -2.367329, 9.88074], [9.969202, -4.013857, 9.855738], [13.944556, -2.368031, 9.909928], [15.591198, 1.606055, 10.011567]]}]},
			"C_midTorso_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.869458, 114.394936, -14.358514], [0.0, 114.394936, -16.729695], [-6.869458, 114.394936, -14.358514], [-9.714875, 114.394936, -8.633965], [-6.869458, 114.394936, -2.909417], [0.0, 114.394936, -0.538236], [6.869458, 114.394936, -2.909417], [9.714875, 114.394936, -8.633965]]}]},
			"R_toe_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-9.940376, 1.527856, 17.841151], [-9.830279, 1.4178, 17.838099], [-9.940376, 1.307725, 17.835856], [-10.050472, 1.417781, 17.838907], [-9.940376, 1.527856, 17.841151], [-9.939971, 1.415143, 17.948558], [-9.940376, 1.307725, 17.835856], [-9.94078, 1.420438, 17.728438], [-9.830279, 1.4178, 17.838099], [-9.939971, 1.415143, 17.948558], [-10.050472, 1.417781, 17.838907], [-9.94078, 1.420438, 17.728438], [-9.940376, 1.527856, 17.841151], [-9.939971, 1.415143, 17.948558], [-9.978517, 1.667547, 7.455104]]}, {"shapeName": "R_toe_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.407886, 1.77853, 7.419621], [0.407482, 1.671111, 7.306909], [0.407886, 1.558398, 7.414326], [0.40829, 1.665817, 7.527039], [0.407886, 1.77853, 7.419621], [0.517973, 1.668474, 7.41657], [0.407886, 1.558398, 7.414326], [0.297789, 1.668454, 7.417378], [0.407482, 1.671111, 7.306909], [0.517973, 1.668474, 7.41657], [0.40829, 1.665817, 7.527039], [0.297789, 1.668454, 7.417378], [0.407886, 1.77853, 7.419621], [0.517973, 1.668474, 7.41657], [-9.978517, 1.667547, 7.455104]]}, {"shapeName": "R_toe_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.86842, -8.715913, 7.204942], [-9.978921, -8.713275, 7.095281], [-10.088613, -8.715932, 7.20575], [-9.978112, -8.71857, 7.315411], [-9.86842, -8.715913, 7.204942], [-9.978517, -8.825978, 7.202699], [-10.088613, -8.715932, 7.20575], [-9.978517, -8.605857, 7.207993], [-9.978921, -8.713275, 7.095281], [-9.978517, -8.825978, 7.202699], [-9.978112, -8.71857, 7.315411], [-9.978517, -8.605857, 7.207993], [-9.86842, -8.715913, 7.204942], [-9.978517, -8.825978, 7.202699], [-9.978517, 1.667547, 7.455104]]}]},
			"L_loArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_loArm_FK_CTLShape", "degree": 3, "form": 2, "points": [[36.500788, 121.368595, -20.600804], [39.676814, 123.84031, -22.123499], [42.345412, 126.755918, -20.422635], [42.943348, 128.407493, -16.494545], [41.120367, 127.827572, -12.640254], [37.944341, 125.355857, -11.117559], [35.275743, 122.440249, -12.818424], [34.677807, 120.788674, -16.746514]]}]},
			"R_shoulder_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-5.51861, 146.415763, -1.982087], [-7.627856, 146.240259, -3.192355], [-8.433518, 146.173222, -3.654637], [-4.774944, 146.240259, -8.164392], [-0.902499, 146.415763, -10.027016], [1.704686, 146.632699, -8.531036], [2.050734, 146.808203, -4.247877], [0.003484, 146.87524, 1.186442], [-0.802179, 146.808203, 0.72416], [-2.911425, 146.632699, -0.486107], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097]]}]},
			"L_arm_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[57.210128, 107.556568, -7.578422], [53.084573, 102.836886, -9.273016], [55.551837, 102.836886, -15.279667], [59.677392, 107.556568, -13.585074], [64.043128, 103.09654, -11.791824], [59.917573, 98.376858, -13.486418], [57.450309, 98.376858, -7.479766], [61.575864, 103.09654, -5.785173], [57.210128, 107.556568, -7.578422], [59.677392, 107.556568, -13.585074], [55.551837, 102.836886, -15.279667], [59.917573, 98.376858, -13.486418], [64.043128, 103.09654, -11.791824], [61.575864, 103.09654, -5.785173], [57.450309, 98.376858, -7.479766], [53.084573, 102.836886, -9.273016]]}]},
			"L_upArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[26.45757, 137.863802, -12.512194], [26.553665, 137.918409, -12.402527], [26.487894, 137.823814, -12.297794], [26.391799, 137.769208, -12.407461], [26.45757, 137.863802, -12.512194], [26.54581, 137.765352, -12.429963], [26.487894, 137.823814, -12.297794], [26.399647, 137.922271, -12.380023], [26.553665, 137.918409, -12.402527], [26.54581, 137.765352, -12.429963], [26.391799, 137.769208, -12.407461], [26.399647, 137.922271, -12.380023], [26.45757, 137.863802, -12.512194], [26.54581, 137.765352, -12.429963], [19.577965, 145.245926, -10.049224]]}, {"shapeName": "L_upArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[27.197923, 152.303645, -9.923672], [27.14, 152.362114, -9.791501], [27.228247, 152.263657, -9.709273], [27.286171, 152.205188, -9.841444], [27.197923, 152.303645, -9.923672], [27.294011, 152.358245, -9.814006], [27.228247, 152.263657, -9.709273], [27.132152, 152.20905, -9.81894], [27.14, 152.362114, -9.791501], [27.294011, 152.358245, -9.814006], [27.286171, 152.205188, -9.841444], [27.132152, 152.20905, -9.81894], [27.197923, 152.303645, -9.923672], [27.294011, 152.358245, -9.814006], [19.577965, 145.245926, -10.049224]]}, {"shapeName": "L_upArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[21.089259, 143.434289, 0.066353], [20.935241, 143.438151, 0.088857], [20.927393, 143.285088, 0.061419], [21.081411, 143.281225, 0.038914], [21.089259, 143.434289, 0.066353], [21.023487, 143.339696, 0.171076], [20.927393, 143.285088, 0.061419], [20.993164, 143.379682, -0.043314], [20.935241, 143.438151, 0.088857], [21.023487, 143.339696, 0.171076], [21.081411, 143.281225, 0.038914], [20.993164, 143.379682, -0.043314], [21.089259, 143.434289, 0.066353], [21.023487, 143.339696, 0.171076], [19.577965, 145.245926, -10.049224]]}]},
			"R_loArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_loArm_FK_CTLShape", "degree": 3, "form": 2, "points": [[-36.500788, 121.368595, -20.600804], [-39.676814, 123.84031, -22.123499], [-42.345412, 126.755918, -20.422635], [-42.943348, 128.407493, -16.494545], [-41.120367, 127.827572, -12.640254], [-37.944341, 125.355857, -11.117559], [-35.275743, 122.440249, -12.818424], [-34.677807, 120.788674, -16.746514]]}]},
			"R_arm_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-62.653711, 106.428981, -8.852488], [-62.510061, 106.264644, -8.911493], [-62.32687, 106.392876, -8.98674], [-62.180036, 106.321821, -9.047053], [-62.146503, 106.088679, -9.060826], [-61.937436, 106.082286, -9.146702], [-61.891776, 106.312986, -9.165457], [-61.741465, 106.37499, -9.227198], [-61.565259, 106.235753, -9.299576], [-61.413241, 106.391054, -9.362018], [-61.53187, 106.589112, -9.31329], [-61.466126, 106.74783, -9.340295], [-61.250472, 106.784087, -9.428876], [-61.244558, 107.010104, -9.431305], [-61.457976, 107.059476, -9.343643], [-61.515298, 107.221977, -9.320098], [-61.386517, 107.412455, -9.372995], [-61.530167, 107.576792, -9.31399], [-61.713371, 107.448575, -9.238738], [-61.860205, 107.51963, -9.178425], [-61.893738, 107.752772, -9.164651], [-62.102796, 107.759155, -9.078779], [-62.148479, 107.52845, -9.060015], [-62.298776, 107.466461, -8.99828], [-62.474969, 107.605683, -8.925908], [-62.626986, 107.450382, -8.863465], [-62.508371, 107.252339, -8.912187], [-62.57413, 107.093607, -8.885177], [-62.78976, 107.057354, -8.796605], [-62.795683, 106.831347, -8.794173], [-62.582265, 106.781975, -8.881835], [-62.524943, 106.619474, -8.90538], [-62.653711, 106.428981, -8.852488]]}, {"shapeName": "R_arm_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-62.341045, 106.930529, -8.980917], [-62.240629, 107.17299, -9.022164], [-62.011034, 107.267668, -9.116471], [-61.786775, 107.159101, -9.208587], [-61.699196, 106.910922, -9.24456], [-61.799612, 106.668462, -9.203314], [-62.029207, 106.573783, -9.109006], [-62.253457, 106.68234, -9.016895]]}, {"shapeName": "R_arm_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-61.48925, 106.313404, -9.330797], [-58.56385, 102.966713, -10.53242]]}]},
			"R_arm_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-65.588617, 95.83296, -7.765984], [-65.616732, 95.912981, -7.635411], [-65.504953, 95.83296, -7.562302], [-65.476837, 95.75294, -7.692874], [-65.588617, 95.83296, -7.765984], [-65.620798, 95.757349, -7.633742], [-65.504953, 95.83296, -7.562302], [-65.472765, 95.908579, -7.694547], [-65.616732, 95.912981, -7.635411], [-65.620798, 95.757349, -7.633742], [-65.476837, 95.75294, -7.692874], [-65.472765, 95.908579, -7.694547], [-65.588617, 95.83296, -7.765984], [-65.620798, 95.757349, -7.633742], [-58.56385, 102.966713, -10.53242]]}, {"shapeName": "R_arm_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.204449, 110.515778, -7.923782], [-65.088598, 110.591397, -7.852345], [-65.120786, 110.515778, -7.720101], [-65.236637, 110.44016, -7.791537], [-65.204449, 110.515778, -7.923782], [-65.232559, 110.595792, -7.793213], [-65.120786, 110.515778, -7.720101], [-65.09267, 110.435758, -7.850673], [-65.088598, 110.591397, -7.852345], [-65.232559, 110.595792, -7.793213], [-65.236637, 110.44016, -7.791537], [-65.09267, 110.435758, -7.850673], [-65.204449, 110.515778, -7.923782], [-65.232559, 110.595792, -7.793213], [-58.56385, 102.966713, -10.53242]]}, {"shapeName": "R_arm_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-54.687444, 103.046734, -0.896134], [-54.543477, 103.042331, -0.95527], [-54.547549, 102.886692, -0.953597], [-54.691516, 102.891095, -0.894462], [-54.687444, 103.046734, -0.896134], [-54.575669, 102.966713, -0.823034], [-54.547549, 102.886692, -0.953597], [-54.659328, 102.966713, -1.026707], [-54.543477, 103.042331, -0.95527], [-54.575669, 102.966713, -0.823034], [-54.691516, 102.891095, -0.894462], [-54.659328, 102.966713, -1.026707], [-54.687444, 103.046734, -0.896134], [-54.575669, 102.966713, -0.823034], [-58.56385, 102.966713, -10.53242]]}]},
			"L_legBase_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_CTLShape", "degree": 3, "form": 0, "points": [[9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.420897, -2.827685], [9.978517, 92.076032, 1.182703], [9.978517, 92.326272, 2.714539], [19.532495, 92.076032, 1.182703], [25.437185, 91.420897, -2.827685], [25.437185, 90.611101, -7.784821], [19.532495, 89.955965, -11.795209], [9.978517, 89.705725, -13.327045], [9.978517, 89.955965, -11.795209], [9.978517, 90.611101, -7.784821], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}]},
			"L_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_C_CTLShape", "degree": 3, "form": 2, "points": [[65.048387, 95.785128, -5.838564], [66.153156, 96.450189, -5.898069], [66.742962, 97.310215, -5.13725], [66.472304, 97.861413, -4.001782], [65.499732, 97.780901, -3.156808], [64.394963, 97.11584, -3.097303], [63.805156, 96.255815, -3.858122], [64.075814, 95.704617, -4.993589]]}]},
			"L_shoulder_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [5.735875, 146.397685, -2.106752], [8.196663, 146.19293, -3.518731], [9.136602, 146.114721, -4.05806], [4.868265, 146.19293, -9.319441], [0.350412, 146.397685, -11.492502], [-2.691303, 146.650777, -9.747193], [-3.095025, 146.855532, -4.750174], [-0.706567, 146.933741, 1.589865], [0.233372, 146.855532, 1.050536], [2.69416, 146.650777, -0.361442], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097]]}]},
			"L_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[58.579959, 90.498095, 5.054677], [58.443824, 90.545324, 5.113663], [58.368959, 90.444519, 5.021595], [58.505095, 90.397289, 4.962609], [58.579959, 90.498095, 5.054677], [58.481715, 90.394338, 5.116509], [58.368959, 90.444519, 5.021595], [58.467203, 90.548283, 4.959756], [58.443824, 90.545324, 5.113663], [58.481715, 90.394338, 5.116509], [58.505095, 90.397289, 4.962609], [58.467203, 90.548283, 4.959756], [58.579959, 90.498095, 5.054677], [58.481715, 90.394338, 5.116509], [57.789896, 97.733129, -2.356194]]}, {"shapeName": "L_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[55.005271, 104.74263, 4.785493], [54.892515, 104.792817, 4.690572], [54.794271, 104.689054, 4.752412], [54.907028, 104.638866, 4.847333], [55.005271, 104.74263, 4.785493], [54.869138, 104.789852, 4.844473], [54.794271, 104.689054, 4.752412], [54.930407, 104.641824, 4.693425], [54.892515, 104.792817, 4.690572], [54.869138, 104.789852, 4.844473], [54.907028, 104.638866, 4.847333], [54.930407, 104.641824, 4.693425], [55.005271, 104.74263, 4.785493], [54.869138, 104.789852, 4.844473], [57.789896, 97.733129, -2.356194]]}, {"shapeName": "L_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[47.806504, 95.279999, -3.841107], [47.829883, 95.282957, -3.995015], [47.867775, 95.131964, -3.992162], [47.844396, 95.129005, -3.838254], [47.806504, 95.279999, -3.841107], [47.731649, 95.179196, -3.933174], [47.867775, 95.131964, -3.992162], [47.94264, 95.232769, -3.900094], [47.829883, 95.282957, -3.995015], [47.731649, 95.179196, -3.933174], [47.844396, 95.129005, -3.838254], [47.94264, 95.232769, -3.900094], [47.806504, 95.279999, -3.841107], [47.731649, 95.179196, -3.933174], [57.789896, 97.733129, -2.356194]]}]},
			"R_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_B_CTLShape", "degree": 3, "form": 2, "points": [[-63.414773, 97.794765, -9.685632], [-64.340003, 98.607958, -10.071673], [-65.009331, 99.5603, -9.513637], [-65.030674, 100.093922, -8.338412], [-64.39153, 99.896237, -7.23443], [-63.4663, 99.083044, -6.84839], [-62.796971, 98.130701, -7.406425], [-62.775629, 97.597079, -8.58165]]}]},
			"R_toe_IK_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-12.761265, 4.449263, 7.532235], [-9.978517, 5.601833, 7.549737], [-7.195769, 4.449755, 7.511804], [-6.043119, 1.667894, 7.440656], [-7.195769, -1.114169, 7.377972], [-9.978517, -2.266739, 7.360471], [-12.761265, -1.114661, 7.398404], [-13.913914, 1.667199, 7.469551]]}]},
			"L_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_D_CTLShape", "degree": 3, "form": 2, "points": [[68.139891, 92.543426, -7.630837], [69.222461, 93.171503, -7.946944], [70.049129, 93.938729, -7.318975], [70.135643, 94.395673, -6.114783], [69.431327, 94.274665, -5.039768], [68.348758, 93.646589, -4.723661], [67.522089, 92.879363, -5.35163], [67.435575, 92.422418, -6.555822]]}]},
			"R_toe_IK_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_CTLShape", "degree": 3, "form": 2, "points": [[-13.944556, 5.580432, 10.101116], [-9.969202, 7.22696, 10.126118], [-5.993848, 5.581134, 10.071928], [-4.347206, 1.607048, 9.970289], [-5.993848, -2.367329, 9.88074], [-9.969202, -4.013857, 9.855738], [-13.944556, -2.368031, 9.909928], [-15.591198, 1.606055, 10.011567]]}]},
			"L_toe_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toe_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.940376, 1.527856, 17.841151], [9.830279, 1.4178, 17.838099], [9.940376, 1.307725, 17.835856], [10.050472, 1.417781, 17.838907], [9.940376, 1.527856, 17.841151], [9.939971, 1.415143, 17.948558], [9.940376, 1.307725, 17.835856], [9.94078, 1.420438, 17.728438], [9.830279, 1.4178, 17.838099], [9.939971, 1.415143, 17.948558], [10.050472, 1.417781, 17.838907], [9.94078, 1.420438, 17.728438], [9.940376, 1.527856, 17.841151], [9.939971, 1.415143, 17.948558], [9.978517, 1.667547, 7.455104]]}, {"shapeName": "L_toe_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.407886, 1.77853, 7.419621], [-0.407482, 1.671111, 7.306909], [-0.407886, 1.558398, 7.414326], [-0.40829, 1.665817, 7.527039], [-0.407886, 1.77853, 7.419621], [-0.517973, 1.668474, 7.41657], [-0.407886, 1.558398, 7.414326], [-0.297789, 1.668454, 7.417378], [-0.407482, 1.671111, 7.306909], [-0.517973, 1.668474, 7.41657], [-0.40829, 1.665817, 7.527039], [-0.297789, 1.668454, 7.417378], [-0.407886, 1.77853, 7.419621], [-0.517973, 1.668474, 7.41657], [9.978517, 1.667547, 7.455104]]}, {"shapeName": "L_toe_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.86842, -8.715913, 7.204942], [9.978921, -8.713275, 7.095281], [10.088613, -8.715932, 7.20575], [9.978112, -8.71857, 7.315411], [9.86842, -8.715913, 7.204942], [9.978517, -8.825978, 7.202699], [10.088613, -8.715932, 7.20575], [9.978517, -8.605857, 7.207993], [9.978921, -8.713275, 7.095281], [9.978517, -8.825978, 7.202699], [9.978112, -8.71857, 7.315411], [9.978517, -8.605857, 7.207993], [9.86842, -8.715913, 7.204942], [9.978517, -8.825978, 7.202699], [9.978517, 1.667547, 7.455104]]}]},
			"L_wrist_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_CTLShape", "degree": 3, "form": 2, "points": [[60.959382, 96.592941, -13.846122], [64.110682, 99.482316, -14.331862], [66.010685, 102.371691, -11.771272], [65.546391, 103.568506, -7.664304], [62.989783, 102.371691, -4.416766], [59.838483, 99.482316, -3.931026], [57.938479, 96.592941, -6.491616], [58.402773, 95.396126, -10.598583]]}]},
			"R_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-70.242824, 89.042772, 0.328447], [-70.263657, 89.134893, 0.452232], [-70.128053, 89.086224, 0.511274], [-70.10722, 88.994103, 0.387489], [-70.242824, 89.042772, 0.328447], [-70.237494, 88.982689, 0.471982], [-70.128053, 89.086224, 0.511274], [-70.133378, 89.146315, 0.367734], [-70.263657, 89.134893, 0.452232], [-70.237494, 88.982689, 0.471982], [-70.10722, 88.994103, 0.387489], [-70.133378, 89.146315, 0.367734], [-70.242824, 89.042772, 0.328447], [-70.237494, 88.982689, 0.471982], [-65.2741, 96.783, -4.49769]]}, {"shapeName": "R_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-72.710511, 103.402258, -1.535233], [-72.601065, 103.505801, -1.495947], [-72.595741, 103.44571, -1.352407], [-72.705187, 103.342167, -1.391694], [-72.710511, 103.402258, -1.535233], [-72.731337, 103.494373, -1.411452], [-72.595741, 103.44571, -1.352407], [-72.574908, 103.353589, -1.476191], [-72.601065, 103.505801, -1.495947], [-72.731337, 103.494373, -1.411452], [-72.705187, 103.342167, -1.391694], [-72.574908, 103.353589, -1.476191], [-72.710511, 103.402258, -1.535233], [-72.731337, 103.494373, -1.411452], [-65.2741, 96.783, -4.49769]]}, {"shapeName": "R_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-59.938674, 98.902998, 4.158508], [-59.808395, 98.914419, 4.07401], [-59.782237, 98.762208, 4.093766], [-59.912516, 98.750786, 4.178263], [-59.938674, 98.902998, 4.158508], [-59.803076, 98.854326, 4.217542], [-59.782237, 98.762208, 4.093766], [-59.91784, 98.810877, 4.034724], [-59.808395, 98.914419, 4.07401], [-59.803076, 98.854326, 4.217542], [-59.912516, 98.750786, 4.178263], [-59.91784, 98.810877, 4.034724], [-59.938674, 98.902998, 4.158508], [-59.803076, 98.854326, 4.217542], [-65.2741, 96.783, -4.49769]]}]},
			"C_jaw_CTL": {"color": 18, "shapes": [{"shapeName": "C_jaw_CTLShape", "degree": 3, "form": 0, "points": [[0.0, 165.665077, -3.905633], [0.0, 165.665077, -3.905633], [0.0, 165.665077, -3.905633], [-3.348563, 165.665077, -3.905633], [-8.766626, 165.665077, -3.905633], [-10.836147, 165.665077, -3.905633], [-8.766626, 155.012956, 7.930065], [-3.348563, 148.429577, 15.244936], [3.348563, 148.429577, 15.244936], [8.766626, 155.012956, 7.930065], [10.836147, 165.665077, -3.905633], [8.766626, 165.665077, -3.905633], [3.348563, 165.665077, -3.905633], [0.0, 165.665077, -3.905633], [0.0, 165.665077, -3.905633], [0.0, 165.665077, -3.905633]]}]},
			"R_arm_PV_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_PV_CTLShape", "degree": 1, "form": 0, "points": [[-38.889805, 127.780623, -117.039834], [-38.889805, 125.751363, -117.039834], [-38.889805, 125.751363, -119.069094], [-38.889805, 127.780623, -119.069094], [-40.919065, 127.780623, -119.069094], [-40.919065, 125.751363, -119.069094], [-40.919065, 125.751363, -117.039834], [-40.919065, 127.780623, -117.039834], [-38.889805, 127.780623, -117.039834], [-38.889805, 127.780623, -119.069094], [-38.889805, 125.751363, -119.069094], [-40.919065, 125.751363, -119.069094], [-40.919065, 127.780623, -119.069094], [-40.919065, 127.780623, -117.039834], [-40.919065, 125.751363, -117.039834], [-38.889805, 125.751363, -117.039834]]}]},
			"R_wrist_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-65.588617, 95.83296, -7.765984], [-65.616732, 95.912981, -7.635411], [-65.504953, 95.83296, -7.562302], [-65.476837, 95.75294, -7.692874], [-65.588617, 95.83296, -7.765984], [-65.620798, 95.757349, -7.633742], [-65.504953, 95.83296, -7.562302], [-65.472765, 95.908579, -7.694547], [-65.616732, 95.912981, -7.635411], [-65.620798, 95.757349, -7.633742], [-65.476837, 95.75294, -7.692874], [-65.472765, 95.908579, -7.694547], [-65.588617, 95.83296, -7.765984], [-65.620798, 95.757349, -7.633742], [-58.56385, 102.966713, -10.53242]]}, {"shapeName": "R_wrist_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.204449, 110.515778, -7.923782], [-65.088598, 110.591397, -7.852345], [-65.120786, 110.515778, -7.720101], [-65.236637, 110.44016, -7.791537], [-65.204449, 110.515778, -7.923782], [-65.232559, 110.595792, -7.793213], [-65.120786, 110.515778, -7.720101], [-65.09267, 110.435758, -7.850673], [-65.088598, 110.591397, -7.852345], [-65.232559, 110.595792, -7.793213], [-65.236637, 110.44016, -7.791537], [-65.09267, 110.435758, -7.850673], [-65.204449, 110.515778, -7.923782], [-65.232559, 110.595792, -7.793213], [-58.56385, 102.966713, -10.53242]]}, {"shapeName": "R_wrist_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-54.687444, 103.046734, -0.896134], [-54.543477, 103.042331, -0.95527], [-54.547549, 102.886692, -0.953597], [-54.691516, 102.891095, -0.894462], [-54.687444, 103.046734, -0.896134], [-54.575669, 102.966713, -0.823034], [-54.547549, 102.886692, -0.953597], [-54.659328, 102.966713, -1.026707], [-54.543477, 103.042331, -0.95527], [-54.575669, 102.966713, -0.823034], [-54.691516, 102.891095, -0.894462], [-54.659328, 102.966713, -1.026707], [-54.687444, 103.046734, -0.896134], [-54.575669, 102.966713, -0.823034], [-58.56385, 102.966713, -10.53242]]}]},
			"R_loLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_loLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-9.978517, 41.496164, -0.380045], [-9.868419, 41.513046, -0.48884], [-9.978517, 41.529929, -0.597635], [-10.088614, 41.513046, -0.48884], [-9.978517, 41.496164, -0.380045], [-9.978517, 41.404261, -0.505721], [-9.978517, 41.529929, -0.597635], [-9.978517, 41.621842, -0.471957], [-9.868419, 41.513046, -0.48884], [-9.978517, 41.404261, -0.505721], [-10.088614, 41.513046, -0.48884], [-9.978517, 41.621842, -0.471957], [-9.978517, 41.496164, -0.380045], [-9.978517, 41.404261, -0.505721], [-9.978517, 51.776676, 1.103868]]}, {"shapeName": "R_loLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.407956, 51.759793, 1.212663], [0.407956, 51.885472, 1.120751], [0.407956, 51.793559, 0.995073], [0.407956, 51.667881, 1.086985], [0.407956, 51.759793, 1.212663], [0.518043, 51.776676, 1.103868], [0.407956, 51.793559, 0.995073], [0.297859, 51.776676, 1.103868], [0.407956, 51.885472, 1.120751], [0.518043, 51.776676, 1.103868], [0.407956, 51.667881, 1.086985], [0.297859, 51.776676, 1.103868], [0.407956, 51.759793, 1.212663], [0.518043, 51.776676, 1.103868], [-9.978517, 51.776676, 1.103868]]}, {"shapeName": "R_loLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.868419, 53.369384, -9.159762], [-9.978517, 53.47818, -9.142879], [-10.088614, 53.369384, -9.159762], [-9.978517, 53.260589, -9.176645], [-9.868419, 53.369384, -9.159762], [-9.978517, 53.386265, -9.268547], [-10.088614, 53.369384, -9.159762], [-9.978517, 53.352501, -9.050966], [-9.978517, 53.47818, -9.142879], [-9.978517, 53.386265, -9.268547], [-9.978517, 53.260589, -9.176645], [-9.978517, 53.352501, -9.050966], [-9.868419, 53.369384, -9.159762], [-9.978517, 53.386265, -9.268547], [-9.978517, 51.776676, 1.103868]]}]},
			"C_neckBase_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[8.586823, 153.343453, -15.142039], [0.0, 150.543911, -18.922211], [-8.586823, 153.343453, -15.142039], [-12.143594, 155.099205, -7.302195], [-8.586823, 149.779738, -1.281473], [0.0, 145.50406, 0.679577], [8.586823, 149.779738, -1.281473], [12.143594, 155.099205, -7.302195]]}]},
			"R_shoulder_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-5.735875, 146.397685, -2.106752], [-8.196663, 146.19293, -3.518731], [-9.136602, 146.114721, -4.05806], [-4.868265, 146.19293, -9.319441], [-0.350412, 146.397685, -11.492502], [2.691303, 146.650777, -9.747193], [3.095025, 146.855532, -4.750174], [0.706567, 146.933741, 1.589865], [-0.233372, 146.855532, 1.050536], [-2.69416, 146.650777, -0.361442], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097], [-4.215017, 146.524231, -1.234097]]}]},
			"C_reverseJaw_CTL": {"color": 18, "shapes": [{"shapeName": "C_reverseJaw_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 180.748452, 9.669394], [0.776557, 180.863266, 9.772727], [1.43489, 181.190244, 10.067007], [1.874793, 181.679579, 10.507408], [2.02926, 182.256789, 11.026897], [1.874793, 182.834, 11.546386], [1.43489, 183.323335, 11.986787], [0.776557, 183.650312, 12.281067], [-0.0, 183.765127, 12.3844], [-0.776557, 183.650312, 12.281067], [-1.43489, 183.323335, 11.986787], [-1.874793, 182.834, 11.546386], [-2.02926, 182.256789, 11.026897], [-1.874793, 181.679579, 10.507408], [-1.43489, 181.190244, 10.067007], [-0.776557, 180.863266, 9.772727], [-0.0, 180.748452, 9.669394], [-0.0, 165.665077, -3.905633]]}]},
			"L_toe_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[13.1588, 4.846651, 7.543254], [9.978517, 6.163874, 7.563256], [6.798233, 4.847213, 7.519904], [5.48092, 1.667944, 7.438593], [6.798233, -1.511558, 7.366953], [9.978517, -2.82878, 7.346952], [13.1588, -1.512119, 7.390304], [14.476114, 1.66715, 7.471615]]}]},
			"R_innerBall_CTL": {"color": 20, "shapes": [{"shapeName": "R_innerBall_CTLShape", "degree": 1, "form": 0, "points": [[-3.336185, 1.940984, 8.543172], [-3.330852, 0.905771, 7.549566], [-4.345356, 1.920187, 7.523325], [-3.336185, 1.940984, 8.543172], [-2.316125, 1.920187, 7.534214], [-3.330852, 0.905771, 7.549566], [-3.325297, 1.899391, 6.514367], [-2.316125, 1.920187, 7.534214], [-3.330629, 2.934604, 7.507974], [-3.336185, 1.940984, 8.543172], [-4.345356, 1.920187, 7.523325], [-3.325297, 1.899391, 6.514367], [-3.330629, 2.934604, 7.507974], [-4.345356, 1.920187, 7.523325]]}]},
		}

		controlShapes.set_data(data)