# -*- coding: utf-8 -*-
"""Functions for creating animatio ncontrool spaces."""

import maya.OpenMaya as om
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
import re

deformer_type = 'spaces'
file_extention = '.spaces'

def generate_arg_string(enum_tuple_list):
    """Formats an arg string which can be passed into the taf function.

        var enum_tuple_list =  A list of tuples - Label and the object that drives it

        Example:
            enum_tuple_list = [('L_Wrist','SoftIk_L_Wrist_World_Ctrl'),('L_Shoulder','SoftIk_L_Shoulder_Ctrl')]
            arg_string = generate_arg_string(enum_tuple_list)
    """
    format_string_list = []
    for tup in enum_tuple_list:

            format_string_list.append(tup[0]+":"+tup[1]+" ")
            individualFormatString = tup[0]
            format_string_list.append(individualFormatString)
            format_string_list.append(":")

    arg_string = "".join(format_string_list)
    arg_string = arg_string[0:-1]
    return arg_string

# This garbage is no longer needed

def build_all(nodes=[]):
    """Build all spaces from space tags."""

    if nodes:
        nodes = [n for n in mc.ls(nodes) if mc.objExists(n+'.tagSpaces')]
    else:
        nodes = mc.ls('*.tagSpaces')
        nodes = [n.replace('.tagSpaces','') for n in nodes if mc.getAttr(n)]

    for node in nodes:
        space_obj = Space(node)
        space_obj.build_space()

def tag(nodes, arg='', split=True, default=0, add_parent_space=True, add_default_spaces=True, zero_node=None, const_node=None):
    """Tag a ctrl for sppaces creation.

        INPUT:
            :nodes: string for a single control or input a list of controls.

        KWARGS:
            :arg: String to declare space labels and drivers
            :default: Default value type(int)
            :split: Split the space to have translation and rotation space attributes
            :zero_node: Parent node use for the parent space, default("ctrl_ZERO")
            :add_parent_space: Get the ZERO node and use that as a parent space (default space)
            :add_default_spaces: Append default spaces. Values are cog, world ctrl and True world

        ARG FORMAT:
            :Format for arg: "label:driver_node label2:driver_node2" """

    nodes = mc.ls(nodes)
    orig_const_node = const_node
    orig_zero_node = zero_node

    for node in nodes:

        # get zero if not specified
        if orig_zero_node:
            zero_node = orig_zero_node
        else:
            zero_node = node+'_ZERO'

        # get const node - this is what the parent constraint will be thrown onto
        if orig_const_node:
            const_node = orig_const_node
        else:
            const_node = node+'_CONST'

        if add_parent_space and not mc.objExists(zero_node):
            mc.warning('Cannot find a zero for '+node)
            continue

        if not mc.objExists(const_node):
            mc.warning('Cannot find a const for '+const_node)
            continue

        # build arg
        arg = arg.strip()
        if ' ' in arg:
            arg = re.sub(' +',' ', arg)

        arg_kwargs = {
            'arg': arg,
            'split': split,
            'default': default,
            'const_node': const_node,
            'zero_node': zero_node,
            'add_default_spaces': add_default_spaces,
            'add_parent_space': add_parent_space
        }

        # create + set attr
        if not mc.objExists(node+'.tagSpaces'):
            mc.addAttr(node, ln='tagSpaces', dt='string', hidden=False)

        mc.setAttr(node+'.tagSpaces', str(arg_kwargs), type='string')

        # This convert all this legacy sloppy crap to the new hotness
        space_obj = Space(node)
        space_obj.set_data()

    return arg

def get_default_arg():
    """Get a default cog, world, trueWorld spaces arg to add ot each space tag"""

    arg = 'cog:C_cog_space_GRP world:parts_GRP trueWorld:noXform_GRP '
    return arg


class Space(object):

    data = {}

    def __init__(self, node='', const_node='', **kwargs):

        # Get node
        if not node:
            node = mc.ls(sl=1)

        node = mc.ls(node)
        if not node:
            raise ValueError('No node specified!')

        self.node = node[0]

        # Get default constraint node
        if not const_node:
            const_node = self.node+'_CONST'

        const_node = mc.ls(const_node)
        if not const_node:
            raise ValueError('No const node specified!')

        # initiate defaults
        self.const_node = const_node[0]
        self.default_value = 0
        self.split = True
        self.spaces = []

        # This is to read data from the actual node if it already has spaces assigned.
        self.get_data()

        # This is IF you specify space options at instatiation time.
        if 'const_node' in kwargs.keys():
            self.const_node = kwargs.get('const_node')
            self.data['const_node'] = self.const_node

        if 'default_value' in kwargs.keys():
            self.default_value = kwargs.get('default_value')
            self.data['default_value'] = self.default_value

        if 'split' in kwargs.keys():
            self.split = kwargs.get('split')
            self.data['split'] = self.split

        if 'spaces' in kwargs.keys():
            self.spaces = kwargs.get('spaces')
            self.data['spaces'] = self.spaces

        if not mc.objExists(self.node+'.tagSpaces'):
            self.set_data()

    def get_data(self):

        spaces = []
        data = {}

        if mc.objExists(self.node+'.tagSpaces'):
            try:
                data = eval(mc.getAttr(self.node+'.tagSpaces'))
            except:
                data = {}

        if 'spaces' in data.keys():
            spaces = data.get('spaces') or []

        else:
            # This is crap to handle legacy spaces
            if data.get('add_parent_space'):

                parent_node = self.node+'_ZERO'
                if not mc.objExists(parent_node):
                    parent_node = utils.get_parent(self.const_node)

                spaces.append(['parent', parent_node])

            if data.get('arg'):
                args = data.get('arg')
                args = [s.strip().split(':') for s in args.split(' ') if ':' in s]
                if args:
                    spaces.extend(args)

            if data.get('add_default_spaces'):
                defaults = get_default_arg()
                defaults = [d.strip().split(':') for d in defaults.split(' ') if ':' in d]

                if defaults:
                    spaces.extend(defaults)

        self.const_node = data.get('const_node') or self.node+'_CONST'
        self.default_value = data.get('default', data.get('default_value')) or 0
        self.split = data.get('split') or True
        self.spaces = spaces

        self.data = {
            'const_node': self.const_node,
            'default_value': self.default_value,
            'split': bool(self.split),
            'spaces': self.spaces,
        }

        return self.data

    def add_parent_space(self):

        parent_node = self.node+'_ZERO'
        if not mc.objExists(parent_node):
            parent_node = utils.get_parent(self.const_node)

        self.spaces.append(['parent', parent_node])
        self.set_data()

    def add_default_spaces(self):
        arg = self.generate_default_spaces()
        for a in arg:
            self.spaces.append([a[0], a[1]])
        self.set_data()

    def set_data(self, data={}):

        if data:
            self.data = data

        else:
            self.data = {
                'const_node': self.const_node,
                'default_value': self.default_value,
                'split': self.split,
                'spaces': self.spaces,
            }

        if not mc.objExists(self.node+'.tagSpaces'):
            mc.addAttr(self.node, ln='tagSpaces', dt='string')

        mc.setAttr(self.node+'.tagSpaces', l=0)
        mc.setAttr(self.node+'.tagSpaces', str(self.data), type='string')
        #mc.setAttr(self.node+'.tagSpaces', l=1)

    def set_const_node(self, const_node=''):

        if not const_node:
            const_node = self.node+'_CONST'

        const_node = mc.ls(const_node)
        if not const_node:
            raise ValueError('No const node specified!')

        self.const_node = const_node[0]
        self.set_data()

        return self.const_node

    def set_split(self, value):

        self.split = bool(value)
        self.set_data()

        return self.split

    def set_default_value(self, value):
        """Set default value to be set when space is created.

            Args:
                :value: (int, str) Specify either the index of the enum OR specify label.

            Returns:
                :space: (list) List of the new default space ['label', 'driver']"""

        if type(value) == int:
            self.default_value = value

        else:

            all_labels = [s[0] for s in self.spaces]
            if value not in all_labels:
                raise ValueError('{0} is not a valid label; in {1}'.format(value, all_labels))

            self.default_value = all_labels.index(value)

        self.set_data()
        return self.spaces[self.default_value]

    # Methods for modifing spaces
    def append_space(self, label, driver):

        self.spaces.append([label, driver])
        self.set_data()

        return [label, driver]

    def remove_space(self, index):
        """Remove a space for the given index."""

        space_to_remove = self.spaces[index]
        self.spaces.remove(space_to_remove)
        self.set_data()

        return space_to_remove

    def insert_space(self, index, label, driver):

        self.spaces.insert(index, [label, driver])
        self.set_data()

        return [label, driver]

    def replace_space(self, index, label, driver):

        self.spaces[index] = [label, driver]
        self.set_data()

        return [label, driver]

    def set_spaces(self, spaces_list):
        self.spaces = spaces_list
        self.set_data()

        return True

    def generate_parent_space(self):
        """Quick helper method to gewnerate a parent space options for the given space.

            Note:
                Parent node will prefereabbly be the ZERO node for this control.
                    If that is not available, then the actual parent node of the const node will be used."""

        parent_node = self.node+'_ZERO'
        parent_node = mc.ls(parent_node)

        if not parent_node:
            parent_node = utils.get_parent(self.const_node)

        parent_node = mc.ls(parent_node)

        if parent_node:
            return ['parent', parent_node[0]]

        else:
            return []

    def generate_default_spaces(self):
        """Generate standard cog and world space options"""

        defaults =[['cog', 'C_cog_space_GRP'],
                   ['world', 'parts_GRP'],
                   ['trueWorld', 'noXform_GRP']]

        return defaults

    def mirror_spaces(self, target_node=None):

        data_str = mc.getAttr(self.node+'.tagSpaces')

        if self.node.startswith('L_'):
            search = "'L_"
            replace = "'R_"

        elif self.node.startswith('R_'):
            search = "'R_"
            replace = "'L_"

        else:
            mc.warning('Cannot mirror space args!')
            return

        if not target_node:
            target_node = self.node.replace(search[1:], replace[1:], 1)

        if not mc.objExists(target_node):
            raise ValueError('Mirror node: {0} does not exist!'.format(target_node))

        data_str = data_str.replace(search, replace)

        if not mc.objExists(target_node+'.tagSpaces'):
            mc.addAttr(target_node, ln='tagSpaces')

        mc.setAttr(target_node+'.tagSpaces', l=0)
        mc.setAttr(target_node+'.tagSpaces', data_str, type='string')
        mc.setAttr(target_node+'.tagSpaces', l=1)

        print 'Mirrored space: from: {0} to: {1}'.format(self.node, target_node)

    def copy_spaces(self, target_node):

        if not mc.objExists(target_node):
            raise ValueError('Target node: {0} does not exist!'.format(target_node))

        data_str = mc.getAttr(self.node+'.tagSpaces')

        if not mc.objExists(target_node+'.tagSpaces'):
            mc.addAttr(target_node, ln='tagSpaces')

        mc.setAttr(target_node+'.tagSpaces', l=0)
        mc.setAttr(target_node+'.tagSpaces', data_str, type='string')
        mc.setAttr(target_node+'.tagSpaces', l=1)

        print 'Copied space: from: {0} to: {1}'.format(self.node, target_node)

    def build_space(self):

        if not mc.objExists('C_cog_space_GRP') and mc.objExists('C_root_JNT'):
            mc.createNode('transform', p='C_root_JNT', n='C_cog_space_GRP')

        # get data
        node = self.node
        const_node = self.const_node
        default_value = self.data.get('default_value')
        split = self.data.get('split')
        spaces = self.spaces

        # Quick check to make sure everything exists!
        for test in [node, const_node]+[s[1] for s in spaces]:
            if test and not mc.objExists(test):
                raise RuntimeError('Cannot create space on {0}! {1} does not exist!'.format(node, test))

        ##########################################################################################################
        # TESTING NEW SPACES
        utils.set_attrs(const_node, l=0, k=1)
        utils.set_attrs(const_node, 'shearX shearY shearZ', l=0, k=1)

        delete_space_mtx(node)
        space_mtx(spaces, const_node, ctrl=node, split=split, dv=default_value)

        return

        ##########################################################################################################
        prc = ''
        enum = ':'.join([s[0] for s in spaces])

        # unlock and rempove const constraints
        utils.set_attrs(const_node, l=0, k=1)
        cons = utils.get_constraints(const_node)
        if cons:
            mc.delete(cons)

        # Remove attrs
        if mc.objExists(node+'.transSpace'):
            mc.deleteAttr(node+'.transSpace')
        if mc.objExists(node+'.orientSpace'):
            mc.deleteAttr(node+'.orientSpace')
        if mc.objExists(node+'.space'):
            mc.deleteAttr(node+'.space')

        # set up for split spaces
        if split:
            splitGrp = const_node+'_oSpace_GRP'
            if mc.objExists(splitGrp):
                utils.set_attrs(splitGrp, l=0, k=1)
                cons = utils.get_constraints(splitGrp)
                if cons:
                    mc.delete(cons)

            else:
                splitGrp = mc.group(utils.get_children(const_node), n=splitGrp)
                mc.xform(splitGrp, piv=[0,0,0])

        # create spadce node  and prc
        for i, space in enumerate(spaces):

            driver = space[1]

            if not mc.objExists(driver):
                raise RuntimeError('Cannot create space on {0}. Driver node: {1} does not exist! '.format(node, driver))

            driver_space_const = driver+'_spaces'
            if not mc.objExists(driver_space_const) or not utils.get_parent(driver_space_const) == driver:
                driver_space_const = mc.createNode('transform', n=driver_space_const, p=driver)
                mc.addAttr(driver_space_const, ln='rigBuildNode', at='message')

            mc.hide(driver_space_const)
            spc = mc.createNode('transform', n=const_node+'_'+driver+'_space#', p=const_node)
            spc_grp = mc.createNode('transform', n=spc+'_GRP', p=const_node)

            mc.setAttr(spc+'.ro', mc.getAttr(const_node+'.ro'))

            mc.addAttr(spc, ln='rigBuildNode', at='message')
            mc.hide(spc_grp, spc)

            mc.parent(spc, spc_grp)
            mc.parent(spc_grp, driver_space_const)

            utils.set_attrs(const_node, 't r', l=0, k=1)
            prc = mc.parentConstraint(spc, const_node, mo=1,n=const_node+'_prc')[0]
            mc.setAttr(prc+'.interpType', 2)

            if split:
                oc = mc.orientConstraint(spc, splitGrp, mo=1,n=splitGrp+'_oc')[0]
                mc.setAttr(oc+'.interpType', 2)

        # create orient constrasint on const nodes "follow Trans" option
        if split:
            oc = mc.orientConstraint(const_node, splitGrp, mo=1, n=splitGrp+'_oc')[0]

        # create space attrs
        if split:
            if not mc.objExists(node+'.transSpace'):
                mc.addAttr(node, ln='transSpace', at='enum', en=enum, dv=default_value, k=1)
            if not mc.objExists(node+'.orientSpace'):
                mc.addAttr(node, ln='orientSpace', at='enum', en=enum+':sameAsTranslate', dv=len(spaces), k=1)

        else:
            if not mc.objExists(node+'.space'):
                mc.addAttr(node, ln='space', at='enum', en=enum, dv=default_value, k=1 )

        # SDK parentConstraint for different spaces
        for i in range(len(spaces)):

            if split:
                mc.setDrivenKeyframe(prc+'.w{0}'.format(i), cd=node+'.transSpace', v=0, dv=i-1)
                mc.setDrivenKeyframe(prc+'.w{0}'.format(i), cd=node+'.transSpace', v=1, dv=i)
                mc.setDrivenKeyframe(prc+'.w{0}'.format(i), cd=node+'.transSpace', v=0, dv=i+1)

                mc.setDrivenKeyframe(oc+'.w{0}'.format(i), cd=node+'.orientSpace', v=0, dv=i-1)
                mc.setDrivenKeyframe(oc+'.w{0}'.format(i), cd=node+'.orientSpace', v=1, dv=i)
                mc.setDrivenKeyframe(oc+'.w{0}'.format(i), cd=node+'.orientSpace', v=0, dv=i+1)

            else:
                mc.setDrivenKeyframe(prc+'.w{0}'.format(i), cd=node+'.space', v=0, dv=i-1)
                mc.setDrivenKeyframe(prc+'.w{0}'.format(i), cd=node+'.space', v=1, dv=i)
                mc.setDrivenKeyframe(prc+'.w{0}'.format(i), cd=node+'.space', v=0, dv=i+1)

        if split:
            i = len(spaces)
            mc.setDrivenKeyframe(oc+'.w{0}'.format(i), cd=node+'.orientSpace', v=0, dv=i-1)
            mc.setDrivenKeyframe(oc+'.w{0}'.format(i), cd=node+'.orientSpace', v=1, dv=i)
            mc.setDrivenKeyframe(oc+'.w{0}'.format(i), cd=node+'.orientSpace', v=0, dv=i+1)
            utils.set_attrs(splitGrp, l=1, k=0)

        utils.set_attrs(const_node, l=1, k=0)


def save_all(file_path, nodes=[]):

    data = {}

    if not nodes:
        nodes = [n.split('.')[0] for n in mc.ls('*.tagSpaces')]

    nodes = mc.ls(nodes)

    for node in nodes:
        node_data = mc.getAttr(node+'.tagSpaces')

        data[node] = node_data

    utils.write_json(file_path, data)

def load(file_path, **kwargs):

    data = utils.read_json(file_path)
    for node, node_data in data.items():
        if mc.objExists(node):
            if not mc.objExists(node+'.tagSpaces'):
                mc.addAttr(node, ln='tagSpaces')

            mc.setAttr(node+'.tagSpaces', l=0)

            if node_data:
                try:
                    mc.setAttr(node+'.tagSpaces', node_data, type='string')
                except:
                    if mc.objExists(node+'.tagSpaces'):
                        mc.deleteAttr(node+'.tagSpaces')
                    mc.addAttr(node, ln='tagSpaces', dt='string')
                    mc.setAttr(node+'.tagSpaces', node_data, type='string')

            if not node_data:
                mc.deleteAttr(node+'.tagSpaces')

def get_offset(parent, child):

    def getDagPath(node=None):
        sel = om.MSelectionList()
        sel.add(node)
        d = om.MDagPath()
        sel.getDagPath(0, d)
        return d

    parentWorldMatrix = getDagPath(parent).inclusiveMatrix()
    childWorldMatrix = getDagPath(child).inclusiveMatrix()

    return childWorldMatrix * parentWorldMatrix.inverse()


def space_mtx(drivers, driven, ctrl=None, split=False, dv=0, s=False):

    labels = [d[0] for d in drivers]
    drivers = [d[1] for d in drivers]

    choice = mc.createNode('choice', n=driven+'_space')
    choice_off = mc.createNode('choice', n=driven+'_off_choice')
    mc.connectAttr(choice+'.selector', choice_off+'.selector')

    mmtx = mc.createNode('multMatrix', n=driven+'_space_mmtx')
    dmtx = mc.createNode('decomposeMatrix', n=driven+'_space_dmtx')

    if not ctrl:
        ctrl = driven

    # Orientation nodes
    if split:
        o_choice = mc.createNode('choice', n=driven+'_space_orient')
        o_choice_off = mc.createNode('choice', n=driven+'_space_orient_off_choice')
        mc.connectAttr(o_choice+'.selector', o_choice_off+'.selector')

        o_mmtx = mc.createNode('multMatrix', n=driven+'_space_orient_mmtx')
        o_dmtx = mc.createNode('decomposeMatrix', n=driven+'_space_orient_dmtx')

    # set up matrix switches
    for i, driver in enumerate(drivers):
        mc.connectAttr(driver+'.worldMatrix', '{0}.input[{1}]'.format(choice, i))

        # cset offsets
        offset = get_offset(driver, driven)

        mc.addAttr(choice, ln=driver, at='matrix', h=1)
        mc.setAttr(choice+'.'+driver, [offset(ii, j) for ii in range(4) for j in range(4)], type='matrix')
        mc.connectAttr(choice+'.'+driver, '{0}.input[{1}]'.format(choice_off, i))

        # orientation
        if split:
            mc.connectAttr(driver+'.worldMatrix', '{0}.input[{1}]'.format(o_choice, i))

            # cset offsets
            mc.addAttr(o_choice, ln=driver, at='matrix', h=1)
            mc.setAttr(o_choice+'.'+driver, [offset(ii, j) for ii in range(4) for j in range(4)], type='matrix')
            mc.connectAttr(o_choice+'.'+driver, '{0}.input[{1}]'.format(o_choice_off, i))

    # create costraint
    mc.connectAttr(choice_off+'.output', mmtx+'.matrixIn[0]')
    mc.connectAttr(choice+'.output', mmtx+'.matrixIn[1]')
    mc.connectAttr(driven+'.parentInverseMatrix', mmtx+'.matrixIn[2]')
    mc.connectAttr(mmtx+'.matrixSum', dmtx+'.inputMatrix')
    mc.setAttr(mmtx+'.ihi', 0)

    mc.setAttr(choice_off+'.ihi', 0)
    mc.setAttr(dmtx+'.ihi', 0)
    mc.setAttr(mmtx+'.ihi', 0)

    if split:
        i = len(drivers)
        mc.connectAttr(choice+'.output', '{0}.input[{1}]'.format(o_choice, i))
        mc.connectAttr(choice_off+'.output', '{0}.input[{1}]'.format(o_choice_off, i))

        mc.connectAttr(o_choice_off+'.output', o_mmtx+'.matrixIn[0]')
        mc.connectAttr(o_choice+'.output', o_mmtx+'.matrixIn[1]')
        mc.connectAttr(driven+'.parentInverseMatrix', o_mmtx+'.matrixIn[2]')
        mc.connectAttr(o_mmtx+'.matrixSum', o_dmtx+'.inputMatrix')
        mc.setAttr(o_mmtx+'.ihi', 0)

        mc.setAttr(o_choice+'.ihi', 0)
        mc.setAttr(o_choice_off+'.ihi', 0)
        mc.setAttr(o_dmtx+'.ihi', 0)
        mc.setAttr(o_mmtx+'.ihi', 0)

        mc.connectAttr(dmtx+'.outputTranslate', driven+'.t')
        mc.connectAttr(o_dmtx+'.outputRotate', driven+'.r')
        if s:
            mc.connectAttr(dmtx+'.outputScale', driven+'.s')
            mc.connectAttr(dmtx+'.outputShear', driven+'.shear')

        mc.addAttr(ctrl, ln='transSpace', at='enum', en=':'.join(labels), dv=dv, k=1)
        mc.addAttr(ctrl, ln='orientSpace', at='enum', en=':'.join(labels+['sameAsTranslate']), dv=i, k=1)

        mc.connectAttr(ctrl+'.transSpace', choice+'.selector')
        mc.connectAttr(ctrl+'.orientSpace', o_choice+'.selector')

    else:
        mc.connectAttr(dmtx+'.outputTranslate', driven+'.t')
        mc.connectAttr(dmtx+'.outputRotate', driven+'.r')
        if s:
            mc.connectAttr(dmtx+'.outputScale', driven+'.s')
            mc.connectAttr(dmtx+'.outputShear', driven+'.shear')

        mc.addAttr(ctrl, ln='space', at='enum', en=':'.join(labels), dv=dv, k=1)
        mc.connectAttr(ctrl+'.space', choice+'.selector')

def delete_space_mtx(ctrl):

    if not mc.objExists(ctrl+'.space') and not mc.objExists(ctrl+'.transSpace') and not mc.objExists(ctrl+'.orientSpace'):
        return

    nodes = []
    if mc.objExists(ctrl+'.space'):
        nodes = mc.listConnections(ctrl+'.space', type='choice', s=0, d=1) or []
        mc.deleteAttr(ctrl+'.space')

    elif mc.objExists(ctrl+'.transSpace'):
        nodes = mc.listConnections(ctrl+'.transSpace', type='choice', s=0, d=1) or []
        nodes.extend(mc.listConnections(ctrl+'.orientSpace', type='choice', s=0, d=1) or [])
        mc.deleteAttr(ctrl+'.transSpace')
        mc.deleteAttr(ctrl+'.orientSpace')

    if nodes:
        nodes.extend(mc.listConnections(nodes, type='choice',s=1, d=1) or [])
        nodes.extend(mc.listConnections(nodes, type='multMatrix',s=1, d=1) or [])
        nodes.extend(mc.listConnections(nodes, type='decomposeMatrix',s=1, d=1) or [])
        nodes = mc.ls(nodes)

        mc.delete(nodes)
