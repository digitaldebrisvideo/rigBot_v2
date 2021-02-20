# -*- rigBot: part -*-
import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import spaces

def connect(namespace=None, curve=None):

    # get namespace and curve then do a ton of checls
    sel = mc.ls(sl=1)
    if namespace is None and curve is None:
        if not len(sel) == 2:
            mc.warning('Select any node on the car rig THEN select a curve.')
            return

        namespace = utils.get_namespace(sel[0])
        curve = sel[1]

    elif curve and namespace is None:
        if not len(sel) >= 1:
            mc.warning('Select any node on the car rig.')
            return

        namespace = utils.get_namespace(sel[0])

    elif namespace and curve is None:
        if not len(sel) >= 1:
            mc.warning('Select a curve.')
            return

        curve = sel[0]

    if not curve:
        mc.warning('Curve not selected or specified.')
        return

    if not utils.get_shapes(curve) or not mc.nodeType(utils.get_shapes(curve)) == 'nurbsCurve':
        mc.warning('Specified curve is not a NURBS curve.')
        return

    ik = mc.ls(namespace+'*C_path_IK')
    set_range = mc.ls(namespace+'*C_path_range')

    if not ik or not set_range:
        mc.warning('Couild not find chassis nodes in this rig! Cannot continue!')
        return

    ctrl = mc.ls(namespace+'C_chassisWorld_CTL', namespace+'C_cog_CTL')
    if not ctrl:
        mc.warning('Couild not find chassis nodes in this rig! Cannot continue!')
        return

    ctrl = ctrl[0]

    # now that i have all crap i need.. connect it up
    mc.setAttr(ik[0]+'.ikBlend', 0)
    spans = mc.getAttr(curve+'.maxValue')
    mc.setAttr(set_range[0]+'.maxX', spans)

    try:
        mc.connectAttr(curve+'.worldSpace', ik[0]+'.inCurve', f=1)
    except:
        pass

    mc.setAttr(ik[0]+'.ikBlend', 1)
    if mc.objExists(ctrl+'.space'):
        mc.setAttr(ctrl+'.space' ,0)
    else:
        mc.setAttr(ctrl+'.transSpace' ,0)
        mc.setAttr(ctrl+'.orientSpace' ,3)


def disconnect(namespace=None):

    # get namespace and curve then do a ton of checls
    sel = mc.ls(sl=1)
    if namespace is None:
        if not len(sel) >= 1:
            mc.warning('Select any node on the car rig.')
            return

        namespace = utils.get_namespace(sel[0])

    ik = mc.ls(namespace+'*C_path_IK')
    set_range = mc.ls(namespace+'*C_path_range')

    if not ik or not set_range:
        mc.warning('Couild not find chassis nodes in this rig! Cannot continue!')
        return

    ctrl = mc.ls(namespace+'C_chassisWorld_CTL', namespace+'C_cog_CTL')
    if not ctrl:
        mc.warning('Couild not find chassis nodes in this rig! Cannot continue!')
        return
    ctrl = ctrl[0]

    # now that i have all crap i need.. connect it up
    mc.setAttr(ik[0]+'.ikBlend', 0)
    utils.break_connections(ik[0], 'inCurve')
    mc.setAttr(set_range[0]+'.maxX', 100)

    if mc.objExists(ctrl+'.space'):
        mc.setAttr(ctrl+'.space' ,1)
    else:
        mc.setAttr(ctrl+'.transSpace' ,0)
        mc.setAttr(ctrl+'.orientSpace' ,3)

def connect_ground(namespace=None, mesh=None):

    # get namespace and mesh then do a ton of checls
    sel = mc.ls(sl=1)
    if namespace is None and mesh is None:
        if not len(sel) == 2:
            mc.warning('Select any node on the car rig THEN select a mesh.')
            return

        namespace = utils.get_namespace(sel[0])
        mesh = sel[1]

    elif mesh and namespace is None:
        if not len(sel) >= 1:
            mc.warning('Select any node on the car rig.')
            return

        namespace = utils.get_namespace(sel[0])

    elif namespace and mesh is None:
        if not len(sel) >= 1:
            mc.warning('Select a mesh.')
            return

        mesh = sel[0]

    if not mesh:
        mc.warning('Curve not selected or specified.')
        return

    if not utils.get_shapes(mesh) or not mc.nodeType(utils.get_shapes(mesh)) == 'mesh':
        mc.warning('Specified geo is not a polygon mesh.')
        return

    nodes = mc.ls(namespace+':*', type='cmCollision')

    for n in nodes:
        try:
            mc.connectAttr(mesh+'.outMesh', n+'.inputMesh', f=1)
        except:
            pass

    mc.setAttr(namespace+':C_steering_CTL.groundCollision', 1)

def disconnect_ground(namespace=None):

    # get namespace and curve then do a ton of checls
    sel = mc.ls(sl=1)
    if namespace is None:
        if not len(sel) >= 1:
            mc.warning('Select any node on the car rig.')
            return

        namespace = utils.get_namespace(sel[0])

    nodes = mc.ls(namespace+':*', type='cmCollision')
    for n in nodes:
        mesh = mc.listConnections(n+'.inputMesh')
        if mesh:
            mc.disconnectAttr(mesh[0]+'.outMesh', n+'.inputMesh')

def create_motion_path_cog(start_pos=[0,0,0], end_pos=[0,0,5]):

    ctrl = 'C_cog_CTL'

    # path jnt
    base_jnt = mc.createNode('joint', n='C_path_JNT')
    end_jnt = mc.createNode('joint', n='C_path_end_JNT')

    mc.xform(base_jnt, ws=1, t=start_pos)
    mc.xform(end_jnt, ws=1, t=end_pos)

    mc.parent(end_jnt, base_jnt)

    grp = mc.createNode('transform', n=base_jnt+'_GRP', p=base_jnt)
    mc.parent(grp, 'C_worldRoot_JNTS')
    mc.parent(base_jnt, grp)

    utils.set_attrs(grp, l=1, k=0)

    mc.select(base_jnt)
    mm.eval('joint -e  -oj xyz -secondaryAxisOrient yup -ch -zso;')

    # Create IK for path
    ik = mc.ikHandle(sj=base_jnt, ee=end_jnt, sol='ikSplineSolver', ccv=0, scv=0, pcv=0, rtm=1, n='C_path_IK')
    mc.parent(ik[0], grp)
    mc.hide(ik)

    mc.addAttr(ctrl, ln='pathTravel', min=0, max=100, k=1)
    mc.addAttr(ctrl, ln='pathRoll', k=1)

    mc.connectAttr(ctrl+'.pathRoll', ik[0]+'.roll')
    sr = mc.createNode('setRange', n='C_path_range')
    mc.setAttr(sr+'.oldMaxX', 100)

    mc.connectAttr(ctrl+'.pathTravel', sr+'.valueX')
    mc.connectAttr(sr+'.outValueX', ik[0]+'.offset')
    mc.setAttr(ik[0]+'.dTwistControlEnable', 1)

    mc.addAttr(base_jnt, ln='zeroValue')
    mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.tx')
    mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.ty')
    mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.tz')
    mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.rx')
    mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.ry')
    mc.connectAttr(base_jnt+'.zeroValue', base_jnt+'.rz')
    mc.connectAttr(base_jnt+'.zeroValue', end_jnt+'.rx')
    mc.connectAttr(base_jnt+'.zeroValue', end_jnt+'.ry')
    mc.connectAttr(base_jnt+'.zeroValue', end_jnt+'.rz')

    # add spaces
    spaces.tag(ctrl, 'motionPath:'+base_jnt, add_parent_space=0, default=1)
    spc = spaces.Space(ctrl)
    spc.remove_space(1)
