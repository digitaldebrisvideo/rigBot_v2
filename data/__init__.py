import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import env

import os
import re
import time
import shutil

"""Module for saving, loading and renaming asset deformers and data. If the asset is set, the default behavior is to save and load
        all data to the asset / variant/ data folder.

        SUPPORTED DATA TYPES:
            :udAttributes: User defined attributes.
            :blendShape: BlendShapes
            :pose: pose Interpolators
            :nonLinear: Non linear deformers
            :skinCluster: Skin clusters
            :cluster: Clusters
            :lattice: Lattices
            :deltaMush: Delta mush deformers
            :sculpt: sculpt deformers
            :cMuscleSystem: cMuscleSystem skin nodes.
            :constraints: Constraints
            :connections: Direct connections
            :sdk: Set driven keyframes
            :stack: Deformation order
            :shaders: Anim shaders and materials
            :kAttributes: Keyable, locked and non-Keyable attributes states adn values.
            :controlShapes: Rig control shapes and colors
            :nCloth: nCloth setup
            :customRig: Custom, hand built rigging
            :lightLocators: Lighting locators

        SUPPORTED CONSTRAINTS:
            :pointConstraint:
            :orientConstraint:
            :parentConstraint:
            :scaleConstraint:
            :aimConstraint:
            :normalConstraint:
            :poleVectorConstraint:
            :tangentConstraint:
            :geometryConstraint:
            :pointOnPolyConstraint:"""

constraint_types = ['pointConstraint',
                   'orientConstraint',
                   'parentConstraint',
                   'scaleConstraint',
                   'aimConstraint',
                   'normalConstraint',
                   'poleVectorConstraint',
                   'tangentConstraint',
                   'geometryConstraint',
                   'pointOnPolyConstraint']

deformer_types = ['skinCluster',
                  'sculpt',
                  'blendShape',
                  'cluster',
                  'deltaMush',
                  'lattice',
                  'nonLinear',
                  'cMuscleSystem']

all_data_types = ['udAttributes',
                  'blendShape',
                  'pose',
                  'nonLinear',
                  'skinCluster',
                  'lattice',
                  'cluster',
                  'deltaMush',
                  'sculpt',
                  'cMuscleSystem',
                  'constraints',
                  'connections',
                  'sdk',
                  'stack',
                  'shaders',
                  'kAttributes',
                  'controlShapes',
                  'spaces',
                  'nCloth',
                  'customRig',
                  'lightLocators']

data_modules = [utils.import_module(i) for i in all_data_types]
file_extentions = [m.file_extention for m in data_modules]
save_all = None

def file_check(file_path):
    """Checks if files existson disk and sets a global setting for the save prompt."""

    global save_all

    if env.using_sandbox:
        save_all = 1
        return True

    if not os.path.isfile(file_path):
        return True

    if save_all == 1:
        return True

    elif save_all == 2:
        shutil.copyfile(file_path, file_path+'.bak')
        print 'Backup created: '+file_path+'.bak'
        return True

    elif save_all == False:
        print 'Skipping..'
        return

    basename = os.path.basename(file_path)
    result = mc.confirmDialog(title='Export Data', message='{0} already exists.\nDo you want to replace it and all other existing files? '.format(basename),
    button=['Overwrite', 'Backup && Export', 'Skip'], icon='warning',
    defaultButton= 'Backup && Export', cancelButton='Skip', dismissString='Skip')

    if result == 'Overwrite':
        save_all = 1
        return True

    elif result == 'Backup && Export':
        shutil.copyfile(file_path, file_path+'.bak')
        print 'Backup created: '+file_path+'.bak'
        save_all = 2
        return True

    save_all = False

def get_file_filter(data_types=[]):
    """Get file filter for import / export"""

    if not data_types:
        data_types = []

    elif not type(data_types) == list:
        data_types = [data_types]

    label = 'Data Files'
    if len(data_types) == 1:
        label = data_types[0]+' Files'

    ext = []
    for dtype in data_types:
        if dtype in all_data_types:
            idx = all_data_types.index(dtype)
            ext.append(file_extentions[idx])

    if not ext:
        ext = file_extentions

    file_filter = '{0} (*{1})'.format(label, ' *'.join(ext))
    return file_filter, label

def rename(data_types=[], nodes=[]):
    """Rename data node based on its connected geo or driver.

        KWARGS:
            :data_types: Types of data to rename. Can be a list of types OR a string for a single type
            :nodes: Specify nodes rename data"""

    if not data_types:
        data_types = deformer_types+['constraints']
    else:
        if type(data_types) is not list:
            data_types = [data_types]

        data_types = [d for d in data_types if d in deformer_types+['constraints']]

    if 'lattice' in data_types:
        i = data_types.index('lattice')
        data_types[i] = 'ffd'

    if 'constraints' in data_types:
        data_types.remove('constraints')
        data_types.append(constraint_types)

    if not nodes:
        nodes = []
        for dtype in data_types:
            nodes.extend(mc.ls(type=dtype))

    new_nodes = []

    for node in nodes:

        if '>>' in node:
            continue

        if mc.objExists(node):
            if mc.nodeType(node) in utils.name_conventions.keys():

                geo = ''
                data_type = mc.nodeType(node)

                if data_type in deformer_types:
                    geo = mc.deformer(node, q=1, g=1)
                    if geo:
                        geo = geo[0].replace('Shape', '')

                elif 'Constraint' in  data_type:
                    geo = mc.listConnections(node+'.constraintParentInverseMatrix')
                    if geo:
                        geo = geo[0]

                elif 'animCurve' in data_type:
                    geo = mc.listConnections(node+'.output', p=1)
                    if geo:
                        geo = geo[0].replace('.', '_')

                if geo:
                    suffix = utils.get_suffix(mc.nodeType(node))

                    new_name = geo+'_'+suffix
                    if node != new_name:
                        new_name = utils.get_unique_name('{0}_#_{1}'.format(geo, suffix))

                        new_name = mc.rename(node, new_name)
                        new_nodes.append(new_name)
                        print 'RENAMED: {0} to {1}'.format(node, new_name)
    return new_nodes

def unfinalize(namespace='*'):
    """Turn ON historical importance on all nodes in scene and make model and joints visible and selectable"""

    utils.set_historical_importance(state=2)

    if namespace:
        namespace += ':'

    attrs = ['visibility_CTL.jointsVis',
            'visibility_CTL.modelVis',
            'visibility_CTL.modelSelectable',
            'visibility_CTL.jointsSelectable']

    attrs += [namespace+'visibility_CTL.jointsVis',
            namespace+'visibility_CTL.modelVis',
            namespace+'visibility_CTL.modelSelectable',
            namespace+'visibility_CTL.jointsSelectable']

    for attr in attrs:
        if mc.objExists(attr):
            mc.setAttr(attr, True)

def save(data_types=[], nodes=[], model=False, asset=None, variant=None, custom_path=None):
    """Save asset deformers and data. If the asset is set, the default behavior is to save
        all data to the asset / variant/ data folder.

        NOTE:
            If "data_types" is not specified then by default all data except "controlShapes" and "kAttributes" will be written out.

        KWARGS:
            :data_types: Types of data to save. Can be a list of types OR a string for a single type
            :nodes: Specify nodes to export data from
            :model: Choose to export data from the entire model hierarchy, A "model_GRP" group node is required.
            :asset: Asset to save to
            :variant: Variant to save to
            :custom_path: Specify a path or file to save OR set to True for a file browser You can save multiple files at once.

        USAGE:
            from rigBot import data

            # Default behavior will look for data folder and save there, otherwise it'll prompot you for a folder
            # Select geo to export from
            data.save()

            # To save to a specific data to a specific location
            data.load('skinCluster', custom_path='my/file/path/node_name.skn')

            # save specifc data for the whole model hierarchy
            data.load(['blendShape', 'skinCluster'], model=True)

        SUPPORTED DATA TYPES:
            :udAttributes: User defined attributes.
            :blendShape: BlendShapes
            :pose: pose Interpolators
            :nonLinear: Non linear deformers
            :skinCluster: Skin clusters
            :cluster: Clusters
            :lattice: Lattices
            :deltaMush: Delta mush deformers
            :sculpt: sculpt deformers
            :constraints: Constraints
            :connections: Direct connections
            :sdk: Set driven keyframes
            :stack: Deformation order
            :shaders: Anim shaders and materials
            :kAttributes: Keyable, locked and non-Keyable attributes states adn values.
            :controlShapes: Rig control shapes and colors"""

    if not utils.check_historical_importance():
        response = mc.confirmDialog(title='rigBot 2.0', message='Can\'t export data because the rig is locked \nWould you like to unfinalize the rig and proceed exporting data?', button=[' Yes, unfinalize rig ','Cancel'], defaultButton=' Yes, unfinalize rig ', cancelButton='Cancel', dismissString='Cancel')
        if response == ' Yes, unfinalize rig ':
            unfinalize()
        else:
            return

    global save_all

    # Process data types list, Poseinterps and controls are going to be handled differently
    if not data_types:
        data_types = [d for d in all_data_types]

        # These dont automatically get exported
        data_types.remove('kAttributes')
        data_types.remove('controlShapes')
        data_types.remove('shaders')
        data_types.remove('spaces')
        data_types.remove('nCloth')
        data_types.remove('customRig')
        data_types.remove('lightLocators')

    else:
        if type(data_types) is not list:
            data_types = [data_types]

        data_types = [d for d in data_types if d in all_data_types]

    # First get selected nodes OR model hierarchy
    if model:
        model_grp = mc.ls('model_GRP', 'model_grp', 'model')
        if not model_grp:
            mc.warning('"model" OR "model_GRP" not found!')
            return

        selection = utils.get_children(model_grp, ad=1)

    elif nodes:
        selection = mc.ls(nodes)

    else:
        selection = mc.ls(sl=1)

    if 'pose' in data_types:
        pose_nodes = data_modules[2].get_pose_nodes() + data_modules[2].get_translation_pose_nodes()
        if pose_nodes:
            selection.extend(pose_nodes)

    if not selection:
        if 'lightLocators' not in data_types and 'customRig' not in data_types and 'shaders' not in data_types and 'controlShapes' not in data_types and 'kAttributes' not in data_types:

            mc.warning('Nothing selected for export!')
            return

    # Get asset adn veraint
    if not asset:
        asset = env.get_asset()

    if not variant:
        variant = env.get_variant()

    # IF set to tru prtompt for a path
    file_filter, filter_label = get_file_filter(data_types)

    if custom_path == True:
        base_path = utils.file_browser('SAVE MULTIPLE', file_filter=file_filter)
        if not base_path:
            return

    #OR use the specireed custom path
    elif custom_path and os.path.isdir(custom_path):
        base_path = utils.file_browser('SAVE MULTIPLE', file_filter=file_filter, file_path=custom_path)
        if not base_path:
            return

    # OR use the rig build path
    elif asset and variant:
        base_path = os.path.join(env.get_rigbuild_path(), 'data', variant)
        utils.make_dirs(base_path)

        base_path = utils.file_browser('SAVE MULTIPLE', file_filter=file_filter, file_path=base_path)
        if not base_path:
            return
    else:
        base_path = utils.file_browser('SAVE MULTIPLE', file_filter=file_filter)
        if not base_path:
            return

    if type(base_path) is list:
        base_path = base_path[0]

    utils.make_dirs(base_path)

    # EXport stuff for each node
    tr_pose_nodes = data_modules[2].get_translation_pose_nodes()
    pose_nodes_in_scene = data_modules[2].get_pose_nodes()+tr_pose_nodes

    exported_buffer = []

    for node in selection:
        for data_type in data_types:

            ext = file_extentions[all_data_types.index(data_type)]
            module = data_modules[all_data_types.index(data_type)]

            # Save deformer stack
            if data_type == 'stack':
                if node not in exported_buffer:

                    file_path = os.path.join(base_path, node+ext)
                    exported_buffer.append(node)

                    if file_check(file_path):
                        module.save(file_path, node)

            # Set set driven keys
            elif data_type == 'sdk':
                sdk_node = node.split('.')[0].split('\n')[0]

                if 'animCurve' in mc.nodeType(node):
                    cnn = mc.listConnections(node+'.output', p=0) or []
                    if cnn:
                        sdk_node = cnn[0]

                elif mc.listConnections(node, type='animCurve', d=0, s=1):
                    sdk_node = node

                if sdk_node:
                    if sdk_node not in exported_buffer:
                        basename = sdk_node.replace('.', '_')
                        file_path = os.path.join(base_path, basename+ext)
                        exported_buffer.append(sdk_node)

                        if file_check(file_path):
                            module.save(file_path, sdk_node)

            # connections
            elif data_type == 'connections':

                if '>>' in node:
                    attrs = [node.split('>>')[1].strip()]

                else:
                    if '.' in node:
                        attrs = [node]

                    else:
                        attrs = [node+'.'+a for a in mc.listAttr(node, k=1) or [] if '.' not in a]
                        if mc.nodeType(node) == 'blendShape':
                            attrs.extend([node+'.weight[{0}]'.format(i) for i in range(mc.blendShape(node, q=1, wc=1))])

                for attr in attrs:
                    if attr not in exported_buffer:
                        attrname = attr.replace('.','_')
                        file_path = os.path.join(base_path, attrname+ext)
                        exported_buffer.append(attr)

                        excluded_types = ['animCurve', 'blendWeighted', 'Constraints']
                        source = [s for s in mc.listConnections(attr, s=1, d=0, p=1) or []
                                                if mc.nodeType(s) not in excluded_types]
                        if source:
                            if 'Constraint' not in mc.nodeType(source[0].split('.')[0]):
                                if 'animCurve' not in mc.nodeType(source[0].split('.')[0]):
                                    if 'blendWeighted' not in mc.nodeType(source[0].split('.')[0]):

                                        cnn_data = {attr: source[0]}
                                        if file_check(file_path):
                                            module.save(file_path, data=cnn_data)

            # User Defined attrs
            elif data_type == 'udAttributes':
                if '.' in node:
                    node = node.split('.')[0]

                if mc.listAttr(node, ud=1):
                    if node not in exported_buffer:
                        file_path = os.path.join(base_path, node+ext)
                        exported_buffer.append(node)

                        if file_check(file_path):
                            module.save(file_path, node)

            # constraints
            elif data_type == 'constraints':
                if mc.nodeType(node) in constraint_types:
                    cons = [node]
                else:
                    cons = [c for c in utils.get_constraints(node) if c in constraint_types]

                for con in cons:
                    if con not in exported_buffer:
                        exported_buffer.append(con)
                        file_path = os.path.join(base_path, con+ext)
                        if file_check(file_path):
                            module.save(file_path, con)

            # get pose nodes
            elif data_type == 'pose':
                if node in pose_nodes_in_scene:
                    if node not in exported_buffer:
                        exported_buffer.append(node)

                        if node in tr_pose_nodes:
                            ext = '.trpose'

                        file_path = os.path.join(base_path, node+ext)
                        if file_check(file_path):
                            module.save(file_path, node)

            # All other deformers
            elif data_type in deformer_types:

                node_type = data_type
                if data_type == 'lattice':
                    node_type = 'ffd'

                export_nodes = []

                if mc.nodeType(node) == node_type:
                    export_nodes = [node]
                else:
                    export_nodes = utils.get_deformers(node, node_type)

                if export_nodes:
                    for ex_node in export_nodes:
                        if ex_node not in exported_buffer:
                            file_path = os.path.join(base_path, utils.strip_namespace(ex_node)+ext)
                            exported_buffer.append(ex_node)

                            if file_check(file_path):
                                module.save(file_path, ex_node)

    # get all control shapes
    if 'controlShapes' in data_types:
        ext = file_extentions[all_data_types.index('controlShapes')]
        module = data_modules[all_data_types.index('controlShapes')]
        token = variant+'_rig'
        token = re.sub('_+', '_', token)
        if token.startswith('_'):
            token = token[1:]

        file_path = os.path.join(base_path, token+ext)
        if file_check(file_path):
            module.save(file_path)

    if 'shaders' in data_types:
        ext = file_extentions[all_data_types.index('shaders')]
        module = data_modules[all_data_types.index('shaders')]
        token = variant+'_rig'
        token = re.sub('_+', '_', token)
        if token.startswith('_'):
            token = token[1:]

        file_path = os.path.join(base_path, token+ext)
        if file_check(file_path):
            if selection:
                module.save(file_path, nodes=selection)
            else:
                module.save(file_path)

    if 'kAttributes' in data_types:
        module = data_modules[all_data_types.index('kAttributes')]
        ext = '.kattrs'
        token = variant+'_rig'
        token = re.sub('_+', '_', token)
        if token.startswith('_'):
            token = token[1:]

        file_path = os.path.join(base_path, token+ext)
        if file_check(file_path):
            module.save(file_path)

    if 'spaces' in data_types:
        ext = '.spaces'
        token = variant+'_rig'
        token = re.sub('_+', '_', token)
        if token.startswith('_'):
            token = token[1:]

        file_path = os.path.join(base_path, token+ext)
        if file_check(file_path):
            spaces.save_all(file_path, nodes=nodes)

    if 'nCloth' in data_types:
        module = data_modules[all_data_types.index('nCloth')]
        ext = '.ncloth'
        token = variant+'_rig'
        token = re.sub('_+', '_', token)
        if token.startswith('_'):
            token = token[1:]

        file_path = os.path.join(base_path, token+ext)
        if file_check(file_path):
            module.save(file_path)

    if 'customRig' in data_types:
        ext = customRig.file_extention
        token = variant+'_rig'
        token = re.sub('_+', '_', token)
        if token.startswith('_'):
            token = token[1:]

        file_path = os.path.join(base_path, token+ext)
        if file_check(file_path):
            customRig.save(file_path)

    if 'lightLocators' in data_types:
        ext = lightLocators.file_extention
        token = variant+'_rig'
        token = re.sub('_+', '_', token)
        if token.startswith('_'):
            token = token[1:]

        file_path = os.path.join(base_path, token+ext)
        if file_check(file_path):
            lightLocators.save(file_path)

    print 'Finished exporting data!'
    save_all = None

def load(data_types=[], asset=None, variant=None, custom_path=None, remap=False, closest_point=False):
    """Load asset deformers and data. If the asset is set, the default behavior is to load
        all data to the asset / variant/ data folder.

        NOTE:
            If "data_types" is not specified then by default all data except "controlShapes" and "kAttributes" will be loaded.

        KWARGS:
            :data_types: Types of data to import. Can be a list of types OR a string for a single type
            :asset: Asset to load from
            :variant: Variant to load from
            :custom_path: Specify a path or file to load OR set to True for a file browser. You can import multiple files at once.
            :remap: Remap node names on import.
            :closest_point: Load deformer weights by closest point instead of by vertexID

        USAGE:
            from rigBot import data

            # Default behavior will look for the data in asset, variant data folder and prompt you if nothing is found.
            data.load()

            # To load a specific file
            data.load(custom_path='my/file/path/node_name.skn')

            # To browse for files
            data.load(custom_path=True)

        SUPPORTED DATA TYPES:
            :udAttributes: User defined attributes.
            :blendShape: BlendShapes
            :pose: pose Interpolators
            :nonLinear: Non linear deformers
            :skinCluster: Skin clusters
            :cluster: Clusters
            :lattice: Lattices
            :deltaMush: Delta mush deformers
            :sculpt: sculpt deformers
            :constraints: Constraints
            :connections: Direct connections
            :sdk: Set driven keyframes
            :stack: Deformation order
            :kAttributes: Keyable, locked and non-Keyable attributes states adn values.
            :controlShapes: Rig control shapes and colors"""


    def get_data_files(base_path, data_types):

        if not os.path.isdir(base_path):
            mc.warning(base_path+' does not exist!')
            return []

        file_paths = []
        exts = []
        for dtype in data_types:
            i = all_data_types.index(dtype)
            exts.append(file_extentions[i])

        for f in os.listdir(base_path) or []:
            ext = '.'+'.'.join(f.split('.')[1:])
            if ext in exts:
                file_paths.append(os.path.join(base_path, f))

        return file_paths

    if not utils.check_historical_importance():
        response = mc.confirmDialog(title='rigBot 2.0', message='Can\'t export data because the rig is locked \nWould you like to unfinalize the rig and proceed exporting data?', button=[' Yes, unfinalize rig ','Cancel'], defaultButton=' Yes, unfinalize rig ', cancelButton='Cancel', dismissString='Cancel')
        if response == ' Yes, unfinalize rig ':
            unfinalize()
        else:
            return

    # Process data types list, Poseinterps and controls are going to be handled differently
    if not data_types:
        data_types = [d for d in all_data_types]

        # These dont automatically get loaded
        data_types.remove('kAttributes')
        data_types.remove('controlShapes')
        data_types.remove('spaces')
        data_types.remove('customRig')
        data_types.remove('lightLocators')

    else:
        if type(data_types) is not list:
            data_types = [data_types]

        data_types = [d for d in all_data_types if d in data_types]

    file_filter, filter_label = get_file_filter(data_types)
    file_paths = []

    if remap:
        if custom_path in [None, False]:
            custom_path=True

    # Get asset and veraint
    if not asset:
        asset = env.get_asset()

    if not variant:
        variant = env.get_variant()

    # IF set to tru prtompt for a path
    file_filter, filter_label = get_file_filter(data_types)
    if custom_path == True:
        if remap:
            file_paths = utils.file_browser('LOAD', file_filter=file_filter)
        else:
            file_paths = utils.file_browser('LOAD MULTIPLE', file_filter=file_filter)
        if not file_paths:
            return

    #OR use the specireed custom path
    elif custom_path and os.path.isdir(custom_path):
        base_path = custom_path
        if remap:
            mc.warning('Can only remap one file at a time! Choose one..')
            file_paths = utils.file_browser('LOAD', file_filter=file_filter)
        else:
            file_paths = get_data_files(base_path, data_types)

    # OR if this is an actual
    elif custom_path and os.path.isfile(custom_path):
        file_paths = [custom_path]

    # OR use the rig build path
    elif asset and variant:
        base_path = os.path.join(env.get_rigbuild_path(), 'data', variant)
        if not os.path.isdir(base_path):
            base_path = os.path.join(env.get_rigbuild_path(), 'data', 'default')

        if not os.path.isdir(base_path):
            return

        file_paths = get_data_files(base_path, data_types)
    else:
        if remap:
            file_paths = utils.file_browser('LOAD', file_filter=file_filter)
        else:
            file_paths = utils.file_browser('LOAD MULTIPLE', file_filter=file_filter)
        if not file_paths:
            return

    file_extentions_to_load = []
    for dtype in data_types:
        i = all_data_types.index(dtype)
        file_extentions_to_load.append(file_extentions[i])

    for ext_type in file_extentions_to_load:
        di = file_extentions.index(ext_type)
        data_type = all_data_types[di]

        print '\n############################################################'
        print 'LOADING DATA TYPE: '+data_type

        for file_path in file_paths:
            ext =  '.'+'.'.join(file_path.split('.')[1:])
            if ext == ext_type:
                i = file_extentions.index(ext)
                module = data_modules[i]

                try:
                    mc.undoInfo(openChunk=True)
                    module.load(file_path=file_path, remap=remap, closest_point=closest_point)
                    mc.undoInfo(closeChunk=True)

                except:
                    mc.undoInfo(closeChunk=True)
                    exception = utils.get_exception()
                    if exception:
                        raise RuntimeError(exception)

    print '\nFinished loading data!'



