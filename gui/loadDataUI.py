# encoding=utf8
from Qt import QtWidgets as wdg
from Qt import QtGui as gui
from Qt import QtCore as qt

import maya.cmds as mc
import maya.mel as mm

from rigBot.gui import mayaWidget
from rigBot.gui import loadData_ui
from rigBot import env
from rigBot import data
from functools import partial

class LoadDataUI(mayaWidget.MayaWidget):

    def __init__(self, parent=None, ignore_missing=False, label=''):
        mayaWidget.MayaWidget.__init__(self, parent=parent)

        title = 'loadData_UI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = loadData_ui.Ui_Form()
        self.ui.setupUi(self)
        self.setObjectName(title)

        self.checkboxes = [c for c in self.ui.filter_frame.children() if 'QCheckBox' in str(type(c))]
        self.checkboxes = [c for c in self.checkboxes if c.whatsThis()]

        self.setMinimumWidth(293)
        self.setMaximumWidth(293)
        self.setMinimumHeight(544)
        self.setMaximumHeight(544)

        # connectiosn
        self.ui.all_chx.stateChanged.connect(self.toggle_all_checkboxes)
        self.ui.remap_chx.toggled.connect(self.toggle_remap_btn)
        self.set_variant_widget()

        self.ui.import_all_btn.released.connect(partial(self.load, custom_path=False))
        self.ui.import_btn.released.connect(self.load)

        self.center()

    def toggle_all_checkboxes(self):
        state = self.ui.all_chx.isChecked()
        for chx in self.checkboxes:
            chx.setChecked(state)

    def toggle_remap_btn(self):
        if self.ui.remap_chx.isChecked():
            self.ui.import_all_btn.setEnabled(0)
        else:
            self.ui.import_all_btn.setEnabled(1)

    def set_variant_widget(self):
        """Set the variant from UI and reset all ui and build list"""

        self.asset = env.get_asset()
        self.variant = env.get_variant()
        self.ui.asset_label.setText('Asset: Not Set!')

        self.ui.variant_cmb.clear()
        if self.asset:
            self.ui.asset_label.setText('Asset: '+self.asset)
            self.ui.variant_cmb.addItem(self.variant)

    def load(self, custom_path=True):

        closest_point = self.ui.cpoint_rdo.isChecked()
        remap = self.ui.remap_chx.isChecked()
        data_types = [c.whatsThis() for c in self.checkboxes if c.isChecked()]

        if not data_types:
            mc.warning('No data types selected!')
            return

        data.load(data_types, remap=remap, closest_point=closest_point, custom_path=custom_path)

def run():
    ui = LoadDataUI()
    ui.show()
