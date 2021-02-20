from Qt import QtCompat
from Qt import QtGui
from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

try:
    from shiboken2 import wrapInstance
except:
    from shiboken import wrapInstance

import maya.OpenMayaUI as omui
import maya.cmds as mc
import maya.mel as mm

def create(gravity=9.8, mass=10.0, rotateInertia=None, frameRange=[], bakeRunup=True):
    """Create a cube and bake gravitational and rotational velocity."""

    def getFrameRange(start=None, end=None):
        '''Returns the frame range based on the highlighted timeslider,
        or otherwise the playback range.'''

        if not start and not end:
            gPlayBackSlider = mm.eval('$temp=$gPlayBackSlider')
            if mc.timeControl(gPlayBackSlider, query=True, rangeVisible=True):
                frameRange = mc.timeControl(gPlayBackSlider, query=True, rangeArray=True)
                start = frameRange[0]
                end = frameRange[1]
            else:
                start = mc.playbackOptions(query=True, min=True)
                end = mc.playbackOptions(query=True, max=True)

        return start, end

    def getFrameRate():
        """Return an int of the current frame rate"""

        currentUnit = mc.currentUnit(query=True, time=True)
        if currentUnit == 'film':
            return 24
        if currentUnit == 'show':
            return 48
        if currentUnit == 'pal':
            return 25
        if currentUnit == 'ntsc':
            return 30
        if currentUnit == 'palf':
            return 50
        if currentUnit == 'ntscf':
            return 60
        if 'fps' in currentUnit:
            return int(currentUnit.substitute('fps',''))

        return 1

    def matchPosition(target, node):
        """Snap the second obj to the first obj"""

        t_xform = mc.xform(target, q=1, ws=1, t=1)
        r_xform = mc.xform(target, q=1, ws=1, ro=1)
        mc.xform(node, ws=1, t=t_xform, ro=r_xform)

    sel = mc.ls(sl=True)

    mass = float(mass)
    gravity = float(gravity)

    if mass < 0.001:
        mass = 0.001

    if gravity < 0.001:
        gravity = 0.001

    if not sel:
        raise RuntimeError('Please select an object.')

    if [x for x in sel if not mc.objExists(x+'.translate')]:
        raise RuntimeError('This only works on transform nodes.')

    unit = mc.currentUnit(q=True, linear=True)
    frameRate = getFrameRate()
    timeFactor = 1.0 / frameRate
    tt = 'spline'

    # rotationalInertia
    if rotateInertia is None:
        if mass < 20:
            rotateInertia = 0.5 + (((mass-0.001)/(20-0.001)) * (1.0-0.5))
        else:
            rotateInertia = 0.5 + (((mass-20)/(100-20)) * (1.0-0.5))

    rotateInertia = float(rotateInertia)
    print rotateInertia

    #default is meters
    distFactor = mass * 0.05

    if unit == 'mm':
        distFactor = 1000 * mass * 0.05
    elif unit == 'cm':
        distFactor = 100 * mass * 0.05
    elif unit == 'km':
        distFactor = 0.001 * mass * 0.05
    elif unit == 'in':
        distFactor = 39.3701 * mass * 0.05
    elif unit == 'ft':
        distFactor = 3.28084 * mass * 0.05
    elif unit == 'yd':
        distFactor = 1.09361 * mass * 0.05
    elif unit == 'mi':
        distFactor = 0.000621371 * mass * 0.05

    g = gravity * distFactor

    if len(frameRange) == 2:
        start, end = frameRange
        runup = mc.playbackOptions(q=True, min=True)

    elif len(frameRange) == 3:
        runup, start, end = frameRange

    else:
        start, end = getFrameRange()
        runup = mc.playbackOptions(q=True, min=True)

    runup = int(runup)
    start = int(start)
    end = int(end)

    # Create cube
    cube = mc.polyCube(ch=0, n='pCube_velocity')[0]
    mm.eval('polyColorPerVertex -r 0.4264 -g -0.341 -b 2.8889 -a 1 -cdo;')
    mc.delete(cube, ch=1)

    # bake for runup:
    if bakeRunup and runup < start:
        for f in range(runup, start):
            mc.currentTime(f)
            matchPosition(sel[0], cube)
            mc.setKeyframe(cube+'.translate', itt=tt, ott=tt)
            mc.setKeyframe(cube+'.rotate', itt=tt, ott=tt)

    # get prev xforms
    mc.currentTime(start-1)
    matchPosition(sel[0], cube)
    mc.setKeyframe(cube+'.translate', itt=tt, ott=tt)
    mc.setKeyframe(cube+'.rotate', itt=tt, ott=tt)

    prevTrans = mc.getAttr(cube+'.translate')[0]
    prevRot = mc.getAttr(cube+'.rotate')[0]

    # get start xforms
    mc.currentTime(start)
    matchPosition(sel[0], cube)
    mc.setKeyframe(cube+'.translate', itt=tt, ott=tt)
    mc.setKeyframe(cube+'.rotate', itt='linear', ott='linear')

    startTrans = mc.getAttr(cube+'.translate')[0]
    startRot = mc.getAttr(cube+'.rotate')[0]

    xInit = startTrans[0]-prevTrans[0]
    yInit = startTrans[1]-prevTrans[1]
    zInit = startTrans[2]-prevTrans[2]
    xInitR = startRot[0]-prevRot[0]
    yInitR = startRot[1]-prevRot[1]
    zInitR = startRot[2]-prevRot[2]

    # Set constant keyframes
    mc.cutKey(cube, attribute='translate', time=(start+0.1,end+0.5))
    mc.setKeyframe(cube, attribute='translateX', time=start+1, value=startTrans[0]+xInit, itt=tt, ott=tt)
    mc.setKeyframe(cube, attribute='translateZ', time=start+1, value=startTrans[2]+zInit, itt=tt, ott=tt)
    mc.setKeyframe(cube, attribute='translateX', time=end, value=startTrans[0]+(xInit*(end-start)), itt=tt, ott=tt)
    mc.setKeyframe(cube, attribute='translateZ', time=end, value=startTrans[2]+(zInit*(end-start)), itt=tt, ott=tt)

    val = startRot[0] + (((rotateInertia -0)/(1-0)) * ((rotateInertia*(startRot[0]+(xInitR*(end-start))))-startRot[0]))
    mc.setKeyframe(cube, attribute='rotateX', time=end, value=val, itt='flat', ott='flat')

    val = startRot[1] + (((rotateInertia -0)/(1-0)) * ((rotateInertia*(startRot[1]+(yInitR*(end-start))))-startRot[1]))
    mc.setKeyframe(cube, attribute='rotateY', time=end, value=val, itt='flat', ott='flat')

    val = startRot[2] + (((rotateInertia -0)/(1-0)) * ((rotateInertia*(startRot[2]+(zInitR*(end-start))))-startRot[2]))
    mc.setKeyframe(cube, attribute='rotateZ', time=end, value=val, itt='flat', ott='flat')

    # set gravity / mass based keyframes on .translateY
    for i,f in enumerate(range(start,end+1)):
        t = i * timeFactor
        y = startTrans[1] + (i * yInit) - (g * t * t)/2

        mc.setKeyframe(cube, attribute='translateY', time=f, value=y, itt=tt, ott=tt)

    mc.currentTime(start)
    mc.select(cube)


class BakeVelocity(QtWidgets.QDialog):
    """base widget class (will eventually be dockable)"""

    def __init__(self, parent=None):

        if not parent:
            main_window_ptr = omui.MQtUtil.mainWindow()
            parent = wrapInstance(long(main_window_ptr), QtWidgets.QDialog)
        super(BakeVelocity, self).__init__(parent)

        if mc.window('bakeVelocityUI', q=1, ex=1):
            mc.deleteUI('bakeVelocityUI')

        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                           QtWidgets.QSizePolicy.Preferred)

        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setMaximumWidth(245)
        self.setMinimumWidth(245)
        self.setMaximumHeight(228)
        self.setMinimumHeight(228)

        self.setObjectName('bakeVelocityUI')

        self.ui.gravityLine.editingFinished.connect(self.validateGravityLine)
        self.ui.massLine.editingFinished.connect(self.validateMassLine)
        self.ui.rotLine.editingFinished.connect(self.validateRotLine)

        item = QtWidgets.QAction(self)
        item.setText('Reset To Default Values.')
        item.triggered.connect(self.resetPhyicalProperties)
        self.ui.groupBox.addAction(item)

        self.ui.createBtn.released.connect(self.create)

    def resetPhyicalProperties(self):
        self.ui.gravityLine.setText('9.8')
        self.ui.rotLine.setText('0.5')
        self.ui.massLine.setText('10.0')

    def validateRotLine(self):
        if float(self.ui.rotLine.text()) < 0.0:
            mc.warning('Value cannot be set below 0.0')
            self.ui.rotLine.setText('0.0')

        elif float(self.ui.rotLine.text()) > 1.0:
            mc.warning('Value cannot be set above 1.0')
            self.ui.rotLine.setText('1.0')

    def validateGravityLine(self):
        if float(self.ui.gravityLine.text()) < 0.001:
            mc.warning('Value cannot be set below 0.001')
            self.ui.gravityLine.setText('0.001')

    def validateMassLine(self):
        if float(self.ui.massLine.text()) < 0.001:
            mc.warning('Value cannot be set below 0.001')
            self.ui.massLine.setText('0.001')

    def create(self):
        gravity = float(self.ui.gravityLine.text())
        mass = float(self.ui.massLine.text())
        rotateInertia = float(self.ui.rotLine.text())
        bakeRunup = self.ui.QCheckBox.isChecked()

        create(gravity, mass, rotateInertia, bakeRunup=bakeRunup)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(279, 343)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(57, 57, 57);\n"
                                 "color: rgb(230, 230, 230);")
        self.label.setIndent(9)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gravityLine = QtWidgets.QLineEdit(self.groupBox)
        self.gravityLine.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.gravityLine.setObjectName("gravityLine")
        self.gridLayout.addWidget(self.gravityLine, 0, 1, 1, 1)
        self.massLine = QtWidgets.QLineEdit(self.groupBox)
        self.massLine.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.massLine.setObjectName("massLine")
        self.gridLayout.addWidget(self.massLine, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.rotLine = QtWidgets.QLineEdit(self.groupBox)
        self.rotLine.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.rotLine.setObjectName("rotLine")
        self.gridLayout.addWidget(self.rotLine, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.QCheckBox = QtWidgets.QCheckBox('Bake animation up to start frame.')
        self.QCheckBox.setObjectName('preBake')
        self.verticalLayout.addWidget(self.QCheckBox)

        self.createBtn = QtWidgets.QPushButton(Form)
        self.createBtn.setObjectName("createBtn")
        self.verticalLayout.addWidget(self.createBtn)

        self.groupBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.gravityLine.setValidator(QtGui.QDoubleValidator())
        self.massLine.setValidator(QtGui.QDoubleValidator())
        self.rotLine.setValidator(QtGui.QDoubleValidator())

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCompat.translate("Form", "Bake Velocity Utility", None, -1))
        self.label.setText(QtCompat.translate("Form", "Bake Velocity", None, -1))
        self.groupBox.setTitle(QtCompat.translate("Form", "Physical Properties", None, -1))
        self.label_2.setText(QtCompat.translate("Form", "Gravity", None, -1))
        self.gravityLine.setText(QtCompat.translate("Form", "9.8", None, -1))
        self.massLine.setText(QtCompat.translate("Form", "10.0", None, -1))
        self.label_7.setText(QtCompat.translate("Form", "Rotational Inertia", None, -1))
        self.label_3.setText(QtCompat.translate("Form", "Object Mass", None, -1))
        self.rotLine.setText(QtCompat.translate("Form", "0.5", None, -1))
        self.createBtn.setText(QtCompat.translate("Form", "Create", None, -1))

