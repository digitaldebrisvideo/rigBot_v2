import maya.cmds as mc

from rigBot import utils

import cPickle as pickle
import os
import time

file_extention = '.pose'

def get_pose_nodes():
    """Get all poseInterpolator nodesin scene"""

    return [utils.get_transform(p) for p in mc.ls(type='poseInterpolator')]

def get_translation_pose_nodes():
    """Get all translation pose drivers in scene"""

    return [n.split('.')[0] for n in mc.ls('*.transPoseInterpolatorDrivers')]

def save(file_path, node):
    """Write ALL pose interpolators in scene to disk"""

    t = time.time()

    interp_nodes = get_pose_nodes()
    trans_nodes = get_translation_pose_nodes()

    if node in interp_nodes:

        if not file_path.endswith(file_extention):
            file_path = os.path.splitext(file_path)[0]+file_extention

        result = mc.poseInterpolator(node, e=1, ex=file_path)
        print 'Wrote pose interpolator data to: %s' % result
        print time.time() - t

    elif node in trans_nodes:

        data = {}
        info = {
            'drivers': eval(mc.getAttr(node+'.transPoseInterpolatorDrivers')),
            'ctrl_driver': mc.getAttr(node+'.transPoseInterpolatorCtrlDriver') or None,
            'driven_attribute': mc.getAttr(node+'.transPoseInterpolatorDrivenAttribute') or None,
            'orientation': mc.getAttr(node+'.transPoseInterpolatorOrientation')
        }

        data[node] = info

        if data:
            ext = '.trpose'
            if not file_path.endswith(ext):
                file_path = os.path.splitext(file_path)[0]+ext

            utils.write_json(file_path, data)
            print time.time() - t

    else:
        mc.warning(node+' is not a pose node!')


def load(file_path, **kwargs):
    """Read pose interpolators from disk"""

    pose_file_path = ''
    trans_pose_file_path = ''

    if file_path.endswith(file_extention):
        pose_file_path = file_path
        trans_pose_file_path = pose_file_path.replace(file_extention,'.tr'+file_extention.replace('.', ''))

    elif file_path.endswith('.trpose'):
        trans_pose_file_path = file_path
        pose_file_path = trans_pose_file_path.replace('.tr'+file_extention.replace('.', ''), file_extention)

    if os.path.isfile(pose_file_path):
        try:
            mc.poseInterpolator(im=pose_file_path)

            if mc.objExists('noXform_GRP'):
                nodes = get_pose_nodes()
                for n in nodes:
                    p = mc.listRelatives(n, p=1) or ['']
                    if not p == 'noXform_GRP':
                        mc.parent(n, 'noXform_GRP')

            print 'Loaded poses from: '+file_path

        except:
            pass

    if os.path.isfile(trans_pose_file_path):
        data = utils.read_json(trans_pose_file_path)

        for name, info in data.items():
            drivers = info['drivers']
            ctrl_driver = info['ctrl_driver']
            driven_attribute = info['driven_attribute']
            orientation = info['orientation']

            trPose = create_translation_pose_node(drivers, ctrl_driver, driven_attribute, orientation)
            if trPose:
                print 'Loaded trPose for: '+name

    pose_interps = [utils.get_transform(p) for p in mc.ls(type='poseInterpolator')]
    pose_interps = [p for p in pose_interps if not utils.get_parent(p)]

    if pose_interps and mc.objExists('noXform_GRP'):
        mc.parent(pose_interps, 'noXform_GRP')


def create_translation_pose_node(drivers=[], ctrl_driver='', driven_attribute='', orientation='local'):
    """Create translation pose interpplator"""

    for d in drivers:
        if not mc.objExists(d):
            return

    name = drivers[1]+'_trPoseInterpolator'

    orig_ctrl_driver = ctrl_driver
    no_translation = False
    if not mc.objExists(ctrl_driver):
        no_translation = True
        ctrl_driver = drivers[1]

    tpose = mc.xform(ctrl_driver, q=1, a=1, t=1)
    rpose = mc.xform(ctrl_driver, q=1, a=1, ro=1)

    if not no_translation:
        mc.xform(ctrl_driver, a=1, t=[0,0,0])
    mc.xform(ctrl_driver, a=1, ro=[0,0,0])

    # Create driver nodes
    if not mc.objExists(name):

        name = mc.createNode('transform', n=name)
        reader = mc.createNode('transform', n=name+'_r', p=name)

        if orientation == 'local':
            mc.delete(mc.pointConstraint(drivers[1], name))
        else:
            mc.delete(mc.parentConstraint(drivers[1], name))

        mc.delete(mc.pointConstraint(drivers[2], name))
        mc.parentConstraint(drivers[0], name, mo=1, n=name+'_prc')
        mc.pointConstraint(drivers[2], reader, mo=1, n=reader+'_pc')
        mc.scaleConstraint(drivers[0], name, mo=1, n=name+'_sc')

        mc.addAttr(name, ln='transPoseInterpolatorDrivers', dt="string", hidden=1)
        mc.addAttr(name, ln='transPoseInterpolatorCtrlDriver', dt="string", hidden=1)
        mc.addAttr(name, ln='transPoseInterpolatorDrivenAttribute', dt="string", hidden=1)
        mc.addAttr(name, ln='transPoseInterpolatorOrientation', dt='string', hidden=1)

        if not driven_attribute:
            driven_attribute = ''

        mc.setAttr(name+'.transPoseInterpolatorDrivers', str(drivers), type='string')
        mc.setAttr(name+'.transPoseInterpolatorCtrlDriver', orig_ctrl_driver, type='string')
        mc.setAttr(name+'.transPoseInterpolatorDrivenAttribute', driven_attribute, type='string')
        mc.setAttr(name+'.transPoseInterpolatorOrientation', orientation, type='string')

        if mc.objExists('noXform_GRP'):
            mc.parent(name, 'noXform_GRP')

        mc.select(name)

    # Key driven attr based on the greatest attribute
    if driven_attribute and mc.objExists(driven_attribute):

        reader = name+'_r'
        mc.xform(ctrl_driver, a=1, t=tpose, ro=rpose)

        attr = 'tx'
        if abs(mc.getAttr(reader+'.ty')) > abs(mc.getAttr (reader+'.tx')):
            attr = 'ty'
        if abs(mc.getAttr(reader+'.tz')) > abs(mc.getAttr (reader+'.ty')):
            attr = 'tz'

        tt = 'linear'
        mc.setDrivenKeyframe(driven_attribute, cd=reader+'.'+attr, v=1, itt=tt, ott=tt)
        mc.setDrivenKeyframe(driven_attribute, cd=reader+'.'+attr, v=0, dv=0, itt=tt, ott=tt)

    return name


'''
def vectorDriver(nodes):

    prefix=mc.createNode('mute', n= nodes[0]+'_'+nodes[1]+'_vector_driver#')
    mc.delete(prefix)

    if not mc.objExists('bcls_drivers'):
        mc.createNode('transform', n='bcls_drivers', p='noTransform')


    pos = mc.xform(nodes[1],q=True,ws=True,t=True)

    #create pose sphere
    poseS = mc.sphere(name=prefix + '_Pose',axis=[0,1,0],ch=0)
    mc.rebuildSurface(poseS[0],ch=0,rpo=1,rt=0,end=0,kr=0,kcp=0,su=4,du=3,sv=8,tol=.01,fr=0,dir=2)

    mc.setAttr(poseS[0] + '.tx',pos[0])
    mc.setAttr(poseS[0] + '.ty',pos[1])
    mc.setAttr(poseS[0] + '.tz',pos[2])

    mc.setAttr(poseS[0] + "Shape.castsShadows", 0)
    mc.setAttr(poseS[0] + "Shape.receiveShadows", 0)
    mc.setAttr(poseS[0] + "Shape.motionBlur", 0)
    mc.setAttr(poseS[0] + "Shape.primaryVisibility", 0)
    mc.setAttr(poseS[0] + "Shape.smoothShading", 0)
    mc.setAttr(poseS[0] + "Shape.visibleInReflections", 0)
    mc.setAttr(poseS[0] + "Shape.visibleInRefractions", 0)
    mc.setAttr(poseS[0] + "Shape.doubleSided", 0)

    # assign influence map to spheres
    shader = mc.shadingNode('lambert',asShader=1,name=prefix+'_PoseLambert')
    mc.select(poseS[0],r=True)
    mc.hyperShade(assign=shader)

    ramp = mc.shadingNode('ramp',asTexture=1,name=prefix+'_PoseRamp')
    mc.removeMultiInstance(ramp + '.colorEntryList[2]',b=True)
    mc.setAttr(ramp + '.colorEntryList[1].position',.5)
    mc.setAttr(ramp + '.colorEntryList[0].color',1,1,1,type='double3')
    mc.setAttr(ramp + '.colorEntryList[1].color',0,0,0,type='double3')
    mc.setAttr(ramp + '.type',1)

    place2DT = mc.shadingNode('place2dTexture',asUtility=1,name=prefix+'_Pose2dText')
    mc.connectAttr(place2DT + '.outUV',ramp + '.uv')
    mc.connectAttr(place2DT + '.outUvFilterSize',ramp + '.uvFilterSize')
    mc.connectAttr(ramp + '.outColor', shader + '.color')

    #create aim locator
    driveLoc = mc.spaceLocator(name=prefix)
    driveLocShape = mc.listRelatives(driveLoc[0],shapes=True)[0]

    mc.addAttr(driveLoc[0],ln='weight',at='double',min=0,max=1, k=1)
    mc.addAttr(driveLoc[0],ln='falloff',at='double',min=.0001,max=1,dv=.5, k=1)
    mc.connectAttr(driveLoc[0] + '.falloff', ramp + '.colorEntryList[1].position')

    mc.select(driveLoc[0],r=1)
    driveLocGrp = mc.createNode ('transform', n=driveLoc[0]+'_att')
    mc.parent(driveLoc[0], driveLocGrp)

    mc.parentConstraint(nodes[1], driveLocGrp, n =driveLocGrp +'_parc')
    mc.scaleConstraint(nodes[1], driveLocGrp, n =driveLocGrp +'_sc')

    mc.delete(mc.pointConstraint(nodes[2], driveLoc[0] ))
    mc.delete(mc.aimConstraint(driveLoc[0],poseS[0],offset=[0,0,0],weight=1,aimVector=[0,-1,0],upVector=[0,0,1],worldUpType='vector',worldUpVector=[0,0,1]))

    #create pose reading nodes
    cpos = mc.createNode('closestPointOnSurface',name=prefix + '_cpos')

    mc.connectAttr(poseS[0] + '.ws[0]',cpos + '.inputSurface')
    mc.connectAttr(driveLocShape + '.worldPosition[0]', cpos + '.inPosition')
    mc.connectAttr(cpos + '.parameterU',ramp + '.uCoord')
    mc.connectAttr(cpos + '.parameterV' ,ramp + '.vCoord')
    mc.connectAttr(ramp + '.outColorR',driveLoc[0] + '.weight')

    #connect poseShere
    poseSpar=mc.createNode('transform', n=poseS[0]+'_att', p=driveLocGrp)
    mc.parent(poseS[0], poseSpar)
    mc.parentConstraint(nodes[0], poseSpar, mo=1, n=poseSpar+'_parc')
    mc.pointConstraint(nodes[1], poseS[0], mo=1,name=poseS[0]+'_pc')

    mc.addAttr (prefix, ln='nodes', dt="string")
    mc.setAttr(prefix+'.nodes', ' '.join(nodes), type='string')

    mc.parent(driveLocGrp, 'bcls_drivers')
    mc.hide(poseS[0], driveLocShape)
    return prefix
'''

class transPoseDriverUI():
    def __init__(self):

        if mc.window ('poseDriverUI', q=1, ex=1):
            mc.deleteUI('poseDriverUI')
        win = mc.window('poseDriverUI', t='Translation Based Driver UI')

        mc.columnLayout(adj=1, rs=4)
        mc.textFieldButtonGrp('drv_tfg', l='3 Joint Drivers', bl='\t\tGet\t\t', bc=self.getDrvs, cw3=[150, 300, 60])
        mc.textFieldButtonGrp('ct_tfg', l='Anim Ctrl Driver', bl='\t\tGet\t\t', bc=self.getCtrl, cw3=[150, 300, 60])
        mc.textFieldButtonGrp('dn_tfg', l='Driven BlendShape Attribute', bc=self.getDvAttr, bl='\t\tGet\t\t', cw3=[150, 300, 60])
        mc.checkBoxGrp( 'chx', numberOfCheckBoxes=1, l='World Orient', cw2=[150, 300])
        mc.button (l='Create Translation Based Driver', c=self.createDrv)

        mc.showWindow (win)
        mc.window(win, e=1, wh=[500, 131])
        mc.window(win, e=1, s=0)

    def getDrvs(self):
        sel = mc.ls (sl=1)
        if not len(sel) == 3:
            mc.warning ('Select 3 joint drivers.')
            return
        mc.textFieldButtonGrp('drv_tfg', e=1, tx=' '.join(sel))

    def getCtrl(self):
        sel = mc.ls (sl=1)
        if not sel:
            mc.warning ('Select Ctrl.')
            return
        mc.textFieldButtonGrp('ct_tfg', e=1, tx=sel[-1])

    def getDvAttr(self):

        sel = mc.ls (sl=1)
        if not sel:
            mc.warning ('Select a node and attribute from the channelBox to drive.')
            return
        attrs = printTools.getAttrsFromCB()
        if not attrs:
            mc.warning ('Select a node and attribute from the channelBox to drive.')
            return

        node = sel[0]+'.'+attrs[0]
        if not mc.objExists(node):
            mc.error (node+' does not exist!')
        mc.textFieldButtonGrp('dn_tfg', e=1, tx=node)

    def createDrv(self, *args):

            drivers = mc.textFieldButtonGrp('drv_tfg', q=1, tx=1).strip().split(' ')
            ctrl = mc.textFieldButtonGrp('ct_tfg', q=1, tx=1).strip().split(' ')[0]
            drivenAttr = mc.textFieldButtonGrp('dn_tfg', q=1, tx=1).strip().split(' ')[0]
            wo = mc.checkBoxGrp('chx', q=1, v1=1)

            if wo == 0:
                orientation = 'local'
            else:
                orientation = 'world'

            for n in drivers+[ctrl]:
                if not mc.objExists(n):
                    mc.warning(n+' does not exist!')
                    return

            create_translation_pose_node(drivers, ctrl, drivenAttr, wo)
