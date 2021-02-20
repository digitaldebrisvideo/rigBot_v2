# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/job/commsdev/staff_dev_la_2017/sandbox/bhamilton/common/maya/2017.p5/python/rigBot/gui/setInheritance.ui'
#
# Created: Thu Aug  9 11:38:35 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtGui, QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 200)
        Form.setMinimumSize(QtCore.QSize(320, 200))
        Form.setMaximumSize(QtCore.QSize(320, 200))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)
        self.cancel_btn = QtWidgets.QPushButton(Form)
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout.addWidget(self.cancel_btn, 4, 0, 1, 1)
        self.set_btn = QtWidgets.QPushButton(Form)
        self.set_btn.setObjectName("set_btn")
        self.gridLayout.addWidget(self.set_btn, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCompat.translate("Form", "Set Asset Inheritance", None, -1))
        self.label_2.setText(QtCompat.translate("Form", "Choose an asset rigbuild path to include in the sys.path for this current asset.\n"
"\n"
"Optionally choose to inherit the guide file as well.", None, -1))
        self.label.setText(QtCompat.translate("Form", "Asset To Inherit:", None, -1))
        self.checkBox.setText(QtCompat.translate("Form", "Inherit Guides File", None, -1))
        self.cancel_btn.setText(QtCompat.translate("Form", "Cancel", None, -1))
        self.set_btn.setText(QtCompat.translate("Form", "Set Inheritance", None, -1))

