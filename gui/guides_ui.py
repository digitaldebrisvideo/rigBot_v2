# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/job/commsdev/staff_dev_la_2017/sandbox/bhamilton/common/maya/2017.p5/python/rigBot/gui/guides.ui'
#
# Created: Tue Apr  9 17:15:42 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtGui, QtCore, QtGui, QtWidgets

class Ui_guides_form(object):
    def setupUi(self, guides_form):
        guides_form.setObjectName("guides_form")
        guides_form.resize(505, 767)
        guides_form.setStatusTip("")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(guides_form)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.banner_frame = QtWidgets.QFrame(guides_form)
        self.banner_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.banner_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.banner_frame.setStyleSheet("QFrame{background-color: rgb(45, 45, 45);\n"
"color: rgb(230, 230, 230);}")
        self.banner_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.banner_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.banner_frame.setObjectName("banner_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.banner_frame)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setContentsMargins(4, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon_label = QtWidgets.QLabel(self.banner_frame)
        self.icon_label.setMinimumSize(QtCore.QSize(40, 40))
        self.icon_label.setMaximumSize(QtCore.QSize(40, 40))
        self.icon_label.setText("")
        self.icon_label.setObjectName("icon_label")
        self.horizontalLayout.addWidget(self.icon_label)
        self.label_19 = QtWidgets.QLabel(self.banner_frame)
        self.label_19.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setIndent(0)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout.addWidget(self.label_19)
        self.job_label = QtWidgets.QLabel(self.banner_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.job_label.setFont(font)
        self.job_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.job_label.setObjectName("job_label")
        self.horizontalLayout.addWidget(self.job_label)
        self.help_btn = QtWidgets.QPushButton(self.banner_frame)
        self.help_btn.setMinimumSize(QtCore.QSize(24, 24))
        self.help_btn.setMaximumSize(QtCore.QSize(24, 24))
        self.help_btn.setStyleSheet("border-color: rgb(190, 190, 190);")
        self.help_btn.setText("")
        self.help_btn.setFlat(True)
        self.help_btn.setObjectName("help_btn")
        self.horizontalLayout.addWidget(self.help_btn)
        self.verticalLayout_12.addWidget(self.banner_frame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(guides_form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_btn.setMinimumSize(QtCore.QSize(0, 27))
        self.add_btn.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.verticalLayout_2.addWidget(self.add_btn)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setStyleSheet("QFrame{background-color: rgb(55, 55, 55);}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_3.addWidget(self.radioButton_3, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.alpha_btn_2 = QtWidgets.QPushButton(self.frame)
        self.alpha_btn_2.setMaximumSize(QtCore.QSize(60, 20))
        self.alpha_btn_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.alpha_btn_2.setObjectName("alpha_btn_2")
        self.horizontalLayout_4.addWidget(self.alpha_btn_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 0, 1, 3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_3.addWidget(self.radioButton_4, 1, 2, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_3.addWidget(self.radioButton_5, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 3)
        self.verticalLayout_15.addWidget(self.frame)
        self.guide_list = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.guide_list.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.guide_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.guide_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.guide_list.setObjectName("guide_list")
        self.verticalLayout_15.addWidget(self.guide_list)
        self.verticalLayout_2.addLayout(self.verticalLayout_15)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.mirror_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mirror_btn.setMaximumSize(QtCore.QSize(16777215, 18))
        self.mirror_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mirror_btn.setObjectName("mirror_btn")
        self.verticalLayout_10.addWidget(self.mirror_btn)
        self.duplicate_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.duplicate_btn.setMaximumSize(QtCore.QSize(16777215, 18))
        self.duplicate_btn.setObjectName("duplicate_btn")
        self.verticalLayout_10.addWidget(self.duplicate_btn)
        self.delete_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_btn.setMaximumSize(QtCore.QSize(16777215, 18))
        self.delete_btn.setObjectName("delete_btn")
        self.verticalLayout_10.addWidget(self.delete_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setEnabled(False)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 27))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pushButton.setText("")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.none_frame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.none_frame.setMinimumSize(QtCore.QSize(245, 0))
        self.none_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.none_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.none_frame.setObjectName("none_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.none_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.part_label_2 = QtWidgets.QLabel(self.none_frame)
        self.part_label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.part_label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.part_label_2.setFont(font)
        self.part_label_2.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.part_label_2.setLineWidth(0)
        self.part_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.part_label_2.setIndent(9)
        self.part_label_2.setObjectName("part_label_2")
        self.verticalLayout_7.addWidget(self.part_label_2)
        self.options_grp_2 = QtWidgets.QGroupBox(self.none_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.options_grp_2.setFont(font)
        self.options_grp_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.options_grp_2.setTitle("")
        self.options_grp_2.setFlat(True)
        self.options_grp_2.setObjectName("options_grp_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.options_grp_2)
        self.verticalLayout_8.setContentsMargins(4, -1, 4, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_18 = QtWidgets.QLabel(self.options_grp_2)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_8.addWidget(self.label_18)
        self.verticalLayout_7.addWidget(self.options_grp_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_3.addWidget(self.none_frame)
        self.options_frame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.options_frame.setMinimumSize(QtCore.QSize(245, 0))
        self.options_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_frame.setObjectName("options_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.options_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.guide_name_label = QtWidgets.QLabel(self.options_frame)
        self.guide_name_label.setMinimumSize(QtCore.QSize(0, 25))
        self.guide_name_label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.guide_name_label.setFont(font)
        self.guide_name_label.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.guide_name_label.setLineWidth(0)
        self.guide_name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.guide_name_label.setIndent(9)
        self.guide_name_label.setObjectName("guide_name_label")
        self.verticalLayout_5.addWidget(self.guide_name_label)
        self.options_grp = QtWidgets.QGroupBox(self.options_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.options_grp.setFont(font)
        self.options_grp.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.options_grp.setTitle("")
        self.options_grp.setFlat(True)
        self.options_grp.setObjectName("options_grp")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.options_grp)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.options_grid_layout = QtWidgets.QGridLayout()
        self.options_grid_layout.setObjectName("options_grid_layout")
        self.verticalLayout_9.addLayout(self.options_grid_layout)
        self.build_btn = QtWidgets.QPushButton(self.options_grp)
        self.build_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.build_btn.setFont(font)
        self.build_btn.setStyleSheet("")
        self.build_btn.setObjectName("build_btn")
        self.verticalLayout_9.addWidget(self.build_btn)
        self.verticalLayout_5.addWidget(self.options_grp)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addWidget(self.options_frame)
        spacerItem = QtWidgets.QSpacerItem(20, 113, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.none_frame_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.none_frame_2.setMinimumSize(QtCore.QSize(245, 0))
        self.none_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.none_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.none_frame_2.setObjectName("none_frame_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.none_frame_2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.part_label_3 = QtWidgets.QLabel(self.none_frame_2)
        self.part_label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.part_label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.part_label_3.setFont(font)
        self.part_label_3.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.part_label_3.setLineWidth(0)
        self.part_label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.part_label_3.setIndent(9)
        self.part_label_3.setObjectName("part_label_3")
        self.verticalLayout_13.addWidget(self.part_label_3)
        self.options_grp_3 = QtWidgets.QGroupBox(self.none_frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.options_grp_3.setFont(font)
        self.options_grp_3.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.options_grp_3.setTitle("")
        self.options_grp_3.setFlat(True)
        self.options_grp_3.setObjectName("options_grp_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.options_grp_3)
        self.verticalLayout_14.setContentsMargins(9, -1, 9, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.model_btn = QtWidgets.QPushButton(self.options_grp_3)
        self.model_btn.setMaximumSize(QtCore.QSize(16777215, 18))
        self.model_btn.setObjectName("model_btn")
        self.verticalLayout_14.addWidget(self.model_btn)
        self.pin_guides_btn = QtWidgets.QPushButton(self.options_grp_3)
        self.pin_guides_btn.setMaximumSize(QtCore.QSize(16777215, 18))
        self.pin_guides_btn.setObjectName("pin_guides_btn")
        self.verticalLayout_14.addWidget(self.pin_guides_btn)
        self.verticalLayout_13.addWidget(self.options_grp_3)
        self.verticalLayout_11.addLayout(self.verticalLayout_13)
        self.verticalLayout_3.addWidget(self.none_frame_2)
        self.verticalLayout_3.setStretch(4, 1)
        self.verticalLayout.addWidget(self.splitter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.load_btn = QtWidgets.QPushButton(guides_form)
        self.load_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.load_btn.setObjectName("load_btn")
        self.horizontalLayout_2.addWidget(self.load_btn)
        self.save_btn = QtWidgets.QPushButton(guides_form)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout_12.addLayout(self.verticalLayout)

        self.retranslateUi(guides_form)
        QtCore.QMetaObject.connectSlotsByName(guides_form)

    def retranslateUi(self, guides_form):
        guides_form.setWindowTitle(QtCompat.translate("guides_form", "Build Guides", None, -1))
        self.label_19.setText(QtCompat.translate("guides_form", "Guides", None, -1))
        self.job_label.setText(QtCompat.translate("guides_form", "Project: Job_name", None, -1))
        self.help_btn.setToolTip(QtCompat.translate("guides_form", "Go to documentation.", None, -1))
        self.add_btn.setToolTip(QtCompat.translate("guides_form", "Add guide parts or assemblies to your scene.", None, -1))
        self.add_btn.setText(QtCompat.translate("guides_form", "Add Part / Assembly", None, -1))
        self.label_4.setText(QtCompat.translate("guides_form", "Guides In Scene:", None, -1))
        self.radioButton_3.setText(QtCompat.translate("guides_form", "Side", None, -1))
        self.label_2.setText(QtCompat.translate("guides_form", "Filter:", None, -1))
        self.alpha_btn_2.setToolTip(QtCompat.translate("guides_form", "Build only selected steps in the list", None, -1))
        self.alpha_btn_2.setText(QtCompat.translate("guides_form", "Clear", None, -1))
        self.radioButton_4.setText(QtCompat.translate("guides_form", "Name", None, -1))
        self.radioButton_5.setText(QtCompat.translate("guides_form", "Hierarchy", None, -1))
        self.label.setText(QtCompat.translate("guides_form", "Sort By:", None, -1))
        self.guide_list.setToolTip(QtCompat.translate("guides_form", "List of guides parts in scene. (Right-click for more options)", None, -1))
        self.mirror_btn.setToolTip(QtCompat.translate("guides_form", "Mirror Selected guide parts", None, -1))
        self.mirror_btn.setText(QtCompat.translate("guides_form", "Mirror Guide", None, -1))
        self.duplicate_btn.setToolTip(QtCompat.translate("guides_form", "Duplicate Selected guide parts", None, -1))
        self.duplicate_btn.setText(QtCompat.translate("guides_form", "Duplicate Guide", None, -1))
        self.delete_btn.setToolTip(QtCompat.translate("guides_form", "Delete Selected guide parts", None, -1))
        self.delete_btn.setText(QtCompat.translate("guides_form", "Delete Guide", None, -1))
        self.label_5.setText(QtCompat.translate("guides_form", "Options:", None, -1))
        self.part_label_2.setText(QtCompat.translate("guides_form", "No Guides In Scene", None, -1))
        self.label_18.setText(QtCompat.translate("guides_form", "No guides exist in scene.\n"
"Add some or build an assembly. ", None, -1))
        self.guide_name_label.setText(QtCompat.translate("guides_form", "BipedArm (New Guide)", None, -1))
        self.build_btn.setToolTip(QtCompat.translate("guides_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Build This Rig Part</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, -1))
        self.build_btn.setText(QtCompat.translate("guides_form", "Build Guide", None, -1))
        self.part_label_3.setText(QtCompat.translate("guides_form", "Guide Utilities", None, -1))
        self.model_btn.setToolTip(QtCompat.translate("guides_form", "Duplicate Selected guide parts", None, -1))
        self.model_btn.setText(QtCompat.translate("guides_form", "Load Model", None, -1))
        self.pin_guides_btn.setToolTip(QtCompat.translate("guides_form", "Duplicate Selected guide parts", None, -1))
        self.pin_guides_btn.setText(QtCompat.translate("guides_form", "Pin Guides", None, -1))
        self.load_btn.setToolTip(QtCompat.translate("guides_form", "Load lastest existing rig layout. (Right-click for more options)", None, -1))
        self.load_btn.setText(QtCompat.translate("guides_form", "Load Guides", None, -1))
        self.save_btn.setToolTip(QtCompat.translate("guides_form", "Save current rig layout.", None, -1))
        self.save_btn.setText(QtCompat.translate("guides_form", "Save Guides", None, -1))
