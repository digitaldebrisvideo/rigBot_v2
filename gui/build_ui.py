# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nicob\Documents\maya\2020\scripts\rigBot\gui\build.ui',
# licensing of 'C:\Users\Nicob\Documents\maya\2020\scripts\rigBot\gui\build.ui' applies.
#
# Created: Mon Mar  1 07:46:22 2021
#      by: pyside2-uic  running on PySide2 5.12.5
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtGui, QtCore, QtGui, QtWidgets

class Ui_guides_form(object):
    def setupUi(self, guides_form):
        guides_form.setObjectName("guides_form")
        guides_form.resize(691, 990)
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
        self.label_6 = QtWidgets.QLabel(guides_form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setIndent(0)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_12.addWidget(self.label_6)
        self.variant_cmb = QtWidgets.QComboBox(guides_form)
        self.variant_cmb.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.variant_cmb.setFont(font)
        self.variant_cmb.setObjectName("variant_cmb")
        self.variant_cmb.addItem("")
        self.verticalLayout_12.addWidget(self.variant_cmb)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(guides_form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.build_tree = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.build_tree.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.build_tree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.build_tree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.build_tree.setUniformRowHeights(True)
        self.build_tree.setAllColumnsShowFocus(True)
        self.build_tree.setColumnCount(2)
        self.build_tree.setObjectName("build_tree")
        self.build_tree.headerItem().setText(0, "1")
        self.build_tree.headerItem().setText(1, "2")
        self.build_tree.header().setVisible(False)
        self.build_tree.header().setDefaultSectionSize(100)
        self.build_tree.header().setMinimumSectionSize(10)
        self.build_tree.header().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.build_tree)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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
        self.module_label = QtWidgets.QLabel(self.none_frame)
        self.module_label.setMinimumSize(QtCore.QSize(20, 25))
        self.module_label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.module_label.setFont(font)
        self.module_label.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.module_label.setLineWidth(0)
        self.module_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.module_label.setIndent(9)
        self.module_label.setObjectName("module_label")
        self.verticalLayout_7.addWidget(self.module_label)
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
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.doc_browser = QtWidgets.QTextBrowser(self.options_grp_2)
        self.doc_browser.setStyleSheet("QTextBrowser{\n"
"color: rgb(140,140, 140);\n"
" background-color: rgb(58, 58, 58); }")
        self.doc_browser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.doc_browser.setObjectName("doc_browser")
        self.verticalLayout_8.addWidget(self.doc_browser)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_btn = QtWidgets.QPushButton(self.options_grp_2)
        self.open_btn.setMaximumSize(QtCore.QSize(16777215, 18))
        self.open_btn.setObjectName("open_btn")
        self.verticalLayout.addWidget(self.open_btn)
        self.open_btn_2 = QtWidgets.QPushButton(self.options_grp_2)
        self.open_btn_2.setMaximumSize(QtCore.QSize(16777215, 18))
        self.open_btn_2.setObjectName("open_btn_2")
        self.verticalLayout.addWidget(self.open_btn_2)
        self.migrate_btn = QtWidgets.QPushButton(self.options_grp_2)
        self.migrate_btn.setMaximumSize(QtCore.QSize(16777215, 18))
        self.migrate_btn.setObjectName("migrate_btn")
        self.verticalLayout.addWidget(self.migrate_btn)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_7.addWidget(self.options_grp_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_3.addWidget(self.none_frame)
        self.none_frame_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.none_frame_2.setMinimumSize(QtCore.QSize(245, 0))
        self.none_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.none_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.none_frame_2.setObjectName("none_frame_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.none_frame_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.part_label_3 = QtWidgets.QLabel(self.none_frame_2)
        self.part_label_3.setMinimumSize(QtCore.QSize(20, 25))
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
        self.verticalLayout_10.addWidget(self.part_label_3)
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
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.options_grp_3)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setContentsMargins(9, 9, 4, 9)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.cache_chx = QtWidgets.QCheckBox(self.options_grp_3)
        self.cache_chx.setObjectName("cache_chx")
        self.verticalLayout_11.addWidget(self.cache_chx)
        self.verticalLayout_10.addWidget(self.options_grp_3)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.verticalLayout_3.addWidget(self.none_frame_2)
        self.none_frame_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.none_frame_3.setMinimumSize(QtCore.QSize(245, 0))
        self.none_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.none_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.none_frame_3.setObjectName("none_frame_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.none_frame_3)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.part_label_4 = QtWidgets.QLabel(self.none_frame_3)
        self.part_label_4.setMinimumSize(QtCore.QSize(20, 25))
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
        self.verticalLayout_14.addWidget(self.part_label_4)
        self.options_grp_4 = QtWidgets.QGroupBox(self.none_frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.options_grp_4.setFont(font)
        self.options_grp_4.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.options_grp_4.setTitle("")
        self.options_grp_4.setFlat(True)
        self.options_grp_4.setObjectName("options_grp_4")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.options_grp_4)
        self.verticalLayout_15.setSpacing(4)
        self.verticalLayout_15.setContentsMargins(9, 9, 4, 9)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.hand_util_btn = QtWidgets.QPushButton(self.options_grp_4)
        self.hand_util_btn.setMaximumSize(QtCore.QSize(16777215, 18))
        self.hand_util_btn.setObjectName("hand_util_btn")
        self.verticalLayout_15.addWidget(self.hand_util_btn)
        self.data_util_btn = QtWidgets.QPushButton(self.options_grp_4)
        self.data_util_btn.setMaximumSize(QtCore.QSize(16777215, 18))
        self.data_util_btn.setObjectName("data_util_btn")
        self.verticalLayout_15.addWidget(self.data_util_btn)
        self.data_util_btn_2 = QtWidgets.QPushButton(self.options_grp_4)
        self.data_util_btn_2.setMaximumSize(QtCore.QSize(16777215, 18))
        self.data_util_btn_2.setObjectName("data_util_btn_2")
        self.verticalLayout_15.addWidget(self.data_util_btn_2)
        self.verticalLayout_14.addWidget(self.options_grp_4)
        self.verticalLayout_13.addLayout(self.verticalLayout_14)
        self.verticalLayout_3.addWidget(self.none_frame_3)
        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.load_cache_build_btn = QtWidgets.QPushButton(guides_form)
        self.load_cache_build_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.load_cache_build_btn.setObjectName("load_cache_build_btn")
        self.gridLayout_2.addWidget(self.load_cache_build_btn, 3, 0, 1, 1)
        self.build_next_btn = QtWidgets.QPushButton(guides_form)
        self.build_next_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.build_next_btn.setObjectName("build_next_btn")
        self.gridLayout_2.addWidget(self.build_next_btn, 0, 0, 1, 1)
        self.build_selected_btn = QtWidgets.QPushButton(guides_form)
        self.build_selected_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.build_selected_btn.setObjectName("build_selected_btn")
        self.gridLayout_2.addWidget(self.build_selected_btn, 1, 0, 1, 1)
        self.build_all_btn = QtWidgets.QPushButton(guides_form)
        self.build_all_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.build_all_btn.setFont(font)
        self.build_all_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.build_all_btn.setObjectName("build_all_btn")
        self.gridLayout_2.addWidget(self.build_all_btn, 4, 0, 1, 1)
        self.build_to_selected_btn = QtWidgets.QPushButton(guides_form)
        self.build_to_selected_btn.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.build_to_selected_btn.setObjectName("build_to_selected_btn")
        self.gridLayout_2.addWidget(self.build_to_selected_btn, 2, 0, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout_2)
        self.verticalLayout_12.setStretch(3, 1)

        self.retranslateUi(guides_form)
        QtCore.QMetaObject.connectSlotsByName(guides_form)
        guides_form.setTabOrder(self.help_btn, self.variant_cmb)
        guides_form.setTabOrder(self.variant_cmb, self.build_tree)
        guides_form.setTabOrder(self.build_tree, self.doc_browser)
        guides_form.setTabOrder(self.doc_browser, self.open_btn)
        guides_form.setTabOrder(self.open_btn, self.open_btn_2)
        guides_form.setTabOrder(self.open_btn_2, self.migrate_btn)
        guides_form.setTabOrder(self.migrate_btn, self.cache_chx)
        guides_form.setTabOrder(self.cache_chx, self.build_next_btn)
        guides_form.setTabOrder(self.build_next_btn, self.build_selected_btn)
        guides_form.setTabOrder(self.build_selected_btn, self.build_to_selected_btn)
        guides_form.setTabOrder(self.build_to_selected_btn, self.load_cache_build_btn)
        guides_form.setTabOrder(self.load_cache_build_btn, self.build_all_btn)

    def retranslateUi(self, guides_form):
        guides_form.setWindowTitle(QtCompat.translate("guides_form", "Build Guides", None, -1))
        self.label_19.setText(QtCompat.translate("guides_form", "Build Rig", None, -1))
        self.asset_label.setText(QtCompat.translate("guides_form", "Project: Job_name", None, -1))
        self.help_btn.setToolTip(QtCompat.translate("guides_form", "Go to documentation.", None, -1))
        self.label_6.setText(QtCompat.translate("guides_form", "Rig Variant:", None, -1))
        self.variant_cmb.setToolTip(QtCompat.translate("guides_form", "Current rig variant. Set it here to build a different vairant.", None, -1))
        self.variant_cmb.setItemText(0, QtCompat.translate("guides_form", " Default", None, -1))
        self.label_4.setText(QtCompat.translate("guides_form", "Build List:", None, -1))
        self.label_5.setText(QtCompat.translate("guides_form", "Module Info:", None, -1))
        self.module_label.setText(QtCompat.translate("guides_form", "Module Documentation", None, -1))
        self.open_btn.setToolTip(QtCompat.translate("guides_form", "Open the specified python module in a text editor", None, -1))
        self.open_btn.setText(QtCompat.translate("guides_form", "Open Python Module File", None, -1))
        self.open_btn_2.setToolTip(QtCompat.translate("guides_form", "Open the specified python module in a text editor", None, -1))
        self.open_btn_2.setText(QtCompat.translate("guides_form", "Open asset_buildList File", None, -1))
        self.migrate_btn.setToolTip(QtCompat.translate("guides_form", "Migrate the selected module from the live tools area to the asset folder", None, -1))
        self.migrate_btn.setText(QtCompat.translate("guides_form", "Migrate Module to Asset", None, -1))
        self.part_label_3.setText(QtCompat.translate("guides_form", "Build Options", None, -1))
        self.cache_chx.setToolTip(QtCompat.translate("guides_form", "Saves each built step as a Maya file to the usr/tmp for quick building", None, -1))
        self.cache_chx.setText(QtCompat.translate("guides_form", "Cache Build Steps", None, -1))
        self.part_label_4.setText(QtCompat.translate("guides_form", "Build Utilities", None, -1))
        self.hand_util_btn.setToolTip(QtCompat.translate("guides_form", "Utility for setting hand and finger poses.", None, -1))
        self.hand_util_btn.setText(QtCompat.translate("guides_form", "Hand Pose Util", None, -1))
        self.data_util_btn.setToolTip(QtCompat.translate("guides_form", "Utility for loading specific rig data with customized options.", None, -1))
        self.data_util_btn.setText(QtCompat.translate("guides_form", "Load Data Util", None, -1))
        self.data_util_btn_2.setToolTip(QtCompat.translate("guides_form", "Utility for loading specific rig data with customized options.", None, -1))
        self.data_util_btn_2.setText(QtCompat.translate("guides_form", "Unfinalize Rig", None, -1))
        self.load_cache_build_btn.setToolTip(QtCompat.translate("guides_form", "Load the cache file for the previous step and run the currently selected step.\n"
"Right click for more options", None, -1))
        self.load_cache_build_btn.setText(QtCompat.translate("guides_form", "Load Previous Cache and Run This Step", None, -1))
        self.build_next_btn.setToolTip(QtCompat.translate("guides_form", "Build the next step in the list", None, -1))
        self.build_next_btn.setText(QtCompat.translate("guides_form", "Build Next Step", None, -1))
        self.build_selected_btn.setToolTip(QtCompat.translate("guides_form", "Build only selected steps in the list", None, -1))
        self.build_selected_btn.setText(QtCompat.translate("guides_form", "Build Selected Steps", None, -1))
        self.build_all_btn.setToolTip(QtCompat.translate("guides_form", "Build all remaining steps in the list.\n"
"Right click for more options", None, -1))
        self.build_all_btn.setText(QtCompat.translate("guides_form", "Build All Remaining Steps", None, -1))
        self.build_to_selected_btn.setToolTip(QtCompat.translate("guides_form", "Build only selected steps in the list", None, -1))
        self.build_to_selected_btn.setText(QtCompat.translate("guides_form", "Build Up To Selected Step", None, -1))

