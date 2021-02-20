from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma
import maya.cmds as mc
import maya.mel as mm

import cPickle as pickle
import time
import os

from rigBot import utils
from rigBot.gui import remapDialog

file_extention = '.udattrs'
deformer_type = 'udAttributes'

def get_data(nodes):

    # get nodes
    if not nodes:
        nodes = mc.ls(sl=1)
    nodes =[n.split('.')[0] for n in mc.ls(nodes)]

    if not nodes:
        mc.warning('No nodes specified.')
        return

    data = {}

    for node in nodes:
        # list user defined attrs
        attrs = mc.listAttr(node, ud=1) or []
        ordered_attr_list = []
        node_data = {}

        for attr in attrs:

            value = None
            attr_type = mc.addAttr(node+'.'+attr, at=1, q=1)

            # check if value is gettable
            try:
                value = mc.getAttr(node+'.'+attr, sl=1)
                test_string_type = mc.addAttr(node+'.'+attr, dt=1, q=1)

                # Do this to record empty string attributes.
                if value is None and test_string_type[0] == 'string':
                    value = ''
                    mc.setAttr(node+'.'+attr, value, type='string')

            except:
                pass

            # This is so maya doesnt crash if you try ot read a compuynd attribute
            if attr_type in ['compound', 'message']:
                value = attr_type

            # now gather data
            if value is not None:
                attr_data = {}

                # check the data type and attr type
                data_type = mc.addAttr(node+'.'+attr, dt=1, q=1)
                attr_type = mc.addAttr(node+'.'+attr, at=1, q=1)

                if type(data_type) is list:
                    data_type = data_type[0]

                # If string handle it differntly. otherwise
                if data_type == 'string':
                    attr_data = {
                        'type': 'string',
                        'value': value
                    }

                # if its an enum
                elif attr_type == 'enum':
                    enum = mc.addAttr(node+'.'+attr, en=1, q=1)
                    default_value = mc.addAttr(node+'.'+attr, q=1, dv=1)

                    attr_data = {
                        'type': attr_type,
                        'enum': enum,
                        'default_value': default_value,
                        'value': value
                    }

                elif attr_type == 'compound':
                    number_children = mc.addAttr(node+'.'+attr, q=1, number_children=1)
                    children = mc.attributeQuery(attr, node=node, lc=True)
                    attr_data = {
                        'type': attr_type,
                        'number_children': number_children,
                        'children': children
                    }

                # if its numeric
                else:
                    min_value = None
                    max_value = None

                    if mc.attributeQuery(attr, node=node, minExists=True):
                        min_value = mc.addAttr(node+'.'+attr, q=1, min=1)

                    if mc.attributeQuery(attr, node=node, minExists=True):
                        max_value = mc.addAttr(node+'.'+attr, q=1, max=1)

                    default_value = None

                    try:
                        default_value = mc.attributeQuery(attr, node=node, ld=True)
                        if default_value and type(default_value) is list:
                            default_value = default_value[0]

                    except:
                        pass

                    attr_data = {
                        'type': attr_type,
                        'min': min_value,
                        'max': max_value,
                        'default_value': default_value,
                        'value': value
                    }

                if attr_data:
                    attr_data['parent'] = mc.attributeQuery(attr, node=node, lp=True)
                    attr_data['keyable'] = mc.getAttr(node+'.'+attr, k=1)
                    attr_data['non_keyable'] = mc.getAttr(node+'.'+attr, cb=1)
                    node_data[attr] = attr_data
                    ordered_attr_list.append(attr)

        if node_data and ordered_attr_list:
            data[node] = {'data': node_data, 'attr_order': ordered_attr_list}

    return data

def set_data(data, create_attrs=True, set_values=True, set_values_on_all=False, verbose=True):
    """Read custom attributes file and recreate them"""

    def set_value(node, attr, attr_data, verbose=False):
        """Sets the value on specifed node from data """

        keyable = attr_data.get('keyable')
        non_keyable = attr_data.get('non_keyable')
        value = attr_data.get('value')
        attr_type = attr_data.get('type')

        excluded_types = ['float2', 'float3', 'double2', 'double3',
                        'compound', 'message', 'short3', 'long2', 'long3']
        try:
            if not mc.objExists(node+'.'+attr):
                if verbose:
                    mc.warning('# Attr {0}.{1} doe not exist! Skipping..'.format(node, attr))
                return

            elif attr_type in excluded_types:
                return

            elif attr_type == 'string':
                if not value:
                    value = ''
                mc.setAttr(node+'.'+attr, value, type='string')

            else:
                mc.setAttr(node+'.'+attr, value)

            if verbose:
                print 'Set attribute value: '+node+'.'+attr

        except:
            if verbose:
                mc.warning('Could not set '+attr_type+' attr value :'+node+'.'+attr)

    def add_attr(node, attr, attr_data, verbose=False):
        """Actually add the attribbutes based on attr_dataDict"""

        parent = attr_data.get('parent')
        keyable = attr_data.get('keyable')
        non_keyable = attr_data.get('non_keyable')
        value = attr_data.get('value')
        attr_type = attr_data.get('type')

        # get parent and make sure it is a string
        if parent and type(parent) is list:
            parent = parent[0]

        # skip if the attr already exists
        if mc.objExists(node+'.'+attr):
            if verbose:
                mc.warning('# Attr {0}.{1} already exists! Skipping..'.format(node, attr))
            return

        # add message attrs
        elif attr_type == 'message':
            mc.addAttr(node, ln=attr, at='message')

            if verbose:
                print 'Added attribute: '+node+'.'+attr
                return True

        # add compound attrs
        elif attr_type == 'compound':
            number_children = attr_data.get('number_children')

            try:
                if parent:
                    mc.addAttr(node, ln=attr, at='compound', p=parent, k=keyable, number_children=number_children)
                else:
                    mc.addAttr(node, ln=attr, at='compound', k=keyable, number_children=number_children)

                if verbose:
                    print 'Added attribute: '+node+'.'+attr
                    return True

            except:
                mc.warning('# Could not add attr: {0}.{1}'.format(node, attr))

        # add string attrs
        elif attr_type == 'string' :
            try:
                if parent:
                    mc.addAttr(node, ln=attr, dt='string',p=parent)
                else:
                    mc.addAttr(node, ln=attr, dt='string')

                if verbose:
                    print 'Added attribute: '+node+'.'+attr
                    return True

            except:
                mc.warning('# Could not add attr: {0}.{1}'.format(node, attr))

        # add enum attrs
        elif attr_type == 'enum':
            try:
                enum = attr_data.get('enum')
                default_value = attr_data.get('default_value')

                if parent:
                    mc.addAttr(node, ln=attr, at=attr_type, k=keyable, en=enum, p=parent)
                else:
                    mc.addAttr(node, ln=attr, at=attr_type, k=keyable, en=enum)

                if verbose:
                    print 'Added attribute: '+node+'.'+attr
                    return True

            except:
                mc.warning('# Could not add attr: {0}.{1}'.format(node, attr))


        elif attr_type == 'bool':
            try:
                default_value = attr_data.get('default_value') or 0
                if parent:
                    mc.addAttr(node, ln=attr, at=attr_type, k=keyable, dv=default_value, p=parent)
                else:
                    mc.addAttr(node, ln=attr, at=attr_type, k=keyable, dv=default_value)

                if verbose:
                    print 'Added attribute: '+node+'.'+attr
                    return True

            except:
                mc.warning('# Could not add attr: {0}.{1}'.format(node, attr))

        elif attr_type in ['float2', 'float3', 'double2', 'double3', 'short3', 'long2', 'long3']:
            try:
                if parent:
                    mc.addAttr(node, ln=attr, at=attr_type, k=keyable, p=parent)
                else:
                    mc.addAttr(node, ln=attr, at=attr_type, k=keyable)

                if verbose:
                    print 'Added attribute: '+node+'.'+attr
                    return True

            except:
                mc.warning('# Could not add attr: {0}.{1}'.format(node, attr))

        else:
            try:
                min_value = attr_data.get('min')
                max_value = attr_data.get('max')
                default_value = attr_data.get('default_value') or 0

                if parent:
                    if min_value and max_value:
                        mc.addAttr(node, ln=attr, min=min_value, max=max_value, at=attr_type, k=keyable, dv=default_value, p=parent)
                    elif min_value:
                        mc.addAttr(node, ln=attr, min=min_value, at=attr_type, k=keyable, dv=default_value, p=parent)
                    elif max_value:
                        mc.addAttr(node, ln=attr, max=max_value, at=attr_type, k=keyable, dv=default_value, p=parent)
                    else:
                        mc.addAttr(node, ln=attr, at=attr_type, k=keyable, dv=default_value, p=parent)
                else:
                    if min_value is not None and max_value is not None:
                        mc.addAttr(node, ln=attr, min=min_value, max=max_value, at=attr_type, k=keyable, dv=default_value)
                    elif min_value:
                        mc.addAttr(node, ln=attr, min=min_value, at=attr_type, k=keyable, dv=default_value)
                    elif max_value:
                        mc.addAttr(node, ln=attr, max=max_value, at=attr_type, k=keyable, dv=default_value)
                    else:
                        mc.addAttr(node, ln=attr, at=attr_type, k=keyable, dv=default_value)

                if verbose:
                    print 'Added attribute: '+node+'.'+attr
                    return True

            except:
                mc.warning('# Could not add attr: {0}.{1}'.format(node, attr))

    nodes = mc.ls(data.keys())

    # first create all compound and child attrs
    if not data:
        return

    for node in nodes:
        if verbose:
            print '\n'

        node_data = data.get(node)
        if not node_data:
            continue

        node_data = node_data.get('data')
        ordered_attr_list = data.get(node).get('attr_order')

        # this is for only setting vcalues on newly created nodes
        # we doint want ot mess with whats already there.
        set_values_for = []

        # first create attrs
        if create_attrs:
            for attr in ordered_attr_list:
                attr_data = node_data.get(attr)
                result = add_attr(node, attr, attr_data, verbose=verbose)
                if result:
                    set_values_for.append(attr)

        if set_values_on_all:
            set_values_for = ordered_attr_list

        # then set them
        for attr in set_values_for:
            attr_data = node_data.get(attr)
            set_value(node, attr, attr_data, verbose=verbose)

def save(file_path, nodes):
    """Wrapper for class export call, Can export multiple and
        prompts for file path"""

    t = time.time()
    data = get_data(nodes)

    if not data:
        mc.warning('Nothing to save for selected nodes!')
        return

    if not file_path.endswith(file_extention):
        file_path = os.path.splitext(file_path)[0]+file_extention

    utils.write_json(file_path, data)
    print time.time() - t

def load(file_path, remap=False, create_attrs=True, set_values=True, set_values_on_all=False, **kwargs):
    """Wrapper for importing weights"""

    def test_nodes(nodes):
        for n in nodes:
            if not mc.objExists(n):
                return False
        return True


    # Load remaping dialog
    if remap:
        data = utils.read_json(file_path)

        if type(data) == dict:

            # get nodes to remap
            nodes = data.keys()
            remap_dialog = RemapAttributes(nodes=nodes)
            remap_dialog.data = data
            remap_dialog.create_attrs = create_attrs
            remap_dialog.set_values = set_values
            remap_dialog.set_values_on_all = set_values_on_all
            remap_dialog.show()

            return

    # If not remap then load as usual
    else:
        data = utils.read_json(file_path)

        if not test_nodes(data.keys()):
            # warn and skip if a remap is needed.
            mc.warning('Nodes need remapping! File path: {0}'.format(file_path))
        else:
            set_data(data,
                     create_attrs=create_attrs,
                     set_values=set_values,
                     set_values_on_all=set_values_on_all)

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

        set_data(self.data,
                 create_attrs=self.create_attrs,
                 set_values=self.set_values,
                 set_values_on_all=self.set_values_on_all)

