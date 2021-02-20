import maya.cmds as mc

from functools import partial
from rigBot.gui import mayaWidget
from rigBot.gui import remapDialog_ui

try:
    from Qt import QtCompat, QtGui, QtCore, QtWidgets

except:
    from PySide2 import QtCompat, QtGui, QtCore, QtWidgets

class RemapDialog(mayaWidget.MayaWidget):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, nodes=[], ignore_missing=False, label=''):
        mayaWidget.MayaWidget.__init__(self, parent=None)

        '''
        class RemapDialog(QtWidgets.QDialog):
            """Remap UI for settind hand pose values intreractively"""

            def __init__(self, nodes=[], ignore_missing=False, label=''):
                super(Remap, self).__init__(mayaWidget.maya_main_window)
        '''

        title = 'remap_UI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = remapDialog_ui.Ui_RemapUI()
        self.ui.setupUi(self)
        self.setObjectName(title)

        self.ignore_missing_nodes = ignore_missing
        self.nodes_to_map = nodes
        self.__orig_mapping = {}
        self.mapping = {}

        mayaWidget.setColor(self.ui.okBtn)

        header = self.ui.node_tree.header()

        header.setSectionResizeMode(0, header.Stretch)
        header.setSectionResizeMode(2, header.Stretch)
        header.setSectionResizeMode(1, header.Fixed)
        header.resizeSection(1, 30)
        header.setHidden(1)

        self.ui.filter_chx.toggled.connect(self.update_tree)

        self.ui.remapBtn.released.connect(self.search_an_replace)
        self.ui.reloadBtn.released.connect(self.reset)
        self.ui.cancelBtn.released.connect(self.cancel)
        self.ui.okBtn.released.connect(self.finish)

        if label:
            self.setWindowTitle(label)

        self.ui.pushButton.released.connect(partial(self.map_selection))

        self.initalize_mapping()
        self.update_tree()

        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def search_an_replace(self):
        """Search and replace mapped node names"""

        search_for = self.ui.searchLine.text()
        replace_with = self.ui.replaceLine.text()
        prefix = self.ui.prefixLine.text()
        suffix = self.ui.suffixLine.text()

        for node, map_to in self.mapping.items():
            if self.ui.mode_chx.isChecked() and mc.objExists(map_to):
                continue

            if search_for:
                new_name = node.replace(search_for, replace_with)
            else:
                new_name = node

            new_name = prefix+new_name+suffix
            new_node = mc.ls(new_name)

            if new_node:
                self.mapping[node] = new_node[0]

        self.update_tree()

    def cancel(self):
        """Cancel out of this UI"""

        self.mapping = {}
        self.deleteLater()

    def reset(self):
        """Reset mapping to its initial state"""

        self.initalize_mapping(reset=True)
        self.ui.filter_chx.setChecked(False)
        self.update_tree()

    def finish(self):
        """Close UI and continue with data import"""

        self.hide()

        # first check if all nodes have been mapped
        passed_check = True
        if self.ignore_missing_nodes == False:
            for node, map_node in self.mapping.items():
                if not mc.objExists(map_node):
                    passed_check = False

        if passed_check:
            self.finish_command()
            self.deleteLater()
            return True

        else:
            self.show()
            mc.warning('Not all nodes have been mapped!')

    def finish_command(self):
        """This is an empty function to be overwritten withthe actual data load command."""

        print self.mapping
        pass

    def initalize_mapping(self, reset=False):
        """Initialize Mapping"""

        if reset:
            self.mapping = dict(self.__orig_mapping)

        for node in self.nodes_to_map:

            # chjeck if node is in scene
            map_node = ''
            sel = mc.ls(node)
            if sel:
                map_node = sel[0]

            # Add item to dict if it doesnt exist
            if node not in self.mapping.keys():
                self.mapping[node] = map_node

        self.__orig_mapping = dict(self.mapping)

    def update_tree(self):
        """Add nodes to be remaped to tree widget"""

        self.btns = []
        for i in reversed(range(self.ui.node_tree.topLevelItemCount())):
            self.ui.node_tree.takeTopLevelItem(i)

        self.nodes_to_map.sort()

        for node in self.nodes_to_map:
            map_node = self.mapping[node]

            if not mc.objExists(map_node):
                map_node = ''
                self.mapping[node] = map_node

            # If filters is on dont add this one
            if self.ui.filter_chx.isChecked() and mc.objExists(map_node):
                continue

            item = QtWidgets.QTreeWidgetItem()
            item.setText(0, node)
            item.setText(1, '>>')
            item.setText(2, map_node)
            item.setSizeHint(3, QtCore.QSize(80, 18))

            self.ui.node_tree.addTopLevelItem(item)

    def map_selection(self):
        """Map selectio nto node"""

        items = self.ui.node_tree.selectedItems() or []
        sel = mc.ls(sl=1)

        if items and sel:
            for item in items:
                node = item.text(0)
                item.setText(2, sel[0])
                self.mapping[node] = sel[0]

        elif not sel:
            mc.warning('Nothing selected!')


