import sys
import maya.cmds as cmds
path = r"L:\3D\scripts\rigging_dept\exchange"
if path not in sys.path:
    sys.path.insert(0, path)
import rigBox
from rigBox import controlTools as cTools

import sys
import maya.cmds as cmds
path = r"L:\3D\scripts\rigging_dept\exchange"
if path not in sys.path:
    sys.path.insert(0, path)
import rigBox


import sys
p = r"D:\autorig_scripts"
if p not in sys.path:
	sys.path.insert(0, p)
import encAsset.rig.autoRig as AR
reload(AR)
AR.autoRig

def SetInitSceneYup():
    if cmds.upAxis(q=1, ax=1) != 'y':
        cmds.upAxis(ax='y', rv=1)
        cmds.viewLookAt(cmds.modelEditor('modelPanel4', q =1, camera = 1))
    fit_tuner = 'World_tuner'
    if cmds.objExists(fit_tuner):
        if cmds.getAttr(fit_tuner + '.rotateX') == 0:
            cmds.setAttr(fit_tuner + '.rotateX', -90) 

def ReOrientControlShapes():
    exportPath = r"D:\autorig_scripts\encAsset\rig\autoRig\rigfiles\yup"
    importPath= r"D:\autorig_scripts\encAsset\rig\autoRig\rigfiles"
    files = [importPath + '\\' + x for x in os.listdir(importPath) if '.' in x and not 'skeleton' in x]
    wrongShapes = []
    for link in files:
        ctrlFile = cmds.file( link, i=1, rnn=1)
        #ctrls = [x for x in ctrlFile if cmds.nodeType(x) in 'transform']
        ctrls = [x for x in ctrlFile if cmds.listRelatives(x, s=1)]
        #ctrls = [cmds.listRelatives(x, p=1)[0] for x in ctrlFile if cmds.nodeType(x) == 'nurbsCurve']
        saveFile = link.split('\\')[-1]
        savePath= exportPath + '\\' + saveFile
        if ctrls:
            if len(ctrls) == 1:
                for ctrl in ctrls:
                    if not 'stretchIndicator' in ctrl and not 'spineIKFK' in ctrl and not 'eye' in ctrl: 
                        try:
                            rotateCtrlAxis(sel = ctrl, axis = 'Z', angle = -90)
                        except:
                            wrongShapes.append(ctrl)
                cmds.file( savePath, ea=1, f=1, typ = 'mayaBinary', pr=1)
                cmds.delete(ctrl)
            if len(ctrls) > 1:
                roots= set([cmds.listRelatives( j, ap=1, f=1)[0].split('|')[1] for j in ctrls if cmds.listRelatives( j, ap=1, f=1)])
                if roots:
                    for root in roots:
                        print 'ROOT', root
                        if 'stretchIndicator' in root:
                            print 'stretch FILE'
                            cmds.setAttr(root + '.rotateY', 180)
                        if 'spineIKFK' in root:
                            print 'spine FILE'
                            cmds.setAttr(root + '.rotateY', 90)                
                            cmds.setAttr(root+ '.rotateY', 0)
                        if 'eye_Lt_base' or 'eye_Rt_base' in root:
                            print 'eyeBase FILE'
                            cmds.setAttr(root+ '.rotateX', 90)
                        if 'eye_Mid' in root:
                            print 'eye_mid FILE'
                            cmds.setAttr(root+ '.rotateY', 90)
                        cmds.file(savePath, ea=1, f=1, typ = 'mayaBinary', pr=1)
                    [cmds.delete(r) for r in roots]
    if wrongShapes:
        cmds.select(wrongShapes, r=1)
                

def rotateCtrlAxis(sel = None, axis=None, angle = None):
    if sel == None:
        ctrls=cmds.ls(sl=1)
    if sel != None:
        ctrls = [sel]
    if ctrls:
        print ctrls
    for each in ctrls:
        cmds.select(each, r=1)
        pivPos=cmds.xform(each, q=1, rotatePivot=1, r=1, os=1)
        buffers = []
        spans=int(cmds.getAttr(each + ".spans"))
        cmds.select(each + ".cv[*]")
        if axis in 'Xx':
            cmds.rotate(angle, 0, 0, r=1, os=1)
        if axis in 'Yy':
            cmds.rotate(0, angle, 0, r=1, os=1)
        if axis in 'Zz':
            cmds.rotate(0, 0, angle, r=1, os=1)
    cmds.select(ctrls, r=1)

rotateCtrlAxis(sel = s, axis = 'X', angle = -90)