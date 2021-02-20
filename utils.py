# -*- coding: utf-8 -*-
"""Various utilities. This module includes most generic utilites used in this system."""

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from maya.api import OpenMaya as OpenMaya
from maya import OpenMaya as om

import cPickle as pickle
import webbrowser
import itertools
import subprocess
import importlib
import random
import functools
import traceback
import string
import math
import stat
import json
import sys
import os
import re
import inspect
import ast
import imp

# Stored letters array to use for lettering node names
name_conventions = {}
letters = [''.join(ltrs)
                for length in range(1, 5)
                        for ltrs in itertools.product(string.ascii_uppercase,
                                repeat=length)]


def reload_name_conventions(verbose=False):
    """Reload the nameConventions.json file from disk. This file is located in rigBot.config.

    Args:
        :verbose: (bool) Verbose will print a verification message when the file is reloaded. Defaults to True."""

    global name_conventions

    system_base_path = os.path.dirname(__file__)
    base_path = os.path.join(system_base_path, 'config')
    file_path = os.path.join(base_path, 'nameConventions.json')

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            name_conventions = json.load(f)
            if verbose:
                print 'Loaded naming conventions: '+file_path

try:
    reload_name_conventions()
except:
    pass

def undoable(function):
    """Decorator code for making Qt methods undoable. The function is wrapped in an undo chunk."""

    @functools.wraps(function)
    def fn(*args, **kwargs):

        try:
            exception = None
            result = None
            mc.undoInfo(openChunk=True)
            result = function(*args, **kwargs)
            mc.undoInfo(closeChunk=True)

        except:
            mc.undoInfo(closeChunk=True)
            exception = get_exception()
            if exception:
                raise RuntimeError(exception)

        return result

    return fn

###############################################################################
# File read / write utilities
def reverse_selection():
    sel = mc.ls(sl=1)
    sel.reverse()
    mc.select(sel)

    return sel

def break_connection(dest_attr):
    """Break incomming connections on the specifed attribute.

    Args:
        :dest_attr: (str) Name of the driven attribute. ie: "node.attribute" """

    source = list(set(mc.listConnections(dest_attr, s=1, d=0, p=1) or []))
    for src in source:
        try:
            mc.disconnectAttr(src, dest_attr)
        except:
            mc.warning('Could not brteak connection between {0} and {1}'.format(src, dest_attr))

def connect_reverse(source_attr, dest_attr):
    """Connect one attribute to another using a reverse node:

    Args:
        :source_attr: (str) Name of the source attribute. ie: "node.attribute"
        :dest_attr: (str) Name of the destination attribute. ie: "node.attribute"

    Math:
        driven.attribute = 1.0 - driver.attribute"""

    reverse = mc.createNode('reverse', n=source_attr.replace('.', '_')+'_rv')
    mc.connectAttr(source_attr, reverse+'.inputX')
    mc.connectAttr(reverse+'.outputX', dest_attr, f=1)
    mc.setAttr(reverse+'.ihi', 0)


def connect_negative(source_attr, dest_attr):
    """Connect one attribute to another using a reverse node:

    Args:
        :source_attr: (str) Name of the source attribute. ie: "node.attribute"
        :dest_attr: (str) Name of the destination attribute. ie: "node.attribute"

    Math:
        driven.attribute = diver.attribute * -1.0"""

    mdl = mc.createNode('multDoubleLinear', n=source_attr.replace('.', '_')+'_mdl')
    mc.connectAttr(source_attr, mdl+'.input1')
    mc.connectAttr(mdl+'.output', dest_attr, f=1)
    mc.setAttr(mdl+'.input2', -1)
    mc.setAttr(mdl+'.ihi', 0)

def connect_abs(source_attr, dest_attr):
    """Connect the absolute value of one attribute to another.

    Args:
        :source_attr: (str) Name of the source attribute. ie: "node.attribute"
        :dest_attr: (str) Name of the destination attribute. ie: "node.attribute"

    Math:
        driven.attribute = abs(driver.attribute)"""

    mdl = mc.createNode('multDoubleLinear', n=source_attr.split('.')[0]+'_abs_mdl')
    cnd = mc.createNode('condition', n=source_attr.split('.')[0]+'_abs_cnd')

    mc.connectAttr(source_attr, cnd+'.firstTerm')
    mc.connectAttr(source_attr, cnd+'.colorIfTrueR')
    mc.connectAttr(mdl+'.output', cnd+'.colorIfFalseR')
    mc.connectAttr(source_attr, mdl+'.input1')
    mc.setAttr(mdl+'.input2', -1)
    mc.setAttr(cnd+'.operation', 2)

    mc.addAttr(cnd, ln='absoluteValue', k=1)
    mc.connectAttr(cnd+'.outColorR', cnd+'.absoluteValue')
    mc.connectAttr(cnd+'.absoluteValue', dest_attr)

    mc.setAttr(mdl+'.ihi', 0)
    mc.setAttr(cnd+'.ihi', 0)

def read_json(file_path, verbose=True):
    """Read json file and return data as dict.

    Args:
        :file_path: (str) Full path to the file on disk.

    Kwargs:
        :verbose: (bool) Verbose will print a verification message when the file is reloaded. Defaults to True.

    Returns:
        :data: (dict) Data read from file."""

    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as f:
                result = json.load(f)
                if verbose:
                    print 'Reading data from: '+norm_path(file_path)
                return result
        except:
            mc.warning('Cannot read: '+norm_path(file_path))
    else:
        mc.warning('File doesn\'t exists: '+norm_path(file_path))

    return {}

def write_json(file_path, data):
    """Write data to json file on disk.

    Args:
        :file_path: (str) Full path to the file on disk.
        :data: (dict) Data to be written to disk."""

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
        print 'Wrote data to: '+norm_path(file_path)

    change_permission(file_path)

def read_pickle(file_path, verbose=True):
    """Read pickled file and return data as dict.

    Args:
        :file_path: (str) Full path to the file on disk.

    Kwargs:
        :verbose: (bool) Verbose will print a verification message when the file is reloaded. Defaults to True.

    Returns:
        :data: (dict) Data read from file."""

    if os.path.isfile(file_path):
        try:
            with open(file_path, 'rb') as f:
                result = pickle.load(f)
                if verbose:
                    print 'Reading data from: '+norm_path(file_path)
                return result
        except:
            mc.warning('Cannot read: '+norm_path(file_path))
    else:
        mc.warning('File doesn\'t exists: '+norm_path(file_path))

    return {}

def write_pickle(file_path, data):
    """Write data to pickled file on disk.

    Args:
        :file_path: (str) Full path to the file on disk.
        :data: (dict) Data to be written to disk."""


    with open(file_path, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        print 'Wrote data to: '+norm_path(file_path)

    change_permission(file_path)

def export_maya_file(file_path, nodes, file_type='mayaAscii'):
    """Export specified nodes to maya scene file.

    Args:
        :file_path: (str) Full path to the file on disk.
        :nodes: (list) Nodes to be exported.

    Kwargs:
        :file_type: (str) File type to be exported. Defaults to "mayaAscii"."""

    try:
        mc.select(nodes)
        result = mc.file(file_path, f=1, op='', typ=file_type, es=1)
        print 'Exported file: '+result
        return result

    except:
        mc.warning('Failed to export: '+norm_path(file_path))

def import_maya_file(file_path):
    if os.path.isfile(file_path):
        try:
            return mc.file(file_path, i=1, rnn=1, pmt=0, iv=1)
        except:
            mc.warning('Cannot import: '+norm_path(file_path))
    else:
        mc.warning('File doesn\'t exists: '+norm_path(file_path))

def edit_file(file_path):
    """Open the specified text file in a text editor.
    Uses the system perffered application.

    Args:
        :file_path: (str) Path to file on disk."""

    file_path = norm_path(file_path)

    if not os.path.isfile(file_path):
        mc.warning('File does not exist: '+file_path)
        return

    try:
        os.startfile(file_path)
        print 'Opening file: '+file_path
    except:
        webbrowser.open(file_path)
        print 'Opening file: '+file_path

def save_changes():
    """Save changes to scene dialog.

    Returns:
        :result: (bool)"""

    return bool(mm.eval('int $reult = `saveChanges("file -f -new")`;'))

def norm_path(path):
    """format path using os.normpath and removes "\\".

    Args:
        :path: (str) Path to file or folder.

    Returns:
        :path: (str) Normalized, formatted path"""

    try:
        return str(os.path.normpath(path).replace('\\','/'))

    except:
        return str(path)

def make_dirs(paths):
    """Make folders on disk

    Args:
        :paths: (str, list) Path or paths to create."""

    if type(paths) is not list:
        paths = [paths]

    for p in paths:
        if not os.path.isdir(p):
            try:
                os.makedirs(p, 0777)
                print 'Created dir: '+p
            except:
                mc.warning('Could not create path: '+p)

def change_permission(path):
    """Change permissions on already created files to be readable and writtable by overyone.
    You'll need permissions first of course.

    Args:
        :path: (str) Path to file on disk."""

    if sys.platform == 'win32':
        return

    FILE_PERMISSIONS = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH
    os.chmod(path, FILE_PERMISSIONS)

###############################################################################
# name and string utils
'''
def get_side(token='C', get_all=False):
    """Get proper side token from config file"""

    if token is None:
        token = 'C'

    sides = [
        name_conventions.get('centerSide') or 'C',
        name_conventions.get('leftSide') or 'L',
        name_conventions.get('rightSide') or 'R']

    if token.upper().startswith('L'):
        side = sides[1]
    elif token.upper().startswith('R'):
        side = sides[2]
    else:
        side = sides[0]

    if get_all:
        side = sides

    return side
'''
def side_decipher(transform):
    """Decipher the side based on the transforms position in world space.

    Args:
        :transform: (str) Node name.

    Returns:
        :result: (str)"""

    posX = mc.xform(transform,  q = True ,rp = True, ws = True)[0]
    if posX > 0:
        side = "L"
    if posX < 0:
        side = "R"
    if posX == 0:
        side = "C"
        mc.warning('Side is centered on x axis, returning "C"')

    return side

def get_suffix(node_type=None):
    """Get name conventions from conventiosn file based on either node_type or
    by querying an existing node.

    Args:
        :node_type: (str) Either a node_type OR an exisitng node name

    Returns:
        :result: (str)

    Note:
        If the node has a shape it will return the suffix for the shape."""

    capitalize_suffix = name_conventions.get('capitalizeSuffix', False)

    result = ''
    if node_type in name_conventions.keys():
        result = name_conventions.get(node_type) or ''

    elif node_type and mc.objExists(node_type):
        node_type = mc.ls(node_type)[0]
        result = name_conventions.get(mc.nodeType(node_type)) or ''

        # check if it has a shape
        shapes = get_shapes(node_type)
        if shapes:
            result = name_conventions.get(mc.nodeType(shapes[0])) or ''

    if capitalize_suffix:
        result = result.upper()

    return result

def find_middle(input_list):
    """Find the middle index of a python list"""

    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

def join_strings(in_list, keep_underscores=True):
    """Convert a list  of strings to a formatted string using underscores.

    Args:
        :in_list: (list) Input string

    Kwargs:
        :keep_underscores: (bool) Keep underscores, otherwise camelCase string.

    Returns:
        :result: (str)"""

    result = '_'.join([i for i in in_list if i])
    result = clean_name(result, keep_underscores=keep_underscores)

    return result

def clean_name(in_string, keep_underscores=False):
    """Convert string with whitespaces or underscores to camelCased string.

    Args:
        :in_string: (str) Input string

    Kwargs:
        :keep_underscores: (bool) Keep underscores, otherwise camelCase string.

    Returns:
        :result: (str)"""

    if not in_string:
        return in_string

    # remove illegal chars
    regex = re.compile('[^a-zA-Z0-9#_]')
    in_string = regex.sub('_', in_string)
    in_string = in_string.replace(' ', '_')
    in_string = in_string.strip()
    in_string = re.sub('_+','_', in_string)

    if in_string[0] == '_':
        in_string = in_string[1:]

    if in_string[-1] == '_':
        in_string = in_string[:-1]

    # remove underscores
    if not keep_underscores:
        in_string = [t for t in re.sub('_+','_', in_string).split('_') if t]
        if len(in_string) > 1:
            in_string = [in_string[0]]+[t[0].capitalize()+t[1:]
                                                    for t in in_string[1:]]
        in_string = ''.join(in_string)

    return in_string

def split_camel_case(in_string):
    """Split string based on camelCase letters into a list of strings.of

    Args:
        :in_string: (str) String to split.

    Returns:
        :result: (list) list of tokens
    """

    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', in_string)
    return [m.group(0) for m in matches]

def split_list(in_list, number):
    """Evenly split a list by specified number.

    Args:
        :in_list: (list) Input list
        :number: (int) Number to split the list by.

    Returns:
        :result: (list) list of lists."""

    k, m = divmod(len(in_list), number)
    out = list(in_list[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in xrange(number))
    out = [o for o in out if o]
    return out

def get_namespace(node):
        ns = ':'.join(node.split(':')[:-1])
        if ns:
            ns += ':'
        return ns

def get_long_names(names):
    """Return the full name of a given node or nodes.

    Args:
        :names: (str, list) List of existing nodes.existing

    Returns:
        :result: (str, list) Long name of node or nodes."""

    return_as_list = True
    if not type(names) == list:
        names = [names]
        return_as_list = False

    result = []
    for name in names:

        try:
            obj = om.MObject()
            dag_path = om.MDagPath()

            msel_list = om.MSelectionList()
            msel_list.add(name.split('.')[0])
            msel_list.getDependNode(0, obj)

            if obj.hasFn(om.MFn.kDagNode):
                om.MDagPath.getAPathTo(obj, dag_path)
                fullPathName = str(dag_path.fullPathName())

            else:
                fullPathName = name.split('.')[0]
        except:
            fullPathName = name.split('.')[0]

        if '.' in name:
            fullPathName += '.'+name.split('.')[-1]

        result.append(fullPathName)

    if return_as_list:
        return convert_to_unicode(result)

    elif result:
        return convert_to_unicode(result[0])

def strip_namespace(name):
    """Strip name space dagpath name.

    Args:
        :name: (str) Node name.

    Returns:
        :result: (str) name without namespace"""

    tokens = name.split('|')
    result = ''

    for i, token in enumerate(tokens):
        if i > 0:
            result += '|'

        cmpt = None
        token = token.split('.')
        if len(token) > 1:
            cmpt = '.'.join(token[1:])

        token = token[0]
        result += token.split(':')[-1]
        if cmpt:
            result += '.'+cmpt

    return result

def check_clashing_node_names(verbose=True):
    """Print clashing non-unique node names.:

    Returns:
        :result: (list) Clashing node names."""

    nodes = [n for n in mc.ls(sn=1) if '|' in n ]

    if nodes:
        if verbose:
            print '\n# Found non-unique node names'

            print_list(nodes, 1, 'nodes')
            mc.select(nodes)
            mc.warning('Found non-unique node names. See script editor.')
        return nodes

    else:
        if verbose:
            print '\n# All node names are unique :)'

def convert_to_unicode(data):
    """Converts unicode lists to string.

    Args:
        :data: (str, list) Input of list or string.

    Returns:
        (str, list)"""

    if type(data) == list:
        for i, n in enumerate(data):
            if type(n) in [str, basestring, unicode]:
                data[i] = str(n)
        return data

    else:
        return str(data)

def get_unique_name(name):
    """Get new unique name. Use a "#" to indicate where to place the new
        letter token.

    Args:
        :name: (str) Node name to check.

    Returns:
        :new_name: (str) A unique node name"""

    i = 0
    new_name = clean_name(name.replace('#',''), keep_underscores=True)
    while mc.objExists(new_name):

        ltr = letters[i]
        new_name = name+ltr

        if '#' in name:
                new_name = name.replace('#', ltr, 1)
        i += 1

    return new_name

def get_mirror_node_names(node, left_side='L', right_side='R', include_center=False):
    """Return the mirrored side of fgiven node"""

    if not left_side:
        left_side = 'L'

    if not right_side:
        right_side = 'R'

    mNode = ''

    if node.startswith(left_side):
        mNode = node.replace(left_side, right_side, 1)

    elif node.startswith(right_side):
        mNode = node.replace(right_side, left_side, 1)

    elif '_%s_' % left_side in node:
        mNode = node.replace('_%s_' % left_side, '_%s_' % right_side, 1)

    elif '_%s_' % right_side in node:
        mNode = node.replace('_%s_' % right_side, '_%s_' % left_side, 1)

    elif include_center:
        mNode = node

    return mNode

###############################
# hierarchy and history utils
###############################

def get_shapes(node, ii=True, ln=False):
    """Return shape from specified node if the node IS a shape node
        then it returns the node itself

    ii = ignore intermediate objects.
    ln = return long names
    """
    if not mc.ls(node):
        return []

    result = []
    if mc.nodeType(node) in ['transform', 'joint']:
        shapes = mc.listRelatives(node, s=1, f=1, path=1) or []

        for shape in shapes:

            # Get intermediate shapes if that flag is set
            is_intermediate = mc.getAttr('%s.intermediateObject' % shape)

            if not is_intermediate:
                result.append(mc.ls(shape, sn=1)[0])

            elif not ii and is_intermediate:
                if mc.listConnections(shape, source=1):
                    result.append(mc.ls(shape, sn=1)[0])

    else:
        shapes = mc.ls(node, sn=1)
        if shapes:
            result.append(shapes[0])

    if ln:
        result = get_long_names(result)

    return convert_to_unicode(result)

class ModelPanel():
    """
    Set various options for the maya model panel.
    More types available at:
    https://help.autodesk.com/cloudhelp/2015/CHS/Maya-Tech-Docs/Commands/modelEditor.html
    Example Usage:
        from rigBot import utils

        mp = utils.ModelPanel()
        mp.set_allObjects_vis(0)
        mp.set_joints_vis(1)
        mp.set_jointXray_vis(0)
        mp.set_polymeshes_vis(1)

    """

    def __init__(self):
        self.get_model_panel()

    def get_model_panel(self):
        """ Get the current model panel. """
        mps = mc.getPanel(visiblePanels = True)
        for each in mps:
            if each.find("modelPanel")!=-1:
                self.mp = each
        #myPanel=str(mc.getPanel(wf=1))
        #if mc.getPanel(to=mp) == "modelPanel":

    def set_allObjects_vis(self, val=1):
        """
        Turn on/off the display of all objects for the view of the model editor.
        This excludes NURBS, CVs, hulls, grids and manipulators.
        """
        mc.modelEditor(self.mp, e=1, allObjects=val)

    def set_renderer(self, renderer_name = "vp2Renderer"):
        """
        Sets a models viewport renderer based on string input.
        Valid viewports are:
            "vp2Renderer"
            "base_OpenGL_Renderer"
        """
        mc.modelEditor(self.mp, e=1, rendererName=renderer_name)

    def set_locator_vis(self, val=1):
        mc.modelEditor(self.mp, e=1, locators=val)

    def set_nurbsCurves_vis(self, val=1):
        mc.modelEditor(self.mp, e=1, nurbsCurves=val)

    def set_deformers_vis(self, val=1):
        mc.modelEditor(self.mp, e=1, deformers=val)

    def set_ikHandles_vis(self, val=1):
        mc.modelEditor(self.mp, e=1, ikHandles=val)

    def set_joints_vis(self, val=1):
        mc.modelEditor(self.mp, e=1, joints=val)

    def set_jointXray_vis(self, val=1):
        mc.modelEditor(self.mp, e=1, jointXray=val)

    def set_lights_vis(self, val=1):
        mc.modelEditor(self.mp, e=1, lights=val)

    def set_grid_vis(self, val=1):
        mc.modelEditor(self.mp, e=1, grid=val)

    def set_polymeshes_vis(self, val=1):
        mc.modelEditor(self.mp, e=1, polymeshes=val)


def get_orig_shape(shape, ln=False):
    """Get the last intermediate shape"""

    result = ''
    node = get_transform(shape)

    shapes = [shape]
    shapes.extend(get_shapes(node, ii=1))
    intermediate_shapes = [s for s in get_shapes(node, ii=0)
                                if s not in shapes]

    if intermediate_shapes:
        result = mc.ls(intermediate_shapes, sn=1)[-1]

    if ln:
        result = get_long_names(result)

    return convert_to_unicode(result)


def get_children(node, ad=False, ln=False, node_type=None, s=False):
    """Get children OR all decendants exluding shapes from given node"""

    if not mc.ls(node):
        return []

    shapes = get_shapes(node, ln=1, ii=0)
    children = mc.listRelatives(node, c=1, ad=ad, f=1, path=1) or []

    if not s:
        if shapes:
            children = [c for c in children if c not in shapes]

    children = mc.ls(children, sn=1)
    if ln:
        children = get_long_names(children)

    result = []
    if node_type:
        for c in children:
            if mc.nodeType(c) == node_type:
                result.append(c)

    else:
        result = children

    return convert_to_unicode(result)

def get_parent(node, ln=False):
    """Return theparent for the given node"""

    parent = mc.listRelatives(node, p=1, f=1, path=1) or []
    if parent:
        parent = mc.ls(parent[0], sn=1)[0]
        if ln:
            parent = get_long_names(parent)
        return parent

def get_transform(shape, ln=False):
    """Get transform parent of given shape node.

    ln = Return long name.
    """

    if mc.nodeType(shape) in ['transform', 'joint']:
        if ln:
            return convert_to_unicode(get_long_names(shape))
        else:
            return convert_to_unicode(mc.ls(shape, sn=1)[0])

    else:
        transform = mc.listRelatives(shape, p=1, f=1)
        if transform:
            if ln:
                return convert_to_unicode(get_long_names(transform[0]))
            else:
                return convert_to_unicode(mc.ls(transform[0], sn=1)[0])

def get_deformers(shape, deformer_type):
    """Return deformers from shape"""

    try:
        history = mc.listHistory(shape, pdo=1) or []
        deformers = [h for h in history if mc.nodeType(h) == deformer_type]
    except:
        return []

    if not deformers:
        test_lattice = get_shapes(shape)
        if test_lattice:
            if mc.nodeType(test_lattice[0]) in ['lattice', 'baseLattice']:
                deformers = mc.listConnections(test_lattice[0], type=deformer_type)
                if deformers :
                    deformers = list(set(deformers))

    if deformers:
        return convert_to_unicode(deformers)
    else:
        return []

def get_constraints(nodes, return_ctrls=False):
    """Gert a list of contraints attatched to this node"""

    nodes = mc.ls(nodes)

    cons = []
    for node in nodes:
        connections = mc.listConnections(node, s=1, d=0, scn=1) or []
        cnn = [c for c in connections if mc.nodeType(c).endswith('Constraint')]
        if cnn:
            if return_ctrls:
                cons.append(node)
            else:
                cons.extend(cnn)

    cons = mc.ls(cons)
    cons = list(set(cons))
    cons.sort()

    return cons

def get_deformers_and_shapes(selection='', deformer_type='nonLinear'):
    """Return the shapes and deforms of the given type based on input OR selection"""

    node_types = ['transform',
                  'joint',
                  'mesh',
                  'bezierCurve',
                  'nurbsCurve',
                  'nurbsSurface',
                  'locator']

    if not selection:
        selection = mc.ls(sl=1)

    if selection and type(selection) == list:
        selection = selection[0]

    if not selection:
        raise ValueError('Nothing specifed or selected!')

    if not mc.objExists(selection):
        raise ValueError('Node doesnt exist!')

    deformers = []
    shapes = []

    # check if this is a mesh or deformer
    if mc.nodeType(selection) in node_types:
        deformers = get_deformers(selection, deformer_type)

    else:
        deformers = [selection]

    deformers = list(set(deformers))

    # Choose single deformer if several are available
    deformer = ''
    shapes = []

    if not deformers:
        test_lattice = get_shapes(selection)
        if test_lattice:
            if mc.nodeType(test_lattice[0]) in ['lattice', 'baseLattice']:
                deformers = mc.listConnections(test_lattice[0], type=deformer_type)
                if deformers :
                    deformers = list(set(deformers))

    if len(deformers) == 1:
        deformer = deformers[0]

    elif len(deformers) > 1:
        from rigBot.gui import mayaWidget
        deformer = mayaWidget.choose_deformer(deformers)

    # get shapes
    if deformers and not deformer:
        deformer = deformers[0]

    if deformer:
        shapes = mc.deformer(deformer, q=1, g=1)

    return deformer, shapes

###############################
# print utils
###############################

def print_list(node_list=None, columns=None, var_name='selection', fl=False):
    """Print a given list in block columkn format"""

    if node_list is None:
        node_list = mc.ls(sl=1, fl=fl)

    if not type(node_list) == list:
        raise ValueError('Variable is not a list.')

    node_list = convert_to_unicode(node_list)

    if not columns:
        columns = 4

    if var_name:
        arg = '%s = [' % var_name
        indent = ' ' * (len(var_name)+4)

    else:
        arg = '['
        indent = ' '

    for i in range(0, len(node_list), columns):
        if i > 0:
            arg += indent

        for ii in range(columns):
            if i+ii < len(node_list):
                arg += "'%s', " % node_list[i+ii]

        arg += '\n'

    print arg[:-3]+']\n'

def printConnections(selected=None):
    """Print connectiosn from selected nodes."""

    if not selected:
        selected = mc.ls(sl=1)
    selected = mc.ls(selected)

    for s in selected:
        print '\n# Incoming connections to {0}: '.format(s)
        cnns = mc.listConnections((s), s=1, c=1, d=0, p=1, scn=1) or []
        for i in range(0, len(cnns), 2):
            print cnns[i+1]+'  -->  '+cnns[i]

        print '\n# Outgoing connections from {0}:'.format(s)
        cnns = mc.listConnections((s), s=0, c=1, d=1, p=1, scn=1) or []
        for i in range(0, len(cnns), 2):
            print cnns[i]+'  -->  '+cnns[i+1]


def print_world_xforms(nodes=None):

    if not nodes:
        nodes = mc.ls(sl=1)

    nodes = mc.ls(nodes)

    for node in nodes:
        tresult = [round(v, 6) for v in mc.xform(node, q=1, ws=1, t=1)]
        rresult = [round(v, 6) for v in mc.xform(node, q=1, ws=1, ro=1)]
        arg = "mc.xform('{0}', ws=1, t={1})\n".format(node, tresult)
        arg += "mc.xform('{0}', ws=1, ro={1})\n".format(node, rresult)
        print arg

###############################
# Basic joint operation
def chain_parent(joints):
    """
    Parents each joint to the next joint in the list of joints
    """
    i = 0

    number_of_joints = len(joints)

    for each in joints:

        if i < number_of_joints-1 :
            mc.parent (joints[i],joints[i+1] )
            i += 1

    return joints

###############################
# Basic joint operations
###############################

def create_ik_solver(type, start_joint, end_joint, numberOfSpans=1):
    #print "made it into create ik solver"
    if type == "Single Chain":

        ikHandleNodes= mc.ikHandle(ee=end_joint,sj=start_joint,sol='ikSCsolver',n=(end_joint + "_IkHandle"))

    if type == "Rotate Plane":

        ikHandleNodes = mc.ikHandle(ee = end_joint,sj = start_joint,sol ='ikRPsolver',n=(end_joint  + "_IkHandle"))

    if type == "Spring":
        #initiate the spring solver
        mm.ikSpringSolver()

        ikHandleNodes = (mc.ikHandle(ee = end_joint,sj = start_joint,sol ='ikSpringSolver',n=(end_joint  + "_IkHandle")))

    if type == "Spline":
        ikHandleNodes = (mc.ikHandle(ee = end_joint,sj = start_joint,sol = 'ikSplineSolver',n=(end_joint  + "_IkHandle"), ns = numberOfSpans))
        splineCurve = mc.listConnections(ikHandleNodes[0], t = 'nurbsCurve')[0]

    effectorNode = mc.rename(ikHandleNodes[1],(end_joint  + "_IkEffector"))
    ikDictionary = {"handle":ikHandleNodes[0], "effector":effectorNode }

    return ikDictionary

###############################
# xfor mand selection utils
###############################

def get_xforms(a=0, t=1, ro=1):
    """Print world or absolute xforms for selected nodes"""

    nodes = mc.ls(sl=1)
    if a:
        ws = 0
    else:
        ws = 1

    for node in nodes:
        trans_xform = [round(x, 5) for x in mc.xform(node, q=1, ws=ws, a=a, t=1)]
        rot_xform = [round(x, 5) for x in mc.xform(node, q=1, ws=ws, a=a, ro=1)]

        if t and ro:
            print 'mc.xform("{0}", ws={1}, a={2}, t={3})'.format(node, ws, a, trans_xform)
            print 'mc.xform("{0}", ws={1}, a={2}, ro={3})'.format(node, ws, a, rot_xform)
            return trans_xform, rot_xform

        elif t:
            print 'mc.xform("{0}", ws={1}, a={2}, t={3})'.format(node, ws, a, trans_xform)
            return trans_xform

        elif ro:
            print 'mc.xform("{0}", ws={1}, a={2}, ro={3})'.format(node, ws, a, rot_xform)
            return rot_xform


def snap_to_transform(driver,
                         driven,
                         freezeTransformsTrueFalse = False,
                         worldOrLocal = "local"):
    '''Snaps to a point via temporary parentConstraint
        Follows standard driver, driven selection order for interactive mode
        Added the ability to freeze transfomations on the driven item
        Added the ability to drive only the transformation(pointConstraint) or
        translations and rotationss(parentConstraint)
    '''
    if worldOrLocal == "world":

        temp = mc.pointConstraint(driver,driven,mo = False)

    if worldOrLocal == "local":
        temp = mc.parentConstraint(driver,driven, mo = False)

    mc.delete(temp)
    if freezeTransformsTrueFalse == True:
        mc.makeIdentity(driven, apply=True, t=1, r=1)

def get_selection():
    """Get current selection"""

    sel = mc.ls(sl=1)

    print_list(sel, var_name='sel')
    mm.eval('python("sel = {0}")'.format(sel))

def get_selected_attrs(verbose=True):
    """Print list of selected channelbox attrs."""

    attrs = []
    channelBox = mm.eval('global string $gChannelBoxName; $temp=$gChannelBoxName;')

    sma = mc.channelBox(channelBox, q=True, sma=True) or []
    ssa = mc.channelBox(channelBox, q=True, ssa=True) or []
    sha = mc.channelBox(channelBox, q=True, sha=True) or []
    soa = mc.channelBox(channelBox, q=True, soa=True) or []

    attrs.extend(sma)
    attrs.extend(ssa)
    attrs.extend(sha)
    attrs.extend(soa)

    if verbose:
        print_list(attrs, var_name='attrs')
        mm.eval('python("attrs = {0}")'.format(attrs))

    return attrs

def get_mesh_data(shape):
    """Get point coordinatesa and triangles"""

    if not mc.nodeType(shape) == 'mesh':
        return {}

    # first get xforms
    transform = get_transform(shape)
    matrix = decompose_matrix(transform)

    obj = om.MObject()
    points = om.MPointArray()
    triangles = om.MIntArray()
    triangle_count = om.MIntArray()

    msel_list = om.MSelectionList()
    msel_list.add(shape)
    msel_list.getDependNode(0, obj)

    fnMesh = om.MFnMesh(obj)
    fnMesh.getTriangles(triangle_count, triangles)
    fnMesh.getPoints(points)

    point_list = []
    for i in range(points.length()):
        point_list.extend([points[i].x, points[i].y, points[i].z])

    data = {
        'matrix': matrix,
        'points': point_list,
        'triangles': list(triangles)
    }
    return data

def create_mesh_from_data(matrix, points, triangles):
    """Generate a mesh from saved data on disk."""

    if not matrix or not points or not triangles:
        return

    number_of_verts = len(points) / 3
    number_of_polygons = len(triangles) / 3
    polygon_connect_verts = om.MIntArray()
    polygon_count_array = om.MIntArray()
    vertex_array = om.MPointArray()

    for i in triangles:
        polygon_connect_verts.append(i)

    for i in xrange(0, len(points), 3):
        vertex_array.append(points[i], points[i+1], points[i+2])

    for i in xrange(number_of_polygons):
        polygon_count_array.append(3)

    new_shape = om.MFnMesh()
    new_shape.create(number_of_verts,
                   number_of_polygons,
                   vertex_array,
                   polygon_count_array,
                   polygon_connect_verts)

    new_node = get_transform(new_shape.name())

    # repo matrix
    mc.setAttr(new_node+'.rotateOrder', matrix[3])
    mc.xform(new_node, ws=1, t=matrix[0], ro=matrix[1])
    mc.xform(new_node, r=1, s=matrix[2])

    return new_node, new_shape.name()

def reverse_selection():
    """Reverses the current selection order"""

    sel = mc.ls(sl=1, l=1)
    sel.reverse()
    mc.select(sel)

def get_distance(src_node=None, dst_node=None):
    """Return the world distance between tow given nodes."""
    if not src_node or not dst_node:
        src_node, dst_node = mc.ls(sl=1)[0:2]

    if type(src_node) is not list:
        src_node = mc.xform(src_node, q=1, ws=1, t=1)
    if type(dst_node) is not list:
        dst_node = mc.xform(dst_node, q=1, ws=1, t=1)

    v1 = om.MVector(src_node[0], src_node[1], src_node[2])
    v2 = om.MVector(dst_node[0], dst_node[1], dst_node[2])
    return om.MVector(v2 - v1).length()

def create_distance_reader(start, end, chain_length=None, no_stretch=False):
    '''Create distacne reader node that has world and local scale, and stretch factor'''

    dst = get_unique_name(start+'_'+end+'_dst')
    dst = mc.createNode('transform', p=start, n=dst)
    dst_shape = mc.createNode('distanceDimShape', n=dst+'Shape', p=dst)

    s_mtx = mc.createNode('decomposeMatrix')
    e_mtx = mc.createNode('decomposeMatrix')

    mc.connectAttr(start+'.worldMatrix', s_mtx+'.inputMatrix')
    mc.connectAttr(end+'.worldMatrix', e_mtx+'.inputMatrix')

    mc.connectAttr(s_mtx+'.outputTranslate', dst_shape+'.startPoint')
    mc.connectAttr(e_mtx+'.outputTranslate', dst_shape+'.endPoint')
    mc.setAttr(s_mtx+'.ihi', 0)
    mc.setAttr(e_mtx+'.ihi', 0)

    if not no_stretch:
        mc.addAttr(dst, ln='jointChainLength', k=1)

    mc.addAttr(dst, ln='origDistance', k=1)
    mc.addAttr(dst, ln='worldDistance', k=1)
    mc.addAttr(dst, ln='localDistance', k=1)

    if not no_stretch:
        mc.addAttr(dst, ln='stretchFactor', k=1,)
        mc.addAttr(dst, ln='inverseStretchFactor', k=1)

    # Set init distance and world distance
    init_v = mc.getAttr(dst_shape+'.distance')
    mc.setAttr(dst+'.origDistance', init_v)
    mc.connectAttr(dst_shape+'.distance', dst+'.worldDistance')

    # connect local distance
    md = mc.createNode('multiplyDivide')
    mc.connectAttr(dst_shape+'.distance', md+'.i1x')
    mc.connectAttr(s_mtx+'.outputScaleX', md+'.i2x')
    mc.connectAttr(md+'.ox', dst+'.localDistance')
    mc.setAttr(md+'.operation', 2)
    mc.setAttr(md+'.ihi', 0)

    if not no_stretch:
        if chain_length is None:
            chain_length = init_v
            mc.setAttr(dst+'.jointChainLength', init_v)

        # Create stretch factor
        clamp = mc.createNode('clamp')
        mc.setAttr(clamp+'.minR', 0.0001)
        mc.setAttr(clamp+'.maxR', 100000000)

        md = mc.createNode('multiplyDivide')
        mc.connectAttr(dst+'.localDistance', clamp+'.inputR')
        mc.connectAttr(clamp+'.outputR', md+'.i1x')
        mc.connectAttr(dst+'.jointChainLength', md+'.i2x')
        mc.connectAttr(md+'.ox', dst+'.stretchFactor')
        mc.setAttr(md+'.operation', 2)
        mc.setAttr(md+'.ihi', 0)

        # Create inverse stretch factor
        md = mc.createNode('multiplyDivide')
        mc.connectAttr(dst+'.stretchFactor', md+'.i2x')
        mc.connectAttr(md+'.ox', dst+'.inverseStretchFactor')
        mc.setAttr(md+'.i1x', 1.0)
        mc.setAttr(md+'.operation', 2)
        mc.setAttr(md+'.ihi', 0)

    set_attrs(dst, 't r s v', k=0, l=1)
    set_attrs(dst, 'origDistance stretchFactor inverseStretchFactor worldDistance localDistance', k=1, l=1)
    mc.hide(dst_shape)
    mc.select(dst)

    return dst

def snap_locator(selection=None, name=None, node_type='locator'):
    """Create a locators centered around selection"""

    if not selection:
        selection = mc.ls(sl=1)
    selection = mc.ls(selection)

    # get BB and pos
    xyz = [0,0,0]

    try:
        bb = mc.exactWorldBoundingBox(selection, ii=1)
        xyz = [(bb[3]+bb[0])/2,
               (bb[4]+bb[1])/2,
               (bb[5]+bb[2])/2]

        jnt_nodes = [n for n in selection if mc.nodeType(n) == 'joint']
        trans_nodes = [n for n in selection if mc.nodeType(n) == 'transform']

        if jnt_nodes:
            tmp = mc.createNode('transform')
            mc.parentConstraint(jnt_nodes, tmp)
            xyz = mc.xform(tmp, q=1, t=1, ws=1)
            mc.delete(tmp)

        if xyz == [0,0,0] and trans_nodes:
            tmp = mc.createNode('transform')
            mc.parentConstraint(trans_nodes, tmp)
            xyz = mc.xform(tmp, q=1, t=1, ws=1)
            mc.delete(tmp)

    except:
        mc.warning('Could not get position to snap to. Creating and origin.')

    loc = get_transform(mc.createNode(node_type))
    mc.xform(loc, ws=1, t=xyz)

    # Rename
    if name:
        loc = mc.rename(loc, name)

    mc.select(loc)
    return loc

def create_group_above(node, name=None, parent_in_hierarchy=True):
    """
    This function creates a null above a transform that inherits the channel values
    it should be zeroed by default

    var transform str : The node to recieve a group above

    var name str : The name of the null grp to be created,
                        if None is assigned "_null_GRP" is suffixed to the created null GRP

    var parent_in_hierarchy bool : Parents transform into the existing hierarchy by
                                    grabbing the parent transform


    """

    #Assign a basic name if none is given.
    #User should assign for anything other than a test

    if name is None:
        name = node + "_null_GRP"

    parent_transform = get_parent(node,ln=True)
    print parent_transform
    null = mc.group(empty = True, n = name)

    #temp parent constrain the grp to the parentObj
    temporary_constraint = mc.parentConstraint(node,null)
    mc.delete (temporary_constraint)
    mc.parent (node, null)

    if parent_in_hierarchy is True:
        if parent_transform:
            mc.parent(null,parent_transform)
    return null



def find_center():
    """Finds the center of any combination of points/edges/transforms, creates a locator at that point and selects it

        Returns:
            (str) locator """

    sel = mc.ls(sl=True,fl = True)

    posPoints = []

    for each in sel:
        posPoint = mc.xform(each, q = True , ws = True, t = True)
        posPoints.append(posPoint)

    x = []
    y = []
    z = []

    i = 0
    for each in posPoints:

        currentX = each[0]

        currentY = each[1]

        currentZ = each[2]

        x.append(currentX)
        y.append(currentY)
        z.append(currentZ)
        i += 1

    x = sum(x)/len(posPoints)
    y = sum(y)/len(posPoints)
    z = sum(z)/len(posPoints)

    print x,y,z

    loc = mc.spaceLocator (a  = True)[0]
    mc.setAttr(loc+".translateX",x)
    mc.setAttr(loc+".translateY",y)
    mc.setAttr(loc+".translateZ",z)

    #xform(loc, cp = True)
    mc.select(loc)
    return loc


def create_node(n_type, **kwargs):
    """Create a node with config specified suffix,

    Kwargs:
        n, name = name of new node (string)
        p, parent = parent for new node (string)"""

    name = n_type
    parent = None
    suffix = get_suffix(n_type) or ''

    for k, v in kwargs.items():
        if k in ['n', 'name']:
            name = v
        elif k in ['p', 'parent']:
            parent = v

    suffix = get_suffix(n_type) or ''
    node_name = join_strings([name, '#', suffix])
    node_name = get_unique_name(node_name)

    if parent:
        node = mc.createNode(n_type, n=node_name, p=parent)
    else:
        node = mc.createNode(n_type, n=node_name)
    return node

def decompose_matrix(node, decimals=8):
    """Decompose world matrix of given node

    Returns:
        list(translate) list(rotate), list(scale), int(rotateOrder)
    """

    #Selection list object and MObject for our matrix
    selection = OpenMaya.MSelectionList()
    matrixObject = OpenMaya.MObject()

    selection.add(node)
    MObjectA = selection.getDependNode(0)
    fnThisNode = OpenMaya.MFnDependencyNode(MObjectA)

    worldMatrixAttr = fnThisNode.attribute('worldMatrix')
    matrixPlug = OpenMaya.MPlug(MObjectA, worldMatrixAttr)
    matrixPlug = matrixPlug.elementByLogicalIndex(0)

    matrixObject = matrixPlug.asMObject()
    worldMatrixData = OpenMaya.MFnMatrixData(matrixObject)
    worldMatrix = worldMatrixData.matrix()

    rotOrder = mc.getAttr(node+'.rotateOrder')

    mTransformMtx = OpenMaya.MTransformationMatrix(worldMatrix)

    trans = mTransformMtx.translation(OpenMaya.MSpace.kWorld)
    trans = [round(x, decimals) for x in [trans.x,trans.y,trans.z]]

    eulerRot = mTransformMtx.rotation()
    eulerRot.reorderIt(rotOrder)
    angles = [round(math.degrees(angle), decimals) for angle in (eulerRot.x, eulerRot.y, eulerRot.z)]

    scale = [round(s, decimals) for s in mTransformMtx.scale(OpenMaya.MSpace.kWorld)]

    return [trans, angles, scale, rotOrder]

###############################
# attr utils
###############################

def set_draw_override(nodes=[], display_type=None, set_on_shape=True):
    """Set drawing override display type

    Kwargs:
        :nodes: nodes to set
        :display_type: 0 - Normal, 1- tempalte, 2- Referenced, None- off (default=None)
    """

    if not nodes:
        nodes = mc.ls(sl=1)

    nodes = mc.ls(nodes)
    if not nodes:
        return

    shapes = []
    if set_on_shape:
        for node in nodes:
            shapes.extend(get_shapes(node))
        nodes.extend(shapes)

    for node in nodes:
        if display_type is None:
            mc.setAttr(node+'.overrideEnabled', 0)
        else:
            print display_type
            mc.setAttr(node+'.overrideEnabled', 1)
            mc.setAttr(node+'.overrideDisplayType', display_type)

def set_attrs(nodes=None, attrs='t r s v jo ro ud', l=False, k=True, cb=False):
    """Set lock keyable, locked and or cb state for specified attrs."""

    if nodes:
        nodes = mc.ls(nodes)
    else:
        nodes = mc.ls(sl=1)

    attrs = ' %s ' % attrs.strip()
    if ' t ' in attrs:
        attrs = attrs.replace(' t ',' tx ty tz ')
    if ' r ' in attrs:
        attrs = attrs.replace(' r ',' rx ry rz ')
    if ' s ' in attrs:
        attrs = attrs.replace(' s ',' sx sy sz ')
    if ' jo ' in attrs:
        attrs = attrs.replace(' jo ',' jox joy joz ')

    attrs = [a for a in attrs.strip().split(' ') if a]

    for node in nodes:
        for attr in attrs:
            if attr == 'ud':
                uds = mc.listAttr(node, ud=1) or []
                for ud in uds:
                    mc.setAttr(node+'.'+ud, k=k, l=l)
                    if cb:
                        mc.setAttr(node+'.'+ud, cb=cb)

            elif mc.objExists(node+'.'+attr):
                mc.setAttr(node+'.'+attr, k=k, l=l)
                if cb:
                    mc.setAttr(node+'.'+attr, cb=cb)

###############################
# module & part utils
###############################

def get_exception():
    """Throw all nodes in scene into a temp namespace
        to compare newly built guide nodes. Thissi  to avoid node name clashes.

    Returns:
        :Raised Exception and stack trace: (str)"""

    return "".join(traceback.format_exception(*sys.exc_info()))


def import_module(name, class_name=None, reload_it=True, verbose=False, catch_quiet=False, path_results=False):
    """Dynamic module import. Input string of module name and it returns your module.
    you are responsible for instantiating classes and otherwise
    properly using the module.

    Args:
        :name: (str) String token of the name of the module.
        :class_name: (str) String of the class name to instatiate.. you only need this if you want ot return an instance of the class instead of hte module.

    kwargs:
        :reload_it: (bool) Reload the module. Defaults to True.
        :verbose: (bool) Print output. Defaults to True.
        :catch_quiet: (bool) Does not throw an error if True. Defaults to True.

    Returns:
        (module, instance) imported module OR instantiated class object

    Usage:
        Importing a module::

            $ python myModule = utils.import_module('name')

        Instantiating a class::

            $ python myObject = import_module('name', 'ClassName')"""

    # rigBot system paths (facility)
    from rigBot import env

    if name.endswith('.py') and os.path.isfile(name):
        modules_to_check = [name]

    else:
        modules_to_check = [
                     'templates.'+name,
                     'rigBot.'+name,
                     'rigBot.asset.'+name,
                     'rigBot.data.'+name,
                     'rigBot.assemblies.'+name,
                     'rigBot.templates.'+name,
                     'rigBot.gui.'+name,
                     'rigBot.partsLibrary.'+name,
                     'rigBot.partsLibrary.generic.'+name,
                     name]

    # try impo
    module = None
    module_path = None

    for mod_name in modules_to_check:
        try:
            module = None
            module_path = None

            if os.path.isfile(mod_name):
                try:
                    module = imp.load_source(name, mod_name)
                except Exception as e:
                    if path_results:
                        return str('IMPORT ERROR: '+mod_name)
            else:
                module = importlib.import_module(mod_name)
                reload(module)

            module_path = module.__file__
            if verbose:
                print '{0} imported: {1}'.format(mod_name, module_path)

            if module_path:
                break

        except:
            if module:
                module = None

    if not module:
        error = get_exception()
        if catch_quiet:
                return

        raise ImportError(error)

    if module and class_name:
        try:
            module_class = getattr(module, class_name)
            instance = module_class()
            return instance

        except:
            error = get_exception()
            if catch_quiet:
                return
            raise RuntimeError(error)
    else:
        return module

def import_module(name, class_name=None, reload_it=True, verbose=False, catch_quiet=False, path_results=False):
    """Dynamic module import. Input string of module name and it returns your module.
    you are responsible for instantiating classes and otherwise
    properly using the module.

    Args:
        :name: (str) String token of the name of the module.
        :class_name: (str) String of the class name to instatiate.. you only need this if you want ot return an instance of the class instead of hte module.

    kwargs:
        :reload_it: (bool) Reload the module. Defaults to True.
        :verbose: (bool) Print output. Defaults to True.
        :catch_quiet: (bool) Does not throw an error if True. Defaults to True.

    Returns:
        (module, instance) imported module OR instantiated class object

    Usage:
        Importing a module::

            $ python myModule = utils.import_module('name')

        Instantiating a class::

            $ python myObject = import_module('name', 'ClassName')"""

    # rigBot system paths (facility)
    if os.path.isfile(name) and name.endswith('.py'):
        modules_to_check = [name]

    else:
        modules_to_check = ['templates.'+name,
                            'rigBot.'+name,
                            'rigBot.asset.'+name,
                            'rigBot.data.'+name,
                            'rigBot.assemblies.'+name,
                            'rigBot.templates.'+name,
                            'rigBot.gui.'+name,
                            'rigBot.partsLibrary.'+name,
                            'rigBot.partsLibrary.generic.'+name,
                            name]

    # try importing all these possibiliotes and reload the module if found.
    for mod_name in modules_to_check:

        module = None
        module_path = None

        if os.path.isfile(mod_name):
            try:
                module = imp.load_source(name, mod_name)
                module_path = module.__file__

                msg = None
                break

            except SyntaxError as e:
                msg = 'SYNTAX ERROR: (%s-%s): %s%s' % (e.lineno, e.offset, e.text, e.filename)

            except ImportError as e:
                msg = 'IMPORT ERROR: '+e.__class__.__name__+': '+str(e)

            except Exception as e:
                msg = 'ERROR: '+e.__class__.__name__+': '+str(e)

        else:
            try:
                module = importlib.import_module(mod_name)
                reload(module)

                module_path = module.__file__

                msg = None
                break

            except SyntaxError as e:
                msg = 'SYNTAX ERROR: lines (%s-%s): %s%s' % (e.lineno, e.offset, e.text, e.filename)

            except ImportError as e:
                msg = 'IMPORT ERROR: '+e.__class__.__name__+': '+str(e)

            except Exception as e:
                msg = 'ERROR: '+e.__class__.__name__+': '+str(e)

    # check the message and return if errored
    if msg:
        print msg
        if catch_quiet:
            return str(msg)

        else:
            if 'SYNTAX ERROR:' in msg:
                raise SyntaxError(msg)

            elif 'ERROR:' in msg:
                raise ImportError(msg)

            elif 'ERROR:' in msg:
                raise Exception(msg)

    if module and class_name:
        try:
            module_class = getattr(module, class_name)
            instance = module_class()
            return instance

        except:
            error = get_exception()
            if catch_quiet:
                return
            raise RuntimeError(error)
    else:
        return module










def create_cfx_locators():
    """Create world space locators for all bind jnts """

    side = 'C'
    set_suffix = get_suffix('objectSet')
    ctrl_suffix = get_suffix('animCtrl')
    grp_suffix = get_suffix('transform')
    loc_suffix = get_suffix('locator')

    mc.select('bindJoints_'+set_suffix)
    jnt_names = mc.ls(sl=1, type='joint')

    parent_node = get_parent(mc.ls('rig_GRP', side+'_parts_'+grp_suffix[0]))
    if not parent_node:
        parent_node = 'rig_GRP'

    hierarchy = get_children(parent_node, ad=1)
    jnts = [j for j in hierarchy if j in jnt_names]

    loc_parent_grp = 'world_locator_{1}'.format(side, grp_suffix)

    if not mc.objExists(loc_parent_grp):
        mc.createNode('transform', n=loc_parent_grp, p=parent_node)

        mc.hide(loc_parent_grp)
        mc.setAttr(loc_parent_grp+'.it', 0)
        mc.setAttr(loc_parent_grp+'.it', l=1)
        set_attrs(loc_parent_grp, 't r s', k=0, l=1)

    # Create locs
    for jnt in jnts:
        loc_name = jnt+'_'+loc_suffix
        if mc.objExists(loc_name):
            mc.rename(loc_name, loc_name+'#')

        loc = mc.createNode('locator', n='locatorShape#')
        loc = get_parent(loc)
        loc = mc.rename(loc, loc_name)

        mc.parent(loc, loc_parent_grp)
        mc.parentConstraint(jnt, loc)
        mc.scaleConstraint(jnt, loc, mo=1)

        if mc.objExists('cache_'+set_suffix):
            mc.sets(loc, add='cache_'+set_suffix)

def create_cfx_curves(jnts, name):
    """Create FX curves for given joint chain"""

    side = 'C'
    crv_suffix = get_suffix('nurbsCurve')
    set_suffix = get_suffix('objectSet')
    grp_suffix = get_suffix('transform')

    parent_node = get_parent(mc.ls('rig_GRP', side+'_parts_'+grp_suffix[0]))
    if not parent_node:
        parent_node = 'rig_GRP'

    parent_grp = 'fx_curve_{1}'.format(side, grp_suffix)

    if not mc.objExists(parent_grp):
        mc.createNode('transform', n=parent_grp, p=parent_node)

        mc.hide(parent_grp)
        mc.setAttr(parent_grp+'.it', 0)
        mc.setAttr(parent_grp+'.it', l=1)
        set_attrs(parent_grp, 't r s', k=0, l=1)

    crv = mc.curve(n=name+'_FX_'+crv_suffix, d=1, p=[[0,0,0]]*len(jnts))
    crv_shape = get_shapes(crv)[0]

    for i, jnt in enumerate(jnts):

        dmtx = mc.createNode('decomposeMatrix')
        point_attr = '{0}.controlPoints[{1}]'.format(crv_shape, i)
        mc.connectAttr(jnt+'.worldMatrix', dmtx+'.inputMatrix')
        mc.connectAttr(dmtx+'.outputTranslate', point_attr)
        mc.setAttr(dmtx+'.ihi', 0)

    mc.parent(crv, parent_grp)

    if mc.objExists('cache_'+set_suffix):
        mc.sets(crv, add='cache_'+set_suffix)

def get_new_file_version(path, file_name, ext='ma'):
    """Get new highest versio nfile"""

    if not os.path.isdir(path):
        return

    files = [f for f in os.listdir(path)
                            if re.search('_v[0-9][0-9][0-9].'+ext, f)]
    files.sort()
    files.reverse()

    v = '001'
    if files:
        version = int(files[0].split('.')[0].split('_v')[-1])
        v = str(version + 1).zfill(3)

    new_file_name = '{0}_v{1}.{2}'.format(file_name, v, ext)
    filepath = norm_path(os.path.join(path, new_file_name))
    return filepath

def set_historical_importance(state=0, nodes=None):
    """Turn off historical importance on nodes

    Kwargs:
        :state: Turn it on or off default(False).
        :nodes: Specify certain nodes.
        :all: Turn stateu for ALL nodes in scene. default(True)"""

    if nodes:
        nodes = mc.ls(nodes)

    else:
        nodes = mc.ls()

    # IF turning state to 0 we want ot exclude certain deformers and node types
    if state == 0:
        excluded = ['skinCluster', 'sculpt', 'blendShape', 'cluster',
                    'deltaMush', 'ffd', 'nonLinear', 'mesh', 'transform',
                    'nucleus', 'nCloth', 'nRigid', 'dynamicConstraint', 'nComponent']

        nodes = [d for d in nodes if mc.nodeType(d) not in excluded]

    # If turning state to 1 or 2 we want to excl,ude unitConversion nodes
    else:
        nodes = [n for n in nodes if mc.nodeType(n) != 'unitConversion1']

    for n in nodes:
        try:
            mc.setAttr(n+'.ihi', state)
        except:
            pass

    try:
        nodes = mc.ls(type=['nucleus', 'nCloth', 'nRigid', 'dynamicConstraint', 'nComponent'])
        for n in nodes:
            mc.setAttr(n+'.ihi', 1)
    except:
        pass

def shakeout_selection(selection):
    """Export and Reimport selection into a clean scene to get rig of unsued nodes."""

    mm.eval('deleteUnknownNodes()')
    tmp = mc.internalVar(utd=1)
    tmp_name = 'shakeout_{0}.mb'.format(random.randint(10**9, 10**10))
    tmp_path = os.path.join(tmp, tmp_name)

    selection = mc.ls(selection)
    mc.select(selection, hi=1)

    path = mc.file(tmp_path, f=1, options='v=0;',type='mayaBinary', pr=1, es=1)
    mc.file(new=1, f=1)

    mc.file(path, i=True)

def browse_path(path):
    """Lauch file browser"""

    if os.path.isdir(path):
        try:
            if sys.platform == 'linux2':
                try:
                    subprocess.check_call(('xdg-open', path))
                except:
                    subprocess.check_call(['gnome-open', path])

            elif sys.platform == 'darwin':
                subprocess.check_call(['open', '-R', path])
            elif sys.platform == 'win32':
                path = os.path.normpath(path)
                subprocess.Popen('explorer "{0}"'.format(path))

        except:
            mc.warning('Cannot open path: '+path)

def break_connections(nodes=None, attrs='t r s v jo ud'):
    """Break incomming connectionson specified nodes."""

    if nodes:
        nodes = mc.ls(nodes)
    else:
        nodes = mc.ls(sl=1)

    attrs = ' %s ' % attrs.strip()
    if ' t ' in attrs:
        attrs = attrs.replace(' t ',' tx ty tz ')
    if ' r ' in attrs:
        attrs = attrs.replace(' r ',' rx ry rz ')
    if ' s ' in attrs:
        attrs = attrs.replace(' s ',' sx sy sz ')
    if ' jo ' in attrs:
        attrs = attrs.replace(' jo ',' jox joy joz ')

    attrs = [a for a in attrs.strip().split(' ') if a]

    for node in nodes:
        for attr in attrs:
            if attr == 'ud':
                uds = mc.listAttr(node, ud=1) or []
                for uattr in uds:
                    if mc.objExists(node+'.'+uattr):
                        mm.eval('CBdeleteConnection "{0}"'.format(node+'.'+uattr))

            elif mc.objExists(node+'.'+attr):
                mm.eval('CBdeleteConnection "{0}"'.format(node+'.'+attr))


def create_twist_reader(parent, node):
    """Create a quaterion based twist reader.

    Args:
        :parent: Stable non twisting or parent node
        :node: node to drive the twist.

    Note:
        This breaks at 180 and -180. This gives you 360 degrees of twist."""

    # first create all the nodes
    name = node+'_twist_reader'

    mult_mtx = mc.createNode('multMatrix', n=name+'_multMtx')
    decomp_mtx = mc.createNode('decomposeMatrix', n=name+'_decompMtx')
    adl = mc.createNode('addDoubleLinear', n=name+'_adl')
    mdl = mc.createNode('multDoubleLinear', n=name+'_mdl')
    md = mc.createNode('multiplyDivide', n=name+'_md')

    reader = mc.createNode('quatToEuler', n=name)

    # add all the attrs
    mc.addAttr(reader, ln='twistOffset', k=1)
    mc.addAttr(reader, ln='numberTwistJoints', min=1, at='short', k=1, dv=1)
    mc.addAttr(reader, ln='twistOutput', k=1)
    mc.addAttr(reader, ln='distributedTwistOutput', k=1)

    # connect matrixes to extract quaternion twist value
    mc.connectAttr(parent+'.worldInverseMatrix', mult_mtx+'.matrixIn[1]')
    mc.connectAttr(node+'.worldMatrix', mult_mtx+'.matrixIn[0]')
    mc.connectAttr(mult_mtx+'.matrixSum', decomp_mtx+'.inputMatrix')
    mc.connectAttr(decomp_mtx+'.outputQuatX', reader+'.inputQuatX')
    mc.connectAttr(decomp_mtx+'.outputQuatW', reader+'.inputQuatW')

    # connect the user offset attr
    mc.connectAttr(reader+'.outputRotateX', adl+'.input1')
    mc.connectAttr(reader+'.twistOffset', adl+'.input2')
    mc.connectAttr(adl+'.output', reader+'.twistOutput')

    # now connect hte distributed twist joints
    # NOTE: these are for all the twist joints after the first Non twist
    mc.setAttr(md+'.operation', 2)
    mc.setAttr(md+'.input1X', 1)
    mc.connectAttr(reader+'.numberTwistJoints', md+'.input2X')

    mc.connectAttr(md+'.outputX', mdl+'.input1')
    mc.connectAttr(reader+'.twistOutput', mdl+'.input2')
    mc.connectAttr(mdl+'.output', reader+'.distributedTwistOutput')

    # tur noff ihi
    nodes = [mult_mtx, decomp_mtx, adl, mdl, md]
    for node in nodes:
        mc.setAttr(node+'.ihi', 0)

    # distplay
    mc.setAttr(reader+'.numberTwistJoints', k=0, cb=1)
    mc.setAttr(reader+'.twistOutput', l=1)
    mc.setAttr(reader+'.distributedTwistOutput', l=1)

    return reader

def translate_pose_driver(parent, joint, end_joint, world_orient=False):
    """Create a translation based pose driver (Legacy Maya 2016 > )

    Args:
        :parent: (str) Parent node
        :joint: (str) Driving joint.
        :end_joint: (str) End child joint.

    Kwargs:
        :world_orient: (bool) Orient the nodes to world. Defaults to False."""

    if not mc.objExists('translatePoseDrivers_GRP'):
        mc.createNode('transform', n='translatePoseDrivers_GRP', p='noXform_GRP')

    name = joint+'_POSE_DRV'

    if mc.objExists(name):
        return name

    grp = mc.createNode('transform',n=name+'_GRP', p='translatePoseDrivers_GRP')
    name = mc.createNode('transform',n=name, p=grp)

    if world_orient:
        mc.delete(mc.pointConstraint(joint, grp))
    else:
        mc.delete(mc.parentConstraint(joint, grp))

    mc.delete(mc.pointConstraint(end_joint, grp))
    mc.parentConstraint(parent, grp, mo=1, n=grp+'_prc')
    mc.scaleConstraint(parent, grp, mo=1, n=grp+'_sc')
    mc.pointConstraint(end_joint, name, mo=1, n=name+'_pc')
    mc.select(name)

    return name

def make_curve_dynamic(crv, name=''):
    """Make selected curve dynamic. Creates a hair system and parents nodes under a sim_GRP."""

    if not name:
        name = crv.split('_CRV')[0].split('_crv')[0]

    mc.select(crv)
    try:
        mm.eval('makeCurvesDynamic 2 { "0", "0", "1", "1", "0"};')
    except:
        pass

    hair_sys = get_parent(mc.ls(sl=1)[0])
    nucleus = mc.listConnections(hair_sys+'.startFrame')[0]
    follicle = mc.listConnections(hair_sys+'.inputHair')[0]
    dyn_crv = mc.listConnections(follicle+'.outCurve')[0]
    crv_grp = get_parent(dyn_crv)

    if mc.objExists('rig_GRP'):
        sim_grp = 'sim_GRP'
        if not mc.objExists('sim_GRP'):
            sim_grp = mc.createNode('transform', n='sim_GRP', p='rig_GRP')
            mc.parent(nucleus, sim_grp)

        mc.parent(hair_sys, sim_grp)

    else:
        mc.parent(dyn_crv, w=1)

    mc.parent(dyn_crv, hair_sys)

    mc.delete(crv_grp)
    dyn_crv = mc.rename(dyn_crv, name+'_DYN_CRV')
    hair_sys = mc.rename(hair_sys, name+'_HAIR_SYS')
    follicle = mc.rename(follicle, name+'_HAIR_FLL')

    # basic settings
    mc.setAttr(hair_sys+'.simulationMethod', 2)
    mc.setAttr(follicle+'.pointLock', 1)
    mc.setAttr(hair_sys+'.stiffnessScale[1].stiffnessScale_Position', 1)
    mc.setAttr(hair_sys+'.stiffnessScale[1].stiffnessScale_FloatValue', 0)
    mc.setAttr(hair_sys+'.bendResistance', 0.01)
    mc.setAttr(hair_sys+'.damp', 0.01)
    mc.setAttr(hair_sys+'.startCurveAttract', 0.01)
    mc.setAttr(hair_sys+'.collide', 0)

    #control.set_color('orange', hair_sys)
    #control.set_color('red', nucleus)
    mc.setAttr(nucleus+'.overrideEnabled', 1)
    mc.setAttr(nucleus+'.overrideColor', 13)
    try:
        mc.setAttr(nucleus+'.enable', 0)
    except RuntimeError:
        pass

    mc.setAttr(hair_sys+'.overrideEnabled', 1)
    mc.setAttr(hair_sys+'.overrideColor', 13)

    set_attrs([nucleus, hair_sys], 't r s v', l=1, k=0)

    attrs = ['dpq', 'cwd', 'ctw', 'bnf', 'hwd', 'bmp', 'opc', 'hcr', 'hcg',
                'hcb', 'hpc', 'thn', 'tlc', 'spr', 'spg', 'spb', 'spp',
                'csd', 'dfr', 'sra', 'chr', 'csr', 'cvr', 'mst', 'ms1',
                'ms2', 'leh', 'nmt', 'noi', 'dno', 'nof', 'nfu', 'nfv',
                'nfw', 'scm', 'scp', 'scr', 'nuc', 'nvc', 'cin', 'inr',
                'dcr', 'dcg', 'dcb', 'csh', 'ai_export_hair_ids',
                'disableFollicleAnim',
                'curlFrequency', 'curl', 'subSegments', 'staticCling', 'repulsion',
                'ai_export_hair_uvs', 'ai_export_hair_colors', 'primaryVisibility',
                'ai_override_hair', 'ai_hair_shaderr', 'ai_hair_shaderg',
                'ai_hair_shaderb', 'aiIndirectDiffuse']

    set_attrs(hair_sys+'Shape', ' '.join(attrs), l=1, k=0)
    mc.hide(dyn_crv)

    return hair_sys, nucleus, follicle, dyn_crv


def create_curve_from_edges(name, edge_loop=[], degree=2, spans='KEEP', side='L'):
    """Create a curve from edge loops"""

    mc.select(edge_loop)
    crv = mc.polyToCurve(form=2, degree=1, ch=0)

    if type(spans) is int:
        kcp = False
    else:
        kcp = True
        spans = -1

    crv = mc.rebuildCurve(crv, d=degree, s=spans, ch=0, rpo=1, rt=0, end=1, kr=1, kcp=kcp, kep=1, kt=0, tol=0.01)

    #reverse crv IF cv[0] is further out in X than the last cv
    cvs = mc.ls(crv[0]+'.cv[*]', fl=1)

    if name.startswith('L_') or name.startswith('C_'):
        if mc.xform(cvs[0], q=1, ws=1, t=1)[0] > mc.xform(cvs[-1], q=1, ws=1, t=1)[0]:
            crv = mc.reverseCurve(crv, ch=0, rpo=1)
    elif name.startswith('R'):
        if mc.xform(cvs[0], q=1, ws=1, t=1)[0] < mc.xform(cvs[-1], q=1, ws=1, t=1)[0]:
            crv = mc.reverseCurve(crv, ch=0, rpo=1)

    if name:
        crv = mc.rename(crv[0], name)
    else:
        crv = crv[0]

    return crv

def create_curve_from_nodes(name, nodes, degree=2, spans='KEEP'):
    """Create a curve from specified edge loops."""

    arg = 'curve -d '+str(degree)
    for j in nodes:
        x = mc.xform(j, ws=1, t=1, q=1)
        arg += ' -p {0} {1} {2}'.format(x[0], x[1],x[2])

    crv = mm.eval(arg)

    # Rebuild it
    if type(spans) is int:
        kcp = False
    else:
        kcp = True
        spans = -1

    crv = mc.rebuildCurve(crv, d=degree, s=spans, ch=0, rpo=1, rt=0, end=1, kr=1, kcp=kcp, kep=1, kt=0, tol=0.01)

    if name:
        crv = mc.rename(crv[0], name)
    else:
        crv = crv[0]

    return crv

def get_uniform_spacing_on_curve(crv, num_points):
    """Get world positions (X,Y,Z) uniformly spaced along a curve.

    Args:
        :crv: (str) Curve name.
        :num_points: (int) Number of positions.

    Returns:
        (list), (list) List of lists constainting x, y, z translations"""

    def get_dag_path(node=None):
        sel = om.MSelectionList()
        sel.add(node)
        d = om.MDagPath()
        sel.getDagPath(0, d)
        return d

    crvFn = om.MFnNurbsCurve(get_dag_path(crv))
    positions = []

    div = crvFn.length() / (num_points-1)

    for i in range(num_points):
        parameter = crvFn.findParamFromLength(div * i)
        point = om.MPoint()
        crvFn.getPointAtParam(parameter, point)
        positions.append([point.x,point.y,point.z])

    return positions


def insert_groups(node, number_grps=1):
    """Insert specified number of offset nodes.

    Args:
        :node: (str) Node to insert groups above.

    Kwargs:
        :number_grps: (int) Number of groupd to insert. Defaults to 3.

    Returns:
        (list) Group names."""

    grp_suffix = 'GRP'
    node_suffix = 'CTL'

    base_name = node.replace('_'+grp_suffix, '')

    # create nodea
    grps = []

    for i in range(number_grps):
        letter = utils.letters[i]
        grp_name = utils.join_strings([base_name, '#', grp_suffix])
        grp_name = utils.get_unique_name(grp_name)

        if grps:
            grps.append(mc.group(grps[-1], n=grp_name))
        else:
            grps.append(mc.group(node, n=grp_name))

    mc.xform(grps, piv=[0,0,0])
    mc.select(node)

    return grps

def remove_unknown_nodes():
    """Remove unknown nodes and plugins from scene."""

    nodes = mc.ls(type=['unknown', 'unknownDag', 'unknownTransform'])
    if nodes:
        mc.delete(nodes)

    mm.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

    plugins = mc.unknownPlugin(q=1, l=1) or []
    for p in plugins:
        try:
            mc.unknownPlugin(p, r=1)

        except:
            pass


def mel_to_py(mel_cmd, use_pymel=False, cmds_as='mc'):
    """Convert mel code to either python or pymel.

        Args:
            :mel_cmd: (str) Mel code to be converted.

        Kwargs:
            :use_pymel: (bool) If true, converts code to pymel, rather than maya.cmds. Defaults to False.
            :cmds_as: (str) Import maya cmds library as "blah". ie. import maya.cmds as "mc" Defaults to 'mc'."""

    import pymel.tools.mel2py as mel2py

    result = mel2py.mel2pyStr("""{0}""".format(mel_cmd))

    if use_pymel:
        print '\n# Mel to pymel converted code.'
        print result

    else:
        result = result.replace('from pymel.all import *', 'import maya.cmds as {0}'.format(cmds_as))
        functions = list(set([f[0] for f in inspect.getmembers(mc)]))

        for func in functions:
            print func
            result = result.replace(func, cmds_as+'.'+func)

        print '\n# Mel to maya.cmds as {0} converted code.'.format(cmds_as)
        print result



def spitback_move_cvs_to_current_pos():
    """Generate custom code to modify the position of cvs

        Select a series of cvs on any number of curves"""
    cvs = mc.ls(sl=True,fl = True)
    for each in cvs:
        v = mc.xform(each, q = True, ws = True, t= True)
        print """mc.xform('{0}', ws = True, t = {1})""".format(each,v)


def check_historical_importance(nodes='rig_GRP'):
    """Check whether historical importance set on or off on the rig_GRP node

    Kwargs:
        :nodes: Specify certain node to check historical importance.

    Usage:
        Throw this bit of code whereever you need to check for ihi

        .. code-block:: python

            if check_historical_importance():
                print 'Ready to keep working'

            else:
                rig.unfinalize()
                print 'rig was locked. but now you can work'"""

    nodes = mc.ls(nodes)

    for n in nodes:
        checkHistory = mc.getAttr(n+'.ihi')

        if checkHistory < 1:
            return False

    return True

# convert list of attr names to a str

# create the attribute save the info on

# save it

def tag_attrs_to_lock(nodes=None, attrs='', add=False):
    """Stores a list of attribute names in a string attribute for specified nodes

    Kwargs:
        :nodes: Specify certain nodes.
        :attrs: Specify attributes to lock for a certain node.
        :add: Turn it on when adding new attributes, default(False)."""

    attrs = ' %s ' % attrs.strip()
    if ' t ' in attrs:
        attrs = attrs.replace(' t ',' tx ty tz ')
    if ' r ' in attrs:
        attrs = attrs.replace(' r ',' rx ry rz ')
    if ' s ' in attrs:
        attrs = attrs.replace(' s ',' sx sy sz ')
    if ' jo ' in attrs:
        attrs = attrs.replace(' jo ',' jox joy joz ')

    attrs = [a for a in attrs.strip().split(' ') if a]

    if nodes:
        nodes = mc.ls(nodes)
    else:
        nodes = mc.ls(sl=1)

    for node in nodes:
        if not mc.objExists(node+'.tagLockedAttributes'):
            mc.addAttr(node, ln='tagLockedAttributes', dt='string')

    for node in nodes:
        if add:
            str_attr = mc.getAttr(node+'.tagLockedAttributes')
            if str_attr:
                eval_str_attr = ast.literal_eval(str_attr)
            else:
                eval_str_attr = []

            for attr in attrs:
                eval_str_attr.append(attr)
            mc.setAttr(node+'.tagLockedAttributes', str(eval_str_attr), type='string')
        else:
            mc.setAttr(node+'.tagLockedAttributes', attrs, type='string')

def lock_tagged_attrs(nodes=None):

    """Locks attributes stores in Tag Locked Attributes string attribute.

    Kwargs:
        :nodes: Specify certain nodes.
        :sel_nodes: Turn it on or off, default(True). """

    if nodes:
        nodes = [n+'.tagLockedAttributes' for n in mc.ls(nodes) if mc.objExists(n+'.tagLockedAttributes')]

    else:
        nodes = mc.ls('*.tagLockedAttributes')

    for node in nodes:

        str_attr = mc.getAttr(node)

        if str_attr:
            eval_str_attr = ast.literal_eval(str_attr)

            for attr in eval_str_attr:
                node_name = node.split('.')[0]

                if mc.objExists(node_name+'.'+attr):
                    mc.setAttr(node_name+'.'+attr, l=1, k=0, cb=0)


def select_mirror_names(add=False):

    current_sel = mc.ls(sl=1)

    mirrored_ctrls = []
    for ct in current_sel:

        # upper case single letter
        if ct.startswith('L_'):
            ct = ct.replace('L_', 'R_', 1)

        elif ct.startswith('R_'):
            ct = ct.replace('R_', 'L_', 1)

        elif '_L_' in ct:
            ct = ct.replace('_L_', '_R_', 1)

        elif '_R_' in ct:
            ct = ct.replace('_R_', '_L_', 1)

        # lower case single letter
        elif ct.startswith('l_'):
            ct = ct.replace('l_', 'r_', 1)

        elif ct.startswith('r_'):
            ct = ct.replace('r_', 'l_', 1)

        elif '_l_' in ct:
            ct = ct.replace('_l_', '_r_', 1)

        elif '_r_' in ct:
            ct = ct.replace('_r_', '_l_', 1)

        # lower case two letter s
        elif ct.startswith('lf_'):
            ct = ct.replace('lf_', 'rt_', 1)

        elif ct.startswith('rt_'):
            ct = ct.replace('rt_', 'lf_', 1)

        elif '_lf_' in ct:
            ct = ct.replace('_lf_', '_rt_', 1)

        elif '_rt_' in ct:
            ct = ct.replace('_rt_', '_lf_', 1)

        if ct not in mirrored_ctrls:
            mirrored_ctrls.append(ct)

    mirrored_ctrls = mc.ls(mirrored_ctrls)
    if mirrored_ctrls:
        if add:
            mc.select(mirrored_ctrls, add=1)
        else:
            mc.select(mirrored_ctrls)
    else:
        mc.warning('No mirrored names found!')

    return mirrored_ctrls

########################################################################
# Non QT based gui stuff

def file_browser(mode, file_filter='All Files (*.*)', file_path=None,  caption=None, button=None):
    """This is a wrapper for the fileDialog2 maya command, first, it checks if the given file_path exits,
        otherwise launches the browser.

        ARGS:
            :file_path: path to file, or directory
            :file_filter: file filter for file types. ie. 'Data Files (*.udattrs *.kattrs *.pose'
            :mode: Mode for file browser.
                        'SAVE' == Any file, whether it exists or not. 0
                        'LOAD' == A single existing file. 1
                        'SAVE MULTIPLE' == The name of a directory. Only directories are displayed in the dialog.
                        'LOAD MULTIPLE' == Then names of one or more existing files.
            :caption: Optional title for the dialog.
            :button: Optional caption for the OK, or Accept, button
        """

    if file_path and os.path.exists(file_path):
        return file_path

    if mode.upper() == 'SAVE':
        file_mode = 0
        if caption is None:
            caption = 'Save '+file_filter.split('(')[0].strip()
        if button is None:
            button = 'Save'

    elif mode.upper() == 'SAVE MULTIPLE':
        file_mode = 3
        if caption is None:
            caption = 'Save Multiple '+file_filter.split('(')[0].strip()
        if button is None:
            button = 'Save Multiple'

    elif mode.upper() == 'LOAD':
        file_mode = 1
        if caption is None:
            caption = 'Load '+file_filter.split('(')[0].strip()
        if button is None:
            button = 'Load'

    elif mode.upper() == 'LOAD MULTIPLE':
        file_mode = 4
        if caption is None:
            caption = 'Load Multiple '+file_filter.split('(')[0].strip()
        if button is None:
            button = 'Load Multiple'

    else:
        raise ValueError('mode not properly specified')

    file_path = mc.fileDialog2(fm=file_mode, cap=caption, okc=button, ff=file_filter)
    return file_path

def assign_shader(nodes, name='', shader_type='blinn'):

    if not name:
        name = shader_type

    nodes = mc.ls(nodes)
    if not nodes:
        return

    shd = name
    sg = name+'_SG'
    if not mc.objExists(shd):
        shd = mc.createNode(shader_type, n=shd)

    if not mc.objExists(sg):
        sg = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=sg)
        mc.connectAttr(shd+'.outColor', sg+'.surfaceShader')

    mc.sets(nodes, forceElement=sg)
    mc.select(nodes)

    return shd


def duplicate_joint_chain(jnts, name):

    if '{0}' not in name:
        name += '_{0}'

    new_jnts =[]
    for i, j in enumerate(jnts):
        nj = mc.duplicate(j, po=1, n=name.format(letters[i ]))[0]
        if new_jnts:
            mc.parent(nj, new_jnts[-1])
        new_jnts.append(nj)

    return new_jnts


def get_offset_matrix(nodeA, nodeB, verbose=False):

    def get_mtx(node):

        selection = OpenMaya.MSelectionList()
        matrixObject = OpenMaya.MObject()

        selection.add(node)
        MObjectA = selection.getDependNode(0)
        fnThisNode = OpenMaya.MFnDependencyNode(MObjectA)

        worldMatrixAttr = fnThisNode.attribute('worldMatrix')
        matrixPlug = OpenMaya.MPlug(MObjectA, worldMatrixAttr)
        matrixPlug = matrixPlug.elementByLogicalIndex(0)

        matrixObject = matrixPlug.asMObject()
        worldMatrixData = OpenMaya.MFnMatrixData(matrixObject)
        return worldMatrixData.matrix()

    parentWorldMatrix = get_mtx(nodeA)
    childWorldMatrix = get_mtx(nodeB)

    offset = childWorldMatrix * parentWorldMatrix.inverse()
    if verbose:
        print offset

    return [o for o in offset]

def ribbon_bin(jnts, axis=[1,0,0], offset=0.5, width=1.0, world_orient=False):

    p0 = [v*(width*0.5) for v in axis]
    p1 = [v*(-width*0.5) for v in axis]

    crv = mc.curve(d=1, p=[p0, p1])

    crvs = []
    for j in jnts:
        c = mc.duplicate(crv)[0]
        if world_orient:
            mc.delete(mc.pointConstraint(j, c))
        else:
            mc.delete(mc.parentConstraint(j, c))
        crvs.append(c)

    surf = mc.loft(crvs, ch=0)
    ribbon = mm.eval('nurbsToPoly -mnd 1  -ch 0 -f 2 -pt 1 -pc 200 -chr 0.1 -ft 0.01 -mel 0.001 -d 0.1 -ut 3 -un 1 -vt 3 -vn 1 -uch 0 -ucr 0 -cht 0.2 -es 0 -ntr 0 -mrt 0 -uss 1 '+surf[0])[0]
    mc.delete(surf, crv, crvs)

    mc.skinCluster(ribbon, jnts, dr=9.9, tsb=1)
    return ribbon


def get_fps():

    unit = mc.currentUnit(q=1, t=1)
    strs = {'game': 15.0,
            'film': 24.0,
            'pal': 25.0,
            'ntsc': 30.0,
            'show': 48.0,
            'palf': 50.0,
            'ntscf': 60.0}

    if unit in strs.keys():
        return strs[unit]

    elif 'fps' in unit or 'df' in unit:
        return float(unit.replace('fps', '').replace('df', ''))
    else:
        return unit

def create_light_locator(driver='', name='', xforms=[], full_name=''):

    driver = mc.ls(driver)
    if not driver:
        driver = mc.ls(sl=1)

    if not driver:
        return

    driver = driver[0]
    cache_sel = mc.ls('cache_SEL')
    model_grp = mc.ls('model_GRP', '*model_GRP')

    if not cache_sel:
        mc.warning('"cache_SEL" does not exist! Cannot continue.')
        return

    if not model_grp:
        mc.warning('model_GRP does not exist! Cannot continue.')
        return

    c_name = get_unique_name(driver.replace('_JNT', '_lighting_#_LOC', 1).replace('_CTL', '_lighting_#_LOC', 1))
    if name:
        c_name = get_unique_name(name+'_lighting_#_LOC')

    if full_name:
        c_name = full_name

    loc = snap_locator(driver, name=c_name)
    mc.parent(loc, model_grp[0])

    if xforms:
        mc.xform(loc, ws=1, t=xforms[0])
        mc.xform(loc, ws=1, ro=xforms[1])

    mc.parentConstraint(driver, loc, n=loc+'_PRC', mo=1)
    mc.scaleConstraint(driver, loc, n=loc+'_SC', mo=1)
    mc.sets(loc, add=cache_sel[0])

    mc.addAttr(loc, ln='lightingLocator', at='message')

    return loc

