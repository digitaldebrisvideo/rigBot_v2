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

class CrabLeg(standardPart.StandardPart):
    """This is an empty part. It only builds a guide master and empty rig hooks.
        Format your options in the docs as follows for proper auto-documentation.
        OR Generate auto doc strings.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_hip_JNT".

        Note:
            AFTER you've added your options and their values. You can automatically generate doc strings using:
                ``from rigBot import guide``
                ``guide.generate_doc_string('MODULE_NAME')``."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)
        self.add_option('parent', data_type='hook', default='C_hip_JNT')
        self.add_option('name', default='leg', required=True)

        self.add_option('numberJoints',
                    data_type='int',
                    default=5,
                    min=3,
                    max=None,
                    rebuild_to_modify=True)

        self.add_option('pickWalkParent',
                    data_type='string',
                    default="C_cog_CTL",
                    selectable=True,
                    tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide. Use Keyword to update any options at build time."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix              # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options = self.options            # Build options
        mirror_value = self.mirror_value  # 1.0 for left and center sided parts and -1.0 for right sided part.

        num_joints = options.get('numberJoints')

        color = 'green'
        if self.mirror_value == -1:
            color = 'red'

        # Ctrate jnts
        jnt_zeros, plcs, jnts = self.guide_joint_chain('leg', num_joints=num_joints+1)

        mc.xform(jnt_zeros[0], ws=1, t=[1.0, 0.0, 0.0])
        mc.xform(jnt_zeros[0], ws=1, ro=[0.0, 0.0, 0.0])

        mc.xform(jnt_zeros[1], ws=1, t=[1.658529, -0.393384, 0.0])
        mc.xform(jnt_zeros[1], ws=1, ro=[0.0, 0.0, 0.0])

        for i, zero in enumerate(jnt_zeros[2:]):
            mc.xform(zero, r=1, t=[0, -i*(i*0.3), 0])

        # Create FK ctrls
        zeros, ctrls = [], []
        for i, jnt in enumerate(jnts[:-1]):
            letter = utils.letters[i]
            zero, ctrl = self.guide_ctrl(name=letter, shape='circle',
                                         color='light_blue', driver=jnt, axis='X')
            zeros.append(zero)
            ctrls.append(ctrl)

        mc.xform(zeros, jnt_zeros, r=1, t=[-1*self.mirror_value, 0, 0])


        # Create IK ctrls
        base_zero, base_ctrl = self.guide_ctrl(name='legBase', shape='pyramid', color=color, driver=jnts[0], axis='X', scale=[0.5]*3)
        leg_zero, leg_ctrl = self.guide_ctrl(name='leg_IK_switch', shape='sphere', color=color, driver=jnts[-1], axis='X', create_pivot=0)
        pv_zero, pv_ctrl = self.guide_ctrl(name='knee_IK', shape='cube', color=color, axis='X', scale=[0.3]*3, create_pivot=0)
        lo_knee_zero, lo_knee_ctrl = self.guide_ctrl(name='lo_knee', shape='circle', driver=jnts[-2], scale=[1.2]*3, color=color, axis='Z', create_pivot=0)

        switch_zero, switch_ctrl = self.guide_ctrl(name='leg_IK_switch', shape='pin_gear', color='lavendar', driver=jnts[-1])
        mc.xform(switch_ctrl, r=1, ro=[0,0,180])
        mc.makeIdentity(switch_ctrl, apply=1, t=1, r=1, s=1, n=0, pn=1)
        mc.setAttr(leg_ctrl+'.numOffsetCtrls', 1)

        mc.pointConstraint(jnts[0], pv_zero)
        mc.xform(pv_ctrl+'_CONST', r=1, t=[0,3,0])

        line = mc.createNode('transform', n=pv_ctrl+'_line_REF', p=utils.get_parent(pv_zero))
        control.create_driven_shape(line, [pv_ctrl, jnts[0]])
        utils.set_draw_override(line, 1)

        # This finalizes your guide.
        mc.setAttr(self.guide_master+'.offsetTranslateY', -self.mirror_value*0.25)
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

        #create Ctrls
        pick_walk_parent = options.get('pickWalkParent')
        num_jnts = options.get('numberJoints')
        parent = options.get('parent')

        jnts = []
        for i in range(num_jnts+1):
            jnts.append(prefix+'_leg_'+utils.letters[i]+'_JNT')

        name = prefix+'_legBase_CTL'
        leg_base_zero, leg_base_ctrl, leg_base_offsets, leg_base_last_node = self.anim_ctrl(name)

        name = prefix+'_lo_knee_CTL'
        lo_knee_zero, lo_knee_ctrl, lo_knee_offsets, lo_knee_last_node = self.anim_ctrl(name, match_position=jnts[-1])

        name = prefix+'_knee_IK_CTL'
        l = utils.snap_locator(name+'_REF')
        knee_zero, knee_ctrl, knee_offsets, knee_last_node = self.anim_ctrl(name, match_position=l)

        name = prefix+'_leg_IK_CTL'
        leg_ik_zero, leg_ik_ctrl, leg_ik_offsets, leg_ik_last_node = self.anim_ctrl(name, node_type='joint')

        name = prefix+'_leg_IK_switch_CTL'
        switch_zero, switch_ctrl, switch_offsets, switch_last_node = self.anim_ctrl(name)

        mc.setAttr(leg_ik_zero+'.sx', self.mirror_value)
        mc.setAttr(knee_zero+'.sx', self.mirror_value)

        mc.delete(l)

        mc.xform(leg_ik_ctrl+'_ZERO', ws=1, ro=[0,0,0])
        mc.parent(lo_knee_zero, leg_ik_last_node)

        fk_zeros, fk_ctrls, fk_offsets, fk_last_ndoes = [],[],[],[]

        for i, jnt in enumerate(jnts[:-1]):
            name = prefix+'_'+utils.letters[i]+'_CTL'
            ct = self.anim_ctrl(name, match_position=l)

            if fk_ctrls:
                mc.parent(ct[0], fk_last_ndoes[-1])

            fk_zeros.append(ct[0])
            fk_ctrls.append(ct[1])
            fk_offsets.append(ct[2])
            fk_last_ndoes.append(ct[3])

        #create duplicate chain and setup IK
        pri_jnts = []
        for j in jnts:
            nj = mc.duplicate(j, n=j.replace('_leg_', '_priLeg_'), po=1)[0]
            if pri_jnts:
                mc.parent(nj, pri_jnts[-1])

            pri_jnts.append(nj)

        mc.setAttr(pri_jnts[-1]+'.jo', 0,0,0)
        mc.setAttr(jnts[-1]+'.jo', 0,0,0)

        # parent jnts and ctrls
        mc.parent(pri_jnts[0], jnts[0], jnt_grps[0])
        mc.parent(leg_base_zero, leg_ik_zero, knee_zero, switch_zero, fk_zeros[0], ctrl_grps[0])

        # constraint all fk ctrls
        for i in range(len(fk_ctrls)):
            mc.orientConstraint(fk_last_ndoes[i], jnts[i])

        # Create IKs
        pri_ik = mc.ikHandle(sj=pri_jnts[0], ee=pri_jnts[-1], n=prefix+'_pri_IK', s='sticky', ap=1)[0]
        ik0 = mc.ikHandle(sj=jnts[0], ee=jnts[1], n=prefix+'_subA_IK', s='sticky', ap=1, sol='ikSCsolver')[0]
        ik1 = mc.ikHandle(sj=jnts[1], ee=jnts[-2], n=prefix+'_subB_IK', s='sticky', ap=1)[0]
        ik2 = mc.ikHandle(sj=jnts[-2], ee=jnts[-1], n=prefix+'_subC_IK', s='sticky', ap=1, sol='ikSCsolver')[0]

        mc.parent(pri_ik, leg_ik_last_node)
        mc.parent(ik0, leg_base_ctrl)
        mc.parent(ik1, lo_knee_last_node)
        mc.parent(ik2, pri_jnts[-1])

        mc.pointConstraint(leg_base_last_node, jnts[0])
        mc.parentConstraint(pri_jnts[-2], lo_knee_zero, mo=1)
        mc.parentConstraint(jnts[-1], switch_zero, mo=1)

        # primary pv
        l = utils.snap_locator(pri_jnts[2])
        mc.poleVectorConstraint(knee_last_node, pri_ik)
        tol = max(utils.get_distance(pri_jnts[2], l)*0.001, 0.001)
        test_twist(pri_jnts[2], pri_ik, l, tol)

        # setup ik pv for center ik handle
        pv = mc.createNode('transform',n=prefix+'_leg_loIk_PV', p=jnts[1])
        mc.xform(pv, r=1, t=[0,0,-self.mirror_value*utils.get_distance(jnts[1], jnts[-2])])
        mc.parent(pv, pri_jnts[2])

        l = utils.snap_locator(jnts[2])
        mc.poleVectorConstraint(pv, ik1)
        tol = max(utils.get_distance(jnts[2], l)*0.001, 0.001)
        test_twist(jnts[2], ik1, l, tol)

        # leg base space
        dup0 = mc.duplicate(leg_base_zero, n=leg_base_ctrl+'_DRV_PAR', po=1)[0]
        dup = mc.duplicate(leg_base_ctrl, n=leg_base_ctrl+'_DRV', po=1)[0]
        mc.parent(dup0, pri_jnts[0])
        mc.parent(dup, dup0)

        oc = mc.orientConstraint(dup, leg_base_ctrl+'_CONST', leg_base_ctrl+'_MOCAP', mo=1)[0]
        mc.addAttr(leg_base_ctrl, ln='legInfluence', min=0, max=1, dv=1, k=1)
        mc.setAttr(oc+'.interpType', 2)

        mc.connectAttr(leg_base_ctrl+'.legInfluence', oc+'.w0', f=1)
        utils.connect_reverse(leg_base_ctrl+'.legInfluence', oc+'.w1')

        mc.hide(ik0, ik1, ik2, pri_ik, pri_jnts)

        # connect ik and twist
        ikChain.create_fk_ik_switch(switch_ctrl, [ik0, ik1, ik2], fk_zeros[0], [knee_zero, leg_base_zero, lo_knee_zero, leg_ik_zero])

        mc.addAttr(leg_ik_ctrl, ln='twist', k=1)
        adl = mc.createNode('addDoubleLinear')
        mc.setAttr(adl+'.i2', mc.getAttr(pri_ik+'.twist'))
        mc.connectAttr(leg_ik_ctrl+'.twist', adl+'.i1')
        mc.connectAttr(adl+'.o', pri_ik+'.twist')

        mc.setAttr(switch_ctrl+'.IK', 1)

        # soft ik and stretch
        par_grp = utils.snap_locator(pri_jnts[0], name=prefix+'_joints_root_GRP', node_type='transform')
        mc.parent(par_grp, jnt_grps[0])
        mc.parent(pri_jnts[0], jnts[0], par_grp)

        ik_handle_parent = ikChain.create_soft_ik(leg_ik_ctrl, pri_jnts, pri_ik)

        last = control.create(prefix+'_last_GRP', shape=None)
        mc.parent(last[0], fk_last_ndoes[-1])
        ikChain.multi_joint_stretch(leg_ik_ctrl, leg_ik_last_node, switch_ctrl, fk_ctrls+[last[-1]], pri_jnts, pri_ik)

        for i in range(1, len(jnts)):
            mc.connectAttr(pri_jnts[i]+'.tx', jnts[i]+'.tx')

        # lo knee pivot compensate for scale
        '''
        esult = control.create_movable_pivot(lo_knee_ctrl)
        mc.pointConstraint(utils.get_parent(pri_ik), result)
        mc.deleteAttr(result+'.animControl')
        mc.setAttr(lo_knee_ctrl+'.animPivotVis',cb=0 ,k=0, l=1)
        mc.delete(utils.get_shapes(result))
        result = mc.rename(result, lo_knee_ctrl+'_PIV')
        '''

        prc = mc.parentConstraint(lo_knee_last_node, lo_knee_ctrl+'_CONST', ik1, mo=1)[0]

        # create blendBias for lo knee ctrl when stretched
        mc.addAttr(lo_knee_ctrl, ln='extendBlendBias', min=0, max=1, dv=1, k=1)

        sr = mc.createNode('setRange')
        mc.connectAttr(leg_ik_ctrl+'.stretchFactor', sr+'.valueX')

        tt = 'linear'
        v = mc.getAttr(leg_ik_ctrl+'.stretchFactor')
        mc.setDrivenKeyframe(sr+'.oldMinX', dv=0, v=v, cd=lo_knee_ctrl+'.extendBlendBias', itt=tt, ott=tt)
        mc.setDrivenKeyframe(sr+'.oldMinX', dv=1, v=0.9, cd=lo_knee_ctrl+'.extendBlendBias', itt=tt, ott=tt)
        #mc.setDrivenKeyframe(sr+'.oldMinX', dv=-1, v=v / 2, cd=lo_knee_ctrl+'.extendBlendBias', itt=tt, ott=tt)

        mc.setAttr(sr+'.oldMaxX', 1)
        mc.setAttr(sr+'.minX', 0)
        mc.setAttr(sr+'.maxX', 1)

        mc.connectAttr(sr+'.outValueX', prc+'.w1', f=1)
        utils.connect_reverse(sr+'.outValueX', prc+'.w0')

        # clenaup
        control.create_movable_pivot(leg_ik_ctrl, ctrl_type='joint')

        for i, fk_ctrl in enumerate(fk_ctrls):
            if i:
                pickWalk.attribute_tag(fk_ctrl, fk_ctrls[i-1])
            else:
                pickWalk.attribute_tag(fk_ctrl, pick_walk_parent)

        pickWalk.attribute_tag(leg_base_ctrl, pick_walk_parent)
        pickWalk.attribute_tag(leg_ik_ctrl, leg_base_ctrl)
        pickWalk.attribute_tag(knee_ctrl, leg_base_ctrl)
        pickWalk.attribute_tag(lo_knee_ctrl, leg_ik_ctrl)

        spc = spaces.Space(knee_ctrl)
        spc.append_space('parent', parent)
        args = spc.generate_default_spaces()
        for a in args:
            spc.append_space(a[0], a[1])

        spc = spaces.Space(leg_ik_ctrl)
        spc.append_space('parent', parent)
        args = spc.generate_default_spaces()
        for a in args:
            spc.append_space(a[0], a[1])

        control.create_driven_shape(knee_ctrl, jnts[0], replace=False)

        utils.set_attrs([leg_ik_ctrl, knee_ctrl], 'r s', l=1, k=0)
        utils.set_attrs(fk_ctrls+[lo_knee_ctrl], 't s', l=1, k=0)
        utils.set_attrs(leg_base_ctrl, 's', l=1, k=0)

        # This finalizes the rig and creates rig sets
        self.finalize_part()

# This is a test to correct the slight shift in PV
def test_twist(jnt, ik, loc, tol=0.01):
    i = 0
    while round(utils.get_distance(loc, jnt), 3)> tol and i < 360:
        mc.setAttr(ik+'.twist', i)
        i += 1

    if round(utils.get_distance(loc, jnt), 3) > tol:
        i = 0
        while round(utils.get_distance(loc, jnt), 3)> tol and i > -360:
            mc.setAttr(ik+'.twist', i)
            i -= 1
    mc.delete(loc)
