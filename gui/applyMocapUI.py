import maya.cmds as mc
import maya.OpenMaya as om
import maya.OpenMayaAnim as oma

from functools import partial

from rigBot import utils
from rigBot.gui import mayaWidget
from rigBot.gui import applyMocap_ui

from Qt import QtWidgets as wdg
from Qt import QtGui as gui
from Qt import QtCore as qt

reload(applyMocap_ui)

class ApplyMocapUI(mayaWidget.MayaWidget):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, parent=None):
        mayaWidget.MayaWidget.__init__(self, parent=parent)

        title = 'applyMocapUI'
        if mc.window(title, q=1, ex=1):
            mc.deleteUI(title)

        self.ui = applyMocap_ui.Ui_applyMocap()
        self.ui.setupUi(self)
        self.setObjectName(title)
        self.rigbuild_path = ''
        mayaWidget.set_icon(self.ui.icon_label, 'rc_logo.png')

        self.ui.import_btn.released.connect(self.import_mocap_fbx)
        self.ui.mocap_ns_btn.released.connect(partial(self.get_selected_ns, self.ui.mocap_ns_line))
        self.ui.rig_ns_btn.released.connect(partial(self.get_selected_ns, self.ui.rig_ns_line))
        self.ui.all_connect_btn.released.connect(self.connect_mocap)
        # self.ui.end_btn.released.connect(partial(self.get_start_end, 'end'))
        # build widget

        self.ui.all_slider.setMinimum(0)
        self.ui.all_slider.setMaximum(10)
        self.ui.all_slider.setValue(0)
        self.ui.all_slider.valueChanged.connect(self.all_slider_set)
        self.ui.spine_slider.valueChanged.connect(self.spine_slider_set)
        self.ui.neck_slider.valueChanged.connect(self.neck_slider_set)
        self.ui.l_leg_slider.valueChanged.connect(self.l_leg_slider_set)
        self.ui.r_leg_slider.valueChanged.connect(self.r_leg_slider_set)
        self.ui.l_arm_slider.valueChanged.connect(self.l_arm_slider_set)
        self.ui.r_arm_slider.valueChanged.connect(self.r_arm_slider_set)

        # int and float attrs
        # self.ui.start_line = wdg.QLineEdit(self)
        # self.ui.start_line.setContextMenuPolicy(qt.Qt.ActionsContextMenu)
        # self.ui.start_line.setValidator(gui.QIntValidator())



    def connect_mocap(self):

        start=self.ui.spinBox.value()
        if not start:
            start=0



        ns= self.ui.rig_ns_line.text()
        if not ns:
            ns=':'
        mns=self.ui.mocap_ns_line.text()
        if not mns:
            mns=':'
        # delete any constraints on mocap space nodes in rig
        self.zero_rig(ns=ns, start=start)
        if mc.objExists (ns+'mocap_spcs_GRP'):
            nodes=utils.get_children(ns+'mocap_spcs_GRP', ad=1)
            constraints=mc.ls (nodes, type='constraint')
            if constraints:
                mc.delete (constraints)


        #first make sure that arms and legs are in fk space
        mc.setAttr(ns+'legIKFK_Rt_anim.FK_IK', 0)
        mc.setAttr(ns+'armIKFK_Lt_anim.FK_IK', 0)
        mc.setAttr(ns+'armIKFK_Rt_anim.FK_IK', 0)
        mc.setAttr(ns+'legIKFK_Lt_anim.FK_IK', 0)

        spc_dict = {
            'root_Mid_anim': 'Hips_grp_spc',
            'hips_Mid_anim': 'Spine_grp_spc',
            'chest_Mid_anim': 'Spine1_grp_spc',
            'clavicle_Lt_anim': 'LeftShoulder_grp_spc',
            'clavicle_Rt_anim': 'RightShoulder_grp_spc',
            'shoulder_Rt_anim': 'RightArm_grp_spc',
            'shoulder_Lt_anim': 'LeftArm_grp_spc',
            'elbow_Lt_anim': 'LeftForeArm_grp_spc',
            'elbow_Rt_anim': 'RightForeArm_grp_spc',
            'hand_Lt_anim': 'LeftHand_grp_spc',
            'hand_Rt_anim': 'RightHand_grp_spc',
            'neck01Fk_Mid_anim': 'Neck_grp_spc',
            'head_Mid_anim': 'Head_grp_spc',
            'thigh_Rt_anim': 'RightUpLeg_grp_spc',
            'thigh_Lt_anim': 'LeftUpLeg_grp_spc',
            'knee_Rt_anim': 'RightLeg_grp_spc',
            'knee_Lt_anim': 'LeftLeg_grp_spc',
            'foot_Rt_anim': 'RightFoot_grp_spc',
            'foot_Lt_anim': 'LeftFoot_grp_spc',
            'toe_Lt_anim': 'LeftToeBase_grp_spc',
            'toe_Rt_anim': 'RightToeBase_grp_spc'}


        fbx_top=mns+'Maya_Hips'
        mc.setAttr (fbx_top+'.tx', 0)
        mc.setAttr (fbx_top+'.tz', 0)
        mc.setAttr (fbx_top+'.r', 0 ,0 ,0)
        children=utils.get_children(fbx_top, ad=1)
        for child in children:
            mc.setAttr (child+'.r', 0,0,0)
        fbx_grp = 'optiTrackSkel_offset_GRP'
        if not mc.objExists (fbx_grp):
            fbx_grp=mc.createNode ('transform', n='optiTrackSkel_offset_GRP')
            mc.parent (fbx_top, fbx_grp )
            mc.setAttr (fbx_grp+'.scale', 1.18, 1.18, 1.18)

        keys=list(spc_dict.keys())
        for key in keys:
            ctrl=ns+key
            spc=spc_dict.get(key)
            driver=mns+'Maya_'+spc.replace ('_grp_spc', '')
            driven=ns+'Maya_'+spc.replace ('_grp_spc', '_mocap_spc')
            # mc.pointConstraint (driver, driven, mo=1)
            ori=mc.orientConstraint (driver, driven, mo=1)
            # mc.setAttr (ori[0]+'.interpType' , 2)
        mc.setAttr  (fbx_grp+'.visibility', 0)

    def l_leg_slider_set(self):
        nss=self.ui.rig_ns_line.text()
        ns=nss+':'
        side='Lt'
        s='l'
        val = self.ui.l_leg_slider.value()
        v=float(val*.1)
        legs = [u'toe_'+side+'_anim', u'foot_'+side+'_anim', u'knee_'+side+'_anim', u'thigh_'+side+'_anim']
        for leg in legs:
            mc.setAttr (ns+leg+'.mocap', v)

    def l_arm_slider_set(self):
        nss=self.ui.rig_ns_line.text()
        ns=nss+':'
        side='Lt'
        s = 'l'
        val = self.ui.l_arm_slider.value()
        v=float(val*.1)
        print v
        ctrls = [u'clavicle_'+side+'_anim', u'shoulder_'+side+'_anim', u'elbow_'+side+'_anim', u'hand_'+side+'_anim']
        for ctrl in ctrls:
            mc.setAttr(ns+ctrl + '.mocap', v)

    def r_leg_slider_set(self):
        nss=self.ui.rig_ns_line.text()
        ns=nss+':'
        side='Rt'
        s = 'r'
        val = self.ui.r_leg_slider.value()
        v = float(val * .1)
        legs = [u'toe_' + side + '_anim', u'foot_' + side + '_anim', u'knee_' + side + '_anim',
                u'thigh_' + side + '_anim']
        for leg in legs:
            mc.setAttr(ns+leg + '.mocap', v)

    def r_arm_slider_set(self):
        nss=self.ui.rig_ns_line.text()
        ns=nss+':'
        side='Rt'
        s = 'r'
        val = self.ui.r_arm_slider.value()
        v = float(val * .1)
        print v
        ctrls = [u'clavicle_' + side + '_anim', u'shoulder_' + side + '_anim', u'elbow_' + side + '_anim',
                 u'hand_' + side + '_anim']
        for ctrl in ctrls:
            mc.setAttr(ns+ctrl + '.mocap', v)

    def spine_slider_set(self):
        nss=self.ui.rig_ns_line.text()
        ns=nss+':'
        val = self.ui.spine_slider.value()
        v=float(val*.1)
        ctrls=[u'hips_Mid_anim', u'chest_Mid_anim']
        for ctrl in ctrls:
            mc.setAttr (ns+ctrl+'.mocap', v)

    def neck_slider_set(self):
        nss=self.ui.rig_ns_line.text()
        ns=nss+':'
        val = self.ui.neck_slider.value()
        v=float(val*.1)
        ctrls = [u'neck01Fk_Mid_anim', u'head_Mid_anim']
        for ctrl in ctrls:
            mc.setAttr(ns+ctrl + '.mocap', v)

    def all_slider_set(self):
        nss=self.ui.rig_ns_line.text()
        ns=nss+':'
        all_ctrls=[u'toe_Rt_anim', u'toe_Lt_anim', u'thigh_Rt_anim', u'thigh_Lt_anim',
         u'shoulder_Rt_anim', u'shoulder_Lt_anim', u'root_Mid_anim', u'neck01Fk_Mid_anim',
         u'knee_Rt_anim', u'knee_Lt_anim', u'hips_Mid_anim', u'head_Mid_anim',
         u'hand_Rt_anim', u'hand_Lt_anim', u'foot_Rt_anim', u'foot_Lt_anim',
         u'elbow_Rt_anim', u'elbow_Lt_anim', u'clavicle_Rt_anim', u'clavicle_Lt_anim',
         u'chest_Mid_anim']

        val =  self.ui.all_slider.value()
        print val
        v=float(val*.1)
        print v
        for ctrl in all_ctrls:
            mc.setAttr (ns+ctrl+'.mocap', v)



    def resetDefaultValues(self, nodes=None):
        nodes = mc.ls(sl=1, type='transform')
        print nodes
        for each in nodes:
            attrs = mc.listAttr(each, k=1, v=1, u=1)
            zeros = [u'translateX', u'translateY', u'translateZ', u'rotateX', u'rotateY', u'rotateZ']
            for attr in attrs:
                if attr in zeros:
                    mc.setAttr(each + '.' + attr, 0)
                if attrs == 'scaleX' or attrs == 'scaleY' or attrs == 'scaleZ':
                    mc.setAttr(each + '.' + attr, 1)
                else:
                    dv = mc.attributeQuery(attr, n=each, ld=1)
                    mc.setAttr(each + '.' + attr, dv[0])

    def zero_rig(self, ns=':', start=0):
        zero_frame = start - 10
        mc.currentTime(start, e=1)
        ctrls= (ns+'all_ctrls')
        if not mc.objExists (ctrls):
            ctrls=mc.ls (ns+'*_anim')
        if not ctrls:
            return ('cannot find controls to apply mocap to, please check rig')
        print (ctrls)
        mc.select(ctrls)
        mc.currentTime(zero_frame, e=1)
        self.resetDefaultValues(nodes=ctrls)
        mc.select (cl=1)
        mc.currentTime(start, e=1)

    def import_mocap_fbx(self):

        ff = 'Mocap Capture Files (*.fbx)'
        file_path = utils.file_browser('LOAD', file_filter=ff)
        print file_path
        if not file_path:
            return
        mc.file(file_path[0], i=1)
        print 'importing {0}'.format (file_path[0])
        self.ui.path_line.setText(file_path[0])


    def get_selected_ns(self, line_edit_item):

        sel = mc.ls(sl=1)
        if not sel:
            mc.warning('Nothing selected!')
            return
        ns=utils.get_namespace(sel[0])
        line_edit_item.setText(ns)


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

