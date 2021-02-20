# encoding=utf8

from Qt import QtWidgets as wdg
from Qt import QtGui as gui
from Qt import QtCore as qt

import maya.cmds as mc
import maya.mel as mm

from rigBot.gui import mayaWidget
from rigBot.gui import export_ui
from rigBot import env
from rigBot import utils
from rigBot import data
from functools import partial
import getpass
import rigBot

from rigBot.data import udAttributes
from rigBot.data import sdk
import os

#mayaWidget.compile('export.ui')
reload(export_ui)
reload(data)

class ExportUI(mayaWidget.MayaWidget):

    deformers = data.deformer_types

    def __init__(self, parent=None, ignore_missing=False, label=''):
        mayaWidget.MayaWidget.__init__(self, parent=parent)

        title = 'build_UI'
        #if mc.window(title, q=1, ex=1):
            #mc.deleteUI(title)

        self.ui = export_ui.Ui_export_form()
        self.ui.setupUi(self)
        self.setObjectName(title)

        mayaWidget.set_icon(self.ui.help_btn, 'info_24x24.png')
        mayaWidget.set_icon(self.ui.icon_label, 'logo_36x36.png')

        css = 'QPushButton:!disabled { background-color: #7c5cb7; }'
        self.ui.export_btn.setStyleSheet(css)

        self.ui.filter_btn.toggled.connect(self.toggle_filters_frame)
        self.resize(445, 720)

        self.toggle_filters_frame()

        # Get all checkboxes
        self.checkboxes = [c for c in self.ui.filter_frame.children() if 'QCheckBox' in str(type(c))]
        self.checkboxes = [c for c in self.checkboxes if c.whatsThis()]

        self.ui.help_btn.released.connect(rigBot.help)
        self.ui.all_chx.stateChanged.connect(self.toggle_all_checkboxes)
        self.ui.variant_cmb.currentIndexChanged.connect(self.set_variant)

        self.ui.list_btn.released.connect(self.list_nodes)
        self.ui.list_model_btn.released.connect(partial(self.list_nodes, model_grp=True))

        self.ui.node_list.itemDoubleClicked.connect(self.ui.node_list.selectAll)
        self.ui.data_list.itemDoubleClicked.connect(self.ui.data_list.selectAll)

        self.ui.fix_names_btn.released.connect(self.rename_data_nodes)
        self.ui.fix_all_names_btn.released.connect(partial(self.rename_data_nodes, rename_all=True))

        self.ui.node_list.itemSelectionChanged.connect(self.list_data)
        self.ui.export_btn.released.connect(self.save_data_files)

        self.ui.custom_btn.released.connect(partial(data.save, 'customRig'))
        self.ui.ncloth_btn.released.connect(partial(data.save, 'nCloth'))

        self.ui.stack_btn.released.connect(self.save_stack)

        self.ui.sttrs_btn.released.connect(partial(data.save, data_types='kAttributes'))
        self.ui.ctrls_btn.released.connect(partial(data.save, data_types='controlShapes'))
        self.ui.shaders_btn.released.connect(partial(data.save, data_types='shaders'))

        for chx in self.checkboxes:
            chx.stateChanged.connect(self.list_data)

        self.initialize_ui_widgets()

        # context menus
        item = wdg.QAction(self)
        item.setText('Add Selected Nodes To List')
        item.triggered.connect(partial(self.list_nodes, add=True))
        self.ui.list_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Add Model_GRP Hierarchy To List')
        item.triggered.connect(partial(self.list_nodes, model_grp=True, add=True))
        self.ui.list_model_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Select Highlighted Nodes')
        item.triggered.connect(self.select_nodes)
        self.ui.node_list.addAction(item)

        item = wdg.QAction(self)
        item.setText('Select Highlighted Data Nodes')
        item.triggered.connect(self.select_data)
        self.ui.data_list.addAction(item)

        item = wdg.QAction(self)
        item.setText('Add This Node to Nodes List')
        item.triggered.connect(self.add_to_nodes_lisd)
        self.ui.data_list.addAction(item)

        self.list_data()

    def add_to_nodes_lisd(self):
        self.select_data()
        self.list_nodes(add=True)

    def toggle_filters_frame(self):
        """Toggles the filter widget bvisibility """

        if self.ui.filter_btn.isChecked():
            self.ui.filter_frame.show()
        else:
            self.ui.filter_frame.hide()

    def toggle_all_checkboxes(self):

        state = self.ui.all_chx.isChecked()
        for chx in self.checkboxes:
            chx.stateChanged.disconnect(self.list_data)
            chx.setChecked(state)
            chx.stateChanged.connect(self.list_data)

        self.list_data()

    def initialize_ui_widgets(self):

        self.set_variant_widget()

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

    def list_nodes(self, model_grp=False, add=False):

        if model_grp:
            model_grp = mc.ls('model_GRP', 'model')
            if not model_grp:
                mc.warning('model_GRP not found!')
                return

            if len(model_grp) > 1:
                print model_grp
                mc.warning('Duplicate "model_GRP" nodes in scene!')
                return

            sel = [n for n in [model_grp[0]] + utils.get_children(model_grp[0], ad=1)
                                                        if mc.nodeType(n) =='transform']
        else:
            sel = mc.ls(sl=1, sn=1)
            if not sel:
                mc.warning('Nothing selected!')
                return

        if not add:
            self.ui.node_list.clear()


        all_items = []
        for i in range(self.ui.node_list.count()):
            item = self.ui.node_list.item(i)
            all_items.append(item.text())

        for s in sel:
            if s in all_items:
                mc.warning(s+' is already in the node list!')

        sel = [s for s in sel if s not in all_items]
        if sel:
            self.ui.node_list.addItems(sel)

        self.list_data()

    def select_nodes(self):

        nodes =[i.text() for i in self.ui.node_list.selectedItems() or []]
        nodes = mc.ls([n.split('\n')[0] for n in nodes])

        if not nodes:
            mc.warning('Nodes do not exist!')
            return

        mc.select(nodes)


    def select_data(self):

        existing_nodes = []
        nodes =[i.text() for i in self.ui.data_list.selectedItems() or []]
        nodes = mc.ls([n.split('.')[0] for n in nodes])

        for node in nodes:
            if '->' in node:
                existing_nodes.append(node.split('->')[-1].strip())
            else:
                existing_nodes.append(node.strip())

        nodes = mc.ls(existing_nodes)

        if not nodes:
            mc.warning('Nodes do not exist!')
            return

        mc.select(nodes)

    def list_data(self):

        self.ui.data_list.clear()

        nodes =[i.text() for i in self.ui.node_list.selectedItems() or []]
        nodes = mc.ls(nodes)

        # get data types
        data_types = []
        for chx in self.checkboxes:
            if chx.isChecked():
                data_types.append(chx.whatsThis())

        if 'pose' in data_types:
            data_types.remove('pose')
            data_types.append('pose')

        for data_type in data_types:
            data_nodes = []

            if data_type == 'sdk':
                label = 'Set Driven Keyframes'

            elif data_type == 'udAttributes':
                label = 'User Defined Attributes'

            elif data_type == 'connections':
                label = 'Connections'

            elif data_type == 'constraints':
                label = 'Constraints'

            elif data_type == 'pose':
                label = 'Pose Interpolators'

            else:
                label = data_type[0].upper()+data_type[1:]+'s'

            label_item = wdg.QListWidgetItem(label)
            label_item.setForeground(qt.Qt.darkGray)
            label_item.setBackground(gui.QColor('#353535'))
            label_item.setSizeHint(qt.QSize(10, 17))
            label_item.setFlags(label_item.flags() & ~qt.Qt.ItemIsSelectable)

            if data_type == 'pose':
                data_nodes.extend([n.split('.')[0] for n in mc.ls('*.transPoseInterpolatorDrivers')])
                data_nodes.extend([utils.get_transform(p) for p in mc.ls(type='poseInterpolator')])

            for node in nodes:
                if not mc.objExists(node):
                    continue

                if data_type == 'pose':
                    break

                elif data_type in self.deformers:
                    if data_type == 'lattice':
                        data_nodes.extend(utils.get_deformers(node, 'ffd'))

                    else:
                        data_nodes.extend(utils.get_deformers(node, data_type))

                elif data_type == 'constraints':
                    data_nodes.extend(utils.get_constraints(node))

                elif data_type == 'sdk':
                    data_nodes.extend(sdk.get_data(node).keys())

                elif data_type == 'udAttributes':
                    attr_data = udAttributes.get_data(node)
                    if attr_data:

                        spacer = '\n         .'
                        attrs = attr_data[node]['data'].keys()
                        attrs = spacer.join(attrs)
                        attrs = node+spacer+attrs
                        data_nodes.append(attrs)

                elif data_type == 'connections':

                    attrs = [node+'.'+a for a in mc.listAttr(node, k=1) if '.' not in a]
                    if mc.nodeType(node) == 'blendShape':
                        weight_attrs = [node+'.weight[{0}]'.format(i) for i in range(mc.blendShape(node, q=1, wc=1))]
                        weight_attrs = [node+'.'+mc.aliasAttr(a, q=1) for a in weight_attrs]
                        attrs.extend(weight_attrs)

                    for plug in attrs:
                        if mc.objExists(plug):
                            source = mc.listConnections(plug, p=1, s=1, d=0)
                            if source:
                                if 'Constraint' not in mc.nodeType(source[0].split('.')[0]):
                                    if 'animCurve' not in mc.nodeType(source[0].split('.')[0]):
                                        if 'blendWeighted' not in mc.nodeType(source[0].split('.')[0]):
                                            data_nodes.append('{0} -> {1}'.format(source[0], plug))

            if data_nodes:
                data_nodes  = list(set(data_nodes))
                data_nodes.sort()

                label_item.data_type = 'label'

                self.ui.data_list.addItem(label_item)

                for d in data_nodes:
                    ditem = wdg.QListWidgetItem('   '+d)
                    ditem.data_type = data_type

                    self.ui.data_list.addItem(ditem)

    @utils.undoable
    def rename_data_nodes(self, rename_all=False):

        if rename_all:
            items = []
            for i in range(self.ui.data_list.count()):
                item = self.ui.data_list.item(i)
                items.append(item)
        else:
            items = self.ui.data_list.selectedItems() or []

        for item in items:

            data_node = item.text().strip().replace('->', '')
            if mc.objExists(data_node):
                if mc.nodeType(data_node) in utils.name_conventions.keys():

                    geo = ''

                    if item.data_type == 'constraints':
                        geo = mc.listConnections(data_node+'.constraintParentInverseMatrix')
                        if geo:
                            geo = geo[0]

                    elif item.data_type in self.deformers:
                        geo = mc.deformer(data_node, q=1, g=1)
                        if geo:
                            geo = geo[0].replace('Shape', '')

                    if geo:
                        suffix = utils.get_suffix(mc.nodeType(data_node))

                        new_name = geo+'_'+suffix
                        if data_node != new_name:
                            new_name = utils.get_unique_name('{0}_#_{1}'.format(geo, suffix))

                            new_name = mc.rename(data_node, new_name)
                            item.setText('   '+new_name)

    @utils.undoable
    def save_data_files(self, custom_path=False):

        nodes_dict = {}

        items = self.ui.data_list.selectedItems()
        for item in items:
            data_node = item.text().strip().split('\n')[0]
            data_type = item.data_type
            if '->' in data_node:
                data_node = data_node.split('->')[-1].strip()

            dlist = nodes_dict.get(data_type, [])
            dlist.append(data_node)

            nodes_dict[data_type] = dlist

        for data_type, selection in nodes_dict.items():
            data.save(data_types=data_type, nodes=selection, model=False, custom_path=custom_path)

    def save_stack(self):

        items = [i.text() for i in self.ui.node_list.selectedItems()]
        items = mc.ls(items)
        if items:
            data.save('stack', items)


