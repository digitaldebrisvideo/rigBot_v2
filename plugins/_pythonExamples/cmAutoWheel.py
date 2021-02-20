import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMaya as OpenMaya
import maya.cmds as mc
import sys

VERSION = '1.0'

## @brief A node that triggers shapes from of an orientation
class AutoWheel(OpenMayaMPx.MPxNode):

    kPluginNodeId = OpenMaya.MTypeId(0x000012345)

    aEnvelope = OpenMaya.MObject()
    aForwardDirectionX = OpenMaya.MObject()
    aForwardDirectionY = OpenMaya.MObject()
    aForwardDirectionZ = OpenMaya.MObject()
    aForwardDirection = OpenMaya.MObject()
    aTime = OpenMaya.MObject()
    aRadius = OpenMaya.MObject()
    aPosMatrix = OpenMaya.MObject()
    aOutSpin = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        self._initialized = False
        self._previousTime = OpenMaya.MTime()
        self._previousVector = OpenMaya.MVector()
        self._previousSpin = 0.0

    def compute(self, plug, data):

        if plug != AutoWheel.aOutSpin:
            return OpenMaya.kUnknownParameter

        dPoint = OpenMaya.MPoint(data.inputValue(self.aForwardDirectionX).asFloat(),
                                 data.inputValue(self.aForwardDirectionY).asFloat(),
                                 data.inputValue(self.aForwardDirectionZ).asFloat()
                            )

        posMatrix = data.inputValue(self.aPosMatrix).asMatrix()
        currentTime = data.inputValue(self.aTime).asTime()
        envelope = data.inputValue(self.aEnvelope).asFloat()
        radius = data.inputValue(self.aRadius).asFloat()

        offsetWorldMatrix = OpenMaya.MMatrix()
        OpenMaya.MScriptUtil.setDoubleArray(offsetWorldMatrix[0], 0, dPoint.x)
        OpenMaya.MScriptUtil.setDoubleArray(offsetWorldMatrix[0], 1, dPoint.y)
        OpenMaya.MScriptUtil.setDoubleArray(offsetWorldMatrix[0], 2, dPoint.z)

        OpenMaya.MScriptUtil.setDoubleArray(offsetWorldMatrix[1], 0, 1)
        OpenMaya.MScriptUtil.setDoubleArray(offsetWorldMatrix[2], 1, 1)
        OpenMaya.MScriptUtil.setDoubleArray(offsetWorldMatrix[3], 2, 1)
        dirMatrix = offsetWorldMatrix * posMatrix

        timeDifference = currentTime.value() - self._previousTime.value()

        mTransformMtx = OpenMaya.MTransformationMatrix(posMatrix)
        currentVector = mTransformMtx.translation(OpenMaya.MSpace.kWorld)

        mTransformMtx = OpenMaya.MTransformationMatrix(dirMatrix)
        dirVector = mTransformMtx.translation(OpenMaya.MSpace.kWorld)

        newSpin = 0.0

        if not self._initialized:
            self._previousVector = currentVector
            self._previousTime = currentTime
            self._previousSpin = newSpin
            self._initialized = True

        # If time stepis greaterthan 1 then zero it out
        if abs(timeDifference) > 1.0:
            self._previousVector = currentVector
            self._previousTime = currentTime
            self._previousSpin = newSpin
            self._initialized = False

        # This is the actual computation for the spin
        else:

            motionVector = OpenMaya.MVector(currentVector - self._previousVector)
            wheelVector  = OpenMaya.MVector(dirVector - currentVector)

            distance = motionVector.length()

            motionVector.normalize()
            wheelVector.normalize()

            dotproduct = sum(i*j for i,j in zip(motionVector, wheelVector))

            #this needs work
            newSpin =  360 / (3.1415*radius*2) * (dotproduct*distance) * envelope
            newSpin += self._previousSpin

            self._previousVector = currentVector
            self._previousTime = OpenMaya.MTime(currentTime)
            self._previousSpin = newSpin

        hOutput = data.outputValue(AutoWheel.aOutSpin)
        hOutput.setFloat(newSpin)
        hOutput.setClean()
        data.setClean(plug)

## @brief Creates the object for Maya.
def creator():
    return OpenMayaMPx.asMPxPtr(AutoWheel())

## @brief Creates the node attributes.
def initialize():

    nAttr = OpenMaya.MFnNumericAttribute()
    mAttr = OpenMaya.MFnMatrixAttribute()
    uAttr = OpenMaya.MFnUnitAttribute()
    compound = OpenMaya.MFnCompoundAttribute()

    #input attrs
    AutoWheel.aEnvelope = nAttr.create('envelope', 'en', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0)
    nAttr.setMax(1)
    AutoWheel.addAttribute(AutoWheel.aEnvelope)

    AutoWheel.aRadius = nAttr.create('radius', 'radi', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0)
    AutoWheel.addAttribute(AutoWheel.aRadius)

    AutoWheel.aForwardDirectionX = nAttr.create('forwardDirectionX', 'fdx', OpenMaya.MFnNumericData.kFloat, 0.0)
    nAttr.setKeyable(True)
    AutoWheel.addAttribute(AutoWheel.aForwardDirectionX)

    AutoWheel.aForwardDirectionY = nAttr.create('forwardDirectionY', 'fdy', OpenMaya.MFnNumericData.kFloat, 0.0)
    nAttr.setKeyable(True)
    AutoWheel.addAttribute(AutoWheel.aForwardDirectionY)

    AutoWheel.aForwardDirectionZ = nAttr.create('forwardDirectionZ', 'fdz', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    AutoWheel.addAttribute(AutoWheel.aForwardDirectionZ)

    aForwardDirection = compound.create('forwardDirection', 'fd')
    compound.addChild(AutoWheel.aForwardDirectionX);
    compound.addChild(AutoWheel.aForwardDirectionY);
    compound.addChild(AutoWheel.aForwardDirectionZ);
    compound.setKeyable(True)
    compound.setWritable(True)
    compound.setStorable(True)
    AutoWheel.addAttribute(aForwardDirection);

    AutoWheel.aPosMatrix = mAttr.create('postitionMatrix', 'pmtx')
    AutoWheel.addAttribute(AutoWheel.aPosMatrix)

    AutoWheel.aTime = uAttr.create('time', 'time', OpenMaya.MFnUnitAttribute.kTime, 0.0)
    AutoWheel.addAttribute(AutoWheel.aTime)

    # output
    AutoWheel.aOutSpin = nAttr.create('outputSpin', 'os', OpenMaya.MFnNumericData.kFloat, 0)
    nAttr.setWritable(False)
    nAttr.setStorable(False)
    AutoWheel.addAttribute(AutoWheel.aOutSpin)

    AutoWheel.attributeAffects(AutoWheel.aEnvelope, AutoWheel.aOutSpin)
    AutoWheel.attributeAffects(AutoWheel.aTime, AutoWheel.aOutSpin)
    AutoWheel.attributeAffects(AutoWheel.aRadius, AutoWheel.aOutSpin)
    AutoWheel.attributeAffects(AutoWheel.aPosMatrix, AutoWheel.aOutSpin)

    AutoWheel.attributeAffects(AutoWheel.aForwardDirectionX, AutoWheel.aOutSpin)
    AutoWheel.attributeAffects(AutoWheel.aForwardDirectionY, AutoWheel.aOutSpin)
    AutoWheel.attributeAffects(AutoWheel.aForwardDirectionZ, AutoWheel.aOutSpin)


## @brief Initializes the plug-in in Maya.
def initializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj, 'Gerorge Saavedra', VERSION, 'Any')
    plugin.registerNode('cmAutoWheel', AutoWheel.kPluginNodeId, creator, initialize)

## @brief Uninitializes the plug-in in Maya.
def uninitializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj)
    plugin.deregisterNode(AutoWheel.kPluginNodeId)

