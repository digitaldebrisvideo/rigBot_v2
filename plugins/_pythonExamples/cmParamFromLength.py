import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMaya as OpenMaya
import math
import sys

import maya.mel as mm

VERSION = '1.0'

## @brief A node that triggers shapes from of an orientation
class ParamFromLength(OpenMayaMPx.MPxNode):

    kPluginNodeId = OpenMaya.MTypeId(0x0001265466)

    inputCurve = OpenMaya.MObject()
    inputValue = OpenMaya.MObject()
    outputValue = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)

    def compute(self, plug, data):

        if plug != ParamFromLength.outputValue:
            return OpenMaya.kUnknownParameter

        try:
            crv = data.inputValue(self.inputCurve).asNurbsCurve()
            crvFn = OpenMaya.MFnNurbsCurve(crv)
        except:
            return OpenMaya.kUnknownParameter

        length = data.inputValue(self.inputValue).asDouble()

        param = crvFn.findParamFromLength(length);

        hOutput = data.outputValue(ParamFromLength.outputValue)
        hOutput.setDouble(param)
        hOutput.setClean()
        data.setClean(plug)

## @brief Creates the object for Maya.
def creator():
    return OpenMayaMPx.asMPxPtr(ParamFromLength())

## @brief Creates the node attributes.
def initialize():

    nAttr = OpenMaya.MFnNumericAttribute()
    tAttr = OpenMaya.MFnTypedAttribute()

    ParamFromLength.inputCurve = tAttr.create("inputCurve", "ic", OpenMaya.MFnData.kNurbsCurve)
    ParamFromLength.addAttribute(ParamFromLength.inputCurve)

    ParamFromLength.inputValue = nAttr.create("length", "l", OpenMaya.MFnNumericData.kDouble, 0)
    nAttr.setKeyable(True)
    nAttr.setMin(0)
    ParamFromLength.addAttribute(ParamFromLength.inputValue)

    ParamFromLength.outputValue = nAttr.create("param", "p", OpenMaya.MFnNumericData.kDouble)
    nAttr.setKeyable(False)
    nAttr.setWritable(False)
    nAttr.setStorable(False)
    ParamFromLength.addAttribute(ParamFromLength.outputValue)

    ParamFromLength.attributeAffects(ParamFromLength.inputValue, ParamFromLength.outputValue)
    ParamFromLength.attributeAffects(ParamFromLength.inputCurve, ParamFromLength.outputValue)

## @brief Initializes the plug-in in Maya.
def initializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj, 'Briana Hamilton', VERSION, 'Any')
    plugin.registerNode('cmParamFromLength', ParamFromLength.kPluginNodeId, creator, initialize)

## @brief Uninitializes the plug-in in Maya.
def uninitializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj)
    plugin.deregisterNode(ParamFromLength.kPluginNodeId)

