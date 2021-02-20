"""uvTools.py - tools for uv layout"""

import maya.OpenMaya as om
import maya.cmds as cmds
 
def get_uv_shell_list(name):
    """Get the uv shells of a given transform."""
    selList = om.MSelectionList()
    selList.add(name)
    selListIter = om.MItSelectionList(selList, om.MFn.kMesh)
    pathToShape = om.MDagPath()
    selListIter.getDagPath(pathToShape)
    meshNode = pathToShape.fullPathName()
    uvSets = cmds.polyUVSet(meshNode, query=True, allUVSets =True)
    allSets = []
    for uvset in uvSets:
        shapeFn = om.MFnMesh(pathToShape)
        shells = om.MScriptUtil()
        shells.createFromInt(0)
        # shellsPtr = shells.asUintPtr()
        nbUvShells = shells.asUintPtr()
 
        uArray = om.MFloatArray()   #array for U coords
        vArray = om.MFloatArray()   #array for V coords
        uvShellIds = om.MIntArray() #The container for the uv shell Ids
 
        shapeFn.getUVs(uArray, vArray)
        shapeFn.getUvShellsIds(uvShellIds, nbUvShells, uvset)
 
        # shellCount = shells.getUint(shellsPtr)
        shells = {}
        for i, n in enumerate(uvShellIds):
            if n in shells:
                shells[n].append( '%s.map[%i]' % ( name, i ) )
            else:
                shells[n] = [ '%s.map[%i]' % ( name, i ) ]
        allSets.append({uvset: shells})
    return allSets

def scale_selected_uvs(user_scale_value):
    """Scale the selected Uvs by the user scale value around their center"""
    uvvalues=cmds.polyEditUV(q=1)
    #number of values in array of all locations, used for the looping 
    selSize=len(uvvalues)
    #This next bit will split the array of both UV values into 2
    #with only the u and v values in each array using every second
    #number starting from different points as the main procedure
    Uarray = []
    Varray = []
    #loop for U array starting from the first number
    current_coord = "u"
    for value in uvvalues:
        if current_coord == "v":
            Varray.append(value)
            current_coord = "u"
            continue
        if current_coord == "u":
            Uarray.append(value)
            current_coord = "v"
        
    Uarray=sorted(Uarray)
    #sort both arrays into acending order so first number will
    #be the lowest (min) U or V value and the last the highest (max)
    Varray=sorted(Varray)
    #only need to find the size of one array 
    #they both have the same number of values
    #i use this to select the last number in the array
    UarraySize=len(Uarray)
    #Max number in U array
    maxNuU=Uarray[UarraySize - 1]
    #Max number in V array
    maxNuV=Varray[UarraySize - 1]
    #Min number in U array
    minNuU=Uarray[0]
    #Min number in V array
    minNuV=Varray[0]
    #get the average of the range to define pivot
    middleU=(maxNuU + minNuU) / 2
    middleV=(maxNuV + minNuV) / 2
    #scale with the pivot we have defined
    cmds.polyEditUVShell(pv=middleV, sv=user_scale_value, su=user_scale_value, pu=middleU)

def scale_uv_shells(transform, user_scale_value):
    """
    Scale a transforms uvshells by a user scale value.
    user_scale_value = .2
    transform = "pSphere1"

    uvTools.scale_uv_shells(transform, user_scale_value)
    """
    a = get_uv_shell_list(transform)
    #ToDo - See if i can work with the map1 as a uv set flag
    for each in a[0]["map1"]:
        cmds.select (a[0]["map1"][each])
        scale_selected_uvs(user_scale_value)
