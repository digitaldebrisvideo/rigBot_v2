import maya.cmds as mc
import maya.mel as mm
import webbrowser

import getpass
import site
import sys
import os

base_path = os.path.normpath(os.path.dirname(__file__)).replace('\\','/')

def load_plugin(plugin_name, v=True):
    try:
        if mc.pluginInfo(plugin_name, q=1, l=1):
            print '{0} plugin is already loaded!'.format(plugin_name)

        else:
            mc.loadPlugin(plugin_name)
            result = mc.pluginInfo(plugin_name, q=1, p=1)
            if result:
                print 'Loaded {0} plugin: {1}'.format(plugin_name, result)

        return True

    except:
        if v:
            mc.warning('Cannot load {0} plugin! See script editor for details.'.format(plugin_name))
        return False

print '\n rigBot...\n'

# Add plugins dir to maya plugin path
platform = mc.about(os=1)
version = mc.about(v=1)
if mc.about(v=1) == '2016 Extension 2 SP2':
    version = '2016_5'

split_token = ':'
if 'win' in platform:
    split_token = ';'

# set plugin path and load plugins
if not load_plugin('cmRigNodes', v=0):

    plugin_base_path = os.path.join(base_path, 'plugins')
    plugin_path = os.path.join(plugin_base_path, '{0}_{1}'.format(platform, version))
    plugin_path = os.path.abspath(plugin_path)

    all_plugin_paths = os.environ.get('MAYA_PLUG_IN_PATH', '').split(split_token)
    all_plugin_paths.append(plugin_base_path)

    if os.path.isdir(plugin_path):
        if not plugin_path in all_plugin_paths:
            all_plugin_paths.append(plugin_path)

    os.environ['MAYA_PLUG_IN_PATH'] = split_token.join(all_plugin_paths)
    # load_plugin('cmRigNodes')

# Load plugins!
required_plugins = ['quatNodes',
                    'matrixNodes']

for plugin_name in required_plugins:
    load_plugin(plugin_name)

# set up icons path
icon_base_path = os.path.join(base_path, 'icons')
icons_path = os.environ.get('XBMLANGPATH')

if icons_path.endswith('%B'):
    icons_path = icons_path[:-2]

icons_path += '%B'+split_token+icon_base_path+'/'
os.environ['XBMLANGPATH'] = icons_path

# Declare some os variables
if 'RIG_ASSET' not in  os.environ.keys():
    os.environ['RIG_ASSET'] = ''

if 'RIG_VARIANT' not in  os.environ.keys():
    os.environ['RIG_VARIANT'] = ''

if 'RIG_USER' not in os.environ.keys():
    os.environ['RIG_USER'] = getpass.getuser()

if 'use_plugin_nodes' not in  os.environ.keys():
    os.environ['use_plugin_nodes'] = 'True'

if 'cache_build' not in os.environ.keys():
    os.environ['cache_build'] = 'True'

if 'RIG_BUILD_MODE' not in os.environ.keys():
    os.environ['RIG_BUILD_MODE'] = 'sandbox'

# load some mel functions
try:
    import commstd
    logger = commstd.get_logger()
    logger.info(base_path)
except:
    pass

mm.eval('source "createAndAssignShader.mel"')
mm.eval('source "channelBoxCommand.mel"')
mm.eval('source "cleanUpScene.mel"')
mm.eval('source "channelBoxCommand.mel"')
mm.eval('source "{0}/mel/jdsWin.mel"'.format(base_path))

mc.evalDeferred('import maya.cmds as mc')
mc.evalDeferred('import maya.mel as mm')
mc.evalDeferred('import os')
mc.evalDeferred('import sys')
mc.evalDeferred('from rigBot import animMarkingMenu')

# load coonfig and asset env and utils data
print '\n'

from rigBot import utils, control, env
print '\nLoaded  rigBot :)'

def help():
    """Load html help docs for rigBot"""

    path = os.path.join(base_path, 'docs', '_build', 'html', 'index.html')
    if os.path.isfile(path):
        webbrowser.open(path)
    else:
        mc.warning('Cannot find herlp docs! '+path)

def menu(mainwin=None):

    # Create Menu
    try:
        mc.deleteUI('rigToolsMenu')
    except:
        pass

    if not mainwin:
        mm.eval('global string $gMainWindow;')
        mainwin = mm.eval('$tmp = $gMainWindow;')
        menu = mc.menu('rigToolsMenu', l='rigBot 2.0', p=mainwin , to=1)
    else:
        pass

    mc.menuItem(d=1, dl='Build', p=menu)

    mc.menuItem(l='Rig Build UI', p=menu, c="""
from rigBot import utils, guide, skel, rig, data, model
from rigBot.data import skinCluster
from rigBot.gui import main, mayaWidget
main.run()""")

    mc.menuItem(d=1, dl='Rigging Utilities', p=menu)

    mc.menuItem(l='Controls UI', p=menu, c="""
from rigBot.gui import controlUI
self = controlUI.ControlUI()
self.show()""")

    mc.menuItem(l='Clusters UI', p=menu, c="""
from rigBot.gui import clusterUI
clusterUI.run()""")

    mc.menuItem(l='Split Blend Shapes Util', p=menu, c="""
from rigBot.gui import splitTargetsUI
splitTargetsUI.run()""")

    mc.menuItem(l='Set Hand Poses Util', p=menu, c="""
from rigBot.gui import handPoseUI
handPoseUI.run()""")

    mc.menuItem(l='Lighting Locators Util', p=menu, c="""
from rigBot.gui import lightLocsUI
lightLocsUI.run()""")

    mc.menuItem(d=1, dl='Anim Utilities', p=menu)

    mc.menuItem(l='Attach Car Rig To Curve', p=menu, c="""
from rigBot import carOnCurve
carOnCurve.connect()""")

    mc.menuItem(l='Create Camera Rig', p=menu)

    mc.menuItem(d=1, dl='Prop It', p=menu)

    mc.menuItem(l='Rig Prop - CM Node ( Shotgun Model )', p=menu, c="""
from rigBot import propIt
reload(propIt)
propIt.create_from_cmnode()""")

    mc.menuItem(l='Rig prop - Anim Scene ( Non-Shotgun Model )', p=menu, c="""
from rigBot import propIt
reload(propIt)
propIt.create()""")

    mc.menuItem(d=1, dl='Misc', p=menu)

    mc.menuItem(l='Load / Reload shelf', p=menu, c="""
import rigBot
rigBot.shelf()""")

    mc.menuItem(d=1, dl='Help', p=menu)

    mc.menuItem(l='Documentation', p=menu, c="""
import rigBot
rigBot.help()""")

# load comms rigging  shelf
def shelf(*kargs):

    shelfName = 'rigBot'

    if mc.layout(shelfName, q=1, ex=1):
        result = mm.eval('deleteShelfTab "{0}";'.format(shelfName))
        if not result:
            raise RuntimeError('Could not delete {0} shelf!'.format(shelfName))

    # delete off disk
    sfiles = [  os.path.join( mc.internalVar(ush=1).split(':')[-1], 'shelf_{0}.mel'.format(shelfName)),
                os.path.join( mc.internalVar(ush=1).split(':')[-1], 'shelf_{0}.mel.deleted'.format(shelfName))]

    for sfile in sfiles:
        if os.path.isfile(sfile):
            os.remove(sfile)

    path = os.path.normpath(os.path.join(base_path, 'shelf', 'shelf_{0}.mel'.format(shelfName)))
    path = path.replace('\\','/')
    mm.eval('loadNewShelf "{0}"'.format(path))
    mm.eval('saveAllShelves $gShelfTopLevel;')

def edit_prefs():
    prefs_file_path  = os.path.join(mc.internalVar(upd=1), 'rigBot.userPrefs.json')
    utils.edit_file(prefs_file_path)

def reload_prefs(rewrite=False):
    if rewrite:
        prefs_file_path  = os.path.join(mc.internalVar(upd=1), 'rigBot.userPrefs.json')
        os.remove(prefs_file_path)

    env.reload_prefs()

# Load top menu
menu()
