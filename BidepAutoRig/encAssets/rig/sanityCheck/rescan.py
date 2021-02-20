"""
    Rescan by Jennifer Hachigian

    adapted from the Asset Manager toolset by Jennifer Hachigian

    8/15/2016

    usage: run "rescan_assets" to scan all published rig folders for flas, supr, leot and arro.
"""

import os
import json
import pkgutil

__author__ = 'jhachigian'

path1 = r"04_episodes\--assets"
path2_list = [r"3d\publish\rigs", r"3d\publish\rig"]
projectsFolder = r"Z:\data\diablo2\PROJECTS"


""" dst_dir's location will change with the current sys.path location of encAsset.loader """
dst_dir = pkgutil.find_loader("encAsset.loader").filename

dst = os.path.join(dst_dir, "show_assets.json")
""" projects_list contains projects visible to everyone. projects_add contains hidden projects (ex: rsbd) """
projects_list = os.path.join(dst_dir, "projects_list.json")
projects_add = os.path.join(dst_dir, "projects_additional.json")


def has_rig(p, x):
    for path2 in path2_list:
        test = os.path.join(p, x, path2)
        if os.path.exists(test) and os.path.isdir(test) and os.listdir(test):
            return True
    return False


def get_show_dict_old():
    """
    Retrieve the current dictionary contained in the show_assets JSON file.

    :return: Dictionary
    """
    if not os.path.exists(dst):
        return {}
    with open(dst, "r") as fp:
        d = json.load(fp)
    return d


def get_projects_list():
    """
    :return: List
    """
    with open(projects_list, "r") as fp:
        projects = json.load(fp)
    with open(projects_add, "r") as fp:
        projects += json.load(fp)
    return projects


def get_show_dict():
    """
    Build a new show_assets dictionary. Respect the contents of the old show_assets dictionary.

    :return: Dictionary
    """
    d = get_show_dict_old()
    projects = get_projects_list()
    for i, show in enumerate(projects):
        print "Analyzing %d of %d: %s" %  (i + 1, len(projects), show)
        if show not in d:
            d[show] = []
        test_path = os.path.join(projectsFolder, show, path1)
        if os.path.exists(test_path):
            try:
                dirs = os.listdir(test_path)
            except WindowsError:  # the user does not have access to test_path. Skip it.
                continue
            for x in dirs:
                if x.startswith(("chr-", "prp-", "veh-")) and has_rig(test_path, x) and x not in d[show]:
                    d[show].append(x)
            d[show].sort()
    return d


def insert_path(p):
    """
    Update the Asset Manager dictionary with a single path.
    :param p: the path of a published character rig.
    :return:
    """
    print "\tUpdating Asset Manager JSON..."
    with open(dst, "r") as fp:
        d = json.load(fp)
    """ update dictionary """
    p = p.replace("/", "\\")
    li = p.split("\\")
    show = li[4]
    x = li[7]
    if show not in d:
        d[show] = []
    if x not in d[show]:
        d[show].append(x)
    d[show].sort()
    """ output updated dictionary """
    with open(dst, "w") as fp:
        json.dump(d, fp, indent=5)


def rescan_assets():
    show_dict = get_show_dict()
    with open(dst, "w") as fp:
        json.dump(show_dict, fp, indent=5)


if __name__ == "__main__":
    # test_path = r"Z:\data\diablo2\PROJECTS\flas\04_episodes\--assets\chr-jaygarrick\3d\publish\rigs\test.mb"
    # rescan_assets()
    from pprint import pprint
    pprint(get_show_dict())
