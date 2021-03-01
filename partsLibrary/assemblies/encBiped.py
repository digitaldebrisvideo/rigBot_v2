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
		guide.build("encBipedArm", **{'pickWalkParent': u'chest_Mid_anim', 'side': u'L', 'parent': u'chest_Mid_bind', 'name': u''})
		guide.build("encTorso", **{'numberMidCtrls': 1, 'parent': u'root_Mid_jnt', 'pickWalkParent': u'world_anim', 'numberJoints': 5, 'side': u'C', 'name': u''})
		guide.build("encNeck", **{'pickWalkParent': u'chest_Mid_anim', 'side': u'C', 'parent': u'chest_Mid_bind', 'name': u''})

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
			mc.xform("C_worldRoot_guide", r=1, s=[1.0, 1.0, 1.0])

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
			mc.xform("world_CTL", r=1, s=[0.09999999999999998, 0.09999999999999998, 0.09999999999999998])

		if mc.objExists("visibility_CTL"):
			if not mc.getAttr("visibility_CTL.mirrorMode", l=1):
				mc.setAttr("visibility_CTL.mirrorMode", 0)

			if not mc.getAttr("visibility_CTL.rotateOrder", l=1):
				mc.setAttr("visibility_CTL.rotateOrder", 0)

			mc.xform("visibility_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("visibility_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("visibility_CTL", r=1, s=[3.4869936676468, 3.4869936676468, 3.4869936676468])

		if mc.objExists("L_thumb_A_CTL"):
			if not mc.getAttr("L_thumb_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_thumb_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_thumb_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_thumb_A_CTL.rotateOrder", 0)

			mc.xform("L_thumb_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_A_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_thumb_B_CTL"):
			if not mc.getAttr("L_thumb_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_thumb_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_thumb_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_thumb_B_CTL.rotateOrder", 0)

			mc.xform("L_thumb_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_B_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_thumb_C_CTL"):
			if not mc.getAttr("L_thumb_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_thumb_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_thumb_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_thumb_C_CTL.rotateOrder", 0)

			mc.xform("L_thumb_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_thumb_C_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_index_A_CTL"):
			if not mc.getAttr("L_index_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_index_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_index_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_A_CTL.rotateOrder", 0)

			mc.xform("L_index_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_A_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_index_B_CTL"):
			if not mc.getAttr("L_index_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_index_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_index_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_B_CTL.rotateOrder", 0)

			mc.xform("L_index_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_B_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_index_C_CTL"):
			if not mc.getAttr("L_index_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_index_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_index_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_C_CTL.rotateOrder", 0)

			mc.xform("L_index_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_C_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_index_D_CTL"):
			if not mc.getAttr("L_index_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_index_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_index_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_index_D_CTL.rotateOrder", 0)

			mc.xform("L_index_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_index_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_index_D_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_middle_A_CTL"):
			if not mc.getAttr("L_middle_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_middle_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_middle_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_A_CTL.rotateOrder", 0)

			mc.xform("L_middle_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_A_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_middle_B_CTL"):
			if not mc.getAttr("L_middle_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_middle_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_middle_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_B_CTL.rotateOrder", 0)

			mc.xform("L_middle_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_B_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_middle_C_CTL"):
			if not mc.getAttr("L_middle_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_middle_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_middle_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_C_CTL.rotateOrder", 0)

			mc.xform("L_middle_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_C_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_middle_D_CTL"):
			if not mc.getAttr("L_middle_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_middle_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_middle_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_middle_D_CTL.rotateOrder", 0)

			mc.xform("L_middle_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_middle_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_middle_D_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_ring_A_CTL"):
			if not mc.getAttr("L_ring_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_ring_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_ring_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_A_CTL.rotateOrder", 0)

			mc.xform("L_ring_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_A_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_ring_B_CTL"):
			if not mc.getAttr("L_ring_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_ring_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_ring_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_B_CTL.rotateOrder", 0)

			mc.xform("L_ring_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_B_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_ring_C_CTL"):
			if not mc.getAttr("L_ring_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_ring_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_ring_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_C_CTL.rotateOrder", 0)

			mc.xform("L_ring_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_C_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_ring_D_CTL"):
			if not mc.getAttr("L_ring_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_ring_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_ring_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_ring_D_CTL.rotateOrder", 0)

			mc.xform("L_ring_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_ring_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_ring_D_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_pinky_A_CTL"):
			if not mc.getAttr("L_pinky_A_CTL.mirrorMode", l=1):
				mc.setAttr("L_pinky_A_CTL.mirrorMode", 0)

			if not mc.getAttr("L_pinky_A_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_A_CTL.rotateOrder", 0)

			mc.xform("L_pinky_A_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_A_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_pinky_B_CTL"):
			if not mc.getAttr("L_pinky_B_CTL.mirrorMode", l=1):
				mc.setAttr("L_pinky_B_CTL.mirrorMode", 0)

			if not mc.getAttr("L_pinky_B_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_B_CTL.rotateOrder", 0)

			mc.xform("L_pinky_B_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_B_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_B_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_pinky_C_CTL"):
			if not mc.getAttr("L_pinky_C_CTL.mirrorMode", l=1):
				mc.setAttr("L_pinky_C_CTL.mirrorMode", 0)

			if not mc.getAttr("L_pinky_C_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_C_CTL.rotateOrder", 0)

			mc.xform("L_pinky_C_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_C_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_pinky_D_CTL"):
			if not mc.getAttr("L_pinky_D_CTL.mirrorMode", l=1):
				mc.setAttr("L_pinky_D_CTL.mirrorMode", 0)

			if not mc.getAttr("L_pinky_D_CTL.rotateOrder", l=1):
				mc.setAttr("L_pinky_D_CTL.rotateOrder", 0)

			mc.xform("L_pinky_D_CTL", a=1, t=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_D_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_pinky_D_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("L_hand_CTL"):
			if not mc.getAttr("L_hand_CTL.mirrorMode", l=1):
				mc.setAttr("L_hand_CTL.mirrorMode", 0)

			if not mc.getAttr("L_hand_CTL.rotateOrder", l=1):
				mc.setAttr("L_hand_CTL.rotateOrder", 0)

			mc.xform("L_hand_CTL", a=1, t=[83.089403742899, 110.30409118816799, 0.0])
			mc.xform("L_hand_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("L_hand_CTL", r=1, s=[15.0, 15.0, 15.0])

		if mc.objExists("R_thumb_A_CTL"):
			if not mc.getAttr("R_thumb_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_A_CTL.rotateOrder", 0)

			mc.xform("R_thumb_A_CTL", a=1, t=[0.000238910301817441, -0.0003077826490169855, 0.00012300587958691267])
			mc.xform("R_thumb_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_thumb_A_CTL", r=1, s=[15.000000000000002, 15.000000000000004, 15.000000000000002])

		if mc.objExists("R_thumb_B_CTL"):
			if not mc.getAttr("R_thumb_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_B_CTL.rotateOrder", 0)

			mc.xform("R_thumb_B_CTL", a=1, t=[-3.827254801080926e-05, 3.450642099167567e-05, 2.3047615968607715e-05])
			mc.xform("R_thumb_B_CTL", a=1, ro=[6.361109362927032e-15, 1.5902773407317584e-15, -3.180554681463516e-15])
			mc.xform("R_thumb_B_CTL", r=1, s=[14.999999999999996, 15.000000000000004, 14.999999999999996])

		if mc.objExists("R_thumb_C_CTL"):
			if not mc.getAttr("R_thumb_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_thumb_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_thumb_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_thumb_C_CTL.rotateOrder", 0)

			mc.xform("R_thumb_C_CTL", a=1, t=[-1.5922931908107785e-05, -2.3182525787035502e-05, 4.160203177150379e-05])
			mc.xform("R_thumb_C_CTL", a=1, ro=[-2.067360542951286e-14, 1.590277340731758e-14, -9.541664044390553e-15])
			mc.xform("R_thumb_C_CTL", r=1, s=[15.0, 15.000000000000004, 15.000000000000002])

		if mc.objExists("R_index_A_CTL"):
			if not mc.getAttr("R_index_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_A_CTL.rotateOrder", 0)

			mc.xform("R_index_A_CTL", a=1, t=[0.0003149489605007716, -0.00027218796279271373, -0.0001036942648688921])
			mc.xform("R_index_A_CTL", a=1, ro=[8.74652537402467e-15, 9.144094709207612e-15, -1.90833280887811e-14])
			mc.xform("R_index_A_CTL", r=1, s=[14.999999999999996, 15.0, 15.000000000000007])

		if mc.objExists("R_index_B_CTL"):
			if not mc.getAttr("R_index_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_B_CTL.rotateOrder", 0)

			mc.xform("R_index_B_CTL", a=1, t=[-1.4454881082315296e-05, 6.187569535143211e-05, -1.8679367890683807e-05])
			mc.xform("R_index_B_CTL", a=1, ro=[-7.95138670365879e-16, -3.975693351829395e-16, 2.7586914362813478e-33])
			mc.xform("R_index_B_CTL", r=1, s=[14.999999999999995, 14.999999999999998, 14.999999999999995])

		if mc.objExists("R_index_C_CTL"):
			if not mc.getAttr("R_index_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_C_CTL.rotateOrder", 0)

			mc.xform("R_index_C_CTL", a=1, t=[-1.910017979867007e-05, -1.2253660301553282e-05, 1.0688317175322481e-05])
			mc.xform("R_index_C_CTL", a=1, ro=[-2.385416011097638e-15, -3.975693351829396e-15, 1.2722218725854067e-14])
			mc.xform("R_index_C_CTL", r=1, s=[14.999999999999996, 14.999999999999995, 15.000000000000002])

		if mc.objExists("R_index_D_CTL"):
			if not mc.getAttr("R_index_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_index_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_index_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_index_D_CTL.rotateOrder", 0)

			mc.xform("R_index_D_CTL", a=1, t=[3.832921663615707e-06, 4.439261589794796e-05, -2.2484446539294822e-05])
			mc.xform("R_index_D_CTL", a=1, ro=[1.5902773407317576e-15, -7.951386703658789e-15, 6.361109362927032e-15])
			mc.xform("R_index_D_CTL", r=1, s=[15.0, 14.999999999999996, 15.000000000000004])

		if mc.objExists("R_middle_A_CTL"):
			if not mc.getAttr("R_middle_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_A_CTL.rotateOrder", 0)

			mc.xform("R_middle_A_CTL", a=1, t=[-3.72612388446214e-05, -2.689711584480392e-05, 1.7835104936025914e-05])
			mc.xform("R_middle_A_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_middle_A_CTL", r=1, s=[15.000000000000004, 15.000000000000005, 15.000000000000004])

		if mc.objExists("R_middle_B_CTL"):
			if not mc.getAttr("R_middle_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_B_CTL.rotateOrder", 0)

			mc.xform("R_middle_B_CTL", a=1, t=[-5.169266594862165e-05, -1.5506161489042825e-05, 1.1902530026475233e-05])
			mc.xform("R_middle_B_CTL", a=1, ro=[1.5902773407317584e-15, -1.5902773407317584e-15, -2.2069531490250799e-32])
			mc.xform("R_middle_B_CTL", r=1, s=[14.999999999999998, 14.999999999999998, 14.999999999999996])

		if mc.objExists("R_middle_C_CTL"):
			if not mc.getAttr("R_middle_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_C_CTL.rotateOrder", 0)

			mc.xform("R_middle_C_CTL", a=1, t=[9.230555093608928e-07, 8.670857710058044e-06, -5.762233504569281e-06])
			mc.xform("R_middle_C_CTL", a=1, ro=[-7.951386703658794e-16, 1.9878466759146984e-15, -1.379345718140675e-32])
			mc.xform("R_middle_C_CTL", r=1, s=[15.0, 14.999999999999996, 15.0])

		if mc.objExists("R_middle_D_CTL"):
			if not mc.getAttr("R_middle_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_middle_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_middle_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_middle_D_CTL.rotateOrder", 0)

			mc.xform("R_middle_D_CTL", a=1, t=[2.6281756120738464e-05, -3.4652374438337574e-05, 7.978014062715033e-06])
			mc.xform("R_middle_D_CTL", a=1, ro=[2.3854160110976376e-15, 7.951386703658794e-16, -6.3611093629270335e-15])
			mc.xform("R_middle_D_CTL", r=1, s=[14.999999999999998, 15.000000000000002, 14.999999999999998])

		if mc.objExists("R_ring_A_CTL"):
			if not mc.getAttr("R_ring_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_A_CTL.rotateOrder", 0)

			mc.xform("R_ring_A_CTL", a=1, t=[8.056650639076679e-05, -9.488693748949117e-05, -2.85526883523346e-05])
			mc.xform("R_ring_A_CTL", a=1, ro=[8.827812596100319e-32, -1.5902773407317584e-15, -6.3611093629270335e-15])
			mc.xform("R_ring_A_CTL", r=1, s=[15.000000000000002, 15.000000000000005, 15.000000000000004])

		if mc.objExists("R_ring_B_CTL"):
			if not mc.getAttr("R_ring_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_B_CTL.rotateOrder", 0)

			mc.xform("R_ring_B_CTL", a=1, t=[-1.861925724711e-07, -3.44350522283321e-05, -9.963525796408135e-06])
			mc.xform("R_ring_B_CTL", a=1, ro=[2.5245652784116664e-14, 1.987846675914698e-16, 4.3794226550966417e-32])
			mc.xform("R_ring_B_CTL", r=1, s=[15.000000000000002, 14.999999999999996, 15.0])

		if mc.objExists("R_ring_C_CTL"):
			if not mc.getAttr("R_ring_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_C_CTL.rotateOrder", 0)

			mc.xform("R_ring_C_CTL", a=1, t=[-1.2271224953508408e-05, -4.062919217062699e-05, -4.6367665722968354e-05])
			mc.xform("R_ring_C_CTL", a=1, ro=[-3.975693351829395e-16, -4.4139062980501564e-32, -1.2722218725854064e-14])
			mc.xform("R_ring_C_CTL", r=1, s=[15.0, 15.000000000000004, 14.999999999999998])

		if mc.objExists("R_ring_D_CTL"):
			if not mc.getAttr("R_ring_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_ring_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_ring_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_ring_D_CTL.rotateOrder", 0)

			mc.xform("R_ring_D_CTL", a=1, t=[2.9658530706910824e-06, 1.612568193820607e-05, -3.207789906056746e-05])
			mc.xform("R_ring_D_CTL", a=1, ro=[7.951386703658794e-16, 5.963540027744092e-16, 1.90833280887811e-14])
			mc.xform("R_ring_D_CTL", r=1, s=[15.000000000000002, 15.000000000000009, 15.000000000000004])

		if mc.objExists("R_pinky_A_CTL"):
			if not mc.getAttr("R_pinky_A_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_A_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_A_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_A_CTL.rotateOrder", 0)

			mc.xform("R_pinky_A_CTL", a=1, t=[-0.00034110449490754036, 0.0002523943627892322, 2.8143788252776858e-05])
			mc.xform("R_pinky_A_CTL", a=1, ro=[0.0, -1.987846675914698e-16, 0.0])
			mc.xform("R_pinky_A_CTL", r=1, s=[15.000000000000007, 15.000000000000004, 14.999999999999998])

		if mc.objExists("R_pinky_B_CTL"):
			if not mc.getAttr("R_pinky_B_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_B_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_B_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_B_CTL.rotateOrder", 0)

			mc.xform("R_pinky_B_CTL", a=1, t=[3.899545799157522e-05, 1.2604645860392338e-07, -7.109554804429763e-06])
			mc.xform("R_pinky_B_CTL", a=1, ro=[2.3854160110976374e-14, 5.565970692561156e-15, -6.361109362927032e-15])
			mc.xform("R_pinky_B_CTL", r=1, s=[15.000000000000005, 14.999999999999998, 15.000000000000002])

		if mc.objExists("R_pinky_C_CTL"):
			if not mc.getAttr("R_pinky_C_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_C_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_C_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_C_CTL.rotateOrder", 0)

			mc.xform("R_pinky_C_CTL", a=1, t=[-3.601237268924251e-05, 4.248576061627318e-06, -5.808647618010809e-05])
			mc.xform("R_pinky_C_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_pinky_C_CTL", r=1, s=[14.999999999999998, 14.999999999999996, 14.999999999999998])

		if mc.objExists("R_pinky_D_CTL"):
			if not mc.getAttr("R_pinky_D_CTL.mirrorMode", l=1):
				mc.setAttr("R_pinky_D_CTL.mirrorMode", 0)

			if not mc.getAttr("R_pinky_D_CTL.rotateOrder", l=1):
				mc.setAttr("R_pinky_D_CTL.rotateOrder", 0)

			mc.xform("R_pinky_D_CTL", a=1, t=[-9.83806927479236e-06, 7.712201352205739e-06, -1.850206550457756e-05])
			mc.xform("R_pinky_D_CTL", a=1, ro=[4.770832022195275e-15, -7.951386703658797e-16, 1.2722218725854067e-14])
			mc.xform("R_pinky_D_CTL", r=1, s=[15.000000000000002, 14.999999999999996, 15.000000000000005])

		if mc.objExists("R_hand_CTL"):
			if not mc.getAttr("R_hand_CTL.mirrorMode", l=1):
				mc.setAttr("R_hand_CTL.mirrorMode", 0)

			if not mc.getAttr("R_hand_CTL.rotateOrder", l=1):
				mc.setAttr("R_hand_CTL.rotateOrder", 0)

			mc.xform("R_hand_CTL", a=1, t=[83.08940374289901, 110.30409118816797, -1.350835522064477e-14])
			mc.xform("R_hand_CTL", a=1, ro=[0.0, 0.0, 0.0])
			mc.xform("R_hand_CTL", r=1, s=[15.0, 15.0, 15.0])

		# Apply contro shapes data
		data = {
			"R_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-65.618507, 96.164927, -10.486582], [-65.627729, 96.170345, -10.475578], [-65.618738, 96.163967, -10.464902], [-65.609516, 96.158549, -10.475906], [-65.618507, 96.164927, -10.486582], [-65.624521, 96.155353, -10.476208], [-65.618738, 96.163967, -10.464902], [-65.612723, 96.173543, -10.475276], [-65.627729, 96.170345, -10.475578], [-65.624521, 96.155353, -10.476208], [-65.609516, 96.158549, -10.475906], [-65.612723, 96.173543, -10.475276], [-65.618507, 96.164927, -10.486582], [-65.624521, 96.155353, -10.476208], [-65.0621, 97.0225, -10.4318]]}, {"shapeName": "R_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.921092, 97.579394, -10.427159], [-65.915308, 97.588009, -10.415854], [-65.921323, 97.578434, -10.40548], [-65.927107, 97.569818, -10.416785], [-65.921092, 97.579394, -10.427159], [-65.930313, 97.584811, -10.416156], [-65.921323, 97.578434, -10.40548], [-65.912101, 97.573016, -10.416484], [-65.915308, 97.588009, -10.415854], [-65.930313, 97.584811, -10.416156], [-65.927107, 97.569818, -10.416785], [-65.912101, 97.573016, -10.416484], [-65.921092, 97.579394, -10.427159], [-65.930313, 97.584811, -10.416156], [-65.0621, 97.0225, -10.4318]]}, {"shapeName": "R_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-65.082115, 96.983104, -9.409026], [-65.067109, 96.986301, -9.408724], [-65.063902, 96.971308, -9.409354], [-65.078907, 96.96811, -9.409656], [-65.082115, 96.983104, -9.409026], [-65.073124, 96.976726, -9.398351], [-65.063902, 96.971308, -9.409354], [-65.072893, 96.977686, -9.42003], [-65.067109, 96.986301, -9.408724], [-65.073124, 96.976726, -9.398351], [-65.078907, 96.96811, -9.409656], [-65.072893, 96.977686, -9.42003], [-65.082115, 96.983104, -9.409026], [-65.073124, 96.976726, -9.398351], [-65.0621, 97.0225, -10.4318]]}]},
			"L_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.924534, 92.208765, -10.685612], [67.934798, 92.212117, -10.674707], [67.924753, 92.207818, -10.663931], [67.914489, 92.204466, -10.674836], [67.924534, 92.208765, -10.685612], [67.928468, 92.198149, -10.675253], [67.924753, 92.207818, -10.663931], [67.920819, 92.218435, -10.67429], [67.934798, 92.212117, -10.674707], [67.928468, 92.198149, -10.675253], [67.914489, 92.204466, -10.674836], [67.920819, 92.218435, -10.67429], [67.924534, 92.208765, -10.685612], [67.928468, 92.198149, -10.675253], [67.563857, 93.165199, -10.629346]]}, {"shapeName": "L_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[68.521678, 93.526555, -10.634083], [68.517963, 93.536224, -10.622762], [68.521896, 93.525608, -10.612403], [68.525611, 93.515938, -10.623725], [68.521678, 93.526555, -10.634083], [68.53194, 93.529906, -10.623178], [68.521896, 93.525608, -10.612403], [68.511633, 93.522256, -10.623308], [68.517963, 93.536224, -10.622762], [68.53194, 93.529906, -10.623178], [68.525611, 93.515938, -10.623725], [68.511633, 93.522256, -10.623308], [68.521678, 93.526555, -10.634083], [68.53194, 93.529906, -10.623178], [67.563857, 93.165199, -10.629346]]}, {"shapeName": "L_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[67.584321, 93.124365, -9.606637], [67.570342, 93.130683, -9.60622], [67.564012, 93.116715, -9.606766], [67.577991, 93.110397, -9.607183], [67.584321, 93.124365, -9.606637], [67.574276, 93.120067, -9.595862], [67.564012, 93.116715, -9.606766], [67.574057, 93.121013, -9.617542], [67.570342, 93.130683, -9.60622], [67.574276, 93.120067, -9.595862], [67.577991, 93.110397, -9.607183], [67.574057, 93.121013, -9.617542], [67.584321, 93.124365, -9.606637], [67.574276, 93.120067, -9.595862], [67.563857, 93.165199, -10.629346]]}]},
			"L_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_A_CTLShape", "degree": 3, "form": 2, "points": [[60.448684, 99.890431, -10.388865], [62.011469, 100.974533, -10.545055], [62.812949, 102.346865, -9.488502], [62.383625, 103.203532, -7.838117], [60.974992, 103.042714, -6.560674], [59.412207, 101.958612, -6.404484], [58.610727, 100.586281, -7.461037], [59.040051, 99.729613, -9.111422]]}]},
			"L_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.427112, 93.760792, -14.092988], [66.438836, 93.761679, -14.083126], [66.430299, 93.754841, -14.072363], [66.418575, 93.753954, -14.082225], [66.427112, 93.760792, -14.092988], [66.432252, 93.748123, -14.08602], [66.430299, 93.754841, -14.072363], [66.425158, 93.767511, -14.079331], [66.438836, 93.761679, -14.083126], [66.432252, 93.748123, -14.08602], [66.418575, 93.753954, -14.082225], [66.425158, 93.767511, -14.079331], [66.427112, 93.760792, -14.092988], [66.432252, 93.748123, -14.08602], [66.094084, 94.67235, -13.767144]]}, {"shapeName": "L_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.048178, 95.039679, -13.819988], [67.046225, 95.046398, -13.806331], [67.051365, 95.033729, -13.799362], [67.053319, 95.02701, -13.81302], [67.048178, 95.039679, -13.819988], [67.059901, 95.040566, -13.810126], [67.051365, 95.033729, -13.799362], [67.039641, 95.032842, -13.809224], [67.046225, 95.046398, -13.806331], [67.059901, 95.040566, -13.810126], [67.053319, 95.02701, -13.81302], [67.039641, 95.032842, -13.809224], [67.048178, 95.039679, -13.819988], [67.059901, 95.040566, -13.810126], [66.094084, 94.67235, -13.767144]]}, {"shapeName": "L_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[66.254517, 94.395538, -12.794696], [66.24084, 94.40137, -12.7909], [66.234257, 94.387814, -12.793794], [66.247934, 94.381982, -12.797589], [66.254517, 94.395538, -12.794696], [66.24598, 94.388701, -12.783933], [66.234257, 94.387814, -12.793794], [66.242794, 94.394651, -12.804558], [66.24084, 94.40137, -12.7909], [66.24598, 94.388701, -12.783933], [66.247934, 94.381982, -12.797589], [66.242794, 94.394651, -12.804558], [66.254517, 94.395538, -12.794696], [66.24598, 94.388701, -12.783933], [66.094084, 94.67235, -13.767144]]}]},
			"world_A_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_A_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -51.993], [23.0985, 0.0, -28.872], [17.316, 0.0, -28.872], [17.316, 0.0, -17.3115], [28.8765, 0.0, -17.3115], [28.8765, 0.0, -23.094], [51.993, 0.0, 0.0], [28.872, 0.0, 23.0985], [28.872, 0.0, 17.316], [17.3115, 0.0, 17.316], [17.3115, 0.0, 28.8765], [23.094, 0.0, 28.8765], [0.0, 0.0, 51.993], [-23.0985, 0.0, 28.872], [-17.316, 0.0, 28.872], [-17.316, 0.0, 17.3115], [-28.8765, 0.0, 17.3115], [-28.8765, 0.0, 23.094], [-51.993, 0.0, 0.0], [-28.872, 0.0, -23.0985], [-28.872, 0.0, -17.316], [-17.3115, 0.0, -17.316], [-17.3115, 0.0, -28.8765], [-23.094, 0.0, -28.8765], [0.0, 0.0, -51.993], [4.527, 0.063, -47.547], [4.131, 0.0, -47.124], [4.131, 0.0, -45.396], [3.771, 0.0, -45.396], [3.7935, 0.0, -47.1375], [3.537, 0.0, -47.007], [3.546, 0.0, -46.251], [3.1815, 0.0, -46.251], [3.1815, 0.0, -47.007], [2.9565, 0.0, -47.1375], [2.9565, 0.0, -45.369], [2.592, 0.0, -45.369], [2.592, 0.0, -47.1825], [2.8845, 0.0, -47.475], [3.3345, 0.0, -47.25], [3.8295, 0.0, -47.475], [4.131, 0.0, -47.133], [3.8295, 0.0, -47.475], [3.339, 0.0, -47.2545], [2.8845, 0.0, -47.4705], [2.007, 0.0, -47.475], [2.304, 0.0, -47.1825], [2.304, 0.0, -45.666], [2.007, 0.0, -45.369], [1.0575, 0.0, -45.369], [0.765, 0.0, -45.666], [0.765, 0.0, -47.1825], [1.0575, 0.0, -47.475], [2.007, 0.0, -47.475], [1.8945, 0.0, -47.1375], [1.9395, 0.0, -45.7425], [1.125, 0.0, -45.7515], [1.1295, 0.0, -47.1375], [1.899, 0.0, -47.1465], [2.007, 0.0, -47.475], [1.0575, 0.0, -47.475], [0.45, 0.0, -47.475], [0.4725, 0.0, -45.369], [-0.5535, 0.0, -45.369], [-0.8505, 0.0, -45.666], [-0.8505, 0.0, -46.3005], [-0.549, 0.0, -46.593], [-0.531, 0.0, -46.6155], [-1.1205, 0.0, -47.466], [-1.1205, 0.0, -47.475], [-0.6975, 0.0, -47.475], [-0.108, 0.0, -46.62], [0.1125, 0.0, -46.62], [0.1125, 0.0, -45.72], [-0.4545, 0.0, -45.72], [-0.459, 0.0, -46.2555], [0.1125, 0.0, -46.2555], [0.1125, 0.0, -47.475], [0.45, 0.0, -47.475], [-2.8935, 0.0, -47.475], [-2.8935, 0.0, -47.1375], [-1.7145, 0.0, -47.133], [-1.7145, 0.0, -45.369], [-1.35, 0.0, -45.369], [-1.35, 0.0, -47.475], [-4.428, 0.0, -47.475], [-4.698, 0.0, -47.1825], [-4.7205, 0.0, -45.666], [-4.428, 0.0, -45.369], [-3.1815, 0.0, -45.369], [-3.1815, 0.0, -47.475], [-3.5505, 0.0, -47.1375], [-3.5415, 0.0, -45.711], [-4.311, 0.0, -45.711], [-4.302, 0.0, -47.1285], [-3.537, 0.0, -47.1465], [-3.1725, 0.0, -47.475]]}]},
			"L_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_C_CTLShape", "degree": 3, "form": 2, "points": [[65.896204, 92.620551, -12.401216], [67.538746, 93.273979, -13.120282], [69.195998, 93.863686, -12.380193], [69.897162, 94.044228, -10.614481], [69.23151, 93.709848, -8.857476], [67.588968, 93.056419, -8.13841], [65.931716, 92.466712, -8.878499], [65.230552, 92.28617, -10.644211]]}]},
			"L_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.767251, 89.821742, -2.155873], [66.771318, 89.824205, -2.141282], [66.756526, 89.825272, -2.13734], [66.752459, 89.822809, -2.15193], [66.767251, 89.821742, -2.155873], [66.761618, 89.812824, -2.144728], [66.756526, 89.825272, -2.13734], [66.762158, 89.83419, -2.148485], [66.771318, 89.824205, -2.141282], [66.761618, 89.812824, -2.144728], [66.752459, 89.822809, -2.15193], [66.762158, 89.83419, -2.148485], [66.767251, 89.821742, -2.155873], [66.761618, 89.812824, -2.144728], [66.78735, 90.831395, -2.323847]]}, {"shapeName": "L_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.682264, 90.895482, -1.830855], [67.677171, 90.907931, -1.823467], [67.671539, 90.899012, -1.812322], [67.676631, 90.886564, -1.81971], [67.682264, 90.895482, -1.830855], [67.68633, 90.897945, -1.816265], [67.671539, 90.899012, -1.812322], [67.667472, 90.896549, -1.826912], [67.677171, 90.907931, -1.823467], [67.68633, 90.897945, -1.816265], [67.676631, 90.886564, -1.81971], [67.667472, 90.896549, -1.826912], [67.682264, 90.895482, -1.830855], [67.68633, 90.897945, -1.816265], [66.78735, 90.831395, -2.323847]]}, {"shapeName": "L_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[66.290862, 90.998605, -1.444323], [66.281703, 91.00859, -1.451526], [66.272004, 90.997209, -1.454971], [66.281163, 90.987223, -1.447769], [66.290862, 90.998605, -1.444323], [66.276071, 90.999672, -1.440382], [66.272004, 90.997209, -1.454971], [66.286796, 90.996142, -1.458914], [66.281703, 91.00859, -1.451526], [66.276071, 90.999672, -1.440382], [66.281163, 90.987223, -1.447769], [66.286796, 90.996142, -1.458914], [66.290862, 90.998605, -1.444323], [66.276071, 90.999672, -1.440382], [66.78735, 90.831395, -2.323847]]}]},
			"R_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_D_CTLShape", "degree": 3, "form": 2, "points": [[-66.126593, 90.431183, -4.694599], [-68.019651, 90.425811, -4.453204], [-69.190845, 90.658024, -2.964462], [-68.954101, 90.991796, -1.100456], [-67.448106, 91.231608, 0.046905], [-65.555048, 91.23698, -0.19449], [-64.383855, 91.004767, -1.683231], [-64.620598, 90.670995, -3.547237]]}]},
			"L_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.52269, 88.885946, -6.167311], [68.530925, 88.888837, -6.154688], [68.518223, 88.887729, -6.146148], [68.509989, 88.884838, -6.158771], [68.52269, 88.885946, -6.167311], [68.522238, 88.87621, -6.155458], [68.518223, 88.887729, -6.146148], [68.518675, 88.897465, -6.158001], [68.530925, 88.888837, -6.154688], [68.522238, 88.87621, -6.155458], [68.509989, 88.884838, -6.158771], [68.518675, 88.897465, -6.158001], [68.52269, 88.885946, -6.167311], [68.522238, 88.87621, -6.155458], [68.352369, 89.889469, -6.276646]]}, {"shapeName": "L_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[69.342151, 90.077168, -6.094655], [69.338136, 90.088687, -6.085345], [69.337684, 90.078951, -6.073492], [69.341699, 90.067431, -6.082802], [69.342151, 90.077168, -6.094655], [69.350385, 90.080058, -6.082032], [69.337684, 90.078951, -6.073492], [69.329449, 90.07606, -6.086115], [69.338136, 90.088687, -6.085345], [69.350385, 90.080058, -6.082032], [69.341699, 90.067431, -6.082802], [69.329449, 90.07606, -6.086115], [69.342151, 90.077168, -6.094655], [69.350385, 90.080058, -6.082032], [68.352369, 89.889469, -6.276646]]}, {"shapeName": "L_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[68.152131, 89.975532, -5.276387], [68.139881, 89.984161, -5.279699], [68.131195, 89.971534, -5.280469], [68.143445, 89.962905, -5.277157], [68.152131, 89.975532, -5.276387], [68.13943, 89.974424, -5.267848], [68.131195, 89.971534, -5.280469], [68.143896, 89.972642, -5.289009], [68.139881, 89.984161, -5.279699], [68.13943, 89.974424, -5.267848], [68.143445, 89.962905, -5.277157], [68.143896, 89.972642, -5.289009], [68.152131, 89.975532, -5.276387], [68.13943, 89.974424, -5.267848], [68.352369, 89.889469, -6.276646]]}]},
			"world_C_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_C_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -40.439], [17.9655, 0.0, -22.456], [13.468, 0.0, -22.456], [13.468, 0.0, -13.4645], [22.4595, 0.0, -13.4645], [22.4595, 0.0, -17.962], [40.439, 0.0, 0.0], [22.456, 0.0, 17.9655], [22.456, 0.0, 13.468], [13.4645, 0.0, 13.468], [13.4645, 0.0, 22.4595], [17.962, 0.0, 22.4595], [0.0, 0.0, 40.439], [-17.9655, 0.0, 22.456], [-13.468, 0.0, 22.456], [-13.468, 0.0, 13.4645], [-22.4595, 0.0, 13.4645], [-22.4595, 0.0, 17.962], [-40.439, 0.0, 0.0], [-22.456, 0.0, -17.9655], [-22.456, 0.0, -13.468], [-13.4645, 0.0, -13.468], [-13.4645, 0.0, -22.4595], [-17.962, 0.0, -22.4595], [0.0, 0.0, -40.439], [3.521, 0.049, -36.981], [3.213, 0.0, -36.652], [3.213, 0.0, -35.308], [2.933, 0.0, -35.308], [2.9505, 0.0, -36.6625], [2.751, 0.0, -36.561], [2.758, 0.0, -35.973], [2.4745, 0.0, -35.973], [2.4745, 0.0, -36.561], [2.2995, 0.0, -36.6625], [2.2995, 0.0, -35.287], [2.016, 0.0, -35.287], [2.016, 0.0, -36.6975], [2.2435, 0.0, -36.925], [2.5935, 0.0, -36.75], [2.9785, 0.0, -36.925], [3.213, 0.0, -36.659], [2.9785, 0.0, -36.925], [2.597, 0.0, -36.7535], [2.2435, 0.0, -36.9215], [1.561, 0.0, -36.925], [1.792, 0.0, -36.6975], [1.792, 0.0, -35.518], [1.561, 0.0, -35.287], [0.8225, 0.0, -35.287], [0.595, 0.0, -35.518], [0.595, 0.0, -36.6975], [0.8225, 0.0, -36.925], [1.561, 0.0, -36.925], [1.4735, 0.0, -36.6625], [1.5085, 0.0, -35.5775], [0.875, 0.0, -35.5845], [0.8785, 0.0, -36.6625], [1.477, 0.0, -36.6695], [1.561, 0.0, -36.925], [0.8225, 0.0, -36.925], [0.35, 0.0, -36.925], [0.3675, 0.0, -35.287], [-0.4305, 0.0, -35.287], [-0.6615, 0.0, -35.518], [-0.6615, 0.0, -36.0115], [-0.427, 0.0, -36.239], [-0.413, 0.0, -36.2565], [-0.8715, 0.0, -36.918], [-0.8715, 0.0, -36.925], [-0.5425, 0.0, -36.925], [-0.084, 0.0, -36.26], [0.0875, 0.0, -36.26], [0.0875, 0.0, -35.56], [-0.3535, 0.0, -35.56], [-0.357, 0.0, -35.9765], [0.0875, 0.0, -35.9765], [0.0875, 0.0, -36.925], [0.35, 0.0, -36.925], [-2.2505, 0.0, -36.925], [-2.2505, 0.0, -36.6625], [-1.3335, 0.0, -36.659], [-1.3335, 0.0, -35.287], [-1.05, 0.0, -35.287], [-1.05, 0.0, -36.925], [-3.444, 0.0, -36.925], [-3.654, 0.0, -36.6975], [-3.6715, 0.0, -35.518], [-3.444, 0.0, -35.287], [-2.4745, 0.0, -35.287], [-2.4745, 0.0, -36.925], [-2.7615, 0.0, -36.6625], [-2.7545, 0.0, -35.553], [-3.353, 0.0, -35.553], [-3.346, 0.0, -36.6555], [-2.751, 0.0, -36.6695], [-2.4675, 0.0, -36.925]]}]},
			"R_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_D_CTLShape", "degree": 3, "form": 2, "points": [[-66.870583, 90.313994, -12.518867], [-68.628448, 90.400411, -13.25671], [-70.394905, 90.429589, -12.535082], [-71.135186, 90.384437, -10.776699], [-70.415649, 90.291403, -9.011598], [-68.657784, 90.204987, -8.273754], [-66.891327, 90.175809, -8.995382], [-66.151046, 90.220961, -10.753766]]}]},
			"R_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-62.05289, 100.240471, -11.139676], [-62.059447, 100.248978, -11.128716], [-62.050211, 100.242608, -11.118246], [-62.043654, 100.234101, -11.129206], [-62.05289, 100.240471, -11.139676], [-62.058871, 100.233713, -11.127266], [-62.050211, 100.242608, -11.118246], [-62.04423, 100.249368, -11.130657], [-62.059447, 100.248978, -11.128716], [-62.058871, 100.233713, -11.127266], [-62.043654, 100.234101, -11.129206], [-62.04423, 100.249368, -11.130657], [-62.05289, 100.240471, -11.139676], [-62.058871, 100.233713, -11.127266], [-61.3609, 100.98, -11.2889]]}, {"shapeName": "R_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-62.107185, 101.680659, -11.27648], [-62.098525, 101.689555, -11.26746], [-62.104507, 101.682796, -11.25505], [-62.113167, 101.6739, -11.26407], [-62.107185, 101.680659, -11.27648], [-62.113742, 101.689165, -11.26552], [-62.104507, 101.682796, -11.25505], [-62.09795, 101.674289, -11.26601], [-62.098525, 101.689555, -11.26746], [-62.113742, 101.689165, -11.26552], [-62.113167, 101.6739, -11.26407], [-62.09795, 101.674289, -11.26601], [-62.107185, 101.680659, -11.27648], [-62.113742, 101.689165, -11.26552], [-61.3609, 100.98, -11.2889]]}, {"shapeName": "R_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.242469, 101.08822, -10.27782], [-61.227252, 101.08861, -10.27976], [-61.226676, 101.073344, -10.27831], [-61.241894, 101.072954, -10.27637], [-61.242469, 101.08822, -10.27782], [-61.233234, 101.08185, -10.267351], [-61.226676, 101.073344, -10.27831], [-61.235912, 101.079714, -10.28878], [-61.227252, 101.08861, -10.27976], [-61.233234, 101.08185, -10.267351], [-61.241894, 101.072954, -10.27637], [-61.235912, 101.079714, -10.28878], [-61.242469, 101.08822, -10.27782], [-61.233234, 101.08185, -10.267351], [-61.3609, 100.98, -11.2889]]}]},
			"R_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-58.360896, 96.074423, -2.847783], [-58.368325, 96.084142, -2.838518], [-58.381683, 96.079865, -2.844744], [-58.374254, 96.070146, -2.854009], [-58.360896, 96.074423, -2.847783], [-58.370327, 96.084977, -2.853709], [-58.381683, 96.079865, -2.844744], [-58.372252, 96.06931, -2.838817], [-58.368325, 96.084142, -2.838518], [-58.370327, 96.084977, -2.853709], [-58.374254, 96.070146, -2.854009], [-58.372252, 96.06931, -2.838817], [-58.360896, 96.074423, -2.847783], [-58.370327, 96.084977, -2.853709], [-58.4621, 95.3381, -2.14379]]}, {"shapeName": "R_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-58.172055, 95.995537, -1.414632], [-58.183411, 95.990424, -1.405667], [-58.192842, 96.00098, -1.411594], [-58.181486, 96.006092, -1.420559], [-58.172055, 95.995537, -1.414632], [-58.179484, 96.005255, -1.405368], [-58.192842, 96.00098, -1.411594], [-58.185413, 95.991261, -1.420858], [-58.183411, 95.990424, -1.405667], [-58.179484, 96.005255, -1.405368], [-58.181486, 96.006092, -1.420559], [-58.185413, 95.991261, -1.420858], [-58.172055, 95.995537, -1.414632], [-58.179484, 96.005255, -1.405368], [-58.4621, 95.3381, -2.14379]]}, {"shapeName": "R_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-59.439671, 95.601821, -1.992712], [-59.443598, 95.58699, -1.993011], [-59.4456, 95.587826, -2.008202], [-59.441673, 95.602658, -2.007904], [-59.439671, 95.601821, -1.992712], [-59.453029, 95.597545, -1.998938], [-59.4456, 95.587826, -2.008202], [-59.432242, 95.592102, -2.001977], [-59.443598, 95.58699, -1.993011], [-59.453029, 95.597545, -1.998938], [-59.441673, 95.602658, -2.007904], [-59.432242, 95.592102, -2.001977], [-59.439671, 95.601821, -1.992712], [-59.453029, 95.597545, -1.998938], [-58.4621, 95.3381, -2.14379]]}]},
			"L_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[65.635372, 95.863556, -7.597983], [65.641884, 95.870551, -7.585976], [65.630227, 95.866084, -7.577052], [65.623715, 95.859089, -7.589058], [65.635372, 95.863556, -7.597983], [65.638147, 95.855694, -7.5851], [65.630227, 95.866084, -7.577052], [65.627451, 95.873947, -7.589934], [65.641884, 95.870551, -7.585976], [65.638147, 95.855694, -7.5851], [65.623715, 95.859089, -7.589058], [65.627451, 95.873947, -7.589934], [65.635372, 95.863556, -7.597983], [65.638147, 95.855694, -7.5851], [65.128259, 96.725837, -7.815532]]}, {"shapeName": "L_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.987829, 97.265249, -7.680652], [65.979909, 97.27564, -7.672604], [65.982684, 97.267777, -7.659721], [65.990605, 97.257386, -7.66777], [65.987829, 97.265249, -7.680652], [65.99434, 97.272244, -7.668646], [65.982684, 97.267777, -7.659721], [65.976173, 97.260782, -7.671728], [65.979909, 97.27564, -7.672604], [65.99434, 97.272244, -7.668646], [65.990605, 97.257386, -7.66777], [65.976173, 97.260782, -7.671728], [65.987829, 97.265249, -7.680652], [65.99434, 97.272244, -7.668646], [65.128259, 96.725837, -7.815532]]}, {"shapeName": "L_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[64.89466, 96.850821, -6.826679], [64.880228, 96.854217, -6.830637], [64.876492, 96.839358, -6.82976], [64.890924, 96.835963, -6.825803], [64.89466, 96.850821, -6.826679], [64.883004, 96.846354, -6.817755], [64.876492, 96.839358, -6.82976], [64.888148, 96.843826, -6.838685], [64.880228, 96.854217, -6.830637], [64.883004, 96.846354, -6.817755], [64.890924, 96.835963, -6.825803], [64.888148, 96.843826, -6.838685], [64.89466, 96.850821, -6.826679], [64.883004, 96.846354, -6.817755], [65.128259, 96.725837, -7.815532]]}]},
			"R_ring_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.924577, 92.208766, -10.685566], [-67.934841, 92.212118, -10.674661], [-67.924796, 92.207819, -10.663885], [-67.914532, 92.204467, -10.67479], [-67.924577, 92.208766, -10.685566], [-67.928511, 92.19815, -10.675207], [-67.924796, 92.207819, -10.663885], [-67.920862, 92.218436, -10.674244], [-67.934841, 92.212118, -10.674661], [-67.928511, 92.19815, -10.675207], [-67.914532, 92.204467, -10.67479], [-67.920862, 92.218436, -10.674244], [-67.924577, 92.208766, -10.685566], [-67.928511, 92.19815, -10.675207], [-67.5639, 93.1652, -10.6293]]}, {"shapeName": "R_ring_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-68.521721, 93.526556, -10.634037], [-68.518006, 93.536225, -10.622716], [-68.521939, 93.525609, -10.612357], [-68.525654, 93.515939, -10.623679], [-68.521721, 93.526556, -10.634037], [-68.531983, 93.529907, -10.623132], [-68.521939, 93.525609, -10.612357], [-68.511676, 93.522257, -10.623262], [-68.518006, 93.536225, -10.622716], [-68.531983, 93.529907, -10.623132], [-68.525654, 93.515939, -10.623679], [-68.511676, 93.522257, -10.623262], [-68.521721, 93.526556, -10.634037], [-68.531983, 93.529907, -10.623132], [-67.5639, 93.1652, -10.6293]]}, {"shapeName": "R_ring_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-67.584364, 93.124366, -9.606591], [-67.570385, 93.130684, -9.606174], [-67.564055, 93.116716, -9.60672], [-67.578034, 93.110398, -9.607137], [-67.584364, 93.124366, -9.606591], [-67.574319, 93.120068, -9.595816], [-67.564055, 93.116716, -9.60672], [-67.5741, 93.121014, -9.617496], [-67.570385, 93.130684, -9.606174], [-67.574319, 93.120068, -9.595816], [-67.578034, 93.110398, -9.607137], [-67.5741, 93.121014, -9.617496], [-67.584364, 93.124366, -9.606591], [-67.574319, 93.120068, -9.595816], [-67.5639, 93.1652, -10.6293]]}]},
			"L_ring_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[65.618478, 96.164909, -10.486592], [65.6277, 96.170327, -10.475588], [65.618709, 96.163949, -10.464912], [65.609487, 96.158531, -10.475916], [65.618478, 96.164909, -10.486592], [65.624492, 96.155335, -10.476218], [65.618709, 96.163949, -10.464912], [65.612694, 96.173525, -10.475286], [65.6277, 96.170327, -10.475588], [65.624492, 96.155335, -10.476218], [65.609487, 96.158531, -10.475916], [65.612694, 96.173525, -10.475286], [65.618478, 96.164909, -10.486592], [65.624492, 96.155335, -10.476218], [65.062071, 97.022482, -10.43181]]}, {"shapeName": "L_ring_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.921063, 97.579376, -10.427169], [65.915279, 97.587991, -10.415864], [65.921294, 97.578416, -10.40549], [65.927078, 97.5698, -10.416795], [65.921063, 97.579376, -10.427169], [65.930284, 97.584793, -10.416166], [65.921294, 97.578416, -10.40549], [65.912072, 97.572998, -10.416494], [65.915279, 97.587991, -10.415864], [65.930284, 97.584793, -10.416166], [65.927078, 97.5698, -10.416795], [65.912072, 97.572998, -10.416494], [65.921063, 97.579376, -10.427169], [65.930284, 97.584793, -10.416166], [65.062071, 97.022482, -10.43181]]}, {"shapeName": "L_ring_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.082086, 96.983086, -9.409036], [65.06708, 96.986283, -9.408734], [65.063873, 96.97129, -9.409364], [65.078878, 96.968092, -9.409666], [65.082086, 96.983086, -9.409036], [65.073095, 96.976708, -9.398361], [65.063873, 96.97129, -9.409364], [65.072864, 96.977668, -9.42004], [65.06708, 96.986283, -9.408734], [65.073095, 96.976708, -9.398361], [65.078878, 96.968092, -9.409666], [65.072864, 96.977668, -9.42004], [65.082086, 96.983086, -9.409036], [65.073095, 96.976708, -9.398361], [65.062071, 97.022482, -10.43181]]}]},
			"R_middle_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.522721, 88.885977, -6.167315], [-68.530956, 88.888868, -6.154692], [-68.518254, 88.88776, -6.146152], [-68.51002, 88.884869, -6.158775], [-68.522721, 88.885977, -6.167315], [-68.522269, 88.876241, -6.155462], [-68.518254, 88.88776, -6.146152], [-68.518706, 88.897496, -6.158005], [-68.530956, 88.888868, -6.154692], [-68.522269, 88.876241, -6.155462], [-68.51002, 88.884869, -6.158775], [-68.518706, 88.897496, -6.158005], [-68.522721, 88.885977, -6.167315], [-68.522269, 88.876241, -6.155462], [-68.3524, 89.8895, -6.27665]]}, {"shapeName": "R_middle_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-69.342182, 90.077199, -6.094659], [-69.338167, 90.088718, -6.085349], [-69.337715, 90.078982, -6.073496], [-69.34173, 90.067462, -6.082806], [-69.342182, 90.077199, -6.094659], [-69.350416, 90.080089, -6.082036], [-69.337715, 90.078982, -6.073496], [-69.32948, 90.076091, -6.086119], [-69.338167, 90.088718, -6.085349], [-69.350416, 90.080089, -6.082036], [-69.34173, 90.067462, -6.082806], [-69.32948, 90.076091, -6.086119], [-69.342182, 90.077199, -6.094659], [-69.350416, 90.080089, -6.082036], [-68.3524, 89.8895, -6.27665]]}, {"shapeName": "R_middle_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-68.152162, 89.975563, -5.276391], [-68.139912, 89.984192, -5.279703], [-68.131226, 89.971565, -5.280473], [-68.143476, 89.962936, -5.277161], [-68.152162, 89.975563, -5.276391], [-68.139461, 89.974455, -5.267852], [-68.131226, 89.971565, -5.280473], [-68.143927, 89.972673, -5.289013], [-68.139912, 89.984192, -5.279703], [-68.139461, 89.974455, -5.267852], [-68.143476, 89.962936, -5.277161], [-68.143927, 89.972673, -5.289013], [-68.152162, 89.975563, -5.276391], [-68.139461, 89.974455, -5.267852], [-68.3524, 89.8895, -6.27665]]}]},
			"R_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_A_CTLShape", "degree": 3, "form": 2, "points": [[-60.295406, 99.597666, -13.069783], [-61.668594, 100.734391, -13.751088], [-62.861533, 102.014917, -12.99009], [-63.175414, 102.689128, -11.232566], [-62.426372, 102.362082, -9.508053], [-61.053184, 101.225357, -8.826748], [-59.860244, 99.944831, -9.587746], [-59.546364, 99.27062, -11.345269]]}]},
			"L_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_D_CTLShape", "degree": 3, "form": 2, "points": [[67.01437, 89.419859, -8.327611], [68.865603, 89.684707, -8.708083], [70.416192, 90.069501, -7.664255], [70.757819, 90.348834, -5.807582], [69.690369, 90.359078, -4.22568], [67.839135, 90.09423, -3.845208], [66.288547, 89.709436, -4.889037], [65.94692, 89.430103, -6.745709]]}]},
			"L_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_B_CTLShape", "degree": 3, "form": 2, "points": [[64.070188, 95.589202, -9.766374], [65.71938, 96.435363, -10.220408], [67.022302, 97.451678, -9.2657], [67.215717, 98.042805, -7.461503], [66.186329, 97.862471, -5.864691], [64.537137, 97.016311, -5.410657], [63.234216, 95.999995, -6.365364], [63.0408, 95.408868, -8.169561]]}]},
			"R_middle_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-65.635413, 95.863519, -7.597981], [-65.641925, 95.870514, -7.585974], [-65.630268, 95.866047, -7.57705], [-65.623756, 95.859052, -7.589056], [-65.635413, 95.863519, -7.597981], [-65.638188, 95.855657, -7.585098], [-65.630268, 95.866047, -7.57705], [-65.627492, 95.87391, -7.589932], [-65.641925, 95.870514, -7.585974], [-65.638188, 95.855657, -7.585098], [-65.623756, 95.859052, -7.589056], [-65.627492, 95.87391, -7.589932], [-65.635413, 95.863519, -7.597981], [-65.638188, 95.855657, -7.585098], [-65.1283, 96.7258, -7.81553]]}, {"shapeName": "R_middle_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.98787, 97.265212, -7.68065], [-65.97995, 97.275603, -7.672602], [-65.982725, 97.26774, -7.659719], [-65.990646, 97.257349, -7.667768], [-65.98787, 97.265212, -7.68065], [-65.994381, 97.272207, -7.668644], [-65.982725, 97.26774, -7.659719], [-65.976214, 97.260745, -7.671726], [-65.97995, 97.275603, -7.672602], [-65.994381, 97.272207, -7.668644], [-65.990646, 97.257349, -7.667768], [-65.976214, 97.260745, -7.671726], [-65.98787, 97.265212, -7.68065], [-65.994381, 97.272207, -7.668644], [-65.1283, 96.7258, -7.81553]]}, {"shapeName": "R_middle_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-64.894701, 96.850784, -6.826677], [-64.880269, 96.85418, -6.830635], [-64.876533, 96.839321, -6.829758], [-64.890965, 96.835926, -6.825801], [-64.894701, 96.850784, -6.826677], [-64.883045, 96.846317, -6.817753], [-64.876533, 96.839321, -6.829758], [-64.888189, 96.843789, -6.838683], [-64.880269, 96.85418, -6.830635], [-64.883045, 96.846317, -6.817753], [-64.890965, 96.835926, -6.825801], [-64.888189, 96.843789, -6.838683], [-64.894701, 96.850784, -6.826677], [-64.883045, 96.846317, -6.817753], [-65.1283, 96.7258, -7.81553]]}]},
			"R_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-57.807666, 100.742936, -7.270901], [-57.794176, 100.748635, -7.266316], [-57.78687, 100.737655, -7.274161], [-57.80036, 100.731956, -7.278747], [-57.807666, 100.742936, -7.270901], [-57.797528, 100.733876, -7.263788], [-57.78687, 100.737655, -7.274161], [-57.797009, 100.746716, -7.281275], [-57.794176, 100.748635, -7.266316], [-57.797528, 100.733876, -7.263788], [-57.80036, 100.731956, -7.278747], [-57.797009, 100.746716, -7.281275], [-57.807666, 100.742936, -7.270901], [-57.797528, 100.733876, -7.263788], [-57.7728, 101.346, -8.09741]]}, {"shapeName": "R_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-57.491495, 102.135398, -7.509415], [-57.480838, 102.139178, -7.519789], [-57.470699, 102.130118, -7.512675], [-57.481357, 102.126337, -7.502301], [-57.491495, 102.135398, -7.509415], [-57.478006, 102.141097, -7.50483], [-57.470699, 102.130118, -7.512675], [-57.484189, 102.124418, -7.51726], [-57.480838, 102.139178, -7.519789], [-57.478006, 102.141097, -7.50483], [-57.481357, 102.126337, -7.502301], [-57.484189, 102.124418, -7.51726], [-57.491495, 102.135398, -7.509415], [-57.478006, 102.141097, -7.50483], [-57.7728, 101.346, -8.09741]]}, {"shapeName": "R_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-56.788783, 101.105269, -8.244989], [-56.791615, 101.10335, -8.259948], [-56.794967, 101.08859, -8.25742], [-56.792134, 101.090509, -8.242461], [-56.788783, 101.105269, -8.244989], [-56.781478, 101.094289, -8.252834], [-56.794967, 101.08859, -8.25742], [-56.802273, 101.099569, -8.249574], [-56.791615, 101.10335, -8.259948], [-56.781478, 101.094289, -8.252834], [-56.792134, 101.090509, -8.242461], [-56.802273, 101.099569, -8.249574], [-56.788783, 101.105269, -8.244989], [-56.781478, 101.094289, -8.252834], [-57.7728, 101.346, -8.09741]]}]},
			"C_world_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_world_PIV_CTLShape", "degree": 1, "form": 0, "points": [[5.118355, 0.0, -0.054255], [5.118355, 0.054255, 0.0], [5.118355, 0.0, 0.054255], [5.118355, -0.054255, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [5.118355, 0.0, 0.054255], [5.0641, 0.0, 0.0], [5.118355, 0.054255, 0.0], [5.172605, 0.0, 0.0], [5.118355, -0.054255, 0.0], [5.0641, 0.0, 0.0], [5.118355, 0.0, -0.054255], [5.172605, 0.0, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.0, 5.118355, -0.054255], [-0.054255, 5.118355, 0.0], [0.0, 5.118355, 0.054255], [0.054255, 5.118355, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 5.118355, 0.054255], [0.0, 5.0641, 0.0], [-0.054255, 5.118355, 0.0], [0.0, 5.172605, 0.0], [0.054255, 5.118355, 0.0], [0.0, 5.0641, 0.0], [0.0, 5.118355, -0.054255], [0.0, 5.172605, 0.0], [0.0, 0.0, 0.0]]}, {"shapeName": "C_world_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.0, 0.054255, 5.118355], [-0.054255, 0.0, 5.118355], [0.0, -0.054255, 5.118355], [0.054255, 0.0, 5.118355], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, -0.054255, 5.118355], [0.0, 0.0, 5.0641], [-0.054255, 0.0, 5.118355], [0.0, 0.0, 5.172605], [0.054255, 0.0, 5.118355], [0.0, 0.0, 5.0641], [0.0, 0.054255, 5.118355], [0.0, 0.0, 5.172605], [0.0, 0.0, 0.0]]}]},
			"R_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_A_CTLShape", "degree": 3, "form": 2, "points": [[-60.279383, 99.75923, -11.422109], [-61.741481, 100.864834, -11.953031], [-62.825262, 102.176152, -11.088257], [-62.895859, 102.925032, -9.334358], [-61.911921, 102.672791, -7.718743], [-60.449823, 101.567187, -7.187821], [-59.366042, 100.255869, -8.052594], [-59.295445, 99.50699, -9.806494]]}]},
			"R_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-61.257962, 100.758755, -7.976656], [-61.259581, 100.768456, -7.964876], [-61.24665, 100.763038, -7.958637], [-61.245031, 100.753338, -7.970417], [-61.257962, 100.758755, -7.976656], [-61.258035, 100.753413, -7.962272], [-61.24665, 100.763038, -7.958637], [-61.246577, 100.768381, -7.973022], [-61.259581, 100.768456, -7.964876], [-61.258035, 100.753413, -7.962272], [-61.245031, 100.753338, -7.970417], [-61.246577, 100.768381, -7.973022], [-61.257962, 100.758755, -7.976656], [-61.258035, 100.753413, -7.962272], [-60.7118, 101.467, -8.47477]]}, {"shapeName": "R_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-61.403801, 102.177961, -8.222404], [-61.392416, 102.187587, -8.21877], [-61.39249, 102.182243, -8.204385], [-61.403875, 102.172617, -8.208019], [-61.403801, 102.177961, -8.222404], [-61.40542, 102.18766, -8.210624], [-61.39249, 102.182243, -8.204385], [-61.39087, 102.172543, -8.216165], [-61.392416, 102.187587, -8.21877], [-61.40542, 102.18766, -8.210624], [-61.403875, 102.172617, -8.208019], [-61.39087, 102.172543, -8.216165], [-61.403801, 102.177961, -8.222404], [-61.40542, 102.18766, -8.210624], [-60.7118, 101.467, -8.47477]]}, {"shapeName": "R_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-60.185517, 101.676564, -7.622051], [-60.172512, 101.676489, -7.630197], [-60.170966, 101.661446, -7.627592], [-60.183971, 101.66152, -7.619446], [-60.185517, 101.676564, -7.622051], [-60.172586, 101.671146, -7.615813], [-60.170966, 101.661446, -7.627592], [-60.183897, 101.666863, -7.633831], [-60.172512, 101.676489, -7.630197], [-60.172586, 101.671146, -7.615813], [-60.183971, 101.66152, -7.619446], [-60.183897, 101.666863, -7.633831], [-60.185517, 101.676564, -7.622051], [-60.172586, 101.671146, -7.615813], [-60.7118, 101.467, -8.47477]]}]},
			"L_ring_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[62.052879, 100.240345, -11.139694], [62.059436, 100.248852, -11.128734], [62.0502, 100.242482, -11.118264], [62.043643, 100.233975, -11.129224], [62.052879, 100.240345, -11.139694], [62.05886, 100.233587, -11.127284], [62.0502, 100.242482, -11.118264], [62.044219, 100.249242, -11.130675], [62.059436, 100.248852, -11.128734], [62.05886, 100.233587, -11.127284], [62.043643, 100.233975, -11.129224], [62.044219, 100.249242, -11.130675], [62.052879, 100.240345, -11.139694], [62.05886, 100.233587, -11.127284], [61.360889, 100.979874, -11.288918]]}, {"shapeName": "L_ring_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[62.107174, 101.680533, -11.276498], [62.098514, 101.689429, -11.267478], [62.104496, 101.68267, -11.255068], [62.113156, 101.673774, -11.264088], [62.107174, 101.680533, -11.276498], [62.113731, 101.689039, -11.265538], [62.104496, 101.68267, -11.255068], [62.097939, 101.674163, -11.266028], [62.098514, 101.689429, -11.267478], [62.113731, 101.689039, -11.265538], [62.113156, 101.673774, -11.264088], [62.097939, 101.674163, -11.266028], [62.107174, 101.680533, -11.276498], [62.113731, 101.689039, -11.265538], [61.360889, 100.979874, -11.288918]]}, {"shapeName": "L_ring_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.242458, 101.088094, -10.277838], [61.227241, 101.088484, -10.279778], [61.226665, 101.073218, -10.278328], [61.241883, 101.072828, -10.276388], [61.242458, 101.088094, -10.277838], [61.233223, 101.081724, -10.267369], [61.226665, 101.073218, -10.278328], [61.235901, 101.079588, -10.288798], [61.227241, 101.088484, -10.279778], [61.233223, 101.081724, -10.267369], [61.241883, 101.072828, -10.276388], [61.235901, 101.079588, -10.288798], [61.242458, 101.088094, -10.277838], [61.233223, 101.081724, -10.267369], [61.360889, 100.979874, -11.288918]]}]},
			"world_D_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_D_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -34.662], [15.399, 0.0, -19.248], [11.544, 0.0, -19.248], [11.544, 0.0, -11.541], [19.251, 0.0, -11.541], [19.251, 0.0, -15.396], [34.662, 0.0, 0.0], [19.248, 0.0, 15.399], [19.248, 0.0, 11.544], [11.541, 0.0, 11.544], [11.541, 0.0, 19.251], [15.396, 0.0, 19.251], [0.0, 0.0, 34.662], [-15.399, 0.0, 19.248], [-11.544, 0.0, 19.248], [-11.544, 0.0, 11.541], [-19.251, 0.0, 11.541], [-19.251, 0.0, 15.396], [-34.662, 0.0, 0.0], [-19.248, 0.0, -15.399], [-19.248, 0.0, -11.544], [-11.541, 0.0, -11.544], [-11.541, 0.0, -19.251], [-15.396, 0.0, -19.251], [0.0, 0.0, -34.662], [3.018, 0.042, -31.698], [2.754, 0.0, -31.416], [2.754, 0.0, -30.264], [2.514, 0.0, -30.264], [2.529, 0.0, -31.425], [2.358, 0.0, -31.338], [2.364, 0.0, -30.834], [2.121, 0.0, -30.834], [2.121, 0.0, -31.338], [1.971, 0.0, -31.425], [1.971, 0.0, -30.246], [1.728, 0.0, -30.246], [1.728, 0.0, -31.455], [1.923, 0.0, -31.65], [2.223, 0.0, -31.5], [2.553, 0.0, -31.65], [2.754, 0.0, -31.422], [2.553, 0.0, -31.65], [2.226, 0.0, -31.503], [1.923, 0.0, -31.647], [1.338, 0.0, -31.65], [1.536, 0.0, -31.455], [1.536, 0.0, -30.444], [1.338, 0.0, -30.246], [0.705, 0.0, -30.246], [0.51, 0.0, -30.444], [0.51, 0.0, -31.455], [0.705, 0.0, -31.65], [1.338, 0.0, -31.65], [1.263, 0.0, -31.425], [1.293, 0.0, -30.495], [0.75, 0.0, -30.501], [0.753, 0.0, -31.425], [1.266, 0.0, -31.431], [1.338, 0.0, -31.65], [0.705, 0.0, -31.65], [0.3, 0.0, -31.65], [0.315, 0.0, -30.246], [-0.369, 0.0, -30.246], [-0.567, 0.0, -30.444], [-0.567, 0.0, -30.867], [-0.366, 0.0, -31.062], [-0.354, 0.0, -31.077], [-0.747, 0.0, -31.644], [-0.747, 0.0, -31.65], [-0.465, 0.0, -31.65], [-0.072, 0.0, -31.08], [0.075, 0.0, -31.08], [0.075, 0.0, -30.48], [-0.303, 0.0, -30.48], [-0.306, 0.0, -30.837], [0.075, 0.0, -30.837], [0.075, 0.0, -31.65], [0.3, 0.0, -31.65], [-1.929, 0.0, -31.65], [-1.929, 0.0, -31.425], [-1.143, 0.0, -31.422], [-1.143, 0.0, -30.246], [-0.9, 0.0, -30.246], [-0.9, 0.0, -31.65], [-2.952, 0.0, -31.65], [-3.132, 0.0, -31.455], [-3.147, 0.0, -30.444], [-2.952, 0.0, -30.246], [-2.121, 0.0, -30.246], [-2.121, 0.0, -31.65], [-2.367, 0.0, -31.425], [-2.361, 0.0, -30.474], [-2.874, 0.0, -30.474], [-2.868, 0.0, -31.419], [-2.358, 0.0, -31.431], [-2.115, 0.0, -31.65]]}]},
			"R_index_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_A_CTLShape", "degree": 3, "form": 2, "points": [[-60.448684, 99.890431, -10.388865], [-62.011469, 100.974533, -10.545055], [-62.812949, 102.346865, -9.488502], [-62.383625, 103.203532, -7.838117], [-60.974992, 103.042714, -6.560674], [-59.412207, 101.958612, -6.404484], [-58.610727, 100.586281, -7.461037], [-59.040051, 99.729613, -9.111422]]}]},
			"L_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_A_CTLShape", "degree": 3, "form": 2, "points": [[60.189224, 100.01413, -14.589285], [61.604937, 101.12845, -15.218585], [62.957823, 102.188862, -14.389614], [63.45538, 102.574189, -12.587968], [62.806148, 102.058716, -10.869028], [61.390436, 100.944396, -10.239728], [60.037549, 99.883984, -11.0687], [59.539992, 99.498656, -12.870346]]}]},
			"L_middle_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_A_CTLShape", "degree": 3, "form": 2, "points": [[60.279383, 99.75923, -11.422109], [61.741481, 100.864834, -11.953031], [62.825262, 102.176152, -11.088257], [62.895859, 102.925032, -9.334358], [61.911921, 102.672791, -7.718743], [60.449823, 101.567187, -7.187821], [59.366042, 100.255869, -8.052594], [59.295445, 99.50699, -9.806494]]}]},
			"L_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_D_CTLShape", "degree": 3, "form": 2, "points": [[64.926715, 92.602506, -16.031811], [66.542621, 93.111811, -16.910119], [68.379885, 93.212182, -16.403804], [69.362262, 92.844822, -14.809454], [68.914292, 92.224926, -13.06102], [67.298386, 91.71562, -12.182712], [65.461122, 91.615249, -12.689027], [64.478745, 91.98261, -14.283377]]}]},
			"R_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_C_CTLShape", "degree": 3, "form": 2, "points": [[-64.189172, 94.528222, -15.369571], [-65.727978, 95.356009, -16.136913], [-67.481244, 95.783318, -15.516078], [-68.421929, 95.559836, -13.87074], [-67.998995, 94.816477, -12.164717], [-66.460189, 93.988691, -11.397376], [-64.706924, 93.561381, -12.01821], [-63.766239, 93.784863, -13.663548]]}]},
			"L_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[64.88486, 96.570868, -13.061545], [64.895599, 96.573711, -13.050958], [64.887954, 96.565031, -13.040873], [64.877215, 96.562188, -13.05146], [64.88486, 96.570868, -13.061545], [64.891962, 96.55923, -13.054502], [64.887954, 96.565031, -13.040873], [64.880852, 96.576669, -13.047915], [64.895599, 96.573711, -13.050958], [64.891962, 96.55923, -13.054502], [64.877215, 96.562188, -13.05146], [64.880852, 96.576669, -13.047915], [64.88486, 96.570868, -13.061545], [64.891962, 96.55923, -13.054502], [64.362319, 97.390571, -12.740519]]}, {"shapeName": "L_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[65.227916, 97.936998, -12.727175], [65.223908, 97.9428, -12.713545], [65.23101, 97.931162, -12.706503], [65.235019, 97.92536, -12.720132], [65.227916, 97.936998, -12.727175], [65.238654, 97.939841, -12.716588], [65.23101, 97.931162, -12.706503], [65.220271, 97.928319, -12.71709], [65.223908, 97.9428, -12.713545], [65.238654, 97.939841, -12.716588], [65.235019, 97.92536, -12.720132], [65.220271, 97.928319, -12.71709], [65.227916, 97.936998, -12.727175], [65.238654, 97.939841, -12.716588], [64.362319, 97.390571, -12.740519]]}, {"shapeName": "L_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[64.51744, 97.121025, -11.765171], [64.502693, 97.123984, -11.762129], [64.499056, 97.109503, -11.765673], [64.513803, 97.106544, -11.768715], [64.51744, 97.121025, -11.765171], [64.509795, 97.112346, -11.755087], [64.499056, 97.109503, -11.765673], [64.506701, 97.118182, -11.775758], [64.502693, 97.123984, -11.762129], [64.509795, 97.112346, -11.755087], [64.513803, 97.106544, -11.768715], [64.506701, 97.118182, -11.775758], [64.51744, 97.121025, -11.765171], [64.509795, 97.112346, -11.755087], [64.362319, 97.390571, -12.740519]]}]},
			"visibility_CTL": {"color": 17, "shapes": [{"shapeName": "visibility_CTLShape", "degree": 3, "form": 2, "points": [[13.176103, 195.497817, 0.0], [2.931462, 203.712084, 0.0], [-7.313179, 195.497817, 0.0], [-7.286275, 195.497817, 0.0], [-7.313179, 195.497817, 0.0], [2.931462, 187.283549, 0.0], [13.176103, 195.497817, 0.0], [13.176103, 195.497817, 0.0]]}, {"shapeName": "visibility_CTLShape1", "degree": 3, "form": 2, "points": [[7.2193, 199.785655, 0.0], [2.931462, 201.561725, 0.0], [-1.356376, 199.785655, 0.0], [-3.132447, 195.497817, 0.0], [-1.356376, 191.209979, 0.0], [2.931462, 189.433908, 0.0], [7.2193, 191.209979, 0.0], [8.99537, 195.497817, 0.0]]}]},
			"R_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.056402, 91.450075, -14.86417], [-67.068673, 91.448913, -14.855028], [-67.059691, 91.443999, -14.843597], [-67.04742, 91.445161, -14.852739], [-67.056402, 91.450075, -14.86417], [-67.059504, 91.436791, -14.857143], [-67.059691, 91.443999, -14.843597], [-67.056588, 91.457283, -14.850624], [-67.068673, 91.448913, -14.855028], [-67.059504, 91.436791, -14.857143], [-67.04742, 91.445161, -14.852739], [-67.056588, 91.457283, -14.850624], [-67.056402, 91.450075, -14.86417], [-67.059504, 91.436791, -14.857143], [-66.9205, 92.4137, -14.5464]]}, {"shapeName": "R_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.921311, 92.593727, -14.664676], [-67.921497, 92.600935, -14.651131], [-67.9246, 92.587651, -14.644103], [-67.924413, 92.580442, -14.657649], [-67.921311, 92.593727, -14.664676], [-67.93358, 92.592565, -14.655534], [-67.9246, 92.587651, -14.644103], [-67.912329, 92.588813, -14.653245], [-67.921497, 92.600935, -14.651131], [-67.93358, 92.592565, -14.655534], [-67.924413, 92.580442, -14.657649], [-67.912329, 92.588813, -14.653245], [-67.921311, 92.593727, -14.664676], [-67.93358, 92.592565, -14.655534], [-66.9205, 92.4137, -14.5464]]}, {"shapeName": "R_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-67.086265, 92.128975, -13.577136], [-67.074181, 92.137346, -13.572732], [-67.065013, 92.125223, -13.574846], [-67.077097, 92.116853, -13.57925], [-67.086265, 92.128975, -13.577136], [-67.077283, 92.124062, -13.565705], [-67.065013, 92.125223, -13.574846], [-67.073994, 92.130137, -13.586277], [-67.074181, 92.137346, -13.572732], [-67.077283, 92.124062, -13.565705], [-67.077097, 92.116853, -13.57925], [-67.073994, 92.130137, -13.586277], [-67.086265, 92.128975, -13.577136], [-67.077283, 92.124062, -13.565705], [-66.9205, 92.4137, -14.5464]]}]},
			"R_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-61.755306, 100.483152, -9.294977], [-61.760329, 100.492117, -9.283581], [-61.749685, 100.486208, -9.27424], [-61.744661, 100.477243, -9.285636], [-61.755306, 100.483152, -9.294977], [-61.759457, 100.476929, -9.281579], [-61.749685, 100.486208, -9.27424], [-61.745533, 100.492432, -9.287638], [-61.760329, 100.492117, -9.283581], [-61.759457, 100.476929, -9.281579], [-61.744661, 100.477243, -9.285636], [-61.745533, 100.492432, -9.287638], [-61.755306, 100.483152, -9.294977], [-61.759457, 100.476929, -9.281579], [-61.0957, 101.216, -9.57043]]}, {"shapeName": "R_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-61.837579, 101.916104, -9.483882], [-61.827806, 101.925384, -9.476543], [-61.831958, 101.91916, -9.463144], [-61.84173, 101.90988, -9.470483], [-61.837579, 101.916104, -9.483882], [-61.842602, 101.925068, -9.472486], [-61.831958, 101.91916, -9.463144], [-61.826934, 101.910194, -9.47454], [-61.827806, 101.925384, -9.476543], [-61.842602, 101.925068, -9.472486], [-61.84173, 101.90988, -9.470483], [-61.826934, 101.910194, -9.47454], [-61.837579, 101.916104, -9.483882], [-61.842602, 101.925068, -9.472486], [-61.0957, 101.216, -9.57043]]}, {"shapeName": "R_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-60.838392, 101.367611, -8.591233], [-60.823595, 101.367926, -8.59529], [-60.822723, 101.352737, -8.593288], [-60.83752, 101.352422, -8.589231], [-60.838392, 101.367611, -8.591233], [-60.827747, 101.361702, -8.581893], [-60.822723, 101.352737, -8.593288], [-60.833368, 101.358646, -8.602629], [-60.823595, 101.367926, -8.59529], [-60.827747, 101.361702, -8.581893], [-60.83752, 101.352422, -8.589231], [-60.833368, 101.358646, -8.602629], [-60.838392, 101.367611, -8.591233], [-60.827747, 101.361702, -8.581893], [-61.0957, 101.216, -9.57043]]}]},
			"L_hand_CTL": {"color": 1, "shapes": [{"shapeName": "L_hand_CTLShape", "degree": 1, "form": 0, "points": [[84.103922, 111.062666, 0.0], [83.519282, 111.166616, 0.0], [82.916057, 111.190346, 0.0], [82.344332, 111.177116, 0.0], [81.775547, 111.189401, 0.0], [81.393977, 111.218276, 0.0], [81.095567, 111.413786, 0.0], [80.846717, 111.868856, 0.0], [80.580017, 112.460111, 0.0], [80.366972, 113.119931, 0.0], [80.166422, 114.055166, 0.0], [80.066777, 115.002896, 0.0], [80.022257, 115.740626, 0.0], [80.008922, 116.320751, 0.0], [79.945187, 116.688251, 0.0], [79.877777, 117.138386, 0.0], [79.743482, 117.637031, 0.0], [79.659167, 118.082756, 0.0], [79.569287, 118.443851, 0.0], [79.433942, 118.868996, 0.0], [79.289252, 119.418041, 0.0], [79.286522, 119.842871, 0.0], [79.459457, 120.178976, 0.0], [79.665362, 120.244706, 0.0], [79.937522, 120.120176, 0.0], [80.040422, 119.796986, 0.0], [80.162747, 119.380136, 0.0], [80.324342, 118.970846, 0.0], [80.487092, 118.544126, 0.0], [80.656562, 118.026581, 0.0], [80.852072, 117.606371, 0.0], [81.025742, 117.429761, 0.0], [81.106382, 117.415901, 0.0], [81.240467, 117.677141, 0.0], [81.255062, 118.054091, 0.0], [81.157517, 118.489211, 0.0], [81.095567, 118.779536, 0.0], [81.050942, 119.219276, 0.0], [81.018392, 119.616806, 0.0], [80.949827, 120.034076, 0.0], [80.904257, 120.388346, 0.0], [80.859212, 120.689696, 0.0], [80.771327, 121.131431, 0.0], [80.697407, 121.481396, 0.0], [80.666012, 121.820651, 0.0], [80.768807, 122.133761, 0.0], [80.969777, 122.336621, 0.0], [81.263462, 122.347121, 0.0], [81.514412, 122.194976, 0.0], [81.641567, 121.859081, 0.0], [81.721787, 121.463231, 0.0], [81.800012, 121.112426, 0.0], [81.897347, 120.699356, 0.0], [81.985232, 120.316211, 0.0], [82.050752, 119.950601, 0.0], [82.100942, 119.555591, 0.0], [82.205627, 119.087081, 0.0], [82.283012, 118.768301, 0.0], [82.346327, 118.393766, 0.0], [82.539632, 118.101761, 0.0], [82.670042, 118.299581, 0.0], [82.747532, 118.819436, 0.0], [82.764752, 119.210351, 0.0], [82.752467, 119.716661, 0.0], [82.774097, 120.167321, 0.0], [82.798982, 120.563171, 0.0], [82.801922, 121.020026, 0.0], [82.779242, 121.453361, 0.0], [82.780397, 122.068661, 0.0], [82.797092, 122.517011, 0.0], [82.857887, 122.898896, 0.0], [83.082167, 123.061016, 0.0], [83.377217, 123.147851, 0.0], [83.638457, 123.059651, 0.0], [83.773907, 122.784971, 0.0], [83.809187, 122.332421, 0.0], [83.841947, 121.883966, 0.0], [83.860007, 121.511741, 0.0], [83.827562, 121.024961, 0.0], [83.822627, 120.578186, 0.0], [83.884472, 120.099176, 0.0], [83.923742, 119.864186, 0.0], [83.913242, 119.546876, 0.0], [83.929307, 119.191766, 0.0], [83.957867, 118.761686, 0.0], [83.983172, 118.247921, 0.0], [84.045542, 118.130006, 0.0], [84.197792, 118.272176, 0.0], [84.270242, 118.628966, 0.0], [84.372197, 119.098946, 0.0], [84.500717, 119.653346, 0.0], [84.587132, 120.135716, 0.0], [84.676697, 120.562751, 0.0], [84.811622, 120.960911, 0.0], [84.956942, 121.433726, 0.0], [85.071392, 121.924286, 0.0], [85.191617, 122.301446, 0.0], [85.328957, 122.598701, 0.0], [85.552397, 122.825291, 0.0], [85.722602, 122.788436, 0.0], [86.022902, 122.593556, 0.0], [86.131472, 122.145836, 0.0], [86.063537, 121.697171, 0.0], [86.009042, 121.389416, 0.0], [85.961162, 121.005956, 0.0], [85.888187, 120.598766, 0.0], [85.744232, 120.153461, 0.0], [85.681337, 119.870066, 0.0], [85.651412, 119.362811, 0.0], [85.633667, 119.033846, 0.0], [85.562057, 118.615736, 0.0], [85.499582, 118.238261, 0.0], [85.469657, 117.820256, 0.0], [85.417997, 117.188891, 0.0], [85.474382, 116.285786, 0.0], [85.583582, 115.821896, 0.0], [85.757777, 115.527686, 0.0], [85.979957, 115.209116, 0.0], [86.162447, 115.597511, 0.0], [86.454347, 116.031371, 0.0], [86.606492, 116.341856, 0.0], [86.676842, 116.694446, 0.0], [86.849672, 117.051656, 0.0], [87.132122, 117.413171, 0.0], [87.508757, 117.683651, 0.0], [87.775142, 117.764501, 0.0], [88.032812, 117.601646, 0.0], [88.078487, 117.345026, 0.0], [88.012337, 116.910326, 0.0], [87.872267, 116.630606, 0.0], [87.852842, 116.377136, 0.0], [87.843392, 115.889831, 0.0], [87.689987, 115.591526, 0.0], [87.502562, 115.351076, 0.0], [87.450167, 115.120391, 0.0], [87.409952, 114.823871, 0.0], [87.227147, 114.353051, 0.0], [86.993312, 113.338331, 0.0], [86.708027, 112.835276, 0.0], [86.337272, 112.266176, 0.0], [85.971032, 111.770576, 0.0], [85.682702, 111.404966, 0.0], [85.167467, 111.120626, 0.0], [84.695807, 111.030011, 0.0], [84.112217, 111.061931, 0.0]]}]},
			"R_middle_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_D_CTLShape", "degree": 3, "form": 2, "points": [[-67.01437, 89.419859, -8.327611], [-68.865603, 89.684707, -8.708083], [-70.416192, 90.069501, -7.664255], [-70.757819, 90.348834, -5.807582], [-69.690369, 90.359078, -4.22568], [-67.839135, 90.09423, -3.845208], [-66.288547, 89.709436, -4.889037], [-65.94692, 89.430103, -6.745709]]}]},
			"R_pinky_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-64.884841, 96.570897, -13.061526], [-64.89558, 96.57374, -13.050939], [-64.887935, 96.56506, -13.040854], [-64.877196, 96.562217, -13.051441], [-64.884841, 96.570897, -13.061526], [-64.891943, 96.559259, -13.054483], [-64.887935, 96.56506, -13.040854], [-64.880833, 96.576698, -13.047896], [-64.89558, 96.57374, -13.050939], [-64.891943, 96.559259, -13.054483], [-64.877196, 96.562217, -13.051441], [-64.880833, 96.576698, -13.047896], [-64.884841, 96.570897, -13.061526], [-64.891943, 96.559259, -13.054483], [-64.3623, 97.3906, -12.7405]]}, {"shapeName": "R_pinky_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-65.227897, 97.937027, -12.727156], [-65.223889, 97.942829, -12.713526], [-65.230991, 97.931191, -12.706484], [-65.235, 97.925389, -12.720113], [-65.227897, 97.937027, -12.727156], [-65.238635, 97.93987, -12.716569], [-65.230991, 97.931191, -12.706484], [-65.220252, 97.928348, -12.717071], [-65.223889, 97.942829, -12.713526], [-65.238635, 97.93987, -12.716569], [-65.235, 97.925389, -12.720113], [-65.220252, 97.928348, -12.717071], [-65.227897, 97.937027, -12.727156], [-65.238635, 97.93987, -12.716569], [-64.3623, 97.3906, -12.7405]]}, {"shapeName": "R_pinky_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-64.517421, 97.121054, -11.765152], [-64.502674, 97.124013, -11.76211], [-64.499037, 97.109532, -11.765654], [-64.513784, 97.106573, -11.768696], [-64.517421, 97.121054, -11.765152], [-64.509776, 97.112375, -11.755068], [-64.499037, 97.109532, -11.765654], [-64.506682, 97.118211, -11.775739], [-64.502674, 97.124013, -11.76211], [-64.509776, 97.112375, -11.755068], [-64.513784, 97.106573, -11.768696], [-64.506682, 97.118211, -11.775739], [-64.517421, 97.121054, -11.765152], [-64.509776, 97.112375, -11.755068], [-64.3623, 97.3906, -12.7405]]}]},
			"L_pinky_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.056405, 91.450091, -14.864185], [67.068676, 91.448929, -14.855043], [67.059694, 91.444015, -14.843612], [67.047423, 91.445177, -14.852754], [67.056405, 91.450091, -14.864185], [67.059507, 91.436807, -14.857158], [67.059694, 91.444015, -14.843612], [67.056591, 91.457299, -14.850639], [67.068676, 91.448929, -14.855043], [67.059507, 91.436807, -14.857158], [67.047423, 91.445177, -14.852754], [67.056591, 91.457299, -14.850639], [67.056405, 91.450091, -14.864185], [67.059507, 91.436807, -14.857158], [66.920503, 92.413716, -14.546415]]}, {"shapeName": "L_pinky_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[67.921314, 92.593743, -14.664691], [67.9215, 92.600951, -14.651146], [67.924603, 92.587667, -14.644118], [67.924416, 92.580458, -14.657664], [67.921314, 92.593743, -14.664691], [67.933583, 92.592581, -14.655549], [67.924603, 92.587667, -14.644118], [67.912332, 92.588829, -14.65326], [67.9215, 92.600951, -14.651146], [67.933583, 92.592581, -14.655549], [67.924416, 92.580458, -14.657664], [67.912332, 92.588829, -14.65326], [67.921314, 92.593743, -14.664691], [67.933583, 92.592581, -14.655549], [66.920503, 92.413716, -14.546415]]}, {"shapeName": "L_pinky_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[67.086268, 92.128991, -13.577151], [67.074184, 92.137362, -13.572747], [67.065016, 92.125239, -13.574861], [67.0771, 92.116869, -13.579265], [67.086268, 92.128991, -13.577151], [67.077286, 92.124078, -13.56572], [67.065016, 92.125239, -13.574861], [67.073997, 92.130153, -13.586292], [67.074184, 92.137362, -13.572747], [67.077286, 92.124078, -13.56572], [67.0771, 92.116869, -13.579265], [67.073997, 92.130153, -13.586292], [67.086268, 92.128991, -13.577151], [67.077286, 92.124078, -13.56572], [66.920503, 92.413716, -14.546415]]}]},
			"R_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-68.676382, 89.280791, -10.816333], [-68.687291, 89.280721, -10.805541], [-68.67651, 89.279941, -10.794648], [-68.665601, 89.28001, -10.805441], [-68.676382, 89.280791, -10.816333], [-68.6768, 89.26953, -10.805918], [-68.67651, 89.279941, -10.794648], [-68.676093, 89.291203, -10.805064], [-68.687291, 89.280721, -10.805541], [-68.6768, 89.26953, -10.805918], [-68.665601, 89.28001, -10.805441], [-68.676093, 89.291203, -10.805064], [-68.676382, 89.280791, -10.816333], [-68.6768, 89.26953, -10.805918], [-68.6431, 90.3027, -10.7652]]}, {"shapeName": "R_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-69.666146, 90.336682, -10.78075], [-69.665857, 90.347094, -10.769481], [-69.666274, 90.335832, -10.759065], [-69.666564, 90.32542, -10.770335], [-69.666146, 90.336682, -10.78075], [-69.677054, 90.336613, -10.769958], [-69.666274, 90.335832, -10.759065], [-69.655365, 90.335901, -10.769858], [-69.665857, 90.347094, -10.769481], [-69.677054, 90.336613, -10.769958], [-69.666564, 90.32542, -10.770335], [-69.655365, 90.335901, -10.769858], [-69.666146, 90.336682, -10.78075], [-69.677054, 90.336613, -10.769958], [-68.6431, 90.3027, -10.7652]]}, {"shapeName": "R_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-68.659967, 90.26294, -9.742383], [-68.648769, 90.273421, -9.741906], [-68.638277, 90.262229, -9.742283], [-68.649476, 90.251748, -9.74276], [-68.659967, 90.26294, -9.742383], [-68.649186, 90.262159, -9.731492], [-68.638277, 90.262229, -9.742283], [-68.649058, 90.26301, -9.753176], [-68.648769, 90.273421, -9.741906], [-68.649186, 90.262159, -9.731492], [-68.649476, 90.251748, -9.74276], [-68.649058, 90.26301, -9.753176], [-68.659967, 90.26294, -9.742383], [-68.649186, 90.262159, -9.731492], [-68.6431, 90.3027, -10.7652]]}]},
			"L_ring_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_D_CTLShape", "degree": 3, "form": 2, "points": [[66.870583, 90.313994, -12.518867], [68.628448, 90.400411, -13.25671], [70.394905, 90.429589, -12.535082], [71.135186, 90.384437, -10.776699], [70.415649, 90.291403, -9.011598], [68.657784, 90.204987, -8.273754], [66.891327, 90.175809, -8.995382], [66.151046, 90.220961, -10.753766]]}]},
			"R_hand_CTL": {"color": 1, "shapes": [{"shapeName": "R_hand_CTLShape", "degree": 1, "form": 0, "points": [[-84.103922, 111.062666, 0.0], [-83.519282, 111.166616, -0.0], [-82.916057, 111.190346, -0.0], [-82.344332, 111.177116, 0.0], [-81.775547, 111.189401, -0.0], [-81.393977, 111.218276, -0.0], [-81.095567, 111.413786, -0.0], [-80.846717, 111.868856, -0.0], [-80.580017, 112.460111, -0.0], [-80.366972, 113.119931, 0.0], [-80.166422, 114.055166, -0.0], [-80.066777, 115.002896, -0.0], [-80.022257, 115.740626, -0.0], [-80.008922, 116.320751, -0.0], [-79.945187, 116.688251, -0.0], [-79.877777, 117.138386, -0.0], [-79.743482, 117.637031, -0.0], [-79.659167, 118.082756, 0.0], [-79.569287, 118.443851, -0.0], [-79.433942, 118.868996, -0.0], [-79.289252, 119.418041, -0.0], [-79.286522, 119.842871, -0.0], [-79.459457, 120.178976, 0.0], [-79.665362, 120.244706, -0.0], [-79.937522, 120.120176, 0.0], [-80.040422, 119.796986, -0.0], [-80.162747, 119.380136, 0.0], [-80.324342, 118.970846, 0.0], [-80.487092, 118.544126, 0.0], [-80.656562, 118.026581, -0.0], [-80.852072, 117.606371, -0.0], [-81.025742, 117.429761, 0.0], [-81.106382, 117.415901, -0.0], [-81.240467, 117.677141, -0.0], [-81.255062, 118.054091, -0.0], [-81.157517, 118.489211, -0.0], [-81.095567, 118.779536, -0.0], [-81.050942, 119.219276, -0.0], [-81.018392, 119.616806, 0.0], [-80.949827, 120.034076, -0.0], [-80.904257, 120.388346, 0.0], [-80.859212, 120.689696, 0.0], [-80.771327, 121.131431, 0.0], [-80.697407, 121.481396, -0.0], [-80.666012, 121.820651, 0.0], [-80.768807, 122.133761, -0.0], [-80.969777, 122.336621, 0.0], [-81.263462, 122.347121, -0.0], [-81.514412, 122.194976, 0.0], [-81.641567, 121.859081, -0.0], [-81.721787, 121.463231, 0.0], [-81.800012, 121.112426, 0.0], [-81.897347, 120.699356, -0.0], [-81.985232, 120.316211, 0.0], [-82.050752, 119.950601, -0.0], [-82.100942, 119.555591, 0.0], [-82.205627, 119.087081, -0.0], [-82.283012, 118.768301, -0.0], [-82.346327, 118.393766, -0.0], [-82.539632, 118.101761, 0.0], [-82.670042, 118.299581, -0.0], [-82.747532, 118.819436, -0.0], [-82.764752, 119.210351, 0.0], [-82.752467, 119.716661, -0.0], [-82.774097, 120.167321, -0.0], [-82.798982, 120.563171, -0.0], [-82.801922, 121.020026, -0.0], [-82.779242, 121.453361, 0.0], [-82.780397, 122.068661, -0.0], [-82.797092, 122.517011, 0.0], [-82.857887, 122.898896, 0.0], [-83.082167, 123.061016, -0.0], [-83.377217, 123.147851, 0.0], [-83.638457, 123.059651, -0.0], [-83.773907, 122.784971, -0.0], [-83.809187, 122.332421, -0.0], [-83.841947, 121.883966, -0.0], [-83.860007, 121.511741, -0.0], [-83.827562, 121.024961, -0.0], [-83.822627, 120.578186, -0.0], [-83.884472, 120.099176, -0.0], [-83.923742, 119.864186, -0.0], [-83.913242, 119.546876, -0.0], [-83.929307, 119.191766, -0.0], [-83.957867, 118.761686, -0.0], [-83.983172, 118.247921, -0.0], [-84.045542, 118.130006, 0.0], [-84.197792, 118.272176, 0.0], [-84.270242, 118.628966, -0.0], [-84.372197, 119.098946, 0.0], [-84.500717, 119.653346, -0.0], [-84.587132, 120.135716, -0.0], [-84.676697, 120.562751, -0.0], [-84.811622, 120.960911, -0.0], [-84.956942, 121.433726, -0.0], [-85.071392, 121.924286, -0.0], [-85.191617, 122.301446, 0.0], [-85.328957, 122.598701, 0.0], [-85.552397, 122.825291, -0.0], [-85.722602, 122.788436, 0.0], [-86.022902, 122.593556, -0.0], [-86.131472, 122.145836, -0.0], [-86.063537, 121.697171, 0.0], [-86.009042, 121.389416, -0.0], [-85.961162, 121.005956, -0.0], [-85.888187, 120.598766, -0.0], [-85.744232, 120.153461, -0.0], [-85.681337, 119.870066, -0.0], [-85.651412, 119.362811, 0.0], [-85.633667, 119.033846, -0.0], [-85.562057, 118.615736, -0.0], [-85.499582, 118.238261, -0.0], [-85.469657, 117.820256, -0.0], [-85.417997, 117.188891, -0.0], [-85.474382, 116.285786, -0.0], [-85.583582, 115.821896, -0.0], [-85.757777, 115.527686, 0.0], [-85.979957, 115.209116, -0.0], [-86.162447, 115.597511, -0.0], [-86.454347, 116.031371, -0.0], [-86.606492, 116.341856, -0.0], [-86.676842, 116.694446, -0.0], [-86.849672, 117.051656, -0.0], [-87.132122, 117.413171, -0.0], [-87.508757, 117.683651, -0.0], [-87.775142, 117.764501, -0.0], [-88.032812, 117.601646, -0.0], [-88.078487, 117.345026, -0.0], [-88.012337, 116.910326, -0.0], [-87.872267, 116.630606, -0.0], [-87.852842, 116.377136, -0.0], [-87.843392, 115.889831, -0.0], [-87.689987, 115.591526, -0.0], [-87.502562, 115.351076, -0.0], [-87.450167, 115.120391, -0.0], [-87.409952, 114.823871, -0.0], [-87.227147, 114.353051, -0.0], [-86.993312, 113.338331, -0.0], [-86.708027, 112.835276, -0.0], [-86.337272, 112.266176, -0.0], [-85.971032, 111.770576, -0.0], [-85.682702, 111.404966, -0.0], [-85.167467, 111.120626, 0.0], [-84.695807, 111.030011, -0.0], [-84.112217, 111.061931, -0.0]]}]},
			"L_thumb_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[57.807642, 100.742528, -7.270903], [57.794152, 100.748227, -7.266318], [57.786846, 100.737247, -7.274163], [57.800336, 100.731548, -7.278749], [57.807642, 100.742528, -7.270903], [57.797504, 100.733468, -7.26379], [57.786846, 100.737247, -7.274163], [57.796985, 100.746308, -7.281277], [57.794152, 100.748227, -7.266318], [57.797504, 100.733468, -7.26379], [57.800336, 100.731548, -7.278749], [57.796985, 100.746308, -7.281277], [57.807642, 100.742528, -7.270903], [57.797504, 100.733468, -7.26379], [57.772776, 101.345592, -8.097412]]}, {"shapeName": "L_thumb_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[57.491471, 102.13499, -7.509417], [57.480814, 102.13877, -7.519791], [57.470675, 102.12971, -7.512677], [57.481333, 102.125929, -7.502303], [57.491471, 102.13499, -7.509417], [57.477982, 102.140689, -7.504832], [57.470675, 102.12971, -7.512677], [57.484165, 102.12401, -7.517262], [57.480814, 102.13877, -7.519791], [57.477982, 102.140689, -7.504832], [57.481333, 102.125929, -7.502303], [57.484165, 102.12401, -7.517262], [57.491471, 102.13499, -7.509417], [57.477982, 102.140689, -7.504832], [57.772776, 101.345592, -8.097412]]}, {"shapeName": "L_thumb_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[56.788759, 101.104861, -8.244991], [56.791591, 101.102942, -8.25995], [56.794943, 101.088182, -8.257422], [56.79211, 101.090101, -8.242463], [56.788759, 101.104861, -8.244991], [56.781454, 101.093881, -8.252836], [56.794943, 101.088182, -8.257422], [56.802249, 101.099161, -8.249576], [56.791591, 101.102942, -8.25995], [56.781454, 101.093881, -8.252836], [56.79211, 101.090101, -8.242463], [56.802249, 101.099161, -8.249576], [56.788759, 101.104861, -8.244991], [56.781454, 101.093881, -8.252836], [57.772776, 101.345592, -8.097412]]}]},
			"L_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[66.349614, 92.441652, -2.936398], [66.353091, 92.44772, -2.922739], [66.338642, 92.445494, -2.918072], [66.335165, 92.439426, -2.931732], [66.349614, 92.441652, -2.936398], [66.346833, 92.433733, -2.923552], [66.338642, 92.445494, -2.918072], [66.341422, 92.453415, -2.930919], [66.353091, 92.44772, -2.922739], [66.346833, 92.433733, -2.923552], [66.335165, 92.439426, -2.931732], [66.341422, 92.453415, -2.930919], [66.349614, 92.441652, -2.936398], [66.346833, 92.433733, -2.923552], [66.08888, 93.372015, -3.274723]]}, {"shapeName": "L_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[66.939902, 93.761304, -2.859712], [66.931711, 93.773067, -2.854232], [66.928931, 93.765147, -2.841386], [66.937122, 93.753384, -2.846865], [66.939902, 93.761304, -2.859712], [66.943379, 93.767372, -2.846053], [66.928931, 93.765147, -2.841386], [66.925454, 93.759079, -2.855045], [66.931711, 93.773067, -2.854232], [66.943379, 93.767372, -2.846053], [66.937122, 93.753384, -2.846865], [66.925454, 93.759079, -2.855045], [66.939902, 93.761304, -2.859712], [66.943379, 93.767372, -2.846053], [66.08888, 93.372015, -3.274723]]}, {"shapeName": "L_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[65.580331, 93.557415, -2.405801], [65.568663, 93.563109, -2.41398], [65.562406, 93.549121, -2.414793], [65.574074, 93.543426, -2.406613], [65.580331, 93.557415, -2.405801], [65.565883, 93.555189, -2.401135], [65.562406, 93.549121, -2.414793], [65.576854, 93.551346, -2.41946], [65.568663, 93.563109, -2.41398], [65.565883, 93.555189, -2.401135], [65.574074, 93.543426, -2.406613], [65.576854, 93.551346, -2.41946], [65.580331, 93.557415, -2.405801], [65.565883, 93.555189, -2.401135], [66.08888, 93.372015, -3.274723]]}]},
			"L_ring_A_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_A_CTLShape", "degree": 3, "form": 2, "points": [[60.295406, 99.597666, -13.069783], [61.668594, 100.734391, -13.751088], [62.861533, 102.014917, -12.99009], [63.175414, 102.689128, -11.232566], [62.426372, 102.362082, -9.508053], [61.053184, 101.225357, -8.826748], [59.860244, 99.944831, -9.587746], [59.546364, 99.27062, -11.345269]]}]},
			"R_index_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.349634, 92.441637, -2.936395], [-66.353111, 92.447705, -2.922736], [-66.338662, 92.445479, -2.918069], [-66.335185, 92.439411, -2.931729], [-66.349634, 92.441637, -2.936395], [-66.346853, 92.433718, -2.923549], [-66.338662, 92.445479, -2.918069], [-66.341442, 92.4534, -2.930916], [-66.353111, 92.447705, -2.922736], [-66.346853, 92.433718, -2.923549], [-66.335185, 92.439411, -2.931729], [-66.341442, 92.4534, -2.930916], [-66.349634, 92.441637, -2.936395], [-66.346853, 92.433718, -2.923549], [-66.0889, 93.372, -3.27472]]}, {"shapeName": "R_index_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-66.939922, 93.761289, -2.859709], [-66.931731, 93.773052, -2.854229], [-66.928951, 93.765132, -2.841383], [-66.937142, 93.753369, -2.846862], [-66.939922, 93.761289, -2.859709], [-66.943399, 93.767357, -2.84605], [-66.928951, 93.765132, -2.841383], [-66.925474, 93.759064, -2.855042], [-66.931731, 93.773052, -2.854229], [-66.943399, 93.767357, -2.84605], [-66.937142, 93.753369, -2.846862], [-66.925474, 93.759064, -2.855042], [-66.939922, 93.761289, -2.859709], [-66.943399, 93.767357, -2.84605], [-66.0889, 93.372, -3.27472]]}, {"shapeName": "R_index_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-65.580351, 93.5574, -2.405798], [-65.568683, 93.563094, -2.413977], [-65.562426, 93.549106, -2.41479], [-65.574094, 93.543411, -2.40661], [-65.580351, 93.5574, -2.405798], [-65.565903, 93.555174, -2.401132], [-65.562426, 93.549106, -2.41479], [-65.576874, 93.551331, -2.419457], [-65.568683, 93.563094, -2.413977], [-65.565903, 93.555174, -2.401132], [-65.574094, 93.543411, -2.40661], [-65.576874, 93.551331, -2.419457], [-65.580351, 93.5574, -2.405798], [-65.565903, 93.555174, -2.401132], [-66.0889, 93.372, -3.27472]]}]},
			"R_index_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.767201, 89.821747, -2.155876], [-66.771268, 89.82421, -2.141285], [-66.756476, 89.825277, -2.137343], [-66.752409, 89.822814, -2.151933], [-66.767201, 89.821747, -2.155876], [-66.761568, 89.812829, -2.144731], [-66.756476, 89.825277, -2.137343], [-66.762108, 89.834195, -2.148488], [-66.771268, 89.82421, -2.141285], [-66.761568, 89.812829, -2.144731], [-66.752409, 89.822814, -2.151933], [-66.762108, 89.834195, -2.148488], [-66.767201, 89.821747, -2.155876], [-66.761568, 89.812829, -2.144731], [-66.7873, 90.8314, -2.32385]]}, {"shapeName": "R_index_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.682214, 90.895487, -1.830858], [-67.677121, 90.907936, -1.82347], [-67.671489, 90.899017, -1.812325], [-67.676581, 90.886569, -1.819713], [-67.682214, 90.895487, -1.830858], [-67.68628, 90.89795, -1.816268], [-67.671489, 90.899017, -1.812325], [-67.667422, 90.896554, -1.826915], [-67.677121, 90.907936, -1.82347], [-67.68628, 90.89795, -1.816268], [-67.676581, 90.886569, -1.819713], [-67.667422, 90.896554, -1.826915], [-67.682214, 90.895487, -1.830858], [-67.68628, 90.89795, -1.816268], [-66.7873, 90.8314, -2.32385]]}, {"shapeName": "R_index_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-66.290812, 90.99861, -1.444326], [-66.281653, 91.008595, -1.451529], [-66.271954, 90.997214, -1.454974], [-66.281113, 90.987228, -1.447772], [-66.290812, 90.99861, -1.444326], [-66.276021, 90.999677, -1.440385], [-66.271954, 90.997214, -1.454974], [-66.286746, 90.996147, -1.458917], [-66.281653, 91.008595, -1.451529], [-66.276021, 90.999677, -1.440385], [-66.281113, 90.987228, -1.447772], [-66.286746, 90.996147, -1.458917], [-66.290812, 90.99861, -1.444326], [-66.276021, 90.999677, -1.440385], [-66.7873, 90.8314, -2.32385]]}]},
			"L_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_C_CTLShape", "degree": 3, "form": 2, "points": [[57.254973, 93.758886, -3.649146], [56.073778, 94.712762, -2.492916], [56.291655, 96.032943, -1.132173], [57.780979, 96.946084, -0.364022], [59.669322, 96.917282, -0.638434], [60.850517, 95.963406, -1.794663], [60.63264, 94.643225, -3.155406], [59.143316, 93.730084, -3.923557]]}]},
			"L_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_C_CTLShape", "degree": 3, "form": 2, "points": [[65.523902, 92.386026, -5.494151], [67.349423, 92.930522, -5.380273], [68.436536, 93.733637, -4.032994], [68.148421, 94.324919, -2.241529], [66.653857, 94.358003, -1.055294], [64.828337, 93.813507, -1.169173], [63.741224, 93.010392, -2.516451], [64.029338, 92.41911, -4.307916]]}]},
			"L_ring_D_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_ring_D_PIV_CTLShape", "degree": 1, "form": 0, "points": [[68.676398, 89.28079, -10.816365], [68.687307, 89.28072, -10.805573], [68.676526, 89.27994, -10.79468], [68.665617, 89.280009, -10.805473], [68.676398, 89.28079, -10.816365], [68.676816, 89.269529, -10.80595], [68.676526, 89.27994, -10.79468], [68.676109, 89.291202, -10.805096], [68.687307, 89.28072, -10.805573], [68.676816, 89.269529, -10.80595], [68.665617, 89.280009, -10.805473], [68.676109, 89.291202, -10.805096], [68.676398, 89.28079, -10.816365], [68.676816, 89.269529, -10.80595], [68.643116, 90.302699, -10.765232]]}, {"shapeName": "L_ring_D_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[69.666162, 90.336681, -10.780782], [69.665873, 90.347093, -10.769513], [69.66629, 90.335831, -10.759097], [69.66658, 90.325419, -10.770367], [69.666162, 90.336681, -10.780782], [69.67707, 90.336612, -10.76999], [69.66629, 90.335831, -10.759097], [69.655381, 90.3359, -10.76989], [69.665873, 90.347093, -10.769513], [69.67707, 90.336612, -10.76999], [69.66658, 90.325419, -10.770367], [69.655381, 90.3359, -10.76989], [69.666162, 90.336681, -10.780782], [69.67707, 90.336612, -10.76999], [68.643116, 90.302699, -10.765232]]}, {"shapeName": "L_ring_D_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[68.659983, 90.262939, -9.742415], [68.648785, 90.27342, -9.741938], [68.638293, 90.262228, -9.742315], [68.649492, 90.251747, -9.742792], [68.659983, 90.262939, -9.742415], [68.649202, 90.262158, -9.731524], [68.638293, 90.262228, -9.742315], [68.649074, 90.263009, -9.753208], [68.648785, 90.27342, -9.741938], [68.649202, 90.262158, -9.731524], [68.649492, 90.251747, -9.742792], [68.649074, 90.263009, -9.753208], [68.659983, 90.262939, -9.742415], [68.649202, 90.262158, -9.731524], [68.643116, 90.302699, -10.765232]]}]},
			"world_B_OFF_CTL": {"color": 1, "shapes": [{"shapeName": "world_B_OFF_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -46.216], [20.532, 0.0, -25.664], [15.392, 0.0, -25.664], [15.392, 0.0, -15.388], [25.668, 0.0, -15.388], [25.668, 0.0, -20.528], [46.216, 0.0, 0.0], [25.664, 0.0, 20.532], [25.664, 0.0, 15.392], [15.388, 0.0, 15.392], [15.388, 0.0, 25.668], [20.528, 0.0, 25.668], [0.0, 0.0, 46.216], [-20.532, 0.0, 25.664], [-15.392, 0.0, 25.664], [-15.392, 0.0, 15.388], [-25.668, 0.0, 15.388], [-25.668, 0.0, 20.528], [-46.216, 0.0, 0.0], [-25.664, 0.0, -20.532], [-25.664, 0.0, -15.392], [-15.388, 0.0, -15.392], [-15.388, 0.0, -25.668], [-20.528, 0.0, -25.668], [0.0, 0.0, -46.216], [4.024, 0.056, -42.264], [3.672, 0.0, -41.888], [3.672, 0.0, -40.352], [3.352, 0.0, -40.352], [3.372, 0.0, -41.9], [3.144, 0.0, -41.784], [3.152, 0.0, -41.112], [2.828, 0.0, -41.112], [2.828, 0.0, -41.784], [2.628, 0.0, -41.9], [2.628, 0.0, -40.328], [2.304, 0.0, -40.328], [2.304, 0.0, -41.94], [2.564, 0.0, -42.2], [2.964, 0.0, -42.0], [3.404, 0.0, -42.2], [3.672, 0.0, -41.896], [3.404, 0.0, -42.2], [2.968, 0.0, -42.004], [2.564, 0.0, -42.196], [1.784, 0.0, -42.2], [2.048, 0.0, -41.94], [2.048, 0.0, -40.592], [1.784, 0.0, -40.328], [0.94, 0.0, -40.328], [0.68, 0.0, -40.592], [0.68, 0.0, -41.94], [0.94, 0.0, -42.2], [1.784, 0.0, -42.2], [1.684, 0.0, -41.9], [1.724, 0.0, -40.66], [1.0, 0.0, -40.668], [1.004, 0.0, -41.9], [1.688, 0.0, -41.908], [1.784, 0.0, -42.2], [0.94, 0.0, -42.2], [0.4, 0.0, -42.2], [0.42, 0.0, -40.328], [-0.492, 0.0, -40.328], [-0.756, 0.0, -40.592], [-0.756, 0.0, -41.156], [-0.488, 0.0, -41.416], [-0.472, 0.0, -41.436], [-0.996, 0.0, -42.192], [-0.996, 0.0, -42.2], [-0.62, 0.0, -42.2], [-0.096, 0.0, -41.44], [0.1, 0.0, -41.44], [0.1, 0.0, -40.64], [-0.404, 0.0, -40.64], [-0.408, 0.0, -41.116], [0.1, 0.0, -41.116], [0.1, 0.0, -42.2], [0.4, 0.0, -42.2], [-2.572, 0.0, -42.2], [-2.572, 0.0, -41.9], [-1.524, 0.0, -41.896], [-1.524, 0.0, -40.328], [-1.2, 0.0, -40.328], [-1.2, 0.0, -42.2], [-3.936, 0.0, -42.2], [-4.176, 0.0, -41.94], [-4.196, 0.0, -40.592], [-3.936, 0.0, -40.328], [-2.828, 0.0, -40.328], [-2.828, 0.0, -42.2], [-3.156, 0.0, -41.9], [-3.148, 0.0, -40.632], [-3.832, 0.0, -40.632], [-3.824, 0.0, -41.892], [-3.144, 0.0, -41.908], [-2.82, 0.0, -42.2]]}]},
			"L_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_B_CTLShape", "degree": 3, "form": 2, "points": [[60.011269, 98.073127, -5.456479], [60.274695, 99.144311, -3.899193], [59.139891, 99.837566, -2.530403], [57.271607, 99.746789, -2.151928], [55.764258, 98.925159, -2.985471], [55.500833, 97.853974, -4.542757], [56.635636, 97.16072, -5.911548], [58.503921, 97.251497, -6.290022]]}]},
			"L_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_B_CTLShape", "degree": 3, "form": 2, "points": [[62.617445, 96.92863, -14.460768], [64.006868, 98.061157, -15.115638], [65.604509, 98.800865, -14.379198], [66.474491, 98.71444, -12.682839], [66.107193, 97.852512, -11.020269], [64.71777, 96.719984, -10.365399], [63.120129, 95.980277, -11.10184], [62.250147, 96.066701, -12.798198]]}]},
			"R_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_B_CTLShape", "degree": 3, "form": 2, "points": [[-63.563593, 96.142151, -12.219774], [-65.035501, 97.132808, -12.922663], [-66.522973, 98.058838, -12.166447], [-67.154668, 98.377783, -10.394103], [-66.560549, 97.902813, -8.643847], [-65.088641, 96.912156, -7.940958], [-63.601169, 95.986126, -8.697174], [-62.969474, 95.66718, -10.469518]]}]},
			"L_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_thumb_A_CTLShape", "degree": 3, "form": 2, "points": [[59.964694, 100.419503, -8.842455], [60.162092, 101.952274, -7.722804], [58.959863, 103.129659, -6.822594], [57.062253, 103.26196, -6.669156], [55.580857, 102.271681, -7.35237], [55.383459, 100.738911, -8.472021], [56.585688, 99.561525, -9.372231], [58.483298, 99.429224, -9.525669]]}]},
			"R_pinky_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_B_CTLShape", "degree": 3, "form": 2, "points": [[-62.617445, 96.92863, -14.460768], [-64.006868, 98.061157, -15.115638], [-65.604509, 98.800865, -14.379198], [-66.474491, 98.71444, -12.682839], [-66.107193, 97.852512, -11.020269], [-64.71777, 96.719984, -10.365399], [-63.120129, 95.980277, -11.10184], [-62.250147, 96.066701, -12.798198]]}]},
			"R_thumb_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_A_CTLShape", "degree": 3, "form": 2, "points": [[-59.964694, 100.419503, -8.842455], [-60.162092, 101.952274, -7.722804], [-58.959863, 103.129659, -6.822594], [-57.062253, 103.26196, -6.669156], [-55.580857, 102.271681, -7.35237], [-55.383459, 100.738911, -8.472021], [-56.585688, 99.561525, -9.372231], [-58.483298, 99.429224, -9.525669]]}]},
			"L_middle_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[61.755258, 100.483163, -9.294973], [61.760281, 100.492128, -9.283577], [61.749637, 100.486219, -9.274236], [61.744613, 100.477254, -9.285632], [61.755258, 100.483163, -9.294973], [61.759409, 100.47694, -9.281575], [61.749637, 100.486219, -9.274236], [61.745485, 100.492443, -9.287634], [61.760281, 100.492128, -9.283577], [61.759409, 100.47694, -9.281575], [61.744613, 100.477254, -9.285632], [61.745485, 100.492443, -9.287634], [61.755258, 100.483163, -9.294973], [61.759409, 100.47694, -9.281575], [61.095652, 101.216011, -9.570426]]}, {"shapeName": "L_middle_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[61.837531, 101.916115, -9.483878], [61.827758, 101.925395, -9.476539], [61.83191, 101.919171, -9.46314], [61.841682, 101.909891, -9.470479], [61.837531, 101.916115, -9.483878], [61.842554, 101.925079, -9.472482], [61.83191, 101.919171, -9.46314], [61.826886, 101.910205, -9.474536], [61.827758, 101.925395, -9.476539], [61.842554, 101.925079, -9.472482], [61.841682, 101.909891, -9.470479], [61.826886, 101.910205, -9.474536], [61.837531, 101.916115, -9.483878], [61.842554, 101.925079, -9.472482], [61.095652, 101.216011, -9.570426]]}, {"shapeName": "L_middle_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[60.838344, 101.367622, -8.591229], [60.823547, 101.367937, -8.595286], [60.822675, 101.352748, -8.593284], [60.837472, 101.352433, -8.589227], [60.838344, 101.367622, -8.591229], [60.827699, 101.361713, -8.581889], [60.822675, 101.352748, -8.593284], [60.83332, 101.358657, -8.602625], [60.823547, 101.367937, -8.595286], [60.827699, 101.361713, -8.581889], [60.837472, 101.352433, -8.589227], [60.83332, 101.358657, -8.602625], [60.838344, 101.367622, -8.591229], [60.827699, 101.361713, -8.581889], [61.095652, 101.216011, -9.570426]]}]},
			"R_pinky_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-66.427128, 93.760742, -14.092944], [-66.438852, 93.761629, -14.083082], [-66.430315, 93.754791, -14.072319], [-66.418591, 93.753904, -14.082181], [-66.427128, 93.760742, -14.092944], [-66.432268, 93.748073, -14.085976], [-66.430315, 93.754791, -14.072319], [-66.425174, 93.767461, -14.079287], [-66.438852, 93.761629, -14.083082], [-66.432268, 93.748073, -14.085976], [-66.418591, 93.753904, -14.082181], [-66.425174, 93.767461, -14.079287], [-66.427128, 93.760742, -14.092944], [-66.432268, 93.748073, -14.085976], [-66.0941, 94.6723, -13.7671]]}, {"shapeName": "R_pinky_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-67.048194, 95.039629, -13.819944], [-67.046241, 95.046348, -13.806287], [-67.051381, 95.033679, -13.799318], [-67.053335, 95.02696, -13.812976], [-67.048194, 95.039629, -13.819944], [-67.059917, 95.040516, -13.810082], [-67.051381, 95.033679, -13.799318], [-67.039657, 95.032792, -13.80918], [-67.046241, 95.046348, -13.806287], [-67.059917, 95.040516, -13.810082], [-67.053335, 95.02696, -13.812976], [-67.039657, 95.032792, -13.80918], [-67.048194, 95.039629, -13.819944], [-67.059917, 95.040516, -13.810082], [-66.0941, 94.6723, -13.7671]]}, {"shapeName": "R_pinky_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-66.254533, 94.395488, -12.794652], [-66.240856, 94.40132, -12.790856], [-66.234273, 94.387764, -12.79375], [-66.24795, 94.381932, -12.797545], [-66.254533, 94.395488, -12.794652], [-66.245996, 94.388651, -12.783889], [-66.234273, 94.387764, -12.79375], [-66.24281, 94.394601, -12.804514], [-66.240856, 94.40132, -12.790856], [-66.245996, 94.388651, -12.783889], [-66.24795, 94.381932, -12.797545], [-66.24281, 94.394601, -12.804514], [-66.254533, 94.395488, -12.794652], [-66.245996, 94.388651, -12.783889], [-66.0941, 94.6723, -13.7671]]}]},
			"L_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[64.574533, 96.186411, -4.830278], [64.57707, 96.194725, -4.817631], [64.563432, 96.19042, -4.812066], [64.560895, 96.182107, -4.824713], [64.574533, 96.186411, -4.830278], [64.573622, 96.179819, -4.816451], [64.563432, 96.19042, -4.812066], [64.564342, 96.197014, -4.825893], [64.57707, 96.194725, -4.817631], [64.573622, 96.179819, -4.816451], [64.560895, 96.182107, -4.824713], [64.564342, 96.197014, -4.825893], [64.574533, 96.186411, -4.830278], [64.573622, 96.179819, -4.816451], [64.131249, 96.999544, -5.266552]]}, {"shapeName": "L_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[64.899761, 97.592695, -4.941617], [64.88957, 97.603298, -4.937233], [64.88866, 97.596705, -4.923406], [64.89885, 97.586102, -4.92779], [64.899761, 97.592695, -4.941617], [64.902297, 97.601008, -4.928971], [64.88866, 97.596705, -4.923406], [64.886123, 97.588391, -4.936052], [64.88957, 97.603298, -4.937233], [64.902297, 97.601008, -4.928971], [64.89885, 97.586102, -4.92779], [64.886123, 97.588391, -4.936052], [64.899761, 97.592695, -4.941617], [64.902297, 97.601008, -4.928971], [64.131249, 96.999544, -5.266552]]}, {"shapeName": "L_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[63.615712, 97.194963, -4.403967], [63.602984, 97.197252, -4.412229], [63.599537, 97.182346, -4.411049], [63.612264, 97.180056, -4.402787], [63.615712, 97.194963, -4.403967], [63.602074, 97.190659, -4.398403], [63.599537, 97.182346, -4.411049], [63.613175, 97.18665, -4.416614], [63.602984, 97.197252, -4.412229], [63.602074, 97.190659, -4.398403], [63.612264, 97.180056, -4.402787], [63.613175, 97.18665, -4.416614], [63.615712, 97.194963, -4.403967], [63.602074, 97.190659, -4.398403], [64.131249, 96.999544, -5.266552]]}]},
			"L_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[58.051838, 97.656149, -3.663784], [58.03877, 97.658771, -3.656181], [58.031063, 97.650534, -3.666585], [58.044132, 97.647912, -3.674189], [58.051838, 97.656149, -3.663784], [58.04308, 97.644377, -3.659294], [58.031063, 97.650534, -3.666585], [58.039822, 97.662307, -3.671076], [58.03877, 97.658771, -3.656181], [58.04308, 97.644377, -3.659294], [58.044132, 97.647912, -3.674189], [58.039822, 97.662307, -3.671076], [58.051838, 97.656149, -3.663784], [58.04308, 97.644377, -3.659294], [57.887764, 98.499143, -4.220975]]}, {"shapeName": "L_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[57.64519, 99.014167, -3.370135], [57.633174, 99.020325, -3.377427], [57.624415, 99.008552, -3.372936], [57.636432, 99.002394, -3.365644], [57.64519, 99.014167, -3.370135], [57.632122, 99.016788, -3.362532], [57.624415, 99.008552, -3.372936], [57.637484, 99.00593, -3.38054], [57.633174, 99.020325, -3.377427], [57.632122, 99.016788, -3.362532], [57.636432, 99.002394, -3.365644], [57.637484, 99.00593, -3.38054], [57.64519, 99.014167, -3.370135], [57.632122, 99.016788, -3.362532], [57.887764, 98.499143, -4.220975]]}, {"shapeName": "L_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[56.905137, 98.239701, -4.344077], [56.906189, 98.243237, -4.358973], [56.9105, 98.228842, -4.362086], [56.909447, 98.225306, -4.34719], [56.905137, 98.239701, -4.344077], [56.897432, 98.231464, -4.354482], [56.9105, 98.228842, -4.362086], [56.918206, 98.237079, -4.351681], [56.906189, 98.243237, -4.358973], [56.897432, 98.231464, -4.354482], [56.909447, 98.225306, -4.34719], [56.918206, 98.237079, -4.351681], [56.905137, 98.239701, -4.344077], [56.897432, 98.231464, -4.354482], [57.887764, 98.499143, -4.220975]]}]},
			"R_middle_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_B_CTLShape", "degree": 3, "form": 2, "points": [[-64.070188, 95.589202, -9.766374], [-65.71938, 96.435363, -10.220408], [-67.022302, 97.451678, -9.2657], [-67.215717, 98.042805, -7.461503], [-66.186329, 97.862471, -5.864691], [-64.537137, 97.016311, -5.410657], [-63.234216, 95.999995, -6.365364], [-63.0408, 95.408868, -8.169561]]}]},
			"L_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[62.130602, 100.231898, -12.742499], [62.138655, 100.23819, -12.731051], [62.129668, 100.231097, -12.720832], [62.121616, 100.224806, -12.73228], [62.130602, 100.231898, -12.742499], [62.136838, 100.222966, -12.731692], [62.129668, 100.231097, -12.720832], [62.123431, 100.24003, -12.731639], [62.138655, 100.23819, -12.731051], [62.136838, 100.222966, -12.731692], [62.121616, 100.224806, -12.73228], [62.123431, 100.24003, -12.731639], [62.130602, 100.231898, -12.742499], [62.136838, 100.222966, -12.731692], [61.497686, 101.036423, -12.729157]]}, {"shapeName": "L_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[62.301877, 101.668148, -12.682026], [62.294706, 101.676279, -12.671166], [62.300943, 101.667347, -12.660359], [62.308114, 101.659215, -12.671219], [62.301877, 101.668148, -12.682026], [62.309929, 101.674439, -12.670578], [62.300943, 101.667347, -12.660359], [62.292891, 101.661055, -12.671807], [62.294706, 101.676279, -12.671166], [62.309929, 101.674439, -12.670578], [62.308114, 101.659215, -12.671219], [62.292891, 101.661055, -12.671807], [62.301877, 101.668148, -12.682026], [62.309929, 101.674439, -12.670578], [61.497686, 101.036423, -12.729157]]}, {"shapeName": "L_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[61.462174, 101.005333, -11.706517], [61.446951, 101.007174, -11.707105], [61.445135, 100.991949, -11.707746], [61.460359, 100.990109, -11.707158], [61.462174, 101.005333, -11.706517], [61.453188, 100.998241, -11.696299], [61.445135, 100.991949, -11.707746], [61.454122, 100.999042, -11.717965], [61.446951, 101.007174, -11.707105], [61.453188, 100.998241, -11.696299], [61.460359, 100.990109, -11.707158], [61.454122, 100.999042, -11.717965], [61.462174, 101.005333, -11.706517], [61.453188, 100.998241, -11.696299], [61.497686, 101.036423, -12.729157]]}]},
			"world_CTL": {"color": 1, "shapes": [{"shapeName": "world_CTLShape", "degree": 1, "form": 0, "points": [[0.0, 0.0, -57.77], [25.665, 0.0, -32.08], [19.24, 0.0, -32.08], [19.24, 0.0, -19.235], [32.085, 0.0, -19.235], [32.085, 0.0, -25.66], [57.77, 0.0, 0.0], [32.08, 0.0, 25.665], [32.08, 0.0, 19.24], [19.235, 0.0, 19.24], [19.235, 0.0, 32.085], [25.66, 0.0, 32.085], [0.0, 0.0, 57.77], [-25.665, 0.0, 32.08], [-19.24, 0.0, 32.08], [-19.24, 0.0, 19.235], [-32.085, 0.0, 19.235], [-32.085, 0.0, 25.66], [-57.77, 0.0, 0.0], [-32.08, 0.0, -25.665], [-32.08, 0.0, -19.24], [-19.235, 0.0, -19.24], [-19.235, 0.0, -32.085], [-25.66, 0.0, -32.085], [0.0, 0.0, -57.77], [5.03, 0.07, -52.83], [4.59, 0.0, -52.36], [4.59, 0.0, -50.44], [4.19, 0.0, -50.44], [4.215, 0.0, -52.375], [3.93, 0.0, -52.23], [3.94, 0.0, -51.39], [3.535, 0.0, -51.39], [3.535, 0.0, -52.23], [3.285, 0.0, -52.375], [3.285, 0.0, -50.41], [2.88, 0.0, -50.41], [2.88, 0.0, -52.425], [3.205, 0.0, -52.75], [3.705, 0.0, -52.5], [4.255, 0.0, -52.75], [4.59, 0.0, -52.37], [4.255, 0.0, -52.75], [3.71, 0.0, -52.505], [3.205, 0.0, -52.745], [2.23, 0.0, -52.75], [2.56, 0.0, -52.425], [2.56, 0.0, -50.74], [2.23, 0.0, -50.41], [1.175, 0.0, -50.41], [0.85, 0.0, -50.74], [0.85, 0.0, -52.425], [1.175, 0.0, -52.75], [2.23, 0.0, -52.75], [2.105, 0.0, -52.375], [2.155, 0.0, -50.825], [1.25, 0.0, -50.835], [1.255, 0.0, -52.375], [2.11, 0.0, -52.385], [2.23, 0.0, -52.75], [1.175, 0.0, -52.75], [0.5, 0.0, -52.75], [0.525, 0.0, -50.41], [-0.615, 0.0, -50.41], [-0.945, 0.0, -50.74], [-0.945, 0.0, -51.445], [-0.61, 0.0, -51.77], [-0.59, 0.0, -51.795], [-1.245, 0.0, -52.74], [-1.245, 0.0, -52.75], [-0.775, 0.0, -52.75], [-0.12, 0.0, -51.8], [0.125, 0.0, -51.8], [0.125, 0.0, -50.8], [-0.505, 0.0, -50.8], [-0.51, 0.0, -51.395], [0.125, 0.0, -51.395], [0.125, 0.0, -52.75], [0.5, 0.0, -52.75], [-3.215, 0.0, -52.75], [-3.215, 0.0, -52.375], [-1.905, 0.0, -52.37], [-1.905, 0.0, -50.41], [-1.5, 0.0, -50.41], [-1.5, 0.0, -52.75], [-4.92, 0.0, -52.75], [-5.22, 0.0, -52.425], [-5.245, 0.0, -50.74], [-4.92, 0.0, -50.41], [-3.535, 0.0, -50.41], [-3.535, 0.0, -52.75], [-3.945, 0.0, -52.375], [-3.935, 0.0, -50.79], [-4.79, 0.0, -50.79], [-4.78, 0.0, -52.365], [-3.93, 0.0, -52.385], [-3.525, 0.0, -52.75]]}]},
			"R_ring_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_ring_C_CTLShape", "degree": 3, "form": 2, "points": [[-65.896204, 92.620551, -12.401216], [-67.538746, 93.273979, -13.120282], [-69.195998, 93.863686, -12.380193], [-69.897162, 94.044228, -10.614481], [-69.23151, 93.709848, -8.857476], [-67.588968, 93.056419, -8.13841], [-65.931716, 92.466712, -8.878499], [-65.230552, 92.28617, -10.644211]]}]},
			"R_thumb_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_C_CTLShape", "degree": 3, "form": 2, "points": [[-57.254973, 93.758886, -3.649146], [-56.073778, 94.712762, -2.492916], [-56.291655, 96.032943, -1.132173], [-57.780979, 96.946084, -0.364022], [-59.669322, 96.917282, -0.638434], [-60.850517, 95.963406, -1.794663], [-60.63264, 94.643225, -3.155406], [-59.143316, 93.730084, -3.923557]]}]},
			"C_visibility_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "C_visibility_PIV_CTLShape", "degree": 1, "form": 0, "points": [[8.933167, 195.497817, -0.063619], [8.933167, 195.561435, 0.0], [8.933167, 195.497817, 0.063619], [8.933167, 195.434198, 0.0], [8.933167, 195.497817, -0.063619], [8.996779, 195.497817, 0.0], [8.933167, 195.497817, 0.063619], [8.869548, 195.497817, 0.0], [8.933167, 195.561435, 0.0], [8.996779, 195.497817, 0.0], [8.933167, 195.434198, 0.0], [8.869548, 195.497817, 0.0], [8.933167, 195.497817, -0.063619], [8.996779, 195.497817, 0.0], [2.931462, 195.497817, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[2.931462, 201.499522, -0.063619], [2.867843, 201.499522, 0.0], [2.931462, 201.499522, 0.063619], [2.99508, 201.499522, 0.0], [2.931462, 201.499522, -0.063619], [2.931462, 201.563134, 0.0], [2.931462, 201.499522, 0.063619], [2.931462, 201.435903, 0.0], [2.867843, 201.499522, 0.0], [2.931462, 201.563134, 0.0], [2.99508, 201.499522, 0.0], [2.931462, 201.435903, 0.0], [2.931462, 201.499522, -0.063619], [2.931462, 201.563134, 0.0], [2.931462, 195.497817, 0.0]]}, {"shapeName": "C_visibility_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[2.931462, 195.561435, 6.001705], [2.867843, 195.497817, 6.001705], [2.931462, 195.434198, 6.001705], [2.99508, 195.497817, 6.001705], [2.931462, 195.561435, 6.001705], [2.931462, 195.497817, 6.065318], [2.931462, 195.434198, 6.001705], [2.931462, 195.497817, 5.938086], [2.867843, 195.497817, 6.001705], [2.931462, 195.497817, 6.065318], [2.99508, 195.497817, 6.001705], [2.931462, 195.497817, 5.938086], [2.931462, 195.561435, 6.001705], [2.931462, 195.497817, 6.065318], [2.931462, 195.497817, 0.0]]}]},
			"R_index_C_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_C_CTLShape", "degree": 3, "form": 2, "points": [[-65.523902, 92.386026, -5.494151], [-67.349423, 92.930522, -5.380273], [-68.436536, 93.733637, -4.032994], [-68.148421, 94.324919, -2.241529], [-66.653857, 94.358003, -1.055294], [-64.828337, 93.813507, -1.169173], [-63.741224, 93.010392, -2.516451], [-64.029338, 92.41911, -4.307916]]}]},
			"L_index_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_index_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[61.258, 100.758328, -7.976656], [61.259619, 100.768029, -7.964876], [61.246688, 100.762611, -7.958637], [61.245069, 100.752911, -7.970417], [61.258, 100.758328, -7.976656], [61.258073, 100.752986, -7.962272], [61.246688, 100.762611, -7.958637], [61.246615, 100.767954, -7.973022], [61.259619, 100.768029, -7.964876], [61.258073, 100.752986, -7.962272], [61.245069, 100.752911, -7.970417], [61.246615, 100.767954, -7.973022], [61.258, 100.758328, -7.976656], [61.258073, 100.752986, -7.962272], [60.711838, 101.466573, -8.47477]]}, {"shapeName": "L_index_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[61.403839, 102.177534, -8.222404], [61.392454, 102.18716, -8.21877], [61.392528, 102.181816, -8.204385], [61.403913, 102.17219, -8.208019], [61.403839, 102.177534, -8.222404], [61.405458, 102.187233, -8.210624], [61.392528, 102.181816, -8.204385], [61.390908, 102.172116, -8.216165], [61.392454, 102.18716, -8.21877], [61.405458, 102.187233, -8.210624], [61.403913, 102.17219, -8.208019], [61.390908, 102.172116, -8.216165], [61.403839, 102.177534, -8.222404], [61.405458, 102.187233, -8.210624], [60.711838, 101.466573, -8.47477]]}, {"shapeName": "L_index_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[60.185555, 101.676137, -7.622051], [60.17255, 101.676062, -7.630197], [60.171004, 101.661019, -7.627592], [60.184009, 101.661093, -7.619446], [60.185555, 101.676137, -7.622051], [60.172624, 101.670719, -7.615813], [60.171004, 101.661019, -7.627592], [60.183935, 101.666436, -7.633831], [60.17255, 101.676062, -7.630197], [60.172624, 101.670719, -7.615813], [60.184009, 101.661093, -7.619446], [60.183935, 101.666436, -7.633831], [60.185555, 101.676137, -7.622051], [60.172624, 101.670719, -7.615813], [60.711838, 101.466573, -8.47477]]}]},
			"R_index_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_index_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-64.574484, 96.186367, -4.830276], [-64.577021, 96.194681, -4.817629], [-64.563383, 96.190376, -4.812064], [-64.560846, 96.182063, -4.824711], [-64.574484, 96.186367, -4.830276], [-64.573573, 96.179775, -4.816449], [-64.563383, 96.190376, -4.812064], [-64.564293, 96.19697, -4.825891], [-64.577021, 96.194681, -4.817629], [-64.573573, 96.179775, -4.816449], [-64.560846, 96.182063, -4.824711], [-64.564293, 96.19697, -4.825891], [-64.574484, 96.186367, -4.830276], [-64.573573, 96.179775, -4.816449], [-64.1312, 96.9995, -5.26655]]}, {"shapeName": "R_index_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-64.899712, 97.592651, -4.941615], [-64.889521, 97.603254, -4.937231], [-64.888611, 97.596661, -4.923404], [-64.898801, 97.586058, -4.927788], [-64.899712, 97.592651, -4.941615], [-64.902248, 97.600964, -4.928969], [-64.888611, 97.596661, -4.923404], [-64.886074, 97.588347, -4.93605], [-64.889521, 97.603254, -4.937231], [-64.902248, 97.600964, -4.928969], [-64.898801, 97.586058, -4.927788], [-64.886074, 97.588347, -4.93605], [-64.899712, 97.592651, -4.941615], [-64.902248, 97.600964, -4.928969], [-64.1312, 96.9995, -5.26655]]}, {"shapeName": "R_index_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-63.615663, 97.194919, -4.403965], [-63.602935, 97.197208, -4.412227], [-63.599488, 97.182302, -4.411047], [-63.612215, 97.180012, -4.402785], [-63.615663, 97.194919, -4.403965], [-63.602025, 97.190615, -4.398401], [-63.599488, 97.182302, -4.411047], [-63.613126, 97.186606, -4.416612], [-63.602935, 97.197208, -4.412227], [-63.602025, 97.190615, -4.398401], [-63.612215, 97.180012, -4.402785], [-63.613126, 97.186606, -4.416612], [-63.615663, 97.194919, -4.403965], [-63.602025, 97.190615, -4.398401], [-64.1312, 96.9995, -5.26655]]}]},
			"R_pinky_A_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_pinky_A_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-62.130616, 100.231475, -12.742542], [-62.138669, 100.237767, -12.731094], [-62.129682, 100.230674, -12.720875], [-62.12163, 100.224383, -12.732323], [-62.130616, 100.231475, -12.742542], [-62.136852, 100.222543, -12.731735], [-62.129682, 100.230674, -12.720875], [-62.123445, 100.239607, -12.731682], [-62.138669, 100.237767, -12.731094], [-62.136852, 100.222543, -12.731735], [-62.12163, 100.224383, -12.732323], [-62.123445, 100.239607, -12.731682], [-62.130616, 100.231475, -12.742542], [-62.136852, 100.222543, -12.731735], [-61.4977, 101.036, -12.7292]]}, {"shapeName": "R_pinky_A_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-62.301891, 101.667725, -12.682069], [-62.29472, 101.675856, -12.671209], [-62.300957, 101.666924, -12.660402], [-62.308128, 101.658792, -12.671262], [-62.301891, 101.667725, -12.682069], [-62.309943, 101.674016, -12.670621], [-62.300957, 101.666924, -12.660402], [-62.292905, 101.660632, -12.67185], [-62.29472, 101.675856, -12.671209], [-62.309943, 101.674016, -12.670621], [-62.308128, 101.658792, -12.671262], [-62.292905, 101.660632, -12.67185], [-62.301891, 101.667725, -12.682069], [-62.309943, 101.674016, -12.670621], [-61.4977, 101.036, -12.7292]]}, {"shapeName": "R_pinky_A_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-61.462188, 101.00491, -11.70656], [-61.446965, 101.006751, -11.707148], [-61.445149, 100.991526, -11.707789], [-61.460373, 100.989686, -11.707201], [-61.462188, 101.00491, -11.70656], [-61.453202, 100.997818, -11.696342], [-61.445149, 100.991526, -11.707789], [-61.454136, 100.998619, -11.718008], [-61.446965, 101.006751, -11.707148], [-61.453202, 100.997818, -11.696342], [-61.460373, 100.989686, -11.707201], [-61.454136, 100.998619, -11.718008], [-61.462188, 101.00491, -11.70656], [-61.453202, 100.997818, -11.696342], [-61.4977, 101.036, -12.7292]]}]},
			"L_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[67.673388, 91.963672, -6.651065], [67.681043, 91.968367, -6.638621], [67.668609, 91.965796, -6.630002], [67.660954, 91.961101, -6.642446], [67.673388, 91.963672, -6.651065], [67.674337, 91.954565, -6.63875], [67.668609, 91.965796, -6.630002], [67.667659, 91.974903, -6.642317], [67.681043, 91.968367, -6.638621], [67.674337, 91.954565, -6.63875], [67.660954, 91.961101, -6.642446], [67.667659, 91.974903, -6.642317], [67.673388, 91.963672, -6.651065], [67.674337, 91.954565, -6.63875], [67.35601, 92.924101, -6.808754]]}, {"shapeName": "L_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[68.305962, 93.265787, -6.63887], [68.300234, 93.277019, -6.630122], [68.301184, 93.267912, -6.617808], [68.306912, 93.25668, -6.626556], [68.305962, 93.265787, -6.63887], [68.313616, 93.270482, -6.626427], [68.301184, 93.267912, -6.617808], [68.293529, 93.263216, -6.630251], [68.300234, 93.277019, -6.630122], [68.313616, 93.270482, -6.626427], [68.306912, 93.25668, -6.626556], [68.293529, 93.263216, -6.630251], [68.305962, 93.265787, -6.63887], [68.313616, 93.270482, -6.626427], [67.35601, 92.924101, -6.808754]]}, {"shapeName": "L_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[67.140648, 93.027934, -5.813335], [67.127265, 93.03447, -5.817031], [67.120559, 93.020667, -5.81716], [67.133942, 93.014131, -5.813465], [67.140648, 93.027934, -5.813335], [67.128214, 93.025363, -5.804717], [67.120559, 93.020667, -5.81716], [67.132993, 93.023238, -5.825779], [67.127265, 93.03447, -5.817031], [67.128214, 93.025363, -5.804717], [67.133942, 93.014131, -5.813465], [67.132993, 93.023238, -5.825779], [67.140648, 93.027934, -5.813335], [67.128214, 93.025363, -5.804717], [67.35601, 92.924101, -6.808754]]}]},
			"L_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[1.273671, 1.0, -0.010851], [1.273671, 1.010851, 0.0], [1.273671, 1.0, 0.010851], [1.273671, 0.989149, 0.0], [1.273671, 1.0, -0.010851], [1.284521, 1.0, 0.0], [1.273671, 1.0, 0.010851], [1.26282, 1.0, 0.0], [1.273671, 1.010851, 0.0], [1.284521, 1.0, 0.0], [1.273671, 0.989149, 0.0], [1.26282, 1.0, 0.0], [1.273671, 1.0, -0.010851], [1.284521, 1.0, 0.0], [0.25, 1.0, 0.0]]}, {"shapeName": "L_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[0.25, 2.023671, -0.010851], [0.239149, 2.023671, 0.0], [0.25, 2.023671, 0.010851], [0.260851, 2.023671, 0.0], [0.25, 2.023671, -0.010851], [0.25, 2.034521, 0.0], [0.25, 2.023671, 0.010851], [0.25, 2.01282, 0.0], [0.239149, 2.023671, 0.0], [0.25, 2.034521, 0.0], [0.260851, 2.023671, 0.0], [0.25, 2.01282, 0.0], [0.25, 2.023671, -0.010851], [0.25, 2.034521, 0.0], [0.25, 1.0, 0.0]]}, {"shapeName": "L_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[0.25, 1.010851, 1.023671], [0.239149, 1.0, 1.023671], [0.25, 0.989149, 1.023671], [0.260851, 1.0, 1.023671], [0.25, 1.010851, 1.023671], [0.25, 1.0, 1.034521], [0.25, 0.989149, 1.023671], [0.25, 1.0, 1.01282], [0.239149, 1.0, 1.023671], [0.25, 1.0, 1.034521], [0.260851, 1.0, 1.023671], [0.25, 1.0, 1.01282], [0.25, 1.010851, 1.023671], [0.25, 1.0, 1.034521], [0.25, 1.0, 0.0]]}]},
			"L_pinky_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_pinky_C_CTLShape", "degree": 3, "form": 2, "points": [[64.189172, 94.528222, -15.369571], [65.727978, 95.356009, -16.136913], [67.481244, 95.783318, -15.516078], [68.421929, 95.559836, -13.87074], [67.998995, 94.816477, -12.164717], [66.460189, 93.988691, -11.397376], [64.706924, 93.561381, -12.01821], [63.766239, 93.784863, -13.663548]]}]},
			"L_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_B_CTLShape", "degree": 3, "form": 2, "points": [[63.719029, 95.648757, -7.321468], [65.406685, 96.538913, -7.358993], [66.34721, 97.698899, -6.170795], [65.989653, 98.449212, -4.452903], [64.54347, 98.350331, -3.211635], [62.855814, 97.460175, -3.174111], [61.915289, 96.300189, -4.362308], [62.272846, 95.549875, -6.0802]]}]},
			"R_pinky_D_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_D_CTLShape", "degree": 3, "form": 2, "points": [[-64.926715, 92.602506, -16.031811], [-66.542621, 93.111811, -16.910119], [-68.379885, 93.212182, -16.403804], [-69.362262, 92.844822, -14.809454], [-68.914292, 92.224926, -13.06102], [-67.298386, 91.71562, -12.182712], [-65.461122, 91.615249, -12.689027], [-64.478745, 91.98261, -14.283377]]}]},
			"R_hand_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_hand_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-1.273671, 1.0, -0.010851], [-1.273671, 1.010851, 0.0], [-1.273671, 1.0, 0.010851], [-1.273671, 0.989149, -0.0], [-1.273671, 1.0, -0.010851], [-1.284521, 1.0, 0.0], [-1.273671, 1.0, 0.010851], [-1.26282, 1.0, 0.0], [-1.273671, 1.010851, 0.0], [-1.284521, 1.0, 0.0], [-1.273671, 0.989149, -0.0], [-1.26282, 1.0, 0.0], [-1.273671, 1.0, -0.010851], [-1.284521, 1.0, 0.0], [-0.25, 1.0, 0.0]]}, {"shapeName": "R_hand_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-0.25, 2.023671, -0.010851], [-0.239149, 2.023671, 0.0], [-0.25, 2.023671, 0.010851], [-0.260851, 2.023671, 0.0], [-0.25, 2.023671, -0.010851], [-0.25, 2.034521, 0.0], [-0.25, 2.023671, 0.010851], [-0.25, 2.01282, 0.0], [-0.239149, 2.023671, 0.0], [-0.25, 2.034521, 0.0], [-0.260851, 2.023671, 0.0], [-0.25, 2.01282, 0.0], [-0.25, 2.023671, -0.010851], [-0.25, 2.034521, 0.0], [-0.25, 1.0, 0.0]]}, {"shapeName": "R_hand_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-0.25, 1.010851, 1.023671], [-0.239149, 1.0, 1.023671], [-0.25, 0.989149, 1.023671], [-0.260851, 1.0, 1.023671], [-0.25, 1.010851, 1.023671], [-0.25, 1.0, 1.034521], [-0.25, 0.989149, 1.023671], [-0.25, 1.0, 1.01282], [-0.239149, 1.0, 1.023671], [-0.25, 1.0, 1.034521], [-0.260851, 1.0, 1.023671], [-0.25, 1.0, 1.01282], [-0.25, 1.010851, 1.023671], [-0.25, 1.0, 1.034521], [-0.25, 1.0, 0.0]]}]},
			"L_ring_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_ring_B_CTLShape", "degree": 3, "form": 2, "points": [[63.563593, 96.142151, -12.219774], [65.035501, 97.132808, -12.922663], [66.522973, 98.058838, -12.166447], [67.154668, 98.377783, -10.394103], [66.560549, 97.902813, -8.643847], [65.088641, 96.912156, -7.940958], [63.601169, 95.986126, -8.697174], [62.969474, 95.66718, -10.469518]]}]},
			"R_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_middle_C_CTLShape", "degree": 3, "form": 2, "points": [[-66.112197, 92.161188, -8.830666], [-67.905049, 92.680039, -9.228716], [-69.376282, 93.341857, -8.209187], [-69.664065, 93.75896, -6.369303], [-68.599822, 93.687014, -4.786842], [-66.80697, 93.168164, -4.388792], [-65.335737, 92.506346, -5.408321], [-65.047954, 92.089243, -7.248205]]}]},
			"R_thumb_B_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_thumb_B_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-58.051874, 97.656106, -3.663789], [-58.038806, 97.658728, -3.656186], [-58.031099, 97.650491, -3.66659], [-58.044168, 97.647869, -3.674194], [-58.051874, 97.656106, -3.663789], [-58.043116, 97.644334, -3.659299], [-58.031099, 97.650491, -3.66659], [-58.039858, 97.662264, -3.671081], [-58.038806, 97.658728, -3.656186], [-58.043116, 97.644334, -3.659299], [-58.044168, 97.647869, -3.674194], [-58.039858, 97.662264, -3.671081], [-58.051874, 97.656106, -3.663789], [-58.043116, 97.644334, -3.659299], [-57.8878, 98.4991, -4.22098]]}, {"shapeName": "R_thumb_B_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-57.645226, 99.014124, -3.37014], [-57.63321, 99.020282, -3.377432], [-57.624451, 99.008509, -3.372941], [-57.636468, 99.002351, -3.365649], [-57.645226, 99.014124, -3.37014], [-57.632158, 99.016745, -3.362537], [-57.624451, 99.008509, -3.372941], [-57.63752, 99.005887, -3.380545], [-57.63321, 99.020282, -3.377432], [-57.632158, 99.016745, -3.362537], [-57.636468, 99.002351, -3.365649], [-57.63752, 99.005887, -3.380545], [-57.645226, 99.014124, -3.37014], [-57.632158, 99.016745, -3.362537], [-57.8878, 98.4991, -4.22098]]}, {"shapeName": "R_thumb_B_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-56.905173, 98.239658, -4.344082], [-56.906225, 98.243194, -4.358978], [-56.910536, 98.228799, -4.362091], [-56.909483, 98.225263, -4.347195], [-56.905173, 98.239658, -4.344082], [-56.897468, 98.231421, -4.354487], [-56.910536, 98.228799, -4.362091], [-56.918242, 98.237036, -4.351686], [-56.906225, 98.243194, -4.358978], [-56.897468, 98.231421, -4.354487], [-56.909483, 98.225263, -4.347195], [-56.918242, 98.237036, -4.351686], [-56.905173, 98.239658, -4.344082], [-56.897468, 98.231421, -4.354487], [-57.8878, 98.4991, -4.22098]]}]},
			"R_pinky_A_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_pinky_A_CTLShape", "degree": 3, "form": 2, "points": [[-60.189224, 100.01413, -14.589285], [-61.604937, 101.12845, -15.218585], [-62.957823, 102.188862, -14.389614], [-63.45538, 102.574189, -12.587968], [-62.806148, 102.058716, -10.869028], [-61.390436, 100.944396, -10.239728], [-60.037549, 99.883984, -11.0687], [-59.539992, 99.498656, -12.870346]]}]},
			"L_middle_C_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "L_middle_C_CTLShape", "degree": 3, "form": 2, "points": [[66.112197, 92.161188, -8.830666], [67.905049, 92.680039, -9.228716], [69.376282, 93.341857, -8.209187], [69.664065, 93.75896, -6.369303], [68.599822, 93.687014, -4.786842], [66.80697, 93.168164, -4.388792], [65.335737, 92.506346, -5.408321], [65.047954, 92.089243, -7.248205]]}]},
			"L_thumb_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "L_thumb_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[58.360944, 96.074407, -2.847783], [58.368373, 96.084126, -2.838518], [58.381731, 96.079849, -2.844744], [58.374302, 96.07013, -2.854009], [58.360944, 96.074407, -2.847783], [58.370375, 96.084961, -2.853709], [58.381731, 96.079849, -2.844744], [58.3723, 96.069294, -2.838817], [58.368373, 96.084126, -2.838518], [58.370375, 96.084961, -2.853709], [58.374302, 96.07013, -2.854009], [58.3723, 96.069294, -2.838817], [58.360944, 96.074407, -2.847783], [58.370375, 96.084961, -2.853709], [58.462148, 95.338084, -2.14379]]}, {"shapeName": "L_thumb_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[58.172103, 95.995521, -1.414632], [58.183459, 95.990408, -1.405667], [58.19289, 96.000964, -1.411594], [58.181534, 96.006076, -1.420559], [58.172103, 95.995521, -1.414632], [58.179532, 96.005239, -1.405368], [58.19289, 96.000964, -1.411594], [58.185461, 95.991245, -1.420858], [58.183459, 95.990408, -1.405667], [58.179532, 96.005239, -1.405368], [58.181534, 96.006076, -1.420559], [58.185461, 95.991245, -1.420858], [58.172103, 95.995521, -1.414632], [58.179532, 96.005239, -1.405368], [58.462148, 95.338084, -2.14379]]}, {"shapeName": "L_thumb_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[59.439719, 95.601805, -1.992712], [59.443646, 95.586974, -1.993011], [59.445648, 95.58781, -2.008202], [59.441721, 95.602642, -2.007904], [59.439719, 95.601805, -1.992712], [59.453077, 95.597529, -1.998938], [59.445648, 95.58781, -2.008202], [59.43229, 95.592086, -2.001977], [59.443646, 95.586974, -1.993011], [59.453077, 95.597529, -1.998938], [59.441721, 95.602642, -2.007904], [59.43229, 95.592086, -2.001977], [59.439719, 95.601805, -1.992712], [59.453077, 95.597529, -1.998938], [58.462148, 95.338084, -2.14379]]}]},
			"R_index_B_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "R_index_B_CTLShape", "degree": 3, "form": 2, "points": [[-63.719029, 95.648757, -7.321468], [-65.406685, 96.538913, -7.358993], [-66.34721, 97.698899, -6.170795], [-65.989653, 98.449212, -4.452903], [-64.54347, 98.350331, -3.211635], [-62.855814, 97.460175, -3.174111], [-61.915289, 96.300189, -4.362308], [-62.272846, 95.549875, -6.0802]]}]},
			"L_index_D_CTL": {"color": [0.0, 0.120646, 0.935], "shapes": [{"shapeName": "L_index_D_CTLShape", "degree": 3, "form": 2, "points": [[66.126593, 90.431183, -4.694599], [68.019651, 90.425811, -4.453204], [69.190845, 90.658024, -2.964462], [68.954101, 90.991796, -1.100456], [67.448106, 91.231608, 0.046905], [65.555048, 91.23698, -0.19449], [64.383855, 91.004767, -1.683231], [64.620598, 90.670995, -3.547237]]}]},
			"R_middle_C_PIV_CTL": {"color": 13, "shapes": [{"shapeName": "R_middle_C_PIV_CTLShape", "degree": 1, "form": 0, "points": [[-67.673378, 91.963671, -6.651061], [-67.681033, 91.968366, -6.638617], [-67.668599, 91.965795, -6.629998], [-67.660944, 91.9611, -6.642442], [-67.673378, 91.963671, -6.651061], [-67.674327, 91.954564, -6.638746], [-67.668599, 91.965795, -6.629998], [-67.667649, 91.974902, -6.642313], [-67.681033, 91.968366, -6.638617], [-67.674327, 91.954564, -6.638746], [-67.660944, 91.9611, -6.642442], [-67.667649, 91.974902, -6.642313], [-67.673378, 91.963671, -6.651061], [-67.674327, 91.954564, -6.638746], [-67.356, 92.9241, -6.80875]]}, {"shapeName": "R_middle_C_PIV_CTLShape1", "degree": 1, "form": 0, "points": [[-68.305952, 93.265786, -6.638866], [-68.300224, 93.277018, -6.630118], [-68.301174, 93.267911, -6.617804], [-68.306902, 93.256679, -6.626552], [-68.305952, 93.265786, -6.638866], [-68.313606, 93.270481, -6.626423], [-68.301174, 93.267911, -6.617804], [-68.293519, 93.263215, -6.630247], [-68.300224, 93.277018, -6.630118], [-68.313606, 93.270481, -6.626423], [-68.306902, 93.256679, -6.626552], [-68.293519, 93.263215, -6.630247], [-68.305952, 93.265786, -6.638866], [-68.313606, 93.270481, -6.626423], [-67.356, 92.9241, -6.80875]]}, {"shapeName": "R_middle_C_PIV_CTLShape2", "degree": 1, "form": 0, "points": [[-67.140638, 93.027933, -5.813331], [-67.127255, 93.034469, -5.817027], [-67.120549, 93.020666, -5.817156], [-67.133932, 93.01413, -5.813461], [-67.140638, 93.027933, -5.813331], [-67.128204, 93.025362, -5.804713], [-67.120549, 93.020666, -5.817156], [-67.132983, 93.023237, -5.825775], [-67.127255, 93.034469, -5.817027], [-67.128204, 93.025362, -5.804713], [-67.133932, 93.01413, -5.813461], [-67.132983, 93.023237, -5.825775], [-67.140638, 93.027933, -5.813331], [-67.128204, 93.025362, -5.804713], [-67.356, 92.9241, -6.80875]]}]},
			"R_thumb_B_CTL": {"color": [0.0, 0.4435, 1.0], "shapes": [{"shapeName": "R_thumb_B_CTLShape", "degree": 3, "form": 2, "points": [[-60.011269, 98.073127, -5.456479], [-60.274695, 99.144311, -3.899193], [-59.139891, 99.837566, -2.530403], [-57.271607, 99.746789, -2.151928], [-55.764258, 98.925159, -2.985471], [-55.500833, 97.853974, -4.542757], [-56.635636, 97.16072, -5.911548], [-58.503921, 97.251497, -6.290022]]}]},
		}

		controlShapes.set_data(data)