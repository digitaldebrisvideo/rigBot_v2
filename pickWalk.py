"""
pickWalk.py - 
    Takes advantage of Maya 2017's controller additon to allow for pickWalk tagging.
"""
import maya.cmds as mc

#Tag attributes.
def attribute_tag(ctrl, parent_ctrl):
    """
    Creates an attribute that defines a pickwalk attribute tag. This dictates the parent child relationship that is run during the rig 
    finalize step.
    
    Example
    ctrl = "L_index_C_CTL"
    parent_ctrl = "L_index_B_CTL"
    attribute_tag(ctrl, parent_ctrl)
    """
    if not mc.objExists(ctrl+'.pickWalkParentTag'):
        mc.addAttr(ctrl, ln='pickWalkParentTag', dt='string')
    mc.setAttr(ctrl+'.pickWalkParentTag', parent_ctrl, type ="string")

#Execute node connections

def get_controller_tag_node(node):
    """Looks for tag node associated with given node, return value is either the control_tag_node or None."""
    connections = mc.listConnections(node)
    for connect in connections:
        if connect.endswith('_tag'):
            controller_tag_node = connect
            return controller_tag_node
        else:
            return None

def assign_controller_tag_node(ctrl):
    """Assign a tag node to a control and returns the controller_tag_node"""
    mc.controller(ctrl)
    controller_tag_node = ''
    
    #Get the name of the controller tag Maya's controller tag returns None.
    connections = mc.listConnections(ctrl)
    for connect in connections:
        if connect.endswith('_tag'):
            controller_tag_node = connect
    return controller_tag_node    

def parent_controller_tag(ctrl,parent_ctrl):
    """Create a parent relationship between two controls. Assumes both controls have tag nodes."""
    mc.controller (ctrl, parent_ctrl, p = 1)

def create_tag(ctrl):
    """
    Reads the '.pickWalkParentTag' attribute and creates the approriate nodes and connections.
    This assumes error checking has already been done
    """
    #get the parent ctrl from the .pickwalkTag attribute
    parent_ctrl = mc.getAttr(ctrl+'.pickWalkParentTag')
    #Get the control tag if it exists, create one if None exist.
    controller_tag_node = get_controller_tag_node(ctrl)
    
    if controller_tag_node == None:
        controller_tag_node = assign_controller_tag_node(ctrl)
    parent_controller_tag_node = get_controller_tag_node(parent_ctrl)
    if parent_controller_tag_node == None:
        parent_controller_tag_node = assign_controller_tag_node(parent_ctrl)
    #Execute
    parent_controller_tag(ctrl, parent_ctrl)

def create_tags():
    """
    Looks for controls that have the '.pickWalkParentTag' and executes the connections using the create_tag() function.
    """
    ctrls = [c.split('.')[0] for c in mc.ls('*.pickWalkParentTag')]
    for ctrl in ctrls:
        parent_ctrl = mc.getAttr(ctrl+'.pickWalkParentTag')

        if parent_ctrl == "":
            print "skipping", ctrl, "its pickwalk parent is a blank string."
            continue
        else:
            create_tag(ctrl)

def delete_tags():
    """
    Delete all tag nodes. This leaves the attributes on the controls intact
    and they can be recreated through the create_all() function.
    """
    initial_search = mc.ls("*_tag")
    for each in initial_search:
        #Ensure it hasnt been deleted
        if mc.objExists(each):
            #Make sure its a controller to ensure we dont accidently delete anything else that happens to have _tag in the name
            if mc.nodeType(each) == "controller":
                mc.delete(each)            
#create_all()