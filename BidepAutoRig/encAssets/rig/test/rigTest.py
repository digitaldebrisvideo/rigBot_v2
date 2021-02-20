"""

    Rig Test by Jennifer Hachigian

    v001 - 05/05/2016
    v003 - 08/08/2016 -- Added "roll_toe" to delete animation blacklist
    v004 - 08/08/2016 -- delete animation routine now pulled from _encLib.py
    v006 - 05/22/2017 -- now checks if sys paths are present before attempting to append them
    v007 - now works with both Maya 2017 (PySide2) and Maya 2014 (PySide)
"""

import os
# import PySide.QtCore as QtCore
import re

import pymel.core as pm
import encLib as enc
from encLib.Qt import QtCore

'''
========================================================================
---->  Global Variables and Functions <----
========================================================================
'''
TOOLS_PATH = os.path.dirname(__file__)

WINDOW_TITLE = 'Rig Test'
WINDOW_VERSION = 1.07
WINDOW_NAME = 'rigTest_tool_window'

UI_FILE_PATH = os.path.join(TOOLS_PATH, 'rigTest.ui')
UI_OBJECT, BASE_CLASS = enc.get_pyside_class(UI_FILE_PATH)

atom_file = os.path.join(os.path.dirname(__file__), "calisthenics.atom")


def load_atom_plugin():
    li = pm.pluginInfo(query=True, listPlugins=True)
    if li is None or "atomImportExport" not in li:
        pm.loadPlugin("atomImportExport")


def get_set_nodes():
    sets = [x for x in pm.ls(type='objectSet') if x.type() == 'objectSet' and
            x.restriction() == 'none' and x.name().lower().find("ctrl") != -1]
    nodes = []
    for s in sets:
        nodes += [x for x in pm.sets(s, query=True) if x not in nodes]
    return nodes


def set_time_slider(start, end):
    cur_time = pm.currentTime(query=True)
    pm.playbackOptions(minTime=start, maxTime=end)
    if cur_time < start:
        pm.currentTime(start)
    elif cur_time > end:
        pm.currentTime(end)


def load_atom_file():
    nodes = get_set_nodes()
    pm.select(nodes)
    print "Analyzing:", atom_file
    with open(atom_file, "r") as fp:
        text = fp.read()
    start = re.compile("(?<=startTime )\d+(?=;)").findall(text)[0]
    end = re.compile("(?<=endTime )\d+(?=;)").findall(text)[0]
    print "\tstartTime:", start, "endTime:", end
    opt = "time%s%s;match=string;selected=selectedOnly;" % (start, end)
    atom_nms = os.path.basename(atom_file).rsplit(".", 1)[0]
    pm.cmds.file(atom_file, i=True, type='atomImport', renameAll=True, namespace=atom_nms, options=opt)
    set_time_slider(start, end)


def has_string(x, li):
    for s in li:
        if x.lower().find(s) != -1:
            return True
    return False


def delete_atom():
    nodes = get_set_nodes()
    enc.delete_anim(nodes)


'''
========================================================================
---->  Create/Connect UI Functionality  <----
========================================================================
'''


class RigTest(BASE_CLASS, UI_OBJECT):
    def __init__(self, parent=enc.get_maya_window()):
        super(RigTest, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle('{0} {1}'.format(WINDOW_TITLE, str(WINDOW_VERSION)))
        """ init data"""
        load_atom_plugin()
        """ UI Connect """
        self.pushButtonATOM.clicked.connect(load_atom_file)
        self.pushButtonDelete.clicked.connect(delete_atom)
        self.pushButtonClose.clicked.connect(self.close)


def launch():
    print "Launching..."
    global rig_test
    try:
        rig_test.close()
    except:
        rig_test = RigTest()
        rig_test.show()