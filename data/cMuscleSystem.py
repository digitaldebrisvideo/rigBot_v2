"""Module for importing, exporting and manipulating blendshapes nodes and targets."""

import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
import maya.OpenMayaAnim as oma

from functools import partial
import cPickle as pickle
import time
import os

from rigBot import utils
from rigBot.gui import remapDialog

file_extention = '.cms'
deformer_type = 'cMuscleSystem'

class CMuscleSystem(object):
    """Class for exporting, import and manipulating skin nonLinears"""

    def __init__(self, selection=None):

        deformer, shapes = utils.get_deformers_and_shapes(selection, deformer_type)

        if not deformer:
            raise ValueError('Deformer not found!')

        if not shapes:
            raise ValueError('Shapes not found for: {0}!'.format(deformer))

        self.deformer = deformer
        self.shapes = shapes

    def save(self, file_path):
        """Export blendShape to disk"""

        t = time.time()
        if not file_path:
            return

        if not self.shapes:
            raise RuntimeError(self.deformer+' does not have any geometry!')

        current_selection = mc.ls(sl=1)
        export_node = mc.duplicate(self.deformer, n=self.deformer+'_data')[0]
        mc.refresh()

        mc.addAttr(export_node, ln='exportData', at='message')
        mc.addAttr(export_node, ln='deformerName', dt='string')
        mc.addAttr(export_node, ln='requiredShapes', dt='string')
        mc.setAttr(export_node+'.deformerName', self.deformer, type='string')
        mc.setAttr(export_node+'.requiredShapes', str(self.shapes), type='string')

        if os.path.isfile(file_path):
            os.remove(file_path)

        mc.select(export_node)
        os.rename(mc.file(file_path, f=1, op='', typ='mayaBinary', es=1), file_path)

        delete_export_data_nodes()
        mc.select(current_selection)

        print 'Exported cMuscleSystem: %s' % file_path
        print time.time() - t


    @classmethod
    def load(self, file_path=None, remap=False, data={}):

        # Start timer for load process
        t = time.time()

        delete_export_data_nodes()

        if not data and not file_path:
            mc.warning('Must either specify a file path OR provide data.')
            return

        # import the file
        try:
            snapshot = mc.ls()
            imported_nodes = mc.file(file_path, i=1, rnn=1, pmt=0, iv=1)

        except:
            imported_nodes = [n for n in mc.ls() if n not in snapshot]
            pass

        if not imported_nodes:
            raise RuntimeError('This file contains no nodes! '+file_path)

        data_node = None
        for n in imported_nodes:
            if mc.objExists(n+'.exportData'):
                data_node = n

        if not data_node:
            raise RuntimeError('This file contains no data node! '+file_path)

        # get data
        name = mc.getAttr(data_node+'.deformerName')
        shapes = eval(mc.getAttr(data_node+'.requiredShapes'))

        if data:
            shapes = data.get('shapes')

        exisiting_shapes = mc.ls(shapes)

        # check shapes for remap
        if remap or not len(shapes) == len(exisiting_shapes):
            delete_export_data_nodes()
            return {'name':name, 'shapes':shapes}

        # delete the original deformer if it exists
        if mc.objExists(name):
            mc.delete(name)

        #Recreate the blendshape node
        deformer = None

        try:
            mc.select(shapes[0])
            deformer = mm.eval('cMuscle_makeMuscleSystem(0);')

        except:
            try:
                mc.select(shapes[0])
                deformer = mm.eval('cMuscle_makeMuscleSystem(0);')
            except:
                delete_export_data_nodes()
                raise RuntimeError('Could not create cMuscleSystemNode node!')

        # get connections
        cnns = mc.listConnections((deformer), s=1, c=1, d=0, p=1, scn=1) or []
        connections = []
        for i in range(0, len(cnns), 2):
            connections.append((cnns[i+1], cnns[i].replace(deformer, data_node)))

        cnns = mc.listConnections((deformer), s=0, c=1, d=1, p=1, scn=1) or []
        for i in range(0, len(cnns), 2):
            connections.append((cnns[i].replace(deformer, data_node), cnns[i+1]))

        # reconnect connstions
        for cnn in connections:
            try:
                mc.connectAttr(cnn[0], cnn[1], f=1)
            except:
                mc.warning('Could not make connection: {0} -->> {1}'.format(cnn[0], cnn[1]))

        mc.delete(deformer)
        deformer = mc.rename(data_node, name)

        mc.deleteAttr(deformer+'.exportData')
        mc.deleteAttr(deformer+'.requiredShapes')
        mc.deleteAttr(deformer+'.deformerName')
        delete_export_data_nodes()

        print '# Loaded cMuscleSystem: {0}'.format(deformer)
        print time.time() - t

class RemapCMuscleSystem(remapDialog.RemapDialog):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, nodes=[], ignore_missing=False, label=''):
        remapDialog.RemapDialog.__init__(self, nodes, False, 'CMuscleSystem Remap UI')

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
        new_shapes = []
        for shape in self.data['shapes']:
            new_shapes.append(self.mapping[shape])

        self.data['shapes'] = new_shapes
        result = CMuscleSystem.load(self.file_path, data=self.data)

def delete_export_data_nodes():
    """Remove all imported ".exportData" nodes in scene."""

    nodes = mc.ls('*.exportData')
    if nodes:
        mc.delete([n.replace('.exportData', '') for n in nodes])

def save(file_path, deformer):
    """Wrapper for class export call.

        Args:
            :file_path: (str) Path to save file on disk.
            :deformer: (str) Blendshape node name."""

    obj = CMuscleSystem(selection=deformer)

    if not file_path.endswith(file_extention):
        file_path = os.path.splitext(file_path)[0]+file_extention

    obj.save(file_path)

def load(file_path, remap=False, **kwargs):
    """Wrapper for importing weights.

        Args:
            :file_path: (str) Path to file on disk.

        Kwargs:
            :remap: (bool) Laucnh remap dialog to remp node names. Defaults to False."""

    # Load remaping dialog
    if remap:
        data = CMuscleSystem.load(file_path, remap=True)

        if type(data) == dict:

            # get nodes to remap
            nodes = data.get('shapes')
            remap_dialog = RemapCMuscleSystem(nodes=nodes)
            remap_dialog.file_path = file_path
            remap_dialog.data = data
            remap_dialog.show()

            return

    # If not remap then load as usual
    else:
        result = CMuscleSystem.load(file_path)
        if type(result) == dict:
            mc.warning('{0} needs remapping! File path: {1}'.format(result['name'], file_path))
