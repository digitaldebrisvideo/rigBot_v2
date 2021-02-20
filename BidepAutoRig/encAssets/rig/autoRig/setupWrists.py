import tools
import copy
import pymel.core as pm
import maya.cmds as cmds
__author__ = 'jhachigian'

debug = True
upScene= cmds.upAxis(q=1, ax=1)
""" this dictionary will be expanded by the functions below """
offsets = {"Lt": {"areas": {"Top": (0, 2.5, 0),
                            "Bottom": (0, -2.5, 0),
                            "Inner": (0, 0, 2.5),
                            "Outer": (0, 0, -2.5)
                            },
                  "nodes": {"wristFixTopBottom_Lt_UTmd": {"type": "multiplyDivide",
                                                          "attrs": {"input2Y": 0.05,
                                                                    "input2Z": 0.05}},
                            "wristFixTopBottom_Lt_UTclmp": {"type": "clamp",
                                                            "attrs": {"minG": 0, "maxG": 5,
                                                                      "minB": -5, "maxB": 0}},
                            "wristFixInnerOuter_Lt_UTmd": {"type": "multiplyDivide",
                                                           "attrs": {"input2Y": -0.025,
                                                                     "input2Z": -0.025}},
                            "wristFixInnerOuter_Lt_UTclmp": {"type": "clamp",
                                                             "attrs": {"minG": 0, "maxG": 5,
                                                                       "minB": -5, "maxB": 0}}
                            },
                  "connections": [["wrist_Lt_bind.rotateZ", "wristFixTopBottom_Lt_UTmd.input1Y"],
                                  ["wrist_Lt_bind.rotateZ", "wristFixTopBottom_Lt_UTmd.input1Z"],
                                  ["wristFixTopBottom_Lt_UTmd.outputY", "wristFixTopBottom_Lt_UTclmp.inputG"],
                                  ["wristFixTopBottom_Lt_UTmd.outputZ", "wristFixTopBottom_Lt_UTclmp.inputB"],
                                  ["wristFixTopBottom_Lt_UTclmp.outputG", "wristFixTop_Lt_bind.translateY"],
                                  ["wristFixTopBottom_Lt_UTclmp.outputB", "wristFixBottom_Lt_bind.translateY"],

                                  ["wrist_Lt_bind.rotateY", "wristFixInnerOuter_Lt_UTmd.input1Y"],
                                  ["wrist_Lt_bind.rotateY", "wristFixInnerOuter_Lt_UTmd.input1Z"],
                                  ["wristFixInnerOuter_Lt_UTmd.outputY", "wristFixInnerOuter_Lt_UTclmp.inputG"],
                                  ["wristFixInnerOuter_Lt_UTmd.outputZ", "wristFixInnerOuter_Lt_UTclmp.inputB"],
                                  ["wristFixInnerOuter_Lt_UTclmp.outputG", "wristFixInner_Lt_bind.translateZ"],
                                  ["wristFixInnerOuter_Lt_UTclmp.outputB", "wristFixOuter_Lt_bind.translateZ"]
                                  ]
                  },
           "Rt": {"areas": {},  # to be mirrored from Lt in mirror_offset_data function
                  "nodes": {},
                  "connections": []
                  }
           }


def mirror_offset_data():
    """
    Mirrors the "Lt" data to "Rt" in the "offsets" dictionary.

    :return: None
    """
    """ mirror area data """
    areas = offsets["Lt"]["areas"]
    for area in areas:
        o = areas[area]
        n = [x * -1 for x in o]
        offsets["Rt"]["areas"][area] = n
    """ mirror node data """
    nodes = offsets["Lt"]["nodes"]
    for node in nodes:
        new_name = node.replace("Lt", "Rt")
        offsets["Rt"]["nodes"][new_name] = copy.deepcopy(nodes[node])
        new_dict = offsets["Rt"]["nodes"][new_name]
        if node.endswith("md"):
            for attr in new_dict["attrs"]:
                new_dict["attrs"][attr] *= -1
        else:
            new_dict["attrs"] = {"minG": -5, "maxG": 0, "minB": 0, "maxB": 5}
    """ mirror connections """
    cons = offsets["Lt"]["connections"]
    offsets["Rt"]["connections"] = [[x[0].replace("Lt", "Rt"), x[1].replace("Lt", "Rt")] for x in cons]


def make_partial_bind_joint(hnd, wri, side):
    fix_name = "wristFix_%s_partial_bind" % side
    jnt = tools.make_joint(fix_name, zero=True, world=True, clear_selection=True)
    jnt.setAttr("drawStyle", 0)
    jnt.setParent(wri, relative=True)
    pm.makeIdentity(jnt, apply=True, translate=True, rotate=True, scale=True, normal=False, preserveNormals=True)
    offset = 0.002
    if side == "Rt":
        offset *= -1
    jnt.setAttr("translateY", offset)
    ori = pm.orientConstraint(hnd, wri, jnt, maintainOffset=True, skip="x", weight=1.0)
    ori.setAttr("interpType", 2)
    offsets[side]["partial_bind_joint"] = jnt
    return jnt


def make_offset_hierarchies(side):
    d = offsets[side]
    pbj = d["partial_bind_joint"]
    d["offset_hierarchies"] = {}
    for area in d["areas"]:
        grp_name = "wristFix%s_%s_grp" % (area, side)
        bnd_name = "wristFix%s_%s_bind" % (area, side)
        bnd = tools.make_joint(bnd_name, zero=True, world=True, clear_selection=True)
        bnd.setAttr("drawStyle", 0)
        grp = pm.group(name=grp_name)
        grp.setParent(pbj, relative=True)
        grp.setAttr("translate", d["areas"][area])
        d["offset_hierarchies"][area] = (grp, bnd)


def create_nodes(side):
    tools.debug_print("setupWrists: create_nodes:", dbg=debug)
    d = offsets[side]["nodes"]
    for key in d:
        typ = d[key]["type"]
        tools.debug_print("\tCreating " + typ + " node: " + key, dbg=debug)
        n = pm.createNode(typ, name=key)
        for attr in d[key]["attrs"]:
            v = d[key]["attrs"][attr]
            n.setAttr(attr, v)


def make_connections(side):
    tools.debug_print("setupWrists: make_connections", dbg=debug)
    cons = offsets[side]["connections"]
    for con in cons:
        tools.debug_print("\tConnecting: " + con[0] + "to:" + con[1], dbg=debug)
        pm.connectAttr(con[0], con[1])


def setup_wrist(side):
    hnd_name = "hand_%s_jnt" % side
    wri_name = "wrist_%s_bind" % side
    hnd = pm.PyNode(hnd_name)
    wri = pm.PyNode(wri_name)
    """ make partial bind joint, the master parent """
    make_partial_bind_joint(hnd, wri, side)
    """ make groups and bind joints """
    make_offset_hierarchies(side)
    """ create nodes """
    create_nodes(side)
    """ make connections """
    make_connections(side)


def setup_wrists():
    mirror_offset_data()
    if not pm.objExists("wrist_Lt_bind"):
        """ ...then this is an isolated test. Add the partial joints. """
        wrist_joints = {'hand_Lt_jnt': 'wrist_Lt_bind', 'hand_Rt_jnt': 'wrist_Rt_bind'}
        tools.insert_joints(wrist_joints)
    for side in ["Lt", "Rt"]:
        setup_wrist(side)
