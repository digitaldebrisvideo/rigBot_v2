# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nicob\Documents\maya\2020\scripts\rigBot\gui\newPart.ui',
# licensing of 'C:\Users\Nicob\Documents\maya\2020\scripts\rigBot\gui\newPart.ui' applies.
#
# Created: Fri Feb 26 15:49:27 2021
#      by: pyside2-uic  running on PySide2 5.12.5
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtGui, QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_1.setIndent(0)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.cat_label_2 = QtWidgets.QLabel(Form)
        self.cat_label_2.setObjectName("cat_label_2")
        self.verticalLayout.addWidget(self.cat_label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.cat_label = QtWidgets.QLabel(Form)
        self.cat_label.setObjectName("cat_label")
        self.verticalLayout.addWidget(self.cat_label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.d_label = QtWidgets.QLabel(Form)
        self.d_label.setObjectName("d_label")
        self.verticalLayout.addWidget(self.d_label)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_btn = QtWidgets.QPushButton(Form)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout.addWidget(self.create_btn)
        self.cance_btn = QtWidgets.QPushButton(Form)
        self.cance_btn.setObjectName("cance_btn")
        self.horizontalLayout.addWidget(self.cance_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCompat.translate("Form", "Create New Part", None, -1))
        self.label_1.setText(QtCompat.translate("Form", "Create New Part", None, -1))
        self.label_2.setText(QtCompat.translate("Form", "This will create an empty part module file in the specified location.\n"
"All you need to do is code your build. ", None, -1))
        self.cat_label_2.setText(QtCompat.translate("Form", "Part Name:", None, -1))
        self.cat_label.setText(QtCompat.translate("Form", "Part Category:", None, -1))
        self.d_label.setText(QtCompat.translate("Form", "Location On Disk:", None, -1))
        self.create_btn.setText(QtCompat.translate("Form", "Create", None, -1))
        self.cance_btn.setText(QtCompat.translate("Form", "Cancel", None, -1))

