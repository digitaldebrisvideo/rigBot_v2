import maya.cmds as mc
import maya.mel as mm

import os
import shutil
import sys

from rigBot import utils
from rigBot import control
from rigBot import env
from rigBot.data import controlShapes
from rigBot.data import kAttributes
from rigBot import partsLibrary

import traceback

try:
    import commstd
except:
    pass


def build(part_type, **kwargs):
    """Build a guide rig for a part module.

        Args:
            :part_type: (str) Part typoe to build.

        Kwargs:
            :variable args: Keyword args vary based on part type."""

    if part_type == 'worldRoot':
        if mc.objExists('C_worldRoot_guide'):
            mc.warning('Cannot build a second worldRoot.. There can only be one!')
            return

    else:
        if not mc.objExists('C_worldRoot_guide'):
            world_part = instantiate_part(part_type='worldRoot')
            world_part.set_guide(clear=1)
            world_part.build_guide()
            mc.warning('Building a worldRoot')

    part = instantiate_part(part_type=part_type)
    part.set_guide(clear=1)

    part.build_guide(**kwargs)

    update_guides_list()

    print 'BUILT PART: '+part.guide_master
    return part

def build_assembly(assembly):
    """Build an assembly of guide rigs.

        Args:
            :assembly: (str) Assembly name."""

    class_name = assembly[0].upper()+assembly[1:]
    ass = partsLibrary.import_part(assembly)

    if ass:
        ass.build_guide()
        print 'FINISHED BUILDING ASSEMBLY: '+assembly

def rebuild(selection=None, world_space=True, **kwargs):
    """Rebuild selected guide rigs with new options.

        Kwargs:
            :variable args: Keyword args vary based on part type."""

    obj = get_instance(selection)
    if not obj:
        return

    mc.select(obj.guide_master)
    obj.rebuild_guide(world_space=world_space, **kwargs)
    mc.select(obj.guide_master)

    update_guides_list()

    print 'DUPLICATED PART: '+obj.guide_master
    return obj

def get_exception():
    """Throw all nodes in scene into a temp namespace
        to compare newly built guide nodes. Thissi  to avoid node name clashes.

    Returns:
        :Raised Exception and stack trace: (str)"""

    return "".join(traceback.format_exception(*sys.exc_info()))

def rebuild_all():

    result = ''
    nodes = [g.split('.')[0] for g in mc.ls('*.guideMasterControl')]
    mc.select(cl=1)

    for n in nodes:
        try:
            mc.select(n)
            rebuild(world_space=False)
        except Exception as e:
            result += '\n'+get_exception()

    if result :
        print result
        mc.confirmDialog( title='Some errors occurred on rebuild',icon='warning', message=result, button=['OK'])

    mc.select(cl=1)

def mirror_all():

    result = ''
    nodes = [g.split('.')[0] for g in mc.ls('C_*.guideMasterControl', 'L_*.guideMasterControl')]
    mc.select(cl=1)

    for n in nodes:
        try:
            mc.select(n)
            mirror()
        except Exception as e:
            result += '\n'+get_exception()

    if result :
        print result
        mc.confirmDialog( title='Some errors occurred on rebuild',icon='warning', message=result, button=['OK'])

def duplicate(selection=None):
    """Duplicate selected guide rigs.

        Kwargs:
            :selection: (str) Guide master node to duplicate. Defaults to None."""

    obj = get_instance(selection)
    if not obj:
        return

    mc.select(obj.guide_master)
    obj.duplicate_guide()

    if not mc.objExists(obj.guide_master):
        return

    mc.select(obj.guide_master)

    update_guides_list()

    print 'DUPLICATED PART: '+obj.guide_master
    return obj

def mirror(selection=None):
    """Mirror selected guide rigs.

        Kwargs:
            :selection: (str) Guide master node to duplicate. Defaults to None."""

    objs = get_instance(selection, get_multiple=1)

    if not objs:
        mc.warning('Could not find any guide masters!')
        return

    masters = [o.guide_master for o in objs]
    result = []

    for master in masters:
        obj = instantiate_part(master=master)
        mc.select(master)
        obj.mirror_guide()
        result.append(obj)

        print 'MIRRORED PART: '+obj.guide_master

    update_guides_list()

    if len(result) == 1:
        return result[0]

    return result

def update_options(selection=None, **kwargs):
    """Update guide options based on selection OR specified master.

        Kwargs:
            :selection: (str) Guide master node to duplicate. Defaults to None.
            :variable args: Keyword args vary based on part type."""

    obj = get_instance(selection)
    if not obj:
        return

    mc.select(obj.guide_master)
    obj.update_options(**kwargs)

    update_guides_list()

    return obj

def get_options(selection=None, verbose=True, data_type=None):
    """Get guide part info based on selection OR specified master.

        Kwargs:
            :selection: (str) Guide master node to duplicate. Defaults to None.
            :verbose: Print results."""

    obj = get_instance(selection)
    if not obj:
        return

    if verbose:
        print '\nSELECTED PART TYPE: '+obj.part_type
        print '\nCURRENT GUIDE MASTER: '+obj.guide_master
        print '\nCURRENT BUILD OPTIONS:\n'
        for k, v in obj.options.items():
            print '\t{0} = {1}'.format(k, v)

    if data_type:
        o_info = obj.options_info_dict
        options = [o for o in obj.options.keys() if o_info.get(o)['data_type'] == data_type]

        dtype_options = {}
        for o in options:
            dtype_options[o] = obj.options[o]

        return dtype_options

    return obj.options

def write_to_json():
    """Write guide data to a json file"""

    rigbuild_path = env.get_rigbuild_path()
    asset = env.get_asset()

    if not asset or asset == 'None':
        mc.warning('Asset env not set!')
        return

    if not mc.objExists('|guides'):
        mc.warning('No guides in scene!')
        return

    # delete junk
    mm.eval('source "cleanUpScene.mel";')
    mm.eval('deleteUnknownNodes();')

    if mc.objExists('rigBuild_currentStep'):
        mc.delete('rigBuild_currentStep')

    # get lists of everything needed
    scale = mc.getAttr('|guides.sy')
    guide_masters = [c for c in utils.get_children('|guides') if mc.objExists(c+'.guideMasterCtrl')]
    for g in guide_masters:
        if 'global' in g:
            guide_masters.remove(g)
            guide_masters.insert(0, g)

    anim_ctrls = [n.replace('.animControl', '') for n in mc.ls('*.animControl')]
    pivot_ctrls = [n.replace('.animControlPivot', '') for n in mc.ls('*.animControlPivot')]
    extras =  [n.replace('.keepAsRef', '') for n in mc.ls('*.keepAsRef')]
    jnts = mc.ls('*_REF', type='joint')

    # build guides data dict
    data = {
            'guideScale': scale,
            'guideOrder': guide_masters,
            'guides': {},
            'nodes': {}
    }

    # get guides args
    for guide in guide_masters:
        options = get_options(guide, verbose=False)
        matrix = utils.decompose_matrix(guide)
        data['guides'][guide] = {'options': options, 'matrix': matrix}


    for node in jnts+extras+anim_ctrls+pivot_ctrls:
        matrix = utils.decompose_matrix(node)

        # If this is a ctrl grab ctrl info
        num_offset_ctrls = 0
        if mc.objExists(node+'.numOffsetCtrls'):
            num_offset_ctrls = mc.getAttr(node+'.numOffsetCtrls')

        mirror_mode = 0
        if mc.objExists(node+'.mirrorMode'):
            mirror_mode = mc.getAttr(node+'.mirrorMode')

        # get curve shape info
        shape_info = []
        shapes = [s for s in utils.get_shapes(node) if mc.nodeType(s).endswith('Curve')]
        for shape in shapes:
            points = control.get_crv_point(shape)
            d = mc.getAttr(shape+'.degree')
            form = mc.getAttr(shape+'.form')
            shape_info.append({'points':points, 'form':form, 'degree':d})

        color_info = control.get_color_value(node)

        data['nodes'][node] = {
                                'matrix': matrix,
                                'numOffsetCtrls': num_offset_ctrls,
                                'shapeInfo': shape_info,
                                'colorInfo': color_info
                            }

    file_path = utils.get_new_file_version(rigbuild_path, 'guide', 'json')
    utils.write_json(file_path, data)

def get_master(selection=None, verbose=True):
    """get guide master based on selection"""

    # get selection
    if selection is None:
        selection = mc.ls(sl=1)
    selection = mc.ls(selection)

    if selection:
        master = selection[0]
    else:
        master = ''

    if not mc.objExists(master+'.partType'):
        hierarchy = utils.get_long_names(master).split('|')
        master = ''
        for node in hierarchy:
            if mc.objExists(node+'.partType'):
                master = node

    if not mc.objExists(master+'.partType'):
        master += '_REF'

    if not mc.objExists(master+'.partType'):
        mc.warning('# Could not find guide master.')

    if verbose:
        print '\nGUIDE MASTER: '+master

    return master

def get_masters(selections=None, verbose=False, all=False):
    """Convenience function to loop the get_master() function.
        Selects and returns a list of master guides."""
    if selections is None:
        selections = mc.ls(sl = True)

    if all:
        selections = [g.split('.')[0] for g in mc.ls('*.guideMasterControl')]

    guides = []
    for each in selections:
        current_guide = get_master(selection=each, verbose=verbose)
        if current_guide != '':
            guides.append(current_guide)
    mc.select(guides)
    return guides

def instantiate_part(master=None, part_type='', verbose=True):
    """Find guide master and instatiate part object."""

    if not part_type:
        if master:
            master = get_master(master, verbose=verbose)
        else:
            master = get_master(verbose=verbose)

        if master and mc.objExists(str(master)+'.partType'):
            part_type = mc.getAttr(master+'.partType', asString=1)

    if not part_type:
        if verbose:
            mc.warning('Part type not specified!')
        return

    class_name = part_type[0].upper()+part_type[1:]
    obj =  partsLibrary.import_part(part_type)
    if master:
        obj.set_guide(master)
    return obj

def get_instance(selection=None, get_multiple=False):
    """Get class instance from selected part node.

        Returns:
            object (class instance)"""

    if 'instance' in str(type(selection)) and hasattr(selection, 'guide_master'):
        return selection

    # get selection
    if selection is None:
        selection = mc.ls(sl=1)
    selection = mc.ls(selection)

    # get guide masters
    guide_masters = list(set([get_master(s, verbose=0) for s in selection]))
    if not guide_masters:
        return

    # either get intances for all selected objects
    if get_multiple:
        objs = []
        for master in guide_masters:
            obj = instantiate_part(master, verbose=0)
            obj.set_guide(master)
            objs.append(obj)
        return objs

    # OR an instancefor just one
    else:
        obj = instantiate_part(guide_masters[0], verbose=0)
        obj.set_guide(guide_masters[0])
        return obj

def help(part_type='', verbose=True):
    """Print information about the specvified part module."""

    sel = mc.ls(sl=1)
    master = None
    if sel and not part_type:

        master = get_master(verbose=False)
        if not master:
            mc.warning('Select a node OR specify a part to query.')
            return

        part = instantiate_part(master, verbose=False)

    elif part_type:
        part = instantiate_part(part_type=part_type)
    else:
        mc.warning('Select a node OR specify a part to query.')
        return

    part.set_guide(clear=1)

    max_len = 0
    for key, value in part.options.items():
        l = len(key)
        if l > max_len:
            max_len = l

    result = '\n\n{0} rig part\n'.format(part.part_type).upper()
    result += '\t'+part.__doc__

    result += '\n\nBUILD ARGS:\n'
    arg = ',\n'

    for key, value in part.options.items():

        p_key = str(key)
        kl = len(key)
        for i in range(kl, max_len, 1):
            p_key += ' '

        tool_tip = part.options_info_dict[key]['tool_tip']
        data_type = part.options_info_dict[key]['data_type']
        result += '\t{0} = type({1}) default({3}) {2}\n'.format(p_key,
                                                             data_type,
                                                             tool_tip,
                                                             value)

        if type(value) in [str, unicode]:
            value = '"%s"' % value

        arg += '            {0}={1},\n'.format(key, value)


    result += '\nUSAGE FOR GUIDE BUILD:\n\n'
    result += 'guide.build("{0}"{1})'.format(part_type, arg)

    if verbose:
        print result
        get_options()

    else:
        return result

def save(write_data_file=False):
    """Wraqpper for comms td save stream"""

    if not mc.objExists('guides.guideMaster'):
        mc.warning('No guides in scene!')
        return

    update_guides_list()
    if write_data_file:
        save_guide_data_file()

    mc.selectPriority(locator=9)
    env.save_stream('guides', workfile=0)

def load_published(stream='guides', i=True, new_file=True, version='LATEST', check_scene=False, asset=None):
    load(stream, i, new_file, version, check_scene, asset=asset, use_published=True )

def load(stream='guides', i=True, new_file=True, version='LATEST', check_scene=False, use_published=False, asset=None):
    """Wraqpper for comms td save stream"""

    version = version.upper()

    if i:
        if new_file and check_scene:
            if not utils.save_changes():
                return


        env.import_stream(stream, version=version, asset=asset, workfile=0, new_file=new_file)

    else:
        if check_scene:
            if not utils.save_changes():
                return

        env.open_stream(stream, version=version, asset=asset, workfile=0)

    mm.eval('selectPriority -locator 9')

def update_guides_list(asset=None):
    """Updates the asset info file with new list og guides to build. This mostly used in the ui."""

    if not asset:
         asset = env.get_asset()

    if not asset or not mc.objExists('guides.guideMaster'):
        return

    guides = [mc.getAttr (g, asString=True) for g in mc.ls('*.partType')]
    guides = list(set(guides))
    guides.sort()

    if 'worldRoot' in guides:
        guides.remove('worldRoot')
        guides.insert(0, 'worldRoot')

    env.update_asset_info(guide_parts=guides)

def generate_doc_string(part_module):
    """This function will generate a doc string based on the options you've added into your part.
        You will still need to write a descriptions for your module along with any extra info needed.info

        Args:
            :part_module: (str) Part module to query for doc string."""

    part = instantiate_part(part_type=part_module, verbose=False)
    arg = '"""'+part_module[0].upper()+part_module[1:]+' module. Auto doc.\n\n'
    arg += '\tBuild Options:\n'

    for key in part.ordered_arg_list:
        if part.options_info_dict[key]['hidden']:
            continue

        default = part.options.get(key)
        tool_tip = part.options_info_dict[key]['tool_tip']
        data_type = part.options_info_dict[key]['data_type']

        if data_type in ['hook', 'enum', 'string']:
            data_type = 'str'
            default = '"%s"' % default

        if data_type in ['selection']:
            data_type = 'list'

        arg +='\t\t:{0}: ({1}) {2} Defaults to {3}.\n'.format(key, data_type, tool_tip, default)
    arg = arg[:-1]+'"""'

    print arg


def save_guide_data_file(browse=False, ascii=True):

    g_data = {
        'build_options': [],
        'joints': {},
        'node_data': {},
        'ctrl_shapes': {},
    }

    guide_grp = [g.split('.')[0] for g in mc.ls('guides.guideMaster')]
    guide_masters = [g.split('.')[0] for g in mc.ls('*.guideMasterControl')]

    if not guide_grp:
        mc.warning('Guides group does not exist')
        #return

    if not guide_masters:
        mc.warning('No guides in scene!')
        #return

    guide_grp = guide_grp[0]

    # get all build options
    build_options = []
    guide_parents = []
    for guide_master in guide_masters:
        partType = mc.getAttr(guide_master+'.partType', asString=1)
        options = get_options(guide_master, verbose=0)
        parent = utils.get_parent(guide_master)
        build_options.append([partType, options, parent])
        guide_parents.append(parent)

    guide_parents = list(set(guide_parents))
    g_data['build_options'] = build_options

    # get joint hierarchy and xforms
    joints = mc.ls('*_JNT', type='joint')
    joints.sort()

    joints_data = {}

    for joint in joints:
        parent = utils.get_parent(joint)
        if not parent in joints:
            gm = get_master(joint, verbose=0)
            g_options = get_options(gm, data_type='hook', verbose=0)
            if g_options:
                parent = g_options.values()[0]
            else:
                parent = None

        xforms = utils.decompose_matrix(joint)
        j_data = {'parent': parent,
                'translate': xforms[0],
                'rotate': xforms[1],
                'scale': xforms[2],
                'rotateOrder': xforms[3]}

        joints_data[joint] = j_data

    g_data['joints'] =  joints_data

    # get all other guide placer pivot and control nodes and values
    joint_placers = mc.ls('*_PLC_ZERO', '*_PLC')
    ctrl_pivots = mc.ls('*_CTL_ZERO', '*_CTL_CONST','*_CTL_MOCAP','*_PIV_CTL')
    ctrls = [c for c in mc.ls('*_CTL') if c not in ctrl_pivots]

    guide_nodes = guide_parents+ guide_masters+joint_placers+ctrl_pivots+ ctrls
    g_data['node_data'] = kAttributes.get_data(guide_nodes)

    # control shapes
    ctrl_crvs = [c for c in ctrls
                        if utils.get_shapes(c) and
                            mc.nodeType(utils.get_shapes(c)[0]) == 'nurbsCurve']

    crv_data = {}
    for c in ctrl_crvs:
        s_data = control.get_shape_data(c)
        color = control.get_color_value(c)
        crv_data[c] = {'shapes': s_data, 'color':color}

    g_data['ctrl_shapes'] = crv_data

    # Write to file
    if not env.get_asset():
        browse = True

    if browse:
        ff = 'Guide Data Files (*.guides)'
        file_path = utils.file_browser('SAVE', file_filter=ff)

        if not file_path:
            return

        file_path = file_path[0]

    elif env.get_asset():
        file_path = os.path.join(env.get_rigbuild_path(), env.get_asset()+'.guides')

        # Create backup
        '''
        if os.path.isfile(file_path):
            bak_file_path = utils.get_new_file_version(env.get_rigbuild_path(), env.get_asset(), 'guides')
            shutil.copyfile(file_path, bak_file_path)
        '''

    if file_path:
        if ascii:
            utils.write_json(file_path, g_data)

        else:
            utils.write_pickle(file_path, g_data)
    else:
        mc.warning('Could not write to path: '+file_path)

def build_guide_from_data_file(browse=False):

    if not env.get_asset():
        browse = True

    if browse:
        ff = 'Guide Data Files (*.guides)'
        file_path = utils.file_browser('LOAD', file_filter=ff)
        if not file_path:
            return

        file_path = file_path[0]

    elif env.get_asset():
        file_path = os.path.join(env.get_rigbuild_path(), env.get_asset()+'.guides')

    if not file_path:
        mc.warning('Could not read file path: '+file_path)
        return

    g_data = {}
    try:
        g_data = utils.read_json(file_path)
    except:
        g_data = utils.read_pickle(file_path)

    if not g_data:
        mc.warning('Could not read data from: '+file_path)
        return

    if not utils.save_changes():
        return

    # first build all guides
    for info in g_data.get('build_options'):
        part_type = info[0]
        options = info[1]
        parent = info[2]

        obj = build(part_type, **options)
        if not obj:
            continue

        gm = obj.guide_master
        if not mc.objExists(parent):
            parent = mc.createNode('transform', p='guides', n=parent)

        if utils.get_parent(gm) != parent:
            mc.parent(gm, parent)

    # set attr data
    for node, info in g_data.get('node_data').items():
        for attr, value in info.get('values').items():
            if attr != 'visibility':
                try:
                    mc.setAttr(node+'.'+attr, value)
                except:
                    pass

    guide_masters = [g.split('.')[0] for g in mc.ls('*.guideMasterControl')]
    for gm in guide_masters:
        mc.setAttr(gm+'.ctrlVis', 1)
        mc.setAttr(gm+'.jointPlacerVis', 1)
        mc.setAttr(gm+'.jointAxisVis', 0)
        mc.setAttr(gm+'.ctrlAxisVis', 0)
        mc.setAttr(gm+'.jointSelectable', 0)
        mc.setAttr(gm+'.v', 1)

    # set ctrl shapes
    for node, shape_data in  g_data.get('ctrl_shapes').items():

        s_data = []
        color = shape_data['color']
        for name, dat in shape_data['shapes'].items():
            s_data.append(dat)

        mc.delete(utils.get_shapes(node))
        tmp = mc.createNode('transform')
        control.create_shape(ctrls=tmp, data=s_data)
        control.copy_shape(tmp, node)
        mc.delete(tmp)

        control.set_color(ctrls=node, color=1, data=color)


