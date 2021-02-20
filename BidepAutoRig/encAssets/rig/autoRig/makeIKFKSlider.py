import pymel.core as pm
import maya.cmds as cmds
import tools

reload(tools)

__author__ = 'jhachigian'

upScene= cmds.upAxis(q=1, ax=1)
arrowList = [(-2.5, 0, 0),
             (-.5, 0, 1),
             (-.5, 0, 0.5),
             (.5, 0, 0.5),
             (.5, 0, 1),
             (2.5, 0, 0),
             (.5, 0, -1),
             (.5, 0, -.5),
             (-.5, 0, -.5),
             (-.5, 0, -1),
             (-2.5, 0, 0)]

ikfkSliderDict = {"Fk": {"offset": -1.25 - 4.3, "exp": "DRIVEN = 1.0 - DRIVER.FK_IK;"},
                  "Ik": {"offset": -0.7 + 4.0, "exp": "DRIVEN = DRIVER.FK_IK;"}}


def lock_all_channels(x):
    for attr in ['translateX', 'translateY', 'translateZ',
                 'rotateX', 'rotateY', 'rotateZ',
                 'scaleX', 'scaleY', 'scaleZ', 'visibility']:
        pm.setAttr(x + "." + attr, lock=True, keyable=False, channelBox=False)


def select_points(shp):
    pm.select(clear=True)
    spans = pm.getAttr(shp + ".spans")
    pm.select(shp + ".cv[0:%d]" % spans)


def move_points(par, offset):
    txt = pm.PyNode(par)
    for shp in txt.getChildren():
        select_points(shp)
        pm.move(offset[0], offset[1], offset[2], relative=True, localSpace=True, worldSpaceDistance=True)
        pm.select(clear=True)


def init_text(shp, offset):
    select_points(shp)
    pm.move(offset, -1.0, 0, relative=True, localSpace=True, worldSpaceDistance=True)
    pm.xform(rotation=(90, 0, 0))
    pm.select(clear=True)
    pm.delete(shp, constructionHistory=True)


def make_text(text):
    txt = pm.textCurves(text=text, font="Kimberley|w400|h-8", caching=False)
    children = pm.PyNode(txt[0]).getChildren()
    offset = 0
    for x in xrange(0, len(text)):
        chi = children[x]
        trn = chi.getChildren()[0]
        shp = trn.getShape()
        pm.rename(shp, text + "_" + text[x] + "_crv")
        off = chi.getTranslation()[0]
        offset = offset + off
        pm.parent(shp, txt[0], relative=True, shape=True)
        shp.setAttr("overrideDisplayType", 2)
        init_text(shp, offset)
        pm.delete(chi)
        if pm.versions.current() > 201400:
            scale_adjust = 2.5
            select_points(shp)
            pm.xform(scale=(scale_adjust, scale_adjust, scale_adjust))
            pm.select(clear=True)
    if text in ikfkSliderDict:
        offset = [ikfkSliderDict[text]["offset"], 0.0, 0.0]
        if pm.versions.current() > 201400:
            offset[2] = 1.5
        move_points(txt[0], offset)
    pm.select(clear=True)
    return txt[0]


def make_arrow():
    curve = pm.curve(degree=1, point=arrowList)
    pm.transformLimits(curve, translationX=(-2.5, 2.5), enableTranslationX=(True, True))
    lock_all_channels(curve)
    pm.addAttr(curve, longName="FK_IK", attributeType="double", keyable=True, hasMaxValue=True,
               hasMinValue=True, minValue=0.0, maxValue=1.0, niceName="FK - IK")
    return curve


def make_ik_fk_slider(name):
    upScene= cmds.upAxis(q=1, ax=1)
    grp_name = tools.get_new_name(name, "a0")
    grp = pm.group(empty=True, name=grp_name)
    col = tools.find_lr_override_color(name)
    curve = make_arrow()
    tools.set_override_color(curve.getShape(), col)
    pm.parent(curve, grp)
    pm.rename(curve, name)
    for text in ikfkSliderDict:
        txt = make_text(text)
        for child in pm.listRelatives(txt, shapes=True):
            tools.set_override_color(child, col)
        trn = name + "_" + text
        pm.parent(txt, grp)
        pm.rename(txt, name + "_" + text)
        """ the older version of this used an expression. This version uses direct connections. """
        driver = name + ".FK_IK"
        driven1 = trn + ".scaleX"
        driven2 = trn + ".scaleZ"
        if text == "Fk":
            rev = pm.createNode("reverse", name=(name + "_reverse"))
            pm.connectAttr(driver, rev + ".inputX")
            control = rev + ".outputX"
        else:
            control = driver
        pm.connectAttr(control, driven1)
        pm.connectAttr(control, driven2)
    for text in ikfkSliderDict:
        trn = name + "_" + text
        lock_all_channels(trn)
    if upScene == 'y':
        print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ SCENE  UP $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
        cmds.setAttr(grp + '.rx', -90)
    return grp
