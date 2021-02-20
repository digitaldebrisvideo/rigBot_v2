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

class EncoreQuadLeg(standardPart.StandardPart):
    """This is an empty part. It only builds a guide master and empty rig hooks.
        Format your options in the docs as follows for proper auto-documentation.

        Build Options:
        :side: (str) Side token for this rig part. Defaults to "L".
        :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "rear".
        :parent: (str) Parent. Defaults to "C_hip_JNT".
        :ikHandleParent: (str) Optional IK handle parent for connecting to a foot part. Will default to it's own IK control if the node doesnt exist. Defaults to "L_rear_foot_IK_handle_driver_JNT".
        :numberTwistJoints: (int) Number of twist joints PER upper and lower leg. Defaults to 4."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('parent', data_type='hook', default='C_hip_JNT')
        self.add_option('name', default='rear')

        self.add_option('ikHandleParent',
                        data_type='hook',
                        default='L_rear_foot_IK_handle_driver_JNT',
                        tool_tip="Optional IK handle parent for connecting to a "+\
                                 "foot part. Will default to it's own IK control "+\
                                 "if the node doesnt exist.")

        self.add_option('numberTwistJoints',
                        data_type='int',
                        rebuild_to_modify=True,
                        default=4,
                        min=0,
                        tool_tip='Number of twist joints PER upper and lower leg.')

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
                data_type='hook',
                default = 'C_hip_CTL',
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
        up_leg_zero, up_leg_plc, up_leg_jnt = self.guide_joint('upLeg', constraint_type='point')
        mid_leg_zero, mid_leg_plc, mid_leg_jnt = self.guide_joint('midLeg', constraint_type='point')
        lo_leg_zero, lo_leg_plc, lo_leg_jnt = self.guide_joint('loLeg', constraint_type='point')
        leg_end_zero, leg_end_plc, leg_end_jnt = self.guide_joint('leg_end', constraint_type='point')

        ik_driver_plc_zero, ik_driver_plc = self.guide_joint('leg_IK_handle_driver', placer_only=1)

        mc.setAttr(ik_driver_plc+'.radius', 1)
        mc.setAttr(ik_driver_plc+'.color', 0.96, 0.71, .01)
        mc.setAttr(ik_driver_plc+'.otherType',  'Leg IK Driver', type='string');
        mc.setAttr(ik_driver_plc+'.type', 18)

        mc.parentConstraint(leg_end_jnt, ik_driver_plc_zero)
        mc.setAttr(ik_driver_plc+'.offsetTranslateX', self.mirror_value*-0.25)

        # position
        mc.setAttr(up_leg_zero+'.tx', 0)
        mc.setAttr(mid_leg_zero+'.tx', 0)
        mc.setAttr(lo_leg_zero+'.tx', 0)
        mc.setAttr(mid_leg_zero+'.ty', -2.35)
        mc.setAttr(mid_leg_zero+'.tz', 1)
        mc.setAttr(lo_leg_zero+'.ty', -4)
        mc.setAttr(lo_leg_zero+'.tz', -0.65)
        mc.setAttr(leg_end_zero+'.tx', 0)
        mc.setAttr(leg_end_zero+'.ty', -6)

        # parent
        mc.parent(leg_end_jnt, lo_leg_jnt)
        mc.parent(lo_leg_jnt, mid_leg_jnt)
        mc.parent(mid_leg_jnt, up_leg_jnt)

        # Create orient reader
        orient = mc.createNode('transform', p=up_leg_plc, n=up_leg_plc+'_orient_GRP')

        mc.aimConstraint(leg_end_plc,
                                  orient ,
                                  aim=[mirror_value,0,0],
                                  u=[0,0,-mirror_value],
                                  wut='object',
                                  wuo=mid_leg_plc)[0]

        # Constraint upLeg
        up_ac = mc.aimConstraint(mid_leg_plc,
                         up_leg_jnt,
                         aim=[mirror_value,0,0],
                         u=[0,1,0],
                         wu=[0,1,0],
                         wut='objectRotation',
                         wuo=orient)[0]

        mid_ac = mc.aimConstraint(lo_leg_plc,
                         mid_leg_jnt,
                         aim=[mirror_value,0,0],
                         u=[0,1,0],
                         wu=[0,1,0],
                         wut='objectRotation',
                         wuo=orient)[0]

        lo_ac = mc.aimConstraint(leg_end_plc,
                         lo_leg_jnt,
                         aim=[mirror_value,0,0],
                         u=[0,1,0],
                         wu=[0,1,0],
                         wut='objectRotation',
                         wuo=orient)[0]

        mc.parentConstraint(orient, lo_leg_zero, mo=1)
        utils.set_attrs(leg_end_jnt, 'jo', l=0, k=1)
        mc.setAttr(leg_end_jnt+'.r', 0,0,0)
        mc.setAttr(leg_end_jnt+'.jo', 0,0,0)

        mc.setDrivenKeyframe(up_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=0, v=self.mirror_value)
        mc.setDrivenKeyframe(up_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=1, v=-self.mirror_value)
        mc.setDrivenKeyframe(mid_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=0, v=self.mirror_value)
        mc.setDrivenKeyframe(mid_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=1, v=-self.mirror_value)
        mc.setDrivenKeyframe(lo_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=0, v=self.mirror_value)
        mc.setDrivenKeyframe(lo_ac+'.upVectorY', cd=self.guide_master+'.flipJoints', dv=1, v=-self.mirror_value)

        # Create twist jnts
        div = 1.0 / (number_twist_jnts+1)

        twist_zeros, twist_plcs, twist_jnts = [], [], []
        lo_twist_zeros, lo_twist_plcs, lo_twist_jnts = [], [], []

        for i in range(number_twist_jnts):

            # setup upper leg jnts
            letter = utils.letters[i]
            zero, plc, jnt = self.guide_joint('upLeg_twist_'+letter, constraint_type='point')
            shp_plc_zero, shp_plc, shp_jnt = self.guide_joint('upLeg_shaper_'+letter, constraint_type='point')
            shp_ctrl_zero, shp_ctrl = self.guide_ctrl(name='upLeg_shaper'+letter,
                                                             shape='pin_circle',
                                                             color='dark_magenta',
                                                             driver=shp_jnt,
                                                             allow_offset_ctrls=False,
                                                             axis='X')

            if twist_jnts:
                mc.parent(jnt, twist_jnts[-1])

            else:
                mc.parent(jnt, mid_leg_jnt)

            mc.delete (mc.pointConstraint (jnt, shp_plc_zero))
            # mc.parentConstraint (jnt, shp_plc_zero, mo=1)
            mc.setAttr (shp_plc_zero+'.visibility', 0)

            twist_jnts.append(jnt)
            twist_plcs.append(plc)
            twist_zeros.append(zero)

            mc.pointConstraint(mid_leg_plc, plc, weight=1.0-(div*(i+1)))
            mc.pointConstraint(lo_leg_plc, plc, weight=(div*(i+1)))
            mc.orientConstraint(mid_leg_plc, plc)

            mc.xform(jnt, a=1, ro=[0,0,0])
            mc.setAttr(jnt+'.jo', 0,0,0)

            utils.set_attrs(plc, 't r s', l=1, k=0)

            # # setup lower leg jnts
            letter = utils.letters[i]
            zero, plc, jnt = self.guide_joint('loLeg_twist_'+letter, constraint_type='point')
            shp_plc_zero, shp_plc, shp_jnt = self.guide_joint('loLeg_shaper_'+letter, constraint_type='point')
            shp_ctrl_zero, shp_ctrl = self.guide_ctrl(name='loLeg_shaper'+letter,
                                                             shape='pin_circle',
                                                             color='dark_magenta',
                                                             driver=shp_jnt,
                                                             allow_offset_ctrls=False,
                                                             axis='X')

            if lo_twist_jnts:
                mc.parent(jnt, lo_twist_jnts[-1])
            else:
                mc.parent(jnt, lo_leg_jnt)

            mc.parentConstraint (jnt, shp_plc_zero)
            mc.setAttr (shp_plc_zero+'.visibility', 0)

            lo_twist_jnts.append(jnt)
            lo_twist_plcs.append(plc)
            lo_twist_zeros.append(zero)

            mc.pointConstraint(lo_leg_plc, plc, weight=1.0-(div*(i+1)))
            mc.pointConstraint(leg_end_plc, plc, weight=(div*(i+1)))
            mc.orientConstraint(lo_leg_jnt, plc)

            mc.xform(jnt, a=1, ro=[0,0,0])
            mc.setAttr(jnt+'.jo', 0,0,0)

            utils.set_attrs(plc, 't r s', l=1, k=0)

        if twist_jnts:
            mc.parent(lo_leg_jnt, twist_jnts[-1])
            for plc in twist_plcs:
                mc.setAttr(plc+'.radius', 0.7)

        if lo_twist_jnts:
            mc.parent(leg_end_jnt, lo_twist_jnts[-1])
            for plc in lo_twist_plcs:
                mc.setAttr(plc+'.radius', 0.7)

        #lock plcs
        utils.set_attrs([up_leg_plc, lo_leg_plc], 'r s', l=1, k=0)

        # Create ctrls
        up_leg_fk_zero, up_leg_fk_ctrl = self.guide_ctrl(name='upLeg_FK',
            shape='circle',
            color='light_blue',
            driver=up_leg_jnt,
            allow_offset_ctrls=False,
            axis='X')

        mid_leg_fk_zero, mid_leg_fk_ctrl = self.guide_ctrl(name='midLeg_FK',
            shape='circle',
            color='light_blue',
            driver=mid_leg_jnt,
            allow_offset_ctrls=False,
            axis='X')

        lo_leg_fk_zero, lo_leg_fk_ctrl = self.guide_ctrl(name='loLeg_FK',
            shape='circle',
            color='light_blue',
            driver=lo_leg_jnt,
            allow_offset_ctrls=False,
            axis='X')

        leg_end_fk_zero, leg_end_fk_ctrl = self.guide_ctrl(name='legEnd_FK',
            shape='circle',
            color='light_blue',
            driver=leg_end_jnt,
            allow_offset_ctrls=False,
            axis='X')

        color = 'blue'
        if mirror_value < 0:
            color = 'red'

        leg_ik_zero, leg_ik_ctrl = self.guide_ctrl('leg_IK',
            shape='circle',
            axis='X',
            color=color,
            create_pivot=False,
            scale=[1.5,1.5,2.5])

        orient_loc = mc.createNode('transform', p=leg_end_jnt, n=leg_end_jnt+'_orient')
        mc.parent(orient_loc, w=1)
        mc.xform(orient_loc, r=1, t=[0,1,0])
        mc.pointConstraint(leg_end_jnt, orient_loc, mo=1)
        mc.parent(orient_loc, self.guide_master+'_CTLS')

        mc.pointConstraint(leg_end_jnt, leg_ik_zero)
        mc.aimConstraint(orient_loc, leg_ik_zero, aim=[mirror_value, 0,0], u=[0,1,0], wu=[0,1,0], wut='objectRotation', wuo=leg_end_jnt)

        pv_zero, pv_ctrl = self.guide_ctrl('leg_PV', shape='cube', color=color, scale=[0.2]*3, allow_offset_ctrls=0, create_pivot=0)
        pv_pivot = utils.get_parent(pv_ctrl)

        noxform = utils.get_parent(pv_zero).replace('CTLS', 'NOX')

        # Constraint pv
        mc.setAttr(pv_zero+'.ty', -2.35)
        mc.setAttr(pv_zero+'.tz', 4)

        mc.parentConstraint(orient, pv_zero, mo=1)
        mc.orientConstraint(noxform, pv_ctrl, n=pv_ctrl+'_pc')

        utils.set_attrs([pv_ctrl, pv_zero], 'r t s v', l=1, k=0)
        utils.set_attrs(pv_ctrl, 'tx tz s ', l=0, k=1)

        # Leg base ctrl
        leg_base_fk_zero, leg_base_fk_ctrl = self.guide_ctrl(name='legBase',
            shape='semi_circle',
            color=color,
            scale=[1.5,1.5,3],
            driver=up_leg_jnt,
            axis='Y')

        mc.xform(leg_base_fk_ctrl+'.cv[*]', r=1, ro=[0,90,90])

        lo_leg_ik_zero, lo_leg_ik_ctrl = self.guide_ctrl(name='loLeg_IK',
            shape='sphere',
            color=color,
            create_pivot=False,
            scale=[0.8]*3,
            driver=lo_leg_jnt)

        # ik fk switch ctrl
        root_jnt='C_root_JNT'
        if not mc.objExists (root_jnt):
            root_zero, root_plc, root_jnt = self.guide_joint('root', constraint_type='parent')
        # switch_zero, switch_ctrl = self.guide_ctrl(name='leg_IK_switch', shape='arrow_double', color='black', driver=up_leg_jnt)
        switch_zero, switch_ctrl = self.guide_ctrl(name='leg_IK_switch', shape='arrow_double', color='black')
        mc.delete (mc.pointConstraint  (up_leg_jnt, switch_zero, mo=0 ))
        mc.setAttr (switch_zero+'.t', 2, 2, 0)
        mc.setAttr (switch_zero+'.rx', 90)
        mc.parentConstraint (root_jnt, switch_zero, mo=1)
        # mc.xform(switch_ctrl, r=1, ro=[0,0,0])
        # mc.makeIdentity(switch_ctrl, apply=1, t=1, r=1, s=1, n=0, pn=1)
        mc.setAttr(leg_ik_ctrl+'.numOffsetCtrls', 1)

        line = mc.createNode('transform', n=pv_ctrl+'_line_REF', p=utils.get_parent(pv_zero))
        control.create_driven_shape(line, [pv_ctrl, mid_leg_jnt])
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

        number_twist_jnts = options.get('numberTwistJoints')
        parent = options.get('parent')
        pickWalk_parent = options.get('pickWalkParent')

        world_orient_trans=options.get('transOrientiation')

        up_leg_jnt = prefix+'_upLeg_JNT'
        mid_leg_jnt = prefix+'_midLeg_JNT'
        lo_leg_jnt = prefix+'_loLeg_JNT'
        leg_end_jnt = prefix+'_leg_end_JNT'

        leg_twist_jnts = mc.ls(prefix+'_upLeg_twist_*_JNT')
        lo_leg_twist_jnts = mc.ls(prefix+'_loLeg_twist_*_JNT')

        # Create FK ctrls
        name = prefix+'_legBase_CTL'
        leg_base_zero, leg_base_ctrl, leg_base_offsets, leg_base_last_node = self.anim_ctrl(name)

        name = prefix+'_upLeg_FK_CTL'
        up_leg_fk_zero, up_leg_fk_ctrl, up_leg_fk_offsets, up_leg_fk_last_node = self.anim_ctrl(name)

        name = prefix+'_midLeg_FK_CTL'
        mid_leg_fk_zero, mid_leg_fk_ctrl, mid_leg_fk_offsets, mid_leg_fk_last_node = self.anim_ctrl(name)

        name = prefix+'_loLeg_FK_CTL'
        lo_leg_fk_zero, lo_leg_fk_ctrl, lo_leg_fk_offsets, lo_leg_fk_last_node = self.anim_ctrl(name)

        name = prefix+'_legEnd_FK_CTL'
        leg_end_fk_zero, leg_end_fk_ctrl, leg_end_fk_offsets, leg_end_fk_last_node = self.anim_ctrl(name)

        #Comment this IF you want the foot tp up vector to the ankle position
        orient_loc = utils.snap_locator(leg_end_jnt)
        tmp_aim = utils.snap_locator(leg_end_jnt)
        mc.xform(tmp_aim, r=1, t=[0,1,0])

        if self.mirror_value < 0:
            mc.xform(orient_loc, r=1, s=[-1,0,0])

        mc.delete(mc.aimConstraint(tmp_aim, orient_loc,
                                   u=[0,0,1],
                                   wu=[0,0,-1],
                                   aim=[0,self.mirror_value, 0],
                                   wuo=leg_end_jnt,
                                   wut='objectRotation'))

        # Create IK ctrls
        name = prefix+'_leg_IK_CTL'
        leg_ik_zero, leg_ik_ctrl, leg_ik_offsets, leg_ik_last_node = self.anim_ctrl(name, node_type='joint', match_position=orient_loc)

        leg_ik_last_node = mc.createNode('transform', p=leg_ik_last_node, n=prefix+'_leg_IK_handle_driver_JNT')

        utils.set_attrs(leg_ik_ctrl, 'jo', l=0, k=1)

        grp = mc.group(leg_ik_ctrl)
        mc.parent(grp, w=1)

        mc.xform(leg_ik_zero, ws=1, ro=[0,0,0])

        mc.parent(leg_ik_ctrl, leg_ik_zero)
        mc.delete(orient_loc, tmp_aim, grp)

        mc.setAttr(leg_ik_ctrl+'.jox', 0)
        mc.setAttr(leg_ik_ctrl+'.joz', 0)

        for ctrl in [leg_ik_ctrl]+leg_ik_offsets:
            control.copy_shape(ctrl+'_REF', ctrl)

        name = prefix+'_leg_PV_CTL'
        loc = utils.snap_locator(name+'_REF')
        mc.setAttr(loc+'.sx', self.mirror_value)
        pv_zero, pv_ctrl, pv_offsets, pv_last_node = self.anim_ctrl(name, match_position=loc)

        name = prefix+'_leg_IK_switch_CTL'
        switch_zero, switch_ctrl, switch_offsets, switch_last_node = self.anim_ctrl(name)

        mc.delete(loc)

        up_leg_grp = mc.createNode('transform', n=up_leg_jnt+'_GRP', p=up_leg_jnt)
        mc.parent(up_leg_grp, jnt_grps[0])
        mc.parent(up_leg_jnt, up_leg_grp)

        # orient leg ik ctrl
        tmp_grp = mc.createNode('transform', p=leg_ik_ctrl)
        mc.parent(tmp_grp, w=1)

        mc.xform(leg_ik_zero, a=1, ro=[0,0,0])
        mc.setAttr(leg_ik_zero+'.s', self.mirror_value,1,1)

        utils.set_attrs(leg_ik_ctrl, 'jo', l=0)
        mc.parent(leg_ik_ctrl, leg_ik_ctrl+'_OFF')
        mc.delete(tmp_grp)

        if world_orient_trans == 'downBone':
            utils.set_attrs(leg_ik_ctrl+'_ZERO', 'ry', k=1, l=0)
            utils.set_attrs(leg_ik_ctrl, 'joy', k=1, l=0)
            mc.setAttr(leg_ik_ctrl+'_ZERO.ry', mc.getAttr(leg_ik_ctrl+'.joy'))

            utils.set_attrs(leg_ik_ctrl+'_ZERO', 'ry', k=0, l=1)
            utils.set_attrs(leg_ik_ctrl, 'joy', k=0, l=1)

        # Create lo leg IK
        tmp = mc.createNode('transform', p=leg_ik_ctrl)
        mc.delete(mc.aimConstraint(lo_leg_jnt, tmp, aim=[0,1,0], u=[0,0,1], wu=[0,0,1], wut='objectRotation', wuo=leg_ik_ctrl))
        mc.parent(tmp, w=1)

        name = prefix+'_loLeg_IK_CTL'
        lo_leg_ik_zero, lo_leg_ik_ctrl, lo_leg_ik_offsets, lo_leg_ik_last_node = self.anim_ctrl(name, match_position=tmp)
        mc.delete(tmp)

        mc.parent(lo_leg_ik_zero, leg_ik_last_node)
        for c in [lo_leg_ik_ctrl]+lo_leg_ik_offsets:
            mc.setAttr(c+'.ro', 1)

        # parent fk ctrls
        mc.parent(up_leg_fk_zero, leg_base_ctrl)
        mc.parent(mid_leg_fk_zero, up_leg_fk_ctrl)
        mc.parent(lo_leg_fk_zero, mid_leg_fk_ctrl)
        mc.parent(leg_end_fk_zero, lo_leg_fk_ctrl)

        # NOW create ik fk chain setup
        up_leg_ik_jnt = mc.duplicate(up_leg_jnt, po=1, n=up_leg_jnt.replace('upLeg', 'upLeg_IK'))[0]
        mid_leg_ik_jnt = mc.duplicate(mid_leg_jnt, po=1, n=mid_leg_jnt.replace('midLeg', 'midLeg_IK'))[0]
        lo_leg_ik_jnt = mc.duplicate(lo_leg_jnt, po=1, n=lo_leg_jnt.replace('loLeg', 'loLeg_IK'))[0]
        leg_end_ik_jnt = mc.duplicate(leg_end_jnt, po=1, n=leg_end_jnt.replace('leg_end', 'leg_end_IK'))[0]

        mc.parent(mid_leg_ik_jnt, up_leg_ik_jnt)
        mc.parent(lo_leg_ik_jnt, mid_leg_ik_jnt )
        mc.parent(leg_end_ik_jnt, lo_leg_ik_jnt)

        # Create second chain
        sec_up_leg_ik_jnt = mc.duplicate(up_leg_jnt, po=1, n=up_leg_jnt.replace('upLeg', 'upLeg_sec_IK'))[0]
        sec_mid_leg_ik_jnt = mc.duplicate(mid_leg_jnt, po=1, n=mid_leg_jnt.replace('midLeg', 'midLeg_sec_IK'))[0]
        sec_lo_leg_ik_jnt = mc.duplicate(lo_leg_jnt, po=1, n=lo_leg_jnt.replace('loLeg', 'loLeg_sec_IK'))[0]
        sec_leg_end_ik_jnt = mc.duplicate(leg_end_jnt, po=1, n=leg_end_jnt.replace('leg_end', 'leg_end_sec_IK'))[0]

        mc.parent(sec_mid_leg_ik_jnt, sec_up_leg_ik_jnt)
        mc.parent(sec_lo_leg_ik_jnt, sec_mid_leg_ik_jnt )
        mc.parent(sec_leg_end_ik_jnt, sec_lo_leg_ik_jnt)

        # orient condstrain upleg
        mc.parentConstraint(up_leg_fk_last_node, sec_up_leg_ik_jnt, mo=1)
        mc.parentConstraint(up_leg_fk_last_node, up_leg_ik_jnt, mo=1)
        mc.scaleConstraint(jnt_grps[0], up_leg_ik_jnt, mo=1)

        # connect the mid leg usuing orient contraint then direct connections to avoid cycling
        ori_par = mc.createNode('transform', p=mid_leg_jnt, n=mid_leg_jnt+'_orient_DRV_PAR')
        ori = mc.createNode('transform', p=ori_par, n=mid_leg_jnt+'_orient_DRV')
        mc.parent(ori_par, mid_leg_fk_zero)

        mc.orientConstraint(mid_leg_fk_ctrl, ori, mo=1)
        mc.connectAttr(ori+'.r', mid_leg_ik_jnt+'.r')
        mc.connectAttr(ori+'.r', sec_mid_leg_ik_jnt+'.r')

        # connect the midleg using orient contraint then direct connectns to avoid cycling
        ori_par = mc.createNode('transform', p=lo_leg_jnt, n=lo_leg_jnt+'_orient_DRV_PAR')
        ori = mc.createNode('transform', p=ori_par, n=lo_leg_jnt+'_orient_DRV')
        mc.parent(ori_par, lo_leg_fk_zero)

        mc.orientConstraint(lo_leg_fk_ctrl, ori, mo=1)
        mc.connectAttr(ori+'.r', lo_leg_ik_jnt+'.r')
        mc.connectAttr(ori+'.r', sec_lo_leg_ik_jnt+'.r')

        # Create spring ik handle
        mm.eval('ikSpringSolver')
        test = utils.snap_locator(mid_leg_ik_jnt)
        ik_handle = mc.ikHandle(sj=up_leg_ik_jnt,
                                ee=leg_end_ik_jnt,
                                s='sticky',
                                n=prefix+'_leg_IK',
                                sol='ikSpringSolver')[0]


        mc.poleVectorConstraint(pv_ctrl, ik_handle)

        # This is a test to correct the slight shift in PV
        i = 0
        while round(utils.get_distance(test, mid_leg_ik_jnt), 3)> 0.01 and i < 360:
            mc.setAttr(ik_handle+'.twist', i)
            i += 1

        if round(utils.get_distance(test, mid_leg_ik_jnt), 3) > 0.01:
            i = 0
            while round(utils.get_distance(test, mid_leg_ik_jnt), 3)> 0.01 and i > -360:
                mc.setAttr(ik_handle+'.twist', i)
                i -= 1

        mc.delete(test)

        # Create lo leg IK
        up_ik_handle = mc.ikHandle(sj=sec_up_leg_ik_jnt,
                                ee=sec_lo_leg_ik_jnt,
                                s='sticky',
                                n=prefix+'_sec_up_leg_IK')[0]

        lo_ik_handle = mc.ikHandle(sj=sec_lo_leg_ik_jnt,
                                ee=sec_leg_end_ik_jnt,
                                s='sticky',
                                n=prefix+'_sec_lo_leg_IK')[0]

        up_sec_pv = mc.createNode('transform', n=prefix+'_up_sec_PV', p=up_leg_ik_jnt)
        mc.delete(mc.pointConstraint(pv_ctrl, up_sec_pv))
        mc.setAttr(up_sec_pv+'.ty', 0)

        mc.poleVectorConstraint(up_sec_pv, up_ik_handle)

        i = 0
        test = utils.snap_locator(mid_leg_ik_jnt)
        while round(utils.get_distance(test, sec_mid_leg_ik_jnt), 3)> 0.01 and i < 360:
            mc.setAttr(up_ik_handle+'.twist', i)
            i += 1

        if round(utils.get_distance(test, sec_mid_leg_ik_jnt), 3) > 0.01:
            i = 0
            while round(utils.get_distance(test, sec_mid_leg_ik_jnt), 3)> 0.01 and i > -360:
                mc.setAttr(up_ik_handle+'.twist', i)
                i -= 1

        mc.delete(test)

        # Create ik switch and parent handles
        ikChain.create_fk_ik_switch(switch_ctrl, [ik_handle, up_ik_handle, lo_ik_handle], up_leg_fk_zero, [leg_ik_zero, pv_zero])

        mc.parent(ik_handle, lo_ik_handle, leg_ik_last_node)
        mc.parent(up_ik_handle, lo_leg_ik_last_node)
        mc.parentConstraint(lo_leg_ik_jnt, lo_leg_ik_zero, mo=1)

        mc.setAttr(switch_ctrl+'.IK', 1)
        mc.hide(ik_handle, lo_ik_handle, up_ik_handle)

        # Add bias and twist attrs
        mc.addAttr(leg_ik_ctrl, ln='bendBias', min=-1, max=1, k=1)
        mc.addAttr(leg_ik_ctrl, ln='twist', k=1)
        mc.addAttr(leg_ik_ctrl, ln='upTwist', k=1)

        # connect bias
        up_attr = ik_handle+'.springAngleBias[0].springAngleBias_FloatValue'
        lo_attr = ik_handle+'.springAngleBias[1].springAngleBias_FloatValue'
        tt = 'linear'

        mc.setDrivenKeyframe(up_attr, cd=leg_ik_ctrl+'.bendBias', dv=0, v=0.5, itt=tt, ott=tt)
        mc.setDrivenKeyframe(up_attr, cd=leg_ik_ctrl+'.bendBias', dv=-1, v=0, itt=tt, ott=tt)
        mc.setDrivenKeyframe(up_attr, cd=leg_ik_ctrl+'.bendBias', dv=1, v=1, itt=tt, ott=tt)

        mc.setDrivenKeyframe(lo_attr, cd=leg_ik_ctrl+'.bendBias', dv=0, v=0.5, itt=tt, ott=tt)
        mc.setDrivenKeyframe(lo_attr, cd=leg_ik_ctrl+'.bendBias', dv=-1, v=1, itt=tt, ott=tt)
        mc.setDrivenKeyframe(lo_attr, cd=leg_ik_ctrl+'.bendBias', dv=1, v=0, itt=tt, ott=tt)

        # Connect twist
        adl = mc.createNode('addDoubleLinear')
        mc.setAttr(adl+'.input1', mc.getAttr(ik_handle+'.twist'))
        mc.connectAttr(adl+'.output', ik_handle+'.twist')

        mc.connectAttr(leg_ik_ctrl+'.twist', adl+'.input2')
        if self.mirror_value < 0.0:
            utils.connect_negative(leg_ik_ctrl+'.twist', adl+'.input2')

        # Connect twist
        adl = mc.createNode('addDoubleLinear')
        mc.setAttr(adl+'.input1', mc.getAttr(up_ik_handle+'.twist'))
        mc.connectAttr(adl+'.output', up_ik_handle+'.twist')

        mc.connectAttr(leg_ik_ctrl+'.upTwist', adl+'.input2')
        if self.mirror_value < 0.0:
            utils.connect_negative(leg_ik_ctrl+'.upTwist', adl+'.input2')

        # Create soft ik
        ik_joints = [up_leg_ik_jnt, mid_leg_ik_jnt, lo_leg_ik_jnt, leg_end_ik_jnt]
        ik_ctrl = leg_ik_ctrl

        # case for IK hook
        ik_handle_grp = mc.createNode('transform', p=leg_ik_last_node, n=ik_handle+'_GRP')
        mc.parent(ik_handle_grp, jnt_grps[1])
        mc.parent(ik_handle, ik_handle_grp)
        mc.parentConstraint(leg_ik_last_node, hooks[1], mo=1)

        ik_handle_parent = ikChain.create_soft_ik(ik_ctrl, ik_joints, ik_handle)

        # Create IK wrist orient switch
        ik_ctrl_follow_par = mc.createNode('transform', n=sec_leg_end_ik_jnt+'_ik_follow_PAR', p=sec_leg_end_ik_jnt)
        fk_ctrl_follow_par = mc.createNode('transform', n=sec_leg_end_ik_jnt+'_fk_follow_PAR', p=sec_leg_end_ik_jnt)

        ik_ctrl_follow = mc.createNode('transform', n=sec_leg_end_ik_jnt+'_ik_follow', p=sec_leg_end_ik_jnt)
        fk_ctrl_follow = mc.createNode('transform', n=sec_leg_end_ik_jnt+'_fk_follow', p=sec_leg_end_ik_jnt)

        mc.parent(fk_ctrl_follow, fk_ctrl_follow_par)
        mc.parent(ik_ctrl_follow, ik_ctrl_follow_par)
        mc.parent(fk_ctrl_follow_par, leg_end_fk_ctrl)
        mc.parent(ik_ctrl_follow_par, leg_ik_last_node)

        oc = mc.orientConstraint(fk_ctrl_follow, ik_ctrl_follow, sec_leg_end_ik_jnt)[0]
        mc.setAttr(oc+'.interpType', 2)

        mc.connectAttr(switch_ctrl+'.IK', oc+'.w1', f=1)
        utils.connect_reverse(oc+'.w1', oc+'.w0')

        # setup leg base ctrl
        mc.pointConstraint(leg_base_last_node, up_leg_grp, mo=1)

        # Create twist
        if leg_twist_jnts:
            ikChain.upper_twist(utils.get_parent(sec_mid_leg_ik_jnt), sec_mid_leg_ik_jnt, sec_lo_leg_ik_jnt, mid_leg_jnt, lo_leg_jnt, leg_twist_jnts)
            ikChain.lower_twist(sec_lo_leg_ik_jnt, sec_leg_end_ik_jnt, lo_leg_jnt, lo_leg_twist_jnts, leg_end_jnt)

            ikChain.stretch_twist_jnts(sec_mid_leg_ik_jnt, sec_lo_leg_ik_jnt, leg_twist_jnts)
            ikChain.stretch_twist_jnts(sec_lo_leg_ik_jnt, sec_leg_end_ik_jnt, lo_leg_twist_jnts)

        else:
            mc.parentConstraint(sec_up_leg_ik_jnt, up_leg_jnt ,mo=1)
            mc.parentConstraint(sec_lo_leg_ik_jnt, lo_leg_jnt ,mo=1)
            mc.parentConstraint(sec_leg_end_ik_jnt, leg_end_jnt, mo=1)

        # Set up Stretch
        fk_ctrls = [up_leg_fk_ctrl, mid_leg_fk_ctrl, lo_leg_fk_ctrl, leg_end_fk_ctrl]
        jnts = [up_leg_ik_jnt, mid_leg_ik_jnt, lo_leg_ik_jnt, leg_end_ik_jnt]
        sec_jnts = [sec_up_leg_ik_jnt, sec_mid_leg_ik_jnt, sec_lo_leg_ik_jnt, sec_leg_end_ik_jnt]

        # ikChain.multi_joint_stretch(leg_ik_ctrl, leg_ik_last_node, switch_ctrl, fk_ctrls, jnts, ik_handle)

        for i in range(1, len(jnts), 1):
            mc.connectAttr(jnts[i]+'.tx', sec_jnts[i]+'.tx')

        # Create movable pivot to compensate lo leg ik stretch
        # piv = mc.createNode('transform', p=lo_leg_ik_ctrl+'_ZERO', n=lo_leg_ik_ctrl+'_piv_correct')
        # mc.connectAttr(piv+'.t', lo_leg_ik_ctrl+'.rotatePivot')
        # mc.connectAttr(piv+'.t', lo_leg_ik_ctrl+'.scalePivot')
        # mc.pointConstraint(leg_end_ik_jnt, piv)

        mc.pointConstraint(leg_end_ik_jnt, lo_ik_handle)

        # Create drive n-line shape for pv
        control.create_driven_shape(pv_ctrl, mid_leg_jnt, replace=False)

        # clean  up now
        mc.hide(up_leg_ik_jnt, sec_up_leg_ik_jnt)


        # mc.parentConstraint(leg_end_jnt, switch_zero, mo=1)
        mc.parentConstraint(ctrl_grps[0], switch_zero, mo=1)

        mc.parent(leg_base_zero, leg_ik_zero, pv_zero, switch_zero, ctrl_grps[0])

        utils.set_attrs([up_leg_fk_ctrl, mid_leg_fk_ctrl, leg_end_fk_ctrl, lo_leg_fk_ctrl], 't s v', l=1, k=0)
        utils.set_attrs([lo_leg_fk_ctrl, mid_leg_fk_ctrl], 'ro', l=1, k=0)
        utils.set_attrs(pv_ctrl, 'r s v ro', l=1, k=0)
        utils.set_attrs(switch_ctrl, 't r s v ro', l=1, k=0)
        utils.set_attrs(leg_base_ctrl, 's', l=1, k=0)

        utils.set_attrs(leg_ik_offsets+[leg_ik_ctrl, lo_leg_ik_ctrl], ' s v ro jo radius', l=1, k=0, cb=0)
        for c in leg_ik_offsets+[leg_ik_ctrl]:
            mc.setAttr(c+'.radius', k=0, cb=0)

        utils.set_attrs(lo_leg_ik_ctrl, 't', l=1, k=0, cb=0)

        # spaces
        spaces.tag(leg_ik_ctrl, default=2)
        spaces.tag(pv_ctrl, default=0)

        jnts = [up_leg_jnt]+leg_twist_jnts+[lo_leg_jnt]+leg_twist_jnts+[leg_end_jnt]
        # #utils.create_cfx_curves(jnts, self.prefix+'_'+self.part_type)

        # movable pivot
        # control.create_movable_pivot(leg_ik_ctrl, ctrl_type='joint')

        mc.parent(up_leg_ik_jnt, noxform_grp)

        # This finalizes guide and creates rig sets
        self.create_ctrl_set('FK', fk_ctrls)
        self.finalize_part()

        #Setup pickwalking
        pickWalk.attribute_tag(lo_leg_fk_ctrl, mid_leg_fk_ctrl)
        pickWalk.attribute_tag(mid_leg_fk_ctrl, up_leg_fk_ctrl)
        pickWalk.attribute_tag(leg_end_fk_ctrl, mid_leg_fk_ctrl)

        pickWalk.attribute_tag(pv_ctrl,leg_base_ctrl)
        pickWalk.attribute_tag(leg_ik_ctrl, lo_leg_ik_ctrl)
        pickWalk.attribute_tag(lo_leg_ik_ctrl, pv_ctrl)

        pickWalk.attribute_tag(leg_base_ctrl, pickWalk_parent)


        utils.set_attrs(up_leg_ik_jnt, l=0, k=1)

