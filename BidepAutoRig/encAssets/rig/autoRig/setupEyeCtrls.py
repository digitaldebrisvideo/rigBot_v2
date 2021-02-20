import pymel.core as pm
import tools
import os
reload(tools)

__author__ = 'jhachigian'

eyeCtrls = [(u'eye_Mid_loc', None, u'transform', u'head_Mid_bind'),
            (u'eyeAim_Lt_loc', u'eye_Mid_loc', u'transform', u'eye_Lt_bind'),
            (u'eyeUpVector_Lt_loc', u'eye_Mid_loc', u'transform', u'eye_Lt_bind'),
            (u'eyeAim_Rt_loc', u'eye_Mid_loc', u'transform', u'eye_Rt_bind'),
            (u'eyeUpVector_Rt_loc', u'eye_Mid_loc', u'transform', u'eye_Rt_bind')]

rotationOrderList = ["eyeFk_Rt_anim", "eyeFk_Lt_anim"]

eyeShapes_mb = os.path.join(tools.shapesLib, "eyeShapes.mb")


attrHeader = "spaceSwitch"

attrData = {"eye_Mid_anim":["character02_Mid_anim"]}


def editEyeShape(x):
    print "\tEditing shape for:", x
    shp = pm.PyNode(x).getShape()
    tools.rotate_shape(shp, (0, 0, 90))


def setupCtrls():
    pnt = pm.pointConstraint("eye_Rt_bind", "eye_Lt_bind", "eye_Mid_a0", weight=0.1, skip="y")
    pm.delete(pnt)
    for x in ["Lt", "Rt"]:
        """ init variables """
        jnt = "eye_%s_bind" % x
        ani = "eye_%s_anim" % x
        upv = "eyeUpVector_%s_loc" % x
        aim = "eyeAim_%s_loc" % x
        bas = "eye_%s_base" % x
        shp = "eyeFk_%s_anim" % x
        """ align controls """
        tools.match_to(bas, aim)
        pm.setAttr(upv + ".translateZ", 20)
        pnt = pm.pointConstraint(jnt, ani, skip="z")
        pm.delete(pnt)
        pm.makeIdentity("eye_%s_anim" % x, translate=True, apply=True)
        editEyeShape(shp)
        """ constraints """
        print "\tParent Constraining:", aim, "to:", bas
        pm.aimConstraint(ani, aim, worldUpObject=upv, upVector=(0, 1, 0), worldUpType="object", aimVector=(1, 0, 0))
        pm.parentConstraint(aim, bas)
        pm.parentConstraint("eye_%s_fk" % x, jnt, maintainOffset=True)


def setupEyeCtrls():
    print "Setting up eye controls..."
    tools.make_ctrl_hierarchy(eyeCtrls)
    print "Importing:", eyeShapes_mb
    pm.importFile(eyeShapes_mb)
    setupCtrls()
    for eye in rotationOrderList:
        pm.setAttr(eye + ".rotateOrder", 3)
    for obj in attrData:
        attrs = attrData[obj]
        tools.create_attributes(obj, attrHeader, attrs)
        for attr in attrs:
            pm.addAttr(obj + "." + attr, edit=True, hasMaxValue=True, hasMinValue=True, minValue=0.0, maxValue=1.0)
