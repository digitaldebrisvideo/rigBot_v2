from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma
import maya.cmds as mc
import maya.mel as mm

import cPickle as pickle
import time
import os

from rigBot import utils
from rigBot.gui import remapDialog

file_extention = '.cnnct'
deformer_type = 'connections'

def get_data(nodes=None):
    """Get data dict of source connections and desitnation connections"""

    # get nodes
    if not nodes:
        nodes = mc.ls(sl=1)
    nodes = mc.ls(nodes)

    if not nodes:
        mc.warning('No nodes specified.')
        return

    connections = {}
    excluded_types = ['animCurve', 'blendWeighted', 'Constraint']

    for node in nodes:

        attrs = mc.listAttr(node) or []

        attrs = [a for a in mc.listAttr(node, k=1) if '.' not in a]
        if mc.nodeType(node) == 'blendShape':
            attrs.extend(['weight[{0}]'.format(i) for i in range(mc.blendShape(node, q=1, wc=1))])

        for attr in attrs:

            if mc.objExists(node+'.'+attr):

                source_connecitons = mc.listConnections(node+'.'+attr, s=1, d=0, p=1, scn=1)

                if source_connecitons:
                    for src_conneciton in source_connecitons:

                        passed_check = True
                        for exluded in excluded_types:
                            if exluded in mc.nodeType(src_conneciton):
                                passed_check = False

                        if passed_check:
                            connections[node+'.'+attr] = src_conneciton
    return connections

def set_data(data):
    """Recreate connections from data dict"""

    for dst_connection, src_conneciton in data.items():
        try:
            mc.connectAttr(src_conneciton, dst_connection, f=1)
        except:
            mc.warning('Could not connect {0} to {1}. This may already be connected.'.format(src_conneciton, dst_connection))

def save(file_path, nodes=[], data={}):
    """Wrapper for class export call, Can export multiple and
        prompts for file path"""

    t = time.time()

    if nodes and not data:
        data = get_data(nodes)

    if not data:
        mc.warning('Nothing to save for selected nodes!')
        return

    if not file_path.endswith(file_extention):
        file_path = os.path.splitext(file_path)[0]+file_extention

    utils.write_json(file_path, data)
    print time.time() - t

def load(file_path, remap=False, **kwargs):
    """Wrapper for importing weights"""

    def test_nodes(nodes):
        for n in nodes:
            if not mc.objExists(n):
                return False
        return True

    # Get files for loading
    if remap:
        data = utils.read_json(file_path)

        if type(data) == dict:

            # get nodes to remap
            nodes = data.keys()+data.values()
            remap_dialog = RemapConnections(nodes=nodes)
            remap_dialog.data = data
            remap_dialog.show()

            return

    # If not remap then load as usual
    else:
        data = utils.read_json(file_path)

        if not test_nodes(data.keys()+data.values()):
            # warn and skip if a remap is needed.
            mc.warning('Nodes need remapping! File path: {0}'.format(file_path))
        else:
            set_data(data)

class RemapConnections(remapDialog.RemapDialog):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, nodes=[], ignore_missing=True, label=''):
        remapDialog.RemapDialog.__init__(self, nodes, True, 'Set Driven Key Remap UI')

        self.ignore_missing_nodes = True
        self.data = {}

    def map_selection(self):
        """Map selectio nto node"""

        items = self.ui.node_tree.selectedItems() or []

        sel = mc.ls(sl=1)
        if items and sel:
            for item in items:

                node = item.text(0)
                new_node = sel[0]
                attrs = utils.get_selected_attrs(verbose=False)

                if attrs:
                    new_node += '.'+attrs[0]
                else:
                    new_node += '.'+node.split('.')[-1]

                if not mc.objExists(new_node):
                    mc.warning('Nothing selected!')
                    return

                item.setText(2, new_node)
                self.mapping[node] = new_node

        elif not sel:
            mc.warning('Nothing selected!')

    def finish_command(self):
        """update data dict with new mapping and load the data"""

        # remap source
        orig_nodes = self.data.keys()
        for orig_node in orig_nodes:
            new_node = self.mapping[orig_node] or orig_node

            if new_node != orig_node:
                self.data[new_node] = self.data[orig_node]
                del self.data[orig_node]

        # remap destination
        for key, orig_node in self.data.items():
            new_node = self.mapping[orig_node] or orig_nodes
            self.data[key] = new_node

        set_data(self.data)
