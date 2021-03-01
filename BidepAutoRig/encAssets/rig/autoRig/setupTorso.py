import pymel.core as pm
import maya.cmds as cmds

import tools
reload(tools)

__author__ = 'jhachigian'
upScene= cmds.upAxis(q=1, ax=1)
torsoJoints = [(u'torso_lt_a0', None, u'transform', u'torso_lt_bind'),
               (u'torso_lt_a1', u'torso_lt_a0', u'transform', u'torso_lt_bind'),
               (u'torso_lt_anim', u'torso_lt_a1', u'joint', u'torso_lt_bind'),
               (u'torso_rt_a0', None, u'transform', u'torso_rt_bind'),
               (u'torso_rt_a1', u'torso_rt_a0', u'transform', u'torso_rt_bind'),
               (u'torso_rt_anim', u'torso_rt_a1', u'joint', u'torso_rt_bind'),
               (u'collar_lt_a0', None, u'transform', u'collar_lt_bind'),
               (u'collar_lt_a1', u'collar_lt_a0', u'transform', u'collar_lt_bind'),
               (u'collar_lt_anim', u'collar_lt_a1', u'joint', u'collar_lt_bind'),
               (u'collar_rt_a0', None, u'transform', u'collar_rt_bind'),
               (u'collar_rt_a1', u'collar_rt_a0', u'transform', u'collar_rt_bind'),
               (u'collar_rt_anim', u'collar_rt_a1', u'joint', u'collar_rt_bind')]

torsoCircleDict = {u'torso_lt_anim': {'radius': 1.0, 'degree': 1, 'sections': 4,
                                      'rotate': 0.0, 'offset': 3.0, 'color': 18},
                   u'collar_lt_anim': {'radius': 1.0, 'degree': 1, 'sections': 4,
                                     'rotate': 0.0, 'offset': 3.0, 'color': 18},
                   u'torso_rt_anim': {'radius': 1.0, 'degree': 1, 'sections': 4,
                                      'rotate': 0.0, 'offset': 3.0, 'color': 20},
                   u'collar_rt_anim': {'radius': 1.0, 'degree': 1, 'sections': 4,
                                     'rotate': 0.0, 'offset': 3.0, 'color': 20}}

if upScene == 'y':
        torsoAdjust = {u'torso_lt_anim': (0, 0, -90), u'torso_rt_anim': (0, 0, 90)}
if upScene == 'z':
        torsoAdjust = {u'torso_lt_anim': (-90, 0, 0), u'torso_rt_anim': (90, 0, 0)}
torsoPCDict = {u'torso_lt_anim': (u'torso_lt_bind', False),
               u'collar_lt_anim':  (u'collar_lt_bind', False),
               u'torso_rt_anim': (u'torso_rt_bind', False),
               u'collar_rt_anim':  (u'collar_rt_bind', False)}


def setup_anims():
    for anim in torsoAdjust:
        shp = pm.PyNode(anim).getShape()
        rot = torsoAdjust[anim]
        tools.rotate_shape(shp, rot)
        tools.parent_constraint_objects(torsoPCDict)


def setup_connections():
    for bind in ["driven_clavicle_lt_bind", "driven_clavicle_rt_bind"]:
        for n in ("collar", "torso"):
            name = tools.get_new_name(bind, "%s_UTmdl" % n)
            mult = pm.createNode("multDoubleLinear", name=name)
            side = tools.get_lower_lr(bind)
            mult.setAttr("input2", 0.3)
            pm.connectAttr(bind + ".rotateZ", mult + ".input1")
            if upScene == 'y':
                pm.connectAttr(mult + ".output", "%s_%s_a1.translateY" % (n, side))
            if upScene == 'z':
                pm.connectAttr(mult + ".output", "%s_%s_a1.translateZ" % (n, side))
            # pm.connectAttr(mult + ".output", "torso_%s_a1.translateZ" % side)


def setup_torso():
    tools.make_ctrl_hierarchy(torsoJoints, torsoCircleDict)
    setup_anims()
    setup_connections()
