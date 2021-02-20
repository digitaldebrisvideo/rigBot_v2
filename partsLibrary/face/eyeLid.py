# -*- rigBot: part -*-

from maya import OpenMaya as om
import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import rivet
from rigBot.partsLibrary import standardPart

class EyeLid(standardPart.StandardPart):
    """Eye lid modules. Build lid joints and spline list controls, master blink, lower and upper blink attributes..

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_head_JNT".
            :eyeJoint: (str) Eye joint. Defaults to "L_eye_A_JNT".
            :eyeCtrl: (str) Eye ctrl. Defaults to "L_eye_FK_CTL".
            :numberJoints: (int) Number joints. Defaults to 7.
            :upperLidEdgeLoop: (list) Edge loop for the upper lid line to place joints. Defaults to [].
            :lowerLidEdgeLoop: (list) Edge loop for the lower lid line to place joints. Defaults to []."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('parent', data_type='hook', default='C_head_JNT')
        self.add_option('eyeJoint', data_type='hook', default='L_eye_A_JNT')
        self.add_option('eyeCtrl', data_type='hook', default='L_eye_FK_CTL')
        self.add_option('numberJoints', data_type='int', default=7, min=1, rebuild_to_modify=True)

        self.add_option('upperLidEdgeLoop',
                        data_type='selection',
                        default=[],
                        tool_tip='Edge loop for the upper lid line to place joints.')

        self.add_option('lowerLidEdgeLoop',
                        data_type='selection',
                        default=[],
                        tool_tip='Edge loop for the lower lid line to place joints.')
        '''
        self.add_option('pickWalkParent',
                        data_type='hook',
                        default="L_eye_FK_CTL",
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")
        '''
    def build_guide(self, **kwargs):
        """This builds your guide. Use KWARGS to update any options at build time."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix              # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options = self.options            # Build options
        mirror_value = self.mirror_value  # 1.0 for left and center sided parts and -1.0 for right sided part.

        number_joints=options['numberJoints']

        # Start coding suckka !!
        upper_edge_loop = mc.ls(options.get('upperLidEdgeLoop'))
        lower_edge_loop = mc.ls(options.get('lowerLidEdgeLoop'))

        if mc.objExists(options.get('eyeJoint')):
            mc.delete(mc.parentConstraint(options.get('eyeJoint'), self.guide_master))

        if upper_edge_loop and lower_edge_loop:
            up_crv = utils.create_curve_from_edges(prefix+'_upperLid_crv', upper_edge_loop, spans=3)
            lo_crv = utils.create_curve_from_edges(prefix+'_lowerLid_crv', lower_edge_loop, spans=3)

        else:
            up_crv = mm.eval('curve -d 2 -p -2 0 0 -p -1 1 0 -p 0 1.3 0 -p 1 1 0 -p 2 0 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 3 ;')
            lo_crv = mm.eval('curve -d 2 -p -2 0 0 -p -1 -1 0 -p 0 -1.3 0 -p 1 -1 0 -p 2 0 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 3 ;')
            up_crv = mc.rename(up_crv, prefix+'_upperLid_crv')
            lo_crv = mc.rename(lo_crv, prefix+'_lowerLid_crv')

        # Create joints
        up_jnts_pos = utils.get_uniform_spacing_on_curve(up_crv, number_joints+2)
        lo_jnts_pos = utils.get_uniform_spacing_on_curve(lo_crv, number_joints+2)

        # Create corner jnts
        loc1 = utils.snap_locator([up_crv+'.cv[0]', lo_crv+'.cv[0]'])
        loc2 = utils.snap_locator([up_crv+'.cv[4]', lo_crv+'.cv[4]'])

        in_jnt_zero, in_jnt_plc, in_jnt = self.guide_joint('innerLid')
        out_jnt_zero, out_jnt_plc, out_jnt = self.guide_joint('outterLid')

        mc.delete(mc.pointConstraint(loc1, in_jnt_zero),loc1)
        mc.delete(mc.pointConstraint(loc2, out_jnt_zero),loc2)

        # eye Base jnt
        base_zero, base_plc = self.guide_joint('eyeLidBase', placer_only=True)
        mc.xform(base_zero, a=1, t=[0,0,0], ro=[0,0,0])
        self.tag_as_ref(base_plc)

        for i in range(number_joints):
            pos = up_jnts_pos[i+1]
            letter = utils.letters[i]
            jnt_zero, jnt_plc, jnt = self.guide_joint('upperLid_'+letter)
            mc.xform(jnt_zero, ws=1, t=pos)

        for i in range(number_joints):
            pos = lo_jnts_pos[i+1]
            letter = utils.letters[i]
            jnt_zero, jnt_plc, jnt = self.guide_joint('lowerLid_'+letter)
            mc.xform(jnt_zero, ws=1, t=pos)

        # Create ctrls
        loc = utils.snap_locator(in_jnt)
        mc.delete(mc.aimConstraint(out_jnt, loc, aim=[1*mirror_value,0,0], u=[1*mirror_value,0,0], wut='scene'))

        zero, ctrl = self.guide_ctrl('innerLid', shape='square', color='blue', scale=[0.02]*3, axis='Z')
        mc.xform(zero, ws=1, t=mc.xform(in_jnt, q=1, ws=1, t=1))
        mc.xform(zero, ws=1, ro=mc.xform(loc, q=1, ws=1, ro=1))
        mc.xform(zero, ws=1, ro=mc.xform(loc, q=1, ws=1, ro=1))
        mc.xform(ctrl+'.cv[*]', r=1, t=[0,0,0.02], ro=[0,0,45])
        mc.setAttr(utils.get_parent(ctrl)+'.sx', mirror_value)

        zero, ctrl = self.guide_ctrl('outterLid', shape='square', color='blue', scale=[0.02]*3, axis='Z')
        mc.xform(zero, ws=1, t=mc.xform(out_jnt, q=1, ws=1, t=1))
        mc.xform(zero, ws=1, ro=mc.xform(loc, q=1, ws=1, ro=1))
        mc.xform(zero, ws=1, ro=mc.xform(loc, q=1, ws=1, ro=1))
        mc.xform(ctrl+'.cv[*]', r=1, t=[0,0,0.02], ro=[0,0,45])
        mc.setAttr(utils.get_parent(ctrl)+'.sx', mirror_value)

        for i in range(1, 4, 1):
            ltr = utils.letters[i-1]
            cv = '{0}.cv[{1}]'.format(up_crv, i)
            zero, ctrl = self.guide_ctrl('upperLid_'+ltr, shape='square', color='blue', scale=[0.02]*3, axis='Z')
            mc.xform(zero, ws=1, t=mc.xform(cv, q=1, ws=1, t=1))
            mc.xform(zero, ws=1, ro=mc.xform(loc, q=1, ws=1, ro=1))
            mc.xform(ctrl+'.cv[*]', r=1, t=[0,0,0.02], ro=[0,0,45])
            mc.setAttr(utils.get_parent(ctrl)+'.sx', mirror_value)

        for i in range(1, 4, 1):
            ltr = utils.letters[i-1]
            cv = '{0}.cv[{1}]'.format(lo_crv, i)
            zero, ctrl = self.guide_ctrl('lowerLid_'+ltr, shape='square', color='blue', scale=[0.02]*3, axis='Z')
            mc.xform(zero, ws=1, t=mc.xform(cv, q=1, ws=1, t=1))
            mc.xform(zero, ws=1, ro=mc.xform(loc, q=1, ws=1, ro=1))
            mc.xform(ctrl+'.cv[*]', r=1, t=[0,0,0.02], ro=[0,0,45])
            mc.setAttr(utils.get_parent(ctrl)+'.sx', mirror_value)

        zero, ctrl = self.guide_ctrl('upperLidPrimary', shape='circle', color='blue', scale=[0.04]*3, axis='Z')
        mc.xform(zero, ws=1, t=mc.xform(up_crv+'.cv[2]', q=1, ws=1, t=1))
        mc.xform(zero, ws=1, ro=mc.xform(loc, q=1, ws=1, ro=1))
        mc.xform(zero, ws=1, ro=mc.xform(loc, q=1, ws=1, ro=1))
        mc.xform(ctrl+'.cv[*]', r=1, t=[0,0,0.02], ro=[0,0,45])
        mc.setAttr(utils.get_parent(ctrl)+'.sx', mirror_value)

        zero, ctrl = self.guide_ctrl('lowerLidPrimary', shape='circle', color='blue', scale=[0.04]*3, axis='Z')
        mc.xform(zero, ws=1, t=mc.xform(lo_crv+'.cv[2]', q=1, ws=1, t=1))
        mc.xform(zero, ws=1, ro=mc.xform(loc, q=1, ws=1, ro=1))
        mc.xform(zero, ws=1, ro=mc.xform(loc, q=1, ws=1, ro=1))
        mc.xform(ctrl+'.cv[*]', r=1, t=[0,0,0.02], ro=[0,0,45])
        mc.setAttr(utils.get_parent(ctrl)+'.sx', mirror_value)

        mc.delete(up_crv, lo_crv, loc)

        # This finalizes your guide.
        self.finalize_guide()

    def rebuild_guide_post(self):

        prefix = self.prefix
        mirror_value = self.mirror_value

        jnts = mc.ls(prefix+'_upperLid_*_JNT_PLC',
            prefix+'_lowerLid_*_JNT_PLC',
            prefix+'_innerLid_JNT_PLC',
            prefix+'_outterLid_JNT_PLC')

        mc.xform(jnts, a=1, t=[0,0,0], ro=[0,0,0])

    def build_rig(self):
        """This builds your anim rig."""

        def connect_blink_jnts(jnts, open_crv, blink_crv, blinkAttr, base_jnt):

            for jnt in jnts:

                # create mpx
                world_open_mpx = mc.createNode('transform', n=jnt+'_ompx_world', p=noxform_grp)
                world_blink_mpx = mc.createNode('transform', n=jnt+'_bmpx_world', p=noxform_grp)

                mc.delete(mc.pointConstraint(jnt, world_open_mpx))
                mc.delete(mc.pointConstraint(jnt, world_blink_mpx))

                open_mp = rivet.motionPath(world_open_mpx, open_crv)
                blink_mp = rivet.motionPath(world_blink_mpx, blink_crv)

                open_mpx = mc.duplicate(world_open_mpx, n=jnt+'_ompx', po=1)[0]
                wide_mpx = mc.duplicate(world_open_mpx, n=jnt+'_wmpx', po=1)[0]
                blink_mpx = mc.duplicate(world_blink_mpx, n=jnt+'_bmpx', po=1)[0]

                mc.pointConstraint(world_open_mpx, open_mpx)
                mc.pointConstraint(world_blink_mpx, blink_mpx)

                mc.parent(blink_mpx, open_mpx, base_jnt)
                mc.parent(wide_mpx, open_mpx)

                dist = utils.get_distance(open_mpx, blink_mpx)

                if 'upper' in jnt:
                    mc.xform(wide_mpx, r=1, t=[0, dist*1.3, -dist*0.3])
                else:
                    mc.xform(wide_mpx, r=1, t=[0, -dist*1.3, -dist*0.3])

                jnt_aim_zero = mc.createNode('transform', n=jnt+'_ZERO', p=lid_base_grp)
                jnt_aim_par = mc.createNode('transform', n=jnt+'_PAR', p=lid_base_grp)

                mc.parent(jnt_aim_par, jnt_aim_zero)


                mc.delete(
                    mc.aimConstraint(
                    open_mpx,
                    blink_mpx,
                    jnt_aim_zero,
                    n=jnt_aim_par+'_ac',
                    aim=[mirror_value, 0, 0],
                    u=[0,1,0],
                    wu=[0,1,0],
                    wut='objectRotation',
                    wuo=lid_base_grp))

                ac = mc.aimConstraint(
                    wide_mpx,
                    open_mpx,
                    blink_mpx,
                    jnt_aim_par,
                    n=jnt_aim_par+'_ac',
                    aim=[mirror_value, 0, 0],
                    u=[0,0,1],
                    wu=[0,0,1],
                    wut='objectRotation',
                    wuo=jnt_aim_zero)[0]

                clamp = mc.createNode('clamp')

                mc.setAttr(clamp+'.max', 1,1,1)
                mc.connectAttr(clamp+'.outputR', ac+'.w2')
                utils.connect_reverse(ac+'.w2', ac+'.w1')

                tt = 'linear'

                mc.setDrivenKeyframe(clamp+'.inputR', dv=1, v=1, cd=eye_ctrl_hook+'.blink', itt=tt, ott=tt)
                mc.setDrivenKeyframe(clamp+'.inputR', dv=0, v=0, cd=eye_ctrl_hook+'.blink', itt=tt, ott=tt)
                mc.setDrivenKeyframe(clamp+'.inputR', dv=1, v=1, cd=eye_ctrl_hook+'.'+blinkAttr, itt=tt, ott=tt)
                mc.setDrivenKeyframe(clamp+'.inputR', dv=0, v=0, cd=eye_ctrl_hook+'.'+blinkAttr, itt=tt, ott=tt)

                mc.setDrivenKeyframe(ac+'.w0', dv=0, v=0, cd=eye_ctrl_hook+'.blink', itt=tt, ott=tt)
                mc.setDrivenKeyframe(ac+'.w0', dv=-1, v=1, cd=eye_ctrl_hook+'.blink', itt=tt, ott=tt)
                mc.setDrivenKeyframe(ac+'.w0', dv=0, v=0, cd=eye_ctrl_hook+'.'+blinkAttr, itt=tt, ott=tt)
                mc.setDrivenKeyframe(ac+'.w0', dv=-1, v=1, cd=eye_ctrl_hook+'.'+blinkAttr, itt=tt, ott=tt)

                mc.parent(jnt, jnt_aim_par)

            mc.connectAttr(clamp+'.outputR', eye_ctrl_hook+'.'+blinkAttr+'Output')

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

        number_joints = options.get('numberJoints')
        #pickWalk_parent = options.get('pickWalkParent')
        # Create ctrls
        in_zero, in_ctrl, in_offsets, in_last_node = self.anim_ctrl(prefix+'_innerLid_CTL')
        out_zero, out_ctrl, out_offsets, out_last_node = self.anim_ctrl(prefix+'_outterLid_CTL')

        up_a_zero, up_a_ctrl, up_a_offsets, up_a_last_node = self.anim_ctrl(prefix+'_upperLid_A_CTL')
        up_b_zero, up_b_ctrl, up_b_offsets, up_b_last_node = self.anim_ctrl(prefix+'_upperLid_B_CTL')
        up_c_zero, up_c_ctrl, up_c_offsets, up_c_last_node = self.anim_ctrl(prefix+'_upperLid_C_CTL')

        lo_a_zero, lo_a_ctrl, lo_a_offsets, lo_a_last_node = self.anim_ctrl(prefix+'_lowerLid_A_CTL')
        lo_b_zero, lo_b_ctrl, lo_b_offsets, lo_b_last_node = self.anim_ctrl(prefix+'_lowerLid_B_CTL')
        lo_c_zero, lo_c_ctrl, lo_c_offsets, lo_c_last_node = self.anim_ctrl(prefix+'_lowerLid_C_CTL')

        up_pri_zero, up_pri_ctrl, up_pri_offsets, up_pri_last_node = self.anim_ctrl(prefix+'_upperLidPrimary_CTL')
        lo_pri_zero, lo_pri_ctrl, lo_pri_offsets, lo_pri_last_node = self.anim_ctrl(prefix+'_lowerLidPrimary_CTL')

        # Create curves
        up_jnts = mc.ls(prefix+'_innerLid_JNT', prefix+'_upperLid_*_JNT', prefix+'_outterLid_JNT', type='joint')
        lo_jnts = mc.ls(prefix+'_innerLid_JNT', prefix+'_lowerLid_*_JNT', prefix+'_outterLid_JNT', type='joint')

        parent_hook = hooks[0]
        eye_jnt_hook = hooks[1]
        eye_ctrl_hook = hooks[2]

        # add attrs
        mc.addAttr(eye_ctrl_hook,ln='blink',at='double', min=-1, max=1, k=1)
        mc.addAttr(eye_ctrl_hook,ln='upperBlink',at='double', min=-1, max=1, k=1)
        mc.addAttr(eye_ctrl_hook,ln='lowerBlink',at='double', min=-1, max=1, k=1)
        mc.addAttr(eye_ctrl_hook,ln='blinkLine',at='double', min=-1, max=1, k=1)
        mc.addAttr(eye_ctrl_hook,ln='blinkBias',at='double', min=-1, max=1, k=1)
        mc.addAttr(eye_ctrl_hook,ln='blinkSlant',at='double', k=1)
        mc.addAttr(eye_ctrl_hook,ln='eyeBallInfluence',at='double', min=0, max=1, k=1, dv=.2)
        mc.addAttr(eye_ctrl_hook,ln='upperBlinkOutput',at='double', k=1)
        mc.addAttr(eye_ctrl_hook,ln='lowerBlinkOutput',at='double', min=-1, max=1, k=1)

        # create curves
        arg = 'curve -d 2 '
        for j in up_jnts:
            x = mc.xform(j, ws=1, t=1, q=1)
            arg += ' -p {0} {1} {2}'.format(x[0], x[1],x[2])
        up_crv = mc.rename(mm.eval(arg), prefix+'_upperLid_crv')
        mm.eval('rebuildCurve -ch 0 -rpo 1 -rt 0 -end 1 -kr 0 -kcp 0 -kep 1 -kt 0 -s 3 -d 2 -tol 0.01 "{0}";'.format(up_crv))

        arg = 'curve -d 2 '
        for j in lo_jnts:
            x = mc.xform(j, ws=1, t=1, q=1)
            arg += ' -p {0} {1} {2}'.format(x[0], x[1],x[2])
        lo_crv = mc.rename(mm.eval(arg), prefix+'_lowerLid_crv')
        mm.eval('rebuildCurve -ch 0 -rpo 1 -rt 0 -end 1 -kr 0 -kcp 0 -kep 1 -kt 0 -s 3 -d 2 -tol 0.01 "{0}";'.format(lo_crv))

        up_blink_crv = mc.duplicate(up_crv, n=prefix+'_upperBlink_crv')[0]
        lo_blink_crv = mc.duplicate(lo_crv, n=prefix+'_lowerBlink_crv')[0]

        #create blend for upper and lower blink curves
        avcs = []
        for bcrv in [up_blink_crv, lo_blink_crv]:
            avc = mc.createNode('avgCurves', n=bcrv+'_avc')
            mc.connectAttr(up_crv+'Shape.worldSpace', avc+'.ic1')
            mc.connectAttr(lo_crv+'Shape.worldSpace', avc+'.ic2')
            mc.connectAttr(avc+'.oc', bcrv+'Shape.create')
            mc.setAttr(avc+'.automaticWeight', 0)
            avcs.append(avc)

        # This is the blink bias - it overshoots or under shoots the blink to allow you to create a better seal.
        mc.setAttr(eye_ctrl_hook+'.blinkBias', 0)
        mc.setAttr(eye_ctrl_hook+'.blinkLine', 0)

        tt = 'linear'
        up_avc = avcs[0]
        lo_avc = avcs[1]

        mc.setDrivenKeyframe([up_avc+'.w1', up_avc+'.w2'], cd=eye_ctrl_hook+'.blinkBias', itt=tt, ott=tt, dv=0)
        mc.setDrivenKeyframe([lo_avc+'.w1', lo_avc+'.w2'], cd=eye_ctrl_hook+'.blinkBias', itt=tt, ott=tt, dv=0)

        mc.setAttr(up_avc+'.w1', 0)
        mc.setAttr(up_avc+'.w2', 1)
        mc.setAttr(lo_avc+'.w1', 1)
        mc.setAttr(lo_avc+'.w2', 0)
        mc.setDrivenKeyframe([up_avc+'.w1', up_avc+'.w2'], cd=eye_ctrl_hook+'.blinkBias', itt=tt, ott=tt, dv=1)
        mc.setDrivenKeyframe([lo_avc+'.w1', lo_avc+'.w2'], cd=eye_ctrl_hook+'.blinkBias', itt=tt, ott=tt, dv=1)

        mc.setAttr(up_avc+'.w1', 1)
        mc.setAttr(up_avc+'.w2', 0)
        mc.setAttr(lo_avc+'.w1', 0)
        mc.setAttr(lo_avc+'.w2', 1)
        mc.setDrivenKeyframe([up_avc+'.w1', up_avc+'.w2'], cd=eye_ctrl_hook+'.blinkBias', itt=tt, ott=tt, dv=-1)
        mc.setDrivenKeyframe([lo_avc+'.w1', lo_avc+'.w2'], cd=eye_ctrl_hook+'.blinkBias', itt=tt, ott=tt, dv=-1)

        # connect blink blend
        mc.setAttr(eye_ctrl_hook+'.blinkBias', 1)
        mc.setAttr(eye_ctrl_hook+'.blinkBias', 0)
        mc.setDrivenKeyframe(up_avc+'.w1', dv=1, v=1.5, cd=eye_ctrl_hook+'.blinkLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(up_avc+'.w1', dv=-1, v=-0.5, cd=eye_ctrl_hook+'.blinkLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(up_avc+'.w2', dv=1, v=-0.5, cd=eye_ctrl_hook+'.blinkLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(up_avc+'.w2', dv=-1, v=1.5, cd=eye_ctrl_hook+'.blinkLine', itt=tt, ott=tt)

        mc.setDrivenKeyframe(lo_avc+'.w1', dv=1, v=1.5, cd=eye_ctrl_hook+'.blinkLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(lo_avc+'.w1', dv=-1, v=-0.5, cd=eye_ctrl_hook+'.blinkLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(lo_avc+'.w2', dv=1, v=-0.5, cd=eye_ctrl_hook+'.blinkLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(lo_avc+'.w2', dv=-1, v=1.5, cd=eye_ctrl_hook+'.blinkLine', itt=tt, ott=tt)
        mc.setAttr(eye_ctrl_hook+'.blinkLine', 0)
        mc.setAttr(eye_ctrl_hook+'.blinkBias', 0)

        # create eyeball blend
        base_ref = prefix+'_eyeLidBase_JNT_PLC_REF'
        lid_base_grp = mc.createNode('transform', p=base_ref, n=prefix+'_eyeLidBase_GRP')

        mc.parent(lid_base_grp, jnt_grps[0])

        base_static = mc.duplicate(lid_base_grp, po=1, n=prefix+'_eyeLidBase_static_GRP')[0]
        ctrls_base_grp = mc.duplicate(lid_base_grp, po=1, n=prefix+'_eyeLidBase_GRP')[0]
        ctrls_slant_grp = mc.duplicate(lid_base_grp, po=1, n=prefix+'_eyeLidSlant_GRP')[0]

        mc.parent(ctrls_slant_grp, ctrls_base_grp)

        base_follow_par = mc.duplicate(lid_base_grp, po=1, n=prefix+'_eyeLidBase_follow_PAR')[0]
        base_follow = mc.duplicate(lid_base_grp, po=1, n=prefix+'_eyeLidBase_follow_GRP')[0]
        mc.parent(base_follow, base_follow_par)
        mc.parent(base_follow_par, jnt_grps[1])

        oc = mc.orientConstraint(base_static, base_follow, lid_base_grp, n=lid_base_grp+'_oc')[0]
        mc.setAttr(oc+'.interpType', 2)

        mc.setDrivenKeyframe(oc+'.w1', dv=0, v=0, cd=eye_ctrl_hook+'.eyeBallInfluence')
        mc.setDrivenKeyframe(oc+'.w1', dv=1, v=1, cd=eye_ctrl_hook+'.eyeBallInfluence')
        mc.setDrivenKeyframe(oc+'.w0', dv=1, v=0, cd=eye_ctrl_hook+'.eyeBallInfluence')
        mc.setDrivenKeyframe(oc+'.w0', dv=0, v=1, cd=eye_ctrl_hook+'.eyeBallInfluence')

        mc.parent(ctrls_base_grp, ctrl_grps[0])
        mc.parentConstraint(lid_base_grp, ctrls_base_grp, n=ctrls_base_grp+'_prc')

        # parent ctrls
        mc.parent(up_a_zero, up_b_zero, up_c_zero, up_pri_ctrl)
        mc.parent(lo_a_zero, lo_b_zero, lo_c_zero, lo_pri_ctrl)
        mc.parent(up_pri_zero, lo_pri_zero, ctrls_slant_grp)

        slant_corner_par = mc.duplicate(ctrls_slant_grp, n=ctrls_slant_grp+'_corner_PAR', po=1)[0]
        slant_corner_grp = mc.createNode('transform', p=slant_corner_par, n=ctrls_slant_grp+'_corner_GRP')

        mc.parent(slant_corner_par, ctrl_grps[0])
        mc.parent(in_zero, out_zero, slant_corner_grp)

        mc.connectAttr(eye_ctrl_hook+'.blinkSlant', slant_corner_grp+'.rx')
        mc.connectAttr(eye_ctrl_hook+'.blinkSlant', ctrls_slant_grp+'.rx')

        # parent crvs
        mc.parent(up_crv, lo_crv, up_blink_crv, lo_blink_crv, noxform_grp)

        # Constrain sub ctrls
        up_prc = mc.parentConstraint(in_zero, up_pri_ctrl, up_a_zero, n=up_a_zero+'_prc', mo=1)[0]
        lo_prc = mc.parentConstraint(in_zero, lo_pri_ctrl, lo_a_zero, n=lo_a_zero+'_prc', mo=1)[0]
        mc.setAttr(up_prc+'.interpType', 2)
        mc.setAttr(lo_prc+'.interpType', 2)

        up_prc = mc.parentConstraint(out_zero, up_pri_ctrl, up_c_zero, n=up_c_zero+'_prc', mo=1)[0]
        lo_prc = mc.parentConstraint(out_zero, lo_pri_ctrl, lo_c_zero, n=lo_c_zero+'_prc', mo=1)[0]
        mc.setAttr(up_prc+'.interpType', 2)
        mc.setAttr(lo_prc+'.interpType', 2)

        # connect curves to ctrls
        up_cvs = mc.ls(up_crv+'.cv[*]', fl=1)
        up_ctrls = [in_ctrl, up_a_ctrl, up_b_ctrl, up_c_ctrl, out_ctrl]

        lo_cvs = mc.ls(lo_crv+'.cv[*]', fl=1)
        lo_ctrls = [in_ctrl, lo_a_ctrl, lo_b_ctrl, lo_c_ctrl, out_ctrl]

        for i, cv in enumerate(up_cvs):

            cv_offset = mc.createNode('transform', p=up_ctrls[i], n=up_ctrls[i]+'_cv_GRP')
            pos = mc.xform(cv, q=1, ws=1, t=1)
            mc.xform(cv_offset, ws=1, t=pos)

            dcmx = mc.createNode('decomposeMatrix')
            mc.connectAttr(cv_offset+'.worldMatrix', dcmx+'.inputMatrix')
            cPoint = '{0}.controlPoints[{1}]'.format(up_crv, i)
            mc.connectAttr(dcmx+'.outputTranslate', cPoint)

        for i, cv in enumerate(lo_cvs):

            cv_offset = mc.createNode('transform', p=lo_ctrls[i], n=lo_ctrls[i]+'_cv_GRP')
            pos = mc.xform(cv, q=1, ws=1, t=1)
            mc.xform(cv_offset, ws=1, t=pos)

            dcmx = mc.createNode('decomposeMatrix')
            mc.connectAttr(cv_offset+'.worldMatrix', dcmx+'.inputMatrix')
            cPoint = '{0}.controlPoints[{1}]'.format(lo_crv, i)
            mc.connectAttr(dcmx+'.outputTranslate', cPoint)

        # Connect joints to motion path
        connect_blink_jnts(up_jnts, up_crv, up_blink_crv, 'upperBlink', jnt_grps[0])
        connect_blink_jnts(lo_jnts[1:-1], lo_crv, lo_blink_crv, 'lowerBlink', jnt_grps[0])

        '''
        # negative blink values
        dst = utils.get_distance(up_crv+'.cv[2]', up_blink_crv+'.cv[2]')
        mc.setDrivenKeyframe (up_pri_ctrl+'_CONST.t', cd=eye_ctrl_hook+'.upperBlink', dv=0, itt='flat', ott='flat')
        mc.setDrivenKeyframe (lo_pri_ctrl+'_CONST.t', cd=eye_ctrl_hook+'.lowerBlink', dv=0, itt='flat', ott='flat')

        mc.setDrivenKeyframe (up_pri_ctrl+'_CONST.t', cd=eye_ctrl_hook+'.blink', dv=0, itt='flat', ott='flat')
        mc.setDrivenKeyframe (lo_pri_ctrl+'_CONST.t', cd=eye_ctrl_hook+'.blink', dv=0, itt='flat', ott='flat')

        mc.xform(up_pri_ctrl+'_CONST', r=1, t=[0, dst, -dst*0.5])
        mc.xform(lo_pri_ctrl+'_CONST', r=1, t=[0, -dst, -dst*0.5])
        mc.setDrivenKeyframe (up_pri_ctrl+'_CONST.t', cd=eye_ctrl_hook+'.upperBlink', dv=-1, itt=tt, ott='flat')
        mc.setDrivenKeyframe (lo_pri_ctrl+'_CONST.t', cd=eye_ctrl_hook+'.lowerBlink', dv=-1, itt=tt, ott='flat')
        mc.setDrivenKeyframe (up_pri_ctrl+'_CONST.t', cd=eye_ctrl_hook+'.blink', dv=-1, itt=tt, ott='flat')
        mc.setDrivenKeyframe (lo_pri_ctrl+'_CONST.t', cd=eye_ctrl_hook+'.blink', dv=-1, itt=tt, ott='flat')

        mc.setAttr(eye_ctrl_hook+'.blink', 1)
        mc.setAttr(eye_ctrl_hook+'.blink', 0)
        mc.setAttr(eye_ctrl_hook+'.blinkLine', 1)
        mc.setAttr(eye_ctrl_hook+'.blinkLine', 0)
        mc.setAttr(eye_ctrl_hook+'.blinkBias', 1)
        mc.setAttr(eye_ctrl_hook+'.blinkBias', 0)
        mc.setAttr(eye_ctrl_hook+'.upperBlink', 1)
        mc.setAttr(eye_ctrl_hook+'.upperBlink', 0)
        mc.setAttr(eye_ctrl_hook+'.lowerBlink', 1)
        mc.setAttr(eye_ctrl_hook+'.lowerBlink', 0)

        '''

        mc.setAttr(eye_ctrl_hook+'.blink', 0)
        mc.setAttr(eye_ctrl_hook+'.blinkLine', 0)
        mc.setAttr(eye_ctrl_hook+'.blinkBias', 0)
        mc.setAttr(eye_ctrl_hook+'.upperBlink', 0)
        mc.setAttr(eye_ctrl_hook+'.lowerBlink', 0)

        # Create driven shape
        drv_ctrls = [in_ctrl, up_a_ctrl, up_b_ctrl, up_c_ctrl, out_ctrl]
        control.create_driven_shape(up_pri_ctrl, drv_ctrls, replace=1)

        drv_ctrls = [in_ctrl, lo_a_ctrl, lo_b_ctrl, lo_c_ctrl, out_ctrl]
        control.create_driven_shape(lo_pri_ctrl, drv_ctrls, replace=1)

        # Hide ctrvs
        mc.hide(up_crv, lo_crv, up_blink_crv, lo_blink_crv)
        mc.setAttr(eye_ctrl_hook+'.upperBlinkOutput', l=1)
        mc.setAttr(eye_ctrl_hook+'.lowerBlinkOutput', l=1)

        #setup pickwalking

        '''
        for ctrl in lo_ctrls:
            pickWalk.attribute_tag(ctrl,lo_pri_ctrl)
        for ctrl in up_ctrls:
            pickWalk.attribute_tag(ctrl,up_pri_ctrl)

        pickWalk.attribute_tag(up_pri_ctrl,pickWalk_parent)
        pickWalk.attribute_tag(lo_pri_ctrl,pickWalk_parent)
        '''
        # This finalizes the rig and creates rig sets
        self.finalize_part()


