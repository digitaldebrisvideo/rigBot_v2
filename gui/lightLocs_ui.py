# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/job/comms/pipeline/dev/bhamilton/git/ rigBot/rigBot/gui/lightLocs.ui'
#
# Created: Tue Aug 13 10:48:33 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtGui, QtCore, QtGui, QtWidgets

class Ui_lightLocsUI(object):
    def setupUi(self, lightLocsUI):
        lightLocsUI.setObjectName("lightLocsUI")
        lightLocsUI.resize(320, 186)
        self.verticalLayout = QtWidgets.QVBoxLayout(lightLocsUI)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(lightLocsUI)
        self.label.setMinimumSize(QtCore.QSize(40, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(40, 40,40);")
        self.label.setIndent(10)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(lightLocsUI)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(lightLocsUI)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.create_btn = QtWidgets.QPushButton(lightLocsUI)
        self.create_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.create_btn.setObjectName("create_btn")
        self.verticalLayout.addWidget(self.create_btn)
        self.update_btn = QtWidgets.QPushButton(lightLocsUI)
        self.update_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.update_btn.setObjectName("update_btn")
        self.verticalLayout.addWidget(self.update_btn)
        self.save_btn = QtWidgets.QPushButton(lightLocsUI)
        self.save_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(lightLocsUI)
        QtCore.QMetaObject.connectSlotsByName(lightLocsUI)

    def retranslateUi(self, lightLocsUI):
        lightLocsUI.setWindowTitle(QtCompat.translate("lightLocsUI", "Lighting Locators Util", None, -1))
        self.label.setText(QtCompat.translate("lightLocsUI", "Create Lighting Locators", None, -1))
        self.label_2.setText(QtCompat.translate("lightLocsUI", "Custom Name", None, -1))
        self.create_btn.setText(QtCompat.translate("lightLocsUI", "Create Using Selection", None, -1))
        self.update_btn.setText(QtCompat.translate("lightLocsUI", "Update Constraints On Selected", None, -1))
        self.save_btn.setText(QtCompat.translate("lightLocsUI", "Save Locators To Json", None, -1))

