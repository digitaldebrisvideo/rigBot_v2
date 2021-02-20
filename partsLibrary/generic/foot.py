# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import ikChain
from rigBot import control
from rigBot import pickWalk
from rigBot.partsLibrary import standardPart

class Foot(standardPart.StandardPart):
    """Biped and Quad foot module with reverse foot functionalitry with extra controls,
        attributes for rolls and animatable pivots.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "L_leg_end_JNT".
            :fkCtrlParent: (str) Parent ctrl to drive the FK foot controls.  Defaults to "L_legEnd_FK_CTL".
            :ikCtrlParent: (str) Parent ctrl to drive the IK foot controls. Be sure to use the last node of the IK (IF driving this with a biped leg or arm use the orange guide PLC). Defaults to "L_leg_IK_handle_driver_JNT".
            :attrCtrlDriver: (str) Control to drive all foot attributes. Defaults to "L_leg_IK_CTL".
            :switchCtrlDriver: (str) FK / IK switch control to drive switch attributes. Defaults to "L_leg_IK_switch_CTL"."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('parent', data_type='hook', default='L_leg_end_JNT')

        self.add_option('fkCtrlParent',
                        data_type='hook',
                        default = ['L_legEnd_FK_CTL'],
                        tool_tip='Parent ctrl to drive the FK foot controls. ')

        self.add_option('ikCtrlParent',
                        data_type='hook',
                        default = ['L_leg_IK_handle_driver_JNT'],
                        tool_tip='Parent ctrl to drive the IK foot controls. Be sure to use the last node of the IK (IF driving ' +\
                                 'this with a biped leg or arm use the orange guide PLC).')

        self.add_option('attrCtrlDriver',
                        data_type='hook',
                        default = ['L_leg_IK_CTL'],
                        tool_tip='Control to drive all foot attributes.')

        self.add_option('switchCtrlDriver',
                        data_type='hook',
                        default = ['L_leg_IK_switch_CTL'],
                        tool_tip='FK / IK switch control to drive switch attributes.')

        self.add_option('pickWalkParent',
                        data_type='string',
                        default = 'L_leg_PV_CTL',
                        selectable=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix       = self.prefix
        options      = self.options
        mirror_value = self.mirror_value

        # Create joitns
        jnt_zeros, plcs, jnts = self.guide_joint_chain('foot', num_joints=3)
        utils.set_attrs(plcs[-1], 'r', l=1, k=0)

        heel_plc_zero, heel_plc = self.guide_joint('heel', placer_only=1)
        inner_plc_zero, inner_plc = self.guide_joint('innerBall', placer_only=1)
        outter_plc_zero, outter_plc = self.guide_joint('outterBall', placer_only=1)
        ik_driver_plc_zero, ik_driver_plc = self.guide_joint('foot_IK_handle_driver', placer_only=1)

        mc.setAttr(ik_driver_plc+'.radius', 1)
        mc.setAttr(ik_driver_plc+'.color', 0.96, 0.71, .01)
        mc.setAttr(ik_driver_plc+'.otherType',  'Leg IK Driver', type='string');
        mc.setAttr(ik_driver_plc+'.type', 18)

        mc.xform(jnt_zeros, r=1, ro=[self.mirror_value*90, 0, 0])
        mc.parentConstraint(jnts[0], ik_driver_plc_zero)
        mc.setAttr(ik_driver_plc+'.offsetTranslateX', self.mirror_value*0.25)

        utils.set_attrs(ik_driver_plc, l=1, k=0)

        mirror_value = self.mirror_value

        mc.setAttr(heel_plc+'.radius', 1)
        mc.setAttr(outter_plc+'.radius', 1)
        mc.setAttr(inner_plc+'.radius', 1)

        self.tag_as_ref(heel_plc)
        self.tag_as_ref(inner_plc)
        self.tag_as_ref(outter_plc)
        self.tag_as_ref(ik_driver_plc)

        # rotate foward and place joints
        jnt_grp = utils.get_parent(jnt_zeros[0])
        grp = mc.group(jnt_zeros)
        mc.xform(grp, piv=[0,0,0])
        mc.xform(grp, r=1, ro=[0,-90,0])
        mc.xform(grp, r=1, t=[0,0,-1])
        mc.parent(jnt_zeros, jnt_grp)
        mc.delete(grp)

        mc.xform(jnt_zeros[1:], r=1, t=[0,-0.5,0])

        # place pivots
        mc.delete(mc.pointConstraint(jnts[1], inner_plc_zero))
        mc.delete(mc.pointConstraint(jnts[1], outter_plc_zero))

        mc.xform(heel_plc_zero, r=1, t=[0,-0.5,-0.25])
        mc.xform(inner_plc_zero, r=1, t=[-0.5,0,0])
        mc.xform(outter_plc_zero, r=1, t=[0.5,0,0])

        # Create foot ctrl
        color = 'green'
        if mirror_value < 0:
            color = 'red'

        # aim controan toe tip joint to heel plc and up vector to world to get proper foot orientation
        mc.aimConstraint(heel_plc, jnts[-1],
                         aim=[0,0, -mirror_value],
                         u=[0,1,0], wuo=self.guide_master,
                         wu=[0,1,0], wut='objectRotation')

        # Creat pivot controls
        inner_zero, inner_ctrl = self.guide_ctrl('innerBall',
                                                    driver=inner_plc,
                                                    shape='diamond',
                                                    color='pink',
                                                    allow_offset_ctrls=0,
                                                    scale=[0.2]*3,
                                                    create_pivot=0)

        outter_zero, outter_ctrl = self.guide_ctrl('outterBall',
                                                        driver=outter_plc,
                                                        shape='diamond',
                                                        color='pink',
                                                        allow_offset_ctrls=0,
                                                        scale=[0.2]*3,
                                                        create_pivot=0)

        heel_zero, heel_ctrl = self.guide_ctrl('heel',
                                                shape='diamond',
                                                color='pink',
                                                driver=heel_plc,
                                                allow_offset_ctrls=0,
                                                scale=[0.2]*3,
                                                create_pivot=0)

        toe_tip_zero, toe_tip_ctrl = self.guide_ctrl('toeTip',
                                                      shape='diamond',
                                                      color='pink',
                                                      scale=[0.2]*3,
                                                      allow_offset_ctrls=0,
                                                      create_pivot=0)

        reverse_ball_zero, reverse_ball_ctrl = self.guide_ctrl('reverseBall',
                                                                shape='pin_diamond',
                                                                color='pink',
                                                                allow_offset_ctrls=0,
                                                                create_pivot=0)

        ankle_offset_zero, ankle_offset_ctrl = self.guide_ctrl('ankleOffset',
                                                        shape='pin_diamond',
                                                        color='pink',
                                                        allow_offset_ctrls=0,
                                                        create_pivot=0)

        mc.parentConstraint(jnts[-1], toe_tip_zero)

        # constrain reverse ball ctrl
        mc.pointConstraint(jnts[1], reverse_ball_zero)
        mc.orientConstraint(jnts[-1], reverse_ball_zero, mo=1)
        mc.select(reverse_ball_ctrl+'.cv[1:13]')
        mm.eval('scale -r -p 0cm 0.05cm 1cm 2 2 2')

        mc.pointConstraint(jnts[0], ankle_offset_zero)
        mc.orientConstraint(jnts[0], ankle_offset_zero, mo=1)
        mc.select(ankle_offset_ctrl+'.cv[1:13]')
        mm.eval('scale -r -p 0cm 0.55cm 0cm 2 2 2')
        mm.eval('rotate -r -os -fo 47.899271 0 0 ;')

        # constraint the rest of the pivot ctrls
        piv = utils.get_parent(heel_ctrl)
        utils.set_attrs(piv, l=0)
        mc.orientConstraint(jnts[-1], piv)
        utils.set_attrs(piv, l=1, k=0)

        piv = utils.get_parent(inner_ctrl)
        utils.set_attrs(piv, l=0)
        mc.orientConstraint(jnts[-1], piv)
        utils.set_attrs(piv, l=1, k=0)

        piv = utils.get_parent(outter_ctrl)
        utils.set_attrs(piv, l=0)
        mc.orientConstraint(jnts[-1], piv)
        utils.set_attrs(piv, l=1, k=0)

        # Crete IK toe ctrls
        ball_zero, ball_ctrl = self.guide_ctrl(name='toe_IK', shape='circle', color=color, driver=jnts[1], axis='X', create_pivot=False)
        mc.xform(ball_ctrl+'.cv[*]', r=1, t=[mirror_value*0.25,0,0])

        # CReate FK toe ctrl
        ball_fk_zero, ball_fk_ctrl = self.guide_ctrl(name='toe_FK', shape='circle', allow_offset_ctrls=0, color='light_blue', driver=jnts[1], axis='X')

        # rename jnts and plcs
        ankle_jnt = mc.rename(jnts[0], prefix+'_ankle_JNT')
        mc.rename(plcs[0], prefix+'_ankle_JNT_PLC')
        mc.rename(jnt_zeros[0], prefix+'_ankle_JNT'+'_PLC_ZERO')

        mc.rename(plcs[1], prefix+'_ball_JNT_PLC')
        mc.rename(jnts[1], prefix+'_ball_JNT')
        mc.rename(jnt_zeros[1], prefix+'_ball_JNT'+'_PLC_ZERO')

        mc.rename(plcs[2], prefix+'_toe_JNT_PLC')
        mc.rename(jnts[2], prefix+'_toe_JNT')
        mc.rename(jnt_zeros[2], prefix+'_toe_JNT_PLC_ZERO')

        mc.setAttr(self.guide_master+'.offsetTranslateZ', mirror_value*-0.5)

        v=0.2
        mc.xform(heel_ctrl+'.cv[*]', r=1, t=[0,0, -v*self.mirror_value])
        mc.xform(toe_tip_ctrl+'.cv[*]', r=1, t=[0,0, v*self.mirror_value])
        mc.xform(inner_ctrl+'.cv[*]', r=1, t=[-v*self.mirror_value, 0,0 ])
        mc.xform(outter_ctrl+'.cv[*]', r=1, t=[v*self.mirror_value, 0,0 ])


        # This finalizes your guide.
        self.finalize_guide()

    def build_rig(self):
        """This builds your anim rig."""

        # this is a special case to not break exisiting rigs
        if 'leg_end_JNT' in self.options.get('parent'):
            self.update_options(parent=self.options.get('parent').replace('leg_end_JNT', 'leg_end_IK_JNT'))
            print ('updating parent to: '+self.options.get('parent').replace('leg_end_JNT', 'leg_end_IK_JNT'))

        # create rig part top nodes
        self.create_part_master()

        # Get all the relevant part info
        prefix            = self.prefix
        options           = self.options
        anim_ctrls        = self.anim_ctrls
        bind_joints       = self.bind_joints
        hooks             = self.hooks
        ctrl_grps         = self.ctrl_grps
        jnt_grps          = self.jnt_grps

        ankle_jnt = bind_joints[0]
        ball_jnt = bind_joints[1]
        toe_jnt = bind_joints[2]

        heel_plc = prefix+'_heel_JNT_PLC_REF'
        inner_plc = prefix+'_innerBall_JNT_PLC_REF'
        outter_plc = prefix+'_outterBall_JNT_PLC_REF'

        pickWalk_parent = options.get('pickWalkParent')
        snap_to_node = options.get('fkCtrlParent')+'_SNAPTO'

        # Create ctrls

        # This is the orientation i want to match
        name = prefix+'_ankleOffset_CTL'
        ankle_offset_zero, ankle_offset_ctrl, ankle_offset_offsets, ankle_offset_last_node = self.anim_ctrl(name, match_position=ankle_jnt)

        name = prefix+'_reverseBall_CTL'
        reverse_ball_zero, reverse_ball_ctrl, reverse_ball_offsets, reverse_ball_last_node = self.anim_ctrl(name)

        orient_loc = mc.createNode('transform', p=reverse_ball_ctrl)
        mc.parent(orient_loc, w=1)

        name = prefix+'_toe_IK_CTL'
        toe_zero, toe_ctrl, toe_offsets, toe_last_node = self.anim_ctrl(name, match_position=orient_loc)

        name = prefix+'_toeTip_CTL'
        pivot = utils.get_parent(name+'_REF')
        mc.delete(mc.pointConstraint(toe_jnt, orient_loc))
        toe_tip_zero, toe_tip_ctrl, toe_tip_offsets, toe_tip_last_node = self.anim_ctrl(name, match_position=orient_loc)

        name = prefix+'_heel_CTL'
        pivot = utils.get_parent(name+'_REF')
        mc.delete(mc.pointConstraint(pivot, orient_loc))
        heel_zero, heel_ctrl, heel_offsets, heel_last_node = self.anim_ctrl(name, match_position=orient_loc)

        name = prefix+'_innerBall_CTL'
        pivot = utils.get_parent(name+'_REF')
        mc.delete(mc.pointConstraint(pivot, orient_loc))
        inner_zero, inner_ctrl, inner_offsets, inner_last_node = self.anim_ctrl(name, match_position=orient_loc)

        name = prefix+'_outterBall_CTL'
        pivot = utils.get_parent(name+'_REF')
        mc.delete(mc.pointConstraint(pivot, orient_loc))
        outter_zero, outter_ctrl, outter_offsets, outter_last_node = self.anim_ctrl(name, match_position=orient_loc)

        name = prefix+'_toe_FK_CTL'
        toe_fk_zero, toe_fk_ctrl, toe_fk_offsets, toe_fk_last_node = self.anim_ctrl(name)

        # orient constraint t ofk ctrls
        mc.orientConstraint(toe_fk_ctrl, ball_jnt, mo=1)

        # create iks
        ankle_ik = mc.ikHandle(sj=ankle_jnt, ee=ball_jnt, n=ball_jnt+'_IK', sol='ikSCsolver', s='sticky')[0]
        toe_ik = mc.ikHandle(sj=ball_jnt, ee=toe_jnt, n=toe_jnt+'_ik', sol='ikSCsolver', s='sticky')[0]

        # Create fgoot attributes
        mc.addAttr(hooks[3], ln='rollBias', at='double', k=1, min=-1, max=1, dv=0)
        mc.addAttr(hooks[3], ln='rollBallUnbend', at='double', k=1, min=0, max=1, dv=1)
        mc.addAttr(hooks[3], ln='roll', at='double', k=1)
        mc.addAttr(hooks[3], ln='sideRoll', at='double', k=1)
        mc.addAttr(hooks[3], ln='toeTipPivot', at='double', k=1)
        mc.addAttr(hooks[3], ln='ballPivot', at='double', k=1)
        mc.addAttr(hooks[3], ln='heelPivot', at='double', k=1)
        mc.addAttr(hooks[3], ln='heelLift', at='double', k=1)
        mc.addAttr(hooks[3], ln='ballLift', at='double', k=1)
        mc.addAttr(hooks[3], ln='toeTipLift', at='double', k=1)
        mc.addAttr(hooks[3], ln='toeLift', at='double', k=1)

        mc.delete(mc.pointConstraint(ball_jnt, orient_loc))

        foot_last_node = mc.rename(orient_loc, self.prefix+'_reverseFoot_GRP')
        mc.parent(foot_last_node, ctrl_grps[2])

        # Create groups for reverse foot
        name = prefix+'_toe_tip_pivot_GRP'
        toe_tip_pivot_grp = mc.createNode('transform', n=name, p=foot_last_node)
        mc.delete(mc.pointConstraint(toe_tip_ctrl, toe_tip_pivot_grp))

        name = prefix+'_ball_pivot_GRP'
        ball_pivot_grp = mc.createNode('transform', n=name, p=toe_tip_pivot_grp)
        mc.delete(mc.pointConstraint(ball_jnt, ball_pivot_grp))

        name = prefix+'_heel_pivot_GRP'
        heel_pivot_grp = mc.createNode('transform', n=name, p=ball_pivot_grp)
        mc.delete(mc.pointConstraint(heel_ctrl, heel_pivot_grp))

        # roll is handled in the foot ctrl attr "sideRoll"
        name = prefix+'_inner_roll_GRP'
        inner_roll_grp = mc.createNode('transform', n=name, p=heel_pivot_grp)
        mc.delete(mc.pointConstraint(inner_ctrl, inner_roll_grp))

        name = prefix+'_outter_roll_GRP'
        outter_roll_grp = mc.createNode('transform', n=name, p=inner_roll_grp)
        mc.delete(mc.pointConstraint(outter_ctrl, outter_roll_grp))

        heel_roll_grp = heel_zero
        reverse_ball_roll_grp = reverse_ball_zero
        toe_tip_roll_grp = toe_tip_zero

        mc.parent(heel_zero, outter_roll_grp)
        mc.parent(toe_tip_zero, heel_ctrl)
        mc.parent(inner_zero, toe_tip_ctrl)
        mc.parent(outter_zero, inner_ctrl)
        mc.parent(toe_zero, outter_ctrl)
        mc.parent(reverse_ball_zero, outter_ctrl)

        ankle_ik_grp = mc.createNode('transform', n=ankle_ik+'_GRP', p=ankle_ik)
        toe_ik_grp = mc.createNode('transform', n=toe_ik+'_GRP', p=toe_ik)

        # This will be the driver for the leg ik (named in the guides)
        name = prefix+'_foot_IK_handle_driver_JNT'
        ankle_ik_grp = mc.rename(ankle_ik_grp, name)

        mc.parent(ankle_ik_grp, reverse_ball_ctrl)
        mc.parent(toe_ik_grp, toe_ctrl)

        mc.parent(ankle_ik, ankle_ik_grp)
        mc.parent(toe_ik, toe_ik_grp)

        mc.parent(toe_fk_zero, ctrl_grps[1])

        # Connect pivot attrs
        foot_ctrl = hooks[3]
        utils.connect_negative(foot_ctrl+'.toeTipPivot', toe_tip_pivot_grp+'.ry')
        utils.connect_negative(foot_ctrl+'.ballPivot', ball_pivot_grp+'.ry')
        mc.connectAttr(foot_ctrl+'.heelPivot', heel_pivot_grp+'.ry', f=1)

        # connect side roll
        inner_clamp = mc.createNode('clamp', n=inner_roll_grp+'_clamp')
        outter_clamp = mc.createNode('clamp', n=outter_roll_grp+'_clamp')
        mc.setAttr(inner_clamp+'.minR', -100000)
        mc.setAttr(outter_clamp+'.maxR', 100000)

        utils.connect_negative(foot_ctrl+'.sideRoll', inner_clamp+'.inputR')
        utils.connect_negative(foot_ctrl+'.sideRoll', outter_clamp+'.inputR')
        mc.connectAttr(inner_clamp+'.outputR', outter_roll_grp+'.rz')
        mc.connectAttr(outter_clamp+'.outputR', inner_roll_grp+'.rz')

        # connect toe flop attr
        utils.connect_negative(foot_ctrl+'.toeLift', toe_zero+'.rx')

        # connect lifts (adding multDoubleLinear to take intao acount the roll attr)
        toe_tip_roll_adl = mc.createNode('addDoubleLinear', n=toe_tip_zero+'_adl')
        mc.connectAttr(foot_ctrl+'.toeTipLift', toe_tip_roll_adl+'.input1')
        mc.connectAttr(toe_tip_roll_adl+'.output', toe_tip_zero+'.rx', f=1)

        reverse_ball_roll_adl = mc.createNode('addDoubleLinear', n= reverse_ball_zero+'_adl')
        mc.connectAttr(foot_ctrl+'.ballLift', reverse_ball_roll_adl+'.input1')
        mc.connectAttr(reverse_ball_roll_adl+'.output', reverse_ball_zero+'.rx', f=1)

        reverse_ball_negative_grp = reverse_ball_ctrl+'_CONST'

        heel_roll_adl = mc.createNode('addDoubleLinear')
        mc.connectAttr(foot_ctrl+'.heelLift', heel_roll_adl+'.input1')
        utils.connect_negative(heel_roll_adl+'.output', heel_zero+'.rx')

        # Connect foot roll heel portion
        heel_roll_clamp = mc.createNode('clamp', name=foot_ctrl+'_heel_roll_CLAMP')
        utils.connect_negative(heel_roll_clamp+'.outputR', heel_roll_adl+'.input2')
        mc.connectAttr(foot_ctrl+'.roll', heel_roll_clamp+'.inputR')
        mc.setAttr(heel_roll_clamp+'.minR', -100000)

        """
        MATH:

            # set range FROM: -1.0 -- 1.01 TO: 0.0 -- 1.0
            float $value = 0 + (((L_foot_foot_CTRL.rollBias+1.0)/(1.0+1.0)) * (1.0-0.0)) ;

            L_foot_reverseBall_CTRL_ZERO_adl.input2 = clamp(0, $value * 90, L_foot_foot_CTRL.roll);
            L_foot_toeTip_CTRL_ZERO_adl.input2 = clamp(0, 3600, L_foot_foot_CTRL.roll - L_foot_reverseBall_CTRL_ZERO_adl.input2);
            L_foot_reverseBall_CTRL_GRP.rotateX = -L_foot_toeTip_CTRL_ZERO_adl.input2;
        """

        # # set range FROM: -1.0 -- 1.01 TO: 0.0 -- 1.0
        bias_set_range = mc.createNode('setRange', n=prefix+'_bias_SR')
        mc.connectAttr(foot_ctrl+'.rollBias', bias_set_range+'.valueX')
        mc.setAttr(bias_set_range+'.maxX', 1)
        mc.setAttr(bias_set_range+'.oldMinX', -1)
        mc.setAttr(bias_set_range+'.oldMaxX', 1)

        # convert value to angular value
        bias_mdl = mc.createNode('multDoubleLinear', n=prefix+'_bias_to_degrees_MDL')
        mc.connectAttr(bias_set_range+'.outValueX', bias_mdl+'.input1')
        mc.setAttr(bias_mdl+'.input2', 90)

        # Create clamp and drive the reverse ball grp  clamp(min: 0 max:value input: foot_ctrl.footRoll)
        reverse_ball_roll_clamp = mc.createNode('clamp', n=prefix+'_reverse_ball_roll_CLAMP')
        mc.connectAttr(foot_ctrl+'.roll', reverse_ball_roll_clamp+'.inputR')
        mc.connectAttr(bias_mdl+'.output', reverse_ball_roll_clamp+'.maxR')
        mc.connectAttr(reverse_ball_roll_clamp+'.outputR', reverse_ball_roll_adl+'.input2')

        # Create clamp and drive the INVERTED reverse ball grp  clamp(min: 0 max:1000000 input: foot_ctrl.footRoll - reverse_ball_roll_clamp+'.outputR')
        reverse_ball_negative_clamp = mc.createNode('clamp', n=prefix+'_neg_inverted_reverse_ball_roll_CLAMP')
        mc.setAttr(reverse_ball_negative_clamp+'.maxR', 1000000)

        # set up subtract node
        reverse_ball_negative_pma = mc.createNode('plusMinusAverage', n=prefix+'_neg_inverted_reverse_ball_roll_PMA')
        mc.setAttr(reverse_ball_negative_pma+'.operation', 2)

        mc.connectAttr(foot_ctrl+'.roll', reverse_ball_negative_pma+'.input1D[0]')
        mc.connectAttr(reverse_ball_roll_clamp+'.outputR', reverse_ball_negative_pma+'.input1D[1]')
        mc.connectAttr(reverse_ball_negative_pma+'.output1D', reverse_ball_negative_clamp+'.inputR')
        mc.connectAttr(reverse_ball_negative_clamp+'.outputR', toe_tip_roll_adl+'.input2')

        # Connect the last part MATH: L_foot_reverseBall_CTRL_GRP.rotateX = -L_foot_toeTip_CTRL_ZERO_adl.input2;
        reverse_ball_roll_grp_mdl = mc.createNode('multDoubleLinear', n=prefix+'_reverse_ball_roll_MDL')
        mc.connectAttr(reverse_ball_negative_clamp+'.outputR', reverse_ball_roll_grp_mdl+'.input1')
        mc.connectAttr(reverse_ball_roll_grp_mdl+'.output', reverse_ball_negative_grp+'.rx')
        mc.setAttr(reverse_ball_roll_grp_mdl+'.input2', -1)

        utils.connect_negative(foot_ctrl+'.rollBallUnbend', reverse_ball_roll_grp_mdl+'.input2')

        # Create IK FK Switch
        ik_handles = [ankle_ik, toe_ik]
        mc.parentConstraint(hooks[0], ankle_jnt, mo=1)

        ikChain.create_fk_ik_switch(hooks[-1], ik_handles, toe_fk_zero, heel_zero)
        mc.setAttr(hooks[-1]+'.IK', 1)
        mc.hide(ik_handles)

        # remove driven nodesna otheri offsets freo any ctrl sets
        mc.parent(ankle_jnt, jnt_grps[0])

        # Create ankle_offset
        mc.parent(ankle_offset_zero, reverse_ball_ctrl)
        mc.parentConstraint(ankle_jnt, ankle_offset_zero, mo=1)

        chain = [ankle_jnt, ball_jnt, toe_jnt]
        chain = [mc.rename(j, j+'_OFF_IK') for j in chain]
        new_chain = ikChain.duplicate_chain(chain, '_JNT_OFF_IK', '_JNT')

        mc.parentConstraint(ankle_offset_ctrl, new_chain[0], mo=1)
        mc.connectAttr(chain[1]+'.r', new_chain[1]+'.r')
        mc.hide(chain)

        if mc.objExists(snap_to_node):
            utils.set_attrs(snap_to_node, l=0, k=1)
            mc.parent(snap_to_node+'_GRP', ankle_jnt)
        else:
            mc.createNode('transform', n=snap_to_node, p=ankle_jnt)

        ikChain.create_snapto_node(toe_ctrl, toe_jnt)

        #Set the foots pickwalk parent
        pickWalk.attribute_tag(foot_ctrl, pickWalk_parent)

        # Create fx cureve
        #utils.create_cfx_curves([ankle_jnt, ball_jnt, toe_jnt], self.prefix+'_'+self.part_type)

        # This finalizes guide and creates rig sets
        self.finalize_part()
