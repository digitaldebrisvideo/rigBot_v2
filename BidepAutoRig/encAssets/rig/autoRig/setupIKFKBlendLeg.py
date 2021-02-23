import pymel.core as pm
import maya.cmds as cmds
import tools
import makeIKFKSlider

reload(tools)
reload(makeIKFKSlider)

__author__ = 'jhachigian'

debug = True
upScene= cmds.upAxis(q=1, ax=1)
ikFkBlend = {
             'legIKFK_Lt_anim': {'chain': ('thigh_Lt_jnt', 'knee_Lt_jnt', 'foot_Lt_bind', 'toe_Lt_bind'),
                                 'offset': (12, 0, -22), 'default': 1.0,
                                 'ik': ('legIk_Lt_anim', 'heel_Lt_anim', 'toeTip_Lt_anim',
                                        'kneeUpVectorIk_Lt_anim', 'kneePV_Lt_a0')},
             'legIKFK_Rt_anim': {'chain': ('thigh_Rt_jnt', 'knee_Rt_jnt', 'foot_Rt_bind', 'toe_Rt_bind'),
                                 'offset': (-12, 0, 22), 'default': 1.0,
                                 'ik': ('legIk_Rt_anim', 'heel_Rt_anim', 'toeTip_Rt_anim',
                                        'kneeUpVectorIk_Rt_anim', 'kneePV_Rt_a0')}}




spaceSwitching = {}


for obj in ikFkBlend:
    key = ikFkBlend[obj]['ik'][0]
    spaceSwitching[key] = {}
    """ add additional data """
    if obj.startswith('arm'):
        spaceSwitching[key]['targets'] = ['world_anim', 'character02_Mid_anim', 'root03_Mid_anim', 'pelvis_Mid_anim',
                                     'spine03Fk_Mid_anim', 'head_Mid_anim', 'clavicle_%s_anim' % tools.get_lr(obj)]
        spaceSwitching[key]['def'] = 'spine03Fk_Mid_anim'
    else:
        spaceSwitching[key]['targets'] = ['world_anim', 'character02_Mid_anim', 'root03_Mid_anim', 'pelvis_Mid_anim']
        spaceSwitching[key]['def'] = 'character02_Mid_anim'
    spaceSwitching[key]['interpType'] = 2
    spaceSwitching[key]['constraint'] = pm.parentConstraint
    spaceSwitching[key]['object'] = tools.get_new_name(key, "a0")

ikAttrHeader = "spaceSwitch"


def apply_constraint(d):
    fk = d['fk']
    ik = d['ik']
    tgt = d['tgt']
    const = d['constraint']
    rv = d['reverse']
    at = d['driver']
    tools.debug_print("\tApplying constraint to: " + tgt, dbg=debug)
    cn = const(fk, ik, tgt)
    ws = const(cn, query=True, weightAliasList=True)
    pm.connectAttr(rv + ".outputX", ws[0])
    pm.connectAttr(at, ws[1])
    """ if this is an orientConstraint, set its interpolation type to Shortest """
    if const == pm.orientConstraint:
        cn.setAttr("interpType", 2)


def get_reverse(name, at):
    rv_name = name + "_reverse"
    if pm.objExists(rv_name):
        rv = pm.PyNode(rv_name)
    else:
        rv = pm.shadingNode('reverse', asUtility=True, name=())
        pm.connectAttr(at, rv + ".inputX")
    return rv


def ik_fk_blend(name):
    tools.debug_print("IKFKblend: " + name, dbg=debug)
    tgts = ikFkBlend[name]['chain']
    ik_grp = ikFkBlend[name]['ik']
    at = name + ".FK_IK"
    rv = get_reverse(name, at)
    for ctl in ik_grp:
        pm.connectAttr(at, ctl + ".visibility")
    d = {'driver': at, 'reverse': rv}
    for tgt in tgts:
        d['fk'] = tools.get_new_name(tgt, "fk")
        d['ik'] = tools.get_new_name(tgt, "ik")
        d['tgt'] = tgt
        sp = tools.get_new_name(tgt, "anim")
        locked = ['scaleX', 'scaleY', 'scaleZ']
        """ apply constraints. """
        if tgt == tgts[0]:  # root of limb
            d['constraint'] = pm.parentConstraint
            apply_constraint(d)
        else:
            for const in [pm.pointConstraint, pm.orientConstraint]:
                d['constraint'] = const
                apply_constraint(d)
        pm.connectAttr(rv + ".outputX", sp + ".visibility")
        """ if it's an elbow control, lock two of the rotate channels """
        for attr in locked:
            pm.setAttr(sp + "." + attr, lock=True, keyable=False, channelBox=False)


def setup_ik_fk_blend():
    pm.select(clear=True)
    for name in ikFkBlend:
        tgts = ikFkBlend[name]['chain']
        off = ikFkBlend[name]['offset']
        dft = ikFkBlend[name]['default']
        slider = makeIKFKSlider.make_ik_fk_slider(name)
        toptgt = tgts[0]
        pm.parent(slider, toptgt, relative=True)
        pm.setAttr(slider + ".translate", off)
        pm.setAttr(name + ".FK_IK", dft)
        pm.parent(slider, world=True)
        upScene= cmds.upAxis(q=1, ax=1)
        tools.zero_rotation(slider)
        if upScene == 'y':
            cmds.setAttr(slider + '.rx', -90)
        ik_fk_blend(name)
        """ create ribbon attrs """
        node = pm.PyNode(name)
        # if name.startswith("arm"):
        for attr in ["stretchyOffOn", "bendyTwistyCtrlsVis", "shaperCtrlsVis", "gimbalCtrlVis"]:
            node.addAttr(attr, hasMaxValue=True, hasMinValue=True, minValue=0.0, maxValue=1.0)
            node.setAttr(attr, channelBox=True, type="double")
            node.setAttr(attr, keyable=True)
    """ create space-switching attrs """
    for name in spaceSwitching:
        anim = pm.PyNode(name)
        attrs = spaceSwitching[name]["targets"]
        tools.create_attributes(name, ikAttrHeader, attrs)
        for attr in attrs:
            pm.addAttr(name + "." + attr, edit=True, hasMaxValue=True, hasMinValue=True, minValue=0.0, maxValue=1.0)
        default = spaceSwitching[name]['def']
        anim.setAttr(default, 1)
