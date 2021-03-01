import time
import datetime
import os
import pymel.core as pm
import maya.OpenMaya as om
import tools
import setupIK
import setupFK
import setupStretchIK
import setupSpine
import setupNeck
import setupFingers
import setupRibbons
import setupClavicle
import setupIKFKBlend
import setupEyeCtrls
import setupTorso
import setupGeoViz
import makeIKFKSlider
import b4AutoRigOptions
import setupHandPoses
import setupTrapezius
import setupScapula
import setupWrists
import encLib
import maya.cmds as cmds
t = time.time()
debug = True

reload(tools)
reload(setupIK)
reload(setupFK)
reload(setupStretchIK)
reload(setupSpine)
reload(setupNeck)
reload(setupFingers)
reload(setupRibbons)
reload(setupClavicle)
reload(setupIKFKBlend)
reload(setupEyeCtrls)
reload(setupTorso)
reload(setupGeoViz)
reload(makeIKFKSlider)
reload(b4AutoRigOptions)
reload(setupHandPoses)
reload(setupTrapezius)
reload(setupScapula)
reload(setupWrists)
reload(encLib)

__author__ = 'jhachigian'

doNotLockScale = ["world_anim", "trap_Lt_anim", "trap_Rt_anim", "torso_Lt_anim", "torso_Rt_anim",
                  "spineShaper01_Mid_anim", "spineShaper02_Mid_anim", "spineShaper03_Mid_anim",
                  "spineShaper04_Mid_anim", "hipsShaper_Mid_anim",
                  "headTop_Mid_anim", "headRear_Mid_anim", "headSide_Lt_anim", "headSide_Rt_anim"]

""" key/value format: {parent: (children)} """
parentDict = {"controls_grp": ("world_anim", "shaper_grp"),
              "world_anim": ("armRibbonCtrl_Lt_grp", "armRibbonCtrl_Rt_grp",
                             "legRibbonCtrl_Lt_grp", "legRibbonCtrl_Rt_grp"),
              "character_Mid_anim": ("neck_ctrls",
                                     "fingers_Rt_a0", "fingers_Lt_a0",
                                     "legIk_Lt_a0", "legIk_Rt_a0",
                                     "handIk_Lt_a0", "handIk_Rt_a0",
                                     "kneeUpVectorIk_Lt_a0", "kneeUpVectorIk_Rt_a0",
                                     "elbowUpVectorIk_Lt_a0", "elbowUpVectorIk_Rt_a0",
                                     "torso_Lt_a0", "torso_Rt_a0", "collar_Lt_a0", "collar_Rt_a0"),
              "tech_grp": ("spine_rig", "neck_rig", "rotateReader_grp",
                           "armRig_Rt_grp", "armRig_Lt_grp", "legRig_Rt_grp", "legRig_Lt_grp"),
              "display_grp": ("kneePV_Rt_a0", "kneePV_Lt_a0", "elbowPV_Lt_a0", "elbowPV_Rt_a0"),
              "spine03Fk_Mid_anim": ("clavicle_Lt_a0", "clavicle_Rt_a0",
                                     "armBase_Rt_loc", "armBase_Lt_loc",
                                     "armIKFK_Rt_a0", "armIKFK_Lt_a0",),
              # "head_Mid_anim": ("eye_Lt_base", "eye_Rt_base", "eye_Mid_a0", "eye_Mid_loc"),
              "pelvis_Mid_anim": ("thigh_Lt_a0", "thigh_Rt_a0", "legIKFK_Rt_a0", "legIKFK_Lt_a0",),
              "armOrient_Rt_loc": "shoulder_Rt_a0",
              "armOrient_Lt_loc": "shoulder_Lt_a0",
              "shaper_grp": ("armShaper_Lt_grp", "armShaper_Rt_grp", "legShaper_Lt_grp", "legShaper_Rt_grp"),
              # "clavicle_Lt_VJ_bind": "trapeziusUpObj_Lt_loc",
              # "clavicle_Rt_VJ_bind": "trapeziusUpObj_Rt_loc",
              "clavicle_Lt_anim": "scapulaCtrl_Lt_grp",
              "clavicle_Rt_anim": "scapulaCtrl_Rt_grp",
              }


parentConstrainDict = {"chest_Mid_ref": (("neck01Fk_Mid_a0", True),
                                         ("torso_Lt_a0", True),
                                         ("torso_Rt_a0", True),
                                         ("collar_Lt_a0", True),
                                         ("collar_Rt_a0", True)),
                       "root_Mid_anim": ("root_Mid_jnt", False)}


ikFkBlend = {'armIKFK_Lt_anim': {'chain': ('shoulder_Lt_jnt', 'elbow_Lt_jnt', 'hand_Lt_jnt'),
                                 'offset': (0, 10, 0)},
             'legIKFK_Lt_anim': {'chain': ('thigh_Lt_jnt', 'knee_Lt_jnt', 'foot_Lt_bind', 'toe_Lt_bind'),
                                 'offset': (0, 0, -10)},
             'armIKFK_Rt_anim': {'chain': ('shoulder_Rt_jnt', 'elbow_Rt_jnt', 'hand_Rt_jnt'),
                                 'offset': (0, -10, 0)},
             'legIKFK_Rt_anim': {'chain': ('thigh_Rt_jnt', 'knee_Rt_jnt', 'foot_Rt_bind', 'toe_Rt_bind'),
                                 'offset': (0, 0, 10)}}

deleteList = ["spine_ctrls"]

shapeOverrides = ["world_anim", "character_Mid_anim", "character02_Mid_anim",
                  "hips_Mid_anim", "pelvis_Mid_anim", "torso_Mid_anim",
                  "spine01Fk_Mid_anim", "spine02Fk_Mid_anim", "chest_Mid_anim", "spine03Fk_Mid_anim",
                  "neck01Fk_Mid_anim", "head_Mid_anim",
                  "clavicle_Lt_anim", "clavicle_Rt_anim",
                  "legIk_Lt_anim", "legIk_Rt_anim",
                  "kneeUpVectorIk_Lt_anim", "kneeUpVectorIk_Rt_anim",
                  "elbowUpVectorIk_Lt_anim", "elbowUpVectorIk_Rt_anim",
                  "revSpine01Fk_Mid_anim", "revSpine02Fk_Mid_anim", "revSpine03Fk_Mid_anim"]

rotateOverrides = ["elbowUpVectorIk_Lt_anim", "elbowUpVectorIk_Rt_anim"]

colorOverrides = {"chest_Mid_anim": 17, "neck01Fk_Mid_anim": 25, "hips_Mid_anim": 17}

volume_joint_targets = ["thumb01_*t_bind", "thumb02_*t_bind",
                        "index01_*t_bind", "index02_*t_bind", "index03_*t_bind", "middle03_*t_bind",
                        "middle02_*t_bind", "middle01_*t_bind", "ring03_*t_bind", "ring02_*t_bind",
                        "ring01_*t_bind", "pinky03_*t_bind", "pinky02_*t_bind", "pinky01_*t_bind", "toe_*t_bind"]

partial_joint_targets = ["thumbCarpal_*t_bind", "foot_*t_bind", "thigh_*t_jnt"]

constraint_targets = ["character_Mid_anim", "root_Mid_anim"]

body_ctrls_vis_targets = ['armIKFK_Lt_anim', 'armIKFK_Rt_anim', 'chest_Mid_anim', 'clavicle_Lt_anim',
                          'clavicle_Rt_anim', 'collar_Lt_anim', 'collar_Rt_anim', 'elbowUpVectorIk_Lt_anim',
                          'elbowUpVectorIk_Rt_anim', 'elbow_Lt_anim', 'elbow_Rt_anim', 'fingerPoses_Lt_anim',
                          'fingerPoses_Rt_anim', 'foot_Lt_anim', 'foot_Rt_anim', 'handIk_Lt_anim',
                          'handIk_Rt_anim', 'hand_Lt_anim', 'hand_Rt_anim', 'head_Mid_anim', 'heel_Lt_anim',
                          'heel_Rt_anim', 'hips_Mid_anim', 'index01_Lt_anim', 'index01_Rt_anim', 'index02_Lt_anim',
                          'index02_Rt_anim', 'index03_Lt_anim', 'index03_Rt_anim', 'kneeUpVectorIk_Lt_anim',
                          'kneeUpVectorIk_Rt_anim', 'knee_Lt_anim', 'knee_Rt_anim', 'legIKFK_Lt_anim',
                          'legIKFK_Rt_anim', 'legIk_Lt_anim', 'legIk_Rt_anim', 'neck01Fk_Mid_anim', 'pelvis_Mid_anim',
                          'root_Mid_anim', 'scapula_Lt_anim', 'scapula_Rt_anim', 'shoulder_Lt_anim', 'shoulder_Rt_anim',
                          'spine01Fk_Mid_anim', 'spine02Fk_Mid_anim', 'spine03Fk_Mid_anim', 'spineIKFK_anim',
                          'thigh_Lt_anim', 'thigh_Rt_anim', 'toe_Lt_anim', 'toe_Rt_anim', 'torso_Lt_anim',
                          'torso_Mid_anim', 'torso_Rt_anim', 'indexCarpal_Lt_anim', 'indexCarpal_Rt_anim',
                          'middle01_Lt_anim', 'middle01_Rt_anim', 'middle02_Lt_anim', 'middle02_Rt_anim',
                          'middle03_Lt_anim', 'middle03_Rt_anim', 'middleCarpal_Lt_anim', 'middleCarpal_Rt_anim',
                          'pinky01_Lt_anim', 'pinky01_Rt_anim', 'pinky02_Lt_anim', 'pinky02_Rt_anim', 'pinky03_Lt_anim',
                          'pinky03_Rt_anim', 'pinkyCarpal_Lt_anim', 'pinkyCarpal_Rt_anim', 'ring01_Rt_anim',
                          'ring01_Lt_anim', 'ring02_Lt_anim', 'ring02_Rt_anim', 'ring03_Rt_anim', 'ring03_Lt_anim',
                          'ringCarpal_Lt_anim', 'ringCarpal_Rt_anim',
                          'thumbCarpal_Lt_anim', 'thumb01_Lt_anim', 'thumb02_Lt_anim',
                          'thumbCarpal_Rt_anim', 'thumb01_Rt_anim', 'thumb02_Rt_anim',
                          'toeTip_Rt_anim', 'toeTip_Lt_anim',
                          'legIKFK_Lt_anim_Ik', 'legIKFK_Lt_anim_Fk', 'legIKFK_Rt_anim_Ik', 'legIKFK_Rt_anim_Fk',
                          'armIKFK_Rt_anim_Ik', 'armIKFK_Rt_anim_Fk', 'armIKFK_Lt_anim_Ik', 'armIKFK_Lt_anim_Fk',
                          'kneePV_Rt_jnt', 'kneePV_Lt_jnt', 'elbowPV_Rt_jnt', 'elbowPV_Lt_jnt']

head_mm_vis_targets = ["headTop_Mid_anim", "headRear_Mid_anim", "headSide_Lt_anim", "headSide_Rt_anim"]


def set_debug(quiet):
    x = not quiet
    global debug
    debug = x
    for mod in [tools, setupSpine, setupFingers, setupStretchIK,  # setupTrapezius,
                setupClavicle, setupIK, setupFK, setupIKFKBlend, setupWrists, setupRibbons]:
        mod.debug = x


def build_rig():
    tools.debug_print("Building rig...\n", dbg=debug)
    setupIK.setup_ik()
    setupFK.setup_fk()
    setupIKFKBlend.setup_ik_fk_blend()
    setupStretchIK.setup_stretch_ik()
    setupWrists.setup_wrists()
    setupSpine.setup_spine()
    setupSpine.setup_reverse_spine()
    setupNeck.setup_neck()
    setupNeck.setup_head()
    setupRibbons.setup_ribbons()
    setupFingers.setup_hand()
    setupClavicle.setup_clavicle()
    setupTorso.setup_torso()
    setupGeoViz.setup_geo_viz()
    setupTrapezius.setup_trapezius()
    setupScapula.setup_scapula()
    b4AutoRigOptions.makeFaceGuides(control="visibility_anim")
    b4AutoRigOptions.makeDistanceWarning(subject="hips_Mid_jnt", distance=80000, parent="root_Mid_anim")
    tools.debug_print("", dbg=debug)


def connect_weights(obj, con, li):
    for i in xrange(len(li)):
        tgt = li[i]
        weight = "%s.%sW%d" % (con, tgt, i)
        control = "%s.%s" % (obj, tgt)
        pm.connectAttr(control, weight, force=True)


def setup_space_switching(d):
    for obj in d:
        tools.debug_print("Initializing multifactor space switching...", dbg=debug)
        """ unpack data """
        par = d[obj]["object"]
        const = d[obj]["constraint"]
        tgts = d[obj]["targets"]
        it = d[obj]["interpType"]
        """ apply data """
        con = const(tgts, par, maintainOffset=True)
        con.setAttr('interpType', it)
        connect_weights(obj, con, tgts)


def setup_binary_space_switching(d):
    for obj in d:
        tools.debug_print("Initializing binary space switching for: " + obj, dbg=debug)
        par = pm.PyNode(obj).getParent()
        tgt1 = d[obj][0]
        tgt2 = par.getParent()
        pnt = pm.parentConstraint(tgt1, tgt2, par, weight=0.0, maintainOffset=True)
        pnt.setAttr('interpType', 2)
        attrs = pm.parentConstraint(pnt, query=True, weightAliasList=True)
        rev = pm.createNode("reverse", name=(obj + "_reverse"))
        control = obj + "." + tgt1
        pm.connectAttr(control, rev + ".inputX")
        pm.connectAttr(control, attrs[0])
        pm.connectAttr(rev + ".outputX", attrs[1])


def hide_objects():
    tools.debug_print("Hiding objects...\n", dbg=debug)
    tools.aim_constraint_up_vector_vis(False)
    tools.pattern_visibility("*Skin_*_loc", False)
    tools.pattern_visibility("*Aim_*_loc", False)
    tools.pattern_visibility("**_ikh", False)
    tools.pattern_visibility("*t_fk", False, maya_type="joint")
    tools.pattern_visibility("*t_ik", False, maya_type="joint")
    tools.pattern_visibility("setup_grp", False)
    tools.pattern_visibility("armRig_*_grp", False)
    tools.pattern_visibility("legRig_*_grp", False)
    tools.pattern_visibility("*RollVector_*t_jnt", False)
    tools.pattern_visibility("*RibbonMid_*t_jnt", False)
    # tools.pattern_visibility("indexCarpal_*t_boxShape", False)
    # tools.pattern_visibility("middleCarpal_*t_boxShape", False)
    tools.list_visibility(setupFingers.blacklist, False)
    tools.list_visibility(['bottomSpineSkin_Mid_jnt', 'topSpineSkin_Mid_jnt', 'midSpineSkin_Mid_jnt'], False)
    tools.pattern_visibility("scapulaUpObj_*_loc", False)
    tools.pattern_visibility("scapulaTarget_*_loc", False)
    tools.debug_print("", dbg=debug)


def delete_objects():
    tools.debug_print("Deleting leftover objects...", dbg=debug)
    for obj in deleteList:
        tools.debug_print("\tDeleting: " + obj, dbg=debug)
        pm.delete(obj)
    tools.debug_print("", dbg=debug)


def connect_attrs():
    tools.debug_print("Connecting attrs...", dbg=debug)
    for x in ["X", "Y", "Z"]:
        pm.connectAttr("world_anim.globalScale", "skeleton_grp.scale%s" % x)
        pm.connectAttr("world_anim.globalScale", "visSwitch_grp.scale%s" % x)
    for x in ["armGlobalScale_Lt_UTmd", "armGlobalScale_Rt_UTmd", "legGlobalScale_Lt_UTmd", "legGlobalScale_Rt_UTmd"]:
        pm.connectAttr("world_anim.globalScale", x + ".input2X")
    for key in ["arm", "leg"]:
        for side in ["Lt", "Rt"]:
            ctrl = "%sIKFK_%s_anim" % (key, side)
            info = setupRibbons.info[key][side]
            pm.connectAttr(ctrl + ".bendyTwistyCtrlsVis", info["lwr"]['twistCtrlMid'].getShape() + ".visibility")
            pm.connectAttr(ctrl + ".gimbalCtrlVis", setupFK.visDict[side][key].getShape() + ".visibility")
            pm.connectAttr(ctrl + ".gimbalCtrlVis", setupIK.visDict[side][key].getShape() + ".visibility")
            for pre in ["upr", "lwr"]:
                pm.connectAttr(ctrl + ".bendyTwistyCtrlsVis", info[pre]['twistCtrl'].getShape() + ".visibility")
                pm.connectAttr(ctrl + ".bendyTwistyCtrlsVis", info[pre]['midAnim'].getShape() + ".visibility")
                for shp in info[pre]['shapers']['anims']:
                    pm.connectAttr(ctrl + ".shaperCtrlsVis", shp.getShape() + ".visibility")


def hide_attrs():
    blacklist = doNotLockScale + [x.name() for x in pm.ls("*Shaper*_anim")]
    rig_objects = [x for x in pm.listRelatives("rig_XXX_grp", type=('transform', 'joint'), allDescendents=True)
                   if x.name() not in blacklist]
    tools.debug_print("Locking scale on " + str(len(rig_objects)) + "objects...", dbg=debug)
    tools.lock_attributes(rig_objects, ['scaleX', 'scaleY', 'scaleZ'])


def apply_shapes():
    tools.apply_circle("root_Mid_anim", (0, 1, 0), radius=40.0, degree=1, sections=4, rotate=45.0, color=17)
    for anim in shapeOverrides:
        pm.refresh(force=True)  # this keeps the spine from snapping out-of-place during the autorig build.
        if cmds.objExists (anim):
            shp = tools.apply_shape(anim)
            if shp:
                if anim in rotateOverrides:
                    tools.rotate_shape(shp, (0, 0, 90))
                if anim in colorOverrides:
                    col = colorOverrides[anim]
                    tools.set_override_color(shp, col)


def lock_anims():
    li = pm.ls("*_anim")
    tools.debug_print("Locking visibility on " + str(len(li)) + " items.", dbg=debug)
    tools.lock_attributes(li, ['visibility'])
    li = pm.ls("*_anim", type='joint')
    tools.debug_print("Locking radius on " + str(len(li)) + " items.", dbg=debug)
    tools.lock_attributes(li, ['radius'])


def create_sets():
    blacklist = setupFingers.blacklist + pm.ls("*_ConstrainMe_*")
    li = [x for x in pm.ls("*_anim") if x not in blacklist]
    additional_items = ["character_Mid_ConstrainMe_anim", "root_Mid_ConstrainMe_anim"]
    add_ons = [x for x in additional_items if pm.objExists(x)]
    li += add_ons
    pm.sets(li, name="all_ctrls")
    """ hand ctrl sets """
    li = [x for x in setupFingers.hand_sel_list if x.find("_Lt_") != -1 and x not in blacklist]
    li.insert(0, setupHandPoses.handCtrls[0])
    pm.sets(li, name="hand_Lt_ctrls")
    li = [x for x in setupFingers.hand_sel_list if x.find("_Rt_") != -1 and x not in blacklist]
    li.insert(0, setupHandPoses.handCtrls[1])
    pm.sets(li, name="hand_Rt_ctrls")
    """ torso_ctrls """
    temp = []
    for pattern in ["root", "hips", "pelvis", "spine", "chest", "scapula", "torso", "trap"]:
        temp += pm.ls("*" + pattern + "*_anim")
    li = [x for x in temp if x not in blacklist]
    pm.sets(li, name="torso_ctrls")
    """ body_ctrls """
    for pattern in ["*Shaper*", "*character*", "*Ribbon*", "*Gimbal*", "*Twist*"]:
        blacklist += pm.ls(pattern)
    blacklist += ["world_anim", "visibility_anim"]
    li = [x for x in pm.ls("*_anim") if x not in blacklist]
    li += add_ons
    pm.sets(li, name="body_ctrls")


def prep_spine_ik_fk_vis():
    upScene= cmds.upAxis(q=1, ax=1)

    name = "spineIKFK_anim"
    """ create slider and place its parent group """
    slider = makeIKFKSlider.make_ik_fk_slider(name)
    tools.match_xyz(slider, "root03_Mid_anim")
    slider.setParent("root03_Mid_anim")
    # slider.setAttr("translate", [-28, 2.5, -28])
    if upScene == 'z':
        slider.setAttr("translate", [-42, 2.5, 0])
    if upScene == 'y':
        slider.setAttr("translate", [0, 2.5, -42])
    slider.setAttr("scale", (2, 2, 2))

    """ set up anim """
    ani = pm.PyNode(name)
    ani.setAttr("FK_IK", 0.5)
    tools.set_override_color(ani.getShape(), 26)

    """ prep attrs """
    pm.addAttr(name + ".FK_IK", edit=True, minValue=-1.0)
    pm.setAttr(name + '_Ik.visibility', edit=True, lock=False)
    pm.setAttr(name + '_Fk.visibility', edit=True, lock=False)
    attrs = [u'extraRootAnimVis', u'stretchIndicatorVis', u'shaperAnimVis', u'reverseSpineCtrlVis']
    for attr in attrs:
        ani.addAttr(attr, keyable=True, defaultValue=0.0, minValue=0.0, maxValue=1.0)

    ani.addAttr(u'ConstrainTorsoMidAnimIK', keyable=True, defaultValue=0, minValue=0, maxValue=1, attributeType='short')

    """ import stretchIndicator """
    f = os.path.join(tools.shapesLib, "stretchIndicator_grp.mb")
    li = pm.importFile(f, returnNewNodes=True)
    pm.parent("stretchIndicator_grp", "root_Mid_anim")
    imported_scripts = [x for x in li if x.type() == "script"]

    """ setup ik/fk visibility """
    ik = [u'chest_Mid_animShape', u'spineIKFK_anim_Ik', u'torso_Mid_animShape', u'hips_Mid_animShape']
    fk = [u'spine01Fk_Mid_animShape', u'spineIKFK_anim_Fk', u'spine02Fk_Mid_animShape',
          u'spine03Fk_Mid_animShape', u'pelvis_Mid_animShape']
    old = [u'spine01Fk_Mid_animShape', u'spine02Fk_Mid_animShape', u'chest_Mid_animShape', u'hips_Mid_animShape']
    old_diff = [x for x in (ik + fk) if x not in old]
    cd = name + ".FK_IK"
    """ ik """
    pm.setDrivenKeyframe(ik, attribute="visibility", currentDriver=cd, driverValue=1, value=1)
    pm.setDrivenKeyframe(ik, attribute="visibility", currentDriver=cd, driverValue=0, value=0)
    """ fk """
    pm.setDrivenKeyframe(fk, attribute="visibility", currentDriver=cd, driverValue=0, value=1)
    pm.setDrivenKeyframe(fk, attribute="visibility", currentDriver=cd, driverValue=1, value=0)
    """ old """
    pm.setDrivenKeyframe(old, attribute="visibility", currentDriver=cd, driverValue=-1, value=1)
    pm.setDrivenKeyframe(old_diff, attribute="visibility", currentDriver=cd, driverValue=-1, value=0)

    """ setup root visibility """
    for x in [u'root03_Mid_animShape', u'root02_Mid_animShape']:
        pm.connectAttr(name + ".extraRootAnimVis", x + ".visibility")

    """ setup stretch indicator and visibility """
    pm.connectAttr("spine_exp_spineCurveInfo_divBy_world_anim_mult.outputX", "stretchIndicatorLevel.translateY")
    pm.connectAttr(name + ".stretchIndicatorVis", "stretchIndicator_grp.visibility")

    """ setup shaper visibility """
    for i in (1, 2, 3, 4):
        shaper = "spineShaper{:02d}_Mid_anim".format(i)
        pm.connectAttr(name + ".shaperAnimVis", shaper + ".visibility")
    pm.connectAttr(name + ".shaperAnimVis", "hipsShaper_Mid_anim.visibility")

    """ setup reverse spline visibility """
    for i in (1, 2, 3):
        reverse_spline = "revSpine{:02d}Fk_Mid_animShape".format(i)
        pm.connectAttr(name + ".reverseSpineCtrlVis", reverse_spline + ".visibility")

    """ connect torso_Mid_grp pointConstraint """
    con = pm.ls("torso_Mid_grp_*", type="pointConstraint")[0]
    weight_attrs = con.getWeightAliasList()
    for w in weight_attrs:
        pm.connectAttr(name + ".ConstrainTorsoMidAnimIK", w)

    """ cleanup on Aisle 4 """
    pm.delete(imported_scripts)


def adjust_radii():
    d = {5: ["armRollReader_*t_jnt", "neck0*Fix_Bk_bind", "neck0*_VJ_bind"],
         10: ["hipsShaper_Mid_bind", "spineShaper0*_Mid_bind", "*ArmRibbon0*_*t_bind",
              "*LegRibbon0*_*t_bind", "wrist_*t_bind", "elbow_*t_VJ_bind", "head_VJ_bind"]}
    for val in d:
        for pattern in d[val]:
            for node in pm.ls(pattern, type="joint"):
                node.setAttr("radius", val)
                
                
def add_volume_joints():
    targets = []
    for pattern in volume_joint_targets:
        targets += [x for x in pm.ls(pattern)]
    for target in targets:
        tools.add_volume_joint(target)


def add_partial_joints():
    targets = []
    for pattern in partial_joint_targets:
        targets += [x for x in pm.ls(pattern)]
    for target in targets:
        tools.add_partial_joint(target)


def add_elbow_fix_joints():
    flip = {"Lt": 1, "Rt": -1}
    for side in ["Lt", "Rt"]:
        n = flip[side]
        front_name = "elbowFrontFix_%s_bind" % side
        back_name = "elbowBackFix_%s_bind" % side
        vj = "elbow_%s_VJ_bind" % side
        for name in [front_name, back_name]:
            pm.select(vj)
            pm.joint(name=name)
        d = {
            front_name: {"translateY": [{"cd": vj + ".rotateZ", "keys": [(0, 4 * n), (-40, 8 * n)]}]},
            back_name: {"translateY": [{"cd": vj + ".rotateZ", "keys": [(0, -4 * n), (-40, -8 * n)]}]}
            }
        for obj in d:
            for attr in d[obj]:
                for x in d[obj][attr]:
                    for key in x["keys"]:
                        cd = x["cd"]
                        pm.setDrivenKeyframe(obj, attribute=attr, currentDriver=cd, driverValue=key[0], value=key[1],
                                             inTangentType='linear', outTangentType='linear')


def insert_constraint_targets():
    for target in constraint_targets:
        node = pm.PyNode(target)
        par = node.getParent()
        grp_name = tools.get_new_name(target, "ConstrainMe_anim")
        grp = pm.group(name=grp_name, empty=True)
        grp.setParent(par, relative=True)
        node.setParent(grp, relative=True)


def set_interpolation_type():
    """
    Set all parent constraint interpolation types to "Shortest."
    :return: None
    """
    tools.debug_print("Setting all parent constraints to \"shortest\" type interpolation.", dbg=debug)
    li = pm.ls(type="parentConstraint")
    for x in li:
        x.setAttr("interpType", 2)


def setup_visibility_anim():
    """
    :return: None
    """
    """ setup visibility anim attributes """
    vis = pm.PyNode("visibility_anim")
    for tup in [("bodyCtrlsVis", body_ctrls_vis_targets, 1.0), ("headMMCtrlVis", head_mm_vis_targets, 0.0)]:
        attr = tup[0]
        vis.addAttr(attr, attributeType='double', defaultValue=tup[2], minValue=0.0, maxValue=1.0, keyable=True)
        for transform in tup[1]:
            if not pm.objExists(transform):
                continue
            shapes = pm.PyNode(transform).getShapes()
            for shp in shapes:
                pm.connectAttr("visibility_anim." + attr, shp + ".lodVisibility")


@encLib.apply_wait_cursor
def auto_rig_routine():
    build_rig()
    add_volume_joints()
    add_partial_joints()
    add_elbow_fix_joints()
    insert_constraint_targets()
    tools.parent_objects(parentDict)
    """ jntHeir02_grp section """
    pm.parent(pm.PyNode("root_Mid_jnt").getChildren(type='joint'), "jntHeir02_grp")
    """ character_Mid_anim section """
    li = [x for x in pm.PyNode("character_Mid_anim").getChildren(type='transform') if x.name() != "character02_Mid_a0"]
    pm.parent(li, "character02_Mid_anim")
    """ parent constraint """
    tools.parent_constraint_objects(parentConstrainDict)
    setup_space_switching(setupIK.pvAttrData)
    setup_space_switching(setupNeck.attrData)
    setup_space_switching(setupIKFKBlend.spaceSwitching)
    hide_objects()
    connect_attrs()
    hide_attrs()
    delete_objects()
    apply_shapes()
    """ connect shape visibility control(s) """
    pm.connectAttr("character_Mid_anim.char02AnimVis", "character02_Mid_animShape.visibility")
    setup_visibility_anim()
    prep_spine_ik_fk_vis()
    """ misc """
    adjust_radii()
    setupHandPoses.setup_hand_poses()
    set_interpolation_type()
    """ lock attrs """
    lock_anims()
    create_sets()


def autoRig(quiet=False):
    set_debug(quiet)
    before = len(pm.ls())
    state = pm.undoInfo(query=True, state=True)
    pm.undoInfo(state=False)
    msg = ""
    try:
        auto_rig_routine()
    except Exception as e:
        msg += "WARNING: the autorig cut out before it finished. Check the rig!!!\n\n"
        print type(e)
        print e
    finally:
        pm.undoInfo(state=state)
    """ finishing moves """
    pm.select(clear=True)
    after = len(pm.ls())
    delta = int(time.time()-t)
    msg += "Autorig finished building in: " + str(datetime.timedelta(seconds=delta))
    msg += "\r\n\r\n(%d nodes added)" % (after - before)
    om.MGlobal.displayInfo(msg)
    # pm.confirmDialog(title="Done", message=msg)
