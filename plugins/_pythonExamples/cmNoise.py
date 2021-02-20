import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMaya as OpenMaya
import math
import sys

import maya.mel as mm

VERSION = '1.0'

## @brief A node that triggers shapes from of an orientation
class Noise(OpenMayaMPx.MPxNode):

    kPluginNodeId = OpenMaya.MTypeId(0x000012346)

    aOutput = OpenMaya.MObject()
    aTime = OpenMaya.MObject()
    aEnvelope = OpenMaya.MObject()
    aAmp = OpenMaya.MObject()
    aFreq = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        self._initialized = False
        self._currentPosition = OpenMaya.MPoint()
        self._previousPosition = OpenMaya.MPoint()
        self._previousTime = OpenMaya.MTime()

    def compute(self, plug, data):

        if plug != Noise.aOutput:
            #return OpenMaya.kUnknownParameter
            pass

        # Get the inputs
        currentTime = data.inputValue(self.aTime).asTime()
        envelope = data.inputValue(self.aEnvelope).asFloat()

        amp = data.inputValue(self.aAmp).asFloat()
        freq = data.inputValue(self.aFreq).asFloat()

        dnoise = list(mm.eval('dnoise(<<{0}, {0}, {0}>>);'.format(currentTime.value()*freq)))
        dnoise[0] *= amp * envelope
        dnoise[1] *= amp * envelope
        dnoise[2] *= amp * envelope

        noiseVec = OpenMaya.MFloatVector(*dnoise)

        hOutput = data.outputValue(Noise.aOutput)
        hOutput.setMFloatVector(noiseVec)
        hOutput.setClean()
        data.setClean(plug)

## @brief Creates the object for Maya.
def creator():
    return OpenMayaMPx.asMPxPtr(Noise())

## @brief Creates the node attributes.
def initialize():
    nAttr = OpenMaya.MFnNumericAttribute()
    uAttr = OpenMaya.MFnUnitAttribute()

    Noise.aOutput = nAttr.createPoint('output', 'out')
    nAttr.setWritable(False)
    nAttr.setStorable(False)
    Noise.addAttribute(Noise.aOutput)

    Noise.aTime = uAttr.create('time', 'time', OpenMaya.MFnUnitAttribute.kTime, 0.0)
    Noise.addAttribute(Noise.aTime)
    Noise.attributeAffects(Noise.aTime, Noise.aOutput)

    Noise.aEnvelope = nAttr.create('envelope', 'en', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    nAttr.setMax(1.0)
    Noise.addAttribute(Noise.aEnvelope)
    Noise.attributeAffects(Noise.aEnvelope, Noise.aOutput)

    Noise.aFreq = nAttr.create('frequency', 'freq', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0.001)
    Noise.addAttribute(Noise.aFreq)
    Noise.attributeAffects(Noise.aFreq, Noise.aOutput)

    Noise.aAmp = nAttr.create('amplitude', 'amp', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    Noise.addAttribute(Noise.aAmp)
    Noise.attributeAffects(Noise.aAmp, Noise.aOutput)

## @brief Initializes the plug-in in Maya.
def initializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj, 'Briana Hamilton', VERSION, 'Any')
    plugin.registerNode('cmNoise', Noise.kPluginNodeId, creator, initialize)

## @brief Uninitializes the plug-in in Maya.
def uninitializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj)
    plugin.deregisterNode(Noise.kPluginNodeId)

