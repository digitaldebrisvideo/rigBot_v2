# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/job/commsdev/staff_dev_la_2017/sandbox/bhamilton/common/maya/2017.p5/python/rigBot/gui/handPose.ui'
#
# Created: Mon Jul  9 11:16:02 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtGui, QtCore, QtGui, QtWidgets

class Ui_handPoseUI(object):
    def setupUi(self, handPoseUI):
        handPoseUI.setObjectName("handPoseUI")
        handPoseUI.resize(220, 186)
        self.verticalLayout = QtWidgets.QVBoxLayout(handPoseUI)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(handPoseUI)
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
        self.stamp_btn = QtWidgets.QPushButton(handPoseUI)
        self.stamp_btn.setObjectName("stamp_btn")
        self.verticalLayout.addWidget(self.stamp_btn)
        self.unstamp_btn = QtWidgets.QPushButton(handPoseUI)
        self.unstamp_btn.setObjectName("unstamp_btn")
        self.verticalLayout.addWidget(self.unstamp_btn)
        self.mirror_btn = QtWidgets.QPushButton(handPoseUI)
        self.mirror_btn.setObjectName("mirror_btn")
        self.verticalLayout.addWidget(self.mirror_btn)
        self.save_btn = QtWidgets.QPushButton(handPoseUI)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(handPoseUI)
        QtCore.QMetaObject.connectSlotsByName(handPoseUI)

    def retranslateUi(self, handPoseUI):
        handPoseUI.setWindowTitle(QtCompat.translate("handPoseUI", "Hand Pose Util", None, -1))
        self.label.setText(QtCompat.translate("handPoseUI", "Set Hand Poses", None, -1))
        self.stamp_btn.setText(QtCompat.translate("handPoseUI", "Stamp Pose", None, -1))
        self.unstamp_btn.setText(QtCompat.translate("handPoseUI", "Unstamp Pose", None, -1))
        self.mirror_btn.setText(QtCompat.translate("handPoseUI", "Mirror / Copy Poses", None, -1))
        self.save_btn.setText(QtCompat.translate("handPoseUI", "Save Poses", None, -1))

