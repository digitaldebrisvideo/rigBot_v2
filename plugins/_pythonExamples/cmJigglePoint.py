import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMaya as OpenMaya
import math
import sys

VERSION = '1.0'

## @brief A node that triggers shapes from of an orientation
class JigglePoint(OpenMayaMPx.MPxNode):

    kPluginNodeId = OpenMaya.MTypeId(0x00001234)

    aOutput = OpenMaya.MObject()
    aTime = OpenMaya.MObject()
    aEnvelope = OpenMaya.MObject()
    aJiggleAmount = OpenMaya.MObject()
    aJiggleX = OpenMaya.MObject()
    aJiggleY = OpenMaya.MObject()
    aJiggleZ = OpenMaya.MObject()
    aDamping = OpenMaya.MObject()
    aStiffness = OpenMaya.MObject()
    aParentInverse = OpenMaya.MObject()
    aGoal = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        self._initialized = False
        self._currentPosition = OpenMaya.MPoint()
        self._previousPosition = OpenMaya.MPoint()
        self._previousTime = OpenMaya.MTime()

    def compute(self, plug, data):

        if plug != JigglePoint.aOutput:
            return OpenMaya.kUnknownParameter

        # Get the inputs
        damping = data.inputValue(self.aDamping).asFloat()
        stiffness = data.inputValue(self.aStiffness).asFloat()
        goal = OpenMaya.MPoint(data.inputValue(self.aGoal).asFloatVector())
        parentInverse = data.inputValue(self.aParentInverse).asMatrix()
        currentTime = data.inputValue(self.aTime).asTime()

        envelope = data.inputValue(self.aEnvelope).asFloat()
        jiggleAmount = data.inputValue(self.aJiggleAmount).asFloat() * envelope
        jiggleX = data.inputValue(self.aJiggleX).asFloat()
        jiggleY = data.inputValue(self.aJiggleY).asFloat()
        jiggleZ = data.inputValue(self.aJiggleZ).asFloat()

        if damping > 1.0:
            damping = 1.0

        if damping <= 0.0:
            damping = 0.001

        if stiffness > 1.0:
            stiffness = 1.0

        if stiffness <= 0.0:
            stiffness = 0.001

        # Initialize the data
        if not self._initialized:
            self._previousTime = currentTime
            self._currentPosition = goal
            self._previousPosition = goal
            self._initialized = True

        # Check if the timestep is just 1 frame since we want a stable simulation
        timeDifference = currentTime.value() - self._previousTime.value()

        if abs(timeDifference) > 1.0:
            self._previousTime = currentTime
            self._currentPosition = goal
            self._previousPosition = goal
            self._initialized = False

            newPosition = goal
            newPosition *= parentInverse

        else:
            # Calculate the output position
            velocity = (self._currentPosition - self._previousPosition) * (1.0 - damping)
            newPosition = self._currentPosition + velocity

            goalForce = (goal - newPosition) * stiffness
            newPosition += goalForce

            # Store the states for the next computation
            self._previousPosition = OpenMaya.MPoint(self._currentPosition)
            self._currentPosition = OpenMaya.MPoint(newPosition)
            self._previousTime = OpenMaya.MTime(currentTime)

            newPosition *= parentInverse
            goalLocal = goal * parentInverse

            newPosition.x = goalLocal.x + ((newPosition.x - goalLocal.x) * jiggleAmount * jiggleX)
            newPosition.y = goalLocal.y + ((newPosition.y - goalLocal.y) * jiggleAmount * jiggleY)
            newPosition.z = goalLocal.z + ((newPosition.z - goalLocal.z) * jiggleAmount * jiggleZ)

        hOutput = data.outputValue(JigglePoint.aOutput)
        outVector = OpenMaya.MFloatVector(newPosition.x, newPosition.y, newPosition.z)
        hOutput.setMFloatVector(outVector)
        hOutput.setClean()
        data.setClean(plug)

## @brief Creates the object for Maya.
def creator():
    return OpenMayaMPx.asMPxPtr(JigglePoint())

## @brief Creates the node attributes.
def initialize():
    nAttr = OpenMaya.MFnNumericAttribute()
    mAttr = OpenMaya.MFnMatrixAttribute()
    uAttr = OpenMaya.MFnUnitAttribute()

    JigglePoint.aOutput = nAttr.createPoint('output', 'out')
    nAttr.setWritable(False)
    nAttr.setStorable(False)
    JigglePoint.addAttribute(JigglePoint.aOutput)

    JigglePoint.aGoal = nAttr.createPoint('goal', 'goal')
    JigglePoint.addAttribute(JigglePoint.aGoal)
    JigglePoint.attributeAffects(JigglePoint.aGoal, JigglePoint.aOutput)

    JigglePoint.aTime = uAttr.create('time', 'time', OpenMaya.MFnUnitAttribute.kTime, 0.0)
    JigglePoint.addAttribute(JigglePoint.aTime)
    JigglePoint.attributeAffects(JigglePoint.aTime, JigglePoint.aOutput)

    JigglePoint.aEnvelope = nAttr.create('envelope', 'envelope', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    nAttr.setMax(1.0)

    JigglePoint.addAttribute(JigglePoint.aEnvelope)
    JigglePoint.attributeAffects(JigglePoint.aEnvelope, JigglePoint.aOutput)

    JigglePoint.aJiggleAmount = nAttr.create('jiggle', 'jiggle', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    JigglePoint.addAttribute(JigglePoint.aJiggleAmount)
    JigglePoint.attributeAffects(JigglePoint.aJiggleAmount, JigglePoint.aOutput)


    JigglePoint.aJiggleX = nAttr.create('jiggleX', 'jiggleX', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    nAttr.setMax(1.0)
    JigglePoint.addAttribute(JigglePoint.aJiggleX)
    JigglePoint.attributeAffects(JigglePoint.aJiggleX, JigglePoint.aOutput)

    JigglePoint.aJiggleY = nAttr.create('jiggleY', 'jiggleY', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    nAttr.setMax(1.0)
    JigglePoint.addAttribute(JigglePoint.aJiggleY)
    JigglePoint.attributeAffects(JigglePoint.aJiggleY, JigglePoint.aOutput)

    JigglePoint.aJiggleZ = nAttr.create('jiggleZ', 'jiggleZ', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    nAttr.setMax(1.0)
    JigglePoint.addAttribute(JigglePoint.aJiggleZ)
    JigglePoint.attributeAffects(JigglePoint.aJiggleZ, JigglePoint.aOutput)

    JigglePoint.aStiffness = nAttr.create('stiffness', 'stiffness', OpenMaya.MFnNumericData.kFloat, 0.1)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    nAttr.setMax(1.0)
    JigglePoint.addAttribute(JigglePoint.aStiffness)
    JigglePoint.attributeAffects(JigglePoint.aStiffness, JigglePoint.aOutput)

    JigglePoint.aDamping = nAttr.create('damping', 'damping', OpenMaya.MFnNumericData.kFloat, 0.1)
    nAttr.setKeyable(True)
    nAttr.setMin(0.0)
    nAttr.setMax(1.0)
    JigglePoint.addAttribute(JigglePoint.aDamping)
    JigglePoint.attributeAffects(JigglePoint.aDamping, JigglePoint.aOutput)

    JigglePoint.aParentInverse = mAttr.create('parentInverse', 'parentInverse')
    JigglePoint.addAttribute(JigglePoint.aParentInverse)


## @brief Initializes the plug-in in Maya.
def initializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj, 'Chad Vernon', VERSION, 'Any')
    plugin.registerNode('cmJigglePoint', JigglePoint.kPluginNodeId, creator, initialize)


## @brief Uninitializes the plug-in in Maya.
def uninitializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj)
    plugin.deregisterNode(JigglePoint.kPluginNodeId)

