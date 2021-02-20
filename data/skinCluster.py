import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
import maya.OpenMayaAnim as oma

import cPickle as pickle
import time
import os

from rigBot import utils
from rigBot.gui import remapDialog

file_extention = '.skn'
deformer_type = 'skinCluster'

class SkinCluster(object):
    """Class for exporting, import and manipulating skin nonLinears"""

    def __init__(self, selection=None):

        deformer, shapes = utils.get_deformers_and_shapes(selection, deformer_type)

        if not deformer:
            raise ValueError('Deformer not found!')

        if not shapes:
            raise ValueError('Shapes not found for: {0}!'.format(deformer))

        self.deformer = deformer
        self.shape = shapes[0]

        self.def_set = mc.listConnections(self.deformer, type='objectSet')[0]
        self.def_cmpts = mc.ls(mc.sets(self.def_set, q=1), fl=1)

        # Get skin cluster api info
        self.skn_obj = om.MObject()
        self.skn_dag_path = om.MDagPath()
        self.skn_cmpts = om.MObject()
        self.skn_members = om.MSelectionList()

        sel_list = om.MSelectionList()
        sel_list.add(self.deformer)
        sel_list.getDependNode(0, self.skn_obj)

        self.fn_skn =  oma.MFnSkinCluster(self.skn_obj)
        self.fn_set = om.MFnSet(self.fn_skn.deformerSet())
        self.fn_set.getMembers(self.skn_members, False)
        self.skn_members.getDagPath(0, self.skn_dag_path, self.skn_cmpts)

    def get_data(self):
        """Gather all info pertaining to this skincluster"""

        # Get weights
        self.get_weights()
        self.get_blend_weights()

        # get scls attributes
        self.skinning_method = mc.getAttr(self.deformer+'.skinningMethod')
        self.normalize_weights = mc.getAttr(self.deformer+'.normalizeWeights')

        # Get orig mesh data to recreate mesh
        orig_shape = utils.get_orig_shape(self.shape)
        shape_data = utils.get_mesh_data(orig_shape)

        # build data dict
        self.data = {
            'name': self.deformer,
            'shape': utils.strip_namespace(self.shape),
            'skinningMethod': self.skinning_method,
            'normalizeWeights': self.normalize_weights,
            'weights': self.weights,
            'blendWeights': list(self.blend_weights),
            'meshData': shape_data
        }

    def get_blend_weights(self):
        """Get blend weights, stored in MDoubleArray"""

        self.blend_weights = om.MDoubleArray()

        self.fn_skn.getBlendWeights(self.skn_dag_path,
                                    self.skn_cmpts,
                                    self.blend_weights)

        return self.blend_weights

    def get_weights(self):
        """Get all weights for all influences as a dict"""

        self.weights = {}

        weights = self.get_weights_array()

        inf_path_array = om.MDagPathArray()
        number_infs = self.fn_skn.influenceObjects(inf_path_array)
        number_cmpts_per_inf = weights.length() / number_infs

        for i in range(inf_path_array.length()):
            inf_name = mc.ls(inf_path_array[i].fullPathName(), sn=1)[0]
            inf_name = utils.strip_namespace(inf_name)

            weight_list = [weights[ii*number_infs+i] for ii in range(number_cmpts_per_inf)]
            self.weights[inf_name] = weight_list

        return self.weights

    def get_weights_array(self):
        """Get MDoubleArray list of weights from deformer node"""

        weights = om.MDoubleArray()

        p_int_util = om.MScriptUtil()
        p_int_util.createFromInt(0)
        p_int = p_int_util.asUintPtr()

        self.fn_skn.getWeights(self.skn_dag_path, self.skn_cmpts, weights, p_int)

        return weights

    def save(self, file_path):
        """Export skin weights to disk"""

        if not file_path:
            return

        t = time.time()
        self.get_data()
        utils.write_pickle(file_path, self.data)

        print time.time() - t

    def set_data(self, data):
        """Set skin cluster data, weights and blend weights from a data dict."""

        self.skinning_method = data['skinningMethod']
        self.normalize_weights = data['normalizeWeights']

        mc.setAttr(self.deformer+'.deformUserNormals', 0)
        mc.setAttr(self.deformer+'.skinningMethod', self.skinning_method)
        mc.setAttr(self.deformer+'.normalizeWeights', self.normalize_weights)

    def set_blend_weights(self, blend_weights):
        """Set blend weights from a list of floats"""

        blend_weights_array = om.MDoubleArray(len(blend_weights))
        for i, w in enumerate(blend_weights):
            blend_weights_array.set(w, i)

        self.fn_skn.setBlendWeights(self.skn_dag_path, self.skn_cmpts, blend_weights_array)
        self.blend_weights = blend_weights

    def set_weights(self, weights_dict):
        """Set weights from weight data dict"""

        mc.setAttr(self.deformer+'.normalizeWeights', 0)

        weights = self.get_weights_array()
        inf_path_array = om.MDagPathArray()

        number_infs = self.fn_skn.influenceObjects(inf_path_array)
        number_cmpts_per_inf = weights.length() / number_infs

        try:
            for influence, weight_list in weights_dict.items():
                for i in range(inf_path_array.length()):
                    inf_name = mc.ls(inf_path_array[i].fullPathName(), sn=1)[0]
                    inf_name = utils.strip_namespace(inf_name)

                    # store weights in mdouble array
                    if inf_name == influence:
                        for ii in range(number_cmpts_per_inf):
                            weights.set(weight_list[ii], ii*number_infs+i)
        except:
            return

        self.set_weights_array(weights)
        self.weights = weights_dict

        return True

    def set_weights_array(self, weights_array):
        """This sets the weights from an MDoubleArray input object."""

        inf_path_array = om.MDagPathArray()
        number_infs = self.fn_skn.influenceObjects(inf_path_array)

        inf_indecies = om.MIntArray(number_infs)
        for i in range(number_infs):
            inf_indecies.set(i, i)

        # set weights
        mc.setAttr(self.deformer+'.normalizeWeights', 0)

        self.fn_skn.setWeights(self.skn_dag_path, self.skn_cmpts, inf_indecies, weights_array, False)

        mc.setAttr(self.deformer+'.normalizeWeights', 1)

    @classmethod
    def load(self, file_path=None, closest_point=False, smooth=False, remap=False, data={}, optimize=False):
        """import weights from disk"""

        # Start timer for load process
        t = time.time()

        if not data and not file_path:
            mc.warning('Must either specify a file path OR provide data.')
            return

        elif file_path and not data:
            data = utils.read_pickle(file_path)

        # get data
        name = data.get('name')
        shape = data.get('shape')
        weights = data.get('weights')
        blend_weights = data.get('blendWeights')
        mesh_data = data.get('meshData')

        influences = mc.ls(weights.keys())
        test_shape = mc.ls(shape)

        # check if this import has all the nodes it needs in scene
        if remap or len(test_shape) != 1 or not len(influences) == len(weights.keys()):
            return data

        # unbind current geo
        if utils.get_deformers(shape, 'skinCluster'):
            mc.skinCluster(shape, e=1, ub=1)

        # Create new skin cluster
        deformer = mc.skinCluster(shape, influences, tsb=1, n=name)[0]

        new_skn_obj = SkinCluster(deformer)
        new_skn_obj.set_data(data)

        # if closest_point thne recreate the original mesh and copy weights
        if closest_point:

            # recreate the original mesh for all shapes
            matrix = mesh_data.get('matrix')
            points = mesh_data.get('points')
            triangles = mesh_data.get('triangles')

            tmp_shape = utils.create_mesh_from_data(matrix, points, triangles)[0]

            # Create the temp deformer and apply weights
            tmp_deformer = mc.skinCluster(tmp_shape, influences, tsb=1)[0]

            tmp_skn_obj = SkinCluster(tmp_deformer)
            tmp_skn_obj.set_blend_weights(blend_weights)
            tmp_skn_obj.set_weights(weights)

            # Copy weights from old skinCluters to new one
            mc.copySkinWeights(ss=tmp_deformer, ds=deformer, nm=1, sm=smooth, sa='closestPoint', ia='oneToOne')
            mc.copySkinWeights(ss=tmp_deformer, ds=deformer, nm=1, sm=smooth, nbw=1, sa='closestPoint', ia='oneToOne')

            # Delete all the temp junk
            mc.delete(tmp_deformer, tmp_shape)

        # OR if not closest_point just apply the weights
        else:

            new_skn_obj.set_blend_weights(blend_weights)
            result = new_skn_obj.set_weights(weights)

            if not result:
                mc.delete(deformer)
                mc.warning('Cannot set weights! Vert count does not match data in file. Use closest_point=True')
                return

        if optimize:
            mc.select(shape)
            self.optimize(self, prune_weights=None, remove_unused_influences=False, rebuild=True, bake_history=False)

        # Print load time
        print time.time() - t

    def optimize(self, prune_weights=0.01, remove_unused_influences=True, rebuild=True, bake_history=False):
        """Prune weights, remove unused influences and rebuild skin cluster"""

        t = time.time()

        # prune_weights
        if prune_weights is not None and prune_weights > 0.001:
            mc.skinPercent(self.deformer, self.shape, prw=prune_weights)
            print 'Pruned weights for: '+self.deformer

        # remove unused
        if remove_unused_influences:
            weighted_infs = mc.skinCluster(self.deformer, q=1, wi=1)
            unweighted_infs = [i for i in mc.skinCluster(self.deformer, q=1, inf=1) if i not in weighted_infs]

            for i in unweighted_infs:
                mc.skinCluster(self.deformer, e=1, ri=i)
                print 'Removed unused influence: {1} for: {0}.'.format(self.deformer, i)

        if rebuild:

            # get weights and deformer info
            weight_array = self.get_weights_array()
            blend_weights = self.get_blend_weights()
            influences = mc.skinCluster(self.deformer, q=1, inf=1)
            skinning_method = mc.getAttr(self.deformer+'.skinningMethod')
            normalize_weights = mc.getAttr(self.deformer+'.normalizeWeights')

            # Get deformation stack
            stack = mc.listHistory(self.shape, il= 1, pdo=1)

            # unbind or bake pose
            if bake_history:
                mc.delete(self.shape, ch=1)
            else:
                mc.skinCluster(self.shape, e=1, ub=1)

            # recreate skin cluster
            deformer = mc.skinCluster(self.shape, influences, tsb=1, n=self.deformer)[0]
            new_skn_obj = SkinCluster(deformer)

            # set weights and deformer values
            mc.setAttr(new_skn_obj.deformer+'.deformUserNormals', 0)
            mc.setAttr(new_skn_obj.deformer+'.skinningMethod', skinning_method)
            mc.setAttr(new_skn_obj.deformer+'.normalizeWeights', normalize_weights)
            new_skn_obj.set_weights_array(weight_array)
            new_skn_obj.set_blend_weights(blend_weights)

            # reorder deformer stack
            if len(stack) > 2:
                for i in range(len(stack)-1):
                    try:
                        mc.reorderDeformers(stack[i], stack[i+1], self.shape)
                    except:
                        pass

            # reinitialize this object with the new deformer
            self.__init__(deformer)

            print 'Rebuilt skinCluster: '+deformer

        print time.time() - t

class RemapSkinCluster(remapDialog.RemapDialog):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, nodes=[], ignore_missing=False, label=''):
        remapDialog.RemapDialog.__init__(self, nodes, False, 'Skin Cluster Remap UI')

        self.data = {}

    def map_selection(self):
        """Map selectio nto node"""

        items = self.ui.node_tree.selectedItems() or []
        sel = mc.ls(sl=1)

        if items and sel:
            for item in items:
                if 'Shape' in item.text(0):
                    shape = utils.get_shapes(sel[0])
                    if not shape:
                        mc.warning('This node needs a shape to remap!')
                        return

                    sel = shape

                node = item.text(0)
                item.setText(2, sel[0])
                self.mapping[node] = sel[0]

        elif not sel:
            mc.warning('Nothing selected!')

    def finish_command(self):
        """update data dict with new mapping and load the data"""

        orig_shape = self.data.get('shape')
        influences = self.data.get('weights').keys()

        new_shape = str(orig_shape)
        new_influences = list(influences)

        # remap new shape
        if orig_shape in self.mapping.keys():
            self.data['shape'] = self.mapping.get(orig_shape)

        for inf, value in self.data['weights'].items():
            new_inf = self.mapping[inf]
            if new_inf != inf:
                self.data['weights'][new_inf] = value
                del self.data['weights'][inf]

        result = SkinCluster.load(closest_point=self.closest_point, smooth=self.smooth, data=self.data, optimize=True)

def save(file_path, deformer):
    """Wrapper for class export call, Can export multiple and
        prompts for file path"""

    if not file_path.endswith(file_extention):
        file_path = os.path.splitext(file_path)[0]+file_extention

    obj = SkinCluster(deformer)
    obj.save(file_path)

def load(file_path, closest_point=False, smooth=False, remap=False):
    """Wrapper for importing weights"""

    # Get files for loading

    # Load remaping dialog
    if remap == True:
        data = SkinCluster.load(file_path, smooth=smooth, closest_point=closest_point, remap=True)

        if type(data) == dict:

            # get nodes to remap
            nodes = [data.get('shape')]
            nodes.extend(data.get('weights').keys())

            remap_dialog = RemapSkinCluster(nodes=nodes)
            remap_dialog.closest_point = closest_point
            remap_dialog.smooth = smooth
            remap_dialog.data = data
            remap_dialog.show()
            return

    # If not remap then load as usual
    else:
        result = SkinCluster.load(file_path, smooth=smooth, closest_point=closest_point)

        # warn and skip if a remap is needed.
        if type(result) == dict:
            mc.warning('{0} needs remapping! File path: {1}'.format(result['name'], file_path))


def optimize(selection=None, prune_weights=0.01, remove_unused_influences=True, rebuild=True, bake_history=False):
    """Wrapper for class optimize call,
        Can prune weights, remove unused influences, and rebuild the skincluster.
        default does all three.
    """

    if not utils.check_historical_importance():
        response = mc.confirmDialog(title='rigBot 2.0', message='Can\'t export data because the rig is locked \nWould you like to unfinalize the rig and proceed exporting data?', button=[' Yes, unfinalize rig ','Cancel'], defaultButton=' Yes, unfinalize rig ', cancelButton='Cancel', dismissString='Cancel')
        if response == ' Yes, unfinalize rig ':
            unfinalize()
        else:
            return

    if selection is None:
        selection = mc.ls(sl=1)

    selection = mc.ls(selection)

    # first get deformers for all selected items
    deformers = []
    for node in selection:
        deformers.extend(utils.get_deformers(node, deformer_type))

    deformers = list(set(deformers))

    for deformer in deformers:
        skn_obj = SkinCluster(deformer)
        skn_obj.optimize(prune_weights=prune_weights,
                         remove_unused_influences=remove_unused_influences,
                         rebuild=rebuild,
                         bake_history=bake_history)


def copy_bind(selection=None, bake_history=False, smooth=False):
    """Copy bind from one meshto another"""

    if not utils.check_historical_importance():
        response = mc.confirmDialog(title='rigBot 2.0', message='Can\'t export data because the rig is locked \nWould you like to unfinalize the rig and proceed exporting data?', button=[' Yes, unfinalize rig ','Cancel'], defaultButton=' Yes, unfinalize rig ', cancelButton='Cancel', dismissString='Cancel')
        if response == ' Yes, unfinalize rig ':
            unfinalize()
        else:
            return

    selection = mc.ls(selection)
    if not len(selection) > 2:
        selection = mc.ls(sl=1)

    if len(selection) < 2:
        msg = 'Select at least two meshs. First, the mesh to copy from, ' +\
              'then the mesh / meshes to copy to.'

        mc.warning(msg)
        return

    # set up time and valid shapes
    t = time.time()
    valid_types = ['mesh', 'nurbsCurve', 'nurbsSurface']

    # sort selection
    source_mesh = selection[0]
    target_meshs = selection[1:]

    # get defomer data
    source_deformer = utils.get_deformers(source_mesh, 'skinCluster')[0]
    influences = mc.skinCluster(source_deformer, q=1, inf=1)
    skinning_method = mc.getAttr(source_deformer+'.skinningMethod')
    normalize_weights = mc.getAttr(source_deformer+'.normalizeWeights')

    # loop throug hall targets and copy bind
    for target in target_meshs:

        # check shapes
        shapes = utils.get_shapes(target)
        target_shape = [s for s in shapes if mc.nodeType(s) in valid_types]

        if shapes and not target_shape:
            mc.warning('Shape: {0} is not valid! Skipping..'.format(shapes[0]))
            continue

        # unbind IF its already bound
        if utils.get_deformers(target, 'skinCluster'):
            if bake_history:
                mc.delete(target, ch=1)
            else:
                mc.skinCluster(target, e=1, ub=1)

        # bind target geo
        target_deformer = mc.skinCluster(target_shape[0], influences, tsb=1)[0]

        # apply values
        mc.setAttr(target_deformer+'.deformUserNormals', 0)
        mc.setAttr(target_deformer+'.skinningMethod', skinning_method)
        mc.setAttr(target_deformer+'.normalizeWeights', normalize_weights)

        # copy weights
        mc.copySkinWeights(ss=source_deformer, ds=target_deformer, sm=smooth, nm=1, sa='closestPoint', ia='oneToOne')
        mc.copySkinWeights(ss=source_deformer, ds=target_deformer, sm=smooth, nm=1, nbw=1, sa='closestPoint', ia='oneToOne')

        print 'Copied skinCluster from: {0} to: {1} (closestPoint)'.format(source_mesh, target)
        print time.time() - t


class RigidWeights():

    source_vert = None
    source_scls = None
    source_infs = []
    source_weights = []

    def __init__(self, source_vert=None):
        self.set_source_vert(source_vert)

    def set_source_vert(self, source_vert=None):

        self.source_vert = None
        self.source_scls = None
        self.source_infs = []
        self.source_weights = []

        if source_vert:
            sel = mc.ls(source_vert)

        else:
            mm.eval('convertToVerts')
            sel = mc.ls(sl=1, fl=1)

        sel = mc.ls(sel)
        if sel and '.vtx' in sel[0]:
            self.source_vert = sel[0]
        else:
            mc.warning('No vert selected!')
            return


        self.source_scls = utils.get_deformers(self.source_vert, 'skinCluster')
        if not self.source_scls:
            mc.warning(self.source_vert+' is not bound!')
            return

        self.source_scls = self.source_scls[0]
        self.source_weights = mc.skinPercent(self.source_scls, self.source_vert, q=1, v=1)
        self.source_infs = mm.eval('skinPercent -ib -0.001 -query  -t '+self.source_scls+' '+self.source_vert)

        print 'Set source vert: '+self.source_vert

    def set_weights(target_verts=[]):

        if not self.source_vert:
            mc.warning('Source vert not set!')
            return

        if not target_verts:
            mm.eval('convertToVerts')
            target_verts = mc.ls(sl=1)

        target_meshs = list(set([v.split('.')[0] for v in target_verts]))
        target_scls = [utils.get_deformers(m, 'skinCluster') for m in target_meshs]
        target_vert_sets = []

        for i, mesh in enumerate(target_meshs):
            target_vert_sets.append([v for v in target_verts if v.startswith(mesh)])

        value_arg = 'skinPercent '
        for i in range(len(self.source_weights)):
            value_arg += '-transformValue {0} {1} '.format(self.source_infs[i], self.source_weights[i])

        for i, verts in enumerate(target_vert_sets):
            arg = '{0} {1} {2}'.format(value_arg, target_scls[i][0], ' '.join(verts))
            mm.eval(arg)
            print 'Set rigid weights for: '+target_scls[i][0]

def get_joints(select=False):
    """Print joint/ influence count for skincluster on selected geo."""

    if not utils.check_historical_importance():
        response = mc.confirmDialog(title='rigBot 2.0', message='Can\'t export data because the rig is locked \nWould you like to unfinalize the rig and proceed exporting data?', button=[' Yes, unfinalize rig ','Cancel'], defaultButton=' Yes, unfinalize rig ', cancelButton='Cancel', dismissString='Cancel')
        if response == ' Yes, unfinalize rig ':
            unfinalize()
        else:
            return

    geo = mc.ls(sl=1)
    if not geo:
        raise ValueError('Nothing saelected!')

    skns = [mm.eval('findRelatedSkinCluster '+g) for g in geo]

    if not skns:
        raise ValueError('No skinCluster found!')

    all_infs = []
    for s in skns:
        infs = mc.skinCluster(s, q=1, inf=1) or []
        for i in infs:
            if i not in all_infs:
                all_infs.append(i)

    if select:
        mc.select(all_infs)

    return infs

def joint_count():

    if not utils.check_historical_importance():
        response = mc.confirmDialog(title='rigBot 2.0', message='Can\'t export data because the rig is locked \nWould you like to unfinalize the rig and proceed exporting data?', button=[' Yes, unfinalize rig ','Cancel'], defaultButton=' Yes, unfinalize rig ', cancelButton='Cancel', dismissString='Cancel')
        if response == ' Yes, unfinalize rig ':
            unfinalize()
        else:
            return

    infs = get_joints()
    print '\n####################################'
    print 'joint count: {0}'.format(str(len(infs)))

