"""

    encAssetRenamer by Jennifer Hachigian

    created 8/31/2016

    usage: select objects and hit "Apply" to give them Encore-formatted names.

    v002 - now renames always in root namespace, regardless of the current namespace
    v003 - now checks if sys paths are present before attempting to append them.
    v004 - now works with both Maya 2017 (PySide2) and Maya 2014 (PySide)
    v005 - now offers an option to auto-number geo descriptions.
    v006 - replaced Qt with direct PySide2 connection to accommodate Mango + Legacy Render Layers.

"""

import os
# import PySide.QtCore as QtCore
# import PySide.QtGui as QtGui
import re

import pymel.core as pm
import encLib as enc
# from Qt import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets

reload(enc)


'''
========================================================================
---->  Global Variables and Functions <----
========================================================================
'''

TOOLS_PATH = os.path.dirname(__file__)

WINDOW_TITLE = 'AssetRenamer'
WINDOW_VERSION = 1.07
WINDOW_NAME = 'assetRenamer_tool_window'

UI_FILE_PATH = os.path.join(TOOLS_PATH, 'assetRenamer.ui')
UI_OBJECT, BASE_CLASS = enc.get_pyside_class(UI_FILE_PATH)

'''
========================================================================
---->  Create/Connect UI Functionality  <----
========================================================================
'''


def validate(text):
    pattern1 = re.compile("^[a-z][a-zA-Z0-9]*$")
    pattern2 = re.compile("[^a-zA-Z0-9]")
    fixed = text
    if len(text) == 0:
        warning = "Zero-length labels are not acceptable."
        fixed = "x"
    elif text[0] not in "abcdefghijklmnopqrstuvwxyz":
        warning = "Labels must start with a lowercase letter."
        if text[0].isalpha():
            fixed = text[0].lower() + text[1:]
        else:
            fixed = "x"
    elif not pattern1.findall(text):
        warning = "Objects may only use letters and numbers in their names."
        fixed = re.sub(pattern2, "", text)
    else:
        """ return text as-is """
        warning = ""
    return warning, fixed


def init_combobox(cb, text):
    i = cb.findText(text)
    if i != -1:
        cb.setCurrentIndex(i)


class AssetRenamer(BASE_CLASS, UI_OBJECT):
    def __init__(self, parent=enc.get_maya_window()):
        super(AssetRenamer, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle('{0} {1}'.format(WINDOW_TITLE, str(WINDOW_VERSION)))

        """ init data"""
        self.data = {}
        self.init_and_update()
        self.red_highlight = QtGui.QColor(200, 0, 0)
        self.black = QtGui.QColor(0, 0, 0)
        p = self.warningLabel.palette()
        self.bg_color = p.color(self.warningLabel.backgroundRole())
        self.text_color = p.color(self.warningLabel.foregroundRole())
        # self.setFixedSize(800, 330)

        """ launch script job """
        self.SCRIPT_JOB_NUMBER = pm.scriptJob(event=["SelectionChanged", self.init_and_update], protected=True)

        """ init behaviors """
        self.modelTypeComboBox.currentIndexChanged.connect(self.update)
        self.assetNameLineEdit.textChanged.connect(self.validate_and_update)
        self.geoDescLineEdit.textChanged.connect(self.validate_and_update)
        self.assetNameLineEdit.editingFinished.connect(self.asset_repair_and_update)
        self.geoDescLineEdit.editingFinished.connect(self.geo_repair_and_update)
        self.resTypeComboBox.currentIndexChanged.connect(self.update)
        self.geoTypeComboBox.currentIndexChanged.connect(self.update)
        self.dispTypeComboBox.currentIndexChanged.connect(self.update)
        self.subTypeComboBox.currentIndexChanged.connect(self.update)
        self.rndrTypeComboBox.currentIndexChanged.connect(self.update)
        self.geoNumCheckBox.stateChanged.connect(self.update)
        self.closeButton.clicked.connect(self.close)
        self.applyButton.clicked.connect(self.rename)

    def keyPressEvent(self, event):
        pass

    def closeEvent(self, event):
        """
        :param event: closing the UI
        :return: kill the scriptJob when the UI is closed.
        """
        pm.cmds.scriptJob(kill=self.SCRIPT_JOB_NUMBER, force=True)
        super(AssetRenamer, self).closeEvent(event)

    def get_num(self, i):
        num = self.numTypeComboBox.currentIndex()
        if num == 0:
            return "X"
        elif num == 1:
            return "%03d" % (i + 1)
        return "abcdefghijklmnopqrstuvwxyz"[i]

    def init_asset_and_geo(self):
        sel = pm.ls(selection=True, type='transform')
        if not sel:
            return

        name = sel[0].name()
        bits = name.split("_")

        if len(bits) < 6:
            return

        init_combobox(self.modelTypeComboBox, bits[0])
        self.assetNameLineEdit.setText(bits[1])
        self.geoDescLineEdit.setText(bits[2])
        # init_combobox(self.numTypeComboBox, bits[3])
        init_combobox(self.resTypeComboBox, bits[4])
        init_combobox(self.geoTypeComboBox, bits[5])

        if len(bits) < 9:
            return

        init_combobox(self.dispTypeComboBox, bits[6])
        init_combobox(self.subTypeComboBox, bits[7])
        init_combobox(self.rndrTypeComboBox, bits[8])

    def get_new_name(self, i):
        mod = self.modelTypeComboBox.currentText()
        ast = self.assetNameLineEdit.text()
        dsc = self.geoDescLineEdit.text()
        num = self.get_num(i)
        res = self.resTypeComboBox.currentText()
        geo = self.geoTypeComboBox.currentText()
        dsp = self.dispTypeComboBox.currentText()
        sub = self.subTypeComboBox.currentText()
        rdr = self.rndrTypeComboBox.currentText()
        if self.geoNumCheckBox.isChecked():
            dsc += "%03d" % i
        if geo in ["lgt", "ctl"]:
            new_name = "%s_%s_%s_%s_%s_%s_" % (mod, ast, dsc, num, res, geo)
        else:
            new_name = "%s_%s_%s_%s_%s_%s_%s_%s_%s_" % (mod, ast, dsc, num, res, geo, dsp, sub, rdr)
        return new_name

    def update_warning_label(self, text):
        self.warningLabel.setText(text)
        p = self.warningLabel.palette()
        if text:
            p.setColor(self.warningLabel.backgroundRole(), self.red_highlight)
            p.setColor(self.warningLabel.foregroundRole(), self.black)
        else:
            p.setColor(self.warningLabel.backgroundRole(), self.bg_color)
            p.setColor(self.warningLabel.foregroundRole(), self.text_color)
        self.warningLabel.setPalette(p)

    def update_data(self):
        self.data = {}
        sel = pm.ls(selection=True, type='transform')
        for i, obj in enumerate(sel):
            new_name = self.get_new_name(i)
            self.data[obj] = obj.shortName(), new_name

    def update_table(self):
        """
        :return: populate the Import Table Widget with the before/after names.
        """
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Before", "After"])
        li = self.data.keys()
        li.sort()
        rowcount = len(li)
        self.tableWidget.setRowCount(rowcount)
        for row, key in enumerate(li):
            old_name, new_name = self.data[key]
            before = QtWidgets.QTableWidgetItem(old_name)
            after = QtWidgets.QTableWidgetItem(new_name)
            self.tableWidget.setItem(row, 0, before)
            self.tableWidget.setItem(row, 1, after)

    def validate_and_update(self, text):
        warning, new_name = validate(text)
        self.update_warning_label(warning)
        self.update()

    def update(self):
        self.update_data()
        self.update_table()

    def init_and_update(self):
        self.init_asset_and_geo()
        self.update()

    def asset_repair_and_update(self):
        text = self.assetNameLineEdit.text()
        warning, new_name = validate(text)
        if new_name != text:
            self.assetNameLineEdit.setText(new_name)
        self.update_warning_label("")
        self.update()

    def geo_repair_and_update(self):
        text = self.geoDescLineEdit.text()
        warning, new_name = validate(text)
        if new_name != text:
            self.geoDescLineEdit.setText(new_name)
        self.update_warning_label("")
        self.update()

    @enc.in_root_namespace
    def rename(self):
        for obj in self.data:
            new_name = self.data[obj][1]
            obj.rename(new_name)
        self.update()


def launch():
    print "Launching..."
    global asset_renamer
    try:
        asset_renamer.close()
    except:
        asset_renamer = AssetRenamer()
        asset_renamer.show()
