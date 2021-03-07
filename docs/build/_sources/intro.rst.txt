.. rigBot 2 documentation master file, created by
   sphinx-quickstart on Sun Jul 22 11:04:41 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

***********************
Loading rigBot2
***********************

To launch the rigBot data toolset, run the following command

.. code-block:: python

   import sys
   p = r'/path/to/package/file'
   if p not in sys.path:
       sys.path.insert(0, p)
   import rigBot
   reload (rigBot)

Once the package imports a menu item named "rigBot"

From here you can access all the UIs and this documentation.

*********************
Key Concepts
*********************

:Asset Environment: The asset environment is a set of of variables that define the current asset and rig variant you are currently
    working on. Setting your asset also modifes your python sys path to include the asset's rigbuild folder, along with any inherited asset paths you may have specified.

:Rig Build Folder: Folder on disk specific to the asset on a particular job. All asset related data and custom files lives in
    this folder.

:Rig Variant: Rigs that are for the same asset, but have a different function.  Examples are animation rig, a mocap rig or any rig that is a one off or special case.
    Users can easily swap the between these rigs in a scene at any given time.

:Parts: A python module for a specific type of rig. ie. bipedArm, quadLeg, torso, hand foot.
    This module defines options for the part and contains all the build code for the guide and the anim rig.

:Part Options: Each part module has it's own specifc set of customizable options. These options determine the things like the
    parenting of your rig, number of joints, control behaivor, etc. Example options include: side tokens, naming prefix, parent, number twist joints.

:Guide: A placement rig that is built by a part module that is used to set rig paramters, layout joint positions and orientations as
    well as customizing rig control shapes and fitting them to your character. Each guide is its own stand alone "mini rig".

:Assembly: Assemblies are simply a template generated from a guides file. It records all parts, build options and positions.
    ie genericBiped, genericQuadraped, humanFace

:Guides File: Is a Maya scene file that contains all of your guides. This file will ultimately be used to build all your
    rig variants. Guides can always be modified down the line. Making this a somewhat non-linear rigging approach.

:Skeleton: A skeleton is a rig variant that contains a single heirarchy of **only** all the bind joints the will end up in the
    final rig. This is generated from the guides file.

:Anim Rig: This is the actual animation control rig, which can be used in mutiple rig variants.

:Asset Data: Any binding information or settings pertaining specifically to a single asset. Things like skinClusters, blendShapes,
    setDrivenKeyframes, control shape information, contraints and connections specific to a single rig variant.

:Asset Custom File: Every asset has its own empty python module where you can add add any custom python code to further customize
    your rig. This single file contains all the custom code for all variants related to this asset.

    This custom python module can also inherit the custom code from other assets if you so choose.

    This file lives in the asset rigbuild folder.

:Asset Build List: Every asset has its own build list which also lives in the rigbuild folder. This build list defines an ordered
    set of commands to build your rig variant from start to finish. This list can also be executed through the script editor.

:Asset Inheritance: You can optionally set an asset environment to include in your sys.path the rigbuild path for a different asset.
    This allows you to use code and asset data from different assets without having to physically copy code from file to file.
