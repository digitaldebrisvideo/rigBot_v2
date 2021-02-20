# StandardPart.py
import maya.cmds as mc
import maya.mel as mm

import re
import os

from rigBot import utils
from rigBot import control
from rigBot.gui import argPrompt_ui
from rigBot.gui import mayaWidget

try:
    from Qt import QtCompat, QtGui, QtCore, QtWidgets

except:
    from PySide2 import QtCompat, QtGui, QtCore, QtWidgets
    
class ArgPrompt(QtWidgets.QDialog):
    """Prompt to change the arguments to avoid name clash"""
    def __init__(self, oldSide, oldName, newSide, newName, nodes, parent=None, label=''):
        super(ArgPrompt, self).__init__(mayaWidget.maya_main_window)

        title = 'argPromptUI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = argPrompt_ui.Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle('Build Arguments Need Attenion')
        self.setObjectName(title)
        self.setModal(True)
        self.setMaximumWidth(305)
        self.setMinimumWidth(305)
        self.setMaximumHeight(213)
        self.setMinimumHeight(213)

        self.ui.part_label.setText('Confilct: '+label)

        mayaWidget.setColor(self.ui.continueBtn)
        mayaWidget.set_icon(self.ui.icon, 'warning_36x36.png')
        validSides = ['C', 'L', 'R']

        self.ui.sideCmb.addItems(validSides)

        if newSide in validSides:
            idx = validSides.index(newSide)
            self.ui.sideCmb.setCurrentIndex(idx)

        self.ui.nameLine.setText(newName)

        # connections
        self.ui.cancelBtn.released.connect(self.__cancel)
        self.ui.continueBtn.released.connect(self.__proceedWithBuild)

        self.oldSide = oldSide
        self.oldName = oldName
        self.newSide = newSide
        self.newName = newName
        self.newNames = nodes
        self.nodes = nodes

        self.success = False
        self.cancelled = False

    def __proceedWithBuild(self):

        idx = self.ui.sideCmb.currentIndex()
        self.newSide = ['C','L','R'][idx]
        self.newName = utils.clean_name(self.ui.nameLine.text())

        newPrefix = utils.join_strings([self.newSide, self.newName])
        oldPrefix = utils.join_strings([self.oldSide, self.oldName])


        # Case for checking parts that have all sided names undder it
        check_all = False
        if self.oldSide == 'C':
            test = [n for n in self.nodes if n.split('|')[-1].startswith('L') or n.split('|')[-1].startswith('R')]
            if test:
                check_all = True

       # Check for clashing names and run prompt if a change is needed
        self.newNames = getNewNodeNames(oldPrefix, newPrefix, self.nodes, check_all_sides=check_all)

        # Loop prompt for new name and side until cancelled or a valid optiop.
        self.success = True
        self.deleteLater()

        #else:
        #    mc.warning('Node names still clash!')

    def __cancel(self):
        self.newSide = self.oldSide
        self.newName = self.oldName
        self.cancelled = True
        self.deleteLater()

def getNewNodeNames(oldPrefix, newPrefix, nodes, check_all_sides=False):

    newNames = []
    for node in nodes:
        if check_all_sides:
            if node.split('|')[-1].startswith('L'):
                newName = 'C' + node.split('|')[-1][1:]
                newName = newName.replace(oldPrefix, newPrefix, 1)
                newName = 'L'+newName[1:]

            elif node.split('|')[-1].startswith('R'):
                newName = 'C' + node.split('|')[-1][1:]
                newName = newName.replace(oldPrefix, newPrefix, 1)
                newName = 'R'+newName[1:]

            else:
                newName = node.split('|')[-1].replace(oldPrefix, newPrefix, 1)

        else:
            newName = node.split('|')[-1].replace(oldPrefix, newPrefix, 1)

        newNames.append(newName)

    return newNames
