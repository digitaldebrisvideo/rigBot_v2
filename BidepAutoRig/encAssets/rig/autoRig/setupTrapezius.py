"""
    setupTrapezius

    original MEL by Vincent DeLay
    Python adaptation by Jennifer Hachigian

    This script must run after setup_geo_viz. It should also run before the selections sets get created.
"""
import maya.cmds as cmds
import pymel.core as pm
import tools
reload(tools)

__author__ = 'jhachigian'

debug = True

info = {}
upScene= cmds.upAxis(q=1, ax=1)

def make_attr():
    tools.debug_print("\tMaking attr...", dbg=debug)
    attr = 'traps_scaps_pecs_anim_vis'
    vis = pm.PyNode("visibility_anim")
    vis.addAttr(attr, attributeType='bool')
    vis.setAttr(attr, True)
    vis.setAttr(attr, channelBox=True)
    vis.setAttr(attr, keyable=True)
    info["visAttr"] = vis + "." + attr


def make_mid_loc():
    pnt1_name = "trapezius_Mid_loc"
    pnt1 = pm.spaceLocator(name=pnt1_name)
    tools.match_xyz(pnt1, "neck03_Mid_bind")
    pm.parent(pnt1, "chest_Mid_bind")


def make_trapezius_controls(side):
    tools.debug_print("make_trapezius_controls")
    pm.select(clear=True)
    ani_name = "trapezius_%s_anim" % side
    ani = pm.circle(name=ani_name, radius=4, normal=(1, 0, 0), degree=1, sections=4)  # returns [transform, nurbsCircle]
    tools.set_color(ani[0], tools.overrideColors[side])
    """ make the parent """
    grp_name = "trapezius_%s_offsetGrp" % side
    grp = pm.group(name=grp_name, empty=True, parent="world_anim")
    """ get pnt1 """
    pnt1 = pm.PyNode("trapezius_Mid_loc")
    """ place the child and parent, and make the point constraint """
    # pnt1 = "neck03_Mid_bind"
    pnt2 = "clavicleEnd_%s_jnt" % side
    pnt = pm.pointConstraint(pnt1, pnt2, ani[0])
    tools.debug_print("deleting: %s" % pnt)
    pm.delete(pnt)
    tools.match_to(grp, ani[0])
    pm.parent(ani[0], grp)
    pnt = pm.pointConstraint(pnt1, pnt2, grp)
    # """ make the aim constraint """
    # aim = pm.aimConstraint(pnt1, grp, aimVector=(1.0, 0.0, 0.0), maintainOffset=True, upVector=(0.0, 0.0, -1.0),
    #                        worldUpObject="chest_Mid_bind", worldUpType="object")
    """ make the bind joint """
    bnd_name = tools.get_new_name(ani_name, "bind")
    bnd_parent_name = "clavicle_%s_bind" % side
    pm.select(ani)
    bnd = pm.joint(name=bnd_name, radius=5.0)
    pm.parent(bnd, bnd_parent_name)
    """ constrain the offsetGrp to the clavicle """
    pm.orientConstraint(bnd_parent_name, grp, maintainOffset=True)
    """ make the bind joint constraints """
    pm.pointConstraint(ani[0], bnd)
    pm.orientConstraint(ani[0], bnd)
    # pm.scaleConstraint(ani, bnd)
    for x in [".scaleX", ".scaleY", ".scaleZ"]:
        pm.connectAttr(ani[0] + x, bnd + x)


def setup_trapezius():
    """
    The "setup_trapezius" routine was retired with v035, but the character riggers needed only two pieces from that
    older setup to make a comeback: the deformers_grp and the visibility_anim.traps_scaps_pecs_anim_vis attribute.

    This replacement routine restored those two pieces in v036.

    v038 update -- now adds additional controls

    :return: None
    """
    pm.group(name="deformers_grp", empty=True, parent="setup_grp")
    """ make trapezius controls """
    make_mid_loc()
    for side in ("Lt", "Rt"):
        make_trapezius_controls(side)
    make_attr()
