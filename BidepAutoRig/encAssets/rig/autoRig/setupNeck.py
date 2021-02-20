import pymel.core as pm
import makeSplineIK
import tools
import makeBox
import maya.cmds as cmds
reload(makeSplineIK)
reload(tools)
reload(makeBox)

__author__ = 'jhachigian'

headAnim = "head_Mid_anim"
upScene= cmds.upAxis(q=1, ax=1)

""" format: (<controlName>, <controlParent>, <type>, <matchObject>) """
neckCtrlList = [(u'neck_ctrls', None, u'transform', None),
                (u'neck_rig', None, u'transform', None),
                (u'neck01Fk_Mid_a0', u'neck_ctrls', u'transform', u'neck01_Mid_bind'),
                (u'neck01Fk_Mid_anim', u'neck01Fk_Mid_a0', u'joint', u'neck01_Mid_bind'),

                (u'neck01_VJ_bind', None, u'joint', u'neck01_Mid_bind'),
                (u'neck01Fix_Bk_bind', None, u'joint', u'neck01_Mid_bind'),

                (u'neck02_VJ_bind', None, u'joint', u'neck02_Mid_bind'),
                (u'neck02Fix_Bk_bind', None, u'joint', u'neck02_Mid_bind'),

                (u'neck03_VJ_bind', None, u'joint', u'neck03_Mid_bind'),
                (u'neck03Fix_Bk_bind', None, u'joint', u'neck03_Mid_bind'),

                (u'head_Mid_a0', u'neck01Fk_Mid_anim', u'transform', u'head_Mid_bind'),
                (u'head_Mid_anim', u'head_Mid_a0', u'joint', u'head_Mid_bind'),
                (u'head_Mid_ref', u'head_Mid_anim', u'transform',  u'head_Mid_bind'),

                (u'head_VJ_bind', None, u'joint', u'head_Mid_bind'),
                (u'headFix_Bk_bind', None, u'joint', u'head_Mid_bind'),

                (u'topNeckSkin_Mid_grp', u'neck_rig', u'transform', u'neckEnd_Mid_jnt'),
                (u'topNeckSkin_Mid_jnt', None, u'joint', u'neckEnd_Mid_jnt'),
                (u'topNeckSkin_Mid_ref', u'head_Mid_anim', u'transform', u'topNeckSkin_Mid_jnt'),

                (u'bottomNeckSkin_Mid_grp', u'neck_rig', u'transform', u'neck01_Mid_bind'),
                (u'bottomNeckSkin_Mid_jnt', None, u'joint', u'neck01_Mid_bind'),
                # (u'bottomNeckSkin_Mid_ref', u'neck01Fk_Mid_anim', u'transform', u'bottomNeckSkin_Mid_jnt'),

                (u'rotateReader_grp', None, u'transform', None),
                (u'headRotReader_grp', u'rotateReader_grp', u'transform', None),
                (u'headRotReader_loc', u'headRotReader_grp', u'transform', None)]

neckCircleDict = {u'head_Mid_anim': {'radius': 10.0, 'degree': 1, 'sections': 6,
                                     'rotate': 30.0, 'offset': 0.0, 'color': 17},
                  u'neck01Fk_Mid_anim': {'radius': 10.0,  'degree': 1, 'sections': 6,
                                         'rotate': 30.0, 'offset': 0.0, 'color': 17}}

neckUpVectors = {u'bottomNeckSkin_Mid_loc': u'neck01Fk_Mid_anim', u'topNeckSkin_Mid_loc': u'head_Mid_anim'}

neckControls = [u'neckIK_Mid_ikh',  u'neck01_Mid_bind', u'neckEnd_Mid_jnt',
                u'bottomNeckSkin_Mid_jnt', u'topNeckSkin_Mid_jnt', u'neck_curve_skinCluster',
                u'neck_rig', u'bottomNeckSkin_Mid_loc', u'topNeckSkin_Mid_loc']

neckPCDict = {u'neck01Fk_Mid_anim': u'neck01_Mid_bind', u'head_Mid_anim': u'head_Mid_bind',
              # u'bottomNeckSkin_Mid_ref': u'bottomNeckSkin_Mid_jnt',
              u'topNeckSkin_Mid_ref': u'topNeckSkin_Mid_jnt'}

curvNode = neckControls[0] + '_arcLength'
backNode = 'neck_curve_normalizedScale'

neckShdNodes = ['neck_exp_spineCurveInfo_divBy_world_anim_mult', 'neck_exp_sqrt_of_scale',
                'neck_exp_1_divBy_sqrt_of_scale']

neckAttrs = {neckShdNodes[0]: {'setAttr': {'operation': 2}, 'lockAttr': [],
                               'connectAttr': [('outputX', neckShdNodes[1] + '.input1X')]},
             neckShdNodes[1]: {'setAttr': {'input2X': .5, 'operation': 3}, 'lockAttr': [],
                               'connectAttr': [('outputX', neckShdNodes[2] + '.input2X')]},
             neckShdNodes[2]: {'setAttr': {'input1X': 1, 'operation': 2},
                               'lockAttr': [], 'connectAttr': []},
             backNode: {'setAttr': {'operation': 2},
                        'lockAttr': [], 'connectAttr': []},
             curvNode: {'setAttr': {}, 'lockAttr': [],
                        'connectAttr': [('normalizedScale', neckShdNodes[0] + '.input1X')]},
             'world_anim': {'setAttr': {}, 'lockAttr': [],
                            'connectAttr': [('globalScale', neckShdNodes[0] + '.input2X')]}}

neckJoints = [u'neck01_Mid_bind', u'neck02_Mid_bind', u'neck03_Mid_bind', u'neckEnd_Mid_jnt']

attrHeader = "spaceSwitch"
attrData = {"head_Mid_anim": {"targets": ["neck01Fk_Mid_anim", "root_Mid_anim", "character02_Mid_anim"],
                              "constraint": pm.orientConstraint, "object": "head_Mid_a0", "interpType": 2}}


""" format: (<controlName>, <controlParent>, <type>, <matchObject>) """
headCtrlList = [(u'headTop_Mid_offsetGrp', u'head_Mid_anim', u'transform', u'headTop_Mid_bind'),
                (u'headTop_Mid_ctrlGrp', u'headTop_Mid_offsetGrp', u'transform', u'headTop_Mid_offsetGrp'),
                (u'headTop_Mid_anim', u'headTop_Mid_ctrlGrp', u'transform', u'headTop_Mid_ctrlGrp'),
                
                
                (u'headRear_Mid_offsetGrp', u'head_Mid_anim', u'transform', u'headRear_Mid_bind'),
                (u'headRear_Mid_ctrlGrp', u'headRear_Mid_offsetGrp', u'transform', u'headRear_Mid_offsetGrp'),
                (u'headRear_Mid_anim', u'headRear_Mid_ctrlGrp', u'transform', u'headRear_Mid_ctrlGrp'),
                
                (u'headSide_Lt_offsetGrp', u'head_Mid_anim', u'transform', u'headSide_Lt_bind'),
                (u'headSide_Lt_ctrlGrp', u'headSide_Lt_offsetGrp', u'transform', u'headSide_Lt_offsetGrp'),
                (u'headSide_Lt_anim', u'headSide_Lt_ctrlGrp', u'transform', u'headSide_Lt_ctrlGrp'),

                (u'headSide_Rt_offsetGrp', u'head_Mid_anim', u'transform', u'headSide_Rt_bind'),
                (u'headSide_Rt_ctrlGrp', u'headSide_Rt_offsetGrp', u'transform', u'headSide_Rt_offsetGrp'),
                (u'headSide_Rt_anim', u'headSide_Rt_ctrlGrp', u'transform', u'headSide_Rt_ctrlGrp')]


""" <anim name>: <overrideColor> """
headAnimDict = {u'headTop_Mid_anim': 25,
                u'headRear_Mid_anim': 26,
                u'headSide_Lt_anim': 18,
                u'headSide_Rt_anim': 20}


def adjust_vj_bk_joints():
    """

    Parents joints, and sets the Y-translate values of the Volume Joints and the Fixer joints.

    :return: None
    """
    d = {'neck01_Mid_bind': {'vj': 'neck01_VJ_bind', 'bk': 'neck01Fix_Bk_bind', 'input2': [-0.5, -0.5, -0.5]},
         'neck02_Mid_bind': {'vj': 'neck02_VJ_bind', 'bk': 'neck02Fix_Bk_bind', 'input2': [-0.1, -0.1, -0.1]},
         'neck03_Mid_bind': {'vj': 'neck03_VJ_bind', 'bk': 'neck03Fix_Bk_bind', 'input2': [-0.5, -0.5, -0.5]},
         'head_Mid_bind': {'vj': 'head_VJ_bind', 'bk': 'headFix_Bk_bind'}}
    for k in d:
        jnt = pm.PyNode(k)
        vj = pm.PyNode(d[k]['vj'])
        bk = pm.PyNode(d[k]['bk'])
        pm.parent(vj, jnt)
        pm.parent(bk, vj)
        for x in [vj, bk]:
            x.setAttr('jointOrient', [0, 0, 0])
            x.setAttr('drawStyle', 0)
        vj.setAttr("translateY", 0.002)
        if k.startswith("neck"):
            bk.setAttr("translateY", 3.0)
            md_name = k + "_VJMultDiv"
            md = pm.createNode('multiplyDivide', name=md_name)
            for x in ["X", "Y", "Z"]:
                pm.connectAttr(k + ".rotate" + x, md + ".input1" + x)
                pm.connectAttr(md + ".output" + x, vj + ".rotate" + x)
            # md.setAttr('input2', [-0.5, -0.5, -0.5])
            md.setAttr('input2', d[k]['input2'])
        else:
            bk.setAttr("translateX", -3.0)


def adjust_head_vj_bk_joints():
    upScene= cmds.upAxis(q=1, ax=1)
    tgt = "headEnd_Mid_jnt"
    loc = "headRotReader_loc"
    upv = "topNeckSkin_Mid_loc"
    md_name = "headRotReader_VJ_UTmd"
    md = pm.createNode("multiplyDivide", name=md_name)
    """ constrain """
    tools.match_to("headRotReader_grp", "head_Mid_bind")
    if upScene == 'y':
        cmds.setAttr('head_Mid_bind.ry', -90)
        print ' !!!!!!!!!!!!!!!!!!!!!!!!!!! HEAD Y-up !!!!!!!!!!!!!!!!!!!!!!!!!!!'
    pm.parentConstraint("neckEnd_Mid_jnt", "headRotReader_grp", maintainOffset=True)
    pm.aimConstraint(tgt, loc, worldUpObject=upv, upVector=(-1, 0, 0), worldUpType="object", aimVector=(0, 1, 0))
    """ connect attrs """
    pm.connectAttr(loc + ".rotate", md_name + ".input1")
    pm.connectAttr(md_name + ".output", "head_VJ_bind.rotate")
    md.setAttr("input2", [0, -0.5, -0.5])


def adjust_weighting():
    curve_name = neckControls[0] + "_curve"
    cluster_name = neckControls[5]
    pm.select(curve_name)
    pm.skinCluster(edit=True, addInfluence="chestDriven_Mid_jnt")
    """ do not remove the redundant parentheses below -- skinPercent needs a tuple of tuple(s) to work """
    # weights = [(("bottomNeckSkin_Mid_jnt", 1.0)),
    #            (("bottomNeckSkin_Mid_jnt", 1.0)),
    #            (("bottomNeckSkin_Mid_jnt", 0.25), ("topNeckSkin_Mid_jnt", 0.75)),
    #            (("topNeckSkin_Mid_jnt", 1.0))]
    weights = [(("bottomNeckSkin_Mid_jnt", 1.0)),
               (("bottomNeckSkin_Mid_jnt", 1.0)),
               (("bottomNeckSkin_Mid_jnt", 0.33), ("topNeckSkin_Mid_jnt", 0.67)),
               (("topNeckSkin_Mid_jnt", 1.0))]
    for i in range(len(weights)):
        pm.skinPercent(cluster_name, curve_name + ".cv[{0}]".format(i), transformValue=weights[i])


def set_driven_keys():
    d = {
         "headFix_Bk_bind": {"translateX": [{"cd": "headRotReader_loc.rotateZ", "keys": [(0, -3), (60, -6)]}]},
         "neck03Fix_Bk_bind": {"translateY": [{"cd": "headRotReader_loc.rotateZ", "keys": [(0, 3), (60, 6)]},
                                              {"cd": "neck03_Mid_bind.rotateZ", "keys": [(0, 3), (40, 6)]}]},
         "neck01Fix_Bk_bind": {"translateY": [{"cd": "neck01_Mid_bind.rotateZ", "keys": [(0, 3), (40, 6)]}]},
         "neck02Fix_Bk_bind": {"translateY": [{"cd": "neck02_Mid_bind.rotateZ", "keys": [(0, 3), (40, 6)]}]},
         }
    for obj in d:
        for attr in d[obj]:
            for x in d[obj][attr]:
                for key in x["keys"]:
                    cd = x["cd"]
                    pm.setDrivenKeyframe(obj, attribute=attr, currentDriver=cd, driverValue=key[0], value=key[1],
                                         inTangentType='linear', outTangentType='linear')


def setup_neck():
    tools.make_ctrl_hierarchy(neckCtrlList, neckCircleDict)
    adjust_vj_bk_joints()
    makeSplineIK.make_spine_up_vectors(neckUpVectors)
    adjust_head_vj_bk_joints()
    makeSplineIK.make_spline_ik(neckControls, u'C_root_JNT', neckPCDict)
    pm.parentConstraint(u'neck01Fk_Mid_anim', u'bottomNeckSkin_Mid_jnt')
    adjust_weighting()
    makeSplineIK.make_stretch_ik(neckControls, neckShdNodes, neckAttrs, neckJoints, curvNode, backNode)
    if upScene == 'z':
        pm.setAttr(headAnim + ".rotateOrder", 3)
    if upScene == 'y':
        pm.setAttr(headAnim + ".rotateOrder", 0)
        cmds.setAttr("head_Mid_bind_parentConstraint1.target[0].targetOffsetRotateY", -90)
        print '0000000000000000000000000000  FIXED HEAD CONSTRAINT 00000000000000000000000000000'
    for obj in attrData:
        attrs = attrData[obj]["targets"]
        tools.create_attributes(obj, attrHeader, attrs)
        for attr in attrs:
            pm.addAttr(obj + "." + attr, edit=True, hasMaxValue=True, hasMinValue=True, minValue=0.0, maxValue=1.0)
    pm.setAttr("head_Mid_anim.neck01Fk_Mid_anim", 1)
    """ add and connect Stretch attrs """
    for x in ["head_Mid_anim", "neck01Fk_Mid_anim"]:
        pm.PyNode(x).addAttr("Stretch")
        pm.connectAttr(neckShdNodes[0] + ".outputX", x + ".Stretch")
        pm.PyNode(x).setAttr("Stretch", channelBox=True, keyable=False)
    set_driven_keys()
    """ add point constraint for head. """
    pm.pointConstraint("neck01Fk_Mid_anim", "head_Mid_a0", maintainOffset=True)
    
    


def setup_head():
    """
    Sets up "anim" controls for head "bind" joints. Must be called AFTER setup_neck() to ensure that
    "head_Mid_anim" exists.

    :return: None
    """
    upScene= cmds.upAxis(q=1, ax=1)

    if not pm.objExists(headCtrlList[0][-1]):  # this does not use a compatible skeleton.
        return
    tools.make_ctrl_hierarchy(headCtrlList)
    for anim in headAnimDict:
        cube = makeBox.make_box(2.5, 2.5, 2.5)
        shp = cube.getShape()
        override_color = headAnimDict[anim]
        tools.set_override_color(shp, override_color)
        pm.parent(shp, anim, shape=True, relative=True)
        pm.delete(cube)
        bnd = tools.get_new_name(anim, "bind")
        pm.pointConstraint(anim, bnd)
        if upScene == 'y':
            pm.orientConstraint(anim, bnd)
        if upScene == 'z':
            pm.orientConstraint(anim, bnd)
        # pm.scaleConstraint(anim, bnd)
        for x in [".scaleX", ".scaleY", ".scaleZ"]:
            pm.connectAttr(anim + x, bnd + x)

