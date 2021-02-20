import pymel.core as pm
from maya import OpenMaya
import maya.cmds as cmds
import tools
import makeBox

reload(tools)
reload(makeBox)

__author__ = 'jhachigian'

debug = True
upScene= cmds.upAxis(q=1, ax=1)
rigChildren = ["geometry_grp", "setup_grp", "controls_grp"]
setChildren = ["skeleton_grp", "tech_grp"]
ctlChildren = ["display_grp"]
upScene= cmds.upAxis(q=1, ax=1)
limbs = ["shoulder_Lt_jnt", "shoulder_Rt_jnt"]

hands = {'handIkGimbal_Lt_anim': 'hand_Lt_ik', 'handIkGimbal_Rt_anim': 'hand_Rt_ik'}

# Each tuple takes the form of (<name>, <parentObjects>, <placement>)


ikDict = {
          'shoulder_Lt_jnt': ["shoulder_Lt_ik", "hand_Lt_ik", "handIk_Lt_ikh", (1, 0, 0)],
          'shoulder_Rt_jnt': ["shoulder_Rt_ik", "hand_Rt_ik", "handIk_Rt_ikh", (1, 0, 0)]
          }

pvDict = {
          'shoulder_Lt_jnt': ["elbowUpVectorIk_Lt_a0", "armBase_Lt_jnt", (0, 0, 1)],
          'shoulder_Rt_jnt': ["elbowUpVectorIk_Rt_a0", "armBase_Rt_jnt", (0, 0, 1)]}

pvChainDict = {
               'shoulder_Lt_jnt': ["shoulder_Lt_jnt", "elbow_Lt_jnt", "hand_Lt_jnt"],
               'shoulder_Rt_jnt': ["shoulder_Rt_jnt", "elbow_Rt_jnt", "hand_Rt_jnt"]}

handTargets = {"shoulder_Lt_jnt": "hand_Lt_jnt", "shoulder_Rt_jnt": "hand_Rt_jnt"}

visDict = {"Lt": {}, "Rt": {}}


# ikAttrs = ["root03_Mid_anim"]
# ikAttrData = {}

pvAttrs = ["world_anim", "character02_Mid_anim", "root03_Mid_anim", "pelvis_Mid_anim"]

pvAttrData = {}
pvAttrHeader = "spaceSwitch"



def create_groups():
    for g in ["rig_XXX_grp"] + rigChildren + setChildren + ctlChildren:
        if not pm.objExists(g):
            pm.group(name=g, empty=True)
    for g in rigChildren:
        pm.parent(g, "rig_XXX_grp")
    for g in setChildren:
        pm.parent(g, "setup_grp")
    for g in ctlChildren:
        pm.parent(g, "controls_grp")






def apply_ik(x):
    start = ikDict[x][0]
    end = ikDict[x][1]
    hnd = ikDict[x][2]
    nrm = ikDict[x][3]
    eff = tools.get_new_name(hnd, "ike")
    trn = tools.get_new_name(hnd, "a0")
    jnt = tools.get_new_name(hnd, "anim")
    gim = tools.expand_prefix(jnt, "Gimbal")
    col = tools.find_lr_override_color(x)
    """ apply Rotate-Plane IK solver """
    ikh = pm.ikHandle(solver="ikRPsolver", startJoint=start, endEffector=end)
    ikh[0].rename(hnd)
    ikh[1].rename(eff)
    """ make empty transform by creating an empty group """
    ikt = pm.group(name=trn, empty=True)
    pm.parent(ikt, ikh[1], relative=True)
    ikt.setParent(None)
    tools.zero_rotation(ikt)
    pm.parent(ikt, "controls_grp")
    """ create control joint """
    ikj = pm.PyNode(tools.make_joint(jnt, clear_selection=False))
    ikg = pm.PyNode(tools.make_joint(gim, zero=True, clear_selection=False))
    if x.startswith("shoulder"):
        pm.parent(ikj, handTargets[x], relative=True)
        z = {'jointOrientX': 0, 'jointOrientZ': 0}
        for k in z:
            ikj.setAttr(k, z[k])
        tools.zero_rotation(ikj)
    pm.parent(ikj, ikt)
    """ replace control joint's shape with that of a circle """
    tools.apply_circle(ikj, nrm, color=col)
    # tools.apply_circle(ikg, nrm, color=col, degree=1, sections=4)
    shp = tools.apply_shape(ikg, "fourPointArrow_anim")
    # tools.set_override_color(shp, 17)
    if ikg.startswith("hand"):
        tools.rotate_shape(shp, (0, 0, 90))
    """ parentObjects IK handle to joint. """
    ikh[0].setParent(ikg)
    """ enter data into visDict """
    side = x.split("_")[1]
    if x.startswith("shoulder"):
        key = "arm"
        ikj.addAttr("elbowSpin")
        ikj.setAttr("elbowSpin", channelBox=True)
        ikj.setAttr("elbowSpin", keyable=True)
        pm.connectAttr(ikj + ".elbowSpin", ikh[0] + ".twist")
    else:
        key = "leg"
    visDict[side][key] = ikg


def make_pv_target(li):
    """
        :param li: a list of three joints
        :return: a group on the same plane as the three joints

        based on a routine by Marco Giordano
        http://vimeo.com/66262994
    """
    start = pm.joint(li[0], query=True, position=True)
    mid = pm.joint(li[1], query=True, position=True)
    end = pm.joint(li[2], query=True, position=True)

    start_v = OpenMaya.MVector(start[0], start[1], start[2])
    mid_v = OpenMaya.MVector(mid[0], mid[1], mid[2])
    end_v = OpenMaya.MVector(end[0], end[1], end[2])

    start_end = end_v - start_v
    start_mid = mid_v - start_v

    dot_p = start_mid * start_end
    proj = dot_p/start_end.length()
    start_end_n = start_end.normal()
    proj_v = start_end_n * proj

    arrow_v = start_mid - proj_v
    tools.debug_print("\tarrowV before: " + str(arrow_v.length()), dbg=debug)
    arrow_v /= arrow_v.length()
    tools.debug_print("\tarrowV after divide: " + str(arrow_v.length()), dbg=debug)
    arrow_v *= start_end.length()
    tools.debug_print("\tarrowV after multiply: " + str(arrow_v.length()), dbg=debug)
    final_v = arrow_v + mid_v

    grp = pm.group(empty=True)
    pm.xform(translation=(final_v.x, final_v.y, final_v.z))
    return grp


def apply_pv(x):
    """
    :param x: the name of the root of the affected limb
    :return: a pole vector constraint
    """
    a0 = pvDict[x][0]
    p0 = pvDict[x][1]
    a1 = tools.get_new_name(a0, "a1")
    jn = tools.get_new_name(a0, "anim")
    nm = pvDict[x][2]
    p1 = ikDict[x][2]
    ih = ikDict[x][2]
    an = tools.get_new_name(ih, "anim")
    co = tools.find_lr_override_color(x)
    """ create a0 transform and constrain it between the start and end of the limb """
    knc = pm.group(name=a0, empty=True)
    pm.parent(a0, "controls_grp")
    pm.pointConstraint(p0, p1, a0, w=0.5)
    kng = make_pv_target(pvChainDict[x])
    pm.rename(kng, a1)
    tools.zero_rotation(knc)
    pm.parent(a1, a0)
    jnt = tools.make_joint(jn, clear_selection=False)
    jnt.setParent(kng)
    tools.apply_circle(jnt, nm, color=co)
    if jnt.startswith("knee"):
        attrs = pvAttrs + [a0, an]
        tools.create_attributes(jnt, pvAttrHeader, attrs)
        jnt.setAttr(an, 1)
    else:
        extra = ["spine03Fk_Mid_anim", "clavicle_%s_anim" % tools.get_lr(jnt)]
        attrs = pvAttrs + extra + [a0, an]
        tools.create_attributes(jnt, pvAttrHeader, attrs)
        jnt.setAttr("spine03Fk_Mid_anim", 1)
    pvAttrData[jnt] = {"object": kng, "targets": attrs, "constraint": pm.parentConstraint, "interpType": 2}
    for attr in attrs:
        pm.addAttr(jnt + "." + attr, edit=True, hasMaxValue=True, hasMinValue=True, minValue=0.0, maxValue=1.0)
    pm.poleVectorConstraint(jnt, ih, name=ih+"_poleVectorConstraint")

def draw_pv_line(x):
    tgt1 = tools.get_new_name(pvChainDict[x][1], "ik")
    tgt2 = tools.get_new_name(pvDict[x][0], "anim")
    line_name = tools.get_new_name(tgt1, "jnt")
    line_name = tools.expand_prefix(line_name, "PV")
    grp_name = tools.get_new_name(line_name, "a0")
    crv_name = tools.get_new_name(line_name, "curve")
    skn_name = tools.get_new_name(crv_name, "skin")
    grp = pm.group(empty=True, name=grp_name)
    jnt = tools.make_joint(line_name, zero=True, world=True)
    jnt.setParent(grp)
    pos1 = pm.xform(tgt1, query=True, translation=True, worldSpace=True)
    pos2 = pm.xform(tgt2, query=True, translation=True, worldSpace=True)
    crv = pm.curve(point=[pos1, pos2], degree=1)
    crv_shape = crv.getShape()
    pm.parent(crv_shape, jnt, relative=True, shape=True)
    pm.delete(crv)
    pm.rename(crv_shape, crv_name)
    tools.debug_print("Skinning " + crv_name + " to " + tgt1 + " and " + tgt2, dbg=debug)
    pm.select([tgt1, tgt2])
    pm.skinCluster(crv_name, tgt1, tgt2, name=skn_name, toSelectedBones=True)
    pm.select(clear=True)
    jnt.setAttr("overrideEnabled", True)
    jnt.setAttr("overrideDisplayType", 2)


def setup_ik():
    """
    :return: main program.
    """
    pm.select(clear=True)
    create_groups()
    # pm.parent("C_root_JNT", "skeleton_grp")
    """ arm setup """
    for limb in limbs:
        tools.create_duplicate_chain(limb, "ik")
        apply_ik(limb)
        apply_pv(limb)
        draw_pv_line(limb)

    for obj in ["armEnd_Lt_ik", "armEnd_Rt_ik"]:  # run this in case an pre-v019 skeleton was used for setup.
        if pm.objExists(obj):
            pm.delete(obj)


    for obj in pm.ls("*_plc"):
        pm.delete(obj)



    pm.select(clear=True)
