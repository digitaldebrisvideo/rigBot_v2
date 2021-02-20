import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import spline
from rigBot import rivet


def make_fkikSwitch_connection_attrs(partpre=None, side='Lt', source_ctrl=None, tag_name='switch', snapTo=None,
                                     add_attrs=None):
    """Adds and connects attributes from default encore FKIK switch anim setup to rig nodes in scene
        Imports default control setup from file or you may specify source_ctrl in args to override

    Keyword Arguments:
        partpre : name to add as prefix for imported control
        source_control {str} -- [provide this argument to override importing the default encore switch control ] (default: {None})
        tag_name {str} -- [used to determine fk and ik visibility connections] (default: {'switch'})
        snapTo: node to move control parent to
        add_attrs {[type]} -- [any additional attributes you would like to add to this node ] (default: {None}
                                        Example: ['bendy', 'shapers', 'ikoffsets'])
    """

    switch_anim = ''
    if source_ctrl is not None:
        switch_anim = source_ctrl

    partpre = partpre
    if partpre == '':
        partpre = 'mypart_'

    if source_ctrl is None:
        # filepath = r'C:/Users/Nicob/Documents/maya/scripts/rigBot/rigBot/config/switcher_anim.mb'
        system_base_path = os.path.dirname(utils.__file__)
        base_path = os.path.join(system_base_path, 'config')
        file_path = os.path.join(base_path, 'switcher_anim.mb')
        newnodes = mc.file(filepath, i=1, ignoreVersion=1, rnn=1, mergeNamespacesOnClash=0, rpr=partpre, ra=1,
                           options="v=0;", pr=1)

        switch_anim = partpre + '_CTL'

    # pos switcher grpOffset node if snapTo

    if snapTo is not None:
        utils.snap_to_transform(snapTo, switch_anim.replace('CTL', 'grpOffset'))
        mc.setAttr(switch_anim.replace('CTL', 'grpOffset') + '.r', 0, 0, 0)

    # get value of tags and sort into ik and fk vis groups

    iks = []
    fks = []
    nodes = mc.ls('*.' + tag_name)

    for node in nodes:
        if partpre in node and side in node:
            mode = mc.getAttr(node)
            if mode:
                mode = mode.lower()
                if 'ik' in mode:
                    iks.append(node.split('.')[0])
                if 'fk' in mode:
                    fks.append(node.split('.')[0])
    for ik in iks:
        # ikparpar=utils.get_parent(ik)
        ikpar = utils.get_parent(ik)
        if ikpar is None:
            mc.connectAttr(switch_anim + '.FK_IK', ik + '.visiblity', f=1)
        else:
            mc.connectAttr(switch_anim + '.FK_IK', ikpar + '.visibility', f=1)
    rvn = mc.createNode('reverse', name=switch_anim + '_fkik_vis_rv')
    mc.connectAttr(switch_anim + '.FK_IK', rvn + '.inputX')
    for fk in fks:
        fkpar = utils.get_parent(fk)
        if fkpar:
            mc.connectAttr(rvn + '.outputX', fkpar + '.visibility', f=1)
    if add_attrs is not None:
        for att in add_attrs:
            mc.addAttr(switch_anim, ln=att, min=0, max=1, dv=0, k=1)

    nns = []

    for nn in reversed(newnodes):
        nnn = ''
        sn = nn.split("|")
        nnn = mc.rename(nn, sn[-1])
        nns.append(nnn)

    anim = mc.ls(partpre + '_CTL')

    # if mc.objExists (partpre+'_skeleton_grp'):
    #     mc.parent (anim, partpre+'_skeleton_grp' )
    return anim

def tag_match_function(ctrl, tag):
    if mc.objExists(ctrl+'.matchFunction'):
        mc.deleteAttr(ctrl+'.matchFunction')

    mc.addAttr(ctrl, ln='matchFunction', dt='string', h=1)
    mc.setAttr(ctrl+'.matchFunction', tag.lower(), type='string')

def create_snapto_node(ctrl, jnt):
    """This will be used for FK IK matching"""

    snapto = ctrl+'_SNAPTO'
    if mc.objExists(snapto):
        jnt = utils.get_parent(snapto)
        mc.delete(snapto)

    snapto_grp = mc.duplicate(ctrl, po=1, n=ctrl+'_SNAPTO_GRP')[0]
    snapto = mc.duplicate(ctrl, po=1, n=ctrl+'_SNAPTO')[0]
    utils.set_attrs([snapto_grp, snapto], k=1, l=0)
    mc.parent(snapto_grp, jnt)
    mc.parent(snapto, snapto_grp)

    ua = mc.listAttr(snapto, ud=1)

    for a in ua:
        try:
            mc.setAttr(snapto+'.'+a, l=0)
            mc.deleteAttr(snapto+'.'+a)

            mc.setAttr(snapto_grp+'.'+a, l=0)
            mc.deleteAttr(snapto_grp+'.'+a)

        except:
            pass

    return snapto

def create_fk_ik_switch(switch_ctrl, ik_handles, fk_ctrls, ik_ctrls, vis_ctrl=None, switch_attr_name='IK', vis_attr_name='fkIkCtrlVis'):
    """Create an IK attribute on the given ctrl, connect IK handles to ik switch.
        Also connect fk ctrls and ik ctrls visibility to switch.

        This will create an 'IK' attr on the switch ctrl
        will create a 'fkIkCtrlVis' on the switch ctrl as an enum to display 'auto:fkOnly:ikOnly:both'

        Kwargs:
            :switch_ctrl: ctrl to add IK switch
            :vis_ctrl: ctrl to add visibility attribute
            :switch_attr_name: name of switch attribute
            :vis_attr_name: name of visibility attribute
            :ik_handles: ik handles to connect to switch
            :fk_ctrls: FK ctrls to connect to visibility attr
            :ik_ctrls: IK ctrls to connect to visibility attr
        """

    fk_ctrls = mc.ls(fk_ctrls)
    ik_ctrls = mc.ls(ik_ctrls)
    ik_handles = mc.ls(ik_handles)

    if not vis_ctrl:
        vis_ctrl = switch_ctrl

    # Create attributes
    if not mc.objExists(switch_ctrl+'.'+switch_attr_name):
        mc.addAttr(switch_ctrl, ln=switch_attr_name, min=0, max=1, k=1)

    if not mc.objExists(vis_ctrl+'.'+vis_attr_name):
        mc.addAttr(vis_ctrl, ln=vis_attr_name, at='enum', en='auto:fkOnly:ikOnly:both', k=1)

    # Connect ik handles
    for handle in ik_handles:
        mc.connectAttr(switch_ctrl+'.'+switch_attr_name, handle+'.ikBlend')

    # Create swicth for ik ctrl
    ik_choice = utils.create_node('choice', n=vis_attr_name+'_ik_choice')
    mc.connectAttr(vis_ctrl+'.'+vis_attr_name, ik_choice+'.selector')
    mc.connectAttr(switch_ctrl+'.'+switch_attr_name, ik_choice+'.input[0]')
    mc.setAttr(ik_choice+'.input[1]', 0)
    mc.setAttr(ik_choice+'.input[2]', 1)
    mc.setAttr(ik_choice+'.input[3]', 1)

    for ctrl in ik_ctrls:
        mc.setAttr(ctrl+'.v', l=0)
        mc.connectAttr(ik_choice+'.output', ctrl+'.v', f=1)
        mc.setAttr(ctrl+'.v', l=1)

    # Create swicth for ik ctrl
    fk_choice = utils.create_node('choice', n=vis_attr_name+'_fk_choice')
    fk_rv = utils.create_node('reverse', n=vis_attr_name+'_fk_choice')
    mc.connectAttr(switch_ctrl+'.'+switch_attr_name, fk_rv+'.inputX')
    mc.connectAttr(vis_ctrl+'.'+vis_attr_name, fk_choice+'.selector')
    mc.connectAttr(fk_rv+'.outputX', fk_choice+'.input[0]')
    mc.setAttr(fk_choice+'.input[1]', 1)
    mc.setAttr(fk_choice+'.input[2]', 0)
    mc.setAttr(fk_choice+'.input[3]', 1)

    for ctrl in fk_ctrls:
        mc.setAttr(ctrl+'.v', l=0)
        mc.connectAttr(fk_choice+'.output', ctrl+'.v', f=1)
        mc.setAttr(ctrl+'.v', l=1)

    return True

def create_soft_ik(ik_ctrl, ik_joints, ik_handle):
    """Create soft ik constraint on ikHandle.

        Args:
            :ik_ctrl: (str) Ik control name.
            :ik_joints: (list) List of ik joints
            :ik_handle: (str) Ik handle."""

    # get name and constant variables
    name = ik_handle+'Soft'
    parent = utils.get_parent(ik_joints[0])
    ik_handle_parent = utils.get_parent(ik_handle)

    # get total length of joint chain
    chain_length = 0
    for jnt in ik_joints[1:]:
        chain_length += abs(mc.getAttr(jnt+'.tx'))

    mc.addAttr(ik_joints[0], ln='softIkChainLength', k=1, dv=chain_length)

    #create dist node, (distance between top ik_joint and ik_handle) = X
    soft_ik_root = utils.snap_locator(ik_joints[0], node_type='transform')
    soft_ik_root = mc.rename(soft_ik_root, name+'_root_'+utils.get_suffix('transform'))

    dist = utils.create_distance_reader(soft_ik_root, ik_handle_parent)

    #create the dSoft and softIK attributes on the controller
    mc.addAttr(ik_ctrl, ln='softIK', min=0, k=1)
    ctrl_clamp = mc.createNode('clamp')
    mc.connectAttr(ik_ctrl+'.softIK', ctrl_clamp+'.inputR')
    mc.setAttr(ctrl_clamp+'.minR', 0.0001)
    mc.setAttr(ctrl_clamp+'.maxR', 10000000)

    #create node network for soft IK
    da_pma = mc.createNode('plusMinusAverage', n=name+'_da_pma')
    x_minus_da_pma = mc.createNode('plusMinusAverage', n=name+'_x_minus_da_pma')
    negate_x_minus_md = mc.createNode('multiplyDivide', n=name+'_negate_x_minus_md')
    divBy_dSoft_md = mc.createNode('multiplyDivide', n=name+'_divBy_dSoft_md')
    pow_e_md = mc.createNode('multiplyDivide', n=name+'_pow_e_md')
    one_minus_pow_e_pma = mc.createNode('plusMinusAverage', n=name+'_one_minus_pow_e_pma')
    times_dSoft_md = mc.createNode('multiplyDivide', n=name+'_times_dSoft_md')
    plus_da_pma = mc.createNode('plusMinusAverage', n=name+'_plus_da_pma')
    da_cond = mc.createNode('condition', n=name+'_da_cond')
    dist_diff_pma = mc.createNode('plusMinusAverage', n=name+'_dist_diff_pma')
    defaultPos_pma = mc.createNode('plusMinusAverage', n=name+'_defaultPos_pma')

    #set operations
    mc.setAttr(da_pma+'.operation', 2)
    mc.setAttr(x_minus_da_pma+'.operation', 2)
    mc.setAttr(negate_x_minus_md+'.operation', 1)
    mc.setAttr(divBy_dSoft_md+'.operation', 2)
    mc.setAttr(pow_e_md+'.operation', 3)
    mc.setAttr(one_minus_pow_e_pma+'.operation', 2)
    mc.setAttr(times_dSoft_md+'.operation', 1)
    mc.setAttr(plus_da_pma+'.operation', 1)
    mc.setAttr(da_cond+'.operation', 5)
    mc.setAttr(dist_diff_pma+'.operation', 2)
    mc.setAttr(defaultPos_pma+'.operation', 2)

    #make connections
    mc.connectAttr(ik_joints[0]+'.softIkChainLength', da_pma+'.input1D[0]')
    mc.connectAttr(ctrl_clamp+'.outputR', da_pma+'.input1D[1]')

    mc.connectAttr(dist+'.localDistance', x_minus_da_pma+'.input1D[0]')
    mc.connectAttr(da_pma+'.output1D', x_minus_da_pma+'.input1D[1]')

    mc.connectAttr(x_minus_da_pma+'.output1D', negate_x_minus_md+'.input1X')
    mc.setAttr(negate_x_minus_md+'.input2X', -1)

    mc.connectAttr(negate_x_minus_md+'.outputX', divBy_dSoft_md+'.input1X')
    mc.connectAttr(ctrl_clamp+'.outputR', divBy_dSoft_md+'.input2X')

    mc.setAttr(pow_e_md+'.input1X', 2.718281828)
    mc.connectAttr(divBy_dSoft_md+'.outputX', pow_e_md+'.input2X')

    mc.setAttr(one_minus_pow_e_pma+'.input1D[0]', 1)
    mc.connectAttr(pow_e_md+'.outputX' , one_minus_pow_e_pma+'.input1D[1]')

    mc.connectAttr(one_minus_pow_e_pma+'.output1D', times_dSoft_md+'.input1X')
    mc.connectAttr(ctrl_clamp+'.outputR', times_dSoft_md+'.input2X')

    mc.connectAttr(times_dSoft_md+'.outputX', plus_da_pma+'.input1D[0]')
    mc.connectAttr(da_pma+'.output1D', plus_da_pma+'.input1D[1]')

    mc.connectAttr(da_pma+'.output1D', da_cond+'.firstTerm')
    mc.connectAttr(dist+'.localDistance', da_cond+'.secondTerm')
    mc.connectAttr(dist+'.localDistance', da_cond+'.colorIfFalseR')
    mc.connectAttr(plus_da_pma+'.output1D', da_cond+'.colorIfTrueR')

    mc.connectAttr(da_cond+'.outColorR', dist_diff_pma+'.input1D[0]')
    mc.connectAttr(dist+'.localDistance', dist_diff_pma+'.input1D[1]')

    mc.setAttr(defaultPos_pma+'.input1D[0]', 0)
    mc.connectAttr(dist_diff_pma+'.output1D', defaultPos_pma+'.input1D[1]')

    # Create new ik aim node
    up = [1,0,0]
    aim = [0,1,0]

    grp = mc.createNode('transform', n=name+'_soft_aim_'+utils.get_suffix('transform'), p=ik_handle_parent)
    gAim = mc.createNode('transform', n=name+'_soft_'+utils.get_suffix('transform'), p=grp)

    mc.aimConstraint(soft_ik_root,
                     grp,
                     aim=aim,
                     u=up,
                     wu=up,
                     wut='objectRotation',
                     wuo=ik_ctrl,
                     n=grp+'_ac')

    mc.connectAttr(defaultPos_pma+'.output1D', gAim+'.ty')
    mc.pointConstraint(gAim, ik_handle)
    mc.parent(ik_handle, gAim)

    # parent stuff
    if parent:
        mc.parent(soft_ik_root, parent)

    return gAim

def upper_twist(shoulder_jnt, up_arm_ik_jnt, lo_arm_ik_jnt, up_arm_jnt, lo_arm_jnt, up_arm_twist_jnts):
    """Quaterion / matrix based twist for upper arms and legs.

        Args:
            :shoulder_jnt: (str) shoulder / Hip joint
            :up_arm_ik_jnt: (str) Upper driving IK joint
            :lo_arm_ik_jnt: (str) Lower driving IK joint
            :up_arm_jnt: (str) Upper blend joint
            :lo_arm_jnt: (str) Lower blend joint
            :up_arm_twist_jnts: (list) List of twist joints."""

    # Create a group that does not rotate and parent under the ik arm parent (shoulder)
    stable_reader_grp = utils.create_node('transform', n=up_arm_ik_jnt+'_stable_reader', p=up_arm_ik_jnt)

    # Create a grp that will rotate with ik arm
    twist_reader_grp = utils.create_node('transform', n=up_arm_ik_jnt+'_twist_reader', p=up_arm_ik_jnt)
    twist_driver_grp = utils.create_node('transform', n=up_arm_ik_jnt+'_twist', p=twist_reader_grp)

    mc.parent(stable_reader_grp, shoulder_jnt)
    mc.addAttr(twist_reader_grp, ln='twist', k=1)

    # Now set up mult matrix and decomp nodes to extract the twist between the two nodes
    mult_mtx = mc.createNode('multMatrix')

    decomp_mtx = mc.createNode('decomposeMatrix')
    quat_to_euler = mc.createNode('quatToEuler')

    mc.connectAttr(stable_reader_grp+'.worldInverseMatrix', mult_mtx+'.matrixIn[1]')
    mc.connectAttr(twist_reader_grp+'.worldMatrix', mult_mtx+'.matrixIn[0]')
    mc.connectAttr(mult_mtx+'.matrixSum', decomp_mtx+'.inputMatrix')
    mc.connectAttr(decomp_mtx+'.outputQuatX', quat_to_euler+'.inputQuatX')
    mc.connectAttr(decomp_mtx+'.outputQuatW', quat_to_euler+'.inputQuatW')

    utils.connect_negative(quat_to_euler+'.outputRotateX', twist_reader_grp+'.twist')
    mc.connectAttr(twist_reader_grp+'.twist', twist_driver_grp+'.rx')

    # Connect joints
    mc.parentConstraint(twist_driver_grp, up_arm_jnt, mo=1)
    mc.parentConstraint(lo_arm_ik_jnt, lo_arm_jnt, mo=1)

    div = 1.0 / (len(up_arm_twist_jnts))

    mdl = mc.createNode('multDoubleLinear')
    mc.setAttr(mdl+'.input1', div)
    mc.connectAttr(quat_to_euler+'.outputRotateX', mdl+'.input2')

    for i, joint in enumerate(up_arm_twist_jnts[:-1]):
        mc.connectAttr(mdl+'.output', joint+'.rx')

    mc.orientConstraint(up_arm_ik_jnt, up_arm_twist_jnts[-1], mo=1)

def lower_twist(lo_arm_ik_jnt, wrist_ik_jnt, lo_arm_jnt, lo_arm_twist_jnts, wrist_jnt=None):
    """Quaterion / matrix based stretch for forearms and lower legs

        Args:
            :lo_arm_ik_jnt: (str) Lower driving IK joint
            :wrist_ik_jnt: (str) Wrist / leg end driving IK joint
            :lo_arm_jnt: (str) Lower Blend joint
            :lo_arm_twist_jnts: (list) List of twist joints.

        Kwargs:
            :wrist_jnt: (str) wrist / leg end Blend joint. Defaults to None."""

    # Create a group that does not rotate and parent under the ik arm parent (shoulder)
    stable_reader_grp = utils.create_node('transform', n=lo_arm_ik_jnt+'_stable_reader', p=lo_arm_ik_jnt)

    # Create a grp that will rotate with ik arm
    twist_reader_grp = utils.create_node('transform', n=lo_arm_ik_jnt+'_twist_reader', p=lo_arm_ik_jnt)
    mc.addAttr(twist_reader_grp, ln='twist', k=1)

    mc.delete(mc.pointConstraint(wrist_ik_jnt, twist_reader_grp))
    mc.parent(twist_reader_grp, wrist_ik_jnt)

    # Now set up mult matrix and decomp nodes to extract the twist between the two nodes
    mult_mtx = mc.createNode('multMatrix')
    decomp_mtx = mc.createNode('decomposeMatrix')
    quat_to_euler = mc.createNode('quatToEuler')

    mc.connectAttr(stable_reader_grp+'.worldInverseMatrix', mult_mtx+'.matrixIn[1]')
    mc.connectAttr(twist_reader_grp+'.worldMatrix', mult_mtx+'.matrixIn[0]')
    mc.connectAttr(mult_mtx+'.matrixSum', decomp_mtx+'.inputMatrix')
    mc.connectAttr(decomp_mtx+'.outputQuatX', quat_to_euler+'.inputQuatX')
    mc.connectAttr(decomp_mtx+'.outputQuatW', quat_to_euler+'.inputQuatW')

    utils.connect_negative(quat_to_euler+'.outputRotateX', twist_reader_grp+'.twist')

    # Connect joints
    mc.parentConstraint(lo_arm_ik_jnt, lo_arm_jnt, mo=1)
    if wrist_jnt:
        mc.parentConstraint(wrist_ik_jnt, wrist_jnt, mo=1)

    div = 1.0 / (len(lo_arm_twist_jnts))

    mdl = mc.createNode('multDoubleLinear')
    mc.setAttr(mdl+'.input1', div)
    mc.connectAttr(quat_to_euler+'.outputRotateX', mdl+'.input2')

    for i, joint in enumerate(lo_arm_twist_jnts):
        mc.connectAttr(mdl+'.output', joint+'.rx')

def biped_stretch(ik_ctrl,
                  ik_last_node,
                  pv_ctrl,
                  switch_ctrl,
                  up_arm_fk_ctrl,
                  lo_arm_fk_ctrl,
                  wrist_fk_ctrl,
                  up_arm_ik_jnt,
                  lo_arm_ik_jnt,
                  wrist_ik_jnt,
                  ik_handle,
                  pin_attr_name='pinElbow',
                  shift_attr_name='shiftElbow'):
    """Stretch setup for biped (2 joint chain) arms and legs"""

    # add all my attrs on ctrls
    mc.addAttr(ik_ctrl, ln=pin_attr_name,  at='double', min=0, max=1, k=1)
    mc.addAttr(ik_ctrl, ln=shift_attr_name,  at='double', min=-1, max=1, k=1)

    mc.addAttr(ik_ctrl, ln='autoStretch',  at='double', min=0, max=1, k=1)
    mc.addAttr(ik_ctrl, ln='upStretch', at='double', dv=1, min=0.001, k=1)
    mc.addAttr(ik_ctrl, ln='loStretch', at='double', dv=1, min=0.001, k=1)

    mc.addAttr(up_arm_fk_ctrl, ln='stretch', at='double', dv=1, min=0.001, k=1)
    mc.addAttr(lo_arm_fk_ctrl, ln='stretch', at='double', dv=1, min=0.001, k=1)

    # store initial length of joint
    lo_init_length = mc.getAttr(lo_arm_ik_jnt+'.tx')
    wrist_init_length = mc.getAttr(wrist_ik_jnt+'.tx')
    max_init_length = mc.getAttr(lo_arm_ik_jnt+'.tx')+mc.getAttr(wrist_ik_jnt+'.tx')

    lo_abs_init_length = abs(mc.getAttr(lo_arm_ik_jnt+'.tx'))
    wrist_abs_length = abs(mc.getAttr(wrist_ik_jnt+'.tx'))

    # Get parents for ik handle and root of the parm
    arm_root_grp = utils.get_parent(up_arm_ik_jnt)

    # Create distance nodes between base, end, and pv ctrl to get the length of side of the triangle
    root_to_end_dist = utils.create_distance_reader(arm_root_grp, ik_last_node)
    root_to_pv_dist = utils.create_distance_reader(arm_root_grp, pv_ctrl)
    pv_to_end_dist = utils.create_distance_reader(pv_ctrl, ik_last_node)

    # easy stuff first - create fk stretch nodes
    lo_arm_fk_mdl = mc.createNode('multDoubleLinear')
    wrist_fk_mdl = mc.createNode('multDoubleLinear')

    mc.setAttr(lo_arm_fk_mdl+'.input1', mc.getAttr(lo_arm_ik_jnt+'.tx'))
    mc.setAttr(wrist_fk_mdl+'.input1', mc.getAttr(wrist_ik_jnt+'.tx'))
    mc.connectAttr(up_arm_fk_ctrl+'.stretch', lo_arm_fk_mdl+'.input2')
    mc.connectAttr(lo_arm_fk_ctrl+'.stretch', wrist_fk_mdl+'.input2')

    utils.connect_abs(lo_arm_fk_mdl+'.output', lo_arm_fk_ctrl+'_ZERO.tx')
    if wrist_fk_ctrl and mc.objExists(wrist_fk_ctrl):
        utils.connect_abs(wrist_fk_mdl+'.output', wrist_fk_ctrl+'_ZERO.tx')

    # These arethe final fk stretch outputs to connect to joints
    fk_stretch_final_output = [lo_arm_fk_mdl+'.output',  wrist_fk_mdl+'.output']

    # NOW creates node s for thew elbow pin
    lo_arm_pin_mdl = mc.createNode('multDoubleLinear')
    wrist_pin_mdl = mc.createNode('multDoubleLinear')

    mc.setAttr(lo_arm_pin_mdl+'.input1', 1)
    mc.setAttr(wrist_pin_mdl+'.input1', 1)

    if lo_init_length < 0.0:
        mc.setAttr(lo_arm_pin_mdl+'.input1', -1)

    if wrist_init_length < 0.0:
        mc.setAttr(wrist_pin_mdl+'.input1', -1)

    mc.connectAttr(root_to_pv_dist+'.localDistance', lo_arm_pin_mdl+'.input2')
    mc.connectAttr(pv_to_end_dist+'.localDistance', wrist_pin_mdl+'.input2')

    # These arethe final elbow pin stretch outputs to connect to joints
    pin_final_output = [lo_arm_pin_mdl+'.output', wrist_pin_mdl+'.output']

    # create shift nodes
    mc.addAttr(lo_arm_ik_jnt, ln='shiftLength', k=1)
    mc.addAttr(wrist_ik_jnt, ln='shiftLength', k=1)

    tt = 'linear'
    mc.setDrivenKeyframe(lo_arm_ik_jnt+'.shiftLength', cd=ik_ctrl+'.'+shift_attr_name, dv=0, v=lo_init_length, itt=tt, ott=tt)
    mc.setDrivenKeyframe(lo_arm_ik_jnt+'.shiftLength', cd=ik_ctrl+'.'+shift_attr_name, dv=1, v=0, itt=tt, ott=tt)
    mc.setDrivenKeyframe(lo_arm_ik_jnt+'.shiftLength', cd=ik_ctrl+'.'+shift_attr_name, dv=-1, v=max_init_length, itt=tt, ott=tt)

    mc.setDrivenKeyframe(wrist_ik_jnt+'.shiftLength', cd=ik_ctrl+'.'+shift_attr_name, dv=0, v=wrist_init_length, itt=tt, ott=tt)
    mc.setDrivenKeyframe(wrist_ik_jnt+'.shiftLength', cd=ik_ctrl+'.'+shift_attr_name, dv=1, v=max_init_length, itt=tt, ott=tt)
    mc.setDrivenKeyframe(wrist_ik_jnt+'.shiftLength', cd=ik_ctrl+'.'+shift_attr_name, dv=-1, v=0, itt=tt, ott=tt)

    shift_final_output = [ lo_arm_ik_jnt+'.shiftLength', wrist_ik_jnt+'.shiftLength']

    # Create ik indivisual stretch nodes
    lo_arm_ik_scale_mdl = mc.createNode('multDoubleLinear')
    wrist_ik_scale_mdl = mc.createNode('multDoubleLinear')

    mc.connectAttr(shift_final_output[0], lo_arm_ik_scale_mdl+'.input1')
    mc.connectAttr(shift_final_output[1], wrist_ik_scale_mdl+'.input1')
    mc.connectAttr(ik_ctrl+'.upStretch', lo_arm_ik_scale_mdl+'.input2')
    mc.connectAttr(ik_ctrl+'.loStretch', wrist_ik_scale_mdl+'.input2')

    # This is the final output for scale and shift
    ik_stretch_final_output = [lo_arm_ik_scale_mdl+'.output', wrist_ik_scale_mdl+'.output']

    # Now create the IK auto stretch nodes
    lo_auto_stretch_mdl = mc.createNode('multDoubleLinear')
    wrist_auto_stretch_mdl = mc.createNode('multDoubleLinear')

    auto_stretch_clamp = mc.createNode('clamp')
    mc.setAttr(auto_stretch_clamp+'.minR', 1)
    mc.setAttr(auto_stretch_clamp+'.maxR', 10000000)

    mc.connectAttr(ik_stretch_final_output[0], lo_auto_stretch_mdl+'.input1', f=1)
    mc.connectAttr(ik_stretch_final_output[1], wrist_auto_stretch_mdl+'.input1', f=1)
    mc.connectAttr(root_to_end_dist+'.stretchFactor', auto_stretch_clamp+'.inputR')

    mc.connectAttr(auto_stretch_clamp+'.outputR', lo_auto_stretch_mdl+'.input2', f=1)
    mc.connectAttr(auto_stretch_clamp+'.outputR', wrist_auto_stretch_mdl+'.input2', f=1)

    adl = mc.createNode('addDoubleLinear')
    mc.connectAttr(lo_arm_ik_scale_mdl+'.output', adl+'.input1')
    mc.connectAttr(wrist_ik_scale_mdl+'.output', adl+'.input2')
    utils.connect_abs(adl+'.output', root_to_end_dist+'.jointChainLength')

    # handle soft ik handle constraint override
    pc = mc.pointConstraint(ik_last_node, ik_handle)[0]
    if mc.objExists(up_arm_ik_jnt+'.softIkChainLength'):

        # compensate feed in new chain length for soft ik chain length
        utils.connect_abs(adl+'.output', up_arm_ik_jnt+'.softIkChainLength')

        # blend off the soft ik constraint IF im in auto s tretch or pin mode
        mdl = mc.createNode('multDoubleLinear')
        utils.connect_reverse(ik_ctrl+'.'+pin_attr_name, mdl+'.input1')
        utils.connect_reverse(ik_ctrl+'.autoStretch', mdl+'.input2')
        mc.connectAttr(mdl+'.output', pc+'.w0')
        utils.connect_reverse(pc+'.w0', pc+'.w1')

    ik_auto_stretch_final_output = [lo_auto_stretch_mdl+'.output', wrist_auto_stretch_mdl+'.output']

    # now create all my blends

    # first blend btween FK and an empty ik input
    #   (this ikl input will take another blend node for blending oall the IK options )
    fk_to_ik_blend = mc.createNode('blendColors')

    mc.connectAttr(switch_ctrl+'.IK', fk_to_ik_blend+'.blender')
    mc.connectAttr(fk_stretch_final_output[0], fk_to_ik_blend+'.color2R')
    mc.connectAttr(fk_stretch_final_output[1], fk_to_ik_blend+'.color2G')

    # now create a blender between pin elbow  and the rest of the ik options
    auto_ik_blend = mc.createNode('blendColors')

    mc.connectAttr(ik_ctrl+'.autoStretch', auto_ik_blend+'.blender')
    mc.connectAttr(ik_auto_stretch_final_output[0], auto_ik_blend+'.color1R')
    mc.connectAttr(ik_auto_stretch_final_output[1], auto_ik_blend+'.color1G')

    # Now connect it toth fk blend
    mc.connectAttr(auto_ik_blend+'.outputR', fk_to_ik_blend+'.color1R')
    mc.connectAttr(auto_ik_blend+'.outputG', fk_to_ik_blend+'.color1G')

    # now create a blender between pin elbow  and the rest of the ik options
    pin_ik_blend = mc.createNode('blendColors')

    mc.connectAttr(ik_ctrl+'.'+pin_attr_name, pin_ik_blend+'.blender')
    mc.connectAttr(pin_final_output[0], pin_ik_blend+'.color1R')
    mc.connectAttr(pin_final_output[1], pin_ik_blend+'.color1G')

    # Now connect it toth fk blend
    mc.connectAttr(pin_ik_blend+'.outputR', auto_ik_blend+'.color2R')
    mc.connectAttr(pin_ik_blend+'.outputG', auto_ik_blend+'.color2G')

    # now connect the shift and scale
    mc.connectAttr(ik_stretch_final_output[0], pin_ik_blend+'.color2R')
    mc.connectAttr(ik_stretch_final_output[1], pin_ik_blend+'.color2G')

    # now for the magic! Connect the blend networll to joints
    mc.connectAttr(fk_to_ik_blend+'.outputR', lo_arm_ik_jnt+'.tx')
    mc.connectAttr(fk_to_ik_blend+'.outputG', wrist_ik_jnt+'.tx')


def multi_joint_stretch(ik_ctrl, ik_last_node, switch_ctrl, fk_ctrls, jnts, ik_handle):
    """Create IK FK Streatch for limbs with more than two bines"""

    root_grp = utils.get_parent(jnts[0])
    stretch_jnts = jnts[1:]
    stretch_fk_ctrls = fk_ctrls[1:]

    # create attrs
    attrs = ['upStretch','loStretch']
    for i in reversed(range(len(stretch_jnts)-2)):
        ltr = ''
        if i > 0:
            ltr = utils.letters[i]

        attrs.insert(1, 'midStretch'+ltr)

    if not mc.objExists(ik_ctrl+'.autoStretch'):
        mc.addAttr(ik_ctrl, ln='autoStretch',  at='double', min=0, max=1, k=1)

    for i in range(len(stretch_jnts)):
        if not mc.objExists(ik_ctrl+'.'+attrs[i]):
            mc.addAttr(ik_ctrl, ln=attrs[i], at='double', dv=1, min=0.001, k=1)

    for fk_ctrl in fk_ctrls[:-1]:
        if not mc.objExists(fk_ctrl+'.stretch'):
            mc.addAttr(fk_ctrl, ln='stretch', at='double', dv=1, min=0.001, k=1)

    # store initial length of joint
    init_lengths = [mc.getAttr(j+'.tx') for j in stretch_jnts]
    abs_init_lengths = [abs(v) for v in init_lengths]

    total_init_length = 0
    for v in init_lengths:
        total_init_length += v

    abs_total_init_length = abs(total_init_length)

    # Create dist reader
    root_to_end_dist = utils.create_distance_reader(root_grp, ik_last_node)

    auto_stretch_clamp = mc.createNode('clamp')
    mc.setAttr(auto_stretch_clamp+'.minR', 1)
    mc.setAttr(auto_stretch_clamp+'.maxR', 10000000)
    mc.connectAttr(root_to_end_dist+'.stretchFactor', auto_stretch_clamp+'.inputR')

    mc.addAttr(ik_ctrl, ln='stretchFactor', k=0)
    mc.connectAttr(auto_stretch_clamp+'.inputR', ik_ctrl+'.stretchFactor')

    pma = mc.createNode('plusMinusAverage')
    utils.connect_abs(pma+'.output1D', root_to_end_dist+'.jointChainLength')

    # handle soft ik handle constraint override
    pc = mc.pointConstraint(ik_last_node, ik_handle)[0]
    if mc.objExists(jnts[0]+'.softIkChainLength'):

        # compensate chain length - feed in new chain length for soft ik chain length
        utils.connect_abs(pma+'.output1D', jnts[0]+'.softIkChainLength')

        # blend off the soft ik constraint IF im in auto stretch
        mc.connectAttr(ik_ctrl+'.autoStretch', pc+'.w1')
        utils.connect_reverse(pc+'.w1', pc+'.w0')

    # easy stuff first - create fk stretch nodes
    fk_to_ik_blends = [] # This is the final output for IK stretch

    for i, jnt in enumerate(stretch_jnts):

        # easy stuff first - create fk stretch nodes
        fk_mdl = mc.createNode('multDoubleLinear')
        mc.setAttr(fk_mdl+'.input1', mc.getAttr(jnt+'.tx'))
        mc.connectAttr(fk_ctrls[i]+'.stretch', fk_mdl+'.input2')
        utils.connect_abs(fk_mdl+'.output', fk_ctrls[i+1]+'_ZERO.tx')

         # Create user secifed IK stretch
        user_ik_scale_mdl = mc.createNode('multDoubleLinear')
        mc.setAttr( user_ik_scale_mdl+'.input1', init_lengths[i])
        mc.connectAttr(ik_ctrl+'.'+attrs[i], user_ik_scale_mdl+'.input2')

        # Now create the IK auto stretch nodes
        auto_stretch_mdl = mc.createNode('multDoubleLinear')
        mc.connectAttr(user_ik_scale_mdl+'.output', auto_stretch_mdl+'.input1', f=1)
        mc.connectAttr(auto_stretch_clamp+'.outputR', auto_stretch_mdl+'.input2', f=1)
        mc.connectAttr(user_ik_scale_mdl+'.output', '{0}.input1D[{1}]'.format(pma, i))

        fk_to_ik_blend = mc.createNode('blendTwoAttr')
        auto_stretch_blend = mc.createNode('blendTwoAttr')

        mc.connectAttr(switch_ctrl+'.IK', fk_to_ik_blend+'.attributesBlender')
        mc.connectAttr(fk_mdl+'.output', fk_to_ik_blend+'.input[0]')
        mc.connectAttr(auto_stretch_blend+'.output', fk_to_ik_blend+'.input[1]')

        mc.connectAttr(ik_ctrl+'.autoStretch', auto_stretch_blend+'.attributesBlender')
        mc.connectAttr(user_ik_scale_mdl+'.output', auto_stretch_blend+'.input[0]')
        mc.connectAttr(auto_stretch_mdl+'.output', auto_stretch_blend+'.input[1]')

        fk_to_ik_blends.append(fk_to_ik_blend+'.output')

    for i, jnt in enumerate(stretch_jnts):
        mc.connectAttr(fk_to_ik_blends[i], jnt+'.tx')

def stretch_twist_jnts(start_jnt, end_jnt, twist_jnts):
    """Create stratch point constraints on a chain of stretch joints."""

    div = 1.0 / (len(twist_jnts)+1)
    for i, joint in enumerate(twist_jnts):

        weight = div*(i+1)
        mc.pointConstraint(start_jnt, joint, weight=1.0-weight)
        mc.pointConstraint(end_jnt, joint, weight=weight)

def duplicate_chain(chain, search='', replace='', suffix=''):
    """Duplicate a joint chain."""

    if suffix:
        suffix = '_'+suffix

    new_jnts = []
    for joint in chain:
        new_name = joint.replace(search, replace, 1)+suffix
        new_jnt = mc.duplicate(joint, po=1, n=new_name)[0]

        if new_jnts:
            mc.parent(new_jnt, new_jnts[-1])
        new_jnts.append(new_jnt)

    return new_jnts


def biped_bendy(bendy_joints_drivers, bendy_ctrls, make_dynamic=False, noxform_grp='', attr_name='smoothElbow', ctrl_driver=''):

    def create_group_hi(name, match_position):

        grps = []
        for i in range(4):
            ltr = utils.letters[i]
            grp = mc.createNode('transform', n=name+'_'+ltr+'_GRP')
            if grps:
                mc.parent(grp, grps[0])

            grps.append(grp)

        mc.delete(mc.parentConstraint(match_position, grps[0]))
        return grps

    # declare drivers
    drivers = [bendy_joints_drivers[0], bendy_ctrls[0], bendy_ctrls[1], bendy_ctrls[2], bendy_joints_drivers[-1]]

    # create mid pos for pointy elbow
    midA = create_group_hi(drivers[2]+'MidA', match_position=drivers[2])
    midB = create_group_hi(drivers[2]+'MidB', match_position=drivers[2])

    mc.delete(mc.pointConstraint(drivers[1], drivers[2], midA[0]))
    mc.delete(mc.pointConstraint(drivers[2], drivers[3], midB[0]))
    drivers.insert(2, midA[-1])
    drivers.insert(4, midB[-1])

    mc.parent(midA[-1], midA[1])
    mc.delete(midA[2])
    midA = [midA[0], midA[1], midA[-1]]

    mc.parent(midB[-1], midB[1])
    mc.delete(midB[2])
    midB = [midB[0], midB[1], midB[-1]]

    # create spline elbow aim setup
    aim = mc.createNode('transform', p=drivers[3], n=drivers[3]+'MidAim')
    mc.pointConstraint(bendy_ctrls[0], aim, n=aim+'_pc')

    mc.aimConstraint(bendy_ctrls[0], bendy_ctrls[2], aim, n=aim+'_ac', aim=[1,0,0], u=[0,1,0], wut='objectRotation', wu=[0,1,0], wuo=bendy_ctrls[1])

    ori = mc.createNode('transform', p=drivers[3], n=drivers[3]+'MidGrp')
    mc.orientConstraint(aim, ori, n=ori+'_oc')
    mc.parent(midA[0], midB[0], ori)

    # create broken elbow blend
    if not ctrl_driver:
        ctrl_driver = bendy_ctrls[1]

    mc.addAttr(ctrl_driver, ln=''+attr_name, at='double', min=0, max=1, k=1)
    mc.addAttr(ctrl_driver, ln='upTangent', at='double', dv=0, k=1)
    mc.addAttr(ctrl_driver, ln='loTangent', at='double', dv=0, k=1)

    pcA = mc.pointConstraint(midA[0], bendy_ctrls[0], bendy_ctrls[1], midA[1], n=midA[1]+'_pc')[0]
    pcB = mc.pointConstraint(midB[0], bendy_ctrls[2], bendy_ctrls[1], midB[1], n=midB[1]+'_pc')[0]

    mc.connectAttr(ctrl_driver+'.'+attr_name, pcA+'.w0')
    mc.setDrivenKeyframe(pcA+'.w1', cd=ctrl_driver+'.'+attr_name, dv=0, v=1, itt='linear', ott='linear')
    mc.setDrivenKeyframe(pcA+'.w1', cd=ctrl_driver+'.'+attr_name, dv=1, v=0, itt='linear', ott='linear')
    mc.connectAttr(pcA+'.w1', pcA+'.w2')

    mc.connectAttr(ctrl_driver+'.'+attr_name, pcB+'.w0')
    mc.setDrivenKeyframe(pcB+'.w1', cd=ctrl_driver+'.'+attr_name, dv=0, v=1, itt='linear', ott='linear')
    mc.setDrivenKeyframe(pcB+'.w1', cd=ctrl_driver+'.'+attr_name, dv=1, v=0, itt='linear', ott='linear')
    mc.connectAttr(pcB+'.w1', pcB+'.w2')

    # set up tangent attrs
    tyA = utils.get_distance(bendy_ctrls[1], midA[-1])
    if mc.getAttr(midA[0]+'.tx') < 0:
        tyA = -tyA

    tyB = utils.get_distance(bendy_ctrls[1], midB[-1])
    if mc.getAttr(midB[0]+'.tx') < 0:
        tyB = -tyB

    mc.setAttr(midA[0]+'.t', tyA, 0, 0)
    mc.setAttr(midB[0]+'.t', tyB, 0, 0)

    mirror = 1.0
    if bendy_joints_drivers[0].startswith('R_'):
        mirror = -1.0

    mdl = mc.createNode('multDoubleLinear')
    mc.connectAttr(ctrl_driver+'.upTangent', mdl+'.i1')
    mc.connectAttr(ctrl_driver+'.'+attr_name, mdl+'.i2')

    if mirror == 1:
        mc.connectAttr(mdl+'.o', midA[-1]+'.tx')
    else:
        utils.connect_negative(mdl+'.o', midA[-1]+'.tx')

    mdl = mc.createNode('multDoubleLinear')
    mc.connectAttr(ctrl_driver+'.loTangent', mdl+'.i1')
    mc.connectAttr(ctrl_driver+'.'+attr_name, mdl+'.i2')
    if mirror == 1:
        mc.connectAttr(mdl+'.o', midB[-1]+'.tx')
    else:
        utils.connect_negative(mdl+'.o', midB[-1]+'.tx')

    mc.setAttr(midA[1]+'.sx', -1)

    # create surf
    crv = mc.curve(bezier=1, d=3, p=[(0,0,0),(0,0.1666,0),(0,0.3333,0),(0,0.5,0),(0,0.6666,0),(0,0.8333,0),(0,1,0)], k=(0,0,0,1,1,1,2,2,2))
    crv = mc.rename(crv, bendy_joints_drivers[0]+'_crv')

    if mc.objExists(noxform_grp):
        mc.parent(crv, noxform_grp)

    for i in range(len(drivers)):
        mc.xform(crv+'.cv[{0}]'.format(i), ws=1, t=mc.xform(drivers[i], q=1, ws=1, t=1))

    for i in range(len(drivers)):

        point = '{0}.cv[{1}]'.format(crv, i)
        point_attr = point.replace('.cv[', '.controlPoints[')

        dcm = mc.createNode('decomposeMatrix', n=drivers[i]+'_dcmx')
        mc.connectAttr(drivers[i]+'.worldMatrix', dcm+'.inputMatrix')
        mc.connectAttr(dcm+'.outputTranslate', point_attr)
        mc.setAttr(dcm+'.ihi', 0)

    # Duplicate and constrain joints
    get_children = utils.get_children(bendy_joints_drivers[-1])
    bendy_joints_drivers = [mc.rename(j,j.replace('_JNT', '_bend_driver_JNT')) for j in bendy_joints_drivers]
    bendy_joints = duplicate_chain(bendy_joints_drivers, '_bend_driver_JNT', '_JNT')
    mc.parent(get_children, bendy_joints[-1])

    rivet_grp = mc.createNode('transform', p=noxform_grp, n=drivers[0]+'_mpx_GRP')

    for i, joint in enumerate(bendy_joints[:-1]):
        mpx = mc.createNode('transform', n=joint+'_MPX', p=rivet_grp)
        mc.delete(mc.pointConstraint(joint, mpx))
        rivet.motionPath(mpx, crv)

        mc.pointConstraint(mpx, joint)

    for i, joint in enumerate(bendy_joints[:-1]):
        mpx = bendy_joints[i+1]+'_MPX'
        if not mc.objExists(mpx):
            mpx = bendy_joints_drivers[i+1]

        mc.aimConstraint(mpx, joint, aim=[mirror,0,0], u=[0,1,0], wu=[0,1,0], wut='objectRotation', wuo=bendy_joints_drivers[i])

    mc.parentConstraint(bendy_joints_drivers[-1], bendy_joints[-1])

    # Create preseerve volume attrs
    drivers = [j+'_MPX' for j in bendy_joints[:-1]]
    drivers.append(bendy_joints_drivers[-1])
    spline.preserve_volume(drivers, bendy_joints, ctrl_driver, attrs=['sy','sz'])

    utils.break_connections(bendy_joints[-1]+'.s')

    grp = mc.createNode('transform', n=bendy_joints[0]+'_A_GRP', p=utils.get_parent(bendy_joints[0]))
    grp2 = mc.createNode('transform', n=bendy_joints[0]+'_B_GRP', p=grp)
    mc.parent(bendy_joints, grp2)

    mc.hide(bendy_joints_drivers, rivet_grp, crv)


