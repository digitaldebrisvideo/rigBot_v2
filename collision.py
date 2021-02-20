import maya.cmds as mc
from rigBot import utils
from rigBot import env

try:
    mc.loadPlugin('cmCollision')
except:
    pass


def create(ctrl=None, mesh='', use_plugin=None):

    sel = mc.ls(sl=1)

    if not ctrl:
        if len(sel) > 1:
            ctrl = mc.ls(sl=1)[0]
            mesh = mc.ls(sl=1)[1]
        else:
            ctrl = mc.ls(sl=1)[0]

    if use_plugin is None:
        use_plugin = env.use_plugin()

    if use_plugin:
        return create_plugin(ctrl, mesh)
    else:
        return create_vanilla(ctrl, mesh)

def create_vanilla(ctrl, mesh):

    # create a collision point locator ( This defins the point of contact)
    colPoint = mc.createNode('transform', n=ctrl+'_collisonPoint', p=ctrl)
    colPointShape = mc.createNode('locator', n=colPoint+'Shape', p=colPoint)
    mc.hide(colPoint)

    # create a collision object ( This is the final result )
    obj = mc.createNode('transform', n=ctrl+'_collison_GRP', p=ctrl)

    # add ctrl attrs
    if not mc.objExists(ctrl+'.collisionEnvelope'):
        mc.addAttr(ctrl, ln='collisionEnvelope', min=0, max=1, dv=1, k=1)

    if not mc.objExists(ctrl+'.collisionFalloff'):
        mc.addAttr(ctrl, ln='collisionFalloff', min=0.001, k=1, dv=0.1)

    # create closest point on mesh to collistion mesh
    cpm = mc.createNode('closestPointOnMesh')
    mc.connectAttr(mesh+'.worldMatrix', cpm+'.inputMatrix')
    mc.connectAttr(mesh+'.outMesh', cpm+'.inMesh')

    # decopmpose matrix for collision point > to posoiton on closest point on mesh
    dmx = mc.createNode('decomposeMatrix')
    mc.connectAttr(colPoint+'.worldMatrix', dmx+'.inputMatrix')
    mc.connectAttr(dmx+'.outputTranslate', cpm+'.inPosition')

    # Create my vectors for ON mesh orientation
    vp0 = mc.createNode('vectorProduct')
    mc.setAttr(vp0+'.operation', 3)
    mc.setAttr(vp0+'.input1X', 1)
    mc.connectAttr(colPoint+'.worldMatrix', vp0+'.matrix')

    z_vp = mc.createNode('vectorProduct')
    mc.setAttr(z_vp+'.operation', 2)
    mc.setAttr(z_vp+'.normalizeOutput', 1)
    mc.connectAttr(vp0+'.output', z_vp+'.input1')
    mc.connectAttr(cpm+'.normal', z_vp+'.input2')

    # Create x vector
    x_vp = mc.createNode('vectorProduct')
    mc.setAttr(x_vp+'.operation', 2)
    mc.setAttr(x_vp+'.normalizeOutput', 1)
    mc.connectAttr(cpm+'.normal', x_vp+'.input1')
    mc.connectAttr(z_vp+'.output', x_vp+'.input2')

    # Create x vector
    y_vp = mc.createNode('vectorProduct')
    mc.setAttr(y_vp+'.operation', 2)
    mc.setAttr(y_vp+'.normalizeOutput', 1)
    mc.connectAttr(x_vp+'.output', y_vp+'.input2')
    mc.connectAttr(z_vp+'.output', y_vp+'.input1')

    # connect 4x4 matrix (matrix on the collison mesh)
    mtx_on_mesh = mc.createNode('fourByFourMatrix')

    mc.connectAttr(x_vp+'.outputX', mtx_on_mesh+'.in00')
    mc.connectAttr(x_vp+'.outputY', mtx_on_mesh+'.in01')
    mc.connectAttr(x_vp+'.outputZ', mtx_on_mesh+'.in02')

    mc.connectAttr(y_vp+'.outputX', mtx_on_mesh+'.in10')
    mc.connectAttr(y_vp+'.outputY', mtx_on_mesh+'.in11')
    mc.connectAttr(y_vp+'.outputZ', mtx_on_mesh+'.in12')

    mc.connectAttr(z_vp+'.outputX', mtx_on_mesh+'.in20')
    mc.connectAttr(z_vp+'.outputY', mtx_on_mesh+'.in21')
    mc.connectAttr(z_vp+'.outputZ', mtx_on_mesh+'.in22')

    mc.connectAttr(cpm+'.positionX', mtx_on_mesh+'.in30')
    mc.connectAttr(cpm+'.positionY', mtx_on_mesh+'.in31')
    mc.connectAttr(cpm+'.positionZ', mtx_on_mesh+'.in32')

    # Create collison reader and pair blend the two matricies
    mmtx = mc.createNode('multMatrix')
    mc.connectAttr(mtx_on_mesh+'.output', mmtx+'.matrixIn[0]')
    mc.connectAttr(colPoint+'.worldInverseMatrix', mmtx+'.matrixIn[1]')

    sr = mc.createNode('setRange')
    mc.setAttr(sr+'.maxX', 1)

    read_mmtx = mc.createNode('multMatrix')
    read_inv = mc.createNode('inverseMatrix')
    read_dmx = mc.createNode('decomposeMatrix')

    mc.connectAttr(mtx_on_mesh+'.output', read_inv+'.inputMatrix')
    mc.connectAttr(colPoint+'.worldMatrix', read_mmtx +'.matrixIn[0]')
    mc.connectAttr(read_inv+'.outputMatrix', read_mmtx +'.matrixIn[1]')
    mc.connectAttr(read_mmtx+'.matrixSum', read_dmx+'.inputMatrix')
    utils.connect_negative(read_dmx+'.outputTranslateY', sr+'.valueX')
    utils.connect_negative(ctrl+'.collisionFalloff', sr+'.oldMinX')

    mdl = mc.createNode('multDoubleLinear')
    mc.connectAttr(ctrl+'.collisionEnvelope', mdl+'.i1')
    mc.connectAttr(sr+'.outValueX', mdl+'.i2')

    # Handle offset support for when the collison point is not exactly where the ctrl pivot is
    mmtx2 = mc.createNode('multMatrix')
    mc.connectAttr(mmtx+'.matrixSum', mmtx2+'.matrixIn[0]')
    mc.connectAttr(ctrl+'.worldMatrix', mmtx2+'.matrixIn[1]')

    wtmtx = mc.createNode('wtAddMatrix')
    mc.connectAttr(ctrl+'.worldMatrix', wtmtx+'.wtMatrix[0].matrixIn')
    utils.connect_reverse(mdl+'.o', wtmtx+'.wtMatrix[0].weightIn')

    mc.connectAttr(mmtx2+'.matrixSum', wtmtx+'.wtMatrix[1].matrixIn')
    mc.connectAttr(mdl+'.o', wtmtx+'.wtMatrix[1].weightIn')

    dmtx_final = mc.createNode('decomposeMatrix')
    mmtx3 = mc.createNode('multMatrix')
    mc.connectAttr(wtmtx+'.matrixSum', mmtx3+'.matrixIn[1]')
    mc.connectAttr(obj+'.parentInverseMatrix', mmtx3+'.matrixIn[2]')
    mc.connectAttr(mmtx3+'.matrixSum', dmtx_final+'.inputMatrix')

    mc.connectAttr(dmtx_final+'.outputTranslate', obj+'.t')
    mc.connectAttr(dmtx_final+'.outputRotate', obj+'.r')

    mc.addAttr(obj, ln='collision', min=0, max=1, k=1)
    mc.connectAttr(mdl+'.o', obj+'.collision')
    mc.setAttr(obj+'.collision', l=1)

    mc.select(ctrl)
    utils.set_attrs(obj, 't r s v', l=1, k=0)
    utils.set_attrs(colPoint, 'r s v', l=1, k=0)

    return obj, colPoint

def create_plugin(ctrl, mesh=''):

    colPoint = mc.createNode('transform', n=ctrl+'_collisonPoint', p=ctrl)
    colPointShape = mc.createNode('locator', n=colPoint+'Shape', p=colPoint)
    mc.hide(colPoint)

    # create a collision object ( This is the final result )
    obj = mc.createNode('transform', n=ctrl+'_collison_GRP', p=ctrl)

    # add ctrl attrs
    if not mc.objExists(ctrl+'.collisionEnvelope'):
        mc.addAttr(ctrl, ln='collisionEnvelope', min=0, max=1, dv=1, k=1)

    if not mc.objExists(ctrl+'.useForceCollision'):
        mc.addAttr(ctrl, ln='useForceCollision', min=0, max=1, dv=0, k=1)

    if not mc.objExists(ctrl+'.forceCollision'):
        mc.addAttr(ctrl, ln='forceCollision', min=0, max=1, dv=0, k=1)

    if not mc.objExists(ctrl+'.collisionFalloff'):
        mc.addAttr(ctrl, ln='collisionFalloff', min=0, k=1, dv=0.1)

    if not mc.objExists(ctrl+'.pinOnContact'):
        mc.addAttr(ctrl, ln='pinOnContact', min=0, max=1, k=1, dv=0)

    if not mc.objExists(ctrl+'.groundPlane'):
        mc.addAttr(ctrl, ln='groundPlane', k=1, dv=0)

    if not mc.objExists(ctrl+'.isColliding'):
        mc.addAttr(ctrl, ln='isColliding', k=1, dv=0)

    cnode = mc.createNode('cmCollision')

    mc.setAttr(ctrl+'.isColliding', l=0, k=1)

    time = mc.ls(type='time')
    mc.connectAttr(time[0]+'.outTime', cnode+'.time')
    mc.connectAttr(colPoint+'.worldMatrix', cnode+'.im')
    mc.connectAttr(obj+'.parentInverseMatrix', cnode+'.pm')

    mc.connectAttr(ctrl+'.collisionEnvelope', cnode+'.envelope')
    mc.connectAttr(ctrl+'.collisionFalloff', cnode+'.falloff')
    mc.connectAttr(ctrl+'.forceCollision', cnode+'.override')
    mc.connectAttr(ctrl+'.useForceCollision', cnode+'.forceOverride')
    mc.connectAttr(ctrl+'.pinOnContact', cnode+'.pinOnContact')
    mc.connectAttr(ctrl+'.groundPlane', cnode+'.groundPlane')

    if mc.objExists(mesh+'.outMesh'):
        mc.connectAttr(mesh+'.outMesh', cnode+'.mesh')
    else:
        mc.warning('No mesh is connected! This will only work with the ground plane attribute. ')

    mc.connectAttr(cnode+'.ot', obj+'.t')
    mc.connectAttr(cnode+'.or', obj+'.r')
    mc.connectAttr(cnode+'.isColliding', ctrl+'.isColliding')
    mc.setAttr(ctrl+'.isColliding', l=1)

    return obj, colPoint
