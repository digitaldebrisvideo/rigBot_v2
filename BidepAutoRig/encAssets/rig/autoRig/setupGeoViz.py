import os
import pymel.core as pm
import tools
import maya.cmds as cmds
reload(tools)

mel_file = os.path.join(os.path.dirname(__file__), "pc_resolutionSwitchesProc.mel").replace("\\", "/")

upScene= cmds.upAxis(q=1, ax=1)
def setup_geo_viz():

    """
    :return: init controls for geometry resolution and visibility
    """

    """ create controls """
    upScene= cmds.upAxis(q=1, ax=1)
    pm.mel.eval("source \"" + mel_file + "\"")

    """ place, constrain and parent visSwitch """
    tools.match_to("visibility_CTL_OFF", "head_Mid_anim")
    if upScene == 'z':
        pm.move("visibility_CTL_OFF", [0, 6.073, 23.982], relative=True)
        pm.rotate("visibility_CTL_OFF", [-90, 90, 0], relative=True)
    if upScene == 'y':
        pm.move("visibility_CTL_OFF", [0, 23.982, 6.073], relative=True)
        pm.rotate("visibility_CTL_OFF", [-90, 0, 0], relative=True)
    
    pm.parentConstraint("head_Mid_anim", "visibility_CTL_OFF", maintainOffset=True)
    pm.parent("visibility_CTL_OFF", "display_grp")

    """ parent skinnedGeo and constrainedGeo groups """
    pm.parent("skinnedGeo_grp", "constrainedGeo_grp", "geometry_grp")
    pm.delete("geoRez_grp")

    # """ init geometry display layer """
    # pm.select("geometry_grp")
    # x = pm.createDisplayLayer(name="XXXGeo_Layer")
    # x.setAttr("displayType", 2)

    """ delete switch_anim """
    if pm.objExists("switch_anim"):
        pm.delete("switch_anim")
