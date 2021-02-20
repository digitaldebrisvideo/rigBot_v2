"""
    Blacklist by Jennifer Hachigian

    01/27/2017

    Use these functions to add/remove paths from the Asset Manager blacklist.
"""

import json
import pkgutil
import os

""" dst_dir's location will change with the current sys.path location of encAsset.loader """
dst_dir = pkgutil.find_loader("encAsset.loader").filename
dst = os.path.join(dst_dir, "blacklist.json")


def get_blacklist():
    """
    Opens the blacklist.json file and returns the contents as a list.
    :return: a list containing all blacklisted paths.
    """
    with open(dst, "r") as fp:
        li = json.load(fp)
    return li


def remove_path(p):
    """
    Removes the given path from the blacklist.
    :param p: the path to be removed from the blacklist.
    :return: None
    """
    li = get_blacklist()
    try:
        i = li.index(p)
        li.pop(i)
    except ValueError:
        print "\tNot blacklisted:", p
    """ update JSON file """
    with open(dst, "w") as fp:
        json.dump(li, fp, indent=5)


def insert_path(p):
    """
    Inserts the given path into the blacklist.
    :param p: the path to be blacklisted.
    :return: None
    """
    li = get_blacklist()
    if p not in li:
        li.append(p)
        li.sort()
    else:
        print "\tAlready blacklisted:", p
    """ update JSON file """
    with open(dst, "w") as fp:
        json.dump(li, fp, indent=5)


if __name__ == "__main__":
    test_path = r"Z:\data\diablo2\PROJECTS\supr\04_episodes\--assets\chr-parasite\3d\publish\rigs\rig_parasite.mb"
    remove_path(test_path)
