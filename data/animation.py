import maya.mel as mm
import maya.cmds as mc
import os
import commstd
#from rigBot import utils

def change_permission(path):
    """Change permissions on already created files to be readable and writtable by overyone.
    You'll need permissions first of course.

    Args:
        :path: (str) Path to file on disk."""

    if sys.platform == 'win32':
        return

    FILE_PERMISSIONS = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH
    os.chmod(path, FILE_PERMISSIONS)

def write_atom(base_name = "temp",controls = []):
    """
    #base_name = "test"
    #controls =
    Args:
        :base_name: (str) name of the atom file to export, this will be saved in user temp
        :controls: (list) list of the control to export

    """
    mc.select(controls)
    atom_file = os.path.join(mc.internalVar(utd=1), 'animExport_{0}.atom'.format(base_name))

    # save anim clip of current char
    start_frame = int(mc.playbackOptions(min=1, q=1))
    end_frame = int(mc.playbackOptions(max=1, q=1))
    options = 'precision=8;statics=1;baked=1;sdk=0;constraint=0;animLayers=1;'
    options += 'selected=selectedOnly;whichRange=1;range=1:10;hierarchy=none;'
    options += 'controlPoints=0;useChannelBox=1;options=keys;'


    mc.file(atom_file,
                typ="atomExport",

                ch=1,
                force=1,
                options = options,
                es=1)

    #utils.change_permission(atom_file)
    return atom_file

def apply_atom_animation(atom_file, controls, old_namespace, anim_namespace):
    """
    Add animation from atom file back onto a rig

    #Example
    atom_file = write_atom(base_name = "temp", controls=controls)
    anim_namespace ="IronMan_01_NS"
    apply_atom_animation(atom_file, controls, anim_namespace)
    """
    #mc.select(controls)
    mc.select(cl = True)
    missing_controls = []
    for each in controls:
        if mc.objExists(each):
            mc.select(each,add= True)
        else:
            missing_controls.append(each)
    print missing_controls
    
    logger = commstd.get_logger()
    logger.info(old_namespace)
    logger.info(anim_namespace)
    mc.file(atom_file,
                i=1,
                namespace="animExport_temp",
                type="atomImport",
                ra=True,
                options=";;match=string;;selected=selectedOnly;search={0};replace={1};prefix=;suffix=;".format(old_namespace,anim_namespace))


def save_studio_library():

    """
        Saves clips to studio library
        Still WIP
    """
    #Studio Library
    camera_creation = mc.camera(n = "Hip_Camera")
    hip_camera= camera_creation[0]
    hip_camera_shape = camera_creation[1]

    hip_control_w_namespace = mc.ls(full_namespace + ":*hip*CTL")
    hip_control_wo_namespace = mc.ls("*hip*CTL")
    hip_control = hip_control_w_namespace + hip_control_wo_namespace
    hip_control = hip_control[0]
    temp_constraint = mc.parentConstraint(hip_control,hip_camera, mo = False)
    mc.delete(temp_constraint)
    mc.parent (hip_camera ,hip_control)

    mc.setAttr(hip_camera + ".translateZ",50)
    mc.parent(hip_camera, world = True)
    mc.pointConstraint(hip_control,hip_camera, mo=True)

    #set the model panel to be the new camera hide undesirable model panel elements
    mps = mc.getPanel(visiblePanels = True)
    for each in mps:
        if each.find("modelPanel")!=-1:
            mp = each

    mc.modelPanel(mp, e = True, cam = hip_camera_shape )
    #myPanel=str(mc.getPanel(wf=1))
    if mc.getPanel(to=mp) == "modelPanel":

        #mc.modelEditor(mp, e=1, all=0)
        mc.modelEditor(mp, e=1, rendererName="base_OpenGL_Renderer")
        mc.modelEditor(mp, e=1, nurbsCurves=0)
        mc.modelEditor(mp, e=1, locators=0)
        mc.modelEditor(mp, e=1, deformers=0)
        mc.modelEditor(mp, e=1, ikHandles=0)
        mc.modelEditor(mp, e=1, joints=0)

    #get the start and end frames from the scene
    start_frame = int(mc.playbackOptions(min=1, q=1))
    end_frame = int(mc.playbackOptions(max=1, q=1))

    #set the permissions on the folder to allow for read, write, copy

    #make sure the nessesary controls are selected
    #mocapTools.utilities.selectCtrls(anim_namespace+ ":")
    unknown = mc.ls(type = "unknown")
    mc.delete(unknown)

    item = studiolibraryitems.animitem.AnimItem()

    path = os.path.join(dest_folder, action + ".anim")

    item.setDescription(fileX) #this will be from the ingest document
    item.save(objects=controls, path =path, startFrame=start_frame, endFrame=end_frame, fileType = "mayaAscii")

    #create a capture playblast w studio library tool so animators can see the results in a window!
    #create a jpeg sequence folder
    thumbnail_sequence_folder = os.path.join(path, "sequence")

    if not os.path.exists(thumbnail_sequence_folder):
        os.makedirs(thumbnail_sequence_folder)

    #playblast
    full_path_thumbnail_filename = os.path.join(path, "thumbnail.jpg")
    sequence_filename_template = os.path.join(thumbnail_sequence_folder, "thumbnail.jpg")
    mc.select(cl = True)
    mutils.playblast(sequence_filename_template , mp, int(start_frame), int(end_frame), 250, 250, step=1)
    #generate a thumbnail
    generated_frames = os.listdir(thumbnail_sequence_folder)
    generated_frames.sort()
    first_generated_frame = os.path.join(thumbnail_sequence_folder, generated_frames[0])
    shutil.copyfile(first_generated_frame, full_path_thumbnail_filename)



def apply_studio_library(item):
    """
        Loads clips from studio library

        Still WIP
    """
    item.load(namespaces=[namespace])

