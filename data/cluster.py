import maya.cmds as mc
import maya.OpenMaya as om
import maya.OpenMayaAnim as oma

from functools import partial
import cPickle as pickle
import time
import os

from rigBot import utils
from rigBot.gui import remapDialog

file_extention = '.cls'
deformer_type = 'cluster'

class Cluster(object):
    """Class for exporting, import and manipulating skin nonLinears"""

    def __init__(self, selection=None):

        deformer, shapes = utils.get_deformers_and_shapes(selection, deformer_type)

        if not deformer:
            raise ValueError('Deformer not found!')

        if not shapes:
            raise ValueError('Shapes not found for: {0}!'.format(deformer))

        self.deformer = deformer
        self.shapes = shapes

        self.__initialize_deformer_mobject()

    def __initialize_deformer_mobject(self):

        self.shapes = mc.cluster(self.deformer, q=1, g=1)

        self.def_set = mc.listConnections(self.deformer, type='objectSet')[0]
        self.def_cmpts = mc.ls(mc.sets(self.def_set, q=1), fl=1)

        # Get skin cluster api info
        self.cls_obj = om.MObject()
        self.cls_dag_path = om.MDagPath()
        self.cls_members = om.MSelectionList()

        sel_list = om.MSelectionList()
        sel_list.add(self.deformer)
        sel_list.getDependNode(0, self.cls_obj)

        # get defomer Geom filter and ObjSet
        self.fn_cls = oma.MFnWeightGeometryFilter(self.cls_obj)
        self.fn_set = om.MFnSet(self.fn_cls.deformerSet())

        # Get cmpts effected by deformer PER mesh
        self.fn_set.getMembers(self.cls_members, False)

    def get_data(self):
        """Get data and build dict"""

        fix_clashing_handle_names()

        # get weighted node and prebind node
        self.relative = mc.getAttr(self.deformer+'.relative')
        self.weighted_node = mc.cluster(self.deformer, q=1, wn=1)
        self.prebind_node = mc.listConnections(self.deformer+'.bindPreMatrix', s=1, d=0)

        if self.prebind_node:
            self.prebind_node = self.prebind_node[0]

        # get weights for each shape in cluster
        weights_dict = {}
        for i in xrange(self.cls_members.length()):

            cmpts = om.MObject()
            mesh_dag_path = om.MDagPath()
            weight_array = om.MFloatArray()

            self.cls_members.getDagPath(i, mesh_dag_path, cmpts)
            self.fn_cls.getWeights(mesh_dag_path, cmpts, weight_array)

            name = mesh_dag_path.partialPathName()
            weight_array = [weight_array[i] for i in xrange(weight_array.length())]

            weights_dict[name] = weight_array

        # get mesh_data
        mesh_data = {}

        for shape in self.shapes:
            orig_shape = utils.get_orig_shape(shape)
            shape_data = utils.get_mesh_data(orig_shape)
            mesh_data[shape] = shape_data

        self.data = {
            'name': self.deformer,
            'shapes': self.shapes,
            'weights': weights_dict,
            'relative': self.relative,
            'weightedNode': self.weighted_node,
            'prebindNode': self.prebind_node,
            'meshData': mesh_data
        }

    def save(self, file_path):
        """Export skin weights to disk"""

        if not file_path:
            return

        t = time.time()
        self.get_data()
        utils.write_pickle(file_path, self.data)

        print time.time() - t

    def set_soft_weights(self):
        """SDet soft selected weights for cluster"""

        self.get_data()
        self.get_soft_weights()

        newshapes = self.soft_weights['weights'].keys()
        for i, shape in enumerate(newshapes):
            shapec = []
            if mc.nodeType(shape) == 'mesh':
                shapec = mc.ls(shape+'.vtx[*]')

            if mc.nodeType(shape) in ['nurbsCurve', 'bezierCurve', 'nurbsSurface']:
                shapec = mc.ls(shape+'.cv[*]')

            if mc.nodeType(shape) == 'lattice':
                shapec = mc.ls(shape+'.pt[*]')

            if shapec:
                newshapes[i] = shapec[0]

        # remove old members from set
        members = mc.sets(self.def_set, q=1)
    
        rm_members = []
        for m in members:
            for s in newshapes:
                if m.split('.')[0] in s:
                    rm_members.append(m)
                
        mc.sets(rm_members, rm=self.def_set)
        mc.sets(newshapes, add=self.def_set)

        self.__initialize_deformer_mobject()

        self.set_weights(weight=0.0)
        self.set_weights(data=self.soft_weights)

    def set_weights(self, weight=1.0, data={}, shape_node=None):
        """Set cluster weights

        Args:
            cls -- cluster node (string) OR (list)
            weights -- (dict(MFloatArray)) OR (int) OR (float)
            soft -- Calculate soft selected weights
            geometry -- Specify piece of geo to set weights on, otherwise all geo will be set (string)
        """

        # Get cmpts effected by deformer PER mesh
        dag_path = om.MDagPath()
        cmpts = om.MObject()

        for i in xrange(self.cls_members.length()):

            self.cls_members.getDagPath(i, dag_path, cmpts)
            name = utils.get_shapes(dag_path.partialPathName())[0] or ''

            if shape_node and name != shape_node:
                continue

            print name

            # create api indexed cmt based on geo type
            node_type = mc.nodeType(name)
            if node_type in ['mesh', 'nurbsCurve']:
                fnComp = om.MFnSingleIndexedComponent(cmpts)
            elif node_type == 'nurbsSurface':
                fnComp = om.MFnDoubleIndexedComponent(cmpts)
            elif node_type == 'lattice':
                fnComp = om.MFnTripleIndexedComponent(cmpts)

            # Create mfloat array with single weight value
            cmpt_count = fnComp.elementCount()
            weight_mfloat_array = om.MFloatArray()
            weight_mfloat_array = om.MFloatArray(cmpt_count, weight)

            if data:
                # Get weight values from data passed in
                weight_array = data['weights'].get(name) or {}
                weight_mfloat_array = om.MFloatArray(len(weight_array))
                for i, w in enumerate(weight_array):
                    weight_mfloat_array.set(w, i)

            # set weight
            self.fn_cls.setWeight(dag_path, cmpts, weight_mfloat_array)

        return True

    def add(self, nodes, weight=1.0):
        """Add nodes to cluster"""

        for n in mc.ls(nodes):
            n = utils.get_shapes(n)
            if n:
                mc.sets(n[0], add=self.def_set)
                mc.percent(self.deformer, n[0], v=weight)

    @classmethod
    def create(self, nodes=None, weighted_node='', prebind_node=None, name='cluster#'):
        """Create cluster"""

        try:
            if nodes:
                if mc.objExists(weighted_node):
                    deformer = mc.cluster(nodes, bs=1, wn=[weighted_node]*2, n=name)
                else:
                    deformer = mc.cluster(nodes, bs=1, n=name)
            else:
                if mc.objExists(weighted_node):
                    deformer = mc.cluster(bs=1, wn=[weighted_node]*2, n=name)
                else:
                    deformer = mc.cluster(bs=1, n=name)
        except:
            mc.warning('Could not create cluster!')
            return

        if deformer and prebind_node:
            if mc.objExists(prebind_node):
                mc.connectAttr(prebind_node+'.parentInverseMatrix',
                               deformer[0]+'.bindPreMatrix', f=1)

        fix_clashing_handle_names()
        return deformer

    @classmethod
    def load(self, file_path=None, closest_point=False, smooth=False, remap=False, data={}):

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
        weights = data.get('weights')
        relative = data.get('relative')
        weighted_node = data.get('weightedNode')
        prebind_node = data.get('prebindNode')
        mesh_data = data.get('meshData')

        # check if this import has all the nodes it needs in scene
        test_shapes = mc.ls(shapes)
        test_weighted_node = mc.ls(weighted_node)
        test_prebind_node = True

        if prebind_node:
            test_prebind_node = mc.ls(weighted_node)

        if remap or not test_weighted_node or not test_prebind_node or not len(test_shapes) == len(shapes):
            return data

        # Create new  cluster
        deformer = self.create(shapes, weighted_node, prebind_node, name)[0]
        mc.setAttr(deformer+'.relative', relative)
        mc.setAttr(deformer+'.envelope', 0)

        new_cls_obj = Cluster(deformer)
        new_cls_obj.set_weights(data=data)

        # Recreate the mesh and coy weights
        if closest_point:

            # recreate the original mesh for all shapes
            for shape, mesh_info in mesh_data.items():

                matrix = mesh_info.get('matrix')
                points = mesh_info.get('points')
                triangles = mesh_info.get('triangles')

                cpoint_mesh = utils.create_mesh_from_data(matrix, points, triangles)

                if cpoint_mesh:
                    tmp_deformer = self.create(cpoint_mesh[0])[0]
                    tmp_cls_obj = Cluster(tmp_deformer)

                    tmp_weight_dict = {cpoint_mesh[1]: data['weights'][shape]}
                    tmp_data = {'weights':tmp_weight_dict}
                    tmp_cls_obj.set_weights(data=tmp_data)

                    dup_shape = mc.duplicate(shape)[0]
                    dup_shape_node = utils.get_shapes(dup_shape)[0]
                    dup_deformer = self.create(dup_shape)[0]
                    dup_obj = Cluster(dup_deformer)

                    mc.copyDeformerWeights(sourceDeformer=tmp_deformer,
                                           destinationDeformer=dup_deformer,
                                           sourceShape=cpoint_mesh[1],
                                           destinationShape=dup_shape,
                                           surfaceAssociation='closestPoint',
                                           smooth=smooth,
                                           noMirror=1)

                    dup_obj.get_data()
                    value = dup_obj.data['weights'].get(dup_shape_node)
                    dup_obj.data['weights'][shape] = value

                    new_cls_obj.set_weights(shape_node=shape, data=dup_obj.data)
                    mc.delete(tmp_deformer, dup_shape, cpoint_mesh[0])

        # OR just apply the weights
        else:
            new_cls_obj = Cluster(deformer)
            new_cls_obj.set_weights(data=data)

        mc.setAttr(deformer+'.envelope', 1)
        fix_clashing_handle_names()

    @classmethod
    def get_soft_weights(self):
        """Get the weight value for the current soft selection.

        Return:
            weights -- (dict(MFloatArray))
        """

        self.soft_weights = {'weights': {}}

        # OM selections
        try:
            richSel = om.MRichSelection()
            om.MGlobal.getRichSelection(richSel)
            richSelList = om.MSelectionList()
            richSel.getSelection(richSelList)
            selCount = richSelList.length()

        except:
            return self.soft_weights

        # get each soft sel from each object
        for x in xrange(selCount):

            shapeDagPath = om.MDagPath()
            shapeComp = om.MObject()
            richSelList.getDagPath(x, shapeDagPath, shapeComp)
            name = mc.ls(shapeDagPath.fullPathName())[0]
            ntype = mc.nodeType(name)

            weightArray = None

            if ntype in ['nurbsCurve', 'mesh']:
                if ntype == 'mesh':
                    ccount = mc.polyEvaluate(name, v=1)
                else:
                    ccount = len(mc.ls(name+'.cv[*]', fl=1))

                weightArray = om.MFloatArray(ccount, 0.0)
                compFn = om.MFnSingleIndexedComponent(shapeComp)

                # get weight value from each soft selected cmpt
                for i in xrange(compFn.elementCount()):
                    vertId = compFn.element(i)
                    weight = compFn.weight(i).influence()
                    weightArray[int(vertId)] = weight

            elif ntype == 'nurbsSurface':
                csel = [c.split('.')[-1] for c in mc.ls(name+'.cv[*]', fl=1)]
                ccount = len(csel)
                weightArray = om.MFloatArray(ccount, 0.0)

                uList = om.MIntArray()
                vList = om.MIntArray()
                compFn = om.MFnDoubleIndexedComponent(shapeComp)
                compFn.getElements(uList, vList)

                # get weight value from each soft selected cmpt
                for i in xrange(compFn.elementCount()):
                    weight = compFn.weight(i).influence()
                    Id = csel.index('cv[{0}][{1}]'.format(uList[i], vList[i]))
                    weightArray[Id] = weight

            elif ntype == 'lattice':
                csel = [c.split('.')[-1] for c in mc.ls(name+'.pt[*]', fl=1)]
                ccount = len(csel)
                weightArray = om.MFloatArray(ccount, 0.0)

                uList = om.MIntArray()
                vList = om.MIntArray()
                wList = om.MIntArray()

                compFn = om.MFnTripleIndexedComponent(shapeComp)
                compFn.getElements(uList, vList, wList)

                for i in xrange(compFn.elementCount()):
                    weight = compFn.weight(i).influence()
                    Id = csel.index('pt[{0}][{1}][{2}]'.format(uList[i],
                                                          vList[i],
                                                          wList[i]))
                    weightArray[Id] = weight

            elif ntype == 'transform':
                shape = utils.get_shapes(name)

                if not shape:
                    continue

                shape = shape[0]

                if mc.nodeType(shape) == 'mesh':
                    ccount = mc.polyEvaluate(name, v=1)
                else:
                    ccount = len(mc.ls(name+'.cv[*]', name+'.pt[*]', fl=1))

                if ccount:
                    weightArray = om.MFloatArray(ccount, 1.0)

            name = utils.get_shapes(name)
            if name:
                if weightArray:
                    self.soft_weights['weights'][name[0]] = weightArray

        return self.soft_weights

class RemapCluster(remapDialog.RemapDialog):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, nodes=[], label=''):
        remapDialog.RemapDialog.__init__(self, nodes, False, 'Cluster Remap UI')
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

    def finish(self):
        """Close UI and continue with data import"""

        self.deleteLater()

        """update data dict with new mapping and load the data"""

        weighted_node = self.data.get('weightedNode')
        prebind_node = self.data.get('prebindNode')
        shapes = self.data.get('shapes')

        # remap weighted node
        if weighted_node in self.mapping.keys():
            self.data['weightedNode'] = self.mapping.get(weighted_node)

        # remap prebind node
        if prebind_node and prebind_node in self.mapping.keys():
            self.data['prebindNode'] = self.mapping.get(prebind_node)

        # remap shapes
        # remap shapes
        new_shapes = []
        for shape in self.data['shapes']:
            new_shape = self.mapping[shape]

            if not new_shape:
                del self.data['weights'][shape]
                del self.data['meshData'][shape]
                continue

            new_shapes.append(new_shape)

            if new_shape != shape:

                # remap weights
                value = self.data['weights'][shape]
                self.data['weights'][new_shape] = value
                del self.data['weights'][shape]

                #remap mesh data
                value = self.data['meshData'][shape]
                self.data['meshData'][new_shape] = value
                del self.data['meshData'][shape]

        self.data['shapes'] = new_shapes

        result = Cluster.load(closest_point=self.closest_point, smooth=self.smooth, data=self.data)

def save(file_path, deformer):
    """Wrapper for class export call, Can export multiple and
        prompts for file path"""

    # export single deformer
    obj = Cluster(selection=deformer)

    if not file_path.endswith(file_extention):
        file_path = os.path.splitext(file_path)[0]+file_extention
    obj.save(file_path)

def load(file_path, closest_point=False, smooth=False, remap=False, **kwargs):
    """Wrapper for importing weights"""

    # Load remaping dialog
    if remap == True:
        data = Cluster.load(file_path, smooth=smooth, closest_point=closest_point, remap=True)

        if type(data) == dict:

            # get nodes to remap
            nodes = [data.get('weightedNode')]
            prebind_node = data.get('prebindNode')
            if prebind_node:
                nodes.append(prebind_node)
            nodes.extend(data.get('shapes'))

            remap_dialog = RemapCluster(nodes=nodes)
            remap_dialog.closest_point = closest_point
            remap_dialog.smooth = smooth
            remap_dialog.data = data
            remap_dialog.show()
            return

    # If not remap then load as usual
    else:
        result = Cluster.load(file_path, smooth=smooth, closest_point=closest_point)
        if type(result) == dict:
            mc.warning('{0} needs remapping! File path: {1}'.format(result['name'], file_path))

def set_soft_weights(selection=None):
    """Wrapper for setting soft selection weights"""

    cls_obj = Cluster(selection=selection)
    if cls_obj.deformer:
        cls_obj.set_soft_weights()


def create(nodes=None, weighted_node='', prebind_node=None, name='cluster#'):
    """Create new cluster"""

    result = Cluster.create(nodes, weighted_node, prebind_node, name)
    return result


def add(nodes=[], selection=None, weight=1.0):
    """Add shape nodes to cluster set"""

    if not selection:
        selection = mc.ls(sl=1)[-1]

    if not nodes:
        nodes = mc.ls(sl=1)[:-1]
    nodes = mc.ls(nodes)

    cls_obj = Cluster(selection=selection)
    if cls_obj.deformer:
        cls_obj.add(nodes, weight)


def connect_prebind(node, deformer):
    """Connecect node parentInverseMatrix"""

    if node and mc.objExists(node+'.parentInverseMatrix') and mc.objExists(deformer+'.bindPreMatrix'):
        mc.connectAttr(node+'.parentInverseMatrix', deformer+'.bindPreMatrix', f=1)


def mirror(source_deformer, target_deformer=None, new_weighted_node='', new_prebind_node=None):
    """Mirror cluster weights.cluster
        NOTE: Will not find mirrored geometry. only geo that is part of the
        source cluster will be added / mirrored to the new cluster
    """

    source_obj = Cluster(source_deformer)
    geo = source_obj.shapes

    if not target_deformer:
        target_deformer = create(geo, new_weighted_node, new_prebind_node)[0]

    mc.percent(target_deformer, geo, v=0.0)
    for shape in geo:
        mc.copyDeformerWeights(sourceDeformer=source_deformer,
                               destinationDeformer=target_deformer,
                               sourceShape=shape,
                               destinationShape=shape,
                               surfaceAssociation='closestPoint',
                               mm='YZ')

def fix_clashing_handle_names():
    dup_handle_names = [h for h in mc.ls(sn=1, type='clusterHandle') if '|' in h]
    for handle in dup_handle_names:
        parent = utils.get_parent(handle)
        suffix = utils.get_suffix('clusterHandle')
        new_name = utils.get_unique_name(parent+'_'+suffix)
        if mc.objExists(handle):
            mc.rename(handle, new_name)

