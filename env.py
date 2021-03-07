import datetime
import subprocess
import shutil
import getpass
import json
import stat
import sys
import os
import re

import maya.cmds as mc
import maya.mel as mm

# Try loading shotgun and commstd pipeline tools
# try:
#     from commstd import pipeline
#     import commstd
#     import sgtk
# 
#     # Create tk instance
#     if sgtk.platform.current_engine() == None:
#         commstd.start_engine()
# 
#     tk = sgtk.platform.current_engine().sgtk
#     shotgun = commstd.current_engine().shotgun
#     project = os.environ.get('PL_DIVISION') or ''

# except:
pipeline = None
commstd = None
shotgun = None
sgtk = None
tk = None

    # mc.warning('Shotgun & commstd is not available in this envrionment!')

# set initial empty vars
try:
    prefs_file_path = ''
    prefs_file_path = os.path.join(mc.internalVar(upd=1), 'rigBot.userPrefs.json')

except:
    pass

rigbuild_var_path = ''
sandbox_var_path = ''
using_sandbox = False
all_assets = []
prefs = {}


def set_build_mode(mode='sandbox'):
    if mode == 'sandbox':
        os.environ['RIG_BUILD_MODE'] = 'sandbox'
    else:
        os.environ['RIG_BUILD_MODE'] = 'forceLive'


def reload_prefs(verbose=True):
    """Reload user setup json config file"""

    global prefs
    global rigbuild_var_path
    global sandbox_var_path

    # Declare os variables
    if 'RIG_ASSET' not in os.environ.keys():
        os.environ['RIG_ASSET'] = ''
        print 'Adding variable to os.environ: RIG_ASSET'

    if 'RIG_VARIANT' not in os.environ.keys():
        os.environ['RIG_VARIANT'] = ''
        print 'Adding variable to os.environ: RIG_VARIANT'

    defaults = {
        "USE_PLUGIN_FOR_GUIDES": False,
        "CACHE_RIG_BUILD": True,
        "CURRENT_PROJECT": "",
        "RIGBUILD_VAR_PATH": "C:/Users/${RIG_USER}/Documents/maya/projects/${PL_DIVISION}",
        "PARTS_VAR_PATH": [
            "/job/${PL_SHOW}/${PL_DIVISION}/sandbox/${RIG_USER}/common/maya/2017.p5/python/Rigbuild_Library",
            "/job/${PL_SHOW}/${PL_DIVISION}/common/maya/2017.p5/python/Rigbuild_Library",
            "C:/Users/${RIG_USER}/Documents/maya/2020/scripts/rigBot"]
    }


    if not os.path.isfile(prefs_file_path):
        with open(prefs_file_path, 'w') as f:
            if prefs:
                json.dump(prefs, f, indent=4, sort_keys=True)
            else:
                json.dump(defaults, f, indent=4, sort_keys=True)
                prefs = dict(defaults)

            if verbose:
                print 'Created userPrefs file: ' + prefs_file_path

        change_permission(prefs_file_path)

    else:
        with open(prefs_file_path, 'r') as f:
            prefs = json.load(f)
            if verbose:
                print 'Loaded userPrefs: ' + prefs_file_path

    if not shotgun:
        set_project(prefs.get('CURRENT_PROJECT') or '')

    rigbuild_var_path = prefs.get('RIGBUILD_VAR_PATH') or ''
    sandbox_var_path = prefs.get('RIGBUILD_SANDBOX_VAR_PATH') or ''
    rigbuild_var_path = rigbuild_var_path.replace('\\', '/')
    sandbox_var_path = sandbox_var_path.replace('\\', '/')

    if prefs:
        for k, v in defaults.items():
            if k not in prefs.keys():
                prefs[k] = v
    return prefs


def use_plugin():
    if os.environ['use_plugin_nodes'] == 'True':
        result = False
    else:
        result = False

    if not mc.pluginInfo('cmRigNodes', q=1, l=1):
        result = False

    return False


def use_plugin_for_guides():
    result = prefs.get('USE_PLUGIN_FOR_GUIDES', True)

    if not mc.pluginInfo('cmRigNodes', q=1, l=1):
        result = False

    return False


def edit_prefs():
    """Edit user prefs file in text editor"""

    global prefs
    edit_file(prefs_file_path)


def set_project(new_project=''):
    """If not using shotgun you may change the project and rely on files on disk."""

    global project
    global prefs

    if shotgun:
        mc.warning('Using shotgun, cannot change project!')
        return

    project = new_project
    os.environ['PL_DIVISION'] = project
    prefs['CURRENT_PROJECT'] = project

    try:
        if os.path.isfile(prefs_file_path):
            os.remove(prefs_file_path)

        with open(prefs_file_path, 'w') as f:
            json.dump(prefs, f, indent=4, sort_keys=True)
        change_permission(prefs_file_path)

    except:
        mc.warning('Do not have permissions to write to: ' + prefs_file_path)

    list_assets(verbose=False)
    set_asset(clear=True)

    print '# Set PROJECT to ' + project


def list_projects(verbose=True):
    """If NOT in a shotgun environment, list all project directories on disk."""

    # if shotgun:
    #     mc.warning('This function is not available in a shotgun environmen!')
    #     return []

    path = prefs.get('RIGBUILD_VAR_PATH') or ''
    path = path.split('${PL_DIVISION}')[0]
    path = os.path.expandvars(path)
    path = os.path.normpath(path)

    all_projects = []
    if os.path.isdir(path):
        all_projects = [str(d) for d in os.listdir(path) if '.' not in d]

    all_projects.sort()
    if verbose:
        print all_projects

    return all_projects


def list_assets(verbose=True):
    """List assets from Shotgun for current project"""

    global all_assets

    # if shotgun:
    #     assets_from_shotgun = tk.shotgun.find('Asset', [['project.Project.name', 'is', project]], ['code']) or []
    #     all_assets = [a['code'] for a in assets_from_shotgun]

    # else:
    asset_path = prefs.get('RIGBUILD_VAR_PATH') or ''
    asset_path = asset_path.split('${RIG_ASSET}')[0].replace('${PL_DIVISION}', project)
    asset_path = os.path.expandvars(asset_path)
    asset_path = os.path.normpath(asset_path)

    assets = []
    if os.path.isdir(asset_path):
        all_assets = [str(d) for d in os.listdir(asset_path) if '.' not in d]
        all_assets = [d for d in all_assets if os.path.isdir(os.path.join(asset_path, d))]

    all_assets.sort()
    if verbose:
        print all_assets

    return all_assets


def get_asset():
    """Get the current asset from os.environ. Uses config variable name: JOB_VAR"""

    return os.environ.get('RIG_ASSET')


def set_asset(asset='', clear=False, verbose=True):
    """Set rig asset (Must be a valid shotgun asset)"""

    if clear or not project:
        os.environ['RIG_ASSET'] = ''
        os.environ['RIG_VARIANT'] = ''

        set_rigbuild_paths(clear=True, verbose=verbose)
        print 'Set asset to None.'

    elif __check_asset_validity(asset):
        os.environ['RIG_ASSET'] = asset
        os.environ['RIG_VARIANT'] = ''

        # set variant
        variants = list_variants(verbose=verbose)
        if variants:
            if 'default' in variants:
                set_variant('default', verbose=verbose)
            else:
                set_variant(variants[0], verbose=verbose)

        # set asset paths
        set_rigbuild_paths(verbose=verbose)

        # set shotgun context
        context_path = get_rigbuild_path(asset)
        # commstd.change_context(context_path)

        if not shotgun:
            workspace_path = os.path.dirname(context_path)
            workspace_file = os.path.join(workspace_path, 'workspace.mel')
            create_workspace_file(workspace_file)

            mm.eval('setProject "{0}"'.format(workspace_path))

        if verbose:
            print 'Set asset to %s.' % asset

        return True

    else:
        print list_assets(verbose=1)


def get_rigbuild_path(asset=None, verbose=False, live=False):
    """Get asset rigbuild path"""

    using_sandbox=False

    if asset is None:
        try:
            asset = get_asset()
        except:
            pass

    if not asset:
        return ''

    asset_path = rigbuild_var_path.replace('${RIG_ASSET}', asset).replace('\\', '/')
    sandbox_path = sandbox_var_path.replace('${RIG_ASSET}', asset).replace('\\', '/')

    asset_path = os.path.expandvars(asset_path)
    sandbox_path = os.path.expandvars(sandbox_path)

    if not live:
        using_sandbox = False

    if os.environ.get('RIG_BUILD_MODE') == 'sandbox' and not live:
        if os.path.isdir(asset_path) and not os.access(asset_path, os.W_OK):
            if os.path.isdir(sandbox_path):
                asset_path = sandbox_path
                using_sandbox = False

    if not asset_path or not asset:
        asset_path = ''

    return asset_path


def get_inherited_paths(asset=None, verbose=False):
    """Get a list of all the paths to be inherited from asset info file."""

    if asset is None:
        asset = get_asset()

    if not __check_asset_validity(asset):
        return []

    data = get_asset_info(asset, verbose=verbose)

    if not data:
        return []

    inherited_paths = []
    inherit_data = data.get('inherit_from')

    if inherit_data:
        for iData in inherit_data:
            inherited_paths.append(str(iData.get('rigbuild_path')))

    return [p for p in inherited_paths]


def set_rigbuild_paths(clear=False, verbose=True):
    """Set sys path to include rig build path for asset"""

    if 'CM_TEMP_SYS_PATH' not in os.environ.keys():
        os.environ['CM_TEMP_SYS_PATH'] = ''

    # reset sys.path
    new_sys_path = []
    stored_paths = [os.path.normpath(p)
                    for p in os.environ['CM_TEMP_SYS_PATH'].split('%')]

    for path in sys.path:
        if os.path.normpath(path) not in stored_paths:
            new_sys_path.append(path)

    sys.path = new_sys_path

    if clear:
        return

    live = get_rigbuild_path(live=1)
    sand = get_rigbuild_path()

    if live == sand:
        paths = [sand]

    else:
        paths = [live, sand]
        paths.extend(get_inherited_paths())

    # add paths to sys path and store in temp path variable
    for path in paths:
        if path in sys.path:
            sys.path.remove(path)
        sys.path.insert(0, path)

    if verbose:
        for path in reversed(paths):
            print 'Inserted to sys.path: ' + path

    stored_paths.extend(paths)
    stored_paths = list(set(stored_paths))
    os.environ['CM_TEMP_SYS_PATH'] = '%'.join(stored_paths)

    return True


def add_inheritance(inherit_from=None,
                    inherit_guide=True,
                    inherit_path=True,
                    inherit_model=False,
                    overwrite=False,
                    remove_all=False):
    """Add asset inheritance, for guides

    ARGS:
        asset = Current asset to add inheritance
        inherit_from = asset to inherit from (must be on same job)
        inherit_guide = inherit guides file
        inherit_path = inherit python import paths
        inherit_model = inherit model
    """

    asset = get_asset()

    if not remove_all and not __check_asset_validity(inherit_from):
        mc.warning('No valid asset specifed for inherit!')
        return

    data = get_asset_info(asset)

    if not data:
        mc.warning('Asset Info does not exist!')
        return

    if remove_all:
        update_asset_info(inherit_from=None)
        return

    iData = {
        'asset': inherit_from,
        'rigbuild_path': get_rigbuild_path(inherit_from),
        'inherit_guide': inherit_guide,
        'inherit_model': inherit_model,
        'inherit_path': inherit_path
    }
    inherit_data = data.get('inherit_from') or []

    if overwrite:
        inherit_data = []

    inherit_data.append(iData)

    update_asset_info(inherit_from=inherit_data)


def set_user(user=None):
    if not user:
        user = getpass.getuser()

    os.environ['RIG_USER'] = user
    print 'Set sandbox usaer to: ' + user
    return user


def get_user():
    if not os.environ.get('RIG_USER'):
        set_user()

    return os.environ.get('RIG_USER')


def update_asset_info(**kwargs):
    """Create / update asset info json file."""

    asset = get_asset()

    if not __check_asset_validity(asset):
        return

    rigbuild_path = get_rigbuild_path(asset)

    if not os.path.isdir(rigbuild_path):
        mc.warning('Dir does not exist: ' + rigbuild_path)

    info_file = os.path.join(rigbuild_path, 'assetInfo.json')
    current_date = datetime.datetime.now()
    current_date = current_date.ctime().replace('  ', ' ')
    msg = 'Created Asset info file: '

    data = {
        'created_by': getpass.getuser(),
        'last_modified_by': getpass.getuser(),
        'date_created': current_date,
        'date_modified': current_date,
        'inherit_from': None,
        'primary_variant': None,
        'models': None,
        'using_assembly': None,
        'parts': None,
        'rig_variants': None,
        'enabled_build_steps': None,
        'asset_type': 'char',
        'guide_parts': []
    }

    if os.path.isfile(info_file):
        with open(info_file, 'r') as f:
            data.update(json.load(f))

        msg = 'Updated Asset info file: '

    if kwargs:
        data.update(kwargs)

    data['date_modified'] = current_date
    data['last_modified_by'] = getpass.getuser()

    if os.path.isdir(rigbuild_path):
        try:
            with open(info_file, 'w') as f:
                json.dump(data, f, indent=4, sort_keys=True)
            change_permission(info_file)
            print msg + info_file

        except:
            pass
    else:
        print 'Dir does not exist' + rigbuild_path


def list_variants(verbose=False):
    """List all rig types for current asset"""

    asset = get_asset()
    if not asset:
        return

    info = get_asset_info(verbose=verbose)
    if not info:
        if verbose:
            mc.warning('Asset Info does not exist!')
        return

    rig_variants = info.get('rig_variants') or []

    if verbose:
        print '\n# EXISTING RIG VARIANTS:'
        for variant in rig_variants:
            print '  ' + variant

        print '\n'

    return rig_variants


def add_variant(variant, set_primary=False):
    """Create a new rigType for current asset"""

    def add_variant_class_to_build_files(variant, src_class='Default'):

        """This add the classes to the buildList and custom .py files"""

        # get files source and target
        variant_class = variant[0].upper() + variant[1:]
        system_path = os.path.dirname(__file__)

        src_file = os.path.join(system_path, 'asset', 'buildList.py')
        bl_path = os.path.join(get_rigbuild_path(), get_asset() + '_buildList.py')

        if os.path.isfile(bl_path):
            # read lines from source
            with open(src_file) as f:
                lines = f.readlines()

            # extract the class to clone
            class_lines = []
            for i, line in enumerate(lines):
                if 'class ' + src_class in line:
                    class_lines = lines[i:]
                    break

            for i, line in enumerate(class_lines[1:]):
                if 'class ' in line:
                    class_lines = class_lines[:i]
                    break

            class_lines = [c.replace('custom.' + src_class, 'custom.' + variant_class, 1) for c in class_lines]
            class_lines[0] = re.sub(' +', ' ', class_lines[0])
            class_lines[0] = class_lines[0].replace('class ' + src_class, 'class ' + variant_class)

            # get all current lines in target module
            with open(bl_path) as f:
                bl_lines = f.readlines()

            # check to see if that new class already exists, if not write it
            do_write_it = True
            for i, bl_line in enumerate(bl_lines):
                if 'class ' + variant_class in re.sub(' +', ' ', bl_line):
                    do_write_it = False

            # join lines and write to file
            if do_write_it:
                all_lines = ''.join(bl_lines + ['\n'] + class_lines)
                with open(bl_path, 'w') as f:
                    f.write(all_lines)
                    print 'Added {0} class to: {1}'.format(variant_class, bl_path)

        # now do the same thing for the custom file
        c_path = os.path.join(get_rigbuild_path(), get_asset() + '_custom.py')
        if os.path.isfile(c_path):
            # read lines from source
            with open(c_path) as f:
                lines = f.readlines()

            class_lines = ['class {0}(Default):\n'.format(variant_class),
                           '    """Class for {0} rig build. Inherits Default class."""\n'.format(variant_class),
                           '    pass\n']

            do_write_it = True
            for i, line in enumerate(lines):
                if 'class ' + variant_class in re.sub(' +', ' ', line):
                    do_write_it = False

            if do_write_it:
                all_lines = ''.join(lines + ['\n'] + class_lines)
                with open(c_path, 'w') as f:
                    f.write(all_lines)
                    print 'Added {0} class to: {1}'.format(variant_class, c_path)

    asset = get_asset()
    if not __check_asset_validity(asset):
        return

    info = get_asset_info()
    if not info:
        mc.warning('Asset Info does not exist!')
        return

    rig_variants = info.get('rig_variants') or []
    primary_variant = info.get('primary_variant')

    if type(rig_variants) is list:
        rig_variants.append(variant)

    else:
        rig_variants = [variant]

    if set_primary:
        primary_variant = variant

    rig_variants = list(set(rig_variants))
    rig_variants.sort()

    update_asset_info(rig_variants=rig_variants, primary_variant=primary_variant)
    add_variant_class_to_build_files(variant)
    set_variant(variant)

    return True


def get_variant():
    """Get  current rig type for current asset"""

    return os.environ.get('RIG_VARIANT')


def set_variant(variant=None, clear=False, verbose=True):
    """Set variant for current asset"""

    asset = get_asset()
    if not __check_asset_validity(asset):
        return

    rig_variants = list_variants()

    if not rig_variants:
        return

    if clear:
        os.environ['RIG_VARIANT'] = ''
        if verbose:
            print 'Set variant to None'
        return

    if not variant:
        if verbose:
            mc.warning('Variant not set!')
        return

    if variant not in rig_variants:
        list_variants(verbose=True)
        mc.warning('%s is not a valid variant!' % variant)
        return

    if variant == get_variant():
        return True

    os.environ['RIG_VARIANT'] = variant
    if verbose:
        print 'Set variant to ' + variant
    return True


def check_if_asset_exists(name):
    """Checks if an asset is already an existing rigBot asset."""

    if not project:
        mc.warning('Job not set! Cannot continue.')
        return

    if not __check_asset_validity(name):
        mc.warning('This is not a valid shotgun asset, cannot make files.')
        return

    rigbuild_path = get_rigbuild_path(asset=name)
    file_check = os.path.join(rigbuild_path, 'assetInfo.json')

    return os.path.isfile(file_check)


def make_rig_asset(name='', variants=['default'], primary_variant='default', force=False):
    """Make a new asset on the job, create build directories and
        migrate custom.py file to asset dir."""

    if not name:
        name = get_asset()
        if not name:
            mc.warning('Asset not set or specified! Cannot continue.')
            return

    if not project:
        mc.warning('Job not set! Cannot continue.')
        return


    if not force and check_if_asset_exists(name):
        mc.warning('{0} is already an existing rigBot asset.'.format(name))
        return


    rigbuild_path = get_rigbuild_path(asset=name)

    if not os.path.isdir(rigbuild_path):
        if shotgun:
            try:
                commstd.change_context(rigbuild_path)
                context = tk.context_from_path(rigbuild_path)

                result = shotgun.find_one("Task", [["entity", "is", context.entity], ["content", "is", "rig"]], [])
                task_id = result.get('id')

                if not task_id:
                    mc.warning('Rig task does not seem to exist. Check shotgun.')
                    return

                tk.create_filesystem_structure("Task", task_id, "tk-maya")
                commstd.change_context(rigbuild_path)
                context = commstd.current_context()

                if not os.path.isdir(rigbuild_path):
                    raise IOError(
                        'Could not create rig task system directory on disk!')

            except:
                try:
                    make_dirs(rigbuild_path)
                except:
                    raise IOError('Cannot create directory on disk:' + rigbuild_path)
        else:
            try:
                make_dirs(rigbuild_path)
            except:
                raise IOError('Cannot create directory on disk:' + rigbuild_path)

    set_asset(name)
    update_asset_info()

    # create data dir IF it doesnt exist
    dPath = os.path.join(rigbuild_path, 'data')
    make_dirs(dPath)

    init_file = os.path.join(dPath, '__init__.py')
    with open(init_file, 'w') as f:
        f.write('')

    if not shotgun:
        b = os.path.dirname(rigbuild_path)
        base= os.path.join (b, name )
        dirs = ['guides', 'rig', 'work', 'model']
        dirs = [os.path.join(base, d) for d in dirs]
        make_dirs(dirs)

    # add variants
    for variant in variants:
        add_variant(variant)

    if primary_variant in variants:
        add_variant(primary_variant, set_primary=True)

    # copy custom build script
    system_path = os.path.dirname(__file__)

    src_file = os.path.join(system_path, 'asset', 'custom.py')
    migrate_file(src_file, add_asset_prefix=True, edit=False, verbose=True)

    src_file = os.path.join(system_path, 'asset', 'buildList.py')
    migrate_file(src_file, add_asset_prefix=True, edit=False, verbose=True)


def get_asset_info(asset=None, verbose=True):
    """Get asset info data as dict."""

    if asset is None:
        asset = get_asset()

    if not __check_asset_validity(asset):
        return

    rigbuild_path = get_rigbuild_path(asset)
    info_file = os.path.join(rigbuild_path, 'assetInfo.json')

    if os.path.isfile(info_file):
        with open(info_file, 'r') as f:
            return json.load(f)
    else:
        if verbose:
            print 'No asset info for: ' + asset


def migrate_file(src_file, dst_file=None, add_asset_prefix=False, force=False, edit=True, verbose=True):
    """Migrate a file to current asset."""

    dst_path = get_rigbuild_path()

    if not dst_file and not dst_path:
        return

    if not os.path.isfile(src_file):
        src_file = src_file
        mc.warning('# File doesn\'t exist! :' + src_file)
        return

    src_fileName = os.path.basename(src_file)
    if add_asset_prefix:
        asset = get_asset()
        src_fileName = asset + '_' + src_fileName

    if dst_file is None:
        dst_file = os.path.join(dst_path, src_fileName)

    if os.path.exists(dst_file) and not force:
        if verbose:
            mc.warning('# File already exists! Use force=True argument to overwrite.')
        return

    if not os.path.normpath(src_file) == os.path.normpath(dst_file):
        shutil.copyfile(src_file, dst_file)
        change_permission(dst_file)

        print '# Migrated file from: ' + src_file
        print '# Migrated file to: ' + dst_file

        if edit:
            edit_file(dst_file)

        return dst_file


def edit_file(file_path):
    """Open the specified file in system text editor."""

    editor = prefs.get('code_editor_cmd')
    file_path = file_path

    if not os.path.isfile(file_path):
        mc.warning('File does not exist: ' + file_path)
        return

    try:
        os.startfile(file_path)
        print 'Opening file: ' + file_path
    except:
        webbrowser.open(file_path)
        print 'Opening file: ' + file_path


def update_stream(scene_file=''):
    """Update to latest workfile from a given versioned file path"""

    if not scene_file:
        scene_file = mc.file(q=1, loc=1)

    context = tk.context_from_path(scene_file)
    sgtk.platform.change_context(context)

    stream = scene_file.split("_")[-2]
    animators_saved_scene = commstd.open_workfile(stream, "LATEST")


def save_stream(stream, token='', version='NEXT', workfile=1):
    """Save a rig stream to a particular asset"""

    asset = get_asset()

    if not asset:
        mc.warning('Asset not set!')
        return

    if shotgun:
        try:
            context_path = get_rigbuild_path(asset, live=1)
            commstd.change_context(context_path)
            path = commstd.save_workfile(stream, version)

            print 'Saved workfile: ' + path
        except:
            mc.ShotgunSaveAs()

    else:
        stream = stream[0].lower() + stream[1:]
        if token:
            token = token[0].lower() + token[1:]
        return save_new_versioned_file(stream=token, variant=stream, workfile=workfile)


def open_stream(stream, version='LATEST', workfile=1, token=''):
    """Open a saved stream worfile from shotgun"""

    asset = get_asset()

    if not asset:
        mc.warning('Asset not set!')
        return

    if shotgun:
        context_path = get_rigbuild_path(asset, live=1)
        commstd.change_context(context_path)
        path = commstd.open_workfile(stream, version)

    else:
        stream = stream[0].lower() + stream[1:]
        if token:
            token = token[0].lower() + token[1:]
        path = get_versioned_file(stream=token, variant=stream, version=version, workfile=workfile)
        mc.file(path, f=1, o=1)

    print 'Opened workfile: ' + path

    return path


def import_stream(stream, version='LATEST', workfile=1, new_file=False, token='', asset=None):
    """Import a saved stream worfile from shotgun"""

    if not asset:
        asset = get_asset()

    if not asset:
        mc.warning('Asset not set!')
        return

    if shotgun:

        context_path = get_rigbuild_path(asset, live=1)
        commstd.change_context(context_path)

        try:
            if version == 'LATEST':
                version = commstd.workfile_versions(stream)[-1]

        except:
            mc.warning('No file versions found!')
            return

        path = commstd.workfile_path(stream, version)

    else:
        stream = stream[0].lower() + stream[1:]
        if token:
            token = token[0].lower() + token[1:]
        path = get_versioned_file(stream=token, variant=stream, version=version, workfile=workfile)

    if os.path.isfile(path):
        try:
            if new_file:
                mc.file(new=1, f=1)

            result = mc.file(path, i=1, rnn=1, pmt=0, iv=1)
            mc.select(result)

            print 'Imported workfile: ' + path
            return path

        except:
            mc.warning('Failed to import: ' + file_path)


def import_published_file(task='model', asset=None, name='default', variant='primary', file_type='Maya Geometry',
                          version=None):
    """Import shotgun published file, rig or model."""

    if not asset:
        asset = get_asset()

    if not asset:
        mc.warning('Asset not set!')
        return

    if shotgun:
        context_path = get_rigbuild_path(asset, live=1)
        commstd.change_context(context_path)

        pf_context = pipeline.create_context(entity_type="Asset", entity=asset, task=task)

        if version:
            pf = pipeline.find_one_pf(pf_context, file_type, name + ' ' + asset, version_number=version)
        else:
            pf = pipeline.find_one_pf(pf_context, file_type, name + ' ' + asset)

        variants = pipeline.find_alternatives(pf, vary_variant=True) or []
        pf_variant = None

        if variants:
            for v in variants:
                if v.get('sg_variant') == variant:
                    pf_variant = v

        if pf_variant:
            path = pf_variant.get('path').get('local_path_linux')

    else:
        path = get_versioned_file(asset=asset, stream=task, variant=variant, version=version, workfile=0)

    try:
        result = mc.file(path, i=1, rnn=1, pmt=0, iv=1)
        mc.select(result)

        print 'Imported published file: ' + path
        return path

    except:
        mc.warning('Failed to import: ' + path)


def import_published_guides(asset=None, version=None):
    if not asset:
        asset = get_asset()

    if not asset:
        mc.warning('Asset not set!')
        return

    context_path = get_rigbuild_path(asset, live=1)
    commstd.change_context(context_path)

    pf_context = pipeline.create_context(entity_type="Asset", entity=asset, task='rig')
    pf = pipeline.find_one_pf(pf_context, 'Maya Workfile', 'guides')

    if type(version) == int:
        pf = pipeline.find_one_pf(pf_context, 'Maya Workfile', 'guides', version_number=version)
    else:
        pf = pipeline.find_one_pf(pf_context, 'Maya Workfile', 'guides')

    path = pf.get('path').get('local_path_linux')

    try:
        result = mc.file(path, i=1, rnn=1, pmt=0, iv=1)
        mc.select(result)
        print 'Imported published file: ' + path
        return path

    except:
        mc.warning('Failed to import: ' + path)


def make_dirs(paths):
    """Make dirs on disk"""

    if type(paths) is not list:
        paths = [paths]

    for p in paths:
        if not os.path.isdir(p):
            try:
                os.makedirs(p, 0777)
                print 'Created dir: ' + p
            except:
                mc.warning('Could not create path: ' + p)


def change_permission(path, permission_code=777):
    """Change permissions on already created folders - you'll need permissions first of course"""

    if sys.platform == 'win32':
        return

    FILE_PERMISSIONS = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH
    os.chmod(path, FILE_PERMISSIONS)

    '''
    old_umask = os.umask(000)
    os.chmod(path, permission_code)
    os.umask(old_umask)
    old_umask = os.umask(000)
    os.chmod(path, permission_code)
    os.umask(old_umask)
    '''


def __check_asset_validity(asset):
    """Check if the specified asset is valid on this job"""

    if shotgun:
        if asset and asset in all_assets:
            return True

    else:
        return True


def save_new_versioned_file(path=None, asset=None, stream='', variant='rig', ext='ma', workfile=0):
    """This is for saving new versioned maya files ."""

    if not path:
        print workfile
        # base_path = os.path.dirname(get_rigbuild_path())
        base_path = get_rigbuild_path()

        if workfile:
            path = os.path.join(base_path, 'work')

        else:
            path = os.path.join(base_path, variant)

    if not asset:
        asset = get_asset()

    if not os.path.isdir(path):
        make_dirs(path)

    files = [f for f in os.listdir(path) if re.search(variant + '_v[0-9][0-9][0-9].' + ext, f)]
    files.sort()

    if files:
        high_version = int(files[-1].split('.' + ext)[0][-3:])
        new_version = high_version + 1
    else:
        new_version = 1

    v = str(new_version).zfill(3)

    if stream:
        stream += '_'

    newname = asset + '_' + stream + variant + '_v' + v + '.' + ext
    newname = newname.replace('__', '_')
    filename = os.path.normpath(os.path.join(path, newname)).replace('\\', '/')

    # clean the scenee
    mm.eval('source "cleanUpScene.mel";')
    mm.eval('deleteUnknownNodes();')

    # save it
    file_type = 'mayaAscii'
    if ext == 'mb':
        file_type = 'mayaBinary'

    mc.file(filename, options='v=0', type=file_type, pr=1, ea=1, f=1)
    print 'Saved file: ' + filename

    return filename


def get_versioned_file(path=None, asset=None, stream='', variant='rig', ext='ma', workfile=0, version='HIGHEST'):

    if not path:
        # base_path = os.path.dirname(get_rigbuild_path())
        base_path = get_rigbuild_path()
        path = os.path.join(base_path, variant)
        if workfile:
            path = os.path.join(base_path, 'work')

    if not asset:
        asset = get_asset()

    if stream:
        stream += '_'

    files = [f for f in os.listdir(path) if re.search(stream + variant + '_v[0-9][0-9][0-9].' + ext, f)]
    files.sort()

    if not files:
        mc.warning('Cannot find file!')
        return ''

    if type(version) == int:
        version = version - 1

    else:
        version = -1

    filename = os.path.join(path, files[version]).replace('\\', '/')
    return filename


def create_workspace_file(workspace_file):
    arg = """//Maya Project Definition

workspace -fr "clips" "rig";
workspace -fr "scene" "rigbuild";
workspace -fr "images" "work";
workspace -fr "renderData" "model";
workspace -fr "sourceImages" "guides";"""

    if not os.path.isdir(os.path.dirname(workspace_file)):
        return

    if not os.path.isfile(workspace_file):
        with open(workspace_file, 'w') as f:
            f.write(arg)
            print 'Created workspace file: ' + workspace_file





def get_parts_paths():
    paths = prefs.get('PARTS_VAR_PATH') or []

    if not type(paths) == list:
        paths = [paths]

    paths.append(os.path.join(os.path.dirname(__file__), 'partsLibrary'))
    paths.insert(0, get_rigbuild_path())
    paths = [str(os.path.expandvars(p).replace('\\', '/')) for p in paths]

    clean_list = []
    for p in paths:
        if os.path.isdir(p) and p not in clean_list:
            clean_list.append(p)

    return clean_list


# initialize all assets on job
try:
    reload_prefs(verbose=0)
except:
    pass

try:
    list_assets(verbose=0)
except:
    pass

try:
    get_rigbuild_path()
except:
    pass
