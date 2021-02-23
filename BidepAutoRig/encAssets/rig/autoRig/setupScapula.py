import pymel.core as pm
import maya.cmds as cmds
import tools
reload(tools)

__author__ = 'jhachigian'

scapula_insert_joints = {"scapulaAim_Lt_jnt": "scapulaCtrl_Lt_bind",
                         "scapulaAim_Rt_jnt": "scapulaCtrl_Rt_bind"}

scapula_dict = {"Lt": {"bind": "scapulaCtrl_Lt_bind"}, "Rt": {"bind": "scapulaCtrl_Rt_bind"}}

upScene= cmds.upAxis(q=1, ax=1)

def make_up_objects():
    for side in ["Lt", "Rt"]:
        loc_name = "scapulaUpObj_%s_loc" % side
        aim_name = "scapulaAim_%s_jnt" % side
        bnd_name = "clavicle_%s_bind" % side
        aim = pm.PyNode(aim_name)
        loc = pm.spaceLocator(name=loc_name)
        tools.match_xyz(loc, aim)
        if upScene == 'z':
            pm.move(0, 0, 20, loc, relative=True, worldSpace=True)
        if upScene == 'y':
            pm.move(0, 20, 0, loc, relative=True, worldSpace=True)
        pm.parent(loc, bnd_name)
        scapula_dict[side]["aimJnt"] = aim
        scapula_dict[side]["upObj"] = loc


def make_aim_targets():
    for side in ["Lt", "Rt"]:
        loc_name = "scapulaTarget_%s_loc" % side
        grp_name = "scapulaTarget_%s_grp" % side
        loc = pm.spaceLocator(name=loc_name)
        grp = pm.group(name=grp_name)
        tools.match_xyz(grp, "scapulaTarget_jnt")
        pm.parent(grp, "chest_armDriven_bind")
        scapula_dict[side]["targetLoc"] = loc
        scapula_dict[side]["targetGrp"] = grp


def constrain_targets():
    for side in ["Lt", "Rt"]:
        tgt1 = "clavicleEnd_%s_jnt" % side
        tgt2 = "chest_armDriven_bind"
        grp = scapula_dict[side]["targetGrp"]
        pm.pointConstraint(tgt1, grp, maintainOffset=True, skip=("x", "z"), weight=1.0)
        pm.pointConstraint(tgt2, grp, maintainOffset=True, skip=("x", "z"), weight=0.5)


def setup_aim_constraints():
    upv_dict = {"Lt": (0, 1, 0), "Rt": (0, 1, 0)}
    aim_dict  = {"Lt": (1, 0, 0), "Rt": (1, 0, 0)}
    for side in ["Lt", "Rt"]:
        tgt = scapula_dict[side]["targetLoc"]
        jnt = scapula_dict[side]["aimJnt"]
        upv = upv_dict[side]
        amv = aim_dict[side]
        upo = scapula_dict[side]["upObj"]
        aim = pm.aimConstraint(tgt, jnt, aimVector=amv, upVector=upv, worldUpType="object", worldUpObject=upo)
        pm.delete(aim)
        pm.makeIdentity(jnt, apply=True, translate=True, rotate=True, scale=True, normal=0, preserveNormals=True)
        pm.aimConstraint(tgt, jnt, aimVector=amv, upVector=upv, worldUpType="object", worldUpObject=upo)


def setup_controls():
    color_dict = {"Lt": 18, "Rt": 20}
    for side in ["Lt", "Rt"]:
        cir_name = "scapula_%s_anim" % side
        grp_name = "scapulaCtrl_%s_grp" % side
        jnt = scapula_dict[side]["aimJnt"]
        bnd = scapula_dict[side]["bind"]
        cir = pm.circle(name=cir_name, radius=4, normal=(0, 0, 1), degree=1, sections=4)
        grp = pm.group(name=grp_name)
        pm.parentConstraint(jnt, grp)
        pm.parentConstraint(cir, bnd)
        pm.transformLimits(jnt, rotationY=(-360, 0), enableRotationY=(False, True))
        # tools.lock_attributes([cir[0]], ["translateX", "translateY", "translateZ"])
        if upScene == 'z':
            pm.move(0, 10, 0, cir[0] + ".cv[0:7]", relative=True, worldSpace=True)
        if upScene == 'y':
            pm.move(0, 0, -10, cir[0] + ".cv[0:7]", relative=True, worldSpace=True)

        tools.set_override_color(cir[0], color_dict[side])


def setup_scapula():
    """
    Scapula rig.
    :return: None
    """
    """ make the scapula ctrl jnts and add to hierarchy """
    tools.insert_joints(scapula_insert_joints)
    """ make the scapula up objects and add to hierarchy"""
    make_up_objects()
    """ make aim target locators and position them """
    make_aim_targets()
    """ constrain scapula target locators """
    constrain_targets()
    """ aim it at the scapulaTarget_jnt, freeze it, and aim it again. """
    setup_aim_constraints()
    """ build control for scapulaCtrl_bind """
    setup_controls()
    """ clear selection """
    pm.select(clear=True)
