import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMaya as OpenMaya
import maya.cmds as mc
import math
import sys

VERSION = '1.0'

def crossProduct(a, b):
    c = OpenMaya.MVector( a[1]*b[2] - a[2]*b[1],
                          a[2]*b[0] - a[0]*b[2],
                          a[0]*b[1] - a[1]*b[0] )

    return c

def get_msg(v):
    return '{0}, {1}, {2}'.format(v.x, v.y, v.z)

## @brief A node that triggers shapes from of an orientation
class Collision(OpenMayaMPx.MPxNode):

    kPluginNodeId = OpenMaya.MTypeId(0x0087874345)

    aEnvelope = OpenMaya.MObject()
    aTime = OpenMaya.MObject()
    aInMesh = OpenMaya.MObject()
    aInMatrix = OpenMaya.MObject()
    outputRotate = OpenMaya.MObject()
    outputRotateX = OpenMaya.MObject()
    outputRotateY = OpenMaya.MObject()
    outputRotateZ = OpenMaya.MObject()

    outputTranslate = OpenMaya.MObject()
    outputTranslateX = OpenMaya.MObject()
    outputTranslateY = OpenMaya.MObject()
    outputTranslateZ = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        self._initialized = False
        self._previousTime = OpenMaya.MTime()
        self._pinnedMatrix = OpenMaya.MMatrix()

    def compute(self, plug, data):

        plugs = [Collision.outputTranslate, Collision.outputTranslateX, Collision.outputTranslateY, Collision.outputTranslateZ,
                 Collision.outputRotate, Collision.outputRotateX, Collision.outputRotateY, Collision.outputRotateZ ]

        if plug not in plugs :
            return OpenMaya.kUnknownParameter

        inMeshPlug = OpenMaya.MPlug(self.thisMObject(), self.aInMesh)
        connected_mesh = inMeshPlug.isConnected()

        inMesh = data.inputValue(self.aInMesh).asMesh()
        currentMatrix = data.inputValue(self.aInMatrix).asMatrix()
        parentInverse_mtx = data.inputValue(self.aPnMatrix).asMatrix()
        currentTime = data.inputValue(self.aTime).asTime()
        envelope = data.inputValue(self.aEnvelope).asFloat()
        falloff = data.inputValue(self.aFalloff).asFloat()
        pin = data.inputValue(self.aPin).asFloat()
        use_force = data.inputValue(self.aUseForce).asInt()
        force = data.inputValue(self.aForce).asFloat()
        timeDifference = currentTime.value() - self._previousTime.value()
        ground =  data.inputValue(self.aGround).asFloat()

        mTransformMtx = OpenMaya.MTransformationMatrix(currentMatrix)
        pointToComp = OpenMaya.MPoint(mTransformMtx.translation(OpenMaya.MSpace.kWorld))

        # build collision matrix
        if connected_mesh:

            pos = OpenMaya.MPoint()
            y_vec = OpenMaya.MVector()

            meshFn = OpenMaya.MFnMesh(inMesh)
            meshFn.getClosestPointAndNormal( pointToComp, pos, y_vec, OpenMaya.MSpace.kWorld)

            # get ctrls x vector
            ct_x_vec = OpenMaya.MVector(currentMatrix(0,0), currentMatrix(0,1), currentMatrix(0,2))
            z_vec = crossProduct(ct_x_vec, y_vec)
            x_vec = crossProduct(y_vec, z_vec)

            mtx = [ x_vec.x, x_vec.y, x_vec.z, 0,
                    y_vec.x, y_vec.y, y_vec.z, 0,
                    z_vec.x, z_vec.y, z_vec.z, 0,
                    pos.x, pos.y, pos.z, 1
            ]

        else:
            pos = pointToComp
            y_vec = OpenMaya.MVector(0,1,0)

            # get ctrls x vector
            ct_x_vec = OpenMaya.MVector(currentMatrix(0,0), currentMatrix(0,1), currentMatrix(0,2))
            z_vec = crossProduct(ct_x_vec, y_vec)
            x_vec = crossProduct(y_vec, z_vec)

            mtx = [ x_vec.x, x_vec.y, x_vec.z, 0,
                    y_vec.x, y_vec.y, y_vec.z, 0,
                    z_vec.x, z_vec.y, z_vec.z, 0,
                    pos.x, ground, pos.z, 1
            ]

        collision_matrix = OpenMaya.MMatrix()
        OpenMaya.MScriptUtil.createMatrixFromList(mtx, collision_matrix)

        # find out IF it's colliding
        local_point = pointToComp * collision_matrix.inverse()

        isColliding = 1.0 + ((( local_point.y - 0.0 ) / ( falloff - 0.0 )) * ( 0.0 - 1.0))
        isColliding = min( max(isColliding, 0), 1.0)

        if use_force:
            isColliding = force
        isColliding *= envelope

        #OpenMaya.MGlobal.displayInfo(isColliding)
        if not self._initialized or not pin or abs(timeDifference) > 1.0 or isColliding < 0.33:
            self._pinnedMatrix = collision_matrix
            self._previousTime = currentTime
            self._initialized = True

        # This is the actual computation for the spin
        else:
            collision_matrix = (collision_matrix * (1.0 - pin)) + (self._pinnedMatrix * pin)
            self._pinnedMatrix = collision_matrix
            self._previousTime = OpenMaya.MTime(currentTime)

        # conver out matrix to trans and rot output
        out_matrix = (currentMatrix * (1.0 - isColliding)) + (collision_matrix * isColliding)
        local_matrix = out_matrix * parentInverse_mtx;

        matrixFn = OpenMaya.MTransformationMatrix(local_matrix)
        out_trans = matrixFn.getTranslation(OpenMaya.MSpace.kTransform)
        out_rot = matrixFn.rotation().asEulerRotation().asVector()

        hOutput = data.outputValue(Collision.outputTranslate)
        hOutput.setMVector(out_trans)
        hOutput.setClean()

        hOutput = data.outputValue(Collision.outputRotate)
        hOutput.setMVector(out_rot)
        hOutput.setClean()

        hOutput = data.outputValue(Collision.aIsColliding)
        hOutput.setFloat(isColliding)
        hOutput.setClean()

        data.setClean(plug)

## @brief Creates the object for Maya.
def creator():
    return OpenMayaMPx.asMPxPtr(Collision())

## @brief Creates the node attributes.
def initialize():

    nAttr = OpenMaya.MFnNumericAttribute()
    mAttr = OpenMaya.MFnMatrixAttribute()
    uAttr = OpenMaya.MFnUnitAttribute()
    tAttr = OpenMaya.MFnTypedAttribute()
    compound = OpenMaya.MFnCompoundAttribute()

    #input attrs
    Collision.aEnvelope = nAttr.create('envelope', 'e', OpenMaya.MFnNumericData.kFloat, 1.0)
    nAttr.setKeyable(True)
    nAttr.setMin(0)
    nAttr.setMax(1)
    Collision.addAttribute(Collision.aEnvelope)

    Collision.aFalloff = nAttr.create('falloff', 'fo', OpenMaya.MFnNumericData.kFloat, 1)
    nAttr.setKeyable(True)
    nAttr.setMin(0)
    Collision.addAttribute(Collision.aFalloff)

    Collision.aPin = nAttr.create('pinOnContact', 'p', OpenMaya.MFnNumericData.kFloat, 0)
    nAttr.setKeyable(True)
    nAttr.setMin(0)
    nAttr.setMax(1)
    Collision.addAttribute(Collision.aPin)

    Collision.aGround = nAttr.create('groundPlane', 'gp', OpenMaya.MFnNumericData.kFloat, 0)
    nAttr.setKeyable(True)
    Collision.addAttribute(Collision.aGround)

    Collision.aUseForce = nAttr.create('forceOverride', 'fov', OpenMaya.MFnNumericData.kInt, 0)
    nAttr.setKeyable(True)
    nAttr.setMin(0)
    nAttr.setMax(1)
    Collision.addAttribute(Collision.aUseForce)

    Collision.aForce = nAttr.create('override', 'ov', OpenMaya.MFnNumericData.kFloat, 0)
    nAttr.setKeyable(True)
    nAttr.setMin(0)
    nAttr.setMax(1)
    Collision.addAttribute(Collision.aForce)

    Collision.aInMesh = tAttr.create("inputMesh", "mesh", OpenMaya.MFnData.kMesh)
    Collision.addAttribute(Collision.aInMesh)

    Collision.aInMatrix = mAttr.create('inputMatrix', 'im')
    Collision.addAttribute(Collision.aInMatrix)

    Collision.aPnMatrix = mAttr.create('parentInverseMatrix', 'pm')
    Collision.addAttribute(Collision.aPnMatrix)

    Collision.aTime = uAttr.create('time', 't', OpenMaya.MFnUnitAttribute.kTime, 0.0)
    Collision.addAttribute(Collision.aTime)

    # output
    Collision.outputTranslateX = nAttr.create("outputTranslateX", "otx", OpenMaya.MFnNumericData.kDouble, 0)
    nAttr.setStorable(False)
    nAttr.setKeyable(False)
    nAttr.setWritable(False)
    Collision.addAttribute(Collision.outputTranslateX)

    Collision.outputTranslateY = nAttr.create("outputTranslateY", "oty", OpenMaya.MFnNumericData.kDouble, 0)
    nAttr.setStorable(False)
    nAttr.setWritable(False)
    nAttr.setKeyable(False)
    Collision.addAttribute(Collision.outputTranslateY)

    Collision.outputTranslateZ = nAttr.create("outputTranslateZ", "otz", OpenMaya.MFnNumericData.kDouble, 0)
    nAttr.setStorable(False)
    nAttr.setKeyable(False)
    nAttr.setWritable(False)
    Collision.addAttribute(Collision.outputTranslateZ)

    Collision.outputTranslate = compound.create("outputTranslate", "ot")
    compound.addChild(Collision.outputTranslateX)
    compound.addChild(Collision.outputTranslateY)
    compound.addChild(Collision.outputTranslateZ)
    compound.setStorable(False)
    compound.setKeyable(False)
    compound.setWritable(False)
    Collision.addAttribute(Collision.outputTranslate)

    Collision.outputRotateX = nAttr.create("outputRotateX", "orx", OpenMaya.MFnNumericData.kDouble, 0)
    nAttr.setStorable(False)
    nAttr.setKeyable(False)
    nAttr.setWritable(False)
    Collision.addAttribute(Collision.outputRotateX)

    Collision.outputRotateY = nAttr.create("outputRotateY", "ory", OpenMaya.MFnNumericData.kDouble, 0)
    nAttr.setStorable(False)
    nAttr.setWritable(False)
    nAttr.setKeyable(False)
    Collision.addAttribute(Collision.outputRotateY)

    Collision.outputRotateZ = nAttr.create("outputRotateZ", "orz", OpenMaya.MFnNumericData.kDouble, 0)
    nAttr.setStorable(False)
    nAttr.setKeyable(False)
    nAttr.setWritable(False)
    Collision.addAttribute(Collision.outputRotateZ)

    Collision.outputRotate = compound.create("outputRotate", "or")
    compound.addChild(Collision.outputRotateX)
    compound.addChild(Collision.outputRotateY)
    compound.addChild(Collision.outputRotateZ)
    compound.setStorable(False)
    compound.setKeyable(False)
    compound.setWritable(False)
    Collision.addAttribute(Collision.outputRotate)

    Collision.aIsColliding = nAttr.create("isColliding", "ic", OpenMaya.MFnNumericData.kFloat, 0)
    nAttr.setStorable(False)
    nAttr.setWritable(False)
    nAttr.setKeyable(False)
    Collision.addAttribute(Collision.aIsColliding)

    Collision.attributeAffects(Collision.aEnvelope, Collision.outputTranslate)
    Collision.attributeAffects(Collision.aInMesh, Collision.outputTranslate)
    Collision.attributeAffects(Collision.aTime, Collision.outputTranslate)
    Collision.attributeAffects(Collision.aInMatrix, Collision.outputTranslate)
    Collision.attributeAffects(Collision.aPnMatrix, Collision.outputTranslate)
    Collision.attributeAffects(Collision.aFalloff, Collision.outputTranslate)
    Collision.attributeAffects(Collision.aPin, Collision.outputTranslate)
    Collision.attributeAffects(Collision.aForce, Collision.outputTranslate)
    Collision.attributeAffects(Collision.aGround, Collision.outputTranslate)
    Collision.attributeAffects(Collision.aUseForce, Collision.outputTranslate)

    Collision.attributeAffects(Collision.aEnvelope, Collision.outputRotate)
    Collision.attributeAffects(Collision.aInMesh, Collision.outputRotate)
    Collision.attributeAffects(Collision.aTime, Collision.outputRotate)
    Collision.attributeAffects(Collision.aInMatrix, Collision.outputRotate)
    Collision.attributeAffects(Collision.aPnMatrix, Collision.outputRotate)
    Collision.attributeAffects(Collision.aFalloff, Collision.outputRotate)
    Collision.attributeAffects(Collision.aPin, Collision.outputRotate)
    Collision.attributeAffects(Collision.aForce, Collision.outputRotate)
    Collision.attributeAffects(Collision.aGround, Collision.outputRotate)
    Collision.attributeAffects(Collision.aUseForce, Collision.outputRotate)

    Collision.attributeAffects(Collision.aEnvelope, Collision.aIsColliding)
    Collision.attributeAffects(Collision.aInMesh, Collision.aIsColliding)
    Collision.attributeAffects(Collision.aTime, Collision.aIsColliding)
    Collision.attributeAffects(Collision.aInMatrix, Collision.aIsColliding)
    Collision.attributeAffects(Collision.aPnMatrix, Collision.aIsColliding)
    Collision.attributeAffects(Collision.aFalloff, Collision.aIsColliding)
    Collision.attributeAffects(Collision.aPin, Collision.aIsColliding)
    Collision.attributeAffects(Collision.aForce, Collision.aIsColliding)
    Collision.attributeAffects(Collision.aGround, Collision.aIsColliding)
    Collision.attributeAffects(Collision.aUseForce, Collision.aIsColliding)


## @brief Initializes the plug-in in Maya.
def initializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj, 'Gerorge Saavedra', VERSION, 'Any')
    plugin.registerNode('cmCollision', Collision.kPluginNodeId, creator, initialize)

## @brief Uninitializes the plug-in in Maya.
def uninitializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj)
    plugin.deregisterNode(Collision.kPluginNodeId)

