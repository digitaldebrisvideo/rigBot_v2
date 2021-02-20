""" 
    This __init__.py is written so that users do NOT have to restart Maya to truly reload _encLib. This way the code
    can be updated without interrupting artists' work.
"""

import os
import camera
import decorators
import deadline
import mango
import shotgun
import util
import pyside_util
import ffmpeg

reload(camera)
reload(decorators)
reload(deadline)
reload(mango)
reload(shotgun)
reload(util)
reload(pyside_util)
reload(ffmpeg)

__all__ = ['camera', 'deadline', 'decorators', 'mango', 'shotgun', 'util']

""" legacy variables """
encPrjRoot = r"Z:\data\diablo2\PROJECTS"
encCacheRoot = r"U:\data\diablo2\PROJECTS"
localRoot = r"C:\data\diablo2\PROJECTS"
encEpiRoot = "04_episodes"

""" empty Maya file for Deadline use """

EMPTY_MAYA_FILE = os.path.join(os.path.dirname(__file__), "empty_maya_scene_file.ma")

""" camera """
get_encore_cameras = camera.get_encore_cameras
get_cameras = camera.get_cameras
is_doom_camera = camera.is_doom_camera
validateCameraSettings = camera.validateCameraSettings
identify_camera = camera.identify_camera
get_camera_name = camera.get_camera_name

""" decorators """
in_root_namespace = decorators.in_root_namespace
restore_selections = decorators.restore_selections
restore_frame_range = decorators.restore_frame_range
viewport_off = decorators.viewport_off
hide_all = decorators.hide_all
switch_to_dg = decorators.switch_to_dg
report_time_to_execute = decorators.report_time_to_execute
apply_wait_cursor = decorators.apply_wait_cursor

""" deadline """
deadline_defaults = deadline.deadline_defaults
get_deadline_temp_folder = deadline.get_deadline_temp_folder
get_deadline_command = deadline.get_deadline_command
show_deadline_message = deadline.show_deadline_message
submit_to_deadline = deadline.submit_to_deadline
prep_temp_folder = deadline.prep_temp_folder
list_to_text_file = deadline.list_to_text_file
save_deadline_job_info = deadline.save_deadline_job_info
save_deadline_plugin_info = deadline.save_deadline_plugin_info

""" mango """
is_mango = mango.is_mango
getProjectDict = mango.getProjectDict
getMangoProjects = mango.getMangoProjects
get_mango_profile = mango.get_mango_profile
sort_episode_list = mango.sort_episode_list
encPrjRoot = mango.encPrjRoot

""" shotgun """
get_shot_prefix = shotgun.get_shot_prefix
get_shotgun_task = shotgun.get_task
get_scene_version = shotgun.get_version
get_shotgun_client = shotgun.get_shotgun_client
get_shotgun_mango_projects = shotgun.get_shotgun_mango_projects
publish_to_shotgun = shotgun.publish_to_shotgun
get_shotgun_rigs_dict = shotgun.get_shotgun_rigs_dict
get_shotgun_project_asset_user = shotgun.get_shotgun_project_asset_user
get_shotgun_scene_publish = shotgun.get_shotgun_scene_publish
get_shotgun_file_publish = shotgun.get_shotgun_file_publish

""" util """
debug = util.debug
save_json_file = util.save_json_file
save_maya_scene_copy = util.save_maya_scene_copy
get_settings = util.get_settings
set_settings = util.set_settings
read_file = util.read_file
has_string = util.has_string
delete_anim = util.delete_anim
openFolder = util.openFolder

""" pyside_util (modified third-party module) """
get_maya_window = pyside_util.get_maya_window
get_pyside_class = pyside_util.get_pyside_class
wrap_instance = pyside_util.wrap_instance


""" ffmpeg """
make_quicktime = ffmpeg.make_quicktime
avi_to_jpeg = ffmpeg.avi_to_jpeg
