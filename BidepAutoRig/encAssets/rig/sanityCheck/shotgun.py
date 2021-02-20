import encLib as enc
reload(enc)
import getpass
import os
import datetime
import pymel.core as pm
import fnmatch

# this filter option restricts tasks to "Open" status (ex: Ready to Start)
filter_open_status = {"filter_operator": "any",
                      "filters": [['sg_status_list', 'is', 'elem'],
                                  ['sg_status_list', 'is', 'ip'],
                                  ['sg_status_list', 'is', 'rdy'],
                                  ['sg_status_list', 'is', 'wtg']]}

'''
========================================================================
---->  Data  <----
========================================================================
'''


def update_project_data(obj):
    projects = enc.get_shotgun_mango_projects()
    projects.sort()
    obj.data["sg_projects"] = projects


def init_shotgun_project(obj):
    project = obj.data["project_info"]["show"]
    projects = obj.data["sg_projects"]
    if project in projects:
        obj.data["sg_show_selected"] = project
    else:
        obj.data["sg_show_selected"] = "hero"


def update_assignee_data(obj):
    """
    Create a dictionary of users where the key-value pairs represent the name-id of each user.

    Originally, this function grabbed all users assigned to open rigging tasks in addition to the current user.
    Right now the dictionary contains only one entry, which represents the current user.

    :param obj: a PySide object
    :return: None
    """
    username = getpass.getuser()
    sg = enc.get_shotgun_client()
    current_user = sg.find_one("HumanUser", [["login", "is", username]], ["name"])
    obj.data["sg_users_current"] = current_user["name"]
    users = {current_user["name"]: current_user["id"]}  # make sure the current user has a place in the dictionary!
    obj.data["sg_users"] = users


def update_asset_data(obj):
    sg = enc.get_shotgun_client()
    # project_name = obj.data["sg_show_selected"]
    open_status = obj.filterStatusComboBox.currentText()
    assignee = obj.filterAssigneeComboBox.currentText()
    rig_filters = {"filter_operator": "any", "filters": [["step.Step.id", "is", 11], ["step.Step.id", "is", 30]]}
    filters = [['entity', 'type_is', 'CustomNonProjectEntity05'], rig_filters]
    if assignee != "<all>":
        current_user = sg.find_one("HumanUser", [["name", "is", assignee]], ["name"])
        filters.append(['task_assignees', 'is', current_user])      # restricts tasks to a specific user
    if open_status != "<all>":
        filters.append(filter_open_status)                          # restricts tasks to open status
    type_filters = [['entity.CustomNonProjectEntity05.sg_asset_type', 'is', obj.ctrls[x]] for x in obj.ctrls if
                    x.isChecked()]
    if type_filters:
        d = {"filter_operator": "any", "filters": type_filters}
        filters.append(d)
    # import pprint
    # pprint.pprint(filters)
    tasks = sg.find("Task", filters, ["step", "task_assignees", "project", "entity", "sg_status_list"])
    assets = {x["entity"]["name"]: x["entity"]["id"] for x in tasks}
    obj.data["sg_assets"] = assets


'''
========================================================================
---->  UI  <----
========================================================================
'''


def init_shotgun_ui_usernames(obj):
    users = obj.data["sg_users"]
    li = users.keys()
    li.sort()
    li.append("<all>")
    i = li.index(obj.data["sg_users_current"])
    obj.filterAssigneeComboBox.clear()
    obj.filterAssigneeComboBox.addItems(li)
    obj.filterAssigneeComboBox.setCurrentIndex(i)


def get_filtered_assets(assets, pattern, case_sensitive=True):
    ptn = "*" + pattern + "*"
    if case_sensitive:
        """ do a case-sensitive match """
        li = [x for x in assets if fnmatch.fnmatchcase(x, ptn)]
    else:
        """ do a case-insensitive match """
        li = fnmatch.filter(assets, ptn)
    return li


def update_shotgun_ui_assets(obj):
    assets = obj.data["sg_assets"].keys()
    assets.sort()
    fil = obj.filterLineEdit.text()
    if fil:
        assets = get_filtered_assets(assets, fil, case_sensitive=obj.mcCheckBox.isChecked())
    obj.shotgunListWidget.clear()
    obj.shotgunListWidget.addItems(assets)


def shotgun_test(obj):
    test1 = obj.shotgunListWidget.selectedItems()
    test2 = obj.shotgunCheckBox.isChecked()
    state = bool(test1) or test2
    return state


'''
========================================================================
---->  Misc. <----
========================================================================
'''


def update_shotgun_assets(obj):
    update_asset_data(obj)
    update_shotgun_ui_assets(obj)


def init_shotgun_ui(obj):
    """
    :param obj:
    :return:
    """
    update_project_data(obj)
    update_assignee_data(obj)
    init_shotgun_project(obj)
    init_shotgun_ui_usernames(obj)
    update_shotgun_assets(obj)


def get_sg_timestamp():
    """
    :return: String - a formatted date string reflecting the current time
    """
    now = datetime.datetime.now()
    timestamp = "%04d/%02d/%02d %02d:%02d" % (now.year, now.month, now.day, now.hour, now.minute)
    return timestamp


def make_thumbnail(p):
    """
    Given a file path, generate a JPEG screen capture of the active viewport next to that file path.

    Example: given "C:\temp\mayascene.mb", generate "C:\temp\mayascene.jpg"

    :param p: String - a file path to a Maya file
    :return: String - a file path to a thumbnail image
    """
    frame = pm.currentTime()
    output_dir = os.path.dirname(p).replace("\\", "/")
    output_name = os.path.basename(p).rsplit(".", 1)[0]
    output = os.path.join(output_dir, output_name)
    """ delete old files as a precaution """
    li = [x for x in os.listdir(output_dir) if x.endswith((".jpeg", ".jpg")) and x.startswith(output_name)]
    for f in li:
        target = os.path.join(output_dir, f)
        os.remove(target)
    """ make thumbnail """
    pm.setAttr("defaultRenderGlobals.imageFormat", 8)
    pm.setAttr("defaultRenderGlobals.extensionPadding", 4)
    pm.playblast(st=frame, et=frame, v=False, fmt="image", f=output, widthHeight=[1000, 1000], offScreen=True)
    """ rename the image generated by the playblast """
    li = [x for x in os.listdir(output_dir) if x.endswith((".jpeg", ".jpg")) and x.startswith(output_name)]
    if li:
        output_path = os.path.join(output_dir, li[0])
        new_name = output_name + ".jpg"
        new_path = os.path.join(output_dir, new_name)
        os.rename(output_path, new_path)
        return new_path
    return ""


'''
========================================================================
---->  Publish Rig to Shotgun <----
========================================================================
'''


def publish_rig_to_shotgun(d):
    """
    :param d: dictionary
    :return: None
    """
    """ Initialize variables """
    mango_path = d["sg_paths"]["mango_publish"]
    rig_backup_path = d["sg_paths"]["rig_backup"]
    rig_publish_path = d["sg_paths"]["rig_publish"]
    thumbnail_path = make_thumbnail(rig_backup_path)
    asset_name = d["sg_asset_selected"]
    asset_id = d["sg_assets"][asset_name]
    username = getpass.getuser()
    show = d["sg_show_selected"]
    """ Initialize Shotgun data. Cancel Shotgun publish if data not found. """
    sg = enc.get_shotgun_client()
    asset_code = "CustomNonProjectEntity05"
    project, asset, user = enc.get_shotgun_project_asset_user(sg, show, asset_id, username, asset_code=asset_code)
    if project is None:   # something failed. Stop immediately.
        return
    """ publish Mango file """
    data = {'description': d["comment"], 'name': "Mango publish"}
    mango_pub = enc.get_shotgun_scene_publish(sg, mango_path, asset[0], project[0], user[0], additional_data=data)
    """ publish backup file """
    data = {'description': d["comment"], 'name': "backup", 'upstream_published_files': [mango_pub]}
    backup_pub = enc.get_shotgun_scene_publish(sg, rig_backup_path, asset[0], project[0], user[0], additional_data=data)
    """ publish and update versionless file """
    data = {'name': "versionless", 'upstream_published_files': [mango_pub]}  # this only applies to the first publish
    rig_type = {'id': 21, 'type': 'PublishedFileType'}
    rig_pub = enc.get_shotgun_file_publish(sg, rig_publish_path, asset[0], project[0], user[0],
                                           rig_type, additional_data=data)
    sg.update("PublishedFile", rig_pub["id"], {'upstream_published_files': [mango_pub]})
    timestamp = get_sg_timestamp()
    description = timestamp + " - " + d["comment"] + "\nMango publish version: " + d["mango_publish_version"]
    if rig_pub['description'] is not None:
        description += "\n\n" + rig_pub['description']
    rig_data = {'description': description,
                'version_number': enc.get_scene_version(),
                'task': enc.get_shotgun_task(sg, asset[0], user[0])}
    sg.update("PublishedFile", rig_pub["id"], rig_data)
    """ update thumbnails """
    if thumbnail_path:
        sg.upload_thumbnail("PublishedFile", mango_pub['id'], thumbnail_path)
        sg.upload_thumbnail("PublishedFile", backup_pub['id'], thumbnail_path)
        sg.upload_thumbnail("PublishedFile", rig_pub['id'], thumbnail_path)
