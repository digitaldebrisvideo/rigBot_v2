from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.OpenMayaUI as omui
import maya.cmds as mc

import os
import site
from functools import partial

try:
    from pyside2uic import compileUi
    from shiboken2 import wrapInstance
    pyversion = 'PySide2'

except:
    from pysideuic import compileUi
    from shiboken import wrapInstance
    pyversion = 'PySide'

try:
    from Qt import QtCompat, QtGui, QtCore, QtWidgets

except:
    from PySide2 import QtCompat, QtGui, QtCore, QtWidgets

blue_color = '#93c8f2'
purple_color= '#c6a9f9'
pink_color= '#e241f4'

try:
    icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'icons')
    maya_main_window = wrapInstance(long(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)

except:
    maya_main_window = None

def choose_deformer(items, all_button_label=False):
    """Prompt user to choose a specifc deformer"""

    dtype = 'deformer'
    for i in items:
        if mc.objExists(i):
            dtype = mc.nodeType(i)
            break

    msg = 'This shape has several {0}s items.\nChoose one.'.format(dtype)

    choose = Choose(items=items, msg=msg, all_button_label=all_button_label)
    choose.exec_()

    return choose.choice

def compile(uiFile):
    """Compile qt .ui file to Qt.py file"""

    if not os.path.isfile(uiFile):
        uiFile = os.path.join(os.path.dirname(__file__), uiFile)

    if not os.path.isfile(uiFile):
        raise RuntimeError('File does not exists: %s' % uiFile)

    # compile .ui
    pyFile = uiFile.replace('.ui','_ui.py')
    with open(pyFile, 'w') as pf:
        compileUi(uiFile, pf, False, 4,False)

    # convert to qt file
    with open(pyFile, 'r') as pf:
        lines = pf.readlines()

    for i, line in enumerate(lines):
        if pyversion == 'PySide2':
            line = line.replace('from PySide2 import',
                                'from Qt import QtCompat, QtGui,')

            line = line.replace('QtWidgets.QApplication.translate',
                                'QtCompat.translate')
        else:
            line = line.replace('QtGui','QtWidgets')
            line = line.replace('from PySide import',
                                'from Qt import QtCompat, QtGui,')

            line = line.replace('QtGui.QApplication.translate',
                                'QtCompat.translate')

            line = line.replace('QtWidgets.QFont', 'QtGui.QFont')

        lines[i] = line

        if "QtCore.SIGNAL" in line:
            raise NotImplementedError('QtCore.SIGNAL is missing from PyQt5 '
                                      'and so Qt.py does not support it: you '
                                      'should avoid defining signals inside '
                                      'your ui files.')

    lines = ''.join(lines)

    with open(pyFile, 'w') as f:
        f.write(lines)

    print 'Converted to: %s' % pyFile

def set_icon(widget, icon_name):
    """Set image on widget from rigBot icons path"""

    path = icon_name
    if not os.path.isfile(path):
        path = os.path.join(icon_path, icon_name)

    if os.path.isfile(path):

        try:
            widget.setPixmap(QtGui.QPixmap(path))
        except:
            icon = QtGui.QIcon(path)
            widget.setIcon(icon)

def setColor(widget, color='#7c5cb7', button_only=False):
    """Set rigBot standard color for specified widget"""

    if button_only:
        widget.setStyleSheet('QPushButton{background-color: %s;}' % color)
    else:
        widget.setStyleSheet('background-color: %s;' % color)

##############################################
# Widget classes
##############################################

class Choose(QtWidgets.QDialog):
    """Dialog for choosing cluster when more thasn one exists"""

    def __init__(self, items=[], msg='Choose one:', all_button_label=''):
        QtWidgets.QDialog.__init__(self)

        title = 'chooseDeformerUI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        if not items:
            self.deleteLater()
            return

        self.setWindowTitle('Choose Deformer')
        self.layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel(msg)
        self.setLayout(self.layout)
        self.layout.addWidget(self.label)

        all_items = list(items)

        items.sort()
        if all_button_label:
            items.append(all_button_label)

        self.btns = []

        for item in items:
            choice = item
            if item == all_button_label:
                choice = all_items

            self.btns.append(QtWidgets.QPushButton(item))
            self.btns[-1].released.connect(partial(self.__finish, choice=choice))
            self.layout.addWidget(self.btns[-1])

        self.choice = None

    def __finish(self, choice=None):
        self.choice = choice
        self.deleteLater()

class MayaWidget(MayaQWidgetDockableMixin, QtWidgets.QWidget):
    """Base widget class for dockable QT UIs.
        window position and state is saved IF dockable.

        USAGE:

            Your qt ui class should start something like this:

            from rigBot.gui import mayaWidget

            class Test(mayaWidget.MayaWidget):

                def __init__(self, parent=None, ignore_missing=False, label=''):
                    mayaWidget.MayaWidget.__init__(self, parent=parent)

                    title = 'test_UI'
                    if mc.window(title, q=1, ex=1):
                        mc.deleteUI(title)

                    self.setObjectName(title)

        """

    def __init__(self, parent=maya_main_window):
        super(MayaWidget, self).__init__(parent)

        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.Tool)

    def run(self, floating=True):
        """this makes your widget dockable, Maya is buggy with this."""

        try:
            self.show(dockable=True, area='right', floating=floating)

        except:
            workspaceControlName = self.objectName() + 'WorkspaceControl'
            self.deleteControl(workspaceControlName)
            self.show(dockable=True, area='right', floating=floating)

        self.raise_()

    def deleteControl(self, control):
        """deletes workspace control dor dockable widget"""

        try:
            if mc.workspaceControl(control, q=True, exists=True):
                mc.workspaceControl(control, e=True, close=True)
                mc.deleteUI(control, control=True)
        except:
            pass

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

# you need this
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

            OR
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
                qt_widget_object = MayaWidget(**kwargs)
                qt_widget_object.run(floating=True)

        else:
            qt_widget_object = MayaWidget(**kwargs)
            qt_widget_object.show()

        return qt_widget_object

    except Exception as e:
        raise RuntimeError(e)
