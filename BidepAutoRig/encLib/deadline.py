import subprocess
import os
import re
try:
    import pymel.core as pm
except ImportError:
    pass

__author__ = 'jhachigian'


deadline_defaults = {"ChunkSize": 100000,
                     "Comment": "This is a script-generated Deadline job.",
                     "Group": "maya",
                     "LimitGroups": "",
                     "MachineLimit": 1,
                     "OverrideTaskExtraInfoNames": False,
                     "Pool": "3d",
                     "Plugin": "MayaBatch",
                     "Priority": 90,
                     "submit_as_suspended": False  # Controls InitialStatus - True == Suspended
                     }


def get_deadline_temp_folder():
    """
    :return: String - a temp folder for Deadline submissions.
    """
    # cmd = "deadlinecommand -GetCurrentUserHomeDirectory"
    # proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    # msg = proc.communicate()
    # folder = msg[0].strip("\r\n")
    # temp_folder = os.path.join(folder, "temp")
    if "LOCALAPPDATA" in os.environ:
        local_app_data = os.environ["LOCALAPPDATA"]
        temp_folder = os.path.join(local_app_data, "Thinkbox", "Deadline10", "temp")
    else:
        temp_folder = r"C:\temp\deadline\submission_files"
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    return temp_folder


def get_deadline_command():
    """
    Called by convertPlates, geocache, and the nCacheTool.

    :return: String - a path to deadlinecommand.exe
    """
    p = os.environ.get("DEADLINE_PATH")
    if p is None:
        return "C:\\apps64\\Thinkbox\\deadline8\\bin\\deadlinecommand.exe"
    else:
        return os.path.join(p, "deadlinecommand.exe")


def show_deadline_message(msg, job_type="Alembic caches"):
    """
    :param msg: List - of tuples from Deadline (ex: (("message1", None), ("message2", None))
    :param job_type: String - what will be mentioned in the message box (ex: "caches", "renders", "bunnies")
    :return: None
    """
    if not msg:
        return
    if type(msg[0]) is str:  # someone sent a single Deadline tuple to this function
        message = msg[0]
    else:  # a tuple of tuples has been sent.
        li = [x[0] for x in msg]
        message = "\r\n\rn".join(li)
    if not message:
        return
    pattern = re.compile("(?<=Result=).*")
    results = pattern.findall(message)
    successes = []
    from PySide2 import QtWidgets
    icon = QtWidgets.QMessageBox.NoIcon  # default icon -- nothing!
    if results:
        successes = [x for x in results if x.startswith("Success")]
        if len(successes) == len(results):
            title = "Success!"
        else:
            icon = QtWidgets.QMessageBox.Critical
            title = "Not all jobs went through..."
    else:
        icon = QtWidgets.QMessageBox.Critical
        title = "Failed."
    body = "Submitted {0} of {1} jobs successfully to Deadline.".format(len(successes), len(results))
    if results:
        body += "\r\n\r\nIMPORTANT: your {0} are NOT yet done. ".format(job_type)
        body += "Please open and use Deadline Monitor to track the progress of your jobs."
    msgbox = QtWidgets.QMessageBox()
    msgbox.setWindowTitle(title)
    msgbox.setText(body)
    msgbox.setDetailedText(message)  # this disables the "X" button...annoying, but fixable...
    msgbox.setIcon(icon)
    """ the following restores the ability of the "X" button to close the QMessageBox """
    msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgbox.setDefaultButton(QtWidgets.QMessageBox.Ok)
    msgbox.setEscapeButton(QtWidgets.QMessageBox.Ok)
    """ launch QMessageBox """
    msgbox.exec_()


def submit_to_deadline(args):
    """
    Called by utilities like Create Geocache and Create Alembic.

    :param args: String - a file path to an arguments list for Deadline command
    :return: Tuple - Deadline's message
    """
    exe = get_deadline_command()
    cmd = "%s %s" % (exe, args)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    msg = proc.communicate()
    return msg


def prep_temp_folder(folder):
    """
    Make the folder if it does not exist, or remove all files from it if it does exist.

    :param folder: String - a folder path
    :return: None
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    else:
        files = [os.path.join(folder, x) for x in os.listdir(folder) if os.path.isfile(os.path.join(folder, x))]
        for p in files:
            os.remove(p)


def list_to_text_file(li, filename):
    """
    Called by Create Geocache and Create Alembic to build an arguments list for Deadline.

    :param li: List - a list of strings
    :param filename: String - a file path
    :return: None
    """
    text = "\r\n".join(li)
    with open(filename, "w") as fp:
        fp.write(text)


def save_deadline_job_info(temp_folder, job_name, output_folder,
                           frames="101",
                           chunk_size=deadline_defaults["ChunkSize"],
                           pool=deadline_defaults["Pool"],
                           override_task=deadline_defaults["OverrideTaskExtraInfoNames"],
                           plugin=deadline_defaults["Plugin"],
                           priority=deadline_defaults["Priority"],
                           machine_limit=deadline_defaults["MachineLimit"],
                           group=deadline_defaults["Group"],
                           submit_as_suspended=deadline_defaults["submit_as_suspended"],
                           limit_groups=deadline_defaults["LimitGroups"],
                           comment=deadline_defaults["Comment"],
                           prefix="", batchname="", job_dependencies=None, env_vars=None):
    """
    Called by Create Geocache, Create Alembic, and other utilities that need to submit a Maya Batch job to the farm.

    :param temp_folder: String - the path to the temp Deadline folder
    :param job_name: String - the name the job should have on the Deadline render farm
    :param output_folder: String - the path to the output directory
    :param frames: String - Frames (ex: "101", "1-10", "1, 5, 6-10")
    :param chunk_size: Integer - ChunkSize (ex: 100000)
    :param pool: String - Pool (ex: "rush")
    :param override_task: Boolean - OverrideTaskExtraInfoNames (ex: False)
    :param plugin: String - Plugin (ex: "MayaBatch")
    :param priority: Integer - Priority (ex: 90)
    :param machine_limit: Integer - MachineLimit (ex: 1)
    :param group: String - Group (ex: "maya")
    :param submit_as_suspended: Boolean - sets InitialStatus (True: "Suspended")
    :param limit_groups: String - LimitGroups (ex: "phx")
    :param comment: String - Comment (ex: "This is a script-generated Deadline job.")
    :param prefix: String - optional prefix for the jobInfo file.
    :param batchname: String - optional batchname (ex: "tita_201_027_690_lnr_trigon_lnr_v0001")
    :param job_dependencies: List - of Strings representing Deadline job IDs (ex: ['5d5760e658815d63e4c20d67'])
    :param env_vars: Dictionary of additional environment variables.
    :return: String - the file path of the job info file
    """
    import getpass
    import socket
    user_name = getpass.getuser()
    host_name = socket.gethostname()
    try:
        profile = os.environ['SWL_PROFILE']
    except KeyError:
        profile = "baseProfile"
    """ build the job info file """
    if not job_name.startswith("Name="):
        job_name = "Name={0}".format(job_name)
    li = [job_name,
          "UserName=%s" % user_name,
          "Comment=%s" % comment,
          "Frames=%s" % frames,
          "ChunkSize=%d" % chunk_size,
          "Pool=%s" % pool,
          "OverrideTaskExtraInfoNames=%s" % str(override_task),
          "MachineName=%s" % host_name,
          "Plugin=%s" % plugin,
          "OutputDirectory0=%s" % output_folder,
          "Priority=%d" % priority,
          "MachineLimit=%d" % machine_limit,
          "LimitGroups=%s" % limit_groups,
          "Group=%s" % group,
          "BatchName=%s" % batchname,
          "ExtraInfoKeyValue0=PluginProfile=%s" % profile,
          "EnvironmentKeyValue0=SWL_PROFILE=%s" % profile,
          ]
    if env_vars:
        for i, k in enumerate(env_vars):
            n = i + 1
            ln = "EnvironmentKeyValue{0}={1}={2}".format(n, k, env_vars[k])
            li.append(ln)
    if submit_as_suspended:
        li.append("InitialStatus=Suspended")
    if job_dependencies:
        for i, job in enumerate(job_dependencies):
            li.append("JobDependency{0}={1}".format(i, job))
        li.append("ResumeOnDeletedDependencies=True")
        li.append("ResumeOnFailedDependencies=True")
    """ write the job info file """
    if not prefix.endswith(("-", "_")):
        prefix = "{0}_".format(prefix)
    filename = os.path.join(temp_folder, "{0}jobInfo.job".format(prefix))
    list_to_text_file(li, filename)
    return filename


def save_deadline_plugin_info(temp_folder, script_name, maya_file="", prefix=""):
    """
    Called by Create Geocache, Create Alembic, and other utilities that need to submit a Maya Batch job to the farm.

    :param temp_folder: String - the path to the temp Deadline folder
    :param script_name: String - the name of the script submitted to Deadline (ex: "createAlembic_Deadline.py")
    :param maya_file: String - location of a Maya file.
    :param prefix: String - optional prefix for the pluginInfo file.
    :return: String - the filename of the plugin info file
    """
    """ build the plugin info file """
    li = ["Animation=0",
          "Version=%s" % pm.about(version=True),
          "Build=64bit",
          "ScriptJob=True",
          "ScriptFilename=%s" % script_name
          ]
    if maya_file:
        line = "SceneFile={0}".format(maya_file)
        li.append(line)
    """ write the plugin info file """
    if not prefix.endswith(("-", "_")):
        prefix = "{0}_".format(prefix)
    filename = os.path.join(temp_folder, "{0}pluginInfo.job".format(prefix))
    list_to_text_file(li, filename)
    return filename
