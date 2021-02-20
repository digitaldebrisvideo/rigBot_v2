#-------------------------------------------------------------------------------
# Name:        ao_fileTools
# # Purpose:  Set of procedures for working with a files or directories.
#           them to the selected attribute.
# How to use
"""

import sys
p = r"L:\3D\scripts\rigging_dept\riggingPipeline\scripts\utilities"
if p not in sys.path:
	sys.path.insert(0, p)
import ao_fileTools
reload(ao_fileTools)
"""

# Author:      andrei.orehov
#
# Created:     28/06/2019
# Copyright:   (c) andrei.orehov 2018
#
#-------------------------------------------------------------------------------

import maya.cmds as cmds
import os
import webbrowser

def openSysDirectory(mode):
    docs = os.getenv('USERPROFILE')+ '\Documents'
    desk = os.getenv('USERPROFILE')+ '\Desktop'
    temp = os.getenv('TEMP')
    pathList = [docs, desk, temp]
    webbrowser.open(pathList[mode])

def reloadScene():
    curFiles = cmds.file(q=1, sn=1)
    question = cmds.confirmDialog(t = 'Warning', m = 'Would you like to reopen existing opened file?', b =( 'Yes', 'No'), cb= 'No')
    if question == 'Yes':
        cmds.file(curFiles, o=1, f=1)

def getCurrentScenePath():
    files = cmds.file(q=1, sn=1)
    path = '/'.join(files.split('/')[0:-1])
    if path:
        return path

def getDirectory(mode = None, *args):
    """
    
    Use one of the elements from the  list:
    [muscle, skel, fit, skinData, faceTunes, face, body, control]
    
    """
    initPath = '/'.join(cmds.file(q=1, sn=1).split('/')[0:-1])
    mainFilePath = cmds.workspace(q=1, act=1)
    if mode == 'template':
        typeFolder = 'Template'
    if mode == 'simplex':
        typeFolder = 'SimplexData'
    if mode == 'muscle':
        typeFolder = 'Muscles'
    if mode == 'skel':
        typeFolder = 'Skeleton'
    if mode == 'fit':
        typeFolder = 'Fit_Skeleton'
    if mode == 'skinData':
        typeFolder = 'Skin_data'
    if mode == 'faceTunes':
        typeFolder = 'FaceTuners'
    if mode == 'face':
        typeFolder=  'Wrapped'
    if mode == 'body':
        typeFolder=  'WrappedBody'
    if mode == 'control':
        typeFolder = 'Controls'
    if mode == None:
        typeFolder = ''
    if 'Z:/data' in  mainFilePath and mode != None:
        print 'old pipeline structure,  folder name input'
        path = mainFilePath.split('3d')[0]
        folder = '3d/publish/rigs/'+ typeFolder
        dest = path + folder
    if 'Z:/projects' in  mainFilePath and mode != None:
        print 'new pipeline structure, folder name input'
        path = mainFilePath.split('/rig/')[0]  + '/rig'
        folder = '/' + typeFolder
        dest = path + folder
    if not 'Z:/data' in mainFilePath and not 'Z:/projects' in  mainFilePath and mode != None:
        print 'out of any pipeline,  folder name input'
        path = [[]]
        #path = cmds.fileDialog2(fm=3, dir = initPath, okc='Select Folder')
        if path:
            dest = path[0]
    if not 'Z:/data' in mainFilePath and not 'Z:/projects' in  mainFilePath and mode == None:
        print 'out of any pipeline, no folder name input'
        path = cmds.fileDialog2(fm=3, dir = initPath, okc='Select Folder')
        if path:
            dest = path[0]
    if 'Z:/projects' in  mainFilePath and mode == None or 'Z:/data' in  mainFilePath and mode == None:
        print 'in pipeline, no folder name input'
        path = cmds.fileDialog2( dir= mainFilePath, fm=3, okc='Select Folder')
        if path:
            dest = path[0]
    if path:
        destination = dest
        return destination
        print destination

def  createCustomWorkingDirectory(folder = None,*args):
    if folder ==  None:
        fold = raw_input('Enter name of the folder')
    if folder != None:
        fold =  folder
    #Define default extension for the files
    basicFilter = '*.mb'
    #Get workspace path
    filePath = cmds.workspace(q=1, act=1)
    if 'Z:/data' in  filePath:
        path = filePath.split('3d')[0]
        #Define default folder for file
        folder = '3d/publish/rigs/' +  fold
    if 'Z:/projects' in  filePath:
        path = filePath.split('/rig/')[0]  + '/rig'
        folder = '/'+  fold
    #Generate string for path
    saver = path + folder
    if not os.path.isdir(saver):
        cmds.sysFile(saver, md=1)
    return saver

def openCurrentFileFolder():
    link = cmds.file(q=1, sn=1)
    if link:
        folder = '/'.join(link.split('/')[0:-1])
        if folder:
            webbrowser.open(folder)
def getAssetFolder(*args):
    link = cmds.file(q=1, sn=1)
    if link:
        folder = '/'.join(link.split('/')[0:-1])
        if 'wip' in folder:
            rigFolder = folder.split('rig')[0]
            publishFolder = rigFolder.replace('wip', 'publish')
        if 'data' in folder:
            rigFolder = folder.split('3d')[0]
            publishFolder =  rigFolder + '/3d/publish/rigs'
    if publishFolder:
        return (publishFolder)
def openAssetFolder():
    link = getAssetFolder()
    if link:
        folder = '/'.join(link.split('/')[0:-1])
        if 'wip' in folder:
            rigFolder = folder.split('rig')[0]
            publishFolder = rigFolder.replace('wip', 'publish')
            webbrowser.open(publishFolder)
        if 'data' in folder:
            rigFolder = folder.split('3d')[0]
            publishFolder =  rigFolder + '/3d/publish/rigs'
            webbrowser.open(publishFolder)

