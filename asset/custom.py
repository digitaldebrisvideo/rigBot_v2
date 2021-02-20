# Asset Custom Module
import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import control
from rigBot import utils
from rigBot import env

"""
This is an empty asset specific cutom module that will run code at certain
build stages. These classes can be left blank, overwritten, or inherited from another asset.
You can use any standard python functionality build your asset custom.py

NOTES:
You can import another assets custom.py file and
inherit its class into any of these.

Also, by default the anim class from this module is inhertied into all other classes below.

The class names corespond tothe rigType you are building. IF you create a new
rigType you'll have to write a custom class for it here.
"""

class Default():
    """Class for Default rig specific build"""

    @classmethod
    def post_skel(self):
        """Runs after the skeleton has been built."""
        pass

    @classmethod
    def post_rig(self):
        """Runs after the control rig has been built."""
        pass

    @classmethod
    def pre_bind(self):
        """Runs before the model is bound."""
        pass

    @classmethod
    def post_bind(self):
        """Runs after deformers and constraints have been loaded."""
        pass

    @classmethod
    def post_finalize(self):
        """Last function to run in the build."""
        pass

class Anim(Default):
    """Class for Anim rig build. (Low res anim rig) Inherits Default class."""
    pass

class Export():
    """Class for Export rig specific build. (skeleton and skincluster only)"""

    @classmethod
    def post_skel(self):
        """Runs after the skeleton has been built."""
        pass

    @classmethod
    def post_rig(self):
        """Runs after the control rig has been built."""
        pass

    @classmethod
    def pre_bind(self):
        """Runs before the model is bound."""
        pass

    @classmethod
    def post_bind(self):
        """Runs after deformers and constraints have been loaded."""
        pass

    @classmethod
    def post_finalize(self):
        """Last function to run in the build."""
        pass

class Mocap(Export):
    """Class for Mocap rig build. (Stripped down export rig for mocap shoots and motion builder) Inherits Export class."""
    pass
