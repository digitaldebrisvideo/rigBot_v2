# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/job/comms/google_ar_stickers_marine_4300074/sandbox/bhamilton/common/maya/2017.p5/python/rigBot/gui/spaces.ui'
#
# Created: Mon Dec  3 19:34:59 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtGui, QtCore, QtGui, QtWidgets

class Ui_export_form(object):
    def setupUi(self, export_form):
        export_form.setObjectName("export_form")
        export_form.resize(473, 700)
        export_form.setStatusTip("")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(export_form)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.banner_frame = QtWidgets.QFrame(export_form)
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
        self.asset_label = QtWidgets.QLabel(self.banner_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.asset_label.setFont(font)
        self.asset_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.asset_label.setObjectName("asset_label")
        self.horizontalLayout.addWidget(self.asset_label)
        self.help_btn = QtWidgets.QPushButton(self.banner_frame)
        self.help_btn.setMinimumSize(QtCore.QSize(24, 24))
        self.help_btn.setMaximumSize(QtCore.QSize(24, 24))
        self.help_btn.setStyleSheet("border-color: rgb(190, 190, 190);")
        self.help_btn.setText("")
        self.help_btn.setFlat(True)
        self.help_btn.setObjectName("help_btn")
        self.horizontalLayout.addWidget(self.help_btn)
        self.verticalLayout_12.addWidget(self.banner_frame)
        self.label_6 = QtWidgets.QLabel(export_form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setIndent(0)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_12.addWidget(self.label_6)
        self.variant_cmb = QtWidgets.QComboBox(export_form)
        self.variant_cmb.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.variant_cmb.setFont(font)
        self.variant_cmb.setObjectName("variant_cmb")
        self.variant_cmb.addItem("")
        self.verticalLayout_12.addWidget(self.variant_cmb)
        self.splitter = QtWidgets.QSplitter(export_form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(4)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.node_list = QtWidgets.QListWidget(self.layoutWidget)
        self.node_list.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.node_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.node_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.node_list.setObjectName("node_list")
        self.verticalLayout_2.addWidget(self.node_list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.list_btn.setMaximumSize(QtCore.QSize(16777215, 18))
        self.list_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.list_btn.setObjectName("list_btn")
        self.verticalLayout.addWidget(self.list_btn)
        self.list_model_btn_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.list_model_btn_2.setMaximumSize(QtCore.QSize(16777215, 18))
        self.list_model_btn_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.list_model_btn_2.setObjectName("list_model_btn_2")
        self.verticalLayout.addWidget(self.list_model_btn_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.none_frame_2 = QtWidgets.QFrame(self.layoutWidget_2)
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
        self.groupBox = QtWidgets.QGroupBox(self.none_frame_2)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.default_cmb = QtWidgets.QComboBox(self.groupBox)
        self.default_cmb.setMinimumSize(QtCore.QSize(0, 20))
        self.default_cmb.setMaximumSize(QtCore.QSize(16777215, 20))
        self.default_cmb.setObjectName("default_cmb")
        self.gridLayout_3.addWidget(self.default_cmb, 1, 1, 1, 1)
        self.const_line = QtWidgets.QLineEdit(self.groupBox)
        self.const_line.setMaximumSize(QtCore.QSize(16777215, 20))
        self.const_line.setObjectName("const_line")
        self.gridLayout_3.addWidget(self.const_line, 0, 1, 1, 1)
        self.const_btn = QtWidgets.QPushButton(self.groupBox)
        self.const_btn.setMaximumSize(QtCore.QSize(100, 20))
        self.const_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.const_btn.setObjectName("const_btn")
        self.gridLayout_3.addWidget(self.const_btn, 0, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.split_chx = QtWidgets.QCheckBox(self.groupBox)
        self.split_chx.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.split_chx.setStyleSheet("")
        self.split_chx.setText("")
        self.split_chx.setChecked(False)
        self.split_chx.setTristate(False)
        self.split_chx.setObjectName("split_chx")
        self.horizontalLayout_4.addWidget(self.split_chx)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 3)
        self.verticalLayout_13.addWidget(self.groupBox)
        self.verticalLayout_11.addLayout(self.verticalLayout_13)
        self.verticalLayout_3.addWidget(self.none_frame_2)
        self.part_label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.part_label_4.setMinimumSize(QtCore.QSize(0, 25))
        self.part_label_4.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.part_label_4.setFont(font)
        self.part_label_4.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.part_label_4.setLineWidth(0)
        self.part_label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.part_label_4.setIndent(9)
        self.part_label_4.setObjectName("part_label_4")
        self.verticalLayout_3.addWidget(self.part_label_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_12.addWidget(self.splitter)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.export_btn = QtWidgets.QPushButton(export_form)
        self.export_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.export_btn.setFont(font)
        self.export_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.export_btn.setObjectName("export_btn")
        self.gridLayout_2.addWidget(self.export_btn, 0, 0, 1, 2)
        self.verticalLayout_12.addLayout(self.gridLayout_2)
        self.verticalLayout_12.setStretch(3, 1)

        self.retranslateUi(export_form)
        QtCore.QMetaObject.connectSlotsByName(export_form)
        export_form.setTabOrder(self.help_btn, self.variant_cmb)
        export_form.setTabOrder(self.variant_cmb, self.list_btn)

    def retranslateUi(self, export_form):
        export_form.setWindowTitle(QtCompat.translate("export_form", "Spaces", None, -1))
        self.label_19.setText(QtCompat.translate("export_form", "Spaces", None, -1))
        self.asset_label.setText(QtCompat.translate("export_form", "Project: Job_name", None, -1))
        self.help_btn.setToolTip(QtCompat.translate("export_form", "Go to documentation.", None, -1))
        self.label_6.setText(QtCompat.translate("export_form", "Rig Variant:", None, -1))
        self.variant_cmb.setToolTip(QtCompat.translate("export_form", "Current rig variant. Set it here to save data for a different vairant.", None, -1))
        self.variant_cmb.setItemText(0, QtCompat.translate("export_form", " Default", None, -1))
        self.label_4.setText(QtCompat.translate("export_form", "Nodes:", None, -1))
        self.node_list.setToolTip(QtCompat.translate("export_form", "Nodes with space tags", None, -1))
        self.list_btn.setToolTip(QtCompat.translate("export_form", "Add selected nodes to list.", None, -1))
        self.list_btn.setText(QtCompat.translate("export_form", "Add Selected Nodes", None, -1))
        self.list_model_btn_2.setToolTip(QtCompat.translate("export_form", "Remove space tag from selected nodes. ", None, -1))
        self.list_model_btn_2.setText(QtCompat.translate("export_form", "Remove Space Tag From Nodes", None, -1))
        self.part_label_3.setText(QtCompat.translate("export_form", "Options", None, -1))
        self.label_7.setToolTip(QtCompat.translate("export_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Const Node: The node to add constraints to.</span></p></body></html>", None, -1))
        self.label_7.setText(QtCompat.translate("export_form", "Const Node  ", None, -1))
        self.label_8.setToolTip(QtCompat.translate("export_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Default space value.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"></p></body></html>", None, -1))
        self.label_8.setText(QtCompat.translate("export_form", "Default Space  ", None, -1))
        self.default_cmb.setToolTip(QtCompat.translate("export_form", "Default space value.", None, -1))
        self.const_line.setToolTip(QtCompat.translate("export_form", "Const Node: The node to add constraints to.", None, -1))
        self.const_btn.setToolTip(QtCompat.translate("export_form", "Const Node: Set the node to add constraints to. (Right-click for more options.)", None, -1))
        self.const_btn.setText(QtCompat.translate("export_form", "  <<  ", None, -1))
        self.label_9.setToolTip(QtCompat.translate("export_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Split Spaces into translate and rotate channels.</p></body></html>", None, -1))
        self.label_9.setText(QtCompat.translate("export_form", "Split Translate & Rotate ", None, -1))
        self.split_chx.setToolTip(QtCompat.translate("export_form", "Split Spaces into translate and rotate channels.", None, -1))
        self.part_label_4.setText(QtCompat.translate("export_form", "Spaces", None, -1))
        self.export_btn.setToolTip(QtCompat.translate("export_form", "Export spaces data to asset / data / variant folder.", None, -1))
        self.export_btn.setText(QtCompat.translate("export_form", "Export Spaces Data", None, -1))
