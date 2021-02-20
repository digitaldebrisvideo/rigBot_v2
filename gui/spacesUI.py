from Qt import QtWidgets as wdg
from Qt import QtGui as gui
from Qt import QtCore as qt

import maya.cmds as mc
import maya.mel as mm

import rigBot
from rigBot.gui import mayaWidget
from rigBot.gui import spaces_ui
from rigBot import env
from rigBot import utils
from rigBot import spaces
from rigBot import data

from functools import partial

import getpass
import inspect

import os
import pydoc

class SpacesUI(mayaWidget.MayaWidget):

    update_it = True

    def __init__(self, parent=None, ignore_missing=False, label=''):
        mayaWidget.MayaWidget.__init__(self, parent=parent)

        title = 'spaces_UI'

        self.ui = spaces_ui.Ui_export_form()
        self.ui.setupUi(self)
        self.setObjectName(title)

        mayaWidget.set_icon(self.ui.help_btn, 'info_24x24.png')
        mayaWidget.set_icon(self.ui.icon_label, 'logo_36x36.png')

        self.ui.help_btn.released.connect(rigBot.help)
        self.resize(445, 720)

        self.ui.splitter.setStretchFactor(1,1)
        self.ui.splitter.setStretchFactor(0,0)
        self.ui.splitter.setCollapsible(1,0)
        self.ui.splitter.setCollapsible(0,0)
        self.ui.splitter.setSizes([0,100])

        self.ui.space_tree = SpaceTreeWidget(self.ui.layoutWidget_2)
        self.ui.space_tree.setDragDropMode(wdg.QAbstractItemView.InternalMove)
        self.ui.space_tree.setSelectionBehavior(wdg.QAbstractItemView.SelectRows)
        self.ui.space_tree.setColumnCount(2)
        self.ui.space_tree.setObjectName("space_tree")
        self.ui.space_tree.headerItem().setText(0, "Label")
        self.ui.space_tree.headerItem().setText(1, "Driver")

        #self.ui.space_tree.headerItem().setText(2, "")
        self.ui.space_tree.header().setVisible(True)
        self.ui.space_tree.header().setDefaultSectionSize(80)
        self.ui.space_tree.header().setStretchLastSection(False)
        self.ui.verticalLayout_4.addWidget(self.ui.space_tree)

        self.ui.space_tree.parent_ui = self

        self.ui.space_tree.header().setSectionResizeMode(0, wdg.QHeaderView.Stretch)
        self.ui.space_tree.header().setSectionResizeMode(1, wdg.QHeaderView.Stretch)

        self.ui.horizontalLayout_3 = wdg.QHBoxLayout()
        self.ui.add_btn = wdg.QPushButton(self.ui.layoutWidget_2)
        self.ui.add_btn.setMaximumSize(qt.QSize(16777215, 18))
        self.ui.add_btn.setObjectName("add_btn")
        self.ui.add_btn.setContextMenuPolicy(qt.Qt.ActionsContextMenu)
        self.ui.add_btn.setToolTip('Add new space. (Right-click for more options.)')
        self.ui.horizontalLayout_3.addWidget(self.ui.add_btn)

        self.ui.remove_btn = wdg.QPushButton(self.ui.layoutWidget_2)
        self.ui.remove_btn.setMaximumSize(qt.QSize(16777215, 18))
        self.ui.remove_btn.setObjectName("remove_btn")
        self.ui.horizontalLayout_3.addWidget(self.ui.remove_btn)
        self.ui.remove_btn.setToolTip('Remove selected space.')

        self.ui.verticalLayout_4.addLayout(self.ui.horizontalLayout_3)

        self.ui.set_btn = wdg.QPushButton(self.ui.layoutWidget_2)
        self.ui.set_btn.setMaximumSize(qt.QSize(16777215, 18))
        self.ui.set_btn.setObjectName("set_btn")
        self.ui.verticalLayout_4.addWidget(self.ui.set_btn)
        self.ui.set_btn.setToolTip('Set driver node for selected space.')

        self.ui.set_btn.setText('Set Driver')
        self.ui.add_btn.setText('Add Space')
        self.ui.remove_btn.setText('Remove Space')

        self.ui.space_tree.setStyleSheet('QTreeWidget{border: none;}')

        # connections
        #self.ui.space_tree.currentItemChanged.connect(self.add_button)
        self.ui.variant_cmb.currentIndexChanged.connect(self.set_variant)
        self.ui.node_list.itemSelectionChanged.connect(self.populate_spaces_info)
        self.ui.const_btn.released.connect(self.set_const_node)

        self.ui.space_tree.itemChanged.connect(self.update_space_args)
        self.ui.split_chx.stateChanged.connect(self.update_space_args)
        self.ui.default_cmb.currentIndexChanged.connect(self.update_space_args)
        self.ui.const_line.returnPressed.connect(self.update_space_args)

        self.ui.export_btn.released.connect(self.save_spaces)

        #self.ui.list_model_btn.released.connect(self.list_all_space_nodes)
        self.ui.list_btn.released.connect(self.add_selected_nodes)
        self.ui.list_model_btn_2.released.connect(self.remove_space_tag)

        self.ui.set_btn.released.connect(self.set_driver_node)
        self.ui.add_btn.released.connect(self.add_space_item)
        self.ui.remove_btn.released.connect(self.remove_space)

        mayaWidget.setColor(self.ui.export_btn, button_only=True)

        # actionms
        item = wdg.QAction(self)
        item.setText('Select Highlighted Nodes')
        item.triggered.connect(self.select_nodes_in_scene)
        self.ui.node_list.addAction(item)

        item = wdg.QAction(self)
        item.setText('Highlight Selected Nodes')
        item.triggered.connect(self.highlight_selected_nodes)
        self.ui.node_list.addAction(item)

        item = wdg.QAction(self)
        item.setText('Set default const node')
        item.triggered.connect(self.set_default_const_node)
        self.ui.const_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Add Parent Space')
        item.triggered.connect(partial(self.add_preset_space, 'parent'))
        self.ui.add_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Add Cog Space')
        item.triggered.connect(partial(self.add_preset_space, 'cog'))
        self.ui.add_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Add World Space')
        item.triggered.connect(partial(self.add_preset_space, 'world'))
        self.ui.add_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Add True World Space')
        item.triggered.connect(partial(self.add_preset_space, 'trueWorld'))
        self.ui.add_btn.addAction(item)

        self.list_all_space_nodes()
        self.populate_spaces_info()

    def initialize_ui_widgets(self):

        self.set_variant_widget()
        self.list_all_space_nodes()

    def set_variant_widget(self):
        """Set the variant from UI and reset all ui and build list"""

        self.asset = env.get_asset()
        self.variant = env.get_variant()
        self.variants = env.list_variants(verbose=0) or []

        try:
            self.ui.variant_cmb.currentIndexChanged.disconnect(self.set_variant)
        except:
            pass

        self.ui.variant_cmb.clear()
        self.ui.asset_label.setText('Asset: Not Set!')

        if self.asset:
            self.ui.asset_label.setText('Asset: '+self.asset)

            self.ui.variant_cmb.addItems(self.variants)

            try:
                idx = self.variants.index(self.variant)
                self.ui.variant_cmb.setCurrentIndex(idx)
            except:
                pass

        self.ui.variant_cmb.currentIndexChanged.connect(self.set_variant)

    def set_variant(self):
        env.set_variant(self.ui.variant_cmb.currentText())

    def list_all_space_nodes(self):

        nodes = [n.split('.')[0] for n in mc.ls('*.tagSpaces')]
        nodes.sort()
        self.ui.node_list.clear()
        self.ui.node_list.addItems(nodes)

    def add_selected_nodes(self):

        nodes = mc.ls(sl=1)

        item_texts = []
        for i in range(self.ui.node_list.count()):
            item_texts.append(self.ui.node_list.item(i).text())

        for node in nodes:
            if node in item_texts:
                nodes.remove(node)

            if not mc.objExists(node+'.tagSpaces'):
                spc = spaces.Space(node)
                spc.set_const_node()

        self.ui.node_list.addItems(nodes)
        self.highlight_selected_nodes()

    def select_nodes_in_scene(self):

        nodes = self.ui.node_list.selectedItems()
        if not nodes:
            return

        nodes = [i.text() for i in nodes]
        ex_nodes = mc.ls(nodes)

        if ex_nodes:
            if not len(nodes) == len(ex_nodes):
                mc.warning('Some nodes do not exist in scene!')
            mc.select(ex_nodes)

    def highlight_selected_nodes(self):

        sel = mc.ls(sl=1)
        items_to_select = []
        item_texts = []

        for node in sel:

            items = self.ui.node_list.findItems(node, qt.Qt.MatchExactly)
            if not items:
                continue
            items_to_select.append(items[0])
            item_texts.append(items[0].text())

        item_to_set=None
        for i in range(self.ui.node_list.count()):
            item = self.ui.node_list.item(i)
            self.ui.node_list.setItemSelected(item, False)

            if items_to_select:
                if item.text() in item_texts and item_to_set is None:
                    item_to_set = item

        if not items_to_select:
            return

        self.ui.node_list.setCurrentItem(item_to_set, True)
        for item in items_to_select:
            self.ui.node_list.setItemSelected(item, True)

        if item_to_set:
            self.ui.node_list.scrollToItem(item_to_set, wdg.QAbstractItemView.PositionAtTop)

    def remove_space_tag(self):

        nodes = self.ui.node_list.selectedItems()
        if not nodes:
            return

        nodes = [i.text() for i in nodes]
        ex_nodes = mc.ls(nodes)

        if not ex_nodes:
            return

        if ex_nodes:
            if not len(nodes) == len(ex_nodes):
                mc.warning('Some nodes do not exist in scene!')

        if len(ex_nodes) > 1:
            msg = 'Are you sure you want to remove these space tags?\n' +\
                  '\nNodes:  '+'\n             '.join(ex_nodes)

        elif len(ex_nodes) == 1:
            msg = 'Are you sure you want to remove this space tag?\n' +\
                  '\nNode:  '+ex_nodes[0]

        result = mc.confirmDialog( title='Remove Space Tag',
            icon='warning',
            message=msg,
            button=['Yes','No'],
            defaultButton='Yes',
            cancelButton='No',
            dismissString='No' )

        if result =='No':
            return

        for node in ex_nodes:
            if mc.objExists(node+'.tagSpaces'):
                mc.setAttr(node+'.tagSpaces', l=0)
                mc.setAttr(node+'.tagSpaces', '', type='string')
                #mc.deleteAttr(node+'.tagSpaces')

                items = self.ui.node_list.findItems(node, qt.Qt.MatchExactly)
                if items:
                    idx = self.ui.node_list.row(items[0])
                    self.ui.node_list.takeItem(idx)

    def set_default_cmb(self, spaces_list, default_value):

        try:
            self.ui.default_cmb.currentIndexChanged.disconnect(self.update_space_args)
        except:
            pass

        self.ui.default_cmb.clear()
        self.ui.default_cmb.addItems([s[0] for s in spaces_list])
        self.ui.default_cmb.setCurrentIndex(0)

        if default_value > 0:
            self.ui.default_cmb.setCurrentIndex(default_value)

        self.ui.default_cmb.currentIndexChanged.connect(self.update_space_args)

    def populate_spaces_info(self):

        self.update_it=False

        self.ui.const_line.setText('')
        self.ui.default_cmb.clear()
        self.ui.split_chx.setChecked(0)
        self.ui.space_tree.clear()

        self.ui.add_btn.setEnabled(0)
        self.ui.set_btn.setEnabled(0)
        self.ui.remove_btn.setEnabled(0)
        self.ui.groupBox.setEnabled(0)
        self.ui.space_tree.setEnabled(0)

        node = self.ui.node_list.selectedItems()
        if len(node) == 1 :
            node = node[0].text()
        else:
            return

        self.ui.add_btn.setEnabled(1)
        self.ui.set_btn.setEnabled(1)
        self.ui.remove_btn.setEnabled(1)
        self.ui.groupBox.setEnabled(1)
        self.ui.space_tree.setEnabled(1)

        if not mc.objExists(node+'.tagSpaces'):
            return

        data = mc.getAttr(node+'.tagSpaces')

        try:
            data = eval(data)
        except:
            return

        const_node = data.get('const_node')
        spaces_list = data.get('spaces')
        default_value = data.get('default_value')
        split = data.get('split')

        for space_enum in spaces_list:
            self.add_space_item(space_enum[0], space_enum[1])

        self.set_default_cmb(spaces_list, default_value)
        self.ui.const_line.setText(const_node)
        self.ui.split_chx.setChecked(split)

        self.update_it=True

    def set_default_const_node(self):

        node = self.ui.node_list.currentItem()
        if not node:
            return

        node = node.text()
        if not mc.objExists(node):
            mc.warning(node +'does not exist!')

        spc = spaces.Space(node)
        spc.set_const_node()

        self.ui.const_line.setText(spc.const_node)

    def add_space_item(self, label='newSpace', driver=''):

        item = wdg.QTreeWidgetItem()
        item.setText(0, label)
        item.setText(1, driver)

        item.setFlags(qt.Qt.ItemIsSelectable | qt.Qt.ItemIsEnabled | qt.Qt.ItemIsEditable | qt.Qt.ItemIsDragEnabled)
        item.setSizeHint(0, qt.QSize (15, 15))

        if not driver:
            item.setText(1, 'C_root_JNT')

        self.ui.space_tree.addTopLevelItem(item)
        self.update_space_args()

    def add_preset_space(self, space_type):

        node = self.ui.node_list.currentItem()
        if not node:
            return

        node = node.text()
        if not mc.objExists(node):
            mc.warning(node +'does not exist!')

        drv_node = None
        if space_type == 'parent':
            drv_node = node+'_ZERO'
            if not mc.objExists(drv_node):
                drv_node = utils.get_parent(self.const_node)

        elif space_type == 'world':
            drv_node = 'parts_GRP'

        elif space_type == 'trueWorld':
            drv_node = 'noXform_GRP'

        elif space_type == 'cog':
            drv_node = 'C_cog_space_GRP'

        if drv_node:
            self.add_space_item(space_type, drv_node)

    def set_driver_node(self):

        sel = mc.ls(sl=1)
        if not sel:
            mc.warning('Nothing selected!')
            return

        if not mc.objExists(sel[0]+'.translate'):
            mc.warning('Node must be a transform or a joint!')
            return

        item = self.ui.space_tree.currentItem()
        if not item:
            mc.warning('No space item selected!')
            return

        item.setText(1, sel[0])

    def set_const_node(self):

        sel = mc.ls(sl=1)
        if not sel:
            mc.warning('Nothing selected!')
            return

        if not mc.objExists(sel[0]+'.translate'):
            mc.warning('Node must be a transform or a joint!')
            return

        self.ui.const_line.setText(sel[0])
        self.update_space_args()

    def remove_space(self):

        item = self.ui.space_tree.currentItem()
        if not item:
            mc.warning('No space item selected!')

        msg = 'Are you sure you want to remove this space?'
        result = mc.confirmDialog( title='Remove Space Enum',
                                icon='warning',
                                message=msg,
                                button=['Yes','No'],
                                defaultButton='Yes',
                                cancelButton='No',
                                dismissString='No' )

        if result =='No':
            return

        idx = self.ui.space_tree.indexOfTopLevelItem(item)
        self.ui.space_tree.takeTopLevelItem(idx)
        self.ui.space_tree.setCurrentItem(None)

        self.update_space_args()

    def update_space_args(self):

        node = self.ui.node_list.currentItem()
        if not node:
            return

        node = node.text()
        if not mc.objExists(node):
            mc.warning(node +'does not exist!')

        const_node = self.ui.const_line.text()
        split = self.ui.split_chx.isChecked()
        default_value = self.ui.default_cmb.currentIndex()

        spaces_list = []
        for i in range(self.ui.space_tree.topLevelItemCount()):
            item = self.ui.space_tree.topLevelItem(i)
            spaces_list.append([item.text(0), item.text(1)])

        self.set_default_cmb(spaces_list, default_value)

        if self.update_it:

            # some checks
            if not spaces_list:
                mc.warning('No valid spaces! Cannot set.')
                return

            if not const_node:
                mc.warning('No valid const node! Cannot set.')
                return

            if not default_value:
                default_value = 0

            split = bool(split)

            spc = spaces.Space(node)
            spc.set_spaces(spaces_list)
            spc.set_const_node(const_node)
            spc.set_default_value(default_value)
            spc.set_split(split)

    def save_spaces(self):

        invalid_nodes = []
        nodes = [n.split('.')[0] for n in mc.ls('*.tagSpaces')]

        for n in nodes:
            try:
                space_data = eval(mc.getAttr(n+'.tagSpaces'))
                spaces_list = space_data.get('spaces')

                if not spaces_list:
                    invalid_nodes.append(n)
                    continue

                if not mc.objExists(space_data.get('const_node')):
                    invalid_nodes.append(n)
                    continue

                non_existent_drivers = [n[1] for n in spaces_list if not mc.objExists(n[1])]
                if non_existent_drivers:
                    invalid_nodes.append(n)
                    continue

            except:
                invalid_nodes.append(n)

        if invalid_nodes:
            try:
                invalid_nodes = list(set(mc.ls(invalid_nodes)))
                for n in invalid_nodes:
                    mc.setAttr(n+'.tagSpaces', l=0)
                    mc.setAttr(n+'.tagSpaces', '', type='string')
            except:
                invalid_nodes = []


            '''
            invalid_nodes = list(set(invalid_nodes))

            msg = 'Some nodes have invalid space tags. Export and skip these anyway?'
            msg += '\nNodes:  '+'\n             '.join(invalid_nodes)

            result = mc.confirmDialog( title='Invalid space tags found.',
                                            icon='warning',
                                            message=msg,
                                            button=['Yes','No'],
                                            defaultButton='Yes',
                                            cancelButton='No',
                                            dismissString='No' )

            if result == 'No':
                return

            for n in invalid_nodes:
                if n in nodes:
                    nodes.remove(n)
            '''

        data.save('spaces', nodes=nodes)






    '''
    def add_button(self):

        return

        for idx in range(self.ui.space_tree.topLevelItemCount()):
            self.__item = self.ui.space_tree.topLevelItem(0)
            btn = self.ui.space_tree.itemWidget(self.__item, 2)
            if btn:
                self.__item = self.ui.space_tree.takeTopLevelItem(idx)
                self.ui.space_tree.insertTopLevelItem(idx, self.__item)

        item = self.ui.space_tree.currentItem()

        if not item:
            return

        btn = wdg.QPushButton('Set Driver')
        btn.setParent(item)
        btn.setMaximumHeight(15)
        btn.setToolTip('Set driver node')
        self.ui.space_tree.setItemWidget(item, 2, btn)
    '''



class SpaceTreeWidget(wdg.QTreeWidget):

    parent_ui = None

    def dropEvent(self, event):

        item =  self.currentItem()
        wdg.QTreeWidget.dropEvent(self, event)

        self.setCurrentItem(item)

        if self.parent_ui:
            #self.parent_ui.add_button()
            self.parent_ui.update_space_args()


