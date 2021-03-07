# -*- rigBot: assembly -*-
from rigBot import guide
from rigBot.data import controlShapes
import maya.cmds as mc

class EncBiped():
	"""Generated assembly build."""

	def __init__(self):
		pass

	def build_guide(self):
		"""Build Assembly guide parts"""

		guide.build("worldRoot", **{'side': u'C', 'name': u''})
		guide.build("hand", **{'createIkCtrls': False, 'parent': u'R_wrist_end_JNT', 'numberFingers': 4, 'createThumb': True, 'pickWalkParent': u'R_arm_IK_CTL', 'numberThumbJoints': 3, 'numberJoints': 4, 'side': u'R', 'name': u''})
		guide.build("hand", **{'createIkCtrls': False, 'parent': u'L_wrist_end_JNT', 'numberFingers': 4, 'createThumb': True, 'pickWalkParent': u'L_arm_IK_CTL', 'numberThumbJoints': 3, 'numberJoints': 4, 'side': u'L', 'name': u''})
		guide.build("encBipedLeg", **{'pickWalkParent': u'C_hip_CTL', 'side': u'L', 'parent': u'hips_Mid_bind', 'name': u''})
		guide.build("encBipedArm", **{'pickWalkParent': u'C_chest_CTL', 'side': u'L', 'parent': u'chest_Mid_bind', 'name': u''})
		guide.build("encTorso", **{'numberMidCtrls': 1, 'parent': u'C_root_JNT', 'pickWalkParent': u'world_CTL', 'numberJoints': 5, 'side': u'C', 'name': u''})
		guide.build("encNeck", **{'pickWalkParent': u'C_chest_CTL', 'side': u'C', 'parent': u'chest_Mid_bind', 'name': u''})

		#Position nodes
		if mc.objExists("R_hand_guide"):
			if not mc.getAttr("R_hand_guide.rotateOrder", l=1):
				mc.setAttr("R_hand_guide.rotateOrder", 0)

			mc.xform("R_hand_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("R_hand_guide", a=1, ro=[-180.0, 0.0, 0.0])
			mc.xform("R_hand_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_hand_guide"):
			if not mc.getAttr("L_hand_guide.rotateOrder", l=1):
				mc.setAttr("L_hand_guide.rotateOrder", 0)

			mc.xform("L_hand_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_hand_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_hand_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_encBipedLeg_guide"):
			if not mc.getAttr("L_encBipedLeg_guide.rotateOrder", l=1):
				mc.setAttr("L_encBipedLeg_guide.rotateOrder", 0)

			mc.xform("L_encBipedLeg_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_encBipedLeg_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_encBipedLeg_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("L_encBipedArm_guide"):
			if not mc.getAttr("L_encBipedArm_guide.rotateOrder", l=1):
				mc.setAttr("L_encBipedArm_guide.rotateOrder", 0)

			mc.xform("L_encBipedArm_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_encBipedArm_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_encBipedArm_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_worldRoot_guide"):
			if not mc.getAttr("C_worldRoot_guide.rotateOrder", l=1):
				mc.setAttr("C_worldRoot_guide.rotateOrder", 0)

			mc.xform("C_worldRoot_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_worldRoot_guide", r=1, s=[5.713929479459039, 5.713929479459039, 5.713929479459039])

		if mc.objExists("C_encTorso_guide"):
			if not mc.getAttr("C_encTorso_guide.rotateOrder", l=1):
				mc.setAttr("C_encTorso_guide.rotateOrder", 0)

			mc.xform("C_encTorso_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_encTorso_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_encTorso_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_encNeck_guide"):
			if not mc.getAttr("C_encNeck_guide.rotateOrder", l=1):
				mc.setAttr("C_encNeck_guide.rotateOrder", 0)

			mc.xform("C_encNeck_guide", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_encNeck_guide", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_encNeck_guide", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_root_JNT_PLC"):
			mc.xform("C_root_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_root_JNT_PLC", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_root_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

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

			mc.xform("L_thumb_D_JNT_PLC", a=1, t=[0.0, 0.0, 0.0])
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

		if mc.objExists("R_thumb_B_JNT_PLC"):
			if not mc.getAttr("R_thumb_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_B_JNT_PLC", a=1, t=[-4.477568247427371, 0.05035392245186898, -9.936432287815933e-05])
			mc.xform("R_thumb_B_JNT_PLC", a=1, ro=[9.700691778463726e-14, 6.327334678254903e-29, -7.474303501439264e-14])
			mc.xform("R_thumb_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_C_JNT_PLC"):
			if not mc.getAttr("R_thumb_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_C_JNT_PLC", a=1, t=[-7.70213136430484, 1.4536111496697686, 0.09318402078974941])
			mc.xform("R_thumb_C_JNT_PLC", a=1, ro=[9.700691778463726e-14, 6.327334678254903e-29, -7.474303501439264e-14])
			mc.xform("R_thumb_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_D_JNT_PLC"):
			if not mc.getAttr("R_thumb_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_D_JNT_PLC", a=1, t=[-0.0001743795683779581, 0.00023357226442755064, -7.6804955682519e-05])
			mc.xform("R_thumb_D_JNT_PLC", a=1, ro=[9.700691778463726e-14, 6.327334678254903e-29, -7.474303501439264e-14])
			mc.xform("R_thumb_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_thumb_A_JNT_PLC"):
			if not mc.getAttr("R_thumb_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_thumb_A_JNT_PLC", a=1, t=[46.45051379870371, 19.850333100648157, 105.56368560342072])
			mc.xform("R_thumb_A_JNT_PLC", a=1, ro=[-41.95659080235962, -58.80108123374742, -144.86009693886004])
			mc.xform("R_thumb_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_B_JNT_PLC"):
			if not mc.getAttr("R_index_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_B_JNT_PLC", a=1, t=[-6.101382328010111, 0.05033555245226751, 8.5104726831986e-05])
			mc.xform("R_index_B_JNT_PLC", a=1, ro=[-2.8624992133171654e-14, -1.272221872585407e-14, -1.9083328088781094e-14])
			mc.xform("R_index_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_C_JNT_PLC"):
			if not mc.getAttr("R_index_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_C_JNT_PLC", a=1, t=[-10.248969035089658, 0.7861323234389062, 0.08250284500319438])
			mc.xform("R_index_C_JNT_PLC", a=1, ro=[-2.8624992133171654e-14, -1.272221872585407e-14, -1.9083328088781094e-14])
			mc.xform("R_index_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_D_JNT_PLC"):
			if not mc.getAttr("R_index_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_D_JNT_PLC", a=1, t=[-12.46623073809372, 1.8148997232932516, 0.15836807448328472])
			mc.xform("R_index_D_JNT_PLC", a=1, ro=[-2.8624992133171654e-14, -1.272221872585407e-14, -1.9083328088781094e-14])
			mc.xform("R_index_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_E_JNT_PLC"):
			if not mc.getAttr("R_index_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_E_JNT_PLC", a=1, t=[-13.678517560253113, 3.154876532978193, 0.2376910070895022])
			mc.xform("R_index_E_JNT_PLC", a=1, ro=[-2.8624992133171654e-14, -1.272221872585407e-14, -1.9083328088781094e-14])
			mc.xform("R_index_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_index_A_JNT_PLC"):
			if not mc.getAttr("R_index_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_index_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_index_A_JNT_PLC", a=1, t=[60.96179999999998, 101.46700000000001, 8.224770000000012])
			mc.xform("R_index_A_JNT_PLC", a=1, ro=[17.093671884009307, -29.695891256926767, 127.43325677584139])
			mc.xform("R_index_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_B_JNT_PLC"):
			if not mc.getAttr("R_middle_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_B_JNT_PLC", a=1, t=[-5.910175638715142, 0.05002201888146374, -4.11365494734639e-06])
			mc.xform("R_middle_B_JNT_PLC", a=1, ro=[6.361109362927032e-15, -3.1805546814635168e-15, 1.2722218725854064e-14])
			mc.xform("R_middle_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_C_JNT_PLC"):
			if not mc.getAttr("R_middle_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_C_JNT_PLC", a=1, t=[-9.961558756363154, 0.9820682109625238, 0.15039971459635382])
			mc.xform("R_middle_C_JNT_PLC", a=1, ro=[6.361109362927032e-15, -3.1805546814635168e-15, 1.2722218725854064e-14])
			mc.xform("R_middle_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_D_JNT_PLC"):
			if not mc.getAttr("R_middle_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_D_JNT_PLC", a=1, t=[-12.542370780936299, 2.2622506265373232, 0.32742469392800544])
			mc.xform("R_middle_D_JNT_PLC", a=1, ro=[6.361109362927032e-15, -3.1805546814635168e-15, 1.2722218725854064e-14])
			mc.xform("R_middle_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_E_JNT_PLC"):
			if not mc.getAttr("R_middle_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_E_JNT_PLC", a=1, t=[-14.41163554339201, 3.663387399609192, 0.5110137402739028])
			mc.xform("R_middle_E_JNT_PLC", a=1, ro=[6.361109362927032e-15, -3.1805546814635168e-15, 1.2722218725854064e-14])
			mc.xform("R_middle_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_middle_A_JNT_PLC"):
			if not mc.getAttr("R_middle_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_middle_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_middle_A_JNT_PLC", a=1, t=[61.34569999999999, 101.21600000000001, 9.570430000000012])
			mc.xform("R_middle_A_JNT_PLC", a=1, ro=[5.65839285216573, -16.213196122326153, 131.92687935904758])
			mc.xform("R_middle_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_B_JNT_PLC"):
			if not mc.getAttr("R_ring_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_B_JNT_PLC", a=1, t=[-5.110919074856287, 0.05006104745089601, 2.0026147634411018e-05])
			mc.xform("R_ring_B_JNT_PLC", a=1, ro=[2.385416011097637e-15, -3.9725156682451414e-31, 1.9083328088781097e-14])
			mc.xform("R_ring_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_C_JNT_PLC"):
			if not mc.getAttr("R_ring_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_C_JNT_PLC", a=1, t=[-9.175572865721616, 0.9080968739428812, 0.8835378059919918])
			mc.xform("R_ring_C_JNT_PLC", a=1, ro=[2.385416011097637e-15, -3.9725156682451414e-31, 1.9083328088781097e-14])
			mc.xform("R_ring_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_D_JNT_PLC"):
			if not mc.getAttr("R_ring_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_D_JNT_PLC", a=1, t=[-11.572417594123031, 2.0580593174294393, 1.4327309720041015])
			mc.xform("R_ring_D_JNT_PLC", a=1, ro=[2.385416011097637e-15, -3.9725156682451414e-31, 1.9083328088781097e-14])
			mc.xform("R_ring_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_E_JNT_PLC"):
			if not mc.getAttr("R_ring_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_E_JNT_PLC", a=1, t=[-13.11686401299377, 3.7333655502022935, 1.8008499449456803])
			mc.xform("R_ring_E_JNT_PLC", a=1, ro=[2.385416011097637e-15, -3.9725156682451414e-31, 1.9083328088781097e-14])
			mc.xform("R_ring_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_ring_A_JNT_PLC"):
			if not mc.getAttr("R_ring_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_ring_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_ring_A_JNT_PLC", a=1, t=[61.61089999999999, 100.98000000000002, 11.538900000000012])
			mc.xform("R_ring_A_JNT_PLC", a=1, ro=[1.311093999357662, -8.988731512360909, 133.08394054046585])
			mc.xform("R_ring_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_B_JNT_PLC"):
			if not mc.getAttr("R_pinky_B_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_B_JNT_PLC", a=1, t=[-4.261270261967383, 0.04974340944923483, -4.645471337028084e-05])
			mc.xform("R_pinky_B_JNT_PLC", a=1, ro=[4.4139062980501586e-32, 1.987846675914698e-16, 2.5444437451708134e-14])
			mc.xform("R_pinky_B_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_C_JNT_PLC"):
			if not mc.getAttr("R_pinky_C_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_C_JNT_PLC", a=1, t=[-7.096166890392695, 0.4546162513985905, 0.9990669908935708])
			mc.xform("R_pinky_C_JNT_PLC", a=1, ro=[4.4139062980501586e-32, 1.987846675914698e-16, 2.5444437451708134e-14])
			mc.xform("R_pinky_C_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_D_JNT_PLC"):
			if not mc.getAttr("R_pinky_D_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_D_JNT_PLC", a=1, t=[-9.009611597991285, 1.212841743437366, 1.7293003809575431])
			mc.xform("R_pinky_D_JNT_PLC", a=1, ro=[4.4139062980501586e-32, 1.987846675914698e-16, 2.5444437451708134e-14])
			mc.xform("R_pinky_D_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_E_JNT_PLC"):
			if not mc.getAttr("R_pinky_E_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_E_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_E_JNT_PLC", a=1, t=[-10.385162116920423, 2.209170066717803, 2.3030854718915563])
			mc.xform("R_pinky_E_JNT_PLC", a=1, ro=[4.4139062980501586e-32, 1.987846675914698e-16, 2.5444437451708134e-14])
			mc.xform("R_pinky_E_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("R_pinky_A_JNT_PLC"):
			if not mc.getAttr("R_pinky_A_JNT_PLC.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_JNT_PLC.rotateOrder", 0)

			mc.xform("R_pinky_A_JNT_PLC", a=1, t=[61.74769999999999, 101.03600000000002, 13.229200000000013])
			mc.xform("R_pinky_A_JNT_PLC", a=1, ro=[3.2460799193349335, 0.14040009945875315, 128.1575637139514])
			mc.xform("R_pinky_A_JNT_PLC", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_world_PIV_CTL"):
			mc.xform("C_world_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_world_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_world_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

		if mc.objExists("C_visibility_PIV_CTL"):
			mc.xform("C_visibility_PIV_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("C_visibility_PIV_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("C_visibility_PIV_CTL", r=1, s=[1.0, 1.0, 1.0])

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

		if mc.objExists("R_thumb_A_PIV_CTL"):
			if not mc.getAttr("R_thumb_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_A_PIV_CTL", a=1, t=[-1.4210854715202004e-14, 0.0, 0.0])
			mc.xform("R_thumb_A_PIV_CTL", a=1, ro=[-1.5051988024868352e-14, -0.0011833865750323135, -179.9957849350297])
			mc.xform("R_thumb_A_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999997, -0.9999999999999994])

		if mc.objExists("R_thumb_B_PIV_CTL"):
			if not mc.getAttr("R_thumb_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_B_PIV_CTL", a=1, t=[-2.842170943040401e-14, -1.7763568394002505e-14, 0.0])
			mc.xform("R_thumb_B_PIV_CTL", a=1, ro=[0.00038082384632953604, -0.0009658537547749514, 179.9991896241336])
			mc.xform("R_thumb_B_PIV_CTL", r=1, s=[1.0000000000000002, 0.9999999999999999, -1.0])

		if mc.objExists("R_thumb_C_PIV_CTL"):
			if not mc.getAttr("R_thumb_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_thumb_C_PIV_CTL", a=1, t=[1.4210854715202004e-14, 2.1316282072803006e-14, 1.4210854715202004e-14])
			mc.xform("R_thumb_C_PIV_CTL", a=1, ro=[-0.00012889116644409387, -0.0006768332293113888, 179.99971162729793])
			mc.xform("R_thumb_C_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999997, -0.9999999999999997])

		if mc.objExists("R_index_A_PIV_CTL"):
			if not mc.getAttr("R_index_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_A_PIV_CTL", a=1, t=[0.0, -1.4210854715202004e-14, 0.0])
			mc.xform("R_index_A_PIV_CTL", a=1, ro=[7.158380930861685e-15, 0.0007529081131812897, -179.99703140745743])
			mc.xform("R_index_A_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, -0.9999999999999997])

		if mc.objExists("R_index_B_PIV_CTL"):
			if not mc.getAttr("R_index_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_B_PIV_CTL", a=1, t=[-2.1316282072803006e-14, 0.0, 1.0658141036401503e-14])
			mc.xform("R_index_B_PIV_CTL", a=1, ro=[-5.783572096862339e-05, 0.00037062289540970025, 179.99913176274907])
			mc.xform("R_index_B_PIV_CTL", r=1, s=[1.0000000000000007, 1.0, -1.0000000000000002])

		if mc.objExists("R_index_C_PIV_CTL"):
			if not mc.getAttr("R_index_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_C_PIV_CTL", a=1, t=[1.4210854715202004e-14, -1.4210854715202004e-14, 0.0])
			mc.xform("R_index_C_PIV_CTL", a=1, ro=[0.00028249956388618863, -0.0006919988332179992, -179.99891976944159])
			mc.xform("R_index_C_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0])

		if mc.objExists("R_index_D_PIV_CTL"):
			if not mc.getAttr("R_index_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_index_D_PIV_CTL", a=1, t=[0.0, -2.1316282072803006e-14, -1.0658141036401503e-14])
			mc.xform("R_index_D_PIV_CTL", a=1, ro=[-4.428772228958053e-05, 5.063680492113937e-05, 179.99957312804204])
			mc.xform("R_index_D_PIV_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, -1.0])

		if mc.objExists("R_middle_A_PIV_CTL"):
			if not mc.getAttr("R_middle_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_A_PIV_CTL", a=1, t=[0.0, 0.0, -3.552713678800501e-15])
			mc.xform("R_middle_A_PIV_CTL", a=1, ro=[-1.6633269311811773e-15, -3.750331286460347e-05, -179.99979927337927])
			mc.xform("R_middle_A_PIV_CTL", r=1, s=[0.9999999999999996, 0.9999999999999996, -0.9999999999999998])

		if mc.objExists("R_middle_B_PIV_CTL"):
			if not mc.getAttr("R_middle_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_B_PIV_CTL", a=1, t=[1.4210854715202004e-14, -1.4210854715202004e-14, -1.7763568394002505e-15])
			mc.xform("R_middle_B_PIV_CTL", a=1, ro=[4.589153691893429e-05, -0.000225327960521344, -179.9996989523899])
			mc.xform("R_middle_B_PIV_CTL", r=1, s=[1.0, 0.9999999999999999, -1.0])

		if mc.objExists("R_middle_C_PIV_CTL"):
			if not mc.getAttr("R_middle_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_C_PIV_CTL", a=1, t=[1.4210854715202004e-14, 1.4210854715202004e-14, -1.7763568394002505e-15])
			mc.xform("R_middle_C_PIV_CTL", a=1, ro=[-0.00010699752273503868, 0.00024181278155914238, 179.99916989354142])
			mc.xform("R_middle_C_PIV_CTL", r=1, s=[1.0, 0.9999999999999998, -0.9999999999999999])

		if mc.objExists("R_middle_D_PIV_CTL"):
			if not mc.getAttr("R_middle_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_middle_D_PIV_CTL", a=1, t=[-4.263256414560601e-14, 0.0, 1.7763568394002505e-15])
			mc.xform("R_middle_D_PIV_CTL", a=1, ro=[0.00019356637836936969, -0.0003003781114847126, -179.99853783060246])
			mc.xform("R_middle_D_PIV_CTL", r=1, s=[1.0, 1.0, -1.0000000000000002])

		if mc.objExists("R_ring_A_PIV_CTL"):
			if not mc.getAttr("R_ring_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_A_PIV_CTL", a=1, t=[7.105427357601002e-15, 1.4210854715202004e-14, -1.7763568394002505e-15])
			mc.xform("R_ring_A_PIV_CTL", a=1, ro=[1.1085190618936743e-14, 0.0002091541156898095, -179.99936241125673])
			mc.xform("R_ring_A_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -0.9999999999999998])

		if mc.objExists("R_ring_B_PIV_CTL"):
			if not mc.getAttr("R_ring_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_B_PIV_CTL", a=1, t=[-1.4210854715202004e-14, 0.0, -5.329070518200751e-15])
			mc.xform("R_ring_B_PIV_CTL", a=1, ro=[8.296318273104656e-05, -0.00045354231838498664, 179.9999671139772])
			mc.xform("R_ring_B_PIV_CTL", r=1, s=[1.0000000000000002, 1.0, -1.0])

		if mc.objExists("R_ring_C_PIV_CTL"):
			if not mc.getAttr("R_ring_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_C_PIV_CTL", a=1, t=[7.105427357601002e-15, -1.4210854715202004e-14, -1.7763568394002505e-15])
			mc.xform("R_ring_C_PIV_CTL", a=1, ro=[-0.00011226349686833478, 0.0002688578386523758, -179.99897057834846])
			mc.xform("R_ring_C_PIV_CTL", r=1, s=[0.9999999999999997, 1.0, -1.0])

		if mc.objExists("R_ring_D_PIV_CTL"):
			if not mc.getAttr("R_ring_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_ring_D_PIV_CTL", a=1, t=[0.0, 5.684341886080802e-14, -1.7763568394002505e-15])
			mc.xform("R_ring_D_PIV_CTL", a=1, ro=[0.0001766749439086491, -0.00020014108795879948, -179.99947900995645])
			mc.xform("R_ring_D_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, -0.9999999999999998])

		if mc.objExists("R_pinky_A_PIV_CTL"):
			if not mc.getAttr("R_pinky_A_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_A_PIV_CTL", a=1, t=[-7.105427357601002e-15, 0.0, 0.0])
			mc.xform("R_pinky_A_PIV_CTL", a=1, ro=[6.801260090299387e-15, -0.0005740948775293076, 179.99682901238174])
			mc.xform("R_pinky_A_PIV_CTL", r=1, s=[1.0, 1.0, -1.0])

		if mc.objExists("R_pinky_B_PIV_CTL"):
			if not mc.getAttr("R_pinky_B_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_B_PIV_CTL", a=1, t=[-7.105427357601002e-15, 1.4210854715202004e-14, -7.105427357601002e-15])
			mc.xform("R_pinky_B_PIV_CTL", a=1, ro=[9.583756079258992e-05, -0.000859480843349123, -179.99980768703702])
			mc.xform("R_pinky_B_PIV_CTL", r=1, s=[0.9999999999999999, 0.9999999999999997, -0.9999999999999999])

		if mc.objExists("R_pinky_C_PIV_CTL"):
			if not mc.getAttr("R_pinky_C_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_C_PIV_CTL", a=1, t=[-2.1316282072803006e-14, -2.842170943040401e-14, -1.4210854715202004e-14])
			mc.xform("R_pinky_C_PIV_CTL", a=1, ro=[-0.0002946534229582181, 0.0008979667047728545, -179.99988181484187])
			mc.xform("R_pinky_C_PIV_CTL", r=1, s=[1.0, 1.0000000000000002, -1.0])

		if mc.objExists("R_pinky_D_PIV_CTL"):
			if not mc.getAttr("R_pinky_D_PIV_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_PIV_CTL.rotateOrder", 0)

			mc.xform("R_pinky_D_PIV_CTL", a=1, t=[1.4210854715202004e-14, 0.0, 7.105427357601002e-15])
			mc.xform("R_pinky_D_PIV_CTL", a=1, ro=[-0.000418205023536433, 0.0007362695881773105, 179.9989607960529])
			mc.xform("R_pinky_D_PIV_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, -0.9999999999999997])

		if mc.objExists("R_hand_PIV_CTL"):
			mc.xform("R_hand_PIV_CTL", a=1, t=[-0.5, -2.0, 1.2246467991473532e-16])
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
			mc.xform("world_A_OFF_CTL", r=1, s=[0.5864588229197176, 0.5864588229197176, 0.5864588229197176])

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

			mc.xform("L_hand_CTL", a=1, t=[77.5952070400253, 108.12454486633015, 0.0])
			mc.xform("L_hand_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_hand_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("R_thumb_A_CTL"):
			if not mc.getAttr("R_thumb_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_CTL.rotateOrder", 0)

			mc.xform("R_thumb_A_CTL", a=1, t=[0.000238910301817441, -0.0003077826490169855, 0.00012300587958691267])
			mc.xform("R_thumb_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_thumb_A_CTL", r=1, s=[1.0000000000000002, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_thumb_B_CTL"):
			if not mc.getAttr("R_thumb_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_CTL.rotateOrder", 0)

			mc.xform("R_thumb_B_CTL", a=1, t=[-3.827254801080926e-05, 3.450642099167567e-05, 2.3047615968607715e-05])
			mc.xform("R_thumb_B_CTL", a=1, ro=[6.361109362927032e-15, 1.5902773407317584e-15, -3.180554681463516e-15])
			mc.xform("R_thumb_B_CTL", r=1, s=[1.0, 1.0000000000000002, 1.0])

		if mc.objExists("R_thumb_C_CTL"):
			if not mc.getAttr("R_thumb_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_CTL.rotateOrder", 0)

			mc.xform("R_thumb_C_CTL", a=1, t=[-1.5922931908107785e-05, -2.3182525787035502e-05, 4.160203177150379e-05])
			mc.xform("R_thumb_C_CTL", a=1, ro=[-2.067360542951286e-14, 1.590277340731758e-14, -9.541664044390553e-15])
			mc.xform("R_thumb_C_CTL", r=1, s=[0.9999999999999999, 1.0000000000000002, 1.0])

		if mc.objExists("R_index_A_CTL"):
			if not mc.getAttr("R_index_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_A_CTL.rotateOrder", 0)

			mc.xform("R_index_A_CTL", a=1, t=[0.0003149489605007716, -0.00027218796279271373, -0.0001036942648688921])
			mc.xform("R_index_A_CTL", a=1, ro=[8.74652537402467e-15, 9.144094709207612e-15, -1.90833280887811e-14])
			mc.xform("R_index_A_CTL", r=1, s=[0.9999999999999999, 0.9999999999999999, 1.0000000000000004])

		if mc.objExists("R_index_B_CTL"):
			if not mc.getAttr("R_index_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_B_CTL.rotateOrder", 0)

			mc.xform("R_index_B_CTL", a=1, t=[-1.4454881082315296e-05, 6.187569535143211e-05, -1.8679367890683807e-05])
			mc.xform("R_index_B_CTL", a=1, ro=[-7.95138670365879e-16, -3.975693351829395e-16, 2.7586914362813478e-33])
			mc.xform("R_index_B_CTL", r=1, s=[0.9999999999999998, 0.9999999999999999, 0.9999999999999998])

		if mc.objExists("R_index_C_CTL"):
			if not mc.getAttr("R_index_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_C_CTL.rotateOrder", 0)

			mc.xform("R_index_C_CTL", a=1, t=[-1.910017979867007e-05, -1.2253660301553282e-05, 1.0688317175322481e-05])
			mc.xform("R_index_C_CTL", a=1, ro=[-2.385416011097638e-15, -3.975693351829396e-15, 1.2722218725854067e-14])
			mc.xform("R_index_C_CTL", r=1, s=[1.0, 0.9999999999999996, 1.0])

		if mc.objExists("R_index_D_CTL"):
			if not mc.getAttr("R_index_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_D_CTL.rotateOrder", 0)

			mc.xform("R_index_D_CTL", a=1, t=[3.832921663615707e-06, 4.439261589794796e-05, -2.2484446539294822e-05])
			mc.xform("R_index_D_CTL", a=1, ro=[1.5902773407317576e-15, -7.951386703658789e-15, 6.361109362927032e-15])
			mc.xform("R_index_D_CTL", r=1, s=[0.9999999999999998, 0.9999999999999997, 1.0000000000000002])

		if mc.objExists("R_middle_A_CTL"):
			if not mc.getAttr("R_middle_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_A_CTL.rotateOrder", 0)

			mc.xform("R_middle_A_CTL", a=1, t=[-3.72612388446214e-05, -2.689711584480392e-05, 1.7835104936025914e-05])
			mc.xform("R_middle_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_middle_A_CTL", r=1, s=[1.0000000000000002, 1.0000000000000002, 1.0])

		if mc.objExists("R_middle_B_CTL"):
			if not mc.getAttr("R_middle_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_B_CTL.rotateOrder", 0)

			mc.xform("R_middle_B_CTL", a=1, t=[-5.169266594862165e-05, -1.5506161489042825e-05, 1.1902530026475233e-05])
			mc.xform("R_middle_B_CTL", a=1, ro=[1.5902773407317584e-15, -1.5902773407317584e-15, -2.2069531490250799e-32])
			mc.xform("R_middle_B_CTL", r=1, s=[0.9999999999999998, 0.9999999999999999, 0.9999999999999999])

		if mc.objExists("R_middle_C_CTL"):
			if not mc.getAttr("R_middle_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_C_CTL.rotateOrder", 0)

			mc.xform("R_middle_C_CTL", a=1, t=[9.230555093608928e-07, 8.670857710058044e-06, -5.762233504569281e-06])
			mc.xform("R_middle_C_CTL", a=1, ro=[-7.951386703658794e-16, 1.9878466759146984e-15, -1.379345718140675e-32])
			mc.xform("R_middle_C_CTL", r=1, s=[0.9999999999999999, 0.9999999999999997, 0.9999999999999999])

		if mc.objExists("R_middle_D_CTL"):
			if not mc.getAttr("R_middle_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_D_CTL.rotateOrder", 0)

			mc.xform("R_middle_D_CTL", a=1, t=[2.6281756120738464e-05, -3.4652374438337574e-05, 7.978014062715033e-06])
			mc.xform("R_middle_D_CTL", a=1, ro=[2.3854160110976376e-15, 7.951386703658794e-16, -6.3611093629270335e-15])
			mc.xform("R_middle_D_CTL", r=1, s=[0.9999999999999999, 1.0, 0.9999999999999999])

		if mc.objExists("R_ring_A_CTL"):
			if not mc.getAttr("R_ring_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_A_CTL.rotateOrder", 0)

			mc.xform("R_ring_A_CTL", a=1, t=[8.056650639076679e-05, -9.488693748949117e-05, -2.85526883523346e-05])
			mc.xform("R_ring_A_CTL", a=1, ro=[8.827812596100319e-32, -1.5902773407317584e-15, -6.3611093629270335e-15])
			mc.xform("R_ring_A_CTL", r=1, s=[1.0, 1.0, 0.9999999999999999])

		if mc.objExists("R_ring_B_CTL"):
			if not mc.getAttr("R_ring_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_B_CTL.rotateOrder", 0)

			mc.xform("R_ring_B_CTL", a=1, t=[-1.861925724711e-07, -3.44350522283321e-05, -9.963525796408135e-06])
			mc.xform("R_ring_B_CTL", a=1, ro=[2.5245652784116664e-14, 1.987846675914698e-16, 4.3794226550966417e-32])
			mc.xform("R_ring_B_CTL", r=1, s=[1.0, 0.9999999999999999, 1.0])

		if mc.objExists("R_ring_C_CTL"):
			if not mc.getAttr("R_ring_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_C_CTL.rotateOrder", 0)

			mc.xform("R_ring_C_CTL", a=1, t=[-1.2271224953508408e-05, -4.062919217062699e-05, -4.6367665722968354e-05])
			mc.xform("R_ring_C_CTL", a=1, ro=[-3.975693351829395e-16, -4.4139062980501564e-32, -1.2722218725854064e-14])
			mc.xform("R_ring_C_CTL", r=1, s=[1.0, 1.0000000000000002, 0.9999999999999999])

		if mc.objExists("R_ring_D_CTL"):
			if not mc.getAttr("R_ring_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_D_CTL.rotateOrder", 0)

			mc.xform("R_ring_D_CTL", a=1, t=[2.9658530706910824e-06, 1.612568193820607e-05, -3.207789906056746e-05])
			mc.xform("R_ring_D_CTL", a=1, ro=[7.951386703658794e-16, 5.963540027744092e-16, 1.90833280887811e-14])
			mc.xform("R_ring_D_CTL", r=1, s=[1.0000000000000002, 1.0000000000000004, 1.0000000000000002])

		if mc.objExists("R_pinky_A_CTL"):
			if not mc.getAttr("R_pinky_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_CTL.rotateOrder", 0)

			mc.xform("R_pinky_A_CTL", a=1, t=[-0.00034110449490754036, 0.0002523943627892322, 2.8143788252776858e-05])
			mc.xform("R_pinky_A_CTL", a=1, ro=[0.0, -1.987846675914698e-16, 0.0])
			mc.xform("R_pinky_A_CTL", r=1, s=[1.0000000000000004, 1.0, 0.9999999999999999])

		if mc.objExists("R_pinky_B_CTL"):
			if not mc.getAttr("R_pinky_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_CTL.rotateOrder", 0)

			mc.xform("R_pinky_B_CTL", a=1, t=[3.899545799157522e-05, 1.2604645860392338e-07, -7.109554804429763e-06])
			mc.xform("R_pinky_B_CTL", a=1, ro=[2.3854160110976374e-14, 5.565970692561156e-15, -6.361109362927032e-15])
			mc.xform("R_pinky_B_CTL", r=1, s=[1.0000000000000002, 0.9999999999999998, 1.0])

		if mc.objExists("R_pinky_C_CTL"):
			if not mc.getAttr("R_pinky_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_CTL.rotateOrder", 0)

			mc.xform("R_pinky_C_CTL", a=1, t=[-3.601237268924251e-05, 4.248576061627318e-06, -5.808647618010809e-05])
			mc.xform("R_pinky_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_C_CTL", r=1, s=[0.9999999999999998, 0.9999999999999998, 0.9999999999999999])

		if mc.objExists("R_pinky_D_CTL"):
			if not mc.getAttr("R_pinky_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_CTL.rotateOrder", 0)

			mc.xform("R_pinky_D_CTL", a=1, t=[-9.83806927479236e-06, 7.712201352205739e-06, -1.850206550457756e-05])
			mc.xform("R_pinky_D_CTL", a=1, ro=[4.770832022195275e-15, -7.951386703658797e-16, 1.2722218725854067e-14])
			mc.xform("R_pinky_D_CTL", r=1, s=[1.0, 0.9999999999999998, 1.0000000000000002])

		if mc.objExists("R_hand_CTL"):
			if not mc.getAttr("R_hand_CTL.mirrorMode", l=1):
				mc.setAttr("R_hand_CTL.mirrorMode", 0)

			if not mc.getAttr("R_hand_CTL.rotateOrder", l=1):
				mc.setAttr("R_hand_CTL.rotateOrder", 0)

			mc.xform("R_hand_CTL", a=1, t=[77.59520704002531, 108.12454486633014, -1.3241437777981561e-14])
			mc.xform("R_hand_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_hand_CTL", r=1, s=[15.0, 15.0, 15.0])

		# Apply contro shapes data
		data = {
			"R_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-65.618507, 96.164927, -10.486582], [-65.627729, 96.170345, -10.475578], [-65.618738, 96.163967, -10.464902], [-65.609516, 96.158549, -10.475906], [-65.618507, 96.164927, -10.486582], [-65.624521, 96.155353, -10.476208], [-65.618738, 96.163967, -10.464902], [-65.612723, 96.173543, -10.475276], [-65.627729, 96.170345, -10.475578], [-65.624521, 96.155353, -10.476208], [-65.609516, 96.158549, -10.475906], [-65.612723, 96.173543, -10.475276], [-65.618507, 96.164927, -10.486582], [-65.624521, 96.155353, -10.476208], [-65.0621, 97.0225, -10.4318]]}, {"shapeName": "R_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.921092, 97.579394, -10.427159], [-65.915308, 97.588009, -10.415854], [-65.921323, 97.578434, -10.40548], [-65.927107, 97.569818, -10.416785], [-65.921092, 97.579394, -10.427159], [-65.930313, 97.584811, -10.416156], [-65.921323, 97.578434, -10.40548], [-65.912101, 97.573016, -10.416484], [-65.915308, 97.588009, -10.415854], [-65.930313, 97.584811, -10.416156], [-65.927107, 97.569818, -10.416785], [-65.912101, 97.573016, -10.416484], [-65.921092, 97.579394, -10.427159], [-65.930313, 97.584811, -10.416156], [-65.0621, 97.0225, -10.4318]]}, {"shapeName": "R_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-65.082115, 96.983104, -9.409026], [-65.067109, 96.986301, -9.408724], [-65.063902, 96.971308, -9.409354], [-65.078907, 96.96811, -9.409656], [-65.082115, 96.983104, -9.409026], [-65.073124, 96.976726, -9.398351], [-65.063902, 96.971308, -9.409354], [-65.072893, 96.977686, -9.42003], [-65.067109, 96.986301, -9.408724], [-65.073124, 96.976726, -9.398351], [-65.078907, 96.96811, -9.409656], [-65.072893, 96.977686, -9.42003], [-65.082115, 96.983104, -9.409026], [-65.073124, 96.976726, -9.398351], [-65.0621, 97.0225, -10.4318]]}]},
			"L_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.924534, 92.208765, -10.685612], [67.934798, 92.212117, -10.674707], [67.924753, 92.207818, -10.663931], [67.914489, 92.204466, -10.674836], [67.924534, 92.208765, -10.685612], [67.928468, 92.198149, -10.675253], [67.924753, 92.207818, -10.663931], [67.920819, 92.218435, -10.67429], [67.934798, 92.212117, -10.674707], [67.928468, 92.198149, -10.675253], [67.914489, 92.204466, -10.674836], [67.920819, 92.218435, -10.67429], [67.924534, 92.208765, -10.685612], [67.928468, 92.198149, -10.675253], [67.563857, 93.165199, -10.629346]]}, {"shapeName": "L_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[68.521678, 93.526555, -10.634083], [68.517963, 93.536224, -10.622762], [68.521896, 93.525608, -10.612403], [68.525611, 93.515938, -10.623725], [68.521678, 93.526555, -10.634083], [68.53194, 93.529906, -10.623178], [68.521896, 93.525608, -10.612403], [68.511633, 93.522256, -10.623308], [68.517963, 93.536224, -10.622762], [68.53194, 93.529906, -10.623178], [68.525611, 93.515938, -10.623725], [68.511633, 93.522256, -10.623308], [68.521678, 93.526555, -10.634083], [68.53194, 93.529906, -10.623178], [67.563857, 93.165199, -10.629346]]}, {"shapeName": "L_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[67.584321, 93.124365, -9.606637], [67.570342, 93.130683, -9.60622], [67.564012, 93.116715, -9.606766], [67.577991, 93.110397, -9.607183], [67.584321, 93.124365, -9.606637], [67.574276, 93.120067, -9.595862], [67.564012, 93.116715, -9.606766], [67.574057, 93.121013, -9.617542], [67.570342, 93.130683, -9.60622], [67.574276, 93.120067, -9.595862], [67.577991, 93.110397, -9.607183], [67.574057, 93.121013, -9.617542], [67.584321, 93.124365, -9.606637], [67.574276, 93.120067, -9.595862], [67.563857, 93.165199, -10.629346]]}]},
			"L_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_A_CTLShape", "degree": 3, "form": 2, "points": [[60.694294, 101.361497, -8.602376], [60.79848, 101.43377, -8.612789], [60.851912, 101.525259, -8.542352], [60.82329, 101.58237, -8.432326], [60.729381, 101.571649, -8.347163], [60.625196, 101.499375, -8.336751], [60.571764, 101.407887, -8.407187], [60.600385, 101.350775, -8.517213]]}]},
			"L_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.427112, 93.760792, -14.092988], [66.438836, 93.761679, -14.083126], [66.430299, 93.754841, -14.072363], [66.418575, 93.753954, -14.082225], [66.427112, 93.760792, -14.092988], [66.432252, 93.748123, -14.08602], [66.430299, 93.754841, -14.072363], [66.425158, 93.767511, -14.079331], [66.438836, 93.761679, -14.083126], [66.432252, 93.748123, -14.08602], [66.418575, 93.753954, -14.082225], [66.425158, 93.767511, -14.079331], [66.427112, 93.760792, -14.092988], [66.432252, 93.748123, -14.08602], [66.094084, 94.67235, -13.767144]]}, {"shapeName": "L_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.048178, 95.039679, -13.819988], [67.046225, 95.046398, -13.806331], [67.051365, 95.033729, -13.799362], [67.053319, 95.02701, -13.81302], [67.048178, 95.039679, -13.819988], [67.059901, 95.040566, -13.810126], [67.051365, 95.033729, -13.799362], [67.039641, 95.032842, -13.809224], [67.046225, 95.046398, -13.806331], [67.059901, 95.040566, -13.810126], [67.053319, 95.02701, -13.81302], [67.039641, 95.032842, -13.809224], [67.048178, 95.039679, -13.819988], [67.059901, 95.040566, -13.810126], [66.094084, 94.67235, -13.767144]]}, {"shapeName": "L_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[66.254517, 94.395538, -12.794696], [66.24084, 94.40137, -12.7909], [66.234257, 94.387814, -12.793794], [66.247934, 94.381982, -12.797589], [66.254517, 94.395538, -12.794696], [66.24598, 94.388701, -12.783933], [66.234257, 94.387814, -12.793794], [66.242794, 94.394651, -12.804558], [66.24084, 94.40137, -12.7909], [66.24598, 94.388701, -12.783933], [66.247934, 94.381982, -12.797589], [66.242794, 94.394651, -12.804558], [66.254517, 94.395538, -12.794696], [66.24598, 94.388701, -12.783933], [66.094084, 94.67235, -13.767144]]}]},
			"world_A_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.007286, 0.0, 34.845546], [-15.484587, 0.0, 19.346688], [-11.609173, 0.0, 19.347496], [-11.607554, 0.0, 11.599685], [-19.355365, 0.0, 11.598066], [-19.356176, 0.0, 15.473479], [-34.845546, 0.0, -0.007286], [-19.346688, 0.0, -15.484587], [-19.347496, 0.0, -11.609173], [-11.599685, 0.0, -11.607554], [-11.598066, 0.0, -19.355365], [-15.473479, 0.0, -19.356176], [0.007286, 0.0, -34.845546], [15.484587, 0.0, -19.346688], [11.609173, 0.0, -19.347496], [11.607554, 0.0, -11.599685], [19.355365, 0.0, -11.598066], [19.356176, 0.0, -15.473479], [34.845546, 0.0, 0.007286], [19.346688, 0.0, 15.484587], [19.347496, 0.0, 11.609173], [11.599685, 0.0, 11.607554], [11.598066, 0.0, 19.355365], [15.473479, 0.0, 19.356176], [-0.007286, 0.0, 34.845546], [-3.040643, 0.042222, 31.865214], [-2.775185, 0.0, 31.581778], [-2.774944, 0.0, 30.423678], [-2.533673, 0.0, 30.423729], [-2.548997, 0.0, 31.590874], [-2.377073, 0.0, 31.503447], [-2.382999, 0.0, 30.996778], [-2.138712, 0.0, 30.996829], [-2.138818, 0.0, 31.503498], [-1.988042, 0.0, 31.590989], [-1.987795, 0.0, 30.405746], [-1.743508, 0.0, 30.405797], [-1.743761, 0.0, 31.621199], [-1.939836, 0.0, 31.817192], [-2.241391, 0.0, 31.666335], [-2.573172, 0.0, 31.81706], [-2.775188, 0.0, 31.58781], [-2.573172, 0.0, 31.81706], [-2.244407, 0.0, 31.669351], [-1.939833, 0.0, 31.814176], [-1.351738, 0.0, 31.817316], [-1.550744, 0.0, 31.621241], [-1.550533, 0.0, 30.604888], [-1.351443, 0.0, 30.405881], [-0.715091, 0.0, 30.406014], [-0.5191, 0.0, 30.605102], [-0.519311, 0.0, 31.621455], [-0.715386, 0.0, 31.817449], [-1.351738, 0.0, 31.817316], [-1.276293, 0.0, 31.59114], [-1.306256, 0.0, 30.656209], [-0.760383, 0.0, 30.662355], [-0.763592, 0.0, 31.591245], [-1.279309, 0.0, 31.597171], [-1.351738, 0.0, 31.817316], [-0.715386, 0.0, 31.817449], [-0.308242, 0.0, 31.817533], [-0.323026, 0.0, 30.406096], [0.364596, 0.0, 30.406237], [0.563603, 0.0, 30.605328], [0.563515, 0.0, 31.030568], [0.361409, 0.0, 31.226558], [0.349342, 0.0, 31.241635], [0.744306, 0.0, 31.811722], [0.744303, 0.0, 31.817753], [0.460809, 0.0, 31.817693], [0.065849, 0.0, 31.244593], [-0.08193, 0.0, 31.244563], [-0.081803, 0.0, 30.641386], [0.298199, 0.0, 30.641464], [0.301139, 0.0, 31.000355], [-0.081878, 0.0, 31.000276], [-0.08205, 0.0, 31.817581], [-0.308242, 0.0, 31.817533], [1.932562, 0.0, 31.818001], [1.93261, 0.0, 31.591809], [1.142448, 0.0, 31.588627], [1.142695, 0.0, 30.4064], [0.898408, 0.0, 30.406352], [0.898113, 0.0, 31.817783], [2.960979, 0.0, 31.818215], [3.141974, 0.0, 31.622221], [3.157265, 0.0, 30.605871], [2.961274, 0.0, 30.406783], [2.125874, 0.0, 30.406608], [2.125578, 0.0, 31.818043], [2.372929, 0.0, 31.591903], [2.367096, 0.0, 30.635864], [2.882813, 0.0, 30.635972], [2.876582, 0.0, 31.585976], [2.363882, 0.0, 31.597931], [2.119547, 0.0, 31.81804]]}]},
			"L_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_C_CTLShape", "degree": 3, "form": 2, "points": [[67.45268, 93.128889, -10.747471], [67.562183, 93.172451, -10.795408], [67.672667, 93.211765, -10.746069], [67.719411, 93.223801, -10.628355], [67.675034, 93.201509, -10.511221], [67.565531, 93.157947, -10.463284], [67.455048, 93.118633, -10.512623], [67.408304, 93.106597, -10.630337]]}]},
			"L_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.767251, 89.821742, -2.155873], [66.771318, 89.824205, -2.141282], [66.756526, 89.825272, -2.13734], [66.752459, 89.822809, -2.15193], [66.767251, 89.821742, -2.155873], [66.761618, 89.812824, -2.144728], [66.756526, 89.825272, -2.13734], [66.762158, 89.83419, -2.148485], [66.771318, 89.824205, -2.141282], [66.761618, 89.812824, -2.144728], [66.752459, 89.822809, -2.15193], [66.762158, 89.83419, -2.148485], [66.767251, 89.821742, -2.155873], [66.761618, 89.812824, -2.144728], [66.78735, 90.831395, -2.323847]]}, {"shapeName": "L_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.682264, 90.895482, -1.830855], [67.677171, 90.907931, -1.823467], [67.671539, 90.899012, -1.812322], [67.676631, 90.886564, -1.81971], [67.682264, 90.895482, -1.830855], [67.68633, 90.897945, -1.816265], [67.671539, 90.899012, -1.812322], [67.667472, 90.896549, -1.826912], [67.677171, 90.907931, -1.823467], [67.68633, 90.897945, -1.816265], [67.676631, 90.886564, -1.81971], [67.667472, 90.896549, -1.826912], [67.682264, 90.895482, -1.830855], [67.68633, 90.897945, -1.816265], [66.78735, 90.831395, -2.323847]]}, {"shapeName": "L_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[66.290862, 90.998605, -1.444323], [66.281703, 91.00859, -1.451526], [66.272004, 90.997209, -1.454971], [66.281163, 90.987223, -1.447769], [66.290862, 90.998605, -1.444323], [66.276071, 90.999672, -1.440382], [66.272004, 90.997209, -1.454971], [66.286796, 90.996142, -1.458914], [66.281703, 91.00859, -1.451526], [66.276071, 90.999672, -1.440382], [66.281163, 90.987223, -1.447769], [66.286796, 90.996142, -1.458914], [66.290862, 90.998605, -1.444323], [66.276071, 90.999672, -1.440382], [66.78735, 90.831395, -2.323847]]}]},
			"R_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_D_CTLShape", "degree": 3, "form": 2, "points": [[-66.743299, 90.804715, -2.481897], [-66.869503, 90.804356, -2.465804], [-66.947583, 90.819837, -2.366554], [-66.9318, 90.842089, -2.242287], [-66.8314, 90.858076, -2.165797], [-66.705196, 90.858434, -2.18189], [-66.627117, 90.842954, -2.281139], [-66.642899, 90.820702, -2.405406]]}]},
			"L_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.52269, 88.885946, -6.167311], [68.530925, 88.888837, -6.154688], [68.518223, 88.887729, -6.146148], [68.509989, 88.884838, -6.158771], [68.52269, 88.885946, -6.167311], [68.522238, 88.87621, -6.155458], [68.518223, 88.887729, -6.146148], [68.518675, 88.897465, -6.158001], [68.530925, 88.888837, -6.154688], [68.522238, 88.87621, -6.155458], [68.509989, 88.884838, -6.158771], [68.518675, 88.897465, -6.158001], [68.52269, 88.885946, -6.167311], [68.522238, 88.87621, -6.155458], [68.352369, 89.889469, -6.276646]]}, {"shapeName": "L_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[69.342151, 90.077168, -6.094655], [69.338136, 90.088687, -6.085345], [69.337684, 90.078951, -6.073492], [69.341699, 90.067431, -6.082802], [69.342151, 90.077168, -6.094655], [69.350385, 90.080058, -6.082032], [69.337684, 90.078951, -6.073492], [69.329449, 90.07606, -6.086115], [69.338136, 90.088687, -6.085345], [69.350385, 90.080058, -6.082032], [69.341699, 90.067431, -6.082802], [69.329449, 90.07606, -6.086115], [69.342151, 90.077168, -6.094655], [69.350385, 90.080058, -6.082032], [68.352369, 89.889469, -6.276646]]}, {"shapeName": "L_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[68.152131, 89.975532, -5.276387], [68.139881, 89.984161, -5.279699], [68.131195, 89.971534, -5.280469], [68.143445, 89.962905, -5.277157], [68.152131, 89.975532, -5.276387], [68.13943, 89.974424, -5.267848], [68.131195, 89.971534, -5.280469], [68.143896, 89.972642, -5.289009], [68.139881, 89.984161, -5.279699], [68.13943, 89.974424, -5.267848], [68.143445, 89.962905, -5.277157], [68.143896, 89.972642, -5.289009], [68.152131, 89.975532, -5.276387], [68.13943, 89.974424, -5.267848], [68.352369, 89.889469, -6.276646]]}]},
			"world_C_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.005667, 0.0, 27.102091], [-12.043567, 0.0, 15.047424], [-9.029357, 0.0, 15.048053], [-9.028097, 0.0, 9.021977], [-15.054173, 0.0, 9.020718], [-15.054804, 0.0, 12.034928], [-27.102091, 0.0, -0.005667], [-15.047424, 0.0, -12.043567], [-15.048053, 0.0, -9.029357], [-9.021977, 0.0, -9.028097], [-9.020718, 0.0, -15.054173], [-12.034928, 0.0, -15.054804], [0.005667, 0.0, -27.102091], [12.043567, 0.0, -15.047424], [9.029357, 0.0, -15.048053], [9.028097, 0.0, -9.021977], [15.054173, 0.0, -9.020718], [15.054804, 0.0, -12.034928], [27.102091, 0.0, 0.005667], [15.047424, 0.0, 12.043567], [15.048053, 0.0, 9.029357], [9.021977, 0.0, 9.028097], [9.020718, 0.0, 15.054173], [12.034928, 0.0, 15.054804], [-0.005667, 0.0, 27.102091], [-2.364945, 0.03284, 24.784056], [-2.158477, 0.0, 24.563605], [-2.15829, 0.0, 23.662861], [-1.970634, 0.0, 23.662901], [-1.982553, 0.0, 24.57068], [-1.848835, 0.0, 24.502681], [-1.853444, 0.0, 24.108605], [-1.663443, 0.0, 24.108645], [-1.663525, 0.0, 24.502721], [-1.546255, 0.0, 24.570769], [-1.546062, 0.0, 23.648913], [-1.356062, 0.0, 23.648953], [-1.356259, 0.0, 24.594266], [-1.508761, 0.0, 24.746705], [-1.743304, 0.0, 24.629371], [-2.001356, 0.0, 24.746602], [-2.15848, 0.0, 24.568297], [-2.001356, 0.0, 24.746602], [-1.74565, 0.0, 24.631717], [-1.508759, 0.0, 24.744359], [-1.051352, 0.0, 24.746801], [-1.206135, 0.0, 24.594299], [-1.20597, 0.0, 23.803801], [-1.051122, 0.0, 23.649019], [-0.556182, 0.0, 23.649122], [-0.403745, 0.0, 23.803968], [-0.403909, 0.0, 24.594465], [-0.556412, 0.0, 24.746905], [-1.051352, 0.0, 24.746801], [-0.992672, 0.0, 24.570886], [-1.015977, 0.0, 23.843718], [-0.591409, 0.0, 23.848499], [-0.593905, 0.0, 24.570968], [-0.995018, 0.0, 24.575578], [-1.051352, 0.0, 24.746801], [-0.556412, 0.0, 24.746905], [-0.239743, 0.0, 24.74697], [-0.251242, 0.0, 23.649185], [0.283575, 0.0, 23.649296], [0.438358, 0.0, 23.804144], [0.43829, 0.0, 24.134886], [0.281096, 0.0, 24.287323], [0.271711, 0.0, 24.299049], [0.578904, 0.0, 24.74245], [0.578902, 0.0, 24.747141], [0.358407, 0.0, 24.747095], [0.051216, 0.0, 24.30135], [-0.063723, 0.0, 24.301327], [-0.063624, 0.0, 23.832189], [0.231932, 0.0, 23.83225], [0.234219, 0.0, 24.111387], [-0.063683, 0.0, 24.111326], [-0.063817, 0.0, 24.747008], [-0.239743, 0.0, 24.74697], [1.503103, 0.0, 24.747334], [1.503141, 0.0, 24.571407], [0.88857, 0.0, 24.568932], [0.888763, 0.0, 23.649422], [0.698762, 0.0, 23.649385], [0.698532, 0.0, 24.747165], [2.302983, 0.0, 24.7475], [2.443758, 0.0, 24.595061], [2.45565, 0.0, 23.804566], [2.303213, 0.0, 23.64972], [1.653457, 0.0, 23.649584], [1.653228, 0.0, 24.747367], [1.845612, 0.0, 24.57148], [1.841075, 0.0, 23.827894], [2.242188, 0.0, 23.827979], [2.237342, 0.0, 24.566871], [1.838575, 0.0, 24.576169], [1.648536, 0.0, 24.747364]]}]},
			"R_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_D_CTLShape", "degree": 3, "form": 2, "points": [[-68.524947, 90.303452, -10.882141], [-68.642138, 90.309213, -10.931331], [-68.759902, 90.311158, -10.883222], [-68.809254, 90.308148, -10.765997], [-68.761285, 90.301946, -10.648323], [-68.644094, 90.296185, -10.599134], [-68.52633, 90.294239, -10.647242], [-68.476978, 90.29725, -10.764468]]}]},
			"R_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-62.05289, 100.240471, -11.139676], [-62.059447, 100.248978, -11.128716], [-62.050211, 100.242608, -11.118246], [-62.043654, 100.234101, -11.129206], [-62.05289, 100.240471, -11.139676], [-62.058871, 100.233713, -11.127266], [-62.050211, 100.242608, -11.118246], [-62.04423, 100.249368, -11.130657], [-62.059447, 100.248978, -11.128716], [-62.058871, 100.233713, -11.127266], [-62.043654, 100.234101, -11.129206], [-62.04423, 100.249368, -11.130657], [-62.05289, 100.240471, -11.139676], [-62.058871, 100.233713, -11.127266], [-61.3609, 100.98, -11.2889]]}, {"shapeName": "R_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-62.107185, 101.680659, -11.27648], [-62.098525, 101.689555, -11.26746], [-62.104507, 101.682796, -11.25505], [-62.113167, 101.6739, -11.26407], [-62.107185, 101.680659, -11.27648], [-62.113742, 101.689165, -11.26552], [-62.104507, 101.682796, -11.25505], [-62.09795, 101.674289, -11.26601], [-62.098525, 101.689555, -11.26746], [-62.113742, 101.689165, -11.26552], [-62.113167, 101.6739, -11.26407], [-62.09795, 101.674289, -11.26601], [-62.107185, 101.680659, -11.27648], [-62.113742, 101.689165, -11.26552], [-61.3609, 100.98, -11.2889]]}, {"shapeName": "R_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.242469, 101.08822, -10.27782], [-61.227252, 101.08861, -10.27976], [-61.226676, 101.073344, -10.27831], [-61.241894, 101.072954, -10.27637], [-61.242469, 101.08822, -10.27782], [-61.233234, 101.08185, -10.267351], [-61.226676, 101.073344, -10.27831], [-61.235912, 101.079714, -10.28878], [-61.227252, 101.08861, -10.27976], [-61.233234, 101.08185, -10.267351], [-61.241894, 101.072954, -10.27637], [-61.235912, 101.079714, -10.28878], [-61.242469, 101.08822, -10.27782], [-61.233234, 101.08185, -10.267351], [-61.3609, 100.98, -11.2889]]}]},
			"R_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-58.360896, 96.074423, -2.847783], [-58.368325, 96.084142, -2.838518], [-58.381683, 96.079865, -2.844744], [-58.374254, 96.070146, -2.854009], [-58.360896, 96.074423, -2.847783], [-58.370327, 96.084977, -2.853709], [-58.381683, 96.079865, -2.844744], [-58.372252, 96.06931, -2.838817], [-58.368325, 96.084142, -2.838518], [-58.370327, 96.084977, -2.853709], [-58.374254, 96.070146, -2.854009], [-58.372252, 96.06931, -2.838817], [-58.360896, 96.074423, -2.847783], [-58.370327, 96.084977, -2.853709], [-58.4621, 95.3381, -2.14379]]}, {"shapeName": "R_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-58.172055, 95.995537, -1.414632], [-58.183411, 95.990424, -1.405667], [-58.192842, 96.00098, -1.411594], [-58.181486, 96.006092, -1.420559], [-58.172055, 95.995537, -1.414632], [-58.179484, 96.005255, -1.405368], [-58.192842, 96.00098, -1.411594], [-58.185413, 95.991261, -1.420858], [-58.183411, 95.990424, -1.405667], [-58.179484, 96.005255, -1.405368], [-58.181486, 96.006092, -1.420559], [-58.185413, 95.991261, -1.420858], [-58.172055, 95.995537, -1.414632], [-58.179484, 96.005255, -1.405368], [-58.4621, 95.3381, -2.14379]]}, {"shapeName": "R_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-59.439671, 95.601821, -1.992712], [-59.443598, 95.58699, -1.993011], [-59.4456, 95.587826, -2.008202], [-59.441673, 95.602658, -2.007904], [-59.439671, 95.601821, -1.992712], [-59.453029, 95.597545, -1.998938], [-59.4456, 95.587826, -2.008202], [-59.432242, 95.592102, -2.001977], [-59.443598, 95.58699, -1.993011], [-59.453029, 95.597545, -1.998938], [-59.441673, 95.602658, -2.007904], [-59.432242, 95.592102, -2.001977], [-59.439671, 95.601821, -1.992712], [-59.453029, 95.597545, -1.998938], [-58.4621, 95.3381, -2.14379]]}]},
			"L_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[65.635372, 95.863556, -7.597983], [65.641884, 95.870551, -7.585976], [65.630227, 95.866084, -7.577052], [65.623715, 95.859089, -7.589058], [65.635372, 95.863556, -7.597983], [65.638147, 95.855694, -7.5851], [65.630227, 95.866084, -7.577052], [65.627451, 95.873947, -7.589934], [65.641884, 95.870551, -7.585976], [65.638147, 95.855694, -7.5851], [65.623715, 95.859089, -7.589058], [65.627451, 95.873947, -7.589934], [65.635372, 95.863556, -7.597983], [65.638147, 95.855694, -7.5851], [65.128259, 96.725837, -7.815532]]}, {"shapeName": "L_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.987829, 97.265249, -7.680652], [65.979909, 97.27564, -7.672604], [65.982684, 97.267777, -7.659721], [65.990605, 97.257386, -7.66777], [65.987829, 97.265249, -7.680652], [65.99434, 97.272244, -7.668646], [65.982684, 97.267777, -7.659721], [65.976173, 97.260782, -7.671728], [65.979909, 97.27564, -7.672604], [65.99434, 97.272244, -7.668646], [65.990605, 97.257386, -7.66777], [65.976173, 97.260782, -7.671728], [65.987829, 97.265249, -7.680652], [65.99434, 97.272244, -7.668646], [65.128259, 96.725837, -7.815532]]}, {"shapeName": "L_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[64.89466, 96.850821, -6.826679], [64.880228, 96.854217, -6.830637], [64.876492, 96.839358, -6.82976], [64.890924, 96.835963, -6.825803], [64.89466, 96.850821, -6.826679], [64.883004, 96.846354, -6.817755], [64.876492, 96.839358, -6.82976], [64.888148, 96.843826, -6.838685], [64.880228, 96.854217, -6.830637], [64.883004, 96.846354, -6.817755], [64.890924, 96.835963, -6.825803], [64.888148, 96.843826, -6.838685], [64.89466, 96.850821, -6.826679], [64.883004, 96.846354, -6.817755], [65.128259, 96.725837, -7.815532]]}]},
			"R_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.924577, 92.208766, -10.685566], [-67.934841, 92.212118, -10.674661], [-67.924796, 92.207819, -10.663885], [-67.914532, 92.204467, -10.67479], [-67.924577, 92.208766, -10.685566], [-67.928511, 92.19815, -10.675207], [-67.924796, 92.207819, -10.663885], [-67.920862, 92.218436, -10.674244], [-67.934841, 92.212118, -10.674661], [-67.928511, 92.19815, -10.675207], [-67.914532, 92.204467, -10.67479], [-67.920862, 92.218436, -10.674244], [-67.924577, 92.208766, -10.685566], [-67.928511, 92.19815, -10.675207], [-67.5639, 93.1652, -10.6293]]}, {"shapeName": "R_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-68.521721, 93.526556, -10.634037], [-68.518006, 93.536225, -10.622716], [-68.521939, 93.525609, -10.612357], [-68.525654, 93.515939, -10.623679], [-68.521721, 93.526556, -10.634037], [-68.531983, 93.529907, -10.623132], [-68.521939, 93.525609, -10.612357], [-68.511676, 93.522257, -10.623262], [-68.518006, 93.536225, -10.622716], [-68.531983, 93.529907, -10.623132], [-68.525654, 93.515939, -10.623679], [-68.511676, 93.522257, -10.623262], [-68.521721, 93.526556, -10.634037], [-68.531983, 93.529907, -10.623132], [-67.5639, 93.1652, -10.6293]]}, {"shapeName": "R_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-67.584364, 93.124366, -9.606591], [-67.570385, 93.130684, -9.606174], [-67.564055, 93.116716, -9.60672], [-67.578034, 93.110398, -9.607137], [-67.584364, 93.124366, -9.606591], [-67.574319, 93.120068, -9.595816], [-67.564055, 93.116716, -9.60672], [-67.5741, 93.121014, -9.617496], [-67.570385, 93.130684, -9.606174], [-67.574319, 93.120068, -9.595816], [-67.578034, 93.110398, -9.607137], [-67.5741, 93.121014, -9.617496], [-67.584364, 93.124366, -9.606591], [-67.574319, 93.120068, -9.595816], [-67.5639, 93.1652, -10.6293]]}]},
			"L_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[65.618478, 96.164909, -10.486592], [65.6277, 96.170327, -10.475588], [65.618709, 96.163949, -10.464912], [65.609487, 96.158531, -10.475916], [65.618478, 96.164909, -10.486592], [65.624492, 96.155335, -10.476218], [65.618709, 96.163949, -10.464912], [65.612694, 96.173525, -10.475286], [65.6277, 96.170327, -10.475588], [65.624492, 96.155335, -10.476218], [65.609487, 96.158531, -10.475916], [65.612694, 96.173525, -10.475286], [65.618478, 96.164909, -10.486592], [65.624492, 96.155335, -10.476218], [65.062071, 97.022482, -10.43181]]}, {"shapeName": "L_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.921063, 97.579376, -10.427169], [65.915279, 97.587991, -10.415864], [65.921294, 97.578416, -10.40549], [65.927078, 97.5698, -10.416795], [65.921063, 97.579376, -10.427169], [65.930284, 97.584793, -10.416166], [65.921294, 97.578416, -10.40549], [65.912072, 97.572998, -10.416494], [65.915279, 97.587991, -10.415864], [65.930284, 97.584793, -10.416166], [65.927078, 97.5698, -10.416795], [65.912072, 97.572998, -10.416494], [65.921063, 97.579376, -10.427169], [65.930284, 97.584793, -10.416166], [65.062071, 97.022482, -10.43181]]}, {"shapeName": "L_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.082086, 96.983086, -9.409036], [65.06708, 96.986283, -9.408734], [65.063873, 96.97129, -9.409364], [65.078878, 96.968092, -9.409666], [65.082086, 96.983086, -9.409036], [65.073095, 96.976708, -9.398361], [65.063873, 96.97129, -9.409364], [65.072864, 96.977668, -9.42004], [65.06708, 96.986283, -9.408734], [65.073095, 96.976708, -9.398361], [65.078878, 96.968092, -9.409666], [65.072864, 96.977668, -9.42004], [65.082086, 96.983086, -9.409036], [65.073095, 96.976708, -9.398361], [65.062071, 97.022482, -10.43181]]}]},
			"R_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.522721, 88.885977, -6.167315], [-68.530956, 88.888868, -6.154692], [-68.518254, 88.88776, -6.146152], [-68.51002, 88.884869, -6.158775], [-68.522721, 88.885977, -6.167315], [-68.522269, 88.876241, -6.155462], [-68.518254, 88.88776, -6.146152], [-68.518706, 88.897496, -6.158005], [-68.530956, 88.888868, -6.154692], [-68.522269, 88.876241, -6.155462], [-68.51002, 88.884869, -6.158775], [-68.518706, 88.897496, -6.158005], [-68.522721, 88.885977, -6.167315], [-68.522269, 88.876241, -6.155462], [-68.3524, 89.8895, -6.27665]]}, {"shapeName": "R_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-69.342182, 90.077199, -6.094659], [-69.338167, 90.088718, -6.085349], [-69.337715, 90.078982, -6.073496], [-69.34173, 90.067462, -6.082806], [-69.342182, 90.077199, -6.094659], [-69.350416, 90.080089, -6.082036], [-69.337715, 90.078982, -6.073496], [-69.32948, 90.076091, -6.086119], [-69.338167, 90.088718, -6.085349], [-69.350416, 90.080089, -6.082036], [-69.34173, 90.067462, -6.082806], [-69.32948, 90.076091, -6.086119], [-69.342182, 90.077199, -6.094659], [-69.350416, 90.080089, -6.082036], [-68.3524, 89.8895, -6.27665]]}, {"shapeName": "R_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-68.152162, 89.975563, -5.276391], [-68.139912, 89.984192, -5.279703], [-68.131226, 89.971565, -5.280473], [-68.143476, 89.962936, -5.277161], [-68.152162, 89.975563, -5.276391], [-68.139461, 89.974455, -5.267852], [-68.131226, 89.971565, -5.280473], [-68.143927, 89.972673, -5.289013], [-68.139912, 89.984192, -5.279703], [-68.139461, 89.974455, -5.267852], [-68.143476, 89.962936, -5.277161], [-68.143927, 89.972673, -5.289013], [-68.152162, 89.975563, -5.276391], [-68.139461, 89.974455, -5.267852], [-68.3524, 89.8895, -6.27665]]}]},
			"R_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_A_CTLShape", "degree": 3, "form": 2, "points": [[-61.289857, 100.887727, -11.407642], [-61.381403, 100.963509, -11.453062], [-61.460932, 101.048877, -11.402329], [-61.481857, 101.093824, -11.285161], [-61.431921, 101.072021, -11.170193], [-61.340375, 100.99624, -11.124773], [-61.260846, 100.910871, -11.175506], [-61.23992, 100.865924, -11.292675]]}]},
			"L_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_D_CTLShape", "degree": 3, "form": 2, "points": [[68.263169, 89.858161, -6.413377], [68.386585, 89.875818, -6.438742], [68.489957, 89.901471, -6.369153], [68.512733, 89.920093, -6.245375], [68.441569, 89.920776, -6.139915], [68.318154, 89.903119, -6.11455], [68.214781, 89.877466, -6.184138], [68.192006, 89.858844, -6.307917]]}]},
			"L_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_B_CTLShape", "degree": 3, "form": 2, "points": [[65.057721, 96.650061, -7.945588], [65.167667, 96.706472, -7.975857], [65.254528, 96.774226, -7.91221], [65.267423, 96.813635, -7.79193], [65.198797, 96.801612, -7.685476], [65.088851, 96.745202, -7.655207], [65.001989, 96.677447, -7.718854], [64.989095, 96.638039, -7.839134]]}]},
			"R_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-65.635413, 95.863519, -7.597981], [-65.641925, 95.870514, -7.585974], [-65.630268, 95.866047, -7.57705], [-65.623756, 95.859052, -7.589056], [-65.635413, 95.863519, -7.597981], [-65.638188, 95.855657, -7.585098], [-65.630268, 95.866047, -7.57705], [-65.627492, 95.87391, -7.589932], [-65.641925, 95.870514, -7.585974], [-65.638188, 95.855657, -7.585098], [-65.623756, 95.859052, -7.589056], [-65.627492, 95.87391, -7.589932], [-65.635413, 95.863519, -7.597981], [-65.638188, 95.855657, -7.585098], [-65.1283, 96.7258, -7.81553]]}, {"shapeName": "R_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.98787, 97.265212, -7.68065], [-65.97995, 97.275603, -7.672602], [-65.982725, 97.26774, -7.659719], [-65.990646, 97.257349, -7.667768], [-65.98787, 97.265212, -7.68065], [-65.994381, 97.272207, -7.668644], [-65.982725, 97.26774, -7.659719], [-65.976214, 97.260745, -7.671726], [-65.97995, 97.275603, -7.672602], [-65.994381, 97.272207, -7.668644], [-65.990646, 97.257349, -7.667768], [-65.976214, 97.260745, -7.671726], [-65.98787, 97.265212, -7.68065], [-65.994381, 97.272207, -7.668644], [-65.1283, 96.7258, -7.81553]]}, {"shapeName": "R_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-64.894701, 96.850784, -6.826677], [-64.880269, 96.85418, -6.830635], [-64.876533, 96.839321, -6.829758], [-64.890965, 96.835926, -6.825801], [-64.894701, 96.850784, -6.826677], [-64.883045, 96.846317, -6.817753], [-64.876533, 96.839321, -6.829758], [-64.888189, 96.843789, -6.838683], [-64.880269, 96.85418, -6.830635], [-64.883045, 96.846317, -6.817753], [-64.890965, 96.835926, -6.825801], [-64.888189, 96.843789, -6.838683], [-64.894701, 96.850784, -6.826677], [-64.883045, 96.846317, -6.817753], [-65.1283, 96.7258, -7.81553]]}]},
			"R_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-57.807666, 100.742936, -7.270901], [-57.794176, 100.748635, -7.266316], [-57.78687, 100.737655, -7.274161], [-57.80036, 100.731956, -7.278747], [-57.807666, 100.742936, -7.270901], [-57.797528, 100.733876, -7.263788], [-57.78687, 100.737655, -7.274161], [-57.797009, 100.746716, -7.281275], [-57.794176, 100.748635, -7.266316], [-57.797528, 100.733876, -7.263788], [-57.80036, 100.731956, -7.278747], [-57.797009, 100.746716, -7.281275], [-57.807666, 100.742936, -7.270901], [-57.797528, 100.733876, -7.263788], [-57.7728, 101.346, -8.09741]]}, {"shapeName": "R_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-57.491495, 102.135398, -7.509415], [-57.480838, 102.139178, -7.519789], [-57.470699, 102.130118, -7.512675], [-57.481357, 102.126337, -7.502301], [-57.491495, 102.135398, -7.509415], [-57.478006, 102.141097, -7.50483], [-57.470699, 102.130118, -7.512675], [-57.484189, 102.124418, -7.51726], [-57.480838, 102.139178, -7.519789], [-57.478006, 102.141097, -7.50483], [-57.481357, 102.126337, -7.502301], [-57.484189, 102.124418, -7.51726], [-57.491495, 102.135398, -7.509415], [-57.478006, 102.141097, -7.50483], [-57.7728, 101.346, -8.09741]]}, {"shapeName": "R_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-56.788783, 101.105269, -8.244989], [-56.791615, 101.10335, -8.259948], [-56.794967, 101.08859, -8.25742], [-56.792134, 101.090509, -8.242461], [-56.788783, 101.105269, -8.244989], [-56.781478, 101.094289, -8.252834], [-56.794967, 101.08859, -8.25742], [-56.802273, 101.099569, -8.249574], [-56.791615, 101.10335, -8.259948], [-56.781478, 101.094289, -8.252834], [-56.792134, 101.090509, -8.242461], [-56.802273, 101.099569, -8.249574], [-56.788783, 101.105269, -8.244989], [-56.781478, 101.094289, -8.252834], [-57.7728, 101.346, -8.09741]]}]},
			"C_world_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_world_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.849184, 0.0, -0.062002], [5.849184, 0.062002, 0.0], [5.849184, 0.0, 0.062002], [5.849184, -0.062002, 0.0], [5.849184, 0.0, -0.062002], [5.91118, 0.0, 0.0], [5.849184, 0.0, 0.062002], [5.787182, 0.0, 0.0], [5.849184, 0.062002, 0.0], [5.91118, 0.0, 0.0], [5.849184, -0.062002, 0.0], [5.787182, 0.0, 0.0], [5.849184, 0.0, -0.062002], [5.91118, 0.0, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 5.849184, -0.062002], [-0.062002, 5.849184, 0.0], [0.0, 5.849184, 0.062002], [0.062002, 5.849184, 0.0], [0.0, 5.849184, -0.062002], [0.0, 5.91118, 0.0], [0.0, 5.849184, 0.062002], [0.0, 5.787182, 0.0], [-0.062002, 5.849184, 0.0], [0.0, 5.91118, 0.0], [0.062002, 5.849184, 0.0], [0.0, 5.787182, 0.0], [0.0, 5.849184, -0.062002], [0.0, 5.91118, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 0.062002, 5.849184], [-0.062002, 0.0, 5.849184], [0.0, -0.062002, 5.849184], [0.062002, 0.0, 5.849184], [0.0, 0.062002, 5.849184], [0.0, 0.0, 5.91118], [0.0, -0.062002, 5.849184], [0.0, 0.0, 5.787182], [-0.062002, 0.0, 5.849184], [0.0, 0.0, 5.91118], [0.062002, 0.0, 5.849184], [0.0, 0.0, 5.787182], [0.0, 0.062002, 5.849184], [0.0, 0.0, 5.91118], [0.0, 0.0, 0.0]]}]},
			"R_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_A_CTLShape", "degree": 3, "form": 2, "points": [[-61.041234, 101.118892, -9.693871], [-61.138707, 101.192599, -9.729266], [-61.210959, 101.28002, -9.671615], [-61.215666, 101.329945, -9.554688], [-61.15007, 101.313129, -9.44698], [-61.052597, 101.239422, -9.411586], [-60.980345, 101.152001, -9.469237], [-60.975638, 101.102076, -9.586164]]}]},
			"R_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-61.257962, 100.758755, -7.976656], [-61.259581, 100.768456, -7.964876], [-61.24665, 100.763038, -7.958637], [-61.245031, 100.753338, -7.970417], [-61.257962, 100.758755, -7.976656], [-61.258035, 100.753413, -7.962272], [-61.24665, 100.763038, -7.958637], [-61.246577, 100.768381, -7.973022], [-61.259581, 100.768456, -7.964876], [-61.258035, 100.753413, -7.962272], [-61.245031, 100.753338, -7.970417], [-61.246577, 100.768381, -7.973022], [-61.257962, 100.758755, -7.976656], [-61.258035, 100.753413, -7.962272], [-60.7118, 101.467, -8.47477]]}, {"shapeName": "R_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-61.403801, 102.177961, -8.222404], [-61.392416, 102.187587, -8.21877], [-61.39249, 102.182243, -8.204385], [-61.403875, 102.172617, -8.208019], [-61.403801, 102.177961, -8.222404], [-61.40542, 102.18766, -8.210624], [-61.39249, 102.182243, -8.204385], [-61.39087, 102.172543, -8.216165], [-61.392416, 102.187587, -8.21877], [-61.40542, 102.18766, -8.210624], [-61.403875, 102.172617, -8.208019], [-61.39087, 102.172543, -8.216165], [-61.403801, 102.177961, -8.222404], [-61.40542, 102.18766, -8.210624], [-60.7118, 101.467, -8.47477]]}, {"shapeName": "R_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-60.185517, 101.676564, -7.622051], [-60.172512, 101.676489, -7.630197], [-60.170966, 101.661446, -7.627592], [-60.183971, 101.66152, -7.619446], [-60.185517, 101.676564, -7.622051], [-60.172586, 101.671146, -7.615813], [-60.170966, 101.661446, -7.627592], [-60.183897, 101.666863, -7.633831], [-60.172512, 101.676489, -7.630197], [-60.172586, 101.671146, -7.615813], [-60.183971, 101.66152, -7.619446], [-60.183897, 101.666863, -7.633831], [-60.185517, 101.676564, -7.622051], [-60.172586, 101.671146, -7.615813], [-60.7118, 101.467, -8.47477]]}]},
			"L_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[62.052879, 100.240345, -11.139694], [62.059436, 100.248852, -11.128734], [62.0502, 100.242482, -11.118264], [62.043643, 100.233975, -11.129224], [62.052879, 100.240345, -11.139694], [62.05886, 100.233587, -11.127284], [62.0502, 100.242482, -11.118264], [62.044219, 100.249242, -11.130675], [62.059436, 100.248852, -11.128734], [62.05886, 100.233587, -11.127284], [62.043643, 100.233975, -11.129224], [62.044219, 100.249242, -11.130675], [62.052879, 100.240345, -11.139694], [62.05886, 100.233587, -11.127284], [61.360889, 100.979874, -11.288918]]}, {"shapeName": "L_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[62.107174, 101.680533, -11.276498], [62.098514, 101.689429, -11.267478], [62.104496, 101.68267, -11.255068], [62.113156, 101.673774, -11.264088], [62.107174, 101.680533, -11.276498], [62.113731, 101.689039, -11.265538], [62.104496, 101.68267, -11.255068], [62.097939, 101.674163, -11.266028], [62.098514, 101.689429, -11.267478], [62.113731, 101.689039, -11.265538], [62.113156, 101.673774, -11.264088], [62.097939, 101.674163, -11.266028], [62.107174, 101.680533, -11.276498], [62.113731, 101.689039, -11.265538], [61.360889, 100.979874, -11.288918]]}, {"shapeName": "L_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.242458, 101.088094, -10.277838], [61.227241, 101.088484, -10.279778], [61.226665, 101.073218, -10.278328], [61.241883, 101.072828, -10.276388], [61.242458, 101.088094, -10.277838], [61.233223, 101.081724, -10.267369], [61.226665, 101.073218, -10.278328], [61.235901, 101.079588, -10.288798], [61.227241, 101.088484, -10.279778], [61.233223, 101.081724, -10.267369], [61.241883, 101.072828, -10.276388], [61.235901, 101.079588, -10.288798], [61.242458, 101.088094, -10.277838], [61.233223, 101.081724, -10.267369], [61.360889, 100.979874, -11.288918]]}]},
			"world_D_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.004858, 0.0, 23.230364], [-10.323058, 0.0, 12.897792], [-7.739449, 0.0, 12.898331], [-7.738369, 0.0, 7.733124], [-12.903576, 0.0, 7.732044], [-12.904117, 0.0, 10.315653], [-23.230364, 0.0, -0.004858], [-12.897792, 0.0, -10.323058], [-12.898331, 0.0, -7.739449], [-7.733124, 0.0, -7.738369], [-7.732044, 0.0, -12.903576], [-10.315653, 0.0, -12.904117], [0.004858, 0.0, -23.230364], [10.323058, 0.0, -12.897792], [7.739449, 0.0, -12.898331], [7.738369, 0.0, -7.733124], [12.903576, 0.0, -7.732044], [12.904117, 0.0, -10.315653], [23.230364, 0.0, 0.004858], [12.897792, 0.0, 10.323058], [12.898331, 0.0, 7.739449], [7.733124, 0.0, 7.738369], [7.732044, 0.0, 12.903576], [10.315653, 0.0, 12.904117], [-0.004858, 0.0, 23.230364], [-2.027096, 0.028148, 21.243476], [-1.850123, 0.0, 21.054519], [-1.849963, 0.0, 20.282452], [-1.689115, 0.0, 20.282486], [-1.699331, 0.0, 21.060583], [-1.584715, 0.0, 21.002298], [-1.588666, 0.0, 20.664519], [-1.425808, 0.0, 20.664553], [-1.425879, 0.0, 21.002332], [-1.325361, 0.0, 21.060659], [-1.325196, 0.0, 20.270497], [-1.162339, 0.0, 20.270531], [-1.162507, 0.0, 21.080799], [-1.293224, 0.0, 21.211462], [-1.494261, 0.0, 21.11089], [-1.715448, 0.0, 21.211373], [-1.850125, 0.0, 21.05854], [-1.715448, 0.0, 21.211373], [-1.496271, 0.0, 21.1129], [-1.293222, 0.0, 21.209451], [-0.901159, 0.0, 21.211544], [-1.03383, 0.0, 21.080827], [-1.033689, 0.0, 20.403258], [-0.900962, 0.0, 20.270588], [-0.476727, 0.0, 20.270676], [-0.346067, 0.0, 20.403401], [-0.346208, 0.0, 21.08097], [-0.476924, 0.0, 21.211632], [-0.901159, 0.0, 21.211544], [-0.850862, 0.0, 21.06076], [-0.870837, 0.0, 20.437473], [-0.506922, 0.0, 20.44157], [-0.509061, 0.0, 21.06083], [-0.852872, 0.0, 21.064781], [-0.901159, 0.0, 21.211544], [-0.476924, 0.0, 21.211632], [-0.205494, 0.0, 21.211689], [-0.21535, 0.0, 20.27073], [0.243064, 0.0, 20.270825], [0.375735, 0.0, 20.403552], [0.375677, 0.0, 20.687045], [0.240939, 0.0, 20.817705], [0.232895, 0.0, 20.827756], [0.496204, 0.0, 21.207814], [0.496202, 0.0, 21.211836], [0.307206, 0.0, 21.211795], [0.043899, 0.0, 20.829729], [-0.05462, 0.0, 20.829709], [-0.054535, 0.0, 20.427591], [0.198799, 0.0, 20.427643], [0.200759, 0.0, 20.666903], [-0.054586, 0.0, 20.666851], [-0.0547, 0.0, 21.211721], [-0.205494, 0.0, 21.211689], [1.288374, 0.0, 21.212], [1.288407, 0.0, 21.061206], [0.761632, 0.0, 21.059085], [0.761797, 0.0, 20.270933], [0.598939, 0.0, 20.270901], [0.598742, 0.0, 21.211856], [1.973986, 0.0, 21.212143], [2.094649, 0.0, 21.081481], [2.104843, 0.0, 20.403914], [1.974183, 0.0, 20.271189], [1.417249, 0.0, 20.271072], [1.417052, 0.0, 21.212029], [1.581953, 0.0, 21.061268], [1.578064, 0.0, 20.423909], [1.921875, 0.0, 20.423982], [1.917721, 0.0, 21.057318], [1.575921, 0.0, 21.065288], [1.413031, 0.0, 21.212027]]}]},
			"R_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_A_CTLShape", "degree": 3, "form": 2, "points": [[-60.694294, 101.361497, -8.602376], [-60.79848, 101.43377, -8.612789], [-60.851912, 101.525259, -8.542352], [-60.82329, 101.58237, -8.432326], [-60.729381, 101.571649, -8.347163], [-60.625196, 101.499375, -8.336751], [-60.571764, 101.407887, -8.407187], [-60.600385, 101.350775, -8.517213]]}]},
			"L_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_A_CTLShape", "degree": 3, "form": 2, "points": [[61.410455, 100.96827, -12.853165], [61.504836, 101.042558, -12.895119], [61.595029, 101.113252, -12.839854], [61.628199, 101.138941, -12.719744], [61.584917, 101.104576, -12.605148], [61.490536, 101.030288, -12.563195], [61.400344, 100.959594, -12.61846], [61.367173, 100.933905, -12.738569]]}]},
			"L_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_A_CTLShape", "degree": 3, "form": 2, "points": [[61.041234, 101.118892, -9.693871], [61.138707, 101.192599, -9.729266], [61.210959, 101.28002, -9.671615], [61.215666, 101.329945, -9.554688], [61.15007, 101.313129, -9.44698], [61.052597, 101.239422, -9.411586], [60.980345, 101.152001, -9.469237], [60.975638, 101.102076, -9.586164]]}]},
			"L_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_D_CTLShape", "degree": 3, "form": 2, "points": [[66.787584, 92.426302, -14.645442], [66.895311, 92.460255, -14.703996], [67.017796, 92.466947, -14.670241], [67.083287, 92.442456, -14.563951], [67.053423, 92.40113, -14.447389], [66.945696, 92.367176, -14.388835], [66.823211, 92.360485, -14.42259], [66.75772, 92.384975, -14.528879]]}]},
			"R_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_C_CTLShape", "degree": 3, "form": 2, "points": [[-65.96709, 94.662741, -13.873973], [-66.069677, 94.717927, -13.925129], [-66.186561, 94.746414, -13.88374], [-66.249273, 94.731515, -13.774051], [-66.221078, 94.681958, -13.660316], [-66.118491, 94.626772, -13.60916], [-66.001606, 94.598285, -13.650549], [-65.938894, 94.613184, -13.760238]]}]},
			"L_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[64.88486, 96.570868, -13.061545], [64.895599, 96.573711, -13.050958], [64.887954, 96.565031, -13.040873], [64.877215, 96.562188, -13.05146], [64.88486, 96.570868, -13.061545], [64.891962, 96.55923, -13.054502], [64.887954, 96.565031, -13.040873], [64.880852, 96.576669, -13.047915], [64.895599, 96.573711, -13.050958], [64.891962, 96.55923, -13.054502], [64.877215, 96.562188, -13.05146], [64.880852, 96.576669, -13.047915], [64.88486, 96.570868, -13.061545], [64.891962, 96.55923, -13.054502], [64.362319, 97.390571, -12.740519]]}, {"shapeName": "L_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.227916, 97.936998, -12.727175], [65.223908, 97.9428, -12.713545], [65.23101, 97.931162, -12.706503], [65.235019, 97.92536, -12.720132], [65.227916, 97.936998, -12.727175], [65.238654, 97.939841, -12.716588], [65.23101, 97.931162, -12.706503], [65.220271, 97.928319, -12.71709], [65.223908, 97.9428, -12.713545], [65.238654, 97.939841, -12.716588], [65.235019, 97.92536, -12.720132], [65.220271, 97.928319, -12.71709], [65.227916, 97.936998, -12.727175], [65.238654, 97.939841, -12.716588], [64.362319, 97.390571, -12.740519]]}, {"shapeName": "L_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[64.51744, 97.121025, -11.765171], [64.502693, 97.123984, -11.762129], [64.499056, 97.109503, -11.765673], [64.513803, 97.106544, -11.768715], [64.51744, 97.121025, -11.765171], [64.509795, 97.112346, -11.755087], [64.499056, 97.109503, -11.765673], [64.506701, 97.118182, -11.775758], [64.502693, 97.123984, -11.762129], [64.509795, 97.112346, -11.755087], [64.513803, 97.106544, -11.768715], [64.506701, 97.118182, -11.775758], [64.51744, 97.121025, -11.765171], [64.509795, 97.112346, -11.755087], [64.362319, 97.390571, -12.740519]]}]},
			"visibility_CTL": {"color": [0.434363, 0.248556, 1.0], "shapes": [{"shapeName": "visibility_CTLShape", "degree": 3, "form": 2, "points": [[85.127421, 200.0, 0.0], [42.516602, 234.165831, 0.0], [-0.094217, 200.0, 0.0], [0.017687, 200.0, 0.0], [-0.094217, 200.0, 0.0], [42.516602, 165.834169, 0.0], [85.127421, 200.0, 0.0], [85.127421, 200.0, 0.0]]}, {"shapeName": "visibility_CTLShape1", "degree": 3, "form": 2, "points": [[60.351126, 217.834524, 0.0], [42.516602, 225.221784, 0.0], [24.682078, 217.834524, 0.0], [17.294818, 200.0, 0.0], [24.682078, 182.165476, 0.0], [42.516602, 174.778216, 0.0], [60.351126, 182.165476, 0.0], [67.738385, 200.0, 0.0]]}]},
			"R_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.056402, 91.450075, -14.86417], [-67.068673, 91.448913, -14.855028], [-67.059691, 91.443999, -14.843597], [-67.04742, 91.445161, -14.852739], [-67.056402, 91.450075, -14.86417], [-67.059504, 91.436791, -14.857143], [-67.059691, 91.443999, -14.843597], [-67.056588, 91.457283, -14.850624], [-67.068673, 91.448913, -14.855028], [-67.059504, 91.436791, -14.857143], [-67.04742, 91.445161, -14.852739], [-67.056588, 91.457283, -14.850624], [-67.056402, 91.450075, -14.86417], [-67.059504, 91.436791, -14.857143], [-66.9205, 92.4137, -14.5464]]}, {"shapeName": "R_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.921311, 92.593727, -14.664676], [-67.921497, 92.600935, -14.651131], [-67.9246, 92.587651, -14.644103], [-67.924413, 92.580442, -14.657649], [-67.921311, 92.593727, -14.664676], [-67.93358, 92.592565, -14.655534], [-67.9246, 92.587651, -14.644103], [-67.912329, 92.588813, -14.653245], [-67.921497, 92.600935, -14.651131], [-67.93358, 92.592565, -14.655534], [-67.924413, 92.580442, -14.657649], [-67.912329, 92.588813, -14.653245], [-67.921311, 92.593727, -14.664676], [-67.93358, 92.592565, -14.655534], [-66.9205, 92.4137, -14.5464]]}, {"shapeName": "R_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-67.086265, 92.128975, -13.577136], [-67.074181, 92.137346, -13.572732], [-67.065013, 92.125223, -13.574846], [-67.077097, 92.116853, -13.57925], [-67.086265, 92.128975, -13.577136], [-67.077283, 92.124062, -13.565705], [-67.065013, 92.125223, -13.574846], [-67.073994, 92.130137, -13.586277], [-67.074181, 92.137346, -13.572732], [-67.077283, 92.124062, -13.565705], [-67.077097, 92.116853, -13.57925], [-67.073994, 92.130137, -13.586277], [-67.086265, 92.128975, -13.577136], [-67.077283, 92.124062, -13.565705], [-66.9205, 92.4137, -14.5464]]}]},
			"R_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-61.755306, 100.483152, -9.294977], [-61.760329, 100.492117, -9.283581], [-61.749685, 100.486208, -9.27424], [-61.744661, 100.477243, -9.285636], [-61.755306, 100.483152, -9.294977], [-61.759457, 100.476929, -9.281579], [-61.749685, 100.486208, -9.27424], [-61.745533, 100.492432, -9.287638], [-61.760329, 100.492117, -9.283581], [-61.759457, 100.476929, -9.281579], [-61.744661, 100.477243, -9.285636], [-61.745533, 100.492432, -9.287638], [-61.755306, 100.483152, -9.294977], [-61.759457, 100.476929, -9.281579], [-61.0957, 101.216, -9.57043]]}, {"shapeName": "R_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-61.837579, 101.916104, -9.483882], [-61.827806, 101.925384, -9.476543], [-61.831958, 101.91916, -9.463144], [-61.84173, 101.90988, -9.470483], [-61.837579, 101.916104, -9.483882], [-61.842602, 101.925068, -9.472486], [-61.831958, 101.91916, -9.463144], [-61.826934, 101.910194, -9.47454], [-61.827806, 101.925384, -9.476543], [-61.842602, 101.925068, -9.472486], [-61.84173, 101.90988, -9.470483], [-61.826934, 101.910194, -9.47454], [-61.837579, 101.916104, -9.483882], [-61.842602, 101.925068, -9.472486], [-61.0957, 101.216, -9.57043]]}, {"shapeName": "R_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-60.838392, 101.367611, -8.591233], [-60.823595, 101.367926, -8.59529], [-60.822723, 101.352737, -8.593288], [-60.83752, 101.352422, -8.589231], [-60.838392, 101.367611, -8.591233], [-60.827747, 101.361702, -8.581893], [-60.822723, 101.352737, -8.593288], [-60.833368, 101.358646, -8.602629], [-60.823595, 101.367926, -8.59529], [-60.827747, 101.361702, -8.581893], [-60.83752, 101.352422, -8.589231], [-60.833368, 101.358646, -8.602629], [-60.838392, 101.367611, -8.591233], [-60.827747, 101.361702, -8.581893], [-61.0957, 101.216, -9.57043]]}]},
			"L_hand_CTL": {"color": 1, "shapes": [{"shapeName": "L_hand_CTLShape", "degree": 1, "form": 0, "points": [[78.609726, 108.88312, 0.0], [78.025086, 108.98707, 0.0], [77.421861, 109.0108, 0.0], [76.850136, 108.99757, 0.0], [76.281351, 109.009855, 0.0], [75.899781, 109.03873, 0.0], [75.601371, 109.23424, 0.0], [75.352521, 109.68931, 0.0], [75.085821, 110.280565, 0.0], [74.872776, 110.940385, 0.0], [74.672226, 111.87562, 0.0], [74.572581, 112.82335, 0.0], [74.528061, 113.56108, 0.0], [74.514726, 114.141205, 0.0], [74.450991, 114.508705, 0.0], [74.383581, 114.95884, 0.0], [74.249286, 115.457485, 0.0], [74.164971, 115.90321, 0.0], [74.075091, 116.264305, 0.0], [73.939746, 116.68945, 0.0], [73.795056, 117.238495, 0.0], [73.792326, 117.663325, 0.0], [73.965261, 117.99943, 0.0], [74.171166, 118.06516, 0.0], [74.443326, 117.94063, 0.0], [74.546226, 117.61744, 0.0], [74.668551, 117.20059, 0.0], [74.830146, 116.7913, 0.0], [74.992896, 116.36458, 0.0], [75.162366, 115.847035, 0.0], [75.357876, 115.426825, 0.0], [75.531546, 115.250215, 0.0], [75.612186, 115.236355, 0.0], [75.746271, 115.497595, 0.0], [75.760866, 115.874545, 0.0], [75.663321, 116.309665, 0.0], [75.601371, 116.59999, 0.0], [75.556746, 117.03973, 0.0], [75.524196, 117.43726, 0.0], [75.455631, 117.85453, 0.0], [75.410061, 118.2088, 0.0], [75.365016, 118.51015, 0.0], [75.277131, 118.951885, 0.0], [75.203211, 119.30185, 0.0], [75.171816, 119.641105, 0.0], [75.274611, 119.954215, 0.0], [75.475581, 120.157075, 0.0], [75.769266, 120.167575, 0.0], [76.020216, 120.01543, 0.0], [76.147371, 119.679535, 0.0], [76.227591, 119.283685, 0.0], [76.305816, 118.93288, 0.0], [76.403151, 118.51981, 0.0], [76.491036, 118.136665, 0.0], [76.556556, 117.771055, 0.0], [76.606746, 117.376045, 0.0], [76.711431, 116.907535, 0.0], [76.788816, 116.588755, 0.0], [76.852131, 116.21422, 0.0], [77.045436, 115.922215, 0.0], [77.175846, 116.120035, 0.0], [77.253336, 116.63989, 0.0], [77.270556, 117.030805, 0.0], [77.258271, 117.537115, 0.0], [77.279901, 117.987775, 0.0], [77.304786, 118.383625, 0.0], [77.307726, 118.84048, 0.0], [77.285046, 119.273815, 0.0], [77.286201, 119.889115, 0.0], [77.302896, 120.337465, 0.0], [77.363691, 120.71935, 0.0], [77.587971, 120.88147, 0.0], [77.883021, 120.968305, 0.0], [78.144261, 120.880105, 0.0], [78.279711, 120.605425, 0.0], [78.314991, 120.152875, 0.0], [78.347751, 119.70442, 0.0], [78.365811, 119.332195, 0.0], [78.333366, 118.845415, 0.0], [78.328431, 118.39864, 0.0], [78.390276, 117.91963, 0.0], [78.429546, 117.68464, 0.0], [78.419046, 117.36733, 0.0], [78.435111, 117.01222, 0.0], [78.463671, 116.58214, 0.0], [78.488976, 116.068375, 0.0], [78.551346, 115.95046, 0.0], [78.703596, 116.09263, 0.0], [78.776046, 116.44942, 0.0], [78.878001, 116.9194, 0.0], [79.006521, 117.4738, 0.0], [79.092936, 117.95617, 0.0], [79.182501, 118.383205, 0.0], [79.317426, 118.781365, 0.0], [79.462746, 119.25418, 0.0], [79.577196, 119.74474, 0.0], [79.697421, 120.1219, 0.0], [79.834761, 120.419155, 0.0], [80.058201, 120.645745, 0.0], [80.228406, 120.60889, 0.0], [80.528706, 120.41401, 0.0], [80.637276, 119.96629, 0.0], [80.569341, 119.517625, 0.0], [80.514846, 119.20987, 0.0], [80.466966, 118.82641, 0.0], [80.393991, 118.41922, 0.0], [80.250036, 117.973915, 0.0], [80.187141, 117.69052, 0.0], [80.157216, 117.183265, 0.0], [80.139471, 116.8543, 0.0], [80.067861, 116.43619, 0.0], [80.005386, 116.058715, 0.0], [79.975461, 115.64071, 0.0], [79.923801, 115.009345, 0.0], [79.980186, 114.10624, 0.0], [80.089386, 113.64235, 0.0], [80.263581, 113.34814, 0.0], [80.485761, 113.02957, 0.0], [80.668251, 113.417965, 0.0], [80.960151, 113.851825, 0.0], [81.112296, 114.16231, 0.0], [81.182646, 114.5149, 0.0], [81.355476, 114.87211, 0.0], [81.637926, 115.233625, 0.0], [82.014561, 115.504105, 0.0], [82.280946, 115.584955, 0.0], [82.538616, 115.4221, 0.0], [82.584291, 115.16548, 0.0], [82.518141, 114.73078, 0.0], [82.378071, 114.45106, 0.0], [82.358646, 114.19759, 0.0], [82.349196, 113.710285, 0.0], [82.195791, 113.41198, 0.0], [82.008366, 113.17153, 0.0], [81.955971, 112.940845, 0.0], [81.915756, 112.644325, 0.0], [81.732951, 112.173505, 0.0], [81.499116, 111.158785, 0.0], [81.213831, 110.65573, 0.0], [80.843076, 110.08663, 0.0], [80.476836, 109.59103, 0.0], [80.188506, 109.22542, 0.0], [79.673271, 108.94108, 0.0], [79.201611, 108.850465, 0.0], [78.618021, 108.882385, 0.0]]}]},
			"R_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_D_CTLShape", "degree": 3, "form": 2, "points": [[-68.263169, 89.858161, -6.413377], [-68.386585, 89.875818, -6.438742], [-68.489957, 89.901471, -6.369153], [-68.512733, 89.920093, -6.245375], [-68.441569, 89.920776, -6.139915], [-68.318154, 89.903119, -6.11455], [-68.214781, 89.877466, -6.184138], [-68.192006, 89.858844, -6.307917]]}]},
			"R_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-64.884841, 96.570897, -13.061526], [-64.89558, 96.57374, -13.050939], [-64.887935, 96.56506, -13.040854], [-64.877196, 96.562217, -13.051441], [-64.884841, 96.570897, -13.061526], [-64.891943, 96.559259, -13.054483], [-64.887935, 96.56506, -13.040854], [-64.880833, 96.576698, -13.047896], [-64.89558, 96.57374, -13.050939], [-64.891943, 96.559259, -13.054483], [-64.877196, 96.562217, -13.051441], [-64.880833, 96.576698, -13.047896], [-64.884841, 96.570897, -13.061526], [-64.891943, 96.559259, -13.054483], [-64.3623, 97.3906, -12.7405]]}, {"shapeName": "R_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.227897, 97.937027, -12.727156], [-65.223889, 97.942829, -12.713526], [-65.230991, 97.931191, -12.706484], [-65.235, 97.925389, -12.720113], [-65.227897, 97.937027, -12.727156], [-65.238635, 97.93987, -12.716569], [-65.230991, 97.931191, -12.706484], [-65.220252, 97.928348, -12.717071], [-65.223889, 97.942829, -12.713526], [-65.238635, 97.93987, -12.716569], [-65.235, 97.925389, -12.720113], [-65.220252, 97.928348, -12.717071], [-65.227897, 97.937027, -12.727156], [-65.238635, 97.93987, -12.716569], [-64.3623, 97.3906, -12.7405]]}, {"shapeName": "R_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-64.517421, 97.121054, -11.765152], [-64.502674, 97.124013, -11.76211], [-64.499037, 97.109532, -11.765654], [-64.513784, 97.106573, -11.768696], [-64.517421, 97.121054, -11.765152], [-64.509776, 97.112375, -11.755068], [-64.499037, 97.109532, -11.765654], [-64.506682, 97.118211, -11.775739], [-64.502674, 97.124013, -11.76211], [-64.509776, 97.112375, -11.755068], [-64.513784, 97.106573, -11.768696], [-64.506682, 97.118211, -11.775739], [-64.517421, 97.121054, -11.765152], [-64.509776, 97.112375, -11.755068], [-64.3623, 97.3906, -12.7405]]}]},
			"L_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.056405, 91.450091, -14.864185], [67.068676, 91.448929, -14.855043], [67.059694, 91.444015, -14.843612], [67.047423, 91.445177, -14.852754], [67.056405, 91.450091, -14.864185], [67.059507, 91.436807, -14.857158], [67.059694, 91.444015, -14.843612], [67.056591, 91.457299, -14.850639], [67.068676, 91.448929, -14.855043], [67.059507, 91.436807, -14.857158], [67.047423, 91.445177, -14.852754], [67.056591, 91.457299, -14.850639], [67.056405, 91.450091, -14.864185], [67.059507, 91.436807, -14.857158], [66.920503, 92.413716, -14.546415]]}, {"shapeName": "L_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.921314, 92.593743, -14.664691], [67.9215, 92.600951, -14.651146], [67.924603, 92.587667, -14.644118], [67.924416, 92.580458, -14.657664], [67.921314, 92.593743, -14.664691], [67.933583, 92.592581, -14.655549], [67.924603, 92.587667, -14.644118], [67.912332, 92.588829, -14.65326], [67.9215, 92.600951, -14.651146], [67.933583, 92.592581, -14.655549], [67.924416, 92.580458, -14.657664], [67.912332, 92.588829, -14.65326], [67.921314, 92.593743, -14.664691], [67.933583, 92.592581, -14.655549], [66.920503, 92.413716, -14.546415]]}, {"shapeName": "L_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[67.086268, 92.128991, -13.577151], [67.074184, 92.137362, -13.572747], [67.065016, 92.125239, -13.574861], [67.0771, 92.116869, -13.579265], [67.086268, 92.128991, -13.577151], [67.077286, 92.124078, -13.56572], [67.065016, 92.125239, -13.574861], [67.073997, 92.130153, -13.586292], [67.074184, 92.137362, -13.572747], [67.077286, 92.124078, -13.56572], [67.0771, 92.116869, -13.579265], [67.073997, 92.130153, -13.586292], [67.086268, 92.128991, -13.577151], [67.077286, 92.124078, -13.56572], [66.920503, 92.413716, -14.546415]]}]},
			"R_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.676382, 89.280791, -10.816333], [-68.687291, 89.280721, -10.805541], [-68.67651, 89.279941, -10.794648], [-68.665601, 89.28001, -10.805441], [-68.676382, 89.280791, -10.816333], [-68.6768, 89.26953, -10.805918], [-68.67651, 89.279941, -10.794648], [-68.676093, 89.291203, -10.805064], [-68.687291, 89.280721, -10.805541], [-68.6768, 89.26953, -10.805918], [-68.665601, 89.28001, -10.805441], [-68.676093, 89.291203, -10.805064], [-68.676382, 89.280791, -10.816333], [-68.6768, 89.26953, -10.805918], [-68.6431, 90.3027, -10.7652]]}, {"shapeName": "R_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-69.666146, 90.336682, -10.78075], [-69.665857, 90.347094, -10.769481], [-69.666274, 90.335832, -10.759065], [-69.666564, 90.32542, -10.770335], [-69.666146, 90.336682, -10.78075], [-69.677054, 90.336613, -10.769958], [-69.666274, 90.335832, -10.759065], [-69.655365, 90.335901, -10.769858], [-69.665857, 90.347094, -10.769481], [-69.677054, 90.336613, -10.769958], [-69.666564, 90.32542, -10.770335], [-69.655365, 90.335901, -10.769858], [-69.666146, 90.336682, -10.78075], [-69.677054, 90.336613, -10.769958], [-68.6431, 90.3027, -10.7652]]}, {"shapeName": "R_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-68.659967, 90.26294, -9.742383], [-68.648769, 90.273421, -9.741906], [-68.638277, 90.262229, -9.742283], [-68.649476, 90.251748, -9.74276], [-68.659967, 90.26294, -9.742383], [-68.649186, 90.262159, -9.731492], [-68.638277, 90.262229, -9.742283], [-68.649058, 90.26301, -9.753176], [-68.648769, 90.273421, -9.741906], [-68.649186, 90.262159, -9.731492], [-68.649476, 90.251748, -9.74276], [-68.649058, 90.26301, -9.753176], [-68.659967, 90.26294, -9.742383], [-68.649186, 90.262159, -9.731492], [-68.6431, 90.3027, -10.7652]]}]},
			"L_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_D_CTLShape", "degree": 3, "form": 2, "points": [[68.524947, 90.303452, -10.882141], [68.642138, 90.309213, -10.931331], [68.759902, 90.311158, -10.883222], [68.809254, 90.308148, -10.765997], [68.761285, 90.301946, -10.648323], [68.644094, 90.296185, -10.599134], [68.52633, 90.294239, -10.647242], [68.476978, 90.29725, -10.764468]]}]},
			"R_hand_CTL": {"color": 1, "shapes": [{"shapeName": "R_hand_CTLShape", "degree": 1, "form": 0, "points": [[-78.609726, 108.88312, -0.0], [-78.025086, 108.98707, -0.0], [-77.421861, 109.0108, -0.0], [-76.850136, 108.99757, -0.0], [-76.281351, 109.009855, -0.0], [-75.899781, 109.03873, -0.0], [-75.601371, 109.23424, -0.0], [-75.352521, 109.68931, -0.0], [-75.085821, 110.280565, -0.0], [-74.872776, 110.940385, -0.0], [-74.672226, 111.87562, -0.0], [-74.572581, 112.82335, -0.0], [-74.528061, 113.56108, -0.0], [-74.514726, 114.141205, -0.0], [-74.450991, 114.508705, -0.0], [-74.383581, 114.95884, -0.0], [-74.249286, 115.457485, -0.0], [-74.164971, 115.90321, -0.0], [-74.075091, 116.264305, -0.0], [-73.939746, 116.68945, -0.0], [-73.795056, 117.238495, -0.0], [-73.792326, 117.663325, -0.0], [-73.965261, 117.99943, -0.0], [-74.171166, 118.06516, -0.0], [-74.443326, 117.94063, -0.0], [-74.546226, 117.61744, -0.0], [-74.668551, 117.20059, -0.0], [-74.830146, 116.7913, -0.0], [-74.992896, 116.36458, -0.0], [-75.162366, 115.847035, -0.0], [-75.357876, 115.426825, -0.0], [-75.531546, 115.250215, -0.0], [-75.612186, 115.236355, -0.0], [-75.746271, 115.497595, -0.0], [-75.760866, 115.874545, -0.0], [-75.663321, 116.309665, -0.0], [-75.601371, 116.59999, -0.0], [-75.556746, 117.03973, -0.0], [-75.524196, 117.43726, -0.0], [-75.455631, 117.85453, -0.0], [-75.410061, 118.2088, -0.0], [-75.365016, 118.51015, -0.0], [-75.277131, 118.951885, -0.0], [-75.203211, 119.30185, -0.0], [-75.171816, 119.641105, -0.0], [-75.274611, 119.954215, -0.0], [-75.475581, 120.157075, -0.0], [-75.769266, 120.167575, -0.0], [-76.020216, 120.01543, -0.0], [-76.147371, 119.679535, -0.0], [-76.227591, 119.283685, -0.0], [-76.305816, 118.93288, -0.0], [-76.403151, 118.51981, -0.0], [-76.491036, 118.136665, -0.0], [-76.556556, 117.771055, -0.0], [-76.606746, 117.376045, -0.0], [-76.711431, 116.907535, -0.0], [-76.788816, 116.588755, -0.0], [-76.852131, 116.21422, -0.0], [-77.045436, 115.922215, -0.0], [-77.175846, 116.120035, -0.0], [-77.253336, 116.63989, -0.0], [-77.270556, 117.030805, -0.0], [-77.258271, 117.537115, -0.0], [-77.279901, 117.987775, -0.0], [-77.304786, 118.383625, -0.0], [-77.307726, 118.84048, -0.0], [-77.285046, 119.273815, -0.0], [-77.286201, 119.889115, -0.0], [-77.302896, 120.337465, -0.0], [-77.363691, 120.71935, -0.0], [-77.587971, 120.88147, -0.0], [-77.883021, 120.968305, -0.0], [-78.144261, 120.880105, -0.0], [-78.279711, 120.605425, -0.0], [-78.314991, 120.152875, -0.0], [-78.347751, 119.70442, -0.0], [-78.365811, 119.332195, -0.0], [-78.333366, 118.845415, -0.0], [-78.328431, 118.39864, -0.0], [-78.390276, 117.91963, -0.0], [-78.429546, 117.68464, -0.0], [-78.419046, 117.36733, -0.0], [-78.435111, 117.01222, -0.0], [-78.463671, 116.58214, -0.0], [-78.488976, 116.068375, -0.0], [-78.551346, 115.95046, -0.0], [-78.703596, 116.09263, -0.0], [-78.776046, 116.44942, -0.0], [-78.878001, 116.9194, -0.0], [-79.006521, 117.4738, -0.0], [-79.092936, 117.95617, -0.0], [-79.182501, 118.383205, -0.0], [-79.317426, 118.781365, -0.0], [-79.462746, 119.25418, -0.0], [-79.577196, 119.74474, -0.0], [-79.697421, 120.1219, -0.0], [-79.834761, 120.419155, -0.0], [-80.058201, 120.645745, -0.0], [-80.228406, 120.60889, -0.0], [-80.528706, 120.41401, -0.0], [-80.637276, 119.96629, -0.0], [-80.569341, 119.517625, -0.0], [-80.514846, 119.20987, -0.0], [-80.466966, 118.82641, -0.0], [-80.393991, 118.41922, -0.0], [-80.250036, 117.973915, -0.0], [-80.187141, 117.69052, -0.0], [-80.157216, 117.183265, -0.0], [-80.139471, 116.8543, -0.0], [-80.067861, 116.43619, -0.0], [-80.005386, 116.058715, -0.0], [-79.975461, 115.64071, -0.0], [-79.923801, 115.009345, -0.0], [-79.980186, 114.10624, -0.0], [-80.089386, 113.64235, -0.0], [-80.263581, 113.34814, -0.0], [-80.485761, 113.02957, -0.0], [-80.668251, 113.417965, -0.0], [-80.960151, 113.851825, -0.0], [-81.112296, 114.16231, -0.0], [-81.182646, 114.5149, -0.0], [-81.355476, 114.87211, -0.0], [-81.637926, 115.233625, -0.0], [-82.014561, 115.504105, -0.0], [-82.280946, 115.584955, -0.0], [-82.538616, 115.4221, -0.0], [-82.584291, 115.16548, -0.0], [-82.518141, 114.73078, -0.0], [-82.378071, 114.45106, -0.0], [-82.358646, 114.19759, -0.0], [-82.349196, 113.710285, -0.0], [-82.195791, 113.41198, -0.0], [-82.008366, 113.17153, -0.0], [-81.955971, 112.940845, -0.0], [-81.915756, 112.644325, -0.0], [-81.732951, 112.173505, -0.0], [-81.499116, 111.158785, -0.0], [-81.213831, 110.65573, -0.0], [-80.843076, 110.08663, -0.0], [-80.476836, 109.59103, -0.0], [-80.188506, 109.22542, -0.0], [-79.673271, 108.94108, -0.0], [-79.201611, 108.850465, -0.0], [-78.618021, 108.882385, -0.0]]}]},
			"L_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[57.807642, 100.742528, -7.270903], [57.794152, 100.748227, -7.266318], [57.786846, 100.737247, -7.274163], [57.800336, 100.731548, -7.278749], [57.807642, 100.742528, -7.270903], [57.797504, 100.733468, -7.26379], [57.786846, 100.737247, -7.274163], [57.796985, 100.746308, -7.281277], [57.794152, 100.748227, -7.266318], [57.797504, 100.733468, -7.26379], [57.800336, 100.731548, -7.278749], [57.796985, 100.746308, -7.281277], [57.807642, 100.742528, -7.270903], [57.797504, 100.733468, -7.26379], [57.772776, 101.345592, -8.097412]]}, {"shapeName": "L_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[57.491471, 102.13499, -7.509417], [57.480814, 102.13877, -7.519791], [57.470675, 102.12971, -7.512677], [57.481333, 102.125929, -7.502303], [57.491471, 102.13499, -7.509417], [57.477982, 102.140689, -7.504832], [57.470675, 102.12971, -7.512677], [57.484165, 102.12401, -7.517262], [57.480814, 102.13877, -7.519791], [57.477982, 102.140689, -7.504832], [57.481333, 102.125929, -7.502303], [57.484165, 102.12401, -7.517262], [57.491471, 102.13499, -7.509417], [57.477982, 102.140689, -7.504832], [57.772776, 101.345592, -8.097412]]}, {"shapeName": "L_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[56.788759, 101.104861, -8.244991], [56.791591, 101.102942, -8.25995], [56.794943, 101.088182, -8.257422], [56.79211, 101.090101, -8.242463], [56.788759, 101.104861, -8.244991], [56.781454, 101.093881, -8.252836], [56.794943, 101.088182, -8.257422], [56.802249, 101.099161, -8.249576], [56.791591, 101.102942, -8.25995], [56.781454, 101.093881, -8.252836], [56.79211, 101.090101, -8.242463], [56.802249, 101.099161, -8.249576], [56.788759, 101.104861, -8.244991], [56.781454, 101.093881, -8.252836], [57.772776, 101.345592, -8.097412]]}]},
			"L_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.349614, 92.441652, -2.936398], [66.353091, 92.44772, -2.922739], [66.338642, 92.445494, -2.918072], [66.335165, 92.439426, -2.931732], [66.349614, 92.441652, -2.936398], [66.346833, 92.433733, -2.923552], [66.338642, 92.445494, -2.918072], [66.341422, 92.453415, -2.930919], [66.353091, 92.44772, -2.922739], [66.346833, 92.433733, -2.923552], [66.335165, 92.439426, -2.931732], [66.341422, 92.453415, -2.930919], [66.349614, 92.441652, -2.936398], [66.346833, 92.433733, -2.923552], [66.08888, 93.372015, -3.274723]]}, {"shapeName": "L_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[66.939902, 93.761304, -2.859712], [66.931711, 93.773067, -2.854232], [66.928931, 93.765147, -2.841386], [66.937122, 93.753384, -2.846865], [66.939902, 93.761304, -2.859712], [66.943379, 93.767372, -2.846053], [66.928931, 93.765147, -2.841386], [66.925454, 93.759079, -2.855045], [66.931711, 93.773067, -2.854232], [66.943379, 93.767372, -2.846053], [66.937122, 93.753384, -2.846865], [66.925454, 93.759079, -2.855045], [66.939902, 93.761304, -2.859712], [66.943379, 93.767372, -2.846053], [66.08888, 93.372015, -3.274723]]}, {"shapeName": "L_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.580331, 93.557415, -2.405801], [65.568663, 93.563109, -2.41398], [65.562406, 93.549121, -2.414793], [65.574074, 93.543426, -2.406613], [65.580331, 93.557415, -2.405801], [65.565883, 93.555189, -2.401135], [65.562406, 93.549121, -2.414793], [65.576854, 93.551346, -2.41946], [65.568663, 93.563109, -2.41398], [65.565883, 93.555189, -2.401135], [65.574074, 93.543426, -2.406613], [65.576854, 93.551346, -2.41946], [65.580331, 93.557415, -2.405801], [65.565883, 93.555189, -2.401135], [66.08888, 93.372015, -3.274723]]}]},
			"L_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_A_CTLShape", "degree": 3, "form": 2, "points": [[61.289857, 100.887727, -11.407642], [61.381403, 100.963509, -11.453062], [61.460932, 101.048877, -11.402329], [61.481857, 101.093824, -11.285161], [61.431921, 101.072021, -11.170193], [61.340375, 100.99624, -11.124773], [61.260846, 100.910871, -11.175506], [61.23992, 100.865924, -11.292675]]}]},
			"R_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.349634, 92.441637, -2.936395], [-66.353111, 92.447705, -2.922736], [-66.338662, 92.445479, -2.918069], [-66.335185, 92.439411, -2.931729], [-66.349634, 92.441637, -2.936395], [-66.346853, 92.433718, -2.923549], [-66.338662, 92.445479, -2.918069], [-66.341442, 92.4534, -2.930916], [-66.353111, 92.447705, -2.922736], [-66.346853, 92.433718, -2.923549], [-66.335185, 92.439411, -2.931729], [-66.341442, 92.4534, -2.930916], [-66.349634, 92.441637, -2.936395], [-66.346853, 92.433718, -2.923549], [-66.0889, 93.372, -3.27472]]}, {"shapeName": "R_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-66.939922, 93.761289, -2.859709], [-66.931731, 93.773052, -2.854229], [-66.928951, 93.765132, -2.841383], [-66.937142, 93.753369, -2.846862], [-66.939922, 93.761289, -2.859709], [-66.943399, 93.767357, -2.84605], [-66.928951, 93.765132, -2.841383], [-66.925474, 93.759064, -2.855042], [-66.931731, 93.773052, -2.854229], [-66.943399, 93.767357, -2.84605], [-66.937142, 93.753369, -2.846862], [-66.925474, 93.759064, -2.855042], [-66.939922, 93.761289, -2.859709], [-66.943399, 93.767357, -2.84605], [-66.0889, 93.372, -3.27472]]}, {"shapeName": "R_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-65.580351, 93.5574, -2.405798], [-65.568683, 93.563094, -2.413977], [-65.562426, 93.549106, -2.41479], [-65.574094, 93.543411, -2.40661], [-65.580351, 93.5574, -2.405798], [-65.565903, 93.555174, -2.401132], [-65.562426, 93.549106, -2.41479], [-65.576874, 93.551331, -2.419457], [-65.568683, 93.563094, -2.413977], [-65.565903, 93.555174, -2.401132], [-65.574094, 93.543411, -2.40661], [-65.576874, 93.551331, -2.419457], [-65.580351, 93.5574, -2.405798], [-65.565903, 93.555174, -2.401132], [-66.0889, 93.372, -3.27472]]}]},
			"R_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.767201, 89.821747, -2.155876], [-66.771268, 89.82421, -2.141285], [-66.756476, 89.825277, -2.137343], [-66.752409, 89.822814, -2.151933], [-66.767201, 89.821747, -2.155876], [-66.761568, 89.812829, -2.144731], [-66.756476, 89.825277, -2.137343], [-66.762108, 89.834195, -2.148488], [-66.771268, 89.82421, -2.141285], [-66.761568, 89.812829, -2.144731], [-66.752409, 89.822814, -2.151933], [-66.762108, 89.834195, -2.148488], [-66.767201, 89.821747, -2.155876], [-66.761568, 89.812829, -2.144731], [-66.7873, 90.8314, -2.32385]]}, {"shapeName": "R_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.682214, 90.895487, -1.830858], [-67.677121, 90.907936, -1.82347], [-67.671489, 90.899017, -1.812325], [-67.676581, 90.886569, -1.819713], [-67.682214, 90.895487, -1.830858], [-67.68628, 90.89795, -1.816268], [-67.671489, 90.899017, -1.812325], [-67.667422, 90.896554, -1.826915], [-67.677121, 90.907936, -1.82347], [-67.68628, 90.89795, -1.816268], [-67.676581, 90.886569, -1.819713], [-67.667422, 90.896554, -1.826915], [-67.682214, 90.895487, -1.830858], [-67.68628, 90.89795, -1.816268], [-66.7873, 90.8314, -2.32385]]}, {"shapeName": "R_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-66.290812, 90.99861, -1.444326], [-66.281653, 91.008595, -1.451529], [-66.271954, 90.997214, -1.454974], [-66.281113, 90.987228, -1.447772], [-66.290812, 90.99861, -1.444326], [-66.276021, 90.999677, -1.440385], [-66.271954, 90.997214, -1.454974], [-66.286746, 90.996147, -1.458917], [-66.281653, 91.008595, -1.451529], [-66.276021, 90.999677, -1.440385], [-66.281113, 90.987228, -1.447772], [-66.286746, 90.996147, -1.458917], [-66.290812, 90.99861, -1.444326], [-66.276021, 90.999677, -1.440385], [-66.7873, 90.8314, -2.32385]]}]},
			"L_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_C_CTLShape", "degree": 3, "form": 2, "points": [[58.381669, 95.232804, -2.244147], [58.302923, 95.296396, -2.167065], [58.317448, 95.384408, -2.076349], [58.416736, 95.445284, -2.025139], [58.542626, 95.443364, -2.043433], [58.621372, 95.379772, -2.120515], [58.606847, 95.29176, -2.211231], [58.507559, 95.230884, -2.262441]]}]},
			"L_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_C_CTLShape", "degree": 3, "form": 2, "points": [[66.051215, 93.306282, -3.422684], [66.172916, 93.342582, -3.415093], [66.24539, 93.396123, -3.325274], [66.226182, 93.435541, -3.205843], [66.126545, 93.437747, -3.126761], [66.004844, 93.401447, -3.134353], [65.932369, 93.347906, -3.224171], [65.951577, 93.308488, -3.343602]]}]},
			"L_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.676398, 89.28079, -10.816365], [68.687307, 89.28072, -10.805573], [68.676526, 89.27994, -10.79468], [68.665617, 89.280009, -10.805473], [68.676398, 89.28079, -10.816365], [68.676816, 89.269529, -10.80595], [68.676526, 89.27994, -10.79468], [68.676109, 89.291202, -10.805096], [68.687307, 89.28072, -10.805573], [68.676816, 89.269529, -10.80595], [68.665617, 89.280009, -10.805473], [68.676109, 89.291202, -10.805096], [68.676398, 89.28079, -10.816365], [68.676816, 89.269529, -10.80595], [68.643116, 90.302699, -10.765232]]}, {"shapeName": "L_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[69.666162, 90.336681, -10.780782], [69.665873, 90.347093, -10.769513], [69.66629, 90.335831, -10.759097], [69.66658, 90.325419, -10.770367], [69.666162, 90.336681, -10.780782], [69.67707, 90.336612, -10.76999], [69.66629, 90.335831, -10.759097], [69.655381, 90.3359, -10.76989], [69.665873, 90.347093, -10.769513], [69.67707, 90.336612, -10.76999], [69.66658, 90.325419, -10.770367], [69.655381, 90.3359, -10.76989], [69.666162, 90.336681, -10.780782], [69.67707, 90.336612, -10.76999], [68.643116, 90.302699, -10.765232]]}, {"shapeName": "L_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[68.659983, 90.262939, -9.742415], [68.648785, 90.27342, -9.741938], [68.638293, 90.262228, -9.742315], [68.649492, 90.251747, -9.742792], [68.659983, 90.262939, -9.742415], [68.649202, 90.262158, -9.731524], [68.638293, 90.262228, -9.742315], [68.649074, 90.263009, -9.753208], [68.648785, 90.27342, -9.741938], [68.649202, 90.262158, -9.731524], [68.649492, 90.251747, -9.742792], [68.649074, 90.263009, -9.753208], [68.659983, 90.262939, -9.742415], [68.649202, 90.262158, -9.731524], [68.643116, 90.302699, -10.765232]]}]},
			"world_B_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[-0.006477, 0.0, 30.973819], [-13.764077, 0.0, 17.197056], [-10.319265, 0.0, 17.197774], [-10.317826, 0.0, 10.310831], [-17.204769, 0.0, 10.309392], [-17.20549, 0.0, 13.754204], [-30.973819, 0.0, -0.006477], [-17.197056, 0.0, -13.764077], [-17.197774, 0.0, -10.319265], [-10.310831, 0.0, -10.317826], [-10.309392, 0.0, -17.204769], [-13.754204, 0.0, -17.20549], [0.006477, 0.0, -30.973819], [13.764077, 0.0, -17.197056], [10.319265, 0.0, -17.197774], [10.317826, 0.0, -10.310831], [17.204769, 0.0, -10.309392], [17.20549, 0.0, -13.754204], [30.973819, 0.0, 0.006477], [17.197056, 0.0, 13.764077], [17.197774, 0.0, 10.319265], [10.310831, 0.0, 10.317826], [10.309392, 0.0, 17.204769], [13.754204, 0.0, 17.20549], [-0.006477, 0.0, 30.973819], [-2.702794, 0.037531, 28.324635], [-2.466831, 0.0, 28.072692], [-2.466617, 0.0, 27.043269], [-2.252154, 0.0, 27.043315], [-2.265775, 0.0, 28.080777], [-2.112954, 0.0, 28.003064], [-2.118222, 0.0, 27.552691], [-1.901078, 0.0, 27.552737], [-1.901172, 0.0, 28.003109], [-1.767148, 0.0, 28.080879], [-1.766928, 0.0, 27.027329], [-1.549785, 0.0, 27.027375], [-1.55001, 0.0, 28.107732], [-1.724299, 0.0, 28.281949], [-1.992348, 0.0, 28.147853], [-2.287264, 0.0, 28.281831], [-2.466834, 0.0, 28.078053], [-2.287264, 0.0, 28.281831], [-1.995029, 0.0, 28.150534], [-1.724296, 0.0, 28.279268], [-1.201545, 0.0, 28.282059], [-1.378439, 0.0, 28.10777], [-1.378252, 0.0, 27.204345], [-1.201282, 0.0, 27.02745], [-0.635636, 0.0, 27.027568], [-0.461423, 0.0, 27.204535], [-0.46161, 0.0, 28.10796], [-0.635899, 0.0, 28.282177], [-1.201545, 0.0, 28.282059], [-1.134482, 0.0, 28.081013], [-1.161116, 0.0, 27.249964], [-0.675896, 0.0, 27.255427], [-0.678749, 0.0, 28.081107], [-1.137163, 0.0, 28.086375], [-1.201545, 0.0, 28.282059], [-0.635899, 0.0, 28.282177], [-0.273993, 0.0, 28.282252], [-0.287134, 0.0, 27.02764], [0.324086, 0.0, 27.027766], [0.50098, 0.0, 27.204736], [0.500902, 0.0, 27.582727], [0.321252, 0.0, 27.756941], [0.310526, 0.0, 27.770342], [0.661605, 0.0, 28.277086], [0.661602, 0.0, 28.282447], [0.409608, 0.0, 28.282394], [0.058532, 0.0, 27.772972], [-0.072826, 0.0, 27.772945], [-0.072714, 0.0, 27.236787], [0.265066, 0.0, 27.236857], [0.267679, 0.0, 27.555871], [-0.072781, 0.0, 27.555801], [-0.072934, 0.0, 28.282295], [-0.273993, 0.0, 28.282252], [1.717833, 0.0, 28.282667], [1.717875, 0.0, 28.081608], [1.015509, 0.0, 28.07878], [1.015729, 0.0, 27.027911], [0.798585, 0.0, 27.027868], [0.798322, 0.0, 28.282474], [2.631981, 0.0, 28.282858], [2.792866, 0.0, 28.108641], [2.806457, 0.0, 27.205218], [2.632244, 0.0, 27.028252], [1.889666, 0.0, 27.028096], [1.889403, 0.0, 28.282705], [2.10927, 0.0, 28.081691], [2.104086, 0.0, 27.231879], [2.5625, 0.0, 27.231975], [2.556962, 0.0, 28.076423], [2.101228, 0.0, 28.08705], [1.884041, 0.0, 28.282702]]}]},
			"L_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_B_CTLShape", "degree": 3, "form": 2, "points": [[58.029331, 98.470742, -4.303342], [58.046892, 98.542154, -4.199523], [57.971239, 98.588371, -4.10827], [57.846687, 98.582319, -4.083039], [57.746197, 98.527544, -4.138608], [57.728635, 98.456132, -4.242427], [57.804289, 98.409915, -4.33368], [57.928841, 98.415967, -4.358912]]}]},
			"L_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_B_CTLShape", "degree": 3, "form": 2, "points": [[64.245994, 97.359775, -12.855202], [64.338622, 97.435276, -12.89886], [64.445132, 97.48459, -12.849764], [64.503131, 97.478829, -12.736673], [64.478644, 97.421367, -12.625835], [64.386016, 97.345865, -12.582177], [64.279506, 97.296551, -12.631273], [64.221508, 97.302313, -12.744364]]}]},
			"R_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_B_CTLShape", "degree": 3, "form": 2, "points": [[-64.962172, 96.963793, -10.551008], [-65.0603, 97.029837, -10.597867], [-65.159464, 97.091572, -10.547453], [-65.201577, 97.112835, -10.429297], [-65.161969, 97.081171, -10.312613], [-65.063842, 97.015127, -10.265754], [-64.964677, 96.953391, -10.316168], [-64.922564, 96.932128, -10.434324]]}]},
			"L_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_A_CTLShape", "degree": 3, "form": 2, "points": [[57.918903, 101.283853, -8.147082], [57.932063, 101.386038, -8.072438], [57.851915, 101.46453, -8.012424], [57.725407, 101.47335, -8.002195], [57.626648, 101.407331, -8.047743], [57.613488, 101.305147, -8.122386], [57.693636, 101.226654, -8.1824], [57.820144, 101.217834, -8.192629]]}]},
			"R_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_B_CTLShape", "degree": 3, "form": 2, "points": [[-64.245994, 97.359775, -12.855202], [-64.338622, 97.435276, -12.89886], [-64.445132, 97.48459, -12.849764], [-64.503131, 97.478829, -12.736673], [-64.478644, 97.421367, -12.625835], [-64.386016, 97.345865, -12.582177], [-64.279506, 97.296551, -12.631273], [-64.221508, 97.302313, -12.744364]]}]},
			"R_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_A_CTLShape", "degree": 3, "form": 2, "points": [[-57.918903, 101.283853, -8.147082], [-57.932063, 101.386038, -8.072438], [-57.851915, 101.46453, -8.012424], [-57.725407, 101.47335, -8.002195], [-57.626648, 101.407331, -8.047743], [-57.613488, 101.305147, -8.122386], [-57.693636, 101.226654, -8.1824], [-57.820144, 101.217834, -8.192629]]}]},
			"L_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[61.755258, 100.483163, -9.294973], [61.760281, 100.492128, -9.283577], [61.749637, 100.486219, -9.274236], [61.744613, 100.477254, -9.285632], [61.755258, 100.483163, -9.294973], [61.759409, 100.47694, -9.281575], [61.749637, 100.486219, -9.274236], [61.745485, 100.492443, -9.287634], [61.760281, 100.492128, -9.283577], [61.759409, 100.47694, -9.281575], [61.744613, 100.477254, -9.285632], [61.745485, 100.492443, -9.287634], [61.755258, 100.483163, -9.294973], [61.759409, 100.47694, -9.281575], [61.095652, 101.216011, -9.570426]]}, {"shapeName": "L_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[61.837531, 101.916115, -9.483878], [61.827758, 101.925395, -9.476539], [61.83191, 101.919171, -9.46314], [61.841682, 101.909891, -9.470479], [61.837531, 101.916115, -9.483878], [61.842554, 101.925079, -9.472482], [61.83191, 101.919171, -9.46314], [61.826886, 101.910205, -9.474536], [61.827758, 101.925395, -9.476539], [61.842554, 101.925079, -9.472482], [61.841682, 101.909891, -9.470479], [61.826886, 101.910205, -9.474536], [61.837531, 101.916115, -9.483878], [61.842554, 101.925079, -9.472482], [61.095652, 101.216011, -9.570426]]}, {"shapeName": "L_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[60.838344, 101.367622, -8.591229], [60.823547, 101.367937, -8.595286], [60.822675, 101.352748, -8.593284], [60.837472, 101.352433, -8.589227], [60.838344, 101.367622, -8.591229], [60.827699, 101.361713, -8.581889], [60.822675, 101.352748, -8.593284], [60.83332, 101.358657, -8.602625], [60.823547, 101.367937, -8.595286], [60.827699, 101.361713, -8.581889], [60.837472, 101.352433, -8.589227], [60.83332, 101.358657, -8.602625], [60.838344, 101.367622, -8.591229], [60.827699, 101.361713, -8.581889], [61.095652, 101.216011, -9.570426]]}]},
			"R_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.427128, 93.760742, -14.092944], [-66.438852, 93.761629, -14.083082], [-66.430315, 93.754791, -14.072319], [-66.418591, 93.753904, -14.082181], [-66.427128, 93.760742, -14.092944], [-66.432268, 93.748073, -14.085976], [-66.430315, 93.754791, -14.072319], [-66.425174, 93.767461, -14.079287], [-66.438852, 93.761629, -14.083082], [-66.432268, 93.748073, -14.085976], [-66.418591, 93.753904, -14.082181], [-66.425174, 93.767461, -14.079287], [-66.427128, 93.760742, -14.092944], [-66.432268, 93.748073, -14.085976], [-66.0941, 94.6723, -13.7671]]}, {"shapeName": "R_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.048194, 95.039629, -13.819944], [-67.046241, 95.046348, -13.806287], [-67.051381, 95.033679, -13.799318], [-67.053335, 95.02696, -13.812976], [-67.048194, 95.039629, -13.819944], [-67.059917, 95.040516, -13.810082], [-67.051381, 95.033679, -13.799318], [-67.039657, 95.032792, -13.80918], [-67.046241, 95.046348, -13.806287], [-67.059917, 95.040516, -13.810082], [-67.053335, 95.02696, -13.812976], [-67.039657, 95.032792, -13.80918], [-67.048194, 95.039629, -13.819944], [-67.059917, 95.040516, -13.810082], [-66.0941, 94.6723, -13.7671]]}, {"shapeName": "R_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-66.254533, 94.395488, -12.794652], [-66.240856, 94.40132, -12.790856], [-66.234273, 94.387764, -12.79375], [-66.24795, 94.381932, -12.797545], [-66.254533, 94.395488, -12.794652], [-66.245996, 94.388651, -12.783889], [-66.234273, 94.387764, -12.79375], [-66.24281, 94.394601, -12.804514], [-66.240856, 94.40132, -12.790856], [-66.245996, 94.388651, -12.783889], [-66.24795, 94.381932, -12.797545], [-66.24281, 94.394601, -12.804514], [-66.254533, 94.395488, -12.794652], [-66.245996, 94.388651, -12.783889], [-66.0941, 94.6723, -13.7671]]}]},
			"L_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[64.574533, 96.186411, -4.830278], [64.57707, 96.194725, -4.817631], [64.563432, 96.19042, -4.812066], [64.560895, 96.182107, -4.824713], [64.574533, 96.186411, -4.830278], [64.573622, 96.179819, -4.816451], [64.563432, 96.19042, -4.812066], [64.564342, 96.197014, -4.825893], [64.57707, 96.194725, -4.817631], [64.573622, 96.179819, -4.816451], [64.560895, 96.182107, -4.824713], [64.564342, 96.197014, -4.825893], [64.574533, 96.186411, -4.830278], [64.573622, 96.179819, -4.816451], [64.131249, 96.999544, -5.266552]]}, {"shapeName": "L_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[64.899761, 97.592695, -4.941617], [64.88957, 97.603298, -4.937233], [64.88866, 97.596705, -4.923406], [64.89885, 97.586102, -4.92779], [64.899761, 97.592695, -4.941617], [64.902297, 97.601008, -4.928971], [64.88866, 97.596705, -4.923406], [64.886123, 97.588391, -4.936052], [64.88957, 97.603298, -4.937233], [64.902297, 97.601008, -4.928971], [64.89885, 97.586102, -4.92779], [64.886123, 97.588391, -4.936052], [64.899761, 97.592695, -4.941617], [64.902297, 97.601008, -4.928971], [64.131249, 96.999544, -5.266552]]}, {"shapeName": "L_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[63.615712, 97.194963, -4.403967], [63.602984, 97.197252, -4.412229], [63.599537, 97.182346, -4.411049], [63.612264, 97.180056, -4.402787], [63.615712, 97.194963, -4.403967], [63.602074, 97.190659, -4.398403], [63.599537, 97.182346, -4.411049], [63.613175, 97.18665, -4.416614], [63.602984, 97.197252, -4.412229], [63.602074, 97.190659, -4.398403], [63.612264, 97.180056, -4.402787], [63.613175, 97.18665, -4.416614], [63.615712, 97.194963, -4.403967], [63.602074, 97.190659, -4.398403], [64.131249, 96.999544, -5.266552]]}]},
			"L_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[58.051838, 97.656149, -3.663784], [58.03877, 97.658771, -3.656181], [58.031063, 97.650534, -3.666585], [58.044132, 97.647912, -3.674189], [58.051838, 97.656149, -3.663784], [58.04308, 97.644377, -3.659294], [58.031063, 97.650534, -3.666585], [58.039822, 97.662307, -3.671076], [58.03877, 97.658771, -3.656181], [58.04308, 97.644377, -3.659294], [58.044132, 97.647912, -3.674189], [58.039822, 97.662307, -3.671076], [58.051838, 97.656149, -3.663784], [58.04308, 97.644377, -3.659294], [57.887764, 98.499143, -4.220975]]}, {"shapeName": "L_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[57.64519, 99.014167, -3.370135], [57.633174, 99.020325, -3.377427], [57.624415, 99.008552, -3.372936], [57.636432, 99.002394, -3.365644], [57.64519, 99.014167, -3.370135], [57.632122, 99.016788, -3.362532], [57.624415, 99.008552, -3.372936], [57.637484, 99.00593, -3.38054], [57.633174, 99.020325, -3.377427], [57.632122, 99.016788, -3.362532], [57.636432, 99.002394, -3.365644], [57.637484, 99.00593, -3.38054], [57.64519, 99.014167, -3.370135], [57.632122, 99.016788, -3.362532], [57.887764, 98.499143, -4.220975]]}, {"shapeName": "L_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[56.905137, 98.239701, -4.344077], [56.906189, 98.243237, -4.358973], [56.9105, 98.228842, -4.362086], [56.909447, 98.225306, -4.34719], [56.905137, 98.239701, -4.344077], [56.897432, 98.231464, -4.354482], [56.9105, 98.228842, -4.362086], [56.918206, 98.237079, -4.351681], [56.906189, 98.243237, -4.358973], [56.897432, 98.231464, -4.354482], [56.909447, 98.225306, -4.34719], [56.918206, 98.237079, -4.351681], [56.905137, 98.239701, -4.344077], [56.897432, 98.231464, -4.354482], [57.887764, 98.499143, -4.220975]]}]},
			"R_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_B_CTLShape", "degree": 3, "form": 2, "points": [[-65.057721, 96.650061, -7.945588], [-65.167667, 96.706472, -7.975857], [-65.254528, 96.774226, -7.91221], [-65.267423, 96.813635, -7.79193], [-65.198797, 96.801612, -7.685476], [-65.088851, 96.745202, -7.655207], [-65.001989, 96.677447, -7.718854], [-64.989095, 96.638039, -7.839134]]}]},
			"L_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[62.130602, 100.231898, -12.742499], [62.138655, 100.23819, -12.731051], [62.129668, 100.231097, -12.720832], [62.121616, 100.224806, -12.73228], [62.130602, 100.231898, -12.742499], [62.136838, 100.222966, -12.731692], [62.129668, 100.231097, -12.720832], [62.123431, 100.24003, -12.731639], [62.138655, 100.23819, -12.731051], [62.136838, 100.222966, -12.731692], [62.121616, 100.224806, -12.73228], [62.123431, 100.24003, -12.731639], [62.130602, 100.231898, -12.742499], [62.136838, 100.222966, -12.731692], [61.497686, 101.036423, -12.729157]]}, {"shapeName": "L_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[62.301877, 101.668148, -12.682026], [62.294706, 101.676279, -12.671166], [62.300943, 101.667347, -12.660359], [62.308114, 101.659215, -12.671219], [62.301877, 101.668148, -12.682026], [62.309929, 101.674439, -12.670578], [62.300943, 101.667347, -12.660359], [62.292891, 101.661055, -12.671807], [62.294706, 101.676279, -12.671166], [62.309929, 101.674439, -12.670578], [62.308114, 101.659215, -12.671219], [62.292891, 101.661055, -12.671807], [62.301877, 101.668148, -12.682026], [62.309929, 101.674439, -12.670578], [61.497686, 101.036423, -12.729157]]}, {"shapeName": "L_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.462174, 101.005333, -11.706517], [61.446951, 101.007174, -11.707105], [61.445135, 100.991949, -11.707746], [61.460359, 100.990109, -11.707158], [61.462174, 101.005333, -11.706517], [61.453188, 100.998241, -11.696299], [61.445135, 100.991949, -11.707746], [61.454122, 100.999042, -11.717965], [61.446951, 101.007174, -11.707105], [61.453188, 100.998241, -11.696299], [61.460359, 100.990109, -11.707158], [61.454122, 100.999042, -11.717965], [61.462174, 101.005333, -11.706517], [61.453188, 100.998241, -11.696299], [61.497686, 101.036423, -12.729157]]}]},
			"world_CTL": {"color": 1, "shapes": [{"shapeName": "world_CTLShape", "degree": 1, "form": 0, "points": [[-0.013805, 0.0, 66.018741], [-29.337262, 0.0, 36.65444], [-21.994863, 0.0, 36.655972], [-21.991795, 0.0, 21.976887], [-36.670879, 0.0, 21.973819], [-36.672417, 0.0, 29.316218], [-66.018741, 0.0, -0.013805], [-36.65444, 0.0, -29.337262], [-36.655972, 0.0, -21.994863], [-21.976887, 0.0, -21.991795], [-21.973819, 0.0, -36.670879], [-29.316218, 0.0, -36.672417], [0.013805, 0.0, -66.018741], [29.337262, 0.0, -36.65444], [21.994863, 0.0, -36.655972], [21.991795, 0.0, -21.976887], [36.670879, 0.0, -21.973819], [36.672417, 0.0, -29.316218], [66.018741, 0.0, 0.013805], [36.65444, 0.0, 29.337262], [36.655972, 0.0, 21.994863], [21.976887, 0.0, 21.991795], [21.973819, 0.0, 36.670879], [29.316218, 0.0, 36.672417], [-0.013805, 0.0, 66.018741], [-5.760835, 0.079995, 60.372173], [-5.257895, 0.0, 59.835172], [-5.257438, 0.0, 57.641024], [-4.800324, 0.0, 57.641121], [-4.829356, 0.0, 59.852406], [-4.503628, 0.0, 59.686765], [-4.514856, 0.0, 58.726824], [-4.052027, 0.0, 58.726922], [-4.052227, 0.0, 59.686862], [-3.766565, 0.0, 59.852623], [-3.766097, 0.0, 57.607048], [-3.303268, 0.0, 57.607146], [-3.303748, 0.0, 59.909859], [-3.675234, 0.0, 60.28119], [-4.246564, 0.0, 59.995374], [-4.875159, 0.0, 60.280939], [-5.257901, 0.0, 59.8466], [-4.875159, 0.0, 60.280939], [-4.252278, 0.0, 60.001088], [-3.675228, 0.0, 60.275476], [-2.561017, 0.0, 60.281425], [-2.938057, 0.0, 59.909939], [-2.937657, 0.0, 57.984345], [-2.560458, 0.0, 57.607306], [-1.354818, 0.0, 57.607557], [-0.983493, 0.0, 57.984751], [-0.983893, 0.0, 59.910345], [-1.355378, 0.0, 60.281676], [-2.561017, 0.0, 60.281425], [-2.418078, 0.0, 59.852908], [-2.474846, 0.0, 58.081579], [-1.44063, 0.0, 58.093224], [-1.44671, 0.0, 59.853108], [-2.423792, 0.0, 59.864336], [-2.561017, 0.0, 60.281425], [-1.355378, 0.0, 60.281676], [-0.583998, 0.0, 60.281836], [-0.612008, 0.0, 57.607711], [0.690768, 0.0, 57.60798], [1.067808, 0.0, 57.985179], [1.067642, 0.0, 58.790843], [0.684729, 0.0, 59.162169], [0.661867, 0.0, 59.190733], [1.410169, 0.0, 60.270825], [1.410164, 0.0, 60.282253], [0.873054, 0.0, 60.282139], [0.124758, 0.0, 59.196338], [-0.155225, 0.0, 59.196281], [-0.154985, 0.0, 58.053495], [0.56497, 0.0, 58.053644], [0.570542, 0.0, 58.733601], [-0.155127, 0.0, 58.733453], [-0.155453, 0.0, 60.281927], [-0.583998, 0.0, 60.281836], [3.661452, 0.0, 60.282722], [3.661543, 0.0, 59.854177], [2.164494, 0.0, 59.848149], [2.164962, 0.0, 57.608288], [1.702134, 0.0, 57.608197], [1.701574, 0.0, 60.28231], [5.609902, 0.0, 60.283127], [5.952817, 0.0, 59.911796], [5.981787, 0.0, 57.986208], [5.610462, 0.0, 57.609014], [4.027703, 0.0, 57.608683], [4.027143, 0.0, 60.282802], [4.495777, 0.0, 59.854354], [4.484726, 0.0, 58.043033], [5.461808, 0.0, 58.043238], [5.450003, 0.0, 59.843126], [4.478635, 0.0, 59.865776], [4.015715, 0.0, 60.282796]]}]},
			"R_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_C_CTLShape", "degree": 3, "form": 2, "points": [[-67.45268, 93.128889, -10.747471], [-67.562183, 93.172451, -10.795408], [-67.672667, 93.211765, -10.746069], [-67.719411, 93.223801, -10.628355], [-67.675034, 93.201509, -10.511221], [-67.565531, 93.157947, -10.463284], [-67.455048, 93.118633, -10.512623], [-67.408304, 93.106597, -10.630337]]}]},
			"R_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_C_CTLShape", "degree": 3, "form": 2, "points": [[-58.381669, 95.232804, -2.244147], [-58.302923, 95.296396, -2.167065], [-58.317448, 95.384408, -2.076349], [-58.416736, 95.445284, -2.025139], [-58.542626, 95.443364, -2.043433], [-58.621372, 95.379772, -2.120515], [-58.606847, 95.29176, -2.211231], [-58.507559, 95.230884, -2.262441]]}]},
			"C_visibility_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_visibility_PIV_CTLShape", "degree": 1, "form": 0, "points": [[129.562627, 200.0, -8.427807], [129.562627, 200.922695, 0.0], [129.562627, 200.0, 8.427807], [129.562627, 199.077305, 0.0], [129.562627, 200.0, -8.427807], [130.485237, 200.0, 0.0], [129.562627, 200.0, 8.427807], [128.639931, 200.0, 0.0], [129.562627, 200.922695, 0.0], [130.485237, 200.0, 0.0], [129.562627, 199.077305, 0.0], [128.639931, 200.0, 0.0], [129.562627, 200.0, -8.427807], [130.485237, 200.0, 0.0], [42.516602, 200.0, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[42.516602, 287.046025, -8.427807], [41.593907, 287.046025, 0.0], [42.516602, 287.046025, 8.427807], [43.439297, 287.046025, 0.0], [42.516602, 287.046025, -8.427807], [42.516602, 287.968635, 0.0], [42.516602, 287.046025, 8.427807], [42.516602, 286.123329, 0.0], [41.593907, 287.046025, 0.0], [42.516602, 287.968635, 0.0], [43.439297, 287.046025, 0.0], [42.516602, 286.123329, 0.0], [42.516602, 287.046025, -8.427807], [42.516602, 287.968635, 0.0], [42.516602, 200.0, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[42.516602, 200.922695, 795.069765], [41.593907, 200.0, 795.069765], [42.516602, 199.077305, 795.069765], [43.439297, 200.0, 795.069765], [42.516602, 200.922695, 795.069765], [42.516602, 200.0, 803.496796], [42.516602, 199.077305, 795.069765], [42.516602, 200.0, 786.641958], [41.593907, 200.0, 795.069765], [42.516602, 200.0, 803.496796], [43.439297, 200.0, 795.069765], [42.516602, 200.0, 786.641958], [42.516602, 200.922695, 795.069765], [42.516602, 200.0, 803.496796], [42.516602, 200.0, 0.0]]}]},
			"R_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_C_CTLShape", "degree": 3, "form": 2, "points": [[-66.051215, 93.306282, -3.422684], [-66.172916, 93.342582, -3.415093], [-66.24539, 93.396123, -3.325274], [-66.226182, 93.435541, -3.205843], [-66.126545, 93.437747, -3.126761], [-66.004844, 93.401447, -3.134353], [-65.932369, 93.347906, -3.224171], [-65.951577, 93.308488, -3.343602]]}]},
			"L_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[61.258, 100.758328, -7.976656], [61.259619, 100.768029, -7.964876], [61.246688, 100.762611, -7.958637], [61.245069, 100.752911, -7.970417], [61.258, 100.758328, -7.976656], [61.258073, 100.752986, -7.962272], [61.246688, 100.762611, -7.958637], [61.246615, 100.767954, -7.973022], [61.259619, 100.768029, -7.964876], [61.258073, 100.752986, -7.962272], [61.245069, 100.752911, -7.970417], [61.246615, 100.767954, -7.973022], [61.258, 100.758328, -7.976656], [61.258073, 100.752986, -7.962272], [60.711838, 101.466573, -8.47477]]}, {"shapeName": "L_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[61.403839, 102.177534, -8.222404], [61.392454, 102.18716, -8.21877], [61.392528, 102.181816, -8.204385], [61.403913, 102.17219, -8.208019], [61.403839, 102.177534, -8.222404], [61.405458, 102.187233, -8.210624], [61.392528, 102.181816, -8.204385], [61.390908, 102.172116, -8.216165], [61.392454, 102.18716, -8.21877], [61.405458, 102.187233, -8.210624], [61.403913, 102.17219, -8.208019], [61.390908, 102.172116, -8.216165], [61.403839, 102.177534, -8.222404], [61.405458, 102.187233, -8.210624], [60.711838, 101.466573, -8.47477]]}, {"shapeName": "L_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[60.185555, 101.676137, -7.622051], [60.17255, 101.676062, -7.630197], [60.171004, 101.661019, -7.627592], [60.184009, 101.661093, -7.619446], [60.185555, 101.676137, -7.622051], [60.172624, 101.670719, -7.615813], [60.171004, 101.661019, -7.627592], [60.183935, 101.666436, -7.633831], [60.17255, 101.676062, -7.630197], [60.172624, 101.670719, -7.615813], [60.184009, 101.661093, -7.619446], [60.183935, 101.666436, -7.633831], [60.185555, 101.676137, -7.622051], [60.172624, 101.670719, -7.615813], [60.711838, 101.466573, -8.47477]]}]},
			"R_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-64.574484, 96.186367, -4.830276], [-64.577021, 96.194681, -4.817629], [-64.563383, 96.190376, -4.812064], [-64.560846, 96.182063, -4.824711], [-64.574484, 96.186367, -4.830276], [-64.573573, 96.179775, -4.816449], [-64.563383, 96.190376, -4.812064], [-64.564293, 96.19697, -4.825891], [-64.577021, 96.194681, -4.817629], [-64.573573, 96.179775, -4.816449], [-64.560846, 96.182063, -4.824711], [-64.564293, 96.19697, -4.825891], [-64.574484, 96.186367, -4.830276], [-64.573573, 96.179775, -4.816449], [-64.1312, 96.9995, -5.26655]]}, {"shapeName": "R_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-64.899712, 97.592651, -4.941615], [-64.889521, 97.603254, -4.937231], [-64.888611, 97.596661, -4.923404], [-64.898801, 97.586058, -4.927788], [-64.899712, 97.592651, -4.941615], [-64.902248, 97.600964, -4.928969], [-64.888611, 97.596661, -4.923404], [-64.886074, 97.588347, -4.93605], [-64.889521, 97.603254, -4.937231], [-64.902248, 97.600964, -4.928969], [-64.898801, 97.586058, -4.927788], [-64.886074, 97.588347, -4.93605], [-64.899712, 97.592651, -4.941615], [-64.902248, 97.600964, -4.928969], [-64.1312, 96.9995, -5.26655]]}, {"shapeName": "R_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-63.615663, 97.194919, -4.403965], [-63.602935, 97.197208, -4.412227], [-63.599488, 97.182302, -4.411047], [-63.612215, 97.180012, -4.402785], [-63.615663, 97.194919, -4.403965], [-63.602025, 97.190615, -4.398401], [-63.599488, 97.182302, -4.411047], [-63.613126, 97.186606, -4.416612], [-63.602935, 97.197208, -4.412227], [-63.602025, 97.190615, -4.398401], [-63.612215, 97.180012, -4.402785], [-63.613126, 97.186606, -4.416612], [-63.615663, 97.194919, -4.403965], [-63.602025, 97.190615, -4.398401], [-64.1312, 96.9995, -5.26655]]}]},
			"R_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-62.130616, 100.231475, -12.742542], [-62.138669, 100.237767, -12.731094], [-62.129682, 100.230674, -12.720875], [-62.12163, 100.224383, -12.732323], [-62.130616, 100.231475, -12.742542], [-62.136852, 100.222543, -12.731735], [-62.129682, 100.230674, -12.720875], [-62.123445, 100.239607, -12.731682], [-62.138669, 100.237767, -12.731094], [-62.136852, 100.222543, -12.731735], [-62.12163, 100.224383, -12.732323], [-62.123445, 100.239607, -12.731682], [-62.130616, 100.231475, -12.742542], [-62.136852, 100.222543, -12.731735], [-61.4977, 101.036, -12.7292]]}, {"shapeName": "R_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-62.301891, 101.667725, -12.682069], [-62.29472, 101.675856, -12.671209], [-62.300957, 101.666924, -12.660402], [-62.308128, 101.658792, -12.671262], [-62.301891, 101.667725, -12.682069], [-62.309943, 101.674016, -12.670621], [-62.300957, 101.666924, -12.660402], [-62.292905, 101.660632, -12.67185], [-62.29472, 101.675856, -12.671209], [-62.309943, 101.674016, -12.670621], [-62.308128, 101.658792, -12.671262], [-62.292905, 101.660632, -12.67185], [-62.301891, 101.667725, -12.682069], [-62.309943, 101.674016, -12.670621], [-61.4977, 101.036, -12.7292]]}, {"shapeName": "R_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.462188, 101.00491, -11.70656], [-61.446965, 101.006751, -11.707148], [-61.445149, 100.991526, -11.707789], [-61.460373, 100.989686, -11.707201], [-61.462188, 101.00491, -11.70656], [-61.453202, 100.997818, -11.696342], [-61.445149, 100.991526, -11.707789], [-61.454136, 100.998619, -11.718008], [-61.446965, 101.006751, -11.707148], [-61.453202, 100.997818, -11.696342], [-61.460373, 100.989686, -11.707201], [-61.454136, 100.998619, -11.718008], [-61.462188, 101.00491, -11.70656], [-61.453202, 100.997818, -11.696342], [-61.4977, 101.036, -12.7292]]}]},
			"L_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.673388, 91.963672, -6.651065], [67.681043, 91.968367, -6.638621], [67.668609, 91.965796, -6.630002], [67.660954, 91.961101, -6.642446], [67.673388, 91.963672, -6.651065], [67.674337, 91.954565, -6.63875], [67.668609, 91.965796, -6.630002], [67.667659, 91.974903, -6.642317], [67.681043, 91.968367, -6.638621], [67.674337, 91.954565, -6.63875], [67.660954, 91.961101, -6.642446], [67.667659, 91.974903, -6.642317], [67.673388, 91.963672, -6.651065], [67.674337, 91.954565, -6.63875], [67.35601, 92.924101, -6.808754]]}, {"shapeName": "L_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[68.305962, 93.265787, -6.63887], [68.300234, 93.277019, -6.630122], [68.301184, 93.267912, -6.617808], [68.306912, 93.25668, -6.626556], [68.305962, 93.265787, -6.63887], [68.313616, 93.270482, -6.626427], [68.301184, 93.267912, -6.617808], [68.293529, 93.263216, -6.630251], [68.300234, 93.277019, -6.630122], [68.313616, 93.270482, -6.626427], [68.306912, 93.25668, -6.626556], [68.293529, 93.263216, -6.630251], [68.305962, 93.265787, -6.63887], [68.313616, 93.270482, -6.626427], [67.35601, 92.924101, -6.808754]]}, {"shapeName": "L_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[67.140648, 93.027934, -5.813335], [67.127265, 93.03447, -5.817031], [67.120559, 93.020667, -5.81716], [67.133942, 93.014131, -5.813465], [67.140648, 93.027934, -5.813335], [67.128214, 93.025363, -5.804717], [67.120559, 93.020667, -5.81716], [67.132993, 93.023238, -5.825779], [67.127265, 93.03447, -5.817031], [67.128214, 93.025363, -5.804717], [67.133942, 93.014131, -5.813465], [67.132993, 93.023238, -5.825779], [67.140648, 93.027934, -5.813335], [67.128214, 93.025363, -5.804717], [67.35601, 92.924101, -6.808754]]}]},
			"L_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.273671, 1.0, -0.010851], [1.273671, 1.010851, 0.0], [1.273671, 1.0, 0.010851], [1.273671, 0.989149, 0.0], [1.273671, 1.0, -0.010851], [1.284521, 1.0, 0.0], [1.273671, 1.0, 0.010851], [1.26282, 1.0, 0.0], [1.273671, 1.010851, 0.0], [1.284521, 1.0, 0.0], [1.273671, 0.989149, 0.0], [1.26282, 1.0, 0.0], [1.273671, 1.0, -0.010851], [1.284521, 1.0, 0.0], [0.25, 1.0, 0.0]]}, {"shapeName": "L_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.25, 2.023671, -0.010851], [0.239149, 2.023671, 0.0], [0.25, 2.023671, 0.010851], [0.260851, 2.023671, 0.0], [0.25, 2.023671, -0.010851], [0.25, 2.034521, 0.0], [0.25, 2.023671, 0.010851], [0.25, 2.01282, 0.0], [0.239149, 2.023671, 0.0], [0.25, 2.034521, 0.0], [0.260851, 2.023671, 0.0], [0.25, 2.01282, 0.0], [0.25, 2.023671, -0.010851], [0.25, 2.034521, 0.0], [0.25, 1.0, 0.0]]}, {"shapeName": "L_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.25, 1.010851, 1.023671], [0.239149, 1.0, 1.023671], [0.25, 0.989149, 1.023671], [0.260851, 1.0, 1.023671], [0.25, 1.010851, 1.023671], [0.25, 1.0, 1.034521], [0.25, 0.989149, 1.023671], [0.25, 1.0, 1.01282], [0.239149, 1.0, 1.023671], [0.25, 1.0, 1.034521], [0.260851, 1.0, 1.023671], [0.25, 1.0, 1.01282], [0.25, 1.010851, 1.023671], [0.25, 1.0, 1.034521], [0.25, 1.0, 0.0]]}]},
			"L_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_C_CTLShape", "degree": 3, "form": 2, "points": [[65.96709, 94.662741, -13.873973], [66.069677, 94.717927, -13.925129], [66.186561, 94.746414, -13.88374], [66.249273, 94.731515, -13.774051], [66.221078, 94.681958, -13.660316], [66.118491, 94.626772, -13.60916], [66.001606, 94.598285, -13.650549], [65.938894, 94.613184, -13.760238]]}]},
			"L_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_B_CTLShape", "degree": 3, "form": 2, "points": [[64.103768, 96.909492, -5.403546], [64.216279, 96.968835, -5.406048], [64.27898, 97.046168, -5.326835], [64.255143, 97.096189, -5.212309], [64.158731, 97.089596, -5.129557], [64.04622, 97.030253, -5.127056], [63.983519, 96.95292, -5.206269], [64.007356, 96.902899, -5.320795]]}]},
			"R_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_D_CTLShape", "degree": 3, "form": 2, "points": [[-66.787584, 92.426302, -14.645442], [-66.895311, 92.460255, -14.703996], [-67.017796, 92.466947, -14.670241], [-67.083287, 92.442456, -14.563951], [-67.053423, 92.40113, -14.447389], [-66.945696, 92.367176, -14.388835], [-66.823211, 92.360485, -14.42259], [-66.75772, 92.384975, -14.528879]]}]},
			"R_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.273671, 1.0, -0.010851], [-1.273671, 1.010851, 0.0], [-1.273671, 1.0, 0.010851], [-1.273671, 0.989149, -0.0], [-1.273671, 1.0, -0.010851], [-1.284521, 1.0, 0.0], [-1.273671, 1.0, 0.010851], [-1.26282, 1.0, 0.0], [-1.273671, 1.010851, 0.0], [-1.284521, 1.0, 0.0], [-1.273671, 0.989149, -0.0], [-1.26282, 1.0, 0.0], [-1.273671, 1.0, -0.010851], [-1.284521, 1.0, 0.0], [-0.25, 1.0, 0.0]]}, {"shapeName": "R_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.25, 2.023671, -0.010851], [-0.239149, 2.023671, 0.0], [-0.25, 2.023671, 0.010851], [-0.260851, 2.023671, 0.0], [-0.25, 2.023671, -0.010851], [-0.25, 2.034521, 0.0], [-0.25, 2.023671, 0.010851], [-0.25, 2.01282, 0.0], [-0.239149, 2.023671, 0.0], [-0.25, 2.034521, 0.0], [-0.260851, 2.023671, 0.0], [-0.25, 2.01282, 0.0], [-0.25, 2.023671, -0.010851], [-0.25, 2.034521, 0.0], [-0.25, 1.0, 0.0]]}, {"shapeName": "R_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.25, 1.010851, 1.023671], [-0.239149, 1.0, 1.023671], [-0.25, 0.989149, 1.023671], [-0.260851, 1.0, 1.023671], [-0.25, 1.010851, 1.023671], [-0.25, 1.0, 1.034521], [-0.25, 0.989149, 1.023671], [-0.25, 1.0, 1.01282], [-0.239149, 1.0, 1.023671], [-0.25, 1.0, 1.034521], [-0.260851, 1.0, 1.023671], [-0.25, 1.0, 1.01282], [-0.25, 1.010851, 1.023671], [-0.25, 1.0, 1.034521], [-0.25, 1.0, 0.0]]}]},
			"L_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_B_CTLShape", "degree": 3, "form": 2, "points": [[64.962172, 96.963793, -10.551008], [65.0603, 97.029837, -10.597867], [65.159464, 97.091572, -10.547453], [65.201577, 97.112835, -10.429297], [65.161969, 97.081171, -10.312613], [65.063842, 97.015127, -10.265754], [64.964677, 96.953391, -10.316168], [64.922564, 96.932128, -10.434324]]}]},
			"R_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_C_CTLShape", "degree": 3, "form": 2, "points": [[-67.273089, 92.873241, -6.943548], [-67.392612, 92.907831, -6.970085], [-67.490694, 92.951952, -6.902116], [-67.50988, 92.979759, -6.779457], [-67.43893, 92.974962, -6.67396], [-67.319407, 92.940372, -6.647423], [-67.221325, 92.896251, -6.715392], [-67.202139, 92.868444, -6.838051]]}]},
			"R_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-58.051874, 97.656106, -3.663789], [-58.038806, 97.658728, -3.656186], [-58.031099, 97.650491, -3.66659], [-58.044168, 97.647869, -3.674194], [-58.051874, 97.656106, -3.663789], [-58.043116, 97.644334, -3.659299], [-58.031099, 97.650491, -3.66659], [-58.039858, 97.662264, -3.671081], [-58.038806, 97.658728, -3.656186], [-58.043116, 97.644334, -3.659299], [-58.044168, 97.647869, -3.674194], [-58.039858, 97.662264, -3.671081], [-58.051874, 97.656106, -3.663789], [-58.043116, 97.644334, -3.659299], [-57.8878, 98.4991, -4.22098]]}, {"shapeName": "R_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-57.645226, 99.014124, -3.37014], [-57.63321, 99.020282, -3.377432], [-57.624451, 99.008509, -3.372941], [-57.636468, 99.002351, -3.365649], [-57.645226, 99.014124, -3.37014], [-57.632158, 99.016745, -3.362537], [-57.624451, 99.008509, -3.372941], [-57.63752, 99.005887, -3.380545], [-57.63321, 99.020282, -3.377432], [-57.632158, 99.016745, -3.362537], [-57.636468, 99.002351, -3.365649], [-57.63752, 99.005887, -3.380545], [-57.645226, 99.014124, -3.37014], [-57.632158, 99.016745, -3.362537], [-57.8878, 98.4991, -4.22098]]}, {"shapeName": "R_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-56.905173, 98.239658, -4.344082], [-56.906225, 98.243194, -4.358978], [-56.910536, 98.228799, -4.362091], [-56.909483, 98.225263, -4.347195], [-56.905173, 98.239658, -4.344082], [-56.897468, 98.231421, -4.354487], [-56.910536, 98.228799, -4.362091], [-56.918242, 98.237036, -4.351686], [-56.906225, 98.243194, -4.358978], [-56.897468, 98.231421, -4.354487], [-56.909483, 98.225263, -4.347195], [-56.918242, 98.237036, -4.351686], [-56.905173, 98.239658, -4.344082], [-56.897468, 98.231421, -4.354487], [-57.8878, 98.4991, -4.22098]]}]},
			"R_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_A_CTLShape", "degree": 3, "form": 2, "points": [[-61.410455, 100.96827, -12.853165], [-61.504836, 101.042558, -12.895119], [-61.595029, 101.113252, -12.839854], [-61.628199, 101.138941, -12.719744], [-61.584917, 101.104576, -12.605148], [-61.490536, 101.030288, -12.563195], [-61.400344, 100.959594, -12.61846], [-61.367173, 100.933905, -12.738569]]}]},
			"L_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_C_CTLShape", "degree": 3, "form": 2, "points": [[67.273089, 92.873241, -6.943548], [67.392612, 92.907831, -6.970085], [67.490694, 92.951952, -6.902116], [67.50988, 92.979759, -6.779457], [67.43893, 92.974962, -6.67396], [67.319407, 92.940372, -6.647423], [67.221325, 92.896251, -6.715392], [67.202139, 92.868444, -6.838051]]}]},
			"L_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[58.360944, 96.074407, -2.847783], [58.368373, 96.084126, -2.838518], [58.381731, 96.079849, -2.844744], [58.374302, 96.07013, -2.854009], [58.360944, 96.074407, -2.847783], [58.370375, 96.084961, -2.853709], [58.381731, 96.079849, -2.844744], [58.3723, 96.069294, -2.838817], [58.368373, 96.084126, -2.838518], [58.370375, 96.084961, -2.853709], [58.374302, 96.07013, -2.854009], [58.3723, 96.069294, -2.838817], [58.360944, 96.074407, -2.847783], [58.370375, 96.084961, -2.853709], [58.462148, 95.338084, -2.14379]]}, {"shapeName": "L_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[58.172103, 95.995521, -1.414632], [58.183459, 95.990408, -1.405667], [58.19289, 96.000964, -1.411594], [58.181534, 96.006076, -1.420559], [58.172103, 95.995521, -1.414632], [58.179532, 96.005239, -1.405368], [58.19289, 96.000964, -1.411594], [58.185461, 95.991245, -1.420858], [58.183459, 95.990408, -1.405667], [58.179532, 96.005239, -1.405368], [58.181534, 96.006076, -1.420559], [58.185461, 95.991245, -1.420858], [58.172103, 95.995521, -1.414632], [58.179532, 96.005239, -1.405368], [58.462148, 95.338084, -2.14379]]}, {"shapeName": "L_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[59.439719, 95.601805, -1.992712], [59.443646, 95.586974, -1.993011], [59.445648, 95.58781, -2.008202], [59.441721, 95.602642, -2.007904], [59.439719, 95.601805, -1.992712], [59.453077, 95.597529, -1.998938], [59.445648, 95.58781, -2.008202], [59.43229, 95.592086, -2.001977], [59.443646, 95.586974, -1.993011], [59.453077, 95.597529, -1.998938], [59.441721, 95.602642, -2.007904], [59.43229, 95.592086, -2.001977], [59.439719, 95.601805, -1.992712], [59.453077, 95.597529, -1.998938], [58.462148, 95.338084, -2.14379]]}]},
			"R_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_B_CTLShape", "degree": 3, "form": 2, "points": [[-64.103768, 96.909492, -5.403546], [-64.216279, 96.968835, -5.406048], [-64.27898, 97.046168, -5.326835], [-64.255143, 97.096189, -5.212309], [-64.158731, 97.089596, -5.129557], [-64.04622, 97.030253, -5.127056], [-63.983519, 96.95292, -5.206269], [-64.007356, 96.902899, -5.320795]]}]},
			"L_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_D_CTLShape", "degree": 3, "form": 2, "points": [[66.743299, 90.804715, -2.481897], [66.869503, 90.804356, -2.465804], [66.947583, 90.819837, -2.366554], [66.9318, 90.842089, -2.242287], [66.8314, 90.858076, -2.165797], [66.705196, 90.858434, -2.18189], [66.627117, 90.842954, -2.281139], [66.642899, 90.820702, -2.405406]]}]},
			"R_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.673378, 91.963671, -6.651061], [-67.681033, 91.968366, -6.638617], [-67.668599, 91.965795, -6.629998], [-67.660944, 91.9611, -6.642442], [-67.673378, 91.963671, -6.651061], [-67.674327, 91.954564, -6.638746], [-67.668599, 91.965795, -6.629998], [-67.667649, 91.974902, -6.642313], [-67.681033, 91.968366, -6.638617], [-67.674327, 91.954564, -6.638746], [-67.660944, 91.9611, -6.642442], [-67.667649, 91.974902, -6.642313], [-67.673378, 91.963671, -6.651061], [-67.674327, 91.954564, -6.638746], [-67.356, 92.9241, -6.80875]]}, {"shapeName": "R_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-68.305952, 93.265786, -6.638866], [-68.300224, 93.277018, -6.630118], [-68.301174, 93.267911, -6.617804], [-68.306902, 93.256679, -6.626552], [-68.305952, 93.265786, -6.638866], [-68.313606, 93.270481, -6.626423], [-68.301174, 93.267911, -6.617804], [-68.293519, 93.263215, -6.630247], [-68.300224, 93.277018, -6.630118], [-68.313606, 93.270481, -6.626423], [-68.306902, 93.256679, -6.626552], [-68.293519, 93.263215, -6.630247], [-68.305952, 93.265786, -6.638866], [-68.313606, 93.270481, -6.626423], [-67.356, 92.9241, -6.80875]]}, {"shapeName": "R_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-67.140638, 93.027933, -5.813331], [-67.127255, 93.034469, -5.817027], [-67.120549, 93.020666, -5.817156], [-67.133932, 93.01413, -5.813461], [-67.140638, 93.027933, -5.813331], [-67.128204, 93.025362, -5.804713], [-67.120549, 93.020666, -5.817156], [-67.132983, 93.023237, -5.825775], [-67.127255, 93.034469, -5.817027], [-67.128204, 93.025362, -5.804713], [-67.133932, 93.01413, -5.813461], [-67.132983, 93.023237, -5.825775], [-67.140638, 93.027933, -5.813331], [-67.128204, 93.025362, -5.804713], [-67.356, 92.9241, -6.80875]]}]},
			"R_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_B_CTLShape", "degree": 3, "form": 2, "points": [[-58.029331, 98.470742, -4.303342], [-58.046892, 98.542154, -4.199523], [-57.971239, 98.588371, -4.10827], [-57.846687, 98.582319, -4.083039], [-57.746197, 98.527544, -4.138608], [-57.728635, 98.456132, -4.242427], [-57.804289, 98.409915, -4.33368], [-57.928841, 98.415967, -4.358912]]}]},
		}

		controlShapes.set_data(data)