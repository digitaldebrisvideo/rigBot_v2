# -*- coding: utf-8 -*-
"""Functions for creating rivets."""
import maya.OpenMaya as om
import maya.api.OpenMaya as OpenMaya

import maya.cmds as mc
import maya.mel as mm
import re

from rigBot import utils

def rebuild_surface(surf):
    surf = mm.eval('rebuildSurface -ch 0 -rpo 1 -rt 0 -end 1 -kr 0 -kcp 1 -kc 1 -su 4 -du 0 -sv 4 -dv 0 -tol 0.01 -fr 0  -dir 2 '+surf)
    mc.delete(surf, ch=1)

def assign_ribbon_shader(nodes):

    nodes = mc.ls(nodes)
    if not nodes:
        return

    shd = 'ribbon_SHD'
    sg = 'ribbon_SG'
    if not mc.objExists(shd):
        shd = mc.createNode('blinn', n=shd)
    mc.setAttr(shd+'.transparency', 0.8, 0.8, 0.8)
    mc.setAttr(shd+'.color', 0.25, 0.25, 0.65)
    mc.setAttr(shd+'.specularRollOff', 0.3)

    if not mc.objExists(sg):
        sg = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=sg)
        mc.connectAttr(shd+'.outColor', sg+'.surfaceShader')

    mc.sets(nodes, forceElement=sg)
    mc.select(nodes)
    mc.toggle(editPoint=1, origin=1)

def surface_fll(nodes, surf, noxform_grp='noXform_GRP', world_scale_node='', constraint_type='parent', ctrl_driver=None):
    """Connect nodes to a nurbs surface using follicles.

        Args:
            :nodes: (list) Nodest o attach .
            :surf: (str) Input surface.

        Kwargs:
            :noxform_grp: No transform group for parenting. Defaults to None.
            :world_scale_node: Uniform scale attribute for proper scaling. Defaults to "".
            :constraint_type: Constraint type. Defaults to "parent". Options are "point", "orient" "parent"

        Returns:
            :follicles: (list) Follicle names."""

    if not noxform_grp:
        noxform_grp = 'rivets'

    nodes = mc.ls(nodes)
    shapes = mc.listRelatives(surf, type='nurbsSurface')

    if not nodes or not shapes:
        raise ValueError('Nodes or surface dont exist!')

    shape = shapes[0]
    fll_suffix = utils.get_suffix('follicle')
    flls = []

    if not mc.objExists(noxform_grp) :
        noxform_grp = mc.createNode('transform', n=noxform_grp)
        mc.setAttr (noxform_grp+'.inheritsTransform', 0)

    poc = mc.createNode('closestPointOnSurface')
    mc.connectAttr(surf+'.worldSpace', poc+'.inputSurface')

    for node in nodes:
        if ctrl_driver:
            dmx = mc.createNode('decomposeMatrix')
            mc.connectAttr(ctrl_driver+'.worldMatrix', dmx+'.inputMatrix')
            mc.connectAttr(dmx+'.outputTranslate', poc+'.inPosition')

        else:
            mc.setAttr(poc+'.inPositionX', mc.xform(node, q=1, ws=1, t=1)[0])
            mc.setAttr(poc+'.inPositionY', mc.xform(node, q=1, ws=1, t=1)[1])
            mc.setAttr(poc+'.inPositionZ', mc.xform(node, q=1, ws=1, t=1)[2])

        fll = mc.createNode('transform', n=node+'_'+fll_suffix, p=noxform_grp)
        fllShape = mc.createNode('follicle', n=fll+'Shape', p=fll)
        mc.hide(fllShape)

        mc.connectAttr(fllShape + '.outRotate', fll+ '.rotate', f=1)
        mc.connectAttr(fllShape + '.outTranslate', fll+ '.translate', f=1)
        mc.connectAttr(surf + '.worldMatrix[0]', fllShape + '.inputWorldMatrix', f=1)
        mc.connectAttr(surf + '.local', fllShape + '.inputSurface', f=1)
        mc.setAttr(fllShape+'.simulationMethod', 0)
        mc.setAttr(fllShape+'.startDirection', 0)

        paramU = mc.getAttr(poc+'.parameterU')
        paramV = mc.getAttr(poc+'.parameterV')

        if ctrl_driver:
            mc.connectAttr(poc+'.parameterU', fllShape+'.parameterU')
            mc.connectAttr(poc+'.parameterV', fllShape+'.parameterV')

        else:
            mc.setAttr(fllShape+'.parameterU', paramU)
            mc.setAttr(fllShape+'.parameterV', paramV)

        if mc.objExists(world_scale_node):
            mc.scaleConstraint(world_scale_node, fll, n=fll+'_sc', mo=1)

        if constraint_type is not None:
            if constraint_type == 'point':
                mc.pointConstraint(fll, node,n=node+'_prc', mo=True)

            elif constraint_type == 'orient':
                mc.orientConstraint(fll, node,n=node+'_prc', mo=True)

            else:
                mc.parentConstraint(fll, node,n=node+'_prc', mo=True)

        flls.append(fll)

    if not ctrl_driver:
        mc.delete(poc)

    return flls


def motionPath(node, crv, up=None):
    """Connect a node to a nurbs curve using a motionPath node.

        Args:
            :node: (str) Nodest o attach .
            :crv: (str) Input curve.

        Kwargs:
            :up: Up object for connecitng rotations. Defaults to None.

        Returns:
            :motionPath: (str) motionPath node name."""

    shape = utils.get_shapes(crv)[0]

    # get param
    pos = mc.xform(node, ws=1,t=1,q=1)
    cpc = mc.createNode('nearestPointOnCurve')
    mc.connectAttr(shape+'.local', cpc+'.inputCurve')
    mc.setAttr(cpc+'.inPosition', pos[0], pos[1], pos[2])

    param = mc.getAttr(cpc+'.parameter')
    mc.delete(cpc)

    # create motion path node
    mp = mc.createNode ('motionPath', n=node+'_mp')

    mc.setAttr(mp+'.uValue', param)
    mc.connectAttr(shape+'.worldSpace', mp+'.geometryPath')
    mc.connectAttr(mp+'.xCoordinate', node+'.tx')
    mc.connectAttr(mp+'.yCoordinate', node+'.ty')
    mc.connectAttr(mp+'.zCoordinate', node+'.tz')

    if not up:
        return mp

    mc.setAttr(mp+'.worldUpType', 1)
    mc.setAttr(mp+'.frontAxis', 0)
    mc.setAttr(mp+'.upAxis', 1)

    mc.connectAttr(up+'.worldMatrix', mp+'.worldUpMatrix')
    mc.connectAttr(mp+'.rx', node+'.rx')
    mc.connectAttr(mp+'.ry', node+'.ry')
    mc.connectAttr(mp+'.rz', node+'.rz')

    return mp

def rivet_ctrl(surf, ctrl, jnt, rivets_grp='rivets_GRP', mo=True):

    jnt_parent = utils.get_parent(jnt)
    shape = [s for s in utils.get_shapes(surf) if mc.nodeType(s) == 'nurbsSurface']

    if not shape:
        raise ValueError('surf has no nurbs shape!')

    if not mc.objExists(rivets_grp) :
        rivets_grp = mc.createNode('transform', n=rivets_grp, p='noXform_GRP')
        mc.setAttr(rivets_grp+'.inheritsTransform', 0)

    # Create closest point on surface
    cpos = mc.createNode('closestPointOnSurface')
    mc.connectAttr(surf+'.worldSpace', cpos+'.inputSurface')

    # Create decompose matrix for ctrl
    dmx = mc.createNode('decomposeMatrix')
    mc.connectAttr(ctrl+'.worldMatrix', dmx+'.inputMatrix')
    mc.connectAttr(dmx+'.outputTranslate', cpos+'.inPosition')

    # Create point on surface info
    psinfo = mc.createNode('pointOnSurfaceInfo')
    mc.connectAttr(surf+'.worldSpace', psinfo+'.inputSurface')
    mc.connectAttr(cpos+'.parameterU', psinfo+'.parameterU')
    mc.connectAttr(cpos+'.parameterV', psinfo+'.parameterV')

    # recreate the new world matrix
    mtx = mc.createNode('fourByFourMatrix')
    mc.connectAttr(psinfo+'.normalX', mtx+'.i00')
    mc.connectAttr(psinfo+'.normalY', mtx+'.i01')
    mc.connectAttr(psinfo+'.normalZ', mtx+'.i02')
    mc.connectAttr(psinfo+'.tangentUx', mtx+'.i10')
    mc.connectAttr(psinfo+'.tangentUy', mtx+'.i11')
    mc.connectAttr(psinfo+'.tangentUz', mtx+'.i12')
    mc.connectAttr(psinfo+'.tangentVx', mtx+'.i20')
    mc.connectAttr(psinfo+'.tangentVy', mtx+'.i21')
    mc.connectAttr(psinfo+'.tangentVz', mtx+'.i22')
    mc.connectAttr(psinfo+'.positionX', mtx+'.i30')
    mc.connectAttr(psinfo+'.positionY', mtx+'.i31')
    mc.connectAttr(psinfo+'.positionZ', mtx+'.i32')

    # Output decompsoe matrix
    out_dmx = mc.createNode('decomposeMatrix')
    mc.connectAttr(mtx+'.o', out_dmx+'.inputMatrix')

    # Create world rivet transform node
    world_drv = mc.createNode('transform', p=rivets_grp, n=jnt+'_world_rivet_GRP')
    mc.connectAttr(out_dmx+'.outputTranslate', world_drv+'.t')
    mc.connectAttr(out_dmx+'.outputRotate', world_drv+'.r')

    if jnt_parent:
        mc.scaleConstraint(jnt_parent, world_drv)

    # group joint
    jnt_parent = utils.get_parent(jnt)
    jnt_offset = mc.createNode('transform', n=jnt+'_rivet_GRP', p=jnt_parent)
    mc.delete(mc.parentConstraint(jnt, jnt_offset))

    # Remove constraints from jnt
    cons = utils.get_constraints(jnt)
    cons_to_remove = ['parentConstraint', 'pointConstraint', 'orientConstraint', 'aimConstraint']
    cons = [c for c in cons if mc.nodeType(c) in cons_to_remove]
    if cons:
        mc.delete(cons)

    # constraint offset node and parent joint
    mc.parentConstraint(world_drv, jnt_offset, mo=mo)
    mc.parent(jnt, jnt_offset)

    # connect offset
    mc.addAttr(ctrl, ln='offsetX', k=1)
    mc.addAttr(ctrl, ln='offsetY', k=1)
    mc.addAttr(ctrl, ln='offsetZ', k=1)

    if ctrl.startswith('R_'):
        utils.connect_negative(ctrl+'.offsetX', jnt+'.tx')
        utils.connect_negative(ctrl+'.offsetY', jnt+'.ty')
        utils.connect_negative(ctrl+'.offsetZ', jnt+'.tz')
        mc.connectAttr(ctrl+'.r', jnt+'.r')

    else:
        mc.connectAttr(ctrl+'.offsetX', jnt+'.tx')
        mc.connectAttr(ctrl+'.offsetY', jnt+'.ty')
        mc.connectAttr(ctrl+'.offsetZ', jnt+'.tz')
        mc.connectAttr(ctrl+'.r', jnt+'.r')

    return psinfo

def surface_mtx(surf, nodes, noxform_grp='noXform_GRP'):

    nodes = mc.ls(nodes)

    for node in nodes:

        # get u and v param
        cpos = mc.createNode('closestPointOnSurface')
        mc.connectAttr(surf+'.worldSpace', cpos+'.inputSurface')
        mc.setAttr(cpos+'.inPositionX', mc.xform(node, q=1, ws=1, t=1)[0])
        mc.setAttr(cpos+'.inPositionY', mc.xform(node, q=1, ws=1, t=1)[1])
        mc.setAttr(cpos+'.inPositionZ', mc.xform(node, q=1, ws=1, t=1)[2])

        param_u = max(mc.getAttr(cpos+'.parameterU'), 0.001)
        param_v = max(mc.getAttr(cpos+'.parameterV'), 0.001)
        mc.delete(cpos)

        # make parameter attrs
        if not mc.objExists(node+'.parameterU'):
            mc.addAttr(node, ln='parameterU', k=1, dv=param_u)
        if not mc.objExists(node+'.parameterV'):
            mc.addAttr(node, ln='parameterV', k=1, dv=param_v)
        if not mc.objExists(node+'.turnOnPercentage'):
            mc.addAttr(node, ln='turnOnPercentage', k=1, dv=0, at='bool')

        # Create point on surface info
        psinfo = mc.createNode('pointOnSurfaceInfo')
        mc.connectAttr(surf+'.worldSpace', psinfo+'.inputSurface')
        mc.connectAttr(node+'.parameterU', psinfo+'.parameterU')
        mc.connectAttr(node+'.parameterV', psinfo+'.parameterV')
        mc.connectAttr(node+'.turnOnPercentage', psinfo+'.turnOnPercentage')

        # recreate the new world matrix for node
        mtx = mc.createNode('fourByFourMatrix')
        mc.connectAttr(psinfo+'.normalX', mtx+'.i00')
        mc.connectAttr(psinfo+'.normalY', mtx+'.i01')
        mc.connectAttr(psinfo+'.normalZ', mtx+'.i02')
        mc.connectAttr(psinfo+'.tangentUx', mtx+'.i10')
        mc.connectAttr(psinfo+'.tangentUy', mtx+'.i11')
        mc.connectAttr(psinfo+'.tangentUz', mtx+'.i12')
        mc.connectAttr(psinfo+'.tangentVx', mtx+'.i20')
        mc.connectAttr(psinfo+'.tangentVy', mtx+'.i21')
        mc.connectAttr(psinfo+'.tangentVz', mtx+'.i22')
        mc.connectAttr(psinfo+'.positionX', mtx+'.i30')
        mc.connectAttr(psinfo+'.positionY', mtx+'.i31')
        mc.connectAttr(psinfo+'.positionZ', mtx+'.i32')

        # get offset
        mult_mtx = mc.createNode('multMatrix')
        dmx = mc.createNode('decomposeMatrix')
        world_drv = mc.createNode('transform', n=node+'_rivet_GRP', p=noxform_grp)

        mc.connectAttr(mtx+'.o', mult_mtx +'.matrixIn[0]')
        mc.connectAttr(world_drv+'.parentInverseMatrix', mult_mtx +'.matrixIn[1]')
        mc.connectAttr(mult_mtx+'.matrixSum', dmx+'.inputMatrix')
        mc.connectAttr(dmx+'.outputTranslate', world_drv+'.t')
        mc.connectAttr(dmx+'.outputRotate', world_drv+'.r')

        # parent constrain node
        mc.parentConstraint(world_drv, node, mo=1)

def curve_surf_mtx(crv, surf, nodes, noxform_grp='noXform_GRP'):

    nodes = mc.ls(nodes)
    world_drv_nodes = []

    for node in nodes:

        # get parameter
        pos = mc.xform(node, q=1, ws=1, t=1)
        npoc = mc.createNode('nearestPointOnCurve')

        mc.connectAttr(crv+'.worldSpace', npoc+'.inputCurve')
        mc.setAttr(npoc+'.inPosition', pos[0], pos[1], pos[2])
        param = mc.getAttr(npoc+'.parameter')
        mc.delete(npoc)

        # create point on curve info and word drv node
        pcinfo = mc.createNode('pointOnCurveInfo')
        mc.setAttr(pcinfo+'.parameter', param)
        mc.setAttr(pcinfo+'.turnOnPercentage', 1)
        mc.connectAttr(crv+'.worldSpace', pcinfo+'.inputCurve')

        # now attatch the node to the surface
        cpos = mc.createNode('closestPointOnSurface')
        mc.connectAttr(surf+'.worldSpace', cpos+'.inputSurface')
        mc.connectAttr(pcinfo+'.position', cpos+'.inPosition')

        # Create point on surface info
        psinfo = mc.createNode('pointOnSurfaceInfo')
        mc.connectAttr(surf+'.worldSpace', psinfo+'.inputSurface')
        mc.connectAttr(cpos+'.parameterU', psinfo+'.parameterU')
        mc.connectAttr(cpos+'.parameterV', psinfo+'.parameterV')

        # recreate the new world matrix for node
        mtx = mc.createNode('fourByFourMatrix')

        # normal of surf (X)
        mc.connectAttr(psinfo+'.normalX', mtx+'.i20')
        mc.connectAttr(psinfo+'.normalY', mtx+'.i21')
        mc.connectAttr(psinfo+'.normalZ', mtx+'.i22')

        # tangentU (Y)
        mc.connectAttr(psinfo+'.tangentUx', mtx+'.i10')
        mc.connectAttr(psinfo+'.tangentUy', mtx+'.i11')
        mc.connectAttr(psinfo+'.tangentUz', mtx+'.i12')

        # tangentY (Z)
        mc.connectAttr(psinfo+'.tangentVx', mtx+'.i00')
        mc.connectAttr(psinfo+'.tangentVy', mtx+'.i01')
        mc.connectAttr(psinfo+'.tangentVz', mtx+'.i02')

        # position
        mc.connectAttr(pcinfo+'.positionX', mtx+'.i30')
        mc.connectAttr(pcinfo+'.positionY', mtx+'.i31')
        mc.connectAttr(pcinfo+'.positionZ', mtx+'.i32')

        # get offset
        mult_mtx = mc.createNode('multMatrix')
        dmx = mc.createNode('decomposeMatrix')
        world_drv = mc.createNode('transform', n=node+'_rivet_GRP', p=noxform_grp)
        world_drv_nodes.append(world_drv)

        mc.connectAttr(mtx+'.o', mult_mtx +'.matrixIn[0]')
        mc.connectAttr(world_drv+'.parentInverseMatrix', mult_mtx +'.matrixIn[1]')
        mc.connectAttr(mult_mtx+'.matrixSum', dmx+'.inputMatrix')
        mc.connectAttr(dmx+'.outputTranslate', world_drv+'.t')
        mc.connectAttr(dmx+'.outputRotate', world_drv+'.r')

        mc.pointConstraint(world_drv, node, mo=0, n=node+'_pc')
        mc.orientConstraint(world_drv, node, mo=1, n=node+'_oc')

    return world_drv_nodes

def mesh_mtx(mesh, node, noxform_grp='noXform_GRP', edges=[], use_trianlge_edges=False, constrain=True, create_offset=True):

    node = mc.ls(node)[0]

    shape = utils.get_shapes(mesh)[0]
    edges = mc.ls(edges)

    if mc.nodeType(shape) != 'mesh':
        raise ValueError(shape+' is not a mesh!')

    if not len(edges) == 2:

        # get triangle verts
        pos = mc.xform(node, q=1, ws=1, t=1)

        m_intersect = OpenMaya.MMeshIntersector()
        m_list = OpenMaya.MSelectionList()
        m_list.add(shape)

        shape_dag = m_list.getDependNode(0)
        node_point = OpenMaya.MPoint(pos[0], pos[1], pos[2])
        m_intersect.create(shape_dag)

        point_info = m_intersect.getClosestPoint(node_point)
        face_id = point_info.face
        triangle_id = point_info.triangle

        fnMesh = OpenMaya.MFnMesh(shape_dag)
        verts = fnMesh.getPolygonTriangleVertices(face_id, triangle_id)
        verts = ['{0}.vtx[{1}]'.format(mesh, v) for v in verts]

        # get two edges (this is our backup if the mesh is triangulated)
        face = '{0}.f[{1}]'.format(mesh, face_id)
        face_edges = mc.polyInfo(face, faceToEdge=1)[0].split(':')[1].replace('\n', '')
        face_edges = ['{0}.e[{1}]'.format(mesh, i) for i in re.sub(' +', ' ', face_edges).strip().split(' ')]

        triangle_edges = []
        for edge in face_edges:
            edge_verts = mc.polyInfo(edge, ev=1)[0].split(':')[1].replace('\n', '')
            edge_verts = ['{0}.vtx[{1}]'.format(mesh, i) for i in re.sub(' +', ' ', edge_verts).strip().split(' ')]

            pass_check = True
            for v in edge_verts:
                if mc.objExists(v) and not v in verts:
                    pass_check = False

            if pass_check:
                triangle_edges.append(edge)

        # get the edge ring
        mc.select(triangle_edges[0])
        mm.eval('SelectEdgeRingSp')
        edge_ring = mc.ls(sl=1, fl=1)

        edges = []

        for e in edge_ring:
            if e in face_edges:
                edges.append(e)

        if not len(edges) == 2 and len(triangle_edges) == 2:
            edges = triangle_edges

        # override and use triangle edges
        if use_trianlge_edges and len(triangle_edges) == 2:
            edges = triangle_edges

    if not len(edges) == 2:
        raise ValueError('2 edges were not found or not specified! ')

    # Create curve from edges then loft
    cme1 = mc.createNode('curveFromMeshEdge')
    cme2 = mc.createNode('curveFromMeshEdge')
    loft = mc.createNode('loft')

    edge_id1 = int(edges[0].split('[')[1].split(']')[0])
    edge_id2 = int(edges[1].split('[')[1].split(']')[0])
    mc.setAttr(cme1+'.ei[0]', edge_id1)
    mc.setAttr(cme2+'.ei[0]', edge_id2)
    mc.setAttr(loft+'.uniform', 1)

    mc.connectAttr(shape+'.worldMesh', cme1+'.inputMesh')
    mc.connectAttr(shape+'.worldMesh', cme2+'.inputMesh')

    mc.connectAttr(cme1+'.outputCurve', loft+'.inputCurve[0]')
    mc.connectAttr(cme2+'.outputCurve', loft+'.inputCurve[1]')

    # get u and v parameters
    cpos = mc.createNode('closestPointOnSurface')
    mc.connectAttr(loft+'.outputSurface', cpos+'.inputSurface')
    mc.setAttr(cpos+'.inPositionX', mc.xform(node, q=1, ws=1, t=1)[0])
    mc.setAttr(cpos+'.inPositionY', mc.xform(node, q=1, ws=1, t=1)[1])
    mc.setAttr(cpos+'.inPositionZ', mc.xform(node, q=1, ws=1, t=1)[2])

    param_u = max(mc.getAttr(cpos+'.parameterU'), 0.001)
    param_v = max(mc.getAttr(cpos+'.parameterV'), 0.001)

    # Create point on surface info
    psinfo = mc.createNode('pointOnSurfaceInfo')
    mc.connectAttr(loft+'.outputSurface', psinfo+'.inputSurface')
    mc.setAttr(psinfo+'.parameterU', param_u)
    mc.setAttr(psinfo+'.parameterV', param_v)
    mc.delete(cpos)

    # recreate the new world matrix for node
    mtx = mc.createNode('fourByFourMatrix')
    mc.connectAttr(psinfo+'.normalX', mtx+'.i00')
    mc.connectAttr(psinfo+'.normalY', mtx+'.i01')
    mc.connectAttr(psinfo+'.normalZ', mtx+'.i02')
    mc.connectAttr(psinfo+'.tangentUx', mtx+'.i10')
    mc.connectAttr(psinfo+'.tangentUy', mtx+'.i11')
    mc.connectAttr(psinfo+'.tangentUz', mtx+'.i12')
    mc.connectAttr(psinfo+'.tangentVx', mtx+'.i20')
    mc.connectAttr(psinfo+'.tangentVy', mtx+'.i21')
    mc.connectAttr(psinfo+'.tangentVz', mtx+'.i22')
    mc.connectAttr(psinfo+'.positionX', mtx+'.i30')
    mc.connectAttr(psinfo+'.positionY', mtx+'.i31')
    mc.connectAttr(psinfo+'.positionZ', mtx+'.i32')

    # get offset
    mult_mtx = mc.createNode('multMatrix')
    dmx = mc.createNode('decomposeMatrix')
    world_drv = mc.createNode('transform', n=node+'_rivet_GRP', p=noxform_grp)

    mc.connectAttr(mtx+'.o', mult_mtx +'.matrixIn[0]')
    mc.connectAttr(world_drv+'.parentInverseMatrix', mult_mtx +'.matrixIn[1]')
    mc.connectAttr(mult_mtx+'.matrixSum', dmx+'.inputMatrix')
    mc.connectAttr(dmx+'.outputTranslate', world_drv+'.t')
    mc.connectAttr(dmx+'.outputRotate', world_drv+'.r')

    # parent constrain node
    if constrain:
        con_node = world_drv
        if create_offset:
            con_node = mc.duplicate(node, n=node+'_rivet_OFF', po=1)[0]
            utils.set_attrs(con_node, k=1, l=0)
            mc.parent(con_node, world_drv)

        prc = mc.parentConstraint(con_node, node, mo=1)[0]
        return prc

    return world_drv

def curve_mtx(crv, nodes):

    nodes = mc.ls(nodes)
    world_drv_nodes = []

    for node in nodes:

        # get parameter
        pos = mc.xform(node, q=1, ws=1, t=1)
        npoc = mc.createNode('nearestPointOnCurve')

        mc.connectAttr(crv+'.worldSpace', npoc+'.inputCurve')
        mc.setAttr(npoc+'.inPosition', pos[0], pos[1], pos[2])
        param = mc.getAttr(npoc+'.parameter')
        mc.delete(npoc)

        # create point on curve info and word drv node
        pcinfo = mc.createNode('pointOnCurveInfo', n=crv+'_cinfo')
        mc.setAttr(pcinfo+'.parameter', param)
        mc.setAttr(pcinfo+'.turnOnPercentage', 0)
        mc.connectAttr(crv+'.worldSpace', pcinfo+'.inputCurve')

        # Aim constraint to node
        aim = mc.createNode('aimConstraint', n=node+'_ac')
        mc.connectAttr(pcinfo+'.tangent', aim+'.tg[0].tt')
        mc.connectAttr(aim+'.cr', node+'.r')

        mc.connectAttr(pcinfo+'.position', node+'.t')
        mc.parent(aim, node)

def curve_mtx2(crv, node, parent_inv=None, upv=None):

    if not parent_inv:
        parent_inv = node

    # get parameter
    pos = mc.xform(node, q=1, ws=1, t=1)
    npoc = mc.createNode('nearestPointOnCurve')

    dmtx = mc.createNode('decomposeMatrix')
    mmtx = mc.createNode('multMatrix')
    mtx = mc.createNode('fourByFourMatrix')


    mc.connectAttr(crv+'.worldSpace', npoc+'.inputCurve')
    mc.setAttr(npoc+'.inPosition', pos[0], pos[1], pos[2])
    param = mc.getAttr(npoc+'.parameter')
    mc.delete(npoc)

    # create point on curve info and word drv node
    pcinfo = mc.createNode('pointOnCurveInfo', n=crv+'_cinfo')
    mc.setAttr(pcinfo+'.parameter', param)
    mc.setAttr(pcinfo+'.turnOnPercentage', 0)
    mc.connectAttr(crv+'.worldSpace', pcinfo+'.inputCurve')

    # recreate the new world matrix for node
    mc.connectAttr(pcinfo+'.tangentX', mtx+'.i00')
    mc.connectAttr(pcinfo+'.tangentY', mtx+'.i01')
    mc.connectAttr(pcinfo+'.tangentZ', mtx+'.i02')

    mc.setAttr(mtx+'.i10', 0)
    mc.setAttr(mtx+'.i11', 1)
    mc.setAttr(mtx+'.i12', 0)
    mc.setAttr(mtx+'.i20', 0)
    mc.setAttr(mtx+'.i21', 0)
    mc.setAttr(mtx+'.i22', 1)

    mc.connectAttr(pcinfo+'.positionX', mtx+'.i30')
    mc.connectAttr(pcinfo+'.positionY', mtx+'.i31')
    mc.connectAttr(pcinfo+'.positionZ', mtx+'.i32')

    # build constraint
    mc.connectAttr(mtx+'.o', mmtx+'.matrixIn[1]')
    mc.connectAttr(parent_inv+'.parentInverseMatrix', mmtx+'.matrixIn[2]')
    mc.connectAttr(mmtx+'.matrixSum', dmtx+'.inputMatrix')

    mc.connectAttr(dmtx+'.outputTranslate', node+'.t', f=1)
    if upv:
        mc.connectAttr(dmtx+'.outputRotate', node+'.r', f=1)


def surface_mtx2(surf, node, parent_inv=None, mo=1, percentage=0):

    if not parent_inv:
        parent_inv = node

    psinfo = mc.createNode('pointOnSurfaceInfo', n=node+'_mrivet')
    dmtx = mc.createNode('decomposeMatrix')
    mmtx = mc.createNode('multMatrix')
    mtx = mc.createNode('fourByFourMatrix')

    # get u and v param
    cpos = mc.createNode('closestPointOnSurface')
    mc.connectAttr(surf+'.worldSpace', cpos+'.inputSurface')
    mc.setAttr(cpos+'.inPositionX', mc.xform(node, q=1, ws=1, t=1)[0])
    mc.setAttr(cpos+'.inPositionY', mc.xform(node, q=1, ws=1, t=1)[1])
    mc.setAttr(cpos+'.inPositionZ', mc.xform(node, q=1, ws=1, t=1)[2])

    #param_u = max(mc.getAttr(cpos+'.parameterU'), 0.001)
    #param_v = max(mc.getAttr(cpos+'.parameterV'), 0.001)

    param_u = mc.getAttr(cpos+'.parameterU')
    param_v = mc.getAttr(cpos+'.parameterV')

    mc.delete(cpos)

    # Create point on surface info
    mc.connectAttr(surf+'.worldSpace', psinfo+'.inputSurface')
    mc.setAttr(psinfo+'.parameterU', param_u)
    mc.setAttr(psinfo+'.parameterV', param_v)
    mc.setAttr(psinfo+'.turnOnPercentage', percentage)

    mc.setAttr(psinfo+'.parameterU', k=1)
    mc.setAttr(psinfo+'.parameterV', k=1)
    mc.setAttr(psinfo+'.turnOnPercentage', k=1)

    # recreate the new world matrix for node
    mc.connectAttr(psinfo+'.normalX', mtx+'.i00')
    mc.connectAttr(psinfo+'.normalY', mtx+'.i01')
    mc.connectAttr(psinfo+'.normalZ', mtx+'.i02')
    mc.connectAttr(psinfo+'.tangentUx', mtx+'.i10')
    mc.connectAttr(psinfo+'.tangentUy', mtx+'.i11')
    mc.connectAttr(psinfo+'.tangentUz', mtx+'.i12')
    mc.connectAttr(psinfo+'.tangentVx', mtx+'.i20')
    mc.connectAttr(psinfo+'.tangentVy', mtx+'.i21')
    mc.connectAttr(psinfo+'.tangentVz', mtx+'.i22')
    mc.connectAttr(psinfo+'.positionX', mtx+'.i30')
    mc.connectAttr(psinfo+'.positionY', mtx+'.i31')
    mc.connectAttr(psinfo+'.positionZ', mtx+'.i32')

    # add some attrs
    mc.addAttr(dmtx, ln='surf', at='enum', k=0, en=surf)
    mc.setAttr(dmtx+'.surf', cb=1)

    # setuo offset
    if mo:
        tmp_dmx = mc.createNode('decomposeMatrix')
        world_tmp = mc.duplicate(node, po=1)[0]
        utils.set_attrs(node, 't r s shear shearX shearY shearZ', l=0, k=1)

        mc.connectAttr(mtx+'.o', tmp_dmx+'.inputMatrix')
        mc.connectAttr(tmp_dmx+'.outputTranslate', world_tmp+'.t')
        mc.connectAttr(tmp_dmx+'.outputRotate', world_tmp+'.r')
        mc.connectAttr(tmp_dmx+'.outputScale', world_tmp+'.s')
        mc.connectAttr(tmp_dmx+'.outputShear', world_tmp+'.shear')

        offset = get_offset(world_tmp, node)
        offset = [round(offset(i, j), 4) for i in range(4) for j in range(4)]
        mc.setAttr(mmtx+'.matrixIn[0]', offset, type='matrix')
        mc.disconnectAttr(mtx+'.o', tmp_dmx+'.inputMatrix')
        mc.delete(tmp_dmx, world_tmp)

    # build constraint
    mc.connectAttr(mtx+'.o', mmtx+'.matrixIn[1]')
    mc.connectAttr(parent_inv+'.parentInverseMatrix', mmtx+'.matrixIn[2]')
    mc.connectAttr(mmtx+'.matrixSum', dmtx+'.inputMatrix')
    mc.setAttr(mmtx+'.ihi', 0)

    mc.connectAttr(dmtx+'.outputTranslate', node+'.t', f=1)
    mc.connectAttr(dmtx+'.outputRotate', node+'.r', f=1)

    mc.setAttr(dmtx+'.ihi', 0)
    mc.setAttr(mmtx+'.ihi', 0)
    mc.setAttr(mtx+'.ihi', 0)

def get_offset(nodeA, nodeB):

    def getDagPath(node=None):
        sel = om.MSelectionList()
        sel.add(node)
        d = om.MDagPath()
        sel.getDagPath(0, d)
        return d

    mtxA = getDagPath(nodeA).inclusiveMatrix()
    mtxB = getDagPath(nodeB).inclusiveMatrix()

    return mtxB * mtxA.inverse()



def orient_surf_mtx(surf, ik_jnt, jnt, parent_inv=None, mo=True):
    '''Orient constrain nodes to closest point on nurbs surface using matrix nodes.'''

    if not parent_inv:
        parent_inv = jnt

    dmx = mc.createNode('decomposeMatrix')
    mc.connectAttr(ik_jnt+'.worldMatrix', dmx+'.inputMatrix')

    cpos = mc.createNode('closestPointOnSurface')
    mc.connectAttr(surf+'.worldSpace', cpos+'.inputSurface')
    mc.connectAttr(dmx+'.outputTranslate',cpos+'.inPosition')

    psinfo = mc.createNode('pointOnSurfaceInfo', n=jnt+'_mrivet')
    dmtx = mc.createNode('decomposeMatrix')
    mmtx = mc.createNode('multMatrix')
    mtx = mc.createNode('fourByFourMatrix')

    # Create point on surface info
    mc.connectAttr(surf+'.worldSpace', psinfo+'.inputSurface')
    mc.connectAttr(cpos+'.parameterU', psinfo+'.parameterU')
    mc.connectAttr(cpos+'.parameterV', psinfo+'.parameterV')
    mc.setAttr(psinfo+'.turnOnPercentage', 0)
    mc.setAttr(psinfo+'.turnOnPercentage', k=1)

    # recreate the new world matrix for node
    mc.connectAttr(psinfo+'.normalX', mtx+'.i00')
    mc.connectAttr(psinfo+'.normalY', mtx+'.i01')
    mc.connectAttr(psinfo+'.normalZ', mtx+'.i02')
    mc.connectAttr(psinfo+'.tangentUx', mtx+'.i10')
    mc.connectAttr(psinfo+'.tangentUy', mtx+'.i11')
    mc.connectAttr(psinfo+'.tangentUz', mtx+'.i12')
    mc.connectAttr(psinfo+'.tangentVx', mtx+'.i20')
    mc.connectAttr(psinfo+'.tangentVy', mtx+'.i21')
    mc.connectAttr(psinfo+'.tangentVz', mtx+'.i22')
    mc.connectAttr(psinfo+'.positionX', mtx+'.i30')
    mc.connectAttr(psinfo+'.positionY', mtx+'.i31')
    mc.connectAttr(psinfo+'.positionZ', mtx+'.i32')

    if mo:
        tmp_dmx = mc.createNode('decomposeMatrix')
        world_tmp = mc.duplicate(jnt, po=1)[0]
        utils.set_attrs(jnt, 't r s shear shearX shearY shearZ', l=0, k=1)

        mc.connectAttr(mtx+'.o', tmp_dmx+'.inputMatrix')
        mc.connectAttr(tmp_dmx+'.outputTranslate', world_tmp+'.t')
        mc.connectAttr(tmp_dmx+'.outputRotate', world_tmp+'.r')
        mc.connectAttr(tmp_dmx+'.outputScale', world_tmp+'.s')
        mc.connectAttr(tmp_dmx+'.outputShear', world_tmp+'.shear')

        offset = get_offset(world_tmp, jnt)
        offset = [round(offset(i, j), 4) for i in range(4) for j in range(4)]
        mc.setAttr(mmtx+'.matrixIn[0]', offset, type='matrix')
        mc.disconnectAttr(mtx+'.o', tmp_dmx+'.inputMatrix')
        mc.delete(tmp_dmx, world_tmp)

    # build constraint
    mc.connectAttr(mtx+'.o', mmtx+'.matrixIn[1]')
    mc.connectAttr(parent_inv+'.parentInverseMatrix', mmtx+'.matrixIn[2]')
    mc.connectAttr(mmtx+'.matrixSum', dmtx+'.inputMatrix')
    mc.setAttr(mmtx+'.ihi', 0)

    mc.connectAttr(dmtx+'.outputRotate', jnt+'.r', f=1)
