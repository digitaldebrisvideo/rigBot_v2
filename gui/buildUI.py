from Qt import QtWidgets as wdg
from Qt import QtGui as gui
from Qt import QtCore as qt

import maya.cmds as mc
import maya.mel as mm

from rigBot.gui import mayaWidget
from rigBot.gui import loadDataUI
from rigBot.gui import handPoseUI
from rigBot.gui import build_ui
from rigBot import env
from rigBot import mod
from rigBot import utils
from rigBot import rig
from functools import partial
import getpass
import inspect
import rigBot

import os
import pydoc

reload(build_ui)

class BuildUI(mayaWidget.MayaWidget):

    def __init__(self, parent=None, ignore_missing=False, label=''):
        mayaWidget.MayaWidget.__init__(self, parent=parent)

        title = 'build_UI'
        #if mc.window(title, q=1, ex=1):
            #mc.deleteUI(title)

        self.ui = build_ui.Ui_guides_form()
        self.ui.setupUi(self)
        self.setObjectName(title)

        mayaWidget.set_icon(self.ui.help_btn, 'info_24x24.png')
        mayaWidget.set_icon(self.ui.icon_label, 'logo_36x36.png')

        css = 'QPushButton:!disabled { background-color: #7c5cb7; }'
        self.ui.build_all_btn.setStyleSheet(css)

        self.ui.help_btn.released.connect(rigBot.help)
        self.resize(445, 720)

        self.ui.splitter.setStretchFactor(0,1)
        self.ui.splitter.setStretchFactor(1,0)
        self.ui.splitter.setCollapsible(1,1)
        self.ui.splitter.setCollapsible(0,0)
        self.ui.splitter.setSizes([1000,100])

        self.asset = ''
        self.variant = ''
        self.variants = ['default']
        self.use_plugin = True
        self.import_error = False
        self.build_module = None
        self.no_asset_mode = False
        self.build_items = []
        self.build_list = []

        self.ui.variant_cmb.currentIndexChanged.connect(self.set_variant)
        self.ui.use_plugin_chx.stateChanged.connect(self.set_use_plugin)
        self.ui.cache_chx.stateChanged.connect(self.set_cache_build)

        self.ui.build_tree.header().setSectionResizeMode(0, wdg.QHeaderView.Stretch)
        self.ui.build_tree.header().setSectionResizeMode(1, wdg.QHeaderView.ResizeToContents)

        self.ui.build_tree.itemChanged.connect(self.set_enabled)
        self.ui.build_tree.itemSelectionChanged.connect(self.update_info_widget)

        self.ui.hand_util_btn.released.connect(handPoseUI.run)
        self.ui.data_util_btn.released.connect(loadDataUI.run)
        self.ui.data_util_btn_2.released.connect(rig.unfinalize)

        self.ui.build_next_btn.released.connect(self.build_next_step)
        self.ui.build_selected_btn.released.connect(self.build_selected_steps)
        self.ui.build_to_selected_btn.released.connect(partial(self.build_selected_steps, to_selection=True))
        self.ui.build_all_btn.released.connect(partial(self.build_selected_steps, remaining=True))
        self.ui.load_cache_build_btn.released.connect(self.load_cache_and_rebuild)
        self.ui.load_cache_build_btn.hide()

        self.ui.open_btn.released.connect(self.open_module_file)
        self.ui.open_btn_2.released.connect(self.open_build_list_file)
        self.ui.migrate_btn.released.connect(self.migrate_file)

        item = wdg.QAction(self)
        item.setText('Build All Steps From Start To Finish')
        item.triggered.connect(partial(self.build_selected_steps, fresh_build=True))
        self.ui.build_all_btn.addAction(item)

        item = wdg.QAction(self)
        item.setText('Build Next Step')
        item.triggered.connect(self.build_next_step)
        self.ui.build_tree.addAction(item)

        item = wdg.QAction(self)
        item.setText('Build Selected Steps')
        item.triggered.connect(self.build_selected_steps)
        self.ui.build_tree.addAction(item)

        item = wdg.QAction(self)
        item.setText('Build Up To Selected Step')
        item.triggered.connect(partial(self.build_selected_steps, to_selection=True))
        self.ui.build_tree.addAction(item)

        div = wdg.QAction(self)
        div.setSeparator(1)
        self.ui.build_tree.addAction(div)

        item = wdg.QAction(self)
        item.setText('Build All Remaining Steps')
        item.triggered.connect(partial(self.build_selected_steps, to_selection=True))
        self.ui.build_tree.addAction(item)

        div = wdg.QAction(self)
        div.setSeparator(1)
        self.ui.build_tree.addAction(div)

        item0 = wdg.QAction(self)
        item0.setText('Load Previous Cache And Run This Step')
        item0.triggered.connect(self.load_cache_and_rebuild)
        self.ui.build_tree.addAction(item0)

        item2 = wdg.QAction(self)
        item2.setText('Load Cache For This Step')
        item2.triggered.connect(self.load_cache)
        self.ui.build_tree.addAction(item2)

        self.cache_items= [item0, item2]

        div = wdg.QAction(self)
        div.setSeparator(1)
        self.ui.build_tree.addAction(div)

        item = wdg.QAction(self)
        item.setText('Reload Build Module and Refresh Steps List')
        item.triggered.connect(self.initialize_ui_widgets)
        self.ui.build_tree.addAction(item)

        item = wdg.QAction(self)
        item.setText('Load Cache For This Step')
        item.triggered.connect(self.load_cache)
        self.ui.load_cache_build_btn.addAction(item)

        self.initialize_ui_widgets()

    def initialize_ui_widgets(self, force_reload=True):

        if force_reload or self.asset != env.get_asset():
            self.read_build_list_from_disk()
            print ('Reloading build list for asset: '+env.get_asset())

        self.set_asset_state()
        self.set_cache_build()
        self.populate_build_tree()

    def read_build_list_from_disk(self):
        """This is what reads the assets build list on disk. The module is reloaded every time its read."""

        self.asset = env.get_asset()
        self.variant = env.get_variant() or 'default'
        self.variants = env.list_variants(verbose=0) or ['default']

        variant_class_name = self.variant[0].upper()+self.variant[1:]
        build_module = mod.import_module(self.asset+'_buildList.'+variant_class_name)

        if not self.asset or not self.variant:
            self.build_module = None
            self.build_list = []
            self.use_plugin = True

        # load default from rigBot asset folder
        self.no_asset_mode = False
        if not build_module:
            build_module = mod.import_module('buildList.'+variant_class_name)
            self.no_asset_mode = True

        elif type(build_module) in [unicode, str]:

            self.ui.build_tree.clear()

            item = wdg.QTreeWidgetItem()
            item.setSizeHint(0, qt.QSize(10, 17))
            item.setText(0, '**No Build List available for this asset!')
            item.setText(1, build_module.split(':')[0])

            item.command_str = self.asset+'_buildList'
            item.file_path = ''
            item.doc_label = self.asset+'_buildList'
            item.build_index = None

            tool_tip = 'Cannot find the {0}_buildList.py\n{1}'.format(self.asset, build_module)

            item.setToolTip(0, tool_tip)
            item.doc_str = tool_tip+'\nMake sure ther are no syntax errors in your code!'
            self.ui.build_tree.addTopLevelItem(item)

            self.ui.module_label.setText(item.doc_label)
            self.ui.doc_browser.setText(item.doc_str)

            self.build_module = build_module
            self.build_list = []
            self.use_plugin = True

            color = gui.QColor('#ff4d4d')
            item.setForeground(0, color)
            item.setForeground(1, color)


        elif build_module:

            build_list = build_module.build_list

            update_required = False
            if len(self.build_list) == len(build_list):
                for i in range(len(build_list)):
                    if build_list[i].get('label') != self.build_list[i].get('label'):
                        update_required = True
            else:
                update_required = True

            self.build_module = build_module
            self.build_list = build_list
            self.use_plugin = build_module.use_plugin_nodes

            if update_required:
                self.populate_build_tree()
        else:
            self.build_module = None
            self.build_list = []
            self.use_plugin = True

    def script_job_functions(self):

        try:
            self.set_build_status()
        except:
            pass

    def set_asset_state(self):

        # Reset widgets if asset is not set

        try:
            self.ui.variant_cmb.currentIndexChanged.disconnect(self.set_variant)
        except:
            pass

        try:
            self.ui.use_plugin_chx.stateChanged.disconnect(self.set_use_plugin)
        except:
            pass

        try:
            self.ui.cache_chx.stateChanged.disconnect(self.set_cache_build)
        except:
            pass

        self.ui.variant_cmb.clear()
        self.ui.asset_label.setText('Asset: Not Set!')

        self.ui.use_plugin_chx.setChecked(1)

        if os.environ['cache_build'] == 'False':
            self.ui.cache_chx.setChecked(0)
        else:
            self.ui.cache_chx.setChecked(1)

        btns = [
        self.ui.open_btn,
        self.ui.open_btn_2,
        self.ui.migrate_btn,
        self.ui.build_all_btn,
        self.ui.build_next_btn,
        self.ui.build_selected_btn,
        self.ui.load_cache_build_btn,
        self.ui.use_plugin_chx,
        self.ui.cache_chx]

        for btn in btns:
            btn.setEnabled(1)

        # IF asset IS set populate everytrhing
        if self.asset:
            self.ui.asset_label.setText('Asset: '+self.asset)

        if self.asset and self.variant and self.variants:
            variants = self.variants

            if 'default' in variants:
                variants.remove('default')
                variants.insert(0, 'default')

            self.ui.variant_cmb.addItems(variants)
            self.ui.use_plugin_chx.setChecked(self.use_plugin)

            for btn in btns:
                btn.setEnabled(1)

            idx = variants.index(self.variant)
            self.ui.variant_cmb.setCurrentIndex(idx)

        self.ui.variant_cmb.currentIndexChanged.connect(self.set_variant)
        self.ui.use_plugin_chx.stateChanged.connect(self.set_use_plugin)
        self.ui.cache_chx.stateChanged.connect(self.set_cache_build)

    def set_variant(self):
        """Set the variant from UI and reset all ui and build list"""

        variant = self.ui.variant_cmb.currentText()
        env.set_variant(variant)

        self.initialize_ui_widgets()

    def set_use_plugin(self):
        """Change the use plugin flag PER variant. This is written to the assets build list file."""

        state = self.ui.use_plugin_chx.isChecked()
        self.build_module.set_use_plugin(state)

    def set_cache_build(self):
        """Set the cache build variable"""

        cache = self.ui.cache_chx.isChecked()

        if cache:
            self.ui.load_cache_build_btn.setEnabled(1)
            os.environ['cache_build'] = 'True'

            for action in self.cache_items:
                action.setEnabled(1)

        else:
            self.ui.load_cache_build_btn.setEnabled(0)
            os.environ['cache_build'] = 'False'

            for action in self.cache_items:
                action.setEnabled(0)

    def clear_build_tree(self):
        for i in reversed(range(self.ui.build_tree.topLevelItemCount())):
            self.ui.build_tree.takeTopLevelItem(i)

    def populate_build_tree(self):
        """This build your build list ui QTreewidget"""

        if type(self.build_module) in [str, unicode]:
            return

        self.clear_build_tree()

        parent_item = None
        self.build_items = []

        try:
            self.ui.build_tree.itemChanged.disconnect(self.set_enabled)
        except:
            pass

        if not self.build_list:
            item = wdg.QTreeWidgetItem()
            item.setSizeHint(0, qt.QSize(10, 17))
            item.setText(0, '**No Build List available for this asset!')
            item.command_str = self.asset+'_buildList'
            item.file_path = ''
            item.doc_label = self.asset+'_buildList'
            item.build_index = None

            tool_tip = 'Cannot find the {0}_buildList.py'.format(self.asset)

            item.setToolTip(0, tool_tip)
            item.doc_str = tool_tip+'\nMake sure ther are no syntax errors in your code!'
            self.ui.build_tree.addTopLevelItem(item)

            self.ui.module_label.setText(item.doc_label)
            self.ui.doc_browser.setText(item.doc_str)

            color = gui.QColor('gray')
            item.setForeground(0, color)

            return

        for idx, item in enumerate(self.build_list):

            label = item.get('label')
            enabled = item.get('enabled')
            command = item.get('command')

            command_str = ''
            file_path = ''
            tool_tip = ''
            doc_str = ''
            doc_label = ''
            error_type = ''
            error_msg = ''

            if command:
                # first get the fila path and doc string for the commands
                if type(command) == partial:
                    error_type = ''
                    error_msg = ''
                    module = command.func.__module__
                    command_str = command.func.__name__
                    args = command.args
                    kwargs = command.keywords
                    file_path = inspect.getfile(inspect.getmodule(command.func))
                    doc = inspect.getdoc(command.func)

                    kwarg_str = '( ' + ', '.join(args)

                    for key, value in kwargs.items():
                        kwarg_str += '{0}={1}, '.format(key, value)
                    if kwarg_str.endswith(', '):
                        kwarg_str = kwarg_str[:-2]
                    kwarg_str += ' )'

                    if kwargs or args:
                        command_str += kwarg_str
                    else:
                        command_str += '()'

                elif type(command) in [unicode, str]:
                    doc = command.replace(' :: ', '\n')
                    command_str = ''

                    file_path = command.split(' :: ')[2]
                    module = command.split(' :: ')[1]

                    error_type = command.split(':')[0]
                    error_msg = '\n'.join(command.split(' :: ')[:-1])

                else:
                    error_type = ''
                    error_msg = ''
                    module = command.__module__
                    command_str = command.__name__+'()'
                    file_path = inspect.getfile(inspect.getmodule(command))
                    doc = inspect.getdoc(command)

                # assemble tool tip
                if not doc:
                    doc = ''

                file_path = file_path.replace('.pyc', '.py')

                tool_tip = 'FILE PATH:\n   '+file_path+'\n\n'
                tool_tip += 'MODULE:\n   '+module+'\n\n'
                tool_tip += 'COMMAND:\n   '+command_str+'\n\n'

                doc_label = module+'.'+command_str.split('(')[0]

                # assemble doc string
                doc_str = tool_tip+'.\n'
                doc_str += doc

            # Create the widget item

            item = wdg.QTreeWidgetItem()
            item.setSizeHint(0, qt.QSize(10, 17))
            item.setText(0, label)
            item.setText(1, error_type)
            item.setToolTip(0, tool_tip)

            item.command_str = command_str
            item.doc_str = doc_str
            item.build_index = idx
            item.file_path = file_path
            item.doc_label = doc_label
            item.label = False
            item.error_type = error_type
            item.error_msg = error_msg

            if command:
                if enabled:
                    item.setCheckState(0, qt.Qt.CheckState.Checked)
                else:
                    item.setCheckState(0, qt.Qt.CheckState.Unchecked)

                if parent_item:
                    parent_item.addChild(item)
                    parent_item.setExpanded(1)
                else:
                     self.ui.build_tree.addTopLevelItem(item)

            else:
                item.label = True
                parent_item = item
                item.setExpanded(1)
                self.ui.build_tree.addTopLevelItem(item)

        self.build_items = [i.value() for i in wdg.QTreeWidgetItemIterator(self.ui.build_tree)]
        self.ui.build_tree.itemChanged.connect(self.set_enabled)

        self.update_info_widget()
        self.set_build_status()

    def set_enabled(self, item):

        new_state = bool(item.checkState(0))
        idx = item.build_index

        try:
            if not 'enabled' in self.build_list[idx].keys():
                return
        except:
            return

        current_state = self.build_list[idx].get('enabled')
        if current_state == new_state:
            return

        if not len(self.build_list) == len(self.build_module.build_list):
            return

        self.build_module.get_step_node()
        self.build_module.get_status()
        self.build_module.set_enabled(idx, new_state)

    def update_info_widget(self):

        items = self.ui.build_tree.selectedItems()

        self.ui.module_label.setText('')
        self.ui.doc_browser.setText('')

        if not items:
            return

        if len(items) > 1:
            self.ui.module_label.setText('Multiple Items Selected...')
            self.ui.doc_browser.setText('')
            return

        item = items[0]
        self.ui.module_label.setText(item.doc_label)
        self.ui.doc_browser.setText(item.doc_str)

    def set_build_status(self):

        self.build_module.get_step_node()
        self.build_module.get_status()

        status_array = self.build_module.status_array
        enabled_array = self.build_module.enabled_array
        next_step = self.build_module.get_next_step()

        build_asset = env.get_asset()
        if mc.objExists(self.build_module.step_node+'.asset'):
            build_asset = mc.getAttr(self.build_module.step_node+'.asset')

        for idx, item in enumerate(self.build_items):

            item.setText(1, item.error_type)

            if item.label:
                color = gui.QColor('gray')
            else:
                color = gui.QColor('#ccc')

                if self.no_asset_mode:
                    color = gui.QColor(mayaWidget.purple_color)

                elif item.file_path and self.asset in item.file_path:
                    color = gui.QColor(mayaWidget.blue_color)

                    if env.using_sandbox:
                        color = gui.QColor(mayaWidget.pink_color)

                # status color
                if status_array[idx] == -1:
                    color = gui.QColor('#ff4d4d')
                    item.setText(1, 'FAILED!  ')

                if status_array[idx] in [2]:
                    color = gui.QColor('#00b386')

                if item.error_type:
                    color = gui.QColor('#ff4d4d')

            item.setForeground(0, color)
            item.setForeground(1, color)

        # Set last successful item to bright green
        for idx in reversed(range(len(self.build_items))):
            if status_array[idx] == 3:
                color = gui.QColor('#00ff99')
                self.build_items[idx].setForeground(0, color)
                self.build_items[idx].setForeground(1, color)
                break

    def set_wip_item_color(self, idx):
        color = gui.QColor('orange')
        self.build_items[idx].setForeground(0, color)
        self.build_items[idx].setForeground(1, color)
        qt.QCoreApplication.processEvents()

    @utils.undoable
    def build_next_step(self):

        self.read_build_list_from_disk()

        self.build_module.get_step_node()
        self.build_module.get_status()
        status_array = self.build_module.status_array
        enabled_array = self.build_module.enabled_array
        next_step = self.build_module.get_next_step()

        try:
            i = self.build_module.get_next_step()
            if not self.build_list[i].get('command'):
                i +=1

            self.set_wip_item_color(i)

            i = self.build_module.build('next')

            if 'command' in self.build_list[i].keys():
                self.save_cache(i)

        except:
            if self.build_items[i].error_msg:
                print self.build_items[i].error_msg
            else:
                print utils.get_exception()

        self.set_build_status()

    @utils.undoable
    def build_selected_steps(self, to_selection=False, remaining=False, fresh_build=False):

        self.read_build_list_from_disk()

        self.build_module.get_step_node()
        self.build_module.get_status()

        status_array = self.build_module.status_array
        enabled_array = self.build_module.enabled_array
        items = self.ui.build_tree.selectedItems()

        next_step = self.build_module.get_next_step()
        last_step = self.build_items[-1].build_index

        if not fresh_build and not remaining and not items:
            mc.warning('No build steps selected!')
            return

        if items:
            selected_idx = [i.build_index for i in items]
            selected_idx.sort()

            next_step = selected_idx[0]
            last_step = selected_idx[-1]

            if to_selection:
                next_step = self.build_module.get_next_step()

                if last_step < next_step:
                    mc.warning('The selected step has already been built up to!')
                    return

        if remaining:
            next_step = self.build_module.get_next_step()
            last_step = self.build_items[-1].build_index

        if fresh_build:
            next_step = 0
            last_step = self.build_items[-1].build_index
            if not utils.save_changes():
                return

        progress_bar = mm.eval('$tmp = $gMainProgressBar')

        try:
            if next_step == last_step:
                self.set_wip_item_color(next_step)
                self.build_module.build(next_step)
                if 'command' in self.build_list[next_step].keys():
                    self.save_cache(next_step)

                self.set_build_status()

            else:

                message = 'Building Rig ...'
                if next_step < last_step+1:
                    mc.progressBar(progress_bar, e=True, bp=True, ii=True, st=message, min=next_step, max=last_step+1)

                for i in range(next_step, last_step+1, 1):

                    if mc.progressBar(progress_bar, q=True, ic=True):
                        mc.warning('Build canceled by user!')
                        mc.progressBar(progress_bar, e=True, ep=1)
                        return

                    self.set_wip_item_color(i)
                    self.build_module.build(i)

                    if 'command' in self.build_list[i].keys():
                        self.save_cache(i)

                    self.set_build_status()
                    qt.QCoreApplication.processEvents()

                    mc.progressBar(progress_bar, e=True, step=1)

        except:
            self.set_build_status()
            mc.progressBar(progress_bar, e=True, ep=1)

            if self.build_items[i].error_msg:
                print self.build_items[i].error_msg
            else:
                print utils.get_exception()

        self.set_build_status()
        mc.progressBar(progress_bar, e=True, ep=1)

    def open_module_file(self):

        items = self.ui.build_tree.selectedItems()
        if not items:
            return

        if len(items) > 1:
            mc.warning('Select only one item to open file!')
            return

        if not items[0].command_str:
            return

        file_path = items[0].file_path
        file_path = file_path.replace('.pyc','.py')
        utils.edit_file(file_path)

    def open_build_list_file(self):

        file_path = os.path.join(env.get_rigbuild_path(), self.asset+'_buildList.py')
        utils.edit_file(file_path)

    def migrate_file(self):

        if not self.asset:
            return

        items = self.ui.build_tree.selectedItems()
        if not items:
            return

        if len(items) > 1:
            mc.warning('Select only one item to open file!')
            return

        if not items[0].command_str:
            return

        file_path = items[0].file_path
        file_path = file_path.replace('.pyc','.py')

        if self.asset in file_path:
            mc.warning('This module is already in the assets rigbuild folder!')
            return

        env.migrate_file(file_path, add_asset_prefix=False, edit=False, verbose=True)
        self.set_build_status()

    def save_cache(self, index):

        if os.environ['cache_build'] != 'True':
            return

        cache_path = mc.internalVar(utd=1)
        utils.make_dirs(cache_path)

        mm.eval('source "cleanUpScene.mel";')
        mm.eval('deleteUnknownNodes();')

        file_path = os.path.join(cache_path, '{0}_{1}_{2}_{3}_rig_cache.ma'.format(
            self.asset,
            self.variant,
            getpass.getuser(),
            index))

        mc.file(file_path, pr=1, ea=1, f=1, type='mayaAscii')
        print '# Cached Step: '+file_path

    def load_cache(self, index=None, previous=False):

        if not self.asset:
            mc.warning('Asset not set.')
            return

        if os.environ['cache_build'] != 'True':
            mc.warning('Caching is currently turned off.')
            return

        item = self.ui.build_tree.currentItem()
        if not item:
            return

        if index is None:
            try:
                index = item.build_index
                if previous:
                    index -= 1
            except:
                return

        cache_path = mc.internalVar(utd=1)
        if not os.path.isdir(cache_path):
            mc.warning('Path doesnt exist: '+cache_path)
            return

        file_path = os.path.join(cache_path, '{0}_{1}_{2}_{3}_rig_cache.ma'.format(
                                    self.asset,
                                    self.variant,
                                    getpass.getuser(),
                                    index))

        if not os.path.isfile(file_path):
            file_path = os.path.join(cache_path, '{0}_{1}_{2}_{3}_rig_cache.ma'.format(
                                    self.asset,
                                    self.variant,
                                    getpass.getuser(),
                                    index-1))

        if not os.path.isfile(file_path):
            mc.warning('Cache file doesnt exist: '+file_path)
            return

        if not utils.save_changes():
            return

        mc.file(file_path, i=1)
        self.build_module.get_status()
        self.set_build_status()

        print '# Loaded cache Step: '+file_path
        return True

    def load_cache_and_rebuild(self):

        item = self.ui.build_tree.currentItem()
        if not item:
            return

        if self.load_cache(previous=1):
            self.build_next_step()




