# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bhamilton/Documents/maya/scripts\rigBot\gui\splitBlendTargets.ui'
#
# Created: Sat Jun 30 17:44:47 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtGui, QtCore, QtGui, QtWidgets

class Ui_SplitTargetsUI(object):
    def setupUi(self, SplitTargetsUI):
        SplitTargetsUI.setObjectName("SplitTargetsUI")
        SplitTargetsUI.resize(307, 256)
        self.verticalLayout = QtWidgets.QVBoxLayout(SplitTargetsUI)
        self.verticalLayout.setObjectName("verticalLayout")
        self.assetLabel_2 = QtWidgets.QLabel(SplitTargetsUI)
        self.assetLabel_2.setMinimumSize(QtCore.QSize(40, 30))
        self.assetLabel_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.assetLabel_2.setFont(font)
        self.assetLabel_2.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(40, 40,40);")
        self.assetLabel_2.setIndent(10)
        self.assetLabel_2.setObjectName("assetLabel_2")
        self.verticalLayout.addWidget(self.assetLabel_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(SplitTargetsUI)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(SplitTargetsUI)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(SplitTargetsUI)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.mesh_line = QtWidgets.QLineEdit(SplitTargetsUI)
        self.mesh_line.setObjectName("mesh_line")
        self.gridLayout.addWidget(self.mesh_line, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(SplitTargetsUI)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.target_line = QtWidgets.QLineEdit(SplitTargetsUI)
        self.target_line.setObjectName("target_line")
        self.gridLayout.addWidget(self.target_line, 1, 1, 1, 1)
        self.target_btn = QtWidgets.QPushButton(SplitTargetsUI)
        self.target_btn.setObjectName("target_btn")
        self.gridLayout.addWidget(self.target_btn, 1, 2, 1, 1)
        self.mesh_btn = QtWidgets.QPushButton(SplitTargetsUI)
        self.mesh_btn.setObjectName("mesh_btn")
        self.gridLayout.addWidget(self.mesh_btn, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.create_btn = QtWidgets.QPushButton(SplitTargetsUI)
        self.create_btn.setObjectName("create_btn")
        self.verticalLayout.addWidget(self.create_btn)
        self.update_btn = QtWidgets.QPushButton(SplitTargetsUI)
        self.update_btn.setObjectName("update_btn")
        self.verticalLayout.addWidget(self.update_btn)
        self.generate_btn = QtWidgets.QPushButton(SplitTargetsUI)
        self.generate_btn.setObjectName("generate_btn")
        self.verticalLayout.addWidget(self.generate_btn)
        self.load_btn = QtWidgets.QPushButton(SplitTargetsUI)
        self.load_btn.setObjectName("load_btn")
        self.verticalLayout.addWidget(self.load_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(SplitTargetsUI)
        QtCore.QMetaObject.connectSlotsByName(SplitTargetsUI)

    def retranslateUi(self, SplitTargetsUI):
        SplitTargetsUI.setWindowTitle(QtCompat.translate("SplitTargetsUI", "Split Blend Shape Targets UI", None, -1))
        self.assetLabel_2.setText(QtCompat.translate("SplitTargetsUI", "Split Blend Shape Targets UI", None, -1))
        self.label_3.setText(QtCompat.translate("SplitTargetsUI", "Number of splits", None, -1))
        self.label.setText(QtCompat.translate("SplitTargetsUI", "Base Mesh", None, -1))
        self.label_2.setText(QtCompat.translate("SplitTargetsUI", "Target Shape", None, -1))
        self.target_btn.setText(QtCompat.translate("SplitTargetsUI", "Get Selected", None, -1))
        self.mesh_btn.setText(QtCompat.translate("SplitTargetsUI", "Get Selected", None, -1))
        self.create_btn.setText(QtCompat.translate("SplitTargetsUI", "Create Split Setup", None, -1))
        self.update_btn.setText(QtCompat.translate("SplitTargetsUI", "Update Split Weights", None, -1))
        self.generate_btn.setText(QtCompat.translate("SplitTargetsUI", "Generate Split Targets", None, -1))
        self.load_btn.setText(QtCompat.translate("SplitTargetsUI", "Load Split Setup", None, -1))

