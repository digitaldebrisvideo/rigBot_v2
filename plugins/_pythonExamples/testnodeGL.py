import maya.api.OpenMaya as OpenMaya
import maya.api.OpenMayaUI as OpenMayaUI
import maya.api.OpenMayaAnim as OpenMayaAnim
import maya.api.OpenMayaRender as OpenMayaRender

class TestNode(OpenMayaUI.MPxLocatorNode):

    id = OpenMaya.MTypeId( 0x82307 )
    drawDbClassification = "drawdb/geometry/TestNode"
    drawRegistrantId = "TestNodePlugin"

    @staticmethod
    def creator():
        return TestNode()

    @staticmethod
    def initialize():
        pass

    def __init__(self):
        OpenMayaUI.MPxLocatorNode.__init__(self)

    def compute(self, plug, data):
        return None

    def draw(self, view, path, style, status):
        return None

## Viewport 2.0 override implementation
def maya_useNewAPI():
 """
 The presence of this function tells Maya that the plugin produces, and
 expects to be passed, objects created using the Maya Python API 2.0.
 """
 pass

class TestNodeData(OpenMaya.MUserData):
    def __init__(self):
        OpenMaya.MUserData.__init__(self, False) ## don't delete after draw

class TestNodeDrawOverride(OpenMayaRender.MPxDrawOverride):
    @staticmethod
    def creator(obj):
        return TestNodeDrawOverride(obj)

    @staticmethod
    def draw(context, data):
        return

    def __init__(self, obj):
        OpenMayaRender.MPxDrawOverride.__init__(self, obj, TestNodeDrawOverride.draw)

    def supportedDrawAPIs(self):
        ## this plugin supports both GL and DX
        return OpenMayaRender.MRenderer.kOpenGL | OpenMayaRender.MRenderer.kDirectX11 | OpenMayaRender.MRenderer.kOpenGLCoreProfile

    def prepareForDraw(self, objPath, cameraPath, frameContext, oldData):
        ## Retrieve data cache (create if does not exist)
        data = oldData
        if not isinstance(data, TestNodeData):
            data = TestNodeData()

        return data

    def hasUIDrawables(self):
        return True

    def addUIDrawables(self, objPath, drawManager, frameContext, data):
        locatordata = data
        if not isinstance(locatordata, TestNodeData):
            return

def initializePlugin(obj):
    plugin = OpenMaya.MFnPlugin(obj, "Dilen Shah", "1.0", "Any")

    try:
        plugin.registerNode("cmAspectRatio", TestNode.id, TestNode.creator, TestNode.initialize, OpenMaya.MPxNode.kLocatorNode, TestNode.drawDbClassification)
    except:
        sys.stderr.write("Failed to register node\n")
        raise

    try:
        OpenMayaRender.MDrawRegistry.registerDrawOverrideCreator(TestNode.drawDbClassification, TestNode.drawRegistrantId, TestNodeDrawOverride.creator)
    except:
        sys.stderr.write("Failed to register override\n")
        raise

def uninitializePlugin(obj):
    plugin = OpenMaya.MFnPlugin(obj)

    try:
        plugin.deregisterNode(TestNode.id)
    except:
        sys.stderr.write("Failed to deregister node\n")
        pass

    try:
        OpenMayaRender.MDrawRegistry.deregisterDrawOverrideCreator(TestNode.drawDbClassification, TestNode.drawRegistrantId)
    except:
        sys.stderr.write("Failed to deregister override\n")
        pass
