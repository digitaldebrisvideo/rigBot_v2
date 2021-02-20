# -*- coding: utf-8 -*-
"""Functions for connecting nodes to spline rigs."""

from maya import OpenMaya as om
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import rivet
import os

reload(utils)

def create_ramp_cluster_weight(cluster, ramp):
    """Create an expression to drive the weights of a cluster with a ramp node

        Kwargs:
            :cluster: (str) cluster node
            :ramp: (str) ramp node
    """

    crv = mc.cluster(cluster, q=1, g=1)
    numCVs = len(mc.ls(crv[0]+'.cv[*]', fl=1))

    arg = '''
    vector $dummy = {1}.outAlpha;
    float $output[];
    for ($i=0; $i < {2}; $i++)
    {3}
        float $j = $i;
        float $pos = ($j / {2});
        float $value[] = `colorAtPoint -o A -u 0.5 -v $pos {1}`;
        $output[$i] = $value[0];
    {4}
    '''.format(cluster, ramp, numCVs, '{','}')

    for i in range(numCVs):
        arg += '{0}.weightList[0].weights[{1}] = $output[{1}];\n'.format(cluster, i)

    mc.expression(n=cluster+'_weight_EXP', s=arg, ae=False)

'''
def create_spline_plugin_node(nodes, crv, surf, aimMode=False, scaleDrivers=[], scaleDriverAttr='sy', interpolation='smooth'):
    """Create a cmSplineChain node, set params and connect nodes..

        Note: Nodes must be in world space, in a fglattened hierarchy.

        Args:
            :nodes: (list) Nodes to connect to spline.
            :crv: (str) Input curve
            :surf: (str) Input surface

        Kwargs:
            :aimMode: (bool) If true, driven nodes will aim at the proceeding node. Otherwise they will aim parallel to the curve tangent.
            :scaleDrivers: (list) Driving nodes for segmented scale.
            :scaleDriverAttr: (str) Driving attribute for scale. Defaults to "sy".
            :interpolation: (str) Ramp interpolation. Defaults to "smooth".

        Returns:
            :cmSplineChain: (str) Name of the cmSplineChain node."""

    print crv

    surfShape =utils.get_shapes(surf)[0]
    crvShape = utils.get_shapes(crv)[0]

    alen = mc.arclen(crvShape, ch=0)
    maxParam = mc.getAttr(crvShape+'.spans')

    gsc = mc.createNode('cmSplineChain', n=crv.replace('_crv','')+'_gsc')
    mc.setAttr(gsc+'.initCurveLength', alen)
    mc.setAttr(gsc+'.numberOfOutputs', len(nodes))
    mc.connectAttr(crvShape+'.worldSpace', gsc+'.inCurve')
    mc.connectAttr(surfShape+'.worldSpace', gsc+'.inSurface')
    mc.setAttr(gsc+'.aimMode', aimMode)

    sel = om.MSelectionList()
    sel.add(crvShape)
    sel.add(surfShape)
    crvObj = om.MDagPath()
    surfObj = om.MDagPath()
    sel.getDagPath(0, crvObj)
    sel.getDagPath(1, surfObj)
    crvFn = om.MFnNurbsCurve(crvObj)
    surfFn = om.MFnNurbsSurface(surfObj)

    div = 1.0 / (len(nodes) -1)
    pval = 0.0

    for i, node in enumerate(nodes):

        nupVal = crvFn.findParamFromLength(pval)
        mc.setAttr('{0}.paramValues[{1}]'.format(gsc, i), pval)
        mc.setAttr('{0}.nonUniformParamValues[{1}]'.format(gsc, i), nupVal)

        if node != nodes[-1]:
            dst = utils.get_distance(node, nodes[i+1])
            mc.setAttr('{0}.initJointDistanceValues[{1}]'.format(gsc, i), dst)
            pval += dst

    mc.setAttr('{0}.initJointDistanceValues[{1}]'.format(gsc, i), dst)

    for i, node in enumerate(nodes):
        mc.connectAttr('{0}.outTranslate[{1}]'.format(gsc, i), node+'.t')
        mc.connectAttr('{0}.outRotate[{1}]'.format(gsc, i), node+'.r')

    # create ramps
    if scaleDrivers:

        interp = 4
        if interpolation == 'linear':
            interp = 1

        ramps = []
        div = 1.0 / (len(scaleDrivers)-1)

        for i, sdrv in enumerate(scaleDrivers):
            prePos = max(min(1, (i-1)*div), 0)
            postPos = max(min(1, (i+1)*div), 0)
            currentPos = i*div

            ramp = mc.createNode('ramp', n=sdrv+'_ramp')
            mc.setAttr(ramp+'.colorEntryList[0].color', 0,0,0, type='double3')
            mc.setAttr(ramp+'.colorEntryList[1].color', 1,1,1,type='double3')
            mc.setAttr(ramp+'.colorEntryList[2].color', 0,0,0, type='double3')
            mc.setAttr(ramp+'.colorEntryList[0].position', prePos)
            mc.setAttr(ramp+'.colorEntryList[1].position', currentPos)
            mc.setAttr(ramp+'.colorEntryList[2].position', postPos)
            mc.setAttr(ramp+'.interpolation', interp)
            ramps.append(ramp)

            mc.connectAttr(sdrv+'.'+scaleDriverAttr, '{0}.scaleDrivers[{1}]'.format(gsc, i))

        mc.removeMultiInstance(ramps[0]+'.colorEntryList[0]', b=True)
        mc.removeMultiInstance(ramps[-1]+'.colorEntryList[2]', b=True)

        # read ramps and create scales
        dst=0
        for ii, dnode in enumerate(nodes):
            dst += mc.getAttr('{0}.initJointDistanceValues[{1}]'.format(gsc, ii))

        div = 1.0 / (dst)
        div2 = 0
        idx = 0

        for ii, dnode in enumerate(nodes):
            div2 += mc.getAttr('{0}.initJointDistanceValues[{1}]'.format(gsc, ii))
            pos = div2*div
            for i, ramp in enumerate(ramps):
                mc.setAttr(ramp+'.vCoord', pos)
                value = mc.getAttr(ramp+'.outColorR')
                mc.setAttr('{0}.scaleRampValues[{1}]'.format(gsc, idx), value)
                idx += 1

        mc.delete(ramps)

    return gsc

def connect_spline(nodes, crv, surf, pc=True, oc=True, sc=True, mo=True, aimMode=False, scaleDriverAttr='sy', scaleAttrs=['sy','sz'], scaleDrivers=[], scaleNodes=[], noXform='noXform', world_scale_attr=None, use_plugin=None):
    """This is the interfacing function to create a spline rig, optionally use pplugin nodes OR build as a vanilla maya rig.

        Args:
            :nodes: (list) Driven nodes
            :crv: (str) Input curve.
            :surf: (str) Input surface.

        Kwargs:
            :pc: (bool) Use pointConstraints. Defaults to True.
            :oc: (bool) Use orientConstraints. Defaults to True.
            :sc: (bool) Use scaleConstraints. Defaults to True.
            :mo: (bool) maintain offsets for constraints. Defaults to True.
            :aimMode: (bool) If true, driven nodes will aim at the proceeding node. Otherwise they will aim parallel to the curve tangent. Defaults to False.
            :scaleDriverAttr: (str) Driving attribute for scale. Defaults to 'sy'.
            :scaleAttrs: (list) Driven scale attributes. Defaults to ['sy','sz'].
            :scaleDrivers: (list) Driving nodes for segmented scale. Defaults to [].
            :scaleNodes: (list) Driven scale nodes. Defaults to [].
            :noXform: (str) . No transform group for parenting to the rig. Defaults to 'noXform'.
            :world_scale_attr: (str) Master uniform scale driver for proper scaling.. Defaults to None.
            :use_plugin: (bool) Use plugin nodes. Defaults to None."""

    if use_plugin is None:

        if os.environ['use_plugin_nodes'] == 'True':
            use_plugin = True
        else:
            use_plugin = False

    print 'USE_PLUGIN_NODES: '+str(use_plugin)

    if use_plugin:
        return connect_spline_plugin(nodes, crv, surf, pc, oc, sc, mo, aimMode, scaleDriverAttr, scaleAttrs, scaleDrivers, scaleNodes, noXform, world_scale_attr)

    else:
        return connect_spline_vanilla(nodes, crv, surf, pc, oc, sc, mo, aimMode, scaleDriverAttr, scaleAttrs, scaleDrivers, scaleNodes, noXform, world_scale_attr)

def connect_spline_plugin(nodes, crv, surf, pc=True, oc=True, sc=True, mo=True, aimMode=False, scaleDriverAttr='sy', scaleAttrs=['sy','sz'], scaleDrivers=[], scaleNodes=[], noXform='noXform', world_scale_attr=None):
    """Connect nodes to using cmSplineChain node.

        Args:
            :nodes: (list) Driven nodes
            :crv: (str) Input curve.
            :surf: (str) Input surface.

        Kwargs:
            :pc: (bool) Use pointConstraints. Defaults to True.
            :oc: (bool) Use orientConstraints. Defaults to True.
            :sc: (bool) Use scaleConstraints. Defaults to True.
            :mo: (bool) maintain offsets for constraints. Defaults to True.
            :aimMode: (bool) If true, driven nodes will aim at the proceeding node. Otherwise they will aim parallel to the curve tangent. Defaults to False.
            :scaleDriverAttr: (str) Driving attribute for scale. Defaults to 'sy'.
            :scaleAttrs: (list) Driven scale attributes. Defaults to ['sy','sz'].
            :scaleDrivers: (list) Driving nodes for segmented scale. Defaults to [].
            :scaleNodes: (list) Driven scale nodes. Defaults to [].
            :noXform: (str) . No transform group for parenting to the rig. Defaults to 'noXform'.
            :world_scale_attr: (str) Master uniform scale driver for proper scaling.. Defaults to None."""

    crv1 = crv.replace('_0_', '_1_')
    if mc.objExists(crv1) and crv1 != crv:
        mc.delete(crv1)

    if not nodes:
        return

    if not mc.objExists(noXform):
        noXform = mc.createNode('transform', n=noXform)

    worldDrvs =[]
    for node in nodes:
        wd = mc.createNode('transform', n=node+'_WORLD_DRV')
        mc.delete(mc.pointConstraint(node, wd))
        mc.delete(mc.orientConstraint(node, wd))
        mc.parent(wd, noXform)
        worldDrvs.append(wd)

    gsc = create_spline_plugin_node(worldDrvs, crv, surf, aimMode=aimMode, scaleDrivers=scaleDrivers, scaleDriverAttr=scaleDriverAttr)
    for i, wd in enumerate(worldDrvs):
        if pc:
            mc.pointConstraint(wd, nodes[i], n=nodes[i]+'_pc', mo=mo)
        if oc:
            follow_par = mc.duplicate(nodes[i], po=1, n=wd+'_follow_PAR')[0]
            follow = mc.duplicate(nodes[i], po=1, n=wd+'_follow')[0]

            mc.parent(follow, follow_par)
            mc.parent(follow_par, wd)

            mc.orientConstraint(follow, nodes[i], n=nodes[i]+'_oc', mo=mo)

    if sc and scaleDrivers and scaleNodes:
        for i, node in enumerate(scaleNodes):
            for attr in scaleAttrs:
                mc.connectAttr('{0}.outScale[{1}]'.format(gsc, i), node+'.'+attr)

    if world_scale_attr:
        mc.connectAttr(world_scale_attr, gsc+'.globalScale')

    return gsc

def connect_spline_vanilla(nodes, crv, surf, pc=True, oc=True, sc=True, mo=True, aimMode=False, scaleDriverAttr='sy', scaleAttrs=['sy','sz'], scaleDrivers=[], scaleNodes=[], noXform='noXform', world_scale_attr=None):
    """Connect nodes using vanilla maya nodes.

        Args:
            :nodes: (list) Driven nodes
            :crv: (str) Input curve.
            :surf: (str) Input surface.

        Kwargs:
            :pc: (bool) Use pointConstraints. Defaults to True.
            :oc: (bool) Use orientConstraints. Defaults to True.
            :sc: (bool) Use scaleConstraints. Defaults to True.
            :mo: (bool) maintain offsets for constraints. Defaults to True.
            :aimMode: (bool) If true, driven nodes will aim at the proceeding node. Otherwise they will aim parallel to the curve tangent. Defaults to False.
            :scaleDriverAttr: (str) Driving attribute for scale. Defaults to 'sy'.
            :scaleAttrs: (list) Driven scale attributes. Defaults to ['sy','sz'].
            :scaleDrivers: (list) Driving nodes for segmented scale. Defaults to [].
            :scaleNodes: (list) Driven scale nodes. Defaults to [].
            :noXform: (str) . No transform group for parenting to the rig. Defaults to 'noXform'.
            :world_scale_attr: (str) Master uniform scale driver for proper scaling.. Defaults to None."""

    if not nodes:
        return

    if not mc.objExists(noXform):
        noXform = mc.createNode('transform', n=noXform)

    if mc.objExists(surf):
        surf_parent = utils.get_parent(surf)
        mc.delete(surf)

    crv0 = crv
    crv1 = crv.replace('_0_', '_1_')
    create_stretch_crv(crv0)
    create_stretch_crv(crv1)

    surf = mc.rename(mc.loft(crv0, crv1)[0], surf)
    mc.parent(surf, surf_parent)

    mc.addAttr(crv0, ln='aimMode', at='bool')
    mc.addAttr(crv0, ln='preserveVolume', k=1, min=0, max=1, dv=0.5)
    mc.addAttr(crv0, ln='preserveVolumeMin', k=1, min=0.01, max=1, dv=0.2)
    mc.addAttr(crv0, ln='preserveVolumeMax', k=1, min=1, max=10, dv=4)

    if world_scale_attr:
        mc.connectAttr(world_scale_attr, crv0+'.globalScale')

    worldDrvs = rivet.curve_surf_mtx(crv0, surf, nodes, noXform)

    attrs = ['.stretch', '.uniformStretch', '.reverseRoot', '.offset', '.globalScale']
    for a in attrs:
        mc.connectAttr(crv0+a, crv1+a)

    if scaleDrivers and scaleNodes:
        scale_ramp_sdk(scaleDrivers, scaleNodes, driver_attr=scaleDriverAttr, driven_attrs=scaleAttrs)
        preserve_volume(worldDrvs, scaleNodes[1:-1], crv0, scaleAttrs)

    return crv0
'''

def connect_shift(driver, nodes, length, param_attr='paramLength'):
    """Connect nodes to a shift attribute. cmSplineChain only.

        Args:
            :driver: (str) Driver attribute.
            :gsc: (str) cmSplineChain node name.
            :nodes: (list) Driven nodes.
            :length: (float) initial curve length."""

    ramp = mc.createNode ('ramp')
    mc.setAttr(ramp+'.colorEntryList[0].color', 0,0,0, type='double3')
    mc.setAttr(ramp+'.colorEntryList[1].color', 1,1,1, type='double3')
    mc.setAttr(ramp+'.colorEntryList[0].position', 0 )
    mc.setAttr(ramp+'.colorEntryList[1].position', 1)

    div = 1.0 / (len(nodes) - 1)

    # get values when shift is set to 0
    default_values = []
    mc.setAttr(ramp+'.interpolation', 1)
    for i, zero in enumerate(nodes):
        value = mc.colorAtPoint(ramp, o='A', u=0.5, v=div*i)[0]
        default_values.append(value*length)

    # get values when shift is set to 1
    shift_up_values = []
    mc.setAttr(ramp+'.interpolation', 3)
    for i, zero in enumerate(nodes):
        value = mc.colorAtPoint(ramp, o='A', u=0.5, v=div*i)[0]
        shift_up_values.append(value*length)

    # get values when shift is set to -1
    shift_down_values = []
    mc.setAttr(ramp+'.interpolation', 2)
    for i, zero in enumerate(nodes):
        value = mc.colorAtPoint(ramp, o='A', u=0.5, v=div*i)[0]
        shift_down_values.append(value*length)

    for i, node in enumerate(nodes):

        driven_attr = '{0}.{1}'.format(node, param_attr)
        df_val = default_values[i]
        up_val = shift_up_values[i]
        lo_val = shift_down_values[i]

        # sdk shift
        mc.setDrivenKeyframe(driven_attr, cd=driver, dv=0, v=df_val, itt='linear', ott='linear')
        mc.setDrivenKeyframe(driven_attr, cd=driver, dv=1, v=up_val, itt = 'linear', ott='linear')
        mc.setDrivenKeyframe(driven_attr, cd=driver, dv=-1, v=lo_val, itt = 'linear', ott='linear')

    mc.delete(ramp)

def create_curve_mtx(ctrls, name='crv', degree=2, axis='X', offset=0.0, parent='noXform_GRP'):
    """Create a lofted ribbon and surface from ctrls. Uses decompose matrix nodes to drive the curve and surface points.surface

        Args:
            :ctrls: (list) Controls to drive the surface and curve
            :name: (str) Name for the new curve and surf

        Kwargs:
            :degree: (int) Degree of the new curve and surface. Defaults to 3
            :parent: (str) No transform group to parent nodes. Defaults to "noXform_GRP" """

    # Create crvs
    crv = mc.curve(n=name+'_CRV', d=degree, p=[[0,0,0]]*len(ctrls))
    shape = mc.rename(utils.get_shapes(crv)[0], crv+'Shape')

    # connect crvs
    for i, ctrl in enumerate(ctrls):

        loc = mc.createNode('locator', p=ctrl, n=ctrl+'_0_loft_locShape')
        cPoint = '{0}.controlPoints[{1}]'.format(shape, i)

        mc.connectAttr(loc+'.worldPosition', cPoint)
        mc.setAttr(loc+'.localPosition'+axis.upper(), offset)
        mc.setAttr(loc+'.io', 1)

    if mc.objExists(parent):
        mc.parent(crv, parent)

    return str(crv)

def create_surface_mtx(ctrls, name='surf', degree=2, axis='X', width=0, parent='noXform_GRP', stretch=False):
    """Create a lofted ribbon and surface from ctrls. Uses decompose matrix nodes to drive the curve and surface points.surface

        Args:
            :ctrls: (list) Controls to drive the surface and curve
            :name: (str) Name for the new curve and surf

        Kwargs:
            :degree: (int) Degree of the new curve and surface. Defaults to 3
            :axis: (str) Axis for the width of the surface. Defaults to 'Y'.
            :width: (float) Width of the surface. Defaults to 0.1.
            :parent: (str) No transform group to parent nodes. Defaults to "noXform_GRP" """

    if not width:
        width = utils.get_distance(ctrls[0], ctrls[1]) * 0.1

    # Create crvs
    crv0 = mc.curve(n=name+'_0_CRV', d=degree, p=[[0,0,0]]*len(ctrls))
    crv1 = mc.curve(n=name+'_1_CRV', d=degree, p=[[0,0,0]]*len(ctrls))

    shape0 = mc.rename(utils.get_shapes(crv0)[0], crv0+'Shape')
    shape1 = mc.rename(utils.get_shapes(crv1)[0], crv1+'Shape')

    # connect crvs
    for i, ctrl in enumerate(ctrls):

        loc0 = mc.createNode('locator', p=ctrl, n=ctrl+'_0_loft_locShape')
        loc1 = mc.createNode('locator', p=ctrl, n=ctrl+'_1_loft_locShape')

        mc.setAttr(loc0+'.localPosition'+axis.upper(), width * 0.5)
        mc.setAttr(loc1+'.localPosition'+axis.upper(), width * -0.5)

        cPoint0 = '{0}.controlPoints[{1}]'.format(shape0, i)
        cPoint1 = '{0}.controlPoints[{1}]'.format(shape1, i)

        mc.connectAttr(loc0+'.worldPosition', cPoint0)
        mc.connectAttr(loc1+'.worldPosition', cPoint1)

        mc.setAttr(loc0+'.io', 1)
        mc.setAttr(loc1+'.io', 1)

    if stretch:
        crv0 = create_stretch_crv(crv0)
        crv1 = create_stretch_crv(crv1)

    surf = mc.loft(crv1, crv0, n=name+'_SURF')[0]

    if stretch:
        mc.parent(crv0, crv1, surf, r=1, s=1)

        attrs = ['stretch','uniformStretch','reverseRoot']
        for a in attrs:
            mc.addAttr(surf, ln=a, min=0, max=1, k=1)
            mc.connectAttr(surf+'.'+a, crv0+'.'+a)
            mc.connectAttr(surf+'.'+a, crv1+'.'+a)


    else:
        mc.parent(shape0, shape1, surf, r=1, s=1)
        mc.setAttr(shape0+'.io', 1)
        mc.setAttr(shape1+'.io', 1)
        mc.delete(crv0, crv1)

    if mc.objExists(parent):
        mc.parent(surf, parent)

    return str(surf)

def create_stretch_crv(crv, globalScale='world_CTL.worldScale'):
    """Legacy function for creating an stretchy nurbs surface. (No plugin nodes)

        Args:
            :surf: (str) Input nurbs surface"""

    shape = utils.get_shapes(crv)[0]

    #create attrs
    mc.addAttr(crv, ln='stretch', at='double', min=0, max=1, k=1 )
    mc.addAttr(crv, ln='uniformStretch', at='double', k=1, min=0, max=1)
    mc.addAttr(crv, ln='reverseRoot', at='double', k=1, min=0, max=1)
    mc.addAttr(crv, ln='offset', at='double', k=1)
    mc.addAttr(crv, ln='globalScale', at='double', min=0, dv=1)

    # initial more blendAttr for forcing uniform on when stretch is on
    uniform_bta = mc.createNode('blendTwoAttr')
    mc.setDrivenKeyframe(uniform_bta+'.attributesBlender', cd=crv+'.stretch',
                         dv=0, v=0, itt='flat', ott='flat')

    mc.setDrivenKeyframe(uniform_bta+'.attributesBlender', cd=crv+'.stretch',
                         dv=1, v=1, itt='flat', ott='flat')

    mc.addAttr(uniform_bta, ln='staticVal', dv=1)
    mc.connectAttr(uniform_bta+'.staticVal', uniform_bta+'.input[0]')
    mc.connectAttr(crv+'.uniformStretch', uniform_bta+'.input[1]')

    orig_crv = crv
    prefix = crv.split('_CRV')[0]

    # rebuild to make new uniform crv
    knots = mc.getAttr(orig_crv+'.spans')
    degree = mc.getAttr(orig_crv+'.degree')
    rebuild_crv = mc.rebuildCurve(crv,
        ch=1,
        rpo=0,
        rt=0,
        end=1,
        kr=0,
        kcp=0,
        kep=1,
        kt=0,
        s=knots,
        d=degree,
        tol=0.01)

    uniform_crv = mc.rename(rebuild_crv[0], crv+'Uniform')

    # create blend Crv
    blend_crv = mc.duplicate(uniform_crv, n=crv+'Blend')[0]

    avc = mc.createNode('avgCurves')
    mc.connectAttr(shape+'.worldSpace', avc+'.ic1')
    mc.connectAttr(uniform_crv+'Shape.worldSpace', avc+'.ic2')
    mc.connectAttr(avc+'.oc', blend_crv+'Shape.create')
    mc.setAttr (avc+'.automaticWeight', 0)

    rv = mc.createNode('reverse')
    mc.connectAttr(uniform_bta+'.output', rv+'.inputX')
    mc.connectAttr(rv+'.outputX', avc+'.w1')
    mc.connectAttr(uniform_bta+'.output', avc+'.w2')

    # create cut curve (for loft)
    dcrvs = mc.detachCurve(blend_crv, p=(0.001, .999 ), ch=1, cos=1, rpo=0)
    detatch_node = dcrvs[3]

    detatch_crv = mc.rename(dcrvs[1], crv+'Detatch')
    mc.delete(dcrvs[0], dcrvs[2])

    # create curv info scale multiplier
    info = mc.arclen(uniform_crv, ch=1)

    # create scale mult for rig uniform scale
    arc_len_md = mc.createNode('multiplyDivide')
    mc.setAttr(arc_len_md+'.input1X', mc.getAttr (info+'.arcLength'))
    mc.connectAttr(orig_crv+'.globalScale', arc_len_md+'.input2X')

    # arc len clamp for max value
    arc_len_clamp = mc.createNode('clamp')
    mc.connectAttr(arc_len_md+'.outputX', arc_len_clamp+'.minR')
    mc.connectAttr(info+'.arcLength', arc_len_clamp+'.inputR' )
    mc.setAttr(arc_len_clamp+'.maxR', 1000000000)

    # blendtwo attr for enabling stretch
    stretch_bta = mc.createNode('blendTwoAttr')
    mc.connectAttr(orig_crv+'.stretch', stretch_bta+'.attributesBlender')
    mc.connectAttr(arc_len_md+'.outputX', stretch_bta+'.input[0]')
    mc.connectAttr(arc_len_clamp+'.outputR', stretch_bta+'.input[1]')

    # mult for calculating stretch and offset cut points
    md = mc.createNode('multiplyDivide')
    mc.setAttr (md+'.operation', 2)
    mc.connectAttr (stretch_bta+'.output', md+'.input1X')
    mc.connectAttr (arc_len_clamp+'.outputR', md+'.input2X')

    mc.addAttr(md, k=1, ln='maxZero', at='double')
    mc.addAttr(md, k=1, ln='maxOne' , at='double', dv=1)
    mc.addAttr(md, k=1, ln='minZero', at='double', dv=0)
    mc.addAttr(md, k=1, ln='minOne' , at='double')

    #store min and max offset values
    min_max_pma = mc.createNode ('plusMinusAverage')
    mc.setAttr(min_max_pma+'.operation', 2)
    mc.addAttr(min_max_pma, ln='one',dv=1 , at='double')

    mc.connectAttr(min_max_pma+'.one', min_max_pma+'.input1D[0]')
    mc.connectAttr(md+'.outputX', min_max_pma+'.input1D[1]')
    mc.connectAttr(md+'.outputX', md+'.maxZero')
    mc.connectAttr(min_max_pma+'.output1D', md+'.minOne')

    #set ranges for min and Max
    min_set_range = mc.createNode('setRange')

    mc.setAttr(min_set_range+'.oldMaxY', 1)
    mc.setAttr(min_set_range+'.oldMaxX', 1)

    mc.connectAttr(crv+'.reverseRoot', min_set_range+'.valueX')
    mc.connectAttr(crv+'.reverseRoot', min_set_range+'.valueY')

    mc.connectAttr(md+'.minZero', min_set_range+'.minX')
    mc.connectAttr(md+'.minOne', min_set_range+'.maxX')
    mc.connectAttr(md+'.maxZero', min_set_range+'.minY')
    mc.connectAttr(md+'.maxOne', min_set_range+'.maxY')

    # Condition for uniform
    cnd = mc.createNode('condition')
    mc.connectAttr(crv+'.stretch', cnd+'.firstTerm')
    mc.connectAttr(min_set_range+'.outValueY', cnd+'.colorIfFalseR')
    mc.setAttr(cnd+'.colorIfTrueR', mc.getAttr(uniform_crv+'Shape.maxValue'))
    mc.setAttr(cnd+'.secondTerm', 2)

    # connect offset attr
    adl0 = mc.createNode('addDoubleLinear')
    adl1 = mc.createNode('addDoubleLinear')

    mc.connectAttr(min_set_range+'.outValueX', adl0+'.input2')
    mc.connectAttr(cnd+'.outColorR', adl1+'.input2')

    # connect to curve detachs
    mc.connectAttr(adl0+'.output', detatch_node+'.parameter[0]')
    mc.connectAttr(adl1+'.output', detatch_node+'.parameter[1]')

    if mc.objExists(globalScale):
        mc.connectAttr(globalScale, crv+'.globalScale')

    # cleanup
    shapes = utils.get_shapes(uniform_crv)+utils.get_shapes(blend_crv)+utils.get_shapes(detatch_crv)
    mc.parent(shapes, crv, r=1, s=1)
    for s in [shape]+shapes[:-1]:
        mc.setAttr(s+'.io', 1)

    mc.delete(uniform_crv, blend_crv, detatch_crv)
    mc.rename(shape, shape+'Orig')
    mc.rename(shapes[-1], shape)

    return crv

def scale_ramp_sdk(ctrls, jnts, interpolation=4, driver_attr='', driven_attrs=['sy','sz']):

    #create attrs
    number_ctrls = len(ctrls)
    ramps = []

    # create ramps
    div = 1.0 / (number_ctrls-1)

    for i in range(number_ctrls):
        pre = (i-1) * div
        post = (i+1) * div
        current = i * div

        ramp = mc.createNode ('ramp', n=ctrls[i]+'_ramp')
        mc.setAttr(ramp+'.colorEntryList[0].color', 0,0,0, type='double3')
        mc.setAttr(ramp+'.colorEntryList[1].color', 1,1,1,type='double3')
        mc.setAttr(ramp+'.colorEntryList[2].color', 0,0,0, type='double3')
        mc.setAttr(ramp+'.colorEntryList[0].position', max(min(1, pre), 0) )
        mc.setAttr(ramp+'.colorEntryList[1].position', current)
        mc.setAttr(ramp+'.colorEntryList[2].position', max(min(1, post), 0))
        mc.setAttr(ramp+'.interpolation', interpolation)
        ramps.append(ramp)

    mc.removeMultiInstance(ramps[-1]+'.colorEntryList[2]', b=True)
    mc.removeMultiInstance(ramps[0]+'.colorEntryList[0]', b=True)

    # setup joint twist and Scale readers//
    number_jnts = len(jnts)
    div = 1.0 / (number_jnts-1)

    tt = 'spline'
    sdk_crvs = []

    for i in range(number_ctrls):
        for dattr in driven_attrs:
            driver_ctrl = ctrls[i]+'.'+driver_attr

            if not mc.objExists(driver_ctrl):
                mc.addAttr(ctrls[i], ln=driver_attr, k=1, dv=1)

            for ji in range(number_jnts):

                driven_attr = jnts[ji]+'.'+dattr
                if not mc.objExists(driven_attr):
                    mc.warning(driven_attr+' doesnt exist. Skipping..')
                    continue

                mc.setAttr(ramps[i]+'.vCoord', div*ji)
                value = mc.getAttr(ramps[i]+'.outColorR')

                mc.setDrivenKeyframe(driven_attr, cd=driver_ctrl, dv=0, v=0, ott=tt, itt=tt)
                mc.setDrivenKeyframe(driven_attr, cd=driver_ctrl, dv=1, v=value, ott=tt, itt=tt)

            sdk_crvs.extend(mc.listConnections(driver_ctrl, type='animCurve', scn=1) )

    if sdk_crvs:
        mc.selectKey(sdk_crvs)
        mc.setInfinity(poi='linear', pri='linear')

    # set infinity
    mc.delete(ramps)


def preserve_volume(drivers, nodes, ctrl, attrs=['sx', 'sy','sz']):
    """Set up scale base volume preservation for a given set of joints in a chain.

        Args:
            :drivers: (list) Driver nodes
            :nodes: (list) Driven nodes - These will scale so it's best to have them in flattened hierarchy.
            :ctrl: (str) Driving ctrl for volume attriobutes.

        Kwargs:
            :attrs: (list) Attributes to scale. Defaults to ["sy", "sz"]."""

    if not mc.objExists(ctrl+'.preserveVolume'):
        mc.addAttr(ctrl, ln='preserveVolume', k=1, min=0, max=1, dv=0.5)
    if not mc.objExists(ctrl+'.preserveVolumeMin'):
        mc.addAttr(ctrl, ln='preserveVolumeMin', k=1, min=0.01, max=1, dv=0.2)
    if not mc.objExists(ctrl+'.preserveVolumeMax'):
        mc.addAttr(ctrl, ln='preserveVolumeMax', k=1, min=1, max=10, dv=4)

    for i, node in enumerate(nodes[:-1]):
        dst = utils.create_distance_reader(drivers[i], drivers[i+1])
        bta = mc.createNode('blendTwoAttr', name = ('blendTwoAttr_preserveVolume_' + node))

        mc.connectAttr(ctrl+'.preserveVolume', bta+'.attributesBlender')
        mc.connectAttr(dst+'.inverseStretchFactor', bta+'.input[1]')
        mc.setAttr(bta+'.input[0]', 1)

        clamp = mc.createNode('clamp',name = ('clamp_preserveVolume_' + node))
        mc.connectAttr(bta+'.output', clamp+'.inputR')
        mc.connectAttr(ctrl+'.preserveVolumeMin', clamp+'.minR')
        mc.connectAttr(ctrl+'.preserveVolumeMax', clamp+'.maxR')

        for attr in attrs:
            cnn = mc.listConnections(node+'.'+attr, s=1, d=0, p=1)
            if cnn:
                mdl = mc.createNode('multDoubleLinear', name = (node + "_preserveVolume_multDoubleLinear"))
                mc.connectAttr(cnn[0], mdl+'.i1')
                mc.connectAttr(clamp+'.outputR', mdl+'.i2')
                mc.connectAttr(mdl+'.o', node+'.'+attr, f=1)

            else:
                mc.connectAttr(clamp+'.outputR', node+'.'+attr)

    try:
        mc.connectAttr(nodes[-2]+'.s', nodes[-1]+'.s')
    except:
        pass

def create_ramps(ctrls, interpolation=4):

    number_ctrls = len(ctrls)
    ramps = []

    # create ramps
    div = 1.0 / (number_ctrls-1)

    for i in range(number_ctrls):
        pre = (i-1) * div
        post = (i+1) * div
        current = i * div

        ramp = mc.createNode ('ramp', n=ctrls[i]+'_ramp')
        mc.setAttr(ramp+'.colorEntryList[0].color', 0,0,0, type='double3')
        mc.setAttr(ramp+'.colorEntryList[1].color', 1,1,1,type='double3')
        mc.setAttr(ramp+'.colorEntryList[2].color', 0,0,0, type='double3')
        mc.setAttr(ramp+'.colorEntryList[0].position', max(min(1, pre), 0) )
        mc.setAttr(ramp+'.colorEntryList[1].position', current)
        mc.setAttr(ramp+'.colorEntryList[2].position', max(min(1, post), 0))
        mc.setAttr(ramp+'.interpolation', interpolation)
        ramps.append(ramp)

    mc.removeMultiInstance(ramps[-1]+'.colorEntryList[2]', b=True)
    mc.removeMultiInstance(ramps[0]+'.colorEntryList[0]', b=True)

    return ramps

def curl_sdk(nodes, ctrl, curl_attr='rz', curl_side_attr='ry'):

    if not mc.objExists(ctrl+'.curl'):
        mc.addAttr(ctrl, ln='curl', min=-10, max=10, k=1)

    if not mc.objExists(ctrl+'.curlSide'):
        mc.addAttr(ctrl, ln='curlSide', min=-10, max=10, k=1)

    if not mc.objExists(ctrl+'.curlTaper'):
        mc.addAttr(ctrl, ln='curlTaper', min=0, max=10, dv=5, k=1)
    if not mc.objExists(ctrl+'.curlTightness'):
        mc.addAttr(ctrl, ln='curlTightness', min=1, dv=10, k=1)

    nodes.reverse()
    nodes = nodes[1:]

    tt = 'linear'
    div = 10.0 / (len(nodes)-1)
    for i, node in enumerate((nodes)):

        #mc.setAttr(node+'.rotateOrder', 3)

        tight_ymd = mc.createNode('multDoubleLinear')
        tight_zmd = mc.createNode('multDoubleLinear')

        taper_ymd = mc.createNode('multDoubleLinear')
        taper_zmd = mc.createNode('multDoubleLinear')

        mc.connectAttr(ctrl+'.curlTightness', tight_ymd+'.i1')
        mc.connectAttr(ctrl+'.curlTightness', tight_zmd+'.i1')
        mc.connectAttr(tight_ymd+'.o', taper_ymd+'.i1')
        mc.connectAttr(tight_zmd+'.o', taper_zmd+'.i1')

        mc.connectAttr(taper_ymd+'.o', node+'.'+curl_side_attr, f=1)
        mc.connectAttr(taper_zmd+'.o', node+'.'+curl_attr, f=1)

        f0 = div*i
        f1 = div*(i+1)
        mc.setDrivenKeyframe(tight_zmd+'.i2', cd=ctrl+'.curl', dv=f0, v=0, itt=tt, ott=tt)
        mc.setDrivenKeyframe(tight_zmd+'.i2', cd=ctrl+'.curl', dv=f1, v=10, itt=tt, ott=tt)
        mc.setDrivenKeyframe(tight_zmd+'.i2', cd=ctrl+'.curl', dv=-f0, v=0, itt=tt, ott=tt)
        mc.setDrivenKeyframe(tight_zmd+'.i2', cd=ctrl+'.curl', dv=-f1, v=-10, itt=tt, ott=tt)

        mc.setDrivenKeyframe(tight_ymd+'.i2', cd=ctrl+'.curlSide', dv=f0, v=0, itt=tt, ott=tt)
        mc.setDrivenKeyframe(tight_ymd+'.i2', cd=ctrl+'.curlSide', dv=f1, v=10, itt=tt, ott=tt)
        mc.setDrivenKeyframe(tight_ymd+'.i2', cd=ctrl+'.curlSide', dv=-f0, v=0, itt=tt, ott=tt)
        mc.setDrivenKeyframe(tight_ymd+'.i2', cd=ctrl+'.curlSide', dv=-f1, v=-10, itt=tt, ott=tt)

        mc.setDrivenKeyframe(taper_ymd+'.i2', cd=ctrl+'.curlTaper', dv=0, v=1, itt=tt, ott=tt)
        mc.setDrivenKeyframe(taper_ymd+'.i2', cd=ctrl+'.curlTaper', dv=10, v=((10.0-div*i)*.1)*2.0, itt=tt, ott=tt)

        mc.setDrivenKeyframe(taper_zmd+'.i2', cd=ctrl+'.curlTaper', dv=0, v=1, itt=tt, ott=tt)
        mc.setDrivenKeyframe(taper_zmd+'.i2', cd=ctrl+'.curlTaper', dv=10, v=((10.0-div*i)*.1)*2.0, itt=tt, ott=tt)

def connect_param_node(crv, surf, nodes, world_scale_attr='world_CTL.worldScale'):

    result = []
    nodes = mc.ls(nodes)

    for node in nodes:


        pn = mc.createNode('cmSplineNode', n=node+'_cspl')

        mc.connectAttr(crv+'.worldSpace', pn+'.inputCurve')
        mc.connectAttr(surf+'.worldSpace', pn+'.inputSurface')
        mc.connectAttr(node+'.parentInverseMatrix', pn+'.parentInverseMatrix')

        if mc.objExists(world_scale_attr):
            mc.connectAttr(world_scale_attr, pn+'.worldScale')

        # get initial values for node
        sel = om.MSelectionList()
        sel.add(utils.get_shapes(crv)[0])
        crvObj = om.MDagPath()
        sel.getDagPath(0, crvObj)
        crvFn = om.MFnNurbsCurve(crvObj)

        # set init length
        crvlen = crvFn.length()
        mc.setAttr(pn+'.origCurveLength', crvlen)

        # get non unifrom param value
        p = mc.xform(node, q=1, ws=1, t=1)
        p = om.MPoint(p[0], p[1], p[2])

        u = om.MScriptUtil()
        u.createFromDouble(0)
        dbl = u.asDoublePtr()

        crvFn.closestPoint(p, dbl, om.MSpace.kWorld)
        nu_param = round(u.getDoubleArrayItem(dbl, 0), 3)

        if nu_param == 0:
            param_len = 0.0

        elif nu_param == round(mc.arclen(crv, ch=0), 3):
            param_len = float(mc.getAttr(crv+'.spans'))
        else:
            tmp = mm.eval('detachCurve -ch 1 -cos on -rpo 0 {0}.u[{1}];'.format(crv, nu_param))
            param_len = mc.arclen(tmp[0])
            mc.delete(tmp)

        mc.setAttr(pn+'.paramLength', param_len)
        mc.setAttr(pn+'.nonUniformParam', nu_param)

        # zero out node
        if mc.nodeType(node) == 'joint':
            mc.setAttr(node+'.jox', l=0)
            mc.setAttr(node+'.joy', l=0)
            mc.setAttr(node+'.joz', l=0)

            mc.setAttr(node+'.rx', mc.getAttr(node+'.jox'))
            mc.setAttr(node+'.ry', mc.getAttr(node+'.joy'))
            mc.setAttr(node+'.rz', mc.getAttr(node+'.joz'))
            mc.setAttr(node+'.jox', 0)
            mc.setAttr(node+'.joy', 0)
            mc.setAttr(node+'.joz', 0)

        # get offset matrix
        tmp = mc.duplicate(node, po=1)[0]
        utils.set_attrs(tmp, l=0, k=1)
        mc.connectAttr(pn+'.outputTranslate', tmp+'.t')
        mc.connectAttr(pn+'.outputRotate', tmp+'.r')

        offset = utils.get_offset_matrix(tmp, node)
        mc.setAttr(pn+'.offsetMatrix', offset, type='matrix')

        # connect to node
        mc.connectAttr(pn+'.outputTranslate', node+'.t', f=1)
        mc.connectAttr(pn+'.outputRotate', node+'.r', f=1)
        mc.delete(tmp)

        result.append(pn)

    return result

def ramp_scale(primary_ctrls, nodes, secondary_ctrls=[], interpolation=4, driver_attr='s'):

    ramps = create_ramps(primary_ctrls, interpolation)
    div = 1.0 / (len(nodes)-1)
    pri_cons = []

    for i, ctrl in enumerate(primary_ctrls):

        if not mc.objExists(ctrl+'.'+driver_attr):
            mc.addAttr(ctrl, ln=driver_attr, k=1, dv=1, min=0.001)

        for ji, node in enumerate(nodes):

            mc.setAttr(ramps[i]+'.vCoord', div*ji)
            value = mc.getAttr(ramps[i]+'.outColorR')

            sc = mc.scaleConstraint(ctrl, node, weight=value, mo=1)[0]
            wi = len(mc.scaleConstraint(sc, q=1, tl=1))-1

            if driver_attr not in ['s','sx','sy','sz','scale','scaleX','scaleY', 'scaleZ']:
                mc.connectAttr(ctrl+'.'+driver_attr, '{0}.target[{1}].targetScaleX'.format(sc, wi))
                mc.connectAttr(ctrl+'.'+driver_attr, '{0}.target[{1}].targetScaleY'.format(sc, wi))
                mc.connectAttr(ctrl+'.'+driver_attr, '{0}.target[{1}].targetScaleZ'.format(sc, wi))

            pri_cons.append(sc)

    mc.delete(ramps)

    # now handle the secondary ctrls
    if not secondary_ctrls:
        return

    for ji, node in enumerate(nodes):
        mc.disconnectAttr(pri_cons[ji]+'.constraintScaleX', node+'.sx')
        mc.disconnectAttr(pri_cons[ji]+'.constraintScaleY', node+'.sy')
        mc.disconnectAttr(pri_cons[ji]+'.constraintScaleZ', node+'.sz')

    ramps = create_ramps(secondary_ctrls, interpolation)
    div = 1.0 / (len(nodes)-1)
    sec_cons = []

    for i, ctrl in enumerate(secondary_ctrls):

        if not mc.objExists(ctrl+'.'+driver_attr):
            mc.addAttr(ctrl, ln=driver_attr, k=1, dv=1, min=0.001)

        for ji, node in enumerate(nodes):
            mc.setAttr(ramps[i]+'.vCoord', div*ji)
            value = mc.getAttr(ramps[i]+'.outColorR')

            sc = mc.scaleConstraint(ctrl, node, weight=value, mo=1)[0]
            wi = len(mc.scaleConstraint(sc, q=1, tl=1))-1

            if driver_attr not in ['s','sx','sy','sz','scale','scaleX','scaleY', 'scaleZ']:
                mc.connectAttr(ctrl+'.'+driver_attr, '{0}.target[{1}].targetScaleX'.format(sc, wi))
                mc.connectAttr(ctrl+'.'+driver_attr, '{0}.target[{1}].targetScaleY'.format(sc, wi))
                mc.connectAttr(ctrl+'.'+driver_attr, '{0}.target[{1}].targetScaleZ'.format(sc, wi))

            sec_cons.append(sc)

    mc.delete(ramps)

    for i, node in enumerate(nodes):
        p_con = pri_cons[i]
        s_con = sec_cons[i]

        mc.disconnectAttr(s_con+'.constraintScaleX', node+'.sx')
        mc.disconnectAttr(s_con+'.constraintScaleY', node+'.sy')
        mc.disconnectAttr(s_con+'.constraintScaleZ', node+'.sz')

        md = mc.createNode('multiplyDivide', name = (node + "_rampScale_multiplyDivide") )
        mc.connectAttr(p_con+'.constraintScale', md+'.i1')
        mc.connectAttr(s_con+'.constraintScale', md+'.i2')
        # test for 'other' incoming connections to sx,sy,sz
        axis = ['X','Y','Z']
        for axi in axis:
            cnn = mc.listConnections((node + '.scale' + axi), s=1, d=0, p=1)
            if cnn:
                multOffset = mc.createNode('multDoubleLinear', name = (node + "_rampScaleOffset_multDoubleLinear") )
                mc.connectAttr(md + '.outputX', (multOffset + "." + "input1"))
                mc.connectAttr(cnn[0], (multOffset + "." + "input2"))
                mc.connectAttr(((multOffset + "." + "output")), (node + '.scale' + axi), f=1)
            else:
                mc.connectAttr((md+'.output' + axi), (node + '.' + 'scale' + axi), f=1)


def create_joints_on_spline(crv, number_joints, prefix, flat=False):
    '''Create joints evenly spanced along a curve. Create either a herirachy chain or flat.'''

    def getDagPath(node=None):
        sel = om.MSelectionList()
        sel.add(node)
        d = om.MDagPath()
        sel.getDagPath(0, d)
        return d

    crv = mc.listRelatives(crv, type='nurbsCurve')[0]
    crvFn = om.MFnNurbsCurve(getDagPath(crv))

    div = 1.0 / (number_joints -1)
    jnts = []

    for i in range(number_joints):
        ltr = utils.letters[i]
        nn = prefix+'_'+ltr+'_JNT'
        parameter = crvFn.findParamFromLength(crvFn.length() * div * i)
        point = om.MPoint()
        crvFn.getPointAtParam(parameter, point)
        jnt = mc.createNode('joint', name=nn)
        mc.xform(jnt,t=[point.x,point.y,point.z])

        jnts.append(jnt)

        if jntrs and not flat:
            mc.parent(jnt, jnts[-1])

    return jnts
