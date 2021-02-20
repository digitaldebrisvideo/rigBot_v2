import maya.cmds as mc
import maya.OpenMaya as om
import maya.OpenMayaAnim as oma

from functools import partial
import cPickle as pickle
import time
import os

from rigBot import utils
from rigBot import control
from rigBot.gui import mayaWidget
from rigBot.gui import control_ui

from Qt import QtGui
from Qt import QtCore
from Qt import QtWidgets

class ControlUI(mayaWidget.MayaWidget):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, parent=None):
        mayaWidget.MayaWidget.__init__(self, parent=parent)

        title = 'control_UI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = control_ui.Ui_ClusterUI()
        self.ui.setupUi(self)
        self.setObjectName(title)
        self.setWindowTitle('Control UI')

        self.setMinimumWidth(350)
        self.setMinimumHeight(800)
        self.setMaximumHeight(800)
        self.resize(350, 800)

        self.ui.create_btn.released.connect(self.create)
        self.ui.shape_mod_cmb.currentIndexChanged.connect(self.mod_shape)
        self.ui.color_mod_cmb.currentIndexChanged.connect(self.mod_color)
        self.ui.mirror_shape_btn.released.connect(self.mirror_shape)
        self.ui.copy_shape_btn.released.connect(self.copy_shape)
        self.ui.copy_color_btn.released.connect(self.copy_color)
        self.ui.pivot_btn.released.connect(self.create_movable_pivot)

        self.ui.save_shape_btn.released.connect(self.save_shape)
        self.ui.save_color_btn.released.connect(self.save_color)


        item = QtWidgets.QAction(self)
        item.setText('Copy Shape in World Space')
        item.triggered.connect(partial(self.copy_shape, world_space=True))
        self.ui.copy_shape_btn.addAction(item)

        self.load_control_data()

        self.center()

    def load_control_data(self):

        try:
            self.ui.shape_mod_cmb.currentIndexChanged.disconnect(self.mod_shape)
        except:
            pass

        control.reload_control_data()
        shapes = control.shapes
        colors = control.colors

        shapes.sort()
        colors.sort()

        self.ui.shape_cmb.clear()
        self.ui.shape_mod_cmb.clear()
        self.ui.shape_cmb.addItems(shapes)
        self.ui.shape_mod_cmb.addItems(['       ---'] + shapes)

        if 'none' in colors:
            colors.remove('none')
            colors.insert(0, '       ---')

        self.ui.color_cmb.clear()
        self.ui.color_mod_cmb.clear()
        self.ui.color_cmb.addItems(colors)
        self.ui.color_mod_cmb.addItems(colors)

        numitems = min(len(shapes) , 80)
        self.ui.shape_cmb.setMaxVisibleItems(numitems)
        self.ui.shape_mod_cmb.setMaxVisibleItems(numitems)

        numitems = min(len(colors) , 80)
        self.ui.color_cmb.setMaxVisibleItems(numitems)
        self.ui.color_mod_cmb.setMaxVisibleItems(numitems)

        # Set color icons
        color_values = [control.color_data.get(c) for c in colors]
        for i, value in enumerate(color_values):
            if type(value) == int:
                try:
                    value = mc.colorIndex(value, q=1)

                except:
                    value = [0.176]*3

            if value:

                value = [min(v, 1.0) for v in value]

                pixmap = QtGui.QPixmap(20,20)
                pixmap.fill(QtGui.QColor(value[0]*255, value[1]*255, value[2]*255))

                self.ui.color_cmb.setItemIcon(i, pixmap)
                self.ui.color_mod_cmb.setItemIcon(i, pixmap)

        self.ui.color_cmb.setCurrentIndex(19)
        self.ui.shape_cmb.setCurrentIndex(15)

        self.ui.shape_mod_cmb.currentIndexChanged.connect(self.mod_shape)

    def save_shape(self):
        control.save_shape()
        self.load_control_data()

    def save_color(self):
        control.save_color()
        self.load_control_data()

    @utils.undoable
    def mirror_shape(self):
        control.mirror_shape()

    @utils.undoable
    def copy_shape(self, world_space=False):
        sel = mc.ls(sl=1)
        for s in sel[1:]:
            mc.select(sel[0], s)
            control.copy_shape(world_space=world_space)

    @utils.undoable
    def copy_color(self):
        sel = mc.ls(sl=1)
        for s in sel[1:]:
            mc.select(sel[0], s)
            control.copy_color()

    @utils.undoable
    def create_movable_pivot(self):
        sel = mc.ls(sl=1)
        for s in sel:
            mc.select(s)
            control.create_movable_pivot()

    @utils.undoable
    def create(self):

        side_token = 'L'
        if self.ui.R_rdo.isChecked():
            side_token = 'R'

        if self.ui.C_rdo.isChecked():
            side_token = 'C'

        name_token = self.ui.name_line.text() or 'myControl'
        basename = utils.join_strings([side_token, name_token])

        shape = self.ui.shape_cmb.currentText()
        color = self.ui.color_cmb.currentText()

        node_type = 'transform'
        if self.ui.joint_rdo.isChecked():
            node_type = 'joint'

        axis = 'X'
        if self.ui.Y_rdo.isChecked():
            axis = 'Y'
        if self.ui.Z_rdo.isChecked():
            axis = 'Z'

        loc = None
        if self.ui.snap_chx.isChecked():
            sel = mc.ls(sl=1)
            if sel:
                loc = utils.snap_locator()
                if loc:
                    try:
                        mc.delete(mc.orientConstraint(sel, loc))
                    except:
                        pass

        result = control.create(name=basename, shape=shape, color=color, axis=axis, node_type=node_type, match_position=loc)

        if loc:
            mc.delete(loc)

        if self.ui.pivot_chx.isChecked():
            control.create_movable_pivot(result[-1])

        mc.select(result[0])

    @utils.undoable
    def mod_shape(self, *kwargs):

        shape = self.ui.shape_mod_cmb.currentText()
        sel = mc.ls(sl=1)

        if shape != '       ---':
            if sel:
                try:
                    control.create_shape(shape)
                    mc.select(sel)
                except:
                    pass
            else:
                mc.warning('Nothing selected!')

        self.ui.shape_mod_cmb.setCurrentIndex(0)

    @utils.undoable
    def mod_color(self, *kwargs):

        color = self.ui.color_mod_cmb.currentText()
        sel = mc.ls(sl=1)

        if color != '       ---':
            if sel:
                try:
                    control.set_color(color)
                    mc.select(sel)
                except:
                    pass
            else:
                mc.warning('Nothing selected!')

        self.ui.color_mod_cmb.setCurrentIndex(0)

qt_widget_object = None
def run(dockable=True, **kwargs):
    """
    This is boiler plate code for launching your dockable UI,
    Copy and paste this into your ui module. then change the className from MayaWidget
    to whatever your class name is.

    UIs using this run wrapper require your UI class to inherit the MayaWidget
    class that is defined above, in this module.

    USAGE:
        import myGui
        myGui.run()

        (OR)
        myGui.run(dockable=False)

    RETURNS:
        object instance of your qt ui

    """

    try:
        if dockable:
            try:
                global qt_widget_object
                qt_widget_object.run(floating=True)

            except:
                qt_widget_object = ControlUI(**kwargs)
                qt_widget_object.run(floating=True)

        else:
            qt_widget_object = ControlUI(**kwargs)
            qt_widget_object.show()

        return qt_widget_object

    except Exception as e:
        raise RuntimeError(e)

