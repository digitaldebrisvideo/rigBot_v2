import maya.cmds as cmds
import pymel.core as pm
import tools

__author__ = 'jhachigian'

debug = True

upScene= cmds.upAxis(q=1, ax=1)
def make_spine_up_vectors(upvectors):
    upScene= cmds.upAxis(q=1, ax=1)
    tools.debug_print("makeSpineUpVectors", dbg=debug)
    for s in upvectors:
        loc_name = s
        grp_name = tools.get_new_name(s, "grp")
        match = upvectors[s]
        loc = pm.spaceLocator(name=loc_name)
        pm.parent(loc, match, relative=True)
        if upScene == 'y':
            loc.setAttr('translate', (0.0, 0.0, -10.0))
        if upScene == 'z':
            loc.setAttr('translate', (-10.0, 0.0, 0.0))
        pm.parent(loc, grp_name)
        tools.zero_rotation(loc)
        pm.parentConstraint(match, grp_name, maintainOffset=True)


def make_spline_ik(li, parent, pc_dict, numSpans=1):
    upScene= cmds.upAxis(q=1, ax=1)
    tools.debug_print("Making Spline IK", dbg=debug)
    ik_s = pm.ikHandle(name=li[0], solver='ikSplineSolver', rootOnCurve=True, startJoint=li[1], endEffector=li[2],
                       priority=1, weight=1, createCurve=True, snapCurve=True, numSpans=numSpans)
    ik_curve = ik_s[2]
    ik_curve.rename(li[0] + "_curve")
    tools.debug_print("\tParenting: " + li[0] + " to: " + li[6], dbg=debug)
    pm.parent(li[0], li[6])
    tools.debug_print("\tParenting: " + ik_curve + " to: " + li[6], dbg=debug)
    pm.parent(ik_curve, li[6])
    tools.debug_print("\tSkincluster for: " + ik_curve + " to: " + li[3] + " and: " + li[4] + " with name: " + li[5],
                      dbg=debug)
    pm.skinCluster(ik_curve, li[3], li[4], name=li[5])
    tools.debug_print("\tSetting twist options...", dbg=debug)
    pm.setAttr(li[0] + '.dTwistControlEnable', 1)  # enable advance twist options.
    pm.setAttr(li[0] + '.dWorldUpType', 4)
    pm.setAttr(li[0] + '.dWorldUpAxis', 0)
    if upScene == 'y':
        cmds.setAttr(li[0] + ".dWorldUpVectorY", 0)
        cmds.setAttr(li[0] + ".dWorldUpVectorZ", -1)
        cmds.setAttr(li[0] + ".dWorldUpVectorEndY", 0)
        cmds.setAttr(li[0] + ".dWorldUpVectorEndZ", -1)
    pm.connectAttr(li[7] + '.worldMatrix', li[0] + '.dWorldUpMatrix', force=True)
    pm.connectAttr(li[8] + '.worldMatrix', li[0] + '.dWorldUpMatrixEnd', force=True)

    """ parentObjects endpoints back to root joint """
    for par in pc_dict:
        tools.debug_print("\tParent constraining: " + pc_dict[par] + " to: " + par, dbg=debug)
        pm.parentConstraint(par, pc_dict[par])
    for jnt in li[3:5]:
        tools.debug_print("\tParenting: " + jnt + "to: " + parent, dbg=debug)
        pm.parent(jnt, parent)


def make_stretch_ik(li, shading_nodes, attrs, spine_joints, curve_node, back_curve_name):
    tools.debug_print("Setting up stretch functions...", dbg=debug)
    arc_len = pm.PyNode(pm.arclen(li[0] + "_curve", constructionHistory=True))
    arc_len.rename(curve_node)
    pm.addAttr(arc_len, longName='normalizedScale', attributeType='double')

    # normalize the back curves stretchy.
    tools.debug_print("Creating backCurve...", dbg=debug)
    back_curve = pm.shadingNode('multiplyDivide', asUtility=True, name=back_curve_name)
    back_curve.connectAttr('outputX', arc_len + '.normalizedScale')
    arc_len.connectAttr('arcLength', back_curve + '.input1X')
    normal_scale = back_curve.getAttr('input1X')  # grab the normalized scale value and adds it to input 2X
    back_curve.setAttr('input2X', normal_scale)

    tools.debug_print("\tSetting up shading nodes", dbg=debug)
    for obj in shading_nodes:
        tools.debug_print("Creating: " + obj, dbg=debug)
        pm.shadingNode('multiplyDivide', asUtility=True, name=obj)

    for obj in attrs:
        for attr in attrs[obj]['setAttr']:
            tools.debug_print("\tsetAttr:" + obj + '.' + attr + " to: " + str(attrs[obj]['setAttr'][attr]), dbg=debug)
            pm.setAttr(obj + '.' + attr, attrs[obj]['setAttr'][attr])

    tools.debug_print("Connecting attributes.", dbg=debug)
    for obj in attrs:
        if pm.objExists(obj):
            for attr in attrs[obj]['connectAttr']:
                tools.debug_print("\tconnectAttr:" + obj + '.' + attr[0] + " to: " + str(attr[1]), dbg=debug)
                pm.connectAttr(obj + '.' + attr[0], attr[1])

    div_mult_node = shading_nodes[0]
    tools.debug_print("Connecting spine joint scaleX to :" + div_mult_node + ".outputX", dbg=debug)
    for spineJoint in spine_joints:
        tools.debug_print("\tconnectAttr:" + div_mult_node + ".outputX" + " to: " + spineJoint + ".scaleX", dbg=debug)
        pm.connectAttr(div_mult_node + ".outputX", spineJoint + ".scaleX")

    tools.debug_print("Locking attributes.", dbg=debug)
    for obj in attrs:
        for attr in attrs[obj]['lockAttr']:
            tools.debug_print("\tLocking:" + obj + '.' + attr, dbg=debug)
            pm.setAttr(obj + '.' + attr, lock=True, keyable=False, channelBox=False)
