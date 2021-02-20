import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
import maya.OpenMayaAnim as oma

from functools import partial
import cPickle as pickle
import time
import os

from rigBot import utils
from rigBot.gui import mayaWidget
from rigBot.gui import splitBlendTargets_ui
from rigBot.gui import remapDialog

from Qt import QtGui
from Qt import QtCore
from Qt import QtWidgets

def create_split(shape, target, num_split=3):
    """Create a paintable ski ncluster to split out bs target"""

    new = mc.duplicate(shape, n=shape+'_bsh_split')[0]
    if utils.get_parent(new):
        mc.parent(new, w=1)

    mc.select(new)
    mm.eval('polyColorPerVertex -r 0.35 -g 0.2953 -b 0.384 -a 1 -cdo;')
    mc.delete(new, ch=1)

    top = mc.createNode('transform', n='split_bsh_nodes')
    jnts = []
    for i in range(num_split):
        jnts.append(mc.createNode('joint', n=new+'_'+str(i)))

    for i, jnt in enumerate(jnts):
        mc.xform(jnt, r=1, t=[i,0,0])

    scls = mc.skinCluster(new, jnts, tsb=1, n=new+'_skn')
    mc.setAttr(scls[0]+'.envelope', 0)
    utils.set_attrs(new, 't r s', l=0, k=1)
    mc.hide(jnts)

    bss = mc.blendShape(new, n=new+'_split_bsh')
    dups = []
    for i in range(num_split):
        trg_name = target+str(i)
        dup = mc.duplicate(target, n=trg_name)[0]
        mc.blendShape(bss[0], e=1, t=(new, i, dup, 1.0))
        dups.append(dup)

    mc.hide(dups)
    mc.parent(jnts, dups, top)

    if mc.objExists(new+'.splitBaseShape'):
        mc.deleteAttr(new+'.splitBaseShape')

    if mc.objExists(new+'.splitTargetShape'):
        mc.deleteAttr(new+'.splitTargetShape')

    mc.addAttr(new, ln='splitBaseShape', dt='mesh')
    mc.addAttr(new, ln='splitTargetShape', dt='mesh')
    mc.connectAttr(shape+'.outMesh', new+'.splitBaseShape')
    mc.connectAttr(target+'.outMesh', new+'.splitTargetShape')

    mc.parent(top, new)
    mc.select(new)
    return new

def update_split_weights(skinned_shape):
    """Create split shapes from skin weights"""

    scls = utils.get_deformers(skinned_shape, 'skinCluster')[0]
    bsh = utils.get_deformers(skinned_shape, 'blendShape')[0]
    verts = mc.polyEvaluate(skinned_shape, vertex=True)
    jnts = mc.skinCluster(scls, q=1, inf=1)
    num_split = len(jnts)

    targets = mc.blendShape(bsh, q=1, t=1)
    for i, jnt in enumerate(jnts):
        trg_name = targets[i]
        weights = [mc.skinPercent(scls, '{0}.vtx[{1}]'.format(skinned_shape, vert), q=1, t=jnt) for vert in range(verts)]
        mc.setAttr('{0}.inputTarget[0].inputTargetGroup[{1}].targetWeights[0:{2}]'.format(bsh, i, verts-1), *weights)
        mc.refresh()
        value = mc.getAttr(bsh+'.'+trg_name)

        mc.setAttr(bsh+'.'+trg_name, 0)
        mc.setAttr(bsh+'.'+trg_name, 1)
        mc.refresh()

        mc.setAttr(bsh+'.'+trg_name, value)

    print 'Updated weights for: '+bsh

def create_split_shapes(skinned_shape, target):

    scls = utils.get_deformers(skinned_shape, 'skinCluster')[0]
    bsh = utils.get_deformers(skinned_shape, 'blendShape')[0]
    verts = mc.polyEvaluate(skinned_shape, vertex=True)
    jnts = mc.skinCluster(scls, q=1, inf=1)
    num_split = len(jnts)

    bbox = mc.exactWorldBoundingBox(skinned_shape)
    dist = bbox[3]-bbox[0]

    children = utils.get_children(skinned_shape)
    mc.parent(children, w=1)

    # zero bsh
    for i, jnt in enumerate(jnts):
        trg_name = target+str(i)
        mc.setAttr(bsh+'.'+trg_name, 0)

    targets = []
    for i, jnt in enumerate(jnts):
        trg_name = target+str(i)

        mc.setAttr(bsh+'.'+trg_name, 1)

        if not mc.objExists(trg_name+'_TRG'):
            trg = mc.duplicate(skinned_shape, n=trg_name+'_TRG')[0]
            mc.xform(trg_name, r=1, t=[(i+1)*dist,0,0])

            if mc.objExists(trg+'.splitBaseShape'):
                mc.deleteAttr(trg+'.splitBaseShape')

            if mc.objExists(trg+'.splitTargetShape'):
                mc.deleteAttr(trg+'.splitTargetShape')

        else:
            src_shape = utils.get_shapes(skinned_shape)
            trg_shape = utils.get_shapes(trg_name)
            mc.connectAttr(src_shape[0]+'.outMesh', trg_shape[0]+'_TRG.inMesh')
            mc.disconnectAttr(src_shape[0]+'.outMesh', trg_shape[0]+'_TRG.inMesh')

        targets.append(trg_name)
        mc.setAttr(bsh+'.'+trg_name, 0)

    if children:
        mc.parent(children, skinned_shape)
    return targets

class SplitTargetsUI(mayaWidget.MayaWidget):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, parent=None, ignore_missing=False, label=''):
        mayaWidget.MayaWidget.__init__(self, parent=parent)

        title = 'cluster_UI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = splitBlendTargets_ui.Ui_SplitTargetsUI()
        self.ui.setupUi(self)
        self.setObjectName(title)

        self.setMinimumWidth(325)
        self.setMinimumHeight(275)
        self.setMaximumHeight(275)

        self.ui.lineEdit.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit.setText('3')

        self.ui.create_btn.released.connect(self.create)
        self.ui.update_btn.released.connect(self.update_weights)
        self.ui.generate_btn.released.connect(self.generate_targets)
        self.ui.load_btn.released.connect(self.load_setup)
        self.ui.mesh_btn.released.connect(partial(self.get_selected, self.ui.mesh_line))
        self.ui.target_btn.released.connect(partial(self.get_selected, self.ui.target_line))

        self.base = None
        self.target = None
        self.split_shape = None
        self.inf_count = 3

        self.center()

    def get_selected(self, line_edit_item):

        sel = mc.ls(sl=1)
        if not sel:
            mc.warning('Nothing selected!')
            return

        line_edit_item.setText(sel[0])

    def load_setup(self, split_shape=None):

        if split_shape:
            sel = [split_shape]
        else:
            sel = mc.ls(sl=1)
        if not sel:
            mc.warning('Nothing is selected!')
            return

        if not mc.objExists(sel[0]+'.splitTargetShape'):
            mc.warning('No split mesh selected!')
            return

        scls = utils.get_deformers(sel[0], 'skinCluster')
        if not scls:
            mc.warning('No split skinCluster found!')
            return

        base = mc.listConnections(sel[0]+'.splitBaseShape')
        target = mc.listConnections(sel[0]+'.splitTargetShape')

        if not base or not target:
            mc.warning('No split mesh selected!')
            return

        self.base = base[0]
        self.target = target[0]
        self.split_shape = sel[0]
        self.inf_count = len(mc.skinCluster(scls[0], q=1, inf=1))

        self.ui.mesh_line.setText(self.base)
        self.ui.target_line.setText(self.target)
        self.ui.lineEdit.setText(str(self.inf_count))

    def create(self):

        self.base = self.ui.mesh_line.text()
        self.target = self.ui.target_line.text()
        self.inf_count = int(self.ui.lineEdit.text())

        if not self.base or not self.target:
            mc.warning('Set mesh and target!')
            return

        if self.inf_count < 2:
            mc.warning('Split must be greater than 1!')
            return

        self.split_shape = create_split(self.base, self.target, self.inf_count)


    def update_weights(self):

        if not self.split_shape:
            mc.warning('Setup not loaded!')
            return

        update_split_weights(self.split_shape)


    def generate_targets(self):

        if not self.split_shape or not self.split_shape:
            mc.warning('Setup not loaded!')
            return

        create_split_shapes(self.split_shape, self.target)

qt_widget_object = None
def run(dockable=False, **kwargs):
    """
    This is boiler plate code for launching your dockable UI,
    Copy and paste this into your ui module. then change the className from MayaWidget
    to whatever your class name is.

    UIs using this run wrapper require your UI class to inherit the MayaWidget
    class that is defined above, in this module.

    Usage:
        import myGui
        myGui.run()
        (OR)
        myGui.run(dockable=False)

    Returns:
        object instance of your qt ui """

    try:
        if dockable:
            try:
                global qt_widget_object
                qt_widget_object.run(floating=True)

            except:
                qt_widget_object = SplitTargetsUI(**kwargs)
                qt_widget_object.run(floating=True)

        else:
            qt_widget_object = SplitTargetsUI(**kwargs)
            qt_widget_object.show()

        return qt_widget_object

    except Exception as e:
        raise RuntimeError(e)
