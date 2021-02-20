import os
import json
import mango
try:
    import pymel.core as pm
except ImportError:
    pass

__author__ = 'jhachigian'


def get_shot_prefix():
    """
    :return: String (ex: flas_501_001_030)
    """
    project_dict = mango.getProjectDict(pm.system.sceneName())
    if not project_dict["isValid"]:
        return ""
    prefix = "_".join((project_dict['show'], project_dict['episode'], project_dict['shot']))
    prefix = prefix.replace("-", "_")
    return prefix


def get_version():
    """
    :return: Integer (ex: 3)
    """
    project_dict = mango.getProjectDict(pm.system.sceneName())
    if not project_dict["isValid"]:
        return None
    return int(project_dict["version"].strip('v'))


def get_task(sg, entity, user):
    """
    :param sg: Shotgun client
    :param entity: Shotgun entity (asset, shot)
    :param user: Shotgun HumanUser
    :return: Shotgun task
    """
    filters = [['task_assignees', 'is', user], ['entity', 'is', entity]]
    return sg.find_one("Task", filters, ["cached_display_name"])


def get_shotgun_client():
    """
    :return: Shotgun client instance
    """
    from shotgun_api3 import Shotgun
    sg = Shotgun("http://shotgunvfx", "3D_publishFiles",
                 "a6bcab2da324036a3963c959c85f739a9440ff287b26cc1e256a16fb3894b05c")
    return sg


def get_shotgun_mango_projects():
    """
    Return a list of all Mango projects listed in Shotgun.

    :return: List
    """
    sg = get_shotgun_client()
    filters = [["archived", "is", False], ["tank_name", "is_not", None]]
    sg_projects = sg.find("Project", filters, ["tank_name"])
    sg_project_names = [k["tank_name"] for k in sg_projects]
    mango_names = mango.getMangoProjects()
    sg_name_set = set(sg_project_names)
    mango_name_set = set(mango_names)
    shotgun_set = mango_name_set.intersection(sg_name_set)
    shotgun_list = list(shotgun_set)
    shotgun_list.sort()
    return shotgun_list


def get_shotgun_project_asset_user(sg, show, asset_id, username, asset_code="Asset"):
    """
    :param sg: a Shotgun client
    :param show: String - show name (ex: "flas", "tita")
    :param asset_id: String - shot name separated by underscores (ex: "flas_421_020_030")
    :param username: String - username (ex: "jhachigian", "shung")
    :param asset_code: String - the Shotgun code for the asset type (ex: "Asset", "CustomNonProjectEntity05")
    :return: a tuple of Shotgun entities if successful or (None, None, None) if failed
    """
    """ get project """
    filters = [["tank_name", "is", show], ['archived', 'is', False]]
    project = sg.find("Project", filters, ["name"])
    """ get shot """
    filters = [["id", "is", asset_id]]
    asset = sg.find(asset_code, filters, ["code"])
    """ get user """
    user = sg.find("HumanUser", [["login", "is", username]], ["name"])
    if not project:
        print "show", show, "not found in Shotgun. This export will not be published to Shotgun."
        return None, None, None
    if not asset:
        print "asset_id", asset_id, "not found in Shotgun. This export will not be published to Shotgun."
        return None, None, None
    if not user:
        print "username", username, "not found in Shotgun. This export will not be published to Shotgun."
        return None, None, None
    return project, asset, user


def get_shotgun_project_shot_user(sg, show, shot_name, username):
    """
    :param sg: a Shotgun client
    :param show: String - show name (ex: "flas", "tita")
    :param shot_name: String - shot name separated by underscores (ex: "flas_421_020_030")
    :param username: String - username (ex: "jhachigian", "shung")
    :return: a tuple of Shotgun entities if successful or (None, None, None) if failed
    """
    """ get project """
    filters = [["tank_name", "is", show], ['archived', 'is', False]]
    project = sg.find("Project", filters, [])
    """ get shot """
    filters = [["code", "is", shot_name]]
    shot = sg.find("Shot", filters, ["code"])
    """ get user """
    user = sg.find("HumanUser", [["login", "is", username]])
    if not project:
        print "show", show, "not found in Shotgun. This export will not be published to Shotgun."
        return None, None, None
    if not shot:
        print "shot", shot_name, "not found in Shotgun. This export will not be published to Shotgun."
        return None, None, None
    if not user:
        print "username", username, "not found in Shotgun. This export will not be published to Shotgun."
        return None, None, None
    return project, shot, user


def get_shotgun_file_publish(sg, path, entity, project, user, publish_file_type, additional_data=None):
    """
    Retrieve (or create) a "PublishedFile" Shotgun entry for the file that fits the publish_file_type and path.

    :param sg: a Shotgun client
    :param path: String - a scene path
    :param entity: a Shotgun Shot entity (shot or asset)
    :param project: a Shotgun Project entity
    :param user: a Shotgun Username entity
    :param publish_file_type: a Shotgun PublishFileType entity
    :param additional_data: dictionary or None
    :return: Shotgun entity - scene file publish
    """
    scene_path = path.replace("\\", "/")
    scene_name = os.path.basename(scene_path)
    filters = [['path_cache', 'is', scene_path],
               ['published_file_type', 'is', publish_file_type],
               ['entity', 'is', entity],
               ['project.Project.archived', "is", False]]
    sg_maya_scene = sg.find_one("PublishedFile", filters, ["code", "description"])
    if not sg_maya_scene:
        """ create an entry for the Maya scene. """
        data = {'published_file_type': {'id': publish_file_type['id'], 'type': 'PublishedFileType'},
                'code': scene_name,
                'entity': entity,
                'path_cache': scene_path,
                'project': project,
                'created_by': user,
                'description': ''
                }
        if scene_name.endswith((".ma", ".mb")):
            data['version_number'] = get_version()
            data['task'] = get_task(sg, entity, user)
        if additional_data is not None:
            for k in additional_data:
                data[k] = additional_data[k]
        sg_maya_scene = sg.create("PublishedFile", data)
    return sg_maya_scene


def get_shotgun_published_file_type(path):
    """
    Return a Shotgun PublishedFileType based on the extension of a given path.

    :param path: String - a path
    :return: Dictionary - a Shotgun published file type
    """
    if path.lower().endswith((".mb", ".ma")):
        """ Maya """
        pf_type = {'id': 17, 'type': 'PublishedFileType'}
    elif path.lower().endswith(".max"):
        """ Max """
        pf_type = {'id': 18, 'type': 'PublishedFileType'}
    else:
        """ Houdini """
        pf_type = {'id': 19, 'type': 'PublishedFileType'}
    return pf_type


def get_shotgun_scene_publish(sg, path, entity, project, user, additional_data=None):
    """
    Retrieve (or create) a "PublishedFile" Shotgun entry for the scene file.

    :param sg: a Shotgun client
    :param path: String - a scene path
    :param entity: a Shotgun Shot entity (shot or asset)
    :param project: a Shotgun Project entity
    :param user: a Shotgun Username entity
    :param additional_data: dictionary or None
    :return: Shotgun entity - scene file publish
    """
    scene_path = path.replace("\\", "/")
    scene_name = os.path.basename(scene_path)
    pf_type = get_shotgun_published_file_type(scene_path)
    filters = [['path_cache', 'is', scene_path],
               ['published_file_type', 'is', pf_type],
               ['entity', 'is', entity],
               ['project.Project.archived', "is", False]]
    sg_maya_scene = sg.find_one("PublishedFile", filters, ["code", "description"])
    if not sg_maya_scene:
        """ create an entry for the Maya scene. """
        data = {'published_file_type': {'id': pf_type['id'], 'type': 'PublishedFileType'},
                'code': scene_name,
                'entity': entity,
                'path_cache': scene_path,
                'project': project,
                'created_by': user,
                'description': '',
                'version_number': get_version()}
        if scene_name.endswith((".ma", ".mb")):
            data['version_number'] = get_version()
            data['task'] = get_task(sg, entity, user)
        if additional_data is not None:
            for k in additional_data:
                data[k] = additional_data[k]
        sg_maya_scene = sg.create("PublishedFile", data)
    return sg_maya_scene


def publish_to_shotgun(sg_dict, scene_path, metadata_dict, username, shot_name):
    """
    :param sg_dict: dictionary for Shotgun publishing
    :param scene_path: a path to the scene file responsible for the exported data.
    :param metadata_dict: dictionary - metadata
    :param username: String - a user's login (ex: "jhachigian", "shung")
    :param shot_name: String - a Shotgun-friendly shot prefix (ex: "flas_421_012_030")
    :return: None
    """
    show = shot_name.split("_")[0]
    '''
    ====================================================================================
        initialize Shotgun
    ====================================================================================
    '''
    sg = get_shotgun_client()
    '''
    ====================================================================================
        get project, shot and user data
    ====================================================================================
    '''
    project, shot, user = get_shotgun_project_shot_user(sg, show, shot_name, username)
    if project is None:  # something failed. Stop immediately.
        return
    '''
    ====================================================================================
        retrieve (or create) a "PublishedFile" Shotgun entry for the Maya scene file
    ====================================================================================
    '''
    sg_maya_scene = get_shotgun_scene_publish(sg, scene_path, shot[0], project[0], user[0])
    '''
    ====================================================================================
        create a "PublishedFile" Shotgun entry for the file
    ====================================================================================
    '''
    data = {k: sg_dict[k] for k in sg_dict}
    """ add Shotgun data to this PublishedFile dictionary """
    data['upstream_published_files'] = [sg_maya_scene]
    data['entity'] = shot[0]
    data['created_by'] = user[0]
    data['project'] = project[0]
    """ update metadata_dict and format it as a JSON string """
    if metadata_dict:
        metadata_dict["mangoProfile"] = mango.get_mango_profile()
        data['sg_meta_data'] = json.dumps(metadata_dict, sort_keys=True)
    """ create the PublishedFile in Shotgun """
    sg.create("PublishedFile", data)


'''
========================================================================
---->  SHOTGUN FUNCTIONS TO GET RIG INFORMATION FOR A SHOT (START) <----
========================================================================
'''


def get_shotgun_asset_dict(sg, asset_id):
    """
    Query Shotgun and return a dictionary containing all rig information for a given asset_id. For example, if given
    the asset_id 797 (aka: "Supergirl S4"), return the following dictionary:

    {'asset_folder': 'chr-supergirl', 'code': 'supergirl', 'project': 'supr',
     'rig_path': 'Z:/data/diablo2/PROJECTS/supr/04_episodes/--assets/chr-supergirl/3d/publish/rigs/rig_supergirl_S4.mb',
     'type': 'chr'}

    :param sg: Shotgun client
    :param asset_id: Integer (ex: 797)
    :return:
    """
    filters = [["id", "is", asset_id]]
    fields = ["code", "sg_project", "sg_asset_type", "sg_asset_code"]
    asset = sg.find_one("CustomNonProjectEntity05", filters, fields)
    filters = [["id", "is", asset["sg_project"][0]["id"]]]
    fields = ["name", "tank_name"]
    project = sg.find_one("Project", filters, fields)
    d = {"type": asset["sg_asset_type"],
         "code": asset["sg_asset_code"],
         "project": project["tank_name"],
         "asset_folder": "{0}-{1}".format(asset["sg_asset_type"], asset["sg_asset_code"])}
    return d


def get_shotgun_rig_dict(sg, asset_id):
    """
    Query Shotgun and return a dictionary containing all rig information for a given asset_id. If the asset has no rig
    information associated with it, search for a parent asset's rig information. If no parent asset exists, return only
    the information that can be had from the original asset.

    For example, if given the asset_id 1535 (aka: "Red Daughter"), return the following dictionary:

    {'asset_folder': 'chr-supergirl', 'code': 'supergirl', 'project': 'supr',
     'rig_paths': ['Z:/data/diablo2/PROJECTS/supr/04_episodes/--assets/chr-supergirl/3d/publish/rigs/rig_supergirl_S4.mb'],
     'type': 'chr'}

    This is the dictionary for parent asset "Supergirl S4", because "Red Daughter" has no rig directly assigned to it.

    :param sg: Shotgun client
    :param asset_id: Integer (ex: 1535)
    :return: Dictionary
    """
    d = get_shotgun_asset_dict(sg, asset_id)
    print d["code"]
    d["rig_paths"] = []
    d["rig_filenames"] = []
    """ look for the Rig associated with the asset_id """
    filters = [["entity.CustomNonProjectEntity05.id", "is", asset_id],
               ["published_file_type.PublishedFileType.code", "is", "Rig"]]
    fields = ["code", "name", "path_cache"]
    rigs = sg.find("PublishedFile", filters, fields)
    if rigs:
        print "Rig found for target asset..."
        d["rig_paths"] = [x["path_cache"] for x in rigs if x["path_cache"] and os.path.exists(x["path_cache"])]
        d["rig_paths"].sort()
        d["rig_filenames"] = [os.path.splitext(os.path.basename(x))[0] for x in d["rig_paths"]]
        d["asset_folder"] = d["rig_paths"][0].split("/")[7]
        return d
    """ if the above failed, look for the Parent Asset """
    filters = [["id", "is", asset_id]]
    fields = ["code", "sg_parent_assets"]
    asset = sg.find_one("CustomNonProjectEntity05", filters, fields)
    if not asset["sg_parent_assets"]:
        print "No parent found for target asset..."
        return d
    """ if a parent asset is found, look for the Rig associated with the parent_id """
    parent_id = asset["sg_parent_assets"][0]["id"]
    filters = [["entity.CustomNonProjectEntity05.id", "is", parent_id],
               ["published_file_type.PublishedFileType.code", "is", "Rig"]]
    fields = ["code", "name", "path_cache"]
    rigs = sg.find("PublishedFile", filters, fields)
    if rigs:
        print "Parent rig found for target asset..."
        d["rig_paths"] = [x["path_cache"] for x in rigs if x["path_cache"] and os.path.exists(x["path_cache"])]
        d["rig_paths"].sort()
        d["rig_filenames"] = [os.path.splitext(os.path.basename(x))[0] for x in d["rig_paths"]]
        d["asset_folder"] = d["rig_paths"][0].split("/")[7]
    print "No parent rig found for target asset..."
    return d


def get_shotgun_rigs_dict(sg, shot_code):
    """
    Query Shotgun and return a dictionary containing all rig information for that shot. For example, a shot_code
    of "supr_410_001_090" would return:

    {'Armored Drone': { 'asset_folder': 'veh-gundrone', 'code': 'gundrone',
                        'project': 'supr', 'rig_path': '', 'type': 'veh'},
     'Red Daughter': {'asset_folder': 'chr-supergirl', 'code': 'supergirl', 'project': 'supr',
                      'rig_paths': ['Z:/data/diablo2/PROJECTS/supr/04_episodes/--assets/chr-supergirl/3d/publish/rigs/rig_supergirl_S4.mb'],
                      'type': 'chr'}}

    :param sg: Shotgun client
    :param shot_code: String (ex: "supr_410_001_090")
    :return: Dictionary
    """
    filters = [["code", "is", shot_code]]
    custom_field = "custom_non_project_entity05_sg_shots_custom_non_project_entity05s"
    fields = ["code", custom_field, "sg_parent_assets"]
    shot = sg.find_one("Shot", filters, fields)
    if shot is None:
        print "Could not find: {0}".format(shot_code)
        return {}
    rig_dict = {x["name"]: get_shotgun_rig_dict(sg, x["id"]) for x in shot[custom_field]}
    return rig_dict

'''
========================================================================
---->  SHOTGUN FUNCTIONS TO GET RIG INFORMATION FOR A SHOT (END) <----
========================================================================
'''
