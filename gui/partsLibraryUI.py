# encoding=utf8
from Qt import QtWidgets as wdg
from Qt import QtGui as gui
from Qt import QtCore as qt

import maya.cmds as mc
import maya.mel as mm

from rigBot.gui import mayaWidget
from rigBot.gui import partsLibrary_ui
from rigBot import partsLibrary
from rigBot import utils
from functools import partial

import getpass
import re
import os

#mayaWidget.compile('partsLibrary.ui')
reload(partsLibrary_ui)

class PartsLibraryUI(wdg.QDialog):

    def __init__(self, parts_data={}, parent=None):
        if not parent:
            parent = mayaWidget.maya_main_window
        super(PartsLibraryUI, self).__init__(parent)

        self.part_to_build = None
        self.is_assembly = False
        self.needs_reload = False

        if parts_data:
            self.all_cat_parts, self.all_parts, self.parts_data = parts_data
        else:
            self.all_cat_parts, self.all_parts, self.parts_data = get_library_data()

        self.current_mode = True

        title = 'partsLibrary_UI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = partsLibrary_ui.Ui_PartsLibrary()
        self.ui.setupUi(self)
        self.setObjectName(title)

        self.ui.cat_btn.released.connect(partial(self.populate_tree, cat_mode=True))
        self.ui.alpha_btn.released.connect(partial(self.populate_tree, cat_mode=False))
        self.ui.ass_chx.toggled.connect(self.populate_tree)
        self.ui.part_chx.toggled.connect(self.populate_tree)
        self.ui.add_btn.released.connect(self.add_part)
        self.ui.splitter.setStretchFactor(0,0)
        self.ui.splitter.setStretchFactor(1,1)
        self.ui.treeWdg.itemSelectionChanged.connect(self.update_docs)
        self.ui.treeWdg.itemDoubleClicked.connect(self.dbl_add_part)
        self.ui.alpha_btn_3.released.connect(self.clear_search)
        self.ui.lineEdit_3.textChanged.connect(self.search_filter)

        item = wdg.QAction(self)
        item.setText('Reload All Parts')
        item.triggered.connect(partial(self.populate_tree, reload_parts=True))
        #self.ui.treeWdg.addAction(item)

        self.populate_tree()
        self.resize(1000, 750)

        self.ui.cancel_btn.released.connect(self.deleteLater)
        self.ui.browse_btn.released.connect(self.browse_path)

    def clear_search(self):
        self.ui.lineEdit_3.setText('')

    def search_filter(self):

        def get_subtree_nodes(tree_widget_item):
            """Returns all QTreeWidgetItems in the subtree rooted at the given node."""
            nodes = []
            nodes.append(tree_widget_item)
            for i in range(tree_widget_item.childCount()):
                nodes.extend(get_subtree_nodes(tree_widget_item.child(i)))
            return nodes

        def get_all_items(tree_widget):
            """Returns all QTreeWidgetItems in the given QTreeWidget."""
            all_items = []
            for i in range(tree_widget.topLevelItemCount()):
                top_item = tree_widget.topLevelItem(i)
                all_items.extend(get_subtree_nodes(top_item))
            return all_items

        text = self.ui.lineEdit_3.text().lower()
        for item in get_all_items(self.ui.treeWdg):
            if text in item.text(0).lower():
                item.setHidden(False)
                parent = item.parent()
                if parent:
                    parent.setHidden(False)
            else:
                item.setHidden(True)


    def browse_path(self):
        """Brose to path"""

        utils.browse_path(os.path.dirname(self.ui.path_line.text()))

    def update_docs(self):

        items = self.ui.treeWdg.selectedItems()
        self.ui.docs.setText('')

        if not items:
            return

        item = items[0]
        self.ui.docs.setText(item.doc_label)
        try:
            self.ui.path_line.setText(item.file_path)
        except:
            self.ui.path_line.setText('')

    def populate_tree(self, dummy=False, cat_mode=None, reload_parts=False):

        user_name = getpass.getuser()

        if cat_mode is None:
            cat_mode = self.current_mode

        # Load all part modules and sort them
        all_parts = [p for p in partsLibrary.list_parts(verbose=0) if p != ['emptyPart', 'standardPart']]

        # add categories
        self.ui.treeWdg.clear()

        if not self.parts_data or reload_parts:
            self.all_cat_parts, self.all_parts, self.parts_data = get_library_data()

        if cat_mode:

            self.current_mode = True
            categories = self.all_cat_parts.keys()
            categories.sort()
            for category in categories:

                parts = self.all_cat_parts[category]

                if category == 'assemblies' and not self.ui.ass_chx.isChecked():
                    continue
                elif category != 'assemblies' and not self.ui.part_chx.isChecked():
                    continue

                cat_item = wdg.QTreeWidgetItem()
                cat_item.setSizeHint(0, qt.QSize(10, 17))
                cat_item.setText(0, category)
                cat_item.command_str = None
                cat_item.file_path = ''
                cat_item.doc_label = ''
                cat_item.is_assembly = 'groupItem'

                tool_tip = ''

                cat_item.setToolTip(0, tool_tip)
                cat_item.setForeground(0, gui.QColor('gray'))

                self.ui.treeWdg.addTopLevelItem(cat_item)

                # Now add module
                for part in parts:
                    instance, name, category, file_path, doc = self.parts_data[part]

                    part = str(name)
                    label = str(name)

                    item = wdg.QTreeWidgetItem()
                    item.setSizeHint(0, qt.QSize(10, 17))
                    item.setText(0, label)
                    item.part = part
                    item.file_path = file_path
                    item.setToolTip(0, 'FILE PATH: '+file_path)

                    if 'IMPORT ERROR' in label:
                        item.setForeground(0, gui.QColor('#ce4e94'))

                    elif category == 'assemblies':
                        item.setForeground(0, gui.QColor('#f2ed9b'))

                    if category == 'assemblies':
                        item.is_assembly = True
                    else:
                        item.is_assembly = False

                    if user_name in file_path:
                        item.setForeground(0, gui.QColor(mayaWidget.pink_color))

                    elif 'ASSET' in category:
                        item.setForeground(0, gui.QColor(mayaWidget.blue_color))

                    item.doc_label = doc
                    cat_item.addChild(item)
                    cat_item.setExpanded(1)


        else:

            self.current_mode = False
            for part in self.all_parts:
                instance, name, category, file_path, doc = self.parts_data[part]

                part = str(name)
                label = str(name)

                if category == 'assemblies' and not self.ui.ass_chx.isChecked():
                    continue
                elif category != 'assemblies' and not self.ui.part_chx.isChecked():
                    continue

                if category == 'assemblies':
                    label += ' - ASSEMBLY'

                item = wdg.QTreeWidgetItem()
                item.setSizeHint(0, qt.QSize(10, 17))
                item.setText(0, label)
                item.part = part
                item.file_path = file_path
                item.setToolTip(0, 'FILE PATH: '+file_path)

                if category == 'assemblies':
                    item.is_assembly = True
                else:
                    item.is_assembly = False

                if 'IMPORT ERROR' in label:
                    item.setForeground(0, gui.QColor('#ce4e94'))

                elif category == 'assemblies':
                    item.setForeground(0, gui.QColor('#f2ed9b'))

                if user_name in file_path:
                    item.setForeground(0, gui.QColor(mayaWidget.pink_color))

                elif 'ASSET' in category:
                    item.setForeground(0, gui.QColor(mayaWidget.blue_color))

                item.doc_label = doc
                self.ui.treeWdg.addTopLevelItem(item)

        self.search_filter()

    def dbl_add_part(self):
        self.add_part(v=False)

    def add_part(self, v=True):

        items = self.ui.treeWdg.selectedItems()
        if items:
            if items[0].is_assembly == 'groupItem':
                if v:
                    mc.warning('This is just a label. Choose a part or assembly!')
                return

            self.is_assembly = items[0].is_assembly
            self.part_to_build =  items[0].text(0).split(' ')[0]
            self.deleteLater()

'''
self = PartsLibraryUI()
self.show()
'''

def get_library_data():

    all_cat_parts = partsLibrary.list_parts(verbose=0, by_category=1)
    all_parts = [p for p in partsLibrary.list_parts(verbose=0)]
    parts_data = {}

    for part in all_parts:
        parts_data[part] = partsLibrary.help(part, verbose=0)

    return all_cat_parts, all_parts, parts_data
