import maya.cmds as mc

import os
from functools import partial
from rigBot.gui import mayaWidget
from rigBot.gui import handPose_ui
from rigBot.data import kAttributes
from rigBot import utils
from rigBot import data
from rigBot import env

from Qt import QtGui
from Qt import QtCore
from Qt import QtWidgets

class HandPoseUI(mayaWidget.MayaWidget):

    def __init__(self):
        mayaWidget.MayaWidget.__init__(self)

        title = 'handPose_UI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.ui = handPose_ui.Ui_handPoseUI()
        self.ui.setupUi(self)
        self.setObjectName('handPose_UI')

        self.ctrl = ''
        self.attr = ''
        self.prefix = ''
        self.pose_grps = []
        self.ctrl_suffix = utils.get_suffix('animCtrl')

        self.ui.stamp_btn.clicked.connect(self.stamp_pose)
        self.ui.unstamp_btn.clicked.connect(self.unstamp_pose)
        self.ui.mirror_btn.clicked.connect(self.copy_pose)
        self.ui.save_btn.clicked.connect(self.save)

        self.setMinimumHeight(180)
        self.setMaximumHeight(180)
        self.setMinimumWidth(235)
        self.setMaximumWidth(235)

        self.center()

    def get_ctrl_attr(self, skip_attr_check=False):
        """Get current ctrl and pose attr to set"""

        selection = mc.ls(sl=1)
        if not selection:
            mc.warning('Select a hand ctrl to set poses on!')
            return False

        attrs = ['spread','fist','cup','reverseCup']
        for attr in attrs:
            if not mc.objExists(selection[0]+'.'+attr):
                msg = 'Spread, fist cup OR reverseCup attrs do not exist on this ctrl!'
                mc.warning(msg)
                return False

        attr = None
        selected_attrs = utils.get_selected_attrs(verbose=False)

        if not skip_attr_check:
            if not selected_attrs:
                mc.warning('Select an attribute in the channelbox to set poses on!')
                return False

            attr = selected_attrs[0]
            if not attr in ['spread','fist','cup','reverseCup'] and 'Curl' not in attr:
                mc.warning('Current attr is not settable: '+attr)
                return False

        self.ctrl = selection[0]
        self.attr = attr
        self.prefix = selection[0].replace('_hand_'+self.ctrl_suffix, '')
        self.pose_grps = mc.ls(self.prefix+'_thumb*'+self.ctrl_suffix+'_AUTO',
                               self.prefix+'_index*'+self.ctrl_suffix+'_AUTO',
                               self.prefix+'_middle*'+self.ctrl_suffix+'_AUTO',
                               self.prefix+'_ring*'+self.ctrl_suffix+'_AUTO',
                               self.prefix+'_pinky*'+self.ctrl_suffix+'_AUTO')

        return True

    @utils.undoable
    def stamp_pose(self):

        self.unlock_nodes()

        if not self.get_ctrl_attr():
            return

        for grp in self.pose_grps:
            ctrl = grp.replace('_AUTO', '')

            if mc.objExists(grp+'.'+self.attr+'X'):
                mc.setAttr(grp+'.'+self.attr+'X', (mc.getAttr(ctrl+'.rx')))

            if mc.objExists(grp+'.'+self.attr+'Y'):
                mc.setAttr(grp+'.'+self.attr+'Y', (mc.getAttr(ctrl+'.ry')))

            if mc.objExists(grp+'.'+self.attr+'Z'):
                mc.setAttr(grp+'.'+self.attr+'Z', (mc.getAttr(ctrl+'.rz')))

            mc.xform(ctrl, a=1,ro=[0,0,0])

        mc.select(self.ctrl)

    @utils.undoable
    def unstamp_pose(self):

        self.unlock_nodes()

        if not self.get_ctrl_attr():
            return

        mc.setAttr(self.ctrl+'.spread', 0)
        mc.setAttr(self.ctrl+'.fist', 0)
        mc.setAttr(self.ctrl+'.cup', 0)
        mc.setAttr(self.ctrl+'.reverseCup', 0)

        for grp in self.pose_grps:
            ctrl = grp.replace('_AUTO', '')

            if mc.objExists(grp+'.'+self.attr+'X'):
                mc.setAttr(ctrl+'.rx', (mc.getAttr(grp+'.'+self.attr+'X')))

            if mc.objExists(grp+'.'+self.attr+'Y'):
                mc.setAttr(ctrl+'.ry', (mc.getAttr(grp+'.'+self.attr+'Y')))

            if mc.objExists(grp+'.'+self.attr+'Z'):
                mc.setAttr(ctrl+'.rz', (mc.getAttr(grp+'.'+self.attr+'Z')))

    @utils.undoable
    def copy_pose(self):

        self.unlock_nodes()

        if not self.get_ctrl_attr(skip_attr_check=True):
            return

        selection = mc.ls(sl=1)

        if not len(selection) == 2:
            mc.warning('Select the source, then the desitnation hand ctrls to copy.')
            return

        dst_prefix = selection[1].replace('_hand_'+self.ctrl_suffix, '')
        attrs = mc.listAttr(self.ctrl, ud=1, k=1)

        for grp in self.pose_grps:
            dst_grp = grp.replace(self.prefix, dst_prefix, 1)

            for attr in attrs:
                if mc.objExists(dst_grp+'.'+attr+'X'):
                    mc.setAttr(dst_grp+'.'+attr+'X', mc.getAttr(grp+'.'+attr+'X'))

                if mc.objExists(dst_grp+'.'+attr+'Y'):
                    mc.setAttr(dst_grp+'.'+attr+'Y', mc.getAttr(grp+'.'+attr+'Y'))

                if mc.objExists(dst_grp+'.'+attr+'Z'):
                    mc.setAttr(dst_grp+'.'+attr+'Z', mc.getAttr(grp+'.'+attr+'Z'))

        mc.select(selection[1])

    def save(self):

        ext = kAttributes.file_extention
        file_filter = data.get_file_filter('kAttributes')[0]
        base_path = os.path.join(env.get_rigbuild_path(), 'data', env.get_variant())

        if not os.path.isdir(base_path):
            base_path = utils.file_browser('SAVE MULTIPLE', file_filter=file_filter, file_path=base_path)

        if not base_path:
            return

        data_path = os.path.join(base_path, 'handPose'+ext)

        nodes = [n.replace('.handPoseNode', '') for n in mc.ls('*.handPoseNode')]
        kAttributes.save(data_path, nodes)

    def unlock_nodes(self):
        nodes = [n.replace('.handPoseNode', '') for n in mc.ls('*.handPoseNode')]
        utils.set_attrs(nodes, k=1)

def run():
    ui = HandPoseUI()
    ui.show()
