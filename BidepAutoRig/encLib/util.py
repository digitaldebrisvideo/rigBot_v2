import json
import os
import codecs
import platform
import shutil
try:
    import pymel.core as pm
except ImportError:
    pass
__author__ = 'jhachigian'

enable_debug = False


def debug(text):
    if enable_debug:
        print text


def openFolder(p):
    if os.path.exists(p) and platform.system() == 'Windows':
        debug("Opening: " + p)
        os.system("explorer.exe " + os.path.normpath(p))


def save_json_file(folder, d, filename="cacheData.json"):
    """
    :param folder: String - destination folder
    :param filename: String - filename
    :return: String - the path of the JSON file
    """
    p = os.path.join(folder, filename)
    with open(p, "w") as fp:
        json.dump(d, fp, indent=5)
    return p


def save_maya_scene_copy(folder, use_shutil=False):
    """
    :param folder: String - destination folder
    :param use_shutil: Boolean - whether to use shutil or Maya's native cmds.file to do the copy.
    :return: String - the path of the copy of the Maya scene
    """
    scene_name = pm.system.sceneName()
    filename = os.path.join(folder, os.path.basename(scene_name))
    if use_shutil:
        shutil.copy2(scene_name, filename)
    else:
        pm.cmds.file(rename=filename)
        pm.cmds.file(save=True)
        pm.cmds.file(rename=scene_name)
    return filename


def get_settings(node_name):
    """
    Given a string representing the name of a scriptNode in the scene, return a dictionary representing the
    settings data contained in that scriptNode.

    :param node_name: a string
    :return: a dictionary
    """
    if pm.objExists(node_name):
        script = pm.scriptNode(node_name, query=True, beforeScript=True)
        s = script.split("= ")[-1]
        """ make 's' JSON safe """
        s = s.replace("True", "true")
        s = s.replace("False", "false")
        d = json.loads(s)
        return d
    return {}


def set_settings(node_name, dict_name, d):
    """
    Given a string and a dictionary, either update an existing scriptNode in the Maya scene with the same name
    as the string, or create a fresh new scriptNode with the same name as the string. The scriptNode's beforeScript
    will have a string assigning a dictionary to a variable.

    :param node_name: a string
    :param dict_name: a string
    :param d: a dictionary
    :return: None
    """
    x = json.dumps(d)
    """ make 'x' scriptNode safe """
    x = x.replace("true", "True")
    x = x.replace("false", "False")
    script = dict_name + " = " + x
    if not pm.objExists(node_name):
        pm.scriptNode(scriptType=1, name=node_name, beforeScript=script, sourceType="python")
        pm.scriptNode(node_name, executeBefore=True)
    else:
        pm.scriptNode(node_name, edit=True, beforeScript=script)


def read_file(src):
    """
    A bilingual way to read INI text files written by Max and by Maya.

    :src: String a path to a text file.
    :return: String
    """
    open_file = file(src, 'r')
    encoding = None
    line = open_file.readline()
    open_file.close()
    if line.startswith('\xFF\xFE'):
        encoding = 'utf-16-le'
    f = codecs.open(src, encoding=encoding)
    t = f.read()
    f.close()
    return t


def has_string(x, li):
    for s in li:
        if x.lower().find(s) != -1:
            return True
    return False


def delete_anim(nodes):
    """
    Delete animation from a given set of nodes and zero out their keyable values.

    :param nodes: a list of PyMEL nodes
    :return:
    """
    blacklist = ("visibility", "scale")  # make this all lowercase.
    for node in nodes:
        user_defined = node.listAttr(userDefined=True)
        pm.cutKey(node)
        for attr in node.listAttr(scalar=True, unlocked=True, keyable=True, visible=True, userDefined=False):
            if not has_string(attr.name(), blacklist) and attr not in user_defined:
                pm.setAttr(attr, 0)
