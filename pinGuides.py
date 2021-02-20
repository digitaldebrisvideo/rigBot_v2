"""
pin_guides.py
Allows users to dynamically pin guides and to a lessser extent other transforms that require temporary 
transforms to be contraints. Also contians functions to aid in the manipulation of rigBot guides.

"""
import maya.cmds as mc
from rigBot import utils

class Pins():

    def __init__(self):
        """
        Initialize the pin system and run the gui.
        self.pin_groups_dic is cheifly responsible for maintaining the pins available in the scene.

        """
        self.pin_groups_dic = {}
        self.pin_identifier_str = "guidePin"

    def identify(self):
        """
        Identify pins existing in the scene and adjusts self.pin_groups_dic accordingly.
        """
        all_pin_constraints = mc.ls( "*_parentConstraint_" + self.pin_identifier_str)
        self.pin_groups_dic = {}
        for parent_constraint_pin in all_pin_constraints:

            new_pin = Pin(self.pin_identifier_str)
            new_pin.parent_constraint_pin = parent_constraint_pin
            new_pin.driver = mc.listConnections(parent_constraint_pin + ".driver")[0]
            new_pin.driven_item = mc.listConnections(parent_constraint_pin + ".driven")[0]
            new_pin.pin_group_name  = mc.getAttr(parent_constraint_pin + ".pinGroupName")

            if new_pin.pin_group_name != "":
                if new_pin.pin_group_name in self.pin_groups_dic.keys():
                    self.pin_groups_dic[new_pin.pin_group_name].append(new_pin)
                if new_pin.pin_group_name not in self.pin_groups_dic.keys():
                    self.pin_groups_dic[new_pin.pin_group_name] = []
                    self.pin_groups_dic[new_pin.pin_group_name].append(new_pin)

    def pin_to_parent(self):
        """Pins the first item in users selection to all following items in selection."""
        selection = get_selection()
        driver = selection[0]
        driven = selection[1:]
        pin_group_name = driver + "_pcGroup"

        #for driven_item in driven:

        new_pins = []

        for driven_item in driven:
            #print pin_group_name
            new_pin = Pin(self.pin_identifier_str)
            new_pin.create(driver,
                            driven_item, 
                            pin_group_name = pin_group_name,
                            mo = True)
            new_pins.append(new_pin)
        if pin_group_name in self.pin_groups_dic.keys():
            self.pin_groups_dic[pin_group_name] = self.pin_groups_dic[pin_group_name] + new_pins
        else:
            self.pin_groups_dic[pin_group_name] = new_pins

    def pin_to_world(self):
        """Pins all items in users selection to a world locator"""
        selection = get_selection()
        driven = get_selection()
        driver = create_world_locator()

        pin_group_name = driver +"_pcGroup"

        new_pins = []

        for driven_item in driven:
            new_pin = Pin(self.pin_identifier_str)
            new_pin.create(driver,
                            driven_item, 
                            pin_group_name = pin_group_name,
                            mo = True)

            print new_pin.pin_identifier_str
            print new_pin.parent_constraint_pin
            print new_pin.driven_item
            print new_pin.pin_group_name
            new_pins.append(new_pin)

        if pin_group_name in self.pin_groups_dic.keys():
            self.pin_groups_dic[pin_group_name] = self.pin_groups_dic[pin_group_name] + new_pins
        else:
            self.pin_groups_dic[pin_group_name] = new_pins

    def pin_hierarchy(self):
        """Creates a hierarchy of pins based on selction order."""
        selection = get_selection()
        driver = selection[0]
        pin_group_name = driver +"_pcGroup"
        if pin_group_name in self.pin_groups_dic.keys():
            pin_group_name = pin_group_name
        if not mc.objExists("PinGuide_World_LOC"):
            loc = create_world_locator()
            #make a world locator if none exists
        else:
            loc = "PinGuide_World_LOC"
        new_pins = []
        for i in range(0,len(selection)-1):
            driver = selection[i]
            driven_PLCs = [selection[i+1]]
            #driven=[]
            for driven_item in driven_PLCs:
                driven_item = mc.pickWalk(driven_item, d = "up")[0]
                #driven.append(parent)
                #driven = parent
            new_pin = Pin(self.pin_identifier_str)
            new_pin.create(driver, driven_item, pin_group_name = pin_group_name, mo = True)
            new_pins.append(new_pin)

        if pin_group_name in self.pin_groups_dic.keys():
            self.pin_groups_dic[pin_group_name] = self.pin_groups_dic[pin_group_name] + new_pins
        else:
            self.pin_groups_dic[pin_group_name] = new_pins
    
    def delete_pin_group(self, pin_group_name):
        """Delete a pin group and the pins it contains within it."""
        pass
        #pins is a list of class objects

        pins = self.pin_groups_dic[pin_group_name]

        for pin in pins:

            pin.delete(pin.parent_constraint_pin)
        
        del self.pin_groups_dic[pin_group_name]

    def delete_pin(self, driven_item):
        """Delete a pin group and the pins it contains within it."""

        parent_constraint_pin = mc.listConnections(driven_item + ".parentConstraint")[0]
        pin_group_name = mc.getAttr(parent_constraint_pin+".pinGroupName")

        pins = self.pin_groups_dic[pin_group_name]
        updated_pins = []
        for pin in pins:
            if pin.parent_constraint_pin == parent_constraint_pin:
                pin.delete(parent_constraint_pin)
            else:
                updated_pins.append(pin)     
        self.pin_groups_dic[pin_group_name] = updated_pins

    def delete_all(self):
        """Delete_all pin objects.
        Note: How should i handle groups vs single pins that dont
        """
        all_pin_constraints = mc.ls("*parentConstraint_guidePin")
        for parent_constraint_pin in all_pin_constraints:
            pass

        self.pin_groups_dic = {}

    def delete_by_name(self, parent_constraint_pin):
        """
        Deletes_all pin objects.
        """
        for pin in self.pins:   
            if pin.parent_constraint_pin == parent_constraint_pin:
                pin.delete(parent_constraint_pin)


class Pin():

    def __init__(self, pin_identifier_str):
        """
        Initialize variables associated with a pin.
        """
        self.pin_identifier_str = pin_identifier_str
        self.parent_constraint_pin = None
        self.driver = None
        self.driven_item = None
        self.pin_group_name = ""

    def cleanup_attributes(self, parent_constraint_pin):
        nodes_for_cleanup=[]
        #pc = "PinGuide_World_LOC_parentConstraint_guidePin"
        a = mc.listConnections(parent_constraint_pin + ".driver")
        b = mc.listConnections(parent_constraint_pin + ".driven")
        for each in [a,b]:
            if each:
                nodes_for_cleanup = nodes_for_cleanup + each
        for node in nodes_for_cleanup:
            if mc.ls(node+".driven"):
                mc.deleteAttr(node+".driven")
            if mc.ls(node+".driver"):
                mc.deleteAttr(node+".driver")

    def delete(self, parent_constraint_pin): 
        """
        Deletes the pin and does clean up.
        parent_constraint_pin - The name of the parent constraint.
        """

        attributes = ["translateX",
        "translateY",
        "translateZ",
        "rotateX",
        "rotateY",
        "rotateZ"]

        pin_group_name  = mc.getAttr(parent_constraint_pin + ".pinGroupName")

        driven_item = mc.listConnections(parent_constraint_pin + ".driven")[0]
        for attribute in attributes:
            utils.break_connection(driven_item + "." + attribute)

        if driven_item.find("_ZERO") != -1: #or whatever pic constraint node we come up with
            print "FOUND ZERO"
            if not mc.objExists("PinGuide_World_LOC"):
                loc = create_world_locator()
            #make a world locator if none exists
            else:
                loc = "PinGuide_World_LOC"
            plc = mc.pickWalk(driven_item, d = "down")[0]
            print plc

            #Create a locator at the target location
            temp_plc_locator = mc.spaceLocator(name = "Temp")
            temp_plc_locator_pc = mc.parentConstraint(plc, temp_plc_locator)[0]
            mc.delete(temp_plc_locator_pc)
            
            temp_constraint_pc =  mc.parentConstraint(temp_plc_locator, plc, mo = True)[0]
            
            zero_reset_pc = mc.parentConstraint(temp_plc_locator, driven_item)[0]

            mc.delete(temp_constraint_pc)
            mc.delete(zero_reset_pc)

            mc.delete(temp_plc_locator)

        self.cleanup_attributes(parent_constraint_pin)
        mc.delete(parent_constraint_pin)
    
    def create(self, driver=None, driven_item=None, pin_group_name = "", mo=True):
        """
        Creates a pin connection. Returns the Pin class itself to be stored by the Pins Class. 
        """
        self.pin_group_name = pin_group_name
        #print "create pin_group_name",pin_group_name
        
        failed_driven_items = []
        #for driven_item in driven:
        self.parent_constraint_pin = driven_item + "_parentConstraint_" + self.pin_identifier_str
        #Check that constraints can be made first.
        constraint_availability = self.check_avail(driven_item)

        if constraint_availability:
            #Parent constrain the driver driven objects and make connections.
            parent_constraint_pin = make_pin(driver,
                                             driven_item, 
                                             self.parent_constraint_pin, 
                                             pin_group_name=self.pin_group_name, 
                                             mo=mo)
            self.driver = driver
            self.driven_item = driven_item

        if not constraint_availability:
            #Warn the user and append the driven item to list of fails.
            message = "Constraint on {0} can not be created.".format(driven_item)
            mc.warning(message)
            failed_driven_items.append(driven_item)

        if failed_driven_items:
            mc.confirmDialog(m="Failed to pin {0}".format(failed_driven_items))

        mc.select(driver)
        
        print self.pin_identifier_str
        print self.parent_constraint_pin
        print self.driven_item
        print self.pin_group_name

        return self


    def check_avail(self, transform):
        """
        Checks whether a transform can be constrained by checking its channels are not connected.
        Returns the availability of the transform as a TRUE False boolean.
        """
        atributes = ["translateX",
                        "translateY",
                        "translateZ",
                        "rotateX",
                        "rotateY",
                        "rotateZ"]
        values = []
        for atribute in atributes:
            val = mc.listConnections(transform + "." + atribute)
            values.append(val)
        constraint_availability = True
        for val in values:
            if val:
                constraint_availability = False
                break
        return constraint_availability

def make_pin(driver, driven_item, parent_constraint_pin, pin_group_name = "", mo = True):
    """
    Does the actual creation of a pin
    Variables:

    driver (str) a transform
    driven_item (str) a transform
    parent_constraint_pin (str) a parent constraint node
    pin_group_name (str) the pin group a pin is associated with
    mo (boolean) Whether to maintain the constraints offset.

    """
    parent_constraint_pin = mc.parentConstraint(driver, driven_item, name=parent_constraint_pin, mo = True)[0]

    #Create and connect message nodes for easy identification later
    mc.addAttr(parent_constraint_pin, ln='driver', at='message')
    mc.addAttr(parent_constraint_pin, ln='driven', at='message')
    mc.addAttr(parent_constraint_pin, ln='pinGroupName', dt='string', k = True)
    mc.setAttr(parent_constraint_pin + ".pinGroupName",  pin_group_name, type="string")
    
    if not mc.ls(driver + ".parentConstraint"):
        mc.addAttr(driver, ln='parentConstraint', at='message')

    attr_name = utils.clean_name("drives_"+ driven_item)    

    if not mc.ls(driver + "." + attr_name):
        mc.addAttr(driver, ln= attr_name, at='message')        

    if not mc.ls(driven_item + ".drivenBy"):
        mc.addAttr(driven_item, ln='drivenBy', at='message')    

    if not mc.ls(driven_item + ".parentConstraint"):
        mc.addAttr(driven_item, ln='parentConstraint', at='message')

    mc.connectAttr(driver + ".parentConstraint", parent_constraint_pin + ".driver")
    mc.connectAttr(driven_item + ".parentConstraint", parent_constraint_pin + ".driven")

    return parent_constraint_pin

def get_selection():
    """Get the users current selection."""
    selection = mc.ls(sl = True)
    return selection

def create_world_locator():
    """Make a world locator if none exists."""
    loc = "PinGuide_World_LOC"
    if not mc.objExists("PinGuide_World_LOC"):
        mc.spaceLocator(n = loc)[0]
    return loc

def orient_plc_to_joint(plc):
    """Orient a placer joint to match the joint it drives"""

    jnt = plc.split("_PLC")[0]
    
    temp_plc_locator = mc.spaceLocator(name = "Temp")
    temp_plc_locator_pc = mc.parentConstraint(jnt, temp_plc_locator)[0]
    mc.delete(temp_plc_locator_pc)
    #reset the driven zero grp back to zero while the PLC is locked in place
    try:
        zero_reset_pc = mc.orientConstraint(temp_plc_locator,plc)
        mc.delete(zero_reset_pc)
    except:
        mc.warning("Aborted - Failed to Orient - Chanels unavailable:")
    mc.delete(temp_plc_locator)
    
def orient_plcs_to_joint():
    """Wrapper tool for easy use of orient_plc_to_joint()"""
    selection = get_selection()
    for plc in selection:
        if plc.find("_PLC")!= -1:
            orient_plc_to_joint(plc)
    mc.select(selection)