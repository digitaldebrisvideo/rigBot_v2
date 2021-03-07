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
		guide.build("hand", **{'createIkCtrls': False, 'parent': u'L_wrist_end_JNT', 'numberFingers': 4, 'createThumb': True, 'pickWalkParent': u'L_arm_IK_CTL', 'numberThumbJoints': 3, 'numberJoints': 4, 'side': u'L', 'name': u''})
		guide.build("foot", **{'name': u'', 'parent': u'L_leg_end_JNT', 'switchCtrlDriver': u'L_leg_IK_switch_CTL', 'attrCtrlDriver': u'L_leg_IK_CTL', 'ikCtrlParent': u'L_leg_IK_handle_driver_JNT', 'pickWalkParent': u'L_leg_PV_CTL', 'fkCtrlParent': u'L_legEnd_FK_CTL', 'side': u'L'})
		guide.build("bipedLeg", **{'flipJoints': False, 'name': u'', 'parent': u'C_hip_JNT', 'transOrientiation': u'world', 'fkAnkleJoint': u'L_ankle_JNT', 'side': u'L', 'pickWalkParent': u'C_hip_CTL', 'ikHandleParent': u'L_foot_IK_handle_driver_JNT', 'numberTwistJoints': 4, 'makeBendy': False})
		guide.build("bipedArm", **{'name': u'', 'parent': u'C_chest_JNT', 'transOrientiation': u'world', 'numberTwistJoints': 4, 'side': u'L', 'pickWalkParent': u'C_chest_CTL', 'doubleClavicle': False, 'ikHandleParent': u'', 'makeBendy': False})
		guide.build("torso", **{'numberMidCtrls': 1, 'parent': u'C_root_JNT', 'pickWalkParent': u'world_CTL', 'numberJoints': 6, 'side': u'C', 'name': u''})
		guide.build("neck", **{'numberMidCtrls': 1, 'parent': u'C_chest_end_JNT', 'pickWalkParent': u'C_chest_CTL', 'createReverseJaw': True, 'name': u'', 'numberJoints': 4, 'side': u'C', 'createJaw': True})
		guide.build("eyeLookAt", **{'pickWalkParent': u'C_head_CTL', 'side': u'C', 'parent': u'C_head_JNT', 'name': u''})

		#Position nodes
		if mc.objExists("L_hand_guide"):
			if not mc.getAttr("L_hand_guide.rotateOrder", l=1):
				mc.setAttr("L_hand_guide.rotateOrder", 0)

			mc.xform("L_hand_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_hand_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_hand_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_foot_guide"):
			if not mc.getAttr("L_foot_guide.rotateOrder", l=1):
				mc.setAttr("L_foot_guide.rotateOrder", 0)

			mc.xform("L_foot_guide", a=1, t=[9.978516578674316, 7.470623970031738, -5.771536350250244])
			mc.xform("L_foot_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_foot_guide", r=1, s=[10.0, 10.0, 10.0])

		if mc.objExists("L_bipedLeg_guide"):
			if not mc.getAttr("L_bipedLeg_guide.rotateOrder", l=1):
				mc.setAttr("L_bipedLeg_guide.rotateOrder", 0)

			mc.xform("L_bipedLeg_guide", a=1, t=[9.978516578674316, 91.01599884033203, -5.306252956390381])
			mc.xform("L_bipedLeg_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bipedLeg_guide", r=1, s=[10.0, 10.0, 10.0])

		if mc.objExists("L_bipedArm_guide"):
			if not mc.getAttr("L_bipedArm_guide.rotateOrder", l=1):
				mc.setAttr("L_bipedArm_guide.rotateOrder", 0)

			mc.xform("L_bipedArm_guide", a=1, t=[4.215017318725586, 146.52423095703125, -1.2340972423553467])
			mc.xform("L_bipedArm_guide", a=1, ro=[0.0, 0.0, -47.95283676159287])
			mc.xform("L_bipedArm_guide", r=1, s=[8.0, 8.0, 8.0])

		if mc.objExists("C_worldRoot_guide"):
			if not mc.getAttr("C_worldRoot_guide.rotateOrder", l=1):
				mc.setAttr("C_worldRoot_guide.rotateOrder", 0)

			mc.xform("C_worldRoot_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_guide"):
			if not mc.getAttr("C_torso_guide.rotateOrder", l=1):
				mc.setAttr("C_torso_guide.rotateOrder", 0)

			mc.xform("C_torso_guide", a=1, t=[-1.4409554511037857e-15, 101.1834974909765, -8.633965683161994])
			mc.xform("C_torso_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("C_neck_guide"):
			if not mc.getAttr("C_neck_guide.rotateOrder", l=1):
				mc.setAttr("C_neck_guide.rotateOrder", 0)

			mc.xform("C_neck_guide", a=1, t=[1.3155039101177777e-14, 151.5544678363174, -8.213586532159582])
			mc.xform("C_neck_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_guide", r=1, s=[5.0, 5.0, 5.0])

		if mc.objExists("C_eyeLookAt_guide"):
			if not mc.getAttr("C_eyeLookAt_guide.rotateOrder", l=1):
				mc.setAttr("C_eyeLookAt_guide.rotateOrder", 0)

			mc.xform("C_eyeLookAt_guide", a=1, t=[0.0, 168.9251316618315, 70.92878317499147])
			mc.xform("C_eyeLookAt_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_eyeLookAt_guide", r=1, s=[10.0, 10.0, 10.0])

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

			mc.xform("C_chest_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_chest_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

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

			mc.xform("C_jaw_end_JNT_PLC", a=1, t=[-1.7255591543290751e-15, -0.3682339757162083, -1.2457523318479686])
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

			mc.xform("C_head_JNT_PLC", a=1, t=[0.5243264924371047, -5.193556190653456e-16, 0.6490339178361595])
			mc.xform("C_head_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_reverseJaw_JNT_PLC"):
			mc.xform("C_reverseJaw_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_JNT_PLC"):
			if not mc.getAttr("L_shoulder_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_shoulder_JNT_PLC.rotateOrder", 0)

			mc.xform("L_shoulder_JNT_PLC", a=1, t=[-0.5, 0.0, 0.0])
			mc.xform("L_shoulder_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_JNT_PLC"):
			if not mc.getAttr("L_upArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_JNT_PLC", a=1, t=[-0.5951907367698599, 1.3190368074610799, -1.1018908321857452])
			mc.xform("L_upArm_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_JNT_PLC"):
			if not mc.getAttr("L_loArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_JNT_PLC", a=1, t=[0.9315404713384527, 1.3756979387385915, -1.4233039915561676])
			mc.xform("L_loArm_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_JNT_PLC"):
			if not mc.getAttr("L_wrist_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_wrist_JNT_PLC.rotateOrder", 0)

			mc.xform("L_wrist_JNT_PLC", a=1, t=[2.5931554375219354, 1.3983501913743623, -1.1622903645038605])
			mc.xform("L_wrist_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_end_JNT_PLC"):
			if not mc.getAttr("L_wrist_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_wrist_end_JNT_PLC.rotateOrder", 0)

			mc.xform("L_wrist_end_JNT_PLC", a=1, t=[2.7394395338559834, 1.424767829228852, -0.976439505815506])
			mc.xform("L_wrist_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_handle_driver_JNT_PLC"):
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_A_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_A_JNT_PLC", a=1, t=[2.1101555048518, 1.3303690337165843, -1.2661734640598297])
			mc.xform("L_upArm_twist_A_JNT_PLC", a=1, ro=[1.3184189669996418, 13.109417753283822, 0.9204456505709763])
			mc.xform("L_upArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_A_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_A_JNT_PLC", a=1, t=[5.663863464575146, 1.3802283892657492, -1.7711012661457062])
			mc.xform("L_loArm_twist_A_JNT_PLC", a=1, ro=[1.311496672220964, -11.740731295960693, 0.3544506802418045])
			mc.xform("L_loArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_B_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_B_JNT_PLC", a=1, t=[2.815501746473462, 1.341701259972087, -1.430456095933914])
			mc.xform("L_upArm_twist_B_JNT_PLC", a=1, ro=[1.3184189669996418, 13.109417753283822, 0.9204456505709763])
			mc.xform("L_upArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_B_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_B_JNT_PLC", a=1, t=[6.396186457811842, 1.3847588397929016, -1.6188985407352448])
			mc.xform("L_loArm_twist_B_JNT_PLC", a=1, ro=[1.311496672220964, -11.740731295960693, 0.3544506802418045])
			mc.xform("L_loArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_C_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_C_JNT_PLC", a=1, t=[3.5208479880951256, 1.353033486227588, -1.5947387278079987])
			mc.xform("L_upArm_twist_C_JNT_PLC", a=1, ro=[1.3184189669996418, 13.109417753283822, 0.9204456505709763])
			mc.xform("L_upArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_C_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_C_JNT_PLC", a=1, t=[7.12850945104854, 1.3892892903200558, -1.4666958153247833])
			mc.xform("L_loArm_twist_C_JNT_PLC", a=1, ro=[1.311496672220964, -11.740731295960693, 0.3544506802418045])
			mc.xform("L_loArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_D_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_D_JNT_PLC", a=1, t=[4.226194229716787, 1.3643657124830888, -1.7590213596820832])
			mc.xform("L_upArm_twist_D_JNT_PLC", a=1, ro=[1.3184189669996418, 13.109417753283822, 0.9204456505709763])
			mc.xform("L_upArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_D_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_D_JNT_PLC", a=1, t=[7.860832444285234, 1.39381974084721, -1.314493089914322])
			mc.xform("L_loArm_twist_D_JNT_PLC", a=1, ro=[1.311496672220964, -11.740731295960693, 0.3544506802418045])
			mc.xform("L_loArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_B_JNT_PLC"):
			if not mc.getAttr("L_thumb_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_B_JNT_PLC", a=1, t=[4.477307001749679, -0.04999999999994742, -1.7053025658242404e-13])
			mc.xform("L_thumb_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_C_JNT_PLC"):
			if not mc.getAttr("L_thumb_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_C_JNT_PLC", a=1, t=[7.70190323116276, -1.453329119008636, -0.09334876856985375])
			mc.xform("L_thumb_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_D_JNT_PLC"):
			if not mc.getAttr("L_thumb_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_D_JNT_PLC", a=1, t=[9.988393240501566, -2.5980201926672706, -0.11556171137432614])
			mc.xform("L_thumb_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_A_JNT_PLC"):
			if not mc.getAttr("L_thumb_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_A_JNT_PLC", a=1, t=[45.51747878658912, 19.31664442045096, -105.87133997049058])
			mc.xform("L_thumb_A_JNT_PLC", a=1, ro=[-41.95659080235949, -58.80108123374743, 35.13990306113987])
			mc.xform("L_thumb_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_B_JNT_PLC"):
			if not mc.getAttr("L_index_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_B_JNT_PLC", a=1, t=[6.101062297821059, -0.04999999998288729, -3.6414604664969374e-10])
			mc.xform("L_index_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_C_JNT_PLC"):
			if not mc.getAttr("L_index_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_C_JNT_PLC", a=1, t=[10.248632093759262, -0.7858642611868447, -0.08238781392407901])
			mc.xform("L_index_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_D_JNT_PLC"):
			if not mc.getAttr("L_index_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_D_JNT_PLC", a=1, t=[12.465946737482298, -1.8145966434796605, -0.15828843929600467])
			mc.xform("L_index_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_E_JNT_PLC"):
			if not mc.getAttr("L_index_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_E_JNT_PLC", a=1, t=[13.67824500008481, -3.154604287950292, -0.2376100753033512])
			mc.xform("L_index_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_A_JNT_PLC"):
			if not mc.getAttr("L_index_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_A_JNT_PLC", a=1, t=[60.461837847908704, 101.4665726839735, -8.7247695703061])
			mc.xform("L_index_A_JNT_PLC", a=1, ro=[17.0936718840093, -29.695891256926767, -52.56674322415862])
			mc.xform("L_index_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_B_JNT_PLC"):
			if not mc.getAttr("L_middle_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_B_JNT_PLC", a=1, t=[5.910159587860107, -0.04999999977157188, -3.46270567774809e-10])
			mc.xform("L_middle_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_C_JNT_PLC"):
			if not mc.getAttr("L_middle_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_C_JNT_PLC", a=1, t=[9.96160001803397, -0.982033758052637, -0.15042356182737748])
			mc.xform("L_middle_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_D_JNT_PLC"):
			if not mc.getAttr("L_middle_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_D_JNT_PLC", a=1, t=[12.5424120031523, -2.26226709398307, -0.3274348484127749])
			mc.xform("L_middle_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_E_JNT_PLC"):
			if not mc.getAttr("L_middle_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_E_JNT_PLC", a=1, t=[14.411657730800641, -3.6633109718888477, -0.5110364283043687])
			mc.xform("L_middle_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_A_JNT_PLC"):
			if not mc.getAttr("L_middle_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_A_JNT_PLC", a=1, t=[60.84565205427198, 101.21601069617124, -9.570425907957183])
			mc.xform("L_middle_A_JNT_PLC", a=1, ro=[5.6583928521657105, -16.213196122326156, -48.07312064095242])
			mc.xform("L_middle_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_B_JNT_PLC"):
			if not mc.getAttr("L_ring_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_B_JNT_PLC", a=1, t=[5.110830307006832, -0.05000000001813021, -1.9524826200267853e-10])
			mc.xform("L_ring_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_C_JNT_PLC"):
			if not mc.getAttr("L_ring_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_C_JNT_PLC", a=1, t=[9.175456823342206, -0.9080347507182154, -0.8835494935346873])
			mc.xform("L_ring_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_D_JNT_PLC"):
			if not mc.getAttr("L_ring_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_D_JNT_PLC", a=1, t=[11.572343650021324, -2.057954304010252, -1.4327363519495275])
			mc.xform("L_ring_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_E_JNT_PLC"):
			if not mc.getAttr("L_ring_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_E_JNT_PLC", a=1, t=[13.11680119895582, -3.7332404622696345, -1.8008667319875329])
			mc.xform("L_ring_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_A_JNT_PLC"):
			if not mc.getAttr("L_ring_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_A_JNT_PLC", a=1, t=[61.110888829033456, 100.97987402441672, -11.038917751360374])
			mc.xform("L_ring_A_JNT_PLC", a=1, ro=[1.3110939993576876, -8.988731512360912, -46.91605945953415])
			mc.xform("L_ring_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_B_JNT_PLC"):
			if not mc.getAttr("L_pinky_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_B_JNT_PLC", a=1, t=[4.261646270751953, -0.04999999999981242, 1.1723955140041653e-13])
			mc.xform("L_pinky_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_C_JNT_PLC"):
			if not mc.getAttr("L_pinky_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_C_JNT_PLC", a=1, t=[7.096459001641577, -0.45485338108461804, -0.9991404737552791])
			mc.xform("L_pinky_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_D_JNT_PLC"):
			if not mc.getAttr("L_pinky_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_D_JNT_PLC", a=1, t=[9.009942430535663, -1.2130825729104942, -1.7293446285479774])
			mc.xform("L_pinky_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_E_JNT_PLC"):
			if not mc.getAttr("L_pinky_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_E_JNT_PLC", a=1, t=[10.385492462622683, -2.209449728776221, -2.303100909921401])
			mc.xform("L_pinky_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_A_JNT_PLC"):
			if not mc.getAttr("L_pinky_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_A_JNT_PLC", a=1, t=[61.2476862114068, 101.03642283406431, -12.229156773938438])
			mc.xform("L_pinky_A_JNT_PLC", a=1, ro=[3.246079919334916, 0.14040009945875195, -51.84243628604861])
			mc.xform("L_pinky_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_JNT_PLC"):
			if not mc.getAttr("L_upLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_JNT_PLC"):
			if not mc.getAttr("L_loLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_JNT_PLC", a=1, t=[0.0, 0.07606773376464826, 0.14101209640502932])
			mc.xform("L_loLeg_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_end_JNT_PLC"):
			if not mc.getAttr("L_leg_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_leg_end_JNT_PLC.rotateOrder", 0)

			mc.xform("L_leg_end_JNT_PLC", a=1, t=[0.0, -0.3545374870300292, -0.04652833938598644])
			mc.xform("L_leg_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_handle_driver_JNT_PLC"):
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_A_JNT_PLC", a=1, t=[0.0, -0.7847864532470705, 0.12820241928100579])
			mc.xform("L_upLeg_twist_A_JNT_PLC", a=1, ro=[-179.99999999999997, -9.27786536180147, -90.0])
			mc.xform("L_upLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_A_JNT_PLC", a=1, t=[0.0, -4.810053310394288, 0.5035040092468261])
			mc.xform("L_loLeg_twist_A_JNT_PLC", a=1, ro=[2.5444437451708134e-14, 171.1792071530017, 89.99999999999999])
			mc.xform("L_loLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_B_JNT_PLC", a=1, t=[0.0, -1.5695729064941428, 0.25640483856201174])
			mc.xform("L_upLeg_twist_B_JNT_PLC", a=1, ro=[-179.99999999999997, -9.27786536180147, -90.0])
			mc.xform("L_upLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_B_JNT_PLC", a=1, t=[0.0, -5.696174354553223, 0.36599592208862297])
			mc.xform("L_loLeg_twist_B_JNT_PLC", a=1, ro=[2.5444437451708134e-14, 171.1792071530017, 89.99999999999999])
			mc.xform("L_loLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_C_JNT_PLC", a=1, t=[0.0, -2.3543593597412116, 0.38460725784301764])
			mc.xform("L_upLeg_twist_C_JNT_PLC", a=1, ro=[-179.99999999999997, -9.27786536180147, -90.0])
			mc.xform("L_upLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_C_JNT_PLC", a=1, t=[0.0, -6.5822953987121595, 0.22848783493041974])
			mc.xform("L_loLeg_twist_C_JNT_PLC", a=1, ro=[2.5444437451708134e-14, 171.1792071530017, 89.99999999999999])
			mc.xform("L_loLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_D_JNT_PLC", a=1, t=[0.0, -3.139145812988283, 0.5128096771240235])
			mc.xform("L_upLeg_twist_D_JNT_PLC", a=1, ro=[-179.99999999999997, -9.27786536180147, -90.0])
			mc.xform("L_upLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_D_JNT_PLC", a=1, t=[0.0, -7.468416442871095, 0.09097974777221673])
			mc.xform("L_loLeg_twist_D_JNT_PLC", a=1, ro=[2.5444437451708134e-14, 171.1792071530017, 89.99999999999999])
			mc.xform("L_loLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

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

			mc.xform("L_ball_JNT_PLC", a=1, t=[0.3226640347313053, 2.7121371148908224e-08, 0.0803077131705324])
			mc.xform("L_ball_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ball_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_JNT_PLC"):
			if not mc.getAttr("L_toe_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_toe_JNT_PLC.rotateOrder", 0)

			mc.xform("L_toe_JNT_PLC", a=1, t=[-0.025947089699422055, 2.7121371148908224e-08, 0.10199925954146746])
			mc.xform("L_toe_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

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
			mc.xform("L_innerBall_PIV_CTL", a=1, ro=[2.625852505250962, -6.846365605409033e-07, -4.222434064431299e-07])
			mc.xform("L_innerBall_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterBall_PIV_CTL"):
			mc.xform("L_outterBall_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterBall_PIV_CTL", a=1, ro=[2.625852505250962, -6.846365605409033e-07, -4.222434064431299e-07])
			mc.xform("L_outterBall_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_heel_PIV_CTL"):
			mc.xform("L_heel_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_heel_PIV_CTL", a=1, ro=[2.625852505250962, -6.846365605409033e-07, -4.222434064431299e-07])
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

		if mc.objExists("C_lookAt_PIV_CTL"):
			mc.xform("C_lookAt_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

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
			mc.xform("world_CTL", r=1, s=[9.915726840055477, 9.915726840055477, 9.915726840055477])

		if mc.objExists("visibility_CTL"):
			if not mc.getAttr("visibility_CTL.mirrorMode", l=1):
				mc.setAttr("visibility_CTL.mirrorMode", 0)

			if not mc.getAttr("visibility_CTL.rotateOrder", l=1):
				mc.setAttr("visibility_CTL.rotateOrder", 0)

			mc.xform("visibility_CTL", a=1, t=[1.143847136726802e-12, 21.764305266882022, -16.70461776250204])
			mc.xform("visibility_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("visibility_CTL", r=1, s=[20.12277163567045, 20.12277163567045, 20.12277163567045])

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
			mc.xform("C_chest_CTL", r=1, s=[3.0, 3.0, 3.0])

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
			mc.xform("C_hip_CTL", r=1, s=[3.0, 3.0, 3.0])

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
			mc.xform("C_midTorso_CTL", r=1, s=[3.1465163235035054, 3.1465163235035054, 3.1465163235035054])

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

			mc.xform("C_head_CTL", a=1, t=[0.0, 1.4745663873675312, 0.0])
			mc.xform("C_head_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_CTL", r=1, s=[2.5267660813489603, 2.375562143567343, 2.375562143567343])

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
			mc.xform("C_neckBase_CTL", r=1, s=[2.862762507143083, 2.862762507143083, 2.862762507143083])

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
			mc.xform("C_midNeck_CTL", r=1, s=[2.081056679465288, 2.081056679465288, 2.081056679465288])

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
			mc.xform("L_loArm_FK_CTL", r=1, s=[2.895992431831707, 2.895992431831707, 2.895992431831707])

		if mc.objExists("L_wrist_FK_CTL"):
			if not mc.getAttr("L_wrist_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_wrist_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_wrist_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_wrist_FK_CTL.rotateOrder", 0)

			mc.xform("L_wrist_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_FK_CTL", r=1, s=[1.637233025949941, 1.637233025949941, 1.637233025949941])

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
			mc.xform("L_arm_IK_A_OFF_CTL", r=1, s=[1.637233025949941, 1.637233025949941, 1.637233025949941])

		if mc.objExists("L_arm_IK_CTL"):
			if not mc.getAttr("L_arm_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_arm_IK_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("L_arm_IK_CTL.mirrorMode", l=1):
				mc.setAttr("L_arm_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_arm_IK_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_IK_CTL.rotateOrder", 0)

			mc.xform("L_arm_IK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_CTL", r=1, s=[0.13102474154967886, 1.637233025949941, 1.637233025949941])

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
			mc.xform("L_wrist_IK_CTL", r=1, s=[1.637233025949941, 1.637233025949941, 1.637233025949941])

		if mc.objExists("L_arm_PV_CTL"):
			if not mc.getAttr("L_arm_PV_CTL.mirrorMode", l=1):
				mc.setAttr("L_arm_PV_CTL.mirrorMode", 0)

			if not mc.getAttr("L_arm_PV_CTL.rotateOrder", l=1):
				mc.setAttr("L_arm_PV_CTL.rotateOrder", 0)

			mc.xform("L_arm_PV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_PV_CTL", a=1, ro=[-1.2243747576593071, 0.6177092716240801, 47.3194775506901])
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
			mc.xform("L_shoulder_CTL", r=1, s=[2.8420583821791507, 2.8420583821791507, 1.8315415047775745])

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
			mc.xform("L_arm_IK_switch_CTL", a=1, ro=[0.0, 0.0, 27.335281570891485])
			mc.xform("L_arm_IK_switch_CTL", r=1, s=[3.1643279129525945, 3.1643279129525945, 3.1643279129525945])

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

			mc.xform("L_hand_CTL", a=1, t=[71.12251072381608, 111.33201316933635, 0.0])
			mc.xform("L_hand_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_hand_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_upLeg_FK_CTL"):
			if not mc.getAttr("L_upLeg_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_upLeg_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upLeg_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_FK_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_FK_CTL", r=1, s=[2.6515592796098764, 2.6515592796098764, 2.6515592796098764])

		if mc.objExists("L_loLeg_FK_CTL"):
			if not mc.getAttr("L_loLeg_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_loLeg_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loLeg_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_FK_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_FK_CTL", r=1, s=[1.9101154353046517, 1.9101154353046517, 1.9101154353046517])

		if mc.objExists("L_legEnd_FK_CTL"):
			if not mc.getAttr("L_legEnd_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_legEnd_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_legEnd_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_legEnd_FK_CTL.rotateOrder", 0)

			mc.xform("L_legEnd_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legEnd_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legEnd_FK_CTL", r=1, s=[2.1345102888423235, 2.1345102888423235, 2.1345102888423235])

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
			mc.xform("L_legBase_CTL", r=1, s=[2.4518717816262168, 2.4518717816262168, 2.4518717816262168])

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
			mc.xform("L_leg_IK_switch_CTL", r=1, s=[3.1826839668621654, 3.1826839668621654, 3.1826839668621654])

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
			mc.xform("L_ankleOffset_CTL", r=1, s=[1.496047991514163, 1.496047991514163, 1.496047991514163])

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

		if mc.objExists("C_lookAt_D_OFF_CTL"):
			if not mc.getAttr("C_lookAt_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lookAt_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lookAt_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lookAt_C_OFF_CTL"):
			if not mc.getAttr("C_lookAt_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lookAt_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lookAt_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lookAt_B_OFF_CTL"):
			if not mc.getAttr("C_lookAt_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lookAt_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lookAt_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lookAt_A_OFF_CTL"):
			if not mc.getAttr("C_lookAt_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lookAt_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lookAt_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lookAt_CTL"):
			if not mc.getAttr("C_lookAt_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_lookAt_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_lookAt_CTL.mirrorMode", l=1):
				mc.setAttr("C_lookAt_CTL.mirrorMode", 0)

			if not mc.getAttr("C_lookAt_CTL.rotateOrder", l=1):
				mc.setAttr("C_lookAt_CTL.rotateOrder", 0)

			mc.xform("C_lookAt_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_CTL", r=1, s=[1.0, 1.0, 1.0])

		# Apply contro shapes data
		data = {
			"C_cog_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_CTLShape", "degree": 1, "form": 0, "points": [[29.97882, 98.683497, -6.476546], [29.9472, 98.683497, -11.192816], [21.80913, 98.683497, -14.024636], [20.697, 98.683497, -17.371316], [25.52145, 98.683497, -24.509696], [22.72374, 98.683497, -28.306646], [14.47416, 98.683497, -25.819226], [11.60811, 98.683497, -27.873176], [11.31579, 98.683497, -36.478826], [6.82056, 98.683497, -37.906196], [1.61055, 98.683497, -31.049606], [-1.91469, 98.683497, -31.026296], [-7.21215, 98.683497, -37.812176], [-11.68782, 98.683497, -36.324716], [-11.86824, 98.683497, -27.717986], [-14.70615, 98.683497, -25.626326], [-22.98528, 98.683497, -28.000436], [-25.73187, 98.683497, -24.166316], [-20.81376, 98.683497, -17.096906], [-21.88035, 98.683497, -13.735856], [-29.97882, 98.683497, -10.791386], [-29.9472, 98.683497, -6.075116], [-21.80913, 98.683497, -3.243296], [-20.697, 98.683497, 0.103384], [-25.52145, 98.683497, 7.241764], [-22.72374, 98.683497, 11.038714], [-14.47416, 98.683497, 8.551294], [-11.60811, 98.683497, 10.605244], [-11.31579, 98.683497, 19.210894], [-6.82056, 98.683497, 20.638264], [-1.61055, 98.683497, 13.781674], [1.91469, 98.683497, 13.758364], [7.21215, 98.683497, 20.544244], [11.68782, 98.683497, 19.056784], [11.86824, 98.683497, 10.450054], [14.70615, 98.683497, 8.358394], [22.98528, 98.683497, 10.732504], [25.73187, 98.683497, 6.898384], [20.81376, 98.683497, -0.171026], [21.88035, 98.683497, -3.532076], [29.97882, 98.683497, -6.476546]]}]},
			"L_wrist_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[56.381143, 99.261663, -14.43344], [59.638512, 101.775154, -16.112277], [62.26636, 104.986643, -14.522516], [62.725325, 107.014883, -10.595407], [60.746558, 106.671763, -6.631401], [57.489189, 104.158272, -4.952563], [54.86134, 100.946783, -6.542325], [54.402376, 98.918543, -10.469434]]}]},
			"L_leg_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_CTLShape", "degree": 3, "form": 2, "points": [[15.855607, 7.470624, -15.566686], [9.978517, 7.470624, -19.623961], [4.101427, 7.470624, -15.566686], [1.667062, 7.470624, -5.771536], [4.101427, 7.470624, 4.023614], [9.978517, 7.470624, 8.080889], [15.855607, 7.470624, 4.023614], [18.289972, 7.470624, -5.771536]]}]},
			"L_outterBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_outterBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[25.215227, 2.475595, 4.120068], [25.215227, 2.57902, 4.233435], [25.215227, 2.465653, 4.33686], [25.215227, 2.362228, 4.223492], [25.215227, 2.475595, 4.120068], [25.323727, 2.470624, 4.228464], [25.215227, 2.465653, 4.33686], [25.106717, 2.470624, 4.228464], [25.215227, 2.57902, 4.233435], [25.323727, 2.470624, 4.228464], [25.215227, 2.362228, 4.223492], [25.106717, 2.470624, 4.228464], [25.215227, 2.475595, 4.120068], [25.323727, 2.470624, 4.228464], [14.978517, 2.470624, 4.228464]]}, {"shapeName": "L_outterBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[14.978517, 12.701557, 4.589049], [14.870007, 12.696585, 4.697446], [14.978517, 12.691614, 4.805842], [15.087027, 12.696585, 4.697446], [14.978517, 12.701557, 4.589049], [14.978517, 12.804971, 4.702416], [14.978517, 12.691614, 4.805842], [14.978517, 12.588189, 4.692474], [14.870007, 12.696585, 4.697446], [14.978517, 12.804971, 4.702416], [15.087027, 12.696585, 4.697446], [14.978517, 12.588189, 4.692474], [14.978517, 12.701557, 4.589049], [14.978517, 12.804971, 4.702416], [14.978517, 2.470624, 4.228464]]}, {"shapeName": "L_outterBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[14.978517, 2.110038, 14.459396], [14.870007, 2.001642, 14.454425], [14.978517, 1.893246, 14.449454], [15.087027, 2.001642, 14.454425], [14.978517, 2.110038, 14.459396], [14.978517, 1.996671, 14.562811], [14.978517, 1.893246, 14.449454], [14.978517, 2.006613, 14.346029], [14.870007, 2.001642, 14.454425], [14.978517, 1.996671, 14.562811], [15.087027, 2.001642, 14.454425], [14.978517, 2.006613, 14.346029], [14.978517, 2.110038, 14.459396], [14.978517, 1.996671, 14.562811], [14.978517, 2.470624, 4.228464]]}]},
			"C_torso_FK_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 106.315182, -8.688221], [-0.054255, 106.315182, -8.633966], [-0.0, 106.315182, -8.579711], [0.054255, 106.315182, -8.633966], [-0.0, 106.315182, -8.688221], [-0.0, 106.369432, -8.633966], [-0.0, 106.315182, -8.579711], [-0.0, 106.260927, -8.633966], [-0.054255, 106.315182, -8.633966], [-0.0, 106.369432, -8.633966], [0.054255, 106.315182, -8.633966], [-0.0, 106.260927, -8.633966], [-0.0, 106.315182, -8.688221], [-0.0, 106.369432, -8.633966], [-0.0, 101.196827, -8.633966]]}, {"shapeName": "C_torso_FK_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 101.196827, -8.688221], [-5.118355, 101.142572, -8.633966], [-5.118355, 101.196827, -8.579711], [-5.118355, 101.251082, -8.633966], [-5.118355, 101.196827, -8.688221], [-5.172605, 101.196827, -8.633966], [-5.118355, 101.196827, -8.579711], [-5.0641, 101.196827, -8.633966], [-5.118355, 101.142572, -8.633966], [-5.172605, 101.196827, -8.633966], [-5.118355, 101.251082, -8.633966], [-5.0641, 101.196827, -8.633966], [-5.118355, 101.196827, -8.688221], [-5.172605, 101.196827, -8.633966], [-0.0, 101.196827, -8.633966]]}, {"shapeName": "C_torso_FK_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 101.196827, -3.515611], [-0.0, 101.142572, -3.515611], [0.054255, 101.196827, -3.515611], [-0.0, 101.251082, -3.515611], [-0.054255, 101.196827, -3.515611], [-0.0, 101.196827, -3.461361], [0.054255, 101.196827, -3.515611], [-0.0, 101.196827, -3.569866], [-0.0, 101.142572, -3.515611], [-0.0, 101.196827, -3.461361], [-0.0, 101.251082, -3.515611], [-0.0, 101.196827, -3.569866], [-0.054255, 101.196827, -3.515611], [-0.0, 101.196827, -3.461361], [-0.0, 101.196827, -8.633966]]}]},
			"L_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_A_CTLShape", "degree": 3, "form": 2, "points": [[60.694294, 101.361497, -8.602376], [60.79848, 101.43377, -8.612789], [60.851912, 101.525259, -8.542352], [60.82329, 101.58237, -8.432326], [60.729381, 101.571649, -8.347163], [60.625196, 101.499375, -8.336751], [60.571764, 101.407887, -8.407187], [60.600385, 101.350775, -8.517213]]}]},
			"L_toe_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toe_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978516, 1.435298, 17.689754], [9.870006, 1.326849, 17.686143], [9.978516, 1.218399, 17.682531], [10.087026, 1.326849, 17.686143], [9.978516, 1.435298, 17.689754], [9.978516, 1.323237, 17.794583], [9.978516, 1.218399, 17.682531], [9.978516, 1.33046, 17.577693], [9.870006, 1.326849, 17.686143], [9.978516, 1.323237, 17.794583], [10.087026, 1.326849, 17.686143], [9.978516, 1.33046, 17.577693], [9.978516, 1.435298, 17.689754], [9.978516, 1.323237, 17.794583], [9.978516, 1.667547, 7.455104]]}, {"shapeName": "L_toe_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.258194, 1.775997, 7.458715], [-0.258194, 1.671158, 7.346654], [-0.258194, 1.559097, 7.451492], [-0.258194, 1.663935, 7.563554], [-0.258194, 1.775997, 7.458715], [-0.366694, 1.667547, 7.455104], [-0.258194, 1.559097, 7.451492], [-0.149684, 1.667547, 7.455104], [-0.258194, 1.671158, 7.346654], [-0.366694, 1.667547, 7.455104], [-0.258194, 1.663935, 7.563554], [-0.149684, 1.667547, 7.455104], [-0.258194, 1.775997, 7.458715], [-0.366694, 1.667547, 7.455104], [9.978516, 1.667547, 7.455104]]}, {"shapeName": "L_toe_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.870006, -8.563492, 7.114406], [9.978516, -8.559881, 7.005956], [10.087026, -8.563492, 7.114406], [9.978516, -8.567103, 7.222856], [9.870006, -8.563492, 7.114406], [9.978516, -8.671932, 7.110795], [10.087026, -8.563492, 7.114406], [9.978516, -8.455042, 7.118017], [9.978516, -8.559881, 7.005956], [9.978516, -8.671932, 7.110795], [9.978516, -8.567103, 7.222856], [9.978516, -8.455042, 7.118017], [9.870006, -8.563492, 7.114406], [9.978516, -8.671932, 7.110795], [9.978516, 1.667547, 7.455104]]}]},
			"L_leg_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[15.267898, 7.470624, -14.587171], [9.978517, 7.470624, -18.238719], [4.689136, 7.470624, -14.587171], [2.498207, 7.470624, -5.771536], [4.689136, 7.470624, 3.044099], [9.978517, 7.470624, 6.695646], [15.267898, 7.470624, 3.044099], [17.458826, 7.470624, -5.771536]]}]},
			"L_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.427112, 93.760792, -14.092988], [66.438836, 93.761679, -14.083126], [66.430299, 93.754841, -14.072363], [66.418575, 93.753954, -14.082225], [66.427112, 93.760792, -14.092988], [66.432252, 93.748123, -14.08602], [66.430299, 93.754841, -14.072363], [66.425158, 93.767511, -14.079331], [66.438836, 93.761679, -14.083126], [66.432252, 93.748123, -14.08602], [66.418575, 93.753954, -14.082225], [66.425158, 93.767511, -14.079331], [66.427112, 93.760792, -14.092988], [66.432252, 93.748123, -14.08602], [66.094084, 94.67235, -13.767144]]}, {"shapeName": "L_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.048178, 95.039679, -13.819988], [67.046225, 95.046398, -13.806331], [67.051365, 95.033729, -13.799362], [67.053319, 95.02701, -13.81302], [67.048178, 95.039679, -13.819988], [67.059901, 95.040566, -13.810126], [67.051365, 95.033729, -13.799362], [67.039641, 95.032842, -13.809224], [67.046225, 95.046398, -13.806331], [67.059901, 95.040566, -13.810126], [67.053319, 95.02701, -13.81302], [67.039641, 95.032842, -13.809224], [67.048178, 95.039679, -13.819988], [67.059901, 95.040566, -13.810126], [66.094084, 94.67235, -13.767144]]}, {"shapeName": "L_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[66.254517, 94.395538, -12.794696], [66.24084, 94.40137, -12.7909], [66.234257, 94.387814, -12.793794], [66.247934, 94.381982, -12.797589], [66.254517, 94.395538, -12.794696], [66.24598, 94.388701, -12.783933], [66.234257, 94.387814, -12.793794], [66.242794, 94.394651, -12.804558], [66.24084, 94.40137, -12.7909], [66.24598, 94.388701, -12.783933], [66.247934, 94.381982, -12.797589], [66.242794, 94.394651, -12.804558], [66.254517, 94.395538, -12.794696], [66.24598, 94.388701, -12.783933], [66.094084, 94.67235, -13.767144]]}]},
			"C_head_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_CTLShape", "degree": 3, "form": 2, "points": [[14.850032, 185.510325, -4.968417], [0.0, 191.29331, -4.968417], [-14.850032, 185.510325, -4.968417], [-21.001103, 171.548932, -4.968417], [-14.850032, 157.58754, -4.968417], [0.0, 151.804554, -4.968417], [14.850032, 157.58754, -4.968417], [21.001103, 171.548932, -4.968417]]}]},
			"world_A_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.021561, 0.0, 103.109677], [-45.819651, 0.0, 57.247797], [-34.352112, 0.0, 57.250189], [-34.34732, 0.0, 34.324037], [-57.273472, 0.0, 34.319245], [-57.275873, 0.0, 45.786783], [-103.109677, 0.0, -0.021561], [-57.247797, 0.0, -45.819651], [-57.250189, 0.0, -34.352112], [-34.324037, 0.0, -34.34732], [-34.319245, 0.0, -57.273472], [-45.786783, 0.0, -57.275873], [0.021561, 0.0, -103.109677], [45.819651, 0.0, -57.247797], [34.352112, 0.0, -57.250189], [34.34732, 0.0, -34.324037], [57.273472, 0.0, -34.319245], [57.275873, 0.0, -45.786783], [103.109677, 0.0, 0.021561], [57.247797, 0.0, 45.819651], [57.250189, 0.0, 34.352112], [34.324037, 0.0, 34.34732], [34.319245, 0.0, 57.273472], [45.786783, 0.0, 57.275873], [-0.021561, 0.0, 103.109677], [-8.997413, 0.124938, 94.29073], [-8.211908, 0.0, 93.452029], [-8.211195, 0.0, 90.025154], [-7.497262, 0.0, 90.025305], [-7.542606, 0.0, 93.478944], [-7.033876, 0.0, 93.220242], [-7.051411, 0.0, 91.720984], [-6.328555, 0.0, 91.721136], [-6.328867, 0.0, 93.220394], [-5.882713, 0.0, 93.479283], [-5.881981, 0.0, 89.972091], [-5.159125, 0.0, 89.972242], [-5.159875, 0.0, 93.568677], [-5.740069, 0.0, 94.148631], [-6.632387, 0.0, 93.702235], [-7.614142, 0.0, 94.148238], [-8.211917, 0.0, 93.469877], [-7.614142, 0.0, 94.148238], [-6.641311, 0.0, 93.71116], [-5.740061, 0.0, 94.139706], [-3.999859, 0.0, 94.148996], [-4.588729, 0.0, 93.568801], [-4.588104, 0.0, 90.561361], [-3.998985, 0.0, 89.972492], [-2.115988, 0.0, 89.972885], [-1.536043, 0.0, 90.561995], [-1.536668, 0.0, 93.569435], [-2.116863, 0.0, 94.149389], [-3.999859, 0.0, 94.148996], [-3.776613, 0.0, 93.479729], [-3.865274, 0.0, 90.713224], [-2.250011, 0.0, 90.731411], [-2.259507, 0.0, 93.480042], [-3.785537, 0.0, 93.497578], [-3.999859, 0.0, 94.148996], [-2.116863, 0.0, 94.149389], [-0.912102, 0.0, 94.149639], [-0.955848, 0.0, 89.973126], [1.078859, 0.0, 89.973545], [1.667728, 0.0, 90.562664], [1.667469, 0.0, 91.82097], [1.069426, 0.0, 92.400915], [1.03372, 0.0, 92.445527], [2.202437, 0.0, 94.132442], [2.202428, 0.0, 94.15029], [1.363557, 0.0, 94.150112], [0.19485, 0.0, 92.454282], [-0.242434, 0.0, 92.454192], [-0.242059, 0.0, 90.669362], [0.882385, 0.0, 90.669594], [0.891086, 0.0, 91.731568], [-0.242282, 0.0, 91.731336], [-0.242791, 0.0, 94.149782], [-0.912102, 0.0, 94.149639], [5.718544, 0.0, 94.151022], [5.718687, 0.0, 93.481711], [3.380559, 0.0, 93.472296], [3.381291, 0.0, 89.974027], [2.658434, 0.0, 89.973884], [2.65756, 0.0, 94.15038], [8.761681, 0.0, 94.151656], [9.297255, 0.0, 93.571702], [9.342501, 0.0, 90.564271], [8.762556, 0.0, 89.975161], [6.290565, 0.0, 89.974643], [6.28969, 0.0, 94.151147], [7.021614, 0.0, 93.481987], [7.004354, 0.0, 90.653021], [8.530385, 0.0, 90.653343], [8.511947, 0.0, 93.464451], [6.994841, 0.0, 93.499827], [6.271842, 0.0, 94.151138]]}]},
			"C_cog_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_cog_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 98.683497, -8.688221], [5.118355, 98.737752, -8.633966], [5.118355, 98.683497, -8.579711], [5.118355, 98.629242, -8.633966], [5.118355, 98.683497, -8.688221], [5.172605, 98.683497, -8.633966], [5.118355, 98.683497, -8.579711], [5.0641, 98.683497, -8.633966], [5.118355, 98.737752, -8.633966], [5.172605, 98.683497, -8.633966], [5.118355, 98.629242, -8.633966], [5.0641, 98.683497, -8.633966], [5.118355, 98.683497, -8.688221], [5.172605, 98.683497, -8.633966], [-0.0, 98.683497, -8.633966]]}, {"shapeName": "C_cog_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.0, 103.801852, -8.688221], [-0.054255, 103.801852, -8.633966], [-0.0, 103.801852, -8.579711], [0.054255, 103.801852, -8.633966], [-0.0, 103.801852, -8.688221], [-0.0, 103.856102, -8.633966], [-0.0, 103.801852, -8.579711], [-0.0, 103.747597, -8.633966], [-0.054255, 103.801852, -8.633966], [-0.0, 103.856102, -8.633966], [0.054255, 103.801852, -8.633966], [-0.0, 103.747597, -8.633966], [-0.0, 103.801852, -8.688221], [-0.0, 103.856102, -8.633966], [-0.0, 98.683497, -8.633966]]}, {"shapeName": "C_cog_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.0, 98.737752, -3.515611], [-0.054255, 98.683497, -3.515611], [-0.0, 98.629242, -3.515611], [0.054255, 98.683497, -3.515611], [-0.0, 98.737752, -3.515611], [-0.0, 98.683497, -3.461361], [-0.0, 98.629242, -3.515611], [-0.0, 98.683497, -3.569866], [-0.054255, 98.683497, -3.515611], [-0.0, 98.683497, -3.461361], [0.054255, 98.683497, -3.515611], [-0.0, 98.683497, -3.569866], [-0.0, 98.737752, -3.515611], [-0.0, 98.683497, -3.461361], [-0.0, 98.683497, -8.633966]]}]},
			"L_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_C_CTLShape", "degree": 3, "form": 2, "points": [[67.45268, 93.128889, -10.747471], [67.562183, 93.172451, -10.795408], [67.672667, 93.211765, -10.746069], [67.719411, 93.223801, -10.628355], [67.675034, 93.201509, -10.511221], [67.565531, 93.157947, -10.463284], [67.455048, 93.118633, -10.512623], [67.408304, 93.106597, -10.630337]]}]},
			"C_lookAt_CTL": {"color": 17, "shapes": [{"shapeName": "C_lookAt_CTLShape", "degree": 1, "form": 0, "points": [[-4.98069, 169.237392, 71.241043], [-4.98069, 168.612872, 71.241043], [-4.98069, 168.612872, 70.616523], [-4.98069, 169.237392, 70.616523], [-4.98069, 169.237392, 71.241043], [4.98069, 169.237392, 71.241043], [4.98069, 168.612872, 71.241043], [4.98069, 168.612872, 70.616523], [4.98069, 169.237392, 70.616523], [4.98069, 169.237392, 71.241043], [4.98069, 168.612872, 71.241043], [-4.98069, 168.612872, 71.241043], [-4.98069, 168.612872, 70.616523], [4.98069, 168.612872, 70.616523], [4.98069, 169.237392, 70.616523], [-4.98069, 169.237392, 70.616523], [-4.98069, 169.237392, 71.241043], [-0.31, 169.235132, 71.238783], [-0.31226, 163.944442, 71.241043], [-0.31226, 163.944442, 70.616523], [0.31226, 163.944442, 70.616523], [0.31226, 163.944442, 71.241043], [-0.31226, 163.944442, 71.241043], [-0.31226, 173.905822, 71.241043], [0.31226, 173.905822, 71.241043], [0.31226, 173.905822, 70.616523], [-0.31226, 173.905822, 70.616523], [-0.31226, 173.905822, 71.241043], [-0.31226, 173.905822, 70.616523], [-0.31226, 163.944442, 70.616523], [0.31226, 163.944442, 70.616523], [0.31226, 173.905822, 70.616523], [0.31226, 173.905822, 71.241043], [0.31226, 163.944442, 71.241043], [0.31, 168.615132, 71.238783], [0.31226, 168.612872, 75.909473], [-0.31226, 168.612872, 75.909473], [-0.31226, 169.237392, 75.909473], [0.31226, 169.237392, 75.909473], [0.31226, 168.612872, 75.909473], [0.31226, 168.612872, 65.948093], [0.31226, 169.237392, 65.948093], [-0.31226, 169.237392, 65.948093], [-0.31226, 168.612872, 65.948093], [0.31226, 168.612872, 65.948093], [-0.31226, 168.612872, 65.948093], [-0.31226, 168.612872, 75.909473], [-0.31226, 169.237392, 75.909473], [-0.31226, 169.237392, 65.948093], [0.31226, 169.237392, 65.948093], [0.31226, 169.237392, 75.909473]]}]},
			"L_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.767251, 89.821742, -2.155873], [66.771318, 89.824205, -2.141282], [66.756526, 89.825272, -2.13734], [66.752459, 89.822809, -2.15193], [66.767251, 89.821742, -2.155873], [66.761618, 89.812824, -2.144728], [66.756526, 89.825272, -2.13734], [66.762158, 89.83419, -2.148485], [66.771318, 89.824205, -2.141282], [66.761618, 89.812824, -2.144728], [66.752459, 89.822809, -2.15193], [66.762158, 89.83419, -2.148485], [66.767251, 89.821742, -2.155873], [66.761618, 89.812824, -2.144728], [66.78735, 90.831395, -2.323847]]}, {"shapeName": "L_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.682264, 90.895482, -1.830855], [67.677171, 90.907931, -1.823467], [67.671539, 90.899012, -1.812322], [67.676631, 90.886564, -1.81971], [67.682264, 90.895482, -1.830855], [67.68633, 90.897945, -1.816265], [67.671539, 90.899012, -1.812322], [67.667472, 90.896549, -1.826912], [67.677171, 90.907931, -1.823467], [67.68633, 90.897945, -1.816265], [67.676631, 90.886564, -1.81971], [67.667472, 90.896549, -1.826912], [67.682264, 90.895482, -1.830855], [67.68633, 90.897945, -1.816265], [66.78735, 90.831395, -2.323847]]}, {"shapeName": "L_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[66.290862, 90.998605, -1.444323], [66.281703, 91.00859, -1.451526], [66.272004, 90.997209, -1.454971], [66.281163, 90.987223, -1.447769], [66.290862, 90.998605, -1.444323], [66.276071, 90.999672, -1.440382], [66.272004, 90.997209, -1.454971], [66.286796, 90.996142, -1.458914], [66.281703, 91.00859, -1.451526], [66.276071, 90.999672, -1.440382], [66.281163, 90.987223, -1.447769], [66.286796, 90.996142, -1.458914], [66.290862, 90.998605, -1.444323], [66.276071, 90.999672, -1.440382], [66.78735, 90.831395, -2.323847]]}]},
			"L_toeTip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toeTip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[20.215226, 1.455603, 13.860597], [20.215226, 1.559027, 13.973964], [20.215226, 1.44566, 14.077389], [20.215226, 1.342235, 13.964022], [20.215226, 1.455603, 13.860597], [20.323726, 1.450631, 13.968993], [20.215226, 1.44566, 14.077389], [20.106716, 1.450631, 13.968993], [20.215226, 1.559027, 13.973964], [20.323726, 1.450631, 13.968993], [20.215226, 1.342235, 13.964022], [20.106716, 1.450631, 13.968993], [20.215226, 1.455603, 13.860597], [20.323726, 1.450631, 13.968993], [9.978516, 1.450631, 13.968993]]}, {"shapeName": "L_toeTip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[9.978516, 11.681564, 14.329579], [9.870006, 11.676593, 14.437975], [9.978516, 11.671622, 14.546371], [10.087026, 11.676593, 14.437975], [9.978516, 11.681564, 14.329579], [9.978516, 11.784979, 14.442945], [9.978516, 11.671622, 14.546371], [9.978516, 11.568197, 14.433003], [9.870006, 11.676593, 14.437975], [9.978516, 11.784979, 14.442945], [10.087026, 11.676593, 14.437975], [9.978516, 11.568197, 14.433003], [9.978516, 11.681564, 14.329579], [9.978516, 11.784979, 14.442945], [9.978516, 1.450631, 13.968993]]}, {"shapeName": "L_toeTip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.978516, 1.090046, 24.199925], [9.870006, 0.98165, 24.194954], [9.978516, 0.873253, 24.189983], [10.087026, 0.98165, 24.194954], [9.978516, 1.090046, 24.199925], [9.978516, 0.976679, 24.30334], [9.978516, 0.873253, 24.189983], [9.978516, 0.986621, 24.086558], [9.870006, 0.98165, 24.194954], [9.978516, 0.976679, 24.30334], [10.087026, 0.98165, 24.194954], [9.978516, 0.986621, 24.086558], [9.978516, 1.090046, 24.199925], [9.978516, 0.976679, 24.30334], [9.978516, 1.450631, 13.968993]]}]},
			"L_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.52269, 88.885946, -6.167311], [68.530925, 88.888837, -6.154688], [68.518223, 88.887729, -6.146148], [68.509989, 88.884838, -6.158771], [68.52269, 88.885946, -6.167311], [68.522238, 88.87621, -6.155458], [68.518223, 88.887729, -6.146148], [68.518675, 88.897465, -6.158001], [68.530925, 88.888837, -6.154688], [68.522238, 88.87621, -6.155458], [68.509989, 88.884838, -6.158771], [68.518675, 88.897465, -6.158001], [68.52269, 88.885946, -6.167311], [68.522238, 88.87621, -6.155458], [68.352369, 89.889469, -6.276646]]}, {"shapeName": "L_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[69.342151, 90.077168, -6.094655], [69.338136, 90.088687, -6.085345], [69.337684, 90.078951, -6.073492], [69.341699, 90.067431, -6.082802], [69.342151, 90.077168, -6.094655], [69.350385, 90.080058, -6.082032], [69.337684, 90.078951, -6.073492], [69.329449, 90.07606, -6.086115], [69.338136, 90.088687, -6.085345], [69.350385, 90.080058, -6.082032], [69.341699, 90.067431, -6.082802], [69.329449, 90.07606, -6.086115], [69.342151, 90.077168, -6.094655], [69.350385, 90.080058, -6.082032], [68.352369, 89.889469, -6.276646]]}, {"shapeName": "L_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[68.152131, 89.975532, -5.276387], [68.139881, 89.984161, -5.279699], [68.131195, 89.971534, -5.280469], [68.143445, 89.962905, -5.277157], [68.152131, 89.975532, -5.276387], [68.13943, 89.974424, -5.267848], [68.131195, 89.971534, -5.280469], [68.143896, 89.972642, -5.289009], [68.139881, 89.984161, -5.279699], [68.13943, 89.974424, -5.267848], [68.143445, 89.962905, -5.277157], [68.143896, 89.972642, -5.289009], [68.152131, 89.975532, -5.276387], [68.13943, 89.974424, -5.267848], [68.352369, 89.889469, -6.276646]]}]},
			"C_midNeck_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[10.273668, 159.997179, -14.88271], [0.0, 160.880237, -18.31724], [-10.273668, 159.997179, -14.88271], [-14.529152, 157.865284, -6.591002], [-10.273668, 155.733389, 1.700706], [0.0, 154.850331, 5.135237], [10.273668, 155.733389, 1.700706], [14.529152, 157.865284, -6.591002]]}]},
			"world_C_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.016769, 0.0, 80.196416], [-35.637506, 0.0, 44.526065], [-26.71831, 0.0, 44.527925], [-26.714582, 0.0, 26.696473], [-44.546034, 0.0, 26.692746], [-44.547901, 0.0, 35.611942], [-80.196416, 0.0, -0.016769], [-44.526065, 0.0, -35.637506], [-44.527925, 0.0, -26.71831], [-26.696473, 0.0, -26.714582], [-26.692746, 0.0, -44.546034], [-35.611942, 0.0, -44.547901], [0.016769, 0.0, -80.196416], [35.637506, 0.0, -44.526065], [26.71831, 0.0, -44.527925], [26.714582, 0.0, -26.696473], [44.546034, 0.0, -26.692746], [44.547901, 0.0, -35.611942], [80.196416, 0.0, 0.016769], [44.526065, 0.0, 35.637506], [44.527925, 0.0, 26.71831], [26.696473, 0.0, 26.714582], [26.692746, 0.0, 44.546034], [35.611942, 0.0, 44.547901], [-0.016769, 0.0, 80.196416], [-6.997988, 0.097174, 73.337234], [-6.38704, 0.0, 72.684911], [-6.386485, 0.0, 70.019564], [-5.831204, 0.0, 70.019682], [-5.866471, 0.0, 72.705845], [-5.470792, 0.0, 72.504633], [-5.484431, 0.0, 71.338543], [-4.922209, 0.0, 71.338661], [-4.922452, 0.0, 72.504751], [-4.575444, 0.0, 72.706109], [-4.574874, 0.0, 69.978293], [-4.012653, 0.0, 69.978411], [-4.013236, 0.0, 72.775637], [-4.464498, 0.0, 73.226713], [-5.158523, 0.0, 72.879516], [-5.92211, 0.0, 73.226407], [-6.387047, 0.0, 72.698793], [-5.92211, 0.0, 73.226407], [-5.165464, 0.0, 72.886457], [-4.464492, 0.0, 73.219772], [-3.111002, 0.0, 73.226997], [-3.569011, 0.0, 72.775734], [-3.568525, 0.0, 70.436614], [-3.110322, 0.0, 69.978605], [-1.645769, 0.0, 69.97891], [-1.1947, 0.0, 70.437107], [-1.195186, 0.0, 72.776227], [-1.646449, 0.0, 73.227303], [-3.111002, 0.0, 73.226997], [-2.937366, 0.0, 72.706456], [-3.006324, 0.0, 70.55473], [-1.750009, 0.0, 70.568875], [-1.757394, 0.0, 72.706699], [-2.944307, 0.0, 72.720338], [-3.111002, 0.0, 73.226997], [-1.646449, 0.0, 73.227303], [-0.709413, 0.0, 73.227497], [-0.743438, 0.0, 69.979098], [0.839112, 0.0, 69.979424], [1.297122, 0.0, 70.437628], [1.296921, 0.0, 71.41631], [0.831776, 0.0, 71.867379], [0.804005, 0.0, 71.902077], [1.713006, 0.0, 73.214122], [1.712999, 0.0, 73.228004], [1.060544, 0.0, 73.227865], [0.15155, 0.0, 71.908886], [-0.188559, 0.0, 71.908816], [-0.188268, 0.0, 70.520615], [0.686299, 0.0, 70.520795], [0.693067, 0.0, 71.346775], [-0.188441, 0.0, 71.346595], [-0.188837, 0.0, 73.227608], [-0.709413, 0.0, 73.227497], [4.447757, 0.0, 73.228573], [4.447868, 0.0, 72.707997], [2.629324, 0.0, 72.700674], [2.629893, 0.0, 69.979799], [2.067671, 0.0, 69.979688], [2.066991, 0.0, 73.228073], [6.814641, 0.0, 73.229066], [7.231198, 0.0, 72.77799], [7.266389, 0.0, 70.438877], [6.815321, 0.0, 69.98068], [4.892662, 0.0, 69.980278], [4.891981, 0.0, 73.22867], [5.461255, 0.0, 72.708212], [5.447831, 0.0, 70.507906], [6.634744, 0.0, 70.508155], [6.620404, 0.0, 72.694573], [5.440432, 0.0, 72.722087], [4.878099, 0.0, 73.228663]]}]},
			"C_neckBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neckBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 151.575099, -8.264302], [5.118355, 151.614135, -8.198245], [5.118355, 151.548079, -8.15921], [5.118355, 151.509043, -8.225266], [5.118355, 151.575099, -8.264302], [5.172605, 151.561589, -8.211756], [5.118355, 151.548079, -8.15921], [5.0641, 151.561589, -8.211756], [5.118355, 151.614135, -8.198245], [5.172605, 151.561589, -8.211756], [5.118355, 151.509043, -8.225266], [5.0641, 151.561589, -8.211756], [5.118355, 151.575099, -8.264302], [5.172605, 151.561589, -8.211756], [0.0, 151.561589, -8.211756]]}, {"shapeName": "C_neckBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 156.532227, -6.989766], [-0.054255, 156.518717, -6.93722], [0.0, 156.505207, -6.884674], [0.054255, 156.518717, -6.93722], [0.0, 156.532227, -6.989766], [0.0, 156.571258, -6.923711], [0.0, 156.505207, -6.884674], [0.0, 156.466171, -6.95073], [-0.054255, 156.518717, -6.93722], [0.0, 156.571258, -6.923711], [0.054255, 156.518717, -6.93722], [0.0, 156.466171, -6.95073], [0.0, 156.532227, -6.989766], [0.0, 156.571258, -6.923711], [0.0, 151.561589, -8.211756]]}, {"shapeName": "C_neckBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 150.339599, -3.241117], [-0.054255, 150.287053, -3.254628], [0.0, 150.234508, -3.268138], [0.054255, 150.287053, -3.254628], [0.0, 150.339599, -3.241117], [0.0, 150.273545, -3.202087], [0.0, 150.234508, -3.268138], [0.0, 150.300564, -3.307174], [-0.054255, 150.287053, -3.254628], [0.0, 150.273545, -3.202087], [0.054255, 150.287053, -3.254628], [0.0, 150.300564, -3.307174], [0.0, 150.339599, -3.241117], [0.0, 150.273545, -3.202087], [0.0, 151.561589, -8.211756]]}]},
			"C_chest_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_chest_FK_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 126.183497, -13.633966], [-0.0, 126.374837, -13.672026], [-0.0, 126.537047, -13.780416], [-0.0, 126.645437, -13.942626], [-0.0, 126.683497, -14.133966], [-0.0, 126.645437, -14.325306], [-0.0, 126.537047, -14.487516], [-0.0, 126.374837, -14.595906], [-0.0, 126.183497, -14.633966], [-0.0, 125.992157, -14.595906], [-0.0, 125.829947, -14.487516], [-0.0, 125.721557, -14.325306], [-0.0, 125.683497, -14.133966], [-0.0, 125.721557, -13.942626], [-0.0, 125.829947, -13.780416], [-0.0, 125.992157, -13.672026], [-0.0, 126.183497, -13.633966], [-0.0, 126.183497, -8.633966]]}]},
			"L_shoulder_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [7.136189, 146.281169, -2.91024], [11.862721, 145.887888, -5.622284], [13.6681, 145.737668, -6.658195], [8.440995, 149.681815, -12.135815], [1.599717, 152.419875, -13.449359], [-4.242626, 152.905998, -10.097073], [-6.854413, 150.954501, -3.359442], [-5.238065, 147.310794, 4.19], [-3.432687, 147.160574, 3.154089], [1.293846, 146.767293, 0.442046], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097]]}]},
			"L_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.924534, 92.208765, -10.685612], [67.934798, 92.212117, -10.674707], [67.924753, 92.207818, -10.663931], [67.914489, 92.204466, -10.674836], [67.924534, 92.208765, -10.685612], [67.928468, 92.198149, -10.675253], [67.924753, 92.207818, -10.663931], [67.920819, 92.218435, -10.67429], [67.934798, 92.212117, -10.674707], [67.928468, 92.198149, -10.675253], [67.914489, 92.204466, -10.674836], [67.920819, 92.218435, -10.67429], [67.924534, 92.208765, -10.685612], [67.928468, 92.198149, -10.675253], [67.563857, 93.165199, -10.629346]]}, {"shapeName": "L_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[68.521678, 93.526555, -10.634083], [68.517963, 93.536224, -10.622762], [68.521896, 93.525608, -10.612403], [68.525611, 93.515938, -10.623725], [68.521678, 93.526555, -10.634083], [68.53194, 93.529906, -10.623178], [68.521896, 93.525608, -10.612403], [68.511633, 93.522256, -10.623308], [68.517963, 93.536224, -10.622762], [68.53194, 93.529906, -10.623178], [68.525611, 93.515938, -10.623725], [68.511633, 93.522256, -10.623308], [68.521678, 93.526555, -10.634083], [68.53194, 93.529906, -10.623178], [67.563857, 93.165199, -10.629346]]}, {"shapeName": "L_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[67.584321, 93.124365, -9.606637], [67.570342, 93.130683, -9.60622], [67.564012, 93.116715, -9.606766], [67.577991, 93.110397, -9.607183], [67.584321, 93.124365, -9.606637], [67.574276, 93.120067, -9.595862], [67.564012, 93.116715, -9.606766], [67.574057, 93.121013, -9.617542], [67.570342, 93.130683, -9.60622], [67.574276, 93.120067, -9.595862], [67.577991, 93.110397, -9.607183], [67.574057, 93.121013, -9.617542], [67.584321, 93.124365, -9.606637], [67.574276, 93.120067, -9.595862], [67.563857, 93.165199, -10.629346]]}]},
			"L_ankleOffset_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ankleOffset_PIV_CTLShape", "degree": 1, "form": 0, "points": [[20.215227, 7.46518, -5.87991], [20.215227, 7.578997, -5.776981], [20.215227, 7.476068, -5.663163], [20.215227, 7.362251, -5.766092], [20.215227, 7.46518, -5.87991], [20.323727, 7.470624, -5.771536], [20.215227, 7.476068, -5.663163], [20.106717, 7.470624, -5.771536], [20.215227, 7.578997, -5.776981], [20.323727, 7.470624, -5.771536], [20.215227, 7.362251, -5.766092], [20.106717, 7.470624, -5.771536], [20.215227, 7.46518, -5.87991], [20.323727, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_ankleOffset_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[9.978517, 17.688996, -6.393531], [9.870007, 17.694441, -6.285158], [9.978517, 17.699885, -6.176784], [10.087027, 17.694441, -6.285158], [9.978517, 17.688996, -6.393531], [9.978517, 17.802804, -6.290602], [9.978517, 17.699885, -6.176784], [9.978517, 17.586067, -6.279713], [9.870007, 17.694441, -6.285158], [9.978517, 17.802804, -6.290602], [10.087027, 17.694441, -6.285158], [9.978517, 17.586067, -6.279713], [9.978517, 17.688996, -6.393531], [9.978517, 17.802804, -6.290602], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_ankleOffset_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.978516, 8.092619, 4.446836], [9.870006, 7.984245, 4.45228], [9.978516, 7.875872, 4.457725], [10.087026, 7.984245, 4.45228], [9.978516, 8.092619, 4.446836], [9.978516, 7.989689, 4.560644], [9.978516, 7.875872, 4.457725], [9.978516, 7.978801, 4.343907], [9.870006, 7.984245, 4.45228], [9.978516, 7.989689, 4.560644], [10.087026, 7.984245, 4.45228], [9.978516, 7.978801, 4.343907], [9.978516, 8.092619, 4.446836], [9.978516, 7.989689, 4.560644], [9.978517, 7.470624, -5.771536]]}]},
			"L_shoulder_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_shoulder_PIV_CTLShape", "degree": 1, "form": 0, "points": [[11.263831, 145.974519, -5.367537], [11.324378, 146.011636, -5.267399], [11.335594, 145.89495, -5.230931], [11.275047, 145.857834, -5.331069], [11.263831, 145.974519, -5.367537], [11.374804, 145.928486, -5.342321], [11.335594, 145.89495, -5.230931], [11.224614, 145.940983, -5.256143], [11.324378, 146.011636, -5.267399], [11.374804, 145.928486, -5.342321], [11.275047, 145.857834, -5.331069], [11.224614, 145.940983, -5.256143], [11.263831, 145.974519, -5.367537], [11.374804, 145.928486, -5.342321], [4.215017, 146.524231, -1.234097]]}, {"shapeName": "L_shoulder_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[6.506042, 153.818775, 1.700885], [6.466825, 153.785239, 1.812279], [6.577805, 153.739206, 1.837491], [6.617022, 153.772742, 1.726097], [6.506042, 153.818775, 1.700885], [6.566587, 153.855884, 1.80102], [6.577805, 153.739206, 1.837491], [6.517258, 153.702089, 1.737353], [6.466825, 153.785239, 1.812279], [6.566587, 153.855884, 1.80102], [6.617022, 153.772742, 1.726097], [6.517258, 153.702089, 1.737353], [6.506042, 153.818775, 1.700885], [6.566587, 153.855884, 1.80102], [4.215017, 146.524231, -1.234097]]}, {"shapeName": "L_shoulder_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.624701, 142.847905, 5.241393], [7.524938, 142.777253, 5.252648], [7.575371, 142.694103, 5.177722], [7.675134, 142.764756, 5.166467], [7.624701, 142.847905, 5.241393], [7.635914, 142.731224, 5.277855], [7.575371, 142.694103, 5.177722], [7.564155, 142.810789, 5.141254], [7.524938, 142.777253, 5.252648], [7.635914, 142.731224, 5.277855], [7.675134, 142.764756, 5.166467], [7.564155, 142.810789, 5.141254], [7.624701, 142.847905, 5.241393], [7.635914, 142.731224, 5.277855], [4.215017, 146.524231, -1.234097]]}]},
			"L_wrist_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[56.108304, 98.798532, -14.921067], [59.772845, 101.626209, -16.80976], [62.729174, 105.239135, -15.021278], [63.245509, 107.520904, -10.60328], [61.019397, 107.134894, -6.143773], [57.354856, 104.307217, -4.255081], [54.398527, 100.694291, -6.043563], [53.882191, 98.412522, -10.46156]]}]},
			"L_loArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[44.230698, 118.665576, -15.039099], [44.281136, 118.736096, -14.952184], [44.203948, 118.688977, -14.869159], [44.15351, 118.618456, -14.956074], [44.230698, 118.665576, -15.039099], [44.27463, 118.614521, -14.936467], [44.203948, 118.688977, -14.869159], [44.160011, 118.740037, -14.971793], [44.281136, 118.736096, -14.952184], [44.27463, 118.614521, -14.936467], [44.15351, 118.618456, -14.956074], [44.160011, 118.740037, -14.971793], [44.230698, 118.665576, -15.039099], [44.27463, 118.614521, -14.936467], [38.810577, 124.598083, -16.620529]]}, {"shapeName": "L_loArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[44.843976, 130.135381, -16.521983], [44.773289, 130.209843, -16.454677], [44.817226, 130.158782, -16.352043], [44.887913, 130.084321, -16.419349], [44.843976, 130.135381, -16.521983], [44.894408, 130.205896, -16.435068], [44.817226, 130.158782, -16.352043], [44.766788, 130.088262, -16.438958], [44.773289, 130.209843, -16.454677], [44.894408, 130.205896, -16.435068], [44.887913, 130.084321, -16.419349], [44.766788, 130.088262, -16.438958], [44.843976, 130.135381, -16.521983], [44.894408, 130.205896, -16.435068], [38.810577, 124.598083, -16.620529]]}, {"shapeName": "L_loArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[37.612581, 125.760718, -8.602651], [37.491457, 125.764659, -8.62226], [37.484956, 125.643078, -8.606542], [37.606081, 125.639137, -8.586932], [37.612581, 125.760718, -8.602651], [37.535395, 125.713597, -8.519635], [37.484956, 125.643078, -8.606542], [37.562144, 125.690197, -8.689566], [37.491457, 125.764659, -8.62226], [37.535395, 125.713597, -8.519635], [37.606081, 125.639137, -8.586932], [37.562144, 125.690197, -8.689566], [37.612581, 125.760718, -8.602651], [37.535395, 125.713597, -8.519635], [38.810577, 124.598083, -16.620529]]}]},
			"L_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_A_CTLShape", "degree": 3, "form": 2, "points": [[61.289857, 100.887727, -11.407642], [61.381403, 100.963509, -11.453062], [61.460932, 101.048877, -11.402329], [61.481857, 101.093824, -11.285161], [61.431921, 101.072021, -11.170193], [61.340375, 100.99624, -11.124773], [61.260846, 100.910871, -11.175506], [61.23992, 100.865924, -11.292675]]}]},
			"L_legBase_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 86.823346, -4.621343], [9.978517, 80.039522, -3.51314], [9.978517, 77.448326, -3.089843], [9.978517, 82.645065, 12.436596], [9.978517, 91.039204, 21.185882], [9.978517, 99.424511, 19.816062], [9.978517, 104.598018, 8.85037], [9.978517, 104.583671, -7.522663], [9.978517, 101.992476, -7.099366], [9.978517, 95.208652, -5.991163], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}]},
			"C_head_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_head_FK_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 164.1761, -9.968417], [0.0, 164.36744, -10.006477], [0.0, 164.52965, -10.114867], [0.0, 164.63804, -10.277077], [0.0, 164.6761, -10.468417], [0.0, 164.63804, -10.659757], [0.0, 164.52965, -10.821967], [0.0, 164.36744, -10.930357], [0.0, 164.1761, -10.968417], [0.0, 163.98476, -10.930357], [0.0, 163.82255, -10.821967], [0.0, 163.71416, -10.659757], [0.0, 163.6761, -10.468417], [0.0, 163.71416, -10.277077], [0.0, 163.82255, -10.114867], [0.0, 163.98476, -10.006477], [0.0, 164.1761, -9.968417], [0.0, 164.1761, -4.968417]]}]},
			"L_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[65.635372, 95.863556, -7.597983], [65.641884, 95.870551, -7.585976], [65.630227, 95.866084, -7.577052], [65.623715, 95.859089, -7.589058], [65.635372, 95.863556, -7.597983], [65.638147, 95.855694, -7.5851], [65.630227, 95.866084, -7.577052], [65.627451, 95.873947, -7.589934], [65.641884, 95.870551, -7.585976], [65.638147, 95.855694, -7.5851], [65.623715, 95.859089, -7.589058], [65.627451, 95.873947, -7.589934], [65.635372, 95.863556, -7.597983], [65.638147, 95.855694, -7.5851], [65.128259, 96.725837, -7.815532]]}, {"shapeName": "L_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.987829, 97.265249, -7.680652], [65.979909, 97.27564, -7.672604], [65.982684, 97.267777, -7.659721], [65.990605, 97.257386, -7.66777], [65.987829, 97.265249, -7.680652], [65.99434, 97.272244, -7.668646], [65.982684, 97.267777, -7.659721], [65.976173, 97.260782, -7.671728], [65.979909, 97.27564, -7.672604], [65.99434, 97.272244, -7.668646], [65.990605, 97.257386, -7.66777], [65.976173, 97.260782, -7.671728], [65.987829, 97.265249, -7.680652], [65.99434, 97.272244, -7.668646], [65.128259, 96.725837, -7.815532]]}, {"shapeName": "L_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[64.89466, 96.850821, -6.826679], [64.880228, 96.854217, -6.830637], [64.876492, 96.839358, -6.82976], [64.890924, 96.835963, -6.825803], [64.89466, 96.850821, -6.826679], [64.883004, 96.846354, -6.817755], [64.876492, 96.839358, -6.82976], [64.888148, 96.843826, -6.838685], [64.880228, 96.854217, -6.830637], [64.883004, 96.846354, -6.817755], [64.890924, 96.835963, -6.825803], [64.888148, 96.843826, -6.838685], [64.89466, 96.850821, -6.826679], [64.883004, 96.846354, -6.817755], [65.128259, 96.725837, -7.815532]]}]},
			"C_midNeck_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_midNeck_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 157.878794, -6.643548], [5.118355, 157.91783, -6.577492], [5.118355, 157.851774, -6.538456], [5.118355, 157.812738, -6.604512], [5.118355, 157.878794, -6.643548], [5.172605, 157.865284, -6.591002], [5.118355, 157.851774, -6.538456], [5.0641, 157.865284, -6.591002], [5.118355, 157.91783, -6.577492], [5.172605, 157.865284, -6.591002], [5.118355, 157.812738, -6.604512], [5.0641, 157.865284, -6.591002], [5.118355, 157.878794, -6.643548], [5.172605, 157.865284, -6.591002], [0.0, 157.865284, -6.591002]]}, {"shapeName": "C_midNeck_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 162.835922, -5.369012], [-0.054255, 162.822412, -5.316466], [0.0, 162.808902, -5.26392], [0.054255, 162.822412, -5.316466], [0.0, 162.835922, -5.369012], [0.0, 162.874953, -5.302957], [0.0, 162.808902, -5.26392], [0.0, 162.769866, -5.329976], [-0.054255, 162.822412, -5.316466], [0.0, 162.874953, -5.302957], [0.054255, 162.822412, -5.316466], [0.0, 162.769866, -5.329976], [0.0, 162.835922, -5.369012], [0.0, 162.874953, -5.302957], [0.0, 157.865284, -6.591002]]}, {"shapeName": "C_midNeck_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 156.643294, -1.620364], [-0.054255, 156.590748, -1.633874], [0.0, 156.538202, -1.647384], [0.054255, 156.590748, -1.633874], [0.0, 156.643294, -1.620364], [0.0, 156.577239, -1.581333], [0.0, 156.538202, -1.647384], [0.0, 156.604259, -1.68642], [-0.054255, 156.590748, -1.633874], [0.0, 156.577239, -1.581333], [0.054255, 156.590748, -1.633874], [0.0, 156.604259, -1.68642], [0.0, 156.643294, -1.620364], [0.0, 156.577239, -1.581333], [0.0, 157.865284, -6.591002]]}]},
			"L_toeTip_CTL": {"color": 20, "shapes": [{"shapeName": "L_toeTip_CTLShape", "degree": 1, "form": 0, "points": [[9.978516, 1.31319, 16.965843], [9.978516, 0.360054, 15.921079], [10.978516, 1.359004, 15.966893], [9.978516, 1.31319, 16.965843], [8.978516, 1.359004, 15.966893], [9.978516, 0.360054, 15.921079], [9.978516, 1.404818, 14.967943], [8.978516, 1.359004, 15.966893], [9.978516, 2.357954, 16.012706], [9.978516, 1.31319, 16.965843], [10.978516, 1.359004, 15.966893], [9.978516, 1.404818, 14.967943], [9.978516, 2.357954, 16.012706], [10.978516, 1.359004, 15.966893]]}]},
			"C_chest_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[16.926019, 126.183497, -22.738982], [-0.0, 133.383497, -28.581458], [-16.926019, 126.183497, -22.738982], [-23.93699, 118.983497, -8.633966], [-16.926019, 126.183497, 5.47105], [-0.0, 133.383497, 11.313526], [16.926019, 126.183497, 5.47105], [23.93699, 118.983497, -8.633966]]}]},
			"L_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[65.618478, 96.164909, -10.486592], [65.6277, 96.170327, -10.475588], [65.618709, 96.163949, -10.464912], [65.609487, 96.158531, -10.475916], [65.618478, 96.164909, -10.486592], [65.624492, 96.155335, -10.476218], [65.618709, 96.163949, -10.464912], [65.612694, 96.173525, -10.475286], [65.6277, 96.170327, -10.475588], [65.624492, 96.155335, -10.476218], [65.609487, 96.158531, -10.475916], [65.612694, 96.173525, -10.475286], [65.618478, 96.164909, -10.486592], [65.624492, 96.155335, -10.476218], [65.062071, 97.022482, -10.43181]]}, {"shapeName": "L_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.921063, 97.579376, -10.427169], [65.915279, 97.587991, -10.415864], [65.921294, 97.578416, -10.40549], [65.927078, 97.5698, -10.416795], [65.921063, 97.579376, -10.427169], [65.930284, 97.584793, -10.416166], [65.921294, 97.578416, -10.40549], [65.912072, 97.572998, -10.416494], [65.915279, 97.587991, -10.415864], [65.930284, 97.584793, -10.416166], [65.927078, 97.5698, -10.416795], [65.912072, 97.572998, -10.416494], [65.921063, 97.579376, -10.427169], [65.930284, 97.584793, -10.416166], [65.062071, 97.022482, -10.43181]]}, {"shapeName": "L_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.082086, 96.983086, -9.409036], [65.06708, 96.986283, -9.408734], [65.063873, 96.97129, -9.409364], [65.078878, 96.968092, -9.409666], [65.082086, 96.983086, -9.409036], [65.073095, 96.976708, -9.398361], [65.063873, 96.97129, -9.409364], [65.072864, 96.977668, -9.42004], [65.06708, 96.986283, -9.408734], [65.073095, 96.976708, -9.398361], [65.078878, 96.968092, -9.409666], [65.072864, 96.977668, -9.42004], [65.082086, 96.983086, -9.409036], [65.073095, 96.976708, -9.398361], [65.062071, 97.022482, -10.43181]]}]},
			"L_heel_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_heel_PIV_CTLShape", "degree": 1, "form": 0, "points": [[20.215227, 2.475595, -8.379932], [20.215227, 2.57902, -8.266565], [20.215227, 2.465653, -8.16314], [20.215227, 2.362228, -8.276508], [20.215227, 2.475595, -8.379932], [20.323727, 2.470624, -8.271536], [20.215227, 2.465653, -8.16314], [20.106717, 2.470624, -8.271536], [20.215227, 2.57902, -8.266565], [20.323727, 2.470624, -8.271536], [20.215227, 2.362228, -8.276508], [20.106717, 2.470624, -8.271536], [20.215227, 2.475595, -8.379932], [20.323727, 2.470624, -8.271536], [9.978517, 2.470624, -8.271536]]}, {"shapeName": "L_heel_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[9.978517, 12.701557, -7.910951], [9.870007, 12.696585, -7.802554], [9.978517, 12.691614, -7.694158], [10.087027, 12.696585, -7.802554], [9.978517, 12.701557, -7.910951], [9.978517, 12.804971, -7.797584], [9.978517, 12.691614, -7.694158], [9.978517, 12.588189, -7.807526], [9.870007, 12.696585, -7.802554], [9.978517, 12.804971, -7.797584], [10.087027, 12.696585, -7.802554], [9.978517, 12.588189, -7.807526], [9.978517, 12.701557, -7.910951], [9.978517, 12.804971, -7.797584], [9.978517, 2.470624, -8.271536]]}, {"shapeName": "L_heel_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.978517, 2.110038, 1.959396], [9.870007, 2.001642, 1.954425], [9.978517, 1.893246, 1.949454], [10.087027, 2.001642, 1.954425], [9.978517, 2.110038, 1.959396], [9.978517, 1.996671, 2.062811], [9.978517, 1.893246, 1.949454], [9.978517, 2.006613, 1.846029], [9.870007, 2.001642, 1.954425], [9.978517, 1.996671, 2.062811], [10.087027, 2.001642, 1.954425], [9.978517, 2.006613, 1.846029], [9.978517, 2.110038, 1.959396], [9.978517, 1.996671, 2.062811], [9.978517, 2.470624, -8.271536]]}]},
			"L_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_D_CTLShape", "degree": 3, "form": 2, "points": [[68.263169, 89.858161, -6.413377], [68.386585, 89.875818, -6.438742], [68.489957, 89.901471, -6.369153], [68.512733, 89.920093, -6.245375], [68.441569, 89.920776, -6.139915], [68.318154, 89.903119, -6.11455], [68.214781, 89.877466, -6.184138], [68.192006, 89.858844, -6.307917]]}]},
			"L_arm_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[61.433087, 108.71553, -4.959725], [52.825726, 100.342522, -4.829448], [55.048496, 97.877969, -16.370511], [63.655857, 106.250976, -16.500789], [64.301975, 105.590904, -16.235392], [55.694614, 97.217896, -16.105115], [53.471844, 99.68245, -4.564052], [62.079204, 108.055457, -4.694329], [61.433087, 108.71553, -4.959725], [63.655857, 106.250976, -16.500789], [55.048496, 97.877969, -16.370511], [55.694614, 97.217896, -16.105115], [64.301975, 105.590904, -16.235392], [62.079204, 108.055457, -4.694329], [53.471844, 99.68245, -4.564052], [52.825726, 100.342522, -4.829448]]}]},
			"L_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_B_CTLShape", "degree": 3, "form": 2, "points": [[65.057721, 96.650061, -7.945588], [65.167667, 96.706472, -7.975857], [65.254528, 96.774226, -7.91221], [65.267423, 96.813635, -7.79193], [65.198797, 96.801612, -7.685476], [65.088851, 96.745202, -7.655207], [65.001989, 96.677447, -7.718854], [64.989095, 96.638039, -7.839134]]}]},
			"C_neck_FK_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_C_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 161.213953, -10.892641], [0.0, 161.408743, -10.881856], [0.0, 161.592834, -10.94644], [0.0, 161.738202, -11.076549], [0.0, 161.82271, -11.252385], [0.0, 161.833495, -11.447175], [0.0, 161.768911, -11.631266], [0.0, 161.638801, -11.776634], [0.0, 161.462966, -11.861141], [0.0, 161.268176, -11.871926], [0.0, 161.084085, -11.807343], [0.0, 160.938717, -11.677233], [0.0, 160.85421, -11.501398], [0.0, 160.843425, -11.306607], [0.0, 160.908008, -11.122516], [0.0, 161.038118, -10.977148], [0.0, 161.213953, -10.892641], [0.0, 159.968889, -6.05014]]}]},
			"C_lookAt_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_lookAt_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.23671, 168.925132, 70.820273], [10.23671, 169.033642, 70.928783], [10.23671, 168.925132, 71.037293], [10.23671, 168.816622, 70.928783], [10.23671, 168.925132, 70.820273], [10.34521, 168.925132, 70.928783], [10.23671, 168.925132, 71.037293], [10.1282, 168.925132, 70.928783], [10.23671, 169.033642, 70.928783], [10.34521, 168.925132, 70.928783], [10.23671, 168.816622, 70.928783], [10.1282, 168.925132, 70.928783], [10.23671, 168.925132, 70.820273], [10.34521, 168.925132, 70.928783], [0.0, 168.925132, 70.928783]]}, {"shapeName": "C_lookAt_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 179.161842, 70.820273], [-0.10851, 179.161842, 70.928783], [0.0, 179.161842, 71.037293], [0.10851, 179.161842, 70.928783], [0.0, 179.161842, 70.820273], [0.0, 179.270342, 70.928783], [0.0, 179.161842, 71.037293], [0.0, 179.053332, 70.928783], [-0.10851, 179.161842, 70.928783], [0.0, 179.270342, 70.928783], [0.10851, 179.161842, 70.928783], [0.0, 179.053332, 70.928783], [0.0, 179.161842, 70.820273], [0.0, 179.270342, 70.928783], [0.0, 168.925132, 70.928783]]}, {"shapeName": "C_lookAt_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 169.033642, 81.165493], [-0.10851, 168.925132, 81.165493], [0.0, 168.816622, 81.165493], [0.10851, 168.925132, 81.165493], [0.0, 169.033642, 81.165493], [0.0, 168.925132, 81.273993], [0.0, 168.816622, 81.165493], [0.0, 168.925132, 81.056983], [-0.10851, 168.925132, 81.165493], [0.0, 168.925132, 81.273993], [0.10851, 168.925132, 81.165493], [0.0, 168.925132, 81.056983], [0.0, 169.033642, 81.165493], [0.0, 168.925132, 81.273993], [0.0, 168.925132, 70.928783]]}]},
			"L_legBase_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 85.625445, -4.425654], [9.978517, 76.903386, -3.000822], [9.978517, 73.571849, -2.456583], [9.978517, 80.25337, 17.505981], [9.978517, 91.045834, 28.755064], [9.978517, 101.826943, 26.993866], [9.978517, 108.478595, 12.895119], [9.978517, 108.460149, -8.155923], [9.978517, 105.128612, -7.611684], [9.978517, 96.406553, -6.186852], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}]},
			"C_hip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_hip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 98.683497, -8.688221], [5.118355, 98.737752, -8.633966], [5.118355, 98.683497, -8.579711], [5.118355, 98.629242, -8.633966], [5.118355, 98.683497, -8.688221], [5.172605, 98.683497, -8.633966], [5.118355, 98.683497, -8.579711], [5.0641, 98.683497, -8.633966], [5.118355, 98.737752, -8.633966], [5.172605, 98.683497, -8.633966], [5.118355, 98.629242, -8.633966], [5.0641, 98.683497, -8.633966], [5.118355, 98.683497, -8.688221], [5.172605, 98.683497, -8.633966], [-0.0, 98.683497, -8.633966]]}, {"shapeName": "C_hip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.0, 103.801852, -8.688221], [-0.054255, 103.801852, -8.633966], [-0.0, 103.801852, -8.579711], [0.054255, 103.801852, -8.633966], [-0.0, 103.801852, -8.688221], [-0.0, 103.856102, -8.633966], [-0.0, 103.801852, -8.579711], [-0.0, 103.747597, -8.633966], [-0.054255, 103.801852, -8.633966], [-0.0, 103.856102, -8.633966], [0.054255, 103.801852, -8.633966], [-0.0, 103.747597, -8.633966], [-0.0, 103.801852, -8.688221], [-0.0, 103.856102, -8.633966], [-0.0, 98.683497, -8.633966]]}, {"shapeName": "C_hip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.0, 98.737752, -3.515611], [-0.054255, 98.683497, -3.515611], [-0.0, 98.629242, -3.515611], [0.054255, 98.683497, -3.515611], [-0.0, 98.737752, -3.515611], [-0.0, 98.683497, -3.461361], [-0.0, 98.629242, -3.515611], [-0.0, 98.683497, -3.569866], [-0.054255, 98.683497, -3.515611], [-0.0, 98.683497, -3.461361], [0.054255, 98.683497, -3.515611], [-0.0, 98.683497, -3.569866], [-0.0, 98.737752, -3.515611], [-0.0, 98.683497, -3.461361], [-0.0, 98.683497, -8.633966]]}]},
			"L_legEnd_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_legEnd_FK_CTLShape", "degree": 3, "form": 2, "points": [[18.341656, 6.188183, 2.49269], [9.978517, 5.65698, 5.915838], [1.615377, 6.188183, 2.49269], [-1.848741, 7.470624, -5.771536], [1.615377, 8.753065, -14.035763], [9.978517, 9.284268, -17.45891], [18.341656, 8.753065, -14.035763], [21.805774, 7.470624, -5.771536]]}]},
			"L_innerBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_innerBall_CTLShape", "degree": 1, "form": 0, "points": [[2.978517, 2.42481, 5.227414], [2.978517, 1.471674, 4.18265], [3.978517, 2.470624, 4.228464], [2.978517, 2.42481, 5.227414], [1.978517, 2.470624, 4.228464], [2.978517, 1.471674, 4.18265], [2.978517, 2.516438, 3.229514], [1.978517, 2.470624, 4.228464], [2.978517, 3.469574, 4.274277], [2.978517, 2.42481, 5.227414], [3.978517, 2.470624, 4.228464], [2.978517, 2.516438, 3.229514], [2.978517, 3.469574, 4.274277], [3.978517, 2.470624, 4.228464]]}]},
			"C_neckBase_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[18.17069, 155.3322, -22.87702], [0.0, 149.408053, -30.876291], [-18.17069, 155.3322, -22.87702], [-25.697219, 159.047572, -6.287022], [-18.17069, 147.790978, 6.453509], [0.0, 138.743161, 10.603313], [18.17069, 147.790978, 6.453509], [25.697219, 159.047572, -6.287022]]}]},
			"C_world_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_world_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 0.0, -0.010851], [1.023671, 0.010851, 0.0], [1.023671, 0.0, 0.010851], [1.023671, -0.010851, 0.0], [1.023671, 0.0, -0.010851], [1.034521, 0.0, 0.0], [1.023671, 0.0, 0.010851], [1.01282, 0.0, 0.0], [1.023671, 0.010851, 0.0], [1.034521, 0.0, 0.0], [1.023671, -0.010851, 0.0], [1.01282, 0.0, 0.0], [1.023671, 0.0, -0.010851], [1.034521, 0.0, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 1.023671, -0.010851], [-0.010851, 1.023671, 0.0], [0.0, 1.023671, 0.010851], [0.010851, 1.023671, 0.0], [0.0, 1.023671, -0.010851], [0.0, 1.034521, 0.0], [0.0, 1.023671, 0.010851], [0.0, 1.01282, 0.0], [-0.010851, 1.023671, 0.0], [0.0, 1.034521, 0.0], [0.010851, 1.023671, 0.0], [0.0, 1.01282, 0.0], [0.0, 1.023671, -0.010851], [0.0, 1.034521, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 0.010851, 1.023671], [-0.010851, 0.0, 1.023671], [0.0, -0.010851, 1.023671], [0.010851, 0.0, 1.023671], [0.0, 0.010851, 1.023671], [0.0, 0.0, 1.034521], [0.0, -0.010851, 1.023671], [0.0, 0.0, 1.01282], [-0.010851, 0.0, 1.023671], [0.0, 0.0, 1.034521], [0.010851, 0.0, 1.023671], [0.0, 0.0, 1.01282], [0.0, 0.010851, 1.023671], [0.0, 0.0, 1.034521], [0.0, 0.0, 0.0]]}]},
			"L_arm_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[64.085716, 97.324185, -8.354311], [64.131868, 97.402526, -8.271826], [64.053581, 97.359816, -8.187457], [64.007428, 97.281474, -8.269943], [64.085716, 97.324185, -8.354311], [64.128005, 97.282383, -8.246914], [64.053581, 97.359816, -8.187457], [64.011286, 97.401623, -8.294857], [64.131868, 97.402526, -8.271826], [64.128005, 97.282383, -8.246914], [64.007428, 97.281474, -8.269943], [64.011286, 97.401623, -8.294857], [64.085716, 97.324185, -8.354311], [64.128005, 97.282383, -8.246914], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_arm_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[64.449692, 108.658855, -10.70469], [64.375262, 108.736293, -10.645235], [64.417556, 108.694486, -10.537836], [64.491986, 108.617048, -10.59729], [64.449692, 108.658855, -10.70469], [64.495839, 108.737191, -10.622204], [64.417556, 108.694486, -10.537836], [64.371404, 108.616144, -10.620321], [64.375262, 108.736293, -10.645235], [64.495839, 108.737191, -10.622204], [64.491986, 108.617048, -10.59729], [64.371404, 108.616144, -10.620321], [64.449692, 108.658855, -10.70469], [64.495839, 108.737191, -10.622204], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_arm_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[57.110257, 104.707937, -2.662955], [56.989674, 104.707033, -2.685985], [56.985816, 104.586885, -2.661071], [57.106398, 104.587788, -2.63804], [57.110257, 104.707937, -2.662955], [57.03197, 104.665225, -2.578594], [56.985816, 104.586885, -2.661071], [57.064104, 104.629595, -2.74544], [56.989674, 104.707033, -2.685985], [57.03197, 104.665225, -2.578594], [57.106398, 104.587788, -2.63804], [57.064104, 104.629595, -2.74544], [57.110257, 104.707937, -2.662955], [57.03197, 104.665225, -2.578594], [58.56385, 102.966713, -10.53242]]}]},
			"L_arm_PV_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_PV_CTLShape", "degree": 1, "form": 0, "points": [[38.873046, 127.107404, -95.797616], [38.873046, 125.507404, -95.797616], [38.873046, 125.507404, -97.397616], [38.873046, 127.107404, -97.397616], [40.473046, 127.107404, -97.397616], [40.473046, 125.507404, -97.397616], [40.473046, 125.507404, -95.797616], [40.473046, 127.107404, -95.797616], [38.873046, 127.107404, -95.797616], [38.873046, 127.107404, -97.397616], [38.873046, 125.507404, -97.397616], [40.473046, 125.507404, -97.397616], [40.473046, 127.107404, -97.397616], [40.473046, 127.107404, -95.797616], [40.473046, 125.507404, -95.797616], [38.873046, 125.507404, -95.797616]]}]},
			"C_cog_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[20.985174, 98.683497, -7.123772], [20.96304, 98.683497, -10.425161], [15.266391, 98.683497, -12.407435], [14.4879, 98.683497, -14.750111], [17.865015, 98.683497, -19.746977], [15.906618, 98.683497, -22.404842], [10.131912, 98.683497, -20.663648], [8.125677, 98.683497, -22.101413], [7.921053, 98.683497, -28.125368], [4.774392, 98.683497, -29.124527], [1.127385, 98.683497, -24.324914], [-1.340283, 98.683497, -24.308597], [-5.048505, 98.683497, -29.058713], [-8.181474, 98.683497, -28.017491], [-8.307768, 98.683497, -21.99278], [-10.294305, 98.683497, -20.528618], [-16.089696, 98.683497, -22.190495], [-18.012309, 98.683497, -19.506611], [-14.569632, 98.683497, -14.558024], [-15.316245, 98.683497, -12.205289], [-20.985174, 98.683497, -10.14416], [-20.96304, 98.683497, -6.842771], [-15.266391, 98.683497, -4.860497], [-14.4879, 98.683497, -2.517821], [-17.865015, 98.683497, 2.479045], [-15.906618, 98.683497, 5.13691], [-10.131912, 98.683497, 3.395716], [-8.125677, 98.683497, 4.833481], [-7.921053, 98.683497, 10.857436], [-4.774392, 98.683497, 11.856595], [-1.127385, 98.683497, 7.056982], [1.340283, 98.683497, 7.040665], [5.048505, 98.683497, 11.790781], [8.181474, 98.683497, 10.749559], [8.307768, 98.683497, 4.724848], [10.294305, 98.683497, 3.260686], [16.089696, 98.683497, 4.922563], [18.012309, 98.683497, 2.238679], [14.569632, 98.683497, -2.709908], [15.316245, 98.683497, -5.062643], [20.985174, 98.683497, -7.123772]]}]},
			"C_neck_FK_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_A_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 152.806653, -13.054257], [0.0, 153.001443, -13.043472], [0.0, 153.185534, -13.108055], [0.0, 153.330902, -13.238165], [0.0, 153.415409, -13.414], [0.0, 153.426194, -13.608791], [0.0, 153.361611, -13.792881], [0.0, 153.231501, -13.93825], [0.0, 153.055666, -14.022757], [0.0, 152.860875, -14.033542], [0.0, 152.676784, -13.968958], [0.0, 152.531416, -13.838848], [0.0, 152.446909, -13.663013], [0.0, 152.436124, -13.468223], [0.0, 152.500708, -13.284132], [0.0, 152.630817, -13.138764], [0.0, 152.806653, -13.054257], [0.0, 151.561589, -8.211756]]}]},
			"L_toe_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_toe_FK_CTLShape", "degree": 3, "form": 2, "points": [[13.896576, 5.583436, 7.585505], [9.978516, 7.205447, 7.639519], [6.060456, 5.583436, 7.585505], [4.437546, 1.667547, 7.455104], [6.060456, -2.248343, 7.324703], [9.978516, -3.870353, 7.270689], [13.896576, -2.248343, 7.324703], [15.519486, 1.667547, 7.455104]]}]},
			"C_head_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[13.365029, 184.114186, -4.968417], [0.0, 189.318872, -4.968417], [-13.365029, 184.114186, -4.968417], [-18.900992, 171.548932, -4.968417], [-13.365029, 158.983679, -4.968417], [0.0, 153.778992, -4.968417], [13.365029, 158.983679, -4.968417], [18.900992, 171.548932, -4.968417]]}]},
			"C_chest_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[12.694514, 126.183497, -19.212728], [-0.0, 131.583497, -23.594585], [-12.694514, 126.183497, -19.212728], [-17.952743, 120.783497, -8.633966], [-12.694514, 126.183497, 1.944796], [-0.0, 131.583497, 6.326653], [12.694514, 126.183497, 1.944796], [17.952743, 120.783497, -8.633966]]}]},
			"C_lookAt_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lookAt_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-4.482621, 169.206166, 71.209817], [-4.482621, 168.644098, 71.209817], [-4.482621, 168.644098, 70.647749], [-4.482621, 169.206166, 70.647749], [-4.482621, 169.206166, 71.209817], [4.482621, 169.206166, 71.209817], [4.482621, 168.644098, 71.209817], [4.482621, 168.644098, 70.647749], [4.482621, 169.206166, 70.647749], [4.482621, 169.206166, 71.209817], [4.482621, 168.644098, 71.209817], [-4.482621, 168.644098, 71.209817], [-4.482621, 168.644098, 70.647749], [4.482621, 168.644098, 70.647749], [4.482621, 169.206166, 70.647749], [-4.482621, 169.206166, 70.647749], [-4.482621, 169.206166, 71.209817], [-0.279, 169.204132, 71.207783], [-0.281034, 164.442511, 71.209817], [-0.281034, 164.442511, 70.647749], [0.281034, 164.442511, 70.647749], [0.281034, 164.442511, 71.209817], [-0.281034, 164.442511, 71.209817], [-0.281034, 173.407753, 71.209817], [0.281034, 173.407753, 71.209817], [0.281034, 173.407753, 70.647749], [-0.281034, 173.407753, 70.647749], [-0.281034, 173.407753, 71.209817], [-0.281034, 173.407753, 70.647749], [-0.281034, 164.442511, 70.647749], [0.281034, 164.442511, 70.647749], [0.281034, 173.407753, 70.647749], [0.281034, 173.407753, 71.209817], [0.281034, 164.442511, 71.209817], [0.279, 168.646132, 71.207783], [0.281034, 168.644098, 75.411404], [-0.281034, 168.644098, 75.411404], [-0.281034, 169.206166, 75.411404], [0.281034, 169.206166, 75.411404], [0.281034, 168.644098, 75.411404], [0.281034, 168.644098, 66.446162], [0.281034, 169.206166, 66.446162], [-0.281034, 169.206166, 66.446162], [-0.281034, 168.644098, 66.446162], [0.281034, 168.644098, 66.446162], [-0.281034, 168.644098, 66.446162], [-0.281034, 168.644098, 75.411404], [-0.281034, 169.206166, 75.411404], [-0.281034, 169.206166, 66.446162], [0.281034, 169.206166, 66.446162], [0.281034, 169.206166, 75.411404]]}]},
			"L_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[62.052879, 100.240345, -11.139694], [62.059436, 100.248852, -11.128734], [62.0502, 100.242482, -11.118264], [62.043643, 100.233975, -11.129224], [62.052879, 100.240345, -11.139694], [62.05886, 100.233587, -11.127284], [62.0502, 100.242482, -11.118264], [62.044219, 100.249242, -11.130675], [62.059436, 100.248852, -11.128734], [62.05886, 100.233587, -11.127284], [62.043643, 100.233975, -11.129224], [62.044219, 100.249242, -11.130675], [62.052879, 100.240345, -11.139694], [62.05886, 100.233587, -11.127284], [61.360889, 100.979874, -11.288918]]}, {"shapeName": "L_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[62.107174, 101.680533, -11.276498], [62.098514, 101.689429, -11.267478], [62.104496, 101.68267, -11.255068], [62.113156, 101.673774, -11.264088], [62.107174, 101.680533, -11.276498], [62.113731, 101.689039, -11.265538], [62.104496, 101.68267, -11.255068], [62.097939, 101.674163, -11.266028], [62.098514, 101.689429, -11.267478], [62.113731, 101.689039, -11.265538], [62.113156, 101.673774, -11.264088], [62.097939, 101.674163, -11.266028], [62.107174, 101.680533, -11.276498], [62.113731, 101.689039, -11.265538], [61.360889, 100.979874, -11.288918]]}, {"shapeName": "L_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.242458, 101.088094, -10.277838], [61.227241, 101.088484, -10.279778], [61.226665, 101.073218, -10.278328], [61.241883, 101.072828, -10.276388], [61.242458, 101.088094, -10.277838], [61.233223, 101.081724, -10.267369], [61.226665, 101.073218, -10.278328], [61.235901, 101.079588, -10.288798], [61.227241, 101.088484, -10.279778], [61.233223, 101.081724, -10.267369], [61.241883, 101.072828, -10.276388], [61.235901, 101.079588, -10.288798], [61.242458, 101.088094, -10.277838], [61.233223, 101.081724, -10.267369], [61.360889, 100.979874, -11.288918]]}]},
			"C_torso_FK_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_D_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 116.183497, -13.633966], [-0.0, 116.374837, -13.672026], [-0.0, 116.537047, -13.780416], [-0.0, 116.645437, -13.942626], [-0.0, 116.683497, -14.133966], [-0.0, 116.645437, -14.325306], [-0.0, 116.537047, -14.487516], [-0.0, 116.374837, -14.595906], [-0.0, 116.183497, -14.633966], [-0.0, 115.992157, -14.595906], [-0.0, 115.829947, -14.487516], [-0.0, 115.721557, -14.325306], [-0.0, 115.683497, -14.133966], [-0.0, 115.721557, -13.942626], [-0.0, 115.829947, -13.780416], [-0.0, 115.992157, -13.672026], [-0.0, 116.183497, -13.633966], [-0.0, 116.183497, -8.633966]]}]},
			"L_wrist_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_wrist_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[64.085716, 97.324185, -8.354311], [64.131868, 97.402526, -8.271826], [64.053581, 97.359816, -8.187457], [64.007428, 97.281474, -8.269943], [64.085716, 97.324185, -8.354311], [64.128005, 97.282383, -8.246914], [64.053581, 97.359816, -8.187457], [64.011286, 97.401623, -8.294857], [64.131868, 97.402526, -8.271826], [64.128005, 97.282383, -8.246914], [64.007428, 97.281474, -8.269943], [64.011286, 97.401623, -8.294857], [64.085716, 97.324185, -8.354311], [64.128005, 97.282383, -8.246914], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_wrist_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[64.449692, 108.658855, -10.70469], [64.375262, 108.736293, -10.645235], [64.417556, 108.694486, -10.537836], [64.491986, 108.617048, -10.59729], [64.449692, 108.658855, -10.70469], [64.495839, 108.737191, -10.622204], [64.417556, 108.694486, -10.537836], [64.371404, 108.616144, -10.620321], [64.375262, 108.736293, -10.645235], [64.495839, 108.737191, -10.622204], [64.491986, 108.617048, -10.59729], [64.371404, 108.616144, -10.620321], [64.449692, 108.658855, -10.70469], [64.495839, 108.737191, -10.622204], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_wrist_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[57.110257, 104.707937, -2.662955], [56.989674, 104.707033, -2.685985], [56.985816, 104.586885, -2.661071], [57.106398, 104.587788, -2.63804], [57.110257, 104.707937, -2.662955], [57.03197, 104.665225, -2.578594], [56.985816, 104.586885, -2.661071], [57.064104, 104.629595, -2.74544], [56.989674, 104.707033, -2.685985], [57.03197, 104.665225, -2.578594], [57.106398, 104.587788, -2.63804], [57.064104, 104.629595, -2.74544], [57.110257, 104.707937, -2.662955], [57.03197, 104.665225, -2.578594], [58.56385, 102.966713, -10.53242]]}]},
			"L_heel_CTL": {"color": 20, "shapes": [{"shapeName": "L_heel_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 2.516438, -9.270486], [9.978517, 1.563301, -10.31525], [10.978517, 2.562251, -10.269436], [9.978517, 2.516438, -9.270486], [8.978517, 2.562251, -10.269436], [9.978517, 1.563301, -10.31525], [9.978517, 2.608065, -11.268386], [8.978517, 2.562251, -10.269436], [9.978517, 3.561201, -10.223623], [9.978517, 2.516438, -9.270486], [10.978517, 2.562251, -10.269436], [9.978517, 2.608065, -11.268386], [9.978517, 3.561201, -10.223623], [10.978517, 2.562251, -10.269436]]}]},
			"world_D_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.014374, 0.0, 68.739785], [-30.546434, 0.0, 38.165198], [-22.901408, 0.0, 38.166793], [-22.898213, 0.0, 22.882691], [-38.182315, 0.0, 22.879497], [-38.183915, 0.0, 30.524522], [-68.739785, 0.0, -0.014374], [-38.165198, 0.0, -30.546434], [-38.166793, 0.0, -22.901408], [-22.882691, 0.0, -22.898213], [-22.879497, 0.0, -38.182315], [-30.524522, 0.0, -38.183915], [0.014374, 0.0, -68.739785], [30.546434, 0.0, -38.165198], [22.901408, 0.0, -38.166793], [22.898213, 0.0, -22.882691], [38.182315, 0.0, -22.879497], [38.183915, 0.0, -30.524522], [68.739785, 0.0, 0.014374], [38.165198, 0.0, 30.546434], [38.166793, 0.0, 22.901408], [22.882691, 0.0, 22.898213], [22.879497, 0.0, 38.182315], [30.524522, 0.0, 38.183915], [-0.014374, 0.0, 68.739785], [-5.998275, 0.083292, 62.860487], [-5.474606, 0.0, 62.301353], [-5.47413, 0.0, 60.016769], [-4.998175, 0.0, 60.01687], [-5.028404, 0.0, 62.319296], [-4.68925, 0.0, 62.146828], [-4.700941, 0.0, 61.147323], [-4.219037, 0.0, 61.147424], [-4.219245, 0.0, 62.146929], [-3.921809, 0.0, 62.319522], [-3.921321, 0.0, 59.981394], [-3.439417, 0.0, 59.981495], [-3.439916, 0.0, 62.379118], [-3.826713, 0.0, 62.765754], [-4.421591, 0.0, 62.468157], [-5.076095, 0.0, 62.765492], [-5.474612, 0.0, 62.313251], [-5.076095, 0.0, 62.765492], [-4.427541, 0.0, 62.474106], [-3.826707, 0.0, 62.759804], [-2.666573, 0.0, 62.765998], [-3.059152, 0.0, 62.379201], [-3.058736, 0.0, 60.374241], [-2.66599, 0.0, 59.981662], [-1.410659, 0.0, 59.981923], [-1.024029, 0.0, 60.374663], [-1.024445, 0.0, 62.379623], [-1.411242, 0.0, 62.766259], [-2.666573, 0.0, 62.765998], [-2.517742, 0.0, 62.31982], [-2.57685, 0.0, 60.475483], [-1.500008, 0.0, 60.487607], [-1.506338, 0.0, 62.320028], [-2.523691, 0.0, 62.331719], [-2.666573, 0.0, 62.765998], [-1.411242, 0.0, 62.766259], [-0.608068, 0.0, 62.766426], [-0.637232, 0.0, 59.982084], [0.719239, 0.0, 59.982364], [1.111819, 0.0, 60.37511], [1.111646, 0.0, 61.21398], [0.712951, 0.0, 61.60061], [0.689147, 0.0, 61.630351], [1.468291, 0.0, 62.754961], [1.468285, 0.0, 62.76686], [0.909038, 0.0, 62.766741], [0.1299, 0.0, 61.636188], [-0.161622, 0.0, 61.636128], [-0.161373, 0.0, 60.446241], [0.588256, 0.0, 60.446396], [0.594057, 0.0, 61.154379], [-0.161521, 0.0, 61.154224], [-0.16186, 0.0, 62.766521], [-0.608068, 0.0, 62.766426], [3.812363, 0.0, 62.767348], [3.812458, 0.0, 62.32114], [2.253706, 0.0, 62.314864], [2.254194, 0.0, 59.982685], [1.772289, 0.0, 59.98259], [1.771706, 0.0, 62.76692], [5.841121, 0.0, 62.767771], [6.19817, 0.0, 62.381135], [6.228334, 0.0, 60.376181], [5.841704, 0.0, 59.98344], [4.19371, 0.0, 59.983095], [4.193127, 0.0, 62.767431], [4.681076, 0.0, 62.321325], [4.66957, 0.0, 60.435348], [5.686923, 0.0, 60.435562], [5.674632, 0.0, 62.309634], [4.663228, 0.0, 62.333218], [4.181228, 0.0, 62.767425]]}]},
			"L_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_B_CTLShape", "degree": 3, "form": 2, "points": [[64.962172, 96.963793, -10.551008], [65.0603, 97.029837, -10.597867], [65.159464, 97.091572, -10.547453], [65.201577, 97.112835, -10.429297], [65.161969, 97.081171, -10.312613], [65.063842, 97.015127, -10.265754], [64.964677, 96.953391, -10.316168], [64.922564, 96.932128, -10.434324]]}]},
			"L_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_A_CTLShape", "degree": 3, "form": 2, "points": [[61.410455, 100.96827, -12.853165], [61.504836, 101.042558, -12.895119], [61.595029, 101.113252, -12.839854], [61.628199, 101.138941, -12.719744], [61.584917, 101.104576, -12.605148], [61.490536, 101.030288, -12.563195], [61.400344, 100.959594, -12.61846], [61.367173, 100.933905, -12.738569]]}]},
			"L_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_A_CTLShape", "degree": 3, "form": 2, "points": [[61.041234, 101.118892, -9.693871], [61.138707, 101.192599, -9.729266], [61.210959, 101.28002, -9.671615], [61.215666, 101.329945, -9.554688], [61.15007, 101.313129, -9.44698], [61.052597, 101.239422, -9.411586], [60.980345, 101.152001, -9.469237], [60.975638, 101.102076, -9.586164]]}]},
			"L_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_D_CTLShape", "degree": 3, "form": 2, "points": [[66.787584, 92.426302, -14.645442], [66.895311, 92.460255, -14.703996], [67.017796, 92.466947, -14.670241], [67.083287, 92.442456, -14.563951], [67.053423, 92.40113, -14.447389], [66.945696, 92.367176, -14.388835], [66.823211, 92.360485, -14.42259], [66.75772, 92.384975, -14.528879]]}]},
			"L_arm_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[62.252868, 110.358049, -3.367527], [51.186262, 99.592754, -3.200027], [54.044109, 96.424042, -18.038537], [65.110716, 107.189337, -18.206037], [65.941439, 106.340672, -17.864813], [54.874832, 95.575377, -17.697313], [52.016985, 98.744089, -2.858803], [63.083591, 109.509384, -3.026303], [62.252868, 110.358049, -3.367527], [65.110716, 107.189337, -18.206037], [54.044109, 96.424042, -18.038537], [54.874832, 95.575377, -17.697313], [65.941439, 106.340672, -17.864813], [63.083591, 109.509384, -3.026303], [52.016985, 98.744089, -2.858803], [51.186262, 99.592754, -3.200027]]}]},
			"C_torso_FK_E_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_E_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 126.301852, -8.688221], [-0.054255, 126.301852, -8.633966], [-0.0, 126.301852, -8.579711], [0.054255, 126.301852, -8.633966], [-0.0, 126.301852, -8.688221], [-0.0, 126.356102, -8.633966], [-0.0, 126.301852, -8.579711], [-0.0, 126.247597, -8.633966], [-0.054255, 126.301852, -8.633966], [-0.0, 126.356102, -8.633966], [0.054255, 126.301852, -8.633966], [-0.0, 126.247597, -8.633966], [-0.0, 126.301852, -8.688221], [-0.0, 126.356102, -8.633966], [-0.0, 121.183497, -8.633966]]}, {"shapeName": "C_torso_FK_E_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 121.183497, -8.688221], [-5.118355, 121.129242, -8.633966], [-5.118355, 121.183497, -8.579711], [-5.118355, 121.237752, -8.633966], [-5.118355, 121.183497, -8.688221], [-5.172605, 121.183497, -8.633966], [-5.118355, 121.183497, -8.579711], [-5.0641, 121.183497, -8.633966], [-5.118355, 121.129242, -8.633966], [-5.172605, 121.183497, -8.633966], [-5.118355, 121.237752, -8.633966], [-5.0641, 121.183497, -8.633966], [-5.118355, 121.183497, -8.688221], [-5.172605, 121.183497, -8.633966], [-0.0, 121.183497, -8.633966]]}, {"shapeName": "C_torso_FK_E_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 121.183497, -3.515611], [-0.0, 121.129242, -3.515611], [0.054255, 121.183497, -3.515611], [-0.0, 121.237752, -3.515611], [-0.054255, 121.183497, -3.515611], [-0.0, 121.183497, -3.461361], [0.054255, 121.183497, -3.515611], [-0.0, 121.183497, -3.569866], [-0.0, 121.129242, -3.515611], [-0.0, 121.183497, -3.461361], [-0.0, 121.237752, -3.515611], [-0.0, 121.183497, -3.569866], [-0.054255, 121.183497, -3.515611], [-0.0, 121.183497, -3.461361], [-0.0, 121.183497, -8.633966]]}]},
			"L_leg_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[27.397811, 10.060679, -5.369612], [26.688565, 10.060679, -5.369612], [26.554247, 9.341506, -5.481213], [26.050256, 9.135156, -5.513235], [25.440619, 9.549836, -5.448885], [24.939101, 9.05425, -5.52579], [25.358722, 8.45189, -5.619264], [25.149992, 7.953794, -5.696558], [24.422144, 7.821063, -5.717155], [24.422144, 7.120185, -5.825917], [25.149992, 6.987454, -5.846515], [25.358722, 6.489424, -5.923799], [24.939101, 5.886998, -6.017283], [25.440619, 5.391412, -6.094188], [26.050256, 5.806092, -6.029838], [26.554247, 5.599742, -6.061859], [26.688565, 4.880569, -6.173461], [27.397811, 4.880569, -6.173461], [27.532196, 5.599742, -6.061859], [28.036187, 5.806092, -6.029838], [28.645824, 5.391412, -6.094188], [29.147297, 5.886998, -6.017283], [28.727721, 6.489424, -5.923799], [28.936451, 6.987454, -5.846515], [29.664232, 7.120185, -5.825917], [29.664232, 7.821063, -5.717155], [28.936451, 7.953794, -5.696558], [28.727721, 8.45189, -5.619264], [29.147297, 9.05425, -5.52579], [28.645824, 9.549836, -5.448885], [28.036187, 9.135156, -5.513235], [27.532196, 9.341506, -5.481213], [27.397811, 10.060679, -5.369612]]}, {"shapeName": "L_leg_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[27.813043, 8.231384, -5.653482], [28.131941, 7.470624, -5.771536], [27.813043, 6.709864, -5.889591], [27.043199, 6.394803, -5.938482], [26.2734, 6.709864, -5.889591], [25.954502, 7.470624, -5.771536], [26.2734, 8.231384, -5.653482], [27.043199, 8.546445, -5.604591]]}, {"shapeName": "L_leg_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[24.422144, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}]},
			"C_chest_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_CTLShape", "degree": 3, "form": 2, "points": [[21.157524, 126.183497, -26.265236], [-0.0, 135.183497, -33.568331], [-21.157524, 126.183497, -26.265236], [-29.921238, 117.183497, -8.633966], [-21.157524, 126.183497, 8.997304], [-0.0, 135.183497, 16.300399], [21.157524, 126.183497, 8.997304], [29.921238, 117.183497, -8.633966]]}]},
			"C_neck_FK_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 156.532227, -6.989766], [-0.054255, 156.518717, -6.93722], [0.0, 156.505207, -6.884674], [0.054255, 156.518717, -6.93722], [0.0, 156.532227, -6.989766], [0.0, 156.571258, -6.923711], [0.0, 156.505207, -6.884674], [0.0, 156.466171, -6.95073], [-0.054255, 156.518717, -6.93722], [0.0, 156.571258, -6.923711], [0.054255, 156.518717, -6.93722], [0.0, 156.466171, -6.95073], [0.0, 156.532227, -6.989766], [0.0, 156.571258, -6.923711], [0.0, 151.561589, -8.211756]]}, {"shapeName": "C_neck_FK_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 151.575099, -8.264302], [-5.118355, 151.509043, -8.225266], [-5.118355, 151.548079, -8.15921], [-5.118355, 151.614135, -8.198245], [-5.118355, 151.575099, -8.264302], [-5.172605, 151.561589, -8.211756], [-5.118355, 151.548079, -8.15921], [-5.0641, 151.561589, -8.211756], [-5.118355, 151.509043, -8.225266], [-5.172605, 151.561589, -8.211756], [-5.118355, 151.614135, -8.198245], [-5.0641, 151.561589, -8.211756], [-5.118355, 151.575099, -8.264302], [-5.172605, 151.561589, -8.211756], [0.0, 151.561589, -8.211756]]}, {"shapeName": "C_neck_FK_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 150.287053, -3.254628], [0.0, 150.234508, -3.268138], [0.054255, 150.287053, -3.254628], [0.0, 150.339599, -3.241117], [-0.054255, 150.287053, -3.254628], [0.0, 150.273545, -3.202087], [0.054255, 150.287053, -3.254628], [0.0, 150.300564, -3.307174], [0.0, 150.234508, -3.268138], [0.0, 150.273545, -3.202087], [0.0, 150.339599, -3.241117], [0.0, 150.300564, -3.307174], [-0.054255, 150.287053, -3.254628], [0.0, 150.273545, -3.202087], [0.0, 151.561589, -8.211756]]}]},
			"C_chest_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_chest_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 126.183497, -8.688221], [5.118355, 126.237752, -8.633966], [5.118355, 126.183497, -8.579711], [5.118355, 126.129242, -8.633966], [5.118355, 126.183497, -8.688221], [5.172605, 126.183497, -8.633966], [5.118355, 126.183497, -8.579711], [5.0641, 126.183497, -8.633966], [5.118355, 126.237752, -8.633966], [5.172605, 126.183497, -8.633966], [5.118355, 126.129242, -8.633966], [5.0641, 126.183497, -8.633966], [5.118355, 126.183497, -8.688221], [5.172605, 126.183497, -8.633966], [-0.0, 126.183497, -8.633966]]}, {"shapeName": "C_chest_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.0, 131.301852, -8.688221], [-0.054255, 131.301852, -8.633966], [-0.0, 131.301852, -8.579711], [0.054255, 131.301852, -8.633966], [-0.0, 131.301852, -8.688221], [-0.0, 131.356102, -8.633966], [-0.0, 131.301852, -8.579711], [-0.0, 131.247597, -8.633966], [-0.054255, 131.301852, -8.633966], [-0.0, 131.356102, -8.633966], [0.054255, 131.301852, -8.633966], [-0.0, 131.247597, -8.633966], [-0.0, 131.301852, -8.688221], [-0.0, 131.356102, -8.633966], [-0.0, 126.183497, -8.633966]]}, {"shapeName": "C_chest_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.0, 126.237752, -3.515611], [-0.054255, 126.183497, -3.515611], [-0.0, 126.129242, -3.515611], [0.054255, 126.183497, -3.515611], [-0.0, 126.237752, -3.515611], [-0.0, 126.183497, -3.461361], [-0.0, 126.129242, -3.515611], [-0.0, 126.183497, -3.569866], [-0.054255, 126.183497, -3.515611], [-0.0, 126.183497, -3.461361], [0.054255, 126.183497, -3.515611], [-0.0, 126.183497, -3.569866], [-0.0, 126.237752, -3.515611], [-0.0, 126.183497, -3.461361], [-0.0, 126.183497, -8.633966]]}]},
			"L_arm_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[45.225312, 120.28898, -96.753203], [45.288188, 120.345946, -96.664474], [45.22344, 120.285271, -96.579637], [45.160563, 120.228306, -96.668365], [45.225312, 120.28898, -96.753203], [45.283215, 120.223316, -96.667149], [45.22344, 120.285271, -96.579637], [45.165531, 120.350941, -96.66569], [45.288188, 120.345946, -96.664474], [45.283215, 120.223316, -96.667149], [45.160563, 120.228306, -96.668365], [45.165531, 120.350941, -96.66569], [45.225312, 120.28898, -96.753203], [45.283215, 120.223316, -96.667149], [39.673046, 126.307404, -96.597616]]}, {"shapeName": "L_arm_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[45.694005, 131.858257, -96.500883], [45.634225, 131.920218, -96.41337], [45.692133, 131.854547, -96.327316], [45.751914, 131.792587, -96.414829], [45.694005, 131.858257, -96.500883], [45.756876, 131.915217, -96.412154], [45.692133, 131.854547, -96.327316], [45.629257, 131.797582, -96.416045], [45.634225, 131.920218, -96.41337], [45.756876, 131.915217, -96.412154], [45.751914, 131.792587, -96.414829], [45.629257, 131.797582, -96.416045], [45.694005, 131.858257, -96.500883], [45.756876, 131.915217, -96.412154], [39.673046, 126.307404, -96.597616]]}, {"shapeName": "L_arm_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[39.64857, 126.191245, -88.408648], [39.525913, 126.196241, -88.409864], [39.520944, 126.073606, -88.412539], [39.643602, 126.06861, -88.411323], [39.64857, 126.191245, -88.408648], [39.583821, 126.130571, -88.323818], [39.520944, 126.073606, -88.412539], [39.585693, 126.13428, -88.497376], [39.525913, 126.196241, -88.409864], [39.583821, 126.130571, -88.323818], [39.643602, 126.06861, -88.411323], [39.585693, 126.13428, -88.497376], [39.64857, 126.191245, -88.408648], [39.583821, 126.130571, -88.323818], [39.673046, 126.307404, -96.597616]]}]},
			"C_neck_FK_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 160.732317, -5.909874], [-0.054255, 160.718807, -5.857328], [0.0, 160.705296, -5.804782], [0.054255, 160.718807, -5.857328], [0.0, 160.732317, -5.909874], [0.0, 160.771348, -5.843819], [0.0, 160.705296, -5.804782], [0.0, 160.666261, -5.870838], [-0.054255, 160.718807, -5.857328], [0.0, 160.771348, -5.843819], [0.054255, 160.718807, -5.857328], [0.0, 160.666261, -5.870838], [0.0, 160.732317, -5.909874], [0.0, 160.771348, -5.843819], [0.0, 155.761679, -7.131863]]}, {"shapeName": "C_neck_FK_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 155.775189, -7.184409], [-5.118355, 155.709133, -7.145374], [-5.118355, 155.748168, -7.079317], [-5.118355, 155.814225, -7.118353], [-5.118355, 155.775189, -7.184409], [-5.172605, 155.761679, -7.131863], [-5.118355, 155.748168, -7.079317], [-5.0641, 155.761679, -7.131863], [-5.118355, 155.709133, -7.145374], [-5.172605, 155.761679, -7.131863], [-5.118355, 155.814225, -7.118353], [-5.0641, 155.761679, -7.131863], [-5.118355, 155.775189, -7.184409], [-5.172605, 155.761679, -7.131863], [0.0, 155.761679, -7.131863]]}, {"shapeName": "C_neck_FK_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 154.487143, -2.174735], [0.0, 154.434597, -2.188246], [0.054255, 154.487143, -2.174735], [0.0, 154.539689, -2.161225], [-0.054255, 154.487143, -2.174735], [0.0, 154.473634, -2.122194], [0.054255, 154.487143, -2.174735], [0.0, 154.500653, -2.227281], [0.0, 154.434597, -2.188246], [0.0, 154.473634, -2.122194], [0.0, 154.539689, -2.161225], [0.0, 154.500653, -2.227281], [-0.054255, 154.487143, -2.174735], [0.0, 154.473634, -2.122194], [0.0, 155.761679, -7.131863]]}]},
			"L_hand_CTL": {"color": 1, "shapes": [{"shapeName": "L_hand_CTLShape", "degree": 1, "form": 0, "points": [[72.137029, 112.090588, 0.0], [71.552389, 112.194538, 0.0], [70.949164, 112.218268, 0.0], [70.377439, 112.205038, 0.0], [69.808654, 112.217323, 0.0], [69.427084, 112.246198, 0.0], [69.128674, 112.441708, 0.0], [68.879824, 112.896778, 0.0], [68.613124, 113.488033, 0.0], [68.400079, 114.147853, 0.0], [68.199529, 115.083088, 0.0], [68.099884, 116.030818, 0.0], [68.055364, 116.768548, 0.0], [68.042029, 117.348673, 0.0], [67.978294, 117.716173, 0.0], [67.910884, 118.166308, 0.0], [67.776589, 118.664953, 0.0], [67.692274, 119.110678, 0.0], [67.602394, 119.471773, 0.0], [67.467049, 119.896918, 0.0], [67.322359, 120.445963, 0.0], [67.319629, 120.870793, 0.0], [67.492564, 121.206898, 0.0], [67.698469, 121.272628, 0.0], [67.970629, 121.148098, 0.0], [68.073529, 120.824908, 0.0], [68.195854, 120.408058, 0.0], [68.357449, 119.998768, 0.0], [68.520199, 119.572048, 0.0], [68.689669, 119.054503, 0.0], [68.885179, 118.634293, 0.0], [69.058849, 118.457683, 0.0], [69.139489, 118.443823, 0.0], [69.273574, 118.705063, 0.0], [69.288169, 119.082013, 0.0], [69.190624, 119.517133, 0.0], [69.128674, 119.807458, 0.0], [69.084049, 120.247198, 0.0], [69.051499, 120.644728, 0.0], [68.982934, 121.061998, 0.0], [68.937364, 121.416268, 0.0], [68.892319, 121.717618, 0.0], [68.804434, 122.159353, 0.0], [68.730514, 122.509318, 0.0], [68.699119, 122.848573, 0.0], [68.801914, 123.161683, 0.0], [69.002884, 123.364543, 0.0], [69.296569, 123.375043, 0.0], [69.547519, 123.222898, 0.0], [69.674674, 122.887003, 0.0], [69.754894, 122.491153, 0.0], [69.833119, 122.140348, 0.0], [69.930454, 121.727278, 0.0], [70.018339, 121.344133, 0.0], [70.083859, 120.978523, 0.0], [70.134049, 120.583513, 0.0], [70.238734, 120.115003, 0.0], [70.316119, 119.796223, 0.0], [70.379434, 119.421688, 0.0], [70.572739, 119.129683, 0.0], [70.703149, 119.327503, 0.0], [70.780639, 119.847358, 0.0], [70.797859, 120.238273, 0.0], [70.785574, 120.744583, 0.0], [70.807204, 121.195243, 0.0], [70.832089, 121.591093, 0.0], [70.835029, 122.047948, 0.0], [70.812349, 122.481283, 0.0], [70.813504, 123.096583, 0.0], [70.830199, 123.544933, 0.0], [70.890994, 123.926818, 0.0], [71.115274, 124.088938, 0.0], [71.410324, 124.175773, 0.0], [71.671564, 124.087573, 0.0], [71.807014, 123.812893, 0.0], [71.842294, 123.360343, 0.0], [71.875054, 122.911888, 0.0], [71.893114, 122.539663, 0.0], [71.860669, 122.052883, 0.0], [71.855734, 121.606108, 0.0], [71.917579, 121.127098, 0.0], [71.956849, 120.892108, 0.0], [71.946349, 120.574798, 0.0], [71.962414, 120.219688, 0.0], [71.990974, 119.789608, 0.0], [72.016279, 119.275843, 0.0], [72.078649, 119.157928, 0.0], [72.230899, 119.300098, 0.0], [72.303349, 119.656888, 0.0], [72.405304, 120.126868, 0.0], [72.533824, 120.681268, 0.0], [72.620239, 121.163638, 0.0], [72.709804, 121.590673, 0.0], [72.844729, 121.988833, 0.0], [72.990049, 122.461648, 0.0], [73.104499, 122.952208, 0.0], [73.224724, 123.329368, 0.0], [73.362064, 123.626623, 0.0], [73.585504, 123.853213, 0.0], [73.755709, 123.816358, 0.0], [74.056009, 123.621478, 0.0], [74.164579, 123.173758, 0.0], [74.096644, 122.725093, 0.0], [74.042149, 122.417338, 0.0], [73.994269, 122.033878, 0.0], [73.921294, 121.626688, 0.0], [73.777339, 121.181383, 0.0], [73.714444, 120.897988, 0.0], [73.684519, 120.390733, 0.0], [73.666774, 120.061768, 0.0], [73.595164, 119.643658, 0.0], [73.532689, 119.266183, 0.0], [73.502764, 118.848178, 0.0], [73.451104, 118.216813, 0.0], [73.507489, 117.313708, 0.0], [73.616689, 116.849818, 0.0], [73.790884, 116.555608, 0.0], [74.013064, 116.237038, 0.0], [74.195554, 116.625433, 0.0], [74.487454, 117.059293, 0.0], [74.639599, 117.369778, 0.0], [74.709949, 117.722368, 0.0], [74.882779, 118.079578, 0.0], [75.165229, 118.441093, 0.0], [75.541864, 118.711573, 0.0], [75.808249, 118.792423, 0.0], [76.065919, 118.629568, 0.0], [76.111594, 118.372948, 0.0], [76.045444, 117.938248, 0.0], [75.905374, 117.658528, 0.0], [75.885949, 117.405058, 0.0], [75.876499, 116.917753, 0.0], [75.723094, 116.619448, 0.0], [75.535669, 116.378998, 0.0], [75.483274, 116.148313, 0.0], [75.443059, 115.851793, 0.0], [75.260254, 115.380973, 0.0], [75.026419, 114.366253, 0.0], [74.741134, 113.863198, 0.0], [74.370379, 113.294098, 0.0], [74.004139, 112.798498, 0.0], [73.715809, 112.432888, 0.0], [73.200574, 112.148548, 0.0], [72.728914, 112.057933, 0.0], [72.145324, 112.089853, 0.0]]}]},
			"C_torso_FK_E_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_E_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 121.183497, -13.633966], [-0.0, 121.374837, -13.672026], [-0.0, 121.537047, -13.780416], [-0.0, 121.645437, -13.942626], [-0.0, 121.683497, -14.133966], [-0.0, 121.645437, -14.325306], [-0.0, 121.537047, -14.487516], [-0.0, 121.374837, -14.595906], [-0.0, 121.183497, -14.633966], [-0.0, 120.992157, -14.595906], [-0.0, 120.829947, -14.487516], [-0.0, 120.721557, -14.325306], [-0.0, 120.683497, -14.133966], [-0.0, 120.721557, -13.942626], [-0.0, 120.829947, -13.780416], [-0.0, 120.992157, -13.672026], [-0.0, 121.183497, -13.633966], [-0.0, 121.183497, -8.633966]]}]},
			"L_upLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_upLeg_FK_CTLShape", "degree": 3, "form": 2, "points": [[20.367485, 92.690935, 4.946808], [9.978517, 93.384715, 9.193755], [-0.410452, 92.690935, 4.946808], [-4.713694, 91.015999, -5.306253], [-0.410452, 89.341063, -15.559314], [9.978517, 88.647283, -19.806261], [20.367485, 89.341063, -15.559314], [24.670727, 91.015999, -5.306253]]}]},
			"C_neckBase_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[14.132759, 154.494287, -19.618072], [0.0, 149.886616, -25.839728], [-14.132759, 154.494287, -19.618072], [-19.986726, 157.38402, -6.71474], [-14.132759, 148.628892, 3.194561], [0.0, 141.5917, 6.422186], [14.132759, 148.628892, 3.194561], [19.986726, 157.38402, -6.71474]]}]},
			"C_head_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 169.294455, -5.022672], [-0.054255, 169.294455, -4.968417], [0.0, 169.294455, -4.914162], [0.054255, 169.294455, -4.968417], [0.0, 169.294455, -5.022672], [0.0, 169.348705, -4.968417], [0.0, 169.294455, -4.914162], [0.0, 169.2402, -4.968417], [-0.054255, 169.294455, -4.968417], [0.0, 169.348705, -4.968417], [0.054255, 169.294455, -4.968417], [0.0, 169.2402, -4.968417], [0.0, 169.294455, -5.022672], [0.0, 169.348705, -4.968417], [0.0, 164.1761, -4.968417]]}, {"shapeName": "C_head_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 164.1761, -5.022672], [-5.118355, 164.121845, -4.968417], [-5.118355, 164.1761, -4.914162], [-5.118355, 164.230355, -4.968417], [-5.118355, 164.1761, -5.022672], [-5.172605, 164.1761, -4.968417], [-5.118355, 164.1761, -4.914162], [-5.0641, 164.1761, -4.968417], [-5.118355, 164.121845, -4.968417], [-5.172605, 164.1761, -4.968417], [-5.118355, 164.230355, -4.968417], [-5.0641, 164.1761, -4.968417], [-5.118355, 164.1761, -5.022672], [-5.172605, 164.1761, -4.968417], [0.0, 164.1761, -4.968417]]}, {"shapeName": "C_head_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 164.1761, 0.149938], [0.0, 164.121845, 0.149938], [0.054255, 164.1761, 0.149938], [0.0, 164.230355, 0.149938], [-0.054255, 164.1761, 0.149938], [0.0, 164.1761, 0.204188], [0.054255, 164.1761, 0.149938], [0.0, 164.1761, 0.095683], [0.0, 164.121845, 0.149938], [0.0, 164.1761, 0.204188], [0.0, 164.230355, 0.149938], [0.0, 164.1761, 0.095683], [-0.054255, 164.1761, 0.149938], [0.0, 164.1761, 0.204188], [0.0, 164.1761, -4.968417]]}]},
			"C_midNeck_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_CTLShape", "degree": 3, "form": 2, "points": [[14.676669, 160.910849, -18.436299], [0.0, 162.17236, -23.342771], [-14.676669, 160.910849, -18.436299], [-20.755931, 157.865284, -6.591002], [-14.676669, 154.819719, 5.254296], [0.0, 153.558208, 10.160768], [14.676669, 154.819719, 5.254296], [20.755931, 157.865284, -6.591002]]}]},
			"C_chest_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[19.041772, 126.183497, -24.502109], [-0.0, 134.283497, -31.074894], [-19.041772, 126.183497, -24.502109], [-26.929114, 118.083497, -8.633966], [-19.041772, 126.183497, 7.234177], [-0.0, 134.283497, 13.806963], [19.041772, 126.183497, 7.234177], [26.929114, 118.083497, -8.633966]]}]},
			"C_head_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[8.910019, 179.925768, -4.968417], [0.0, 183.395559, -4.968417], [-8.910019, 179.925768, -4.968417], [-12.600662, 171.548932, -4.968417], [-8.910019, 163.172097, -4.968417], [0.0, 159.702306, -4.968417], [8.910019, 163.172097, -4.968417], [12.600662, 171.548932, -4.968417]]}]},
			"C_lookAt_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lookAt_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.988414, 169.112488, 71.116139], [-2.988414, 168.737776, 71.116139], [-2.988414, 168.737776, 70.741427], [-2.988414, 169.112488, 70.741427], [-2.988414, 169.112488, 71.116139], [2.988414, 169.112488, 71.116139], [2.988414, 168.737776, 71.116139], [2.988414, 168.737776, 70.741427], [2.988414, 169.112488, 70.741427], [2.988414, 169.112488, 71.116139], [2.988414, 168.737776, 71.116139], [-2.988414, 168.737776, 71.116139], [-2.988414, 168.737776, 70.741427], [2.988414, 168.737776, 70.741427], [2.988414, 169.112488, 70.741427], [-2.988414, 169.112488, 70.741427], [-2.988414, 169.112488, 71.116139], [-0.186, 169.111132, 71.114783], [-0.187356, 165.936718, 71.116139], [-0.187356, 165.936718, 70.741427], [0.187356, 165.936718, 70.741427], [0.187356, 165.936718, 71.116139], [-0.187356, 165.936718, 71.116139], [-0.187356, 171.913546, 71.116139], [0.187356, 171.913546, 71.116139], [0.187356, 171.913546, 70.741427], [-0.187356, 171.913546, 70.741427], [-0.187356, 171.913546, 71.116139], [-0.187356, 171.913546, 70.741427], [-0.187356, 165.936718, 70.741427], [0.187356, 165.936718, 70.741427], [0.187356, 171.913546, 70.741427], [0.187356, 171.913546, 71.116139], [0.187356, 165.936718, 71.116139], [0.186, 168.739132, 71.114783], [0.187356, 168.737776, 73.917197], [-0.187356, 168.737776, 73.917197], [-0.187356, 169.112488, 73.917197], [0.187356, 169.112488, 73.917197], [0.187356, 168.737776, 73.917197], [0.187356, 168.737776, 67.940369], [0.187356, 169.112488, 67.940369], [-0.187356, 169.112488, 67.940369], [-0.187356, 168.737776, 67.940369], [0.187356, 168.737776, 67.940369], [-0.187356, 168.737776, 67.940369], [-0.187356, 168.737776, 73.917197], [-0.187356, 169.112488, 73.917197], [-0.187356, 169.112488, 67.940369], [0.187356, 169.112488, 67.940369], [0.187356, 169.112488, 73.917197]]}]},
			"L_loLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_loLeg_FK_CTLShape", "degree": 3, "form": 2, "points": [[17.462463, 50.629054, 8.499301], [9.978517, 50.153695, 11.562582], [2.49457, 50.629054, 8.499301], [-0.605376, 51.776676, 1.103868], [2.49457, 52.924298, -6.291565], [9.978517, 53.399657, -9.354846], [17.462463, 52.924298, -6.291565], [20.562409, 51.776676, 1.103868]]}]},
			"C_reverseJaw_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_reverseJaw_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.054255, 161.930574, 2.131058], [0.0, 161.979329, 2.154861], [-0.054255, 161.930574, 2.131058], [0.0, 161.881819, 2.107255], [0.054255, 161.930574, 2.131058], [0.0, 161.906773, 2.179808], [-0.054255, 161.930574, 2.131058], [0.0, 161.954377, 2.082303], [0.0, 161.979329, 2.154861], [0.0, 161.906773, 2.179808], [0.0, 161.881819, 2.107255], [0.0, 161.954377, 2.082303], [0.054255, 161.930574, 2.131058], [0.0, 161.906773, 2.179808], [0.0, 164.1761, -2.468417]]}, {"shapeName": "C_reverseJaw_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.054255, 168.775575, -0.222891], [0.0, 168.799378, -0.271646], [-0.054255, 168.775575, -0.222891], [0.0, 168.751772, -0.174136], [0.054255, 168.775575, -0.222891], [0.0, 168.824326, -0.19909], [-0.054255, 168.775575, -0.222891], [0.0, 168.72682, -0.246693], [0.0, 168.799378, -0.271646], [0.0, 168.824326, -0.19909], [0.0, 168.751772, -0.174136], [0.0, 168.72682, -0.246693], [0.054255, 168.775575, -0.222891], [0.0, 168.824326, -0.19909], [0.0, 164.1761, -2.468417]]}, {"shapeName": "C_reverseJaw_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-5.118355, 164.224855, -2.444614], [-5.118355, 164.199903, -2.517172], [-5.118355, 164.127345, -2.49222], [-5.118355, 164.152298, -2.419662], [-5.118355, 164.224855, -2.444614], [-5.172605, 164.1761, -2.468417], [-5.118355, 164.127345, -2.49222], [-5.0641, 164.1761, -2.468417], [-5.118355, 164.199903, -2.517172], [-5.172605, 164.1761, -2.468417], [-5.118355, 164.152298, -2.419662], [-5.0641, 164.1761, -2.468417], [-5.118355, 164.224855, -2.444614], [-5.172605, 164.1761, -2.468417], [0.0, 164.1761, -2.468417]]}]},
			"L_wrist_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[56.92682, 100.187925, -13.458185], [59.369847, 102.073044, -14.717313], [61.340733, 104.481661, -13.524992], [61.684956, 106.00284, -10.57966], [60.200881, 105.745501, -7.606656], [57.757854, 103.860382, -6.347527], [55.786968, 101.451765, -7.539848], [55.442744, 99.930586, -10.48518]]}]},
			"L_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.056405, 91.450091, -14.864185], [67.068676, 91.448929, -14.855043], [67.059694, 91.444015, -14.843612], [67.047423, 91.445177, -14.852754], [67.056405, 91.450091, -14.864185], [67.059507, 91.436807, -14.857158], [67.059694, 91.444015, -14.843612], [67.056591, 91.457299, -14.850639], [67.068676, 91.448929, -14.855043], [67.059507, 91.436807, -14.857158], [67.047423, 91.445177, -14.852754], [67.056591, 91.457299, -14.850639], [67.056405, 91.450091, -14.864185], [67.059507, 91.436807, -14.857158], [66.920503, 92.413716, -14.546415]]}, {"shapeName": "L_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.921314, 92.593743, -14.664691], [67.9215, 92.600951, -14.651146], [67.924603, 92.587667, -14.644118], [67.924416, 92.580458, -14.657664], [67.921314, 92.593743, -14.664691], [67.933583, 92.592581, -14.655549], [67.924603, 92.587667, -14.644118], [67.912332, 92.588829, -14.65326], [67.9215, 92.600951, -14.651146], [67.933583, 92.592581, -14.655549], [67.924416, 92.580458, -14.657664], [67.912332, 92.588829, -14.65326], [67.921314, 92.593743, -14.664691], [67.933583, 92.592581, -14.655549], [66.920503, 92.413716, -14.546415]]}, {"shapeName": "L_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[67.086268, 92.128991, -13.577151], [67.074184, 92.137362, -13.572747], [67.065016, 92.125239, -13.574861], [67.0771, 92.116869, -13.579265], [67.086268, 92.128991, -13.577151], [67.077286, 92.124078, -13.56572], [67.065016, 92.125239, -13.574861], [67.073997, 92.130153, -13.586292], [67.074184, 92.137362, -13.572747], [67.077286, 92.124078, -13.56572], [67.0771, 92.116869, -13.579265], [67.073997, 92.130153, -13.586292], [67.086268, 92.128991, -13.577151], [67.077286, 92.124078, -13.56572], [66.920503, 92.413716, -14.546415]]}]},
			"C_neckBase_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[16.151724, 154.913244, -21.247546], [0.0, 149.647335, -28.35801], [-16.151724, 154.913244, -21.247546], [-22.841973, 158.215796, -6.500881], [-16.151724, 148.209935, 4.824035], [0.0, 140.16743, 8.51275], [16.151724, 148.209935, 4.824035], [22.841973, 158.215796, -6.500881]]}]},
			"L_arm_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[65.964594, 117.077383, -12.120346], [65.753131, 116.474723, -12.032377], [65.100233, 116.552419, -12.174714], [64.774125, 116.179209, -12.157824], [64.945734, 115.550578, -11.990531], [64.373887, 115.256619, -12.037893], [63.985691, 115.773851, -12.223111], [63.499, 115.72935, -12.307343], [63.168883, 115.146286, -12.246411], [62.571623, 115.333237, -12.401364], [62.675525, 115.987108, -12.520985], [62.313358, 116.297313, -12.65698], [61.674884, 116.101442, -12.738121], [61.402094, 116.659783, -12.909891], [61.937232, 117.067194, -12.893826], [61.911656, 117.550486, -13.001957], [61.338853, 117.85645, -13.177615], [61.550316, 118.45911, -13.265584], [62.203234, 118.38147, -13.123254], [62.529342, 118.754681, -13.140145], [62.357734, 119.383312, -13.307438], [62.929567, 119.677233, -13.26007], [63.317833, 119.160021, -13.074843], [63.804467, 119.20454, -12.990626], [64.134564, 119.787546, -13.051549], [64.731824, 119.600596, -12.896596], [64.627942, 118.946781, -12.776984], [64.990166, 118.636559, -12.640974], [65.62857, 118.83241, -12.559842], [65.901373, 118.274106, -12.388078], [65.366235, 117.866696, -12.404143], [65.391812, 117.383403, -12.296011], [65.964594, 117.077383, -12.120346]]}, {"shapeName": "L_arm_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[64.529547, 117.918155, -12.576275], [63.976338, 118.392053, -12.78402], [63.232969, 118.324001, -12.912658], [62.734956, 117.753887, -12.886828], [62.773921, 117.015735, -12.721694], [63.327129, 116.541837, -12.513949], [64.070499, 116.609889, -12.38531], [64.568498, 117.179965, -12.411135]]}, {"shapeName": "L_arm_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[62.870253, 115.239762, -12.323888], [58.56385, 102.966713, -10.53242]]}]},
			"L_arm_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[61.023196, 107.89427, -5.755825], [53.645458, 100.717407, -5.644158], [55.55069, 98.604932, -15.536498], [62.928427, 105.781796, -15.648165], [63.482243, 105.216019, -15.420682], [56.104505, 98.039156, -15.309016], [54.199274, 100.15163, -5.416676], [61.577011, 107.328494, -5.528342], [61.023196, 107.89427, -5.755825], [62.928427, 105.781796, -15.648165], [55.55069, 98.604932, -15.536498], [56.104505, 98.039156, -15.309016], [63.482243, 105.216019, -15.420682], [61.577011, 107.328494, -5.528342], [54.199274, 100.15163, -5.416676], [53.645458, 100.717407, -5.644158]]}]},
			"C_midTorso_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_CTLShape", "degree": 3, "form": 2, "points": [[22.190832, 113.683497, -27.126325], [-0.0, 113.683497, -34.786095], [-22.190832, 113.683497, -27.126325], [-31.382555, 113.683497, -8.633966], [-22.190832, 113.683497, 9.858394], [-0.0, 113.683497, 17.518163], [22.190832, 113.683497, 9.858394], [31.382555, 113.683497, -8.633966]]}]},
			"visibility_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "visibility_CTLShape", "degree": 3, "form": 2, "points": [[10.583682, 221.764305, -16.704618], [0.5, 229.849514, -16.704618], [-9.583682, 221.764305, -16.704618], [-9.5572, 221.764305, -16.704618], [-9.583682, 221.764305, -16.704618], [0.5, 213.679096, -16.704618], [10.583682, 221.764305, -16.704618], [10.583682, 221.764305, -16.704618]]}, {"shapeName": "visibility_CTLShape1", "degree": 3, "form": 2, "points": [[4.72047, 225.984775, -16.704618], [0.5, 227.732941, -16.704618], [-3.72047, 225.984775, -16.704618], [-5.468635, 221.764305, -16.704618], [-3.72047, 217.543836, -16.704618], [0.5, 215.79567, -16.704618], [4.72047, 217.543836, -16.704618], [6.468635, 221.764305, -16.704618]]}]},
			"L_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_D_CTLShape", "degree": 3, "form": 2, "points": [[68.524947, 90.303452, -10.882141], [68.642138, 90.309213, -10.931331], [68.759902, 90.311158, -10.883222], [68.809254, 90.308148, -10.765997], [68.761285, 90.301946, -10.648323], [68.644094, 90.296185, -10.599134], [68.52633, 90.294239, -10.647242], [68.476978, 90.29725, -10.764468]]}]},
			"C_torso_FK_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 116.301852, -8.688221], [-0.054255, 116.301852, -8.633966], [-0.0, 116.301852, -8.579711], [0.054255, 116.301852, -8.633966], [-0.0, 116.301852, -8.688221], [-0.0, 116.356102, -8.633966], [-0.0, 116.301852, -8.579711], [-0.0, 116.247597, -8.633966], [-0.054255, 116.301852, -8.633966], [-0.0, 116.356102, -8.633966], [0.054255, 116.301852, -8.633966], [-0.0, 116.247597, -8.633966], [-0.0, 116.301852, -8.688221], [-0.0, 116.356102, -8.633966], [-0.0, 111.183497, -8.633966]]}, {"shapeName": "C_torso_FK_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 111.183497, -8.688221], [-5.118355, 111.129242, -8.633966], [-5.118355, 111.183497, -8.579711], [-5.118355, 111.237752, -8.633966], [-5.118355, 111.183497, -8.688221], [-5.172605, 111.183497, -8.633966], [-5.118355, 111.183497, -8.579711], [-5.0641, 111.183497, -8.633966], [-5.118355, 111.129242, -8.633966], [-5.172605, 111.183497, -8.633966], [-5.118355, 111.237752, -8.633966], [-5.0641, 111.183497, -8.633966], [-5.118355, 111.183497, -8.688221], [-5.172605, 111.183497, -8.633966], [-0.0, 111.183497, -8.633966]]}, {"shapeName": "C_torso_FK_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 111.183497, -3.515611], [-0.0, 111.129242, -3.515611], [0.054255, 111.183497, -3.515611], [-0.0, 111.237752, -3.515611], [-0.054255, 111.183497, -3.515611], [-0.0, 111.183497, -3.461361], [0.054255, 111.183497, -3.515611], [-0.0, 111.183497, -3.569866], [-0.0, 111.129242, -3.515611], [-0.0, 111.183497, -3.461361], [-0.0, 111.237752, -3.515611], [-0.0, 111.183497, -3.569866], [-0.054255, 111.183497, -3.515611], [-0.0, 111.183497, -3.461361], [-0.0, 111.183497, -8.633966]]}]},
			"L_shoulder_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [8.109913, 146.200148, -3.468955], [14.411956, 145.675774, -7.085013], [16.819128, 145.475481, -8.466227], [9.849654, 150.734344, -15.769721], [0.72795, 154.385089, -17.521113], [-7.061841, 155.033254, -13.051398], [-10.544223, 152.431257, -4.06789], [-8.389093, 147.572981, 5.998032], [-5.981921, 147.372688, 4.616818], [0.320122, 146.848314, 1.00076], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097]]}]},
			"L_leg_PV_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_PV_CTLShape", "degree": 1, "form": 0, "points": [[8.978517, 52.219762, 102.102317], [8.978517, 50.219762, 102.102317], [8.978517, 50.219762, 100.102317], [8.978517, 52.219762, 100.102317], [10.978517, 52.219762, 100.102317], [10.978517, 50.219762, 100.102317], [10.978517, 50.219762, 102.102317], [10.978517, 52.219762, 102.102317], [8.978517, 52.219762, 102.102317], [8.978517, 52.219762, 100.102317], [8.978517, 50.219762, 100.102317], [10.978517, 50.219762, 100.102317], [10.978517, 52.219762, 100.102317], [10.978517, 52.219762, 102.102317], [10.978517, 50.219762, 102.102317], [8.978517, 50.219762, 102.102317]]}]},
			"C_neckBase_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_CTLShape", "degree": 3, "form": 2, "points": [[20.189655, 155.751157, -24.506493], [0.0, 149.168771, -33.394573], [-20.189655, 155.751157, -24.506493], [-28.552466, 159.879347, -6.073162], [-20.189655, 147.372021, 8.082982], [0.0, 137.318891, 12.693876], [20.189655, 147.372021, 8.082982], [28.552466, 159.879347, -6.073162]]}]},
			"C_midNeck_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[13.209002, 160.606292, -17.251769], [0.0, 161.741653, -21.667594], [-13.209002, 160.606292, -17.251769], [-18.680338, 157.865284, -6.591002], [-13.209002, 155.124276, 4.069766], [0.0, 153.988916, 8.485591], [13.209002, 155.124276, 4.069766], [18.680338, 157.865284, -6.591002]]}]},
			"C_midNeck_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[11.741335, 160.301736, -16.06724], [0.0, 161.310945, -19.992417], [-11.741335, 160.301736, -16.06724], [-16.604745, 157.865284, -6.591002], [-11.741335, 155.428832, 2.885236], [0.0, 154.419623, 6.810414], [11.741335, 155.428832, 2.885236], [16.604745, 157.865284, -6.591002]]}]},
			"L_toe_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[12.329352, 4.01708, 7.533345], [9.978516, 4.990287, 7.565753], [7.62768, 4.01708, 7.533344], [6.653934, 1.667547, 7.455104], [7.62768, -0.681987, 7.376863], [9.978516, -1.655193, 7.344455], [12.329352, -0.681987, 7.376863], [13.303098, 1.667547, 7.455104]]}]},
			"C_torso_FK_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_A_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 101.196827, -13.633966], [-0.0, 101.388167, -13.672026], [-0.0, 101.550377, -13.780416], [-0.0, 101.658767, -13.942626], [-0.0, 101.696827, -14.133966], [-0.0, 101.658767, -14.325306], [-0.0, 101.550377, -14.487516], [-0.0, 101.388167, -14.595906], [-0.0, 101.196827, -14.633966], [-0.0, 101.005487, -14.595906], [-0.0, 100.843277, -14.487516], [-0.0, 100.734887, -14.325306], [-0.0, 100.696827, -14.133966], [-0.0, 100.734887, -13.942626], [-0.0, 100.843277, -13.780416], [-0.0, 101.005487, -13.672026], [-0.0, 101.196827, -13.633966], [-0.0, 101.196827, -8.633966]]}]},
			"L_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[57.807642, 100.742528, -7.270903], [57.794152, 100.748227, -7.266318], [57.786846, 100.737247, -7.274163], [57.800336, 100.731548, -7.278749], [57.807642, 100.742528, -7.270903], [57.797504, 100.733468, -7.26379], [57.786846, 100.737247, -7.274163], [57.796985, 100.746308, -7.281277], [57.794152, 100.748227, -7.266318], [57.797504, 100.733468, -7.26379], [57.800336, 100.731548, -7.278749], [57.796985, 100.746308, -7.281277], [57.807642, 100.742528, -7.270903], [57.797504, 100.733468, -7.26379], [57.772776, 101.345592, -8.097412]]}, {"shapeName": "L_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[57.491471, 102.13499, -7.509417], [57.480814, 102.13877, -7.519791], [57.470675, 102.12971, -7.512677], [57.481333, 102.125929, -7.502303], [57.491471, 102.13499, -7.509417], [57.477982, 102.140689, -7.504832], [57.470675, 102.12971, -7.512677], [57.484165, 102.12401, -7.517262], [57.480814, 102.13877, -7.519791], [57.477982, 102.140689, -7.504832], [57.481333, 102.125929, -7.502303], [57.484165, 102.12401, -7.517262], [57.491471, 102.13499, -7.509417], [57.477982, 102.140689, -7.504832], [57.772776, 101.345592, -8.097412]]}, {"shapeName": "L_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[56.788759, 101.104861, -8.244991], [56.791591, 101.102942, -8.25995], [56.794943, 101.088182, -8.257422], [56.79211, 101.090101, -8.242463], [56.788759, 101.104861, -8.244991], [56.781454, 101.093881, -8.252836], [56.794943, 101.088182, -8.257422], [56.802249, 101.099161, -8.249576], [56.791591, 101.102942, -8.25995], [56.781454, 101.093881, -8.252836], [56.79211, 101.090101, -8.242463], [56.802249, 101.099161, -8.249576], [56.788759, 101.104861, -8.244991], [56.781454, 101.093881, -8.252836], [57.772776, 101.345592, -8.097412]]}]},
			"L_leg_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[24.90934, 9.690671, -5.42703], [24.301416, 9.690671, -5.42703], [24.186285, 9.074237, -5.522688], [23.754293, 8.897366, -5.550135], [23.231747, 9.252806, -5.494978], [22.801875, 8.828018, -5.560896], [23.16155, 8.311709, -5.641017], [22.982639, 7.884769, -5.707269], [22.358769, 7.771001, -5.724924], [22.358769, 7.170247, -5.818149], [22.982639, 7.056479, -5.835803], [23.16155, 6.629596, -5.902047], [22.801875, 6.11323, -5.982176], [23.231747, 5.688442, -6.048095], [23.754293, 6.043882, -5.992938], [24.186285, 5.867011, -6.020385], [24.301416, 5.250577, -6.116043], [24.90934, 5.250577, -6.116043], [25.024528, 5.867011, -6.020385], [25.45652, 6.043882, -5.992938], [25.979066, 5.688442, -6.048095], [26.4089, 6.11323, -5.982176], [26.049263, 6.629596, -5.902047], [26.228174, 7.056479, -5.835803], [26.851987, 7.170247, -5.818149], [26.851987, 7.771001, -5.724924], [26.228174, 7.884769, -5.707269], [26.049263, 8.311709, -5.641017], [26.4089, 8.828018, -5.560896], [25.979066, 9.252806, -5.494978], [25.45652, 8.897366, -5.550135], [25.024528, 9.074237, -5.522688], [24.90934, 9.690671, -5.42703]]}, {"shapeName": "L_leg_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[25.265253, 8.122704, -5.670347], [25.538595, 7.470624, -5.771536], [25.265253, 6.818544, -5.872726], [24.605387, 6.548491, -5.914633], [23.94556, 6.818544, -5.872726], [23.672218, 7.470624, -5.771536], [23.94556, 8.122704, -5.670347], [24.605387, 8.392756, -5.62844]]}, {"shapeName": "L_leg_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[22.358769, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}]},
			"L_arm_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_CTLShape", "degree": 1, "form": 0, "points": [[61.067409, 107.982856, -5.669953], [53.557037, 100.676969, -5.556279], [55.49652, 98.526518, -15.62646], [63.006892, 105.832404, -15.740134], [63.570664, 105.256456, -15.508562], [56.060292, 97.95057, -15.394888], [54.120809, 100.101022, -5.324706], [61.631181, 107.406908, -5.43838], [61.067409, 107.982856, -5.669953], [63.006892, 105.832404, -15.740134], [55.49652, 98.526518, -15.62646], [56.060292, 97.95057, -15.394888], [63.570664, 105.256456, -15.508562], [61.631181, 107.406908, -5.43838], [54.120809, 100.101022, -5.324706], [53.557037, 100.676969, -5.556279]]}]},
			"L_legBase_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 86.224395, -4.523498], [9.978517, 78.471454, -3.256981], [9.978517, 75.510088, -2.773213], [9.978517, 81.449217, 14.971289], [9.978517, 91.042519, 24.970473], [9.978517, 100.625727, 23.404964], [9.978517, 106.538307, 10.872744], [9.978517, 106.52191, -7.839293], [9.978517, 103.560544, -7.355525], [9.978517, 95.807603, -6.089008], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}]},
			"L_outterBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_outterBall_CTLShape", "degree": 1, "form": 0, "points": [[16.978517, 2.42481, 5.227414], [16.978517, 1.471674, 4.18265], [17.978517, 2.470624, 4.228464], [16.978517, 2.42481, 5.227414], [15.978517, 2.470624, 4.228464], [16.978517, 1.471674, 4.18265], [16.978517, 2.516438, 3.229514], [15.978517, 2.470624, 4.228464], [16.978517, 3.469574, 4.274277], [16.978517, 2.42481, 5.227414], [17.978517, 2.470624, 4.228464], [16.978517, 2.516438, 3.229514], [16.978517, 3.469574, 4.274277], [17.978517, 2.470624, 4.228464]]}]},
			"C_midTorso_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[13.314499, 113.683497, -19.729381], [-0.0, 113.683497, -24.325243], [-13.314499, 113.683497, -19.729381], [-18.829533, 113.683497, -8.633966], [-13.314499, 113.683497, 2.46145], [-0.0, 113.683497, 7.057312], [13.314499, 113.683497, 2.46145], [18.829533, 113.683497, -8.633966]]}]},
			"L_toe_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[12.721158, 4.408669, 7.546385], [9.978516, 5.544077, 7.584194], [7.235874, 4.408669, 7.546385], [6.099837, 1.667547, 7.455104], [7.235874, -1.073576, 7.363823], [9.978516, -2.208983, 7.326014], [12.721158, -1.073576, 7.363823], [13.857195, 1.667547, 7.455104]]}]},
			"C_cog_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[26.980938, 98.683497, -6.692288], [26.95248, 98.683497, -10.936931], [19.628217, 98.683497, -13.485569], [18.6273, 98.683497, -16.497581], [22.969305, 98.683497, -22.922123], [20.451366, 98.683497, -26.339378], [13.026744, 98.683497, -24.1007], [10.447299, 98.683497, -25.949255], [10.184211, 98.683497, -33.69434], [6.138504, 98.683497, -34.978973], [1.449495, 98.683497, -28.808042], [-1.723221, 98.683497, -28.787063], [-6.490935, 98.683497, -34.894355], [-10.519038, 98.683497, -33.555641], [-10.681416, 98.683497, -25.809584], [-13.235535, 98.683497, -23.92709], [-20.686752, 98.683497, -26.063789], [-23.158683, 98.683497, -22.613081], [-18.732384, 98.683497, -16.250612], [-19.692315, 98.683497, -13.225667], [-26.980938, 98.683497, -10.575644], [-26.95248, 98.683497, -6.331001], [-19.628217, 98.683497, -3.782363], [-18.6273, 98.683497, -0.770351], [-22.969305, 98.683497, 5.654191], [-20.451366, 98.683497, 9.071446], [-13.026744, 98.683497, 6.832768], [-10.447299, 98.683497, 8.681323], [-10.184211, 98.683497, 16.426408], [-6.138504, 98.683497, 17.711041], [-1.449495, 98.683497, 11.54011], [1.723221, 98.683497, 11.519131], [6.490935, 98.683497, 17.626423], [10.519038, 98.683497, 16.287709], [10.681416, 98.683497, 8.541652], [13.235535, 98.683497, 6.659158], [20.686752, 98.683497, 8.795857], [23.158683, 98.683497, 5.345149], [18.732384, 98.683497, -1.01732], [19.692315, 98.683497, -4.042265], [26.980938, 98.683497, -6.692288]]}]},
			"L_arm_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[64.114408, 113.549716, -11.723364], [63.955811, 113.09772, -11.657388], [63.466138, 113.155993, -11.764141], [63.221556, 112.876085, -11.751473], [63.350263, 112.404612, -11.626003], [62.921378, 112.184142, -11.661525], [62.630231, 112.572067, -11.800438], [62.265213, 112.538691, -11.863612], [62.017625, 112.101393, -11.817913], [61.56968, 112.241606, -11.934128], [61.647607, 112.732009, -12.023844], [61.375981, 112.964663, -12.12584], [60.897125, 112.81776, -12.186696], [60.692533, 113.236516, -12.315523], [61.093887, 113.542074, -12.303475], [61.074704, 113.904543, -12.384573], [60.645102, 114.134016, -12.516316], [60.8037, 114.586011, -12.582293], [61.293388, 114.527781, -12.475546], [61.537969, 114.807689, -12.488213], [61.409263, 115.279162, -12.613683], [61.838138, 115.499603, -12.578158], [62.129337, 115.111694, -12.439237], [62.494313, 115.145083, -12.376074], [62.741886, 115.582338, -12.421767], [63.189831, 115.442125, -12.305552], [63.111919, 114.951764, -12.215843], [63.383587, 114.719097, -12.113835], [63.86239, 114.865985, -12.052987], [64.066993, 114.447258, -11.924163], [63.665639, 114.1417, -11.936212], [63.684821, 113.779231, -11.855113], [64.114408, 113.549716, -11.723364]]}, {"shapeName": "L_arm_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[63.038123, 114.180294, -12.065311], [62.623216, 114.535718, -12.22112], [62.065689, 114.484679, -12.317599], [61.69218, 114.057094, -12.298226], [61.721403, 113.503479, -12.174375], [62.136309, 113.148056, -12.018566], [62.693837, 113.199095, -11.922088], [63.067336, 113.626652, -11.941456]]}, {"shapeName": "L_arm_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[61.793652, 112.171499, -11.876021], [58.56385, 102.966713, -10.53242]]}]},
			"C_hip_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[19.041772, 98.683497, -24.502109], [-0.0, 90.583497, -31.074894], [-19.041772, 98.683497, -24.502109], [-26.929114, 106.783497, -8.633966], [-19.041772, 98.683497, 7.234177], [-0.0, 90.583497, 13.806963], [19.041772, 98.683497, 7.234177], [26.929114, 106.783497, -8.633966]]}]},
			"L_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.349614, 92.441652, -2.936398], [66.353091, 92.44772, -2.922739], [66.338642, 92.445494, -2.918072], [66.335165, 92.439426, -2.931732], [66.349614, 92.441652, -2.936398], [66.346833, 92.433733, -2.923552], [66.338642, 92.445494, -2.918072], [66.341422, 92.453415, -2.930919], [66.353091, 92.44772, -2.922739], [66.346833, 92.433733, -2.923552], [66.335165, 92.439426, -2.931732], [66.341422, 92.453415, -2.930919], [66.349614, 92.441652, -2.936398], [66.346833, 92.433733, -2.923552], [66.08888, 93.372015, -3.274723]]}, {"shapeName": "L_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[66.939902, 93.761304, -2.859712], [66.931711, 93.773067, -2.854232], [66.928931, 93.765147, -2.841386], [66.937122, 93.753384, -2.846865], [66.939902, 93.761304, -2.859712], [66.943379, 93.767372, -2.846053], [66.928931, 93.765147, -2.841386], [66.925454, 93.759079, -2.855045], [66.931711, 93.773067, -2.854232], [66.943379, 93.767372, -2.846053], [66.937122, 93.753384, -2.846865], [66.925454, 93.759079, -2.855045], [66.939902, 93.761304, -2.859712], [66.943379, 93.767372, -2.846053], [66.08888, 93.372015, -3.274723]]}, {"shapeName": "L_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.580331, 93.557415, -2.405801], [65.568663, 93.563109, -2.41398], [65.562406, 93.549121, -2.414793], [65.574074, 93.543426, -2.406613], [65.580331, 93.557415, -2.405801], [65.565883, 93.555189, -2.401135], [65.562406, 93.549121, -2.414793], [65.576854, 93.551346, -2.41946], [65.568663, 93.563109, -2.41398], [65.565883, 93.555189, -2.401135], [65.574074, 93.543426, -2.406613], [65.576854, 93.551346, -2.41946], [65.580331, 93.557415, -2.405801], [65.565883, 93.555189, -2.401135], [66.08888, 93.372015, -3.274723]]}]},
			"L_leg_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[13.504771, 7.470624, -11.648626], [9.978517, 7.470624, -14.082991], [6.452263, 7.470624, -11.648626], [4.991644, 7.470624, -5.771536], [6.452263, 7.470624, 0.105554], [9.978517, 7.470624, 2.539919], [13.504771, 7.470624, 0.105554], [14.96539, 7.470624, -5.771536]]}]},
			"C_chest_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[14.810267, 126.183497, -20.975855], [-0.0, 132.483497, -26.088021], [-14.810267, 126.183497, -20.975855], [-20.944867, 119.883497, -8.633966], [-14.810267, 126.183497, 3.707923], [-0.0, 132.483497, 8.82009], [14.810267, 126.183497, 3.707923], [20.944867, 119.883497, -8.633966]]}]},
			"L_shoulder_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_CTLShape", "degree": 3, "form": 0, "points": [[4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [5.714113, 144.86207, 1.619553], [8.139691, 142.172649, 6.236833], [9.066181, 141.145379, 8.000481], [26.660943, 140.63155, -4.390502], [35.682141, 142.368519, -15.575843], [32.683949, 145.692842, -21.283143], [18.811597, 149.334715, -19.332363], [-0.636146, 151.903083, -10.468676], [0.290344, 150.875813, -8.705028], [2.715921, 148.186392, -4.087747], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097]]}]},
			"C_chest_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_chest_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 131.301852, -8.688221], [-0.054255, 131.301852, -8.633966], [-0.0, 131.301852, -8.579711], [0.054255, 131.301852, -8.633966], [-0.0, 131.301852, -8.688221], [-0.0, 131.356102, -8.633966], [-0.0, 131.301852, -8.579711], [-0.0, 131.247597, -8.633966], [-0.054255, 131.301852, -8.633966], [-0.0, 131.356102, -8.633966], [0.054255, 131.301852, -8.633966], [-0.0, 131.247597, -8.633966], [-0.0, 131.301852, -8.688221], [-0.0, 131.356102, -8.633966], [-0.0, 126.183497, -8.633966]]}, {"shapeName": "C_chest_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 126.183497, -8.688221], [-5.118355, 126.129242, -8.633966], [-5.118355, 126.183497, -8.579711], [-5.118355, 126.237752, -8.633966], [-5.118355, 126.183497, -8.688221], [-5.172605, 126.183497, -8.633966], [-5.118355, 126.183497, -8.579711], [-5.0641, 126.183497, -8.633966], [-5.118355, 126.129242, -8.633966], [-5.172605, 126.183497, -8.633966], [-5.118355, 126.237752, -8.633966], [-5.0641, 126.183497, -8.633966], [-5.118355, 126.183497, -8.688221], [-5.172605, 126.183497, -8.633966], [-0.0, 126.183497, -8.633966]]}, {"shapeName": "C_chest_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 126.183497, -3.515611], [-0.0, 126.129242, -3.515611], [0.054255, 126.183497, -3.515611], [-0.0, 126.237752, -3.515611], [-0.054255, 126.183497, -3.515611], [-0.0, 126.183497, -3.461361], [0.054255, 126.183497, -3.515611], [-0.0, 126.183497, -3.569866], [-0.0, 126.129242, -3.515611], [-0.0, 126.183497, -3.461361], [-0.0, 126.237752, -3.515611], [-0.0, 126.183497, -3.569866], [-0.054255, 126.183497, -3.515611], [-0.0, 126.183497, -3.461361], [-0.0, 126.183497, -8.633966]]}]},
			"L_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_C_CTLShape", "degree": 3, "form": 2, "points": [[58.603667, 95.31383, -2.227553], [58.621396, 95.379362, -2.119952], [58.54584, 95.420713, -2.026316], [58.421258, 95.413662, -2.001494], [58.320628, 95.362338, -2.060027], [58.302899, 95.296806, -2.167627], [58.378455, 95.255455, -2.261264], [58.503037, 95.262506, -2.286086]]}]},
			"C_midTorso_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_midTorso_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 113.683497, -8.688221], [5.118355, 113.737752, -8.633966], [5.118355, 113.683497, -8.579711], [5.118355, 113.629242, -8.633966], [5.118355, 113.683497, -8.688221], [5.172605, 113.683497, -8.633966], [5.118355, 113.683497, -8.579711], [5.0641, 113.683497, -8.633966], [5.118355, 113.737752, -8.633966], [5.172605, 113.683497, -8.633966], [5.118355, 113.629242, -8.633966], [5.0641, 113.683497, -8.633966], [5.118355, 113.683497, -8.688221], [5.172605, 113.683497, -8.633966], [-0.0, 113.683497, -8.633966]]}, {"shapeName": "C_midTorso_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.0, 118.801852, -8.688221], [-0.054255, 118.801852, -8.633966], [-0.0, 118.801852, -8.579711], [0.054255, 118.801852, -8.633966], [-0.0, 118.801852, -8.688221], [-0.0, 118.856102, -8.633966], [-0.0, 118.801852, -8.579711], [-0.0, 118.747597, -8.633966], [-0.054255, 118.801852, -8.633966], [-0.0, 118.856102, -8.633966], [0.054255, 118.801852, -8.633966], [-0.0, 118.747597, -8.633966], [-0.0, 118.801852, -8.688221], [-0.0, 118.856102, -8.633966], [-0.0, 113.683497, -8.633966]]}, {"shapeName": "C_midTorso_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.0, 113.737752, -3.515611], [-0.054255, 113.683497, -3.515611], [-0.0, 113.629242, -3.515611], [0.054255, 113.683497, -3.515611], [-0.0, 113.737752, -3.515611], [-0.0, 113.683497, -3.461361], [-0.0, 113.629242, -3.515611], [-0.0, 113.683497, -3.569866], [-0.054255, 113.683497, -3.515611], [-0.0, 113.683497, -3.461361], [0.054255, 113.683497, -3.515611], [-0.0, 113.683497, -3.569866], [-0.0, 113.737752, -3.515611], [-0.0, 113.683497, -3.461361], [-0.0, 113.683497, -8.633966]]}]},
			"C_visibility_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_visibility_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.523671, 200.0, -0.010851], [1.523671, 200.010851, 0.0], [1.523671, 200.0, 0.010851], [1.523671, 199.989149, 0.0], [1.523671, 200.0, -0.010851], [1.534521, 200.0, 0.0], [1.523671, 200.0, 0.010851], [1.51282, 200.0, 0.0], [1.523671, 200.010851, 0.0], [1.534521, 200.0, 0.0], [1.523671, 199.989149, 0.0], [1.51282, 200.0, 0.0], [1.523671, 200.0, -0.010851], [1.534521, 200.0, 0.0], [0.5, 200.0, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.5, 201.023671, -0.010851], [0.489149, 201.023671, 0.0], [0.5, 201.023671, 0.010851], [0.510851, 201.023671, 0.0], [0.5, 201.023671, -0.010851], [0.5, 201.034521, 0.0], [0.5, 201.023671, 0.010851], [0.5, 201.01282, 0.0], [0.489149, 201.023671, 0.0], [0.5, 201.034521, 0.0], [0.510851, 201.023671, 0.0], [0.5, 201.01282, 0.0], [0.5, 201.023671, -0.010851], [0.5, 201.034521, 0.0], [0.5, 200.0, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.5, 200.010851, 1.023671], [0.489149, 200.0, 1.023671], [0.5, 199.989149, 1.023671], [0.510851, 200.0, 1.023671], [0.5, 200.010851, 1.023671], [0.5, 200.0, 1.034521], [0.5, 199.989149, 1.023671], [0.5, 200.0, 1.01282], [0.489149, 200.0, 1.023671], [0.5, 200.0, 1.034521], [0.510851, 200.0, 1.023671], [0.5, 200.0, 1.01282], [0.5, 200.010851, 1.023671], [0.5, 200.0, 1.034521], [0.5, 200.0, 0.0]]}]},
			"L_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_C_CTLShape", "degree": 3, "form": 2, "points": [[66.051215, 93.306282, -3.422684], [66.172916, 93.342582, -3.415093], [66.24539, 93.396123, -3.325274], [66.226182, 93.435541, -3.205843], [66.126545, 93.437747, -3.126761], [66.004844, 93.401447, -3.134353], [65.932369, 93.347906, -3.224171], [65.951577, 93.308488, -3.343602]]}]},
			"L_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.676398, 89.28079, -10.816365], [68.687307, 89.28072, -10.805573], [68.676526, 89.27994, -10.79468], [68.665617, 89.280009, -10.805473], [68.676398, 89.28079, -10.816365], [68.676816, 89.269529, -10.80595], [68.676526, 89.27994, -10.79468], [68.676109, 89.291202, -10.805096], [68.687307, 89.28072, -10.805573], [68.676816, 89.269529, -10.80595], [68.665617, 89.280009, -10.805473], [68.676109, 89.291202, -10.805096], [68.676398, 89.28079, -10.816365], [68.676816, 89.269529, -10.80595], [68.643116, 90.302699, -10.765232]]}, {"shapeName": "L_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[69.666162, 90.336681, -10.780782], [69.665873, 90.347093, -10.769513], [69.66629, 90.335831, -10.759097], [69.66658, 90.325419, -10.770367], [69.666162, 90.336681, -10.780782], [69.67707, 90.336612, -10.76999], [69.66629, 90.335831, -10.759097], [69.655381, 90.3359, -10.76989], [69.665873, 90.347093, -10.769513], [69.67707, 90.336612, -10.76999], [69.66658, 90.325419, -10.770367], [69.655381, 90.3359, -10.76989], [69.666162, 90.336681, -10.780782], [69.67707, 90.336612, -10.76999], [68.643116, 90.302699, -10.765232]]}, {"shapeName": "L_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[68.659983, 90.262939, -9.742415], [68.648785, 90.27342, -9.741938], [68.638293, 90.262228, -9.742315], [68.649492, 90.251747, -9.742792], [68.659983, 90.262939, -9.742415], [68.649202, 90.262158, -9.731524], [68.638293, 90.262228, -9.742315], [68.649074, 90.263009, -9.753208], [68.648785, 90.27342, -9.741938], [68.649202, 90.262158, -9.731524], [68.649492, 90.251747, -9.742792], [68.649074, 90.263009, -9.753208], [68.659983, 90.262939, -9.742415], [68.649202, 90.262158, -9.731524], [68.643116, 90.302699, -10.765232]]}]},
			"C_torso_FK_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_C_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 111.183497, -13.633966], [-0.0, 111.374837, -13.672026], [-0.0, 111.537047, -13.780416], [-0.0, 111.645437, -13.942626], [-0.0, 111.683497, -14.133966], [-0.0, 111.645437, -14.325306], [-0.0, 111.537047, -14.487516], [-0.0, 111.374837, -14.595906], [-0.0, 111.183497, -14.633966], [-0.0, 110.992157, -14.595906], [-0.0, 110.829947, -14.487516], [-0.0, 110.721557, -14.325306], [-0.0, 110.683497, -14.133966], [-0.0, 110.721557, -13.942626], [-0.0, 110.829947, -13.780416], [-0.0, 110.992157, -13.672026], [-0.0, 111.183497, -13.633966], [-0.0, 111.183497, -8.633966]]}]},
			"world_B_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.019165, 0.0, 91.653046], [-40.728578, 0.0, 50.886931], [-30.535211, 0.0, 50.889057], [-30.530951, 0.0, 30.510255], [-50.909753, 0.0, 30.505995], [-50.911887, 0.0, 40.699363], [-91.653046, 0.0, -0.019165], [-50.886931, 0.0, -40.728578], [-50.889057, 0.0, -30.535211], [-30.510255, 0.0, -30.530951], [-30.505995, 0.0, -50.909753], [-40.699363, 0.0, -50.911887], [0.019165, 0.0, -91.653046], [40.728578, 0.0, -50.886931], [30.535211, 0.0, -50.889057], [30.530951, 0.0, -30.510255], [50.909753, 0.0, -30.505995], [50.911887, 0.0, -40.699363], [91.653046, 0.0, 0.019165], [50.886931, 0.0, 40.728578], [50.889057, 0.0, 30.535211], [30.510255, 0.0, 30.530951], [30.505995, 0.0, 50.909753], [40.699363, 0.0, 50.911887], [-0.019165, 0.0, 91.653046], [-7.9977, 0.111056, 83.813982], [-7.299474, 0.0, 83.06847], [-7.29884, 0.0, 80.022359], [-6.664233, 0.0, 80.022494], [-6.704539, 0.0, 83.092395], [-6.252334, 0.0, 82.862437], [-6.267921, 0.0, 81.529763], [-5.625382, 0.0, 81.529898], [-5.62566, 0.0, 82.862572], [-5.229078, 0.0, 83.092696], [-5.228428, 0.0, 79.975192], [-4.585889, 0.0, 79.975327], [-4.586555, 0.0, 83.172157], [-5.102284, 0.0, 83.687672], [-5.895455, 0.0, 83.290876], [-6.768126, 0.0, 83.687323], [-7.299482, 0.0, 83.084335], [-6.768126, 0.0, 83.687323], [-5.903387, 0.0, 83.298808], [-5.102276, 0.0, 83.679739], [-3.555431, 0.0, 83.687997], [-4.07887, 0.0, 83.172268], [-4.078315, 0.0, 80.498988], [-3.554653, 0.0, 79.975549], [-1.880879, 0.0, 79.975898], [-1.365372, 0.0, 80.499551], [-1.365927, 0.0, 83.172831], [-1.881656, 0.0, 83.688346], [-3.555431, 0.0, 83.687997], [-3.356989, 0.0, 83.093093], [-3.435799, 0.0, 80.633977], [-2.00001, 0.0, 80.650143], [-2.00845, 0.0, 83.09337], [-3.364922, 0.0, 83.108958], [-3.555431, 0.0, 83.687997], [-1.881656, 0.0, 83.688346], [-0.810757, 0.0, 83.688568], [-0.849643, 0.0, 79.976112], [0.958986, 0.0, 79.976485], [1.482425, 0.0, 80.500146], [1.482195, 0.0, 81.61864], [0.950601, 0.0, 82.134147], [0.918863, 0.0, 82.173802], [1.957721, 0.0, 83.673282], [1.957714, 0.0, 83.689147], [1.212051, 0.0, 83.688988], [0.1732, 0.0, 82.181584], [-0.215497, 0.0, 82.181504], [-0.215163, 0.0, 80.594988], [0.784342, 0.0, 80.595194], [0.792076, 0.0, 81.539172], [-0.215362, 0.0, 81.538965], [-0.215814, 0.0, 83.688695], [-0.810757, 0.0, 83.688568], [5.083151, 0.0, 83.689797], [5.083278, 0.0, 83.094854], [3.004941, 0.0, 83.086485], [3.005592, 0.0, 79.976913], [2.363053, 0.0, 79.976786], [2.362275, 0.0, 83.689226], [7.788161, 0.0, 83.690361], [8.264227, 0.0, 83.174846], [8.304445, 0.0, 80.501574], [7.788938, 0.0, 79.977921], [5.591613, 0.0, 79.97746], [5.590836, 0.0, 83.689909], [6.241434, 0.0, 83.0951], [6.226093, 0.0, 80.580464], [7.582564, 0.0, 80.580749], [7.566176, 0.0, 83.079512], [6.217637, 0.0, 83.110957], [5.574971, 0.0, 83.689901]]}]},
			"L_upLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 80.930699, -3.548774], [9.870007, 80.913205, -3.655864], [9.978517, 80.89571, -3.762955], [10.087027, 80.913205, -3.655864], [9.978517, 80.930699, -3.548774], [9.978517, 80.806124, -3.638372], [9.978517, 80.89571, -3.762955], [9.978517, 81.020295, -3.673359], [9.870007, 80.913205, -3.655864], [9.978517, 80.806124, -3.638372], [10.087027, 80.913205, -3.655864], [9.978517, 81.020295, -3.673359], [9.978517, 80.930699, -3.548774], [9.978517, 80.806124, -3.638372], [9.978517, 91.015999, -5.306253]]}, {"shapeName": "L_upLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.258193, 91.033493, -5.199162], [-0.258193, 91.123089, -5.323747], [-0.258193, 90.998505, -5.413343], [-0.258193, 90.908908, -5.288759], [-0.258193, 91.033493, -5.199162], [-0.366693, 91.015999, -5.306253], [-0.258193, 90.998505, -5.413343], [-0.149683, 91.015999, -5.306253], [-0.258193, 91.123089, -5.323747], [-0.366693, 91.015999, -5.306253], [-0.258193, 90.908908, -5.288759], [-0.149683, 91.015999, -5.306253], [-0.258193, 91.033493, -5.199162], [-0.366693, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}, {"shapeName": "L_upLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.870007, 89.36561, -15.409047], [9.978517, 89.472701, -15.426541], [10.087027, 89.36561, -15.409047], [9.978517, 89.25852, -15.391553], [9.870007, 89.36561, -15.409047], [9.978517, 89.348118, -15.516128], [10.087027, 89.36561, -15.409047], [9.978517, 89.383104, -15.301957], [9.978517, 89.472701, -15.426541], [9.978517, 89.348118, -15.516128], [9.978517, 89.25852, -15.391553], [9.978517, 89.383104, -15.301957], [9.870007, 89.36561, -15.409047], [9.978517, 89.348118, -15.516128], [9.978517, 91.015999, -5.306253]]}]},
			"C_torso_FK_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 121.301852, -8.688221], [-0.054255, 121.301852, -8.633966], [-0.0, 121.301852, -8.579711], [0.054255, 121.301852, -8.633966], [-0.0, 121.301852, -8.688221], [-0.0, 121.356102, -8.633966], [-0.0, 121.301852, -8.579711], [-0.0, 121.247597, -8.633966], [-0.054255, 121.301852, -8.633966], [-0.0, 121.356102, -8.633966], [0.054255, 121.301852, -8.633966], [-0.0, 121.247597, -8.633966], [-0.0, 121.301852, -8.688221], [-0.0, 121.356102, -8.633966], [-0.0, 116.183497, -8.633966]]}, {"shapeName": "C_torso_FK_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 116.183497, -8.688221], [-5.118355, 116.129242, -8.633966], [-5.118355, 116.183497, -8.579711], [-5.118355, 116.237752, -8.633966], [-5.118355, 116.183497, -8.688221], [-5.172605, 116.183497, -8.633966], [-5.118355, 116.183497, -8.579711], [-5.0641, 116.183497, -8.633966], [-5.118355, 116.129242, -8.633966], [-5.172605, 116.183497, -8.633966], [-5.118355, 116.237752, -8.633966], [-5.0641, 116.183497, -8.633966], [-5.118355, 116.183497, -8.688221], [-5.172605, 116.183497, -8.633966], [-0.0, 116.183497, -8.633966]]}, {"shapeName": "C_torso_FK_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 116.183497, -3.515611], [-0.0, 116.129242, -3.515611], [0.054255, 116.183497, -3.515611], [-0.0, 116.237752, -3.515611], [-0.054255, 116.183497, -3.515611], [-0.0, 116.183497, -3.461361], [0.054255, 116.183497, -3.515611], [-0.0, 116.183497, -3.569866], [-0.0, 116.129242, -3.515611], [-0.0, 116.183497, -3.461361], [-0.0, 116.237752, -3.515611], [-0.0, 116.183497, -3.569866], [-0.054255, 116.183497, -3.515611], [-0.0, 116.183497, -3.461361], [-0.0, 116.183497, -8.633966]]}]},
			"L_reverseBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_reverseBall_CTLShape", "degree": 1, "form": 0, "points": [[9.978516, 1.667547, 7.455104], [9.978516, 6.162822, 7.661266], [9.978516, 7.207586, 6.70813], [10.978516, 7.161772, 7.70708], [9.978516, 8.160722, 7.752893], [9.978516, 7.207586, 6.70813], [8.978516, 7.161772, 7.70708], [9.978516, 6.162822, 7.661266], [9.978516, 7.115958, 8.70603], [8.978516, 7.161772, 7.70708], [9.978516, 8.160722, 7.752893], [9.978516, 7.115958, 8.70603], [10.978516, 7.161772, 7.70708], [9.978516, 6.162822, 7.661266]]}]},
			"L_arm_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[67.814781, 120.605051, -12.517327], [67.550452, 119.851725, -12.407366], [66.734329, 119.948846, -12.585288], [66.326694, 119.482333, -12.564175], [66.541204, 118.696544, -12.355059], [65.826396, 118.329095, -12.414261], [65.341151, 118.975636, -12.645784], [64.732788, 118.920009, -12.751074], [64.320142, 118.19118, -12.674909], [63.573566, 118.424868, -12.8686], [63.703444, 119.242207, -13.018126], [63.250735, 119.629963, -13.18812], [62.452642, 119.385125, -13.289546], [62.111655, 120.083051, -13.504259], [62.780578, 120.592314, -13.484178], [62.748607, 121.196429, -13.619342], [62.032603, 121.578884, -13.838914], [62.296932, 122.332209, -13.948875], [63.11308, 122.235159, -13.770963], [63.520715, 122.701672, -13.792076], [63.306204, 123.487462, -14.001192], [64.020997, 123.854863, -13.941983], [64.506329, 123.208348, -13.710449], [65.114621, 123.263997, -13.605177], [65.527242, 123.992755, -13.681331], [66.273818, 123.759067, -13.48764], [66.143965, 122.941799, -13.338125], [66.596744, 122.55402, -13.168112], [67.39475, 122.798834, -13.066698], [67.735754, 122.100955, -12.851992], [67.066831, 121.591692, -12.872073], [67.098802, 120.987576, -12.736909], [67.814781, 120.605051, -12.517327]]}, {"shapeName": "L_arm_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[66.020971, 121.656015, -13.087238], [65.32946, 122.248387, -13.34692], [64.400248, 122.163323, -13.507718], [63.777732, 121.450681, -13.47543], [63.826438, 120.52799, -13.269012], [64.517949, 119.935618, -13.009331], [65.447161, 120.020683, -12.848533], [66.06966, 120.733277, -12.880814]]}, {"shapeName": "L_arm_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[63.946854, 118.308024, -12.771755], [58.56385, 102.966713, -10.53242]]}]},
			"C_cog_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[17.987292, 98.683497, -7.339514], [17.96832, 98.683497, -10.169276], [13.085478, 98.683497, -11.868368], [12.4182, 98.683497, -13.876376], [15.31287, 98.683497, -18.159404], [13.634244, 98.683497, -20.437574], [8.684496, 98.683497, -18.945122], [6.964866, 98.683497, -20.177492], [6.789474, 98.683497, -25.340882], [4.092336, 98.683497, -26.197304], [0.96633, 98.683497, -22.08335], [-1.148814, 98.683497, -22.069364], [-4.32729, 98.683497, -26.140892], [-7.012692, 98.683497, -25.248416], [-7.120944, 98.683497, -20.084378], [-8.82369, 98.683497, -18.829382], [-13.791168, 98.683497, -20.253848], [-15.439122, 98.683497, -17.953376], [-12.488256, 98.683497, -13.71173], [-13.12821, 98.683497, -11.6951], [-17.987292, 98.683497, -9.928418], [-17.96832, 98.683497, -7.098656], [-13.085478, 98.683497, -5.399564], [-12.4182, 98.683497, -3.391556], [-15.31287, 98.683497, 0.891472], [-13.634244, 98.683497, 3.169642], [-8.684496, 98.683497, 1.67719], [-6.964866, 98.683497, 2.90956], [-6.789474, 98.683497, 8.07295], [-4.092336, 98.683497, 8.929372], [-0.96633, 98.683497, 4.815418], [1.148814, 98.683497, 4.801432], [4.32729, 98.683497, 8.87296], [7.012692, 98.683497, 7.980484], [7.120944, 98.683497, 2.816446], [8.82369, 98.683497, 1.56145], [13.791168, 98.683497, 2.985916], [15.439122, 98.683497, 0.685444], [12.488256, 98.683497, -3.556202], [13.12821, 98.683497, -5.572832], [17.987292, 98.683497, -7.339514]]}]},
			"L_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_B_CTLShape", "degree": 3, "form": 2, "points": [[64.245994, 97.359775, -12.855202], [64.338622, 97.435276, -12.89886], [64.445132, 97.48459, -12.849764], [64.503131, 97.478829, -12.736673], [64.478644, 97.421367, -12.625835], [64.386016, 97.345865, -12.582177], [64.279506, 97.296551, -12.631273], [64.221508, 97.302313, -12.744364]]}]},
			"L_leg_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 17.707334, -5.880046], [9.870007, 17.707334, -5.771536], [9.978517, 17.707334, -5.663026], [10.087027, 17.707334, -5.771536], [9.978517, 17.707334, -5.880046], [9.978517, 17.815834, -5.771536], [9.978517, 17.707334, -5.663026], [9.978517, 17.598824, -5.771536], [9.870007, 17.707334, -5.771536], [9.978517, 17.815834, -5.771536], [10.087027, 17.707334, -5.771536], [9.978517, 17.598824, -5.771536], [9.978517, 17.707334, -5.880046], [9.978517, 17.815834, -5.771536], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_leg_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.258193, 7.470624, -5.880046], [-0.258193, 7.362114, -5.771536], [-0.258193, 7.470624, -5.663026], [-0.258193, 7.579134, -5.771536], [-0.258193, 7.470624, -5.880046], [-0.366693, 7.470624, -5.771536], [-0.258193, 7.470624, -5.663026], [-0.149683, 7.470624, -5.771536], [-0.258193, 7.362114, -5.771536], [-0.366693, 7.470624, -5.771536], [-0.258193, 7.579134, -5.771536], [-0.149683, 7.470624, -5.771536], [-0.258193, 7.470624, -5.880046], [-0.366693, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_leg_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.870007, 7.470624, 4.465174], [9.978517, 7.362114, 4.465174], [10.087027, 7.470624, 4.465174], [9.978517, 7.579134, 4.465174], [9.870007, 7.470624, 4.465174], [9.978517, 7.470624, 4.573674], [10.087027, 7.470624, 4.465174], [9.978517, 7.470624, 4.356664], [9.978517, 7.362114, 4.465174], [9.978517, 7.470624, 4.573674], [9.978517, 7.579134, 4.465174], [9.978517, 7.470624, 4.356664], [9.870007, 7.470624, 4.465174], [9.978517, 7.470624, 4.573674], [9.978517, 7.470624, -5.771536]]}]},
			"L_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_B_CTLShape", "degree": 3, "form": 2, "points": [[58.029331, 98.470742, -4.303342], [58.046892, 98.542154, -4.199523], [57.971239, 98.588371, -4.10827], [57.846687, 98.582319, -4.083039], [57.746197, 98.527544, -4.138608], [57.728635, 98.456132, -4.242427], [57.804289, 98.409915, -4.33368], [57.928841, 98.415967, -4.358912]]}]},
			"L_loLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 41.644398, -0.358648], [9.870007, 41.661038, -0.465875], [9.978517, 41.677677, -0.573101], [10.087027, 41.661038, -0.465875], [9.978517, 41.644398, -0.358648], [9.978517, 41.553821, -0.482513], [9.978517, 41.677677, -0.573101], [9.978517, 41.768264, -0.449235], [9.870007, 41.661038, -0.465875], [9.978517, 41.553821, -0.482513], [10.087027, 41.661038, -0.465875], [9.978517, 41.768264, -0.449235], [9.978517, 41.644398, -0.358648], [9.978517, 41.553821, -0.482513], [9.978517, 51.776676, 1.103868]]}, {"shapeName": "L_loLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.258193, 51.760037, 1.211095], [-0.258193, 51.883903, 1.120507], [-0.258193, 51.793316, 0.996641], [-0.258193, 51.66945, 1.087229], [-0.258193, 51.760037, 1.211095], [-0.366693, 51.776676, 1.103868], [-0.258193, 51.793316, 0.996641], [-0.149683, 51.776676, 1.103868], [-0.258193, 51.883903, 1.120507], [-0.366693, 51.776676, 1.103868], [-0.258193, 51.66945, 1.087229], [-0.149683, 51.776676, 1.103868], [-0.258193, 51.760037, 1.211095], [-0.366693, 51.776676, 1.103868], [9.978517, 51.776676, 1.103868]]}, {"shapeName": "L_loLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.870007, 53.346419, -9.01177], [9.978517, 53.453646, -8.995131], [10.087027, 53.346419, -9.01177], [9.978517, 53.239192, -9.02841], [9.870007, 53.346419, -9.01177], [9.978517, 53.363057, -9.118987], [10.087027, 53.346419, -9.01177], [9.978517, 53.32978, -8.904544], [9.978517, 53.453646, -8.995131], [9.978517, 53.363057, -9.118987], [9.978517, 53.239192, -9.02841], [9.978517, 53.32978, -8.904544], [9.870007, 53.346419, -9.01177], [9.978517, 53.363057, -9.118987], [9.978517, 51.776676, 1.103868]]}]},
			"L_arm_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[66.889688, 118.841217, -12.318836], [66.651791, 118.163224, -12.219871], [65.917281, 118.250633, -12.380001], [65.550409, 117.830771, -12.361], [65.743469, 117.123561, -12.172795], [65.100141, 116.792857, -12.226077], [64.663421, 117.374744, -12.434448], [64.115894, 117.324679, -12.529208], [63.744512, 116.668733, -12.46066], [63.072595, 116.879052, -12.634982], [63.189485, 117.614658, -12.769555], [62.782046, 117.963638, -12.92255], [62.063763, 117.743283, -13.013833], [61.756875, 118.371417, -13.207075], [62.358905, 118.829754, -13.189002], [62.330131, 119.373458, -13.31065], [61.685728, 119.717667, -13.508264], [61.923624, 120.39566, -13.607229], [62.658157, 120.308315, -13.447108], [63.025029, 120.728176, -13.46611], [62.831969, 121.435387, -13.654315], [63.475282, 121.766048, -13.601027], [63.912081, 121.184184, -13.392646], [64.459544, 121.234268, -13.297901], [64.830903, 121.890151, -13.36644], [65.502821, 121.679832, -13.192118], [65.385953, 120.94429, -13.057554], [65.793455, 120.595289, -12.904543], [66.51166, 120.815622, -12.81327], [66.818564, 120.18753, -12.620035], [66.216533, 119.729194, -12.638108], [66.245307, 119.18549, -12.51646], [66.889688, 118.841217, -12.318836]]}, {"shapeName": "L_arm_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[65.275259, 119.787085, -12.831757], [64.652899, 120.32022, -13.06547], [63.816609, 120.243662, -13.210188], [63.256344, 119.602284, -13.181129], [63.300179, 118.771863, -12.995353], [63.922539, 118.238728, -12.76164], [64.75883, 118.315286, -12.616922], [65.319079, 118.956621, -12.645974]]}, {"shapeName": "L_arm_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[63.408553, 116.773893, -12.547821], [58.56385, 102.966713, -10.53242]]}]},
			"L_reverseBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_reverseBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[20.215226, 1.672518, 7.346708], [20.215226, 1.775943, 7.460075], [20.215226, 1.662576, 7.5635], [20.215226, 1.559151, 7.450133], [20.215226, 1.672518, 7.346708], [20.323726, 1.667547, 7.455104], [20.215226, 1.662576, 7.5635], [20.106716, 1.667547, 7.455104], [20.215226, 1.775943, 7.460075], [20.323726, 1.667547, 7.455104], [20.215226, 1.559151, 7.450133], [20.106716, 1.667547, 7.455104], [20.215226, 1.672518, 7.346708], [20.323726, 1.667547, 7.455104], [9.978516, 1.667547, 7.455104]]}, {"shapeName": "L_reverseBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[9.978516, 11.89848, 7.81569], [9.870006, 11.893508, 7.924086], [9.978516, 11.888537, 8.032482], [10.087026, 11.893508, 7.924086], [9.978516, 11.89848, 7.81569], [9.978516, 12.001894, 7.929057], [9.978516, 11.888537, 8.032482], [9.978516, 11.785112, 7.919115], [9.870006, 11.893508, 7.924086], [9.978516, 12.001894, 7.929057], [10.087026, 11.893508, 7.924086], [9.978516, 11.785112, 7.919115], [9.978516, 11.89848, 7.81569], [9.978516, 12.001894, 7.929057], [9.978516, 1.667547, 7.455104]]}, {"shapeName": "L_reverseBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.978516, 1.306961, 17.686037], [9.870006, 1.198565, 17.681065], [9.978516, 1.090169, 17.676094], [10.087026, 1.198565, 17.681065], [9.978516, 1.306961, 17.686037], [9.978516, 1.193594, 17.789452], [9.978516, 1.090169, 17.676094], [9.978516, 1.203536, 17.572669], [9.870006, 1.198565, 17.681065], [9.978516, 1.193594, 17.789452], [10.087026, 1.198565, 17.681065], [9.978516, 1.203536, 17.572669], [9.978516, 1.306961, 17.686037], [9.978516, 1.193594, 17.789452], [9.978516, 1.667547, 7.455104]]}]},
			"L_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[64.88486, 96.570868, -13.061545], [64.895599, 96.573711, -13.050958], [64.887954, 96.565031, -13.040873], [64.877215, 96.562188, -13.05146], [64.88486, 96.570868, -13.061545], [64.891962, 96.55923, -13.054502], [64.887954, 96.565031, -13.040873], [64.880852, 96.576669, -13.047915], [64.895599, 96.573711, -13.050958], [64.891962, 96.55923, -13.054502], [64.877215, 96.562188, -13.05146], [64.880852, 96.576669, -13.047915], [64.88486, 96.570868, -13.061545], [64.891962, 96.55923, -13.054502], [64.362319, 97.390571, -12.740519]]}, {"shapeName": "L_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.227916, 97.936998, -12.727175], [65.223908, 97.9428, -12.713545], [65.23101, 97.931162, -12.706503], [65.235019, 97.92536, -12.720132], [65.227916, 97.936998, -12.727175], [65.238654, 97.939841, -12.716588], [65.23101, 97.931162, -12.706503], [65.220271, 97.928319, -12.71709], [65.223908, 97.9428, -12.713545], [65.238654, 97.939841, -12.716588], [65.235019, 97.92536, -12.720132], [65.220271, 97.928319, -12.71709], [65.227916, 97.936998, -12.727175], [65.238654, 97.939841, -12.716588], [64.362319, 97.390571, -12.740519]]}, {"shapeName": "L_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[64.51744, 97.121025, -11.765171], [64.502693, 97.123984, -11.762129], [64.499056, 97.109503, -11.765673], [64.513803, 97.106544, -11.768715], [64.51744, 97.121025, -11.765171], [64.509795, 97.112346, -11.755087], [64.499056, 97.109503, -11.765673], [64.506701, 97.118182, -11.775758], [64.502693, 97.123984, -11.762129], [64.509795, 97.112346, -11.755087], [64.513803, 97.106544, -11.768715], [64.506701, 97.118182, -11.775758], [64.51744, 97.121025, -11.765171], [64.509795, 97.112346, -11.755087], [64.362319, 97.390571, -12.740519]]}]},
			"L_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[61.755258, 100.483163, -9.294973], [61.760281, 100.492128, -9.283577], [61.749637, 100.486219, -9.274236], [61.744613, 100.477254, -9.285632], [61.755258, 100.483163, -9.294973], [61.759409, 100.47694, -9.281575], [61.749637, 100.486219, -9.274236], [61.745485, 100.492443, -9.287634], [61.760281, 100.492128, -9.283577], [61.759409, 100.47694, -9.281575], [61.744613, 100.477254, -9.285632], [61.745485, 100.492443, -9.287634], [61.755258, 100.483163, -9.294973], [61.759409, 100.47694, -9.281575], [61.095652, 101.216011, -9.570426]]}, {"shapeName": "L_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[61.837531, 101.916115, -9.483878], [61.827758, 101.925395, -9.476539], [61.83191, 101.919171, -9.46314], [61.841682, 101.909891, -9.470479], [61.837531, 101.916115, -9.483878], [61.842554, 101.925079, -9.472482], [61.83191, 101.919171, -9.46314], [61.826886, 101.910205, -9.474536], [61.827758, 101.925395, -9.476539], [61.842554, 101.925079, -9.472482], [61.841682, 101.909891, -9.470479], [61.826886, 101.910205, -9.474536], [61.837531, 101.916115, -9.483878], [61.842554, 101.925079, -9.472482], [61.095652, 101.216011, -9.570426]]}, {"shapeName": "L_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[60.838344, 101.367622, -8.591229], [60.823547, 101.367937, -8.595286], [60.822675, 101.352748, -8.593284], [60.837472, 101.352433, -8.589227], [60.838344, 101.367622, -8.591229], [60.827699, 101.361713, -8.581889], [60.822675, 101.352748, -8.593284], [60.83332, 101.358657, -8.602625], [60.823547, 101.367937, -8.595286], [60.827699, 101.361713, -8.581889], [60.837472, 101.352433, -8.589227], [60.83332, 101.358657, -8.602625], [60.838344, 101.367622, -8.591229], [60.827699, 101.361713, -8.581889], [61.095652, 101.216011, -9.570426]]}]},
			"C_torso_FK_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_B_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 106.183497, -13.633966], [-0.0, 106.374837, -13.672026], [-0.0, 106.537047, -13.780416], [-0.0, 106.645437, -13.942626], [-0.0, 106.683497, -14.133966], [-0.0, 106.645437, -14.325306], [-0.0, 106.537047, -14.487516], [-0.0, 106.374837, -14.595906], [-0.0, 106.183497, -14.633966], [-0.0, 105.992157, -14.595906], [-0.0, 105.829947, -14.487516], [-0.0, 105.721557, -14.325306], [-0.0, 105.683497, -14.133966], [-0.0, 105.721557, -13.942626], [-0.0, 105.829947, -13.780416], [-0.0, 105.992157, -13.672026], [-0.0, 106.183497, -13.633966], [-0.0, 106.183497, -8.633966]]}]},
			"L_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[64.574533, 96.186411, -4.830278], [64.57707, 96.194725, -4.817631], [64.563432, 96.19042, -4.812066], [64.560895, 96.182107, -4.824713], [64.574533, 96.186411, -4.830278], [64.573622, 96.179819, -4.816451], [64.563432, 96.19042, -4.812066], [64.564342, 96.197014, -4.825893], [64.57707, 96.194725, -4.817631], [64.573622, 96.179819, -4.816451], [64.560895, 96.182107, -4.824713], [64.564342, 96.197014, -4.825893], [64.574533, 96.186411, -4.830278], [64.573622, 96.179819, -4.816451], [64.131249, 96.999544, -5.266552]]}, {"shapeName": "L_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[64.899761, 97.592695, -4.941617], [64.88957, 97.603298, -4.937233], [64.88866, 97.596705, -4.923406], [64.89885, 97.586102, -4.92779], [64.899761, 97.592695, -4.941617], [64.902297, 97.601008, -4.928971], [64.88866, 97.596705, -4.923406], [64.886123, 97.588391, -4.936052], [64.88957, 97.603298, -4.937233], [64.902297, 97.601008, -4.928971], [64.89885, 97.586102, -4.92779], [64.886123, 97.588391, -4.936052], [64.899761, 97.592695, -4.941617], [64.902297, 97.601008, -4.928971], [64.131249, 96.999544, -5.266552]]}, {"shapeName": "L_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[63.615712, 97.194963, -4.403967], [63.602984, 97.197252, -4.412229], [63.599537, 97.182346, -4.411049], [63.612264, 97.180056, -4.402787], [63.615712, 97.194963, -4.403967], [63.602074, 97.190659, -4.398403], [63.599537, 97.182346, -4.411049], [63.613175, 97.18665, -4.416614], [63.602984, 97.197252, -4.412229], [63.602074, 97.190659, -4.398403], [63.612264, 97.180056, -4.402787], [63.613175, 97.18665, -4.416614], [63.615712, 97.194963, -4.403967], [63.602074, 97.190659, -4.398403], [64.131249, 96.999544, -5.266552]]}]},
			"L_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[58.051838, 97.656149, -3.663784], [58.03877, 97.658771, -3.656181], [58.031063, 97.650534, -3.666585], [58.044132, 97.647912, -3.674189], [58.051838, 97.656149, -3.663784], [58.04308, 97.644377, -3.659294], [58.031063, 97.650534, -3.666585], [58.039822, 97.662307, -3.671076], [58.03877, 97.658771, -3.656181], [58.04308, 97.644377, -3.659294], [58.044132, 97.647912, -3.674189], [58.039822, 97.662307, -3.671076], [58.051838, 97.656149, -3.663784], [58.04308, 97.644377, -3.659294], [57.887764, 98.499143, -4.220975]]}, {"shapeName": "L_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[57.64519, 99.014167, -3.370135], [57.633174, 99.020325, -3.377427], [57.624415, 99.008552, -3.372936], [57.636432, 99.002394, -3.365644], [57.64519, 99.014167, -3.370135], [57.632122, 99.016788, -3.362532], [57.624415, 99.008552, -3.372936], [57.637484, 99.00593, -3.38054], [57.633174, 99.020325, -3.377427], [57.632122, 99.016788, -3.362532], [57.636432, 99.002394, -3.365644], [57.637484, 99.00593, -3.38054], [57.64519, 99.014167, -3.370135], [57.632122, 99.016788, -3.362532], [57.887764, 98.499143, -4.220975]]}, {"shapeName": "L_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[56.905137, 98.239701, -4.344077], [56.906189, 98.243237, -4.358973], [56.9105, 98.228842, -4.362086], [56.909447, 98.225306, -4.34719], [56.905137, 98.239701, -4.344077], [56.897432, 98.231464, -4.354482], [56.9105, 98.228842, -4.362086], [56.918206, 98.237079, -4.351681], [56.906189, 98.243237, -4.358973], [56.897432, 98.231464, -4.354482], [56.909447, 98.225306, -4.34719], [56.918206, 98.237079, -4.351681], [56.905137, 98.239701, -4.344077], [56.897432, 98.231464, -4.354482], [57.887764, 98.499143, -4.220975]]}]},
			"C_hip_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[12.694514, 98.683497, -19.212728], [-0.0, 93.283497, -23.594585], [-12.694514, 98.683497, -19.212728], [-17.952743, 104.083497, -8.633966], [-12.694514, 98.683497, 1.944796], [-0.0, 93.283497, 6.326653], [12.694514, 98.683497, 1.944796], [17.952743, 104.083497, -8.633966]]}]},
			"C_lookAt_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lookAt_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-3.984552, 169.17494, 71.178591], [-3.984552, 168.675324, 71.178591], [-3.984552, 168.675324, 70.678975], [-3.984552, 169.17494, 70.678975], [-3.984552, 169.17494, 71.178591], [3.984552, 169.17494, 71.178591], [3.984552, 168.675324, 71.178591], [3.984552, 168.675324, 70.678975], [3.984552, 169.17494, 70.678975], [3.984552, 169.17494, 71.178591], [3.984552, 168.675324, 71.178591], [-3.984552, 168.675324, 71.178591], [-3.984552, 168.675324, 70.678975], [3.984552, 168.675324, 70.678975], [3.984552, 169.17494, 70.678975], [-3.984552, 169.17494, 70.678975], [-3.984552, 169.17494, 71.178591], [-0.248, 169.173132, 71.176783], [-0.249808, 164.94058, 71.178591], [-0.249808, 164.94058, 70.678975], [0.249808, 164.94058, 70.678975], [0.249808, 164.94058, 71.178591], [-0.249808, 164.94058, 71.178591], [-0.249808, 172.909684, 71.178591], [0.249808, 172.909684, 71.178591], [0.249808, 172.909684, 70.678975], [-0.249808, 172.909684, 70.678975], [-0.249808, 172.909684, 71.178591], [-0.249808, 172.909684, 70.678975], [-0.249808, 164.94058, 70.678975], [0.249808, 164.94058, 70.678975], [0.249808, 172.909684, 70.678975], [0.249808, 172.909684, 71.178591], [0.249808, 164.94058, 71.178591], [0.248, 168.677132, 71.176783], [0.249808, 168.675324, 74.913335], [-0.249808, 168.675324, 74.913335], [-0.249808, 169.17494, 74.913335], [0.249808, 169.17494, 74.913335], [0.249808, 168.675324, 74.913335], [0.249808, 168.675324, 66.944231], [0.249808, 169.17494, 66.944231], [-0.249808, 169.17494, 66.944231], [-0.249808, 168.675324, 66.944231], [0.249808, 168.675324, 66.944231], [-0.249808, 168.675324, 66.944231], [-0.249808, 168.675324, 74.913335], [-0.249808, 169.17494, 74.913335], [-0.249808, 169.17494, 66.944231], [0.249808, 169.17494, 66.944231], [0.249808, 169.17494, 74.913335]]}]},
			"C_head_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[11.880025, 182.718046, -4.968417], [0.0, 187.344435, -4.968417], [-11.880025, 182.718046, -4.968417], [-16.800882, 171.548932, -4.968417], [-11.880025, 160.379818, -4.968417], [0.0, 155.75343, -4.968417], [11.880025, 160.379818, -4.968417], [16.800882, 171.548932, -4.968417]]}]},
			"L_ankleOffset_CTL": {"color": 20, "shapes": [{"shapeName": "L_ankleOffset_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 7.470624, -5.771536], [9.978516, 12.229085, -1.009207], [9.978516, 14.344816, -1.008347], [11.474564, 13.286521, 0.049088], [9.978516, 14.343957, 1.107384], [9.978516, 14.344816, -1.008347], [8.482468, 13.286521, 0.049088], [9.978516, 12.229085, -1.009207], [9.978516, 12.228225, 1.106524], [8.482468, 13.286521, 0.049088], [9.978516, 14.343957, 1.107384], [9.978516, 12.228225, 1.106524], [11.474564, 13.286521, 0.049088], [9.978516, 12.229085, -1.009207]]}]},
			"L_legEnd_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_legEnd_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, -2.661654, -7.234052], [9.870007, -2.645014, -7.341279], [9.978517, -2.628375, -7.448506], [10.087027, -2.645014, -7.341279], [9.978517, -2.661654, -7.234052], [9.978517, -2.752231, -7.357917], [9.978517, -2.628375, -7.448506], [9.978517, -2.537788, -7.32464], [9.870007, -2.645014, -7.341279], [9.978517, -2.752231, -7.357917], [10.087027, -2.645014, -7.341279], [9.978517, -2.537788, -7.32464], [9.978517, -2.661654, -7.234052], [9.978517, -2.752231, -7.357917], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_legEnd_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.258193, 7.453985, -5.66431], [-0.258193, 7.577851, -5.754897], [-0.258193, 7.487263, -5.878763], [-0.258193, 7.363397, -5.788176], [-0.258193, 7.453985, -5.66431], [-0.366693, 7.470624, -5.771536], [-0.258193, 7.487263, -5.878763], [-0.149683, 7.470624, -5.771536], [-0.258193, 7.577851, -5.754897], [-0.366693, 7.470624, -5.771536], [-0.258193, 7.363397, -5.788176], [-0.149683, 7.470624, -5.771536], [-0.258193, 7.453985, -5.66431], [-0.366693, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_legEnd_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.870007, 9.040367, -15.887175], [9.978517, 9.147593, -15.870535], [10.087027, 9.040367, -15.887175], [9.978517, 8.93314, -15.903814], [9.870007, 9.040367, -15.887175], [9.978517, 9.057005, -15.994391], [10.087027, 9.040367, -15.887175], [9.978517, 9.023727, -15.779948], [9.978517, 9.147593, -15.870535], [9.978517, 9.057005, -15.994391], [9.978517, 8.93314, -15.903814], [9.978517, 9.023727, -15.779948], [9.870007, 9.040367, -15.887175], [9.978517, 9.057005, -15.994391], [9.978517, 7.470624, -5.771536]]}]},
			"L_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[62.130602, 100.231898, -12.742499], [62.138655, 100.23819, -12.731051], [62.129668, 100.231097, -12.720832], [62.121616, 100.224806, -12.73228], [62.130602, 100.231898, -12.742499], [62.136838, 100.222966, -12.731692], [62.129668, 100.231097, -12.720832], [62.123431, 100.24003, -12.731639], [62.138655, 100.23819, -12.731051], [62.136838, 100.222966, -12.731692], [62.121616, 100.224806, -12.73228], [62.123431, 100.24003, -12.731639], [62.130602, 100.231898, -12.742499], [62.136838, 100.222966, -12.731692], [61.497686, 101.036423, -12.729157]]}, {"shapeName": "L_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[62.301877, 101.668148, -12.682026], [62.294706, 101.676279, -12.671166], [62.300943, 101.667347, -12.660359], [62.308114, 101.659215, -12.671219], [62.301877, 101.668148, -12.682026], [62.309929, 101.674439, -12.670578], [62.300943, 101.667347, -12.660359], [62.292891, 101.661055, -12.671807], [62.294706, 101.676279, -12.671166], [62.309929, 101.674439, -12.670578], [62.308114, 101.659215, -12.671219], [62.292891, 101.661055, -12.671807], [62.301877, 101.668148, -12.682026], [62.309929, 101.674439, -12.670578], [61.497686, 101.036423, -12.729157]]}, {"shapeName": "L_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.462174, 101.005333, -11.706517], [61.446951, 101.007174, -11.707105], [61.445135, 100.991949, -11.707746], [61.460359, 100.990109, -11.707158], [61.462174, 101.005333, -11.706517], [61.453188, 100.998241, -11.696299], [61.445135, 100.991949, -11.707746], [61.454122, 100.999042, -11.717965], [61.446951, 101.007174, -11.707105], [61.453188, 100.998241, -11.696299], [61.460359, 100.990109, -11.707158], [61.454122, 100.999042, -11.717965], [61.462174, 101.005333, -11.706517], [61.453188, 100.998241, -11.696299], [61.497686, 101.036423, -12.729157]]}]},
			"C_neck_FK_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_B_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 157.006742, -11.974364], [0.0, 157.201533, -11.963579], [0.0, 157.385624, -12.028163], [0.0, 157.530992, -12.158273], [0.0, 157.615499, -12.334108], [0.0, 157.626284, -12.528898], [0.0, 157.5617, -12.712989], [0.0, 157.431591, -12.858357], [0.0, 157.255755, -12.942865], [0.0, 157.060965, -12.95365], [0.0, 156.876874, -12.889066], [0.0, 156.731506, -12.758956], [0.0, 156.646999, -12.583121], [0.0, 156.636214, -12.388331], [0.0, 156.700797, -12.20424], [0.0, 156.830907, -12.058872], [0.0, 157.006742, -11.974364], [0.0, 155.761679, -7.131863]]}]},
			"L_leg_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, -2.661654, -7.234052], [9.870007, -2.645014, -7.341279], [9.978517, -2.628375, -7.448506], [10.087027, -2.645014, -7.341279], [9.978517, -2.661654, -7.234052], [9.978517, -2.752231, -7.357917], [9.978517, -2.628375, -7.448506], [9.978517, -2.537788, -7.32464], [9.870007, -2.645014, -7.341279], [9.978517, -2.752231, -7.357917], [10.087027, -2.645014, -7.341279], [9.978517, -2.537788, -7.32464], [9.978517, -2.661654, -7.234052], [9.978517, -2.752231, -7.357917], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_leg_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.258193, 7.453985, -5.66431], [-0.258193, 7.577851, -5.754897], [-0.258193, 7.487263, -5.878763], [-0.258193, 7.363397, -5.788176], [-0.258193, 7.453985, -5.66431], [-0.366693, 7.470624, -5.771536], [-0.258193, 7.487263, -5.878763], [-0.149683, 7.470624, -5.771536], [-0.258193, 7.577851, -5.754897], [-0.366693, 7.470624, -5.771536], [-0.258193, 7.363397, -5.788176], [-0.149683, 7.470624, -5.771536], [-0.258193, 7.453985, -5.66431], [-0.366693, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}, {"shapeName": "L_leg_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.870007, 9.040367, -15.887175], [9.978517, 9.147593, -15.870535], [10.087027, 9.040367, -15.887175], [9.978517, 8.93314, -15.903814], [9.870007, 9.040367, -15.887175], [9.978517, 9.057005, -15.994391], [10.087027, 9.040367, -15.887175], [9.978517, 9.023727, -15.779948], [9.978517, 9.147593, -15.870535], [9.978517, 9.057005, -15.994391], [9.978517, 8.93314, -15.903814], [9.978517, 9.023727, -15.779948], [9.870007, 9.040367, -15.887175], [9.978517, 9.057005, -15.994391], [9.978517, 7.470624, -5.771536]]}]},
			"C_jaw_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_jaw_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.054255, 161.930574, 2.131058], [0.0, 161.979329, 2.154861], [-0.054255, 161.930574, 2.131058], [0.0, 161.881819, 2.107255], [0.054255, 161.930574, 2.131058], [0.0, 161.906773, 2.179808], [-0.054255, 161.930574, 2.131058], [0.0, 161.954377, 2.082303], [0.0, 161.979329, 2.154861], [0.0, 161.906773, 2.179808], [0.0, 161.881819, 2.107255], [0.0, 161.954377, 2.082303], [0.054255, 161.930574, 2.131058], [0.0, 161.906773, 2.179808], [0.0, 164.1761, -2.468417]]}, {"shapeName": "C_jaw_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.054255, 168.775575, -0.222891], [0.0, 168.799378, -0.271646], [-0.054255, 168.775575, -0.222891], [0.0, 168.751772, -0.174136], [0.054255, 168.775575, -0.222891], [0.0, 168.824326, -0.19909], [-0.054255, 168.775575, -0.222891], [0.0, 168.72682, -0.246693], [0.0, 168.799378, -0.271646], [0.0, 168.824326, -0.19909], [0.0, 168.751772, -0.174136], [0.0, 168.72682, -0.246693], [0.054255, 168.775575, -0.222891], [0.0, 168.824326, -0.19909], [0.0, 164.1761, -2.468417]]}, {"shapeName": "C_jaw_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-5.118355, 164.224855, -2.444614], [-5.118355, 164.199903, -2.517172], [-5.118355, 164.127345, -2.49222], [-5.118355, 164.152298, -2.419662], [-5.118355, 164.224855, -2.444614], [-5.172605, 164.1761, -2.468417], [-5.118355, 164.127345, -2.49222], [-5.0641, 164.1761, -2.468417], [-5.118355, 164.199903, -2.517172], [-5.172605, 164.1761, -2.468417], [-5.118355, 164.152298, -2.419662], [-5.0641, 164.1761, -2.468417], [-5.118355, 164.224855, -2.444614], [-5.172605, 164.1761, -2.468417], [0.0, 164.1761, -2.468417]]}]},
			"C_head_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 164.1761, -5.022672], [5.118355, 164.230355, -4.968417], [5.118355, 164.1761, -4.914162], [5.118355, 164.121845, -4.968417], [5.118355, 164.1761, -5.022672], [5.172605, 164.1761, -4.968417], [5.118355, 164.1761, -4.914162], [5.0641, 164.1761, -4.968417], [5.118355, 164.230355, -4.968417], [5.172605, 164.1761, -4.968417], [5.118355, 164.121845, -4.968417], [5.0641, 164.1761, -4.968417], [5.118355, 164.1761, -5.022672], [5.172605, 164.1761, -4.968417], [0.0, 164.1761, -4.968417]]}, {"shapeName": "C_head_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 169.294455, -5.022672], [-0.054255, 169.294455, -4.968417], [0.0, 169.294455, -4.914162], [0.054255, 169.294455, -4.968417], [0.0, 169.294455, -5.022672], [0.0, 169.348705, -4.968417], [0.0, 169.294455, -4.914162], [0.0, 169.2402, -4.968417], [-0.054255, 169.294455, -4.968417], [0.0, 169.348705, -4.968417], [0.054255, 169.294455, -4.968417], [0.0, 169.2402, -4.968417], [0.0, 169.294455, -5.022672], [0.0, 169.348705, -4.968417], [0.0, 164.1761, -4.968417]]}, {"shapeName": "C_head_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 164.230355, 0.149938], [-0.054255, 164.1761, 0.149938], [0.0, 164.121845, 0.149938], [0.054255, 164.1761, 0.149938], [0.0, 164.230355, 0.149938], [0.0, 164.1761, 0.204188], [0.0, 164.121845, 0.149938], [0.0, 164.1761, 0.095683], [-0.054255, 164.1761, 0.149938], [0.0, 164.1761, 0.204188], [0.054255, 164.1761, 0.149938], [0.0, 164.1761, 0.095683], [0.0, 164.230355, 0.149938], [0.0, 164.1761, 0.204188], [0.0, 164.1761, -4.968417]]}]},
			"C_cog_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[23.983056, 98.683497, -6.90803], [23.95776, 98.683497, -10.681046], [17.447304, 98.683497, -12.946502], [16.5576, 98.683497, -15.623846], [20.41716, 98.683497, -21.33455], [18.178992, 98.683497, -24.37211], [11.579328, 98.683497, -22.382174], [9.286488, 98.683497, -24.025334], [9.052632, 98.683497, -30.909854], [5.456448, 98.683497, -32.05175], [1.28844, 98.683497, -26.566478], [-1.531752, 98.683497, -26.54783], [-5.76972, 98.683497, -31.976534], [-9.350256, 98.683497, -30.786566], [-9.494592, 98.683497, -23.901182], [-11.76492, 98.683497, -22.227854], [-18.388224, 98.683497, -24.127142], [-20.585496, 98.683497, -21.059846], [-16.651008, 98.683497, -15.404318], [-17.50428, 98.683497, -12.715478], [-23.983056, 98.683497, -10.359902], [-23.95776, 98.683497, -6.586886], [-17.447304, 98.683497, -4.32143], [-16.5576, 98.683497, -1.644086], [-20.41716, 98.683497, 4.066618], [-18.178992, 98.683497, 7.104178], [-11.579328, 98.683497, 5.114242], [-9.286488, 98.683497, 6.757402], [-9.052632, 98.683497, 13.641922], [-5.456448, 98.683497, 14.783818], [-1.28844, 98.683497, 9.298546], [1.531752, 98.683497, 9.279898], [5.76972, 98.683497, 14.708602], [9.350256, 98.683497, 13.518634], [9.494592, 98.683497, 6.63325], [11.76492, 98.683497, 4.959922], [18.388224, 98.683497, 6.85921], [20.585496, 98.683497, 3.791914], [16.651008, 98.683497, -1.863614], [17.50428, 98.683497, -4.552454], [23.983056, 98.683497, -6.90803]]}]},
			"L_arm_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[64.085716, 97.324185, -8.354311], [64.131868, 97.402526, -8.271826], [64.053581, 97.359816, -8.187457], [64.007428, 97.281474, -8.269943], [64.085716, 97.324185, -8.354311], [64.128005, 97.282383, -8.246914], [64.053581, 97.359816, -8.187457], [64.011286, 97.401623, -8.294857], [64.131868, 97.402526, -8.271826], [64.128005, 97.282383, -8.246914], [64.007428, 97.281474, -8.269943], [64.011286, 97.401623, -8.294857], [64.085716, 97.324185, -8.354311], [64.128005, 97.282383, -8.246914], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_arm_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[64.449692, 108.658855, -10.70469], [64.375262, 108.736293, -10.645235], [64.417556, 108.694486, -10.537836], [64.491986, 108.617048, -10.59729], [64.449692, 108.658855, -10.70469], [64.495839, 108.737191, -10.622204], [64.417556, 108.694486, -10.537836], [64.371404, 108.616144, -10.620321], [64.375262, 108.736293, -10.645235], [64.495839, 108.737191, -10.622204], [64.491986, 108.617048, -10.59729], [64.371404, 108.616144, -10.620321], [64.449692, 108.658855, -10.70469], [64.495839, 108.737191, -10.622204], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_arm_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[57.110257, 104.707937, -2.662955], [56.989674, 104.707033, -2.685985], [56.985816, 104.586885, -2.661071], [57.106398, 104.587788, -2.63804], [57.110257, 104.707937, -2.662955], [57.03197, 104.665225, -2.578594], [56.985816, 104.586885, -2.661071], [57.064104, 104.629595, -2.74544], [56.989674, 104.707033, -2.685985], [57.03197, 104.665225, -2.578594], [57.106398, 104.587788, -2.63804], [57.064104, 104.629595, -2.74544], [57.110257, 104.707937, -2.662955], [57.03197, 104.665225, -2.578594], [58.56385, 102.966713, -10.53242]]}]},
			"C_torso_FK_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-0.0, 111.301852, -8.688221], [-0.054255, 111.301852, -8.633966], [-0.0, 111.301852, -8.579711], [0.054255, 111.301852, -8.633966], [-0.0, 111.301852, -8.688221], [-0.0, 111.356102, -8.633966], [-0.0, 111.301852, -8.579711], [-0.0, 111.247597, -8.633966], [-0.054255, 111.301852, -8.633966], [-0.0, 111.356102, -8.633966], [0.054255, 111.301852, -8.633966], [-0.0, 111.247597, -8.633966], [-0.0, 111.301852, -8.688221], [-0.0, 111.356102, -8.633966], [-0.0, 106.183497, -8.633966]]}, {"shapeName": "C_torso_FK_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 106.183497, -8.688221], [-5.118355, 106.129242, -8.633966], [-5.118355, 106.183497, -8.579711], [-5.118355, 106.237752, -8.633966], [-5.118355, 106.183497, -8.688221], [-5.172605, 106.183497, -8.633966], [-5.118355, 106.183497, -8.579711], [-5.0641, 106.183497, -8.633966], [-5.118355, 106.129242, -8.633966], [-5.172605, 106.183497, -8.633966], [-5.118355, 106.237752, -8.633966], [-5.0641, 106.183497, -8.633966], [-5.118355, 106.183497, -8.688221], [-5.172605, 106.183497, -8.633966], [-0.0, 106.183497, -8.633966]]}, {"shapeName": "C_torso_FK_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 106.183497, -3.515611], [-0.0, 106.129242, -3.515611], [0.054255, 106.183497, -3.515611], [-0.0, 106.237752, -3.515611], [-0.054255, 106.183497, -3.515611], [-0.0, 106.183497, -3.461361], [0.054255, 106.183497, -3.515611], [-0.0, 106.183497, -3.569866], [-0.0, 106.129242, -3.515611], [-0.0, 106.183497, -3.461361], [-0.0, 106.237752, -3.515611], [-0.0, 106.183497, -3.569866], [-0.054255, 106.183497, -3.515611], [-0.0, 106.183497, -3.461361], [-0.0, 106.183497, -8.633966]]}]},
			"C_neck_FK_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 164.939528, -4.82815], [-0.054255, 164.926017, -4.775604], [0.0, 164.912507, -4.723059], [0.054255, 164.926017, -4.775604], [0.0, 164.939528, -4.82815], [0.0, 164.978558, -4.762096], [0.0, 164.912507, -4.723059], [0.0, 164.873471, -4.789115], [-0.054255, 164.926017, -4.775604], [0.0, 164.978558, -4.762096], [0.054255, 164.926017, -4.775604], [0.0, 164.873471, -4.789115], [0.0, 164.939528, -4.82815], [0.0, 164.978558, -4.762096], [0.0, 159.968889, -6.05014]]}, {"shapeName": "C_neck_FK_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.118355, 159.9824, -6.102686], [-5.118355, 159.916343, -6.06365], [-5.118355, 159.955379, -5.997594], [-5.118355, 160.021435, -6.03663], [-5.118355, 159.9824, -6.102686], [-5.172605, 159.968889, -6.05014], [-5.118355, 159.955379, -5.997594], [-5.0641, 159.968889, -6.05014], [-5.118355, 159.916343, -6.06365], [-5.172605, 159.968889, -6.05014], [-5.118355, 160.021435, -6.03663], [-5.0641, 159.968889, -6.05014], [-5.118355, 159.9824, -6.102686], [-5.172605, 159.968889, -6.05014], [0.0, 159.968889, -6.05014]]}, {"shapeName": "C_neck_FK_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.054255, 158.694354, -1.093012], [0.0, 158.641808, -1.106522], [0.054255, 158.694354, -1.093012], [0.0, 158.7469, -1.079502], [-0.054255, 158.694354, -1.093012], [0.0, 158.680845, -1.040471], [0.054255, 158.694354, -1.093012], [0.0, 158.707864, -1.145558], [0.0, 158.641808, -1.106522], [0.0, 158.680845, -1.040471], [0.0, 158.7469, -1.079502], [0.0, 158.707864, -1.145558], [-0.054255, 158.694354, -1.093012], [0.0, 158.680845, -1.040471], [0.0, 159.968889, -6.05014]]}]},
			"C_midTorso_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[19.971748, 113.683497, -25.277089], [-0.0, 113.683497, -32.170882], [-19.971748, 113.683497, -25.277089], [-28.244299, 113.683497, -8.633966], [-19.971748, 113.683497, 8.009158], [-0.0, 113.683497, 14.90295], [19.971748, 113.683497, 8.009158], [28.244299, 113.683497, -8.633966]]}]},
			"C_midTorso_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[15.533582, 113.683497, -21.578617], [-0.0, 113.683497, -26.940456], [-15.533582, 113.683497, -21.578617], [-21.967788, 113.683497, -8.633966], [-15.533582, 113.683497, 4.310686], [-0.0, 113.683497, 9.672524], [15.533582, 113.683497, 4.310686], [21.967788, 113.683497, -8.633966]]}]},
			"C_hip_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[14.810267, 98.683497, -20.975855], [-0.0, 92.383497, -26.088021], [-14.810267, 98.683497, -20.975855], [-20.944867, 104.983497, -8.633966], [-14.810267, 98.683497, 3.707923], [-0.0, 92.383497, 8.82009], [14.810267, 98.683497, 3.707923], [20.944867, 104.983497, -8.633966]]}]},
			"L_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.673388, 91.963672, -6.651065], [67.681043, 91.968367, -6.638621], [67.668609, 91.965796, -6.630002], [67.660954, 91.961101, -6.642446], [67.673388, 91.963672, -6.651065], [67.674337, 91.954565, -6.63875], [67.668609, 91.965796, -6.630002], [67.667659, 91.974903, -6.642317], [67.681043, 91.968367, -6.638621], [67.674337, 91.954565, -6.63875], [67.660954, 91.961101, -6.642446], [67.667659, 91.974903, -6.642317], [67.673388, 91.963672, -6.651065], [67.674337, 91.954565, -6.63875], [67.35601, 92.924101, -6.808754]]}, {"shapeName": "L_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[68.305962, 93.265787, -6.63887], [68.300234, 93.277019, -6.630122], [68.301184, 93.267912, -6.617808], [68.306912, 93.25668, -6.626556], [68.305962, 93.265787, -6.63887], [68.313616, 93.270482, -6.626427], [68.301184, 93.267912, -6.617808], [68.293529, 93.263216, -6.630251], [68.300234, 93.277019, -6.630122], [68.313616, 93.270482, -6.626427], [68.306912, 93.25668, -6.626556], [68.293529, 93.263216, -6.630251], [68.305962, 93.265787, -6.63887], [68.313616, 93.270482, -6.626427], [67.35601, 92.924101, -6.808754]]}, {"shapeName": "L_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[67.140648, 93.027934, -5.813335], [67.127265, 93.03447, -5.817031], [67.120559, 93.020667, -5.81716], [67.133942, 93.014131, -5.813465], [67.140648, 93.027934, -5.813335], [67.128214, 93.025363, -5.804717], [67.120559, 93.020667, -5.81716], [67.132993, 93.023238, -5.825779], [67.127265, 93.03447, -5.817031], [67.128214, 93.025363, -5.804717], [67.133942, 93.014131, -5.813465], [67.132993, 93.023238, -5.825779], [67.140648, 93.027934, -5.813335], [67.128214, 93.025363, -5.804717], [67.35601, 92.924101, -6.808754]]}]},
			"L_arm_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[65.039501, 115.313549, -11.921855], [64.854471, 114.786222, -11.844882], [64.283186, 114.854206, -11.969428], [63.997841, 114.527647, -11.954649], [64.147998, 113.977595, -11.808267], [63.647632, 113.720381, -11.849709], [63.307961, 114.172959, -12.011775], [62.882106, 114.13402, -12.085478], [62.593254, 113.62384, -12.032162], [62.070651, 113.787421, -12.167746], [62.161566, 114.359559, -12.272414], [61.844669, 114.630988, -12.39141], [61.286005, 114.459601, -12.462408], [61.047314, 114.94815, -12.612707], [61.515559, 115.304634, -12.59865], [61.49318, 115.727515, -12.693265], [60.991978, 115.995233, -12.846966], [61.177008, 116.52256, -12.923938], [61.748311, 116.454626, -12.7994], [62.033656, 116.781185, -12.814179], [61.883498, 117.331237, -12.960561], [62.383853, 117.588418, -12.919114], [62.723585, 117.135857, -12.75704], [63.14939, 117.174812, -12.68335], [63.438225, 117.684942, -12.736658], [63.960828, 117.521361, -12.601074], [63.86993, 116.949273, -12.496413], [64.186876, 116.677828, -12.377405], [64.74548, 116.849197, -12.306415], [64.984183, 116.360682, -12.156121], [64.515937, 116.004198, -12.170177], [64.538316, 115.581317, -12.075562], [65.039501, 115.313549, -11.921855]]}, {"shapeName": "L_arm_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[63.783835, 116.049225, -12.320793], [63.299777, 116.463885, -12.50257], [62.649329, 116.40434, -12.615129], [62.213568, 115.90549, -12.592527], [62.247662, 115.259607, -12.448035], [62.731719, 114.844947, -12.266258], [63.382168, 114.904492, -12.153699], [63.817917, 115.403308, -12.176296]]}, {"shapeName": "L_arm_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[62.331953, 113.70563, -12.099954], [58.56385, 102.966713, -10.53242]]}]},
			"L_leg_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[14.680189, 7.470624, -13.607656], [9.978517, 7.470624, -16.853476], [5.276845, 7.470624, -13.607656], [3.329353, 7.470624, -5.771536], [5.276845, 7.470624, 2.064584], [9.978517, 7.470624, 5.310404], [14.680189, 7.470624, 2.064584], [16.627681, 7.470624, -5.771536]]}]},
			"L_upArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_upArm_FK_CTLShape", "degree": 3, "form": 2, "points": [[16.842168, 143.691301, -13.171416], [18.96751, 146.050941, -14.365333], [21.450448, 147.939015, -13.030936], [22.836509, 148.249511, -9.949889], [22.313762, 146.800551, -6.927032], [20.18842, 144.440911, -5.733115], [17.705482, 142.552837, -7.067512], [16.319421, 142.24234, -10.148558]]}]},
			"L_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_A_CTLShape", "degree": 3, "form": 2, "points": [[57.918903, 101.283853, -8.147082], [57.932063, 101.386038, -8.072438], [57.851915, 101.46453, -8.012424], [57.725407, 101.47335, -8.002195], [57.626648, 101.407331, -8.047743], [57.613488, 101.305147, -8.122386], [57.693636, 101.226654, -8.1824], [57.820144, 101.217834, -8.192629]]}]},
			"L_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[61.258, 100.758328, -7.976656], [61.259619, 100.768029, -7.964876], [61.246688, 100.762611, -7.958637], [61.245069, 100.752911, -7.970417], [61.258, 100.758328, -7.976656], [61.258073, 100.752986, -7.962272], [61.246688, 100.762611, -7.958637], [61.246615, 100.767954, -7.973022], [61.259619, 100.768029, -7.964876], [61.258073, 100.752986, -7.962272], [61.245069, 100.752911, -7.970417], [61.246615, 100.767954, -7.973022], [61.258, 100.758328, -7.976656], [61.258073, 100.752986, -7.962272], [60.711838, 101.466573, -8.47477]]}, {"shapeName": "L_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[61.403839, 102.177534, -8.222404], [61.392454, 102.18716, -8.21877], [61.392528, 102.181816, -8.204385], [61.403913, 102.17219, -8.208019], [61.403839, 102.177534, -8.222404], [61.405458, 102.187233, -8.210624], [61.392528, 102.181816, -8.204385], [61.390908, 102.172116, -8.216165], [61.392454, 102.18716, -8.21877], [61.405458, 102.187233, -8.210624], [61.403913, 102.17219, -8.208019], [61.390908, 102.172116, -8.216165], [61.403839, 102.177534, -8.222404], [61.405458, 102.187233, -8.210624], [60.711838, 101.466573, -8.47477]]}, {"shapeName": "L_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[60.185555, 101.676137, -7.622051], [60.17255, 101.676062, -7.630197], [60.171004, 101.661019, -7.627592], [60.184009, 101.661093, -7.619446], [60.185555, 101.676137, -7.622051], [60.172624, 101.670719, -7.615813], [60.171004, 101.661019, -7.627592], [60.183935, 101.666436, -7.633831], [60.17255, 101.676062, -7.630197], [60.172624, 101.670719, -7.615813], [60.184009, 101.661093, -7.619446], [60.183935, 101.666436, -7.633831], [60.185555, 101.676137, -7.622051], [60.172624, 101.670719, -7.615813], [60.711838, 101.466573, -8.47477]]}]},
			"C_hip_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[16.926019, 98.683497, -22.738982], [-0.0, 91.483497, -28.581458], [-16.926019, 98.683497, -22.738982], [-23.93699, 105.883497, -8.633966], [-16.926019, 98.683497, 5.47105], [-0.0, 91.483497, 11.313526], [16.926019, 98.683497, 5.47105], [23.93699, 105.883497, -8.633966]]}]},
			"C_hip_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_CTLShape", "degree": 3, "form": 2, "points": [[21.157524, 98.683497, -26.265236], [-0.0, 89.683497, -33.568331], [-21.157524, 98.683497, -26.265236], [-29.921238, 107.683497, -8.633966], [-21.157524, 98.683497, 8.997304], [-0.0, 89.683497, 16.300399], [21.157524, 98.683497, 8.997304], [29.921238, 107.683497, -8.633966]]}]},
			"world_CTL": {"color": 1, "shapes": [{"shapeName": "world_CTLShape", "degree": 1, "form": 0, "points": [[-0.023956, 0.0, 114.566308], [-50.910723, 0.0, 63.608664], [-38.169014, 0.0, 63.611321], [-38.163689, 0.0, 38.137819], [-63.637191, 0.0, 38.132494], [-63.639859, 0.0, 50.874203], [-114.566308, 0.0, -0.023956], [-63.608664, 0.0, -50.910723], [-63.611321, 0.0, -38.169014], [-38.137819, 0.0, -38.163689], [-38.132494, 0.0, -63.637191], [-50.874203, 0.0, -63.639859], [0.023956, 0.0, -114.566308], [50.910723, 0.0, -63.608664], [38.169014, 0.0, -63.611321], [38.163689, 0.0, -38.137819], [63.637191, 0.0, -38.132494], [63.639859, 0.0, -50.874203], [114.566308, 0.0, 0.023956], [63.608664, 0.0, 50.910723], [63.611321, 0.0, 38.169014], [38.137819, 0.0, 38.163689], [38.132494, 0.0, 63.637191], [50.874203, 0.0, 63.639859], [-0.023956, 0.0, 114.566308], [-9.997125, 0.13882, 104.767478], [-9.124343, 0.0, 103.835588], [-9.12355, 0.0, 100.027949], [-8.330291, 0.0, 100.028117], [-8.380673, 0.0, 103.865493], [-7.815417, 0.0, 103.578046], [-7.834902, 0.0, 101.912204], [-7.031728, 0.0, 101.912373], [-7.032075, 0.0, 103.578215], [-6.536348, 0.0, 103.86587], [-6.535535, 0.0, 99.96899], [-5.732361, 0.0, 99.969158], [-5.733194, 0.0, 103.965196], [-6.377855, 0.0, 104.609589], [-7.369319, 0.0, 104.113595], [-8.460158, 0.0, 104.609153], [-9.124353, 0.0, 103.855419], [-8.460158, 0.0, 104.609153], [-7.379234, 0.0, 104.123511], [-6.377845, 0.0, 104.599674], [-4.444288, 0.0, 104.609996], [-5.098587, 0.0, 103.965335], [-5.097893, 0.0, 100.623735], [-4.443317, 0.0, 99.969436], [-2.351098, 0.0, 99.969872], [-1.706715, 0.0, 100.624439], [-1.707409, 0.0, 103.966039], [-2.35207, 0.0, 104.610432], [-4.444288, 0.0, 104.609996], [-4.196236, 0.0, 103.866366], [-4.294749, 0.0, 100.792471], [-2.500013, 0.0, 100.812679], [-2.510563, 0.0, 103.866713], [-4.206152, 0.0, 103.886198], [-4.444288, 0.0, 104.609996], [-2.35207, 0.0, 104.610432], [-1.013447, 0.0, 104.61071], [-1.062054, 0.0, 99.97014], [1.198732, 0.0, 99.970606], [1.853031, 0.0, 100.625183], [1.852744, 0.0, 102.0233], [1.188251, 0.0, 102.667684], [1.148578, 0.0, 102.717252], [2.447152, 0.0, 104.591602], [2.447142, 0.0, 104.611434], [1.515064, 0.0, 104.611235], [0.2165, 0.0, 102.72698], [-0.269371, 0.0, 102.72688], [-0.268954, 0.0, 100.743735], [0.980427, 0.0, 100.743993], [0.990095, 0.0, 101.923964], [-0.269202, 0.0, 101.923707], [-0.269767, 0.0, 104.610869], [-1.013447, 0.0, 104.61071], [6.353938, 0.0, 104.612247], [6.354097, 0.0, 103.868567], [3.756176, 0.0, 103.858106], [3.75699, 0.0, 99.971141], [2.953816, 0.0, 99.970983], [2.952844, 0.0, 104.611533], [9.735201, 0.0, 104.612951], [10.330284, 0.0, 103.968558], [10.380556, 0.0, 100.626968], [9.736173, 0.0, 99.972401], [6.989517, 0.0, 99.971826], [6.988545, 0.0, 104.612386], [7.801793, 0.0, 103.868875], [7.782616, 0.0, 100.725579], [9.478205, 0.0, 100.725936], [9.457719, 0.0, 103.84939], [7.772046, 0.0, 103.888696], [6.968713, 0.0, 104.612376]]}]},
			"C_lookAt_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lookAt_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-3.486483, 169.143714, 71.147365], [-3.486483, 168.70655, 71.147365], [-3.486483, 168.70655, 70.710201], [-3.486483, 169.143714, 70.710201], [-3.486483, 169.143714, 71.147365], [3.486483, 169.143714, 71.147365], [3.486483, 168.70655, 71.147365], [3.486483, 168.70655, 70.710201], [3.486483, 169.143714, 70.710201], [3.486483, 169.143714, 71.147365], [3.486483, 168.70655, 71.147365], [-3.486483, 168.70655, 71.147365], [-3.486483, 168.70655, 70.710201], [3.486483, 168.70655, 70.710201], [3.486483, 169.143714, 70.710201], [-3.486483, 169.143714, 70.710201], [-3.486483, 169.143714, 71.147365], [-0.217, 169.142132, 71.145783], [-0.218582, 165.438649, 71.147365], [-0.218582, 165.438649, 70.710201], [0.218582, 165.438649, 70.710201], [0.218582, 165.438649, 71.147365], [-0.218582, 165.438649, 71.147365], [-0.218582, 172.411615, 71.147365], [0.218582, 172.411615, 71.147365], [0.218582, 172.411615, 70.710201], [-0.218582, 172.411615, 70.710201], [-0.218582, 172.411615, 71.147365], [-0.218582, 172.411615, 70.710201], [-0.218582, 165.438649, 70.710201], [0.218582, 165.438649, 70.710201], [0.218582, 172.411615, 70.710201], [0.218582, 172.411615, 71.147365], [0.218582, 165.438649, 71.147365], [0.217, 168.708132, 71.145783], [0.218582, 168.70655, 74.415266], [-0.218582, 168.70655, 74.415266], [-0.218582, 169.143714, 74.415266], [0.218582, 169.143714, 74.415266], [0.218582, 168.70655, 74.415266], [0.218582, 168.70655, 67.4423], [0.218582, 169.143714, 67.4423], [-0.218582, 169.143714, 67.4423], [-0.218582, 168.70655, 67.4423], [0.218582, 168.70655, 67.4423], [-0.218582, 168.70655, 67.4423], [-0.218582, 168.70655, 74.415266], [-0.218582, 169.143714, 74.415266], [-0.218582, 169.143714, 67.4423], [0.218582, 169.143714, 67.4423], [0.218582, 169.143714, 74.415266]]}]},
			"L_legBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_legBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 80.930699, -3.548774], [9.870007, 80.913205, -3.655864], [9.978517, 80.89571, -3.762955], [10.087027, 80.913205, -3.655864], [9.978517, 80.930699, -3.548774], [9.978517, 80.806124, -3.638372], [9.978517, 80.89571, -3.762955], [9.978517, 81.020295, -3.673359], [9.870007, 80.913205, -3.655864], [9.978517, 80.806124, -3.638372], [10.087027, 80.913205, -3.655864], [9.978517, 81.020295, -3.673359], [9.978517, 80.930699, -3.548774], [9.978517, 80.806124, -3.638372], [9.978517, 91.015999, -5.306253]]}, {"shapeName": "L_legBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.258193, 91.033493, -5.199162], [-0.258193, 91.123089, -5.323747], [-0.258193, 90.998505, -5.413343], [-0.258193, 90.908908, -5.288759], [-0.258193, 91.033493, -5.199162], [-0.366693, 91.015999, -5.306253], [-0.258193, 90.998505, -5.413343], [-0.149683, 91.015999, -5.306253], [-0.258193, 91.123089, -5.323747], [-0.366693, 91.015999, -5.306253], [-0.258193, 90.908908, -5.288759], [-0.149683, 91.015999, -5.306253], [-0.258193, 91.033493, -5.199162], [-0.366693, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}, {"shapeName": "L_legBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.870007, 89.36561, -15.409047], [9.978517, 89.472701, -15.426541], [10.087027, 89.36561, -15.409047], [9.978517, 89.25852, -15.391553], [9.870007, 89.36561, -15.409047], [9.978517, 89.348118, -15.516128], [10.087027, 89.36561, -15.409047], [9.978517, 89.383104, -15.301957], [9.978517, 89.472701, -15.426541], [9.978517, 89.348118, -15.516128], [9.978517, 89.25852, -15.391553], [9.978517, 89.383104, -15.301957], [9.870007, 89.36561, -15.409047], [9.978517, 89.348118, -15.516128], [9.978517, 91.015999, -5.306253]]}]},
			"C_head_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[10.395022, 181.321907, -4.968417], [0.0, 185.369997, -4.968417], [-10.395022, 181.321907, -4.968417], [-14.700772, 171.548932, -4.968417], [-10.395022, 161.775957, -4.968417], [0.0, 157.727868, -4.968417], [10.395022, 161.775957, -4.968417], [14.700772, 171.548932, -4.968417]]}]},
			"L_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.273671, 1.0, -0.010851], [1.273671, 1.010851, 0.0], [1.273671, 1.0, 0.010851], [1.273671, 0.989149, 0.0], [1.273671, 1.0, -0.010851], [1.284521, 1.0, 0.0], [1.273671, 1.0, 0.010851], [1.26282, 1.0, 0.0], [1.273671, 1.010851, 0.0], [1.284521, 1.0, 0.0], [1.273671, 0.989149, 0.0], [1.26282, 1.0, 0.0], [1.273671, 1.0, -0.010851], [1.284521, 1.0, 0.0], [0.25, 1.0, 0.0]]}, {"shapeName": "L_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.25, 2.023671, -0.010851], [0.239149, 2.023671, 0.0], [0.25, 2.023671, 0.010851], [0.260851, 2.023671, 0.0], [0.25, 2.023671, -0.010851], [0.25, 2.034521, 0.0], [0.25, 2.023671, 0.010851], [0.25, 2.01282, 0.0], [0.239149, 2.023671, 0.0], [0.25, 2.034521, 0.0], [0.260851, 2.023671, 0.0], [0.25, 2.01282, 0.0], [0.25, 2.023671, -0.010851], [0.25, 2.034521, 0.0], [0.25, 1.0, 0.0]]}, {"shapeName": "L_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.25, 1.010851, 1.023671], [0.239149, 1.0, 1.023671], [0.25, 0.989149, 1.023671], [0.260851, 1.0, 1.023671], [0.25, 1.010851, 1.023671], [0.25, 1.0, 1.034521], [0.25, 0.989149, 1.023671], [0.25, 1.0, 1.01282], [0.239149, 1.0, 1.023671], [0.25, 1.0, 1.034521], [0.260851, 1.0, 1.023671], [0.25, 1.0, 1.01282], [0.25, 1.010851, 1.023671], [0.25, 1.0, 1.034521], [0.25, 1.0, 0.0]]}]},
			"L_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_C_CTLShape", "degree": 3, "form": 2, "points": [[65.96709, 94.662741, -13.873973], [66.069677, 94.717927, -13.925129], [66.186561, 94.746414, -13.88374], [66.249273, 94.731515, -13.774051], [66.221078, 94.681958, -13.660316], [66.118491, 94.626772, -13.60916], [66.001606, 94.598285, -13.650549], [65.938894, 94.613184, -13.760238]]}]},
			"L_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_B_CTLShape", "degree": 3, "form": 2, "points": [[64.103768, 96.909492, -5.403546], [64.216279, 96.968835, -5.406048], [64.27898, 97.046168, -5.326835], [64.255143, 97.096189, -5.212309], [64.158731, 97.089596, -5.129557], [64.04622, 97.030253, -5.127056], [63.983519, 96.95292, -5.206269], [64.007356, 96.902899, -5.320795]]}]},
			"L_leg_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[32.374752, 10.800695, -5.254777], [31.462865, 10.800695, -5.254777], [31.290169, 9.876043, -5.398264], [30.642181, 9.610737, -5.439434], [29.858363, 10.143897, -5.356698], [29.213554, 9.506715, -5.455576], [29.753067, 8.732251, -5.575757], [29.4847, 8.091842, -5.675136], [28.548895, 7.921189, -5.701618], [28.548895, 7.020059, -5.841455], [29.4847, 6.849406, -5.867937], [29.753067, 6.209082, -5.967302], [29.213554, 5.434533, -6.087496], [29.858363, 4.797351, -6.186374], [30.642181, 5.330511, -6.103639], [31.290169, 5.065205, -6.144809], [31.462865, 4.140553, -6.288296], [32.374752, 4.140553, -6.288296], [32.547533, 5.065205, -6.144809], [33.195521, 5.330511, -6.103639], [33.97934, 4.797351, -6.186374], [34.624091, 5.434533, -6.087496], [34.084636, 6.209082, -5.967302], [34.353003, 6.849406, -5.867937], [35.288722, 7.020059, -5.841455], [35.288722, 7.921189, -5.701618], [34.353003, 8.091842, -5.675136], [34.084636, 8.732251, -5.575757], [34.624091, 9.506715, -5.455576], [33.97934, 10.143897, -5.356698], [33.195521, 9.610737, -5.439434], [32.547533, 9.876043, -5.398264], [32.374752, 10.800695, -5.254777]]}, {"shapeName": "L_leg_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[32.908622, 8.448745, -5.619752], [33.318634, 7.470624, -5.771536], [32.908622, 6.492503, -5.923321], [31.918823, 6.087425, -5.986181], [30.929081, 6.492503, -5.923321], [30.519069, 7.470624, -5.771536], [30.929081, 8.448745, -5.619752], [31.918823, 8.853823, -5.556892]]}, {"shapeName": "L_leg_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[28.548895, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}]},
			"L_innerBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_innerBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[15.215227, 2.475595, 4.120068], [15.215227, 2.57902, 4.233435], [15.215227, 2.465653, 4.33686], [15.215227, 2.362228, 4.223492], [15.215227, 2.475595, 4.120068], [15.323727, 2.470624, 4.228464], [15.215227, 2.465653, 4.33686], [15.106717, 2.470624, 4.228464], [15.215227, 2.57902, 4.233435], [15.323727, 2.470624, 4.228464], [15.215227, 2.362228, 4.223492], [15.106717, 2.470624, 4.228464], [15.215227, 2.475595, 4.120068], [15.323727, 2.470624, 4.228464], [4.978517, 2.470624, 4.228464]]}, {"shapeName": "L_innerBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[4.978517, 12.701557, 4.589049], [4.870007, 12.696585, 4.697446], [4.978517, 12.691614, 4.805842], [5.087027, 12.696585, 4.697446], [4.978517, 12.701557, 4.589049], [4.978517, 12.804971, 4.702416], [4.978517, 12.691614, 4.805842], [4.978517, 12.588189, 4.692474], [4.870007, 12.696585, 4.697446], [4.978517, 12.804971, 4.702416], [5.087027, 12.696585, 4.697446], [4.978517, 12.588189, 4.692474], [4.978517, 12.701557, 4.589049], [4.978517, 12.804971, 4.702416], [4.978517, 2.470624, 4.228464]]}, {"shapeName": "L_innerBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.978517, 2.110038, 14.459396], [4.870007, 2.001642, 14.454425], [4.978517, 1.893246, 14.449454], [5.087027, 2.001642, 14.454425], [4.978517, 2.110038, 14.459396], [4.978517, 1.996671, 14.562811], [4.978517, 1.893246, 14.449454], [4.978517, 2.006613, 14.346029], [4.870007, 2.001642, 14.454425], [4.978517, 1.996671, 14.562811], [5.087027, 2.001642, 14.454425], [4.978517, 2.006613, 14.346029], [4.978517, 2.110038, 14.459396], [4.978517, 1.996671, 14.562811], [4.978517, 2.470624, 4.228464]]}]},
			"L_wrist_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_wrist_FK_CTLShape", "degree": 3, "form": 2, "points": [[58.036924, 96.086395, -14.504434], [62.108635, 99.228259, -16.602981], [65.393446, 103.242621, -14.615779], [65.967152, 105.77792, -9.706893], [63.493693, 105.34902, -4.751885], [59.421981, 102.207156, -2.653338], [56.137171, 98.192795, -4.64054], [55.563465, 95.657495, -9.549427]]}]},
			"L_wrist_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_wrist_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[64.085716, 97.324185, -8.354311], [64.131868, 97.402526, -8.271826], [64.053581, 97.359816, -8.187457], [64.007428, 97.281474, -8.269943], [64.085716, 97.324185, -8.354311], [64.128005, 97.282383, -8.246914], [64.053581, 97.359816, -8.187457], [64.011286, 97.401623, -8.294857], [64.131868, 97.402526, -8.271826], [64.128005, 97.282383, -8.246914], [64.007428, 97.281474, -8.269943], [64.011286, 97.401623, -8.294857], [64.085716, 97.324185, -8.354311], [64.128005, 97.282383, -8.246914], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_wrist_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[64.449692, 108.658855, -10.70469], [64.375262, 108.736293, -10.645235], [64.417556, 108.694486, -10.537836], [64.491986, 108.617048, -10.59729], [64.449692, 108.658855, -10.70469], [64.495839, 108.737191, -10.622204], [64.417556, 108.694486, -10.537836], [64.371404, 108.616144, -10.620321], [64.375262, 108.736293, -10.645235], [64.495839, 108.737191, -10.622204], [64.491986, 108.617048, -10.59729], [64.371404, 108.616144, -10.620321], [64.449692, 108.658855, -10.70469], [64.495839, 108.737191, -10.622204], [58.56385, 102.966713, -10.53242]]}, {"shapeName": "L_wrist_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[57.110257, 104.707937, -2.662955], [56.989674, 104.707033, -2.685985], [56.985816, 104.586885, -2.661071], [57.106398, 104.587788, -2.63804], [57.110257, 104.707937, -2.662955], [57.03197, 104.665225, -2.578594], [56.985816, 104.586885, -2.661071], [57.064104, 104.629595, -2.74544], [56.989674, 104.707033, -2.685985], [57.03197, 104.665225, -2.578594], [57.106398, 104.587788, -2.63804], [57.064104, 104.629595, -2.74544], [57.110257, 104.707937, -2.662955], [57.03197, 104.665225, -2.578594], [58.56385, 102.966713, -10.53242]]}]},
			"L_wrist_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_CTLShape", "degree": 3, "form": 2, "points": [[60.238381, 93.83739, -13.600173], [64.310093, 96.979254, -15.698721], [67.594904, 100.993616, -13.711519], [68.168609, 103.528915, -8.802632], [65.695151, 103.100015, -3.847625], [61.623439, 99.958151, -1.749078], [58.338629, 95.94379, -3.73628], [57.764923, 93.40849, -8.645166]]}]},
			"L_leg_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[34.863222, 11.170703, -5.197359], [33.850015, 11.170703, -5.197359], [33.658131, 10.143312, -5.356789], [32.938144, 9.848527, -5.402534], [32.067234, 10.440927, -5.310605], [31.35078, 9.732947, -5.42047], [31.950239, 8.872432, -5.554004], [31.652053, 8.160866, -5.664425], [30.61227, 7.971252, -5.693849], [30.61227, 6.969996, -5.849224], [31.652053, 6.780382, -5.878648], [31.950239, 6.06891, -5.989054], [31.35078, 5.208301, -6.122603], [32.067234, 4.500321, -6.232467], [32.938144, 5.092721, -6.140539], [33.658131, 4.797936, -6.186284], [33.850015, 3.770545, -6.345714], [34.863222, 3.770545, -6.345714], [35.055202, 4.797936, -6.186284], [35.775189, 5.092721, -6.140539], [36.646098, 4.500321, -6.232467], [37.362489, 5.208301, -6.122603], [36.763094, 6.06891, -5.989054], [37.061279, 6.780382, -5.878648], [38.100967, 6.969996, -5.849224], [38.100967, 7.971252, -5.693849], [37.061279, 8.160866, -5.664425], [36.763094, 8.872432, -5.554004], [37.362489, 9.732947, -5.42047], [36.646098, 10.440927, -5.310605], [35.775189, 9.848527, -5.402534], [35.055202, 10.143312, -5.356789], [34.863222, 11.170703, -5.197359]]}, {"shapeName": "L_leg_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[35.456411, 8.557425, -5.602887], [35.91198, 7.470624, -5.771536], [35.456411, 6.383823, -5.940186], [34.356635, 5.933736, -6.01003], [33.256922, 6.383823, -5.940186], [32.801352, 7.470624, -5.771536], [33.256922, 8.557425, -5.602887], [34.356635, 9.007512, -5.533042]]}, {"shapeName": "L_leg_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[30.61227, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}]},
			"C_midNeck_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[8.806001, 159.692623, -13.69818], [0.0, 160.44953, -16.642063], [-8.806001, 159.692623, -13.69818], [-12.453558, 157.865284, -6.591002], [-8.806001, 156.037945, 0.516177], [0.0, 155.281038, 3.46006], [8.806001, 156.037945, 0.516177], [12.453558, 157.865284, -6.591002]]}]},
			"L_leg_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978517, 40.982606, 101.153816], [9.870007, 40.983211, 101.045308], [9.978517, 40.983815, 100.936799], [10.087027, 40.983211, 101.045308], [9.978517, 40.982606, 101.153816], [9.978517, 40.874712, 101.044703], [9.978517, 40.983815, 100.936799], [9.978517, 41.091719, 101.045912], [9.870007, 40.983211, 101.045308], [9.978517, 40.874712, 101.044703], [10.087027, 40.983211, 101.045308], [9.978517, 41.091719, 101.045912], [9.978517, 40.982606, 101.153816], [9.978517, 40.874712, 101.044703], [9.978517, 51.219762, 101.102317]]}, {"shapeName": "L_leg_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.258193, 51.219158, 101.210826], [-0.258193, 51.32827, 101.102922], [-0.258193, 51.220366, 100.993809], [-0.258193, 51.111254, 101.101713], [-0.258193, 51.219158, 101.210826], [-0.366693, 51.219762, 101.102317], [-0.258193, 51.220366, 100.993809], [-0.149683, 51.219762, 101.102317], [-0.258193, 51.32827, 101.102922], [-0.366693, 51.219762, 101.102317], [-0.258193, 51.111254, 101.101713], [-0.149683, 51.219762, 101.102317], [-0.258193, 51.219158, 101.210826], [-0.366693, 51.219762, 101.102317], [9.978517, 51.219762, 101.102317]]}, {"shapeName": "L_leg_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.870007, 51.276772, 90.865766], [9.978517, 51.38528, 90.86637], [10.087027, 51.276772, 90.865766], [9.978517, 51.168263, 90.865162], [9.870007, 51.276772, 90.865766], [9.978517, 51.277376, 90.757268], [10.087027, 51.276772, 90.865766], [9.978517, 51.276167, 90.974274], [9.978517, 51.38528, 90.86637], [9.978517, 51.277376, 90.757268], [9.978517, 51.168263, 90.865162], [9.978517, 51.276167, 90.974274], [9.870007, 51.276772, 90.865766], [9.978517, 51.277376, 90.757268], [9.978517, 51.219762, 101.102317]]}]},
			"L_leg_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[29.886281, 10.430687, -5.312194], [29.075715, 10.430687, -5.312194], [28.922208, 9.608774, -5.439739], [28.346219, 9.372946, -5.476334], [27.649491, 9.846867, -5.402792], [27.076328, 9.280482, -5.490683], [27.555895, 8.59207, -5.597511], [27.317346, 8.022818, -5.685847], [26.48552, 7.871126, -5.709386], [26.48552, 7.070122, -5.833686], [27.317346, 6.91843, -5.857226], [27.555895, 6.349253, -5.94555], [27.076328, 5.660766, -6.05239], [27.649491, 5.094381, -6.140281], [28.346219, 5.568301, -6.066738], [28.922208, 5.332474, -6.103334], [29.075715, 4.510561, -6.230878], [29.886281, 4.510561, -6.230878], [30.039865, 5.332474, -6.103334], [30.615854, 5.568301, -6.066738], [31.312582, 5.094381, -6.140281], [31.885694, 5.660766, -6.05239], [31.406178, 6.349253, -5.94555], [31.644727, 6.91843, -5.857226], [32.476477, 7.070122, -5.833686], [32.476477, 7.871126, -5.709386], [31.644727, 8.022818, -5.685847], [31.406178, 8.59207, -5.597511], [31.885694, 9.280482, -5.490683], [31.312582, 9.846867, -5.402792], [30.615854, 9.372946, -5.476334], [30.039865, 9.608774, -5.439739], [29.886281, 10.430687, -5.312194]]}, {"shapeName": "L_leg_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[30.360832, 8.340064, -5.636617], [30.725288, 7.470624, -5.771536], [30.360832, 6.601183, -5.906456], [29.481011, 6.241114, -5.962331], [28.601241, 6.601183, -5.906456], [28.236785, 7.470624, -5.771536], [28.601241, 8.340064, -5.636617], [29.481011, 8.700134, -5.580741]]}, {"shapeName": "L_leg_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[26.48552, 7.470624, -5.771536], [9.978517, 7.470624, -5.771536]]}]},
			"L_toe_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[13.50477, 5.191847, 7.572465], [9.978516, 6.651657, 7.621077], [6.452262, 5.191847, 7.572465], [4.991643, 1.667547, 7.455104], [6.452262, -1.856754, 7.337743], [9.978516, -3.316563, 7.289131], [13.50477, -1.856754, 7.337743], [14.965389, 1.667547, 7.455104]]}]},
			"L_leg_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[14.09248, 7.470624, -12.628141], [9.978517, 7.470624, -15.468234], [5.864554, 7.470624, -12.628141], [4.160498, 7.470624, -5.771536], [5.864554, 7.470624, 1.085069], [9.978517, 7.470624, 3.925161], [14.09248, 7.470624, 1.085069], [15.796535, 7.470624, -5.771536]]}]},
			"L_wrist_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[56.653981, 99.724794, -13.945812], [59.504179, 101.924099, -15.414795], [61.803547, 104.734152, -14.023754], [62.205141, 106.508862, -10.587533], [60.47372, 106.208632, -7.119028], [57.623521, 104.009327, -5.650045], [55.324154, 101.199274, -7.041087], [54.92256, 99.424564, -10.477307]]}]},
			"L_legBase_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 87.422296, -4.719187], [9.978517, 81.60759, -3.769299], [9.978517, 79.386565, -3.406473], [9.978517, 83.840913, 9.901903], [9.978517, 91.035889, 17.401291], [9.978517, 98.223295, 16.22716], [9.978517, 102.65773, 6.827995], [9.978517, 102.645432, -7.206033], [9.978517, 100.424407, -6.843207], [9.978517, 94.609702, -5.893319], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}]},
			"L_shoulder_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [8.596775, 146.159638, -3.748312], [15.686573, 145.569717, -7.816377], [18.394641, 145.344387, -9.370243], [10.553984, 151.260608, -17.586673], [0.292067, 155.367696, -19.55699], [-8.471448, 156.096882, -14.528561], [-12.389128, 153.169636, -4.422114], [-9.964607, 147.704075, 6.902049], [-7.256539, 147.478745, 5.348183], [-0.16674, 146.888824, 1.280117], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097]]}]},
			"L_toe_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_CTLShape", "degree": 3, "form": 2, "points": [[13.896576, 5.500231, 10.08412], [9.978516, 7.122242, 10.138134], [6.060456, 5.500231, 10.08412], [4.437546, 1.584342, 9.953719], [6.060456, -2.331548, 9.823318], [9.978516, -3.953558, 9.769304], [13.896576, -2.331548, 9.823318], [15.519486, 1.584342, 9.953719]]}]},
			"C_midTorso_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[17.752665, 113.683497, -23.427853], [-0.0, 113.683497, -29.555669], [-17.752665, 113.683497, -23.427853], [-25.106044, 113.683497, -8.633966], [-17.752665, 113.683497, 6.159922], [-0.0, 113.683497, 12.287737], [17.752665, 113.683497, 6.159922], [25.106044, 113.683497, -8.633966]]}]},
			"L_loArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_loArm_FK_CTLShape", "degree": 3, "form": 2, "points": [[33.536431, 117.223909, -25.709041], [40.788532, 122.867793, -29.185946], [46.881976, 129.525257, -25.302211], [48.247297, 133.296444, -16.332857], [44.084724, 131.972258, -7.532017], [36.832623, 126.328374, -4.055112], [30.739179, 119.67091, -7.938847], [29.373858, 115.899723, -16.908201]]}]},
			"L_arm_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[61.842978, 109.536789, -4.163626], [52.005994, 99.967638, -4.014738], [54.546303, 97.151006, -17.204524], [64.383286, 106.720157, -17.353413], [65.121707, 105.965788, -17.050103], [55.284723, 96.396637, -16.901214], [52.744415, 99.213269, -3.711427], [62.581398, 108.78242, -3.860316], [61.842978, 109.536789, -4.163626], [64.383286, 106.720157, -17.353413], [54.546303, 97.151006, -17.204524], [55.284723, 96.396637, -16.901214], [65.121707, 105.965788, -17.050103], [62.581398, 108.78242, -3.860316], [52.744415, 99.213269, -3.711427], [52.005994, 99.967638, -4.014738]]}]},
			"L_upArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[25.002291, 139.425381, -11.991189], [25.078059, 139.468437, -11.904721], [25.026201, 139.393852, -11.822143], [24.950433, 139.350797, -11.908611], [25.002291, 139.425381, -11.991189], [25.071866, 139.347757, -11.926353], [25.026201, 139.393852, -11.822143], [24.956621, 139.471482, -11.886977], [25.078059, 139.468437, -11.904721], [25.071866, 139.347757, -11.926353], [24.950433, 139.350797, -11.908611], [24.956621, 139.471482, -11.886977], [25.002291, 139.425381, -11.991189], [25.071866, 139.347757, -11.926353], [19.577965, 145.245926, -10.049224]]}, {"shapeName": "L_upArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[25.586034, 150.810689, -9.950231], [25.540364, 150.85679, -9.846019], [25.609943, 150.77916, -9.781184], [25.655614, 150.733059, -9.885397], [25.586034, 150.810689, -9.950231], [25.661795, 150.853739, -9.863763], [25.609943, 150.77916, -9.781184], [25.534176, 150.736104, -9.867653], [25.540364, 150.85679, -9.846019], [25.661795, 150.853739, -9.863763], [25.655614, 150.733059, -9.885397], [25.534176, 150.736104, -9.867653], [25.586034, 150.810689, -9.950231], [25.661795, 150.853739, -9.863763], [19.577965, 145.245926, -10.049224]]}, {"shapeName": "L_upArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[20.769567, 143.817514, -2.073448], [20.648129, 143.820559, -2.055704], [20.641942, 143.699874, -2.077338], [20.76338, 143.696828, -2.095082], [20.769567, 143.817514, -2.073448], [20.717708, 143.74293, -1.990877], [20.641942, 143.699874, -2.077338], [20.6938, 143.774459, -2.159916], [20.648129, 143.820559, -2.055704], [20.717708, 143.74293, -1.990877], [20.76338, 143.696828, -2.095082], [20.6938, 143.774459, -2.159916], [20.769567, 143.817514, -2.073448], [20.717708, 143.74293, -1.990877], [19.577965, 145.245926, -10.049224]]}]},
			"L_legBase_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_CTLShape", "degree": 3, "form": 0, "points": [[9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.994442, 0.683252], [9.978517, 93.577589, 10.374428], [9.978517, 94.182299, 14.076136], [33.065881, 93.577589, 10.374428], [47.334671, 91.994442, 0.683252], [47.334671, 90.037556, -11.295758], [33.065881, 88.454409, -20.986934], [9.978517, 87.849699, -24.688642], [9.978517, 88.454409, -20.986934], [9.978517, 90.037556, -11.295758], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253], [9.978517, 91.015999, -5.306253]]}]},
			"L_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_C_CTLShape", "degree": 3, "form": 2, "points": [[67.273089, 92.873241, -6.943548], [67.392612, 92.907831, -6.970085], [67.490694, 92.951952, -6.902116], [67.50988, 92.979759, -6.779457], [67.43893, 92.974962, -6.67396], [67.319407, 92.940372, -6.647423], [67.221325, 92.896251, -6.715392], [67.202139, 92.868444, -6.838051]]}]},
			"L_shoulder_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [7.623051, 146.240659, -3.189597], [13.137339, 145.781831, -6.353648], [15.243614, 145.606574, -7.562211], [9.145325, 150.20808, -13.952768], [1.163834, 153.402482, -15.485236], [-5.652233, 153.969626, -11.574235], [-8.699318, 151.692879, -3.713666], [-6.813579, 147.441888, 5.094016], [-4.707304, 147.266631, 3.885454], [0.806984, 146.807803, 0.721403], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097], [4.215017, 146.524231, -1.234097]]}]},
			"L_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[58.6234, 94.465182, -1.633829], [58.610336, 94.467421, -1.626096], [58.60261, 94.459793, -1.636941], [58.615674, 94.457554, -1.644674], [58.6234, 94.465182, -1.633829], [58.614604, 94.453207, -1.629996], [58.60261, 94.459793, -1.636941], [58.611406, 94.471769, -1.640774], [58.610336, 94.467421, -1.626096], [58.614604, 94.453207, -1.629996], [58.615674, 94.457554, -1.644674], [58.611406, 94.471769, -1.640774], [58.6234, 94.465182, -1.633829], [58.614604, 94.453207, -1.629996], [58.462148, 95.338084, -2.14379]]}, {"shapeName": "L_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[58.220735, 95.8062, -1.265947], [58.208741, 95.812787, -1.272892], [58.199945, 95.800811, -1.269059], [58.211939, 95.794224, -1.262114], [58.220735, 95.8062, -1.265947], [58.207671, 95.808438, -1.258215], [58.199945, 95.800811, -1.269059], [58.213009, 95.798572, -1.276792], [58.208741, 95.812787, -1.272892], [58.207671, 95.808438, -1.258215], [58.211939, 95.794224, -1.262114], [58.213009, 95.798572, -1.276792], [58.220735, 95.8062, -1.265947], [58.207671, 95.808438, -1.258215], [58.462148, 95.338084, -2.14379]]}, {"shapeName": "L_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[57.478796, 95.08882, -2.281296], [57.479866, 95.093168, -2.295974], [57.484135, 95.078953, -2.299873], [57.483065, 95.074605, -2.285195], [57.478796, 95.08882, -2.281296], [57.471071, 95.081192, -2.29214], [57.484135, 95.078953, -2.299873], [57.491861, 95.086581, -2.289029], [57.479866, 95.093168, -2.295974], [57.471071, 95.081192, -2.29214], [57.483065, 95.074605, -2.285195], [57.491861, 95.086581, -2.289029], [57.478796, 95.08882, -2.281296], [57.471071, 95.081192, -2.29214], [58.462148, 95.338084, -2.14379]]}]},
			"L_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_D_CTLShape", "degree": 3, "form": 2, "points": [[66.743299, 90.804715, -2.481897], [66.869503, 90.804356, -2.465804], [66.947583, 90.819837, -2.366554], [66.9318, 90.842089, -2.242287], [66.8314, 90.858076, -2.165797], [66.705196, 90.858434, -2.18189], [66.627117, 90.842954, -2.281139], [66.642899, 90.820702, -2.405406]]}]},
			"L_toe_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toe_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.978516, 1.435298, 17.689754], [9.870006, 1.326849, 17.686143], [9.978516, 1.218399, 17.682531], [10.087026, 1.326849, 17.686143], [9.978516, 1.435298, 17.689754], [9.978516, 1.323237, 17.794583], [9.978516, 1.218399, 17.682531], [9.978516, 1.33046, 17.577693], [9.870006, 1.326849, 17.686143], [9.978516, 1.323237, 17.794583], [10.087026, 1.326849, 17.686143], [9.978516, 1.33046, 17.577693], [9.978516, 1.435298, 17.689754], [9.978516, 1.323237, 17.794583], [9.978516, 1.667547, 7.455104]]}, {"shapeName": "L_toe_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.258194, 1.775997, 7.458715], [-0.258194, 1.671158, 7.346654], [-0.258194, 1.559097, 7.451492], [-0.258194, 1.663935, 7.563554], [-0.258194, 1.775997, 7.458715], [-0.366694, 1.667547, 7.455104], [-0.258194, 1.559097, 7.451492], [-0.149684, 1.667547, 7.455104], [-0.258194, 1.671158, 7.346654], [-0.366694, 1.667547, 7.455104], [-0.258194, 1.663935, 7.563554], [-0.149684, 1.667547, 7.455104], [-0.258194, 1.775997, 7.458715], [-0.366694, 1.667547, 7.455104], [9.978516, 1.667547, 7.455104]]}, {"shapeName": "L_toe_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.870006, -8.563492, 7.114406], [9.978516, -8.559881, 7.005956], [10.087026, -8.563492, 7.114406], [9.978516, -8.567103, 7.222856], [9.870006, -8.563492, 7.114406], [9.978516, -8.671932, 7.110795], [10.087026, -8.563492, 7.114406], [9.978516, -8.455042, 7.118017], [9.978516, -8.559881, 7.005956], [9.978516, -8.671932, 7.110795], [9.978516, -8.567103, 7.222856], [9.978516, -8.455042, 7.118017], [9.870006, -8.563492, 7.114406], [9.978516, -8.671932, 7.110795], [9.978516, 1.667547, 7.455104]]}]},
			"C_jaw_CTL": {"color": 18, "shapes": [{"shapeName": "C_jaw_CTLShape", "degree": 3, "form": 0, "points": [[0.0, 164.1761, -2.468417], [0.0, 164.1761, -2.468417], [0.0, 164.1761, -2.468417], [-1.65014, 164.1761, -2.468417], [-4.32011, 164.1761, -2.468417], [-5.33995, 164.1761, -2.468417], [-4.32011, 160.733528, 4.582948], [-1.65014, 158.605899, 8.940936], [1.65014, 158.605899, 8.940936], [4.32011, 160.733528, 4.582948], [5.33995, 164.1761, -2.468417], [4.32011, 164.1761, -2.468417], [1.65014, 164.1761, -2.468417], [0.0, 164.1761, -2.468417], [0.0, 164.1761, -2.468417], [0.0, 164.1761, -2.468417]]}]},
			"C_neckBase_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[12.113793, 154.07533, -17.988598], [0.0, 150.125898, -23.321446], [-12.113793, 154.07533, -17.988598], [-17.13148, 156.552244, -6.9286], [-12.113793, 149.047848, 1.565087], [0.0, 143.01597, 4.331623], [12.113793, 149.047848, 1.565087], [17.13148, 156.552244, -6.9286]]}]},
			"C_reverseJaw_CTL": {"color": 18, "shapes": [{"shapeName": "C_reverseJaw_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 173.162337, 1.918786], [0.38268, 173.23074, 1.952181], [0.7071, 173.425544, 2.047287], [0.92388, 173.717075, 2.189617], [1.0, 174.060961, 2.357506], [0.92388, 174.404846, 2.525396], [0.7071, 174.696377, 2.667726], [0.38268, 174.891181, 2.762831], [0.0, 174.959584, 2.796227], [-0.38268, 174.891181, 2.762831], [-0.7071, 174.696377, 2.667726], [-0.92388, 174.404846, 2.525396], [-1.0, 174.060961, 2.357506], [-0.92388, 173.717075, 2.189617], [-0.7071, 173.425544, 2.047287], [-0.38268, 173.23074, 1.952181], [0.0, 173.162337, 1.918786], [0.0, 164.1761, -2.468417]]}]},
			"L_toe_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[13.112964, 4.800258, 7.559425], [9.978516, 6.097867, 7.602636], [6.844068, 4.800258, 7.559425], [5.54574, 1.667547, 7.455104], [6.844068, -1.465165, 7.350783], [9.978516, -2.762773, 7.307572], [13.112964, -1.465165, 7.350783], [14.411292, 1.667547, 7.455104]]}]},
		}

		controlShapes.set_data(data)