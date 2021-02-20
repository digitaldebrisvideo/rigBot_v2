from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma
import maya.cmds as mc
import maya.mel as mm

import cPickle as pickle
import time
import os

from rigBot import utils
from rigBot.gui import remapDialog

file_extention = '.kattrs'
deformer_type = 'kAttributes'

def get_data(nodes=None):

    # get nodes
    current = mc.ls(sl=1)

    if not nodes:
        nodes = [c.replace('.animControl','') for c in mc.ls('*.animControl', ln=1)]
        if mc.objExists('control_SEL'):
            mc.select('control_SEL')
            nodes.extend(mc.ls(sl=1))

        nodes.extend(mc.ls('*_CTL'))

    nodes = mc.ls(nodes)
    mc.select(current)

    if not nodes:
        mc.warning('No nodes specified.')
        return

    data = {}
    for node in nodes:

        keyable = mc.listAttr(node, k=1) or []
        nonkeyable = mc.listAttr(node, cb=1) or []
        painted_attrs = [a for a in mc.listAttr(node) or [] if 'PerVertex' in a]
        locked = mc.listAttr(node, l=1) or []

        values = {}
        attrs_to_set = list(set(keyable+nonkeyable+locked+painted_attrs))

        for attr in attrs_to_set:
            try:
                if mc.objExists(node+'.'+attr):
                    value = mc.getAttr(node+'.'+attr)
                    if value is not None:
                        values[attr] = value

            except:
                pass

        data[utils.strip_namespace(node)] = {
            'keyable': keyable,
            'nonkeyable': nonkeyable,
            'locked': locked,
            'values': values
        }

    return data

def set_data(data, set_values=True):

    for node, value_data in data.items():
        pass

        ls_node = mc.ls(node)
        if not ls_node:
            mc.warning(node+' doesnt exist! Try remapping... Skipping for now..')
            continue

        node = ls_node[0]

        keyable = value_data['keyable']
        nonkeyable = value_data['nonkeyable']
        locked = value_data['locked']
        values = value_data['values']

        if set_values:
            try:
                utils.set_attrs(node, l=0, k=1)
            except:
                pass

            for attr, v in values.items():
                try:
                    try:
                        mc.setAttr(node+'.'+attr, v)
                    except:
                        mc.setAttr(node+'.'+attr, v, type='doubleArray')

                except:
                    #print 'Could not set value for: '+node+'.'+attr
                    pass

        try:
            utils.set_attrs(node, l=1, k=0)
            utils.set_attrs(node, ' '.join(keyable), l=0, k=1)

            for attr in nonkeyable:
                if mc.objExists(node+'.'+attr):
                    mc.setAttr(node+'.'+attr, cb=1, k=0)

            for attr in locked:
                if mc.objExists(node+'.'+attr):
                    mc.setAttr(node+'.'+attr, l=1)
        except:
            pass

def save(file_path, nodes=None):
    """Wrapper for class export call, Can export multiple and
        prompts for file path"""

    t = time.time()
    data = get_data(nodes)

    if not data:
        mc.warning('Nothing to save for selected nodes!')
        return

    if not file_path.endswith(file_extention):
        file_path = os.path.splitext(file_path)[0]+'.kattrs'

    utils.write_json(file_path, data)
    print time.time() - t

def load(file_path, set_values=True, remap=False, **kwargs):
    """Wrapper for importing weights"""

    if remap:
        data = utils.read_json(file_path)

        if type(data) == dict:

            # get nodes to remap
            nodes = data.keys()
            if not mc.ls(nodes):
                csel = mc.ls(sl=1)
                if csel and ':' in csel[0]:
                    ns = csel[0].split(':')[0]+':'
                    #nodes = [ns+n for n in nodes]

            remap_dialog = RemapAttributes(nodes=nodes)
            remap_dialog.data = data
            remap_dialog.set_values = set_values
            remap_dialog.show()

            return

    else:
        # If not remap then load as usual
        data = utils.read_json(file_path)
        set_data(data, set_values)

class RemapAttributes(remapDialog.RemapDialog):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, nodes=[], ignore_missing=True, label=''):
        remapDialog.RemapDialog.__init__(self, nodes, True, 'Set Driven Key Remap UI')

        self.ignore_missing_nodes = True
        self.data = {}

    def finish_command(self):
        """update data dict with new mapping and load the data"""

        # remap source
        orig_nodes = self.data.keys()
        for orig_node in orig_nodes:
            new_node = self.mapping[orig_node] or orig_node

            if new_node != orig_node:
                self.data[new_node] = self.data[orig_node]
                del self.data[orig_node]

        set_data(self.data, self.set_values)

