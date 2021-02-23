import pymel.core as pm
import tools
import setupFingers
import maya.cmds as cmds
reload(tools)
reload(setupFingers)

debug = True
upScene= cmds.upAxis(q=1, ax=1)
__author__ = 'jhachigian'

limbs = [ "shoulder_Lt_jnt", "shoulder_Rt_jnt"]


fkDict = {"Lt": ('shoulder_Lt_jnt', 'elbow_Lt_jnt', 'hand_Lt_jnt'),
          "Rt": ('shoulder_Rt_jnt', 'elbow_Rt_jnt', 'hand_Rt_jnt') }

visDict = {}


def setup_fk(parentConstrain=False):
    # for limb in ["shoulder_Lt_jnt", "shoulder_Rt_jnt"]:
    for limb in limbs:
        tools.create_duplicate_chain(limb, "fk")
    for obj in ["indexCarpal", "middleCarpal", "ringCarpal", "thumbCarpal",
                "pinkyCarpal", "armEnd", "legEnd", "knee_Lt", "knee_Rt"]:
        obj_name = obj + "_*_fk"
        if pm.objExists(obj_name):
            pm.delete(obj_name)
    for limb in limbs:
        fk_limb = tools.get_new_name(limb, "fk")
        setupFingers.chain_setup(fk_limb, base_h=8, base_w=8)
    """ cleanup on Aisle 4! """
    for x in ["Lt", "Rt"]:
        """ define the names """
        hand_aim = "handAim_" + x + "_loc"
        hand_anim = "hand_" + x + "_anim"
        hand_end_grp = "handEnd_" + x + "_a0"
        elbow_anim = "elbow_" + x + "_anim"
        """ insert gimbal controls and map them to a dictionary """
        pars = {hand_anim: ["handUpVec_%s_loc" % x, hand_aim]}
        grps = {}

        # name = tools.expand_prefix(anim, "Gimbal")
        name=hand_anim.replace ('hand', 'handGimbal')
        grp = pm.group(empty=True, name=name)
        grp.setParent(hand_anim, relative=True)
        # tools.apply_circle(grp, (1, 0, 0), degree=1, sections=4)
        shp = tools.apply_shape(grp, "fourPointArrow_anim")
        tools.set_override_color(shp, 17)
        if grp.startswith("hand"):
            tools.rotate_shape(shp, (0, 0, 90))
        pm.parent(pars[hand_anim], grp)
        grps[hand_anim] = grp

        visDict[x] = {}
        visDict[x]["arm"] = grps[hand_anim]
        """ reparent """
        """ delete unwanted leftovers from the chain setup """
        pm.delete(hand_end_grp)
        """ set attributes """
        pm.setAttr(elbow_anim + ".rotateOrder", 3)
        """ if applicable, set parentConstraints """
        if parentConstrain:
            """ parentObjects constrain jnts to FK counterparts """
            for jnt in fkDict[x]:
                fk = tools.get_new_name(jnt, "fk")
                tools.debug_print("Parent constraining: " + jnt + " to: " + fk, dbg=debug)
                pm.parentConstraint(fk, jnt)
