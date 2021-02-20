import pymel.core as pm


def select_bind():
    li = pm.ls("*bind", type='joint')
    pm.select(li)


def mirror_left_to_right():
    # capture current selection
    selection = pm.ls(selection=True)

    # delete left side
    li = pm.listRelatives("|root_Mid_jnt", allDescendents=True, fullPath=True) + pm.ls("*_plc", type='joint')
    deljnts = [x for x in li if x.find("_Rt_") != -1]
    pm.delete(deljnts)

    # grab roots of branches
    li = pm.listRelatives("|root_Mid_jnt", allDescendents=True, fullPath=True) + pm.ls("*_plc", type='joint')
    jnts = [x for x in li if x.find("_Lt_") != -1 and (x.getParent() is None or x.getParent().find("_Lt_") == -1)]

    # for each root, mirror the branch!
    for jnt in jnts:
        pm.select(jnt)
        pm.mirrorJoint(jnt, mirrorBehavior=True, mirrorYZ=True, searchReplace=("_Lt_", "_Rt_"))

    # restore selection
    pm.select(selection)


def mirror_right_to_left():
    # capture current selection
    selection = pm.ls(selection=True)

    # delete left side
    li = pm.listRelatives("|root_Mid_jnt", allDescendents=True, fullPath=True) + pm.ls("*_plc", type='joint')
    deljnts = [x for x in li if x.find("_Lt_") != -1]
    pm.delete(deljnts)

    # grab roots of branches
    li = pm.listRelatives("|root_Mid_jnt", allDescendents=True, fullPath=True) + pm.ls("*_plc", type='joint')
    jnts = [x for x in li if x.find("_Rt_") != -1 and (x.getParent() is None or x.getParent().find("_Rt_") == -1)]

    # for each root, mirror the branch!
    for jnt in jnts:
        pm.select(jnt)
        pm.mirrorJoint(jnt, mirrorBehavior=True, mirrorYZ=True, searchReplace=("_Rt_", "_Lt_"))

    # restore selection
    pm.select(selection)


""" Fix Joint Orient """


def fix_joint_orient(jnt):
    loc = pm.spaceLocator()
    par = jnt.getParent()
    loc.setParent(jnt, relative=True)
    loc.setParent(par)
    jnt.setParent(loc)
    for attr in ['jointOrient', 'rotate', 'rotateAxis']:
        jnt.setAttr(attr, [0, 0, 0])
    jnt.setParent(par)
    pm.delete(loc)


def needs_fixing(jnt):
    test = False
    for attr in ['rotate', 'rotateAxis']:
        for x in ['X', 'Y', 'Z']:
            if jnt.getAttr(attr + x) != 0.0:
                print jnt, attr + x, jnt.getAttr(attr + x)
                test = True
    return test


def report(li):
    if li:
        msg = "Fixed the following:\r\n\r\n"
        msg += "\r\n".join(li)
    else:
        msg = "No joint problems found."
    print msg
    pm.confirmDialog(message=msg, title="Done.")


def fix_joints_orient():
    li = []
    sel = pm.ls(selection=True, type='joint')
    for jnt in sel:
        if needs_fixing(jnt):
            fix_joint_orient(jnt)
            li.append(jnt.name())
    report(li)
    pm.select(sel)
