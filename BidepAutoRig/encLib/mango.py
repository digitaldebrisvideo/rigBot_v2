import os
import re
import util

__author__ = 'jhachigian'

encPrjRoot = r"Z:\data\diablo2\PROJECTS"
encCacheRoot = r"U:\data\diablo2\PROJECTS"
localRoot = r"C:\data\diablo2\PROJECTS"
encEpiRoot = "04_episodes"


def is_mango(p):
    if not p.startswith(encPrjRoot):
        util.debug("Path does not start with: " + encPrjRoot)
        return False
    li = p.split(os.path.sep)
    ver = re.compile("v\d{4}")
    if not ver.findall(li[-1]):
        util.debug("Filename does not contain a properly formatted version.")
        return False
    if li[8].lower() not in ("3d", "2d"):
        util.debug("Path not in a 3d/2d folder...")
        return False
    return True


def getProjectDict(scenepath):
    """
    :param scenepath: the path of a Mango-formatted scene file.
    :return: a dictionary containing information parsed from the scenepath.
    """
    p = os.path.normpath(scenepath)
    d = {}
    d["isValid"] = False
    if not is_mango(p):
        return d
    try:
        d["fullPath"] = p
        d["path"] = os.path.dirname(p)
        d["filename"] = os.path.basename(p)
        d["fullName"], d["extension"] = os.path.splitext(d["filename"])
        d["name"] = d["fullName"][:-6]
        # parse the fullName to get episode, shot, type, task and version info.
        li = d["fullName"].split("_")
        d["episode"] = li[0]
        d["shot"] = li[1]
        d["type"] = li[2]
        d["task"] = li[3]
        if "-" in li[4]:
            d["isSnapshot"] = True
            d["version"] = li[4].split("-")[0]
        else:
            d["isSnapshot"] = False
            d["version"] = li[4]
        # get remaining values.
        d["show"] = p.split(os.path.sep)[4]
        d["dirShow"] = os.path.join(encPrjRoot, d["show"], "")
        d["dirEpisode"] = os.path.join(d["dirShow"], encEpiRoot, d["episode"], "")
        d["dirShot"] = os.path.join(d["dirEpisode"], d["shot"], "")
        d["dir3d"] = os.path.join(d["dirShot"], "3d", "")
        d["dir2d"] = os.path.join(d["dirShot"], "2d", "")
        d["dirCache"] = os.path.join(d["dir3d"].replace(encPrjRoot, encCacheRoot), "publish", "cache", "")
        d["dirCacheLocal"] = d["dirCache"].replace(encCacheRoot, localRoot)
        d["dir3delements"] = os.path.join(d["dir3d"], "publish", "3delements", "")
        d["dirCamera"] = os.path.join(d["dir3d"], "publish", "cameras", "publishCamera", "")
        d["isValid"] = True
    except:
        pass
    return d


def getMangoProjects():
    li = []
    for f in os.listdir(encPrjRoot):
        test = os.path.join(encPrjRoot, f, "04_episodes")
        if os.path.exists(test):
            li.append(f)
    li.sort()
    return li


def get_mango_profile():
    """
    :return: String - the Mango profile (ex: "baseProfile", "Redshift") or an empty string if no profile is found.
    """
    try:
        import losPipeLineTools
        return losPipeLineTools.mangoAPI.getSoftwareLauncherProfile()
    except ImportError:
        print "Mango modules not installed."
        return ""
    except AttributeError:
        print "losPipeLineTools.mangoAPI.getSoftwareLauncherProfile() not found."
        return ""


def sort_episode_list(li):
    """
    usage: sort a list (li) so that "--assets" is listed first, episodes (ex: 312, 313, 314) get listed in reverse
           order, and everything else gets listed in alphabetical order.

    example: if li is #("--assets", "001", "002", "003", "rnd", "ini"), this script will return:
                      #("--assets", "003", "002", "001", "ini", "rnd")

    :param li: a List of strings representing episodes
    :return: a sorted List
    """
    episodes = [x for x in li if x.isdigit()]
    remainder = [x for x in li if x != "--assets" and x not in episodes]
    episodes.sort(reverse=True)
    remainder.sort()
    ordered = []
    if "--assets" in li:
        ordered.append("--assets")
    ordered += episodes
    ordered += remainder
    return ordered


if __name__ == "__main__":
    test_path = r"Z:\data\diablo2\PROJECTS\tita\04_episodes\--assets\chr-tony-zucco\3d\publish\workfiles\mdl_tony-zucco\v0004\--assets_chr-tony-zucco_mdl_tony-zucco_v0004.max"
    test_dict = getProjectDict(test_path)
    import pprint
    pprint.pprint(test_dict)
    # for mango_project in getMangoProjects():
    #     print mango_project
    sort_episode_list_test = "--assets", "001", "002", "003", "rnd", "ini"
    print sort_episode_list(sort_episode_list_test)
