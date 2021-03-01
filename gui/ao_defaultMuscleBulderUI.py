################ Run the script #########################

'''
*********************************************************
import sys
p = r"Y:\Artists\Riggers\Scripts\riggingTools"
if p not in sys.path:
	sys.path.insert(0, p)
import ao_defaultMuscleBulder
reload(ao_defaultMuscleBulder)
ao_defaultMuscleBulder.defaulMuscleUI()
*********************************************************

'''
#########################################################
# import sys
# r = r"C:\Users\Nicob\Documents\ENCORE\aoutils\riggingTools"
# u = r"C:\Users\Nicob\Documents\ENCORE\skinningTools"
# paths = [r, u]
# for link in paths:
#     if link not in sys.path:
#         sys.path.insert(0, link)


import maya.cmds as cmds
import os
from functools import partial
from rigBot import ao_fileTools
reload(ao_fileTools)

upScene= cmds.upAxis(q=1, ax=1)
from rigBot import ao_breathSystem as breathSys
reload(breathSys)

def DelBreath(*args):
    breathSys.deleteAllBreath()
    
def CreateBreath(*args):
    breathSys.makeBreath()

def getSelectedElements(*args):
    initJnts = cmds.ls(os=1, tr=1)
    if initJnts:
        print initJnts
        return initJnts
    else:
        return None



def makeNubsDriver4(initJnts = None, *args):
    if initJnts == None:
        initJnts = getSelectedElements()
    if len(initJnts) == 4:
        cmds.promptDialog(t = 'Informatoion', m = 'Enter name of the system')
        name = cmds.promptDialog(q=1, tx=1)
        cmds.select(cl=1)
        upperSet = [initJnts[0], initJnts[1]]
        lowerSet = [initJnts[2], initJnts[3]]
        posUp = [cmds.xform(objUp, q=True, ws=True, translation=True) for objUp in upperSet]
        posLow = [cmds.xform(objLow, q=True, ws=True, translation=True) for objLow in lowerSet]
        UpCurve = cmds.curve(d=1, p=posUp, n = name + '_UpCrv')
        LowCurve = cmds.curve(d=1, p=posLow, n = name + '_LowCrv')
        nrb = cmds.loft( UpCurve, LowCurve, d=1, ch=0, u=1, n = name + '_nrb')
        nrbShape = cmds.listRelatives( nrb, s=1, ni=1)[0]
        cmds.rebuildSurface( nrb[0], ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kc=0, su=0, du=1, sv=0, dv=1, tol = 0.01, fr=0, dir =2)
        skin = cmds.skinCluster(nrb, upperSet, lowerSet , tsb=1)
        foly = cmds.createNode('follicle', n= name + '_fol')
        fol_top = cmds.listRelatives(foly, p=1)
        cmds.connectAttr(nrbShape + '.worldSpace', (foly + '.inputSurface'))
        cmds.connectAttr(nrbShape + '.worldMatrix', (foly + '.inputWorldMatrix'))
        cmds.connectAttr((foly + '.outTranslate'), (fol_top[0] + '.translate'))
        cmds.connectAttr((foly + '.outRotate'), (fol_top[0] + '.rotate'))
        cmds.setAttr((foly + '.parameterU'), 0.5)
        cmds.setAttr((foly + '.parameterV'), 0.5)
        fol_top = cmds.rename(fol_top, foly + '_fol_tr')
        cmds.select(cl=1)
        infJnt = cmds.joint(n = name + '_bind', p = cmds.xform(fol_top, q=1, ws=1, t=1), rad=3)
        cmds.parentConstraint(fol_top, infJnt, mo=1)
        cmds.delete(UpCurve, LowCurve)
    else:
        cmds.warning('You need to select 4 joints before start the script!')

def buildArmpitMuscles(*args):
    if not cmds.objExists('armpit*'):
        sides = ['_Lt_', '_Rt_']
        fol_grp = 'musclefollicleGroup'
        musRig_grp = 'muscle_rig'
        ancorLoc_grp = 'ancorLocs_grp'
        musCtrl_grp = 'muscle_controls_grp'
        musJoints_grp = 'muscle_jnts_grp'
        groups = [fol_grp, musRig_grp, ancorLoc_grp, musCtrl_grp, musJoints_grp]
        for initGrp in groups:
            if not cmds.objExists(initGrp):
                cmds.createNode('transform', n = initGrp)
                cmds.addAttr(initGrp, ln = "nodetype",  dt ="string", k=0)
                cmds.setAttr( initGrp + '.nodetype', "muscleNode", type = 'string')
        if not cmds.listRelatives(musRig_grp, p=1):
            cmds.parent(musRig_grp, 'tech_grp', a=1)
        if not cmds.listRelatives(musCtrl_grp, p=1):
            cmds.parent(musCtrl_grp, 'world_CTL', a=1)
        if not cmds.listRelatives(musJoints_grp, p=1):
            cmds.parent(musJoints_grp, 'skeleton_grp', a=1)
        if not cmds.listRelatives(ancorLoc_grp, p=1):
            cmds.parent(ancorLoc_grp, musRig_grp, a=1)
        if not cmds.listRelatives(fol_grp, p=1):
            cmds.parent(fol_grp, musRig_grp, a=1)
        folGrp = 'armpit_follices_grp'
        if not cmds.objExists(folGrp):
            cmds.createNode('transform', n = folGrp)
        initJnts = ['uprArmRibbon01', 'uprArmRibbon03', 'clavicle']
        for side in sides:
            cmds.select(cl=1)
            armpitJnt = cmds.joint( n = 'armpit' + side + 'jnt', p = cmds.xform('torso' + side + 'bind', q=1, ws=1, t=1), rad = 3)
            cmds.parent(armpitJnt, musJoints_grp, a=1)
            snap = cmds.pointConstraint('clavicle' + side + 'bind', 'torso' + side + 'bind', armpitJnt, mo=1)
            upperSet = [initJnts[0] + side + 'bind', initJnts[1] + side + 'bind']
            lowerSet = [initJnts[2] + side + 'bind', armpitJnt]
            posUp = [cmds.xform(objUp, q=True, ws=True, translation=True) for objUp in upperSet]
            posLow = [cmds.xform(objLow, q=True, ws=True, translation=True) for objLow in lowerSet]
            UpCurve = cmds.curve(d=1, p=posUp, n = 'armpit' + side + 'UpCrv')
            LowCurve = cmds.curve(d=1, p=posLow, n = 'armpit' + side + 'LowCrv')
            nrb = cmds.loft( UpCurve, LowCurve, d=1, ch=0, u=1, n = 'armpit' + side + 'nrb')
            nrbShape = cmds.listRelatives( nrb, s=1, ni=1)[0]
            cmds.rebuildSurface( nrb[0], ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kc=0, su=0, du=1, sv=0, dv=1, tol = 0.01, fr=0, dir =2)
            skin = cmds.skinCluster(nrb, upperSet, lowerSet , tsb=1)
            foly = cmds.createNode('follicle', n= 'armpit' + side + 'fol')
            fol_top = cmds.listRelatives(foly, p=1)
            cmds.connectAttr(nrbShape + '.worldSpace', (foly + '.inputSurface'))
            cmds.connectAttr(nrbShape + '.worldMatrix', (foly + '.inputWorldMatrix'))
            cmds.connectAttr((foly + '.outTranslate'), (fol_top[0] + '.translate'))
            cmds.connectAttr((foly + '.outRotate'), (fol_top[0] + '.rotate'))
            cmds.setAttr((foly + '.parameterU'), 0.5)
            cmds.setAttr((foly + '.parameterV'), 0.75)
            cmds.parent(fol_top, folGrp)
            fol_top = cmds.rename(fol_top, foly + '_fol_tr')
            cmds.select(cl=1)
            infJnt = cmds.joint(n = 'armpit' + side + 'bind', p = cmds.xform(fol_top, q=1, ws=1, t=1), rad=3)
            cmds.parent(infJnt, musJoints_grp, a=1)
            snapOrient = cmds.orientConstraint(upperSet[0], infJnt, mo=0)
            cmds.delete(snapOrient)
            cmds.parentConstraint(fol_top, infJnt, mo=1)
            cmds.parent(nrb, UpCurve,LowCurve, musRig_grp, a=1)
        cmds.parent(folGrp, fol_grp, a=1)
    else:
        exist = cmds.ls('armpit*', tr=1)
        cmds.select(exist, r=1)
        print exist
        cmds.confirmDialog(t = 'Information', m = "This rig has armpit!", b = 'Ok')

def colorizeMuscleControls(*args):
    controlShapes = [x for x in cmds.ls(cmds.listRelatives('muscle_controls_grp', ad=1), type = 'nurbsCurve')]
    for ctrl in controlShapes:
        cmds.setAttr(ctrl +'.overrideEnabled', True)
        cmds.setAttr(ctrl+'.overrideRGBColors', 1)
        if 'Lt' in ctrl:
            cmds.setAttr(ctrl+'.overrideColorRGB', 0.3,0.3,1)
        if 'Rt' in ctrl:
            cmds.setAttr(ctrl+'.overrideColorRGB', 1,0.3,0.3)
    #cmds.confirmDialog(t = 'Information', m = 'Controls are colorized!')
def updatePecs(*args):
    grps = ['pecs_Lt_end_cl_locGrpOffset', 'pecs_Rt_end_cl_locGrpOffset', 'pecs_Lt_end_cl_ctrlGrpOffset', 'pecs_Rt_end_cl_ctrlGrpOffset']
    sides = ['Lt', 'Rt']
    for grp in grps:
        if cmds.objExists(grp):
            if 'Lt' in grp:
                cons = cmds.ls(cmds.listHistory(grp, lv=2), type = 'constraint')
                if cons:
                	cmds.delete(cons)
                pcon = cmds.pointConstraint('uprArmRibbon02_Lt_bind', grp, mo=1)
                ocon = cmds.orientConstraint('chest_Mid_bind', grp, mo=1)
            if 'Rt' in grp:
                cons = cmds.ls(cmds.listHistory(grp, lv=2), type = 'constraint')
                if cons:
                	cmds.delete(cons)
                pcon = cmds.pointConstraint('uprArmRibbon02_Rt_bind', grp, mo=1)
                ocon = cmds.orientConstraint('chest_Mid_bind', grp, mo=1)
            cmds.setAttr(ocon[0] + '.interpType', 2)

def snapUpperPecs(*args):
    initLocs = [cmds.listRelatives(x, p=1)[0] for x in cmds.ls('upperPecs*') if cmds.listRelatives(x, s=1) and cmds.nodeType(cmds.listRelatives(x, s=1)[0]) in 'locator']
    for loc in initLocs:
        if 'Lt' in loc and 'start' in loc:
            snap = cmds.pointConstraint('clavicle_Lt_bind', 'clavicleEnd_Lt_jnt', loc, mo=0)
        if 'Lt' in loc and 'end' in loc:
            snap = cmds.pointConstraint('uprArmRibbon02_Lt_bind', 'uprArmRibbon03_Lt_bind', loc, mo=0)
        if 'Rt' in loc and 'start' in loc:
            snap = cmds.pointConstraint('clavicle_Rt_bind', 'clavicleEnd_Rt_jnt', loc, mo=0)
        if 'Rt' in loc and 'end' in loc:
            snap = cmds.pointConstraint('uprArmRibbon02_Rt_bind', 'uprArmRibbon03_Rt_bind', loc, mo=0)


def buildMuscle(mod, *args):
    sides = ['Lt', 'Rt']
    if mod == 0:
        for side in sides:
            if not cmds.objExists('kneeFix_' + side + '*'):
                buildNurbMuscleSystem('uprLegRibbon04_' + side + '_bind' ,'lwrLegRibbon02_' + side + '_bind', 'kneeFix_' + side, 1, (1,0,0), (1,0,0))
                attachMuscleToControlSet()
            else:
                pass
                exist = cmds.ls('*kneeFix*', tr=1)
                cmds.select(exist, r=1)
                print exist

    if mod == 1:
        for side in sides:
            if not cmds.objExists('*pecs_' + side + '*'):
                if upScene == 'z':
                    buildNurbMuscleSystem('pectorals_' + side + '_jnt' ,'uprArmRibbon02_' + side + '_bind', 'pecs_' + side, 2, (0,1,0), (0,0,1))
                if upScene == 'y':
                    buildNurbMuscleSystem('pectorals_' + side + '_jnt' ,'uprArmRibbon02_' + side + '_bind', 'pecs_' + side, 2, (0,0,1), (0,0,1))
                attachMuscleToControlSet()

            else:
                pass
                exist = cmds.ls('*pecs*', tr=1)
                cmds.select(exist, r=1)
                print exist
        updatePecs()


    if mod == 2:
        if upScene == 'z':
            hipPos = cmds.xform('hips_Mid_jnt', q=1, ws=1, t=1)[2]
        if upScene == 'y':
            hipPos = cmds.xform('hips_Mid_jnt', q=1, ws=1, t=1)[1]
        for side in sides:
            if not cmds.objExists('hipFix_' + side + '*'):
                ancorLoc = cmds.spaceLocator(n = 'hip_' + side + '_AncorLoc')
                axises = ['X', 'Y', 'Z']
                for a in axises:
                    cmds.setAttr(cmds.listRelatives(ancorLoc, s=1)[0] + '.localScale' + a, 3)
                ancorLoc_grp = 'ancorLocs_grp'
                if not cmds.objExists(ancorLoc_grp):
                    cmds.createNode('transform', n = ancorLoc_grp)
                cmds.parent(ancorLoc, ancorLoc_grp, a=1)
                snap = cmds.pointConstraint('uprLegRibbon02_' + side + '_bind', ancorLoc, mo=0)
                cmds.delete(snap)
                posAncor= cmds.xform(ancorLoc, q=1, ws=1, t=1)
                if upScene == 'z':
                    cmds.xform(ancorLoc, ws=1, t = (posAncor[0], posAncor[1], hipPos))
                if upScene == 'y':
                    cmds.xform(ancorLoc, ws=1, t = (posAncor[0], hipPos, posAncor[2]))
                cmds.parentConstraint('hips_Mid_jnt', ancorLoc[0], mo=1 )
                start_end_grp = buildNurbMuscleSystem(ancorLoc[0], 'uprLegRibbon02_' + side + '_bind', 'hipFix_' + side, 1, (1,0,0), (1,0,0))
                attachMuscleToControlSet()
                if upScene == 'y':
                    for g in start_end_grp:
                        cmds.setAttr(g + '.rx', 90)
            else:
                exist = cmds.ls('*hipFix_*', tr=1)
                cmds.select(exist, r=1)
                print exist
                pass
    if mod == 3:
        for side in sides:
            if not cmds.objExists('deltoid_' + side + '*'):
                buildNurbMuscleSystem('trapezius_' + side + '_offsetGrp' ,'uprArmRibbon02_' + side + '_bind', 'deltoid_' + side, 1, (1,0,0), (0,0,1))
                attachMuscleToControlSet()
            else:
                exist = cmds.ls('*deltoid*', tr=1)
                cmds.select(exist, r=1)
                print exist
                pass
            if not cmds.objExists('upperPecs_' + side + '*'):
                buildNurbMuscleSystem('clavicle_' + side + '_bind' ,'uprArmRibbon03_' + side + '_bind', 'upperPecs_' + side, 1, (0,1,0), (0,0,1))
                attachMuscleToControlSet()
                
            else:
                exist = cmds.ls('*upperPecs*', tr=1)
                cmds.select(exist, r=1)
                print exist
                pass

    if mod == 4:
        for side in sides:
            if not cmds.objExists('upperPecs_' + side + '*'):
                buildNurbMuscleSystem('clavicle_' + side + '_bind' ,'uprArmRibbon03_' + side + '_bind', 'upperPecs_' + side, 1, (0,1,0), (0,0,1))
                attachMuscleToControlSet()
                
            else:
                exist = cmds.ls('*upperPecs*', tr=1)
                cmds.select(exist, r=1)
                print exist
                pass

    colorizeMuscleControls()
    makeTrueMirrorMuscleControls(1,1)



def updateDeltoid(*args):
    nodes = ['deltoid_Rt_start_cl_locGrpOffset', 'deltoid_Lt_start_cl_locGrpOffset', 'deltoid_Lt_start_cl_ctrlGrpOffset', 'deltoid_Rt_start_cl_ctrlGrpOffset']
    updated = []
    for node in nodes:
        if cmds.objExists(node):
            cons = cmds.listRelatives(node, type = 'constraint')
            if cmds.nodeType(cons[0]) in 'parentConstraint':
                targets = cmds.parentConstraint(cons[0], q=1 ,tl=1)
                for target in targets:
                    if 'bind' in target:
                        cmds.delete(cons[0])
                        parcon = cmds.parentConstraint(target.replace('bind', 'offsetGrp'), node, mo=1)
                        updated.append(node)
    if updated:
        cmds.confirmDialog(t = 'Information', m = 'Deltoid updated!')
    if not updated:
        cmds.confirmDialog(t = 'Information', m = 'Deltoid is correct!')

def buildNurbMuscleSystem(startJnt, endJnt, nameMus, numJnts, axisNrb, axisCtrl, *args):
    sel = [startJnt, endJnt]
    name = nameMus
    number = numJnts
    cmds.select(sel, r=1)
    fol_grp = 'musclefollicleGroup'
    musRig_grp = 'muscle_rig'
    ancorLoc_grp = 'ancorLocs_grp'
    musCtrl_grp = 'muscle_controls_grp'
    musJoints_grp = 'muscle_jnts_grp'
    groups = [fol_grp, musRig_grp, ancorLoc_grp, musCtrl_grp, musJoints_grp]
    for initGrp in groups:
        if not cmds.objExists(initGrp):
            cmds.createNode('transform', n = initGrp)
            cmds.addAttr(initGrp, ln = "nodetype",  dt ="string", k=0)
            cmds.setAttr( initGrp + '.nodetype', "muscleNode", type = 'string')
    if not cmds.listRelatives(musRig_grp, p=1):
        cmds.parent(musRig_grp, 'tech_grp', a=1)
    if not cmds.listRelatives(musCtrl_grp, p=1):
        cmds.parent(musCtrl_grp, 'world_CTL', a=1)
    if not cmds.listRelatives(musJoints_grp, p=1):
        cmds.parent(musJoints_grp, 'skeleton_grp', a=1)
    if not cmds.listRelatives(ancorLoc_grp, p=1):
        cmds.parent(ancorLoc_grp, musRig_grp, a=1)
    if not cmds.listRelatives(fol_grp, p=1):
        cmds.parent(fol_grp, musRig_grp, a=1)
    jnt_grp = cmds.createNode('transform', n = name + '_jnt_grp')
    clusters_grp = cmds.createNode('transform', n = name + '_clusters_grp')
    ctrl_grp = cmds.createNode('transform', n = name + '_ctrl_grp')
    nurb = cmds.nurbsPlane(n = name, ch=1, o =1, ax = axisNrb, w=10 , lr=0.2, d=1)
    geo_shape = cmds.listRelatives(nurb[0], s=1)
    cmds.select(nurb[0] + '.cv[0][0]', r=1)
    cmds.select(nurb[0] + '.cv[0][1]', add=1)
    start = cmds.cluster(n = nurb[0] + '_start_cl')
    start_ctrl = cmds.spaceLocator(n = start[0] + '_loc')
    startLocShape = cmds.listRelatives(start_ctrl, s=1)
    start_grp = cmds.group(start_ctrl[0], n = start_ctrl[0] + 'Grp')
    start_off = cmds.group(start_grp, n = start_grp + 'Offset')
    pos_s = cmds.pointConstraint(start[1], start_off)
    cmds.delete(pos_s)
    cmds.parentConstraint(start_ctrl[0], start[1])
    cmds.select(nurb[0] + '.cv[1][0]', r=1)
    cmds.select(nurb[0] + '.cv[1][1]', add=1)
    end = cmds.cluster(n = nurb[0] + '_end_cl')
    end_ctrl = cmds.spaceLocator(n = end[0] + '_loc')
    endLocShape = cmds.listRelatives(end_ctrl, s=1)
    end_grp = cmds.group(end_ctrl[0], n = end_ctrl[0] + 'Grp')
    end_off = cmds.group(end_grp, n = end_grp + 'Offset')
    pos_e = cmds.pointConstraint(end[1], end_off)
    cmds.delete(pos_e)
    axises = ['X', 'Y', 'Z']
    for a in axises:
        cmds.setAttr(startLocShape[0] + '.localScale' + a, 3)
        cmds.setAttr(endLocShape[0] + '.localScale' + a, 3)
    cmds.parentConstraint(end_ctrl[0], end[1])
    for i in range(1, (number+1)):
        cmds.select(cl=1)
        if number ==1:
            jnt  = cmds.joint(n = name  + '_bind')
        if number ==2:
            if 'Lt' in name:
                jnt  = cmds.joint(n = name.split('_Lt')[0] + '_'+ str(i) + '_Lt' + '_bind')
            if 'Rt' in name:
                jnt  = cmds.joint(n = name.split('_Rt')[0] + '_'+ str(i) + '_Rt' + '_bind')
        fol = jnt.replace('bind', 'fol')
        foly = cmds.createNode('follicle', n= fol )
        fol_top = cmds.listRelatives(foly, p=1)
        fol_top[0] = cmds.rename(fol_top, foly + '_Handle')
        cmds.connectAttr(geo_shape[0] + '.worldSpace', (foly + '.inputSurface'))
        cmds.connectAttr(geo_shape[0] + '.worldMatrix', (foly + '.inputWorldMatrix'))
        cmds.connectAttr((foly + '.outTranslate'), (fol_top[0] + '.translate'))
        cmds.connectAttr((foly + '.outRotate'), (fol_top[0] + '.rotate'))
        cmds.setAttr((foly + '.parameterU'), (1.0/(number+1)) * i)
        cmds.setAttr((foly + '.parameterV'), 0.5)
        par_con = cmds.parentConstraint(fol_top, jnt)
        cmds.parent(fol_top, fol_grp)
        cmds.parent(jnt, jnt_grp)
        cmds.delete(par_con)
        ctrl = cmds.circle( n = jnt.replace('bind', 'anim'), d=1, r=4, nr = axisCtrl, s=6)[0]
        grp = cmds.group(ctrl, n = ctrl.replace('anim', 'ctrl') + 'Grp')
        grpOffset = cmds.group(grp, n = grp + 'Offset')
        snap = cmds.parentConstraint(jnt, grpOffset)
        cmds.delete(snap)
        cmds.parentConstraint(ctrl, jnt, mo=1)
        cmds.connectAttr(ctrl + '.sx', jnt + '.sx')
        cmds.connectAttr(ctrl + '.sy', jnt + '.sy')
        cmds.connectAttr(ctrl + '.sz', jnt + '.sz')
        cmds.parent(grpOffset, ctrl_grp, a=1)
        cmds.parentConstraint(fol_top, grpOffset, mo=1)
        cmds.select(cl=1)
    #snap to pos
    start_snap = cmds.pointConstraint(sel[0], start_off)
    end_snap = cmds.pointConstraint(sel[1], end_off)
    cmds.delete(start_snap, end_snap)
    #parent groups
    cmds.scaleConstraint('world_CTL', clusters_grp, mo=1)
    cmds.parent(start[1], end[1], clusters_grp, a=1)
    cmds.parent(nurb[0], clusters_grp, musRig_grp, a=1)
    cmds.parent(ctrl_grp, musCtrl_grp)
    cmds.parent(start_off, end_off, ancorLoc_grp, a=1)
    cmds.parent(jnt_grp, musJoints_grp, a=1)
    cmds.parentConstraint(sel[0], start_off, mo=1)
    cmds.parentConstraint(sel[1], end_off, mo=1)
    return start_grp, end_grp


def attachMuscleToControlSet(*args):
    allMuscleControls = cmds.listRelatives('muscle_controls_grp', ad=1)
    mus_ctrls =  [x for x in allMuscleControls if '_anim' in x and cmds.nodeType(x) == 'transform']
    if not cmds.objExists('all_ctrls'):
        cmds.select(cl=1)
        cmds.sets(n = 'all_ctrls')
    for ctr in mus_ctrls:
        cmds.sets(ctr, fe= 'all_ctrls')




def makeAllMusclesDoIt(*args):
    buildMuscle(0)
    buildMuscle(1)
    buildMuscle(2)
    buildMuscle(3)
    buildMuscle(4)
    buildArmpitMuscles()
    fixMuscleScale()
    cmds.select(cl=1)

def selectAllMuscles(mode, *args):
    muscleList = ['deltoid', 'pecs', 'hipFix', 'kneeFix', 'armpit', 'upperPecs']
    toSel = []
    modifer = cmds.getModifiers()
    for item in muscleList:
        if mode ==0:
            jnts = cmds.ls(item + '*', type = 'joint')
        if mode ==1:
            typ = ''
            jnts = [cmds.listRelatives(x, p=1)[0] for x  in cmds.ls(item + '*', type = 'nurbsCurve')]
        if jnts:
            for jnt in jnts:
                if cmds.objExists(jnt):
                    toSel.append(jnt)
    if toSel:
        if modifer == 0:
            cmds.select(toSel, r=1)
        if modifer == 1:
            cmds.select(toSel, add=1)
        if modifer == 8:
            cmds.select(toSel, d=1)


def selectMuscles(musTyp, mode, *args):
    modifer = cmds.getModifiers()
    if mode ==0:
        typ = 'bind'
    if mode ==1:
        typ = 'anim'
    sel = cmds.ls(musTyp + '*' + typ)
    if sel:
        if modifer == 0:
            cmds.select(sel, r=1)
        if modifer == 1:
            cmds.select(sel, add=1)
        if modifer == 8:
            cmds.select(sel, d=1)

def deleteAllMuscles(*args):
    musNodes = [x for x in cmds.ls(tr =1) if 'nodetype' in cmds.listAttr(x) and cmds.getAttr(x + '.nodetype') in  'muscleNode']
    if musNodes:
        mess = cmds.confirmDialog( t = 'Warning!', m = 'Do you want to delete all muscles from the rig?', b = ['Yes', 'No'], db = 'No', cb = 'No', bgc = (0.7, 0, 0))
        if mess == 'Yes':
            cmds.delete(musNodes)
        else:
            pass
    else:
        cmds.confirmDialog(t = 'Information', m = "This rig doesn't have any muscles!", b = 'Ok')

def fixMuscleScale(*args):
    cluster_grp =[ x for x in cmds.listRelatives('muscle_rig', c=1) if 'clusters_grp' in x]
    if cluster_grp:
        for cl_grp in cluster_grp:
            scaleConst = cmds.ls(cmds.listHistory(cl_grp, lv=20), type= 'scaleConstraint')
            if not scaleConst:
                world='world_CTL'
                if not mc.objExists ('world_CTL'):
                    world='world_CTL'
                if mc.objExists (world):
                    cmds.scaleConstraint('world_CTL', cl_grp, mo=1)
            else:
                pass

def collapseCmd(*args):
    if cmds.frameLayout('advMus', q=1, cl=1):
        print  cmds.frameLayout('advMus', q=1, cl=1)
        cmds.window('DefaulMusclesTools', e=1, h=185)
    if not cmds.frameLayout('advMus', q=1, cl=1):
        print  cmds.frameLayout('advMus', q=1, cl=1)
        cmds.window( 'DefaulMusclesTools', e=1, h=210)


def ExportMuscles(*args):
    follicles = [x for x in cmds.listRelatives('musclefollicleGroup', ad=1) if cmds.nodeType(x) in 'follicle']
    initMuscleLocs = [x for x in cmds.listRelatives( 'ancorLocs_grp', ad=1, type = 'transform') if cmds.listRelatives(x, s=1) and cmds.nodeType(cmds.listRelatives(x, s=1)[0]) in 'locator' and not 'AncorLoc' in x]
    toExport = [y for y in initMuscleLocs if cmds.objExists(y)]
    muscleLocGrp = [x + 'GrpOffset' for x in toExport]
    if toExport:
        basicFilter = "*.muscle"
        #path = cmds.workspace(q=1, act=1)
        #folder = 'publish/rigs/Muscles'
        #links = path.split('workarea')
        saver = ao_fileTools.getDirectory('muscle')
        print saver
        if not os.path.isdir(saver):
            cmds.sysFile(saver, md = 1)
        filepath = cmds.fileDialog2(cap = 'Export Muscles', dir = saver , ff = basicFilter)
        if filepath:
            file = open(filepath[0], 'w')
            sel = toExport
            for obj in sel:
                t = cmds.xform(obj, q=1, t=1, ws=1)
                r = cmds.xform(obj, q=1, ro=1, ws=1)
                file.write(obj + '@' + str(t) + '@' + str(r) + '\n')
            if follicles:
                for fol in follicles:
                    pU = cmds.getAttr(fol + '.parameterU')
                    pV = cmds.getAttr(fol + '.parameterV')
                    file.write('$' + fol + '$' + str(pU) + '$' + str(pV) + '\n')
            file.close()
            cmds.confirmDialog(t = 'Information', m = str(len(toExport)/2) + ' Muscles were exported!')
        print '########################################################\n'
        for each in toExport:
            print each
        print '########################################################\n'
def ImportMuscles(*args):
    basicFilter = "*.muscle"
    path = cmds.workspace(q=1, act=1)
    #folder = 'publish/rigs/Muscles'
    #links = path.split('workarea')
    reader = ao_fileTools.getDirectory('muscle')
    if os.path.isdir(reader):
        filepath = cmds.fileDialog2(cap = 'Load Muscles', dir = reader, fileMode=1, ff = basicFilter)
        ctrls = []
        if filepath:
            file = open(filepath[0], 'r')
            lines = file.readlines()
            for line in lines:
                if '$' not in line:
                    ctrl = line.split('@')[0]
                    tr = line.split('@')[1].strip('][').split(',')
                    ro = line.split('@')[2].split('\n')[0].strip('][').split(',')
                    if cmds.objExists(ctrl):
                        ctrls.append(ctrl)
                        cmds.xform(ctrl, t=(float(tr[0]), float(tr[1]), float(tr[2])), ws=1)
                        cmds.xform(ctrl, ro=(float(ro[0]), float(ro[1]), float(ro[2])), ws=1)
                if '$' in line:
                    fol = line.split('$')[1]
                    pU = line.split('$')[2]
                    pV = line.split('$')[3].split('\n')[0]
                    if cmds.objExists(fol):
                        cmds.setAttr(fol + '.parameterU', float(pU))
                        cmds.setAttr(fol + '.parameterV', float(pV))
            file.close()
            cmds.confirmDialog(t = 'Information', m = str(len(ctrls)/2) + ' muscle locators were imported!')
            print '########################################################\n'
            for c in ctrls:
                print c
            print '########################################################\n'
    if not os.path.isdir(reader):
        cmds.confirmDialog(t = 'Warning', m = "Current asset doesn't have Exported Muscles!")
        

def mirrorControlShapes(*args):
    import ao_EncoreRiggingTools
    reload(ao_EncoreRiggingTools)
    ao_EncoreRiggingTools.mirrorShapeControls(0)



def makeTrueMirrorMuscleControls(type = None, h= None, *args):
    hidden = int(h)
    mode = int(type)
    print mode
    trs = ['t', 'r', 's']
    axises = ['x', 'y', 'z']
    controls = [cmds.listRelatives(x, p=1)[0] for x in cmds.ls(cmds.listRelatives('muscle_controls_grp', ad=1), type = 'nurbsCurve') if 'Rt' in x]
    if controls:
        for ctrl in controls:
            con = cmds.listConnections(ctrl + '.t', type = 'constraint')
            if con:
                cmds.delete(con)
            grp = cmds.listRelatives(ctrl, p=1)[0]
            for chan in trs:
                for axis in axises:
                    if cmds.getAttr(grp + '.' + chan + axis, l=1):
                        cmds.setAttr(grp + '.' + chan + axis, l=0)
                    if chan in 's' and axis in 'z':
                        if mode == 1:
                            cmds.setAttr(grp + '.' + chan + axis, -1)
                        if mode == 0:
                            cmds.setAttr(grp + '.' + chan + axis, 1)
                    cmds.setAttr(grp + '.' + chan + axis, l=1)
            par = cmds.parentConstraint(ctrl, ctrl.replace('anim', 'bind'), mo=1)
            cmds.setAttr(par[0] + '.interpType', 2)
    controlMirror = [cmds.listRelatives(x, p=1)[0] for x in cmds.ls(cmds.listRelatives('muscle_controls_grp', ad=1), type = 'nurbsCurve') if 'Lt' in x]
    cmds.select(controlMirror, r=1)
    mirrorControlShapes()
    if mode == 1:
        if hidden == 1:
            pass
        if hidden == 0:
            cmds.confirmDialog(t = 'Information', m = 'Muscle controls are True Symmetric now!')
    if mode == 0:
        cmds.confirmDialog(t = 'Information', m = 'Muscle controls are NOT True Symmetric now!')

def getCurrentValues(*args):
    follicles = [x for x in cmds.listRelatives('musclefollicleGroup', ad=1) if cmds.nodeType(x) in 'follicle']
    for fol in follicles:
        if 'delt' in fol and 'Lt' in fol:
            val = cmds.getAttr(fol + '.parameterU')
            cmds.floatSliderGrp('del', e=1, v=val)
        if 'armpit' in fol and 'Lt' in fol:
            valU = cmds.getAttr(fol + '.parameterU')
            valV = cmds.getAttr(fol + '.parameterV')
            cmds.floatSliderGrp('armptU', e=1, v=valU)
            cmds.floatSliderGrp('armptV', e=1, v=valV)
        if 'pecs_1' in fol and 'Lt' in fol:
            val = cmds.getAttr(fol + '.parameterU')
            cmds.floatSliderGrp('pecs1', e=1, v=val)
        if 'pecs_2' in fol and 'Lt' in fol:
            val = cmds.getAttr(fol + '.parameterU')
            cmds.floatSliderGrp('pecs2', e=1, v=val)
        if 'hipFix' in fol and 'Lt' in fol:
            val = cmds.getAttr(fol + '.parameterU')
            cmds.floatSliderGrp('hip', e=1, v=val)
        if 'kneeFix' in fol and 'Lt' in fol:
            val = cmds.getAttr(fol + '.parameterU')
            cmds.floatSliderGrp('knee', e=1, v=val)
        if 'upperPecs' in fol and 'Lt' in fol:
            val = cmds.getAttr(fol + '.parameterU')
            cmds.floatSliderGrp('upPec', e=1, v=val)
        



def SetMuscleAdjustments(*args):
    follicles = [x for x in cmds.listRelatives('musclefollicleGroup', ad=1) if cmds.nodeType(x) in 'follicle']
    for fol in follicles:
        if 'delt' in fol:
            val = cmds.floatSliderGrp('del', q=1, v=1)
            cmds.setAttr(fol + '.parameterU', val)
        if 'armpit' in fol:
            valU = cmds.floatSliderGrp('armptU', q=1, v=1)
            valV = cmds.floatSliderGrp('armptV', q=1, v=1)
            cmds.setAttr(fol + '.parameterU', valU)
            cmds.setAttr(fol + '.parameterV', valV)
        if 'pecs_1' in fol:
            val = cmds.floatSliderGrp('pecs1', q=1, v=1)
            cmds.setAttr(fol + '.parameterU', val)
        if 'pecs_2' in fol:
            val = cmds.floatSliderGrp('pecs2', q=1, v=1)
            cmds.setAttr(fol + '.parameterU', val)
        if 'hipFix' in fol:
            val = cmds.floatSliderGrp('hip', q=1, v=1)
            cmds.setAttr(fol + '.parameterU', val)
        if 'kneeFix' in fol:
            val = cmds.floatSliderGrp('knee', q=1, v=1)
            cmds.setAttr(fol + '.parameterU', val)
        if 'upperPecs' in fol:
            val = cmds.floatSliderGrp('upPec', q=1, v=1)
            cmds.setAttr(fol + '.parameterU', val)

def SaveMuscleInformation(*args):
    mainNode = 'muscle_rig'
    follicles = [x for x in cmds.listRelatives('musclefollicleGroup', ad=1) if cmds.nodeType(x) in 'follicle']
    if cmds.objExists(mainNode):
        allAttrs = cmds.listAttr(mainNode, ud=1)
        for fol in follicles:
            if fol not in allAttrs:
                cmds.addAttr(mainNode, ln= fol, dt='string')
            valU = cmds.getAttr(fol + '.parameterU')
            valV = cmds.getAttr(fol + '.parameterV')
            cmds.setAttr(mainNode + '.' + fol, str(valU) + '@' + str(valV), type= 'string')
    SetMuscleAdjustments()
    getCurrentValues()


def RestoreSavedMuscleInformation(*args):
    mainNode = 'muscle_rig'
    follicles = [x for x in cmds.listRelatives('musclefollicleGroup', ad=1) if cmds.nodeType(x) in 'follicle']
    if cmds.objExists(mainNode):
        allAttrs = cmds.listAttr(mainNode, ud=1)
        for attr in allAttrs:
            if attr in follicles:
                valU = float(cmds.getAttr(mainNode + '.' + attr).split('@')[0])
                valV = float(cmds.getAttr(mainNode + '.' + attr).split('@')[0])
                cmds.setAttr(attr + '.parameterU', valU)
                cmds.setAttr(attr + '.parameterV', valV)
    getCurrentValues()

def MuscleAdjustmentUI(*args):
    title = "MuscleAdjustments"
    if cmds.window(title, exists = True):
        cmds.deleteUI(title)
    winMuscleAdjTools = cmds.window( title, mb=1,  widthHeight = (235,175), resizeToFitChildren = 1, s=1)
    cmds.menu(l = 'Tools')
    cmds.menuItem(l = 'Save values as default', c = SaveMuscleInformation)
    cmds.menuItem(l = 'Reset values to default', c = RestoreSavedMuscleInformation)
    cmds.columnLayout(adj=1)
    cmds.text(l= 'Settings of UV positions for the muscles follicles', bgc = (0.0,0.0,0.0), h = 30, w=295)
    cmds.floatSliderGrp( 'del', l = 'deltoid', bgc = (0.3,0.6,0.7), min = 0, max = 1, v = 0.5, f = 1, fmn = 0, fmx = 1, ss = 0.05, s = 0.05, cw3 = (50,30,60), cc = SetMuscleAdjustments)
    cmds.setParent('..')
    
    cmds.paneLayout( cn='horizontal2')
    
    cmds.paneLayout( cn='vertical2')
    cmds.floatSliderGrp('armptU', l = 'armpitU', bgc = (0,0.8,0.0), min = 0, max = 1, v = 0.5, f = 1, fmn = 0, fmx = 1, ss = 0.05, s = 0.05, cw3 = (50,30,60), cc = SetMuscleAdjustments)
    cmds.floatSliderGrp('armptV', l = 'armpitV', bgc = (0,0.8,0.0), min = 0, max = 1, v = 0.5, f = 1, fmn = 0, fmx = 1, ss = 0.05, s = 0.05, cw3 = (50,30,60), cc = SetMuscleAdjustments)
    cmds.setParent('..')
    
    cmds.paneLayout( cn='vertical2')
    cmds.floatSliderGrp('pecs1', l = 'Pecs-1', bgc = (0.7,0.8,0.3), min = 0, max = 1, v=0.33, f= 1,  fmn = 0, fmx = 1, ss = 0.05, s=0.05, cw3 = (50,30,60), cc = SetMuscleAdjustments)
    cmds.floatSliderGrp('pecs2', l = 'Pecs-2', bgc = (0.7,0.8,0.3), min = 0, max = 1, v=0.66, f= 1,  fmn = 0, fmx = 1, ss = 0.05, s=0.05, cw3 = (50,30,60), cc = SetMuscleAdjustments)
    cmds.setParent('..')

    cmds.setParent('..')

    cmds.paneLayout( cn='horizontal3')
    cmds.floatSliderGrp('upPec', l = 'UpPecs', bgc = (0.5,0.8,0.5), min = 0, max = 1, v = 0.5, f = 1, fmn = 0, fmx = 1, ss = 0.05, s = 0.05, cw3 = (50,30,60), cc = SetMuscleAdjustments)
    cmds.floatSliderGrp('hip', l = 'Hip', bgc = (1,0.8,0), min = 0, max = 1, v = 0.5, f = 1, fmn = 0, fmx = 1, ss = 0.05, s = 0.05, cw3 = (50,30,60), cc = SetMuscleAdjustments)
    cmds.floatSliderGrp('knee', l = 'Knee', bgc = (1,0.8,0), min = 0, max = 1, v = 0.5, f = 1, fmn = 0, fmx = 1, ss = 0.05, s = 0.05, cw3 = (50,30,60), cc = SetMuscleAdjustments)
    cmds.setParent('..')

    cmds.showWindow(winMuscleAdjTools)
    getCurrentValues()


def defaulMuscleUI():
    # if 'yes' in loader.Result():
    print 'Loading Muscle Builder......'
    if cmds.window('DefaulMusclesTools', exists = True):
        cmds.deleteUI("DefaulMusclesTools")
    title = "DefaulMusclesTools"
    winMuscleTools = cmds.window( title, mb=1,  widthHeight = (235,175), resizeToFitChildren = 1, s=1)
    cmds.menu(l = 'File')
    cmds.menuItem(l = 'Export muscle locators', c= ExportMuscles)
    cmds.menuItem(l = 'Import muscle locators', c= ImportMuscles)
    cmds.menu(l = 'Edit')
    cmds.menuItem(l = 'Open Muscle Adjustments', c= MuscleAdjustmentUI)
    cmds.menuItem(l = 'Colorize Muscle Controls', c = colorizeMuscleControls)
    cmds.menuItem(l = 'Delete muscles', c= deleteAllMuscles)
    cmds.menu(l = 'Tools')
    cmds.menuItem(l = 'Make True Mirror Muscle Controls', c= partial(makeTrueMirrorMuscleControls, 1))
    cmds.menuItem(l = 'Make Assimetrical Muscle Controls', c= partial(makeTrueMirrorMuscleControls, 0))
    cmds.columnLayout(adj=1)
    cmds.button('allBut', l = 'Create all default muscles (RMB)', ais=1,  bgc = (0.2,0.5,0), h = 40, c = partial(makeAllMusclesDoIt, attachMuscleToControlSet))
    cmds.popupMenu(mm=1)
    cmds.menuItem(l = 'Select joints', c = partial(selectAllMuscles, 0))
    cmds.menuItem(l = 'Select controls', c = partial(selectAllMuscles, 1))
    cmds.separator(h= 5, style = 'in')
    cmds.separator(h= 5, style = 'in')
    cmds.setParent('..')
    cmds.paneLayout(cn= 'quad')
    cmds.button(l = 'Deltoid (RMB)', bgc = (0.7,0.5,0), h = 30, c= partial(buildMuscle, 3, attachMuscleToControlSet))
    cmds.popupMenu( mm=1 )
    cmds.menuItem(l = 'Update deltiod setup', c = updateDeltoid, rp = 'S')
    cmds.menuItem(l = 'Select joints', c = partial(selectMuscles, 'deltoid', 0))
    cmds.menuItem(l = 'Select controls', c = partial(selectMuscles, 'deltoid', 1))
    cmds.button( l = 'Pectoral (RMB)', bgc = (0.7,0.5,0), h = 30, c= partial(buildMuscle, 1, attachMuscleToControlSet))
    cmds.popupMenu( mm=1 )
    cmds.menuItem(l = 'Select joints', c = partial(selectMuscles, 'pecs', 0))
    cmds.menuItem(l = 'Select controls', c = partial(selectMuscles, 'pecs', 1))
    cmds.menuItem(l = 'Update constraints', c = updatePecs, rp = 'S')
    cmds.menuItem(l = 'Upper Pecs', c= partial(buildMuscle, 4, attachMuscleToControlSet), rp = 'N')
    cmds.button(l = 'Hip (RMB)', bgc = (0.2,0.5,0.7), h = 30, c= partial(buildMuscle, 2, attachMuscleToControlSet))
    cmds.popupMenu( mm=1 )
    cmds.menuItem(l = 'Select joints', c = partial(selectMuscles, 'hipFix', 0))
    cmds.menuItem(l = 'Select controls', c = partial(selectMuscles, 'hipFix', 1))
    cmds.button(l = 'Knee (RMB)', bgc = (0.2,0.5,0.7), h = 30, c= partial(buildMuscle, 0, attachMuscleToControlSet))
    cmds.popupMenu( mm=1 )
    cmds.menuItem(l = 'Select joints', c = partial(selectMuscles, 'kneeFix', 0))
    cmds.menuItem(l = 'Select controls', c = partial(selectMuscles, 'kneeFix', 1))
    cmds.setParent('..')
    cmds.paneLayout(cn= 'single')
    cmds.button(l = 'Armpit (RMB)', bgc = (0.9,0.5,0.1), h = 30, c= buildArmpitMuscles)
    cmds.popupMenu( mm=1 )
    cmds.menuItem(l = 'Select joints', c = partial(selectMuscles, 'armpit', 0))
    cmds.setParent('..')
    cmds.columnLayout(adj=1)
    cmds.separator(h= 5, style = 'in')
    cmds.text('Breath system', h = 25, bgc =  (0,0,0))
    cmds.paneLayout(cn= 'vertical2')
    cmds.button(l = 'Make Breath', bgc = (0.7,0.2,0.2), h = 30, c =  CreateBreath)
    cmds.button(l = 'Delete Breath', bgc = (0.9,0.5,0.7), h = 30, c = DelBreath)
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.showWindow(winMuscleTools)
    print cmds.window(winMuscleTools, q=1, wh=1)
    # if not 'yes' in loader.Result():
    #     cmds.error("Object 'null' doesn't exist")
    #     pass
