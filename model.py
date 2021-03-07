import maya.cmds as mc
import maya.mel as mm

from rigBot import guide
from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import env

import os
import time

try:
    import commstd
    from commstd import pipeline

except:
    pass

def save(variant='Default', version='NEXT'):
    """Save a model stream"""
    env.save_stream('model', token=variant, version=version, workfile=0)

def load(asset=None, name='Default', variant='primary', file_type=None, version='HIGHEST', soften_normals=None, unlock_normals=True, keep_cm_node=False, kill_layers=True):

    """Import a model into the scene and IF there is a rig, parent and connect the visibitly.

        Kwargs:
            :asset: (None, str) Asset name. Defaults to currently set asset from env.
            :name: (str) Stream name. Defaults to 'default'.
            :version: (str, int) File version. Defaults to "HIGHEST"
            :variant: (str) Stream variant. Defaults to "primary".
            :file_type: (str) Options are: "Maya Geometry" OR "Alembic Geometry" Defaults to "Maya Geometry"
            :soften_normals: (bool) Soften all the normals for the geo. Defaults to False
            :unlock_normals: (bool) Unlock all the normals for the geo. Defaults to True
            :keep_cm_node: (bool) Keep the cm node for the model in the scene. Defaults to False
            :kill_layers: (bool) Kill display layers in the scene and set display overrides to off. Defaults to True"""

    # testing new shotgun cm node loading

    return load_vanilla(asset, name, version, soften_normals, unlock_normals, kill_layers)


def load_vanilla(asset='', name='', version=None, soften_normals=False, unlock_normals=True, kill_layers=True):

    ###########################################################################
    # Old method for import from vanilla maya model path

    if type(version) in [str, unicode]:
        if version.upper() == 'HIGHEST':
            version = None

    # import the file path
    path = ''
    snapshot = mc.ls('|*')
    try:
        asset_path = env.get_rigbuild_path()
        path=os.path.join (path, 'model\model.mb')
        print path
        mc.file (path, i=1)
        top_node = [n for n in mc.ls('|*') if n not in snapshot]
        if top_node:
            top_node = top_node[0]

    except:
        mc.warning('No model found!')
        return

    # grab the toop node
    if not top_node:
        mc.warning('Model import was an emty file!')
        return

    # if not mc.objExists('rig_GRP'):
    #     return

    # Create model grp IF one does not already exist
    if not mc.objExists ('geometry_grp'):
        if not top_node == 'model_GRP' and not mc.objExists('model_GRP'):
            top_node = mc.group(top_node, n='model_GRP')
            mc.parent(top_node, 'rig_GRP')
            mc.xform(top_node, piv=[0,0,0])

        elif mc.objExists('model_GRP'):
            mc.parent(top_node, 'model_GRP')
    elif mc.objExists ('geometry_grp'):
        mc.parent (top_node, 'geometry_grp')

    # connect model nodes
    connect_model(top_node, soften_normals, unlock_normals, kill_layers=kill_layers, model_path=path)

    # print result
    print '\n#####################################################################'
    print '#LOADED MODEL (vanilla):'

    print '\tpath: '+path
    print '\n#####################################################################'

    return top_node

def connect_model(top_node, soften_normals=False, unlock_normals=True, kill_layers=True, model_path=''):

    # get shapes
    shapes = utils.get_children(top_node, ad=1)
    shapes = [utils.get_parent(s) for s in shapes
                    if mc.nodeType(s) in ['mesh', 'nurbsCurve', 'nurbsSurface']]

    # unloc normals and soften normals
    if shapes:
        if soften_normals:
            unlock_normals = True

        if unlock_normals:
            mc.polyNormalPerVertex(shapes, ufn=True)

        if soften_normals:
            for shape in shapes:
                mc.polySoftEdge(shape, a=180)
                mc.delete(shape, ch=1)

    # remove all draw overrides on geo and kill layers
    if kill_layers:
        layers =[ l for l in mc.ls(type='displayLayer') if l != 'defaultLayer']
        if layers:
            mc.delete(layers)

        utils.set_draw_override([top_node]+utils.get_children(top_node, ad=1))

    # connect vis ctrl

    if mc.objExists('visibility_CTL'):

        ctrl = 'rig_GRP'
        vis_ctrl = mc.ls('visibility_CTL', 'rig_GRP')[0]
        cnd = ctrl+'_cnd'

        if not mc.objExists(cnd):
            cnd = mc.createNode('condition', n=cnd)
            mc.connectAttr(vis_ctrl+'.modelSelectable', cnd+'.firstTerm')
            mc.setAttr(cnd+'.ihi', 0)
            mc.setAttr(cnd+'.secondTerm', 0)
            mc.setAttr(cnd+'.colorIfTrueR', 2)
            mc.setAttr(cnd+'.colorIfFalseR', 0)

        # connect draw override to model GRP
        mc.setAttr(top_node+'.v', l=0)
        mc.setAttr(top_node+'.overrideEnabled', 1)

        mc.select(top_node, hi=1)
        nodes = mc.ls(sl=1)
        utils.set_draw_override(nodes)
        mc.setAttr(top_node+'.overrideEnabled', 1)

        if not mc.isConnected(vis_ctrl+'.modelVis', top_node+'.v'):
            mc.connectAttr(vis_ctrl+'.modelVis', top_node+'.v', f=1)

        if not mc.isConnected(cnd+'.outColorR', top_node+'.overrideDisplayType'):
            mc.connectAttr(cnd+'.outColorR', top_node+'.overrideDisplayType', f=1)

    # add model path to rig sel
    if mc.objExists('rig_SEL'):
        if not mc.objExists('rig_SEL.modelPath'):
            mc.addAttr('rig_SEL', ln='modelPath', dt='string')

        mc.setAttr('rig_SEL.modelPath', l=0)
        mc.setAttr('rig_SEL.modelPath', model_path, type='string')
        mc.setAttr('rig_SEL.modelPath', l=1)

    # Add geo to cache sel
    # if mc.objExists('cache_SEL'):
    #     mc.sets(shapes, add='cache_SEL')
    #
    # else:
    #     mc.sets(shapes, n='cache_SEL')
    #     mc.sets('cache_SEL', n='rig_SEL')

    # if mc.objExists('engine_SEL'):
    #     mc.sets(shapes, add='engine_SEL')

    mc.select(top_node)
    return top_node
