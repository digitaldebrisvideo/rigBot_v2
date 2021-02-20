import functools
import time
import datetime
try:
    import pymel.core as pm
    import maya.OpenMaya as om
    import maya.utils
except ImportError:
    pass

__author__ = 'jhachigian'


def in_root_namespace(func):
    """
    A decorator function that switches to the root namespace in Maya, executes the function, then
    restores the namespace. Used for all EncoreTools that have import functions.

    :param func: the function to be wrapped in the decorator
    :return: the wrapped function
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        nms = pm.Namespace.getCurrent()
        pm.namespace(set=":")
        result = func(*args, **kwargs)
        nms.setCurrent()
        return result
    return wrapped


def restore_selections(func):
    """
    A decorator function that captures the selection in Maya, executes the function, then
    restores the selection. Used for newer EncoreTools that change the selection during their work.

    :param func: the function to be wrapped in the decorator
    :return: the wrapped function
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        selected = [x for x in pm.ls(selection=True)]
        result = func(*args, **kwargs)
        """ restore the original selection """
        leftovers = [x for x in selected if pm.objExists(x)]
        pm.select(leftovers)
        return result
    return wrapped


def restore_frame_range(func):
    """
    A decorator function that records the "before" frame range and restores it after

    :param func: the function to be wrapped in the decorator
    :return: the wrapped function
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        current_time = pm.currentTime(query=True)
        original_start = pm.playbackOptions(q=True, minTime=True)
        original_end = pm.playbackOptions(q=True, maxTime=True)
        original_animation_start = pm.playbackOptions(q=True, animationStartTime=True)
        original_animation_end = pm.playbackOptions(q=True, animationEndTime=True)
        """ execute function """
        result = func(*args, **kwargs)
        """ restore the original frame range """
        pm.playbackOptions(animationStartTime=original_animation_start)
        pm.playbackOptions(minTime=original_start)
        pm.playbackOptions(maxTime=original_end)
        pm.playbackOptions(animationEndTime=original_animation_end)
        pm.currentTime(current_time, edit=True)
        return result
    return wrapped


def viewport_off(func):
    """
    A decorator function that disables the Maya display while function is running. Raises an Exception if
    the function fails.

    Modified copy of original at: http://blog.asimation.com/disable-maya-viewport-while-running-code/

    :param func: the function to be wrapped in the decorator
    :return: the wrapped function
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):

        # Turn $gMainPane Off:
        pm.mel.eval("paneLayout -e -manage false $gMainPane")

        # Decorator will try/except running the function.
        # But it will always turn on the viewport at the end.
        # In case the function failed, it will prevent leaving maya viewport off.
        try:
            return func(*args, **kwargs)
        except Exception:
            raise  # will raise original error
        finally:
            pm.mel.eval("paneLayout -e -manage true $gMainPane")

    return wrapped


def hide_all(func):
    """
    The equivalent of "Hide All" in the viewport; restores everything when done.

    :param func: the function to be wrapped in the decorator
    :return: the wrapped function
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        # capture viewport switches to a dictionary.
        categories = ["nurbsCurves", "nurbsSurfaces", "polymeshes", "subdivSurfaces",
                     "planes", "lights", "cameras", "controlVertices", "hulls", "grid", "imagePlane",
                     "joints", "ikHandles", "deformers", "dynamics", "particleInstancers", "fluids",
                     "hairSystems", "follicles", "nCloths", "nParticles", "nRigids", "dynamicConstraints",
                     "locators", "manipulators", "pluginShapes", "dimensions", "handles", "pivots",
                     "textures", "strokes", "motionTrails", "clipGhosts", "greasePencils"]
        if pm.about(version=True) > u'2017':
            categories += ["controllers"]
        d = {}
        for mp in ["modelPanel1", "modelPanel2", "modelPanel3", "modelPanel4"]:
            d[mp] = {}
            for category in categories:
                d[mp][category] = pm.mel.eval("modelEditor -q -{0} {1}".format(category, mp))
        for mp in ["modelPanel1", "modelPanel2", "modelPanel3", "modelPanel4"]:
            pm.mel.eval("modelEditor -e -allObjects 0 {0}".format(mp))
        try:
            return func(*args, **kwargs)
        except Exception:
            raise  # will raise original error
        finally:
            for mp in ["modelPanel1", "modelPanel2", "modelPanel3", "modelPanel4"]:
                for category in categories:
                    pm.mel.eval("modelEditor -e -{0} {1} {2}".format(category, d[mp][category], mp))

    return wrapped


def switch_to_dg(func):
    """
    A decorator function that switches evaluation to DG, then restores the original evaluation.

    :param func: the function to be wrapped in the decorator
    :return: the wrapped function
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        mode = pm.evaluationManager(query=True, mode=True)[0]
        if not mode == 'off':
            print "Switching to DG evaluation."
            pm.evaluationManager(mode="off")
        try:
            return func(*args, **kwargs)
        except Exception:
            raise  # will raise original error
        finally:
            cur_mode = pm.evaluationManager(query=True, mode=True)[0]
            if not mode == cur_mode:
                print "Restoring {0} evaluation.".format(mode)
                pm.evaluationManager(mode=mode)
    return wrapped


def report_time_to_execute(func):
    """
    Prints out the name of the function and the time it took to execute the function.

    :param func: the function to be wrapped in the decorator
    :return: the wrapped function
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        delta = t2 - t1
        time_msg = str(datetime.timedelta(seconds=delta))
        msg = "{0} execute time: {1} seconds.".format(func.__name__, time_msg)
        om.MGlobal.displayInfo(msg)
        return result
    return wrapped


def apply_wait_cursor(func):
    """
    Enables the wait cursor for the entire duration of the function.

    :param func: the function to be wrapped in the decorator
    :return: the wrapped function
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        if pm.about(batch=True):  # ...this is Batch mode...
            return func(*args, **kwargs)
        # om.MGlobal.displayInfo("Enabling wait cursor for this function...")
        maya.utils.processIdleEvents()
        pm.waitCursor(state=False)  # make SURE the waitCursor stack is empty!
        pm.waitCursor(state=True)
        try:
            result = func(*args, **kwargs)
        except Exception:
            raise  # will raise original error
        finally:
            # om.MGlobal.displayInfo("Disabling wait cursor.")
            maya.utils.processIdleEvents()
            pm.waitCursor(state=False)
        return result
    return wrapped
