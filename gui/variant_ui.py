# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/job/comms/google_ar_stickers_marine_4300074/sandbox/bhamilton/common/maya/2017.p5/python/rigBot/gui/variant.ui'
#
# Created: Thu Aug 30 11:27:07 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtGui, QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(326, 186)
        Form.setMinimumSize(QtCore.QSize(326, 186))
        Form.setMaximumSize(QtCore.QSize(326, 186))
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
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 2)
        self.cancel_btn = QtWidgets.QPushButton(Form)
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout.addWidget(self.cancel_btn, 6, 0, 1, 1)
        self.set_btn = QtWidgets.QPushButton(Form)
        self.set_btn.setObjectName("set_btn")
        self.gridLayout.addWidget(self.set_btn, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCompat.translate("Form", "New Variant", None, -1))
        self.label_2.setText(QtCompat.translate("Form", "Create a new rig variant.", None, -1))
        self.label.setText(QtCompat.translate("Form", "New Variant:", None, -1))
        self.comboBox.setItemText(0, QtCompat.translate("Form", "default", None, -1))
        self.comboBox.setItemText(1, QtCompat.translate("Form", "anim", None, -1))
        self.comboBox.setItemText(2, QtCompat.translate("Form", "mocap", None, -1))
        self.comboBox.setItemText(3, QtCompat.translate("Form", "export", None, -1))
        self.comboBox.setItemText(4, QtCompat.translate("Form", "other ...", None, -1))
        self.checkBox.setText(QtCompat.translate("Form", "Set as primary (Swap to this rig at publish time.)", None, -1))
        self.cancel_btn.setText(QtCompat.translate("Form", "Cancel", None, -1))
        self.set_btn.setText(QtCompat.translate("Form", "Add Variant", None, -1))

