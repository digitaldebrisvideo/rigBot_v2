# -*- rigBot: assembly -*-
from rigBot import guide
from rigBot.data import controlShapes
import maya.cmds as mc

class LorezBiped():
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

			mc.xform("R_hand_guide", a=1, t=[-31.670807360691903, 52.527031637424834, 0.9997930675880048])
			mc.xform("R_hand_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_hand_guide", r=1, s=[3.0, 3.0, 3.0])

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

			mc.xform("L_hand_guide", a=1, t=[31.670816317784762, 52.526841577418914, 0.9997929821301804])
			mc.xform("L_hand_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_hand_guide", r=1, s=[3.0, 3.0, 3.0])

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

			mc.xform("C_torso_guide", a=1, t=[1.8967837686030552e-13, 51.81369170989436, -0.030520057793558486])
			mc.xform("C_torso_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_guide", r=1, s=[3.0, 3.0, 3.0])

		if mc.objExists("C_neck_guide"):
			if not mc.getAttr("C_neck_guide.rotateOrder", l=1):
				mc.setAttr("C_neck_guide.rotateOrder", 0)

			mc.xform("C_neck_guide", a=1, t=[7.994906741102653e-14, 76.61747744462573, -1.0524376148926267])
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

			mc.xform("C_chest_end_JNT_PLC", a=1, t=[3.251497560619512e-15, 0.30776546280834793, 0.08369041607996736])
			mc.xform("C_chest_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_chest_JNT_PLC"):
			if not mc.getAttr("C_chest_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_chest_JNT_PLC.rotateOrder", 0)

			mc.xform("C_chest_JNT_PLC", a=1, t=[-0.038563601832478867, 3.981222385248889e-14, -0.4241598673012852])
			mc.xform("C_chest_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_chest_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_shoulder_JNT_PLC"):
			if not mc.getAttr("L_shoulder_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_shoulder_JNT_PLC.rotateOrder", 0)

			mc.xform("L_shoulder_JNT_PLC", a=1, t=[-0.6501410883931217, 0.2085441611098453, 0.7535778709970726])
			mc.xform("L_shoulder_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_shoulder_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_JNT_PLC"):
			if not mc.getAttr("L_upArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_JNT_PLC", a=1, t=[-0.7360278345948457, 0.5296625570924363, -0.07616727017381535])
			mc.xform("L_upArm_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_JNT_PLC"):
			if not mc.getAttr("L_loArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_JNT_PLC", a=1, t=[-0.3158919516754546, -1.9655246955886714, 0.01146653515212226])
			mc.xform("L_loArm_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_JNT_PLC"):
			if not mc.getAttr("L_wrist_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_wrist_JNT_PLC.rotateOrder", 0)

			mc.xform("L_wrist_JNT_PLC", a=1, t=[-0.4647517831903203, -3.584092880289484, 0.19615104947569187])
			mc.xform("L_wrist_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_wrist_end_JNT_PLC"):
			if not mc.getAttr("L_wrist_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_wrist_end_JNT_PLC.rotateOrder", 0)

			mc.xform("L_wrist_end_JNT_PLC", a=1, t=[-0.5812608305091373, -3.9357813409212135, 0.32158887457870944])
			mc.xform("L_wrist_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_wrist_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_handle_driver_JNT_PLC"):
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_A_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_A_JNT_PLC", a=1, t=[1.747999341989033, 0.030625106556215087, -0.15864050910862787])
			mc.xform("L_upArm_twist_A_JNT_PLC", a=1, ro=[-11.773754719829386, 6.765392783563177, -45.87477313043311])
			mc.xform("L_upArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_A_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_A_JNT_PLC", a=1, t=[4.054336082021573, -2.289238332528834, -0.3515965619831639])
			mc.xform("L_loArm_twist_A_JNT_PLC", a=1, ro=[-12.141995839226434, -15.559584100389518, -41.165242514282966])
			mc.xform("L_loArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_B_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_B_JNT_PLC", a=1, t=[2.2320265185729116, -0.46841234398000786, -0.24111374804344038])
			mc.xform("L_upArm_twist_B_JNT_PLC", a=1, ro=[-11.773754719829386, 6.765392783563177, -45.87477313043311])
			mc.xform("L_upArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_B_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_B_JNT_PLC", a=1, t=[4.4245641157186, -2.612951969468998, -0.21465965911844992])
			mc.xform("L_loArm_twist_B_JNT_PLC", a=1, ro=[-12.141995839226434, -15.559584100389518, -41.165242514282966])
			mc.xform("L_loArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_C_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_C_JNT_PLC", a=1, t=[2.7160536951567895, -0.9674497945162273, -0.3235869869782529])
			mc.xform("L_upArm_twist_C_JNT_PLC", a=1, ro=[-11.773754719829386, 6.765392783563177, -45.87477313043311])
			mc.xform("L_upArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_C_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_C_JNT_PLC", a=1, t=[4.794792149415626, -2.9366656064091607, -0.07772275625373591])
			mc.xform("L_loArm_twist_C_JNT_PLC", a=1, ro=[-12.141995839226434, -15.559584100389518, -41.165242514282966])
			mc.xform("L_loArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_D_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_D_JNT_PLC", a=1, t=[3.2000808717406684, -1.4664872450524502, -0.40606022591306534])
			mc.xform("L_upArm_twist_D_JNT_PLC", a=1, ro=[-11.773754719829386, 6.765392783563177, -45.87477313043311])
			mc.xform("L_upArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_D_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_D_JNT_PLC", a=1, t=[5.165020183112653, -3.2603792433493215, 0.05921414661097798])
			mc.xform("L_loArm_twist_D_JNT_PLC", a=1, ro=[-12.141995839226434, -15.559584100389518, -41.165242514282966])
			mc.xform("L_loArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_JNT_PLC"):
			if not mc.getAttr("L_upLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_JNT_PLC", a=1, t=[-0.03162543459538214, 0.3665641687225456, 0.6193783936959723])
			mc.xform("L_upLeg_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_JNT_PLC"):
			if not mc.getAttr("L_loLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_JNT_PLC", a=1, t=[0.08422821668077352, -0.10967391454548103, -0.07018868832318052])
			mc.xform("L_loLeg_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_end_JNT_PLC"):
			if not mc.getAttr("L_leg_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_leg_end_JNT_PLC.rotateOrder", 0)

			mc.xform("L_leg_end_JNT_PLC", a=1, t=[0.19426437672963393, -0.32643845757551593, 0.010730258118343605])
			mc.xform("L_leg_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_handle_driver_JNT_PLC"):
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_A_JNT_PLC", a=1, t=[-0.008454704340150831, -0.5286834479310603, 0.5814649772921419])
			mc.xform("L_upLeg_twist_A_JNT_PLC", a=1, ro=[0.21409717527996522, 177.5758041266967, 91.48259398633458])
			mc.xform("L_upLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_A_JNT_PLC", a=1, t=[0.10623544869054591, -4.95302682315149, 0.34599510096512437])
			mc.xform("L_loLeg_twist_A_JNT_PLC", a=1, ro=[180.21495866599054, 5.673756043876992, -88.5052100837069])
			mc.xform("L_loLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_B_JNT_PLC", a=1, t=[0.014716025915080366, -1.423931064584667, 0.5435515608883112])
			mc.xform("L_upLeg_twist_B_JNT_PLC", a=1, ro=[0.21409717527996522, 177.5758041266967, 91.48259398633458])
			mc.xform("L_upLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_B_JNT_PLC", a=1, t=[0.12824268070031764, -5.796379731757497, 0.26217889025342916])
			mc.xform("L_loLeg_twist_B_JNT_PLC", a=1, ro=[180.21495866599054, 5.673756043876992, -88.5052100837069])
			mc.xform("L_loLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_C_JNT_PLC", a=1, t=[0.03788675617031134, -2.3191786812382738, 0.5056381444844806])
			mc.xform("L_upLeg_twist_C_JNT_PLC", a=1, ro=[0.21409717527996522, 177.5758041266967, 91.48259398633458])
			mc.xform("L_upLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_C_JNT_PLC", a=1, t=[0.1502499127100898, -6.639732640363505, 0.17836267954173401])
			mc.xform("L_loLeg_twist_C_JNT_PLC", a=1, ro=[180.21495866599054, 5.673756043876992, -88.5052100837069])
			mc.xform("L_loLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_D_JNT_PLC", a=1, t=[0.06105748642554265, -3.214426297891877, 0.46772472808065013])
			mc.xform("L_upLeg_twist_D_JNT_PLC", a=1, ro=[0.21409717527996522, 177.5758041266967, 91.48259398633458])
			mc.xform("L_upLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_D_JNT_PLC", a=1, t=[0.17225714471986175, -7.483085548969511, 0.09454646883003887])
			mc.xform("L_loLeg_twist_D_JNT_PLC", a=1, ro=[180.21495866599054, 5.673756043876992, -88.5052100837069])
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

			mc.xform("L_ankle_JNT_PLC", a=1, t=[0.05658770490023968, -0.19426437672963393, 0.09236513248656542])
			mc.xform("L_ankle_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ankle_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ball_JNT_PLC"):
			if not mc.getAttr("L_ball_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ball_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ball_JNT_PLC", a=1, t=[0.5243054881072211, -0.20420256150276073, -0.04357534819743053])
			mc.xform("L_ball_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ball_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_toe_JNT_PLC"):
			if not mc.getAttr("L_toe_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_toe_JNT_PLC.rotateOrder", 0)

			mc.xform("L_toe_JNT_PLC", a=1, t=[0.16538232075671533, -0.20495450012406535, -0.0031203689268703705])
			mc.xform("L_toe_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_toe_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

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

			mc.xform("C_head_end_JNT_PLC", a=1, t=[1.4349279490756012e-15, -1.2767221064666678, -2.0816681711721685e-17])
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

			mc.xform("C_head_JNT_PLC", a=1, t=[-0.658983639502015, -1.1971130983904568e-14, 0.17884441841870552])
			mc.xform("C_head_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_head_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_reverseJaw_JNT_PLC"):
			mc.xform("C_reverseJaw_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_B_JNT_PLC"):
			if not mc.getAttr("L_thumb_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_B_JNT_PLC", a=1, t=[0.48608889945844025, -0.049693667665783536, -4.325960716755617e-06])
			mc.xform("L_thumb_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_C_JNT_PLC"):
			if not mc.getAttr("L_thumb_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_C_JNT_PLC", a=1, t=[0.5763988486096827, -0.2127463687061244, 0.02534745374355296])
			mc.xform("L_thumb_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_D_JNT_PLC"):
			if not mc.getAttr("L_thumb_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_D_JNT_PLC", a=1, t=[0.7462862481121058, -0.24179587847284623, 0.02254138943284545])
			mc.xform("L_thumb_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_thumb_A_JNT_PLC"):
			if not mc.getAttr("L_thumb_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_thumb_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_thumb_A_JNT_PLC", a=1, t=[-0.8890586232546251, 0.4853583727205004, -0.3236478508655942])
			mc.xform("L_thumb_A_JNT_PLC", a=1, ro=[-31.43320054508624, -40.27726976485678, 33.82879971671178])
			mc.xform("L_thumb_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_B_JNT_PLC"):
			if not mc.getAttr("L_index_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_B_JNT_PLC", a=1, t=[0.7557481666231343, -0.049690717084061475, -1.504900939930387e-05])
			mc.xform("L_index_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_C_JNT_PLC"):
			if not mc.getAttr("L_index_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_C_JNT_PLC", a=1, t=[1.1702941947554801, -0.353331735831393, 0.03446645317872976])
			mc.xform("L_index_C_JNT_PLC", a=1, ro=[-2.0073814384624815, -2.933206938367625, -33.06812474892573])
			mc.xform("L_index_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_D_JNT_PLC"):
			if not mc.getAttr("L_index_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_D_JNT_PLC", a=1, t=[1.1555859259909649, -0.5579259963292174, 0.056496104012863535])
			mc.xform("L_index_D_JNT_PLC", a=1, ro=[-1.3575635030494129, -3.280830925789087, -45.073779986896525])
			mc.xform("L_index_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_E_JNT_PLC"):
			if not mc.getAttr("L_index_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_E_JNT_PLC", a=1, t=[1.0431888630651371, -0.7716711915200563, 0.07783902492952843])
			mc.xform("L_index_E_JNT_PLC", a=1, ro=[-1.3560495132504589, -3.2827345664694354, -45.077509909660975])
			mc.xform("L_index_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_index_A_JNT_PLC"):
			if not mc.getAttr("L_index_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_index_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_index_A_JNT_PLC", a=1, t=[-0.641782038753119, 0.695784409186821, -0.14339420271024256])
			mc.xform("L_index_A_JNT_PLC", a=1, ro=[4.966824508924263, -24.631324573818787, -30.801995271335986])
			mc.xform("L_index_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_B_JNT_PLC"):
			if not mc.getAttr("L_middle_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_B_JNT_PLC", a=1, t=[0.703558020944741, -0.04968197805496999, 2.9328550331886305e-05])
			mc.xform("L_middle_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_C_JNT_PLC"):
			if not mc.getAttr("L_middle_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_C_JNT_PLC", a=1, t=[1.163166196088909, -0.27699896280520875, -0.05905074270269228])
			mc.xform("L_middle_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_D_JNT_PLC"):
			if not mc.getAttr("L_middle_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_D_JNT_PLC", a=1, t=[1.1694475449621236, -0.5017762228979947, -0.07776694147469643])
			mc.xform("L_middle_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_E_JNT_PLC"):
			if not mc.getAttr("L_middle_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_E_JNT_PLC", a=1, t=[1.1213776477106174, -0.6960746998331864, -0.10712821226734626])
			mc.xform("L_middle_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_middle_A_JNT_PLC"):
			if not mc.getAttr("L_middle_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_middle_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_middle_A_JNT_PLC", a=1, t=[-0.612175824247803, 0.5966950906289483, -0.2820272334859496])
			mc.xform("L_middle_A_JNT_PLC", a=1, ro=[-9.48829350771246, 0.15938052337367833, -36.1742124027068])
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

			mc.xform("L_ring_C_JNT_PLC", a=1, t=[1.1854465053348382, -0.335589217054725, -0.025220939547803134])
			mc.xform("L_ring_C_JNT_PLC", a=1, ro=[1.4680680138951505, 2.3399923446798585, -38.327636223597246])
			mc.xform("L_ring_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_D_JNT_PLC"):
			if not mc.getAttr("L_ring_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_D_JNT_PLC", a=1, t=[1.1898515110057097, -0.6055311930233316, -0.04498447819749751])
			mc.xform("L_ring_D_JNT_PLC", a=1, ro=[0.9627975577308084, 2.5890618593950556, -50.037002959997345])
			mc.xform("L_ring_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_E_JNT_PLC"):
			if not mc.getAttr("L_ring_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_E_JNT_PLC", a=1, t=[1.0964524291767168, -0.8920827026891232, -0.0648328357472927])
			mc.xform("L_ring_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_ring_A_JNT_PLC"):
			if not mc.getAttr("L_ring_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_ring_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_ring_A_JNT_PLC", a=1, t=[-0.554125291828667, 0.6453169485846431, 0.1351529602075161])
			mc.xform("L_ring_A_JNT_PLC", a=1, ro=[-8.084198189509424, -11.39104583198509, -30.26927802657762])
			mc.xform("L_ring_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_B_JNT_PLC"):
			if not mc.getAttr("L_pinky_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_B_JNT_PLC", a=1, t=[0.6155558952424744, -0.05000000000001137, -1.7763568394002505e-14])
			mc.xform("L_pinky_B_JNT_PLC", a=1, ro=[18.27454166968388, 15.639863701634054, -10.707722758058836])
			mc.xform("L_pinky_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_C_JNT_PLC"):
			if not mc.getAttr("L_pinky_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_C_JNT_PLC", a=1, t=[0.8422198398308618, -0.19376957688386298, -0.1714237936503693])
			mc.xform("L_pinky_C_JNT_PLC", a=1, ro=[10.808565753239957, 21.952132058666205, -33.88328748286179])
			mc.xform("L_pinky_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_D_JNT_PLC"):
			if not mc.getAttr("L_pinky_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_D_JNT_PLC", a=1, t=[0.718116979929166, -0.33188284893684283, -0.2930869059130021])
			mc.xform("L_pinky_D_JNT_PLC", a=1, ro=[16.03066153003638, 18.580164169382392, -18.887046322885727])
			mc.xform("L_pinky_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_E_JNT_PLC"):
			if not mc.getAttr("L_pinky_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_E_JNT_PLC", a=1, t=[0.6589345815362089, -0.39026533698078225, -0.40542280890348614])
			mc.xform("L_pinky_E_JNT_PLC", a=1, ro=[16.03143723794509, 18.58007661198998, -18.888576887048018])
			mc.xform("L_pinky_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_pinky_A_JNT_PLC"):
			if not mc.getAttr("L_pinky_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_pinky_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_pinky_A_JNT_PLC", a=1, t=[-0.5955678580654293, 0.5305443861028394, -0.09619550013641445])
			mc.xform("L_pinky_A_JNT_PLC", a=1, ro=[-31.163346716486487, 5.112855851864327, -43.80643026964389])
			mc.xform("L_pinky_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_JNT_PLC"):
			if not mc.getAttr("R_upLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_JNT_PLC", a=1, t=[0.03162532279801633, -0.36656713750518044, -0.6193781229449131])
			mc.xform("R_upLeg_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_JNT_PLC"):
			if not mc.getAttr("R_loLeg_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_JNT_PLC", a=1, t=[-0.08422578021917537, 8.109675610919009, -0.9298109825923865])
			mc.xform("R_loLeg_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_loLeg_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_end_JNT_PLC"):
			if not mc.getAttr("R_leg_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_leg_end_JNT_PLC.rotateOrder", 0)

			mc.xform("R_leg_end_JNT_PLC", a=1, t=[-0.19426589772099978, 16.326438538694656, -0.010730020235042548])
			mc.xform("R_leg_end_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_leg_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_handle_driver_JNT_PLC"):
			mc.xform("R_leg_IK_handle_driver_JNT_PLC", a=1, t=[4.9960036108132044e-15, -2.220446049250313e-16, -6.661338147750939e-16])
			mc.xform("R_leg_IK_handle_driver_JNT_PLC", a=1, ro=[-0.0015533898779605862, 9.97296896885037e-07, 5.40386685843313e-05])
			mc.xform("R_leg_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_A_JNT_PLC", a=1, t=[0.008455299310776043, 0.528685354503617, -0.5814646948744078])
			mc.xform("R_upLeg_twist_A_JNT_PLC", a=1, ro=[0.21409717527996522, 177.5758041266967, 91.4825939863346])
			mc.xform("R_upLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_A_JNT_PLC", a=1, t=[-0.10623380371954017, 4.953027408009347, -0.34599510550683443])
			mc.xform("R_loLeg_twist_A_JNT_PLC", a=1, ro=[0.2165174249840935, 174.3262431630392, 91.49484422440224])
			mc.xform("R_loLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_B_JNT_PLC", a=1, t=[-0.014712753014485047, 1.4239279907025155, -0.5435512668039024])
			mc.xform("R_upLeg_twist_B_JNT_PLC", a=1, ro=[0.21409717527996522, 177.5758041266967, 91.4825939863346])
			mc.xform("R_upLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_B_JNT_PLC", a=1, t=[-0.12824182721990496, 5.796379205099684, -0.2621783413983916])
			mc.xform("R_loLeg_twist_B_JNT_PLC", a=1, ro=[0.2165174249840935, 174.3262431630392, 91.49484422440224])
			mc.xform("R_loLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_C_JNT_PLC", a=1, t=[-0.037883762082714934, 2.319180482711313, -0.5056378387333972])
			mc.xform("R_upLeg_twist_C_JNT_PLC", a=1, ro=[0.21409717527996522, 177.5758041266967, 91.4825939863346])
			mc.xform("R_upLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_C_JNT_PLC", a=1, t=[-0.15024985072026997, 6.639731002190021, -0.1783625628709385])
			mc.xform("R_loLeg_twist_C_JNT_PLC", a=1, ro=[0.2165174249840935, 174.3262431630392, 91.49484422440224])
			mc.xform("R_loLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("R_upLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upLeg_twist_D_JNT_PLC", a=1, t=[-0.06105477115094515, 3.2144231189102133, -0.46772441066289183])
			mc.xform("R_upLeg_twist_D_JNT_PLC", a=1, ro=[0.21409717527996522, 177.5758041266967, 91.4825939863346])
			mc.xform("R_upLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("R_loLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loLeg_twist_D_JNT_PLC", a=1, t=[-0.17225787422063477, 7.483082799280358, -0.09454579876249564])
			mc.xform("R_loLeg_twist_D_JNT_PLC", a=1, ro=[0.2165174249840935, 174.3262431630392, 91.49484422440224])
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
			mc.xform("R_foot_IK_handle_driver_JNT_PLC", a=1, t=[-3.3306690738754696e-16, -2.220446049250313e-16, 0.0])
			mc.xform("R_foot_IK_handle_driver_JNT_PLC", a=1, ro=[-9.826557704379517e-08, 1.4952100756268487e-05, -0.00013359645573403787])
			mc.xform("R_foot_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ankle_JNT_PLC"):
			if not mc.getAttr("R_ankle_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ankle_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ankle_JNT_PLC", a=1, t=[0.056588118105550755, 0.19426589772099978, 0.09236470803225239])
			mc.xform("R_ankle_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_ankle_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ball_JNT_PLC"):
			if not mc.getAttr("R_ball_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ball_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ball_JNT_PLC", a=1, t=[2.5243054721811617, 0.20420055409733984, 0.9564245274995957])
			mc.xform("R_ball_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_ball_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_JNT_PLC"):
			if not mc.getAttr("R_toe_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_toe_JNT_PLC.rotateOrder", 0)

			mc.xform("R_toe_JNT_PLC", a=1, t=[4.165384511590044, 0.2049495956495243, 0.9968796703844806])
			mc.xform("R_toe_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_toe_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_JNT_PLC"):
			if not mc.getAttr("R_shoulder_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_shoulder_JNT_PLC.rotateOrder", 0)

			mc.xform("R_shoulder_JNT_PLC", a=1, t=[-0.349858563188599, -0.2085489374239664, -0.7535781814800488])
			mc.xform("R_shoulder_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_shoulder_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upArm_JNT_PLC"):
			if not mc.getAttr("R_upArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upArm_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upArm_JNT_PLC", a=1, t=[-3.2639760807194786, -0.529651223873536, 0.07616668446626511])
			mc.xform("R_upArm_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loArm_JNT_PLC"):
			if not mc.getAttr("R_loArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loArm_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loArm_JNT_PLC", a=1, t=[-7.684109624207431, 1.9655441677912098, 0.9885327849825734])
			mc.xform("R_loArm_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_loArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_JNT_PLC"):
			if not mc.getAttr("R_wrist_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_wrist_JNT_PLC.rotateOrder", 0)

			mc.xform("R_wrist_JNT_PLC", a=1, t=[-11.535247550712372, 3.5840652691033092, -0.1961513141543273])
			mc.xform("R_wrist_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_wrist_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_end_JNT_PLC"):
			if not mc.getAttr("R_wrist_end_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_wrist_end_JNT_PLC.rotateOrder", 0)

			mc.xform("R_wrist_end_JNT_PLC", a=1, t=[-12.418737113810984, 3.9357205662340853, -0.3215891634584895])
			mc.xform("R_wrist_end_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_wrist_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_handle_driver_JNT_PLC"):
			mc.xform("R_arm_IK_handle_driver_JNT_PLC", a=1, t=[4.440892098500626e-15, -1.7763568394002505e-15, -8.881784197001252e-16])
			mc.xform("R_arm_IK_handle_driver_JNT_PLC", a=1, ro=[-4.245407455187192e-05, 4.870666638035589e-05, -0.002583883360888561])
			mc.xform("R_arm_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upArm_twist_A_JNT_PLC"):
			if not mc.getAttr("R_upArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upArm_twist_A_JNT_PLC", a=1, t=[-1.7479949047691512, -0.030651568780177385, 0.15864010168572473])
			mc.xform("R_upArm_twist_A_JNT_PLC", a=1, ro=[-11.773754719829356, 6.765392783563176, -45.8747731304331])
			mc.xform("R_upArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loArm_twist_A_JNT_PLC"):
			if not mc.getAttr("R_loArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loArm_twist_A_JNT_PLC", a=1, t=[-4.054333267184461, 2.2892089648140406, 0.35159616227139107])
			mc.xform("R_loArm_twist_A_JNT_PLC", a=1, ro=[-12.144195685182646, 344.4402281074445, -41.1644509910622])
			mc.xform("R_loArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upArm_twist_B_JNT_PLC"):
			if not mc.getAttr("R_upArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upArm_twist_B_JNT_PLC", a=1, t=[-2.232023584628721, 0.4683480863131848, 0.24111351890518423])
			mc.xform("R_upArm_twist_B_JNT_PLC", a=1, ro=[-11.773754719829356, 6.765392783563176, -45.8747731304331])
			mc.xform("R_upArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loArm_twist_B_JNT_PLC"):
			if not mc.getAttr("R_loArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loArm_twist_B_JNT_PLC", a=1, t=[-4.424566765971386, 2.612972319935844, 0.2146595395602089])
			mc.xform("R_loArm_twist_B_JNT_PLC", a=1, ro=[-12.144195685182646, 344.4402281074445, -41.1644509910622])
			mc.xform("R_loArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upArm_twist_C_JNT_PLC"):
			if not mc.getAttr("R_upArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upArm_twist_C_JNT_PLC", a=1, t=[-2.7160522644882907, 0.9674462995055162, 0.32358693612464384])
			mc.xform("R_upArm_twist_C_JNT_PLC", a=1, ro=[-11.773754719829356, 6.765392783563176, -45.8747731304331])
			mc.xform("R_upArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loArm_twist_C_JNT_PLC"):
			if not mc.getAttr("R_loArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loArm_twist_C_JNT_PLC", a=1, t=[-4.794790408948416, 2.9366371169586767, 0.07772291684902673])
			mc.xform("R_loArm_twist_C_JNT_PLC", a=1, ro=[-12.144195685182646, 344.4402281074445, -41.1644509910622])
			mc.xform("R_loArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upArm_twist_D_JNT_PLC"):
			if not mc.getAttr("R_upArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upArm_twist_D_JNT_PLC", a=1, t=[-3.2000809443478606, 1.4664459545988766, 0.40606035334410334])
			mc.xform("R_upArm_twist_D_JNT_PLC", a=1, ro=[-11.773754719829356, 6.765392783563176, -45.8747731304331])
			mc.xform("R_upArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_loArm_twist_D_JNT_PLC"):
			if not mc.getAttr("R_loArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_loArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_loArm_twist_D_JNT_PLC", a=1, t=[-5.165023907735343, 3.2604004720804785, -0.05921439576884823])
			mc.xform("R_loArm_twist_D_JNT_PLC", a=1, ro=[-12.144195685182646, 344.4402281074445, -41.1644509910622])
			mc.xform("R_loArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_B_JNT_PLC"):
			if not mc.getAttr("R_thumb_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_B_JNT_PLC", a=1, t=[-0.4860875903276809, 0.049693575909232734, 1.7836909929513922e-05])
			mc.xform("R_thumb_B_JNT_PLC", a=1, ro=[5.168401357378215e-14, -6.361109362927035e-15, 4.373262687012333e-15])
			mc.xform("R_thumb_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_C_JNT_PLC"):
			if not mc.getAttr("R_thumb_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_C_JNT_PLC", a=1, t=[-0.5763636864430679, 0.2126808475629023, -0.025302651625384698])
			mc.xform("R_thumb_C_JNT_PLC", a=1, ro=[5.168401357378215e-14, -6.361109362927035e-15, 4.373262687012333e-15])
			mc.xform("R_thumb_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_D_JNT_PLC"):
			if not mc.getAttr("R_thumb_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_D_JNT_PLC", a=1, t=[-0.7462868368073416, 0.24178586378770994, -0.022525393297673446])
			mc.xform("R_thumb_D_JNT_PLC", a=1, ro=[5.168401357378215e-14, -6.361109362927035e-15, 4.373262687012333e-15])
			mc.xform("R_thumb_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_A_JNT_PLC"):
			if not mc.getAttr("R_thumb_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_A_JNT_PLC", a=1, t=[0.043954007942016204, 1.0187948587364932, 0.015534516213332239])
			mc.xform("R_thumb_A_JNT_PLC", a=1, ro=[-31.433200545086272, -40.27726976485678, -146.17120028328821])
			mc.xform("R_thumb_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_B_JNT_PLC"):
			if not mc.getAttr("R_index_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_B_JNT_PLC", a=1, t=[-0.7557063782725489, 0.0496017304994254, 3.1544322984800033e-06])
			mc.xform("R_index_B_JNT_PLC", a=1, ro=[0.0, -9.54166404439055e-15, 0.0])
			mc.xform("R_index_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_C_JNT_PLC"):
			if not mc.getAttr("R_index_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_C_JNT_PLC", a=1, t=[-1.1702769605829646, 0.35329815207895265, -0.03447179592604588])
			mc.xform("R_index_C_JNT_PLC", a=1, ro=[-2.0073814384625015, -2.933206938367644, -33.06812474892578])
			mc.xform("R_index_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_D_JNT_PLC"):
			if not mc.getAttr("R_index_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_D_JNT_PLC", a=1, t=[-1.155578559876819, 0.557902193976819, -0.05649699013384257])
			mc.xform("R_index_D_JNT_PLC", a=1, ro=[-1.3575635030493938, -3.2808309257890897, -45.07377998689652])
			mc.xform("R_index_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_E_JNT_PLC"):
			if not mc.getAttr("R_index_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_E_JNT_PLC", a=1, t=[-1.0431694111611374, 0.7716152653438719, -0.07784439386393416])
			mc.xform("R_index_E_JNT_PLC", a=1, ro=[-1.356049513250428, -3.282734566469433, -45.077509909660975])
			mc.xform("R_index_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_A_JNT_PLC"):
			if not mc.getAttr("R_index_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_A_JNT_PLC", a=1, t=[-0.14178486976205562, 0.6956559152414172, -0.3566053677526631])
			mc.xform("R_index_A_JNT_PLC", a=1, ro=[4.966824508924262, -24.631324573818777, 149.19800472866402])
			mc.xform("R_index_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_B_JNT_PLC"):
			if not mc.getAttr("R_middle_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_B_JNT_PLC", a=1, t=[-0.7035628497049953, 0.049685472561286304, -2.8729567280727508e-05])
			mc.xform("R_middle_B_JNT_PLC", a=1, ro=[-1.1131941385122306e-14, -3.9756933518293826e-16, 1.2722218725854064e-14])
			mc.xform("R_middle_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_C_JNT_PLC"):
			if not mc.getAttr("R_middle_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_C_JNT_PLC", a=1, t=[-1.1631666216425969, 0.27701515438167945, 0.05905344448426675])
			mc.xform("R_middle_C_JNT_PLC", a=1, ro=[-1.1131941385122306e-14, -3.9756933518293826e-16, 1.2722218725854064e-14])
			mc.xform("R_middle_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_D_JNT_PLC"):
			if not mc.getAttr("R_middle_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_D_JNT_PLC", a=1, t=[-1.1694290206344429, 0.5017582100210234, 0.07776401559092427])
			mc.xform("R_middle_D_JNT_PLC", a=1, ro=[-1.1131941385122306e-14, -3.9756933518293826e-16, 1.2722218725854064e-14])
			mc.xform("R_middle_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_E_JNT_PLC"):
			if not mc.getAttr("R_middle_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_E_JNT_PLC", a=1, t=[-1.1213486625371085, 0.6960539055926382, 0.1071247982985768])
			mc.xform("R_middle_E_JNT_PLC", a=1, ro=[-1.1131941385122306e-14, -3.9756933518293826e-16, 1.2722218725854064e-14])
			mc.xform("R_middle_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_A_JNT_PLC"):
			if not mc.getAttr("R_middle_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_A_JNT_PLC", a=1, t=[-0.1121681610210814, 0.5966050257749309, 0.2820272854772839])
			mc.xform("R_middle_A_JNT_PLC", a=1, ro=[-9.48829350771243, 0.15938052337367603, 143.8257875972932])
			mc.xform("R_middle_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_B_JNT_PLC"):
			if not mc.getAttr("R_ring_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_B_JNT_PLC", a=1, t=[1.1279901194538589e-05, -3.3835645645297063e-06, -2.241835683314264e-06])
			mc.xform("R_ring_B_JNT_PLC", a=1, ro=[-1.0336802714756429e-14, -6.361109362927032e-15, 5.738078187465204e-31])
			mc.xform("R_ring_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_C_JNT_PLC"):
			if not mc.getAttr("R_ring_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_C_JNT_PLC", a=1, t=[-1.1854646137330835, 0.3356400467316476, 0.025231945455290283])
			mc.xform("R_ring_C_JNT_PLC", a=1, ro=[1.468068013895139, 2.3399923446798367, -38.32763622359728])
			mc.xform("R_ring_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_D_JNT_PLC"):
			if not mc.getAttr("R_ring_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_D_JNT_PLC", a=1, t=[-1.1898256421108497, 0.6054969212564956, 0.04497517127825823])
			mc.xform("R_ring_D_JNT_PLC", a=1, ro=[0.9627975577308036, 2.5890618593950334, -50.03700295999737])
			mc.xform("R_ring_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_E_JNT_PLC"):
			if not mc.getAttr("R_ring_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_E_JNT_PLC", a=1, t=[-1.0964330150807002, 0.8920728841829693, 0.06482861564187914])
			mc.xform("R_ring_E_JNT_PLC", a=1, ro=[-1.0336802714756429e-14, -6.361109362927032e-15, 5.738078187465204e-31])
			mc.xform("R_ring_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_A_JNT_PLC"):
			if not mc.getAttr("R_ring_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_A_JNT_PLC", a=1, t=[-0.0541174407267917, 0.6452270212676048, 0.3648464674616743])
			mc.xform("R_ring_A_JNT_PLC", a=1, ro=[-8.084198189509411, -11.391045831985089, 149.7307219734224])
			mc.xform("R_ring_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_B_JNT_PLC"):
			if not mc.getAttr("R_pinky_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_B_JNT_PLC", a=1, t=[-0.6154721824203371, 0.04992906618440074, -3.52486200476676e-05])
			mc.xform("R_pinky_B_JNT_PLC", a=1, ro=[18.274541669683863, 15.639863701634049, -10.70772275805884])
			mc.xform("R_pinky_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_C_JNT_PLC"):
			if not mc.getAttr("R_pinky_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_C_JNT_PLC", a=1, t=[-0.8421525436220945, 0.19371385423960064, 0.17139597937927675])
			mc.xform("R_pinky_C_JNT_PLC", a=1, ro=[10.808565753239945, 21.952132058666173, -33.88328748286179])
			mc.xform("R_pinky_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_D_JNT_PLC"):
			if not mc.getAttr("R_pinky_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_D_JNT_PLC", a=1, t=[-0.7180180529219786, 0.3317945890275489, 0.2930437168713649])
			mc.xform("R_pinky_D_JNT_PLC", a=1, ro=[16.030661530036348, 18.580164169382392, -18.887046322885745])
			mc.xform("R_pinky_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_E_JNT_PLC"):
			if not mc.getAttr("R_pinky_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_E_JNT_PLC", a=1, t=[-0.6588758270857937, 0.390221309033965, 0.4054016561174212])
			mc.xform("R_pinky_E_JNT_PLC", a=1, ro=[16.031437237945067, 18.58007661198997, -18.888576887048043])
			mc.xform("R_pinky_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_A_JNT_PLC"):
			if not mc.getAttr("R_pinky_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_A_JNT_PLC", a=1, t=[-0.09556112134436212, 0.5304068359656533, 1.0961960096641987])
			mc.xform("R_pinky_A_JNT_PLC", a=1, ro=[-31.163346716486462, 5.11285585186432, 136.1935697303561])
			mc.xform("R_pinky_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

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
			mc.xform("L_innerBall_PIV_CTL", a=1, ro=[-3.0549104212812654, 4.76349828529822, 2.593157532725474e-15])
			mc.xform("L_innerBall_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterBall_PIV_CTL"):
			mc.xform("L_outterBall_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterBall_PIV_CTL", a=1, ro=[-3.0549104212812654, 4.76349828529822, 2.593157532725474e-15])
			mc.xform("L_outterBall_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_heel_PIV_CTL"):
			mc.xform("L_heel_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_heel_PIV_CTL", a=1, ro=[-3.0549104212812654, 4.76349828529822, 2.593157532725474e-15])
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

		if mc.objExists("R_upLeg_FK_PIV_CTL"):
			if not mc.getAttr("R_upLeg_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_FK_PIV_CTL", a=1, t=[-3.0685530347795975e-06, -5.281988439964636e-07, 1.1125371113251958e-07])
			mc.xform("R_upLeg_FK_PIV_CTL", a=1, ro=[0.0015539553661390283, 1.8694402895955457e-06, 179.9999658970656])
			mc.xform("R_upLeg_FK_PIV_CTL", r=1, s=[0.9999999999999998, 1.0000000000000004, -1.0000000000000002])

		if mc.objExists("R_loLeg_FK_PIV_CTL"):
			if not mc.getAttr("R_loLeg_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_FK_PIV_CTL", a=1, t=[1.5230252339293315e-06, 2.1393756113319284e-06, -1.215051829150937e-07])
			mc.xform("R_loLeg_FK_PIV_CTL", a=1, ro=[0.0015533898779669245, 2.523195207061083e-16, -179.9999459613314])
			mc.xform("R_loLeg_FK_PIV_CTL", r=1, s=[0.9999999999999997, 1.0, -1.0])

		if mc.objExists("R_legEnd_FK_PIV_CTL"):
			if not mc.getAttr("R_legEnd_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_legEnd_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_legEnd_FK_PIV_CTL", a=1, t=[9.946842016717028e-09, -1.8586173911039339e-06, -4.77212436233998e-08])
			mc.xform("R_legEnd_FK_PIV_CTL", a=1, ro=[0.0015533898779661296, 6.4980300025308e-16, -179.99994596133138])
			mc.xform("R_legEnd_FK_PIV_CTL", r=1, s=[0.9999999999999997, 0.9999999999999999, -1.0])

		if mc.objExists("R_leg_IK_PIV_CTL"):
			mc.xform("R_leg_IK_PIV_CTL", a=1, t=[4.9960036108132044e-15, -4.440892098500626e-16, -2.220446049250313e-16])
			mc.xform("R_leg_IK_PIV_CTL", a=1, ro=[179.99844837439244, -2.3914931264383798e-20, -1.7661794469383253e-15])
			mc.xform("R_leg_IK_PIV_CTL", r=1, s=[0.9999999999999996, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_leg_PV_PIV_CTL"):
			mc.xform("R_leg_PV_PIV_CTL", a=1, t=[-1.552601095688999e-06, 0.00026836464675117355, 9.99995975218514])
			mc.xform("R_leg_PV_PIV_CTL", a=1, ro=[0.001554304934696472, 1.5985282158058811e-06, -179.9999912555329])
			mc.xform("R_leg_PV_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000004, -0.9999999999999996])

		if mc.objExists("R_legBase_PIV_CTL"):
			if not mc.getAttr("R_legBase_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_PIV_CTL.rotateOrder", 0)

			mc.xform("R_legBase_PIV_CTL", a=1, t=[-3.0685530347795975e-06, -5.281988439964636e-07, 1.1125371113251958e-07])
			mc.xform("R_legBase_PIV_CTL", a=1, ro=[0.0015539553661390283, 1.8694402895955457e-06, 179.9999658970656])
			mc.xform("R_legBase_PIV_CTL", r=1, s=[0.9999999999999998, 1.0000000000000004, -1.0000000000000002])

		if mc.objExists("R_leg_IK_switch_PIV_CTL"):
			if not mc.getAttr("R_leg_IK_switch_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_PIV_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_PIV_CTL", a=1, t=[9.946842016717028e-09, -1.8586173911039339e-06, -4.77212436233998e-08])
			mc.xform("R_leg_IK_switch_PIV_CTL", a=1, ro=[0.0015533898779661296, 6.4980300025308e-16, -179.99994596133138])
			mc.xform("R_leg_IK_switch_PIV_CTL", r=1, s=[0.9999999999999997, 0.9999999999999999, -1.0])

		if mc.objExists("R_innerBall_PIV_CTL"):
			mc.xform("R_innerBall_PIV_CTL", a=1, t=[1.1102230246251565e-16, -2.7755575615628914e-16, 8.881784197001252e-16])
			mc.xform("R_innerBall_PIV_CTL", a=1, ro=[3.054910421281263, -4.763498285298221, -180.0])
			mc.xform("R_innerBall_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0])

		if mc.objExists("R_outterBall_PIV_CTL"):
			mc.xform("R_outterBall_PIV_CTL", a=1, t=[0.0, -1.3877787807814457e-16, 4.440892098500626e-16])
			mc.xform("R_outterBall_PIV_CTL", a=1, ro=[3.054910421281263, -4.763498285298221, -180.0])
			mc.xform("R_outterBall_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0])

		if mc.objExists("R_heel_PIV_CTL"):
			mc.xform("R_heel_PIV_CTL", a=1, t=[1.1102230246251565e-16, 0.0, -2.220446049250313e-16])
			mc.xform("R_heel_PIV_CTL", a=1, ro=[3.054910421281263, -4.763498285298221, -180.0])
			mc.xform("R_heel_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0])

		if mc.objExists("R_toeTip_PIV_CTL"):
			mc.xform("R_toeTip_PIV_CTL", a=1, t=[0.0, -1.3877787807814457e-16, 6.661338147750939e-16])
			mc.xform("R_toeTip_PIV_CTL", a=1, ro=[1.7114110872626014e-05, -0.0001000111583899304, -179.99999466255167])
			mc.xform("R_toeTip_PIV_CTL", r=1, s=[1.0, 1.0000000000000002, -1.0000000000000002])

		if mc.objExists("R_reverseBall_PIV_CTL"):
			mc.xform("R_reverseBall_PIV_CTL", a=1, t=[0.0, -1.942890293094024e-16, -8.881784197001252e-16])
			mc.xform("R_reverseBall_PIV_CTL", a=1, ro=[-179.99998288588912, 0.0001000111583938665, -5.337448324291366e-06])
			mc.xform("R_reverseBall_PIV_CTL", r=1, s=[0.9999999999999997, 1.0, -0.9999999999999993])

		if mc.objExists("R_ankleOffset_PIV_CTL"):
			mc.xform("R_ankleOffset_PIV_CTL", a=1, t=[2.220446049250313e-16, 1.1102230246251565e-16, 2.220446049250313e-16])
			mc.xform("R_ankleOffset_PIV_CTL", a=1, ro=[-179.99998504796136, 0.00011953624829900721, 179.99994034174009])
			mc.xform("R_ankleOffset_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, -1.0])

		if mc.objExists("R_toe_IK_PIV_CTL"):
			mc.xform("R_toe_IK_PIV_CTL", a=1, t=[8.881784197001252e-16, 0.0, 0.0])
			mc.xform("R_toe_IK_PIV_CTL", a=1, ro=[-3.275781006466382e-14, -2.1682791454303856e-06, 179.9997413607546])
			mc.xform("R_toe_IK_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000004, -1.0])

		if mc.objExists("R_toe_FK_PIV_CTL"):
			if not mc.getAttr("R_toe_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_toe_FK_PIV_CTL", a=1, t=[-3.600261093694712e-07, 1.6697873794768725e-06, 2.9010333207901695e-07])
			mc.xform("R_toe_FK_PIV_CTL", a=1, ro=[-3.275781006466382e-14, -2.1682791454303856e-06, 179.9997413607546])
			mc.xform("R_toe_FK_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000004, -1.0])

		if mc.objExists("R_upArm_FK_PIV_CTL"):
			if not mc.getAttr("R_upArm_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upArm_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upArm_FK_PIV_CTL", a=1, t=[2.7157037257197203e-05, -2.102384387114853e-05, -7.690519119307737e-07])
			mc.xform("R_upArm_FK_PIV_CTL", a=1, ro=[-0.002105778879197801, 1.5086769751940717e-05, -179.9998803215295])
			mc.xform("R_upArm_FK_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0000000000000002])

		if mc.objExists("R_loArm_FK_PIV_CTL"):
			if not mc.getAttr("R_loArm_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_loArm_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_loArm_FK_PIV_CTL", a=1, t=[2.8225115212165974e-05, -2.8335499544951404e-05, -1.3703313444413112e-05])
			mc.xform("R_loArm_FK_PIV_CTL", a=1, ro=[-0.0019875241231907016, -0.0003440006929162853, 179.99929405469828])
			mc.xform("R_loArm_FK_PIV_CTL", r=1, s=[0.9999999999999998, 1.0, -0.9999999999999996])

		if mc.objExists("R_wrist_FK_PIV_CTL"):
			if not mc.getAttr("R_wrist_FK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_FK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_wrist_FK_PIV_CTL", a=1, t=[-3.4751930777510154e-06, 3.402726324708283e-06, 1.181683986217763e-07])
			mc.xform("R_wrist_FK_PIV_CTL", a=1, ro=[4.245407459242379e-05, -4.870666637081332e-05, 179.99741611663913])
			mc.xform("R_wrist_FK_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, -1.0])

		if mc.objExists("R_arm_IK_PIV_CTL"):
			if not mc.getAttr("R_arm_IK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_PIV_CTL", a=1, t=[-3.4751930777510154e-06, 3.402726324708283e-06, 1.181683986217763e-07])
			mc.xform("R_arm_IK_PIV_CTL", a=1, ro=[4.245407459242379e-05, -4.870666637081332e-05, 179.99741611663913])
			mc.xform("R_arm_IK_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, -1.0])

		if mc.objExists("R_wrist_IK_PIV_CTL"):
			if not mc.getAttr("R_wrist_IK_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_PIV_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_PIV_CTL", a=1, t=[-3.4751930777510154e-06, 3.402726324708283e-06, 1.181683986217763e-07])
			mc.xform("R_wrist_IK_PIV_CTL", a=1, ro=[4.245407459242379e-05, -4.870666637081332e-05, 179.99741611663913])
			mc.xform("R_wrist_IK_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, -1.0])

		if mc.objExists("R_arm_PV_PIV_CTL"):
			mc.xform("R_arm_PV_PIV_CTL", a=1, t=[2.22131121985214e-05, -0.00038061019886370673, 9.999988800460113])
			mc.xform("R_arm_PV_PIV_CTL", a=1, ro=[-0.0020962709843959345, -5.881389886322366e-05, 179.99976703065784])
			mc.xform("R_arm_PV_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000004])

		if mc.objExists("R_shoulder_PIV_CTL"):
			if not mc.getAttr("R_shoulder_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_PIV_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_PIV_CTL", a=1, t=[-3.5473167865340827e-06, -1.7633338023514966e-05, -9.215727958533648e-09])
			mc.xform("R_shoulder_PIV_CTL", a=1, ro=[-1.608734406554536e-05, -8.213899970522619e-05, -179.99943451839323])
			mc.xform("R_shoulder_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999998, -0.9999999999999999])

		if mc.objExists("R_arm_IK_switch_PIV_CTL"):
			if not mc.getAttr("R_arm_IK_switch_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_PIV_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_PIV_CTL", a=1, t=[-3.4751930777510154e-06, 3.402726324708283e-06, 1.181683986217763e-07])
			mc.xform("R_arm_IK_switch_PIV_CTL", a=1, ro=[4.245407459242379e-05, -4.870666637081332e-05, 179.99741611663913])
			mc.xform("R_arm_IK_switch_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, -1.0])

		if mc.objExists("R_thumb_A_PIV_CTL"):
			if not mc.getAttr("R_thumb_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_A_PIV_CTL", a=1, t=[-4.884981308350689e-15, 5.329070518200751e-15, -3.552713678800501e-15])
			mc.xform("R_thumb_A_PIV_CTL", a=1, ro=[-1.8859939965375673e-14, 0.0009447167950532077, 179.99999354996112])
			mc.xform("R_thumb_A_PIV_CTL", r=1, s=[1.0, 0.9999999999999999, -1.0000000000000002])

		if mc.objExists("R_thumb_B_PIV_CTL"):
			if not mc.getAttr("R_thumb_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_B_PIV_CTL", a=1, t=[-1.7763568394002505e-15, 4.440892098500626e-15, 7.105427357601002e-15])
			mc.xform("R_thumb_B_PIV_CTL", a=1, ro=[-0.0014145385957760428, 0.0036818268876645335, 179.9939138523471])
			mc.xform("R_thumb_B_PIV_CTL", r=1, s=[1.0, 0.9999999999999997, -0.9999999999999999])

		if mc.objExists("R_thumb_C_PIV_CTL"):
			if not mc.getAttr("R_thumb_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_C_PIV_CTL", a=1, t=[0.0, 3.552713678800501e-15, -3.552713678800501e-15])
			mc.xform("R_thumb_C_PIV_CTL", a=1, ro=[0.0005124346808809306, -0.0032621551363119523, -179.99445412669812])
			mc.xform("R_thumb_C_PIV_CTL", r=1, s=[1.0000000000000004, 0.9999999999999998, -1.0000000000000002])

		if mc.objExists("R_index_A_PIV_CTL"):
			if not mc.getAttr("R_index_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_A_PIV_CTL", a=1, t=[-6.661338147750939e-16, 7.105427357601002e-15, -8.881784197001252e-16])
			mc.xform("R_index_A_PIV_CTL", a=1, ro=[-3.167311455788997e-14, -0.0006027003906716217, 179.99549024378135])
			mc.xform("R_index_A_PIV_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, -0.9999999999999998])

		if mc.objExists("R_index_B_PIV_CTL"):
			if not mc.getAttr("R_index_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_B_PIV_CTL", a=1, t=[-6.217248937900877e-15, 0.0, -6.661338147750939e-16])
			mc.xform("R_index_B_PIV_CTL", a=1, ro=[-0.00018067561973892106, 0.0005218066178313647, -179.99695696614737])
			mc.xform("R_index_B_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_index_C_PIV_CTL"):
			if not mc.getAttr("R_index_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_C_PIV_CTL", a=1, t=[3.552713678800501e-15, 0.0, 4.388850394221322e-16])
			mc.xform("R_index_C_PIV_CTL", a=1, ro=[1.8153229232340605e-14, 0.0006977007342983042, -179.99964992404816])
			mc.xform("R_index_C_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999998, -1.0])

		if mc.objExists("R_index_D_PIV_CTL"):
			if not mc.getAttr("R_index_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_D_PIV_CTL", a=1, t=[-5.329070518200751e-15, -1.7763568394002505e-15, -4.909267437014364e-16])
			mc.xform("R_index_D_PIV_CTL", a=1, ro=[-1.858877289240166e-14, -0.0010142267845394007, 179.9978559666285])
			mc.xform("R_index_D_PIV_CTL", r=1, s=[1.0, 0.9999999999999998, -0.9999999999999998])

		if mc.objExists("R_middle_A_PIV_CTL"):
			if not mc.getAttr("R_middle_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_A_PIV_CTL", a=1, t=[-2.220446049250313e-15, 1.0658141036401503e-14, 1.7763568394002505e-15])
			mc.xform("R_middle_A_PIV_CTL", a=1, ro=[8.040498681599515e-15, 3.182635348417793e-05, -179.9998142880374])
			mc.xform("R_middle_A_PIV_CTL", r=1, s=[1.0, 0.9999999999999998, -1.0000000000000002])

		if mc.objExists("R_middle_B_PIV_CTL"):
			if not mc.getAttr("R_middle_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_B_PIV_CTL", a=1, t=[-7.993605777301127e-15, 7.105427357601002e-15, 4.440892098500626e-16])
			mc.xform("R_middle_B_PIV_CTL", a=1, ro=[-3.785652973518673e-05, 0.00016052562052837772, -179.99911140794907])
			mc.xform("R_middle_B_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, -1.0000000000000002])

		if mc.objExists("R_middle_C_PIV_CTL"):
			if not mc.getAttr("R_middle_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_C_PIV_CTL", a=1, t=[-3.552713678800501e-15, 3.552713678800501e-15, 4.440892098500626e-16])
			mc.xform("R_middle_C_PIV_CTL", a=1, ro=[0.0003909398612204008, -0.0005857569623729887, 179.9977789241384])
			mc.xform("R_middle_C_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999996, -1.0])

		if mc.objExists("R_middle_D_PIV_CTL"):
			if not mc.getAttr("R_middle_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_D_PIV_CTL", a=1, t=[0.0, 0.0, 4.440892098500626e-16])
			mc.xform("R_middle_D_PIV_CTL", a=1, ro=[-4.685497161129829e-05, 6.295558144723405e-05, -179.999437723364])
			mc.xform("R_middle_D_PIV_CTL", r=1, s=[1.0, 1.0, -0.9999999999999998])

		if mc.objExists("R_ring_A_PIV_CTL"):
			if not mc.getAttr("R_ring_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_A_PIV_CTL", a=1, t=[-4.440892098500626e-16, 7.105427357601002e-15, 2.6645352591003757e-15])
			mc.xform("R_ring_A_PIV_CTL", a=1, ro=[-4.527103885239301e-05, -0.0003395327913103121, 179.999266260498])
			mc.xform("R_ring_A_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999999, -1.0])

		if mc.objExists("R_ring_B_PIV_CTL"):
			if not mc.getAttr("R_ring_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_B_PIV_CTL", a=1, t=[-1.7763568394002505e-15, 0.0, 0.0])
			mc.xform("R_ring_B_PIV_CTL", a=1, ro=[-9.00946445870878e-05, 0.00046011509215987016, -179.99828813660082])
			mc.xform("R_ring_B_PIV_CTL", r=1, s=[0.9999999999999997, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_ring_C_PIV_CTL"):
			if not mc.getAttr("R_ring_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_C_PIV_CTL", a=1, t=[7.105427357601002e-15, -3.552713678800501e-15, 4.440892098500626e-16])
			mc.xform("R_ring_C_PIV_CTL", a=1, ro=[-2.842440993437593e-14, -0.0018605264532177816, 179.99527606229418])
			mc.xform("R_ring_C_PIV_CTL", r=1, s=[1.0, 0.9999999999999996, -0.9999999999999999])

		if mc.objExists("R_ring_D_PIV_CTL"):
			if not mc.getAttr("R_ring_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_D_PIV_CTL", a=1, t=[-3.552713678800501e-15, -1.7763568394002505e-15, -1.7763568394002505e-15])
			mc.xform("R_ring_D_PIV_CTL", a=1, ro=[0.00014049192879808645, 0.000504272084605796, -179.99859034698085])
			mc.xform("R_ring_D_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -0.9999999999999998])

		if mc.objExists("R_pinky_A_PIV_CTL"):
			if not mc.getAttr("R_pinky_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_A_PIV_CTL", a=1, t=[-3.552713678800501e-15, 7.105427357601002e-15, 3.552713678800501e-15])
			mc.xform("R_pinky_A_PIV_CTL", a=1, ro=[-2.8364953304714144e-14, -0.0020390246171137463, 179.99589669622046])
			mc.xform("R_pinky_A_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -1.0])

		if mc.objExists("R_pinky_B_PIV_CTL"):
			if not mc.getAttr("R_pinky_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_B_PIV_CTL", a=1, t=[-1.7763568394002505e-15, -3.552713678800501e-15, -2.220446049250313e-15])
			mc.xform("R_pinky_B_PIV_CTL", a=1, ro=[-5.641690105739879e-15, -0.00016084412260978145, -179.99892430199006])
			mc.xform("R_pinky_B_PIV_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, -0.9999999999999999])

		if mc.objExists("R_pinky_C_PIV_CTL"):
			if not mc.getAttr("R_pinky_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_C_PIV_CTL", a=1, t=[1.7763568394002505e-15, -1.7763568394002505e-15, -2.220446049250313e-15])
			mc.xform("R_pinky_C_PIV_CTL", a=1, ro=[-7.108421016520861e-15, 0.0007136068881045721, 179.99844797625138])
			mc.xform("R_pinky_C_PIV_CTL", r=1, s=[0.9999999999999997, 0.9999999999999997, -1.0])

		if mc.objExists("R_pinky_D_PIV_CTL"):
			if not mc.getAttr("R_pinky_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_D_PIV_CTL", a=1, t=[0.0, -7.105427357601002e-15, 1.1102230246251565e-15])
			mc.xform("R_pinky_D_PIV_CTL", a=1, ro=[8.528304284831679e-15, -0.0006366949763188418, -179.99531093615963])
			mc.xform("R_pinky_D_PIV_CTL", r=1, s=[0.9999999999999996, 0.9999999999999996, -0.9999999999999998])

		if mc.objExists("R_hand_PIV_CTL"):
			mc.xform("R_hand_PIV_CTL", a=1, t=[-0.5000090443913674, -1.9998719140671817, 1.6653345369377348e-16])
			mc.xform("R_hand_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_hand_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, -1.0000000000000002])

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
			mc.xform("L_arm_PV_CTL", a=1, ro=[10.271260166632098, -6.220613507069252, 43.63365665734056])
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
			mc.xform("L_leg_PV_CTL", a=1, ro=[175.99205948083937, -0.11043862343333515, -88.51512080211955])
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

		if mc.objExists("R_upLeg_FK_CTL"):
			if not mc.getAttr("R_upLeg_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_upLeg_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upLeg_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_upLeg_FK_CTL.rotateOrder", 0)

			mc.xform("R_upLeg_FK_CTL", a=1, t=[0.0, 4.440892098500626e-16, -4.440892098500626e-16])
			mc.xform("R_upLeg_FK_CTL", a=1, ro=[5.963540027744094e-16, 1.9878466759146992e-16, -1.9077116067918868e-14])
			mc.xform("R_upLeg_FK_CTL", r=1, s=[1.0, 0.9999999999999999, 1.0])

		if mc.objExists("R_loLeg_FK_CTL"):
			if not mc.getAttr("R_loLeg_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_loLeg_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_loLeg_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_loLeg_FK_CTL.rotateOrder", 0)

			mc.xform("R_loLeg_FK_CTL", a=1, t=[-2.6645352591003757e-15, -2.220446049250313e-16, 1.1102230246251565e-16])
			mc.xform("R_loLeg_FK_CTL", a=1, ro=[3.975693351829396e-16, -7.951386703658792e-16, 4.969616689786745e-17])
			mc.xform("R_loLeg_FK_CTL", r=1, s=[1.0000000000000002, 1.0000000000000004, 1.0])

		if mc.objExists("R_legEnd_FK_CTL"):
			if not mc.getAttr("R_legEnd_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_legEnd_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_legEnd_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_legEnd_FK_CTL.rotateOrder", 0)

			mc.xform("R_legEnd_FK_CTL", a=1, t=[-3.3306690738754696e-16, 8.881784197001252e-16, -1.1102230246251565e-16])
			mc.xform("R_legEnd_FK_CTL", a=1, ro=[-7.951386703658792e-16, -1.5902773407317584e-15, -2.4848083448933712e-17])
			mc.xform("R_legEnd_FK_CTL", r=1, s=[1.0000000000000002, 0.9999999999999999, 1.0])

		if mc.objExists("R_leg_IK_D_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_leg_IK_D_OFF_CTL", a=1, ro=[1.4051591190372022e-14, 4.099933769074197e-16, -1.0813885916975958e-13])
			mc.xform("R_leg_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_C_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_leg_IK_C_OFF_CTL", a=1, ro=[1.4051591190372022e-14, 4.099933769074197e-16, -1.0813885916975958e-13])
			mc.xform("R_leg_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_B_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_leg_IK_B_OFF_CTL", a=1, ro=[1.4051591190372022e-14, 4.099933769074197e-16, -1.0813885916975958e-13])
			mc.xform("R_leg_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_A_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_A_OFF_CTL", a=1, t=[1.1102230246251565e-16, 0.0, 0.0])
			mc.xform("R_leg_IK_A_OFF_CTL", a=1, ro=[1.4051591190372022e-14, 4.099933769074197e-16, -1.0813885916975958e-13])
			mc.xform("R_leg_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_CTL"):
			if not mc.getAttr("R_leg_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_leg_IK_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("R_leg_IK_CTL.mirrorMode", l=1):
				mc.setAttr("R_leg_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_leg_IK_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_CTL", a=1, t=[-3.317553476378521e-08, 1.8583775363012478e-06, -4.655297303202133e-08])
			mc.xform("R_leg_IK_CTL", a=1, ro=[-2.5444437451708134e-14, 0.0, 0.0])
			mc.xform("R_leg_IK_CTL", r=1, s=[1.0000000000000002, 1.0, 0.9999999999999999])

		if mc.objExists("R_leg_PV_CTL"):
			if not mc.getAttr("R_leg_PV_CTL.mirrorMode", l=1):
				mc.setAttr("R_leg_PV_CTL.mirrorMode", 0)

			if not mc.getAttr("R_leg_PV_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_PV_CTL.rotateOrder", 0)

			mc.xform("R_leg_PV_CTL", a=1, t=[-2.7994851850010605e-06, 0.0, -4.016720505362059e-05])
			mc.xform("R_leg_PV_CTL", a=1, ro=[-4.0079405191606305, -0.1104386234334393, -88.51512080211955])
			mc.xform("R_leg_PV_CTL", r=1, s=[0.9999999999999994, 0.9999999999999997, 0.9999999999999998])

		if mc.objExists("R_legBase_D_OFF_CTL"):
			if not mc.getAttr("R_legBase_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_legBase_D_OFF_CTL", a=1, ro=[-5.963540027744094e-16, 3.975693351829396e-16, 9.318031293350144e-18])
			mc.xform("R_legBase_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_C_OFF_CTL"):
			if not mc.getAttr("R_legBase_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_legBase_C_OFF_CTL", a=1, ro=[-5.963540027744094e-16, 3.975693351829396e-16, 9.318031293350144e-18])
			mc.xform("R_legBase_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_B_OFF_CTL"):
			if not mc.getAttr("R_legBase_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_legBase_B_OFF_CTL", a=1, ro=[-5.963540027744094e-16, 3.975693351829396e-16, 9.318031293350144e-18])
			mc.xform("R_legBase_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_A_OFF_CTL"):
			if not mc.getAttr("R_legBase_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_legBase_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_legBase_A_OFF_CTL", a=1, ro=[-5.963540027744094e-16, 3.975693351829396e-16, 9.318031293350144e-18])
			mc.xform("R_legBase_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_legBase_CTL"):
			if not mc.getAttr("R_legBase_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_legBase_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_legBase_CTL.mirrorMode", l=1):
				mc.setAttr("R_legBase_CTL.mirrorMode", 0)

			if not mc.getAttr("R_legBase_CTL.rotateOrder", l=1):
				mc.setAttr("R_legBase_CTL.rotateOrder", 0)

			mc.xform("R_legBase_CTL", a=1, t=[0.0, 4.440892098500626e-16, -4.440892098500626e-16])
			mc.xform("R_legBase_CTL", a=1, ro=[5.963540027744094e-16, 1.9878466759146992e-16, -1.9077116067918868e-14])
			mc.xform("R_legBase_CTL", r=1, s=[1.0, 0.9999999999999999, 1.0])

		if mc.objExists("R_leg_IK_switch_D_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_D_OFF_CTL", a=1, t=[1.1102230246251565e-16, -4.440892098500626e-16, 0.0])
			mc.xform("R_leg_IK_switch_D_OFF_CTL", a=1, ro=[1.5905127720221035e-15, 9.972968958531318e-07, 2.7051561793032115e-11])
			mc.xform("R_leg_IK_switch_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_C_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_C_OFF_CTL", a=1, t=[-1.1102230246251565e-16, 4.440892098500626e-16, 0.0])
			mc.xform("R_leg_IK_switch_C_OFF_CTL", a=1, ro=[1.5905127720221035e-15, 9.972968958531318e-07, 2.7051561793032115e-11])
			mc.xform("R_leg_IK_switch_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_B_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_B_OFF_CTL", a=1, t=[1.1102230246251565e-16, -4.440892098500626e-16, 0.0])
			mc.xform("R_leg_IK_switch_B_OFF_CTL", a=1, ro=[1.5905127720221035e-15, 9.972968958531318e-07, 2.7051561793032115e-11])
			mc.xform("R_leg_IK_switch_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_A_OFF_CTL"):
			if not mc.getAttr("R_leg_IK_switch_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_A_OFF_CTL", a=1, t=[-1.1102230246251565e-16, 4.440892098500626e-16, 0.0])
			mc.xform("R_leg_IK_switch_A_OFF_CTL", a=1, ro=[1.5905127720221035e-15, 9.972968958531318e-07, 2.7051561793032115e-11])
			mc.xform("R_leg_IK_switch_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_leg_IK_switch_CTL"):
			if not mc.getAttr("R_leg_IK_switch_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_leg_IK_switch_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_leg_IK_switch_CTL.mirrorMode", l=1):
				mc.setAttr("R_leg_IK_switch_CTL.mirrorMode", 0)

			if not mc.getAttr("R_leg_IK_switch_CTL.rotateOrder", l=1):
				mc.setAttr("R_leg_IK_switch_CTL.rotateOrder", 0)

			mc.xform("R_leg_IK_switch_CTL", a=1, t=[-3.3306690738754696e-16, 8.881784197001252e-16, -1.1102230246251565e-16])
			mc.xform("R_leg_IK_switch_CTL", a=1, ro=[-7.951386703658792e-16, -1.5902773407317584e-15, -2.4848083448933712e-17])
			mc.xform("R_leg_IK_switch_CTL", r=1, s=[1.0000000000000002, 0.9999999999999999, 1.0])

		if mc.objExists("R_innerBall_CTL"):
			if not mc.getAttr("R_innerBall_CTL.mirrorMode", l=1):
				mc.setAttr("R_innerBall_CTL.mirrorMode", 0)

			if not mc.getAttr("R_innerBall_CTL.rotateOrder", l=1):
				mc.setAttr("R_innerBall_CTL.rotateOrder", 0)

			mc.xform("R_innerBall_CTL", a=1, t=[1.4991697810939897e-07, -2.6087583318568086e-07, -5.084461740523238e-09])
			mc.xform("R_innerBall_CTL", a=1, ro=[-1.7233402618615484e-34, 7.947504190619896e-16, -2.4848083448933725e-17])
			mc.xform("R_innerBall_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0])

		if mc.objExists("R_outterBall_CTL"):
			if not mc.getAttr("R_outterBall_CTL.mirrorMode", l=1):
				mc.setAttr("R_outterBall_CTL.mirrorMode", 0)

			if not mc.getAttr("R_outterBall_CTL.rotateOrder", l=1):
				mc.setAttr("R_outterBall_CTL.rotateOrder", 0)

			mc.xform("R_outterBall_CTL", a=1, t=[1.2827313955465769e-06, 3.036035065157039e-07, 1.412751911011867e-07])
			mc.xform("R_outterBall_CTL", a=1, ro=[-1.7233402618615484e-34, 7.947504190619896e-16, -2.4848083448933725e-17])
			mc.xform("R_outterBall_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, 1.0])

		if mc.objExists("R_heel_CTL"):
			if not mc.getAttr("R_heel_CTL.mirrorMode", l=1):
				mc.setAttr("R_heel_CTL.mirrorMode", 0)

			if not mc.getAttr("R_heel_CTL.rotateOrder", l=1):
				mc.setAttr("R_heel_CTL.rotateOrder", 0)

			mc.xform("R_heel_CTL", a=1, t=[5.8949441994471385e-08, -2.877812639023869e-07, 4.487607387360093e-06])
			mc.xform("R_heel_CTL", a=1, ro=[-1.7233402618615484e-34, 7.947504190619896e-16, -2.4848083448933725e-17])
			mc.xform("R_heel_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0])

		if mc.objExists("R_toeTip_CTL"):
			if not mc.getAttr("R_toeTip_CTL.mirrorMode", l=1):
				mc.setAttr("R_toeTip_CTL.mirrorMode", 0)

			if not mc.getAttr("R_toeTip_CTL.rotateOrder", l=1):
				mc.setAttr("R_toeTip_CTL.rotateOrder", 0)

			mc.xform("R_toeTip_CTL", a=1, t=[4.70356141191175e-06, 5.070140934315681e-07, -1.4205143792356267e-06])
			mc.xform("R_toeTip_CTL", a=1, ro=[-1.7233402618615484e-34, 7.947504190619896e-16, -2.4848083448933725e-17])
			mc.xform("R_toeTip_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 0.9999999999999999])

		if mc.objExists("R_reverseBall_CTL"):
			if not mc.getAttr("R_reverseBall_CTL.mirrorMode", l=1):
				mc.setAttr("R_reverseBall_CTL.mirrorMode", 0)

			if not mc.getAttr("R_reverseBall_CTL.rotateOrder", l=1):
				mc.setAttr("R_reverseBall_CTL.rotateOrder", 0)

			mc.xform("R_reverseBall_CTL", a=1, t=[1.633242978194005e-06, 2.392549853791337e-07, 5.265387552633172e-07])
			mc.xform("R_reverseBall_CTL", a=1, ro=[-1.7233402618615484e-34, 7.947504190619896e-16, -2.4848083448933725e-17])
			mc.xform("R_reverseBall_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_ankleOffset_CTL"):
			if not mc.getAttr("R_ankleOffset_CTL.mirrorMode", l=1):
				mc.setAttr("R_ankleOffset_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ankleOffset_CTL.rotateOrder", l=1):
				mc.setAttr("R_ankleOffset_CTL.rotateOrder", 0)

			mc.xform("R_ankleOffset_CTL", a=1, t=[-1.8578618734554908e-06, -1.5210988579816842e-08, -7.037576221780029e-08])
			mc.xform("R_ankleOffset_CTL", a=1, ro=[0.0, 3.106010431116715e-18, 0.0])
			mc.xform("R_ankleOffset_CTL", r=1, s=[0.9999999999999997, 0.9999999999999998, 0.9999999999999997])

		if mc.objExists("R_toe_IK_D_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_toe_IK_D_OFF_CTL", a=1, ro=[-2.5375546637307635e-09, -7.043129034797101e-26, -3.1805546814635168e-15])
			mc.xform("R_toe_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_C_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_toe_IK_C_OFF_CTL", a=1, ro=[-2.5375546637307635e-09, -7.043129034797101e-26, -3.1805546814635168e-15])
			mc.xform("R_toe_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_B_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_toe_IK_B_OFF_CTL", a=1, ro=[-2.5375546637307635e-09, -7.043129034797101e-26, -3.1805546814635168e-15])
			mc.xform("R_toe_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_A_OFF_CTL"):
			if not mc.getAttr("R_toe_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_toe_IK_A_OFF_CTL", a=1, ro=[-2.5375546637307635e-09, -7.043129034797101e-26, -3.1805546814635168e-15])
			mc.xform("R_toe_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_toe_IK_CTL"):
			if not mc.getAttr("R_toe_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_toe_IK_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_toe_IK_CTL.mirrorMode", l=1):
				mc.setAttr("R_toe_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_toe_IK_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_IK_CTL.rotateOrder", 0)

			mc.xform("R_toe_IK_CTL", a=1, t=[3.6003365833092715e-07, -1.6697857538883198e-06, -2.901033183677626e-07])
			mc.xform("R_toe_IK_CTL", a=1, ro=[-9.541664044390549e-15, 1.5902773407317578e-14, -3.1805546814635176e-15])
			mc.xform("R_toe_IK_CTL", r=1, s=[1.0, 0.9999999999999999, 1.0000000000000002])

		if mc.objExists("R_toe_FK_CTL"):
			if not mc.getAttr("R_toe_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_toe_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_toe_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_toe_FK_CTL.rotateOrder", 0)

			mc.xform("R_toe_FK_CTL", a=1, t=[0.0, -2.220446049250313e-16, 0.0])
			mc.xform("R_toe_FK_CTL", a=1, ro=[-9.541664044390549e-15, 1.5902773407317578e-14, -3.1805546814635176e-15])
			mc.xform("R_toe_FK_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_upArm_FK_CTL"):
			if not mc.getAttr("R_upArm_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_upArm_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upArm_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_upArm_FK_CTL.rotateOrder", 0)

			mc.xform("R_upArm_FK_CTL", a=1, t=[0.0, -1.7763568394002505e-15, 0.0])
			mc.xform("R_upArm_FK_CTL", a=1, ro=[-1.5902773407317584e-15, -3.975693351829396e-16, 5.517382872562698e-33])
			mc.xform("R_upArm_FK_CTL", r=1, s=[0.9999999999999994, 1.0000000000000002, 0.9999999999999998])

		if mc.objExists("R_loArm_FK_CTL"):
			if not mc.getAttr("R_loArm_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_loArm_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_loArm_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_loArm_FK_CTL.rotateOrder", 0)

			mc.xform("R_loArm_FK_CTL", a=1, t=[-8.881784197001252e-16, 0.0, 8.881784197001252e-16])
			mc.xform("R_loArm_FK_CTL", a=1, ro=[-3.1805546814635168e-15, -1.5902773407317582e-15, 6.3611093629270335e-15])
			mc.xform("R_loArm_FK_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, 1.0000000000000007])

		if mc.objExists("R_wrist_FK_CTL"):
			if not mc.getAttr("R_wrist_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_wrist_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_wrist_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_FK_CTL.rotateOrder", 0)

			mc.xform("R_wrist_FK_CTL", a=1, t=[-1.3322676295501878e-15, -7.105427357601002e-15, -1.3322676295501878e-15])
			mc.xform("R_wrist_FK_CTL", a=1, ro=[2.385416011097637e-15, 3.975693351829395e-16, 8.276074308844043e-33])
			mc.xform("R_wrist_FK_CTL", r=1, s=[0.9999999999999998, 0.9999999999999999, 0.9999999999999999])

		if mc.objExists("R_arm_IK_D_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_D_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, -2.220446049250313e-16])
			mc.xform("R_arm_IK_D_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_arm_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_C_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_C_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 4.440892098500626e-16])
			mc.xform("R_arm_IK_C_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_arm_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_B_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_B_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, -4.440892098500626e-16])
			mc.xform("R_arm_IK_B_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_arm_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_A_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_A_OFF_CTL", a=1, t=[1.7763568394002505e-15, -1.7763568394002505e-15, 0.0])
			mc.xform("R_arm_IK_A_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_arm_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_CTL"):
			if not mc.getAttr("R_arm_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_arm_IK_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("R_arm_IK_CTL.mirrorMode", l=1):
				mc.setAttr("R_arm_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_arm_IK_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_CTL", a=1, t=[-1.3322676295501878e-15, -7.105427357601002e-15, -1.3322676295501878e-15])
			mc.xform("R_arm_IK_CTL", a=1, ro=[2.385416011097637e-15, 3.975693351829395e-16, 8.276074308844043e-33])
			mc.xform("R_arm_IK_CTL", r=1, s=[0.9999999999999998, 0.9999999999999999, 0.9999999999999999])

		if mc.objExists("R_wrist_IK_D_OFF_CTL"):
			if not mc.getAttr("R_wrist_IK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_D_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, -2.220446049250313e-16])
			mc.xform("R_wrist_IK_D_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_wrist_IK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_IK_C_OFF_CTL"):
			if not mc.getAttr("R_wrist_IK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_C_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 4.440892098500626e-16])
			mc.xform("R_wrist_IK_C_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_wrist_IK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_IK_B_OFF_CTL"):
			if not mc.getAttr("R_wrist_IK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_B_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, -4.440892098500626e-16])
			mc.xform("R_wrist_IK_B_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_wrist_IK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_IK_A_OFF_CTL"):
			if not mc.getAttr("R_wrist_IK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_A_OFF_CTL", a=1, t=[1.7763568394002505e-15, -1.7763568394002505e-15, 0.0])
			mc.xform("R_wrist_IK_A_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_wrist_IK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_wrist_IK_CTL"):
			if not mc.getAttr("R_wrist_IK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_wrist_IK_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_wrist_IK_CTL.mirrorMode", l=1):
				mc.setAttr("R_wrist_IK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_wrist_IK_CTL.rotateOrder", l=1):
				mc.setAttr("R_wrist_IK_CTL.rotateOrder", 0)

			mc.xform("R_wrist_IK_CTL", a=1, t=[-1.3322676295501878e-15, -7.105427357601002e-15, -1.3322676295501878e-15])
			mc.xform("R_wrist_IK_CTL", a=1, ro=[2.385416011097637e-15, 3.975693351829395e-16, 8.276074308844043e-33])
			mc.xform("R_wrist_IK_CTL", r=1, s=[0.9999999999999998, 0.9999999999999999, 0.9999999999999999])

		if mc.objExists("R_arm_PV_CTL"):
			if not mc.getAttr("R_arm_PV_CTL.mirrorMode", l=1):
				mc.setAttr("R_arm_PV_CTL.mirrorMode", 0)

			if not mc.getAttr("R_arm_PV_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_PV_CTL.rotateOrder", 0)

			mc.xform("R_arm_PV_CTL", a=1, t=[-1.866053366583742e-05, 1.7763568394002505e-15, -4.304350248673927e-06])
			mc.xform("R_arm_PV_CTL", a=1, ro=[-169.7287398333679, -6.220613507069218, 43.63365665734055])
			mc.xform("R_arm_PV_CTL", r=1, s=[0.9999999999999997, 0.9999999999999999, 0.9999999999999997])

		if mc.objExists("R_shoulder_D_OFF_CTL"):
			if not mc.getAttr("R_shoulder_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_D_OFF_CTL", a=1, t=[0.0, 0.0, 1.1102230246251565e-16])
			mc.xform("R_shoulder_D_OFF_CTL", a=1, ro=[3.975693351829396e-16, -1.2722218725854067e-14, -4.4139062980501586e-32])
			mc.xform("R_shoulder_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_C_OFF_CTL"):
			if not mc.getAttr("R_shoulder_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_C_OFF_CTL", a=1, t=[0.0, 0.0, -1.1102230246251565e-16])
			mc.xform("R_shoulder_C_OFF_CTL", a=1, ro=[3.975693351829396e-16, -1.2722218725854067e-14, -4.4139062980501586e-32])
			mc.xform("R_shoulder_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_B_OFF_CTL"):
			if not mc.getAttr("R_shoulder_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_B_OFF_CTL", a=1, t=[0.0, 0.0, 1.1102230246251565e-16])
			mc.xform("R_shoulder_B_OFF_CTL", a=1, ro=[3.975693351829396e-16, -1.2722218725854067e-14, -4.4139062980501586e-32])
			mc.xform("R_shoulder_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_A_OFF_CTL"):
			if not mc.getAttr("R_shoulder_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_A_OFF_CTL", a=1, t=[0.0, 0.0, 2.220446049250313e-16])
			mc.xform("R_shoulder_A_OFF_CTL", a=1, ro=[3.975693351829396e-16, -1.2722218725854067e-14, -4.4139062980501586e-32])
			mc.xform("R_shoulder_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_shoulder_CTL"):
			if not mc.getAttr("R_shoulder_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_shoulder_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_shoulder_CTL.mirrorMode", l=1):
				mc.setAttr("R_shoulder_CTL.mirrorMode", 0)

			if not mc.getAttr("R_shoulder_CTL.rotateOrder", l=1):
				mc.setAttr("R_shoulder_CTL.rotateOrder", 0)

			mc.xform("R_shoulder_CTL", a=1, t=[0.0, -5.329070518200751e-15, 0.0])
			mc.xform("R_shoulder_CTL", a=1, ro=[-6.896728590703373e-34, -4.969616689786745e-17, 1.5902773407317584e-15])
			mc.xform("R_shoulder_CTL", r=1, s=[0.9999999999999997, 0.9999999999999999, 1.0000000000000002])

		if mc.objExists("R_arm_IK_switch_D_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_D_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, -2.220446049250313e-16])
			mc.xform("R_arm_IK_switch_D_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_arm_IK_switch_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_C_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_C_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, 4.440892098500626e-16])
			mc.xform("R_arm_IK_switch_C_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_arm_IK_switch_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_B_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_B_OFF_CTL", a=1, t=[-4.440892098500626e-16, 0.0, -4.440892098500626e-16])
			mc.xform("R_arm_IK_switch_B_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_arm_IK_switch_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_A_OFF_CTL"):
			if not mc.getAttr("R_arm_IK_switch_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_A_OFF_CTL", a=1, t=[1.7763568394002505e-15, -1.7763568394002505e-15, 0.0])
			mc.xform("R_arm_IK_switch_A_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_arm_IK_switch_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_arm_IK_switch_CTL"):
			if not mc.getAttr("R_arm_IK_switch_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_arm_IK_switch_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_arm_IK_switch_CTL.mirrorMode", l=1):
				mc.setAttr("R_arm_IK_switch_CTL.mirrorMode", 0)

			if not mc.getAttr("R_arm_IK_switch_CTL.rotateOrder", l=1):
				mc.setAttr("R_arm_IK_switch_CTL.rotateOrder", 0)

			mc.xform("R_arm_IK_switch_CTL", a=1, t=[-1.3322676295501878e-15, -7.105427357601002e-15, -1.3322676295501878e-15])
			mc.xform("R_arm_IK_switch_CTL", a=1, ro=[2.385416011097637e-15, 3.975693351829395e-16, 8.276074308844043e-33])
			mc.xform("R_arm_IK_switch_CTL", r=1, s=[0.9999999999999998, 0.9999999999999999, 0.9999999999999999])

		if mc.objExists("R_thumb_A_CTL"):
			if not mc.getAttr("R_thumb_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_CTL.rotateOrder", 0)

			mc.xform("R_thumb_A_CTL", a=1, t=[-1.81222775883505e-05, 3.9673030194364856e-05, -2.92159095458544e-05])
			mc.xform("R_thumb_A_CTL", a=1, ro=[-1.2722218725854067e-14, -4.174478019420865e-15, 3.1805546814635176e-15])
			mc.xform("R_thumb_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_B_CTL"):
			if not mc.getAttr("R_thumb_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_CTL.rotateOrder", 0)

			mc.xform("R_thumb_B_CTL", a=1, t=[-3.074923122969864e-05, 3.058102218922443e-05, -1.4671583887349016e-05])
			mc.xform("R_thumb_B_CTL", a=1, ro=[6.361109362927032e-15, -5.565970692561153e-15, -3.0897344086351093e-31])
			mc.xform("R_thumb_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_C_CTL"):
			if not mc.getAttr("R_thumb_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_CTL.rotateOrder", 0)

			mc.xform("R_thumb_C_CTL", a=1, t=[2.0744751804802064e-05, -2.2913255797618604e-05, 1.5680995257838504e-05])
			mc.xform("R_thumb_C_CTL", a=1, ro=[1.908332808878109e-14, -3.975693351829394e-15, 5.565970692561151e-15])
			mc.xform("R_thumb_C_CTL", r=1, s=[0.9999999999999998, 1.0, 1.0000000000000002])

		if mc.objExists("R_index_A_CTL"):
			if not mc.getAttr("R_index_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_A_CTL.rotateOrder", 0)

			mc.xform("R_index_A_CTL", a=1, t=[-2.559654645628573e-05, 5.977123495881642e-05, 7.036354437772729e-06])
			mc.xform("R_index_A_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_index_A_CTL", r=1, s=[0.9999999999999997, 0.9999999999999998, 1.0])

		if mc.objExists("R_index_B_CTL"):
			if not mc.getAttr("R_index_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_B_CTL.rotateOrder", 0)

			mc.xform("R_index_B_CTL", a=1, t=[2.463168607480526e-05, -2.2395776284156454e-05, -5.559010952671528e-06])
			mc.xform("R_index_B_CTL", a=1, ro=[2.6239576122074014e-14, -4.969616689786745e-16, -1.1379602174660566e-31])
			mc.xform("R_index_B_CTL", r=1, s=[1.0, 0.9999999999999997, 0.9999999999999998])

		if mc.objExists("R_index_C_CTL"):
			if not mc.getAttr("R_index_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_C_CTL.rotateOrder", 0)

			mc.xform("R_index_C_CTL", a=1, t=[-2.119217643503646e-05, 1.7259687588477846e-05, 3.3886863461916883e-06])
			mc.xform("R_index_C_CTL", a=1, ro=[-3.1805546814635148e-15, -6.95746336570144e-15, -6.36110936292703e-15])
			mc.xform("R_index_C_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0])

		if mc.objExists("R_index_D_CTL"):
			if not mc.getAttr("R_index_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_D_CTL.rotateOrder", 0)

			mc.xform("R_index_D_CTL", a=1, t=[-3.794329861506185e-05, 1.224275517053286e-05, 8.628378410322282e-06])
			mc.xform("R_index_D_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_index_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_A_CTL"):
			if not mc.getAttr("R_middle_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_A_CTL.rotateOrder", 0)

			mc.xform("R_middle_A_CTL", a=1, t=[-1.9536530651009798e-05, 1.8554989654973042e-05, 3.0694286019539163e-06])
			mc.xform("R_middle_A_CTL", a=1, ro=[1.059337511532038e-30, 4.770832022195275e-15, 2.5444437451708134e-14])
			mc.xform("R_middle_A_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, 1.0])

		if mc.objExists("R_middle_B_CTL"):
			if not mc.getAttr("R_middle_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_B_CTL.rotateOrder", 0)

			mc.xform("R_middle_B_CTL", a=1, t=[-2.897278703795081e-05, 1.5815812041353183e-05, 1.9378727538210683e-06])
			mc.xform("R_middle_B_CTL", a=1, ro=[4.700810207423417e-30, 2.8227422797988705e-14, 1.9083328088781097e-14])
			mc.xform("R_middle_B_CTL", r=1, s=[1.0000000000000002, 0.9999999999999999, 1.0])

		if mc.objExists("R_middle_C_CTL"):
			if not mc.getAttr("R_middle_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_C_CTL.rotateOrder", 0)

			mc.xform("R_middle_C_CTL", a=1, t=[-3.610933017128559e-05, 1.7667858656977842e-05, 4.7847535116218864e-06])
			mc.xform("R_middle_C_CTL", a=1, ro=[1.5902773407317584e-15, -7.951386703658791e-16, -6.3611093629270335e-15])
			mc.xform("R_middle_C_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, 1.0000000000000002])

		if mc.objExists("R_middle_D_CTL"):
			if not mc.getAttr("R_middle_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_D_CTL.rotateOrder", 0)

			mc.xform("R_middle_D_CTL", a=1, t=[-1.1436672835429817e-06, -1.825846975833656e-07, 5.1402829548408135e-08])
			mc.xform("R_middle_D_CTL", a=1, ro=[1.5902773407317592e-15, -3.975693351829396e-15, -1.90833280887811e-14])
			mc.xform("R_middle_D_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0])

		if mc.objExists("R_ring_A_CTL"):
			if not mc.getAttr("R_ring_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_A_CTL.rotateOrder", 0)

			mc.xform("R_ring_A_CTL", a=1, t=[-1.458816543431496e-05, 2.2010035294783847e-05, 5.7405069586735635e-06])
			mc.xform("R_ring_A_CTL", a=1, ro=[0.0, 3.975693351829396e-16, 0.0])
			mc.xform("R_ring_A_CTL", r=1, s=[1.0000000000000004, 1.0000000000000002, 0.9999999999999998])

		if mc.objExists("R_ring_B_CTL"):
			if not mc.getAttr("R_ring_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_B_CTL.rotateOrder", 0)

			mc.xform("R_ring_B_CTL", a=1, t=[-9.202116636242152e-06, 1.50169550501289e-05, 3.3998092909826028e-06])
			mc.xform("R_ring_B_CTL", a=1, ro=[-4.770832022195274e-15, 1.987846675914698e-15, 1.9083328088781097e-14])
			mc.xform("R_ring_B_CTL", r=1, s=[0.9999999999999997, 1.0, 1.0000000000000002])

		if mc.objExists("R_ring_C_CTL"):
			if not mc.getAttr("R_ring_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_C_CTL.rotateOrder", 0)

			mc.xform("R_ring_C_CTL", a=1, t=[-7.231243169592005e-05, 3.3817182384154876e-05, 1.2943318059566167e-05])
			mc.xform("R_ring_C_CTL", a=1, ro=[-3.975693351829395e-15, -4.7708320221952736e-15, 1.2722218725854064e-14])
			mc.xform("R_ring_C_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0000000000000002])

		if mc.objExists("R_ring_D_CTL"):
			if not mc.getAttr("R_ring_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_D_CTL.rotateOrder", 0)

			mc.xform("R_ring_D_CTL", a=1, t=[1.662954414705098e-05, -2.757777089357205e-06, -2.7720337869574507e-06])
			mc.xform("R_ring_D_CTL", a=1, ro=[-3.975693351829397e-15, -2.7829853462805764e-15, 1.90833280887811e-14])
			mc.xform("R_ring_D_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0000000000000002])

		if mc.objExists("R_pinky_A_CTL"):
			if not mc.getAttr("R_pinky_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_CTL.rotateOrder", 0)

			mc.xform("R_pinky_A_CTL", a=1, t=[-5.389560636004376e-05, 4.58431637753165e-05, 2.2652481945328873e-05])
			mc.xform("R_pinky_A_CTL", a=1, ro=[3.1805546814635148e-15, 2.226388277024462e-14, -1.2722218725854067e-14])
			mc.xform("R_pinky_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_B_CTL"):
			if not mc.getAttr("R_pinky_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_CTL.rotateOrder", 0)

			mc.xform("R_pinky_B_CTL", a=1, t=[3.609828654482783e-05, -1.9082479862930768e-05, 3.168995625246751e-06])
			mc.xform("R_pinky_B_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_pinky_B_CTL", r=1, s=[1.0, 0.9999999999999998, 1.0])

		if mc.objExists("R_pinky_C_CTL"):
			if not mc.getAttr("R_pinky_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_CTL.rotateOrder", 0)

			mc.xform("R_pinky_C_CTL", a=1, t=[1.7355949797348558e-05, -4.665948356574745e-07, 1.5419609047384597e-06])
			mc.xform("R_pinky_C_CTL", a=1, ro=[7.951386703658796e-16, 2.3854160110976376e-15, 1.2722218725854067e-14])
			mc.xform("R_pinky_C_CTL", r=1, s=[0.9999999999999996, 0.9999999999999996, 1.0000000000000002])

		if mc.objExists("R_pinky_D_CTL"):
			if not mc.getAttr("R_pinky_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_CTL.rotateOrder", 0)

			mc.xform("R_pinky_D_CTL", a=1, t=[5.9967784535430724e-05, -2.4924923952340805e-05, 5.600948970618802e-06])
			mc.xform("R_pinky_D_CTL", a=1, ro=[0.0, 0.0, -6.361109362927032e-15])
			mc.xform("R_pinky_D_CTL", r=1, s=[1.0000000000000002, 1.0, 0.9999999999999998])

		if mc.objExists("R_hand_CTL"):
			if not mc.getAttr("R_hand_CTL.mirrorMode", l=1):
				mc.setAttr("R_hand_CTL.mirrorMode", 0)

			if not mc.getAttr("R_hand_CTL.rotateOrder", l=1):
				mc.setAttr("R_hand_CTL.rotateOrder", 0)

			mc.xform("R_hand_CTL", a=1, t=[-6.058693744037669e-06, 6.473259750805482e-05, -2.8485941327982545e-08])
			mc.xform("R_hand_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_hand_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, 0.9999999999999997])

		# Apply contro shapes data
		data = {
			"C_cog_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_CTLShape", "degree": 1, "form": 0, "points": [[36.500891, 102.099558, 2.564846], [36.462392, 102.099558, -3.177476], [26.553836, 102.099558, -6.625375], [25.199756, 102.099558, -10.700146], [31.073793, 102.099558, -19.391523], [27.667425, 102.099558, -24.014522], [17.6231, 102.099558, -20.985949], [14.133523, 102.099558, -23.486748], [13.777607, 102.099558, -33.964608], [8.304413, 102.099558, -35.702511], [1.960935, 102.099558, -27.354229], [-2.331242, 102.099558, -27.325848], [-8.781196, 102.099558, -35.588036], [-14.230575, 102.099558, -33.776971], [-14.450246, 102.099558, -23.297795], [-17.90556, 102.099558, -20.751082], [-27.985864, 102.099558, -23.641694], [-31.329991, 102.099558, -18.973438], [-25.341917, 102.099558, -10.366036], [-26.64055, 102.099558, -6.27377], [-36.500891, 102.099558, -2.688713], [-36.462392, 102.099558, 3.05361], [-26.553836, 102.099558, 6.501509], [-25.199756, 102.099558, 10.576279], [-31.073793, 102.099558, 19.267656], [-27.667425, 102.099558, 23.890655], [-17.6231, 102.099558, 20.862082], [-14.133523, 102.099558, 23.362882], [-13.777607, 102.099558, 33.840742], [-8.304413, 102.099558, 35.578645], [-1.960935, 102.099558, 27.230363], [2.331242, 102.099558, 27.201982], [8.781196, 102.099558, 35.46417], [14.230575, 102.099558, 33.653104], [14.450246, 102.099558, 23.173929], [17.90556, 102.099558, 20.627216], [27.985864, 102.099558, 23.517828], [31.329991, 102.099558, 18.849572], [25.341917, 102.099558, 10.24217], [26.64055, 102.099558, 6.149903], [36.500891, 102.099558, 2.564846]]}]},
			"L_wrist_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[59.379903, 107.761525, -2.916249], [61.775554, 110.158951, -3.518647], [63.35213, 112.556377, -1.616955], [63.186091, 113.549421, 1.674849], [61.374705, 112.556377, 4.428469], [58.979054, 110.158951, 5.030867], [57.402478, 107.761525, 3.129175], [57.568517, 106.768481, -0.162629]]}]},
			"L_leg_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_CTLShape", "degree": 3, "form": 2, "points": [[17.949727, 6.53346, -15.113494], [12.002071, 6.53346, -19.252368], [6.023667, 6.53346, -15.158033], [3.516589, 6.53346, -5.228874], [5.949435, 6.53346, 4.718733], [11.897091, 6.53346, 8.857607], [17.875495, 6.53346, 4.763272], [20.382574, 6.53346, -5.165887]]}]},
			"L_outterBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_outterBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[25.623581, 1.427286, 3.383035], [25.632223, 1.543094, 3.486749], [25.64184, 1.439021, 3.602158], [25.633198, 1.323212, 3.498444], [25.623581, 1.427286, 3.383035], [25.742418, 1.433153, 3.483455], [25.64184, 1.439021, 3.602158], [25.522993, 1.433153, 3.501739], [25.632223, 1.543094, 3.486749], [25.742418, 1.433153, 3.483455], [25.633198, 1.323212, 3.498444], [25.522993, 1.433153, 3.501739], [25.623581, 1.427286, 3.383035], [25.742418, 1.433153, 3.483455], [15.282113, 1.433153, 4.35512]]}, {"shapeName": "L_outterBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[15.227017, 11.798998, 3.693945], [15.126429, 11.804866, 3.812649], [15.245276, 11.810733, 3.913067], [15.345864, 11.804866, 3.794363], [15.227017, 11.798998, 3.693945], [15.235659, 11.914797, 3.797659], [15.245276, 11.810733, 3.913067], [15.236634, 11.694925, 3.809353], [15.126429, 11.804866, 3.812649], [15.235659, 11.914797, 3.797659], [15.345864, 11.804866, 3.794363], [15.236634, 11.694925, 3.809353], [15.227017, 11.798998, 3.693945], [15.235659, 11.914797, 3.797659], [15.282113, 1.433153, 4.35512]]}, {"shapeName": "L_outterBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[16.142924, 2.09662, 14.685161], [16.033694, 1.986679, 14.700151], [16.143898, 1.876738, 14.696856], [16.253128, 1.986679, 14.681866], [16.142924, 2.09662, 14.685161], [16.15254, 1.992546, 14.80056], [16.143898, 1.876738, 14.696856], [16.134281, 1.980812, 14.581447], [16.033694, 1.986679, 14.700151], [16.15254, 1.992546, 14.80056], [16.253128, 1.986679, 14.681866], [16.134281, 1.980812, 14.581447], [16.142924, 2.09662, 14.685161], [16.15254, 1.992546, 14.80056], [15.282113, 1.433153, 4.35512]]}]},
			"C_torso_FK_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 111.363866, -0.660024], [-0.066058, 111.369493, -0.594206], [0.0, 111.375119, -0.528388], [0.066058, 111.369493, -0.594206], [0.0, 111.363866, -0.660024], [0.0, 111.435305, -0.599832], [0.0, 111.375119, -0.528388], [0.0, 111.303674, -0.588579], [-0.066058, 111.369493, -0.594206], [0.0, 111.435305, -0.599832], [0.066058, 111.369493, -0.594206], [0.0, 111.303674, -0.588579], [0.0, 111.363866, -0.660024], [0.0, 111.435305, -0.599832], [0.0, 105.160259, -0.06337]]}, {"shapeName": "C_torso_FK_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 105.154632, -0.129189], [-6.231884, 105.09444, -0.057743], [-6.231884, 105.165885, 0.002448], [-6.231884, 105.226077, -0.068997], [-6.231884, 105.154632, -0.129189], [-6.297936, 105.160259, -0.06337], [-6.231884, 105.165885, 0.002448], [-6.165825, 105.160259, -0.06337], [-6.231884, 105.09444, -0.057743], [-6.297936, 105.160259, -0.06337], [-6.231884, 105.226077, -0.068997], [-6.165825, 105.160259, -0.06337], [-6.231884, 105.154632, -0.129189], [-6.297936, 105.160259, -0.06337], [0.0, 105.160259, -0.06337]]}, {"shapeName": "C_torso_FK_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 105.691094, 6.145864], [0.0, 105.625276, 6.151491], [0.066058, 105.691094, 6.145864], [0.0, 105.756913, 6.140237], [-0.066058, 105.691094, 6.145864], [0.0, 105.696721, 6.211676], [0.066058, 105.691094, 6.145864], [0.0, 105.685467, 6.080045], [0.0, 105.625276, 6.151491], [0.0, 105.696721, 6.211676], [0.0, 105.756913, 6.140237], [0.0, 105.685467, 6.080045], [-0.066058, 105.691094, 6.145864], [0.0, 105.696721, 6.211676], [0.0, 105.160259, -0.06337]]}]},
			"L_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_A_CTLShape", "degree": 3, "form": 2, "points": [[61.82744, 110.101834, 1.973579], [62.289002, 110.686496, 1.761395], [62.512872, 111.353109, 2.086047], [62.367909, 111.711181, 2.75736], [61.939031, 111.550959, 3.382086], [61.477469, 110.966298, 3.59427], [61.253599, 110.299684, 3.269617], [61.398562, 109.941613, 2.598305]]}]},
			"L_toe_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toe_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[12.062575, 2.295348, 20.067304], [11.952478, 2.185461, 20.060499], [12.062575, 2.07559, 20.053437], [12.172673, 2.185477, 20.060242], [12.062575, 2.295348, 20.067304], [12.062704, 2.178536, 20.170239], [12.062575, 2.07559, 20.053437], [12.062446, 2.192403, 19.950492], [11.952478, 2.185461, 20.060499], [12.062704, 2.178536, 20.170239], [12.172673, 2.185477, 20.060242], [12.062446, 2.192403, 19.950492], [12.062575, 2.295348, 20.067304], [12.062704, 2.178536, 20.170239], [12.050417, 2.839603, 9.694524]]}, {"shapeName": "L_toe_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.663951, 2.948716, 9.713592], [1.663823, 2.845771, 9.596779], [1.663951, 2.728958, 9.699724], [1.66408, 2.831903, 9.816537], [1.663951, 2.948716, 9.713592], [1.553864, 2.838829, 9.706787], [1.663951, 2.728958, 9.699724], [1.774049, 2.838845, 9.706529], [1.663823, 2.845771, 9.596779], [1.553864, 2.838829, 9.706787], [1.66408, 2.831903, 9.816537], [1.774049, 2.838845, 9.706529], [1.663951, 2.948716, 9.713592], [1.553864, 2.838829, 9.706787], [12.050417, 2.839603, 9.694524]]}, {"shapeName": "L_toe_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[11.94032, -7.526259, 9.040518], [12.050288, -7.519317, 8.930511], [12.160514, -7.526243, 9.040261], [12.050546, -7.533185, 9.150268], [11.94032, -7.526259, 9.040518], [12.050417, -7.63612, 9.033456], [12.160514, -7.526243, 9.040261], [12.050417, -7.416372, 9.047323], [12.050288, -7.519317, 8.930511], [12.050417, -7.63612, 9.033456], [12.050546, -7.533185, 9.150268], [12.050417, -7.416372, 9.047323], [11.94032, -7.526259, 9.040518], [12.050417, -7.63612, 9.033456], [12.050417, 2.839603, 9.694524]]}]},
			"L_leg_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[17.349713, 6.53346, -14.121883], [11.996822, 6.53346, -17.846869], [6.616259, 6.53346, -14.161968], [4.359888, 6.53346, -5.225725], [6.54945, 6.53346, 3.727122], [11.90234, 6.53346, 7.452108], [17.282904, 6.53346, 3.767207], [19.539274, 6.53346, -5.169036]]}]},
			"L_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.983239, 96.210779, -3.8135], [69.066489, 96.214957, -3.771315], [69.025381, 96.200207, -3.688731], [68.942132, 96.196029, -3.730916], [68.983239, 96.210779, -3.8135], [69.011631, 96.140336, -3.759109], [69.025381, 96.200207, -3.688731], [68.996989, 96.270656, -3.743121], [69.066489, 96.214957, -3.771315], [69.011631, 96.140336, -3.759109], [68.942132, 96.196029, -3.730916], [68.996989, 96.270656, -3.743121], [68.983239, 96.210779, -3.8135], [69.011631, 96.140336, -3.759109], [68.313612, 102.352895, -2.996953]]}, {"shapeName": "L_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[74.158362, 103.251021, -4.964948], [74.172112, 103.310899, -4.894569], [74.200504, 103.24045, -4.840179], [74.186755, 103.180573, -4.910558], [74.158362, 103.251021, -4.964948], [74.241606, 103.255199, -4.922761], [74.200504, 103.24045, -4.840179], [74.117255, 103.236271, -4.882364], [74.172112, 103.310899, -4.894569], [74.241606, 103.255199, -4.922761], [74.186755, 103.180573, -4.910558], [74.117255, 103.236271, -4.882364], [74.158362, 103.251021, -4.964948], [74.241606, 103.255199, -4.922761], [68.313612, 102.352895, -2.996953]]}, {"shapeName": "L_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[70.363616, 101.863701, 2.868105], [70.294117, 101.9194, 2.896299], [70.23926, 101.844772, 2.908505], [70.308759, 101.789074, 2.880311], [70.363616, 101.863701, 2.868105], [70.322507, 101.848951, 2.950683], [70.23926, 101.844772, 2.908505], [70.280367, 101.859522, 2.825921], [70.294117, 101.9194, 2.896299], [70.322507, 101.848951, 2.950683], [70.308759, 101.789074, 2.880311], [70.280367, 101.859522, 2.825921], [70.363616, 101.863701, 2.868105], [70.322507, 101.848951, 2.950683], [68.313612, 102.352895, -2.996953]]}]},
			"C_head_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_CTLShape", "degree": 3, "form": 2, "points": [[11.926143, 181.009273, -0.32106], [0.0, 185.949232, -0.32106], [-11.926143, 181.009273, -0.32106], [-16.866103, 169.08313, -0.32106], [-11.926143, 157.156987, -0.32106], [0.0, 152.217027, -0.32106], [11.926143, 157.156987, -0.32106], [16.866103, 169.08313, -0.32106]]}]},
			"world_A_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -519.93], [230.985, 0.0, -288.72], [173.16, 0.0, -288.72], [173.16, 0.0, -173.115], [288.765, 0.0, -173.115], [288.765, 0.0, -230.94], [519.93, 0.0, 0.0], [288.72, 0.0, 230.985], [288.72, 0.0, 173.16], [173.115, 0.0, 173.16], [173.115, 0.0, 288.765], [230.94, 0.0, 288.765], [0.0, 0.0, 519.93], [-230.985, 0.0, 288.72], [-173.16, 0.0, 288.72], [-173.16, 0.0, 173.115], [-288.765, 0.0, 173.115], [-288.765, 0.0, 230.94], [-519.93, 0.0, 0.0], [-288.72, 0.0, -230.985], [-288.72, 0.0, -173.16], [-173.115, 0.0, -173.16], [-173.115, 0.0, -288.765], [-230.94, 0.0, -288.765], [0.0, 0.0, -519.93], [45.27, 0.63, -475.47], [41.31, 0.0, -471.24], [41.31, 0.0, -453.96], [37.71, 0.0, -453.96], [37.935, 0.0, -471.375], [35.37, 0.0, -470.07], [35.46, 0.0, -462.51], [31.815, 0.0, -462.51], [31.815, 0.0, -470.07], [29.565, 0.0, -471.375], [29.565, 0.0, -453.69], [25.92, 0.0, -453.69], [25.92, 0.0, -471.825], [28.845, 0.0, -474.75], [33.345, 0.0, -472.5], [38.295, 0.0, -474.75], [41.31, 0.0, -471.33], [38.295, 0.0, -474.75], [33.39, 0.0, -472.545], [28.845, 0.0, -474.705], [20.07, 0.0, -474.75], [23.04, 0.0, -471.825], [23.04, 0.0, -456.66], [20.07, 0.0, -453.69], [10.575, 0.0, -453.69], [7.65, 0.0, -456.66], [7.65, 0.0, -471.825], [10.575, 0.0, -474.75], [20.07, 0.0, -474.75], [18.945, 0.0, -471.375], [19.395, 0.0, -457.425], [11.25, 0.0, -457.515], [11.295, 0.0, -471.375], [18.99, 0.0, -471.465], [20.07, 0.0, -474.75], [10.575, 0.0, -474.75], [4.5, 0.0, -474.75], [4.725, 0.0, -453.69], [-5.535, 0.0, -453.69], [-8.505, 0.0, -456.66], [-8.505, 0.0, -463.005], [-5.49, 0.0, -465.93], [-5.31, 0.0, -466.155], [-11.205, 0.0, -474.66], [-11.205, 0.0, -474.75], [-6.975, 0.0, -474.75], [-1.08, 0.0, -466.2], [1.125, 0.0, -466.2], [1.125, 0.0, -457.2], [-4.545, 0.0, -457.2], [-4.59, 0.0, -462.555], [1.125, 0.0, -462.555], [1.125, 0.0, -474.75], [4.5, 0.0, -474.75], [-28.935, 0.0, -474.75], [-28.935, 0.0, -471.375], [-17.145, 0.0, -471.33], [-17.145, 0.0, -453.69], [-13.5, 0.0, -453.69], [-13.5, 0.0, -474.75], [-44.28, 0.0, -474.75], [-46.98, 0.0, -471.825], [-47.205, 0.0, -456.66], [-44.28, 0.0, -453.69], [-31.815, 0.0, -453.69], [-31.815, 0.0, -474.75], [-35.505, 0.0, -471.375], [-35.415, 0.0, -457.11], [-43.11, 0.0, -457.11], [-43.02, 0.0, -471.285], [-35.37, 0.0, -471.465], [-31.725, 0.0, -474.75]]}]},
			"C_cog_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_cog_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.231884, 102.099558, -0.127992], [6.231884, 102.165616, -0.061933], [6.231884, 102.099558, 0.004125], [6.231884, 102.033499, -0.061933], [6.231884, 102.099558, -0.127992], [6.297936, 102.099558, -0.061933], [6.231884, 102.099558, 0.004125], [6.165825, 102.099558, -0.061933], [6.231884, 102.165616, -0.061933], [6.297936, 102.099558, -0.061933], [6.231884, 102.033499, -0.061933], [6.165825, 102.099558, -0.061933], [6.231884, 102.099558, -0.127992], [6.297936, 102.099558, -0.061933], [0.0, 102.099558, -0.061933]]}, {"shapeName": "C_cog_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 108.331442, -0.127992], [-0.066058, 108.331442, -0.061933], [0.0, 108.331442, 0.004125], [0.066058, 108.331442, -0.061933], [0.0, 108.331442, -0.127992], [0.0, 108.397494, -0.061933], [0.0, 108.331442, 0.004125], [0.0, 108.265383, -0.061933], [-0.066058, 108.331442, -0.061933], [0.0, 108.397494, -0.061933], [0.066058, 108.331442, -0.061933], [0.0, 108.265383, -0.061933], [0.0, 108.331442, -0.127992], [0.0, 108.397494, -0.061933], [0.0, 102.099558, -0.061933]]}, {"shapeName": "C_cog_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 102.165616, 6.16995], [-0.066058, 102.099558, 6.16995], [0.0, 102.033499, 6.16995], [0.066058, 102.099558, 6.16995], [0.0, 102.165616, 6.16995], [0.0, 102.099558, 6.236003], [0.0, 102.033499, 6.16995], [0.0, 102.099558, 6.103892], [-0.066058, 102.099558, 6.16995], [0.0, 102.099558, 6.236003], [0.066058, 102.099558, 6.16995], [0.0, 102.099558, 6.103892], [0.0, 102.165616, 6.16995], [0.0, 102.099558, 6.236003], [0.0, 102.099558, -0.061933]]}]},
			"L_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_C_CTLShape", "degree": 3, "form": 2, "points": [[71.00353, 102.974151, 2.993596], [71.703102, 103.178813, 2.731675], [72.338665, 103.486385, 3.050028], [72.537915, 103.716695, 3.76217], [72.184135, 103.734832, 4.450938], [71.484563, 103.53017, 4.712859], [70.849, 103.222598, 4.394506], [70.64975, 102.992287, 3.682364]]}]},
			"L_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[72.301638, 95.846809, 10.278704], [72.335304, 95.878606, 10.359839], [72.249949, 95.873104, 10.397412], [72.216283, 95.841307, 10.316277], [72.301638, 95.846809, 10.278704], [72.288215, 95.79797, 10.357197], [72.249949, 95.873104, 10.397412], [72.263372, 95.921949, 10.318918], [72.335304, 95.878606, 10.359839], [72.288215, 95.79797, 10.357197], [72.216283, 95.841307, 10.316277], [72.263372, 95.921949, 10.318918], [72.301638, 95.846809, 10.278704], [72.288215, 95.79797, 10.357197], [71.103903, 101.708248, 8.532365]]}, {"shapeName": "L_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[76.743894, 103.454506, 10.527815], [76.705628, 103.529645, 10.568029], [76.692206, 103.4808, 10.646524], [76.730472, 103.405661, 10.60631], [76.743894, 103.454506, 10.527815], [76.777555, 103.486301, 10.608949], [76.692206, 103.4808, 10.646524], [76.65854, 103.449003, 10.565389], [76.705628, 103.529645, 10.568029], [76.777555, 103.486301, 10.608949], [76.730472, 103.405661, 10.60631], [76.65854, 103.449003, 10.565389], [76.743894, 103.454506, 10.527815], [76.777555, 103.486301, 10.608949], [71.103903, 101.708248, 8.532365]]}, {"shapeName": "L_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[68.725299, 102.9672, 14.153576], [68.653367, 103.010543, 14.112655], [68.606278, 102.929901, 14.110014], [68.678211, 102.886558, 14.150936], [68.725299, 102.9672, 14.153576], [68.639947, 102.961697, 14.191144], [68.606278, 102.929901, 14.110014], [68.691633, 102.935403, 14.072441], [68.653367, 103.010543, 14.112655], [68.639947, 102.961697, 14.191144], [68.678211, 102.886558, 14.150936], [68.691633, 102.935403, 14.072441], [68.725299, 102.9672, 14.153576], [68.639947, 102.961697, 14.191144], [71.103903, 101.708248, 8.532365]]}]},
			"R_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_D_CTLShape", "degree": 3, "form": 2, "points": [[-70.739219, 101.36381, 7.653476], [-71.499817, 101.506841, 7.6231], [-72.028494, 101.767854, 8.125357], [-72.015558, 101.99395, 8.866035], [-71.468587, 102.052686, 9.411253], [-70.707989, 101.909655, 9.44163], [-70.179312, 101.648643, 8.939372], [-70.192248, 101.422547, 8.198695]]}]},
			"R_arm_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-45.128164, 151.783452, 92.689591], [-45.19176, 151.840876, 92.559588], [-45.104305, 151.744421, 92.474201], [-45.04071, 151.686996, 92.604205], [-45.128164, 151.783452, 92.689591], [-45.037027, 151.840223, 92.576846], [-45.104305, 151.744421, 92.474201], [-45.19545, 151.687642, 92.586947], [-45.19176, 151.840876, 92.559588], [-45.037027, 151.840223, 92.576846], [-45.04071, 151.686996, 92.604205], [-45.19545, 151.687642, 92.586947], [-45.128164, 151.783452, 92.689591], [-45.037027, 151.840223, 92.576846], [-52.589355, 144.566418, 93.05835]]}, {"shapeName": "R_arm_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-59.726217, 151.844371, 91.061468], [-59.793503, 151.748561, 90.958823], [-59.702358, 151.805338, 90.846077], [-59.635072, 151.901149, 90.948722], [-59.726217, 151.844371, 91.061468], [-59.789805, 151.901787, 90.931466], [-59.702358, 151.805338, 90.846077], [-59.638762, 151.747915, 90.976081], [-59.793503, 151.748561, 90.958823], [-59.789805, 151.901787, 90.931466], [-59.635072, 151.901149, 90.948722], [-59.638762, 151.747915, 90.976081], [-59.726217, 151.844371, 91.061468], [-59.789805, 151.901787, 90.931466], [-52.589355, 144.566418, 93.05835]]}, {"shapeName": "R_arm_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-51.539433, 142.802264, 82.876191], [-51.543124, 142.649029, 82.903551], [-51.388383, 142.648384, 82.920809], [-51.384692, 142.801619, 82.89345], [-51.539433, 142.802264, 82.876191], [-51.451979, 142.70581, 82.790815], [-51.388383, 142.648384, 82.920809], [-51.475838, 142.744839, 83.006195], [-51.543124, 142.649029, 82.903551], [-51.451979, 142.70581, 82.790815], [-51.384692, 142.801619, 82.89345], [-51.475838, 142.744839, 83.006195], [-51.539433, 142.802264, 82.876191], [-51.451979, 142.70581, 82.790815], [-52.589355, 144.566418, 93.05835]]}]},
			"R_arm_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.853237, 103.334378, 3.08561], [-67.887766, 103.417374, 3.212742], [-67.784782, 103.334378, 3.294894], [-67.750253, 103.251383, 3.167762], [-67.853237, 103.334378, 3.08561], [-67.897885, 103.262044, 3.216052], [-67.784782, 103.334378, 3.294894], [-67.740127, 103.406719, 3.16445], [-67.887766, 103.417374, 3.212742], [-67.897885, 103.262044, 3.216052], [-67.750253, 103.251383, 3.167762], [-67.740127, 103.406719, 3.16445], [-67.853237, 103.334378, 3.08561], [-67.897885, 103.262044, 3.216052], [-60.377304, 110.158951, 0.75611]]}, {"shapeName": "R_arm_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-66.897928, 117.988639, 2.773133], [-66.784817, 118.06098, 2.851973], [-66.829472, 117.988639, 2.982417], [-66.942582, 117.916298, 2.903577], [-66.897928, 117.988639, 2.773133], [-66.93245, 118.071627, 2.900263], [-66.829472, 117.988639, 2.982417], [-66.794943, 117.905644, 2.855285], [-66.784817, 118.06098, 2.851973], [-66.93245, 118.071627, 2.900263], [-66.942582, 117.916298, 2.903577], [-66.794943, 117.905644, 2.855285], [-66.897928, 117.988639, 2.773133], [-66.93245, 118.071627, 2.900263], [-60.377304, 110.158951, 0.75611]]}, {"shapeName": "R_arm_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-57.21705, 110.241946, 10.650393], [-57.069411, 110.231292, 10.602101], [-57.079537, 110.075955, 10.605414], [-57.227176, 110.08661, 10.653706], [-57.21705, 110.241946, 10.650393], [-57.114069, 110.158951, 10.732536], [-57.079537, 110.075955, 10.605414], [-57.182521, 110.158951, 10.523262], [-57.069411, 110.231292, 10.602101], [-57.114069, 110.158951, 10.732536], [-57.227176, 110.08661, 10.653706], [-57.182521, 110.158951, 10.523262], [-57.21705, 110.241946, 10.650393], [-57.114069, 110.158951, 10.732536], [-60.377304, 110.158951, 0.75611]]}]},
			"R_ankleOffset_CTL": {"color": 20, "shapes": [{"shapeName": "R_ankleOffset_CTLShape", "degree": 1, "form": 0, "points": [[-11.950418, 3.797464, -5.744851], [-11.960498, 10.26143, -2.561292], [-11.956712, 11.675668, -2.80391], [-12.977532, 11.091473, -1.981966], [-11.965349, 11.918306, -1.389696], [-11.956712, 11.675668, -2.80391], [-10.948315, 11.088263, -1.969022], [-11.960498, 10.26143, -2.561292], [-11.969135, 10.504068, -1.147078], [-10.948315, 11.088263, -1.969022], [-11.965349, 11.918306, -1.389696], [-11.969135, 10.504068, -1.147078], [-12.977532, 11.091473, -1.981966], [-11.960498, 10.26143, -2.561292]]}]},
			"L_toeTip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toeTip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[22.399514, 2.423267, 15.226996], [22.408157, 2.539075, 15.330711], [22.417774, 2.435002, 15.446119], [22.409131, 2.319193, 15.342405], [22.399514, 2.423267, 15.226996], [22.518351, 2.429134, 15.327416], [22.417774, 2.435002, 15.446119], [22.298927, 2.429134, 15.345701], [22.408157, 2.539075, 15.330711], [22.518351, 2.429134, 15.327416], [22.409131, 2.319193, 15.342405], [22.298927, 2.429134, 15.345701], [22.399514, 2.423267, 15.226996], [22.518351, 2.429134, 15.327416], [12.058046, 2.429134, 16.199081]]}, {"shapeName": "L_toeTip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[12.00295, 12.79498, 15.537906], [11.902363, 12.800847, 15.65661], [12.02121, 12.806714, 15.757028], [12.121797, 12.800847, 15.638324], [12.00295, 12.79498, 15.537906], [12.011593, 12.910778, 15.641621], [12.02121, 12.806714, 15.757028], [12.012567, 12.690906, 15.653314], [11.902363, 12.800847, 15.65661], [12.011593, 12.910778, 15.641621], [12.121797, 12.800847, 15.638324], [12.012567, 12.690906, 15.653314], [12.00295, 12.79498, 15.537906], [12.011593, 12.910778, 15.641621], [12.058046, 2.429134, 16.199081]]}, {"shapeName": "L_toeTip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[12.918857, 3.092602, 26.529123], [12.809627, 2.982661, 26.544113], [12.919832, 2.872719, 26.540817], [13.029062, 2.982661, 26.525827], [12.918857, 3.092602, 26.529123], [12.928473, 2.988527, 26.644521], [12.919832, 2.872719, 26.540817], [12.910214, 2.976793, 26.425409], [12.809627, 2.982661, 26.544113], [12.928473, 2.988527, 26.644521], [13.029062, 2.982661, 26.525827], [12.910214, 2.976793, 26.425409], [12.918857, 3.092602, 26.529123], [12.928473, 2.988527, 26.644521], [12.058046, 2.429134, 16.199081]]}]},
			"L_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[73.490414, 93.759648, 0.353049], [73.56392, 93.783365, 0.405602], [73.513048, 93.76997, 0.482803], [73.439542, 93.746252, 0.430251], [73.490414, 93.759648, 0.353049], [73.520917, 93.701626, 0.419605], [73.513048, 93.76997, 0.482803], [73.482544, 93.827997, 0.416247], [73.56392, 93.783365, 0.405602], [73.520917, 93.701626, 0.419605], [73.439542, 93.746252, 0.430251], [73.482544, 93.827997, 0.416247], [73.490414, 93.759648, 0.353049], [73.520917, 93.701626, 0.419605], [71.691597, 99.725906, 0.259492]]}, {"shapeName": "L_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[77.547129, 101.471359, -0.968059], [77.539258, 101.539708, -0.904861], [77.569763, 101.481681, -0.838305], [77.577633, 101.413332, -0.901502], [77.547129, 101.471359, -0.968059], [77.620629, 101.495075, -0.915505], [77.569763, 101.481681, -0.838305], [77.496257, 101.457963, -0.890857], [77.539258, 101.539708, -0.904861], [77.620629, 101.495075, -0.915505], [77.577633, 101.413332, -0.901502], [77.496257, 101.457963, -0.890857], [77.547129, 101.471359, -0.968059], [77.620629, 101.495075, -0.915505], [71.691597, 99.725906, 0.259492]]}, {"shapeName": "L_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[72.821434, 100.231331, 6.367581], [72.740057, 100.275962, 6.378226], [72.697056, 100.194218, 6.39223], [72.778433, 100.149586, 6.381585], [72.821434, 100.231331, 6.367581], [72.770561, 100.217935, 6.444777], [72.697056, 100.194218, 6.39223], [72.747928, 100.207613, 6.315029], [72.740057, 100.275962, 6.378226], [72.770561, 100.217935, 6.444777], [72.778433, 100.149586, 6.381585], [72.747928, 100.207613, 6.315029], [72.821434, 100.231331, 6.367581], [72.770561, 100.217935, 6.444777], [71.691597, 99.725906, 0.259492]]}]},
			"C_midNeck_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[10.01796, 163.383551, -9.503399], [0.0, 163.840676, -12.931023], [-10.01796, 163.383551, -9.503399], [-14.167526, 162.279953, -1.228365], [-10.01796, 161.176355, 7.046669], [0.0, 160.71923, 10.474293], [10.01796, 161.176355, 7.046669], [14.167526, 162.279953, -1.228365]]}]},
			"R_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-71.363731, 101.576368, 0.02507], [-71.423563, 101.624416, 0.078352], [-71.384376, 101.588185, 0.155028], [-71.324545, 101.540136, 0.101746], [-71.363731, 101.576368, 0.02507], [-71.416547, 101.531753, 0.087893], [-71.384376, 101.588185, 0.155028], [-71.331556, 101.632804, 0.092206], [-71.423563, 101.624416, 0.078352], [-71.416547, 101.531753, 0.087893], [-71.324545, 101.540136, 0.101746], [-71.331556, 101.632804, 0.092206], [-71.363731, 101.576368, 0.02507], [-71.416547, 101.531753, 0.087893], [-67.3649, 106.349, 0.293512]]}, {"shapeName": "R_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-72.025201, 110.318519, -0.874927], [-71.993026, 110.374955, -0.807791], [-72.045846, 110.330336, -0.744969], [-72.078021, 110.2739, -0.812105], [-72.025201, 110.318519, -0.874927], [-72.085028, 110.366563, -0.821644], [-72.045846, 110.330336, -0.744969], [-71.986014, 110.282288, -0.798251], [-71.993026, 110.374955, -0.807791], [-72.085028, 110.366563, -0.821644], [-72.078021, 110.2739, -0.812105], [-71.986014, 110.282288, -0.798251], [-72.025201, 110.318519, -0.874927], [-72.085028, 110.366563, -0.821644], [-67.3649, 106.349, 0.293512]]}, {"shapeName": "R_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-68.38823, 106.948539, 6.411852], [-68.296224, 106.956927, 6.425706], [-68.289212, 106.864259, 6.435246], [-68.381219, 106.855871, 6.421392], [-68.38823, 106.948539, 6.411852], [-68.349043, 106.912307, 6.488522], [-68.289212, 106.864259, 6.435246], [-68.328399, 106.90049, 6.35857], [-68.296224, 106.956927, 6.425706], [-68.349043, 106.912307, 6.488522], [-68.381219, 106.855871, 6.421392], [-68.328399, 106.90049, 6.35857], [-68.38823, 106.948539, 6.411852], [-68.349043, 106.912307, 6.488522], [-67.3649, 106.349, 0.293512]]}]},
			"R_leg_IK_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-16.749698, 6.53346, -13.130272], [-11.991573, 6.53346, -16.44137], [-7.20885, 6.53346, -13.165903], [-5.203187, 6.53346, -5.222576], [-7.149464, 6.53346, 2.73551], [-11.907589, 6.53346, 6.046609], [-16.690312, 6.53346, 2.771142], [-18.695975, 6.53346, -5.172185]]}]},
			"R_upLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-9.925836, 84.356899, 0.648821], [-9.816067, 84.358734, 0.538412], [-9.926418, 84.366231, 0.428825], [-10.036187, 84.364396, 0.539234], [-9.925836, 84.356899, 0.648821], [-9.928973, 84.251613, 0.534167], [-9.926418, 84.366231, 0.428825], [-9.923281, 84.471527, 0.54348], [-9.816067, 84.358734, 0.538412], [-9.928973, 84.251613, 0.534167], [-10.036187, 84.364396, 0.539234], [-9.923281, 84.471527, 0.54348], [-9.925836, 84.356899, 0.648821], [-9.928973, 84.251613, 0.534167], [-9.657635, 94.735269, 0.978146]]}, {"shapeName": "R_upLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.725621, 94.463514, 1.049368], [0.728176, 94.578142, 0.944026], [0.725039, 94.472846, 0.829371], [0.722484, 94.358218, 0.934713], [0.725621, 94.463514, 1.049368], [0.83538, 94.465349, 0.938958], [0.725039, 94.472846, 0.829371], [0.61527, 94.471011, 0.939781], [0.728176, 94.578142, 0.944026], [0.83538, 94.465349, 0.938958], [0.722484, 94.358218, 0.934713], [0.61527, 94.471011, 0.939781], [0.725621, 94.463514, 1.049368], [0.83538, 94.465349, 0.938958], [-9.657635, 94.735269, 0.978146]]}, {"shapeName": "R_upLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.575007, 95.172614, -9.39937], [-9.682221, 95.285408, -9.394302], [-9.795127, 95.178277, -9.398548], [-9.687913, 95.065483, -9.403616], [-9.575007, 95.172614, -9.39937], [-9.685358, 95.180111, -9.508947], [-9.795127, 95.178277, -9.398548], [-9.684776, 95.170779, -9.288961], [-9.682221, 95.285408, -9.394302], [-9.685358, 95.180111, -9.508947], [-9.687913, 95.065483, -9.403616], [-9.684776, 95.170779, -9.288961], [-9.575007, 95.172614, -9.39937], [-9.685358, 95.180111, -9.508947], [-9.657635, 94.735269, 0.978146]]}]},
			"C_neckBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neckBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.386473, 155.499078, -2.243768], [10.386473, 155.593655, -2.120082], [10.386473, 155.469969, -2.025505], [10.386473, 155.375392, -2.149191], [10.386473, 155.499078, -2.243768], [10.49656, 155.484523, -2.134636], [10.386473, 155.469969, -2.025505], [10.276375, 155.484523, -2.134636], [10.386473, 155.593655, -2.120082], [10.49656, 155.484523, -2.134636], [10.386473, 155.375392, -2.149191], [10.276375, 155.484523, -2.134636], [10.386473, 155.499078, -2.243768], [10.49656, 155.484523, -2.134636], [0.0, 155.484523, -2.134636]]}, {"shapeName": "C_neckBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 165.794397, -0.870734], [-0.110097, 165.779842, -0.761603], [0.0, 165.765288, -0.652472], [0.110097, 165.779842, -0.761603], [0.0, 165.794397, -0.870734], [0.0, 165.888964, -0.74705], [0.0, 165.765288, -0.652472], [0.0, 165.670711, -0.776157], [-0.110097, 165.779842, -0.761603], [0.0, 165.888964, -0.74705], [0.110097, 165.779842, -0.761603], [0.0, 165.670711, -0.776157], [0.0, 165.794397, -0.870734], [0.0, 165.888964, -0.74705], [0.0, 155.484523, -2.134636]]}, {"shapeName": "C_neckBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 154.220621, 8.175237], [-0.110097, 154.11149, 8.160683], [0.0, 154.002359, 8.146128], [0.110097, 154.11149, 8.160683], [0.0, 154.220621, 8.175237], [0.0, 154.096937, 8.269804], [0.0, 154.002359, 8.146128], [0.0, 154.126044, 8.051551], [-0.110097, 154.11149, 8.160683], [0.0, 154.096937, 8.269804], [0.110097, 154.11149, 8.160683], [0.0, 154.126044, 8.051551], [0.0, 154.220621, 8.175237], [0.0, 154.096937, 8.269804], [0.0, 155.484523, -2.134636]]}]},
			"C_chest_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_chest_FK_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 135.501559, -8.729957], [0.0, 135.735623, -8.77039], [0.0, 135.936398, -8.897323], [0.0, 136.073322, -9.091422], [0.0, 136.12554, -9.323142], [0.0, 136.085107, -9.557207], [0.0, 135.958174, -9.757982], [0.0, 135.764075, -9.894906], [0.0, 135.532355, -9.947124], [0.0, 135.29829, -9.906691], [0.0, 135.097515, -9.779757], [0.0, 134.960591, -9.585659], [0.0, 134.908373, -9.353938], [0.0, 134.948806, -9.119874], [0.0, 135.07574, -8.919099], [0.0, 135.269838, -8.782175], [0.0, 135.501559, -8.729957], [0.0, 135.34758, -2.644125]]}]},
			"L_shoulder_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [3.967055, 148.929805, 5.663568], [6.030708, 149.398422, 4.452699], [6.818955, 149.577418, 3.990187], [3.129693, 149.398422, -0.491427], [-0.726888, 148.929805, -2.336198], [-3.277716, 148.35056, -0.839475], [-3.548441, 147.881943, 3.427035], [-1.435673, 147.702947, 8.833673], [-0.647426, 147.881943, 8.371161], [1.416227, 148.35056, 7.160291], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193]]}]},
			"L_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[73.741716, 97.625443, 4.907738], [73.79621, 97.660555, 4.975006], [73.72745, 97.648379, 5.037065], [73.672955, 97.613267, 4.969797], [73.741716, 97.625443, 4.907738], [73.757273, 97.57631, 4.985652], [73.72745, 97.648379, 5.037065], [73.711891, 97.697518, 4.95915], [73.79621, 97.660555, 4.975006], [73.757273, 97.57631, 4.985652], [73.672955, 97.613267, 4.969797], [73.711891, 97.697518, 4.95915], [73.741716, 97.625443, 4.907738], [73.757273, 97.57631, 4.985652], [71.593832, 103.354491, 3.722267]]}, {"shapeName": "L_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[77.414808, 105.573545, 3.903337], [77.384983, 105.645619, 3.954748], [77.400542, 105.59648, 4.032663], [77.430367, 105.524406, 3.981252], [77.414808, 105.573545, 3.903337], [77.469296, 105.608654, 3.970605], [77.400542, 105.59648, 4.032663], [77.346047, 105.561369, 3.965395], [77.384983, 105.645619, 3.954748], [77.469296, 105.608654, 3.970605], [77.430367, 105.524406, 3.981252], [77.346047, 105.561369, 3.965395], [77.414808, 105.573545, 3.903337], [77.469296, 105.608654, 3.970605], [71.593832, 103.354491, 3.722267]]}, {"shapeName": "L_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[70.982557, 104.459996, 9.82513], [70.898238, 104.496959, 9.809274], [70.859303, 104.412709, 9.819921], [70.943622, 104.375745, 9.835777], [70.982557, 104.459996, 9.82513], [70.913798, 104.447819, 9.887183], [70.859303, 104.412709, 9.819921], [70.928063, 104.424884, 9.757862], [70.898238, 104.496959, 9.809274], [70.913798, 104.447819, 9.887183], [70.943622, 104.375745, 9.835777], [70.928063, 104.424884, 9.757862], [70.982557, 104.459996, 9.82513], [70.913798, 104.447819, 9.887183], [71.593832, 103.354491, 3.722267]]}]},
			"R_leg_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[-19.849085, 7.924901, -5.04975], [-19.526186, 7.916595, -5.050956], [-19.473639, 7.585309, -5.083953], [-19.246655, 7.484804, -5.094212], [-18.964145, 7.667779, -5.076354], [-18.741747, 7.434698, -5.099787], [-18.939995, 7.163454, -5.12652], [-18.850925, 6.932651, -5.14957], [-18.521145, 6.863276, -5.156855], [-18.52953, 6.54195, -5.18879], [-18.862486, 6.489622, -5.1936], [-18.963473, 6.26374, -5.215938], [-18.779639, 5.982636, -5.2441], [-19.013894, 5.761302, -5.265828], [-19.286483, 5.958557, -5.245897], [-19.518403, 5.869856, -5.254442], [-19.588159, 5.541716, -5.286982], [-19.911057, 5.550022, -5.285776], [-19.963635, 5.881309, -5.25278], [-20.190618, 5.981815, -5.242521], [-20.473129, 5.798839, -5.260378], [-20.695506, 6.031919, -5.236945], [-20.497278, 6.303195, -5.210209], [-20.586349, 6.533967, -5.187162], [-20.916098, 6.603342, -5.179877], [-20.907713, 6.924667, -5.147942], [-20.574788, 6.976996, -5.143132], [-20.4738, 7.202909, -5.120792], [-20.657615, 7.483981, -5.092632], [-20.42338, 7.705316, -5.070904], [-20.150791, 7.508061, -5.090835], [-19.91887, 7.596762, -5.08229], [-19.849085, 7.924901, -5.04975]]}, {"shapeName": "R_leg_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[-20.060012, 7.091104, -5.132394], [-20.214299, 6.746059, -5.166515], [-20.078215, 6.393545, -5.201721], [-19.731497, 6.240086, -5.217385], [-19.377261, 6.375514, -5.204338], [-19.222975, 6.720559, -5.170217], [-19.359059, 7.073073, -5.135012], [-19.705756, 7.226531, -5.119348]]}, {"shapeName": "R_leg_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[-18.525338, 6.702613, -5.172823], [-11.949581, 6.53346, -5.197381]]}]},
			"R_arm_IK_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-59.232786, 114.167263, 3.370826], [-55.684399, 109.884026, 2.210167], [-57.450831, 109.884026, -3.190205], [-60.999219, 114.167263, -2.029546], [-65.070209, 110.433876, -0.697947], [-61.521822, 106.150638, -1.858606], [-59.755389, 106.150638, 3.541766], [-63.303777, 110.433876, 4.702425], [-59.232786, 114.167263, 3.370826], [-60.999219, 114.167263, -2.029546], [-57.450831, 109.884026, -3.190205], [-61.521822, 106.150638, -1.858606], [-65.070209, 110.433876, -0.697947], [-63.303777, 110.433876, 4.702425], [-59.755389, 106.150638, 3.541766], [-55.684399, 109.884026, 2.210167]]}]},
			"L_ankleOffset_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ankleOffset_PIV_CTLShape", "degree": 1, "form": 0, "points": [[22.335182, 6.525811, -5.371061], [22.335506, 6.657324, -5.287712], [22.336477, 6.573975, -5.156202], [22.336153, 6.442462, -5.239551], [22.335182, 6.525811, -5.371061], [22.445914, 6.550067, -5.264334], [22.336477, 6.573975, -5.156202], [22.225734, 6.549719, -5.262929], [22.335506, 6.657324, -5.287712], [22.445914, 6.550067, -5.264334], [22.336153, 6.442462, -5.239551], [22.225734, 6.549719, -5.262929], [22.335182, 6.525811, -5.371061], [22.445914, 6.550067, -5.264334], [11.949581, 6.53346, -5.197381]]}, {"shapeName": "L_ankleOffset_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[11.918408, 16.644328, -7.576519], [11.80896, 16.668236, -7.468387], [11.919702, 16.692492, -7.36166], [12.02915, 16.668584, -7.469792], [11.918408, 16.644328, -7.576519], [11.918731, 16.775832, -7.493168], [11.919702, 16.692492, -7.36166], [11.919379, 16.560979, -7.445009], [11.80896, 16.668236, -7.468387], [11.918731, 16.775832, -7.493168], [12.02915, 16.668584, -7.469792], [11.919379, 16.560979, -7.445009], [11.918408, 16.644328, -7.576519], [11.918731, 16.775832, -7.493168], [11.949581, 6.53346, -5.197381]]}, {"shapeName": "L_ankleOffset_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[12.01031, 8.912746, 4.913319], [11.900538, 8.80514, 4.938102], [12.010957, 8.697883, 4.96148], [12.120729, 8.805489, 4.936697], [12.01031, 8.912746, 4.913319], [12.011281, 8.829394, 5.044819], [12.010957, 8.697883, 4.96148], [12.009986, 8.781233, 4.82997], [11.900538, 8.80514, 4.938102], [12.011281, 8.829394, 5.044819], [12.120729, 8.805489, 4.936697], [12.009986, 8.781233, 4.82997], [12.01031, 8.912746, 4.913319], [12.011281, 8.829394, 5.044819], [11.949581, 6.53346, -5.197381]]}]},
			"L_shoulder_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_shoulder_PIV_CTLShape", "degree": 1, "form": 0, "points": [[11.427124, 150.636498, 1.158646], [11.464591, 150.744543, 1.264313], [11.538559, 150.636498, 1.348562], [11.501093, 150.528453, 1.242895], [11.427124, 150.636498, 1.158646], [11.576021, 150.657657, 1.198931], [11.538559, 150.636498, 1.348562], [11.389654, 150.615337, 1.308283], [11.464591, 150.744543, 1.264313], [11.576021, 150.657657, 1.198931], [11.501093, 150.528453, 1.242895], [11.389654, 150.615337, 1.308283], [11.427124, 150.636498, 1.158646], [11.576021, 150.657657, 1.198931], [2.691641, 148.640182, 6.41193]]}, {"shapeName": "L_shoulder_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.914122, 158.833, 7.327256], [0.876652, 158.811839, 7.476893], [1.025557, 158.833, 7.517172], [1.063027, 158.854162, 7.367535], [0.914122, 158.833, 7.327256], [0.95159, 158.941035, 7.432922], [1.025557, 158.833, 7.517172], [0.98809, 158.724956, 7.411505], [0.876652, 158.811839, 7.476893], [0.95159, 158.941035, 7.432922], [1.063027, 158.854162, 7.367535], [0.98809, 158.724956, 7.411505], [0.914122, 158.833, 7.327256], [0.95159, 158.941035, 7.432922], [2.691641, 148.640182, 6.41193]]}, {"shapeName": "L_shoulder_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.929719, 148.748227, 15.380865], [7.854783, 148.619021, 15.424835], [7.966221, 148.532138, 15.359447], [8.041157, 148.661344, 15.315477], [7.929719, 148.748227, 15.380865], [8.003682, 148.640182, 15.465105], [7.966221, 148.532138, 15.359447], [7.892252, 148.640182, 15.275198], [7.854783, 148.619021, 15.424835], [8.003682, 148.640182, 15.465105], [8.041157, 148.661344, 15.315477], [7.892252, 148.640182, 15.275198], [7.929719, 148.748227, 15.380865], [8.003682, 148.640182, 15.465105], [2.691641, 148.640182, 6.41193]]}]},
			"R_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_B_CTLShape", "degree": 3, "form": 2, "points": [[-65.68196, 105.346002, -2.643882], [-66.177446, 105.734633, -3.094825], [-66.861419, 106.081157, -2.985316], [-67.333216, 106.182584, -2.379503], [-67.316467, 105.9795, -1.632263], [-66.820981, 105.590869, -1.181321], [-66.137008, 105.244345, -1.29083], [-65.665211, 105.142918, -1.896643]]}]},
			"R_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.08413, 108.144823, 2.372049], [-68.104513, 108.218745, 2.425411], [-68.071183, 108.173892, 2.500276], [-68.0508, 108.09997, 2.446913], [-68.08413, 108.144823, 2.372049], [-68.137655, 108.134347, 2.44789], [-68.071183, 108.173892, 2.500276], [-68.017652, 108.18437, 2.424434], [-68.104513, 108.218745, 2.425411], [-68.137655, 108.134347, 2.44789], [-68.0508, 108.09997, 2.446913], [-68.017652, 108.18437, 2.424434], [-68.08413, 108.144823, 2.372049], [-68.137655, 108.134347, 2.44789], [-62.4169, 110.519, 1.32968]]}, {"shapeName": "R_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-64.956999, 116.107002, 0.251317], [-64.89052, 116.146549, 0.303702], [-64.944051, 116.136071, 0.379545], [-65.010529, 116.096524, 0.32716], [-64.956999, 116.107002, 0.251317], [-64.977379, 116.180918, 0.304681], [-64.944051, 116.136071, 0.379545], [-64.923668, 116.062149, 0.326182], [-64.89052, 116.146549, 0.303702], [-64.977379, 116.180918, 0.304681], [-65.010529, 116.096524, 0.32716], [-64.923668, 116.062149, 0.326182], [-64.956999, 116.107002, 0.251317], [-64.977379, 116.180918, 0.304681], [-62.4169, 110.519, 1.32968]]}, {"shapeName": "R_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.833052, 111.949534, 7.367348], [-61.746191, 111.915159, 7.36637], [-61.779339, 111.830759, 7.38885], [-61.8662, 111.865134, 7.389828], [-61.833052, 111.949534, 7.367348], [-61.799723, 111.90468, 7.442207], [-61.779339, 111.830759, 7.38885], [-61.812669, 111.875613, 7.313985], [-61.746191, 111.915159, 7.36637], [-61.799723, 111.90468, 7.442207], [-61.8662, 111.865134, 7.389828], [-61.812669, 111.875613, 7.313985], [-61.833052, 111.949534, 7.367348], [-61.799723, 111.90468, 7.442207], [-62.4169, 110.519, 1.32968]]}]},
			"R_arm_IK_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_CTLShape", "degree": 1, "form": 0, "points": [[-58.742279, 115.885111, 4.491418], [-53.673153, 109.766201, 2.833335], [-56.196629, 109.766201, -4.881483], [-61.265754, 115.885111, -3.223399], [-67.081455, 110.5517, -1.321115], [-62.012329, 104.43279, -2.979198], [-59.488854, 104.43279, 4.735619], [-64.557979, 110.5517, 6.393703], [-58.742279, 115.885111, 4.491418], [-61.265754, 115.885111, -3.223399], [-56.196629, 109.766201, -4.881483], [-62.012329, 104.43279, -2.979198], [-67.081455, 110.5517, -1.321115], [-64.557979, 110.5517, 6.393703], [-59.488854, 104.43279, 4.735619], [-53.673153, 109.766201, 2.833335]]}]},
			"L_wrist_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[59.255228, 107.461847, -3.375294], [61.950335, 110.158951, -4.052992], [63.723984, 112.856055, -1.913588], [63.53719, 113.973229, 1.789692], [61.49938, 112.856055, 4.887514], [58.804273, 110.158951, 5.565212], [57.030624, 107.461847, 3.425808], [57.217419, 106.344672, -0.277471]]}]},
			"L_loArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[49.134106, 119.958825, -3.508523], [49.203138, 120.072202, -3.427142], [49.121121, 120.0317, -3.301143], [49.052088, 119.918322, -3.382524], [49.134106, 119.958825, -3.508523], [49.207451, 119.925455, -3.375303], [49.121121, 120.0317, -3.301143], [49.047768, 120.065076, -3.434366], [49.203138, 120.072202, -3.427142], [49.207451, 119.925455, -3.375303], [49.052088, 119.918322, -3.382524], [49.047768, 120.065076, -3.434366], [49.134106, 119.958825, -3.508523], [49.207451, 119.925455, -3.375303], [41.595081, 126.581429, -6.190904]]}, {"shapeName": "L_loArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[48.726505, 133.803428, -8.399172], [48.640168, 133.90968, -8.325015], [48.713521, 133.876303, -8.191792], [48.799859, 133.770052, -8.26595], [48.726505, 133.803428, -8.399172], [48.795531, 133.916799, -8.317789], [48.713521, 133.876303, -8.191792], [48.644488, 133.762926, -8.273173], [48.640168, 133.90968, -8.325015], [48.795531, 133.916799, -8.317789], [48.799859, 133.770052, -8.26595], [48.644488, 133.762926, -8.273173], [48.726505, 133.803428, -8.399172], [48.795531, 133.916799, -8.317789], [41.595081, 126.581429, -6.190904]]}, {"shapeName": "L_loArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[41.058134, 130.095856, 3.568779], [40.902764, 130.08873, 3.561556], [40.907085, 129.941976, 3.613397], [41.062455, 129.949102, 3.620621], [41.058134, 130.095856, 3.568779], [40.976118, 130.05535, 3.694769], [40.907085, 129.941976, 3.613397], [40.989102, 129.982478, 3.487398], [40.902764, 130.08873, 3.561556], [40.976118, 130.05535, 3.694769], [41.062455, 129.949102, 3.620621], [40.989102, 129.982478, 3.487398], [41.058134, 130.095856, 3.568779], [40.976118, 130.05535, 3.694769], [41.595081, 126.581429, -6.190904]]}]},
			"R_wrist_IK_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_CTLShape", "degree": 3, "form": 2, "points": [[-62.765366, 103.828787, -2.645411], [-65.75993, 106.825569, -3.398409], [-67.73065, 109.822351, -1.021293], [-67.523101, 111.063656, 3.093462], [-65.258868, 109.822351, 6.535486], [-62.264304, 106.825569, 7.288484], [-60.293584, 103.828787, 4.911369], [-60.501133, 102.587482, 0.796614]]}]},
			"L_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_A_CTLShape", "degree": 3, "form": 2, "points": [[62.196073, 109.718417, 0.751634], [62.51604, 110.296508, 0.347502], [62.777914, 111.005026, 0.518714], [62.828294, 111.428931, 1.164977], [62.637667, 111.319907, 1.907719], [62.317701, 110.741816, 2.31185], [62.055827, 110.033298, 2.140639], [62.005447, 109.609392, 1.494376]]}]},
			"R_leg_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-12.219067, -3.809504, -6.114671], [-12.109135, -3.801443, -6.224639], [-12.219325, -3.78772, -6.333786], [-12.329256, -3.795781, -6.223817], [-12.219067, -3.809504, -6.114671], [-12.222053, -3.908123, -6.235112], [-12.219325, -3.78772, -6.333786], [-12.216338, -3.689091, -6.213344], [-12.109135, -3.801443, -6.224639], [-12.222053, -3.908123, -6.235112], [-12.329256, -3.795781, -6.223817], [-12.216338, -3.689091, -6.213344], [-12.219067, -3.809504, -6.114671], [-12.222053, -3.908123, -6.235112], [-11.949581, 6.53346, -5.197381]]}, {"shapeName": "R_leg_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.566487, 6.255479, -5.1266], [-1.563758, 6.375892, -5.225272], [-1.566745, 6.277262, -5.345714], [-1.569474, 6.15685, -5.247042], [-1.566487, 6.255479, -5.1266], [-1.456565, 6.26354, -5.236568], [-1.566745, 6.277262, -5.345714], [-1.676676, 6.269202, -5.235746], [-1.563758, 6.375892, -5.225272], [-1.456565, 6.26354, -5.236568], [-1.569474, 6.15685, -5.247042], [-1.676676, 6.269202, -5.235746], [-1.566487, 6.255479, -5.1266], [-1.456565, 6.26354, -5.236568], [-11.949581, 6.53346, -5.197381]]}, {"shapeName": "R_leg_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-11.851689, 7.558136, -15.533308], [-11.958891, 7.670488, -15.522012], [-12.071809, 7.563798, -15.532486], [-11.964607, 7.451446, -15.543781], [-11.851689, 7.558136, -15.533308], [-11.961878, 7.571858, -15.642444], [-12.071809, 7.563798, -15.532486], [-11.96162, 7.550076, -15.423339], [-11.958891, 7.670488, -15.522012], [-11.961878, 7.571858, -15.642444], [-11.964607, 7.451446, -15.543781], [-11.96162, 7.550076, -15.423339], [-11.851689, 7.558136, -15.533308], [-11.961878, 7.571858, -15.642444], [-11.949581, 6.53346, -5.197381]]}]},
			"R_upArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-24.195701, 144.488118, -3.337514], [-24.296192, 144.571585, -3.252792], [-24.245633, 144.501171, -3.123452], [-24.145142, 144.417705, -3.208174], [-24.195701, 144.488118, -3.337514], [-24.296779, 144.416172, -3.243452], [-24.245633, 144.501171, -3.123452], [-24.144548, 144.573124, -3.217513], [-24.296192, 144.571585, -3.252792], [-24.296779, 144.416172, -3.243452], [-24.145142, 144.417705, -3.208174], [-24.144548, 144.573124, -3.217513], [-24.195701, 144.488118, -3.337514], [-24.296779, 144.416172, -3.243452], [-17.039658, 151.898346, -2.006913]]}, {"shapeName": "R_upArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-24.139623, 159.150257, -4.218522], [-24.08847, 159.235263, -4.098521], [-24.189555, 159.16331, -4.004461], [-24.240709, 159.078303, -4.124461], [-24.139623, 159.150257, -4.218522], [-24.240107, 159.233716, -4.133798], [-24.189555, 159.16331, -4.004461], [-24.089065, 159.079843, -4.089182], [-24.08847, 159.235263, -4.098521], [-24.240107, 159.233716, -4.133798], [-24.240709, 159.078303, -4.124461], [-24.089065, 159.079843, -4.089182], [-24.139623, 159.150257, -4.218522], [-24.240107, 159.233716, -4.133798], [-17.039658, 151.898346, -2.006913]]}, {"shapeName": "R_upArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-19.470445, 152.591004, 8.067928], [-19.318801, 152.592544, 8.103207], [-19.319396, 152.437124, 8.112546], [-19.47104, 152.435584, 8.077267], [-19.470445, 152.591004, 8.067928], [-19.419884, 152.52059, 8.197258], [-19.319396, 152.437124, 8.112546], [-19.369954, 152.507538, 7.983206], [-19.318801, 152.592544, 8.103207], [-19.419884, 152.52059, 8.197258], [-19.47104, 152.435584, 8.077267], [-19.369954, 152.507538, 7.983206], [-19.470445, 152.591004, 8.067928], [-19.419884, 152.52059, 8.197258], [-17.039658, 151.898346, -2.006913]]}]},
			"L_legBase_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.70308, 92.979434, 0.903787], [9.77661, 90.138448, 0.783472], [9.804696, 89.053286, 0.737516], [9.758947, 89.855021, 7.465226], [9.674501, 92.52084, 11.715095], [9.583612, 96.032508, 11.863813], [9.520998, 99.048662, 7.854573], [9.510575, 100.417252, 1.218776], [9.538661, 99.332089, 1.172819], [9.612191, 96.491103, 1.052505], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146]]}]},
			"C_head_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_head_FK_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 169.08313, -10.46736], [0.0, 169.471408, -10.544594], [0.0, 169.800575, -10.764545], [0.0, 170.020526, -11.093711], [0.0, 170.09776, -11.48199], [0.0, 170.020526, -11.870269], [0.0, 169.800575, -12.199435], [0.0, 169.471408, -12.419386], [0.0, 169.08313, -12.49662], [0.0, 168.694851, -12.419386], [0.0, 168.365685, -12.199435], [0.0, 168.145734, -11.870269], [0.0, 168.0685, -11.48199], [0.0, 168.145734, -11.093711], [0.0, 168.365685, -10.764545], [0.0, 168.694851, -10.544594], [0.0, 169.08313, -10.46736], [0.0, 169.08313, -0.32106]]}]},
			"L_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[71.363692, 101.576565, 0.02507], [71.423524, 101.624613, 0.078352], [71.384337, 101.588382, 0.155028], [71.324506, 101.540333, 0.101746], [71.363692, 101.576565, 0.02507], [71.416508, 101.53195, 0.087893], [71.384337, 101.588382, 0.155028], [71.331517, 101.633001, 0.092206], [71.423524, 101.624613, 0.078352], [71.416508, 101.53195, 0.087893], [71.324506, 101.540333, 0.101746], [71.331517, 101.633001, 0.092206], [71.363692, 101.576565, 0.02507], [71.416508, 101.53195, 0.087893], [67.364861, 106.349197, 0.293512]]}, {"shapeName": "L_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[72.025162, 110.318716, -0.874927], [71.992987, 110.375152, -0.807791], [72.045807, 110.330533, -0.744969], [72.077982, 110.274097, -0.812105], [72.025162, 110.318716, -0.874927], [72.084989, 110.36676, -0.821644], [72.045807, 110.330533, -0.744969], [71.985975, 110.282485, -0.798251], [71.992987, 110.375152, -0.807791], [72.084989, 110.36676, -0.821644], [72.077982, 110.274097, -0.812105], [71.985975, 110.282485, -0.798251], [72.025162, 110.318716, -0.874927], [72.084989, 110.36676, -0.821644], [67.364861, 106.349197, 0.293512]]}, {"shapeName": "L_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[68.388191, 106.948736, 6.411852], [68.296185, 106.957124, 6.425706], [68.289173, 106.864456, 6.435246], [68.38118, 106.856068, 6.421392], [68.388191, 106.948736, 6.411852], [68.349004, 106.912504, 6.488522], [68.289173, 106.864456, 6.435246], [68.32836, 106.900687, 6.35857], [68.296185, 106.957124, 6.425706], [68.349004, 106.912504, 6.488522], [68.38118, 106.856068, 6.421392], [68.32836, 106.900687, 6.35857], [68.388191, 106.948736, 6.411852], [68.349004, 106.912504, 6.488522], [67.364861, 106.349197, 0.293512]]}]},
			"R_wrist_IK_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-59.629253, 108.360882, -1.998159], [-61.425992, 110.158951, -2.449958], [-62.608424, 111.95702, -1.023688], [-62.483894, 112.701803, 1.445164], [-61.125355, 111.95702, 3.510379], [-59.328617, 110.158951, 3.962178], [-58.146184, 108.360882, 2.535909], [-58.270714, 107.616099, 0.067056]]}]},
			"R_innerBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_innerBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[4.981497, 1.926057, 8.489965], [4.991115, 2.030131, 8.374557], [4.999757, 1.914323, 8.270842], [4.99014, 1.810249, 8.386251], [4.981497, 1.926057, 8.489965], [5.100334, 1.92019, 8.389546], [4.999757, 1.914323, 8.270842], [4.88091, 1.92019, 8.371261], [4.991115, 2.030131, 8.374557], [5.100334, 1.92019, 8.389546], [4.99014, 1.810249, 8.386251], [4.88091, 1.92019, 8.371261], [4.981497, 1.926057, 8.489965], [5.100334, 1.92019, 8.389546], [-5.35997, 1.92019, 7.51788]]}, {"shapeName": "R_innerBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-5.323134, 12.297771, 7.075827], [-5.423721, 12.291903, 6.957122], [-5.304874, 12.286035, 6.856705], [-5.204287, 12.291903, 6.975408], [-5.323134, 12.297771, 7.075827], [-5.313516, 12.401834, 6.960419], [-5.304874, 12.286035, 6.856705], [-5.314491, 12.181962, 6.972113], [-5.423721, 12.291903, 6.957122], [-5.313516, 12.401834, 6.960419], [-5.204287, 12.291903, 6.975408], [-5.314491, 12.181962, 6.972113], [-5.323134, 12.297771, 7.075827], [-5.313516, 12.401834, 6.960419], [-5.35997, 1.92019, 7.51788]]}, {"shapeName": "R_innerBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-4.498185, 1.476605, -2.823855], [-4.60839, 1.366663, -2.827151], [-4.499159, 1.256722, -2.812162], [-4.388955, 1.366663, -2.808866], [-4.498185, 1.476605, -2.823855], [-4.489544, 1.360797, -2.92756], [-4.499159, 1.256722, -2.812162], [-4.507802, 1.372531, -2.708447], [-4.60839, 1.366663, -2.827151], [-4.489544, 1.360797, -2.92756], [-4.388955, 1.366663, -2.808866], [-4.507802, 1.372531, -2.708447], [-4.498185, 1.476605, -2.823855], [-4.489544, 1.360797, -2.92756], [-5.35997, 1.92019, 7.51788]]}]},
			"C_midNeck_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_midNeck_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.386473, 162.294507, -1.337496], [10.386473, 162.389084, -1.213811], [10.386473, 162.265399, -1.119234], [10.386473, 162.170822, -1.242919], [10.386473, 162.294507, -1.337496], [10.49656, 162.279953, -1.228365], [10.386473, 162.265399, -1.119234], [10.276375, 162.279953, -1.228365], [10.386473, 162.389084, -1.213811], [10.49656, 162.279953, -1.228365], [10.386473, 162.170822, -1.242919], [10.276375, 162.279953, -1.228365], [10.386473, 162.294507, -1.337496], [10.49656, 162.279953, -1.228365], [0.0, 162.279953, -1.228365]]}, {"shapeName": "C_midNeck_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 172.589826, 0.035537], [-0.110097, 172.575272, 0.144669], [0.0, 172.560718, 0.2538], [0.110097, 172.575272, 0.144669], [0.0, 172.589826, 0.035537], [0.0, 172.684393, 0.159221], [0.0, 172.560718, 0.2538], [0.0, 172.466141, 0.130114], [-0.110097, 172.575272, 0.144669], [0.0, 172.684393, 0.159221], [0.110097, 172.575272, 0.144669], [0.0, 172.466141, 0.130114], [0.0, 172.589826, 0.035537], [0.0, 172.684393, 0.159221], [0.0, 162.279953, -1.228365]]}, {"shapeName": "C_midNeck_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 161.016051, 9.081508], [-0.110097, 160.90692, 9.066954], [0.0, 160.797788, 9.0524], [0.110097, 160.90692, 9.066954], [0.0, 161.016051, 9.081508], [0.0, 160.892367, 9.176075], [0.0, 160.797788, 9.0524], [0.0, 160.921474, 8.957823], [-0.110097, 160.90692, 9.066954], [0.0, 160.892367, 9.176075], [0.110097, 160.90692, 9.066954], [0.0, 160.921474, 8.957823], [0.0, 161.016051, 9.081508], [0.0, 160.892367, 9.176075], [0.0, 162.279953, -1.228365]]}]},
			"R_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_D_CTLShape", "degree": 3, "form": 2, "points": [[-71.979742, 100.409534, 3.556106], [-72.71537, 100.475218, 3.322809], [-73.386989, 100.643811, 3.669787], [-73.601174, 100.816555, 4.393786], [-73.232458, 100.892258, 5.070697], [-72.496831, 100.826574, 5.303993], [-71.825211, 100.657981, 4.957015], [-71.611027, 100.485237, 4.233016]]}]},
			"L_toeTip_CTL": {"color": 20, "shapes": [{"shapeName": "L_toeTip_CTLShape", "degree": 1, "form": 0, "points": [[12.310461, 2.591352, 19.228147], [12.230813, 1.524092, 18.272344], [13.237448, 2.53728, 18.134201], [12.310461, 2.591352, 19.228147], [11.215197, 2.53728, 18.302716], [12.230813, 1.524092, 18.272344], [12.142185, 2.483207, 17.20877], [11.215197, 2.53728, 18.302716], [12.221832, 3.550468, 18.164573], [12.310461, 2.591352, 19.228147], [13.237448, 2.53728, 18.134201], [12.142185, 2.483207, 17.20877], [12.221832, 3.550468, 18.164573], [13.237448, 2.53728, 18.134201]]}]},
			"C_chest_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.869458, 135.492372, -8.366842], [0.0, 138.473545, -10.663354], [-6.869458, 135.492372, -8.366842], [-9.714875, 132.426381, -2.718035], [-6.869458, 135.202788, 3.078592], [0.0, 138.064013, 5.522924], [6.869458, 135.202788, 3.078592], [9.714875, 132.426381, -2.718035]]}]},
			"L_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[69.07506, 105.582534, 2.951174], [69.114164, 105.644747, 3.008861], [69.063922, 105.610544, 3.079806], [69.024817, 105.54833, 3.022119], [69.07506, 105.582534, 2.951174], [69.117829, 105.553606, 3.029024], [69.063922, 105.610544, 3.079806], [69.021149, 105.639475, 3.001955], [69.114164, 105.644747, 3.008861], [69.117829, 105.553606, 3.029024], [69.024817, 105.54833, 3.022119], [69.021149, 105.639475, 3.001955], [69.07506, 105.582534, 2.951174], [69.117829, 105.553606, 3.029024], [64.508919, 109.647108, 1.738599]]}, {"shapeName": "L_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[68.728934, 114.181035, 1.048879], [68.675023, 114.237976, 1.09966], [68.717796, 114.209045, 1.177512], [68.771708, 114.152103, 1.126731], [68.728934, 114.181035, 1.048879], [68.768035, 114.243244, 1.106567], [68.717796, 114.209045, 1.177512], [68.678692, 114.146831, 1.119825], [68.675023, 114.237976, 1.09966], [68.768035, 114.243244, 1.106567], [68.771708, 114.152103, 1.126731], [68.678692, 114.146831, 1.119825], [68.728934, 114.181035, 1.048879], [68.768035, 114.243244, 1.106567], [64.508919, 109.647108, 1.738599]]}, {"shapeName": "L_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[64.028235, 111.016519, 7.79949], [63.935219, 111.011247, 7.792584], [63.938888, 110.920102, 7.812748], [64.031904, 110.925374, 7.819654], [64.028235, 111.016519, 7.79949], [63.977993, 110.982314, 7.870429], [63.938888, 110.920102, 7.812748], [63.98913, 110.954306, 7.741803], [63.935219, 111.011247, 7.792584], [63.977993, 110.982314, 7.870429], [64.031904, 110.925374, 7.819654], [63.98913, 110.954306, 7.741803], [64.028235, 111.016519, 7.79949], [63.977993, 110.982314, 7.870429], [64.508919, 109.647108, 1.738599]]}]},
			"R_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-72.472412, 98.593468, 9.745066], [-72.502171, 98.637794, 9.821728], [-72.420713, 98.619772, 9.863768], [-72.390955, 98.575446, 9.787106], [-72.472412, 98.593468, 9.745066], [-72.471123, 98.54989, 9.827685], [-72.420713, 98.619772, 9.863768], [-72.422001, 98.663356, 9.781147], [-72.502171, 98.637794, 9.821728], [-72.471123, 98.54989, 9.827685], [-72.390955, 98.575446, 9.787106], [-72.422001, 98.663356, 9.781147], [-72.472412, 98.593468, 9.745066], [-72.471123, 98.54989, 9.827685], [-70.1294, 103.959, 7.60916]]}, {"shapeName": "R_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-75.401234, 106.886763, 9.182918], [-75.350822, 106.95665, 9.218999], [-75.349535, 106.913067, 9.30162], [-75.399947, 106.843179, 9.265539], [-75.401234, 106.886763, 9.182918], [-75.430987, 106.931086, 9.259579], [-75.349535, 106.913067, 9.30162], [-75.319777, 106.868741, 9.224958], [-75.350822, 106.95665, 9.218999], [-75.430987, 106.931086, 9.259579], [-75.399947, 106.843179, 9.265539], [-75.319777, 106.868741, 9.224958], [-75.401234, 106.886763, 9.182918], [-75.430987, 106.931086, 9.259579], [-70.1294, 103.959, 7.60916]]}, {"shapeName": "R_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-67.746406, 105.230908, 13.225593], [-67.666236, 105.256469, 13.185012], [-67.63519, 105.16856, 13.190971], [-67.71536, 105.142998, 13.231552], [-67.746406, 105.230908, 13.225593], [-67.664951, 105.212884, 13.267628], [-67.63519, 105.16856, 13.190971], [-67.716647, 105.186582, 13.148931], [-67.666236, 105.256469, 13.185012], [-67.664951, 105.212884, 13.267628], [-67.71536, 105.142998, 13.231552], [-67.716647, 105.186582, 13.148931], [-67.746406, 105.230908, 13.225593], [-67.664951, 105.212884, 13.267628], [-70.1294, 103.959, 7.60916]]}]},
			"R_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-73.490417, 93.759642, 0.353049], [-73.563923, 93.783359, 0.405602], [-73.513051, 93.769964, 0.482803], [-73.439545, 93.746246, 0.430251], [-73.490417, 93.759642, 0.353049], [-73.52092, 93.70162, 0.419605], [-73.513051, 93.769964, 0.482803], [-73.482547, 93.827991, 0.416247], [-73.563923, 93.783359, 0.405602], [-73.52092, 93.70162, 0.419605], [-73.439545, 93.746246, 0.430251], [-73.482547, 93.827991, 0.416247], [-73.490417, 93.759642, 0.353049], [-73.52092, 93.70162, 0.419605], [-71.6916, 99.7259, 0.259492]]}, {"shapeName": "R_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-77.547132, 101.471353, -0.968059], [-77.539261, 101.539702, -0.904861], [-77.569766, 101.481675, -0.838305], [-77.577636, 101.413326, -0.901502], [-77.547132, 101.471353, -0.968059], [-77.620632, 101.495069, -0.915505], [-77.569766, 101.481675, -0.838305], [-77.49626, 101.457957, -0.890857], [-77.539261, 101.539702, -0.904861], [-77.620632, 101.495069, -0.915505], [-77.577636, 101.413326, -0.901502], [-77.49626, 101.457957, -0.890857], [-77.547132, 101.471353, -0.968059], [-77.620632, 101.495069, -0.915505], [-71.6916, 99.7259, 0.259492]]}, {"shapeName": "R_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-72.821437, 100.231325, 6.367581], [-72.74006, 100.275956, 6.378226], [-72.697059, 100.194212, 6.39223], [-72.778436, 100.14958, 6.381585], [-72.821437, 100.231325, 6.367581], [-72.770564, 100.217929, 6.444777], [-72.697059, 100.194212, 6.39223], [-72.747931, 100.207607, 6.315029], [-72.74006, 100.275956, 6.378226], [-72.770564, 100.217929, 6.444777], [-72.778436, 100.14958, 6.381585], [-72.747931, 100.207607, 6.315029], [-72.821437, 100.231325, 6.367581], [-72.770564, 100.217929, 6.444777], [-71.6916, 99.7259, 0.259492]]}]},
			"L_heel_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_heel_PIV_CTLShape", "degree": 1, "form": 0, "points": [[20.160712, 0.984467, -11.63944], [20.169355, 1.100276, -11.535725], [20.178972, 0.996202, -11.420317], [20.170329, 0.880393, -11.524031], [20.160712, 0.984467, -11.63944], [20.279549, 0.990335, -11.53902], [20.178972, 0.996202, -11.420317], [20.060125, 0.990335, -11.520735], [20.169355, 1.100276, -11.535725], [20.279549, 0.990335, -11.53902], [20.170329, 0.880393, -11.524031], [20.060125, 0.990335, -11.520735], [20.160712, 0.984467, -11.63944], [20.279549, 0.990335, -11.53902], [9.819244, 0.990335, -10.667355]]}, {"shapeName": "L_heel_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[9.764148, 11.35618, -11.32853], [9.663561, 11.362047, -11.209826], [9.782408, 11.367915, -11.109408], [9.882995, 11.362047, -11.228112], [9.764148, 11.35618, -11.32853], [9.772791, 11.471978, -11.224815], [9.782408, 11.367915, -11.109408], [9.773765, 11.252106, -11.213122], [9.663561, 11.362047, -11.209826], [9.772791, 11.471978, -11.224815], [9.882995, 11.362047, -11.228112], [9.773765, 11.252106, -11.213122], [9.764148, 11.35618, -11.32853], [9.772791, 11.471978, -11.224815], [9.819244, 0.990335, -10.667355]]}, {"shapeName": "L_heel_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[10.680055, 1.653802, -0.337313], [10.570825, 1.543861, -0.322323], [10.68103, 1.43392, -0.325619], [10.79026, 1.543861, -0.340609], [10.680055, 1.653802, -0.337313], [10.689671, 1.549728, -0.221915], [10.68103, 1.43392, -0.325619], [10.671413, 1.537993, -0.441027], [10.570825, 1.543861, -0.322323], [10.689671, 1.549728, -0.221915], [10.79026, 1.543861, -0.340609], [10.671413, 1.537993, -0.441027], [10.680055, 1.653802, -0.337313], [10.689671, 1.549728, -0.221915], [9.819244, 0.990335, -10.667355]]}]},
			"L_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_D_CTLShape", "degree": 3, "form": 2, "points": [[70.895352, 99.46899, -0.309774], [71.518227, 99.646846, -0.734373], [72.242659, 99.871014, -0.57678], [72.644287, 100.01018, 0.070691], [72.487842, 99.982822, 0.828759], [71.864967, 99.804967, 1.253357], [71.140534, 99.580798, 1.095764], [70.738907, 99.441633, 0.448294]]}]},
			"L_arm_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[59.232786, 114.167263, 3.370826], [55.684399, 109.884026, 2.210167], [57.450831, 109.884026, -3.190205], [60.999219, 114.167263, -2.029546], [65.070209, 110.433876, -0.697947], [61.521822, 106.150638, -1.858606], [59.755389, 106.150638, 3.541766], [63.303777, 110.433876, 4.702425], [59.232786, 114.167263, 3.370826], [60.999219, 114.167263, -2.029546], [57.450831, 109.884026, -3.190205], [61.521822, 106.150638, -1.858606], [65.070209, 110.433876, -0.697947], [63.303777, 110.433876, 4.702425], [59.755389, 106.150638, 3.541766], [55.684399, 109.884026, 2.210167]]}]},
			"L_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_B_CTLShape", "degree": 3, "form": 2, "points": [[66.716744, 105.828721, -0.283658], [67.206726, 106.258684, -0.701915], [67.789341, 106.741668, -0.537065], [68.123301, 106.994748, 0.114327], [68.012977, 106.869674, 0.870683], [67.522995, 106.439711, 1.28894], [66.94038, 105.956726, 1.12409], [66.60642, 105.703647, 0.472698]]}]},
			"R_arm_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-65.024947, 114.315727, 2.276329], [-64.863572, 114.120931, 2.223544], [-64.643028, 114.258267, 2.151405], [-64.473844, 114.169835, 2.096066], [-64.444677, 113.901937, 2.086526], [-64.199649, 113.884255, 2.006378], [-64.136002, 114.145432, 1.98556], [-63.956929, 114.208772, 1.926986], [-63.756258, 114.041023, 1.861348], [-63.57111, 114.210817, 1.800787], [-63.701655, 114.442877, 1.843487], [-63.617585, 114.620857, 1.815988], [-63.362967, 114.651551, 1.732704], [-63.346161, 114.909354, 1.727207], [-63.594417, 114.976332, 1.80841], [-63.65458, 115.164744, 1.828089], [-63.49516, 115.375862, 1.775944], [-63.656536, 115.570657, 1.828729], [-63.877095, 115.43334, 1.900873], [-64.046279, 115.521772, 1.956212], [-64.075446, 115.78967, 1.965752], [-64.320464, 115.80734, 2.045896], [-64.384138, 115.546159, 2.066724], [-64.563193, 115.482835, 2.125292], [-64.763849, 115.650566, 2.190925], [-64.948998, 115.480771, 2.251487], [-64.818468, 115.24873, 2.208791], [-64.902555, 115.070733, 2.236295], [-65.157146, 115.040043, 2.31957], [-65.173962, 114.782252, 2.325071], [-64.925706, 114.715275, 2.243868], [-64.865543, 114.526863, 2.224189], [-65.024947, 114.315727, 2.276329]]}, {"shapeName": "R_arm_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-64.636187, 114.872935, 2.149168], [-64.507779, 115.144822, 2.107166], [-64.234253, 115.241538, 2.017697], [-63.97586, 115.106425, 1.933178], [-63.883936, 114.818672, 1.90311], [-64.012343, 114.546785, 1.945112], [-64.28587, 114.450069, 2.034581], [-64.544252, 114.58517, 2.119096]]}, {"shapeName": "R_arm_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-63.663684, 114.12592, 1.831067], [-60.377304, 110.158951, 0.75611]]}]},
			"C_neck_FK_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_C_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 165.888963, -10.983184], [0.0, 166.284043, -11.008411], [0.0, 166.639397, -11.182919], [0.0, 166.900932, -11.48012], [0.0, 167.028816, -11.854781], [0.0, 167.003589, -12.249862], [0.0, 166.829082, -12.605215], [0.0, 166.53188, -12.866751], [0.0, 166.157219, -12.994635], [0.0, 165.762139, -12.969407], [0.0, 165.406785, -12.7949], [0.0, 165.14525, -12.497699], [0.0, 165.017366, -12.123038], [0.0, 165.042593, -11.727957], [0.0, 165.2171, -11.372603], [0.0, 165.514301, -11.111068], [0.0, 165.888963, -10.983184], [0.0, 164.547679, -0.92593]]}]},
			"R_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-72.301635, 95.846561, 10.278699], [-72.335301, 95.878358, 10.359834], [-72.249946, 95.872856, 10.397407], [-72.21628, 95.841059, 10.316272], [-72.301635, 95.846561, 10.278699], [-72.288212, 95.797722, 10.357192], [-72.249946, 95.872856, 10.397407], [-72.263369, 95.921701, 10.318913], [-72.335301, 95.878358, 10.359834], [-72.288212, 95.797722, 10.357192], [-72.21628, 95.841059, 10.316272], [-72.263369, 95.921701, 10.318913], [-72.301635, 95.846561, 10.278699], [-72.288212, 95.797722, 10.357192], [-71.1039, 101.708, 8.53236]]}, {"shapeName": "R_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-76.743891, 103.454258, 10.52781], [-76.705625, 103.529397, 10.568024], [-76.692203, 103.480552, 10.646519], [-76.730469, 103.405413, 10.606305], [-76.743891, 103.454258, 10.52781], [-76.777552, 103.486053, 10.608944], [-76.692203, 103.480552, 10.646519], [-76.658537, 103.448755, 10.565384], [-76.705625, 103.529397, 10.568024], [-76.777552, 103.486053, 10.608944], [-76.730469, 103.405413, 10.606305], [-76.658537, 103.448755, 10.565384], [-76.743891, 103.454258, 10.52781], [-76.777552, 103.486053, 10.608944], [-71.1039, 101.708, 8.53236]]}, {"shapeName": "R_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-68.725296, 102.966952, 14.153571], [-68.653364, 103.010295, 14.11265], [-68.606275, 102.929653, 14.110009], [-68.678208, 102.88631, 14.150931], [-68.725296, 102.966952, 14.153571], [-68.639944, 102.961449, 14.191139], [-68.606275, 102.929653, 14.110009], [-68.69163, 102.935155, 14.072436], [-68.653364, 103.010295, 14.11265], [-68.639944, 102.961449, 14.191139], [-68.678208, 102.88631, 14.150931], [-68.69163, 102.935155, 14.072436], [-68.725296, 102.966952, 14.153571], [-68.639944, 102.961449, 14.191139], [-71.1039, 101.708, 8.53236]]}]},
			"L_legBase_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.716064, 92.477768, 0.882541], [9.810603, 88.825071, 0.727851], [9.846713, 87.429862, 0.668764], [9.787893, 88.460665, 9.318677], [9.679319, 91.888146, 14.782795], [9.562462, 96.403148, 14.974004], [9.481959, 100.28106, 9.819266], [9.468557, 102.040675, 1.287527], [9.504668, 100.645466, 1.228441], [9.599207, 96.99277, 1.07375], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146]]}]},
			"C_hip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_hip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.231884, 102.093931, -0.127752], [6.231884, 102.165376, -0.06756], [6.231884, 102.105185, 0.003885], [6.231884, 102.03374, -0.056306], [6.231884, 102.093931, -0.127752], [6.297936, 102.099558, -0.061933], [6.231884, 102.105185, 0.003885], [6.165825, 102.099558, -0.061933], [6.231884, 102.165376, -0.06756], [6.297936, 102.099558, -0.061933], [6.231884, 102.03374, -0.056306], [6.165825, 102.099558, -0.061933], [6.231884, 102.093931, -0.127752], [6.297936, 102.099558, -0.061933], [0.0, 102.099558, -0.061933]]}, {"shapeName": "C_hip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 108.303165, -0.658587], [-0.066058, 108.308792, -0.592769], [0.0, 108.314419, -0.52695], [0.066058, 108.308792, -0.592769], [0.0, 108.303165, -0.658587], [0.0, 108.374604, -0.598395], [0.0, 108.314419, -0.52695], [0.0, 108.242974, -0.587142], [-0.066058, 108.308792, -0.592769], [0.0, 108.374604, -0.598395], [0.066058, 108.308792, -0.592769], [0.0, 108.242974, -0.587142], [0.0, 108.303165, -0.658587], [0.0, 108.374604, -0.598395], [0.0, 102.099558, -0.061933]]}, {"shapeName": "C_hip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 102.696212, 6.141674], [-0.066058, 102.630394, 6.147301], [0.0, 102.564575, 6.152928], [0.066058, 102.630394, 6.147301], [0.0, 102.696212, 6.141674], [0.0, 102.63602, 6.213113], [0.0, 102.564575, 6.152928], [0.0, 102.624767, 6.081482], [-0.066058, 102.630394, 6.147301], [0.0, 102.63602, 6.213113], [0.066058, 102.630394, 6.147301], [0.0, 102.624767, 6.081482], [0.0, 102.696212, 6.141674], [0.0, 102.63602, 6.213113], [0.0, 102.099558, -0.061933]]}]},
			"L_legEnd_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_legEnd_FK_CTLShape", "degree": 3, "form": 2, "points": [[15.918963, 6.242412, -1.226661], [11.942995, 5.977286, 0.397072], [7.970885, 6.037958, -1.256344], [6.329445, 6.388889, -5.21837], [7.9802, 6.824507, -9.1681], [11.956167, 7.089633, -10.791833], [15.928277, 7.028961, -9.138417], [17.569717, 6.678031, -5.176392]]}]},
			"R_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-73.741684, 97.624952, 4.907741], [-73.796178, 97.660064, 4.975009], [-73.727418, 97.647888, 5.037068], [-73.672923, 97.612776, 4.9698], [-73.741684, 97.624952, 4.907741], [-73.757241, 97.575819, 4.985655], [-73.727418, 97.647888, 5.037068], [-73.711859, 97.697027, 4.959153], [-73.796178, 97.660064, 4.975009], [-73.757241, 97.575819, 4.985655], [-73.672923, 97.612776, 4.9698], [-73.711859, 97.697027, 4.959153], [-73.741684, 97.624952, 4.907741], [-73.757241, 97.575819, 4.985655], [-71.5938, 103.354, 3.72227]]}, {"shapeName": "R_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-77.414776, 105.573054, 3.90334], [-77.384951, 105.645128, 3.954751], [-77.40051, 105.595989, 4.032666], [-77.430335, 105.523915, 3.981255], [-77.414776, 105.573054, 3.90334], [-77.469264, 105.608163, 3.970608], [-77.40051, 105.595989, 4.032666], [-77.346015, 105.560878, 3.965398], [-77.384951, 105.645128, 3.954751], [-77.469264, 105.608163, 3.970608], [-77.430335, 105.523915, 3.981255], [-77.346015, 105.560878, 3.965398], [-77.414776, 105.573054, 3.90334], [-77.469264, 105.608163, 3.970608], [-71.5938, 103.354, 3.72227]]}, {"shapeName": "R_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-70.982525, 104.459505, 9.825133], [-70.898206, 104.496468, 9.809277], [-70.859271, 104.412218, 9.819924], [-70.94359, 104.375254, 9.83578], [-70.982525, 104.459505, 9.825133], [-70.913766, 104.447328, 9.887186], [-70.859271, 104.412218, 9.819924], [-70.928031, 104.424393, 9.757865], [-70.898206, 104.496468, 9.809277], [-70.913766, 104.447328, 9.887186], [-70.94359, 104.375254, 9.83578], [-70.928031, 104.424393, 9.757865], [-70.982525, 104.459505, 9.825133], [-70.913766, 104.447328, 9.887186], [-71.5938, 103.354, 3.72227]]}]},
			"R_shoulder_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_CTLShape", "degree": 3, "form": 0, "points": [[-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-3.962608, 148.640182, 8.578006], [-6.019065, 148.640182, 12.082773], [-6.804564, 148.640182, 13.421479], [-14.105637, 150.47649, 7.337897], [-17.04696, 151.611392, 0.900631], [-14.505026, 151.611392, -3.431521], [-7.450787, 150.47649, -4.003791], [1.421282, 148.640182, -0.597619], [0.635784, 148.640182, 0.741086], [-1.420674, 148.640182, 4.245854], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193]]}]},
			"L_innerBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_innerBall_CTLShape", "degree": 1, "form": 0, "points": [[3.421859, 1.97426, 8.696084], [3.342211, 0.906999, 7.740282], [4.348846, 1.920187, 7.602138], [3.421859, 1.97426, 8.696084], [2.326595, 1.920187, 7.770654], [3.342211, 0.906999, 7.740282], [3.253583, 1.866115, 6.676707], [2.326595, 1.920187, 7.770654], [3.33323, 2.933375, 7.63251], [3.421859, 1.97426, 8.696084], [4.348846, 1.920187, 7.602138], [3.253583, 1.866115, 6.676707], [3.33323, 2.933375, 7.63251], [4.348846, 1.920187, 7.602138]]}]},
			"C_neckBase_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[12.880235, 156.903436, -12.773966], [0.0, 152.06025, -17.905204], [-12.880235, 156.903436, -12.773966], [-18.215391, 160.91544, -1.410343], [-12.880235, 154.065611, 8.504693], [0.0, 148.046963, 12.187345], [12.880235, 154.065611, 8.504693], [18.215391, 160.91544, -1.410343]]}]},
			"R_leg_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-16.689283, 7.368325, -5.108802], [-16.495544, 7.363341, -5.109526], [-16.464016, 7.164569, -5.129324], [-16.327826, 7.104266, -5.135479], [-16.158319, 7.214051, -5.124765], [-16.024881, 7.074203, -5.138825], [-16.143829, 6.911456, -5.154864], [-16.090388, 6.772975, -5.168694], [-15.89252, 6.731349, -5.173065], [-15.897551, 6.538554, -5.192226], [-16.097324, 6.507157, -5.195112], [-16.157916, 6.371628, -5.208515], [-16.047616, 6.202966, -5.225412], [-16.188169, 6.070165, -5.238449], [-16.351722, 6.188518, -5.22649], [-16.490875, 6.135297, -5.231618], [-16.532728, 5.938413, -5.251142], [-16.726467, 5.943397, -5.250418], [-16.758013, 6.142169, -5.23062], [-16.894204, 6.202473, -5.224465], [-17.06371, 6.092688, -5.235179], [-17.197136, 6.232535, -5.221119], [-17.078199, 6.395301, -5.205078], [-17.131642, 6.533764, -5.19125], [-17.329491, 6.575389, -5.186879], [-17.32446, 6.768184, -5.167718], [-17.124705, 6.799581, -5.164831], [-17.064113, 6.935129, -5.151427], [-17.174401, 7.103773, -5.134532], [-17.03386, 7.236573, -5.121495], [-16.870307, 7.118221, -5.133453], [-16.731155, 7.171441, -5.128326], [-16.689283, 7.368325, -5.108802]]}, {"shapeName": "R_leg_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-16.81584, 6.868046, -5.158389], [-16.908412, 6.661019, -5.178861], [-16.826762, 6.449511, -5.199985], [-16.618731, 6.357436, -5.209383], [-16.406189, 6.438692, -5.201555], [-16.313617, 6.645719, -5.181083], [-16.395268, 6.857227, -5.159959], [-16.603286, 6.949302, -5.150561]]}, {"shapeName": "R_leg_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-15.895035, 6.634952, -5.182646], [-11.949581, 6.53346, -5.197381]]}]},
			"R_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_B_CTLShape", "degree": 3, "form": 2, "points": [[-62.223365, 107.952185, 7.830568], [-62.216261, 108.527043, 8.349584], [-61.689735, 108.817932, 8.837482], [-60.952218, 108.65445, 9.008458], [-60.435738, 108.132364, 8.762358], [-60.442843, 107.557505, 8.243342], [-60.969369, 107.266617, 7.755444], [-61.706885, 107.430099, 7.584468]]}]},
			"C_world_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_world_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 0.0, -0.054255], [5.118355, 0.054255, 0.0], [5.118355, 0.0, 0.054255], [5.118355, -0.054255, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [5.118355, 0.0, 0.054255], [5.0641, 0.0, 0.0], [5.118355, 0.054255, 0.0], [5.172605, 0.0, 0.0], [5.118355, -0.054255, 0.0], [5.0641, 0.0, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 5.118355, -0.054255], [-0.054255, 5.118355, 0.0], [0.0, 5.118355, 0.054255], [0.054255, 5.118355, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 5.118355, 0.054255], [0.0, 5.0641, 0.0], [-0.054255, 5.118355, 0.0], [0.0, 5.172605, 0.0], [0.054255, 5.118355, 0.0], [0.0, 5.0641, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 0.054255, 5.118355], [-0.054255, 0.0, 5.118355], [0.0, -0.054255, 5.118355], [0.054255, 0.0, 5.118355], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, -0.054255, 5.118355], [0.0, 0.0, 5.0641], [-0.054255, 0.0, 5.118355], [0.0, 0.0, 5.172605], [0.054255, 0.0, 5.118355], [0.0, 0.0, 5.0641], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, 0.0, 0.0]]}]},
			"R_hand_CTL": {"color": 18, "shapes": [{"shapeName": "R_hand_CTLShape", "degree": 3, "form": 2, "points": [[-66.505832, 112.678394, 1.313271], [-65.790263, 112.678394, 1.016874], [-65.074695, 112.678394, 1.313271], [-64.778297, 112.678394, 2.02884], [-65.074695, 112.678394, 2.744408], [-65.790263, 112.678394, 3.040806], [-66.505832, 112.678394, 2.744408], [-66.802229, 112.678394, 2.02884]]}, {"shapeName": "R_hand_CTLShape1", "degree": 3, "form": 2, "points": [[-65.790263, 113.393963, 1.313271], [-65.790263, 112.678394, 1.016874], [-65.790263, 111.962825, 1.313271], [-65.790263, 111.666428, 2.02884], [-65.790263, 111.962825, 2.744408], [-65.790263, 112.678394, 3.040806], [-65.790263, 113.393963, 2.744408], [-65.790263, 113.69036, 2.02884]]}, {"shapeName": "R_hand_CTLShape2", "degree": 3, "form": 2, "points": [[-65.074695, 113.393963, 2.02884], [-64.778297, 112.678394, 2.02884], [-65.074695, 111.962825, 2.02884], [-65.790263, 111.666428, 2.02884], [-66.505832, 111.962825, 2.02884], [-66.802229, 112.678394, 2.02884], [-66.505832, 113.393963, 2.02884], [-65.790263, 113.69036, 2.02884]]}]},
			"R_arm_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[-66.186858, 115.354921, 2.656384], [-65.985138, 115.111427, 2.590402], [-65.709459, 115.283096, 2.500229], [-65.497979, 115.172556, 2.431055], [-65.46152, 114.837684, 2.41913], [-65.155235, 114.815581, 2.318945], [-65.075677, 115.142052, 2.292922], [-64.851836, 115.221228, 2.219705], [-64.600997, 115.01154, 2.137657], [-64.369561, 115.223784, 2.061956], [-64.532743, 115.513858, 2.115332], [-64.427655, 115.736334, 2.080958], [-64.109383, 115.774701, 1.976853], [-64.088375, 116.096955, 1.969981], [-64.398695, 116.180677, 2.071485], [-64.473899, 116.416193, 2.096084], [-64.274625, 116.680089, 2.030903], [-64.476344, 116.923584, 2.096884], [-64.752042, 116.751937, 2.187063], [-64.963523, 116.862477, 2.256237], [-64.999981, 117.19735, 2.268163], [-65.306254, 117.219437, 2.368343], [-65.385846, 116.892961, 2.394377], [-65.609666, 116.813806, 2.467587], [-65.860486, 117.02347, 2.549629], [-66.091922, 116.811227, 2.625331], [-65.928759, 116.521175, 2.571961], [-66.033868, 116.298679, 2.606342], [-66.352106, 116.260317, 2.710436], [-66.373126, 115.938078, 2.717311], [-66.062806, 115.854356, 2.615807], [-65.987602, 115.618841, 2.591208], [-66.186858, 115.354921, 2.656384]]}, {"shapeName": "R_arm_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[-65.700908, 116.051431, 2.497432], [-65.540398, 116.39129, 2.44493], [-65.19849, 116.512184, 2.333094], [-64.8755, 116.343294, 2.227446], [-64.760593, 115.983602, 2.18986], [-64.921103, 115.643743, 2.242362], [-65.263012, 115.522849, 2.354199], [-65.585989, 115.691724, 2.459843]]}, {"shapeName": "R_arm_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[-64.485279, 115.117662, 2.099806], [-60.377304, 110.158951, 0.75611]]}]},
			"L_arm_PV_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_PV_CTLShape", "degree": 1, "form": 0, "points": [[29.586224, 109.61085, -104.425449], [29.586224, 107.58159, -104.425449], [29.586224, 107.58159, -106.454709], [29.586224, 109.61085, -106.454709], [31.615484, 109.61085, -106.454709], [31.615484, 107.58159, -106.454709], [31.615484, 107.58159, -104.425449], [31.615484, 109.61085, -104.425449], [29.586224, 109.61085, -104.425449], [29.586224, 109.61085, -106.454709], [29.586224, 107.58159, -106.454709], [31.615484, 107.58159, -106.454709], [31.615484, 109.61085, -106.454709], [31.615484, 109.61085, -104.425449], [31.615484, 107.58159, -104.425449], [29.586224, 107.58159, -104.425449]]}]},
			"R_legBase_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.709572, 92.728601, 0.893164], [-9.793606, 89.48176, 0.755662], [-9.825705, 88.241574, 0.70314], [-9.77342, 89.157843, 8.391951], [-9.67691, 92.204493, 13.248945], [-9.573037, 96.217828, 13.418908], [-9.501478, 99.664861, 8.83692], [-9.489566, 101.228963, 1.253151], [-9.521665, 99.988778, 1.20063], [-9.605699, 96.741936, 1.063127], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146]]}]},
			"C_cog_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[25.550624, 102.099558, 1.776813], [25.523674, 102.099558, -2.242813], [18.587685, 102.099558, -4.656343], [17.639829, 102.099558, -7.508682], [21.751655, 102.099558, -13.592646], [19.367197, 102.099558, -16.828745], [12.33617, 102.099558, -14.708744], [9.893466, 102.099558, -16.459303], [9.644325, 102.099558, -23.793806], [5.813089, 102.099558, -25.010338], [1.372654, 102.099558, -19.16654], [-1.63187, 102.099558, -19.146673], [-6.146837, 102.099558, -24.930205], [-9.961402, 102.099558, -23.662459], [-10.115172, 102.099558, -16.327037], [-12.533892, 102.099558, -14.544337], [-19.590105, 102.099558, -16.567766], [-21.930994, 102.099558, -13.299987], [-17.739342, 102.099558, -7.274805], [-18.648385, 102.099558, -4.410219], [-25.550624, 102.099558, -1.900679], [-25.523674, 102.099558, 2.118947], [-18.587685, 102.099558, 4.532477], [-17.639829, 102.099558, 7.384816], [-21.751655, 102.099558, 13.46878], [-19.367197, 102.099558, 16.704879], [-12.33617, 102.099558, 14.584878], [-9.893466, 102.099558, 16.335437], [-9.644325, 102.099558, 23.669939], [-5.813089, 102.099558, 24.886471], [-1.372654, 102.099558, 19.042674], [1.63187, 102.099558, 19.022807], [6.146837, 102.099558, 24.806339], [9.961402, 102.099558, 23.538593], [10.115172, 102.099558, 16.20317], [12.533892, 102.099558, 14.420471], [19.590105, 102.099558, 16.443899], [21.930994, 102.099558, 13.176121], [17.739342, 102.099558, 7.150939], [18.648385, 102.099558, 4.286352], [25.550624, 102.099558, 1.776813]]}]},
			"R_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.776302, 107.917538, 5.215378], [-66.781453, 107.984427, 5.280392], [-66.723327, 107.935803, 5.335023], [-66.718177, 107.868914, 5.270009], [-66.776302, 107.917538, 5.215378], [-66.801397, 107.895941, 5.30273], [-66.723327, 107.935803, 5.335023], [-66.698228, 107.957404, 5.247668], [-66.781453, 107.984427, 5.280392], [-66.801397, 107.895941, 5.30273], [-66.718177, 107.868914, 5.270009], [-66.698228, 107.957404, 5.247668], [-66.776302, 107.917538, 5.215378], [-66.801397, 107.895941, 5.30273], [-61.8832, 110.826, 2.67783]]}, {"shapeName": "R_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-64.894399, 116.265539, 3.107753], [-64.816326, 116.305404, 3.140043], [-64.841425, 116.283803, 3.227398], [-64.919499, 116.243938, 3.195108], [-64.894399, 116.265539, 3.107753], [-64.899547, 116.332422, 3.172766], [-64.841425, 116.283803, 3.227398], [-64.836274, 116.216914, 3.162384], [-64.816326, 116.305404, 3.140043], [-64.899547, 116.332422, 3.172766], [-64.919499, 116.243938, 3.195108], [-64.836274, 116.216914, 3.162384], [-64.894399, 116.265539, 3.107753], [-64.899547, 116.332422, 3.172766], [-61.8832, 110.826, 2.67783]]}, {"shapeName": "R_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-59.416052, 111.745293, 8.326619], [-59.332828, 111.71827, 8.293896], [-59.352776, 111.629781, 8.316237], [-59.436001, 111.656804, 8.34896], [-59.416052, 111.745293, 8.326619], [-59.357929, 111.696669, 8.381245], [-59.352776, 111.629781, 8.316237], [-59.410901, 111.678405, 8.261605], [-59.332828, 111.71827, 8.293896], [-59.357929, 111.696669, 8.381245], [-59.436001, 111.656804, 8.34896], [-59.410901, 111.678405, 8.261605], [-59.416052, 111.745293, 8.326619], [-59.357929, 111.696669, 8.381245], [-61.8832, 110.826, 2.67783]]}]},
			"C_neck_FK_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_A_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 156.825807, -12.19189], [0.0, 157.220888, -12.217118], [0.0, 157.576242, -12.391625], [0.0, 157.837777, -12.688826], [0.0, 157.965661, -13.063487], [0.0, 157.940434, -13.458568], [0.0, 157.765926, -13.813922], [0.0, 157.468725, -14.075457], [0.0, 157.094064, -14.203341], [0.0, 156.698983, -14.178113], [0.0, 156.34363, -14.003606], [0.0, 156.082094, -13.706405], [0.0, 155.95421, -13.331744], [0.0, 155.979438, -12.936663], [0.0, 156.153945, -12.581309], [0.0, 156.451146, -12.319774], [0.0, 156.825807, -12.19189], [0.0, 155.484523, -2.134636]]}]},
			"L_toe_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_toe_FK_CTLShape", "degree": 3, "form": 2, "points": [[16.025795, 6.807385, 9.940247], [12.050417, 8.450476, 10.048596], [8.075039, 6.806799, 9.949535], [6.428387, 2.839188, 9.701092], [8.075039, -1.12818, 9.448801], [12.050417, -2.771271, 9.340451], [16.025795, -1.127593, 9.439512], [17.672447, 2.840017, 9.687956]]}]},
			"C_head_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[10.733529, 179.816659, -0.32106], [0.0, 184.262622, -0.32106], [-10.733529, 179.816659, -0.32106], [-15.179492, 169.08313, -0.32106], [-10.733529, 158.349601, -0.32106], [0.0, 153.903638, -0.32106], [10.733529, 158.349601, -0.32106], [15.179492, 169.08313, -0.32106]]}]},
			"C_chest_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[5.152094, 135.456174, -6.936163], [0.0, 137.692054, -8.658547], [-5.152094, 135.456174, -6.936163], [-7.286156, 133.15668, -2.699557], [-5.152094, 135.238986, 1.647913], [0.0, 137.384905, 3.481162], [5.152094, 135.238986, 1.647913], [7.286156, 133.15668, -2.699557]]}]},
			"L_upLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_upLeg_FK_CTLShape", "degree": 3, "form": 2, "points": [[13.621175, 94.66902, 4.964783], [9.642787, 94.497008, 6.595109], [5.673097, 94.464566, 4.9351], [4.0375, 94.590698, 0.957157], [5.694096, 94.801517, -3.008491], [9.672484, 94.973529, -4.638818], [13.642173, 95.005972, -2.978808], [15.277771, 94.87984, 0.999135]]}]},
			"L_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.0841, 108.144985, 2.372045], [68.104483, 108.218907, 2.425407], [68.071153, 108.174054, 2.500272], [68.05077, 108.100132, 2.446909], [68.0841, 108.144985, 2.372045], [68.137625, 108.134509, 2.447886], [68.071153, 108.174054, 2.500272], [68.017622, 108.184532, 2.42443], [68.104483, 108.218907, 2.425407], [68.137625, 108.134509, 2.447886], [68.05077, 108.100132, 2.446909], [68.017622, 108.184532, 2.42443], [68.0841, 108.144985, 2.372045], [68.137625, 108.134509, 2.447886], [62.41687, 110.519162, 1.329676]]}, {"shapeName": "L_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[64.956969, 116.107164, 0.251313], [64.89049, 116.146711, 0.303698], [64.944021, 116.136233, 0.379541], [65.010499, 116.096686, 0.327156], [64.956969, 116.107164, 0.251313], [64.977349, 116.18108, 0.304677], [64.944021, 116.136233, 0.379541], [64.923638, 116.062311, 0.326178], [64.89049, 116.146711, 0.303698], [64.977349, 116.18108, 0.304677], [65.010499, 116.096686, 0.327156], [64.923638, 116.062311, 0.326178], [64.956969, 116.107164, 0.251313], [64.977349, 116.18108, 0.304677], [62.41687, 110.519162, 1.329676]]}, {"shapeName": "L_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.833022, 111.949696, 7.367344], [61.746161, 111.915321, 7.366366], [61.779309, 111.830921, 7.388846], [61.86617, 111.865296, 7.389824], [61.833022, 111.949696, 7.367344], [61.799693, 111.904842, 7.442203], [61.779309, 111.830921, 7.388846], [61.812639, 111.875775, 7.313981], [61.746161, 111.915321, 7.366366], [61.799693, 111.904842, 7.442203], [61.86617, 111.865296, 7.389824], [61.812639, 111.875775, 7.313981], [61.833022, 111.949696, 7.367344], [61.799693, 111.904842, 7.442203], [62.41687, 110.519162, 1.329676]]}]},
			"C_torso_FK_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_D_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 122.747366, -7.676902], [0.0, 122.975539, -7.742918], [0.0, 123.16108, -7.891233], [0.0, 123.275748, -8.099256], [0.0, 123.302076, -8.335324], [0.0, 123.236059, -8.563497], [0.0, 123.087745, -8.749037], [0.0, 122.879722, -8.863705], [0.0, 122.643654, -8.890033], [0.0, 122.415481, -8.824017], [0.0, 122.22994, -8.675702], [0.0, 122.115272, -8.467679], [0.0, 122.088945, -8.231611], [0.0, 122.154961, -8.003438], [0.0, 122.303275, -7.817898], [0.0, 122.511298, -7.70323], [0.0, 122.747366, -7.676902], [0.0, 123.265927, -1.611248]]}]},
			"L_wrist_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_wrist_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.853237, 103.334378, 3.08561], [67.887766, 103.417374, 3.212742], [67.784782, 103.334378, 3.294894], [67.750253, 103.251383, 3.167762], [67.853237, 103.334378, 3.08561], [67.897885, 103.262044, 3.216052], [67.784782, 103.334378, 3.294894], [67.740127, 103.406719, 3.16445], [67.887766, 103.417374, 3.212742], [67.897885, 103.262044, 3.216052], [67.750253, 103.251383, 3.167762], [67.740127, 103.406719, 3.16445], [67.853237, 103.334378, 3.08561], [67.897885, 103.262044, 3.216052], [60.377304, 110.158951, 0.75611]]}, {"shapeName": "L_wrist_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[66.897928, 117.988639, 2.773133], [66.784817, 118.06098, 2.851973], [66.829472, 117.988639, 2.982417], [66.942582, 117.916298, 2.903577], [66.897928, 117.988639, 2.773133], [66.93245, 118.071627, 2.900263], [66.829472, 117.988639, 2.982417], [66.794943, 117.905644, 2.855285], [66.784817, 118.06098, 2.851973], [66.93245, 118.071627, 2.900263], [66.942582, 117.916298, 2.903577], [66.794943, 117.905644, 2.855285], [66.897928, 117.988639, 2.773133], [66.93245, 118.071627, 2.900263], [60.377304, 110.158951, 0.75611]]}, {"shapeName": "L_wrist_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[57.21705, 110.241946, 10.650393], [57.069411, 110.231292, 10.602101], [57.079537, 110.075955, 10.605414], [57.227176, 110.08661, 10.653706], [57.21705, 110.241946, 10.650393], [57.114069, 110.158951, 10.732536], [57.079537, 110.075955, 10.605414], [57.182521, 110.158951, 10.523262], [57.069411, 110.231292, 10.602101], [57.114069, 110.158951, 10.732536], [57.227176, 110.08661, 10.653706], [57.182521, 110.158951, 10.523262], [57.21705, 110.241946, 10.650393], [57.114069, 110.158951, 10.732536], [60.377304, 110.158951, 0.75611]]}]},
			"L_heel_CTL": {"color": 20, "shapes": [{"shapeName": "L_heel_CTLShape", "degree": 1, "form": 0, "points": [[9.735106, 0.936262, -11.677043], [9.655458, -0.130999, -12.632846], [10.662093, 0.882189, -12.770989], [9.735106, 0.936262, -11.677043], [8.639843, 0.882189, -12.602474], [9.655458, -0.130999, -12.632846], [9.56683, 0.828117, -13.69642], [8.639843, 0.882189, -12.602474], [9.646478, 1.895377, -12.740617], [9.735106, 0.936262, -11.677043], [10.662093, 0.882189, -12.770989], [9.56683, 0.828117, -13.69642], [9.646478, 1.895377, -12.740617], [10.662093, 0.882189, -12.770989]]}]},
			"R_legEnd_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_legEnd_FK_CTLShape", "degree": 3, "form": 2, "points": [[-15.918963, 6.242412, -1.226661], [-11.942995, 5.977286, 0.397072], [-7.970885, 6.037958, -1.256344], [-6.329445, 6.388889, -5.21837], [-7.9802, 6.824507, -9.1681], [-11.956167, 7.089633, -10.791833], [-15.928277, 7.028961, -9.138417], [-17.569717, 6.678031, -5.176392]]}]},
			"world_D_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -346.62], [153.99, 0.0, -192.48], [115.44, 0.0, -192.48], [115.44, 0.0, -115.41], [192.51, 0.0, -115.41], [192.51, 0.0, -153.96], [346.62, 0.0, 0.0], [192.48, 0.0, 153.99], [192.48, 0.0, 115.44], [115.41, 0.0, 115.44], [115.41, 0.0, 192.51], [153.96, 0.0, 192.51], [0.0, 0.0, 346.62], [-153.99, 0.0, 192.48], [-115.44, 0.0, 192.48], [-115.44, 0.0, 115.41], [-192.51, 0.0, 115.41], [-192.51, 0.0, 153.96], [-346.62, 0.0, 0.0], [-192.48, 0.0, -153.99], [-192.48, 0.0, -115.44], [-115.41, 0.0, -115.44], [-115.41, 0.0, -192.51], [-153.96, 0.0, -192.51], [0.0, 0.0, -346.62], [30.18, 0.42, -316.98], [27.54, 0.0, -314.16], [27.54, 0.0, -302.64], [25.14, 0.0, -302.64], [25.29, 0.0, -314.25], [23.58, 0.0, -313.38], [23.64, 0.0, -308.34], [21.21, 0.0, -308.34], [21.21, 0.0, -313.38], [19.71, 0.0, -314.25], [19.71, 0.0, -302.46], [17.28, 0.0, -302.46], [17.28, 0.0, -314.55], [19.23, 0.0, -316.5], [22.23, 0.0, -315.0], [25.53, 0.0, -316.5], [27.54, 0.0, -314.22], [25.53, 0.0, -316.5], [22.26, 0.0, -315.03], [19.23, 0.0, -316.47], [13.38, 0.0, -316.5], [15.36, 0.0, -314.55], [15.36, 0.0, -304.44], [13.38, 0.0, -302.46], [7.05, 0.0, -302.46], [5.1, 0.0, -304.44], [5.1, 0.0, -314.55], [7.05, 0.0, -316.5], [13.38, 0.0, -316.5], [12.63, 0.0, -314.25], [12.93, 0.0, -304.95], [7.5, 0.0, -305.01], [7.53, 0.0, -314.25], [12.66, 0.0, -314.31], [13.38, 0.0, -316.5], [7.05, 0.0, -316.5], [3.0, 0.0, -316.5], [3.15, 0.0, -302.46], [-3.69, 0.0, -302.46], [-5.67, 0.0, -304.44], [-5.67, 0.0, -308.67], [-3.66, 0.0, -310.62], [-3.54, 0.0, -310.77], [-7.47, 0.0, -316.44], [-7.47, 0.0, -316.5], [-4.65, 0.0, -316.5], [-0.72, 0.0, -310.8], [0.75, 0.0, -310.8], [0.75, 0.0, -304.8], [-3.03, 0.0, -304.8], [-3.06, 0.0, -308.37], [0.75, 0.0, -308.37], [0.75, 0.0, -316.5], [3.0, 0.0, -316.5], [-19.29, 0.0, -316.5], [-19.29, 0.0, -314.25], [-11.43, 0.0, -314.22], [-11.43, 0.0, -302.46], [-9.0, 0.0, -302.46], [-9.0, 0.0, -316.5], [-29.52, 0.0, -316.5], [-31.32, 0.0, -314.55], [-31.47, 0.0, -304.44], [-29.52, 0.0, -302.46], [-21.21, 0.0, -302.46], [-21.21, 0.0, -316.5], [-23.67, 0.0, -314.25], [-23.61, 0.0, -304.74], [-28.74, 0.0, -304.74], [-28.68, 0.0, -314.19], [-23.58, 0.0, -314.31], [-21.15, 0.0, -316.5]]}]},
			"L_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_B_CTLShape", "degree": 3, "form": 2, "points": [[64.085324, 108.973191, 1.113715], [64.594229, 109.432564, 0.753324], [65.053161, 110.017613, 0.970093], [65.193283, 110.385625, 1.637043], [64.932514, 110.321024, 2.363484], [64.423609, 109.861651, 2.723875], [63.964677, 109.276602, 2.507106], [63.824555, 108.90859, 1.840156]]}]},
			"L_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_A_CTLShape", "degree": 3, "form": 2, "points": [[61.468832, 109.126256, -1.841721], [61.746386, 109.495946, -2.463156], [62.268911, 110.055727, -2.579358], [62.730318, 110.477687, -2.122255], [62.860323, 110.514648, -1.359613], [62.582768, 110.144958, -0.738178], [62.060243, 109.585176, -0.621976], [61.598836, 109.163217, -1.079079]]}]},
			"L_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_A_CTLShape", "degree": 3, "form": 2, "points": [[61.576133, 109.559049, -0.275899], [61.962789, 110.090125, -0.686198], [62.408424, 110.699132, -0.511814], [62.65199, 111.029322, 0.145103], [62.55081, 110.887276, 0.899739], [62.164154, 110.3562, 1.310038], [61.718519, 109.747193, 1.135654], [61.474953, 109.417003, 0.478737]]}]},
			"L_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_D_CTLShape", "degree": 3, "form": 2, "points": [[67.672164, 100.180648, -3.722059], [68.210477, 100.478645, -4.192491], [68.937896, 100.729169, -4.103109], [69.428309, 100.785465, -3.506271], [69.394439, 100.614558, -2.751596], [68.856125, 100.316561, -2.281165], [68.128706, 100.066038, -2.370546], [67.638293, 100.009741, -2.967385]]}]},
			"R_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_C_CTLShape", "degree": 3, "form": 2, "points": [[-67.411826, 102.307633, -3.453911], [-67.990818, 102.433869, -3.952632], [-68.758898, 102.512672, -3.89153], [-69.266135, 102.497879, -3.306396], [-69.215398, 102.398156, -2.539995], [-68.636406, 102.27192, -2.041274], [-67.868326, 102.193117, -2.102376], [-67.361089, 102.20791, -2.68751]]}]},
			"L_arm_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[58.905781, 115.312495, 4.117887], [54.343569, 109.805476, 2.625612], [56.614696, 109.805476, -4.317723], [61.176909, 115.312495, -2.825448], [66.41104, 110.512425, -1.113392], [61.848827, 105.005406, -2.605667], [59.577699, 105.005406, 4.337668], [64.139912, 110.512425, 5.829943], [58.905781, 115.312495, 4.117887], [61.176909, 115.312495, -2.825448], [56.614696, 109.805476, -4.317723], [61.848827, 105.005406, -2.605667], [66.41104, 110.512425, -1.113392], [64.139912, 110.512425, 5.829943], [59.577699, 105.005406, 4.337668], [54.343569, 109.805476, 2.625612]]}]},
			"C_torso_FK_E_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_E_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 135.510361, -2.724341], [-0.066058, 135.515988, -2.658522], [0.0, 135.521614, -2.592704], [0.066058, 135.515988, -2.658522], [0.0, 135.510361, -2.724341], [0.0, 135.5818, -2.664149], [0.0, 135.521614, -2.592704], [0.0, 135.450169, -2.652895], [-0.066058, 135.515988, -2.658522], [0.0, 135.5818, -2.664149], [0.066058, 135.515988, -2.658522], [0.0, 135.450169, -2.652895], [0.0, 135.510361, -2.724341], [0.0, 135.5818, -2.664149], [0.0, 129.306754, -2.127687]]}, {"shapeName": "C_torso_FK_E_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 129.301127, -2.193505], [-6.231884, 129.240935, -2.12206], [-6.231884, 129.31238, -2.061868], [-6.231884, 129.372572, -2.133314], [-6.231884, 129.301127, -2.193505], [-6.297936, 129.306754, -2.127687], [-6.231884, 129.31238, -2.061868], [-6.165825, 129.306754, -2.127687], [-6.231884, 129.240935, -2.12206], [-6.297936, 129.306754, -2.127687], [-6.231884, 129.372572, -2.133314], [-6.165825, 129.306754, -2.127687], [-6.231884, 129.301127, -2.193505], [-6.297936, 129.306754, -2.127687], [0.0, 129.306754, -2.127687]]}, {"shapeName": "C_torso_FK_E_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 129.837589, 4.081547], [0.0, 129.771771, 4.087174], [0.066058, 129.837589, 4.081547], [0.0, 129.903408, 4.07592], [-0.066058, 129.837589, 4.081547], [0.0, 129.843216, 4.14736], [0.066058, 129.837589, 4.081547], [0.0, 129.831962, 4.015729], [0.0, 129.771771, 4.087174], [0.0, 129.843216, 4.14736], [0.0, 129.903408, 4.07592], [0.0, 129.831962, 4.015729], [-0.066058, 129.837589, 4.081547], [0.0, 129.843216, 4.14736], [0.0, 129.306754, -2.127687]]}]},
			"R_wrist_IK_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-59.504578, 108.061203, -2.457204], [-61.600773, 110.158951, -2.984302], [-62.980277, 112.256698, -1.320321], [-62.834993, 113.125612, 1.560007], [-61.25003, 112.256698, 3.969424], [-59.153835, 110.158951, 4.496523], [-57.774331, 108.061203, 2.832542], [-57.919615, 107.19229, -0.047787]]}]},
			"L_leg_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[17.479234, 7.507469, -5.094039], [17.253205, 7.501655, -5.094883], [17.216422, 7.269754, -5.117981], [17.057533, 7.1994, -5.125162], [16.859776, 7.327483, -5.112662], [16.704098, 7.164327, -5.129065], [16.842871, 6.974455, -5.147778], [16.780522, 6.812894, -5.163913], [16.549676, 6.764331, -5.169013], [16.555546, 6.539403, -5.191367], [16.788615, 6.502774, -5.194734], [16.859305, 6.344656, -5.21037], [16.730622, 6.147883, -5.230084], [16.8946, 5.99295, -5.245294], [17.085412, 6.131028, -5.231342], [17.247757, 6.068937, -5.237324], [17.296585, 5.839239, -5.260102], [17.522614, 5.845053, -5.259258], [17.559419, 6.076954, -5.23616], [17.718307, 6.147308, -5.228979], [17.916065, 6.019226, -5.241479], [18.071729, 6.182381, -5.225076], [17.932969, 6.372274, -5.206361], [17.995318, 6.533815, -5.190228], [18.226143, 6.582377, -5.185128], [18.220273, 6.807305, -5.162774], [17.987226, 6.843935, -5.159407], [17.916534, 7.002074, -5.143768], [18.045205, 7.198825, -5.124057], [17.88124, 7.353759, -5.108847], [17.690428, 7.215681, -5.122799], [17.528084, 7.277771, -5.116817], [17.479234, 7.507469, -5.094039]]}, {"shapeName": "L_leg_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[17.626883, 6.923811, -5.15189], [17.734884, 6.682279, -5.175775], [17.639625, 6.43552, -5.200419], [17.396922, 6.328098, -5.211384], [17.148957, 6.422898, -5.202251], [17.040957, 6.664429, -5.178366], [17.136215, 6.911189, -5.153722], [17.378904, 7.01861, -5.142757]]}, {"shapeName": "L_leg_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[16.552611, 6.651867, -5.18019], [11.949581, 6.53346, -5.197381]]}]},
			"C_chest_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_CTLShape", "degree": 3, "form": 2, "points": [[8.586823, 135.528569, -9.797522], [0.0, 139.255037, -12.668162], [-8.586823, 135.528569, -9.797522], [-12.143594, 131.696081, -2.736512], [-8.586823, 135.16659, 4.509272], [0.0, 138.743122, 7.564686], [8.586823, 135.16659, 4.509272], [12.143594, 131.696081, -2.736512]]}]},
			"C_neck_FK_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 165.794397, -0.870734], [-0.110097, 165.779842, -0.761603], [0.0, 165.765288, -0.652472], [0.110097, 165.779842, -0.761603], [0.0, 165.794397, -0.870734], [0.0, 165.888964, -0.74705], [0.0, 165.765288, -0.652472], [0.0, 165.670711, -0.776157], [-0.110097, 165.779842, -0.761603], [0.0, 165.888964, -0.74705], [0.110097, 165.779842, -0.761603], [0.0, 165.670711, -0.776157], [0.0, 165.794397, -0.870734], [0.0, 165.888964, -0.74705], [0.0, 155.484523, -2.134636]]}, {"shapeName": "C_neck_FK_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-10.386473, 155.499078, -2.243768], [-10.386473, 155.375392, -2.149191], [-10.386473, 155.469969, -2.025505], [-10.386473, 155.593655, -2.120082], [-10.386473, 155.499078, -2.243768], [-10.49656, 155.484523, -2.134636], [-10.386473, 155.469969, -2.025505], [-10.276375, 155.484523, -2.134636], [-10.386473, 155.375392, -2.149191], [-10.49656, 155.484523, -2.134636], [-10.386473, 155.593655, -2.120082], [-10.276375, 155.484523, -2.134636], [-10.386473, 155.499078, -2.243768], [-10.49656, 155.484523, -2.134636], [0.0, 155.484523, -2.134636]]}, {"shapeName": "C_neck_FK_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.110097, 154.11149, 8.160683], [0.0, 154.002359, 8.146128], [0.110097, 154.11149, 8.160683], [0.0, 154.220621, 8.175237], [-0.110097, 154.11149, 8.160683], [0.0, 154.096937, 8.269804], [0.110097, 154.11149, 8.160683], [0.0, 154.126044, 8.051551], [0.0, 154.002359, 8.146128], [0.0, 154.096937, 8.269804], [0.0, 154.220621, 8.175237], [0.0, 154.126044, 8.051551], [-0.110097, 154.11149, 8.160683], [0.0, 154.096937, 8.269804], [0.0, 155.484523, -2.134636]]}]},
			"C_chest_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_chest_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.231884, 135.349251, -2.710162], [6.231884, 135.413617, -2.642454], [6.231884, 135.345909, -2.578088], [6.231884, 135.281543, -2.645796], [6.231884, 135.349251, -2.710162], [6.297936, 135.34758, -2.644125], [6.231884, 135.345909, -2.578088], [6.165825, 135.34758, -2.644125], [6.231884, 135.413617, -2.642454], [6.297936, 135.34758, -2.644125], [6.231884, 135.281543, -2.645796], [6.165825, 135.34758, -2.644125], [6.231884, 135.349251, -2.710162], [6.297936, 135.34758, -2.644125], [0.0, 135.34758, -2.644125]]}, {"shapeName": "C_chest_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 141.579141, -2.552539], [-0.066058, 141.57747, -2.486501], [0.0, 141.575799, -2.420464], [0.066058, 141.57747, -2.486501], [0.0, 141.579141, -2.552539], [0.0, 141.643501, -2.484831], [0.0, 141.575799, -2.420464], [0.0, 141.511432, -2.488172], [-0.066058, 141.57747, -2.486501], [0.0, 141.643501, -2.484831], [0.066058, 141.57747, -2.486501], [0.0, 141.511432, -2.488172], [0.0, 141.579141, -2.552539], [0.0, 141.643501, -2.484831], [0.0, 135.34758, -2.644125]]}, {"shapeName": "C_chest_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 135.255994, 3.587436], [-0.066058, 135.189956, 3.585765], [0.0, 135.123919, 3.584094], [0.066058, 135.189956, 3.585765], [0.0, 135.255994, 3.587436], [0.0, 135.188286, 3.651796], [0.0, 135.123919, 3.584094], [0.0, 135.191627, 3.519728], [-0.066058, 135.189956, 3.585765], [0.0, 135.188286, 3.651796], [0.066058, 135.189956, 3.585765], [0.0, 135.191627, 3.519728], [0.0, 135.255994, 3.587436], [0.0, 135.188286, 3.651796], [0.0, 135.34758, -2.644125]]}]},
			"L_arm_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[38.062044, 101.379185, -105.07132], [38.149499, 101.475641, -104.985934], [38.085904, 101.418217, -104.85593], [37.998449, 101.321761, -104.941316], [38.062044, 101.379185, -105.07132], [38.153182, 101.322414, -104.958575], [38.085904, 101.418217, -104.85593], [37.994758, 101.474995, -104.968676], [38.149499, 101.475641, -104.985934], [38.153182, 101.322414, -104.958575], [37.998449, 101.321761, -104.941316], [37.994758, 101.474995, -104.968676], [38.062044, 101.379185, -105.07132], [38.153182, 101.322414, -104.958575], [30.600854, 108.59622, -105.440079]]}, {"shapeName": "L_arm_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[37.713856, 115.835141, -107.652353], [37.64657, 115.930951, -107.549708], [37.737715, 115.874173, -107.436962], [37.805001, 115.778363, -107.539607], [37.713856, 115.835141, -107.652353], [37.801303, 115.93159, -107.566964], [37.737715, 115.874173, -107.436962], [37.650261, 115.777717, -107.522349], [37.64657, 115.930951, -107.549708], [37.801303, 115.93159, -107.566964], [37.805001, 115.778363, -107.539607], [37.650261, 115.777717, -107.522349], [37.713856, 115.835141, -107.652353], [37.801303, 115.93159, -107.566964], [30.600854, 108.59622, -105.440079]]}, {"shapeName": "L_arm_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[31.801826, 110.514254, -95.302538], [31.647085, 110.513608, -95.28528], [31.650776, 110.360373, -95.25792], [31.805517, 110.361019, -95.275179], [31.801826, 110.514254, -95.302538], [31.73823, 110.456827, -95.172544], [31.650776, 110.360373, -95.25792], [31.714371, 110.417798, -95.387924], [31.647085, 110.513608, -95.28528], [31.73823, 110.456827, -95.172544], [31.805517, 110.361019, -95.275179], [31.714371, 110.417798, -95.387924], [31.801826, 110.514254, -95.302538], [31.73823, 110.456827, -95.172544], [30.600854, 108.59622, -105.440079]]}]},
			"R_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-70.634986, 94.668988, -4.502562], [-70.714483, 94.689017, -4.457767], [-70.677132, 94.658408, -4.377795], [-70.597635, 94.638379, -4.42259], [-70.634986, 94.668988, -4.502562], [-70.678558, 94.60292, -4.452933], [-70.677132, 94.658408, -4.377795], [-70.633557, 94.724482, -4.427423], [-70.714483, 94.689017, -4.457767], [-70.678558, 94.60292, -4.452933], [-70.597635, 94.638379, -4.42259], [-70.633557, 94.724482, -4.427423], [-70.634986, 94.668988, -4.502562], [-70.678558, 94.60292, -4.452933], [-68.5333, 100.398, -3.23683]]}, {"shapeName": "R_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-74.023858, 102.791821, -4.958495], [-74.02243, 102.847315, -4.883356], [-74.066004, 102.781241, -4.833728], [-74.067433, 102.725747, -4.908867], [-74.023858, 102.791821, -4.958495], [-74.10335, 102.811847, -4.913698], [-74.066004, 102.781241, -4.833728], [-73.986507, 102.761212, -4.878523], [-74.02243, 102.847315, -4.883356], [-74.10335, 102.811847, -4.913698], [-74.067433, 102.725747, -4.908867], [-73.986507, 102.761212, -4.878523], [-74.023858, 102.791821, -4.958495], [-74.10335, 102.811847, -4.913698], [-68.5333, 100.398, -3.23683]]}, {"shapeName": "R_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-70.579735, 99.924247, 2.630742], [-70.49881, 99.959712, 2.661086], [-70.462888, 99.873609, 2.665919], [-70.543813, 99.838144, 2.635575], [-70.579735, 99.924247, 2.630742], [-70.542383, 99.893638, 2.710708], [-70.462888, 99.873609, 2.665919], [-70.500238, 99.904218, 2.585947], [-70.49881, 99.959712, 2.661086], [-70.542383, 99.893638, 2.710708], [-70.543813, 99.838144, 2.635575], [-70.500238, 99.904218, 2.585947], [-70.579735, 99.924247, 2.630742], [-70.542383, 99.893638, 2.710708], [-68.5333, 100.398, -3.23683]]}]},
			"C_neck_FK_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 170.322101, -0.266898], [-0.110097, 170.307546, -0.157766], [0.0, 170.292992, -0.048635], [0.110097, 170.307546, -0.157766], [0.0, 170.322101, -0.266898], [0.0, 170.416668, -0.143213], [0.0, 170.292992, -0.048635], [0.0, 170.198415, -0.172321], [-0.110097, 170.307546, -0.157766], [0.0, 170.416668, -0.143213], [0.110097, 170.307546, -0.157766], [0.0, 170.198415, -0.172321], [0.0, 170.322101, -0.266898], [0.0, 170.416668, -0.143213], [0.0, 160.012227, -1.5308]]}, {"shapeName": "C_neck_FK_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-10.386473, 160.026782, -1.639931], [-10.386473, 159.903096, -1.545354], [-10.386473, 159.997673, -1.421669], [-10.386473, 160.121359, -1.516246], [-10.386473, 160.026782, -1.639931], [-10.49656, 160.012227, -1.5308], [-10.386473, 159.997673, -1.421669], [-10.276375, 160.012227, -1.5308], [-10.386473, 159.903096, -1.545354], [-10.49656, 160.012227, -1.5308], [-10.386473, 160.121359, -1.516246], [-10.276375, 160.012227, -1.5308], [-10.386473, 160.026782, -1.639931], [-10.49656, 160.012227, -1.5308], [0.0, 160.012227, -1.5308]]}, {"shapeName": "C_neck_FK_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.110097, 158.639194, 8.764519], [0.0, 158.530063, 8.749965], [0.110097, 158.639194, 8.764519], [0.0, 158.748325, 8.779073], [-0.110097, 158.639194, 8.764519], [0.0, 158.624641, 8.87364], [0.110097, 158.639194, 8.764519], [0.0, 158.653748, 8.655388], [0.0, 158.530063, 8.749965], [0.0, 158.624641, 8.87364], [0.0, 158.748325, 8.779073], [0.0, 158.653748, 8.655388], [-0.110097, 158.639194, 8.764519], [0.0, 158.624641, 8.87364], [0.0, 160.012227, -1.5308]]}]},
			"R_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.088532, 106.537493, 0.229295], [-67.133521, 106.598802, 0.28356], [-67.101677, 106.554862, 0.359604], [-67.056688, 106.493554, 0.305338], [-67.088532, 106.537493, 0.229295], [-67.148435, 106.507207, 0.294264], [-67.101677, 106.554862, 0.359604], [-67.041769, 106.585152, 0.294634], [-67.133521, 106.598802, 0.28356], [-67.148435, 106.507207, 0.294264], [-67.056688, 106.493554, 0.305338], [-67.041769, 106.585152, 0.294634], [-67.088532, 106.537493, 0.229295], [-67.148435, 106.507207, 0.294264], [-62.0635, 110.223, 0.31192]]}, {"shapeName": "R_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.681137, 115.178804, -0.780527], [-65.634374, 115.226463, -0.715187], [-65.694282, 115.196173, -0.650218], [-65.741045, 115.148514, -0.715558], [-65.681137, 115.178804, -0.780527], [-65.726123, 115.240107, -0.726261], [-65.694282, 115.196173, -0.650218], [-65.649292, 115.134864, -0.704483], [-65.634374, 115.226463, -0.715187], [-65.726123, 115.240107, -0.726261], [-65.741045, 115.148514, -0.715558], [-65.649292, 115.134864, -0.704483], [-65.681137, 115.178804, -0.780527], [-65.726123, 115.240107, -0.726261], [-62.0635, 110.223, 0.31192]]}, {"shapeName": "R_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-62.721939, 111.094896, 6.447635], [-62.630186, 111.081247, 6.458709], [-62.645105, 110.989648, 6.469413], [-62.736857, 111.003298, 6.458339], [-62.721939, 111.094896, 6.447635], [-62.690093, 111.050956, 6.523672], [-62.645105, 110.989648, 6.469413], [-62.67695, 111.033588, 6.393369], [-62.630186, 111.081247, 6.458709], [-62.690093, 111.050956, 6.523672], [-62.736857, 111.003298, 6.458339], [-62.67695, 111.033588, 6.393369], [-62.721939, 111.094896, 6.447635], [-62.690093, 111.050956, 6.523672], [-62.0635, 110.223, 0.31192]]}]},
			"R_legBase_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.70308, 92.979434, 0.903787], [-9.77661, 90.138448, 0.783472], [-9.804696, 89.053286, 0.737516], [-9.758947, 89.855021, 7.465226], [-9.674501, 92.52084, 11.715095], [-9.583612, 96.032508, 11.863813], [-9.520998, 99.048662, 7.854573], [-9.510575, 100.417252, 1.218776], [-9.538661, 99.332089, 1.172819], [-9.612191, 96.491103, 1.052505], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146]]}]},
			"L_hand_CTL": {"color": 18, "shapes": [{"shapeName": "L_hand_CTLShape", "degree": 3, "form": 2, "points": [[66.505832, 112.678394, 1.313271], [65.790263, 112.678394, 1.016874], [65.074695, 112.678394, 1.313271], [64.778297, 112.678394, 2.02884], [65.074695, 112.678394, 2.744408], [65.790263, 112.678394, 3.040806], [66.505832, 112.678394, 2.744408], [66.802229, 112.678394, 2.02884]]}, {"shapeName": "L_hand_CTLShape1", "degree": 3, "form": 2, "points": [[65.790263, 113.393963, 1.313271], [65.790263, 112.678394, 1.016874], [65.790263, 111.962825, 1.313271], [65.790263, 111.666428, 2.02884], [65.790263, 111.962825, 2.744408], [65.790263, 112.678394, 3.040806], [65.790263, 113.393963, 2.744408], [65.790263, 113.69036, 2.02884]]}, {"shapeName": "L_hand_CTLShape2", "degree": 3, "form": 2, "points": [[65.074695, 113.393963, 2.02884], [64.778297, 112.678394, 2.02884], [65.074695, 111.962825, 2.02884], [65.790263, 111.666428, 2.02884], [66.505832, 111.962825, 2.02884], [66.802229, 112.678394, 2.02884], [66.505832, 113.393963, 2.02884], [65.790263, 113.69036, 2.02884]]}]},
			"C_torso_FK_E_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_E_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 128.788193, -8.19334], [0.0, 129.016366, -8.259357], [0.0, 129.201906, -8.407671], [0.0, 129.316574, -8.615694], [0.0, 129.342902, -8.851762], [0.0, 129.276886, -9.079935], [0.0, 129.128571, -9.265476], [0.0, 128.920548, -9.380144], [0.0, 128.68448, -9.406471], [0.0, 128.456307, -9.340455], [0.0, 128.270767, -9.192141], [0.0, 128.156099, -8.984118], [0.0, 128.129771, -8.74805], [0.0, 128.195787, -8.519877], [0.0, 128.344102, -8.334336], [0.0, 128.552125, -8.219668], [0.0, 128.788193, -8.19334], [0.0, 129.306754, -2.127687]]}]},
			"R_legBase_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.696588, 93.230268, 0.91441], [-9.759614, 90.795137, 0.811283], [-9.783687, 89.864998, 0.771892], [-9.744474, 90.5522, 6.5385], [-9.672091, 92.837187, 10.181245], [-9.594187, 95.847188, 10.308718], [-9.540518, 98.432463, 6.872226], [-9.531583, 99.60554, 1.1844], [-9.555657, 98.6754, 1.145009], [-9.618683, 96.24027, 1.041882], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146]]}]},
			"R_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-63.955517, 103.426315, 15.503258], [-63.870685, 103.441317, 15.539397], [-63.841305, 103.359911, 15.504222], [-63.926136, 103.344909, 15.468083], [-63.955517, 103.426315, 15.503258], [-63.916683, 103.362493, 15.559341], [-63.841305, 103.359911, 15.504222], [-63.880137, 103.423735, 15.448133], [-63.870685, 103.441317, 15.539397], [-63.916683, 103.362493, 15.559341], [-63.926136, 103.344909, 15.468083], [-63.880137, 103.423735, 15.448133], [-63.955517, 103.426315, 15.503258], [-63.916683, 103.362493, 15.559341], [-62.1745, 106.282, 10.2579]]}, {"shapeName": "R_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-59.61602, 110.862687, 13.621265], [-59.540641, 110.860107, 13.566141], [-59.501808, 110.796282, 13.622229], [-59.577188, 110.798862, 13.677353], [-59.61602, 110.862687, 13.621265], [-59.531191, 110.877684, 13.657401], [-59.501808, 110.796282, 13.622229], [-59.58664, 110.781281, 13.58609], [-59.540641, 110.860107, 13.566141], [-59.531191, 110.877684, 13.657401], [-59.577188, 110.798862, 13.677353], [-59.58664, 110.781281, 13.58609], [-59.61602, 110.862687, 13.621265], [-59.531191, 110.877684, 13.657401], [-62.1745, 106.282, 10.2579]]}, {"shapeName": "R_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-56.759455, 103.197937, 10.339021], [-56.768906, 103.180356, 10.247757], [-56.814905, 103.10153, 10.267707], [-56.805454, 103.119111, 10.35897], [-56.759455, 103.197937, 10.339021], [-56.730079, 103.116535, 10.303846], [-56.814905, 103.10153, 10.267707], [-56.844286, 103.182936, 10.302882], [-56.768906, 103.180356, 10.247757], [-56.730079, 103.116535, 10.303846], [-56.805454, 103.119111, 10.35897], [-56.844286, 103.182936, 10.302882], [-56.759455, 103.197937, 10.339021], [-56.730079, 103.116535, 10.303846], [-62.1745, 106.282, 10.2579]]}]},
			"R_wrist_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.853237, 103.334378, 3.08561], [-67.887766, 103.417374, 3.212742], [-67.784782, 103.334378, 3.294894], [-67.750253, 103.251383, 3.167762], [-67.853237, 103.334378, 3.08561], [-67.897885, 103.262044, 3.216052], [-67.784782, 103.334378, 3.294894], [-67.740127, 103.406719, 3.16445], [-67.887766, 103.417374, 3.212742], [-67.897885, 103.262044, 3.216052], [-67.750253, 103.251383, 3.167762], [-67.740127, 103.406719, 3.16445], [-67.853237, 103.334378, 3.08561], [-67.897885, 103.262044, 3.216052], [-60.377304, 110.158951, 0.75611]]}, {"shapeName": "R_wrist_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-66.897928, 117.988639, 2.773133], [-66.784817, 118.06098, 2.851973], [-66.829472, 117.988639, 2.982417], [-66.942582, 117.916298, 2.903577], [-66.897928, 117.988639, 2.773133], [-66.93245, 118.071627, 2.900263], [-66.829472, 117.988639, 2.982417], [-66.794943, 117.905644, 2.855285], [-66.784817, 118.06098, 2.851973], [-66.93245, 118.071627, 2.900263], [-66.942582, 117.916298, 2.903577], [-66.794943, 117.905644, 2.855285], [-66.897928, 117.988639, 2.773133], [-66.93245, 118.071627, 2.900263], [-60.377304, 110.158951, 0.75611]]}, {"shapeName": "R_wrist_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-57.21705, 110.241946, 10.650393], [-57.069411, 110.231292, 10.602101], [-57.079537, 110.075955, 10.605414], [-57.227176, 110.08661, 10.653706], [-57.21705, 110.241946, 10.650393], [-57.114069, 110.158951, 10.732536], [-57.079537, 110.075955, 10.605414], [-57.182521, 110.158951, 10.523262], [-57.069411, 110.231292, 10.602101], [-57.114069, 110.158951, 10.732536], [-57.227176, 110.08661, 10.653706], [-57.182521, 110.158951, 10.523262], [-57.21705, 110.241946, 10.650393], [-57.114069, 110.158951, 10.732536], [-60.377304, 110.158951, 0.75611]]}]},
			"R_reverseBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_reverseBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-22.391868, 2.833732, 8.722435], [-22.40051, 2.949541, 8.826149], [-22.410127, 2.845467, 8.941557], [-22.401485, 2.729659, 8.837843], [-22.391868, 2.833732, 8.722435], [-22.510704, 2.8396, 8.822854], [-22.410127, 2.845467, 8.941557], [-22.29128, 2.8396, 8.841139], [-22.40051, 2.949541, 8.826149], [-22.510704, 2.8396, 8.822854], [-22.401485, 2.729659, 8.837843], [-22.29128, 2.8396, 8.841139], [-22.391868, 2.833732, 8.722435], [-22.510704, 2.8396, 8.822854], [-12.0504, 2.8396, 9.69452]]}, {"shapeName": "R_reverseBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-11.995304, 13.205445, 9.033344], [-11.894716, 13.211312, 9.152048], [-12.013563, 13.21718, 9.252467], [-12.114151, 13.211312, 9.133763], [-11.995304, 13.205445, 9.033344], [-12.003946, 13.321243, 9.137059], [-12.013563, 13.21718, 9.252467], [-12.004921, 13.101371, 9.148753], [-11.894716, 13.211312, 9.152048], [-12.003946, 13.321243, 9.137059], [-12.114151, 13.211312, 9.133763], [-12.004921, 13.101371, 9.148753], [-11.995304, 13.205445, 9.033344], [-12.003946, 13.321243, 9.137059], [-12.0504, 2.8396, 9.69452]]}, {"shapeName": "R_reverseBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-12.911211, 3.503067, 20.024561], [-12.801981, 3.393126, 20.039551], [-12.912185, 3.283185, 20.036255], [-13.021415, 3.393126, 20.021265], [-12.911211, 3.503067, 20.024561], [-12.920827, 3.398993, 20.139959], [-12.912185, 3.283185, 20.036255], [-12.902568, 3.387258, 19.920847], [-12.801981, 3.393126, 20.039551], [-12.920827, 3.398993, 20.139959], [-13.021415, 3.393126, 20.021265], [-12.902568, 3.387258, 19.920847], [-12.911211, 3.503067, 20.024561], [-12.920827, 3.398993, 20.139959], [-12.0504, 2.8396, 9.69452]]}]},
			"R_leg_IK_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_CTLShape", "degree": 3, "form": 2, "points": [[-17.949727, 6.53346, -15.113494], [-12.002071, 6.53346, -19.252368], [-6.023667, 6.53346, -15.158033], [-3.516589, 6.53346, -5.228874], [-5.949435, 6.53346, 4.718733], [-11.897091, 6.53346, 8.857607], [-17.875495, 6.53346, 4.763272], [-20.382574, 6.53346, -5.165887]]}]},
			"C_neckBase_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[10.01796, 156.588122, -10.40967], [0.0, 152.8212, -14.400633], [-10.01796, 156.588122, -10.40967], [-14.167526, 159.70857, -1.571297], [-10.01796, 154.380925, 6.140398], [0.0, 149.699754, 9.004682], [10.01796, 154.380925, 6.140398], [14.167526, 159.70857, -1.571297]]}]},
			"R_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_D_CTLShape", "degree": 3, "form": 2, "points": [[-70.895352, 99.46899, -0.309774], [-71.518227, 99.646846, -0.734373], [-72.242659, 99.871014, -0.57678], [-72.644287, 100.01018, 0.070691], [-72.487842, 99.982822, 0.828759], [-71.864967, 99.804967, 1.253357], [-71.140534, 99.580798, 1.095764], [-70.738907, 99.441633, 0.448294]]}]},
			"R_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_A_CTLShape", "degree": 3, "form": 2, "points": [[-62.196073, 109.718417, 0.751634], [-62.51604, 110.296508, 0.347502], [-62.777914, 111.005026, 0.518714], [-62.828294, 111.428931, 1.164977], [-62.637667, 111.319907, 1.907719], [-62.317701, 110.741816, 2.31185], [-62.055827, 110.033298, 2.140639], [-62.005447, 109.609392, 1.494376]]}]},
			"C_head_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 179.469603, -0.431158], [-0.110097, 179.469603, -0.32106], [0.0, 179.469603, -0.210963], [0.110097, 179.469603, -0.32106], [0.0, 179.469603, -0.431158], [0.0, 179.57969, -0.32106], [0.0, 179.469603, -0.210963], [0.0, 179.359505, -0.32106], [-0.110097, 179.469603, -0.32106], [0.0, 179.57969, -0.32106], [0.110097, 179.469603, -0.32106], [0.0, 179.359505, -0.32106], [0.0, 179.469603, -0.431158], [0.0, 179.57969, -0.32106], [0.0, 169.08313, -0.32106]]}, {"shapeName": "C_head_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-10.386473, 169.08313, -0.431158], [-10.386473, 168.973032, -0.32106], [-10.386473, 169.08313, -0.210963], [-10.386473, 169.193227, -0.32106], [-10.386473, 169.08313, -0.431158], [-10.49656, 169.08313, -0.32106], [-10.386473, 169.08313, -0.210963], [-10.276375, 169.08313, -0.32106], [-10.386473, 168.973032, -0.32106], [-10.49656, 169.08313, -0.32106], [-10.386473, 169.193227, -0.32106], [-10.276375, 169.08313, -0.32106], [-10.386473, 169.08313, -0.431158], [-10.49656, 169.08313, -0.32106], [0.0, 169.08313, -0.32106]]}, {"shapeName": "C_head_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.110097, 169.08313, 10.065412], [0.0, 168.973032, 10.065412], [0.110097, 169.08313, 10.065412], [0.0, 169.193227, 10.065412], [-0.110097, 169.08313, 10.065412], [0.0, 169.08313, 10.1755], [0.110097, 169.08313, 10.065412], [0.0, 169.08313, 9.955315], [0.0, 168.973032, 10.065412], [0.0, 169.08313, 10.1755], [0.0, 169.193227, 10.065412], [0.0, 169.08313, 9.955315], [-0.110097, 169.08313, 10.065412], [0.0, 169.08313, 10.1755], [0.0, 169.08313, -0.32106]]}]},
			"C_midNeck_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_CTLShape", "degree": 3, "form": 2, "points": [[14.311372, 163.856522, -13.049842], [0.0, 164.509557, -17.946447], [-14.311372, 163.856522, -13.049842], [-20.239323, 162.279953, -1.228365], [-14.311372, 160.703384, 10.593112], [0.0, 160.050349, 15.489717], [14.311372, 160.703384, 10.593112], [20.239323, 162.279953, -1.228365]]}]},
			"C_chest_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[7.728141, 135.51047, -9.082182], [0.0, 138.864291, -11.665758], [-7.728141, 135.51047, -9.082182], [-10.929234, 132.061231, -2.727274], [-7.728141, 135.184689, 3.793932], [0.0, 138.403567, 6.543805], [7.728141, 135.184689, 3.793932], [10.929234, 132.061231, -2.727274]]}]},
			"C_head_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[7.155686, 176.238816, -0.32106], [0.0, 179.202791, -0.32106], [-7.155686, 176.238816, -0.32106], [-10.119662, 169.08313, -0.32106], [-7.155686, 161.927444, -0.32106], [0.0, 158.963468, -0.32106], [7.155686, 161.927444, -0.32106], [10.119662, 169.08313, -0.32106]]}]},
			"R_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-69.399156, 100.339228, -3.583216], [-69.474602, 100.368469, -3.536522], [-69.441164, 100.329844, -3.458308], [-69.365719, 100.300603, -3.505002], [-69.399156, 100.339228, -3.583216], [-69.45112, 100.278059, -3.535417], [-69.441164, 100.329844, -3.458308], [-69.389198, 100.391018, -3.506105], [-69.474602, 100.368469, -3.536522], [-69.45112, 100.278059, -3.535417], [-69.365719, 100.300603, -3.505002], [-69.389198, 100.391018, -3.506105], [-69.399156, 100.339228, -3.583216], [-69.45112, 100.278059, -3.535417], [-66.4992, 105.663, -2.13807]]}, {"shapeName": "R_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-71.614147, 108.868925, -3.687295], [-71.604189, 108.920715, -3.610184], [-71.656156, 108.859541, -3.562387], [-71.666114, 108.807751, -3.639498], [-71.614147, 108.868925, -3.687295], [-71.689588, 108.898163, -3.6406], [-71.656156, 108.859541, -3.562387], [-71.58071, 108.8303, -3.609081], [-71.604189, 108.920715, -3.610184], [-71.689588, 108.898163, -3.6406], [-71.666114, 108.807751, -3.639498], [-71.58071, 108.8303, -3.609081], [-71.614147, 108.868925, -3.687295], [-71.689588, 108.898163, -3.6406], [-66.4992, 105.663, -2.13807]]}, {"shapeName": "R_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-68.53515, 105.254268, 3.738033], [-68.449746, 105.276817, 3.76845], [-68.426267, 105.186401, 3.769553], [-68.511671, 105.163852, 3.739136], [-68.53515, 105.254268, 3.738033], [-68.501711, 105.215643, 3.816241], [-68.426267, 105.186401, 3.769553], [-68.459704, 105.225027, 3.691339], [-68.449746, 105.276817, 3.76845], [-68.501711, 105.215643, 3.816241], [-68.511671, 105.163852, 3.739136], [-68.459704, 105.225027, 3.691339], [-68.53515, 105.254268, 3.738033], [-68.501711, 105.215643, 3.816241], [-66.4992, 105.663, -2.13807]]}]},
			"L_reverseBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_reverseBall_CTLShape", "degree": 1, "form": 0, "points": [[12.062765, 0.053335, 9.84271], [12.03021, 7.398949, 9.452037], [11.941582, 8.358065, 8.388463], [13.036845, 8.412137, 9.313894], [12.02123, 9.425325, 9.344266], [11.941582, 8.358065, 8.388463], [11.014595, 8.412137, 9.482409], [12.03021, 7.398949, 9.452037], [12.109858, 8.46621, 10.40784], [11.014595, 8.412137, 9.482409], [12.02123, 9.425325, 9.344266], [12.109858, 8.46621, 10.40784], [13.036845, 8.412137, 9.313894], [12.03021, 7.398949, 9.452037]]}]},
			"R_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-61.63932, 107.643302, 9.434696], [-61.551908, 107.662608, 9.461415], [-61.524956, 107.577152, 9.434987], [-61.612368, 107.557847, 9.408268], [-61.63932, 107.643302, 9.434696], [-61.595557, 107.587293, 9.495314], [-61.524956, 107.577152, 9.434987], [-61.568718, 107.633163, 9.374364], [-61.551908, 107.662608, 9.461415], [-61.595557, 107.587293, 9.495314], [-61.612368, 107.557847, 9.408268], [-61.568718, 107.633163, 9.374364], [-61.63932, 107.643302, 9.434696], [-61.595557, 107.587293, 9.495314], [-60.3161, 109.774, 3.72944]]}, {"shapeName": "R_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-57.521388, 114.748583, 6.236201], [-57.450787, 114.738444, 6.175868], [-57.407025, 114.682433, 6.236491], [-57.477627, 114.692572, 6.296823], [-57.521388, 114.748583, 6.236201], [-57.433979, 114.767883, 6.262917], [-57.407025, 114.682433, 6.236491], [-57.494437, 114.663127, 6.209772], [-57.450787, 114.738444, 6.175868], [-57.433979, 114.767883, 6.262917], [-57.477627, 114.692572, 6.296823], [-57.494437, 114.663127, 6.209772], [-57.521388, 114.748583, 6.236201], [-57.433979, 114.767883, 6.262917], [-60.3161, 109.774, 3.72944]]}, {"shapeName": "R_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-54.891407, 106.70613, 3.769699], [-54.908217, 106.676686, 3.682648], [-54.951868, 106.601369, 3.716552], [-54.935058, 106.630814, 3.803603], [-54.891407, 106.70613, 3.769699], [-54.864461, 106.620678, 3.74327], [-54.951868, 106.601369, 3.716552], [-54.978819, 106.686825, 3.74298], [-54.908217, 106.676686, 3.682648], [-54.864461, 106.620678, 3.74327], [-54.935058, 106.630814, 3.803603], [-54.978819, 106.686825, 3.74298], [-54.891407, 106.70613, 3.769699], [-54.864461, 106.620678, 3.74327], [-60.3161, 109.774, 3.72944]]}]},
			"L_loLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_loLeg_FK_CTLShape", "degree": 3, "form": 2, "points": [[14.802503, 49.026969, 3.025461], [10.826535, 48.761842, 4.649194], [6.854425, 48.822514, 2.995778], [5.212985, 49.173445, -0.966248], [6.86374, 49.609063, -4.915978], [10.839708, 49.87419, -6.539711], [14.811817, 49.813518, -4.886295], [16.453257, 49.462587, -0.92427]]}]},
			"C_reverseJaw_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_reverseJaw_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.110097, 163.623924, 8.46193], [0.0, 163.705759, 8.535582], [-0.110097, 163.623924, 8.46193], [0.0, 163.542089, 8.388279], [0.110097, 163.623924, 8.46193], [0.0, 163.550279, 8.543758], [-0.110097, 163.623924, 8.46193], [0.0, 163.697575, 8.380095], [0.0, 163.705759, 8.535582], [0.0, 163.550279, 8.543758], [0.0, 163.542089, 8.388279], [0.0, 163.697575, 8.380095], [0.110097, 163.623924, 8.46193], [0.0, 163.550279, 8.543758], [0.0, 170.572105, 0.741723]]}, {"shapeName": "C_reverseJaw_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.110097, 178.292312, 7.689904], [0.0, 178.365963, 7.60807], [-0.110097, 178.292312, 7.689904], [0.0, 178.21866, 7.771739], [0.110097, 178.292312, 7.689904], [0.0, 178.374139, 7.763549], [-0.110097, 178.292312, 7.689904], [0.0, 178.210477, 7.616253], [0.0, 178.365963, 7.60807], [0.0, 178.374139, 7.763549], [0.0, 178.21866, 7.771739], [0.0, 178.210477, 7.616253], [0.110097, 178.292312, 7.689904], [0.0, 178.374139, 7.763549], [0.0, 170.572105, 0.741723]]}, {"shapeName": "C_reverseJaw_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-10.386473, 170.65394, 0.815375], [-10.386473, 170.645756, 0.659889], [-10.386473, 170.49027, 0.668072], [-10.386473, 170.498453, 0.823558], [-10.386473, 170.65394, 0.815375], [-10.49656, 170.572105, 0.741723], [-10.386473, 170.49027, 0.668072], [-10.276375, 170.572105, 0.741723], [-10.386473, 170.645756, 0.659889], [-10.49656, 170.572105, 0.741723], [-10.386473, 170.498453, 0.823558], [-10.276375, 170.572105, 0.741723], [-10.386473, 170.65394, 0.815375], [-10.49656, 170.572105, 0.741723], [0.0, 170.572105, 0.741723]]}]},
			"L_wrist_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[59.629253, 108.360882, -1.998159], [61.425992, 110.158951, -2.449958], [62.608424, 111.95702, -1.023688], [62.483894, 112.701803, 1.445164], [61.125355, 111.95702, 3.510379], [59.328617, 110.158951, 3.962178], [58.146184, 108.360882, 2.535909], [58.270714, 107.616099, 0.067056]]}]},
			"L_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[70.634987, 94.668591, -4.50256], [70.714484, 94.68862, -4.457765], [70.677133, 94.658011, -4.377793], [70.597636, 94.637982, -4.422588], [70.634987, 94.668591, -4.50256], [70.678559, 94.602523, -4.452931], [70.677133, 94.658011, -4.377793], [70.633558, 94.724085, -4.427421], [70.714484, 94.68862, -4.457765], [70.678559, 94.602523, -4.452931], [70.597636, 94.637982, -4.422588], [70.633558, 94.724085, -4.427421], [70.634987, 94.668591, -4.50256], [70.678559, 94.602523, -4.452931], [68.533301, 100.397603, -3.236828]]}, {"shapeName": "L_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[74.023859, 102.791424, -4.958493], [74.022431, 102.846918, -4.883354], [74.066005, 102.780844, -4.833726], [74.067434, 102.72535, -4.908865], [74.023859, 102.791424, -4.958493], [74.103351, 102.81145, -4.913696], [74.066005, 102.780844, -4.833726], [73.986508, 102.760815, -4.878521], [74.022431, 102.846918, -4.883354], [74.103351, 102.81145, -4.913696], [74.067434, 102.72535, -4.908865], [73.986508, 102.760815, -4.878521], [74.023859, 102.791424, -4.958493], [74.103351, 102.81145, -4.913696], [68.533301, 100.397603, -3.236828]]}, {"shapeName": "L_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[70.579736, 99.92385, 2.630744], [70.498811, 99.959315, 2.661088], [70.462889, 99.873212, 2.665921], [70.543814, 99.837747, 2.635577], [70.579736, 99.92385, 2.630744], [70.542384, 99.893241, 2.71071], [70.462889, 99.873212, 2.665921], [70.500239, 99.903821, 2.585949], [70.498811, 99.959315, 2.661088], [70.542384, 99.893241, 2.71071], [70.543814, 99.837747, 2.635577], [70.500239, 99.903821, 2.585949], [70.579736, 99.92385, 2.630744], [70.542384, 99.893241, 2.71071], [68.533301, 100.397603, -3.236828]]}]},
			"C_neckBase_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[11.449097, 156.745779, -11.591818], [0.0, 152.440725, -16.152918], [-11.449097, 156.745779, -11.591818], [-16.191458, 160.312005, -1.49082], [-11.449097, 154.223268, 7.322545], [0.0, 148.873358, 10.596013], [11.449097, 154.223268, 7.322545], [16.191458, 160.312005, -1.49082]]}]},
			"L_arm_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[65.024947, 114.315727, 2.276329], [64.863572, 114.120931, 2.223544], [64.643028, 114.258267, 2.151405], [64.473844, 114.169835, 2.096066], [64.444677, 113.901937, 2.086526], [64.199649, 113.884255, 2.006378], [64.136002, 114.145432, 1.98556], [63.956929, 114.208772, 1.926986], [63.756258, 114.041023, 1.861348], [63.57111, 114.210817, 1.800787], [63.701655, 114.442877, 1.843487], [63.617585, 114.620857, 1.815988], [63.362967, 114.651551, 1.732704], [63.346161, 114.909354, 1.727207], [63.594417, 114.976332, 1.80841], [63.65458, 115.164744, 1.828089], [63.49516, 115.375862, 1.775944], [63.656536, 115.570657, 1.828729], [63.877095, 115.43334, 1.900873], [64.046279, 115.521772, 1.956212], [64.075446, 115.78967, 1.965752], [64.320464, 115.80734, 2.045896], [64.384138, 115.546159, 2.066724], [64.563193, 115.482835, 2.125292], [64.763849, 115.650566, 2.190925], [64.948998, 115.480771, 2.251487], [64.818468, 115.24873, 2.208791], [64.902555, 115.070733, 2.236295], [65.157146, 115.040043, 2.31957], [65.173962, 114.782252, 2.325071], [64.925706, 114.715275, 2.243868], [64.865543, 114.526863, 2.224189], [65.024947, 114.315727, 2.276329]]}, {"shapeName": "L_arm_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[64.636187, 114.872935, 2.149168], [64.507779, 115.144822, 2.107166], [64.234253, 115.241538, 2.017697], [63.97586, 115.106425, 1.933178], [63.883936, 114.818672, 1.90311], [64.012343, 114.546785, 1.945112], [64.28587, 114.450069, 2.034581], [64.544252, 114.58517, 2.119096]]}, {"shapeName": "L_arm_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[63.663684, 114.12592, 1.831067], [60.377304, 110.158951, 0.75611]]}]},
			"R_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-73.525907, 94.587654, 5.422693], [-73.58373, 94.609936, 5.492604], [-73.511641, 94.61059, 5.55202], [-73.453818, 94.588308, 5.482109], [-73.525907, 94.587654, 5.422693], [-73.528447, 94.534978, 5.4998], [-73.511641, 94.61059, 5.55202], [-73.5091, 94.663273, 5.474913], [-73.58373, 94.609936, 5.492604], [-73.528447, 94.534978, 5.4998], [-73.453818, 94.588308, 5.482109], [-73.5091, 94.663273, 5.474913], [-73.525907, 94.587654, 5.422693], [-73.528447, 94.534978, 5.4998], [-72.6061, 100.651, 4.3134]]}, {"shapeName": "R_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-78.741088, 101.65969, 4.743762], [-78.72428, 101.735308, 4.795981], [-78.726822, 101.682626, 4.873088], [-78.743629, 101.607007, 4.820869], [-78.741088, 101.65969, 4.743762], [-78.798905, 101.68197, 4.813672], [-78.726822, 101.682626, 4.873088], [-78.668999, 101.660344, 4.803178], [-78.72428, 101.735308, 4.795981], [-78.798905, 101.68197, 4.813672], [-78.743629, 101.607007, 4.820869], [-78.668999, 101.660344, 4.803178], [-78.741088, 101.65969, 4.743762], [-78.798905, 101.68197, 4.813672], [-72.6061, 100.651, 4.3134]]}, {"shapeName": "R_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-71.998153, 101.743676, 10.418906], [-71.923523, 101.797013, 10.401214], [-71.868242, 101.722048, 10.408411], [-71.942872, 101.668712, 10.426102], [-71.998153, 101.743676, 10.418906], [-71.926065, 101.744329, 10.478316], [-71.868242, 101.722048, 10.408411], [-71.94033, 101.721394, 10.348995], [-71.923523, 101.797013, 10.401214], [-71.926065, 101.744329, 10.478316], [-71.942872, 101.668712, 10.426102], [-71.94033, 101.721394, 10.348995], [-71.998153, 101.743676, 10.418906], [-71.926065, 101.744329, 10.478316], [-72.6061, 100.651, 4.3134]]}]},
			"L_arm_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[59.396289, 113.594647, 2.997295], [56.354814, 109.923301, 2.002445], [57.868899, 109.923301, -2.626446], [60.910374, 113.594647, -1.631595], [64.399794, 110.394601, -0.490225], [61.358319, 106.723254, -1.485075], [59.844234, 106.723254, 3.143816], [62.885709, 110.394601, 4.138666], [59.396289, 113.594647, 2.997295], [60.910374, 113.594647, -1.631595], [57.868899, 109.923301, -2.626446], [61.358319, 106.723254, -1.485075], [64.399794, 110.394601, -0.490225], [62.885709, 110.394601, 4.138666], [59.844234, 106.723254, 3.143816], [56.354814, 109.923301, 2.002445]]}]},
			"R_leg_IK_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-17.349713, 6.53346, -14.121883], [-11.996822, 6.53346, -17.846869], [-6.616259, 6.53346, -14.161968], [-4.359888, 6.53346, -5.225725], [-6.54945, 6.53346, 3.727122], [-11.90234, 6.53346, 7.452108], [-17.282904, 6.53346, 3.767207], [-19.539274, 6.53346, -5.169036]]}]},
			"C_midTorso_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_CTLShape", "degree": 3, "form": 2, "points": [[8.586823, 119.635988, -8.482708], [0.0, 119.383515, -11.435911], [-8.586823, 119.635988, -8.482708], [-12.143594, 120.245514, -1.353029], [-8.586823, 120.85504, 5.77665], [0.0, 121.107513, 8.729853], [8.586823, 120.85504, 5.77665], [12.143594, 120.245514, -1.353029]]}]},
			"visibility_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "visibility_CTLShape", "degree": 3, "form": 2, "points": [[2.274043, 209.103428, 0.0], [0.5, 210.525876, 0.0], [-1.274043, 209.103428, 0.0], [-1.269384, 209.103428, 0.0], [-1.274043, 209.103428, 0.0], [0.5, 207.680981, 0.0], [2.274043, 209.103428, 0.0], [2.274043, 209.103428, 0.0]]}, {"shapeName": "visibility_CTLShape1", "degree": 3, "form": 2, "points": [[1.242516, 209.845944, 0.0], [0.5, 210.153503, 0.0], [-0.242516, 209.845944, 0.0], [-0.550074, 209.103428, 0.0], [-0.242516, 208.360913, 0.0], [0.5, 208.053354, 0.0], [1.242516, 208.360913, 0.0], [1.550074, 209.103428, 0.0]]}]},
			"R_toe_IK_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-14.435644, 5.220272, 9.841958], [-12.050417, 6.206127, 9.906967], [-9.66519, 5.21992, 9.847531], [-8.677199, 2.839354, 9.698465], [-9.66519, 0.458933, 9.54709], [-12.050417, -0.526921, 9.48208], [-14.435644, 0.459285, 9.541517], [-15.423635, 2.839851, 9.690583]]}]},
			"L_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_D_CTLShape", "degree": 3, "form": 2, "points": [[71.979742, 100.409534, 3.556106], [72.71537, 100.475218, 3.322809], [73.386989, 100.643811, 3.669787], [73.601174, 100.816555, 4.393786], [73.232458, 100.892258, 5.070697], [72.496831, 100.826574, 5.303993], [71.825211, 100.657981, 4.957015], [71.611027, 100.485237, 4.233016]]}]},
			"C_torso_FK_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 123.428708, -1.691464], [-0.066058, 123.434335, -1.625646], [0.0, 123.439962, -1.559827], [0.066058, 123.434335, -1.625646], [0.0, 123.428708, -1.691464], [0.0, 123.500147, -1.631272], [0.0, 123.439962, -1.559827], [0.0, 123.368516, -1.620019], [-0.066058, 123.434335, -1.625646], [0.0, 123.500147, -1.631272], [0.066058, 123.434335, -1.625646], [0.0, 123.368516, -1.620019], [0.0, 123.428708, -1.691464], [0.0, 123.500147, -1.631272], [0.0, 117.225101, -1.09481]]}, {"shapeName": "C_torso_FK_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 117.219474, -1.160628], [-6.231884, 117.159282, -1.089183], [-6.231884, 117.230728, -1.028991], [-6.231884, 117.290919, -1.100437], [-6.231884, 117.219474, -1.160628], [-6.297936, 117.225101, -1.09481], [-6.231884, 117.230728, -1.028991], [-6.165825, 117.225101, -1.09481], [-6.231884, 117.159282, -1.089183], [-6.297936, 117.225101, -1.09481], [-6.231884, 117.290919, -1.100437], [-6.165825, 117.225101, -1.09481], [-6.231884, 117.219474, -1.160628], [-6.297936, 117.225101, -1.09481], [0.0, 117.225101, -1.09481]]}, {"shapeName": "C_torso_FK_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 117.755936, 5.114424], [0.0, 117.690118, 5.120051], [0.066058, 117.755936, 5.114424], [0.0, 117.821755, 5.108797], [-0.066058, 117.755936, 5.114424], [0.0, 117.761563, 5.180236], [0.066058, 117.755936, 5.114424], [0.0, 117.75031, 5.048606], [0.0, 117.690118, 5.120051], [0.0, 117.761563, 5.180236], [0.0, 117.821755, 5.108797], [0.0, 117.75031, 5.048606], [-0.066058, 117.755936, 5.114424], [0.0, 117.761563, 5.180236], [0.0, 117.225101, -1.09481]]}]},
			"L_shoulder_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [4.392193, 149.026346, 5.414114], [7.14373, 149.651168, 3.799622], [8.194726, 149.889829, 3.182939], [3.27571, 149.651168, -2.792546], [-1.866398, 149.026346, -5.252241], [-5.267502, 148.254019, -3.256609], [-5.628469, 147.629197, 2.432071], [-2.811445, 147.390536, 9.64092], [-1.760448, 147.629197, 9.024238], [0.991089, 148.254019, 7.409745], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193]]}]},
			"L_leg_PV_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_PV_CTLShape", "degree": 1, "form": 0, "points": [[9.62292, 43.240931, 101.284039], [9.62292, 41.211671, 101.284039], [9.62292, 41.211671, 99.254779], [9.62292, 43.240931, 99.254779], [11.65218, 43.240931, 99.254779], [11.65218, 41.211671, 99.254779], [11.65218, 41.211671, 101.284039], [11.65218, 43.240931, 101.284039], [9.62292, 43.240931, 101.284039], [9.62292, 43.240931, 99.254779], [9.62292, 41.211671, 99.254779], [11.65218, 41.211671, 99.254779], [11.65218, 43.240931, 99.254779], [11.65218, 43.240931, 101.284039], [11.65218, 41.211671, 101.284039], [9.62292, 41.211671, 101.284039]]}]},
			"R_shoulder_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-4.392193, 149.026346, 5.414114], [-7.14373, 149.651168, 3.799622], [-8.194726, 149.889829, 3.182939], [-3.27571, 149.651168, -2.792546], [1.866398, 149.026346, -5.252241], [5.267502, 148.254019, -3.256609], [5.628469, 147.629197, 2.432071], [2.811445, 147.390536, 9.64092], [1.760448, 147.629197, 9.024238], [-0.991089, 148.254019, 7.409745], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193]]}]},
			"R_legBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-9.925836, 84.356899, 0.648821], [-9.816067, 84.358734, 0.538412], [-9.926418, 84.366231, 0.428825], [-10.036187, 84.364396, 0.539234], [-9.925836, 84.356899, 0.648821], [-9.928973, 84.251613, 0.534167], [-9.926418, 84.366231, 0.428825], [-9.923281, 84.471527, 0.54348], [-9.816067, 84.358734, 0.538412], [-9.928973, 84.251613, 0.534167], [-10.036187, 84.364396, 0.539234], [-9.923281, 84.471527, 0.54348], [-9.925836, 84.356899, 0.648821], [-9.928973, 84.251613, 0.534167], [-9.657635, 94.735269, 0.978146]]}, {"shapeName": "R_legBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.725621, 94.463514, 1.049368], [0.728176, 94.578142, 0.944026], [0.725039, 94.472846, 0.829371], [0.722484, 94.358218, 0.934713], [0.725621, 94.463514, 1.049368], [0.83538, 94.465349, 0.938958], [0.725039, 94.472846, 0.829371], [0.61527, 94.471011, 0.939781], [0.728176, 94.578142, 0.944026], [0.83538, 94.465349, 0.938958], [0.722484, 94.358218, 0.934713], [0.61527, 94.471011, 0.939781], [0.725621, 94.463514, 1.049368], [0.83538, 94.465349, 0.938958], [-9.657635, 94.735269, 0.978146]]}, {"shapeName": "R_legBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-9.575007, 95.172614, -9.39937], [-9.682221, 95.285408, -9.394302], [-9.795127, 95.178277, -9.398548], [-9.687913, 95.065483, -9.403616], [-9.575007, 95.172614, -9.39937], [-9.685358, 95.180111, -9.508947], [-9.795127, 95.178277, -9.398548], [-9.684776, 95.170779, -9.288961], [-9.682221, 95.285408, -9.394302], [-9.685358, 95.180111, -9.508947], [-9.687913, 95.065483, -9.403616], [-9.684776, 95.170779, -9.288961], [-9.575007, 95.172614, -9.39937], [-9.685358, 95.180111, -9.508947], [-9.657635, 94.735269, 0.978146]]}]},
			"C_neckBase_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_CTLShape", "degree": 3, "form": 2, "points": [[14.311372, 157.061093, -13.956113], [0.0, 151.679775, -19.657489], [-14.311372, 157.061093, -13.956113], [-20.239323, 161.518876, -1.329866], [-14.311372, 153.907954, 9.686841], [0.0, 147.220567, 13.778676], [14.311372, 153.907954, 9.686841], [20.239323, 161.518876, -1.329866]]}]},
			"R_wrist_IK_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-59.379903, 107.761525, -2.916249], [-61.775554, 110.158951, -3.518647], [-63.35213, 112.556377, -1.616955], [-63.186091, 113.549421, 1.674849], [-61.374705, 112.556377, 4.428469], [-58.979054, 110.158951, 5.030867], [-57.402478, 107.761525, 3.129175], [-57.568517, 106.768481, -0.162629]]}]},
			"C_midNeck_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[12.880235, 163.698865, -11.867694], [0.0, 164.286597, -16.274639], [-12.880235, 163.698865, -11.867694], [-18.215391, 162.279953, -1.228365], [-12.880235, 160.861041, 9.410964], [0.0, 160.273309, 13.817909], [12.880235, 160.861041, 9.410964], [18.215391, 162.279953, -1.228365]]}]},
			"R_arm_IK_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-59.396289, 113.594647, 2.997295], [-56.354814, 109.923301, 2.002445], [-57.868899, 109.923301, -2.626446], [-60.910374, 113.594647, -1.631595], [-64.399794, 110.394601, -0.490225], [-61.358319, 106.723254, -1.485075], [-59.844234, 106.723254, 3.143816], [-62.885709, 110.394601, 4.138666], [-59.396289, 113.594647, 2.997295], [-60.910374, 113.594647, -1.631595], [-57.868899, 109.923301, -2.626446], [-61.358319, 106.723254, -1.485075], [-64.399794, 110.394601, -0.490225], [-62.885709, 110.394601, 4.138666], [-59.844234, 106.723254, 3.143816], [-56.354814, 109.923301, 2.002445]]}]},
			"L_arm_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.853237, 103.334378, 3.08561], [67.887766, 103.417374, 3.212742], [67.784782, 103.334378, 3.294894], [67.750253, 103.251383, 3.167762], [67.853237, 103.334378, 3.08561], [67.897885, 103.262044, 3.216052], [67.784782, 103.334378, 3.294894], [67.740127, 103.406719, 3.16445], [67.887766, 103.417374, 3.212742], [67.897885, 103.262044, 3.216052], [67.750253, 103.251383, 3.167762], [67.740127, 103.406719, 3.16445], [67.853237, 103.334378, 3.08561], [67.897885, 103.262044, 3.216052], [60.377304, 110.158951, 0.75611]]}, {"shapeName": "L_arm_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[66.897928, 117.988639, 2.773133], [66.784817, 118.06098, 2.851973], [66.829472, 117.988639, 2.982417], [66.942582, 117.916298, 2.903577], [66.897928, 117.988639, 2.773133], [66.93245, 118.071627, 2.900263], [66.829472, 117.988639, 2.982417], [66.794943, 117.905644, 2.855285], [66.784817, 118.06098, 2.851973], [66.93245, 118.071627, 2.900263], [66.942582, 117.916298, 2.903577], [66.794943, 117.905644, 2.855285], [66.897928, 117.988639, 2.773133], [66.93245, 118.071627, 2.900263], [60.377304, 110.158951, 0.75611]]}, {"shapeName": "L_arm_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[57.21705, 110.241946, 10.650393], [57.069411, 110.231292, 10.602101], [57.079537, 110.075955, 10.605414], [57.227176, 110.08661, 10.653706], [57.21705, 110.241946, 10.650393], [57.114069, 110.158951, 10.732536], [57.079537, 110.075955, 10.605414], [57.182521, 110.158951, 10.523262], [57.069411, 110.231292, 10.602101], [57.114069, 110.158951, 10.732536], [57.227176, 110.08661, 10.653706], [57.182521, 110.158951, 10.523262], [57.21705, 110.241946, 10.650393], [57.114069, 110.158951, 10.732536], [60.377304, 110.158951, 0.75611]]}]},
			"L_toe_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[14.435644, 5.220272, 9.841958], [12.050417, 6.206127, 9.906967], [9.66519, 5.21992, 9.847531], [8.677199, 2.839354, 9.698465], [9.66519, 0.458933, 9.54709], [12.050417, -0.526921, 9.48208], [14.435644, 0.459285, 9.541517], [15.423635, 2.839851, 9.690583]]}]},
			"C_torso_FK_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_A_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 104.641698, -6.129024], [0.0, 104.869871, -6.19504], [0.0, 105.055411, -6.343355], [0.0, 105.170079, -6.551378], [0.0, 105.196407, -6.787446], [0.0, 105.130391, -7.015619], [0.0, 104.982076, -7.201159], [0.0, 104.774053, -7.315827], [0.0, 104.537985, -7.342155], [0.0, 104.309812, -7.276139], [0.0, 104.124272, -7.127825], [0.0, 104.009604, -6.919801], [0.0, 103.983276, -6.683733], [0.0, 104.049292, -6.45556], [0.0, 104.197607, -6.27002], [0.0, 104.40563, -6.155352], [0.0, 104.641698, -6.129024], [0.0, 105.160259, -0.06337]]}]},
			"L_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[61.639341, 107.643621, 9.434692], [61.551929, 107.662927, 9.461411], [61.524977, 107.577471, 9.434983], [61.612389, 107.558166, 9.408264], [61.639341, 107.643621, 9.434692], [61.595578, 107.587612, 9.49531], [61.524977, 107.577471, 9.434983], [61.568739, 107.633482, 9.37436], [61.551929, 107.662927, 9.461411], [61.595578, 107.587612, 9.49531], [61.612389, 107.558166, 9.408264], [61.568739, 107.633482, 9.37436], [61.639341, 107.643621, 9.434692], [61.595578, 107.587612, 9.49531], [60.316121, 109.774319, 3.729436]]}, {"shapeName": "L_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[57.521409, 114.748902, 6.236197], [57.450808, 114.738763, 6.175864], [57.407046, 114.682752, 6.236487], [57.477648, 114.692891, 6.296819], [57.521409, 114.748902, 6.236197], [57.434, 114.768202, 6.262913], [57.407046, 114.682752, 6.236487], [57.494458, 114.663446, 6.209768], [57.450808, 114.738763, 6.175864], [57.434, 114.768202, 6.262913], [57.477648, 114.692891, 6.296819], [57.494458, 114.663446, 6.209768], [57.521409, 114.748902, 6.236197], [57.434, 114.768202, 6.262913], [60.316121, 109.774319, 3.729436]]}, {"shapeName": "L_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[54.891428, 106.706449, 3.769695], [54.908238, 106.677005, 3.682644], [54.951889, 106.601688, 3.716548], [54.935079, 106.631133, 3.803599], [54.891428, 106.706449, 3.769695], [54.864482, 106.620997, 3.743266], [54.951889, 106.601688, 3.716548], [54.97884, 106.687144, 3.742976], [54.908238, 106.677005, 3.682644], [54.864482, 106.620997, 3.743266], [54.935079, 106.631133, 3.803599], [54.97884, 106.687144, 3.742976], [54.891428, 106.706449, 3.769695], [54.864482, 106.620997, 3.743266], [60.316121, 109.774319, 3.729436]]}]},
			"L_leg_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[16.689283, 7.368325, -5.108802], [16.495544, 7.363341, -5.109526], [16.464016, 7.164569, -5.129324], [16.327826, 7.104266, -5.135479], [16.158319, 7.214051, -5.124765], [16.024881, 7.074203, -5.138825], [16.143829, 6.911456, -5.154864], [16.090388, 6.772975, -5.168694], [15.89252, 6.731349, -5.173065], [15.897551, 6.538554, -5.192226], [16.097324, 6.507157, -5.195112], [16.157916, 6.371628, -5.208515], [16.047616, 6.202966, -5.225412], [16.188169, 6.070165, -5.238449], [16.351722, 6.188518, -5.22649], [16.490875, 6.135297, -5.231618], [16.532728, 5.938413, -5.251142], [16.726467, 5.943397, -5.250418], [16.758013, 6.142169, -5.23062], [16.894204, 6.202473, -5.224465], [17.06371, 6.092688, -5.235179], [17.197136, 6.232535, -5.221119], [17.078199, 6.395301, -5.205078], [17.131642, 6.533764, -5.19125], [17.329491, 6.575389, -5.186879], [17.32446, 6.768184, -5.167718], [17.124705, 6.799581, -5.164831], [17.064113, 6.935129, -5.151427], [17.174401, 7.103773, -5.134532], [17.03386, 7.236573, -5.121495], [16.870307, 7.118221, -5.133453], [16.731155, 7.171441, -5.128326], [16.689283, 7.368325, -5.108802]]}, {"shapeName": "L_leg_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[16.81584, 6.868046, -5.158389], [16.908412, 6.661019, -5.178861], [16.826762, 6.449511, -5.199985], [16.618731, 6.357436, -5.209383], [16.406189, 6.438692, -5.201555], [16.313617, 6.645719, -5.181083], [16.395268, 6.857227, -5.159959], [16.603286, 6.949302, -5.150561]]}, {"shapeName": "L_leg_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[15.895035, 6.634952, -5.182646], [11.949581, 6.53346, -5.197381]]}]},
			"L_arm_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_CTLShape", "degree": 1, "form": 0, "points": [[58.742279, 115.885111, 4.491418], [53.673153, 109.766201, 2.833335], [56.196629, 109.766201, -4.881483], [61.265754, 115.885111, -3.223399], [67.081455, 110.5517, -1.321115], [62.012329, 104.43279, -2.979198], [59.488854, 104.43279, 4.735619], [64.557979, 110.5517, 6.393703], [58.742279, 115.885111, 4.491418], [61.265754, 115.885111, -3.223399], [56.196629, 109.766201, -4.881483], [62.012329, 104.43279, -2.979198], [67.081455, 110.5517, -1.321115], [64.557979, 110.5517, 6.393703], [59.488854, 104.43279, 4.735619], [53.673153, 109.766201, 2.833335]]}]},
			"L_legBase_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.709572, 92.728601, 0.893164], [9.793606, 89.48176, 0.755662], [9.825705, 88.241574, 0.70314], [9.77342, 89.157843, 8.391951], [9.67691, 92.204493, 13.248945], [9.573037, 96.217828, 13.418908], [9.501478, 99.664861, 8.83692], [9.489566, 101.228963, 1.253151], [9.521665, 99.988778, 1.20063], [9.605699, 96.741936, 1.063127], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146]]}]},
			"L_outterBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_outterBall_CTLShape", "degree": 1, "form": 0, "points": [[17.388502, 1.487226, 5.196293], [17.308854, 0.419965, 4.24049], [18.315489, 1.433153, 4.102346], [17.388502, 1.487226, 5.196293], [16.293238, 1.433153, 4.270862], [17.308854, 0.419965, 4.24049], [17.220226, 1.37908, 3.176916], [16.293238, 1.433153, 4.270862], [17.299874, 2.446341, 4.132718], [17.388502, 1.487226, 5.196293], [18.315489, 1.433153, 4.102346], [17.220226, 1.37908, 3.176916], [17.299874, 2.446341, 4.132718], [18.315489, 1.433153, 4.102346]]}]},
			"R_ankleOffset_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ankleOffset_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-22.335201, 6.525811, -5.37106], [-22.335525, 6.657324, -5.287711], [-22.336496, 6.573975, -5.156201], [-22.336172, 6.442462, -5.23955], [-22.335201, 6.525811, -5.37106], [-22.445933, 6.550067, -5.264333], [-22.336496, 6.573975, -5.156201], [-22.225753, 6.549719, -5.262928], [-22.335525, 6.657324, -5.287711], [-22.445933, 6.550067, -5.264333], [-22.336172, 6.442462, -5.23955], [-22.225753, 6.549719, -5.262928], [-22.335201, 6.525811, -5.37106], [-22.445933, 6.550067, -5.264333], [-11.9496, 6.53346, -5.19738]]}, {"shapeName": "R_ankleOffset_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-11.918427, 16.644328, -7.576518], [-11.808979, 16.668236, -7.468386], [-11.919721, 16.692492, -7.361659], [-12.029169, 16.668584, -7.469791], [-11.918427, 16.644328, -7.576518], [-11.91875, 16.775832, -7.493167], [-11.919721, 16.692492, -7.361659], [-11.919398, 16.560979, -7.445008], [-11.808979, 16.668236, -7.468386], [-11.91875, 16.775832, -7.493167], [-12.029169, 16.668584, -7.469791], [-11.919398, 16.560979, -7.445008], [-11.918427, 16.644328, -7.576518], [-11.91875, 16.775832, -7.493167], [-11.9496, 6.53346, -5.19738]]}, {"shapeName": "R_ankleOffset_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-12.010329, 8.912746, 4.91332], [-11.900557, 8.80514, 4.938103], [-12.010976, 8.697883, 4.961481], [-12.120748, 8.805489, 4.936698], [-12.010329, 8.912746, 4.91332], [-12.0113, 8.829394, 5.04482], [-12.010976, 8.697883, 4.961481], [-12.010005, 8.781233, 4.829971], [-11.900557, 8.80514, 4.938103], [-12.0113, 8.829394, 5.04482], [-12.120748, 8.805489, 4.936698], [-12.010005, 8.781233, 4.829971], [-12.010329, 8.912746, 4.91332], [-12.0113, 8.829394, 5.04482], [-11.9496, 6.53346, -5.19738]]}]},
			"C_midTorso_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[5.152094, 119.879798, -5.630836], [0.0, 119.728314, -7.402758], [-5.152094, 119.879798, -5.630836], [-7.286156, 120.245514, -1.353029], [-5.152094, 120.611229, 2.924778], [0.0, 120.762713, 4.6967], [5.152094, 120.611229, 2.924778], [7.286156, 120.245514, -1.353029]]}]},
			"L_toe_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[14.833182, 5.61705, 9.86653], [12.050417, 6.767214, 9.942375], [9.267652, 5.61664, 9.873032], [8.114996, 2.839313, 9.699121], [9.267652, 0.062155, 9.522518], [12.050417, -1.088009, 9.446673], [14.833182, 0.062565, 9.516016], [15.985838, 2.839893, 9.689926]]}]},
			"C_cog_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[32.850802, 102.099558, 2.302168], [32.816152, 102.099558, -2.865922], [23.898452, 102.099558, -5.969031], [22.67978, 102.099558, -9.636324], [27.966414, 102.099558, -17.458564], [24.900682, 102.099558, -21.619263], [15.86079, 102.099558, -18.893547], [12.720171, 102.099558, -21.144266], [12.399847, 102.099558, -30.574341], [7.473972, 102.099558, -32.138453], [1.764841, 102.099558, -24.624999], [-2.098118, 102.099558, -24.599456], [-7.903077, 102.099558, -32.035426], [-12.807517, 102.099558, -30.405467], [-13.005222, 102.099558, -20.974209], [-16.115004, 102.099558, -18.682167], [-25.187278, 102.099558, -21.283718], [-28.196992, 102.099558, -17.082288], [-22.807726, 102.099558, -9.335626], [-23.976495, 102.099558, -5.652586], [-32.850802, 102.099558, -2.426035], [-32.816152, 102.099558, 2.742056], [-23.898452, 102.099558, 5.845165], [-22.67978, 102.099558, 9.512458], [-27.966414, 102.099558, 17.334697], [-24.900682, 102.099558, 21.495397], [-15.86079, 102.099558, 18.769681], [-12.720171, 102.099558, 21.0204], [-12.399847, 102.099558, 30.450474], [-7.473972, 102.099558, 32.014587], [-1.764841, 102.099558, 24.501133], [2.098118, 102.099558, 24.47559], [7.903077, 102.099558, 31.91156], [12.807517, 102.099558, 30.281601], [13.005222, 102.099558, 20.850343], [16.115004, 102.099558, 18.558301], [25.187278, 102.099558, 21.159852], [28.196992, 102.099558, 16.958422], [22.807726, 102.099558, 9.21176], [23.976495, 102.099558, 5.52872], [32.850802, 102.099558, 2.302168]]}]},
			"L_arm_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[63.863036, 113.276533, 1.896274], [63.742005, 113.130436, 1.856686], [63.576597, 113.233438, 1.802582], [63.449709, 113.167114, 1.761077], [63.427834, 112.966191, 1.753922], [63.244063, 112.952929, 1.693811], [63.196328, 113.148812, 1.678198], [63.062023, 113.196317, 1.634267], [62.91152, 113.070505, 1.585038], [62.772658, 113.19785, 1.539618], [62.870567, 113.371895, 1.571643], [62.807515, 113.505381, 1.551019], [62.616551, 113.528401, 1.488556], [62.603947, 113.721754, 1.484433], [62.790139, 113.771987, 1.545335], [62.835261, 113.913296, 1.560095], [62.715696, 114.071634, 1.520986], [62.836728, 114.217731, 1.560574], [63.002147, 114.114743, 1.614682], [63.129035, 114.181067, 1.656186], [63.15091, 114.38199, 1.663342], [63.334674, 114.395243, 1.72345], [63.38243, 114.199357, 1.73907], [63.516721, 114.151864, 1.782996], [63.667213, 114.277662, 1.832222], [63.806075, 114.150316, 1.877642], [63.708177, 113.976285, 1.845621], [63.771243, 113.842788, 1.866249], [63.962185, 113.81977, 1.928705], [63.974797, 113.626427, 1.932831], [63.788605, 113.576194, 1.871928], [63.743483, 113.434885, 1.857169], [63.863036, 113.276533, 1.896274]]}, {"shapeName": "L_arm_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[63.571467, 113.694439, 1.800903], [63.475161, 113.898354, 1.769402], [63.270015, 113.970891, 1.7023], [63.076221, 113.869557, 1.638911], [63.007278, 113.653742, 1.61636], [63.103584, 113.449826, 1.647861], [63.308729, 113.37729, 1.714963], [63.502515, 113.478615, 1.77835]]}, {"shapeName": "L_arm_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[62.842089, 113.134178, 1.562328], [60.377304, 110.158951, 0.75611]]}]},
			"C_hip_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[7.728141, 101.550985, -6.478644], [0.0, 98.048306, -8.856504], [-7.728141, 101.550985, -6.478644], [-10.929234, 105.375011, -0.341956], [-7.728141, 102.648131, 6.354778], [0.0, 99.599904, 9.292683], [7.728141, 102.648131, 6.354778], [10.929234, 105.375011, -0.341956]]}]},
			"R_arm_IK_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-59.069284, 114.739879, 3.744357], [-55.013984, 109.844751, 2.41789], [-57.032764, 109.844751, -3.753964], [-61.088064, 114.739879, -2.427497], [-65.740625, 110.47315, -0.90567], [-61.685324, 105.578022, -2.232137], [-59.666544, 105.578022, 3.939717], [-63.721844, 110.47315, 5.266184], [-59.069284, 114.739879, 3.744357], [-61.088064, 114.739879, -2.427497], [-57.032764, 109.844751, -3.753964], [-61.685324, 105.578022, -2.232137], [-65.740625, 110.47315, -0.90567], [-63.721844, 110.47315, 5.266184], [-59.666544, 105.578022, 3.939717], [-55.013984, 109.844751, 2.41789]]}]},
			"L_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[72.472444, 98.593632, 9.745067], [72.502203, 98.637958, 9.821729], [72.420745, 98.619936, 9.863769], [72.390987, 98.57561, 9.787107], [72.472444, 98.593632, 9.745067], [72.471155, 98.550054, 9.827686], [72.420745, 98.619936, 9.863769], [72.422033, 98.66352, 9.781148], [72.502203, 98.637958, 9.821729], [72.471155, 98.550054, 9.827686], [72.390987, 98.57561, 9.787107], [72.422033, 98.66352, 9.781148], [72.472444, 98.593632, 9.745067], [72.471155, 98.550054, 9.827686], [70.129432, 103.959164, 7.609161]]}, {"shapeName": "L_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[75.401266, 106.886927, 9.182919], [75.350854, 106.956814, 9.219], [75.349567, 106.913231, 9.301621], [75.399979, 106.843343, 9.26554], [75.401266, 106.886927, 9.182919], [75.431019, 106.93125, 9.25958], [75.349567, 106.913231, 9.301621], [75.319809, 106.868905, 9.224959], [75.350854, 106.956814, 9.219], [75.431019, 106.93125, 9.25958], [75.399979, 106.843343, 9.26554], [75.319809, 106.868905, 9.224959], [75.401266, 106.886927, 9.182919], [75.431019, 106.93125, 9.25958], [70.129432, 103.959164, 7.609161]]}, {"shapeName": "L_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[67.746438, 105.231072, 13.225594], [67.666268, 105.256633, 13.185013], [67.635222, 105.168724, 13.190972], [67.715392, 105.143162, 13.231553], [67.746438, 105.231072, 13.225594], [67.664983, 105.213048, 13.267629], [67.635222, 105.168724, 13.190972], [67.716679, 105.186746, 13.148932], [67.666268, 105.256633, 13.185013], [67.664983, 105.213048, 13.267629], [67.715392, 105.143162, 13.231553], [67.716679, 105.186746, 13.148932], [67.746438, 105.231072, 13.225594], [67.664983, 105.213048, 13.267629], [70.129432, 103.959164, 7.609161]]}]},
			"L_leg_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[15.549669, 6.53346, -11.147049], [11.981075, 6.53346, -13.630373], [8.394033, 6.53346, -11.173772], [6.889786, 6.53346, -5.216277], [8.349494, 6.53346, 0.752288], [11.918087, 6.53346, 3.235612], [15.50513, 6.53346, 0.779011], [17.009377, 6.53346, -5.178484]]}]},
			"C_chest_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.010776, 135.474273, -7.651503], [0.0, 138.0828, -9.660951], [-6.010776, 135.474273, -7.651503], [-8.500516, 132.79153, -2.708796], [-6.010776, 135.220887, 2.363253], [0.0, 137.724459, 4.502043], [6.010776, 135.220887, 2.363253], [8.500516, 132.79153, -2.708796]]}]},
			"L_shoulder_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_CTLShape", "degree": 3, "form": 0, "points": [[2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [3.962608, 148.640182, 8.578006], [6.019065, 148.640182, 12.082773], [6.804564, 148.640182, 13.421479], [14.105637, 150.47649, 7.337897], [17.04696, 151.611392, 0.900631], [14.505026, 151.611392, -3.431521], [7.450787, 150.47649, -4.003791], [-1.421282, 148.640182, -0.597619], [-0.635784, 148.640182, 0.741086], [1.420674, 148.640182, 4.245854], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193]]}]},
			"C_chest_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_chest_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 141.579141, -2.552539], [-0.066058, 141.57747, -2.486501], [0.0, 141.575799, -2.420464], [0.066058, 141.57747, -2.486501], [0.0, 141.579141, -2.552539], [0.0, 141.643501, -2.484831], [0.0, 141.575799, -2.420464], [0.0, 141.511432, -2.488172], [-0.066058, 141.57747, -2.486501], [0.0, 141.643501, -2.484831], [0.066058, 141.57747, -2.486501], [0.0, 141.511432, -2.488172], [0.0, 141.579141, -2.552539], [0.0, 141.643501, -2.484831], [0.0, 135.34758, -2.644125]]}, {"shapeName": "C_chest_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 135.349251, -2.710162], [-6.231884, 135.281543, -2.645796], [-6.231884, 135.345909, -2.578088], [-6.231884, 135.413617, -2.642454], [-6.231884, 135.349251, -2.710162], [-6.297936, 135.34758, -2.644125], [-6.231884, 135.345909, -2.578088], [-6.165825, 135.34758, -2.644125], [-6.231884, 135.281543, -2.645796], [-6.297936, 135.34758, -2.644125], [-6.231884, 135.413617, -2.642454], [-6.165825, 135.34758, -2.644125], [-6.231884, 135.349251, -2.710162], [-6.297936, 135.34758, -2.644125], [0.0, 135.34758, -2.644125]]}, {"shapeName": "C_chest_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 135.189956, 3.585765], [0.0, 135.123919, 3.584094], [0.066058, 135.189956, 3.585765], [0.0, 135.255994, 3.587436], [-0.066058, 135.189956, 3.585765], [0.0, 135.188286, 3.651796], [0.066058, 135.189956, 3.585765], [0.0, 135.191627, 3.519728], [0.0, 135.123919, 3.584094], [0.0, 135.188286, 3.651796], [0.0, 135.255994, 3.587436], [0.0, 135.191627, 3.519728], [-0.066058, 135.189956, 3.585765], [0.0, 135.188286, 3.651796], [0.0, 135.34758, -2.644125]]}]},
			"L_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_C_CTLShape", "degree": 3, "form": 2, "points": [[63.093435, 106.119291, 9.866462], [63.049332, 106.790426, 10.250549], [62.492772, 107.16361, 10.638961], [61.749778, 107.020236, 10.804171], [61.255587, 106.444292, 10.649402], [61.29969, 105.773158, 10.265314], [61.85625, 105.399974, 9.876902], [62.599244, 105.543347, 9.711692]]}]},
			"C_midTorso_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_midTorso_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.231884, 120.239887, -1.418847], [6.231884, 120.311332, -1.358656], [6.231884, 120.251141, -1.287211], [6.231884, 120.179696, -1.347402], [6.231884, 120.239887, -1.418847], [6.297936, 120.245514, -1.353029], [6.231884, 120.251141, -1.287211], [6.165825, 120.245514, -1.353029], [6.231884, 120.311332, -1.358656], [6.297936, 120.245514, -1.353029], [6.231884, 120.179696, -1.347402], [6.165825, 120.245514, -1.353029], [6.231884, 120.239887, -1.418847], [6.297936, 120.245514, -1.353029], [0.0, 120.245514, -1.353029]]}, {"shapeName": "C_midTorso_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 126.449121, -1.949683], [-0.066058, 126.454748, -1.883865], [0.0, 126.460375, -1.818046], [0.066058, 126.454748, -1.883865], [0.0, 126.449121, -1.949683], [0.0, 126.52056, -1.889491], [0.0, 126.460375, -1.818046], [0.0, 126.388929, -1.878238], [-0.066058, 126.454748, -1.883865], [0.0, 126.52056, -1.889491], [0.066058, 126.454748, -1.883865], [0.0, 126.388929, -1.878238], [0.0, 126.449121, -1.949683], [0.0, 126.52056, -1.889491], [0.0, 120.245514, -1.353029]]}, {"shapeName": "C_midTorso_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 120.842168, 4.850578], [-0.066058, 120.77635, 4.856205], [0.0, 120.710531, 4.861832], [0.066058, 120.77635, 4.856205], [0.0, 120.842168, 4.850578], [0.0, 120.781976, 4.922017], [0.0, 120.710531, 4.861832], [0.0, 120.770723, 4.790387], [-0.066058, 120.77635, 4.856205], [0.0, 120.781976, 4.922017], [0.066058, 120.77635, 4.856205], [0.0, 120.770723, 4.790387], [0.0, 120.842168, 4.850578], [0.0, 120.781976, 4.922017], [0.0, 120.245514, -1.353029]]}]},
			"C_visibility_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_visibility_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.523671, 209.103428, -0.010851], [1.523671, 209.114279, 0.0], [1.523671, 209.103428, 0.010851], [1.523671, 209.092577, 0.0], [1.523671, 209.103428, -0.010851], [1.534521, 209.103428, 0.0], [1.523671, 209.103428, 0.010851], [1.51282, 209.103428, 0.0], [1.523671, 209.114279, 0.0], [1.534521, 209.103428, 0.0], [1.523671, 209.092577, 0.0], [1.51282, 209.103428, 0.0], [1.523671, 209.103428, -0.010851], [1.534521, 209.103428, 0.0], [0.5, 209.103428, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.5, 210.127099, -0.010851], [0.489149, 210.127099, 0.0], [0.5, 210.127099, 0.010851], [0.510851, 210.127099, 0.0], [0.5, 210.127099, -0.010851], [0.5, 210.137949, 0.0], [0.5, 210.127099, 0.010851], [0.5, 210.116248, 0.0], [0.489149, 210.127099, 0.0], [0.5, 210.137949, 0.0], [0.510851, 210.127099, 0.0], [0.5, 210.116248, 0.0], [0.5, 210.127099, -0.010851], [0.5, 210.137949, 0.0], [0.5, 209.103428, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.5, 209.114279, 1.023671], [0.489149, 209.103428, 1.023671], [0.5, 209.092577, 1.023671], [0.510851, 209.103428, 1.023671], [0.5, 209.114279, 1.023671], [0.5, 209.103428, 1.034521], [0.5, 209.092577, 1.023671], [0.5, 209.103428, 1.01282], [0.489149, 209.103428, 1.023671], [0.5, 209.103428, 1.034521], [0.510851, 209.103428, 1.023671], [0.5, 209.103428, 1.01282], [0.5, 209.114279, 1.023671], [0.5, 209.103428, 1.034521], [0.5, 209.103428, 0.0]]}]},
			"R_toe_IK_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-15.23072, 6.013829, 9.891102], [-12.050417, 7.328301, 9.977782], [-8.870114, 6.01336, 9.898533], [-7.552793, 2.839271, 9.699778], [-8.870114, -0.334623, 9.497945], [-12.050417, -1.649096, 9.411266], [-15.23072, -0.334154, 9.490514], [-16.548041, 2.839934, 9.689269]]}]},
			"L_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_C_CTLShape", "degree": 3, "form": 2, "points": [[69.807078, 103.479012, 6.778728], [70.525426, 103.757688, 6.699946], [71.011806, 104.154386, 7.153768], [70.981303, 104.436726, 7.874354], [70.451787, 104.439317, 8.439593], [69.733439, 104.160641, 8.518376], [69.247059, 103.763943, 8.064553], [69.277562, 103.481603, 7.343968]]}]},
			"L_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[73.525907, 94.58755, 5.422694], [73.58373, 94.609832, 5.492605], [73.511641, 94.610486, 5.552021], [73.453818, 94.588204, 5.48211], [73.525907, 94.58755, 5.422694], [73.528447, 94.534874, 5.499801], [73.511641, 94.610486, 5.552021], [73.5091, 94.663169, 5.474914], [73.58373, 94.609832, 5.492605], [73.528447, 94.534874, 5.499801], [73.453818, 94.588204, 5.48211], [73.5091, 94.663169, 5.474914], [73.525907, 94.58755, 5.422694], [73.528447, 94.534874, 5.499801], [72.6061, 100.650896, 4.313401]]}, {"shapeName": "L_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[78.741088, 101.659586, 4.743763], [78.72428, 101.735204, 4.795982], [78.726822, 101.682522, 4.873089], [78.743629, 101.606903, 4.82087], [78.741088, 101.659586, 4.743763], [78.798905, 101.681866, 4.813673], [78.726822, 101.682522, 4.873089], [78.668999, 101.66024, 4.803179], [78.72428, 101.735204, 4.795982], [78.798905, 101.681866, 4.813673], [78.743629, 101.606903, 4.82087], [78.668999, 101.66024, 4.803179], [78.741088, 101.659586, 4.743763], [78.798905, 101.681866, 4.813673], [72.6061, 100.650896, 4.313401]]}, {"shapeName": "L_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[71.998153, 101.743572, 10.418907], [71.923523, 101.796909, 10.401215], [71.868242, 101.721944, 10.408412], [71.942872, 101.668608, 10.426103], [71.998153, 101.743572, 10.418907], [71.926065, 101.744225, 10.478317], [71.868242, 101.721944, 10.408412], [71.94033, 101.72129, 10.348996], [71.923523, 101.796909, 10.401215], [71.926065, 101.744225, 10.478317], [71.942872, 101.668608, 10.426103], [71.94033, 101.72129, 10.348996], [71.998153, 101.743572, 10.418907], [71.926065, 101.744225, 10.478317], [72.6061, 100.650896, 4.313401]]}]},
			"R_wrist_IK_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-59.255228, 107.461847, -3.375294], [-61.950335, 110.158951, -4.052992], [-63.723984, 112.856055, -1.913588], [-63.53719, 113.973229, 1.789692], [-61.49938, 112.856055, 4.887514], [-58.804273, 110.158951, 5.565212], [-57.030624, 107.461847, 3.425808], [-57.217419, 106.344672, -0.277471]]}]},
			"R_leg_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-10.75971, 66.775053, -101.544964], [-10.649437, 66.764527, -101.435547], [-10.759285, 66.759663, -101.325308], [-10.869558, 66.770189, -101.434725], [-10.75971, 66.775053, -101.544964], [-10.756645, 66.87714, -101.42745], [-10.759285, 66.759663, -101.325308], [-10.76235, 66.657566, -101.442824], [-10.649437, 66.764527, -101.435547], [-10.756645, 66.87714, -101.42745], [-10.869558, 66.770189, -101.434725], [-10.76235, 66.657566, -101.442824], [-10.75971, 66.775053, -101.544964], [-10.756645, 66.87714, -101.42745], [-11.028643, 56.40973, -102.160335]]}, {"shapeName": "R_leg_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.64589, 56.150336, -102.308939], [-0.64853, 56.032849, -102.206799], [-0.645465, 56.134946, -102.089283], [-0.642825, 56.252433, -102.191424], [-0.64589, 56.150336, -102.308939], [-0.535627, 56.13981, -102.199522], [-0.645465, 56.134946, -102.089283], [-0.755737, 56.145472, -102.1987], [-0.64853, 56.032849, -102.206799], [-0.535627, 56.13981, -102.199522], [-0.642825, 56.252433, -102.191424], [-0.755737, 56.145472, -102.1987], [-0.64589, 56.150336, -102.308939], [-0.535627, 56.13981, -102.199522], [-11.028643, 56.40973, -102.160335]]}, {"shapeName": "R_leg_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-10.898562, 55.680941, -91.799694], [-11.011476, 55.57398, -91.80697], [-11.118683, 55.686602, -91.798872], [-11.00577, 55.793563, -91.791596], [-10.898562, 55.680941, -91.799694], [-11.008411, 55.676077, -91.689465], [-11.118683, 55.686602, -91.798872], [-11.008836, 55.691467, -91.909111], [-11.011476, 55.57398, -91.80697], [-11.008411, 55.676077, -91.689465], [-11.00577, 55.793563, -91.791596], [-11.008836, 55.691467, -91.909111], [-10.898562, 55.680941, -91.799694], [-11.008411, 55.676077, -91.689465], [-11.028643, 56.40973, -102.160335]]}]},
			"R_loLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_loLeg_FK_CTLShape", "degree": 3, "form": 2, "points": [[-14.802503, 49.026969, 3.025461], [-10.826535, 48.761842, 4.649194], [-6.854425, 48.822514, 2.995778], [-5.212985, 49.173445, -0.966248], [-6.86374, 49.609063, -4.915978], [-10.839708, 49.87419, -6.539711], [-14.811817, 49.813518, -4.886295], [-16.453257, 49.462587, -0.92427]]}]},
			"C_torso_FK_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_C_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 116.70654, -7.160464], [0.0, 116.934713, -7.22648], [0.0, 117.120254, -7.374794], [0.0, 117.234922, -7.582818], [0.0, 117.261249, -7.818885], [0.0, 117.195233, -8.047058], [0.0, 117.046919, -8.232599], [0.0, 116.838895, -8.347267], [0.0, 116.602828, -8.373595], [0.0, 116.374654, -8.307578], [0.0, 116.189114, -8.159264], [0.0, 116.074446, -7.951241], [0.0, 116.048118, -7.715173], [0.0, 116.114134, -7.487], [0.0, 116.262449, -7.301459], [0.0, 116.470472, -7.186791], [0.0, 116.70654, -7.160464], [0.0, 117.225101, -1.09481]]}]},
			"world_B_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -462.16], [205.32, 0.0, -256.64], [153.92, 0.0, -256.64], [153.92, 0.0, -153.88], [256.68, 0.0, -153.88], [256.68, 0.0, -205.28], [462.16, 0.0, 0.0], [256.64, 0.0, 205.32], [256.64, 0.0, 153.92], [153.88, 0.0, 153.92], [153.88, 0.0, 256.68], [205.28, 0.0, 256.68], [0.0, 0.0, 462.16], [-205.32, 0.0, 256.64], [-153.92, 0.0, 256.64], [-153.92, 0.0, 153.88], [-256.68, 0.0, 153.88], [-256.68, 0.0, 205.28], [-462.16, 0.0, 0.0], [-256.64, 0.0, -205.32], [-256.64, 0.0, -153.92], [-153.88, 0.0, -153.92], [-153.88, 0.0, -256.68], [-205.28, 0.0, -256.68], [0.0, 0.0, -462.16], [40.24, 0.56, -422.64], [36.72, 0.0, -418.88], [36.72, 0.0, -403.52], [33.52, 0.0, -403.52], [33.72, 0.0, -419.0], [31.44, 0.0, -417.84], [31.52, 0.0, -411.12], [28.28, 0.0, -411.12], [28.28, 0.0, -417.84], [26.28, 0.0, -419.0], [26.28, 0.0, -403.28], [23.04, 0.0, -403.28], [23.04, 0.0, -419.4], [25.64, 0.0, -422.0], [29.64, 0.0, -420.0], [34.04, 0.0, -422.0], [36.72, 0.0, -418.96], [34.04, 0.0, -422.0], [29.68, 0.0, -420.04], [25.64, 0.0, -421.96], [17.84, 0.0, -422.0], [20.48, 0.0, -419.4], [20.48, 0.0, -405.92], [17.84, 0.0, -403.28], [9.4, 0.0, -403.28], [6.8, 0.0, -405.92], [6.8, 0.0, -419.4], [9.4, 0.0, -422.0], [17.84, 0.0, -422.0], [16.84, 0.0, -419.0], [17.24, 0.0, -406.6], [10.0, 0.0, -406.68], [10.04, 0.0, -419.0], [16.88, 0.0, -419.08], [17.84, 0.0, -422.0], [9.4, 0.0, -422.0], [4.0, 0.0, -422.0], [4.2, 0.0, -403.28], [-4.92, 0.0, -403.28], [-7.56, 0.0, -405.92], [-7.56, 0.0, -411.56], [-4.88, 0.0, -414.16], [-4.72, 0.0, -414.36], [-9.96, 0.0, -421.92], [-9.96, 0.0, -422.0], [-6.2, 0.0, -422.0], [-0.96, 0.0, -414.4], [1.0, 0.0, -414.4], [1.0, 0.0, -406.4], [-4.04, 0.0, -406.4], [-4.08, 0.0, -411.16], [1.0, 0.0, -411.16], [1.0, 0.0, -422.0], [4.0, 0.0, -422.0], [-25.72, 0.0, -422.0], [-25.72, 0.0, -419.0], [-15.24, 0.0, -418.96], [-15.24, 0.0, -403.28], [-12.0, 0.0, -403.28], [-12.0, 0.0, -422.0], [-39.36, 0.0, -422.0], [-41.76, 0.0, -419.4], [-41.96, 0.0, -405.92], [-39.36, 0.0, -403.28], [-28.28, 0.0, -403.28], [-28.28, 0.0, -422.0], [-31.56, 0.0, -419.0], [-31.48, 0.0, -406.32], [-38.32, 0.0, -406.32], [-38.24, 0.0, -418.92], [-31.44, 0.0, -419.08], [-28.2, 0.0, -422.0]]}]},
			"L_upLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.925836, 84.356899, 0.648821], [9.816067, 84.358734, 0.538412], [9.926418, 84.366231, 0.428825], [10.036187, 84.364396, 0.539234], [9.925836, 84.356899, 0.648821], [9.928973, 84.251613, 0.534167], [9.926418, 84.366231, 0.428825], [9.923281, 84.471527, 0.54348], [9.816067, 84.358734, 0.538412], [9.928973, 84.251613, 0.534167], [10.036187, 84.364396, 0.539234], [9.923281, 84.471527, 0.54348], [9.925836, 84.356899, 0.648821], [9.928973, 84.251613, 0.534167], [9.657635, 94.735269, 0.978146]]}, {"shapeName": "L_upLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.725621, 94.463514, 1.049368], [-0.728176, 94.578142, 0.944026], [-0.725039, 94.472846, 0.829371], [-0.722484, 94.358218, 0.934713], [-0.725621, 94.463514, 1.049368], [-0.83538, 94.465349, 0.938958], [-0.725039, 94.472846, 0.829371], [-0.61527, 94.471011, 0.939781], [-0.728176, 94.578142, 0.944026], [-0.83538, 94.465349, 0.938958], [-0.722484, 94.358218, 0.934713], [-0.61527, 94.471011, 0.939781], [-0.725621, 94.463514, 1.049368], [-0.83538, 94.465349, 0.938958], [9.657635, 94.735269, 0.978146]]}, {"shapeName": "L_upLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.575007, 95.172614, -9.39937], [9.682221, 95.285408, -9.394302], [9.795127, 95.178277, -9.398548], [9.687913, 95.065483, -9.403616], [9.575007, 95.172614, -9.39937], [9.685358, 95.180111, -9.508947], [9.795127, 95.178277, -9.398548], [9.684776, 95.170779, -9.288961], [9.682221, 95.285408, -9.394302], [9.685358, 95.180111, -9.508947], [9.687913, 95.065483, -9.403616], [9.684776, 95.170779, -9.288961], [9.575007, 95.172614, -9.39937], [9.685358, 95.180111, -9.508947], [9.657635, 94.735269, 0.978146]]}]},
			"world_C_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -404.39], [179.655, 0.0, -224.56], [134.68, 0.0, -224.56], [134.68, 0.0, -134.645], [224.595, 0.0, -134.645], [224.595, 0.0, -179.62], [404.39, 0.0, 0.0], [224.56, 0.0, 179.655], [224.56, 0.0, 134.68], [134.645, 0.0, 134.68], [134.645, 0.0, 224.595], [179.62, 0.0, 224.595], [0.0, 0.0, 404.39], [-179.655, 0.0, 224.56], [-134.68, 0.0, 224.56], [-134.68, 0.0, 134.645], [-224.595, 0.0, 134.645], [-224.595, 0.0, 179.62], [-404.39, 0.0, 0.0], [-224.56, 0.0, -179.655], [-224.56, 0.0, -134.68], [-134.645, 0.0, -134.68], [-134.645, 0.0, -224.595], [-179.62, 0.0, -224.595], [0.0, 0.0, -404.39], [35.21, 0.49, -369.81], [32.13, 0.0, -366.52], [32.13, 0.0, -353.08], [29.33, 0.0, -353.08], [29.505, 0.0, -366.625], [27.51, 0.0, -365.61], [27.58, 0.0, -359.73], [24.745, 0.0, -359.73], [24.745, 0.0, -365.61], [22.995, 0.0, -366.625], [22.995, 0.0, -352.87], [20.16, 0.0, -352.87], [20.16, 0.0, -366.975], [22.435, 0.0, -369.25], [25.935, 0.0, -367.5], [29.785, 0.0, -369.25], [32.13, 0.0, -366.59], [29.785, 0.0, -369.25], [25.97, 0.0, -367.535], [22.435, 0.0, -369.215], [15.61, 0.0, -369.25], [17.92, 0.0, -366.975], [17.92, 0.0, -355.18], [15.61, 0.0, -352.87], [8.225, 0.0, -352.87], [5.95, 0.0, -355.18], [5.95, 0.0, -366.975], [8.225, 0.0, -369.25], [15.61, 0.0, -369.25], [14.735, 0.0, -366.625], [15.085, 0.0, -355.775], [8.75, 0.0, -355.845], [8.785, 0.0, -366.625], [14.77, 0.0, -366.695], [15.61, 0.0, -369.25], [8.225, 0.0, -369.25], [3.5, 0.0, -369.25], [3.675, 0.0, -352.87], [-4.305, 0.0, -352.87], [-6.615, 0.0, -355.18], [-6.615, 0.0, -360.115], [-4.27, 0.0, -362.39], [-4.13, 0.0, -362.565], [-8.715, 0.0, -369.18], [-8.715, 0.0, -369.25], [-5.425, 0.0, -369.25], [-0.84, 0.0, -362.6], [0.875, 0.0, -362.6], [0.875, 0.0, -355.6], [-3.535, 0.0, -355.6], [-3.57, 0.0, -359.765], [0.875, 0.0, -359.765], [0.875, 0.0, -369.25], [3.5, 0.0, -369.25], [-22.505, 0.0, -369.25], [-22.505, 0.0, -366.625], [-13.335, 0.0, -366.59], [-13.335, 0.0, -352.87], [-10.5, 0.0, -352.87], [-10.5, 0.0, -369.25], [-34.44, 0.0, -369.25], [-36.54, 0.0, -366.975], [-36.715, 0.0, -355.18], [-34.44, 0.0, -352.87], [-24.745, 0.0, -352.87], [-24.745, 0.0, -369.25], [-27.615, 0.0, -366.625], [-27.545, 0.0, -355.53], [-33.53, 0.0, -355.53], [-33.46, 0.0, -366.555], [-27.51, 0.0, -366.695], [-24.675, 0.0, -369.25]]}]},
			"C_torso_FK_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 129.469534, -2.207902], [-0.066058, 129.475161, -2.142084], [0.0, 129.480788, -2.076266], [0.066058, 129.475161, -2.142084], [0.0, 129.469534, -2.207902], [0.0, 129.540973, -2.14771], [0.0, 129.480788, -2.076266], [0.0, 129.409343, -2.136457], [-0.066058, 129.475161, -2.142084], [0.0, 129.540973, -2.14771], [0.066058, 129.475161, -2.142084], [0.0, 129.409343, -2.136457], [0.0, 129.469534, -2.207902], [0.0, 129.540973, -2.14771], [0.0, 123.265927, -1.611248]]}, {"shapeName": "C_torso_FK_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 123.2603, -1.677067], [-6.231884, 123.200109, -1.605621], [-6.231884, 123.271554, -1.54543], [-6.231884, 123.331746, -1.616875], [-6.231884, 123.2603, -1.677067], [-6.297936, 123.265927, -1.611248], [-6.231884, 123.271554, -1.54543], [-6.165825, 123.265927, -1.611248], [-6.231884, 123.200109, -1.605621], [-6.297936, 123.265927, -1.611248], [-6.231884, 123.331746, -1.616875], [-6.165825, 123.265927, -1.611248], [-6.231884, 123.2603, -1.677067], [-6.297936, 123.265927, -1.611248], [0.0, 123.265927, -1.611248]]}, {"shapeName": "C_torso_FK_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 123.796763, 4.597986], [0.0, 123.730944, 4.603613], [0.066058, 123.796763, 4.597986], [0.0, 123.862581, 4.592359], [-0.066058, 123.796763, 4.597986], [0.0, 123.802389, 4.663798], [0.066058, 123.796763, 4.597986], [0.0, 123.791136, 4.532167], [0.0, 123.730944, 4.603613], [0.0, 123.802389, 4.663798], [0.0, 123.862581, 4.592359], [0.0, 123.791136, 4.532167], [-0.066058, 123.796763, 4.597986], [0.0, 123.802389, 4.663798], [0.0, 123.265927, -1.611248]]}]},
			"R_toe_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_toe_FK_CTLShape", "degree": 3, "form": 2, "points": [[-16.025795, 6.807385, 9.940247], [-12.050417, 8.450476, 10.048596], [-8.075039, 6.806799, 9.949535], [-6.428387, 2.839188, 9.701092], [-8.075039, -1.12818, 9.448801], [-12.050417, -2.771271, 9.340451], [-16.025795, -1.127593, 9.439512], [-17.672447, 2.840017, 9.687956]]}]},
			"R_upArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_upArm_FK_CTLShape", "degree": 3, "form": 2, "points": [[-13.411151, 148.884544, -5.066038], [-15.764791, 151.565067, -7.472342], [-18.865229, 154.44082, -6.677076], [-20.896271, 155.827224, -3.146088], [-20.668164, 154.912148, 1.052212], [-18.314524, 152.231625, 3.458515], [-15.214086, 149.355872, 2.66325], [-13.183044, 147.969468, -0.867738]]}]},
			"R_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_A_CTLShape", "degree": 3, "form": 2, "points": [[-61.468832, 109.126256, -1.841721], [-61.746386, 109.495946, -2.463156], [-62.268911, 110.055727, -2.579358], [-62.730318, 110.477687, -2.122255], [-62.860323, 110.514648, -1.359613], [-62.582768, 110.144958, -0.738178], [-62.060243, 109.585176, -0.621976], [-61.598836, 109.163217, -1.079079]]}]},
			"L_arm_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[66.186858, 115.354921, 2.656384], [65.985138, 115.111427, 2.590402], [65.709459, 115.283096, 2.500229], [65.497979, 115.172556, 2.431055], [65.46152, 114.837684, 2.41913], [65.155235, 114.815581, 2.318945], [65.075677, 115.142052, 2.292922], [64.851836, 115.221228, 2.219705], [64.600997, 115.01154, 2.137657], [64.369561, 115.223784, 2.061956], [64.532743, 115.513858, 2.115332], [64.427655, 115.736334, 2.080958], [64.109383, 115.774701, 1.976853], [64.088375, 116.096955, 1.969981], [64.398695, 116.180677, 2.071485], [64.473899, 116.416193, 2.096084], [64.274625, 116.680089, 2.030903], [64.476344, 116.923584, 2.096884], [64.752042, 116.751937, 2.187063], [64.963523, 116.862477, 2.256237], [64.999981, 117.19735, 2.268163], [65.306254, 117.219437, 2.368343], [65.385846, 116.892961, 2.394377], [65.609666, 116.813806, 2.467587], [65.860486, 117.02347, 2.549629], [66.091922, 116.811227, 2.625331], [65.928759, 116.521175, 2.571961], [66.033868, 116.298679, 2.606342], [66.352106, 116.260317, 2.710436], [66.373126, 115.938078, 2.717311], [66.062806, 115.854356, 2.615807], [65.987602, 115.618841, 2.591208], [66.186858, 115.354921, 2.656384]]}, {"shapeName": "L_arm_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[65.700908, 116.051431, 2.497432], [65.540398, 116.39129, 2.44493], [65.19849, 116.512184, 2.333094], [64.8755, 116.343294, 2.227446], [64.760593, 115.983602, 2.18986], [64.921103, 115.643743, 2.242362], [65.263012, 115.522849, 2.354199], [65.585989, 115.691724, 2.459843]]}, {"shapeName": "L_arm_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[64.485279, 115.117662, 2.099806], [60.377304, 110.158951, 0.75611]]}]},
			"C_cog_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[21.900534, 102.099558, 1.514135], [21.877435, 102.099558, -1.931259], [15.932302, 102.099558, -3.999999], [15.119853, 102.099558, -6.444861], [18.644276, 102.099558, -11.659687], [16.600455, 102.099558, -14.433486], [10.57386, 102.099558, -12.616342], [8.480114, 102.099558, -14.116822], [8.266564, 102.099558, -20.403538], [4.982648, 102.099558, -21.44628], [1.176561, 102.099558, -16.437311], [-1.398745, 102.099558, -16.420282], [-5.268718, 102.099558, -21.377595], [-8.538345, 102.099558, -20.290956], [-8.670148, 102.099558, -14.00345], [-10.743336, 102.099558, -12.475423], [-16.791519, 102.099558, -14.20979], [-18.797995, 102.099558, -11.408836], [-15.20515, 102.099558, -6.244395], [-15.98433, 102.099558, -3.789035], [-21.900534, 102.099558, -1.638001], [-21.877435, 102.099558, 1.807393], [-15.932302, 102.099558, 3.876132], [-15.119853, 102.099558, 6.320994], [-18.644276, 102.099558, 11.535821], [-16.600455, 102.099558, 14.30962], [-10.57386, 102.099558, 12.492476], [-8.480114, 102.099558, 13.992956], [-8.266564, 102.099558, 20.279672], [-4.982648, 102.099558, 21.322414], [-1.176561, 102.099558, 16.313444], [1.398745, 102.099558, 16.296416], [5.268718, 102.099558, 21.253729], [8.538345, 102.099558, 20.167089], [8.670148, 102.099558, 13.879584], [10.743336, 102.099558, 12.351556], [16.791519, 102.099558, 14.085923], [18.797995, 102.099558, 11.28497], [15.20515, 102.099558, 6.120529], [15.98433, 102.099558, 3.665169], [21.900534, 102.099558, 1.514135]]}]},
			"R_toeTip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_toeTip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.716532, 2.434998, 17.171185], [-1.706915, 2.539071, 17.055776], [-1.698272, 2.423263, 16.952062], [-1.70789, 2.319189, 17.067471], [-1.716532, 2.434998, 17.171185], [-1.597695, 2.42913, 17.070765], [-1.698272, 2.423263, 16.952062], [-1.817119, 2.42913, 17.05248], [-1.706915, 2.539071, 17.055776], [-1.597695, 2.42913, 17.070765], [-1.70789, 2.319189, 17.067471], [-1.817119, 2.42913, 17.05248], [-1.716532, 2.434998, 17.171185], [-1.597695, 2.42913, 17.070765], [-12.058, 2.42913, 16.1991]]}, {"shapeName": "R_toeTip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-12.021163, 12.80671, 15.757047], [-12.12175, 12.800843, 15.638343], [-12.002903, 12.794975, 15.537925], [-11.902316, 12.800843, 15.656629], [-12.021163, 12.80671, 15.757047], [-12.011546, 12.910774, 15.641639], [-12.002903, 12.794975, 15.537925], [-12.012521, 12.690902, 15.653333], [-12.12175, 12.800843, 15.638343], [-12.011546, 12.910774, 15.641639], [-11.902316, 12.800843, 15.656629], [-12.012521, 12.690902, 15.653333], [-12.021163, 12.80671, 15.757047], [-12.011546, 12.910774, 15.641639], [-12.058, 2.42913, 16.1991]]}, {"shapeName": "R_toeTip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-11.196215, 1.985545, 5.857364], [-11.306419, 1.875604, 5.854068], [-11.197189, 1.765662, 5.869059], [-11.086984, 1.875604, 5.872354], [-11.196215, 1.985545, 5.857364], [-11.187573, 1.869737, 5.75366], [-11.197189, 1.765662, 5.869059], [-11.205832, 1.881471, 5.972772], [-11.306419, 1.875604, 5.854068], [-11.187573, 1.869737, 5.75366], [-11.086984, 1.875604, 5.872354], [-11.205832, 1.881471, 5.972772], [-11.196215, 1.985545, 5.857364], [-11.187573, 1.869737, 5.75366], [-12.058, 2.42913, 16.1991]]}]},
			"L_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_B_CTLShape", "degree": 3, "form": 2, "points": [[65.68196, 105.346002, -2.643882], [66.177446, 105.734633, -3.094825], [66.861419, 106.081157, -2.985316], [67.333216, 106.182584, -2.379503], [67.316467, 105.9795, -1.632263], [66.820981, 105.590869, -1.181321], [66.137008, 105.244345, -1.29083], [65.665211, 105.142918, -1.896643]]}]},
			"R_toe_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-12.038241, 3.383855, -0.67826], [-11.928144, 3.493725, -0.671198], [-12.038241, 3.603613, -0.664393], [-12.148339, 3.493742, -0.671455], [-12.038241, 3.383855, -0.67826], [-12.038112, 3.500667, -0.781195], [-12.038241, 3.603613, -0.664393], [-12.03837, 3.4868, -0.561448], [-11.928144, 3.493725, -0.671198], [-12.038112, 3.500667, -0.781195], [-12.148339, 3.493742, -0.671455], [-12.03837, 3.4868, -0.561448], [-12.038241, 3.383855, -0.67826], [-12.038112, 3.500667, -0.781195], [-12.0504, 2.8396, 9.69452]]}, {"shapeName": "R_toe_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.663934, 2.728955, 9.69972], [-1.664064, 2.8319, 9.816533], [-1.663934, 2.948713, 9.713588], [-1.663805, 2.845768, 9.596775], [-1.663934, 2.728955, 9.69972], [-1.553847, 2.838826, 9.706783], [-1.663934, 2.948713, 9.713588], [-1.774032, 2.838842, 9.706526], [-1.664064, 2.8319, 9.816533], [-1.553847, 2.838826, 9.706783], [-1.663805, 2.845768, 9.596775], [-1.774032, 2.838842, 9.706526], [-1.663934, 2.728955, 9.69972], [-1.553847, 2.838826, 9.706783], [-12.0504, 2.8396, 9.69452]]}, {"shapeName": "R_toe_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-11.940303, 13.205445, 10.348783], [-12.050529, 13.19852, 10.458533], [-12.160497, 13.205462, 10.348526], [-12.050271, 13.212388, 10.238776], [-11.940303, 13.205445, 10.348783], [-12.0504, 13.315323, 10.355588], [-12.160497, 13.205462, 10.348526], [-12.0504, 13.095575, 10.341721], [-12.050529, 13.19852, 10.458533], [-12.0504, 13.315323, 10.355588], [-12.050271, 13.212388, 10.238776], [-12.0504, 13.095575, 10.341721], [-11.940303, 13.205445, 10.348783], [-12.0504, 13.315323, 10.355588], [-12.0504, 2.8396, 9.69452]]}]},
			"L_leg_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[11.949992, 16.919932, -5.307477], [11.839484, 16.919932, -5.197792], [11.94917, 16.919932, -5.087284], [12.059678, 16.919932, -5.196969], [11.949992, 16.919932, -5.307477], [11.949581, 17.03002, -5.197381], [11.94917, 16.919932, -5.087284], [11.949581, 16.809835, -5.197381], [11.839484, 16.919932, -5.197792], [11.949581, 17.03002, -5.197381], [12.059678, 16.919932, -5.196969], [11.949581, 16.809835, -5.197381], [11.949992, 16.919932, -5.307477], [11.949581, 17.03002, -5.197381], [11.949581, 6.53346, -5.197381]]}, {"shapeName": "L_leg_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.563592, 6.53346, -5.346266], [1.563181, 6.423362, -5.23617], [1.56277, 6.53346, -5.126073], [1.563181, 6.643557, -5.23617], [1.563592, 6.53346, -5.346266], [1.453094, 6.53346, -5.236581], [1.56277, 6.53346, -5.126073], [1.673278, 6.53346, -5.235759], [1.563181, 6.423362, -5.23617], [1.453094, 6.53346, -5.236581], [1.563181, 6.643557, -5.23617], [1.673278, 6.53346, -5.235759], [1.563592, 6.53346, -5.346266], [1.453094, 6.53346, -5.236581], [11.949581, 6.53346, -5.197381]]}, {"shapeName": "L_leg_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[11.800695, 6.53346, 5.188609], [11.910792, 6.423362, 5.18902], [12.020889, 6.53346, 5.189431], [11.910792, 6.643557, 5.18902], [11.800695, 6.53346, 5.188609], [11.910381, 6.53346, 5.299106], [12.020889, 6.53346, 5.189431], [11.911203, 6.53346, 5.078923], [11.910792, 6.423362, 5.18902], [11.910381, 6.53346, 5.299106], [11.910792, 6.643557, 5.18902], [11.911203, 6.53346, 5.078923], [11.800695, 6.53346, 5.188609], [11.910381, 6.53346, 5.299106], [11.949581, 6.53346, -5.197381]]}]},
			"L_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_B_CTLShape", "degree": 3, "form": 2, "points": [[62.223365, 107.952185, 7.830568], [62.216261, 108.527043, 8.349584], [61.689735, 108.817932, 8.837482], [60.952218, 108.65445, 9.008458], [60.435738, 108.132364, 8.762358], [60.442843, 107.557505, 8.243342], [60.969369, 107.266617, 7.755444], [61.706885, 107.430099, 7.584468]]}]},
			"R_leg_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-19.059134, 7.785757, -5.064513], [-18.768526, 7.778282, -5.065599], [-18.721233, 7.480124, -5.095296], [-18.516948, 7.389669, -5.104529], [-18.262688, 7.554347, -5.088457], [-18.062531, 7.344574, -5.109547], [-18.240953, 7.100454, -5.133606], [-18.160791, 6.892732, -5.154351], [-17.863989, 6.830294, -5.160908], [-17.871536, 6.541101, -5.189649], [-18.171196, 6.494006, -5.193978], [-18.262084, 6.290712, -5.214082], [-18.096633, 6.037718, -5.239428], [-18.307463, 5.838518, -5.258983], [-18.552793, 6.016047, -5.241045], [-18.761521, 5.936216, -5.248736], [-18.824301, 5.64089, -5.278022], [-19.114909, 5.648366, -5.276937], [-19.16223, 5.946524, -5.24724], [-19.366515, 6.036979, -5.238007], [-19.620774, 5.872301, -5.254079], [-19.820914, 6.082073, -5.232988], [-19.642508, 6.326221, -5.208927], [-19.722672, 6.533916, -5.188184], [-20.019446, 6.596353, -5.181628], [-20.0119, 6.885546, -5.152886], [-19.712267, 6.932642, -5.148557], [-19.621378, 7.135964, -5.128451], [-19.786811, 7.388929, -5.103107], [-19.576, 7.58813, -5.083552], [-19.33067, 7.410601, -5.10149], [-19.121941, 7.490432, -5.093799], [-19.059134, 7.785757, -5.064513]]}, {"shapeName": "R_leg_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-19.248969, 7.035339, -5.138893], [-19.387827, 6.724799, -5.169602], [-19.265352, 6.407537, -5.201287], [-18.953306, 6.269424, -5.215384], [-18.634493, 6.391309, -5.203643], [-18.495636, 6.701849, -5.172934], [-18.618111, 7.019111, -5.141249], [-18.930139, 7.157224, -5.127151]]}, {"shapeName": "R_leg_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-17.867762, 6.685698, -5.175278], [-11.949581, 6.53346, -5.197381]]}]},
			"L_loLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[11.102607, 38.975053, -1.862549], [10.992676, 38.983113, -1.972517], [11.102865, 38.996836, -2.081664], [11.212796, 38.988776, -1.971695], [11.102607, 38.975053, -1.862549], [11.105594, 38.876434, -1.98299], [11.102865, 38.996836, -2.081664], [11.099878, 39.095465, -1.961222], [10.992676, 38.983113, -1.972517], [11.105594, 38.876434, -1.98299], [11.212796, 38.988776, -1.971695], [11.099878, 39.095465, -1.961222], [11.102607, 38.975053, -1.862549], [11.105594, 38.876434, -1.98299], [10.833121, 49.318016, -0.945259]]}, {"shapeName": "L_loLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.450027, 49.040035, -0.874478], [0.447298, 49.160448, -0.97315], [0.450285, 49.061819, -1.093592], [0.453014, 48.941406, -0.99492], [0.450027, 49.040035, -0.874478], [0.340106, 49.048096, -0.984446], [0.450285, 49.061819, -1.093592], [0.560216, 49.053758, -0.983624], [0.447298, 49.160448, -0.97315], [0.340106, 49.048096, -0.984446], [0.453014, 48.941406, -0.99492], [0.560216, 49.053758, -0.983624], [0.450027, 49.040035, -0.874478], [0.340106, 49.048096, -0.984446], [10.833121, 49.318016, -0.945259]]}, {"shapeName": "L_loLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[10.735229, 50.342693, -11.281186], [10.842431, 50.455045, -11.26989], [10.955349, 50.348355, -11.280364], [10.848147, 50.236003, -11.291659], [10.735229, 50.342693, -11.281186], [10.845418, 50.356414, -11.390322], [10.955349, 50.348355, -11.280364], [10.84516, 50.334632, -11.171217], [10.842431, 50.455045, -11.26989], [10.845418, 50.356414, -11.390322], [10.848147, 50.236003, -11.291659], [10.84516, 50.334632, -11.171217], [10.735229, 50.342693, -11.281186], [10.845418, 50.356414, -11.390322], [10.833121, 49.318016, -0.945259]]}]},
			"L_arm_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[65.605903, 114.835324, 2.466356], [65.424355, 114.616179, 2.406973], [65.176244, 114.770682, 2.325817], [64.985911, 114.671196, 2.263561], [64.953099, 114.36981, 2.252828], [64.677442, 114.349918, 2.162662], [64.60584, 114.643742, 2.139241], [64.404383, 114.715, 2.073346], [64.178627, 114.526282, 1.999502], [63.970335, 114.7173, 1.931371], [64.117199, 114.978368, 1.97941], [64.02262, 115.178596, 1.948473], [63.736175, 115.213126, 1.854779], [63.717268, 115.503155, 1.848594], [63.996556, 115.578505, 1.939948], [64.06424, 115.790468, 1.962087], [63.884892, 116.027975, 1.903423], [64.06644, 116.24712, 1.962807], [64.314568, 116.092638, 2.043968], [64.504901, 116.192124, 2.106225], [64.537714, 116.49351, 2.116958], [64.813359, 116.513389, 2.20712], [64.884992, 116.21956, 2.230551], [65.08643, 116.14832, 2.29644], [65.312168, 116.337018, 2.370277], [65.52046, 116.145999, 2.438409], [65.373613, 115.884952, 2.390376], [65.468212, 115.684706, 2.421319], [65.754626, 115.65018, 2.515003], [65.773544, 115.360165, 2.521191], [65.494256, 115.284815, 2.429838], [65.426572, 115.072852, 2.407699], [65.605903, 114.835324, 2.466356]]}, {"shapeName": "L_arm_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[65.168548, 115.462183, 2.3233], [65.024089, 115.768056, 2.276048], [64.716371, 115.876861, 2.175396], [64.42568, 115.724859, 2.080312], [64.322264, 115.401137, 2.046485], [64.466723, 115.095264, 2.093737], [64.774441, 114.986459, 2.19439], [65.065121, 115.138447, 2.28947]]}, {"shapeName": "L_arm_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[64.074481, 114.621791, 1.965437], [60.377304, 110.158951, 0.75611]]}]},
			"R_loArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_loArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-49.134106, 119.958825, -3.508523], [-49.203138, 120.072202, -3.427142], [-49.121121, 120.0317, -3.301143], [-49.052088, 119.918322, -3.382524], [-49.134106, 119.958825, -3.508523], [-49.207451, 119.925455, -3.375303], [-49.121121, 120.0317, -3.301143], [-49.047768, 120.065076, -3.434366], [-49.203138, 120.072202, -3.427142], [-49.207451, 119.925455, -3.375303], [-49.052088, 119.918322, -3.382524], [-49.047768, 120.065076, -3.434366], [-49.134106, 119.958825, -3.508523], [-49.207451, 119.925455, -3.375303], [-41.595081, 126.581429, -6.190904]]}, {"shapeName": "R_loArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-48.726505, 133.803428, -8.399172], [-48.640168, 133.90968, -8.325015], [-48.713521, 133.876303, -8.191792], [-48.799859, 133.770052, -8.26595], [-48.726505, 133.803428, -8.399172], [-48.795531, 133.916799, -8.317789], [-48.713521, 133.876303, -8.191792], [-48.644488, 133.762926, -8.273173], [-48.640168, 133.90968, -8.325015], [-48.795531, 133.916799, -8.317789], [-48.799859, 133.770052, -8.26595], [-48.644488, 133.762926, -8.273173], [-48.726505, 133.803428, -8.399172], [-48.795531, 133.916799, -8.317789], [-41.595081, 126.581429, -6.190904]]}, {"shapeName": "R_loArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-41.058134, 130.095856, 3.568779], [-40.902764, 130.08873, 3.561556], [-40.907085, 129.941976, 3.613397], [-41.062455, 129.949102, 3.620621], [-41.058134, 130.095856, 3.568779], [-40.976118, 130.05535, 3.694769], [-40.907085, 129.941976, 3.613397], [-40.989102, 129.982478, 3.487398], [-40.902764, 130.08873, 3.561556], [-40.976118, 130.05535, 3.694769], [-41.062455, 129.949102, 3.620621], [-40.989102, 129.982478, 3.487398], [-41.058134, 130.095856, 3.568779], [-40.976118, 130.05535, 3.694769], [-41.595081, 126.581429, -6.190904]]}]},
			"L_reverseBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_reverseBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[22.391885, 2.833735, 8.722439], [22.400527, 2.949544, 8.826153], [22.410144, 2.84547, 8.941561], [22.401502, 2.729662, 8.837847], [22.391885, 2.833735, 8.722439], [22.510721, 2.839603, 8.822858], [22.410144, 2.84547, 8.941561], [22.291297, 2.839603, 8.841143], [22.400527, 2.949544, 8.826153], [22.510721, 2.839603, 8.822858], [22.401502, 2.729662, 8.837847], [22.291297, 2.839603, 8.841143], [22.391885, 2.833735, 8.722439], [22.510721, 2.839603, 8.822858], [12.050417, 2.839603, 9.694524]]}, {"shapeName": "L_reverseBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[11.995321, 13.205448, 9.033348], [11.894733, 13.211315, 9.152052], [12.01358, 13.217183, 9.252471], [12.114168, 13.211315, 9.133767], [11.995321, 13.205448, 9.033348], [12.003963, 13.321246, 9.137063], [12.01358, 13.217183, 9.252471], [12.004938, 13.101374, 9.148757], [11.894733, 13.211315, 9.152052], [12.003963, 13.321246, 9.137063], [12.114168, 13.211315, 9.133767], [12.004938, 13.101374, 9.148757], [11.995321, 13.205448, 9.033348], [12.003963, 13.321246, 9.137063], [12.050417, 2.839603, 9.694524]]}, {"shapeName": "L_reverseBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[12.911228, 3.50307, 20.024565], [12.801998, 3.393129, 20.039555], [12.912202, 3.283188, 20.036259], [13.021432, 3.393129, 20.021269], [12.911228, 3.50307, 20.024565], [12.920844, 3.398996, 20.139963], [12.912202, 3.283188, 20.036259], [12.902585, 3.387261, 19.920851], [12.801998, 3.393129, 20.039555], [12.920844, 3.398996, 20.139963], [13.021432, 3.393129, 20.021269], [12.902585, 3.387261, 19.920851], [12.911228, 3.50307, 20.024565], [12.920844, 3.398996, 20.139963], [12.050417, 2.839603, 9.694524]]}]},
			"R_toe_IK_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-15.628257, 6.410607, 9.915674], [-12.050417, 7.889389, 10.013189], [-8.472576, 6.410079, 9.924034], [-6.99059, 2.83923, 9.700435], [-8.472576, -0.731401, 9.473373], [-12.050417, -2.210183, 9.375858], [-15.628257, -0.730874, 9.465013], [-17.110244, 2.839976, 9.688613]]}]},
			"R_outterBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_outterBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-4.940632, 1.439018, 5.327205], [-4.931016, 1.543091, 5.211797], [-4.922373, 1.427283, 5.108082], [-4.93199, 1.323209, 5.223491], [-4.940632, 1.439018, 5.327205], [-4.821795, 1.43315, 5.226785], [-4.922373, 1.427283, 5.108082], [-5.04122, 1.43315, 5.208501], [-4.931016, 1.543091, 5.211797], [-4.821795, 1.43315, 5.226785], [-4.93199, 1.323209, 5.223491], [-5.04122, 1.43315, 5.208501], [-4.940632, 1.439018, 5.327205], [-4.821795, 1.43315, 5.226785], [-15.2821, 1.43315, 4.35512]]}, {"shapeName": "R_outterBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-15.245263, 11.81073, 3.913067], [-15.345851, 11.804863, 3.794363], [-15.227004, 11.798995, 3.693945], [-15.126416, 11.804863, 3.812649], [-15.245263, 11.81073, 3.913067], [-15.235647, 11.914794, 3.797659], [-15.227004, 11.798995, 3.693945], [-15.236621, 11.694922, 3.809353], [-15.345851, 11.804863, 3.794363], [-15.235647, 11.914794, 3.797659], [-15.126416, 11.804863, 3.812649], [-15.236621, 11.694922, 3.809353], [-15.245263, 11.81073, 3.913067], [-15.235647, 11.914794, 3.797659], [-15.2821, 1.43315, 4.35512]]}, {"shapeName": "R_outterBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-14.420315, 0.989565, -5.986615], [-14.530519, 0.879624, -5.989911], [-14.42129, 0.769683, -5.974921], [-14.311085, 0.879624, -5.971626], [-14.420315, 0.989565, -5.986615], [-14.411673, 0.873757, -6.09032], [-14.42129, 0.769683, -5.974921], [-14.429932, 0.885491, -5.871207], [-14.530519, 0.879624, -5.989911], [-14.411673, 0.873757, -6.09032], [-14.311085, 0.879624, -5.971626], [-14.429932, 0.885491, -5.871207], [-14.420315, 0.989565, -5.986615], [-14.411673, 0.873757, -6.09032], [-15.2821, 1.43315, 4.35512]]}]},
			"R_heel_CTL": {"color": 20, "shapes": [{"shapeName": "R_heel_CTLShape", "degree": 1, "form": 0, "points": [[-9.735106, 0.936262, -11.677043], [-9.655458, -0.130999, -12.632846], [-10.662093, 0.882189, -12.770989], [-9.735106, 0.936262, -11.677043], [-8.639843, 0.882189, -12.602474], [-9.655458, -0.130999, -12.632846], [-9.56683, 0.828117, -13.69642], [-8.639843, 0.882189, -12.602474], [-9.646478, 1.895377, -12.740617], [-9.735106, 0.936262, -11.677043], [-10.662093, 0.882189, -12.770989], [-9.56683, 0.828117, -13.69642], [-9.646478, 1.895377, -12.740617], [-10.662093, 0.882189, -12.770989]]}]},
			"R_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_A_CTLShape", "degree": 3, "form": 2, "points": [[-61.262999, 109.565195, 3.440012], [-61.192102, 110.281002, 3.727213], [-60.608068, 110.700001, 4.015717], [-59.853016, 110.576747, 4.13652], [-59.369243, 109.983443, 4.01886], [-59.44014, 109.267636, 3.731658], [-60.024174, 108.848637, 3.443155], [-60.779227, 108.971891, 3.322351]]}]},
			"R_outterBall_CTL": {"color": 20, "shapes": [{"shapeName": "R_outterBall_CTLShape", "degree": 1, "form": 0, "points": [[-17.388502, 1.487226, 5.196293], [-17.308854, 0.419965, 4.24049], [-18.315489, 1.433153, 4.102346], [-17.388502, 1.487226, 5.196293], [-16.293238, 1.433153, 4.270862], [-17.308854, 0.419965, 4.24049], [-17.220226, 1.37908, 3.176916], [-16.293238, 1.433153, 4.270862], [-17.299874, 2.446341, 4.132718], [-17.388502, 1.487226, 5.196293], [-18.315489, 1.433153, 4.102346], [-17.220226, 1.37908, 3.176916], [-17.299874, 2.446341, 4.132718], [-18.315489, 1.433153, 4.102346]]}]},
			"L_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[69.399169, 100.338979, -3.583219], [69.474615, 100.36822, -3.536525], [69.441177, 100.329595, -3.458311], [69.365732, 100.300354, -3.505005], [69.399169, 100.338979, -3.583219], [69.451133, 100.27781, -3.53542], [69.441177, 100.329595, -3.458311], [69.389211, 100.390769, -3.506108], [69.474615, 100.36822, -3.536525], [69.451133, 100.27781, -3.53542], [69.365732, 100.300354, -3.505005], [69.389211, 100.390769, -3.506108], [69.399169, 100.338979, -3.583219], [69.451133, 100.27781, -3.53542], [66.499213, 105.662751, -2.138073]]}, {"shapeName": "L_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[71.61416, 108.868676, -3.687298], [71.604202, 108.920466, -3.610187], [71.656169, 108.859292, -3.56239], [71.666127, 108.807502, -3.639501], [71.61416, 108.868676, -3.687298], [71.689601, 108.897914, -3.640603], [71.656169, 108.859292, -3.56239], [71.580723, 108.830051, -3.609084], [71.604202, 108.920466, -3.610187], [71.689601, 108.897914, -3.640603], [71.666127, 108.807502, -3.639501], [71.580723, 108.830051, -3.609084], [71.61416, 108.868676, -3.687298], [71.689601, 108.897914, -3.640603], [66.499213, 105.662751, -2.138073]]}, {"shapeName": "L_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[68.535163, 105.254019, 3.73803], [68.449759, 105.276568, 3.768447], [68.42628, 105.186152, 3.76955], [68.511684, 105.163603, 3.739133], [68.535163, 105.254019, 3.73803], [68.501724, 105.215394, 3.816238], [68.42628, 105.186152, 3.76955], [68.459717, 105.224778, 3.691336], [68.449759, 105.276568, 3.768447], [68.501724, 105.215394, 3.816238], [68.511684, 105.163603, 3.739133], [68.459717, 105.224778, 3.691336], [68.535163, 105.254019, 3.73803], [68.501724, 105.215394, 3.816238], [66.499213, 105.662751, -2.138073]]}]},
			"L_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.088504, 106.537656, 0.229295], [67.133493, 106.598965, 0.28356], [67.101649, 106.555025, 0.359604], [67.05666, 106.493717, 0.305338], [67.088504, 106.537656, 0.229295], [67.148407, 106.50737, 0.294264], [67.101649, 106.555025, 0.359604], [67.041741, 106.585315, 0.294634], [67.133493, 106.598965, 0.28356], [67.148407, 106.50737, 0.294264], [67.05666, 106.493717, 0.305338], [67.041741, 106.585315, 0.294634], [67.088504, 106.537656, 0.229295], [67.148407, 106.50737, 0.294264], [62.063472, 110.223163, 0.31192]]}, {"shapeName": "L_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.681109, 115.178967, -0.780527], [65.634346, 115.226626, -0.715187], [65.694254, 115.196336, -0.650218], [65.741017, 115.148677, -0.715558], [65.681109, 115.178967, -0.780527], [65.726095, 115.24027, -0.726261], [65.694254, 115.196336, -0.650218], [65.649264, 115.135027, -0.704483], [65.634346, 115.226626, -0.715187], [65.726095, 115.24027, -0.726261], [65.741017, 115.148677, -0.715558], [65.649264, 115.135027, -0.704483], [65.681109, 115.178967, -0.780527], [65.726095, 115.24027, -0.726261], [62.063472, 110.223163, 0.31192]]}, {"shapeName": "L_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[62.721911, 111.095059, 6.447635], [62.630158, 111.08141, 6.458709], [62.645077, 110.989811, 6.469413], [62.736829, 111.003461, 6.458339], [62.721911, 111.095059, 6.447635], [62.690065, 111.051119, 6.523672], [62.645077, 110.989811, 6.469413], [62.676922, 111.033751, 6.393369], [62.630158, 111.08141, 6.458709], [62.690065, 111.051119, 6.523672], [62.736829, 111.003461, 6.458339], [62.676922, 111.033751, 6.393369], [62.721911, 111.095059, 6.447635], [62.690065, 111.051119, 6.523672], [62.063472, 110.223163, 0.31192]]}]},
			"R_shoulder_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-11.427124, 150.636498, 1.158646], [-11.464591, 150.744543, 1.264313], [-11.538559, 150.636498, 1.348562], [-11.501093, 150.528453, 1.242895], [-11.427124, 150.636498, 1.158646], [-11.576021, 150.657657, 1.198931], [-11.538559, 150.636498, 1.348562], [-11.389654, 150.615337, 1.308283], [-11.464591, 150.744543, 1.264313], [-11.576021, 150.657657, 1.198931], [-11.501093, 150.528453, 1.242895], [-11.389654, 150.615337, 1.308283], [-11.427124, 150.636498, 1.158646], [-11.576021, 150.657657, 1.198931], [-2.691641, 148.640182, 6.41193]]}, {"shapeName": "R_shoulder_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.914122, 158.833, 7.327256], [-0.876652, 158.811839, 7.476893], [-1.025557, 158.833, 7.517172], [-1.063027, 158.854162, 7.367535], [-0.914122, 158.833, 7.327256], [-0.95159, 158.941035, 7.432922], [-1.025557, 158.833, 7.517172], [-0.98809, 158.724956, 7.411505], [-0.876652, 158.811839, 7.476893], [-0.95159, 158.941035, 7.432922], [-1.063027, 158.854162, 7.367535], [-0.98809, 158.724956, 7.411505], [-0.914122, 158.833, 7.327256], [-0.95159, 158.941035, 7.432922], [-2.691641, 148.640182, 6.41193]]}, {"shapeName": "R_shoulder_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-7.929719, 148.748227, 15.380865], [-7.854783, 148.619021, 15.424835], [-7.966221, 148.532138, 15.359447], [-8.041157, 148.661344, 15.315477], [-7.929719, 148.748227, 15.380865], [-8.003682, 148.640182, 15.465105], [-7.966221, 148.532138, 15.359447], [-7.892252, 148.640182, 15.275198], [-7.854783, 148.619021, 15.424835], [-8.003682, 148.640182, 15.465105], [-8.041157, 148.661344, 15.315477], [-7.892252, 148.640182, 15.275198], [-7.929719, 148.748227, 15.380865], [-8.003682, 148.640182, 15.465105], [-2.691641, 148.640182, 6.41193]]}]},
			"C_torso_FK_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_B_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 110.665713, -6.644025], [0.0, 110.893887, -6.710041], [0.0, 111.079427, -6.858356], [0.0, 111.194095, -7.066379], [0.0, 111.220423, -7.302447], [0.0, 111.154407, -7.53062], [0.0, 111.006092, -7.716161], [0.0, 110.798069, -7.830829], [0.0, 110.562001, -7.857156], [0.0, 110.333828, -7.79114], [0.0, 110.148287, -7.642826], [0.0, 110.033619, -7.434802], [0.0, 110.007292, -7.198735], [0.0, 110.073308, -6.970562], [0.0, 110.221622, -6.785021], [0.0, 110.429646, -6.670353], [0.0, 110.665713, -6.644025], [0.0, 111.184274, -0.578372]]}]},
			"R_legBase_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.716064, 92.477768, 0.882541], [-9.810603, 88.825071, 0.727851], [-9.846713, 87.429862, 0.668764], [-9.787893, 88.460665, 9.318677], [-9.679319, 91.888146, 14.782795], [-9.562462, 96.403148, 14.974004], [-9.481959, 100.28106, 9.819266], [-9.468557, 102.040675, 1.287527], [-9.504668, 100.645466, 1.228441], [-9.599207, 96.99277, 1.07375], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146]]}]},
			"L_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[70.801146, 103.127819, 8.012547], [70.818824, 103.182934, 8.085877], [70.74372, 103.148751, 8.129675], [70.726041, 103.093636, 8.056344], [70.801146, 103.127819, 8.012547], [70.809673, 103.090743, 8.097865], [70.74372, 103.148751, 8.129675], [70.735189, 103.185832, 8.044354], [70.818824, 103.182934, 8.085877], [70.809673, 103.090743, 8.097865], [70.726041, 103.093636, 8.056344], [70.735189, 103.185832, 8.044354], [70.801146, 103.127819, 8.012547], [70.809673, 103.090743, 8.097865], [67.258904, 107.623795, 5.54689]]}, {"shapeName": "L_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[71.664151, 111.825427, 6.881361], [71.598194, 111.88344, 6.913168], [71.606725, 111.846359, 6.998489], [71.672682, 111.788346, 6.966682], [71.664151, 111.825427, 6.881361], [71.681825, 111.880538, 6.95469], [71.606725, 111.846359, 6.998489], [71.589046, 111.791245, 6.925159], [71.598194, 111.88344, 6.913168], [71.681825, 111.880538, 6.95469], [71.672682, 111.788346, 6.966682], [71.589046, 111.791245, 6.925159], [71.664151, 111.825427, 6.881361], [71.681825, 111.880538, 6.95469], [67.258904, 107.623795, 5.54689]]}, {"shapeName": "L_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[64.596526, 108.655764, 11.086522], [64.51289, 108.658662, 11.044999], [64.503742, 108.566467, 11.056989], [64.587378, 108.563568, 11.098513], [64.596526, 108.655764, 11.086522], [64.521423, 108.62158, 11.130314], [64.503742, 108.566467, 11.056989], [64.578847, 108.60065, 11.013192], [64.51289, 108.658662, 11.044999], [64.521423, 108.62158, 11.130314], [64.587378, 108.563568, 11.098513], [64.578847, 108.60065, 11.013192], [64.596526, 108.655764, 11.086522], [64.521423, 108.62158, 11.130314], [67.258904, 107.623795, 5.54689]]}]},
			"R_wrist_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_wrist_FK_CTLShape", "degree": 3, "form": 2, "points": [[-60.947959, 105.495478, -3.239875], [-63.942523, 108.49226, -3.992872], [-65.913244, 111.489042, -1.615757], [-65.705694, 112.730347, 2.498998], [-63.441462, 111.489042, 5.941022], [-60.446898, 108.49226, 6.69402], [-58.476178, 105.495478, 4.316905], [-58.683727, 104.254173, 0.20215]]}]},
			"R_heel_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_heel_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.522228, 0.996202, -9.695315], [0.531845, 1.100276, -9.810724], [0.540488, 0.984468, -9.914438], [0.53087, 0.880393, -9.799029], [0.522228, 0.996202, -9.695315], [0.641065, 0.990335, -9.795735], [0.540488, 0.984468, -9.914438], [0.421641, 0.990335, -9.81402], [0.531845, 1.100276, -9.810724], [0.641065, 0.990335, -9.795735], [0.53087, 0.880393, -9.799029], [0.421641, 0.990335, -9.81402], [0.522228, 0.996202, -9.695315], [0.641065, 0.990335, -9.795735], [-9.81924, 0.990336, -10.6674]]}, {"shapeName": "R_heel_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-9.782403, 11.367915, -11.109453], [-9.88299, 11.362047, -11.228157], [-9.764143, 11.356181, -11.328575], [-9.663556, 11.362048, -11.209871], [-9.782403, 11.367915, -11.109453], [-9.772786, 11.471978, -11.224861], [-9.764143, 11.356181, -11.328575], [-9.773761, 11.252107, -11.213167], [-9.88299, 11.362047, -11.228157], [-9.772786, 11.471978, -11.224861], [-9.663556, 11.362048, -11.209871], [-9.773761, 11.252107, -11.213167], [-9.782403, 11.367915, -11.109453], [-9.772786, 11.471978, -11.224861], [-9.81924, 0.990336, -10.6674]]}, {"shapeName": "R_heel_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-8.957455, 0.54675, -21.009136], [-9.067659, 0.436809, -21.012432], [-8.958429, 0.326868, -20.997441], [-8.848224, 0.436809, -20.994146], [-8.957455, 0.54675, -21.009136], [-8.948813, 0.430942, -21.11284], [-8.958429, 0.326868, -20.997441], [-8.967071, 0.442676, -20.893728], [-9.067659, 0.436809, -21.012432], [-8.948813, 0.430942, -21.11284], [-8.848224, 0.436809, -20.994146], [-8.967071, 0.442676, -20.893728], [-8.957455, 0.54675, -21.009136], [-8.948813, 0.430942, -21.11284], [-9.81924, 0.990336, -10.6674]]}]},
			"R_toeTip_CTL": {"color": 20, "shapes": [{"shapeName": "R_toeTip_CTLShape", "degree": 1, "form": 0, "points": [[-12.310461, 2.591352, 19.228147], [-12.230813, 1.524092, 18.272344], [-13.237448, 2.53728, 18.134201], [-12.310461, 2.591352, 19.228147], [-11.215197, 2.53728, 18.302716], [-12.230813, 1.524092, 18.272344], [-12.142185, 2.483207, 17.20877], [-11.215197, 2.53728, 18.302716], [-12.221832, 3.550468, 18.164573], [-12.310461, 2.591352, 19.228147], [-13.237448, 2.53728, 18.134201], [-12.142185, 2.483207, 17.20877], [-12.221832, 3.550468, 18.164573], [-13.237448, 2.53728, 18.134201]]}]},
			"L_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[63.289928, 104.11005, 12.716336], [63.207414, 104.118367, 12.759345], [63.174164, 104.046761, 12.7094], [63.256677, 104.038444, 12.666391], [63.289928, 104.11005, 12.716336], [63.25221, 104.036392, 12.759678], [63.174164, 104.046761, 12.7094], [63.211879, 104.120423, 12.666054], [63.207414, 104.118367, 12.759345], [63.25221, 104.036392, 12.759678], [63.256677, 104.038444, 12.666391], [63.211879, 104.120423, 12.666054], [63.289928, 104.11005, 12.716336], [63.25221, 104.036392, 12.759678], [61.329552, 108.042274, 8.296463]]}, {"shapeName": "L_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[59.06374, 111.843812, 12.684532], [58.985691, 111.854185, 12.63425], [58.947976, 111.780523, 12.677597], [59.026024, 111.77015, 12.727879], [59.06374, 111.843812, 12.684532], [58.981229, 111.852125, 12.727537], [58.947976, 111.780523, 12.677597], [59.030489, 111.772206, 12.634587], [58.985691, 111.854185, 12.63425], [58.981229, 111.852125, 12.727537], [59.026024, 111.77015, 12.727879], [59.030489, 111.772206, 12.634587], [59.06374, 111.843812, 12.684532], [58.981229, 111.852125, 12.727537], [61.329552, 108.042274, 8.296463]]}, {"shapeName": "L_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[55.844395, 105.096934, 8.015813], [55.84886, 105.09899, 7.922521], [55.893658, 105.017012, 7.922858], [55.889193, 105.014956, 8.01615], [55.844395, 105.096934, 8.015813], [55.81115, 105.025332, 7.965868], [55.893658, 105.017012, 7.922858], [55.926908, 105.088618, 7.972803], [55.84886, 105.09899, 7.922521], [55.81115, 105.025332, 7.965868], [55.889193, 105.014956, 8.01615], [55.926908, 105.088618, 7.972803], [55.844395, 105.096934, 8.015813], [55.81115, 105.025332, 7.965868], [61.329552, 108.042274, 8.296463]]}]},
			"C_hip_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[5.152094, 101.733843, -4.33974], [0.0, 99.398723, -5.92498], [-5.152094, 101.733843, -4.33974], [-7.286156, 104.283193, -0.248615], [-5.152094, 102.465273, 4.215874], [0.0, 100.433122, 6.174478], [5.152094, 102.465273, 4.215874], [7.286156, 104.283193, -0.248615]]}]},
			"C_head_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[9.540915, 178.624044, -0.32106], [0.0, 182.576012, -0.32106], [-9.540915, 178.624044, -0.32106], [-13.492882, 169.08313, -0.32106], [-9.540915, 159.542215, -0.32106], [0.0, 155.590248, -0.32106], [9.540915, 159.542215, -0.32106], [13.492882, 169.08313, -0.32106]]}]},
			"R_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_A_CTLShape", "degree": 3, "form": 2, "points": [[-61.576133, 109.559049, -0.275899], [-61.962789, 110.090125, -0.686198], [-62.408424, 110.699132, -0.511814], [-62.65199, 111.029322, 0.145103], [-62.55081, 110.887276, 0.899739], [-62.164154, 110.3562, 1.310038], [-61.718519, 109.747193, 1.135654], [-61.474953, 109.417003, 0.478737]]}]},
			"R_arm_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-65.605903, 114.835324, 2.466356], [-65.424355, 114.616179, 2.406973], [-65.176244, 114.770682, 2.325817], [-64.985911, 114.671196, 2.263561], [-64.953099, 114.36981, 2.252828], [-64.677442, 114.349918, 2.162662], [-64.60584, 114.643742, 2.139241], [-64.404383, 114.715, 2.073346], [-64.178627, 114.526282, 1.999502], [-63.970335, 114.7173, 1.931371], [-64.117199, 114.978368, 1.97941], [-64.02262, 115.178596, 1.948473], [-63.736175, 115.213126, 1.854779], [-63.717268, 115.503155, 1.848594], [-63.996556, 115.578505, 1.939948], [-64.06424, 115.790468, 1.962087], [-63.884892, 116.027975, 1.903423], [-64.06644, 116.24712, 1.962807], [-64.314568, 116.092638, 2.043968], [-64.504901, 116.192124, 2.106225], [-64.537714, 116.49351, 2.116958], [-64.813359, 116.513389, 2.20712], [-64.884992, 116.21956, 2.230551], [-65.08643, 116.14832, 2.29644], [-65.312168, 116.337018, 2.370277], [-65.52046, 116.145999, 2.438409], [-65.373613, 115.884952, 2.390376], [-65.468212, 115.684706, 2.421319], [-65.754626, 115.65018, 2.515003], [-65.773544, 115.360165, 2.521191], [-65.494256, 115.284815, 2.429838], [-65.426572, 115.072852, 2.407699], [-65.605903, 114.835324, 2.466356]]}, {"shapeName": "R_arm_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-65.168548, 115.462183, 2.3233], [-65.024089, 115.768056, 2.276048], [-64.716371, 115.876861, 2.175396], [-64.42568, 115.724859, 2.080312], [-64.322264, 115.401137, 2.046485], [-64.466723, 115.095264, 2.093737], [-64.774441, 114.986459, 2.19439], [-65.065121, 115.138447, 2.28947]]}, {"shapeName": "R_arm_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-64.074481, 114.621791, 1.965437], [-60.377304, 110.158951, 0.75611]]}]},
			"L_ankleOffset_CTL": {"color": 20, "shapes": [{"shapeName": "L_ankleOffset_CTLShape", "degree": 1, "form": 0, "points": [[11.950418, 3.797464, -5.744851], [11.960498, 10.26143, -2.561292], [11.956712, 11.675668, -2.80391], [12.977532, 11.091473, -1.981966], [11.965349, 11.918306, -1.389696], [11.956712, 11.675668, -2.80391], [10.948315, 11.088263, -1.969022], [11.960498, 10.26143, -2.561292], [11.969135, 10.504068, -1.147078], [10.948315, 11.088263, -1.969022], [11.965349, 11.918306, -1.389696], [11.969135, 10.504068, -1.147078], [12.977532, 11.091473, -1.981966], [11.960498, 10.26143, -2.561292]]}]},
			"L_legEnd_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_legEnd_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[12.219067, -3.809504, -6.114671], [12.109135, -3.801443, -6.224639], [12.219325, -3.78772, -6.333786], [12.329256, -3.795781, -6.223817], [12.219067, -3.809504, -6.114671], [12.222053, -3.908123, -6.235112], [12.219325, -3.78772, -6.333786], [12.216338, -3.689091, -6.213344], [12.109135, -3.801443, -6.224639], [12.222053, -3.908123, -6.235112], [12.329256, -3.795781, -6.223817], [12.216338, -3.689091, -6.213344], [12.219067, -3.809504, -6.114671], [12.222053, -3.908123, -6.235112], [11.949581, 6.53346, -5.197381]]}, {"shapeName": "L_legEnd_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.566487, 6.255479, -5.1266], [1.563758, 6.375892, -5.225272], [1.566745, 6.277262, -5.345714], [1.569474, 6.15685, -5.247042], [1.566487, 6.255479, -5.1266], [1.456565, 6.26354, -5.236568], [1.566745, 6.277262, -5.345714], [1.676676, 6.269202, -5.235746], [1.563758, 6.375892, -5.225272], [1.456565, 6.26354, -5.236568], [1.569474, 6.15685, -5.247042], [1.676676, 6.269202, -5.235746], [1.566487, 6.255479, -5.1266], [1.456565, 6.26354, -5.236568], [11.949581, 6.53346, -5.197381]]}, {"shapeName": "L_legEnd_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[11.851689, 7.558136, -15.533308], [11.958891, 7.670488, -15.522012], [12.071809, 7.563798, -15.532486], [11.964607, 7.451446, -15.543781], [11.851689, 7.558136, -15.533308], [11.961878, 7.571858, -15.642444], [12.071809, 7.563798, -15.532486], [11.96162, 7.550076, -15.423339], [11.958891, 7.670488, -15.522012], [11.961878, 7.571858, -15.642444], [11.964607, 7.451446, -15.543781], [11.96162, 7.550076, -15.423339], [11.851689, 7.558136, -15.533308], [11.961878, 7.571858, -15.642444], [11.949581, 6.53346, -5.197381]]}]},
			"R_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_B_CTLShape", "degree": 3, "form": 2, "points": [[-66.716744, 105.828721, -0.283658], [-67.206726, 106.258684, -0.701915], [-67.789341, 106.741668, -0.537065], [-68.123301, 106.994748, 0.114327], [-68.012977, 106.869674, 0.870683], [-67.522995, 106.439711, 1.28894], [-66.94038, 105.956726, 1.12409], [-66.60642, 105.703647, 0.472698]]}]},
			"R_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-69.075041, 105.582426, 2.951175], [-69.114145, 105.644639, 3.008862], [-69.063903, 105.610436, 3.079807], [-69.024798, 105.548222, 3.02212], [-69.075041, 105.582426, 2.951175], [-69.11781, 105.553498, 3.029025], [-69.063903, 105.610436, 3.079807], [-69.02113, 105.639367, 3.001956], [-69.114145, 105.644639, 3.008862], [-69.11781, 105.553498, 3.029025], [-69.024798, 105.548222, 3.02212], [-69.02113, 105.639367, 3.001956], [-69.075041, 105.582426, 2.951175], [-69.11781, 105.553498, 3.029025], [-64.5089, 109.647, 1.7386]]}, {"shapeName": "R_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-68.728915, 114.180927, 1.04888], [-68.675004, 114.237868, 1.099661], [-68.717777, 114.208937, 1.177513], [-68.771689, 114.151995, 1.126732], [-68.728915, 114.180927, 1.04888], [-68.768016, 114.243136, 1.106568], [-68.717777, 114.208937, 1.177513], [-68.678673, 114.146723, 1.119826], [-68.675004, 114.237868, 1.099661], [-68.768016, 114.243136, 1.106568], [-68.771689, 114.151995, 1.126732], [-68.678673, 114.146723, 1.119826], [-68.728915, 114.180927, 1.04888], [-68.768016, 114.243136, 1.106568], [-64.5089, 109.647, 1.7386]]}, {"shapeName": "R_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-64.028216, 111.016411, 7.799491], [-63.9352, 111.011139, 7.792585], [-63.938869, 110.919994, 7.812749], [-64.031885, 110.925266, 7.819655], [-64.028216, 111.016411, 7.799491], [-63.977974, 110.982206, 7.87043], [-63.938869, 110.919994, 7.812749], [-63.989111, 110.954198, 7.741804], [-63.9352, 111.011139, 7.792585], [-63.977974, 110.982206, 7.87043], [-64.031885, 110.925266, 7.819655], [-63.989111, 110.954198, 7.741804], [-64.028216, 111.016411, 7.799491], [-63.977974, 110.982206, 7.87043], [-64.5089, 109.647, 1.7386]]}]},
			"L_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.616825, 105.502573, -2.21234], [66.681054, 105.566658, -2.190087], [66.671422, 105.544939, -2.099738], [66.607194, 105.480853, -2.121991], [66.616825, 105.502573, -2.21234], [66.691603, 105.478215, -2.161925], [66.671422, 105.544939, -2.099738], [66.59664, 105.569301, -2.150152], [66.681054, 105.566658, -2.190087], [66.691603, 105.478215, -2.161925], [66.607194, 105.480853, -2.121991], [66.59664, 105.569301, -2.150152], [66.616825, 105.502573, -2.21234], [66.691603, 105.478215, -2.161925], [62.164577, 109.820452, -1.600667]]}, {"shapeName": "L_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.621223, 113.84665, -4.86901], [65.601038, 113.913378, -4.806822], [65.67582, 113.889016, -4.756408], [65.696005, 113.822288, -4.818596], [65.621223, 113.84665, -4.86901], [65.685448, 113.910732, -4.846754], [65.67582, 113.889016, -4.756408], [65.611591, 113.82493, -4.778661], [65.601038, 113.913378, -4.806822], [65.685448, 113.910732, -4.846754], [65.696005, 113.822288, -4.818596], [65.611591, 113.82493, -4.778661], [65.621223, 113.84665, -4.86901], [65.685448, 113.910732, -4.846754], [62.164577, 109.820452, -1.600667]]}, {"shapeName": "L_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[64.776807, 111.861724, 3.676662], [64.692393, 111.864367, 3.716597], [64.702947, 111.775919, 3.744758], [64.78736, 111.773276, 3.704823], [64.776807, 111.861724, 3.676662], [64.767173, 111.840002, 3.767006], [64.702947, 111.775919, 3.744758], [64.712579, 111.797639, 3.654409], [64.692393, 111.864367, 3.716597], [64.767173, 111.840002, 3.767006], [64.78736, 111.773276, 3.704823], [64.712579, 111.797639, 3.654409], [64.776807, 111.861724, 3.676662], [64.767173, 111.840002, 3.767006], [62.164577, 109.820452, -1.600667]]}]},
			"C_neck_FK_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_B_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 161.353511, -11.588054], [0.0, 161.748592, -11.613281], [0.0, 162.103946, -11.787788], [0.0, 162.365481, -12.084989], [0.0, 162.493365, -12.459651], [0.0, 162.468138, -12.854731], [0.0, 162.29363, -13.210085], [0.0, 161.996429, -13.47162], [0.0, 161.621768, -13.599504], [0.0, 161.226687, -13.574277], [0.0, 160.871333, -13.39977], [0.0, 160.609798, -13.102568], [0.0, 160.481914, -12.727907], [0.0, 160.507142, -12.332826], [0.0, 160.681649, -11.977473], [0.0, 160.97885, -11.715938], [0.0, 161.353511, -11.588054], [0.0, 160.012227, -1.5308]]}]},
			"R_leg_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-11.949189, -3.853012, -5.087284], [-11.839503, -3.853012, -5.197791], [-11.950011, -3.853012, -5.307477], [-12.059697, -3.853012, -5.196969], [-11.949189, -3.853012, -5.087284], [-11.9496, -3.9631, -5.19738], [-11.950011, -3.853012, -5.307477], [-11.9496, -3.742915, -5.19738], [-11.839503, -3.853012, -5.197791], [-11.9496, -3.9631, -5.19738], [-12.059697, -3.853012, -5.196969], [-11.9496, -3.742915, -5.19738], [-11.949189, -3.853012, -5.087284], [-11.9496, -3.9631, -5.19738], [-11.9496, 6.53346, -5.19738]]}, {"shapeName": "R_leg_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.562789, 6.53346, -5.126073], [-1.5632, 6.643558, -5.236169], [-1.563611, 6.53346, -5.346266], [-1.5632, 6.423363, -5.236169], [-1.562789, 6.53346, -5.126073], [-1.453113, 6.53346, -5.23658], [-1.563611, 6.53346, -5.346266], [-1.673297, 6.53346, -5.235757], [-1.5632, 6.643558, -5.236169], [-1.453113, 6.53346, -5.23658], [-1.5632, 6.423363, -5.236169], [-1.673297, 6.53346, -5.235757], [-1.562789, 6.53346, -5.126073], [-1.453113, 6.53346, -5.23658], [-11.9496, 6.53346, -5.19738]]}, {"shapeName": "R_leg_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-11.878292, 6.53346, -15.584192], [-11.988389, 6.643558, -15.583781], [-12.098486, 6.53346, -15.583369], [-11.988389, 6.423363, -15.583781], [-11.878292, 6.53346, -15.584192], [-11.9888, 6.53346, -15.693867], [-12.098486, 6.53346, -15.583369], [-11.987978, 6.53346, -15.473684], [-11.988389, 6.643558, -15.583781], [-11.9888, 6.53346, -15.693867], [-11.988389, 6.423363, -15.583781], [-11.987978, 6.53346, -15.473684], [-11.878292, 6.53346, -15.584192], [-11.9888, 6.53346, -15.693867], [-11.9496, 6.53346, -5.19738]]}]},
			"R_upLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_upLeg_FK_CTLShape", "degree": 3, "form": 2, "points": [[-13.621175, 94.66902, 4.964783], [-9.642787, 94.497008, 6.595109], [-5.673097, 94.464566, 4.9351], [-4.0375, 94.590698, 0.957157], [-5.694096, 94.801517, -3.008491], [-9.672484, 94.973529, -4.638818], [-13.642173, 95.005972, -2.978808], [-15.277771, 94.87984, 0.999135]]}]},
			"L_leg_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[12.219067, -3.809504, -6.114671], [12.109135, -3.801443, -6.224639], [12.219325, -3.78772, -6.333786], [12.329256, -3.795781, -6.223817], [12.219067, -3.809504, -6.114671], [12.222053, -3.908123, -6.235112], [12.219325, -3.78772, -6.333786], [12.216338, -3.689091, -6.213344], [12.109135, -3.801443, -6.224639], [12.222053, -3.908123, -6.235112], [12.329256, -3.795781, -6.223817], [12.216338, -3.689091, -6.213344], [12.219067, -3.809504, -6.114671], [12.222053, -3.908123, -6.235112], [11.949581, 6.53346, -5.197381]]}, {"shapeName": "L_leg_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.566487, 6.255479, -5.1266], [1.563758, 6.375892, -5.225272], [1.566745, 6.277262, -5.345714], [1.569474, 6.15685, -5.247042], [1.566487, 6.255479, -5.1266], [1.456565, 6.26354, -5.236568], [1.566745, 6.277262, -5.345714], [1.676676, 6.269202, -5.235746], [1.563758, 6.375892, -5.225272], [1.456565, 6.26354, -5.236568], [1.569474, 6.15685, -5.247042], [1.676676, 6.269202, -5.235746], [1.566487, 6.255479, -5.1266], [1.456565, 6.26354, -5.236568], [11.949581, 6.53346, -5.197381]]}, {"shapeName": "L_leg_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[11.851689, 7.558136, -15.533308], [11.958891, 7.670488, -15.522012], [12.071809, 7.563798, -15.532486], [11.964607, 7.451446, -15.543781], [11.851689, 7.558136, -15.533308], [11.961878, 7.571858, -15.642444], [12.071809, 7.563798, -15.532486], [11.96162, 7.550076, -15.423339], [11.958891, 7.670488, -15.522012], [11.961878, 7.571858, -15.642444], [11.964607, 7.451446, -15.543781], [11.96162, 7.550076, -15.423339], [11.851689, 7.558136, -15.533308], [11.961878, 7.571858, -15.642444], [11.949581, 6.53346, -5.197381]]}]},
			"C_jaw_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_jaw_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.110097, 163.623924, 8.46193], [0.0, 163.705759, 8.535582], [-0.110097, 163.623924, 8.46193], [0.0, 163.542089, 8.388279], [0.110097, 163.623924, 8.46193], [0.0, 163.550279, 8.543758], [-0.110097, 163.623924, 8.46193], [0.0, 163.697575, 8.380095], [0.0, 163.705759, 8.535582], [0.0, 163.550279, 8.543758], [0.0, 163.542089, 8.388279], [0.0, 163.697575, 8.380095], [0.110097, 163.623924, 8.46193], [0.0, 163.550279, 8.543758], [0.0, 170.572105, 0.741723]]}, {"shapeName": "C_jaw_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.110097, 178.292312, 7.689904], [0.0, 178.365963, 7.60807], [-0.110097, 178.292312, 7.689904], [0.0, 178.21866, 7.771739], [0.110097, 178.292312, 7.689904], [0.0, 178.374139, 7.763549], [-0.110097, 178.292312, 7.689904], [0.0, 178.210477, 7.616253], [0.0, 178.365963, 7.60807], [0.0, 178.374139, 7.763549], [0.0, 178.21866, 7.771739], [0.0, 178.210477, 7.616253], [0.110097, 178.292312, 7.689904], [0.0, 178.374139, 7.763549], [0.0, 170.572105, 0.741723]]}, {"shapeName": "C_jaw_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-10.386473, 170.65394, 0.815375], [-10.386473, 170.645756, 0.659889], [-10.386473, 170.49027, 0.668072], [-10.386473, 170.498453, 0.823558], [-10.386473, 170.65394, 0.815375], [-10.49656, 170.572105, 0.741723], [-10.386473, 170.49027, 0.668072], [-10.276375, 170.572105, 0.741723], [-10.386473, 170.645756, 0.659889], [-10.49656, 170.572105, 0.741723], [-10.386473, 170.498453, 0.823558], [-10.276375, 170.572105, 0.741723], [-10.386473, 170.65394, 0.815375], [-10.49656, 170.572105, 0.741723], [0.0, 170.572105, 0.741723]]}]},
			"R_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_B_CTLShape", "degree": 3, "form": 2, "points": [[-64.085324, 108.973191, 1.113715], [-64.594229, 109.432564, 0.753324], [-65.053161, 110.017613, 0.970093], [-65.193283, 110.385625, 1.637043], [-64.932514, 110.321024, 2.363484], [-64.423609, 109.861651, 2.723875], [-63.964677, 109.276602, 2.507106], [-63.824555, 108.90859, 1.840156]]}]},
			"R_leg_PV_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_PV_CTLShape", "degree": 1, "form": 0, "points": [[-9.62292, 43.240931, 101.284039], [-9.62292, 41.211671, 101.284039], [-9.62292, 41.211671, 99.254779], [-9.62292, 43.240931, 99.254779], [-11.65218, 43.240931, 99.254779], [-11.65218, 41.211671, 99.254779], [-11.65218, 41.211671, 101.284039], [-11.65218, 43.240931, 101.284039], [-9.62292, 43.240931, 101.284039], [-9.62292, 43.240931, 99.254779], [-9.62292, 41.211671, 99.254779], [-11.65218, 41.211671, 99.254779], [-11.65218, 43.240931, 99.254779], [-11.65218, 43.240931, 101.284039], [-11.65218, 41.211671, 101.284039], [-9.62292, 41.211671, 101.284039]]}]},
			"R_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_C_CTLShape", "degree": 3, "form": 2, "points": [[-71.00353, 102.974151, 2.993596], [-71.703102, 103.178813, 2.731675], [-72.338665, 103.486385, 3.050028], [-72.537915, 103.716695, 3.76217], [-72.184135, 103.734832, 4.450938], [-71.484563, 103.53017, 4.712859], [-70.849, 103.222598, 4.394506], [-70.64975, 102.992287, 3.682364]]}]},
			"C_head_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.386473, 169.08313, -0.431158], [10.386473, 169.193227, -0.32106], [10.386473, 169.08313, -0.210963], [10.386473, 168.973032, -0.32106], [10.386473, 169.08313, -0.431158], [10.49656, 169.08313, -0.32106], [10.386473, 169.08313, -0.210963], [10.276375, 169.08313, -0.32106], [10.386473, 169.193227, -0.32106], [10.49656, 169.08313, -0.32106], [10.386473, 168.973032, -0.32106], [10.276375, 169.08313, -0.32106], [10.386473, 169.08313, -0.431158], [10.49656, 169.08313, -0.32106], [0.0, 169.08313, -0.32106]]}, {"shapeName": "C_head_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 179.469603, -0.431158], [-0.110097, 179.469603, -0.32106], [0.0, 179.469603, -0.210963], [0.110097, 179.469603, -0.32106], [0.0, 179.469603, -0.431158], [0.0, 179.57969, -0.32106], [0.0, 179.469603, -0.210963], [0.0, 179.359505, -0.32106], [-0.110097, 179.469603, -0.32106], [0.0, 179.57969, -0.32106], [0.110097, 179.469603, -0.32106], [0.0, 179.359505, -0.32106], [0.0, 179.469603, -0.431158], [0.0, 179.57969, -0.32106], [0.0, 169.08313, -0.32106]]}, {"shapeName": "C_head_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 169.193227, 10.065412], [-0.110097, 169.08313, 10.065412], [0.0, 168.973032, 10.065412], [0.110097, 169.08313, 10.065412], [0.0, 169.193227, 10.065412], [0.0, 169.08313, 10.1755], [0.0, 168.973032, 10.065412], [0.0, 169.08313, 9.955315], [-0.110097, 169.08313, 10.065412], [0.0, 169.08313, 10.1755], [0.110097, 169.08313, 10.065412], [0.0, 169.08313, 9.955315], [0.0, 169.193227, 10.065412], [0.0, 169.08313, 10.1755], [0.0, 169.08313, -0.32106]]}]},
			"R_legEnd_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_legEnd_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-12.219067, -3.809504, -6.114671], [-12.109135, -3.801443, -6.224639], [-12.219325, -3.78772, -6.333786], [-12.329256, -3.795781, -6.223817], [-12.219067, -3.809504, -6.114671], [-12.222053, -3.908123, -6.235112], [-12.219325, -3.78772, -6.333786], [-12.216338, -3.689091, -6.213344], [-12.109135, -3.801443, -6.224639], [-12.222053, -3.908123, -6.235112], [-12.329256, -3.795781, -6.223817], [-12.216338, -3.689091, -6.213344], [-12.219067, -3.809504, -6.114671], [-12.222053, -3.908123, -6.235112], [-11.949581, 6.53346, -5.197381]]}, {"shapeName": "R_legEnd_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.566487, 6.255479, -5.1266], [-1.563758, 6.375892, -5.225272], [-1.566745, 6.277262, -5.345714], [-1.569474, 6.15685, -5.247042], [-1.566487, 6.255479, -5.1266], [-1.456565, 6.26354, -5.236568], [-1.566745, 6.277262, -5.345714], [-1.676676, 6.269202, -5.235746], [-1.563758, 6.375892, -5.225272], [-1.456565, 6.26354, -5.236568], [-1.569474, 6.15685, -5.247042], [-1.676676, 6.269202, -5.235746], [-1.566487, 6.255479, -5.1266], [-1.456565, 6.26354, -5.236568], [-11.949581, 6.53346, -5.197381]]}, {"shapeName": "R_legEnd_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-11.851689, 7.558136, -15.533308], [-11.958891, 7.670488, -15.522012], [-12.071809, 7.563798, -15.532486], [-11.964607, 7.451446, -15.543781], [-11.851689, 7.558136, -15.533308], [-11.961878, 7.571858, -15.642444], [-12.071809, 7.563798, -15.532486], [-11.96162, 7.550076, -15.423339], [-11.958891, 7.670488, -15.522012], [-11.961878, 7.571858, -15.642444], [-11.964607, 7.451446, -15.543781], [-11.96162, 7.550076, -15.423339], [-11.851689, 7.558136, -15.533308], [-11.961878, 7.571858, -15.642444], [-11.949581, 6.53346, -5.197381]]}]},
			"R_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_C_CTLShape", "degree": 3, "form": 2, "points": [[-63.093435, 106.119291, 9.866462], [-63.049332, 106.790426, 10.250549], [-62.492772, 107.16361, 10.638961], [-61.749778, 107.020236, 10.804171], [-61.255587, 106.444292, 10.649402], [-61.29969, 105.773158, 10.265314], [-61.85625, 105.399974, 9.876902], [-62.599244, 105.543347, 9.711692]]}]},
			"C_cog_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[29.200713, 102.099558, 2.039491], [29.169913, 102.099558, -2.554368], [21.243069, 102.099558, -5.312687], [20.159804, 102.099558, -8.572503], [24.859035, 102.099558, -15.525605], [22.13394, 102.099558, -19.224004], [14.09848, 102.099558, -16.801146], [11.306819, 102.099558, -18.801785], [11.022086, 102.099558, -27.184073], [6.643531, 102.099558, -28.574395], [1.568748, 102.099558, -21.89577], [-1.864994, 102.099558, -21.873065], [-7.024957, 102.099558, -28.482816], [-11.38446, 102.099558, -27.033963], [-11.560197, 102.099558, -18.650623], [-14.324448, 102.099558, -16.613252], [-22.388692, 102.099558, -18.925742], [-25.063993, 102.099558, -15.191137], [-20.273534, 102.099558, -8.305216], [-21.31244, 102.099558, -5.031402], [-29.200713, 102.099558, -2.163357], [-29.169913, 102.099558, 2.430501], [-21.243069, 102.099558, 5.188821], [-20.159804, 102.099558, 8.448637], [-24.859035, 102.099558, 15.401739], [-22.13394, 102.099558, 19.100138], [-14.09848, 102.099558, 16.677279], [-11.306819, 102.099558, 18.677919], [-11.022086, 102.099558, 27.060207], [-6.643531, 102.099558, 28.450529], [-1.568748, 102.099558, 21.771904], [1.864994, 102.099558, 21.749199], [7.024957, 102.099558, 28.358949], [11.38446, 102.099558, 26.910097], [11.560197, 102.099558, 18.526757], [14.324448, 102.099558, 16.489386], [22.388692, 102.099558, 18.801876], [25.063993, 102.099558, 15.067271], [20.273534, 102.099558, 8.181349], [21.31244, 102.099558, 4.907536], [29.200713, 102.099558, 2.039491]]}]},
			"L_arm_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.853237, 103.334378, 3.08561], [67.887766, 103.417374, 3.212742], [67.784782, 103.334378, 3.294894], [67.750253, 103.251383, 3.167762], [67.853237, 103.334378, 3.08561], [67.897885, 103.262044, 3.216052], [67.784782, 103.334378, 3.294894], [67.740127, 103.406719, 3.16445], [67.887766, 103.417374, 3.212742], [67.897885, 103.262044, 3.216052], [67.750253, 103.251383, 3.167762], [67.740127, 103.406719, 3.16445], [67.853237, 103.334378, 3.08561], [67.897885, 103.262044, 3.216052], [60.377304, 110.158951, 0.75611]]}, {"shapeName": "L_arm_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[66.897928, 117.988639, 2.773133], [66.784817, 118.06098, 2.851973], [66.829472, 117.988639, 2.982417], [66.942582, 117.916298, 2.903577], [66.897928, 117.988639, 2.773133], [66.93245, 118.071627, 2.900263], [66.829472, 117.988639, 2.982417], [66.794943, 117.905644, 2.855285], [66.784817, 118.06098, 2.851973], [66.93245, 118.071627, 2.900263], [66.942582, 117.916298, 2.903577], [66.794943, 117.905644, 2.855285], [66.897928, 117.988639, 2.773133], [66.93245, 118.071627, 2.900263], [60.377304, 110.158951, 0.75611]]}, {"shapeName": "L_arm_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[57.21705, 110.241946, 10.650393], [57.069411, 110.231292, 10.602101], [57.079537, 110.075955, 10.605414], [57.227176, 110.08661, 10.653706], [57.21705, 110.241946, 10.650393], [57.114069, 110.158951, 10.732536], [57.079537, 110.075955, 10.605414], [57.182521, 110.158951, 10.523262], [57.069411, 110.231292, 10.602101], [57.114069, 110.158951, 10.732536], [57.227176, 110.08661, 10.653706], [57.182521, 110.158951, 10.523262], [57.21705, 110.241946, 10.650393], [57.114069, 110.158951, 10.732536], [60.377304, 110.158951, 0.75611]]}]},
			"R_shoulder_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-4.604762, 149.074616, 5.289387], [-7.700241, 149.777541, 3.473083], [-8.882612, 150.046035, 2.779315], [-3.348719, 149.777541, -3.943105], [2.436153, 149.074616, -6.710262], [6.262394, 148.205749, -4.465177], [6.668482, 147.502824, 1.934588], [3.49933, 147.23433, 10.044544], [2.31696, 147.502824, 9.350776], [-0.77852, 148.205749, 7.534472], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193]]}]},
			"C_torso_FK_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 117.387881, -1.175026], [-0.066058, 117.393508, -1.109207], [0.0, 117.399135, -1.043389], [0.066058, 117.393508, -1.109207], [0.0, 117.387881, -1.175026], [0.0, 117.459321, -1.114834], [0.0, 117.399135, -1.043389], [0.0, 117.32769, -1.10358], [-0.066058, 117.393508, -1.109207], [0.0, 117.459321, -1.114834], [0.066058, 117.393508, -1.109207], [0.0, 117.32769, -1.10358], [0.0, 117.387881, -1.175026], [0.0, 117.459321, -1.114834], [0.0, 111.184274, -0.578372]]}, {"shapeName": "C_torso_FK_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-6.231884, 111.178647, -0.64419], [-6.231884, 111.118456, -0.572745], [-6.231884, 111.189901, -0.512553], [-6.231884, 111.250093, -0.583998], [-6.231884, 111.178647, -0.64419], [-6.297936, 111.184274, -0.578372], [-6.231884, 111.189901, -0.512553], [-6.165825, 111.184274, -0.578372], [-6.231884, 111.118456, -0.572745], [-6.297936, 111.184274, -0.578372], [-6.231884, 111.250093, -0.583998], [-6.165825, 111.184274, -0.578372], [-6.231884, 111.178647, -0.64419], [-6.297936, 111.184274, -0.578372], [0.0, 111.184274, -0.578372]]}, {"shapeName": "C_torso_FK_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.066058, 111.71511, 5.630862], [0.0, 111.649292, 5.636489], [0.066058, 111.71511, 5.630862], [0.0, 111.780928, 5.625236], [-0.066058, 111.71511, 5.630862], [0.0, 111.720736, 5.696675], [0.066058, 111.71511, 5.630862], [0.0, 111.709483, 5.565044], [0.0, 111.649292, 5.636489], [0.0, 111.720736, 5.696675], [0.0, 111.780928, 5.625236], [0.0, 111.709483, 5.565044], [-0.066058, 111.71511, 5.630862], [0.0, 111.720736, 5.696675], [0.0, 111.184274, -0.578372]]}]},
			"R_arm_IK_switch_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-63.863036, 113.276533, 1.896274], [-63.742005, 113.130436, 1.856686], [-63.576597, 113.233438, 1.802582], [-63.449709, 113.167114, 1.761077], [-63.427834, 112.966191, 1.753922], [-63.244063, 112.952929, 1.693811], [-63.196328, 113.148812, 1.678198], [-63.062023, 113.196317, 1.634267], [-62.91152, 113.070505, 1.585038], [-62.772658, 113.19785, 1.539618], [-62.870567, 113.371895, 1.571643], [-62.807515, 113.505381, 1.551019], [-62.616551, 113.528401, 1.488556], [-62.603947, 113.721754, 1.484433], [-62.790139, 113.771987, 1.545335], [-62.835261, 113.913296, 1.560095], [-62.715696, 114.071634, 1.520986], [-62.836728, 114.217731, 1.560574], [-63.002147, 114.114743, 1.614682], [-63.129035, 114.181067, 1.656186], [-63.15091, 114.38199, 1.663342], [-63.334674, 114.395243, 1.72345], [-63.38243, 114.199357, 1.73907], [-63.516721, 114.151864, 1.782996], [-63.667213, 114.277662, 1.832222], [-63.806075, 114.150316, 1.877642], [-63.708177, 113.976285, 1.845621], [-63.771243, 113.842788, 1.866249], [-63.962185, 113.81977, 1.928705], [-63.974797, 113.626427, 1.932831], [-63.788605, 113.576194, 1.871928], [-63.743483, 113.434885, 1.857169], [-63.863036, 113.276533, 1.896274]]}, {"shapeName": "R_arm_IK_switch_D_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-63.571467, 113.694439, 1.800903], [-63.475161, 113.898354, 1.769402], [-63.270015, 113.970891, 1.7023], [-63.076221, 113.869557, 1.638911], [-63.007278, 113.653742, 1.61636], [-63.103584, 113.449826, 1.647861], [-63.308729, 113.37729, 1.714963], [-63.502515, 113.478615, 1.77835]]}, {"shapeName": "R_arm_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-62.842089, 113.134178, 1.562328], [-60.377304, 110.158951, 0.75611]]}]},
			"C_neck_FK_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 174.857552, 0.337972], [-0.110097, 174.842998, 0.447103], [0.0, 174.828443, 0.556235], [0.110097, 174.842998, 0.447103], [0.0, 174.857552, 0.337972], [0.0, 174.952119, 0.461656], [0.0, 174.828443, 0.556235], [0.0, 174.733866, 0.432549], [-0.110097, 174.842998, 0.447103], [0.0, 174.952119, 0.461656], [0.110097, 174.842998, 0.447103], [0.0, 174.733866, 0.432549], [0.0, 174.857552, 0.337972], [0.0, 174.952119, 0.461656], [0.0, 164.547679, -0.92593]]}, {"shapeName": "C_neck_FK_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-10.386473, 164.562233, -1.035061], [-10.386473, 164.438547, -0.940484], [-10.386473, 164.533124, -0.816799], [-10.386473, 164.65681, -0.911376], [-10.386473, 164.562233, -1.035061], [-10.49656, 164.547679, -0.92593], [-10.386473, 164.533124, -0.816799], [-10.276375, 164.547679, -0.92593], [-10.386473, 164.438547, -0.940484], [-10.49656, 164.547679, -0.92593], [-10.386473, 164.65681, -0.911376], [-10.276375, 164.547679, -0.92593], [-10.386473, 164.562233, -1.035061], [-10.49656, 164.547679, -0.92593], [0.0, 164.547679, -0.92593]]}, {"shapeName": "C_neck_FK_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.110097, 163.174645, 9.369389], [0.0, 163.065514, 9.354835], [0.110097, 163.174645, 9.369389], [0.0, 163.283776, 9.383943], [-0.110097, 163.174645, 9.369389], [0.0, 163.160092, 9.47851], [0.110097, 163.174645, 9.369389], [0.0, 163.189199, 9.260258], [0.0, 163.065514, 9.354835], [0.0, 163.160092, 9.47851], [0.0, 163.283776, 9.383943], [0.0, 163.189199, 9.260258], [-0.110097, 163.174645, 9.369389], [0.0, 163.160092, 9.47851], [0.0, 164.547679, -0.92593]]}]},
			"C_midTorso_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[7.728141, 119.696941, -7.76974], [0.0, 119.469715, -10.427623], [-7.728141, 119.696941, -7.76974], [-10.929234, 120.245514, -1.353029], [-7.728141, 120.794087, 5.063682], [0.0, 121.021313, 7.721565], [7.728141, 120.794087, 5.063682], [10.929234, 120.245514, -1.353029]]}]},
			"R_leg_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-17.479234, 7.507469, -5.094039], [-17.253205, 7.501655, -5.094883], [-17.216422, 7.269754, -5.117981], [-17.057533, 7.1994, -5.125162], [-16.859776, 7.327483, -5.112662], [-16.704098, 7.164327, -5.129065], [-16.842871, 6.974455, -5.147778], [-16.780522, 6.812894, -5.163913], [-16.549676, 6.764331, -5.169013], [-16.555546, 6.539403, -5.191367], [-16.788615, 6.502774, -5.194734], [-16.859305, 6.344656, -5.21037], [-16.730622, 6.147883, -5.230084], [-16.8946, 5.99295, -5.245294], [-17.085412, 6.131028, -5.231342], [-17.247757, 6.068937, -5.237324], [-17.296585, 5.839239, -5.260102], [-17.522614, 5.845053, -5.259258], [-17.559419, 6.076954, -5.23616], [-17.718307, 6.147308, -5.228979], [-17.916065, 6.019226, -5.241479], [-18.071729, 6.182381, -5.225076], [-17.932969, 6.372274, -5.206361], [-17.995318, 6.533815, -5.190228], [-18.226143, 6.582377, -5.185128], [-18.220273, 6.807305, -5.162774], [-17.987226, 6.843935, -5.159407], [-17.916534, 7.002074, -5.143768], [-18.045205, 7.198825, -5.124057], [-17.88124, 7.353759, -5.108847], [-17.690428, 7.215681, -5.122799], [-17.528084, 7.277771, -5.116817], [-17.479234, 7.507469, -5.094039]]}, {"shapeName": "R_leg_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-17.626883, 6.923811, -5.15189], [-17.734884, 6.682279, -5.175775], [-17.639625, 6.43552, -5.200419], [-17.396922, 6.328098, -5.211384], [-17.148957, 6.422898, -5.202251], [-17.040957, 6.664429, -5.178366], [-17.136215, 6.911189, -5.153722], [-17.378904, 7.01861, -5.142757]]}, {"shapeName": "R_leg_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-16.552611, 6.651867, -5.18019], [-11.949581, 6.53346, -5.197381]]}]},
			"C_midTorso_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.010776, 119.818846, -6.343804], [0.0, 119.642115, -8.411046], [-6.010776, 119.818846, -6.343804], [-8.500516, 120.245514, -1.353029], [-6.010776, 120.672182, 3.637746], [0.0, 120.848913, 5.704988], [6.010776, 120.672182, 3.637746], [8.500516, 120.245514, -1.353029]]}]},
			"C_hip_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.010776, 101.67289, -5.052708], [0.0, 98.948584, -6.902155], [-6.010776, 101.67289, -5.052708], [-8.500516, 104.647133, -0.279729], [-6.010776, 102.526226, 4.928842], [0.0, 100.155383, 7.21388], [6.010776, 102.526226, 4.928842], [8.500516, 104.647133, -0.279729]]}]},
			"L_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[72.863612, 96.494945, 0.362803], [72.934146, 96.523612, 0.416937], [72.881972, 96.508467, 0.492937], [72.811438, 96.4798, 0.438803], [72.863612, 96.494945, 0.362803], [72.895486, 96.439759, 0.431105], [72.881972, 96.508467, 0.492937], [72.850096, 96.563659, 0.424635], [72.934146, 96.523612, 0.416937], [72.895486, 96.439759, 0.431105], [72.811438, 96.4798, 0.438803], [72.850096, 96.563659, 0.424635], [72.863612, 96.494945, 0.362803], [72.895486, 96.439759, 0.431105], [70.731628, 102.346245, 0.12265]]}, {"shapeName": "L_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[76.510517, 104.406098, -0.973792], [76.497001, 104.474812, -0.91196], [76.528878, 104.41962, -0.843658], [76.542394, 104.350906, -0.905489], [76.510517, 104.406098, -0.973792], [76.581046, 104.434763, -0.919656], [76.528878, 104.41962, -0.843658], [76.458344, 104.390953, -0.897792], [76.497001, 104.474812, -0.91196], [76.581046, 104.434763, -0.919656], [76.542394, 104.350906, -0.905489], [76.458344, 104.390953, -0.897792], [76.510517, 104.406098, -0.973792], [76.581046, 104.434763, -0.919656], [70.731628, 102.346245, 0.12265]]}, {"shapeName": "L_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[71.659035, 103.005996, 6.250079], [71.574984, 103.046043, 6.257776], [71.536327, 102.962184, 6.271944], [71.620377, 102.922137, 6.264247], [71.659035, 103.005996, 6.250079], [71.60686, 102.990851, 6.326073], [71.536327, 102.962184, 6.271944], [71.588501, 102.977329, 6.195944], [71.574984, 103.046043, 6.257776], [71.60686, 102.990851, 6.326073], [71.620377, 102.922137, 6.264247], [71.588501, 102.977329, 6.195944], [71.659035, 103.005996, 6.250079], [71.60686, 102.990851, 6.326073], [70.731628, 102.346245, 0.12265]]}]},
			"L_arm_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_arm_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[64.443992, 113.79613, 2.086302], [64.302788, 113.625684, 2.040115], [64.109813, 113.745852, 1.976994], [63.961777, 113.668475, 1.928572], [63.936255, 113.434064, 1.920224], [63.721856, 113.418592, 1.850095], [63.666165, 113.647122, 1.831879], [63.509476, 113.702545, 1.780627], [63.333889, 113.555764, 1.723193], [63.171884, 113.704334, 1.670202], [63.286111, 113.907386, 1.707565], [63.21255, 114.063119, 1.683504], [62.989759, 114.089976, 1.61063], [62.975054, 114.315554, 1.60582], [63.192278, 114.374159, 1.676873], [63.244921, 114.53902, 1.694092], [63.105428, 114.723748, 1.648465], [63.246632, 114.894194, 1.694652], [63.439621, 114.774041, 1.757777], [63.587657, 114.851419, 1.806199], [63.613178, 115.08583, 1.814547], [63.827569, 115.101291, 1.884673], [63.883284, 114.872758, 1.902897], [64.039957, 114.817349, 1.954144], [64.215531, 114.964114, 2.011574], [64.377536, 114.815544, 2.064564], [64.263322, 114.612508, 2.027206], [64.336899, 114.456761, 2.051272], [64.559665, 114.429907, 2.124138], [64.57438, 114.20434, 2.128951], [64.357156, 114.145734, 2.057898], [64.304513, 113.980874, 2.040679], [64.443992, 113.79613, 2.086302]]}, {"shapeName": "L_arm_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[64.103827, 114.283687, 1.975036], [63.99147, 114.521588, 1.938284], [63.752134, 114.606214, 1.859999], [63.526041, 114.487991, 1.786045], [63.445607, 114.236207, 1.759735], [63.557963, 113.998305, 1.796487], [63.797299, 113.913679, 1.874772], [64.023384, 114.031892, 1.948723]]}, {"shapeName": "L_arm_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[63.252886, 113.630049, 1.696698], [60.377304, 110.158951, 0.75611]]}]},
			"R_reverseBall_CTL": {"color": 20, "shapes": [{"shapeName": "R_reverseBall_CTLShape", "degree": 1, "form": 0, "points": [[-12.062765, 0.053335, 9.84271], [-12.03021, 7.398949, 9.452037], [-11.941582, 8.358065, 8.388463], [-13.036845, 8.412137, 9.313894], [-12.02123, 9.425325, 9.344266], [-11.941582, 8.358065, 8.388463], [-11.014595, 8.412137, 9.482409], [-12.03021, 7.398949, 9.452037], [-12.109858, 8.46621, 10.40784], [-11.014595, 8.412137, 9.482409], [-12.02123, 9.425325, 9.344266], [-12.109858, 8.46621, 10.40784], [-13.036845, 8.412137, 9.313894], [-12.03021, 7.398949, 9.452037]]}]},
			"R_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.616848, 105.502121, -2.212343], [-66.681077, 105.566206, -2.19009], [-66.671445, 105.544487, -2.099741], [-66.607217, 105.480401, -2.121994], [-66.616848, 105.502121, -2.212343], [-66.691626, 105.477763, -2.161928], [-66.671445, 105.544487, -2.099741], [-66.596663, 105.568849, -2.150155], [-66.681077, 105.566206, -2.19009], [-66.691626, 105.477763, -2.161928], [-66.607217, 105.480401, -2.121994], [-66.596663, 105.568849, -2.150155], [-66.616848, 105.502121, -2.212343], [-66.691626, 105.477763, -2.161928], [-62.1646, 109.82, -1.60067]]}, {"shapeName": "R_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.621246, 113.846198, -4.869013], [-65.601061, 113.912926, -4.806825], [-65.675843, 113.888564, -4.756411], [-65.696028, 113.821836, -4.818599], [-65.621246, 113.846198, -4.869013], [-65.685471, 113.91028, -4.846757], [-65.675843, 113.888564, -4.756411], [-65.611614, 113.824478, -4.778664], [-65.601061, 113.912926, -4.806825], [-65.685471, 113.91028, -4.846757], [-65.696028, 113.821836, -4.818599], [-65.611614, 113.824478, -4.778664], [-65.621246, 113.846198, -4.869013], [-65.685471, 113.91028, -4.846757], [-62.1646, 109.82, -1.60067]]}, {"shapeName": "R_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-64.77683, 111.861272, 3.676659], [-64.692416, 111.863915, 3.716594], [-64.70297, 111.775467, 3.744755], [-64.787383, 111.772824, 3.70482], [-64.77683, 111.861272, 3.676659], [-64.767196, 111.83955, 3.767003], [-64.70297, 111.775467, 3.744755], [-64.712602, 111.797187, 3.654406], [-64.692416, 111.863915, 3.716594], [-64.767196, 111.83955, 3.767003], [-64.787383, 111.772824, 3.70482], [-64.712602, 111.797187, 3.654406], [-64.77683, 111.861272, 3.676659], [-64.767196, 111.83955, 3.767003], [-62.1646, 109.82, -1.60067]]}]},
			"L_leg_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[16.749698, 6.53346, -13.130272], [11.991573, 6.53346, -16.44137], [7.20885, 6.53346, -13.165903], [5.203187, 6.53346, -5.222576], [7.149464, 6.53346, 2.73551], [11.907589, 6.53346, 6.046609], [16.690312, 6.53346, 2.771142], [18.695975, 6.53346, -5.172185]]}]},
			"R_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_C_CTLShape", "degree": 3, "form": 2, "points": [[-69.807078, 103.479012, 6.778728], [-70.525426, 103.757688, 6.699946], [-71.011806, 104.154386, 7.153768], [-70.981303, 104.436726, 7.874354], [-70.451787, 104.439317, 8.439593], [-69.733439, 104.160641, 8.518376], [-69.247059, 103.763943, 8.064553], [-69.277562, 103.481603, 7.343968]]}]},
			"L_upArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_upArm_FK_CTLShape", "degree": 3, "form": 2, "points": [[13.411151, 148.884544, -5.066038], [15.764791, 151.565067, -7.472342], [18.865229, 154.44082, -6.677076], [20.896271, 155.827224, -3.146088], [20.668164, 154.912148, 1.052212], [18.314524, 152.231625, 3.458515], [15.214086, 149.355872, 2.66325], [13.183044, 147.969468, -0.867738]]}]},
			"L_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_A_CTLShape", "degree": 3, "form": 2, "points": [[61.262999, 109.565195, 3.440012], [61.192102, 110.281002, 3.727213], [60.608068, 110.700001, 4.015717], [59.853016, 110.576747, 4.13652], [59.369243, 109.983443, 4.01886], [59.44014, 109.267636, 3.731658], [60.024174, 108.848637, 3.443155], [60.779227, 108.971891, 3.322351]]}]},
			"L_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.776337, 107.917935, 5.21538], [66.781488, 107.984824, 5.280394], [66.723362, 107.9362, 5.335025], [66.718212, 107.869311, 5.270011], [66.776337, 107.917935, 5.21538], [66.801432, 107.896338, 5.302732], [66.723362, 107.9362, 5.335025], [66.698263, 107.957801, 5.24767], [66.781488, 107.984824, 5.280394], [66.801432, 107.896338, 5.302732], [66.718212, 107.869311, 5.270011], [66.698263, 107.957801, 5.24767], [66.776337, 107.917935, 5.21538], [66.801432, 107.896338, 5.302732], [61.883235, 110.826397, 2.677832]]}, {"shapeName": "L_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[64.894434, 116.265936, 3.107755], [64.816361, 116.305801, 3.140045], [64.84146, 116.2842, 3.2274], [64.919534, 116.244335, 3.19511], [64.894434, 116.265936, 3.107755], [64.899582, 116.332819, 3.172768], [64.84146, 116.2842, 3.2274], [64.836309, 116.217311, 3.162386], [64.816361, 116.305801, 3.140045], [64.899582, 116.332819, 3.172768], [64.919534, 116.244335, 3.19511], [64.836309, 116.217311, 3.162386], [64.894434, 116.265936, 3.107755], [64.899582, 116.332819, 3.172768], [61.883235, 110.826397, 2.677832]]}, {"shapeName": "L_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[59.416087, 111.74569, 8.326621], [59.332863, 111.718667, 8.293898], [59.352811, 111.630178, 8.316239], [59.436036, 111.657201, 8.348962], [59.416087, 111.74569, 8.326621], [59.357964, 111.697066, 8.381247], [59.352811, 111.630178, 8.316239], [59.410936, 111.678802, 8.261607], [59.332863, 111.718667, 8.293898], [59.357964, 111.697066, 8.381247], [59.436036, 111.657201, 8.348962], [59.410936, 111.678802, 8.261607], [59.416087, 111.74569, 8.326621], [59.357964, 111.697066, 8.381247], [61.883235, 110.826397, 2.677832]]}]},
			"C_hip_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.869458, 101.611937, -5.765676], [0.0, 98.498445, -7.879329], [-6.869458, 101.611937, -5.765676], [-9.714875, 105.011072, -0.310842], [-6.869458, 102.587179, 5.64181], [0.0, 99.877643, 8.253282], [6.869458, 102.587179, 5.64181], [9.714875, 105.011072, -0.310842]]}]},
			"C_hip_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_CTLShape", "degree": 3, "form": 2, "points": [[8.586823, 101.490032, -7.191612], [0.0, 97.598167, -9.833678], [-8.586823, 101.490032, -7.191612], [-12.143594, 105.73895, -0.37307], [-8.586823, 102.709084, 7.067746], [0.0, 99.322165, 10.332085], [8.586823, 102.709084, 7.067746], [12.143594, 105.73895, -0.37307]]}]},
			"R_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-70.801142, 103.128024, 8.012547], [-70.81882, 103.183139, 8.085877], [-70.743716, 103.148956, 8.129675], [-70.726037, 103.093841, 8.056344], [-70.801142, 103.128024, 8.012547], [-70.809669, 103.090948, 8.097865], [-70.743716, 103.148956, 8.129675], [-70.735185, 103.186037, 8.044354], [-70.81882, 103.183139, 8.085877], [-70.809669, 103.090948, 8.097865], [-70.726037, 103.093841, 8.056344], [-70.735185, 103.186037, 8.044354], [-70.801142, 103.128024, 8.012547], [-70.809669, 103.090948, 8.097865], [-67.2589, 107.624, 5.54689]]}, {"shapeName": "R_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-71.664147, 111.825632, 6.881361], [-71.59819, 111.883645, 6.913168], [-71.606721, 111.846564, 6.998489], [-71.672678, 111.788551, 6.966682], [-71.664147, 111.825632, 6.881361], [-71.681821, 111.880743, 6.95469], [-71.606721, 111.846564, 6.998489], [-71.589042, 111.79145, 6.925159], [-71.59819, 111.883645, 6.913168], [-71.681821, 111.880743, 6.95469], [-71.672678, 111.788551, 6.966682], [-71.589042, 111.79145, 6.925159], [-71.664147, 111.825632, 6.881361], [-71.681821, 111.880743, 6.95469], [-67.2589, 107.624, 5.54689]]}, {"shapeName": "R_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-64.596522, 108.655969, 11.086522], [-64.512886, 108.658867, 11.044999], [-64.503738, 108.566672, 11.056989], [-64.587374, 108.563773, 11.098513], [-64.596522, 108.655969, 11.086522], [-64.521419, 108.621785, 11.130314], [-64.503738, 108.566672, 11.056989], [-64.578843, 108.600855, 11.013192], [-64.512886, 108.658867, 11.044999], [-64.521419, 108.621785, 11.130314], [-64.587374, 108.563773, 11.098513], [-64.578843, 108.600855, 11.013192], [-64.596522, 108.655969, 11.086522], [-64.521419, 108.621785, 11.130314], [-67.2589, 107.624, 5.54689]]}]},
			"L_legBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_legBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.925836, 84.356899, 0.648821], [9.816067, 84.358734, 0.538412], [9.926418, 84.366231, 0.428825], [10.036187, 84.364396, 0.539234], [9.925836, 84.356899, 0.648821], [9.928973, 84.251613, 0.534167], [9.926418, 84.366231, 0.428825], [9.923281, 84.471527, 0.54348], [9.816067, 84.358734, 0.538412], [9.928973, 84.251613, 0.534167], [10.036187, 84.364396, 0.539234], [9.923281, 84.471527, 0.54348], [9.925836, 84.356899, 0.648821], [9.928973, 84.251613, 0.534167], [9.657635, 94.735269, 0.978146]]}, {"shapeName": "L_legBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.725621, 94.463514, 1.049368], [-0.728176, 94.578142, 0.944026], [-0.725039, 94.472846, 0.829371], [-0.722484, 94.358218, 0.934713], [-0.725621, 94.463514, 1.049368], [-0.83538, 94.465349, 0.938958], [-0.725039, 94.472846, 0.829371], [-0.61527, 94.471011, 0.939781], [-0.728176, 94.578142, 0.944026], [-0.83538, 94.465349, 0.938958], [-0.722484, 94.358218, 0.934713], [-0.61527, 94.471011, 0.939781], [-0.725621, 94.463514, 1.049368], [-0.83538, 94.465349, 0.938958], [9.657635, 94.735269, 0.978146]]}, {"shapeName": "L_legBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[9.575007, 95.172614, -9.39937], [9.682221, 95.285408, -9.394302], [9.795127, 95.178277, -9.398548], [9.687913, 95.065483, -9.403616], [9.575007, 95.172614, -9.39937], [9.685358, 95.180111, -9.508947], [9.795127, 95.178277, -9.398548], [9.684776, 95.170779, -9.288961], [9.682221, 95.285408, -9.394302], [9.685358, 95.180111, -9.508947], [9.687913, 95.065483, -9.403616], [9.684776, 95.170779, -9.288961], [9.575007, 95.172614, -9.39937], [9.685358, 95.180111, -9.508947], [9.657635, 94.735269, 0.978146]]}]},
			"C_head_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[8.3483, 177.43143, -0.32106], [0.0, 180.889402, -0.32106], [-8.3483, 177.43143, -0.32106], [-11.806272, 169.08313, -0.32106], [-8.3483, 160.73483, -0.32106], [0.0, 157.276858, -0.32106], [8.3483, 160.73483, -0.32106], [11.806272, 169.08313, -0.32106]]}]},
			"L_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[72.022147, 112.678394, 1.962781], [72.022147, 112.744453, 2.02884], [72.022147, 112.678394, 2.094898], [72.022147, 112.612336, 2.02884], [72.022147, 112.678394, 1.962781], [72.088199, 112.678394, 2.02884], [72.022147, 112.678394, 2.094898], [71.956088, 112.678394, 2.02884], [72.022147, 112.744453, 2.02884], [72.088199, 112.678394, 2.02884], [72.022147, 112.612336, 2.02884], [71.956088, 112.678394, 2.02884], [72.022147, 112.678394, 1.962781], [72.088199, 112.678394, 2.02884], [65.790263, 112.678394, 2.02884]]}, {"shapeName": "L_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.790263, 118.910278, 1.962781], [65.724205, 118.910278, 2.02884], [65.790263, 118.910278, 2.094898], [65.856322, 118.910278, 2.02884], [65.790263, 118.910278, 1.962781], [65.790263, 118.97633, 2.02884], [65.790263, 118.910278, 2.094898], [65.790263, 118.844219, 2.02884], [65.724205, 118.910278, 2.02884], [65.790263, 118.97633, 2.02884], [65.856322, 118.910278, 2.02884], [65.790263, 118.844219, 2.02884], [65.790263, 118.910278, 1.962781], [65.790263, 118.97633, 2.02884], [65.790263, 112.678394, 2.02884]]}, {"shapeName": "L_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.790263, 112.744453, 8.260723], [65.724205, 112.678394, 8.260723], [65.790263, 112.612336, 8.260723], [65.856322, 112.678394, 8.260723], [65.790263, 112.744453, 8.260723], [65.790263, 112.678394, 8.326776], [65.790263, 112.612336, 8.260723], [65.790263, 112.678394, 8.194665], [65.724205, 112.678394, 8.260723], [65.790263, 112.678394, 8.326776], [65.856322, 112.678394, 8.260723], [65.790263, 112.678394, 8.194665], [65.790263, 112.744453, 8.260723], [65.790263, 112.678394, 8.326776], [65.790263, 112.678394, 2.02884]]}]},
			"L_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_C_CTLShape", "degree": 3, "form": 2, "points": [[67.411826, 102.307633, -3.453911], [67.990818, 102.433869, -3.952632], [68.758898, 102.512672, -3.89153], [69.266135, 102.497879, -3.306396], [69.215398, 102.398156, -2.539995], [68.636406, 102.27192, -2.041274], [67.868326, 102.193117, -2.102376], [67.361089, 102.20791, -2.68751]]}]},
			"R_leg_IK_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-16.149683, 6.53346, -12.13866], [-11.986324, 6.53346, -15.035872], [-7.801441, 6.53346, -12.169838], [-6.046486, 6.53346, -5.219426], [-7.749479, 6.53346, 1.743899], [-11.912838, 6.53346, 4.641111], [-16.097721, 6.53346, 1.775077], [-17.852676, 6.53346, -5.175335]]}]},
			"L_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_B_CTLShape", "degree": 3, "form": 2, "points": [[67.067404, 107.026777, 4.752551], [67.698768, 107.463468, 4.649733], [68.072465, 107.994076, 5.072458], [67.969588, 108.307777, 5.773099], [67.450403, 108.220812, 6.34123], [66.819039, 107.784121, 6.444047], [66.445342, 107.253513, 6.021323], [66.548219, 106.939812, 5.320682]]}]},
			"L_leg_IK_switch_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[19.059134, 7.785757, -5.064513], [18.768526, 7.778282, -5.065599], [18.721233, 7.480124, -5.095296], [18.516948, 7.389669, -5.104529], [18.262688, 7.554347, -5.088457], [18.062531, 7.344574, -5.109547], [18.240953, 7.100454, -5.133606], [18.160791, 6.892732, -5.154351], [17.863989, 6.830294, -5.160908], [17.871536, 6.541101, -5.189649], [18.171196, 6.494006, -5.193978], [18.262084, 6.290712, -5.214082], [18.096633, 6.037718, -5.239428], [18.307463, 5.838518, -5.258983], [18.552793, 6.016047, -5.241045], [18.761521, 5.936216, -5.248736], [18.824301, 5.64089, -5.278022], [19.114909, 5.648366, -5.276937], [19.16223, 5.946524, -5.24724], [19.366515, 6.036979, -5.238007], [19.620774, 5.872301, -5.254079], [19.820914, 6.082073, -5.232988], [19.642508, 6.326221, -5.208927], [19.722672, 6.533916, -5.188184], [20.019446, 6.596353, -5.181628], [20.0119, 6.885546, -5.152886], [19.712267, 6.932642, -5.148557], [19.621378, 7.135964, -5.128451], [19.786811, 7.388929, -5.103107], [19.576, 7.58813, -5.083552], [19.33067, 7.410601, -5.10149], [19.121941, 7.490432, -5.093799], [19.059134, 7.785757, -5.064513]]}, {"shapeName": "L_leg_IK_switch_A_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[19.248969, 7.035339, -5.138893], [19.387827, 6.724799, -5.169602], [19.265352, 6.407537, -5.201287], [18.953306, 6.269424, -5.215384], [18.634493, 6.391309, -5.203643], [18.495636, 6.701849, -5.172934], [18.618111, 7.019111, -5.141249], [18.930139, 7.157224, -5.127151]]}, {"shapeName": "L_leg_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[17.867762, 6.685698, -5.175278], [11.949581, 6.53346, -5.197381]]}]},
			"L_innerBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_innerBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[15.701439, 1.91432, 6.545795], [15.710082, 2.030128, 6.649509], [15.719699, 1.926055, 6.764918], [15.711056, 1.810246, 6.661203], [15.701439, 1.91432, 6.545795], [15.820276, 1.920187, 6.646214], [15.719699, 1.926055, 6.764918], [15.600852, 1.920187, 6.664499], [15.710082, 2.030128, 6.649509], [15.820276, 1.920187, 6.646214], [15.711056, 1.810246, 6.661203], [15.600852, 1.920187, 6.664499], [15.701439, 1.91432, 6.545795], [15.820276, 1.920187, 6.646214], [5.359972, 1.920187, 7.51788]]}, {"shapeName": "L_innerBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[5.304875, 12.286033, 6.856704], [5.204288, 12.2919, 6.975409], [5.323135, 12.297767, 7.075827], [5.423722, 12.2919, 6.957123], [5.304875, 12.286033, 6.856704], [5.313518, 12.401831, 6.960419], [5.323135, 12.297767, 7.075827], [5.314492, 12.181959, 6.972113], [5.204288, 12.2919, 6.975409], [5.313518, 12.401831, 6.960419], [5.423722, 12.2919, 6.957123], [5.314492, 12.181959, 6.972113], [5.304875, 12.286033, 6.856704], [5.313518, 12.401831, 6.960419], [5.359972, 1.920187, 7.51788]]}, {"shapeName": "L_innerBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[6.220782, 2.583655, 17.847921], [6.111552, 2.473713, 17.862911], [6.221757, 2.363772, 17.859616], [6.330987, 2.473713, 17.844626], [6.220782, 2.583655, 17.847921], [6.230398, 2.47958, 17.96332], [6.221757, 2.363772, 17.859616], [6.21214, 2.467846, 17.744207], [6.111552, 2.473713, 17.862911], [6.230398, 2.47958, 17.96332], [6.330987, 2.473713, 17.844626], [6.21214, 2.467846, 17.744207], [6.220782, 2.583655, 17.847921], [6.230398, 2.47958, 17.96332], [5.359972, 1.920187, 7.51788]]}]},
			"R_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_D_CTLShape", "degree": 3, "form": 2, "points": [[-67.672164, 100.180648, -3.722059], [-68.210477, 100.478645, -4.192491], [-68.937896, 100.729169, -4.103109], [-69.428309, 100.785465, -3.506271], [-69.394439, 100.614558, -2.751596], [-68.856125, 100.316561, -2.281165], [-68.128706, 100.066038, -2.370546], [-67.638293, 100.009741, -2.967385]]}]},
			"L_wrist_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_wrist_FK_CTLShape", "degree": 3, "form": 2, "points": [[60.947959, 105.495478, -3.239875], [63.942523, 108.49226, -3.992872], [65.913244, 111.489042, -1.615757], [65.705694, 112.730347, 2.498998], [63.441462, 111.489042, 5.941022], [60.446898, 108.49226, 6.69402], [58.476178, 105.495478, 4.316905], [58.683727, 104.254173, 0.20215]]}]},
			"L_wrist_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_wrist_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.853237, 103.334378, 3.08561], [67.887766, 103.417374, 3.212742], [67.784782, 103.334378, 3.294894], [67.750253, 103.251383, 3.167762], [67.853237, 103.334378, 3.08561], [67.897885, 103.262044, 3.216052], [67.784782, 103.334378, 3.294894], [67.740127, 103.406719, 3.16445], [67.887766, 103.417374, 3.212742], [67.897885, 103.262044, 3.216052], [67.750253, 103.251383, 3.167762], [67.740127, 103.406719, 3.16445], [67.853237, 103.334378, 3.08561], [67.897885, 103.262044, 3.216052], [60.377304, 110.158951, 0.75611]]}, {"shapeName": "L_wrist_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[66.897928, 117.988639, 2.773133], [66.784817, 118.06098, 2.851973], [66.829472, 117.988639, 2.982417], [66.942582, 117.916298, 2.903577], [66.897928, 117.988639, 2.773133], [66.93245, 118.071627, 2.900263], [66.829472, 117.988639, 2.982417], [66.794943, 117.905644, 2.855285], [66.784817, 118.06098, 2.851973], [66.93245, 118.071627, 2.900263], [66.942582, 117.916298, 2.903577], [66.794943, 117.905644, 2.855285], [66.897928, 117.988639, 2.773133], [66.93245, 118.071627, 2.900263], [60.377304, 110.158951, 0.75611]]}, {"shapeName": "L_wrist_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[57.21705, 110.241946, 10.650393], [57.069411, 110.231292, 10.602101], [57.079537, 110.075955, 10.605414], [57.227176, 110.08661, 10.653706], [57.21705, 110.241946, 10.650393], [57.114069, 110.158951, 10.732536], [57.079537, 110.075955, 10.605414], [57.182521, 110.158951, 10.523262], [57.069411, 110.231292, 10.602101], [57.114069, 110.158951, 10.732536], [57.227176, 110.08661, 10.653706], [57.182521, 110.158951, 10.523262], [57.21705, 110.241946, 10.650393], [57.114069, 110.158951, 10.732536], [60.377304, 110.158951, 0.75611]]}]},
			"R_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-72.022184, 112.678, 1.962781], [-72.022184, 112.744059, 2.02884], [-72.022184, 112.678, 2.094898], [-72.022184, 112.611942, 2.02884], [-72.022184, 112.678, 1.962781], [-72.088236, 112.678, 2.02884], [-72.022184, 112.678, 2.094898], [-71.956125, 112.678, 2.02884], [-72.022184, 112.744059, 2.02884], [-72.088236, 112.678, 2.02884], [-72.022184, 112.611942, 2.02884], [-71.956125, 112.678, 2.02884], [-72.022184, 112.678, 1.962781], [-72.088236, 112.678, 2.02884], [-65.7903, 112.678, 2.02884]]}, {"shapeName": "R_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.7903, 118.909884, 1.962781], [-65.724242, 118.909884, 2.02884], [-65.7903, 118.909884, 2.094898], [-65.856359, 118.909884, 2.02884], [-65.7903, 118.909884, 1.962781], [-65.7903, 118.975936, 2.02884], [-65.7903, 118.909884, 2.094898], [-65.7903, 118.843825, 2.02884], [-65.724242, 118.909884, 2.02884], [-65.7903, 118.975936, 2.02884], [-65.856359, 118.909884, 2.02884], [-65.7903, 118.843825, 2.02884], [-65.7903, 118.909884, 1.962781], [-65.7903, 118.975936, 2.02884], [-65.7903, 112.678, 2.02884]]}, {"shapeName": "R_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-65.7903, 112.744059, 8.260723], [-65.724242, 112.678, 8.260723], [-65.7903, 112.611942, 8.260723], [-65.856359, 112.678, 8.260723], [-65.7903, 112.744059, 8.260723], [-65.7903, 112.678, 8.326776], [-65.7903, 112.611942, 8.260723], [-65.7903, 112.678, 8.194665], [-65.724242, 112.678, 8.260723], [-65.7903, 112.678, 8.326776], [-65.856359, 112.678, 8.260723], [-65.7903, 112.678, 8.194665], [-65.7903, 112.744059, 8.260723], [-65.7903, 112.678, 8.326776], [-65.7903, 112.678, 2.02884]]}]},
			"C_midNeck_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[11.449097, 163.541208, -10.685547], [0.0, 164.063636, -14.602831], [-11.449097, 163.541208, -10.685547], [-16.191458, 162.279953, -1.228365], [-11.449097, 161.018698, 8.228817], [0.0, 160.49627, 12.146101], [11.449097, 161.018698, 8.228817], [16.191458, 162.279953, -1.228365]]}]},
			"R_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_A_CTLShape", "degree": 3, "form": 2, "points": [[-61.82744, 110.101834, 1.973579], [-62.289002, 110.686496, 1.761395], [-62.512872, 111.353109, 2.086047], [-62.367909, 111.711181, 2.75736], [-61.939031, 111.550959, 3.382086], [-61.477469, 110.966298, 3.59427], [-61.253599, 110.299684, 3.269617], [-61.398562, 109.941613, 2.598305]]}]},
			"world_CTL": {"color": 1, "shapes": [{"shapeName": "world_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -577.7], [256.65, 0.0, -320.8], [192.4, 0.0, -320.8], [192.4, 0.0, -192.35], [320.85, 0.0, -192.35], [320.85, 0.0, -256.6], [577.7, 0.0, 0.0], [320.8, 0.0, 256.65], [320.8, 0.0, 192.4], [192.35, 0.0, 192.4], [192.35, 0.0, 320.85], [256.6, 0.0, 320.85], [0.0, 0.0, 577.7], [-256.65, 0.0, 320.8], [-192.4, 0.0, 320.8], [-192.4, 0.0, 192.35], [-320.85, 0.0, 192.35], [-320.85, 0.0, 256.6], [-577.7, 0.0, 0.0], [-320.8, 0.0, -256.65], [-320.8, 0.0, -192.4], [-192.35, 0.0, -192.4], [-192.35, 0.0, -320.85], [-256.6, 0.0, -320.85], [0.0, 0.0, -577.7], [50.3, 0.7, -528.3], [45.9, 0.0, -523.6], [45.9, 0.0, -504.4], [41.9, 0.0, -504.4], [42.15, 0.0, -523.75], [39.3, 0.0, -522.3], [39.4, 0.0, -513.9], [35.35, 0.0, -513.9], [35.35, 0.0, -522.3], [32.85, 0.0, -523.75], [32.85, 0.0, -504.1], [28.8, 0.0, -504.1], [28.8, 0.0, -524.25], [32.05, 0.0, -527.5], [37.05, 0.0, -525.0], [42.55, 0.0, -527.5], [45.9, 0.0, -523.7], [42.55, 0.0, -527.5], [37.1, 0.0, -525.05], [32.05, 0.0, -527.45], [22.3, 0.0, -527.5], [25.6, 0.0, -524.25], [25.6, 0.0, -507.4], [22.3, 0.0, -504.1], [11.75, 0.0, -504.1], [8.5, 0.0, -507.4], [8.5, 0.0, -524.25], [11.75, 0.0, -527.5], [22.3, 0.0, -527.5], [21.05, 0.0, -523.75], [21.55, 0.0, -508.25], [12.5, 0.0, -508.35], [12.55, 0.0, -523.75], [21.1, 0.0, -523.85], [22.3, 0.0, -527.5], [11.75, 0.0, -527.5], [5.0, 0.0, -527.5], [5.25, 0.0, -504.1], [-6.15, 0.0, -504.1], [-9.45, 0.0, -507.4], [-9.45, 0.0, -514.45], [-6.1, 0.0, -517.7], [-5.9, 0.0, -517.95], [-12.45, 0.0, -527.4], [-12.45, 0.0, -527.5], [-7.75, 0.0, -527.5], [-1.2, 0.0, -518.0], [1.25, 0.0, -518.0], [1.25, 0.0, -508.0], [-5.05, 0.0, -508.0], [-5.1, 0.0, -513.95], [1.25, 0.0, -513.95], [1.25, 0.0, -527.5], [5.0, 0.0, -527.5], [-32.15, 0.0, -527.5], [-32.15, 0.0, -523.75], [-19.05, 0.0, -523.7], [-19.05, 0.0, -504.1], [-15.0, 0.0, -504.1], [-15.0, 0.0, -527.5], [-49.2, 0.0, -527.5], [-52.2, 0.0, -524.25], [-52.45, 0.0, -507.4], [-49.2, 0.0, -504.1], [-35.35, 0.0, -504.1], [-35.35, 0.0, -527.5], [-39.45, 0.0, -523.75], [-39.35, 0.0, -507.9], [-47.9, 0.0, -507.9], [-47.8, 0.0, -523.65], [-39.3, 0.0, -523.85], [-35.25, 0.0, -527.5]]}]},
			"L_leg_IK_switch_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[19.849085, 7.924901, -5.04975], [19.526186, 7.916595, -5.050956], [19.473639, 7.585309, -5.083953], [19.246655, 7.484804, -5.094212], [18.964145, 7.667779, -5.076354], [18.741747, 7.434698, -5.099787], [18.939995, 7.163454, -5.12652], [18.850925, 6.932651, -5.14957], [18.521145, 6.863276, -5.156855], [18.52953, 6.54195, -5.18879], [18.862486, 6.489622, -5.1936], [18.963473, 6.26374, -5.215938], [18.779639, 5.982636, -5.2441], [19.013894, 5.761302, -5.265828], [19.286483, 5.958557, -5.245897], [19.518403, 5.869856, -5.254442], [19.588159, 5.541716, -5.286982], [19.911057, 5.550022, -5.285776], [19.963635, 5.881309, -5.25278], [20.190618, 5.981815, -5.242521], [20.473129, 5.798839, -5.260378], [20.695506, 6.031919, -5.236945], [20.497278, 6.303195, -5.210209], [20.586349, 6.533967, -5.187162], [20.916098, 6.603342, -5.179877], [20.907713, 6.924667, -5.147942], [20.574788, 6.976996, -5.143132], [20.4738, 7.202909, -5.120792], [20.657615, 7.483981, -5.092632], [20.42338, 7.705316, -5.070904], [20.150791, 7.508061, -5.090835], [19.91887, 7.596762, -5.08229], [19.849085, 7.924901, -5.04975]]}, {"shapeName": "L_leg_IK_switch_CTLShape1", "degree": 3, "form": 2, "points": [[20.060012, 7.091104, -5.132394], [20.214299, 6.746059, -5.166515], [20.078215, 6.393545, -5.201721], [19.731497, 6.240086, -5.217385], [19.377261, 6.375514, -5.204338], [19.222975, 6.720559, -5.170217], [19.359059, 7.073073, -5.135012], [19.705756, 7.226531, -5.119348]]}, {"shapeName": "L_leg_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[18.525338, 6.702613, -5.172823], [11.949581, 6.53346, -5.197381]]}]},
			"R_arm_IK_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-58.905781, 115.312495, 4.117887], [-54.343569, 109.805476, 2.625612], [-56.614696, 109.805476, -4.317723], [-61.176909, 115.312495, -2.825448], [-66.41104, 110.512425, -1.113392], [-61.848827, 105.005406, -2.605667], [-59.577699, 105.005406, 4.337668], [-64.139912, 110.512425, 5.829943], [-58.905781, 115.312495, 4.117887], [-61.176909, 115.312495, -2.825448], [-56.614696, 109.805476, -4.317723], [-61.848827, 105.005406, -2.605667], [-66.41104, 110.512425, -1.113392], [-64.139912, 110.512425, 5.829943], [-59.577699, 105.005406, 4.337668], [-54.343569, 109.805476, 2.625612]]}]},
			"C_midNeck_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[8.586823, 163.225895, -8.321251], [0.0, 163.617716, -11.259214], [-8.586823, 163.225895, -8.321251], [-12.143594, 162.279953, -1.228365], [-8.586823, 161.334011, 5.864521], [0.0, 160.94219, 8.802484], [8.586823, 161.334011, 5.864521], [12.143594, 162.279953, -1.228365]]}]},
			"R_leg_IK_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_leg_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-15.549669, 6.53346, -11.147049], [-11.981075, 6.53346, -13.630373], [-8.394033, 6.53346, -11.173772], [-6.889786, 6.53346, -5.216277], [-8.349494, 6.53346, 0.752288], [-11.918087, 6.53346, 3.235612], [-15.50513, 6.53346, 0.779011], [-17.009377, 6.53346, -5.178484]]}]},
			"R_legBase_CTL": {"color": 13, "shapes": [{"shapeName": "R_legBase_CTLShape", "degree": 3, "form": 0, "points": [[-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.651003, 94.628835, 3.487303], [-9.64027, 94.456623, 7.547185], [-9.636171, 94.390843, 9.097926], [-19.191023, 94.702304, 7.582854], [-25.104452, 95.026356, 3.545016], [-25.117717, 95.239223, -1.473299], [-19.225753, 95.259596, -5.555225], [-9.6791, 95.079694, -7.141634], [-9.675, 95.013915, -5.590894], [-9.664268, 94.841702, -1.531011], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146], [-9.657635, 94.735269, 0.978146]]}]},
			"L_leg_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[10.906483, 31.860978, 99.654038], [10.796635, 31.865842, 99.543799], [10.906907, 31.876368, 99.434382], [11.016756, 31.871504, 99.544621], [10.906483, 31.860978, 99.654038], [10.909548, 31.758891, 99.536524], [10.906907, 31.876368, 99.434382], [10.903842, 31.978465, 99.551898], [10.796635, 31.865842, 99.543799], [10.909548, 31.758891, 99.536524], [11.016756, 31.871504, 99.544621], [10.903842, 31.978465, 99.551898], [10.906483, 31.860978, 99.654038], [10.909548, 31.758891, 99.536524], [10.63755, 42.226301, 100.269409]]}, {"shapeName": "L_leg_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.254372, 41.951517, 100.34046], [0.251731, 42.069004, 100.23832], [0.254796, 41.966907, 100.120804], [0.257437, 41.84942, 100.222945], [0.254372, 41.951517, 100.34046], [0.144534, 41.956381, 100.230221], [0.254796, 41.966907, 100.120804], [0.364644, 41.962043, 100.231043], [0.251731, 42.069004, 100.23832], [0.144534, 41.956381, 100.230221], [0.257437, 41.84942, 100.222945], [0.364644, 41.962043, 100.231043], [0.254372, 41.951517, 100.34046], [0.144534, 41.956381, 100.230221], [10.63755, 42.226301, 100.269409]]}, {"shapeName": "L_leg_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[10.547509, 42.949428, 89.907946], [10.654717, 43.062051, 89.916044], [10.76763, 42.955091, 89.908768], [10.660423, 42.842468, 89.90067], [10.547509, 42.949428, 89.907946], [10.657782, 42.959954, 89.798539], [10.76763, 42.955091, 89.908768], [10.657358, 42.944564, 90.018185], [10.654717, 43.062051, 89.916044], [10.657782, 42.959954, 89.798539], [10.660423, 42.842468, 89.90067], [10.657358, 42.944564, 90.018185], [10.547509, 42.949428, 89.907946], [10.657782, 42.959954, 89.798539], [10.63755, 42.226301, 100.269409]]}]},
			"R_leg_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_leg_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-18.269184, 7.646613, -5.079276], [-18.010865, 7.639968, -5.080241], [-17.968827, 7.374939, -5.106638], [-17.787241, 7.294535, -5.114846], [-17.561232, 7.440915, -5.100559], [-17.383314, 7.25445, -5.119306], [-17.541912, 7.037455, -5.140692], [-17.470656, 6.852813, -5.159132], [-17.206833, 6.797313, -5.16496], [-17.213541, 6.540252, -5.190508], [-17.479905, 6.49839, -5.194356], [-17.560694, 6.317684, -5.212226], [-17.413627, 6.092801, -5.234756], [-17.601032, 5.915734, -5.252139], [-17.819102, 6.073537, -5.236194], [-18.004639, 6.002577, -5.24303], [-18.060443, 5.740065, -5.269062], [-18.318762, 5.74671, -5.268097], [-18.360824, 6.011739, -5.2417], [-18.542411, 6.092144, -5.233493], [-18.768419, 5.945763, -5.247779], [-18.946321, 6.132227, -5.229032], [-18.787739, 6.349248, -5.207644], [-18.858995, 6.533865, -5.189206], [-19.122795, 6.589365, -5.183378], [-19.116087, 6.846426, -5.15783], [-18.849746, 6.888288, -5.153982], [-18.768956, 7.069019, -5.13611], [-18.916008, 7.293877, -5.113582], [-18.72862, 7.470944, -5.096199], [-18.510549, 7.313141, -5.112144], [-18.325013, 7.384102, -5.105308], [-18.269184, 7.646613, -5.079276]]}, {"shapeName": "R_leg_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-18.437926, 6.979575, -5.145391], [-18.561355, 6.703539, -5.172688], [-18.452488, 6.421528, -5.200853], [-18.175114, 6.298761, -5.213384], [-17.891725, 6.407103, -5.202947], [-17.768296, 6.683139, -5.17565], [-17.877163, 6.96515, -5.147486], [-18.154521, 7.087917, -5.134954]]}, {"shapeName": "R_leg_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-17.210187, 6.668782, -5.177734], [-11.949581, 6.53346, -5.197381]]}]},
			"L_leg_IK_switch_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "L_leg_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[18.269184, 7.646613, -5.079276], [18.010865, 7.639968, -5.080241], [17.968827, 7.374939, -5.106638], [17.787241, 7.294535, -5.114846], [17.561232, 7.440915, -5.100559], [17.383314, 7.25445, -5.119306], [17.541912, 7.037455, -5.140692], [17.470656, 6.852813, -5.159132], [17.206833, 6.797313, -5.16496], [17.213541, 6.540252, -5.190508], [17.479905, 6.49839, -5.194356], [17.560694, 6.317684, -5.212226], [17.413627, 6.092801, -5.234756], [17.601032, 5.915734, -5.252139], [17.819102, 6.073537, -5.236194], [18.004639, 6.002577, -5.24303], [18.060443, 5.740065, -5.269062], [18.318762, 5.74671, -5.268097], [18.360824, 6.011739, -5.2417], [18.542411, 6.092144, -5.233493], [18.768419, 5.945763, -5.247779], [18.946321, 6.132227, -5.229032], [18.787739, 6.349248, -5.207644], [18.858995, 6.533865, -5.189206], [19.122795, 6.589365, -5.183378], [19.116087, 6.846426, -5.15783], [18.849746, 6.888288, -5.153982], [18.768956, 7.069019, -5.13611], [18.916008, 7.293877, -5.113582], [18.72862, 7.470944, -5.096199], [18.510549, 7.313141, -5.112144], [18.325013, 7.384102, -5.105308], [18.269184, 7.646613, -5.079276]]}, {"shapeName": "L_leg_IK_switch_B_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[18.437926, 6.979575, -5.145391], [18.561355, 6.703539, -5.172688], [18.452488, 6.421528, -5.200853], [18.175114, 6.298761, -5.213384], [17.891725, 6.407103, -5.202947], [17.768296, 6.683139, -5.17565], [17.877163, 6.96515, -5.147486], [18.154521, 7.087917, -5.134954]]}, {"shapeName": "L_leg_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[17.210187, 6.668782, -5.177734], [11.949581, 6.53346, -5.197381]]}]},
			"L_toe_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[15.628257, 6.410607, 9.915674], [12.050417, 7.889389, 10.013189], [8.472576, 6.410079, 9.924034], [6.99059, 2.83923, 9.700435], [8.472576, -0.731401, 9.473373], [12.050417, -2.210183, 9.375858], [15.628257, -0.730874, 9.465013], [17.110244, 2.839976, 9.688613]]}]},
			"L_leg_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[16.149683, 6.53346, -12.13866], [11.986324, 6.53346, -15.035872], [7.801441, 6.53346, -12.169838], [6.046486, 6.53346, -5.219426], [7.749479, 6.53346, 1.743899], [11.912838, 6.53346, 4.641111], [16.097721, 6.53346, 1.775077], [17.852676, 6.53346, -5.175335]]}]},
			"L_wrist_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[59.504578, 108.061203, -2.457204], [61.600773, 110.158951, -2.984302], [62.980277, 112.256698, -1.320321], [62.834993, 113.125612, 1.560007], [61.25003, 112.256698, 3.969424], [59.153835, 110.158951, 4.496523], [57.774331, 108.061203, 2.832542], [57.919615, 107.19229, -0.047787]]}]},
			"R_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_C_CTLShape", "degree": 3, "form": 2, "points": [[-69.967577, 102.035708, -0.463753], [-70.590994, 102.242668, -0.874129], [-71.296793, 102.510302, -0.700606], [-71.671526, 102.681833, -0.04483], [-71.49568, 102.656781, 0.709054], [-70.872263, 102.449821, 1.11943], [-70.166464, 102.182188, 0.945907], [-69.791731, 102.010657, 0.29013]]}]},
			"R_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-63.289976, 104.109776, 12.716333], [-63.207462, 104.118093, 12.759342], [-63.174212, 104.046487, 12.709397], [-63.256725, 104.03817, 12.666388], [-63.289976, 104.109776, 12.716333], [-63.252258, 104.036118, 12.759675], [-63.174212, 104.046487, 12.709397], [-63.211927, 104.120149, 12.666051], [-63.207462, 104.118093, 12.759342], [-63.252258, 104.036118, 12.759675], [-63.256725, 104.03817, 12.666388], [-63.211927, 104.120149, 12.666051], [-63.289976, 104.109776, 12.716333], [-63.252258, 104.036118, 12.759675], [-61.3296, 108.042, 8.29646]]}, {"shapeName": "R_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-59.063788, 111.843538, 12.684529], [-58.985739, 111.853911, 12.634247], [-58.948024, 111.780249, 12.677594], [-59.026072, 111.769876, 12.727876], [-59.063788, 111.843538, 12.684529], [-58.981277, 111.851851, 12.727534], [-58.948024, 111.780249, 12.677594], [-59.030537, 111.771932, 12.634584], [-58.985739, 111.853911, 12.634247], [-58.981277, 111.851851, 12.727534], [-59.026072, 111.769876, 12.727876], [-59.030537, 111.771932, 12.634584], [-59.063788, 111.843538, 12.684529], [-58.981277, 111.851851, 12.727534], [-61.3296, 108.042, 8.29646]]}, {"shapeName": "R_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-55.844443, 105.09666, 8.01581], [-55.848908, 105.098716, 7.922518], [-55.893706, 105.016738, 7.922855], [-55.889241, 105.014682, 8.016147], [-55.844443, 105.09666, 8.01581], [-55.811198, 105.025058, 7.965865], [-55.893706, 105.016738, 7.922855], [-55.926956, 105.088344, 7.9728], [-55.848908, 105.098716, 7.922518], [-55.811198, 105.025058, 7.965865], [-55.889241, 105.014682, 8.016147], [-55.926956, 105.088344, 7.9728], [-55.844443, 105.09666, 8.01581], [-55.811198, 105.025058, 7.965865], [-61.3296, 108.042, 8.29646]]}]},
			"L_legBase_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.696588, 93.230268, 0.91441], [9.759614, 90.795137, 0.811283], [9.783687, 89.864998, 0.771892], [9.744474, 90.5522, 6.5385], [9.672091, 92.837187, 10.181245], [9.594187, 95.847188, 10.308718], [9.540518, 98.432463, 6.872226], [9.531583, 99.60554, 1.1844], [9.555657, 98.6754, 1.145009], [9.618683, 96.24027, 1.041882], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146]]}]},
			"R_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.983227, 96.210884, -3.813497], [-69.066477, 96.215062, -3.771312], [-69.025369, 96.200312, -3.688728], [-68.94212, 96.196134, -3.730913], [-68.983227, 96.210884, -3.813497], [-69.011619, 96.140441, -3.759106], [-69.025369, 96.200312, -3.688728], [-68.996977, 96.270761, -3.743118], [-69.066477, 96.215062, -3.771312], [-69.011619, 96.140441, -3.759106], [-68.94212, 96.196134, -3.730913], [-68.996977, 96.270761, -3.743118], [-68.983227, 96.210884, -3.813497], [-69.011619, 96.140441, -3.759106], [-68.3136, 102.353, -2.99695]]}, {"shapeName": "R_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-74.15835, 103.251126, -4.964945], [-74.1721, 103.311004, -4.894566], [-74.200492, 103.240555, -4.840176], [-74.186743, 103.180678, -4.910555], [-74.15835, 103.251126, -4.964945], [-74.241594, 103.255304, -4.922758], [-74.200492, 103.240555, -4.840176], [-74.117243, 103.236376, -4.882361], [-74.1721, 103.311004, -4.894566], [-74.241594, 103.255304, -4.922758], [-74.186743, 103.180678, -4.910555], [-74.117243, 103.236376, -4.882361], [-74.15835, 103.251126, -4.964945], [-74.241594, 103.255304, -4.922758], [-68.3136, 102.353, -2.99695]]}, {"shapeName": "R_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-70.363604, 101.863806, 2.868108], [-70.294105, 101.919505, 2.896302], [-70.239248, 101.844877, 2.908508], [-70.308747, 101.789179, 2.880314], [-70.363604, 101.863806, 2.868108], [-70.322495, 101.849056, 2.950686], [-70.239248, 101.844877, 2.908508], [-70.280355, 101.859627, 2.825924], [-70.294105, 101.919505, 2.896302], [-70.322495, 101.849056, 2.950686], [-70.308747, 101.789179, 2.880314], [-70.280355, 101.859627, 2.825924], [-70.363604, 101.863806, 2.868108], [-70.322495, 101.849056, 2.950686], [-68.3136, 102.353, -2.99695]]}]},
			"L_shoulder_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [4.604762, 149.074616, 5.289387], [7.700241, 149.777541, 3.473083], [8.882612, 150.046035, 2.779315], [3.348719, 149.777541, -3.943105], [-2.436153, 149.074616, -6.710262], [-6.262394, 148.205749, -4.465177], [-6.668482, 147.502824, 1.934588], [-3.49933, 147.23433, 10.044544], [-2.31696, 147.502824, 9.350776], [0.77852, 148.205749, 7.534472], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193]]}]},
			"L_toe_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_CTLShape", "degree": 3, "form": 2, "points": [[16.028765, 6.647633, 12.471784], [12.053386, 8.290724, 12.580134], [8.078008, 6.647047, 12.481073], [6.431356, 2.679436, 12.23263], [8.078008, -1.287932, 11.980338], [12.053386, -2.931023, 11.871989], [16.028765, -1.287345, 11.97105], [17.675417, 2.680265, 12.219493]]}]},
			"C_midTorso_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.869458, 119.757893, -7.056772], [0.0, 119.555915, -9.419335], [-6.869458, 119.757893, -7.056772], [-9.714875, 120.245514, -1.353029], [-6.869458, 120.733135, 4.350714], [0.0, 120.935113, 6.713276], [6.869458, 120.733135, 4.350714], [9.714875, 120.245514, -1.353029]]}]},
			"R_toe_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-12.062575, 2.295348, 20.067304], [-11.952478, 2.185461, 20.060499], [-12.062575, 2.07559, 20.053437], [-12.172673, 2.185477, 20.060242], [-12.062575, 2.295348, 20.067304], [-12.062704, 2.178536, 20.170239], [-12.062575, 2.07559, 20.053437], [-12.062446, 2.192403, 19.950492], [-11.952478, 2.185461, 20.060499], [-12.062704, 2.178536, 20.170239], [-12.172673, 2.185477, 20.060242], [-12.062446, 2.192403, 19.950492], [-12.062575, 2.295348, 20.067304], [-12.062704, 2.178536, 20.170239], [-12.050417, 2.839603, 9.694524]]}, {"shapeName": "R_toe_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.663951, 2.948716, 9.713592], [-1.663823, 2.845771, 9.596779], [-1.663951, 2.728958, 9.699724], [-1.66408, 2.831903, 9.816537], [-1.663951, 2.948716, 9.713592], [-1.553864, 2.838829, 9.706787], [-1.663951, 2.728958, 9.699724], [-1.774049, 2.838845, 9.706529], [-1.663823, 2.845771, 9.596779], [-1.553864, 2.838829, 9.706787], [-1.66408, 2.831903, 9.816537], [-1.774049, 2.838845, 9.706529], [-1.663951, 2.948716, 9.713592], [-1.553864, 2.838829, 9.706787], [-12.050417, 2.839603, 9.694524]]}, {"shapeName": "R_toe_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-11.94032, -7.526259, 9.040518], [-12.050288, -7.519317, 8.930511], [-12.160514, -7.526243, 9.040261], [-12.050546, -7.533185, 9.150268], [-11.94032, -7.526259, 9.040518], [-12.050417, -7.63612, 9.033456], [-12.160514, -7.526243, 9.040261], [-12.050417, -7.416372, 9.047323], [-12.050288, -7.519317, 8.930511], [-12.050417, -7.63612, 9.033456], [-12.050546, -7.533185, 9.150268], [-12.050417, -7.416372, 9.047323], [-11.94032, -7.526259, 9.040518], [-12.050417, -7.63612, 9.033456], [-12.050417, 2.839603, 9.694524]]}]},
			"L_loArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_loArm_FK_CTLShape", "degree": 3, "form": 2, "points": [[39.102463, 122.487606, -9.129404], [41.926603, 124.720771, -11.485743], [44.556542, 128.043882, -10.740442], [45.451695, 130.510306, -7.330079], [44.0877, 130.675251, -3.252404], [41.26356, 128.442086, -0.896066], [38.633621, 125.118975, -1.641367], [37.738468, 122.652551, -5.051729]]}]},
			"R_shoulder_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-3.967055, 148.929805, 5.663568], [-6.030708, 149.398422, 4.452699], [-6.818955, 149.577418, 3.990187], [-3.129693, 149.398422, -0.491427], [0.726888, 148.929805, -2.336198], [3.277716, 148.35056, -0.839475], [3.548441, 147.881943, 3.427035], [1.435673, 147.702947, 8.833673], [0.647426, 147.881943, 8.371161], [-1.416227, 148.35056, 7.160291], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193]]}]},
			"L_arm_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_arm_IK_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[59.069284, 114.739879, 3.744357], [55.013984, 109.844751, 2.41789], [57.032764, 109.844751, -3.753964], [61.088064, 114.739879, -2.427497], [65.740625, 110.47315, -0.90567], [61.685324, 105.578022, -2.232137], [59.666544, 105.578022, 3.939717], [63.721844, 110.47315, 5.266184], [59.069284, 114.739879, 3.744357], [61.088064, 114.739879, -2.427497], [57.032764, 109.844751, -3.753964], [61.685324, 105.578022, -2.232137], [65.740625, 110.47315, -0.90567], [63.721844, 110.47315, 5.266184], [59.666544, 105.578022, 3.939717], [55.013984, 109.844751, 2.41789]]}]},
			"L_upArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[24.195701, 144.488118, -3.337514], [24.296192, 144.571585, -3.252792], [24.245633, 144.501171, -3.123452], [24.145142, 144.417705, -3.208174], [24.195701, 144.488118, -3.337514], [24.296779, 144.416172, -3.243452], [24.245633, 144.501171, -3.123452], [24.144548, 144.573124, -3.217513], [24.296192, 144.571585, -3.252792], [24.296779, 144.416172, -3.243452], [24.145142, 144.417705, -3.208174], [24.144548, 144.573124, -3.217513], [24.195701, 144.488118, -3.337514], [24.296779, 144.416172, -3.243452], [17.039658, 151.898346, -2.006913]]}, {"shapeName": "L_upArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[24.139623, 159.150257, -4.218522], [24.08847, 159.235263, -4.098521], [24.189555, 159.16331, -4.004461], [24.240709, 159.078303, -4.124461], [24.139623, 159.150257, -4.218522], [24.240107, 159.233716, -4.133798], [24.189555, 159.16331, -4.004461], [24.089065, 159.079843, -4.089182], [24.08847, 159.235263, -4.098521], [24.240107, 159.233716, -4.133798], [24.240709, 159.078303, -4.124461], [24.089065, 159.079843, -4.089182], [24.139623, 159.150257, -4.218522], [24.240107, 159.233716, -4.133798], [17.039658, 151.898346, -2.006913]]}, {"shapeName": "L_upArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[19.470445, 152.591004, 8.067928], [19.318801, 152.592544, 8.103207], [19.319396, 152.437124, 8.112546], [19.47104, 152.435584, 8.077267], [19.470445, 152.591004, 8.067928], [19.419884, 152.52059, 8.197258], [19.319396, 152.437124, 8.112546], [19.369954, 152.507538, 7.983206], [19.318801, 152.592544, 8.103207], [19.419884, 152.52059, 8.197258], [19.47104, 152.435584, 8.077267], [19.369954, 152.507538, 7.983206], [19.470445, 152.591004, 8.067928], [19.419884, 152.52059, 8.197258], [17.039658, 151.898346, -2.006913]]}]},
			"R_loArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_loArm_FK_CTLShape", "degree": 3, "form": 2, "points": [[-39.102463, 122.487606, -9.129404], [-41.926603, 124.720771, -11.485743], [-44.556542, 128.043882, -10.740442], [-45.451695, 130.510306, -7.330079], [-44.0877, 130.675251, -3.252404], [-41.26356, 128.442086, -0.896066], [-38.633621, 125.118975, -1.641367], [-37.738468, 122.652551, -5.051729]]}]},
			"R_arm_IK_switch_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "R_arm_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-64.443992, 113.79613, 2.086302], [-64.302788, 113.625684, 2.040115], [-64.109813, 113.745852, 1.976994], [-63.961777, 113.668475, 1.928572], [-63.936255, 113.434064, 1.920224], [-63.721856, 113.418592, 1.850095], [-63.666165, 113.647122, 1.831879], [-63.509476, 113.702545, 1.780627], [-63.333889, 113.555764, 1.723193], [-63.171884, 113.704334, 1.670202], [-63.286111, 113.907386, 1.707565], [-63.21255, 114.063119, 1.683504], [-62.989759, 114.089976, 1.61063], [-62.975054, 114.315554, 1.60582], [-63.192278, 114.374159, 1.676873], [-63.244921, 114.53902, 1.694092], [-63.105428, 114.723748, 1.648465], [-63.246632, 114.894194, 1.694652], [-63.439621, 114.774041, 1.757777], [-63.587657, 114.851419, 1.806199], [-63.613178, 115.08583, 1.814547], [-63.827569, 115.101291, 1.884673], [-63.883284, 114.872758, 1.902897], [-64.039957, 114.817349, 1.954144], [-64.215531, 114.964114, 2.011574], [-64.377536, 114.815544, 2.064564], [-64.263322, 114.612508, 2.027206], [-64.336899, 114.456761, 2.051272], [-64.559665, 114.429907, 2.124138], [-64.57438, 114.20434, 2.128951], [-64.357156, 114.145734, 2.057898], [-64.304513, 113.980874, 2.040679], [-64.443992, 113.79613, 2.086302]]}, {"shapeName": "R_arm_IK_switch_C_OFF_CTLShape1", "degree": 3, "form": 2, "points": [[-64.103827, 114.283687, 1.975036], [-63.99147, 114.521588, 1.938284], [-63.752134, 114.606214, 1.859999], [-63.526041, 114.487991, 1.786045], [-63.445607, 114.236207, 1.759735], [-63.557963, 113.998305, 1.796487], [-63.797299, 113.913679, 1.874772], [-64.023384, 114.031892, 1.948723]]}, {"shapeName": "R_arm_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[-63.252886, 113.630049, 1.696698], [-60.377304, 110.158951, 0.75611]]}]},
			"R_arm_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.853237, 103.334378, 3.08561], [-67.887766, 103.417374, 3.212742], [-67.784782, 103.334378, 3.294894], [-67.750253, 103.251383, 3.167762], [-67.853237, 103.334378, 3.08561], [-67.897885, 103.262044, 3.216052], [-67.784782, 103.334378, 3.294894], [-67.740127, 103.406719, 3.16445], [-67.887766, 103.417374, 3.212742], [-67.897885, 103.262044, 3.216052], [-67.750253, 103.251383, 3.167762], [-67.740127, 103.406719, 3.16445], [-67.853237, 103.334378, 3.08561], [-67.897885, 103.262044, 3.216052], [-60.377304, 110.158951, 0.75611]]}, {"shapeName": "R_arm_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-66.897928, 117.988639, 2.773133], [-66.784817, 118.06098, 2.851973], [-66.829472, 117.988639, 2.982417], [-66.942582, 117.916298, 2.903577], [-66.897928, 117.988639, 2.773133], [-66.93245, 118.071627, 2.900263], [-66.829472, 117.988639, 2.982417], [-66.794943, 117.905644, 2.855285], [-66.784817, 118.06098, 2.851973], [-66.93245, 118.071627, 2.900263], [-66.942582, 117.916298, 2.903577], [-66.794943, 117.905644, 2.855285], [-66.897928, 117.988639, 2.773133], [-66.93245, 118.071627, 2.900263], [-60.377304, 110.158951, 0.75611]]}, {"shapeName": "R_arm_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-57.21705, 110.241946, 10.650393], [-57.069411, 110.231292, 10.602101], [-57.079537, 110.075955, 10.605414], [-57.227176, 110.08661, 10.653706], [-57.21705, 110.241946, 10.650393], [-57.114069, 110.158951, 10.732536], [-57.079537, 110.075955, 10.605414], [-57.182521, 110.158951, 10.523262], [-57.069411, 110.231292, 10.602101], [-57.114069, 110.158951, 10.732536], [-57.227176, 110.08661, 10.653706], [-57.182521, 110.158951, 10.523262], [-57.21705, 110.241946, 10.650393], [-57.114069, 110.158951, 10.732536], [-60.377304, 110.158951, 0.75611]]}]},
			"L_legBase_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_CTLShape", "degree": 3, "form": 0, "points": [[9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.651003, 94.628835, 3.487303], [9.64027, 94.456623, 7.547185], [9.636171, 94.390843, 9.097926], [19.191023, 94.702304, 7.582854], [25.104452, 95.026356, 3.545016], [25.117717, 95.239223, -1.473299], [19.225753, 95.259596, -5.555225], [9.6791, 95.079694, -7.141634], [9.675, 95.013915, -5.590894], [9.664268, 94.841702, -1.531011], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146], [9.657635, 94.735269, 0.978146]]}]},
			"L_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_C_CTLShape", "degree": 3, "form": 2, "points": [[69.967577, 102.035708, -0.463753], [70.590994, 102.242668, -0.874129], [71.296793, 102.510302, -0.700606], [71.671526, 102.681833, -0.04483], [71.49568, 102.656781, 0.709054], [70.872263, 102.449821, 1.11943], [70.166464, 102.182188, 0.945907], [69.791731, 102.010657, 0.29013]]}]},
			"L_shoulder_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_shoulder_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [4.179624, 148.978075, 5.538841], [6.587219, 149.524795, 4.12616], [7.506841, 149.733623, 3.586563], [3.202701, 149.524795, -1.641986], [-1.296643, 148.978075, -3.79422], [-4.272609, 148.30229, -2.048042], [-4.588455, 147.75557, 2.929553], [-2.123559, 147.546742, 9.237296], [-1.203937, 147.75557, 8.697699], [1.203658, 148.30229, 7.285018], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193], [2.691641, 148.640182, 6.41193]]}]},
			"L_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[63.955528, 103.426107, 15.50329], [63.870696, 103.441109, 15.539429], [63.841316, 103.359703, 15.504254], [63.926147, 103.344701, 15.468115], [63.955528, 103.426107, 15.50329], [63.916694, 103.362285, 15.559373], [63.841316, 103.359703, 15.504254], [63.880148, 103.423527, 15.448165], [63.870696, 103.441109, 15.539429], [63.916694, 103.362285, 15.559373], [63.926147, 103.344701, 15.468115], [63.880148, 103.423527, 15.448165], [63.955528, 103.426107, 15.50329], [63.916694, 103.362285, 15.559373], [62.174511, 106.281792, 10.257932]]}, {"shapeName": "L_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[59.616031, 110.862479, 13.621297], [59.540652, 110.859899, 13.566173], [59.501819, 110.796074, 13.622261], [59.577199, 110.798654, 13.677385], [59.616031, 110.862479, 13.621297], [59.531202, 110.877476, 13.657433], [59.501819, 110.796074, 13.622261], [59.586651, 110.781073, 13.586122], [59.540652, 110.859899, 13.566173], [59.531202, 110.877476, 13.657433], [59.577199, 110.798654, 13.677385], [59.586651, 110.781073, 13.586122], [59.616031, 110.862479, 13.621297], [59.531202, 110.877476, 13.657433], [62.174511, 106.281792, 10.257932]]}, {"shapeName": "L_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[56.759466, 103.197729, 10.339053], [56.768917, 103.180148, 10.247789], [56.814916, 103.101322, 10.267739], [56.805465, 103.118903, 10.359002], [56.759466, 103.197729, 10.339053], [56.73009, 103.116327, 10.303878], [56.814916, 103.101322, 10.267739], [56.844297, 103.182728, 10.302914], [56.768917, 103.180148, 10.247789], [56.73009, 103.116327, 10.303878], [56.805465, 103.118903, 10.359002], [56.844297, 103.182728, 10.302914], [56.759466, 103.197729, 10.339053], [56.73009, 103.116327, 10.303878], [62.174511, 106.281792, 10.257932]]}]},
			"R_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_B_CTLShape", "degree": 3, "form": 2, "points": [[-67.067404, 107.026777, 4.752551], [-67.698768, 107.463468, 4.649733], [-68.072465, 107.994076, 5.072458], [-67.969588, 108.307777, 5.773099], [-67.450403, 108.220812, 6.34123], [-66.819039, 107.784121, 6.444047], [-66.445342, 107.253513, 6.021323], [-66.548219, 106.939812, 5.320682]]}]},
			"R_toe_IK_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-14.833182, 5.61705, 9.86653], [-12.050417, 6.767214, 9.942375], [-9.267652, 5.61664, 9.873032], [-8.114996, 2.839313, 9.699121], [-9.267652, 0.062155, 9.522518], [-12.050417, -1.088009, 9.446673], [-14.833182, 0.062565, 9.516016], [-15.985838, 2.839893, 9.689926]]}]},
			"L_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_D_CTLShape", "degree": 3, "form": 2, "points": [[70.739219, 101.36381, 7.653476], [71.499817, 101.506841, 7.6231], [72.028494, 101.767854, 8.125357], [72.015558, 101.99395, 8.866035], [71.468587, 102.052686, 9.411253], [70.707989, 101.909655, 9.44163], [70.179312, 101.648643, 8.939372], [70.192248, 101.422547, 8.198695]]}]},
			"R_toe_IK_CTL": {"color": 13, "shapes": [{"shapeName": "R_toe_IK_CTLShape", "degree": 3, "form": 2, "points": [[-16.028765, 6.647633, 12.471784], [-12.053386, 8.290724, 12.580134], [-8.078008, 6.647047, 12.481073], [-6.431356, 2.679436, 12.23263], [-8.078008, -1.287932, 11.980338], [-12.053386, -2.931023, 11.871989], [-16.028765, -1.287345, 11.97105], [-17.675417, 2.680265, 12.219493]]}]},
			"L_toe_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toe_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[12.062575, 2.295348, 20.067304], [11.952478, 2.185461, 20.060499], [12.062575, 2.07559, 20.053437], [12.172673, 2.185477, 20.060242], [12.062575, 2.295348, 20.067304], [12.062704, 2.178536, 20.170239], [12.062575, 2.07559, 20.053437], [12.062446, 2.192403, 19.950492], [11.952478, 2.185461, 20.060499], [12.062704, 2.178536, 20.170239], [12.172673, 2.185477, 20.060242], [12.062446, 2.192403, 19.950492], [12.062575, 2.295348, 20.067304], [12.062704, 2.178536, 20.170239], [12.050417, 2.839603, 9.694524]]}, {"shapeName": "L_toe_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.663951, 2.948716, 9.713592], [1.663823, 2.845771, 9.596779], [1.663951, 2.728958, 9.699724], [1.66408, 2.831903, 9.816537], [1.663951, 2.948716, 9.713592], [1.553864, 2.838829, 9.706787], [1.663951, 2.728958, 9.699724], [1.774049, 2.838845, 9.706529], [1.663823, 2.845771, 9.596779], [1.553864, 2.838829, 9.706787], [1.66408, 2.831903, 9.816537], [1.774049, 2.838845, 9.706529], [1.663951, 2.948716, 9.713592], [1.553864, 2.838829, 9.706787], [12.050417, 2.839603, 9.694524]]}, {"shapeName": "L_toe_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[11.94032, -7.526259, 9.040518], [12.050288, -7.519317, 8.930511], [12.160514, -7.526243, 9.040261], [12.050546, -7.533185, 9.150268], [11.94032, -7.526259, 9.040518], [12.050417, -7.63612, 9.033456], [12.160514, -7.526243, 9.040261], [12.050417, -7.416372, 9.047323], [12.050288, -7.519317, 8.930511], [12.050417, -7.63612, 9.033456], [12.050546, -7.533185, 9.150268], [12.050417, -7.416372, 9.047323], [11.94032, -7.526259, 9.040518], [12.050417, -7.63612, 9.033456], [12.050417, 2.839603, 9.694524]]}]},
			"L_wrist_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_wrist_IK_CTLShape", "degree": 3, "form": 2, "points": [[62.765366, 103.828787, -2.645411], [65.75993, 106.825569, -3.398409], [67.73065, 109.822351, -1.021293], [67.523101, 111.063656, 3.093462], [65.258868, 109.822351, 6.535486], [62.264304, 106.825569, 7.288484], [60.293584, 103.828787, 4.911369], [60.501133, 102.587482, 0.796614]]}]},
			"R_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-72.863584, 96.4947, 0.362803], [-72.934118, 96.523367, 0.416937], [-72.881944, 96.508222, 0.492937], [-72.81141, 96.479555, 0.438803], [-72.863584, 96.4947, 0.362803], [-72.895458, 96.439514, 0.431105], [-72.881944, 96.508222, 0.492937], [-72.850068, 96.563414, 0.424635], [-72.934118, 96.523367, 0.416937], [-72.895458, 96.439514, 0.431105], [-72.81141, 96.479555, 0.438803], [-72.850068, 96.563414, 0.424635], [-72.863584, 96.4947, 0.362803], [-72.895458, 96.439514, 0.431105], [-70.7316, 102.346, 0.12265]]}, {"shapeName": "R_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-76.510489, 104.405853, -0.973792], [-76.496973, 104.474567, -0.91196], [-76.52885, 104.419375, -0.843658], [-76.542366, 104.350661, -0.905489], [-76.510489, 104.405853, -0.973792], [-76.581018, 104.434518, -0.919656], [-76.52885, 104.419375, -0.843658], [-76.458316, 104.390708, -0.897792], [-76.496973, 104.474567, -0.91196], [-76.581018, 104.434518, -0.919656], [-76.542366, 104.350661, -0.905489], [-76.458316, 104.390708, -0.897792], [-76.510489, 104.405853, -0.973792], [-76.581018, 104.434518, -0.919656], [-70.7316, 102.346, 0.12265]]}, {"shapeName": "R_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-71.659007, 103.005751, 6.250079], [-71.574956, 103.045798, 6.257776], [-71.536299, 102.961939, 6.271944], [-71.620349, 102.921892, 6.264247], [-71.659007, 103.005751, 6.250079], [-71.606832, 102.990606, 6.326073], [-71.536299, 102.961939, 6.271944], [-71.588473, 102.977084, 6.195944], [-71.574956, 103.045798, 6.257776], [-71.606832, 102.990606, 6.326073], [-71.620349, 102.921892, 6.264247], [-71.588473, 102.977084, 6.195944], [-71.659007, 103.005751, 6.250079], [-71.606832, 102.990606, 6.326073], [-70.7316, 102.346, 0.12265]]}]},
			"C_jaw_CTL": {"color": 18, "shapes": [{"shapeName": "C_jaw_CTLShape", "degree": 3, "form": 0, "points": [[0.0, 170.572105, 0.741723], [0.0, 170.572105, 0.741723], [0.0, 170.572105, 0.741723], [-3.348563, 170.572105, 0.741723], [-8.766626, 170.572105, 0.741723], [-10.836147, 170.572105, 0.741723], [-8.766626, 159.919984, 12.577422], [-3.348563, 153.336605, 19.892293], [3.348563, 153.336605, 19.892293], [8.766626, 159.919984, 12.577422], [10.836147, 170.572105, 0.741723], [8.766626, 170.572105, 0.741723], [3.348563, 170.572105, 0.741723], [0.0, 170.572105, 0.741723], [0.0, 170.572105, 0.741723], [0.0, 170.572105, 0.741723]]}]},
			"R_arm_PV_CTL": {"color": 13, "shapes": [{"shapeName": "R_arm_PV_CTLShape", "degree": 1, "form": 0, "points": [[-29.586224, 109.61085, -104.425449], [-29.586224, 107.58159, -104.425449], [-29.586224, 107.58159, -106.454709], [-29.586224, 109.61085, -106.454709], [-31.615484, 109.61085, -106.454709], [-31.615484, 107.58159, -106.454709], [-31.615484, 107.58159, -104.425449], [-31.615484, 109.61085, -104.425449], [-29.586224, 109.61085, -104.425449], [-29.586224, 109.61085, -106.454709], [-29.586224, 107.58159, -106.454709], [-31.615484, 107.58159, -106.454709], [-31.615484, 109.61085, -106.454709], [-31.615484, 109.61085, -104.425449], [-31.615484, 107.58159, -104.425449], [-29.586224, 107.58159, -104.425449]]}]},
			"R_wrist_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_wrist_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.853237, 103.334378, 3.08561], [-67.887766, 103.417374, 3.212742], [-67.784782, 103.334378, 3.294894], [-67.750253, 103.251383, 3.167762], [-67.853237, 103.334378, 3.08561], [-67.897885, 103.262044, 3.216052], [-67.784782, 103.334378, 3.294894], [-67.740127, 103.406719, 3.16445], [-67.887766, 103.417374, 3.212742], [-67.897885, 103.262044, 3.216052], [-67.750253, 103.251383, 3.167762], [-67.740127, 103.406719, 3.16445], [-67.853237, 103.334378, 3.08561], [-67.897885, 103.262044, 3.216052], [-60.377304, 110.158951, 0.75611]]}, {"shapeName": "R_wrist_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-66.897928, 117.988639, 2.773133], [-66.784817, 118.06098, 2.851973], [-66.829472, 117.988639, 2.982417], [-66.942582, 117.916298, 2.903577], [-66.897928, 117.988639, 2.773133], [-66.93245, 118.071627, 2.900263], [-66.829472, 117.988639, 2.982417], [-66.794943, 117.905644, 2.855285], [-66.784817, 118.06098, 2.851973], [-66.93245, 118.071627, 2.900263], [-66.942582, 117.916298, 2.903577], [-66.794943, 117.905644, 2.855285], [-66.897928, 117.988639, 2.773133], [-66.93245, 118.071627, 2.900263], [-60.377304, 110.158951, 0.75611]]}, {"shapeName": "R_wrist_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-57.21705, 110.241946, 10.650393], [-57.069411, 110.231292, 10.602101], [-57.079537, 110.075955, 10.605414], [-57.227176, 110.08661, 10.653706], [-57.21705, 110.241946, 10.650393], [-57.114069, 110.158951, 10.732536], [-57.079537, 110.075955, 10.605414], [-57.182521, 110.158951, 10.523262], [-57.069411, 110.231292, 10.602101], [-57.114069, 110.158951, 10.732536], [-57.227176, 110.08661, 10.653706], [-57.182521, 110.158951, 10.523262], [-57.21705, 110.241946, 10.650393], [-57.114069, 110.158951, 10.732536], [-60.377304, 110.158951, 0.75611]]}]},
			"R_loLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_loLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-11.102607, 38.975053, -1.862549], [-10.992676, 38.983113, -1.972517], [-11.102865, 38.996836, -2.081664], [-11.212796, 38.988776, -1.971695], [-11.102607, 38.975053, -1.862549], [-11.105594, 38.876434, -1.98299], [-11.102865, 38.996836, -2.081664], [-11.099878, 39.095465, -1.961222], [-10.992676, 38.983113, -1.972517], [-11.105594, 38.876434, -1.98299], [-11.212796, 38.988776, -1.971695], [-11.099878, 39.095465, -1.961222], [-11.102607, 38.975053, -1.862549], [-11.105594, 38.876434, -1.98299], [-10.833121, 49.318016, -0.945259]]}, {"shapeName": "R_loLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.450027, 49.040035, -0.874478], [-0.447298, 49.160448, -0.97315], [-0.450285, 49.061819, -1.093592], [-0.453014, 48.941406, -0.99492], [-0.450027, 49.040035, -0.874478], [-0.340106, 49.048096, -0.984446], [-0.450285, 49.061819, -1.093592], [-0.560216, 49.053758, -0.983624], [-0.447298, 49.160448, -0.97315], [-0.340106, 49.048096, -0.984446], [-0.453014, 48.941406, -0.99492], [-0.560216, 49.053758, -0.983624], [-0.450027, 49.040035, -0.874478], [-0.340106, 49.048096, -0.984446], [-10.833121, 49.318016, -0.945259]]}, {"shapeName": "R_loLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-10.735229, 50.342693, -11.281186], [-10.842431, 50.455045, -11.26989], [-10.955349, 50.348355, -11.280364], [-10.848147, 50.236003, -11.291659], [-10.735229, 50.342693, -11.281186], [-10.845418, 50.356414, -11.390322], [-10.955349, 50.348355, -11.280364], [-10.84516, 50.334632, -11.171217], [-10.842431, 50.455045, -11.26989], [-10.845418, 50.356414, -11.390322], [-10.848147, 50.236003, -11.291659], [-10.84516, 50.334632, -11.171217], [-10.735229, 50.342693, -11.281186], [-10.845418, 50.356414, -11.390322], [-10.833121, 49.318016, -0.945259]]}]},
			"C_neckBase_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[8.586823, 156.430465, -9.227522], [0.0, 153.201675, -12.648348], [-8.586823, 156.430465, -9.227522], [-12.143594, 159.105135, -1.651774], [-8.586823, 154.538582, 4.95825], [0.0, 150.52615, 7.413351], [8.586823, 154.538582, 4.95825], [12.143594, 159.105135, -1.651774]]}]},
			"R_shoulder_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_shoulder_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-4.179624, 148.978075, 5.538841], [-6.587219, 149.524795, 4.12616], [-7.506841, 149.733623, 3.586563], [-3.202701, 149.524795, -1.641986], [1.296643, 148.978075, -3.79422], [4.272609, 148.30229, -2.048042], [4.588455, 147.75557, 2.929553], [2.123559, 147.546742, 9.237296], [1.203937, 147.75557, 8.697699], [-1.203658, 148.30229, 7.285018], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193], [-2.691641, 148.640182, 6.41193]]}]},
			"C_reverseJaw_CTL": {"color": 18, "shapes": [{"shapeName": "C_reverseJaw_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 185.65548, 14.316751], [0.776557, 185.770295, 14.420084], [1.43489, 186.097272, 14.714364], [1.874793, 186.586607, 15.154765], [2.02926, 187.163817, 15.674254], [1.874793, 187.741028, 16.193743], [1.43489, 188.230363, 16.634144], [0.776557, 188.55734, 16.928423], [0.0, 188.672155, 17.031757], [-0.776557, 188.55734, 16.928423], [-1.43489, 188.230363, 16.634144], [-1.874793, 187.741028, 16.193743], [-2.02926, 187.163817, 15.674254], [-1.874793, 186.586607, 15.154765], [-1.43489, 186.097272, 14.714364], [-0.776557, 185.770295, 14.420084], [0.0, 185.65548, 14.316751], [0.0, 170.572105, 0.741723]]}]},
			"L_toe_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[15.23072, 6.013829, 9.891102], [12.050417, 7.328301, 9.977782], [8.870114, 6.01336, 9.898533], [7.552793, 2.839271, 9.699778], [8.870114, -0.334623, 9.497945], [12.050417, -1.649096, 9.411266], [15.23072, -0.334154, 9.490514], [16.548041, 2.839934, 9.689269]]}]},
			"R_innerBall_CTL": {"color": 20, "shapes": [{"shapeName": "R_innerBall_CTLShape", "degree": 1, "form": 0, "points": [[-3.421859, 1.97426, 8.696084], [-3.342211, 0.906999, 7.740282], [-4.348846, 1.920187, 7.602138], [-3.421859, 1.97426, 8.696084], [-2.326595, 1.920187, 7.770654], [-3.342211, 0.906999, 7.740282], [-3.253583, 1.866115, 6.676707], [-2.326595, 1.920187, 7.770654], [-3.33323, 2.933375, 7.63251], [-3.421859, 1.97426, 8.696084], [-4.348846, 1.920187, 7.602138], [-3.253583, 1.866115, 6.676707], [-3.33323, 2.933375, 7.63251], [-4.348846, 1.920187, 7.602138]]}]},
		}

		controlShapes.set_data(data)