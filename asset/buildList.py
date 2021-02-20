# -*- coding: utf-8 -*-
"""This is a standard buildList build script.
    This is the complete build script for asset rigs.
    For now this is only a python script that you can call and run. Eventually
    it will be integrated with the UI to allow a seamless back bacn forth between
    a fully ui based aproach and a fully script based approach.

    Feel free to modify this however you see fit.

    Note:
        This module will be procedurally modified by the buildUI.
        The enabled settings and use plugin options will be affected.

    Usage:
        ``import Bear_buildList``
        ``Bear_buildList.Default.build()``
        ``Bear_buildList.Mocap.build()``"""

import maya.cmds as mc
import maya.mel as mm

from rigBot.asset import standardBuild
from rigBot import env
from rigBot import mod

asset = env.get_asset()

class Default(standardBuild.Default):
    """Class for anim rig build"""

    use_plugin_nodes = True

    build_list = [

        {'label': 'Build Rig From Guides'},

        {'label': 'File new',
         'enabled': True,
         'command': mod.partial('mc.file', new=True, f=True)},

        {'label': 'Load latest guides file',
         'enabled': True,
         'command': mod.partial('guide.load', 'guides')},

        {'label': 'Build skeleton',
         'enabled': True,
         'command': mod.partial('skel.build')},

        {'label': 'Custom code: post_skel',
         'enabled' : True,
         'command': mod.partial(asset+'_custom.Default.post_skel')},

        {'label': 'Build Default rig',
         'enabled': True,
         'command': mod.partial('rig.build')},

        {'label': 'Load custom rigging data',
         'enabled': True,
         'command': mod.partial('data.load', 'customRig')},

        {'label': 'Custom code: post_rig',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Default.post_rig')},

        {'label': 'Load Model'},

        {'label': 'Import model',
         'enabled': True,
         'command': mod.partial('model.load', name='Default', variant='primary', version='HIGHEST', file_type='Alembic Geometry')},

        {'label': 'Custom code: pre_bind',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Default.pre_bind')},

        {'label': 'Load Deformers'},

        {'label': 'Load deformers & data',
         'enabled': True,
         'command': mod.partial('data.load')},

        {'label': 'Custom code: post_bind',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Default.post_bind')},

        {'label': 'Finalize Rig'},

        {'label': 'Connect hooks & create spaces',
         'enabled': True,
         'command': mod.partial('rig.connect_rig')},

        # Enable this if you need to build a mocap blend rig.
        {'label': 'Create HIK mocap blend rig.',
         'enabled': False,
         'command': mod.partial('mocapHIK.create_mocap_blend_rig')},

        {'label': 'Load attribute values and control shapes',
         'enabled': True,
         'command': mod.partial('data.load', data_types=['kAttributes','controlShapes'])},

        {'label': 'Custom code: post_finalize',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Default.post_finalize')},

        {'label': 'Turn off historical importance and set rig display',
         'enabled': True,
         'command': mod.partial('rig.finalize', fx_curves=False, world_locators=False, ram=16, cpu=4)}

    ]

class Anim(standardBuild.Default):
    """Class for anim rig build"""

    use_plugin_nodes = True

    build_list = [

        {'label': 'Build Rig From Guides'},

        {'label': 'File new',
         'enabled': True,
         'command': mod.partial('mc.file', new=True, f=True)},

        {'label': 'Load latest guides file',
         'enabled': True,
         'command': mod.partial('guide.load', 'guides')},

        {'label': 'Build skeleton',
         'enabled': True,
         'command': mod.partial('skel.build')},

        {'label': 'Custom code: post_skel',
         'enabled' : True,
         'command': mod.partial(asset+'_custom.Anim.post_skel')},

        {'label': 'Build Default rig',
         'enabled': True,
         'command': mod.partial('rig.build')},

        {'label': 'Load custom rigging data',
         'enabled': True,
         'command': mod.partial('data.load', 'customRig')},

        {'label': 'Custom code: post_rig',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Anim.post_rig')},

        {'label': 'Load Model'},

        {'label': 'Import model',
         'enabled': True,
         'command': mod.partial('model.load', name='Default', variant='anim', version='HIGHEST', file_type='Alembic Geometry')},

        {'label': 'Custom code: pre_bind',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Anim.pre_bind')},

        {'label': 'Load Deformers'},

        {'label': 'Load deformers & data',
         'enabled': True,
         'command': mod.partial('data.load')},

        {'label': 'Custom code: post_bind',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Anim.post_bind')},

        {'label': 'Finalize Rig'},

        {'label': 'Connect hooks & create spaces',
         'enabled': True,
         'command': mod.partial('rig.connect_rig')},

        # Enable this if you need to build a mocap blend rig.
        {'label': 'Create HIK mocap blend rig.',
         'enabled': False,
         'command': mod.partial('mocapHIK.create_mocap_blend_rig')},

        {'label': 'Load attribute values and control shapes',
         'enabled': True,
         'command': mod.partial('data.load', data_types=['kAttributes','controlShapes'])},

        {'label': 'Custom code: post_finalize',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Anim.post_finalize')},

        {'label': 'Turn off historical importance and set rig display',
         'enabled': True,
         'command': mod.partial('rig.finalize', fx_curves=False, world_locators=False, ram=16, cpu=4)}

    ]

class Export(standardBuild.Default):
    """Class for anim rig build"""

    use_plugin_nodes = True

    build_list = [

        {'label': 'File new',
         'enabled': True,
         'command': mod.partial('mc.file', new=True, f=True)},

        {'label': 'Load latest guides file',
         'enabled': True,
         'command': mod.partial('guide.load', 'guides')},

        {'label': 'Build skeleton',
         'enabled': True,
         'command': mod.partial('skel.build')},

        {'label': 'Custom code: post_skel',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Export.post_skel')},

        {'label': 'Build Export Rig',
         'enabled': True,
         'command': mod.partial('rig.build_mocap_root')},

        {'label': 'Custom code: post_rig',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Export.post_rig')},

        {'label': 'Import model',
         'enabled': True,
         'command': mod.partial('model.load', name='Default', variant='primary', version='HIGHEST', file_type='Alembic Geometry')},

        {'label': 'Custom code: pre_bind',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Export.pre_bind')},

        {'label': 'Load deformers & data',
         'enabled': True,
         'command': mod.partial('data.load', data_types='skinCluster')},

        {'label': 'Custom code: post_bind',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Export.post_bind')},

        {'label': 'Remove unused joints from scene',
         'enabled': True,
         'command': mod.partial('rig.remove_unused_jnts_from_scene')},

        {'label': 'Finalize rig',
         'enabled': True,
         'command': mod.partial('rig.connect_rig')},

        {'label': 'Custom code: post_finalize',
         'enabled': True,
         'command': mod.partial(asset+'_custom.Export.post_finalize')}
    ]

class Mocap(standardBuild.Default):
    """Class for anim rig build"""

    use_plugin_nodes = True

    build_list = [

        {'label': 'File new',
         'enabled': True,
         'command': mod.partial('mc.file', new=True, f=True)},

        {'label': 'Load latest guides file',
         'enabled': True,
         'command': mod.partial('guide.load', 'guides')},

        {'label': 'Build skeleton',
         'enabled': True,
         'command': mod.partial('skel.build')},

        {'label': 'Build Export Rig',
         'enabled': True,
         'command': mod.partial('rig.build_mocap_root')},

        {'label': 'Build Export Rig',
         'enabled': True,
         'command': mod.partial('rig.build_mocap_rig')},

        {'label': 'Import model',
         'enabled': True,
         'command': mod.partial('model.load', name='Default', variant='anim', version='HIGHEST', file_type='Alembic Geometry')},

        {'label': 'Load skinClusters',
         'enabled': True,
         'command': mod.partial('data.load', data_types='skinCluster')},

        {'label': 'Set T-Pose',
         'enabled': True,
         'command': mod.partial('mocapHIK.set_tPose')}
    ]

