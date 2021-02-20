import maya.cmds as mc

from functools import partial
from rigBot.gui import mayaWidget
from rigBot import pinGuides
from rigBot.gui import pinGuidesDialog_ui #this is the auto generated code

import pprint

from Qt import QtGui
from Qt import QtCore
from Qt import QtWidgets

#Connect the functions found in pinGuides.py

class PinGuidesDialogUI(mayaWidget.MayaWidget):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, nodes=[], ignore_missing=False, label=''):
        mayaWidget.MayaWidget.__init__(self, parent=None)

        '''
        class RemapDialog(QtWidgets.QDialog):
            """Remap UI for settind hand pose values intreractively"""

            def __init__(self, nodes=[], ignore_missing=False, label=''):
                super(Remap, self).__init__(mayaWidget.maya_main_window)
        '''
        title = 'pinGuides'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.pins = pinGuides.Pins()

        #self.ui = control_ui.Ui_ClusterUI()
        self.ui = pinGuidesDialog_ui.Ui_RemapUI()
        self.ui.setupUi(self)
        self.setObjectName(title)

        header = self.ui.node_tree.header()

        header.setSectionResizeMode(0, header.Stretch)
        header.setSectionResizeMode(1, header.Stretch)
        header.resizeSection(1, 30)
        #Connect buttons to functions of the ui
        self.ui.pinWorldBtn.released.connect(self.pinWorld)
        self.ui.pinHierarchyBtn.released.connect(self.pinHierarchy)
        self.ui.pinParentBtn.released.connect(self.pinParent)
        self.ui.delSelectedBtn.released.connect(self.delSelected)
        self.ui.deleteAllBtn.released.connect(self.deleteAll)
        self.ui.refreshBtn.released.connect(self.refresh)
        self.ui.printBtn.released.connect(self.printPins)
        self.ui.orientPlcsBtn.released.connect(self.orientPlcs)

        if label:
            self.setWindowTitle(label)
        #Update the tree node with available pin constraints.
        self.pins.identify()
        self.update_tree()
    '''
    def cancel(self):
        """Cancel out of this UI"""

        self.mapping = {}
        self.deleteLater()
    '''
    def update_tree(self):
        """
        Clear the node tree and create update it with the information gathered from the
        pins.pin_groups_dic
        """

        self.tableWidget = self.ui.node_tree
        self.tableWidget.clear()

        #Good for debugging the contents of a pin
        #for pin_group_name in self.pins.pin_groups_dic.keys():
        #   pins = self.pins.pin_groups_dic[pin_group_name]

            #for pin in pins:

                #print pin.driver
                #print pin.driven_item
                #print pin.pin_group_name

        for pin_group_name in self.pins.pin_groups_dic.keys():
            pins = self.pins.pin_groups_dic[pin_group_name]
            #Add a Pin Group Item Parent.
            row_index = 0
            item = QtWidgets.QTreeWidgetItem(pin_group_name)
            item.setText(0,pin_group_name)
            self.tableWidget.setItemWidget(item, 0, self.tableWidget)
            item.setText(1,"Pin Group")

            for pin in pins:
                #Add associated pins under the PinGroup Item.
                item2 = QtWidgets.QTreeWidgetItem(item, 0)#unicode("item {0} {1}").format("k","x")
                item2.setText(0, pin.driver)
                #print pin.driven_item
                item2.setText(1, pin.driven_item)

                parentItem =item
                #help(item)
                parentItem.addChild(item2)

            self.tableWidget.addTopLevelItem(item)
            row_index += 1

    def orientPlcs(self):
        pinGuides.orient_plcs_to_joint()

    def pinWorld(self):
        self.pins.pin_to_world()
        self.update_tree()

    def pinHierarchy(self):
        self.pins.pin_hierarchy()
        self.update_tree()

    def pinParent(self):
        self.pins.pin_to_parent()
        self.update_tree()

    def printPins(self):
        """Useful for debugging."""
        for pin_group_name in self.pins.pin_groups_dic.keys():
            pins = self.pins.pin_groups_dic[pin_group_name]

            for pin in pins:
                print pin.driver
                print pin.driven_item
                print pin.pin_group_name

    def get_selected_items(self):
        """Get the selected tree items."""

        items = self.ui.node_tree.selectedItems() or []
        #print "selected = ", items
        return items

    def delSelected(self):
        """
        Delete user selected items from the ui.
        """
        items = self.get_selected_items()

        if items:
            for item in items:
                #Figure out what if were dealing with a group or parent constraint
                #If pcGroup ..
                print item.text(0)
                if item.text(0).find("pcGroup") !=-1:
                    print "found pcGroup"
                    pin_group_name = item.text(0)
                    #print "Found a group,",pin_group_name
                    self.pins.delete_pin_group(pin_group_name)
                else:
                    driven_item = item.text(1)
                    print "not a pin group"
                    self.pins.delete_pin(driven_item)


        self.update_tree()

    def deleteAll(self):
        self.pins.delete_all()
        self.update_tree()

    def refresh(self):

        self.pins.identify()
        self.ui.node_tree.clear()
        self.update_tree()


qt_widget_object = None

def run(dockable=True, **kwargs):
    """
    This is boiler plate code for launching your dockable UI,
    Copy and paste this into your ui module. then change the className from MayaWidget
    to whatever your class name is.

    UIs using this run wrapper require your UI class to inherit the MayaWidget
    class that is defined above, in this module.

    USAGE:
        import myGui
        myGui.run()

        (OR)
        myGui.run(dockable=False)

    RETURNS:
        object instance of your qt ui

    """

    #try:
    if dockable:
        try:
            global qt_widget_object
            qt_widget_object.run(floating=True)

        except:
            qt_widget_object = PinGuidesDialogUI(**kwargs)
            qt_widget_object.run(floating=True)

    else:
        qt_widget_object = PinGuidesDialogUI(**kwargs)
        qt_widget_object.show()

    return qt_widget_object

    #except Exception as e:
    #    raise RuntimeError(e)
