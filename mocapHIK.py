#Create the new character -- pass in the name hint

from rigBot import utils
from rigBot import env

import maya.cmds as mc
import maya.mel as mm
import os
import re

try:
    import captureMtlAnimation
    import bake
except:
    from rigBot import bake

tPose_ctrls = ['world_CTL',
             'C_cog_CTL',
             'C_chest_CTL',
             'C_head_CTL',
             'L_leg_IK_CTL',
             'R_leg_IK_CTL',
             'L_leg_PV_CTL',
             'R_leg_PV_CTL',
             'L_upLeg_FK_CTL',
             'L_loLeg_FK_CTL',
             'L_legEnd_FK_CTL',
             'R_upLeg_FK_CTL',
             'R_loLeg_FK_CTL',
             'R_legEnd_FK_CTL',
             'L_toe_FK_CTL',
             'L_toe_IK_CTL',
             'R_toe_FK_CTL',
             'R_toe_IK_CTL',
             'L_shoulder_CTL',
             'L_arm_PV_CTL',
             'L_arm_IK_CTL',
             'L_upArm_FK_CTL',
             'L_loArm_FK_CTL',
             'L_wrist_FK_CTL',
             'R_shoulder_CTL',
             'R_arm_PV_CTL',
             'R_arm_IK_CTL',
             'R_upArm_FK_CTL',
             'R_loArm_FK_CTL',
             'R_wrist_FK_CTL']

def create_mocap_hik(hip_joint=None):
    """Generate an hik defenition on for selected MOBU mocap skeletons.

        Note:
            HIK definitions do not work if referenced, So this needs to be run in the anim scene,
            on a rig that has already been refernced or imported into the scene.

        Kwargs:
            :hip_joint: (None, str) Hip joint for selected motion builder mocap skeleton. Defaults to "*_Hips" OR currect selection."""

    # get prefix
    if not hip_joint:
        # look for hip joint
        hip_joint = mc.ls('*_Hips', type='joint')
        if not hip_joint:
            hip_joint = mc.ls(sl=1)

    hip_joint = mc.ls(hip_joint)
    if not hip_joint:
        raise RuntimeError('Cannot find hip joint!')

    prefix = hip_joint[0].split('_')[0]+'_'
    hik_node = hip_joint[0].split('_')[0]

    # Set tPose ~~~~~~~~~~~~~
    joints = hip_joint+utils.get_children(hip_joint, ad=1)
    mc.xform(joints, a=1, ro=[0,0,0])

    # Create root
    root = mc.createNode('transform', n='root')
    mc.parent(hip_joint, root)


    ###########################################3
    # Create character definition

    hik_node = create_character(hik_node)


    ###########################################3
    # Setup character map

    # hips and first spine
    set_joint(root, hik_node, 0)
    set_joint(prefix+'Hips', hik_node, 1)
    set_joint(prefix+'Spine', hik_node, 8)

    # special case for spine:
    primary_spine = prefix+'Spine'
    spines = mc.ls(prefix+'Spine*', type='joint')
    if primary_spine in spines:
        spines.remove(primary_spine)

    i = 23
    for spine in spines:
        set_joint(spine, hik_node, i)
        i += 1

    # special case for necks:
    necks = mc.ls(prefix+'Neck*', type='joint')
    i = 20

    for neck in necks:
        set_joint(neck, hik_node, i)

        if i == 20:
            i = 32
        else:
            i += 1

    # head
    set_joint(prefix+'Head', hik_node, 15)

    # arms
    set_joint(prefix+'LeftShoulder', hik_node, 18)
    set_joint(prefix+'LeftArm', hik_node, 9)
    set_joint(prefix+'LeftForeArm', hik_node, 10)
    set_joint(prefix+'LeftHand', hik_node, 11)

    set_joint(prefix+'RightShoulder', hik_node, 19)
    set_joint(prefix+'RightArm', hik_node, 12)
    set_joint(prefix+'RightForeArm', hik_node, 13)
    set_joint(prefix+'RightHand', hik_node, 14)

    # legs
    set_joint(prefix+'LeftUpLeg', hik_node, 2)
    set_joint(prefix+'LeftLeg', hik_node, 3)
    set_joint(prefix+'LeftFoot', hik_node, 4)
    set_joint(prefix+'LeftToeBase', hik_node, 16)

    set_joint(prefix+'RightUpLeg', hik_node, 5)
    set_joint(prefix+'RightLeg', hik_node, 6)
    set_joint(prefix+'RightFoot', hik_node, 7)
    set_joint(prefix+'RightToeBase', hik_node, 17)

    # L hand
    set_joint(prefix+'LeftHandThumb2', hik_node, 50)
    set_joint(prefix+'LeftHandThumb3', hik_node, 51)
    set_joint(prefix+'LeftHandThumb4', hik_node, 52)

    set_joint(prefix+'LeftHandIndex1', hik_node, 54)
    set_joint(prefix+'LeftHandIndex2', hik_node, 55)
    set_joint(prefix+'LeftHandIndex3', hik_node, 56)
    set_joint(prefix+'LeftHandIndex4', hik_node, 57)

    set_joint(prefix+'LeftHandMiddle1', hik_node, 58)
    set_joint(prefix+'LeftHandMiddle2', hik_node, 59)
    set_joint(prefix+'LeftHandMiddle3', hik_node, 60)
    set_joint(prefix+'LeftHandMiddle4', hik_node, 61)

    set_joint(prefix+'LeftHandRing1', hik_node, 62)
    set_joint(prefix+'LeftHandRing2', hik_node, 63)
    set_joint(prefix+'LeftHandRing3', hik_node, 64)
    set_joint(prefix+'LeftHandRing4', hik_node, 65)

    set_joint(prefix+'LeftHandPinky1', hik_node, 66)
    set_joint(prefix+'LeftHandPinky2', hik_node, 67)
    set_joint(prefix+'LeftHandPinky3', hik_node, 68)
    set_joint(prefix+'LeftHandPinky4', hik_node, 69)

    # R hand
    set_joint(prefix+'RightHandThumb2', hik_node, 74)
    set_joint(prefix+'RightHandThumb3', hik_node, 75)
    set_joint(prefix+'RightHandThumb4', hik_node, 76)

    set_joint(prefix+'RightHandIndex1', hik_node, 78)
    set_joint(prefix+'RightHandIndex2', hik_node, 79)
    set_joint(prefix+'RightHandIndex3', hik_node, 80)
    set_joint(prefix+'RightHandIndex4', hik_node, 81)

    set_joint(prefix+'RightHandMiddle1', hik_node, 82)
    set_joint(prefix+'RightHandMiddle2', hik_node, 83)
    set_joint(prefix+'RightHandMiddle3', hik_node, 84)
    set_joint(prefix+'RightHandMiddle4', hik_node, 85)

    set_joint(prefix+'RightHandRing1', hik_node, 86)
    set_joint(prefix+'RightHandRing2', hik_node, 87)
    set_joint(prefix+'RightHandRing3', hik_node, 88)
    set_joint(prefix+'RightHandRing4', hik_node, 89)

    set_joint(prefix+'RightHandPinky1', hik_node, 90)
    set_joint(prefix+'RightHandPinky2', hik_node, 91)
    set_joint(prefix+'RightHandPinky3', hik_node, 92)
    set_joint(prefix+'RightHandPinky4', hik_node, 93)

    # lock
    lock_character(hik_node)

    print 'Created mocap definiton: '+hik_node
    return hik_node

def create_mocap_blend_rig():
    """Create a duplicate compa skeleton that can drive the anim controls. allows the rig to
        blend off and on from mocap to anim controls only.

        Note:
            This is to be run on the anim rig at build time.
            This only works on bipeds. torso, neck, bipedArm, bipedLeg and foot parts must exist."""


    # grab all zero_nodes:
    zeros = [n.split('.')[0] for n in mc.ls('*.animControlZero')]
    zeros.sort()

    mc_grp_suffix = utils.get_suffix('mocapGroup')
    zero_suffix = utils.get_suffix('animCtrlZero')

    zeros = [n.split('.')[0] for n in mc.ls('*.animControlZero')]
    zeros = [z for z in zeros if z.endswith(zero_suffix)]
    zeros.sort()

    for zero in zeros:
        name = zero.replace(zero_suffix, mc_grp_suffix, 1)
        children = utils.get_children(zero)

        mc_grp = mc.createNode('transform', n=name, p=zero)
        mc.addAttr(mc_grp, ln='mocapGroup', at='message')
        mc.parent(children, mc_grp)
        mc.setAttr(mc_grp+'.v', l=1, k=0)



    asset = env.get_asset() or 'character1'

    # skeel skel ref
    guide_ref = mc.ls('guides_REF')
    world_jnt = mc.ls('C_world_'+utils.get_suffix('joint')+'_REF')

    if world_jnt:
        grp = mc.group(world_jnt, n='skel_REF')
        mc.setAttr(grp+'.it', 0)
        mc.setAttr(grp+'.it', l=1)
        mc.parent(grp, utils.get_parent(guide_ref))
        mc.hide(grp)

    # Connect ctrls to mocap ske
    jnts = ['L_upArm_JNT_MOCAP',
    'R_upArm_JNT_MOCAP',
    'L_loArm_JNT_MOCAP',
    'R_loArm_JNT_MOCAP',
    'L_wrist_JNT_MOCAP',
    'R_wrist_JNT_MOCAP',

    'L_wrist_JNT_MOCAP',
    'R_wrist_JNT_MOCAP',
    'L_upArm_JNT_MOCAP',
    'R_upArm_JNT_MOCAP',

    'L_upLeg_JNT_MOCAP',
    'R_upLeg_JNT_MOCAP',
    'L_loLeg_JNT_MOCAP',
    'R_loLeg_JNT_MOCAP',
    'L_ankle_JNT_MOCAP',
    'R_ankle_JNT_MOCAP',

    'L_ball_JNT_MOCAP',
    'R_ball_JNT_MOCAP',
    'L_ball_JNT_MOCAP',
    'R_ball_JNT_MOCAP',
    'L_ankle_JNT_MOCAP',
    'R_ankle_JNT_MOCAP',
    'L_upLeg_JNT_MOCAP',
    'R_upLeg_JNT_MOCAP',

    'C_hip_JNT_MOCAP',
    'C_chest_JNT_MOCAP',
    'C_head_JNT_MOCAP',
    'L_shoulder_JNT_MOCAP',
    'R_shoulder_JNT_MOCAP']

    # Connect ctrls to mocap ske
    nodes = ['L_upArm_FK_CTL_MOCAP',
    'R_upArm_FK_CTL_MOCAP',
    'L_loArm_FK_CTL_MOCAP',
    'R_loArm_FK_CTL_MOCAP',
    'L_wrist_FK_CTL_MOCAP',
    'R_wrist_FK_CTL_MOCAP',

    'L_arm_IK_CTL_MOCAP',
    'R_arm_IK_CTL_MOCAP',
    'L_arm_PV_CTL_MOCAP',
    'R_arm_PV_CTL_MOCAP',

    'L_upLeg_FK_CTL_MOCAP',
    'R_upLeg_FK_CTL_MOCAP',
    'L_loLeg_FK_CTL_MOCAP',
    'R_loLeg_FK_CTL_MOCAP',
    'L_legEnd_FK_CTL_MOCAP',
    'R_legEnd_FK_CTL_MOCAP',

    'L_toe_FK_CTL_MOCAP',
    'R_toe_FK_CTL_MOCAP',
    'L_toe_IK_CTL_MOCAP',
    'R_toe_IK_CTL_MOCAP',
    'L_leg_IK_CTL_MOCAP',
    'R_leg_IK_CTL_MOCAP',
    'L_leg_PV_CTL_MOCAP',
    'R_leg_PV_CTL_MOCAP',

    'C_cog_CTL_MOCAP',
    'C_chest_CTL_MOCAP',
    'C_head_CTL_MOCAP',
    'L_shoulder_CTL_MOCAP',
    'R_shoulder_CTL_MOCAP']

    mc.addAttr('world_CTL', ln='mocapBlend', min=0, max=1, k=1, dv=1)

    # rename mocap jnts
    ref_jnts = utils.get_children('skel_REF', ad=1)
    for j in ref_jnts:
        mc.rename(j, j.replace('_REF', '_MOCAP'))


    aim = mc.createNode('transform', p='L_upArm_JNT_MOCAP', n='L_upArm_JNT_MOCAP_AIM')
    mc.aimConstraint('L_wrist_JNT_MOCAP', aim, aim=[1,0,0], u=[0,0,-1], wuo='L_loArm_JNT_MOCAP', wut='object')

    aim = mc.createNode('transform', p='R_upArm_JNT_MOCAP', n='R_upArm_JNT_MOCAP_AIM')
    mc.aimConstraint('R_wrist_JNT_MOCAP', aim, aim=[1,0,0], u=[0,0,-1], wuo='R_loArm_JNT_MOCAP', wut='object')

    aim = mc.createNode('transform', p='L_upLeg_JNT_MOCAP', n='L_upLeg_JNT_MOCAP_AIM')
    mc.aimConstraint('L_ankle_JNT_MOCAP', aim, aim=[1,0,0], u=[0,0,-1], wuo='L_loLeg_JNT_MOCAP', wut='object')

    aim = mc.createNode('transform', p='R_upLeg_JNT_MOCAP', n='R_upLeg_JNT_MOCAP_AIM')
    mc.aimConstraint('R_ankle_JNT_MOCAP', aim, aim=[1,0,0], u=[0,0,-1], wuo='R_loLeg_JNT_MOCAP', wut='object')

    # Connectg blend
    for i, node in enumerate(nodes):

        mocap_off_par = mc.duplicate(node, po=1, n=node+'_off_PAR')[0]
        mocap_off = mc.duplicate(node, po=1, n=node+'_off')[0]
        mc.parent(mocap_off, mocap_off_par)

        utils.set_attrs([mocap_off_par, mocap_off], k=1, l=0)

        par = utils.get_parent(node)
        prc = mc.parentConstraint(mocap_off, par, node, mo=1)[0]
        mc.connectAttr('world_CTL.mocapBlend', prc+'.w0')
        utils.connect_reverse('world_CTL.mocapBlend', prc+'.w1')

        if '_PV_' in node:
            mc.parent(mocap_off_par, jnts[i]+'_AIM')
        else:
            mc.parent(mocap_off_par, jnts[i])

        mc.setAttr(prc+'.interpType', 2)

    mc.xform('L_upArm_JNT_MOCAP', ws=1, ro=[0,0,0])
    mc.xform('L_loArm_JNT_MOCAP', ws=1, ro=[0,0,0])
    mc.xform('L_wrist_JNT_MOCAP', ws=1, ro=[0,0,0])

    # legs
    orient = utils.decompose_matrix('L_ankle_JNT_MOCAP')

    loc = utils.snap_locator('L_upLeg_JNT')
    mc.xform(loc, r=1, t=[0,-10,0])
    mc.delete(mc.aimConstraint(loc, 'L_upLeg_JNT_MOCAP', aim=[1,0,0], u=[0,0,-1], wu=[0,0,1], wut='vector'), loc)

    loc = utils.snap_locator('L_loLeg_JNT')
    mc.xform(loc, r=1, t=[0,-10,0])
    mc.delete(mc.aimConstraint(loc, 'L_loLeg_JNT_MOCAP', aim=[1,0,0], u=[0,0,-1], wu=[0,0,1], wut='vector'), loc)

    mc.xform('L_ankle_JNT_MOCAP', ws=1, ro=orient[1])
    loc = utils.snap_locator('L_ankle_JNT_MOCAP')
    mc.parent(loc, 'L_ankle_JNT_MOCAP')
    mc.xform(loc, r=1, t=[1,0,0])
    mc.parent(loc,w=1)

    mc.delete(loc)

    for jnt in jnts:
        if jnt.startswith('R_'):
            l_jnt = jnt.replace('R_','L_', 1)
            mc.xform(jnt, a=1, ro=mc.xform(l_jnt, q=1, a=1, ro=1))

    for jnt in jnts:
        trans = mc.xform(jnt, q=1, a=1, t=1)
        rot = mc.xform(jnt, q=1, a=1, ro=1)
        pose = [trans, rot]
        if not mc.objExists(jnt+'.TPose'):
            mc.addAttr(jnt, ln='TPose', dt='string')

        mc.setAttr(jnt+'.TPose', str(pose), type='string')

    mc.select('L_upLeg_JNT_MOCAP_AIM','R_upLeg_JNT_MOCAP_AIM')
    mm.eval('move -r 0 0 -0.05 ;')

    mc.select('L_upArm_JNT_MOCAP_AIM','R_upArm_JNT_MOCAP_AIM')
    mm.eval('move -r 0 0 0.05 ;')

    switch_ctrls = [
        'L_arm_IK_switch_CTL',
        'R_arm_IK_switch_CTL',
        'L_leg_IK_switch_CTL',
        'R_leg_IK_switch_CTL']

    for c in switch_ctrls:
        mc.setAttr(c+'.IK', 1)

    mc.setAttr('world_CTL.mocapBlend', 0)
    mc.rename('skel_REF', 'skel_MOCAP')

    mc.parentConstraint("L_loLeg_twist_A_JNT_MOCAP","L_leg_PV_CTL_MOCAP_off",mo= True)
    mc.parentConstraint("R_loLeg_twist_A_JNT_MOCAP","R_leg_PV_CTL_MOCAP_off",mo= True)

    print 'Setup mocap blend and biund pose.'

def create_anim_rig_hik(ns=''):
    """Generate an hik defenition on for biped anim rig.

        Note:
            HIK definitions do not work if referenced, So this needs to be run in the anim scene,
            on a rig that has already been refernced or imported into the scene.

        Kwargs:
            :ns: (str) Anim rig namespace. Defaults to ""."""

    asset = ns or 'character1'
    hik_node = create_character(asset)

    #########################################################################
    # JOINT MAPPING

    if ns:
        ns +=':'
    # hips and first spine
    set_joint(ns+'C_world_JNT_MOCAP', hik_node, 0)
    set_joint(ns+'C_hip_JNT_MOCAP', hik_node, 1)
    set_joint(ns+'C_torso_A_JNT_MOCAP', hik_node, 8)

    # special case for spine:
    spines = mc.ls([ns+'C_torso_*_JNT_MOCAP', ns+'C_chest_JNT_MOCAP'], type='joint')

    if ns+'C_torso_A_JNT_MOCAP' in spines:
        spines.remove(ns+'C_torso_A_JNT_MOCAP')

    i = 23
    for spine in spines:
        set_joint(spine, hik_node, i)
        i += 1

    # special case for necks:
    necks = mc.ls(ns+'C_neck_*_JNT_MOCAP', type='joint')
    i = 20

    for neck in necks[:-1]:
        set_joint(neck, hik_node, i)

        if i == 20:
            i = 32
        else:
            i += 1

    # head
    set_joint(ns+'C_head_JNT_MOCAP', hik_node, 15)

    # arms
    set_joint(ns+'L_shoulder_JNT_MOCAP', hik_node, 18)
    set_joint(ns+'L_upArm_JNT_MOCAP', hik_node, 9)
    set_joint(ns+'L_loArm_JNT_MOCAP', hik_node, 10)
    set_joint(ns+'L_wrist_JNT_MOCAP', hik_node, 11)

    set_joint(ns+'R_shoulder_JNT_MOCAP', hik_node, 19)
    set_joint(ns+'R_upArm_JNT_MOCAP', hik_node, 12)
    set_joint(ns+'R_loArm_JNT_MOCAP', hik_node, 13)
    set_joint(ns+'R_wrist_JNT_MOCAP', hik_node, 14)

    # legs
    set_joint(ns+'L_upLeg_JNT_MOCAP', hik_node, 2)
    set_joint(ns+'L_loLeg_JNT_MOCAP', hik_node, 3)
    set_joint(ns+'L_ankle_JNT_MOCAP', hik_node, 4)
    set_joint(ns+'L_ball_JNT_MOCAP', hik_node, 16)

    set_joint(ns+'R_upLeg_JNT_MOCAP', hik_node, 5)
    set_joint(ns+'R_loLeg_JNT_MOCAP', hik_node, 6)
    set_joint(ns+'R_ankle_JNT_MOCAP', hik_node, 7)
    set_joint(ns+'R_ball_JNT_MOCAP', hik_node, 17)

    print 'Setup HIK node: '+hik_node
    return hik_node


def set_custom_ctrl(node, index, trans=True, rot=True):
    """Asssign node to hik position (joint)"""

    if mc.objExists(node):
        try:
            body = mm.eval('hikCustomRigElementNameFromId( hikGetCurrentCharacter(), {0} )'.format(index))
            retargeter = mm.eval('RetargeterGetName( hikGetCurrentCharacter() );')

            if trans:
                # translate
                mm.eval('RetargeterAddMapping( "{0}", "{1}", "T", "{2}", {3} );'.format(retargeter, body, node, index))

            if rot:
                # Rotate
                mm.eval('RetargeterAddMapping( "{0}", "{1}", "R", "{2}", {3} );'.format(retargeter, body, node, index))

            mm.eval('hikUpdateCustomRigAssignedMappings(hikGetCurrentCharacter())')
            update_hik_UI()

        except:
            mc.warning('Could not connect {0} at index: {2}'.format(node, index))
    else:
        #mc.warning('Node doesnt exist: {0}'.format(node))
        pass

def update_hik_UI():
    """Update the HIK maya UI."""

    try:
        mm.eval('ToggleCharacterControls;ToggleCharacterControls;')
        mm.eval('hikUpdateCharacterList(); hikSelectDefinitionTab();')
        mm.eval('hikUpdateDefinitionButtonState();')
        mm.eval('hikUpdateContextualUI;')
        mm.eval('hikUpdateCustomRigUI;')
    except:
        pass

def set_joint(node, char_node, index):
    """Asssign noe to hik posiotion (joints)"""

    if mc.objExists(node):
        try:
            mm.eval('setCharacterObject("{0}","{1}", {2}, 0);'.format(node, char_node, index))
            update_hik_UI()

        except:
            mc.warning('Could not connect {0} to character: {1} at index: {2}'.format(node, char_node, index))
    else:
        #mc.warning('Node doesnt exist: {0}'.format(node))
        pass

def create_character(name):
    """Create hik new character defionition.

    Args:
        :name: (str) character name"""

    # Create char definiton
    name += '_HIK'
    if mc.objExists(name):
        mm.eval('hikSetCurrentCharacter "{0}"; hikDeleteDefinition'.format(name))
        update_hik_UI()

    result = mm.eval('hikCreateCharacter( "{0}" )'.format(name))

    return name

def lock_character(name):
    # lock HIK character definiton

    mm.eval('hikCharacterLock("{0}", 1, 1 );'.format(name))

def create_tPose():
    """Create T-pose on anim ctrl rig."""

    # constraint stuff
    cons = []

    # elbow cons
    for side in ['L', 'R']:
        cons.extend(mc.parentConstraint(side+'_wrist_FK_CTL',side+'_arm_IK_CTL', mo=1))
        cons.extend(mc.parentConstraint(side+'_legEnd_FK_CTL',side+'_leg_IK_CTL', mo=1))
        cons.extend(mc.parentConstraint(side+'_toe_FK_CTL',side+'_toe_IK_CTL', mo=1))

        for token in ['arm', 'leg']:
            cons.extend(mc.pointConstraint('{0}_lo{1}_FK_CTL'.format(side, token.capitalize()), '{0}_{1}_PV_CTL'.format(side, token)))

    switch_ctrls = [
        'L_arm_IK_switch_CTL',
        'R_arm_IK_switch_CTL',
        'L_leg_IK_switch_CTL',
        'R_leg_IK_switch_CTL']

    for c in switch_ctrls:
        mc.setAttr(c+'.IK', 0)

    # fk arm and fingerts
    fk_ctrls = [
        'L_upArm_FK_CTL',
        'L_loArm_FK_CTL',
        'L_wrist_FK_CTL']

    mc.xform(fk_ctrls, ws=1, ro=[0,0,0])

    for ctrl in fk_ctrls:
        r_ctrl = ctrl.replace('L','R',1)
        mc.xform(r_ctrl, a=1, ro=mc.xform(ctrl, q=1, ro=1, a=1))

    # legs
    orient = utils.decompose_matrix('L_legEnd_FK_CTL')

    loc = utils.snap_locator('L_upLeg_JNT')
    mc.xform(loc, r=1, t=[0,-10,0])
    mc.delete(mc.aimConstraint(loc, 'L_upLeg_FK_CTL', aim=[1,0,0], u=[0,0,-1], wu=[0,0,1], wut='vector'), loc)

    loc = utils.snap_locator('L_loLeg_JNT')
    mc.xform(loc, r=1, t=[0,-10,0])
    mc.delete(mc.aimConstraint(loc, 'L_loLeg_FK_CTL', aim=[1,0,0], u=[0,0,-1], wu=[0,0,1], wut='vector'), loc)

    mc.xform('L_legEnd_FK_CTL', ws=1, ro=orient[1])
    loc = utils.snap_locator('L_legEnd_FK_CTL')
    mc.parent(loc, 'L_legEnd_FK_CTL')
    mc.xform(loc, r=1, t=[1,0,0])
    mc.parent(loc,w=1)

    mc.delete(mc.aimConstraint(loc, 'L_legEnd_FK_CTL', aim=[1,0,0], u=[0,0,-1], wu=[0,0,1], wut='vector'), loc)

    fk_ctrls=  ['L_upLeg_FK_CTL',
                 'L_loLeg_FK_CTL',
                 'L_leg_PV_CTL',
                 'L_leg_IK_A_OFF_CTL',
                 'L_leg_IK_CTL',
                 'L_legEnd_FK_CTL',
                 'L_toe_FK_CTL',
                 'L_toe_IK_CTL']

    for ctrl in fk_ctrls:
        r_ctrl = ctrl.replace('L','R',1)
        mc.xform(r_ctrl, a=1, ro=mc.xform(ctrl, q=1, ro=1, a=1))

    mc.delete(cons)

    for ctrl in tPose_ctrls:
        trans = mc.xform(ctrl, q=1, a=1, t=1)
        rot = mc.xform(ctrl, q=1, a=1, ro=1)
        pose = [trans, rot]
        if not mc.objExists(ctrl+'.TPose'):
            mc.addAttr(ctrl, ln='TPose', dt='string')

        mc.setAttr(ctrl+'.TPose', str(pose), type='string')

def set_aPose(anim_ns=''):
    """Set A-pose on anim rig.

        Kwargs:
            :anim_ns: (str) Namespace of rig. Defaults to ""."""

    try:
        ctrls = [anim_ns+c for c in tPose_ctrls]
        mc.xform(ctrls, a=1, ro=[0,0,0], t=[0,0,0])

    except:
        pass

    apose_jnts = [j.split('.')[0] for j in mc.ls('*.APose')]
    if anim_ns:
        apose_jnts = [j for j in apose_jnts if anim_ns in j]

    for jnt in apose_jnts:
        pose = eval(mc.getAttr(jnt+'.APose'))
        mc.xform(jnt, a=1, t=pose[0], ro=pose[1])

def set_tPose(anim_ns=''):
    """Set T-pose on anim rig.

        Kwargs:
            :anim_ns: (str) Namespace of rig. Defaults to ""."""

    try:
        ctrls = [anim_ns+c for c in tPose_ctrls]

        for ctrl in ctrls:
            if mc.objExists(ctrl+'.TPose'):
                pose = eval(mc.getAttr(ctrl+'.TPose'))
                mc.xform(ctrl, a=1, t=pose[0], ro=pose[1])
    except:
        pass

    apose_jnts = [j.split('.')[0] for j in mc.ls('*.APose')]
    if anim_ns:
        apose_jnts =[j for j in apose_jnts if anim_ns in j]

    if apose_jnts:
        mc.xform(apose_jnts, a=1, ro=[0,0,0])

def delete_all_HIK():
    nodes = mc.ls(type='HIKCharacterNode')
    for node in nodes:
        mm.eval('deleteCharacter( "{0}" )'.format(node))

def connect_rig_to_mocap(mocap_ns='', anim_ns=''):
    """Connect a clean anim, referenced rig to an animated mocap skeleton fbx.

        Kwargs:
            :mocap_ns: (str) Namespace of FBX Skeleton with mocap. Defaults to "".
            :anim_ns: (str) Namespace of anim rig. Defaults to "". """

    # step 2 setup HIK for rig and skel if needed
    if mocap_ns:
        mocap_ns += ':'

    delete_all_HIK()

    #mc.xform(mc.ls(anim_ns+':*_CTL_MOCAP', anim_ns+':*_CTL'), a=1, t=[0,0,0], ro=[0,0,0])

    rig_hik_node = create_anim_rig_hik(anim_ns)
    mocap_hik_node = create_mocap_hik('skel01_Hips')

    if anim_ns:
        anim_ns += ':'

    mc.setAttr(anim_ns+'world_CTL.mocapBlend', 1)
    mm.eval('ToggleCharacterControls;ToggleCharacterControls;')

    arg = """$character = "{0}";
            $source="{1}";
            hikSetCurrentCharacter $character;
            hikSetCurrentSource( $source );
            hikEnableCharacter( $character, 2 );
            hikSetRigInput($character);
            hikSetLiveState( $character, 1 );
            hikSelectControlRigTab();
            hikEnableCharacter( $character, 1 );
            hikSetStanceInput($character);
            hikSetCharacterInput( $character, $source );""".format(rig_hik_node, mocap_hik_node)

    mm.eval(arg)
    update_hik_UI()
    print 'Connected: {0}, driven by: {1}'.format(rig_hik_node, mocap_hik_node)

def bake_mocap_to_rig(anim_ns='', extra_ctrls=[]):
    """Bake mocap down to anim controls.

        Kwargs
            :anim_ns: (str) Namespace of anim rig. Defaults to "".
            :extra_ctrls: (list) Any extra nodes to include in the bake. Defaults to []."""

    ctrls = ['C_head_CTL',
             'L_shoulder_CTL',
             'R_shoulder_CTL',
             'R_arm_IK_CTL',
             'L_arm_IK_CTL',
             'L_arm_PV_CTL',
             'R_arm_PV_CTL',
             'R_leg_IK_CTL',
             'L_leg_IK_CTL',
             'L_toe_IK_CTL',
             'R_toe_IK_CTL',
             'R_leg_PV_CTL',
             'L_leg_PV_CTL',
             'C_cog_CTL',
             'C_chest_CTL',
             'L_upArm_FK_CTL',
             'L_loArm_FK_CTL',
             'L_wrist_FK_CTL',
             'R_upArm_FK_CTL',
             'R_loArm_FK_CTL',
             'R_wrist_FK_CTL',
             'L_upLeg_FK_CTL',
             'R_upLeg_FK_CTL',
             'R_loLeg_FK_CTL',
             'L_loLeg_FK_CTL',
             'L_legEnd_FK_CTL',
             'R_legEnd_FK_CTL',
             'R_toe_FK_CTL',
             'L_toe_FK_CTL']

    if anim_ns:
        anim_ns += ':'

    ctrls = [anim_ns+c for c in ctrls]
    mocap_grps = [c+'_MOCAP' for c in ctrls]

    locs = []
    for ctrl in ctrls:
        loc = mc.createNode('transform', n=ctrl+'_tmp')
        mc.parentConstraint(ctrl, loc)
        locs.append(loc)

    start = mc.playbackOptions(q=1, min=1)
    end = mc.playbackOptions(q=1, max=1)

    mc.bakeResults(locs,
        simulation=True,
        t=(start, end),
        at=['tx','ty','tz', 'rx','ry','rz'],
        sampleBy=1,
        oversamplingRate=1,
        disableImplicitControl=True,
        preserveOutsideKeys=True,
        sparseAnimCurveBake=False,
        removeBakedAttributeFromLayer=False,
        bakeOnOverrideLayer=False,
        minimizeRotation=0,
        controlPoints=False,
        shape=False)

    mc.cutKey(mocap_grps)
    mc.xform(mocap_grps, a=1, t=[0,0,0], ro=[0,0,0])
    cons = []

    for i, ctrl in enumerate(ctrls):
        try:
            con = mc.parentConstraint(locs[i], ctrl)
            cons.append(con[0])
        except:
            try:
                con = mc.orientConstraint(locs[i], ctrl)
                cons.append(con[0])
            except:
                try:
                    con = mc.pointConstraint(locs[i], ctrl)
                    cons.append(con[0])
                except:
                    pass

    mc.setAttr(anim_ns+'world_CTL.mocapBlend', 0)
    extra_ctrls = mc.ls(extra_ctrls)

    mc.bakeResults(ctrls+extra_ctrls,
        simulation=True,
        t=(start, end),
        at=['tx','ty','tz', 'rx','ry','rz'],
        sampleBy=1,
        oversamplingRate=1,
        disableImplicitControl=True,
        preserveOutsideKeys=True,
        sparseAnimCurveBake=False,
        removeBakedAttributeFromLayer=False,
        bakeOnOverrideLayer=False,
        minimizeRotation=0,
        controlPoints=False,
        shape=False)

    mc.delete(locs)

def create_mocap_rig_TPose():
    """This creates a T-pose for newly built mocap rig."""

    arm_jnts = ['L_shoulder_JNT',
                'L_upArm_JNT',
                'L_loArm_JNT',
                'L_wrist_JNT']

    leg_jnts = ['L_upLeg_JNT',
                'L_loLeg_JNT',
                'L_ankle_JNT',
                'L_ball_JNT']

    all_jnts = arm_jnts+ leg_jnts
    all_jnts += [j.replace('L','R', 1) for j in all_jnts]

    all_rotations = [mc.xform(j, q=1, ws=1, ro=1) for j in all_jnts]

    # tpose arms
    mc.xform(arm_jnts, ws=1, ro=[0,0,0])

    # tpose legs
    a_loc = utils.snap_locator(leg_jnts[2])
    a_aim = utils.snap_locator(leg_jnts[2])
    a_up = utils.snap_locator(leg_jnts[-1])

    mc.xform(a_aim, r=1, t=[0,1,0])
    mc.delete(mc.aimConstraint(a_aim, a_loc, aim=[0,1,0], u=[0,0,1], wuo=a_up, wut='object'))
    oc = mc.orientConstraint(a_loc, leg_jnts[2], mo=1)

    loc = utils.snap_locator(leg_jnts[0])
    aim = utils.snap_locator(leg_jnts[0])
    up = utils.snap_locator(leg_jnts[0])

    mc.parent(up, leg_jnts[0])
    mc.xform(aim, r=1, t=[0,-1,0])
    mc.xform(up, r=1, t=[0,0,1])
    mc.parent(up, w=1)

    mc.delete(mc.aimConstraint(aim, loc, aim=[1,0,0], u=[0,0,1], wuo=up, wut='object'))
    mc.delete(mc.orientConstraint(loc, leg_jnts[0]))
    mc.delete(mc.orientConstraint(loc, leg_jnts[1]))
    mc.xform(a_loc, a=1, ro=[0,0,0])

    mc.delete(oc)
    mc.delete(aim, loc, up, a_loc, a_up, a_aim)

    for j in arm_jnts+ leg_jnts:
        r_j = j.replace('L','R', 1)
        mc.xform(r_j, a=1, ro=mc.xform(j, q=1, a=1, ro=1))

    # Freeeezxe jnt s
    mc.makeIdentity('C_root_JNT', apply=1, r=1)

    for i, jnt in enumerate(all_jnts):
        mc.xform(jnt, ws=1, ro=all_rotations[i])

    # REcord tPosae
    for jnt in all_jnts:
        trans = mc.xform(jnt, q=1, a=1, t=1)
        rot = mc.xform(jnt, q=1, a=1, ro=1)
        pose = [trans, rot]
        if not mc.objExists(jnt+'.APose'):
            mc.addAttr(jnt, ln='APose', dt='string')

        mc.setAttr(jnt+'.APose', str(pose), type='string')


def set_up_mocap_scene(asset,
                         fbx_path=None,
                         bake_results=False,
                         remove_HIK=False,

                         offset_position = False,
                         animated_joint = "",
                         offset_curve_translation_values = [0,0,0]):
    """This sets up an hik from fbx scene.

    Args:
        :asset: (str) Asset name.

    Kwargs:
        :fbx_path: (None, str) Defaults to None.
        :bake_results: (bool) Defaults to False.
        :remove_HIK: (bool) Defaults to False.
        :offset_position: (bool) Defaults to: False.
        :animated_joint: (str) Defaults to "".
        :offset_curve_translation_values: (list) Defaults to: [0,0,0]"""

    # shotgun load rig
    if fbx_path and os.path.isfile(fbx_path):
        mc.file(new=1, f=1)
        mc.file(fbx_path, i=1)
        mm.eval('setPlaybackRangeToMinMax;')

    anim_ns = None
    try:
        cm_node = captureMtlAnimation.load_rig(asset_name=asset)
        anim_ns = mc.getAttr(cm_node+'.namespace')
    except:
        pass

    if anim_ns is None:
        raise RuntimeError('Asset not loaded correctly')

    if offset_position == True:
        mc.keyframe (animated_joint + "_translateX",
                    e=True,
                     iub=True,
                      r = True,
                       o =  "over",
                        vc = offset_curve_translation_values[0])

        mc.keyframe (animated_joint + "_translateY",
                    e=True,
                     iub=True,
                      r = True,
                       o =  "over",
                        vc = offset_curve_translation_values[1])

        mc.keyframe (animated_joint + "_translateZ",
                    e=True,
                     iub=True,
                      r = True,
                       o =  "over",
                        vc = offset_curve_translation_values[2])

    connect_rig_to_mocap(anim_ns=anim_ns)


    if bake_results:
        panel = bake.set_dull_panel()
        bake_mocap_to_rig(anim_ns)
        bake.set_model_panel(panel)

    if remove_HIK:
        delete_all_HIK()


def batch_data_list(data_list):
    """Batches the set_up_mocap_scene() function.

        Input lists of data including [source folder, destination folder, shotgun asset name, offset animation - True or False,
        the joint to offset, and a [list of the transform values xyz]

        Example:

            data_list =[

                ["/job/comms/google_ar_stickers_marine_4300074/work/editorial/in/mocap/blackwidow/convert/",  #source folder
                "/job/comms/google_ar_stickers_marine_4300074/work/editorial/in/mocap/blackwidow/BW",         #destination folder
                "BlackWidow",   #Shotgun asset name
                False,          #Offset animation curves? True or False
                "skel01_Hips",  #The joint to offset
                [0,0,0]],       #The value to offset the animation curves by

                ["/job/comms/google_ar_stickers_marine_4300074/work/editorial/in/mocap/thor/process/",
                "/job/comms/google_ar_stickers_marine_4300074/work/editorial/in/mocap/thor/THOR/",
                "Thor",
                False,
                "",
                [0,0,0]]

                ]

        batch_data_list(data_list)"""
    new_file_paths = []

    for data_item in data_list:
        print data_item

        source_folder = data_item[0]
        destination_folder = data_item[1]
        asset_name = data_item[2]

        offset_position = data_item[3]
        animated_joint = data_item[4]
        offset_curve_translation_values = data_item[5]

        raw_files = os.listdir(source_folder)
        files = []
        for each in raw_files:
            if each.find(".fbx") != -1:
                files.append(each)

        for current_file in files:
            print current_file
            mc.file( f=True, new=True )
            mocap_file_path = os.path.join(source_folder,current_file)

            set_up_mocap_scene(asset_name,
                                         fbx_path=mocap_file_path,
                                         bake_results=True,
                                         remove_HIK=True,

                                         offset_position = offset_position,
                                         animated_joint = animated_joint,
                                         offset_curve_translation_values = offset_curve_translation_values)

            stream_safe_name = re.sub("\.",'', current_file)
            stream_safe_name = re.sub("\_",'', stream_safe_name)
            file_name = stream_safe_name + ".mb"
            new_file_path = os.path.join(destination_folder,file_name)
            mc.file(rename=new_file_path)
            mc.file(s=1, type='mayaBinary')
            new_file_paths.append(new_file_path)
