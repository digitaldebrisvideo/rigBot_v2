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

    if env.shotgun:
        mc.warning('This feature is not available in a shotgun environment.')

    else:
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
    if env.shotgun:
        if asset == None:
            asset = ''
        if name == 'Default':
            name = ''
        if variant == 'primary':
            variant = ''
        if version == 'HIGHEST':
            version = None
        if file_type == None:
            file_type = 'Alembic Geometry'

        return load_published(asset, name, variant, version, file_type, keep_cm_node, soften_normals, unlock_normals, kill_layers)

    else:
        return load_vanilla(asset, name, version, soften_normals, unlock_normals, kill_layers)

def load_published(asset='', name='', variant='', version=None, file_type='Alembic Geometry',
                   keep_cm_node=False, soften_normals=False, unlock_normals=True, kill_layers=True):

    def remove_namespace(namespace):
        try:
            mc.namespace(removeNamespace=namespace, mergeNamespaceWithRoot=1)
        except:
            pass

    # get asset
    if not asset:
        asset = env.get_asset()

    # parent GEOMETRY_GRP to world (fp_load requires this)
    if mc.objExists('GEOMETRY_GRP'):
        parent = mc.listRelatives('GEOMETRY_GRP', p=1)
        if parent:
            mc.parent('GEOMETRY_GRP', w=1)

    # find context asset, version and variant model
    pf_context = commstd.pipeline.create_context(entity_type="Asset", entity=asset, task="model")
    pf = pipeline.find_one_pf(pf_context, file_type, name+' '+asset, version_number=version)

    # If no pf is returned then there is no published model with that name
    if not pf:
        mc.warning('Cannot find published model for: {0} {1}'.format(name, asset))
        return

    # get variant
    load_this_pf = {}
    variants = pipeline.find_alternatives(pf, vary_variant=True)
    variant_names = [v['sg_variant'] for v in variants]

    if variant:
        variants = pipeline.find_alternatives(pf, vary_variant=True)
        for each in variants:
            if each['sg_variant'] == variant:
                load_this_pf = each
    else:
        # if variant is not set then look for primary
        for each in variants:
            if each['sg_variant'] == 'primary':
                load_this_pf = each

        # still if no variant is found, just use watever it found
        if not load_this_pf:
            load_this_pf = pf

    # if pf is still not found the we have to bail
    if not load_this_pf:
        mc.warning('Cannot find variant to load for "{0}". See script editor for details.'.format(pf.get('name')))
        print 'Available variants: {0}'.format(variant_names)
        return

    # try to clear namespaces
    bad_namespaces = [n for n in mc.namespaceInfo(listOnlyNamespaces=True, recurse=True) if '_NS' in n]
    for ns in bad_namespaces:
        remove_namespace(ns)

    # use pipeline tools to load context wit cm content node
    cm_node = pipeline.load_pf(load_this_pf)
    if not cm_node:
        mc.warning('Cannot load "{0}". See script editor for details.'.format(pf.get('name')))
        print '# ASSET PF INFO:\n'
        print load_this_pf
        return

    mc.select(cm_node)
    cm_node = mc.ls(sl=1)[0]
    namespace = mc.getAttr(cm_node+'.namespace')
    bad_namespaces = [n for n in mc.namespaceInfo(listOnlyNamespaces=True, recurse=True) if namespace in n]

    # Check if the pf_load broke and did not parent the model under the cm content node correctly.
    # This is usually becasue there are bad namespaces in the scene.. lets attempt to fix that
    ch = [c for c in mc.listRelatives(cm_node) if not mc.nodeType(c) == 'cmContent']
    if ch:
        if mc.referenceQuery(ch[0], isNodeReferenced=1):
            rf = mc.referenceQuery(ch[0], f=1)
            mc.file(rf, ir=1)

    elif not [n for n in mc.listRelatives(cm_node) or [] if mc.nodeType(n) != 'cmContent']:
        mc.warning('Broken namespaces exists in scene, model is not properly parented.. Attempting to fix..')

        for ns in bad_namespaces:
            nodes = mc.ls('|'+ns+':*')
            if nodes:
                mc.parent(nodes, cm_node)
                mc.warning('Parenting {0} under {1}'.format(nodes, cm_node))

    # remove all namespaces from scene
    for ns in bad_namespaces:
        remove_namespace(ns)

    # reparent GEOMETRY_GRP under rig_GRP OR other parent
    if mc.objExists('rig_GRP'):
        mc.parent(cm_node, 'rig_GRP')

    if not mc.listRelatives('GEOMETRY_GRP', c=1):
        mc.delete('GEOMETRY_GRP')

    # get info to print in script editor
    sg_name = load_this_pf.get('name')
    sg_path = load_this_pf.get('path').get('local_path_linux')
    sg_variant = load_this_pf.get('sg_variant')
    sg_version = load_this_pf.get('version_number')
    sg_file_type = load_this_pf.get('published_file_type').get('name')
    sg_code = load_this_pf.get('code')

    top_node = cm_node
    if not keep_cm_node:
        top_node = utils.get_children(cm_node)[0]
        mc.parent(utils.get_children(cm_node), utils.get_parent(cm_node))

        mc.delete(cm_node)

    connect_model(top_node, soften_normals, unlock_normals, kill_layers=kill_layers, model_path=sg_path)

    print '\n#####################################################################'
    print '#LOADED MODEL:'

    print '\tsg_name: '+sg_name
    print '\tsg_variant: '+sg_variant
    print '\tsg_version: v'+str(sg_version).zfill(3)
    print '\tsg_file_type: '+sg_file_type
    print '\tsg_filename: '+sg_code
    print '\tsg_path: '+sg_path
    print '\n#####################################################################'

    return top_node

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
        path = env.import_stream('model', asset=asset, token=name, version=version, workfile=False)
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

    if not mc.objExists('rig_GRP'):
        return

    # Create model grp IF one does not already exist
    if not top_node == 'model_GRP' and not mc.objExists('model_GRP'):
        top_node = mc.group(top_node, n='model_GRP')
        mc.parent(top_node, 'rig_GRP')
        mc.xform(top_node, piv=[0,0,0])

    elif mc.objExists('model_GRP'):
        mc.parent(top_node, 'model_GRP')

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
    if mc.objExists('rig_GRP'):
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
        if mc.objExists('cache_SEL'):
            mc.sets(shapes, add='cache_SEL')

        else:
            mc.sets(shapes, n='cache_SEL')
            mc.sets('cache_SEL', n='rig_SEL')

        if mc.objExists('engine_SEL'):
            mc.sets(shapes, add='engine_SEL')

    mc.select(top_node)
    return top_node
