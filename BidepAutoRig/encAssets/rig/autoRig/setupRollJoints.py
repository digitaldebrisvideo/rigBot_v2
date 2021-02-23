import maya.cmds as cmds
import pymel.core as pm
import tools
reload(tools)

__author__ = 'jhachigian'
upScene= cmds.upAxis(q=1, ax=1)
if upScene == 'z':
    limbsRollDict = {'shoulder_Lt_jnt': {
                                        'matchPoints': ('shoulder_Lt_jnt', 'elbow_Lt_jnt', 'hand_Lt_jnt'),
                                        # 'matchPoints': ('shoulder_Lt_jnt', 'elbow_Lt_jnt', 'wrist_Lt_bind'),
                                        'skinPoints': ('clavicle_Lt_bind', 'elbow_Lt_jnt', 'hand_Lt_jnt'),
                                        # 'skinPoints': ('clavicle_Lt_bind', 'elbow_Lt_jnt', 'wrist_Lt_bind'),
                                        'rollJoints': [], 'rollTargets': [], 'aimVector': (1, 0, 0), 'upVector': (0, 1, 0),
                                        'curveName': 'armRoll_Lt_crv', 'groupName': 'armRoll_Lt_a0',
                                        'offset': (0, 10, 0)},
                    'shoulder_Rt_jnt': {
                                        'matchPoints': ('shoulder_Rt_jnt', 'elbow_Rt_jnt', 'hand_Rt_jnt'),
                                        # 'matchPoints': ('shoulder_Rt_jnt', 'elbow_Rt_jnt', 'wrist_Rt_bind'),
                                        'skinPoints': ('clavicle_Rt_bind', 'elbow_Rt_jnt', 'hand_Rt_jnt'),
                                        # 'skinPoints': ('clavicle_Rt_bind', 'elbow_Rt_jnt', 'wrist_Rt_bind'),
                                        'rollJoints': [], 'rollTargets': [],
                                        'aimVector': (1, 0, 0), 'upVector': (0, 1, 0),
                                        'curveName': 'armRoll_Rt_crv', 'groupName': 'armRoll_Rt_a0',
                                        'offset': (0, -10, 0)},
                    'thigh_Lt_jnt': {'matchPoints': ('thigh_Lt_jnt', 'knee_Lt_jnt', 'legEnd_Lt_jnt'),
                                    'skinPoints': ('hips_Mid_bind', 'knee_Lt_jnt', 'foot_Lt_bind'),
                                    'rollJoints': [], 'rollTargets': [], 'aimVector': (1, 0, 0), 'upVector': (0, 0, -1),
                                    'curveName': 'legRoll_Lt_crv', 'groupName': 'legRoll_Lt_a0',
                                    'offset': (0, 0, -10)},
                    'thigh_Rt_jnt': {'matchPoints': ('thigh_Rt_jnt', 'knee_Rt_jnt', 'legEnd_Rt_jnt'),
                                    'skinPoints': ('hips_Mid_bind', 'knee_Rt_jnt', 'foot_Rt_bind'),
                                    'rollJoints': [], 'rollTargets': [], 'aimVector': (-1, 0, 0), 'upVector': (0, 0, 1),
                                    'curveName': 'legRoll_Rt_crv', 'groupName': 'legRoll_Rt_a0',
                                    'offset': (0, 0, 10)}}
if upScene == 'y':
 limbsRollDict = {'shoulder_Lt_jnt': {
                                        'matchPoints': ('shoulder_Lt_jnt', 'elbow_Lt_jnt', 'hand_Lt_jnt'),
                                        # 'matchPoints': ('shoulder_Lt_jnt', 'elbow_Lt_jnt', 'wrist_Lt_bind'),
                                        'skinPoints': ('clavicle_Lt_bind', 'elbow_Lt_jnt', 'hand_Lt_jnt'),
                                        # 'skinPoints': ('clavicle_Lt_bind', 'elbow_Lt_jnt', 'wrist_Lt_bind'),
                                        'rollJoints': [], 'rollTargets': [], 'aimVector': (1, 0, 0), 'upVector': (0, 0, 1),
                                        'curveName': 'armRoll_Lt_crv', 'groupName': 'armRoll_Lt_a0',
                                        'offset': (0, 10, 0)},
                    'shoulder_Rt_jnt': {
                                        'matchPoints': ('shoulder_Rt_jnt', 'elbow_Rt_jnt', 'hand_Rt_jnt'),
                                        # 'matchPoints': ('shoulder_Rt_jnt', 'elbow_Rt_jnt', 'wrist_Rt_bind'),
                                        'skinPoints': ('clavicle_Rt_bind', 'elbow_Rt_jnt', 'hand_Rt_jnt'),
                                        # 'skinPoints': ('clavicle_Rt_bind', 'elbow_Rt_jnt', 'wrist_Rt_bind'),
                                        'rollJoints': [], 'rollTargets': [], 'aimVector': (1, 0, 0), 'upVector': (0, 0, 1),
                                        'curveName': 'armRoll_Rt_crv', 'groupName': 'armRoll_Rt_a0',
                                        'offset': (0, -10, 0)},
                    'thigh_Lt_jnt': {'matchPoints': ('thigh_Lt_jnt', 'knee_Lt_jnt', 'legEnd_Lt_jnt'),
                                    'skinPoints': ('hips_Mid_bind', 'knee_Lt_jnt', 'foot_Lt_bind'),
                                    'rollJoints': [], 'rollTargets': [], 'aimVector': (-1, 0, 0), 'upVector': (0, 0, -1),
                                    'curveName': 'legRoll_Lt_crv', 'groupName': 'legRoll_Lt_a0',
                                    'offset': (0, 0, -10)},
                    'thigh_Rt_jnt': {'matchPoints': ('thigh_Rt_jnt', 'knee_Rt_jnt', 'legEnd_Rt_jnt'),
                                    'skinPoints': ('hips_Mid_bind', 'knee_Rt_jnt', 'foot_Rt_bind'),
                                    'rollJoints': [], 'rollTargets': [], 'aimVector': (-1, 0, 0), 'upVector': (0, 0, 1),
                                    'curveName': 'legRoll_Rt_crv', 'groupName': 'legRoll_Rt_a0',
                                    'offset': (0, 0, 10)}}

limbsMMDict = {}

colorDict = {"Lt": 18, "Rt": 20}

showRollJointHandles = False


def make_roll_groups(limb):
    grp1 = limbsRollDict[limb]['groupName']
    pm.group(name=grp1, empty=True, world=True)
    """ create matchmove counterpart """
    grp2 = tools.expand_prefix(grp1, "MM")
    limbsMMDict[limb] = {}
    limbsMMDict[limb]['groupName'] = grp2
    pm.group(name=grp2, empty=True, world=True)
    limbsMMDict[limb]['matchGroups'] = []
    for x in [0, 1]:
        par = limbsRollDict[limb]['matchPoints'][x]
        grp_name = tools.expand_prefix(par, "MM")
        grp_name = tools.get_new_name(grp_name, "a0")
        grp = pm.group(name=grp_name, empty=True, parent=grp2)
        pm.parentConstraint(par, grp)
        limbsMMDict[limb]['matchGroups'].append(grp_name)


def make_roll_joint(start, spacing, offset, n):
    print "\t\tmakeRollJoint:", start, n
    pm.select(start)
    name = tools.expand_prefix(start, 'Roll' + "%02d" % n)
    name = tools.get_new_name(name, "bind")
    ikj = pm.joint(name=name)
    ikj.setAttr('translateX', (n-offset)*spacing)
    return ikj


def make_roll_group(jnt, par):
    grp_name = tools.get_new_name(jnt, "a0")
    grp_name = tools.expand_prefix(grp_name, "MM")
    grp = pm.group(name=grp_name, parent=par, empty=True)
    tools.match_to(grp, jnt)
    return grp


def make_roll_anim(par):
    grp_name = tools.get_new_name(par, "anim")
    grp = pm.group(name=grp_name, parent=par, empty=True)
    key = tools.get_lr(grp_name)
    col = colorDict[key]
    tools.apply_circle(grp, (1, 0, 0), radius=7.0, degree=1, sections=6, color=col)
    return grp


def make_roll_joints(limb):
    print "\tmakeRollJoints:", limb
    li = limbsRollDict[limb]['matchPoints']
    limbsMMDict[limb]['rollGroups'] = []
    limbsMMDict[limb]['rollAnims'] = []
    for x in [0, 1]:
        start = pm.PyNode(li[x])
        end = pm.PyNode(li[x+1])
        mm_par = limbsMMDict[limb]['matchGroups'][x]
        spacing = end.getAttr('translateX')/4
        for y in xrange(1, 5-x):
            ikj = make_roll_joint(start, spacing, 1-x, y)
            if x == 0 and y == 1:
                ikg = None
                ika = None
            else:
                ikg = make_roll_group(ikj, mm_par)
                ika = make_roll_anim(ikg)
            if showRollJointHandles:
                pm.toggle(ikj, localAxis=True)  # turn this on to test orientation of roll joints!
            limbsRollDict[limb]['rollJoints'].append(ikj)
            limbsMMDict[limb]['rollGroups'].append(ikg)
            limbsMMDict[limb]['rollAnims'].append(ika)


def get_offset_xyz(n, offset):
    loc = pm.spaceLocator(name="tempLocatorForMeasurements", p=(0, 0, 0))
    pm.parent(loc, n, relative=True)
    loc.setAttr('translate', offset)
    pos = pm.xform(loc, query=True, translation=True, worldSpace=True)
    pm.delete(loc)
    return pos


def make_roll_curve(limb):
    print "\tmakeRollCurve:", limb
    jnts = limbsRollDict[limb]['skinPoints']
    li = []
    for p in limbsRollDict[limb]['matchPoints']:
        pos = get_offset_xyz(p, limbsRollDict[limb]['offset'])
        li.append(pos)
    curve_name = limbsRollDict[limb]['curveName']
    group_name = limbsRollDict[limb]['groupName']
    curve = pm.curve(point=li, degree=1)
    curve.rename(curve_name)
    print "\t\tParenting:", curve_name, "to:", group_name
    pm.parent(curve_name, group_name)
    print "\t\tSkinning:", curve_name, "to:", jnts
    pm.select(clear=True)
    pm.select(jnts)
    skin = pm.skinCluster(jnts[0], jnts[1], jnts[2], curve_name, toSelectedBones=True)
    skin_name = tools.get_new_name(curve_name, "skin")
    pm.rename(skin, skin_name)
    for x in [0, 1, 2]:
        pm.skinPercent(skin, curve_name + ".cv[%d]" % x, transformValue=[jnts[x], 1.0], zeroRemainingInfluences=True)
    pm.select(clear=True)


def get_u_value(arclen, limb, jnt):
    start, mid, end = limbsRollDict[limb]['matchPoints']
    mid_len = pm.getAttr(mid + ".translateX")
    upper_portion = mid_len/arclen
    x_value = jnt.getAttr("translateX")
    upper_prefix = start.split("_")[0]
    is_upper = jnt.startswith(upper_prefix)
    if is_upper:
        return abs(x_value/upper_portion/arclen)
    else:
        return abs((mid_len + x_value)/upper_portion/arclen)


def make_roll_targets(limb):
    print "\tmakeRollTargets:", limb
    curve_name = limbsRollDict[limb]['curveName']
    group_name = limbsRollDict[limb]['groupName']
    arc_len = pm.arclen(curve_name)
    jnts = limbsRollDict[limb]['rollJoints']
    for jnt in jnts:
        u_value = get_u_value(arc_len, limb, jnt)
        loc_name = tools.get_new_name(jnt, "loc")
        pth_name = tools.get_new_name(jnt, "path")
        print "\t\tPositioning:", loc_name, "along:", pth_name, "with a uValue of:", u_value
        loc = pm.spaceLocator(name=loc_name, position=(0, 0, 0))
        pm.pathAnimation(loc, curve=curve_name, startU=u_value, follow=True, name=pth_name)
        pm.disconnectAttr(pth_name + "_uValue.output", pth_name + ".uValue")
        pm.parent(loc, group_name)
        limbsRollDict[limb]['rollTargets'].append(loc)


def make_aim_constraints(limb):
    print "\tmakeAimConstraints:", limb
    jnts = limbsRollDict[limb]['rollJoints']
    upvs = limbsRollDict[limb]['rollTargets']
    mid_p = limbsRollDict[limb]['matchPoints'][-2]
    end_p = limbsRollDict[limb]['matchPoints'][-1]
    aim_v = limbsRollDict[limb]['aimVector']
    up_v = limbsRollDict[limb]['upVector']
    test = len(jnts)
    for x in xrange(0, test):
        jnt = jnts[x]
        upv = upvs[x]
        if x == 3:
            tgt = mid_p
        elif x + 1 != test:
            tgt = jnts[x + 1]
        else:
            tgt = end_p
        print "\t\tTargeting: ", jnt, "at:", tgt, "with an upVector target of:", upv, "and an aimVector of:", aim_v
        pm.aimConstraint(tgt, jnt, worldUpObject=upv, upVector=up_v, worldUpType="object", aimVector=aim_v)


def make_anim_constraints(limb):
    print "\tmakePointConstraints:", limb
    pars = limbsMMDict[limb]['rollAnims']
    jnts = limbsRollDict[limb]['rollJoints']
    print "pars:", pars
    print "jnts:", jnts
    for x in xrange(0, len(jnts)):
        par = pars[x]
        jnt = jnts[x]
        if par:
            print "\t\tPoint constraining:", jnt, "to:", par
            pm.pointConstraint(par, jnt)
            print "\t\tScale constraining:", jnt, "to:", par
            pm.scaleConstraint(par, jnt)


def roll_joints():
    print "Don't bogart that joint, my friend...pass it over to meeee...."
    # for limb in ['shoulder_Lt_jnt']:
    for limb in limbsRollDict:
        print "Processing:", limb
        make_roll_groups(limb)
        make_roll_joints(limb)
        make_roll_curve(limb)
        make_roll_targets(limb)
        make_aim_constraints(limb)
        make_anim_constraints(limb)
    # from pprint import pprint
    # pprint(limbsMMDict)


if __name__ == "__main__":
    roll_joints()
