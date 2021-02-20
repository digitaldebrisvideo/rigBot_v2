from Qt import QtWidgets as wdg
from Qt import QtGui as gui
from Qt import QtCore as qt

import maya.cmds as mc
import maya.mel as mm

from rigBot import partsLibrary
from rigBot.gui import partsLibraryUI
from rigBot.gui import mayaWidget
from rigBot.gui import guides_ui
from rigBot import env
from rigBot import utils
from rigBot import guide
from functools import partial
import rigBot
from rigBot.gui import pinGuidesDialogUI

import os

reload(partsLibrary)
reload(partsLibraryUI)

class GuidesUI(mayaWidget.MayaWidget):

    def __init__(self, parent=None, ignore_missing=False, label=''):
        mayaWidget.MayaWidget.__init__(self, parent=parent)

        self.parts_data = partsLibraryUI.get_library_data()

        title = 'assetEnv_UI'
        #if mc.window(title, q=1, ex=1):
            #mc.deleteUI(title)

        self.ui = guides_ui.Ui_guides_form()
        self.ui.setupUi(self)
        self.setObjectName(title)

        mayaWidget.set_icon(self.ui.help_btn, 'info_24x24.png')
        mayaWidget.set_icon(self.ui.icon_label, 'logo_36x36.png')

        self.ui.help_btn.released.connect(rigBot.help)
        self.ui.pushButton.setMinimumWidth(245)
        self.resize(445, 720)

        self.parts_menu = wdg.QMenu(self)

        self.ui.add_btn.released.connect(self.add_part_from_lib)
        self.ui.add_btn.setText('Parts Library')

        self.ui.guide_list.itemSelectionChanged.connect(partial(self.build_options_menu, use_selected=True))
        self.ui.guide_list.itemDoubleClicked.connect(self.select_guide)
        self.ui.splitter.setStretchFactor(0,0)
        self.ui.splitter.setStretchFactor(1,1)
        self.ui.guide_list.resize(50, 200)

        self.ui.build_btn.released.connect(self.build_new_guide)
        self.ui.mirror_btn.released.connect(self.mirror_guides)
        self.ui.duplicate_btn.released.connect(self.copy_guides)
        self.ui.delete_btn.released.connect(self.delete_guides)
        self.ui.save_btn.released.connect(guide.save)
        self.ui.load_btn.released.connect(guide.load)

        self.ui.alpha_btn_2.released.connect(partial(self.ui.lineEdit.setText, ''))

        # Utilities
        self.ui.model_btn.released.connect(self.load_model)
        self.ui.pin_guides_btn.released.connect(self.load_pinGuideUi)

        self.ui.lineEdit.textChanged.connect(self.list_guides_in_scene)
        self.ui.lineEdit.textChanged.connect(self.clear_options_menu)

        self.ui.radioButton_3.toggled.connect(self.list_guides_in_scene)
        self.ui.radioButton_4.toggled.connect(self.list_guides_in_scene)
        self.ui.radioButton_5.toggled.connect(self.list_guides_in_scene)

        self.ui.radioButton_3.toggled.connect(self.clear_options_menu)
        self.ui.radioButton_4.toggled.connect(self.clear_options_menu)
        self.ui.radioButton_5.toggled.connect(self.clear_options_menu)

        # Right click actions
        item = wdg.QAction(self)
        item.setText('Create New Part Module')
        item.triggered.connect(self.create_new_part)
        item.triggered.connect(self.refresh_guides_menu)
        self.ui.add_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Create New Assembly From Scene')
        item.triggered.connect(self.save_assembly)
        item.triggered.connect(self.refresh_guides_menu)
        self.ui.add_btn.addAction(item)

        div = wdg.QAction(self)
        div.setSeparator(1)
        self.ui.add_btn.addAction(div)

        item = wdg.QAction(self)
        item.setText('Edit Parts Paths')
        #item.triggered.connect(self.save_assembly)
        #item.triggered.connect(self.refresh_guides_menu)
        self.ui.add_btn.addAction(item)

        div = wdg.QAction(self)
        div.setSeparator(1)
        self.ui.add_btn.addAction(div)

        # Add refresh and other options
        item = wdg.QAction(self)
        item.setText('Refresh Parts List')
        item.triggered.connect(self.refresh_guides_menu)
        self.ui.add_btn.addAction(item)

        # Right click actions
        item = wdg.QAction(self)
        item.setText('Import latest guides into new scene')
        item.triggered.connect(guide.load)
        self.ui.load_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Import latest guides into current scene')
        item.triggered.connect(partial(guide.load, i=1, new_file=0))
        self.ui.load_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Open latest guides file')
        item.triggered.connect(partial(guide.load, i=0))
        self.ui.load_btn.addAction(item)

        div = wdg.QAction(self)
        div.setSeparator(1)
        self.ui.load_btn.addAction(div)

        item = wdg.QAction(self)
        item.setText('Build guides from data file')
        item.triggered.connect(guide.build_guide_from_data_file)
        self.ui.load_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Browse && Build guides from data file')
        item.triggered.connect(partial(guide.build_guide_from_data_file, browse=True))
        self.ui.load_btn.addAction(item)

        div = wdg.QAction(self)
        div.setSeparator(1)
        self.ui.load_btn.addAction(div)

        item = wdg.QAction(self)
        item.setText('Load SG published guides file')
        item.triggered.connect(guide.load_published)
        self.ui.load_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Select highlighted guides.')
        item.triggered.connect(self.select_guide)
        self.ui.guide_list.addAction(item)

        item = wdg.QAction(self)
        item.setText('Highlight selected guides.')
        item.triggered.connect(self.highlight_selected_guide)
        self.ui.guide_list.addAction(item)

        div = wdg.QAction(self)
        div.setSeparator(1)
        self.ui.guide_list.addAction(div)

        item = wdg.QAction(self)
        item.setText('Toggle Selected Guide Visibility')
        item.triggered.connect(self.toggle_guide_vis)
        self.ui.guide_list.addAction(item)

        item = wdg.QAction(self)
        item.setText('Hide All Unselected Guides')
        item.triggered.connect(self.hide_unselected_guides)
        self.ui.guide_list.addAction(item)

        item = wdg.QAction(self)
        item.setText('Show All Guides')
        item.triggered.connect(self.show_all_guides)
        self.ui.guide_list.addAction(item)

        item = wdg.QAction(self)
        item.setText('Rebuild Selected Guides')
        item.triggered.connect(self.rebuild_guides)
        self.ui.mirror_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Rebuild All Guides In Scene')
        item.triggered.connect(guide.rebuild_all)
        self.ui.mirror_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Mirror All Left to Right Guides In Scene')
        item.triggered.connect(guide.mirror_all)
        self.ui.mirror_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Rebuild Selected Guides')
        item.triggered.connect(self.rebuild_guides)
        self.ui.duplicate_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Rebuild All Guides In Scene')
        item.triggered.connect(guide.rebuild_all)
        self.ui.duplicate_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Mirror All Left to Right Guides In Scene')
        item.triggered.connect(guide.mirror_all)
        self.ui.duplicate_btn.addAction(item)

        div = wdg.QAction(self)
        div.setSeparator(1)
        self.ui.guide_list.addAction(div)

        self.ui.duplicate_btn.setContextMenuPolicy(qt.Qt.ActionsContextMenu)
        self.ui.add_btn.setContextMenuPolicy(qt.Qt.ActionsContextMenu)

        self.plc_vis_item = wdg.QAction(self)
        self.plc_vis_item.setCheckable(True)
        self.plc_vis_item.setChecked(True)
        self.plc_vis_item.triggered.connect(partial(self.set_guide_vis, 'joints'))
        self.plc_vis_item.setText('Show Placers && Joints')
        self.ui.guide_list.addAction(self.plc_vis_item)

        self.ctl_vis_item = wdg.QAction(self)
        self.ctl_vis_item.setCheckable(True)
        self.ctl_vis_item.setChecked(True)
        self.ctl_vis_item.triggered.connect(partial(self.set_guide_vis, 'ctrls'))
        self.ctl_vis_item.setText('Show Anim Ctrls')
        self.ui.guide_list.addAction(self.ctl_vis_item)

        self.lra_vis_item = wdg.QAction(self)
        self.lra_vis_item.setCheckable(True)
        self.lra_vis_item.triggered.connect(partial(self.set_guide_vis, 'lra'))
        self.lra_vis_item.setText('Show Joint LRAs')
        self.ui.guide_list.addAction(self.lra_vis_item)

        self.ctlra_vis_item = wdg.QAction(self)
        self.ctlra_vis_item.setCheckable(True)
        self.ctlra_vis_item.triggered.connect(partial(self.set_guide_vis, 'ctlra'))
        self.ctlra_vis_item.setText('Show Ctrl LRAs')
        self.ui.guide_list.addAction(self.ctlra_vis_item)

        div = wdg.QAction(self)
        div.setSeparator(1)
        self.ui.guide_list.addAction(div)

        item = wdg.QAction(self)
        item.setText('Joint Display Size...')
        item.triggered.connect(partial(mm.eval, 'jdsWin'))
        self.ui.guide_list.addAction(item)

        div = wdg.QAction(self)
        div.setSeparator(1)
        self.ui.guide_list.addAction(div)

        item = wdg.QAction(self)
        item.setText('Refresh guides list')
        item.triggered.connect(self.list_guides_in_scene)
        item.triggered.connect(self.clear_options_menu)
        self.ui.guide_list.addAction(item)

        self.ui.none_frame.hide()
        self.initialize_ui_widgets()
        self.refresh_guides_menu()

    def add_part_from_lib(self):
        u = partsLibraryUI.PartsLibraryUI(parts_data=self.parts_data, parent=self)
        u.exec_()

        part_to_build = u.part_to_build
        assembly = u.is_assembly

        if part_to_build:
            if assembly:
                self.build_assembly(part_to_build)
            else:
                self.build_options_menu(new_part=part_to_build)

    def load_model(self, variant='Default'):

        asset = env.get_asset()
        if not asset:
            mc.warning('Asset not set!')
            return

        try:
            build_module = utils.import_module(asset+'_buildList', variant, catch_quiet=1)
            build_list = build_module.build_list

        except:
            mc.warning('Cannot import build module!')
            return

        for item in build_list:
            label = item.get('label')
            command = item.get('command')
            module = ''

            if command:
                if type(command) == partial:
                    command_str = command.func.__module__
                    command_str += '.'+command.func.__name__

                elif command:
                     command_str = command.__module__
                     command_str += '.'+command.__name__

                if command_str == 'rigBot.model.load':
                    print 'Loading model for '+variant+' variant.. '
                    command()

    def load_pinGuideUi(self):

        pinGuidesDialogUI.run()

    def initialize_ui_widgets(self):

        try:
            self.list_guides_in_scene()
            self.check_guides_widget()
            self.set_save_load_button_state()

            if self.ui.options_frame.isVisible():
                self.build_options_menu(use_selected=True)

        except:
            pass

    def check_guides_widget(self):

        if not self.ui.options_frame.isVisible():

            guides_in_scene = [g.split('.')[0] for g in mc.ls('*.guideMasterControl')]
            self.ui.none_frame.show()

            if guides_in_scene:
                self.ui.none_frame.hide()

    def get_guides_in_scene(self, for_display=False):

        sort_by_side = self.ui.radioButton_3.isChecked()
        sort_by_name = self.ui.radioButton_4.isChecked()

        childs = utils.get_children('guides')

        if sort_by_side:
            childs.sort()

        elif sort_by_name:
            childs_dict = {}
            tmp = ['_'.join(c.split('_')[1:])+'_'+c for c in childs]
            for i, child  in enumerate(childs):
                childs_dict[tmp[i]] = child

            childs = []
            tmp.sort()
            for token in tmp:
                childs.append(childs_dict[token])


        guides_list = []
        group_mode = False

        for c in [_ for _ in childs if self.ui.lineEdit.text().strip().lower() in _.lower()]:
            if mc.objExists(c+'.guideMasterControl'):
                guides_list.append('   '+c)

        for c in childs:
            if not mc.objExists(c+'.guideMasterControl'):
                ch = ['   '+g for g in utils.get_children(c) if mc.objExists(g+'.guideMasterControl')]
                ch = [_ for _ in ch if self.ui.lineEdit.text().strip().lower() in _.lower()]
                if ch:
                    if sort_by_side:
                        ch.sort()

                    elif sort_by_name:
                        ch_dict = {}
                        tmp = ['_'.join(c.split('_')[1:]) for c in ch]
                        for i, child  in enumerate(ch):
                            ch_dict[tmp[i]] = child

                        ch = []
                        tmp.sort()
                        for token in tmp:
                            ch.append(ch_dict[token])

                    guides_list.append('\n'+c+' | GRP ')
                    guides_list.extend(ch)

        guides_in_scene = [g for g in guides_list if 'GUIDE' not in g and 'REBUILD' not in g]

        if mc.objExists('guides'):
            guides_in_scene = ['guides | GRP ']+guides_in_scene

        if not for_display:
            guides_in_scene = [c.split('(')[0].strip() for c in guides_in_scene]

        return  guides_in_scene

    def list_guides_in_scene(self):

        guides_in_scene = self.get_guides_in_scene(for_display=True)

        items = []
        for i in range(self.ui.guide_list.count()):
            items.append(self.ui.guide_list.item(i).text())

        if guides_in_scene == items:
            self.update_color_list()
            return

        self.ui.guide_list.clear()
        self.ui.guide_list.addItems(guides_in_scene)
        self.update_color_list()

    def get_selected_guide_items(self):
        selected_guides = mc.ls([i.text().strip().split(' (')[0] for i in self.ui.guide_list.selectedItems()])
        return selected_guides

    def hide_unselected_guides(self):

        selected_guides = self.get_selected_guide_items()
        guides_in_scene = self.get_guides_in_scene()

        if not guides_in_scene or  not selected_guides:
            return

        if guides_in_scene:
            for g in guides_in_scene:
                try:
                    mc.setAttr(g+'.v', 0)
                except:
                    pass

        for sg in selected_guides:
            try:
                mc.setAttr(sg+'.v', 1)
            except:
                pass

        self.update_color_list()

    def toggle_guide_vis(self):

        selected_guides = self.get_selected_guide_items()

        for g in selected_guides:
            if mc.getAttr(g+'.v'):
                try:
                    mc.setAttr(g+'.v', 0)
                except:
                    pass
            else:
                try:
                    mc.setAttr(g+'.v', 1)
                except:
                    pass
        self.update_color_list()

    def show_all_guides(self):

        guides_in_scene = self.get_guides_in_scene()
        if guides_in_scene:
            for g in guides_in_scene:
                try:
                    mc.setAttr(g+'.v', 1)
                except:
                    pass
        self.update_color_list()

    def set_guide_vis(self, attr):

        guides = [ g.split('.')[0] for g in mc.ls('*.guideMasterControl')]

        guides = mc.ls(guides)

        for guide_master in guides:
            if attr == 'joints':
                value = self.plc_vis_item.isChecked()
                mc.setAttr(guide_master+'.jointPlacerVis', value)

            if attr == 'ctrls':
                value = self.ctl_vis_item.isChecked()
                mc.setAttr(guide_master+'.ctrlVis', value)

            if attr == 'lra':
                value = self.lra_vis_item.isChecked()
                mc.setAttr(guide_master+'.jointAxisVis', value)

            if attr == 'ctlra':
                value = self.ctlra_vis_item.isChecked()
                mc.setAttr(guide_master+'.ctrlAxisVis', value)

    def update_color_list(self):
        items = [self.ui.guide_list.item(i) for i in range(self.ui.guide_list.count())]

        for item in items:
            if mc.objExists(item.text().split('|')[0].strip()+'.v'):
                if not mc.getAttr(item.text().split('|')[0].strip()+'.v'):
                    item.setForeground(gui.QColor('gray'))
                    if '|' in item.text():
                        item.setForeground(gui.QColor('#737373'))

                else:
                    item.setForeground(gui.QColor('#ccc'))
                    if '| GRP' in item.text():
                        item.setForeground(gui.QColor('#9a9a9a'))

    def set_save_load_button_state(self):
        """Disable vbuttons IF the asset is not set"""

        if env.get_asset():
            self.ui.load_btn.setEnabled(1)
            self.ui.save_btn.setEnabled(1)
            self.ui.job_label.setText('Asset: '+env.get_asset())

        else:
            self.ui.load_btn.setEnabled(0)
            self.ui.save_btn.setEnabled(0)
            self.ui.job_label.setText('Asset: Not Set!')

    def refresh_guides_menu(self):
        self.parts_data = partsLibraryUI.get_library_data()

    def get_selection_action(self, widget, data_type):

        sel = mc.ls(sl=1)
        orig_sel = mc.ls(sl=1)
        if data_type == 'hook' or data_type == 'string':
            if sel:
                sel = sel[0].replace('_JNT_PLC','_JNT')
                widget.setText(sel)
            else:
                mc.warning('Nothing is selected!')

        elif data_type == 'selection':
            widget.clear()
            if sel:
                widget.addItems(sel)

        mc.select(orig_sel)

    def clear_options_menu(self):

        self.ui.options_frame.hide()
        self.ui.build_btn.hide()
        self.ui.guide_name_label.setText('')

        layout = self.ui.options_grid_layout

        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()
            layout.removeItem(layout.itemAt(i))

        '''
        for i in reversed(range(self.ui.options_grid_layout.count())):
            item = self.ui.options_grid_layout.itemAt(i)

            if item:
                try:
                    widget = item.widget()
                    widget.deleteLater()
                except:
                    widget = None

                try:
                    self.ui.options_grid_layout.removeItem(item)
                except:
                    pass
        '''

    def select_guide(self):
        self.update_color_list()
        selected_guides = self.get_selected_guide_items()

        if selected_guides:
            mc.select(selected_guides)

    def highlight_selected_guide(self):

        guide_nodes = [guide.get_master(n, verbose=0) for n in mc.ls(sl=1)]

        items_to_select = []
        item_texts = []

        for node in guide_nodes:

            items = self.ui.guide_list.findItems(node, qt.Qt.MatchContains)
            if not items:
                continue
            items_to_select.append(items[0])
            item_texts.append(items[0].text())

        item_to_set=None
        for i in range(self.ui.guide_list.count()):
            item = self.ui.guide_list.item(i)
            self.ui.guide_list.setItemSelected(item, False)

            if items_to_select:
                if item.text() in item_texts and item_to_set is None:
                    item_to_set = item

        if not items_to_select:
            return

        self.ui.guide_list.setCurrentItem(item_to_set, True)
        for item in items_to_select:
            self.ui.guide_list.setItemSelected(item, True)

        if item_to_set:
            self.ui.guide_list.scrollToItem(item_to_set, wdg.QAbstractItemView.PositionAtTop)


        self.build_options_menu(use_selected=True)

    def add_prefix_to_arg(self, guide_master, option, field):

        item = self.ui.guide_list.currentItem()

        if not item:
            return

        guide_master = mc.ls(item.text())
        if not guide_master:
            return

        guide_master = guide_master[0]

        name = guide.get_options(guide_master, verbose=0).get('name')
        side = guide.get_options(guide_master, verbose=0).get('side')
        prefix = utils.join_strings([side, name])

        current_value = guide.get_options(guide_master, verbose=0).get(option)

        new_value = current_value
        if current_value.startswith(prefix):
            new_value = prefix + current_value.replace(prefix, '', 1)

        mc.select(guide_master)
        guide.update_options(**{option: new_value})
        self.build_options_menu(self, use_selected=1)

    def build_options_menu(self, new_part='', use_selected=False):

        self.clear_options_menu()

        # get guide from selection
        part = new_part
        part_module = None
        guide_master = None

        if use_selected:
            item = self.ui.guide_list.currentItem()

            if not item:
                self.ui.options_frame.guide_master = None
                self.ui.options_frame.part = None
                return

            if len(self.ui.guide_list.selectedItems()) > 1:
                self.ui.options_frame.guide_master = None
                self.ui.options_frame.part = None
                return

            guide_master = item.text()

        # get part type if not specifed
        if guide_master and mc.objExists(guide_master+'.partType'):
            part = mc.getAttr(guide_master+'.partType', asString=1)
            options_values = guide.get_options(guide_master, verbose=0)
            part_module = guide.instantiate_part(guide_master, verbose=0)
            label = part

        elif part:
            part_module = guide.instantiate_part(part_type=part, verbose=0)
            options_values = part_module.options
            label = part+' (New Guide)'

            self.ui.guide_list.clearSelection()
            self.clear_options_menu()

        self.ui.none_frame.hide()

        if not part_module:
            return

        if len(self.ui.guide_list.selectedItems()) > 1:
            return

        self.ui.guide_name_label.setText(label)
        self.ui.options_frame.guide_master = guide_master
        self.ui.options_frame.part = part

        if new_part:
            self.ui.build_btn.show()
            mayaWidget.setColor(self.ui.build_btn)

        # special cases for worldRoot
        if part == 'worldRoot':
            self.ui.options_frame.show()
            return

        # now build the new options widgets
        options_info = part_module.options_info_dict
        options_list_order = part_module.ordered_arg_list

        self.name_field = None
        for i, option in enumerate(options_list_order):

            self.field = None
            self.btn = None

            value = options_values[option]
            data_type = options_info[option]['data_type']
            hidden = options_info[option]['hidden']
            enum = str(options_info[option]['enum'] or '').split(':')
            tool_tip = options_info[option]['tool_tip']
            lock = options_info[option]['lock']
            selectable_str = options_info[option]['selectable']

            # side option
            if option == 'side' or data_type == 'enum':
                if option == 'side':
                    enum = ['C', 'L', 'R']

                self.field = wdg.QComboBox(self)
                self.field.addItems(enum)
                self.field.setCurrentIndex(enum.index(value))

            # hook andf string attrs
            elif data_type in ['hook', 'string']:
                self.field = wdg.QLineEdit(self)
                self.field.setText(value)

                # if hook create a button
                if data_type == 'hook':
                    self.btn = wdg.QPushButton('<<')

                elif data_type == 'string' and selectable_str:
                    self.btn = wdg.QPushButton('<<')

                self.field.setContextMenuPolicy(qt.Qt.ActionsContextMenu)
                if option == 'name':
                    self.name_field = self.field

                else:
                    if use_selected:
                        itm = wdg.QAction(self)
                        itm.setText('Add part name as prefix to this option')
                        itm.triggered.connect(partial(self.add_prefix_to_arg, guide_master, option, self.field))
                        self.field.addAction(itm)

            #int and float attrs
            elif data_type in ['float','int']:
                self.field = wdg.QLineEdit(self)
                self.field.setText('{0}'.format(value))
                self.field.setContextMenuPolicy(qt.Qt.ActionsContextMenu)

                # set validator
                if data_type == 'int':
                    self.field.setValidator(gui.QIntValidator())
                else:
                    self.field.setValidator(gui.QDoubleValidator())

            #bool attrs
            elif data_type == 'bool':
                self.field = wdg.QComboBox(self)
                self.field.addItems(['False','True'])
                self.field.setCurrentIndex(int(value))

            # selection attrs
            elif data_type == 'selection':
                self.field = wdg.QListWidget(self)
                self.field.setMaximumHeight(150)
                self.field.setMinimumHeight(50)
                self.field.addItems(value)
                self.btn = wdg.QPushButton('<<')

            if hidden:
                continue

            self.label = wdg.QLabel(option)
            self.label.setStyleSheet("font-weight: bold; ");

            self.ui.options_grid_layout.addWidget(self.label, i, 0)
            self.ui.options_grid_layout.addWidget(self.field, i, 1)

            self.field.setStyleSheet('QComboBox{background-color:rgb(45,45,45);}')
            self.field.setToolTip(tool_tip)
            self.field.data_type = data_type

            if self.btn:
                self.btn.released.connect(partial(self.get_selection_action, self.field, data_type))
                self.btn.released.connect(self.update_options)

                self.ui.options_grid_layout.addWidget(self.btn, i, 2)
                self.btn.setMinimumHeight(19)
                self.btn.setMaximumHeight(19)
                self.btn.setToolTip('Use current selection.')

                self.btn.setMinimumWidth(40)
                self.btn.setMaximumWidth(40)

            self.ui.options_grid_layout.setRowStretch(i, 0)

            if type(self.field) is wdg.QLineEdit:
                self.field.returnPressed.connect(self.update_options)

            elif type(self.field) is wdg.QComboBox:
                self.field.currentIndexChanged.connect(self.update_options)

            if lock:
                self.field.setEnabled(False)

        self.ui.options_grid_layout.setColumnStretch(0, 0)
        self.ui.options_grid_layout.setColumnStretch(1, 1)

        if self.ui.options_grid_layout.columnCount() == 3:
            self.ui.options_grid_layout.setColumnStretch(2, 0)

        self.ui.options_frame.show()
        self.update_color_list()

    def create_new_part(self):

        partsLibrary.new_part()
        self.parts_data = partsLibraryUI.get_library_data()

    def save_assembly(self):

        partsLibrary.new_assembly()
        self.parts_data = partsLibraryUI.get_library_data()

    def get_options_from_ui(self):

        options = {}
        for i in range(self.ui.options_grid_layout.count()):
            check_widget = None
            try:
                check_widget = self.ui.options_grid_layout.itemAt(i).widget()
            except:
                pass

            if check_widget is None:
                continue

            if 'QLabel' in str(check_widget):
                value = None
                label = check_widget.text()

                try:
                    widget = self.ui.options_grid_layout.itemAt(i+1).widget()
                except:
                    continue

                data_type = widget.data_type

                if data_type == 'int':
                    value = int(widget.text())

                elif data_type == 'float':
                    value = float(widget.text())

                elif 'QLineEdit' in str(widget):
                    value = widget.text()

                elif 'QComboBox' in str(widget):
                    if widget.currentText() == 'True':
                        value = True

                    elif widget.currentText() == 'False':
                        value = False

                    else:
                        value = widget.currentText()

                elif data_type == 'selection':
                    value = [widget.item(i).text() for i in range(widget.count())]

                options[label] = value
        return options

    @utils.undoable
    def build_assembly(self, part):

        reload(guide)
        guide.build_assembly(part)
        self.list_guides_in_scene()
        self.clear_options_menu()

    @utils.undoable
    def build_new_guide(self):

        part = self.ui.options_frame.part
        options = self.get_options_from_ui()
        guide.build(part, **options)

        self.list_guides_in_scene()
        self.clear_options_menu()

    @utils.undoable
    def update_options(self, args=False):

        guide_master = self.ui.options_frame.guide_master
        if not guide_master or not mc.objExists(guide_master):
            return

        if 'GUIDE' in guide_master:
            return

        current_options = guide.get_options(selection=guide_master, verbose=0)
        new_options = self.get_options_from_ui()

        for key in new_options.keys():
            if current_options[key] == new_options[key]:
                del new_options[key]

        current_sel = mc.ls(sl=1)
        obj = guide.update_options(guide_master, **new_options)

        # update ui
        guide_master = obj.guide_master
        self.ui.guide_list.currentItem().setText('   '+guide_master)
        self.ui.options_frame.guide_master = guide_master
        self.build_options_menu(use_selected=1)

        current_sel = mc.ls(current_sel)
        if current_sel:
            mc.select(current_sel)

    @utils.undoable
    def rebuild_guides(self):

        current_sel = mc.ls(sl=1)

        guides =  self.get_selected_guide_items()
        existing_guides = mc.ls(guides)
        if guides and not existing_guides:
            mc.warning('Guides do not exist in scene!')
            return

        if not existing_guides:
            return

        for node in existing_guides:
            mc.select(node)
            guide.rebuild()

        self.list_guides_in_scene()
        self.clear_options_menu()

        current_sel = mc.ls(current_sel)
        if current_sel:
            mc.select(current_sel)

    @utils.undoable
    def mirror_guides(self):

        current_sel = mc.ls(sl=1)

        guides = self.get_selected_guide_items()
        existing_guides = mc.ls(guides)
        if guides and not existing_guides:
            mc.warning('Guides do not exist in scene!')
            return

        if not existing_guides:
            return

        mc.select(existing_guides)
        guide.mirror()

        self.list_guides_in_scene()
        self.clear_options_menu()

        current_sel = mc.ls(current_sel)
        if current_sel:
            mc.select(current_sel)


    @utils.undoable
    def copy_guides(self):

        current_sel = mc.ls(sl=1)

        guides = self.get_selected_guide_items()
        existing_guides = mc.ls(guides)
        if guides and not existing_guides:
            mc.warning('Guides do not exist in scene!')
            return

        if not existing_guides:
            return

        for guide_master in existing_guides:
            mc.select(guide_master)
            guide.duplicate()

        self.list_guides_in_scene()
        self.clear_options_menu()

        current_sel = mc.ls(current_sel)
        if current_sel:
            mc.select(current_sel)

    @utils.undoable
    def delete_guides(self):

        current_sel = mc.ls(sl=1)

        guides = [i.text() for i in self.ui.guide_list.selectedItems()]
        existing_guides = mc.ls(guides)
        if guides and not existing_guides:
            mc.warning('Guides do not exist in scene!')
            return

        if not existing_guides:
            return

        mc.delete(existing_guides)

        self.list_guides_in_scene()
        self.clear_options_menu()

        current_sel = mc.ls(current_sel)
        if current_sel:
            mc.select(current_sel)
