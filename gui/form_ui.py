# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/net/homes/bhamilton/maya/scripts/rigBot/gui/form.ui'
#
# Created: Tue May 22 17:31:03 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtGui, QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(623, 811)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(40, 35))
        self.label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(89, 89, 89);")
        self.label.setIndent(10)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setObjectName("toolBox")
        self.assetPage = QtWidgets.QWidget()
        self.assetPage.setGeometry(QtCore.QRect(0, 0, 694, 669))
        self.assetPage.setObjectName("assetPage")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.assetPage)
        self.verticalLayout_11.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.splitter = QtWidgets.QSplitter(self.assetPage)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.jobFrame = QtWidgets.QFrame(self.splitter)
        self.jobFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.jobFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.jobFrame.setObjectName("jobFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.jobFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.jobsGrp = QtWidgets.QGroupBox(self.jobFrame)
        self.jobsGrp.setObjectName("jobsGrp")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.jobsGrp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.jobsCmb = QtWidgets.QComboBox(self.jobsGrp)
        self.jobsCmb.setObjectName("jobsCmb")
        self.jobsCmb.addItem("")
        self.jobsCmb.addItem("")
        self.verticalLayout.addWidget(self.jobsCmb)
        self.verticalLayout_4.addWidget(self.jobsGrp)
        self.assetsGrp = QtWidgets.QGroupBox(self.jobFrame)
        self.assetsGrp.setObjectName("assetsGrp")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.assetsGrp)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.assetsList = QtWidgets.QListWidget(self.assetsGrp)
        self.assetsList.setObjectName("assetsList")
        QtWidgets.QListWidgetItem(self.assetsList)
        QtWidgets.QListWidgetItem(self.assetsList)
        QtWidgets.QListWidgetItem(self.assetsList)
        QtWidgets.QListWidgetItem(self.assetsList)
        self.verticalLayout_3.addWidget(self.assetsList)
        self.newAssetBtn = QtWidgets.QPushButton(self.assetsGrp)
        self.newAssetBtn.setObjectName("newAssetBtn")
        self.verticalLayout_3.addWidget(self.newAssetBtn)
        self.verticalLayout_4.addWidget(self.assetsGrp)
        self.verticalLayout_4.setStretch(1, 1)
        self.infoFrame = QtWidgets.QFrame(self.splitter)
        self.infoFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.infoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infoFrame.setObjectName("infoFrame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.infoFrame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.userGrp = QtWidgets.QGroupBox(self.infoFrame)
        self.userGrp.setObjectName("userGrp")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.userGrp)
        self.verticalLayout_9.setContentsMargins(9, -1, 9, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.userCmb = QtWidgets.QComboBox(self.userGrp)
        self.userCmb.setObjectName("userCmb")
        self.userCmb.addItem("")
        self.userCmb.addItem("")
        self.userCmb.addItem("")
        self.verticalLayout_9.addWidget(self.userCmb)
        self.verticalLayout_8.addWidget(self.userGrp)
        self.infoGrp = QtWidgets.QGroupBox(self.infoFrame)
        self.infoGrp.setObjectName("infoGrp")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.infoGrp)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.infoList = QtWidgets.QListWidget(self.infoGrp)
        self.infoList.setObjectName("infoList")
        self.verticalLayout_10.addWidget(self.infoList)
        self.newRigTypeBtn = QtWidgets.QPushButton(self.infoGrp)
        self.newRigTypeBtn.setObjectName("newRigTypeBtn")
        self.verticalLayout_10.addWidget(self.newRigTypeBtn)
        self.verticalLayout_8.addWidget(self.infoGrp)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_11.addWidget(self.splitter)
        self.toolBox.addItem(self.assetPage, "")
        self.buildPage = QtWidgets.QWidget()
        self.buildPage.setGeometry(QtCore.QRect(0, 0, 694, 669))
        self.buildPage.setObjectName("buildPage")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.buildPage)
        self.verticalLayout_12.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.assetLabel = QtWidgets.QLabel(self.buildPage)
        self.assetLabel.setMinimumSize(QtCore.QSize(40, 30))
        self.assetLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.assetLabel.setFont(font)
        self.assetLabel.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(89, 89, 89);")
        self.assetLabel.setIndent(10)
        self.assetLabel.setObjectName("assetLabel")
        self.verticalLayout_12.addWidget(self.assetLabel)
        self.buildTabs = QtWidgets.QTabWidget(self.buildPage)
        self.buildTabs.setObjectName("buildTabs")
        self.guidesTab = QtWidgets.QWidget()
        self.guidesTab.setObjectName("guidesTab")
        self.buildTabs.addTab(self.guidesTab, "")
        self.buildTab = QtWidgets.QWidget()
        self.buildTab.setObjectName("buildTab")
        self.buildTabs.addTab(self.buildTab, "")
        self.exportTab = QtWidgets.QWidget()
        self.exportTab.setObjectName("exportTab")
        self.buildTabs.addTab(self.exportTab, "")
        self.spacesTab = QtWidgets.QWidget()
        self.spacesTab.setObjectName("spacesTab")
        self.buildTabs.addTab(self.spacesTab, "")
        self.verticalLayout_12.addWidget(self.buildTabs)
        self.toolBox.addItem(self.buildPage, "")
        self.modulesPage = QtWidgets.QWidget()
        self.modulesPage.setGeometry(QtCore.QRect(0, 0, 605, 665))
        self.modulesPage.setObjectName("modulesPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.modulesPage)
        self.verticalLayout_6.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter_2 = QtWidgets.QSplitter(self.modulesPage)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.modulesTree = QtWidgets.QTreeWidget(self.splitter_2)
        self.modulesTree.setHeaderHidden(True)
        self.modulesTree.setObjectName("modulesTree")
        item_0 = QtWidgets.QTreeWidgetItem(self.modulesTree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.widget = QtWidgets.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.assetLabel_2 = QtWidgets.QLabel(self.widget)
        self.assetLabel_2.setMinimumSize(QtCore.QSize(40, 30))
        self.assetLabel_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.assetLabel_2.setFont(font)
        self.assetLabel_2.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(89, 89, 89);")
        self.assetLabel_2.setIndent(10)
        self.assetLabel_2.setObjectName("assetLabel_2")
        self.verticalLayout_5.addWidget(self.assetLabel_2)
        self.moduleText = QtWidgets.QTextEdit(self.widget)
        self.moduleText.setObjectName("moduleText")
        self.verticalLayout_5.addWidget(self.moduleText)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_6.addWidget(self.splitter_2)
        self.toolBox.addItem(self.modulesPage, "")
        self.verticalLayout_2.addWidget(self.toolBox)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(2)
        self.buildTabs.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCompat.translate("Form", "Form", None, -1))
        self.label.setText(QtCompat.translate("Form", "Rig Build UI", None, -1))
        self.jobsGrp.setTitle(QtCompat.translate("Form", "Jobs", None, -1))
        self.jobsCmb.setItemText(0, QtCompat.translate("Form", "jobA", None, -1))
        self.jobsCmb.setItemText(1, QtCompat.translate("Form", "jobB", None, -1))
        self.assetsGrp.setTitle(QtCompat.translate("Form", "Assets", None, -1))
        __sortingEnabled = self.assetsList.isSortingEnabled()
        self.assetsList.setSortingEnabled(False)
        self.assetsList.item(0).setText(QtCompat.translate("Form", "Finch", None, -1))
        self.assetsList.item(1).setText(QtCompat.translate("Form", "Fawn", None, -1))
        self.assetsList.item(2).setText(QtCompat.translate("Form", "Tentacle", None, -1))
        self.assetsList.item(3).setText(QtCompat.translate("Form", "DudeA", None, -1))
        self.assetsList.setSortingEnabled(__sortingEnabled)
        self.newAssetBtn.setText(QtCompat.translate("Form", "Create New Rig Asset", None, -1))
        self.userGrp.setTitle(QtCompat.translate("Form", "Current User", None, -1))
        self.userCmb.setItemText(0, QtCompat.translate("Form", "bhamiltona", None, -1))
        self.userCmb.setItemText(1, QtCompat.translate("Form", "rgarcia", None, -1))
        self.userCmb.setItemText(2, QtCompat.translate("Form", "wryer", None, -1))
        self.infoGrp.setTitle(QtCompat.translate("Form", "Asset Info", None, -1))
        self.newRigTypeBtn.setText(QtCompat.translate("Form", "Create New Rig Type", None, -1))
        self.toolBox.setItemText(self.toolBox.indexOf(self.assetPage), QtCompat.translate("Form", "Asset Env", None, -1))
        self.assetLabel.setText(QtCompat.translate("Form", "Finch | Gsaavedra", None, -1))
        self.buildTabs.setTabText(self.buildTabs.indexOf(self.guidesTab), QtCompat.translate("Form", "Guides", None, -1))
        self.buildTabs.setTabText(self.buildTabs.indexOf(self.buildTab), QtCompat.translate("Form", "Build Rig", None, -1))
        self.buildTabs.setTabText(self.buildTabs.indexOf(self.exportTab), QtCompat.translate("Form", "Export Data", None, -1))
        self.buildTabs.setTabText(self.buildTabs.indexOf(self.spacesTab), QtCompat.translate("Form", "Spaces", None, -1))
        self.toolBox.setItemText(self.toolBox.indexOf(self.buildPage), QtCompat.translate("Form", "Rig Build", None, -1))
        self.modulesTree.headerItem().setText(0, QtCompat.translate("Form", "Functions", None, -1))
        __sortingEnabled = self.modulesTree.isSortingEnabled()
        self.modulesTree.setSortingEnabled(False)
        self.modulesTree.topLevelItem(0).setText(0, QtCompat.translate("Form", "rigTools", None, -1))
        self.modulesTree.topLevelItem(0).child(0).setText(0, QtCompat.translate("Form", "utils", None, -1))
        self.modulesTree.topLevelItem(0).child(1).setText(0, QtCompat.translate("Form", "control", None, -1))
        self.modulesTree.topLevelItem(0).child(2).setText(0, QtCompat.translate("Form", "spaces", None, -1))
        self.modulesTree.topLevelItem(0).child(3).setText(0, QtCompat.translate("Form", "skincluster", None, -1))
        self.modulesTree.topLevelItem(0).child(4).setText(0, QtCompat.translate("Form", "rigParts", None, -1))
        self.modulesTree.topLevelItem(0).child(4).child(0).setText(0, QtCompat.translate("Form", "bipedArm", None, -1))
        self.modulesTree.topLevelItem(0).child(4).child(1).setText(0, QtCompat.translate("Form", "bipedLeg", None, -1))
        self.modulesTree.topLevelItem(0).child(4).child(2).setText(0, QtCompat.translate("Form", "root", None, -1))
        self.modulesTree.topLevelItem(0).child(4).child(3).setText(0, QtCompat.translate("Form", "splineChain", None, -1))
        self.modulesTree.topLevelItem(0).child(4).child(4).setText(0, QtCompat.translate("Form", "fkChain", None, -1))
        self.modulesTree.setSortingEnabled(__sortingEnabled)
        self.assetLabel_2.setText(QtCompat.translate("Form", "rigTools.utils (utils.py)", None, -1))
        self.moduleText.setHtml(QtCompat.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Help on module rigBot.utils in rigBot:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NAME</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    rigBot.utils</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FILE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    /net/homes/bhamilton/maya/scripts/rigBot/utils.py</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FUNCTIONS</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    camelCaseSplit(input)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Split string base on camel calse</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    checkNodeNames()</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Print clashing non-unique node names.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    cleanName(inputString, keepUnderscores=False)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Convert string with whitespaces or underscores to camelCased string.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    convertUnicode(data)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Converts unicode lists to string</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    exportMayaFile(filePath, nodes, fileType=\'mayaAscii\')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Export selection to maya scene file</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getChildren(node, ad=False, ln=False)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Get children OR all decendants exluding shapes from given node</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getDeformers(shape, deformerType)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Return deformers from shape</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getDistance(nodeA=None, nodeB=None)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Return the world distance between tow given nodes.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getException()</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Throw all nodes in scene into a temp namespace</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        to compare newly built guide nodes. Thissi  to avoid node name clashes.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getLongNames(names)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Return the full name of a given node or nodes</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getMeshData(shape)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Get point coordinatesa and triangles</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getMirrorNodeName(node, leftSide=\'L\', rightSide=\'R\', returnCenter=False)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Return the mirrored side of fgiven node</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getParent(node, ln=False)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Return theparent for the given node</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getSelectedAttrs()</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Print list of selected channelbox attrs.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getSelection()</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Get current selection</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getShapes(node, ii=True, ln=False, ic=False)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Return shape from specified node</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        ii = ignore intermediate objects.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        ln = return long names</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        ic = include locators</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getSide(token, allSides=False)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Get proper side token from config file</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getSuffix(token)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Get suffix settings from config file</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        ARGS:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            \'BIND_JOINT_TOKEN\',</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            \'MOCAP_JOINT_TOKEN\',</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            \'CTRL\',</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            \'OFFSET_CTRL_TOKEN\',</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            \'JOINT\',</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            \'RIG_JOINT_TOKEN\',</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            \'PIVOT_CTRL_TOKEN\'</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getTransform(shape, ln=False)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Get transform parent of given shape node.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        ln = Return long name.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getUniqueName(name)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Get new unique name. Use a &quot;#&quot; to indicate where to place the new</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        letter token.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        USAGE:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        getUniqueName(\'test_#_CTRL\') &gt; will find either</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            &quot;test_CTRL&quot; OR &quot;test_A_CTRL&quot; and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            return &quot;test_B_CTRL&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    getXforms(a=0, t=1, ro=1)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Print world or absolute xforms for selected nodes</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    importMayaFile(filePath)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    importModule(moduleName, className=None, reloadMod=True, verbose=True)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Dynamic module import. Input string of module name and it returns your module.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        you are responsible for instantiating classes and otherwise</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        properly using the module.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        moduleName = String token of the name of the module.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                        NOTE: This will check for its existence first in the sys.path</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                              THEN in the rigBot package.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        ARGS:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            className = string of the class name to instatiate.. you only need this if</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                        you want ot return an instance of the class instead of hte module.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        RETURNS:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            imported module OR instantiated class object</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        USAGE:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            # importing a module</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            myModule = utils.importModule(\'moduleName\')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            # instantiating a class</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            myObject = utils.importModule(\'moduleName\', \'ClassName\')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    joinStrings(inputList, keepUnderscores=True)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Get properly formated prefix and side token</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    printConnections()</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Print connectiosn from selected nodes.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    printList(nlist, columns=None, varname=\'\')</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Print a given list in block columkn format</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    readJson(filePath, verbose=True)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Read json file and return data as dict</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    readPickle(filePath, verbose=True)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Read json file and return data as dict</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    reverseSelection()</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Reverses the current selection order</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    setAttrs(nodes=None, attrs=\'t r s v jo ro ud\', l=False, k=True, cb=False)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Set lock keyable, locked and or cb state for specified attrs.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    setDrawOverride(nodes, displayType=None, setShape=True)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Set drawing override display type</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        KWARGS:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        nodes = nodes to set</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        displayType = 0 - Normal, 1- tempalte, 2- Referenced, None- off (default=None)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    snapLocator(nodes=None, name=\'locator#\', shape=True)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Create a locators centered around selection</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    splitList(myList, num)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Evenly split a list by specified number.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        RETURNS:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        list of lists</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    stripNamespace(name)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Strip name space dagpath name</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    writeJson(filePath, data)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Write dict to json file</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    writePickle(filePath, data)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Write dict to json file</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DATA</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    letters = [\'A\', \'B\', \'C\', \'D\', \'E\', \'F\', \'G\', \'H\', \'I\', \'J\', \'K\', \'L\',...</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, -1))
        self.toolBox.setItemText(self.toolBox.indexOf(self.modulesPage), QtCompat.translate("Form", "Module Library", None, -1))

