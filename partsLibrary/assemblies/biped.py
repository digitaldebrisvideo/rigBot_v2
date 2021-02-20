# -*- rigBot: assembly -*-
from rigBot import guide
from rigBot.data import controlShapes
import maya.cmds as mc

class Biped():
	"""Generated assembly build."""

	def __init__(self):
		pass

	def build_guide(self):
		"""Build Assembly guide parts"""

		guide.build("worldRoot", **{'side': u'C', 'name': u''})
		guide.build("hand", **{'createIkCtrls': False, 'parent': u'L_wrist_end_JNT', 'numberFingers': 4, 'createThumb': True, 'pickWalkParent': u'L_arm_IK_CTL', 'numberThumbJoints': 3, 'numberJoints': 4, 'side': u'L', 'name': u''})
		guide.build("foot", **{'name': u'', 'parent': u'L_leg_end_JNT', 'switchCtrlDriver': u'L_leg_IK_switch_CTL', 'attrCtrlDriver': u'L_leg_IK_CTL', 'ikCtrlParent': u'L_leg_IK_handle_driver_JNT', 'pickWalkParent': u'L_leg_PV_CTL', 'fkCtrlParent': u'L_legEnd_FK_CTL', 'side': u'L'})
		guide.build("encoreBipedLeg", **{'flipJoints': False, 'name': u'', 'parent': u'C_hip_JNT', 'transOrientiation': u'world', 'fkAnkleJoint': u'L_ankle_JNT', 'side': u'L', 'pickWalkParent': u'C_hip_CTL', 'ikHandleParent': u'L_foot_IK_handle_driver_JNT', 'numberTwistJoints': 4, 'makeBendy': False})
		guide.build("encoreBipedArm", **{'name': u'', 'parent': u'C_chest_JNT', 'transOrientiation': u'world', 'numberTwistJoints': 4, 'side': u'L', 'pickWalkParent': u'C_chest_CTL', 'doubleClavicle': False, 'ikHandleParent': u'', 'makeBendy': True})
		guide.build("torso", **{'numberMidCtrls': 1, 'parent': u'C_root_JNT', 'pickWalkParent': u'world_CTL', 'numberJoints': 6, 'side': u'C', 'name': u''})
		guide.build("neck", **{'numberMidCtrls': 1, 'parent': u'C_chest_end_JNT', 'pickWalkParent': u'C_chest_CTL', 'createReverseJaw': True, 'name': u'', 'numberJoints': 4, 'side': u'C', 'createJaw': True})

		#Position nodes
		if mc.objExists("L_hand_guide"):
			if not mc.getAttr("L_hand_guide.rotateOrder", l=1):
				mc.setAttr("L_hand_guide.rotateOrder", 0)

			mc.xform("L_hand_guide", a=1, t=[6.925000190734863, 15.299516677856445, -6.938893903907228e-17])
			mc.xform("L_hand_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_hand_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_foot_guide"):
			if not mc.getAttr("L_foot_guide.rotateOrder", l=1):
				mc.setAttr("L_foot_guide.rotateOrder", 0)

			mc.xform("L_foot_guide", a=1, t=[1.001780266464723, 0.6865488949137433, 0.0])
			mc.xform("L_foot_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_foot_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_encoreBipedLeg_guide"):
			if not mc.getAttr("L_encoreBipedLeg_guide.rotateOrder", l=1):
				mc.setAttr("L_encoreBipedLeg_guide.rotateOrder", 0)

			mc.xform("L_encoreBipedLeg_guide", a=1, t=[1.0, 9.514179229736328, 0.0])
			mc.xform("L_encoreBipedLeg_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_encoreBipedLeg_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_encoreBipedArm_guide"):
			if not mc.getAttr("L_encoreBipedArm_guide.rotateOrder", l=1):
				mc.setAttr("L_encoreBipedArm_guide.rotateOrder", 0)

			mc.xform("L_encoreBipedArm_guide", a=1, t=[0.925000011920929, 15.299516677856445, 0.0])
			mc.xform("L_encoreBipedArm_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_encoreBipedArm_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_worldRoot_guide"):
			if not mc.getAttr("C_worldRoot_guide.rotateOrder", l=1):
				mc.setAttr("C_worldRoot_guide.rotateOrder", 0)

			mc.xform("C_worldRoot_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_torso_guide"):
			if not mc.getAttr("C_torso_guide.rotateOrder", l=1):
				mc.setAttr("C_torso_guide.rotateOrder", 0)

			mc.xform("C_torso_guide", a=1, t=[0.0, 10.2734340364422, 0.0])
			mc.xform("C_torso_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_torso_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_neck_guide"):
			if not mc.getAttr("C_neck_guide.rotateOrder", l=1):
				mc.setAttr("C_neck_guide.rotateOrder", 0)

			mc.xform("C_neck_guide", a=1, t=[0.0, 18.556284762484356, 0.0])
			mc.xform("C_neck_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_neck_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_root_JNT_PLC"):
			mc.xform("C_root_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_root_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_root_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

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

			mc.xform("L_leg_end_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_end_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_end_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_leg_IK_handle_driver_JNT_PLC"):
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_leg_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_A_JNT_PLC", a=1, t=[0.0, -0.8000000000000007, 0.1])
			mc.xform("L_upLeg_twist_A_JNT_PLC", a=1, ro=[179.99999999999997, -7.125016348901798, -90.0])
			mc.xform("L_upLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_A_JNT_PLC"):
			if not mc.getAttr("L_upLeg_shaper_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_A_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_A_JNT_PLC", a=1, t=[0.0, -4.8, 0.4])
			mc.xform("L_loLeg_twist_A_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 172.8749836510982, 90.0])
			mc.xform("L_loLeg_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_A_JNT_PLC"):
			if not mc.getAttr("L_loLeg_shaper_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_B_JNT_PLC", a=1, t=[0.0, -1.5999999999999996, 0.2])
			mc.xform("L_upLeg_twist_B_JNT_PLC", a=1, ro=[179.99999999999997, -7.125016348901798, -90.0])
			mc.xform("L_upLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_B_JNT_PLC"):
			if not mc.getAttr("L_upLeg_shaper_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_B_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_B_JNT_PLC", a=1, t=[0.0, -5.6, 0.3])
			mc.xform("L_loLeg_twist_B_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 172.8749836510982, 90.0])
			mc.xform("L_loLeg_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_B_JNT_PLC"):
			if not mc.getAttr("L_loLeg_shaper_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_C_JNT_PLC", a=1, t=[0.0, -2.4000000000000004, 0.30000000000000004])
			mc.xform("L_upLeg_twist_C_JNT_PLC", a=1, ro=[179.99999999999997, -7.125016348901798, -90.0])
			mc.xform("L_upLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_C_JNT_PLC"):
			if not mc.getAttr("L_upLeg_shaper_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_C_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_C_JNT_PLC", a=1, t=[0.0, -6.4, 0.19999999999999996])
			mc.xform("L_loLeg_twist_C_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 172.8749836510982, 90.0])
			mc.xform("L_loLeg_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_C_JNT_PLC"):
			if not mc.getAttr("L_loLeg_shaper_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("L_upLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_twist_D_JNT_PLC", a=1, t=[0.0, -3.200000000000001, 0.4])
			mc.xform("L_upLeg_twist_D_JNT_PLC", a=1, ro=[179.99999999999997, -7.125016348901798, -90.0])
			mc.xform("L_upLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_D_JNT_PLC"):
			if not mc.getAttr("L_upLeg_shaper_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_twist_D_JNT_PLC"):
			if not mc.getAttr("L_loLeg_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_twist_D_JNT_PLC", a=1, t=[0.0, -7.2, 0.09999999999999998])
			mc.xform("L_loLeg_twist_D_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 172.8749836510982, 90.0])
			mc.xform("L_loLeg_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_D_JNT_PLC"):
			if not mc.getAttr("L_loLeg_shaper_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("C_reverseJaw_JNT_PLC"):
			mc.xform("C_reverseJaw_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_reverseJaw_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_clavicle_JNT_PLC"):
			if not mc.getAttr("L_clavicle_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_clavicle_JNT_PLC.rotateOrder", 0)

			mc.xform("L_clavicle_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_JNT_PLC"):
			if not mc.getAttr("L_upArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_JNT_PLC"):
			if not mc.getAttr("L_loArm_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("L_clavicleEnd_JNT_PLC"):
			if not mc.getAttr("L_clavicleEnd_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_clavicleEnd_JNT_PLC.rotateOrder", 0)

			mc.xform("L_clavicleEnd_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_clavicleEnd_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_clavicleEnd_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_arm_IK_handle_driver_JNT_PLC"):
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_IK_handle_driver_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_A_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_A_JNT_PLC", a=1, t=[2.4000000000000004, 0.0, -0.1])
			mc.xform("L_upArm_twist_A_JNT_PLC", a=1, ro=[0.0, 14.036243467926484, 0.0])
			mc.xform("L_upArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_shaper_A_JNT_PLC"):
			if not mc.getAttr("L_upArm_shaper_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_shaper_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_A_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_A_JNT_PLC", a=1, t=[4.4, 0.0, -0.4])
			mc.xform("L_loArm_twist_A_JNT_PLC", a=1, ro=[0.0, -14.036243467926473, 0.0])
			mc.xform("L_loArm_twist_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_A_JNT_PLC"):
			if not mc.getAttr("L_loArm_shaper_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_shaper_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_B_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_B_JNT_PLC", a=1, t=[2.8, 0.0, -0.2])
			mc.xform("L_upArm_twist_B_JNT_PLC", a=1, ro=[0.0, 14.036243467926484, 0.0])
			mc.xform("L_upArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_shaper_B_JNT_PLC"):
			if not mc.getAttr("L_upArm_shaper_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_shaper_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_B_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_B_JNT_PLC", a=1, t=[4.800000000000001, 0.0, -0.3])
			mc.xform("L_loArm_twist_B_JNT_PLC", a=1, ro=[0.0, -14.036243467926473, 0.0])
			mc.xform("L_loArm_twist_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_B_JNT_PLC"):
			if not mc.getAttr("L_loArm_shaper_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_shaper_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_C_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_C_JNT_PLC", a=1, t=[3.2, 0.0, -0.30000000000000004])
			mc.xform("L_upArm_twist_C_JNT_PLC", a=1, ro=[0.0, 14.036243467926484, 0.0])
			mc.xform("L_upArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_shaper_C_JNT_PLC"):
			if not mc.getAttr("L_upArm_shaper_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_shaper_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_C_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_C_JNT_PLC", a=1, t=[5.2, 0.0, -0.19999999999999996])
			mc.xform("L_loArm_twist_C_JNT_PLC", a=1, ro=[0.0, -14.036243467926473, 0.0])
			mc.xform("L_loArm_twist_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_C_JNT_PLC"):
			if not mc.getAttr("L_loArm_shaper_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_shaper_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_twist_D_JNT_PLC"):
			if not mc.getAttr("L_upArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_twist_D_JNT_PLC", a=1, t=[3.5999999999999996, 0.0, -0.4])
			mc.xform("L_upArm_twist_D_JNT_PLC", a=1, ro=[0.0, 14.036243467926484, 0.0])
			mc.xform("L_upArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_shaper_D_JNT_PLC"):
			if not mc.getAttr("L_upArm_shaper_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upArm_shaper_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_twist_D_JNT_PLC"):
			if not mc.getAttr("L_loArm_twist_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_twist_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_twist_D_JNT_PLC", a=1, t=[5.6000000000000005, 0.0, -0.09999999999999998])
			mc.xform("L_loArm_twist_D_JNT_PLC", a=1, ro=[0.0, -14.036243467926473, 0.0])
			mc.xform("L_loArm_twist_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_D_JNT_PLC"):
			if not mc.getAttr("L_loArm_shaper_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_loArm_shaper_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("C_world_PIV_CTL"):
			mc.xform("C_world_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_world_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_world_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_visibility_PIV_CTL"):
			mc.xform("C_visibility_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_visibility_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_visibility_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("L_upLeg_shaper_A_PIV_CTL"):
			if not mc.getAttr("L_upLeg_shaper_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_A_PIV_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_A_PIV_CTL"):
			if not mc.getAttr("L_loLeg_shaper_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_A_PIV_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_B_PIV_CTL"):
			if not mc.getAttr("L_upLeg_shaper_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_B_PIV_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_B_PIV_CTL"):
			if not mc.getAttr("L_loLeg_shaper_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_B_PIV_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_C_PIV_CTL"):
			if not mc.getAttr("L_upLeg_shaper_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_C_PIV_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_C_PIV_CTL"):
			if not mc.getAttr("L_loLeg_shaper_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_C_PIV_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_D_PIV_CTL"):
			if not mc.getAttr("L_upLeg_shaper_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_D_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_D_PIV_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_D_PIV_CTL"):
			if not mc.getAttr("L_loLeg_shaper_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_D_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_D_PIV_CTL", a=1, ro=[180.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("L_upArm_shaper_A_PIV_CTL"):
			if not mc.getAttr("L_upArm_shaper_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upArm_shaper_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_A_PIV_CTL"):
			if not mc.getAttr("L_loArm_shaper_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loArm_shaper_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_shaper_B_PIV_CTL"):
			if not mc.getAttr("L_upArm_shaper_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upArm_shaper_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_B_PIV_CTL"):
			if not mc.getAttr("L_loArm_shaper_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loArm_shaper_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_shaper_C_PIV_CTL"):
			if not mc.getAttr("L_upArm_shaper_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upArm_shaper_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_C_PIV_CTL"):
			if not mc.getAttr("L_loArm_shaper_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loArm_shaper_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_shaper_D_PIV_CTL"):
			if not mc.getAttr("L_upArm_shaper_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_D_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upArm_shaper_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_D_PIV_CTL"):
			if not mc.getAttr("L_loArm_shaper_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_D_PIV_CTL.rotateOrder", 0)

			mc.xform("L_loArm_shaper_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("L_clavicle_PIV_CTL"):
			if not mc.getAttr("L_clavicle_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_clavicle_PIV_CTL.rotateOrder", 0)

			mc.xform("L_clavicle_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_clavicle_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_A_PIV_CTL"):
			if not mc.getAttr("L_bendyArm_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_B_PIV_CTL"):
			if not mc.getAttr("L_bendyArm_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_C_PIV_CTL"):
			if not mc.getAttr("L_bendyArm_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

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
			mc.xform("world_A_OFF_CTL", r=1, s=[0.4611898214335878, 0.4611898214335878, 0.4611898214335878])

		if mc.objExists("world_CTL"):
			if not mc.getAttr("world_CTL.numOffsetCtrls", l=1):
				mc.setAttr("world_CTL.numOffsetCtrls", 1)

			if not mc.getAttr("world_CTL.mirrorMode", l=1):
				mc.setAttr("world_CTL.mirrorMode", 0)

			if not mc.getAttr("world_CTL.rotateOrder", l=1):
				mc.setAttr("world_CTL.rotateOrder", 0)

			mc.xform("world_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("world_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("world_CTL", r=1, s=[0.4611898214335878, 0.4611898214335878, 0.4611898214335878])

		if mc.objExists("visibility_CTL"):
			if not mc.getAttr("visibility_CTL.mirrorMode", l=1):
				mc.setAttr("visibility_CTL.mirrorMode", 0)

			if not mc.getAttr("visibility_CTL.rotateOrder", l=1):
				mc.setAttr("visibility_CTL.rotateOrder", 0)

			mc.xform("visibility_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("visibility_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("visibility_CTL", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("L_upLeg_shaper_A_CTL"):
			if not mc.getAttr("L_upLeg_shaper_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_upLeg_shaper_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upLeg_shaper_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_A_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_A_CTL"):
			if not mc.getAttr("L_loLeg_shaper_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_loLeg_shaper_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loLeg_shaper_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_A_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_B_CTL"):
			if not mc.getAttr("L_upLeg_shaper_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_upLeg_shaper_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upLeg_shaper_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_B_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_B_CTL"):
			if not mc.getAttr("L_loLeg_shaper_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_loLeg_shaper_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loLeg_shaper_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_B_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_C_CTL"):
			if not mc.getAttr("L_upLeg_shaper_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_upLeg_shaper_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upLeg_shaper_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_C_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_C_CTL"):
			if not mc.getAttr("L_loLeg_shaper_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_loLeg_shaper_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loLeg_shaper_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_C_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upLeg_shaper_D_CTL"):
			if not mc.getAttr("L_upLeg_shaper_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_upLeg_shaper_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upLeg_shaper_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_upLeg_shaper_D_CTL.rotateOrder", 0)

			mc.xform("L_upLeg_shaper_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upLeg_shaper_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loLeg_shaper_D_CTL"):
			if not mc.getAttr("L_loLeg_shaper_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_loLeg_shaper_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loLeg_shaper_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_loLeg_shaper_D_CTL.rotateOrder", 0)

			mc.xform("L_loLeg_shaper_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loLeg_shaper_D_CTL", r=1, s=[1.0, 1.0, 1.0])

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
			mc.xform("L_legBase_D_OFF_CTL", r=1, s=[1.0000000000000004, 1.0, 1.0000000000000004])

		if mc.objExists("L_legBase_C_OFF_CTL"):
			if not mc.getAttr("L_legBase_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_legBase_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_legBase_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_C_OFF_CTL", r=1, s=[0.9999999999999996, 1.0, 0.9999999999999996])

		if mc.objExists("L_legBase_B_OFF_CTL"):
			if not mc.getAttr("L_legBase_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_legBase_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_legBase_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_B_OFF_CTL", r=1, s=[1.0000000000000004, 1.0, 1.0000000000000004])

		if mc.objExists("L_legBase_A_OFF_CTL"):
			if not mc.getAttr("L_legBase_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_legBase_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_legBase_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_legBase_A_OFF_CTL", r=1, s=[0.9999999999999998, 1.0, 0.9999999999999998])

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

		if mc.objExists("L_upArm_shaper_A_CTL"):
			if not mc.getAttr("L_upArm_shaper_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_upArm_shaper_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upArm_shaper_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_A_CTL.rotateOrder", 0)

			mc.xform("L_upArm_shaper_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_A_CTL"):
			if not mc.getAttr("L_loArm_shaper_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_loArm_shaper_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loArm_shaper_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_A_CTL.rotateOrder", 0)

			mc.xform("L_loArm_shaper_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_shaper_B_CTL"):
			if not mc.getAttr("L_upArm_shaper_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_upArm_shaper_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upArm_shaper_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_B_CTL.rotateOrder", 0)

			mc.xform("L_upArm_shaper_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_B_CTL"):
			if not mc.getAttr("L_loArm_shaper_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_loArm_shaper_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loArm_shaper_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_B_CTL.rotateOrder", 0)

			mc.xform("L_loArm_shaper_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_shaper_C_CTL"):
			if not mc.getAttr("L_upArm_shaper_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_upArm_shaper_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upArm_shaper_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_C_CTL.rotateOrder", 0)

			mc.xform("L_upArm_shaper_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_C_CTL"):
			if not mc.getAttr("L_loArm_shaper_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_loArm_shaper_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loArm_shaper_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_C_CTL.rotateOrder", 0)

			mc.xform("L_loArm_shaper_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upArm_shaper_D_CTL"):
			if not mc.getAttr("L_upArm_shaper_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_upArm_shaper_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upArm_shaper_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_upArm_shaper_D_CTL.rotateOrder", 0)

			mc.xform("L_upArm_shaper_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upArm_shaper_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_loArm_shaper_D_CTL"):
			if not mc.getAttr("L_loArm_shaper_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_loArm_shaper_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_loArm_shaper_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_loArm_shaper_D_CTL.rotateOrder", 0)

			mc.xform("L_loArm_shaper_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_loArm_shaper_D_CTL", r=1, s=[1.0, 1.0, 1.0])

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
			mc.xform("L_arm_PV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_arm_PV_CTL", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("L_bendyArm_A_D_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_A_C_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_A_B_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_A_A_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_A_CTL"):
			if not mc.getAttr("L_bendyArm_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_bendyArm_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_bendyArm_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_bendyArm_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_bendyArm_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_A_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_B_D_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_B_C_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_B_B_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_B_A_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_B_CTL"):
			if not mc.getAttr("L_bendyArm_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_bendyArm_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_bendyArm_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_bendyArm_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_bendyArm_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_B_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_C_D_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_C_C_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_C_B_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_C_A_OFF_CTL"):
			if not mc.getAttr("L_bendyArm_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_bendyArm_C_CTL"):
			if not mc.getAttr("L_bendyArm_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_bendyArm_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_bendyArm_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_bendyArm_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_bendyArm_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_bendyArm_C_CTL.rotateOrder", 0)

			mc.xform("L_bendyArm_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_bendyArm_C_CTL", r=1, s=[1.0, 1.0, 1.0])

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

		# Apply contro shapes data
		data = {
			"C_cog_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_CTLShape", "degree": 3, "form": 2, "points": [[2.350836, 9.773434, -2.350836], [0.0, 9.773434, -3.324582], [-2.350836, 9.773434, -2.350836], [-3.324582, 9.773434, 0.0], [-2.350836, 9.773434, 2.350836], [0.0, 9.773434, 3.324582], [2.350836, 9.773434, 2.350836], [3.324582, 9.773434, 0.0]]}]},
			"L_bendyArm_C_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[6.022014, 15.43285, -0.638057], [6.022014, 15.51285, -0.638057], [6.070521, 15.299517, -0.832086], [6.022014, 15.086183, -0.638057], [6.022014, 15.166183, -0.638057], [5.957338, 15.166183, -0.379353], [5.957338, 14.899517, -0.379353], [5.976741, 14.899517, -0.456964], [5.925, 14.699517, -0.25], [5.873259, 14.899517, -0.043036], [5.892662, 14.899517, -0.120647], [5.892662, 15.166183, -0.120647], [5.827986, 15.166183, 0.138057], [5.827986, 15.086183, 0.138057], [5.779479, 15.299517, 0.332086], [5.827986, 15.51285, 0.138057], [5.827986, 15.43285, 0.138057], [5.892662, 15.43285, -0.120647], [5.892662, 15.699517, -0.120647], [5.873259, 15.699517, -0.043036], [5.925, 15.899517, -0.25], [5.976741, 15.699517, -0.456964], [5.957338, 15.699517, -0.379353], [5.957338, 15.43285, -0.379353], [6.022014, 15.43285, -0.638057]]}]},
			"L_leg_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_CTLShape", "degree": 3, "form": 2, "points": [[1.587709, 1.514179, -0.979515], [1.0, 1.514179, -1.385242], [0.412291, 1.514179, -0.979515], [0.168855, 1.514179, 0.0], [0.412291, 1.514179, 0.979515], [1.0, 1.514179, 1.385242], [1.587709, 1.514179, 0.979515], [1.831145, 1.514179, 0.0]]}]},
			"L_outterBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_outterBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.525451, 0.186549, 0.989149], [2.525451, 0.1974, 1.0], [2.525451, 0.186549, 1.010851], [2.525451, 0.175698, 1.0], [2.525451, 0.186549, 0.989149], [2.536301, 0.186549, 1.0], [2.525451, 0.186549, 1.010851], [2.5146, 0.186549, 1.0], [2.525451, 0.1974, 1.0], [2.536301, 0.186549, 1.0], [2.525451, 0.175698, 1.0], [2.5146, 0.186549, 1.0], [2.525451, 0.186549, 0.989149], [2.536301, 0.186549, 1.0], [1.50178, 0.186549, 1.0]]}, {"shapeName": "L_outterBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.50178, 1.21022, 0.989149], [1.490929, 1.21022, 1.0], [1.50178, 1.21022, 1.010851], [1.512631, 1.21022, 1.0], [1.50178, 1.21022, 0.989149], [1.50178, 1.22107, 1.0], [1.50178, 1.21022, 1.010851], [1.50178, 1.199369, 1.0], [1.490929, 1.21022, 1.0], [1.50178, 1.22107, 1.0], [1.512631, 1.21022, 1.0], [1.50178, 1.199369, 1.0], [1.50178, 1.21022, 0.989149], [1.50178, 1.22107, 1.0], [1.50178, 0.186549, 1.0]]}, {"shapeName": "L_outterBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.50178, 0.1974, 2.023671], [1.490929, 0.186549, 2.023671], [1.50178, 0.175698, 2.023671], [1.512631, 0.186549, 2.023671], [1.50178, 0.1974, 2.023671], [1.50178, 0.186549, 2.034521], [1.50178, 0.175698, 2.023671], [1.50178, 0.186549, 2.01282], [1.490929, 0.186549, 2.023671], [1.50178, 0.186549, 2.034521], [1.512631, 0.186549, 2.023671], [1.50178, 0.186549, 2.01282], [1.50178, 0.1974, 2.023671], [1.50178, 0.186549, 2.034521], [1.50178, 0.186549, 1.0]]}]},
			"C_torso_FK_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 11.297105, -0.010851], [-0.010851, 11.297105, 0.0], [0.0, 11.297105, 0.010851], [0.010851, 11.297105, 0.0], [0.0, 11.297105, -0.010851], [0.0, 11.307955, 0.0], [0.0, 11.297105, 0.010851], [0.0, 11.286254, 0.0], [-0.010851, 11.297105, 0.0], [0.0, 11.307955, 0.0], [0.010851, 11.297105, 0.0], [0.0, 11.286254, 0.0], [0.0, 11.297105, -0.010851], [0.0, 11.307955, 0.0], [0.0, 10.273434, 0.0]]}, {"shapeName": "C_torso_FK_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.023671, 10.273434, -0.010851], [-1.023671, 10.262583, 0.0], [-1.023671, 10.273434, 0.010851], [-1.023671, 10.284285, 0.0], [-1.023671, 10.273434, -0.010851], [-1.034521, 10.273434, 0.0], [-1.023671, 10.273434, 0.010851], [-1.01282, 10.273434, 0.0], [-1.023671, 10.262583, 0.0], [-1.034521, 10.273434, 0.0], [-1.023671, 10.284285, 0.0], [-1.01282, 10.273434, 0.0], [-1.023671, 10.273434, -0.010851], [-1.034521, 10.273434, 0.0], [0.0, 10.273434, 0.0]]}, {"shapeName": "C_torso_FK_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.010851, 10.273434, 1.023671], [0.0, 10.262583, 1.023671], [0.010851, 10.273434, 1.023671], [0.0, 10.284285, 1.023671], [-0.010851, 10.273434, 1.023671], [0.0, 10.273434, 1.034521], [0.010851, 10.273434, 1.023671], [0.0, 10.273434, 1.01282], [0.0, 10.262583, 1.023671], [0.0, 10.273434, 1.034521], [0.0, 10.284285, 1.023671], [0.0, 10.273434, 1.01282], [-0.010851, 10.273434, 1.023671], [0.0, 10.273434, 1.034521], [0.0, 10.273434, 0.0]]}]},
			"L_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_A_CTLShape", "degree": 3, "form": 2, "points": [[7.190535, 15.183006, 0.132458], [7.175, 15.299517, 0.083771], [7.159465, 15.416027, 0.132458], [7.153031, 15.464288, 0.25], [7.159465, 15.416027, 0.367542], [7.175, 15.299517, 0.416229], [7.190535, 15.183006, 0.367542], [7.19697, 15.134746, 0.25]]}]},
			"L_loLeg_shaper_C_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_C_CTLShape", "degree": 1, "form": 0, "points": [[2.5, 3.114179, 0.2], [2.511418, 3.038234, 0.190507], [2.543935, 2.973851, 0.182459], [2.592598, 2.93083, 0.177081], [2.65, 2.915724, 0.175193], [2.707402, 2.93083, 0.177081], [2.756065, 2.973851, 0.182459], [2.788582, 3.038234, 0.190507], [2.8, 3.114179, 0.2], [2.788582, 3.190124, 0.209493], [2.756065, 3.254507, 0.217541], [2.707402, 3.297528, 0.222919], [2.65, 3.312635, 0.224807], [2.592598, 3.297528, 0.222919], [2.543935, 3.254507, 0.217541], [2.511418, 3.190124, 0.209493], [2.5, 3.114179, 0.2], [1.0, 3.114179, 0.2]]}]},
			"L_bendyArm_C_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[6.009887, 15.416184, -0.58955], [6.009887, 15.486184, -0.58955], [6.052331, 15.299517, -0.759325], [6.009887, 15.11285, -0.58955], [6.009887, 15.18285, -0.58955], [5.953296, 15.18285, -0.363184], [5.953296, 14.949517, -0.363184], [5.970273, 14.949517, -0.431093], [5.925, 14.774517, -0.25], [5.879727, 14.949517, -0.068907], [5.896704, 14.949517, -0.136816], [5.896704, 15.18285, -0.136816], [5.840113, 15.18285, 0.08955], [5.840113, 15.11285, 0.08955], [5.797669, 15.299517, 0.259325], [5.840113, 15.486184, 0.08955], [5.840113, 15.416184, 0.08955], [5.896704, 15.416184, -0.136816], [5.896704, 15.649517, -0.136816], [5.879727, 15.649517, -0.068907], [5.925, 15.824517, -0.25], [5.970273, 15.649517, -0.431093], [5.953296, 15.649517, -0.363184], [5.953296, 15.416184, -0.363184], [6.009887, 15.416184, -0.58955]]}]},
			"L_leg_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.528938, 1.514179, -0.881563], [1.0, 1.514179, -1.246718], [0.471062, 1.514179, -0.881563], [0.251969, 1.514179, 0.0], [0.471062, 1.514179, 0.881563], [1.0, 1.514179, 1.246718], [1.528938, 1.514179, 0.881563], [1.748031, 1.514179, 0.0]]}]},
			"L_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.945411, 15.297884, -0.510851], [8.946276, 15.3087, -0.5], [8.945411, 15.297884, -0.489149], [8.944546, 15.287067, -0.5], [8.945411, 15.297884, -0.510851], [8.956227, 15.297019, -0.5], [8.945411, 15.297884, -0.489149], [8.934595, 15.298749, -0.5], [8.946276, 15.3087, -0.5], [8.956227, 15.297019, -0.5], [8.944546, 15.287067, -0.5], [8.934595, 15.298749, -0.5], [8.945411, 15.297884, -0.510851], [8.956227, 15.297019, -0.5], [7.925, 15.379517, -0.5]]}, {"shapeName": "L_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[8.006633, 16.399928, -0.510851], [7.995817, 16.400793, -0.5], [8.006633, 16.399928, -0.489149], [8.01745, 16.399062, -0.5], [8.006633, 16.399928, -0.510851], [8.007498, 16.410743, -0.5], [8.006633, 16.399928, -0.489149], [8.005768, 16.389111, -0.5], [7.995817, 16.400793, -0.5], [8.007498, 16.410743, -0.5], [8.01745, 16.399062, -0.5], [8.005768, 16.389111, -0.5], [8.006633, 16.399928, -0.510851], [8.007498, 16.410743, -0.5], [7.925, 15.379517, -0.5]]}, {"shapeName": "L_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.925866, 15.390333, 0.523671], [7.914184, 15.380382, 0.523671], [7.924135, 15.3687, 0.523671], [7.935817, 15.378651, 0.523671], [7.925866, 15.390333, 0.523671], [7.925, 15.379517, 0.534521], [7.924135, 15.3687, 0.523671], [7.925, 15.379517, 0.51282], [7.914184, 15.380382, 0.523671], [7.925, 15.379517, 0.534521], [7.935817, 15.378651, 0.523671], [7.925, 15.379517, 0.51282], [7.925866, 15.390333, 0.523671], [7.925, 15.379517, 0.534521], [7.925, 15.379517, -0.5]]}]},
			"C_head_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_CTLShape", "degree": 3, "form": 2, "points": [[1.175418, 21.731703, 0.0], [0.0, 22.218576, 0.0], [-1.175418, 21.731703, 0.0], [-1.662291, 20.556285, 0.0], [-1.175418, 19.380867, 0.0], [0.0, 18.893994, 0.0], [1.175418, 19.380867, 0.0], [1.662291, 20.556285, 0.0]]}]},
			"world_A_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -110.587058], [49.129597, 0.0, -61.409604], [36.830448, 0.0, -61.409604], [36.830448, 0.0, -36.820877], [61.419175, 0.0, -36.820877], [61.419175, 0.0, -49.120026], [110.587058, 0.0, 0.0], [61.409604, 0.0, 49.129597], [61.409604, 0.0, 36.830448], [36.820877, 0.0, 36.830448], [36.820877, 0.0, 61.419175], [49.120026, 0.0, 61.419175], [0.0, 0.0, 110.587058], [-49.129597, 0.0, 61.409604], [-36.830448, 0.0, 61.409604], [-36.830448, 0.0, 36.820877], [-61.419175, 0.0, 36.820877], [-61.419175, 0.0, 49.120026], [-110.587058, 0.0, 0.0], [-61.409604, 0.0, -49.129597], [-61.409604, 0.0, -36.830448], [-36.820877, 0.0, -36.830448], [-36.820877, 0.0, -61.419175], [-49.120026, 0.0, -61.419175], [0.0, 0.0, -110.587058], [9.62875, 0.133999, -101.130592], [8.786474, 0.0, -100.230887], [8.786474, 0.0, -96.555499], [8.020768, 0.0, -96.555499], [8.068625, 0.0, -100.259601], [7.523059, 0.0, -99.982033], [7.542202, 0.0, -98.374051], [6.766925, 0.0, -98.374051], [6.766925, 0.0, -99.982033], [6.288359, 0.0, -100.259601], [6.288359, 0.0, -96.498072], [5.513082, 0.0, -96.498072], [5.513082, 0.0, -100.355314], [6.135218, 0.0, -100.97745], [7.09235, 0.0, -100.498884], [8.145195, 0.0, -100.97745], [8.786474, 0.0, -100.25003], [8.145195, 0.0, -100.97745], [7.101921, 0.0, -100.508456], [6.135218, 0.0, -100.967879], [4.26881, 0.0, -100.97745], [4.900517, 0.0, -100.355314], [4.900517, 0.0, -97.129779], [4.26881, 0.0, -96.498072], [2.249261, 0.0, -96.498072], [1.627125, 0.0, -97.129779], [1.627125, 0.0, -100.355314], [2.249261, 0.0, -100.97745], [4.26881, 0.0, -100.97745], [4.029527, 0.0, -100.259601], [4.12524, 0.0, -97.292491], [2.392831, 0.0, -97.311634], [2.402402, 0.0, -100.259601], [4.039098, 0.0, -100.278744], [4.26881, 0.0, -100.97745], [2.249261, 0.0, -100.97745], [0.957132, 0.0, -100.97745], [1.004989, 0.0, -96.498072], [-1.177273, 0.0, -96.498072], [-1.80898, 0.0, -97.129779], [-1.80898, 0.0, -98.479335], [-1.167701, 0.0, -99.101471], [-1.129416, 0.0, -99.149328], [-2.383259, 0.0, -100.958308], [-2.383259, 0.0, -100.97745], [-1.483555, 0.0, -100.97745], [-0.229712, 0.0, -99.158899], [0.239283, 0.0, -99.158899], [0.239283, 0.0, -97.244635], [-0.966704, 0.0, -97.244635], [-0.976275, 0.0, -98.383622], [0.239283, 0.0, -98.383622], [0.239283, 0.0, -100.97745], [0.957132, 0.0, -100.97745], [-6.15436, 0.0, -100.97745], [-6.15436, 0.0, -100.259601], [-3.646674, 0.0, -100.25003], [-3.646674, 0.0, -96.498072], [-2.871397, 0.0, -96.498072], [-2.871397, 0.0, -100.97745], [-9.418181, 0.0, -100.97745], [-9.99246, 0.0, -100.355314], [-10.040317, 0.0, -97.129779], [-9.418181, 0.0, -96.498072], [-6.766925, 0.0, -96.498072], [-6.766925, 0.0, -100.97745], [-7.551773, 0.0, -100.259601], [-7.532631, 0.0, -97.225492], [-9.169327, 0.0, -97.225492], [-9.150184, 0.0, -100.240459], [-7.523059, 0.0, -100.278744], [-6.747782, 0.0, -100.97745]]}]},
			"C_cog_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_cog_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 9.773434, -0.010851], [1.023671, 9.784285, 0.0], [1.023671, 9.773434, 0.010851], [1.023671, 9.762583, 0.0], [1.023671, 9.773434, -0.010851], [1.034521, 9.773434, 0.0], [1.023671, 9.773434, 0.010851], [1.01282, 9.773434, 0.0], [1.023671, 9.784285, 0.0], [1.034521, 9.773434, 0.0], [1.023671, 9.762583, 0.0], [1.01282, 9.773434, 0.0], [1.023671, 9.773434, -0.010851], [1.034521, 9.773434, 0.0], [0.0, 9.773434, 0.0]]}, {"shapeName": "C_cog_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 10.797105, -0.010851], [-0.010851, 10.797105, 0.0], [0.0, 10.797105, 0.010851], [0.010851, 10.797105, 0.0], [0.0, 10.797105, -0.010851], [0.0, 10.807955, 0.0], [0.0, 10.797105, 0.010851], [0.0, 10.786254, 0.0], [-0.010851, 10.797105, 0.0], [0.0, 10.807955, 0.0], [0.010851, 10.797105, 0.0], [0.0, 10.786254, 0.0], [0.0, 10.797105, -0.010851], [0.0, 10.807955, 0.0], [0.0, 9.773434, 0.0]]}, {"shapeName": "C_cog_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 9.784285, 1.023671], [-0.010851, 9.773434, 1.023671], [0.0, 9.762583, 1.023671], [0.010851, 9.773434, 1.023671], [0.0, 9.784285, 1.023671], [0.0, 9.773434, 1.034521], [0.0, 9.762583, 1.023671], [0.0, 9.773434, 1.01282], [-0.010851, 9.773434, 1.023671], [0.0, 9.773434, 1.034521], [0.010851, 9.773434, 1.023671], [0.0, 9.773434, 1.01282], [0.0, 9.784285, 1.023671], [0.0, 9.773434, 1.034521], [0.0, 9.773434, 0.0]]}]},
			"L_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_C_CTLShape", "degree": 3, "form": 2, "points": [[7.915627, 15.262349, -0.367542], [7.925, 15.379517, -0.416229], [7.934374, 15.496684, -0.367542], [7.938256, 15.545216, -0.25], [7.934374, 15.496684, -0.132458], [7.925, 15.379517, -0.083771], [7.915627, 15.262349, -0.132458], [7.911744, 15.213817, -0.25]]}]},
			"L_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.314691, 15.214225, 0.239149], [9.316126, 15.22498, 0.25], [9.314691, 15.214225, 0.260851], [9.313257, 15.203469, 0.25], [9.314691, 15.214225, 0.239149], [9.325446, 15.212791, 0.25], [9.314691, 15.214225, 0.260851], [9.303936, 15.215659, 0.25], [9.316126, 15.22498, 0.25], [9.325446, 15.212791, 0.25], [9.313257, 15.203469, 0.25], [9.303936, 15.215659, 0.25], [9.314691, 15.214225, 0.239149], [9.325446, 15.212791, 0.25], [8.3, 15.349517, 0.25]]}, {"shapeName": "L_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[8.435292, 16.364208, 0.239149], [8.424537, 16.365642, 0.25], [8.435292, 16.364208, 0.260851], [8.446048, 16.362774, 0.25], [8.435292, 16.364208, 0.239149], [8.436726, 16.374963, 0.25], [8.435292, 16.364208, 0.260851], [8.433858, 16.353452, 0.25], [8.424537, 16.365642, 0.25], [8.436726, 16.374963, 0.25], [8.446048, 16.362774, 0.25], [8.433858, 16.353452, 0.25], [8.435292, 16.364208, 0.239149], [8.436726, 16.374963, 0.25], [8.3, 15.349517, 0.25]]}, {"shapeName": "L_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[8.301434, 15.360272, 1.273671], [8.289244, 15.350951, 1.273671], [8.298566, 15.338761, 1.273671], [8.310756, 15.348083, 1.273671], [8.301434, 15.360272, 1.273671], [8.3, 15.349517, 1.284521], [8.298566, 15.338761, 1.273671], [8.3, 15.349517, 1.26282], [8.289244, 15.350951, 1.273671], [8.3, 15.349517, 1.284521], [8.310756, 15.348083, 1.273671], [8.3, 15.349517, 1.26282], [8.301434, 15.360272, 1.273671], [8.3, 15.349517, 1.284521], [8.3, 15.349517, 0.25]]}]},
			"L_upLeg_shaper_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_shaper_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 5.297067, 0.516204], [1.010851, 5.298413, 0.526971], [1.0, 5.299759, 0.537738], [0.989149, 5.298413, 0.526971], [1.0, 5.297067, 0.516204], [1.0, 5.287647, 0.528317], [1.0, 5.299759, 0.537738], [1.0, 5.30918, 0.525625], [1.010851, 5.298413, 0.526971], [1.0, 5.287647, 0.528317], [0.989149, 5.298413, 0.526971], [1.0, 5.30918, 0.525625], [1.0, 5.297067, 0.516204], [1.0, 5.287647, 0.528317], [1.0, 6.314179, 0.4]]}, {"shapeName": "L_upLeg_shaper_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.023671, 6.312833, 0.389233], [2.023671, 6.324946, 0.398654], [2.023671, 6.315525, 0.410767], [2.023671, 6.303412, 0.401346], [2.023671, 6.312833, 0.389233], [2.034521, 6.314179, 0.4], [2.023671, 6.315525, 0.410767], [2.01282, 6.314179, 0.4], [2.023671, 6.324946, 0.398654], [2.034521, 6.314179, 0.4], [2.023671, 6.303412, 0.401346], [2.01282, 6.314179, 0.4], [2.023671, 6.312833, 0.389233], [2.034521, 6.314179, 0.4], [1.0, 6.314179, 0.4]]}, {"shapeName": "L_upLeg_shaper_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.010851, 6.44115, 1.415766], [1.0, 6.451917, 1.41442], [0.989149, 6.44115, 1.415766], [1.0, 6.430383, 1.417112], [1.010851, 6.44115, 1.415766], [1.0, 6.442496, 1.426532], [0.989149, 6.44115, 1.415766], [1.0, 6.439804, 1.404999], [1.0, 6.451917, 1.41442], [1.0, 6.442496, 1.426532], [1.0, 6.430383, 1.417112], [1.0, 6.439804, 1.404999], [1.010851, 6.44115, 1.415766], [1.0, 6.442496, 1.426532], [1.0, 6.314179, 0.4]]}]},
			"L_clavicle_CTL": {"color": 6, "shapes": [{"shapeName": "L_clavicle_CTLShape", "degree": 3, "form": 0, "points": [[2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.253273, 15.299517, -0.015181], [2.379921, 15.299517, 0.364762], [2.428296, 15.299517, 0.509888], [2.379921, 16.241139, 0.364762], [2.253273, 16.823094, -0.015181], [2.096727, 16.823094, -0.484819], [1.970079, 16.241139, -0.864762], [1.921704, 15.299517, -1.009888], [1.970079, 15.299517, -0.864762], [2.096727, 15.299517, -0.484819], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25]]}]},
			"L_loLeg_shaper_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_shaper_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 2.099759, 0.062262], [1.010851, 2.098413, 0.073029], [1.0, 2.097067, 0.083796], [0.989149, 2.098413, 0.073029], [1.0, 2.099759, 0.062262], [1.0, 2.087647, 0.071683], [1.0, 2.097067, 0.083796], [1.0, 2.10918, 0.074375], [1.010851, 2.098413, 0.073029], [1.0, 2.087647, 0.071683], [0.989149, 2.098413, 0.073029], [1.0, 2.10918, 0.074375], [1.0, 2.099759, 0.062262], [1.0, 2.087647, 0.071683], [1.0, 3.114179, 0.2]]}, {"shapeName": "L_loLeg_shaper_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.023671, 3.115525, 0.189233], [2.023671, 3.124946, 0.201346], [2.023671, 3.112833, 0.210767], [2.023671, 3.103412, 0.198654], [2.023671, 3.115525, 0.189233], [2.034521, 3.114179, 0.2], [2.023671, 3.112833, 0.210767], [2.01282, 3.114179, 0.2], [2.023671, 3.124946, 0.201346], [2.034521, 3.114179, 0.2], [2.023671, 3.103412, 0.198654], [2.01282, 3.114179, 0.2], [2.023671, 3.115525, 0.189233], [2.034521, 3.114179, 0.2], [1.0, 3.114179, 0.2]]}, {"shapeName": "L_loLeg_shaper_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.010851, 2.987208, 1.215766], [1.0, 2.997976, 1.217112], [0.989149, 2.987208, 1.215766], [1.0, 2.976441, 1.21442], [1.010851, 2.987208, 1.215766], [1.0, 2.985863, 1.226532], [0.989149, 2.987208, 1.215766], [1.0, 2.988554, 1.204999], [1.0, 2.997976, 1.217112], [1.0, 2.985863, 1.226532], [1.0, 2.976441, 1.21442], [1.0, 2.988554, 1.204999], [1.010851, 2.987208, 1.215766], [1.0, 2.985863, 1.226532], [1.0, 3.114179, 0.2]]}]},
			"L_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.314691, 15.214225, -0.010851], [9.316126, 15.22498, -0.0], [9.314691, 15.214225, 0.010851], [9.313257, 15.203469, -0.0], [9.314691, 15.214225, -0.010851], [9.325446, 15.212791, -0.0], [9.314691, 15.214225, 0.010851], [9.303936, 15.215659, -0.0], [9.316126, 15.22498, -0.0], [9.325446, 15.212791, -0.0], [9.313257, 15.203469, -0.0], [9.303936, 15.215659, -0.0], [9.314691, 15.214225, -0.010851], [9.325446, 15.212791, -0.0], [8.3, 15.349517, -0.0]]}, {"shapeName": "L_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[8.435292, 16.364208, -0.010851], [8.424537, 16.365642, -0.0], [8.435292, 16.364208, 0.010851], [8.446048, 16.362774, -0.0], [8.435292, 16.364208, -0.010851], [8.436726, 16.374963, -0.0], [8.435292, 16.364208, 0.010851], [8.433858, 16.353452, -0.0], [8.424537, 16.365642, -0.0], [8.436726, 16.374963, -0.0], [8.446048, 16.362774, -0.0], [8.433858, 16.353452, -0.0], [8.435292, 16.364208, -0.010851], [8.436726, 16.374963, -0.0], [8.3, 15.349517, -0.0]]}, {"shapeName": "L_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[8.301434, 15.360272, 1.023671], [8.289244, 15.350951, 1.023671], [8.298566, 15.338761, 1.023671], [8.310756, 15.348083, 1.023671], [8.301434, 15.360272, 1.023671], [8.3, 15.349517, 1.034521], [8.298566, 15.338761, 1.023671], [8.3, 15.349517, 1.01282], [8.289244, 15.350951, 1.023671], [8.3, 15.349517, 1.034521], [8.310756, 15.348083, 1.023671], [8.3, 15.349517, 1.01282], [8.301434, 15.360272, 1.023671], [8.3, 15.349517, 1.034521], [8.3, 15.349517, -0.0]]}]},
			"L_upArm_shaper_B_CTL": {"color": 4, "shapes": [{"shapeName": "L_upArm_shaper_B_CTLShape", "degree": 1, "form": 0, "points": [[3.725, 16.799517, -0.2], [3.799251, 16.810935, -0.218563], [3.862198, 16.843452, -0.234299], [3.904259, 16.892115, -0.244815], [3.919029, 16.949517, -0.248507], [3.904259, 17.006919, -0.244815], [3.862198, 17.055582, -0.234299], [3.799251, 17.088099, -0.218563], [3.725, 17.099517, -0.2], [3.650749, 17.088099, -0.181437], [3.587802, 17.055582, -0.165701], [3.545741, 17.006919, -0.155185], [3.530972, 16.949517, -0.151493], [3.545741, 16.892115, -0.155185], [3.587802, 16.843452, -0.165701], [3.650749, 16.810935, -0.181437], [3.725, 16.799517, -0.2], [3.725, 15.299517, -0.2]]}]},
			"C_midNeck_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.987351, 19.556285, -0.822793], [0.0, 19.556285, -1.163604], [-0.987351, 19.556285, -0.822793], [-1.396324, 19.556285, 0.0], [-0.987351, 19.556285, 0.822793], [0.0, 19.556285, 1.163604], [0.987351, 19.556285, 0.822793], [1.396324, 19.556285, 0.0]]}]},
			"L_clavicle_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_clavicle_PIV_CTLShape", "degree": 1, "form": 0, "points": [[3.142708, 15.299517, -0.584007], [3.14614, 15.310368, -0.573713], [3.149571, 15.299517, -0.563419], [3.14614, 15.288666, -0.573713], [3.142708, 15.299517, -0.584007], [3.156433, 15.299517, -0.577144], [3.149571, 15.299517, -0.563419], [3.135845, 15.299517, -0.570282], [3.14614, 15.310368, -0.573713], [3.156433, 15.299517, -0.577144], [3.14614, 15.288666, -0.573713], [3.135845, 15.299517, -0.570282], [3.142708, 15.299517, -0.584007], [3.156433, 15.299517, -0.577144], [2.175, 15.299517, -0.25]]}, {"shapeName": "L_clavicle_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.171569, 16.323188, -0.260294], [2.164706, 16.323188, -0.246569], [2.178431, 16.323188, -0.239706], [2.185294, 16.323188, -0.253431], [2.171569, 16.323188, -0.260294], [2.175, 16.334038, -0.25], [2.178431, 16.323188, -0.239706], [2.175, 16.312337, -0.25], [2.164706, 16.323188, -0.246569], [2.175, 16.334038, -0.25], [2.185294, 16.323188, -0.253431], [2.175, 16.312337, -0.25], [2.171569, 16.323188, -0.260294], [2.175, 16.334038, -0.25], [2.175, 15.299517, -0.25]]}, {"shapeName": "L_clavicle_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.498713, 15.310368, 0.72114], [2.488419, 15.299517, 0.724571], [2.498713, 15.288666, 0.72114], [2.509007, 15.299517, 0.717708], [2.498713, 15.310368, 0.72114], [2.502144, 15.299517, 0.731433], [2.498713, 15.288666, 0.72114], [2.495282, 15.299517, 0.710845], [2.488419, 15.299517, 0.724571], [2.502144, 15.299517, 0.731433], [2.509007, 15.299517, 0.717708], [2.495282, 15.299517, 0.710845], [2.498713, 15.310368, 0.72114], [2.502144, 15.299517, 0.731433], [2.175, 15.299517, -0.25]]}]},
			"L_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.945411, 15.297884, 0.239149], [8.946276, 15.3087, 0.25], [8.945411, 15.297884, 0.260851], [8.944546, 15.287067, 0.25], [8.945411, 15.297884, 0.239149], [8.956227, 15.297019, 0.25], [8.945411, 15.297884, 0.260851], [8.934595, 15.298749, 0.25], [8.946276, 15.3087, 0.25], [8.956227, 15.297019, 0.25], [8.944546, 15.287067, 0.25], [8.934595, 15.298749, 0.25], [8.945411, 15.297884, 0.239149], [8.956227, 15.297019, 0.25], [7.925, 15.379517, 0.25]]}, {"shapeName": "L_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[8.006633, 16.399928, 0.239149], [7.995817, 16.400793, 0.25], [8.006633, 16.399928, 0.260851], [8.01745, 16.399062, 0.25], [8.006633, 16.399928, 0.239149], [8.007498, 16.410743, 0.25], [8.006633, 16.399928, 0.260851], [8.005768, 16.389111, 0.25], [7.995817, 16.400793, 0.25], [8.007498, 16.410743, 0.25], [8.01745, 16.399062, 0.25], [8.005768, 16.389111, 0.25], [8.006633, 16.399928, 0.239149], [8.007498, 16.410743, 0.25], [7.925, 15.379517, 0.25]]}, {"shapeName": "L_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.925866, 15.390333, 1.273671], [7.914184, 15.380382, 1.273671], [7.924135, 15.3687, 1.273671], [7.935817, 15.378651, 1.273671], [7.925866, 15.390333, 1.273671], [7.925, 15.379517, 1.284521], [7.924135, 15.3687, 1.273671], [7.925, 15.379517, 1.26282], [7.914184, 15.380382, 1.273671], [7.925, 15.379517, 1.284521], [7.935817, 15.378651, 1.273671], [7.925, 15.379517, 1.26282], [7.925866, 15.390333, 1.273671], [7.925, 15.379517, 1.284521], [7.925, 15.379517, 0.25]]}]},
			"L_upArm_shaper_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upArm_shaper_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[4.315475, 15.299517, -0.358804], [4.318107, 15.310368, -0.348277], [4.320739, 15.299517, -0.33775], [4.318107, 15.288666, -0.348277], [4.315475, 15.299517, -0.358804], [4.328633, 15.299517, -0.350908], [4.320739, 15.299517, -0.33775], [4.30758, 15.299517, -0.345645], [4.318107, 15.310368, -0.348277], [4.328633, 15.299517, -0.350908], [4.318107, 15.288666, -0.348277], [4.30758, 15.299517, -0.345645], [4.315475, 15.299517, -0.358804], [4.328633, 15.299517, -0.350908], [3.325, 15.299517, -0.1]]}, {"shapeName": "L_upArm_shaper_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[3.322368, 16.323188, -0.110527], [3.314473, 16.323188, -0.097368], [3.327632, 16.323188, -0.089473], [3.335527, 16.323188, -0.102632], [3.322368, 16.323188, -0.110527], [3.325, 16.334038, -0.1], [3.327632, 16.323188, -0.089473], [3.325, 16.312337, -0.1], [3.314473, 16.323188, -0.097368], [3.325, 16.334038, -0.1], [3.335527, 16.323188, -0.102632], [3.325, 16.312337, -0.1], [3.322368, 16.323188, -0.110527], [3.325, 16.334038, -0.1], [3.325, 15.299517, -0.1]]}, {"shapeName": "L_upArm_shaper_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[3.573277, 15.310368, 0.893107], [3.56275, 15.299517, 0.895738], [3.573277, 15.288666, 0.893107], [3.583804, 15.299517, 0.890475], [3.573277, 15.310368, 0.893107], [3.575908, 15.299517, 0.903633], [3.573277, 15.288666, 0.893107], [3.570645, 15.299517, 0.88258], [3.56275, 15.299517, 0.895738], [3.575908, 15.299517, 0.903633], [3.583804, 15.299517, 0.890475], [3.570645, 15.299517, 0.88258], [3.573277, 15.310368, 0.893107], [3.575908, 15.299517, 0.903633], [3.325, 15.299517, -0.1]]}]},
			"C_neckBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neckBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 18.556285, -0.010851], [1.023671, 18.567136, 0.0], [1.023671, 18.556285, 0.010851], [1.023671, 18.545434, 0.0], [1.023671, 18.556285, -0.010851], [1.034521, 18.556285, 0.0], [1.023671, 18.556285, 0.010851], [1.01282, 18.556285, 0.0], [1.023671, 18.567136, 0.0], [1.034521, 18.556285, 0.0], [1.023671, 18.545434, 0.0], [1.01282, 18.556285, 0.0], [1.023671, 18.556285, -0.010851], [1.034521, 18.556285, 0.0], [0.0, 18.556285, 0.0]]}, {"shapeName": "C_neckBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 19.579956, -0.010851], [-0.010851, 19.579956, 0.0], [0.0, 19.579956, 0.010851], [0.010851, 19.579956, 0.0], [0.0, 19.579956, -0.010851], [0.0, 19.590806, 0.0], [0.0, 19.579956, 0.010851], [0.0, 19.569105, 0.0], [-0.010851, 19.579956, 0.0], [0.0, 19.590806, 0.0], [0.010851, 19.579956, 0.0], [0.0, 19.569105, 0.0], [0.0, 19.579956, -0.010851], [0.0, 19.590806, 0.0], [0.0, 18.556285, 0.0]]}, {"shapeName": "C_neckBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 18.567136, 1.023671], [-0.010851, 18.556285, 1.023671], [0.0, 18.545434, 1.023671], [0.010851, 18.556285, 1.023671], [0.0, 18.567136, 1.023671], [0.0, 18.556285, 1.034521], [0.0, 18.545434, 1.023671], [0.0, 18.556285, 1.01282], [-0.010851, 18.556285, 1.023671], [0.0, 18.556285, 1.034521], [0.010851, 18.556285, 1.023671], [0.0, 18.556285, 1.01282], [0.0, 18.567136, 1.023671], [0.0, 18.556285, 1.034521], [0.0, 18.556285, 0.0]]}]},
			"C_chest_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_chest_FK_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 15.273434, -1.0], [0.0, 15.311702, -1.007612], [0.0, 15.344144, -1.02929], [0.0, 15.365822, -1.061732], [0.0, 15.373434, -1.1], [0.0, 15.365822, -1.138268], [0.0, 15.344144, -1.17071], [0.0, 15.311702, -1.192388], [0.0, 15.273434, -1.2], [0.0, 15.235166, -1.192388], [0.0, 15.202724, -1.17071], [0.0, 15.181046, -1.138268], [0.0, 15.173434, -1.1], [0.0, 15.181046, -1.061732], [0.0, 15.202724, -1.02929], [0.0, 15.235166, -1.007612], [0.0, 15.273434, -1.0], [0.0, 15.273434, 0.0]]}]},
			"L_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.945411, 15.297884, -0.260851], [8.946276, 15.3087, -0.25], [8.945411, 15.297884, -0.239149], [8.944546, 15.287067, -0.25], [8.945411, 15.297884, -0.260851], [8.956227, 15.297019, -0.25], [8.945411, 15.297884, -0.239149], [8.934595, 15.298749, -0.25], [8.946276, 15.3087, -0.25], [8.956227, 15.297019, -0.25], [8.944546, 15.287067, -0.25], [8.934595, 15.298749, -0.25], [8.945411, 15.297884, -0.260851], [8.956227, 15.297019, -0.25], [7.925, 15.379517, -0.25]]}, {"shapeName": "L_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[8.006633, 16.399928, -0.260851], [7.995817, 16.400793, -0.25], [8.006633, 16.399928, -0.239149], [8.01745, 16.399062, -0.25], [8.006633, 16.399928, -0.260851], [8.007498, 16.410743, -0.25], [8.006633, 16.399928, -0.239149], [8.005768, 16.389111, -0.25], [7.995817, 16.400793, -0.25], [8.007498, 16.410743, -0.25], [8.01745, 16.399062, -0.25], [8.005768, 16.389111, -0.25], [8.006633, 16.399928, -0.260851], [8.007498, 16.410743, -0.25], [7.925, 15.379517, -0.25]]}, {"shapeName": "L_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.925866, 15.390333, 0.773671], [7.914184, 15.380382, 0.773671], [7.924135, 15.3687, 0.773671], [7.935817, 15.378651, 0.773671], [7.925866, 15.390333, 0.773671], [7.925, 15.379517, 0.784521], [7.924135, 15.3687, 0.773671], [7.925, 15.379517, 0.76282], [7.914184, 15.380382, 0.773671], [7.925, 15.379517, 0.784521], [7.935817, 15.378651, 0.773671], [7.925, 15.379517, 0.76282], [7.925866, 15.390333, 0.773671], [7.925, 15.379517, 0.784521], [7.925, 15.379517, -0.25]]}]},
			"L_loArm_shaper_A_CTL": {"color": 4, "shapes": [{"shapeName": "L_loArm_shaper_A_CTLShape", "degree": 1, "form": 0, "points": [[5.325, 16.799517, -0.4], [5.399251, 16.810935, -0.381437], [5.462198, 16.843452, -0.365701], [5.504259, 16.892115, -0.355185], [5.519029, 16.949517, -0.351493], [5.504259, 17.006919, -0.355185], [5.462198, 17.055582, -0.365701], [5.399251, 17.088099, -0.381437], [5.325, 17.099517, -0.4], [5.250749, 17.088099, -0.418563], [5.187802, 17.055582, -0.434299], [5.145741, 17.006919, -0.444815], [5.130972, 16.949517, -0.448507], [5.145741, 16.892115, -0.444815], [5.187802, 16.843452, -0.434299], [5.250749, 16.810935, -0.418563], [5.325, 16.799517, -0.4], [5.325, 15.299517, -0.4]]}]},
			"L_ankleOffset_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ankleOffset_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.025451, 0.686549, -0.010851], [2.025451, 0.6974, -0.0], [2.025451, 0.686549, 0.010851], [2.025451, 0.675698, -0.0], [2.025451, 0.686549, -0.010851], [2.036301, 0.686549, -0.0], [2.025451, 0.686549, 0.010851], [2.0146, 0.686549, -0.0], [2.025451, 0.6974, -0.0], [2.036301, 0.686549, -0.0], [2.025451, 0.675698, -0.0], [2.0146, 0.686549, -0.0], [2.025451, 0.686549, -0.010851], [2.036301, 0.686549, -0.0], [1.00178, 0.686549, -0.0]]}, {"shapeName": "L_ankleOffset_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.00178, 1.71022, -0.010851], [0.990929, 1.71022, -0.0], [1.00178, 1.71022, 0.010851], [1.012631, 1.71022, -0.0], [1.00178, 1.71022, -0.010851], [1.00178, 1.72107, -0.0], [1.00178, 1.71022, 0.010851], [1.00178, 1.699369, -0.0], [0.990929, 1.71022, -0.0], [1.00178, 1.72107, -0.0], [1.012631, 1.71022, -0.0], [1.00178, 1.699369, -0.0], [1.00178, 1.71022, -0.010851], [1.00178, 1.72107, -0.0], [1.00178, 0.686549, -0.0]]}, {"shapeName": "L_ankleOffset_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.00178, 0.6974, 1.023671], [0.990929, 0.686549, 1.023671], [1.00178, 0.675698, 1.023671], [1.012631, 0.686549, 1.023671], [1.00178, 0.6974, 1.023671], [1.00178, 0.686549, 1.034521], [1.00178, 0.675698, 1.023671], [1.00178, 0.686549, 1.01282], [0.990929, 0.686549, 1.023671], [1.00178, 0.686549, 1.034521], [1.012631, 0.686549, 1.023671], [1.00178, 0.686549, 1.01282], [1.00178, 0.6974, 1.023671], [1.00178, 0.686549, 1.034521], [1.00178, 0.686549, -0.0]]}]},
			"L_upArm_shaper_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upArm_shaper_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.515475, 15.299517, -0.658804], [5.518107, 15.310368, -0.648277], [5.520739, 15.299517, -0.63775], [5.518107, 15.288666, -0.648277], [5.515475, 15.299517, -0.658804], [5.528633, 15.299517, -0.650908], [5.520739, 15.299517, -0.63775], [5.50758, 15.299517, -0.645645], [5.518107, 15.310368, -0.648277], [5.528633, 15.299517, -0.650908], [5.518107, 15.288666, -0.648277], [5.50758, 15.299517, -0.645645], [5.515475, 15.299517, -0.658804], [5.528633, 15.299517, -0.650908], [4.525, 15.299517, -0.4]]}, {"shapeName": "L_upArm_shaper_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[4.522368, 16.323188, -0.410527], [4.514473, 16.323188, -0.397368], [4.527632, 16.323188, -0.389473], [4.535527, 16.323188, -0.402632], [4.522368, 16.323188, -0.410527], [4.525, 16.334038, -0.4], [4.527632, 16.323188, -0.389473], [4.525, 16.312337, -0.4], [4.514473, 16.323188, -0.397368], [4.525, 16.334038, -0.4], [4.535527, 16.323188, -0.402632], [4.525, 16.312337, -0.4], [4.522368, 16.323188, -0.410527], [4.525, 16.334038, -0.4], [4.525, 15.299517, -0.4]]}, {"shapeName": "L_upArm_shaper_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.773277, 15.310368, 0.593107], [4.76275, 15.299517, 0.595738], [4.773277, 15.288666, 0.593107], [4.783804, 15.299517, 0.590475], [4.773277, 15.310368, 0.593107], [4.775908, 15.299517, 0.603633], [4.773277, 15.288666, 0.593107], [4.770645, 15.299517, 0.58258], [4.76275, 15.299517, 0.595738], [4.775908, 15.299517, 0.603633], [4.783804, 15.299517, 0.590475], [4.770645, 15.299517, 0.58258], [4.773277, 15.310368, 0.593107], [4.775908, 15.299517, 0.603633], [4.525, 15.299517, -0.4]]}]},
			"L_wrist_IK_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_wrist_IK_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[6.925, 15.749517, -0.45], [6.925, 15.749517, 0.45], [6.925, 14.849517, 0.45], [6.925, 14.849517, -0.45], [6.925, 15.749517, -0.45]]}]},
			"L_loArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.920739, 15.299517, -0.01225], [6.918107, 15.310368, -0.001723], [6.915475, 15.299517, 0.008804], [6.918107, 15.288666, -0.001723], [6.920739, 15.299517, -0.01225], [6.928633, 15.299517, 0.000908], [6.915475, 15.299517, 0.008804], [6.90758, 15.299517, -0.004355], [6.918107, 15.310368, -0.001723], [6.928633, 15.299517, 0.000908], [6.918107, 15.288666, -0.001723], [6.90758, 15.299517, -0.004355], [6.920739, 15.299517, -0.01225], [6.928633, 15.299517, 0.000908], [5.925, 15.299517, -0.25]]}, {"shapeName": "L_loArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[5.927632, 16.323188, -0.260527], [5.914473, 16.323188, -0.252632], [5.922368, 16.323188, -0.239473], [5.935527, 16.323188, -0.247368], [5.927632, 16.323188, -0.260527], [5.925, 16.334038, -0.25], [5.922368, 16.323188, -0.239473], [5.925, 16.312337, -0.25], [5.914473, 16.323188, -0.252632], [5.925, 16.334038, -0.25], [5.935527, 16.323188, -0.247368], [5.925, 16.312337, -0.25], [5.927632, 16.323188, -0.260527], [5.925, 16.334038, -0.25], [5.925, 15.299517, -0.25]]}, {"shapeName": "L_loArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[5.676723, 15.310368, 0.743107], [5.666196, 15.299517, 0.740475], [5.676723, 15.288666, 0.743107], [5.68725, 15.299517, 0.745738], [5.676723, 15.310368, 0.743107], [5.674092, 15.299517, 0.753633], [5.676723, 15.288666, 0.743107], [5.679355, 15.299517, 0.73258], [5.666196, 15.299517, 0.740475], [5.674092, 15.299517, 0.753633], [5.68725, 15.299517, 0.745738], [5.679355, 15.299517, 0.73258], [5.676723, 15.310368, 0.743107], [5.674092, 15.299517, 0.753633], [5.925, 15.299517, -0.25]]}]},
			"L_bendyArm_A_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[3.815859, 15.449517, -0.686564], [3.815859, 15.539517, -0.686564], [3.761288, 15.299517, -0.904846], [3.815859, 15.059516, -0.686564], [3.815859, 15.149516, -0.686564], [3.88862, 15.149516, -0.395522], [3.88862, 14.849517, -0.395522], [3.866791, 14.849517, -0.482834], [3.925, 14.624517, -0.25], [3.983209, 14.849517, -0.017166], [3.96138, 14.849517, -0.104478], [3.96138, 15.149516, -0.104478], [4.034141, 15.149516, 0.186564], [4.034141, 15.059516, 0.186564], [4.088712, 15.299517, 0.404846], [4.034141, 15.539517, 0.186564], [4.034141, 15.449517, 0.186564], [3.96138, 15.449517, -0.104478], [3.96138, 15.749517, -0.104478], [3.983209, 15.749517, -0.017166], [3.925, 15.974517, -0.25], [3.866791, 15.749517, -0.482834], [3.88862, 15.749517, -0.395522], [3.88862, 15.449517, -0.395522], [3.815859, 15.449517, -0.686564]]}]},
			"L_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_A_CTLShape", "degree": 3, "form": 2, "points": [[7.190535, 15.183006, -0.367542], [7.175, 15.299517, -0.416229], [7.159465, 15.416027, -0.367542], [7.153031, 15.464288, -0.25], [7.159465, 15.416027, -0.132458], [7.175, 15.299517, -0.083771], [7.190535, 15.183006, -0.132458], [7.19697, 15.134746, -0.25]]}]},
			"L_legBase_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.342253, 0.021491], [1.0, 9.064071, 0.056264], [1.0, 8.957814, 0.069546], [1.0, 9.145826, 0.710309], [1.0, 9.474536, 1.079759], [1.0, 9.818389, 1.036777], [1.0, 10.046044, 0.597782], [1.0, 10.070544, -0.069546], [1.0, 9.964288, -0.056264], [1.0, 9.686106, -0.021491], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0]]}]},
			"C_head_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_head_FK_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 20.556285, -1.0], [0.0, 20.594553, -1.007612], [0.0, 20.626995, -1.02929], [0.0, 20.648673, -1.061732], [0.0, 20.656285, -1.1], [0.0, 20.648673, -1.138268], [0.0, 20.626995, -1.17071], [0.0, 20.594553, -1.192388], [0.0, 20.556285, -1.2], [0.0, 20.518017, -1.192388], [0.0, 20.485575, -1.17071], [0.0, 20.463897, -1.138268], [0.0, 20.456285, -1.1], [0.0, 20.463897, -1.061732], [0.0, 20.485575, -1.02929], [0.0, 20.518017, -1.007612], [0.0, 20.556285, -1.0], [0.0, 20.556285, 0.0]]}]},
			"L_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.570411, 15.43115, -0.010851], [8.569546, 15.441966, -0.0], [8.570411, 15.43115, 0.010851], [8.571276, 15.420333, -0.0], [8.570411, 15.43115, -0.010851], [8.581227, 15.432015, -0.0], [8.570411, 15.43115, 0.010851], [8.559595, 15.430284, -0.0], [8.569546, 15.441966, -0.0], [8.581227, 15.432015, -0.0], [8.571276, 15.420333, -0.0], [8.559595, 15.430284, -0.0], [8.570411, 15.43115, -0.010851], [8.581227, 15.432015, -0.0], [7.55, 15.349517, -0.0]]}, {"shapeName": "L_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.468367, 16.369928, -0.010851], [7.457551, 16.369062, -0.0], [7.468367, 16.369928, 0.010851], [7.479184, 16.370793, -0.0], [7.468367, 16.369928, -0.010851], [7.467502, 16.380743, -0.0], [7.468367, 16.369928, 0.010851], [7.469233, 16.359111, -0.0], [7.457551, 16.369062, -0.0], [7.467502, 16.380743, -0.0], [7.479184, 16.370793, -0.0], [7.469233, 16.359111, -0.0], [7.468367, 16.369928, -0.010851], [7.467502, 16.380743, -0.0], [7.55, 15.349517, -0.0]]}, {"shapeName": "L_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.549135, 15.360333, 1.023671], [7.539184, 15.348651, 1.023671], [7.550866, 15.3387, 1.023671], [7.560817, 15.350382, 1.023671], [7.549135, 15.360333, 1.023671], [7.55, 15.349517, 1.034521], [7.550866, 15.3387, 1.023671], [7.55, 15.349517, 1.01282], [7.539184, 15.348651, 1.023671], [7.55, 15.349517, 1.034521], [7.560817, 15.350382, 1.023671], [7.55, 15.349517, 1.01282], [7.549135, 15.360333, 1.023671], [7.55, 15.349517, 1.034521], [7.55, 15.349517, -0.0]]}]},
			"C_midNeck_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_midNeck_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 19.556285, -0.010851], [1.023671, 19.567136, 0.0], [1.023671, 19.556285, 0.010851], [1.023671, 19.545434, 0.0], [1.023671, 19.556285, -0.010851], [1.034521, 19.556285, 0.0], [1.023671, 19.556285, 0.010851], [1.01282, 19.556285, 0.0], [1.023671, 19.567136, 0.0], [1.034521, 19.556285, 0.0], [1.023671, 19.545434, 0.0], [1.01282, 19.556285, 0.0], [1.023671, 19.556285, -0.010851], [1.034521, 19.556285, 0.0], [0.0, 19.556285, 0.0]]}, {"shapeName": "C_midNeck_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 20.579956, -0.010851], [-0.010851, 20.579956, 0.0], [0.0, 20.579956, 0.010851], [0.010851, 20.579956, 0.0], [0.0, 20.579956, -0.010851], [0.0, 20.590806, 0.0], [0.0, 20.579956, 0.010851], [0.0, 20.569105, 0.0], [-0.010851, 20.579956, 0.0], [0.0, 20.590806, 0.0], [0.010851, 20.579956, 0.0], [0.0, 20.569105, 0.0], [0.0, 20.579956, -0.010851], [0.0, 20.590806, 0.0], [0.0, 19.556285, 0.0]]}, {"shapeName": "C_midNeck_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 19.567136, 1.023671], [-0.010851, 19.556285, 1.023671], [0.0, 19.545434, 1.023671], [0.010851, 19.556285, 1.023671], [0.0, 19.567136, 1.023671], [0.0, 19.556285, 1.034521], [0.0, 19.545434, 1.023671], [0.0, 19.556285, 1.01282], [-0.010851, 19.556285, 1.023671], [0.0, 19.556285, 1.034521], [0.010851, 19.556285, 1.023671], [0.0, 19.556285, 1.01282], [0.0, 19.567136, 1.023671], [0.0, 19.556285, 1.034521], [0.0, 19.556285, 0.0]]}]},
			"L_upArm_shaper_A_CTL": {"color": 4, "shapes": [{"shapeName": "L_upArm_shaper_A_CTLShape", "degree": 1, "form": 0, "points": [[3.325, 16.799517, -0.1], [3.399251, 16.810935, -0.118563], [3.462198, 16.843452, -0.134299], [3.504259, 16.892115, -0.144815], [3.519029, 16.949517, -0.148507], [3.504259, 17.006919, -0.144815], [3.462198, 17.055582, -0.134299], [3.399251, 17.088099, -0.118563], [3.325, 17.099517, -0.1], [3.250749, 17.088099, -0.081437], [3.187802, 17.055582, -0.065701], [3.145741, 17.006919, -0.055185], [3.130972, 16.949517, -0.051493], [3.145741, 16.892115, -0.055185], [3.187802, 16.843452, -0.065701], [3.250749, 16.810935, -0.081437], [3.325, 16.799517, -0.1], [3.325, 15.299517, -0.1]]}]},
			"L_toeTip_CTL": {"color": 20, "shapes": [{"shapeName": "L_toeTip_CTLShape", "degree": 1, "form": 0, "points": [[1.00178, 0.186549, 2.3], [1.00178, 0.086549, 2.2], [1.10178, 0.186549, 2.2], [1.00178, 0.186549, 2.3], [0.90178, 0.186549, 2.2], [1.00178, 0.086549, 2.2], [1.00178, 0.186549, 2.1], [0.90178, 0.186549, 2.2], [1.00178, 0.286549, 2.2], [1.00178, 0.186549, 2.3], [1.10178, 0.186549, 2.2], [1.00178, 0.186549, 2.1], [1.00178, 0.286549, 2.2], [1.10178, 0.186549, 2.2]]}]},
			"C_chest_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.128401, 15.273434, -0.940334], [0.0, 15.753434, -1.329833], [-1.128401, 15.273434, -0.940334], [-1.595799, 14.793434, 0.0], [-1.128401, 15.273434, 0.940334], [0.0, 15.753434, 1.329833], [1.128401, 15.273434, 0.940334], [1.595799, 14.793434, 0.0]]}]},
			"L_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.570411, 15.43115, -0.260851], [8.569546, 15.441966, -0.25], [8.570411, 15.43115, -0.239149], [8.571276, 15.420333, -0.25], [8.570411, 15.43115, -0.260851], [8.581227, 15.432015, -0.25], [8.570411, 15.43115, -0.239149], [8.559595, 15.430284, -0.25], [8.569546, 15.441966, -0.25], [8.581227, 15.432015, -0.25], [8.571276, 15.420333, -0.25], [8.559595, 15.430284, -0.25], [8.570411, 15.43115, -0.260851], [8.581227, 15.432015, -0.25], [7.55, 15.349517, -0.25]]}, {"shapeName": "L_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.468367, 16.369928, -0.260851], [7.457551, 16.369062, -0.25], [7.468367, 16.369928, -0.239149], [7.479184, 16.370793, -0.25], [7.468367, 16.369928, -0.260851], [7.467502, 16.380743, -0.25], [7.468367, 16.369928, -0.239149], [7.469233, 16.359111, -0.25], [7.457551, 16.369062, -0.25], [7.467502, 16.380743, -0.25], [7.479184, 16.370793, -0.25], [7.469233, 16.359111, -0.25], [7.468367, 16.369928, -0.260851], [7.467502, 16.380743, -0.25], [7.55, 15.349517, -0.25]]}, {"shapeName": "L_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.549135, 15.360333, 0.773671], [7.539184, 15.348651, 0.773671], [7.550866, 15.3387, 0.773671], [7.560817, 15.350382, 0.773671], [7.549135, 15.360333, 0.773671], [7.55, 15.349517, 0.784521], [7.550866, 15.3387, 0.773671], [7.55, 15.349517, 0.76282], [7.539184, 15.348651, 0.773671], [7.55, 15.349517, 0.784521], [7.560817, 15.350382, 0.773671], [7.55, 15.349517, 0.76282], [7.549135, 15.360333, 0.773671], [7.55, 15.349517, 0.784521], [7.55, 15.349517, -0.25]]}]},
			"L_heel_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_heel_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.025451, 0.186549, -0.260851], [2.025451, 0.1974, -0.25], [2.025451, 0.186549, -0.239149], [2.025451, 0.175698, -0.25], [2.025451, 0.186549, -0.260851], [2.036301, 0.186549, -0.25], [2.025451, 0.186549, -0.239149], [2.0146, 0.186549, -0.25], [2.025451, 0.1974, -0.25], [2.036301, 0.186549, -0.25], [2.025451, 0.175698, -0.25], [2.0146, 0.186549, -0.25], [2.025451, 0.186549, -0.260851], [2.036301, 0.186549, -0.25], [1.00178, 0.186549, -0.25]]}, {"shapeName": "L_heel_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.00178, 1.21022, -0.260851], [0.990929, 1.21022, -0.25], [1.00178, 1.21022, -0.239149], [1.012631, 1.21022, -0.25], [1.00178, 1.21022, -0.260851], [1.00178, 1.22107, -0.25], [1.00178, 1.21022, -0.239149], [1.00178, 1.199369, -0.25], [0.990929, 1.21022, -0.25], [1.00178, 1.22107, -0.25], [1.012631, 1.21022, -0.25], [1.00178, 1.199369, -0.25], [1.00178, 1.21022, -0.260851], [1.00178, 1.22107, -0.25], [1.00178, 0.186549, -0.25]]}, {"shapeName": "L_heel_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.00178, 0.1974, 0.773671], [0.990929, 0.186549, 0.773671], [1.00178, 0.175698, 0.773671], [1.012631, 0.186549, 0.773671], [1.00178, 0.1974, 0.773671], [1.00178, 0.186549, 0.784521], [1.00178, 0.175698, 0.773671], [1.00178, 0.186549, 0.76282], [0.990929, 0.186549, 0.773671], [1.00178, 0.186549, 0.784521], [1.012631, 0.186549, 0.773671], [1.00178, 0.186549, 0.76282], [1.00178, 0.1974, 0.773671], [1.00178, 0.186549, 0.784521], [1.00178, 0.186549, -0.25]]}]},
			"L_toe_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toe_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.00178, 0.1974, 2.023671], [0.990929, 0.186549, 2.023671], [1.00178, 0.175698, 2.023671], [1.012631, 0.186549, 2.023671], [1.00178, 0.1974, 2.023671], [1.00178, 0.186549, 2.034521], [1.00178, 0.175698, 2.023671], [1.00178, 0.186549, 2.01282], [0.990929, 0.186549, 2.023671], [1.00178, 0.186549, 2.034521], [1.012631, 0.186549, 2.023671], [1.00178, 0.186549, 2.01282], [1.00178, 0.1974, 2.023671], [1.00178, 0.186549, 2.034521], [1.00178, 0.186549, 1.0]]}, {"shapeName": "L_toe_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.021891, 0.1974, 1.0], [-0.021891, 0.186549, 0.989149], [-0.021891, 0.175698, 1.0], [-0.021891, 0.186549, 1.010851], [-0.021891, 0.1974, 1.0], [-0.032741, 0.186549, 1.0], [-0.021891, 0.175698, 1.0], [-0.01104, 0.186549, 1.0], [-0.021891, 0.186549, 0.989149], [-0.032741, 0.186549, 1.0], [-0.021891, 0.186549, 1.010851], [-0.01104, 0.186549, 1.0], [-0.021891, 0.1974, 1.0], [-0.032741, 0.186549, 1.0], [1.00178, 0.186549, 1.0]]}, {"shapeName": "L_toe_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.990929, -0.837122, 1.0], [1.00178, -0.837122, 0.989149], [1.012631, -0.837122, 1.0], [1.00178, -0.837122, 1.010851], [0.990929, -0.837122, 1.0], [1.00178, -0.847972, 1.0], [1.012631, -0.837122, 1.0], [1.00178, -0.826271, 1.0], [1.00178, -0.837122, 0.989149], [1.00178, -0.847972, 1.0], [1.00178, -0.837122, 1.010851], [1.00178, -0.826271, 1.0], [0.990929, -0.837122, 1.0], [1.00178, -0.847972, 1.0], [1.00178, 0.186549, 1.0]]}]},
			"L_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_D_CTLShape", "degree": 3, "form": 2, "points": [[8.284465, 15.233006, -0.117542], [8.3, 15.349517, -0.166229], [8.315535, 15.466027, -0.117542], [8.32197, 15.514288, -0.0], [8.315535, 15.466027, 0.117542], [8.3, 15.349517, 0.166229], [8.284465, 15.233006, 0.117542], [8.278031, 15.184746, -0.0]]}]},
			"L_arm_IK_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_arm_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.925, 15.080105, -0.219411], [6.925, 15.299517, -0.310294], [6.925, 15.518928, -0.219411], [6.925, 15.609811, -0.0], [6.925, 15.518928, 0.219411], [6.925, 15.299517, 0.310294], [6.925, 15.080105, 0.219411], [6.925, 14.989222, -0.0]]}]},
			"L_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_B_CTLShape", "degree": 3, "form": 2, "points": [[7.559374, 15.232349, -0.117542], [7.55, 15.349517, -0.166229], [7.540627, 15.466684, -0.117542], [7.536744, 15.515216, -0.0], [7.540627, 15.466684, 0.117542], [7.55, 15.349517, 0.166229], [7.559374, 15.232349, 0.117542], [7.563256, 15.183817, -0.0]]}]},
			"L_bendyArm_B_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.925, 15.399517, -0.8], [4.925, 15.459517, -0.8], [4.925, 15.299517, -0.95], [4.925, 15.139516, -0.8], [4.925, 15.199516, -0.8], [4.925, 15.199516, -0.6], [4.925, 14.999517, -0.6], [4.925, 14.999517, -0.66], [4.925, 14.849517, -0.5], [4.925, 14.999517, -0.34], [4.925, 14.999517, -0.4], [4.925, 15.199516, -0.4], [4.925, 15.199516, -0.2], [4.925, 15.139516, -0.2], [4.925, 15.299517, -0.05], [4.925, 15.459517, -0.2], [4.925, 15.399517, -0.2], [4.925, 15.399517, -0.4], [4.925, 15.599517, -0.4], [4.925, 15.599517, -0.34], [4.925, 15.749517, -0.5], [4.925, 15.599517, -0.66], [4.925, 15.599517, -0.6], [4.925, 15.399517, -0.6], [4.925, 15.399517, -0.8]]}]},
			"C_neck_FK_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_C_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 19.889618, -1.0], [0.0, 19.927886, -1.007612], [0.0, 19.960328, -1.02929], [0.0, 19.982006, -1.061732], [0.0, 19.989618, -1.1], [0.0, 19.982006, -1.138268], [0.0, 19.960328, -1.17071], [0.0, 19.927886, -1.192388], [0.0, 19.889618, -1.2], [0.0, 19.85135, -1.192388], [0.0, 19.818908, -1.17071], [0.0, 19.79723, -1.138268], [0.0, 19.789618, -1.1], [0.0, 19.79723, -1.061732], [0.0, 19.818908, -1.02929], [0.0, 19.85135, -1.007612], [0.0, 19.889618, -1.0], [0.0, 19.889618, 0.0]]}]},
			"L_bendyArm_B_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_B_CTLShape", "degree": 1, "form": 0, "points": [[4.925, 15.466184, -1.0], [4.925, 15.566184, -1.0], [4.925, 15.299517, -1.25], [4.925, 15.03285, -1.0], [4.925, 15.13285, -1.0], [4.925, 15.13285, -0.666667], [4.925, 14.799517, -0.666667], [4.925, 14.799517, -0.766667], [4.925, 14.549517, -0.5], [4.925, 14.799517, -0.233333], [4.925, 14.799517, -0.333333], [4.925, 15.13285, -0.333333], [4.925, 15.13285, 0.0], [4.925, 15.03285, 0.0], [4.925, 15.299517, 0.25], [4.925, 15.566184, 0.0], [4.925, 15.466184, 0.0], [4.925, 15.466184, -0.333333], [4.925, 15.799517, -0.333333], [4.925, 15.799517, -0.233333], [4.925, 16.049517, -0.5], [4.925, 15.799517, -0.766667], [4.925, 15.799517, -0.666667], [4.925, 15.466184, -0.666667], [4.925, 15.466184, -1.0]]}]},
			"L_legBase_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.293131, 0.027631], [1.0, 8.935468, 0.072339], [1.0, 8.798853, 0.089416], [1.0, 9.040582, 0.913255], [1.0, 9.463209, 1.388262], [1.0, 9.905307, 1.332999], [1.0, 10.198005, 0.768577], [1.0, 10.229506, -0.089416], [1.0, 10.09289, -0.072339], [1.0, 9.735228, -0.027631], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0]]}]},
			"C_hip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_hip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 9.773434, -0.010851], [1.023671, 9.784285, 0.0], [1.023671, 9.773434, 0.010851], [1.023671, 9.762583, 0.0], [1.023671, 9.773434, -0.010851], [1.034521, 9.773434, 0.0], [1.023671, 9.773434, 0.010851], [1.01282, 9.773434, 0.0], [1.023671, 9.784285, 0.0], [1.034521, 9.773434, 0.0], [1.023671, 9.762583, 0.0], [1.01282, 9.773434, 0.0], [1.023671, 9.773434, -0.010851], [1.034521, 9.773434, 0.0], [0.0, 9.773434, 0.0]]}, {"shapeName": "C_hip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 10.797105, -0.010851], [-0.010851, 10.797105, 0.0], [0.0, 10.797105, 0.010851], [0.010851, 10.797105, 0.0], [0.0, 10.797105, -0.010851], [0.0, 10.807955, 0.0], [0.0, 10.797105, 0.010851], [0.0, 10.786254, 0.0], [-0.010851, 10.797105, 0.0], [0.0, 10.807955, 0.0], [0.010851, 10.797105, 0.0], [0.0, 10.786254, 0.0], [0.0, 10.797105, -0.010851], [0.0, 10.807955, 0.0], [0.0, 9.773434, 0.0]]}, {"shapeName": "C_hip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 9.784285, 1.023671], [-0.010851, 9.773434, 1.023671], [0.0, 9.762583, 1.023671], [0.010851, 9.773434, 1.023671], [0.0, 9.784285, 1.023671], [0.0, 9.773434, 1.034521], [0.0, 9.762583, 1.023671], [0.0, 9.773434, 1.01282], [-0.010851, 9.773434, 1.023671], [0.0, 9.773434, 1.034521], [0.010851, 9.773434, 1.023671], [0.0, 9.773434, 1.01282], [0.0, 9.784285, 1.023671], [0.0, 9.773434, 1.034521], [0.0, 9.773434, 0.0]]}]},
			"L_legEnd_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_legEnd_FK_CTLShape", "degree": 1, "form": 0, "points": [[0.5, 1.080058, -0.558156], [0.5, 2.072336, -0.434122], [0.5, 1.948301, 0.558156], [0.5, 0.956023, 0.434122], [1.5, 0.956023, 0.434122], [1.5, 1.948301, 0.558156], [1.5, 2.072336, -0.434122], [1.5, 1.080058, -0.558156], [0.5, 1.080058, -0.558156], [0.5, 0.956023, 0.434122], [0.5, 1.948301, 0.558156], [1.5, 1.948301, 0.558156], [1.5, 0.956023, 0.434122], [1.5, 1.080058, -0.558156], [1.5, 2.072336, -0.434122], [0.5, 2.072336, -0.434122]]}]},
			"L_innerBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_innerBall_CTLShape", "degree": 1, "form": 0, "points": [[0.30178, 0.186549, 1.1], [0.30178, 0.086549, 1.0], [0.40178, 0.186549, 1.0], [0.30178, 0.186549, 1.1], [0.20178, 0.186549, 1.0], [0.30178, 0.086549, 1.0], [0.30178, 0.186549, 0.9], [0.20178, 0.186549, 1.0], [0.30178, 0.286549, 1.0], [0.30178, 0.186549, 1.1], [0.40178, 0.186549, 1.0], [0.30178, 0.186549, 0.9], [0.30178, 0.286549, 1.0], [0.40178, 0.186549, 1.0]]}]},
			"C_neckBase_A_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.269451, 18.556285, -1.057876], [0.0, 18.016285, -1.496062], [-1.269451, 18.556285, -1.057876], [-1.795274, 19.096285, 0.0], [-1.269451, 18.556285, 1.057876], [0.0, 18.016285, 1.496062], [1.269451, 18.556285, 1.057876], [1.795274, 19.096285, 0.0]]}]},
			"C_world_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_world_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 0.0, -0.054255], [5.118355, 0.054255, 0.0], [5.118355, 0.0, 0.054255], [5.118355, -0.054255, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [5.118355, 0.0, 0.054255], [5.0641, 0.0, 0.0], [5.118355, 0.054255, 0.0], [5.172605, 0.0, 0.0], [5.118355, -0.054255, 0.0], [5.0641, 0.0, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 5.118355, -0.054255], [-0.054255, 5.118355, 0.0], [0.0, 5.118355, 0.054255], [0.054255, 5.118355, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 5.118355, 0.054255], [0.0, 5.0641, 0.0], [-0.054255, 5.118355, 0.0], [0.0, 5.172605, 0.0], [0.054255, 5.118355, 0.0], [0.0, 5.0641, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 0.054255, 5.118355], [-0.054255, 0.0, 5.118355], [0.0, -0.054255, 5.118355], [0.054255, 0.0, 5.118355], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, -0.054255, 5.118355], [0.0, 0.0, 5.0641], [-0.054255, 0.0, 5.118355], [0.0, 0.0, 5.172605], [0.054255, 0.0, 5.118355], [0.0, 0.0, 5.0641], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, 0.0, 0.0]]}]},
			"L_bendyArm_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_bendyArm_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.920739, 15.299517, -0.01225], [6.918107, 15.310368, -0.001723], [6.915475, 15.299517, 0.008804], [6.918107, 15.288666, -0.001723], [6.920739, 15.299517, -0.01225], [6.928633, 15.299517, 0.000908], [6.915475, 15.299517, 0.008804], [6.90758, 15.299517, -0.004355], [6.918107, 15.310368, -0.001723], [6.928633, 15.299517, 0.000908], [6.918107, 15.288666, -0.001723], [6.90758, 15.299517, -0.004355], [6.920739, 15.299517, -0.01225], [6.928633, 15.299517, 0.000908], [5.925, 15.299517, -0.25]]}, {"shapeName": "L_bendyArm_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[5.927632, 16.323188, -0.260527], [5.914473, 16.323188, -0.252632], [5.922368, 16.323188, -0.239473], [5.935527, 16.323188, -0.247368], [5.927632, 16.323188, -0.260527], [5.925, 16.334038, -0.25], [5.922368, 16.323188, -0.239473], [5.925, 16.312337, -0.25], [5.914473, 16.323188, -0.252632], [5.925, 16.334038, -0.25], [5.935527, 16.323188, -0.247368], [5.925, 16.312337, -0.25], [5.927632, 16.323188, -0.260527], [5.925, 16.334038, -0.25], [5.925, 15.299517, -0.25]]}, {"shapeName": "L_bendyArm_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[5.676723, 15.310368, 0.743107], [5.666196, 15.299517, 0.740475], [5.676723, 15.288666, 0.743107], [5.68725, 15.299517, 0.745738], [5.676723, 15.310368, 0.743107], [5.674092, 15.299517, 0.753633], [5.676723, 15.288666, 0.743107], [5.679355, 15.299517, 0.73258], [5.666196, 15.299517, 0.740475], [5.674092, 15.299517, 0.753633], [5.68725, 15.299517, 0.745738], [5.679355, 15.299517, 0.73258], [5.676723, 15.310368, 0.743107], [5.674092, 15.299517, 0.753633], [5.925, 15.299517, -0.25]]}]},
			"L_bendyArm_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_bendyArm_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[4.915475, 15.299517, -0.508804], [4.918107, 15.310368, -0.498277], [4.920739, 15.299517, -0.48775], [4.918107, 15.288666, -0.498277], [4.915475, 15.299517, -0.508804], [4.928633, 15.299517, -0.500908], [4.920739, 15.299517, -0.48775], [4.90758, 15.299517, -0.495645], [4.918107, 15.310368, -0.498277], [4.928633, 15.299517, -0.500908], [4.918107, 15.288666, -0.498277], [4.90758, 15.299517, -0.495645], [4.915475, 15.299517, -0.508804], [4.928633, 15.299517, -0.500908], [3.925, 15.299517, -0.25]]}, {"shapeName": "L_bendyArm_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[3.922368, 16.323188, -0.260527], [3.914473, 16.323188, -0.247368], [3.927632, 16.323188, -0.239473], [3.935527, 16.323188, -0.252632], [3.922368, 16.323188, -0.260527], [3.925, 16.334038, -0.25], [3.927632, 16.323188, -0.239473], [3.925, 16.312337, -0.25], [3.914473, 16.323188, -0.247368], [3.925, 16.334038, -0.25], [3.935527, 16.323188, -0.252632], [3.925, 16.312337, -0.25], [3.922368, 16.323188, -0.260527], [3.925, 16.334038, -0.25], [3.925, 15.299517, -0.25]]}, {"shapeName": "L_bendyArm_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.173277, 15.310368, 0.743107], [4.16275, 15.299517, 0.745738], [4.173277, 15.288666, 0.743107], [4.183804, 15.299517, 0.740475], [4.173277, 15.310368, 0.743107], [4.175908, 15.299517, 0.753633], [4.173277, 15.288666, 0.743107], [4.170645, 15.299517, 0.73258], [4.16275, 15.299517, 0.745738], [4.175908, 15.299517, 0.753633], [4.183804, 15.299517, 0.740475], [4.170645, 15.299517, 0.73258], [4.173277, 15.310368, 0.743107], [4.175908, 15.299517, 0.753633], [3.925, 15.299517, -0.25]]}]},
			"L_arm_PV_CTL": {"color": 6, "shapes": [{"shapeName": "L_arm_PV_CTLShape", "degree": 1, "form": 0, "points": [[4.825, 15.399517, -10.4], [4.825, 15.199517, -10.4], [4.825, 15.199517, -10.6], [4.825, 15.399517, -10.6], [5.025, 15.399517, -10.6], [5.025, 15.199517, -10.6], [5.025, 15.199517, -10.4], [5.025, 15.399517, -10.4], [4.825, 15.399517, -10.4], [4.825, 15.399517, -10.6], [4.825, 15.199517, -10.6], [5.025, 15.199517, -10.6], [5.025, 15.399517, -10.6], [5.025, 15.399517, -10.4], [5.025, 15.199517, -10.4], [4.825, 15.199517, -10.4]]}]},
			"L_loLeg_shaper_D_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_D_CTLShape", "degree": 1, "form": 0, "points": [[2.5, 2.314179, 0.1], [2.511418, 2.238234, 0.090507], [2.543935, 2.173851, 0.082459], [2.592598, 2.13083, 0.077081], [2.65, 2.115724, 0.075193], [2.707402, 2.13083, 0.077081], [2.756065, 2.173851, 0.082459], [2.788582, 2.238234, 0.090507], [2.8, 2.314179, 0.1], [2.788582, 2.390124, 0.109493], [2.756065, 2.454507, 0.117541], [2.707402, 2.497528, 0.122919], [2.65, 2.512635, 0.124807], [2.592598, 2.497528, 0.122919], [2.543935, 2.454507, 0.117541], [2.511418, 2.390124, 0.109493], [2.5, 2.314179, 0.1], [1.0, 2.314179, 0.1]]}]},
			"L_upArm_shaper_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upArm_shaper_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.115475, 15.299517, -0.558804], [5.118107, 15.310368, -0.548277], [5.120739, 15.299517, -0.53775], [5.118107, 15.288666, -0.548277], [5.115475, 15.299517, -0.558804], [5.128633, 15.299517, -0.550908], [5.120739, 15.299517, -0.53775], [5.10758, 15.299517, -0.545645], [5.118107, 15.310368, -0.548277], [5.128633, 15.299517, -0.550908], [5.118107, 15.288666, -0.548277], [5.10758, 15.299517, -0.545645], [5.115475, 15.299517, -0.558804], [5.128633, 15.299517, -0.550908], [4.125, 15.299517, -0.3]]}, {"shapeName": "L_upArm_shaper_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[4.122368, 16.323188, -0.310527], [4.114473, 16.323188, -0.297368], [4.127632, 16.323188, -0.289473], [4.135527, 16.323188, -0.302632], [4.122368, 16.323188, -0.310527], [4.125, 16.334038, -0.3], [4.127632, 16.323188, -0.289473], [4.125, 16.312337, -0.3], [4.114473, 16.323188, -0.297368], [4.125, 16.334038, -0.3], [4.135527, 16.323188, -0.302632], [4.125, 16.312337, -0.3], [4.122368, 16.323188, -0.310527], [4.125, 16.334038, -0.3], [4.125, 15.299517, -0.3]]}, {"shapeName": "L_upArm_shaper_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.373277, 15.310368, 0.693107], [4.36275, 15.299517, 0.695738], [4.373277, 15.288666, 0.693107], [4.383804, 15.299517, 0.690475], [4.373277, 15.310368, 0.693107], [4.375908, 15.299517, 0.703633], [4.373277, 15.288666, 0.693107], [4.370645, 15.299517, 0.68258], [4.36275, 15.299517, 0.695738], [4.375908, 15.299517, 0.703633], [4.383804, 15.299517, 0.690475], [4.370645, 15.299517, 0.68258], [4.373277, 15.310368, 0.693107], [4.375908, 15.299517, 0.703633], [4.125, 15.299517, -0.3]]}]},
			"C_cog_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.645585, 9.773434, -1.645585], [0.0, 9.773434, -2.327207], [-1.645585, 9.773434, -1.645585], [-2.327207, 9.773434, 0.0], [-1.645585, 9.773434, 1.645585], [0.0, 9.773434, 2.327207], [1.645585, 9.773434, 1.645585], [2.327207, 9.773434, 0.0]]}]},
			"C_neck_FK_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_A_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 18.556285, -1.0], [0.0, 18.594553, -1.007612], [0.0, 18.626995, -1.02929], [0.0, 18.648673, -1.061732], [0.0, 18.656285, -1.1], [0.0, 18.648673, -1.138268], [0.0, 18.626995, -1.17071], [0.0, 18.594553, -1.192388], [0.0, 18.556285, -1.2], [0.0, 18.518017, -1.192388], [0.0, 18.485575, -1.17071], [0.0, 18.463897, -1.138268], [0.0, 18.456285, -1.1], [0.0, 18.463897, -1.061732], [0.0, 18.485575, -1.02929], [0.0, 18.518017, -1.007612], [0.0, 18.556285, -1.0], [0.0, 18.556285, 0.0]]}]},
			"L_toe_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_toe_FK_CTLShape", "degree": 3, "form": 2, "points": [[1.393586, 0.578355, 1.0], [1.00178, 0.740646, 1.0], [0.609974, 0.578355, 1.0], [0.447683, 0.186549, 1.0], [0.609974, -0.205257, 1.0], [1.00178, -0.367548, 1.0], [1.393586, -0.205257, 1.0], [1.555877, 0.186549, 1.0]]}]},
			"C_head_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.057876, 21.614161, 0.0], [0.0, 22.052347, 0.0], [-1.057876, 21.614161, 0.0], [-1.496062, 20.556285, 0.0], [-1.057876, 19.498409, 0.0], [0.0, 19.060223, 0.0], [1.057876, 19.498409, 0.0], [1.496062, 20.556285, 0.0]]}]},
			"C_chest_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.846301, 15.273434, -0.705251], [0.0, 15.633434, -0.997375], [-0.846301, 15.273434, -0.705251], [-1.19685, 14.913434, 0.0], [-0.846301, 15.273434, 0.705251], [0.0, 15.633434, 0.997375], [0.846301, 15.273434, 0.705251], [1.19685, 14.913434, 0.0]]}]},
			"L_upLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_upLeg_FK_CTLShape", "degree": 1, "form": 0, "points": [[0.5, 8.956023, -0.434122], [0.5, 9.948301, -0.558156], [0.5, 10.072336, 0.434122], [0.5, 9.080058, 0.558156], [1.5, 9.080058, 0.558156], [1.5, 10.072336, 0.434122], [1.5, 9.948301, -0.558156], [1.5, 8.956023, -0.434122], [0.5, 8.956023, -0.434122], [0.5, 9.080058, 0.558156], [0.5, 10.072336, 0.434122], [1.5, 10.072336, 0.434122], [1.5, 9.080058, 0.558156], [1.5, 8.956023, -0.434122], [1.5, 9.948301, -0.558156], [0.5, 9.948301, -0.558156]]}]},
			"L_bendyArm_A_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_A_CTLShape", "degree": 1, "form": 0, "points": [[3.803732, 15.466184, -0.735071], [3.803732, 15.566184, -0.735071], [3.743098, 15.299517, -0.977607], [3.803732, 15.03285, -0.735071], [3.803732, 15.13285, -0.735071], [3.884577, 15.13285, -0.411691], [3.884577, 14.799517, -0.411691], [3.860324, 14.799517, -0.508705], [3.925, 14.549517, -0.25], [3.989676, 14.799517, 0.008705], [3.965423, 14.799517, -0.088309], [3.965423, 15.13285, -0.088309], [4.046268, 15.13285, 0.235071], [4.046268, 15.03285, 0.235071], [4.106902, 15.299517, 0.477607], [4.046268, 15.566184, 0.235071], [4.046268, 15.466184, 0.235071], [3.965423, 15.466184, -0.088309], [3.965423, 15.799517, -0.088309], [3.989676, 15.799517, 0.008705], [3.925, 16.049517, -0.25], [3.860324, 15.799517, -0.508705], [3.884577, 15.799517, -0.411691], [3.884577, 15.466184, -0.411691], [3.803732, 15.466184, -0.735071]]}]},
			"C_torso_FK_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_D_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 13.273434, -1.0], [0.0, 13.311702, -1.007612], [0.0, 13.344144, -1.02929], [0.0, 13.365822, -1.061732], [0.0, 13.373434, -1.1], [0.0, 13.365822, -1.138268], [0.0, 13.344144, -1.17071], [0.0, 13.311702, -1.192388], [0.0, 13.273434, -1.2], [0.0, 13.235166, -1.192388], [0.0, 13.202724, -1.17071], [0.0, 13.181046, -1.138268], [0.0, 13.173434, -1.1], [0.0, 13.181046, -1.061732], [0.0, 13.202724, -1.02929], [0.0, 13.235166, -1.007612], [0.0, 13.273434, -1.0], [0.0, 13.273434, 0.0]]}]},
			"L_wrist_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_wrist_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[7.948671, 15.299517, -0.010851], [7.948671, 15.310368, -0.0], [7.948671, 15.299517, 0.010851], [7.948671, 15.288666, -0.0], [7.948671, 15.299517, -0.010851], [7.959521, 15.299517, -0.0], [7.948671, 15.299517, 0.010851], [7.93782, 15.299517, -0.0], [7.948671, 15.310368, -0.0], [7.959521, 15.299517, -0.0], [7.948671, 15.288666, -0.0], [7.93782, 15.299517, -0.0], [7.948671, 15.299517, -0.010851], [7.959521, 15.299517, -0.0], [6.925, 15.299517, -0.0]]}, {"shapeName": "L_wrist_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[6.925, 16.323188, -0.010851], [6.914149, 16.323188, -0.0], [6.925, 16.323188, 0.010851], [6.935851, 16.323188, -0.0], [6.925, 16.323188, -0.010851], [6.925, 16.334038, -0.0], [6.925, 16.323188, 0.010851], [6.925, 16.312337, -0.0], [6.914149, 16.323188, -0.0], [6.925, 16.334038, -0.0], [6.935851, 16.323188, -0.0], [6.925, 16.312337, -0.0], [6.925, 16.323188, -0.010851], [6.925, 16.334038, -0.0], [6.925, 15.299517, -0.0]]}, {"shapeName": "L_wrist_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[6.925, 15.310368, 1.023671], [6.914149, 15.299517, 1.023671], [6.925, 15.288666, 1.023671], [6.935851, 15.299517, 1.023671], [6.925, 15.310368, 1.023671], [6.925, 15.299517, 1.034521], [6.925, 15.288666, 1.023671], [6.925, 15.299517, 1.01282], [6.914149, 15.299517, 1.023671], [6.925, 15.299517, 1.034521], [6.935851, 15.299517, 1.023671], [6.925, 15.299517, 1.01282], [6.925, 15.310368, 1.023671], [6.925, 15.299517, 1.034521], [6.925, 15.299517, -0.0]]}]},
			"L_heel_CTL": {"color": 20, "shapes": [{"shapeName": "L_heel_CTLShape", "degree": 1, "form": 0, "points": [[1.00178, 0.186549, -0.35], [1.00178, 0.086549, -0.45], [1.10178, 0.186549, -0.45], [1.00178, 0.186549, -0.35], [0.90178, 0.186549, -0.45], [1.00178, 0.086549, -0.45], [1.00178, 0.186549, -0.55], [0.90178, 0.186549, -0.45], [1.00178, 0.286549, -0.45], [1.00178, 0.186549, -0.35], [1.10178, 0.186549, -0.45], [1.00178, 0.186549, -0.55], [1.00178, 0.286549, -0.45], [1.10178, 0.186549, -0.45]]}]},
			"world_D_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -73.724705], [32.753065, 0.0, -40.939736], [24.553632, 0.0, -40.939736], [24.553632, 0.0, -24.547251], [40.946117, 0.0, -24.547251], [40.946117, 0.0, -32.746684], [73.724705, 0.0, 0.0], [40.939736, 0.0, 32.753065], [40.939736, 0.0, 24.553632], [24.547251, 0.0, 24.553632], [24.547251, 0.0, 40.946117], [32.746684, 0.0, 40.946117], [0.0, 0.0, 73.724705], [-32.753065, 0.0, 40.939736], [-24.553632, 0.0, 40.939736], [-24.553632, 0.0, 24.547251], [-40.946117, 0.0, 24.547251], [-40.946117, 0.0, 32.746684], [-73.724705, 0.0, 0.0], [-40.939736, 0.0, -32.753065], [-40.939736, 0.0, -24.553632], [-24.547251, 0.0, -24.553632], [-24.547251, 0.0, -40.946117], [-32.746684, 0.0, -40.946117], [0.0, 0.0, -73.724705], [6.419167, 0.089332, -67.420394], [5.857649, 0.0, -66.820592], [5.857649, 0.0, -64.370333], [5.347179, 0.0, -64.370333], [5.379083, 0.0, -66.839734], [5.015373, 0.0, -66.654689], [5.028135, 0.0, -65.5827], [4.511283, 0.0, -65.5827], [4.511283, 0.0, -66.654689], [4.192239, 0.0, -66.839734], [4.192239, 0.0, -64.332048], [3.675388, 0.0, -64.332048], [3.675388, 0.0, -66.903543], [4.090145, 0.0, -67.3183], [4.728233, 0.0, -66.999256], [5.43013, 0.0, -67.3183], [5.857649, 0.0, -66.833353], [5.43013, 0.0, -67.3183], [4.734614, 0.0, -67.005637], [4.090145, 0.0, -67.311919], [2.845873, 0.0, -67.3183], [3.267011, 0.0, -66.903543], [3.267011, 0.0, -64.753186], [2.845873, 0.0, -64.332048], [1.499507, 0.0, -64.332048], [1.08475, 0.0, -64.753186], [1.08475, 0.0, -66.903543], [1.499507, 0.0, -67.3183], [2.845873, 0.0, -67.3183], [2.686351, 0.0, -66.839734], [2.75016, 0.0, -64.861661], [1.59522, 0.0, -64.874423], [1.601601, 0.0, -66.839734], [2.692732, 0.0, -66.852496], [2.845873, 0.0, -67.3183], [1.499507, 0.0, -67.3183], [0.638088, 0.0, -67.3183], [0.669993, 0.0, -64.332048], [-0.784848, 0.0, -64.332048], [-1.205987, 0.0, -64.753186], [-1.205987, 0.0, -65.65289], [-0.778468, 0.0, -66.067647], [-0.752944, 0.0, -66.099552], [-1.58884, 0.0, -67.305539], [-1.58884, 0.0, -67.3183], [-0.989037, 0.0, -67.3183], [-0.153141, 0.0, -66.105933], [0.159522, 0.0, -66.105933], [0.159522, 0.0, -64.829756], [-0.644469, 0.0, -64.829756], [-0.65085, 0.0, -65.589081], [0.159522, 0.0, -65.589081], [0.159522, 0.0, -67.3183], [0.638088, 0.0, -67.3183], [-4.102907, 0.0, -67.3183], [-4.102907, 0.0, -66.839734], [-2.431116, 0.0, -66.833353], [-2.431116, 0.0, -64.332048], [-1.914264, 0.0, -64.332048], [-1.914264, 0.0, -67.3183], [-6.278787, 0.0, -67.3183], [-6.66164, 0.0, -66.903543], [-6.693545, 0.0, -64.753186], [-6.278787, 0.0, -64.332048], [-4.511283, 0.0, -64.332048], [-4.511283, 0.0, -67.3183], [-5.034516, 0.0, -66.839734], [-5.021754, 0.0, -64.816995], [-6.112885, 0.0, -64.816995], [-6.100123, 0.0, -66.826972], [-5.015373, 0.0, -66.852496], [-4.498521, 0.0, -67.3183]]}]},
			"L_upLeg_shaper_D_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_D_CTLShape", "degree": 1, "form": 0, "points": [[2.5, 6.314179, 0.4], [2.511418, 6.238234, 0.409493], [2.543935, 6.173851, 0.417541], [2.592598, 6.13083, 0.422919], [2.65, 6.115724, 0.424807], [2.707402, 6.13083, 0.422919], [2.756065, 6.173851, 0.417541], [2.788582, 6.238234, 0.409493], [2.8, 6.314179, 0.4], [2.788582, 6.390124, 0.390507], [2.756065, 6.454507, 0.382459], [2.707402, 6.497528, 0.377081], [2.65, 6.512635, 0.375193], [2.592598, 6.497528, 0.377081], [2.543935, 6.454507, 0.382459], [2.511418, 6.390124, 0.390507], [2.5, 6.314179, 0.4], [1.0, 6.314179, 0.4]]}]},
			"L_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_B_CTLShape", "degree": 3, "form": 2, "points": [[7.559374, 15.232349, -0.367542], [7.55, 15.349517, -0.416229], [7.540627, 15.466684, -0.367542], [7.536744, 15.515216, -0.25], [7.540627, 15.466684, -0.132458], [7.55, 15.349517, -0.083771], [7.559374, 15.232349, -0.132458], [7.563256, 15.183817, -0.25]]}]},
			"L_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_A_CTLShape", "degree": 3, "form": 2, "points": [[7.190535, 15.183006, -0.617542], [7.175, 15.299517, -0.666229], [7.159465, 15.416027, -0.617542], [7.153031, 15.464288, -0.5], [7.159465, 15.416027, -0.382458], [7.175, 15.299517, -0.333771], [7.190535, 15.183006, -0.382458], [7.19697, 15.134746, -0.5]]}]},
			"L_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_A_CTLShape", "degree": 3, "form": 2, "points": [[7.190535, 15.183006, -0.117542], [7.175, 15.299517, -0.166229], [7.159465, 15.416027, -0.117542], [7.153031, 15.464288, -0.0], [7.159465, 15.416027, 0.117542], [7.175, 15.299517, 0.166229], [7.190535, 15.183006, 0.117542], [7.19697, 15.134746, -0.0]]}]},
			"L_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_D_CTLShape", "degree": 3, "form": 2, "points": [[8.284465, 15.233006, -0.617542], [8.3, 15.349517, -0.666229], [8.315535, 15.466027, -0.617542], [8.32197, 15.514288, -0.5], [8.315535, 15.466027, -0.382458], [8.3, 15.349517, -0.333771], [8.284465, 15.233006, -0.382458], [8.278031, 15.184746, -0.5]]}]},
			"L_arm_IK_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_arm_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.925, 15.017416, -0.2821], [6.925, 15.299517, -0.39895], [6.925, 15.581617, -0.2821], [6.925, 15.698467, -0.0], [6.925, 15.581617, 0.2821], [6.925, 15.299517, 0.39895], [6.925, 15.017416, 0.2821], [6.925, 14.900567, -0.0]]}]},
			"C_torso_FK_E_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_E_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 15.297105, -0.010851], [-0.010851, 15.297105, 0.0], [0.0, 15.297105, 0.010851], [0.010851, 15.297105, 0.0], [0.0, 15.297105, -0.010851], [0.0, 15.307955, 0.0], [0.0, 15.297105, 0.010851], [0.0, 15.286254, 0.0], [-0.010851, 15.297105, 0.0], [0.0, 15.307955, 0.0], [0.010851, 15.297105, 0.0], [0.0, 15.286254, 0.0], [0.0, 15.297105, -0.010851], [0.0, 15.307955, 0.0], [0.0, 14.273434, 0.0]]}, {"shapeName": "C_torso_FK_E_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.023671, 14.273434, -0.010851], [-1.023671, 14.262583, 0.0], [-1.023671, 14.273434, 0.010851], [-1.023671, 14.284285, 0.0], [-1.023671, 14.273434, -0.010851], [-1.034521, 14.273434, 0.0], [-1.023671, 14.273434, 0.010851], [-1.01282, 14.273434, 0.0], [-1.023671, 14.262583, 0.0], [-1.034521, 14.273434, 0.0], [-1.023671, 14.284285, 0.0], [-1.01282, 14.273434, 0.0], [-1.023671, 14.273434, -0.010851], [-1.034521, 14.273434, 0.0], [0.0, 14.273434, 0.0]]}, {"shapeName": "C_torso_FK_E_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.010851, 14.273434, 1.023671], [0.0, 14.262583, 1.023671], [0.010851, 14.273434, 1.023671], [0.0, 14.284285, 1.023671], [-0.010851, 14.273434, 1.023671], [0.0, 14.273434, 1.034521], [0.010851, 14.273434, 1.023671], [0.0, 14.273434, 1.01282], [0.0, 14.262583, 1.023671], [0.0, 14.273434, 1.034521], [0.0, 14.284285, 1.023671], [0.0, 14.273434, 1.01282], [-0.010851, 14.273434, 1.023671], [0.0, 14.273434, 1.034521], [0.0, 14.273434, 0.0]]}]},
			"L_bendyArm_A_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[3.827986, 15.43285, -0.638057], [3.827986, 15.51285, -0.638057], [3.779479, 15.299517, -0.832086], [3.827986, 15.086183, -0.638057], [3.827986, 15.166183, -0.638057], [3.892662, 15.166183, -0.379353], [3.892662, 14.899517, -0.379353], [3.873259, 14.899517, -0.456964], [3.925, 14.699517, -0.25], [3.976741, 14.899517, -0.043036], [3.957338, 14.899517, -0.120647], [3.957338, 15.166183, -0.120647], [4.022014, 15.166183, 0.138057], [4.022014, 15.086183, 0.138057], [4.070521, 15.299517, 0.332086], [4.022014, 15.51285, 0.138057], [4.022014, 15.43285, 0.138057], [3.957338, 15.43285, -0.120647], [3.957338, 15.699517, -0.120647], [3.976741, 15.699517, -0.043036], [3.925, 15.899517, -0.25], [3.873259, 15.699517, -0.456964], [3.892662, 15.699517, -0.379353], [3.892662, 15.43285, -0.379353], [3.827986, 15.43285, -0.638057]]}]},
			"L_leg_IK_switch_C_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "L_leg_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[3.216019, 1.367725, -0.018307], [3.285871, 1.463372, -0.006351], [3.347716, 1.371396, -0.017848], [3.503752, 1.371396, -0.017848], [3.487393, 1.467761, -0.005802], [3.7539, 1.319158, -0.024378], [3.487393, 1.178669, -0.041939], [3.503752, 1.275034, -0.029893], [3.278372, 1.275034, -0.029893], [3.216019, 1.367725, -0.018307]]}, {"shapeName": "L_leg_IK_switch_C_OFF_CTLShape1", "degree": 1, "form": 0, "points": [[1.0, 1.514179, 0.0], [3.123098, 1.514179, 0.0], [3.076199, 1.753325, 0.029893], [2.854665, 1.753325, 0.029893], [2.871022, 1.849689, 0.041939], [2.604515, 1.709201, 0.024378], [2.871022, 1.560598, 0.005802], [2.854665, 1.656962, 0.017848], [3.006854, 1.656962, 0.017848], [3.02264, 1.52195, 0.000971]]}, {"shapeName": "L_leg_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[2.604515, 1.319158, -0.024378], [2.871022, 1.467761, -0.005802], [2.854665, 1.371396, -0.017848], [3.0107, 1.371396, -0.017848], [3.282217, 1.753325, 0.029893], [3.503752, 1.753325, 0.029893], [3.487393, 1.849689, 0.041939], [3.7539, 1.709201, 0.024378], [3.487393, 1.560598, 0.005802], [3.503752, 1.656962, 0.017848], [3.351561, 1.656962, 0.017848], [3.080044, 1.275034, -0.029893], [2.854665, 1.275034, -0.029893], [2.871022, 1.178669, -0.041939], [2.604515, 1.319158, -0.024378]]}]},
			"L_scapulaCtrl_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_scapulaCtrl_PIV_CTLShape", "degree": 1, "form": 0, "points": [[3.948671, 15.299517, -1.510851], [3.948671, 15.310368, -1.5], [3.948671, 15.299517, -1.489149], [3.948671, 15.288666, -1.5], [3.948671, 15.299517, -1.510851], [3.959521, 15.299517, -1.5], [3.948671, 15.299517, -1.489149], [3.93782, 15.299517, -1.5], [3.948671, 15.310368, -1.5], [3.959521, 15.299517, -1.5], [3.948671, 15.288666, -1.5], [3.93782, 15.299517, -1.5], [3.948671, 15.299517, -1.510851], [3.959521, 15.299517, -1.5], [2.925, 15.299517, -1.5]]}, {"shapeName": "L_scapulaCtrl_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.925, 16.323188, -1.510851], [2.914149, 16.323188, -1.5], [2.925, 16.323188, -1.489149], [2.935851, 16.323188, -1.5], [2.925, 16.323188, -1.510851], [2.925, 16.334038, -1.5], [2.925, 16.323188, -1.489149], [2.925, 16.312337, -1.5], [2.914149, 16.323188, -1.5], [2.925, 16.334038, -1.5], [2.935851, 16.323188, -1.5], [2.925, 16.312337, -1.5], [2.925, 16.323188, -1.510851], [2.925, 16.334038, -1.5], [2.925, 15.299517, -1.5]]}, {"shapeName": "L_scapulaCtrl_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.925, 15.310368, -0.476329], [2.914149, 15.299517, -0.476329], [2.925, 15.288666, -0.476329], [2.935851, 15.299517, -0.476329], [2.925, 15.310368, -0.476329], [2.925, 15.299517, -0.465479], [2.925, 15.288666, -0.476329], [2.925, 15.299517, -0.48718], [2.914149, 15.299517, -0.476329], [2.925, 15.299517, -0.465479], [2.935851, 15.299517, -0.476329], [2.925, 15.299517, -0.48718], [2.925, 15.310368, -0.476329], [2.925, 15.299517, -0.465479], [2.925, 15.299517, -1.5]]}]},
			"C_chest_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_CTLShape", "degree": 3, "form": 2, "points": [[1.410502, 15.273434, -1.175418], [0.0, 15.873434, -1.662291], [-1.410502, 15.273434, -1.175418], [-1.994749, 14.673434, 0.0], [-1.410502, 15.273434, 1.175418], [0.0, 15.873434, 1.662291], [1.410502, 15.273434, 1.175418], [1.994749, 14.673434, 0.0]]}]},
			"L_loLeg_shaper_A_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_A_CTLShape", "degree": 1, "form": 0, "points": [[2.5, 4.714179, 0.4], [2.511418, 4.638234, 0.390507], [2.543935, 4.573851, 0.382459], [2.592598, 4.53083, 0.377081], [2.65, 4.515724, 0.375193], [2.707402, 4.53083, 0.377081], [2.756065, 4.573851, 0.382459], [2.788582, 4.638234, 0.390507], [2.8, 4.714179, 0.4], [2.788582, 4.790124, 0.409493], [2.756065, 4.854507, 0.417541], [2.707402, 4.897528, 0.422919], [2.65, 4.912635, 0.424807], [2.592598, 4.897528, 0.422919], [2.543935, 4.854507, 0.417541], [2.511418, 4.790124, 0.409493], [2.5, 4.714179, 0.4], [1.0, 4.714179, 0.4]]}]},
			"C_neck_FK_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 19.579956, -0.010851], [-0.010851, 19.579956, 0.0], [0.0, 19.579956, 0.010851], [0.010851, 19.579956, 0.0], [0.0, 19.579956, -0.010851], [0.0, 19.590806, 0.0], [0.0, 19.579956, 0.010851], [0.0, 19.569105, 0.0], [-0.010851, 19.579956, 0.0], [0.0, 19.590806, 0.0], [0.010851, 19.579956, 0.0], [0.0, 19.569105, 0.0], [0.0, 19.579956, -0.010851], [0.0, 19.590806, 0.0], [0.0, 18.556285, 0.0]]}, {"shapeName": "C_neck_FK_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.023671, 18.556285, -0.010851], [-1.023671, 18.545434, 0.0], [-1.023671, 18.556285, 0.010851], [-1.023671, 18.567136, 0.0], [-1.023671, 18.556285, -0.010851], [-1.034521, 18.556285, 0.0], [-1.023671, 18.556285, 0.010851], [-1.01282, 18.556285, 0.0], [-1.023671, 18.545434, 0.0], [-1.034521, 18.556285, 0.0], [-1.023671, 18.567136, 0.0], [-1.01282, 18.556285, 0.0], [-1.023671, 18.556285, -0.010851], [-1.034521, 18.556285, 0.0], [0.0, 18.556285, 0.0]]}, {"shapeName": "C_neck_FK_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.010851, 18.556285, 1.023671], [0.0, 18.545434, 1.023671], [0.010851, 18.556285, 1.023671], [0.0, 18.567136, 1.023671], [-0.010851, 18.556285, 1.023671], [0.0, 18.556285, 1.034521], [0.010851, 18.556285, 1.023671], [0.0, 18.556285, 1.01282], [0.0, 18.545434, 1.023671], [0.0, 18.556285, 1.034521], [0.0, 18.567136, 1.023671], [0.0, 18.556285, 1.01282], [-0.010851, 18.556285, 1.023671], [0.0, 18.556285, 1.034521], [0.0, 18.556285, 0.0]]}]},
			"C_chest_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_chest_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 15.273434, -0.010851], [1.023671, 15.284285, 0.0], [1.023671, 15.273434, 0.010851], [1.023671, 15.262583, 0.0], [1.023671, 15.273434, -0.010851], [1.034521, 15.273434, 0.0], [1.023671, 15.273434, 0.010851], [1.01282, 15.273434, 0.0], [1.023671, 15.284285, 0.0], [1.034521, 15.273434, 0.0], [1.023671, 15.262583, 0.0], [1.01282, 15.273434, 0.0], [1.023671, 15.273434, -0.010851], [1.034521, 15.273434, 0.0], [0.0, 15.273434, 0.0]]}, {"shapeName": "C_chest_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 16.297105, -0.010851], [-0.010851, 16.297105, 0.0], [0.0, 16.297105, 0.010851], [0.010851, 16.297105, 0.0], [0.0, 16.297105, -0.010851], [0.0, 16.307955, 0.0], [0.0, 16.297105, 0.010851], [0.0, 16.286254, 0.0], [-0.010851, 16.297105, 0.0], [0.0, 16.307955, 0.0], [0.010851, 16.297105, 0.0], [0.0, 16.286254, 0.0], [0.0, 16.297105, -0.010851], [0.0, 16.307955, 0.0], [0.0, 15.273434, 0.0]]}, {"shapeName": "C_chest_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 15.284285, 1.023671], [-0.010851, 15.273434, 1.023671], [0.0, 15.262583, 1.023671], [0.010851, 15.273434, 1.023671], [0.0, 15.284285, 1.023671], [0.0, 15.273434, 1.034521], [0.0, 15.262583, 1.023671], [0.0, 15.273434, 1.01282], [-0.010851, 15.273434, 1.023671], [0.0, 15.273434, 1.034521], [0.010851, 15.273434, 1.023671], [0.0, 15.273434, 1.01282], [0.0, 15.284285, 1.023671], [0.0, 15.273434, 1.034521], [0.0, 15.273434, 0.0]]}]},
			"L_arm_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.948671, 15.299517, -10.510851], [5.948671, 15.310368, -10.5], [5.948671, 15.299517, -10.489149], [5.948671, 15.288666, -10.5], [5.948671, 15.299517, -10.510851], [5.959521, 15.299517, -10.5], [5.948671, 15.299517, -10.489149], [5.93782, 15.299517, -10.5], [5.948671, 15.310368, -10.5], [5.959521, 15.299517, -10.5], [5.948671, 15.288666, -10.5], [5.93782, 15.299517, -10.5], [5.948671, 15.299517, -10.510851], [5.959521, 15.299517, -10.5], [4.925, 15.299517, -10.5]]}, {"shapeName": "L_arm_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[4.925, 16.323188, -10.510851], [4.914149, 16.323188, -10.5], [4.925, 16.323188, -10.489149], [4.935851, 16.323188, -10.5], [4.925, 16.323188, -10.510851], [4.925, 16.334038, -10.5], [4.925, 16.323188, -10.489149], [4.925, 16.312337, -10.5], [4.914149, 16.323188, -10.5], [4.925, 16.334038, -10.5], [4.935851, 16.323188, -10.5], [4.925, 16.312337, -10.5], [4.925, 16.323188, -10.510851], [4.925, 16.334038, -10.5], [4.925, 15.299517, -10.5]]}, {"shapeName": "L_arm_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.925, 15.310368, -9.476329], [4.914149, 15.299517, -9.476329], [4.925, 15.288666, -9.476329], [4.935851, 15.299517, -9.476329], [4.925, 15.310368, -9.476329], [4.925, 15.299517, -9.465479], [4.925, 15.288666, -9.476329], [4.925, 15.299517, -9.48718], [4.914149, 15.299517, -9.476329], [4.925, 15.299517, -9.465479], [4.935851, 15.299517, -9.476329], [4.925, 15.299517, -9.48718], [4.925, 15.310368, -9.476329], [4.925, 15.299517, -9.465479], [4.925, 15.299517, -10.5]]}]},
			"L_bendyArm_C_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_C_CTLShape", "degree": 1, "form": 0, "points": [[6.046268, 15.466184, -0.735071], [6.046268, 15.566184, -0.735071], [6.106902, 15.299517, -0.977607], [6.046268, 15.03285, -0.735071], [6.046268, 15.13285, -0.735071], [5.965423, 15.13285, -0.411691], [5.965423, 14.799517, -0.411691], [5.989676, 14.799517, -0.508705], [5.925, 14.549517, -0.25], [5.860324, 14.799517, 0.008705], [5.884577, 14.799517, -0.088309], [5.884577, 15.13285, -0.088309], [5.803732, 15.13285, 0.235071], [5.803732, 15.03285, 0.235071], [5.743098, 15.299517, 0.477607], [5.803732, 15.566184, 0.235071], [5.803732, 15.466184, 0.235071], [5.884577, 15.466184, -0.088309], [5.884577, 15.799517, -0.088309], [5.860324, 15.799517, 0.008705], [5.925, 16.049517, -0.25], [5.989676, 15.799517, -0.508705], [5.965423, 15.799517, -0.411691], [5.965423, 15.466184, -0.411691], [6.046268, 15.466184, -0.735071]]}]},
			"C_neck_FK_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 20.246622, -0.010851], [-0.010851, 20.246622, 0.0], [0.0, 20.246622, 0.010851], [0.010851, 20.246622, 0.0], [0.0, 20.246622, -0.010851], [0.0, 20.257472, 0.0], [0.0, 20.246622, 0.010851], [0.0, 20.235771, 0.0], [-0.010851, 20.246622, 0.0], [0.0, 20.257472, 0.0], [0.010851, 20.246622, 0.0], [0.0, 20.235771, 0.0], [0.0, 20.246622, -0.010851], [0.0, 20.257472, 0.0], [0.0, 19.222951, 0.0]]}, {"shapeName": "C_neck_FK_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.023671, 19.222951, -0.010851], [-1.023671, 19.2121, 0.0], [-1.023671, 19.222951, 0.010851], [-1.023671, 19.233802, 0.0], [-1.023671, 19.222951, -0.010851], [-1.034521, 19.222951, 0.0], [-1.023671, 19.222951, 0.010851], [-1.01282, 19.222951, 0.0], [-1.023671, 19.2121, 0.0], [-1.034521, 19.222951, 0.0], [-1.023671, 19.233802, 0.0], [-1.01282, 19.222951, 0.0], [-1.023671, 19.222951, -0.010851], [-1.034521, 19.222951, 0.0], [0.0, 19.222951, 0.0]]}, {"shapeName": "C_neck_FK_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.010851, 19.222951, 1.023671], [0.0, 19.2121, 1.023671], [0.010851, 19.222951, 1.023671], [0.0, 19.233802, 1.023671], [-0.010851, 19.222951, 1.023671], [0.0, 19.222951, 1.034521], [0.010851, 19.222951, 1.023671], [0.0, 19.222951, 1.01282], [0.0, 19.2121, 1.023671], [0.0, 19.222951, 1.034521], [0.0, 19.233802, 1.023671], [0.0, 19.222951, 1.01282], [-0.010851, 19.222951, 1.023671], [0.0, 19.222951, 1.034521], [0.0, 19.222951, 0.0]]}]},
			"L_scapulaCtrl_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_scapulaCtrl_CTLShape", "degree": 1, "form": 0, "points": [[2.925, 15.799868, -1.5], [3.114449, 15.496779, -1.5], [3.388265, 15.299517, -1.5], [3.110832, 15.096469, -1.5], [2.925, 14.799166, -1.5], [2.738275, 15.097897, -1.5], [2.461735, 15.299517, -1.5], [2.738175, 15.500976, -1.5], [2.925, 15.799868, -1.5]]}]},
			"L_hand_CTL": {"color": 1, "shapes": [{"shapeName": "L_hand_CTLShape", "degree": 1, "form": 0, "points": [[7.225968, 16.283422, -0.0], [7.186992, 16.290352, -0.0], [7.146777, 16.291934, -0.0], [7.108662, 16.291052, -0.0], [7.070743, 16.291871, -0.0], [7.045305, 16.293796, -0.0], [7.025411, 16.30683, -0.0], [7.008821, 16.337168, -0.0], [6.991041, 16.376585, -0.0], [6.976838, 16.420573, -0.0], [6.963468, 16.482922, -0.0], [6.956825, 16.546104, -0.0], [6.953857, 16.595286, -0.0], [6.952968, 16.633961, -0.0], [6.948719, 16.658461, -0.0], [6.944225, 16.68847, -0.0], [6.935272, 16.721713, -0.0], [6.929651, 16.751428, -0.0], [6.923659, 16.775501, -0.0], [6.914636, 16.803844, -0.0], [6.90499, 16.840447, -0.0], [6.904808, 16.868769, -0.0], [6.916337, 16.891176, -0.0], [6.930064, 16.895558, -0.0], [6.948208, 16.887256, -0.0], [6.955068, 16.86571, -0.0], [6.963223, 16.83792, -0.0], [6.973996, 16.810634, -0.0], [6.984846, 16.782186, -0.0], [6.996144, 16.747683, -0.0], [7.009178, 16.719669, -0.0], [7.020756, 16.707895, -0.0], [7.026132, 16.706971, -0.0], [7.035071, 16.724387, -0.0], [7.036044, 16.749517, -0.0], [7.029541, 16.778525, -0.0], [7.025411, 16.79788, -0.0], [7.022436, 16.827196, -0.0], [7.020266, 16.853698, -0.0], [7.015695, 16.881516, -0.0], [7.012657, 16.905134, -0.0], [7.009654, 16.925224, -0.0], [7.003795, 16.954673, -0.0], [6.998867, 16.978004, -0.0], [6.996774, 17.000621, -0.0], [7.003627, 17.021495, -0.0], [7.017025, 17.035019, -0.0], [7.036604, 17.035719, -0.0], [7.053334, 17.025576, -0.0], [7.061811, 17.003183, -0.0], [7.067159, 16.976793, -0.0], [7.072374, 16.953406, -0.0], [7.078863, 16.925868, -0.0], [7.084722, 16.900325, -0.0], [7.08909, 16.875951, -0.0], [7.092436, 16.849617, -0.0], [7.099415, 16.818383, -0.0], [7.104574, 16.797131, -0.0], [7.108795, 16.772162, -0.0], [7.121682, 16.752695, -0.0], [7.130376, 16.765883, -0.0], [7.135542, 16.80054, -0.0], [7.13669, 16.826601, -0.0], [7.135871, 16.860355, -0.0], [7.137313, 16.890399, -0.0], [7.138972, 16.916789, -0.0], [7.139168, 16.947246, -0.0], [7.137656, 16.976135, -0.0], [7.137733, 17.017155, -0.0], [7.138846, 17.047045, -0.0], [7.142899, 17.072504, -0.0], [7.157851, 17.083312, -0.0], [7.177521, 17.089101, -0.0], [7.194937, 17.083221, -0.0], [7.203967, 17.064909, -0.0], [7.206319, 17.034739, -0.0], [7.208503, 17.004842, -0.0], [7.209707, 16.980027, -0.0], [7.207544, 16.947575, -0.0], [7.207215, 16.91779, -0.0], [7.211338, 16.885856, -0.0], [7.213956, 16.87019, -0.0], [7.213256, 16.849036, -0.0], [7.214327, 16.825362, -0.0], [7.216231, 16.79669, -0.0], [7.217918, 16.762439, -0.0], [7.222076, 16.754578, -0.0], [7.232226, 16.764056, -0.0], [7.237056, 16.787842, -0.0], [7.243853, 16.819174, -0.0], [7.252421, 16.856134, -0.0], [7.258182, 16.888292, -0.0], [7.264153, 16.916761, -0.0], [7.273148, 16.943305, -0.0], [7.282836, 16.974826, -0.0], [7.290466, 17.00753, -0.0], [7.298481, 17.032674, -0.0], [7.307637, 17.052491, -0.0], [7.322533, 17.067597, -0.0], [7.33388, 17.06514, -0.0], [7.3539, 17.052148, -0.0], [7.361138, 17.0223, -0.0], [7.356609, 16.992389, -0.0], [7.352976, 16.971872, -0.0], [7.349784, 16.946308, -0.0], [7.344919, 16.919162, -0.0], [7.335322, 16.889475, -0.0], [7.331129, 16.870582, -0.0], [7.329134, 16.836765, -0.0], [7.327951, 16.814834, -0.0], [7.323177, 16.78696, -0.0], [7.319012, 16.761795, -0.0], [7.317017, 16.733928, -0.0], [7.313573, 16.691837, -0.0], [7.317332, 16.63163, -0.0], [7.324612, 16.600704, -0.0], [7.336225, 16.58109, -0.0], [7.351037, 16.559852, -0.0], [7.363203, 16.585745, -0.0], [7.382663, 16.614669, -0.0], [7.392806, 16.635368, -0.0], [7.397496, 16.658874, -0.0], [7.409018, 16.682688, -0.0], [7.427848, 16.706789, -0.0], [7.452957, 16.724821, -0.0], [7.470716, 16.730211, -0.0], [7.487894, 16.719354, -0.0], [7.490939, 16.702246, -0.0], [7.486529, 16.673266, -0.0], [7.477191, 16.654618, -0.0], [7.475896, 16.63772, -0.0], [7.475266, 16.605233, -0.0], [7.465039, 16.585346, -0.0], [7.452544, 16.569316, -0.0], [7.449051, 16.553937, -0.0], [7.44637, 16.534169, -0.0], [7.434183, 16.502781, -0.0], [7.418594, 16.435133, -0.0], [7.399575, 16.401596, -0.0], [7.374858, 16.363656, -0.0], [7.350442, 16.330616, -0.0], [7.33122, 16.306242, -0.0], [7.296871, 16.287286, -0.0], [7.265427, 16.281245, -0.0], [7.226521, 16.283373, -0.0]]}]},
			"C_torso_FK_E_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_E_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 14.273434, -1.0], [0.0, 14.311702, -1.007612], [0.0, 14.344144, -1.02929], [0.0, 14.365822, -1.061732], [0.0, 14.373434, -1.1], [0.0, 14.365822, -1.138268], [0.0, 14.344144, -1.17071], [0.0, 14.311702, -1.192388], [0.0, 14.273434, -1.2], [0.0, 14.235166, -1.192388], [0.0, 14.202724, -1.17071], [0.0, 14.181046, -1.138268], [0.0, 14.173434, -1.1], [0.0, 14.181046, -1.061732], [0.0, 14.202724, -1.02929], [0.0, 14.235166, -1.007612], [0.0, 14.273434, -1.0], [0.0, 14.273434, 0.0]]}]},
			"L_scapulaChest_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_scapulaChest_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.948671, 15.299517, -0.010851], [1.948671, 15.310368, 0.0], [1.948671, 15.299517, 0.010851], [1.948671, 15.288666, 0.0], [1.948671, 15.299517, -0.010851], [1.959521, 15.299517, 0.0], [1.948671, 15.299517, 0.010851], [1.93782, 15.299517, 0.0], [1.948671, 15.310368, 0.0], [1.959521, 15.299517, 0.0], [1.948671, 15.288666, 0.0], [1.93782, 15.299517, 0.0], [1.948671, 15.299517, -0.010851], [1.959521, 15.299517, 0.0], [0.925, 15.299517, 0.0]]}, {"shapeName": "L_scapulaChest_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.925, 16.323188, -0.010851], [0.914149, 16.323188, 0.0], [0.925, 16.323188, 0.010851], [0.935851, 16.323188, 0.0], [0.925, 16.323188, -0.010851], [0.925, 16.334038, 0.0], [0.925, 16.323188, 0.010851], [0.925, 16.312337, 0.0], [0.914149, 16.323188, 0.0], [0.925, 16.334038, 0.0], [0.935851, 16.323188, 0.0], [0.925, 16.312337, 0.0], [0.925, 16.323188, -0.010851], [0.925, 16.334038, 0.0], [0.925, 15.299517, 0.0]]}, {"shapeName": "L_scapulaChest_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.925, 15.310368, 1.023671], [0.914149, 15.299517, 1.023671], [0.925, 15.288666, 1.023671], [0.935851, 15.299517, 1.023671], [0.925, 15.310368, 1.023671], [0.925, 15.299517, 1.034521], [0.925, 15.288666, 1.023671], [0.925, 15.299517, 1.01282], [0.914149, 15.299517, 1.023671], [0.925, 15.299517, 1.034521], [0.935851, 15.299517, 1.023671], [0.925, 15.299517, 1.01282], [0.925, 15.310368, 1.023671], [0.925, 15.299517, 1.034521], [0.925, 15.299517, 0.0]]}]},
			"C_neckBase_C_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.987351, 18.556285, -0.822793], [0.0, 18.136285, -1.163604], [-0.987351, 18.556285, -0.822793], [-1.396324, 18.976285, 0.0], [-0.987351, 18.556285, 0.822793], [0.0, 18.136285, 1.163604], [0.987351, 18.556285, 0.822793], [1.396324, 18.976285, 0.0]]}]},
			"C_head_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 21.579956, -0.010851], [-0.010851, 21.579956, 0.0], [0.0, 21.579956, 0.010851], [0.010851, 21.579956, 0.0], [0.0, 21.579956, -0.010851], [0.0, 21.590806, 0.0], [0.0, 21.579956, 0.010851], [0.0, 21.569105, 0.0], [-0.010851, 21.579956, 0.0], [0.0, 21.590806, 0.0], [0.010851, 21.579956, 0.0], [0.0, 21.569105, 0.0], [0.0, 21.579956, -0.010851], [0.0, 21.590806, 0.0], [0.0, 20.556285, 0.0]]}, {"shapeName": "C_head_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.023671, 20.556285, -0.010851], [-1.023671, 20.545434, 0.0], [-1.023671, 20.556285, 0.010851], [-1.023671, 20.567136, 0.0], [-1.023671, 20.556285, -0.010851], [-1.034521, 20.556285, 0.0], [-1.023671, 20.556285, 0.010851], [-1.01282, 20.556285, 0.0], [-1.023671, 20.545434, 0.0], [-1.034521, 20.556285, 0.0], [-1.023671, 20.567136, 0.0], [-1.01282, 20.556285, 0.0], [-1.023671, 20.556285, -0.010851], [-1.034521, 20.556285, 0.0], [0.0, 20.556285, 0.0]]}, {"shapeName": "C_head_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.010851, 20.556285, 1.023671], [0.0, 20.545434, 1.023671], [0.010851, 20.556285, 1.023671], [0.0, 20.567136, 1.023671], [-0.010851, 20.556285, 1.023671], [0.0, 20.556285, 1.034521], [0.010851, 20.556285, 1.023671], [0.0, 20.556285, 1.01282], [0.0, 20.545434, 1.023671], [0.0, 20.556285, 1.034521], [0.0, 20.567136, 1.023671], [0.0, 20.556285, 1.01282], [-0.010851, 20.556285, 1.023671], [0.0, 20.556285, 1.034521], [0.0, 20.556285, 0.0]]}]},
			"C_midNeck_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_CTLShape", "degree": 3, "form": 2, "points": [[1.410502, 19.556285, -1.175418], [0.0, 19.556285, -1.662291], [-1.410502, 19.556285, -1.175418], [-1.994749, 19.556285, 0.0], [-1.410502, 19.556285, 1.175418], [0.0, 19.556285, 1.662291], [1.410502, 19.556285, 1.175418], [1.994749, 19.556285, 0.0]]}]},
			"C_chest_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.269451, 15.273434, -1.057876], [0.0, 15.813434, -1.496062], [-1.269451, 15.273434, -1.057876], [-1.795274, 14.733434, 0.0], [-1.269451, 15.273434, 1.057876], [0.0, 15.813434, 1.496062], [1.269451, 15.273434, 1.057876], [1.795274, 14.733434, 0.0]]}]},
			"C_head_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.705251, 21.261536, 0.0], [0.0, 21.553659, 0.0], [-0.705251, 21.261536, 0.0], [-0.997375, 20.556285, 0.0], [-0.705251, 19.851034, 0.0], [0.0, 19.55891, 0.0], [0.705251, 19.851034, 0.0], [0.997375, 20.556285, 0.0]]}]},
			"L_reverseBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_reverseBall_CTLShape", "degree": 1, "form": 0, "points": [[1.00178, -0.088451, 1.0], [1.00178, 0.636549, 1.0], [1.00178, 0.736549, 0.9], [1.10178, 0.736549, 1.0], [1.00178, 0.836549, 1.0], [1.00178, 0.736549, 0.9], [0.90178, 0.736549, 1.0], [1.00178, 0.636549, 1.0], [1.00178, 0.736549, 1.1], [0.90178, 0.736549, 1.0], [1.00178, 0.836549, 1.0], [1.00178, 0.736549, 1.1], [1.10178, 0.736549, 1.0], [1.00178, 0.636549, 1.0]]}]},
			"L_loLeg_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_loLeg_FK_CTLShape", "degree": 1, "form": 0, "points": [[0.5, 5.080058, -0.058156], [0.5, 6.072336, 0.065878], [0.5, 5.948301, 1.058156], [0.5, 4.956023, 0.934122], [1.5, 4.956023, 0.934122], [1.5, 5.948301, 1.058156], [1.5, 6.072336, 0.065878], [1.5, 5.080058, -0.058156], [0.5, 5.080058, -0.058156], [0.5, 4.956023, 0.934122], [0.5, 5.948301, 1.058156], [1.5, 5.948301, 1.058156], [1.5, 4.956023, 0.934122], [1.5, 5.080058, -0.058156], [1.5, 6.072336, 0.065878], [0.5, 6.072336, 0.065878]]}]},
			"C_reverseJaw_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_reverseJaw_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.010851, 20.556285, 1.523671], [0.0, 20.567136, 1.523671], [-0.010851, 20.556285, 1.523671], [0.0, 20.545434, 1.523671], [0.010851, 20.556285, 1.523671], [0.0, 20.556285, 1.534521], [-0.010851, 20.556285, 1.523671], [0.0, 20.556285, 1.51282], [0.0, 20.567136, 1.523671], [0.0, 20.556285, 1.534521], [0.0, 20.545434, 1.523671], [0.0, 20.556285, 1.51282], [0.010851, 20.556285, 1.523671], [0.0, 20.556285, 1.534521], [0.0, 20.556285, 0.5]]}, {"shapeName": "C_reverseJaw_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.010851, 21.579956, 0.5], [0.0, 21.579956, 0.489149], [-0.010851, 21.579956, 0.5], [0.0, 21.579956, 0.510851], [0.010851, 21.579956, 0.5], [0.0, 21.590806, 0.5], [-0.010851, 21.579956, 0.5], [0.0, 21.569105, 0.5], [0.0, 21.579956, 0.489149], [0.0, 21.590806, 0.5], [0.0, 21.579956, 0.510851], [0.0, 21.569105, 0.5], [0.010851, 21.579956, 0.5], [0.0, 21.590806, 0.5], [0.0, 20.556285, 0.5]]}, {"shapeName": "C_reverseJaw_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.023671, 20.567136, 0.5], [-1.023671, 20.556285, 0.489149], [-1.023671, 20.545434, 0.5], [-1.023671, 20.556285, 0.510851], [-1.023671, 20.567136, 0.5], [-1.034521, 20.556285, 0.5], [-1.023671, 20.545434, 0.5], [-1.01282, 20.556285, 0.5], [-1.023671, 20.556285, 0.489149], [-1.034521, 20.556285, 0.5], [-1.023671, 20.556285, 0.510851], [-1.01282, 20.556285, 0.5], [-1.023671, 20.567136, 0.5], [-1.034521, 20.556285, 0.5], [0.0, 20.556285, 0.5]]}]},
			"L_wrist_IK_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_wrist_IK_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[6.925, 15.599517, -0.3], [6.925, 15.599517, 0.3], [6.925, 14.999517, 0.3], [6.925, 14.999517, -0.3], [6.925, 15.599517, -0.3]]}]},
			"L_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.314691, 15.214225, -0.510851], [9.316126, 15.22498, -0.5], [9.314691, 15.214225, -0.489149], [9.313257, 15.203469, -0.5], [9.314691, 15.214225, -0.510851], [9.325446, 15.212791, -0.5], [9.314691, 15.214225, -0.489149], [9.303936, 15.215659, -0.5], [9.316126, 15.22498, -0.5], [9.325446, 15.212791, -0.5], [9.313257, 15.203469, -0.5], [9.303936, 15.215659, -0.5], [9.314691, 15.214225, -0.510851], [9.325446, 15.212791, -0.5], [8.3, 15.349517, -0.5]]}, {"shapeName": "L_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[8.435292, 16.364208, -0.510851], [8.424537, 16.365642, -0.5], [8.435292, 16.364208, -0.489149], [8.446048, 16.362774, -0.5], [8.435292, 16.364208, -0.510851], [8.436726, 16.374963, -0.5], [8.435292, 16.364208, -0.489149], [8.433858, 16.353452, -0.5], [8.424537, 16.365642, -0.5], [8.436726, 16.374963, -0.5], [8.446048, 16.362774, -0.5], [8.433858, 16.353452, -0.5], [8.435292, 16.364208, -0.510851], [8.436726, 16.374963, -0.5], [8.3, 15.349517, -0.5]]}, {"shapeName": "L_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[8.301434, 15.360272, 0.523671], [8.289244, 15.350951, 0.523671], [8.298566, 15.338761, 0.523671], [8.310756, 15.348083, 0.523671], [8.301434, 15.360272, 0.523671], [8.3, 15.349517, 0.534521], [8.298566, 15.338761, 0.523671], [8.3, 15.349517, 0.51282], [8.289244, 15.350951, 0.523671], [8.3, 15.349517, 0.534521], [8.310756, 15.348083, 0.523671], [8.3, 15.349517, 0.51282], [8.301434, 15.360272, 0.523671], [8.3, 15.349517, 0.534521], [8.3, 15.349517, -0.5]]}]},
			"C_neckBase_B_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.128401, 18.556285, -0.940334], [0.0, 18.076285, -1.329833], [-1.128401, 18.556285, -0.940334], [-1.595799, 19.036285, 0.0], [-1.128401, 18.556285, 0.940334], [0.0, 18.076285, 1.329833], [1.128401, 18.556285, 0.940334], [1.595799, 19.036285, 0.0]]}]},
			"L_arm_IK_switch_B_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "L_arm_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[6.868774, 16.143714, -0.0], [6.905494, 16.170325, -0.0], [6.870183, 16.193885, -0.0], [6.870183, 16.253327, -0.0], [6.907179, 16.247095, -0.0], [6.850128, 16.348621, -0.0], [6.796192, 16.247095, -0.0], [6.833188, 16.253327, -0.0], [6.833188, 16.167468, -0.0], [6.868774, 16.143714, -0.0]]}, {"shapeName": "L_arm_IK_switch_B_OFF_CTLShape1", "degree": 1, "form": 0, "points": [[6.925, 15.299517, -0.0], [6.925, 16.108316, -0.0], [7.016812, 16.090449, -0.0], [7.016812, 16.006056, -0.0], [7.053808, 16.012287, -0.0], [6.999872, 15.910761, -0.0], [6.942821, 16.012287, -0.0], [6.979817, 16.006056, -0.0], [6.979817, 16.064033, -0.0], [6.927983, 16.070046, -0.0]]}, {"shapeName": "L_arm_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[6.850128, 15.910761, -0.0], [6.907179, 16.012287, -0.0], [6.870183, 16.006056, -0.0], [6.870183, 16.065497, -0.0], [7.016812, 16.168933, -0.0], [7.016812, 16.253327, -0.0], [7.053808, 16.247095, -0.0], [6.999872, 16.348621, -0.0], [6.942821, 16.247095, -0.0], [6.979817, 16.253327, -0.0], [6.979817, 16.195349, -0.0], [6.833188, 16.091914, -0.0], [6.833188, 16.006056, -0.0], [6.796192, 16.012287, -0.0], [6.850128, 15.910761, -0.0]]}]},
			"L_arm_IK_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_arm_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.925, 15.11145, -0.188067], [6.925, 15.299517, -0.265967], [6.925, 15.487584, -0.188067], [6.925, 15.565483, -0.0], [6.925, 15.487584, 0.188067], [6.925, 15.299517, 0.265967], [6.925, 15.11145, 0.188067], [6.925, 15.03355, -0.0]]}]},
			"L_scapulaTarget_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_scapulaTarget_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.948671, 15.299517, -2.010851], [1.948671, 15.310368, -2.0], [1.948671, 15.299517, -1.989149], [1.948671, 15.288666, -2.0], [1.948671, 15.299517, -2.010851], [1.959521, 15.299517, -2.0], [1.948671, 15.299517, -1.989149], [1.93782, 15.299517, -2.0], [1.948671, 15.310368, -2.0], [1.959521, 15.299517, -2.0], [1.948671, 15.288666, -2.0], [1.93782, 15.299517, -2.0], [1.948671, 15.299517, -2.010851], [1.959521, 15.299517, -2.0], [0.925, 15.299517, -2.0]]}, {"shapeName": "L_scapulaTarget_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.925, 16.323188, -2.010851], [0.914149, 16.323188, -2.0], [0.925, 16.323188, -1.989149], [0.935851, 16.323188, -2.0], [0.925, 16.323188, -2.010851], [0.925, 16.334038, -2.0], [0.925, 16.323188, -1.989149], [0.925, 16.312337, -2.0], [0.914149, 16.323188, -2.0], [0.925, 16.334038, -2.0], [0.935851, 16.323188, -2.0], [0.925, 16.312337, -2.0], [0.925, 16.323188, -2.010851], [0.925, 16.334038, -2.0], [0.925, 15.299517, -2.0]]}, {"shapeName": "L_scapulaTarget_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.925, 15.310368, -0.976329], [0.914149, 15.299517, -0.976329], [0.925, 15.288666, -0.976329], [0.935851, 15.299517, -0.976329], [0.925, 15.310368, -0.976329], [0.925, 15.299517, -0.965479], [0.925, 15.288666, -0.976329], [0.925, 15.299517, -0.98718], [0.914149, 15.299517, -0.976329], [0.925, 15.299517, -0.965479], [0.935851, 15.299517, -0.976329], [0.925, 15.299517, -0.98718], [0.925, 15.310368, -0.976329], [0.925, 15.299517, -0.965479], [0.925, 15.299517, -2.0]]}]},
			"C_midTorso_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_CTLShape", "degree": 3, "form": 2, "points": [[1.410502, 12.773434, -1.175418], [0.0, 12.773434, -1.662291], [-1.410502, 12.773434, -1.175418], [-1.994749, 12.773434, 0.0], [-1.410502, 12.773434, 1.175418], [0.0, 12.773434, 1.662291], [1.410502, 12.773434, 1.175418], [1.994749, 12.773434, 0.0]]}]},
			"L_upLeg_shaper_A_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_A_CTLShape", "degree": 1, "form": 0, "points": [[2.5, 8.714179, 0.1], [2.511418, 8.638234, 0.109493], [2.543935, 8.573851, 0.117541], [2.592598, 8.53083, 0.122919], [2.65, 8.515724, 0.124807], [2.707402, 8.53083, 0.122919], [2.756065, 8.573851, 0.117541], [2.788582, 8.638234, 0.109493], [2.8, 8.714179, 0.1], [2.788582, 8.790124, 0.090507], [2.756065, 8.854507, 0.082459], [2.707402, 8.897528, 0.077081], [2.65, 8.912635, 0.075193], [2.592598, 8.897528, 0.077081], [2.543935, 8.854507, 0.082459], [2.511418, 8.790124, 0.090507], [2.5, 8.714179, 0.1], [1.0, 8.714179, 0.1]]}]},
			"L_loArm_shaper_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loArm_shaper_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.320739, 15.299517, -0.16225], [6.318107, 15.310368, -0.151723], [6.315475, 15.299517, -0.141196], [6.318107, 15.288666, -0.151723], [6.320739, 15.299517, -0.16225], [6.328633, 15.299517, -0.149092], [6.315475, 15.299517, -0.141196], [6.30758, 15.299517, -0.154355], [6.318107, 15.310368, -0.151723], [6.328633, 15.299517, -0.149092], [6.318107, 15.288666, -0.151723], [6.30758, 15.299517, -0.154355], [6.320739, 15.299517, -0.16225], [6.328633, 15.299517, -0.149092], [5.325, 15.299517, -0.4]]}, {"shapeName": "L_loArm_shaper_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[5.327632, 16.323188, -0.410527], [5.314473, 16.323188, -0.402632], [5.322368, 16.323188, -0.389473], [5.335527, 16.323188, -0.397368], [5.327632, 16.323188, -0.410527], [5.325, 16.334038, -0.4], [5.322368, 16.323188, -0.389473], [5.325, 16.312337, -0.4], [5.314473, 16.323188, -0.402632], [5.325, 16.334038, -0.4], [5.335527, 16.323188, -0.397368], [5.325, 16.312337, -0.4], [5.327632, 16.323188, -0.410527], [5.325, 16.334038, -0.4], [5.325, 15.299517, -0.4]]}, {"shapeName": "L_loArm_shaper_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[5.076723, 15.310368, 0.593107], [5.066196, 15.299517, 0.590475], [5.076723, 15.288666, 0.593107], [5.08725, 15.299517, 0.595738], [5.076723, 15.310368, 0.593107], [5.074092, 15.299517, 0.603633], [5.076723, 15.288666, 0.593107], [5.079355, 15.299517, 0.58258], [5.066196, 15.299517, 0.590475], [5.074092, 15.299517, 0.603633], [5.08725, 15.299517, 0.595738], [5.079355, 15.299517, 0.58258], [5.076723, 15.310368, 0.593107], [5.074092, 15.299517, 0.603633], [5.325, 15.299517, -0.4]]}]},
			"L_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_D_CTLShape", "degree": 3, "form": 2, "points": [[8.284465, 15.233006, -0.367542], [8.3, 15.349517, -0.416229], [8.315535, 15.466027, -0.367542], [8.32197, 15.514288, -0.25], [8.315535, 15.466027, -0.132458], [8.3, 15.349517, -0.083771], [8.284465, 15.233006, -0.132458], [8.278031, 15.184746, -0.25]]}]},
			"C_torso_FK_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 13.297105, -0.010851], [-0.010851, 13.297105, 0.0], [0.0, 13.297105, 0.010851], [0.010851, 13.297105, 0.0], [0.0, 13.297105, -0.010851], [0.0, 13.307955, 0.0], [0.0, 13.297105, 0.010851], [0.0, 13.286254, 0.0], [-0.010851, 13.297105, 0.0], [0.0, 13.307955, 0.0], [0.010851, 13.297105, 0.0], [0.0, 13.286254, 0.0], [0.0, 13.297105, -0.010851], [0.0, 13.307955, 0.0], [0.0, 12.273434, 0.0]]}, {"shapeName": "C_torso_FK_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.023671, 12.273434, -0.010851], [-1.023671, 12.262583, 0.0], [-1.023671, 12.273434, 0.010851], [-1.023671, 12.284285, 0.0], [-1.023671, 12.273434, -0.010851], [-1.034521, 12.273434, 0.0], [-1.023671, 12.273434, 0.010851], [-1.01282, 12.273434, 0.0], [-1.023671, 12.262583, 0.0], [-1.034521, 12.273434, 0.0], [-1.023671, 12.284285, 0.0], [-1.01282, 12.273434, 0.0], [-1.023671, 12.273434, -0.010851], [-1.034521, 12.273434, 0.0], [0.0, 12.273434, 0.0]]}, {"shapeName": "C_torso_FK_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.010851, 12.273434, 1.023671], [0.0, 12.262583, 1.023671], [0.010851, 12.273434, 1.023671], [0.0, 12.284285, 1.023671], [-0.010851, 12.273434, 1.023671], [0.0, 12.273434, 1.034521], [0.010851, 12.273434, 1.023671], [0.0, 12.273434, 1.01282], [0.0, 12.262583, 1.023671], [0.0, 12.273434, 1.034521], [0.0, 12.284285, 1.023671], [0.0, 12.273434, 1.01282], [-0.010851, 12.273434, 1.023671], [0.0, 12.273434, 1.034521], [0.0, 12.273434, 0.0]]}]},
			"L_bendyArm_A_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[3.852239, 15.399517, -0.541043], [3.852239, 15.459517, -0.541043], [3.815859, 15.299517, -0.686564], [3.852239, 15.139516, -0.541043], [3.852239, 15.199516, -0.541043], [3.900746, 15.199516, -0.347014], [3.900746, 14.999517, -0.347014], [3.886194, 14.999517, -0.405223], [3.925, 14.849517, -0.25], [3.963806, 14.999517, -0.094777], [3.949254, 14.999517, -0.152986], [3.949254, 15.199516, -0.152986], [3.997761, 15.199516, 0.041043], [3.997761, 15.139516, 0.041043], [4.034141, 15.299517, 0.186564], [3.997761, 15.459517, 0.041043], [3.997761, 15.399517, 0.041043], [3.949254, 15.399517, -0.152986], [3.949254, 15.599517, -0.152986], [3.963806, 15.599517, -0.094777], [3.925, 15.749517, -0.25], [3.886194, 15.599517, -0.405223], [3.900746, 15.599517, -0.347014], [3.900746, 15.399517, -0.347014], [3.852239, 15.399517, -0.541043]]}]},
			"L_leg_PV_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_PV_CTLShape", "degree": 1, "form": 0, "points": [[0.9, 5.614179, 10.6], [0.9, 5.414179, 10.6], [0.9, 5.414179, 10.4], [0.9, 5.614179, 10.4], [1.1, 5.614179, 10.4], [1.1, 5.414179, 10.4], [1.1, 5.414179, 10.6], [1.1, 5.614179, 10.6], [0.9, 5.614179, 10.6], [0.9, 5.614179, 10.4], [0.9, 5.414179, 10.4], [1.1, 5.414179, 10.4], [1.1, 5.614179, 10.4], [1.1, 5.614179, 10.6], [1.1, 5.414179, 10.6], [0.9, 5.414179, 10.6]]}]},
			"L_loArm_shaper_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loArm_shaper_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[7.120739, 15.299517, 0.03775], [7.118107, 15.310368, 0.048277], [7.115475, 15.299517, 0.058804], [7.118107, 15.288666, 0.048277], [7.120739, 15.299517, 0.03775], [7.128633, 15.299517, 0.050908], [7.115475, 15.299517, 0.058804], [7.10758, 15.299517, 0.045645], [7.118107, 15.310368, 0.048277], [7.128633, 15.299517, 0.050908], [7.118107, 15.288666, 0.048277], [7.10758, 15.299517, 0.045645], [7.120739, 15.299517, 0.03775], [7.128633, 15.299517, 0.050908], [6.125, 15.299517, -0.2]]}, {"shapeName": "L_loArm_shaper_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[6.127632, 16.323188, -0.210527], [6.114473, 16.323188, -0.202632], [6.122368, 16.323188, -0.189473], [6.135527, 16.323188, -0.197368], [6.127632, 16.323188, -0.210527], [6.125, 16.334038, -0.2], [6.122368, 16.323188, -0.189473], [6.125, 16.312337, -0.2], [6.114473, 16.323188, -0.202632], [6.125, 16.334038, -0.2], [6.135527, 16.323188, -0.197368], [6.125, 16.312337, -0.2], [6.127632, 16.323188, -0.210527], [6.125, 16.334038, -0.2], [6.125, 15.299517, -0.2]]}, {"shapeName": "L_loArm_shaper_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[5.876723, 15.310368, 0.793107], [5.866196, 15.299517, 0.790475], [5.876723, 15.288666, 0.793107], [5.88725, 15.299517, 0.795738], [5.876723, 15.310368, 0.793107], [5.874092, 15.299517, 0.803633], [5.876723, 15.288666, 0.793107], [5.879355, 15.299517, 0.78258], [5.866196, 15.299517, 0.790475], [5.874092, 15.299517, 0.803633], [5.88725, 15.299517, 0.795738], [5.879355, 15.299517, 0.78258], [5.876723, 15.310368, 0.793107], [5.874092, 15.299517, 0.803633], [6.125, 15.299517, -0.2]]}]},
			"C_neckBase_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_CTLShape", "degree": 3, "form": 2, "points": [[1.410502, 18.556285, -1.175418], [0.0, 17.956285, -1.662291], [-1.410502, 18.556285, -1.175418], [-1.994749, 19.156285, 0.0], [-1.410502, 18.556285, 1.175418], [0.0, 17.956285, 1.662291], [1.410502, 18.556285, 1.175418], [1.994749, 19.156285, 0.0]]}]},
			"C_midNeck_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.269451, 19.556285, -1.057876], [0.0, 19.556285, -1.496062], [-1.269451, 19.556285, -1.057876], [-1.795274, 19.556285, 0.0], [-1.269451, 19.556285, 1.057876], [0.0, 19.556285, 1.496062], [1.269451, 19.556285, 1.057876], [1.795274, 19.556285, 0.0]]}]},
			"L_arm_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.925, 16.323188, -0.010851], [6.914149, 16.323188, -0.0], [6.925, 16.323188, 0.010851], [6.935851, 16.323188, -0.0], [6.925, 16.323188, -0.010851], [6.925, 16.334038, -0.0], [6.925, 16.323188, 0.010851], [6.925, 16.312337, -0.0], [6.914149, 16.323188, -0.0], [6.925, 16.334038, -0.0], [6.935851, 16.323188, -0.0], [6.925, 16.312337, -0.0], [6.925, 16.323188, -0.010851], [6.925, 16.334038, -0.0], [6.925, 15.299517, -0.0]]}, {"shapeName": "L_arm_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[5.901329, 15.299517, -0.010851], [5.901329, 15.288666, -0.0], [5.901329, 15.299517, 0.010851], [5.901329, 15.310368, -0.0], [5.901329, 15.299517, -0.010851], [5.890479, 15.299517, -0.0], [5.901329, 15.299517, 0.010851], [5.91218, 15.299517, -0.0], [5.901329, 15.288666, -0.0], [5.890479, 15.299517, -0.0], [5.901329, 15.310368, -0.0], [5.91218, 15.299517, -0.0], [5.901329, 15.299517, -0.010851], [5.890479, 15.299517, -0.0], [6.925, 15.299517, -0.0]]}, {"shapeName": "L_arm_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[6.914149, 15.299517, 1.023671], [6.925, 15.288666, 1.023671], [6.935851, 15.299517, 1.023671], [6.925, 15.310368, 1.023671], [6.914149, 15.299517, 1.023671], [6.925, 15.299517, 1.034521], [6.935851, 15.299517, 1.023671], [6.925, 15.299517, 1.01282], [6.925, 15.288666, 1.023671], [6.925, 15.299517, 1.034521], [6.925, 15.310368, 1.023671], [6.925, 15.299517, 1.01282], [6.914149, 15.299517, 1.023671], [6.925, 15.299517, 1.034521], [6.925, 15.299517, -0.0]]}]},
			"L_toe_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.236864, 0.421633, 1.0], [1.00178, 0.519007, 1.0], [0.766697, 0.421633, 1.0], [0.669322, 0.186549, 1.0], [0.766697, -0.048535, 1.0], [1.00178, -0.145909, 1.0], [1.236864, -0.048535, 1.0], [1.334238, 0.186549, 1.0]]}]},
			"C_torso_FK_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_A_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 10.273434, -1.0], [0.0, 10.311702, -1.007612], [0.0, 10.344144, -1.02929], [0.0, 10.365822, -1.061732], [0.0, 10.373434, -1.1], [0.0, 10.365822, -1.138268], [0.0, 10.344144, -1.17071], [0.0, 10.311702, -1.192388], [0.0, 10.273434, -1.2], [0.0, 10.235166, -1.192388], [0.0, 10.202724, -1.17071], [0.0, 10.181046, -1.138268], [0.0, 10.173434, -1.1], [0.0, 10.181046, -1.061732], [0.0, 10.202724, -1.02929], [0.0, 10.235166, -1.007612], [0.0, 10.273434, -1.0], [0.0, 10.273434, 0.0]]}]},
			"L_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[7.988676, 15.38484, 1.115363], [7.979923, 15.380808, 1.127305], [7.983251, 15.366045, 1.12476], [7.992004, 15.370077, 1.112818], [7.988676, 15.38484, 1.115363], [7.994559, 15.376247, 1.126634], [7.983251, 15.366045, 1.12476], [7.977367, 15.374638, 1.113489], [7.979923, 15.380808, 1.127305], [7.994559, 15.376247, 1.126634], [7.992004, 15.370077, 1.112818], [7.977367, 15.374638, 1.113489], [7.988676, 15.38484, 1.115363], [7.994559, 15.376247, 1.126634], [7.175, 15.299517, 0.5]]}, {"shapeName": "L_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[6.607847, 15.815087, 1.178635], [6.596538, 15.804885, 1.17676], [6.602421, 15.796292, 1.188032], [6.61373, 15.806494, 1.189906], [6.607847, 15.815087, 1.178635], [6.599094, 15.811054, 1.190576], [6.602421, 15.796292, 1.188032], [6.611175, 15.800324, 1.17609], [6.596538, 15.804885, 1.17676], [6.599094, 15.811054, 1.190576], [6.61373, 15.806494, 1.189906], [6.611175, 15.800324, 1.17609], [6.607847, 15.815087, 1.178635], [6.599094, 15.811054, 1.190576], [7.175, 15.299517, 0.5]]}, {"shapeName": "L_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[6.913042, 14.418357, 0.950506], [6.910486, 14.412187, 0.93669], [6.925123, 14.407626, 0.936019], [6.927679, 14.413796, 0.949835], [6.913042, 14.418357, 0.950506], [6.91637, 14.403595, 0.947961], [6.925123, 14.407626, 0.936019], [6.921795, 14.422389, 0.938564], [6.910486, 14.412187, 0.93669], [6.91637, 14.403595, 0.947961], [6.927679, 14.413796, 0.949835], [6.921795, 14.422389, 0.938564], [6.913042, 14.418357, 0.950506], [6.91637, 14.403595, 0.947961], [7.175, 15.299517, 0.5]]}]},
			"L_leg_IK_switch_D_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "L_leg_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.899445, 1.388647, -0.015692], [2.959318, 1.470631, -0.005444], [3.012328, 1.391794, -0.015298], [3.146073, 1.391794, -0.015298], [3.132051, 1.474392, -0.004973], [3.360486, 1.347018, -0.020895], [3.132051, 1.226599, -0.035947], [3.146073, 1.309197, -0.025623], [2.95289, 1.309197, -0.025623], [2.899445, 1.388647, -0.015692]]}, {"shapeName": "L_leg_IK_switch_D_OFF_CTLShape1", "degree": 1, "form": 0, "points": [[1.0, 1.514179, 0.0], [2.819798, 1.514179, 0.0], [2.779599, 1.719161, 0.025623], [2.589713, 1.719161, 0.025623], [2.603733, 1.801759, 0.035947], [2.375299, 1.68134, 0.020895], [2.603733, 1.553966, 0.004973], [2.589713, 1.636565, 0.015298], [2.720161, 1.636565, 0.015298], [2.733692, 1.52084, 0.000833]]}, {"shapeName": "L_leg_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[2.375299, 1.347018, -0.020895], [2.603733, 1.474392, -0.004973], [2.589713, 1.391794, -0.015298], [2.723457, 1.391794, -0.015298], [2.956186, 1.719161, 0.025623], [3.146073, 1.719161, 0.025623], [3.132051, 1.801759, 0.035947], [3.360486, 1.68134, 0.020895], [3.132051, 1.553966, 0.004973], [3.146073, 1.636565, 0.015298], [3.015624, 1.636565, 0.015298], [2.782895, 1.309197, -0.025623], [2.589713, 1.309197, -0.025623], [2.603733, 1.226599, -0.035947], [2.375299, 1.347018, -0.020895]]}]},
			"L_arm_IK_CTL": {"color": 6, "shapes": [{"shapeName": "L_arm_IK_CTLShape", "degree": 3, "form": 2, "points": [[6.925, 14.986072, -0.313445], [6.925, 15.299517, -0.443278], [6.925, 15.612961, -0.313445], [6.925, 15.742794, -0.0], [6.925, 15.612961, 0.313445], [6.925, 15.299517, 0.443278], [6.925, 14.986072, 0.313445], [6.925, 14.856239, -0.0]]}]},
			"L_legBase_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.317692, 0.024561], [1.0, 8.999769, 0.064301], [1.0, 8.878334, 0.079481], [1.0, 9.093204, 0.811782], [1.0, 9.468873, 1.23401], [1.0, 9.861848, 1.184888], [1.0, 10.122024, 0.683179], [1.0, 10.150025, -0.079481], [1.0, 10.028589, -0.064301], [1.0, 9.710667, -0.024561], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0]]}]},
			"L_outterBall_CTL": {"color": 20, "shapes": [{"shapeName": "L_outterBall_CTLShape", "degree": 1, "form": 0, "points": [[1.70178, 0.186549, 1.1], [1.70178, 0.086549, 1.0], [1.80178, 0.186549, 1.0], [1.70178, 0.186549, 1.1], [1.60178, 0.186549, 1.0], [1.70178, 0.086549, 1.0], [1.70178, 0.186549, 0.9], [1.60178, 0.186549, 1.0], [1.70178, 0.286549, 1.0], [1.70178, 0.186549, 1.1], [1.80178, 0.186549, 1.0], [1.70178, 0.186549, 0.9], [1.70178, 0.286549, 1.0], [1.80178, 0.186549, 1.0]]}]},
			"L_bendyArm_C_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[5.997761, 15.399517, -0.541043], [5.997761, 15.459517, -0.541043], [6.034141, 15.299517, -0.686564], [5.997761, 15.139516, -0.541043], [5.997761, 15.199516, -0.541043], [5.949254, 15.199516, -0.347014], [5.949254, 14.999517, -0.347014], [5.963806, 14.999517, -0.405223], [5.925, 14.849517, -0.25], [5.886194, 14.999517, -0.094777], [5.900746, 14.999517, -0.152986], [5.900746, 15.199516, -0.152986], [5.852239, 15.199516, 0.041043], [5.852239, 15.139516, 0.041043], [5.815859, 15.299517, 0.186564], [5.852239, 15.459517, 0.041043], [5.852239, 15.399517, 0.041043], [5.900746, 15.399517, -0.152986], [5.900746, 15.599517, -0.152986], [5.886194, 15.599517, -0.094777], [5.925, 15.749517, -0.25], [5.963806, 15.599517, -0.405223], [5.949254, 15.599517, -0.347014], [5.949254, 15.399517, -0.347014], [5.997761, 15.399517, -0.541043]]}]},
			"C_midTorso_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.846301, 12.773434, -0.705251], [0.0, 12.773434, -0.997375], [-0.846301, 12.773434, -0.705251], [-1.19685, 12.773434, 0.0], [-0.846301, 12.773434, 0.705251], [0.0, 12.773434, 0.997375], [0.846301, 12.773434, 0.705251], [1.19685, 12.773434, 0.0]]}]},
			"L_toe_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.276044, 0.460813, 1.0], [1.00178, 0.574417, 1.0], [0.727516, 0.460813, 1.0], [0.613912, 0.186549, 1.0], [0.727516, -0.087715, 1.0], [1.00178, -0.201319, 1.0], [1.276044, -0.087715, 1.0], [1.389648, 0.186549, 1.0]]}]},
			"L_loArm_shaper_B_CTL": {"color": 4, "shapes": [{"shapeName": "L_loArm_shaper_B_CTLShape", "degree": 1, "form": 0, "points": [[5.725, 16.799517, -0.3], [5.799251, 16.810935, -0.281437], [5.862198, 16.843452, -0.265701], [5.904259, 16.892115, -0.255185], [5.919029, 16.949517, -0.251493], [5.904259, 17.006919, -0.255185], [5.862198, 17.055582, -0.265701], [5.799251, 17.088099, -0.281437], [5.725, 17.099517, -0.3], [5.650749, 17.088099, -0.318563], [5.587802, 17.055582, -0.334299], [5.545741, 17.006919, -0.344815], [5.530972, 16.949517, -0.348507], [5.545741, 16.892115, -0.344815], [5.587802, 16.843452, -0.334299], [5.650749, 16.810935, -0.318563], [5.725, 16.799517, -0.3], [5.725, 15.299517, -0.3]]}]},
			"C_cog_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.115752, 9.773434, -2.115752], [0.0, 9.773434, -2.992124], [-2.115752, 9.773434, -2.115752], [-2.992124, 9.773434, 0.0], [-2.115752, 9.773434, 2.115752], [0.0, 9.773434, 2.992124], [2.115752, 9.773434, 2.115752], [2.992124, 9.773434, 0.0]]}]},
			"L_arm_IK_switch_D_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "L_arm_IK_switch_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[6.88283, 15.932665, -0.0], [6.910371, 15.952623, -0.0], [6.883887, 15.970293, -0.0], [6.883887, 16.014874, -0.0], [6.911634, 16.0102, -0.0], [6.868846, 16.086345, -0.0], [6.828394, 16.0102, -0.0], [6.856141, 16.014874, -0.0], [6.856141, 15.95048, -0.0], [6.88283, 15.932665, -0.0]]}, {"shapeName": "L_arm_IK_switch_D_OFF_CTLShape1", "degree": 1, "form": 0, "points": [[6.925, 15.299517, -0.0], [6.925, 15.906116, -0.0], [6.993859, 15.892716, -0.0], [6.993859, 15.829421, -0.0], [7.021606, 15.834094, -0.0], [6.981154, 15.75795, -0.0], [6.938366, 15.834094, -0.0], [6.966113, 15.829421, -0.0], [6.966113, 15.872904, -0.0], [6.927237, 15.877414, -0.0]]}, {"shapeName": "L_arm_IK_switch_D_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[6.868846, 15.75795, -0.0], [6.911634, 15.834094, -0.0], [6.883887, 15.829421, -0.0], [6.883887, 15.874002, -0.0], [6.993859, 15.951579, -0.0], [6.993859, 16.014874, -0.0], [7.021606, 16.0102, -0.0], [6.981154, 16.086345, -0.0], [6.938366, 16.0102, -0.0], [6.966113, 16.014874, -0.0], [6.966113, 15.971391, -0.0], [6.856141, 15.893815, -0.0], [6.856141, 15.829421, -0.0], [6.828394, 15.834094, -0.0], [6.868846, 15.75795, -0.0]]}]},
			"C_hip_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.269451, 9.773434, -1.057876], [0.0, 9.233434, -1.496062], [-1.269451, 9.773434, -1.057876], [-1.795274, 10.313434, 0.0], [-1.269451, 9.773434, 1.057876], [0.0, 9.233434, 1.496062], [1.269451, 9.773434, 1.057876], [1.795274, 10.313434, 0.0]]}]},
			"L_bendyArm_B_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.925, 15.416184, -0.85], [4.925, 15.486184, -0.85], [4.925, 15.299517, -1.025], [4.925, 15.11285, -0.85], [4.925, 15.18285, -0.85], [4.925, 15.18285, -0.616667], [4.925, 14.949517, -0.616667], [4.925, 14.949517, -0.686667], [4.925, 14.774517, -0.5], [4.925, 14.949517, -0.313333], [4.925, 14.949517, -0.383333], [4.925, 15.18285, -0.383333], [4.925, 15.18285, -0.15], [4.925, 15.11285, -0.15], [4.925, 15.299517, 0.025], [4.925, 15.486184, -0.15], [4.925, 15.416184, -0.15], [4.925, 15.416184, -0.383333], [4.925, 15.649517, -0.383333], [4.925, 15.649517, -0.313333], [4.925, 15.824517, -0.5], [4.925, 15.649517, -0.686667], [4.925, 15.649517, -0.616667], [4.925, 15.416184, -0.616667], [4.925, 15.416184, -0.85]]}]},
			"L_leg_IK_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.352625, 1.514179, -0.587709], [1.0, 1.514179, -0.831145], [0.647375, 1.514179, -0.587709], [0.501313, 1.514179, 0.0], [0.647375, 1.514179, 0.587709], [1.0, 1.514179, 0.831145], [1.352625, 1.514179, 0.587709], [1.498687, 1.514179, 0.0]]}]},
			"L_loArm_shaper_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loArm_shaper_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[7.520739, 15.299517, 0.13775], [7.518107, 15.310368, 0.148277], [7.515475, 15.299517, 0.158804], [7.518107, 15.288666, 0.148277], [7.520739, 15.299517, 0.13775], [7.528633, 15.299517, 0.150908], [7.515475, 15.299517, 0.158804], [7.50758, 15.299517, 0.145645], [7.518107, 15.310368, 0.148277], [7.528633, 15.299517, 0.150908], [7.518107, 15.288666, 0.148277], [7.50758, 15.299517, 0.145645], [7.520739, 15.299517, 0.13775], [7.528633, 15.299517, 0.150908], [6.525, 15.299517, -0.1]]}, {"shapeName": "L_loArm_shaper_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[6.527632, 16.323188, -0.110527], [6.514473, 16.323188, -0.102632], [6.522368, 16.323188, -0.089473], [6.535527, 16.323188, -0.097368], [6.527632, 16.323188, -0.110527], [6.525, 16.334038, -0.1], [6.522368, 16.323188, -0.089473], [6.525, 16.312337, -0.1], [6.514473, 16.323188, -0.102632], [6.525, 16.334038, -0.1], [6.535527, 16.323188, -0.097368], [6.525, 16.312337, -0.1], [6.527632, 16.323188, -0.110527], [6.525, 16.334038, -0.1], [6.525, 15.299517, -0.1]]}, {"shapeName": "L_loArm_shaper_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[6.276723, 15.310368, 0.893107], [6.266196, 15.299517, 0.890475], [6.276723, 15.288666, 0.893107], [6.28725, 15.299517, 0.895738], [6.276723, 15.310368, 0.893107], [6.274092, 15.299517, 0.903633], [6.276723, 15.288666, 0.893107], [6.279355, 15.299517, 0.88258], [6.266196, 15.299517, 0.890475], [6.274092, 15.299517, 0.903633], [6.28725, 15.299517, 0.895738], [6.279355, 15.299517, 0.88258], [6.276723, 15.310368, 0.893107], [6.274092, 15.299517, 0.903633], [6.525, 15.299517, -0.1]]}]},
			"C_chest_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_chest_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.987351, 15.273434, -0.822793], [0.0, 15.693434, -1.163604], [-0.987351, 15.273434, -0.822793], [-1.396324, 14.853434, 0.0], [-0.987351, 15.273434, 0.822793], [0.0, 15.693434, 1.163604], [0.987351, 15.273434, 0.822793], [1.396324, 14.853434, 0.0]]}]},
			"C_chest_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_chest_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 16.297105, -0.010851], [-0.010851, 16.297105, 0.0], [0.0, 16.297105, 0.010851], [0.010851, 16.297105, 0.0], [0.0, 16.297105, -0.010851], [0.0, 16.307955, 0.0], [0.0, 16.297105, 0.010851], [0.0, 16.286254, 0.0], [-0.010851, 16.297105, 0.0], [0.0, 16.307955, 0.0], [0.010851, 16.297105, 0.0], [0.0, 16.286254, 0.0], [0.0, 16.297105, -0.010851], [0.0, 16.307955, 0.0], [0.0, 15.273434, 0.0]]}, {"shapeName": "C_chest_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.023671, 15.273434, -0.010851], [-1.023671, 15.262583, 0.0], [-1.023671, 15.273434, 0.010851], [-1.023671, 15.284285, 0.0], [-1.023671, 15.273434, -0.010851], [-1.034521, 15.273434, 0.0], [-1.023671, 15.273434, 0.010851], [-1.01282, 15.273434, 0.0], [-1.023671, 15.262583, 0.0], [-1.034521, 15.273434, 0.0], [-1.023671, 15.284285, 0.0], [-1.01282, 15.273434, 0.0], [-1.023671, 15.273434, -0.010851], [-1.034521, 15.273434, 0.0], [0.0, 15.273434, 0.0]]}, {"shapeName": "C_chest_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.010851, 15.273434, 1.023671], [0.0, 15.262583, 1.023671], [0.010851, 15.273434, 1.023671], [0.0, 15.284285, 1.023671], [-0.010851, 15.273434, 1.023671], [0.0, 15.273434, 1.034521], [0.010851, 15.273434, 1.023671], [0.0, 15.273434, 1.01282], [0.0, 15.262583, 1.023671], [0.0, 15.273434, 1.034521], [0.0, 15.284285, 1.023671], [0.0, 15.273434, 1.01282], [-0.010851, 15.273434, 1.023671], [0.0, 15.273434, 1.034521], [0.0, 15.273434, 0.0]]}]},
			"L_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_C_CTLShape", "degree": 3, "form": 2, "points": [[7.795319, 15.36819, 0.724037], [7.772257, 15.468475, 0.798854], [7.724851, 15.484432, 0.915835], [7.680872, 15.406712, 1.006455], [7.666081, 15.280843, 1.01763], [7.689143, 15.180558, 0.942813], [7.736548, 15.164602, 0.825831], [7.780528, 15.242322, 0.735212]]}]},
			"C_midTorso_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_midTorso_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 12.773434, -0.010851], [1.023671, 12.784285, 0.0], [1.023671, 12.773434, 0.010851], [1.023671, 12.762583, 0.0], [1.023671, 12.773434, -0.010851], [1.034521, 12.773434, 0.0], [1.023671, 12.773434, 0.010851], [1.01282, 12.773434, 0.0], [1.023671, 12.784285, 0.0], [1.034521, 12.773434, 0.0], [1.023671, 12.762583, 0.0], [1.01282, 12.773434, 0.0], [1.023671, 12.773434, -0.010851], [1.034521, 12.773434, 0.0], [0.0, 12.773434, 0.0]]}, {"shapeName": "C_midTorso_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 13.797105, -0.010851], [-0.010851, 13.797105, 0.0], [0.0, 13.797105, 0.010851], [0.010851, 13.797105, 0.0], [0.0, 13.797105, -0.010851], [0.0, 13.807955, 0.0], [0.0, 13.797105, 0.010851], [0.0, 13.786254, 0.0], [-0.010851, 13.797105, 0.0], [0.0, 13.807955, 0.0], [0.010851, 13.797105, 0.0], [0.0, 13.786254, 0.0], [0.0, 13.797105, -0.010851], [0.0, 13.807955, 0.0], [0.0, 12.773434, 0.0]]}, {"shapeName": "C_midTorso_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 12.784285, 1.023671], [-0.010851, 12.773434, 1.023671], [0.0, 12.762583, 1.023671], [0.010851, 12.773434, 1.023671], [0.0, 12.784285, 1.023671], [0.0, 12.773434, 1.034521], [0.0, 12.762583, 1.023671], [0.0, 12.773434, 1.01282], [-0.010851, 12.773434, 1.023671], [0.0, 12.773434, 1.034521], [0.010851, 12.773434, 1.023671], [0.0, 12.773434, 1.01282], [0.0, 12.784285, 1.023671], [0.0, 12.773434, 1.034521], [0.0, 12.773434, 0.0]]}]},
			"C_visibility_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_visibility_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.523671, 58.902272, -0.010851], [1.523671, 58.913123, 0.0], [1.523671, 58.902272, 0.010851], [1.523671, 58.891421, 0.0], [1.523671, 58.902272, -0.010851], [1.534521, 58.902272, 0.0], [1.523671, 58.902272, 0.010851], [1.51282, 58.902272, 0.0], [1.523671, 58.913123, 0.0], [1.534521, 58.902272, 0.0], [1.523671, 58.891421, 0.0], [1.51282, 58.902272, 0.0], [1.523671, 58.902272, -0.010851], [1.534521, 58.902272, 0.0], [0.5, 58.902272, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.5, 59.925943, -0.010851], [0.489149, 59.925943, 0.0], [0.5, 59.925943, 0.010851], [0.510851, 59.925943, 0.0], [0.5, 59.925943, -0.010851], [0.5, 59.936793, 0.0], [0.5, 59.925943, 0.010851], [0.5, 59.915092, 0.0], [0.489149, 59.925943, 0.0], [0.5, 59.936793, 0.0], [0.510851, 59.925943, 0.0], [0.5, 59.915092, 0.0], [0.5, 59.925943, -0.010851], [0.5, 59.936793, 0.0], [0.5, 58.902272, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.5, 58.913123, 1.023671], [0.489149, 58.902272, 1.023671], [0.5, 58.891421, 1.023671], [0.510851, 58.902272, 1.023671], [0.5, 58.913123, 1.023671], [0.5, 58.902272, 1.034521], [0.5, 58.891421, 1.023671], [0.5, 58.902272, 1.01282], [0.489149, 58.902272, 1.023671], [0.5, 58.902272, 1.034521], [0.510851, 58.902272, 1.023671], [0.5, 58.902272, 1.01282], [0.5, 58.913123, 1.023671], [0.5, 58.902272, 1.034521], [0.5, 58.902272, 0.0]]}]},
			"L_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_C_CTLShape", "degree": 3, "form": 2, "points": [[7.915627, 15.262349, 0.132458], [7.925, 15.379517, 0.083771], [7.934374, 15.496684, 0.132458], [7.938256, 15.545216, 0.25], [7.934374, 15.496684, 0.367542], [7.925, 15.379517, 0.416229], [7.915627, 15.262349, 0.367542], [7.911744, 15.213817, 0.25]]}]},
			"L_bendyArm_B_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.925, 15.43285, -0.9], [4.925, 15.51285, -0.9], [4.925, 15.299517, -1.1], [4.925, 15.086183, -0.9], [4.925, 15.166183, -0.9], [4.925, 15.166183, -0.633334], [4.925, 14.899517, -0.633334], [4.925, 14.899517, -0.713334], [4.925, 14.699517, -0.5], [4.925, 14.899517, -0.286666], [4.925, 14.899517, -0.366666], [4.925, 15.166183, -0.366666], [4.925, 15.166183, -0.1], [4.925, 15.086183, -0.1], [4.925, 15.299517, 0.1], [4.925, 15.51285, -0.1], [4.925, 15.43285, -0.1], [4.925, 15.43285, -0.366666], [4.925, 15.699517, -0.366666], [4.925, 15.699517, -0.286666], [4.925, 15.899517, -0.5], [4.925, 15.699517, -0.713334], [4.925, 15.699517, -0.633334], [4.925, 15.43285, -0.633334], [4.925, 15.43285, -0.9]]}]},
			"L_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[9.314691, 15.214225, -0.260851], [9.316126, 15.22498, -0.25], [9.314691, 15.214225, -0.239149], [9.313257, 15.203469, -0.25], [9.314691, 15.214225, -0.260851], [9.325446, 15.212791, -0.25], [9.314691, 15.214225, -0.239149], [9.303936, 15.215659, -0.25], [9.316126, 15.22498, -0.25], [9.325446, 15.212791, -0.25], [9.313257, 15.203469, -0.25], [9.303936, 15.215659, -0.25], [9.314691, 15.214225, -0.260851], [9.325446, 15.212791, -0.25], [8.3, 15.349517, -0.25]]}, {"shapeName": "L_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[8.435292, 16.364208, -0.260851], [8.424537, 16.365642, -0.25], [8.435292, 16.364208, -0.239149], [8.446048, 16.362774, -0.25], [8.435292, 16.364208, -0.260851], [8.436726, 16.374963, -0.25], [8.435292, 16.364208, -0.239149], [8.433858, 16.353452, -0.25], [8.424537, 16.365642, -0.25], [8.436726, 16.374963, -0.25], [8.446048, 16.362774, -0.25], [8.433858, 16.353452, -0.25], [8.435292, 16.364208, -0.260851], [8.436726, 16.374963, -0.25], [8.3, 15.349517, -0.25]]}, {"shapeName": "L_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[8.301434, 15.360272, 0.773671], [8.289244, 15.350951, 0.773671], [8.298566, 15.338761, 0.773671], [8.310756, 15.348083, 0.773671], [8.301434, 15.360272, 0.773671], [8.3, 15.349517, 0.784521], [8.298566, 15.338761, 0.773671], [8.3, 15.349517, 0.76282], [8.289244, 15.350951, 0.773671], [8.3, 15.349517, 0.784521], [8.310756, 15.348083, 0.773671], [8.3, 15.349517, 0.76282], [8.301434, 15.360272, 0.773671], [8.3, 15.349517, 0.784521], [8.3, 15.349517, -0.25]]}]},
			"C_torso_FK_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_C_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 12.273434, -1.0], [0.0, 12.311702, -1.007612], [0.0, 12.344144, -1.02929], [0.0, 12.365822, -1.061732], [0.0, 12.373434, -1.1], [0.0, 12.365822, -1.138268], [0.0, 12.344144, -1.17071], [0.0, 12.311702, -1.192388], [0.0, 12.273434, -1.2], [0.0, 12.235166, -1.192388], [0.0, 12.202724, -1.17071], [0.0, 12.181046, -1.138268], [0.0, 12.173434, -1.1], [0.0, 12.181046, -1.061732], [0.0, 12.202724, -1.02929], [0.0, 12.235166, -1.007612], [0.0, 12.273434, -1.0], [0.0, 12.273434, 0.0]]}]},
			"world_B_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -98.299607], [43.670753, 0.0, -54.586315], [32.738176, 0.0, -54.586315], [32.738176, 0.0, -32.729668], [54.594822, 0.0, -32.729668], [54.594822, 0.0, -43.662245], [98.299607, 0.0, 0.0], [54.586315, 0.0, 43.670753], [54.586315, 0.0, 32.738176], [32.729668, 0.0, 32.738176], [32.729668, 0.0, 54.594822], [43.662245, 0.0, 54.594822], [0.0, 0.0, 98.299607], [-43.670753, 0.0, 54.586315], [-32.738176, 0.0, 54.586315], [-32.738176, 0.0, 32.729668], [-54.594822, 0.0, 32.729668], [-54.594822, 0.0, 43.662245], [-98.299607, 0.0, 0.0], [-54.586315, 0.0, -43.670753], [-54.586315, 0.0, -32.738176], [-32.729668, 0.0, -32.738176], [-32.729668, 0.0, -54.594822], [-43.662245, 0.0, -54.594822], [0.0, 0.0, -98.299607], [8.558889, 0.11911, -89.893859], [7.810199, 0.0, -89.094122], [7.810199, 0.0, -85.827111], [7.129572, 0.0, -85.827111], [7.172111, 0.0, -89.119646], [6.687164, 0.0, -88.872918], [6.70418, 0.0, -87.443601], [6.015044, 0.0, -87.443601], [6.015044, 0.0, -88.872918], [5.589652, 0.0, -89.119646], [5.589652, 0.0, -85.776064], [4.900517, 0.0, -85.776064], [4.900517, 0.0, -89.204724], [5.453527, 0.0, -89.757734], [6.304311, 0.0, -89.332342], [7.240174, 0.0, -89.757734], [7.810199, 0.0, -89.111138], [7.240174, 0.0, -89.757734], [6.312819, 0.0, -89.340849], [5.453527, 0.0, -89.749226], [3.794498, 0.0, -89.757734], [4.356015, 0.0, -89.204724], [4.356015, 0.0, -86.337581], [3.794498, 0.0, -85.776064], [1.999343, 0.0, -85.776064], [1.446333, 0.0, -86.337581], [1.446333, 0.0, -89.204724], [1.999343, 0.0, -89.757734], [3.794498, 0.0, -89.757734], [3.581802, 0.0, -89.119646], [3.66688, 0.0, -86.482214], [2.126961, 0.0, -86.49923], [2.135468, 0.0, -89.119646], [3.590309, 0.0, -89.136661], [3.794498, 0.0, -89.757734], [1.999343, 0.0, -89.757734], [0.850784, 0.0, -89.757734], [0.893323, 0.0, -85.776064], [-1.046465, 0.0, -85.776064], [-1.607982, 0.0, -86.337581], [-1.607982, 0.0, -87.537187], [-1.037957, 0.0, -88.090197], [-1.003925, 0.0, -88.132736], [-2.118453, 0.0, -89.740718], [-2.118453, 0.0, -89.757734], [-1.318716, 0.0, -89.757734], [-0.204188, 0.0, -88.141244], [0.212696, 0.0, -88.141244], [0.212696, 0.0, -86.439675], [-0.859292, 0.0, -86.439675], [-0.8678, 0.0, -87.452108], [0.212696, 0.0, -87.452108], [0.212696, 0.0, -89.757734], [0.850784, 0.0, -89.757734], [-5.470542, 0.0, -89.757734], [-5.470542, 0.0, -89.119646], [-3.241488, 0.0, -89.111138], [-3.241488, 0.0, -85.776064], [-2.552353, 0.0, -85.776064], [-2.552353, 0.0, -89.757734], [-8.371717, 0.0, -89.757734], [-8.882187, 0.0, -89.204724], [-8.924726, 0.0, -86.337581], [-8.371717, 0.0, -85.776064], [-6.015044, 0.0, -85.776064], [-6.015044, 0.0, -89.757734], [-6.712687, 0.0, -89.119646], [-6.695672, 0.0, -86.42266], [-8.150513, 0.0, -86.42266], [-8.133497, 0.0, -89.10263], [-6.687164, 0.0, -89.136661], [-5.998029, 0.0, -89.757734]]}]},
			"L_upLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 8.499759, 0.137738], [0.989149, 8.498413, 0.126971], [1.0, 8.497067, 0.116204], [1.010851, 8.498413, 0.126971], [1.0, 8.499759, 0.137738], [1.0, 8.487647, 0.128317], [1.0, 8.497067, 0.116204], [1.0, 8.50918, 0.125625], [0.989149, 8.498413, 0.126971], [1.0, 8.487647, 0.128317], [1.010851, 8.498413, 0.126971], [1.0, 8.50918, 0.125625], [1.0, 8.499759, 0.137738], [1.0, 8.487647, 0.128317], [1.0, 9.514179, 0.0]]}, {"shapeName": "L_upLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.023671, 9.515525, 0.010767], [-0.023671, 9.524946, -0.001346], [-0.023671, 9.512833, -0.010767], [-0.023671, 9.503412, 0.001346], [-0.023671, 9.515525, 0.010767], [-0.034521, 9.514179, -0.0], [-0.023671, 9.512833, -0.010767], [-0.01282, 9.514179, -0.0], [-0.023671, 9.524946, -0.001346], [-0.034521, 9.514179, -0.0], [-0.023671, 9.503412, 0.001346], [-0.01282, 9.514179, -0.0], [-0.023671, 9.515525, 0.010767], [-0.034521, 9.514179, -0.0], [1.0, 9.514179, 0.0]]}, {"shapeName": "L_upLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.989149, 9.387208, -1.015766], [1.0, 9.397976, -1.017112], [1.010851, 9.387208, -1.015766], [1.0, 9.376441, -1.01442], [0.989149, 9.387208, -1.015766], [1.0, 9.385863, -1.026532], [1.010851, 9.387208, -1.015766], [1.0, 9.388554, -1.004999], [1.0, 9.397976, -1.017112], [1.0, 9.385863, -1.026532], [1.0, 9.376441, -1.01442], [1.0, 9.388554, -1.004999], [0.989149, 9.387208, -1.015766], [1.0, 9.385863, -1.026532], [1.0, 9.514179, 0.0]]}]},
			"world_C_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -86.012156], [38.211909, 0.0, -47.763025], [28.645904, 0.0, -47.763025], [28.645904, 0.0, -28.63846], [47.77047, 0.0, -28.63846], [47.77047, 0.0, -38.204465], [86.012156, 0.0, 0.0], [47.763025, 0.0, 38.211909], [47.763025, 0.0, 28.645904], [28.63846, 0.0, 28.645904], [28.63846, 0.0, 47.77047], [38.204465, 0.0, 47.77047], [0.0, 0.0, 86.012156], [-38.211909, 0.0, 47.763025], [-28.645904, 0.0, 47.763025], [-28.645904, 0.0, 28.63846], [-47.77047, 0.0, 28.63846], [-47.77047, 0.0, 38.204465], [-86.012156, 0.0, 0.0], [-47.763025, 0.0, -38.211909], [-47.763025, 0.0, -28.645904], [-28.63846, 0.0, -28.645904], [-28.63846, 0.0, -47.77047], [-38.204465, 0.0, -47.77047], [0.0, 0.0, -86.012156], [7.489028, 0.104221, -78.657127], [6.833924, 0.0, -77.957357], [6.833924, 0.0, -75.098722], [6.238375, 0.0, -75.098722], [6.275597, 0.0, -77.97969], [5.851268, 0.0, -77.763803], [5.866157, 0.0, -76.513151], [5.263164, 0.0, -76.513151], [5.263164, 0.0, -77.763803], [4.890946, 0.0, -77.97969], [4.890946, 0.0, -75.054056], [4.287952, 0.0, -75.054056], [4.287952, 0.0, -78.054133], [4.771836, 0.0, -78.538017], [5.516272, 0.0, -78.165799], [6.335152, 0.0, -78.538017], [6.833924, 0.0, -77.972245], [6.335152, 0.0, -78.538017], [5.523716, 0.0, -78.173243], [4.771836, 0.0, -78.530573], [3.320185, 0.0, -78.538017], [3.811513, 0.0, -78.054133], [3.811513, 0.0, -75.545384], [3.320185, 0.0, -75.054056], [1.749425, 0.0, -75.054056], [1.265542, 0.0, -75.545384], [1.265542, 0.0, -78.054133], [1.749425, 0.0, -78.538017], [3.320185, 0.0, -78.538017], [3.134076, 0.0, -77.97969], [3.20852, 0.0, -75.671938], [1.86109, 0.0, -75.686826], [1.868535, 0.0, -77.97969], [3.141521, 0.0, -77.994579], [3.320185, 0.0, -78.538017], [1.749425, 0.0, -78.538017], [0.744436, 0.0, -78.538017], [0.781658, 0.0, -75.054056], [-0.915657, 0.0, -75.054056], [-1.406984, 0.0, -75.545384], [-1.406984, 0.0, -76.595039], [-0.908212, 0.0, -77.078922], [-0.878435, 0.0, -77.116144], [-1.853646, 0.0, -78.523128], [-1.853646, 0.0, -78.538017], [-1.153876, 0.0, -78.538017], [-0.178665, 0.0, -77.123588], [0.186109, 0.0, -77.123588], [0.186109, 0.0, -75.634716], [-0.751881, 0.0, -75.634716], [-0.759325, 0.0, -76.520595], [0.186109, 0.0, -76.520595], [0.186109, 0.0, -78.538017], [0.744436, 0.0, -78.538017], [-4.786725, 0.0, -78.538017], [-4.786725, 0.0, -77.97969], [-2.836302, 0.0, -77.972245], [-2.836302, 0.0, -75.054056], [-2.233309, 0.0, -75.054056], [-2.233309, 0.0, -78.538017], [-7.325252, 0.0, -78.538017], [-7.771914, 0.0, -78.054133], [-7.809136, 0.0, -75.545384], [-7.325252, 0.0, -75.054056], [-5.263164, 0.0, -75.054056], [-5.263164, 0.0, -78.538017], [-5.873601, 0.0, -77.97969], [-5.858713, 0.0, -75.619827], [-7.131699, 0.0, -75.619827], [-7.11681, 0.0, -77.964801], [-5.851268, 0.0, -77.994579], [-5.248275, 0.0, -78.538017]]}]},
			"C_torso_FK_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 14.297105, -0.010851], [-0.010851, 14.297105, 0.0], [0.0, 14.297105, 0.010851], [0.010851, 14.297105, 0.0], [0.0, 14.297105, -0.010851], [0.0, 14.307955, 0.0], [0.0, 14.297105, 0.010851], [0.0, 14.286254, 0.0], [-0.010851, 14.297105, 0.0], [0.0, 14.307955, 0.0], [0.010851, 14.297105, 0.0], [0.0, 14.286254, 0.0], [0.0, 14.297105, -0.010851], [0.0, 14.307955, 0.0], [0.0, 13.273434, 0.0]]}, {"shapeName": "C_torso_FK_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.023671, 13.273434, -0.010851], [-1.023671, 13.262583, 0.0], [-1.023671, 13.273434, 0.010851], [-1.023671, 13.284285, 0.0], [-1.023671, 13.273434, -0.010851], [-1.034521, 13.273434, 0.0], [-1.023671, 13.273434, 0.010851], [-1.01282, 13.273434, 0.0], [-1.023671, 13.262583, 0.0], [-1.034521, 13.273434, 0.0], [-1.023671, 13.284285, 0.0], [-1.01282, 13.273434, 0.0], [-1.023671, 13.273434, -0.010851], [-1.034521, 13.273434, 0.0], [0.0, 13.273434, 0.0]]}, {"shapeName": "C_torso_FK_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.010851, 13.273434, 1.023671], [0.0, 13.262583, 1.023671], [0.010851, 13.273434, 1.023671], [0.0, 13.284285, 1.023671], [-0.010851, 13.273434, 1.023671], [0.0, 13.273434, 1.034521], [0.010851, 13.273434, 1.023671], [0.0, 13.273434, 1.01282], [0.0, 13.262583, 1.023671], [0.0, 13.273434, 1.034521], [0.0, 13.284285, 1.023671], [0.0, 13.273434, 1.01282], [-0.010851, 13.273434, 1.023671], [0.0, 13.273434, 1.034521], [0.0, 13.273434, 0.0]]}]},
			"L_scapulaTarget_CTL": {"color": 17, "shapes": [{"shapeName": "L_scapulaTarget_CTLShape", "degree": 1, "form": 0, "points": [[0.925, 15.299517, -1.5], [0.425, 15.299517, -2.0], [0.925, 14.799517, -2.0], [0.925, 15.299517, -1.5], [0.925, 15.799517, -2.0], [0.425, 15.299517, -2.0], [0.925, 15.299517, -2.5], [0.925, 15.799517, -2.0], [1.425, 15.299517, -2.0], [0.925, 15.299517, -1.5], [0.925, 14.799517, -2.0], [0.925, 15.299517, -2.5], [1.425, 15.299517, -2.0], [0.925, 14.799517, -2.0]]}]},
			"L_upArm_shaper_D_CTL": {"color": 4, "shapes": [{"shapeName": "L_upArm_shaper_D_CTLShape", "degree": 1, "form": 0, "points": [[4.525, 16.799517, -0.4], [4.599251, 16.810935, -0.418563], [4.662198, 16.843452, -0.434299], [4.704259, 16.892115, -0.444815], [4.719029, 16.949517, -0.448507], [4.704259, 17.006919, -0.444815], [4.662198, 17.055582, -0.434299], [4.599251, 17.088099, -0.418563], [4.525, 17.099517, -0.4], [4.450749, 17.088099, -0.381437], [4.387802, 17.055582, -0.365701], [4.345741, 17.006919, -0.355185], [4.330972, 16.949517, -0.351493], [4.345741, 16.892115, -0.355185], [4.387802, 16.843452, -0.365701], [4.450749, 16.810935, -0.381437], [4.525, 16.799517, -0.4], [4.525, 15.299517, -0.4]]}]},
			"L_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.189691, 15.434809, -0.510851], [8.188257, 15.445565, -0.5], [8.189691, 15.434809, -0.489149], [8.191126, 15.424053, -0.5], [8.189691, 15.434809, -0.510851], [8.200446, 15.436243, -0.5], [8.189691, 15.434809, -0.489149], [8.178936, 15.433375, -0.5], [8.188257, 15.445565, -0.5], [8.200446, 15.436243, -0.5], [8.191126, 15.424053, -0.5], [8.178936, 15.433375, -0.5], [8.189691, 15.434809, -0.510851], [8.200446, 15.436243, -0.5], [7.175, 15.299517, -0.5]]}, {"shapeName": "L_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.039708, 16.314208, -0.510851], [7.028952, 16.312774, -0.5], [7.039708, 16.314208, -0.489149], [7.050464, 16.315642, -0.5], [7.039708, 16.314208, -0.510851], [7.038274, 16.324963, -0.5], [7.039708, 16.314208, -0.489149], [7.041142, 16.303452, -0.5], [7.028952, 16.312774, -0.5], [7.038274, 16.324963, -0.5], [7.050464, 16.315642, -0.5], [7.041142, 16.303452, -0.5], [7.039708, 16.314208, -0.510851], [7.038274, 16.324963, -0.5], [7.175, 15.299517, -0.5]]}, {"shapeName": "L_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.173566, 15.310272, 0.523671], [7.164244, 15.298083, 0.523671], [7.176434, 15.288761, 0.523671], [7.185756, 15.300951, 0.523671], [7.173566, 15.310272, 0.523671], [7.175, 15.299517, 0.534521], [7.176434, 15.288761, 0.523671], [7.175, 15.299517, 0.51282], [7.164244, 15.298083, 0.523671], [7.175, 15.299517, 0.534521], [7.185756, 15.300951, 0.523671], [7.175, 15.299517, 0.51282], [7.173566, 15.310272, 0.523671], [7.175, 15.299517, 0.534521], [7.175, 15.299517, -0.5]]}]},
			"L_arm_IK_switch_CTL": {"color": 1, "shapes": [{"shapeName": "L_arm_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[6.854717, 16.354764, -0.0], [6.900618, 16.388027, -0.0], [6.856479, 16.417477, -0.0], [6.856479, 16.49178, -0.0], [6.902724, 16.48399, -0.0], [6.83141, 16.610898, -0.0], [6.76399, 16.48399, -0.0], [6.810235, 16.49178, -0.0], [6.810235, 16.384456, -0.0], [6.854717, 16.354764, -0.0]]}, {"shapeName": "L_arm_IK_switch_CTLShape1", "degree": 1, "form": 0, "points": [[6.925, 15.299517, -0.0], [6.925, 16.310516, -0.0], [7.039765, 16.288183, -0.0], [7.039765, 16.182691, -0.0], [7.08601, 16.19048, -0.0], [7.01859, 16.063572, -0.0], [6.947276, 16.19048, -0.0], [6.993521, 16.182691, -0.0], [6.993521, 16.255162, -0.0], [6.928729, 16.262679, -0.0]]}, {"shapeName": "L_arm_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[6.83141, 16.063572, -0.0], [6.902724, 16.19048, -0.0], [6.856479, 16.182691, -0.0], [6.856479, 16.256993, -0.0], [7.039765, 16.386287, -0.0], [7.039765, 16.49178, -0.0], [7.08601, 16.48399, -0.0], [7.01859, 16.610898, -0.0], [6.947276, 16.48399, -0.0], [6.993521, 16.49178, -0.0], [6.993521, 16.419308, -0.0], [6.810235, 16.290014, -0.0], [6.810235, 16.182691, -0.0], [6.76399, 16.19048, -0.0], [6.83141, 16.063572, -0.0]]}]},
			"C_cog_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.410502, 9.773434, -1.410502], [0.0, 9.773434, -1.994749], [-1.410502, 9.773434, -1.410502], [-1.994749, 9.773434, 0.0], [-1.410502, 9.773434, 1.410502], [0.0, 9.773434, 1.994749], [1.410502, 9.773434, 1.410502], [1.994749, 9.773434, 0.0]]}]},
			"L_bendyArm_C_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[6.034141, 15.449517, -0.686564], [6.034141, 15.539517, -0.686564], [6.088712, 15.299517, -0.904846], [6.034141, 15.059516, -0.686564], [6.034141, 15.149516, -0.686564], [5.96138, 15.149516, -0.395522], [5.96138, 14.849517, -0.395522], [5.983209, 14.849517, -0.482834], [5.925, 14.624517, -0.25], [5.866791, 14.849517, -0.017166], [5.88862, 14.849517, -0.104478], [5.88862, 15.149516, -0.104478], [5.815859, 15.149516, 0.186564], [5.815859, 15.059516, 0.186564], [5.761288, 15.299517, 0.404846], [5.815859, 15.539517, 0.186564], [5.815859, 15.449517, 0.186564], [5.88862, 15.449517, -0.104478], [5.88862, 15.749517, -0.104478], [5.866791, 15.749517, -0.017166], [5.925, 15.974517, -0.25], [5.983209, 15.749517, -0.482834], [5.96138, 15.749517, -0.395522], [5.96138, 15.449517, -0.395522], [6.034141, 15.449517, -0.686564]]}]},
			"L_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_B_CTLShape", "degree": 3, "form": 2, "points": [[7.559374, 15.232349, -0.617542], [7.55, 15.349517, -0.666229], [7.540627, 15.466684, -0.617542], [7.536744, 15.515216, -0.5], [7.540627, 15.466684, -0.382458], [7.55, 15.349517, -0.333771], [7.559374, 15.232349, -0.382458], [7.563256, 15.183817, -0.5]]}]},
			"L_leg_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 2.53785, -0.010851], [0.989149, 2.53785, 0.0], [1.0, 2.53785, 0.010851], [1.010851, 2.53785, 0.0], [1.0, 2.53785, -0.010851], [1.0, 2.5487, 0.0], [1.0, 2.53785, 0.010851], [1.0, 2.526999, 0.0], [0.989149, 2.53785, 0.0], [1.0, 2.5487, 0.0], [1.010851, 2.53785, 0.0], [1.0, 2.526999, 0.0], [1.0, 2.53785, -0.010851], [1.0, 2.5487, 0.0], [1.0, 1.514179, 0.0]]}, {"shapeName": "L_leg_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.023671, 1.514179, -0.010851], [-0.023671, 1.503328, 0.0], [-0.023671, 1.514179, 0.010851], [-0.023671, 1.52503, 0.0], [-0.023671, 1.514179, -0.010851], [-0.034521, 1.514179, 0.0], [-0.023671, 1.514179, 0.010851], [-0.01282, 1.514179, 0.0], [-0.023671, 1.503328, 0.0], [-0.034521, 1.514179, 0.0], [-0.023671, 1.52503, 0.0], [-0.01282, 1.514179, 0.0], [-0.023671, 1.514179, -0.010851], [-0.034521, 1.514179, 0.0], [1.0, 1.514179, 0.0]]}, {"shapeName": "L_leg_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.989149, 1.514179, 1.023671], [1.0, 1.503328, 1.023671], [1.010851, 1.514179, 1.023671], [1.0, 1.52503, 1.023671], [0.989149, 1.514179, 1.023671], [1.0, 1.514179, 1.034521], [1.010851, 1.514179, 1.023671], [1.0, 1.514179, 1.01282], [1.0, 1.503328, 1.023671], [1.0, 1.514179, 1.034521], [1.0, 1.52503, 1.023671], [1.0, 1.514179, 1.01282], [0.989149, 1.514179, 1.023671], [1.0, 1.514179, 1.034521], [1.0, 1.514179, 0.0]]}]},
			"L_scapulaChest_CTL": {"color": 17, "shapes": [{"shapeName": "L_scapulaChest_CTLShape", "degree": 3, "form": 2, "points": [[0.925, 14.907711, -0.391806], [0.925, 15.299517, -0.554097], [0.925, 15.691323, -0.391806], [0.925, 15.853614, 0.0], [0.925, 15.691323, 0.391806], [0.925, 15.299517, 0.554097], [0.925, 14.907711, 0.391806], [0.925, 14.74542, 0.0]]}, {"shapeName": "L_scapulaChest_CTLShape1", "degree": 3, "form": 2, "points": [[1.316806, 15.299517, -0.391806], [0.925, 15.299517, -0.554097], [0.533194, 15.299517, -0.391806], [0.370903, 15.299517, 0.0], [0.533194, 15.299517, 0.391806], [0.925, 15.299517, 0.554097], [1.316806, 15.299517, 0.391806], [1.479097, 15.299517, 0.0]]}, {"shapeName": "L_scapulaChest_CTLShape2", "degree": 3, "form": 2, "points": [[1.316806, 15.691323, 0.0], [0.925, 15.853614, 0.0], [0.533194, 15.691323, 0.0], [0.370903, 15.299517, 0.0], [0.533194, 14.907711, 0.0], [0.925, 14.74542, 0.0], [1.316806, 14.907711, 0.0], [1.479097, 15.299517, 0.0]]}]},
			"L_loLeg_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 4.497067, 0.383796], [0.989149, 4.498413, 0.373029], [1.0, 4.499759, 0.362262], [1.010851, 4.498413, 0.373029], [1.0, 4.497067, 0.383796], [1.0, 4.487647, 0.371683], [1.0, 4.499759, 0.362262], [1.0, 4.50918, 0.374375], [0.989149, 4.498413, 0.373029], [1.0, 4.487647, 0.371683], [1.010851, 4.498413, 0.373029], [1.0, 4.50918, 0.374375], [1.0, 4.497067, 0.383796], [1.0, 4.487647, 0.371683], [1.0, 5.514179, 0.5]]}, {"shapeName": "L_loLeg_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.023671, 5.512833, 0.510767], [-0.023671, 5.524946, 0.501346], [-0.023671, 5.515525, 0.489233], [-0.023671, 5.503412, 0.498654], [-0.023671, 5.512833, 0.510767], [-0.034521, 5.514179, 0.5], [-0.023671, 5.515525, 0.489233], [-0.01282, 5.514179, 0.5], [-0.023671, 5.524946, 0.501346], [-0.034521, 5.514179, 0.5], [-0.023671, 5.503412, 0.498654], [-0.01282, 5.514179, 0.5], [-0.023671, 5.512833, 0.510767], [-0.034521, 5.514179, 0.5], [1.0, 5.514179, 0.5]]}, {"shapeName": "L_loLeg_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.989149, 5.64115, -0.515766], [1.0, 5.651917, -0.51442], [1.010851, 5.64115, -0.515766], [1.0, 5.630383, -0.517112], [0.989149, 5.64115, -0.515766], [1.0, 5.642496, -0.526532], [1.010851, 5.64115, -0.515766], [1.0, 5.639804, -0.504999], [1.0, 5.651917, -0.51442], [1.0, 5.642496, -0.526532], [1.0, 5.630383, -0.517112], [1.0, 5.639804, -0.504999], [0.989149, 5.64115, -0.515766], [1.0, 5.642496, -0.526532], [1.0, 5.514179, 0.5]]}]},
			"L_bendyArm_A_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[3.840113, 15.416184, -0.58955], [3.840113, 15.486184, -0.58955], [3.797669, 15.299517, -0.759325], [3.840113, 15.11285, -0.58955], [3.840113, 15.18285, -0.58955], [3.896704, 15.18285, -0.363184], [3.896704, 14.949517, -0.363184], [3.879727, 14.949517, -0.431093], [3.925, 14.774517, -0.25], [3.970273, 14.949517, -0.068907], [3.953296, 14.949517, -0.136816], [3.953296, 15.18285, -0.136816], [4.009887, 15.18285, 0.08955], [4.009887, 15.11285, 0.08955], [4.052331, 15.299517, 0.259325], [4.009887, 15.486184, 0.08955], [4.009887, 15.416184, 0.08955], [3.953296, 15.416184, -0.136816], [3.953296, 15.649517, -0.136816], [3.970273, 15.649517, -0.068907], [3.925, 15.824517, -0.25], [3.879727, 15.649517, -0.431093], [3.896704, 15.649517, -0.363184], [3.896704, 15.416184, -0.363184], [3.840113, 15.416184, -0.58955]]}]},
			"L_arm_IK_switch_A_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "L_arm_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[6.861745, 16.249239, -0.0], [6.903056, 16.279176, -0.0], [6.863331, 16.305681, -0.0], [6.863331, 16.372553, -0.0], [6.904952, 16.365542, -0.0], [6.840769, 16.47976, -0.0], [6.780091, 16.365542, -0.0], [6.821712, 16.372553, -0.0], [6.821712, 16.275962, -0.0], [6.861745, 16.249239, -0.0]]}, {"shapeName": "L_arm_IK_switch_A_OFF_CTLShape1", "degree": 1, "form": 0, "points": [[6.925, 15.299517, -0.0], [6.925, 16.209416, -0.0], [7.028289, 16.189316, -0.0], [7.028289, 16.094373, -0.0], [7.069909, 16.101383, -0.0], [7.009231, 15.987166, -0.0], [6.945048, 16.101383, -0.0], [6.986669, 16.094373, -0.0], [6.986669, 16.159597, -0.0], [6.928356, 16.166362, -0.0]]}, {"shapeName": "L_arm_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[6.840769, 15.987166, -0.0], [6.904952, 16.101383, -0.0], [6.863331, 16.094373, -0.0], [6.863331, 16.161245, -0.0], [7.028289, 16.27761, -0.0], [7.028289, 16.372553, -0.0], [7.069909, 16.365542, -0.0], [7.009231, 16.47976, -0.0], [6.945048, 16.365542, -0.0], [6.986669, 16.372553, -0.0], [6.986669, 16.307329, -0.0], [6.821712, 16.190964, -0.0], [6.821712, 16.094373, -0.0], [6.780091, 16.101383, -0.0], [6.840769, 15.987166, -0.0]]}]},
			"L_reverseBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_reverseBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.025451, 0.186549, 0.989149], [2.025451, 0.1974, 1.0], [2.025451, 0.186549, 1.010851], [2.025451, 0.175698, 1.0], [2.025451, 0.186549, 0.989149], [2.036301, 0.186549, 1.0], [2.025451, 0.186549, 1.010851], [2.0146, 0.186549, 1.0], [2.025451, 0.1974, 1.0], [2.036301, 0.186549, 1.0], [2.025451, 0.175698, 1.0], [2.0146, 0.186549, 1.0], [2.025451, 0.186549, 0.989149], [2.036301, 0.186549, 1.0], [1.00178, 0.186549, 1.0]]}, {"shapeName": "L_reverseBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.00178, 1.21022, 0.989149], [0.990929, 1.21022, 1.0], [1.00178, 1.21022, 1.010851], [1.012631, 1.21022, 1.0], [1.00178, 1.21022, 0.989149], [1.00178, 1.22107, 1.0], [1.00178, 1.21022, 1.010851], [1.00178, 1.199369, 1.0], [0.990929, 1.21022, 1.0], [1.00178, 1.22107, 1.0], [1.012631, 1.21022, 1.0], [1.00178, 1.199369, 1.0], [1.00178, 1.21022, 0.989149], [1.00178, 1.22107, 1.0], [1.00178, 0.186549, 1.0]]}, {"shapeName": "L_reverseBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.00178, 0.1974, 2.023671], [0.990929, 0.186549, 2.023671], [1.00178, 0.175698, 2.023671], [1.012631, 0.186549, 2.023671], [1.00178, 0.1974, 2.023671], [1.00178, 0.186549, 2.034521], [1.00178, 0.175698, 2.023671], [1.00178, 0.186549, 2.01282], [0.990929, 0.186549, 2.023671], [1.00178, 0.186549, 2.034521], [1.012631, 0.186549, 2.023671], [1.00178, 0.186549, 2.01282], [1.00178, 0.1974, 2.023671], [1.00178, 0.186549, 2.034521], [1.00178, 0.186549, 1.0]]}]},
			"L_loLeg_shaper_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_shaper_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 2.899759, 0.162262], [1.010851, 2.898413, 0.173029], [1.0, 2.897067, 0.183796], [0.989149, 2.898413, 0.173029], [1.0, 2.899759, 0.162262], [1.0, 2.887647, 0.171683], [1.0, 2.897067, 0.183796], [1.0, 2.90918, 0.174375], [1.010851, 2.898413, 0.173029], [1.0, 2.887647, 0.171683], [0.989149, 2.898413, 0.173029], [1.0, 2.90918, 0.174375], [1.0, 2.899759, 0.162262], [1.0, 2.887647, 0.171683], [1.0, 3.914179, 0.3]]}, {"shapeName": "L_loLeg_shaper_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.023671, 3.915525, 0.289233], [2.023671, 3.924946, 0.301346], [2.023671, 3.912833, 0.310767], [2.023671, 3.903412, 0.298654], [2.023671, 3.915525, 0.289233], [2.034521, 3.914179, 0.3], [2.023671, 3.912833, 0.310767], [2.01282, 3.914179, 0.3], [2.023671, 3.924946, 0.301346], [2.034521, 3.914179, 0.3], [2.023671, 3.903412, 0.298654], [2.01282, 3.914179, 0.3], [2.023671, 3.915525, 0.289233], [2.034521, 3.914179, 0.3], [1.0, 3.914179, 0.3]]}, {"shapeName": "L_loLeg_shaper_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.010851, 3.787208, 1.315766], [1.0, 3.797976, 1.317112], [0.989149, 3.787208, 1.315766], [1.0, 3.776441, 1.31442], [1.010851, 3.787208, 1.315766], [1.0, 3.785863, 1.326532], [0.989149, 3.787208, 1.315766], [1.0, 3.788554, 1.304999], [1.0, 3.797976, 1.317112], [1.0, 3.785863, 1.326532], [1.0, 3.776441, 1.31442], [1.0, 3.788554, 1.304999], [1.010851, 3.787208, 1.315766], [1.0, 3.785863, 1.326532], [1.0, 3.914179, 0.3]]}]},
			"L_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.189691, 15.434809, -0.010851], [8.188257, 15.445565, -0.0], [8.189691, 15.434809, 0.010851], [8.191126, 15.424053, -0.0], [8.189691, 15.434809, -0.010851], [8.200446, 15.436243, -0.0], [8.189691, 15.434809, 0.010851], [8.178936, 15.433375, -0.0], [8.188257, 15.445565, -0.0], [8.200446, 15.436243, -0.0], [8.191126, 15.424053, -0.0], [8.178936, 15.433375, -0.0], [8.189691, 15.434809, -0.010851], [8.200446, 15.436243, -0.0], [7.175, 15.299517, -0.0]]}, {"shapeName": "L_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.039708, 16.314208, -0.010851], [7.028952, 16.312774, -0.0], [7.039708, 16.314208, 0.010851], [7.050464, 16.315642, -0.0], [7.039708, 16.314208, -0.010851], [7.038274, 16.324963, -0.0], [7.039708, 16.314208, 0.010851], [7.041142, 16.303452, -0.0], [7.028952, 16.312774, -0.0], [7.038274, 16.324963, -0.0], [7.050464, 16.315642, -0.0], [7.041142, 16.303452, -0.0], [7.039708, 16.314208, -0.010851], [7.038274, 16.324963, -0.0], [7.175, 15.299517, -0.0]]}, {"shapeName": "L_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.173566, 15.310272, 1.023671], [7.164244, 15.298083, 1.023671], [7.176434, 15.288761, 1.023671], [7.185756, 15.300951, 1.023671], [7.173566, 15.310272, 1.023671], [7.175, 15.299517, 1.034521], [7.176434, 15.288761, 1.023671], [7.175, 15.299517, 1.01282], [7.164244, 15.298083, 1.023671], [7.175, 15.299517, 1.034521], [7.185756, 15.300951, 1.023671], [7.175, 15.299517, 1.01282], [7.173566, 15.310272, 1.023671], [7.175, 15.299517, 1.034521], [7.175, 15.299517, -0.0]]}]},
			"C_torso_FK_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_torso_FK_B_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 11.273434, -1.0], [0.0, 11.311702, -1.007612], [0.0, 11.344144, -1.02929], [0.0, 11.365822, -1.061732], [0.0, 11.373434, -1.1], [0.0, 11.365822, -1.138268], [0.0, 11.344144, -1.17071], [0.0, 11.311702, -1.192388], [0.0, 11.273434, -1.2], [0.0, 11.235166, -1.192388], [0.0, 11.202724, -1.17071], [0.0, 11.181046, -1.138268], [0.0, 11.173434, -1.1], [0.0, 11.181046, -1.061732], [0.0, 11.202724, -1.02929], [0.0, 11.235166, -1.007612], [0.0, 11.273434, -1.0], [0.0, 11.273434, 0.0]]}]},
			"L_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.570411, 15.43115, 0.239149], [8.569546, 15.441966, 0.25], [8.570411, 15.43115, 0.260851], [8.571276, 15.420333, 0.25], [8.570411, 15.43115, 0.239149], [8.581227, 15.432015, 0.25], [8.570411, 15.43115, 0.260851], [8.559595, 15.430284, 0.25], [8.569546, 15.441966, 0.25], [8.581227, 15.432015, 0.25], [8.571276, 15.420333, 0.25], [8.559595, 15.430284, 0.25], [8.570411, 15.43115, 0.239149], [8.581227, 15.432015, 0.25], [7.55, 15.349517, 0.25]]}, {"shapeName": "L_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.468367, 16.369928, 0.239149], [7.457551, 16.369062, 0.25], [7.468367, 16.369928, 0.260851], [7.479184, 16.370793, 0.25], [7.468367, 16.369928, 0.239149], [7.467502, 16.380743, 0.25], [7.468367, 16.369928, 0.260851], [7.469233, 16.359111, 0.25], [7.457551, 16.369062, 0.25], [7.467502, 16.380743, 0.25], [7.479184, 16.370793, 0.25], [7.469233, 16.359111, 0.25], [7.468367, 16.369928, 0.239149], [7.467502, 16.380743, 0.25], [7.55, 15.349517, 0.25]]}, {"shapeName": "L_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.549135, 15.360333, 1.273671], [7.539184, 15.348651, 1.273671], [7.550866, 15.3387, 1.273671], [7.560817, 15.350382, 1.273671], [7.549135, 15.360333, 1.273671], [7.55, 15.349517, 1.284521], [7.550866, 15.3387, 1.273671], [7.55, 15.349517, 1.26282], [7.539184, 15.348651, 1.273671], [7.55, 15.349517, 1.284521], [7.560817, 15.350382, 1.273671], [7.55, 15.349517, 1.26282], [7.549135, 15.360333, 1.273671], [7.55, 15.349517, 1.284521], [7.55, 15.349517, 0.25]]}]},
			"L_toeTip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toeTip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.025451, 0.186549, 1.989149], [2.025451, 0.1974, 2.0], [2.025451, 0.186549, 2.010851], [2.025451, 0.175698, 2.0], [2.025451, 0.186549, 1.989149], [2.036301, 0.186549, 2.0], [2.025451, 0.186549, 2.010851], [2.0146, 0.186549, 2.0], [2.025451, 0.1974, 2.0], [2.036301, 0.186549, 2.0], [2.025451, 0.175698, 2.0], [2.0146, 0.186549, 2.0], [2.025451, 0.186549, 1.989149], [2.036301, 0.186549, 2.0], [1.00178, 0.186549, 2.0]]}, {"shapeName": "L_toeTip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.00178, 1.21022, 1.989149], [0.990929, 1.21022, 2.0], [1.00178, 1.21022, 2.010851], [1.012631, 1.21022, 2.0], [1.00178, 1.21022, 1.989149], [1.00178, 1.22107, 2.0], [1.00178, 1.21022, 2.010851], [1.00178, 1.199369, 2.0], [0.990929, 1.21022, 2.0], [1.00178, 1.22107, 2.0], [1.012631, 1.21022, 2.0], [1.00178, 1.199369, 2.0], [1.00178, 1.21022, 1.989149], [1.00178, 1.22107, 2.0], [1.00178, 0.186549, 2.0]]}, {"shapeName": "L_toeTip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.00178, 0.1974, 3.023671], [0.990929, 0.186549, 3.023671], [1.00178, 0.175698, 3.023671], [1.012631, 0.186549, 3.023671], [1.00178, 0.1974, 3.023671], [1.00178, 0.186549, 3.034521], [1.00178, 0.175698, 3.023671], [1.00178, 0.186549, 3.01282], [0.990929, 0.186549, 3.023671], [1.00178, 0.186549, 3.034521], [1.012631, 0.186549, 3.023671], [1.00178, 0.186549, 3.01282], [1.00178, 0.1974, 3.023671], [1.00178, 0.186549, 3.034521], [1.00178, 0.186549, 2.0]]}]},
			"L_loLeg_shaper_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_shaper_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 1.299759, -0.037738], [1.010851, 1.298413, -0.026971], [1.0, 1.297067, -0.016204], [0.989149, 1.298413, -0.026971], [1.0, 1.299759, -0.037738], [1.0, 1.287647, -0.028317], [1.0, 1.297067, -0.016204], [1.0, 1.30918, -0.025625], [1.010851, 1.298413, -0.026971], [1.0, 1.287647, -0.028317], [0.989149, 1.298413, -0.026971], [1.0, 1.30918, -0.025625], [1.0, 1.299759, -0.037738], [1.0, 1.287647, -0.028317], [1.0, 2.314179, 0.1]]}, {"shapeName": "L_loLeg_shaper_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.023671, 2.315525, 0.089233], [2.023671, 2.324946, 0.101346], [2.023671, 2.312833, 0.110767], [2.023671, 2.303412, 0.098654], [2.023671, 2.315525, 0.089233], [2.034521, 2.314179, 0.1], [2.023671, 2.312833, 0.110767], [2.01282, 2.314179, 0.1], [2.023671, 2.324946, 0.101346], [2.034521, 2.314179, 0.1], [2.023671, 2.303412, 0.098654], [2.01282, 2.314179, 0.1], [2.023671, 2.315525, 0.089233], [2.034521, 2.314179, 0.1], [1.0, 2.314179, 0.1]]}, {"shapeName": "L_loLeg_shaper_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.010851, 2.187208, 1.115766], [1.0, 2.197976, 1.117112], [0.989149, 2.187208, 1.115766], [1.0, 2.176441, 1.11442], [1.010851, 2.187208, 1.115766], [1.0, 2.185863, 1.126532], [0.989149, 2.187208, 1.115766], [1.0, 2.188554, 1.104999], [1.0, 2.197976, 1.117112], [1.0, 2.185863, 1.126532], [1.0, 2.176441, 1.11442], [1.0, 2.188554, 1.104999], [1.010851, 2.187208, 1.115766], [1.0, 2.185863, 1.126532], [1.0, 2.314179, 0.1]]}]},
			"L_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.189691, 15.434809, -0.260851], [8.188257, 15.445565, -0.25], [8.189691, 15.434809, -0.239149], [8.191126, 15.424053, -0.25], [8.189691, 15.434809, -0.260851], [8.200446, 15.436243, -0.25], [8.189691, 15.434809, -0.239149], [8.178936, 15.433375, -0.25], [8.188257, 15.445565, -0.25], [8.200446, 15.436243, -0.25], [8.191126, 15.424053, -0.25], [8.178936, 15.433375, -0.25], [8.189691, 15.434809, -0.260851], [8.200446, 15.436243, -0.25], [7.175, 15.299517, -0.25]]}, {"shapeName": "L_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.039708, 16.314208, -0.260851], [7.028952, 16.312774, -0.25], [7.039708, 16.314208, -0.239149], [7.050464, 16.315642, -0.25], [7.039708, 16.314208, -0.260851], [7.038274, 16.324963, -0.25], [7.039708, 16.314208, -0.239149], [7.041142, 16.303452, -0.25], [7.028952, 16.312774, -0.25], [7.038274, 16.324963, -0.25], [7.050464, 16.315642, -0.25], [7.041142, 16.303452, -0.25], [7.039708, 16.314208, -0.260851], [7.038274, 16.324963, -0.25], [7.175, 15.299517, -0.25]]}, {"shapeName": "L_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.173566, 15.310272, 0.773671], [7.164244, 15.298083, 0.773671], [7.176434, 15.288761, 0.773671], [7.185756, 15.300951, 0.773671], [7.173566, 15.310272, 0.773671], [7.175, 15.299517, 0.784521], [7.176434, 15.288761, 0.773671], [7.175, 15.299517, 0.76282], [7.164244, 15.298083, 0.773671], [7.175, 15.299517, 0.784521], [7.185756, 15.300951, 0.773671], [7.175, 15.299517, 0.76282], [7.173566, 15.310272, 0.773671], [7.175, 15.299517, 0.784521], [7.175, 15.299517, -0.25]]}]},
			"L_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.331263, 15.333914, 1.211304], [8.323851, 15.329942, 1.22414], [8.325837, 15.315119, 1.220701], [8.333248, 15.319091, 1.207864], [8.331263, 15.333914, 1.211304], [8.337946, 15.324517, 1.221427], [8.325837, 15.315119, 1.220701], [8.319153, 15.324517, 1.210577], [8.323851, 15.329942, 1.22414], [8.337946, 15.324517, 1.221427], [8.333248, 15.319091, 1.207864], [8.319153, 15.324517, 1.210577], [8.331263, 15.333914, 1.211304], [8.337946, 15.324517, 1.221427], [7.442025, 15.324517, 0.704167]]}, {"shapeName": "L_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.001475, 15.845749, 1.467221], [6.989365, 15.836352, 1.466494], [6.996049, 15.826955, 1.476619], [7.008159, 15.836352, 1.477345], [7.001475, 15.845749, 1.467221], [6.994064, 15.841777, 1.480057], [6.996049, 15.826955, 1.476619], [7.003461, 15.830927, 1.463782], [6.989365, 15.836352, 1.466494], [6.994064, 15.841777, 1.480057], [7.008159, 15.836352, 1.477345], [7.003461, 15.830927, 1.463782], [7.001475, 15.845749, 1.467221], [6.994064, 15.841777, 1.480057], [7.442025, 15.324517, 0.704167]]}, {"shapeName": "L_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.181408, 14.443417, 1.155567], [7.17671, 14.437992, 1.142004], [7.190806, 14.432566, 1.139291], [7.195504, 14.437992, 1.152855], [7.181408, 14.443417, 1.155567], [7.183394, 14.428595, 1.152127], [7.190806, 14.432566, 1.139291], [7.18882, 14.447389, 1.142731], [7.17671, 14.437992, 1.142004], [7.183394, 14.428595, 1.152127], [7.195504, 14.437992, 1.152855], [7.18882, 14.447389, 1.142731], [7.181408, 14.443417, 1.155567], [7.183394, 14.428595, 1.152127], [7.442025, 15.324517, 0.704167]]}]},
			"C_hip_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.846301, 9.773434, -0.705251], [0.0, 9.413434, -0.997375], [-0.846301, 9.773434, -0.705251], [-1.19685, 10.133434, 0.0], [-0.846301, 9.773434, 0.705251], [0.0, 9.413434, 0.997375], [0.846301, 9.773434, 0.705251], [1.19685, 10.133434, 0.0]]}]},
			"L_bendyArm_B_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_bendyArm_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[4.925, 15.449517, -0.95], [4.925, 15.539517, -0.95], [4.925, 15.299517, -1.175], [4.925, 15.059516, -0.95], [4.925, 15.149516, -0.95], [4.925, 15.149516, -0.65], [4.925, 14.849517, -0.65], [4.925, 14.849517, -0.74], [4.925, 14.624517, -0.5], [4.925, 14.849517, -0.26], [4.925, 14.849517, -0.35], [4.925, 15.149516, -0.35], [4.925, 15.149516, -0.05], [4.925, 15.059516, -0.05], [4.925, 15.299517, 0.175], [4.925, 15.539517, -0.05], [4.925, 15.449517, -0.05], [4.925, 15.449517, -0.35], [4.925, 15.749517, -0.35], [4.925, 15.749517, -0.26], [4.925, 15.974517, -0.5], [4.925, 15.749517, -0.74], [4.925, 15.749517, -0.65], [4.925, 15.449517, -0.65], [4.925, 15.449517, -0.95]]}]},
			"C_head_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.940334, 21.496619, 0.0], [0.0, 21.886118, 0.0], [-0.940334, 21.496619, 0.0], [-1.329833, 20.556285, 0.0], [-0.940334, 19.61595, 0.0], [0.0, 19.226452, 0.0], [0.940334, 19.61595, 0.0], [1.329833, 20.556285, 0.0]]}]},
			"L_ankleOffset_CTL": {"color": 20, "shapes": [{"shapeName": "L_ankleOffset_CTLShape", "degree": 1, "form": 0, "points": [[1.00178, 0.435226, -0.111632], [1.00178, 0.988245, 0.333885], [1.00178, 1.129486, 0.341038], [1.10178, 1.055289, 0.408082], [1.00178, 1.122332, 0.482279], [1.00178, 1.129486, 0.341038], [0.90178, 1.055289, 0.408082], [1.00178, 0.988245, 0.333885], [1.00178, 0.981092, 0.475126], [0.90178, 1.055289, 0.408082], [1.00178, 1.122332, 0.482279], [1.00178, 0.981092, 0.475126], [1.10178, 1.055289, 0.408082], [1.00178, 0.988245, 0.333885]]}]},
			"L_legEnd_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_legEnd_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 0.497067, -0.116204], [0.989149, 0.498413, -0.126971], [1.0, 0.499759, -0.137738], [1.010851, 0.498413, -0.126971], [1.0, 0.497067, -0.116204], [1.0, 0.487647, -0.128317], [1.0, 0.499759, -0.137738], [1.0, 0.50918, -0.125625], [0.989149, 0.498413, -0.126971], [1.0, 0.487647, -0.128317], [1.010851, 0.498413, -0.126971], [1.0, 0.50918, -0.125625], [1.0, 0.497067, -0.116204], [1.0, 0.487647, -0.128317], [1.0, 1.514179, 0.0]]}, {"shapeName": "L_legEnd_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.023671, 1.512833, 0.010767], [-0.023671, 1.524946, 0.001346], [-0.023671, 1.515525, -0.010767], [-0.023671, 1.503412, -0.001346], [-0.023671, 1.512833, 0.010767], [-0.034521, 1.514179, 0.0], [-0.023671, 1.515525, -0.010767], [-0.01282, 1.514179, 0.0], [-0.023671, 1.524946, 0.001346], [-0.034521, 1.514179, 0.0], [-0.023671, 1.503412, -0.001346], [-0.01282, 1.514179, 0.0], [-0.023671, 1.512833, 0.010767], [-0.034521, 1.514179, 0.0], [1.0, 1.514179, 0.0]]}, {"shapeName": "L_legEnd_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.989149, 1.64115, -1.015766], [1.0, 1.651917, -1.01442], [1.010851, 1.64115, -1.015766], [1.0, 1.630383, -1.017112], [0.989149, 1.64115, -1.015766], [1.0, 1.642496, -1.026532], [1.010851, 1.64115, -1.015766], [1.0, 1.639804, -1.004999], [1.0, 1.651917, -1.01442], [1.0, 1.642496, -1.026532], [1.0, 1.630383, -1.017112], [1.0, 1.639804, -1.004999], [0.989149, 1.64115, -1.015766], [1.0, 1.642496, -1.026532], [1.0, 1.514179, 0.0]]}]},
			"L_loLeg_shaper_B_CTL": {"color": 4, "shapes": [{"shapeName": "L_loLeg_shaper_B_CTLShape", "degree": 1, "form": 0, "points": [[2.5, 3.914179, 0.3], [2.511418, 3.838234, 0.290507], [2.543935, 3.773851, 0.282459], [2.592598, 3.73083, 0.277081], [2.65, 3.715724, 0.275193], [2.707402, 3.73083, 0.277081], [2.756065, 3.773851, 0.282459], [2.788582, 3.838234, 0.290507], [2.8, 3.914179, 0.3], [2.788582, 3.990124, 0.309493], [2.756065, 4.054507, 0.317541], [2.707402, 4.097528, 0.322919], [2.65, 4.112635, 0.324807], [2.592598, 4.097528, 0.322919], [2.543935, 4.054507, 0.317541], [2.511418, 3.990124, 0.309493], [2.5, 3.914179, 0.3], [1.0, 3.914179, 0.3]]}]},
			"L_loArm_shaper_C_CTL": {"color": 4, "shapes": [{"shapeName": "L_loArm_shaper_C_CTLShape", "degree": 1, "form": 0, "points": [[6.125, 16.799517, -0.2], [6.199251, 16.810935, -0.181437], [6.262198, 16.843452, -0.165701], [6.304259, 16.892115, -0.155185], [6.319029, 16.949517, -0.151493], [6.304259, 17.006919, -0.155185], [6.262198, 17.055582, -0.165701], [6.199251, 17.088099, -0.181437], [6.125, 17.099517, -0.2], [6.050749, 17.088099, -0.218563], [5.987802, 17.055582, -0.234299], [5.945741, 17.006919, -0.244815], [5.930972, 16.949517, -0.248507], [5.945741, 16.892115, -0.244815], [5.987802, 16.843452, -0.234299], [6.050749, 16.810935, -0.218563], [6.125, 16.799517, -0.2], [6.125, 15.299517, -0.2]]}]},
			"L_clavicle_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_clavicle_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.315891, 15.299517, -0.296964], [2.543857, 15.299517, -0.372952], [2.630933, 15.299517, -0.401978], [2.365197, 15.299517, -0.908933], [2.026813, 15.299517, -1.164199], [1.74503, 15.299517, -1.070271], [1.627482, 15.299517, -0.663028], [1.719067, 15.299517, -0.098022], [1.806143, 15.299517, -0.127048], [2.034109, 15.299517, -0.203036], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25]]}]},
			"C_neck_FK_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_neck_FK_B_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 19.222951, -1.0], [0.0, 19.261219, -1.007612], [0.0, 19.293661, -1.02929], [0.0, 19.315339, -1.061732], [0.0, 19.322951, -1.1], [0.0, 19.315339, -1.138268], [0.0, 19.293661, -1.17071], [0.0, 19.261219, -1.192388], [0.0, 19.222951, -1.2], [0.0, 19.184683, -1.192388], [0.0, 19.152241, -1.17071], [0.0, 19.130563, -1.138268], [0.0, 19.122951, -1.1], [0.0, 19.130563, -1.061732], [0.0, 19.152241, -1.02929], [0.0, 19.184683, -1.007612], [0.0, 19.222951, -1.0], [0.0, 19.222951, 0.0]]}]},
			"L_clavicle_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_clavicle_C_OFF_CTLShape", "degree": 3, "form": 0, "points": [[2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.339373, 15.299517, -0.304791], [2.605334, 15.299517, -0.393445], [2.706922, 15.299517, -0.427307], [2.396897, 15.299517, -1.018755], [2.002115, 15.299517, -1.316566], [1.673369, 15.299517, -1.206983], [1.536229, 15.299517, -0.731866], [1.643078, 15.299517, -0.072693], [1.744666, 15.299517, -0.106555], [2.010627, 15.299517, -0.195209], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25]]}]},
			"L_leg_IK_switch_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_IK_switch_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 0.497067, -0.116204], [0.989149, 0.498413, -0.126971], [1.0, 0.499759, -0.137738], [1.010851, 0.498413, -0.126971], [1.0, 0.497067, -0.116204], [1.0, 0.487647, -0.128317], [1.0, 0.499759, -0.137738], [1.0, 0.50918, -0.125625], [0.989149, 0.498413, -0.126971], [1.0, 0.487647, -0.128317], [1.010851, 0.498413, -0.126971], [1.0, 0.50918, -0.125625], [1.0, 0.497067, -0.116204], [1.0, 0.487647, -0.128317], [1.0, 1.514179, 0.0]]}, {"shapeName": "L_leg_IK_switch_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.023671, 1.512833, 0.010767], [-0.023671, 1.524946, 0.001346], [-0.023671, 1.515525, -0.010767], [-0.023671, 1.503412, -0.001346], [-0.023671, 1.512833, 0.010767], [-0.034521, 1.514179, 0.0], [-0.023671, 1.515525, -0.010767], [-0.01282, 1.514179, 0.0], [-0.023671, 1.524946, 0.001346], [-0.034521, 1.514179, 0.0], [-0.023671, 1.503412, -0.001346], [-0.01282, 1.514179, 0.0], [-0.023671, 1.512833, 0.010767], [-0.034521, 1.514179, 0.0], [1.0, 1.514179, 0.0]]}, {"shapeName": "L_leg_IK_switch_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.989149, 1.64115, -1.015766], [1.0, 1.651917, -1.01442], [1.010851, 1.64115, -1.015766], [1.0, 1.630383, -1.017112], [0.989149, 1.64115, -1.015766], [1.0, 1.642496, -1.026532], [1.010851, 1.64115, -1.015766], [1.0, 1.639804, -1.004999], [1.0, 1.651917, -1.01442], [1.0, 1.642496, -1.026532], [1.0, 1.630383, -1.017112], [1.0, 1.639804, -1.004999], [0.989149, 1.64115, -1.015766], [1.0, 1.642496, -1.026532], [1.0, 1.514179, 0.0]]}]},
			"C_jaw_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_jaw_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.010851, 20.556285, 1.523671], [0.0, 20.567136, 1.523671], [-0.010851, 20.556285, 1.523671], [0.0, 20.545434, 1.523671], [0.010851, 20.556285, 1.523671], [0.0, 20.556285, 1.534521], [-0.010851, 20.556285, 1.523671], [0.0, 20.556285, 1.51282], [0.0, 20.567136, 1.523671], [0.0, 20.556285, 1.534521], [0.0, 20.545434, 1.523671], [0.0, 20.556285, 1.51282], [0.010851, 20.556285, 1.523671], [0.0, 20.556285, 1.534521], [0.0, 20.556285, 0.5]]}, {"shapeName": "C_jaw_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.010851, 21.579956, 0.5], [0.0, 21.579956, 0.489149], [-0.010851, 21.579956, 0.5], [0.0, 21.579956, 0.510851], [0.010851, 21.579956, 0.5], [0.0, 21.590806, 0.5], [-0.010851, 21.579956, 0.5], [0.0, 21.569105, 0.5], [0.0, 21.579956, 0.489149], [0.0, 21.590806, 0.5], [0.0, 21.579956, 0.510851], [0.0, 21.569105, 0.5], [0.010851, 21.579956, 0.5], [0.0, 21.590806, 0.5], [0.0, 20.556285, 0.5]]}, {"shapeName": "C_jaw_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.023671, 20.567136, 0.5], [-1.023671, 20.556285, 0.489149], [-1.023671, 20.545434, 0.5], [-1.023671, 20.556285, 0.510851], [-1.023671, 20.567136, 0.5], [-1.034521, 20.556285, 0.5], [-1.023671, 20.545434, 0.5], [-1.01282, 20.556285, 0.5], [-1.023671, 20.556285, 0.489149], [-1.034521, 20.556285, 0.5], [-1.023671, 20.556285, 0.510851], [-1.01282, 20.556285, 0.5], [-1.023671, 20.567136, 0.5], [-1.034521, 20.556285, 0.5], [0.0, 20.556285, 0.5]]}]},
			"C_head_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_head_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 20.556285, -0.010851], [1.023671, 20.567136, 0.0], [1.023671, 20.556285, 0.010851], [1.023671, 20.545434, 0.0], [1.023671, 20.556285, -0.010851], [1.034521, 20.556285, 0.0], [1.023671, 20.556285, 0.010851], [1.01282, 20.556285, 0.0], [1.023671, 20.567136, 0.0], [1.034521, 20.556285, 0.0], [1.023671, 20.545434, 0.0], [1.01282, 20.556285, 0.0], [1.023671, 20.556285, -0.010851], [1.034521, 20.556285, 0.0], [0.0, 20.556285, 0.0]]}, {"shapeName": "C_head_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 21.579956, -0.010851], [-0.010851, 21.579956, 0.0], [0.0, 21.579956, 0.010851], [0.010851, 21.579956, 0.0], [0.0, 21.579956, -0.010851], [0.0, 21.590806, 0.0], [0.0, 21.579956, 0.010851], [0.0, 21.569105, 0.0], [-0.010851, 21.579956, 0.0], [0.0, 21.590806, 0.0], [0.010851, 21.579956, 0.0], [0.0, 21.569105, 0.0], [0.0, 21.579956, -0.010851], [0.0, 21.590806, 0.0], [0.0, 20.556285, 0.0]]}, {"shapeName": "C_head_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 20.567136, 1.023671], [-0.010851, 20.556285, 1.023671], [0.0, 20.545434, 1.023671], [0.010851, 20.556285, 1.023671], [0.0, 20.567136, 1.023671], [0.0, 20.556285, 1.034521], [0.0, 20.545434, 1.023671], [0.0, 20.556285, 1.01282], [-0.010851, 20.556285, 1.023671], [0.0, 20.556285, 1.034521], [0.010851, 20.556285, 1.023671], [0.0, 20.556285, 1.01282], [0.0, 20.567136, 1.023671], [0.0, 20.556285, 1.034521], [0.0, 20.556285, 0.0]]}]},
			"C_cog_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_cog_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.880669, 9.773434, -1.880669], [0.0, 9.773434, -2.659666], [-1.880669, 9.773434, -1.880669], [-2.659666, 9.773434, 0.0], [-1.880669, 9.773434, 1.880669], [0.0, 9.773434, 2.659666], [1.880669, 9.773434, 1.880669], [2.659666, 9.773434, 0.0]]}]},
			"L_arm_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_arm_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[7.948671, 15.299517, -0.010851], [7.948671, 15.310368, -0.0], [7.948671, 15.299517, 0.010851], [7.948671, 15.288666, -0.0], [7.948671, 15.299517, -0.010851], [7.959521, 15.299517, -0.0], [7.948671, 15.299517, 0.010851], [7.93782, 15.299517, -0.0], [7.948671, 15.310368, -0.0], [7.959521, 15.299517, -0.0], [7.948671, 15.288666, -0.0], [7.93782, 15.299517, -0.0], [7.948671, 15.299517, -0.010851], [7.959521, 15.299517, -0.0], [6.925, 15.299517, -0.0]]}, {"shapeName": "L_arm_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[6.925, 16.323188, -0.010851], [6.914149, 16.323188, -0.0], [6.925, 16.323188, 0.010851], [6.935851, 16.323188, -0.0], [6.925, 16.323188, -0.010851], [6.925, 16.334038, -0.0], [6.925, 16.323188, 0.010851], [6.925, 16.312337, -0.0], [6.914149, 16.323188, -0.0], [6.925, 16.334038, -0.0], [6.935851, 16.323188, -0.0], [6.925, 16.312337, -0.0], [6.925, 16.323188, -0.010851], [6.925, 16.334038, -0.0], [6.925, 15.299517, -0.0]]}, {"shapeName": "L_arm_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[6.925, 15.310368, 1.023671], [6.914149, 15.299517, 1.023671], [6.925, 15.288666, 1.023671], [6.935851, 15.299517, 1.023671], [6.925, 15.310368, 1.023671], [6.925, 15.299517, 1.034521], [6.925, 15.288666, 1.023671], [6.925, 15.299517, 1.01282], [6.914149, 15.299517, 1.023671], [6.925, 15.299517, 1.034521], [6.935851, 15.299517, 1.023671], [6.925, 15.299517, 1.01282], [6.925, 15.310368, 1.023671], [6.925, 15.299517, 1.034521], [6.925, 15.299517, -0.0]]}]},
			"L_toe_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_toe_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.00178, 0.1974, 2.023671], [0.990929, 0.186549, 2.023671], [1.00178, 0.175698, 2.023671], [1.012631, 0.186549, 2.023671], [1.00178, 0.1974, 2.023671], [1.00178, 0.186549, 2.034521], [1.00178, 0.175698, 2.023671], [1.00178, 0.186549, 2.01282], [0.990929, 0.186549, 2.023671], [1.00178, 0.186549, 2.034521], [1.012631, 0.186549, 2.023671], [1.00178, 0.186549, 2.01282], [1.00178, 0.1974, 2.023671], [1.00178, 0.186549, 2.034521], [1.00178, 0.186549, 1.0]]}, {"shapeName": "L_toe_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.021891, 0.1974, 1.0], [-0.021891, 0.186549, 0.989149], [-0.021891, 0.175698, 1.0], [-0.021891, 0.186549, 1.010851], [-0.021891, 0.1974, 1.0], [-0.032741, 0.186549, 1.0], [-0.021891, 0.175698, 1.0], [-0.01104, 0.186549, 1.0], [-0.021891, 0.186549, 0.989149], [-0.032741, 0.186549, 1.0], [-0.021891, 0.186549, 1.010851], [-0.01104, 0.186549, 1.0], [-0.021891, 0.1974, 1.0], [-0.032741, 0.186549, 1.0], [1.00178, 0.186549, 1.0]]}, {"shapeName": "L_toe_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.990929, -0.837122, 1.0], [1.00178, -0.837122, 0.989149], [1.012631, -0.837122, 1.0], [1.00178, -0.837122, 1.010851], [0.990929, -0.837122, 1.0], [1.00178, -0.847972, 1.0], [1.012631, -0.837122, 1.0], [1.00178, -0.826271, 1.0], [1.00178, -0.837122, 0.989149], [1.00178, -0.847972, 1.0], [1.00178, -0.837122, 1.010851], [1.00178, -0.826271, 1.0], [0.990929, -0.837122, 1.0], [1.00178, -0.847972, 1.0], [1.00178, 0.186549, 1.0]]}]},
			"C_torso_FK_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_torso_FK_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 12.297105, -0.010851], [-0.010851, 12.297105, 0.0], [0.0, 12.297105, 0.010851], [0.010851, 12.297105, 0.0], [0.0, 12.297105, -0.010851], [0.0, 12.307955, 0.0], [0.0, 12.297105, 0.010851], [0.0, 12.286254, 0.0], [-0.010851, 12.297105, 0.0], [0.0, 12.307955, 0.0], [0.010851, 12.297105, 0.0], [0.0, 12.286254, 0.0], [0.0, 12.297105, -0.010851], [0.0, 12.307955, 0.0], [0.0, 11.273434, 0.0]]}, {"shapeName": "C_torso_FK_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.023671, 11.273434, -0.010851], [-1.023671, 11.262583, 0.0], [-1.023671, 11.273434, 0.010851], [-1.023671, 11.284285, 0.0], [-1.023671, 11.273434, -0.010851], [-1.034521, 11.273434, 0.0], [-1.023671, 11.273434, 0.010851], [-1.01282, 11.273434, 0.0], [-1.023671, 11.262583, 0.0], [-1.034521, 11.273434, 0.0], [-1.023671, 11.284285, 0.0], [-1.01282, 11.273434, 0.0], [-1.023671, 11.273434, -0.010851], [-1.034521, 11.273434, 0.0], [0.0, 11.273434, 0.0]]}, {"shapeName": "C_torso_FK_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.010851, 11.273434, 1.023671], [0.0, 11.262583, 1.023671], [0.010851, 11.273434, 1.023671], [0.0, 11.284285, 1.023671], [-0.010851, 11.273434, 1.023671], [0.0, 11.273434, 1.034521], [0.010851, 11.273434, 1.023671], [0.0, 11.273434, 1.01282], [0.0, 11.262583, 1.023671], [0.0, 11.273434, 1.034521], [0.0, 11.284285, 1.023671], [0.0, 11.273434, 1.01282], [-0.010851, 11.273434, 1.023671], [0.0, 11.273434, 1.034521], [0.0, 11.273434, 0.0]]}]},
			"C_neck_FK_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_neck_FK_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 20.913289, -0.010851], [-0.010851, 20.913289, 0.0], [0.0, 20.913289, 0.010851], [0.010851, 20.913289, 0.0], [0.0, 20.913289, -0.010851], [0.0, 20.924139, 0.0], [0.0, 20.913289, 0.010851], [0.0, 20.902438, 0.0], [-0.010851, 20.913289, 0.0], [0.0, 20.924139, 0.0], [0.010851, 20.913289, 0.0], [0.0, 20.902438, 0.0], [0.0, 20.913289, -0.010851], [0.0, 20.924139, 0.0], [0.0, 19.889618, 0.0]]}, {"shapeName": "C_neck_FK_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.023671, 19.889618, -0.010851], [-1.023671, 19.878767, 0.0], [-1.023671, 19.889618, 0.010851], [-1.023671, 19.900469, 0.0], [-1.023671, 19.889618, -0.010851], [-1.034521, 19.889618, 0.0], [-1.023671, 19.889618, 0.010851], [-1.01282, 19.889618, 0.0], [-1.023671, 19.878767, 0.0], [-1.034521, 19.889618, 0.0], [-1.023671, 19.900469, 0.0], [-1.01282, 19.889618, 0.0], [-1.023671, 19.889618, -0.010851], [-1.034521, 19.889618, 0.0], [0.0, 19.889618, 0.0]]}, {"shapeName": "C_neck_FK_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.010851, 19.889618, 1.023671], [0.0, 19.878767, 1.023671], [0.010851, 19.889618, 1.023671], [0.0, 19.900469, 1.023671], [-0.010851, 19.889618, 1.023671], [0.0, 19.889618, 1.034521], [0.010851, 19.889618, 1.023671], [0.0, 19.889618, 1.01282], [0.0, 19.878767, 1.023671], [0.0, 19.889618, 1.034521], [0.0, 19.900469, 1.023671], [0.0, 19.889618, 1.01282], [-0.010851, 19.889618, 1.023671], [0.0, 19.889618, 1.034521], [0.0, 19.889618, 0.0]]}]},
			"C_midTorso_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.269451, 12.773434, -1.057876], [0.0, 12.773434, -1.496062], [-1.269451, 12.773434, -1.057876], [-1.795274, 12.773434, 0.0], [-1.269451, 12.773434, 1.057876], [0.0, 12.773434, 1.496062], [1.269451, 12.773434, 1.057876], [1.795274, 12.773434, 0.0]]}]},
			"L_wrist_IK_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_wrist_IK_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[6.925, 15.699517, -0.4], [6.925, 15.699517, 0.4], [6.925, 14.899517, 0.4], [6.925, 14.899517, -0.4], [6.925, 15.699517, -0.4]]}]},
			"C_midTorso_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.987351, 12.773434, -0.822793], [0.0, 12.773434, -1.163604], [-0.987351, 12.773434, -0.822793], [-1.396324, 12.773434, 0.0], [-0.987351, 12.773434, 0.822793], [0.0, 12.773434, 1.163604], [0.987351, 12.773434, 0.822793], [1.396324, 12.773434, 0.0]]}]},
			"C_hip_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.987351, 9.773434, -0.822793], [0.0, 9.353434, -1.163604], [-0.987351, 9.773434, -0.822793], [-1.396324, 10.193434, 0.0], [-0.987351, 9.773434, 0.822793], [0.0, 9.353434, 1.163604], [0.987351, 9.773434, 0.822793], [1.396324, 10.193434, 0.0]]}]},
			"L_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.945411, 15.297884, -0.010851], [8.946276, 15.3087, -0.0], [8.945411, 15.297884, 0.010851], [8.944546, 15.287067, -0.0], [8.945411, 15.297884, -0.010851], [8.956227, 15.297019, -0.0], [8.945411, 15.297884, 0.010851], [8.934595, 15.298749, -0.0], [8.946276, 15.3087, -0.0], [8.956227, 15.297019, -0.0], [8.944546, 15.287067, -0.0], [8.934595, 15.298749, -0.0], [8.945411, 15.297884, -0.010851], [8.956227, 15.297019, -0.0], [7.925, 15.379517, -0.0]]}, {"shapeName": "L_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[8.006633, 16.399928, -0.010851], [7.995817, 16.400793, -0.0], [8.006633, 16.399928, 0.010851], [8.01745, 16.399062, -0.0], [8.006633, 16.399928, -0.010851], [8.007498, 16.410743, -0.0], [8.006633, 16.399928, 0.010851], [8.005768, 16.389111, -0.0], [7.995817, 16.400793, -0.0], [8.007498, 16.410743, -0.0], [8.01745, 16.399062, -0.0], [8.005768, 16.389111, -0.0], [8.006633, 16.399928, -0.010851], [8.007498, 16.410743, -0.0], [7.925, 15.379517, -0.0]]}, {"shapeName": "L_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.925866, 15.390333, 1.023671], [7.914184, 15.380382, 1.023671], [7.924135, 15.3687, 1.023671], [7.935817, 15.378651, 1.023671], [7.925866, 15.390333, 1.023671], [7.925, 15.379517, 1.034521], [7.924135, 15.3687, 1.023671], [7.925, 15.379517, 1.01282], [7.914184, 15.380382, 1.023671], [7.925, 15.379517, 1.034521], [7.935817, 15.378651, 1.023671], [7.925, 15.379517, 1.01282], [7.925866, 15.390333, 1.023671], [7.925, 15.379517, 1.034521], [7.925, 15.379517, -0.0]]}]},
			"L_arm_IK_switch_C_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "L_arm_IK_switch_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[6.875802, 16.03819, -0.0], [6.907933, 16.061474, -0.0], [6.877035, 16.082089, -0.0], [6.877035, 16.134101, -0.0], [6.909407, 16.128648, -0.0], [6.859487, 16.217483, -0.0], [6.812293, 16.128648, -0.0], [6.844665, 16.134101, -0.0], [6.844665, 16.058974, -0.0], [6.875802, 16.03819, -0.0]]}, {"shapeName": "L_arm_IK_switch_C_OFF_CTLShape1", "degree": 1, "form": 0, "points": [[6.925, 15.299517, -0.0], [6.925, 16.007216, -0.0], [7.005336, 15.991583, -0.0], [7.005336, 15.917738, -0.0], [7.037707, 15.923191, -0.0], [6.990513, 15.834355, -0.0], [6.940593, 15.923191, -0.0], [6.972965, 15.917738, -0.0], [6.972965, 15.968468, -0.0], [6.92761, 15.97373, -0.0]]}, {"shapeName": "L_arm_IK_switch_C_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[6.859487, 15.834355, -0.0], [6.909407, 15.923191, -0.0], [6.877035, 15.917738, -0.0], [6.877035, 15.96975, -0.0], [7.005336, 16.060256, -0.0], [7.005336, 16.134101, -0.0], [7.037707, 16.128648, -0.0], [6.990513, 16.217483, -0.0], [6.940593, 16.128648, -0.0], [6.972965, 16.134101, -0.0], [6.972965, 16.08337, -0.0], [6.844665, 15.992865, -0.0], [6.844665, 15.917738, -0.0], [6.812293, 15.923191, -0.0], [6.859487, 15.834355, -0.0]]}]},
			"L_leg_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.470167, 1.514179, -0.783612], [1.0, 1.514179, -1.108194], [0.529833, 1.514179, -0.783612], [0.335084, 1.514179, 0.0], [0.529833, 1.514179, 0.783612], [1.0, 1.514179, 1.108194], [1.470167, 1.514179, 0.783612], [1.664916, 1.514179, 0.0]]}]},
			"L_upArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_upArm_FK_CTLShape", "degree": 1, "form": 0, "points": [[4.713241, 15.549517, -0.189366], [3.258027, 15.549517, 0.174437], [3.136759, 15.549517, -0.310634], [4.591973, 15.549517, -0.674437], [4.591973, 15.049517, -0.674437], [3.136759, 15.049517, -0.310634], [3.258027, 15.049517, 0.174437], [4.713241, 15.049517, -0.189366], [4.713241, 15.549517, -0.189366], [4.591973, 15.549517, -0.674437], [3.136759, 15.549517, -0.310634], [3.136759, 15.049517, -0.310634], [4.591973, 15.049517, -0.674437], [4.713241, 15.049517, -0.189366], [3.258027, 15.049517, 0.174437], [3.258027, 15.549517, 0.174437]]}]},
			"L_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_A_CTLShape", "degree": 3, "form": 2, "points": [[7.26982, 15.34319, 0.37064], [7.216557, 15.443475, 0.428021], [7.138951, 15.459432, 0.527566], [7.082462, 15.381712, 0.610963], [7.080181, 15.255843, 0.62936], [7.133443, 15.155558, 0.571979], [7.211049, 15.139602, 0.472434], [7.267538, 15.217322, 0.389037]]}]},
			"L_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.189691, 15.434809, 0.239149], [8.188257, 15.445565, 0.25], [8.189691, 15.434809, 0.260851], [8.191126, 15.424053, 0.25], [8.189691, 15.434809, 0.239149], [8.200446, 15.436243, 0.25], [8.189691, 15.434809, 0.260851], [8.178936, 15.433375, 0.25], [8.188257, 15.445565, 0.25], [8.200446, 15.436243, 0.25], [8.191126, 15.424053, 0.25], [8.178936, 15.433375, 0.25], [8.189691, 15.434809, 0.239149], [8.200446, 15.436243, 0.25], [7.175, 15.299517, 0.25]]}, {"shapeName": "L_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.039708, 16.314208, 0.239149], [7.028952, 16.312774, 0.25], [7.039708, 16.314208, 0.260851], [7.050464, 16.315642, 0.25], [7.039708, 16.314208, 0.239149], [7.038274, 16.324963, 0.25], [7.039708, 16.314208, 0.260851], [7.041142, 16.303452, 0.25], [7.028952, 16.312774, 0.25], [7.038274, 16.324963, 0.25], [7.050464, 16.315642, 0.25], [7.041142, 16.303452, 0.25], [7.039708, 16.314208, 0.239149], [7.038274, 16.324963, 0.25], [7.175, 15.299517, 0.25]]}, {"shapeName": "L_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.173566, 15.310272, 1.273671], [7.164244, 15.298083, 1.273671], [7.176434, 15.288761, 1.273671], [7.185756, 15.300951, 1.273671], [7.173566, 15.310272, 1.273671], [7.175, 15.299517, 1.284521], [7.176434, 15.288761, 1.273671], [7.175, 15.299517, 1.26282], [7.164244, 15.298083, 1.273671], [7.175, 15.299517, 1.284521], [7.185756, 15.300951, 1.273671], [7.175, 15.299517, 1.26282], [7.173566, 15.310272, 1.273671], [7.175, 15.299517, 1.284521], [7.175, 15.299517, 0.25]]}]},
			"C_hip_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.128401, 9.773434, -0.940334], [0.0, 9.293434, -1.329833], [-1.128401, 9.773434, -0.940334], [-1.595799, 10.253434, 0.0], [-1.128401, 9.773434, 0.940334], [0.0, 9.293434, 1.329833], [1.128401, 9.773434, 0.940334], [1.595799, 10.253434, 0.0]]}]},
			"C_hip_CTL": {"color": 17, "shapes": [{"shapeName": "C_hip_CTLShape", "degree": 3, "form": 2, "points": [[1.410502, 9.773434, -1.175418], [0.0, 9.173434, -1.662291], [-1.410502, 9.773434, -1.175418], [-1.994749, 10.373434, 0.0], [-1.410502, 9.773434, 1.175418], [0.0, 9.173434, 1.662291], [1.410502, 9.773434, 1.175418], [1.994749, 10.373434, 0.0]]}]},
			"world_CTL": {"color": 1, "shapes": [{"shapeName": "world_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -266.42936], [118.364368, 0.0, -147.949695], [88.732922, 0.0, -147.949695], [88.732922, 0.0, -88.709862], [147.972754, 0.0, -88.709862], [147.972754, 0.0, -118.341308], [266.42936, 0.0, 0.0], [147.949695, 0.0, 118.364368], [147.949695, 0.0, 88.732922], [88.709862, 0.0, 88.732922], [88.709862, 0.0, 147.972754], [118.341308, 0.0, 147.972754], [0.0, 0.0, 266.42936], [-118.364368, 0.0, 147.949695], [-88.732922, 0.0, 147.949695], [-88.732922, 0.0, 88.709862], [-147.972754, 0.0, 88.709862], [-147.972754, 0.0, 118.341308], [-266.42936, 0.0, 0.0], [-147.949695, 0.0, -118.364368], [-147.949695, 0.0, -88.732922], [-88.709862, 0.0, -88.732922], [-88.709862, 0.0, -147.972754], [-118.341308, 0.0, -147.972754], [0.0, 0.0, -266.42936], [23.197848, 0.322833, -243.646583], [21.168613, 0.0, -241.478991], [21.168613, 0.0, -232.624146], [19.323854, 0.0, -232.624146], [19.439151, 0.0, -241.548169], [18.12476, 0.0, -240.879444], [18.170879, 0.0, -237.005449], [16.30306, 0.0, -237.005449], [16.30306, 0.0, -240.879444], [15.150086, 0.0, -241.548169], [15.150086, 0.0, -232.485789], [13.282267, 0.0, -232.485789], [13.282267, 0.0, -241.778764], [14.781134, 0.0, -243.277631], [17.087083, 0.0, -242.124656], [19.623627, 0.0, -243.277631], [21.168613, 0.0, -241.525109], [19.623627, 0.0, -243.277631], [17.110142, 0.0, -242.147716], [14.781134, 0.0, -243.254571], [10.284533, 0.0, -243.277631], [11.806459, 0.0, -241.778764], [11.806459, 0.0, -234.007715], [10.284533, 0.0, -232.485789], [5.41898, 0.0, -232.485789], [3.920113, 0.0, -234.007715], [3.920113, 0.0, -241.778764], [5.41898, 0.0, -243.277631], [10.284533, 0.0, -243.277631], [9.708046, 0.0, -241.548169], [9.938641, 0.0, -234.399727], [5.764873, 0.0, -234.445846], [5.787932, 0.0, -241.548169], [9.731105, 0.0, -241.594288], [10.284533, 0.0, -243.277631], [5.41898, 0.0, -243.277631], [2.305949, 0.0, -243.277631], [2.421247, 0.0, -232.485789], [-2.836317, 0.0, -232.485789], [-4.358244, 0.0, -234.007715], [-4.358244, 0.0, -237.259104], [-2.813258, 0.0, -238.757971], [-2.72102, 0.0, -238.873268], [-5.741813, 0.0, -243.231512], [-5.741813, 0.0, -243.277631], [-3.574221, 0.0, -243.277631], [-0.553428, 0.0, -238.896328], [0.576487, 0.0, -238.896328], [0.576487, 0.0, -234.284429], [-2.329009, 0.0, -234.284429], [-2.352068, 0.0, -237.028509], [0.576487, 0.0, -237.028509], [0.576487, 0.0, -243.277631], [2.305949, 0.0, -243.277631], [-14.827253, 0.0, -243.277631], [-14.827253, 0.0, -241.548169], [-8.785666, 0.0, -241.525109], [-8.785666, 0.0, -232.485789], [-6.917847, 0.0, -232.485789], [-6.917847, 0.0, -243.277631], [-22.690539, 0.0, -243.277631], [-24.074109, 0.0, -241.778764], [-24.189406, 0.0, -234.007715], [-22.690539, 0.0, -232.485789], [-16.30306, 0.0, -232.485789], [-16.30306, 0.0, -243.277631], [-18.193938, 0.0, -241.548169], [-18.147819, 0.0, -234.23831], [-22.090992, 0.0, -234.23831], [-22.044873, 0.0, -241.50205], [-18.12476, 0.0, -241.594288], [-16.256941, 0.0, -243.277631]]}]},
			"L_legBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_legBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 8.499759, 0.137738], [0.989149, 8.498413, 0.126971], [1.0, 8.497067, 0.116204], [1.010851, 8.498413, 0.126971], [1.0, 8.499759, 0.137738], [1.0, 8.487647, 0.128317], [1.0, 8.497067, 0.116204], [1.0, 8.50918, 0.125625], [0.989149, 8.498413, 0.126971], [1.0, 8.487647, 0.128317], [1.010851, 8.498413, 0.126971], [1.0, 8.50918, 0.125625], [1.0, 8.499759, 0.137738], [1.0, 8.487647, 0.128317], [1.0, 9.514179, 0.0]]}, {"shapeName": "L_legBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.023671, 9.515525, 0.010767], [-0.023671, 9.524946, -0.001346], [-0.023671, 9.512833, -0.010767], [-0.023671, 9.503412, 0.001346], [-0.023671, 9.515525, 0.010767], [-0.034521, 9.514179, -0.0], [-0.023671, 9.512833, -0.010767], [-0.01282, 9.514179, -0.0], [-0.023671, 9.524946, -0.001346], [-0.034521, 9.514179, -0.0], [-0.023671, 9.503412, 0.001346], [-0.01282, 9.514179, -0.0], [-0.023671, 9.515525, 0.010767], [-0.034521, 9.514179, -0.0], [1.0, 9.514179, 0.0]]}, {"shapeName": "L_legBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.989149, 9.387208, -1.015766], [1.0, 9.397976, -1.017112], [1.010851, 9.387208, -1.015766], [1.0, 9.376441, -1.01442], [0.989149, 9.387208, -1.015766], [1.0, 9.385863, -1.026532], [1.010851, 9.387208, -1.015766], [1.0, 9.388554, -1.004999], [1.0, 9.397976, -1.017112], [1.0, 9.385863, -1.026532], [1.0, 9.376441, -1.01442], [1.0, 9.388554, -1.004999], [0.989149, 9.387208, -1.015766], [1.0, 9.385863, -1.026532], [1.0, 9.514179, 0.0]]}]},
			"C_head_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_head_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.822793, 21.379077, 0.0], [0.0, 21.719888, 0.0], [-0.822793, 21.379077, 0.0], [-1.163604, 20.556285, 0.0], [-0.822793, 19.733492, 0.0], [0.0, 19.392681, 0.0], [0.822793, 19.733492, 0.0], [1.163604, 20.556285, 0.0]]}]},
			"L_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.198671, 16.299517, -0.010851], [8.198671, 16.310368, -0.0], [8.198671, 16.299517, 0.010851], [8.198671, 16.288666, -0.0], [8.198671, 16.299517, -0.010851], [8.209521, 16.299517, -0.0], [8.198671, 16.299517, 0.010851], [8.18782, 16.299517, -0.0], [8.198671, 16.310368, -0.0], [8.209521, 16.299517, -0.0], [8.198671, 16.288666, -0.0], [8.18782, 16.299517, -0.0], [8.198671, 16.299517, -0.010851], [8.209521, 16.299517, -0.0], [7.175, 16.299517, -0.0]]}, {"shapeName": "L_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.175, 17.323188, -0.010851], [7.164149, 17.323188, -0.0], [7.175, 17.323188, 0.010851], [7.185851, 17.323188, -0.0], [7.175, 17.323188, -0.010851], [7.175, 17.334038, -0.0], [7.175, 17.323188, 0.010851], [7.175, 17.312337, -0.0], [7.164149, 17.323188, -0.0], [7.175, 17.334038, -0.0], [7.185851, 17.323188, -0.0], [7.175, 17.312337, -0.0], [7.175, 17.323188, -0.010851], [7.175, 17.334038, -0.0], [7.175, 16.299517, -0.0]]}, {"shapeName": "L_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.175, 16.310368, 1.023671], [7.164149, 16.299517, 1.023671], [7.175, 16.288666, 1.023671], [7.185851, 16.299517, 1.023671], [7.175, 16.310368, 1.023671], [7.175, 16.299517, 1.034521], [7.175, 16.288666, 1.023671], [7.175, 16.299517, 1.01282], [7.164149, 16.299517, 1.023671], [7.175, 16.299517, 1.034521], [7.185851, 16.299517, 1.023671], [7.175, 16.299517, 1.01282], [7.175, 16.310368, 1.023671], [7.175, 16.299517, 1.034521], [7.175, 16.299517, -0.0]]}]},
			"L_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_C_CTLShape", "degree": 3, "form": 2, "points": [[7.915627, 15.262349, -0.617542], [7.925, 15.379517, -0.666229], [7.934374, 15.496684, -0.617542], [7.938256, 15.545216, -0.5], [7.934374, 15.496684, -0.382458], [7.925, 15.379517, -0.333771], [7.915627, 15.262349, -0.382458], [7.911744, 15.213817, -0.5]]}]},
			"L_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_B_CTLShape", "degree": 3, "form": 2, "points": [[7.559374, 15.232349, 0.132458], [7.55, 15.349517, 0.083771], [7.540627, 15.466684, 0.132458], [7.536744, 15.515216, 0.25], [7.540627, 15.466684, 0.367542], [7.55, 15.349517, 0.416229], [7.559374, 15.232349, 0.367542], [7.563256, 15.183817, 0.25]]}]},
			"L_leg_IK_switch_A_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "L_leg_IK_switch_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[3.849167, 1.325881, -0.023537], [3.938977, 1.448856, -0.008165], [4.018492, 1.330601, -0.022947], [4.21911, 1.330601, -0.022947], [4.198077, 1.454498, -0.00746], [4.540729, 1.263438, -0.031343], [4.198077, 1.082809, -0.053921], [4.21911, 1.206707, -0.038434], [3.929335, 1.206707, -0.038434], [3.849167, 1.325881, -0.023537]]}, {"shapeName": "L_leg_IK_switch_A_OFF_CTLShape1", "degree": 1, "form": 0, "points": [[1.0, 1.514179, 0.0], [3.729697, 1.514179, 0.0], [3.669398, 1.821652, 0.038434], [3.38457, 1.821652, 0.038434], [3.4056, 1.945549, 0.053921], [3.062949, 1.764921, 0.031343], [3.4056, 1.57386, 0.00746], [3.38457, 1.697757, 0.022947], [3.580242, 1.697757, 0.022947], [3.600537, 1.52417, 0.001249]]}, {"shapeName": "L_leg_IK_switch_A_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[3.062949, 1.263438, -0.031343], [3.4056, 1.454498, -0.00746], [3.38457, 1.330601, -0.022947], [3.585185, 1.330601, -0.022947], [3.934279, 1.821652, 0.038434], [4.21911, 1.821652, 0.038434], [4.198077, 1.945549, 0.053921], [4.540729, 1.764921, 0.031343], [4.198077, 1.57386, 0.00746], [4.21911, 1.697757, 0.022947], [4.023436, 1.697757, 0.022947], [3.674342, 1.206707, -0.038434], [3.38457, 1.206707, -0.038434], [3.4056, 1.082809, -0.053921], [3.062949, 1.263438, -0.031343]]}]},
			"L_innerBall_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_innerBall_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.525451, 0.186549, 0.989149], [1.525451, 0.1974, 1.0], [1.525451, 0.186549, 1.010851], [1.525451, 0.175698, 1.0], [1.525451, 0.186549, 0.989149], [1.536301, 0.186549, 1.0], [1.525451, 0.186549, 1.010851], [1.5146, 0.186549, 1.0], [1.525451, 0.1974, 1.0], [1.536301, 0.186549, 1.0], [1.525451, 0.175698, 1.0], [1.5146, 0.186549, 1.0], [1.525451, 0.186549, 0.989149], [1.536301, 0.186549, 1.0], [0.50178, 0.186549, 1.0]]}, {"shapeName": "L_innerBall_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.50178, 1.21022, 0.989149], [0.490929, 1.21022, 1.0], [0.50178, 1.21022, 1.010851], [0.512631, 1.21022, 1.0], [0.50178, 1.21022, 0.989149], [0.50178, 1.22107, 1.0], [0.50178, 1.21022, 1.010851], [0.50178, 1.199369, 1.0], [0.490929, 1.21022, 1.0], [0.50178, 1.22107, 1.0], [0.512631, 1.21022, 1.0], [0.50178, 1.199369, 1.0], [0.50178, 1.21022, 0.989149], [0.50178, 1.22107, 1.0], [0.50178, 0.186549, 1.0]]}, {"shapeName": "L_innerBall_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.50178, 0.1974, 2.023671], [0.490929, 0.186549, 2.023671], [0.50178, 0.175698, 2.023671], [0.512631, 0.186549, 2.023671], [0.50178, 0.1974, 2.023671], [0.50178, 0.186549, 2.034521], [0.50178, 0.175698, 2.023671], [0.50178, 0.186549, 2.01282], [0.490929, 0.186549, 2.023671], [0.50178, 0.186549, 2.034521], [0.512631, 0.186549, 2.023671], [0.50178, 0.186549, 2.01282], [0.50178, 0.1974, 2.023671], [0.50178, 0.186549, 2.034521], [0.50178, 0.186549, 1.0]]}]},
			"L_wrist_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_wrist_FK_CTLShape", "degree": 1, "form": 0, "points": [[7.225, 15.799517, 0.5], [7.125, 15.799517, 0.5], [7.125, 15.799517, -0.5], [7.225, 15.799517, -0.5], [7.225, 14.799517, -0.5], [7.125, 14.799517, -0.5], [7.125, 14.799517, 0.5], [7.225, 14.799517, 0.5], [7.225, 15.799517, 0.5], [7.225, 15.799517, -0.5], [7.125, 15.799517, -0.5], [7.125, 14.799517, -0.5], [7.225, 14.799517, -0.5], [7.225, 14.799517, 0.5], [7.125, 14.799517, 0.5], [7.125, 15.799517, 0.5]]}]},
			"L_wrist_IK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_wrist_IK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[7.948671, 15.299517, -0.010851], [7.948671, 15.310368, -0.0], [7.948671, 15.299517, 0.010851], [7.948671, 15.288666, -0.0], [7.948671, 15.299517, -0.010851], [7.959521, 15.299517, -0.0], [7.948671, 15.299517, 0.010851], [7.93782, 15.299517, -0.0], [7.948671, 15.310368, -0.0], [7.959521, 15.299517, -0.0], [7.948671, 15.288666, -0.0], [7.93782, 15.299517, -0.0], [7.948671, 15.299517, -0.010851], [7.959521, 15.299517, -0.0], [6.925, 15.299517, -0.0]]}, {"shapeName": "L_wrist_IK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[6.925, 16.323188, -0.010851], [6.914149, 16.323188, -0.0], [6.925, 16.323188, 0.010851], [6.935851, 16.323188, -0.0], [6.925, 16.323188, -0.010851], [6.925, 16.334038, -0.0], [6.925, 16.323188, 0.010851], [6.925, 16.312337, -0.0], [6.914149, 16.323188, -0.0], [6.925, 16.334038, -0.0], [6.935851, 16.323188, -0.0], [6.925, 16.312337, -0.0], [6.925, 16.323188, -0.010851], [6.925, 16.334038, -0.0], [6.925, 15.299517, -0.0]]}, {"shapeName": "L_wrist_IK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[6.925, 15.310368, 1.023671], [6.914149, 15.299517, 1.023671], [6.925, 15.288666, 1.023671], [6.935851, 15.299517, 1.023671], [6.925, 15.310368, 1.023671], [6.925, 15.299517, 1.034521], [6.925, 15.288666, 1.023671], [6.925, 15.299517, 1.01282], [6.914149, 15.299517, 1.023671], [6.925, 15.299517, 1.034521], [6.935851, 15.299517, 1.023671], [6.925, 15.299517, 1.01282], [6.925, 15.310368, 1.023671], [6.925, 15.299517, 1.034521], [6.925, 15.299517, -0.0]]}]},
			"C_midNeck_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.128401, 19.556285, -0.940334], [0.0, 19.556285, -1.329833], [-1.128401, 19.556285, -0.940334], [-1.595799, 19.556285, 0.0], [-1.128401, 19.556285, 0.940334], [0.0, 19.556285, 1.329833], [1.128401, 19.556285, 0.940334], [1.595799, 19.556285, 0.0]]}]},
			"L_upLeg_shaper_B_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_B_CTLShape", "degree": 1, "form": 0, "points": [[2.5, 7.914179, 0.2], [2.511418, 7.838234, 0.209493], [2.543935, 7.773851, 0.217541], [2.592598, 7.73083, 0.222919], [2.65, 7.715724, 0.224807], [2.707402, 7.73083, 0.222919], [2.756065, 7.773851, 0.217541], [2.788582, 7.838234, 0.209493], [2.8, 7.914179, 0.2], [2.788582, 7.990124, 0.190507], [2.756065, 8.054507, 0.182459], [2.707402, 8.097528, 0.177081], [2.65, 8.112635, 0.175193], [2.592598, 8.097528, 0.177081], [2.543935, 8.054507, 0.182459], [2.511418, 7.990124, 0.190507], [2.5, 7.914179, 0.2], [1.0, 7.914179, 0.2]]}]},
			"L_upLeg_shaper_C_CTL": {"color": 4, "shapes": [{"shapeName": "L_upLeg_shaper_C_CTLShape", "degree": 1, "form": 0, "points": [[2.5, 7.114179, 0.3], [2.511418, 7.038234, 0.309493], [2.543935, 6.973851, 0.317541], [2.592598, 6.93083, 0.322919], [2.65, 6.915724, 0.324807], [2.707402, 6.93083, 0.322919], [2.756065, 6.973851, 0.317541], [2.788582, 7.038234, 0.309493], [2.8, 7.114179, 0.3], [2.788582, 7.190124, 0.290507], [2.756065, 7.254507, 0.282459], [2.707402, 7.297528, 0.277081], [2.65, 7.312635, 0.275193], [2.592598, 7.297528, 0.277081], [2.543935, 7.254507, 0.282459], [2.511418, 7.190124, 0.290507], [2.5, 7.114179, 0.3], [1.0, 7.114179, 0.3]]}]},
			"L_leg_IK_switch_CTL": {"color": 1, "shapes": [{"shapeName": "L_leg_IK_switch_CTLShape", "degree": 1, "form": 0, "points": [[4.165741, 1.304958, -0.026153], [4.26553, 1.441598, -0.009073], [4.35388, 1.310204, -0.025497], [4.576789, 1.310204, -0.025497], [4.553419, 1.447867, -0.008289], [4.934143, 1.235577, -0.034825], [4.553419, 1.034879, -0.059912], [4.576789, 1.172543, -0.042705], [4.254817, 1.172543, -0.042705], [4.165741, 1.304958, -0.026153]]}, {"shapeName": "L_leg_IK_switch_CTLShape1", "degree": 1, "form": 0, "points": [[1.0, 1.514179, 0.0], [4.032997, 1.514179, 0.0], [3.965998, 1.855816, 0.042705], [3.649522, 1.855816, 0.042705], [3.672889, 1.993479, 0.059912], [3.292165, 1.792781, 0.034825], [3.672889, 1.580491, 0.008289], [3.649522, 1.718155, 0.025497], [3.866935, 1.718155, 0.025497], [3.889486, 1.52528, 0.001388]]}, {"shapeName": "L_leg_IK_switch_CTLShape2", "degree": 1, "form": 0, "points": [[3.292165, 1.235577, -0.034825], [3.672889, 1.447867, -0.008289], [3.649522, 1.310204, -0.025497], [3.872428, 1.310204, -0.025497], [4.26031, 1.855816, 0.042705], [4.576789, 1.855816, 0.042705], [4.553419, 1.993479, 0.059912], [4.934143, 1.792781, 0.034825], [4.553419, 1.580491, 0.008289], [4.576789, 1.718155, 0.025497], [4.359373, 1.718155, 0.025497], [3.971491, 1.172543, -0.042705], [3.649522, 1.172543, -0.042705], [3.672889, 1.034879, -0.059912], [3.292165, 1.235577, -0.034825]]}]},
			"C_midNeck_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midNeck_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.846301, 19.556285, -0.705251], [0.0, 19.556285, -0.997375], [-0.846301, 19.556285, -0.705251], [-1.19685, 19.556285, 0.0], [-0.846301, 19.556285, 0.705251], [0.0, 19.556285, 0.997375], [0.846301, 19.556285, 0.705251], [1.19685, 19.556285, 0.0]]}]},
			"L_leg_PV_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_leg_PV_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 4.490508, 10.510851], [0.989149, 4.490508, 10.5], [1.0, 4.490508, 10.489149], [1.010851, 4.490508, 10.5], [1.0, 4.490508, 10.510851], [1.0, 4.479658, 10.5], [1.0, 4.490508, 10.489149], [1.0, 4.501359, 10.5], [0.989149, 4.490508, 10.5], [1.0, 4.479658, 10.5], [1.010851, 4.490508, 10.5], [1.0, 4.501359, 10.5], [1.0, 4.490508, 10.510851], [1.0, 4.479658, 10.5], [1.0, 5.514179, 10.5]]}, {"shapeName": "L_leg_PV_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.023671, 5.514179, 10.510851], [-0.023671, 5.52503, 10.5], [-0.023671, 5.514179, 10.489149], [-0.023671, 5.503328, 10.5], [-0.023671, 5.514179, 10.510851], [-0.034521, 5.514179, 10.5], [-0.023671, 5.514179, 10.489149], [-0.01282, 5.514179, 10.5], [-0.023671, 5.52503, 10.5], [-0.034521, 5.514179, 10.5], [-0.023671, 5.503328, 10.5], [-0.01282, 5.514179, 10.5], [-0.023671, 5.514179, 10.510851], [-0.034521, 5.514179, 10.5], [1.0, 5.514179, 10.5]]}, {"shapeName": "L_leg_PV_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.989149, 5.514179, 9.476329], [1.0, 5.52503, 9.476329], [1.010851, 5.514179, 9.476329], [1.0, 5.503328, 9.476329], [0.989149, 5.514179, 9.476329], [1.0, 5.514179, 9.465479], [1.010851, 5.514179, 9.476329], [1.0, 5.514179, 9.48718], [1.0, 5.52503, 9.476329], [1.0, 5.514179, 9.465479], [1.0, 5.503328, 9.476329], [1.0, 5.514179, 9.48718], [0.989149, 5.514179, 9.476329], [1.0, 5.514179, 9.465479], [1.0, 5.514179, 10.5]]}]},
			"L_leg_IK_switch_B_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "L_leg_IK_switch_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[3.532593, 1.346803, -0.020922], [3.612424, 1.456114, -0.007258], [3.683104, 1.350999, -0.020398], [3.861431, 1.350999, -0.020398], [3.842735, 1.46113, -0.006631], [4.147314, 1.291298, -0.02786], [3.842735, 1.130739, -0.04793], [3.861431, 1.24087, -0.034164], [3.603854, 1.24087, -0.034164], [3.532593, 1.346803, -0.020922]]}, {"shapeName": "L_leg_IK_switch_B_OFF_CTLShape1", "degree": 1, "form": 0, "points": [[1.0, 1.514179, 0.0], [3.426398, 1.514179, 0.0], [3.372798, 1.787488, 0.034164], [3.119618, 1.787488, 0.034164], [3.138311, 1.897619, 0.04793], [2.833732, 1.737061, 0.02786], [3.138311, 1.567229, 0.006631], [3.119618, 1.67736, 0.020398], [3.293548, 1.67736, 0.020398], [3.311589, 1.52306, 0.00111]]}, {"shapeName": "L_leg_IK_switch_B_OFF_CTLShape2", "degree": 1, "form": 0, "points": [[2.833732, 1.291298, -0.02786], [3.138311, 1.46113, -0.006631], [3.119618, 1.350999, -0.020398], [3.297942, 1.350999, -0.020398], [3.608248, 1.787488, 0.034164], [3.861431, 1.787488, 0.034164], [3.842735, 1.897619, 0.04793], [4.147314, 1.737061, 0.02786], [3.842735, 1.567229, 0.006631], [3.861431, 1.67736, 0.020398], [3.687498, 1.67736, 0.020398], [3.377193, 1.24087, -0.034164], [3.119618, 1.24087, -0.034164], [3.138311, 1.130739, -0.04793], [2.833732, 1.291298, -0.02786]]}]},
			"L_toe_IK_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.354406, 0.539174, 1.0], [1.00178, 0.685236, 1.0], [0.649155, 0.539174, 1.0], [0.503093, 0.186549, 1.0], [0.649155, -0.166076, 1.0], [1.00178, -0.312138, 1.0], [1.354406, -0.166076, 1.0], [1.500468, 0.186549, 1.0]]}]},
			"L_leg_IK_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_leg_IK_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.411396, 1.514179, -0.68566], [1.0, 1.514179, -0.96967], [0.588604, 1.514179, -0.68566], [0.418198, 1.514179, 0.0], [0.588604, 1.514179, 0.68566], [1.0, 1.514179, 0.96967], [1.411396, 1.514179, 0.68566], [1.581802, 1.514179, 0.0]]}]},
			"L_wrist_IK_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_wrist_IK_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[6.925, 15.649517, -0.35], [6.925, 15.649517, 0.35], [6.925, 14.949517, 0.35], [6.925, 14.949517, -0.35], [6.925, 15.649517, -0.35]]}]},
			"L_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.570411, 15.43115, -0.510851], [8.569546, 15.441966, -0.5], [8.570411, 15.43115, -0.489149], [8.571276, 15.420333, -0.5], [8.570411, 15.43115, -0.510851], [8.581227, 15.432015, -0.5], [8.570411, 15.43115, -0.489149], [8.559595, 15.430284, -0.5], [8.569546, 15.441966, -0.5], [8.581227, 15.432015, -0.5], [8.571276, 15.420333, -0.5], [8.559595, 15.430284, -0.5], [8.570411, 15.43115, -0.510851], [8.581227, 15.432015, -0.5], [7.55, 15.349517, -0.5]]}, {"shapeName": "L_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.468367, 16.369928, -0.510851], [7.457551, 16.369062, -0.5], [7.468367, 16.369928, -0.489149], [7.479184, 16.370793, -0.5], [7.468367, 16.369928, -0.510851], [7.467502, 16.380743, -0.5], [7.468367, 16.369928, -0.489149], [7.469233, 16.359111, -0.5], [7.457551, 16.369062, -0.5], [7.467502, 16.380743, -0.5], [7.479184, 16.370793, -0.5], [7.469233, 16.359111, -0.5], [7.468367, 16.369928, -0.510851], [7.467502, 16.380743, -0.5], [7.55, 15.349517, -0.5]]}, {"shapeName": "L_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.549135, 15.360333, 0.523671], [7.539184, 15.348651, 0.523671], [7.550866, 15.3387, 0.523671], [7.560817, 15.350382, 0.523671], [7.549135, 15.360333, 0.523671], [7.55, 15.349517, 0.534521], [7.550866, 15.3387, 0.523671], [7.55, 15.349517, 0.51282], [7.539184, 15.348651, 0.523671], [7.55, 15.349517, 0.534521], [7.560817, 15.350382, 0.523671], [7.55, 15.349517, 0.51282], [7.549135, 15.360333, 0.523671], [7.55, 15.349517, 0.534521], [7.55, 15.349517, -0.5]]}]},
			"L_legBase_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_D_OFF_CTLShape", "degree": 3, "form": 0, "points": [[1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.366813, 0.018421], [1.0, 9.128372, 0.048226], [1.0, 9.037295, 0.059611], [1.0, 9.198448, 0.608836], [1.0, 9.480199, 0.925508], [1.0, 9.774931, 0.888666], [1.0, 9.970063, 0.512384], [1.0, 9.991064, -0.059611], [1.0, 9.899987, -0.048226], [1.0, 9.661545, -0.018421], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0]]}]},
			"L_toe_IK_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_CTLShape", "degree": 3, "form": 2, "points": [[1.393586, 0.578355, 1.25], [1.00178, 0.740646, 1.25], [0.609974, 0.578355, 1.25], [0.447683, 0.186549, 1.25], [0.609974, -0.205257, 1.25], [1.00178, -0.367548, 1.25], [1.393586, -0.205257, 1.25], [1.555877, 0.186549, 1.25]]}]},
			"C_midTorso_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_midTorso_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.128401, 12.773434, -0.940334], [0.0, 12.773434, -1.329833], [-1.128401, 12.773434, -0.940334], [-1.595799, 12.773434, 0.0], [-1.128401, 12.773434, 0.940334], [0.0, 12.773434, 1.329833], [1.128401, 12.773434, 0.940334], [1.595799, 12.773434, 0.0]]}]},
			"L_loArm_FK_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_loArm_FK_CTLShape", "degree": 1, "form": 0, "points": [[6.591973, 15.549517, 0.174437], [5.136759, 15.549517, -0.189366], [5.258027, 15.549517, -0.674437], [6.713241, 15.549517, -0.310634], [6.713241, 15.049517, -0.310634], [5.258027, 15.049517, -0.674437], [5.136759, 15.049517, -0.189366], [6.591973, 15.049517, 0.174437], [6.591973, 15.549517, 0.174437], [6.713241, 15.549517, -0.310634], [5.258027, 15.549517, -0.674437], [5.258027, 15.049517, -0.674437], [6.713241, 15.049517, -0.310634], [6.591973, 15.049517, 0.174437], [5.136759, 15.049517, -0.189366], [5.136759, 15.549517, -0.189366]]}]},
			"L_arm_IK_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_arm_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[6.925, 15.048761, -0.250756], [6.925, 15.299517, -0.354622], [6.925, 15.550273, -0.250756], [6.925, 15.654139, -0.0], [6.925, 15.550273, 0.250756], [6.925, 15.299517, 0.354622], [6.925, 15.048761, 0.250756], [6.925, 14.944895, -0.0]]}]},
			"L_upArm_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upArm_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[4.915475, 15.299517, -0.508804], [4.918107, 15.310368, -0.498277], [4.920739, 15.299517, -0.48775], [4.918107, 15.288666, -0.498277], [4.915475, 15.299517, -0.508804], [4.928633, 15.299517, -0.500908], [4.920739, 15.299517, -0.48775], [4.90758, 15.299517, -0.495645], [4.918107, 15.310368, -0.498277], [4.928633, 15.299517, -0.500908], [4.918107, 15.288666, -0.498277], [4.90758, 15.299517, -0.495645], [4.915475, 15.299517, -0.508804], [4.928633, 15.299517, -0.500908], [3.925, 15.299517, -0.25]]}, {"shapeName": "L_upArm_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[3.922368, 16.323188, -0.260527], [3.914473, 16.323188, -0.247368], [3.927632, 16.323188, -0.239473], [3.935527, 16.323188, -0.252632], [3.922368, 16.323188, -0.260527], [3.925, 16.334038, -0.25], [3.927632, 16.323188, -0.239473], [3.925, 16.312337, -0.25], [3.914473, 16.323188, -0.247368], [3.925, 16.334038, -0.25], [3.935527, 16.323188, -0.252632], [3.925, 16.312337, -0.25], [3.922368, 16.323188, -0.260527], [3.925, 16.334038, -0.25], [3.925, 15.299517, -0.25]]}, {"shapeName": "L_upArm_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.173277, 15.310368, 0.743107], [4.16275, 15.299517, 0.745738], [4.173277, 15.288666, 0.743107], [4.183804, 15.299517, 0.740475], [4.173277, 15.310368, 0.743107], [4.175908, 15.299517, 0.753633], [4.173277, 15.288666, 0.743107], [4.170645, 15.299517, 0.73258], [4.16275, 15.299517, 0.745738], [4.175908, 15.299517, 0.753633], [4.183804, 15.299517, 0.740475], [4.170645, 15.299517, 0.73258], [4.173277, 15.310368, 0.743107], [4.175908, 15.299517, 0.753633], [3.925, 15.299517, -0.25]]}]},
			"L_loArm_shaper_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loArm_shaper_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[6.720739, 15.299517, -0.06225], [6.718107, 15.310368, -0.051723], [6.715475, 15.299517, -0.041196], [6.718107, 15.288666, -0.051723], [6.720739, 15.299517, -0.06225], [6.728633, 15.299517, -0.049092], [6.715475, 15.299517, -0.041196], [6.70758, 15.299517, -0.054355], [6.718107, 15.310368, -0.051723], [6.728633, 15.299517, -0.049092], [6.718107, 15.288666, -0.051723], [6.70758, 15.299517, -0.054355], [6.720739, 15.299517, -0.06225], [6.728633, 15.299517, -0.049092], [5.725, 15.299517, -0.3]]}, {"shapeName": "L_loArm_shaper_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[5.727632, 16.323188, -0.310527], [5.714473, 16.323188, -0.302632], [5.722368, 16.323188, -0.289473], [5.735527, 16.323188, -0.297368], [5.727632, 16.323188, -0.310527], [5.725, 16.334038, -0.3], [5.722368, 16.323188, -0.289473], [5.725, 16.312337, -0.3], [5.714473, 16.323188, -0.302632], [5.725, 16.334038, -0.3], [5.735527, 16.323188, -0.297368], [5.725, 16.312337, -0.3], [5.727632, 16.323188, -0.310527], [5.725, 16.334038, -0.3], [5.725, 15.299517, -0.3]]}, {"shapeName": "L_loArm_shaper_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[5.476723, 15.310368, 0.693107], [5.466196, 15.299517, 0.690475], [5.476723, 15.288666, 0.693107], [5.48725, 15.299517, 0.695738], [5.476723, 15.310368, 0.693107], [5.474092, 15.299517, 0.703633], [5.476723, 15.288666, 0.693107], [5.479355, 15.299517, 0.68258], [5.466196, 15.299517, 0.690475], [5.474092, 15.299517, 0.703633], [5.48725, 15.299517, 0.695738], [5.479355, 15.299517, 0.68258], [5.476723, 15.310368, 0.693107], [5.474092, 15.299517, 0.703633], [5.725, 15.299517, -0.3]]}]},
			"L_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_B_CTLShape", "degree": 3, "form": 2, "points": [[7.522307, 15.36754, 0.565113], [7.483582, 15.468475, 0.632187], [7.420513, 15.485082, 0.741426], [7.370045, 15.407631, 0.828838], [7.361742, 15.281493, 0.84322], [7.400467, 15.180558, 0.776146], [7.463536, 15.163952, 0.666907], [7.514004, 15.241402, 0.579495]]}]},
			"L_upLeg_shaper_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_shaper_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 6.897067, 0.316204], [1.010851, 6.898413, 0.326971], [1.0, 6.899759, 0.337738], [0.989149, 6.898413, 0.326971], [1.0, 6.897067, 0.316204], [1.0, 6.887647, 0.328317], [1.0, 6.899759, 0.337738], [1.0, 6.90918, 0.325625], [1.010851, 6.898413, 0.326971], [1.0, 6.887647, 0.328317], [0.989149, 6.898413, 0.326971], [1.0, 6.90918, 0.325625], [1.0, 6.897067, 0.316204], [1.0, 6.887647, 0.328317], [1.0, 7.914179, 0.2]]}, {"shapeName": "L_upLeg_shaper_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.023671, 7.912833, 0.189233], [2.023671, 7.924946, 0.198654], [2.023671, 7.915525, 0.210767], [2.023671, 7.903412, 0.201346], [2.023671, 7.912833, 0.189233], [2.034521, 7.914179, 0.2], [2.023671, 7.915525, 0.210767], [2.01282, 7.914179, 0.2], [2.023671, 7.924946, 0.198654], [2.034521, 7.914179, 0.2], [2.023671, 7.903412, 0.201346], [2.01282, 7.914179, 0.2], [2.023671, 7.912833, 0.189233], [2.034521, 7.914179, 0.2], [1.0, 7.914179, 0.2]]}, {"shapeName": "L_upLeg_shaper_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.010851, 8.04115, 1.215766], [1.0, 8.051917, 1.21442], [0.989149, 8.04115, 1.215766], [1.0, 8.030383, 1.217112], [1.010851, 8.04115, 1.215766], [1.0, 8.042496, 1.226532], [0.989149, 8.04115, 1.215766], [1.0, 8.039804, 1.204999], [1.0, 8.051917, 1.21442], [1.0, 8.042496, 1.226532], [1.0, 8.030383, 1.217112], [1.0, 8.039804, 1.204999], [1.010851, 8.04115, 1.215766], [1.0, 8.042496, 1.226532], [1.0, 7.914179, 0.2]]}]},
			"visibility_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "visibility_CTLShape", "degree": 3, "form": 2, "points": [[1.001108, 58.902272, 0.0], [0.5, 59.304066, 0.0], [-0.001108, 58.902272, 0.0], [0.000208, 58.902272, 0.0], [-0.001108, 58.902272, 0.0], [0.5, 58.500478, 0.0], [1.001108, 58.902272, 0.0], [1.001108, 58.902272, 0.0]]}, {"shapeName": "visibility_CTLShape1", "degree": 3, "form": 2, "points": [[0.709736, 59.112008, 0.0], [0.5, 59.198883, 0.0], [0.290264, 59.112008, 0.0], [0.203389, 58.902272, 0.0], [0.290264, 58.692536, 0.0], [0.5, 58.605661, 0.0], [0.709736, 58.692536, 0.0], [0.796611, 58.902272, 0.0]]}]},
			"L_legBase_CTL": {"color": 14, "shapes": [{"shapeName": "L_legBase_CTLShape", "degree": 3, "form": 0, "points": [[1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.54488, 0.24561], [1.0, 9.594556, 0.643012], [1.0, 9.61353, 0.794807], [1.941622, 9.594556, 0.643012], [2.523577, 9.54488, 0.24561], [2.523577, 9.483478, -0.24561], [1.941622, 9.433803, -0.643012], [1.0, 9.414828, -0.794807], [1.0, 9.433803, -0.643012], [1.0, 9.483478, -0.24561], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0], [1.0, 9.514179, 0.0]]}]},
			"L_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_C_CTLShape", "degree": 3, "form": 2, "points": [[7.915627, 15.262349, -0.117542], [7.925, 15.379517, -0.166229], [7.934374, 15.496684, -0.117542], [7.938256, 15.545216, -0.0], [7.934374, 15.496684, 0.117542], [7.925, 15.379517, 0.166229], [7.915627, 15.262349, 0.117542], [7.911744, 15.213817, -0.0]]}]},
			"L_clavicle_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_clavicle_B_OFF_CTLShape", "degree": 3, "form": 0, "points": [[2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.362855, 15.299517, -0.312618], [2.66681, 15.299517, -0.413937], [2.782911, 15.299517, -0.452637], [2.428596, 15.299517, -1.128577], [1.977417, 15.299517, -1.468932], [1.601707, 15.299517, -1.343695], [1.444976, 15.299517, -0.800704], [1.567089, 15.299517, -0.047363], [1.68319, 15.299517, -0.086063], [1.987145, 15.299517, -0.187382], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25]]}]},
			"L_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.675883, 15.257988, 1.258419], [8.669918, 15.253956, 1.27197], [8.670458, 15.239194, 1.267816], [8.676423, 15.243225, 1.254264], [8.675883, 15.257988, 1.258419], [8.68316, 15.247786, 1.267275], [8.670458, 15.239194, 1.267816], [8.66318, 15.249396, 1.258959], [8.669918, 15.253956, 1.27197], [8.68316, 15.247786, 1.267275], [8.676423, 15.243225, 1.254264], [8.66318, 15.249396, 1.258959], [8.675883, 15.257988, 1.258419], [8.68316, 15.247786, 1.267275], [7.7307, 15.324517, 0.870833]]}, {"shapeName": "L_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[7.426562, 15.840087, 1.70132], [7.413859, 15.831494, 1.70186], [7.421136, 15.821292, 1.710717], [7.433839, 15.829885, 1.710177], [7.426562, 15.840087, 1.70132], [7.420597, 15.836054, 1.714871], [7.421136, 15.821292, 1.710717], [7.427102, 15.825324, 1.697165], [7.413859, 15.831494, 1.70186], [7.420597, 15.836054, 1.714871], [7.433839, 15.829885, 1.710177], [7.427102, 15.825324, 1.697165], [7.426562, 15.840087, 1.70132], [7.420597, 15.836054, 1.714871], [7.7307, 15.324517, 0.870833]]}, {"shapeName": "L_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[7.471529, 14.443357, 1.322949], [7.464792, 14.438796, 1.309938], [7.478035, 14.432626, 1.305243], [7.484772, 14.437187, 1.318254], [7.471529, 14.443357, 1.322949], [7.47207, 14.428595, 1.318794], [7.478035, 14.432626, 1.305243], [7.477495, 14.447389, 1.309397], [7.464792, 14.438796, 1.309938], [7.47207, 14.428595, 1.318794], [7.484772, 14.437187, 1.318254], [7.477495, 14.447389, 1.309397], [7.471529, 14.443357, 1.322949], [7.47207, 14.428595, 1.318794], [7.7307, 15.324517, 0.870833]]}]},
			"L_upArm_shaper_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upArm_shaper_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[4.715475, 15.299517, -0.458804], [4.718107, 15.310368, -0.448277], [4.720739, 15.299517, -0.43775], [4.718107, 15.288666, -0.448277], [4.715475, 15.299517, -0.458804], [4.728633, 15.299517, -0.450908], [4.720739, 15.299517, -0.43775], [4.70758, 15.299517, -0.445645], [4.718107, 15.310368, -0.448277], [4.728633, 15.299517, -0.450908], [4.718107, 15.288666, -0.448277], [4.70758, 15.299517, -0.445645], [4.715475, 15.299517, -0.458804], [4.728633, 15.299517, -0.450908], [3.725, 15.299517, -0.2]]}, {"shapeName": "L_upArm_shaper_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[3.722368, 16.323188, -0.210527], [3.714473, 16.323188, -0.197368], [3.727632, 16.323188, -0.189473], [3.735527, 16.323188, -0.202632], [3.722368, 16.323188, -0.210527], [3.725, 16.334038, -0.2], [3.727632, 16.323188, -0.189473], [3.725, 16.312337, -0.2], [3.714473, 16.323188, -0.197368], [3.725, 16.334038, -0.2], [3.735527, 16.323188, -0.202632], [3.725, 16.312337, -0.2], [3.722368, 16.323188, -0.210527], [3.725, 16.334038, -0.2], [3.725, 15.299517, -0.2]]}, {"shapeName": "L_upArm_shaper_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[3.973277, 15.310368, 0.793107], [3.96275, 15.299517, 0.795738], [3.973277, 15.288666, 0.793107], [3.983804, 15.299517, 0.790475], [3.973277, 15.310368, 0.793107], [3.975908, 15.299517, 0.803633], [3.973277, 15.288666, 0.793107], [3.970645, 15.299517, 0.78258], [3.96275, 15.299517, 0.795738], [3.975908, 15.299517, 0.803633], [3.983804, 15.299517, 0.790475], [3.970645, 15.299517, 0.78258], [3.973277, 15.310368, 0.793107], [3.975908, 15.299517, 0.803633], [3.725, 15.299517, -0.2]]}]},
			"L_loLeg_shaper_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_loLeg_shaper_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 3.699759, 0.262262], [1.010851, 3.698413, 0.273029], [1.0, 3.697067, 0.283796], [0.989149, 3.698413, 0.273029], [1.0, 3.699759, 0.262262], [1.0, 3.687647, 0.271683], [1.0, 3.697067, 0.283796], [1.0, 3.70918, 0.274375], [1.010851, 3.698413, 0.273029], [1.0, 3.687647, 0.271683], [0.989149, 3.698413, 0.273029], [1.0, 3.70918, 0.274375], [1.0, 3.699759, 0.262262], [1.0, 3.687647, 0.271683], [1.0, 4.714179, 0.4]]}, {"shapeName": "L_loLeg_shaper_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.023671, 4.715525, 0.389233], [2.023671, 4.724946, 0.401346], [2.023671, 4.712833, 0.410767], [2.023671, 4.703412, 0.398654], [2.023671, 4.715525, 0.389233], [2.034521, 4.714179, 0.4], [2.023671, 4.712833, 0.410767], [2.01282, 4.714179, 0.4], [2.023671, 4.724946, 0.401346], [2.034521, 4.714179, 0.4], [2.023671, 4.703412, 0.398654], [2.01282, 4.714179, 0.4], [2.023671, 4.715525, 0.389233], [2.034521, 4.714179, 0.4], [1.0, 4.714179, 0.4]]}, {"shapeName": "L_loLeg_shaper_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.010851, 4.587208, 1.415766], [1.0, 4.597976, 1.417112], [0.989149, 4.587208, 1.415766], [1.0, 4.576441, 1.41442], [1.010851, 4.587208, 1.415766], [1.0, 4.585863, 1.426532], [0.989149, 4.587208, 1.415766], [1.0, 4.588554, 1.404999], [1.0, 4.597976, 1.417112], [1.0, 4.585863, 1.426532], [1.0, 4.576441, 1.41442], [1.0, 4.588554, 1.404999], [1.010851, 4.587208, 1.415766], [1.0, 4.585863, 1.426532], [1.0, 4.714179, 0.4]]}]},
			"L_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_D_CTLShape", "degree": 3, "form": 2, "points": [[8.284465, 15.233006, 0.132458], [8.3, 15.349517, 0.083771], [8.315535, 15.466027, 0.132458], [8.32197, 15.514288, 0.25], [8.315535, 15.466027, 0.367542], [8.3, 15.349517, 0.416229], [8.284465, 15.233006, 0.367542], [8.278031, 15.184746, 0.25]]}]},
			"L_loArm_shaper_D_CTL": {"color": 4, "shapes": [{"shapeName": "L_loArm_shaper_D_CTLShape", "degree": 1, "form": 0, "points": [[6.525, 16.799517, -0.1], [6.599251, 16.810935, -0.081437], [6.662198, 16.843452, -0.065701], [6.704259, 16.892115, -0.055185], [6.719029, 16.949517, -0.051493], [6.704259, 17.006919, -0.055185], [6.662198, 17.055582, -0.065701], [6.599251, 17.088099, -0.081437], [6.525, 17.099517, -0.1], [6.450749, 17.088099, -0.118563], [6.387802, 17.055582, -0.134299], [6.345741, 17.006919, -0.144815], [6.330972, 16.949517, -0.148507], [6.345741, 16.892115, -0.144815], [6.387802, 16.843452, -0.134299], [6.450749, 16.810935, -0.118563], [6.525, 16.799517, -0.1], [6.525, 15.299517, -0.1]]}]},
			"L_bendyArm_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_bendyArm_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.948671, 15.299517, -0.510851], [5.948671, 15.310368, -0.5], [5.948671, 15.299517, -0.489149], [5.948671, 15.288666, -0.5], [5.948671, 15.299517, -0.510851], [5.959521, 15.299517, -0.5], [5.948671, 15.299517, -0.489149], [5.93782, 15.299517, -0.5], [5.948671, 15.310368, -0.5], [5.959521, 15.299517, -0.5], [5.948671, 15.288666, -0.5], [5.93782, 15.299517, -0.5], [5.948671, 15.299517, -0.510851], [5.959521, 15.299517, -0.5], [4.925, 15.299517, -0.5]]}, {"shapeName": "L_bendyArm_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[4.925, 16.323188, -0.510851], [4.914149, 16.323188, -0.5], [4.925, 16.323188, -0.489149], [4.935851, 16.323188, -0.5], [4.925, 16.323188, -0.510851], [4.925, 16.334038, -0.5], [4.925, 16.323188, -0.489149], [4.925, 16.312337, -0.5], [4.914149, 16.323188, -0.5], [4.925, 16.334038, -0.5], [4.935851, 16.323188, -0.5], [4.925, 16.312337, -0.5], [4.925, 16.323188, -0.510851], [4.925, 16.334038, -0.5], [4.925, 15.299517, -0.5]]}, {"shapeName": "L_bendyArm_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[4.925, 15.310368, 0.523671], [4.914149, 15.299517, 0.523671], [4.925, 15.288666, 0.523671], [4.935851, 15.299517, 0.523671], [4.925, 15.310368, 0.523671], [4.925, 15.299517, 0.534521], [4.925, 15.288666, 0.523671], [4.925, 15.299517, 0.51282], [4.914149, 15.299517, 0.523671], [4.925, 15.299517, 0.534521], [4.935851, 15.299517, 0.523671], [4.925, 15.299517, 0.51282], [4.925, 15.310368, 0.523671], [4.925, 15.299517, 0.534521], [4.925, 15.299517, -0.5]]}]},
			"L_wrist_IK_CTL": {"color": 6, "shapes": [{"shapeName": "L_wrist_IK_CTLShape", "degree": 1, "form": 0, "points": [[7.425, 15.799517, -0.5], [7.425, 15.799517, 0.5], [7.425, 14.799517, 0.5], [7.425, 14.799517, -0.5], [7.425, 15.799517, -0.5]]}]},
			"L_upLeg_shaper_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_shaper_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 7.697067, 0.216204], [1.010851, 7.698413, 0.226971], [1.0, 7.699759, 0.237738], [0.989149, 7.698413, 0.226971], [1.0, 7.697067, 0.216204], [1.0, 7.687647, 0.228317], [1.0, 7.699759, 0.237738], [1.0, 7.70918, 0.225625], [1.010851, 7.698413, 0.226971], [1.0, 7.687647, 0.228317], [0.989149, 7.698413, 0.226971], [1.0, 7.70918, 0.225625], [1.0, 7.697067, 0.216204], [1.0, 7.687647, 0.228317], [1.0, 8.714179, 0.1]]}, {"shapeName": "L_upLeg_shaper_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.023671, 8.712833, 0.089233], [2.023671, 8.724946, 0.098654], [2.023671, 8.715525, 0.110767], [2.023671, 8.703412, 0.101346], [2.023671, 8.712833, 0.089233], [2.034521, 8.714179, 0.1], [2.023671, 8.715525, 0.110767], [2.01282, 8.714179, 0.1], [2.023671, 8.724946, 0.098654], [2.034521, 8.714179, 0.1], [2.023671, 8.703412, 0.101346], [2.01282, 8.714179, 0.1], [2.023671, 8.712833, 0.089233], [2.034521, 8.714179, 0.1], [1.0, 8.714179, 0.1]]}, {"shapeName": "L_upLeg_shaper_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.010851, 8.84115, 1.115766], [1.0, 8.851917, 1.11442], [0.989149, 8.84115, 1.115766], [1.0, 8.830383, 1.117112], [1.010851, 8.84115, 1.115766], [1.0, 8.842496, 1.126532], [0.989149, 8.84115, 1.115766], [1.0, 8.839804, 1.104999], [1.0, 8.851917, 1.11442], [1.0, 8.842496, 1.126532], [1.0, 8.830383, 1.117112], [1.0, 8.839804, 1.104999], [1.010851, 8.84115, 1.115766], [1.0, 8.842496, 1.126532], [1.0, 8.714179, 0.1]]}]},
			"L_clavicle_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_clavicle_A_OFF_CTLShape", "degree": 3, "form": 0, "points": [[2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.386337, 15.299517, -0.320446], [2.728286, 15.299517, -0.434429], [2.858899, 15.299517, -0.477966], [2.460296, 15.299517, -1.2384], [1.95272, 15.299517, -1.621299], [1.530045, 15.299517, -1.480407], [1.353724, 15.299517, -0.869542], [1.491101, 15.299517, -0.022034], [1.621714, 15.299517, -0.065571], [1.963663, 15.299517, -0.179554], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25], [2.175, 15.299517, -0.25]]}]},
			"C_jaw_CTL": {"color": 18, "shapes": [{"shapeName": "C_jaw_CTLShape", "degree": 3, "form": 0, "points": [[0.0, 20.556285, 0.5], [0.0, 20.556285, 0.5], [0.0, 20.556285, 0.5], [-0.330028, 20.556285, 0.5], [-0.864022, 20.556285, 0.5], [-1.06799, 20.556285, 0.5], [-0.864022, 20.556285, 2.06937], [-0.330028, 20.556285, 3.039295], [0.330028, 20.556285, 3.039295], [0.864022, 20.556285, 2.06937], [1.06799, 20.556285, 0.5], [0.864022, 20.556285, 0.5], [0.330028, 20.556285, 0.5], [0.0, 20.556285, 0.5], [0.0, 20.556285, 0.5], [0.0, 20.556285, 0.5]]}]},
			"L_upLeg_shaper_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upLeg_shaper_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.0, 6.097067, 0.416204], [1.010851, 6.098413, 0.426971], [1.0, 6.099759, 0.437738], [0.989149, 6.098413, 0.426971], [1.0, 6.097067, 0.416204], [1.0, 6.087647, 0.428317], [1.0, 6.099759, 0.437738], [1.0, 6.10918, 0.425625], [1.010851, 6.098413, 0.426971], [1.0, 6.087647, 0.428317], [0.989149, 6.098413, 0.426971], [1.0, 6.10918, 0.425625], [1.0, 6.097067, 0.416204], [1.0, 6.087647, 0.428317], [1.0, 7.114179, 0.3]]}, {"shapeName": "L_upLeg_shaper_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.023671, 7.112833, 0.289233], [2.023671, 7.124946, 0.298654], [2.023671, 7.115525, 0.310767], [2.023671, 7.103412, 0.301346], [2.023671, 7.112833, 0.289233], [2.034521, 7.114179, 0.3], [2.023671, 7.115525, 0.310767], [2.01282, 7.114179, 0.3], [2.023671, 7.124946, 0.298654], [2.034521, 7.114179, 0.3], [2.023671, 7.103412, 0.301346], [2.01282, 7.114179, 0.3], [2.023671, 7.112833, 0.289233], [2.034521, 7.114179, 0.3], [1.0, 7.114179, 0.3]]}, {"shapeName": "L_upLeg_shaper_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.010851, 7.24115, 1.315766], [1.0, 7.251917, 1.31442], [0.989149, 7.24115, 1.315766], [1.0, 7.230383, 1.317112], [1.010851, 7.24115, 1.315766], [1.0, 7.242496, 1.326532], [0.989149, 7.24115, 1.315766], [1.0, 7.239804, 1.304999], [1.0, 7.251917, 1.31442], [1.0, 7.242496, 1.326532], [1.0, 7.230383, 1.317112], [1.0, 7.239804, 1.304999], [1.010851, 7.24115, 1.315766], [1.0, 7.242496, 1.326532], [1.0, 7.114179, 0.3]]}]},
			"C_neckBase_D_OFF_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "C_neckBase_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.846301, 18.556285, -0.705251], [0.0, 18.196285, -0.997375], [-0.846301, 18.556285, -0.705251], [-1.19685, 18.916285, 0.0], [-0.846301, 18.556285, 0.705251], [0.0, 18.196285, 0.997375], [0.846301, 18.556285, 0.705251], [1.19685, 18.916285, 0.0]]}]},
			"C_reverseJaw_CTL": {"color": 18, "shapes": [{"shapeName": "C_reverseJaw_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 22.556285, 0.5], [0.076536, 22.571509, 0.5], [0.14142, 22.614865, 0.5], [0.184776, 22.679749, 0.5], [0.2, 22.756285, 0.5], [0.184776, 22.832821, 0.5], [0.14142, 22.897705, 0.5], [0.076536, 22.941061, 0.5], [0.0, 22.956285, 0.5], [-0.076536, 22.941061, 0.5], [-0.14142, 22.897705, 0.5], [-0.184776, 22.832821, 0.5], [-0.2, 22.756285, 0.5], [-0.184776, 22.679749, 0.5], [-0.14142, 22.614865, 0.5], [-0.076536, 22.571509, 0.5], [0.0, 22.556285, 0.5], [0.0, 20.556285, 0.5]]}]},
			"L_toe_IK_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_toe_IK_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.315225, 0.499994, 1.0], [1.00178, 0.629827, 1.0], [0.688335, 0.499994, 1.0], [0.558503, 0.186549, 1.0], [0.688335, -0.126896, 1.0], [1.00178, -0.256729, 1.0], [1.315225, -0.126896, 1.0], [1.445058, 0.186549, 1.0]]}]},
			"L_upArm_shaper_C_CTL": {"color": 4, "shapes": [{"shapeName": "L_upArm_shaper_C_CTLShape", "degree": 1, "form": 0, "points": [[4.125, 16.799517, -0.3], [4.199251, 16.810935, -0.318563], [4.262198, 16.843452, -0.334299], [4.304259, 16.892115, -0.344815], [4.319029, 16.949517, -0.348507], [4.304259, 17.006919, -0.344815], [4.262198, 17.055582, -0.334299], [4.199251, 17.088099, -0.318563], [4.125, 17.099517, -0.3], [4.050749, 17.088099, -0.281437], [3.987802, 17.055582, -0.265701], [3.945741, 17.006919, -0.255185], [3.930972, 16.949517, -0.251493], [3.945741, 16.892115, -0.255185], [3.987802, 16.843452, -0.265701], [4.050749, 16.810935, -0.281437], [4.125, 16.799517, -0.3], [4.125, 15.299517, -0.3]]}]},
		}

		controlShapes.set_data(data)