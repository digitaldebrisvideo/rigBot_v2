import maya.cmds as mc
import maya.OpenMaya as om
import maya.OpenMayaAnim as oma

from functools import partial

from rigBot import utils


import maya.cmds as mc

import os
import getpass

from rigBot import env

from rigBot.gui import newPart_ui


from rigBot.gui import mayaWidget
from rigBot import partsLibrary
from functools import partial

from Qt import QtWidgets
from Qt import QtCore


class NewPartUI(mayaWidget.MayaWidget):

    """Remap UI for remapping shape and influences during import"""

    def __init__(self, assembly_mode=False, current_categories=[]):
        super(NewPartUI, self).__init__(mayaWidget.maya_main_window)

        title = 'newPartUI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = newPart_ui.Ui_Form()
        self.ui.setupUi(self)
        self.setObjectName(title)

        self.part_paths = env.get_parts_paths()

        # add all paths and select sanbdbox as default
        user = getpass.getuser()
        self.default_path_idx = 0
        for idx, path in enumerate(self.part_paths):
            if user in path:
                self.default_path_idx = idx

        self.ui.listWidget.addItems(self.part_paths)

        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            self.ui.listWidget.setItemSelected(item, False)

            if not os.access(item.text(), os.W_OK) and user not in item.text():
                item.setFlags(item.flags() & QtCore.Qt.ItemIsSelectable)

        # item = self.ui.listWidget.item(self.default_path_idx)
        # self.ui.listWidget.setCurrentItem(item, True)
        # self.ui.listWidget.setItemSelected(item, True)

        if current_categories:
            self.current_categories = current_categories
        else:
            self.current_categories = partsLibrary.list_parts(verbose=0, by_category=1).keys()
            self.current_categories.sort()

        self.resize(650, 350)


        # add categoris
        self.ui.lineEdit_2.setPlaceholderText('Enter part name')
        self.ui.lineEdit.setPlaceholderText('generic (Right click for current categories)')
        for cat in [c for c in self.current_categories if '- ASSET' not in c]:
            item = QtWidgets.QAction(self)
            item.setText(cat)
            item.triggered.connect(partial(self.ui.lineEdit.setText, cat))
            self.ui.lineEdit.addAction(item)

        self.assembly_mode = assembly_mode
        if self.assembly_mode:
            self.ui.cat_label.hide()
            self.ui.lineEdit.hide()
            self.ui.cat_label_2.setText('Assembly Name:')
            self.ui.lineEdit_2.setPlaceholderText('Enter assembly name')
            self.ui.label_1.setText('Create New Assembly')
            self.ui.label_2.setText('This will save the current guides in scene as an assembly in the specified location. ')
            self.setWindowTitle('Create New Assembly')

        self.ui.cance_btn.released.connect(self.deleteLater)
        self.ui.create_btn.released.connect(self.check_file_path)

        self.output_path = None

    def check_file_path(self):

        self.output_path = None

        cat = self.ui.lineEdit.text() or 'generic'
        if self.assembly_mode:
            cat = 'assemblies'

        file_name = self.ui.lineEdit_2.text()

        if not file_name:
            mc.warning('No name specifed!')
            return

        items = self.ui.listWidget.selectedItems()
        if not items:
            mc.warning('No path selected!')
            return

        asset = env.get_asset() or '%ASSET%NOT%SET%'
        if asset in items[0].text():
            path_to_check = os.path.join(items[0].text(), file_name+'.py')
        else:
            path_to_check = os.path.join(items[0].text(), cat, file_name+'.py')

        if os.path.isfile(path_to_check):
            result = mc.confirmDialog(title='Overwrite Module?',
                            message='{0} already exists. Do you want to replace it?'.format(file_name),
                            button=['Yes','No'],
                            defaultButton='Yes',
                            cancelButton='No',
                            dismissString='No' )

            if result == 'Yes':
                self.output_path = path_to_check
                self.deleteLater()

        else:
            self.output_path = path_to_check
            self.deleteLater()

    def save_to_asset(self):
        self.check_file_path(self.asset_path)


# you need this
qt_widget_object = None
def run(dockable=False, **kwargs):
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

    try:
        if dockable:
            try:
                global qt_widget_object
                qt_widget_object.run(floating=True)

            except:
                qt_widget_object = NewPartUI(**kwargs)
                qt_widget_object.run(floating=True)

        else:
            qt_widget_object = NewPartUI(**kwargs)
            qt_widget_object.show()

        return qt_widget_object

    except Exception as e:
        raise RuntimeError(e)

