import pymel.core as pm
import tools

reload(tools)

__author__ = 'jhachigian'

debug = True

clavicleDict = {u'clavicle_Lt_bind': {'xMatch': u'clavicleEnd_Lt_jnt'},
                u'clavicle_Rt_bind': {'xMatch': u'clavicleEnd_Rt_jnt'}}

clavicleHierarchy = [(u'armBase_Rt_loc', None, u'transform', u'armBase_Rt_jnt'),
                     (u'armOrient_Rt_loc', u'armBase_Rt_loc', u'transform', u'armBase_Rt_jnt'),
                     (u'armBase_Rt_ref', u'clavicleEnd_Rt_jnt', u'joint', u'armOrient_Rt_jnt'),
                     (u'armBase_Lt_loc', None, u'transform', u'armBase_Lt_jnt'),
                     (u'armOrient_Lt_loc', u'armBase_Lt_loc', u'transform', u'armBase_Lt_jnt'),
                     (u'armBase_Lt_ref', u'clavicleEnd_Lt_jnt', u'joint', u'armOrient_Lt_jnt')]

orientJoints = [(u'armOrient_Rt_jnt', u'armBase_Rt_jnt'),
                (u'armOrient_Lt_jnt', u'armBase_Lt_jnt')]

parentDict = {u'armOrient_Rt_jnt': u'shoulder_Rt_jnt',
              u'armOrient_Lt_jnt': u'shoulder_Lt_jnt'}

pointDict = {u'armBase_Rt_ref': (u'armBase_Rt_jnt', u'armBase_Rt_loc'),
             u'armBase_Lt_ref': (u'armBase_Lt_jnt', u'armBase_Lt_loc')}

orientList = [(u'armBase_Rt_loc', u'armOrient_Rt_loc', 0),
              (u'armBase_Rt_ref', u'armOrient_Rt_loc', 1),
              (u'armBase_Rt_jnt', u'armOrient_Rt_jnt', 0),
              (u'armBase_Rt_ref', u'armOrient_Rt_jnt', 1),
              (u'armBase_Lt_loc', u'armOrient_Lt_loc', 0),
              (u'armBase_Lt_ref', u'armOrient_Lt_loc', 1),
              (u'armBase_Lt_jnt', u'armOrient_Lt_jnt', 0),
              (u'armBase_Lt_ref', u'armOrient_Lt_jnt', 1)]

attributes = {u'clavicle_Lt_anim': {'attributes': [u'chestClavicleLt'],
                                    'spaceSwitch': u'armIKFK_Lt_anim',
                                    'lock': ["radius", "visibility"]},
              u'clavicle_Rt_anim': {'attributes': [u'chestClavicleRt'],
                                    'spaceSwitch': u'armIKFK_Rt_anim',
                                    'lock': ["radius", "visibility"]}}

attrHeader = "spaceSwitch"

connectAttrs = [(u'armIKFK_Lt_anim.chestClavicleLt', (u'armOrient_Lt_jnt_orientConstraint*',
                                                      u'armOrient_Lt_loc_orientConstraint*')),
                (u'armIKFK_Rt_anim.chestClavicleRt', (u'armOrient_Rt_jnt_orientConstraint*',
                                                      u'armOrient_Rt_loc_orientConstraint*'))]


def make_orient_joints():
    for x in orientJoints:
        tools.debug_print("makeOrientJoints: " + str(x), dbg=debug)
        pm.select(clear=True)
        name = x[0]
        par = x[1]
        jnt = tools.make_joint(name, zero=True, world=True)
        pm.parent(jnt, par, relative=True)
        pm.select(clear=True)


def make_clavicle_anim(clavicle):
    grp_name = tools.get_new_name(clavicle, "a0")
    ani_name = tools.get_new_name(clavicle, "anim")
    grp = pm.group(name=grp_name, empty=True)
    ani = tools.make_joint(ani_name, zero=True)
    xmt = clavicleDict[clavicle]['xMatch']
    off = pm.getAttr(xmt + ".translateX")
    off *= 0.75
    col = tools.find_lr_override_color(clavicle)
    tools.apply_circle(ani, (1, 0, 0), radius=10.0, offset=off, color=col)
    pm.parent(ani, grp, relative=True)
    tools.match_to(grp, clavicle)
    pm.parentConstraint(ani, clavicle)
    clavicleDict[clavicle]['group'] = grp
    clavicleDict[clavicle]['anim'] = ani


def setup_clavicle_orient():
    for ori in orientList:
        tools.debug_print("orientConstraint: " + ori[0] + " " + ori[1], dbg=debug)
        con = pm.orientConstraint(ori[0], ori[1], weight=ori[2])
        con.setAttr("interpType", 2)


def link_clavicle_attrs():
    for x in connectAttrs:
        control = x[0]
        tools.debug_print(control, dbg=debug)
        tools.debug_print("\tSetting minimum and maximum limits on: " + control, dbg=debug)
        pm.addAttr(control, edit=True, hasMaxValue=True, hasMinValue=True, minValue=0.0, maxValue=1.0)
        shd_name = control.split(".")[0] + "clavicle_reverse"
        tools.debug_print("\tMaking shader node: " + shd_name, dbg=debug)
        pm.shadingNode('reverse', asUtility=True, name=shd_name)
        input_x = shd_name + ".inputX"
        tools.debug_print("\tConnecting: " + control + " to: " + input_x, dbg=debug)
        pm.connectAttr(control, input_x)
        output_x = shd_name + ".outputX"
        for o in x[1]:
            orient = pm.ls(o)[0]
            tools.debug_print("\t" + orient, dbg=debug)
            attrs = pm.orientConstraint(orient, query=True, weightAliasList=True)
            tools.debug_print("\tConnecting: " + control + " to: " + attrs[0], dbg=debug)
            pm.connectAttr(control, attrs[0])
            tools.debug_print("\tConnecting: " + output_x + " to: " + attrs[1], dbg=debug)
            pm.connectAttr(output_x, attrs[1])
            tools.debug_print("", dbg=debug)
        tools.debug_print("", dbg=debug)


def setup_clavicle():
    tools.debug_print("setup_clavicle\n", dbg=debug)
    make_orient_joints()
    tools.make_ctrl_hierarchy(clavicleHierarchy)
    tools.parent_objects(parentDict)
    tools.point_constraint_objects(pointDict)
    setup_clavicle_orient()
    for clavicle in clavicleDict:
        make_clavicle_anim(clavicle)
        ani = tools.get_new_name(clavicle, "anim")
        attrs = attributes[ani][u'attributes']
        locks = attributes[ani][u'lock']
        obj = attributes[ani][u'spaceSwitch']
        tools.create_attributes(obj, attrHeader, attrs)
        tools.lock_attributes([clavicle], locks)
    link_clavicle_attrs()
