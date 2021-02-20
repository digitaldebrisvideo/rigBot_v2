# Asset Custom Module
import maya.cmds as mc
import maya.mel as mm
import time
import os

from rigBot import utils

file_extention = '.ncloth'
deformer_type = 'nCloth'

def get_data():

    all_nodes = mc.ls(type=['nucleus', 'nCloth', 'nRigid', 'dynamicConstraint', 'nComponent'])
    if not all_nodes:
        return {}

    ncloths = mc.ls(type=['nCloth'])
    nrigids = mc.ls(type=['nRigid'])
    ncons = mc.ls(type=['dynamicConstraint'])
    nucleus = mc.ls(type=['nucleus'])

    if not nucleus:
        return

    data = {}

    ncloth_data = {}
    nrigid_data = {}
    ncon_data = {}
    param_data = {}

    for cloth in ncloths:
        members = mc.listConnections(cloth+'.inputMesh')
        if members:
            ncloth_data[utils.strip_namespace(utils.get_transform(cloth))] = utils.strip_namespace(members[0])

    # get rigids members
    for rigid in nrigids:
        members = mc.listConnections(rigid+'.inputMesh')
        if members:
            nrigid_data[utils.strip_namespace(utils.get_transform(rigid))] = utils.strip_namespace(members[0])

    # get constraint members
    for con in ncons:
        mc.select(con)
        mm.eval('dynamicConstraintMembership "select";')
        members = [utils.strip_namespace(m) for m in mc.ls(sl=1)]

        parent = utils.strip_namespace(utils.get_parent(utils.get_transform(con)))
        ncon_data[utils.strip_namespace(utils.get_transform(con))] = { 'members': members, 'parent': parent}

    # Get params
    for node in all_nodes:
        attrs = mc.listAttr(node, k=1) or []
        attrs += mc.listAttr(node, cb=1) or []
        attrs += mc.listAttr(node, l=1) or []
        attrs += [a for a in mc.listAttr(node) or [] if 'PerVertex' in a]

        for a in attrs:
            try:
                value = mc.getAttr(node+'.'+a)
                if value is not None:
                    param_data[utils.strip_namespace(node)+'.'+a] = value

            except:
                pass

    data = {
        'nucleus': nucleus[0],
        'nCloth': ncloth_data,
        'nRigid': nrigid_data,
        'dynamicConstraint': ncon_data,
        'parameters': param_data
    }

    return data

def save(file_path):
    """Wrapper for class export call, Can export multiple and
        prompts for file path"""

    t = time.time()
    data = get_data()

    if not data:
        mc.warning('Nothing to save!!')
        return

    if not file_path.endswith(file_extention):
        file_path = os.path.splitext(file_path)[0]+'.ncloth'

    utils.write_json(file_path, data)
    print time.time() - t

def load(file_path, namespace='', **kwargs):
    """Wrapper for importing weights"""

    if namespace:
        namespace += ':'

    # If not remap then load as usual
    data = utils.read_json(file_path)

    create_nodes(data, namespace)
    set_data(data, namespace)

    nuc = mc.ls(type='nucleus')
    if nuc:
        mc.setAttr(nuc[0]+'.enable', 0)

    nodes = mc.ls(type=['nucleus', 'nCloth', 'nRigid', 'dynamicConstraint', 'nComponent'])
    for n in nodes:
        mc.setAttr(n+'.ihi', 1)

    if mc.objExists('sim_GRP'):
        mc.hide('sim_GRP')

    print 'loaded data: '+file_path

def create_nodes(data, namespace=''):

    if not data:
        return

    new_nodes = []
    for name, node in data['nCloth'].items():
        if mc.objExists(namespace+node) and not mc.objExists(namespace+name):
            mc.select(namespace+node)

            mm.eval('nClothCreate;')
            cloth = mc.ls(sl=1)[0]
            cloth = mc.rename(utils.get_parent(cloth), name)
            new_nodes.append(cloth)

    nucleus = mc.ls(type='nucleus')
    if not nucleus:
        raise RuntimeError('Cloth nodes not created and no nucleus found!')

    if not mc.objExists('sim_GRP'):
        mc.createNode('transform', n='sim_GRP', p='rig_GRP')

    nucleus = mc.rename(nucleus[0], data.get('nucleus'))

    for name, node in data['nRigid'].items():
        if mc.objExists(namespace+node) and not mc.objExists(namespace+name):
            mc.select(namespace+node)

            mm.eval('makeCollideNCloth;')
            rigid = mc.ls(sl=1)[0]
            rigid = mc.rename(utils.get_parent(rigid), name)
            new_nodes.append(rigid)

    try:
        mc.parent(nucleus, 'sim_GRP')
        mc.parent(new_nodes, 'sim_GRP')
    except:
        pass

    for name, con_dict in data['dynamicConstraint'].items():
        cmpts = con_dict.get('members')
        parent = con_dict.get('parent')

        if namespace:
            cmpts = [namespace+n for n in cmpts]

        cmpts = mc.ls(cmpts)

        if cmpts and not mc.objExists(namespace+name):
            mc.select(cmpts)
            mm.eval('createNConstraint transform 0;')
            con = utils.get_transform(mc.ls(sl=1)[0])

            con = mc.rename(con, name)
            try:
                mc.parent(con, parent)
            except:
                mc.parent(con, 'sim_GRP')

def set_data(data, namespace=''):

    for node, value in data.get('parameters').items():

        node = namespace+node
        try:
            try:
                mc.setAttr(node, value)
            except:
                mc.setAttr(node, value, type='doubleArray')
        except:
            pass



