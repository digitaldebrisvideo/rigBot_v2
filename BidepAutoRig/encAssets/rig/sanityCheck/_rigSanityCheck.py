"""
    rigSanityCheck by Jennifer Hachigian

    Executes safety checks before the rig gets published.

    v001 - auto_fixes()
    v002 - now flags problems that require human intervention.
    v003 - now deletes unused nodes.
    v004 - offers publishing option and a tabbed interface.
    v005 - disables the closing of windows in the autofix section.
    v006 - implemented character rigger requests -- closing specific windows, launching Mango PWF after publishing,
           creating the "rigs" folder if it does not exist, ability to add a comment to the DAT and clipboard.
    v007 - now includes expected Mango published location in the *.dat file.
    v009 - autofixes now removes Turtle nodes and disables the Turtle plugin
    v013 - autofixes now focus on transforms specifically when deleting animation on *_anim objects
    v014 - now checks if sys paths are present before attempting to append them.
    v015 - now works with both Maya 2017 (PySide2) and Maya 2014 (PySide)
    v016 - bugfix for autofix' lock anim parents. Removed layer check.
    v018 - rescan now includes "libr"
    v019 - rescan now includes "blkl"
    v020 - Publish now default tab; Auto-Fixes have separate button and launches on start ONLY if user agrees.
    v021 - rescan now includes "exgf"
    v022 - autofixes now include a routine to lock/hide visibility on "*_anim" objects.
    v023 - rescan now includes "seal"
    v024 - rescan now consults projects_list.json for list of projects to scan.
    v025 - now remembers/restores window position in "encToolsSettings.ini" (located in user's Documents folder)
    v026 - added "dispRS" to Encore-compatible name check in tests.
    v027 - added "dispRS" to Encore-compatible name check in tests. (???)
    v028 - reordered Mango publish to take place before publishing the rig.
    v029 - added Shotgun tab and Shotgun integration.
    v030 - removed Shotgun tab, replaced Publish button ghosting behavior with clear warning.
    v031 - added additional "type" filters (Character, Vehicle, Prop, and Building)
    v032 - added Cherie Rye's removeMentalRay to the auto_fixes() routine.
    v033 - updated Shotgun Asset type to CustomNonProjectEntity05; new safety check forces the user to enter a comment;
           now prevents hot keys from accidentally executing outside of the PySide UI while the PySide UI has focus.
    v034 - added filters for "Environment" and "None"
    v035 - disabled "test_lo_res_names()" in "tests()" routine.
    v036 - added a search filter for Shotgun list. Includes case-sensitive checkbox option.
"""

import pymel.core as pm
import maya.OpenMaya as om
import os

# import PySide.QtCore as QtCore
# import PySide.QtGui as QtGui

import autofixes as auto
import blacklist as blk
import publish as pub
import rescan as scan
import shotgun as sgun
import tests as test

import encLib as enc
reload(enc)
from PySide2 import QtCore, QtGui, QtWidgets

reload(enc)
reload(auto)
reload(test)
reload(pub)
reload(scan)
reload(blk)
reload(sgun)

__author__ = 'jhachigian'

script_dir = os.path.basename(__file__)
icon_check = os.path.join(script_dir, "icon_checkbox_16x16.png")
icon_warning = os.path.join(script_dir, "icon_warning_16x16.png")

'''
========================================================================
---->  Global Variables  <----
========================================================================
'''

TOOLS_PATH = os.path.dirname(__file__)

WINDOW_TITLE = 'Rig Sanity Check'
WINDOW_VERSION = 1.37
WINDOW_NAME = 'rigSanityCheck_tool_window'

UI_FILE_PATH = os.path.join(TOOLS_PATH, '_rigSanityCheck.ui')
UI_OBJECT, BASE_CLASS = enc.get_pyside_class(UI_FILE_PATH)

'''
========================================================================
---->  Create/Connect UI Functionality  <----
========================================================================
'''


class RigSanityCheck(BASE_CLASS, UI_OBJECT):
    def __init__(self, parent=enc.get_maya_window()):
        super(RigSanityCheck, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle('{0} {1}'.format(WINDOW_TITLE, str(WINDOW_VERSION)))

        self.setFocus()
        self.setFixedWidth(640)
        self.setFixedHeight(630)
        self.red_highlight = QtGui.QColor(200, 0, 0)
        self.green_highlight = QtGui.QColor(0, 200, 0)
        self.black = QtGui.QColor(0, 0, 0)
        self.grey = QtGui.QColor(64, 64, 64)
        self.c_row = 0
        self.data = {"comment": "", "project_info": None, "workfiles_path": None, "sg_users_current": None,
                     "sg_projects": None, "sg_assets": None, "sg_users": None, "sg_asset_selected": None,
                     "sg_show_selected": None,
                     "sg_paths": {"mango_publish": None, "rig_publish": None, "rig_backup": None},
                     "mango_publish_version": ""}
        """ init UI """
        self.ctrls = {self.chrCheckBox: "chr", self.prpCheckBox: "prp",
                      self.vehCheckBox: "veh", self.blgCheckBox: "bdg",
                      self.envCheckBox: "env", self.noneCheckBox: None}
        for ctrl in self.ctrls:
            ctrl.addAction(self.actionShotgunSelectAll)
            ctrl.addAction(self.actionShotgunSelectNone)
        self.plainTextEdit.setReadOnly(True)
        self.settings_path = os.path.join(os.getenv('HOME'), "encToolsSettings.ini")
        self.restore_saved_window_geometry()
        self.show()
        try:
            self.update_test_table()
            self.update_test_text(self.c_row, 0)
            self.update_publish_path_and_ui()
            self.update_publish_table()
            self.update_character_notes_display()
            auto.auto_check()
            maya_path = pm.system.sceneName()
            self.data["project_info"] = enc.getProjectDict(maya_path)
            self.data["workfiles_path"] = os.path.join(self.data["project_info"]["dir3d"], "publish", "workfiles",
                                                       self.data["project_info"]["type"] + "_" +
                                                       self.data["project_info"]["task"])
            print self.data["workfiles_path"]
            sgun.init_shotgun_ui(self)
            self.tabWidget.setCurrentIndex(0)
        except BaseException as e:
            print "Whoops...", e
            """ disable tabs """
            self.tabSanityCheck.setEnabled(False)
            self.tabNote.setEnabled(False)
            self.tabWidget.setCurrentIndex(1)
            """ disable controls on Publish tab """
            self.publishTableWidget.setEnabled(False)
            self.publishLineEdit.setEnabled(False)
            self.commentTextEdit.setEnabled(False)
            self.publishButton.setEnabled(False)
            self.publishOpenFolder.setEnabled(False)
            print "Could not initialize everything."
        """ hook up UI """
        self.tableWidget.cellClicked.connect(self.update_test_text)
        self.autoButton.clicked.connect(auto.auto_fixes)
        self.retestButton.clicked.connect(self.retest)
        self.closeButton.clicked.connect(self.close)
        self.publishOpenFolder.clicked.connect(self.open_publish_folder)
        self.publishTableWidget.cellClicked.connect(self.update_publish_path_and_ui)
        self.publishLineEdit.textChanged.connect(self.update_publish_filename)
        self.rescanButton.clicked.connect(self.update_asset_manager)
        self.publishButton.clicked.connect(self.publish_rig)
        self.blacklistButton.clicked.connect(self.add_to_blacklist)
        self.relistButton.clicked.connect(self.remove_from_blacklist)
        self.filterAssigneeComboBox.currentIndexChanged.connect(lambda: sgun.update_shotgun_assets(self))
        self.filterStatusComboBox.currentIndexChanged.connect(lambda: sgun.update_shotgun_assets(self))
        self.actionShotgunSelectAll.triggered.connect(lambda: self.ui_shotgun_select(True))
        self.actionShotgunSelectNone.triggered.connect(lambda: self.ui_shotgun_select(False))
        self.chrCheckBox.stateChanged.connect(lambda: sgun.update_shotgun_assets(self))
        self.prpCheckBox.stateChanged.connect(lambda: sgun.update_shotgun_assets(self))
        self.vehCheckBox.stateChanged.connect(lambda: sgun.update_shotgun_assets(self))
        self.blgCheckBox.stateChanged.connect(lambda: sgun.update_shotgun_assets(self))
        self.envCheckBox.stateChanged.connect(lambda: sgun.update_shotgun_assets(self))
        self.noneCheckBox.stateChanged.connect(lambda: sgun.update_shotgun_assets(self))
        self.filterLineEdit.textChanged.connect(lambda: sgun.update_shotgun_ui_assets(self))
        self.mcCheckBox.stateChanged.connect(lambda: sgun.update_shotgun_ui_assets(self))

    def restore_saved_window_geometry(self):
        """
        Restores the geometry of the PySide window from an INI file in the root of the user's Documents folder.
        Because the width/height of the window is fixed, this will only restore the position of the window.

        Code solution by Green Cell on stackoverflow.

        :return: None
        """
        if os.path.exists(self.settings_path):
            settings_obj = QtCore.QSettings(self.settings_path, QtCore.QSettings.IniFormat)
            geo = settings_obj.value("rigSanityCheckWindowGeometry")
            if geo is not None:
                self.restoreGeometry(geo)

    def closeEvent(self, event):
        """
        Writes the geometry of the PySide window to an INI file in the root of the user's Documents folder.

        Code solution by Green Cell on stackoverflow.

        :param event:
        :return: None
        """
        settings_obj = QtCore.QSettings(self.settings_path, QtCore.QSettings.IniFormat)
        settings_obj.setValue("rigSanityCheckWindowGeometry", self.saveGeometry())

    def keyPressEvent(self, event):
        """
        This stops Maya from misinterpreting hotkeys meant for the PySide UI (ex: Shift-F)

        :param event:
        :return:
        """
        pass

    """ Test Tab """

    def update_test_table(self):
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Test Results", "Pass/Fail"])
        keys = test.checklist["tests"].keys()
        keys.sort()
        self.tableWidget.setRowCount(len(keys))
        d = {True: "Passed.", False: "FAILED."}
        flaws = []
        for i, key in enumerate(keys):
            val = test.checklist["tests"][key]
            col1 = QtWidgets.QTableWidgetItem(key)
            col2 = QtWidgets.QTableWidgetItem(d[val])
            if not val:
                col2.setBackground(self.red_highlight)
                col2.setForeground(self.black)
                flaws.append(i)
            self.tableWidget.setItem(i, 0, col1)
            self.tableWidget.setItem(i, 1, col2)
        if flaws:
            self.c_row = flaws[0]
            self.tableWidget.setCurrentCell(flaws[0], 0)
            self.passFailLineEdit.setText("FAILED.")
            pal = self.passFailLineEdit.palette()
            pal.setColor(self.passFailLineEdit.backgroundRole(), self.red_highlight)
            pal.setColor(self.passFailLineEdit.foregroundRole(), self.black)
            icon_color = self.red_highlight
        else:
            self.c_row = 0
            self.tableWidget.setCurrentCell(0, 0)
            self.passFailLineEdit.setText("PASSED.")
            pal = self.passFailLineEdit.palette()
            pal.setColor(self.passFailLineEdit.backgroundRole(), self.green_highlight)
            pal.setColor(self.passFailLineEdit.foregroundRole(), self.black)
            icon_color = self.green_highlight
        pix_map = QtGui.QPixmap(16, 16)
        pix_map.fill(icon_color)
        icon = QtGui.QIcon(pix_map)
        self.tabWidget.setTabIcon(0, icon)
        self.passFailLineEdit.setPalette(pal)

    def update_test_text(self, row, column):
        self.plainTextEdit.clear()
        key = self.tableWidget.item(row, 0).text()
        if key in test.checklist["messages"]:
            text = test.checklist["messages"][key]
            self.plainTextEdit.setPlainText(text)

    def retest(self):
        test.tests()
        self.c_row = 0
        self.update_test_table()
        self.update_test_text(self.c_row, 0)

    """ Publish Tab """

    def ui_shotgun_select(self, state):
        for ctrl in self.ctrls:
            ctrl.setChecked(state)

    def blacklist_color(self, item):
        item.setForeground(self.grey)

    def add_to_blacklist(self):
        p = self.get_output_path()
        print "Blacklisting:", p
        blk.insert_path(p)
        self.update_publish_table()
        """ messageBox """
        filename = self.get_text()
        msg = "%s added to blacklist." % filename
        pm.confirmDialog(title='Done', message=msg)
        """ update blacklist buttons """
        self.update_blacklist_buttons()

    def remove_from_blacklist(self):
        p = self.get_output_path()
        print "Allowing:", p
        blk.remove_path(p)
        self.update_publish_table()
        """ messageBox """
        filename = self.get_text()
        msg = "%s removed from blacklist." % filename
        pm.confirmDialog(title='Done', message=msg)
        """ update blacklist buttons """
        self.update_blacklist_buttons()

    def get_text(self):
        text = self.publishLineEdit.text()
        for c in "\n\r<>:\"/\|?* ":
            text = text.replace(c, "")
        return text

    def open_publish_folder(self):
        folder = pub.publishDict["rigFolder"]
        enc.openFolder(folder)

    def update_publish_text(self, row):
        if self.publishTableWidget.hasFocus():
            if row == -1:
                text = ""
            else:
                text = self.publishTableWidget.item(row, 0).text()
            self.publishLineEdit.setText(text)

    def get_output_path(self):
        folder = pub.publishDict["rigFolder"]
        filename = self.get_text()
        ext = pm.system.sceneName().split(".")[-1]
        if filename and ext:
            filename += "." + ext
        path = os.path.join(folder, filename)
        return path

    def update_publish_label(self):
        path = self.get_output_path()
        abb = "Output: Z:\\..." + path.split("--assets")[-1]
        self.publishPathLabel.setText(abb)

    def update_blacklist_buttons(self):
        row = self.publishTableWidget.currentRow()
        item = self.publishTableWidget.item(row, 0)
        if item is not None:
            is_greyed_out = item.foreground().color() == self.grey
            self.blacklistButton.setEnabled(not is_greyed_out)
            self.relistButton.setEnabled(is_greyed_out)

    def update_publish_path_and_ui(self):
        row = self.publishTableWidget.currentRow()
        self.update_publish_text(row)
        self.update_publish_label()
        """ update blacklist buttons """
        self.update_blacklist_buttons()

    def update_publish_filename(self):
        if self.publishLineEdit.hasFocus():
            self.publishTableWidget.clearSelection()
            self.update_publish_label()

    def update_publish_table(self):
        blacklist = blk.get_blacklist()
        selected = self.publishTableWidget.selectedRanges()
        self.publishTableWidget.clear()
        self.publishTableWidget.setHorizontalHeaderLabels(["File", "Date", "Size"])
        keys = pub.publishDict["rigs"].keys()
        keys.sort()
        self.publishTableWidget.setRowCount(len(keys))
        self.publishTableWidget.setColumnWidth(0, 293)
        self.publishTableWidget.setColumnWidth(1, 150)
        for i, key in enumerate(keys):
            date = pub.publishDict["rigs"][key]["timestamp"]
            size = pub.publishDict["rigs"][key]["size"]
            path = pub.publishDict["rigs"][key]["path"]
            col1 = QtWidgets.QTableWidgetItem(key)
            col2 = QtWidgets.QTableWidgetItem(date)
            col3 = QtWidgets.QTableWidgetItem(size)
            if path in blacklist:
                for col in [col1, col2, col3]:
                    self.blacklist_color(col)
            self.publishTableWidget.setItem(i, 0, col1)
            self.publishTableWidget.setItem(i, 1, col2)
            self.publishTableWidget.setItem(i, 2, col3)
        """ restore selection, if applicable """
        for sel in selected:
            self.publishTableWidget.setRangeSelected(sel, True)

    def update_asset_manager(self):
        temp = self.publishPathLabel.text()
        self.publishPathLabel.setText("Updating Asset Manager... (this could take a minute or two...)")
        self.publishPathLabel.repaint()
        scan.rescan_assets()
        msg = "Asset Manager updated."
        print msg
        pm.confirmDialog(title='Done', message=msg)
        self.publishPathLabel.setText(temp)

    def safety_check_text(self):
        """
        :return: Boolean
        """
        msg_list = []
        """ did the user make a Shotgun selection? """
        if not sgun.shotgun_test(self):
            msg_list.append("No Shotgun selection defined.")
        """ did the user choose an output filename? """
        if not self.get_text():
            msg_list.append("No output filename chosen.")
        """ did the user enter a comment? """
        if not self.commentTextEdit.toPlainText():
            msg_list.append("No comment entered.")
        """ notify the user if something went wrong. """
        if msg_list:
            msg = "\r\n\r\n".join(msg_list)
            pm.confirmDialog(title='ERROR', message=msg, icon='critical')
            return False
        """ return True if nothing went wrong. """
        return True

    def update_comment(self):
        comment = self.commentTextEdit.toPlainText()
        """ copy comment to clipboard """
        QtWidgets.QApplication.clipboard().setText(comment)
        self.data["comment"] = comment

    def safety_check_mango(self):
        work_dir = self.data["workfiles_path"]
        old_versions = [x for x in os.listdir(work_dir) if x.startswith("v") and len(x) == 5]
        success = pub.publish_mango()  # catches whether the user COULD launch Mango.
        new_versions = [x for x in os.listdir(work_dir) if x.startswith("v") and len(x) == 5]
        if success and (len(new_versions) == len(old_versions)):
            """ the user successfully launched Mango, but cancelled the publish """
            msg = "Mango publish failed. Cancelling rig publish."
            print msg
            pm.confirmDialog(title='ERROR', message=msg, icon='critical')
            return False
        """ update the Shotgun path data """
        self.data["sg_paths"]["mango_publish"] = pub.get_latest_published_workfile(self.data["workfiles_path"])
        """ update the mango_publish_version data """
        li = [x for x in new_versions if x not in old_versions]
        if li:
            li.sort(reverse=True)
            self.data["mango_publish_version"] = li[0]
        return True

    @enc.apply_wait_cursor
    def publish_rig_routine(self):
        ui_msg = "Publishing rig..."
        om.MGlobal.displayInfo(ui_msg)
        self.publishPathLabel.setText(ui_msg)
        pub.update_rig_comment(self.data["comment"], mango_publish_version=self.data["mango_publish_version"])
        src = pm.system.sceneName()
        dst = self.get_output_path()
        self.data["sg_paths"]["rig_publish"] = dst
        title, msg = pub.publish_rig(src, dst)
        """ back up published rig """
        if title != "FAILED":
            scan.insert_path(dst)
            self.data["sg_paths"]["rig_backup"] = pub.backup_rig(src, dst, comment=self.data["comment"])
        print(msg)
        pub.update_publish_dict()
        self.update_publish_table()
        self.update_character_notes_display()
        """ publish to Shotgun """
        if title != "FAILED" and not self.shotgunCheckBox.isChecked():
            print "Publishing to Shotgun..."
            selected_asset = self.shotgunListWidget.currentItem().text()
            self.data["sg_asset_selected"] = selected_asset
            sgun.publish_rig_to_shotgun(self.data)
        print("Done.")
        if title == "FAILED":
            ui_msg = "FAILED. See Script Editor for details. ({0})".format(pub.TIMESTAMP)
            warning = "Could not publish file due to permissions issues."
            om.MGlobal.displayWarning(warning)
            print msg
        else:
            ui_msg = "Rig successfully published ({0}): {1}".format(pub.TIMESTAMP, msg)
            om.MGlobal.displayInfo(ui_msg)
        self.publishPathLabel.setText(ui_msg)
        # pm.confirmDialog(title=title, message=msg, icon=icon)

    def publish_rig(self):
        if not self.safety_check_text():
            return
        """ update world_anim comment and copy comment to clipboard """
        self.update_comment()
        """ Mango publish """
        if not self.safety_check_mango():
            return
        """ rig publish """
        self.publish_rig_routine()

    """ Character Record Tab """

    def update_character_notes_display(self):
        self.crTextEdit.clear()
        if not pm.objExists("world_anim"):
            return

        n = pm.PyNode("world_anim")
        if not n.hasAttr("notes"):
            return

        text = n.getAttr("notes")
        self.crTextEdit.setText(text)


def launch():
    """
    run autofixes and tests

    :return: None
    """
    test.tests()
    pub.update_publish_dict()

    """ launch UI """
    global rig_sanity_check
    try:
        rig_sanity_check.close()
    except:
        rig_sanity_check = RigSanityCheck()

    # from pprint import pprint
    # pprint(checklist)
