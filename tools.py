import pymel.core as pm
import os
import maya.cmds as cmds
from rigBot import env
__author__ = 'jhachigian'

src_dir = os.path.dirname(__file__)
system_base_path = os.path.dirname(utils.__file__)
####################################
upScene= cmds.upAxis(q=1, ax=1)
# if upScene == 'y':
    #cmds.warning('**************************** Y-up system ****************************')
pp=env.get_parts_paths()[-1].replace ('partsLibrary', '')
branch=r'BidepAutoRig\encAssets\rig\autoRig\rigfiles\yup'
shapesLib = os.path.join(pp, "yup")
# shapesLib = os.path.join(system_base_path, "BipedAutoRig\encAssets\rig\autoRig\RigFiles\yup")
# shapesLib = env.get_auto_rig_path()
# if upScene == 'z':
#     #cmds.warning('**************************** Z-up system ****************************')
#     shapesLib = os.path.join(src_dir, "rigfiles")

#shapesLib = os.path.join(src_dir, "rigfiles")
#####################################
debug = True

overrideColors = {"Lt": (0.0, 0.5, 0.8999999761581421), "Rt": (0.8999999761581421, 0.5, 0.9900000095367432)}


def debug_print(s, dbg=True):
    if dbg:
        print s


def get_lr(x):
    if x.find("_lt_") != -1:
        return "lt"
    else:
        return "rt"




def zero_rotation(x, axes=None):
    if not axes:
        axes = "rotateX", "rotateY", "rotateZ"
    else:
        axes = ["rotate" + axis.upper() for axis in axes]
    for k in axes:
        pm.setAttr(x + "." + k, 0.0)


def get_new_name(x, suffix):
    return x.rsplit("_", 1)[0] + "_" + suffix


def expand_prefix(x, prefix):
    bits = x.split("_")
    nbts = [(bits[0] + prefix), bits[1], bits[2]]
    return "_".join(nbts)


def set_override_color(x, col):
    pm.setAttr(x + '.overrideColor', col)
    pm.setAttr(x + '.overrideEnabled', True)


def set_color(ani, color):
    """
    :param ani: a PyNode representing a transform.
    :param color: a Tuple representing an RGB color
    :return: None
    """
    shp = ani.getShape()
    shp.setAttr("overrideEnabled", True)
    shp.setAttr("overrideRGBColors", True)
    shp.setAttr("overrideColorRGB", color)


def find_lr_override_color(x):
    key = get_lr(x)
    # col = {"Lt": 6, "Rt": 13}[key]
    col = {"lt": 6, "rt": 13}[key]
    return col


def rotate_shape(s, rot):
    spn = pm.getAttr(s + ".spans")
    pm.select(s + ".cv[0:%d]" % spn)
    pm.xform(rotation=rot, relative=True, objectSpace=True)
    pm.select(clear=True)
    pm.delete(s, constructionHistory=True)


def scale_shape(s, scl):
    spn = pm.getAttr(s + ".spans")
    pm.select(s + ".cv[0:%d]" % spn)
    pm.xform(scale=scl, relative=True, objectSpace=True)
    pm.select(clear=True)
    pm.delete(s, constructionHistory=True)


def apply_circle(x, norm, radius=8.0, degree=3, sections=8, offset=0.0, rotate=0.0, color=None):
    pm.select(clear=True)
    cir = pm.circle(radius=radius, normal=norm, degree=degree, sections=sections)
    n = get_new_name(x, "nurbsCircle")
    cir[0].rename(n)
    c_name = cir[0].name() + "Shape"
    if rotate or offset:
        spans = pm.getAttr(c_name + ".spans")
        pm.select(c_name + ".cv[0:%d]" % spans)
    if rotate:
        rot = (norm[0]*rotate, norm[1]*rotate, norm[2]*rotate)
        pm.xform(rotation=rot, relative=True, objectSpace=True)
    if offset:
        trans = (norm[0]*offset, norm[1]*offset, norm[2]*offset)
        pm.move(trans[0], trans[1], trans[2], relative=True, localSpace=True, worldSpaceDistance=True)
    pm.select(clear=True)
    if color:
        set_override_color(c_name, color)
    pm.parent(c_name, x, shape=True, relative=True)
    pm.delete(cir)
    return c_name


def apply_shape(x, filename=""):
    """
    :param x: the name of the anim object
    :param filename: (optional) the filename containing the shape data to load onto x. This filename should be a
                      Maya binary file containing ONLY a parent object and a shape object.
    :return: the shape PyNode
    """
    debug_print("applyShape: " + x, dbg=debug)
    if filename:
        """ use the shape provided by the user. """
        if filename.endswith(".mb"):
            m_file = filename
        else:
            m_file = filename + ".mb"
        f = os.path.join(shapesLib, m_file)
    else:
        """ look for a filename based on the name of the anim object. """
        f = os.path.join(shapesLib, x + ".mb")
    if os.path.exists(f):
        old_shp = pm.PyNode(x).getShape()
        if old_shp:
            debug_print("\toldShape: " + old_shp, dbg=debug)
            debug_print("\tDeleting: " + old_shp, dbg=debug)
            pm.delete(old_shp)
        debug_print("\tLoading: " + f + " for " + x, dbg=debug)
        li = pm.importFile(f, returnNewNodes=True)
        shp = [o for o in li if o.type() == 'nurbsCurve'][0]
        par = shp.getParent()
        par_name = "pleeeeeaseDeleteMeLetMeGooooo"
        shp_name = get_new_name(x, "CTLShape")
        pm.rename(par, par_name)
        pm.rename(shp, shp_name)
        debug_print("\tParenting: " + shp_name + " to: " + x, dbg=debug)
        pm.parent(shp_name, x, relative=True, shape=True)
        excess = [o for o in li if pm.objExists(o) and o.type() != 'nurbsCurve']
        debug_print("\tDeleting: " + str(excess), dbg=debug)
        pm.delete(excess)
        pm.reorder(shp_name, front=True)
        debug_print("", dbg=debug)
        return shp_name
    else:
        debug_print("\tCould not find file: " + f + "\n", dbg=debug)
        return None


def make_joint(n, zero=False, world=False, clear_selection=True):
    if clear_selection:
        pm.select(clear=True)
    ikj = pm.joint(name=n)
    if zero: 
        d = {'drawStyle': 2, 'radius': 2, 'jointOrientX': 0, 'jointOrientZ': 0}
    else:
        if upScene == 'y':
            d = {'drawStyle': 2, 'radius': 2, 'jointOrientY': 0.0}
            #d = {'drawStyle': 2, 'radius': 2, 'jointOrientY': 90.0}
        if upScene == 'z':
            d = {'drawStyle': 2, 'radius': 2, 'jointOrientX': -90, 'jointOrientZ': 90}
    for k in d:
        ikj.setAttr(k, d[k])
    if world:
        ikj.setParent(world=True)
    return ikj


def insert_joints(d):
    for k in d:
        par = pm.PyNode(k)
        pm.select(par)
        children = par.getChildren()
        jnt = pm.joint(name=d[k], relative=True, position=(0, 0, 0), orientation=(0, 0, 0))
        for c in children:
            c.setParent(jnt, relative=True)


def add_volume_joint(parent):
    par = pm.PyNode(parent)
    vj_name = get_new_name(parent, "VJ_JNT")
    mt_name = get_new_name(parent, "VJ_UTmd")
    rad = par.getAttr("radius")
    """ create volume joint """
    pm.select(parent)
    jnt = pm.joint(name=vj_name)
    jnt.setAttr("radius", rad * 2)
    jnt.setAttr("translateY", 0.002)
    set_override_color(jnt, 17)
    """ create multiply node """
    node = pm.createNode("multiplyDivide", name=mt_name)
    node.setAttr("operation", 1)
    node.setAttr("input2", (-0.5, -0.5, -0.5))
    """ connect nodes """
    pm.connectAttr(par + ".rotate", node + ".input1")
    pm.connectAttr(node + ".output", jnt + ".rotate")


def add_partial_joint(sibling):
    sib = pm.PyNode(sibling)
    par = sib.getParent()
    ref_name = get_new_name(sibling, "partialRef_JNT")
    jnt_name = get_new_name(sibling, "partial_JNT")
    """ make two zeroed-out child joints for the would-be sibling """
    pm.select(sib)
    ref = pm.joint(name=ref_name)
    pm.select(sib)
    jnt = pm.joint(name=jnt_name)
    jnt.setAttr("translateY", 0.002)
    """ reparent both to the sibling's parent """
    ref.setParent(par)
    jnt.setParent(par)
    """ constrain the joint """
    con = pm.orientConstraint(sibling, ref, jnt)
    con.setAttr("interpType", 2)  # "Shortest" interpolation.
    pm.pointConstraint(sibling, jnt, maintainOffset=True)
    """ misc """
    ref.setAttr("visibility", False)
    rad = jnt.getAttr("radius")
    jnt.setAttr("radius", rad * 3.0)
    set_override_color(jnt, 25)
    """ return the joint """
    return jnt


def match_to(child, parent, tab=1):
    debug_print("\t" * tab + "Matching: " + child + " + to: " + parent, dbg=debug)
    pm.cycleCheck(evaluation=False)
    pc = pm.parentConstraint(parent, child)
    #print '((((((((((((((((((((((((((((( ', child, cmds.getAttr(child + '.ry'), ')))))))))))))))))))))))))))))))'
    pm.delete(pc)
    pm.cycleCheck(evaluation=True)


def match_xyz(child, parent, tab=1, report=True):
    if report:
        debug_print("\t" * tab + "Matching XYZ: " + child + "to: " + parent, dbg=debug)
    pm.cycleCheck(evaluation=False)
    pt = pm.pointConstraint(parent, child)
    pm.delete(pt)
    pm.cycleCheck(evaluation=True)


def create_duplicate_chain(x, suffix):
    roots = pm.duplicate(x, renameChildren=True)
    dups = []
    for root in roots:
        dups += [root]
        dups += root.listRelatives(allDescendents=True)
    dups = list(set(dups))  # ...just in case, to eliminate duplicates.
    for dup in dups:
        new_name = get_new_name(dup.name(), suffix)
        dup.rename(new_name)


def aim_constraint_up_vector_vis(vis):
    debug_print("\taimConstraintUpVectorVisibility: " + str(vis), dbg=debug)
    li = pm.ls("*_aimConstraint*")
    for x in li:
        upv = pm.aimConstraint(x, query=True, worldUpObject=True)
        if upv and upv.type() == 'transform':
            pm.setAttr(upv + ".visibility", vis)


def pattern_visibility(pattern, vis, maya_type=""):
    debug_print("\tpatternVisibility: " + pattern + " " + str(vis), dbg=debug)
    if maya_type:
        li = pm.ls(pattern, type=maya_type)
    else:
        li = pm.ls(pattern)
    for x in li:
        if "visibility" in pm.listAttr(x):
            pm.setAttr(x + ".visibility", vis)


def list_visibility(li, vis):
    for x in li:
        if pm.objExists(x) and "visibility" in pm.listAttr(x):
            pm.setAttr(x + ".visibility", vis)


def parent_objects(d):
    debug_print("Reparenting objects...", dbg=debug)
    for key in d:
        debug_print("\tParenting: " + str(d[key]) + "to: " + key, dbg=debug)
        pm.parent(d[key], key)


def parent_constraint_objects(d):
    debug_print("Parent constraint setup...", dbg=debug)
    for par in d:
        if type(d[par][0]) == tuple:
            for tup in d[par]:
                debug_print("\tParent constraining: " + tup[0] + "to: " + par + "maintainOffset: " + str(tup[1]),
                            dbg=debug)
                pm.parentConstraint(par, tup[0], maintainOffset=tup[1])
        else:
            debug_print("\tParent constraining: " + d[par][0] + "to: " + par + "maintainOffset: " + str(d[par][1]),
                        dbg=debug)
            pm.parentConstraint(par, d[par][0], maintainOffset=d[par][1])


def point_constraint_objects(d, separate=True):
    debug_print("Point constraint setup...", dbg=debug)
    for pnt in d:
        if separate:
            for x in d[pnt]:
                debug_print("\tPoint constraining: " + x + "to: " + pnt, dbg=debug)
                pm.pointConstraint(pnt, x)
        else:
            debug_print("\tPoint constraining: " + d[pnt] + "to " + pnt, dbg=debug)
            pm.pointConstraint(pnt, d[x])


def make_ctrl_hierarchy(ctrl_hierarchy, circle_dict=None):
    debug_print("makeCtrlHierarchy", dbg=debug)
    for ctrl in ctrl_hierarchy:
        name = ctrl[0]
        if not pm.objExists(name):
            debug_print("\tMaking: " + name, dbg=debug)
            prnt = ctrl[1]
            typ = ctrl[2]
            mtch = ctrl[3]
            if typ == 'joint':
                node = make_joint(name, world=True)
            elif typ == 'locator':
                node = pm.spaceLocator(name=name)
            else:
                node = pm.group(name=name, empty=True)
            if mtch:
                match_to(node, mtch)
            if not name.endswith(("ref", "armBase_Rt_loc", "armBase_Lt_loc")):
                zero_rotation(node)
            if circle_dict is not None and name.endswith("_CTL") and name in circle_dict:
                info = circle_dict[name]
                if type(info) == dict:
                    radius = info['radius']
                    degree = info['degree']
                    sections = info['sections']
                    rotate = info['rotate']
                    offset = info['offset']
                    color = info['color']
                    apply_circle(name, (0, 1, 0), radius=radius, degree=degree,
                                 sections=sections, rotate=rotate, offset=offset, color=color)
                else:
                    apply_circle(name, (0, 1, 0), radius=info)
            if prnt:
                node.setParent(prnt)
            if pm.objExists(name):
                debug_print("\tSuccessfully made " + name, dbg=debug)
            else:
                debug_print("\tUh-oh.", dbg=debug)
            debug_print("", dbg=debug)
        else:
            debug_print("\t" + name + "already exists.", dbg=debug)


def create_attributes(name, header, attrs):
    node = pm.PyNode(name)
    name = "________"
    while node.hasAttr(name):
        name += "_"
    node.addAttr(name, attributeType='enum', enumName=header, keyable=False)
    node.setAttr(name, channelBox=True)
    for attr in attrs:
        node.addAttr(attr)
        node.setAttr(attr, channelBox=True, type="double")
        node.setAttr(attr, keyable=True)


def lock_attributes(li, attrs):
    for x in li:
        node = pm.PyNode(x)
        for attr in attrs:
            node.setAttr(attr, lock=True, keyable=False, channelBox=False)
