"""
    setupHandPoses

    Original code by Juan Carlos Leon

    refactored by Jennifer Lynn Hachigian

    This code will build hand controls that can apply prefabricated pose data for the hands via Set Driven Key.
"""

import pymel.core as pm

import sys
p = r"C:\Users\Nicob\Documents\ENCORE\aoutils\riggingTools"
if p not in sys.path:
	sys.path.insert(0, p)
import ao_PresetBuilder as presetBuilder
reload(presetBuilder)

import tools
reload(tools)


PALM_CTRL = [
    (0.496016, 0.743892, 0), (0.490448, 0.744882, 0), (0.484703, 0.745108, 0),
    (0.479258, 0.744982, 0), (0.473841, 0.745099, 0), (0.470207, 0.745374, 0),
    (0.467365, 0.747236, 0), (0.464995,  0.75157, 0), (0.462455, 0.757201, 0),
    (0.460426, 0.763485, 0), (0.458516, 0.772392, 0), (0.457567, 0.781418, 0),
    (0.457143, 0.788444, 0), (0.457016, 0.793969, 0), (0.456409, 0.797469, 0),
    (0.455767, 0.801756, 0), (0.454488, 0.806505, 0), (0.453685,  0.81075, 0),
    (0.452829, 0.814189, 0), (0.45154, 0.818238, 0), (0.450162, 0.823467, 0),
    (0.450136, 0.827513, 0), (0.451783, 0.830714, 0), (0.453744, 0.83134,  0),
    (0.456336, 0.830154, 0), (0.457316, 0.827076, 0), (0.458481, 0.823106, 0),
    (0.46002, 0.819208, 0), (0.46157, 0.815144, 0), (0.463184, 0.810215, 0),
    (0.465046, 0.806213, 0), (0.4667, 0.804531, 0), (0.467468, 0.804399, 0),
    (0.468745, 0.806887, 0), (0.468884, 0.810477, 0), (0.467955, 0.814621, 0),
    (0.467365, 0.817386, 0), (0.46694, 0.821574, 0), (0.46663,  0.82536, 0),
    (0.465977, 0.829334, 0), (0.465543, 0.832708, 0), (0.465114, 0.835578, 0),
    (0.464277, 0.839785, 0), (0.463573, 0.843118, 0), (0.463274, 0.846349, 0),
    (0.464253, 0.849331, 0), (0.466167, 0.851263, 0), (0.468964, 0.851363, 0),
    (0.471354, 0.849914, 0), (0.472565, 0.846715, 0), (0.473329, 0.842945, 0),
    (0.474074, 0.839604, 0), (0.475001,  0.83567, 0), (0.475838, 0.832021, 0),
    (0.476462, 0.828539, 0), (0.47694, 0.824777, 0), (0.477937, 0.820315, 0),
    (0.478674, 0.817279, 0), (0.479277, 0.813712, 0), (0.481118, 0.810931, 0),
    (0.48236, 0.812815, 0), (0.483098, 0.817766, 0), (0.483262, 0.821489, 0),
    (0.483145, 0.826311, 0), (0.483351, 0.830603, 0), (0.483588, 0.834373, 0),
    (0.483616, 0.838724, 0), (0.4834, 0.842851, 0), (0.483411, 0.848711, 0),
    (0.48357, 0.852981, 0), (0.484149, 0.856618, 0), (0.486285, 0.858162, 0),
    (0.489095, 0.858989, 0), (0.491583, 0.858149, 0), (0.492873, 0.855533, 0),
    (0.493209, 0.851223, 0), (0.493521, 0.846952, 0), (0.493693, 0.843407, 0),
    (0.493384, 0.838771, 0), (0.493337, 0.834516, 0), (0.493926, 0.829954, 0),
    (0.4943, 0.827716, 0), (0.4942, 0.824694, 0), (0.494353, 0.821312, 0),
    (0.494625, 0.817216, 0), (0.494866, 0.812323, 0), (0.49546,   0.8112, 0),
    (0.49691, 0.812554, 0), (0.4976, 0.815952, 0), (0.498571, 0.820428, 0),
    (0.499795, 0.825708, 0), (0.500618, 0.830302, 0), (0.501471, 0.834369, 0),
    (0.502756, 0.838161, 0), (0.50414, 0.842664, 0), (0.50523, 0.847336, 0),
    (0.506375, 0.850928, 0), (0.507683, 0.853759, 0), (0.509811, 0.855917, 0),
    (0.511432, 0.855566, 0), (0.514292,  0.85371, 0), (0.515326, 0.849446, 0),
    (0.514679, 0.845173, 0), (0.51416, 0.842242, 0), (0.513704,  0.83859, 0),
    (0.513009, 0.834712, 0), (0.511638, 0.830471, 0), (0.511039, 0.827772, 0),
    (0.510754, 0.822941, 0), (0.510585, 0.819808, 0), (0.509903, 0.815826, 0),
    (0.509308, 0.812231, 0), (0.509023,  0.80825, 0), (0.508531, 0.802237, 0),
    (0.509068, 0.793636, 0), (0.510108, 0.789218, 0), (0.511767, 0.786416, 0),
    (0.513883, 0.783382, 0), (0.515621, 0.787081, 0), (0.518401, 0.791213, 0),
    (0.51985,  0.79417, 0), (0.52052, 0.797528, 0), (0.522166,  0.80093, 0),
    (0.524856, 0.804373, 0), (0.528443, 0.806949, 0), (0.53098, 0.807719, 0),
    (0.533434, 0.806168, 0), (0.533869, 0.803724, 0), (0.533239, 0.799584, 0),
    (0.531905,  0.79692, 0), (0.53172, 0.794506, 0), (0.53163, 0.789865, 0),
    (0.530169, 0.787024, 0), (0.528384, 0.784734, 0), (0.527885, 0.782537, 0),
    (0.527502, 0.779713, 0), (0.525761, 0.775229, 0), (0.523534, 0.765565, 0),
    (0.520817, 0.760774, 0), (0.517286, 0.755354, 0), (0.513798, 0.750634, 0),
    (0.511052, 0.747152, 0), (0.506145, 0.744444, 0), (0.501653, 0.743581, 0),
    (0.496095, 0.743885, 0)]

# pose data for frame 100
fist_dict = {"index": {"01": {"rotateX": -7,
                              "rotateY": 5}},
             "middle": {"01": {"rotateY": 9}},
             "ring": {"01": {"rotateY": 9}},
             "pinky": {"01": {"rotateX": 6,
                              "rotateY": 3}},
             "thumb": {"Carpal": {"rotateX": -15,
                                  "rotateY": -9,
                                  "rotateZ": -25},
                       "01": {"rotateX": 0,
                              "rotateY": 0,
                              "rotateZ": -25},
                       "02": {"rotateX": 0,
                              "rotateY": 0,
                              "rotateZ": -103}}
             }

# additional data for fist_dict
for k in ["index", "middle", "ring", "pinky"]:
    for n in ["01", "02", "03"]:
        if n not in fist_dict[k]:
            fist_dict[k][n] = {}
        fist_dict[k][n]["rotateZ"] = -90

# pose data for value 100
splay_dict1 = {"index": {"Carpal": {"rotateZ": 5},
                         "01": {"rotateZ": 50},
                         "02": {"rotateZ": 10}},
               "middle": {"Carpal": {"rotateZ": 5},
                          "01": {"rotateZ": 20}},
               "ring": {"Carpal": {"rotateZ": -5},
                        "01": {"rotateZ": -25}},
               "pinky": {"Carpal": {"rotateZ": -5},
                         "01": {"rotateZ": -75}},
               "thumb": {"Carpal": {"rotateZ": -25}}
               }

# for value -100
splay_dict2 = {"index": {"Carpal": {"rotateY": -5,
                                    "rotateZ": -5},
                         "01": {"rotateZ": -60},
                         "02": {"rotateZ": -20}},
               "middle": {"01": {"rotateZ": -45},
                          "02": {"rotateZ": 5},
                          "03": {"rotateZ": 5}},
               "ring": {"Carpal": {"rotateZ": 5}},
               "pinky": {"Carpal": {"rotateZ": 15},
                         "01": {"rotateZ": 30}},
               "thumb": {"Carpal": {"rotateZ": 10},
                         "01": {"rotateZ": 10},
                         "02": {"rotateZ": 10}}
               }

# 100
spread_dict1 = {"index": {"01": {"rotateY": -10}},
                "ring": {"01": {"rotateY": 10}},
                "pinky": {"01": {"rotateY": 10}},
                }

# -100
spread_dict2 = {"index": {"Carpal": {"rotateY": 3},
                          "01": {"rotateX": 2,
                                 "rotateY": 15,
                                 "rotateZ": 5},
                          "02": {"rotateZ": 3}},
                "ring": {"01": {"rotateY": -20}},
                "pinky": {"Carpal": {"rotateY": -3},
                          "01": {"rotateY": -35}},
                "thumb": {"Carpal": {"rotateX": 10,
                                     "rotateY": 15,
                                     "rotateZ": -20},
                          "01": {"rotateZ": -30},
                          "02": {"rotateZ": -10}}
                }

grip_dict = {"index": {"01": {"rotateY": 21},
                       "02": {"rotateZ": -32},
                       "03": {"rotateZ": -32}},
             "middle": {"01": {"rotateZ": -22},
                        "02": {"rotateZ": -60},
                        "03": {"rotateZ": -60}},
             "ring": {"01": {"rotateY": -15,
                             "rotateZ": -45},
                      "02": {"rotateZ": -66},
                      "03": {"rotateZ": -45}},
             "pinky": {"Carpal": {"rotateX": -5,
                                  "rotateY": -0.2,
                                  "rotateZ": -2},
                       "01": {"rotateY": -12,
                              "rotateZ": -66},
                       "02": {"rotateZ": -69},
                       "03": {"rotateZ": -35}},
             "thumb": {"Carpal": {"rotateX": 30,
                                  "rotateY": -10,
                                  "rotateZ": -35},
                       "01": {"rotateZ": -15},
                       "02": {"rotateZ": -25}}
             }

claw_dict = {"index": {"01": {"rotateX": 5,
                              "rotateY": -10,
                              "rotateZ": 30},
                       "02": {"rotateZ": -50},
                       "03": {"rotateZ": -40}},
             "middle": {"01": {"rotateZ": 10},
                        "02": {"rotateZ": -45},
                        "03": {"rotateZ": -45}},
             "ring": {"01": {"rotateX": -10,
                             "rotateY": 12,
                             "rotateZ": 10},
                      "02": {"rotateZ": -45},
                      "03": {"rotateZ": -45}},
             "pinky": {"01": {"rotateX": -20,
                              "rotateY": 15,
                              "rotateZ": -30},
                       "02": {"rotateZ": -30},
                       "03": {"rotateZ": -30}},
             "thumb": {"Carpal": {"rotateX": -1,
                                  "rotateY": -10,
                                  "rotateZ": 5},
                       "01": {"rotateZ": 0.2},
                       "02": {"rotateZ": -45}}
             }

ape_dict = {"index": {"01": {"rotateX": 5,
                             "rotateY": 20,
                             "rotateZ": 15},
                      "02": {"rotateZ": -90},
                      "03": {"rotateX": 20,
                             "rotateY": 20,
                             "rotateZ": -110}},
            "middle": {"01": {"rotateZ": 16},
                       "02": {"rotateZ": -101},
                       "03": {"rotateX": 33,
                              "rotateY": 1,
                              "rotateZ": -110}},
            "ring": {"01": {"rotateX": -5,
                            "rotateY": -15,
                            "rotateZ": 16},
                     "02": {"rotateZ": -90},
                     "03": {"rotateZ": -90}},
            "pinky": {"01": {"rotateX": 10,
                             "rotateY": -20,
                             "rotateZ": -20},
                      "02": {"rotateZ": -60},
                      "03": {"rotateZ": -60}},
            "thumb": {"Carpal": {"rotateX": 10,
                                 "rotateY": 2,
                                 "rotateZ": -10},
                      "01": {"rotateZ": -31},
                      "02": {"rotateZ": -15}}
            }

pose_data = {"fist": {100: fist_dict},
             "splay": {100: splay_dict1, -100: splay_dict2},
             "spread": {100: spread_dict1, -100: spread_dict2},
             "grip": {100: grip_dict},
             "claw": {100: claw_dict},
             "ape": {100: ape_dict}}

handCtrls = ['fingerPoses_Lt_anim', 'fingerPoses_Rt_anim']


def make_hand_controls():
    """
    Uses the data in PALM_CTRL to build little "hand" shapes, one for each of the names in handCtrls.
    :return: None
    """
    for handCtrl in handCtrls:
        pm.curve(name=handCtrl, d=1, p=PALM_CTRL)
        pm.xform(relative=True, centerPivots=True)
        d = {'splay': -100, 'fist': -100, 'spread': -100, 'claw': -100, 'ape': -100, 'grip': -100}
        for name in ['splay', 'fist', 'spread', 'claw', 'ape', 'grip']:
            pm.addAttr(handCtrl, keyable=True, min=d[name], max=100, longName=name)
        grp_name = tools.get_new_name(handCtrl, 'grp')
        pm.group(empty=True, name=grp_name)
        tools.match_to(handCtrl, grp_name)
        pm.parent(handCtrl, grp_name)
        pm.scale(handCtrl, (70, 70, 70))
        pm.makeIdentity(handCtrl, apply=True, translate=True, rotate=True, scale=True)

        # hide unused attributes on the hand control.
        hnd = pm.PyNode(handCtrl)
        for attr in ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']:
            hnd.setAttr(attr, lock=True, keyable=False, channelBox=False)

    sides = ['Lt', 'Rt']

    for i in range(0, 2):
        cont = pm.parentConstraint('handEnd_' + sides[i] + '_jnt', 'fingerPoses_' + sides[i] + '_grp')
        pm.delete(cont)
        pm.parentConstraint('handEnd_' + sides[i] + '_jnt', 'fingerPoses_' + sides[i] + '_grp')
        pm.parent('fingerPoses_' + sides[i] + '_grp', 'character_Mid_anim')

    pm.select(handCtrls[0] + '.cv[0:144]')
    pm.move(0, 10, 0, r=True, os=True, worldSpaceDistance=True)
    pm.select(cl=1)

    pm.select(handCtrls[1] + '.cv[0:144]')
    pm.rotate(180, 0, 0, r=True, os=True)
    pm.move(0, -10, 0, r=True, os=True, worldSpaceDistance=True)

    pm.select(clear=True)


def set_attr(d, key):
    for sd in ["Lt", "Rt"]:
        for a in d:
            for b in d[a]:
                for attr in d[a][b]:
                    name = "%s%s_%s_%s_sdk" % (a, b, sd, key)
                    node = pm.PyNode(name)
                    node.setAttr(attr, d[a][b][attr])


####################################################

# controls have been built and position where they
# need to be, next goal is  linking the attributes
# to their correct animation.
# create finger sdk groups

###################################################


fin = ['index', 'middle', 'ring', 'pinky', 'thumb']
ger = ['Carpal_', '01_', '02_', '03_']
side = ['Lt_', 'Rt_']
sdk = ['splay_sdk', 'fist_sdk', 'spread_sdk', 'claw_sdk', 'ape_sdk', 'grip_sdk']


# creates all the carpel group nodes.
def build_hierarchy():
    """
    Creates six transforms for each finger anim, using the data in fin, ger, side and sdk.
    :return: None
    """
    for sd in side:
        for s in sdk:
            for f in fin:
                for g in ger:
                    if not (f == 'thumb' and g == '03_'):
                        name = f + g + sd + s
                        i = sdk.index(s)
                        if i > 0:
                            parent = f + g + sd + sdk[i - 1]
                            pm.group(empty=True, name=name, parent=parent)
                        else:
                            pm.group(empty=True, name=name)
            pm.select(clear=True)


def insert_hierarchy():
    """
    Inserts the set driven key hierarchy into the finger hierarchy.
    :return:
    """
    for sd in side:
        for f in fin:
            for g in ger:
                if not (f == 'thumb' and g == '03_'):
                    """ parent the root of the hierarchy to the parent of the anim """
                    root_parent = f + g + sd + 'a0'
                    root_child = f + g + sd + sdk[0]
                    pm.parent(root_child, root_parent, relative=True)
                    """ parent the anim to the end of the hierarchy """
                    end_parent = f + g + sd + sdk[5]
                    end_child = f + g + sd + 'anim'
                    pm.parent(end_child, end_parent)


def set_driven_key(attribute):
    """
    :param attribute: the name of the attribute to setDrivenKey on both hand controls
    :return: None
    """
    d = {"Lt_": handCtrls[0], "Rt_": handCtrls[1]}
    s = attribute + "_sdk"
    for sd in side:
        for fn in fin:
            for gr in ger[:4]:
                if not (fn == 'thumb' and gr == '03_'):
                    for at in ["rotateX", "rotateY", "rotateZ"]:
                        obj = fn + gr + sd + s + "." + at
                        cd = d[sd] + "." + attribute
                        pm.setDrivenKeyframe(obj, currentDriver=cd, inTangentType="spline", outTangentType="spline")


def set_infinity(attribute):
    """
    :param attribute: the name of the attribute to setDrivenKey on both hand controls
    :return: None
    """
    s = attribute + "_sdk"
    for sd in side:
        for fn in fin:
            for gr in ger[:4]:
                if not (fn == 'thumb' and gr == '03_'):
                    for at in ["rotateX", "rotateY", "rotateZ"]:
                        obj = fn + gr + sd + s + "." + at
                        """ set pre/post infinity behavior """
                        li = pm.listConnections(obj, type="animCurve")
                        if li:
                            for animCurve in li:
                                pm.setAttr(animCurve + ".preInfinity", 4)   # 4 - Cycle with Offset
                                pm.setAttr(animCurve + ".postInfinity", 1)  # 1 - Linear


def set_val(attr, i):
    """
    Sets the value of an attribute found on both palm controls.

    :param attr: an attribute found on both palm controls
    :param i: the value to assign to the attribute
    :return: None
    """
    for p in handCtrls:
        pm.setAttr(p + '.' + attr, i)


def make_set_driven_keys():
    """
    Takes the pose_data dictionary and creates set driven keys for the fingers in that dictionary.

    :return: None
    """
    for key in pose_data:
        """ capture pose for the attribute value of 0 """
        set_val(key, 0)
        set_driven_key(key)
        """ for each key value in pose data, set the key value, set the pose and capture the pose at that key value"""
        for val in pose_data[key]:
            set_val(key, val)
            set_attr(pose_data[key][val], key)
            set_driven_key(key)
        set_infinity(key)
        set_val(key, 0)
    pm.select(clear=True)

def setup_hand_poses():
    make_hand_controls()
    presetBuilder.makeDefaultPresets()
    #build_hierarchy()
    #insert_hierarchy()
    #make_set_driven_keys()
    
    # for p in handCtrls:
    #     pm.setAttr(p + ".grip", 100)


if __name__ == '__main__':
    setup_hand_poses()
