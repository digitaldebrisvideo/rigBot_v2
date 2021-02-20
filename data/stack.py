import maya.cmds as mc

from rigBot import utils
from rigBot.gui import remapDialog

import cPickle as pickle
import time
import os

deformer_type = 'deformationStack'
file_extention = '.dstak'

class RemapStack(remapDialog.RemapDialog):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, nodes=[], ignore_missing=False, label=''):
        remapDialog.RemapDialog.__init__(self, nodes, False, 'Non-Linear Remap UI')
        self.data = {}

    def finish_command(self):
        """update data dict with new mapping and load the data"""

        # remap parent
        for node in self.mapping.keys():
            self.data[self.mapping[node]] = self.data[node]

        set_data(self.data)

def get_data(shapes):
    """Get deformation stack fro mnodes"""

    data = {}
    for shape in shapes:
        stack = mc.listHistory(shape, il= 1, pdo=1) or []
        data[shape] = stack

    return data

def set_data(data):
    """Set deformation stack"""

    for shape, stack in data.items():

        shape = mc.ls(shape)

        if not shape:
            continue

        for i in range(len(stack)-1):
            try:
                mc.reorderDeformers(stack[i], stack[i+1], shape[0])
                print 'Reordered deformation stack: '+shape[0]

            except:
                pass

    return True

def save(file_path, node):
    """Wrapper for class export call, Can export multiple and
        prompts for file path"""

    t = time.time()

    shapes = utils.get_shapes(node)
    data = get_data(shapes)

    if not data:
        mc.warning('Nothing to save for selected nodes!')
        return

    if not file_path.endswith(file_extention):
        file_path = os.path.splitext(file_path)[0]+file_extention

    utils.write_json(file_path, data)
    print time.time() - t

def load(file_path, remap=False, **kwargs):
    """Wrapper for importing weights"""

    # Load remaping dialog
    if remap:
        data = utils.read_json(file_path)

        if type(data) == dict:

            # get nodes to remap
            nodes = []
            if data.keys():
                nodes= data.keys()

            remap_dialog = RemapStack(nodes=nodes)
            remap_dialog.data = data
            remap_dialog.show()
            return

    # If not remap then load as usual
    else:
        data = utils.read_json(file_path)
        result = set_data(data)

        # warn and skip if a remap is needed.
        if result is None:
            mc.warning('{0} needs remapping! File path: {1}'.format(data['node'], file_path))

