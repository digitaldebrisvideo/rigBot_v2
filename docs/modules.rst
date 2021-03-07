.. rigBot  documentation master file, created by
   sphinx-quickstart on Sun Jul 22 11:04:41 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

************************
Module Documentaiton
************************


Rig Parts
*******************
.. _parts-label:

Available rig parts. These modules are all located under *rigBot.partsLibrary*

bipedArm
===================================
.. automodule:: parts.bipedArm
    :members:
    :show-inheritance:

.. seealso:: For building guides and their respective rigs use :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`

bipedLeg
===================================
.. automodule:: parts.bipedLeg
    :members:
    :show-inheritance:

.. seealso:: For building guides and their respective rigs use :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`

fkChain
===================================
.. automodule:: parts.fkChain
    :members:
    :show-inheritance:

.. seealso:: For building guides and their respective rigs use :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`

foot
===================================
.. automodule:: parts.foot
    :members:
    :show-inheritance:

.. seealso:: For building guides and their respective rigs use :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`

hand
===================================
.. automodule:: parts.hand
    :members:
    :show-inheritance:

.. seealso:: For building guides and their respective rigs use :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`

neck
===================================
.. automodule:: parts.neck
    :members:
    :show-inheritance:

.. seealso:: For building guides and their respective rigs use :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`

piston
===================================
.. automodule:: parts.piston
    :members:
    :show-inheritance:

.. seealso:: For building guides and their respective rigs use :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`

splineChain
===================================
.. automodule:: parts.splineChain
    :members:
    :show-inheritance:

.. seealso:: For building guides and their respective rigs use :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`

tongue
===================================
.. automodule:: parts.tongue
    :members:
    :show-inheritance:

.. seealso:: For building guides and their respective rigs use :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`

torso
===================================
.. automodule:: parts.torso
    :members:
    :show-inheritance:

.. seealso:: For building guides and their respective rigs use :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`

encTorso
===================================
.. automodule:: parts.encTorso
    :members:
    :show-inheritance:

.. seealso:: CAUTION!   All parts with "enc" prefix, uses bipedAutoRig, so please only use for reference.  It's important that you DO NOT use the same exact rig another production :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`

worldRoot
===================================
.. automodule:: parts.worldRoot
    :members:
    :show-inheritance:

.. seealso:: For building guides and their respective rigs use :ref:`guide.build<label-name>`,
    :ref:`skel.build<skel-name>` and
    :ref:`rig.build<rig-name>`


Rig Build Modules
*******************

env
========================
.. _env-label:

Functions for setting and querying asset / variant environment.

.. automodule:: env
    :members:
    :inherited-members:
    :show-inheritance:


guide
========================
.. _label-name:

Functions for building guide rigs, creating new part modules and migrating parts to the asset.

.. automodule:: guide
    :members:
    :inherited-members:
    :show-inheritance:


skel
========================
.. _skel-name:

Functions for building a skeleton.

.. automodule:: skel
    :members:
    :inherited-members:
    :show-inheritance:


rig
========================
.. _rig-name:

Functions for building rigs.

.. automodule:: rig
    :members:
    :inherited-members:
    :show-inheritance:



Asset Specific Modules
***********************

asset.rigAll
============================
.. _rigall-label:

For now this is a master build list to build all rig parts, import your
latest model and load any deformers.
This file lives in the ``${ASSET}//rigbuild`` directory

.. warning:: This will eventually change to allow for better UI introspection.

.. automodule:: asset.rigAll
    :members:
    :inherited-members:
    :show-inheritance:


asset.custom
========================
.. _assetcustom-label:

This is an asset specific custom build script to insert custom code into your build.
This file lives in the ``${ASSET}/rigbuild`` directory.

.. automodule:: asset.custom
    :members:
    :inherited-members:
    :show-inheritance:


Deformers & Data
***********************
.. _data-label:

The data module allows you to save and load data for either a whole asset, which saves
data to the asset's data folder OR you can save and load standalone files.

Scroll down to see what data types are supported.

data
===============================

.. automodule:: data.__init__
    :members:

data.attributes
===============================

.. automodule:: data.attributes
    :members:

data.blendShape
===============================

.. automodule:: data.blendShape
    :members:


data.cluster
===============================

.. automodule:: data.cluster
    :members:

data.connections
===============================

.. automodule:: data.connections
    :members:

data.constraints
===============================

.. automodule:: data.constraints
    :members:

data.controlShapes
==================================
.. _control-shape-label:

.. automodule:: data.controlShapes
    :members:


data.deltaMush
===============================

.. automodule:: data.deltaMush
    :members:


data.lattice
===============================

.. automodule:: data.lattice
    :members:

data.nonLinear
===============================

.. automodule:: data.nonLinear
    :members:

data.pose
===============================

.. automodule:: data.pose
    :members:


data.sculpt
===============================

.. automodule:: data.sculpt
    :members:


data.sdk
===============================

.. automodule:: data.sdk
    :members:

data.skinCluster
===============================

.. automodule:: data.skinCluster
    :members:

data.stack
===============================

.. automodule:: data.stack
    :members:





Utilites & Tools
*******************

utils
========================

Assorted utilies.

.. automodule:: utils
    :members:
    :inherited-members:
    :show-inheritance:


control
========================
.. _control-label:

Functions for creating and modifying animation controls.

.. automodule:: control
    :members:
    :inherited-members:
    :show-inheritance:


ikChain
========================

Functions for working with ik joint chains.

.. automodule:: ikChain
    :members:
    :inherited-members:
    :show-inheritance:


spline
========================

Functions for working with spline setups. (Uses cmRigNodes plugin. Optionally build using vanilla Maya.)

.. automodule:: spline
    :members:
    :inherited-members:
    :show-inheritance:

spaces
========================

Functions for setting up animation control spaces.

.. automodule:: spaces
    :members:
    :inherited-members:
    :show-inheritance:

rivet
========================

Create rivets on poly meshes and nurbs surfaces

.. automodule:: rivet
    :members:
    :inherited-members:
    :show-inheritance:


