from rigBot import env
from rigBot.data import controlShapes

import re
import os
import imp
import sys
import getpass
import traceback
import shutil

import maya.cmds as mc

def get_exception():
    """Throw all nodes in scene into a temp namespace
        to compare newly built guide nodes. Thissi  to avoid node name clashes.

    Returns:
        :Raised Exception and stack trace: (str)"""

    return ''.join(traceback.format_exception(*sys.exc_info()))

def get_paths():

    part_dict = {}
    asset = env.get_asset() or '%NO%ASSET%IS%SET%'
    part_paths = env.get_parts_paths()

    all_paths = []

    for part_path in part_paths:
        if os.path.isdir(part_path):
            all_paths.append(part_path)

            if asset not in part_path:
                for root, directories, filenames in os.walk(part_path):
                    for directory in directories:
                        p = os.path.join(root, directory)
                        if p not in all_paths:
                            all_paths.append(p)

    return all_paths

def get_module_files():

    discovered_modules = []
    part_paths = get_paths()
    file_paths = []

    for path in part_paths:
        modules = [f for f in os.listdir(path) or [] if f.endswith('.py') and f != '__init__.py']

        for module in modules:
            if module not in discovered_modules:

                file_path = os.path.join(path, module)

                line = ''
                if os.path.isfile(file_path):
                        with open(file_path, 'r') as f:
                            line = f.readline().rstrip().strip()

                if line.startswith('#')  and '-*-' in line and 'rigBot:' in line:
                    file_paths.append(file_path)
                    discovered_modules.append(module)

    return file_paths

def list_parts(by_category=False, verbose=True):

    asset = env.get_asset() or '%NO%ASSET%IS%SET%'

    if by_category:

        data = {}
        cats = []
        parts = [os.path.splitext(p)[0] for p in get_module_files()]
        parts = [p for p in parts if 'standardPart' not in p]
        parts = [p for p in parts if 'emptyPart' not in p]
        parts.sort()

        for p in parts:
            cat = os.path.basename(os.path.dirname(p))
            cats.append(cat)

            if asset in p:
                cat = asset+' - ASSET'

            if cat in data.keys():
                data[cat].append(os.path.basename(p))
            else:
                data[cat] = [os.path.basename(p)]

        cats = list(set(cats))
        cats.sort()

        for cat in data.keys():
            data[cat].sort()

        if verbose:
            print '\nPARTS LIBRARY MODULES BY CATEGORY:'

            for cat in cats:
                print '\n\t'+cat.upper()

                for p in data[cat]:
                    print '\t\t'+p
        else:
            return data

    else:
        parts = [os.path.basename(os.path.splitext(p)[0]) for p in get_module_files()]
        parts = [p for p in parts if 'standardPart' not in p]
        parts = [p for p in parts if 'emptyPart' not in p]
        parts.sort()

        if verbose:
            print '\nPARTS LIBRARY MODULES:'
            for p in parts:
                print '\t'+p

        else:
            return parts

def import_part(part_name, with_path=False):

    part_name = os.path.splitext(part_name)[0]
    class_name = part_name[0].upper()+part_name[1:]

    # Get the file path for specified part
    module = None
    module_path = None
    files = get_module_files()

    for f in files:
        if f.endswith(part_name+'.py'):
            module_path = f

    # Check if file exists
    if not module_path:
        raise Exception ('File not found for part: '+part_name)

    if module_path and not os.path.isfile(module_path):
        raise Exception ('File not found! PART: {0} FILE PATH: {1}'.format(part_name, module_path))

    # now that i found the file try importing it
    try:
        module = imp.load_source(part_name, module_path)

    except Exception as e:
        raise ImportError(get_exception())

    try:
        module_class = getattr(module, class_name)
        instance = module_class()

        if with_path:
            return instance, module_path
        else:
            return instance

    except:
        raise ImportError(get_exception())

def help(part, verbose=True):
    """Print information about the specvified part module."""

    instance, file_path = import_part(part, 1)
    if not instance:
        return

    category = os.path.basename(os.path.dirname(file_path))

    asset = env.get_asset() or '%NO%ASSET%IS%SET%'

    if asset in file_path:
        category = asset+' - ASSET'

    docstr = instance.__doc__

    doc = 'PART: '+instance.__module__+'\n\n'
    doc += 'CATEGORY: '+category+'\n\n'
    doc += 'FILE PATH: '+file_path+'\n\n'

    try:
        doc +='DESCRIPTION:\n'
        doc += re.sub( ' +', ' ', docstr.split('Build Options:')[0]).replace('\n ', '\n')

        try:
            arg = 'BUILD OPTIONS:\n'

            for key, value in instance.options.items():

                p_key = str(key)
                kl = len(key)
                for i in range(kl, max_len, 1):
                    p_key += ' '

                tool_tip = instance.options_info_dict[key]['tool_tip']
                data_type = instance.options_info_dict[key]['data_type']
                arg += '\t{0} = type({1}) default({3}) {2}\n'.format(p_key, data_type, tool_tip, value)

                if type(value) in [str, unicode]:
                    value = '"%s"' % value

            doc += arg

        except:
            pass
    except:
        doc = 'Could not retrieve module documentation!'

    if verbose:
        print doc

    else:
        return instance, str(instance.__module__), category, file_path, doc

def new_assembly(module_path=''):
    """Save a new assembly module to either the asset level or the rigBot
        system level (must be in your sandbox git repo for the proper write permission.)"""

    def get_options(guide_master):
        part = mc.getAttr(guide_master+'.partType', asString=1)
        mod = import_part(part)
        mod.set_guide(guide_master)
        options = mod.options

        return options

    if not os.path.isdir(os.path.dirname(module_path)):
        from rigBot.gui import newPart

        module_path = newPart.get_path(assembly_mode=True)
        if not module_path:
            print 'New assembly cancelled by user.'
            return

    try:
        os.makedirs(os.path.dirname(module_path), 0777)
    except:
        pass

    if not os.path.isdir(os.path.dirname(module_path)):
        mc.warning('Could not create path: '+os.path.dirname(module_path))
        return

    name = os.path.basename(module_path).split('.')[0]
    new_assembly_class = name[0].upper()+name[1:]

    # Now gather all guides in scene
    all_guides = [g.replace('.partType', '') for g in mc.ls('*guide.partType')]
    if not all_guides:
        mc.warning('No guides in scene!')
        return

    # gather all nodes to record joint_suffix = utils.get_suffix('joint')
    all_hierarchy = mc.ls(mc.listRelatives('|guides', c=1, ad=1, f=1, path=1) or [])

    plcs = [c for c in all_hierarchy if c.endswith('_JNT_PLC')]
    pivots = [c for c in all_hierarchy if mc.objExists(c+'.animControlPivot')]
    ctrls = [c for c in all_hierarchy if mc.objExists(c+'.animControl')]

    all_nodes = all_guides+plcs+pivots+ctrls

    # generate python code
    arg = '# -*- rigBot: assembly -*-\n'
    arg += 'from rigBot import guide\n'
    arg += 'from rigBot.data import controlShapes\n'
    arg += 'import maya.cmds as mc\n\n'

    arg += 'class {0}():\n'.format(new_assembly_class)
    arg += '\t"""Generated assembly build."""\n\n'

    arg += '\tdef __init__(self):\n\t\tpass\n\n'

    arg += '\tdef build_guide(self):\n'
    arg += '\t\t"""Build Assembly guide parts"""\n\n'

    world_guide = 'C_worldRoot_guide'
    if world_guide in all_guides:
        all_guides.remove(world_guide)
        all_guides.insert(0, world_guide)

    for guide_master in all_guides:
        part_type = mc.getAttr(guide_master+'.partType', asString=1)
        options = get_options(guide_master)
        if options:
            arg += '\t\tguide.build("{0}", **{1})\n'.format(part_type, options)
        else:
            arg += '\t\tguide.build("{0}")\n'.format(part_type)

    arg += '\n\t\t#Position nodes'
    for node in all_nodes:

        arg += '\n\t\tif mc.objExists("{0}"):\n'.format(node)

        extra_attrs = ['numOffsetCtrls', 'mirrorMode', 'rotateOrder']
        for attr in extra_attrs:
            if mc.objExists(node+'.'+attr):
                if not mc.getAttr(node+'.'+attr, l=1):
                    value = mc.getAttr(node+'.'+attr)
                    arg += '\t\t\tif not mc.getAttr("{0}.{1}", l=1):\n'.format(node, attr)
                    arg += '\t\t\t\tmc.setAttr("{0}.{1}", {2})\n\n'.format(node, attr, value)

        trans = mc.xform(node, q=1, a=1, t=1)
        rot = mc.xform(node, q=1, a=1, ro=1)
        scale = mc.xform(node, q=1, r=1, s=1)

        arg += '\t\t\tmc.xform("{0}", a=1, t={1})\n'.format(node, trans)
        arg += '\t\t\tmc.xform("{0}", a=1, ro={1})\n'.format(node, rot)
        arg += '\t\t\tmc.xform("{0}", r=1, s={1})\n'.format(node, scale)

    # Store control curve data
    data = controlShapes.get_data()
    data = '\n'.join(['\t\t\t"%s": %s,' % (key, value) for (key, value) in data.items()])
    data = data.replace("'", '"')
    data = '{\n'+data+'\n\t\t}'

    arg += '\n\t\t# Apply contro shapes data\n'
    arg += '\t\tdata = {0}\n\n'.format(data)
    arg += '\t\tcontrolShapes.set_data(data)'.format(data)

    with open(module_path, 'w') as file:
        file.write(arg)
        print 'Saved Assembly as {0} to: {1}'.format(name, module_path)

def new_part(module_path=''):
    """Create a new empty part module."""

    if not os.path.isdir(os.path.dirname(module_path)):
        from rigBot.gui import newPart

        module_path = newPart.get_path()

        if not module_path:
            print 'New assembly cancelled by user.'
            return

    try:
        os.makedirs(os.path.dirname(module_path), 0777)
    except:
        pass

    if not os.path.isdir(os.path.dirname(module_path)):
        mc.warning('Could not create path: '+os.path.dirname(module_path))
        return

    name = os.path.basename(module_path).split('.')[0]
    class_name = name[0].upper()+name[1:]

    # Create new file
    base_path = os.path.join(os.path.dirname(__file__))
    src_file = os.path.join(base_path, 'emptyPart.py')
    shutil.copyfile(src_file, module_path)

    if not os.path.isfile(module_path):
        return

    # Update class namein new file
    lines = []
    with open(module_path, 'r') as pf:
        lines = pf.readlines()

    for i, line in enumerate(lines):
        lines[i] = line.replace('EmptyPart', class_name)

    lines = ''.join(lines)
    with open(module_path, 'w') as f:
        f.write(lines)

    print 'Created new part: {0} {1}'.format(name, module_path)
