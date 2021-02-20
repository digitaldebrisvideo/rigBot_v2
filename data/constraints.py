import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot.gui import remapDialog

import cPickle as pickle
import time
import os

deformer_type = 'constraints'
file_extention = '.cons'

constraint_types = ['pointConstraint',
                   'orientConstraint',
                   'parentConstraint',
                   'scaleConstraint',
                   'aimConstraint',
                   'normalConstraint',
                   'poleVectorConstraint',
                   'tangentConstraint',
                   'geometryConstraint',
                   'pointOnPolyConstraint']

def get_constraint_func(ntype):
    """Get constraint command function object based on contraint type"""

    func = None
    if ntype == 'pointConstraint':
        func = mc.pointConstraint

    elif ntype == 'orientConstraint':
        func = mc.orientConstraint

    elif ntype == 'parentConstraint':
        func = mc.parentConstraint

    elif ntype == 'scaleConstraint':
        func = mc.scaleConstraint

    elif ntype == 'aimConstraint':
        func = mc.aimConstraint

    elif ntype == 'normalConstraint':
        func = mc.normalConstraint

    elif ntype == 'poleVectorConstraint':
        func = mc.poleVectorConstraint

    elif ntype == 'tangentConstraint':
        func = mc.tangentConstraint

    elif ntype == 'geometryConstraint':
        func = mc.geometryConstraint

    elif ntype == 'pointOnPolyConstraint':
        func = mc.pointOnPolyConstraint

    return func

def get_data(nodes=[]):
    """Get constraint data dict from nodes"""

    # get nodes
    if not nodes:
        nodes = mc.ls(sl=1)

    # decipher if the nodes are constraints themselves or are driven by constraints
    nodes = mc.ls(nodes)
    constraints = [n for n in nodes if mc.nodeType(n) in constraint_types]
    non_con_nodes = [n for n in nodes if n not in constraints]
    constraints.extend(utils.get_constraints(non_con_nodes))

    data = {}

    for constraint in constraints:

        # get driven target nodes
        ntype = mc.nodeType(constraint)
        constraint_func = get_constraint_func(ntype)
        driven = mc.listConnections(constraint+'.constraintParentInverseMatrix') or []
        drivers = constraint_func(constraint, q=1, tl=1)

        if not ntype in constraint_types or not driven or not drivers:
            continue

        driven = list(set(driven))
        weight_alias_list = constraint_func(constraint, q=1, wal=1)

        con_data = {
            'con_type': ntype,
            'drivers': drivers,
            'driven': driven,
            'weight_list': [mc.getAttr(constraint+'.'+w) for w in weight_alias_list]
        }

        # Create dict entry for constrant types with upvectors
        if ntype in ['aimConstraint', 'tangentConstraint', 'normalConstraint']:

            aim = constraint_func(constraint, q=1, aim=1)
            upv = constraint_func(constraint, q=1, u=1)
            wupv = constraint_func(constraint, q=1, wu=1)
            wut = constraint_func(constraint, q=1, wut=1)
            wuo = constraint_func(constraint, q=1, wuo=1)

            if type(wuo) == list:
                wuo = wuo[0]

            con_data['aim'] = aim
            con_data['u'] = upv
            con_data['wu'] = wupv
            con_data['wut'] = wut
            con_data['wuo'] = wuo

        if mc.objExists(constraint+'.interpType'):
            con_data['interp_type'] = mc.getAttr(constraint+'.interpType')

        data[constraint] = con_data

    return data

def set_data(data, verbose=True):
    """Set deformation stack"""

    for name, con_data in data.items():

        # get data
        ntype = con_data.get('con_type')
        drivers = con_data.get('drivers')
        driven = con_data.get('driven')
        weight_list = con_data.get('weight_list')
        interp_type = con_data.get('interp_type')

        constraint_func = get_constraint_func(ntype)
        constraint = None

        # Recreate constraints with aim and ups
        try:
            if ntype in ['aimConstraint', 'tangentConstraint', 'normalConstraint']:

                aim = con_data['aim']
                u = con_data['u']
                wu = con_data['wu']
                wut = con_data['wut']
                wuo = con_data['wuo']

                for i, driver in enumerate(drivers):
                    if wuo:
                        constraint = constraint_func(driver, driven, aim=aim, u=u, wu=wu, wut=wut, wuo=wuo, mo=1, w=weight_list[i])[0]
                    else:
                        constraint = constraint_func(driver, driven, aim=aim, u=u, wu=wu, wut=wut, mo=1, w=weight_list[i])[0]

            else:
                for i, driver in enumerate(drivers):
                    try:
                        constraint = constraint_func(driver, driven, mo=1, w=weight_list[i])[0]
                    except:
                        constraint = constraint_func(driver, driven, w=weight_list[i])[0]

            if mc.objExists(constraint+'.interpType'):
                mc.setAttr(constraint+'.interpType', interp_type)

            constraint = mc.rename(constraint, utils.get_unique_name(name.split('|')[-1]))

            if verbose:
                print 'Created constraint: '+constraint

        except:
            if verbose:
                print data
                mc.warning('Could not create constraint! '+name)

    return True

def save(file_path, nodes=[]):
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
    return file_path
    print time.time() - t

def load(file_path, remap=False, **kwargs):
    """Wrapper for importing weights"""

    if remap:
        data = utils.read_json(file_path)

        # get nodes to remap
        nodes = []
        for name, con_data in data.items():
            nodes.extend(con_data.get('drivers'))
            nodes.extend(con_data.get('driven'))
            nodes.extend([ i for i in [con_data.get('wuo', '')] if i])

        remap_dialog = RemapContraints(nodes=nodes)
        remap_dialog.data = data
        remap_dialog.show()
        return

    # If not remap then load as usual
    else:
        data = utils.read_json(file_path)

        nodes = []
        for name, con_data in data.items():
            nodes.extend(con_data.get('drivers'))
            nodes.extend(con_data.get('driven'))
            nodes.extend([ i for i in [con_data.get('wuo', '')] if i])

        if not len(nodes) == len(mc.ls(nodes)):
            mc.warning('Nodes need remapping! File path: {0}'.format(file_path))
        else:
            set_data(data)


def weighted_constraint(mesh=None, nodes=None, values=[]):
    """Createa constraint based on skin weights for the closest vert"""

    if not mesh and not nodes:
        nodes = mc.ls(sl=1)[:-1]
        mesh = mc.ls(sl=1)[-1]

    nodes = mc.ls(nodes)

    cpom = mc.createNode('closestPointOnMesh')
    shape = utils.get_shapes(mesh)[0]

    mc.connectAttr(shape+'.outMesh', cpom+'.inMesh')

    for grp_node in nodes:

        node = mc.listRelatives(grp_node, c=1)[0]
        scls = mm.eval('findRelatedSkinCluster '+mesh)

        utils.set_attrs([node, grp_node], k=1, l=0)

        pos = mc.xform(grp_node, q=1, ws=1, t=1)
        mc.setAttr(cpom+'.inPosition', pos[0], pos[1], pos[2])
        vert = mesh+'.vtx[{0}]'.format(mc.getAttr(cpom+'.closestVertexIndex'))

        existing_cons = utils.get_constraints([grp_node, node])
        if existing_cons:
            mc.delete(existing_cons)

        # get influences
        if values:
            sorted_influences = values
        else:
            infs = mc.skinCluster(scls, q=1, inf=1)

            # get values
            weighted_influences = {}
            values = []
            for inf in infs:
                val = mc.skinPercent(scls, vert, q=1, t=inf, v=1)
                val = round(val, 3)

                if val > 0.0:
                    weighted_influences[inf] = val
                    values.append(val)

            values.sort()
            values.reverse()

            sorted_influences = []
            for sv in values:
                for inf, val in weighted_influences.items():
                    if val == sv:
                        sorted_influences.append([inf, val])

        suffix = utils.get_suffix('parentConstraint')
        prc1 = mc.parentConstraint(sorted_influences[0][0], grp_node, n=grp_node+'_'+suffix, mo=1)[0]
        for si in sorted_influences:
            prc2 = mc.parentConstraint(si[0], node, n=node+'_'+suffix, mo=1, weight=si[1])[0]

        mc.setAttr(prc2+'.interpType', 2)
        mc.addAttr(prc1, ln='weighted_constraint', at='message')

    mc.delete(cpom)

class RemapContraints(remapDialog.RemapDialog):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, nodes=[], ignore_missing=False, label=''):
        remapDialog.RemapDialog.__init__(self, nodes, False, 'Non-Linear Remap UI')

        self.data = {}

    def finish_command(self):
        """update data dict with new mapping and load the data"""

        # remap parent
        for key, con_data in self.data.items():

            self.data[key]['drivers'] = [self.mapping[d] for d in con_data.get('drivers')]
            self.data[key]['driven'] = [self.mapping[d] for d in con_data.get('driven')]

            if 'wuo' in con_data.keys() and con_data.get('wuo') in self.mapping.keys():
                self.data[key]['wuo'] = self.mapping[con_data.get('wuo')]

        set_data(self.data)

def constraint_multiple(selection=None, constraint_types=['parentConstraint', 'scaleConstraint']):
    """Parent constraint multple objecto to a driver. Select driver first"""

    if type(constraint_types) is not list:
        constraint_types = [constraint_types]

    if not selection:
        selection = mc.ls(sl=1)
    selection = mc.ls(selection)

    if not len(selection) > 1:
        mc.warning('Select at least two nodes')

    suffix = utils.get_suffix('parentConstraint')
    scale_suffix = utils.get_suffix('scaleConstraint')

    driver = selection[0]
    driven = selection[1:]

    for con_type in constraint_types:

        con_func = get_constraint_func(con_type)

        for node in driven:
            con_func(driver, node, n=node+'_'+suffix, mo=1)

