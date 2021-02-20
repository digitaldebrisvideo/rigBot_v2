# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import ikChain
from rigBot import pickWalk
from rigBot.partsLibrary import standardPart

class QuadArm(standardPart.StandardPart):
    """This is an empty part. It only builds a guide master and empty rig hooks.
        Format your options in the docs as follows for proper auto-documentation.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "front".
            :parent: (str) Parent. Defaults to "C_hip_JNT".
            :ikHandleParent: (str) Optional IK handle parent for connecting to a foot part. Will default to it's own IK control if the node doesnt exist. Defaults to "L_foot_IK_handle_driver_JNT".
            :numberTwistJoints: (int) Number of twist joints PER upper and lower arm. Defaults to 4."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('parent', data_type='hook', default='C_hip_JNT')
        self.add_option('name', default='front')

        self.add_option('ikHandleParent',
                        data_type='hook',
                        default='L_foot_IK_handle_driver_JNT',
                        tool_tip="Optional IK handle parent for connecting to a "+\
                                 "foot part. Will default to it's own IK control "+\
                                 "if the node doesnt exist.")

        self.add_option('numberTwistJoints',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=4,
                        min=0,
                        tool_tip='Number of twist joints PER upper and lower arm.')

        self.add_option('flipJoints',
                        data_type='bool',
                        default=False,
                        hidden=True,
                        tool_tip='Flip the up axis of the bind joints. '+\
                                 '(Useful when the knee points backwards.)')

        self.add_option('transOrientiation',
                 data_type='enum',
                 default='world',
                 enum='world:downBone',
                 tool_tip='Orient the translates on IK control to the world OR down the bone.')

        self.add_option('pickWalkParent',
                        data_type='string',
                        default = 'C_chest_CTL',
                        selectable=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide. Use KWARGS to update any options at build time."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix              # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options = self.options            # Build options
        mirror_value = self.mirror_value  # 1.0 for left and center sided parts and -1.0 for right sided part.

        # Start coding suckka !!

        number_twist_jnts = options.get('numberTwistJoints')
        make_bendy = options.get('bendy')

        # draw joints
        shoulder_zero, shoulder_plc, shoulder_jnt = self.guide_joint('shoulder', constraint_type='point')
        up_arm_zero, up_arm_plc, up_arm_jnt = self.guide_joint('upArm', constraint_type='point')
        mid_arm_zero, mid_arm_plc, mid_arm_jnt = self.guide_joint('midArm', constraint_type='point')
        lo_arm_zero, lo_arm_plc, lo_arm_jnt = self.guide_joint('loArm', constraint_type='point')
        arm_end_zero, arm_end_plc, arm_end_jnt = self.guide_joint('arm_end', constraint_type='point')

        ik_driver_plc_zero, ik_driver_plc = self.guide_joint('arm_IK_handle_driver', placer_only=1)

        mc.setAttr(ik_driver_plc+'.radius', 1)
        mc.setAttr(ik_driver_plc+'.color', 0.96, 0.71, .01)
        mc.setAttr(ik_driver_plc+'.otherType',  'Arm IK Driver', type='string');
        mc.setAttr(ik_driver_plc+'.type', 18)

        mc.parentConstraint(arm_end_jnt, ik_driver_plc_zero)
        mc.setAttr(ik_driver_plc+'.offsetTranslateX', self.mirror_value*-0.25)

        # position
        mc.setAttr(shoulder_zero+'.tx', -1)
        mc.setAttr(up_arm_zero+'.tx', 0)
        mc.setAttr(mid_arm_zero+'.tx', 0)
        mc.setAttr(lo_arm_zero+'.tx', 0)
        mc.setAttr(mid_arm_zero+'.ty', -2)
        mc.setAttr(mid_arm_zero+'.tz', -1)
        mc.setAttr(lo_arm_zero+'.ty', -4)
        mc.setAttr(lo_arm_zero+'.tz', -0.2)
        mc.setAttr(arm_end_zero+'.tx', 0)
        mc.setAttr(arm_end_zero+'.ty', -6)

        # parent
        mc.parent(up_arm_jnt, shoulder_jnt)
        mc.parent(arm_end_jnt, lo_arm_jnt)
        mc.parent(lo_arm_jnt, mid_arm_jnt)
        mc.parent(mid_arm_jnt, up_arm_jnt)

        # Create orient reader
        orient = mc.createNode('transform', p=up_arm_plc, n=up_arm_plc+'_orient_GRP')

        mc.aimConstraint(arm_end_plc,
                                  orient ,
                                  aim=[mirror_value,0,0],
                                  u=[0,0,-mirror_value],
                                  wut='object',
                                  wuo=mid_arm_plc)[0]

        # Constraint upArm
        up_ac = mc.aimConstraint(mid_arm_plc,
                         up_arm_jnt,
                         aim=[mirror_value,0,0],
                         u=[0,1,0],
                         wu=[0,1,0],
                         wut='objectRotation',
                         wuo=orient)[0]

        mid_ac = mc.aimConstraint(lo_arm_plc,
                         mid_arm_jnt,
                         aim=[mirror_value,0,0],
                         u=[0,1,0],
                         wu=[0,1,0],
                         wut='objectRotation',
                         wuo=orient)[0]

        lo_ac = mc.aimConstraint(arm_end_plc,
                         lo_arm_jnt,
                         aim=[mirror_value,0,0],
                         u=[0,1,0],
                         wu=[0,1,0],
                         wut='objectRotation',
                         wuo=orient)[0]

        mc.aimConstraint(up_arm_plc,
                         shoulder_jnt ,
                         aim=[mirror_value,0,0],
                         u=[0,0,1],
                         wu=[0,0,1],
                         wut='objectRotation',
                         wuo=shoulder_plc)[0]

        mc.parentConstraint(orient, lo_arm_zero, mo=1)
        utils.set_attrs(arm_end_jnt, 'jo', l=0, k=1)
        mc.setAttr(arm_end_jnt+'.r', 0,0,0)
        mc.setAttr(arm_end_jnt+'.jo', 0,0,0)

        mc.setDrivenKeyframe(up_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=1, v=self.mirror_value)
        mc.setDrivenKeyframe(up_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=0, v=-self.mirror_value)
        mc.setDrivenKeyframe(mid_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=1, v=self.mirror_value)
        mc.setDrivenKeyframe(mid_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=0, v=-self.mirror_value)
        mc.setDrivenKeyframe(lo_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=1, v=self.mirror_value)
        mc.setDrivenKeyframe(lo_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=0, v=-self.mirror_value)

        # Create twist jnts
        div = 1.0 / (number_twist_jnts+1)

        up_twist_zeros, up_twist_plcs, up_twist_jnts = [], [], []
        lo_twist_zeros, lo_twist_plcs, lo_twist_jnts = [], [], []

        for i in range(number_twist_jnts):

            # setup upper arm jnts
            letter = utils.letters[i]
            zero, plc, jnt = self.guide_joint('upArm_twist_'+letter, constraint_type='point')

            if up_twist_jnts:
                mc.parent(jnt, up_twist_jnts[-1])
            else:
                mc.parent(jnt, up_arm_jnt)

            up_twist_jnts.append(jnt)
            up_twist_plcs.append(plc)
            up_twist_zeros.append(zero)

            mc.pointConstraint(up_arm_plc, plc, weight=1.0-(div*(i+1)))
            mc.pointConstraint(mid_arm_plc, plc, weight=(div*(i+1)))
            mc.orientConstraint(up_arm_jnt, plc)

            mc.xform(jnt, a=1, ro=[0,0,0])
            mc.setAttr(jnt+'.jo', 0,0,0)

            utils.set_attrs(plc, 't r s', l=1, k=0)

            # setup uplowerper arm jnts
            letter = utils.letters[i]
            zero, plc, jnt = self.guide_joint('loArm_twist_'+letter, constraint_type='point')

            if lo_twist_jnts:
                mc.parent(jnt, lo_twist_jnts[-1])
            else:
                mc.parent(jnt, lo_arm_jnt)

            lo_twist_jnts.append(jnt)
            lo_twist_plcs.append(plc)
            lo_twist_zeros.append(zero)

            mc.pointConstraint(lo_arm_plc, plc, weight=1.0-(div*(i+1)))
            mc.pointConstraint(arm_end_plc, plc, weight=(div*(i+1)))
            mc.orientConstraint(lo_arm_jnt, plc)

            mc.xform(jnt, a=1, ro=[0,0,0])
            mc.setAttr(jnt+'.jo', 0,0,0)

            utils.set_attrs(plc, 't r s', l=1, k=0)

        if up_twist_jnts:
            mc.parent(mid_arm_jnt, up_twist_jnts[-1])
            for plc in up_twist_plcs:
                mc.setAttr(plc+'.radius', 0.7)

        if lo_twist_jnts:
            mc.parent(arm_end_jnt, lo_twist_jnts[-1])
            for plc in lo_twist_plcs:
                mc.setAttr(plc+'.radius', 0.7)

        #lock plcs
        utils.set_attrs([up_arm_plc, lo_arm_plc], 'r s', l=1, k=0)

        # Create ctrls
        up_arm_fk_zero, up_arm_fk_ctrl = self.guide_ctrl(name='upArm_FK',
            shape='circle',
            color='light_blue',
            driver=up_arm_jnt,
            allow_offset_ctrls=False,
            axis='X')

        mid_arm_fk_zero, mid_arm_fk_ctrl = self.guide_ctrl(name='midArm_FK',
            shape='circle',
            color='light_blue',
            driver=mid_arm_jnt,
            allow_offset_ctrls=False,
            axis='X')

        lo_arm_fk_zero, lo_arm_fk_ctrl = self.guide_ctrl(name='loArm_FK',
            shape='circle',
            color='light_blue',
            driver=lo_arm_jnt,
            allow_offset_ctrls=False,
            axis='X')

        arm_end_fk_zero, arm_end_fk_ctrl = self.guide_ctrl(name='armEnd_FK',
            shape='circle',
            color='light_blue',
            driver=arm_end_jnt,
            allow_offset_ctrls=False,
            axis='X')

        color = 'green'
        if mirror_value < 0:
            color = 'red'

        arm_ik_zero, arm_ik_ctrl = self.guide_ctrl('arm_IK',
            shape='circle',
            axis='X',
            color=color,
            create_pivot=False,
            scale=[1.5,1.5,2.5])

        orient_loc = mc.createNode('transform', p=arm_end_jnt, n=arm_end_jnt+'_orient')
        mc.parent(orient_loc, w=1)
        mc.xform(orient_loc, r=1, t=[0,1,0])
        mc.pointConstraint(arm_end_jnt, orient_loc, mo=1)
        mc.parent(orient_loc, self.guide_master+'_CTLS')

        mc.pointConstraint(arm_end_jnt, arm_ik_zero)
        mc.aimConstraint(orient_loc, arm_ik_zero, aim=[mirror_value, 0,0], u=[0,1,0], wu=[0,1,0], wut='objectRotation', wuo=arm_end_jnt)

        pv_zero, pv_ctrl = self.guide_ctrl('arm_PV', shape='cube', color=color, scale=[0.2]*3, allow_offset_ctrls=0, create_pivot=0)
        pv_pivot = utils.get_parent(pv_ctrl)

        noxform = utils.get_parent(pv_zero).replace('CTLS', 'NOX')

        # Constraint pv
        mc.setAttr(pv_zero+'.ty', -2.35)
        mc.setAttr(pv_zero+'.tz', -4)

        mc.parentConstraint(orient, pv_zero, mo=1)
        mc.orientConstraint(noxform, pv_ctrl, n=pv_ctrl+'_pc')

        utils.set_attrs([pv_ctrl, pv_zero], 'r t s v', l=1, k=0)
        utils.set_attrs(pv_ctrl, 'tx tz s ', l=0, k=1)

        # Arm base ctrl
        arm_base_fk_zero, arm_base_fk_ctrl = self.guide_ctrl(name='shoulder',
            shape='semi_circle',
            color=color,
            scale=[1.5,1.5,3],
            driver=shoulder_jnt,
            axis='Y')

        mc.xform(arm_base_fk_ctrl+'.cv[*]', r=1, ro=[0,-90,0])

        lo_arm_ik_zero, lo_arm_ik_ctrl = self.guide_ctrl(name='loArm_IK',
            shape='sphere',
            color=color,
            create_pivot=False,
            scale=[0.8]*3,
            driver=lo_arm_jnt)

        # ik fk switch ctrl
        switch_zero, switch_ctrl = self.guide_ctrl(name='arm_IK_switch', shape='pin_gear', color='lavendar', driver=arm_end_jnt)
        mc.xform(switch_ctrl, r=1, ro=[0,0,180])
        mc.makeIdentity(switch_ctrl, apply=1, t=1, r=1, s=1, n=0, pn=1)
        mc.setAttr(arm_ik_ctrl+'.numOffsetCtrls', 1)

        line = mc.createNode('transform', n=pv_ctrl+'_line_REF', p=utils.get_parent(pv_zero))
        control.create_driven_shape(line, [pv_ctrl, mid_arm_jnt])
        utils.set_draw_override(line, 1)

        # This finalizes your guide.
        mc.setAttr(self.guide_master+'.tx', self.mirror_value)
        mc.setAttr(self.guide_master+'.offsetTranslateY', self.mirror_value*0.5)
        utils.set_attrs(ik_driver_plc, l=1, k=0)

        # This finalizes your guide.
        self.finalize_guide()

    def build_rig(self):
        """This builds your anim rig."""

        # create rig part top nodes
        self.create_part_master()

        prefix            = self.prefix                 # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options           = self.options                # Build options
        anim_ctrls        = self.anim_ctrls             # Anim controls in this part
        bind_joints       = self.bind_joints            # Bind joints in this rig part
        world_scale_attr  = self.hooks[0]+'.worldScale' # World scale multiplier (Each hooks has it's own world scale)
        hooks             = self.hooks                  # A hook grp is created per hook attribute.
        ctrl_grps         = self.ctrl_grps              # A ctrl group is created per hook. Parent controls here.
        jnt_grps          = self.jnt_grps               # A joint groupd is created per hook. Parent joints here.
        noxform_grp       = self.noxform_grp            # No scale, no transform group for this rig part.
        mirror_value      = self.mirror_value           # 1.0 for left and center sided parts and -1.0 for right sided part.

        # Start coding suckka!!

        number_twist_jnts = options.get('numberTwistJoints')
        parent = options.get('parent')

        world_orient_trans=options.get('transOrientiation')

        shoulder_jnt = prefix+'_shoulder_JNT'
        up_arm_jnt = prefix+'_upArm_JNT'
        mid_arm_jnt = prefix+'_midArm_JNT'
        lo_arm_jnt = prefix+'_loArm_JNT'
        arm_end_jnt = prefix+'_arm_end_JNT'

        up_arm_twist_jnts = mc.ls(prefix+'_upArm_twist_*_JNT')
        lo_arm_twist_jnts = mc.ls(prefix+'_loArm_twist_*_JNT')
        pickWalk_parent = options.get('pickWalkParent')
        # Create FK ctrls
        name = prefix+'_shoulder_CTL'
        arm_base_zero, arm_base_ctrl, arm_base_offsets, arm_base_last_node = self.anim_ctrl(name)

        name = prefix+'_upArm_FK_CTL'
        up_arm_fk_zero, up_arm_fk_ctrl, up_arm_fk_offsets, up_arm_fk_last_node = self.anim_ctrl(name)

        name = prefix+'_midArm_FK_CTL'
        mid_arm_fk_zero, mid_arm_fk_ctrl, mid_arm_fk_offsets, mid_arm_fk_last_node = self.anim_ctrl(name)

        name = prefix+'_loArm_FK_CTL'
        lo_arm_fk_zero, lo_arm_fk_ctrl, lo_arm_fk_offsets, lo_arm_fk_last_node = self.anim_ctrl(name)

        name = prefix+'_armEnd_FK_CTL'
        arm_end_fk_zero, arm_end_fk_ctrl, arm_end_fk_offsets, arm_end_fk_last_node = self.anim_ctrl(name)

        #Comment this IF you want the foot tp up vector to the ankle position
        orient_loc = utils.snap_locator(arm_end_jnt)
        tmp_aim = utils.snap_locator(arm_end_jnt)
        mc.xform(tmp_aim, r=1, t=[0,1,0])

        if self.mirror_value < 0:
            mc.xform(orient_loc, r=1, s=[-1,0,0])

        mc.delete(mc.aimConstraint(tmp_aim, orient_loc,
                                   u=[0,0,1],
                                   wu=[0,0,-1],
                                   aim=[0,self.mirror_value, 0],
                                   wuo=arm_end_jnt,
                                   wut='objectRotation'))

        # Create IK ctrls
        name = prefix+'_arm_IK_CTL'
        arm_ik_zero, arm_ik_ctrl, arm_ik_offsets, arm_ik_last_node = self.anim_ctrl(name, node_type='joint', match_position=orient_loc)

        arm_ik_last_node = mc.createNode('transform', p=arm_ik_last_node, n=prefix+'_arm_IK_handle_driver_JNT')

        utils.set_attrs(arm_ik_ctrl, 'jo', l=0, k=1)

        grp = mc.group(arm_ik_ctrl)
        mc.parent(grp, w=1)

        mc.xform(arm_ik_zero, ws=1, ro=[0,0,0])

        mc.parent(arm_ik_ctrl, arm_ik_zero)
        mc.delete(orient_loc, tmp_aim, grp)

        mc.setAttr(arm_ik_ctrl+'.jox', 0)
        mc.setAttr(arm_ik_ctrl+'.joz', 0)

        for ctrl in [arm_ik_ctrl]+arm_ik_offsets:
            control.copy_shape(ctrl+'_REF', ctrl)

        name = prefix+'_arm_PV_CTL'
        loc = utils.snap_locator(name+'_REF')
        mc.setAttr(loc+'.sx', self.mirror_value)
        pv_zero, pv_ctrl, pv_offsets, pv_last_node = self.anim_ctrl(name, match_position=loc)

        name = prefix+'_arm_IK_switch_CTL'
        switch_zero, switch_ctrl, switch_offsets, switch_last_node = self.anim_ctrl(name)

        mc.delete(loc)

        up_arm_grp = mc.createNode('transform', n=up_arm_jnt+'_GRP', p=up_arm_jnt)
        mc.parent(up_arm_grp, jnt_grps[0])
        mc.parent(up_arm_jnt, up_arm_grp)

        # orient arm ik ctrl
        tmp_grp = mc.createNode('transform', p=arm_ik_ctrl)
        mc.parent(tmp_grp, w=1)

        mc.xform(arm_ik_zero, a=1, ro=[0,0,0])
        mc.setAttr(arm_ik_zero+'.s', self.mirror_value,1,1)

        utils.set_attrs(arm_ik_ctrl, 'jo', l=0)
        mc.parent(arm_ik_ctrl, arm_ik_ctrl+'_OFF')
        mc.delete(tmp_grp)

        if world_orient_trans == 'downBone':
            utils.set_attrs(arm_ik_ctrl+'_ZERO', 'ry', k=1, l=0)
            utils.set_attrs(arm_ik_ctrl, 'joy', k=1, l=0)
            mc.setAttr(arm_ik_ctrl+'_ZERO.ry', mc.getAttr(arm_ik_ctrl+'.joy'))

            utils.set_attrs(arm_ik_ctrl+'_ZERO', 'ry', k=0, l=1)
            utils.set_attrs(arm_ik_ctrl, 'joy', k=0, l=1)


        # Create lo arm IK
        tmp = mc.createNode('transform', p=arm_ik_ctrl)
        mc.delete(mc.aimConstraint(lo_arm_jnt, tmp, aim=[0,1,0], u=[0,0,1], wu=[0,0,1], wut='objectRotation', wuo=arm_ik_ctrl))
        mc.parent(tmp, w=1)

        name = prefix+'_loArm_IK_CTL'
        lo_arm_ik_zero, lo_arm_ik_ctrl, lo_arm_ik_offsets, lo_arm_ik_last_node = self.anim_ctrl(name, match_position=tmp)
        mc.delete(tmp)

        mc.parent(lo_arm_ik_zero, arm_ik_last_node)
        for c in [lo_arm_ik_ctrl]+lo_arm_ik_offsets:
            mc.setAttr(c+'.ro', 1)

        # parent fk ctrls
        mc.parent(up_arm_fk_zero, arm_base_last_node)
        mc.parent(mid_arm_fk_zero, up_arm_fk_ctrl)
        mc.parent(lo_arm_fk_zero, mid_arm_fk_ctrl)
        mc.parent(arm_end_fk_zero, lo_arm_fk_ctrl)

        # NOW create ik fk chain setup
        up_arm_ik_jnt = mc.duplicate(up_arm_jnt, po=1, n=up_arm_jnt.replace('upArm', 'upArm_IK'))[0]
        mid_arm_ik_jnt = mc.duplicate(mid_arm_jnt, po=1, n=mid_arm_jnt.replace('midArm', 'midArm_IK'))[0]
        lo_arm_ik_jnt = mc.duplicate(lo_arm_jnt, po=1, n=lo_arm_jnt.replace('loArm', 'loArm_IK'))[0]
        arm_end_ik_jnt = mc.duplicate(arm_end_jnt, po=1, n=arm_end_jnt.replace('arm_end', 'arm_end_IK'))[0]

        mc.parent(mid_arm_ik_jnt, up_arm_ik_jnt)
        mc.parent(lo_arm_ik_jnt, mid_arm_ik_jnt )
        mc.parent(arm_end_ik_jnt, lo_arm_ik_jnt)

        # Create second chain
        sec_up_arm_ik_jnt = mc.duplicate(up_arm_jnt, po=1, n=up_arm_jnt.replace('upArm', 'upArm_sec_IK'))[0]
        sec_mid_arm_ik_jnt = mc.duplicate(mid_arm_jnt, po=1, n=mid_arm_jnt.replace('midArm', 'midArm_sec_IK'))[0]
        sec_lo_arm_ik_jnt = mc.duplicate(lo_arm_jnt, po=1, n=lo_arm_jnt.replace('loArm', 'loArm_sec_IK'))[0]
        sec_arm_end_ik_jnt = mc.duplicate(arm_end_jnt, po=1, n=arm_end_jnt.replace('arm_end', 'arm_end_sec_IK'))[0]

        mc.parent(sec_mid_arm_ik_jnt, sec_up_arm_ik_jnt)
        mc.parent(sec_lo_arm_ik_jnt, sec_mid_arm_ik_jnt )
        mc.parent(sec_arm_end_ik_jnt, sec_lo_arm_ik_jnt)

        # orient condstrain uparm
        mc.parentConstraint(up_arm_fk_last_node, sec_up_arm_ik_jnt, mo=1)
        mc.parentConstraint(up_arm_fk_last_node, up_arm_ik_jnt, mo=1)
        mc.scaleConstraint(jnt_grps[0], up_arm_ik_jnt, mo=1)

        # connect the midarm usuing orient contraint then direct connections to avoid cycling
        ori_par = mc.createNode('transform', p=mid_arm_jnt, n=mid_arm_jnt+'_orient_DRV_PAR')
        ori = mc.createNode('transform', p=ori_par, n=mid_arm_jnt+'_orient_DRV')
        mc.parent(ori_par, mid_arm_fk_zero)

        mc.orientConstraint(mid_arm_fk_ctrl, ori, mo=1)
        mc.connectAttr(ori+'.r', mid_arm_ik_jnt+'.r')
        mc.connectAttr(ori+'.r', sec_mid_arm_ik_jnt+'.r')

        # connect the midarm usuing orient contraint then direct connectns to avoid cycling
        ori_par = mc.createNode('transform', p=lo_arm_jnt, n=lo_arm_jnt+'_orient_DRV_PAR')
        ori = mc.createNode('transform', p=ori_par, n=lo_arm_jnt+'_orient_DRV')
        mc.parent(ori_par, lo_arm_fk_zero)

        mc.orientConstraint(lo_arm_fk_ctrl, ori, mo=1)
        mc.connectAttr(ori+'.r', lo_arm_ik_jnt+'.r')
        mc.connectAttr(ori+'.r', sec_lo_arm_ik_jnt+'.r')

        # Create spring ik handle

        utils.set_attrs(lo_arm_ik_jnt, 'r', l=1)
        test = utils.snap_locator(mid_arm_ik_jnt)
        ik_handle = mc.ikHandle(sj=up_arm_ik_jnt,
                                ee=arm_end_ik_jnt,
                                s='sticky',
                                n=prefix+'_arm_IK')[0]

        mc.poleVectorConstraint(pv_ctrl, ik_handle)

        # This is a test to correct the slight shift in PV
        i = 0
        while round(utils.get_distance(test, mid_arm_ik_jnt), 3)> 0.01 and i < 360:
            mc.setAttr(ik_handle+'.twist', i)
            i += 1

        if round(utils.get_distance(test, mid_arm_ik_jnt), 3) > 0.01:
            i = 0
            while round(utils.get_distance(test, mid_arm_ik_jnt), 3)> 0.01 and i > -360:
                mc.setAttr(ik_handle+'.twist', i)
                i -= 1

        mc.delete(test)

        # Create lo arm IK
        up_ik_handle = mc.ikHandle(sj=sec_up_arm_ik_jnt,
                                ee=sec_lo_arm_ik_jnt,
                                s='sticky',
                                n=prefix+'_sec_up_arm_IK')[0]

        lo_ik_handle = mc.ikHandle(sj=sec_lo_arm_ik_jnt,
                                ee=sec_arm_end_ik_jnt,
                                s='sticky',
                                n=prefix+'_sec_lo_arm_IK')[0]

        up_sec_pv = mc.createNode('transform', n=prefix+'_up_sec_PV', p=up_arm_ik_jnt)
        mc.delete(mc.pointConstraint(pv_ctrl, up_sec_pv))
        mc.setAttr(up_sec_pv+'.ty', 0)

        mc.poleVectorConstraint(up_sec_pv, up_ik_handle)

        i = 0
        test = utils.snap_locator(mid_arm_ik_jnt)
        while round(utils.get_distance(test, sec_mid_arm_ik_jnt), 3)> 0.01 and i < 360:
            mc.setAttr(up_ik_handle+'.twist', i)
            i += 1

        if round(utils.get_distance(test, sec_mid_arm_ik_jnt), 3) > 0.01:
            i = 0
            while round(utils.get_distance(test, sec_mid_arm_ik_jnt), 3)> 0.01 and i > -360:
                mc.setAttr(up_ik_handle+'.twist', i)
                i -= 1

        mc.delete(test)

        # Create ik switch and parent handles
        ikChain.create_fk_ik_switch(switch_ctrl, [ik_handle, up_ik_handle, lo_ik_handle], up_arm_fk_zero, [arm_ik_zero, pv_zero])

        mc.parent(ik_handle, lo_ik_handle, arm_ik_last_node)
        mc.parent(up_ik_handle, lo_arm_ik_last_node)
        mc.parentConstraint(lo_arm_ik_jnt, lo_arm_ik_zero, mo=1)

        mc.setAttr(switch_ctrl+'.IK', 1)
        mc.hide(ik_handle, lo_ik_handle, up_ik_handle)

        # Add bias and twist attrs
        mc.addAttr(arm_ik_ctrl, ln='twist', k=1)
        mc.addAttr(arm_ik_ctrl, ln='upTwist', k=1)

        # Connect twist
        adl = mc.createNode('addDoubleLinear')
        mc.setAttr(adl+'.input1', mc.getAttr(ik_handle+'.twist'))
        mc.connectAttr(adl+'.output', ik_handle+'.twist')

        mc.connectAttr(arm_ik_ctrl+'.twist', adl+'.input2')
        if self.mirror_value < 0.0:
            utils.connect_negative(arm_ik_ctrl+'.twist', adl+'.input2')

        # Connect twist
        adl = mc.createNode('addDoubleLinear')
        mc.setAttr(adl+'.input1', mc.getAttr(up_ik_handle+'.twist'))
        mc.connectAttr(adl+'.output', up_ik_handle+'.twist')

        mc.connectAttr(arm_ik_ctrl+'.upTwist', adl+'.input2')
        if self.mirror_value < 0.0:
            utils.connect_negative(arm_ik_ctrl+'.upTwist', adl+'.input2')

        # Create soft ik
        ik_joints = [up_arm_ik_jnt, mid_arm_ik_jnt, lo_arm_ik_jnt, arm_end_ik_jnt]
        ik_ctrl = arm_ik_ctrl

        # case for IK hook
        ik_handle_grp = mc.createNode('transform', p=arm_ik_last_node, n=ik_handle+'_GRP')
        mc.parent(ik_handle_grp, jnt_grps[1])
        mc.parent(ik_handle, ik_handle_grp)
        mc.parentConstraint(arm_ik_last_node, hooks[1], mo=1)

        ik_handle_parent = ikChain.create_soft_ik(ik_ctrl, ik_joints, ik_handle)

        # Create IK wrist orient switch
        ik_ctrl_follow_par = mc.createNode('transform', n=sec_arm_end_ik_jnt+'_ik_follow_PAR', p=sec_arm_end_ik_jnt)
        fk_ctrl_follow_par = mc.createNode('transform', n=sec_arm_end_ik_jnt+'_fk_follow_PAR', p=sec_arm_end_ik_jnt)

        ik_ctrl_follow = mc.createNode('transform', n=sec_arm_end_ik_jnt+'_ik_follow', p=sec_arm_end_ik_jnt)
        fk_ctrl_follow = mc.createNode('transform', n=sec_arm_end_ik_jnt+'_fk_follow', p=sec_arm_end_ik_jnt)

        mc.parent(fk_ctrl_follow, fk_ctrl_follow_par)
        mc.parent(ik_ctrl_follow, ik_ctrl_follow_par)
        mc.parent(fk_ctrl_follow_par, arm_end_fk_ctrl)
        mc.parent(ik_ctrl_follow_par, arm_ik_last_node)

        oc = mc.orientConstraint(fk_ctrl_follow, ik_ctrl_follow, sec_arm_end_ik_jnt)[0]
        mc.setAttr(oc+'.interpType', 2)

        mc.connectAttr(switch_ctrl+'.IK', oc+'.w1', f=1)
        utils.connect_reverse(oc+'.w1', oc+'.w0')

        # Create twist
        if up_arm_twist_jnts:
            ikChain.upper_twist(utils.get_parent(sec_up_arm_ik_jnt), sec_up_arm_ik_jnt, sec_mid_arm_ik_jnt, up_arm_jnt, mid_arm_jnt, up_arm_twist_jnts)
            ikChain.lower_twist(sec_lo_arm_ik_jnt, sec_arm_end_ik_jnt, lo_arm_jnt, lo_arm_twist_jnts, arm_end_jnt)

            ikChain.stretch_twist_jnts(sec_up_arm_ik_jnt, sec_mid_arm_ik_jnt, up_arm_twist_jnts)
            ikChain.stretch_twist_jnts(sec_lo_arm_ik_jnt, sec_arm_end_ik_jnt, lo_arm_twist_jnts)

        else:
            mc.parentConstraint(sec_up_arm_ik_jnt, up_arm_jnt ,mo=1)
            mc.parentConstraint(sec_lo_arm_ik_jnt, lo_arm_jnt ,mo=1)
            mc.parentConstraint(sec_arm_end_ik_jnt, arm_end_jnt, mo=1)

        # Set up Stretch
        fk_ctrls = [up_arm_fk_ctrl, mid_arm_fk_ctrl, lo_arm_fk_ctrl, arm_end_fk_ctrl]
        jnts = [up_arm_ik_jnt, mid_arm_ik_jnt, lo_arm_ik_jnt, arm_end_ik_jnt]
        sec_jnts = [sec_up_arm_ik_jnt, sec_mid_arm_ik_jnt, sec_lo_arm_ik_jnt, sec_arm_end_ik_jnt]

        ikChain.multi_joint_stretch(arm_ik_ctrl, arm_ik_last_node, switch_ctrl, fk_ctrls, jnts, ik_handle)

        for i in range(1, len(jnts), 1):
            mc.connectAttr(jnts[i]+'.tx', sec_jnts[i]+'.tx')

        # Create movable pivot to compensate lo arm ik stretch
        piv = mc.createNode('transform', p=lo_arm_ik_ctrl+'_ZERO', n=lo_arm_ik_ctrl+'_piv_correct')
        mc.connectAttr(piv+'.t', lo_arm_ik_ctrl+'.rotatePivot')
        mc.connectAttr(piv+'.t', lo_arm_ik_ctrl+'.scalePivot')
        mc.pointConstraint(arm_end_ik_jnt, piv)

        mc.pointConstraint(arm_end_ik_jnt, lo_ik_handle)

        # Create drive nline shape for pv
        control.create_driven_shape(pv_ctrl, mid_arm_jnt, replace=False)

        # clean shit up now
        mc.hide(up_arm_ik_jnt, sec_up_arm_ik_jnt)

        mc.parentConstraint(arm_end_jnt, switch_zero, mo=1)
        mc.parent(arm_base_zero, arm_ik_zero, pv_zero, switch_zero, ctrl_grps[0])

        utils.set_attrs([up_arm_fk_ctrl, mid_arm_fk_ctrl, arm_end_fk_ctrl, lo_arm_fk_ctrl], 't s v', l=1, k=0)
        utils.set_attrs([lo_arm_fk_ctrl, mid_arm_fk_ctrl], 'ro', l=1, k=0)
        utils.set_attrs(pv_ctrl, 'r s v ro', l=1, k=0)
        utils.set_attrs(switch_ctrl, 't r s v ro', l=1, k=0)
        utils.set_attrs(arm_base_ctrl, 's', l=1, k=0)

        utils.set_attrs(arm_ik_offsets+[arm_ik_ctrl, lo_arm_ik_ctrl], ' s v ro jo radius', l=1, k=0, cb=0)
        for c in arm_ik_offsets+[arm_ik_ctrl]:
            mc.setAttr(c+'.radius', k=0, cb=0)

        utils.set_attrs(lo_arm_ik_ctrl, 't', l=1, k=0, cb=0)

        # spaces
        spaces.tag(arm_ik_ctrl, default=2)
        spaces.tag(pv_ctrl, default=0)

        jnts = [up_arm_jnt]+up_arm_twist_jnts+[lo_arm_jnt]+lo_arm_twist_jnts+[arm_end_jnt]
        #utils.create_cfx_curves(jnts, self.prefix+'_'+self.part_type)

        # movable pivot
        control.create_movable_pivot(arm_ik_ctrl, ctrl_type='joint')

        # Set up shoulder
        mc.parent(shoulder_jnt, jnt_grps[0])
        mc.parent(up_arm_grp, shoulder_jnt)
        mc.parentConstraint(arm_base_last_node, shoulder_jnt, mo=1)

        # Create all joints
        auto_shoulder = mc.duplicate(shoulder_jnt, po=1, n=shoulder_jnt+'_AUTO')[0]
        auto_wrist = mc.duplicate(up_arm_jnt, po=1, n=up_arm_jnt+'_AUTO')[0]
        mc.parent(auto_wrist, auto_shoulder)

        # Create ik
        auto_ik_handle = mc.ikHandle(sj=auto_shoulder, ee=auto_wrist, s='sticky', n=prefix+'_arm_auto_clav_IK')[0]
        mc.pointConstraint(ik_handle_grp, auto_ik_handle)
        mc.refresh()
        mc.delete(auto_ik_handle)
        mc.makeIdentity(auto_shoulder, apply=1, t=1, r=1, s=1, n=0, pn=1)

        auto_ik_handle = mc.ikHandle(sj=auto_shoulder, ee=auto_wrist, s='sticky', n=prefix+'_arm_auto_clav_IK')[0]
        mc.pointConstraint(ik_handle_grp, auto_ik_handle)
        mc.parent(auto_ik_handle, ik_handle_grp)
        mc.setAttr(auto_ik_handle+'.poleVector', 0,0,0)

        up_grp = mc.createNode('transform', n=auto_ik_handle+'_up_GRP', p=jnt_grps[0])
        mc.delete(mc.pointConstraint(shoulder_jnt, up_grp))
        mc.xform(up_grp, r=1, t=[0,1,0])

        mc.poleVectorConstraint(up_grp, auto_ik_handle)

        # Create atrtrs
        mc.addAttr(arm_base_ctrl, ln='autoClavicle', min=0, max=1, k=1)
        mc.addAttr(arm_base_ctrl, ln='clavUpLimit', min=0, dv=90, k=1)
        mc.addAttr(arm_base_ctrl, ln='clavDownLimit', min=0, dv=45, k=1)
        mc.addAttr(arm_base_ctrl, ln='clavFrontLimit', min=0, dv=90, k=1)
        mc.addAttr(arm_base_ctrl, ln='clavBackLimit', min=0, dv=90, k=1)

        mc.connectAttr(arm_base_ctrl+'.clavUpLimit', auto_shoulder+'.maxRotZLimit')
        mc.connectAttr(arm_base_ctrl+'.clavBackLimit', auto_shoulder+'.maxRotYLimit')
        utils.connect_negative(arm_base_ctrl+'.clavDownLimit', auto_shoulder+'.minRotZLimit')
        utils.connect_negative(arm_base_ctrl+'.clavFrontLimit', auto_shoulder+'.minRotYLimit')

        mc.setAttr(auto_shoulder+'.maxRotYLimitEnable', 1)
        mc.setAttr(auto_shoulder+'.minRotYLimitEnable', 1)
        mc.setAttr(auto_shoulder+'.maxRotZLimitEnable', 1)
        mc.setAttr(auto_shoulder+'.minRotZLimitEnable', 1)

        auto_follow_par = mc.duplicate(arm_base_ctrl+'_CONST', po=1, n=arm_base_ctrl+'_AUTO_GRP')[0]
        auto_follow = mc.duplicate(arm_base_ctrl+'_CONST', po=1, n=arm_base_ctrl+'_AUTO')[0]
        auto_follow_static = mc.duplicate(arm_base_ctrl+'_CONST', po=1, n=arm_base_ctrl+'_AUTO_STATIC')[0]

        mc.parent(auto_follow, auto_follow_par)
        mc.parent(auto_follow_par, auto_shoulder)

        oc = mc.orientConstraint(auto_follow_static, auto_follow, arm_base_ctrl+'_CONST')[0]
        mc.connectAttr(arm_base_ctrl+'.autoClavicle', oc+'.w1')
        utils.connect_reverse(arm_base_ctrl+'.autoClavicle', oc+'.w0')

        mc.hide(auto_shoulder, auto_shoulder, auto_ik_handle)
        mc.setAttr(oc+'.interpType', 2)

        # Doesnt workl correctly yet
        utils.set_attrs(arm_base_ctrl, 'autoClavicle clavUpLimit clavDownLimit clavBackLimit clavFrontLimit', l=1, k=0)
        #Setup pickwalking

        pickWalk.attribute_tag(lo_arm_fk_ctrl, mid_arm_fk_ctrl)
        pickWalk.attribute_tag(mid_arm_fk_ctrl, up_arm_fk_ctrl)
        pickWalk.attribute_tag(arm_end_fk_ctrl, mid_arm_fk_ctrl)

        pickWalk.attribute_tag(pv_ctrl,arm_base_ctrl)
        pickWalk.attribute_tag(arm_ik_ctrl, lo_arm_ik_ctrl)
        pickWalk.attribute_tag(lo_arm_ik_ctrl, pv_ctrl)

        pickWalk.attribute_tag(arm_base_ctrl, pickWalk_parent)

        # This finalizes guide and creates rig sets
        self.create_ctrl_set('FK', fk_ctrls)
        self.finalize_part()

        utils.set_attrs(up_arm_ik_jnt, l=0, k=1)
