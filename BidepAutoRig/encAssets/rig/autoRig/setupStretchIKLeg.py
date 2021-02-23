import pymel.core as pm
import tools
import maya.cmds as cmds

debug = True
upScene= cmds.upAxis(q=1, ax=1)

def flip(x):
    if x.find("_Lt_") != -1:
        return x.replace("_Lt_", "_Rt_")
    return x.replace("_Rt_", "_Lt_")


def arm_to_leg(x):
    swap = [("arm", "leg"), ("Arm", "Leg"), ("elbow", "knee"),
            ("handIk", "legIk"), ("hand", "foot"), ("shoulder", "thigh")]
    for k in swap:
        x = x.replace(k[0], k[1])
    return x


""" shared data goes here """
locArmLt = {"shoulderArmDist_Lt_loc": "shoulder_Lt_ik",
            "elbowArmDist_Lt_loc": "elbow_Lt_ik",
            "handArmDist_Lt_loc": "hand_Lt_ik",
            "allArmDist_Lt_loc": "handIk_Lt_ikh"}

distArmLt = {"uprArmDist_Lt_dist": ("elbowArmDist_Lt_loc", "shoulderArmDist_Lt_loc"),
             "lwrArmDist_Lt_dist": ("handArmDist_Lt_loc", "elbowArmDist_Lt_loc"),
             "allArmDist_Lt_dist": ("allArmDist_Lt_loc", "shoulderArmDist_Lt_loc")}

nodesArmLt = {"normalizeArmLength_Lt_Utmd": {'type': 'multiplyDivide',
                                             'attrs': {'operation': 2}},
              "armGlobalScale_Lt_UTmd": {'type': 'multiplyDivide',
                                         'attrs': {'operation': 2}},
              "uprArmStretch_Lt_UTmdl": {'type': 'multiplyDivide',
                                         'attrs': {}},
              "lwrArmStretch_Lt_UTmdl": {'type': 'multiplyDivide',
                                         'attrs': {}},
              "armStretchyOnOff_Lt_UTcond": {'type': 'condition',
                                             'attrs': {'operation': 2,
                                                       'secondTerm': 0,
                                                       'colorIfFalseR': 1}},
              "armStretchMinimum_Lt_UTcond": {'type': 'condition',
                                              'attrs': {'operation': 2,
                                                        'secondTerm': 1,
                                                        'colorIfFalseR': 1}
                                              }
              }

connectArmLt = [
                ("allArmDist_Lt_dist.distance", "normalizeArmLength_Lt_Utmd.input1X"),
                ("normalizeArmLength_Lt_Utmd.outputX", "armGlobalScale_Lt_UTmd.input1X"),
                ("armIKFK_Lt_anim.stretchyOffOn", "armStretchyOnOff_Lt_UTcond.firstTerm"),
                ("armStretchyOnOff_Lt_UTcond.outColorR", "armStretchMinimum_Lt_UTcond.colorIfTrueR"),
                ("armStretchyOnOff_Lt_UTcond.outColorR", "armStretchMinimum_Lt_UTcond.firstTerm"),
                ("armStretchMinimum_Lt_UTcond.outColorR", "uprArmStretch_Lt_UTmdl.input1X"),
                ("armStretchMinimum_Lt_UTcond.outColorR", "lwrArmStretch_Lt_UTmdl.input1X"),
                ("armGlobalScale_Lt_UTmd.outputX", "armStretchyOnOff_Lt_UTcond.colorIfTrueR"),
                ("uprArmStretch_Lt_UTmdl.outputX", "elbow_Lt_ik.translateX"),
                ("lwrArmStretch_Lt_UTmdl.outputX", "hand_Lt_ik.translateX"),
                ]

#

""" build left leg data from left arm data """
locLegLt = dict((arm_to_leg(k), arm_to_leg(v)) for k, v in locArmLt.items())
distLegLt = dict((arm_to_leg(k), (arm_to_leg(v[0]), arm_to_leg(v[1]))) for k, v in distArmLt.items())
nodesLegLt = dict((arm_to_leg(k), v) for k, v in nodesArmLt.items())
connectLegLt = [(arm_to_leg(c[0]), arm_to_leg(c[1])) for c in connectArmLt]

""" build right leg data from left leg data """
locLegRt = dict((flip(k), flip(v)) for k, v in locLegLt.items())
distLegRt = dict((flip(k), (flip(v[0]), flip(v[1]))) for k, v in distLegLt.items())
nodesLegRt = dict((flip(k), v) for k, v in nodesLegLt.items())
connectLegRt = [(flip(c[0]), flip(c[1])) for c in connectLegLt]


""" build the dictionary """
strDict = {
           "legDistance_Lt_grp": {'loc': locLegLt,
                                  'dist': distLegLt,
                                  'nodes': nodesLegLt,
                                  'connect': connectLegLt
                                  },
           "legDistance_Rt_grp": {'loc': locLegRt,
                                  'dist': distLegRt,
                                  'nodes': nodesLegRt,
                                  'connect': connectLegRt
                                  },
           }


def make_locators(d):
    li = []
    for name in d:
        tools.debug_print("\tCreating: " + name, dbg=debug)
        loc = pm.spaceLocator(name=name)
        tgt = d[name]
        pm.pointConstraint(tgt, name)
        li.append(loc)
    return li


def make_dist(d):
    li = []
    for name in d:
        tools.debug_print("\tCreating: " + name, dbg=debug)
        tgt1 = d[name][0]
        tgt2 = d[name][1]
        dist = pm.distanceDimension(tgt1, tgt2)
        if dist.type() != 'transform':
            dist = dist.getParent()
        dist.rename(name)
        li.append(dist)
    return li


def get_attrs(name, d):
    attrs = d
    if name.startswith(("upr", "lwr")):
        attrs['input2X'] = pm.getAttr(name[:6] + "Dist_" + tools.get_lr(name) + "_dist.distance")
        if tools.get_lr(name) == "Rt":
            attrs['input2X'] *= -1
    if name.startswith("normalize"):
        if name.find("Arm") != -1:
            a = pm.getAttr("uprArmDist_" + tools.get_lr(name) + "_dist.distance")
            b = pm.getAttr("lwrArmDist_" + tools.get_lr(name) + "_dist.distance")
            attrs['input2X'] = a + b
        else:
            a = pm.getAttr("uprLegDist_" + tools.get_lr(name) + "_dist.distance")
            b = pm.getAttr("lwrLegDist_" + tools.get_lr(name) + "_dist.distance")
            attrs['input2X'] = a + b
    return attrs


def make_nodes(d):
    for name in d:
        tools.debug_print("\tCreating: " + name, dbg=debug)
        typ = d[name]['type']
        node = pm.createNode(typ, name=name)
        attrs = get_attrs(name, d[name]['attrs'])
        for attr in attrs:
            tools.debug_print("\t\tSetting " + node + "." + attr + " to:  " + str(attrs[attr]), dbg=debug)
            node.setAttr(attr, attrs[attr])


def setup_stretch_ik():
    for grp_name in strDict:
        tools.debug_print("Setting up: " + grp_name, dbg=debug)
        li = make_locators(strDict[grp_name]['loc'])
        li += make_dist(strDict[grp_name]['dist'])
        par_grp_name = grp_name.replace("Distance", "Rig")
        grp = pm.group(name=grp_name, empty=True)
        par_grp = pm.group(name=par_grp_name, empty=True)
        """ group the locators and distanceDimensions """
        pm.parent(grp, par_grp)
        pm.parent(li, grp)
        """ make the nodes """
        make_nodes(strDict[grp_name]['nodes'])
        """ make the connections """
        tools.debug_print("\tMaking connections...", dbg=debug)
        for attrs in strDict[grp_name]['connect']:
            tools.debug_print("\t\tConnecting:  " + attrs[0] + " to: " + attrs[1], dbg=debug)
            pm.connectAttr(attrs[0], attrs[1])
        if debug:
            from pprint import pprint
            pprint(strDict)

