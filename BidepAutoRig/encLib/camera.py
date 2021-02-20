import os
import re
import util
import mango
import shotgun
try:
    import pymel.core as pm
except ImportError:
    pass
__author__ = 'jhachigian'


def get_encore_cameras():
    """
    Returns a dictionary of Encore-named cameras that match the shot. Called by Publish Camera.

    :return: Dictionary
    """
    maya_path = pm.system.sceneName()
    if not maya_path:
        return {}
    prefix = shotgun.get_shot_prefix()
    pattern = re.compile(prefix + "_[0-9_]+mm_f\d{3,4}_\d{3,4}_v\d{3}($|_previs$|_master$|_tracked$)")
    d = {}
    for c in pm.ls(cameras=True):
        par = c.getParent()
        n = par.nodeName()     # the name of the camera transform
        util.debug("Testing: " + n)
        m = re.search(pattern, n)
        if m:
            if c.nodeName() == n:       # this will cause problems. Rename the camera shape!
                c.rename(n + "Shape")
            k = par.shortName()    # the shortest unique pathname of the camera transform.
            d[k] = {"transform": par, "camera": c}
    return d


def get_cameras():
    """
    Return Encore cameras, if they exist, if not, return renderable cameras, if that fails, return ANY cameras.

    :return: list of Maya cameras
    """
    cameras = pm.ls(cameras=True)
    encore_cam_dict = get_encore_cameras()
    encore_cams = encore_cam_dict.keys()
    if encore_cams:
        return encore_cams
    else:
        renderable_cameras = []
        scene_cameras = []
        for cam in cameras:
            cam_name = cam.name()
            mypar = cam.getParent()
            mypar_name = mypar.name()
            renderable = pm.getAttr(cam_name + '.renderable')
            if renderable:
                renderable_cameras.append(mypar_name)
            else:
                scene_cameras.append(mypar_name)
        if renderable_cameras:
            return renderable_cameras
        else:
            return scene_cameras


def is_doom_camera(cam):
    """
    If it's a "doom" scene and the camera has a 2:39 aspect ratio, return True. Otherwise return False.

    :param cam: PyNode - a camera shape
    :return: Boolean
    """
    maya_path = pm.system.sceneName()
    if not maya_path:
        return
    project_dict = mango.getProjectDict(maya_path)
    if project_dict["show"] != "doom":
        return False
    w = cam.getAttr("horizontalFilmAperture")
    h = cam.getAttr("verticalFilmAperture")
    if w/h == 2.39:
        return True
    return False


def validateCameraSettings(cam):
    """
    A safety check for making previews and exporting cameras.

    Return True if the camera settings are valid and False otherwise.

    :param cam: PyNode - a camera shape
    :return: Boolean
    """
    if is_doom_camera(cam):
        return True
    d = {"horizontalFilmAperture": 0.935,
         "verticalFilmAperture": 0.526,
         "lensSqueezeRatio": 1.0}
    for k in d:
        if round(cam.getAttr(k), 3) != d[k]:
            util.debug("Cam: " + cam.name() + " attr: " + k + " is " + str(cam.getAttr(k)) + " not " + str(d[k]))
            x = cam.getAttr(k)
            util.debug(str(type(x)))
            return False
    return True


def identify_camera(cam):
    """
    :param cam: PyNode - a camera shape.
    :return: String - camera type or "unknown" if the camera cannot be identified.
    """
    d = {"Red Epic Mysterium-X": {"horizontalFilmAperture": 1.0906,
                                  "verticalFilmAperture": 0.5751,
                                  "lensSqueezeRatio": 1.0},
         "Red Dragon": {"horizontalFilmAperture": 1.2087,
                        "verticalFilmAperture": 0.6216,
                        "lensSqueezeRatio": 1.0},
         "Red Epic": {"horizontalFilmAperture": 1.0205,
                      "verticalFilmAperture": 0.5740,
                      "lensSqueezeRatio": 1.0},
         "Sony PMW-F55": {"horizontalFilmAperture": 0.9949,
                          "verticalFilmAperture": 0.5000,
                          "lensSqueezeRatio": 1.0},
         "Alexa Mini": {"horizontalFilmAperture": 1.0394,
                        "verticalFilmAperture": 0.05846,
                        "lensSqueezeRatio": 1.0},
         "Red Weapon": {"horizontalFilmAperture": 0.883,
                        "verticalFilmAperture": 0.454,
                        "lensSqueezeRatio": 1.0},
         }
    for camera_type in d:
        test = True
        for k in d[camera_type]:
            if round(cam.getAttr(k), 3) != round(d[camera_type][k], 3):
                util.debug("Cam: %s attr: %s is %0.4f not %f" % (cam.name(), k, cam.getAttr(k), d[camera_type][k]))
                test = False
                util.debug("")
        if test:
            return camera_type
    return "unknown"


def get_camera_name(d, cam, offset=1):
    """
    :param d: the "pstruct" dictionary made by encLib from the Maya scene file path
    :param cam: the camera transform, in PyNode format.
    :return: the ideal name for this camera. NOTE: this function relies on PyMEL.
    """
    """ gather data """
    if cam.type() == "camera":
        shp = cam
    else:
        shp = cam.getShape()
    foc = ("%g" % shp.getAttr("focalLength")).replace(".", "_")
    start_frame = pm.animation.playbackOptions(q=True, minTime=True)
    end_frame = pm.animation.playbackOptions(q=True, maxTime=True)
    backup = os.path.join(d['dirCamera'], "_old")
    if os.path.exists(backup):
        ver = len(os.listdir(backup)) + offset
    else:
        ver = 1
    """ build camera name """
    name = "_".join((d['show'], d['episode'], d['shot'].replace("-", "_")))
    name += "_%smm_f%03d_%03d_v%03d" % (foc, start_frame, end_frame, ver)
    return name
