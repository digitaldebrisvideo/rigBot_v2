# -*- rigBot: assembly -*-
from rigBot import guide
from rigBot.data import controlShapes
import maya.cmds as mc

class Generic_face():
	"""Generated assembly build."""

	def __init__(self):
		pass

	def build_guide(self):
		"""Build Assembly guide parts"""

		guide.build("worldRoot", **{'side': u'C', 'name': u''})
		guide.build("eye", **{'name': u'', 'parent': u'C_head_JNT', 'pickWalkParent': u'C_lookAt_CTL', 'centerLookAtControl': u'C_lookAt_CTL', 'eyeBallCenter': [], 'createSquashCtrl': False, 'pupilCenter': [], 'side': u'R'})
		guide.build("eyeLid", **{'eyeJoint': u'R_eye_A_JNT', 'parent': u'C_head_JNT', 'lowerLidEdgeLoop': [], 'eyeCtrl': u'R_eye_FK_CTL', 'numberJoints': 7, 'side': u'R', 'upperLidEdgeLoop': [], 'name': u''})
		guide.build("cheek", **{'numberPrimaryCtrls': 3, 'parent': u'C_head_JNT', 'pickWalkParent': u'C_head_CTL', 'jawParent': u'C_jaw_JNT', 'numberLowerCtrls': 3, 'side': u'R', 'createSquintControls': True, 'name': u''})
		guide.build("eye", **{'name': u'', 'parent': u'C_head_JNT', 'pickWalkParent': u'C_lookAt_CTL', 'centerLookAtControl': u'C_lookAt_CTL', 'eyeBallCenter': [], 'createSquashCtrl': False, 'pupilCenter': [], 'side': u'L'})
		guide.build("eyeLid", **{'eyeJoint': u'L_eye_A_JNT', 'parent': u'C_head_JNT', 'lowerLidEdgeLoop': [], 'eyeCtrl': u'L_eye_FK_CTL', 'numberJoints': 7, 'side': u'L', 'upperLidEdgeLoop': [], 'name': u''})
		guide.build("cheek", **{'numberPrimaryCtrls': 3, 'parent': u'C_head_JNT', 'pickWalkParent': u'C_head_CTL', 'jawParent': u'C_jaw_JNT', 'numberLowerCtrls': 3, 'side': u'L', 'createSquintControls': True, 'name': u''})
		guide.build("tongue", **{'addVolumeControls': True, 'name': u'', 'parent': u'C_jaw_JNT', 'addCurl': True, 'pickWalkParent': u'C_jaw_CTL', 'createFkCtrls': True, 'shiftJoints': 0.0, 'numberCtrls': 5, 'shiftCtrls': 0.0, 'numberJoints': 8, 'side': u'C'})
		guide.build("nose", **{'name': u'', 'parent': u'C_reverseJaw_JNT', 'pickWalkParent': u'C_head_CTL', 'side': u'C', 'createMuzzleControl': False, 'createNoseTipControl': True, 'createBridgeControl': True})
		guide.build("mouth", **{'lowerLipEdgeLoop': [], 'name': u'', 'parent': u'C_reverseJaw_JNT', 'pickWalkParent': u'C_head_CTL', 'upperLipEdgeLoop': [], 'jawParent': u'C_jaw_JNT', 'createZipperControl': True, 'upperLipRollEdgeLoop': [], 'numberCtrls': 1, 'lowerLipRollEdgeLoop': [], 'numberJoints': 4, 'side': u'C'})
		guide.build("eyeLookAt", **{'pickWalkParent': u'C_head_CTL', 'side': u'C', 'parent': u'C_head_JNT', 'name': u''})
		guide.build("brow", **{'name': u'', 'parent': u'C_head_JNT', 'pickWalkParent': u'C_head_CTL', 'createUpperControls': True, 'createCenterControl': True, 'numberCtrls': 3, 'side': u'C'})

		#Position nodes
		if mc.objExists("R_eye_guide"):
			if not mc.getAttr("R_eye_guide.rotateOrder", l=1):
				mc.setAttr("R_eye_guide.rotateOrder", 0)

			mc.xform("R_eye_guide", a=1, t=[-2.0, 6.0, 0.0])
			mc.xform("R_eye_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_eye_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_eyeLid_guide"):
			if not mc.getAttr("R_eyeLid_guide.rotateOrder", l=1):
				mc.setAttr("R_eyeLid_guide.rotateOrder", 0)

			mc.xform("R_eyeLid_guide", a=1, t=[-2.0, 8.30108, 0.144183])
			mc.xform("R_eyeLid_guide", a=1, ro=[-180.0, 90.0, 0.0])
			mc.xform("R_eyeLid_guide", r=1, s=[0.38892499232410827, 0.38892499232410827, 0.38892499232410827])

		if mc.objExists("R_cheek_guide"):
			if not mc.getAttr("R_cheek_guide.rotateOrder", l=1):
				mc.setAttr("R_cheek_guide.rotateOrder", 0)

			mc.xform("R_cheek_guide", a=1, t=[-2.0, 2.59915, 0.0])
			mc.xform("R_cheek_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_cheek_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_eye_guide"):
			if not mc.getAttr("L_eye_guide.rotateOrder", l=1):
				mc.setAttr("L_eye_guide.rotateOrder", 0)

			mc.xform("L_eye_guide", a=1, t=[2.0, 6.0, 0.0])
			mc.xform("L_eye_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_eye_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_eyeLid_guide"):
			if not mc.getAttr("L_eyeLid_guide.rotateOrder", l=1):
				mc.setAttr("L_eyeLid_guide.rotateOrder", 0)

			mc.xform("L_eyeLid_guide", a=1, t=[2.0, 8.301079171062138, 0.1441827681548753])
			mc.xform("L_eyeLid_guide", a=1, ro=[0.0, -90.0, 0.0])
			mc.xform("L_eyeLid_guide", r=1, s=[0.38892499232410827, 0.38892499232410827, 0.38892499232410827])

		if mc.objExists("L_cheek_guide"):
			if not mc.getAttr("L_cheek_guide.rotateOrder", l=1):
				mc.setAttr("L_cheek_guide.rotateOrder", 0)

			mc.xform("L_cheek_guide", a=1, t=[2.0, 2.599147562012985, 0.0])
			mc.xform("L_cheek_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_worldRoot_guide"):
			if not mc.getAttr("C_worldRoot_guide.rotateOrder", l=1):
				mc.setAttr("C_worldRoot_guide.rotateOrder", 0)

			mc.xform("C_worldRoot_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_guide"):
			if not mc.getAttr("C_tongue_guide.rotateOrder", l=1):
				mc.setAttr("C_tongue_guide.rotateOrder", 0)

			mc.xform("C_tongue_guide", a=1, t=[0.0, 0.0, -3.4070655112035793])
			mc.xform("C_tongue_guide", a=1, ro=[0.0, -90.0, 0.0])
			mc.xform("C_tongue_guide", r=1, s=[0.25, 0.25, 0.25])

		if mc.objExists("C_nose_guide"):
			if not mc.getAttr("C_nose_guide.rotateOrder", l=1):
				mc.setAttr("C_nose_guide.rotateOrder", 0)

			mc.xform("C_nose_guide", a=1, t=[0.0, 5.147208056594563, -1.6137235877303506])
			mc.xform("C_nose_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_nose_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_mouth_guide"):
			if not mc.getAttr("C_mouth_guide.rotateOrder", l=1):
				mc.setAttr("C_mouth_guide.rotateOrder", 0)

			mc.xform("C_mouth_guide", a=1, t=[0.0, 0.19121653378065018, -0.39463711797601153])
			mc.xform("C_mouth_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_mouth_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_eyeLookAt_guide"):
			if not mc.getAttr("C_eyeLookAt_guide.rotateOrder", l=1):
				mc.setAttr("C_eyeLookAt_guide.rotateOrder", 0)

			mc.xform("C_eyeLookAt_guide", a=1, t=[0.0, 6.0, 3.036525831359062])
			mc.xform("C_eyeLookAt_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_eyeLookAt_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_guide"):
			if not mc.getAttr("C_brow_guide.rotateOrder", l=1):
				mc.setAttr("C_brow_guide.rotateOrder", 0)

			mc.xform("C_brow_guide", a=1, t=[0.0, 7.842624838837992, -0.9414162942782736])
			mc.xform("C_brow_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_root_JNT_PLC"):
			mc.xform("C_root_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_root_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_root_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_A_JNT_PLC"):
			mc.xform("C_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_B_JNT_PLC"):
			mc.xform("C_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_C_JNT_PLC"):
			mc.xform("C_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_D_JNT_PLC"):
			mc.xform("C_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_E_JNT_PLC"):
			mc.xform("C_E_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_F_JNT_PLC"):
			mc.xform("C_F_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_F_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_F_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_G_JNT_PLC"):
			mc.xform("C_G_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_G_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_G_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_H_JNT_PLC"):
			mc.xform("C_H_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_H_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_H_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spline_A_JNT_PLC"):
			if not mc.getAttr("C_spline_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_spline_A_JNT_PLC.rotateOrder", 0)

			mc.xform("C_spline_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spline_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spline_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spline_B_JNT_PLC"):
			if not mc.getAttr("C_spline_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_spline_B_JNT_PLC.rotateOrder", 0)

			mc.xform("C_spline_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spline_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spline_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spline_C_JNT_PLC"):
			if not mc.getAttr("C_spline_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_spline_C_JNT_PLC.rotateOrder", 0)

			mc.xform("C_spline_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spline_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spline_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spline_D_JNT_PLC"):
			if not mc.getAttr("C_spline_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_spline_D_JNT_PLC.rotateOrder", 0)

			mc.xform("C_spline_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spline_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spline_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_spline_E_JNT_PLC"):
			if not mc.getAttr("C_spline_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_spline_E_JNT_PLC.rotateOrder", 0)

			mc.xform("C_spline_E_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_spline_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_spline_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBase_JNT_PLC"):
			if not mc.getAttr("C_noseBase_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_noseBase_JNT_PLC.rotateOrder", 0)

			mc.xform("C_noseBase_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_nostril_JNT_PLC"):
			if not mc.getAttr("L_nostril_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_nostril_JNT_PLC.rotateOrder", 0)

			mc.xform("L_nostril_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_nostril_JNT_PLC"):
			if not mc.getAttr("R_nostril_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_nostril_JNT_PLC.rotateOrder", 0)

			mc.xform("R_nostril_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBridge_JNT_PLC"):
			if not mc.getAttr("C_noseBridge_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_noseBridge_JNT_PLC.rotateOrder", 0)

			mc.xform("C_noseBridge_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseTip_JNT_PLC"):
			if not mc.getAttr("C_noseTip_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_noseTip_JNT_PLC.rotateOrder", 0)

			mc.xform("C_noseTip_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLip_JNT_PLC"):
			if not mc.getAttr("C_upperLip_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_upperLip_JNT_PLC.rotateOrder", 0)

			mc.xform("C_upperLip_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLip_JNT_PLC"):
			if not mc.getAttr("C_lowerLip_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_lowerLip_JNT_PLC.rotateOrder", 0)

			mc.xform("C_lowerLip_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCorner_JNT_PLC"):
			if not mc.getAttr("R_lipCorner_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lipCorner_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lipCorner_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCorner_JNT_PLC"):
			if not mc.getAttr("L_lipCorner_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lipCorner_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lipCorner_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_D_JNT_PLC"):
			if not mc.getAttr("R_upperLip_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLip_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLip_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_C_JNT_PLC"):
			if not mc.getAttr("R_upperLip_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLip_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLip_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_B_JNT_PLC"):
			if not mc.getAttr("R_upperLip_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLip_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLip_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_A_JNT_PLC"):
			if not mc.getAttr("R_upperLip_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLip_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLip_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_D_JNT_PLC"):
			if not mc.getAttr("R_lowerLip_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLip_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_C_JNT_PLC"):
			if not mc.getAttr("R_lowerLip_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLip_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_B_JNT_PLC"):
			if not mc.getAttr("R_lowerLip_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLip_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_A_JNT_PLC"):
			if not mc.getAttr("R_lowerLip_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLip_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_A_JNT_PLC"):
			if not mc.getAttr("L_upperLip_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLip_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLip_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_B_JNT_PLC"):
			if not mc.getAttr("L_upperLip_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLip_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLip_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_C_JNT_PLC"):
			if not mc.getAttr("L_upperLip_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLip_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLip_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_D_JNT_PLC"):
			if not mc.getAttr("L_upperLip_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLip_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLip_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_A_JNT_PLC"):
			if not mc.getAttr("L_lowerLip_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLip_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_B_JNT_PLC"):
			if not mc.getAttr("L_lowerLip_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLip_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_C_JNT_PLC"):
			if not mc.getAttr("L_lowerLip_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLip_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_D_JNT_PLC"):
			if not mc.getAttr("L_lowerLip_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLip_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_D_roll_JNT_PLC"):
			if not mc.getAttr("R_upperLip_D_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLip_D_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLip_D_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_D_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_D_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_C_roll_JNT_PLC"):
			if not mc.getAttr("R_upperLip_C_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLip_C_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLip_C_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_C_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_C_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_B_roll_JNT_PLC"):
			if not mc.getAttr("R_upperLip_B_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLip_B_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLip_B_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_B_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_B_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_A_roll_JNT_PLC"):
			if not mc.getAttr("R_upperLip_A_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLip_A_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLip_A_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLip_roll_JNT_PLC"):
			if not mc.getAttr("C_upperLip_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_upperLip_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("C_upperLip_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_A_roll_JNT_PLC"):
			if not mc.getAttr("L_upperLip_A_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLip_A_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLip_A_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_B_roll_JNT_PLC"):
			if not mc.getAttr("L_upperLip_B_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLip_B_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLip_B_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_B_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_B_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_C_roll_JNT_PLC"):
			if not mc.getAttr("L_upperLip_C_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLip_C_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLip_C_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_C_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_C_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_D_roll_JNT_PLC"):
			if not mc.getAttr("L_upperLip_D_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLip_D_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLip_D_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_D_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_D_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_D_roll_JNT_PLC"):
			if not mc.getAttr("R_lowerLip_D_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_D_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLip_D_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_D_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_D_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_C_roll_JNT_PLC"):
			if not mc.getAttr("R_lowerLip_C_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_C_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLip_C_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_C_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_C_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_B_roll_JNT_PLC"):
			if not mc.getAttr("R_lowerLip_B_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_B_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLip_B_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_B_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_B_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_A_roll_JNT_PLC"):
			if not mc.getAttr("R_lowerLip_A_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_A_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLip_A_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLip_roll_JNT_PLC"):
			if not mc.getAttr("C_lowerLip_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_lowerLip_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("C_lowerLip_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_A_roll_JNT_PLC"):
			if not mc.getAttr("L_lowerLip_A_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_A_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLip_A_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_B_roll_JNT_PLC"):
			if not mc.getAttr("L_lowerLip_B_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_B_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLip_B_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_B_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_B_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_C_roll_JNT_PLC"):
			if not mc.getAttr("L_lowerLip_C_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_C_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLip_C_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_C_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_C_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_D_roll_JNT_PLC"):
			if not mc.getAttr("L_lowerLip_D_roll_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_D_roll_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLip_D_roll_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_D_roll_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_D_roll_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_eye_A_JNT_PLC"):
			if not mc.getAttr("L_eye_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_eye_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_eye_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_eye_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_eye_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_eye_B_JNT_PLC"):
			if not mc.getAttr("L_eye_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_eye_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_eye_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_eye_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_eye_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_innerLid_JNT_PLC"):
			if not mc.getAttr("L_innerLid_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_innerLid_JNT_PLC.rotateOrder", 0)

			mc.xform("L_innerLid_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterLid_JNT_PLC"):
			if not mc.getAttr("L_outterLid_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_outterLid_JNT_PLC.rotateOrder", 0)

			mc.xform("L_outterLid_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_eyeLidBase_JNT_PLC"):
			if not mc.getAttr("L_eyeLidBase_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_eyeLidBase_JNT_PLC.rotateOrder", 0)

			mc.xform("L_eyeLidBase_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_eyeLidBase_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_eyeLidBase_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_A_JNT_PLC"):
			if not mc.getAttr("L_upperLid_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLid_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLid_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_B_JNT_PLC"):
			if not mc.getAttr("L_upperLid_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLid_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLid_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_C_JNT_PLC"):
			if not mc.getAttr("L_upperLid_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLid_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLid_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_D_JNT_PLC"):
			if not mc.getAttr("L_upperLid_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLid_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLid_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_E_JNT_PLC"):
			if not mc.getAttr("L_upperLid_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLid_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLid_E_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_F_JNT_PLC"):
			if not mc.getAttr("L_upperLid_F_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLid_F_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLid_F_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_F_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_F_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_G_JNT_PLC"):
			if not mc.getAttr("L_upperLid_G_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_upperLid_G_JNT_PLC.rotateOrder", 0)

			mc.xform("L_upperLid_G_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_G_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_G_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_A_JNT_PLC"):
			if not mc.getAttr("L_lowerLid_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLid_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_B_JNT_PLC"):
			if not mc.getAttr("L_lowerLid_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLid_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_C_JNT_PLC"):
			if not mc.getAttr("L_lowerLid_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLid_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_D_JNT_PLC"):
			if not mc.getAttr("L_lowerLid_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_D_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLid_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_D_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_E_JNT_PLC"):
			if not mc.getAttr("L_lowerLid_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_E_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLid_E_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_E_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_F_JNT_PLC"):
			if not mc.getAttr("L_lowerLid_F_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_F_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLid_F_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_F_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_F_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_G_JNT_PLC"):
			if not mc.getAttr("L_lowerLid_G_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_G_JNT_PLC.rotateOrder", 0)

			mc.xform("L_lowerLid_G_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_G_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_G_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_A_JNT_PLC"):
			if not mc.getAttr("L_cheek_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_cheek_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_cheek_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_B_JNT_PLC"):
			if not mc.getAttr("L_cheek_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_cheek_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_cheek_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_C_JNT_PLC"):
			if not mc.getAttr("L_cheek_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_cheek_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_cheek_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_A_JNT_PLC"):
			if not mc.getAttr("L_squint_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_squint_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_squint_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_squint_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_B_JNT_PLC"):
			if not mc.getAttr("L_squint_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_squint_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_squint_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_squint_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_C_JNT_PLC"):
			if not mc.getAttr("L_squint_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_squint_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_squint_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_squint_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_A_JNT_PLC"):
			if not mc.getAttr("L_cheekLower_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_cheekLower_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_B_JNT_PLC"):
			if not mc.getAttr("L_cheekLower_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_cheekLower_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_C_JNT_PLC"):
			if not mc.getAttr("L_cheekLower_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_cheekLower_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_JNT_PLC"):
			if not mc.getAttr("C_brow_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_brow_JNT_PLC.rotateOrder", 0)

			mc.xform("C_brow_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_brow_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_A_JNT_PLC"):
			if not mc.getAttr("L_brow_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_brow_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_brow_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_B_JNT_PLC"):
			if not mc.getAttr("L_brow_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_brow_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_brow_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_C_JNT_PLC"):
			if not mc.getAttr("L_brow_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_brow_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_brow_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_A_JNT_PLC"):
			if not mc.getAttr("R_brow_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_brow_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_brow_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_B_JNT_PLC"):
			if not mc.getAttr("R_brow_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_brow_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_brow_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_C_JNT_PLC"):
			if not mc.getAttr("R_brow_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_brow_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_brow_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_upper_JNT_PLC"):
			if not mc.getAttr("C_brow_upper_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("C_brow_upper_JNT_PLC.rotateOrder", 0)

			mc.xform("C_brow_upper_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_brow_upper_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_upper_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_A_JNT_PLC"):
			if not mc.getAttr("L_brow_upper_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_A_JNT_PLC.rotateOrder", 0)

			mc.xform("L_brow_upper_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_B_JNT_PLC"):
			if not mc.getAttr("L_brow_upper_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_B_JNT_PLC.rotateOrder", 0)

			mc.xform("L_brow_upper_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_C_JNT_PLC"):
			if not mc.getAttr("L_brow_upper_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_C_JNT_PLC.rotateOrder", 0)

			mc.xform("L_brow_upper_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_upper_A_JNT_PLC"):
			if not mc.getAttr("R_brow_upper_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_brow_upper_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_A_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_upper_B_JNT_PLC"):
			if not mc.getAttr("R_brow_upper_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_brow_upper_B_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_B_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_upper_C_JNT_PLC"):
			if not mc.getAttr("R_brow_upper_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_brow_upper_C_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_C_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_eye_A_JNT_PLC"):
			if not mc.getAttr("R_eye_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_eye_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_eye_A_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_eye_A_JNT_PLC", a=1, ro=[7.016709298534876e-15, -0.0, 180.0])
			mc.xform("R_eye_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_eye_B_JNT_PLC"):
			if not mc.getAttr("R_eye_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_eye_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_eye_B_JNT_PLC", a=1, t=[1.0, 0.0, 0.0])
			mc.xform("R_eye_B_JNT_PLC", a=1, ro=[7.016709298534876e-15, -0.0, 180.0])
			mc.xform("R_eye_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_innerLid_JNT_PLC"):
			if not mc.getAttr("R_innerLid_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_innerLid_JNT_PLC.rotateOrder", 0)

			mc.xform("R_innerLid_JNT_PLC", a=1, t=[3.8285145706428323, -1.1841705394033397e-07, -1.1102230246251565e-16])
			mc.xform("R_innerLid_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_innerLid_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_outterLid_JNT_PLC"):
			if not mc.getAttr("R_outterLid_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_outterLid_JNT_PLC.rotateOrder", 0)

			mc.xform("R_outterLid_JNT_PLC", a=1, t=[-4.171472652352524, -1.1841705394033397e-07, -1.1102230246251565e-16])
			mc.xform("R_outterLid_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_outterLid_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_eyeLidBase_JNT_PLC"):
			if not mc.getAttr("R_eyeLidBase_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_eyeLidBase_JNT_PLC.rotateOrder", 0)

			mc.xform("R_eyeLidBase_JNT_PLC", a=1, t=[1.1102230246251565e-16, 3.552713678800501e-15, -8.881784197001252e-16])
			mc.xform("R_eyeLidBase_JNT_PLC", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_eyeLidBase_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_A_JNT_PLC"):
			if not mc.getAttr("R_upperLid_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLid_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLid_A_JNT_PLC", a=1, t=[2.957324026247156, -8.361237586740344e-07, -1.1102230246251565e-16])
			mc.xform("R_upperLid_A_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_upperLid_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_B_JNT_PLC"):
			if not mc.getAttr("R_upperLid_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLid_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLid_B_JNT_PLC", a=1, t=[2.033772101156843, 4.274344203025748e-06, -1.1102230246251565e-16])
			mc.xform("R_upperLid_B_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_upperLid_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_C_JNT_PLC"):
			if not mc.getAttr("R_upperLid_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLid_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLid_C_JNT_PLC", a=1, t=[1.007335987448228, 6.370793528276408e-07, -5.551115123125783e-17])
			mc.xform("R_upperLid_C_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_upperLid_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_D_JNT_PLC"):
			if not mc.getAttr("R_upperLid_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLid_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLid_D_JNT_PLC", a=1, t=[-0.1714726128801738, -8.129208580953673e-06, -1.1102230246251565e-16])
			mc.xform("R_upperLid_D_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_upperLid_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_E_JNT_PLC"):
			if not mc.getAttr("R_upperLid_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLid_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLid_E_JNT_PLC", a=1, t=[-1.350306925107264, 6.370793528276408e-07, -5.551115123125783e-17])
			mc.xform("R_upperLid_E_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_upperLid_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_F_JNT_PLC"):
			if not mc.getAttr("R_upperLid_F_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLid_F_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLid_F_JNT_PLC", a=1, t=[-2.376730182866534, 4.274344203025748e-06, -1.1102230246251565e-16])
			mc.xform("R_upperLid_F_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_upperLid_F_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_G_JNT_PLC"):
			if not mc.getAttr("R_upperLid_G_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_upperLid_G_JNT_PLC.rotateOrder", 0)

			mc.xform("R_upperLid_G_JNT_PLC", a=1, t=[-3.300292392716322, -8.361237586740344e-07, -1.1102230246251565e-16])
			mc.xform("R_upperLid_G_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_upperLid_G_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_A_JNT_PLC"):
			if not mc.getAttr("R_lowerLid_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLid_A_JNT_PLC", a=1, t=[2.9573240262471563, 5.992896490170097e-07, -5.551115123125783e-17])
			mc.xform("R_lowerLid_A_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_lowerLid_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_B_JNT_PLC"):
			if not mc.getAttr("R_lowerLid_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLid_B_JNT_PLC", a=1, t=[2.033772101156843, -4.511178310906416e-06, -5.551115123125783e-17])
			mc.xform("R_lowerLid_B_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_lowerLid_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_C_JNT_PLC"):
			if not mc.getAttr("R_lowerLid_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLid_C_JNT_PLC", a=1, t=[1.007335987448227, -8.739134624846656e-07, -5.551115123125783e-17])
			mc.xform("R_lowerLid_C_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_lowerLid_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_D_JNT_PLC"):
			if not mc.getAttr("R_lowerLid_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLid_D_JNT_PLC", a=1, t=[-0.17147261288017335, 7.892374471296648e-06, -5.551115123125783e-17])
			mc.xform("R_lowerLid_D_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_lowerLid_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_E_JNT_PLC"):
			if not mc.getAttr("R_lowerLid_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLid_E_JNT_PLC", a=1, t=[-1.350306925107263, -8.739134624846656e-07, -5.551115123125783e-17])
			mc.xform("R_lowerLid_E_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_lowerLid_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_F_JNT_PLC"):
			if not mc.getAttr("R_lowerLid_F_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_F_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLid_F_JNT_PLC", a=1, t=[-2.376730182866534, -4.511178310906416e-06, -5.551115123125783e-17])
			mc.xform("R_lowerLid_F_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_lowerLid_F_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_G_JNT_PLC"):
			if not mc.getAttr("R_lowerLid_G_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_G_JNT_PLC.rotateOrder", 0)

			mc.xform("R_lowerLid_G_JNT_PLC", a=1, t=[-3.300292392716322, 5.992896490170097e-07, -5.551115123125783e-17])
			mc.xform("R_lowerLid_G_JNT_PLC", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_lowerLid_G_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_A_JNT_PLC"):
			if not mc.getAttr("R_cheek_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_cheek_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_cheek_A_JNT_PLC", a=1, t=[2.883720211510621e-06, -4.303467255439841e-06, -1.3577746332815721e-06])
			mc.xform("R_cheek_A_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 180.0, 0.0])
			mc.xform("R_cheek_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_B_JNT_PLC"):
			if not mc.getAttr("R_cheek_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_cheek_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_cheek_B_JNT_PLC", a=1, t=[6.363961031485843e-07, -4.53912609854612e-06, 1.388939275814849e-07])
			mc.xform("R_cheek_B_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_cheek_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_C_JNT_PLC"):
			if not mc.getAttr("R_cheek_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_cheek_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_cheek_C_JNT_PLC", a=1, t=[6.847477507232469e-07, -2.9762474156314056e-06, -7.69861188354426e-07])
			mc.xform("R_cheek_C_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_cheek_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_A_JNT_PLC"):
			if not mc.getAttr("R_squint_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_squint_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_squint_A_JNT_PLC", a=1, t=[1.6842711307862857e-06, -9.25790903938406e-07, -1.044793113136322e-06])
			mc.xform("R_squint_A_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_squint_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_B_JNT_PLC"):
			if not mc.getAttr("R_squint_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_squint_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_squint_B_JNT_PLC", a=1, t=[3.0405591591176062e-06, -3.974199305201154e-06, -2.776475223953412e-06])
			mc.xform("R_squint_B_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_squint_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_C_JNT_PLC"):
			if not mc.getAttr("R_squint_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_squint_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_squint_C_JNT_PLC", a=1, t=[-4.295509214991e-08, 3.503556198936053e-06, -1.031168575860164e-06])
			mc.xform("R_squint_C_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 180.0, 0.0])
			mc.xform("R_squint_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_A_JNT_PLC"):
			if not mc.getAttr("R_cheekLower_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_cheekLower_A_JNT_PLC", a=1, t=[-2.3066694938567167e-06, -2.7799329087585534e-06, 2.7191015353755787e-06])
			mc.xform("R_cheekLower_A_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_cheekLower_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_B_JNT_PLC"):
			if not mc.getAttr("R_cheekLower_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_cheekLower_B_JNT_PLC", a=1, t=[-7.07106781128175e-07, -3.956806215121844e-06, 2.3163809034221217e-06])
			mc.xform("R_cheekLower_B_JNT_PLC", a=1, ro=[0.0, 180.0, 0.0])
			mc.xform("R_cheekLower_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_C_JNT_PLC"):
			if not mc.getAttr("R_cheekLower_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_cheekLower_C_JNT_PLC", a=1, t=[9.76065630542422e-08, -3.58314947046523e-06, 8.788330507769615e-08])
			mc.xform("R_cheekLower_C_JNT_PLC", a=1, ro=[-2.5444437451708134e-14, 180.0, 0.0])
			mc.xform("R_cheekLower_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_world_PIV_CTL"):
			mc.xform("C_world_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_world_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_world_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_visibility_PIV_CTL"):
			mc.xform("C_visibility_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_visibility_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_visibility_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_A_PIV_CTL"):
			mc.xform("C_tongue_IK_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_B_PIV_CTL"):
			mc.xform("C_tongue_IK_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_C_PIV_CTL"):
			mc.xform("C_tongue_IK_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_D_PIV_CTL"):
			mc.xform("C_tongue_IK_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_E_PIV_CTL"):
			mc.xform("C_tongue_IK_E_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_A_PIV_CTL"):
			mc.xform("C_tongue_FK_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_B_PIV_CTL"):
			mc.xform("C_tongue_FK_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_C_PIV_CTL"):
			mc.xform("C_tongue_FK_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_D_PIV_CTL"):
			mc.xform("C_tongue_FK_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_E_PIV_CTL"):
			mc.xform("C_tongue_FK_E_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_E_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_E_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_F_PIV_CTL"):
			mc.xform("C_tongue_FK_F_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_F_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_F_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_G_PIV_CTL"):
			mc.xform("C_tongue_FK_G_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_G_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_G_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_H_PIV_CTL"):
			mc.xform("C_tongue_FK_H_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_H_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_H_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBase_PIV_CTL"):
			if not mc.getAttr("C_noseBase_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBase_PIV_CTL.rotateOrder", 0)

			mc.xform("C_noseBase_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_nostril_PIV_CTL"):
			if not mc.getAttr("L_nostril_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_nostril_PIV_CTL.rotateOrder", 0)

			mc.xform("L_nostril_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_nostril_PIV_CTL"):
			if not mc.getAttr("R_nostril_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_nostril_PIV_CTL.rotateOrder", 0)

			mc.xform("R_nostril_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_PIV_CTL", r=1, s=[-1.0, 1.0, 1.0])

		if mc.objExists("C_noseBridge_PIV_CTL"):
			if not mc.getAttr("C_noseBridge_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBridge_PIV_CTL.rotateOrder", 0)

			mc.xform("C_noseBridge_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseTip_PIV_CTL"):
			if not mc.getAttr("C_noseTip_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseTip_PIV_CTL.rotateOrder", 0)

			mc.xform("C_noseTip_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLip_PIV_CTL"):
			if not mc.getAttr("C_upperLip_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLip_PIV_CTL.rotateOrder", 0)

			mc.xform("C_upperLip_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLip_PIV_CTL"):
			if not mc.getAttr("C_lowerLip_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLip_PIV_CTL.rotateOrder", 0)

			mc.xform("C_lowerLip_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCorner_PIV_CTL"):
			if not mc.getAttr("R_lipCorner_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCorner_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lipCorner_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lipCorner_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCorner_PIV_CTL"):
			if not mc.getAttr("L_lipCorner_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCorner_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lipCorner_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("L_lipCorner_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_A_PIV_CTL"):
			if not mc.getAttr("R_upperLip_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLip_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upperLip_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upperLip_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_A_PIV_CTL"):
			if not mc.getAttr("R_lowerLip_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lowerLip_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lowerLip_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_A_PIV_CTL"):
			if not mc.getAttr("L_upperLip_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLip_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upperLip_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("L_upperLip_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_A_PIV_CTL"):
			if not mc.getAttr("L_lowerLip_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lowerLip_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("L_lowerLip_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_mouthAll_PIV_CTL"):
			if not mc.getAttr("C_mouthAll_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_mouthAll_PIV_CTL.rotateOrder", 0)

			mc.xform("C_mouthAll_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipZipper_PIV_CTL"):
			mc.xform("L_lipZipper_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipZipper_PIV_CTL"):
			mc.xform("R_lipZipper_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_C_PIV_CTL"):
			if not mc.getAttr("L_upperLipSecondary_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_B_PIV_CTL"):
			if not mc.getAttr("R_upperLipSecondary_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_B_PIV_CTL"):
			if not mc.getAttr("L_upperLipSecondary_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCornerSecondary_PIV_CTL"):
			if not mc.getAttr("R_lipCornerSecondary_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCornerSecondary_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lipCornerSecondary_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_C_PIV_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_D_PIV_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_D_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_D_PIV_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCornerSecondary_PIV_CTL"):
			if not mc.getAttr("L_lipCornerSecondary_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCornerSecondary_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lipCornerSecondary_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_B_PIV_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_C_PIV_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_C_PIV_CTL"):
			if not mc.getAttr("R_upperLipSecondary_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_A_PIV_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_B_PIV_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_A_PIV_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_A_PIV_CTL"):
			if not mc.getAttr("L_upperLipSecondary_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_A_PIV_CTL"):
			if not mc.getAttr("R_upperLipSecondary_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLipSecondary_PIV_CTL"):
			if not mc.getAttr("C_lowerLipSecondary_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLipSecondary_PIV_CTL.rotateOrder", 0)

			mc.xform("C_lowerLipSecondary_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLipSecondary_PIV_CTL"):
			if not mc.getAttr("C_upperLipSecondary_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLipSecondary_PIV_CTL.rotateOrder", 0)

			mc.xform("C_upperLipSecondary_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_D_PIV_CTL"):
			if not mc.getAttr("L_upperLipSecondary_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_D_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_D_PIV_CTL"):
			if not mc.getAttr("R_upperLipSecondary_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_D_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lookAt_PIV_CTL"):
			mc.xform("C_lookAt_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lookAt_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_eye_FK_PIV_CTL"):
			mc.xform("L_eye_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lookAt_PIV_CTL"):
			mc.xform("L_lookAt_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_innerLid_PIV_CTL"):
			if not mc.getAttr("L_innerLid_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_innerLid_PIV_CTL.rotateOrder", 0)

			mc.xform("L_innerLid_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterLid_PIV_CTL"):
			if not mc.getAttr("L_outterLid_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_outterLid_PIV_CTL.rotateOrder", 0)

			mc.xform("L_outterLid_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_A_PIV_CTL"):
			if not mc.getAttr("L_upperLid_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_B_PIV_CTL"):
			if not mc.getAttr("L_upperLid_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_C_PIV_CTL"):
			if not mc.getAttr("L_upperLid_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_A_PIV_CTL"):
			if not mc.getAttr("L_lowerLid_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_B_PIV_CTL"):
			if not mc.getAttr("L_lowerLid_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_C_PIV_CTL"):
			if not mc.getAttr("L_lowerLid_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLidPrimary_PIV_CTL"):
			if not mc.getAttr("L_upperLidPrimary_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLidPrimary_PIV_CTL.rotateOrder", 0)

			mc.xform("L_upperLidPrimary_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLidPrimary_PIV_CTL"):
			if not mc.getAttr("L_lowerLidPrimary_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLidPrimary_PIV_CTL.rotateOrder", 0)

			mc.xform("L_lowerLidPrimary_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_A_PIV_CTL"):
			if not mc.getAttr("L_cheek_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_cheek_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_B_PIV_CTL"):
			if not mc.getAttr("L_cheek_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_cheek_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_C_PIV_CTL"):
			if not mc.getAttr("L_cheek_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_cheek_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_A_PIV_CTL"):
			if not mc.getAttr("L_squint_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_squint_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_squint_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_B_PIV_CTL"):
			if not mc.getAttr("L_squint_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_squint_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_squint_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_C_PIV_CTL"):
			if not mc.getAttr("L_squint_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_squint_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_squint_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_A_PIV_CTL"):
			if not mc.getAttr("L_cheekLower_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_B_PIV_CTL"):
			if not mc.getAttr("L_cheekLower_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_C_PIV_CTL"):
			if not mc.getAttr("L_cheekLower_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_PIV_CTL"):
			if not mc.getAttr("C_brow_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_PIV_CTL.rotateOrder", 0)

			mc.xform("C_brow_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_brow_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_A_PIV_CTL"):
			if not mc.getAttr("L_brow_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_brow_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_B_PIV_CTL"):
			if not mc.getAttr("L_brow_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_brow_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_C_PIV_CTL"):
			if not mc.getAttr("L_brow_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_brow_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_A_PIV_CTL"):
			if not mc.getAttr("R_brow_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_brow_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_A_PIV_CTL", a=1, ro=[0.0, 0.0, -180.0])
			mc.xform("R_brow_A_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_brow_B_PIV_CTL"):
			if not mc.getAttr("R_brow_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_brow_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_B_PIV_CTL", a=1, ro=[0.0, 0.0, -180.0])
			mc.xform("R_brow_B_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_brow_C_PIV_CTL"):
			if not mc.getAttr("R_brow_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_brow_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_C_PIV_CTL", a=1, ro=[0.0, 0.0, -180.0])
			mc.xform("R_brow_C_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("C_brow_upper_PIV_CTL"):
			if not mc.getAttr("C_brow_upper_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_upper_PIV_CTL.rotateOrder", 0)

			mc.xform("C_brow_upper_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_brow_upper_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_upper_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_A_PIV_CTL"):
			if not mc.getAttr("L_brow_upper_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_A_PIV_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_A_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_A_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_B_PIV_CTL"):
			if not mc.getAttr("L_brow_upper_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_B_PIV_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_B_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_B_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_C_PIV_CTL"):
			if not mc.getAttr("L_brow_upper_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_C_PIV_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_C_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_C_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_upper_A_PIV_CTL"):
			if not mc.getAttr("R_brow_upper_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_A_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_A_PIV_CTL", a=1, ro=[0.0, 0.0, -180.0])
			mc.xform("R_brow_upper_A_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_brow_upper_B_PIV_CTL"):
			if not mc.getAttr("R_brow_upper_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_B_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_B_PIV_CTL", a=1, ro=[0.0, 0.0, -180.0])
			mc.xform("R_brow_upper_B_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_brow_upper_C_PIV_CTL"):
			if not mc.getAttr("R_brow_upper_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_C_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_C_PIV_CTL", a=1, ro=[0.0, 0.0, -180.0])
			mc.xform("R_brow_upper_C_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_eye_FK_PIV_CTL"):
			mc.xform("R_eye_FK_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_eye_FK_PIV_CTL", a=1, ro=[7.016709298534875e-15, -1.2722218725854067e-14, 180.0])
			mc.xform("R_eye_FK_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_lookAt_PIV_CTL"):
			mc.xform("R_lookAt_PIV_CTL", a=1, t=[0.0, 0.0, -5.0])
			mc.xform("R_lookAt_PIV_CTL", a=1, ro=[1.4033418597069752e-14, -8.592990582998206e-31, -180.0])
			mc.xform("R_lookAt_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_innerLid_PIV_CTL"):
			if not mc.getAttr("R_innerLid_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_innerLid_PIV_CTL.rotateOrder", 0)

			mc.xform("R_innerLid_PIV_CTL", a=1, t=[-3.828515081620729, -2.131356636070336e-06, 5.961178358160346e-07])
			mc.xform("R_innerLid_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_innerLid_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_outterLid_PIV_CTL"):
			if not mc.getAttr("R_outterLid_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_outterLid_PIV_CTL.rotateOrder", 0)

			mc.xform("R_outterLid_PIV_CTL", a=1, t=[4.171484918379271, -2.131356636070336e-06, 5.961178358160346e-07])
			mc.xform("R_outterLid_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_outterLid_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_upperLid_A_PIV_CTL"):
			if not mc.getAttr("R_upperLid_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_A_PIV_CTL", a=1, t=[-1.8285150816207278, -2.1313566413994067e-06, 5.961178359270569e-07])
			mc.xform("R_upperLid_A_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upperLid_A_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_upperLid_B_PIV_CTL"):
			if not mc.getAttr("R_upperLid_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_B_PIV_CTL", a=1, t=[0.17148491837927216, -2.1313566342939794e-06, 5.961178358160346e-07])
			mc.xform("R_upperLid_B_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upperLid_B_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_upperLid_C_PIV_CTL"):
			if not mc.getAttr("R_upperLid_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_C_PIV_CTL", a=1, t=[2.1714849183792726, -2.1313566413994067e-06, 5.961178359270569e-07])
			mc.xform("R_upperLid_C_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upperLid_C_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_lowerLid_A_PIV_CTL"):
			if not mc.getAttr("R_lowerLid_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_A_PIV_CTL", a=1, t=[-1.8285150816207287, -2.1313566342939794e-06, 5.961178358160346e-07])
			mc.xform("R_lowerLid_A_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lowerLid_A_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_lowerLid_B_PIV_CTL"):
			if not mc.getAttr("R_lowerLid_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_B_PIV_CTL", a=1, t=[0.17148491837927082, -2.131356637846693e-06, 5.961178358160346e-07])
			mc.xform("R_lowerLid_B_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lowerLid_B_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_lowerLid_C_PIV_CTL"):
			if not mc.getAttr("R_lowerLid_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_C_PIV_CTL", a=1, t=[2.171484918379271, -2.1313566342939794e-06, 5.961178358160346e-07])
			mc.xform("R_lowerLid_C_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lowerLid_C_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_upperLidPrimary_PIV_CTL"):
			if not mc.getAttr("R_upperLidPrimary_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLidPrimary_PIV_CTL.rotateOrder", 0)

			mc.xform("R_upperLidPrimary_PIV_CTL", a=1, t=[0.17148491837927216, -2.1313566342939794e-06, 5.961178358160346e-07])
			mc.xform("R_upperLidPrimary_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upperLidPrimary_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_lowerLidPrimary_PIV_CTL"):
			if not mc.getAttr("R_lowerLidPrimary_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLidPrimary_PIV_CTL.rotateOrder", 0)

			mc.xform("R_lowerLidPrimary_PIV_CTL", a=1, t=[0.17148491837927082, -2.131356637846693e-06, 5.961178358160346e-07])
			mc.xform("R_lowerLidPrimary_PIV_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lowerLidPrimary_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_cheek_A_PIV_CTL"):
			if not mc.getAttr("R_cheek_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_cheek_A_PIV_CTL", a=1, t=[2.883759857796875e-06, 4.301467619871602e-06, 3.784103563830854e-07])
			mc.xform("R_cheek_A_PIV_CTL", a=1, ro=[-0.0005087068989038188, 0.00010137567693353734, 179.99992293234314])
			mc.xform("R_cheek_A_PIV_CTL", r=1, s=[1.0, 1.0, -0.9999999999999999])

		if mc.objExists("R_cheek_B_PIV_CTL"):
			if not mc.getAttr("R_cheek_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_cheek_B_PIV_CTL", a=1, t=[6.36462244907321e-07, 4.537143250882281e-06, 2.2289137302511364e-07])
			mc.xform("R_cheek_B_PIV_CTL", a=1, ro=[-0.0005320903573118503, 1.0122614007545495e-05, 179.9999990582643])
			mc.xform("R_cheek_B_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_cheek_C_PIV_CTL"):
			if not mc.getAttr("R_cheek_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_cheek_C_PIV_CTL", a=1, t=[6.847071973847818e-07, 2.9742569078727854e-06, 3.146774361084681e-07])
			mc.xform("R_cheek_C_PIV_CTL", a=1, ro=[-0.00048335547639856045, -4.820948458263836e-05, -179.9999246607087])
			mc.xform("R_cheek_C_PIV_CTL", r=1, s=[1.0, 0.9999999999999999, -1.0])

		if mc.objExists("R_squint_A_PIV_CTL"):
			if not mc.getAttr("R_squint_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_squint_A_PIV_CTL", a=1, t=[1.6843095564933463e-06, 9.2377434368629e-07, -1.0960551943828278e-06])
			mc.xform("R_squint_A_PIV_CTL", a=1, ro=[-0.00021953722197165838, 0.000113408166875824, 179.99986658401133])
			mc.xform("R_squint_A_PIV_CTL", r=1, s=[0.9999999999999999, 1.0, -0.9999999999999999])

		if mc.objExists("R_squint_B_PIV_CTL"):
			if not mc.getAttr("R_squint_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_squint_B_PIV_CTL", a=1, t=[3.0561406472173758e-06, 3.972169023480632e-06, -1.3089634172125386e-06])
			mc.xform("R_squint_B_PIV_CTL", a=1, ro=[-0.000287240020640971, 4.852009659668648e-05, 179.99999082368575])
			mc.xform("R_squint_B_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999998, -0.9999999999999996])

		if mc.objExists("R_squint_C_PIV_CTL"):
			if not mc.getAttr("R_squint_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_squint_C_PIV_CTL", a=1, t=[-4.298231304211697e-08, -3.5055652198856535e-06, -1.1432627136098716e-06])
			mc.xform("R_squint_C_PIV_CTL", a=1, ro=[-7.046102282448998e-05, -9.153642616704786e-05, -179.99986122012734])
			mc.xform("R_squint_C_PIV_CTL", r=1, s=[0.9999999999999997, 0.9999999999999999, -0.9999999999999999])

		if mc.objExists("R_cheekLower_A_PIV_CTL"):
			if not mc.getAttr("R_cheekLower_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_A_PIV_CTL", a=1, t=[-2.3066334398080812e-06, 2.7779856335286013e-06, 3.1331589028793516e-06])
			mc.xform("R_cheekLower_A_PIV_CTL", a=1, ro=[-7.206061919131682e-05, -5.029008776549777e-05, 179.99995358705885])
			mc.xform("R_cheekLower_A_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, -1.0])

		if mc.objExists("R_cheekLower_B_PIV_CTL"):
			if not mc.getAttr("R_cheekLower_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_B_PIV_CTL", a=1, t=[-7.071011509651726e-07, 3.95482488757537e-06, 3.1682246603992326e-06])
			mc.xform("R_cheekLower_B_PIV_CTL", a=1, ro=[-8.585914933954308e-05, -1.1209644076061996e-05, -179.9999998178757])
			mc.xform("R_cheekLower_B_PIV_CTL", r=1, s=[0.9999999999999999, 1.0, -0.9999999999999999])

		if mc.objExists("R_cheekLower_C_PIV_CTL"):
			if not mc.getAttr("R_cheekLower_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_C_PIV_CTL", a=1, t=[9.756634167246148e-08, 3.5811970566790308e-06, 3.1296839924088715e-06])
			mc.xform("R_cheekLower_C_PIV_CTL", a=1, ro=[-7.626878501003635e-05, 1.5141781087713166e-05, -179.99995165165348])
			mc.xform("R_cheekLower_C_PIV_CTL", r=1, s=[1.0, 0.9999999999999996, -0.9999999999999998])

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
			mc.xform("visibility_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_A_D_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_A_C_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_A_B_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_A_A_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_A_CTL"):
			if not mc.getAttr("C_tongue_IK_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_tongue_IK_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_tongue_IK_A_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_IK_A_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_IK_A_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_A_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_B_D_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_B_C_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_B_B_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_B_A_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_B_CTL"):
			if not mc.getAttr("C_tongue_IK_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_tongue_IK_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_tongue_IK_B_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_IK_B_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_IK_B_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_B_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_C_D_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_C_C_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_C_B_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_C_A_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_C_CTL"):
			if not mc.getAttr("C_tongue_IK_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_tongue_IK_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_tongue_IK_C_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_IK_C_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_IK_C_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_C_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_D_D_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_D_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_D_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_D_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_D_C_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_D_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_D_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_D_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_D_B_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_D_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_D_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_D_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_D_A_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_D_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_D_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_D_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_D_CTL"):
			if not mc.getAttr("C_tongue_IK_D_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_tongue_IK_D_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_tongue_IK_D_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_IK_D_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_IK_D_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_D_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_E_D_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_E_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_E_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_E_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_E_C_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_E_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_E_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_E_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_E_B_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_E_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_E_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_E_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_E_A_OFF_CTL"):
			if not mc.getAttr("C_tongue_IK_E_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_E_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_E_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_IK_E_CTL"):
			if not mc.getAttr("C_tongue_IK_E_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_tongue_IK_E_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_tongue_IK_E_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_IK_E_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_IK_E_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_IK_E_CTL.rotateOrder", 0)

			mc.xform("C_tongue_IK_E_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_IK_E_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_A_CTL"):
			if not mc.getAttr("C_tongue_FK_A_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_FK_A_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_FK_A_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_FK_A_CTL.rotateOrder", 0)

			mc.xform("C_tongue_FK_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_B_CTL"):
			if not mc.getAttr("C_tongue_FK_B_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_FK_B_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_FK_B_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_FK_B_CTL.rotateOrder", 0)

			mc.xform("C_tongue_FK_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_C_CTL"):
			if not mc.getAttr("C_tongue_FK_C_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_FK_C_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_FK_C_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_FK_C_CTL.rotateOrder", 0)

			mc.xform("C_tongue_FK_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_D_CTL"):
			if not mc.getAttr("C_tongue_FK_D_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_FK_D_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_FK_D_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_FK_D_CTL.rotateOrder", 0)

			mc.xform("C_tongue_FK_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_E_CTL"):
			if not mc.getAttr("C_tongue_FK_E_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_FK_E_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_FK_E_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_FK_E_CTL.rotateOrder", 0)

			mc.xform("C_tongue_FK_E_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_E_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_E_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_F_CTL"):
			if not mc.getAttr("C_tongue_FK_F_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_FK_F_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_FK_F_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_FK_F_CTL.rotateOrder", 0)

			mc.xform("C_tongue_FK_F_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_F_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_F_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_G_CTL"):
			if not mc.getAttr("C_tongue_FK_G_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_FK_G_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_FK_G_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_FK_G_CTL.rotateOrder", 0)

			mc.xform("C_tongue_FK_G_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_G_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_G_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_tongue_FK_H_CTL"):
			if not mc.getAttr("C_tongue_FK_H_CTL.mirrorMode", l=1):
				mc.setAttr("C_tongue_FK_H_CTL.mirrorMode", 0)

			if not mc.getAttr("C_tongue_FK_H_CTL.rotateOrder", l=1):
				mc.setAttr("C_tongue_FK_H_CTL.rotateOrder", 0)

			mc.xform("C_tongue_FK_H_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_H_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_tongue_FK_H_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBase_D_OFF_CTL"):
			if not mc.getAttr("C_noseBase_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBase_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseBase_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBase_C_OFF_CTL"):
			if not mc.getAttr("C_noseBase_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBase_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseBase_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBase_B_OFF_CTL"):
			if not mc.getAttr("C_noseBase_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBase_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseBase_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBase_A_OFF_CTL"):
			if not mc.getAttr("C_noseBase_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBase_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseBase_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBase_CTL"):
			if not mc.getAttr("C_noseBase_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_noseBase_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_noseBase_CTL.mirrorMode", l=1):
				mc.setAttr("C_noseBase_CTL.mirrorMode", 0)

			if not mc.getAttr("C_noseBase_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBase_CTL.rotateOrder", 0)

			mc.xform("C_noseBase_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBase_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_nostril_D_OFF_CTL"):
			if not mc.getAttr("L_nostril_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_nostril_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_nostril_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_nostril_C_OFF_CTL"):
			if not mc.getAttr("L_nostril_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_nostril_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_nostril_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_nostril_B_OFF_CTL"):
			if not mc.getAttr("L_nostril_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_nostril_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_nostril_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_nostril_A_OFF_CTL"):
			if not mc.getAttr("L_nostril_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_nostril_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_nostril_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_nostril_CTL"):
			if not mc.getAttr("L_nostril_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_nostril_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_nostril_CTL.mirrorMode", l=1):
				mc.setAttr("L_nostril_CTL.mirrorMode", 0)

			if not mc.getAttr("L_nostril_CTL.rotateOrder", l=1):
				mc.setAttr("L_nostril_CTL.rotateOrder", 0)

			mc.xform("L_nostril_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_nostril_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_nostril_D_OFF_CTL"):
			if not mc.getAttr("R_nostril_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_nostril_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_nostril_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_nostril_C_OFF_CTL"):
			if not mc.getAttr("R_nostril_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_nostril_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_nostril_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_nostril_B_OFF_CTL"):
			if not mc.getAttr("R_nostril_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_nostril_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_nostril_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_nostril_A_OFF_CTL"):
			if not mc.getAttr("R_nostril_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_nostril_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_nostril_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_nostril_CTL"):
			if not mc.getAttr("R_nostril_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_nostril_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_nostril_CTL.mirrorMode", l=1):
				mc.setAttr("R_nostril_CTL.mirrorMode", 0)

			if not mc.getAttr("R_nostril_CTL.rotateOrder", l=1):
				mc.setAttr("R_nostril_CTL.rotateOrder", 0)

			mc.xform("R_nostril_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_nostril_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBridge_D_OFF_CTL"):
			if not mc.getAttr("C_noseBridge_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBridge_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseBridge_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBridge_C_OFF_CTL"):
			if not mc.getAttr("C_noseBridge_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBridge_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseBridge_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBridge_B_OFF_CTL"):
			if not mc.getAttr("C_noseBridge_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBridge_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseBridge_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBridge_A_OFF_CTL"):
			if not mc.getAttr("C_noseBridge_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBridge_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseBridge_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseBridge_CTL"):
			if not mc.getAttr("C_noseBridge_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_noseBridge_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_noseBridge_CTL.mirrorMode", l=1):
				mc.setAttr("C_noseBridge_CTL.mirrorMode", 0)

			if not mc.getAttr("C_noseBridge_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseBridge_CTL.rotateOrder", 0)

			mc.xform("C_noseBridge_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseBridge_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseTip_D_OFF_CTL"):
			if not mc.getAttr("C_noseTip_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseTip_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseTip_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseTip_C_OFF_CTL"):
			if not mc.getAttr("C_noseTip_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseTip_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseTip_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseTip_B_OFF_CTL"):
			if not mc.getAttr("C_noseTip_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseTip_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseTip_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseTip_A_OFF_CTL"):
			if not mc.getAttr("C_noseTip_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseTip_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_noseTip_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_noseTip_CTL"):
			if not mc.getAttr("C_noseTip_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_noseTip_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_noseTip_CTL.mirrorMode", l=1):
				mc.setAttr("C_noseTip_CTL.mirrorMode", 0)

			if not mc.getAttr("C_noseTip_CTL.rotateOrder", l=1):
				mc.setAttr("C_noseTip_CTL.rotateOrder", 0)

			mc.xform("C_noseTip_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_noseTip_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLip_D_OFF_CTL"):
			if not mc.getAttr("C_upperLip_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLip_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_upperLip_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLip_C_OFF_CTL"):
			if not mc.getAttr("C_upperLip_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLip_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_upperLip_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLip_B_OFF_CTL"):
			if not mc.getAttr("C_upperLip_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLip_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_upperLip_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLip_A_OFF_CTL"):
			if not mc.getAttr("C_upperLip_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLip_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_upperLip_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLip_CTL"):
			if not mc.getAttr("C_upperLip_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_upperLip_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_upperLip_CTL.mirrorMode", l=1):
				mc.setAttr("C_upperLip_CTL.mirrorMode", 0)

			if not mc.getAttr("C_upperLip_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLip_CTL.rotateOrder", 0)

			mc.xform("C_upperLip_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLip_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLip_D_OFF_CTL"):
			if not mc.getAttr("C_lowerLip_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLip_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lowerLip_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLip_C_OFF_CTL"):
			if not mc.getAttr("C_lowerLip_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLip_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lowerLip_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLip_B_OFF_CTL"):
			if not mc.getAttr("C_lowerLip_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLip_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lowerLip_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLip_A_OFF_CTL"):
			if not mc.getAttr("C_lowerLip_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLip_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lowerLip_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLip_CTL"):
			if not mc.getAttr("C_lowerLip_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_lowerLip_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_lowerLip_CTL.mirrorMode", l=1):
				mc.setAttr("C_lowerLip_CTL.mirrorMode", 0)

			if not mc.getAttr("C_lowerLip_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLip_CTL.rotateOrder", 0)

			mc.xform("C_lowerLip_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLip_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCorner_D_OFF_CTL"):
			if not mc.getAttr("R_lipCorner_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCorner_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipCorner_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCorner_C_OFF_CTL"):
			if not mc.getAttr("R_lipCorner_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCorner_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipCorner_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCorner_B_OFF_CTL"):
			if not mc.getAttr("R_lipCorner_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCorner_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipCorner_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCorner_A_OFF_CTL"):
			if not mc.getAttr("R_lipCorner_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCorner_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipCorner_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCorner_CTL"):
			if not mc.getAttr("R_lipCorner_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lipCorner_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lipCorner_CTL.mirrorMode", l=1):
				mc.setAttr("R_lipCorner_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lipCorner_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCorner_CTL.rotateOrder", 0)

			mc.xform("R_lipCorner_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCorner_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCorner_D_OFF_CTL"):
			if not mc.getAttr("L_lipCorner_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCorner_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipCorner_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCorner_C_OFF_CTL"):
			if not mc.getAttr("L_lipCorner_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCorner_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipCorner_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCorner_B_OFF_CTL"):
			if not mc.getAttr("L_lipCorner_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCorner_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipCorner_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCorner_A_OFF_CTL"):
			if not mc.getAttr("L_lipCorner_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCorner_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipCorner_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCorner_CTL"):
			if not mc.getAttr("L_lipCorner_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lipCorner_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lipCorner_CTL.mirrorMode", l=1):
				mc.setAttr("L_lipCorner_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lipCorner_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCorner_CTL.rotateOrder", 0)

			mc.xform("L_lipCorner_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCorner_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_A_D_OFF_CTL"):
			if not mc.getAttr("R_upperLip_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLip_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLip_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_A_C_OFF_CTL"):
			if not mc.getAttr("R_upperLip_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLip_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLip_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_A_B_OFF_CTL"):
			if not mc.getAttr("R_upperLip_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLip_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLip_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_A_A_OFF_CTL"):
			if not mc.getAttr("R_upperLip_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLip_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLip_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLip_A_CTL"):
			if not mc.getAttr("R_upperLip_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upperLip_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upperLip_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_upperLip_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upperLip_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLip_A_CTL.rotateOrder", 0)

			mc.xform("R_upperLip_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLip_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_A_D_OFF_CTL"):
			if not mc.getAttr("R_lowerLip_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLip_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_A_C_OFF_CTL"):
			if not mc.getAttr("R_lowerLip_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLip_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_A_B_OFF_CTL"):
			if not mc.getAttr("R_lowerLip_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLip_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_A_A_OFF_CTL"):
			if not mc.getAttr("R_lowerLip_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLip_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLip_A_CTL"):
			if not mc.getAttr("R_lowerLip_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lowerLip_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lowerLip_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_lowerLip_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lowerLip_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLip_A_CTL.rotateOrder", 0)

			mc.xform("R_lowerLip_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLip_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_A_D_OFF_CTL"):
			if not mc.getAttr("L_upperLip_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLip_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLip_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_A_C_OFF_CTL"):
			if not mc.getAttr("L_upperLip_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLip_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLip_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_A_B_OFF_CTL"):
			if not mc.getAttr("L_upperLip_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLip_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLip_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_A_A_OFF_CTL"):
			if not mc.getAttr("L_upperLip_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLip_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLip_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLip_A_CTL"):
			if not mc.getAttr("L_upperLip_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upperLip_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upperLip_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_upperLip_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upperLip_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLip_A_CTL.rotateOrder", 0)

			mc.xform("L_upperLip_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLip_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_A_D_OFF_CTL"):
			if not mc.getAttr("L_lowerLip_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLip_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_A_C_OFF_CTL"):
			if not mc.getAttr("L_lowerLip_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLip_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_A_B_OFF_CTL"):
			if not mc.getAttr("L_lowerLip_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLip_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_A_A_OFF_CTL"):
			if not mc.getAttr("L_lowerLip_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLip_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLip_A_CTL"):
			if not mc.getAttr("L_lowerLip_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lowerLip_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lowerLip_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_lowerLip_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lowerLip_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLip_A_CTL.rotateOrder", 0)

			mc.xform("L_lowerLip_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLip_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_mouthAll_D_OFF_CTL"):
			if not mc.getAttr("C_mouthAll_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_mouthAll_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_mouthAll_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_mouthAll_C_OFF_CTL"):
			if not mc.getAttr("C_mouthAll_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_mouthAll_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_mouthAll_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_mouthAll_B_OFF_CTL"):
			if not mc.getAttr("C_mouthAll_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_mouthAll_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_mouthAll_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_mouthAll_A_OFF_CTL"):
			if not mc.getAttr("C_mouthAll_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_mouthAll_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_mouthAll_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_mouthAll_CTL"):
			if not mc.getAttr("C_mouthAll_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_mouthAll_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_mouthAll_CTL.mirrorMode", l=1):
				mc.setAttr("C_mouthAll_CTL.mirrorMode", 0)

			if not mc.getAttr("C_mouthAll_CTL.rotateOrder", l=1):
				mc.setAttr("C_mouthAll_CTL.rotateOrder", 0)

			mc.xform("C_mouthAll_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_mouthAll_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipZipper_D_OFF_CTL"):
			if not mc.getAttr("L_lipZipper_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipZipper_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipZipper_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipZipper_C_OFF_CTL"):
			if not mc.getAttr("L_lipZipper_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipZipper_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipZipper_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipZipper_B_OFF_CTL"):
			if not mc.getAttr("L_lipZipper_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipZipper_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipZipper_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipZipper_A_OFF_CTL"):
			if not mc.getAttr("L_lipZipper_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipZipper_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipZipper_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipZipper_CTL"):
			if not mc.getAttr("L_lipZipper_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lipZipper_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lipZipper_CTL.mirrorMode", l=1):
				mc.setAttr("L_lipZipper_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lipZipper_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipZipper_CTL.rotateOrder", 0)

			mc.xform("L_lipZipper_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipZipper_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipZipper_D_OFF_CTL"):
			if not mc.getAttr("R_lipZipper_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipZipper_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipZipper_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipZipper_C_OFF_CTL"):
			if not mc.getAttr("R_lipZipper_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipZipper_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipZipper_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipZipper_B_OFF_CTL"):
			if not mc.getAttr("R_lipZipper_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipZipper_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipZipper_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipZipper_A_OFF_CTL"):
			if not mc.getAttr("R_lipZipper_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipZipper_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipZipper_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipZipper_CTL"):
			if not mc.getAttr("R_lipZipper_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lipZipper_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lipZipper_CTL.mirrorMode", l=1):
				mc.setAttr("R_lipZipper_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lipZipper_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipZipper_CTL.rotateOrder", 0)

			mc.xform("R_lipZipper_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipZipper_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_C_D_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_C_C_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_C_B_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_C_A_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_C_CTL"):
			if not mc.getAttr("L_upperLipSecondary_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upperLipSecondary_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upperLipSecondary_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_upperLipSecondary_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upperLipSecondary_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_C_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_B_D_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_B_C_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_B_B_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_B_A_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_B_CTL"):
			if not mc.getAttr("R_upperLipSecondary_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upperLipSecondary_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upperLipSecondary_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_upperLipSecondary_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upperLipSecondary_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_B_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_B_D_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_B_C_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_B_B_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_B_A_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_B_CTL"):
			if not mc.getAttr("L_upperLipSecondary_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upperLipSecondary_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upperLipSecondary_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_upperLipSecondary_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upperLipSecondary_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_B_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCornerSecondary_D_OFF_CTL"):
			if not mc.getAttr("R_lipCornerSecondary_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCornerSecondary_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipCornerSecondary_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCornerSecondary_C_OFF_CTL"):
			if not mc.getAttr("R_lipCornerSecondary_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCornerSecondary_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipCornerSecondary_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCornerSecondary_B_OFF_CTL"):
			if not mc.getAttr("R_lipCornerSecondary_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCornerSecondary_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipCornerSecondary_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCornerSecondary_A_OFF_CTL"):
			if not mc.getAttr("R_lipCornerSecondary_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCornerSecondary_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lipCornerSecondary_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lipCornerSecondary_CTL"):
			if not mc.getAttr("R_lipCornerSecondary_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lipCornerSecondary_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lipCornerSecondary_CTL.mirrorMode", l=1):
				mc.setAttr("R_lipCornerSecondary_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lipCornerSecondary_CTL.rotateOrder", l=1):
				mc.setAttr("R_lipCornerSecondary_CTL.rotateOrder", 0)

			mc.xform("R_lipCornerSecondary_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lipCornerSecondary_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_C_D_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_C_C_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_C_B_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_C_A_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_C_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lowerLipSecondary_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lowerLipSecondary_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_lowerLipSecondary_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lowerLipSecondary_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_C_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_D_D_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_D_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_D_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_D_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_D_C_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_D_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_D_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_D_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_D_B_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_D_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_D_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_D_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_D_A_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_D_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_D_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_D_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_D_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_D_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lowerLipSecondary_D_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lowerLipSecondary_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_lowerLipSecondary_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lowerLipSecondary_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_D_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_D_D_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_D_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_D_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_D_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_D_C_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_D_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_D_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_D_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_D_B_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_D_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_D_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_D_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_D_A_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_D_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_D_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_D_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_D_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_D_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lowerLipSecondary_D_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lowerLipSecondary_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_lowerLipSecondary_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lowerLipSecondary_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_D_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCornerSecondary_D_OFF_CTL"):
			if not mc.getAttr("L_lipCornerSecondary_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCornerSecondary_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipCornerSecondary_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCornerSecondary_C_OFF_CTL"):
			if not mc.getAttr("L_lipCornerSecondary_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCornerSecondary_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipCornerSecondary_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCornerSecondary_B_OFF_CTL"):
			if not mc.getAttr("L_lipCornerSecondary_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCornerSecondary_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipCornerSecondary_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCornerSecondary_A_OFF_CTL"):
			if not mc.getAttr("L_lipCornerSecondary_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCornerSecondary_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lipCornerSecondary_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lipCornerSecondary_CTL"):
			if not mc.getAttr("L_lipCornerSecondary_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lipCornerSecondary_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lipCornerSecondary_CTL.mirrorMode", l=1):
				mc.setAttr("L_lipCornerSecondary_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lipCornerSecondary_CTL.rotateOrder", l=1):
				mc.setAttr("L_lipCornerSecondary_CTL.rotateOrder", 0)

			mc.xform("L_lipCornerSecondary_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lipCornerSecondary_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_B_D_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_B_C_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_B_B_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_B_A_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_B_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lowerLipSecondary_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lowerLipSecondary_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_lowerLipSecondary_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lowerLipSecondary_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_B_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_C_D_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_C_C_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_C_B_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_C_A_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_C_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lowerLipSecondary_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lowerLipSecondary_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_lowerLipSecondary_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lowerLipSecondary_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_C_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_C_D_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_C_C_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_C_B_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_C_A_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_C_CTL"):
			if not mc.getAttr("R_upperLipSecondary_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upperLipSecondary_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upperLipSecondary_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_upperLipSecondary_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upperLipSecondary_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_C_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_A_D_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_A_C_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_A_B_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_A_A_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_A_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lowerLipSecondary_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lowerLipSecondary_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_lowerLipSecondary_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lowerLipSecondary_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_A_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_B_D_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_B_C_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_B_B_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_B_A_OFF_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLipSecondary_B_CTL"):
			if not mc.getAttr("R_lowerLipSecondary_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lowerLipSecondary_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lowerLipSecondary_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_lowerLipSecondary_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lowerLipSecondary_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLipSecondary_B_CTL.rotateOrder", 0)

			mc.xform("R_lowerLipSecondary_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLipSecondary_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_A_D_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_A_C_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_A_B_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_A_A_OFF_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLipSecondary_A_CTL"):
			if not mc.getAttr("L_lowerLipSecondary_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lowerLipSecondary_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lowerLipSecondary_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_lowerLipSecondary_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lowerLipSecondary_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLipSecondary_A_CTL.rotateOrder", 0)

			mc.xform("L_lowerLipSecondary_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLipSecondary_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_A_D_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_A_C_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_A_B_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_A_A_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_A_CTL"):
			if not mc.getAttr("L_upperLipSecondary_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upperLipSecondary_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upperLipSecondary_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_upperLipSecondary_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upperLipSecondary_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_A_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_A_D_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_A_C_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_A_B_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_A_A_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_A_CTL"):
			if not mc.getAttr("R_upperLipSecondary_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upperLipSecondary_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upperLipSecondary_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_upperLipSecondary_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upperLipSecondary_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_A_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLipSecondary_D_OFF_CTL"):
			if not mc.getAttr("C_lowerLipSecondary_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLipSecondary_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lowerLipSecondary_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLipSecondary_C_OFF_CTL"):
			if not mc.getAttr("C_lowerLipSecondary_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLipSecondary_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lowerLipSecondary_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLipSecondary_B_OFF_CTL"):
			if not mc.getAttr("C_lowerLipSecondary_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLipSecondary_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lowerLipSecondary_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLipSecondary_A_OFF_CTL"):
			if not mc.getAttr("C_lowerLipSecondary_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLipSecondary_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_lowerLipSecondary_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_lowerLipSecondary_CTL"):
			if not mc.getAttr("C_lowerLipSecondary_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_lowerLipSecondary_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_lowerLipSecondary_CTL.mirrorMode", l=1):
				mc.setAttr("C_lowerLipSecondary_CTL.mirrorMode", 0)

			if not mc.getAttr("C_lowerLipSecondary_CTL.rotateOrder", l=1):
				mc.setAttr("C_lowerLipSecondary_CTL.rotateOrder", 0)

			mc.xform("C_lowerLipSecondary_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_lowerLipSecondary_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLipSecondary_D_OFF_CTL"):
			if not mc.getAttr("C_upperLipSecondary_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLipSecondary_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_upperLipSecondary_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLipSecondary_C_OFF_CTL"):
			if not mc.getAttr("C_upperLipSecondary_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLipSecondary_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_upperLipSecondary_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLipSecondary_B_OFF_CTL"):
			if not mc.getAttr("C_upperLipSecondary_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLipSecondary_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_upperLipSecondary_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLipSecondary_A_OFF_CTL"):
			if not mc.getAttr("C_upperLipSecondary_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLipSecondary_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_upperLipSecondary_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_upperLipSecondary_CTL"):
			if not mc.getAttr("C_upperLipSecondary_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_upperLipSecondary_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_upperLipSecondary_CTL.mirrorMode", l=1):
				mc.setAttr("C_upperLipSecondary_CTL.mirrorMode", 0)

			if not mc.getAttr("C_upperLipSecondary_CTL.rotateOrder", l=1):
				mc.setAttr("C_upperLipSecondary_CTL.rotateOrder", 0)

			mc.xform("C_upperLipSecondary_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_upperLipSecondary_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_D_D_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_D_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_D_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_D_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_D_C_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_D_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_D_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_D_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_D_B_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_D_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_D_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_D_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_D_A_OFF_CTL"):
			if not mc.getAttr("L_upperLipSecondary_D_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_D_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_D_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLipSecondary_D_CTL"):
			if not mc.getAttr("L_upperLipSecondary_D_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upperLipSecondary_D_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upperLipSecondary_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_upperLipSecondary_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upperLipSecondary_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLipSecondary_D_CTL.rotateOrder", 0)

			mc.xform("L_upperLipSecondary_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLipSecondary_D_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_D_D_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_D_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_D_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_D_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_D_C_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_D_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_D_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_D_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_D_B_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_D_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_D_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_D_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_D_A_OFF_CTL"):
			if not mc.getAttr("R_upperLipSecondary_D_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_D_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_D_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLipSecondary_D_CTL"):
			if not mc.getAttr("R_upperLipSecondary_D_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upperLipSecondary_D_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upperLipSecondary_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_upperLipSecondary_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upperLipSecondary_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLipSecondary_D_CTL.rotateOrder", 0)

			mc.xform("R_upperLipSecondary_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_upperLipSecondary_D_CTL", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("L_eye_FK_D_OFF_CTL"):
			if not mc.getAttr("L_eye_FK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_eye_FK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_eye_FK_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_eye_FK_C_OFF_CTL"):
			if not mc.getAttr("L_eye_FK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_eye_FK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_eye_FK_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_eye_FK_B_OFF_CTL"):
			if not mc.getAttr("L_eye_FK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_eye_FK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_eye_FK_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_eye_FK_A_OFF_CTL"):
			if not mc.getAttr("L_eye_FK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_eye_FK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_eye_FK_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_eye_FK_CTL"):
			if not mc.getAttr("L_eye_FK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_eye_FK_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_eye_FK_CTL.mirrorMode", l=1):
				mc.setAttr("L_eye_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("L_eye_FK_CTL.rotateOrder", l=1):
				mc.setAttr("L_eye_FK_CTL.rotateOrder", 0)

			mc.xform("L_eye_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_eye_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lookAt_D_OFF_CTL"):
			if not mc.getAttr("L_lookAt_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lookAt_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lookAt_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lookAt_C_OFF_CTL"):
			if not mc.getAttr("L_lookAt_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lookAt_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lookAt_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lookAt_B_OFF_CTL"):
			if not mc.getAttr("L_lookAt_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lookAt_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lookAt_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lookAt_A_OFF_CTL"):
			if not mc.getAttr("L_lookAt_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lookAt_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lookAt_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lookAt_CTL"):
			if not mc.getAttr("L_lookAt_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lookAt_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lookAt_CTL.mirrorMode", l=1):
				mc.setAttr("L_lookAt_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lookAt_CTL.rotateOrder", l=1):
				mc.setAttr("L_lookAt_CTL.rotateOrder", 0)

			mc.xform("L_lookAt_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lookAt_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_innerLid_D_OFF_CTL"):
			if not mc.getAttr("L_innerLid_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_innerLid_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_innerLid_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_innerLid_C_OFF_CTL"):
			if not mc.getAttr("L_innerLid_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_innerLid_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_innerLid_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_innerLid_B_OFF_CTL"):
			if not mc.getAttr("L_innerLid_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_innerLid_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_innerLid_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_innerLid_A_OFF_CTL"):
			if not mc.getAttr("L_innerLid_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_innerLid_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_innerLid_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_innerLid_CTL"):
			if not mc.getAttr("L_innerLid_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_innerLid_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_innerLid_CTL.mirrorMode", l=1):
				mc.setAttr("L_innerLid_CTL.mirrorMode", 0)

			if not mc.getAttr("L_innerLid_CTL.rotateOrder", l=1):
				mc.setAttr("L_innerLid_CTL.rotateOrder", 0)

			mc.xform("L_innerLid_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_innerLid_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterLid_D_OFF_CTL"):
			if not mc.getAttr("L_outterLid_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_outterLid_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_outterLid_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterLid_C_OFF_CTL"):
			if not mc.getAttr("L_outterLid_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_outterLid_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_outterLid_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterLid_B_OFF_CTL"):
			if not mc.getAttr("L_outterLid_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_outterLid_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_outterLid_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterLid_A_OFF_CTL"):
			if not mc.getAttr("L_outterLid_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_outterLid_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_outterLid_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_outterLid_CTL"):
			if not mc.getAttr("L_outterLid_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_outterLid_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_outterLid_CTL.mirrorMode", l=1):
				mc.setAttr("L_outterLid_CTL.mirrorMode", 0)

			if not mc.getAttr("L_outterLid_CTL.rotateOrder", l=1):
				mc.setAttr("L_outterLid_CTL.rotateOrder", 0)

			mc.xform("L_outterLid_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_outterLid_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_A_D_OFF_CTL"):
			if not mc.getAttr("L_upperLid_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_A_C_OFF_CTL"):
			if not mc.getAttr("L_upperLid_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_A_B_OFF_CTL"):
			if not mc.getAttr("L_upperLid_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_A_A_OFF_CTL"):
			if not mc.getAttr("L_upperLid_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_A_CTL"):
			if not mc.getAttr("L_upperLid_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upperLid_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upperLid_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_upperLid_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upperLid_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_A_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_B_D_OFF_CTL"):
			if not mc.getAttr("L_upperLid_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_B_C_OFF_CTL"):
			if not mc.getAttr("L_upperLid_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_B_B_OFF_CTL"):
			if not mc.getAttr("L_upperLid_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_B_A_OFF_CTL"):
			if not mc.getAttr("L_upperLid_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_B_CTL"):
			if not mc.getAttr("L_upperLid_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upperLid_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upperLid_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_upperLid_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upperLid_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_B_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_C_D_OFF_CTL"):
			if not mc.getAttr("L_upperLid_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_C_C_OFF_CTL"):
			if not mc.getAttr("L_upperLid_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_C_B_OFF_CTL"):
			if not mc.getAttr("L_upperLid_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_C_A_OFF_CTL"):
			if not mc.getAttr("L_upperLid_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLid_C_CTL"):
			if not mc.getAttr("L_upperLid_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upperLid_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upperLid_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_upperLid_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upperLid_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLid_C_CTL.rotateOrder", 0)

			mc.xform("L_upperLid_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLid_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_A_D_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_A_C_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_A_B_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_A_A_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_A_CTL"):
			if not mc.getAttr("L_lowerLid_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lowerLid_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lowerLid_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_lowerLid_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lowerLid_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_A_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_B_D_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_B_C_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_B_B_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_B_A_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_B_CTL"):
			if not mc.getAttr("L_lowerLid_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lowerLid_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lowerLid_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_lowerLid_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lowerLid_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_B_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_C_D_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_C_C_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_C_B_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_C_A_OFF_CTL"):
			if not mc.getAttr("L_lowerLid_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLid_C_CTL"):
			if not mc.getAttr("L_lowerLid_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lowerLid_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lowerLid_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_lowerLid_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lowerLid_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLid_C_CTL.rotateOrder", 0)

			mc.xform("L_lowerLid_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLid_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLidPrimary_D_OFF_CTL"):
			if not mc.getAttr("L_upperLidPrimary_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLidPrimary_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLidPrimary_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLidPrimary_C_OFF_CTL"):
			if not mc.getAttr("L_upperLidPrimary_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLidPrimary_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLidPrimary_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLidPrimary_B_OFF_CTL"):
			if not mc.getAttr("L_upperLidPrimary_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLidPrimary_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLidPrimary_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLidPrimary_A_OFF_CTL"):
			if not mc.getAttr("L_upperLidPrimary_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLidPrimary_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_upperLidPrimary_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_upperLidPrimary_CTL"):
			if not mc.getAttr("L_upperLidPrimary_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_upperLidPrimary_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_upperLidPrimary_CTL.mirrorMode", l=1):
				mc.setAttr("L_upperLidPrimary_CTL.mirrorMode", 0)

			if not mc.getAttr("L_upperLidPrimary_CTL.rotateOrder", l=1):
				mc.setAttr("L_upperLidPrimary_CTL.rotateOrder", 0)

			mc.xform("L_upperLidPrimary_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_upperLidPrimary_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLidPrimary_D_OFF_CTL"):
			if not mc.getAttr("L_lowerLidPrimary_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLidPrimary_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLidPrimary_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLidPrimary_C_OFF_CTL"):
			if not mc.getAttr("L_lowerLidPrimary_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLidPrimary_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLidPrimary_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLidPrimary_B_OFF_CTL"):
			if not mc.getAttr("L_lowerLidPrimary_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLidPrimary_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLidPrimary_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLidPrimary_A_OFF_CTL"):
			if not mc.getAttr("L_lowerLidPrimary_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLidPrimary_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_lowerLidPrimary_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_lowerLidPrimary_CTL"):
			if not mc.getAttr("L_lowerLidPrimary_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_lowerLidPrimary_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_lowerLidPrimary_CTL.mirrorMode", l=1):
				mc.setAttr("L_lowerLidPrimary_CTL.mirrorMode", 0)

			if not mc.getAttr("L_lowerLidPrimary_CTL.rotateOrder", l=1):
				mc.setAttr("L_lowerLidPrimary_CTL.rotateOrder", 0)

			mc.xform("L_lowerLidPrimary_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_lowerLidPrimary_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_A_D_OFF_CTL"):
			if not mc.getAttr("L_cheek_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_A_D_OFF_CTL", a=1, t=[0.0, 4.336808689942018e-19, 0.0])
			mc.xform("L_cheek_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_A_C_OFF_CTL"):
			if not mc.getAttr("L_cheek_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_A_C_OFF_CTL", a=1, t=[0.0, -4.336808689942018e-19, 0.0])
			mc.xform("L_cheek_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_A_B_OFF_CTL"):
			if not mc.getAttr("L_cheek_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_A_B_OFF_CTL", a=1, t=[0.0, -4.336808689942018e-19, 0.0])
			mc.xform("L_cheek_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_A_A_OFF_CTL"):
			if not mc.getAttr("L_cheek_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_A_A_OFF_CTL", a=1, t=[-5.551115123125783e-17, 8.673617379884035e-19, -6.938893903907228e-18])
			mc.xform("L_cheek_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_A_CTL"):
			if not mc.getAttr("L_cheek_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_cheek_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_cheek_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_cheek_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_cheek_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_A_CTL.rotateOrder", 0)

			mc.xform("L_cheek_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_B_D_OFF_CTL"):
			if not mc.getAttr("L_cheek_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_B_C_OFF_CTL"):
			if not mc.getAttr("L_cheek_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_B_B_OFF_CTL"):
			if not mc.getAttr("L_cheek_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_B_A_OFF_CTL"):
			if not mc.getAttr("L_cheek_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_B_CTL"):
			if not mc.getAttr("L_cheek_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_cheek_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_cheek_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_cheek_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_cheek_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_B_CTL.rotateOrder", 0)

			mc.xform("L_cheek_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_C_D_OFF_CTL"):
			if not mc.getAttr("L_cheek_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_C_C_OFF_CTL"):
			if not mc.getAttr("L_cheek_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_C_B_OFF_CTL"):
			if not mc.getAttr("L_cheek_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_C_A_OFF_CTL"):
			if not mc.getAttr("L_cheek_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheek_C_A_OFF_CTL", a=1, t=[0.0, 0.0, -6.938893903907228e-18])
			mc.xform("L_cheek_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheek_C_CTL"):
			if not mc.getAttr("L_cheek_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_cheek_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_cheek_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_cheek_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_cheek_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheek_C_CTL.rotateOrder", 0)

			mc.xform("L_cheek_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheek_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_A_D_OFF_CTL"):
			if not mc.getAttr("L_squint_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_A_D_OFF_CTL", a=1, t=[0.0, 0.0, -3.469446951953614e-18])
			mc.xform("L_squint_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_A_D_OFF_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, 0.9999999999999998])

		if mc.objExists("L_squint_A_C_OFF_CTL"):
			if not mc.getAttr("L_squint_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_A_C_OFF_CTL", a=1, t=[0.0, 5.551115123125783e-17, 1.3877787807814457e-17])
			mc.xform("L_squint_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_A_C_OFF_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("L_squint_A_B_OFF_CTL"):
			if not mc.getAttr("L_squint_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 2.0816681711721685e-17])
			mc.xform("L_squint_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_A_B_OFF_CTL", r=1, s=[0.9999999999999997, 0.9999999999999998, 0.9999999999999997])

		if mc.objExists("L_squint_A_A_OFF_CTL"):
			if not mc.getAttr("L_squint_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_A_A_OFF_CTL", a=1, t=[0.0, -5.551115123125783e-17, -1.734723475976807e-17])
			mc.xform("L_squint_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_A_A_OFF_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("L_squint_A_CTL"):
			if not mc.getAttr("L_squint_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_squint_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_squint_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_squint_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_squint_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_A_CTL.rotateOrder", 0)

			mc.xform("L_squint_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_squint_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_B_D_OFF_CTL"):
			if not mc.getAttr("L_squint_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_squint_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_B_C_OFF_CTL"):
			if not mc.getAttr("L_squint_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_B_C_OFF_CTL", a=1, t=[6.162975822039155e-33, 0.0, -6.938893903907228e-18])
			mc.xform("L_squint_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_B_C_OFF_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("L_squint_B_B_OFF_CTL"):
			if not mc.getAttr("L_squint_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_B_B_OFF_CTL", a=1, t=[-6.162975822039155e-33, 0.0, -6.938893903907228e-18])
			mc.xform("L_squint_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_B_B_OFF_CTL", r=1, s=[1.0, 0.9999999999999997, 0.9999999999999997])

		if mc.objExists("L_squint_B_A_OFF_CTL"):
			if not mc.getAttr("L_squint_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_B_A_OFF_CTL", a=1, t=[6.162975822039155e-33, 0.0, 0.0])
			mc.xform("L_squint_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_B_A_OFF_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("L_squint_B_CTL"):
			if not mc.getAttr("L_squint_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_squint_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_squint_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_squint_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_squint_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_B_CTL.rotateOrder", 0)

			mc.xform("L_squint_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_squint_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_C_D_OFF_CTL"):
			if not mc.getAttr("L_squint_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_C_D_OFF_CTL", a=1, t=[0.0, 0.0, -3.469446951953614e-18])
			mc.xform("L_squint_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_C_C_OFF_CTL"):
			if not mc.getAttr("L_squint_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_C_C_OFF_CTL", a=1, t=[0.0, 0.0, -3.469446951953614e-18])
			mc.xform("L_squint_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_C_B_OFF_CTL"):
			if not mc.getAttr("L_squint_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_C_B_OFF_CTL", a=1, t=[-5.551115123125783e-17, 5.551115123125783e-17, 2.0816681711721685e-17])
			mc.xform("L_squint_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_squint_C_A_OFF_CTL"):
			if not mc.getAttr("L_squint_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_squint_C_A_OFF_CTL", a=1, t=[5.551115123125783e-17, 0.0, -6.938893903907228e-18])
			mc.xform("L_squint_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_C_A_OFF_CTL", r=1, s=[1.0, 0.9999999999999999, 0.9999999999999999])

		if mc.objExists("L_squint_C_CTL"):
			if not mc.getAttr("L_squint_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_squint_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_squint_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_squint_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_squint_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_squint_C_CTL.rotateOrder", 0)

			mc.xform("L_squint_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_squint_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_squint_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_A_D_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_A_D_OFF_CTL", a=1, t=[5.551115123125783e-17, 0.0, -3.469446951953614e-18])
			mc.xform("L_cheekLower_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_A_D_OFF_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("L_cheekLower_A_C_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 3.469446951953614e-18])
			mc.xform("L_cheekLower_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_A_C_OFF_CTL", r=1, s=[0.9999999999999997, 0.9999999999999997, 0.9999999999999997])

		if mc.objExists("L_cheekLower_A_B_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_A_B_OFF_CTL", a=1, t=[-5.551115123125783e-17, 5.551115123125783e-17, 0.0])
			mc.xform("L_cheekLower_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_A_B_OFF_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("L_cheekLower_A_A_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 3.469446951953614e-18])
			mc.xform("L_cheekLower_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_A_A_OFF_CTL", r=1, s=[1.0, 0.9999999999999998, 0.9999999999999999])

		if mc.objExists("L_cheekLower_A_CTL"):
			if not mc.getAttr("L_cheekLower_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_cheekLower_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_cheekLower_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_cheekLower_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_cheekLower_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_A_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_B_D_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_B_C_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_B_B_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_B_A_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_B_CTL"):
			if not mc.getAttr("L_cheekLower_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_cheekLower_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_cheekLower_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_cheekLower_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_cheekLower_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_B_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_cheekLower_C_D_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_C_D_OFF_CTL", a=1, t=[-5.551115123125783e-17, 0.0, -6.938893903907228e-18])
			mc.xform("L_cheekLower_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_C_D_OFF_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, 0.9999999999999999])

		if mc.objExists("L_cheekLower_C_C_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 6.938893903907228e-18])
			mc.xform("L_cheekLower_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_C_C_OFF_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, 0.9999999999999999])

		if mc.objExists("L_cheekLower_C_B_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_C_B_OFF_CTL", a=1, t=[5.551115123125783e-17, 0.0, 0.0])
			mc.xform("L_cheekLower_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_C_B_OFF_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("L_cheekLower_C_A_OFF_CTL"):
			if not mc.getAttr("L_cheekLower_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 3.469446951953614e-18])
			mc.xform("L_cheekLower_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_C_A_OFF_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, 0.9999999999999999])

		if mc.objExists("L_cheekLower_C_CTL"):
			if not mc.getAttr("L_cheekLower_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_cheekLower_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_cheekLower_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_cheekLower_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_cheekLower_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_cheekLower_C_CTL.rotateOrder", 0)

			mc.xform("L_cheekLower_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_cheekLower_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_D_OFF_CTL"):
			if not mc.getAttr("C_brow_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_brow_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_brow_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_C_OFF_CTL"):
			if not mc.getAttr("C_brow_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_brow_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_brow_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_B_OFF_CTL"):
			if not mc.getAttr("C_brow_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_brow_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_brow_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_A_OFF_CTL"):
			if not mc.getAttr("C_brow_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_brow_A_OFF_CTL", a=1, t=[1.232595164407831e-32, 0.0, 0.0])
			mc.xform("C_brow_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_CTL"):
			if not mc.getAttr("C_brow_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_brow_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_brow_CTL.mirrorMode", l=1):
				mc.setAttr("C_brow_CTL.mirrorMode", 0)

			if not mc.getAttr("C_brow_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_CTL.rotateOrder", 0)

			mc.xform("C_brow_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_brow_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_A_D_OFF_CTL"):
			if not mc.getAttr("L_brow_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_A_D_OFF_CTL", a=1, t=[0.0, -1.734723475976807e-18, -6.938893903907228e-18])
			mc.xform("L_brow_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 0.9999999999999999])

		if mc.objExists("L_brow_A_C_OFF_CTL"):
			if not mc.getAttr("L_brow_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_A_C_OFF_CTL", a=1, t=[0.0, -3.469446951953614e-18, -6.938893903907228e-18])
			mc.xform("L_brow_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 0.9999999999999999])

		if mc.objExists("L_brow_A_B_OFF_CTL"):
			if not mc.getAttr("L_brow_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_A_B_OFF_CTL", a=1, t=[0.0, 6.938893903907228e-18, 1.0408340855860843e-17])
			mc.xform("L_brow_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0000000000000002])

		if mc.objExists("L_brow_A_A_OFF_CTL"):
			if not mc.getAttr("L_brow_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_A_A_OFF_CTL", a=1, t=[0.0, -1.734723475976807e-18, -6.938893903907228e-18])
			mc.xform("L_brow_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 0.9999999999999999])

		if mc.objExists("L_brow_A_CTL"):
			if not mc.getAttr("L_brow_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_brow_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_brow_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_brow_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_brow_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_A_CTL.rotateOrder", 0)

			mc.xform("L_brow_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_B_D_OFF_CTL"):
			if not mc.getAttr("L_brow_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_B_D_OFF_CTL", a=1, t=[5.551115123125783e-17, 3.469446951953614e-17, 0.0])
			mc.xform("L_brow_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_B_C_OFF_CTL"):
			if not mc.getAttr("L_brow_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_B_C_OFF_CTL", a=1, t=[-5.551115123125783e-17, -3.469446951953614e-17, -1.3877787807814457e-17])
			mc.xform("L_brow_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_B_B_OFF_CTL"):
			if not mc.getAttr("L_brow_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_B_B_OFF_CTL", a=1, t=[5.551115123125783e-17, 3.469446951953614e-17, 0.0])
			mc.xform("L_brow_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_B_A_OFF_CTL"):
			if not mc.getAttr("L_brow_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_B_A_OFF_CTL", a=1, t=[-5.551115123125783e-17, 0.0, 0.0])
			mc.xform("L_brow_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_B_CTL"):
			if not mc.getAttr("L_brow_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_brow_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_brow_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_brow_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_brow_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_B_CTL.rotateOrder", 0)

			mc.xform("L_brow_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_C_D_OFF_CTL"):
			if not mc.getAttr("L_brow_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_C_D_OFF_CTL", a=1, t=[2.220446049250313e-16, 2.7755575615628914e-17, 0.0])
			mc.xform("L_brow_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_C_D_OFF_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0])

		if mc.objExists("L_brow_C_C_OFF_CTL"):
			if not mc.getAttr("L_brow_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_C_C_OFF_CTL", a=1, t=[-1.1102230246251565e-16, -3.8163916471489756e-17, 0.0])
			mc.xform("L_brow_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_C_C_OFF_CTL", r=1, s=[0.9999999999999999, 1.0, 1.0])

		if mc.objExists("L_brow_C_B_OFF_CTL"):
			if not mc.getAttr("L_brow_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_C_B_OFF_CTL", a=1, t=[-1.1102230246251565e-16, 3.8163916471489756e-17, -5.551115123125783e-17])
			mc.xform("L_brow_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_C_B_OFF_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, 1.0])

		if mc.objExists("L_brow_C_A_OFF_CTL"):
			if not mc.getAttr("L_brow_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_C_A_OFF_CTL", a=1, t=[1.1102230246251565e-16, -1.734723475976807e-17, 0.0])
			mc.xform("L_brow_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_C_A_OFF_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("L_brow_C_CTL"):
			if not mc.getAttr("L_brow_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_brow_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_brow_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_brow_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_brow_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_C_CTL.rotateOrder", 0)

			mc.xform("L_brow_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_A_D_OFF_CTL"):
			if not mc.getAttr("R_brow_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_A_D_OFF_CTL", a=1, t=[-2.7755575615628914e-17, 6.938893903907228e-18, 3.469446951953614e-18])
			mc.xform("R_brow_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_A_D_OFF_CTL", r=1, s=[0.9999999999999997, 0.9999999999999994, 0.9999999999999996])

		if mc.objExists("R_brow_A_C_OFF_CTL"):
			if not mc.getAttr("R_brow_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_A_C_OFF_CTL", a=1, t=[0.0, -6.938893903907228e-18, -6.938893903907228e-18])
			mc.xform("R_brow_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_A_C_OFF_CTL", r=1, s=[1.0000000000000002, 1.0000000000000004, 1.0000000000000004])

		if mc.objExists("R_brow_A_B_OFF_CTL"):
			if not mc.getAttr("R_brow_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_A_B_OFF_CTL", a=1, t=[0.0, 5.204170427930421e-18, 3.469446951953614e-18])
			mc.xform("R_brow_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_A_B_OFF_CTL", r=1, s=[0.9999999999999999, 0.9999999999999997, 0.9999999999999997])

		if mc.objExists("R_brow_A_A_OFF_CTL"):
			if not mc.getAttr("R_brow_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_A_A_OFF_CTL", a=1, t=[2.7755575615628914e-17, -3.469446951953614e-18, -3.469446951953614e-18])
			mc.xform("R_brow_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_A_A_OFF_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_brow_A_CTL"):
			if not mc.getAttr("R_brow_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_brow_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_brow_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_brow_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_brow_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_A_CTL.rotateOrder", 0)

			mc.xform("R_brow_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_B_D_OFF_CTL"):
			if not mc.getAttr("R_brow_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_B_D_OFF_CTL", a=1, t=[-5.551115123125783e-17, -2.42861286636753e-17, 6.938893903907228e-18])
			mc.xform("R_brow_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_B_C_OFF_CTL"):
			if not mc.getAttr("R_brow_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_B_C_OFF_CTL", a=1, t=[-5.551115123125783e-17, 3.469446951953614e-18, 2.0816681711721685e-17])
			mc.xform("R_brow_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_B_B_OFF_CTL"):
			if not mc.getAttr("R_brow_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_B_B_OFF_CTL", a=1, t=[1.1102230246251565e-16, 1.0408340855860843e-17, 6.938893903907228e-18])
			mc.xform("R_brow_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_B_A_OFF_CTL"):
			if not mc.getAttr("R_brow_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_B_A_OFF_CTL", a=1, t=[-5.551115123125783e-17, -1.0408340855860843e-17, 6.938893903907228e-18])
			mc.xform("R_brow_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_B_CTL"):
			if not mc.getAttr("R_brow_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_brow_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_brow_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_brow_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_brow_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_B_CTL.rotateOrder", 0)

			mc.xform("R_brow_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_C_D_OFF_CTL"):
			if not mc.getAttr("R_brow_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_C_D_OFF_CTL", a=1, t=[1.1102230246251565e-16, -2.7755575615628914e-17, 0.0])
			mc.xform("R_brow_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_C_D_OFF_CTL", r=1, s=[1.0, 0.9999999999999998, 1.0000000000000002])

		if mc.objExists("R_brow_C_C_OFF_CTL"):
			if not mc.getAttr("R_brow_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_C_C_OFF_CTL", a=1, t=[-1.1102230246251565e-16, -6.938893903907228e-18, 2.7755575615628914e-17])
			mc.xform("R_brow_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_C_C_OFF_CTL", r=1, s=[1.0, 1.0000000000000004, 1.0])

		if mc.objExists("R_brow_C_B_OFF_CTL"):
			if not mc.getAttr("R_brow_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_C_B_OFF_CTL", a=1, t=[0.0, 2.0816681711721685e-17, -2.7755575615628914e-17])
			mc.xform("R_brow_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_C_B_OFF_CTL", r=1, s=[0.9999999999999998, 0.9999999999999996, 0.9999999999999999])

		if mc.objExists("R_brow_C_A_OFF_CTL"):
			if not mc.getAttr("R_brow_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_C_A_OFF_CTL", a=1, t=[0.0, 3.469446951953614e-18, 0.0])
			mc.xform("R_brow_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_C_A_OFF_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0])

		if mc.objExists("R_brow_C_CTL"):
			if not mc.getAttr("R_brow_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_brow_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_brow_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_brow_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_brow_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_C_CTL.rotateOrder", 0)

			mc.xform("R_brow_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_upper_D_OFF_CTL"):
			if not mc.getAttr("C_brow_upper_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_upper_D_OFF_CTL.rotateOrder", 0)

			mc.xform("C_brow_upper_D_OFF_CTL", a=1, t=[-1.232595164407831e-32, 0.0, 0.0])
			mc.xform("C_brow_upper_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_upper_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_upper_C_OFF_CTL"):
			if not mc.getAttr("C_brow_upper_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_upper_C_OFF_CTL.rotateOrder", 0)

			mc.xform("C_brow_upper_C_OFF_CTL", a=1, t=[1.232595164407831e-32, 0.0, 0.0])
			mc.xform("C_brow_upper_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_upper_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_upper_B_OFF_CTL"):
			if not mc.getAttr("C_brow_upper_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_upper_B_OFF_CTL.rotateOrder", 0)

			mc.xform("C_brow_upper_B_OFF_CTL", a=1, t=[-1.232595164407831e-32, 0.0, 0.0])
			mc.xform("C_brow_upper_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_upper_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_upper_A_OFF_CTL"):
			if not mc.getAttr("C_brow_upper_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_upper_A_OFF_CTL.rotateOrder", 0)

			mc.xform("C_brow_upper_A_OFF_CTL", a=1, t=[1.232595164407831e-32, 0.0, 0.0])
			mc.xform("C_brow_upper_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_upper_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_brow_upper_CTL"):
			if not mc.getAttr("C_brow_upper_CTL.numOffsetCtrls", l=1):
				mc.setAttr("C_brow_upper_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("C_brow_upper_CTL.mirrorMode", l=1):
				mc.setAttr("C_brow_upper_CTL.mirrorMode", 0)

			if not mc.getAttr("C_brow_upper_CTL.rotateOrder", l=1):
				mc.setAttr("C_brow_upper_CTL.rotateOrder", 0)

			mc.xform("C_brow_upper_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_brow_upper_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_brow_upper_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_A_D_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 1.3877787807814457e-17])
			mc.xform("L_brow_upper_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_A_C_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 1.3877787807814457e-17])
			mc.xform("L_brow_upper_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_A_B_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 1.3877787807814457e-17])
			mc.xform("L_brow_upper_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_A_A_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_A_A_OFF_CTL", a=1, t=[0.0, -5.551115123125783e-17, -1.3877787807814457e-17])
			mc.xform("L_brow_upper_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_A_CTL"):
			if not mc.getAttr("L_brow_upper_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_brow_upper_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_brow_upper_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_brow_upper_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_brow_upper_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_A_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_B_D_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_B_D_OFF_CTL", a=1, t=[-5.551115123125783e-17, 5.551115123125783e-17, 4.163336342344337e-17])
			mc.xform("L_brow_upper_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0000000000000004])

		if mc.objExists("L_brow_upper_B_C_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_B_C_OFF_CTL", a=1, t=[0.0, 0.0, -6.938893903907228e-17])
			mc.xform("L_brow_upper_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_B_C_OFF_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 0.9999999999999999])

		if mc.objExists("L_brow_upper_B_B_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_B_B_OFF_CTL", a=1, t=[0.0, -5.551115123125783e-17, 5.551115123125783e-17])
			mc.xform("L_brow_upper_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_B_B_OFF_CTL", r=1, s=[0.9999999999999999, 0.9999999999999996, 1.0])

		if mc.objExists("L_brow_upper_B_A_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_B_A_OFF_CTL", a=1, t=[5.551115123125783e-17, 0.0, -1.3877787807814457e-17])
			mc.xform("L_brow_upper_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_B_A_OFF_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0])

		if mc.objExists("L_brow_upper_B_CTL"):
			if not mc.getAttr("L_brow_upper_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_brow_upper_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_brow_upper_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_brow_upper_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_brow_upper_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_B_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_brow_upper_C_D_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_C_D_OFF_CTL", a=1, t=[0.0, -5.551115123125783e-17, 0.0])
			mc.xform("L_brow_upper_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_C_D_OFF_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("L_brow_upper_C_C_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_C_C_OFF_CTL", a=1, t=[0.0, 5.551115123125783e-17, -8.326672684688674e-17])
			mc.xform("L_brow_upper_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_C_C_OFF_CTL", r=1, s=[1.0, 0.9999999999999999, 0.9999999999999998])

		if mc.objExists("L_brow_upper_C_B_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_C_B_OFF_CTL", a=1, t=[1.1102230246251565e-16, -5.551115123125783e-17, 1.3877787807814457e-16])
			mc.xform("L_brow_upper_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_C_B_OFF_CTL", r=1, s=[1.0, 0.9999999999999999, 1.0])

		if mc.objExists("L_brow_upper_C_A_OFF_CTL"):
			if not mc.getAttr("L_brow_upper_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_C_A_OFF_CTL", a=1, t=[-5.551115123125783e-17, 5.551115123125783e-17, -5.551115123125783e-17])
			mc.xform("L_brow_upper_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_C_A_OFF_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("L_brow_upper_C_CTL"):
			if not mc.getAttr("L_brow_upper_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("L_brow_upper_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("L_brow_upper_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_brow_upper_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_brow_upper_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_brow_upper_C_CTL.rotateOrder", 0)

			mc.xform("L_brow_upper_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_brow_upper_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_upper_A_D_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_A_D_OFF_CTL", a=1, t=[0.0, -5.551115123125783e-17, -9.020562075079397e-17])
			mc.xform("R_brow_upper_A_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_A_D_OFF_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, 1.0])

		if mc.objExists("R_brow_upper_A_C_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 5.204170427930421e-17])
			mc.xform("R_brow_upper_A_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_A_C_OFF_CTL", r=1, s=[1.0000000000000002, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_brow_upper_A_B_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_A_B_OFF_CTL", a=1, t=[-5.551115123125783e-17, 5.551115123125783e-17, 1.3877787807814457e-17])
			mc.xform("R_brow_upper_A_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_A_B_OFF_CTL", r=1, s=[0.9999999999999999, 0.9999999999999998, 0.9999999999999999])

		if mc.objExists("R_brow_upper_A_A_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_A_A_OFF_CTL", a=1, t=[5.551115123125783e-17, -5.551115123125783e-17, 2.0816681711721685e-17])
			mc.xform("R_brow_upper_A_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 0.9999999999999999])

		if mc.objExists("R_brow_upper_A_CTL"):
			if not mc.getAttr("R_brow_upper_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_brow_upper_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_brow_upper_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_brow_upper_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_brow_upper_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_A_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_upper_B_D_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_B_D_OFF_CTL", a=1, t=[5.551115123125783e-17, 1.1102230246251565e-16, -1.3877787807814457e-17])
			mc.xform("R_brow_upper_B_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_upper_B_C_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_B_C_OFF_CTL", a=1, t=[-5.551115123125783e-17, -1.1102230246251565e-16, 1.3877787807814457e-17])
			mc.xform("R_brow_upper_B_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_upper_B_B_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_B_B_OFF_CTL", a=1, t=[5.551115123125783e-17, 1.1102230246251565e-16, -1.3877787807814457e-17])
			mc.xform("R_brow_upper_B_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_upper_B_A_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_B_A_OFF_CTL", a=1, t=[0.0, -1.1102230246251565e-16, 2.7755575615628914e-17])
			mc.xform("R_brow_upper_B_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_upper_B_CTL"):
			if not mc.getAttr("R_brow_upper_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_brow_upper_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_brow_upper_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_brow_upper_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_brow_upper_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_B_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_B_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_brow_upper_C_D_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_C_D_OFF_CTL", a=1, t=[-5.551115123125783e-17, 0.0, 0.0])
			mc.xform("R_brow_upper_C_D_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_C_D_OFF_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000004])

		if mc.objExists("R_brow_upper_C_C_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_C_C_OFF_CTL", a=1, t=[0.0, 0.0, -5.551115123125783e-17])
			mc.xform("R_brow_upper_C_C_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_C_C_OFF_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, 0.9999999999999997])

		if mc.objExists("R_brow_upper_C_B_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_C_B_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_C_B_OFF_CTL", r=1, s=[1.0, 0.9999999999999999, 1.0000000000000002])

		if mc.objExists("R_brow_upper_C_A_OFF_CTL"):
			if not mc.getAttr("R_brow_upper_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_C_A_OFF_CTL", a=1, t=[5.551115123125783e-17, 0.0, 0.0])
			mc.xform("R_brow_upper_C_A_OFF_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_C_A_OFF_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0])

		if mc.objExists("R_brow_upper_C_CTL"):
			if not mc.getAttr("R_brow_upper_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_brow_upper_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_brow_upper_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_brow_upper_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_brow_upper_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_brow_upper_C_CTL.rotateOrder", 0)

			mc.xform("R_brow_upper_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_brow_upper_C_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_eye_FK_D_OFF_CTL"):
			if not mc.getAttr("R_eye_FK_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_eye_FK_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_eye_FK_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_eye_FK_D_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_eye_FK_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_eye_FK_C_OFF_CTL"):
			if not mc.getAttr("R_eye_FK_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_eye_FK_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_eye_FK_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_eye_FK_C_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_eye_FK_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_eye_FK_B_OFF_CTL"):
			if not mc.getAttr("R_eye_FK_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_eye_FK_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_eye_FK_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_eye_FK_B_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_eye_FK_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_eye_FK_A_OFF_CTL"):
			if not mc.getAttr("R_eye_FK_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_eye_FK_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_eye_FK_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_eye_FK_A_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_eye_FK_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_eye_FK_CTL"):
			if not mc.getAttr("R_eye_FK_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_eye_FK_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_eye_FK_CTL.mirrorMode", l=1):
				mc.setAttr("R_eye_FK_CTL.mirrorMode", 0)

			if not mc.getAttr("R_eye_FK_CTL.rotateOrder", l=1):
				mc.setAttr("R_eye_FK_CTL.rotateOrder", 0)

			mc.xform("R_eye_FK_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_eye_FK_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_eye_FK_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lookAt_D_OFF_CTL"):
			if not mc.getAttr("R_lookAt_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lookAt_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lookAt_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lookAt_D_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lookAt_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lookAt_C_OFF_CTL"):
			if not mc.getAttr("R_lookAt_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lookAt_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lookAt_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lookAt_C_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lookAt_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lookAt_B_OFF_CTL"):
			if not mc.getAttr("R_lookAt_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lookAt_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lookAt_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lookAt_B_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lookAt_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lookAt_A_OFF_CTL"):
			if not mc.getAttr("R_lookAt_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lookAt_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lookAt_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lookAt_A_OFF_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lookAt_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lookAt_CTL"):
			if not mc.getAttr("R_lookAt_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lookAt_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lookAt_CTL.mirrorMode", l=1):
				mc.setAttr("R_lookAt_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lookAt_CTL.rotateOrder", l=1):
				mc.setAttr("R_lookAt_CTL.rotateOrder", 0)

			mc.xform("R_lookAt_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lookAt_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lookAt_CTL", r=1, s=[1.0, 0.9999999999999998, 1.0])

		if mc.objExists("R_innerLid_D_OFF_CTL"):
			if not mc.getAttr("R_innerLid_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_innerLid_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_innerLid_D_OFF_CTL", a=1, t=[0.0, -1.7763568394002505e-15, 0.0])
			mc.xform("R_innerLid_D_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_innerLid_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_innerLid_C_OFF_CTL"):
			if not mc.getAttr("R_innerLid_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_innerLid_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_innerLid_C_OFF_CTL", a=1, t=[0.0, 1.7763568394002505e-15, 0.0])
			mc.xform("R_innerLid_C_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_innerLid_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_innerLid_B_OFF_CTL"):
			if not mc.getAttr("R_innerLid_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_innerLid_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_innerLid_B_OFF_CTL", a=1, t=[0.0, -1.7763568394002505e-15, 0.0])
			mc.xform("R_innerLid_B_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_innerLid_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_innerLid_A_OFF_CTL"):
			if not mc.getAttr("R_innerLid_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_innerLid_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_innerLid_A_OFF_CTL", a=1, t=[2.220446049250313e-16, 1.7763568394002505e-15, 0.0])
			mc.xform("R_innerLid_A_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_innerLid_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_innerLid_CTL"):
			if not mc.getAttr("R_innerLid_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_innerLid_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_innerLid_CTL.mirrorMode", l=1):
				mc.setAttr("R_innerLid_CTL.mirrorMode", 0)

			if not mc.getAttr("R_innerLid_CTL.rotateOrder", l=1):
				mc.setAttr("R_innerLid_CTL.rotateOrder", 0)

			mc.xform("R_innerLid_CTL", a=1, t=[2.6645352591003757e-15, 1.7763568394002505e-15, 0.0])
			mc.xform("R_innerLid_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_innerLid_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_outterLid_D_OFF_CTL"):
			if not mc.getAttr("R_outterLid_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_outterLid_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_outterLid_D_OFF_CTL", a=1, t=[0.0, -1.7763568394002505e-15, 0.0])
			mc.xform("R_outterLid_D_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_outterLid_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_outterLid_C_OFF_CTL"):
			if not mc.getAttr("R_outterLid_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_outterLid_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_outterLid_C_OFF_CTL", a=1, t=[0.0, 1.7763568394002505e-15, 0.0])
			mc.xform("R_outterLid_C_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_outterLid_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_outterLid_B_OFF_CTL"):
			if not mc.getAttr("R_outterLid_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_outterLid_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_outterLid_B_OFF_CTL", a=1, t=[0.0, -1.7763568394002505e-15, 0.0])
			mc.xform("R_outterLid_B_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_outterLid_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_outterLid_A_OFF_CTL"):
			if not mc.getAttr("R_outterLid_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_outterLid_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_outterLid_A_OFF_CTL", a=1, t=[0.0, 1.7763568394002505e-15, 0.0])
			mc.xform("R_outterLid_A_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_outterLid_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_outterLid_CTL"):
			if not mc.getAttr("R_outterLid_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_outterLid_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_outterLid_CTL.mirrorMode", l=1):
				mc.setAttr("R_outterLid_CTL.mirrorMode", 0)

			if not mc.getAttr("R_outterLid_CTL.rotateOrder", l=1):
				mc.setAttr("R_outterLid_CTL.rotateOrder", 0)

			mc.xform("R_outterLid_CTL", a=1, t=[2.6645352591003757e-15, 8.881784197001252e-15, -1.1102230246251565e-16])
			mc.xform("R_outterLid_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_outterLid_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_upperLid_A_D_OFF_CTL"):
			if not mc.getAttr("R_upperLid_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLid_A_D_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_A_C_OFF_CTL"):
			if not mc.getAttr("R_upperLid_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLid_A_C_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_A_B_OFF_CTL"):
			if not mc.getAttr("R_upperLid_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLid_A_B_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_A_A_OFF_CTL"):
			if not mc.getAttr("R_upperLid_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLid_A_A_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_A_CTL"):
			if not mc.getAttr("R_upperLid_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upperLid_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upperLid_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_upperLid_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upperLid_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_A_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_A_CTL", a=1, t=[-8.881784197001252e-16, 3.552713678800501e-15, 1.1102230246251565e-16])
			mc.xform("R_upperLid_A_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upperLid_A_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_upperLid_B_D_OFF_CTL"):
			if not mc.getAttr("R_upperLid_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_B_D_OFF_CTL", a=1, t=[0.0, 0.0, -5.551115123125783e-17])
			mc.xform("R_upperLid_B_D_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_B_C_OFF_CTL"):
			if not mc.getAttr("R_upperLid_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 5.551115123125783e-17])
			mc.xform("R_upperLid_B_C_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_B_B_OFF_CTL"):
			if not mc.getAttr("R_upperLid_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_B_B_OFF_CTL", a=1, t=[0.0, 0.0, -5.551115123125783e-17])
			mc.xform("R_upperLid_B_B_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_B_A_OFF_CTL"):
			if not mc.getAttr("R_upperLid_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 5.551115123125783e-17])
			mc.xform("R_upperLid_B_A_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_B_CTL"):
			if not mc.getAttr("R_upperLid_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upperLid_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upperLid_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_upperLid_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upperLid_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_B_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_B_CTL", a=1, t=[0.0, -7.105427357601002e-15, 0.0])
			mc.xform("R_upperLid_B_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upperLid_B_CTL", r=1, s=[1.0, 1.0, 1.0000000000000002])

		if mc.objExists("R_upperLid_C_D_OFF_CTL"):
			if not mc.getAttr("R_upperLid_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLid_C_D_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_C_C_OFF_CTL"):
			if not mc.getAttr("R_upperLid_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLid_C_C_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_C_B_OFF_CTL"):
			if not mc.getAttr("R_upperLid_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLid_C_B_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_C_A_OFF_CTL"):
			if not mc.getAttr("R_upperLid_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_upperLid_C_A_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLid_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLid_C_CTL"):
			if not mc.getAttr("R_upperLid_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upperLid_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upperLid_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_upperLid_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upperLid_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLid_C_CTL.rotateOrder", 0)

			mc.xform("R_upperLid_C_CTL", a=1, t=[0.0, 7.105427357601002e-15, 2.7755575615628914e-16])
			mc.xform("R_upperLid_C_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upperLid_C_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_lowerLid_A_D_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_A_D_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_A_C_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_A_C_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_A_B_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_A_B_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_A_A_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_A_A_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_A_CTL"):
			if not mc.getAttr("R_lowerLid_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lowerLid_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lowerLid_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_lowerLid_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lowerLid_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_A_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_A_CTL", a=1, t=[-8.881784197001252e-16, 3.552713678800501e-15, 0.0])
			mc.xform("R_lowerLid_A_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lowerLid_A_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_lowerLid_B_D_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_B_D_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_B_C_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_B_C_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_B_B_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_B_B_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_B_A_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_B_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_B_A_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_B_CTL"):
			if not mc.getAttr("R_lowerLid_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lowerLid_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lowerLid_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_lowerLid_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lowerLid_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_B_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_B_CTL", a=1, t=[1.7763568394002505e-15, 8.881784197001252e-15, -1.1102230246251565e-16])
			mc.xform("R_lowerLid_B_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lowerLid_B_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_lowerLid_C_D_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_C_D_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_C_C_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_C_C_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_C_B_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_C_B_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_C_A_OFF_CTL"):
			if not mc.getAttr("R_lowerLid_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLid_C_A_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLid_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLid_C_CTL"):
			if not mc.getAttr("R_lowerLid_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lowerLid_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lowerLid_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_lowerLid_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lowerLid_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLid_C_CTL.rotateOrder", 0)

			mc.xform("R_lowerLid_C_CTL", a=1, t=[8.881784197001252e-16, 3.552713678800501e-15, 0.0])
			mc.xform("R_lowerLid_C_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lowerLid_C_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_upperLidPrimary_D_OFF_CTL"):
			if not mc.getAttr("R_upperLidPrimary_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLidPrimary_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLidPrimary_D_OFF_CTL", a=1, t=[0.0, 0.0, -5.551115123125783e-17])
			mc.xform("R_upperLidPrimary_D_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLidPrimary_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLidPrimary_C_OFF_CTL"):
			if not mc.getAttr("R_upperLidPrimary_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLidPrimary_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLidPrimary_C_OFF_CTL", a=1, t=[0.0, 0.0, 5.551115123125783e-17])
			mc.xform("R_upperLidPrimary_C_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLidPrimary_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLidPrimary_B_OFF_CTL"):
			if not mc.getAttr("R_upperLidPrimary_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLidPrimary_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLidPrimary_B_OFF_CTL", a=1, t=[0.0, 0.0, -5.551115123125783e-17])
			mc.xform("R_upperLidPrimary_B_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLidPrimary_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLidPrimary_A_OFF_CTL"):
			if not mc.getAttr("R_upperLidPrimary_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLidPrimary_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_upperLidPrimary_A_OFF_CTL", a=1, t=[0.0, 0.0, 5.551115123125783e-17])
			mc.xform("R_upperLidPrimary_A_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_upperLidPrimary_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_upperLidPrimary_CTL"):
			if not mc.getAttr("R_upperLidPrimary_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_upperLidPrimary_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_upperLidPrimary_CTL.mirrorMode", l=1):
				mc.setAttr("R_upperLidPrimary_CTL.mirrorMode", 0)

			if not mc.getAttr("R_upperLidPrimary_CTL.rotateOrder", l=1):
				mc.setAttr("R_upperLidPrimary_CTL.rotateOrder", 0)

			mc.xform("R_upperLidPrimary_CTL", a=1, t=[0.0, -7.105427357601002e-15, 0.0])
			mc.xform("R_upperLidPrimary_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_upperLidPrimary_CTL", r=1, s=[1.0, 1.0, 1.0000000000000002])

		if mc.objExists("R_lowerLidPrimary_D_OFF_CTL"):
			if not mc.getAttr("R_lowerLidPrimary_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLidPrimary_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLidPrimary_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLidPrimary_D_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLidPrimary_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLidPrimary_C_OFF_CTL"):
			if not mc.getAttr("R_lowerLidPrimary_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLidPrimary_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLidPrimary_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLidPrimary_C_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLidPrimary_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLidPrimary_B_OFF_CTL"):
			if not mc.getAttr("R_lowerLidPrimary_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLidPrimary_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLidPrimary_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLidPrimary_B_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLidPrimary_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLidPrimary_A_OFF_CTL"):
			if not mc.getAttr("R_lowerLidPrimary_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLidPrimary_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_lowerLidPrimary_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_lowerLidPrimary_A_OFF_CTL", a=1, ro=[1.4033418597069752e-14, -0.0, -0.0])
			mc.xform("R_lowerLidPrimary_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_lowerLidPrimary_CTL"):
			if not mc.getAttr("R_lowerLidPrimary_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_lowerLidPrimary_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_lowerLidPrimary_CTL.mirrorMode", l=1):
				mc.setAttr("R_lowerLidPrimary_CTL.mirrorMode", 0)

			if not mc.getAttr("R_lowerLidPrimary_CTL.rotateOrder", l=1):
				mc.setAttr("R_lowerLidPrimary_CTL.rotateOrder", 0)

			mc.xform("R_lowerLidPrimary_CTL", a=1, t=[1.7763568394002505e-15, 8.881784197001252e-15, -1.1102230246251565e-16])
			mc.xform("R_lowerLidPrimary_CTL", a=1, ro=[0.0, -0.0, 0.0])
			mc.xform("R_lowerLidPrimary_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0000000000000002])

		if mc.objExists("R_cheek_A_D_OFF_CTL"):
			if not mc.getAttr("R_cheek_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheek_A_D_OFF_CTL", a=1, ro=[-3.975693351829396e-16, 2.758691436281349e-33, 7.951386703658792e-16])
			mc.xform("R_cheek_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_A_C_OFF_CTL"):
			if not mc.getAttr("R_cheek_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheek_A_C_OFF_CTL", a=1, ro=[-3.975693351829396e-16, 2.758691436281349e-33, 7.951386703658792e-16])
			mc.xform("R_cheek_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_A_B_OFF_CTL"):
			if not mc.getAttr("R_cheek_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheek_A_B_OFF_CTL", a=1, ro=[-3.975693351829396e-16, 2.758691436281349e-33, 7.951386703658792e-16])
			mc.xform("R_cheek_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_A_A_OFF_CTL"):
			if not mc.getAttr("R_cheek_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheek_A_A_OFF_CTL", a=1, ro=[-3.975693351829396e-16, 2.758691436281349e-33, 7.951386703658792e-16])
			mc.xform("R_cheek_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_A_CTL"):
			if not mc.getAttr("R_cheek_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_cheek_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_cheek_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_cheek_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_cheek_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_A_CTL.rotateOrder", 0)

			mc.xform("R_cheek_A_CTL", a=1, t=[-6.661338147750939e-16, -8.881784197001252e-16, 2.220446049250313e-16])
			mc.xform("R_cheek_A_CTL", a=1, ro=[-3.4483642953516847e-34, -4.969616689786744e-17, 7.95138670365879e-16])
			mc.xform("R_cheek_A_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_B_D_OFF_CTL"):
			if not mc.getAttr("R_cheek_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheek_B_D_OFF_CTL", a=1, ro=[-1.651899868878668e-13, -8.746525375382232e-12, -9.417356915011434e-07])
			mc.xform("R_cheek_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_B_C_OFF_CTL"):
			if not mc.getAttr("R_cheek_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheek_B_C_OFF_CTL", a=1, ro=[-1.651899868878668e-13, -8.746525375382232e-12, -9.417356915011434e-07])
			mc.xform("R_cheek_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_B_B_OFF_CTL"):
			if not mc.getAttr("R_cheek_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheek_B_B_OFF_CTL", a=1, ro=[-1.651899868878668e-13, -8.746525375382232e-12, -9.417356915011434e-07])
			mc.xform("R_cheek_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_B_A_OFF_CTL"):
			if not mc.getAttr("R_cheek_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_B_A_OFF_CTL", a=1, t=[0.0, 0.0, -1.1102230246251565e-16])
			mc.xform("R_cheek_B_A_OFF_CTL", a=1, ro=[-1.651899868878668e-13, -8.746525375382232e-12, -9.417356915011434e-07])
			mc.xform("R_cheek_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_B_CTL"):
			if not mc.getAttr("R_cheek_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_cheek_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_cheek_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_cheek_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_cheek_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_B_CTL.rotateOrder", 0)

			mc.xform("R_cheek_B_CTL", a=1, t=[6.661338147750939e-16, -4.440892098500626e-16, -9.992007221626409e-16])
			mc.xform("R_cheek_B_CTL", a=1, ro=[4.4139062980501586e-32, -6.3611093629270335e-15, -7.951386703658792e-16])
			mc.xform("R_cheek_B_CTL", r=1, s=[0.9999999999999999, 1.0000000000000004, 1.0])

		if mc.objExists("R_cheek_C_D_OFF_CTL"):
			if not mc.getAttr("R_cheek_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_C_D_OFF_CTL", a=1, t=[-2.220446049250313e-16, -4.440892098500626e-16, 0.0])
			mc.xform("R_cheek_C_D_OFF_CTL", a=1, ro=[-2.1866313435061676e-15, 1.517280289954742e-32, 7.951386703658792e-16])
			mc.xform("R_cheek_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_C_C_OFF_CTL"):
			if not mc.getAttr("R_cheek_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_C_C_OFF_CTL", a=1, t=[0.0, 4.440892098500626e-16, -2.220446049250313e-16])
			mc.xform("R_cheek_C_C_OFF_CTL", a=1, ro=[-2.1866313435061676e-15, 1.517280289954742e-32, 7.951386703658792e-16])
			mc.xform("R_cheek_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_C_B_OFF_CTL"):
			if not mc.getAttr("R_cheek_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_C_B_OFF_CTL", a=1, t=[-2.220446049250313e-16, -4.440892098500626e-16, 0.0])
			mc.xform("R_cheek_C_B_OFF_CTL", a=1, ro=[-2.1866313435061676e-15, 1.517280289954742e-32, 7.951386703658792e-16])
			mc.xform("R_cheek_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_C_A_OFF_CTL"):
			if not mc.getAttr("R_cheek_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheek_C_A_OFF_CTL", a=1, t=[0.0, 4.440892098500626e-16, -2.220446049250313e-16])
			mc.xform("R_cheek_C_A_OFF_CTL", a=1, ro=[-2.1866313435061676e-15, 1.517280289954742e-32, 7.951386703658792e-16])
			mc.xform("R_cheek_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheek_C_CTL"):
			if not mc.getAttr("R_cheek_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_cheek_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_cheek_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_cheek_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_cheek_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheek_C_CTL.rotateOrder", 0)

			mc.xform("R_cheek_C_CTL", a=1, t=[-6.661338147750939e-16, 1.3322676295501878e-15, 0.0])
			mc.xform("R_cheek_C_CTL", a=1, ro=[2.7034714792439894e-14, -2.9817700138720494e-16, 1.1927080055488188e-15])
			mc.xform("R_cheek_C_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0])

		if mc.objExists("R_squint_A_D_OFF_CTL"):
			if not mc.getAttr("R_squint_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_squint_A_D_OFF_CTL", a=1, ro=[9.93923337957349e-16, 3.4483642953516864e-33, -3.975693351829396e-16])
			mc.xform("R_squint_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_A_C_OFF_CTL"):
			if not mc.getAttr("R_squint_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_squint_A_C_OFF_CTL", a=1, ro=[9.93923337957349e-16, 3.4483642953516864e-33, -3.975693351829396e-16])
			mc.xform("R_squint_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_A_B_OFF_CTL"):
			if not mc.getAttr("R_squint_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_squint_A_B_OFF_CTL", a=1, ro=[9.93923337957349e-16, 3.4483642953516864e-33, -3.975693351829396e-16])
			mc.xform("R_squint_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_A_A_OFF_CTL"):
			if not mc.getAttr("R_squint_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_A_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_squint_A_A_OFF_CTL", a=1, ro=[9.93923337957349e-16, 3.4483642953516864e-33, -3.975693351829396e-16])
			mc.xform("R_squint_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_A_CTL"):
			if not mc.getAttr("R_squint_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_squint_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_squint_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_squint_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_squint_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_A_CTL.rotateOrder", 0)

			mc.xform("R_squint_A_CTL", a=1, t=[2.220446049250313e-16, 8.881784197001252e-16, 0.0])
			mc.xform("R_squint_A_CTL", a=1, ro=[0.0, 0.0, -3.975693351829396e-16])
			mc.xform("R_squint_A_CTL", r=1, s=[0.9999999999999996, 0.9999999999999998, 1.0])

		if mc.objExists("R_squint_B_D_OFF_CTL"):
			if not mc.getAttr("R_squint_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_B_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_squint_B_D_OFF_CTL", a=1, ro=[-3.972515668245143e-31, -2.5444437451708134e-14, 1.7890620083232284e-15])
			mc.xform("R_squint_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_B_C_OFF_CTL"):
			if not mc.getAttr("R_squint_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_B_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_squint_B_C_OFF_CTL", a=1, ro=[-3.972515668245143e-31, -2.5444437451708134e-14, 1.7890620083232284e-15])
			mc.xform("R_squint_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_B_B_OFF_CTL"):
			if not mc.getAttr("R_squint_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_B_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_squint_B_B_OFF_CTL", a=1, ro=[-3.972515668245143e-31, -2.5444437451708134e-14, 1.7890620083232284e-15])
			mc.xform("R_squint_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_B_A_OFF_CTL"):
			if not mc.getAttr("R_squint_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_B_A_OFF_CTL", a=1, t=[-2.220446049250313e-16, 0.0, 2.220446049250313e-16])
			mc.xform("R_squint_B_A_OFF_CTL", a=1, ro=[-3.972515668245143e-31, -2.5444437451708134e-14, 1.7890620083232284e-15])
			mc.xform("R_squint_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_B_CTL"):
			if not mc.getAttr("R_squint_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_squint_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_squint_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_squint_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_squint_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_B_CTL.rotateOrder", 0)

			mc.xform("R_squint_B_CTL", a=1, t=[-2.220446049250313e-16, 8.881784197001252e-16, -6.661338147750939e-16])
			mc.xform("R_squint_B_CTL", a=1, ro=[2.2069531490250793e-32, -6.3611093629270335e-15, -3.975693351829396e-16])
			mc.xform("R_squint_B_CTL", r=1, s=[1.0000000000000004, 1.0000000000000004, 1.0000000000000004])

		if mc.objExists("R_squint_C_D_OFF_CTL"):
			if not mc.getAttr("R_squint_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_squint_C_D_OFF_CTL", a=1, ro=[9.939233379573479e-17, 1.2722218725854067e-14, -9.93923337957349e-16])
			mc.xform("R_squint_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_C_C_OFF_CTL"):
			if not mc.getAttr("R_squint_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_squint_C_C_OFF_CTL", a=1, ro=[9.939233379573479e-17, 1.2722218725854067e-14, -9.93923337957349e-16])
			mc.xform("R_squint_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_C_B_OFF_CTL"):
			if not mc.getAttr("R_squint_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_squint_C_B_OFF_CTL", a=1, ro=[9.939233379573479e-17, 1.2722218725854067e-14, -9.93923337957349e-16])
			mc.xform("R_squint_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_C_A_OFF_CTL"):
			if not mc.getAttr("R_squint_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_squint_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_squint_C_A_OFF_CTL", a=1, ro=[9.939233379573479e-17, 1.2722218725854067e-14, -9.93923337957349e-16])
			mc.xform("R_squint_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_squint_C_CTL"):
			if not mc.getAttr("R_squint_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_squint_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_squint_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_squint_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_squint_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_squint_C_CTL.rotateOrder", 0)

			mc.xform("R_squint_C_CTL", a=1, t=[-4.440892098500626e-16, 0.0, -8.881784197001252e-16])
			mc.xform("R_squint_C_CTL", a=1, ro=[2.5444437451708134e-14, -2.2673876147152017e-16, -3.975693351829397e-16])
			mc.xform("R_squint_C_CTL", r=1, s=[1.0000000000000002, 1.0, 1.0])

		if mc.objExists("R_cheekLower_A_D_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_A_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_A_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_A_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheekLower_A_D_OFF_CTL", a=1, ro=[-4.413906298050157e-31, -1.2722218725854064e-14, 3.975693351829394e-15])
			mc.xform("R_cheekLower_A_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_A_C_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_A_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_A_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_A_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheekLower_A_C_OFF_CTL", a=1, ro=[3.9756933518293915e-16, -1.2722218725854064e-14, 3.180554681463516e-15])
			mc.xform("R_cheekLower_A_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_A_B_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_A_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_A_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_A_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheekLower_A_B_OFF_CTL", a=1, ro=[2.385416011097637e-14, -1.2722218725854064e-14, 3.1805546814635132e-15])
			mc.xform("R_cheekLower_A_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_A_A_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_A_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_A_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_A_A_OFF_CTL", a=1, t=[0.0, 0.0, -1.1102230246251565e-16])
			mc.xform("R_cheekLower_A_A_OFF_CTL", a=1, ro=[3.9756933518293915e-16, -1.2722218725854064e-14, 3.180554681463516e-15])
			mc.xform("R_cheekLower_A_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_A_CTL"):
			if not mc.getAttr("R_cheekLower_A_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_cheekLower_A_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_cheekLower_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_cheekLower_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_cheekLower_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_A_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_A_CTL", a=1, t=[8.881784197001252e-16, 0.0, 1.1102230246251565e-16])
			mc.xform("R_cheekLower_A_CTL", a=1, ro=[4.310455369189609e-31, -1.2424041724466865e-14, -3.975693351829397e-15])
			mc.xform("R_cheekLower_A_CTL", r=1, s=[1.0, 0.9999999999999998, 1.0])

		if mc.objExists("R_cheekLower_B_D_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_B_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_B_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_B_D_OFF_CTL", a=1, t=[0.0, -4.440892098500626e-16, 1.1102230246251565e-16])
			mc.xform("R_cheekLower_B_D_OFF_CTL", a=1, ro=[1.7666159552675807e-07, -4.294322593699357e-08, 1.0761576858203275e-08])
			mc.xform("R_cheekLower_B_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_B_C_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_B_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_B_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_B_C_OFF_CTL", a=1, t=[0.0, 4.440892098500626e-16, -1.1102230246251565e-16])
			mc.xform("R_cheekLower_B_C_OFF_CTL", a=1, ro=[1.7666159552675807e-07, -4.294322593699357e-08, 1.0761576858203275e-08])
			mc.xform("R_cheekLower_B_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_B_B_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_B_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_B_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_B_B_OFF_CTL", a=1, t=[0.0, -4.440892098500626e-16, 2.220446049250313e-16])
			mc.xform("R_cheekLower_B_B_OFF_CTL", a=1, ro=[1.7666159552675807e-07, -4.294322593699357e-08, 1.0761576858203275e-08])
			mc.xform("R_cheekLower_B_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_B_A_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_B_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_B_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_B_A_OFF_CTL", a=1, t=[0.0, 4.440892098500626e-16, -1.1102230246251565e-16])
			mc.xform("R_cheekLower_B_A_OFF_CTL", a=1, ro=[1.7666159552675807e-07, -4.294322593699357e-08, 1.0761576858203275e-08])
			mc.xform("R_cheekLower_B_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_B_CTL"):
			if not mc.getAttr("R_cheekLower_B_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_cheekLower_B_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_cheekLower_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_cheekLower_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_cheekLower_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_B_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_B_CTL", a=1, t=[-2.220446049250313e-16, 0.0, -6.661338147750939e-16])
			mc.xform("R_cheekLower_B_CTL", a=1, ro=[3.951825482473033e-31, -1.8983935754985366e-14, -2.3854160110976376e-15])
			mc.xform("R_cheekLower_B_CTL", r=1, s=[0.9999999999999998, 1.0000000000000002, 1.0])

		if mc.objExists("R_cheekLower_C_D_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_C_D_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_C_D_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_C_D_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheekLower_C_D_OFF_CTL", a=1, ro=[2.782985346280577e-15, 1.9310840053969444e-32, -7.951386703658792e-16])
			mc.xform("R_cheekLower_C_D_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_C_C_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_C_C_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_C_C_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_C_C_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheekLower_C_C_OFF_CTL", a=1, ro=[2.782985346280577e-15, 1.9310840053969444e-32, -7.951386703658792e-16])
			mc.xform("R_cheekLower_C_C_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_C_B_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_C_B_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_C_B_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_C_B_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheekLower_C_B_OFF_CTL", a=1, ro=[2.782985346280577e-15, 1.9310840053969444e-32, -7.951386703658792e-16])
			mc.xform("R_cheekLower_C_B_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_C_A_OFF_CTL"):
			if not mc.getAttr("R_cheekLower_C_A_OFF_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_C_A_OFF_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_C_A_OFF_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_cheekLower_C_A_OFF_CTL", a=1, ro=[2.3854160110976376e-15, -6.3611093629270335e-15, 7.951386703658792e-16])
			mc.xform("R_cheekLower_C_A_OFF_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_cheekLower_C_CTL"):
			if not mc.getAttr("R_cheekLower_C_CTL.numOffsetCtrls", l=1):
				mc.setAttr("R_cheekLower_C_CTL.numOffsetCtrls", 0)

			if not mc.getAttr("R_cheekLower_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_cheekLower_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_cheekLower_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_cheekLower_C_CTL.rotateOrder", 0)

			mc.xform("R_cheekLower_C_CTL", a=1, t=[-8.881784197001252e-16, 4.440892098500626e-16, -4.440892098500626e-16])
			mc.xform("R_cheekLower_C_CTL", a=1, ro=[-2.067360542951286e-14, 8.448348372637464e-15, -1.4312496066585827e-14])
			mc.xform("R_cheekLower_C_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0])

		# Apply contro shapes data
		data = {
			"C_tongue_FK_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_FK_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -3.029897], [0.0, 0.002713, -3.029897], [-0.002713, 0.0, -3.029897], [0.0, -0.002713, -3.029897], [0.002713, 0.0, -3.029897], [0.0, 0.0, -3.027184], [-0.002713, 0.0, -3.029897], [0.0, 0.0, -3.03261], [0.0, 0.002713, -3.029897], [0.0, 0.0, -3.027184], [0.0, -0.002713, -3.029897], [0.0, 0.0, -3.03261], [0.002713, 0.0, -3.029897], [0.0, 0.0, -3.027184], [0.0, 0.0, -3.285815]]}, {"shapeName": "C_tongue_FK_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -3.285815], [0.0, 0.255918, -3.288527], [-0.002713, 0.255918, -3.285815], [0.0, 0.255918, -3.283102], [0.002713, 0.255918, -3.285815], [0.0, 0.25863, -3.285815], [-0.002713, 0.255918, -3.285815], [0.0, 0.253205, -3.285815], [0.0, 0.255918, -3.288527], [0.0, 0.25863, -3.285815], [0.0, 0.255918, -3.283102], [0.0, 0.253205, -3.285815], [0.002713, 0.255918, -3.285815], [0.0, 0.25863, -3.285815], [0.0, 0.0, -3.285815]]}, {"shapeName": "C_tongue_FK_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -3.285815], [-0.255918, 0.0, -3.288527], [-0.255918, -0.002713, -3.285815], [-0.255918, 0.0, -3.283102], [-0.255918, 0.002713, -3.285815], [-0.25863, 0.0, -3.285815], [-0.255918, -0.002713, -3.285815], [-0.253205, 0.0, -3.285815], [-0.255918, 0.0, -3.288527], [-0.25863, 0.0, -3.285815], [-0.255918, 0.0, -3.283102], [-0.253205, 0.0, -3.285815], [-0.255918, 0.002713, -3.285815], [-0.25863, 0.0, -3.285815], [0.0, 0.0, -3.285815]]}]},
			"C_mouthAll_B_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "C_mouthAll_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.047017, 0.222561, -1.619637], [0.0, 0.235544, -1.619637], [-0.047017, 0.222561, -1.619637], [-0.066492, 0.191217, -1.619637], [-0.047017, 0.159872, -1.619637], [0.0, 0.146889, -1.619637], [0.047017, 0.159872, -1.619637], [0.066492, 0.191217, -1.619637]]}]},
			"R_cheekLower_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheekLower_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.729311, 2.149375, -1.07847], [-2.739139, 2.157271, -1.06972], [-2.745254, 2.144115, -1.064719], [-2.735426, 2.13622, -1.073468], [-2.729311, 2.149375, -1.07847], [-2.744406, 2.146946, -1.079776], [-2.745254, 2.144115, -1.064719], [-2.730159, 2.146544, -1.063412], [-2.739139, 2.157271, -1.06972], [-2.744406, 2.146946, -1.079776], [-2.735426, 2.13622, -1.073468], [-2.730159, 2.146544, -1.063412], [-2.729311, 2.149375, -1.07847], [-2.744406, 2.146946, -1.079776], [-2.065239, 2.127817, -0.299647]]}, {"shapeName": "R_cheekLower_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-2.232371, 3.123415, -0.129733], [-2.233219, 3.120584, -0.114674], [-2.248315, 3.118155, -0.115981], [-2.247467, 3.120985, -0.13104], [-2.232371, 3.123415, -0.129733], [-2.242199, 3.131309, -0.120983], [-2.248315, 3.118155, -0.115981], [-2.238487, 3.110259, -0.124731], [-2.233219, 3.120584, -0.114674], [-2.242199, 3.131309, -0.120983], [-2.247467, 3.120985, -0.13104], [-2.238487, 3.110259, -0.124731], [-2.232371, 3.123415, -0.129733], [-2.242199, 3.131309, -0.120983], [-2.065239, 2.127817, -0.299647]]}, {"shapeName": "R_cheekLower_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.819159, 1.890233, 0.350875], [-2.810179, 1.879507, 0.357184], [-2.815446, 1.869182, 0.347127], [-2.824426, 1.879908, 0.340819], [-2.819159, 1.890233, 0.350875], [-2.825274, 1.877078, 0.355877], [-2.815446, 1.869182, 0.347127], [-2.809331, 1.882338, 0.342126], [-2.810179, 1.879507, 0.357184], [-2.825274, 1.877078, 0.355877], [-2.824426, 1.879908, 0.340819], [-2.809331, 1.882338, 0.342126], [-2.819159, 1.890233, 0.350875], [-2.825274, 1.877078, 0.355877], [-2.065239, 2.127817, -0.299647]]}]},
			"L_squint_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_squint_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.825458, 2.89531, -0.976489], [2.834078, 2.905368, -0.968741], [2.841807, 2.893781, -0.9623], [2.833188, 2.883723, -0.970048], [2.825458, 2.89531, -0.976489], [2.840754, 2.894747, -0.977578], [2.841807, 2.893781, -0.9623], [2.826511, 2.894344, -0.96121], [2.834078, 2.905368, -0.968741], [2.840754, 2.894747, -0.977578], [2.833188, 2.883723, -0.970048], [2.826511, 2.894344, -0.96121], [2.825458, 2.89531, -0.976489], [2.840754, 2.894747, -0.977578], [2.161769, 2.875554, -0.197292]]}, {"shapeName": "L_squint_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.195566, 3.897269, -0.142752], [2.196619, 3.896304, -0.127473], [2.211915, 3.895741, -0.128563], [2.210862, 3.896706, -0.143841], [2.195566, 3.897269, -0.142752], [2.204185, 3.907326, -0.135004], [2.211915, 3.895741, -0.128563], [2.203296, 3.885683, -0.13631], [2.196619, 3.896304, -0.127473], [2.204185, 3.907326, -0.135004], [2.210862, 3.896706, -0.143841], [2.203296, 3.885683, -0.13631], [2.195566, 3.897269, -0.142752], [2.204185, 3.907326, -0.135004], [2.161769, 2.875554, -0.197292]]}, {"shapeName": "L_squint_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.933408, 2.814266, 0.472661], [2.925842, 2.803243, 0.480192], [2.932519, 2.792622, 0.471354], [2.940085, 2.803645, 0.463823], [2.933408, 2.814266, 0.472661], [2.941137, 2.80268, 0.479101], [2.932519, 2.792622, 0.471354], [2.924789, 2.804208, 0.464913], [2.925842, 2.803243, 0.480192], [2.941137, 2.80268, 0.479101], [2.940085, 2.803645, 0.463823], [2.924789, 2.804208, 0.464913], [2.933408, 2.814266, 0.472661], [2.941137, 2.80268, 0.479101], [2.161769, 2.875554, -0.197292]]}]},
			"L_cheek_C_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_C_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.162516, 2.650554, -0.238523], [2.145802, 2.661247, -0.216442], [2.126509, 2.649539, -0.197155], [2.115938, 2.622289, -0.191962], [2.120281, 2.59546, -0.203904], [2.136995, 2.584768, -0.225985], [2.156289, 2.596476, -0.245271], [2.16686, 2.623725, -0.250465]]}]},
			"R_innerLid_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_innerLid_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-0.909336, 5.967979, 0.139964], [-0.909336, 5.972198, 0.144183], [-0.909336, 5.967979, 0.148402], [-0.909336, 5.96376, 0.144183], [-0.909336, 5.967979, 0.139964], [-0.913556, 5.967979, 0.144183], [-0.909336, 5.967979, 0.148402], [-0.905117, 5.967979, 0.144183], [-0.909336, 5.972198, 0.144183], [-0.913556, 5.967979, 0.144183], [-0.909336, 5.96376, 0.144183], [-0.905117, 5.967979, 0.144183], [-0.909336, 5.967979, 0.139964], [-0.913556, 5.967979, 0.144183], [-0.511282, 5.967979, 0.144183]]}, {"shapeName": "R_innerLid_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.511282, 6.366033, 0.139964], [-0.507063, 6.366033, 0.144183], [-0.511282, 6.366033, 0.148402], [-0.515501, 6.366033, 0.144183], [-0.511282, 6.366033, 0.139964], [-0.511282, 6.370252, 0.144183], [-0.511282, 6.366033, 0.148402], [-0.511282, 6.361814, 0.144183], [-0.507063, 6.366033, 0.144183], [-0.511282, 6.370252, 0.144183], [-0.515501, 6.366033, 0.144183], [-0.511282, 6.361814, 0.144183], [-0.511282, 6.366033, 0.139964], [-0.511282, 6.370252, 0.144183], [-0.511282, 5.967979, 0.144183]]}, {"shapeName": "R_innerLid_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.511282, 5.972198, 0.542237], [-0.507063, 5.967979, 0.542237], [-0.511282, 5.96376, 0.542237], [-0.515501, 5.967979, 0.542237], [-0.511282, 5.972198, 0.542237], [-0.511282, 5.967979, 0.546456], [-0.511282, 5.96376, 0.542237], [-0.511282, 5.967979, 0.538018], [-0.507063, 5.967979, 0.542237], [-0.511282, 5.967979, 0.546456], [-0.515501, 5.967979, 0.542237], [-0.511282, 5.967979, 0.538018], [-0.511282, 5.972198, 0.542237], [-0.511282, 5.967979, 0.546456], [-0.511282, 5.967979, 0.144183]]}]},
			"L_nostril_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_nostril_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.523671, 5.147208, -1.624575], [1.523671, 5.158059, -1.613724], [1.523671, 5.147208, -1.602873], [1.523671, 5.136357, -1.613724], [1.523671, 5.147208, -1.624575], [1.534521, 5.147208, -1.613724], [1.523671, 5.147208, -1.602873], [1.51282, 5.147208, -1.613724], [1.523671, 5.158059, -1.613724], [1.534521, 5.147208, -1.613724], [1.523671, 5.136357, -1.613724], [1.51282, 5.147208, -1.613724], [1.523671, 5.147208, -1.624575], [1.534521, 5.147208, -1.613724], [0.5, 5.147208, -1.613724]]}, {"shapeName": "L_nostril_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.5, 6.170879, -1.624575], [0.489149, 6.170879, -1.613724], [0.5, 6.170879, -1.602873], [0.510851, 6.170879, -1.613724], [0.5, 6.170879, -1.624575], [0.5, 6.181729, -1.613724], [0.5, 6.170879, -1.602873], [0.5, 6.160028, -1.613724], [0.489149, 6.170879, -1.613724], [0.5, 6.181729, -1.613724], [0.510851, 6.170879, -1.613724], [0.5, 6.160028, -1.613724], [0.5, 6.170879, -1.624575], [0.5, 6.181729, -1.613724], [0.5, 5.147208, -1.613724]]}, {"shapeName": "L_nostril_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.5, 5.158059, -0.590053], [0.489149, 5.147208, -0.590053], [0.5, 5.136357, -0.590053], [0.510851, 5.147208, -0.590053], [0.5, 5.158059, -0.590053], [0.5, 5.147208, -0.579203], [0.5, 5.136357, -0.590053], [0.5, 5.147208, -0.600904], [0.489149, 5.147208, -0.590053], [0.5, 5.147208, -0.579203], [0.510851, 5.147208, -0.590053], [0.5, 5.147208, -0.600904], [0.5, 5.158059, -0.590053], [0.5, 5.147208, -0.579203], [0.5, 5.147208, -1.613724]]}]},
			"R_lowerLipSecondary_A_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.466266, -0.97502, -0.385637], [-0.466266, -0.97502, -0.403637], [-0.466266, -0.95702, -0.403637], [-0.466266, -0.95702, -0.385637], [-0.484266, -0.95702, -0.385637], [-0.484266, -0.95702, -0.403637], [-0.484266, -0.97502, -0.403637], [-0.484266, -0.97502, -0.385637], [-0.466266, -0.97502, -0.385637], [-0.466266, -0.95702, -0.385637], [-0.466266, -0.95702, -0.403637], [-0.484266, -0.95702, -0.403637], [-0.484266, -0.95702, -0.385637], [-0.484266, -0.97502, -0.385637], [-0.484266, -0.97502, -0.403637], [-0.466266, -0.97502, -0.403637]]}]},
			"C_lowerLip_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lowerLip_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.013713, -1.02007, -0.394637], [0.0, -1.01439, -0.394637], [-0.013713, -1.02007, -0.394637], [-0.019393, -1.033783, -0.394637], [-0.013713, -1.047497, -0.394637], [0.0, -1.053177, -0.394637], [0.013713, -1.047497, -0.394637], [0.019393, -1.033783, -0.394637]]}]},
			"R_brow_upper_C_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_C_CTLShape", "degree": 1, "form": 0, "points": [[-1.421832, 8.239842, -1.669392], [-1.475078, 8.218129, -1.652263], [-1.498771, 8.234772, -1.704815], [-1.445525, 8.256486, -1.721944], [-1.421832, 8.239842, -1.669392]]}]},
			"L_brow_C_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_C_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.691935, 7.81021, -1.506136], [1.668231, 7.818319, -1.501685], [1.650525, 7.813365, -1.484094], [1.649191, 7.79825, -1.463668], [1.665008, 7.781828, -1.452373], [1.688712, 7.773719, -1.456824], [1.706418, 7.778673, -1.474415], [1.707753, 7.793788, -1.494841]]}]},
			"L_innerLid_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_innerLid_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.507883, 5.970641, 0.144183], [0.507883, 5.964418, 0.144183], [0.514106, 5.964418, 0.144183], [0.514106, 5.970641, 0.144183], [0.507883, 5.970641, 0.144183]]}]},
			"C_tongue_IK_D_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_D_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.068566, -0.068566, -1.282066], [0.096967, 0.0, -1.282066], [0.068566, 0.068566, -1.282066], [0.0, 0.096967, -1.282066], [-0.068566, 0.068566, -1.282066], [-0.096967, 0.0, -1.282066], [-0.068566, -0.068566, -1.282066], [0.0, -0.096967, -1.282066]]}]},
			"R_lowerLipSecondary_A_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.468266, -0.97302, -0.387637], [-0.468266, -0.97302, -0.401637], [-0.468266, -0.95902, -0.401637], [-0.468266, -0.95902, -0.387637], [-0.482266, -0.95902, -0.387637], [-0.482266, -0.95902, -0.401637], [-0.482266, -0.97302, -0.401637], [-0.482266, -0.97302, -0.387637], [-0.468266, -0.97302, -0.387637], [-0.468266, -0.95902, -0.387637], [-0.468266, -0.95902, -0.401637], [-0.482266, -0.95902, -0.401637], [-0.482266, -0.95902, -0.387637], [-0.482266, -0.97302, -0.387637], [-0.482266, -0.97302, -0.401637], [-0.468266, -0.97302, -0.401637]]}]},
			"C_tongue_FK_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_FK_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -2.669005], [0.0, 0.002713, -2.669005], [-0.002713, 0.0, -2.669005], [0.0, -0.002713, -2.669005], [0.002713, 0.0, -2.669005], [0.0, 0.0, -2.666292], [-0.002713, 0.0, -2.669005], [0.0, 0.0, -2.671718], [0.0, 0.002713, -2.669005], [0.0, 0.0, -2.666292], [0.0, -0.002713, -2.669005], [0.0, 0.0, -2.671718], [0.002713, 0.0, -2.669005], [0.0, 0.0, -2.666292], [0.0, 0.0, -2.924923]]}, {"shapeName": "C_tongue_FK_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -2.924923], [0.0, 0.255918, -2.927635], [-0.002713, 0.255918, -2.924923], [0.0, 0.255918, -2.92221], [0.002713, 0.255918, -2.924923], [0.0, 0.25863, -2.924923], [-0.002713, 0.255918, -2.924923], [0.0, 0.253205, -2.924923], [0.0, 0.255918, -2.927635], [0.0, 0.25863, -2.924923], [0.0, 0.255918, -2.92221], [0.0, 0.253205, -2.924923], [0.002713, 0.255918, -2.924923], [0.0, 0.25863, -2.924923], [0.0, 0.0, -2.924923]]}, {"shapeName": "C_tongue_FK_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -2.924923], [-0.255918, 0.0, -2.927635], [-0.255918, -0.002713, -2.924923], [-0.255918, 0.0, -2.92221], [-0.255918, 0.002713, -2.924923], [-0.25863, 0.0, -2.924923], [-0.255918, -0.002713, -2.924923], [-0.253205, 0.0, -2.924923], [-0.255918, 0.0, -2.927635], [-0.25863, 0.0, -2.924923], [-0.255918, 0.0, -2.92221], [-0.253205, 0.0, -2.924923], [-0.255918, 0.002713, -2.924923], [-0.25863, 0.0, -2.924923], [0.0, 0.0, -2.924923]]}]},
			"R_upperLid_C_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.675047, 6.359177, 0.144183], [-1.675047, 6.353732, 0.144183], [-1.680492, 6.353732, 0.144183], [-1.680492, 6.359177, 0.144183], [-1.675047, 6.359177, 0.144183]]}]},
			"L_lipCorner_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lipCorner_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.011754, 0.202971, -0.394637], [2.0, 0.207839, -0.394637], [1.988246, 0.202971, -0.394637], [1.983377, 0.191217, -0.394637], [1.988246, 0.179462, -0.394637], [2.0, 0.174594, -0.394637], [2.011754, 0.179462, -0.394637], [2.016623, 0.191217, -0.394637]]}]},
			"R_lipZipper_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_lipZipper_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.083115, 0.197113, 2.055363], [-0.089115, 0.185217, 2.055363], [-0.077115, 0.185217, 2.055363], [-0.083115, 0.197113, 2.055363], [-0.083115, 0.197113, 2.055363]]}]},
			"L_lipCorner_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lipCorner_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.015672, 0.206889, -0.394637], [2.0, 0.21338, -0.394637], [1.984328, 0.206889, -0.394637], [1.977836, 0.191217, -0.394637], [1.984328, 0.175544, -0.394637], [2.0, 0.169053, -0.394637], [2.015672, 0.175544, -0.394637], [2.022164, 0.191217, -0.394637]]}]},
			"R_lowerLipSecondary_A_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.469266, -0.97202, -0.388637], [-0.469266, -0.97202, -0.400637], [-0.469266, -0.96002, -0.400637], [-0.469266, -0.96002, -0.388637], [-0.481266, -0.96002, -0.388637], [-0.481266, -0.96002, -0.400637], [-0.481266, -0.97202, -0.400637], [-0.481266, -0.97202, -0.388637], [-0.469266, -0.97202, -0.388637], [-0.469266, -0.96002, -0.388637], [-0.469266, -0.96002, -0.400637], [-0.481266, -0.96002, -0.400637], [-0.481266, -0.96002, -0.388637], [-0.481266, -0.97202, -0.388637], [-0.481266, -0.97202, -0.400637], [-0.469266, -0.97202, -0.400637]]}]},
			"R_upperLipSecondary_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upperLipSecondary_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.498937, 1.348453, -0.405488], [-1.498937, 1.359304, -0.394637], [-1.498937, 1.348453, -0.383786], [-1.498937, 1.337602, -0.394637], [-1.498937, 1.348453, -0.405488], [-1.509787, 1.348453, -0.394637], [-1.498937, 1.348453, -0.383786], [-1.488086, 1.348453, -0.394637], [-1.498937, 1.359304, -0.394637], [-1.509787, 1.348453, -0.394637], [-1.498937, 1.337602, -0.394637], [-1.488086, 1.348453, -0.394637], [-1.498937, 1.348453, -0.405488], [-1.509787, 1.348453, -0.394637], [-0.475266, 1.348453, -0.394637]]}, {"shapeName": "R_upperLipSecondary_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.475266, 2.372124, -0.405488], [-0.464415, 2.372124, -0.394637], [-0.475266, 2.372124, -0.383786], [-0.486117, 2.372124, -0.394637], [-0.475266, 2.372124, -0.405488], [-0.475266, 2.382974, -0.394637], [-0.475266, 2.372124, -0.383786], [-0.475266, 2.361273, -0.394637], [-0.464415, 2.372124, -0.394637], [-0.475266, 2.382974, -0.394637], [-0.486117, 2.372124, -0.394637], [-0.475266, 2.361273, -0.394637], [-0.475266, 2.372124, -0.405488], [-0.475266, 2.382974, -0.394637], [-0.475266, 1.348453, -0.394637]]}, {"shapeName": "R_upperLipSecondary_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.475266, 1.359304, 0.629034], [-0.464415, 1.348453, 0.629034], [-0.475266, 1.337602, 0.629034], [-0.486117, 1.348453, 0.629034], [-0.475266, 1.359304, 0.629034], [-0.475266, 1.348453, 0.639884], [-0.475266, 1.337602, 0.629034], [-0.475266, 1.348453, 0.618183], [-0.464415, 1.348453, 0.629034], [-0.475266, 1.348453, 0.639884], [-0.486117, 1.348453, 0.629034], [-0.475266, 1.348453, 0.618183], [-0.475266, 1.359304, 0.629034], [-0.475266, 1.348453, 0.639884], [-0.475266, 1.348453, -0.394637]]}]},
			"C_brow_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_brow_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.027426, 7.842407, -1.061736], [-0.0, 7.849781, -1.070378], [-0.027426, 7.842407, -1.061736], [-0.038787, 7.824604, -1.040873], [-0.027426, 7.806801, -1.02001], [-0.0, 7.799427, -1.011368], [0.027426, 7.806801, -1.02001], [0.038787, 7.824604, -1.040873]]}]},
			"R_cheek_A_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_A_CTLShape", "degree": 3, "form": 2, "points": [[-1.946635, 2.617757, 0.263231], [-1.919159, 2.634455, 0.290885], [-1.887637, 2.619168, 0.314784], [-1.870534, 2.58085, 0.320928], [-1.877869, 2.541948, 0.305718], [-1.905345, 2.52525, 0.278064], [-1.936867, 2.540538, 0.254165], [-1.95397, 2.578855, 0.248021]]}]},
			"R_lowerLipSecondary_C_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.283093, -0.471611, -0.386637], [-1.283093, -0.471611, -0.402637], [-1.283093, -0.455611, -0.402637], [-1.283093, -0.455611, -0.386637], [-1.299093, -0.455611, -0.386637], [-1.299093, -0.455611, -0.402637], [-1.299093, -0.471611, -0.402637], [-1.299093, -0.471611, -0.386637], [-1.283093, -0.471611, -0.386637], [-1.283093, -0.455611, -0.386637], [-1.283093, -0.455611, -0.402637], [-1.299093, -0.455611, -0.402637], [-1.299093, -0.455611, -0.386637], [-1.299093, -0.471611, -0.386637], [-1.299093, -0.471611, -0.402637], [-1.283093, -0.471611, -0.402637]]}]},
			"R_lowerLid_A_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.896808, 5.581716, 0.144183], [-0.896808, 5.575493, 0.144183], [-0.903031, 5.575493, 0.144183], [-0.903031, 5.581716, 0.144183], [-0.896808, 5.581716, 0.144183]]}]},
			"L_brow_upper_B_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_B_CTLShape", "degree": 1, "form": 0, "points": [[0.979961, 8.266268, -1.518588], [1.030674, 8.245871, -1.493846], [1.061277, 8.262833, -1.542588], [1.010564, 8.28323, -1.56733], [0.979961, 8.266268, -1.518588]]}]},
			"L_squint_B_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.986945, 2.844445, -0.013055], [1.973248, 2.866957, -0.026752], [2.002905, 2.865386, -0.026794], [1.986945, 2.844445, -0.013055], [1.973206, 2.865386, 0.002905], [1.973248, 2.866957, -0.026752], [1.989166, 2.886327, -0.010834], [1.973206, 2.865386, 0.002905], [2.002863, 2.863816, 0.002863], [1.986945, 2.844445, -0.013055], [2.002905, 2.865386, -0.026794], [1.989166, 2.886327, -0.010834], [2.002863, 2.863816, 0.002863], [2.002905, 2.865386, -0.026794]]}]},
			"R_lowerLipSecondary_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lowerLipSecondary_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.929322, -0.753362, -0.405488], [-1.929322, -0.742511, -0.394637], [-1.929322, -0.753362, -0.383786], [-1.929322, -0.764213, -0.394637], [-1.929322, -0.753362, -0.405488], [-1.940172, -0.753362, -0.394637], [-1.929322, -0.753362, -0.383786], [-1.918471, -0.753362, -0.394637], [-1.929322, -0.742511, -0.394637], [-1.940172, -0.753362, -0.394637], [-1.929322, -0.764213, -0.394637], [-1.918471, -0.753362, -0.394637], [-1.929322, -0.753362, -0.405488], [-1.940172, -0.753362, -0.394637], [-0.905651, -0.753362, -0.394637]]}, {"shapeName": "R_lowerLipSecondary_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.905651, 0.270309, -0.405488], [-0.8948, 0.270309, -0.394637], [-0.905651, 0.270309, -0.383786], [-0.916502, 0.270309, -0.394637], [-0.905651, 0.270309, -0.405488], [-0.905651, 0.281159, -0.394637], [-0.905651, 0.270309, -0.383786], [-0.905651, 0.259458, -0.394637], [-0.8948, 0.270309, -0.394637], [-0.905651, 0.281159, -0.394637], [-0.916502, 0.270309, -0.394637], [-0.905651, 0.259458, -0.394637], [-0.905651, 0.270309, -0.405488], [-0.905651, 0.281159, -0.394637], [-0.905651, -0.753362, -0.394637]]}, {"shapeName": "R_lowerLipSecondary_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.905651, -0.742511, 0.629034], [-0.8948, -0.753362, 0.629034], [-0.905651, -0.764213, 0.629034], [-0.916502, -0.753362, 0.629034], [-0.905651, -0.742511, 0.629034], [-0.905651, -0.753362, 0.639884], [-0.905651, -0.764213, 0.629034], [-0.905651, -0.753362, 0.618183], [-0.8948, -0.753362, 0.629034], [-0.905651, -0.753362, 0.639884], [-0.916502, -0.753362, 0.629034], [-0.905651, -0.753362, 0.618183], [-0.905651, -0.742511, 0.629034], [-0.905651, -0.753362, 0.639884], [-0.905651, -0.753362, -0.394637]]}]},
			"C_tongue_IK_C_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_C_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.088156, -0.088156, -1.907066], [0.124672, 0.0, -1.907066], [0.088156, 0.088156, -1.907066], [0.0, 0.124672, -1.907066], [-0.088156, 0.088156, -1.907066], [-0.124672, 0.0, -1.907066], [-0.088156, -0.088156, -1.907066], [0.0, -0.124672, -1.907066]]}]},
			"R_cheekLower_A_C_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_A_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.730859, 2.152217, 0.046898], [-1.712173, 2.163729, 0.066888], [-1.689563, 2.153203, 0.082989], [-1.676273, 2.126804, 0.085769], [-1.680087, 2.099997, 0.0736], [-1.698773, 2.088484, 0.053611], [-1.721383, 2.09901, 0.03751], [-1.734673, 2.125409, 0.034729]]}]},
			"R_cheek_B_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_B_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.985318, 2.639949, -0.047927], [-1.969854, 2.649548, -0.030146], [-1.952073, 2.639949, -0.014682], [-1.942391, 2.616776, -0.010593], [-1.94648, 2.593602, -0.020274], [-1.961944, 2.584003, -0.038056], [-1.979726, 2.593602, -0.05352], [-1.989407, 2.616776, -0.057609]]}]},
			"R_squint_C_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.161031, 2.857601, -0.198376], [-2.148209, 2.876822, -0.209061], [-2.173583, 2.875888, -0.210869], [-2.161031, 2.857601, -0.198376], [-2.149956, 2.87522, -0.183716], [-2.148209, 2.876822, -0.209061], [-2.162507, 2.893506, -0.196209], [-2.149956, 2.87522, -0.183716], [-2.17533, 2.874286, -0.185524], [-2.161031, 2.857601, -0.198376], [-2.173583, 2.875888, -0.210869], [-2.162507, 2.893506, -0.196209], [-2.17533, 2.874286, -0.185524], [-2.173583, 2.875888, -0.210869]]}]},
			"L_lowerLid_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lowerLid_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.298051, 5.578604, 0.139963], [1.298051, 5.582824, 0.144183], [1.298051, 5.578604, 0.148403], [1.298051, 5.574384, 0.144183], [1.298051, 5.578604, 0.139963], [1.302271, 5.578604, 0.144183], [1.298051, 5.578604, 0.148403], [1.293831, 5.578604, 0.144183], [1.298051, 5.582824, 0.144183], [1.302271, 5.578604, 0.144183], [1.298051, 5.574384, 0.144183], [1.293831, 5.578604, 0.144183], [1.298051, 5.578604, 0.139963], [1.302271, 5.578604, 0.144183], [0.89992, 5.578604, 0.144183]]}, {"shapeName": "L_lowerLid_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.89992, 5.976735, 0.139963], [0.8957, 5.976735, 0.144183], [0.89992, 5.976735, 0.148403], [0.90414, 5.976735, 0.144183], [0.89992, 5.976735, 0.139963], [0.89992, 5.980955, 0.144183], [0.89992, 5.976735, 0.148403], [0.89992, 5.972515, 0.144183], [0.8957, 5.976735, 0.144183], [0.89992, 5.980955, 0.144183], [0.90414, 5.976735, 0.144183], [0.89992, 5.972515, 0.144183], [0.89992, 5.976735, 0.139963], [0.89992, 5.980955, 0.144183], [0.89992, 5.578604, 0.144183]]}, {"shapeName": "L_lowerLid_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.89992, 5.582824, 0.542314], [0.8957, 5.578604, 0.542314], [0.89992, 5.574384, 0.542314], [0.90414, 5.578604, 0.542314], [0.89992, 5.582824, 0.542314], [0.89992, 5.578604, 0.546534], [0.89992, 5.574384, 0.542314], [0.89992, 5.578604, 0.538094], [0.8957, 5.578604, 0.542314], [0.89992, 5.578604, 0.546534], [0.90414, 5.578604, 0.542314], [0.89992, 5.578604, 0.538094], [0.89992, 5.582824, 0.542314], [0.89992, 5.578604, 0.546534], [0.89992, 5.578604, 0.144183]]}]},
			"R_upperLipSecondary_C_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_C_CTLShape", "degree": 1, "form": 0, "points": [[-1.281093, 0.836044, -0.384637], [-1.281093, 0.836044, -0.404637], [-1.281093, 0.856044, -0.404637], [-1.281093, 0.856044, -0.384637], [-1.301093, 0.856044, -0.384637], [-1.301093, 0.856044, -0.404637], [-1.301093, 0.836044, -0.404637], [-1.301093, 0.836044, -0.384637], [-1.281093, 0.836044, -0.384637], [-1.281093, 0.856044, -0.384637], [-1.281093, 0.856044, -0.404637], [-1.301093, 0.856044, -0.404637], [-1.301093, 0.856044, -0.384637], [-1.301093, 0.836044, -0.384637], [-1.301093, 0.836044, -0.404637], [-1.281093, 0.836044, -0.404637]]}]},
			"R_brow_upper_A_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_A_CTLShape", "degree": 1, "form": 0, "points": [[-0.477867, 8.276633, -1.40689], [-0.524874, 8.25713, -1.375109], [-0.56185, 8.274916, -1.418886], [-0.514843, 8.294418, -1.450667], [-0.477867, 8.276633, -1.40689]]}]},
			"L_lowerLid_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lowerLid_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.686976, 5.461927, 0.139963], [1.686976, 5.466147, 0.144183], [1.686976, 5.461927, 0.148403], [1.686976, 5.457707, 0.144183], [1.686976, 5.461927, 0.139963], [1.691196, 5.461927, 0.144183], [1.686976, 5.461927, 0.148403], [1.682756, 5.461927, 0.144183], [1.686976, 5.466147, 0.144183], [1.691196, 5.461927, 0.144183], [1.686976, 5.457707, 0.144183], [1.682756, 5.461927, 0.144183], [1.686976, 5.461927, 0.139963], [1.691196, 5.461927, 0.144183], [1.288845, 5.461927, 0.144183]]}, {"shapeName": "L_lowerLid_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.288845, 5.860058, 0.139963], [1.284625, 5.860058, 0.144183], [1.288845, 5.860058, 0.148403], [1.293065, 5.860058, 0.144183], [1.288845, 5.860058, 0.139963], [1.288845, 5.864278, 0.144183], [1.288845, 5.860058, 0.148403], [1.288845, 5.855838, 0.144183], [1.284625, 5.860058, 0.144183], [1.288845, 5.864278, 0.144183], [1.293065, 5.860058, 0.144183], [1.288845, 5.855838, 0.144183], [1.288845, 5.860058, 0.139963], [1.288845, 5.864278, 0.144183], [1.288845, 5.461927, 0.144183]]}, {"shapeName": "L_lowerLid_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.288845, 5.466147, 0.542314], [1.284625, 5.461927, 0.542314], [1.288845, 5.457707, 0.542314], [1.293065, 5.461927, 0.542314], [1.288845, 5.466147, 0.542314], [1.288845, 5.461927, 0.546534], [1.288845, 5.457707, 0.542314], [1.288845, 5.461927, 0.538094], [1.284625, 5.461927, 0.542314], [1.288845, 5.461927, 0.546534], [1.293065, 5.461927, 0.542314], [1.288845, 5.461927, 0.538094], [1.288845, 5.466147, 0.542314], [1.288845, 5.461927, 0.546534], [1.288845, 5.461927, 0.144183]]}]},
			"C_brow_upper_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_brow_upper_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 8.079748, -1.444501], [1.023671, 8.094318, -1.44932], [1.023671, 8.099137, -1.434751], [1.023671, 8.084568, -1.429931], [1.023671, 8.079748, -1.444501], [1.034521, 8.089443, -1.439626], [1.023671, 8.099137, -1.434751], [1.01282, 8.089443, -1.439626], [1.023671, 8.094318, -1.44932], [1.034521, 8.089443, -1.439626], [1.023671, 8.084568, -1.429931], [1.01282, 8.089443, -1.439626], [1.023671, 8.079748, -1.444501], [1.034521, 8.089443, -1.439626], [-0.0, 8.089443, -1.439626]]}, {"shapeName": "C_brow_upper_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.0, 8.53964, -2.359051], [-0.010851, 8.549335, -2.354176], [-0.0, 8.559029, -2.349301], [0.010851, 8.549335, -2.354176], [-0.0, 8.53964, -2.359051], [-0.0, 8.554209, -2.363869], [-0.0, 8.559029, -2.349301], [-0.0, 8.54446, -2.344481], [-0.010851, 8.549335, -2.354176], [-0.0, 8.554209, -2.363869], [0.010851, 8.549335, -2.354176], [-0.0, 8.54446, -2.344481], [-0.0, 8.53964, -2.359051], [-0.0, 8.554209, -2.363869], [-0.0, 8.089443, -1.439626]]}, {"shapeName": "C_brow_upper_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.0, 9.008868, -0.989428], [-0.010851, 9.003993, -0.979734], [-0.0, 8.999118, -0.970039], [0.010851, 9.003993, -0.979734], [-0.0, 9.008868, -0.989428], [-0.0, 9.013686, -0.974859], [-0.0, 8.999118, -0.970039], [-0.0, 8.994298, -0.984609], [-0.010851, 9.003993, -0.979734], [-0.0, 9.013686, -0.974859], [0.010851, 9.003993, -0.979734], [-0.0, 8.994298, -0.984609], [-0.0, 9.008868, -0.989428], [-0.0, 9.013686, -0.974859], [-0.0, 8.089443, -1.439626]]}]},
			"L_brow_B_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_B_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.223203, 7.841247, -1.300442], [1.186716, 7.85242, -1.299664], [1.156528, 7.844503, -1.277691], [1.150324, 7.822134, -1.247394], [1.171737, 7.798416, -1.226521], [1.208225, 7.787243, -1.227299], [1.238413, 7.79516, -1.249272], [1.244617, 7.817529, -1.279568]]}]},
			"C_tongue_FK_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_FK_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -2.311862], [0.0, 0.002713, -2.311862], [-0.002713, 0.0, -2.311862], [0.0, -0.002713, -2.311862], [0.002713, 0.0, -2.311862], [0.0, 0.0, -2.30915], [-0.002713, 0.0, -2.311862], [0.0, 0.0, -2.314575], [0.0, 0.002713, -2.311862], [0.0, 0.0, -2.30915], [0.0, -0.002713, -2.311862], [0.0, 0.0, -2.314575], [0.002713, 0.0, -2.311862], [0.0, 0.0, -2.30915], [0.0, 0.0, -2.56778]]}, {"shapeName": "C_tongue_FK_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -2.56778], [0.0, 0.255918, -2.570493], [-0.002713, 0.255918, -2.56778], [0.0, 0.255918, -2.565067], [0.002713, 0.255918, -2.56778], [0.0, 0.25863, -2.56778], [-0.002713, 0.255918, -2.56778], [0.0, 0.253205, -2.56778], [0.0, 0.255918, -2.570493], [0.0, 0.25863, -2.56778], [0.0, 0.255918, -2.565067], [0.0, 0.253205, -2.56778], [0.002713, 0.255918, -2.56778], [0.0, 0.25863, -2.56778], [0.0, 0.0, -2.56778]]}, {"shapeName": "C_tongue_FK_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -2.56778], [-0.255918, 0.0, -2.570493], [-0.255918, -0.002713, -2.56778], [-0.255918, 0.0, -2.565067], [-0.255918, 0.002713, -2.56778], [-0.25863, 0.0, -2.56778], [-0.255918, -0.002713, -2.56778], [-0.253205, 0.0, -2.56778], [-0.255918, 0.0, -2.570493], [-0.25863, 0.0, -2.56778], [-0.255918, 0.0, -2.565067], [-0.253205, 0.0, -2.56778], [-0.255918, 0.002713, -2.56778], [-0.25863, 0.0, -2.56778], [0.0, 0.0, -2.56778]]}]},
			"L_innerLid_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_innerLid_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.508272, 5.970252, 0.144183], [0.508272, 5.964807, 0.144183], [0.513717, 5.964807, 0.144183], [0.513717, 5.970252, 0.144183], [0.508272, 5.970252, 0.144183]]}]},
			"L_lowerLid_A_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_A_CTLShape", "degree": 1, "form": 0, "points": [[0.89442, 5.578604, 0.151961], [0.89992, 5.573104, 0.151961], [0.90542, 5.578604, 0.151961], [0.89992, 5.584104, 0.151961], [0.89442, 5.578604, 0.151961]]}]},
			"R_upperLipSecondary_B_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_B_CTLShape", "degree": 1, "form": 0, "points": [[-0.895651, 1.125795, -0.384637], [-0.895651, 1.125795, -0.404637], [-0.895651, 1.145795, -0.404637], [-0.895651, 1.145795, -0.384637], [-0.915651, 1.145795, -0.384637], [-0.915651, 1.145795, -0.404637], [-0.915651, 1.125795, -0.404637], [-0.915651, 1.125795, -0.384637], [-0.895651, 1.125795, -0.384637], [-0.895651, 1.145795, -0.384637], [-0.895651, 1.145795, -0.404637], [-0.915651, 1.145795, -0.404637], [-0.915651, 1.145795, -0.384637], [-0.915651, 1.125795, -0.384637], [-0.915651, 1.125795, -0.404637], [-0.895651, 1.125795, -0.404637]]}]},
			"R_eye_FK_D_OFF_CTL": {"color": 8, "shapes": [{"shapeName": "R_eye_FK_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.0, 6.0, 0.5], [-2.075, 6.0, 0.425], [-2.069291, 5.971299, 0.425], [-2.0, 6.0, 0.5], [-1.925, 6.0, 0.425], [-1.930709, 6.028701, 0.425], [-2.0, 6.0, 0.5], [-2.053033, 5.946967, 0.425], [-2.028701, 5.930709, 0.425], [-2.0, 6.0, 0.5], [-1.946967, 6.053033, 0.425], [-1.971299, 6.069291, 0.425], [-2.0, 6.0, 0.5], [-2.0, 5.925, 0.425], [-1.971299, 5.930709, 0.425], [-2.0, 6.0, 0.5], [-2.0, 6.075, 0.425], [-2.028701, 6.069291, 0.425], [-2.0, 6.0, 0.5], [-1.946967, 5.946967, 0.425], [-1.930709, 5.971299, 0.425], [-2.0, 6.0, 0.5], [-2.053033, 6.053033, 0.425], [-2.069291, 6.028701, 0.425], [-2.075, 6.0, 0.425], [-2.069291, 5.971299, 0.425], [-2.053033, 5.946967, 0.425], [-2.028701, 5.930709, 0.425], [-2.0, 5.925, 0.425], [-1.971299, 5.930709, 0.425], [-1.946967, 5.946967, 0.425], [-1.930709, 5.971299, 0.425], [-1.925, 6.0, 0.425], [-1.930709, 6.028701, 0.425], [-1.946967, 6.053033, 0.425], [-1.971299, 6.069291, 0.425], [-2.0, 6.075, 0.425], [-2.028701, 6.069291, 0.425], [-2.053033, 6.053033, 0.425], [-2.069291, 6.028701, 0.425], [-2.0, 6.0, 0.5]]}]},
			"R_upperLipSecondary_C_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.284093, 0.839044, -0.387637], [-1.284093, 0.839044, -0.401637], [-1.284093, 0.853044, -0.401637], [-1.284093, 0.853044, -0.387637], [-1.298093, 0.853044, -0.387637], [-1.298093, 0.853044, -0.401637], [-1.298093, 0.839044, -0.401637], [-1.298093, 0.839044, -0.387637], [-1.284093, 0.839044, -0.387637], [-1.284093, 0.853044, -0.387637], [-1.284093, 0.853044, -0.401637], [-1.298093, 0.853044, -0.401637], [-1.298093, 0.853044, -0.387637], [-1.298093, 0.839044, -0.387637], [-1.298093, 0.839044, -0.401637], [-1.284093, 0.839044, -0.401637]]}]},
			"R_lipCornerSecondary_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lipCornerSecondary_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.994, 0.185217, -0.388637], [-1.994, 0.185217, -0.400637], [-1.994, 0.197217, -0.400637], [-1.994, 0.197217, -0.388637], [-2.006, 0.197217, -0.388637], [-2.006, 0.197217, -0.400637], [-2.006, 0.185217, -0.400637], [-2.006, 0.185217, -0.388637], [-1.994, 0.185217, -0.388637], [-1.994, 0.197217, -0.388637], [-1.994, 0.197217, -0.400637], [-2.006, 0.197217, -0.400637], [-2.006, 0.197217, -0.388637], [-2.006, 0.185217, -0.388637], [-2.006, 0.185217, -0.400637], [-1.994, 0.185217, -0.400637]]}]},
			"R_brow_upper_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_upper_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.967971, 8.033992, -1.907056], [-1.967131, 8.048502, -1.911979], [-1.971434, 8.053457, -1.898107], [-1.972274, 8.038947, -1.893184], [-1.967971, 8.033992, -1.907056], [-1.9801, 8.043285, -1.90565], [-1.971434, 8.053457, -1.898107], [-1.959304, 8.044164, -1.899513], [-1.967131, 8.048502, -1.911979], [-1.9801, 8.043285, -1.90565], [-1.972274, 8.038947, -1.893184], [-1.959304, 8.044164, -1.899513], [-1.967971, 8.033992, -1.907056], [-1.9801, 8.043285, -1.90565], [-0.988703, 8.085161, -1.613054]]}, {"shapeName": "R_brow_upper_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.744366, 8.526127, -2.504047], [-0.735699, 8.536299, -2.496504], [-0.747829, 8.545593, -2.495098], [-0.756496, 8.535421, -2.502642], [-0.744366, 8.526127, -2.504047], [-0.743526, 8.540637, -2.508969], [-0.747829, 8.545593, -2.495098], [-0.748669, 8.531082, -2.490175], [-0.735699, 8.536299, -2.496504], [-0.743526, 8.540637, -2.508969], [-0.756496, 8.535421, -2.502642], [-0.748669, 8.531082, -2.490175], [-0.744366, 8.526127, -2.504047], [-0.743526, 8.540637, -2.508969], [-0.988703, 8.085161, -1.613054]]}, {"shapeName": "R_brow_upper_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.149488, 9.008119, -1.20036], [-1.141661, 9.00378, -1.187894], [-1.154632, 8.998564, -1.181565], [-1.162459, 9.002902, -1.194032], [-1.149488, 9.008119, -1.20036], [-1.153791, 9.013073, -1.186489], [-1.154632, 8.998564, -1.181565], [-1.150328, 8.993608, -1.195437], [-1.141661, 9.00378, -1.187894], [-1.153791, 9.013073, -1.186489], [-1.162459, 9.002902, -1.194032], [-1.150328, 8.993608, -1.195437], [-1.149488, 9.008119, -1.20036], [-1.153791, 9.013073, -1.186489], [-0.988703, 8.085161, -1.613054]]}]},
			"R_brow_upper_A_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.477239, 8.107198, -1.517375], [-0.482913, 8.086105, -1.474633], [-0.530421, 8.085133, -1.481419], [-0.524747, 8.106227, -1.524161], [-0.477239, 8.107198, -1.517375]]}]},
			"L_brow_C_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_C_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.694179, 7.812575, -1.510617], [1.666524, 7.822036, -1.505423], [1.645868, 7.816256, -1.484901], [1.64431, 7.798621, -1.461071], [1.662764, 7.779463, -1.447892], [1.690419, 7.770002, -1.453086], [1.711075, 7.775782, -1.473608], [1.712633, 7.793417, -1.497439]]}]},
			"L_eye_FK_C_OFF_CTL": {"color": 8, "shapes": [{"shapeName": "L_eye_FK_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.0, 6.0, 0.5], [2.0875, 6.0, 0.4125], [2.08084, 5.966515, 0.4125], [2.0, 6.0, 0.5], [1.9125, 6.0, 0.4125], [1.919161, 6.033485, 0.4125], [2.0, 6.0, 0.5], [2.061872, 5.938128, 0.4125], [2.033485, 5.919161, 0.4125], [2.0, 6.0, 0.5], [1.938128, 6.061872, 0.4125], [1.966515, 6.080839, 0.4125], [2.0, 6.0, 0.5], [2.0, 5.9125, 0.4125], [1.966515, 5.919161, 0.4125], [2.0, 6.0, 0.5], [2.0, 6.0875, 0.4125], [2.033485, 6.080839, 0.4125], [2.0, 6.0, 0.5], [1.938128, 5.938128, 0.4125], [1.919161, 5.966515, 0.4125], [2.0, 6.0, 0.5], [2.061872, 6.061872, 0.4125], [2.08084, 6.033485, 0.4125], [2.0875, 6.0, 0.4125], [2.08084, 5.966515, 0.4125], [2.061872, 5.938128, 0.4125], [2.033485, 5.919161, 0.4125], [2.0, 5.9125, 0.4125], [1.966515, 5.919161, 0.4125], [1.938128, 5.938128, 0.4125], [1.919161, 5.966515, 0.4125], [1.9125, 6.0, 0.4125], [1.919161, 6.033485, 0.4125], [1.938128, 6.061872, 0.4125], [1.966515, 6.080839, 0.4125], [2.0, 6.0875, 0.4125], [2.033485, 6.080839, 0.4125], [2.061872, 6.061872, 0.4125], [2.08084, 6.033485, 0.4125], [2.0, 6.0, 0.5]]}]},
			"R_upperLip_A_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_upperLip_A_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.114383, 1.007517, -0.394637], [-1.102629, 1.012386, -0.394637], [-1.090874, 1.007517, -0.394637], [-1.086006, 0.995763, -0.394637], [-1.090874, 0.984009, -0.394637], [-1.102629, 0.97914, -0.394637], [-1.114383, 0.984009, -0.394637], [-1.119251, 0.995763, -0.394637]]}]},
			"C_tongue_IK_D_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_D_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.058771, -0.058771, -1.282066], [0.083115, 0.0, -1.282066], [0.058771, 0.058771, -1.282066], [0.0, 0.083115, -1.282066], [-0.058771, 0.058771, -1.282066], [-0.083115, 0.0, -1.282066], [-0.058771, -0.058771, -1.282066], [0.0, -0.083115, -1.282066]]}]},
			"C_tongue_FK_G_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_tongue_FK_G_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.125, -1.139208], [0.0, 0.125951, -1.134425], [0.0, 0.128661, -1.13037], [0.0, 0.132716, -1.12766], [0.0, 0.1375, -1.126708], [0.0, 0.142284, -1.12766], [0.0, 0.146339, -1.13037], [0.0, 0.149049, -1.134425], [0.0, 0.15, -1.139208], [0.0, 0.149049, -1.143992], [0.0, 0.146339, -1.148047], [0.0, 0.142284, -1.150757], [0.0, 0.1375, -1.151708], [0.0, 0.132716, -1.150757], [0.0, 0.128661, -1.148047], [0.0, 0.125951, -1.143992], [0.0, 0.125, -1.139208], [0.0, 0.0, -1.139208]]}]},
			"C_upperLip_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_upperLip_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.011754, 1.427971, -0.394637], [0.0, 1.432839, -0.394637], [-0.011754, 1.427971, -0.394637], [-0.016623, 1.416217, -0.394637], [-0.011754, 1.404462, -0.394637], [0.0, 1.399594, -0.394637], [0.011754, 1.404462, -0.394637], [0.016623, 1.416217, -0.394637]]}]},
			"L_eye_FK_B_OFF_CTL": {"color": 8, "shapes": [{"shapeName": "L_eye_FK_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.0, 6.0, 0.5], [2.1, 6.0, 0.4], [2.092388, 5.961732, 0.4], [2.0, 6.0, 0.5], [1.9, 6.0, 0.4], [1.907612, 6.038268, 0.4], [2.0, 6.0, 0.5], [2.070711, 5.929289, 0.4], [2.038268, 5.907612, 0.4], [2.0, 6.0, 0.5], [1.929289, 6.070711, 0.4], [1.961732, 6.092388, 0.4], [2.0, 6.0, 0.5], [2.0, 5.9, 0.4], [1.961732, 5.907612, 0.4], [2.0, 6.0, 0.5], [2.0, 6.1, 0.4], [2.038268, 6.092388, 0.4], [2.0, 6.0, 0.5], [1.929289, 5.929289, 0.4], [1.907612, 5.961732, 0.4], [2.0, 6.0, 0.5], [2.070711, 6.070711, 0.4], [2.092388, 6.038268, 0.4], [2.1, 6.0, 0.4], [2.092388, 5.961732, 0.4], [2.070711, 5.929289, 0.4], [2.038268, 5.907612, 0.4], [2.0, 5.9, 0.4], [1.961732, 5.907612, 0.4], [1.929289, 5.929289, 0.4], [1.907612, 5.961732, 0.4], [1.9, 6.0, 0.4], [1.907612, 6.038268, 0.4], [1.929289, 6.070711, 0.4], [1.961732, 6.092388, 0.4], [2.0, 6.1, 0.4], [2.038268, 6.092388, 0.4], [2.070711, 6.070711, 0.4], [2.092388, 6.038268, 0.4], [2.0, 6.0, 0.5]]}]},
			"C_upperLip_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_upperLip_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.015672, 1.431889, -0.394637], [0.0, 1.43838, -0.394637], [-0.015672, 1.431889, -0.394637], [-0.022164, 1.416217, -0.394637], [-0.015672, 1.400544, -0.394637], [0.0, 1.394053, -0.394637], [0.015672, 1.400544, -0.394637], [0.022164, 1.416217, -0.394637]]}]},
			"L_squint_B_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.986628, 2.838462, -0.013372], [1.969017, 2.867406, -0.030983], [2.007148, 2.865386, -0.031036], [1.986628, 2.838462, -0.013372], [1.968964, 2.865386, 0.007148], [1.969017, 2.867406, -0.030983], [1.989484, 2.892311, -0.010516], [1.968964, 2.865386, 0.007148], [2.007094, 2.863367, 0.007094], [1.986628, 2.838462, -0.013372], [2.007148, 2.865386, -0.031036], [1.989484, 2.892311, -0.010516], [2.007094, 2.863367, 0.007094], [2.007148, 2.865386, -0.031036]]}]},
			"L_nostril_D_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "L_nostril_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.617542, 5.26475, -1.613724], [0.5, 5.313437, -1.613724], [0.382458, 5.26475, -1.613724], [0.333771, 5.147208, -1.613724], [0.382458, 5.029666, -1.613724], [0.5, 4.980979, -1.613724], [0.617542, 5.029666, -1.613724], [0.666229, 5.147208, -1.613724]]}]},
			"C_lowerLipSecondary_CTL": {"color": 20, "shapes": [{"shapeName": "C_lowerLipSecondary_CTLShape", "degree": 1, "form": 0, "points": [[-0.01, -1.043783, -0.384637], [-0.01, -1.043783, -0.404637], [-0.01, -1.023783, -0.404637], [-0.01, -1.023783, -0.384637], [0.01, -1.023783, -0.384637], [0.01, -1.023783, -0.404637], [0.01, -1.043783, -0.404637], [0.01, -1.043783, -0.384637], [-0.01, -1.043783, -0.384637], [-0.01, -1.023783, -0.384637], [-0.01, -1.023783, -0.404637], [0.01, -1.023783, -0.404637], [0.01, -1.023783, -0.384637], [0.01, -1.043783, -0.384637], [0.01, -1.043783, -0.404637], [-0.01, -1.043783, -0.404637]]}]},
			"C_tongue_IK_B_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_B_CTLShape", "degree": 3, "form": 2, "points": [[0.097951, -0.097951, -2.532066], [0.138524, 0.0, -2.532066], [0.097951, 0.097951, -2.532066], [0.0, 0.138524, -2.532066], [-0.097951, 0.097951, -2.532066], [-0.138524, 0.0, -2.532066], [-0.097951, -0.097951, -2.532066], [0.0, -0.138524, -2.532066]]}]},
			"C_tongue_IK_A_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_A_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.058771, -0.058771, -3.157066], [0.083115, 0.0, -3.157066], [0.058771, 0.058771, -3.157066], [0.0, 0.083115, -3.157066], [-0.058771, 0.058771, -3.157066], [-0.083115, 0.0, -3.157066], [-0.058771, -0.058771, -3.157066], [0.0, -0.083115, -3.157066]]}]},
			"R_upperLip_A_CTL": {"color": 17, "shapes": [{"shapeName": "R_upperLip_A_CTLShape", "degree": 3, "form": 2, "points": [[-1.122219, 1.035353, -0.384637], [-1.102629, 1.043468, -0.384637], [-1.083038, 1.035353, -0.384637], [-1.074924, 1.015763, -0.384637], [-1.083038, 0.996173, -0.384637], [-1.102629, 0.988058, -0.384637], [-1.122219, 0.996173, -0.384637], [-1.130333, 1.015763, -0.384637]]}]},
			"R_cheekLower_B_D_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_B_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.909645, 2.147579, -0.123601], [-1.894696, 2.157024, -0.105304], [-1.876399, 2.147579, -0.090355], [-1.865473, 2.124776, -0.08751], [-1.868318, 2.101972, -0.098436], [-1.883267, 2.092527, -0.116733], [-1.901564, 2.101972, -0.131682], [-1.91249, 2.124776, -0.134527]]}]},
			"R_upperLipSecondary_A_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.467266, 1.340453, -0.386637], [-0.467266, 1.340453, -0.402637], [-0.467266, 1.356453, -0.402637], [-0.467266, 1.356453, -0.386637], [-0.483266, 1.356453, -0.386637], [-0.483266, 1.356453, -0.402637], [-0.483266, 1.340453, -0.402637], [-0.483266, 1.340453, -0.386637], [-0.467266, 1.340453, -0.386637], [-0.467266, 1.356453, -0.386637], [-0.467266, 1.356453, -0.402637], [-0.483266, 1.356453, -0.402637], [-0.483266, 1.356453, -0.386637], [-0.483266, 1.340453, -0.386637], [-0.483266, 1.340453, -0.402637], [-0.467266, 1.340453, -0.402637]]}]},
			"R_brow_A_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_A_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-0.647797, 7.852738, -1.139254], [-0.61142, 7.862989, -1.144586], [-0.57822, 7.85437, -1.127845], [-0.567644, 7.83193, -1.098839], [-0.585888, 7.808812, -1.074558], [-0.622265, 7.798561, -1.069227], [-0.655465, 7.80718, -1.085967], [-0.666041, 7.82962, -1.114974]]}]},
			"L_upperLipSecondary_A_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.467266, 1.340453, -0.386637], [0.467266, 1.340453, -0.402637], [0.467266, 1.356453, -0.402637], [0.467266, 1.356453, -0.386637], [0.483266, 1.356453, -0.386637], [0.483266, 1.356453, -0.402637], [0.483266, 1.340453, -0.402637], [0.483266, 1.340453, -0.386637], [0.467266, 1.340453, -0.386637], [0.467266, 1.356453, -0.386637], [0.467266, 1.356453, -0.402637], [0.483266, 1.356453, -0.402637], [0.483266, 1.356453, -0.386637], [0.483266, 1.340453, -0.386637], [0.483266, 1.340453, -0.402637], [0.467266, 1.340453, -0.402637]]}]},
			"R_upperLid_A_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.896808, 6.359566, 0.144183], [-0.896808, 6.353343, 0.144183], [-0.903031, 6.353343, 0.144183], [-0.903031, 6.359566, 0.144183], [-0.896808, 6.359566, 0.144183]]}]},
			"C_lookAt_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lookAt_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.298841, 6.018736, 3.055261], [-0.298841, 5.981264, 3.055261], [-0.298841, 5.981264, 3.01779], [-0.298841, 6.018736, 3.01779], [-0.298841, 6.018736, 3.055261], [0.298841, 6.018736, 3.055261], [0.298841, 5.981264, 3.055261], [0.298841, 5.981264, 3.01779], [0.298841, 6.018736, 3.01779], [0.298841, 6.018736, 3.055261], [0.298841, 5.981264, 3.055261], [-0.298841, 5.981264, 3.055261], [-0.298841, 5.981264, 3.01779], [0.298841, 5.981264, 3.01779], [0.298841, 6.018736, 3.01779], [-0.298841, 6.018736, 3.01779], [-0.298841, 6.018736, 3.055261], [-0.0186, 6.0186, 3.055126], [-0.018736, 5.701159, 3.055261], [-0.018736, 5.701159, 3.01779], [0.018736, 5.701159, 3.01779], [0.018736, 5.701159, 3.055261], [-0.018736, 5.701159, 3.055261], [-0.018736, 6.298841, 3.055261], [0.018736, 6.298841, 3.055261], [0.018736, 6.298841, 3.01779], [-0.018736, 6.298841, 3.01779], [-0.018736, 6.298841, 3.055261], [-0.018736, 6.298841, 3.01779], [-0.018736, 5.701159, 3.01779], [0.018736, 5.701159, 3.01779], [0.018736, 6.298841, 3.01779], [0.018736, 6.298841, 3.055261], [0.018736, 5.701159, 3.055261], [0.0186, 5.9814, 3.055126], [0.018736, 5.981264, 3.335367], [-0.018736, 5.981264, 3.335367], [-0.018736, 6.018736, 3.335367], [0.018736, 6.018736, 3.335367], [0.018736, 5.981264, 3.335367], [0.018736, 5.981264, 2.737684], [0.018736, 6.018736, 2.737684], [-0.018736, 6.018736, 2.737684], [-0.018736, 5.981264, 2.737684], [0.018736, 5.981264, 2.737684], [-0.018736, 5.981264, 2.737684], [-0.018736, 5.981264, 3.335367], [-0.018736, 6.018736, 3.335367], [-0.018736, 6.018736, 2.737684], [0.018736, 6.018736, 2.737684], [0.018736, 6.018736, 3.335367]]}]},
			"C_lowerLip_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lowerLip_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.017631, -1.016152, -0.394637], [0.0, -1.008849, -0.394637], [-0.017631, -1.016152, -0.394637], [-0.024934, -1.033783, -0.394637], [-0.017631, -1.051415, -0.394637], [0.0, -1.058718, -0.394637], [0.017631, -1.051415, -0.394637], [0.024934, -1.033783, -0.394637]]}]},
			"C_tongue_FK_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_tongue_FK_D_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.125, -2.210637], [0.0, 0.125951, -2.205853], [0.0, 0.128661, -2.201798], [0.0, 0.132716, -2.199088], [0.0, 0.1375, -2.198137], [0.0, 0.142284, -2.199088], [0.0, 0.146339, -2.201798], [0.0, 0.149049, -2.205853], [0.0, 0.15, -2.210637], [0.0, 0.149049, -2.21542], [0.0, 0.146339, -2.219476], [0.0, 0.142284, -2.222185], [0.0, 0.1375, -2.223137], [0.0, 0.132716, -2.222185], [0.0, 0.128661, -2.219476], [0.0, 0.125951, -2.21542], [0.0, 0.125, -2.210637], [0.0, 0.0, -2.210637]]}]},
			"R_brow_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.576158, 7.71932, -1.965358], [-2.576719, 7.734613, -1.966493], [-2.583965, 7.73535, -1.952986], [-2.583404, 7.720057, -1.951851], [-2.576158, 7.71932, -1.965358], [-2.589617, 7.726607, -1.964259], [-2.583965, 7.73535, -1.952986], [-2.570504, 7.728063, -1.954085], [-2.576719, 7.734613, -1.966493], [-2.589617, 7.726607, -1.964259], [-2.583404, 7.720057, -1.951851], [-2.570504, 7.728063, -1.954085], [-2.576158, 7.71932, -1.965358], [-2.589617, 7.726607, -1.964259], [-1.678472, 7.796019, -1.479255]]}, {"shapeName": "R_brow_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.359241, 8.47464, -2.176094], [-1.353587, 8.483383, -2.164821], [-1.367048, 8.49067, -2.163722], [-1.372701, 8.481927, -2.174995], [-1.359241, 8.47464, -2.176094], [-1.359802, 8.489932, -2.177228], [-1.367048, 8.49067, -2.163722], [-1.366487, 8.475376, -2.162587], [-1.353587, 8.483383, -2.164821], [-1.359802, 8.489932, -2.177228], [-1.372701, 8.481927, -2.174995], [-1.366487, 8.475376, -2.162587], [-1.359241, 8.47464, -2.176094], [-1.359802, 8.489932, -2.177228], [-1.678472, 7.796019, -1.479255]]}, {"shapeName": "R_brow_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.043378, 8.559416, -0.902984], [-2.037163, 8.552866, -0.890576], [-2.050063, 8.54486, -0.888342], [-2.056277, 8.55141, -0.90075], [-2.043378, 8.559416, -0.902984], [-2.050623, 8.560152, -0.889477], [-2.050063, 8.54486, -0.888342], [-2.042817, 8.544123, -0.901849], [-2.037163, 8.552866, -0.890576], [-2.050623, 8.560152, -0.889477], [-2.056277, 8.55141, -0.90075], [-2.042817, 8.544123, -0.901849], [-2.043378, 8.559416, -0.902984], [-2.050623, 8.560152, -0.889477], [-1.678472, 7.796019, -1.479255]]}]},
			"C_tongue_IK_C_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_C_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.058771, -0.058771, -1.907066], [0.083115, 0.0, -1.907066], [0.058771, 0.058771, -1.907066], [0.0, 0.083115, -1.907066], [-0.058771, 0.058771, -1.907066], [-0.083115, 0.0, -1.907066], [-0.058771, -0.058771, -1.907066], [0.0, -0.083115, -1.907066]]}]},
			"R_cheek_B_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_B_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.995028, 2.651536, -0.054841], [-1.971831, 2.665934, -0.028169], [-1.945159, 2.651536, -0.004972], [-1.930637, 2.616776, 0.001162], [-1.93677, 2.582015, -0.013361], [-1.959967, 2.567617, -0.040033], [-1.986639, 2.582015, -0.06323], [-2.001162, 2.616776, -0.069363]]}]},
			"C_noseBridge_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_noseBridge_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.176313, 5.923521, -1.313724], [0.0, 5.996552, -1.313724], [-0.176313, 5.923521, -1.313724], [-0.249344, 5.747208, -1.313724], [-0.176313, 5.570895, -1.313724], [0.0, 5.497864, -1.313724], [0.176313, 5.570895, -1.313724], [0.249344, 5.747208, -1.313724]]}]},
			"R_brow_upper_A_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.480563, 8.105819, -1.515128], [-0.485528, 8.087362, -1.477728], [-0.527097, 8.086512, -1.483666], [-0.522132, 8.104969, -1.521065], [-0.480563, 8.105819, -1.515128]]}]},
			"R_upperLipSecondary_D_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_D_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.646693, 0.52094, -0.388637], [-1.646693, 0.52094, -0.400637], [-1.646693, 0.53294, -0.400637], [-1.646693, 0.53294, -0.388637], [-1.658693, 0.53294, -0.388637], [-1.658693, 0.53294, -0.400637], [-1.658693, 0.52094, -0.400637], [-1.658693, 0.52094, -0.388637], [-1.646693, 0.52094, -0.388637], [-1.646693, 0.53294, -0.388637], [-1.646693, 0.53294, -0.400637], [-1.658693, 0.53294, -0.400637], [-1.658693, 0.53294, -0.388637], [-1.658693, 0.52094, -0.388637], [-1.658693, 0.52094, -0.400637], [-1.646693, 0.52094, -0.400637]]}]},
			"R_lipZipper_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_lipZipper_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.083115, 0.199079, 2.055363], [-0.091115, 0.183217, 2.055363], [-0.075115, 0.183217, 2.055363], [-0.083115, 0.199079, 2.055363], [-0.083115, 0.199079, 2.055363]]}]},
			"C_tongue_IK_A_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_A_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.078361, -0.078361, -3.157066], [0.110819, 0.0, -3.157066], [0.078361, 0.078361, -3.157066], [0.0, 0.110819, -3.157066], [-0.078361, 0.078361, -3.157066], [-0.110819, 0.0, -3.157066], [-0.078361, -0.078361, -3.157066], [0.0, -0.110819, -3.157066]]}]},
			"L_brow_C_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_C_CTLShape", "degree": 3, "form": 2, "points": [[1.772857, 7.967398, -1.410038], [1.73335, 7.980912, -1.402619], [1.703841, 7.972655, -1.373301], [1.701617, 7.947464, -1.339258], [1.727979, 7.920094, -1.320432], [1.767486, 7.906579, -1.327851], [1.796995, 7.914836, -1.357169], [1.79922, 7.940028, -1.391212]]}]},
			"R_brow_C_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_C_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.698667, 7.817306, -1.519577], [-1.66311, 7.829469, -1.5129], [-1.636552, 7.822038, -1.486514], [-1.63455, 7.799365, -1.455875], [-1.658276, 7.774732, -1.438932], [-1.693833, 7.762569, -1.445609], [-1.720391, 7.77, -1.471995], [-1.722393, 7.792673, -1.502634]]}]},
			"C_tongue_IK_E_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_IK_E_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -0.401148], [0.0, 0.002713, -0.401148], [-0.002713, 0.0, -0.401148], [0.0, -0.002713, -0.401148], [0.002713, 0.0, -0.401148], [0.0, 0.0, -0.398435], [-0.002713, 0.0, -0.401148], [0.0, 0.0, -0.403861], [0.0, 0.002713, -0.401148], [0.0, 0.0, -0.398435], [0.0, -0.002713, -0.401148], [0.0, 0.0, -0.403861], [0.002713, 0.0, -0.401148], [0.0, 0.0, -0.398435], [0.0, 0.0, -0.657066]]}, {"shapeName": "C_tongue_IK_E_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -0.657066], [0.0, 0.255918, -0.659778], [-0.002713, 0.255918, -0.657066], [0.0, 0.255918, -0.654353], [0.002713, 0.255918, -0.657066], [0.0, 0.25863, -0.657066], [-0.002713, 0.255918, -0.657066], [0.0, 0.253205, -0.657066], [0.0, 0.255918, -0.659778], [0.0, 0.25863, -0.657066], [0.0, 0.255918, -0.654353], [0.0, 0.253205, -0.657066], [0.002713, 0.255918, -0.657066], [0.0, 0.25863, -0.657066], [0.0, 0.0, -0.657066]]}, {"shapeName": "C_tongue_IK_E_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -0.657066], [-0.255918, 0.0, -0.659778], [-0.255918, -0.002713, -0.657066], [-0.255918, 0.0, -0.654353], [-0.255918, 0.002713, -0.657066], [-0.25863, 0.0, -0.657066], [-0.255918, -0.002713, -0.657066], [-0.253205, 0.0, -0.657066], [-0.255918, 0.0, -0.659778], [-0.25863, 0.0, -0.657066], [-0.255918, 0.0, -0.654353], [-0.253205, 0.0, -0.657066], [-0.255918, 0.002713, -0.657066], [-0.25863, 0.0, -0.657066], [0.0, 0.0, -0.657066]]}]},
			"L_upperLipSecondary_D_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_D_CTLShape", "degree": 1, "form": 0, "points": [[1.642693, 0.51694, -0.384637], [1.642693, 0.51694, -0.404637], [1.642693, 0.53694, -0.404637], [1.642693, 0.53694, -0.384637], [1.662693, 0.53694, -0.384637], [1.662693, 0.53694, -0.404637], [1.662693, 0.51694, -0.404637], [1.662693, 0.51694, -0.384637], [1.642693, 0.51694, -0.384637], [1.642693, 0.53694, -0.384637], [1.642693, 0.53694, -0.404637], [1.662693, 0.53694, -0.404637], [1.662693, 0.53694, -0.384637], [1.662693, 0.51694, -0.384637], [1.662693, 0.51694, -0.404637], [1.642693, 0.51694, -0.404637]]}]},
			"L_brow_B_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_B_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.214626, 7.834108, -1.288122], [1.1903, 7.841557, -1.287603], [1.170175, 7.836279, -1.272955], [1.166039, 7.821366, -1.252757], [1.180315, 7.805554, -1.238841], [1.20464, 7.798105, -1.239359], [1.224765, 7.803383, -1.254008], [1.228901, 7.818296, -1.274206]]}]},
			"R_cheek_A_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_A_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.810513, 2.644, 0.118645], [-1.788532, 2.657358, 0.140769], [-1.763315, 2.645128, 0.159888], [-1.749632, 2.614474, 0.164803], [-1.7555, 2.583352, 0.152635], [-1.777481, 2.569994, 0.130512], [-1.802698, 2.582224, 0.111393], [-1.816381, 2.612878, 0.106477]]}]},
			"L_cheekLower_A_C_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_A_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.730859, 2.152217, 0.046898], [1.712173, 2.163729, 0.066888], [1.689563, 2.153203, 0.082989], [1.676273, 2.126804, 0.085769], [1.680087, 2.099997, 0.0736], [1.698773, 2.088484, 0.053611], [1.721383, 2.09901, 0.03751], [1.734673, 2.125409, 0.034729]]}]},
			"L_innerLid_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_innerLid_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.909126, 5.967529, 0.139963], [0.909126, 5.971749, 0.144183], [0.909126, 5.967529, 0.148403], [0.909126, 5.963309, 0.144183], [0.909126, 5.967529, 0.139963], [0.913346, 5.967529, 0.144183], [0.909126, 5.967529, 0.148403], [0.904906, 5.967529, 0.144183], [0.909126, 5.971749, 0.144183], [0.913346, 5.967529, 0.144183], [0.909126, 5.963309, 0.144183], [0.904906, 5.967529, 0.144183], [0.909126, 5.967529, 0.139963], [0.913346, 5.967529, 0.144183], [0.510995, 5.967529, 0.144183]]}, {"shapeName": "L_innerLid_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.510995, 6.36566, 0.139963], [0.506775, 6.36566, 0.144183], [0.510995, 6.36566, 0.148403], [0.515215, 6.36566, 0.144183], [0.510995, 6.36566, 0.139963], [0.510995, 6.36988, 0.144183], [0.510995, 6.36566, 0.148403], [0.510995, 6.36144, 0.144183], [0.506775, 6.36566, 0.144183], [0.510995, 6.36988, 0.144183], [0.515215, 6.36566, 0.144183], [0.510995, 6.36144, 0.144183], [0.510995, 6.36566, 0.139963], [0.510995, 6.36988, 0.144183], [0.510995, 5.967529, 0.144183]]}, {"shapeName": "L_innerLid_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.510995, 5.971749, 0.542314], [0.506775, 5.967529, 0.542314], [0.510995, 5.963309, 0.542314], [0.515215, 5.967529, 0.542314], [0.510995, 5.971749, 0.542314], [0.510995, 5.967529, 0.546534], [0.510995, 5.963309, 0.542314], [0.510995, 5.967529, 0.538094], [0.506775, 5.967529, 0.542314], [0.510995, 5.967529, 0.546534], [0.515215, 5.967529, 0.542314], [0.510995, 5.967529, 0.538094], [0.510995, 5.971749, 0.542314], [0.510995, 5.967529, 0.546534], [0.510995, 5.967529, 0.144183]]}]},
			"R_squint_A_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_A_CTLShape", "degree": 1, "form": 0, "points": [[-1.93587, 2.81125, 0.305203], [-1.918191, 2.84352, 0.284082], [-1.960424, 2.840611, 0.286898], [-1.93587, 2.81125, 0.305203], [-1.915245, 2.841693, 0.326366], [-1.918191, 2.84352, 0.284082], [-1.939799, 2.871053, 0.308061], [-1.915245, 2.841693, 0.326366], [-1.957478, 2.838784, 0.329183], [-1.93587, 2.81125, 0.305203], [-1.960424, 2.840611, 0.286898], [-1.939799, 2.871053, 0.308061], [-1.957478, 2.838784, 0.329183], [-1.960424, 2.840611, 0.286898]]}]},
			"L_lowerLid_C_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.674658, 5.581716, 0.144183], [1.674658, 5.575493, 0.144183], [1.680881, 5.575493, 0.144183], [1.680881, 5.581716, 0.144183], [1.674658, 5.581716, 0.144183]]}]},
			"R_upperLidPrimary_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLidPrimary_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.293112, 6.477398, 0.144183], [-1.288845, 6.479166, 0.144183], [-1.284578, 6.477398, 0.144183], [-1.282811, 6.473132, 0.144183], [-1.284578, 6.468865, 0.144183], [-1.288845, 6.467098, 0.144183], [-1.293112, 6.468865, 0.144183], [-1.294879, 6.473132, 0.144183]]}]},
			"L_upperLipSecondary_D_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_D_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.645693, 0.51994, -0.387637], [1.645693, 0.51994, -0.401637], [1.645693, 0.53394, -0.401637], [1.645693, 0.53394, -0.387637], [1.659693, 0.53394, -0.387637], [1.659693, 0.53394, -0.401637], [1.659693, 0.51994, -0.401637], [1.659693, 0.51994, -0.387637], [1.645693, 0.51994, -0.387637], [1.645693, 0.53394, -0.387637], [1.645693, 0.53394, -0.401637], [1.659693, 0.53394, -0.401637], [1.659693, 0.53394, -0.387637], [1.659693, 0.51994, -0.387637], [1.659693, 0.51994, -0.401637], [1.645693, 0.51994, -0.401637]]}]},
			"C_noseBridge_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_noseBridge_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.137132, 5.88434, -1.313724], [0.0, 5.941142, -1.313724], [-0.137132, 5.88434, -1.313724], [-0.193934, 5.747208, -1.313724], [-0.137132, 5.610076, -1.313724], [0.0, 5.553274, -1.313724], [0.137132, 5.610076, -1.313724], [0.193934, 5.747208, -1.313724]]}]},
			"R_nostril_C_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "R_nostril_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-0.637132, 5.28434, -1.613724], [-0.5, 5.341142, -1.613724], [-0.362868, 5.28434, -1.613724], [-0.306066, 5.147208, -1.613724], [-0.362868, 5.010076, -1.613724], [-0.5, 4.953274, -1.613724], [-0.637132, 5.010076, -1.613724], [-0.693934, 5.147208, -1.613724]]}]},
			"L_lowerLid_A_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.896419, 5.582105, 0.144183], [0.896419, 5.575104, 0.144183], [0.90342, 5.575104, 0.144183], [0.90342, 5.582105, 0.144183], [0.896419, 5.582105, 0.144183]]}]},
			"R_lowerLip_A_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lowerLip_A_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.12026, -0.595699, -0.394637], [-1.102629, -0.588396, -0.394637], [-1.084997, -0.595699, -0.394637], [-1.077694, -0.61333, -0.394637], [-1.084997, -0.630961, -0.394637], [-1.102629, -0.638264, -0.394637], [-1.12026, -0.630961, -0.394637], [-1.127563, -0.61333, -0.394637]]}]},
			"R_lowerLid_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lowerLid_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.075886, 5.579129, 0.139964], [-2.075886, 5.583348, 0.144183], [-2.075886, 5.579129, 0.148402], [-2.075886, 5.57491, 0.144183], [-2.075886, 5.579129, 0.139964], [-2.080106, 5.579129, 0.144183], [-2.075886, 5.579129, 0.148402], [-2.071667, 5.579129, 0.144183], [-2.075886, 5.583348, 0.144183], [-2.080106, 5.579129, 0.144183], [-2.075886, 5.57491, 0.144183], [-2.071667, 5.579129, 0.144183], [-2.075886, 5.579129, 0.139964], [-2.080106, 5.579129, 0.144183], [-1.677832, 5.579129, 0.144183]]}, {"shapeName": "R_lowerLid_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.677832, 5.977183, 0.139964], [-1.673613, 5.977183, 0.144183], [-1.677832, 5.977183, 0.148402], [-1.682051, 5.977183, 0.144183], [-1.677832, 5.977183, 0.139964], [-1.677832, 5.981402, 0.144183], [-1.677832, 5.977183, 0.148402], [-1.677832, 5.972964, 0.144183], [-1.673613, 5.977183, 0.144183], [-1.677832, 5.981402, 0.144183], [-1.682051, 5.977183, 0.144183], [-1.677832, 5.972964, 0.144183], [-1.677832, 5.977183, 0.139964], [-1.677832, 5.981402, 0.144183], [-1.677832, 5.579129, 0.144183]]}, {"shapeName": "R_lowerLid_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.677832, 5.583348, 0.542237], [-1.673613, 5.579129, 0.542237], [-1.677832, 5.57491, 0.542237], [-1.682051, 5.579129, 0.542237], [-1.677832, 5.583348, 0.542237], [-1.677832, 5.579129, 0.546456], [-1.677832, 5.57491, 0.542237], [-1.677832, 5.579129, 0.538018], [-1.673613, 5.579129, 0.542237], [-1.677832, 5.579129, 0.546456], [-1.682051, 5.579129, 0.542237], [-1.677832, 5.579129, 0.538018], [-1.677832, 5.583348, 0.542237], [-1.677832, 5.579129, 0.546456], [-1.677832, 5.579129, 0.144183]]}]},
			"R_cheekLower_A_B_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_A_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.734485, 2.155947, 0.044991], [-1.71313, 2.169104, 0.067836], [-1.68729, 2.157074, 0.086237], [-1.672101, 2.126904, 0.089415], [-1.676461, 2.096267, 0.075508], [-1.697816, 2.083109, 0.052662], [-1.723656, 2.09514, 0.034261], [-1.738845, 2.12531, 0.031083]]}]},
			"L_upperLipSecondary_B_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.897651, 1.127795, -0.386637], [0.897651, 1.127795, -0.402637], [0.897651, 1.143795, -0.402637], [0.897651, 1.143795, -0.386637], [0.913651, 1.143795, -0.386637], [0.913651, 1.143795, -0.402637], [0.913651, 1.127795, -0.402637], [0.913651, 1.127795, -0.386637], [0.897651, 1.127795, -0.386637], [0.897651, 1.143795, -0.386637], [0.897651, 1.143795, -0.402637], [0.913651, 1.143795, -0.402637], [0.913651, 1.143795, -0.386637], [0.913651, 1.127795, -0.386637], [0.913651, 1.127795, -0.402637], [0.897651, 1.127795, -0.402637]]}]},
			"L_upperLipSecondary_D_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_D_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.644693, 0.51894, -0.386637], [1.644693, 0.51894, -0.402637], [1.644693, 0.53494, -0.402637], [1.644693, 0.53494, -0.386637], [1.660693, 0.53494, -0.386637], [1.660693, 0.53494, -0.402637], [1.660693, 0.51894, -0.402637], [1.660693, 0.51894, -0.386637], [1.644693, 0.51894, -0.386637], [1.644693, 0.53494, -0.386637], [1.644693, 0.53494, -0.402637], [1.660693, 0.53494, -0.402637], [1.660693, 0.53494, -0.386637], [1.660693, 0.51894, -0.386637], [1.660693, 0.51894, -0.402637], [1.644693, 0.51894, -0.402637]]}]},
			"L_lowerLipSecondary_A_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_A_CTLShape", "degree": 1, "form": 0, "points": [[0.465266, -0.97602, -0.384637], [0.465266, -0.97602, -0.404637], [0.465266, -0.95602, -0.404637], [0.465266, -0.95602, -0.384637], [0.485266, -0.95602, -0.384637], [0.485266, -0.95602, -0.404637], [0.485266, -0.97602, -0.404637], [0.485266, -0.97602, -0.384637], [0.465266, -0.97602, -0.384637], [0.465266, -0.95602, -0.384637], [0.465266, -0.95602, -0.404637], [0.485266, -0.95602, -0.404637], [0.485266, -0.95602, -0.384637], [0.485266, -0.97602, -0.384637], [0.485266, -0.97602, -0.404637], [0.465266, -0.97602, -0.404637]]}]},
			"C_lookAt_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_lookAt_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 6.0, 3.025675], [1.023671, 6.010851, 3.036526], [1.023671, 6.0, 3.047377], [1.023671, 5.989149, 3.036526], [1.023671, 6.0, 3.025675], [1.034521, 6.0, 3.036526], [1.023671, 6.0, 3.047377], [1.01282, 6.0, 3.036526], [1.023671, 6.010851, 3.036526], [1.034521, 6.0, 3.036526], [1.023671, 5.989149, 3.036526], [1.01282, 6.0, 3.036526], [1.023671, 6.0, 3.025675], [1.034521, 6.0, 3.036526], [0.0, 6.0, 3.036526]]}, {"shapeName": "C_lookAt_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 7.023671, 3.025675], [-0.010851, 7.023671, 3.036526], [0.0, 7.023671, 3.047377], [0.010851, 7.023671, 3.036526], [0.0, 7.023671, 3.025675], [0.0, 7.034521, 3.036526], [0.0, 7.023671, 3.047377], [0.0, 7.01282, 3.036526], [-0.010851, 7.023671, 3.036526], [0.0, 7.034521, 3.036526], [0.010851, 7.023671, 3.036526], [0.0, 7.01282, 3.036526], [0.0, 7.023671, 3.025675], [0.0, 7.034521, 3.036526], [0.0, 6.0, 3.036526]]}, {"shapeName": "C_lookAt_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 6.010851, 4.060197], [-0.010851, 6.0, 4.060197], [0.0, 5.989149, 4.060197], [0.010851, 6.0, 4.060197], [0.0, 6.010851, 4.060197], [0.0, 6.0, 4.071047], [0.0, 5.989149, 4.060197], [0.0, 6.0, 4.049346], [-0.010851, 6.0, 4.060197], [0.0, 6.0, 4.071047], [0.010851, 6.0, 4.060197], [0.0, 6.0, 4.049346], [0.0, 6.010851, 4.060197], [0.0, 6.0, 4.071047], [0.0, 6.0, 3.036526]]}]},
			"C_upperLipSecondary_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_upperLipSecondary_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.008, 1.408217, -0.386637], [-0.008, 1.408217, -0.402637], [-0.008, 1.424217, -0.402637], [-0.008, 1.424217, -0.386637], [0.008, 1.424217, -0.386637], [0.008, 1.424217, -0.402637], [0.008, 1.408217, -0.402637], [0.008, 1.408217, -0.386637], [-0.008, 1.408217, -0.386637], [-0.008, 1.424217, -0.386637], [-0.008, 1.424217, -0.402637], [0.008, 1.424217, -0.402637], [0.008, 1.424217, -0.386637], [0.008, 1.408217, -0.386637], [0.008, 1.408217, -0.402637], [-0.008, 1.408217, -0.402637]]}]},
			"C_tongue_IK_D_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_D_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.078361, -0.078361, -1.282066], [0.110819, 0.0, -1.282066], [0.078361, 0.078361, -1.282066], [0.0, 0.110819, -1.282066], [-0.078361, 0.078361, -1.282066], [-0.110819, 0.0, -1.282066], [-0.078361, -0.078361, -1.282066], [0.0, -0.110819, -1.282066]]}]},
			"R_brow_B_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_B_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.223203, 7.841247, -1.300442], [-1.186716, 7.85242, -1.299664], [-1.156528, 7.844503, -1.277691], [-1.150324, 7.822134, -1.247394], [-1.171737, 7.798416, -1.226521], [-1.208225, 7.787243, -1.227299], [-1.238413, 7.79516, -1.249272], [-1.244617, 7.817529, -1.279568]]}]},
			"L_nostril_A_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "L_nostril_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.676313, 5.323521, -1.613724], [0.5, 5.396552, -1.613724], [0.323687, 5.323521, -1.613724], [0.250656, 5.147208, -1.613724], [0.323687, 4.970895, -1.613724], [0.5, 4.897864, -1.613724], [0.676313, 4.970895, -1.613724], [0.749344, 5.147208, -1.613724]]}]},
			"C_noseBase_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_noseBase_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 5.147208, -1.124575], [1.023671, 5.158059, -1.113724], [1.023671, 5.147208, -1.102873], [1.023671, 5.136357, -1.113724], [1.023671, 5.147208, -1.124575], [1.034521, 5.147208, -1.113724], [1.023671, 5.147208, -1.102873], [1.01282, 5.147208, -1.113724], [1.023671, 5.158059, -1.113724], [1.034521, 5.147208, -1.113724], [1.023671, 5.136357, -1.113724], [1.01282, 5.147208, -1.113724], [1.023671, 5.147208, -1.124575], [1.034521, 5.147208, -1.113724], [0.0, 5.147208, -1.113724]]}, {"shapeName": "C_noseBase_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 6.170879, -1.124575], [-0.010851, 6.170879, -1.113724], [0.0, 6.170879, -1.102873], [0.010851, 6.170879, -1.113724], [0.0, 6.170879, -1.124575], [0.0, 6.181729, -1.113724], [0.0, 6.170879, -1.102873], [0.0, 6.160028, -1.113724], [-0.010851, 6.170879, -1.113724], [0.0, 6.181729, -1.113724], [0.010851, 6.170879, -1.113724], [0.0, 6.160028, -1.113724], [0.0, 6.170879, -1.124575], [0.0, 6.181729, -1.113724], [0.0, 5.147208, -1.113724]]}, {"shapeName": "C_noseBase_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 5.158059, -0.090053], [-0.010851, 5.147208, -0.090053], [0.0, 5.136357, -0.090053], [0.010851, 5.147208, -0.090053], [0.0, 5.158059, -0.090053], [0.0, 5.147208, -0.079203], [0.0, 5.136357, -0.090053], [0.0, 5.147208, -0.100904], [-0.010851, 5.147208, -0.090053], [0.0, 5.147208, -0.079203], [0.010851, 5.147208, -0.090053], [0.0, 5.147208, -0.100904], [0.0, 5.158059, -0.090053], [0.0, 5.147208, -0.079203], [0.0, 5.147208, -1.113724]]}]},
			"R_lowerLipSecondary_B_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.899651, -0.759362, -0.388637], [-0.899651, -0.759362, -0.400637], [-0.899651, -0.747362, -0.400637], [-0.899651, -0.747362, -0.388637], [-0.911651, -0.747362, -0.388637], [-0.911651, -0.747362, -0.400637], [-0.911651, -0.759362, -0.400637], [-0.911651, -0.759362, -0.388637], [-0.899651, -0.759362, -0.388637], [-0.899651, -0.747362, -0.388637], [-0.899651, -0.747362, -0.400637], [-0.911651, -0.747362, -0.400637], [-0.911651, -0.747362, -0.388637], [-0.911651, -0.759362, -0.388637], [-0.911651, -0.759362, -0.400637], [-0.899651, -0.759362, -0.400637]]}]},
			"R_upperLid_B_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_B_CTLShape", "degree": 1, "form": 0, "points": [[-1.283345, 6.473132, 0.151961], [-1.288845, 6.467631, 0.151961], [-1.294345, 6.473132, 0.151961], [-1.288845, 6.478632, 0.151961], [-1.283345, 6.473132, 0.151961]]}]},
			"L_brow_A_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_A_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.644357, 7.850297, -1.13566], [0.612023, 7.85941, -1.140399], [0.582511, 7.851749, -1.125518], [0.573111, 7.831801, -1.099735], [0.589328, 7.811253, -1.078153], [0.621663, 7.80214, -1.073414], [0.651174, 7.809801, -1.088294], [0.660574, 7.829749, -1.114077]]}]},
			"L_upperLipSecondary_B_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.899651, 1.129795, -0.388637], [0.899651, 1.129795, -0.400637], [0.899651, 1.141795, -0.400637], [0.899651, 1.141795, -0.388637], [0.911651, 1.141795, -0.388637], [0.911651, 1.141795, -0.400637], [0.911651, 1.129795, -0.400637], [0.911651, 1.129795, -0.388637], [0.899651, 1.129795, -0.388637], [0.899651, 1.141795, -0.388637], [0.899651, 1.141795, -0.400637], [0.911651, 1.141795, -0.400637], [0.911651, 1.141795, -0.388637], [0.911651, 1.129795, -0.388637], [0.911651, 1.129795, -0.400637], [0.899651, 1.129795, -0.400637]]}]},
			"L_lowerLidPrimary_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lowerLidPrimary_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.686976, 5.461927, 0.139963], [1.686976, 5.466147, 0.144183], [1.686976, 5.461927, 0.148403], [1.686976, 5.457707, 0.144183], [1.686976, 5.461927, 0.139963], [1.691196, 5.461927, 0.144183], [1.686976, 5.461927, 0.148403], [1.682756, 5.461927, 0.144183], [1.686976, 5.466147, 0.144183], [1.691196, 5.461927, 0.144183], [1.686976, 5.457707, 0.144183], [1.682756, 5.461927, 0.144183], [1.686976, 5.461927, 0.139963], [1.691196, 5.461927, 0.144183], [1.288845, 5.461927, 0.144183]]}, {"shapeName": "L_lowerLidPrimary_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.288845, 5.860058, 0.139963], [1.284625, 5.860058, 0.144183], [1.288845, 5.860058, 0.148403], [1.293065, 5.860058, 0.144183], [1.288845, 5.860058, 0.139963], [1.288845, 5.864278, 0.144183], [1.288845, 5.860058, 0.148403], [1.288845, 5.855838, 0.144183], [1.284625, 5.860058, 0.144183], [1.288845, 5.864278, 0.144183], [1.293065, 5.860058, 0.144183], [1.288845, 5.855838, 0.144183], [1.288845, 5.860058, 0.139963], [1.288845, 5.864278, 0.144183], [1.288845, 5.461927, 0.144183]]}, {"shapeName": "L_lowerLidPrimary_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.288845, 5.466147, 0.542314], [1.284625, 5.461927, 0.542314], [1.288845, 5.457707, 0.542314], [1.293065, 5.461927, 0.542314], [1.288845, 5.466147, 0.542314], [1.288845, 5.461927, 0.546534], [1.288845, 5.457707, 0.542314], [1.288845, 5.461927, 0.538094], [1.284625, 5.461927, 0.542314], [1.288845, 5.461927, 0.546534], [1.293065, 5.461927, 0.542314], [1.288845, 5.461927, 0.538094], [1.288845, 5.466147, 0.542314], [1.288845, 5.461927, 0.546534], [1.288845, 5.461927, 0.144183]]}]},
			"R_lowerLipSecondary_A_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.467266, -0.97402, -0.386637], [-0.467266, -0.97402, -0.402637], [-0.467266, -0.95802, -0.402637], [-0.467266, -0.95802, -0.386637], [-0.483266, -0.95802, -0.386637], [-0.483266, -0.95802, -0.402637], [-0.483266, -0.97402, -0.402637], [-0.483266, -0.97402, -0.386637], [-0.467266, -0.97402, -0.386637], [-0.467266, -0.95802, -0.386637], [-0.467266, -0.95802, -0.402637], [-0.483266, -0.95802, -0.402637], [-0.483266, -0.95802, -0.386637], [-0.483266, -0.97402, -0.386637], [-0.483266, -0.97402, -0.402637], [-0.467266, -0.97402, -0.402637]]}]},
			"R_squint_C_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.160785, 2.851617, -0.198738], [-2.143689, 2.877244, -0.212984], [-2.177521, 2.875999, -0.215394], [-2.160785, 2.851617, -0.198738], [-2.146018, 2.875108, -0.179191], [-2.143689, 2.877244, -0.212984], [-2.162753, 2.89949, -0.195847], [-2.146018, 2.875108, -0.179191], [-2.17985, 2.873863, -0.181601], [-2.160785, 2.851617, -0.198738], [-2.177521, 2.875999, -0.215394], [-2.162753, 2.89949, -0.195847], [-2.17985, 2.873863, -0.181601], [-2.177521, 2.875999, -0.215394]]}]},
			"C_tongue_IK_B_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_B_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.078361, -0.078361, -2.532066], [0.110819, 0.0, -2.532066], [0.078361, 0.078361, -2.532066], [0.0, 0.110819, -2.532066], [-0.078361, 0.078361, -2.532066], [-0.110819, 0.0, -2.532066], [-0.078361, -0.078361, -2.532066], [0.0, -0.110819, -2.532066]]}]},
			"R_upperLipSecondary_B_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.896651, 1.126795, -0.385637], [-0.896651, 1.126795, -0.403637], [-0.896651, 1.144795, -0.403637], [-0.896651, 1.144795, -0.385637], [-0.914651, 1.144795, -0.385637], [-0.914651, 1.144795, -0.403637], [-0.914651, 1.126795, -0.403637], [-0.914651, 1.126795, -0.385637], [-0.896651, 1.126795, -0.385637], [-0.896651, 1.144795, -0.385637], [-0.896651, 1.144795, -0.403637], [-0.914651, 1.144795, -0.403637], [-0.914651, 1.144795, -0.385637], [-0.914651, 1.126795, -0.385637], [-0.914651, 1.126795, -0.403637], [-0.896651, 1.126795, -0.403637]]}]},
			"R_lookAt_A_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "R_lookAt_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.176313, 6.176313, 2.5], [-2.0, 6.249344, 2.5], [-1.823687, 6.176313, 2.5], [-1.750656, 6.0, 2.5], [-1.823687, 5.823687, 2.5], [-2.0, 5.750656, 2.5], [-2.176313, 5.823687, 2.5], [-2.249344, 6.0, 2.5]]}]},
			"L_cheek_C_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_C_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.16855, 2.658425, -0.243469], [2.14706, 2.672172, -0.215078], [2.122254, 2.657119, -0.190282], [2.108663, 2.622084, -0.183605], [2.114248, 2.587589, -0.198958], [2.135737, 2.573842, -0.227348], [2.160543, 2.588895, -0.252145], [2.174134, 2.623931, -0.258822]]}]},
			"R_brow_upper_B_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.963602, 8.095256, -1.625301], [-0.973556, 8.076765, -1.588928], [-1.013805, 8.075065, -1.600807], [-1.003851, 8.093556, -1.63718], [-0.963602, 8.095256, -1.625301]]}]},
			"C_lowerLipSecondary_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_lowerLipSecondary_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.008, -1.041783, -0.386637], [-0.008, -1.041783, -0.402637], [-0.008, -1.025783, -0.402637], [-0.008, -1.025783, -0.386637], [0.008, -1.025783, -0.386637], [0.008, -1.025783, -0.402637], [0.008, -1.041783, -0.402637], [0.008, -1.041783, -0.386637], [-0.008, -1.041783, -0.386637], [-0.008, -1.025783, -0.386637], [-0.008, -1.025783, -0.402637], [0.008, -1.025783, -0.402637], [0.008, -1.025783, -0.386637], [0.008, -1.041783, -0.386637], [0.008, -1.041783, -0.402637], [-0.008, -1.041783, -0.402637]]}]},
			"L_lowerLipSecondary_D_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_D_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.645693, -0.151506, -0.387637], [1.645693, -0.151506, -0.401637], [1.645693, -0.137506, -0.401637], [1.645693, -0.137506, -0.387637], [1.659693, -0.137506, -0.387637], [1.659693, -0.137506, -0.401637], [1.659693, -0.151506, -0.401637], [1.659693, -0.151506, -0.387637], [1.645693, -0.151506, -0.387637], [1.645693, -0.137506, -0.387637], [1.645693, -0.137506, -0.401637], [1.659693, -0.137506, -0.401637], [1.659693, -0.137506, -0.387637], [1.659693, -0.151506, -0.387637], [1.659693, -0.151506, -0.401637], [1.645693, -0.151506, -0.401637]]}]},
			"L_upperLipSecondary_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upperLipSecondary_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.929322, 1.135795, -0.405488], [1.929322, 1.146646, -0.394637], [1.929322, 1.135795, -0.383786], [1.929322, 1.124944, -0.394637], [1.929322, 1.135795, -0.405488], [1.940172, 1.135795, -0.394637], [1.929322, 1.135795, -0.383786], [1.918471, 1.135795, -0.394637], [1.929322, 1.146646, -0.394637], [1.940172, 1.135795, -0.394637], [1.929322, 1.124944, -0.394637], [1.918471, 1.135795, -0.394637], [1.929322, 1.135795, -0.405488], [1.940172, 1.135795, -0.394637], [0.905651, 1.135795, -0.394637]]}, {"shapeName": "L_upperLipSecondary_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.905651, 2.159466, -0.405488], [0.8948, 2.159466, -0.394637], [0.905651, 2.159466, -0.383786], [0.916502, 2.159466, -0.394637], [0.905651, 2.159466, -0.405488], [0.905651, 2.170316, -0.394637], [0.905651, 2.159466, -0.383786], [0.905651, 2.148615, -0.394637], [0.8948, 2.159466, -0.394637], [0.905651, 2.170316, -0.394637], [0.916502, 2.159466, -0.394637], [0.905651, 2.148615, -0.394637], [0.905651, 2.159466, -0.405488], [0.905651, 2.170316, -0.394637], [0.905651, 1.135795, -0.394637]]}, {"shapeName": "L_upperLipSecondary_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.905651, 1.146646, 0.629034], [0.8948, 1.135795, 0.629034], [0.905651, 1.124944, 0.629034], [0.916502, 1.135795, 0.629034], [0.905651, 1.146646, 0.629034], [0.905651, 1.135795, 0.639884], [0.905651, 1.124944, 0.629034], [0.905651, 1.135795, 0.618183], [0.8948, 1.135795, 0.629034], [0.905651, 1.135795, 0.639884], [0.916502, 1.135795, 0.629034], [0.905651, 1.135795, 0.618183], [0.905651, 1.146646, 0.629034], [0.905651, 1.135795, 0.639884], [0.905651, 1.135795, -0.394637]]}]},
			"L_cheek_A_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_A_CTLShape", "degree": 3, "form": 2, "points": [[1.946635, 2.617757, 0.263231], [1.919159, 2.634455, 0.290885], [1.887637, 2.619168, 0.314784], [1.870534, 2.58085, 0.320928], [1.877869, 2.541948, 0.305718], [1.905345, 2.52525, 0.278064], [1.936867, 2.540538, 0.254165], [1.95397, 2.578855, 0.248021]]}]},
			"L_lipZipper_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_lipZipper_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.083115, 0.200062, 2.055363], [0.074115, 0.182217, 2.055363], [0.092115, 0.182217, 2.055363], [0.083115, 0.200062, 2.055363], [0.083115, 0.200062, 2.055363]]}]},
			"C_upperLipSecondary_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_upperLipSecondary_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.007, 1.409217, -0.387637], [-0.007, 1.409217, -0.401637], [-0.007, 1.423217, -0.401637], [-0.007, 1.423217, -0.387637], [0.007, 1.423217, -0.387637], [0.007, 1.423217, -0.401637], [0.007, 1.409217, -0.401637], [0.007, 1.409217, -0.387637], [-0.007, 1.409217, -0.387637], [-0.007, 1.423217, -0.387637], [-0.007, 1.423217, -0.401637], [0.007, 1.423217, -0.401637], [0.007, 1.423217, -0.387637], [0.007, 1.409217, -0.387637], [0.007, 1.409217, -0.401637], [-0.007, 1.409217, -0.401637]]}]},
			"L_upperLidPrimary_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLidPrimary_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.292502, 6.476789, 0.144183], [1.288845, 6.478304, 0.144183], [1.285188, 6.476789, 0.144183], [1.283673, 6.473132, 0.144183], [1.285188, 6.469475, 0.144183], [1.288845, 6.46796, 0.144183], [1.292502, 6.469475, 0.144183], [1.294017, 6.473132, 0.144183]]}]},
			"L_lipCornerSecondary_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lipCornerSecondary_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.993, 0.184217, -0.387637], [1.993, 0.184217, -0.401637], [1.993, 0.198217, -0.401637], [1.993, 0.198217, -0.387637], [2.007, 0.198217, -0.387637], [2.007, 0.198217, -0.401637], [2.007, 0.184217, -0.401637], [2.007, 0.184217, -0.387637], [1.993, 0.184217, -0.387637], [1.993, 0.198217, -0.387637], [1.993, 0.198217, -0.401637], [2.007, 0.198217, -0.401637], [2.007, 0.198217, -0.387637], [2.007, 0.184217, -0.387637], [2.007, 0.184217, -0.401637], [1.993, 0.184217, -0.401637]]}]},
			"L_cheek_B_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_B_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.995028, 2.651536, -0.054841], [1.971831, 2.665934, -0.028169], [1.945159, 2.651536, -0.004972], [1.930637, 2.616776, 0.001162], [1.93677, 2.582015, -0.013361], [1.959967, 2.567617, -0.040033], [1.986639, 2.582015, -0.06323], [2.001162, 2.616776, -0.069363]]}]},
			"L_upperLid_B_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.285344, 6.476632, 0.144183], [1.285344, 6.469631, 0.144183], [1.292345, 6.469631, 0.144183], [1.292345, 6.476632, 0.144183], [1.285344, 6.476632, 0.144183]]}]},
			"R_lowerLipSecondary_C_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_C_CTLShape", "degree": 1, "form": 0, "points": [[-1.281093, -0.473611, -0.384637], [-1.281093, -0.473611, -0.404637], [-1.281093, -0.453611, -0.404637], [-1.281093, -0.453611, -0.384637], [-1.301093, -0.453611, -0.384637], [-1.301093, -0.453611, -0.404637], [-1.301093, -0.473611, -0.404637], [-1.301093, -0.473611, -0.384637], [-1.281093, -0.473611, -0.384637], [-1.281093, -0.453611, -0.384637], [-1.281093, -0.453611, -0.404637], [-1.301093, -0.453611, -0.404637], [-1.301093, -0.453611, -0.384637], [-1.301093, -0.473611, -0.384637], [-1.301093, -0.473611, -0.404637], [-1.281093, -0.473611, -0.404637]]}]},
			"L_outterLid_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_outterLid_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.464826, 5.967529, 0.139963], [2.464826, 5.971749, 0.144183], [2.464826, 5.967529, 0.148403], [2.464826, 5.963309, 0.144183], [2.464826, 5.967529, 0.139963], [2.469046, 5.967529, 0.144183], [2.464826, 5.967529, 0.148403], [2.460606, 5.967529, 0.144183], [2.464826, 5.971749, 0.144183], [2.469046, 5.967529, 0.144183], [2.464826, 5.963309, 0.144183], [2.460606, 5.967529, 0.144183], [2.464826, 5.967529, 0.139963], [2.469046, 5.967529, 0.144183], [2.066695, 5.967529, 0.144183]]}, {"shapeName": "L_outterLid_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.066695, 6.36566, 0.139963], [2.062475, 6.36566, 0.144183], [2.066695, 6.36566, 0.148403], [2.070915, 6.36566, 0.144183], [2.066695, 6.36566, 0.139963], [2.066695, 6.36988, 0.144183], [2.066695, 6.36566, 0.148403], [2.066695, 6.36144, 0.144183], [2.062475, 6.36566, 0.144183], [2.066695, 6.36988, 0.144183], [2.070915, 6.36566, 0.144183], [2.066695, 6.36144, 0.144183], [2.066695, 6.36566, 0.139963], [2.066695, 6.36988, 0.144183], [2.066695, 5.967529, 0.144183]]}, {"shapeName": "L_outterLid_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.066695, 5.971749, 0.542314], [2.062475, 5.967529, 0.542314], [2.066695, 5.963309, 0.542314], [2.070915, 5.967529, 0.542314], [2.066695, 5.971749, 0.542314], [2.066695, 5.967529, 0.546534], [2.066695, 5.963309, 0.542314], [2.066695, 5.967529, 0.538094], [2.062475, 5.967529, 0.542314], [2.066695, 5.967529, 0.546534], [2.070915, 5.967529, 0.542314], [2.066695, 5.967529, 0.538094], [2.066695, 5.971749, 0.542314], [2.066695, 5.967529, 0.546534], [2.066695, 5.967529, 0.144183]]}]},
			"R_lipCorner_CTL": {"color": 17, "shapes": [{"shapeName": "R_lipCorner_CTLShape", "degree": 3, "form": 2, "points": [[-2.01959, 0.210807, -0.394637], [-2.0, 0.218921, -0.394637], [-1.98041, 0.210807, -0.394637], [-1.972295, 0.191217, -0.394637], [-1.98041, 0.171626, -0.394637], [-2.0, 0.163512, -0.394637], [-2.01959, 0.171626, -0.394637], [-2.027705, 0.191217, -0.394637]]}]},
			"R_brow_upper_C_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.382626, 8.071591, -1.774607], [-1.399344, 8.049893, -1.73519], [-1.442867, 8.047026, -1.755228], [-1.426149, 8.068724, -1.794645], [-1.382626, 8.071591, -1.774607]]}]},
			"R_eye_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_eye_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.989149, 6.0, -0.523671], [-2.0, 6.010851, -0.523671], [-2.010851, 6.0, -0.523671], [-2.0, 5.989149, -0.523671], [-1.989149, 6.0, -0.523671], [-2.0, 6.0, -0.534521], [-2.010851, 6.0, -0.523671], [-2.0, 6.0, -0.51282], [-2.0, 6.010851, -0.523671], [-2.0, 6.0, -0.534521], [-2.0, 5.989149, -0.523671], [-2.0, 6.0, -0.51282], [-1.989149, 6.0, -0.523671], [-2.0, 6.0, -0.534521], [-2.0, 6.0, 0.5]]}, {"shapeName": "R_eye_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.989149, 7.023671, 0.5], [-2.0, 7.023671, 0.510851], [-2.010851, 7.023671, 0.5], [-2.0, 7.023671, 0.489149], [-1.989149, 7.023671, 0.5], [-2.0, 7.034521, 0.5], [-2.010851, 7.023671, 0.5], [-2.0, 7.01282, 0.5], [-2.0, 7.023671, 0.510851], [-2.0, 7.034521, 0.5], [-2.0, 7.023671, 0.489149], [-2.0, 7.01282, 0.5], [-1.989149, 7.023671, 0.5], [-2.0, 7.034521, 0.5], [-2.0, 6.0, 0.5]]}, {"shapeName": "R_eye_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-3.023671, 6.010851, 0.5], [-3.023671, 6.0, 0.510851], [-3.023671, 5.989149, 0.5], [-3.023671, 6.0, 0.489149], [-3.023671, 6.010851, 0.5], [-3.034521, 6.0, 0.5], [-3.023671, 5.989149, 0.5], [-3.01282, 6.0, 0.5], [-3.023671, 6.0, 0.510851], [-3.034521, 6.0, 0.5], [-3.023671, 6.0, 0.489149], [-3.01282, 6.0, 0.5], [-3.023671, 6.010851, 0.5], [-3.034521, 6.0, 0.5], [-2.0, 6.0, 0.5]]}]},
			"R_lowerLid_A_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.897197, 5.581327, 0.144183], [-0.897197, 5.575882, 0.144183], [-0.902642, 5.575882, 0.144183], [-0.902642, 5.581327, 0.144183], [-0.897197, 5.581327, 0.144183]]}]},
			"L_brow_upper_A_A_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.473915, 8.108577, -1.519622], [0.480298, 8.084847, -1.471537], [0.533745, 8.083754, -1.479172], [0.527361, 8.107484, -1.527256], [0.473915, 8.108577, -1.519622]]}]},
			"L_cheek_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_cheek_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.68218, 2.618601, -0.765509], [2.691035, 2.627472, -0.756655], [2.697307, 2.61495, -0.750382], [2.688453, 2.606079, -0.759236], [2.68218, 2.618601, -0.765509], [2.697416, 2.616776, -0.765618], [2.697307, 2.61495, -0.750382], [2.682071, 2.616776, -0.750273], [2.691035, 2.627472, -0.756655], [2.697416, 2.616776, -0.765618], [2.688453, 2.606079, -0.759236], [2.682071, 2.616776, -0.750273], [2.68218, 2.618601, -0.765509], [2.697416, 2.616776, -0.765618], [1.965899, 2.616776, -0.034101]]}, {"shapeName": "L_cheek_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.080102, 3.627684, 0.080102], [2.079993, 3.625858, 0.095339], [2.095229, 3.624033, 0.095229], [2.095339, 3.625858, 0.079993], [2.080102, 3.627684, 0.080102], [2.088956, 3.636554, 0.088956], [2.095229, 3.624033, 0.095229], [2.086375, 3.615162, 0.086375], [2.079993, 3.625858, 0.095339], [2.088956, 3.636554, 0.088956], [2.095339, 3.625858, 0.079993], [2.086375, 3.615162, 0.086375], [2.080102, 3.627684, 0.080102], [2.088956, 3.636554, 0.088956], [1.965899, 2.616776, -0.034101]]}, {"shapeName": "L_cheek_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.680719, 2.455268, 0.680719], [2.671756, 2.444571, 0.687101], [2.678138, 2.433875, 0.678138], [2.687101, 2.444571, 0.671756], [2.680719, 2.455268, 0.680719], [2.686991, 2.442746, 0.686991], [2.678138, 2.433875, 0.678138], [2.671865, 2.446397, 0.671865], [2.671756, 2.444571, 0.687101], [2.686991, 2.442746, 0.686991], [2.687101, 2.444571, 0.671756], [2.671865, 2.446397, 0.671865], [2.680719, 2.455268, 0.680719], [2.686991, 2.442746, 0.686991], [1.965899, 2.616776, -0.034101]]}]},
			"R_cheek_B_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_B_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.988555, 2.643811, -0.050232], [-1.970513, 2.65501, -0.029487], [-1.949768, 2.643811, -0.011445], [-1.938473, 2.616776, -0.006674], [-1.943243, 2.58974, -0.01797], [-1.961285, 2.578541, -0.038715], [-1.98203, 2.58974, -0.056757], [-1.993326, 2.616776, -0.061527]]}]},
			"L_lipCornerSecondary_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lipCornerSecondary_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.992, 0.183217, -0.386637], [1.992, 0.183217, -0.402637], [1.992, 0.199217, -0.402637], [1.992, 0.199217, -0.386637], [2.008, 0.199217, -0.386637], [2.008, 0.199217, -0.402637], [2.008, 0.183217, -0.402637], [2.008, 0.183217, -0.386637], [1.992, 0.183217, -0.386637], [1.992, 0.199217, -0.386637], [1.992, 0.199217, -0.402637], [2.008, 0.199217, -0.402637], [2.008, 0.199217, -0.386637], [2.008, 0.183217, -0.386637], [2.008, 0.183217, -0.402637], [1.992, 0.183217, -0.402637]]}]},
			"R_lipCorner_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lipCorner_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.011754, 0.202971, -0.394637], [-2.0, 0.207839, -0.394637], [-1.988246, 0.202971, -0.394637], [-1.983377, 0.191217, -0.394637], [-1.988246, 0.179462, -0.394637], [-2.0, 0.174594, -0.394637], [-2.011754, 0.179462, -0.394637], [-2.016623, 0.191217, -0.394637]]}]},
			"L_upperLid_B_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.286511, 6.475465, 0.144183], [1.286511, 6.470798, 0.144183], [1.291178, 6.470798, 0.144183], [1.291178, 6.475465, 0.144183], [1.286511, 6.475465, 0.144183]]}]},
			"R_squint_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_squint_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.825458, 2.89531, -0.976489], [-2.834078, 2.905368, -0.968741], [-2.841807, 2.893781, -0.9623], [-2.833188, 2.883723, -0.970048], [-2.825458, 2.89531, -0.976489], [-2.840754, 2.894747, -0.977578], [-2.841807, 2.893781, -0.9623], [-2.826511, 2.894344, -0.96121], [-2.834078, 2.905368, -0.968741], [-2.840754, 2.894747, -0.977578], [-2.833188, 2.883723, -0.970048], [-2.826511, 2.894344, -0.96121], [-2.825458, 2.89531, -0.976489], [-2.840754, 2.894747, -0.977578], [-2.161769, 2.875554, -0.197292]]}, {"shapeName": "R_squint_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-2.195566, 3.897269, -0.142752], [-2.196619, 3.896304, -0.127473], [-2.211915, 3.895741, -0.128563], [-2.210862, 3.896706, -0.143841], [-2.195566, 3.897269, -0.142752], [-2.204185, 3.907326, -0.135004], [-2.211915, 3.895741, -0.128563], [-2.203296, 3.885683, -0.13631], [-2.196619, 3.896304, -0.127473], [-2.204185, 3.907326, -0.135004], [-2.210862, 3.896706, -0.143841], [-2.203296, 3.885683, -0.13631], [-2.195566, 3.897269, -0.142752], [-2.204185, 3.907326, -0.135004], [-2.161769, 2.875554, -0.197292]]}, {"shapeName": "R_squint_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.933408, 2.814266, 0.472661], [-2.925842, 2.803243, 0.480192], [-2.932519, 2.792622, 0.471354], [-2.940085, 2.803645, 0.463823], [-2.933408, 2.814266, 0.472661], [-2.941137, 2.80268, 0.479101], [-2.932519, 2.792622, 0.471354], [-2.924789, 2.804208, 0.464913], [-2.925842, 2.803243, 0.480192], [-2.941137, 2.80268, 0.479101], [-2.940085, 2.803645, 0.463823], [-2.924789, 2.804208, 0.464913], [-2.933408, 2.814266, 0.472661], [-2.941137, 2.80268, 0.479101], [-2.161769, 2.875554, -0.197292]]}]},
			"L_upperLidPrimary_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upperLidPrimary_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.686976, 6.473132, 0.139963], [1.686976, 6.477352, 0.144183], [1.686976, 6.473132, 0.148403], [1.686976, 6.468911, 0.144183], [1.686976, 6.473132, 0.139963], [1.691196, 6.473132, 0.144183], [1.686976, 6.473132, 0.148403], [1.682756, 6.473132, 0.144183], [1.686976, 6.477352, 0.144183], [1.691196, 6.473132, 0.144183], [1.686976, 6.468911, 0.144183], [1.682756, 6.473132, 0.144183], [1.686976, 6.473132, 0.139963], [1.691196, 6.473132, 0.144183], [1.288845, 6.473132, 0.144183]]}, {"shapeName": "L_upperLidPrimary_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.288845, 6.871263, 0.139963], [1.284625, 6.871263, 0.144183], [1.288845, 6.871263, 0.148403], [1.293065, 6.871263, 0.144183], [1.288845, 6.871263, 0.139963], [1.288845, 6.875483, 0.144183], [1.288845, 6.871263, 0.148403], [1.288845, 6.867043, 0.144183], [1.284625, 6.871263, 0.144183], [1.288845, 6.875483, 0.144183], [1.293065, 6.871263, 0.144183], [1.288845, 6.867043, 0.144183], [1.288845, 6.871263, 0.139963], [1.288845, 6.875483, 0.144183], [1.288845, 6.473132, 0.144183]]}, {"shapeName": "L_upperLidPrimary_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.288845, 6.477352, 0.542314], [1.284625, 6.473132, 0.542314], [1.288845, 6.468911, 0.542314], [1.293065, 6.473132, 0.542314], [1.288845, 6.477352, 0.542314], [1.288845, 6.473132, 0.546534], [1.288845, 6.468911, 0.542314], [1.288845, 6.473132, 0.538094], [1.284625, 6.473132, 0.542314], [1.288845, 6.473132, 0.546534], [1.293065, 6.473132, 0.542314], [1.288845, 6.473132, 0.538094], [1.288845, 6.477352, 0.542314], [1.288845, 6.473132, 0.546534], [1.288845, 6.473132, 0.144183]]}]},
			"L_upperLipSecondary_B_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.898651, 1.128795, -0.387637], [0.898651, 1.128795, -0.401637], [0.898651, 1.142795, -0.401637], [0.898651, 1.142795, -0.387637], [0.912651, 1.142795, -0.387637], [0.912651, 1.142795, -0.401637], [0.912651, 1.128795, -0.401637], [0.912651, 1.128795, -0.387637], [0.898651, 1.128795, -0.387637], [0.898651, 1.142795, -0.387637], [0.898651, 1.142795, -0.401637], [0.912651, 1.142795, -0.401637], [0.912651, 1.142795, -0.387637], [0.912651, 1.128795, -0.387637], [0.912651, 1.128795, -0.401637], [0.898651, 1.128795, -0.401637]]}]},
			"R_brow_upper_C_C_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.386391, 8.070056, -1.773396], [-1.40102, 8.05107, -1.738906], [-1.439102, 8.048561, -1.756439], [-1.424474, 8.067547, -1.790929], [-1.386391, 8.070056, -1.773396]]}]},
			"R_cheek_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.546711, 2.597085, -0.545902], [-2.555076, 2.605943, -0.536571], [-2.560736, 2.593415, -0.529752], [-2.552371, 2.584557, -0.539082], [-2.546711, 2.597085, -0.545902], [-2.561893, 2.595055, -0.544965], [-2.560736, 2.593415, -0.529752], [-2.545554, 2.595445, -0.530688], [-2.555076, 2.605943, -0.536571], [-2.561893, 2.595055, -0.544965], [-2.552371, 2.584557, -0.539082], [-2.545554, 2.595445, -0.530688], [-2.546711, 2.597085, -0.545902], [-2.561893, 2.595055, -0.544965], [-1.783006, 2.613676, 0.13564]]}, {"shapeName": "R_cheek_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.903601, 3.624269, 0.245999], [-1.902443, 3.622629, 0.261213], [-1.917625, 3.620599, 0.262149], [-1.918783, 3.622239, 0.246935], [-1.903601, 3.624269, 0.245999], [-1.911965, 3.633126, 0.255329], [-1.917625, 3.620599, 0.262149], [-1.90926, 3.611741, 0.252819], [-1.902443, 3.622629, 0.261213], [-1.911965, 3.633126, 0.255329], [-1.918783, 3.622239, 0.246935], [-1.90926, 3.611741, 0.252819], [-1.903601, 3.624269, 0.245999], [-1.911965, 3.633126, 0.255329], [-1.783006, 2.613676, 0.13564]]}, {"shapeName": "R_cheek_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.445883, 2.451249, 0.898682], [-2.436361, 2.440752, 0.904565], [-2.443178, 2.429863, 0.896171], [-2.4527, 2.440361, 0.890288], [-2.445883, 2.451249, 0.898682], [-2.451542, 2.438721, 0.905501], [-2.443178, 2.429863, 0.896171], [-2.437518, 2.442391, 0.889351], [-2.436361, 2.440752, 0.904565], [-2.451542, 2.438721, 0.905501], [-2.4527, 2.440361, 0.890288], [-2.437518, 2.442391, 0.889351], [-2.445883, 2.451249, 0.898682], [-2.451542, 2.438721, 0.905501], [-1.783006, 2.613676, 0.13564]]}]},
			"R_outterLid_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_outterLid_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.064361, 5.969863, 0.144183], [-2.064361, 5.965196, 0.144183], [-2.069028, 5.965196, 0.144183], [-2.069028, 5.969863, 0.144183], [-2.064361, 5.969863, 0.144183]]}]},
			"L_brow_upper_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_brow_upper_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.516138, 8.065709, -1.648812], [1.515725, 8.080222, -1.653781], [1.517877, 8.085198, -1.639425], [1.51829, 8.070685, -1.634456], [1.516138, 8.065709, -1.648812], [1.527746, 8.075234, -1.645652], [1.517877, 8.085198, -1.639425], [1.506268, 8.075673, -1.642584], [1.515725, 8.080222, -1.653781], [1.527746, 8.075234, -1.645652], [1.51829, 8.070685, -1.634456], [1.506268, 8.075673, -1.642584], [1.516138, 8.065709, -1.648812], [1.527746, 8.075234, -1.645652], [0.50383, 8.096166, -1.499397]]}, {"shapeName": "L_brow_upper_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.381953, 8.536264, -2.415628], [0.372083, 8.546229, -2.4094], [0.383692, 8.555754, -2.406241], [0.393562, 8.545789, -2.412468], [0.381953, 8.536264, -2.415628], [0.38154, 8.550777, -2.420596], [0.383692, 8.555754, -2.406241], [0.384105, 8.541241, -2.401272], [0.372083, 8.546229, -2.4094], [0.38154, 8.550777, -2.420596], [0.393562, 8.545789, -2.412468], [0.384105, 8.541241, -2.401272], [0.381953, 8.536264, -2.415628], [0.38154, 8.550777, -2.420596], [0.50383, 8.096166, -1.499397]]}, {"shapeName": "L_brow_upper_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.584587, 9.020235, -1.066275], [0.57513, 9.015686, -1.055079], [0.587152, 9.010698, -1.046951], [0.596609, 9.015247, -1.058147], [0.584587, 9.020235, -1.066275], [0.586739, 9.02521, -1.05192], [0.587152, 9.010698, -1.046951], [0.585, 9.005722, -1.061307], [0.57513, 9.015686, -1.055079], [0.586739, 9.02521, -1.05192], [0.596609, 9.015247, -1.058147], [0.585, 9.005722, -1.061307], [0.584587, 9.020235, -1.066275], [0.586739, 9.02521, -1.05192], [0.50383, 8.096166, -1.499397]]}]},
			"L_cheekLower_A_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_A_CTLShape", "degree": 3, "form": 2, "points": [[1.868764, 2.114905, 0.187846], [1.842071, 2.131351, 0.216402], [1.80977, 2.116313, 0.239404], [1.790784, 2.078601, 0.243376], [1.796234, 2.040304, 0.225992], [1.822927, 2.023858, 0.197435], [1.855227, 2.038896, 0.174434], [1.874213, 2.076608, 0.170462]]}]},
			"R_cheekLower_B_A_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_B_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.919977, 2.15898, -0.129892], [-1.897553, 2.173149, -0.102447], [-1.870108, 2.15898, -0.080023], [-1.853719, 2.124776, -0.075756], [-1.857986, 2.090571, -0.092145], [-1.88041, 2.076403, -0.11959], [-1.907855, 2.090571, -0.142014], [-1.924244, 2.124776, -0.146281]]}]},
			"L_eye_FK_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_eye_FK_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.010851, 6.0, 1.523671], [2.0, 6.010851, 1.523671], [1.989149, 6.0, 1.523671], [2.0, 5.989149, 1.523671], [2.010851, 6.0, 1.523671], [2.0, 6.0, 1.534521], [1.989149, 6.0, 1.523671], [2.0, 6.0, 1.51282], [2.0, 6.010851, 1.523671], [2.0, 6.0, 1.534521], [2.0, 5.989149, 1.523671], [2.0, 6.0, 1.51282], [2.010851, 6.0, 1.523671], [2.0, 6.0, 1.534521], [2.0, 6.0, 0.5]]}, {"shapeName": "L_eye_FK_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.010851, 7.023671, 0.5], [2.0, 7.023671, 0.489149], [1.989149, 7.023671, 0.5], [2.0, 7.023671, 0.510851], [2.010851, 7.023671, 0.5], [2.0, 7.034521, 0.5], [1.989149, 7.023671, 0.5], [2.0, 7.01282, 0.5], [2.0, 7.023671, 0.489149], [2.0, 7.034521, 0.5], [2.0, 7.023671, 0.510851], [2.0, 7.01282, 0.5], [2.010851, 7.023671, 0.5], [2.0, 7.034521, 0.5], [2.0, 6.0, 0.5]]}, {"shapeName": "L_eye_FK_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.976329, 6.010851, 0.5], [0.976329, 6.0, 0.489149], [0.976329, 5.989149, 0.5], [0.976329, 6.0, 0.510851], [0.976329, 6.010851, 0.5], [0.965479, 6.0, 0.5], [0.976329, 5.989149, 0.5], [0.98718, 6.0, 0.5], [0.976329, 6.0, 0.489149], [0.965479, 6.0, 0.5], [0.976329, 6.0, 0.510851], [0.98718, 6.0, 0.5], [0.976329, 6.010851, 0.5], [0.965479, 6.0, 0.5], [2.0, 6.0, 0.5]]}]},
			"C_lowerLip_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lowerLip_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.015672, -1.018111, -0.394637], [0.0, -1.01162, -0.394637], [-0.015672, -1.018111, -0.394637], [-0.022164, -1.033783, -0.394637], [-0.015672, -1.049456, -0.394637], [0.0, -1.055947, -0.394637], [0.015672, -1.049456, -0.394637], [0.022164, -1.033783, -0.394637]]}]},
			"C_lookAt_CTL": {"color": 17, "shapes": [{"shapeName": "C_lookAt_CTLShape", "degree": 1, "form": 0, "points": [[-0.498069, 6.031226, 3.067752], [-0.498069, 5.968774, 3.067752], [-0.498069, 5.968774, 3.0053], [-0.498069, 6.031226, 3.0053], [-0.498069, 6.031226, 3.067752], [0.498069, 6.031226, 3.067752], [0.498069, 5.968774, 3.067752], [0.498069, 5.968774, 3.0053], [0.498069, 6.031226, 3.0053], [0.498069, 6.031226, 3.067752], [0.498069, 5.968774, 3.067752], [-0.498069, 5.968774, 3.067752], [-0.498069, 5.968774, 3.0053], [0.498069, 5.968774, 3.0053], [0.498069, 6.031226, 3.0053], [-0.498069, 6.031226, 3.0053], [-0.498069, 6.031226, 3.067752], [-0.031, 6.031, 3.067526], [-0.031226, 5.501931, 3.067752], [-0.031226, 5.501931, 3.0053], [0.031226, 5.501931, 3.0053], [0.031226, 5.501931, 3.067752], [-0.031226, 5.501931, 3.067752], [-0.031226, 6.498069, 3.067752], [0.031226, 6.498069, 3.067752], [0.031226, 6.498069, 3.0053], [-0.031226, 6.498069, 3.0053], [-0.031226, 6.498069, 3.067752], [-0.031226, 6.498069, 3.0053], [-0.031226, 5.501931, 3.0053], [0.031226, 5.501931, 3.0053], [0.031226, 6.498069, 3.0053], [0.031226, 6.498069, 3.067752], [0.031226, 5.501931, 3.067752], [0.031, 5.969, 3.067526], [0.031226, 5.968774, 3.534595], [-0.031226, 5.968774, 3.534595], [-0.031226, 6.031226, 3.534595], [0.031226, 6.031226, 3.534595], [0.031226, 5.968774, 3.534595], [0.031226, 5.968774, 2.538457], [0.031226, 6.031226, 2.538457], [-0.031226, 6.031226, 2.538457], [-0.031226, 5.968774, 2.538457], [0.031226, 5.968774, 2.538457], [-0.031226, 5.968774, 2.538457], [-0.031226, 5.968774, 3.534595], [-0.031226, 6.031226, 3.534595], [-0.031226, 6.031226, 2.538457], [0.031226, 6.031226, 2.538457], [0.031226, 6.031226, 3.534595]]}]},
			"C_noseTip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_noseTip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 5.147208, -1.024575], [1.023671, 5.158059, -1.013724], [1.023671, 5.147208, -1.002873], [1.023671, 5.136357, -1.013724], [1.023671, 5.147208, -1.024575], [1.034521, 5.147208, -1.013724], [1.023671, 5.147208, -1.002873], [1.01282, 5.147208, -1.013724], [1.023671, 5.158059, -1.013724], [1.034521, 5.147208, -1.013724], [1.023671, 5.136357, -1.013724], [1.01282, 5.147208, -1.013724], [1.023671, 5.147208, -1.024575], [1.034521, 5.147208, -1.013724], [0.0, 5.147208, -1.013724]]}, {"shapeName": "C_noseTip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 6.170879, -1.024575], [-0.010851, 6.170879, -1.013724], [0.0, 6.170879, -1.002873], [0.010851, 6.170879, -1.013724], [0.0, 6.170879, -1.024575], [0.0, 6.181729, -1.013724], [0.0, 6.170879, -1.002873], [0.0, 6.160028, -1.013724], [-0.010851, 6.170879, -1.013724], [0.0, 6.181729, -1.013724], [0.010851, 6.170879, -1.013724], [0.0, 6.160028, -1.013724], [0.0, 6.170879, -1.024575], [0.0, 6.181729, -1.013724], [0.0, 5.147208, -1.013724]]}, {"shapeName": "C_noseTip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 5.158059, 0.009947], [-0.010851, 5.147208, 0.009947], [0.0, 5.136357, 0.009947], [0.010851, 5.147208, 0.009947], [0.0, 5.158059, 0.009947], [0.0, 5.147208, 0.020797], [0.0, 5.136357, 0.009947], [0.0, 5.147208, -0.000904], [-0.010851, 5.147208, 0.009947], [0.0, 5.147208, 0.020797], [0.010851, 5.147208, 0.009947], [0.0, 5.147208, -0.000904], [0.0, 5.158059, 0.009947], [0.0, 5.147208, 0.020797], [0.0, 5.147208, -1.013724]]}]},
			"L_lowerLip_A_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lowerLip_A_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.118301, -0.597658, -0.394637], [1.102629, -0.591166, -0.394637], [1.086956, -0.597658, -0.394637], [1.080465, -0.61333, -0.394637], [1.086956, -0.629002, -0.394637], [1.102629, -0.635494, -0.394637], [1.118301, -0.629002, -0.394637], [1.124792, -0.61333, -0.394637]]}]},
			"L_upperLid_B_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.285733, 6.476243, 0.144183], [1.285733, 6.47002, 0.144183], [1.291956, 6.47002, 0.144183], [1.291956, 6.476243, 0.144183], [1.285733, 6.476243, 0.144183]]}]},
			"R_brow_upper_C_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.378861, 8.073127, -1.775818], [-1.397669, 8.048717, -1.731474], [-1.446632, 8.04549, -1.754017], [-1.427825, 8.069901, -1.798361], [-1.378861, 8.073127, -1.775818]]}]},
			"C_tongue_IK_C_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_C_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.068566, -0.068566, -1.907066], [0.096967, 0.0, -1.907066], [0.068566, 0.068566, -1.907066], [0.0, 0.096967, -1.907066], [-0.068566, 0.068566, -1.907066], [-0.096967, 0.0, -1.907066], [-0.068566, -0.068566, -1.907066], [0.0, -0.096967, -1.907066]]}]},
			"L_cheek_A_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_A_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.810513, 2.644, 0.118645], [1.788532, 2.657358, 0.140769], [1.763315, 2.645128, 0.159888], [1.749632, 2.614474, 0.164803], [1.7555, 2.583352, 0.152635], [1.777481, 2.569994, 0.130512], [1.802698, 2.582224, 0.111393], [1.816381, 2.612878, 0.106477]]}]},
			"C_brow_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_brow_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 7.81635, -1.047917], [1.023671, 7.831648, -1.049127], [1.023671, 7.832859, -1.033829], [1.023671, 7.817561, -1.032619], [1.023671, 7.81635, -1.047917], [1.034521, 7.824604, -1.040873], [1.023671, 7.832859, -1.033829], [1.01282, 7.824604, -1.040873], [1.023671, 7.831648, -1.049127], [1.034521, 7.824604, -1.040873], [1.023671, 7.817561, -1.032619], [1.01282, 7.824604, -1.040873], [1.023671, 7.81635, -1.047917], [1.034521, 7.824604, -1.040873], [-0.0, 7.824604, -1.040873]]}, {"shapeName": "C_brow_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.0, 8.48083, -1.826614], [-0.010851, 8.489084, -1.81957], [-0.0, 8.497338, -1.812527], [0.010851, 8.489084, -1.81957], [-0.0, 8.48083, -1.826614], [-0.0, 8.496127, -1.827824], [-0.0, 8.497338, -1.812527], [-0.0, 8.48204, -1.811316], [-0.010851, 8.489084, -1.81957], [-0.0, 8.496127, -1.827824], [0.010851, 8.489084, -1.81957], [-0.0, 8.48204, -1.811316], [-0.0, 8.48083, -1.826614], [-0.0, 8.496127, -1.827824], [-0.0, 7.824604, -1.040873]]}, {"shapeName": "C_brow_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.0, 8.610345, -0.384648], [-0.010851, 8.603302, -0.376394], [-0.0, 8.596258, -0.368139], [0.010851, 8.603302, -0.376394], [-0.0, 8.610345, -0.384648], [-0.0, 8.611555, -0.369351], [-0.0, 8.596258, -0.368139], [-0.0, 8.595047, -0.383437], [-0.010851, 8.603302, -0.376394], [-0.0, 8.611555, -0.369351], [0.010851, 8.603302, -0.376394], [-0.0, 8.595047, -0.383437], [-0.0, 8.610345, -0.384648], [-0.0, 8.611555, -0.369351], [-0.0, 7.824604, -1.040873]]}]},
			"L_eye_FK_A_OFF_CTL": {"color": 8, "shapes": [{"shapeName": "L_eye_FK_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.0, 6.0, 0.5], [2.1125, 6.0, 0.3875], [2.103937, 5.956948, 0.3875], [2.0, 6.0, 0.5], [1.8875, 6.0, 0.3875], [1.896063, 6.043052, 0.3875], [2.0, 6.0, 0.5], [2.079549, 5.920451, 0.3875], [2.043052, 5.896064, 0.3875], [2.0, 6.0, 0.5], [1.920451, 6.07955, 0.3875], [1.956948, 6.103936, 0.3875], [2.0, 6.0, 0.5], [2.0, 5.8875, 0.3875], [1.956948, 5.896064, 0.3875], [2.0, 6.0, 0.5], [2.0, 6.1125, 0.3875], [2.043052, 6.103936, 0.3875], [2.0, 6.0, 0.5], [1.92045, 5.920451, 0.3875], [1.896063, 5.956948, 0.3875], [2.0, 6.0, 0.5], [2.079549, 6.079549, 0.3875], [2.103937, 6.043052, 0.3875], [2.1125, 6.0, 0.3875], [2.103937, 5.956948, 0.3875], [2.079549, 5.920451, 0.3875], [2.043052, 5.896064, 0.3875], [2.0, 5.8875, 0.3875], [1.956948, 5.896064, 0.3875], [1.92045, 5.920451, 0.3875], [1.896063, 5.956948, 0.3875], [1.8875, 6.0, 0.3875], [1.896063, 6.043052, 0.3875], [1.920451, 6.07955, 0.3875], [1.956948, 6.103936, 0.3875], [2.0, 6.1125, 0.3875], [2.043052, 6.103936, 0.3875], [2.079549, 6.079549, 0.3875], [2.103937, 6.043052, 0.3875], [2.0, 6.0, 0.5]]}]},
			"L_lowerLidPrimary_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLidPrimary_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.293721, 5.466803, 0.144183], [1.288845, 5.468823, 0.144183], [1.283969, 5.466803, 0.144183], [1.281949, 5.461927, 0.144183], [1.283969, 5.45705, 0.144183], [1.288845, 5.455031, 0.144183], [1.293721, 5.45705, 0.144183], [1.295741, 5.461927, 0.144183]]}]},
			"L_brow_A_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_A_CTLShape", "degree": 3, "form": 2, "points": [[0.675635, 8.007778, -1.015892], [0.635216, 8.019169, -1.021816], [0.598327, 8.009592, -1.003216], [0.586577, 7.984658, -0.970987], [0.606848, 7.958973, -0.944008], [0.647267, 7.947582, -0.938085], [0.684156, 7.957158, -0.956685], [0.695906, 7.982093, -0.988914]]}]},
			"L_lipZipper_CTL": {"color": 14, "shapes": [{"shapeName": "L_lipZipper_CTLShape", "degree": 1, "form": 0, "points": [[0.073287, 0.191217, 2.055363], [0.093115, 0.181217, 2.055363], [0.093115, 0.201217, 2.055363], [0.073287, 0.191217, 2.055363], [0.073287, 0.191217, 2.055363]]}]},
			"R_lowerLidPrimary_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lowerLidPrimary_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.687036, 5.462474, 0.139964], [-1.687036, 5.466694, 0.144183], [-1.687036, 5.462474, 0.148402], [-1.687036, 5.458255, 0.144183], [-1.687036, 5.462474, 0.139964], [-1.691256, 5.462474, 0.144183], [-1.687036, 5.462474, 0.148402], [-1.682817, 5.462474, 0.144183], [-1.687036, 5.466694, 0.144183], [-1.691256, 5.462474, 0.144183], [-1.687036, 5.458255, 0.144183], [-1.682817, 5.462474, 0.144183], [-1.687036, 5.462474, 0.139964], [-1.691256, 5.462474, 0.144183], [-1.288982, 5.462474, 0.144183]]}, {"shapeName": "R_lowerLidPrimary_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.288982, 5.860529, 0.139964], [-1.284763, 5.860529, 0.144183], [-1.288982, 5.860529, 0.148402], [-1.293201, 5.860529, 0.144183], [-1.288982, 5.860529, 0.139964], [-1.288982, 5.864748, 0.144183], [-1.288982, 5.860529, 0.148402], [-1.288982, 5.856309, 0.144183], [-1.284763, 5.860529, 0.144183], [-1.288982, 5.864748, 0.144183], [-1.293201, 5.860529, 0.144183], [-1.288982, 5.856309, 0.144183], [-1.288982, 5.860529, 0.139964], [-1.288982, 5.864748, 0.144183], [-1.288982, 5.462474, 0.144183]]}, {"shapeName": "R_lowerLidPrimary_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.288982, 5.466694, 0.542237], [-1.284763, 5.462474, 0.542237], [-1.288982, 5.458255, 0.542237], [-1.293201, 5.462474, 0.542237], [-1.288982, 5.466694, 0.542237], [-1.288982, 5.462474, 0.546456], [-1.288982, 5.458255, 0.542237], [-1.288982, 5.462474, 0.538018], [-1.284763, 5.462474, 0.542237], [-1.288982, 5.462474, 0.546456], [-1.293201, 5.462474, 0.542237], [-1.288982, 5.462474, 0.538018], [-1.288982, 5.466694, 0.542237], [-1.288982, 5.462474, 0.546456], [-1.288982, 5.462474, 0.144183]]}]},
			"R_squint_C_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.160662, 2.848625, -0.198918], [-2.141429, 2.877456, -0.214946], [-2.17949, 2.876054, -0.217657], [-2.160662, 2.848625, -0.198918], [-2.144049, 2.875053, -0.176928], [-2.141429, 2.877456, -0.214946], [-2.162876, 2.902482, -0.195667], [-2.144049, 2.875053, -0.176928], [-2.18211, 2.873652, -0.179639], [-2.160662, 2.848625, -0.198918], [-2.17949, 2.876054, -0.217657], [-2.162876, 2.902482, -0.195667], [-2.18211, 2.873652, -0.179639], [-2.17949, 2.876054, -0.217657]]}]},
			"R_lowerLip_A_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lowerLip_A_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.118301, -0.597658, -0.394637], [-1.102629, -0.591166, -0.394637], [-1.086956, -0.597658, -0.394637], [-1.080465, -0.61333, -0.394637], [-1.086956, -0.629002, -0.394637], [-1.102629, -0.635494, -0.394637], [-1.118301, -0.629002, -0.394637], [-1.124792, -0.61333, -0.394637]]}]},
			"L_brow_upper_B_A_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.95643, 8.098141, -1.6288], [0.969228, 8.074366, -1.582035], [1.020977, 8.07218, -1.597308], [1.008179, 8.095955, -1.644073], [0.95643, 8.098141, -1.6288]]}]},
			"C_brow_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_brow_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.031344, 7.844951, -1.064716], [-0.0, 7.853378, -1.074593], [-0.031344, 7.844951, -1.064716], [-0.044328, 7.824604, -1.040873], [-0.031344, 7.804258, -1.01703], [-0.0, 7.795831, -1.007153], [0.031344, 7.804258, -1.01703], [0.044328, 7.824604, -1.040873]]}]},
			"L_lowerLipSecondary_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lowerLipSecondary_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.498937, -0.96602, -0.405488], [1.498937, -0.955169, -0.394637], [1.498937, -0.96602, -0.383786], [1.498937, -0.976871, -0.394637], [1.498937, -0.96602, -0.405488], [1.509787, -0.96602, -0.394637], [1.498937, -0.96602, -0.383786], [1.488086, -0.96602, -0.394637], [1.498937, -0.955169, -0.394637], [1.509787, -0.96602, -0.394637], [1.498937, -0.976871, -0.394637], [1.488086, -0.96602, -0.394637], [1.498937, -0.96602, -0.405488], [1.509787, -0.96602, -0.394637], [0.475266, -0.96602, -0.394637]]}, {"shapeName": "L_lowerLipSecondary_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.475266, 0.057651, -0.405488], [0.464415, 0.057651, -0.394637], [0.475266, 0.057651, -0.383786], [0.486117, 0.057651, -0.394637], [0.475266, 0.057651, -0.405488], [0.475266, 0.068501, -0.394637], [0.475266, 0.057651, -0.383786], [0.475266, 0.0468, -0.394637], [0.464415, 0.057651, -0.394637], [0.475266, 0.068501, -0.394637], [0.486117, 0.057651, -0.394637], [0.475266, 0.0468, -0.394637], [0.475266, 0.057651, -0.405488], [0.475266, 0.068501, -0.394637], [0.475266, -0.96602, -0.394637]]}, {"shapeName": "L_lowerLipSecondary_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.475266, -0.955169, 0.629034], [0.464415, -0.96602, 0.629034], [0.475266, -0.976871, 0.629034], [0.486117, -0.96602, 0.629034], [0.475266, -0.955169, 0.629034], [0.475266, -0.96602, 0.639884], [0.475266, -0.976871, 0.629034], [0.475266, -0.96602, 0.618183], [0.464415, -0.96602, 0.629034], [0.475266, -0.96602, 0.639884], [0.486117, -0.96602, 0.629034], [0.475266, -0.96602, 0.618183], [0.475266, -0.955169, 0.629034], [0.475266, -0.96602, 0.639884], [0.475266, -0.96602, -0.394637]]}]},
			"L_brow_upper_B_D_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.967188, 8.093814, -1.623552], [0.97572, 8.077964, -1.592375], [1.010219, 8.076507, -1.602557], [1.001687, 8.092357, -1.633734], [0.967188, 8.093814, -1.623552]]}]},
			"R_lipCorner_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lipCorner_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.013713, 0.20493, -0.394637], [-2.0, 0.21061, -0.394637], [-1.986287, 0.20493, -0.394637], [-1.980607, 0.191217, -0.394637], [-1.986287, 0.177503, -0.394637], [-2.0, 0.171823, -0.394637], [-2.013713, 0.177503, -0.394637], [-2.019393, 0.191217, -0.394637]]}]},
			"C_upperLip_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_upperLip_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.017631, 1.433848, -0.394637], [0.0, 1.441151, -0.394637], [-0.017631, 1.433848, -0.394637], [-0.024934, 1.416217, -0.394637], [-0.017631, 1.398585, -0.394637], [0.0, 1.391282, -0.394637], [0.017631, 1.398585, -0.394637], [0.024934, 1.416217, -0.394637]]}]},
			"C_noseBase_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_noseBase_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.235084, 5.382292, -1.113724], [0.0, 5.479666, -1.113724], [-0.235084, 5.382292, -1.113724], [-0.332458, 5.147208, -1.113724], [-0.235084, 4.912124, -1.113724], [0.0, 4.81475, -1.113724], [0.235084, 4.912124, -1.113724], [0.332458, 5.147208, -1.113724]]}]},
			"L_upperLid_C_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.674658, 6.359566, 0.144183], [1.674658, 6.353343, 0.144183], [1.680881, 6.353343, 0.144183], [1.680881, 6.359566, 0.144183], [1.674658, 6.359566, 0.144183]]}]},
			"R_lowerLipSecondary_B_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.897651, -0.761362, -0.386637], [-0.897651, -0.761362, -0.402637], [-0.897651, -0.745362, -0.402637], [-0.897651, -0.745362, -0.386637], [-0.913651, -0.745362, -0.386637], [-0.913651, -0.745362, -0.402637], [-0.913651, -0.761362, -0.402637], [-0.913651, -0.761362, -0.386637], [-0.897651, -0.761362, -0.386637], [-0.897651, -0.745362, -0.386637], [-0.897651, -0.745362, -0.402637], [-0.913651, -0.745362, -0.402637], [-0.913651, -0.745362, -0.386637], [-0.913651, -0.761362, -0.386637], [-0.913651, -0.761362, -0.402637], [-0.897651, -0.761362, -0.402637]]}]},
			"L_outterLid_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_outterLid_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.063194, 5.97103, 0.144183], [2.063194, 5.964029, 0.144183], [2.070195, 5.964029, 0.144183], [2.070195, 5.97103, 0.144183], [2.063194, 5.97103, 0.144183]]}]},
			"C_tongue_FK_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_FK_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -1.954719], [0.0, 0.002713, -1.954719], [-0.002713, 0.0, -1.954719], [0.0, -0.002713, -1.954719], [0.002713, 0.0, -1.954719], [0.0, 0.0, -1.952007], [-0.002713, 0.0, -1.954719], [0.0, 0.0, -1.957432], [0.0, 0.002713, -1.954719], [0.0, 0.0, -1.952007], [0.0, -0.002713, -1.954719], [0.0, 0.0, -1.957432], [0.002713, 0.0, -1.954719], [0.0, 0.0, -1.952007], [0.0, 0.0, -2.210637]]}, {"shapeName": "C_tongue_FK_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -2.210637], [0.0, 0.255918, -2.21335], [-0.002713, 0.255918, -2.210637], [0.0, 0.255918, -2.207924], [0.002713, 0.255918, -2.210637], [0.0, 0.25863, -2.210637], [-0.002713, 0.255918, -2.210637], [0.0, 0.253205, -2.210637], [0.0, 0.255918, -2.21335], [0.0, 0.25863, -2.210637], [0.0, 0.255918, -2.207924], [0.0, 0.253205, -2.210637], [0.002713, 0.255918, -2.210637], [0.0, 0.25863, -2.210637], [0.0, 0.0, -2.210637]]}, {"shapeName": "C_tongue_FK_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -2.210637], [-0.255918, 0.0, -2.21335], [-0.255918, -0.002713, -2.210637], [-0.255918, 0.0, -2.207924], [-0.255918, 0.002713, -2.210637], [-0.25863, 0.0, -2.210637], [-0.255918, -0.002713, -2.210637], [-0.253205, 0.0, -2.210637], [-0.255918, 0.0, -2.21335], [-0.25863, 0.0, -2.210637], [-0.255918, 0.0, -2.207924], [-0.253205, 0.0, -2.210637], [-0.255918, 0.002713, -2.210637], [-0.25863, 0.0, -2.210637], [0.0, 0.0, -2.210637]]}]},
			"L_lowerLipSecondary_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lowerLipSecondary_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.929322, -0.753362, -0.405488], [1.929322, -0.742511, -0.394637], [1.929322, -0.753362, -0.383786], [1.929322, -0.764213, -0.394637], [1.929322, -0.753362, -0.405488], [1.940172, -0.753362, -0.394637], [1.929322, -0.753362, -0.383786], [1.918471, -0.753362, -0.394637], [1.929322, -0.742511, -0.394637], [1.940172, -0.753362, -0.394637], [1.929322, -0.764213, -0.394637], [1.918471, -0.753362, -0.394637], [1.929322, -0.753362, -0.405488], [1.940172, -0.753362, -0.394637], [0.905651, -0.753362, -0.394637]]}, {"shapeName": "L_lowerLipSecondary_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.905651, 0.270309, -0.405488], [0.8948, 0.270309, -0.394637], [0.905651, 0.270309, -0.383786], [0.916502, 0.270309, -0.394637], [0.905651, 0.270309, -0.405488], [0.905651, 0.281159, -0.394637], [0.905651, 0.270309, -0.383786], [0.905651, 0.259458, -0.394637], [0.8948, 0.270309, -0.394637], [0.905651, 0.281159, -0.394637], [0.916502, 0.270309, -0.394637], [0.905651, 0.259458, -0.394637], [0.905651, 0.270309, -0.405488], [0.905651, 0.281159, -0.394637], [0.905651, -0.753362, -0.394637]]}, {"shapeName": "L_lowerLipSecondary_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.905651, -0.742511, 0.629034], [0.8948, -0.753362, 0.629034], [0.905651, -0.764213, 0.629034], [0.916502, -0.753362, 0.629034], [0.905651, -0.742511, 0.629034], [0.905651, -0.753362, 0.639884], [0.905651, -0.764213, 0.629034], [0.905651, -0.753362, 0.618183], [0.8948, -0.753362, 0.629034], [0.905651, -0.753362, 0.639884], [0.916502, -0.753362, 0.629034], [0.905651, -0.753362, 0.618183], [0.905651, -0.742511, 0.629034], [0.905651, -0.753362, 0.639884], [0.905651, -0.753362, -0.394637]]}]},
			"L_outterLid_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_outterLid_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.063583, 5.970641, 0.144183], [2.063583, 5.964418, 0.144183], [2.069806, 5.964418, 0.144183], [2.069806, 5.970641, 0.144183], [2.063583, 5.970641, 0.144183]]}]},
			"L_lowerLid_C_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.675436, 5.580938, 0.144183], [1.675436, 5.576271, 0.144183], [1.680103, 5.576271, 0.144183], [1.680103, 5.580938, 0.144183], [1.675436, 5.580938, 0.144183]]}]},
			"C_brow_upper_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_brow_upper_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.021, 8.098877, -1.458387], [-0.021, 8.080008, -1.420864], [0.021, 8.080008, -1.420864], [0.021, 8.098877, -1.458387], [-0.021, 8.098877, -1.458387]]}]},
			"R_brow_A_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_A_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-0.644357, 7.850297, -1.13566], [-0.612023, 7.85941, -1.140399], [-0.582511, 7.851749, -1.125518], [-0.573111, 7.831801, -1.099735], [-0.589328, 7.811253, -1.078153], [-0.621663, 7.80214, -1.073414], [-0.651174, 7.809801, -1.088294], [-0.660574, 7.829749, -1.114077]]}]},
			"C_lowerLip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_lowerLip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, -1.033783, -0.405488], [1.023671, -1.022932, -0.394637], [1.023671, -1.033783, -0.383786], [1.023671, -1.044634, -0.394637], [1.023671, -1.033783, -0.405488], [1.034521, -1.033783, -0.394637], [1.023671, -1.033783, -0.383786], [1.01282, -1.033783, -0.394637], [1.023671, -1.022932, -0.394637], [1.034521, -1.033783, -0.394637], [1.023671, -1.044634, -0.394637], [1.01282, -1.033783, -0.394637], [1.023671, -1.033783, -0.405488], [1.034521, -1.033783, -0.394637], [0.0, -1.033783, -0.394637]]}, {"shapeName": "C_lowerLip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, -0.010112, -0.405488], [-0.010851, -0.010112, -0.394637], [0.0, -0.010112, -0.383786], [0.010851, -0.010112, -0.394637], [0.0, -0.010112, -0.405488], [0.0, 0.000738, -0.394637], [0.0, -0.010112, -0.383786], [0.0, -0.020963, -0.394637], [-0.010851, -0.010112, -0.394637], [0.0, 0.000738, -0.394637], [0.010851, -0.010112, -0.394637], [0.0, -0.020963, -0.394637], [0.0, -0.010112, -0.405488], [0.0, 0.000738, -0.394637], [0.0, -1.033783, -0.394637]]}, {"shapeName": "C_lowerLip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, -1.022932, 0.629034], [-0.010851, -1.033783, 0.629034], [0.0, -1.044634, 0.629034], [0.010851, -1.033783, 0.629034], [0.0, -1.022932, 0.629034], [0.0, -1.033783, 0.639884], [0.0, -1.044634, 0.629034], [0.0, -1.033783, 0.618183], [-0.010851, -1.033783, 0.629034], [0.0, -1.033783, 0.639884], [0.010851, -1.033783, 0.629034], [0.0, -1.033783, 0.618183], [0.0, -1.022932, 0.629034], [0.0, -1.033783, 0.639884], [0.0, -1.033783, -0.394637]]}]},
			"C_upperLip_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_upperLip_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 1.416217, -0.405488], [1.023671, 1.427068, -0.394637], [1.023671, 1.416217, -0.383786], [1.023671, 1.405366, -0.394637], [1.023671, 1.416217, -0.405488], [1.034521, 1.416217, -0.394637], [1.023671, 1.416217, -0.383786], [1.01282, 1.416217, -0.394637], [1.023671, 1.427068, -0.394637], [1.034521, 1.416217, -0.394637], [1.023671, 1.405366, -0.394637], [1.01282, 1.416217, -0.394637], [1.023671, 1.416217, -0.405488], [1.034521, 1.416217, -0.394637], [0.0, 1.416217, -0.394637]]}, {"shapeName": "C_upperLip_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 2.439888, -0.405488], [-0.010851, 2.439888, -0.394637], [0.0, 2.439888, -0.383786], [0.010851, 2.439888, -0.394637], [0.0, 2.439888, -0.405488], [0.0, 2.450738, -0.394637], [0.0, 2.439888, -0.383786], [0.0, 2.429037, -0.394637], [-0.010851, 2.439888, -0.394637], [0.0, 2.450738, -0.394637], [0.010851, 2.439888, -0.394637], [0.0, 2.429037, -0.394637], [0.0, 2.439888, -0.405488], [0.0, 2.450738, -0.394637], [0.0, 1.416217, -0.394637]]}, {"shapeName": "C_upperLip_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 1.427068, 0.629034], [-0.010851, 1.416217, 0.629034], [0.0, 1.405366, 0.629034], [0.010851, 1.416217, 0.629034], [0.0, 1.427068, 0.629034], [0.0, 1.416217, 0.639884], [0.0, 1.405366, 0.629034], [0.0, 1.416217, 0.618183], [-0.010851, 1.416217, 0.629034], [0.0, 1.416217, 0.639884], [0.010851, 1.416217, 0.629034], [0.0, 1.416217, 0.618183], [0.0, 1.427068, 0.629034], [0.0, 1.416217, 0.639884], [0.0, 1.416217, -0.394637]]}]},
			"R_lookAt_C_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "R_lookAt_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.137132, 6.137132, 2.5], [-2.0, 6.193934, 2.5], [-1.862868, 6.137132, 2.5], [-1.806066, 6.0, 2.5], [-1.862868, 5.862868, 2.5], [-2.0, 5.806066, 2.5], [-2.137132, 5.862868, 2.5], [-2.193934, 6.0, 2.5]]}]},
			"R_lipCornerSecondary_CTL": {"color": 20, "shapes": [{"shapeName": "R_lipCornerSecondary_CTLShape", "degree": 1, "form": 0, "points": [[-1.99, 0.181217, -0.384637], [-1.99, 0.181217, -0.404637], [-1.99, 0.201217, -0.404637], [-1.99, 0.201217, -0.384637], [-2.01, 0.201217, -0.384637], [-2.01, 0.201217, -0.404637], [-2.01, 0.181217, -0.404637], [-2.01, 0.181217, -0.384637], [-1.99, 0.181217, -0.384637], [-1.99, 0.201217, -0.384637], [-1.99, 0.201217, -0.404637], [-2.01, 0.201217, -0.404637], [-2.01, 0.201217, -0.384637], [-2.01, 0.181217, -0.384637], [-2.01, 0.181217, -0.404637], [-1.99, 0.181217, -0.404637]]}]},
			"C_lookAt_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lookAt_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.448262, 6.028103, 3.064629], [-0.448262, 5.971897, 3.064629], [-0.448262, 5.971897, 3.008422], [-0.448262, 6.028103, 3.008422], [-0.448262, 6.028103, 3.064629], [0.448262, 6.028103, 3.064629], [0.448262, 5.971897, 3.064629], [0.448262, 5.971897, 3.008422], [0.448262, 6.028103, 3.008422], [0.448262, 6.028103, 3.064629], [0.448262, 5.971897, 3.064629], [-0.448262, 5.971897, 3.064629], [-0.448262, 5.971897, 3.008422], [0.448262, 5.971897, 3.008422], [0.448262, 6.028103, 3.008422], [-0.448262, 6.028103, 3.008422], [-0.448262, 6.028103, 3.064629], [-0.0279, 6.0279, 3.064426], [-0.028103, 5.551738, 3.064629], [-0.028103, 5.551738, 3.008422], [0.028103, 5.551738, 3.008422], [0.028103, 5.551738, 3.064629], [-0.028103, 5.551738, 3.064629], [-0.028103, 6.448262, 3.064629], [0.028103, 6.448262, 3.064629], [0.028103, 6.448262, 3.008422], [-0.028103, 6.448262, 3.008422], [-0.028103, 6.448262, 3.064629], [-0.028103, 6.448262, 3.008422], [-0.028103, 5.551738, 3.008422], [0.028103, 5.551738, 3.008422], [0.028103, 6.448262, 3.008422], [0.028103, 6.448262, 3.064629], [0.028103, 5.551738, 3.064629], [0.0279, 5.9721, 3.064426], [0.028103, 5.971897, 3.484788], [-0.028103, 5.971897, 3.484788], [-0.028103, 6.028103, 3.484788], [0.028103, 6.028103, 3.484788], [0.028103, 5.971897, 3.484788], [0.028103, 5.971897, 2.588264], [0.028103, 6.028103, 2.588264], [-0.028103, 6.028103, 2.588264], [-0.028103, 5.971897, 2.588264], [0.028103, 5.971897, 2.588264], [-0.028103, 5.971897, 2.588264], [-0.028103, 5.971897, 3.484788], [-0.028103, 6.028103, 3.484788], [-0.028103, 6.028103, 2.588264], [0.028103, 6.028103, 2.588264], [0.028103, 6.028103, 3.484788]]}]},
			"L_squint_B_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.986786, 2.841453, -0.013214], [1.971133, 2.867181, -0.028867], [2.005026, 2.865386, -0.028915], [1.986786, 2.841453, -0.013214], [1.971085, 2.865386, 0.005026], [1.971133, 2.867181, -0.028867], [1.989325, 2.889319, -0.010675], [1.971085, 2.865386, 0.005026], [2.004979, 2.863591, 0.004979], [1.986786, 2.841453, -0.013214], [2.005026, 2.865386, -0.028915], [1.989325, 2.889319, -0.010675], [2.004979, 2.863591, 0.004979], [2.005026, 2.865386, -0.028915]]}]},
			"L_squint_A_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.805503, 2.836008, 0.155295], [1.793128, 2.858597, 0.14051], [1.82269, 2.856561, 0.142481], [1.805503, 2.836008, 0.155295], [1.791065, 2.857318, 0.170109], [1.793128, 2.858597, 0.14051], [1.808253, 2.87787, 0.157296], [1.791065, 2.857318, 0.170109], [1.820628, 2.855282, 0.172081], [1.805503, 2.836008, 0.155295], [1.82269, 2.856561, 0.142481], [1.808253, 2.87787, 0.157296], [1.820628, 2.855282, 0.172081], [1.82269, 2.856561, 0.142481]]}]},
			"R_upperLipSecondary_A_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.466266, 1.339453, -0.385637], [-0.466266, 1.339453, -0.403637], [-0.466266, 1.357453, -0.403637], [-0.466266, 1.357453, -0.385637], [-0.484266, 1.357453, -0.385637], [-0.484266, 1.357453, -0.403637], [-0.484266, 1.339453, -0.403637], [-0.484266, 1.339453, -0.385637], [-0.466266, 1.339453, -0.385637], [-0.466266, 1.357453, -0.385637], [-0.466266, 1.357453, -0.403637], [-0.484266, 1.357453, -0.403637], [-0.484266, 1.357453, -0.385637], [-0.484266, 1.339453, -0.385637], [-0.484266, 1.339453, -0.403637], [-0.466266, 1.339453, -0.403637]]}]},
			"L_upperLipSecondary_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upperLipSecondary_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.676364, 0.52694, -0.405488], [2.676364, 0.537791, -0.394637], [2.676364, 0.52694, -0.383786], [2.676364, 0.516089, -0.394637], [2.676364, 0.52694, -0.405488], [2.687214, 0.52694, -0.394637], [2.676364, 0.52694, -0.383786], [2.665513, 0.52694, -0.394637], [2.676364, 0.537791, -0.394637], [2.687214, 0.52694, -0.394637], [2.676364, 0.516089, -0.394637], [2.665513, 0.52694, -0.394637], [2.676364, 0.52694, -0.405488], [2.687214, 0.52694, -0.394637], [1.652693, 0.52694, -0.394637]]}, {"shapeName": "L_upperLipSecondary_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.652693, 1.550611, -0.405488], [1.641842, 1.550611, -0.394637], [1.652693, 1.550611, -0.383786], [1.663544, 1.550611, -0.394637], [1.652693, 1.550611, -0.405488], [1.652693, 1.561461, -0.394637], [1.652693, 1.550611, -0.383786], [1.652693, 1.53976, -0.394637], [1.641842, 1.550611, -0.394637], [1.652693, 1.561461, -0.394637], [1.663544, 1.550611, -0.394637], [1.652693, 1.53976, -0.394637], [1.652693, 1.550611, -0.405488], [1.652693, 1.561461, -0.394637], [1.652693, 0.52694, -0.394637]]}, {"shapeName": "L_upperLipSecondary_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.652693, 0.537791, 0.629034], [1.641842, 0.52694, 0.629034], [1.652693, 0.516089, 0.629034], [1.663544, 0.52694, 0.629034], [1.652693, 0.537791, 0.629034], [1.652693, 0.52694, 0.639884], [1.652693, 0.516089, 0.629034], [1.652693, 0.52694, 0.618183], [1.641842, 0.52694, 0.629034], [1.652693, 0.52694, 0.639884], [1.663544, 0.52694, 0.629034], [1.652693, 0.52694, 0.618183], [1.652693, 0.537791, 0.629034], [1.652693, 0.52694, 0.639884], [1.652693, 0.52694, -0.394637]]}]},
			"R_lowerLipSecondary_B_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.896651, -0.762362, -0.385637], [-0.896651, -0.762362, -0.403637], [-0.896651, -0.744362, -0.403637], [-0.896651, -0.744362, -0.385637], [-0.914651, -0.744362, -0.385637], [-0.914651, -0.744362, -0.403637], [-0.914651, -0.762362, -0.403637], [-0.914651, -0.762362, -0.385637], [-0.896651, -0.762362, -0.385637], [-0.896651, -0.744362, -0.385637], [-0.896651, -0.744362, -0.403637], [-0.914651, -0.744362, -0.403637], [-0.914651, -0.744362, -0.385637], [-0.914651, -0.762362, -0.385637], [-0.914651, -0.762362, -0.403637], [-0.896651, -0.762362, -0.403637]]}]},
			"L_upperLid_A_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.896808, 6.359566, 0.144183], [0.896808, 6.353343, 0.144183], [0.903031, 6.353343, 0.144183], [0.903031, 6.359566, 0.144183], [0.896808, 6.359566, 0.144183]]}]},
			"C_tongue_IK_A_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_A_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.088156, -0.088156, -3.157066], [0.124672, 0.0, -3.157066], [0.088156, 0.088156, -3.157066], [0.0, 0.124672, -3.157066], [-0.088156, 0.088156, -3.157066], [-0.124672, 0.0, -3.157066], [-0.088156, -0.088156, -3.157066], [0.0, -0.124672, -3.157066]]}]},
			"L_upperLidPrimary_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLidPrimary_CTLShape", "degree": 3, "form": 2, "points": [[1.288845, 6.481752, 0.151961], [1.282749, 6.479227, 0.151961], [1.280225, 6.473132, 0.151961], [1.282749, 6.467036, 0.151961], [1.288845, 6.464512, 0.151961], [1.29494, 6.467036, 0.151961], [1.297465, 6.473132, 0.151961], [1.29494, 6.479227, 0.151961]]}]},
			"C_brow_upper_CTL": {"color": 20, "shapes": [{"shapeName": "C_brow_upper_CTLShape", "degree": 1, "form": 0, "points": [[-0.042426, 8.268123, -1.349774], [-0.0, 8.249063, -1.31187], [0.042426, 8.268123, -1.349774], [-0.0, 8.287183, -1.387678], [-0.042426, 8.268123, -1.349774]]}]},
			"R_lipCorner_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lipCorner_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.015672, 0.206889, -0.394637], [-2.0, 0.21338, -0.394637], [-1.984328, 0.206889, -0.394637], [-1.977836, 0.191217, -0.394637], [-1.984328, 0.175544, -0.394637], [-2.0, 0.169053, -0.394637], [-2.015672, 0.175544, -0.394637], [-2.022164, 0.191217, -0.394637]]}]},
			"R_lowerLipSecondary_C_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.284093, -0.470611, -0.387637], [-1.284093, -0.470611, -0.401637], [-1.284093, -0.456611, -0.401637], [-1.284093, -0.456611, -0.387637], [-1.298093, -0.456611, -0.387637], [-1.298093, -0.456611, -0.401637], [-1.298093, -0.470611, -0.401637], [-1.298093, -0.470611, -0.387637], [-1.284093, -0.470611, -0.387637], [-1.284093, -0.456611, -0.387637], [-1.284093, -0.456611, -0.401637], [-1.298093, -0.456611, -0.401637], [-1.298093, -0.456611, -0.387637], [-1.298093, -0.470611, -0.387637], [-1.298093, -0.470611, -0.401637], [-1.284093, -0.470611, -0.401637]]}]},
			"L_upperLipSecondary_A_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.468266, 1.341453, -0.387637], [0.468266, 1.341453, -0.401637], [0.468266, 1.355453, -0.401637], [0.468266, 1.355453, -0.387637], [0.482266, 1.355453, -0.387637], [0.482266, 1.355453, -0.401637], [0.482266, 1.341453, -0.401637], [0.482266, 1.341453, -0.387637], [0.468266, 1.341453, -0.387637], [0.468266, 1.355453, -0.387637], [0.468266, 1.355453, -0.401637], [0.482266, 1.355453, -0.401637], [0.482266, 1.355453, -0.387637], [0.482266, 1.341453, -0.387637], [0.482266, 1.341453, -0.401637], [0.468266, 1.341453, -0.401637]]}]},
			"L_lipCorner_CTL": {"color": 17, "shapes": [{"shapeName": "L_lipCorner_CTLShape", "degree": 3, "form": 2, "points": [[2.01959, 0.210807, -0.394637], [2.0, 0.218921, -0.394637], [1.98041, 0.210807, -0.394637], [1.972295, 0.191217, -0.394637], [1.98041, 0.171626, -0.394637], [2.0, 0.163512, -0.394637], [2.01959, 0.171626, -0.394637], [2.027705, 0.191217, -0.394637]]}]},
			"L_upperLip_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upperLip_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.1263, 0.995763, -0.405488], [2.1263, 1.006614, -0.394637], [2.1263, 0.995763, -0.383786], [2.1263, 0.984912, -0.394637], [2.1263, 0.995763, -0.405488], [2.13715, 0.995763, -0.394637], [2.1263, 0.995763, -0.383786], [2.115449, 0.995763, -0.394637], [2.1263, 1.006614, -0.394637], [2.13715, 0.995763, -0.394637], [2.1263, 0.984912, -0.394637], [2.115449, 0.995763, -0.394637], [2.1263, 0.995763, -0.405488], [2.13715, 0.995763, -0.394637], [1.102629, 0.995763, -0.394637]]}, {"shapeName": "L_upperLip_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.102629, 2.019434, -0.405488], [1.091778, 2.019434, -0.394637], [1.102629, 2.019434, -0.383786], [1.11348, 2.019434, -0.394637], [1.102629, 2.019434, -0.405488], [1.102629, 2.030284, -0.394637], [1.102629, 2.019434, -0.383786], [1.102629, 2.008583, -0.394637], [1.091778, 2.019434, -0.394637], [1.102629, 2.030284, -0.394637], [1.11348, 2.019434, -0.394637], [1.102629, 2.008583, -0.394637], [1.102629, 2.019434, -0.405488], [1.102629, 2.030284, -0.394637], [1.102629, 0.995763, -0.394637]]}, {"shapeName": "L_upperLip_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.102629, 1.006614, 0.629034], [1.091778, 0.995763, 0.629034], [1.102629, 0.984912, 0.629034], [1.11348, 0.995763, 0.629034], [1.102629, 1.006614, 0.629034], [1.102629, 0.995763, 0.639884], [1.102629, 0.984912, 0.629034], [1.102629, 0.995763, 0.618183], [1.091778, 0.995763, 0.629034], [1.102629, 0.995763, 0.639884], [1.11348, 0.995763, 0.629034], [1.102629, 0.995763, 0.618183], [1.102629, 1.006614, 0.629034], [1.102629, 0.995763, 0.639884], [1.102629, 0.995763, -0.394637]]}]},
			"R_lowerLid_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lowerLid_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.687036, 5.462474, 0.139964], [-1.687036, 5.466694, 0.144183], [-1.687036, 5.462474, 0.148402], [-1.687036, 5.458255, 0.144183], [-1.687036, 5.462474, 0.139964], [-1.691256, 5.462474, 0.144183], [-1.687036, 5.462474, 0.148402], [-1.682817, 5.462474, 0.144183], [-1.687036, 5.466694, 0.144183], [-1.691256, 5.462474, 0.144183], [-1.687036, 5.458255, 0.144183], [-1.682817, 5.462474, 0.144183], [-1.687036, 5.462474, 0.139964], [-1.691256, 5.462474, 0.144183], [-1.288982, 5.462474, 0.144183]]}, {"shapeName": "R_lowerLid_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.288982, 5.860529, 0.139964], [-1.284763, 5.860529, 0.144183], [-1.288982, 5.860529, 0.148402], [-1.293201, 5.860529, 0.144183], [-1.288982, 5.860529, 0.139964], [-1.288982, 5.864748, 0.144183], [-1.288982, 5.860529, 0.148402], [-1.288982, 5.856309, 0.144183], [-1.284763, 5.860529, 0.144183], [-1.288982, 5.864748, 0.144183], [-1.293201, 5.860529, 0.144183], [-1.288982, 5.856309, 0.144183], [-1.288982, 5.860529, 0.139964], [-1.288982, 5.864748, 0.144183], [-1.288982, 5.462474, 0.144183]]}, {"shapeName": "R_lowerLid_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.288982, 5.466694, 0.542237], [-1.284763, 5.462474, 0.542237], [-1.288982, 5.458255, 0.542237], [-1.293201, 5.462474, 0.542237], [-1.288982, 5.466694, 0.542237], [-1.288982, 5.462474, 0.546456], [-1.288982, 5.458255, 0.542237], [-1.288982, 5.462474, 0.538018], [-1.284763, 5.462474, 0.542237], [-1.288982, 5.462474, 0.546456], [-1.293201, 5.462474, 0.542237], [-1.288982, 5.462474, 0.538018], [-1.288982, 5.466694, 0.542237], [-1.288982, 5.462474, 0.546456], [-1.288982, 5.462474, 0.144183]]}]},
			"R_cheek_C_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_C_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.162516, 2.650554, -0.238523], [-2.145802, 2.661247, -0.216442], [-2.126509, 2.649539, -0.197155], [-2.115938, 2.622289, -0.191962], [-2.120281, 2.59546, -0.203904], [-2.136995, 2.584768, -0.225985], [-2.156289, 2.596476, -0.245271], [-2.16686, 2.623725, -0.250465]]}]},
			"C_mouthAll_CTL": {"color": 18, "shapes": [{"shapeName": "C_mouthAll_CTLShape", "degree": 3, "form": 2, "points": [[0.058771, 0.230397, 2.055363], [0.0, 0.246626, 2.055363], [-0.058771, 0.230397, 2.055363], [-0.083115, 0.191217, 2.055363], [-0.058771, 0.152036, 2.055363], [0.0, 0.135807, 2.055363], [0.058771, 0.152036, 2.055363], [0.083115, 0.191217, 2.055363]]}]},
			"R_cheek_C_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_C_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.159499, 2.646619, -0.23605], [-2.145173, 2.655784, -0.217123], [-2.128636, 2.645749, -0.200592], [-2.119575, 2.622392, -0.196141], [-2.123298, 2.599395, -0.206376], [-2.137624, 2.590231, -0.225303], [-2.154161, 2.600266, -0.241834], [-2.163222, 2.623623, -0.246286]]}]},
			"R_lowerLip_A_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lowerLip_A_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.114383, -0.601576, -0.394637], [-1.102629, -0.596707, -0.394637], [-1.090874, -0.601576, -0.394637], [-1.086006, -0.61333, -0.394637], [-1.090874, -0.625084, -0.394637], [-1.102629, -0.629953, -0.394637], [-1.114383, -0.625084, -0.394637], [-1.119251, -0.61333, -0.394637]]}]},
			"L_lowerLid_B_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.286511, 5.46426, 0.144183], [1.286511, 5.459593, 0.144183], [1.291178, 5.459593, 0.144183], [1.291178, 5.46426, 0.144183], [1.286511, 5.46426, 0.144183]]}]},
			"L_upperLip_A_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_upperLip_A_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.12026, 1.013394, -0.394637], [1.102629, 1.020698, -0.394637], [1.084997, 1.013394, -0.394637], [1.077694, 0.995763, -0.394637], [1.084997, 0.978132, -0.394637], [1.102629, 0.970829, -0.394637], [1.12026, 0.978132, -0.394637], [1.127563, 0.995763, -0.394637]]}]},
			"L_cheek_C_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_C_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.159499, 2.646619, -0.23605], [2.145173, 2.655784, -0.217123], [2.128636, 2.645749, -0.200592], [2.119575, 2.622392, -0.196141], [2.123298, 2.599395, -0.206376], [2.137624, 2.590231, -0.225303], [2.154161, 2.600266, -0.241834], [2.163222, 2.623623, -0.246286]]}]},
			"C_tongue_FK_G_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_FK_G_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -0.883291], [0.0, 0.002713, -0.883291], [-0.002713, 0.0, -0.883291], [0.0, -0.002713, -0.883291], [0.002713, 0.0, -0.883291], [0.0, 0.0, -0.880578], [-0.002713, 0.0, -0.883291], [0.0, 0.0, -0.886003], [0.0, 0.002713, -0.883291], [0.0, 0.0, -0.880578], [0.0, -0.002713, -0.883291], [0.0, 0.0, -0.886003], [0.002713, 0.0, -0.883291], [0.0, 0.0, -0.880578], [0.0, 0.0, -1.139208]]}, {"shapeName": "C_tongue_FK_G_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -1.139208], [0.0, 0.255918, -1.141921], [-0.002713, 0.255918, -1.139208], [0.0, 0.255918, -1.136496], [0.002713, 0.255918, -1.139208], [0.0, 0.25863, -1.139208], [-0.002713, 0.255918, -1.139208], [0.0, 0.253205, -1.139208], [0.0, 0.255918, -1.141921], [0.0, 0.25863, -1.139208], [0.0, 0.255918, -1.136496], [0.0, 0.253205, -1.139208], [0.002713, 0.255918, -1.139208], [0.0, 0.25863, -1.139208], [0.0, 0.0, -1.139208]]}, {"shapeName": "C_tongue_FK_G_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -1.139208], [-0.255918, 0.0, -1.141921], [-0.255918, -0.002713, -1.139208], [-0.255918, 0.0, -1.136496], [-0.255918, 0.002713, -1.139208], [-0.25863, 0.0, -1.139208], [-0.255918, -0.002713, -1.139208], [-0.253205, 0.0, -1.139208], [-0.255918, 0.0, -1.141921], [-0.25863, 0.0, -1.139208], [-0.255918, 0.0, -1.136496], [-0.253205, 0.0, -1.139208], [-0.255918, 0.002713, -1.139208], [-0.25863, 0.0, -1.139208], [0.0, 0.0, -1.139208]]}]},
			"C_noseBridge_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_noseBridge_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.117542, 5.86475, -1.313724], [0.0, 5.913437, -1.313724], [-0.117542, 5.86475, -1.313724], [-0.166229, 5.747208, -1.313724], [-0.117542, 5.629666, -1.313724], [0.0, 5.580979, -1.313724], [0.117542, 5.629666, -1.313724], [0.166229, 5.747208, -1.313724]]}]},
			"R_brow_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.625428, 7.798795, -1.279396], [-1.625572, 7.814084, -1.280707], [-1.628076, 7.815354, -1.26562], [-1.627932, 7.800065, -1.264309], [-1.625428, 7.798795, -1.279396], [-1.637456, 7.806824, -1.274263], [-1.628076, 7.815354, -1.26562], [-1.616047, 7.807326, -1.270752], [-1.625572, 7.814084, -1.280707], [-1.637456, 7.806824, -1.274263], [-1.627932, 7.800065, -1.264309], [-1.616047, 7.807326, -1.270752], [-1.625428, 7.798795, -1.279396], [-1.637456, 7.806824, -1.274263], [-0.616843, 7.830775, -1.106906]]}, {"shapeName": "R_brow_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.504209, 8.483768, -1.887249], [-0.494827, 8.492298, -1.878605], [-0.506856, 8.500326, -1.873473], [-0.516238, 8.491796, -1.882116], [-0.504209, 8.483768, -1.887249], [-0.504353, 8.499056, -1.888559], [-0.506856, 8.500326, -1.873473], [-0.506712, 8.485037, -1.872162], [-0.494827, 8.492298, -1.878605], [-0.504353, 8.499056, -1.888559], [-0.516238, 8.491796, -1.882116], [-0.506712, 8.485037, -1.872162], [-0.504209, 8.483768, -1.887249], [-0.504353, 8.499056, -1.888559], [-0.616843, 7.830775, -1.106906]]}, {"shapeName": "R_brow_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.740545, 8.618848, -0.4653], [-0.73102, 8.61209, -0.455346], [-0.742905, 8.604829, -0.448902], [-0.75243, 8.611587, -0.458857], [-0.740545, 8.618848, -0.4653], [-0.743049, 8.620117, -0.450214], [-0.742905, 8.604829, -0.448902], [-0.740401, 8.603559, -0.463989], [-0.73102, 8.61209, -0.455346], [-0.743049, 8.620117, -0.450214], [-0.75243, 8.611587, -0.458857], [-0.740401, 8.603559, -0.463989], [-0.740545, 8.618848, -0.4653], [-0.743049, 8.620117, -0.450214], [-0.616843, 7.830775, -1.106906]]}]},
			"R_brow_B_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_B_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.214626, 7.834108, -1.288122], [-1.1903, 7.841557, -1.287603], [-1.170175, 7.836279, -1.272955], [-1.166039, 7.821366, -1.252757], [-1.180315, 7.805554, -1.238841], [-1.20464, 7.798105, -1.239359], [-1.224765, 7.803383, -1.254008], [-1.228901, 7.818296, -1.274206]]}]},
			"C_noseBridge_CTL": {"color": 17, "shapes": [{"shapeName": "C_noseBridge_CTLShape", "degree": 3, "form": 2, "points": [[0.195903, 5.943111, -1.313724], [0.0, 6.024257, -1.313724], [-0.195903, 5.943111, -1.313724], [-0.277048, 5.747208, -1.313724], [-0.195903, 5.551305, -1.313724], [0.0, 5.47016, -1.313724], [0.195903, 5.551305, -1.313724], [0.277048, 5.747208, -1.313724]]}]},
			"L_upperLid_B_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_B_CTLShape", "degree": 1, "form": 0, "points": [[1.283345, 6.473132, 0.151961], [1.288845, 6.467631, 0.151961], [1.294345, 6.473132, 0.151961], [1.288845, 6.478632, 0.151961], [1.283345, 6.473132, 0.151961]]}]},
			"L_brow_C_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_C_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.696423, 7.81494, -1.515097], [1.664817, 7.825752, -1.509162], [1.64121, 7.819147, -1.485707], [1.63943, 7.798993, -1.458473], [1.66052, 7.777097, -1.443412], [1.692126, 7.766286, -1.449347], [1.715733, 7.772891, -1.472802], [1.717513, 7.793045, -1.500036]]}]},
			"L_lowerLipSecondary_A_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.468266, -0.97302, -0.387637], [0.468266, -0.97302, -0.401637], [0.468266, -0.95902, -0.401637], [0.468266, -0.95902, -0.387637], [0.482266, -0.95902, -0.387637], [0.482266, -0.95902, -0.401637], [0.482266, -0.97302, -0.401637], [0.482266, -0.97302, -0.387637], [0.468266, -0.97302, -0.387637], [0.468266, -0.95902, -0.387637], [0.468266, -0.95902, -0.401637], [0.482266, -0.95902, -0.401637], [0.482266, -0.95902, -0.387637], [0.482266, -0.97302, -0.387637], [0.482266, -0.97302, -0.401637], [0.468266, -0.97302, -0.401637]]}]},
			"R_lipCorner_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lipCorner_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-3.023671, 0.191217, -0.405488], [-3.023671, 0.202068, -0.394637], [-3.023671, 0.191217, -0.383786], [-3.023671, 0.180366, -0.394637], [-3.023671, 0.191217, -0.405488], [-3.034521, 0.191217, -0.394637], [-3.023671, 0.191217, -0.383786], [-3.01282, 0.191217, -0.394637], [-3.023671, 0.202068, -0.394637], [-3.034521, 0.191217, -0.394637], [-3.023671, 0.180366, -0.394637], [-3.01282, 0.191217, -0.394637], [-3.023671, 0.191217, -0.405488], [-3.034521, 0.191217, -0.394637], [-2.0, 0.191217, -0.394637]]}, {"shapeName": "R_lipCorner_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-2.0, 1.214888, -0.405488], [-1.989149, 1.214888, -0.394637], [-2.0, 1.214888, -0.383786], [-2.010851, 1.214888, -0.394637], [-2.0, 1.214888, -0.405488], [-2.0, 1.225738, -0.394637], [-2.0, 1.214888, -0.383786], [-2.0, 1.204037, -0.394637], [-1.989149, 1.214888, -0.394637], [-2.0, 1.225738, -0.394637], [-2.010851, 1.214888, -0.394637], [-2.0, 1.204037, -0.394637], [-2.0, 1.214888, -0.405488], [-2.0, 1.225738, -0.394637], [-2.0, 0.191217, -0.394637]]}, {"shapeName": "R_lipCorner_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.0, 0.202068, 0.629034], [-1.989149, 0.191217, 0.629034], [-2.0, 0.180366, 0.629034], [-2.010851, 0.191217, 0.629034], [-2.0, 0.202068, 0.629034], [-2.0, 0.191217, 0.639884], [-2.0, 0.180366, 0.629034], [-2.0, 0.191217, 0.618183], [-1.989149, 0.191217, 0.629034], [-2.0, 0.191217, 0.639884], [-2.010851, 0.191217, 0.629034], [-2.0, 0.191217, 0.618183], [-2.0, 0.202068, 0.629034], [-2.0, 0.191217, 0.639884], [-2.0, 0.191217, -0.394637]]}]},
			"L_lowerLid_C_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_C_CTLShape", "degree": 1, "form": 0, "points": [[1.67227, 5.578604, 0.151961], [1.67777, 5.573104, 0.151961], [1.68327, 5.578604, 0.151961], [1.67777, 5.584104, 0.151961], [1.67227, 5.578604, 0.151961]]}]},
			"L_brow_A_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_A_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.647797, 7.852738, -1.139254], [0.61142, 7.862989, -1.144586], [0.57822, 7.85437, -1.127845], [0.567644, 7.83193, -1.098839], [0.585888, 7.808812, -1.074558], [0.622265, 7.798561, -1.069227], [0.655465, 7.80718, -1.085967], [0.666041, 7.82962, -1.114974]]}]},
			"R_upperLipSecondary_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upperLipSecondary_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.314764, 0.846044, -0.405488], [-2.314764, 0.856895, -0.394637], [-2.314764, 0.846044, -0.383786], [-2.314764, 0.835193, -0.394637], [-2.314764, 0.846044, -0.405488], [-2.325614, 0.846044, -0.394637], [-2.314764, 0.846044, -0.383786], [-2.303913, 0.846044, -0.394637], [-2.314764, 0.856895, -0.394637], [-2.325614, 0.846044, -0.394637], [-2.314764, 0.835193, -0.394637], [-2.303913, 0.846044, -0.394637], [-2.314764, 0.846044, -0.405488], [-2.325614, 0.846044, -0.394637], [-1.291093, 0.846044, -0.394637]]}, {"shapeName": "R_upperLipSecondary_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.291093, 1.869715, -0.405488], [-1.280242, 1.869715, -0.394637], [-1.291093, 1.869715, -0.383786], [-1.301944, 1.869715, -0.394637], [-1.291093, 1.869715, -0.405488], [-1.291093, 1.880565, -0.394637], [-1.291093, 1.869715, -0.383786], [-1.291093, 1.858864, -0.394637], [-1.280242, 1.869715, -0.394637], [-1.291093, 1.880565, -0.394637], [-1.301944, 1.869715, -0.394637], [-1.291093, 1.858864, -0.394637], [-1.291093, 1.869715, -0.405488], [-1.291093, 1.880565, -0.394637], [-1.291093, 0.846044, -0.394637]]}, {"shapeName": "R_upperLipSecondary_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.291093, 0.856895, 0.629034], [-1.280242, 0.846044, 0.629034], [-1.291093, 0.835193, 0.629034], [-1.301944, 0.846044, 0.629034], [-1.291093, 0.856895, 0.629034], [-1.291093, 0.846044, 0.639884], [-1.291093, 0.835193, 0.629034], [-1.291093, 0.846044, 0.618183], [-1.280242, 0.846044, 0.629034], [-1.291093, 0.846044, 0.639884], [-1.301944, 0.846044, 0.629034], [-1.291093, 0.846044, 0.618183], [-1.291093, 0.856895, 0.629034], [-1.291093, 0.846044, 0.639884], [-1.291093, 0.846044, -0.394637]]}]},
			"L_lipZipper_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lipZipper_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.106786, 0.191217, 2.044512], [1.106786, 0.202068, 2.055363], [1.106786, 0.191217, 2.066214], [1.106786, 0.180366, 2.055363], [1.106786, 0.191217, 2.044512], [1.117636, 0.191217, 2.055363], [1.106786, 0.191217, 2.066214], [1.095935, 0.191217, 2.055363], [1.106786, 0.202068, 2.055363], [1.117636, 0.191217, 2.055363], [1.106786, 0.180366, 2.055363], [1.095935, 0.191217, 2.055363], [1.106786, 0.191217, 2.044512], [1.117636, 0.191217, 2.055363], [0.083115, 0.191217, 2.055363]]}, {"shapeName": "L_lipZipper_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.083115, 1.214888, 2.044512], [0.072264, 1.214888, 2.055363], [0.083115, 1.214888, 2.066214], [0.093966, 1.214888, 2.055363], [0.083115, 1.214888, 2.044512], [0.083115, 1.225738, 2.055363], [0.083115, 1.214888, 2.066214], [0.083115, 1.204037, 2.055363], [0.072264, 1.214888, 2.055363], [0.083115, 1.225738, 2.055363], [0.093966, 1.214888, 2.055363], [0.083115, 1.204037, 2.055363], [0.083115, 1.214888, 2.044512], [0.083115, 1.225738, 2.055363], [0.083115, 0.191217, 2.055363]]}, {"shapeName": "L_lipZipper_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.083115, 0.202068, 3.079034], [0.072264, 0.191217, 3.079034], [0.083115, 0.180366, 3.079034], [0.093966, 0.191217, 3.079034], [0.083115, 0.202068, 3.079034], [0.083115, 0.191217, 3.089884], [0.083115, 0.180366, 3.079034], [0.083115, 0.191217, 3.068183], [0.072264, 0.191217, 3.079034], [0.083115, 0.191217, 3.089884], [0.093966, 0.191217, 3.079034], [0.083115, 0.191217, 3.068183], [0.083115, 0.202068, 3.079034], [0.083115, 0.191217, 3.089884], [0.083115, 0.191217, 2.055363]]}]},
			"R_cheekLower_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheekLower_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.605383, 2.127413, -0.842306], [-2.614691, 2.135301, -0.832998], [-2.620269, 2.122138, -0.827421], [-2.610961, 2.11425, -0.836728], [-2.605383, 2.127413, -0.842306], [-2.620498, 2.124776, -0.842535], [-2.620269, 2.122138, -0.827421], [-2.605153, 2.124776, -0.82719], [-2.614691, 2.135301, -0.832998], [-2.620498, 2.124776, -0.842535], [-2.610961, 2.11425, -0.836728], [-2.605153, 2.124776, -0.82719], [-2.605383, 2.127413, -0.842306], [-2.620498, 2.124776, -0.842535], [-1.888981, 2.124776, -0.111019]]}, {"shapeName": "R_cheekLower_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-2.057493, 3.12038, 0.057493], [-2.057263, 3.117742, 0.072609], [-2.072379, 3.115104, 0.072379], [-2.072609, 3.117742, 0.057263], [-2.057493, 3.12038, 0.057493], [-2.066801, 3.128267, 0.066801], [-2.072379, 3.115104, 0.072379], [-2.063071, 3.107216, 0.063071], [-2.057263, 3.117742, 0.072609], [-2.066801, 3.128267, 0.066801], [-2.072609, 3.117742, 0.057263], [-2.063071, 3.107216, 0.063071], [-2.057493, 3.12038, 0.057493], [-2.066801, 3.128267, 0.066801], [-1.888981, 2.124776, -0.111019]]}, {"shapeName": "R_cheekLower_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.59298, 1.886464, 0.59298], [-2.583442, 1.875938, 0.598787], [-2.58925, 1.865413, 0.58925], [-2.598787, 1.875938, 0.583442], [-2.59298, 1.886464, 0.59298], [-2.598557, 1.873301, 0.598557], [-2.58925, 1.865413, 0.58925], [-2.583672, 1.878576, 0.583672], [-2.583442, 1.875938, 0.598787], [-2.598557, 1.873301, 0.598557], [-2.598787, 1.875938, 0.583442], [-2.583672, 1.878576, 0.583672], [-2.59298, 1.886464, 0.59298], [-2.598557, 1.873301, 0.598557], [-1.888981, 2.124776, -0.111019]]}]},
			"C_tongue_IK_A_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_A_CTLShape", "degree": 3, "form": 2, "points": [[0.097951, -0.097951, -3.157066], [0.138524, 0.0, -3.157066], [0.097951, 0.097951, -3.157066], [0.0, 0.138524, -3.157066], [-0.097951, 0.097951, -3.157066], [-0.138524, 0.0, -3.157066], [-0.097951, -0.097951, -3.157066], [0.0, -0.138524, -3.157066]]}]},
			"R_cheekLower_A_A_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_A_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.738112, 2.159677, 0.043083], [-1.714088, 2.174478, 0.068784], [-1.685017, 2.160945, 0.089486], [-1.66793, 2.127003, 0.093061], [-1.672834, 2.092537, 0.077415], [-1.696858, 2.077735, 0.051714], [-1.725929, 2.091269, 0.031013], [-1.743016, 2.12521, 0.027438]]}]},
			"L_lowerLid_C_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.674269, 5.582105, 0.144183], [1.674269, 5.575104, 0.144183], [1.68127, 5.575104, 0.144183], [1.68127, 5.582105, 0.144183], [1.674269, 5.582105, 0.144183]]}]},
			"R_lowerLipSecondary_D_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_D_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.646693, -0.150506, -0.388637], [-1.646693, -0.150506, -0.400637], [-1.646693, -0.138506, -0.400637], [-1.646693, -0.138506, -0.388637], [-1.658693, -0.138506, -0.388637], [-1.658693, -0.138506, -0.400637], [-1.658693, -0.150506, -0.400637], [-1.658693, -0.150506, -0.388637], [-1.646693, -0.150506, -0.388637], [-1.646693, -0.138506, -0.388637], [-1.646693, -0.138506, -0.400637], [-1.658693, -0.138506, -0.400637], [-1.658693, -0.138506, -0.388637], [-1.658693, -0.150506, -0.388637], [-1.658693, -0.150506, -0.400637], [-1.646693, -0.150506, -0.400637]]}]},
			"C_lowerLip_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lowerLip_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.011754, -1.022029, -0.394637], [0.0, -1.017161, -0.394637], [-0.011754, -1.022029, -0.394637], [-0.016623, -1.033783, -0.394637], [-0.011754, -1.045538, -0.394637], [0.0, -1.050406, -0.394637], [0.011754, -1.045538, -0.394637], [0.016623, -1.033783, -0.394637]]}]},
			"C_noseTip_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_noseTip_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.164559, 5.311767, -1.013724], [0.0, 5.379929, -1.013724], [-0.164559, 5.311767, -1.013724], [-0.232721, 5.147208, -1.013724], [-0.164559, 4.98265, -1.013724], [0.0, 4.914487, -1.013724], [0.164559, 4.98265, -1.013724], [0.232721, 5.147208, -1.013724]]}]},
			"L_upperLip_A_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_upperLip_A_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.114383, 1.007517, -0.394637], [1.102629, 1.012386, -0.394637], [1.090874, 1.007517, -0.394637], [1.086006, 0.995763, -0.394637], [1.090874, 0.984009, -0.394637], [1.102629, 0.97914, -0.394637], [1.114383, 0.984009, -0.394637], [1.119251, 0.995763, -0.394637]]}]},
			"R_lowerLipSecondary_D_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_D_CTLShape", "degree": 1, "form": 0, "points": [[-1.642693, -0.154506, -0.384637], [-1.642693, -0.154506, -0.404637], [-1.642693, -0.134506, -0.404637], [-1.642693, -0.134506, -0.384637], [-1.662693, -0.134506, -0.384637], [-1.662693, -0.134506, -0.404637], [-1.662693, -0.154506, -0.404637], [-1.662693, -0.154506, -0.384637], [-1.642693, -0.154506, -0.384637], [-1.642693, -0.134506, -0.384637], [-1.642693, -0.134506, -0.404637], [-1.662693, -0.134506, -0.404637], [-1.662693, -0.134506, -0.384637], [-1.662693, -0.154506, -0.384637], [-1.662693, -0.154506, -0.404637], [-1.642693, -0.154506, -0.404637]]}]},
			"R_outterLid_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_outterLid_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.063972, 5.970252, 0.144183], [-2.063972, 5.964807, 0.144183], [-2.069417, 5.964807, 0.144183], [-2.069417, 5.970252, 0.144183], [-2.063972, 5.970252, 0.144183]]}]},
			"C_tongue_FK_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_tongue_FK_C_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.125, -2.56778], [0.0, 0.125951, -2.562996], [0.0, 0.128661, -2.558941], [0.0, 0.132716, -2.556231], [0.0, 0.1375, -2.55528], [0.0, 0.142284, -2.556231], [0.0, 0.146339, -2.558941], [0.0, 0.149049, -2.562996], [0.0, 0.15, -2.56778], [0.0, 0.149049, -2.572563], [0.0, 0.146339, -2.576619], [0.0, 0.142284, -2.579328], [0.0, 0.1375, -2.58028], [0.0, 0.132716, -2.579328], [0.0, 0.128661, -2.576619], [0.0, 0.125951, -2.572563], [0.0, 0.125, -2.56778], [0.0, 0.0, -2.56778]]}]},
			"L_lookAt_CTL": {"color": 18, "shapes": [{"shapeName": "L_lookAt_CTLShape", "degree": 3, "form": 2, "points": [[2.195903, 6.195903, 2.5], [2.0, 6.277049, 2.5], [1.804097, 6.195903, 2.5], [1.722951, 6.0, 2.5], [1.804097, 5.804097, 2.5], [2.0, 5.722951, 2.5], [2.195903, 5.804097, 2.5], [2.277048, 6.0, 2.5]]}]},
			"L_outterLid_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_outterLid_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.064361, 5.969863, 0.144183], [2.064361, 5.965196, 0.144183], [2.069028, 5.965196, 0.144183], [2.069028, 5.969863, 0.144183], [2.064361, 5.969863, 0.144183]]}]},
			"L_upperLid_C_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.675047, 6.359177, 0.144183], [1.675047, 6.353732, 0.144183], [1.680492, 6.353732, 0.144183], [1.680492, 6.359177, 0.144183], [1.675047, 6.359177, 0.144183]]}]},
			"C_tongue_IK_B_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_B_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.088156, -0.088156, -2.532066], [0.124672, 0.0, -2.532066], [0.088156, 0.088156, -2.532066], [0.0, 0.124672, -2.532066], [-0.088156, 0.088156, -2.532066], [-0.124672, 0.0, -2.532066], [-0.088156, -0.088156, -2.532066], [0.0, -0.124672, -2.532066]]}]},
			"L_cheekLower_B_A_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_B_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.919977, 2.15898, -0.129892], [1.897553, 2.173149, -0.102447], [1.870108, 2.15898, -0.080023], [1.853719, 2.124776, -0.075756], [1.857986, 2.090571, -0.092145], [1.88041, 2.076403, -0.11959], [1.907855, 2.090571, -0.142014], [1.924244, 2.124776, -0.146281]]}]},
			"L_upperLipSecondary_C_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.283093, 0.838044, -0.386637], [1.283093, 0.838044, -0.402637], [1.283093, 0.854044, -0.402637], [1.283093, 0.854044, -0.386637], [1.299093, 0.854044, -0.386637], [1.299093, 0.854044, -0.402637], [1.299093, 0.838044, -0.402637], [1.299093, 0.838044, -0.386637], [1.283093, 0.838044, -0.386637], [1.283093, 0.854044, -0.386637], [1.283093, 0.854044, -0.402637], [1.299093, 0.854044, -0.402637], [1.299093, 0.854044, -0.386637], [1.299093, 0.838044, -0.386637], [1.299093, 0.838044, -0.402637], [1.283093, 0.838044, -0.402637]]}]},
			"C_upperLip_CTL": {"color": 17, "shapes": [{"shapeName": "C_upperLip_CTLShape", "degree": 3, "form": 2, "points": [[0.01959, 1.455807, -0.384637], [0.0, 1.463921, -0.384637], [-0.01959, 1.455807, -0.384637], [-0.027705, 1.436217, -0.384637], [-0.01959, 1.416626, -0.384637], [0.0, 1.408512, -0.384637], [0.01959, 1.416626, -0.384637], [0.027705, 1.436217, -0.384637]]}]},
			"R_lowerLid_B_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_B_CTLShape", "degree": 1, "form": 0, "points": [[-1.283345, 5.461927, 0.151961], [-1.288845, 5.456426, 0.151961], [-1.294345, 5.461927, 0.151961], [-1.288845, 5.467427, 0.151961], [-1.283345, 5.461927, 0.151961]]}]},
			"L_upperLipSecondary_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upperLipSecondary_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.314764, 0.846044, -0.405488], [2.314764, 0.856895, -0.394637], [2.314764, 0.846044, -0.383786], [2.314764, 0.835193, -0.394637], [2.314764, 0.846044, -0.405488], [2.325614, 0.846044, -0.394637], [2.314764, 0.846044, -0.383786], [2.303913, 0.846044, -0.394637], [2.314764, 0.856895, -0.394637], [2.325614, 0.846044, -0.394637], [2.314764, 0.835193, -0.394637], [2.303913, 0.846044, -0.394637], [2.314764, 0.846044, -0.405488], [2.325614, 0.846044, -0.394637], [1.291093, 0.846044, -0.394637]]}, {"shapeName": "L_upperLipSecondary_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.291093, 1.869715, -0.405488], [1.280242, 1.869715, -0.394637], [1.291093, 1.869715, -0.383786], [1.301944, 1.869715, -0.394637], [1.291093, 1.869715, -0.405488], [1.291093, 1.880565, -0.394637], [1.291093, 1.869715, -0.383786], [1.291093, 1.858864, -0.394637], [1.280242, 1.869715, -0.394637], [1.291093, 1.880565, -0.394637], [1.301944, 1.869715, -0.394637], [1.291093, 1.858864, -0.394637], [1.291093, 1.869715, -0.405488], [1.291093, 1.880565, -0.394637], [1.291093, 0.846044, -0.394637]]}, {"shapeName": "L_upperLipSecondary_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.291093, 0.856895, 0.629034], [1.280242, 0.846044, 0.629034], [1.291093, 0.835193, 0.629034], [1.301944, 0.846044, 0.629034], [1.291093, 0.856895, 0.629034], [1.291093, 0.846044, 0.639884], [1.291093, 0.835193, 0.629034], [1.291093, 0.846044, 0.618183], [1.280242, 0.846044, 0.629034], [1.291093, 0.846044, 0.639884], [1.301944, 0.846044, 0.629034], [1.291093, 0.846044, 0.618183], [1.291093, 0.856895, 0.629034], [1.291093, 0.846044, 0.639884], [1.291093, 0.846044, -0.394637]]}]},
			"L_lowerLipSecondary_D_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_D_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.644693, -0.152506, -0.386637], [1.644693, -0.152506, -0.402637], [1.644693, -0.136506, -0.402637], [1.644693, -0.136506, -0.386637], [1.660693, -0.136506, -0.386637], [1.660693, -0.136506, -0.402637], [1.660693, -0.152506, -0.402637], [1.660693, -0.152506, -0.386637], [1.644693, -0.152506, -0.386637], [1.644693, -0.136506, -0.386637], [1.644693, -0.136506, -0.402637], [1.660693, -0.136506, -0.402637], [1.660693, -0.136506, -0.386637], [1.660693, -0.152506, -0.386637], [1.660693, -0.152506, -0.402637], [1.644693, -0.152506, -0.402637]]}]},
			"L_upperLipSecondary_A_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.466266, 1.339453, -0.385637], [0.466266, 1.339453, -0.403637], [0.466266, 1.357453, -0.403637], [0.466266, 1.357453, -0.385637], [0.484266, 1.357453, -0.385637], [0.484266, 1.357453, -0.403637], [0.484266, 1.339453, -0.403637], [0.484266, 1.339453, -0.385637], [0.466266, 1.339453, -0.385637], [0.466266, 1.357453, -0.385637], [0.466266, 1.357453, -0.403637], [0.484266, 1.357453, -0.403637], [0.484266, 1.357453, -0.385637], [0.484266, 1.339453, -0.385637], [0.484266, 1.339453, -0.403637], [0.466266, 1.339453, -0.403637]]}]},
			"C_noseBase_CTL": {"color": 17, "shapes": [{"shapeName": "C_noseBase_CTLShape", "degree": 3, "form": 2, "points": [[0.391806, 5.539014, -1.113724], [0.0, 5.701305, -1.113724], [-0.391806, 5.539014, -1.113724], [-0.554097, 5.147208, -1.113724], [-0.391806, 4.755402, -1.113724], [0.0, 4.593111, -1.113724], [0.391806, 4.755402, -1.113724], [0.554097, 5.147208, -1.113724]]}]},
			"R_squint_C_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.160908, 2.854609, -0.198557], [-2.145949, 2.877033, -0.211023], [-2.175552, 2.875943, -0.213132], [-2.160908, 2.854609, -0.198557], [-2.147987, 2.875164, -0.181453], [-2.145949, 2.877033, -0.211023], [-2.16263, 2.896498, -0.196028], [-2.147987, 2.875164, -0.181453], [-2.17759, 2.874074, -0.183562], [-2.160908, 2.854609, -0.198557], [-2.175552, 2.875943, -0.213132], [-2.16263, 2.896498, -0.196028], [-2.17759, 2.874074, -0.183562], [-2.175552, 2.875943, -0.213132]]}]},
			"R_nostril_B_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "R_nostril_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-0.656722, 5.30393, -1.613724], [-0.5, 5.368847, -1.613724], [-0.343278, 5.30393, -1.613724], [-0.278361, 5.147208, -1.613724], [-0.343278, 4.990486, -1.613724], [-0.5, 4.925569, -1.613724], [-0.656722, 4.990486, -1.613724], [-0.721639, 5.147208, -1.613724]]}]},
			"R_cheek_C_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_C_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.16855, 2.658425, -0.243469], [-2.14706, 2.672172, -0.215078], [-2.122254, 2.657119, -0.190282], [-2.108663, 2.622084, -0.183605], [-2.114248, 2.587589, -0.198958], [-2.135737, 2.573842, -0.227348], [-2.160543, 2.588895, -0.252145], [-2.174134, 2.623931, -0.258822]]}]},
			"L_cheek_C_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_C_CTLShape", "degree": 3, "form": 2, "points": [[2.320725, 2.629085, -0.116928], [2.296848, 2.64436, -0.085383], [2.269286, 2.627634, -0.057831], [2.254184, 2.588706, -0.050412], [2.260389, 2.550379, -0.067471], [2.284266, 2.535104, -0.099016], [2.311828, 2.55183, -0.126568], [2.32693, 2.590758, -0.133987]]}]},
			"C_tongue_IK_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_IK_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -1.651148], [0.0, 0.002713, -1.651148], [-0.002713, 0.0, -1.651148], [0.0, -0.002713, -1.651148], [0.002713, 0.0, -1.651148], [0.0, 0.0, -1.648435], [-0.002713, 0.0, -1.651148], [0.0, 0.0, -1.653861], [0.0, 0.002713, -1.651148], [0.0, 0.0, -1.648435], [0.0, -0.002713, -1.651148], [0.0, 0.0, -1.653861], [0.002713, 0.0, -1.651148], [0.0, 0.0, -1.648435], [0.0, 0.0, -1.907066]]}, {"shapeName": "C_tongue_IK_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -1.907066], [0.0, 0.255918, -1.909778], [-0.002713, 0.255918, -1.907066], [0.0, 0.255918, -1.904353], [0.002713, 0.255918, -1.907066], [0.0, 0.25863, -1.907066], [-0.002713, 0.255918, -1.907066], [0.0, 0.253205, -1.907066], [0.0, 0.255918, -1.909778], [0.0, 0.25863, -1.907066], [0.0, 0.255918, -1.904353], [0.0, 0.253205, -1.907066], [0.002713, 0.255918, -1.907066], [0.0, 0.25863, -1.907066], [0.0, 0.0, -1.907066]]}, {"shapeName": "C_tongue_IK_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -1.907066], [-0.255918, 0.0, -1.909778], [-0.255918, -0.002713, -1.907066], [-0.255918, 0.0, -1.904353], [-0.255918, 0.002713, -1.907066], [-0.25863, 0.0, -1.907066], [-0.255918, -0.002713, -1.907066], [-0.253205, 0.0, -1.907066], [-0.255918, 0.0, -1.909778], [-0.25863, 0.0, -1.907066], [-0.255918, 0.0, -1.904353], [-0.253205, 0.0, -1.907066], [-0.255918, 0.002713, -1.907066], [-0.25863, 0.0, -1.907066], [0.0, 0.0, -1.907066]]}]},
			"L_eye_FK_D_OFF_CTL": {"color": 8, "shapes": [{"shapeName": "L_eye_FK_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.0, 6.0, 0.5], [2.075, 6.0, 0.425], [2.069291, 5.971299, 0.425], [2.0, 6.0, 0.5], [1.925, 6.0, 0.425], [1.930709, 6.028701, 0.425], [2.0, 6.0, 0.5], [2.053033, 5.946967, 0.425], [2.028701, 5.930709, 0.425], [2.0, 6.0, 0.5], [1.946967, 6.053033, 0.425], [1.971299, 6.069291, 0.425], [2.0, 6.0, 0.5], [2.0, 5.925, 0.425], [1.971299, 5.930709, 0.425], [2.0, 6.0, 0.5], [2.0, 6.075, 0.425], [2.028701, 6.069291, 0.425], [2.0, 6.0, 0.5], [1.946967, 5.946967, 0.425], [1.930709, 5.971299, 0.425], [2.0, 6.0, 0.5], [2.053033, 6.053033, 0.425], [2.069291, 6.028701, 0.425], [2.075, 6.0, 0.425], [2.069291, 5.971299, 0.425], [2.053033, 5.946967, 0.425], [2.028701, 5.930709, 0.425], [2.0, 5.925, 0.425], [1.971299, 5.930709, 0.425], [1.946967, 5.946967, 0.425], [1.930709, 5.971299, 0.425], [1.925, 6.0, 0.425], [1.930709, 6.028701, 0.425], [1.946967, 6.053033, 0.425], [1.971299, 6.069291, 0.425], [2.0, 6.075, 0.425], [2.028701, 6.069291, 0.425], [2.053033, 6.053033, 0.425], [2.069291, 6.028701, 0.425], [2.0, 6.0, 0.5]]}]},
			"R_brow_C_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_C_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.696423, 7.81494, -1.515097], [-1.664817, 7.825752, -1.509162], [-1.64121, 7.819147, -1.485707], [-1.63943, 7.798993, -1.458473], [-1.66052, 7.777097, -1.443412], [-1.692126, 7.766286, -1.449347], [-1.715733, 7.772891, -1.472802], [-1.717513, 7.793045, -1.500036]]}]},
			"L_lowerLidPrimary_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLidPrimary_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.293112, 5.466193, 0.144183], [1.288845, 5.467961, 0.144183], [1.284578, 5.466193, 0.144183], [1.282811, 5.461927, 0.144183], [1.284578, 5.45766, 0.144183], [1.288845, 5.455893, 0.144183], [1.293112, 5.45766, 0.144183], [1.294879, 5.461927, 0.144183]]}]},
			"C_mouthAll_D_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "C_mouthAll_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.035263, 0.214725, -1.619637], [0.0, 0.224462, -1.619637], [-0.035263, 0.214725, -1.619637], [-0.049869, 0.191217, -1.619637], [-0.035263, 0.167708, -1.619637], [0.0, 0.157971, -1.619637], [0.035263, 0.167708, -1.619637], [0.049869, 0.191217, -1.619637]]}]},
			"L_upperLid_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upperLid_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.298051, 6.356454, 0.139963], [1.298051, 6.360674, 0.144183], [1.298051, 6.356454, 0.148403], [1.298051, 6.352234, 0.144183], [1.298051, 6.356454, 0.139963], [1.302271, 6.356454, 0.144183], [1.298051, 6.356454, 0.148403], [1.293831, 6.356454, 0.144183], [1.298051, 6.360674, 0.144183], [1.302271, 6.356454, 0.144183], [1.298051, 6.352234, 0.144183], [1.293831, 6.356454, 0.144183], [1.298051, 6.356454, 0.139963], [1.302271, 6.356454, 0.144183], [0.89992, 6.356454, 0.144183]]}, {"shapeName": "L_upperLid_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.89992, 6.754585, 0.139963], [0.8957, 6.754585, 0.144183], [0.89992, 6.754585, 0.148403], [0.90414, 6.754585, 0.144183], [0.89992, 6.754585, 0.139963], [0.89992, 6.758805, 0.144183], [0.89992, 6.754585, 0.148403], [0.89992, 6.750365, 0.144183], [0.8957, 6.754585, 0.144183], [0.89992, 6.758805, 0.144183], [0.90414, 6.754585, 0.144183], [0.89992, 6.750365, 0.144183], [0.89992, 6.754585, 0.139963], [0.89992, 6.758805, 0.144183], [0.89992, 6.356454, 0.144183]]}, {"shapeName": "L_upperLid_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.89992, 6.360674, 0.542314], [0.8957, 6.356454, 0.542314], [0.89992, 6.352234, 0.542314], [0.90414, 6.356454, 0.542314], [0.89992, 6.360674, 0.542314], [0.89992, 6.356454, 0.546534], [0.89992, 6.352234, 0.542314], [0.89992, 6.356454, 0.538094], [0.8957, 6.356454, 0.542314], [0.89992, 6.356454, 0.546534], [0.90414, 6.356454, 0.542314], [0.89992, 6.356454, 0.538094], [0.89992, 6.360674, 0.542314], [0.89992, 6.356454, 0.546534], [0.89992, 6.356454, 0.144183]]}]},
			"C_tongue_FK_E_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_tongue_FK_E_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.125, -1.853494], [0.0, 0.125951, -1.848711], [0.0, 0.128661, -1.844655], [0.0, 0.132716, -1.841946], [0.0, 0.1375, -1.840994], [0.0, 0.142284, -1.841946], [0.0, 0.146339, -1.844655], [0.0, 0.149049, -1.848711], [0.0, 0.15, -1.853494], [0.0, 0.149049, -1.858278], [0.0, 0.146339, -1.862333], [0.0, 0.142284, -1.865043], [0.0, 0.1375, -1.865994], [0.0, 0.132716, -1.865043], [0.0, 0.128661, -1.862333], [0.0, 0.125951, -1.858278], [0.0, 0.125, -1.853494], [0.0, 0.0, -1.853494]]}]},
			"R_lipCornerSecondary_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lipCornerSecondary_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-3.023671, 0.191217, -0.405488], [-3.023671, 0.202068, -0.394637], [-3.023671, 0.191217, -0.383786], [-3.023671, 0.180366, -0.394637], [-3.023671, 0.191217, -0.405488], [-3.034521, 0.191217, -0.394637], [-3.023671, 0.191217, -0.383786], [-3.01282, 0.191217, -0.394637], [-3.023671, 0.202068, -0.394637], [-3.034521, 0.191217, -0.394637], [-3.023671, 0.180366, -0.394637], [-3.01282, 0.191217, -0.394637], [-3.023671, 0.191217, -0.405488], [-3.034521, 0.191217, -0.394637], [-2.0, 0.191217, -0.394637]]}, {"shapeName": "R_lipCornerSecondary_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-2.0, 1.214888, -0.405488], [-1.989149, 1.214888, -0.394637], [-2.0, 1.214888, -0.383786], [-2.010851, 1.214888, -0.394637], [-2.0, 1.214888, -0.405488], [-2.0, 1.225738, -0.394637], [-2.0, 1.214888, -0.383786], [-2.0, 1.204037, -0.394637], [-1.989149, 1.214888, -0.394637], [-2.0, 1.225738, -0.394637], [-2.010851, 1.214888, -0.394637], [-2.0, 1.204037, -0.394637], [-2.0, 1.214888, -0.405488], [-2.0, 1.225738, -0.394637], [-2.0, 0.191217, -0.394637]]}, {"shapeName": "R_lipCornerSecondary_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.0, 0.202068, 0.629034], [-1.989149, 0.191217, 0.629034], [-2.0, 0.180366, 0.629034], [-2.010851, 0.191217, 0.629034], [-2.0, 0.202068, 0.629034], [-2.0, 0.191217, 0.639884], [-2.0, 0.180366, 0.629034], [-2.0, 0.191217, 0.618183], [-1.989149, 0.191217, 0.629034], [-2.0, 0.191217, 0.639884], [-2.010851, 0.191217, 0.629034], [-2.0, 0.191217, 0.618183], [-2.0, 0.202068, 0.629034], [-2.0, 0.191217, 0.639884], [-2.0, 0.191217, -0.394637]]}]},
			"L_lookAt_D_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "L_lookAt_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.117542, 6.117542, 2.5], [2.0, 6.166229, 2.5], [1.882458, 6.117542, 2.5], [1.833771, 6.0, 2.5], [1.882458, 5.882458, 2.5], [2.0, 5.833771, 2.5], [2.117542, 5.882458, 2.5], [2.166229, 6.0, 2.5]]}]},
			"L_lowerLid_C_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.675047, 5.581327, 0.144183], [1.675047, 5.575882, 0.144183], [1.680492, 5.575882, 0.144183], [1.680492, 5.581327, 0.144183], [1.675047, 5.581327, 0.144183]]}]},
			"L_upperLipSecondary_C_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.284093, 0.839044, -0.387637], [1.284093, 0.839044, -0.401637], [1.284093, 0.853044, -0.401637], [1.284093, 0.853044, -0.387637], [1.298093, 0.853044, -0.387637], [1.298093, 0.853044, -0.401637], [1.298093, 0.839044, -0.401637], [1.298093, 0.839044, -0.387637], [1.284093, 0.839044, -0.387637], [1.284093, 0.853044, -0.387637], [1.284093, 0.853044, -0.401637], [1.298093, 0.853044, -0.401637], [1.298093, 0.853044, -0.387637], [1.298093, 0.839044, -0.387637], [1.298093, 0.839044, -0.401637], [1.284093, 0.839044, -0.401637]]}]},
			"R_eye_FK_C_OFF_CTL": {"color": 8, "shapes": [{"shapeName": "R_eye_FK_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.0, 6.0, 0.5], [-2.0875, 6.0, 0.4125], [-2.08084, 5.966515, 0.4125], [-2.0, 6.0, 0.5], [-1.9125, 6.0, 0.4125], [-1.919161, 6.033485, 0.4125], [-2.0, 6.0, 0.5], [-2.061872, 5.938128, 0.4125], [-2.033485, 5.919161, 0.4125], [-2.0, 6.0, 0.5], [-1.938128, 6.061872, 0.4125], [-1.966515, 6.080839, 0.4125], [-2.0, 6.0, 0.5], [-2.0, 5.9125, 0.4125], [-1.966515, 5.919161, 0.4125], [-2.0, 6.0, 0.5], [-2.0, 6.0875, 0.4125], [-2.033485, 6.080839, 0.4125], [-2.0, 6.0, 0.5], [-1.938128, 5.938128, 0.4125], [-1.919161, 5.966515, 0.4125], [-2.0, 6.0, 0.5], [-2.061872, 6.061872, 0.4125], [-2.08084, 6.033485, 0.4125], [-2.0875, 6.0, 0.4125], [-2.08084, 5.966515, 0.4125], [-2.061872, 5.938128, 0.4125], [-2.033485, 5.919161, 0.4125], [-2.0, 5.9125, 0.4125], [-1.966515, 5.919161, 0.4125], [-1.938128, 5.938128, 0.4125], [-1.919161, 5.966515, 0.4125], [-1.9125, 6.0, 0.4125], [-1.919161, 6.033485, 0.4125], [-1.938128, 6.061872, 0.4125], [-1.966515, 6.080839, 0.4125], [-2.0, 6.0875, 0.4125], [-2.033485, 6.080839, 0.4125], [-2.061872, 6.061872, 0.4125], [-2.08084, 6.033485, 0.4125], [-2.0, 6.0, 0.5]]}]},
			"R_upperLipSecondary_A_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_A_CTLShape", "degree": 1, "form": 0, "points": [[-0.465266, 1.338453, -0.384637], [-0.465266, 1.338453, -0.404637], [-0.465266, 1.358453, -0.404637], [-0.465266, 1.358453, -0.384637], [-0.485266, 1.358453, -0.384637], [-0.485266, 1.358453, -0.404637], [-0.485266, 1.338453, -0.404637], [-0.485266, 1.338453, -0.384637], [-0.465266, 1.338453, -0.384637], [-0.465266, 1.358453, -0.384637], [-0.465266, 1.358453, -0.404637], [-0.485266, 1.358453, -0.404637], [-0.485266, 1.358453, -0.384637], [-0.485266, 1.338453, -0.384637], [-0.485266, 1.338453, -0.404637], [-0.465266, 1.338453, -0.404637]]}]},
			"C_tongue_IK_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_IK_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -1.026148], [0.0, 0.002713, -1.026148], [-0.002713, 0.0, -1.026148], [0.0, -0.002713, -1.026148], [0.002713, 0.0, -1.026148], [0.0, 0.0, -1.023435], [-0.002713, 0.0, -1.026148], [0.0, 0.0, -1.028861], [0.0, 0.002713, -1.026148], [0.0, 0.0, -1.023435], [0.0, -0.002713, -1.026148], [0.0, 0.0, -1.028861], [0.002713, 0.0, -1.026148], [0.0, 0.0, -1.023435], [0.0, 0.0, -1.282066]]}, {"shapeName": "C_tongue_IK_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -1.282066], [0.0, 0.255918, -1.284778], [-0.002713, 0.255918, -1.282066], [0.0, 0.255918, -1.279353], [0.002713, 0.255918, -1.282066], [0.0, 0.25863, -1.282066], [-0.002713, 0.255918, -1.282066], [0.0, 0.253205, -1.282066], [0.0, 0.255918, -1.284778], [0.0, 0.25863, -1.282066], [0.0, 0.255918, -1.279353], [0.0, 0.253205, -1.282066], [0.002713, 0.255918, -1.282066], [0.0, 0.25863, -1.282066], [0.0, 0.0, -1.282066]]}, {"shapeName": "C_tongue_IK_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -1.282066], [-0.255918, 0.0, -1.284778], [-0.255918, -0.002713, -1.282066], [-0.255918, 0.0, -1.279353], [-0.255918, 0.002713, -1.282066], [-0.25863, 0.0, -1.282066], [-0.255918, -0.002713, -1.282066], [-0.253205, 0.0, -1.282066], [-0.255918, 0.0, -1.284778], [-0.25863, 0.0, -1.282066], [-0.255918, 0.0, -1.279353], [-0.253205, 0.0, -1.282066], [-0.255918, 0.002713, -1.282066], [-0.25863, 0.0, -1.282066], [0.0, 0.0, -1.282066]]}]},
			"L_cheek_B_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_B_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.988555, 2.643811, -0.050232], [1.970513, 2.65501, -0.029487], [1.949768, 2.643811, -0.011445], [1.938473, 2.616776, -0.006674], [1.943243, 2.58974, -0.01797], [1.961285, 2.578541, -0.038715], [1.98203, 2.58974, -0.056757], [1.993326, 2.616776, -0.061527]]}]},
			"R_upperLid_B_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.286511, 6.475465, 0.144183], [-1.286511, 6.470798, 0.144183], [-1.291178, 6.470798, 0.144183], [-1.291178, 6.475465, 0.144183], [-1.286511, 6.475465, 0.144183]]}]},
			"R_upperLipSecondary_B_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.897651, 1.127795, -0.386637], [-0.897651, 1.127795, -0.402637], [-0.897651, 1.143795, -0.402637], [-0.897651, 1.143795, -0.386637], [-0.913651, 1.143795, -0.386637], [-0.913651, 1.143795, -0.402637], [-0.913651, 1.127795, -0.402637], [-0.913651, 1.127795, -0.386637], [-0.897651, 1.127795, -0.386637], [-0.897651, 1.143795, -0.386637], [-0.897651, 1.143795, -0.402637], [-0.913651, 1.143795, -0.402637], [-0.913651, 1.143795, -0.386637], [-0.913651, 1.127795, -0.386637], [-0.913651, 1.127795, -0.402637], [-0.897651, 1.127795, -0.402637]]}]},
			"C_mouthAll_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_mouthAll_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 0.191217, -1.630488], [1.023671, 0.202068, -1.619637], [1.023671, 0.191217, -1.608786], [1.023671, 0.180366, -1.619637], [1.023671, 0.191217, -1.630488], [1.034521, 0.191217, -1.619637], [1.023671, 0.191217, -1.608786], [1.01282, 0.191217, -1.619637], [1.023671, 0.202068, -1.619637], [1.034521, 0.191217, -1.619637], [1.023671, 0.180366, -1.619637], [1.01282, 0.191217, -1.619637], [1.023671, 0.191217, -1.630488], [1.034521, 0.191217, -1.619637], [0.0, 0.191217, -1.619637]]}, {"shapeName": "C_mouthAll_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 1.214888, -1.630488], [-0.010851, 1.214888, -1.619637], [0.0, 1.214888, -1.608786], [0.010851, 1.214888, -1.619637], [0.0, 1.214888, -1.630488], [0.0, 1.225738, -1.619637], [0.0, 1.214888, -1.608786], [0.0, 1.204037, -1.619637], [-0.010851, 1.214888, -1.619637], [0.0, 1.225738, -1.619637], [0.010851, 1.214888, -1.619637], [0.0, 1.204037, -1.619637], [0.0, 1.214888, -1.630488], [0.0, 1.225738, -1.619637], [0.0, 0.191217, -1.619637]]}, {"shapeName": "C_mouthAll_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 0.202068, -0.595966], [-0.010851, 0.191217, -0.595966], [0.0, 0.180366, -0.595966], [0.010851, 0.191217, -0.595966], [0.0, 0.202068, -0.595966], [0.0, 0.191217, -0.585116], [0.0, 0.180366, -0.595966], [0.0, 0.191217, -0.606817], [-0.010851, 0.191217, -0.595966], [0.0, 0.191217, -0.585116], [0.010851, 0.191217, -0.595966], [0.0, 0.191217, -0.606817], [0.0, 0.202068, -0.595966], [0.0, 0.191217, -0.585116], [0.0, 0.191217, -1.619637]]}]},
			"L_lipZipper_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_lipZipper_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.083115, 0.199079, 2.055363], [0.075115, 0.183217, 2.055363], [0.091115, 0.183217, 2.055363], [0.083115, 0.199079, 2.055363], [0.083115, 0.199079, 2.055363]]}]},
			"R_lowerLipSecondary_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lowerLipSecondary_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.314764, -0.463611, -0.405488], [-2.314764, -0.45276, -0.394637], [-2.314764, -0.463611, -0.383786], [-2.314764, -0.474462, -0.394637], [-2.314764, -0.463611, -0.405488], [-2.325614, -0.463611, -0.394637], [-2.314764, -0.463611, -0.383786], [-2.303913, -0.463611, -0.394637], [-2.314764, -0.45276, -0.394637], [-2.325614, -0.463611, -0.394637], [-2.314764, -0.474462, -0.394637], [-2.303913, -0.463611, -0.394637], [-2.314764, -0.463611, -0.405488], [-2.325614, -0.463611, -0.394637], [-1.291093, -0.463611, -0.394637]]}, {"shapeName": "R_lowerLipSecondary_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.291093, 0.56006, -0.405488], [-1.280242, 0.56006, -0.394637], [-1.291093, 0.56006, -0.383786], [-1.301944, 0.56006, -0.394637], [-1.291093, 0.56006, -0.405488], [-1.291093, 0.57091, -0.394637], [-1.291093, 0.56006, -0.383786], [-1.291093, 0.549209, -0.394637], [-1.280242, 0.56006, -0.394637], [-1.291093, 0.57091, -0.394637], [-1.301944, 0.56006, -0.394637], [-1.291093, 0.549209, -0.394637], [-1.291093, 0.56006, -0.405488], [-1.291093, 0.57091, -0.394637], [-1.291093, -0.463611, -0.394637]]}, {"shapeName": "R_lowerLipSecondary_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.291093, -0.45276, 0.629034], [-1.280242, -0.463611, 0.629034], [-1.291093, -0.474462, 0.629034], [-1.301944, -0.463611, 0.629034], [-1.291093, -0.45276, 0.629034], [-1.291093, -0.463611, 0.639884], [-1.291093, -0.474462, 0.629034], [-1.291093, -0.463611, 0.618183], [-1.280242, -0.463611, 0.629034], [-1.291093, -0.463611, 0.639884], [-1.301944, -0.463611, 0.629034], [-1.291093, -0.463611, 0.618183], [-1.291093, -0.45276, 0.629034], [-1.291093, -0.463611, 0.639884], [-1.291093, -0.463611, -0.394637]]}]},
			"L_lowerLipSecondary_D_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_D_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.646693, -0.150506, -0.388637], [1.646693, -0.150506, -0.400637], [1.646693, -0.138506, -0.400637], [1.646693, -0.138506, -0.388637], [1.658693, -0.138506, -0.388637], [1.658693, -0.138506, -0.400637], [1.658693, -0.150506, -0.400637], [1.658693, -0.150506, -0.388637], [1.646693, -0.150506, -0.388637], [1.646693, -0.138506, -0.388637], [1.646693, -0.138506, -0.400637], [1.658693, -0.138506, -0.400637], [1.658693, -0.138506, -0.388637], [1.658693, -0.150506, -0.388637], [1.658693, -0.150506, -0.400637], [1.646693, -0.150506, -0.400637]]}]},
			"R_upperLid_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upperLid_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.687036, 6.473484, 0.139964], [-1.687036, 6.477704, 0.144183], [-1.687036, 6.473484, 0.148402], [-1.687036, 6.469264, 0.144183], [-1.687036, 6.473484, 0.139964], [-1.691256, 6.473484, 0.144183], [-1.687036, 6.473484, 0.148402], [-1.682817, 6.473484, 0.144183], [-1.687036, 6.477704, 0.144183], [-1.691256, 6.473484, 0.144183], [-1.687036, 6.469264, 0.144183], [-1.682817, 6.473484, 0.144183], [-1.687036, 6.473484, 0.139964], [-1.691256, 6.473484, 0.144183], [-1.288982, 6.473484, 0.144183]]}, {"shapeName": "R_upperLid_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.288982, 6.871539, 0.139964], [-1.284763, 6.871539, 0.144183], [-1.288982, 6.871539, 0.148402], [-1.293201, 6.871539, 0.144183], [-1.288982, 6.871539, 0.139964], [-1.288982, 6.875758, 0.144183], [-1.288982, 6.871539, 0.148402], [-1.288982, 6.86732, 0.144183], [-1.284763, 6.871539, 0.144183], [-1.288982, 6.875758, 0.144183], [-1.293201, 6.871539, 0.144183], [-1.288982, 6.86732, 0.144183], [-1.288982, 6.871539, 0.139964], [-1.288982, 6.875758, 0.144183], [-1.288982, 6.473484, 0.144183]]}, {"shapeName": "R_upperLid_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.288982, 6.477704, 0.542237], [-1.284763, 6.473484, 0.542237], [-1.288982, 6.469264, 0.542237], [-1.293201, 6.473484, 0.542237], [-1.288982, 6.477704, 0.542237], [-1.288982, 6.473484, 0.546456], [-1.288982, 6.469264, 0.542237], [-1.288982, 6.473484, 0.538018], [-1.284763, 6.473484, 0.542237], [-1.288982, 6.473484, 0.546456], [-1.293201, 6.473484, 0.542237], [-1.288982, 6.473484, 0.538018], [-1.288982, 6.477704, 0.542237], [-1.288982, 6.473484, 0.546456], [-1.288982, 6.473484, 0.144183]]}]},
			"R_lowerLid_B_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.286122, 5.464649, 0.144183], [-1.286122, 5.459204, 0.144183], [-1.291567, 5.459204, 0.144183], [-1.291567, 5.464649, 0.144183], [-1.286122, 5.464649, 0.144183]]}]},
			"L_brow_upper_C_A_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.378861, 8.073127, -1.775818], [1.397669, 8.048717, -1.731474], [1.446632, 8.04549, -1.754017], [1.427825, 8.069901, -1.798361], [1.378861, 8.073127, -1.775818]]}]},
			"R_upperLid_A_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.896419, 6.359955, 0.144183], [-0.896419, 6.352954, 0.144183], [-0.90342, 6.352954, 0.144183], [-0.90342, 6.359955, 0.144183], [-0.896419, 6.359955, 0.144183]]}]},
			"L_upperLid_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upperLid_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.075901, 6.356454, 0.139963], [2.075901, 6.360674, 0.144183], [2.075901, 6.356454, 0.148403], [2.075901, 6.352234, 0.144183], [2.075901, 6.356454, 0.139963], [2.080121, 6.356454, 0.144183], [2.075901, 6.356454, 0.148403], [2.071681, 6.356454, 0.144183], [2.075901, 6.360674, 0.144183], [2.080121, 6.356454, 0.144183], [2.075901, 6.352234, 0.144183], [2.071681, 6.356454, 0.144183], [2.075901, 6.356454, 0.139963], [2.080121, 6.356454, 0.144183], [1.67777, 6.356454, 0.144183]]}, {"shapeName": "L_upperLid_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.67777, 6.754585, 0.139963], [1.67355, 6.754585, 0.144183], [1.67777, 6.754585, 0.148403], [1.68199, 6.754585, 0.144183], [1.67777, 6.754585, 0.139963], [1.67777, 6.758805, 0.144183], [1.67777, 6.754585, 0.148403], [1.67777, 6.750365, 0.144183], [1.67355, 6.754585, 0.144183], [1.67777, 6.758805, 0.144183], [1.68199, 6.754585, 0.144183], [1.67777, 6.750365, 0.144183], [1.67777, 6.754585, 0.139963], [1.67777, 6.758805, 0.144183], [1.67777, 6.356454, 0.144183]]}, {"shapeName": "L_upperLid_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.67777, 6.360674, 0.542314], [1.67355, 6.356454, 0.542314], [1.67777, 6.352234, 0.542314], [1.68199, 6.356454, 0.542314], [1.67777, 6.360674, 0.542314], [1.67777, 6.356454, 0.546534], [1.67777, 6.352234, 0.542314], [1.67777, 6.356454, 0.538094], [1.67355, 6.356454, 0.542314], [1.67777, 6.356454, 0.546534], [1.68199, 6.356454, 0.542314], [1.67777, 6.356454, 0.538094], [1.67777, 6.360674, 0.542314], [1.67777, 6.356454, 0.546534], [1.67777, 6.356454, 0.144183]]}]},
			"R_upperLipSecondary_B_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.899651, 1.129795, -0.388637], [-0.899651, 1.129795, -0.400637], [-0.899651, 1.141795, -0.400637], [-0.899651, 1.141795, -0.388637], [-0.911651, 1.141795, -0.388637], [-0.911651, 1.141795, -0.400637], [-0.911651, 1.129795, -0.400637], [-0.911651, 1.129795, -0.388637], [-0.899651, 1.129795, -0.388637], [-0.899651, 1.141795, -0.388637], [-0.899651, 1.141795, -0.400637], [-0.911651, 1.141795, -0.400637], [-0.911651, 1.141795, -0.388637], [-0.911651, 1.129795, -0.388637], [-0.911651, 1.129795, -0.400637], [-0.899651, 1.129795, -0.400637]]}]},
			"L_brow_upper_A_C_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.480563, 8.105819, -1.515128], [0.485528, 8.087362, -1.477728], [0.527097, 8.086512, -1.483666], [0.522132, 8.104969, -1.521065], [0.480563, 8.105819, -1.515128]]}]},
			"R_lipZipper_CTL": {"color": 13, "shapes": [{"shapeName": "R_lipZipper_CTLShape", "degree": 1, "form": 0, "points": [[-0.073287, 0.191217, 2.055363], [-0.093115, 0.201217, 2.055363], [-0.093115, 0.181217, 2.055363], [-0.073287, 0.191217, 2.055363], [-0.073287, 0.191217, 2.055363]]}]},
			"R_brow_B_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_B_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.217485, 7.836488, -1.292228], [-1.189105, 7.845178, -1.291624], [-1.165626, 7.83902, -1.274534], [-1.160801, 7.821622, -1.250969], [-1.177456, 7.803175, -1.234734], [-1.205835, 7.794484, -1.235339], [-1.229314, 7.800642, -1.252429], [-1.23414, 7.818041, -1.275994]]}]},
			"R_lowerLid_C_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.674658, 5.581716, 0.144183], [-1.674658, 5.575493, 0.144183], [-1.680881, 5.575493, 0.144183], [-1.680881, 5.581716, 0.144183], [-1.674658, 5.581716, 0.144183]]}]},
			"L_upperLipSecondary_B_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_B_CTLShape", "degree": 1, "form": 0, "points": [[0.895651, 1.125795, -0.384637], [0.895651, 1.125795, -0.404637], [0.895651, 1.145795, -0.404637], [0.895651, 1.145795, -0.384637], [0.915651, 1.145795, -0.384637], [0.915651, 1.145795, -0.404637], [0.915651, 1.125795, -0.404637], [0.915651, 1.125795, -0.384637], [0.895651, 1.125795, -0.384637], [0.895651, 1.145795, -0.384637], [0.895651, 1.145795, -0.404637], [0.915651, 1.145795, -0.404637], [0.915651, 1.145795, -0.384637], [0.915651, 1.125795, -0.384637], [0.915651, 1.125795, -0.404637], [0.895651, 1.125795, -0.404637]]}]},
			"R_eye_FK_B_OFF_CTL": {"color": 8, "shapes": [{"shapeName": "R_eye_FK_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.0, 6.0, 0.5], [-2.1, 6.0, 0.4], [-2.092388, 5.961732, 0.4], [-2.0, 6.0, 0.5], [-1.9, 6.0, 0.4], [-1.907612, 6.038268, 0.4], [-2.0, 6.0, 0.5], [-2.070711, 5.929289, 0.4], [-2.038268, 5.907612, 0.4], [-2.0, 6.0, 0.5], [-1.929289, 6.070711, 0.4], [-1.961732, 6.092388, 0.4], [-2.0, 6.0, 0.5], [-2.0, 5.9, 0.4], [-1.961732, 5.907612, 0.4], [-2.0, 6.0, 0.5], [-2.0, 6.1, 0.4], [-2.038268, 6.092388, 0.4], [-2.0, 6.0, 0.5], [-1.929289, 5.929289, 0.4], [-1.907612, 5.961732, 0.4], [-2.0, 6.0, 0.5], [-2.070711, 6.070711, 0.4], [-2.092388, 6.038268, 0.4], [-2.1, 6.0, 0.4], [-2.092388, 5.961732, 0.4], [-2.070711, 5.929289, 0.4], [-2.038268, 5.907612, 0.4], [-2.0, 5.9, 0.4], [-1.961732, 5.907612, 0.4], [-1.929289, 5.929289, 0.4], [-1.907612, 5.961732, 0.4], [-1.9, 6.0, 0.4], [-1.907612, 6.038268, 0.4], [-1.929289, 6.070711, 0.4], [-1.961732, 6.092388, 0.4], [-2.0, 6.1, 0.4], [-2.038268, 6.092388, 0.4], [-2.070711, 6.070711, 0.4], [-2.092388, 6.038268, 0.4], [-2.0, 6.0, 0.5]]}]},
			"L_lowerLipSecondary_C_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.282093, -0.472611, -0.385637], [1.282093, -0.472611, -0.403637], [1.282093, -0.454611, -0.403637], [1.282093, -0.454611, -0.385637], [1.300093, -0.454611, -0.385637], [1.300093, -0.454611, -0.403637], [1.300093, -0.472611, -0.403637], [1.300093, -0.472611, -0.385637], [1.282093, -0.472611, -0.385637], [1.282093, -0.454611, -0.385637], [1.282093, -0.454611, -0.403637], [1.300093, -0.454611, -0.403637], [1.300093, -0.454611, -0.385637], [1.300093, -0.472611, -0.385637], [1.300093, -0.472611, -0.403637], [1.282093, -0.472611, -0.403637]]}]},
			"L_brow_C_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_C_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.698667, 7.817306, -1.519577], [1.66311, 7.829469, -1.5129], [1.636552, 7.822038, -1.486514], [1.63455, 7.799365, -1.455875], [1.658276, 7.774732, -1.438932], [1.693833, 7.762569, -1.445609], [1.720391, 7.77, -1.471995], [1.722393, 7.792673, -1.502634]]}]},
			"R_upperLipSecondary_D_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_D_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.643693, 0.51794, -0.385637], [-1.643693, 0.51794, -0.403637], [-1.643693, 0.53594, -0.403637], [-1.643693, 0.53594, -0.385637], [-1.661693, 0.53594, -0.385637], [-1.661693, 0.53594, -0.403637], [-1.661693, 0.51794, -0.403637], [-1.661693, 0.51794, -0.385637], [-1.643693, 0.51794, -0.385637], [-1.643693, 0.53594, -0.385637], [-1.643693, 0.53594, -0.403637], [-1.661693, 0.53594, -0.403637], [-1.661693, 0.53594, -0.385637], [-1.661693, 0.51794, -0.385637], [-1.661693, 0.51794, -0.403637], [-1.643693, 0.51794, -0.403637]]}]},
			"R_lowerLid_B_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.285733, 5.465038, 0.144183], [-1.285733, 5.458815, 0.144183], [-1.291956, 5.458815, 0.144183], [-1.291956, 5.465038, 0.144183], [-1.285733, 5.465038, 0.144183]]}]},
			"C_tongue_IK_E_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_E_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.078361, -0.078361, -0.657066], [0.110819, 0.0, -0.657066], [0.078361, 0.078361, -0.657066], [0.0, 0.110819, -0.657066], [-0.078361, 0.078361, -0.657066], [-0.110819, 0.0, -0.657066], [-0.078361, -0.078361, -0.657066], [0.0, -0.110819, -0.657066]]}]},
			"L_brow_B_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_B_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.217485, 7.836488, -1.292228], [1.189105, 7.845178, -1.291624], [1.165626, 7.83902, -1.274534], [1.160801, 7.821622, -1.250969], [1.177456, 7.803175, -1.234734], [1.205835, 7.794484, -1.235339], [1.229314, 7.800642, -1.252429], [1.23414, 7.818041, -1.275994]]}]},
			"R_lowerLid_C_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_C_CTLShape", "degree": 1, "form": 0, "points": [[-1.67227, 5.578604, 0.151961], [-1.67777, 5.573104, 0.151961], [-1.68327, 5.578604, 0.151961], [-1.67777, 5.584104, 0.151961], [-1.67227, 5.578604, 0.151961]]}]},
			"R_upperLipSecondary_A_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.469266, 1.342453, -0.388637], [-0.469266, 1.342453, -0.400637], [-0.469266, 1.354453, -0.400637], [-0.469266, 1.354453, -0.388637], [-0.481266, 1.354453, -0.388637], [-0.481266, 1.354453, -0.400637], [-0.481266, 1.342453, -0.400637], [-0.481266, 1.342453, -0.388637], [-0.469266, 1.342453, -0.388637], [-0.469266, 1.354453, -0.388637], [-0.469266, 1.354453, -0.400637], [-0.481266, 1.354453, -0.400637], [-0.481266, 1.354453, -0.388637], [-0.481266, 1.342453, -0.388637], [-0.481266, 1.342453, -0.400637], [-0.469266, 1.342453, -0.400637]]}]},
			"R_nostril_D_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "R_nostril_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-0.617542, 5.26475, -1.613724], [-0.5, 5.313437, -1.613724], [-0.382458, 5.26475, -1.613724], [-0.333771, 5.147208, -1.613724], [-0.382458, 5.029666, -1.613724], [-0.5, 4.980979, -1.613724], [-0.617542, 5.029666, -1.613724], [-0.666229, 5.147208, -1.613724]]}]},
			"L_lowerLipSecondary_A_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.467266, -0.97402, -0.386637], [0.467266, -0.97402, -0.402637], [0.467266, -0.95802, -0.402637], [0.467266, -0.95802, -0.386637], [0.483266, -0.95802, -0.386637], [0.483266, -0.95802, -0.402637], [0.483266, -0.97402, -0.402637], [0.483266, -0.97402, -0.386637], [0.467266, -0.97402, -0.386637], [0.467266, -0.95802, -0.386637], [0.467266, -0.95802, -0.402637], [0.483266, -0.95802, -0.402637], [0.483266, -0.95802, -0.386637], [0.483266, -0.97402, -0.386637], [0.483266, -0.97402, -0.402637], [0.467266, -0.97402, -0.402637]]}]},
			"R_upperLid_A_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.897586, 6.358788, 0.144183], [-0.897586, 6.354121, 0.144183], [-0.902253, 6.354121, 0.144183], [-0.902253, 6.358788, 0.144183], [-0.897586, 6.358788, 0.144183]]}]},
			"L_upperLid_A_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_A_CTLShape", "degree": 1, "form": 0, "points": [[0.89442, 6.356454, 0.151961], [0.89992, 6.350954, 0.151961], [0.90542, 6.356454, 0.151961], [0.89992, 6.361954, 0.151961], [0.89442, 6.356454, 0.151961]]}]},
			"R_lowerLid_C_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.674269, 5.582105, 0.144183], [-1.674269, 5.575104, 0.144183], [-1.68127, 5.575104, 0.144183], [-1.68127, 5.582105, 0.144183], [-1.674269, 5.582105, 0.144183]]}]},
			"L_brow_A_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_A_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.640918, 7.847857, -1.132066], [0.612625, 7.855831, -1.136212], [0.586803, 7.849127, -1.123192], [0.578577, 7.831673, -1.100632], [0.592767, 7.813693, -1.081747], [0.62106, 7.805719, -1.0776], [0.646882, 7.812423, -1.090621], [0.655108, 7.829877, -1.113181]]}]},
			"C_brow_upper_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_brow_upper_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.018, 8.097529, -1.455707], [-0.018, 8.081356, -1.423544], [0.018, 8.081356, -1.423544], [0.018, 8.097529, -1.455707], [-0.018, 8.097529, -1.455707]]}]},
			"R_squint_B_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.986628, 2.838462, -0.013372], [-1.969017, 2.867406, -0.030983], [-2.007148, 2.865386, -0.031036], [-1.986628, 2.838462, -0.013372], [-1.968964, 2.865386, 0.007148], [-1.969017, 2.867406, -0.030983], [-1.989484, 2.892311, -0.010516], [-1.968964, 2.865386, 0.007148], [-2.007094, 2.863367, 0.007094], [-1.986628, 2.838462, -0.013372], [-2.007148, 2.865386, -0.031036], [-1.989484, 2.892311, -0.010516], [-2.007094, 2.863367, 0.007094], [-2.007148, 2.865386, -0.031036]]}]},
			"L_innerLid_CTL": {"color": 6, "shapes": [{"shapeName": "L_innerLid_CTLShape", "degree": 1, "form": 0, "points": [[0.505495, 5.967529, 0.151961], [0.510995, 5.962029, 0.151961], [0.516495, 5.967529, 0.151961], [0.510995, 5.973029, 0.151961], [0.505495, 5.967529, 0.151961]]}]},
			"L_upperLid_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upperLid_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.686976, 6.473132, 0.139963], [1.686976, 6.477352, 0.144183], [1.686976, 6.473132, 0.148403], [1.686976, 6.468911, 0.144183], [1.686976, 6.473132, 0.139963], [1.691196, 6.473132, 0.144183], [1.686976, 6.473132, 0.148403], [1.682756, 6.473132, 0.144183], [1.686976, 6.477352, 0.144183], [1.691196, 6.473132, 0.144183], [1.686976, 6.468911, 0.144183], [1.682756, 6.473132, 0.144183], [1.686976, 6.473132, 0.139963], [1.691196, 6.473132, 0.144183], [1.288845, 6.473132, 0.144183]]}, {"shapeName": "L_upperLid_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.288845, 6.871263, 0.139963], [1.284625, 6.871263, 0.144183], [1.288845, 6.871263, 0.148403], [1.293065, 6.871263, 0.144183], [1.288845, 6.871263, 0.139963], [1.288845, 6.875483, 0.144183], [1.288845, 6.871263, 0.148403], [1.288845, 6.867043, 0.144183], [1.284625, 6.871263, 0.144183], [1.288845, 6.875483, 0.144183], [1.293065, 6.871263, 0.144183], [1.288845, 6.867043, 0.144183], [1.288845, 6.871263, 0.139963], [1.288845, 6.875483, 0.144183], [1.288845, 6.473132, 0.144183]]}, {"shapeName": "L_upperLid_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.288845, 6.477352, 0.542314], [1.284625, 6.473132, 0.542314], [1.288845, 6.468911, 0.542314], [1.293065, 6.473132, 0.542314], [1.288845, 6.477352, 0.542314], [1.288845, 6.473132, 0.546534], [1.288845, 6.468911, 0.542314], [1.288845, 6.473132, 0.538094], [1.284625, 6.473132, 0.542314], [1.288845, 6.473132, 0.546534], [1.293065, 6.473132, 0.542314], [1.288845, 6.473132, 0.538094], [1.288845, 6.477352, 0.542314], [1.288845, 6.473132, 0.546534], [1.288845, 6.473132, 0.144183]]}]},
			"R_upperLid_B_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.285344, 6.476632, 0.144183], [-1.285344, 6.469631, 0.144183], [-1.292345, 6.469631, 0.144183], [-1.292345, 6.476632, 0.144183], [-1.285344, 6.476632, 0.144183]]}]},
			"R_upperLipSecondary_D_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_D_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.645693, 0.51994, -0.387637], [-1.645693, 0.51994, -0.401637], [-1.645693, 0.53394, -0.401637], [-1.645693, 0.53394, -0.387637], [-1.659693, 0.53394, -0.387637], [-1.659693, 0.53394, -0.401637], [-1.659693, 0.51994, -0.401637], [-1.659693, 0.51994, -0.387637], [-1.645693, 0.51994, -0.387637], [-1.645693, 0.53394, -0.387637], [-1.645693, 0.53394, -0.401637], [-1.659693, 0.53394, -0.401637], [-1.659693, 0.53394, -0.387637], [-1.659693, 0.51994, -0.387637], [-1.659693, 0.51994, -0.401637], [-1.645693, 0.51994, -0.401637]]}]},
			"R_cheek_B_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_B_CTLShape", "degree": 3, "form": 2, "points": [[-2.137671, 2.621753, 0.082261], [-2.111896, 2.637751, 0.111896], [-2.082261, 2.621753, 0.137671], [-2.066125, 2.583131, 0.144486], [-2.07294, 2.544509, 0.128349], [-2.098714, 2.528511, 0.098714], [-2.128349, 2.544509, 0.07294], [-2.144486, 2.583131, 0.066125]]}]},
			"R_cheek_C_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_C_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.165533, 2.65449, -0.240996], [-2.146431, 2.666709, -0.21576], [-2.124382, 2.653329, -0.193719], [-2.1123, 2.622186, -0.187783], [-2.117265, 2.591525, -0.201431], [-2.136366, 2.579305, -0.226667], [-2.158416, 2.592685, -0.248708], [-2.170497, 2.623828, -0.254643]]}]},
			"R_lowerLip_A_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lowerLip_A_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.116342, -0.599617, -0.394637], [-1.102629, -0.593937, -0.394637], [-1.088915, -0.599617, -0.394637], [-1.083235, -0.61333, -0.394637], [-1.088915, -0.627043, -0.394637], [-1.102629, -0.632723, -0.394637], [-1.116342, -0.627043, -0.394637], [-1.122022, -0.61333, -0.394637]]}]},
			"C_noseTip_CTL": {"color": 20, "shapes": [{"shapeName": "C_noseTip_CTLShape", "degree": 3, "form": 2, "points": [[0.235084, 5.382292, -1.013724], [0.0, 5.479666, -1.013724], [-0.235084, 5.382292, -1.013724], [-0.332458, 5.147208, -1.013724], [-0.235084, 4.912124, -1.013724], [0.0, 4.81475, -1.013724], [0.235084, 4.912124, -1.013724], [0.332458, 5.147208, -1.013724]]}]},
			"R_squint_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_squint_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.570573, 2.839336, -0.525232], [-2.578389, 2.849295, -0.516559], [-2.584783, 2.837623, -0.508919], [-2.576968, 2.827664, -0.517593], [-2.570573, 2.839336, -0.525232], [-2.585848, 2.838284, -0.524213], [-2.584783, 2.837623, -0.508919], [-2.569508, 2.838675, -0.509938], [-2.578389, 2.849295, -0.516559], [-2.585848, 2.838284, -0.524213], [-2.576968, 2.827664, -0.517593], [-2.569508, 2.838675, -0.509938], [-2.570573, 2.839336, -0.525232], [-2.585848, 2.838284, -0.524213], [-1.806878, 2.856939, 0.156295]]}, {"shapeName": "R_squint_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.866802, 3.878106, 0.196896], [-1.865737, 3.877445, 0.21219], [-1.881012, 3.876392, 0.213209], [-1.882078, 3.877053, 0.197915], [-1.866802, 3.878106, 0.196896], [-1.874618, 3.888063, 0.205569], [-1.881012, 3.876392, 0.213209], [-1.873197, 3.866434, 0.204536], [-1.865737, 3.877445, 0.21219], [-1.874618, 3.888063, 0.205569], [-1.882078, 3.877053, 0.197915], [-1.873197, 3.866434, 0.204536], [-1.866802, 3.878106, 0.196896], [-1.874618, 3.888063, 0.205569], [-1.806878, 2.856939, 0.156295]]}, {"shapeName": "R_squint_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.477869, 2.78695, 0.92629], [-2.468988, 2.77633, 0.932911], [-2.476448, 2.765319, 0.925256], [-2.485329, 2.775939, 0.918635], [-2.477869, 2.78695, 0.92629], [-2.484263, 2.775278, 0.933929], [-2.476448, 2.765319, 0.925256], [-2.470054, 2.776991, 0.917617], [-2.468988, 2.77633, 0.932911], [-2.484263, 2.775278, 0.933929], [-2.485329, 2.775939, 0.918635], [-2.470054, 2.776991, 0.917617], [-2.477869, 2.78695, 0.92629], [-2.484263, 2.775278, 0.933929], [-1.806878, 2.856939, 0.156295]]}]},
			"L_lowerLidPrimary_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLidPrimary_CTLShape", "degree": 3, "form": 2, "points": [[1.288845, 5.470547, 0.151961], [1.282749, 5.468022, 0.151961], [1.280225, 5.461927, 0.151961], [1.282749, 5.455831, 0.151961], [1.288845, 5.453307, 0.151961], [1.29494, 5.455831, 0.151961], [1.297465, 5.461927, 0.151961], [1.29494, 5.468022, 0.151961]]}]},
			"R_brow_upper_B_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.967188, 8.093814, -1.623552], [-0.97572, 8.077964, -1.592375], [-1.010219, 8.076507, -1.602557], [-1.001687, 8.092357, -1.633734], [-0.967188, 8.093814, -1.623552]]}]},
			"L_squint_A_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.805306, 2.833018, 0.155152], [1.791163, 2.858834, 0.138255], [1.824949, 2.856506, 0.140508], [1.805306, 2.833018, 0.155152], [1.788807, 2.857372, 0.172082], [1.791163, 2.858834, 0.138255], [1.808449, 2.88086, 0.157438], [1.788807, 2.857372, 0.172082], [1.822593, 2.855045, 0.174336], [1.805306, 2.833018, 0.155152], [1.824949, 2.856506, 0.140508], [1.808449, 2.88086, 0.157438], [1.822593, 2.855045, 0.174336], [1.824949, 2.856506, 0.140508]]}]},
			"L_lowerLip_A_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lowerLip_A_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.116342, -0.599617, -0.394637], [1.102629, -0.593937, -0.394637], [1.088915, -0.599617, -0.394637], [1.083235, -0.61333, -0.394637], [1.088915, -0.627043, -0.394637], [1.102629, -0.632723, -0.394637], [1.116342, -0.627043, -0.394637], [1.122022, -0.61333, -0.394637]]}]},
			"R_lowerLipSecondary_C_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.282093, -0.472611, -0.385637], [-1.282093, -0.472611, -0.403637], [-1.282093, -0.454611, -0.403637], [-1.282093, -0.454611, -0.385637], [-1.300093, -0.454611, -0.385637], [-1.300093, -0.454611, -0.403637], [-1.300093, -0.472611, -0.403637], [-1.300093, -0.472611, -0.385637], [-1.282093, -0.472611, -0.385637], [-1.282093, -0.454611, -0.385637], [-1.282093, -0.454611, -0.403637], [-1.300093, -0.454611, -0.403637], [-1.300093, -0.454611, -0.385637], [-1.300093, -0.472611, -0.385637], [-1.300093, -0.472611, -0.403637], [-1.282093, -0.472611, -0.403637]]}]},
			"L_lowerLipSecondary_B_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.898651, -0.760362, -0.387637], [0.898651, -0.760362, -0.401637], [0.898651, -0.746362, -0.401637], [0.898651, -0.746362, -0.387637], [0.912651, -0.746362, -0.387637], [0.912651, -0.746362, -0.401637], [0.912651, -0.760362, -0.401637], [0.912651, -0.760362, -0.387637], [0.898651, -0.760362, -0.387637], [0.898651, -0.746362, -0.387637], [0.898651, -0.746362, -0.401637], [0.912651, -0.746362, -0.401637], [0.912651, -0.746362, -0.387637], [0.912651, -0.760362, -0.387637], [0.912651, -0.760362, -0.401637], [0.898651, -0.760362, -0.401637]]}]},
			"L_cheekLower_C_C_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_C_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.087936, 2.154927, -0.315593], [2.071874, 2.16544, -0.292949], [2.051925, 2.153913, -0.274229], [2.039776, 2.127099, -0.270399], [2.042542, 2.100706, -0.283702], [2.058605, 2.090193, -0.306346], [2.078553, 2.10172, -0.325066], [2.090703, 2.128534, -0.328896]]}]},
			"R_lowerLidPrimary_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLidPrimary_CTLShape", "degree": 3, "form": 2, "points": [[-1.288845, 5.470547, 0.151961], [-1.282749, 5.468022, 0.151961], [-1.280225, 5.461927, 0.151961], [-1.282749, 5.455831, 0.151961], [-1.288845, 5.453307, 0.151961], [-1.29494, 5.455831, 0.151961], [-1.297465, 5.461927, 0.151961], [-1.29494, 5.468022, 0.151961]]}]},
			"R_upperLipSecondary_D_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_D_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.644693, 0.51894, -0.386637], [-1.644693, 0.51894, -0.402637], [-1.644693, 0.53494, -0.402637], [-1.644693, 0.53494, -0.386637], [-1.660693, 0.53494, -0.386637], [-1.660693, 0.53494, -0.402637], [-1.660693, 0.51894, -0.402637], [-1.660693, 0.51894, -0.386637], [-1.644693, 0.51894, -0.386637], [-1.644693, 0.53494, -0.386637], [-1.644693, 0.53494, -0.402637], [-1.660693, 0.53494, -0.402637], [-1.660693, 0.53494, -0.386637], [-1.660693, 0.51894, -0.386637], [-1.660693, 0.51894, -0.402637], [-1.644693, 0.51894, -0.402637]]}]},
			"C_mouthAll_C_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "C_mouthAll_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.04114, 0.218643, -1.619637], [0.0, 0.230003, -1.619637], [-0.04114, 0.218643, -1.619637], [-0.05818, 0.191217, -1.619637], [-0.04114, 0.16379, -1.619637], [0.0, 0.15243, -1.619637], [0.04114, 0.16379, -1.619637], [0.05818, 0.191217, -1.619637]]}]},
			"L_cheekLower_B_C_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_B_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.913089, 2.151379, -0.125698], [1.895648, 2.162399, -0.104352], [1.874302, 2.151379, -0.086911], [1.861555, 2.124776, -0.083592], [1.864874, 2.098172, -0.096339], [1.882315, 2.087152, -0.117685], [1.903661, 2.098172, -0.135126], [1.916408, 2.124776, -0.138445]]}]},
			"L_brow_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_brow_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.576158, 7.71932, -1.965358], [2.576719, 7.734613, -1.966493], [2.583965, 7.73535, -1.952986], [2.583404, 7.720057, -1.951851], [2.576158, 7.71932, -1.965358], [2.589617, 7.726607, -1.964259], [2.583965, 7.73535, -1.952986], [2.570504, 7.728063, -1.954085], [2.576719, 7.734613, -1.966493], [2.589617, 7.726607, -1.964259], [2.583404, 7.720057, -1.951851], [2.570504, 7.728063, -1.954085], [2.576158, 7.71932, -1.965358], [2.589617, 7.726607, -1.964259], [1.678472, 7.796019, -1.479255]]}, {"shapeName": "L_brow_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.359241, 8.47464, -2.176094], [1.353587, 8.483383, -2.164821], [1.367048, 8.49067, -2.163722], [1.372701, 8.481927, -2.174995], [1.359241, 8.47464, -2.176094], [1.359802, 8.489932, -2.177228], [1.367048, 8.49067, -2.163722], [1.366487, 8.475376, -2.162587], [1.353587, 8.483383, -2.164821], [1.359802, 8.489932, -2.177228], [1.372701, 8.481927, -2.174995], [1.366487, 8.475376, -2.162587], [1.359241, 8.47464, -2.176094], [1.359802, 8.489932, -2.177228], [1.678472, 7.796019, -1.479255]]}, {"shapeName": "L_brow_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.043378, 8.559416, -0.902984], [2.037163, 8.552866, -0.890576], [2.050063, 8.54486, -0.888342], [2.056277, 8.55141, -0.90075], [2.043378, 8.559416, -0.902984], [2.050623, 8.560152, -0.889477], [2.050063, 8.54486, -0.888342], [2.042817, 8.544123, -0.901849], [2.037163, 8.552866, -0.890576], [2.050623, 8.560152, -0.889477], [2.056277, 8.55141, -0.90075], [2.042817, 8.544123, -0.901849], [2.043378, 8.559416, -0.902984], [2.050623, 8.560152, -0.889477], [1.678472, 7.796019, -1.479255]]}]},
			"C_tongue_FK_E_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_FK_E_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -1.597576], [0.0, 0.002713, -1.597576], [-0.002713, 0.0, -1.597576], [0.0, -0.002713, -1.597576], [0.002713, 0.0, -1.597576], [0.0, 0.0, -1.594864], [-0.002713, 0.0, -1.597576], [0.0, 0.0, -1.600289], [0.0, 0.002713, -1.597576], [0.0, 0.0, -1.594864], [0.0, -0.002713, -1.597576], [0.0, 0.0, -1.600289], [0.002713, 0.0, -1.597576], [0.0, 0.0, -1.594864], [0.0, 0.0, -1.853494]]}, {"shapeName": "C_tongue_FK_E_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -1.853494], [0.0, 0.255918, -1.856207], [-0.002713, 0.255918, -1.853494], [0.0, 0.255918, -1.850781], [0.002713, 0.255918, -1.853494], [0.0, 0.25863, -1.853494], [-0.002713, 0.255918, -1.853494], [0.0, 0.253205, -1.853494], [0.0, 0.255918, -1.856207], [0.0, 0.25863, -1.853494], [0.0, 0.255918, -1.850781], [0.0, 0.253205, -1.853494], [0.002713, 0.255918, -1.853494], [0.0, 0.25863, -1.853494], [0.0, 0.0, -1.853494]]}, {"shapeName": "C_tongue_FK_E_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -1.853494], [-0.255918, 0.0, -1.856207], [-0.255918, -0.002713, -1.853494], [-0.255918, 0.0, -1.850781], [-0.255918, 0.002713, -1.853494], [-0.25863, 0.0, -1.853494], [-0.255918, -0.002713, -1.853494], [-0.253205, 0.0, -1.853494], [-0.255918, 0.0, -1.856207], [-0.25863, 0.0, -1.853494], [-0.255918, 0.0, -1.850781], [-0.253205, 0.0, -1.853494], [-0.255918, 0.002713, -1.853494], [-0.25863, 0.0, -1.853494], [0.0, 0.0, -1.853494]]}]},
			"R_brow_upper_A_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.483887, 8.10444, -1.51288], [-0.488142, 8.08862, -1.480824], [-0.523773, 8.087891, -1.485913], [-0.519518, 8.103711, -1.51797], [-0.483887, 8.10444, -1.51288]]}]},
			"L_cheekLower_A_B_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_A_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.734485, 2.155947, 0.044991], [1.71313, 2.169104, 0.067836], [1.68729, 2.157074, 0.086237], [1.672101, 2.126904, 0.089415], [1.676461, 2.096267, 0.075508], [1.697816, 2.083109, 0.052662], [1.723656, 2.09514, 0.034261], [1.738845, 2.12531, 0.031083]]}]},
			"C_tongue_FK_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_tongue_FK_B_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.125, -2.924923], [0.0, 0.125951, -2.920139], [0.0, 0.128661, -2.916084], [0.0, 0.132716, -2.913374], [0.0, 0.1375, -2.912423], [0.0, 0.142284, -2.913374], [0.0, 0.146339, -2.916084], [0.0, 0.149049, -2.920139], [0.0, 0.15, -2.924923], [0.0, 0.149049, -2.929706], [0.0, 0.146339, -2.933761], [0.0, 0.142284, -2.936471], [0.0, 0.1375, -2.937423], [0.0, 0.132716, -2.936471], [0.0, 0.128661, -2.933761], [0.0, 0.125951, -2.929706], [0.0, 0.125, -2.924923], [0.0, 0.0, -2.924923]]}]},
			"L_cheekLower_A_A_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_A_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.738112, 2.159677, 0.043083], [1.714088, 2.174478, 0.068784], [1.685017, 2.160945, 0.089486], [1.66793, 2.127003, 0.093061], [1.672834, 2.092537, 0.077415], [1.696858, 2.077735, 0.051714], [1.725929, 2.091269, 0.031013], [1.743016, 2.12521, 0.027438]]}]},
			"L_lowerLipSecondary_D_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_D_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.643693, -0.153506, -0.385637], [1.643693, -0.153506, -0.403637], [1.643693, -0.135506, -0.403637], [1.643693, -0.135506, -0.385637], [1.661693, -0.135506, -0.385637], [1.661693, -0.135506, -0.403637], [1.661693, -0.153506, -0.403637], [1.661693, -0.153506, -0.385637], [1.643693, -0.153506, -0.385637], [1.643693, -0.135506, -0.385637], [1.643693, -0.135506, -0.403637], [1.661693, -0.135506, -0.403637], [1.661693, -0.135506, -0.385637], [1.661693, -0.153506, -0.385637], [1.661693, -0.153506, -0.403637], [1.643693, -0.153506, -0.403637]]}]},
			"L_outterLid_CTL": {"color": 6, "shapes": [{"shapeName": "L_outterLid_CTLShape", "degree": 1, "form": 0, "points": [[2.061195, 5.967529, 0.151961], [2.066695, 5.962029, 0.151961], [2.072195, 5.967529, 0.151961], [2.066695, 5.973029, 0.151961], [2.061195, 5.967529, 0.151961]]}]},
			"C_noseBase_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_noseBase_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.352625, 5.499833, -1.113724], [0.0, 5.645895, -1.113724], [-0.352625, 5.499833, -1.113724], [-0.498687, 5.147208, -1.113724], [-0.352625, 4.794583, -1.113724], [0.0, 4.648521, -1.113724], [0.352625, 4.794583, -1.113724], [0.498687, 5.147208, -1.113724]]}]},
			"L_innerLid_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_innerLid_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.507494, 5.97103, 0.144183], [0.507494, 5.964029, 0.144183], [0.514495, 5.964029, 0.144183], [0.514495, 5.97103, 0.144183], [0.507494, 5.97103, 0.144183]]}]},
			"R_cheekLower_A_D_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_A_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.727232, 2.148487, 0.048805], [-1.711216, 2.158354, 0.065939], [-1.691836, 2.149332, 0.07974], [-1.680444, 2.126704, 0.082123], [-1.683714, 2.103727, 0.071693], [-1.69973, 2.093859, 0.054559], [-1.71911, 2.102881, 0.040758], [-1.730502, 2.125509, 0.038375]]}]},
			"C_tongue_FK_H_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_FK_H_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -0.526148], [0.0, 0.002713, -0.526148], [-0.002713, 0.0, -0.526148], [0.0, -0.002713, -0.526148], [0.002713, 0.0, -0.526148], [0.0, 0.0, -0.523435], [-0.002713, 0.0, -0.526148], [0.0, 0.0, -0.528861], [0.0, 0.002713, -0.526148], [0.0, 0.0, -0.523435], [0.0, -0.002713, -0.526148], [0.0, 0.0, -0.528861], [0.002713, 0.0, -0.526148], [0.0, 0.0, -0.523435], [0.0, 0.0, -0.782066]]}, {"shapeName": "C_tongue_FK_H_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -0.782066], [0.0, 0.255918, -0.784778], [-0.002713, 0.255918, -0.782066], [0.0, 0.255918, -0.779353], [0.002713, 0.255918, -0.782066], [0.0, 0.25863, -0.782066], [-0.002713, 0.255918, -0.782066], [0.0, 0.253205, -0.782066], [0.0, 0.255918, -0.784778], [0.0, 0.25863, -0.782066], [0.0, 0.255918, -0.779353], [0.0, 0.253205, -0.782066], [0.002713, 0.255918, -0.782066], [0.0, 0.25863, -0.782066], [0.0, 0.0, -0.782066]]}, {"shapeName": "C_tongue_FK_H_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -0.782066], [-0.255918, 0.0, -0.784778], [-0.255918, -0.002713, -0.782066], [-0.255918, 0.0, -0.779353], [-0.255918, 0.002713, -0.782066], [-0.25863, 0.0, -0.782066], [-0.255918, -0.002713, -0.782066], [-0.253205, 0.0, -0.782066], [-0.255918, 0.0, -0.784778], [-0.25863, 0.0, -0.782066], [-0.255918, 0.0, -0.779353], [-0.253205, 0.0, -0.782066], [-0.255918, 0.002713, -0.782066], [-0.25863, 0.0, -0.782066], [0.0, 0.0, -0.782066]]}]},
			"L_cheekLower_B_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_B_CTLShape", "degree": 3, "form": 2, "points": [[2.0606, 2.114164, 0.005191], [2.035685, 2.129907, 0.035685], [2.005191, 2.114164, 0.0606], [1.98698, 2.076159, 0.065341], [1.991721, 2.038154, 0.047131], [2.016637, 2.022411, 0.016637], [2.047131, 2.038154, -0.008279], [2.065341, 2.076159, -0.01302]]}]},
			"L_squint_C_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.161031, 2.857601, -0.198376], [2.148209, 2.876822, -0.209061], [2.173583, 2.875888, -0.210869], [2.161031, 2.857601, -0.198376], [2.149956, 2.87522, -0.183716], [2.148209, 2.876822, -0.209061], [2.162507, 2.893506, -0.196209], [2.149956, 2.87522, -0.183716], [2.17533, 2.874286, -0.185524], [2.161031, 2.857601, -0.198376], [2.173583, 2.875888, -0.210869], [2.162507, 2.893506, -0.196209], [2.17533, 2.874286, -0.185524], [2.173583, 2.875888, -0.210869]]}]},
			"R_upperLidPrimary_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upperLidPrimary_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.687036, 6.473484, 0.139964], [-1.687036, 6.477704, 0.144183], [-1.687036, 6.473484, 0.148402], [-1.687036, 6.469264, 0.144183], [-1.687036, 6.473484, 0.139964], [-1.691256, 6.473484, 0.144183], [-1.687036, 6.473484, 0.148402], [-1.682817, 6.473484, 0.144183], [-1.687036, 6.477704, 0.144183], [-1.691256, 6.473484, 0.144183], [-1.687036, 6.469264, 0.144183], [-1.682817, 6.473484, 0.144183], [-1.687036, 6.473484, 0.139964], [-1.691256, 6.473484, 0.144183], [-1.288982, 6.473484, 0.144183]]}, {"shapeName": "R_upperLidPrimary_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.288982, 6.871539, 0.139964], [-1.284763, 6.871539, 0.144183], [-1.288982, 6.871539, 0.148402], [-1.293201, 6.871539, 0.144183], [-1.288982, 6.871539, 0.139964], [-1.288982, 6.875758, 0.144183], [-1.288982, 6.871539, 0.148402], [-1.288982, 6.86732, 0.144183], [-1.284763, 6.871539, 0.144183], [-1.288982, 6.875758, 0.144183], [-1.293201, 6.871539, 0.144183], [-1.288982, 6.86732, 0.144183], [-1.288982, 6.871539, 0.139964], [-1.288982, 6.875758, 0.144183], [-1.288982, 6.473484, 0.144183]]}, {"shapeName": "R_upperLidPrimary_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.288982, 6.477704, 0.542237], [-1.284763, 6.473484, 0.542237], [-1.288982, 6.469264, 0.542237], [-1.293201, 6.473484, 0.542237], [-1.288982, 6.477704, 0.542237], [-1.288982, 6.473484, 0.546456], [-1.288982, 6.469264, 0.542237], [-1.288982, 6.473484, 0.538018], [-1.284763, 6.473484, 0.542237], [-1.288982, 6.473484, 0.546456], [-1.293201, 6.473484, 0.542237], [-1.288982, 6.473484, 0.538018], [-1.288982, 6.477704, 0.542237], [-1.288982, 6.473484, 0.546456], [-1.288982, 6.473484, 0.144183]]}]},
			"L_upperLid_C_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.674269, 6.359955, 0.144183], [1.674269, 6.352954, 0.144183], [1.68127, 6.352954, 0.144183], [1.68127, 6.359955, 0.144183], [1.674269, 6.359955, 0.144183]]}]},
			"L_lowerLipSecondary_A_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.466266, -0.97502, -0.385637], [0.466266, -0.97502, -0.403637], [0.466266, -0.95702, -0.403637], [0.466266, -0.95702, -0.385637], [0.484266, -0.95702, -0.385637], [0.484266, -0.95702, -0.403637], [0.484266, -0.97502, -0.403637], [0.484266, -0.97502, -0.385637], [0.466266, -0.97502, -0.385637], [0.466266, -0.95702, -0.385637], [0.466266, -0.95702, -0.403637], [0.484266, -0.95702, -0.403637], [0.484266, -0.95702, -0.385637], [0.484266, -0.97502, -0.385637], [0.484266, -0.97502, -0.403637], [0.466266, -0.97502, -0.403637]]}]},
			"C_world_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_world_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 0.0, -0.054255], [5.118355, 0.054255, 0.0], [5.118355, 0.0, 0.054255], [5.118355, -0.054255, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [5.118355, 0.0, 0.054255], [5.0641, 0.0, 0.0], [5.118355, 0.054255, 0.0], [5.172605, 0.0, 0.0], [5.118355, -0.054255, 0.0], [5.0641, 0.0, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 5.118355, -0.054255], [-0.054255, 5.118355, 0.0], [0.0, 5.118355, 0.054255], [0.054255, 5.118355, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 5.118355, 0.054255], [0.0, 5.0641, 0.0], [-0.054255, 5.118355, 0.0], [0.0, 5.172605, 0.0], [0.054255, 5.118355, 0.0], [0.0, 5.0641, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 0.054255, 5.118355], [-0.054255, 0.0, 5.118355], [0.0, -0.054255, 5.118355], [0.054255, 0.0, 5.118355], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, -0.054255, 5.118355], [0.0, 0.0, 5.0641], [-0.054255, 0.0, 5.118355], [0.0, 0.0, 5.172605], [0.054255, 0.0, 5.118355], [0.0, 0.0, 5.0641], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, 0.0, 0.0]]}]},
			"R_brow_A_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_A_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-0.637479, 7.845417, -1.128471], [-0.613228, 7.852251, -1.132026], [-0.591094, 7.846505, -1.120865], [-0.584044, 7.831545, -1.101528], [-0.596206, 7.816133, -1.085341], [-0.620458, 7.809299, -1.081787], [-0.642591, 7.815045, -1.092947], [-0.649641, 7.830005, -1.112284]]}]},
			"R_lipCornerSecondary_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lipCornerSecondary_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.991, 0.182217, -0.385637], [-1.991, 0.182217, -0.403637], [-1.991, 0.200217, -0.403637], [-1.991, 0.200217, -0.385637], [-2.009, 0.200217, -0.385637], [-2.009, 0.200217, -0.403637], [-2.009, 0.182217, -0.403637], [-2.009, 0.182217, -0.385637], [-1.991, 0.182217, -0.385637], [-1.991, 0.200217, -0.385637], [-1.991, 0.200217, -0.403637], [-2.009, 0.200217, -0.403637], [-2.009, 0.200217, -0.385637], [-2.009, 0.182217, -0.385637], [-2.009, 0.182217, -0.403637], [-1.991, 0.182217, -0.403637]]}]},
			"R_lipCorner_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_lipCorner_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.017631, 0.208848, -0.394637], [-2.0, 0.216151, -0.394637], [-1.982369, 0.208848, -0.394637], [-1.975066, 0.191217, -0.394637], [-1.982369, 0.173585, -0.394637], [-2.0, 0.166282, -0.394637], [-2.017631, 0.173585, -0.394637], [-2.024934, 0.191217, -0.394637]]}]},
			"C_upperLip_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_upperLip_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.013713, 1.42993, -0.394637], [0.0, 1.43561, -0.394637], [-0.013713, 1.42993, -0.394637], [-0.019393, 1.416217, -0.394637], [-0.013713, 1.402503, -0.394637], [0.0, 1.396823, -0.394637], [0.013713, 1.402503, -0.394637], [0.019393, 1.416217, -0.394637]]}]},
			"L_squint_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_squint_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.704249, 2.866198, -0.74344], [2.712474, 2.876207, -0.735215], [2.719552, 2.864575, -0.728138], [2.711327, 2.854566, -0.736363], [2.704249, 2.866198, -0.74344], [2.719572, 2.865386, -0.743461], [2.719552, 2.864575, -0.728138], [2.704228, 2.865386, -0.728116], [2.712474, 2.876207, -0.735215], [2.719572, 2.865386, -0.743461], [2.711327, 2.854566, -0.736363], [2.704228, 2.865386, -0.728116], [2.704249, 2.866198, -0.74344], [2.719572, 2.865386, -0.743461], [1.988056, 2.865386, -0.011944]]}, {"shapeName": "L_squint_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.034541, 3.887002, 0.034541], [2.034519, 3.88619, 0.049865], [2.049843, 3.885379, 0.049843], [2.049865, 3.88619, 0.034519], [2.034541, 3.887002, 0.034541], [2.042766, 3.89701, 0.042766], [2.049843, 3.885379, 0.049843], [2.041618, 3.87537, 0.041618], [2.034519, 3.88619, 0.049865], [2.042766, 3.89701, 0.042766], [2.049865, 3.88619, 0.034519], [2.041618, 3.87537, 0.041618], [2.034541, 3.887002, 0.034541], [2.042766, 3.89701, 0.042766], [1.988056, 2.865386, -0.011944]]}, {"shapeName": "L_squint_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.710447, 2.799647, 0.710447], [2.7022, 2.788826, 0.717546], [2.709299, 2.778006, 0.709299], [2.717546, 2.788826, 0.7022], [2.710447, 2.799647, 0.710447], [2.717524, 2.788015, 0.717524], [2.709299, 2.778006, 0.709299], [2.702222, 2.789638, 0.702222], [2.7022, 2.788826, 0.717546], [2.717524, 2.788015, 0.717524], [2.717546, 2.788826, 0.7022], [2.702222, 2.789638, 0.702222], [2.710447, 2.799647, 0.710447], [2.717524, 2.788015, 0.717524], [1.988056, 2.865386, -0.011944]]}]},
			"C_lowerLipSecondary_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_lowerLipSecondary_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, -1.033783, -0.405488], [1.023671, -1.022932, -0.394637], [1.023671, -1.033783, -0.383786], [1.023671, -1.044634, -0.394637], [1.023671, -1.033783, -0.405488], [1.034521, -1.033783, -0.394637], [1.023671, -1.033783, -0.383786], [1.01282, -1.033783, -0.394637], [1.023671, -1.022932, -0.394637], [1.034521, -1.033783, -0.394637], [1.023671, -1.044634, -0.394637], [1.01282, -1.033783, -0.394637], [1.023671, -1.033783, -0.405488], [1.034521, -1.033783, -0.394637], [0.0, -1.033783, -0.394637]]}, {"shapeName": "C_lowerLipSecondary_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, -0.010112, -0.405488], [-0.010851, -0.010112, -0.394637], [0.0, -0.010112, -0.383786], [0.010851, -0.010112, -0.394637], [0.0, -0.010112, -0.405488], [0.0, 0.000738, -0.394637], [0.0, -0.010112, -0.383786], [0.0, -0.020963, -0.394637], [-0.010851, -0.010112, -0.394637], [0.0, 0.000738, -0.394637], [0.010851, -0.010112, -0.394637], [0.0, -0.020963, -0.394637], [0.0, -0.010112, -0.405488], [0.0, 0.000738, -0.394637], [0.0, -1.033783, -0.394637]]}, {"shapeName": "C_lowerLipSecondary_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, -1.022932, 0.629034], [-0.010851, -1.033783, 0.629034], [0.0, -1.044634, 0.629034], [0.010851, -1.033783, 0.629034], [0.0, -1.022932, 0.629034], [0.0, -1.033783, 0.639884], [0.0, -1.044634, 0.629034], [0.0, -1.033783, 0.618183], [-0.010851, -1.033783, 0.629034], [0.0, -1.033783, 0.639884], [0.010851, -1.033783, 0.629034], [0.0, -1.033783, 0.618183], [0.0, -1.022932, 0.629034], [0.0, -1.033783, 0.639884], [0.0, -1.033783, -0.394637]]}]},
			"C_tongue_IK_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_IK_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -2.276148], [0.0, 0.002713, -2.276148], [-0.002713, 0.0, -2.276148], [0.0, -0.002713, -2.276148], [0.002713, 0.0, -2.276148], [0.0, 0.0, -2.273435], [-0.002713, 0.0, -2.276148], [0.0, 0.0, -2.278861], [0.0, 0.002713, -2.276148], [0.0, 0.0, -2.273435], [0.0, -0.002713, -2.276148], [0.0, 0.0, -2.278861], [0.002713, 0.0, -2.276148], [0.0, 0.0, -2.273435], [0.0, 0.0, -2.532066]]}, {"shapeName": "C_tongue_IK_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -2.532066], [0.0, 0.255918, -2.534778], [-0.002713, 0.255918, -2.532066], [0.0, 0.255918, -2.529353], [0.002713, 0.255918, -2.532066], [0.0, 0.25863, -2.532066], [-0.002713, 0.255918, -2.532066], [0.0, 0.253205, -2.532066], [0.0, 0.255918, -2.534778], [0.0, 0.25863, -2.532066], [0.0, 0.255918, -2.529353], [0.0, 0.253205, -2.532066], [0.002713, 0.255918, -2.532066], [0.0, 0.25863, -2.532066], [0.0, 0.0, -2.532066]]}, {"shapeName": "C_tongue_IK_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -2.532066], [-0.255918, 0.0, -2.534778], [-0.255918, -0.002713, -2.532066], [-0.255918, 0.0, -2.529353], [-0.255918, 0.002713, -2.532066], [-0.25863, 0.0, -2.532066], [-0.255918, -0.002713, -2.532066], [-0.253205, 0.0, -2.532066], [-0.255918, 0.0, -2.534778], [-0.25863, 0.0, -2.532066], [-0.255918, 0.0, -2.529353], [-0.253205, 0.0, -2.532066], [-0.255918, 0.002713, -2.532066], [-0.25863, 0.0, -2.532066], [0.0, 0.0, -2.532066]]}]},
			"R_cheek_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.805279, 2.643766, -1.00022], [-2.814603, 2.652658, -0.991886], [-2.821464, 2.640155, -0.986221], [-2.81214, 2.631263, -0.994556], [-2.805279, 2.643766, -1.00022], [-2.820494, 2.642161, -1.001403], [-2.821464, 2.640155, -0.986221], [-2.806249, 2.64176, -0.985037], [-2.814603, 2.652658, -0.991886], [-2.820494, 2.642161, -1.001403], [-2.81214, 2.631263, -0.994556], [-2.806249, 2.64176, -0.985037], [-2.805279, 2.643766, -1.00022], [-2.820494, 2.642161, -1.001403], [-2.141399, 2.623007, -0.221213]]}, {"shapeName": "R_cheek_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-2.249523, 3.634038, -0.102278], [-2.250493, 3.632032, -0.087095], [-2.265708, 3.630427, -0.088279], [-2.264739, 3.632434, -0.103462], [-2.249523, 3.634038, -0.102278], [-2.258847, 3.64293, -0.093943], [-2.265708, 3.630427, -0.088279], [-2.256384, 3.621535, -0.096613], [-2.250493, 3.632032, -0.087095], [-2.258847, 3.64293, -0.093943], [-2.264739, 3.632434, -0.103462], [-2.256384, 3.621535, -0.096613], [-2.249523, 3.634038, -0.102278], [-2.258847, 3.64293, -0.093943], [-2.141399, 2.623007, -0.221213]]}, {"shapeName": "R_cheek_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.906076, 2.463391, 0.44046], [-2.897721, 2.452492, 0.447309], [-2.903612, 2.441995, 0.43779], [-2.911967, 2.452894, 0.430942], [-2.906076, 2.463391, 0.44046], [-2.912936, 2.450888, 0.446124], [-2.903612, 2.441995, 0.43779], [-2.896751, 2.454499, 0.432126], [-2.897721, 2.452492, 0.447309], [-2.912936, 2.450888, 0.446124], [-2.911967, 2.452894, 0.430942], [-2.896751, 2.454499, 0.432126], [-2.906076, 2.463391, 0.44046], [-2.912936, 2.450888, 0.446124], [-2.141399, 2.623007, -0.221213]]}]},
			"R_squint_C_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_C_CTLShape", "degree": 1, "form": 0, "points": [[-2.311212, 2.831545, -0.068334], [-2.289841, 2.863578, -0.086143], [-2.332131, 2.862022, -0.089155], [-2.311212, 2.831545, -0.068334], [-2.292752, 2.860909, -0.0439], [-2.289841, 2.863578, -0.086143], [-2.313672, 2.891385, -0.064722], [-2.292752, 2.860909, -0.0439], [-2.335042, 2.859352, -0.046913], [-2.311212, 2.831545, -0.068334], [-2.332131, 2.862022, -0.089155], [-2.313672, 2.891385, -0.064722], [-2.335042, 2.859352, -0.046913], [-2.332131, 2.862022, -0.089155]]}]},
			"R_outterLid_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_outterLid_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.063583, 5.970641, 0.144183], [-2.063583, 5.964418, 0.144183], [-2.069806, 5.964418, 0.144183], [-2.069806, 5.970641, 0.144183], [-2.063583, 5.970641, 0.144183]]}]},
			"R_lowerLipSecondary_A_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_A_CTLShape", "degree": 1, "form": 0, "points": [[-0.465266, -0.97602, -0.384637], [-0.465266, -0.97602, -0.404637], [-0.465266, -0.95602, -0.404637], [-0.465266, -0.95602, -0.384637], [-0.485266, -0.95602, -0.384637], [-0.485266, -0.95602, -0.404637], [-0.485266, -0.97602, -0.404637], [-0.485266, -0.97602, -0.384637], [-0.465266, -0.97602, -0.384637], [-0.465266, -0.95602, -0.384637], [-0.465266, -0.95602, -0.404637], [-0.485266, -0.95602, -0.404637], [-0.485266, -0.95602, -0.384637], [-0.485266, -0.97602, -0.384637], [-0.485266, -0.97602, -0.404637], [-0.465266, -0.97602, -0.404637]]}]},
			"L_lipCornerSecondary_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lipCornerSecondary_PIV_CTLShape", "degree": 1, "form": 0, "points": [[3.023671, 0.191217, -0.405488], [3.023671, 0.202068, -0.394637], [3.023671, 0.191217, -0.383786], [3.023671, 0.180366, -0.394637], [3.023671, 0.191217, -0.405488], [3.034521, 0.191217, -0.394637], [3.023671, 0.191217, -0.383786], [3.01282, 0.191217, -0.394637], [3.023671, 0.202068, -0.394637], [3.034521, 0.191217, -0.394637], [3.023671, 0.180366, -0.394637], [3.01282, 0.191217, -0.394637], [3.023671, 0.191217, -0.405488], [3.034521, 0.191217, -0.394637], [2.0, 0.191217, -0.394637]]}, {"shapeName": "L_lipCornerSecondary_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.0, 1.214888, -0.405488], [1.989149, 1.214888, -0.394637], [2.0, 1.214888, -0.383786], [2.010851, 1.214888, -0.394637], [2.0, 1.214888, -0.405488], [2.0, 1.225738, -0.394637], [2.0, 1.214888, -0.383786], [2.0, 1.204037, -0.394637], [1.989149, 1.214888, -0.394637], [2.0, 1.225738, -0.394637], [2.010851, 1.214888, -0.394637], [2.0, 1.204037, -0.394637], [2.0, 1.214888, -0.405488], [2.0, 1.225738, -0.394637], [2.0, 0.191217, -0.394637]]}, {"shapeName": "L_lipCornerSecondary_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.0, 0.202068, 0.629034], [1.989149, 0.191217, 0.629034], [2.0, 0.180366, 0.629034], [2.010851, 0.191217, 0.629034], [2.0, 0.202068, 0.629034], [2.0, 0.191217, 0.639884], [2.0, 0.180366, 0.629034], [2.0, 0.191217, 0.618183], [1.989149, 0.191217, 0.629034], [2.0, 0.191217, 0.639884], [2.010851, 0.191217, 0.629034], [2.0, 0.191217, 0.618183], [2.0, 0.202068, 0.629034], [2.0, 0.191217, 0.639884], [2.0, 0.191217, -0.394637]]}]},
			"visibility_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "visibility_CTLShape", "degree": 3, "form": 2, "points": [[1.001108, 22.568531, 0.0], [0.5, 22.970325, 0.0], [-0.001108, 22.568531, 0.0], [0.000208, 22.568531, 0.0], [-0.001108, 22.568531, 0.0], [0.5, 22.166737, 0.0], [1.001108, 22.568531, 0.0], [1.001108, 22.568531, 0.0]]}, {"shapeName": "visibility_CTLShape1", "degree": 3, "form": 2, "points": [[0.709736, 22.778267, 0.0], [0.5, 22.865142, 0.0], [0.290264, 22.778267, 0.0], [0.203389, 22.568531, 0.0], [0.290264, 22.358795, 0.0], [0.5, 22.27192, 0.0], [0.709736, 22.358795, 0.0], [0.796611, 22.568531, 0.0]]}]},
			"L_innerLid_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_innerLid_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.508661, 5.969863, 0.144183], [0.508661, 5.965196, 0.144183], [0.513328, 5.965196, 0.144183], [0.513328, 5.969863, 0.144183], [0.508661, 5.969863, 0.144183]]}]},
			"C_brow_CTL": {"color": 17, "shapes": [{"shapeName": "C_brow_CTLShape", "degree": 3, "form": 2, "points": [[0.039181, 8.002175, -0.940855], [-0.0, 8.01271, -0.9532], [-0.039181, 8.002175, -0.940855], [-0.05541, 7.976743, -0.91105], [-0.039181, 7.95131, -0.881246], [-0.0, 7.940775, -0.868901], [0.039181, 7.95131, -0.881246], [0.05541, 7.976743, -0.91105]]}]},
			"R_upperLipSecondary_D_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_D_CTLShape", "degree": 1, "form": 0, "points": [[-1.642693, 0.51694, -0.384637], [-1.642693, 0.51694, -0.404637], [-1.642693, 0.53694, -0.404637], [-1.642693, 0.53694, -0.384637], [-1.662693, 0.53694, -0.384637], [-1.662693, 0.53694, -0.404637], [-1.662693, 0.51694, -0.404637], [-1.662693, 0.51694, -0.384637], [-1.642693, 0.51694, -0.384637], [-1.642693, 0.53694, -0.384637], [-1.642693, 0.53694, -0.404637], [-1.662693, 0.53694, -0.404637], [-1.662693, 0.53694, -0.384637], [-1.662693, 0.51694, -0.384637], [-1.662693, 0.51694, -0.404637], [-1.642693, 0.51694, -0.404637]]}]},
			"R_lowerLidPrimary_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLidPrimary_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.293721, 5.466803, 0.144183], [-1.288845, 5.468823, 0.144183], [-1.283969, 5.466803, 0.144183], [-1.281949, 5.461927, 0.144183], [-1.283969, 5.45705, 0.144183], [-1.288845, 5.455031, 0.144183], [-1.293721, 5.45705, 0.144183], [-1.295741, 5.461927, 0.144183]]}]},
			"R_lowerLid_A_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.896419, 5.582105, 0.144183], [-0.896419, 5.575104, 0.144183], [-0.90342, 5.575104, 0.144183], [-0.90342, 5.582105, 0.144183], [-0.896419, 5.582105, 0.144183]]}]},
			"L_squint_C_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.160785, 2.851617, -0.198738], [2.143689, 2.877244, -0.212984], [2.177521, 2.875999, -0.215394], [2.160785, 2.851617, -0.198738], [2.146018, 2.875108, -0.179191], [2.143689, 2.877244, -0.212984], [2.162753, 2.89949, -0.195847], [2.146018, 2.875108, -0.179191], [2.17985, 2.873863, -0.181601], [2.160785, 2.851617, -0.198738], [2.177521, 2.875999, -0.215394], [2.162753, 2.89949, -0.195847], [2.17985, 2.873863, -0.181601], [2.177521, 2.875999, -0.215394]]}]},
			"L_lowerLid_B_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.286122, 5.464649, 0.144183], [1.286122, 5.459204, 0.144183], [1.291567, 5.459204, 0.144183], [1.291567, 5.464649, 0.144183], [1.286122, 5.464649, 0.144183]]}]},
			"R_brow_B_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_B_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.220344, 7.838867, -1.296335], [-1.18791, 7.848799, -1.295644], [-1.161077, 7.841762, -1.276112], [-1.155562, 7.821878, -1.249182], [-1.174597, 7.800795, -1.230628], [-1.20703, 7.790863, -1.231319], [-1.233863, 7.797901, -1.25085], [-1.239378, 7.817785, -1.277781]]}]},
			"R_lowerLid_A_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_A_CTLShape", "degree": 1, "form": 0, "points": [[-0.89442, 5.578604, 0.151961], [-0.89992, 5.573104, 0.151961], [-0.90542, 5.578604, 0.151961], [-0.89992, 5.584104, 0.151961], [-0.89442, 5.578604, 0.151961]]}]},
			"L_brow_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_brow_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.162611, 7.764373, -1.600302], [2.162922, 7.779662, -1.601579], [2.167913, 7.780769, -1.58711], [2.167602, 7.76548, -1.585833], [2.162611, 7.764373, -1.600302], [2.175519, 7.77207, -1.597206], [2.167913, 7.780769, -1.58711], [2.155003, 7.773072, -1.590206], [2.162922, 7.779662, -1.601579], [2.175519, 7.77207, -1.597206], [2.167602, 7.76548, -1.585833], [2.155003, 7.773072, -1.590206], [2.162611, 7.764373, -1.600302], [2.175519, 7.77207, -1.597206], [1.19747, 7.819831, -1.263481]]}, {"shapeName": "L_brow_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.974054, 8.480592, -2.012815], [0.966446, 8.489291, -2.002718], [0.979356, 8.496988, -1.999623], [0.986963, 8.488289, -2.009719], [0.974054, 8.480592, -2.012815], [0.974365, 8.49588, -2.014091], [0.979356, 8.496988, -1.999623], [0.979045, 8.481699, -1.998346], [0.966446, 8.489291, -2.002718], [0.974365, 8.49588, -2.014091], [0.986963, 8.488289, -2.009719], [0.979045, 8.481699, -1.998346], [0.974054, 8.480592, -2.012815], [0.974365, 8.49588, -2.014091], [1.19747, 7.819831, -1.263481]]}, {"shapeName": "L_brow_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.445219, 8.600332, -0.649105], [1.437301, 8.593742, -0.637731], [1.449899, 8.58615, -0.633358], [1.457818, 8.59274, -0.644732], [1.445219, 8.600332, -0.649105], [1.45021, 8.601439, -0.634636], [1.449899, 8.58615, -0.633358], [1.444908, 8.585043, -0.647827], [1.437301, 8.593742, -0.637731], [1.45021, 8.601439, -0.634636], [1.457818, 8.59274, -0.644732], [1.444908, 8.585043, -0.647827], [1.445219, 8.600332, -0.649105], [1.45021, 8.601439, -0.634636], [1.19747, 7.819831, -1.263481]]}]},
			"L_lowerLipSecondary_C_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.283093, -0.471611, -0.386637], [1.283093, -0.471611, -0.402637], [1.283093, -0.455611, -0.402637], [1.283093, -0.455611, -0.386637], [1.299093, -0.455611, -0.386637], [1.299093, -0.455611, -0.402637], [1.299093, -0.471611, -0.402637], [1.299093, -0.471611, -0.386637], [1.283093, -0.471611, -0.386637], [1.283093, -0.455611, -0.386637], [1.283093, -0.455611, -0.402637], [1.299093, -0.455611, -0.402637], [1.299093, -0.455611, -0.386637], [1.299093, -0.471611, -0.386637], [1.299093, -0.471611, -0.402637], [1.283093, -0.471611, -0.402637]]}]},
			"R_cheekLower_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheekLower_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.469243, 2.110335, -0.621239], [-2.478009, 2.118229, -0.611424], [-2.483027, 2.105072, -0.605324], [-2.474261, 2.097178, -0.615139], [-2.469243, 2.110335, -0.621239], [-2.484303, 2.107508, -0.62042], [-2.483027, 2.105072, -0.605324], [-2.467966, 2.107898, -0.606142], [-2.478009, 2.118229, -0.611424], [-2.484303, 2.107508, -0.62042], [-2.474261, 2.097178, -0.615139], [-2.467966, 2.107898, -0.606142], [-2.469243, 2.110335, -0.621239], [-2.484303, 2.107508, -0.62042], [-1.705473, 2.126107, 0.060249]]}, {"shapeName": "R_cheekLower_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.875416, 3.121681, 0.227497], [-1.874138, 3.119244, 0.242594], [-1.889199, 3.116418, 0.243412], [-1.890477, 3.118854, 0.228315], [-1.875416, 3.121681, 0.227497], [-1.884182, 3.129573, 0.237312], [-1.889199, 3.116418, 0.243412], [-1.880433, 3.108524, 0.233597], [-1.874138, 3.119244, 0.242594], [-1.884182, 3.129573, 0.237312], [-1.890477, 3.118854, 0.228315], [-1.880433, 3.108524, 0.233597], [-1.875416, 3.121681, 0.227497], [-1.884182, 3.129573, 0.237312], [-1.705473, 2.126107, 0.060249]]}, {"shapeName": "R_cheekLower_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.35751, 1.888381, 0.812814], [-2.347467, 1.87805, 0.818096], [-2.353762, 1.86733, 0.809099], [-2.363805, 1.87766, 0.803817], [-2.35751, 1.888381, 0.812814], [-2.362527, 1.875224, 0.818913], [-2.353762, 1.86733, 0.809099], [-2.348744, 1.880487, 0.802999], [-2.347467, 1.87805, 0.818096], [-2.362527, 1.875224, 0.818913], [-2.363805, 1.87766, 0.803817], [-2.348744, 1.880487, 0.802999], [-2.35751, 1.888381, 0.812814], [-2.362527, 1.875224, 0.818913], [-1.705473, 2.126107, 0.060249]]}]},
			"R_lowerLidPrimary_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLidPrimary_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.292502, 5.465584, 0.144183], [-1.288845, 5.467099, 0.144183], [-1.285188, 5.465584, 0.144183], [-1.283673, 5.461927, 0.144183], [-1.285188, 5.45827, 0.144183], [-1.288845, 5.456755, 0.144183], [-1.292502, 5.45827, 0.144183], [-1.294017, 5.461927, 0.144183]]}]},
			"R_lowerLid_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lowerLid_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.298186, 5.579129, 0.139964], [-1.298186, 5.583348, 0.144183], [-1.298186, 5.579129, 0.148402], [-1.298186, 5.57491, 0.144183], [-1.298186, 5.579129, 0.139964], [-1.302406, 5.579129, 0.144183], [-1.298186, 5.579129, 0.148402], [-1.293967, 5.579129, 0.144183], [-1.298186, 5.583348, 0.144183], [-1.302406, 5.579129, 0.144183], [-1.298186, 5.57491, 0.144183], [-1.293967, 5.579129, 0.144183], [-1.298186, 5.579129, 0.139964], [-1.302406, 5.579129, 0.144183], [-0.900132, 5.579129, 0.144183]]}, {"shapeName": "R_lowerLid_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.900132, 5.977183, 0.139964], [-0.895913, 5.977183, 0.144183], [-0.900132, 5.977183, 0.148402], [-0.904351, 5.977183, 0.144183], [-0.900132, 5.977183, 0.139964], [-0.900132, 5.981402, 0.144183], [-0.900132, 5.977183, 0.148402], [-0.900132, 5.972964, 0.144183], [-0.895913, 5.977183, 0.144183], [-0.900132, 5.981402, 0.144183], [-0.904351, 5.977183, 0.144183], [-0.900132, 5.972964, 0.144183], [-0.900132, 5.977183, 0.139964], [-0.900132, 5.981402, 0.144183], [-0.900132, 5.579129, 0.144183]]}, {"shapeName": "R_lowerLid_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.900132, 5.583348, 0.542237], [-0.895913, 5.579129, 0.542237], [-0.900132, 5.57491, 0.542237], [-0.904351, 5.579129, 0.542237], [-0.900132, 5.583348, 0.542237], [-0.900132, 5.579129, 0.546456], [-0.900132, 5.57491, 0.542237], [-0.900132, 5.579129, 0.538018], [-0.895913, 5.579129, 0.542237], [-0.900132, 5.579129, 0.546456], [-0.904351, 5.579129, 0.542237], [-0.900132, 5.579129, 0.538018], [-0.900132, 5.583348, 0.542237], [-0.900132, 5.579129, 0.546456], [-0.900132, 5.579129, 0.144183]]}]},
			"L_upperLidPrimary_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLidPrimary_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.293721, 6.478008, 0.144183], [1.288845, 6.480028, 0.144183], [1.283969, 6.478008, 0.144183], [1.281949, 6.473132, 0.144183], [1.283969, 6.468255, 0.144183], [1.288845, 6.466236, 0.144183], [1.293721, 6.468255, 0.144183], [1.295741, 6.473132, 0.144183]]}]},
			"L_squint_B_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_B_CTLShape", "degree": 1, "form": 0, "points": [[2.127494, 2.820512, 0.127494], [2.107927, 2.852672, 0.107927], [2.150294, 2.850428, 0.107868], [2.127494, 2.820512, 0.127494], [2.107868, 2.850428, 0.150294], [2.107927, 2.852672, 0.107927], [2.130667, 2.880344, 0.130667], [2.107868, 2.850428, 0.150294], [2.150235, 2.848185, 0.150235], [2.127494, 2.820512, 0.127494], [2.150294, 2.850428, 0.107868], [2.130667, 2.880344, 0.130667], [2.150235, 2.848185, 0.150235], [2.150294, 2.850428, 0.107868]]}]},
			"L_lowerLidPrimary_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLidPrimary_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.292502, 5.465584, 0.144183], [1.288845, 5.467099, 0.144183], [1.285188, 5.465584, 0.144183], [1.283673, 5.461927, 0.144183], [1.285188, 5.45827, 0.144183], [1.288845, 5.456755, 0.144183], [1.292502, 5.45827, 0.144183], [1.294017, 5.461927, 0.144183]]}]},
			"C_tongue_FK_H_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_tongue_FK_H_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.125, -0.782066], [0.0, 0.125951, -0.777282], [0.0, 0.128661, -0.773227], [0.0, 0.132716, -0.770517], [0.0, 0.1375, -0.769566], [0.0, 0.142284, -0.770517], [0.0, 0.146339, -0.773227], [0.0, 0.149049, -0.777282], [0.0, 0.15, -0.782066], [0.0, 0.149049, -0.786849], [0.0, 0.146339, -0.790904], [0.0, 0.142284, -0.793614], [0.0, 0.1375, -0.794566], [0.0, 0.132716, -0.793614], [0.0, 0.128661, -0.790904], [0.0, 0.125951, -0.786849], [0.0, 0.125, -0.782066], [0.0, 0.0, -0.782066]]}]},
			"L_lowerLid_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lowerLid_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.075901, 5.578604, 0.139963], [2.075901, 5.582824, 0.144183], [2.075901, 5.578604, 0.148403], [2.075901, 5.574384, 0.144183], [2.075901, 5.578604, 0.139963], [2.080121, 5.578604, 0.144183], [2.075901, 5.578604, 0.148403], [2.071681, 5.578604, 0.144183], [2.075901, 5.582824, 0.144183], [2.080121, 5.578604, 0.144183], [2.075901, 5.574384, 0.144183], [2.071681, 5.578604, 0.144183], [2.075901, 5.578604, 0.139963], [2.080121, 5.578604, 0.144183], [1.67777, 5.578604, 0.144183]]}, {"shapeName": "L_lowerLid_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.67777, 5.976735, 0.139963], [1.67355, 5.976735, 0.144183], [1.67777, 5.976735, 0.148403], [1.68199, 5.976735, 0.144183], [1.67777, 5.976735, 0.139963], [1.67777, 5.980955, 0.144183], [1.67777, 5.976735, 0.148403], [1.67777, 5.972515, 0.144183], [1.67355, 5.976735, 0.144183], [1.67777, 5.980955, 0.144183], [1.68199, 5.976735, 0.144183], [1.67777, 5.972515, 0.144183], [1.67777, 5.976735, 0.139963], [1.67777, 5.980955, 0.144183], [1.67777, 5.578604, 0.144183]]}, {"shapeName": "L_lowerLid_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.67777, 5.582824, 0.542314], [1.67355, 5.578604, 0.542314], [1.67777, 5.574384, 0.542314], [1.68199, 5.578604, 0.542314], [1.67777, 5.582824, 0.542314], [1.67777, 5.578604, 0.546534], [1.67777, 5.574384, 0.542314], [1.67777, 5.578604, 0.538094], [1.67355, 5.578604, 0.542314], [1.67777, 5.578604, 0.546534], [1.68199, 5.578604, 0.542314], [1.67777, 5.578604, 0.538094], [1.67777, 5.582824, 0.542314], [1.67777, 5.578604, 0.546534], [1.67777, 5.578604, 0.144183]]}]},
			"R_innerLid_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_innerLid_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.507883, 5.970641, 0.144183], [-0.507883, 5.964418, 0.144183], [-0.514106, 5.964418, 0.144183], [-0.514106, 5.970641, 0.144183], [-0.507883, 5.970641, 0.144183]]}]},
			"R_innerLid_CTL": {"color": 6, "shapes": [{"shapeName": "R_innerLid_CTLShape", "degree": 1, "form": 0, "points": [[-0.505495, 5.967529, 0.151961], [-0.510995, 5.962029, 0.151961], [-0.516495, 5.967529, 0.151961], [-0.510995, 5.973029, 0.151961], [-0.505495, 5.967529, 0.151961]]}]},
			"R_cheekLower_C_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_C_CTLShape", "degree": 3, "form": 2, "points": [[-2.244598, 2.118072, -0.195697], [-2.221652, 2.13309, -0.163348], [-2.193154, 2.116623, -0.136605], [-2.175797, 2.078318, -0.131133], [-2.17975, 2.040612, -0.150138], [-2.202696, 2.025594, -0.182487], [-2.231194, 2.042061, -0.20923], [-2.248551, 2.080367, -0.214702]]}]},
			"R_upperLidPrimary_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLidPrimary_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.292502, 6.476789, 0.144183], [-1.288845, 6.478304, 0.144183], [-1.285188, 6.476789, 0.144183], [-1.283673, 6.473132, 0.144183], [-1.285188, 6.469475, 0.144183], [-1.288845, 6.46796, 0.144183], [-1.292502, 6.469475, 0.144183], [-1.294017, 6.473132, 0.144183]]}]},
			"L_cheekLower_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_cheekLower_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.469243, 2.110335, -0.621239], [2.478009, 2.118229, -0.611424], [2.483027, 2.105072, -0.605324], [2.474261, 2.097178, -0.615139], [2.469243, 2.110335, -0.621239], [2.484303, 2.107508, -0.62042], [2.483027, 2.105072, -0.605324], [2.467966, 2.107898, -0.606142], [2.478009, 2.118229, -0.611424], [2.484303, 2.107508, -0.62042], [2.474261, 2.097178, -0.615139], [2.467966, 2.107898, -0.606142], [2.469243, 2.110335, -0.621239], [2.484303, 2.107508, -0.62042], [1.705473, 2.126107, 0.060249]]}, {"shapeName": "L_cheekLower_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.875416, 3.121681, 0.227497], [1.874138, 3.119244, 0.242594], [1.889199, 3.116418, 0.243412], [1.890477, 3.118854, 0.228315], [1.875416, 3.121681, 0.227497], [1.884182, 3.129573, 0.237312], [1.889199, 3.116418, 0.243412], [1.880433, 3.108524, 0.233597], [1.874138, 3.119244, 0.242594], [1.884182, 3.129573, 0.237312], [1.890477, 3.118854, 0.228315], [1.880433, 3.108524, 0.233597], [1.875416, 3.121681, 0.227497], [1.884182, 3.129573, 0.237312], [1.705473, 2.126107, 0.060249]]}, {"shapeName": "L_cheekLower_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.35751, 1.888381, 0.812814], [2.347467, 1.87805, 0.818096], [2.353762, 1.86733, 0.809099], [2.363805, 1.87766, 0.803817], [2.35751, 1.888381, 0.812814], [2.362527, 1.875224, 0.818913], [2.353762, 1.86733, 0.809099], [2.348744, 1.880487, 0.802999], [2.347467, 1.87805, 0.818096], [2.362527, 1.875224, 0.818913], [2.363805, 1.87766, 0.803817], [2.348744, 1.880487, 0.802999], [2.35751, 1.888381, 0.812814], [2.362527, 1.875224, 0.818913], [1.705473, 2.126107, 0.060249]]}]},
			"C_tongue_IK_E_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_E_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.058771, -0.058771, -0.657066], [0.083115, 0.0, -0.657066], [0.058771, 0.058771, -0.657066], [0.0, 0.083115, -0.657066], [-0.058771, 0.058771, -0.657066], [-0.083115, 0.0, -0.657066], [-0.058771, -0.058771, -0.657066], [0.0, -0.083115, -0.657066]]}]},
			"L_cheek_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_cheek_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.805279, 2.643766, -1.00022], [2.814603, 2.652658, -0.991886], [2.821464, 2.640155, -0.986221], [2.81214, 2.631263, -0.994556], [2.805279, 2.643766, -1.00022], [2.820494, 2.642161, -1.001403], [2.821464, 2.640155, -0.986221], [2.806249, 2.64176, -0.985037], [2.814603, 2.652658, -0.991886], [2.820494, 2.642161, -1.001403], [2.81214, 2.631263, -0.994556], [2.806249, 2.64176, -0.985037], [2.805279, 2.643766, -1.00022], [2.820494, 2.642161, -1.001403], [2.141399, 2.623007, -0.221213]]}, {"shapeName": "L_cheek_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.249523, 3.634038, -0.102278], [2.250493, 3.632032, -0.087095], [2.265708, 3.630427, -0.088279], [2.264739, 3.632434, -0.103462], [2.249523, 3.634038, -0.102278], [2.258847, 3.64293, -0.093943], [2.265708, 3.630427, -0.088279], [2.256384, 3.621535, -0.096613], [2.250493, 3.632032, -0.087095], [2.258847, 3.64293, -0.093943], [2.264739, 3.632434, -0.103462], [2.256384, 3.621535, -0.096613], [2.249523, 3.634038, -0.102278], [2.258847, 3.64293, -0.093943], [2.141399, 2.623007, -0.221213]]}, {"shapeName": "L_cheek_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.906076, 2.463391, 0.44046], [2.897721, 2.452492, 0.447309], [2.903612, 2.441995, 0.43779], [2.911967, 2.452894, 0.430942], [2.906076, 2.463391, 0.44046], [2.912936, 2.450888, 0.446124], [2.903612, 2.441995, 0.43779], [2.896751, 2.454499, 0.432126], [2.897721, 2.452492, 0.447309], [2.912936, 2.450888, 0.446124], [2.911967, 2.452894, 0.430942], [2.896751, 2.454499, 0.432126], [2.906076, 2.463391, 0.44046], [2.912936, 2.450888, 0.446124], [2.141399, 2.623007, -0.221213]]}]},
			"C_tongue_IK_D_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_D_CTLShape", "degree": 3, "form": 2, "points": [[0.097951, -0.097951, -1.282066], [0.138524, 0.0, -1.282066], [0.097951, 0.097951, -1.282066], [0.0, 0.138524, -1.282066], [-0.097951, 0.097951, -1.282066], [-0.138524, 0.0, -1.282066], [-0.097951, -0.097951, -1.282066], [0.0, -0.138524, -1.282066]]}]},
			"L_lowerLid_A_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.897586, 5.580938, 0.144183], [0.897586, 5.576271, 0.144183], [0.902253, 5.576271, 0.144183], [0.902253, 5.580938, 0.144183], [0.897586, 5.580938, 0.144183]]}]},
			"R_cheek_A_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_A_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.807075, 2.640209, 0.12077], [-1.787841, 2.651898, 0.140128], [-1.765776, 2.641197, 0.156857], [-1.753804, 2.614374, 0.161158], [-1.758938, 2.587143, 0.150511], [-1.778171, 2.575454, 0.131153], [-1.800237, 2.586156, 0.114424], [-1.812209, 2.612978, 0.110123]]}]},
			"R_brow_upper_B_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.95643, 8.098141, -1.6288], [-0.969228, 8.074366, -1.582035], [-1.020977, 8.07218, -1.597308], [-1.008179, 8.095955, -1.644073], [-0.95643, 8.098141, -1.6288]]}]},
			"R_cheekLower_B_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_B_CTLShape", "degree": 3, "form": 2, "points": [[-2.0606, 2.114164, 0.005191], [-2.035685, 2.129907, 0.035685], [-2.005191, 2.114164, 0.0606], [-1.98698, 2.076159, 0.065341], [-1.991721, 2.038154, 0.047131], [-2.016637, 2.022411, 0.016637], [-2.047131, 2.038154, -0.008279], [-2.065341, 2.076159, -0.01302]]}]},
			"C_tongue_IK_A_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_A_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.068566, -0.068566, -3.157066], [0.096967, 0.0, -3.157066], [0.068566, 0.068566, -3.157066], [0.0, 0.096967, -3.157066], [-0.068566, 0.068566, -3.157066], [-0.096967, 0.0, -3.157066], [-0.068566, -0.068566, -3.157066], [0.0, -0.096967, -3.157066]]}]},
			"L_lowerLipSecondary_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lowerLipSecondary_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.314764, -0.463611, -0.405488], [2.314764, -0.45276, -0.394637], [2.314764, -0.463611, -0.383786], [2.314764, -0.474462, -0.394637], [2.314764, -0.463611, -0.405488], [2.325614, -0.463611, -0.394637], [2.314764, -0.463611, -0.383786], [2.303913, -0.463611, -0.394637], [2.314764, -0.45276, -0.394637], [2.325614, -0.463611, -0.394637], [2.314764, -0.474462, -0.394637], [2.303913, -0.463611, -0.394637], [2.314764, -0.463611, -0.405488], [2.325614, -0.463611, -0.394637], [1.291093, -0.463611, -0.394637]]}, {"shapeName": "L_lowerLipSecondary_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.291093, 0.56006, -0.405488], [1.280242, 0.56006, -0.394637], [1.291093, 0.56006, -0.383786], [1.301944, 0.56006, -0.394637], [1.291093, 0.56006, -0.405488], [1.291093, 0.57091, -0.394637], [1.291093, 0.56006, -0.383786], [1.291093, 0.549209, -0.394637], [1.280242, 0.56006, -0.394637], [1.291093, 0.57091, -0.394637], [1.301944, 0.56006, -0.394637], [1.291093, 0.549209, -0.394637], [1.291093, 0.56006, -0.405488], [1.291093, 0.57091, -0.394637], [1.291093, -0.463611, -0.394637]]}, {"shapeName": "L_lowerLipSecondary_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.291093, -0.45276, 0.629034], [1.280242, -0.463611, 0.629034], [1.291093, -0.474462, 0.629034], [1.301944, -0.463611, 0.629034], [1.291093, -0.45276, 0.629034], [1.291093, -0.463611, 0.639884], [1.291093, -0.474462, 0.629034], [1.291093, -0.463611, 0.618183], [1.280242, -0.463611, 0.629034], [1.291093, -0.463611, 0.639884], [1.301944, -0.463611, 0.629034], [1.291093, -0.463611, 0.618183], [1.291093, -0.45276, 0.629034], [1.291093, -0.463611, 0.639884], [1.291093, -0.463611, -0.394637]]}]},
			"R_upperLid_B_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.285733, 6.476243, 0.144183], [-1.285733, 6.47002, 0.144183], [-1.291956, 6.47002, 0.144183], [-1.291956, 6.476243, 0.144183], [-1.285733, 6.476243, 0.144183]]}]},
			"world_B_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -462.16], [205.32, 0.0, -256.64], [153.92, 0.0, -256.64], [153.92, 0.0, -153.88], [256.68, 0.0, -153.88], [256.68, 0.0, -205.28], [462.16, 0.0, 0.0], [256.64, 0.0, 205.32], [256.64, 0.0, 153.92], [153.88, 0.0, 153.92], [153.88, 0.0, 256.68], [205.28, 0.0, 256.68], [0.0, 0.0, 462.16], [-205.32, 0.0, 256.64], [-153.92, 0.0, 256.64], [-153.92, 0.0, 153.88], [-256.68, 0.0, 153.88], [-256.68, 0.0, 205.28], [-462.16, 0.0, 0.0], [-256.64, 0.0, -205.32], [-256.64, 0.0, -153.92], [-153.88, 0.0, -153.92], [-153.88, 0.0, -256.68], [-205.28, 0.0, -256.68], [0.0, 0.0, -462.16], [40.24, 0.56, -422.64], [36.72, 0.0, -418.88], [36.72, 0.0, -403.52], [33.52, 0.0, -403.52], [33.72, 0.0, -419.0], [31.44, 0.0, -417.84], [31.52, 0.0, -411.12], [28.28, 0.0, -411.12], [28.28, 0.0, -417.84], [26.28, 0.0, -419.0], [26.28, 0.0, -403.28], [23.04, 0.0, -403.28], [23.04, 0.0, -419.4], [25.64, 0.0, -422.0], [29.64, 0.0, -420.0], [34.04, 0.0, -422.0], [36.72, 0.0, -418.96], [34.04, 0.0, -422.0], [29.68, 0.0, -420.04], [25.64, 0.0, -421.96], [17.84, 0.0, -422.0], [20.48, 0.0, -419.4], [20.48, 0.0, -405.92], [17.84, 0.0, -403.28], [9.4, 0.0, -403.28], [6.8, 0.0, -405.92], [6.8, 0.0, -419.4], [9.4, 0.0, -422.0], [17.84, 0.0, -422.0], [16.84, 0.0, -419.0], [17.24, 0.0, -406.6], [10.0, 0.0, -406.68], [10.04, 0.0, -419.0], [16.88, 0.0, -419.08], [17.84, 0.0, -422.0], [9.4, 0.0, -422.0], [4.0, 0.0, -422.0], [4.2, 0.0, -403.28], [-4.92, 0.0, -403.28], [-7.56, 0.0, -405.92], [-7.56, 0.0, -411.56], [-4.88, 0.0, -414.16], [-4.72, 0.0, -414.36], [-9.96, 0.0, -421.92], [-9.96, 0.0, -422.0], [-6.2, 0.0, -422.0], [-0.96, 0.0, -414.4], [1.0, 0.0, -414.4], [1.0, 0.0, -406.4], [-4.04, 0.0, -406.4], [-4.08, 0.0, -411.16], [1.0, 0.0, -411.16], [1.0, 0.0, -422.0], [4.0, 0.0, -422.0], [-25.72, 0.0, -422.0], [-25.72, 0.0, -419.0], [-15.24, 0.0, -418.96], [-15.24, 0.0, -403.28], [-12.0, 0.0, -403.28], [-12.0, 0.0, -422.0], [-39.36, 0.0, -422.0], [-41.76, 0.0, -419.4], [-41.96, 0.0, -405.92], [-39.36, 0.0, -403.28], [-28.28, 0.0, -403.28], [-28.28, 0.0, -422.0], [-31.56, 0.0, -419.0], [-31.48, 0.0, -406.32], [-38.32, 0.0, -406.32], [-38.24, 0.0, -418.92], [-31.44, 0.0, -419.08], [-28.2, 0.0, -422.0]]}]},
			"R_lowerLipSecondary_D_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_D_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.643693, -0.153506, -0.385637], [-1.643693, -0.153506, -0.403637], [-1.643693, -0.135506, -0.403637], [-1.643693, -0.135506, -0.385637], [-1.661693, -0.135506, -0.385637], [-1.661693, -0.135506, -0.403637], [-1.661693, -0.153506, -0.403637], [-1.661693, -0.153506, -0.385637], [-1.643693, -0.153506, -0.385637], [-1.643693, -0.135506, -0.385637], [-1.643693, -0.135506, -0.403637], [-1.661693, -0.135506, -0.403637], [-1.661693, -0.135506, -0.385637], [-1.661693, -0.153506, -0.385637], [-1.661693, -0.153506, -0.403637], [-1.643693, -0.153506, -0.403637]]}]},
			"L_lowerLidPrimary_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLidPrimary_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.294331, 5.467413, 0.144183], [1.288845, 5.469685, 0.144183], [1.283359, 5.467413, 0.144183], [1.281087, 5.461927, 0.144183], [1.283359, 5.456441, 0.144183], [1.288845, 5.454169, 0.144183], [1.294331, 5.456441, 0.144183], [1.296603, 5.461927, 0.144183]]}]},
			"L_lowerLipSecondary_B_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_B_CTLShape", "degree": 1, "form": 0, "points": [[0.895651, -0.763362, -0.384637], [0.895651, -0.763362, -0.404637], [0.895651, -0.743362, -0.404637], [0.895651, -0.743362, -0.384637], [0.915651, -0.743362, -0.384637], [0.915651, -0.743362, -0.404637], [0.915651, -0.763362, -0.404637], [0.915651, -0.763362, -0.384637], [0.895651, -0.763362, -0.384637], [0.895651, -0.743362, -0.384637], [0.895651, -0.743362, -0.404637], [0.915651, -0.743362, -0.404637], [0.915651, -0.743362, -0.384637], [0.915651, -0.763362, -0.384637], [0.915651, -0.763362, -0.404637], [0.895651, -0.763362, -0.404637]]}]},
			"L_upperLipSecondary_D_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_D_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.643693, 0.51794, -0.385637], [1.643693, 0.51794, -0.403637], [1.643693, 0.53594, -0.403637], [1.643693, 0.53594, -0.385637], [1.661693, 0.53594, -0.385637], [1.661693, 0.53594, -0.403637], [1.661693, 0.51794, -0.403637], [1.661693, 0.51794, -0.385637], [1.643693, 0.51794, -0.385637], [1.643693, 0.53594, -0.385637], [1.643693, 0.53594, -0.403637], [1.661693, 0.53594, -0.403637], [1.661693, 0.53594, -0.385637], [1.661693, 0.51794, -0.385637], [1.661693, 0.51794, -0.403637], [1.643693, 0.51794, -0.403637]]}]},
			"L_brow_upper_C_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_C_CTLShape", "degree": 1, "form": 0, "points": [[1.421832, 8.239842, -1.669392], [1.475078, 8.218129, -1.652263], [1.498771, 8.234772, -1.704815], [1.445525, 8.256486, -1.721944], [1.421832, 8.239842, -1.669392]]}]},
			"L_lowerLid_B_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_B_CTLShape", "degree": 1, "form": 0, "points": [[1.283345, 5.461927, 0.151961], [1.288845, 5.456426, 0.151961], [1.294345, 5.461927, 0.151961], [1.288845, 5.467427, 0.151961], [1.283345, 5.461927, 0.151961]]}]},
			"R_upperLipSecondary_C_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.285093, 0.840044, -0.388637], [-1.285093, 0.840044, -0.400637], [-1.285093, 0.852044, -0.400637], [-1.285093, 0.852044, -0.388637], [-1.297093, 0.852044, -0.388637], [-1.297093, 0.852044, -0.400637], [-1.297093, 0.840044, -0.400637], [-1.297093, 0.840044, -0.388637], [-1.285093, 0.840044, -0.388637], [-1.285093, 0.852044, -0.388637], [-1.285093, 0.852044, -0.400637], [-1.297093, 0.852044, -0.400637], [-1.297093, 0.852044, -0.388637], [-1.297093, 0.840044, -0.388637], [-1.297093, 0.840044, -0.400637], [-1.285093, 0.840044, -0.400637]]}]},
			"R_eye_FK_CTL": {"color": 8, "shapes": [{"shapeName": "R_eye_FK_CTLShape", "degree": 1, "form": 0, "points": [[-2.0, 6.0, 0.625], [-2.125, 6.0, 0.5], [-2.115485, 5.952165, 0.5], [-2.0, 6.0, 0.625], [-1.875, 6.0, 0.5], [-1.884515, 6.047835, 0.5], [-2.0, 6.0, 0.625], [-2.088388, 5.911612, 0.5], [-2.047836, 5.884515, 0.5], [-2.0, 6.0, 0.625], [-1.911612, 6.088388, 0.5], [-1.952165, 6.115485, 0.5], [-2.0, 6.0, 0.625], [-2.0, 5.875, 0.5], [-1.952165, 5.884515, 0.5], [-2.0, 6.0, 0.625], [-2.0, 6.125, 0.5], [-2.047836, 6.115485, 0.5], [-2.0, 6.0, 0.625], [-1.911612, 5.911612, 0.5], [-1.884515, 5.952165, 0.5], [-2.0, 6.0, 0.625], [-2.088388, 6.088388, 0.5], [-2.115485, 6.047835, 0.5], [-2.125, 6.0, 0.5], [-2.115485, 5.952165, 0.5], [-2.088388, 5.911612, 0.5], [-2.047836, 5.884515, 0.5], [-2.0, 5.875, 0.5], [-1.952165, 5.884515, 0.5], [-1.911612, 5.911612, 0.5], [-1.884515, 5.952165, 0.5], [-1.875, 6.0, 0.5], [-1.884515, 6.047835, 0.5], [-1.911612, 6.088388, 0.5], [-1.952165, 6.115485, 0.5], [-2.0, 6.125, 0.5], [-2.047836, 6.115485, 0.5], [-2.088388, 6.088388, 0.5], [-2.115485, 6.047835, 0.5], [-2.0, 6.0, 0.625]]}]},
			"L_lookAt_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lookAt_PIV_CTLShape", "degree": 1, "form": 0, "points": [[3.023671, 6.0, 2.489149], [3.023671, 6.010851, 2.5], [3.023671, 6.0, 2.510851], [3.023671, 5.989149, 2.5], [3.023671, 6.0, 2.489149], [3.034521, 6.0, 2.5], [3.023671, 6.0, 2.510851], [3.01282, 6.0, 2.5], [3.023671, 6.010851, 2.5], [3.034521, 6.0, 2.5], [3.023671, 5.989149, 2.5], [3.01282, 6.0, 2.5], [3.023671, 6.0, 2.489149], [3.034521, 6.0, 2.5], [2.0, 6.0, 2.5]]}, {"shapeName": "L_lookAt_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.0, 7.023671, 2.489149], [1.989149, 7.023671, 2.5], [2.0, 7.023671, 2.510851], [2.010851, 7.023671, 2.5], [2.0, 7.023671, 2.489149], [2.0, 7.034521, 2.5], [2.0, 7.023671, 2.510851], [2.0, 7.01282, 2.5], [1.989149, 7.023671, 2.5], [2.0, 7.034521, 2.5], [2.010851, 7.023671, 2.5], [2.0, 7.01282, 2.5], [2.0, 7.023671, 2.489149], [2.0, 7.034521, 2.5], [2.0, 6.0, 2.5]]}, {"shapeName": "L_lookAt_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.0, 6.010851, 3.523671], [1.989149, 6.0, 3.523671], [2.0, 5.989149, 3.523671], [2.010851, 6.0, 3.523671], [2.0, 6.010851, 3.523671], [2.0, 6.0, 3.534521], [2.0, 5.989149, 3.523671], [2.0, 6.0, 3.51282], [1.989149, 6.0, 3.523671], [2.0, 6.0, 3.534521], [2.010851, 6.0, 3.523671], [2.0, 6.0, 3.51282], [2.0, 6.010851, 3.523671], [2.0, 6.0, 3.534521], [2.0, 6.0, 2.5]]}]},
			"R_upperLip_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upperLip_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.1263, 0.995763, -0.405488], [-2.1263, 1.006614, -0.394637], [-2.1263, 0.995763, -0.383786], [-2.1263, 0.984912, -0.394637], [-2.1263, 0.995763, -0.405488], [-2.13715, 0.995763, -0.394637], [-2.1263, 0.995763, -0.383786], [-2.115449, 0.995763, -0.394637], [-2.1263, 1.006614, -0.394637], [-2.13715, 0.995763, -0.394637], [-2.1263, 0.984912, -0.394637], [-2.115449, 0.995763, -0.394637], [-2.1263, 0.995763, -0.405488], [-2.13715, 0.995763, -0.394637], [-1.102629, 0.995763, -0.394637]]}, {"shapeName": "R_upperLip_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.102629, 2.019434, -0.405488], [-1.091778, 2.019434, -0.394637], [-1.102629, 2.019434, -0.383786], [-1.11348, 2.019434, -0.394637], [-1.102629, 2.019434, -0.405488], [-1.102629, 2.030284, -0.394637], [-1.102629, 2.019434, -0.383786], [-1.102629, 2.008583, -0.394637], [-1.091778, 2.019434, -0.394637], [-1.102629, 2.030284, -0.394637], [-1.11348, 2.019434, -0.394637], [-1.102629, 2.008583, -0.394637], [-1.102629, 2.019434, -0.405488], [-1.102629, 2.030284, -0.394637], [-1.102629, 0.995763, -0.394637]]}, {"shapeName": "R_upperLip_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.102629, 1.006614, 0.629034], [-1.091778, 0.995763, 0.629034], [-1.102629, 0.984912, 0.629034], [-1.11348, 0.995763, 0.629034], [-1.102629, 1.006614, 0.629034], [-1.102629, 0.995763, 0.639884], [-1.102629, 0.984912, 0.629034], [-1.102629, 0.995763, 0.618183], [-1.091778, 0.995763, 0.629034], [-1.102629, 0.995763, 0.639884], [-1.11348, 0.995763, 0.629034], [-1.102629, 0.995763, 0.618183], [-1.102629, 1.006614, 0.629034], [-1.102629, 0.995763, 0.639884], [-1.102629, 0.995763, -0.394637]]}]},
			"C_lowerLipSecondary_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_lowerLipSecondary_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.006, -1.039783, -0.388637], [-0.006, -1.039783, -0.400637], [-0.006, -1.027783, -0.400637], [-0.006, -1.027783, -0.388637], [0.006, -1.027783, -0.388637], [0.006, -1.027783, -0.400637], [0.006, -1.039783, -0.400637], [0.006, -1.039783, -0.388637], [-0.006, -1.039783, -0.388637], [-0.006, -1.027783, -0.388637], [-0.006, -1.027783, -0.400637], [0.006, -1.027783, -0.400637], [0.006, -1.027783, -0.388637], [0.006, -1.039783, -0.388637], [0.006, -1.039783, -0.400637], [-0.006, -1.039783, -0.400637]]}]},
			"L_lowerLip_A_CTL": {"color": 17, "shapes": [{"shapeName": "L_lowerLip_A_CTLShape", "degree": 3, "form": 2, "points": [[1.122219, -0.61374, -0.384637], [1.102629, -0.605625, -0.384637], [1.083038, -0.61374, -0.384637], [1.074924, -0.63333, -0.384637], [1.083038, -0.65292, -0.384637], [1.102629, -0.661035, -0.384637], [1.122219, -0.65292, -0.384637], [1.130333, -0.63333, -0.384637]]}]},
			"L_brow_upper_C_B_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.382626, 8.071591, -1.774607], [1.399344, 8.049893, -1.73519], [1.442867, 8.047026, -1.755228], [1.426149, 8.068724, -1.794645], [1.382626, 8.071591, -1.774607]]}]},
			"C_tongue_IK_B_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_B_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.058771, -0.058771, -2.532066], [0.083115, 0.0, -2.532066], [0.058771, 0.058771, -2.532066], [0.0, 0.083115, -2.532066], [-0.058771, 0.058771, -2.532066], [-0.083115, 0.0, -2.532066], [-0.058771, -0.058771, -2.532066], [0.0, -0.083115, -2.532066]]}]},
			"L_lowerLipSecondary_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lowerLipSecondary_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.676364, -0.144506, -0.405488], [2.676364, -0.133655, -0.394637], [2.676364, -0.144506, -0.383786], [2.676364, -0.155357, -0.394637], [2.676364, -0.144506, -0.405488], [2.687214, -0.144506, -0.394637], [2.676364, -0.144506, -0.383786], [2.665513, -0.144506, -0.394637], [2.676364, -0.133655, -0.394637], [2.687214, -0.144506, -0.394637], [2.676364, -0.155357, -0.394637], [2.665513, -0.144506, -0.394637], [2.676364, -0.144506, -0.405488], [2.687214, -0.144506, -0.394637], [1.652693, -0.144506, -0.394637]]}, {"shapeName": "L_lowerLipSecondary_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.652693, 0.879165, -0.405488], [1.641842, 0.879165, -0.394637], [1.652693, 0.879165, -0.383786], [1.663544, 0.879165, -0.394637], [1.652693, 0.879165, -0.405488], [1.652693, 0.890015, -0.394637], [1.652693, 0.879165, -0.383786], [1.652693, 0.868314, -0.394637], [1.641842, 0.879165, -0.394637], [1.652693, 0.890015, -0.394637], [1.663544, 0.879165, -0.394637], [1.652693, 0.868314, -0.394637], [1.652693, 0.879165, -0.405488], [1.652693, 0.890015, -0.394637], [1.652693, -0.144506, -0.394637]]}, {"shapeName": "L_lowerLipSecondary_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.652693, -0.133655, 0.629034], [1.641842, -0.144506, 0.629034], [1.652693, -0.155357, 0.629034], [1.663544, -0.144506, 0.629034], [1.652693, -0.133655, 0.629034], [1.652693, -0.144506, 0.639884], [1.652693, -0.155357, 0.629034], [1.652693, -0.144506, 0.618183], [1.641842, -0.144506, 0.629034], [1.652693, -0.144506, 0.639884], [1.663544, -0.144506, 0.629034], [1.652693, -0.144506, 0.618183], [1.652693, -0.133655, 0.629034], [1.652693, -0.144506, 0.639884], [1.652693, -0.144506, -0.394637]]}]},
			"L_lowerLipSecondary_C_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.285093, -0.469611, -0.388637], [1.285093, -0.469611, -0.400637], [1.285093, -0.457611, -0.400637], [1.285093, -0.457611, -0.388637], [1.297093, -0.457611, -0.388637], [1.297093, -0.457611, -0.400637], [1.297093, -0.469611, -0.400637], [1.297093, -0.469611, -0.388637], [1.285093, -0.469611, -0.388637], [1.285093, -0.457611, -0.388637], [1.285093, -0.457611, -0.400637], [1.297093, -0.457611, -0.400637], [1.297093, -0.457611, -0.388637], [1.297093, -0.469611, -0.388637], [1.297093, -0.469611, -0.400637], [1.285093, -0.469611, -0.400637]]}]},
			"R_lowerLipSecondary_C_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.285093, -0.469611, -0.388637], [-1.285093, -0.469611, -0.400637], [-1.285093, -0.457611, -0.400637], [-1.285093, -0.457611, -0.388637], [-1.297093, -0.457611, -0.388637], [-1.297093, -0.457611, -0.400637], [-1.297093, -0.469611, -0.400637], [-1.297093, -0.469611, -0.388637], [-1.285093, -0.469611, -0.388637], [-1.285093, -0.457611, -0.388637], [-1.285093, -0.457611, -0.400637], [-1.297093, -0.457611, -0.400637], [-1.297093, -0.457611, -0.388637], [-1.297093, -0.469611, -0.388637], [-1.297093, -0.469611, -0.400637], [-1.285093, -0.469611, -0.400637]]}]},
			"L_cheekLower_A_D_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_A_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.727232, 2.148487, 0.048805], [1.711216, 2.158354, 0.065939], [1.691836, 2.149332, 0.07974], [1.680444, 2.126704, 0.082123], [1.683714, 2.103727, 0.071693], [1.69973, 2.093859, 0.054559], [1.71911, 2.102881, 0.040758], [1.730502, 2.125509, 0.038375]]}]},
			"R_lookAt_CTL": {"color": 18, "shapes": [{"shapeName": "R_lookAt_CTLShape", "degree": 3, "form": 2, "points": [[-2.195903, 6.195903, 2.5], [-2.0, 6.277049, 2.5], [-1.804097, 6.195903, 2.5], [-1.722951, 6.0, 2.5], [-1.804097, 5.804097, 2.5], [-2.0, 5.722951, 2.5], [-2.195903, 5.804097, 2.5], [-2.277048, 6.0, 2.5]]}]},
			"R_brow_upper_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_upper_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.516138, 8.065709, -1.648812], [-1.515725, 8.080222, -1.653781], [-1.517877, 8.085198, -1.639425], [-1.51829, 8.070685, -1.634456], [-1.516138, 8.065709, -1.648812], [-1.527746, 8.075234, -1.645652], [-1.517877, 8.085198, -1.639425], [-1.506268, 8.075673, -1.642584], [-1.515725, 8.080222, -1.653781], [-1.527746, 8.075234, -1.645652], [-1.51829, 8.070685, -1.634456], [-1.506268, 8.075673, -1.642584], [-1.516138, 8.065709, -1.648812], [-1.527746, 8.075234, -1.645652], [-0.50383, 8.096166, -1.499397]]}, {"shapeName": "R_brow_upper_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.381953, 8.536264, -2.415628], [-0.372083, 8.546229, -2.4094], [-0.383692, 8.555754, -2.406241], [-0.393562, 8.545789, -2.412468], [-0.381953, 8.536264, -2.415628], [-0.38154, 8.550777, -2.420596], [-0.383692, 8.555754, -2.406241], [-0.384105, 8.541241, -2.401272], [-0.372083, 8.546229, -2.4094], [-0.38154, 8.550777, -2.420596], [-0.393562, 8.545789, -2.412468], [-0.384105, 8.541241, -2.401272], [-0.381953, 8.536264, -2.415628], [-0.38154, 8.550777, -2.420596], [-0.50383, 8.096166, -1.499397]]}, {"shapeName": "R_brow_upper_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.584587, 9.020235, -1.066275], [-0.57513, 9.015686, -1.055079], [-0.587152, 9.010698, -1.046951], [-0.596609, 9.015247, -1.058147], [-0.584587, 9.020235, -1.066275], [-0.586739, 9.02521, -1.05192], [-0.587152, 9.010698, -1.046951], [-0.585, 9.005722, -1.061307], [-0.57513, 9.015686, -1.055079], [-0.586739, 9.02521, -1.05192], [-0.596609, 9.015247, -1.058147], [-0.585, 9.005722, -1.061307], [-0.584587, 9.020235, -1.066275], [-0.586739, 9.02521, -1.05192], [-0.50383, 8.096166, -1.499397]]}]},
			"R_squint_A_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.805699, 2.838998, 0.155438], [-1.795092, 2.85836, 0.142765], [-1.820432, 2.856615, 0.144455], [-1.805699, 2.838998, 0.155438], [-1.793324, 2.857264, 0.168136], [-1.795092, 2.85836, 0.142765], [-1.808057, 2.87488, 0.157153], [-1.793324, 2.857264, 0.168136], [-1.818664, 2.855518, 0.169826], [-1.805699, 2.838998, 0.155438], [-1.820432, 2.856615, 0.144455], [-1.808057, 2.87488, 0.157153], [-1.818664, 2.855518, 0.169826], [-1.820432, 2.856615, 0.144455]]}]},
			"R_cheekLower_B_C_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_B_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.913089, 2.151379, -0.125698], [-1.895648, 2.162399, -0.104352], [-1.874302, 2.151379, -0.086911], [-1.861555, 2.124776, -0.083592], [-1.864874, 2.098172, -0.096339], [-1.882315, 2.087152, -0.117685], [-1.903661, 2.098172, -0.135126], [-1.916408, 2.124776, -0.138445]]}]},
			"R_upperLid_C_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.674269, 6.359955, 0.144183], [-1.674269, 6.352954, 0.144183], [-1.68127, 6.352954, 0.144183], [-1.68127, 6.359955, 0.144183], [-1.674269, 6.359955, 0.144183]]}]},
			"R_squint_A_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.80511, 2.830028, 0.155009], [-1.789199, 2.85907, 0.136], [-1.827208, 2.856452, 0.138535], [-1.80511, 2.830028, 0.155009], [-1.786548, 2.857426, 0.174056], [-1.789199, 2.85907, 0.136], [-1.808646, 2.883851, 0.157581], [-1.786548, 2.857426, 0.174056], [-1.824557, 2.854808, 0.176591], [-1.80511, 2.830028, 0.155009], [-1.827208, 2.856452, 0.138535], [-1.808646, 2.883851, 0.157581], [-1.824557, 2.854808, 0.176591], [-1.827208, 2.856452, 0.138535]]}]},
			"R_upperLip_A_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_upperLip_A_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.118301, 1.011435, -0.394637], [-1.102629, 1.017927, -0.394637], [-1.086956, 1.011435, -0.394637], [-1.080465, 0.995763, -0.394637], [-1.086956, 0.980091, -0.394637], [-1.102629, 0.973599, -0.394637], [-1.118301, 0.980091, -0.394637], [-1.124792, 0.995763, -0.394637]]}]},
			"L_lipCorner_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lipCorner_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.017631, 0.208848, -0.394637], [2.0, 0.216151, -0.394637], [1.982369, 0.208848, -0.394637], [1.975066, 0.191217, -0.394637], [1.982369, 0.173585, -0.394637], [2.0, 0.166282, -0.394637], [2.017631, 0.173585, -0.394637], [2.024934, 0.191217, -0.394637]]}]},
			"R_upperLip_A_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_upperLip_A_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.12026, 1.013394, -0.394637], [-1.102629, 1.020698, -0.394637], [-1.084997, 1.013394, -0.394637], [-1.077694, 0.995763, -0.394637], [-1.084997, 0.978132, -0.394637], [-1.102629, 0.970829, -0.394637], [-1.12026, 0.978132, -0.394637], [-1.127563, 0.995763, -0.394637]]}]},
			"C_tongue_IK_E_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_E_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.088156, -0.088156, -0.657066], [0.124672, 0.0, -0.657066], [0.088156, 0.088156, -0.657066], [0.0, 0.124672, -0.657066], [-0.088156, 0.088156, -0.657066], [-0.124672, 0.0, -0.657066], [-0.088156, -0.088156, -0.657066], [0.0, -0.124672, -0.657066]]}]},
			"C_visibility_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_visibility_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.523671, 22.568531, -0.010851], [1.523671, 22.579382, 0.0], [1.523671, 22.568531, 0.010851], [1.523671, 22.55768, 0.0], [1.523671, 22.568531, -0.010851], [1.534521, 22.568531, 0.0], [1.523671, 22.568531, 0.010851], [1.51282, 22.568531, 0.0], [1.523671, 22.579382, 0.0], [1.534521, 22.568531, 0.0], [1.523671, 22.55768, 0.0], [1.51282, 22.568531, 0.0], [1.523671, 22.568531, -0.010851], [1.534521, 22.568531, 0.0], [0.5, 22.568531, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.5, 23.592202, -0.010851], [0.489149, 23.592202, 0.0], [0.5, 23.592202, 0.010851], [0.510851, 23.592202, 0.0], [0.5, 23.592202, -0.010851], [0.5, 23.603052, 0.0], [0.5, 23.592202, 0.010851], [0.5, 23.581351, 0.0], [0.489149, 23.592202, 0.0], [0.5, 23.603052, 0.0], [0.510851, 23.592202, 0.0], [0.5, 23.581351, 0.0], [0.5, 23.592202, -0.010851], [0.5, 23.603052, 0.0], [0.5, 22.568531, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.5, 22.579382, 1.023671], [0.489149, 22.568531, 1.023671], [0.5, 22.55768, 1.023671], [0.510851, 22.568531, 1.023671], [0.5, 22.579382, 1.023671], [0.5, 22.568531, 1.034521], [0.5, 22.55768, 1.023671], [0.5, 22.568531, 1.01282], [0.489149, 22.568531, 1.023671], [0.5, 22.568531, 1.034521], [0.510851, 22.568531, 1.023671], [0.5, 22.568531, 1.01282], [0.5, 22.579382, 1.023671], [0.5, 22.568531, 1.034521], [0.5, 22.568531, 0.0]]}]},
			"R_upperLipSecondary_C_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.283093, 0.838044, -0.386637], [-1.283093, 0.838044, -0.402637], [-1.283093, 0.854044, -0.402637], [-1.283093, 0.854044, -0.386637], [-1.299093, 0.854044, -0.386637], [-1.299093, 0.854044, -0.402637], [-1.299093, 0.838044, -0.402637], [-1.299093, 0.838044, -0.386637], [-1.283093, 0.838044, -0.386637], [-1.283093, 0.854044, -0.386637], [-1.283093, 0.854044, -0.402637], [-1.299093, 0.854044, -0.402637], [-1.299093, 0.854044, -0.386637], [-1.299093, 0.838044, -0.386637], [-1.299093, 0.838044, -0.402637], [-1.283093, 0.838044, -0.402637]]}]},
			"world_CTL": {"color": 1, "shapes": [{"shapeName": "world_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -577.7], [256.65, 0.0, -320.8], [192.4, 0.0, -320.8], [192.4, 0.0, -192.35], [320.85, 0.0, -192.35], [320.85, 0.0, -256.6], [577.7, 0.0, 0.0], [320.8, 0.0, 256.65], [320.8, 0.0, 192.4], [192.35, 0.0, 192.4], [192.35, 0.0, 320.85], [256.6, 0.0, 320.85], [0.0, 0.0, 577.7], [-256.65, 0.0, 320.8], [-192.4, 0.0, 320.8], [-192.4, 0.0, 192.35], [-320.85, 0.0, 192.35], [-320.85, 0.0, 256.6], [-577.7, 0.0, 0.0], [-320.8, 0.0, -256.65], [-320.8, 0.0, -192.4], [-192.35, 0.0, -192.4], [-192.35, 0.0, -320.85], [-256.6, 0.0, -320.85], [0.0, 0.0, -577.7], [50.3, 0.7, -528.3], [45.9, 0.0, -523.6], [45.9, 0.0, -504.4], [41.9, 0.0, -504.4], [42.15, 0.0, -523.75], [39.3, 0.0, -522.3], [39.4, 0.0, -513.9], [35.35, 0.0, -513.9], [35.35, 0.0, -522.3], [32.85, 0.0, -523.75], [32.85, 0.0, -504.1], [28.8, 0.0, -504.1], [28.8, 0.0, -524.25], [32.05, 0.0, -527.5], [37.05, 0.0, -525.0], [42.55, 0.0, -527.5], [45.9, 0.0, -523.7], [42.55, 0.0, -527.5], [37.1, 0.0, -525.05], [32.05, 0.0, -527.45], [22.3, 0.0, -527.5], [25.6, 0.0, -524.25], [25.6, 0.0, -507.4], [22.3, 0.0, -504.1], [11.75, 0.0, -504.1], [8.5, 0.0, -507.4], [8.5, 0.0, -524.25], [11.75, 0.0, -527.5], [22.3, 0.0, -527.5], [21.05, 0.0, -523.75], [21.55, 0.0, -508.25], [12.5, 0.0, -508.35], [12.55, 0.0, -523.75], [21.1, 0.0, -523.85], [22.3, 0.0, -527.5], [11.75, 0.0, -527.5], [5.0, 0.0, -527.5], [5.25, 0.0, -504.1], [-6.15, 0.0, -504.1], [-9.45, 0.0, -507.4], [-9.45, 0.0, -514.45], [-6.1, 0.0, -517.7], [-5.9, 0.0, -517.95], [-12.45, 0.0, -527.4], [-12.45, 0.0, -527.5], [-7.75, 0.0, -527.5], [-1.2, 0.0, -518.0], [1.25, 0.0, -518.0], [1.25, 0.0, -508.0], [-5.05, 0.0, -508.0], [-5.1, 0.0, -513.95], [1.25, 0.0, -513.95], [1.25, 0.0, -527.5], [5.0, 0.0, -527.5], [-32.15, 0.0, -527.5], [-32.15, 0.0, -523.75], [-19.05, 0.0, -523.7], [-19.05, 0.0, -504.1], [-15.0, 0.0, -504.1], [-15.0, 0.0, -527.5], [-49.2, 0.0, -527.5], [-52.2, 0.0, -524.25], [-52.45, 0.0, -507.4], [-49.2, 0.0, -504.1], [-35.35, 0.0, -504.1], [-35.35, 0.0, -527.5], [-39.45, 0.0, -523.75], [-39.35, 0.0, -507.9], [-47.9, 0.0, -507.9], [-47.8, 0.0, -523.65], [-39.3, 0.0, -523.85], [-35.25, 0.0, -527.5]]}]},
			"R_brow_upper_A_A_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.473915, 8.108577, -1.519622], [-0.480298, 8.084847, -1.471537], [-0.533745, 8.083754, -1.479172], [-0.527361, 8.107484, -1.527256], [-0.473915, 8.108577, -1.519622]]}]},
			"L_brow_upper_A_B_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.477239, 8.107198, -1.517375], [0.482913, 8.086105, -1.474633], [0.530421, 8.085133, -1.481419], [0.524747, 8.106227, -1.524161], [0.477239, 8.107198, -1.517375]]}]},
			"C_upperLipSecondary_CTL": {"color": 20, "shapes": [{"shapeName": "C_upperLipSecondary_CTLShape", "degree": 1, "form": 0, "points": [[-0.01, 1.406217, -0.384637], [-0.01, 1.406217, -0.404637], [-0.01, 1.426217, -0.404637], [-0.01, 1.426217, -0.384637], [0.01, 1.426217, -0.384637], [0.01, 1.426217, -0.404637], [0.01, 1.406217, -0.404637], [0.01, 1.406217, -0.384637], [-0.01, 1.406217, -0.384637], [-0.01, 1.426217, -0.384637], [-0.01, 1.426217, -0.404637], [0.01, 1.426217, -0.404637], [0.01, 1.426217, -0.384637], [0.01, 1.406217, -0.384637], [0.01, 1.406217, -0.404637], [-0.01, 1.406217, -0.404637]]}]},
			"R_brow_upper_C_D_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.390156, 8.068521, -1.772185], [-1.402695, 8.052247, -1.742622], [-1.435337, 8.050096, -1.757651], [-1.422799, 8.06637, -1.787213], [-1.390156, 8.068521, -1.772185]]}]},
			"L_upperLipSecondary_A_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.469266, 1.342453, -0.388637], [0.469266, 1.342453, -0.400637], [0.469266, 1.354453, -0.400637], [0.469266, 1.354453, -0.388637], [0.481266, 1.354453, -0.388637], [0.481266, 1.354453, -0.400637], [0.481266, 1.342453, -0.400637], [0.481266, 1.342453, -0.388637], [0.469266, 1.342453, -0.388637], [0.469266, 1.354453, -0.388637], [0.469266, 1.354453, -0.400637], [0.481266, 1.354453, -0.400637], [0.481266, 1.354453, -0.388637], [0.481266, 1.342453, -0.388637], [0.481266, 1.342453, -0.400637], [0.469266, 1.342453, -0.400637]]}]},
			"L_lowerLipSecondary_A_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.469266, -0.97202, -0.388637], [0.469266, -0.97202, -0.400637], [0.469266, -0.96002, -0.400637], [0.469266, -0.96002, -0.388637], [0.481266, -0.96002, -0.388637], [0.481266, -0.96002, -0.400637], [0.481266, -0.97202, -0.400637], [0.481266, -0.97202, -0.388637], [0.469266, -0.97202, -0.388637], [0.469266, -0.96002, -0.388637], [0.469266, -0.96002, -0.400637], [0.481266, -0.96002, -0.400637], [0.481266, -0.96002, -0.388637], [0.481266, -0.97202, -0.388637], [0.481266, -0.97202, -0.400637], [0.469266, -0.97202, -0.400637]]}]},
			"L_cheek_A_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_A_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.807075, 2.640209, 0.12077], [1.787841, 2.651898, 0.140128], [1.765776, 2.641197, 0.156857], [1.753804, 2.614374, 0.161158], [1.758938, 2.587143, 0.150511], [1.778171, 2.575454, 0.131153], [1.800237, 2.586156, 0.114424], [1.812209, 2.612978, 0.110123]]}]},
			"L_lipCornerSecondary_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lipCornerSecondary_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.991, 0.182217, -0.385637], [1.991, 0.182217, -0.403637], [1.991, 0.200217, -0.403637], [1.991, 0.200217, -0.385637], [2.009, 0.200217, -0.385637], [2.009, 0.200217, -0.403637], [2.009, 0.182217, -0.403637], [2.009, 0.182217, -0.385637], [1.991, 0.182217, -0.385637], [1.991, 0.200217, -0.385637], [1.991, 0.200217, -0.403637], [2.009, 0.200217, -0.403637], [2.009, 0.200217, -0.385637], [2.009, 0.182217, -0.385637], [2.009, 0.182217, -0.403637], [1.991, 0.182217, -0.403637]]}]},
			"L_brow_upper_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_brow_upper_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.338358, 7.988492, -2.196483], [2.337159, 8.003054, -2.201172], [2.343518, 8.007806, -2.188039], [2.344718, 7.993244, -2.18335], [2.338358, 7.988492, -2.196483], [2.350776, 7.997501, -2.196791], [2.343518, 8.007806, -2.188039], [2.331099, 7.998797, -2.187731], [2.337159, 8.003054, -2.201172], [2.350776, 7.997501, -2.196791], [2.344718, 7.993244, -2.18335], [2.331099, 7.998797, -2.187731], [2.338358, 7.988492, -2.196483], [2.350776, 7.997501, -2.196791], [1.412747, 8.059309, -1.764918]]}, {"shapeName": "L_brow_upper_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.053629, 8.512393, -2.609766], [1.04637, 8.522699, -2.601014], [1.058789, 8.531708, -2.601322], [1.066048, 8.521402, -2.610074], [1.053629, 8.512393, -2.609766], [1.05243, 8.526955, -2.614454], [1.058789, 8.531708, -2.601322], [1.059989, 8.517146, -2.596633], [1.04637, 8.522699, -2.601014], [1.05243, 8.526955, -2.614454], [1.066048, 8.521402, -2.610074], [1.059989, 8.517146, -2.596633], [1.053629, 8.512393, -2.609766], [1.05243, 8.526955, -2.614454], [1.412747, 8.059309, -1.764918]]}, {"shapeName": "L_brow_upper_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.652368, 8.975274, -1.375548], [1.646309, 8.971017, -1.362108], [1.659927, 8.965464, -1.357727], [1.665987, 8.969721, -1.371168], [1.652368, 8.975274, -1.375548], [1.658727, 8.980026, -1.362416], [1.659927, 8.965464, -1.357727], [1.653568, 8.960712, -1.370859], [1.646309, 8.971017, -1.362108], [1.658727, 8.980026, -1.362416], [1.665987, 8.969721, -1.371168], [1.653568, 8.960712, -1.370859], [1.652368, 8.975274, -1.375548], [1.658727, 8.980026, -1.362416], [1.412747, 8.059309, -1.764918]]}]},
			"L_upperLipSecondary_B_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.896651, 1.126795, -0.385637], [0.896651, 1.126795, -0.403637], [0.896651, 1.144795, -0.403637], [0.896651, 1.144795, -0.385637], [0.914651, 1.144795, -0.385637], [0.914651, 1.144795, -0.403637], [0.914651, 1.126795, -0.403637], [0.914651, 1.126795, -0.385637], [0.896651, 1.126795, -0.385637], [0.896651, 1.144795, -0.385637], [0.896651, 1.144795, -0.403637], [0.914651, 1.144795, -0.403637], [0.914651, 1.144795, -0.385637], [0.914651, 1.126795, -0.385637], [0.914651, 1.126795, -0.403637], [0.896651, 1.126795, -0.403637]]}]},
			"L_cheekLower_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_cheekLower_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.729311, 2.149375, -1.07847], [2.739139, 2.157271, -1.06972], [2.745254, 2.144115, -1.064719], [2.735426, 2.13622, -1.073468], [2.729311, 2.149375, -1.07847], [2.744406, 2.146946, -1.079776], [2.745254, 2.144115, -1.064719], [2.730159, 2.146544, -1.063412], [2.739139, 2.157271, -1.06972], [2.744406, 2.146946, -1.079776], [2.735426, 2.13622, -1.073468], [2.730159, 2.146544, -1.063412], [2.729311, 2.149375, -1.07847], [2.744406, 2.146946, -1.079776], [2.065239, 2.127817, -0.299647]]}, {"shapeName": "L_cheekLower_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.232371, 3.123415, -0.129733], [2.233219, 3.120584, -0.114674], [2.248315, 3.118155, -0.115981], [2.247467, 3.120985, -0.13104], [2.232371, 3.123415, -0.129733], [2.242199, 3.131309, -0.120983], [2.248315, 3.118155, -0.115981], [2.238487, 3.110259, -0.124731], [2.233219, 3.120584, -0.114674], [2.242199, 3.131309, -0.120983], [2.247467, 3.120985, -0.13104], [2.238487, 3.110259, -0.124731], [2.232371, 3.123415, -0.129733], [2.242199, 3.131309, -0.120983], [2.065239, 2.127817, -0.299647]]}, {"shapeName": "L_cheekLower_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.819159, 1.890233, 0.350875], [2.810179, 1.879507, 0.357184], [2.815446, 1.869182, 0.347127], [2.824426, 1.879908, 0.340819], [2.819159, 1.890233, 0.350875], [2.825274, 1.877078, 0.355877], [2.815446, 1.869182, 0.347127], [2.809331, 1.882338, 0.342126], [2.810179, 1.879507, 0.357184], [2.825274, 1.877078, 0.355877], [2.824426, 1.879908, 0.340819], [2.809331, 1.882338, 0.342126], [2.819159, 1.890233, 0.350875], [2.825274, 1.877078, 0.355877], [2.065239, 2.127817, -0.299647]]}]},
			"R_lowerLid_B_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.285344, 5.465427, 0.144183], [-1.285344, 5.458426, 0.144183], [-1.292345, 5.458426, 0.144183], [-1.292345, 5.465427, 0.144183], [-1.285344, 5.465427, 0.144183]]}]},
			"R_cheekLower_C_D_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_C_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.084694, 2.151054, -0.313315], [-2.070926, 2.160065, -0.293906], [-2.053827, 2.150185, -0.27786], [-2.043413, 2.127202, -0.274577], [-2.045785, 2.104579, -0.28598], [-2.059553, 2.095568, -0.305389], [-2.076651, 2.105448, -0.321435], [-2.087065, 2.128431, -0.324718]]}]},
			"L_cheekLower_C_A_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_C_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.094421, 2.162673, -0.320149], [2.07377, 2.17619, -0.291035], [2.048121, 2.161369, -0.266966], [2.0325, 2.126894, -0.262042], [2.036058, 2.09296, -0.279146], [2.056709, 2.079443, -0.30826], [2.082358, 2.094264, -0.332329], [2.097978, 2.128739, -0.337253]]}]},
			"L_cheek_A_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_A_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.803636, 2.636419, 0.122894], [1.787151, 2.646438, 0.139487], [1.768238, 2.637265, 0.153826], [1.757976, 2.614274, 0.157513], [1.762377, 2.590933, 0.148387], [1.778862, 2.580915, 0.131794], [1.797775, 2.590087, 0.117455], [1.808037, 2.613078, 0.113768]]}]},
			"L_cheekLower_B_B_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_B_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.916533, 2.15518, -0.127795], [1.896601, 2.167774, -0.103399], [1.872205, 2.15518, -0.083467], [1.857637, 2.124776, -0.079674], [1.86143, 2.094371, -0.094242], [1.881362, 2.081777, -0.118638], [1.905758, 2.094371, -0.13857], [1.920326, 2.124776, -0.142363]]}]},
			"L_brow_B_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_B_CTLShape", "degree": 3, "form": 2, "points": [[1.274924, 7.994732, -1.182976], [1.234382, 8.007146, -1.182112], [1.20084, 7.998349, -1.157698], [1.193946, 7.973495, -1.124035], [1.217739, 7.947141, -1.100842], [1.258281, 7.934727, -1.101706], [1.291823, 7.943523, -1.12612], [1.298716, 7.968378, -1.159784]]}]},
			"L_eye_FK_CTL": {"color": 8, "shapes": [{"shapeName": "L_eye_FK_CTLShape", "degree": 1, "form": 0, "points": [[2.0, 6.0, 0.625], [2.125, 6.0, 0.5], [2.115485, 5.952165, 0.5], [2.0, 6.0, 0.625], [1.875, 6.0, 0.5], [1.884515, 6.047835, 0.5], [2.0, 6.0, 0.625], [2.088388, 5.911612, 0.5], [2.047836, 5.884515, 0.5], [2.0, 6.0, 0.625], [1.911612, 6.088388, 0.5], [1.952165, 6.115485, 0.5], [2.0, 6.0, 0.625], [2.0, 5.875, 0.5], [1.952165, 5.884515, 0.5], [2.0, 6.0, 0.625], [2.0, 6.125, 0.5], [2.047836, 6.115485, 0.5], [2.0, 6.0, 0.625], [1.911612, 5.911612, 0.5], [1.884515, 5.952165, 0.5], [2.0, 6.0, 0.625], [2.088388, 6.088388, 0.5], [2.115485, 6.047835, 0.5], [2.125, 6.0, 0.5], [2.115485, 5.952165, 0.5], [2.088388, 5.911612, 0.5], [2.047836, 5.884515, 0.5], [2.0, 5.875, 0.5], [1.952165, 5.884515, 0.5], [1.911612, 5.911612, 0.5], [1.884515, 5.952165, 0.5], [1.875, 6.0, 0.5], [1.884515, 6.047835, 0.5], [1.911612, 6.088388, 0.5], [1.952165, 6.115485, 0.5], [2.0, 6.125, 0.5], [2.047836, 6.115485, 0.5], [2.088388, 6.088388, 0.5], [2.115485, 6.047835, 0.5], [2.0, 6.0, 0.625]]}]},
			"L_brow_upper_B_C_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.963602, 8.095256, -1.625301], [0.973556, 8.076765, -1.588928], [1.013805, 8.075065, -1.600807], [1.003851, 8.093556, -1.63718], [0.963602, 8.095256, -1.625301]]}]},
			"R_upperLip_A_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "R_upperLip_A_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.116342, 1.009476, -0.394637], [-1.102629, 1.015157, -0.394637], [-1.088915, 1.009476, -0.394637], [-1.083235, 0.995763, -0.394637], [-1.088915, 0.98205, -0.394637], [-1.102629, 0.97637, -0.394637], [-1.116342, 0.98205, -0.394637], [-1.122022, 0.995763, -0.394637]]}]},
			"C_lowerLipSecondary_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_lowerLipSecondary_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.009, -1.042783, -0.385637], [-0.009, -1.042783, -0.403637], [-0.009, -1.024783, -0.403637], [-0.009, -1.024783, -0.385637], [0.009, -1.024783, -0.385637], [0.009, -1.024783, -0.403637], [0.009, -1.042783, -0.403637], [0.009, -1.042783, -0.385637], [-0.009, -1.042783, -0.385637], [-0.009, -1.024783, -0.385637], [-0.009, -1.024783, -0.403637], [0.009, -1.024783, -0.403637], [0.009, -1.024783, -0.385637], [0.009, -1.042783, -0.385637], [0.009, -1.042783, -0.403637], [-0.009, -1.042783, -0.403637]]}]},
			"L_cheek_C_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_C_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.165533, 2.65449, -0.240996], [2.146431, 2.666709, -0.21576], [2.124382, 2.653329, -0.193719], [2.1123, 2.622186, -0.187783], [2.117265, 2.591525, -0.201431], [2.136366, 2.579305, -0.226667], [2.158416, 2.592685, -0.248708], [2.170497, 2.623828, -0.254643]]}]},
			"C_noseBase_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_noseBase_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.274264, 5.421472, -1.113724], [0.0, 5.535076, -1.113724], [-0.274264, 5.421472, -1.113724], [-0.387868, 5.147208, -1.113724], [-0.274264, 4.872944, -1.113724], [0.0, 4.75934, -1.113724], [0.274264, 4.872944, -1.113724], [0.387868, 5.147208, -1.113724]]}]},
			"L_upperLid_A_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.897586, 6.358788, 0.144183], [0.897586, 6.354121, 0.144183], [0.902253, 6.354121, 0.144183], [0.902253, 6.358788, 0.144183], [0.897586, 6.358788, 0.144183]]}]},
			"R_lowerLid_A_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.897586, 5.580938, 0.144183], [-0.897586, 5.576271, 0.144183], [-0.902253, 5.576271, 0.144183], [-0.902253, 5.580938, 0.144183], [-0.897586, 5.580938, 0.144183]]}]},
			"L_upperLipSecondary_C_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.285093, 0.840044, -0.388637], [1.285093, 0.840044, -0.400637], [1.285093, 0.852044, -0.400637], [1.285093, 0.852044, -0.388637], [1.297093, 0.852044, -0.388637], [1.297093, 0.852044, -0.400637], [1.297093, 0.840044, -0.400637], [1.297093, 0.840044, -0.388637], [1.285093, 0.840044, -0.388637], [1.285093, 0.852044, -0.388637], [1.285093, 0.852044, -0.400637], [1.297093, 0.852044, -0.400637], [1.297093, 0.852044, -0.388637], [1.297093, 0.840044, -0.388637], [1.297093, 0.840044, -0.400637], [1.285093, 0.840044, -0.400637]]}]},
			"L_nostril_CTL": {"color": 18, "shapes": [{"shapeName": "L_nostril_CTLShape", "degree": 3, "form": 2, "points": [[0.695903, 5.343111, -1.613724], [0.5, 5.424257, -1.613724], [0.304097, 5.343111, -1.613724], [0.222952, 5.147208, -1.613724], [0.304097, 4.951305, -1.613724], [0.5, 4.87016, -1.613724], [0.695903, 4.951305, -1.613724], [0.777049, 5.147208, -1.613724]]}]},
			"R_lookAt_D_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "R_lookAt_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.117542, 6.117542, 2.5], [-2.0, 6.166229, 2.5], [-1.882458, 6.117542, 2.5], [-1.833771, 6.0, 2.5], [-1.882458, 5.882458, 2.5], [-2.0, 5.833771, 2.5], [-2.117542, 5.882458, 2.5], [-2.166229, 6.0, 2.5]]}]},
			"L_squint_C_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.160908, 2.854609, -0.198557], [2.145949, 2.877033, -0.211023], [2.175552, 2.875943, -0.213132], [2.160908, 2.854609, -0.198557], [2.147987, 2.875164, -0.181453], [2.145949, 2.877033, -0.211023], [2.16263, 2.896498, -0.196028], [2.147987, 2.875164, -0.181453], [2.17759, 2.874074, -0.183562], [2.160908, 2.854609, -0.198557], [2.175552, 2.875943, -0.213132], [2.16263, 2.896498, -0.196028], [2.17759, 2.874074, -0.183562], [2.175552, 2.875943, -0.213132]]}]},
			"C_tongue_IK_C_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_C_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.078361, -0.078361, -1.907066], [0.110819, 0.0, -1.907066], [0.078361, 0.078361, -1.907066], [0.0, 0.110819, -1.907066], [-0.078361, 0.078361, -1.907066], [-0.110819, 0.0, -1.907066], [-0.078361, -0.078361, -1.907066], [0.0, -0.110819, -1.907066]]}]},
			"L_brow_upper_A_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_A_CTLShape", "degree": 1, "form": 0, "points": [[0.477867, 8.276633, -1.40689], [0.524874, 8.25713, -1.375109], [0.56185, 8.274916, -1.418886], [0.514843, 8.294418, -1.450667], [0.477867, 8.276633, -1.40689]]}]},
			"C_tongue_IK_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_IK_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -2.901148], [0.0, 0.002713, -2.901148], [-0.002713, 0.0, -2.901148], [0.0, -0.002713, -2.901148], [0.002713, 0.0, -2.901148], [0.0, 0.0, -2.898435], [-0.002713, 0.0, -2.901148], [0.0, 0.0, -2.903861], [0.0, 0.002713, -2.901148], [0.0, 0.0, -2.898435], [0.0, -0.002713, -2.901148], [0.0, 0.0, -2.903861], [0.002713, 0.0, -2.901148], [0.0, 0.0, -2.898435], [0.0, 0.0, -3.157066]]}, {"shapeName": "C_tongue_IK_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -3.157066], [0.0, 0.255918, -3.159778], [-0.002713, 0.255918, -3.157066], [0.0, 0.255918, -3.154353], [0.002713, 0.255918, -3.157066], [0.0, 0.25863, -3.157066], [-0.002713, 0.255918, -3.157066], [0.0, 0.253205, -3.157066], [0.0, 0.255918, -3.159778], [0.0, 0.25863, -3.157066], [0.0, 0.255918, -3.154353], [0.0, 0.253205, -3.157066], [0.002713, 0.255918, -3.157066], [0.0, 0.25863, -3.157066], [0.0, 0.0, -3.157066]]}, {"shapeName": "C_tongue_IK_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -3.157066], [-0.255918, 0.0, -3.159778], [-0.255918, -0.002713, -3.157066], [-0.255918, 0.0, -3.154353], [-0.255918, 0.002713, -3.157066], [-0.25863, 0.0, -3.157066], [-0.255918, -0.002713, -3.157066], [-0.253205, 0.0, -3.157066], [-0.255918, 0.0, -3.159778], [-0.25863, 0.0, -3.157066], [-0.255918, 0.0, -3.154353], [-0.253205, 0.0, -3.157066], [-0.255918, 0.002713, -3.157066], [-0.25863, 0.0, -3.157066], [0.0, 0.0, -3.157066]]}]},
			"L_upperLipSecondary_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_upperLipSecondary_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.498937, 1.348453, -0.405488], [1.498937, 1.359304, -0.394637], [1.498937, 1.348453, -0.383786], [1.498937, 1.337602, -0.394637], [1.498937, 1.348453, -0.405488], [1.509787, 1.348453, -0.394637], [1.498937, 1.348453, -0.383786], [1.488086, 1.348453, -0.394637], [1.498937, 1.359304, -0.394637], [1.509787, 1.348453, -0.394637], [1.498937, 1.337602, -0.394637], [1.488086, 1.348453, -0.394637], [1.498937, 1.348453, -0.405488], [1.509787, 1.348453, -0.394637], [0.475266, 1.348453, -0.394637]]}, {"shapeName": "L_upperLipSecondary_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.475266, 2.372124, -0.405488], [0.464415, 2.372124, -0.394637], [0.475266, 2.372124, -0.383786], [0.486117, 2.372124, -0.394637], [0.475266, 2.372124, -0.405488], [0.475266, 2.382974, -0.394637], [0.475266, 2.372124, -0.383786], [0.475266, 2.361273, -0.394637], [0.464415, 2.372124, -0.394637], [0.475266, 2.382974, -0.394637], [0.486117, 2.372124, -0.394637], [0.475266, 2.361273, -0.394637], [0.475266, 2.372124, -0.405488], [0.475266, 2.382974, -0.394637], [0.475266, 1.348453, -0.394637]]}, {"shapeName": "L_upperLipSecondary_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.475266, 1.359304, 0.629034], [0.464415, 1.348453, 0.629034], [0.475266, 1.337602, 0.629034], [0.486117, 1.348453, 0.629034], [0.475266, 1.359304, 0.629034], [0.475266, 1.348453, 0.639884], [0.475266, 1.337602, 0.629034], [0.475266, 1.348453, 0.618183], [0.464415, 1.348453, 0.629034], [0.475266, 1.348453, 0.639884], [0.486117, 1.348453, 0.629034], [0.475266, 1.348453, 0.618183], [0.475266, 1.359304, 0.629034], [0.475266, 1.348453, 0.639884], [0.475266, 1.348453, -0.394637]]}]},
			"L_lowerLipSecondary_B_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.897651, -0.761362, -0.386637], [0.897651, -0.761362, -0.402637], [0.897651, -0.745362, -0.402637], [0.897651, -0.745362, -0.386637], [0.913651, -0.745362, -0.386637], [0.913651, -0.745362, -0.402637], [0.913651, -0.761362, -0.402637], [0.913651, -0.761362, -0.386637], [0.897651, -0.761362, -0.386637], [0.897651, -0.745362, -0.386637], [0.897651, -0.745362, -0.402637], [0.913651, -0.745362, -0.402637], [0.913651, -0.745362, -0.386637], [0.913651, -0.761362, -0.386637], [0.913651, -0.761362, -0.402637], [0.897651, -0.761362, -0.402637]]}]},
			"R_innerLid_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_innerLid_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.508661, 5.969863, 0.144183], [-0.508661, 5.965196, 0.144183], [-0.513328, 5.965196, 0.144183], [-0.513328, 5.969863, 0.144183], [-0.508661, 5.969863, 0.144183]]}]},
			"L_outterLid_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_outterLid_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.063972, 5.970252, 0.144183], [2.063972, 5.964807, 0.144183], [2.069417, 5.964807, 0.144183], [2.069417, 5.970252, 0.144183], [2.063972, 5.970252, 0.144183]]}]},
			"R_upperLid_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upperLid_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.075886, 6.356829, 0.139964], [-2.075886, 6.361048, 0.144183], [-2.075886, 6.356829, 0.148402], [-2.075886, 6.35261, 0.144183], [-2.075886, 6.356829, 0.139964], [-2.080106, 6.356829, 0.144183], [-2.075886, 6.356829, 0.148402], [-2.071667, 6.356829, 0.144183], [-2.075886, 6.361048, 0.144183], [-2.080106, 6.356829, 0.144183], [-2.075886, 6.35261, 0.144183], [-2.071667, 6.356829, 0.144183], [-2.075886, 6.356829, 0.139964], [-2.080106, 6.356829, 0.144183], [-1.677832, 6.356829, 0.144183]]}, {"shapeName": "R_upperLid_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.677832, 6.754883, 0.139964], [-1.673613, 6.754883, 0.144183], [-1.677832, 6.754883, 0.148402], [-1.682051, 6.754883, 0.144183], [-1.677832, 6.754883, 0.139964], [-1.677832, 6.759102, 0.144183], [-1.677832, 6.754883, 0.148402], [-1.677832, 6.750664, 0.144183], [-1.673613, 6.754883, 0.144183], [-1.677832, 6.759102, 0.144183], [-1.682051, 6.754883, 0.144183], [-1.677832, 6.750664, 0.144183], [-1.677832, 6.754883, 0.139964], [-1.677832, 6.759102, 0.144183], [-1.677832, 6.356829, 0.144183]]}, {"shapeName": "R_upperLid_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.677832, 6.361048, 0.542237], [-1.673613, 6.356829, 0.542237], [-1.677832, 6.35261, 0.542237], [-1.682051, 6.356829, 0.542237], [-1.677832, 6.361048, 0.542237], [-1.677832, 6.356829, 0.546456], [-1.677832, 6.35261, 0.542237], [-1.677832, 6.356829, 0.538018], [-1.673613, 6.356829, 0.542237], [-1.677832, 6.356829, 0.546456], [-1.682051, 6.356829, 0.542237], [-1.677832, 6.356829, 0.538018], [-1.677832, 6.361048, 0.542237], [-1.677832, 6.356829, 0.546456], [-1.677832, 6.356829, 0.144183]]}]},
			"R_upperLid_B_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.286122, 6.475854, 0.144183], [-1.286122, 6.470409, 0.144183], [-1.291567, 6.470409, 0.144183], [-1.291567, 6.475854, 0.144183], [-1.286122, 6.475854, 0.144183]]}]},
			"R_upperLidPrimary_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLidPrimary_CTLShape", "degree": 3, "form": 2, "points": [[-1.288845, 6.481752, 0.151961], [-1.282749, 6.479227, 0.151961], [-1.280225, 6.473132, 0.151961], [-1.282749, 6.467036, 0.151961], [-1.288845, 6.464512, 0.151961], [-1.29494, 6.467036, 0.151961], [-1.297465, 6.473132, 0.151961], [-1.29494, 6.479227, 0.151961]]}]},
			"C_brow_upper_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_brow_upper_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.024, 8.100225, -1.461067], [-0.024, 8.07866, -1.418184], [0.024, 8.07866, -1.418184], [0.024, 8.100225, -1.461067], [-0.024, 8.100225, -1.461067]]}]},
			"R_lipCornerSecondary_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lipCornerSecondary_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.992, 0.183217, -0.386637], [-1.992, 0.183217, -0.402637], [-1.992, 0.199217, -0.402637], [-1.992, 0.199217, -0.386637], [-2.008, 0.199217, -0.386637], [-2.008, 0.199217, -0.402637], [-2.008, 0.183217, -0.402637], [-2.008, 0.183217, -0.386637], [-1.992, 0.183217, -0.386637], [-1.992, 0.199217, -0.386637], [-1.992, 0.199217, -0.402637], [-2.008, 0.199217, -0.402637], [-2.008, 0.199217, -0.386637], [-2.008, 0.183217, -0.386637], [-2.008, 0.183217, -0.402637], [-1.992, 0.183217, -0.402637]]}]},
			"R_cheekLower_C_B_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_C_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.091179, 2.1588, -0.317871], [-2.072822, 2.170815, -0.291992], [-2.050023, 2.157641, -0.270597], [-2.036138, 2.126997, -0.26622], [-2.0393, 2.096833, -0.281424], [-2.057657, 2.084818, -0.307303], [-2.080456, 2.097992, -0.328698], [-2.094341, 2.128636, -0.333075]]}]},
			"L_brow_B_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_B_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.220344, 7.838867, -1.296335], [1.18791, 7.848799, -1.295644], [1.161077, 7.841762, -1.276112], [1.155562, 7.821878, -1.249182], [1.174597, 7.800795, -1.230628], [1.20703, 7.790863, -1.231319], [1.233863, 7.797901, -1.25085], [1.239378, 7.817785, -1.277781]]}]},
			"R_lowerLipSecondary_B_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.898651, -0.760362, -0.387637], [-0.898651, -0.760362, -0.401637], [-0.898651, -0.746362, -0.401637], [-0.898651, -0.746362, -0.387637], [-0.912651, -0.746362, -0.387637], [-0.912651, -0.746362, -0.401637], [-0.912651, -0.760362, -0.401637], [-0.912651, -0.760362, -0.387637], [-0.898651, -0.760362, -0.387637], [-0.898651, -0.746362, -0.387637], [-0.898651, -0.746362, -0.401637], [-0.912651, -0.746362, -0.401637], [-0.912651, -0.746362, -0.387637], [-0.912651, -0.760362, -0.387637], [-0.912651, -0.760362, -0.401637], [-0.898651, -0.760362, -0.401637]]}]},
			"R_outterLid_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_outterLid_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.464736, 5.967979, 0.139964], [-2.464736, 5.972198, 0.144183], [-2.464736, 5.967979, 0.148402], [-2.464736, 5.96376, 0.144183], [-2.464736, 5.967979, 0.139964], [-2.468956, 5.967979, 0.144183], [-2.464736, 5.967979, 0.148402], [-2.460517, 5.967979, 0.144183], [-2.464736, 5.972198, 0.144183], [-2.468956, 5.967979, 0.144183], [-2.464736, 5.96376, 0.144183], [-2.460517, 5.967979, 0.144183], [-2.464736, 5.967979, 0.139964], [-2.468956, 5.967979, 0.144183], [-2.066682, 5.967979, 0.144183]]}, {"shapeName": "R_outterLid_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-2.066682, 6.366033, 0.139964], [-2.062463, 6.366033, 0.144183], [-2.066682, 6.366033, 0.148402], [-2.070901, 6.366033, 0.144183], [-2.066682, 6.366033, 0.139964], [-2.066682, 6.370252, 0.144183], [-2.066682, 6.366033, 0.148402], [-2.066682, 6.361814, 0.144183], [-2.062463, 6.366033, 0.144183], [-2.066682, 6.370252, 0.144183], [-2.070901, 6.366033, 0.144183], [-2.066682, 6.361814, 0.144183], [-2.066682, 6.366033, 0.139964], [-2.066682, 6.370252, 0.144183], [-2.066682, 5.967979, 0.144183]]}, {"shapeName": "R_outterLid_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.066682, 5.972198, 0.542237], [-2.062463, 5.967979, 0.542237], [-2.066682, 5.96376, 0.542237], [-2.070901, 5.967979, 0.542237], [-2.066682, 5.972198, 0.542237], [-2.066682, 5.967979, 0.546456], [-2.066682, 5.96376, 0.542237], [-2.066682, 5.967979, 0.538018], [-2.062463, 5.967979, 0.542237], [-2.066682, 5.967979, 0.546456], [-2.070901, 5.967979, 0.542237], [-2.066682, 5.967979, 0.538018], [-2.066682, 5.972198, 0.542237], [-2.066682, 5.967979, 0.546456], [-2.066682, 5.967979, 0.144183]]}]},
			"R_nostril_CTL": {"color": 18, "shapes": [{"shapeName": "R_nostril_CTLShape", "degree": 3, "form": 2, "points": [[-0.695903, 5.343111, -1.613724], [-0.5, 5.424257, -1.613724], [-0.304097, 5.343111, -1.613724], [-0.222952, 5.147208, -1.613724], [-0.304097, 4.951305, -1.613724], [-0.5, 4.87016, -1.613724], [-0.695903, 4.951305, -1.613724], [-0.777049, 5.147208, -1.613724]]}]},
			"world_A_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -519.93], [230.985, 0.0, -288.72], [173.16, 0.0, -288.72], [173.16, 0.0, -173.115], [288.765, 0.0, -173.115], [288.765, 0.0, -230.94], [519.93, 0.0, 0.0], [288.72, 0.0, 230.985], [288.72, 0.0, 173.16], [173.115, 0.0, 173.16], [173.115, 0.0, 288.765], [230.94, 0.0, 288.765], [0.0, 0.0, 519.93], [-230.985, 0.0, 288.72], [-173.16, 0.0, 288.72], [-173.16, 0.0, 173.115], [-288.765, 0.0, 173.115], [-288.765, 0.0, 230.94], [-519.93, 0.0, 0.0], [-288.72, 0.0, -230.985], [-288.72, 0.0, -173.16], [-173.115, 0.0, -173.16], [-173.115, 0.0, -288.765], [-230.94, 0.0, -288.765], [0.0, 0.0, -519.93], [45.27, 0.63, -475.47], [41.31, 0.0, -471.24], [41.31, 0.0, -453.96], [37.71, 0.0, -453.96], [37.935, 0.0, -471.375], [35.37, 0.0, -470.07], [35.46, 0.0, -462.51], [31.815, 0.0, -462.51], [31.815, 0.0, -470.07], [29.565, 0.0, -471.375], [29.565, 0.0, -453.69], [25.92, 0.0, -453.69], [25.92, 0.0, -471.825], [28.845, 0.0, -474.75], [33.345, 0.0, -472.5], [38.295, 0.0, -474.75], [41.31, 0.0, -471.33], [38.295, 0.0, -474.75], [33.39, 0.0, -472.545], [28.845, 0.0, -474.705], [20.07, 0.0, -474.75], [23.04, 0.0, -471.825], [23.04, 0.0, -456.66], [20.07, 0.0, -453.69], [10.575, 0.0, -453.69], [7.65, 0.0, -456.66], [7.65, 0.0, -471.825], [10.575, 0.0, -474.75], [20.07, 0.0, -474.75], [18.945, 0.0, -471.375], [19.395, 0.0, -457.425], [11.25, 0.0, -457.515], [11.295, 0.0, -471.375], [18.99, 0.0, -471.465], [20.07, 0.0, -474.75], [10.575, 0.0, -474.75], [4.5, 0.0, -474.75], [4.725, 0.0, -453.69], [-5.535, 0.0, -453.69], [-8.505, 0.0, -456.66], [-8.505, 0.0, -463.005], [-5.49, 0.0, -465.93], [-5.31, 0.0, -466.155], [-11.205, 0.0, -474.66], [-11.205, 0.0, -474.75], [-6.975, 0.0, -474.75], [-1.08, 0.0, -466.2], [1.125, 0.0, -466.2], [1.125, 0.0, -457.2], [-4.545, 0.0, -457.2], [-4.59, 0.0, -462.555], [1.125, 0.0, -462.555], [1.125, 0.0, -474.75], [4.5, 0.0, -474.75], [-28.935, 0.0, -474.75], [-28.935, 0.0, -471.375], [-17.145, 0.0, -471.33], [-17.145, 0.0, -453.69], [-13.5, 0.0, -453.69], [-13.5, 0.0, -474.75], [-44.28, 0.0, -474.75], [-46.98, 0.0, -471.825], [-47.205, 0.0, -456.66], [-44.28, 0.0, -453.69], [-31.815, 0.0, -453.69], [-31.815, 0.0, -474.75], [-35.505, 0.0, -471.375], [-35.415, 0.0, -457.11], [-43.11, 0.0, -457.11], [-43.02, 0.0, -471.285], [-35.37, 0.0, -471.465], [-31.725, 0.0, -474.75]]}]},
			"L_nostril_C_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "L_nostril_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.637132, 5.28434, -1.613724], [0.5, 5.341142, -1.613724], [0.362868, 5.28434, -1.613724], [0.306066, 5.147208, -1.613724], [0.362868, 5.010076, -1.613724], [0.5, 4.953274, -1.613724], [0.637132, 5.010076, -1.613724], [0.693934, 5.147208, -1.613724]]}]},
			"C_mouthAll_A_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "C_mouthAll_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.052894, 0.226479, -1.619637], [0.0, 0.241085, -1.619637], [-0.052894, 0.226479, -1.619637], [-0.074803, 0.191217, -1.619637], [-0.052894, 0.155954, -1.619637], [0.0, 0.141348, -1.619637], [0.052894, 0.155954, -1.619637], [0.074803, 0.191217, -1.619637]]}]},
			"R_squint_A_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.805306, 2.833018, 0.155152], [-1.791163, 2.858834, 0.138255], [-1.824949, 2.856506, 0.140508], [-1.805306, 2.833018, 0.155152], [-1.788807, 2.857372, 0.172082], [-1.791163, 2.858834, 0.138255], [-1.808449, 2.88086, 0.157438], [-1.788807, 2.857372, 0.172082], [-1.822593, 2.855045, 0.174336], [-1.805306, 2.833018, 0.155152], [-1.824949, 2.856506, 0.140508], [-1.808449, 2.88086, 0.157438], [-1.822593, 2.855045, 0.174336], [-1.824949, 2.856506, 0.140508]]}]},
			"R_lowerLipSecondary_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lowerLipSecondary_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.498937, -0.96602, -0.405488], [-1.498937, -0.955169, -0.394637], [-1.498937, -0.96602, -0.383786], [-1.498937, -0.976871, -0.394637], [-1.498937, -0.96602, -0.405488], [-1.509787, -0.96602, -0.394637], [-1.498937, -0.96602, -0.383786], [-1.488086, -0.96602, -0.394637], [-1.498937, -0.955169, -0.394637], [-1.509787, -0.96602, -0.394637], [-1.498937, -0.976871, -0.394637], [-1.488086, -0.96602, -0.394637], [-1.498937, -0.96602, -0.405488], [-1.509787, -0.96602, -0.394637], [-0.475266, -0.96602, -0.394637]]}, {"shapeName": "R_lowerLipSecondary_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.475266, 0.057651, -0.405488], [-0.464415, 0.057651, -0.394637], [-0.475266, 0.057651, -0.383786], [-0.486117, 0.057651, -0.394637], [-0.475266, 0.057651, -0.405488], [-0.475266, 0.068501, -0.394637], [-0.475266, 0.057651, -0.383786], [-0.475266, 0.0468, -0.394637], [-0.464415, 0.057651, -0.394637], [-0.475266, 0.068501, -0.394637], [-0.486117, 0.057651, -0.394637], [-0.475266, 0.0468, -0.394637], [-0.475266, 0.057651, -0.405488], [-0.475266, 0.068501, -0.394637], [-0.475266, -0.96602, -0.394637]]}, {"shapeName": "R_lowerLipSecondary_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.475266, -0.955169, 0.629034], [-0.464415, -0.96602, 0.629034], [-0.475266, -0.976871, 0.629034], [-0.486117, -0.96602, 0.629034], [-0.475266, -0.955169, 0.629034], [-0.475266, -0.96602, 0.639884], [-0.475266, -0.976871, 0.629034], [-0.475266, -0.96602, 0.618183], [-0.464415, -0.96602, 0.629034], [-0.475266, -0.96602, 0.639884], [-0.486117, -0.96602, 0.629034], [-0.475266, -0.96602, 0.618183], [-0.475266, -0.955169, 0.629034], [-0.475266, -0.96602, 0.639884], [-0.475266, -0.96602, -0.394637]]}]},
			"world_C_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -404.39], [179.655, 0.0, -224.56], [134.68, 0.0, -224.56], [134.68, 0.0, -134.645], [224.595, 0.0, -134.645], [224.595, 0.0, -179.62], [404.39, 0.0, 0.0], [224.56, 0.0, 179.655], [224.56, 0.0, 134.68], [134.645, 0.0, 134.68], [134.645, 0.0, 224.595], [179.62, 0.0, 224.595], [0.0, 0.0, 404.39], [-179.655, 0.0, 224.56], [-134.68, 0.0, 224.56], [-134.68, 0.0, 134.645], [-224.595, 0.0, 134.645], [-224.595, 0.0, 179.62], [-404.39, 0.0, 0.0], [-224.56, 0.0, -179.655], [-224.56, 0.0, -134.68], [-134.645, 0.0, -134.68], [-134.645, 0.0, -224.595], [-179.62, 0.0, -224.595], [0.0, 0.0, -404.39], [35.21, 0.49, -369.81], [32.13, 0.0, -366.52], [32.13, 0.0, -353.08], [29.33, 0.0, -353.08], [29.505, 0.0, -366.625], [27.51, 0.0, -365.61], [27.58, 0.0, -359.73], [24.745, 0.0, -359.73], [24.745, 0.0, -365.61], [22.995, 0.0, -366.625], [22.995, 0.0, -352.87], [20.16, 0.0, -352.87], [20.16, 0.0, -366.975], [22.435, 0.0, -369.25], [25.935, 0.0, -367.5], [29.785, 0.0, -369.25], [32.13, 0.0, -366.59], [29.785, 0.0, -369.25], [25.97, 0.0, -367.535], [22.435, 0.0, -369.215], [15.61, 0.0, -369.25], [17.92, 0.0, -366.975], [17.92, 0.0, -355.18], [15.61, 0.0, -352.87], [8.225, 0.0, -352.87], [5.95, 0.0, -355.18], [5.95, 0.0, -366.975], [8.225, 0.0, -369.25], [15.61, 0.0, -369.25], [14.735, 0.0, -366.625], [15.085, 0.0, -355.775], [8.75, 0.0, -355.845], [8.785, 0.0, -366.625], [14.77, 0.0, -366.695], [15.61, 0.0, -369.25], [8.225, 0.0, -369.25], [3.5, 0.0, -369.25], [3.675, 0.0, -352.87], [-4.305, 0.0, -352.87], [-6.615, 0.0, -355.18], [-6.615, 0.0, -360.115], [-4.27, 0.0, -362.39], [-4.13, 0.0, -362.565], [-8.715, 0.0, -369.18], [-8.715, 0.0, -369.25], [-5.425, 0.0, -369.25], [-0.84, 0.0, -362.6], [0.875, 0.0, -362.6], [0.875, 0.0, -355.6], [-3.535, 0.0, -355.6], [-3.57, 0.0, -359.765], [0.875, 0.0, -359.765], [0.875, 0.0, -369.25], [3.5, 0.0, -369.25], [-22.505, 0.0, -369.25], [-22.505, 0.0, -366.625], [-13.335, 0.0, -366.59], [-13.335, 0.0, -352.87], [-10.5, 0.0, -352.87], [-10.5, 0.0, -369.25], [-34.44, 0.0, -369.25], [-36.54, 0.0, -366.975], [-36.715, 0.0, -355.18], [-34.44, 0.0, -352.87], [-24.745, 0.0, -352.87], [-24.745, 0.0, -369.25], [-27.615, 0.0, -366.625], [-27.545, 0.0, -355.53], [-33.53, 0.0, -355.53], [-33.46, 0.0, -366.555], [-27.51, 0.0, -366.695], [-24.675, 0.0, -369.25]]}]},
			"L_lowerLipSecondary_B_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.896651, -0.762362, -0.385637], [0.896651, -0.762362, -0.403637], [0.896651, -0.744362, -0.403637], [0.896651, -0.744362, -0.385637], [0.914651, -0.744362, -0.385637], [0.914651, -0.744362, -0.403637], [0.914651, -0.762362, -0.403637], [0.914651, -0.762362, -0.385637], [0.896651, -0.762362, -0.385637], [0.896651, -0.744362, -0.385637], [0.896651, -0.744362, -0.403637], [0.914651, -0.744362, -0.403637], [0.914651, -0.744362, -0.385637], [0.914651, -0.762362, -0.385637], [0.914651, -0.762362, -0.403637], [0.896651, -0.762362, -0.403637]]}]},
			"C_tongue_IK_B_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_B_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.068566, -0.068566, -2.532066], [0.096967, 0.0, -2.532066], [0.068566, 0.068566, -2.532066], [0.0, 0.096967, -2.532066], [-0.068566, 0.068566, -2.532066], [-0.096967, 0.0, -2.532066], [-0.068566, -0.068566, -2.532066], [0.0, -0.096967, -2.532066]]}]},
			"L_cheek_A_A_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_A_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.813951, 2.64779, 0.116521], [1.789223, 2.662818, 0.14141], [1.760853, 2.64906, 0.162919], [1.74546, 2.614574, 0.168449], [1.752062, 2.579562, 0.15476], [1.77679, 2.564534, 0.129871], [1.80516, 2.578292, 0.108362], [1.820552, 2.612778, 0.102832]]}]},
			"L_cheekLower_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_cheekLower_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.605383, 2.127413, -0.842306], [2.614691, 2.135301, -0.832998], [2.620269, 2.122138, -0.827421], [2.610961, 2.11425, -0.836728], [2.605383, 2.127413, -0.842306], [2.620498, 2.124776, -0.842535], [2.620269, 2.122138, -0.827421], [2.605153, 2.124776, -0.82719], [2.614691, 2.135301, -0.832998], [2.620498, 2.124776, -0.842535], [2.610961, 2.11425, -0.836728], [2.605153, 2.124776, -0.82719], [2.605383, 2.127413, -0.842306], [2.620498, 2.124776, -0.842535], [1.888981, 2.124776, -0.111019]]}, {"shapeName": "L_cheekLower_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.057493, 3.12038, 0.057493], [2.057263, 3.117742, 0.072609], [2.072379, 3.115104, 0.072379], [2.072609, 3.117742, 0.057263], [2.057493, 3.12038, 0.057493], [2.066801, 3.128267, 0.066801], [2.072379, 3.115104, 0.072379], [2.063071, 3.107216, 0.063071], [2.057263, 3.117742, 0.072609], [2.066801, 3.128267, 0.066801], [2.072609, 3.117742, 0.057263], [2.063071, 3.107216, 0.063071], [2.057493, 3.12038, 0.057493], [2.066801, 3.128267, 0.066801], [1.888981, 2.124776, -0.111019]]}, {"shapeName": "L_cheekLower_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.59298, 1.886464, 0.59298], [2.583442, 1.875938, 0.598787], [2.58925, 1.865413, 0.58925], [2.598787, 1.875938, 0.583442], [2.59298, 1.886464, 0.59298], [2.598557, 1.873301, 0.598557], [2.58925, 1.865413, 0.58925], [2.583672, 1.878576, 0.583672], [2.583442, 1.875938, 0.598787], [2.598557, 1.873301, 0.598557], [2.598787, 1.875938, 0.583442], [2.583672, 1.878576, 0.583672], [2.59298, 1.886464, 0.59298], [2.598557, 1.873301, 0.598557], [1.888981, 2.124776, -0.111019]]}]},
			"C_upperLipSecondary_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_upperLipSecondary_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 1.416217, -0.405488], [1.023671, 1.427068, -0.394637], [1.023671, 1.416217, -0.383786], [1.023671, 1.405366, -0.394637], [1.023671, 1.416217, -0.405488], [1.034521, 1.416217, -0.394637], [1.023671, 1.416217, -0.383786], [1.01282, 1.416217, -0.394637], [1.023671, 1.427068, -0.394637], [1.034521, 1.416217, -0.394637], [1.023671, 1.405366, -0.394637], [1.01282, 1.416217, -0.394637], [1.023671, 1.416217, -0.405488], [1.034521, 1.416217, -0.394637], [0.0, 1.416217, -0.394637]]}, {"shapeName": "C_upperLipSecondary_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 2.439888, -0.405488], [-0.010851, 2.439888, -0.394637], [0.0, 2.439888, -0.383786], [0.010851, 2.439888, -0.394637], [0.0, 2.439888, -0.405488], [0.0, 2.450738, -0.394637], [0.0, 2.439888, -0.383786], [0.0, 2.429037, -0.394637], [-0.010851, 2.439888, -0.394637], [0.0, 2.450738, -0.394637], [0.010851, 2.439888, -0.394637], [0.0, 2.429037, -0.394637], [0.0, 2.439888, -0.405488], [0.0, 2.450738, -0.394637], [0.0, 1.416217, -0.394637]]}, {"shapeName": "C_upperLipSecondary_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 1.427068, 0.629034], [-0.010851, 1.416217, 0.629034], [0.0, 1.405366, 0.629034], [0.010851, 1.416217, 0.629034], [0.0, 1.427068, 0.629034], [0.0, 1.416217, 0.639884], [0.0, 1.405366, 0.629034], [0.0, 1.416217, 0.618183], [-0.010851, 1.416217, 0.629034], [0.0, 1.416217, 0.639884], [0.010851, 1.416217, 0.629034], [0.0, 1.416217, 0.618183], [0.0, 1.427068, 0.629034], [0.0, 1.416217, 0.639884], [0.0, 1.416217, -0.394637]]}]},
			"C_lowerLipSecondary_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_lowerLipSecondary_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.007, -1.040783, -0.387637], [-0.007, -1.040783, -0.401637], [-0.007, -1.026783, -0.401637], [-0.007, -1.026783, -0.387637], [0.007, -1.026783, -0.387637], [0.007, -1.026783, -0.401637], [0.007, -1.040783, -0.401637], [0.007, -1.040783, -0.387637], [-0.007, -1.040783, -0.387637], [-0.007, -1.026783, -0.387637], [-0.007, -1.026783, -0.401637], [0.007, -1.026783, -0.401637], [0.007, -1.026783, -0.387637], [0.007, -1.040783, -0.387637], [0.007, -1.040783, -0.401637], [-0.007, -1.040783, -0.401637]]}]},
			"R_eye_FK_A_OFF_CTL": {"color": 8, "shapes": [{"shapeName": "R_eye_FK_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.0, 6.0, 0.5], [-2.1125, 6.0, 0.3875], [-2.103937, 5.956948, 0.3875], [-2.0, 6.0, 0.5], [-1.8875, 6.0, 0.3875], [-1.896063, 6.043052, 0.3875], [-2.0, 6.0, 0.5], [-2.079549, 5.920451, 0.3875], [-2.043052, 5.896064, 0.3875], [-2.0, 6.0, 0.5], [-1.920451, 6.07955, 0.3875], [-1.956948, 6.103936, 0.3875], [-2.0, 6.0, 0.5], [-2.0, 5.8875, 0.3875], [-1.956948, 5.896064, 0.3875], [-2.0, 6.0, 0.5], [-2.0, 6.1125, 0.3875], [-2.043052, 6.103936, 0.3875], [-2.0, 6.0, 0.5], [-1.92045, 5.920451, 0.3875], [-1.896063, 5.956948, 0.3875], [-2.0, 6.0, 0.5], [-2.079549, 6.079549, 0.3875], [-2.103937, 6.043052, 0.3875], [-2.1125, 6.0, 0.3875], [-2.103937, 5.956948, 0.3875], [-2.079549, 5.920451, 0.3875], [-2.043052, 5.896064, 0.3875], [-2.0, 5.8875, 0.3875], [-1.956948, 5.896064, 0.3875], [-1.92045, 5.920451, 0.3875], [-1.896063, 5.956948, 0.3875], [-1.8875, 6.0, 0.3875], [-1.896063, 6.043052, 0.3875], [-1.920451, 6.07955, 0.3875], [-1.956948, 6.103936, 0.3875], [-2.0, 6.1125, 0.3875], [-2.043052, 6.103936, 0.3875], [-2.079549, 6.079549, 0.3875], [-2.103937, 6.043052, 0.3875], [-2.0, 6.0, 0.5]]}]},
			"R_brow_B_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_B_CTLShape", "degree": 3, "form": 2, "points": [[-1.274924, 7.994732, -1.182976], [-1.234382, 8.007146, -1.182112], [-1.20084, 7.998349, -1.157698], [-1.193946, 7.973495, -1.124035], [-1.217739, 7.947141, -1.100842], [-1.258281, 7.934727, -1.101706], [-1.291823, 7.943523, -1.12612], [-1.298716, 7.968378, -1.159784]]}]},
			"L_brow_upper_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_brow_upper_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.967971, 8.033992, -1.907056], [1.967131, 8.048502, -1.911979], [1.971434, 8.053457, -1.898107], [1.972274, 8.038947, -1.893184], [1.967971, 8.033992, -1.907056], [1.9801, 8.043285, -1.90565], [1.971434, 8.053457, -1.898107], [1.959304, 8.044164, -1.899513], [1.967131, 8.048502, -1.911979], [1.9801, 8.043285, -1.90565], [1.972274, 8.038947, -1.893184], [1.959304, 8.044164, -1.899513], [1.967971, 8.033992, -1.907056], [1.9801, 8.043285, -1.90565], [0.988703, 8.085161, -1.613054]]}, {"shapeName": "L_brow_upper_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.744366, 8.526127, -2.504047], [0.735699, 8.536299, -2.496504], [0.747829, 8.545593, -2.495098], [0.756496, 8.535421, -2.502642], [0.744366, 8.526127, -2.504047], [0.743526, 8.540637, -2.508969], [0.747829, 8.545593, -2.495098], [0.748669, 8.531082, -2.490175], [0.735699, 8.536299, -2.496504], [0.743526, 8.540637, -2.508969], [0.756496, 8.535421, -2.502642], [0.748669, 8.531082, -2.490175], [0.744366, 8.526127, -2.504047], [0.743526, 8.540637, -2.508969], [0.988703, 8.085161, -1.613054]]}, {"shapeName": "L_brow_upper_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.149488, 9.008119, -1.20036], [1.141661, 9.00378, -1.187894], [1.154632, 8.998564, -1.181565], [1.162459, 9.002902, -1.194032], [1.149488, 9.008119, -1.20036], [1.153791, 9.013073, -1.186489], [1.154632, 8.998564, -1.181565], [1.150328, 8.993608, -1.195437], [1.141661, 9.00378, -1.187894], [1.153791, 9.013073, -1.186489], [1.162459, 9.002902, -1.194032], [1.150328, 8.993608, -1.195437], [1.149488, 9.008119, -1.20036], [1.153791, 9.013073, -1.186489], [0.988703, 8.085161, -1.613054]]}]},
			"C_noseTip_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_noseTip_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.188067, 5.335275, -1.013724], [0.0, 5.413175, -1.013724], [-0.188067, 5.335275, -1.013724], [-0.265967, 5.147208, -1.013724], [-0.188067, 4.959141, -1.013724], [0.0, 4.881241, -1.013724], [0.188067, 4.959141, -1.013724], [0.265967, 5.147208, -1.013724]]}]},
			"L_lookAt_A_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "L_lookAt_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.176313, 6.176313, 2.5], [2.0, 6.249344, 2.5], [1.823687, 6.176313, 2.5], [1.750656, 6.0, 2.5], [1.823687, 5.823687, 2.5], [2.0, 5.750656, 2.5], [2.176313, 5.823687, 2.5], [2.249344, 6.0, 2.5]]}]},
			"L_lowerLipSecondary_C_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_C_CTLShape", "degree": 1, "form": 0, "points": [[1.281093, -0.473611, -0.384637], [1.281093, -0.473611, -0.404637], [1.281093, -0.453611, -0.404637], [1.281093, -0.453611, -0.384637], [1.301093, -0.453611, -0.384637], [1.301093, -0.453611, -0.404637], [1.301093, -0.473611, -0.404637], [1.301093, -0.473611, -0.384637], [1.281093, -0.473611, -0.384637], [1.281093, -0.453611, -0.384637], [1.281093, -0.453611, -0.404637], [1.301093, -0.453611, -0.404637], [1.301093, -0.453611, -0.384637], [1.301093, -0.473611, -0.384637], [1.301093, -0.473611, -0.404637], [1.281093, -0.473611, -0.404637]]}]},
			"R_brow_C_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_C_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.694179, 7.812575, -1.510617], [-1.666524, 7.822036, -1.505423], [-1.645868, 7.816256, -1.484901], [-1.64431, 7.798621, -1.461071], [-1.662764, 7.779463, -1.447892], [-1.690419, 7.770002, -1.453086], [-1.711075, 7.775782, -1.473608], [-1.712633, 7.793417, -1.497439]]}]},
			"L_lipCorner_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lipCorner_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.013713, 0.20493, -0.394637], [2.0, 0.21061, -0.394637], [1.986287, 0.20493, -0.394637], [1.980607, 0.191217, -0.394637], [1.986287, 0.177503, -0.394637], [2.0, 0.171823, -0.394637], [2.013713, 0.177503, -0.394637], [2.019393, 0.191217, -0.394637]]}]},
			"R_lowerLip_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lowerLip_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.1263, -0.61333, -0.405488], [-2.1263, -0.602479, -0.394637], [-2.1263, -0.61333, -0.383786], [-2.1263, -0.624181, -0.394637], [-2.1263, -0.61333, -0.405488], [-2.13715, -0.61333, -0.394637], [-2.1263, -0.61333, -0.383786], [-2.115449, -0.61333, -0.394637], [-2.1263, -0.602479, -0.394637], [-2.13715, -0.61333, -0.394637], [-2.1263, -0.624181, -0.394637], [-2.115449, -0.61333, -0.394637], [-2.1263, -0.61333, -0.405488], [-2.13715, -0.61333, -0.394637], [-1.102629, -0.61333, -0.394637]]}, {"shapeName": "R_lowerLip_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.102629, 0.410341, -0.405488], [-1.091778, 0.410341, -0.394637], [-1.102629, 0.410341, -0.383786], [-1.11348, 0.410341, -0.394637], [-1.102629, 0.410341, -0.405488], [-1.102629, 0.421191, -0.394637], [-1.102629, 0.410341, -0.383786], [-1.102629, 0.39949, -0.394637], [-1.091778, 0.410341, -0.394637], [-1.102629, 0.421191, -0.394637], [-1.11348, 0.410341, -0.394637], [-1.102629, 0.39949, -0.394637], [-1.102629, 0.410341, -0.405488], [-1.102629, 0.421191, -0.394637], [-1.102629, -0.61333, -0.394637]]}, {"shapeName": "R_lowerLip_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.102629, -0.602479, 0.629034], [-1.091778, -0.61333, 0.629034], [-1.102629, -0.624181, 0.629034], [-1.11348, -0.61333, 0.629034], [-1.102629, -0.602479, 0.629034], [-1.102629, -0.61333, 0.639884], [-1.102629, -0.624181, 0.629034], [-1.102629, -0.61333, 0.618183], [-1.091778, -0.61333, 0.629034], [-1.102629, -0.61333, 0.639884], [-1.11348, -0.61333, 0.629034], [-1.102629, -0.61333, 0.618183], [-1.102629, -0.602479, 0.629034], [-1.102629, -0.61333, 0.639884], [-1.102629, -0.61333, -0.394637]]}]},
			"R_upperLidPrimary_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLidPrimary_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.293721, 6.478008, 0.144183], [-1.288845, 6.480028, 0.144183], [-1.283969, 6.478008, 0.144183], [-1.281949, 6.473132, 0.144183], [-1.283969, 6.468255, 0.144183], [-1.288845, 6.466236, 0.144183], [-1.293721, 6.468255, 0.144183], [-1.295741, 6.473132, 0.144183]]}]},
			"R_lowerLipSecondary_B_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_B_CTLShape", "degree": 1, "form": 0, "points": [[-0.895651, -0.763362, -0.384637], [-0.895651, -0.763362, -0.404637], [-0.895651, -0.743362, -0.404637], [-0.895651, -0.743362, -0.384637], [-0.915651, -0.743362, -0.384637], [-0.915651, -0.743362, -0.404637], [-0.915651, -0.763362, -0.404637], [-0.915651, -0.763362, -0.384637], [-0.895651, -0.763362, -0.384637], [-0.895651, -0.743362, -0.384637], [-0.895651, -0.743362, -0.404637], [-0.915651, -0.743362, -0.404637], [-0.915651, -0.743362, -0.384637], [-0.915651, -0.763362, -0.384637], [-0.915651, -0.763362, -0.404637], [-0.895651, -0.763362, -0.404637]]}]},
			"C_tongue_IK_C_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_C_CTLShape", "degree": 3, "form": 2, "points": [[0.097951, -0.097951, -1.907066], [0.138524, 0.0, -1.907066], [0.097951, 0.097951, -1.907066], [0.0, 0.138524, -1.907066], [-0.097951, 0.097951, -1.907066], [-0.138524, 0.0, -1.907066], [-0.097951, -0.097951, -1.907066], [0.0, -0.138524, -1.907066]]}]},
			"C_lowerLip_CTL": {"color": 17, "shapes": [{"shapeName": "C_lowerLip_CTLShape", "degree": 3, "form": 2, "points": [[0.01959, -1.034193, -0.384637], [0.0, -1.026079, -0.384637], [-0.01959, -1.034193, -0.384637], [-0.027705, -1.053783, -0.384637], [-0.01959, -1.073374, -0.384637], [0.0, -1.081488, -0.384637], [0.01959, -1.073374, -0.384637], [0.027705, -1.053783, -0.384637]]}]},
			"R_lowerLipSecondary_D_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_D_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.644693, -0.152506, -0.386637], [-1.644693, -0.152506, -0.402637], [-1.644693, -0.136506, -0.402637], [-1.644693, -0.136506, -0.386637], [-1.660693, -0.136506, -0.386637], [-1.660693, -0.136506, -0.402637], [-1.660693, -0.152506, -0.402637], [-1.660693, -0.152506, -0.386637], [-1.644693, -0.152506, -0.386637], [-1.644693, -0.136506, -0.386637], [-1.644693, -0.136506, -0.402637], [-1.660693, -0.136506, -0.402637], [-1.660693, -0.136506, -0.386637], [-1.660693, -0.152506, -0.386637], [-1.660693, -0.152506, -0.402637], [-1.644693, -0.152506, -0.402637]]}]},
			"R_cheekLower_B_B_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_B_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.916533, 2.15518, -0.127795], [-1.896601, 2.167774, -0.103399], [-1.872205, 2.15518, -0.083467], [-1.857637, 2.124776, -0.079674], [-1.86143, 2.094371, -0.094242], [-1.881362, 2.081777, -0.118638], [-1.905758, 2.094371, -0.13857], [-1.920326, 2.124776, -0.142363]]}]},
			"R_squint_B_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.987104, 2.847437, -0.012896], [-1.975363, 2.866732, -0.024637], [-2.000784, 2.865386, -0.024672], [-1.987104, 2.847437, -0.012896], [-1.975328, 2.865386, 0.000784], [-1.975363, 2.866732, -0.024637], [-1.989008, 2.883336, -0.010992], [-1.975328, 2.865386, 0.000784], [-2.000748, 2.86404, 0.000748], [-1.987104, 2.847437, -0.012896], [-2.000784, 2.865386, -0.024672], [-1.989008, 2.883336, -0.010992], [-2.000748, 2.86404, 0.000748], [-2.000784, 2.865386, -0.024672]]}]},
			"R_brow_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.162611, 7.764373, -1.600302], [-2.162922, 7.779662, -1.601579], [-2.167913, 7.780769, -1.58711], [-2.167602, 7.76548, -1.585833], [-2.162611, 7.764373, -1.600302], [-2.175519, 7.77207, -1.597206], [-2.167913, 7.780769, -1.58711], [-2.155003, 7.773072, -1.590206], [-2.162922, 7.779662, -1.601579], [-2.175519, 7.77207, -1.597206], [-2.167602, 7.76548, -1.585833], [-2.155003, 7.773072, -1.590206], [-2.162611, 7.764373, -1.600302], [-2.175519, 7.77207, -1.597206], [-1.19747, 7.819831, -1.263481]]}, {"shapeName": "R_brow_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.974054, 8.480592, -2.012815], [-0.966446, 8.489291, -2.002718], [-0.979356, 8.496988, -1.999623], [-0.986963, 8.488289, -2.009719], [-0.974054, 8.480592, -2.012815], [-0.974365, 8.49588, -2.014091], [-0.979356, 8.496988, -1.999623], [-0.979045, 8.481699, -1.998346], [-0.966446, 8.489291, -2.002718], [-0.974365, 8.49588, -2.014091], [-0.986963, 8.488289, -2.009719], [-0.979045, 8.481699, -1.998346], [-0.974054, 8.480592, -2.012815], [-0.974365, 8.49588, -2.014091], [-1.19747, 7.819831, -1.263481]]}, {"shapeName": "R_brow_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.445219, 8.600332, -0.649105], [-1.437301, 8.593742, -0.637731], [-1.449899, 8.58615, -0.633358], [-1.457818, 8.59274, -0.644732], [-1.445219, 8.600332, -0.649105], [-1.45021, 8.601439, -0.634636], [-1.449899, 8.58615, -0.633358], [-1.444908, 8.585043, -0.647827], [-1.437301, 8.593742, -0.637731], [-1.45021, 8.601439, -0.634636], [-1.457818, 8.59274, -0.644732], [-1.444908, 8.585043, -0.647827], [-1.445219, 8.600332, -0.649105], [-1.45021, 8.601439, -0.634636], [-1.19747, 7.819831, -1.263481]]}]},
			"R_outterLid_CTL": {"color": 6, "shapes": [{"shapeName": "R_outterLid_CTLShape", "degree": 1, "form": 0, "points": [[-2.061195, 5.967529, 0.151961], [-2.066695, 5.962029, 0.151961], [-2.072195, 5.967529, 0.151961], [-2.066695, 5.973029, 0.151961], [-2.061195, 5.967529, 0.151961]]}]},
			"R_upperLid_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upperLid_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.298186, 6.356829, 0.139964], [-1.298186, 6.361048, 0.144183], [-1.298186, 6.356829, 0.148402], [-1.298186, 6.35261, 0.144183], [-1.298186, 6.356829, 0.139964], [-1.302406, 6.356829, 0.144183], [-1.298186, 6.356829, 0.148402], [-1.293967, 6.356829, 0.144183], [-1.298186, 6.361048, 0.144183], [-1.302406, 6.356829, 0.144183], [-1.298186, 6.35261, 0.144183], [-1.293967, 6.356829, 0.144183], [-1.298186, 6.356829, 0.139964], [-1.302406, 6.356829, 0.144183], [-0.900132, 6.356829, 0.144183]]}, {"shapeName": "R_upperLid_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.900132, 6.754883, 0.139964], [-0.895913, 6.754883, 0.144183], [-0.900132, 6.754883, 0.148402], [-0.904351, 6.754883, 0.144183], [-0.900132, 6.754883, 0.139964], [-0.900132, 6.759102, 0.144183], [-0.900132, 6.754883, 0.148402], [-0.900132, 6.750664, 0.144183], [-0.895913, 6.754883, 0.144183], [-0.900132, 6.759102, 0.144183], [-0.904351, 6.754883, 0.144183], [-0.900132, 6.750664, 0.144183], [-0.900132, 6.754883, 0.139964], [-0.900132, 6.759102, 0.144183], [-0.900132, 6.356829, 0.144183]]}, {"shapeName": "R_upperLid_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.900132, 6.361048, 0.542237], [-0.895913, 6.356829, 0.542237], [-0.900132, 6.35261, 0.542237], [-0.904351, 6.356829, 0.542237], [-0.900132, 6.361048, 0.542237], [-0.900132, 6.356829, 0.546456], [-0.900132, 6.35261, 0.542237], [-0.900132, 6.356829, 0.538018], [-0.895913, 6.356829, 0.542237], [-0.900132, 6.356829, 0.546456], [-0.904351, 6.356829, 0.542237], [-0.900132, 6.356829, 0.538018], [-0.900132, 6.361048, 0.542237], [-0.900132, 6.356829, 0.546456], [-0.900132, 6.356829, 0.144183]]}]},
			"L_lipCornerSecondary_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lipCornerSecondary_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.994, 0.185217, -0.388637], [1.994, 0.185217, -0.400637], [1.994, 0.197217, -0.400637], [1.994, 0.197217, -0.388637], [2.006, 0.197217, -0.388637], [2.006, 0.197217, -0.400637], [2.006, 0.185217, -0.400637], [2.006, 0.185217, -0.388637], [1.994, 0.185217, -0.388637], [1.994, 0.197217, -0.388637], [1.994, 0.197217, -0.400637], [2.006, 0.197217, -0.400637], [2.006, 0.197217, -0.388637], [2.006, 0.185217, -0.388637], [2.006, 0.185217, -0.400637], [1.994, 0.185217, -0.400637]]}]},
			"R_nostril_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_nostril_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.523671, 5.147208, -1.624575], [-1.523671, 5.158059, -1.613724], [-1.523671, 5.147208, -1.602873], [-1.523671, 5.136357, -1.613724], [-1.523671, 5.147208, -1.624575], [-1.534521, 5.147208, -1.613724], [-1.523671, 5.147208, -1.602873], [-1.51282, 5.147208, -1.613724], [-1.523671, 5.158059, -1.613724], [-1.534521, 5.147208, -1.613724], [-1.523671, 5.136357, -1.613724], [-1.51282, 5.147208, -1.613724], [-1.523671, 5.147208, -1.624575], [-1.534521, 5.147208, -1.613724], [-0.5, 5.147208, -1.613724]]}, {"shapeName": "R_nostril_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.5, 6.170879, -1.624575], [-0.489149, 6.170879, -1.613724], [-0.5, 6.170879, -1.602873], [-0.510851, 6.170879, -1.613724], [-0.5, 6.170879, -1.624575], [-0.5, 6.181729, -1.613724], [-0.5, 6.170879, -1.602873], [-0.5, 6.160028, -1.613724], [-0.489149, 6.170879, -1.613724], [-0.5, 6.181729, -1.613724], [-0.510851, 6.170879, -1.613724], [-0.5, 6.160028, -1.613724], [-0.5, 6.170879, -1.624575], [-0.5, 6.181729, -1.613724], [-0.5, 5.147208, -1.613724]]}, {"shapeName": "R_nostril_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.5, 5.158059, -0.590053], [-0.489149, 5.147208, -0.590053], [-0.5, 5.136357, -0.590053], [-0.510851, 5.147208, -0.590053], [-0.5, 5.158059, -0.590053], [-0.5, 5.147208, -0.579203], [-0.5, 5.136357, -0.590053], [-0.5, 5.147208, -0.600904], [-0.489149, 5.147208, -0.590053], [-0.5, 5.147208, -0.579203], [-0.510851, 5.147208, -0.590053], [-0.5, 5.147208, -0.600904], [-0.5, 5.158059, -0.590053], [-0.5, 5.147208, -0.579203], [-0.5, 5.147208, -1.613724]]}]},
			"L_lowerLipSecondary_C_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.284093, -0.470611, -0.387637], [1.284093, -0.470611, -0.401637], [1.284093, -0.456611, -0.401637], [1.284093, -0.456611, -0.387637], [1.298093, -0.456611, -0.387637], [1.298093, -0.456611, -0.401637], [1.298093, -0.470611, -0.401637], [1.298093, -0.470611, -0.387637], [1.284093, -0.470611, -0.387637], [1.284093, -0.456611, -0.387637], [1.284093, -0.456611, -0.401637], [1.298093, -0.456611, -0.401637], [1.298093, -0.456611, -0.387637], [1.298093, -0.470611, -0.387637], [1.298093, -0.470611, -0.401637], [1.284093, -0.470611, -0.401637]]}]},
			"L_brow_upper_C_C_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.386391, 8.070056, -1.773396], [1.40102, 8.05107, -1.738906], [1.439102, 8.048561, -1.756439], [1.424474, 8.067547, -1.790929], [1.386391, 8.070056, -1.773396]]}]},
			"R_lowerLipSecondary_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lowerLipSecondary_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.676364, -0.144506, -0.405488], [-2.676364, -0.133655, -0.394637], [-2.676364, -0.144506, -0.383786], [-2.676364, -0.155357, -0.394637], [-2.676364, -0.144506, -0.405488], [-2.687214, -0.144506, -0.394637], [-2.676364, -0.144506, -0.383786], [-2.665513, -0.144506, -0.394637], [-2.676364, -0.133655, -0.394637], [-2.687214, -0.144506, -0.394637], [-2.676364, -0.155357, -0.394637], [-2.665513, -0.144506, -0.394637], [-2.676364, -0.144506, -0.405488], [-2.687214, -0.144506, -0.394637], [-1.652693, -0.144506, -0.394637]]}, {"shapeName": "R_lowerLipSecondary_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.652693, 0.879165, -0.405488], [-1.641842, 0.879165, -0.394637], [-1.652693, 0.879165, -0.383786], [-1.663544, 0.879165, -0.394637], [-1.652693, 0.879165, -0.405488], [-1.652693, 0.890015, -0.394637], [-1.652693, 0.879165, -0.383786], [-1.652693, 0.868314, -0.394637], [-1.641842, 0.879165, -0.394637], [-1.652693, 0.890015, -0.394637], [-1.663544, 0.879165, -0.394637], [-1.652693, 0.868314, -0.394637], [-1.652693, 0.879165, -0.405488], [-1.652693, 0.890015, -0.394637], [-1.652693, -0.144506, -0.394637]]}, {"shapeName": "R_lowerLipSecondary_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.652693, -0.133655, 0.629034], [-1.641842, -0.144506, 0.629034], [-1.652693, -0.155357, 0.629034], [-1.663544, -0.144506, 0.629034], [-1.652693, -0.133655, 0.629034], [-1.652693, -0.144506, 0.639884], [-1.652693, -0.155357, 0.629034], [-1.652693, -0.144506, 0.618183], [-1.641842, -0.144506, 0.629034], [-1.652693, -0.144506, 0.639884], [-1.663544, -0.144506, 0.629034], [-1.652693, -0.144506, 0.618183], [-1.652693, -0.133655, 0.629034], [-1.652693, -0.144506, 0.639884], [-1.652693, -0.144506, -0.394637]]}]},
			"L_upperLid_A_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.897197, 6.359177, 0.144183], [0.897197, 6.353732, 0.144183], [0.902642, 6.353732, 0.144183], [0.902642, 6.359177, 0.144183], [0.897197, 6.359177, 0.144183]]}]},
			"L_lookAt_C_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "L_lookAt_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.137132, 6.137132, 2.5], [2.0, 6.193934, 2.5], [1.862868, 6.137132, 2.5], [1.806066, 6.0, 2.5], [1.862868, 5.862868, 2.5], [2.0, 5.806066, 2.5], [2.137132, 5.862868, 2.5], [2.193934, 6.0, 2.5]]}]},
			"R_upperLipSecondary_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upperLipSecondary_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.929322, 1.135795, -0.405488], [-1.929322, 1.146646, -0.394637], [-1.929322, 1.135795, -0.383786], [-1.929322, 1.124944, -0.394637], [-1.929322, 1.135795, -0.405488], [-1.940172, 1.135795, -0.394637], [-1.929322, 1.135795, -0.383786], [-1.918471, 1.135795, -0.394637], [-1.929322, 1.146646, -0.394637], [-1.940172, 1.135795, -0.394637], [-1.929322, 1.124944, -0.394637], [-1.918471, 1.135795, -0.394637], [-1.929322, 1.135795, -0.405488], [-1.940172, 1.135795, -0.394637], [-0.905651, 1.135795, -0.394637]]}, {"shapeName": "R_upperLipSecondary_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.905651, 2.159466, -0.405488], [-0.8948, 2.159466, -0.394637], [-0.905651, 2.159466, -0.383786], [-0.916502, 2.159466, -0.394637], [-0.905651, 2.159466, -0.405488], [-0.905651, 2.170316, -0.394637], [-0.905651, 2.159466, -0.383786], [-0.905651, 2.148615, -0.394637], [-0.8948, 2.159466, -0.394637], [-0.905651, 2.170316, -0.394637], [-0.916502, 2.159466, -0.394637], [-0.905651, 2.148615, -0.394637], [-0.905651, 2.159466, -0.405488], [-0.905651, 2.170316, -0.394637], [-0.905651, 1.135795, -0.394637]]}, {"shapeName": "R_upperLipSecondary_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.905651, 1.146646, 0.629034], [-0.8948, 1.135795, 0.629034], [-0.905651, 1.124944, 0.629034], [-0.916502, 1.135795, 0.629034], [-0.905651, 1.146646, 0.629034], [-0.905651, 1.135795, 0.639884], [-0.905651, 1.124944, 0.629034], [-0.905651, 1.135795, 0.618183], [-0.8948, 1.135795, 0.629034], [-0.905651, 1.135795, 0.639884], [-0.916502, 1.135795, 0.629034], [-0.905651, 1.135795, 0.618183], [-0.905651, 1.146646, 0.629034], [-0.905651, 1.135795, 0.639884], [-0.905651, 1.135795, -0.394637]]}]},
			"L_upperLipSecondary_D_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_D_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.646693, 0.52094, -0.388637], [1.646693, 0.52094, -0.400637], [1.646693, 0.53294, -0.400637], [1.646693, 0.53294, -0.388637], [1.658693, 0.53294, -0.388637], [1.658693, 0.53294, -0.400637], [1.658693, 0.52094, -0.400637], [1.658693, 0.52094, -0.388637], [1.646693, 0.52094, -0.388637], [1.646693, 0.53294, -0.388637], [1.646693, 0.53294, -0.400637], [1.658693, 0.53294, -0.400637], [1.658693, 0.53294, -0.388637], [1.658693, 0.52094, -0.388637], [1.658693, 0.52094, -0.400637], [1.646693, 0.52094, -0.400637]]}]},
			"R_cheek_A_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_A_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.813951, 2.64779, 0.116521], [-1.789223, 2.662818, 0.14141], [-1.760853, 2.64906, 0.162919], [-1.74546, 2.614574, 0.168449], [-1.752062, 2.579562, 0.15476], [-1.77679, 2.564534, 0.129871], [-1.80516, 2.578292, 0.108362], [-1.820552, 2.612778, 0.102832]]}]},
			"L_brow_upper_A_D_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.483887, 8.10444, -1.51288], [0.488142, 8.08862, -1.480824], [0.523773, 8.087891, -1.485913], [0.519518, 8.103711, -1.51797], [0.483887, 8.10444, -1.51288]]}]},
			"L_lowerLip_A_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lowerLip_A_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.114383, -0.601576, -0.394637], [1.102629, -0.596707, -0.394637], [1.090874, -0.601576, -0.394637], [1.086006, -0.61333, -0.394637], [1.090874, -0.625084, -0.394637], [1.102629, -0.629953, -0.394637], [1.114383, -0.625084, -0.394637], [1.119251, -0.61333, -0.394637]]}]},
			"L_upperLip_A_CTL": {"color": 17, "shapes": [{"shapeName": "L_upperLip_A_CTLShape", "degree": 3, "form": 2, "points": [[1.122219, 1.035353, -0.384637], [1.102629, 1.043468, -0.384637], [1.083038, 1.035353, -0.384637], [1.074924, 1.015763, -0.384637], [1.083038, 0.996173, -0.384637], [1.102629, 0.988058, -0.384637], [1.122219, 0.996173, -0.384637], [1.130333, 1.015763, -0.384637]]}]},
			"R_brow_upper_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_upper_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.338358, 7.988492, -2.196483], [-2.337159, 8.003054, -2.201172], [-2.343518, 8.007806, -2.188039], [-2.344718, 7.993244, -2.18335], [-2.338358, 7.988492, -2.196483], [-2.350776, 7.997501, -2.196791], [-2.343518, 8.007806, -2.188039], [-2.331099, 7.998797, -2.187731], [-2.337159, 8.003054, -2.201172], [-2.350776, 7.997501, -2.196791], [-2.344718, 7.993244, -2.18335], [-2.331099, 7.998797, -2.187731], [-2.338358, 7.988492, -2.196483], [-2.350776, 7.997501, -2.196791], [-1.412747, 8.059309, -1.764918]]}, {"shapeName": "R_brow_upper_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.053629, 8.512393, -2.609766], [-1.04637, 8.522699, -2.601014], [-1.058789, 8.531708, -2.601322], [-1.066048, 8.521402, -2.610074], [-1.053629, 8.512393, -2.609766], [-1.05243, 8.526955, -2.614454], [-1.058789, 8.531708, -2.601322], [-1.059989, 8.517146, -2.596633], [-1.04637, 8.522699, -2.601014], [-1.05243, 8.526955, -2.614454], [-1.066048, 8.521402, -2.610074], [-1.059989, 8.517146, -2.596633], [-1.053629, 8.512393, -2.609766], [-1.05243, 8.526955, -2.614454], [-1.412747, 8.059309, -1.764918]]}, {"shapeName": "R_brow_upper_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.652368, 8.975274, -1.375548], [-1.646309, 8.971017, -1.362108], [-1.659927, 8.965464, -1.357727], [-1.665987, 8.969721, -1.371168], [-1.652368, 8.975274, -1.375548], [-1.658727, 8.980026, -1.362416], [-1.659927, 8.965464, -1.357727], [-1.653568, 8.960712, -1.370859], [-1.646309, 8.971017, -1.362108], [-1.658727, 8.980026, -1.362416], [-1.665987, 8.969721, -1.371168], [-1.653568, 8.960712, -1.370859], [-1.652368, 8.975274, -1.375548], [-1.658727, 8.980026, -1.362416], [-1.412747, 8.059309, -1.764918]]}]},
			"C_upperLipSecondary_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_upperLipSecondary_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.009, 1.407217, -0.385637], [-0.009, 1.407217, -0.403637], [-0.009, 1.425217, -0.403637], [-0.009, 1.425217, -0.385637], [0.009, 1.425217, -0.385637], [0.009, 1.425217, -0.403637], [0.009, 1.407217, -0.403637], [0.009, 1.407217, -0.385637], [-0.009, 1.407217, -0.385637], [-0.009, 1.425217, -0.385637], [-0.009, 1.425217, -0.403637], [0.009, 1.425217, -0.403637], [0.009, 1.425217, -0.385637], [0.009, 1.407217, -0.385637], [0.009, 1.407217, -0.403637], [-0.009, 1.407217, -0.403637]]}]},
			"L_upperLipSecondary_A_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_A_CTLShape", "degree": 1, "form": 0, "points": [[0.465266, 1.338453, -0.384637], [0.465266, 1.338453, -0.404637], [0.465266, 1.358453, -0.404637], [0.465266, 1.358453, -0.384637], [0.485266, 1.358453, -0.384637], [0.485266, 1.358453, -0.404637], [0.485266, 1.338453, -0.404637], [0.485266, 1.338453, -0.384637], [0.465266, 1.338453, -0.384637], [0.465266, 1.358453, -0.384637], [0.465266, 1.358453, -0.404637], [0.485266, 1.358453, -0.404637], [0.485266, 1.358453, -0.384637], [0.485266, 1.338453, -0.384637], [0.485266, 1.338453, -0.404637], [0.465266, 1.338453, -0.404637]]}]},
			"R_lowerLid_C_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.675436, 5.580938, 0.144183], [-1.675436, 5.576271, 0.144183], [-1.680103, 5.576271, 0.144183], [-1.680103, 5.580938, 0.144183], [-1.675436, 5.580938, 0.144183]]}]},
			"L_upperLid_C_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_C_CTLShape", "degree": 1, "form": 0, "points": [[1.67227, 6.356454, 0.151961], [1.67777, 6.350954, 0.151961], [1.68327, 6.356454, 0.151961], [1.67777, 6.361954, 0.151961], [1.67227, 6.356454, 0.151961]]}]},
			"L_upperLidPrimary_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLidPrimary_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.293112, 6.477398, 0.144183], [1.288845, 6.479166, 0.144183], [1.284578, 6.477398, 0.144183], [1.282811, 6.473132, 0.144183], [1.284578, 6.468865, 0.144183], [1.288845, 6.467098, 0.144183], [1.293112, 6.468865, 0.144183], [1.294879, 6.473132, 0.144183]]}]},
			"L_upperLip_A_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_upperLip_A_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.118301, 1.011435, -0.394637], [1.102629, 1.017927, -0.394637], [1.086956, 1.011435, -0.394637], [1.080465, 0.995763, -0.394637], [1.086956, 0.980091, -0.394637], [1.102629, 0.973599, -0.394637], [1.118301, 0.980091, -0.394637], [1.124792, 0.995763, -0.394637]]}]},
			"C_noseBridge_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_noseBridge_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.023671, 5.747208, -1.324575], [1.023671, 5.758059, -1.313724], [1.023671, 5.747208, -1.302873], [1.023671, 5.736357, -1.313724], [1.023671, 5.747208, -1.324575], [1.034521, 5.747208, -1.313724], [1.023671, 5.747208, -1.302873], [1.01282, 5.747208, -1.313724], [1.023671, 5.758059, -1.313724], [1.034521, 5.747208, -1.313724], [1.023671, 5.736357, -1.313724], [1.01282, 5.747208, -1.313724], [1.023671, 5.747208, -1.324575], [1.034521, 5.747208, -1.313724], [0.0, 5.747208, -1.313724]]}, {"shapeName": "C_noseBridge_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 6.770879, -1.324575], [-0.010851, 6.770879, -1.313724], [0.0, 6.770879, -1.302873], [0.010851, 6.770879, -1.313724], [0.0, 6.770879, -1.324575], [0.0, 6.781729, -1.313724], [0.0, 6.770879, -1.302873], [0.0, 6.760028, -1.313724], [-0.010851, 6.770879, -1.313724], [0.0, 6.781729, -1.313724], [0.010851, 6.770879, -1.313724], [0.0, 6.760028, -1.313724], [0.0, 6.770879, -1.324575], [0.0, 6.781729, -1.313724], [0.0, 5.747208, -1.313724]]}, {"shapeName": "C_noseBridge_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 5.758059, -0.290053], [-0.010851, 5.747208, -0.290053], [0.0, 5.736357, -0.290053], [0.010851, 5.747208, -0.290053], [0.0, 5.758059, -0.290053], [0.0, 5.747208, -0.279203], [0.0, 5.736357, -0.290053], [0.0, 5.747208, -0.300904], [-0.010851, 5.747208, -0.290053], [0.0, 5.747208, -0.279203], [0.010851, 5.747208, -0.290053], [0.0, 5.747208, -0.300904], [0.0, 5.758059, -0.290053], [0.0, 5.747208, -0.279203], [0.0, 5.747208, -1.313724]]}]},
			"L_cheekLower_B_D_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_B_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.909645, 2.147579, -0.123601], [1.894696, 2.157024, -0.105304], [1.876399, 2.147579, -0.090355], [1.865473, 2.124776, -0.08751], [1.868318, 2.101972, -0.098436], [1.883267, 2.092527, -0.116733], [1.901564, 2.101972, -0.131682], [1.91249, 2.124776, -0.134527]]}]},
			"L_lowerLipSecondary_B_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.899651, -0.759362, -0.388637], [0.899651, -0.759362, -0.400637], [0.899651, -0.747362, -0.400637], [0.899651, -0.747362, -0.388637], [0.911651, -0.747362, -0.388637], [0.911651, -0.747362, -0.400637], [0.911651, -0.759362, -0.400637], [0.911651, -0.759362, -0.388637], [0.899651, -0.759362, -0.388637], [0.899651, -0.747362, -0.388637], [0.899651, -0.747362, -0.400637], [0.911651, -0.747362, -0.400637], [0.911651, -0.747362, -0.388637], [0.911651, -0.759362, -0.388637], [0.911651, -0.759362, -0.400637], [0.899651, -0.759362, -0.400637]]}]},
			"L_lookAt_B_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "L_lookAt_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.156722, 6.156722, 2.5], [2.0, 6.221639, 2.5], [1.843278, 6.156722, 2.5], [1.778361, 6.0, 2.5], [1.843278, 5.843278, 2.5], [2.0, 5.778361, 2.5], [2.156722, 5.843278, 2.5], [2.221639, 6.0, 2.5]]}]},
			"C_noseTip_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_noseTip_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.211575, 5.358783, -1.013724], [0.0, 5.44642, -1.013724], [-0.211575, 5.358783, -1.013724], [-0.299212, 5.147208, -1.013724], [-0.211575, 4.935633, -1.013724], [0.0, 4.847996, -1.013724], [0.211575, 4.935633, -1.013724], [0.299212, 5.147208, -1.013724]]}]},
			"R_lowerLipSecondary_D_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lowerLipSecondary_D_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.645693, -0.151506, -0.387637], [-1.645693, -0.151506, -0.401637], [-1.645693, -0.137506, -0.401637], [-1.645693, -0.137506, -0.387637], [-1.659693, -0.137506, -0.387637], [-1.659693, -0.137506, -0.401637], [-1.659693, -0.151506, -0.401637], [-1.659693, -0.151506, -0.387637], [-1.645693, -0.151506, -0.387637], [-1.645693, -0.137506, -0.387637], [-1.645693, -0.137506, -0.401637], [-1.659693, -0.137506, -0.401637], [-1.659693, -0.137506, -0.387637], [-1.659693, -0.151506, -0.387637], [-1.659693, -0.151506, -0.401637], [-1.645693, -0.151506, -0.401637]]}]},
			"R_squint_A_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.805503, 2.836008, 0.155295], [-1.793128, 2.858597, 0.14051], [-1.82269, 2.856561, 0.142481], [-1.805503, 2.836008, 0.155295], [-1.791065, 2.857318, 0.170109], [-1.793128, 2.858597, 0.14051], [-1.808253, 2.87787, 0.157296], [-1.791065, 2.857318, 0.170109], [-1.820628, 2.855282, 0.172081], [-1.805503, 2.836008, 0.155295], [-1.82269, 2.856561, 0.142481], [-1.808253, 2.87787, 0.157296], [-1.820628, 2.855282, 0.172081], [-1.82269, 2.856561, 0.142481]]}]},
			"L_upperLid_B_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.286122, 6.475854, 0.144183], [1.286122, 6.470409, 0.144183], [1.291567, 6.470409, 0.144183], [1.291567, 6.475854, 0.144183], [1.286122, 6.475854, 0.144183]]}]},
			"R_brow_upper_B_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_B_CTLShape", "degree": 1, "form": 0, "points": [[-0.979961, 8.266268, -1.518588], [-1.030674, 8.245871, -1.493846], [-1.061277, 8.262833, -1.542588], [-1.010564, 8.28323, -1.56733], [-0.979961, 8.266268, -1.518588]]}]},
			"R_upperLipSecondary_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_upperLipSecondary_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.676364, 0.52694, -0.405488], [-2.676364, 0.537791, -0.394637], [-2.676364, 0.52694, -0.383786], [-2.676364, 0.516089, -0.394637], [-2.676364, 0.52694, -0.405488], [-2.687214, 0.52694, -0.394637], [-2.676364, 0.52694, -0.383786], [-2.665513, 0.52694, -0.394637], [-2.676364, 0.537791, -0.394637], [-2.687214, 0.52694, -0.394637], [-2.676364, 0.516089, -0.394637], [-2.665513, 0.52694, -0.394637], [-2.676364, 0.52694, -0.405488], [-2.687214, 0.52694, -0.394637], [-1.652693, 0.52694, -0.394637]]}, {"shapeName": "R_upperLipSecondary_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-1.652693, 1.550611, -0.405488], [-1.641842, 1.550611, -0.394637], [-1.652693, 1.550611, -0.383786], [-1.663544, 1.550611, -0.394637], [-1.652693, 1.550611, -0.405488], [-1.652693, 1.561461, -0.394637], [-1.652693, 1.550611, -0.383786], [-1.652693, 1.53976, -0.394637], [-1.641842, 1.550611, -0.394637], [-1.652693, 1.561461, -0.394637], [-1.663544, 1.550611, -0.394637], [-1.652693, 1.53976, -0.394637], [-1.652693, 1.550611, -0.405488], [-1.652693, 1.561461, -0.394637], [-1.652693, 0.52694, -0.394637]]}, {"shapeName": "R_upperLipSecondary_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-1.652693, 0.537791, 0.629034], [-1.641842, 0.52694, 0.629034], [-1.652693, 0.516089, 0.629034], [-1.663544, 0.52694, 0.629034], [-1.652693, 0.537791, 0.629034], [-1.652693, 0.52694, 0.639884], [-1.652693, 0.516089, 0.629034], [-1.652693, 0.52694, 0.618183], [-1.641842, 0.52694, 0.629034], [-1.652693, 0.52694, 0.639884], [-1.663544, 0.52694, 0.629034], [-1.652693, 0.52694, 0.618183], [-1.652693, 0.537791, 0.629034], [-1.652693, 0.52694, 0.639884], [-1.652693, 0.52694, -0.394637]]}]},
			"C_noseBase_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_noseBase_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.313445, 5.460653, -1.113724], [0.0, 5.590486, -1.113724], [-0.313445, 5.460653, -1.113724], [-0.443278, 5.147208, -1.113724], [-0.313445, 4.833763, -1.113724], [0.0, 4.70393, -1.113724], [0.313445, 4.833763, -1.113724], [0.443278, 5.147208, -1.113724]]}]},
			"R_nostril_A_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "R_nostril_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-0.676313, 5.323521, -1.613724], [-0.5, 5.396552, -1.613724], [-0.323687, 5.323521, -1.613724], [-0.250656, 5.147208, -1.613724], [-0.323687, 4.970895, -1.613724], [-0.5, 4.897864, -1.613724], [-0.676313, 4.970895, -1.613724], [-0.749344, 5.147208, -1.613724]]}]},
			"C_tongue_FK_F_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_tongue_FK_F_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.002713, 0.0, -1.240433], [0.0, 0.002713, -1.240433], [-0.002713, 0.0, -1.240433], [0.0, -0.002713, -1.240433], [0.002713, 0.0, -1.240433], [0.0, 0.0, -1.237721], [-0.002713, 0.0, -1.240433], [0.0, 0.0, -1.243146], [0.0, 0.002713, -1.240433], [0.0, 0.0, -1.237721], [0.0, -0.002713, -1.240433], [0.0, 0.0, -1.243146], [0.002713, 0.0, -1.240433], [0.0, 0.0, -1.237721], [0.0, 0.0, -1.496351]]}, {"shapeName": "C_tongue_FK_F_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.002713, 0.255918, -1.496351], [0.0, 0.255918, -1.499064], [-0.002713, 0.255918, -1.496351], [0.0, 0.255918, -1.493638], [0.002713, 0.255918, -1.496351], [0.0, 0.25863, -1.496351], [-0.002713, 0.255918, -1.496351], [0.0, 0.253205, -1.496351], [0.0, 0.255918, -1.499064], [0.0, 0.25863, -1.496351], [0.0, 0.255918, -1.493638], [0.0, 0.253205, -1.496351], [0.002713, 0.255918, -1.496351], [0.0, 0.25863, -1.496351], [0.0, 0.0, -1.496351]]}, {"shapeName": "C_tongue_FK_F_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.255918, 0.002713, -1.496351], [-0.255918, 0.0, -1.499064], [-0.255918, -0.002713, -1.496351], [-0.255918, 0.0, -1.493638], [-0.255918, 0.002713, -1.496351], [-0.25863, 0.0, -1.496351], [-0.255918, -0.002713, -1.496351], [-0.253205, 0.0, -1.496351], [-0.255918, 0.0, -1.499064], [-0.25863, 0.0, -1.496351], [-0.255918, 0.0, -1.493638], [-0.253205, 0.0, -1.496351], [-0.255918, 0.002713, -1.496351], [-0.25863, 0.0, -1.496351], [0.0, 0.0, -1.496351]]}]},
			"R_upperLipSecondary_C_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.282093, 0.837044, -0.385637], [-1.282093, 0.837044, -0.403637], [-1.282093, 0.855044, -0.403637], [-1.282093, 0.855044, -0.385637], [-1.300093, 0.855044, -0.385637], [-1.300093, 0.855044, -0.403637], [-1.300093, 0.837044, -0.403637], [-1.300093, 0.837044, -0.385637], [-1.282093, 0.837044, -0.385637], [-1.282093, 0.855044, -0.385637], [-1.282093, 0.855044, -0.403637], [-1.300093, 0.855044, -0.403637], [-1.300093, 0.855044, -0.385637], [-1.300093, 0.837044, -0.385637], [-1.300093, 0.837044, -0.403637], [-1.282093, 0.837044, -0.403637]]}]},
			"R_lowerLid_B_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.286511, 5.46426, 0.144183], [-1.286511, 5.459593, 0.144183], [-1.291178, 5.459593, 0.144183], [-1.291178, 5.46426, 0.144183], [-1.286511, 5.46426, 0.144183]]}]},
			"L_upperLid_A_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.896419, 6.359955, 0.144183], [0.896419, 6.352954, 0.144183], [0.90342, 6.352954, 0.144183], [0.90342, 6.359955, 0.144183], [0.896419, 6.359955, 0.144183]]}]},
			"R_lipZipper_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_lipZipper_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.083115, 0.198096, 2.055363], [-0.090115, 0.184217, 2.055363], [-0.076115, 0.184217, 2.055363], [-0.083115, 0.198096, 2.055363], [-0.083115, 0.198096, 2.055363]]}]},
			"L_lipCornerSecondary_CTL": {"color": 20, "shapes": [{"shapeName": "L_lipCornerSecondary_CTLShape", "degree": 1, "form": 0, "points": [[1.99, 0.181217, -0.384637], [1.99, 0.181217, -0.404637], [1.99, 0.201217, -0.404637], [1.99, 0.201217, -0.384637], [2.01, 0.201217, -0.384637], [2.01, 0.201217, -0.404637], [2.01, 0.181217, -0.404637], [2.01, 0.181217, -0.384637], [1.99, 0.181217, -0.384637], [1.99, 0.201217, -0.384637], [1.99, 0.201217, -0.404637], [2.01, 0.201217, -0.404637], [2.01, 0.201217, -0.384637], [2.01, 0.181217, -0.384637], [2.01, 0.181217, -0.404637], [1.99, 0.181217, -0.404637]]}]},
			"L_lipZipper_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_lipZipper_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.083115, 0.197113, 2.055363], [0.077115, 0.185217, 2.055363], [0.089115, 0.185217, 2.055363], [0.083115, 0.197113, 2.055363], [0.083115, 0.197113, 2.055363]]}]},
			"C_tongue_IK_D_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_D_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.088156, -0.088156, -1.282066], [0.124672, 0.0, -1.282066], [0.088156, 0.088156, -1.282066], [0.0, 0.124672, -1.282066], [-0.088156, 0.088156, -1.282066], [-0.124672, 0.0, -1.282066], [-0.088156, -0.088156, -1.282066], [0.0, -0.124672, -1.282066]]}]},
			"L_cheek_B_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_B_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.985318, 2.639949, -0.047927], [1.969854, 2.649548, -0.030146], [1.952073, 2.639949, -0.014682], [1.942391, 2.616776, -0.010593], [1.94648, 2.593602, -0.020274], [1.961944, 2.584003, -0.038056], [1.979726, 2.593602, -0.05352], [1.989407, 2.616776, -0.057609]]}]},
			"R_lowerLidPrimary_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLidPrimary_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.294331, 5.467413, 0.144183], [-1.288845, 5.469685, 0.144183], [-1.283359, 5.467413, 0.144183], [-1.281087, 5.461927, 0.144183], [-1.283359, 5.456441, 0.144183], [-1.288845, 5.454169, 0.144183], [-1.294331, 5.456441, 0.144183], [-1.296603, 5.461927, 0.144183]]}]},
			"L_upperLip_A_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_upperLip_A_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.116342, 1.009476, -0.394637], [1.102629, 1.015157, -0.394637], [1.088915, 1.009476, -0.394637], [1.083235, 0.995763, -0.394637], [1.088915, 0.98205, -0.394637], [1.102629, 0.97637, -0.394637], [1.116342, 0.98205, -0.394637], [1.122022, 0.995763, -0.394637]]}]},
			"R_brow_A_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_A_CTLShape", "degree": 3, "form": 2, "points": [[-0.675635, 8.007778, -1.015892], [-0.635216, 8.019169, -1.021816], [-0.598327, 8.009592, -1.003216], [-0.586577, 7.984658, -0.970987], [-0.606848, 7.958973, -0.944008], [-0.647267, 7.947582, -0.938085], [-0.684156, 7.957158, -0.956685], [-0.695906, 7.982093, -0.988914]]}]},
			"C_tongue_IK_E_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_E_CTLShape", "degree": 3, "form": 2, "points": [[0.097951, -0.097951, -0.657066], [0.138524, 0.0, -0.657066], [0.097951, 0.097951, -0.657066], [0.0, 0.138524, -0.657066], [-0.097951, 0.097951, -0.657066], [-0.138524, 0.0, -0.657066], [-0.097951, -0.097951, -0.657066], [0.0, -0.138524, -0.657066]]}]},
			"L_upperLid_C_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLid_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.675436, 6.358788, 0.144183], [1.675436, 6.354121, 0.144183], [1.680103, 6.354121, 0.144183], [1.680103, 6.358788, 0.144183], [1.675436, 6.358788, 0.144183]]}]},
			"L_brow_upper_C_D_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.390156, 8.068521, -1.772185], [1.402695, 8.052247, -1.742622], [1.435337, 8.050096, -1.757651], [1.422799, 8.06637, -1.787213], [1.390156, 8.068521, -1.772185]]}]},
			"R_upperLipSecondary_B_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.898651, 1.128795, -0.387637], [-0.898651, 1.128795, -0.401637], [-0.898651, 1.142795, -0.401637], [-0.898651, 1.142795, -0.387637], [-0.912651, 1.142795, -0.387637], [-0.912651, 1.142795, -0.401637], [-0.912651, 1.128795, -0.401637], [-0.912651, 1.128795, -0.387637], [-0.898651, 1.128795, -0.387637], [-0.898651, 1.142795, -0.387637], [-0.898651, 1.142795, -0.401637], [-0.912651, 1.142795, -0.401637], [-0.912651, 1.142795, -0.387637], [-0.912651, 1.128795, -0.387637], [-0.912651, 1.128795, -0.401637], [-0.898651, 1.128795, -0.401637]]}]},
			"L_upperLipSecondary_C_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_C_CTLShape", "degree": 1, "form": 0, "points": [[1.281093, 0.836044, -0.384637], [1.281093, 0.836044, -0.404637], [1.281093, 0.856044, -0.404637], [1.281093, 0.856044, -0.384637], [1.301093, 0.856044, -0.384637], [1.301093, 0.856044, -0.404637], [1.301093, 0.836044, -0.404637], [1.301093, 0.836044, -0.384637], [1.281093, 0.836044, -0.384637], [1.281093, 0.856044, -0.384637], [1.281093, 0.856044, -0.404637], [1.301093, 0.856044, -0.404637], [1.301093, 0.856044, -0.384637], [1.301093, 0.836044, -0.384637], [1.301093, 0.836044, -0.404637], [1.281093, 0.836044, -0.404637]]}]},
			"L_lowerLid_B_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_B_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.285344, 5.465427, 0.144183], [1.285344, 5.458426, 0.144183], [1.292345, 5.458426, 0.144183], [1.292345, 5.465427, 0.144183], [1.285344, 5.465427, 0.144183]]}]},
			"L_lowerLip_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lowerLip_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.1263, -0.61333, -0.405488], [2.1263, -0.602479, -0.394637], [2.1263, -0.61333, -0.383786], [2.1263, -0.624181, -0.394637], [2.1263, -0.61333, -0.405488], [2.13715, -0.61333, -0.394637], [2.1263, -0.61333, -0.383786], [2.115449, -0.61333, -0.394637], [2.1263, -0.602479, -0.394637], [2.13715, -0.61333, -0.394637], [2.1263, -0.624181, -0.394637], [2.115449, -0.61333, -0.394637], [2.1263, -0.61333, -0.405488], [2.13715, -0.61333, -0.394637], [1.102629, -0.61333, -0.394637]]}, {"shapeName": "L_lowerLip_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.102629, 0.410341, -0.405488], [1.091778, 0.410341, -0.394637], [1.102629, 0.410341, -0.383786], [1.11348, 0.410341, -0.394637], [1.102629, 0.410341, -0.405488], [1.102629, 0.421191, -0.394637], [1.102629, 0.410341, -0.383786], [1.102629, 0.39949, -0.394637], [1.091778, 0.410341, -0.394637], [1.102629, 0.421191, -0.394637], [1.11348, 0.410341, -0.394637], [1.102629, 0.39949, -0.394637], [1.102629, 0.410341, -0.405488], [1.102629, 0.421191, -0.394637], [1.102629, -0.61333, -0.394637]]}, {"shapeName": "L_lowerLip_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[1.102629, -0.602479, 0.629034], [1.091778, -0.61333, 0.629034], [1.102629, -0.624181, 0.629034], [1.11348, -0.61333, 0.629034], [1.102629, -0.602479, 0.629034], [1.102629, -0.61333, 0.639884], [1.102629, -0.624181, 0.629034], [1.102629, -0.61333, 0.618183], [1.091778, -0.61333, 0.629034], [1.102629, -0.61333, 0.639884], [1.11348, -0.61333, 0.629034], [1.102629, -0.61333, 0.618183], [1.102629, -0.602479, 0.629034], [1.102629, -0.61333, 0.639884], [1.102629, -0.61333, -0.394637]]}]},
			"C_tongue_FK_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_tongue_FK_A_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.125, -3.285815], [0.0, 0.125951, -3.281031], [0.0, 0.128661, -3.276976], [0.0, 0.132716, -3.274266], [0.0, 0.1375, -3.273315], [0.0, 0.142284, -3.274266], [0.0, 0.146339, -3.276976], [0.0, 0.149049, -3.281031], [0.0, 0.15, -3.285815], [0.0, 0.149049, -3.290598], [0.0, 0.146339, -3.294653], [0.0, 0.142284, -3.297363], [0.0, 0.1375, -3.298315], [0.0, 0.132716, -3.297363], [0.0, 0.128661, -3.294653], [0.0, 0.125951, -3.290598], [0.0, 0.125, -3.285815], [0.0, 0.0, -3.285815]]}]},
			"R_upperLid_C_D_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_C_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.675436, 6.358788, 0.144183], [-1.675436, 6.354121, 0.144183], [-1.680103, 6.354121, 0.144183], [-1.680103, 6.358788, 0.144183], [-1.675436, 6.358788, 0.144183]]}]},
			"R_lowerLid_C_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLid_C_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.675047, 5.581327, 0.144183], [-1.675047, 5.575882, 0.144183], [-1.680492, 5.575882, 0.144183], [-1.680492, 5.581327, 0.144183], [-1.675047, 5.581327, 0.144183]]}]},
			"R_cheek_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.68218, 2.618601, -0.765509], [-2.691035, 2.627472, -0.756655], [-2.697307, 2.61495, -0.750382], [-2.688453, 2.606079, -0.759236], [-2.68218, 2.618601, -0.765509], [-2.697416, 2.616776, -0.765618], [-2.697307, 2.61495, -0.750382], [-2.682071, 2.616776, -0.750273], [-2.691035, 2.627472, -0.756655], [-2.697416, 2.616776, -0.765618], [-2.688453, 2.606079, -0.759236], [-2.682071, 2.616776, -0.750273], [-2.68218, 2.618601, -0.765509], [-2.697416, 2.616776, -0.765618], [-1.965899, 2.616776, -0.034101]]}, {"shapeName": "R_cheek_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-2.080102, 3.627684, 0.080102], [-2.079993, 3.625858, 0.095339], [-2.095229, 3.624033, 0.095229], [-2.095339, 3.625858, 0.079993], [-2.080102, 3.627684, 0.080102], [-2.088956, 3.636554, 0.088956], [-2.095229, 3.624033, 0.095229], [-2.086375, 3.615162, 0.086375], [-2.079993, 3.625858, 0.095339], [-2.088956, 3.636554, 0.088956], [-2.095339, 3.625858, 0.079993], [-2.086375, 3.615162, 0.086375], [-2.080102, 3.627684, 0.080102], [-2.088956, 3.636554, 0.088956], [-1.965899, 2.616776, -0.034101]]}, {"shapeName": "R_cheek_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.680719, 2.455268, 0.680719], [-2.671756, 2.444571, 0.687101], [-2.678138, 2.433875, 0.678138], [-2.687101, 2.444571, 0.671756], [-2.680719, 2.455268, 0.680719], [-2.686991, 2.442746, 0.686991], [-2.678138, 2.433875, 0.678138], [-2.671865, 2.446397, 0.671865], [-2.671756, 2.444571, 0.687101], [-2.686991, 2.442746, 0.686991], [-2.687101, 2.444571, 0.671756], [-2.671865, 2.446397, 0.671865], [-2.680719, 2.455268, 0.680719], [-2.686991, 2.442746, 0.686991], [-1.965899, 2.616776, -0.034101]]}]},
			"C_tongue_FK_F_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "C_tongue_FK_F_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.125, -1.496351], [0.0, 0.125951, -1.491568], [0.0, 0.128661, -1.487512], [0.0, 0.132716, -1.484803], [0.0, 0.1375, -1.483851], [0.0, 0.142284, -1.484803], [0.0, 0.146339, -1.487512], [0.0, 0.149049, -1.491568], [0.0, 0.15, -1.496351], [0.0, 0.149049, -1.501135], [0.0, 0.146339, -1.50519], [0.0, 0.142284, -1.5079], [0.0, 0.1375, -1.508851], [0.0, 0.132716, -1.5079], [0.0, 0.128661, -1.50519], [0.0, 0.125951, -1.501135], [0.0, 0.125, -1.496351], [0.0, 0.0, -1.496351]]}]},
			"L_squint_C_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_C_CTLShape", "degree": 1, "form": 0, "points": [[2.311212, 2.831545, -0.068334], [2.289841, 2.863578, -0.086143], [2.332131, 2.862022, -0.089155], [2.311212, 2.831545, -0.068334], [2.292752, 2.860909, -0.0439], [2.289841, 2.863578, -0.086143], [2.313672, 2.891385, -0.064722], [2.292752, 2.860909, -0.0439], [2.335042, 2.859352, -0.046913], [2.311212, 2.831545, -0.068334], [2.332131, 2.862022, -0.089155], [2.313672, 2.891385, -0.064722], [2.335042, 2.859352, -0.046913], [2.332131, 2.862022, -0.089155]]}]},
			"R_squint_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_squint_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-2.704249, 2.866198, -0.74344], [-2.712474, 2.876207, -0.735215], [-2.719552, 2.864575, -0.728138], [-2.711327, 2.854566, -0.736363], [-2.704249, 2.866198, -0.74344], [-2.719572, 2.865386, -0.743461], [-2.719552, 2.864575, -0.728138], [-2.704228, 2.865386, -0.728116], [-2.712474, 2.876207, -0.735215], [-2.719572, 2.865386, -0.743461], [-2.711327, 2.854566, -0.736363], [-2.704228, 2.865386, -0.728116], [-2.704249, 2.866198, -0.74344], [-2.719572, 2.865386, -0.743461], [-1.988056, 2.865386, -0.011944]]}, {"shapeName": "R_squint_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-2.034541, 3.887002, 0.034541], [-2.034519, 3.88619, 0.049865], [-2.049843, 3.885379, 0.049843], [-2.049865, 3.88619, 0.034519], [-2.034541, 3.887002, 0.034541], [-2.042766, 3.89701, 0.042766], [-2.049843, 3.885379, 0.049843], [-2.041618, 3.87537, 0.041618], [-2.034519, 3.88619, 0.049865], [-2.042766, 3.89701, 0.042766], [-2.049865, 3.88619, 0.034519], [-2.041618, 3.87537, 0.041618], [-2.034541, 3.887002, 0.034541], [-2.042766, 3.89701, 0.042766], [-1.988056, 2.865386, -0.011944]]}, {"shapeName": "R_squint_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.710447, 2.799647, 0.710447], [-2.7022, 2.788826, 0.717546], [-2.709299, 2.778006, 0.709299], [-2.717546, 2.788826, 0.7022], [-2.710447, 2.799647, 0.710447], [-2.717524, 2.788015, 0.717524], [-2.709299, 2.778006, 0.709299], [-2.702222, 2.789638, 0.702222], [-2.7022, 2.788826, 0.717546], [-2.717524, 2.788015, 0.717524], [-2.717546, 2.788826, 0.7022], [-2.702222, 2.789638, 0.702222], [-2.710447, 2.799647, 0.710447], [-2.717524, 2.788015, 0.717524], [-1.988056, 2.865386, -0.011944]]}]},
			"R_cheekLower_C_C_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_C_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.087936, 2.154927, -0.315593], [-2.071874, 2.16544, -0.292949], [-2.051925, 2.153913, -0.274229], [-2.039776, 2.127099, -0.270399], [-2.042542, 2.100706, -0.283702], [-2.058605, 2.090193, -0.306346], [-2.078553, 2.10172, -0.325066], [-2.090703, 2.128534, -0.328896]]}]},
			"L_upperLidPrimary_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_upperLidPrimary_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.294331, 6.478618, 0.144183], [1.288845, 6.48089, 0.144183], [1.283359, 6.478618, 0.144183], [1.281087, 6.473132, 0.144183], [1.283359, 6.467646, 0.144183], [1.288845, 6.465374, 0.144183], [1.294331, 6.467646, 0.144183], [1.296603, 6.473132, 0.144183]]}]},
			"L_cheekLower_C_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_C_CTLShape", "degree": 3, "form": 2, "points": [[2.244598, 2.118072, -0.195697], [2.221652, 2.13309, -0.163348], [2.193154, 2.116623, -0.136605], [2.175797, 2.078318, -0.131133], [2.17975, 2.040612, -0.150138], [2.202696, 2.025594, -0.182487], [2.231194, 2.042061, -0.20923], [2.248551, 2.080367, -0.214702]]}]},
			"C_noseTip_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_noseTip_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.14105, 5.288258, -1.013724], [0.0, 5.346683, -1.013724], [-0.14105, 5.288258, -1.013724], [-0.199475, 5.147208, -1.013724], [-0.14105, 5.006158, -1.013724], [0.0, 4.947733, -1.013724], [0.14105, 5.006158, -1.013724], [0.199475, 5.147208, -1.013724]]}]},
			"C_noseBridge_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_noseBridge_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.156722, 5.90393, -1.313724], [0.0, 5.968847, -1.313724], [-0.156722, 5.90393, -1.313724], [-0.221639, 5.747208, -1.313724], [-0.156722, 5.590486, -1.313724], [0.0, 5.525569, -1.313724], [0.156722, 5.590486, -1.313724], [0.221639, 5.747208, -1.313724]]}]},
			"R_upperLid_A_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.897197, 6.359177, 0.144183], [-0.897197, 6.353732, 0.144183], [-0.902642, 6.353732, 0.144183], [-0.902642, 6.359177, 0.144183], [-0.897197, 6.359177, 0.144183]]}]},
			"R_cheekLower_C_A_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_C_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.094421, 2.162673, -0.320149], [-2.07377, 2.17619, -0.291035], [-2.048121, 2.161369, -0.266966], [-2.0325, 2.126894, -0.262042], [-2.036058, 2.09296, -0.279146], [-2.056709, 2.079443, -0.30826], [-2.082358, 2.094264, -0.332329], [-2.097978, 2.128739, -0.337253]]}]},
			"L_upperLipSecondary_C_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_upperLipSecondary_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.282093, 0.837044, -0.385637], [1.282093, 0.837044, -0.403637], [1.282093, 0.855044, -0.403637], [1.282093, 0.855044, -0.385637], [1.300093, 0.855044, -0.385637], [1.300093, 0.855044, -0.403637], [1.300093, 0.837044, -0.403637], [1.300093, 0.837044, -0.385637], [1.282093, 0.837044, -0.385637], [1.282093, 0.855044, -0.385637], [1.282093, 0.855044, -0.403637], [1.300093, 0.855044, -0.403637], [1.300093, 0.855044, -0.385637], [1.300093, 0.837044, -0.385637], [1.300093, 0.837044, -0.403637], [1.282093, 0.837044, -0.403637]]}]},
			"C_lookAt_B_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lookAt_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.398455, 6.024981, 3.061507], [-0.398455, 5.975019, 3.061507], [-0.398455, 5.975019, 3.011545], [-0.398455, 6.024981, 3.011545], [-0.398455, 6.024981, 3.061507], [0.398455, 6.024981, 3.061507], [0.398455, 5.975019, 3.061507], [0.398455, 5.975019, 3.011545], [0.398455, 6.024981, 3.011545], [0.398455, 6.024981, 3.061507], [0.398455, 5.975019, 3.061507], [-0.398455, 5.975019, 3.061507], [-0.398455, 5.975019, 3.011545], [0.398455, 5.975019, 3.011545], [0.398455, 6.024981, 3.011545], [-0.398455, 6.024981, 3.011545], [-0.398455, 6.024981, 3.061507], [-0.0248, 6.0248, 3.061326], [-0.024981, 5.601545, 3.061507], [-0.024981, 5.601545, 3.011545], [0.024981, 5.601545, 3.011545], [0.024981, 5.601545, 3.061507], [-0.024981, 5.601545, 3.061507], [-0.024981, 6.398455, 3.061507], [0.024981, 6.398455, 3.061507], [0.024981, 6.398455, 3.011545], [-0.024981, 6.398455, 3.011545], [-0.024981, 6.398455, 3.061507], [-0.024981, 6.398455, 3.011545], [-0.024981, 5.601545, 3.011545], [0.024981, 5.601545, 3.011545], [0.024981, 6.398455, 3.011545], [0.024981, 6.398455, 3.061507], [0.024981, 5.601545, 3.061507], [0.0248, 5.9752, 3.061326], [0.024981, 5.975019, 3.434981], [-0.024981, 5.975019, 3.434981], [-0.024981, 6.024981, 3.434981], [0.024981, 6.024981, 3.434981], [0.024981, 5.975019, 3.434981], [0.024981, 5.975019, 2.638071], [0.024981, 6.024981, 2.638071], [-0.024981, 6.024981, 2.638071], [-0.024981, 5.975019, 2.638071], [0.024981, 5.975019, 2.638071], [-0.024981, 5.975019, 2.638071], [-0.024981, 5.975019, 3.434981], [-0.024981, 6.024981, 3.434981], [-0.024981, 6.024981, 2.638071], [0.024981, 6.024981, 2.638071], [0.024981, 6.024981, 3.434981]]}]},
			"L_lowerLid_A_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.897197, 5.581327, 0.144183], [0.897197, 5.575882, 0.144183], [0.902642, 5.575882, 0.144183], [0.902642, 5.581327, 0.144183], [0.897197, 5.581327, 0.144183]]}]},
			"L_nostril_B_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "L_nostril_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.656722, 5.30393, -1.613724], [0.5, 5.368847, -1.613724], [0.343278, 5.30393, -1.613724], [0.278361, 5.147208, -1.613724], [0.343278, 4.990486, -1.613724], [0.5, 4.925569, -1.613724], [0.656722, 4.990486, -1.613724], [0.721639, 5.147208, -1.613724]]}]},
			"L_cheekLower_C_B_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_C_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.091179, 2.1588, -0.317871], [2.072822, 2.170815, -0.291992], [2.050023, 2.157641, -0.270597], [2.036138, 2.126997, -0.26622], [2.0393, 2.096833, -0.281424], [2.057657, 2.084818, -0.307303], [2.080456, 2.097992, -0.328698], [2.094341, 2.128636, -0.333075]]}]},
			"R_lookAt_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lookAt_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-3.023671, 6.0, 2.489149], [-3.023671, 6.010851, 2.5], [-3.023671, 6.0, 2.510851], [-3.023671, 5.989149, 2.5], [-3.023671, 6.0, 2.489149], [-3.034521, 6.0, 2.5], [-3.023671, 6.0, 2.510851], [-3.01282, 6.0, 2.5], [-3.023671, 6.010851, 2.5], [-3.034521, 6.0, 2.5], [-3.023671, 5.989149, 2.5], [-3.01282, 6.0, 2.5], [-3.023671, 6.0, 2.489149], [-3.034521, 6.0, 2.5], [-2.0, 6.0, 2.5]]}, {"shapeName": "R_lookAt_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-2.0, 7.023671, 2.489149], [-1.989149, 7.023671, 2.5], [-2.0, 7.023671, 2.510851], [-2.010851, 7.023671, 2.5], [-2.0, 7.023671, 2.489149], [-2.0, 7.034521, 2.5], [-2.0, 7.023671, 2.510851], [-2.0, 7.01282, 2.5], [-1.989149, 7.023671, 2.5], [-2.0, 7.034521, 2.5], [-2.010851, 7.023671, 2.5], [-2.0, 7.01282, 2.5], [-2.0, 7.023671, 2.489149], [-2.0, 7.034521, 2.5], [-2.0, 6.0, 2.5]]}, {"shapeName": "R_lookAt_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-2.0, 6.010851, 3.523671], [-1.989149, 6.0, 3.523671], [-2.0, 5.989149, 3.523671], [-2.010851, 6.0, 3.523671], [-2.0, 6.010851, 3.523671], [-2.0, 6.0, 3.534521], [-2.0, 5.989149, 3.523671], [-2.0, 6.0, 3.51282], [-1.989149, 6.0, 3.523671], [-2.0, 6.0, 3.534521], [-2.010851, 6.0, 3.523671], [-2.0, 6.0, 3.51282], [-2.0, 6.010851, 3.523671], [-2.0, 6.0, 3.534521], [-2.0, 6.0, 2.5]]}]},
			"L_squint_A_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_A_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.80511, 2.830028, 0.155009], [1.789199, 2.85907, 0.136], [1.827208, 2.856452, 0.138535], [1.80511, 2.830028, 0.155009], [1.786548, 2.857426, 0.174056], [1.789199, 2.85907, 0.136], [1.808646, 2.883851, 0.157581], [1.786548, 2.857426, 0.174056], [1.824557, 2.854808, 0.176591], [1.80511, 2.830028, 0.155009], [1.827208, 2.856452, 0.138535], [1.808646, 2.883851, 0.157581], [1.824557, 2.854808, 0.176591], [1.827208, 2.856452, 0.138535]]}]},
			"R_innerLid_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_innerLid_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.508272, 5.970252, 0.144183], [-0.508272, 5.964807, 0.144183], [-0.513717, 5.964807, 0.144183], [-0.513717, 5.970252, 0.144183], [-0.508272, 5.970252, 0.144183]]}]},
			"C_brow_upper_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_brow_upper_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.027, 8.101573, -1.463748], [-0.027, 8.077313, -1.415504], [0.027, 8.077313, -1.415504], [0.027, 8.101573, -1.463748], [-0.027, 8.101573, -1.463748]]}]},
			"L_brow_A_D_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_brow_A_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.637479, 7.845417, -1.128471], [0.613228, 7.852251, -1.132026], [0.591094, 7.846505, -1.120865], [0.584044, 7.831545, -1.101528], [0.596206, 7.816133, -1.085341], [0.620458, 7.809299, -1.081787], [0.642591, 7.815045, -1.092947], [0.649641, 7.830005, -1.112284]]}]},
			"C_tongue_IK_E_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_tongue_IK_E_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.068566, -0.068566, -0.657066], [0.096967, 0.0, -0.657066], [0.068566, 0.068566, -0.657066], [0.0, 0.096967, -0.657066], [-0.068566, 0.068566, -0.657066], [-0.096967, 0.0, -0.657066], [-0.068566, -0.068566, -0.657066], [0.0, -0.096967, -0.657066]]}]},
			"R_upperLid_C_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_C_CTLShape", "degree": 1, "form": 0, "points": [[-1.67227, 6.356454, 0.151961], [-1.67777, 6.350954, 0.151961], [-1.68327, 6.356454, 0.151961], [-1.67777, 6.361954, 0.151961], [-1.67227, 6.356454, 0.151961]]}]},
			"L_squint_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_squint_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.570573, 2.839336, -0.525232], [2.578389, 2.849295, -0.516559], [2.584783, 2.837623, -0.508919], [2.576968, 2.827664, -0.517593], [2.570573, 2.839336, -0.525232], [2.585848, 2.838284, -0.524213], [2.584783, 2.837623, -0.508919], [2.569508, 2.838675, -0.509938], [2.578389, 2.849295, -0.516559], [2.585848, 2.838284, -0.524213], [2.576968, 2.827664, -0.517593], [2.569508, 2.838675, -0.509938], [2.570573, 2.839336, -0.525232], [2.585848, 2.838284, -0.524213], [1.806878, 2.856939, 0.156295]]}, {"shapeName": "L_squint_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.866802, 3.878106, 0.196896], [1.865737, 3.877445, 0.21219], [1.881012, 3.876392, 0.213209], [1.882078, 3.877053, 0.197915], [1.866802, 3.878106, 0.196896], [1.874618, 3.888063, 0.205569], [1.881012, 3.876392, 0.213209], [1.873197, 3.866434, 0.204536], [1.865737, 3.877445, 0.21219], [1.874618, 3.888063, 0.205569], [1.882078, 3.877053, 0.197915], [1.873197, 3.866434, 0.204536], [1.866802, 3.878106, 0.196896], [1.874618, 3.888063, 0.205569], [1.806878, 2.856939, 0.156295]]}, {"shapeName": "L_squint_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.477869, 2.78695, 0.92629], [2.468988, 2.77633, 0.932911], [2.476448, 2.765319, 0.925256], [2.485329, 2.775939, 0.918635], [2.477869, 2.78695, 0.92629], [2.484263, 2.775278, 0.933929], [2.476448, 2.765319, 0.925256], [2.470054, 2.776991, 0.917617], [2.468988, 2.77633, 0.932911], [2.484263, 2.775278, 0.933929], [2.485329, 2.775939, 0.918635], [2.470054, 2.776991, 0.917617], [2.477869, 2.78695, 0.92629], [2.484263, 2.775278, 0.933929], [1.806878, 2.856939, 0.156295]]}]},
			"L_squint_B_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_B_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.987104, 2.847437, -0.012896], [1.975363, 2.866732, -0.024637], [2.000784, 2.865386, -0.024672], [1.987104, 2.847437, -0.012896], [1.975328, 2.865386, 0.000784], [1.975363, 2.866732, -0.024637], [1.989008, 2.883336, -0.010992], [1.975328, 2.865386, 0.000784], [2.000748, 2.86404, 0.000748], [1.987104, 2.847437, -0.012896], [2.000784, 2.865386, -0.024672], [1.989008, 2.883336, -0.010992], [2.000748, 2.86404, 0.000748], [2.000784, 2.865386, -0.024672]]}]},
			"L_lowerLid_A_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_A_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.896808, 5.581716, 0.144183], [0.896808, 5.575493, 0.144183], [0.903031, 5.575493, 0.144183], [0.903031, 5.581716, 0.144183], [0.896808, 5.581716, 0.144183]]}]},
			"L_cheekLower_C_D_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_cheekLower_C_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[2.084694, 2.151054, -0.313315], [2.070926, 2.160065, -0.293906], [2.053827, 2.150185, -0.27786], [2.043413, 2.127202, -0.274577], [2.045785, 2.104579, -0.28598], [2.059553, 2.095568, -0.305389], [2.076651, 2.105448, -0.321435], [2.087065, 2.128431, -0.324718]]}]},
			"C_lookAt_C_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_lookAt_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.348648, 6.021858, 3.058384], [-0.348648, 5.978142, 3.058384], [-0.348648, 5.978142, 3.014668], [-0.348648, 6.021858, 3.014668], [-0.348648, 6.021858, 3.058384], [0.348648, 6.021858, 3.058384], [0.348648, 5.978142, 3.058384], [0.348648, 5.978142, 3.014668], [0.348648, 6.021858, 3.014668], [0.348648, 6.021858, 3.058384], [0.348648, 5.978142, 3.058384], [-0.348648, 5.978142, 3.058384], [-0.348648, 5.978142, 3.014668], [0.348648, 5.978142, 3.014668], [0.348648, 6.021858, 3.014668], [-0.348648, 6.021858, 3.014668], [-0.348648, 6.021858, 3.058384], [-0.0217, 6.0217, 3.058226], [-0.021858, 5.651352, 3.058384], [-0.021858, 5.651352, 3.014668], [0.021858, 5.651352, 3.014668], [0.021858, 5.651352, 3.058384], [-0.021858, 5.651352, 3.058384], [-0.021858, 6.348648, 3.058384], [0.021858, 6.348648, 3.058384], [0.021858, 6.348648, 3.014668], [-0.021858, 6.348648, 3.014668], [-0.021858, 6.348648, 3.058384], [-0.021858, 6.348648, 3.014668], [-0.021858, 5.651352, 3.014668], [0.021858, 5.651352, 3.014668], [0.021858, 6.348648, 3.014668], [0.021858, 6.348648, 3.058384], [0.021858, 5.651352, 3.058384], [0.0217, 5.9783, 3.058226], [0.021858, 5.978142, 3.385174], [-0.021858, 5.978142, 3.385174], [-0.021858, 6.021858, 3.385174], [0.021858, 6.021858, 3.385174], [0.021858, 5.978142, 3.385174], [0.021858, 5.978142, 2.687878], [0.021858, 6.021858, 2.687878], [-0.021858, 6.021858, 2.687878], [-0.021858, 5.978142, 2.687878], [0.021858, 5.978142, 2.687878], [-0.021858, 5.978142, 2.687878], [-0.021858, 5.978142, 3.385174], [-0.021858, 6.021858, 3.385174], [-0.021858, 6.021858, 2.687878], [0.021858, 6.021858, 2.687878], [0.021858, 6.021858, 3.385174]]}]},
			"R_outterLid_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_outterLid_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-2.063194, 5.97103, 0.144183], [-2.063194, 5.964029, 0.144183], [-2.070195, 5.964029, 0.144183], [-2.070195, 5.97103, 0.144183], [-2.063194, 5.97103, 0.144183]]}]},
			"L_lowerLip_A_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "L_lowerLip_A_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.12026, -0.595699, -0.394637], [1.102629, -0.588396, -0.394637], [1.084997, -0.595699, -0.394637], [1.077694, -0.61333, -0.394637], [1.084997, -0.630961, -0.394637], [1.102629, -0.638264, -0.394637], [1.12026, -0.630961, -0.394637], [1.127563, -0.61333, -0.394637]]}]},
			"world_D_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -346.62], [153.99, 0.0, -192.48], [115.44, 0.0, -192.48], [115.44, 0.0, -115.41], [192.51, 0.0, -115.41], [192.51, 0.0, -153.96], [346.62, 0.0, 0.0], [192.48, 0.0, 153.99], [192.48, 0.0, 115.44], [115.41, 0.0, 115.44], [115.41, 0.0, 192.51], [153.96, 0.0, 192.51], [0.0, 0.0, 346.62], [-153.99, 0.0, 192.48], [-115.44, 0.0, 192.48], [-115.44, 0.0, 115.41], [-192.51, 0.0, 115.41], [-192.51, 0.0, 153.96], [-346.62, 0.0, 0.0], [-192.48, 0.0, -153.99], [-192.48, 0.0, -115.44], [-115.41, 0.0, -115.44], [-115.41, 0.0, -192.51], [-153.96, 0.0, -192.51], [0.0, 0.0, -346.62], [30.18, 0.42, -316.98], [27.54, 0.0, -314.16], [27.54, 0.0, -302.64], [25.14, 0.0, -302.64], [25.29, 0.0, -314.25], [23.58, 0.0, -313.38], [23.64, 0.0, -308.34], [21.21, 0.0, -308.34], [21.21, 0.0, -313.38], [19.71, 0.0, -314.25], [19.71, 0.0, -302.46], [17.28, 0.0, -302.46], [17.28, 0.0, -314.55], [19.23, 0.0, -316.5], [22.23, 0.0, -315.0], [25.53, 0.0, -316.5], [27.54, 0.0, -314.22], [25.53, 0.0, -316.5], [22.26, 0.0, -315.03], [19.23, 0.0, -316.47], [13.38, 0.0, -316.5], [15.36, 0.0, -314.55], [15.36, 0.0, -304.44], [13.38, 0.0, -302.46], [7.05, 0.0, -302.46], [5.1, 0.0, -304.44], [5.1, 0.0, -314.55], [7.05, 0.0, -316.5], [13.38, 0.0, -316.5], [12.63, 0.0, -314.25], [12.93, 0.0, -304.95], [7.5, 0.0, -305.01], [7.53, 0.0, -314.25], [12.66, 0.0, -314.31], [13.38, 0.0, -316.5], [7.05, 0.0, -316.5], [3.0, 0.0, -316.5], [3.15, 0.0, -302.46], [-3.69, 0.0, -302.46], [-5.67, 0.0, -304.44], [-5.67, 0.0, -308.67], [-3.66, 0.0, -310.62], [-3.54, 0.0, -310.77], [-7.47, 0.0, -316.44], [-7.47, 0.0, -316.5], [-4.65, 0.0, -316.5], [-0.72, 0.0, -310.8], [0.75, 0.0, -310.8], [0.75, 0.0, -304.8], [-3.03, 0.0, -304.8], [-3.06, 0.0, -308.37], [0.75, 0.0, -308.37], [0.75, 0.0, -316.5], [3.0, 0.0, -316.5], [-19.29, 0.0, -316.5], [-19.29, 0.0, -314.25], [-11.43, 0.0, -314.22], [-11.43, 0.0, -302.46], [-9.0, 0.0, -302.46], [-9.0, 0.0, -316.5], [-29.52, 0.0, -316.5], [-31.32, 0.0, -314.55], [-31.47, 0.0, -304.44], [-29.52, 0.0, -302.46], [-21.21, 0.0, -302.46], [-21.21, 0.0, -316.5], [-23.67, 0.0, -314.25], [-23.61, 0.0, -304.74], [-28.74, 0.0, -304.74], [-28.68, 0.0, -314.19], [-23.58, 0.0, -314.31], [-21.15, 0.0, -316.5]]}]},
			"L_squint_A_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_A_CTLShape", "degree": 1, "form": 0, "points": [[1.93587, 2.81125, 0.305203], [1.918191, 2.84352, 0.284082], [1.960424, 2.840611, 0.286898], [1.93587, 2.81125, 0.305203], [1.915245, 2.841693, 0.326366], [1.918191, 2.84352, 0.284082], [1.939799, 2.871053, 0.308061], [1.915245, 2.841693, 0.326366], [1.957478, 2.838784, 0.329183], [1.93587, 2.81125, 0.305203], [1.960424, 2.840611, 0.286898], [1.939799, 2.871053, 0.308061], [1.957478, 2.838784, 0.329183], [1.960424, 2.840611, 0.286898]]}]},
			"L_cheek_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_cheek_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[2.546711, 2.597085, -0.545902], [2.555076, 2.605943, -0.536571], [2.560736, 2.593415, -0.529752], [2.552371, 2.584557, -0.539082], [2.546711, 2.597085, -0.545902], [2.561893, 2.595055, -0.544965], [2.560736, 2.593415, -0.529752], [2.545554, 2.595445, -0.530688], [2.555076, 2.605943, -0.536571], [2.561893, 2.595055, -0.544965], [2.552371, 2.584557, -0.539082], [2.545554, 2.595445, -0.530688], [2.546711, 2.597085, -0.545902], [2.561893, 2.595055, -0.544965], [1.783006, 2.613676, 0.13564]]}, {"shapeName": "L_cheek_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[1.903601, 3.624269, 0.245999], [1.902443, 3.622629, 0.261213], [1.917625, 3.620599, 0.262149], [1.918783, 3.622239, 0.246935], [1.903601, 3.624269, 0.245999], [1.911965, 3.633126, 0.255329], [1.917625, 3.620599, 0.262149], [1.90926, 3.611741, 0.252819], [1.902443, 3.622629, 0.261213], [1.911965, 3.633126, 0.255329], [1.918783, 3.622239, 0.246935], [1.90926, 3.611741, 0.252819], [1.903601, 3.624269, 0.245999], [1.911965, 3.633126, 0.255329], [1.783006, 2.613676, 0.13564]]}, {"shapeName": "L_cheek_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.445883, 2.451249, 0.898682], [2.436361, 2.440752, 0.904565], [2.443178, 2.429863, 0.896171], [2.4527, 2.440361, 0.890288], [2.445883, 2.451249, 0.898682], [2.451542, 2.438721, 0.905501], [2.443178, 2.429863, 0.896171], [2.437518, 2.442391, 0.889351], [2.436361, 2.440752, 0.904565], [2.451542, 2.438721, 0.905501], [2.4527, 2.440361, 0.890288], [2.437518, 2.442391, 0.889351], [2.445883, 2.451249, 0.898682], [2.451542, 2.438721, 0.905501], [1.783006, 2.613676, 0.13564]]}]},
			"R_cheek_B_B_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_B_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.991791, 2.647673, -0.052536], [-1.971172, 2.660472, -0.028828], [-1.947464, 2.647673, -0.008209], [-1.934555, 2.616776, -0.002756], [-1.940007, 2.585878, -0.015665], [-1.960626, 2.573079, -0.039374], [-1.984335, 2.585878, -0.059993], [-1.997244, 2.616776, -0.065445]]}]},
			"C_brow_A_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_brow_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.035263, 7.847494, -1.067697], [-0.0, 7.856975, -1.078808], [-0.035263, 7.847494, -1.067697], [-0.049869, 7.824604, -1.040873], [-0.035263, 7.801715, -1.014049], [-0.0, 7.792234, -1.002938], [0.035263, 7.801715, -1.014049], [0.049869, 7.824604, -1.040873]]}]},
			"C_brow_D_OFF_CTL": {"color": 17, "shapes": [{"shapeName": "C_brow_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[0.023508, 7.839864, -1.058756], [-0.0, 7.846185, -1.066163], [-0.023508, 7.839864, -1.058756], [-0.033246, 7.824604, -1.040873], [-0.023508, 7.809345, -1.02299], [-0.0, 7.803024, -1.015583], [0.023508, 7.809345, -1.02299], [0.033246, 7.824604, -1.040873]]}]},
			"L_squint_A_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_A_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.805699, 2.838998, 0.155438], [1.795092, 2.85836, 0.142765], [1.820432, 2.856615, 0.144455], [1.805699, 2.838998, 0.155438], [1.793324, 2.857264, 0.168136], [1.795092, 2.85836, 0.142765], [1.808057, 2.87488, 0.157153], [1.793324, 2.857264, 0.168136], [1.818664, 2.855518, 0.169826], [1.805699, 2.838998, 0.155438], [1.820432, 2.856615, 0.144455], [1.808057, 2.87488, 0.157153], [1.818664, 2.855518, 0.169826], [1.820432, 2.856615, 0.144455]]}]},
			"L_squint_C_A_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "L_squint_C_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[2.160662, 2.848625, -0.198918], [2.141429, 2.877456, -0.214946], [2.17949, 2.876054, -0.217657], [2.160662, 2.848625, -0.198918], [2.144049, 2.875053, -0.176928], [2.141429, 2.877456, -0.214946], [2.162876, 2.902482, -0.195667], [2.144049, 2.875053, -0.176928], [2.18211, 2.873652, -0.179639], [2.160662, 2.848625, -0.198918], [2.17949, 2.876054, -0.217657], [2.162876, 2.902482, -0.195667], [2.18211, 2.873652, -0.179639], [2.17949, 2.876054, -0.217657]]}]},
			"R_brow_upper_B_B_OFF_CTL": {"color": 4, "shapes": [{"shapeName": "R_brow_upper_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.960016, 8.096699, -1.627051], [-0.971392, 8.075565, -1.585482], [-1.017391, 8.073622, -1.599058], [-1.006015, 8.094756, -1.640627], [-0.960016, 8.096699, -1.627051]]}]},
			"R_lipZipper_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_lipZipper_PIV_CTLShape", "degree": 1, "form": 0, "points": [[0.940556, 0.191217, 2.044512], [0.940556, 0.202068, 2.055363], [0.940556, 0.191217, 2.066214], [0.940556, 0.180366, 2.055363], [0.940556, 0.191217, 2.044512], [0.951406, 0.191217, 2.055363], [0.940556, 0.191217, 2.066214], [0.929705, 0.191217, 2.055363], [0.940556, 0.202068, 2.055363], [0.951406, 0.191217, 2.055363], [0.940556, 0.180366, 2.055363], [0.929705, 0.191217, 2.055363], [0.940556, 0.191217, 2.044512], [0.951406, 0.191217, 2.055363], [-0.083115, 0.191217, 2.055363]]}, {"shapeName": "R_lipZipper_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.083115, 1.214888, 2.044512], [-0.093966, 1.214888, 2.055363], [-0.083115, 1.214888, 2.066214], [-0.072264, 1.214888, 2.055363], [-0.083115, 1.214888, 2.044512], [-0.083115, 1.225738, 2.055363], [-0.083115, 1.214888, 2.066214], [-0.083115, 1.204037, 2.055363], [-0.093966, 1.214888, 2.055363], [-0.083115, 1.225738, 2.055363], [-0.072264, 1.214888, 2.055363], [-0.083115, 1.204037, 2.055363], [-0.083115, 1.214888, 2.044512], [-0.083115, 1.225738, 2.055363], [-0.083115, 0.191217, 2.055363]]}, {"shapeName": "R_lipZipper_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.083115, 0.202068, 3.079034], [-0.093966, 0.191217, 3.079034], [-0.083115, 0.180366, 3.079034], [-0.072264, 0.191217, 3.079034], [-0.083115, 0.202068, 3.079034], [-0.083115, 0.191217, 3.089884], [-0.083115, 0.180366, 3.079034], [-0.083115, 0.191217, 3.068183], [-0.093966, 0.191217, 3.079034], [-0.083115, 0.191217, 3.089884], [-0.072264, 0.191217, 3.079034], [-0.083115, 0.191217, 3.068183], [-0.083115, 0.202068, 3.079034], [-0.083115, 0.191217, 3.089884], [-0.083115, 0.191217, 2.055363]]}]},
			"L_brow_upper_B_B_OFF_CTL": {"color": 28, "shapes": [{"shapeName": "L_brow_upper_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.960016, 8.096699, -1.627051], [0.971392, 8.075565, -1.585482], [1.017391, 8.073622, -1.599058], [1.006015, 8.094756, -1.640627], [0.960016, 8.096699, -1.627051]]}]},
			"R_squint_B_B_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.986786, 2.841453, -0.013214], [-1.971133, 2.867181, -0.028867], [-2.005026, 2.865386, -0.028915], [-1.986786, 2.841453, -0.013214], [-1.971085, 2.865386, 0.005026], [-1.971133, 2.867181, -0.028867], [-1.989325, 2.889319, -0.010675], [-1.971085, 2.865386, 0.005026], [-2.004979, 2.863591, 0.004979], [-1.986786, 2.841453, -0.013214], [-2.005026, 2.865386, -0.028915], [-1.989325, 2.889319, -0.010675], [-2.004979, 2.863591, 0.004979], [-2.005026, 2.865386, -0.028915]]}]},
			"R_lookAt_B_OFF_CTL": {"color": 18, "shapes": [{"shapeName": "R_lookAt_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-2.156722, 6.156722, 2.5], [-2.0, 6.221639, 2.5], [-1.843278, 6.156722, 2.5], [-1.778361, 6.0, 2.5], [-1.843278, 5.843278, 2.5], [-2.0, 5.778361, 2.5], [-2.156722, 5.843278, 2.5], [-2.221639, 6.0, 2.5]]}]},
			"L_lipZipper_C_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_lipZipper_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.083115, 0.198096, 2.055363], [0.076115, 0.184217, 2.055363], [0.090115, 0.184217, 2.055363], [0.083115, 0.198096, 2.055363], [0.083115, 0.198096, 2.055363]]}]},
			"R_cheekLower_A_CTL": {"color": 28, "shapes": [{"shapeName": "R_cheekLower_A_CTLShape", "degree": 3, "form": 2, "points": [[-1.868764, 2.114905, 0.187846], [-1.842071, 2.131351, 0.216402], [-1.80977, 2.116313, 0.239404], [-1.790784, 2.078601, 0.243376], [-1.796234, 2.040304, 0.225992], [-1.822927, 2.023858, 0.197435], [-1.855227, 2.038896, 0.174434], [-1.874213, 2.076608, 0.170462]]}]},
			"L_lipCorner_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_lipCorner_PIV_CTLShape", "degree": 1, "form": 0, "points": [[3.023671, 0.191217, -0.405488], [3.023671, 0.202068, -0.394637], [3.023671, 0.191217, -0.383786], [3.023671, 0.180366, -0.394637], [3.023671, 0.191217, -0.405488], [3.034521, 0.191217, -0.394637], [3.023671, 0.191217, -0.383786], [3.01282, 0.191217, -0.394637], [3.023671, 0.202068, -0.394637], [3.034521, 0.191217, -0.394637], [3.023671, 0.180366, -0.394637], [3.01282, 0.191217, -0.394637], [3.023671, 0.191217, -0.405488], [3.034521, 0.191217, -0.394637], [2.0, 0.191217, -0.394637]]}, {"shapeName": "L_lipCorner_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.0, 1.214888, -0.405488], [1.989149, 1.214888, -0.394637], [2.0, 1.214888, -0.383786], [2.010851, 1.214888, -0.394637], [2.0, 1.214888, -0.405488], [2.0, 1.225738, -0.394637], [2.0, 1.214888, -0.383786], [2.0, 1.204037, -0.394637], [1.989149, 1.214888, -0.394637], [2.0, 1.225738, -0.394637], [2.010851, 1.214888, -0.394637], [2.0, 1.204037, -0.394637], [2.0, 1.214888, -0.405488], [2.0, 1.225738, -0.394637], [2.0, 0.191217, -0.394637]]}, {"shapeName": "L_lipCorner_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.0, 0.202068, 0.629034], [1.989149, 0.191217, 0.629034], [2.0, 0.180366, 0.629034], [2.010851, 0.191217, 0.629034], [2.0, 0.202068, 0.629034], [2.0, 0.191217, 0.639884], [2.0, 0.180366, 0.629034], [2.0, 0.191217, 0.618183], [1.989149, 0.191217, 0.629034], [2.0, 0.191217, 0.639884], [2.010851, 0.191217, 0.629034], [2.0, 0.191217, 0.618183], [2.0, 0.202068, 0.629034], [2.0, 0.191217, 0.639884], [2.0, 0.191217, -0.394637]]}]},
			"R_innerLid_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_innerLid_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.507494, 5.97103, 0.144183], [-0.507494, 5.964029, 0.144183], [-0.514495, 5.964029, 0.144183], [-0.514495, 5.97103, 0.144183], [-0.507494, 5.97103, 0.144183]]}]},
			"R_lipCornerSecondary_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_lipCornerSecondary_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.993, 0.184217, -0.387637], [-1.993, 0.184217, -0.401637], [-1.993, 0.198217, -0.401637], [-1.993, 0.198217, -0.387637], [-2.007, 0.198217, -0.387637], [-2.007, 0.198217, -0.401637], [-2.007, 0.184217, -0.401637], [-2.007, 0.184217, -0.387637], [-1.993, 0.184217, -0.387637], [-1.993, 0.198217, -0.387637], [-1.993, 0.198217, -0.401637], [-2.007, 0.198217, -0.401637], [-2.007, 0.198217, -0.387637], [-2.007, 0.184217, -0.387637], [-2.007, 0.184217, -0.401637], [-1.993, 0.184217, -0.401637]]}]},
			"R_lowerLip_A_CTL": {"color": 17, "shapes": [{"shapeName": "R_lowerLip_A_CTLShape", "degree": 3, "form": 2, "points": [[-1.122219, -0.61374, -0.384637], [-1.102629, -0.605625, -0.384637], [-1.083038, -0.61374, -0.384637], [-1.074924, -0.63333, -0.384637], [-1.083038, -0.65292, -0.384637], [-1.102629, -0.661035, -0.384637], [-1.122219, -0.65292, -0.384637], [-1.130333, -0.63333, -0.384637]]}]},
			"R_upperLid_A_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_A_CTLShape", "degree": 1, "form": 0, "points": [[-0.89442, 6.356454, 0.151961], [-0.89992, 6.350954, 0.151961], [-0.90542, 6.356454, 0.151961], [-0.89992, 6.361954, 0.151961], [-0.89442, 6.356454, 0.151961]]}]},
			"L_cheek_B_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_B_CTLShape", "degree": 3, "form": 2, "points": [[2.137671, 2.621753, 0.082261], [2.111896, 2.637751, 0.111896], [2.082261, 2.621753, 0.137671], [2.066125, 2.583131, 0.144486], [2.07294, 2.544509, 0.128349], [2.098714, 2.528511, 0.098714], [2.128349, 2.544509, 0.07294], [2.144486, 2.583131, 0.066125]]}]},
			"R_brow_C_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_C_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.691935, 7.81021, -1.506136], [-1.668231, 7.818319, -1.501685], [-1.650525, 7.813365, -1.484094], [-1.649191, 7.79825, -1.463668], [-1.665008, 7.781828, -1.452373], [-1.688712, 7.773719, -1.456824], [-1.706418, 7.778673, -1.474415], [-1.707753, 7.793788, -1.494841]]}]},
			"R_lipZipper_A_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_lipZipper_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.083115, 0.200062, 2.055363], [-0.092115, 0.182217, 2.055363], [-0.074115, 0.182217, 2.055363], [-0.083115, 0.200062, 2.055363], [-0.083115, 0.200062, 2.055363]]}]},
			"R_squint_B_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_B_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.986945, 2.844445, -0.013055], [-1.973248, 2.866957, -0.026752], [-2.002905, 2.865386, -0.026794], [-1.986945, 2.844445, -0.013055], [-1.973206, 2.865386, 0.002905], [-1.973248, 2.866957, -0.026752], [-1.989166, 2.886327, -0.010834], [-1.973206, 2.865386, 0.002905], [-2.002863, 2.863816, 0.002863], [-1.986945, 2.844445, -0.013055], [-2.002905, 2.865386, -0.026794], [-1.989166, 2.886327, -0.010834], [-2.002863, 2.863816, 0.002863], [-2.002905, 2.865386, -0.026794]]}]},
			"R_cheek_A_D_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_A_D_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.803636, 2.636419, 0.122894], [-1.787151, 2.646438, 0.139487], [-1.768238, 2.637265, 0.153826], [-1.757976, 2.614274, 0.157513], [-1.762377, 2.590933, 0.148387], [-1.778862, 2.580915, 0.131794], [-1.797775, 2.590087, 0.117455], [-1.808037, 2.613078, 0.113768]]}]},
			"R_cheek_C_CTL": {"color": 13, "shapes": [{"shapeName": "R_cheek_C_CTLShape", "degree": 3, "form": 2, "points": [[-2.320725, 2.629085, -0.116928], [-2.296848, 2.64436, -0.085383], [-2.269286, 2.627634, -0.057831], [-2.254184, 2.588706, -0.050412], [-2.260389, 2.550379, -0.067471], [-2.284266, 2.535104, -0.099016], [-2.311828, 2.55183, -0.126568], [-2.32693, 2.590758, -0.133987]]}]},
			"R_upperLidPrimary_A_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLidPrimary_A_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.294331, 6.478618, 0.144183], [-1.288845, 6.48089, 0.144183], [-1.283359, 6.478618, 0.144183], [-1.281087, 6.473132, 0.144183], [-1.283359, 6.467646, 0.144183], [-1.288845, 6.465374, 0.144183], [-1.294331, 6.467646, 0.144183], [-1.296603, 6.473132, 0.144183]]}]},
			"R_upperLid_C_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_upperLid_C_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-1.674658, 6.359566, 0.144183], [-1.674658, 6.353343, 0.144183], [-1.680881, 6.353343, 0.144183], [-1.680881, 6.359566, 0.144183], [-1.674658, 6.359566, 0.144183]]}]},
			"R_brow_C_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_C_CTLShape", "degree": 3, "form": 2, "points": [[-1.772857, 7.967398, -1.410038], [-1.73335, 7.980912, -1.402619], [-1.703841, 7.972655, -1.373301], [-1.701617, 7.947464, -1.339258], [-1.727979, 7.920094, -1.320432], [-1.767486, 7.906579, -1.327851], [-1.796995, 7.914836, -1.357169], [-1.79922, 7.940028, -1.391212]]}]},
			"R_upperLipSecondary_A_C_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "R_upperLipSecondary_A_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.468266, 1.341453, -0.387637], [-0.468266, 1.341453, -0.401637], [-0.468266, 1.355453, -0.401637], [-0.468266, 1.355453, -0.387637], [-0.482266, 1.355453, -0.387637], [-0.482266, 1.355453, -0.401637], [-0.482266, 1.341453, -0.401637], [-0.482266, 1.341453, -0.387637], [-0.468266, 1.341453, -0.387637], [-0.468266, 1.355453, -0.387637], [-0.468266, 1.355453, -0.401637], [-0.482266, 1.355453, -0.401637], [-0.482266, 1.355453, -0.387637], [-0.482266, 1.341453, -0.387637], [-0.482266, 1.341453, -0.401637], [-0.468266, 1.341453, -0.401637]]}]},
			"L_lowerLipSecondary_D_CTL": {"color": 20, "shapes": [{"shapeName": "L_lowerLipSecondary_D_CTLShape", "degree": 1, "form": 0, "points": [[1.642693, -0.154506, -0.384637], [1.642693, -0.154506, -0.404637], [1.642693, -0.134506, -0.404637], [1.642693, -0.134506, -0.384637], [1.662693, -0.134506, -0.384637], [1.662693, -0.134506, -0.404637], [1.662693, -0.154506, -0.404637], [1.662693, -0.154506, -0.384637], [1.642693, -0.154506, -0.384637], [1.642693, -0.134506, -0.384637], [1.642693, -0.134506, -0.404637], [1.662693, -0.134506, -0.404637], [1.662693, -0.134506, -0.384637], [1.662693, -0.154506, -0.384637], [1.662693, -0.154506, -0.404637], [1.642693, -0.154506, -0.404637]]}]},
			"R_brow_A_C_OFF_CTL": {"color": 13, "shapes": [{"shapeName": "R_brow_A_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-0.640918, 7.847857, -1.132066], [-0.612625, 7.855831, -1.136212], [-0.586803, 7.849127, -1.123192], [-0.578577, 7.831673, -1.100632], [-0.592767, 7.813693, -1.081747], [-0.62106, 7.805719, -1.0776], [-0.646882, 7.812423, -1.090621], [-0.655108, 7.829877, -1.113181]]}]},
			"R_lowerLidPrimary_C_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "R_lowerLidPrimary_C_OFF_CTLShape", "degree": 3, "form": 2, "points": [[-1.293112, 5.466193, 0.144183], [-1.288845, 5.467961, 0.144183], [-1.284578, 5.466193, 0.144183], [-1.282811, 5.461927, 0.144183], [-1.284578, 5.45766, 0.144183], [-1.288845, 5.455893, 0.144183], [-1.293112, 5.45766, 0.144183], [-1.294879, 5.461927, 0.144183]]}]},
			"C_upperLipSecondary_D_OFF_CTL": {"color": 20, "shapes": [{"shapeName": "C_upperLipSecondary_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.006, 1.410217, -0.388637], [-0.006, 1.410217, -0.400637], [-0.006, 1.422217, -0.400637], [-0.006, 1.422217, -0.388637], [0.006, 1.422217, -0.388637], [0.006, 1.422217, -0.400637], [0.006, 1.410217, -0.400637], [0.006, 1.410217, -0.388637], [-0.006, 1.410217, -0.388637], [-0.006, 1.422217, -0.388637], [-0.006, 1.422217, -0.400637], [0.006, 1.422217, -0.400637], [0.006, 1.422217, -0.388637], [0.006, 1.410217, -0.388637], [0.006, 1.410217, -0.400637], [-0.006, 1.410217, -0.400637]]}]},
			"R_squint_B_CTL": {"color": 20, "shapes": [{"shapeName": "R_squint_B_CTLShape", "degree": 1, "form": 0, "points": [[-2.127494, 2.820512, 0.127494], [-2.107927, 2.852672, 0.107927], [-2.150294, 2.850428, 0.107868], [-2.127494, 2.820512, 0.127494], [-2.107868, 2.850428, 0.150294], [-2.107927, 2.852672, 0.107927], [-2.130667, 2.880344, 0.130667], [-2.107868, 2.850428, 0.150294], [-2.150235, 2.848185, 0.150235], [-2.127494, 2.820512, 0.127494], [-2.150294, 2.850428, 0.107868], [-2.130667, 2.880344, 0.130667], [-2.150235, 2.848185, 0.150235], [-2.150294, 2.850428, 0.107868]]}]},
			"L_lowerLid_B_B_OFF_CTL": {"color": 6, "shapes": [{"shapeName": "L_lowerLid_B_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[1.285733, 5.465038, 0.144183], [1.285733, 5.458815, 0.144183], [1.291956, 5.458815, 0.144183], [1.291956, 5.465038, 0.144183], [1.285733, 5.465038, 0.144183]]}]},
			"L_cheek_B_B_OFF_CTL": {"color": 14, "shapes": [{"shapeName": "L_cheek_B_B_OFF_CTLShape", "degree": 3, "form": 2, "points": [[1.991791, 2.647673, -0.052536], [1.971172, 2.660472, -0.028828], [1.947464, 2.647673, -0.008209], [1.934555, 2.616776, -0.002756], [1.940007, 2.585878, -0.015665], [1.960626, 2.573079, -0.039374], [1.984335, 2.585878, -0.059993], [1.997244, 2.616776, -0.065445]]}]},
			"L_brow_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_brow_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.625428, 7.798795, -1.279396], [1.625572, 7.814084, -1.280707], [1.628076, 7.815354, -1.26562], [1.627932, 7.800065, -1.264309], [1.625428, 7.798795, -1.279396], [1.637456, 7.806824, -1.274263], [1.628076, 7.815354, -1.26562], [1.616047, 7.807326, -1.270752], [1.625572, 7.814084, -1.280707], [1.637456, 7.806824, -1.274263], [1.627932, 7.800065, -1.264309], [1.616047, 7.807326, -1.270752], [1.625428, 7.798795, -1.279396], [1.637456, 7.806824, -1.274263], [0.616843, 7.830775, -1.106906]]}, {"shapeName": "L_brow_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.504209, 8.483768, -1.887249], [0.494827, 8.492298, -1.878605], [0.506856, 8.500326, -1.873473], [0.516238, 8.491796, -1.882116], [0.504209, 8.483768, -1.887249], [0.504353, 8.499056, -1.888559], [0.506856, 8.500326, -1.873473], [0.506712, 8.485037, -1.872162], [0.494827, 8.492298, -1.878605], [0.504353, 8.499056, -1.888559], [0.516238, 8.491796, -1.882116], [0.506712, 8.485037, -1.872162], [0.504209, 8.483768, -1.887249], [0.504353, 8.499056, -1.888559], [0.616843, 7.830775, -1.106906]]}, {"shapeName": "L_brow_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.740545, 8.618848, -0.4653], [0.73102, 8.61209, -0.455346], [0.742905, 8.604829, -0.448902], [0.75243, 8.611587, -0.458857], [0.740545, 8.618848, -0.4653], [0.743049, 8.620117, -0.450214], [0.742905, 8.604829, -0.448902], [0.740401, 8.603559, -0.463989], [0.73102, 8.61209, -0.455346], [0.743049, 8.620117, -0.450214], [0.75243, 8.611587, -0.458857], [0.740401, 8.603559, -0.463989], [0.740545, 8.618848, -0.4653], [0.743049, 8.620117, -0.450214], [0.616843, 7.830775, -1.106906]]}]},
		}

		controlShapes.set_data(data)