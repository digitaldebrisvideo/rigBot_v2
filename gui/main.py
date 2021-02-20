from Qt import QtWidgets as wdg
from Qt import QtGui as gui
from Qt import QtCore as qt

import maya.cmds as mc
import maya.mel as mm

from functools import partial
import os

from rigBot.gui import mayaWidget

from rigBot.gui import setInheritance_ui
from rigBot.gui import variant_ui
from rigBot.gui import main_ui

from rigBot import env
from rigBot import utils
from rigBot import guide
import rigBot

from rigBot.gui import guidesUI
from rigBot.gui import buildUI
from rigBot.gui import exportUI
from rigBot.gui import spacesUI

reload(buildUI)
reload(guidesUI)
reload(main_ui)
reload(exportUI)
reload(spacesUI)

class Main(mayaWidget.MayaWidget):

    def __init__(self, parent=None):
        mayaWidget.MayaWidget.__init__(self)

        title = ' rigBotMainUI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = main_ui.Ui_asset_env_form()
        self.ui.setupUi(self)
        self.setObjectName(title)

        self.setWindowTitle('rigBot 2.0 | Rig Build UI')

        # Add tabs
        self.guides_UI = guidesUI.GuidesUI(parent=self)
        self.ui.tabWidget.insertTab(1, self.guides_UI, 'Guides')

        self.build_UI = buildUI.BuildUI(parent=self)
        self.ui.tabWidget.insertTab(2, self.build_UI, 'Build Rig')

        self.export_UI = exportUI.ExportUI(parent=self)
        self.ui.tabWidget.insertTab(3, self.export_UI, 'Export Data')

        self.spaces_UI = spacesUI.SpacesUI(parent=self)
        self.ui.tabWidget.insertTab(4, self.spaces_UI, 'Spaces')
        self.ui.lineEdit_3.textChanged.connect(self.search_filter)

        self.ui.tabWidget.currentChanged.connect(self.reload_all)
        self.ui.tabWidget.setStyleSheet('QTabWidget { border: 0; }');

        self.SCRIPT_JOB_NUMBERS = self.create_ui_script_jobs(self.script_job_reload)

        self.blue_color = mayaWidget.blue_color

        ######################################################################

        # Set up asset env TAb
        mayaWidget.set_icon(self.ui.help_btn, 'info_24x24.png')
        mayaWidget.set_icon(self.ui.icon_label, 'logo_36x36.png')

        self.ui.help_btn.released.connect(rigBot.help)

        # connections
        self.ui.asset_list.itemSelectionChanged.connect(self.set_asset_and_populate_info)
        self.ui.browse_btn.released.connect(self.browse_path)
        self.ui.create_files_btn.released.connect(self.make_rig_asset)
        self.ui.inherit_btn.released.connect(self.set_inheritance)
        self.ui.icon_btn_2.released.connect(self.take_thumbnail_snapshot)
        self.ui.variant_btn.released.connect(self.add_variant)
        self.ui.set_project_cmb.currentIndexChanged.connect(self.set_project)

        self.ui.alpha_btn_3.released.connect(self.clear_search)

        self.ui.comboBox.currentIndexChanged.connect(self.set_build_mode)

        # context menus
        item = wdg.QAction(self)
        item.setText('Delete Custom Thumbnail')
        item.triggered.connect(self.clear_thumbnail)
        self.ui.icon_grp.addAction(item)

        item = wdg.QAction(self)
        item.setText('Refresh asset list')
        item.triggered.connect(partial(self.populate_assets, reload_list=True))
        self.ui.asset_list.addAction(item)

        # variables
        self.assets = env.list_assets(verbose=False)
        self.asset = ''
        self.rigbuild_path = ''
        self.info = {}

        self.ui.lineEdit.returnPressed.connect(self.set_user)
        self.ui.pushButton.released.connect(partial(self.set_user, reset=True))

        # populate
        self.populate_assets()
        self.initialize_ui_widgets()

        if not env.shotgun:
            item = wdg.QAction(self)
            item.setText('Refresh Projects List')
            item.triggered.connect(self.list_projects)
            self.ui.set_project_cmb.addAction(item)

            div = wdg.QAction(self)
            div.setSeparator(1)
            self.ui.asset_list.addAction(div)

            item = wdg.QAction(self)
            item.setText('Create New Asset')
            item.triggered.connect(partial(self.make_rig_asset, new=True))
            self.ui.asset_list.addAction(item)

        self.list_projects()
        self.resize(600, 900)
        self.ui.lineEdit.setText(env.get_user())

        self.center()

    def clear_search(self):
        self.ui.lineEdit_3.setText('')

    def search_filter(self):

        text = self.ui.lineEdit_3.text().lower()
        for i in range(self.ui.asset_list.count()):
            item = self.ui.asset_list.item(i)
            if text in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)

    def set_user(self, reset=False):
        if reset:
            env.set_user()
            self.ui.lineEdit.setText(env.get_user())
            self.set_asset_and_populate_info()
            return

        env.set_user(self.ui.lineEdit.text())
        self.set_asset_and_populate_info()

    def set_build_mode(self):
        if self.ui.comboBox.currentText() == 'User Sandbox ( If available )':
            env.set_build_mode('sandbox')
        else:
            env.set_build_mode('forceLive')

        self.set_asset_and_populate_info()

    def script_job_reload(self):

        try:
            mm.eval('selectPriority -locator 9')
            self.guides_UI.list_guides_in_scene()
            self.guides_UI.check_guides_widget()
            self.build_UI.script_job_functions()
            self.export_UI.list_data()

        except:
            pass

    def reload_all(self):

        # refresh env widget
        self.initialize_ui_widgets()
        self.guides_UI.initialize_ui_widgets()
        self.export_UI.initialize_ui_widgets()
        self.spaces_UI.initialize_ui_widgets()
        self.build_UI.initialize_ui_widgets(force_reload=False)
        self.export_UI.list_data()

    def create_ui_script_jobs(self, command):

        sj_numbers = []
        sj_numbers.append(mc.scriptJob(e=['PreFileNewOrOpened', command], cu=1))
        sj_numbers.append(mc.scriptJob(e=['Undo', command], cu=1))
        sj_numbers.append(mc.scriptJob(e=['Redo', command], cu=1))
        sj_numbers.append(mc.scriptJob(ct=['delete', command], cu=1))

        sj_numbers.append(mc.scriptJob(e=['DagObjectCreated', command], cu=1))
        return sj_numbers

    def kill_ui_script_jobs(self, sj_numbers):
        for sn in sj_numbers:
            try:
                mc.scriptJob(kill=sn, force=True)
            except:
                pass

    def closeEvent(self, event):

        if self.SCRIPT_JOB_NUMBERS:
            self.kill_ui_script_jobs(self.SCRIPT_JOB_NUMBERS)

        #super(GuidesUI, self).closeEvent(event)

    def list_projects(self):

        if env.shotgun:
            self.ui.set_project_cmb.hide()
            self.ui.job_label.setText('Project: '+os.environ.get('PL_DIVISION'))

        else:

            current_project = env.project

            env.reload_prefs()

            self.ui.job_label.setText('Project: ')
            self.ui.set_project_cmb.show()

            projects = env.list_projects(verbose=False)
            self.ui.set_project_cmb.clear()
            self.ui.set_project_cmb.addItems(projects)

            if current_project in projects:
                self.ui.set_project_cmb.setCurrentText(current_project)

    def set_project(self):

        project = self.ui.set_project_cmb.currentText()
        env.set_project(project)
        self.populate_assets(reload_list=1)

    def populate_assets(self, reload_list=False):
        """Populate assets list."""

        if reload_list or not env.shotgun:
            self.assets = env.list_assets(verbose=False)

        self.ui.asset_list.clear()
        self.ui.asset_list.addItems(self.assets)
        self.update_asset_color_status()
        self.clear_search()

    def update_asset_color_status(self):
        """Changes the color of the asset in list to reflect whether they
            have rig files or not"""

        count = self.ui.asset_list.count()
        for i in range(count):
            item = self.ui.asset_list.item(i)
            asset = item.text()

            item.setForeground(gui.QColor('gray'))
            info = env.get_asset_info(asset, verbose=0)

            if info:
                item.setForeground(gui.QColor('#ccc'))

    def browse_path(self):
        """Brose to path"""
        utils.browse_path(self.ui.rigbuild_path_line.text())

    def make_rig_asset(self, new=False):
        """Initialize a rig asset and create all flies on disk"""

        if new:
            result = mc.promptDialog(
                            title='New Asset',
                            message='New asset name:',
                            button=['Create', 'Cancel'],
                            defaultButton='Create',
                            cancelButton='Cancel',
                            dismissString='Cancel')

            if result == 'Create':
                asset = mc.promptDialog(query=True, text=True)
            else:
                return

        else:

            items = self.ui.asset_list.selectedItems()
            if not items:
                return

            asset = items[0].text()

        env.make_rig_asset(asset)
        self.set_asset_and_populate_info()

        if new:
            self.populate_assets()

    def initialize_ui_widgets(self):

        self.asset = env.get_asset()
        self.rigbuild_path = env.get_rigbuild_path()
        self.info = env.get_asset_info(verbose=False) or {}

        if not self.asset:
            self.ui.make_files_frame_2.show()
            self.ui.info_frame.hide()
            self.ui.make_files_frame.hide()
            return

        else:

            for i in range(self.ui.asset_list.count()):
                item = self.ui.asset_list.item(i)
                if item.text() == env.get_asset():
                    self.ui.asset_list.setCurrentRow(i)

        user = env.get_user()
        if not user:
            user = env.set_user()

        self.ui.lineEdit.setText(user)

    def set_asset_and_populate_info(self):
        """Set all info widgets for currrently selected asset."""

        # This clears the info field
        self.ui.make_files_frame_2.hide()
        self.ui.info_frame.hide()
        self.ui.make_files_frame.hide()
        self.update_asset_color_status()

        mayaWidget.set_icon(self.ui.thumb_label, 'thumbnail_213x120.png')

        rb_style = 'background-color: rgb(55, 55, 55); color: rgb(150, 150, 150);'
        self.ui.rigbuild_path_line.setText('')
        self.ui.rigbuild_path_line.setStyleSheet(rb_style)

        items = self.ui.asset_list.selectedItems()
        if not items:
            return

        # set asset
        self.asset = items[0].text() or ''
        env.set_asset(self.asset, verbose=False)
        self.info = env.get_asset_info(verbose=False) or {}
        self.rigbuild_path = env.get_rigbuild_path() or ''

        if os.path.exists(self.rigbuild_path):
            self.ui.rigbuild_path_line.setText(self.rigbuild_path)

        if not self.info:
            self.ui.make_files_frame.show()
            return

        # Otherwise populate all fields
        self.ui.info_frame.show()
        self.ui.make_files_frame.hide()

        # set asset label and rigbuild path
        self.ui.asset_label.setText(self.asset)
        self.ui.rigbuild_path_line.setStyleSheet('background-color: rgb(55, 55, 55); color:{0};'.format(self.blue_color))

        # Set creation info
        self.ui.create_date_label.setText(self.info.get('date_created'))
        self.ui.modified_label.setText(self.info.get('date_modified'))
        self.ui.modified_by_label.setText(self.info.get('last_modified_by'))

        # populate variants and inheritas
        self.populate_variants()
        self.populate_inheritance()

        # set icon
        icon_path = os.path.join(self.rigbuild_path, 'thumbnail.jpg')

        if os.path.isfile(icon_path):
            mayaWidget.set_icon(self.ui.thumb_label, icon_path)

        else:
            mayaWidget.set_icon(self.ui.thumb_label, 'thumbnail_213x120.png')

        if env.using_sandbox:
            self.ui.rigbuild_path_line.setStyleSheet('background-color: rgb(55, 55, 55); color:{0};'.format(mayaWidget.pink_color))

    def populate_variants(self):
        """Clear variants list and repopulate with info from assetInfo json """
        # set variants

        label = ''
        primary = self.info.get('primary_variant') or ''
        for variant in self.info.get('rig_variants') or []:
            if variant == primary:
                variant += ' ( Primary Rig )'

            label += variant+'\n'

        self.ui.variant_label.setText(label)


    def populate_inheritance(self):
        """Clear rig inheritance list and repopulate with info from assetInfo json """

        label = ''

        inheritance = self.info.get('inherit_from') or []
        for i_info in inheritance:
            text = i_info.get('asset')

            if i_info.get('inherit_guide'):
                text += '  ( Inheriting: sys.path, guides )'
            else:
                text += '  ( Inheriting: sys.path )'

            label += text+'\n'

        self.ui.inherit_label.setText(label)


    def set_inheritance(self):
        """"Add Asset Inheritance."""

        inherit_ui = SetInheritance(asset=self.asset)
        inherit_ui.ui.comboBox.addItems(['<NONE>']+self.assets)

        inheritance = self.info.get('inherit_from') or []
        for i_info in inheritance:
            text = i_info.get('asset')
            inherit_ui.ui.comboBox.setCurrentText(text)
            if i_info.get('inherit_guide'):
                inherit_ui.ui.checkBox.setChecked(True)

        inherit_ui.exec_()

        self.info = env.get_asset_info(verbose=False) or {}
        self.populate_inheritance()

    def add_variant(self):
        """"Add Asset Inheritance."""

        variant_ui = AddVariant(asset=self.asset)
        variant_ui.exec_()

        self.info = env.get_asset_info(verbose=False) or {}
        self.populate_variants()

    def take_thumbnail_snapshot(self):
        """Take a thumbnail snapshot for the selected asset."""

        self.clear_thumbnail()

        icon_path = os.path.join(self.rigbuild_path, 'thumbnail.jpg')

        if os.path.isdir(self.rigbuild_path):
            current_sel = mc.ls(sl=1, l=1)
            mc.select(cl=1)

            # Create icon
            mc.playblast(fr=mc.currentTime(q=1), cf=icon_path,
                        format='image',
                        clearCache=0,
                        viewer=0,
                        showOrnaments=0,
                        offScreen=1,
                        percent=100,
                        compression= 'jpg',
                        quality=25,
                        widthHeight=[213, 120])

            if os.path.isfile(icon_path):
                mayaWidget.set_icon(self.ui.thumb_label, icon_path)

            else:
                mayaWidget.set_icon(self.ui.thumb_label, 'thumbnail_213x120.png')
                mc.warning ('Could not save image!')

            mc.select(current_sel)

    def clear_thumbnail(self):
        """deletes the thumbnail from disk for the selected asset."""

        icon_path = os.path.join(self.rigbuild_path, 'thumbnail.jpg')

        if os.path.isfile(icon_path):
            os.remove(icon_path)

        mayaWidget.set_icon(self.ui.thumb_label, 'thumbnail_213x120.png')

class SetInheritance(wdg.QDialog):

    def __init__(self, asset=''):
        super(SetInheritance, self).__init__(mayaWidget.maya_main_window)

        title = 'setInheritance_UI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = setInheritance_ui.Ui_Form()
        self.ui.setupUi(self)
        self.setObjectName(title)

        self.asset = asset

        self.ui.cancel_btn.released.connect(self.deleteLater)
        self.ui.set_btn.released.connect(self.set_inheritance)

    def set_inheritance(self):

        inherit_guide = self.ui.checkBox.isChecked()
        inherit_asset = self.ui.comboBox.currentText()

        if inherit_asset == '<NONE>':
            env.add_inheritance(remove_all=True)

        else:
            env.add_inheritance(
                inherit_from=inherit_asset,
                inherit_guide=inherit_guide,
                inherit_path=True,
                inherit_model=False,
                overwrite=True)

        self.deleteLater()


class AddVariant(wdg.QDialog):

    def __init__(self, asset=''):
        super(AddVariant, self).__init__(mayaWidget.maya_main_window)

        title = 'createVariant_UI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = variant_ui.Ui_Form()
        self.ui.setupUi(self)
        self.setObjectName(title)

        self.asset = asset

        self.ui.cancel_btn.released.connect(self.deleteLater)
        self.ui.set_btn.released.connect(self.add_variant)
        self.ui.comboBox.currentIndexChanged.connect(self.update_line_edit)

        self.update_line_edit()

    def update_line_edit(self):

        if self.ui.comboBox.currentText() == 'other ...':
            self.ui.lineEdit.show()
        else:
            self.ui.lineEdit.hide()

    def add_variant(self):

        set_primary = self.ui.checkBox.isChecked()
        name = self.ui.comboBox.currentText()

        if name == 'other ...':
            name = self.ui.lineEdit.text()

        env.add_variant(name, set_primary=set_primary)
        self.deleteLater()


main_UI = None

def run():
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
        try:
            global main_UI
            main_UI.run(floating=True)

        except:
            main_UI = Main()
            main_UI.run(floating=True)

        return main_UI

    except Exception as e:
        raise RuntimeError(e)
