.. commsrigging 2 documentation master file, created by
   sphinx-quickstart on Sun Jul 22 11:04:41 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

*********************
Scripted Workflow
*********************


Asset Environment
*******************

The asset environment is a set of os variables that allow your build process to
find the appropriate python files, deformer data and asset info to create your final rig.

Listing available assets
-------------------------

Once set to a project you can list all the available  assets in projoct folder.

.. code-block:: python
   :emphasize-lines: 2

   from rigBot import env
   env.list_assets()


Creating rig asset files
-------------------------

To start the rigging process from scratch you first need to create the appropriate file on disk.


.. code-block:: python
   :emphasize-lines: 2

   from rigBot import env
   env.make_rig_asset('Bob')

.. seealso::
        :ref:`env.make_rig_asset<env-label>`



Setting asset environment
----------------------------------

Setting your asset environment sets your ``sys.path``, and your build directories to import
and save all your build files and data from its proper location on disk.

.. code-block:: python
   :emphasize-lines: 2

   from rigBot import env
   env.set_asset('Bob')

.. seealso::
        :ref:`env.set_asset<env-label>`

Guides & Parts
*******************

Guides are placement rigs used by riggers to position joints in their proper place on a model
and to fit the animation controls around their character. Each part has its own unique set of options
to allow you to vastly customize your rig to meet the needs of your anmators.

.. note:: If you wish to scale the whole guide rig then grab the top node in the outliner, named ``guides`` and scale that. Every guide part should be scalable.

.. seealso:: For more information on part modules see
    :ref:`Rig Parts<parts-label>`




Building guides
-------------------

Build a guide using the
:ref:`guide<label-name>` module.

Build a guide using the default options

.. code-block:: python
   :emphasize-lines: 2

   from rigBot import guide
   guide.build('bipedArm')

Build a guide using specific options just include them as keyword arguments.

.. code-block:: python
   :emphasize-lines: 2

   from rigBot import guide
   guide.build('bipedArm', side='C', name='front', numberTwistJoints=3)

Mirroring guides
------------------
Mirror a guide either from left to right OR right to left. If the new mirrored part does not
exists it will be created, otherwise it will update the existing part.

To mirror you must select any node belonging to the part you wish to mirror.

.. code-block:: python
   :emphasize-lines: 2

   from rigBot import guide
   guide.mirror()


Duplicating guides
--------------------
Duplicating a guide creates an exact copy with the same build options.
You will be prompted to specify a new name for this new part.

.. warning:: At the moment this is a little buggy. It may rename your guides incorrectly so proceed with caution.

To duplicate you must select any node belonging to the part you wish to copy.

.. code-block:: python
   :emphasize-lines: 2

   from rigBot import guide
   guide.duplicate()


Updating guide options
------------------------
Updating options allows you to change build options, rename the part or update the side.

.. note:: There are some build options that are locked once the guide is built. If you try to change those options you will be promted to rebuild the part. Sometimes depending on what new joints or controls are created they may build in odd positions. You will have to position them accordinly.

To change options you must select any node belonging to the part you wish to modify.

.. code-block:: python
   :emphasize-lines: 2

   from rigBot import guide
   guide.update_options(name='myNewName', parent='myNewParent')


Opening & saving guides
------------------------


To open the latest guide

.. code-block:: python
   :emphasize-lines: 2

   from rigBot import guide
   guide.load()

To save the guides file

.. code-block:: python
   :emphasize-lines: 2

   from rigBot import guide
   guide.save()

Assemblies
*******************

Assemblies are simply a template generated from a guides file. It records all parts, build options and positions.

Saving assemblies
--------------------

To save a new assembly. You will be prompted to specify a name.

.. code-block:: python
    :emphasize-lines: 2

    from rigBot import guide
    guide.save_assembly()

Building assemblies
--------------------

To load an assembly to use as a jump off point to build your guide

.. code-block:: python
    :emphasize-lines: 2

    from rigBot import guide
    guide.build_assembly('genericMan')

Building A Skeleton
*********************

A clean skeleton is required for every rig build. This skeleton is used to generate
the anim, mocap and any other rig variant you will be building.

To build a skeleton you must have a guide rig opened.

.. code-block:: python
    :emphasize-lines: 2

    from rigBot import skel
    skel.build()

Building The Anim Rig
**********************

Building the rig
---------------------
You can either build the entire anim rig at once or build each part type
one at a time.

.. code-block:: python

    from rigBot import rig
    rig.build()

Or build each part type one by one

.. code-block:: python
    :emphasize-lines: 2, 3, 4

    from rigBot import rig
    rig.build('worldRoot')
    rig.build('torso')
    rig.build('bipedArm')

Once all parts have been build, the rig needs to be finalize. In this step the
rig hooks are all connected, spaces are created and the rig is cleaned up.

.. code-block:: python

    from rigBot import rig
    rig.finalize()

You can connect hooks and recreate spaces at any time during build by running connect hook command.
This will check hook attribute on all part HOOK nodes and connect them.  If they are already connected to node specified in hook attr, it will skip.
The spaces command works the same way

.. code-block:: python

    from rigBot import rig
    rig.connect_hooks()

Importing the latest model
-------------------------------

To automatically load the latest version of model in rigbuild/model folder

.. code-block:: python

    from rigBot import rig
    rig.import_model()

Deformers & Data
*******************

Load and save deformer data to the asset. By default all data will be saved to your assets
data folder in ``rigbuild/data/${RIG_VARIANT}``

To load data

.. code-block:: python

    from rigBot import data
    data.load()


To save data

.. code-block:: python

    from rigBot import data
    data.save()

.. seealso::
    :ref:`data.load & data.save<data-label>`

Migrating Parts
*******************

You can migrate a part to the asset level. This creates a copy of the part module in the ``asset/rigbuild`` folder that
you can modify to your liking. This newly modified module will only be sourced by the currently set asset.

.. code-block:: python

    from rigBot import guide
    guide.migrate_part()

.. seealso::
    :ref:`guides.migrate_part<label-name>`

Creating New Parts
*******************

You can create new part modules and code them up however you'd like. There are alot of helper functions to create placement joints and create reference controls that you have at your disposal.

To create a new empty part module

.. code-block:: python

    from rigBot import guide
    guide.create_new_part()

.. seealso::
    :ref:`guides.create_new_part<label-name>`

Modifying Control Shapes & Colors
***********************************

In a guide scene all ctrls can be translated, scaled and rotated on a transform level. When the final rig is built, thier transform information gets transferred to the shape node and the ctrl pivots and offsets will be in their appropriate positions .
    Guide controls are only REFERENCE used for shape placement, rotation, scaling and color.

You can always change the shapes and colors of the controls either in the guide stage or after the rig has been built.

Changing control shapes & colors
-----------------------------------

To change control shapes just select one or more controls and run the following

.. code-block:: python

    from rigBot import control
    control.create_shape('square')

To change control colors just select one or more controls and run the following.

.. code-block:: python

    from rigBot import control
    control.set_color('green')

Saving shapes & colors
-------------------------

New shapes and RGB control colors can be saved out to the ``controlData.json`` file

.. note:: Shapes to be saved out should be moved to the origin.

To save shapes select the control

.. code-block:: python

    from rigBot import control
    control.save_shape()

To save an RGB color select the control

.. code-block:: python

    from rigBot import control
    control.save_color()

Available shapes and colors
-----------------------------

To see a list of all available shapes

.. code-block:: python

    from rigBot import control
    control.shapes

To see a list of all available colors

.. code-block:: python

    from rigBot import control
    control.colors

.. seealso::
    :ref:`control<control-label>` and
    :ref:`data.controlShapes<control-shape-label>`

Modifying rigAll.py
*********************

The ``${RIG_ASSET}_rigAll.py`` is your complete build list for your rig or rig variant.
The following is a list of the standard operations run during a build.

This file is created for each asset when the ``env.make_rig_asset`` function is called.
If you wish to modify this file. It lives in ``${RIG_ASSET}/rigbuild`` folder.
You will rarely need to modify this.

the ``${RIG_ASSET}_custom.py`` file already has empty slots for your custom code.

.. warning:: At the moment this file is a simple python file. Would like to allow for UI introspection in future.

Rig All build operations:

- Load the latest guide file
- Build skeleton
- Run asset.custom.post_skel code (custom adjustments needed AFTER skel build, but BEFORE the anim rig is built)
- Build the rig
- Run asset.custom.post_rig code
- Load the latest versioned model
- Run asset.custom.pre_bind code(for custom adjustments needed AFTER model is imported, but BEFORE deformations are imported)
- Load deformers and other data
- Run asset.custom.post_bind code
- Connect hooks
- Create spaces
- Run asset.custom.post_finalize code(for custom adjustments before rig is finalized

.. seealso::
    :ref:`asset_rigALL<rigall-label>` and
    :ref:`asset_rigALL<assetcustom-label>`
