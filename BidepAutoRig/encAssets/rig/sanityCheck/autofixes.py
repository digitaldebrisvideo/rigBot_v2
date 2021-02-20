import pymel.core as pm
import functools
import encLib as enc
import encAsset.removeMentalRay as removeMR
reload(removeMR)

__author__ = 'jhachigian'

error_list = []


def catch_errors(func):
    """
    A decorator function that catches errors to the "error_list" list if they occur.

    :param func: the function to be wrapped in the decorator
    :return: the wrapped function
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print "\t\tERROR"
            error_list.append(func.__name__)
    return wrapped


@catch_errors
def lower_display_smoothness():
    """
    Set the display smoothness of the NURBS and meshes in the scene.

    :return: None
    """
    nodes = pm.ls(type='nurbsCurve') + pm.ls(type='mesh')
    pm.displaySmoothness(nodes, divisionsU=0, divisionsV=0, pointsWire=4, pointsShaded=1, polygonObject=1)


@catch_errors
def lock_major_groups():
    """
    Lock the channels of the geometry_grp, setup_grp and controls_grp.

    :return: None
    """
    nodes = [pm.PyNode(x) for x in ["geometry_grp", "setup_grp", "controls_grp"] if pm.objExists(x)]
    nodes += pm.ls("rig_*_grp")
    print "\tLocking translate/rotate/scale on:", nodes
    lock_nodes(nodes)


@catch_errors
def disable_setup_grp_visibility():
    """
    Hide the setup_grp.

    :return: None
    """
    if pm.objExists("setup_grp"):
        grp = pm.PyNode("setup_grp")
        grp.setAttr("visibility", False)


@catch_errors
def set_ik_fk_defaults():
    """
    Set legs to default to IK and everything else (usually arms) to FK.

    :return: None
    """
    anims = [x for x in pm.ls("*_anim") if x.hasAttr("FK_IK")]
    for anim in anims:
        if anim.startswith("leg"):
            anim.setAttr("FK_IK", 1)
        else:
            anim.setAttr("FK_IK", 0)


@catch_errors
def delete_animation():
    """
    Strip the animation curves from every animation control on the rig.

    :return: None
    """
    nodes = pm.ls("*_anim", type='transform')
    enc.delete_anim(nodes)


@catch_errors
def lock_nodes(nodes):
    """
    Lock and hide the translate, rotate and scale channels from the channel box.
    :param nodes: a list of PyMEL nodes.
    :return: None
    """
    for node in nodes:
        for x in ["translate", "rotate", "scale"]:
            for c in ["X", "Y", "Z"]:
                node.setAttr(x + c, lock=True, keyable=False, channelBox=False)


@catch_errors
def lock_parents():
    """
    Lock the channels of the parents of every "*_anim" object (IF that parent is NOT an animation control itself).

    :return: None
    """
    targets = pm.ls("*_anim", type=("transform", "joint"))
    nodes = [x.getParent() for x in targets if x.name() != "world_anim" and
             x.getParent().name().find("_anim") == -1 and
             x.getParent().name().find("_ctl") == -1 and
             x.getParent().name().find("_offset") == -1]
    lock_nodes(nodes)


@catch_errors
def remove_unused_nodes():
    """
    Removes any nodes not being used in the scene. Does not remove mental ray contamination.

    :return: None
    """
    print "\n"
    print "*** ============================== ***"
    print "*** REMOVING unused nodes          ***"
    print "*** ============================== ***"
    print "\n"
    pm.mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes")')
    print "\n"
    print "*** ============================== ***"
    print "*** FINISHED removing unused nodes ***"
    print "*** ============================== ***"
    print "\n"


@catch_errors
def delete_open_windows():
    """
    Close all open floating Maya windows that start with the specific prefixes listed in "targets."
    :return: None
    """
    targets = "hyperShadePanel", "nodeEditorPanel", "hyperGraphPanel", "graphEditor"
    windows = pm.lsUI(windows=True)
    for w in windows:
        if w.name().startswith(targets):
            print "\t\tDeleting window:", w
            pm.deleteUI(w)


@catch_errors
def remove_turtle_nodes():
    """
    Remove any Turtle nodes.
    :return: None
    """
    """ remove all Turtle nodes """
    li = [x for x in pm.ls("*urtle*") if x.type().startswith("ilr")]
    if li:
        try:
            pm.undoInfo(stateWithoutFlush=False)
            pm.lockNode("*urtle*", lock=False)
            pm.delete(li)
        finally:
            pm.undoInfo(stateWithoutFlush=True)


@catch_errors
def remove_turtle_plugin():
    """
    Remove the Turtle plugin.
    :return:
    """
    li = pm.pluginInfo(query=True, listPlugins=True)
    if li is not None and "Turtle" in li:
        pm.unloadPlugin("Turtle")


@catch_errors
def set_display_layer_to_reference():
    """
    Finds all display layers that end in "Geo_Layer" and sets them to Reference mode.
    :return: None
    """
    display_layers = [x for x in pm.ls(type="displayLayer") if x.name().endswith("Geo_Layer")]
    for display_layer in display_layers:
        display_layer.setAttr("displayType", 2)


@catch_errors
def remove_atom_nodes():
    """
    Remove all traces of tmpOfflineForAtomR* nodes.
    :return: None
    """
    li = pm.ls("tmpOfflineForAtomR*")
    if li:
        try:
            pm.undoInfo(stateWithoutFlush=False)
            pm.lockNode("tmpOfflineForAtomR*", lock=False)
            pm.delete(li)
        finally:
            pm.undoInfo(stateWithoutFlush=True)


@catch_errors
def lock_and_hide_anim_visibility():
    """
    Lock and hide the "visibility" attribute of every transform that ends in "*anim"
    :return: None
    """
    li = pm.ls("*_anim", type="transform")

    for obj in li:
        if obj.hasAttr("visibility"):
            obj.setAttr("visibility", channelBox=False, lock=True, keyable=False)


@catch_errors
def remove_mental_ray():
    """
    Delete all mental ray nodes from the scene using Cherie Rye's removeMentalRay function.

    :return: None
    """
    print "\n"
    print "*** ========================= ***"
    print "*** EXECUTING kill_mental_ray ***"
    print "*** ========================= ***"
    print "\n"
    li = removeMR.kill_mental_ray()
    print "\n"
    print "*** ========================= ***"
    print "*** FINISHED  kill_mental_ray ***"
    print "*** ========================= ***"
    print "\n"
    if li:
        print "Deleted the following mental ray nodes:"
    for x in li:
        print "\t", x


@catch_errors
def unload_arnold_plugin():
    """
    Unload Arnold plugin.

    :return: None
    """
    li = pm.pluginInfo(query=True, listPlugins=True)
    if li is not None and "mtoa" in li:
        pm.unloadPlugin("mtoa", force=True)


def auto_fixes():
    """
    Auto fix issues.
    :return: None
    """
    global error_list
    error_list = []
    print "Starting auto-fixes..."

    """ lower displaySmoothness """
    print "\tLowering displaySmoothness for nurbCurves and meshes..."
    lower_display_smoothness()

    """ lock major groups """
    lock_major_groups()

    """ setup_grp visibility """
    print "\tDisabling setup_grp visibility..."
    disable_setup_grp_visibility()

    """ FK_IK default values """
    print "\tSetting all FK_IK slider values to 0."
    set_ik_fk_defaults()

    """ Delete all animation """
    print "\tDeleting all animation from *_anim objects..."
    delete_animation()

    """ lock all nodes above controls """
    print "\tLocking the parents of every *_anim object..."
    lock_parents()

    """ delete all unused nodes """
    print "\tDeleting unused nodes..."
    remove_unused_nodes()

    """ Close unwanted Maya windows """
    print "\tDeleting open windows..."
    delete_open_windows()

    """ Remove all trace of the Turtle plugin """
    print "\tRemoving all traces of Turtle..."
    remove_turtle_nodes()
    remove_turtle_plugin()

    """ Set all display layers that end in "Geo_Layer" to Reference mode """
    print "\tSetting all display layers to Reference..."
    set_display_layer_to_reference()

    """ delete tmpOfflineForAtomR* nodes """
    print "\tRemoving all traces of tmpOfflineForAtomR* nodes..."
    remove_atom_nodes()

    """ Lock and hide Visibility on anim objects """
    print "\tLocking and hiding visibility on all transform objects whose names end in \"_anim\"..."
    lock_and_hide_anim_visibility()

    """ Clean out mental ray """
    print "\tRemoving mental ray nodes (if any)..."
    remove_mental_ray()

    """ lock and hide Arnold attributes """
    print("\tUnloading Arnold plugin (if loaded)...")
    unload_arnold_plugin()

    """ warn the user if anything went wrong! """
    if error_list:
        msg = "Auto-fixes failed on the following routines:\r\n\r\n"
        msg += "\r\n".join(error_list)
        print msg
        pm.confirmDialog(title="ERROR", message=msg)
    print "Done."


def auto_check():
    msg = "Run auto-fixes?\r\n\r\n(Click NO if this is a Counterpunch rig)."
    answer = pm.confirmDialog(title='Confirm', message=msg,
                              button=['Yes', 'No'], defaultButton='Yes',
                              cancelButton='No', dismissString='No')
    if answer == "Yes":
        auto_fixes()
