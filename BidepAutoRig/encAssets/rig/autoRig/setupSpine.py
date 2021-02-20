import os
import pymel.core as pm
import maya.cmds as cmds
import makeSplineIK
import tools

reload(makeSplineIK)
reload(tools)

__author__ = 'jhachigian'

debug = True
upScene= cmds.upAxis(q=1, ax=1)
""" format: (<controlName>, <controlParent>, <type>, <matchObject>) """
splineCtrlDict = [(u'spine_ctrls', None, u'transform', None),
                  (u'spine_rig', None, u'transform', None),

                  (u'world_anim', u'spine_ctrls', u'joint', None),

                  (u'character_Mid_a0', u'world_anim', u'transform', None),
                  (u'character_Mid_anim', u'character_Mid_a0', u'joint', None),

                  (u'character02_Mid_a0', u'character_Mid_anim', u'transform', None),
                  (u'character02_Mid_anim', u'character02_Mid_a0', u'joint', None),

                  (u'jntHeir01_grp', u'root_Mid_jnt', u'transform', u'root_Mid_jnt'),
                  (u'jntHeir02_grp', u'jntHeir01_grp', u'transform', u'root_Mid_jnt'),

                  (u'root_Mid_a0', u'character_Mid_anim', u'transform', u'root_Mid_jnt'),
                  (u'root_Mid_anim', u'root_Mid_a0', u'joint',  u'root_Mid_jnt'),

                  (u'spine01Fk_Mid_a0', u'root_Mid_anim', u'transform', u'spine01_Mid_jnt'),
                  (u'spine01Fk_Mid_anim', u'spine01Fk_Mid_a0', u'joint', u'spine01_Mid_jnt'),

                  (u'spine02Fk_Mid_a0', u'spine01Fk_Mid_anim', u'transform', u'spine03_Mid_jnt'),
                  (u'spine02Fk_Mid_anim', u'spine02Fk_Mid_a0', u'joint', u'spine03_Mid_jnt'),

                  (u'chest_Mid_a0', u'spine02Fk_Mid_anim', u'transform', u'chest_Mid_bind'),
                  (u'chest_Mid_anim', u'chest_Mid_a0', u'joint', u'chest_Mid_bind'),

                  (u'spine03Fk_Mid_a0', u'chest_Mid_anim', u'transform', u'chest_Mid_bind'),
                  (u'spine03Fk_Mid_anim', u'spine03Fk_Mid_a0', u'joint', u'chest_Mid_bind'),
                  (u'chest_Mid_ref', u'spine03Fk_Mid_anim', u'transform',  u'chest_Mid_bind'),

                  (u'hips_Mid_a0', u'root_Mid_anim', u'transform', u'hips_Mid_jnt'),
                  (u'hips_Mid_anim', u'hips_Mid_a0', u'joint', u'hips_Mid_jnt'),

                  (u'pelvis_Mid_a0', u'hips_Mid_anim', u'transform', u'hips_Mid_jnt'),
                  (u'pelvis_Mid_anim', u'pelvis_Mid_a0', u'joint', u'hips_Mid_jnt'),

                  (u'hips_Mid_ref', u'pelvis_Mid_anim', u'transform', u'hips_Mid_jnt'),
                  
                  (u'topSpineSkin_Mid_grp', u'spine_rig', u'transform', u'spineEnd_Mid_jnt'),
                  (u'topSpineSkin_Mid_jnt', None, u'joint', u'spineEnd_Mid_jnt'),
                  (u'topSpineSkin_Mid_ref', u'chest_Mid_anim', u'transform', u'topSpineSkin_Mid_jnt'),

                  (u'bottomSpineSkin_Mid_grp', u'spine_rig', u'transform', u'spine01_Mid_jnt'),
                  (u'bottomSpineSkin_Mid_jnt', None, u'joint', u'spine01_Mid_jnt'),
                  (u'bottomSpineSkin_Mid_ref', u'hips_Mid_anim', u'transform', u'bottomSpineSkin_Mid_jnt'),

                  (u'shaper_grp', None, u'transform', None),
                  (u'spineShaper_grp', u'shaper_grp', u'transform', None)]


""" format: (<controlName>, <controlParent>, <type>, <matchObject>) """
revSpineCtrlDict = [(u'revSpine03Fk_Mid_ctrlGrp', u'root03_Mid_anim', u'transform', u'spine03Fk_Mid_anim'),
                    (u'revSpine03Fk_Mid_anim', u'revSpine03Fk_Mid_ctrlGrp', u'transform', u'revSpine03Fk_Mid_ctrlGrp'),
                    
                    (u'revSpine02Fk_Mid_ctrlGrp', u'revSpine03Fk_Mid_anim', u'transform', u'spine02Fk_Mid_anim'),
                    (u'revSpine02Fk_Mid_anim', u'revSpine02Fk_Mid_ctrlGrp', u'transform', u'revSpine02Fk_Mid_ctrlGrp'),

                    (u'revSpine01Fk_Mid_ctrlGrp', u'revSpine02Fk_Mid_anim', u'transform', u'spine01Fk_Mid_anim'),
                    (u'revSpine01Fk_Mid_anim', u'revSpine01Fk_Mid_ctrlGrp', u'transform', u'revSpine01Fk_Mid_ctrlGrp')]


splineCircleDict = {u'chest_Mid_anim': {'radius': 15.0, 'degree': 1, 'sections': 6,
                                        'rotate': 30.0, 'offset': 0.0, 'color': 20},
                    u'hips_Mid_anim': {'radius': 20.0,  'degree': 1, 'sections': 6,
                                       'rotate': 30.0, 'offset': 0.0, 'color': 20},
                    u'spine01Fk_Mid_anim': {'radius': 15.0, 'degree': 1, 'sections': 6,
                                            'rotate': 30.0, 'offset': 0.0, 'color': 17},
                    u'spine02Fk_Mid_anim': {'radius': 15.0, 'degree': 1, 'sections': 6,
                                            'rotate': 30.0, 'offset': 0.0, 'color': 17}}

spineUpVectors = {u'bottomSpineSkin_Mid_loc': u'pelvis_Mid_anim', u'topSpineSkin_Mid_loc': u'spine03Fk_Mid_anim'}

spineControls = [u'spineIK_Mid_ikh',  u'spine01_Mid_jnt', u'spineEnd_Mid_jnt',
                 u'bottomSpineSkin_Mid_jnt', u'topSpineSkin_Mid_jnt', u'spine_curve_skinCluster',
                 u'spine_rig', u'bottomSpineSkin_Mid_loc', u'topSpineSkin_Mid_loc']

spinePCDict = {u'hips_Mid_ref': u'hips_Mid_jnt', u'chest_Mid_ref': u'chest_Mid_bind',
               u'bottomSpineSkin_Mid_ref': u'bottomSpineSkin_Mid_jnt',
               u'topSpineSkin_Mid_ref': u'topSpineSkin_Mid_jnt'}

curvNode = spineControls[0] + '_arcLength'
backNode = 'back_curve_normalizedScale'


spineShdNodes = ['spine_exp_spineCurveInfo_divBy_world_anim_mult']

spineAttrs = {spineShdNodes[0]: {'setAttr': {'operation': 2}, 'lockAttr': [],
                                 'connectAttr': []},
              backNode: {'setAttr': {'operation': 2},
                         'lockAttr': [], 'connectAttr': []},
              curvNode: {'setAttr': {}, 'lockAttr': [],
                         'connectAttr': [('normalizedScale', spineShdNodes[0] + '.input1X')]},
              'world_anim': {'setAttr': {}, 'lockAttr': [],
                             'connectAttr': [('globalScale', spineShdNodes[0] + '.input2X')]},
              'bottomSpineSkin_Mid_jnt': {'setAttr': {'drawStyle': 0}, 'lockAttr': [],
                                          'connectAttr': []},
              'topSpineSkin_Mid_jnt': {'setAttr': {'drawStyle': 0}, 'lockAttr': [],
                                       'connectAttr': []}}

spineJoints = [u'spine01_Mid_jnt', u'spine02_Mid_jnt', u'spine03_Mid_jnt', u'spine04_Mid_jnt']


def prep_root_anim():
    li = []
    for f in ["root02_Mid_anim.mb", "root03_Mid_anim.mb"]:
        p = os.path.join(tools.shapesLib, f)
        li += pm.importFile(p, returnNewNodes=True)
        tools.match_to(f[:-3], "root_Mid_anim")
        pm.parent(f[:-3], "root_Mid_anim")
    pm.parent("root03_Mid_anim", "root02_Mid_anim")
    pm.parent("spine01Fk_Mid_a0", "hips_Mid_a0", "root03_Mid_anim")
    scripts = [x for x in li if x.type() == 'script']
    pm.delete(scripts)


def prep_world_anim(x):
    tools.create_attributes(x, " ", ["globalScale"])
    attr = x + ".globalScale"
    pm.addAttr(attr, edit=True, hasMinValue=True, minValue=0.01)
    pm.setAttr(attr, 1.0)
    for y in [".scaleX", ".scaleY", ".scaleZ"]:
        attr1 = x + y
        attr2 = "shaper_grp" + y
        pm.connectAttr(attr, attr1)
        pm.connectAttr(attr, attr2)
        pm.setAttr(attr1, lock=True, keyable=False, channelBox=False)


def prep_mid_anim():
    loc = pm.spaceLocator()
    upScene= cmds.upAxis(q=1, ax=1)
    if upScene == 'y':
        ani = tools.make_joint("torso_Mid_anim", zero=True)
        jnt = tools.make_joint("midSpineSkin_Mid_jnt", zero=True)
        print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Y - Up @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ '
    if upScene == 'z':
        ani = tools.make_joint("torso_Mid_anim")
        jnt = tools.make_joint("midSpineSkin_Mid_jnt")
    jnt.setAttr("drawStyle", 0)
    trn = pm.group(name="torso_Mid_a0", empty=True, world=True)
    cmds.setAttr(trn + '.ry', 90)
    con = pm.group(name="torso_Mid_grp", empty=True, parent=trn)
    curve_name = spineControls[0] + "_curve"
    arc_len = pm.PyNode(curvNode).getAttr("arcLength")
    pm.pathAnimation(loc, curve=curve_name, startU=(0.5*arc_len), follow=False)
    """ match the world position of jnt to loc """
    tools.match_xyz(ani, loc)
    tools.match_xyz(jnt, loc)
    pm.delete(loc)
    """ match the trn to jnt """
    tools.match_xyz(trn, ani)
    pm.parent(ani, con)
    pm.parent(trn, "spine01Fk_Mid_anim")
    pm.parent(jnt, "root_Mid_jnt")
    pm.parentConstraint(ani, jnt)
    pm.pointConstraint("spine02Fk_Mid_anim", trn, maintainOffset=True)
    pm.pointConstraint("chest_Mid_anim", "hips_Mid_anim", con, maintainOffset=True)
    pm.select(curve_name)
    """ add the new joint to the curve skin cluster, and adjust the weights """
    pm.skinCluster(edit=True, addInfluence=jnt)
    weights = [("bottomSpineSkin_Mid_jnt", 1.0),
               ("bottomSpineSkin_Mid_jnt", 1.0),
               (("bottomSpineSkin_Mid_jnt", 0.5), ("midSpineSkin_Mid_jnt", 0.5)),
               (("midSpineSkin_Mid_jnt", 0.9), ("topSpineSkin_Mid_jnt", 0.1)),
               ("topSpineSkin_Mid_jnt", 1.0),
               ("topSpineSkin_Mid_jnt", 1.0)]
    for i in range(6):
        pm.skinPercent("spine_curve_skinCluster", curve_name + ".cv[{0}]".format(i), transformValue=weights[i])


def prep_spine_shapers():
    for jnt_name in spineJoints + [u'hips_Mid_jnt']:
        jnt = pm.PyNode(jnt_name)
        """ set up the names """
        if jnt_name.startswith("hips"):
            bnd_name = tools.get_new_name(jnt_name.replace("hips", "hipsShaper"), "bind")
        else:
            bnd_name = tools.get_new_name(jnt_name.replace("spine", "spineShaper"), "bind")
        grp_name = bnd_name.rsplit("_", 1)[0] + "_a0"
        ani_name = bnd_name.rsplit("_", 1)[0] + "_anim"
        """ make the objects """
        bnd = tools.make_joint(bnd_name, zero=True)
        bnd.setAttr("drawStyle", 0)
        pm.parent(bnd, jnt, relative=True)
        grp = pm.group(name=grp_name, empty=True)
        ani = tools.make_joint(ani_name, zero=True)
        """ set up the relationships """
        pm.parent(grp, "spineShaper_grp")
        pm.parent(ani, grp, relative=True)
        tools.apply_shape(ani, "spineShaper_anim.mb")
        if ani_name.startswith("hips"):
            ani.setAttr("jointOrientZ", 90)
            tools.rotate_shape(ani.getShape(), [0, 0, -15])
            """ offset both the anim and the bind by -0.2. Technically, only the bind needs this offset, but
                offsetting the anim makes the control line up visually with the bind. """
            offset = -0.2
            tools.match_to(grp, jnt)
            pm.move(0, 0, offset, grp, relative=True)
            pm.parentConstraint(jnt, grp, maintainOffset=True)
            for attr in [".translateX", ".translateZ"]:
                pm.connectAttr(ani_name + attr, bnd_name + attr)
            """ set up a connection between the ani and bnd with an offset of -0.2 on translateY """
            node = pm.createNode("addDoubleLinear", name="hipsShaper_addDoubleLinear")
            pm.connectAttr(ani_name + ".translateY", node + ".input1")
            node.setAttr("input2", offset)
            pm.connectAttr(node + ".output", bnd_name + ".translateY")
            """ set up a connection between the ani and bnd with an inversion of the value """
            node = pm.createNode("multDoubleLinear", name="hipsShaper_multDoubleLinear")
            pm.connectAttr(ani_name + ".rotateY", node + ".input1")
            node.setAttr("input2", -1.0)
            pm.connectAttr(node + ".output", bnd_name + ".rotateX")
            """ build a list of connections """
            attrs = [(".rotateX", ".rotateY"), (".rotateZ", ".rotateZ"), (".scale", ".scale")]
        else:
            pm.parentConstraint(jnt, grp)
            attrs = [(".translate", ".translate"), (".rotate", ".rotate"), (".scale", ".scale")]
        for attr in attrs:
            pm.connectAttr(ani_name + attr[0], bnd_name + attr[1])


def setup_spine():
    makeSplineIK.debug = debug
    tools.make_ctrl_hierarchy(splineCtrlDict, splineCircleDict)
    """ insert root anim controls """
    prep_root_anim()
    """ prep world anim """
    prep_world_anim("world_anim")
    """ prep character_Mid_anim" """
    tools.create_attributes("character_Mid_anim", "visibility", [])
    char = pm.PyNode("character_Mid_anim")
    char.addAttr("char02AnimVis", keyable=True, defaultValue=0.0, maxValue=1.0, minValue=0.0)
    """ setup splineIK """
    makeSplineIK.make_spine_up_vectors(spineUpVectors)
    makeSplineIK.make_spline_ik(spineControls, u'root_Mid_jnt', spinePCDict, numSpans=3)
    makeSplineIK.make_stretch_ik(spineControls, spineShdNodes, spineAttrs, spineJoints, curvNode, backNode)
    """ insert a mid_anim control """
    prep_mid_anim()
    """ insert spine shaper controls """
    prep_spine_shapers()
    """ add Stretch indicators """
    for x in ["chest_Mid_anim", "torso_Mid_anim", "hips_Mid_anim", "pelvis_Mid_anim",
              "spine01Fk_Mid_anim", "spine02Fk_Mid_anim", "spine03Fk_Mid_anim"]:
        pm.PyNode(x).addAttr("Stretch")
        pm.connectAttr(spineShdNodes[0] + ".outputX", x + ".Stretch")
        pm.PyNode(x).setAttr("Stretch", channelBox=True, keyable=False)
    """ setup constraints... """
    pm.pointConstraint("pelvis_Mid_anim", "bottomSpineSkin_Mid_ref")
    pm.pointConstraint("spine03Fk_Mid_anim", "topSpineSkin_Mid_ref")


def setup_reverse_spine():
    """
    This must be run AFTER root03_Mid_anim and hips_Mid_anim have been constructed with setup_spine().

    :return: None
    """
    tools.make_ctrl_hierarchy(revSpineCtrlDict)
    pm.parent("hips_Mid_a0", "revSpine01Fk_Mid_anim")


if __name__ == "__main__":
    setup_spine()
