import maya.cmds as mc
import maya.mel as mm

import cPickle as pickle
import time
import os

from rigBot import utils
from rigBot.gui import remapDialog

file_extention = '.dmush'
deformer_type = 'deltaMush'

class DeltaMush(object):
    """Class for exporting, import and manipulating skin nonLinears"""

    def __init__(self, selection=None):

        deformer, shapes = utils.get_deformers_and_shapes(selection, deformer_type)

        if not deformer:
            raise ValueError('Deformer not found!')

        if not shapes:
            raise ValueError('Shapes not found for: {0}!'.format(deformer))

        self.deformer = deformer
        self.shapes = shapes

        self.def_set = mc.listConnections(self.deformer, type='objectSet')[0]
        self.def_cmpts = mc.ls(mc.sets(self.def_set, q=1), fl=1)

    def get_data(self):

        # get all xforms and attr values
        deformer_attrs = ['smoothingIterations',
                          'smoothingStep',
                          'pinBorderVertices',
                          'displacement',
                          'scaleX',
                          'scaleY',
                          'scaleZ']

        attr_dict = {}
        for attr in deformer_attrs:
            if mc.objExists(self.deformer+'.'+attr):
                attr_dict[attr] = round(mc.getAttr(self.deformer+'.'+attr), 3)

        # get weights
        weights = []
        for i in range(len(self.shapes)):
            try:
                index_weight = list(mc.getAttr('{0}.weightList[{1}].weights'.format(self.deformer, i))[0])
            except:
                index_weight = []

            weights.append(index_weight)

        # get mesh data
        mesh_data = {}

        for shape in self.shapes:
            orig_shape = utils.get_orig_shape(shape)
            shape_data = utils.get_mesh_data(orig_shape)
            mesh_data[shape] = shape_data

        # Create data dict
        self.data = {
            'name' : self.deformer,
            'shapes' : self.shapes,
            'setMembers' : self.def_cmpts,
            'attrValues' : attr_dict,
            'weights' : weights,
            'meshData' : mesh_data
        }

    def save(self, file_path):
        """Export skin weights to disk"""

        if not file_path:
            return

        t = time.time()
        self.get_data()
        utils.write_pickle(file_path, self.data)

        print time.time() - t

    @classmethod
    def load(self, file_path=None, closest_point=False, smooth=False, remap=False, data={}):
        """import weights from disk"""

        def set_weights(deformer, data):
            """Actually set all the data """

            weights = data.get('weights')
            if weights:
                for i in range(len(weights)):
                    index_weight = weights[i]
                    if index_weight:
                        attr = '.weightList[{0}].weights[0:{1}]'.format(i, len(index_weight)-1)
                        mc.setAttr(deformer+attr, *index_weight)

        def set_data(deformer, data):
            """Actually set all the data """

            attr_vals = data.get('attrValues')
            for attr, val in attr_vals.items():
                mc.setAttr(deformer+'.'+attr, val)

        # Start timer for load process
        t = time.time()

        if not data and not file_path:
            mc.warning('Must either specify a file path OR provide data.')
            return

        elif file_path and not data:
            data = utils.read_pickle(file_path)

        # get data
        name = data.get('name')
        shapes = data.get('shapes')
        set_members = data.get('setMembers')
        weights = data.get('weights')

        # check if this import has all the nodes it needs in scene
        test_shapes = len(shapes) == len(mc.ls(shapes))
        test_set_members = len(set_members) == len(mc.ls(set_members))
        test_parent = True

        # set remap flag if needed
        if remap or not test_shapes or not test_set_members:
            return data

        # delete existing deformer
        if mc.objExists(name):
            mc.delete(name)

        # IF weights have been painted and closest point then
        # recreate the original mesh anc copy weights

        tmp_shapes = {}
        tmp_deformer = None
        tmp_handle = None
        tmp_set_members = list(set_members)
        mesh_data = data.get('meshData')

        if len(weights) and closest_point:

            # recreate the original mesh for all shapes
            for shape, mesh_info in mesh_data.items():
                matrix = mesh_info.get('matrix')
                points = mesh_info.get('points')
                triangles = mesh_info.get('triangles')

                cpoint_mesh = utils.create_mesh_from_data(matrix, points, triangles)
                tmp_shapes[shape] = cpoint_mesh[0]

            # generate a new set members list for creating the tmp deformer
            for i, member in enumerate(tmp_set_members):
                for shape in shapes:
                    transform = utils.get_transform(shape)

                    if tmp_shapes[shape]:
                        if shape in member:
                            tmp_set_members[i] = member.replace(shape, tmp_shapes[shape])

                        elif transform in member:
                            tmp_set_members[i] = member.replace(transform, tmp_shapes[shape])

            # Creat REAL deformer on recreated mesh
            result = mc.deltaMush(shapes)
            deformer = mc.rename(result[0], name)

            # Create the temp deformer and apply weights
            tmp_deformer = mc.deltaMush(tmp_set_members)[0]
            set_weights(tmp_deformer, data)

            # copy defomer weights from tem pto real
            for shape, tmp_shape in tmp_shapes.items():
                mc.copyDeformerWeights(sourceDeformer=tmp_deformer,
                                       destinationDeformer=deformer,
                                       sourceShape=tmp_shape,
                                       destinationShape=shape,
                                       smooth=smooth,
                                       surfaceAssociation='closestPoint',
                                       noMirror=1)

            # Delete all the temp junk
            mc.delete(tmp_deformer)
            mc.delete(tmp_shapes.values())

            # set data on the real deformer
            set_data(deformer, data)

        else:

            if closest_point:
                set_members = shapes

            result = mc.deltaMush(set_members)
            deformer = mc.rename(result[0], name)

            # set data and weights on the real deformer
            set_weights(deformer, data)
            set_data(deformer, data)

        print time.time() - t

class RemapDeltaMush(remapDialog.RemapDialog):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, nodes=[], ignore_missing=False, label=''):
        remapDialog.RemapDialog.__init__(self, nodes, False, 'Non-Linear Remap UI')

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

        # remap shapes and set members
        shapes_list = list(self.data.get('shapes') or [])
        set_members = list(self.data.get('setMembers') or [])
        mesh_data = dict(self.data.get('meshData') or {})

        for i, orig_shape in enumerate(shapes_list):
            if orig_shape in self.mapping.keys():

                # get new shape and get original transform name to test
                new_shape = self.mapping.get(orig_shape)
                test_orig_xform = orig_shape.replace('Shape', '')

                # first update set members then
                for ii, member in enumerate(set_members):
                    if orig_shape in member:
                        set_members[ii] = member.replace(orig_shape, new_shape)

                    elif test_orig_xform in member:
                        set_members[ii] = member.replace(test_orig_xform, new_shape)

                # update mesh data and remove the original key
                for key, value in mesh_data.items():
                    if key in [orig_shape, test_orig_xform]:
                        mesh_data[new_shape] = value
                        del mesh_data[key]

                # finally update the shapes entry
                shapes_list[i] = new_shape

        self.data['shapes'] = shapes_list
        self.data['setMembers'] = set_members
        self.data['meshData'] = mesh_data

        result = DeltaMush.load(closest_point=self.closest_point, smooth=self.smooth, data=self.data)

def save(file_path, deformer):
    """Wrapper for class export call, Can export multiple and
        prompts for file path"""

    if not file_path.endswith(file_extention):
        file_path = os.path.splitext(file_path)[0]+file_extention

    # export single deformer
    obj = DeltaMush(selection=deformer)
    obj.save(file_path)

def load(file_path, closest_point=False, smooth=False, remap=False, **kwargs):
    """Wrapper for importing weights"""

    if remap:
        data = DeltaMush.load(file_path, closest_point=closest_point, remap=True)

        if type(data) == dict:

            # get nodes to remap
            nodes = data.get('shapes')

            remap_dialog = RemapDeltaMush(nodes=nodes)
            remap_dialog.closest_point = closest_point
            remap_dialog.smooth = smooth
            remap_dialog.data = data
            remap_dialog.show()
            return

    # If not remap then load as usual
    else:
        result = DeltaMush.load(file_path, closest_point=closest_point)

        # warn and skip if a remap is needed.
        if type(result) == dict:
            mc.warning('{0} needs remapping! File path: {1}'.format(result['name'], file_path))

