
import maya.api.OpenMaya as OpenMaya
import maya.api.OpenMayaUI as OpenMayaUI
import maya.api.OpenMayaAnim as OpenMayaAnim
import maya.api.OpenMayaRender as OpenMayaRender
import maya.OpenMayaRender as v1omr

import maya.cmds as mc
import maya.mel as mm

class TestNode(OpenMayaUI.MPxLocatorNode):

    id = OpenMaya.MTypeId( 0x82307 )
    drawDbClassification = "drawdb/geometry/TestNode"
    drawRegistrantId = "TestNodePlugin"

    @staticmethod
    def creator():
        return TestNode()

    def excludeAsLocator(self):
        return False

    @staticmethod
    def initialize():

        n_attr = OpenMaya.MFnNumericAttribute()
        t_attr = OpenMaya.MFnTypedAttribute()
        compound = OpenMaya.MFnCompoundAttribute()

        TestNode.camera_name = t_attr.create("camera", "cam", OpenMaya.MFnData.kString)
        TestNode.addAttribute(TestNode.camera_name)

        TestNode.showBorder = n_attr.create("textVisibility", "tv", OpenMaya.MFnNumericData.kBoolean, True)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.showBorder)


        TestNode.showBackground = n_attr.create("backgroundVisibility", "bgv", OpenMaya.MFnNumericData.kBoolean, True)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.showBackground)

        TestNode.transparency = n_attr.create("textAlpha", "ta", OpenMaya.MFnNumericData.kFloat, 0.5)
        n_attr.keyable = True
        n_attr.setMin(0)
        n_attr.setMax(1)
        TestNode.addAttribute(TestNode.transparency)

        TestNode.bgTransparency = n_attr.create("backgroundAlpha", "bga", OpenMaya.MFnNumericData.kFloat, 0.5)
        n_attr.keyable = True
        n_attr.setMin(0)
        n_attr.setMax(1)
        TestNode.addAttribute(TestNode.bgTransparency)

        TestNode.color = n_attr.createColor("textColor", "tcl")
        n_attr.default = (0.0, 1.0, 1.0)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.color)

        TestNode.bgColor = n_attr.createColor("backgroundColor", "bgc")
        n_attr.default = (0,0,0)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.bgColor)

        TestNode.label = t_attr.create("label", "l", OpenMaya.MFnData.kString)
        TestNode.addAttribute(TestNode.label)

        TestNode.textOffsetX = n_attr.create("textPosition", "tp",  OpenMaya.MFnNumericData.kBoolean, False)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.textOffsetX)

        TestNode.fontSize = n_attr.create("fontSize", "fs",  OpenMaya.MFnNumericData.kInt, 24)
        n_attr.keyable = True
        n_attr.setMin(1)
        TestNode.addAttribute(TestNode.fontSize)

        TestNode.lineWidth = n_attr.create("lineWidth", "lw",  OpenMaya.MFnNumericData.kInt, 1)
        n_attr.keyable = True
        n_attr.setMin(1)
        TestNode.addAttribute(TestNode.lineWidth)

        TestNode.allCams = n_attr.create("showOnAllCameras", "sac", OpenMaya.MFnNumericData.kBoolean, False)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.allCams)

        TestNode.aFixed = n_attr.create("useFixedSize", "ufs", OpenMaya.MFnNumericData.kBoolean, False)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.aFixed)

        TestNode.aAspectRatio = n_attr.create("aspectRatio", "ar",  OpenMaya.MFnNumericData.kFloat, 1.77)
        n_attr.keyable = True
        n_attr.setMin(0.001)
        TestNode.addAttribute(TestNode.aAspectRatio)

        TestNode.aWidth = n_attr.create("width", "w",  OpenMaya.MFnNumericData.kInt, 0)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.aWidth)

        TestNode.aHeight = n_attr.create("height", "h",  OpenMaya.MFnNumericData.kInt, 0)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.aHeight)

        TestNode.focalLength = n_attr.create("focalLength", "fl", OpenMaya.MFnNumericData.kFloat, 35.0)
        n_attr.keyable = True
        n_attr.setMin(0)
        TestNode.addAttribute(TestNode.focalLength)

        TestNode.focalLengthVis = n_attr.create("focalLengthVisibility", "flv", OpenMaya.MFnNumericData.kBoolean, True)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.focalLengthVis)

        TestNode.upperOffset = n_attr.create("upperOffset", "uo", OpenMaya.MFnNumericData.kInt, 0)
        n_attr.keyable = True
        n_attr.setMin(0)
        TestNode.addAttribute(TestNode.upperOffset)

        TestNode.lowerOffset = n_attr.create("lowerOffset", "lo", OpenMaya.MFnNumericData.kInt, 0)
        n_attr.keyable = True
        n_attr.setMin(0)
        TestNode.addAttribute(TestNode.lowerOffset)

        TestNode.hlv = n_attr.create("horizontalLineVisibility", "hlv", OpenMaya.MFnNumericData.kBoolean, True)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.hlv)

        TestNode.depth = n_attr.create("depth", "d", OpenMaya.MFnNumericData.kInt, 5)
        n_attr.keyable = True
        n_attr.setMin(2)
        TestNode.addAttribute(TestNode.depth)

        TestNode.gho = n_attr.create("globalHorizontalOffset", "gho", OpenMaya.MFnNumericData.kInt, 0)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.gho)

        TestNode.gvo = n_attr.create("globalVerticalOffset", "gvo", OpenMaya.MFnNumericData.kInt, 0)
        n_attr.keyable = True
        TestNode.addAttribute(TestNode.gvo)


    def __init__(self):
        OpenMayaUI.MPxLocatorNode.__init__(self)

    def compute(self, plug, data):
        return

    def draw(self, view, path, style, status):
        return


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

        fnDagNode = OpenMaya.MFnDagNode(objPath)

        data.camera_name = fnDagNode.findPlug("camera", False).asString()
        data.label = fnDagNode.findPlug("label", False).asString()
        data.aspectRatio = fnDagNode.findPlug("aspectRatio", False).asFloat()
        data.allCams = fnDagNode.findPlug("showOnAllCameras", False).asBool()

        data.bv = fnDagNode.findPlug("textVisibility", False).asBool()
        data.flv = fnDagNode.findPlug("focalLengthVisibility", False).asBool()

        data.font_size = fnDagNode.findPlug("fontSize", False).asInt()
        data.line_width = fnDagNode.findPlug("lineWidth", False).asFloat()

        data.dp = fnDagNode.findPlug("depth", False).asBool()
        data.fixed = fnDagNode.findPlug("useFixedSize", False).asBool()

        data.tox = fnDagNode.findPlug("textPosition", False).asBool()
        data.width = fnDagNode.findPlug("width", False).asInt()
        data.height = fnDagNode.findPlug("height", False).asInt()
        data.focalLength = fnDagNode.findPlug("focalLength", False).asFloat()
        data.upperOffset = fnDagNode.findPlug("upperOffset", False).asInt()
        data.lowerOffset = fnDagNode.findPlug("lowerOffset", False).asInt()

        r = fnDagNode.findPlug("textColorR", False).asFloat()
        g = fnDagNode.findPlug("textColorG", False).asFloat()
        b = fnDagNode.findPlug("textColorB", False).asFloat()
        a = fnDagNode.findPlug("textAlpha", False).asFloat()
        data.font_color = OpenMaya.MColor((r, g, b, a))

        data.gho = fnDagNode.findPlug("globalHorizontalOffset", False).asInt()
        data.gvo = fnDagNode.findPlug("globalVerticalOffset", False).asInt()

        data.hlv = fnDagNode.findPlug("horizontalLineVisibility", False).asBool()
        data.bgv = fnDagNode.findPlug("backgroundVisibility", False).asBool()
        r = fnDagNode.findPlug("backgroundColorR", False).asFloat()
        g = fnDagNode.findPlug("backgroundColorG", False).asFloat()
        b = fnDagNode.findPlug("backgroundColorB", False).asFloat()
        a = fnDagNode.findPlug("backgroundAlpha", False).asFloat()
        data.bg_color = OpenMaya.MColor((r, g, b, a))

        return data

    def hasUIDrawables(self):
        return True

    def addUIDrawables(self, objPath, drawManager, frameContext, data):

        if not isinstance(data, TestNodeData):
            return

        camera_path = frameContext.getCurrentCameraPath()
        camera = OpenMaya.MFnCamera(camera_path)
        cam_name = camera_path.partialPathName()

        if not data.allCams and data.camera_name not in cam_name:
            return

        camera_aspect_ratio = camera.aspectRatio()
        device_aspect_ratio = mc.getAttr("defaultResolution.deviceAspectRatio")

        render_width = mc.getAttr("defaultResolution.width")
        render_height = mc.getAttr("defaultResolution.height")

        vp_x, vp_y, vp_width, vp_height = frameContext.getViewportDimensions()
        vp_half_width = 0.5 * vp_width
        vp_half_height = 0.5 * vp_height
        vp_aspect_ratio = vp_width / float(vp_height)

        scale = 1.0

        if camera.filmFit == OpenMaya.MFnCamera.kHorizontalFilmFit:
            mask_width = vp_width / camera.overscan
            mask_height = mask_width / device_aspect_ratio

        elif camera.filmFit == OpenMaya.MFnCamera.kVerticalFilmFit:
            mask_height = vp_height / camera.overscan
            mask_width = mask_height * device_aspect_ratio

        elif camera.filmFit == OpenMaya.MFnCamera.kFillFilmFit:
            if vp_aspect_ratio < camera_aspect_ratio:
                if camera_aspect_ratio < device_aspect_ratio:
                    scale = camera_aspect_ratio / vp_aspect_ratio

                else:
                    scale = device_aspect_ratio / vp_aspect_ratio

            elif camera_aspect_ratio > device_aspect_ratio:
                scale = device_aspect_ratio / camera_aspect_ratio

            mask_width = vp_width / camera.overscan * scale
            mask_height = mask_width / device_aspect_ratio

        elif camera.filmFit == OpenMaya.MFnCamera.kOverscanFilmFit:
            if vp_aspect_ratio < camera_aspect_ratio:
                if camera_aspect_ratio < device_aspect_ratio:
                    scale = camera_aspect_ratio / vp_aspect_ratio
                else:
                    scale = device_aspect_ratio / vp_aspect_ratio
            elif camera_aspect_ratio > device_aspect_ratio:
                scale = device_aspect_ratio / camera_aspect_ratio

            mask_height = vp_height / camera.overscan / scale
            mask_width = mask_height * device_aspect_ratio

        else:
            OpenMaya.MGlobal.displayError("[cmAspectRatio] Unknown Film Fit value")
            return

        new_ratio = data.aspectRatio
        if data.fixed:
            new_ratio = device_aspect_ratio

        width = int(render_height * new_ratio)
        height = int(render_height)

        orig_width = float(mask_width)
        mask_width = mask_height * new_ratio

        width = int(render_height * new_ratio)
        height = int(render_height)

        if mask_width > orig_width:
            mask_height = orig_width * mask_height / mask_width
            mask_width = orig_width

            width = int(render_width)
            height = int(width * mask_height / mask_width)

        # use fixed width and height
        if data.fixed:
            mask_width = (data.width / float(render_width)) * mask_width
            mask_height = (data.height / float(render_height)) * mask_height

            width = data.width
            height = data.height

        mask_half_width = 0.5 * mask_width
        mask_x = vp_half_width - mask_half_width

        mask_half_height = 0.5 * mask_height
        mask_bottom_y = vp_half_height - mask_half_height
        mask_top_y = vp_half_height + mask_half_height

        border_height = int(mask_height)
        border_width = int(mask_width)
        background_size = (int(mask_width), border_height)

        if data.bgv:

            data.gho *= 0.5
            data.gvo *= 0.5

            drawManager.beginDrawable()

            drawManager.setColor(data.bg_color)
            drawManager.setDepthPriority(1)

            center = OpenMaya.MPoint((vp_width/2)+data.gho, data.gvo)
            drawManager.rect2d(center, OpenMaya.MVector(0, 1), vp_width, mask_bottom_y+data.gvo, filled=True)

            center = OpenMaya.MPoint((vp_width/2)+data.gho, vp_height+data.gvo)
            drawManager.rect2d(center, OpenMaya.MVector(0, 1), vp_width, mask_bottom_y-data.gvo, filled=True)

            center = OpenMaya.MPoint(data.gho, mask_half_height+mask_bottom_y+(2*data.gvo))
            drawManager.rect2d(center, OpenMaya.MVector(0, 1), mask_x+(data.gho), mask_half_height, filled=True)

            center = OpenMaya.MPoint(((mask_width+mask_x+(mask_x/2)))+data.gho, mask_half_height+mask_bottom_y+(2*data.gvo))
            drawManager.rect2d(center, OpenMaya.MVector(0, 1), (mask_x/2)-(data.gho), mask_half_height, filled=True)
            drawManager.endDrawable()

        if data.bv:

            data.gho *= 2
            data.gvo *= 2

            drawManager.beginDrawInXray()

            drawManager.setFontName('Arial')
            drawManager.setFontSize(data.font_size)
            drawManager.setLineWidth(data.line_width)
            drawManager.setColor(data.font_color)
            drawManager.setDepthPriority(data.dp)

            drawManager.setLineStyle(OpenMayaRender.MUIDrawManager.kSolid)

            p0 = OpenMaya.MPoint(mask_x+data.gho, mask_top_y+data.gvo)
            p1 = OpenMaya.MPoint(mask_x+data.gho, mask_bottom_y+data.gvo)
            drawManager.line2d(p0, p1)

            p0 = OpenMaya.MPoint(mask_x+mask_width+data.gho, mask_top_y+data.gvo)
            p1 = OpenMaya.MPoint(mask_x+mask_width+data.gho, mask_bottom_y+data.gvo)
            drawManager.line2d(p0, p1)

            if data.hlv:
                p0 = OpenMaya.MPoint(mask_x+data.gho, mask_bottom_y+data.gvo)
                p1 = OpenMaya.MPoint(mask_x+mask_width+data.gho, mask_bottom_y+data.gvo)
                drawManager.line2d(p0, p1)

                p0 = OpenMaya.MPoint(mask_x+data.gho, mask_top_y+data.gvo)
                p1 = OpenMaya.MPoint(mask_x+mask_width+data.gho, mask_top_y+data.gvo)
                drawManager.line2d(p0, p1)

            if data.flv:
                # focal length
                p0 = OpenMaya.MPoint(mask_x+mask_width-5+data.gho, (mask_bottom_y+data.lowerOffset)+5+data.gvo)
                msg = 'Focal Length {0}'.format(round(data.focalLength, 2))
                drawManager.setFontSize(int(data.font_size*0.8))
                drawManager.text2d(p0, msg, alignment=OpenMayaRender.MUIDrawManager.kRight)
            drawManager.setFontSize(int(data.font_size))

            # text on bottom
            if data.tox:
                p0 = OpenMaya.MPoint(mask_x+5+data.gho, (mask_bottom_y+data.lowerOffset+5)+data.gvo)
                drawManager.text2d(p0, data.label, alignment=OpenMayaRender.MUIDrawManager.kLeft)

                p0 = OpenMaya.MPoint(mask_x+5+data.gho, (mask_bottom_y+data.lowerOffset)+data.font_size+5+data.gvo)
                msg = '{0} x {1}'.format(int(data.width), int(data.height))
                drawManager.setFontSize(int(data.font_size*0.8))
                drawManager.text2d(p0, msg, alignment=OpenMayaRender.MUIDrawManager.kLeft)

            # text on top
            else:
                p0 = OpenMaya.MPoint(mask_x+5+data.gho, (mask_top_y-data.upperOffset-5)-(data.font_size*2)+data.gvo)
                drawManager.text2d(p0, data.label, alignment=OpenMayaRender.MUIDrawManager.kLeft)

                p0 = OpenMaya.MPoint(mask_x+5+data.gho, (mask_top_y-data.upperOffset-5)-data.font_size+data.gvo)
                msg = '{0} x {1}'.format(int(data.width), int(data.height))

                drawManager.setFontSize(int(data.font_size*0.8))
                drawManager.text2d(p0, msg, alignment=OpenMayaRender.MUIDrawManager.kLeft)

            drawManager.endDrawInXray()

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
