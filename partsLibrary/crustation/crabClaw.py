# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot.partsLibrary import standardPart

class CrabClaw(standardPart.StandardPart):
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
        self.add_option('name', default='claw', required=True)
        self.add_option('numberJoints',
                    data_type='int',
                    default=3,
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
        jnt_zeros, plcs, jnts = self.guide_joint_chain(num_joints=num_joints)

        mc.xform(jnt_zeros[0], ws=1, t=[1.0, 0.0, 0.0])
        mc.xform(jnt_zeros[1], ws=1, t=[2, 0, 0])

        for i, zero in enumerate(jnt_zeros[1:]):
            mc.xform(zero, r=1, t=[0, -i*(i*0.1), 0])

        mc.setAttr(zero+'.ty', mc.getAttr(zero+'.ty')*1.5)
        mc.setAttr(zero+'.tx', mc.getAttr(zero+'.tx')*1.1)

        mc.xform(jnt_zeros, r=1, t=[-1*self.mirror_value, 0, 0])

        p_jnt_zeros, p_plcs, p_jnts = self.guide_joint_chain('pincer', num_joints=2)

        pc=mc.pointConstraint(jnt_zeros[-2:], p_jnt_zeros[0])
        mc.setAttr(pc[0]+'.w0', 0.8)
        mc.setAttr(pc[0]+'.w1', 0.2)

        pc1=mc.pointConstraint(jnt_zeros[-2:], p_jnt_zeros[1])
        mc.setAttr(pc1[0]+'.w0', 0.1)
        mc.setAttr(pc1[0]+'.w1', 0.9)
        mc.delete(pc, pc1)

        mc.xform(p_jnt_zeros, r=1, t=[0,0,0.2])
        mc.xform(p_jnt_zeros[1], r=1, t=[0,0,0.4])

        mc.parentConstraint(jnts[-2], p_jnt_zeros[0], mo=1)
        mc.parentConstraint(jnts[-2], p_jnt_zeros[1], mo=1)

        par = utils.get_parent(jnt_zeros[0])
        tmp = mc.createNode('transform')
        mc.parent(jnt_zeros, p_jnt_zeros, tmp)
        mc.xform(tmp, r=1, ro=[-90,-45,0])
        mc.parent(jnt_zeros, p_jnt_zeros, par)
        mc.delete(tmp)

        # Create FK ctrls
        zeros, ctrls = [], []
        for i, jnt in enumerate(jnts[:-1]):
            letter = utils.letters[i]
            zero, ctrl = self.guide_ctrl(name=letter, shape='circle', color='light_blue', driver=jnt, axis='X', scale=[0.5]*3)
            zeros.append(zero)
            ctrls.append(ctrl)

        # Create IK ctrls
        pn_zero, pn_ctrl = self.guide_ctrl(name='pincer', shape='pyramid', color='pink', driver=p_jnts[0], axis='X', scale=[1, 0.5, 0.5])
        base_zero, base_ctrl = self.guide_ctrl(name='clawBase', shape='pyramid', color=color, driver=jnts[0], axis='X', scale=[1, 0.5, 0.5])
        claw_zero, claw_ctrl = self.guide_ctrl(name='claw_IK', shape='sphere', color=color, driver=jnts[-2], axis='X', create_pivot=0)
        pv_zero, pv_ctrl = self.guide_ctrl(name='elbow_IK', shape='cube', color=color, axis='X', scale=[0.3]*3, create_pivot=0)

        mc.pointConstraint(jnts[0], pv_zero)
        mc.xform(pv_ctrl+'_CONST', r=1, t=[0,3,0])

        line = mc.createNode('transform', n=pv_ctrl+'_line_REF', p=utils.get_parent(pv_zero))
        control.create_driven_shape(line, [pv_ctrl, jnts[0]])
        utils.set_draw_override(line, 1)


        switch_zero, switch_ctrl = self.guide_ctrl(name='leg_IK_switch', shape='pin_gear', color='lavendar', driver=jnts[-1])
        mc.xform(switch_ctrl, r=1, ro=[0,0,180])
        mc.makeIdentity(switch_ctrl, apply=1, t=1, r=1, s=1, n=0, pn=1)
        mc.setAttr(leg_ctrl+'.numOffsetCtrls', 1)


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

        # Start coding suckka!!

        # This finalizes the rig and creates rig sets
        self.finalize_part()

kwargs = {}
self = CrabClaw()
