# -*- coding: utf-8 -*-
"""Functions for building a skeleton from a guide_node rig."""

import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import guide
from rigBot import env

def build(scale_compensate=False, shakeout=True):
    """Create a clean skeleton rig from a guide_node rig. This will also save guide_node and ctrl nodes under a *guides_REF* node.

        Args:
            :scale_compensate: (bool) Turn segment scale compensate on or off on skeleton. Defaults to False."""

    # handle legacy rig
    if not mc.objExists('guides.guideMaster'):
        mc.warning('Guides do not exist in scene!')
        return

    world_root = [p for p in mc.ls('|guides|*.partType')
                        if mc.getAttr(p, asString=1) == 'worldRoot'] or None

    if not world_root:
        mc.warning('worldRoot part does not exist! Creating one..')
        guide.build('worldRoot')

    # Kill constraints
    junk = mc.ls(type=('pointConstraint', 'aimConstraint', 'orientConstraint', 'scaleConstraint',
                       'cmJointShape', 'cmPivotShape', 'parentConstraint', 'ikHandle', 'follicle'))

    junk = [j for j in junk if not mc.objExists(j+'.keepAsRef')]
    if junk:
        mc.delete(junk)

    keep_ref_nodes = [n.replace('.keepAsRef','') for n in mc.ls('*.keepAsRef')]
    keep_ref_nodes = [mc.rename(n, n+'_tmpREF') for n in keep_ref_nodes]

    # Get rig parts, tpose nodes and ctrls
    guides = [n.replace('.partType', '') for n in mc.ls('*.partType')]
    pivots = [n.replace('.animControlPivot', '') for n in mc.ls('*.animControlPivot')]
    ctrls = [n.replace('.animControl', '') for n in mc.ls('*.animControl')]
    ctrls = [c for c in ctrls if not c.endswith('OFF_CTL')]

    # dup off guide_node nodes:
    skel_top_grp = mc.createNode('transform', n='skel_GRP')
    skel_guides = mc.createNode('transform', n='guides_REF' )

    ##########################################################
    # Create ref guide_node nodes which contain options

    # Create skel grpo for each part

    for guide_node in guides:
        skel_guide = mc.duplicate(guide_node ,n=guide_node+'_REF', po=1)[0]
        mc.parent(skel_guide, skel_guides)

    ##########################################################
    # process ctrls

    utils.set_attrs(pivots+ctrls, 't r s v', k=1, l=0)
    processed_ctrls = []

    for pivot in pivots:

        # duplicate to ensure connections are proken
        pivot = mc.parent(pivot, skel_guides)[0]
        dup_pivot = mc.duplicate(pivot)[0]
        mc.delete(pivot)
        pivot = mc.rename(dup_pivot, pivot+'_REF')


        # get all children of pivot
        children = [n for n in utils.get_children(pivot, ad=1)
                            if not mc.nodeType(n) == 'nurbsCurve']

        # delete any nodes that are not ctrls
        for child in children:
            if mc.objExists(child+'.animControl'):
                if mc.objExists(child):
                    if not mc.getAttr(child+'.v'):
                        mc.delete(child)

                    else:
                        if utils.get_parent(child) != pivot:
                            mc.parent(child, pivot)

                        mc.makeIdentity(child, apply=1, t=1, r=1, s=1, n=0, pn=1)
                        mc.xform(child, piv=[0,0,0])
                        mc.rename(child, child+'_REF')

                processed_ctrls.append(child)

            else:
                if mc.objExists(child):
                    mc.delete(child)

    # adjust CTRLs attrs to reflect new ctrls in scene
    for guide_node in guides:
        skel_guide = guide_node+'_REF'
        guide_ctrls = eval(mc.getAttr(skel_guide+'.CTLS') or '[]')
        guide_ctrls = [c for c in guide_ctrls if mc.objExists(c+'_REF')]
        guide_ctrls = [c for c in guide_ctrls if c in ctrls]
        mc.setAttr(skel_guide+'.CTLS', str(guide_ctrls), type='string')


    # handle any leftovers that may not have had pivots for some reason.
    left_overs = [c for c in ctrls if c not in processed_ctrls]
    if left_overs:
        mc.parent(left_overs, skel_guides)
        mc.makeIdentity(left_overs, apply=1, t=1, r=1, s=1, n=0, pn=1)
        mc.xform(left_overs, piv=[0,0,0])

    ##########################################################
    # process joints

    world_jnt = 'C_world_JNT'
    root_jnt = 'C_root_JNT'

    all_guide_top_jnts = []
    all_guide_parents = []

    for guide_node in guides:

        # find parent for the part.
        guide_parent = root_jnt
        if mc.getAttr(guide_node+'.partType', asString=True) == 'worldRoot':
            guide_parent = skel_top_grp

        elif not mc.objExists(guide_node+'.parent'):
            guide_parent = root_jnt

        else:
            guide_parent = mc.getAttr(guide_node+'.parent')
            if '[' in guide_parent:
                guide_parent = eval(guide_parent)
                guide_parent = guide_parent[0]

            if not mc.objExists(guide_parent):
                new_parent = guide_parent.replace('_CTL', '_JNT')
                if mc.objExists(new_parent):
                    guide_parent = new_parent
                else:
                    guide_parent = root_jnt

        # find guide_node top nodes
        guide_top_jnts = [c for c in utils.get_children(guide_node+'_JNTS')
                        if mc.nodeType(c) == 'joint']

        # duplicate and group / freeze joints to all be at world scale of 1
        dup_top = mc.duplicate(guide_node+'_JNTS', n=guide_node+'_JNTS_REF')[0]
        mc.delete(guide_node+'_JNTS')

        all_guide_jnts = utils.get_children(dup_top, ad=1)
        all_guide_jnts.reverse()

        utils.set_attrs([dup_top]+all_guide_jnts, 't r s', k=1, l=0)

        mc.parent(dup_top, w=1)
        mc.makeIdentity(dup_top, apply=1, t=1, r=1, s=1, n=0, pn=1)

        # now unparent clean joints to world
        if guide_top_jnts:
            guide_top_jnts = mc.parent(guide_top_jnts, w=1)
        mc.delete(dup_top)

        all_guide_top_jnts.append(guide_top_jnts)
        all_guide_parents.append(guide_parent)

        # reset guide_node ref JNTS attr to reflect jnts in scene
        non_ref_names= [j.replace('_REF','') for j in all_guide_jnts]
        mc.setAttr(guide_node+'_REF.JNTS', str(non_ref_names), type='string')

    # now deleete old guides and parent joints
    for i, guide_parent in enumerate(all_guide_parents):
        if all_guide_top_jnts[i]:
            mc.parent(all_guide_top_jnts[i], guide_parent)
            mc.addAttr(all_guide_top_jnts[i], ln='partTopJoint', at='message')

    # now freeze skel grp
    mc.makeIdentity(skel_top_grp, apply=1, t=1, r=1, s=1, n=0, pn=1)

    # remove all _ref tokens from joints
    all_joints = mc.ls(type='joint')

    for jnt in all_joints:
        mc.setAttr(jnt+'.radi', 1)
        mc.setAttr(jnt+'.segmentScaleCompensate', scale_compensate)

        if jnt.endswith('_REF'):
            mc.rename(jnt, jnt.replace('_REF', ''))

    mc.parent(keep_ref_nodes, skel_guides)

    # now handle any nodes the use parented under the guides node
    user_nodes= [n for n in utils.get_children('guides') if n not in guides]
    for node in user_nodes:
        if mc.nodeType(node) != 'joint':
            mc.parent(node, skel_top_grp)

        else:
            tmp = mc.createNode('transform', p=utils.get_parent(node))
            mc.parent(node, tmp)
            mc.parent(tmp, w=1)
            mc.makeIdentity(tmp, apply=1, t=1, r=1, s=1, n=0, pn=1)
            mc.parent(node, skel_top_grp)
            mc.delete(tmp)

    ##############################################
    # cleanup

    keep_ref_nodes = [mc.rename(n, n.replace('_tmpREF', '_REF')) for n in keep_ref_nodes]

    mc.delete('guides')
    mc.parent(skel_guides, skel_top_grp)
    mc.hide(skel_guides)

    for node in mc.listRelatives(skel_top_grp, ad=1):
        try:
            mc.setAttr(node+'.displayLocalAxis', 0)
        except:
            pass

    set_suffix = utils.get_suffix('objectSet')
    guide_sets = [s for s in mc.ls(type='objectSet')
                                    if s.endswith(set_suffix)]
    if guide_sets:
        mc.delete(guide_sets)

    # Create dupliicate ref skeletion
    ref_skel = mc.duplicate(world_jnt, rc=1)

    for i, jnt in enumerate(ref_skel):
        ref_name = jnt.split('JNT')[0]+'JNT_REF'
        ref_skel[i] = mc.rename(jnt, ref_name)

    mc.parent(ref_skel[0], skel_guides)

    junk = [j for j in utils.get_children('C_world_JNT', ad=1) if mc.nodeType(j) != 'joint']
    junk.extend([j for j in utils.get_children('C_world_JNT_REF', ad=1) if mc.nodeType(j) != 'joint'])
    for j in junk:
        parent = utils.get_parent(j)
        children = utils.get_children(j)
        if children:
            mc.parent(children, parent)
        mc.delete(j)

    if shakeout:
        utils.shakeout_selection(skel_top_grp)
    return True

def save():
    """Wraqpper for comms td save stream as skel."""

    mc.selectPriority(locator=9)
    env.save_stream('skel')

def load(i=True, new_file=True, version='LATEST'):
    """Wraqpper for comms td save stream as skel.

    Kwargs:
        :i: (bool) Import file int o current scene. Defaults to True.
        :new_file: (bool) Start a new scene. Defaults to True.
        :version: (str) File version. Defaults to "LATEST"."""

    mc.selectPriority(locator=9)
    version = version.upper()

    if i:
        env.import_stream('skel', version=version, new_file=new_file)
    else:
        env.open_stream('skel', version=version)

