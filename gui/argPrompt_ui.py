# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bhamilton/Documents/maya/scripts\rigBot\gui\argPrompt.ui'
#
# Created: Sat Sep 08 22:17:33 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

try:
    from Qt import QtCompat, QtGui, QtCore, QtWidgets

except:
    from PySide2 import QtCompat, QtGui, QtCore, QtWidgets
    
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(294, 230)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelBtn = QtWidgets.QPushButton(Form)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.continueBtn = QtWidgets.QPushButton(Form)
        self.continueBtn.setDefault(True)
        self.continueBtn.setObjectName("continueBtn")
        self.horizontalLayout.addWidget(self.continueBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        self.icon = QtWidgets.QLabel(Form)
        self.icon.setMinimumSize(QtCore.QSize(36, 36))
        self.icon.setMaximumSize(QtCore.QSize(36, 36))
        self.icon.setText("")
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        self.sideCmb = QtWidgets.QComboBox(Form)
        self.sideCmb.setObjectName("sideCmb")
        self.gridLayout.addWidget(self.sideCmb, 2, 1, 1, 1)
        self.nameLine = QtWidgets.QLineEdit(Form)
        self.nameLine.setObjectName("nameLine")
        self.gridLayout.addWidget(self.nameLine, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.part_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.part_label.setFont(font)
        self.part_label.setIndent(-1)
        self.part_label.setObjectName("part_label")
        self.gridLayout.addWidget(self.part_label, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCompat.translate("Form", "Change Build Arguments", None, -1))
        self.cancelBtn.setText(QtCompat.translate("Form", "Cancel", None, -1))
        self.continueBtn.setText(QtCompat.translate("Form", "Continue", None, -1))
        self.label.setText(QtCompat.translate("Form", "New Side", None, -1))
        self.label_2.setText(QtCompat.translate("Form", "New Name", None, -1))
        self.label_3.setText(QtCompat.translate("Form", "The current side and or name arguments will result in a\n"
"node name clash in the rig.\n"
"\n"
"Update your aguments or cancel this part build.\n"
"", None, -1))
        self.part_label.setText(QtCompat.translate("Form", "Part name", None, -1))

