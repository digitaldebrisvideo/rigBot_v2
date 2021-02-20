import pymel.core as pm
import makeBox
import tools
reload(makeBox)
reload(tools)

__author__ = 'jhachigian'

debug = True

fingerRootPatterns = ["*Carpal_Lt*", "*Carpal_Rt*"]
chainDict = {}
upVectorTrans = {'Lt': (0, 3, 0), 'Rt': (0, -3, 0)}
upVectorAim = {'Lt': (0, 1, 0), 'Rt': (0, -1, 0)}
aimVector = {'Lt': (1, 0, 0), 'Rt': (-1, 0, 0)}

colorDict = {'Lt': {'index': 15, 'mid': 6, 'ring': 28, 'pinky': 18, 'thumb': 5, 'shoulder_Lt': 6, 'thigh_Lt': 6},
             'Rt': {'index': 4, 'mid': 13, 'ring': 20, 'pinky': 31, 'thumb': 11, 'shoulder_Rt': 13, 'thigh_Rt': 13}}

fingerCtrlParents = {"Lt": ("fingers_Lt_a0", "handEnd_Lt_jnt"), "Rt": ("fingers_Rt_a0", "handEnd_Rt_jnt")}

blacklist = []

hand_sel_list = []

for side_lr in ['Lt', 'Rt']:
    for part in ['index', 'middle', 'ring', 'pinky', 'thumb']:
        name = "{0}End_{1}_anim".format(part, side_lr)
        blacklist.append(name)


def get_chain(jnt, li=[]):
    li.append(jnt)
    for child in pm.listRelatives(jnt, children=True, type="joint"):
        get_chain(child, li)
    return li


def get_color(x):
    side = tools.get_lr(x)
    for k in colorDict[side]:
        if x.startswith(k):
            return colorDict[side][k]
    return 0


def setup_data_structure(carpal):
    chainDict[carpal] = {}
    chainDict[carpal]['jnts'] = get_chain(carpal, li=[])
    chainDict[carpal]['grps'] = []
    chainDict[carpal]['locs'] = []
    chainDict[carpal]['anis'] = []
    chainDict[carpal]['upvs'] = []


def create_group(carpal, i):
    jnt = chainDict[carpal]['jnts'][i]
    grp_name = tools.get_new_name(jnt, "a0")
    grp = pm.group(name=grp_name, empty=True, world=True)
    chainDict[carpal]['grps'].append(grp)
    pm.parent(grp, jnt, relative=True)
    if i == 0:
        pm.parent(grp, world=True)
    else:
        pm.parent(grp, chainDict[carpal]['anis'][i-1])


def create_anim(carpal, i):
    jnt = chainDict[carpal]['jnts'][i]
    ani_name = tools.get_new_name(jnt, "anim")
    ani = tools.make_joint(ani_name, zero=True)
    chainDict[carpal]['anis'].append(ani)
    grp = chainDict[carpal]['grps'][i]
    pm.parent(ani, grp, relative=True)


def create_loc(carpal, i):
    jnt = chainDict[carpal]['jnts'][i]
    loc_name = tools.expand_prefix(jnt, "Aim")
    loc_name = tools.get_new_name(loc_name, "loc")
    loc = pm.spaceLocator(name=loc_name)
    ani = chainDict[carpal]['anis'][i]
    if i > 0:
        pm.parent(chainDict[carpal]['locs'][i-1], ani, relative=True)
    jnts_len = len(chainDict[carpal]['jnts'])
    if i == (jnts_len-1):
        pm.delete(loc)
    else:
        chainDict[carpal]['locs'].append(loc)


def create_up_v(carpal, i):
    jnt = chainDict[carpal]['jnts'][i]
    upv_name = tools.expand_prefix(jnt, "UpVec")
    upv_name = tools.get_new_name(upv_name, "loc")
    jnts_len = len(chainDict[carpal]['jnts'])
    ani = chainDict[carpal]['anis'][i]
    if i < (jnts_len-1):
        upv = pm.spaceLocator(name=upv_name)
        chainDict[carpal]['upvs'].append(upv)
        pm.parent(upv, ani, relative=True)
        pm.setAttr(upv_name + "Shape.localScale", (0.1, 0.1, 0.1))
        upv.setAttr("translate", upVectorTrans[tools.get_lr(upv)])


def create_test_circles(carpal, i):
    """
    :param carpal: the key to the fingerDict representing the root of the finger
    :param i: the index representing the joint in the 'jnts' list (ex: i=0 would be the root joint)
    :return: a circle shape parented to the given joint, placed between the joint and its child
    """
    jnt = chainDict[carpal]['jnts'][i]
    jnt_len = len(chainDict[carpal]['jnts'])
    if i < (jnt_len-1):
        """ do not create a circle for the last joint in the chain. """
        chi = chainDict[carpal]['jnts'][i+1]
        cir_name = tools.get_new_name(jnt, "circle")
        cir = pm.circle(name=cir_name, radius=2, normal=(1, 0, 0))
        pm.parent(cir, jnt, relative=True)
        x_cn = pm.getAttr(chi + ".translateX")/2
        cir[0].setAttr("translateX", x_cn)


def create_aim(carpal, i):
    jnts_len = len(chainDict[carpal]['jnts'])
    if i < (jnts_len-1):
        """ do not create an aim constraint for the last joint in the chain. """
        jnt = chainDict[carpal]['jnts'][i]
        upv = chainDict[carpal]['upvs'][i]
        tgt = chainDict[carpal]['locs'][i]
        up_vc = upVectorAim[tools.get_lr(jnt)]
        aim_v = aimVector[tools.get_lr(jnt)]
        tools.debug_print("\t\tTargeting: " + jnt + " at: " + tgt + " with an upVector target of: " + str(upv) +
                          " and an aimVector of: " + str(aim_v), dbg=debug)
        pm.aimConstraint(tgt, jnt, worldUpObject=upv, upVector=up_vc, worldUpType="object", aimVector=aim_v)


def create_constraints(carpal, i):
    jnt = chainDict[carpal]['jnts'][i]
    ani = chainDict[carpal]['anis'][i]
    tools.debug_print("\t\tConstraining: " + jnt + " to: " + ani, dbg=debug)
    pm.pointConstraint(ani, jnt)
    pm.connectAttr(ani + ".scale", jnt + ".scale")


def create_joint_shape(carpal, i, base_h=1, base_w=2):
    taper = 0.4
    jnts_len = len(chainDict[carpal]['jnts'])
    tpr = taper**(1.0/jnts_len)
    adj = tpr**i
    """ do not create a distance-based shape for the last joint in the chain. """
    jnt = chainDict[carpal]['jnts'][i]
    ani = chainDict[carpal]['anis'][i]
    if i < (jnts_len-1):
        chi = chainDict[carpal]['jnts'][i+1]
        x_ln = pm.getAttr(chi + ".translateX")
        x_cn = x_ln/2.0
    else:
        x_ln = 1.0
        if tools.get_lr(jnt) == "Rt":
            x_ln = -x_ln
        x_cn = 0.0
    h = base_h * adj
    w = base_w * adj
    # print "i:", i, "H:", H, "W:", W, "tpr:", tpr, "adj:", adj
    crv = makeBox.make_box(h, w, x_ln, taper=tpr, rotation=(0, 90, 0), offset=x_cn)
    col = get_color(carpal)
    crv_name = tools.get_new_name(jnt, "box")
    crv_shp = crv_name + "Shape"
    pm.rename(crv, crv_name)
    pm.parent(crv_shp, ani, relative=True, shape=True)
    tools.set_override_color(crv_shp, col)
    pm.delete(crv_name)


def chain_setup(carpal, base_h=1, base_w=2):
    tools.debug_print("chainSetup: " + carpal + " with dimensions of:  " + str(base_h) + " " + str(base_w), dbg=debug)
    setup_data_structure(carpal)
    jnts_len = len(chainDict[carpal]['jnts'])
    """ setup control hierarchy """
    tools.debug_print("\tSetting up hierarchy for: " + carpal, dbg=debug)
    for i in xrange(0, jnts_len):
        create_group(carpal, i)
        create_anim(carpal, i)
        create_loc(carpal, i)
        create_up_v(carpal, i)
        # createTestCircles(carpal, i)
    """ after the control hierarchy is defined, setup constraints on that hierarchy """
    for i in xrange(0, jnts_len):
        tools.debug_print("\tSetting up constraints for: " + carpal, dbg=debug)
        create_joint_shape(carpal, i, base_h=base_h, base_w=base_w)
        create_aim(carpal, i)
        create_constraints(carpal, i)
    # from pprint import pprint
    # pprint(fingerDict[carpal])
    tools.debug_print("", dbg=debug)


def setup_hand():
    # chainSetup("indexCarpal_Lt_bind")
    global hand_sel_list
    for side in fingerCtrlParents:
        pair = fingerCtrlParents[side]
        tools.debug_print("Making: " + pair[0], dbg=debug)
        grp = pm.group(name=pair[0], empty=True, world=True)
        jnt = pair[1]
        pm.parent(grp, jnt, relative=True)
        pm.parent(grp, world=True)
        pm.parentConstraint(jnt, grp)
    for pattern in fingerRootPatterns:
        carpals = pm.ls(pattern, type="joint")
        carpals.sort()
        for carpal in carpals:
            chain_setup(carpal)
            lr = tools.get_lr(carpal)
            parent_grp = fingerCtrlParents[lr][0]
            root_group = chainDict[carpal]['grps'][0]
            pm.parent(root_group, parent_grp)
            """ for later use in selection set creation """
            hand_sel_list += chainDict[carpal]['anis']


if __name__ == "__main__":
    setup_hand()
