from __future__ import division  # used for humanize_bytes function
import os
import datetime
import shutil
import getpass
try:
    import pymel.core as pm
except ImportError:
    pass

import encLib as enc
reload(enc)

__author__ = 'jhachigian'

publishDict = {}
TIMESTAMP = ""


def publish_mango():
    try:
        import losPipeLineTools
        losPipeLineTools.workFilePublishUI()
    except ImportError:
        msg = "Failed to import Mango."
        print msg
        pm.confirmDialog(title="Failed to launch Mango...", message=msg, icon='critical')
        return False
    return True


def get_latest_published_workfile(folder_path):
    """
    Retrieves the latest published workfile for a given "workfiles_path" folder. For examp

    :param folder_path: a folder path
    :return: String - path to the latest published Mango workfile
    """
    versions = [x for x in os.listdir(folder_path) if x.startswith("v") and len(x) == 5]
    versions.sort()
    if not versions:
        return folder_path
    p = os.path.join(folder_path, versions[-1])
    published_maya_files = [x for x in os.listdir(p) if x.endswith((".mb", ".ma"))]
    if not published_maya_files:
        return p
    p = os.path.join(p, published_maya_files[0])
    return p


# def get_timestamp():
#     now = datetime.datetime.now()
#     timestamp = "%04d%02d%02d%02d%02d" % (now.year, now.month, now.day, now.hour, now.minute)
#     return timestamp


def get_timestamp(now=None):
    if now is None:
        now = datetime.datetime.now()
    timestamp = "%04d%02d%02d%02d%02d" % (now.year, now.month, now.day, now.hour, now.minute)
    return timestamp


def humanize_bytes(bytes, precision=1):
    """
    A recipe by Doug Latornell from http://code.activestate.com
    :param bytes: number of bytes
    :param precision: number of decimal places
    :return:
    """
    abbrevs = (
        (1 << 50L, 'PB'),
        (1 << 40L, 'TB'),
        (1 << 30L, 'GB'),
        (1 << 20L, 'MB'),
        (1 << 10L, 'kB'),
        (1, 'bytes')
    )
    if bytes == 1:
        return "1 byte"
    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return '%.*f %s' % (precision, bytes / factor, suffix)


def update_publish_dict():
    maya_path = pm.system.sceneName()
    project_info = enc.getProjectDict(maya_path)
    if project_info["isValid"]:
        # from pprint import pprint
        # pprint(project_info)
        rig_folder = os.path.join(project_info["dir3d"], "publish", "rigs")
        publishDict["rigs"] = {}
        if os.path.exists(rig_folder):
            files = [x for x in os.listdir(rig_folder) if x.endswith((".mb", ".ma"))]
            for f in files:
                key = f.rsplit(".", 1)[0]
                rig_path = os.path.join(rig_folder, f)
                rig_name = f
                rig_size = humanize_bytes(os.path.getsize(rig_path))
                rig_date = os.path.getmtime(rig_path)
                rig_datetime = datetime.datetime.fromtimestamp(rig_date)
                rig_timestamp = rig_datetime.strftime("%m-%d-%Y %I:%M%p")
                publishDict["rigs"][key] = {}
                publishDict["rigs"][key]["path"] = rig_path
                publishDict["rigs"][key]["filename"] = rig_name
                publishDict["rigs"][key]["size"] = rig_size
                publishDict["rigs"][key]["date"] = rig_date
                publishDict["rigs"][key]["timestamp"] = rig_timestamp
        publishDict["rigFolder"] = rig_folder
        # pprint(publishDict)


def copyfile(src, dst, msg="Copying:"):
    print "\t", msg, src
    print "\t\tTo:", dst
    shutil.copyfile(src, dst)


def publish_rig(src, dst):
    folder = os.path.dirname(dst)
    if not os.path.exists(folder):
        print "Making directory:", folder
        os.makedirs(folder)
    print "\tSaving scene..."
    pm.cmds.file(save=True)
    try:
        copyfile(src, dst)
        msg = os.path.basename(dst)
        title = "Done."
    except (WindowsError, IOError):
        msg = "Could not publish file due to permissions issues. Open up an IT ticket for this folder:\r\n\r\n"
        msg += os.path.dirname(dst)
        title = "FAILED"
    return title, msg


def backup_rig(src, dst, comment=""):
    folder, filename = os.path.split(dst)
    timestamp = get_timestamp()
    backup_folder = os.path.join(folder, "_old", timestamp)
    backup_path = os.path.join(backup_folder, filename)
    backup_dat = backup_path.rsplit(".", 1)[0] + ".dat"

    """ include publish directory, if possible """
    publish_dir = ""
    publish_path = ""
    d = enc.getProjectDict(src)
    if d["isValid"]:
        # version = int(d["version"][1:]) + 1
        # v = "v%04d" % version
        v = d["version"]
        work_dir = os.path.basename(d["path"])
        publish_file = d["filename"].replace(d["version"], v)
        publish_dir = os.path.join(d["dir3d"], "publish", "workfiles", work_dir, v)
        publish_path = os.path.join(publish_dir, publish_file)

    if not os.path.exists(backup_folder):
        print "\t\tMaking directory:", backup_folder
        os.makedirs(backup_folder)
    copyfile(dst, backup_path, msg="Backing up:")
    """ write report """
    print "\tWriting:", backup_dat
    report = ["",
              "[Information]",
              "creationDatetime=" + timestamp,
              "source=Maya",
              "username=" + getpass.getuser(),
              "workarea=" + src.split("/")[10],
              "originalFile=" + filename,
              "fullPath=" + src,
              "publishDir=" + publish_dir,
              "publishPath=" + publish_path,
              "comment=" + comment]
    text = "\r\n".join(report)
    with open(backup_dat, "w") as fp:
        fp.write(text)
    return backup_path


@enc.restore_selections
def update_rig_comment(comment, mango_publish_version=""):
    """
    Updates the note on world_anim with a comment. world_anim MUST be unselected for its notes to get updated.
    :param comment: a text string
    :param mango_publish_version: the Mango Publish Version (ex: "v0004")
    :return: None
    """
    print "\tUpdating comment on world_anim..."
    global TIMESTAMP
    target = "world_anim"
    now = datetime.datetime.now()
    date = now.strftime("%m-%d-%Y %I:%M%p")
    TIMESTAMP = date
    if pm.objExists(target):
        pm.select(clear=True)
        pm.refresh(force=True)
        node = pm.PyNode(target)
        if not node.hasAttr("notes"):
            pm.addAttr(node, longName="notes", shortName="nts", dataType="string")
            node.setAttr("notes", "")
        old_text = node.getAttr("notes")
        lines = ["Published: " + date + " by " + getpass.getuser(),
                 "Timestamp: " + get_timestamp(now),
                 "Filename: " + os.path.basename(pm.system.sceneName()),
                 "Fullpath: " + pm.system.sceneName(),
                 "Workarea: " + pm.system.sceneName().split("/")[10],
                 "User: " + getpass.getuser(),
                 "Mango publish version: " + mango_publish_version,
                 ""]
        new_text = "\r\n".join(lines) + "\r\n\r\n"
        new_text += comment + "\r\n\r\n" + ("_" * 20 + "\r\n") * 3 + "\r\n\r\n"
        if old_text.find(new_text) == -1:
            new_text += old_text
            node.setAttr("notes", new_text)


if __name__ == "__main__":
    p1 = r"Z:\data\diablo2\PROJECTS\test\04_episodes\--assets\chr-dominator\3d\publish\workfiles\rig_dominator"
    print get_latest_published_workfile(p1)
