
#materails
import maya.cmds as mc
import maya.mel as mm

import json
import os

from rigBot import env

#get the materails in the scene

deformer_type = 'shaders'
file_extention = '.shd'

def get_data(nodes=None,
               shaders_only=False,
               file_path=False,
               searchString=[ '*_GEP',
                              '*_GES',
                              '*_PLY',
                              '*_GEN',
                              '*_NRB']):

    """
    Gets data from the scene and returns a dictionary of data about the material in the scene

    data = {'all_materials': ['warmachine_MAT'],
            'animShaders_file': '/net/homes/rgarcia/Desktop/OkoyeAnimationsAndFriends/animShaders.mb',
            'shading_group_lookup': {'warmachine_MAT': 'blinn1SG'},
            'warmachine_GEP': {'materials': ['warmachine_MAT'],
                               'shape': 'warmachine_GEPShape',
                               'single_shader_assignment': 'warmachine_MAT',
                               'transform': 'warmachine_GEP'}}

    """
    #List all objects that have  rigBot naming conventions
    print "file_path at the start", file_path
    mesh_transforms = mc.ls(searchString)

    if nodes:
        nodes = mc.ls(nodes)
        if nodes:
            mesh_transforms = nodes

    #Create the data group
    data = {}
    for mesh_transform in mesh_transforms:
        data[mesh_transform]= {}

    all_materials = []
    for mesh_transform in mesh_transforms:
        mesh = mc.listRelatives(mesh_transform,s=1)[0]
        shading_groups = []
        for connect in mc.listConnections(mesh):
            if mc.nodeType(connect) == "shadingEngine":
                shading_groups.append(connect)

        materials = []
        for sg in shading_groups:
            material_connection = mc.listConnections(sg + ".surfaceShader")
            if material_connection:
                material = material_connection[0]
                materials.append(material)

        materials = list(set(materials))

        all_materials = all_materials + materials
        face_assignment = {}
        for material in materials:
            mm.eval('hyperShade -objects {0};'.format(material))
            faces = mc.ls(sl = True)
            if faces:
                face_assignment[material]= faces
            mc.select(cl = True)

        data[mesh_transform]["transform"] = mesh_transform
        data[mesh_transform]["materials"] = materials
        data[mesh_transform]["shape"] = mesh
        if len(materials) == 1:
            data[mesh_transform]["single_shader_assignment"] = materials[0]
        if len(materials) > 1:
            data[mesh_transform]["multi_face_assignment"] = face_assignment

    data["all_materials"] = all_materials

    data["shading_group_lookup"] = {}
    all_materials = list(set(all_materials))
    shading_groups = []
    for material in all_materials:
        for connect in mc.listConnections(material):
            if mc.nodeType(connect) == "shadingEngine":
                data["shading_group_lookup"][material] = connect
                shading_groups.append(connect)
    # write materials
    print "file_path before if statement",file_path

    # if a file path isnt given build one
    if file_path == False:
        file_path = build_file_path()

    dataPath= os.path.dirname(file_path)
    jsonFile=file_path
    animShaders_file = os.path.join(dataPath,'animShaders.mb')
    data["animShaders_file"]= animShaders_file

    mc.select(cl=1)
    mc.select(shading_groups,r=1,ne=1)
    print all_materials
    print animShaders_file
    mc.file(animShaders_file, op='v=0;',type='mayaBinary', es=1, f= True)
    mc.warning('wrote related materials to '+ animShaders_file)

    if dataPath[-1]!='/':
        dataPath+='/'

    mc.warning('wrote materials to file')

    jsonDump=json.dumps(data,indent=4)
    file = open(jsonFile, 'w')
    file.write(jsonDump)
    file.close()
    env.change_permission(jsonFile)
    mc.warning('Wrote jSon deformer info to: '+ jsonFile)

    return data

def build_file_path():
    """
        Build a json file_path for use with the save and load functions.
        Returns file_path
        Ex.
        file_path = build_file_path()
    """
    rigbuild_path = env.get_rigbuild_path()
    variant = env.get_variant()
    asset = env.get_asset()
    dataPath=os.path.join(rigbuild_path,'data',variant +'/')
    fileName='Materials_{0}.shd'.format(asset)
    file_path = os.path.join(dataPath,fileName)
    return file_path

def assign_data(file_path,import_shaders=True):
    """data is a dictionary."""
    #import the shader file

    jsonFile=file_path

    if not jsonFile:
        jsonFile =build_file_path()

    jsonDataFile=open(jsonFile,'r')
    jsonData=jsonDataFile.read()
    data=json.loads(jsonData)

    if import_shaders:
        animShaders_file=data['animShaders_file']
        mc.file(animShaders_file,i=True)
    for mesh_transform in data.keys():
        if mc.objExists(mesh_transform):
            if mc.nodeType(mesh_transform) == "transform":
                if "single_shader_assignment" in data[mesh_transform].keys():
                    single_shader_assignment = data[mesh_transform]["single_shader_assignment"]
                    shading_group = data["shading_group_lookup"][single_shader_assignment]
                    mc.select(mesh_transform)
                    mc.sets(forceElement = shading_group, e = 1)
                if "multi_face_assignment" in data[mesh_transform].keys():
                    multi_face_assignment = data[mesh_transform]["multi_face_assignment"]
                    for material in multi_face_assignment.keys():
                        shading_group = data["shading_group_lookup"][material]
                        #mc.select(multi_face_assignment[material])
                        mc.select(cl=True)
                        for each in multi_face_assignment[material]:
                            if mc.objExists(each):
                                mc.select(each, add =True)
                        mc.sets(forceElement = shading_group, e = 1)
                        mc.select(cl=True)

def save(file_path, nodes=None):
    """Save charachter shaders"""
    data = get_data(file_path=file_path, nodes=nodes)
    return data

def load(file_path, remap=False, import_shaders=True, **kwargs):
    """Load charachter shaders"""
    assign_data(file_path)

#file_path = "/net/homes/rgarcia/Desktop/OkoyeAnimationsAndFriends/Materials_MatTest.shd"
#save(file_path, node=None)
#load(file_path, import_shaders=True)


#mc.select([u'red_MAT', u'blue_MAT', u'lambert1', u'green_MAT', u'blinn2'])

"""
def _findNodesAndConnections(nodeType=False,nodes=False):
    '''
    Finds all nodes of type, or a list of nodes
    Returns a dictionary Formatted like this
    {
    node={inputs:{source=destination,source=destination}}
                 {outputs:{source=destination,source=destination}}
    }
    '''
    if not nodeType and not nodes:
        mc.error('please supply nodeType= or nodes=')
    if not nodes:
        nodes=mc.ls(type=nodeType)

    connectionDict={}
    for node in nodes:

        inputDict=_findInputNodeConnections(node)
        outputDict=_findOutputNodeConnections(node)
        connectDict={'inputs':inputDict,'outputs':outputDict}
        connectionDict[node]=connectDict

    if connectionDict:
        return connectionDict
    else:
        return False

def _findInputNodeConnections(node):
    '''
    returns a dictoinary of inputs, should connect the key to the value
    '''
    inputs=mc.listConnections(node,s=1,d=0,c=1,p=1)
    i=0
    connectionDict={}
    while i <len(inputs):
        connectionDict[inputs[i+1]]=inputs[i]
        i+=2
    return connectionDict

def _findOutputNodeConnections(node):
    '''
    returns a dictionary of outputs, should connect the key to the value
    '''
    outputs=mc.listConnections(node,s=0,d=1,c=1,p=1)
    i=0
    connectionDict={}
    while i <len(outputs):
        connectionDict[outputs[i]]=outputs[i+1]
        i+=2
    return connectionDict

def _disconnectNodeConnections(nodeType=False,nodes=False,inputs=True,outputs=True):
    if nodeType:
        nodes=mc.ls(type=nodeType)

    if not nodes:
        mc.error('no nodes listed, or none of type '+str(nodeType)+' found in scene')

    connectionDict=_findNodesAndConnections(nodes=nodes)
    if connectionDict:
        for node,inputOutput in connectionDict.items():
            if 'inputs' in inputOutput and inputs:
                for source,destination in inputOutput['inputs'].items():
                    mc.disconnectAttr(source,destination)
            if 'outputs' in inputOutput and outputs:
                for source,destination in inputOutput['outputs'].items():
                    mc.disconnectAttr(source,destination)

def _reconnectNodeConnectionsWithDict(connectionDict):
    '''
    This requires the dictonary created from the
    findNodeConnectionsAndConnections function
    '''
    if connectionDict:
        for node,inputOutput in connectionDict.items():
            for source,destination in inputOutput['inputs'].items():
                if mc.objExists(source):
                    if not mc.isConnected(source,destination):
                        mc.connectAttr(source,destination,f=1)
            for source,destination in inputOutput['outputs'].items():
                if not mc.isConnected(source,destination):
                    mc.connectAttr(source,destination,f=1)

_findNodesAndConnections(nodeType=False,nodes=["blue_MAT"])
"""
