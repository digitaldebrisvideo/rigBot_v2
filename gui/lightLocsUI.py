import maya.cmds as mc

import os
from functools import partial
from rigBot.gui import mayaWidget
from rigBot.gui import lightLocs_ui
from rigBot.data import kAttributes
from rigBot.data import constraints

from rigBot import utils
from rigBot import data
from rigBot import env

from Qt import QtGui
from Qt import QtCore
from Qt import QtWidgets

reload(lightLocs_ui)

class LightLocsUI(mayaWidget.MayaWidget):

    def __init__(self):
        mayaWidget.MayaWidget.__init__(self)

        title = 'lightLocs_ui'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.ui = lightLocs_ui.Ui_lightLocsUI()
        self.ui.setupUi(self)
        self.setObjectName('lightLocs_ui')

        self.setMinimumHeight(172)
        self.setMaximumHeight(172)
        self.setMinimumWidth(340)
        self.setMaximumWidth(340)

        self.ui.lineEdit.setPlaceholderText('OR generate name based on selection.')
        self.center()

        self.ui.create_btn.released.connect(self.create)
        self.ui.update_btn.released.connect(self.update_xforms)
        self.ui.save_btn.released.connect(self.save_all)

        item = QtWidgets.QAction(self)
        item.setText('Convert selected locators to tagged lighting locators.')
        item.triggered.connect(self.convert_sel)
        self.ui.create_btn.addAction(item)

    def create(self):
        name = self.ui.lineEdit.text()
        mc.select(utils.create_light_locator(name=name, xforms=[]))

    def convert_sel(self):

        sel = mc.ls(sl=1)
        cache_sel = mc.ls('cache_SEL')
        model_grp = mc.ls('model_GRP', '*model_GRP')

        if not cache_sel:
            mc.warning('"cache_SEL" does not exist! Cannot continue.')
            return

        if not model_grp:
            mc.warning('model_GRP does not exist! Cannot continue.')
            return

        for s in sel:

            # find constraint driver
            drv = get_con_driver(s)
            if not drv :
                drv = utils.get_parent(sel)

            if not drv:
                mc.warning('Could not find driver based on parent or constraints, Maybe just create one from scratch..')
                return

            # parent properly if not parented
            utils.set_attrs(s, l=0, k=1)
            par = utils.get_parent(s)
            if model_grp and par != model_grp[0]:
                mc.parent(s, model_grp[0])

            cons = utils.get_constraints(s)
            if cons:
                mc.delete(cons)

            mc.parentConstraint(drv, s, n=s+'_PRC', mo=1)
            mc.scaleConstraint(drv, s, n=s+'_SC', mo=1)
            mc.sets(s, add=cache_sel[0])

            try:
                if not mc.objExists(s+'.lightingLocator'):
                    mc.addAttr(s, ln='lightingLocator', at='message')
            except:
                pass

            print 'Converted {0} to a tagged lighting locator! '.format(s)

    def update_xforms(self):

        sel = mc.ls(sl=1)
        for s in sel:
            c_data = constraints.get_data(s)
            mc.delete(utils.get_constraints(s))
            constraints.set_data(c_data, verbose=False)

    def save_all(self):
        data.save('lightLocators')

def run():
    ui = LightLocsUI()
    ui.show()


def get_con_driver(node):
    cons = [c for c in utils.get_constraints(node) if mc.nodeType(c) in ['pointConstraint','parentConstraint']]
    drv = ''
    if cons:
        for c in cons:
            drv = list(set([x for x in mc.listConnections(c+'.target') if x != c]))
        if drv:
            drv = drv[0]
    return drv

