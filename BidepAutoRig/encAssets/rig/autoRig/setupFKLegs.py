import pymel.core as pm
import tools
import setupFingers
import maya.cmds as cmds
reload(tools)
reload(setupFingers)

debug = True
upScene= cmds.upAxis(q=1, ax=1)
__author__ = 'jhachigian'

limbs = ["thigh_Lt_jnt", "thigh_Rt_jnt"]

fkDict = {"Lt": ('shoulder_Lt_jnt', 'elbow_Lt_jnt', 'hand_Lt_jnt',
                 'thigh_Lt_jnt', 'knee_Lt_jnt', 'foot_Lt_bind', 'toe_Lt_bind')}

visDict = {}


def setup_fk(parentConstrain=False):
    # for limb in ["shoulder_Lt_jnt", "shoulder_Rt_jnt"]:
    for limb in limbs:
        tools.create_duplicate_chain(limb, "fk")
    for obj in [ "legEnd", "knee_Lt", "knee_Rt"]:
        obj_name = obj + "_*_fk"
        if pm.objExists(obj_name):
            pm.delete(obj_name)
    for limb in limbs:
        fk_limb = tools.get_new_name(limb, "fk")
        setupFingers.chain_setup(fk_limb, base_h=8, base_w=8)
    """ cleanup on Aisle 4! """
    for x in ["Lt", "Rt"]:
        """ define the names """
        toe_aim = "toeAim_" + x + "_loc"
        foot_anim = "foot_" + x + "_anim"
        toe_anim = "toe_" + x + "_anim"
        toe_end_grp = "toeEnd_" + x + "_a0"
        """ insert gimbal controls and map them to a dictionary """
        pars = {foot_anim: ["toe_%s_a0" % x, "footUpVec_%s_loc" % x, "kneeAim_%s_loc" % x, toe_aim]}
        grps = {}
        for anim in [foot_anim]:
            name = tools.expand_prefix(anim, "Gimbal")
            grp = pm.group(empty=True, name=name)
            grp.setParent(anim, relative=True)
            # tools.apply_circle(grp, (1, 0, 0), degree=1, sections=4)
            shp = tools.apply_shape(grp, "fourPointArrow_anim")
            # tools.set_override_color(shp, 17)
            if grp.startswith("hand"):
                tools.rotate_shape(shp, (0, 0, 90))
            pm.parent(pars[anim], grp)
            grps[anim] = grp
        visDict[x] = {}
        visDict[x]["leg"] = grps[foot_anim]
        """ reparent """
        pm.parent(toe_aim, toe_anim)
        """ delete unwanted leftovers from the chain setup """
        pm.delete(toe_end_grp)
        """ set attributes """
        """ if applicable, set parentConstraints """
        if parentConstrain:
            """ parentObjects constrain jnts to FK counterparts """
            for jnt in fkDict[x]:
                fk = tools.get_new_name(jnt, "fk")
                tools.debug_print("Parent constraining: " + jnt + " to: " + fk, dbg=debug)
                pm.parentConstraint(fk, jnt)
