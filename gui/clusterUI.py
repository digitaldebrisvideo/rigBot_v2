import maya.cmds as mc
import maya.OpenMaya as om
import maya.OpenMayaAnim as oma

from functools import partial

from rigBot import utils
from rigBot.gui import mayaWidget
from rigBot.gui import cluster_ui
from rigBot.data import cluster

from Qt import QtGui
from Qt import QtCore
from Qt import QtWidgets

file_extention = '.cls'
deformer_type = 'cluster'

reload(cluster_ui)

class ClusterUI(mayaWidget.MayaWidget):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, parent=None):
        mayaWidget.MayaWidget.__init__(self, parent=parent)

        title = 'cluster_UI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = cluster_ui.Ui_ClusterUI()
        self.ui.setupUi(self)
        self.setObjectName(title)

        mayaWidget.setColor(self.ui.create_btn)
        mayaWidget.setColor(self.ui.mirror_btn)

        self.ui.weighted_node_btn.released.connect(partial(self.get_selected, self.ui.weighted_node_line))
        self.ui.prebind_node_btn.released.connect(partial(self.get_selected, self.ui.prebind_node_line))
        self.ui.mirror_weighted_node_btn.released.connect(partial(self.get_selected, self.ui.mirror_weighted_node_line))
        self.ui.mirror_prebind_node_btn.released.connect(partial(self.get_selected, self.ui.mirror_prebind_node_line))

        self.ui.mirror_weighted_node_btn_2.released.connect(partial(self.get_cluster, self.ui.mirror_cluster_line))
        self.ui.mirror_weighted_node_btn_3.released.connect(partial(self.get_cluster, self.ui.mod_cluster_line))

        self.ui.mirror_cluster_line.setPlaceholderText('No cluster Selected')
        self.ui.mod_cluster_line.setPlaceholderText('No cluster Selected')

        self.ui.create_btn.released.connect(self.create)
        self.ui.create_soft_btn.released.connect(partial(self.create, soft_weights=True))

        self.ui.mirror_btn.released.connect(self.mirror)
        self.ui.add_btn.released.connect(self.add)
        self.ui.connect_prebind_btn.released.connect(self.connect_prebind)
        self.ui.set_soft_weights_btn.released.connect(self.set_soft_weights)

        self.setMinimumWidth(345)
        self.setMinimumHeight(570)
        self.setMaximumHeight(570)

        self.center()

    def get_cluster(self, line_edit_item):

        sel = [s.split('.')[0] for s in mc.ls(sl=1)]
        if not sel:
            mc.warning('Nothing selected!')
            return

        deformer, shapes = utils.get_deformers_and_shapes(sel, deformer_type)

        if sel and not deformer:
            shapes = utils.get_shapes(sel[0])
            deformers = []
            for shape in shapes:
               deformers.extend(mc.listConnections(sel[0], type='cluster') or [])

            if len(deformers) > 1:
                deformer = mayaWidget.choose_deformer(deformers)
            elif len(deformers) == 1:
                deformer = deformers[0]

        if deformer:
            line_edit_item.setText(deformer)

        else:
            line_edit_item.setText('')
            mc.warning('No clusters found on selection!')

    def get_selected(self, line_edit_item):

        sel = mc.ls(sl=1)
        if not sel:
            mc.warning('Nothing selected!')
            return

        line_edit_item.setText(sel[0])


    def create(self, soft_weights=False):

        nodes = mc.ls(sl=1)
        if not nodes:
            mc.warning('Nothing is selected!')
            return

        name = self.ui.name_line.text() or 'cluster#'
        weighted_node = mc.ls(self.ui.weighted_node_line.text()) or ''
        prebind_node = mc.ls(self.ui.prebind_node_line.text()) or None

        if weighted_node:
            weighted_node = weighted_node[0]

        if prebind_node:
            prebind_node = prebind_node[0]

        clss = cluster.create(nodes, weighted_node, prebind_node, name)
        if soft_weights:
            mc.select(nodes)
            cluster.set_soft_weights(clss[0])

        if weighted_node:
            mc.select(weighted_node)

        else:
            mc.select(clss[-1])


    def set_soft_weights(self):
        deformer = self.ui.mod_cluster_line.text()
        if not mc.objExists(deformer):
            mc.warning(deformer+' does not exist!')
            return

        cluster.set_soft_weights(deformer)


    def mirror(self):

        source_deformer = self.ui.mirror_cluster_line.text()
        new_weighted_node = mc.ls(self.ui.mirror_weighted_node_line.text()) or ''
        new_prebind_node = mc.ls(self.ui.mirror_prebind_node_line.text()) or None

        if not mc.objExists(source_deformer):
            mc.warning(source_deformer+' does not exist!')
            return

        if new_weighted_node:
            new_weighted_node = new_weighted_node[0]

        if new_prebind_node:
            new_prebind_node = new_prebind_node[0]

        cluster.mirror(source_deformer, None, new_weighted_node, new_prebind_node)

        if new_weighted_node:
            mc.select(new_weighted_node)
        else:
            mc.select(cl=1)

    def connect_prebind(self):
        deformer = self.ui.mod_cluster_line.text()

        nodes = mc.ls(sl=1)
        if not nodes:
            mc.warning('Nothing is selected!')
            return

        cluster.connect_prebind(nodes[0], deformer)
        print nodes[0]+' connected to prebind: '+deformer


    def add(self):
        deformer = self.ui.mod_cluster_line.text()

        nodes = mc.ls(sl=1)
        if not nodes:
            mc.warning('Nothing is selected!')
            return

        cluster.add(nodes, deformer)
        print 'Selection was added to : '+deformer

# you need this
qt_widget_object = None
def run(dockable=False, **kwargs):
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
                qt_widget_object = ClusterUI(**kwargs)
                qt_widget_object.run(floating=True)

        else:
            qt_widget_object = ClusterUI(**kwargs)
            qt_widget_object.show()

        return qt_widget_object

    except Exception as e:
        raise RuntimeError(e)

