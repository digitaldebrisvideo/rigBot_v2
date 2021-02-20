# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import rivet
from rigBot import pickWalk
from rigBot.partsLibrary import standardPart

class Brow(standardPart.StandardPart):
    """Brow module. Builds a set of joints and controls that can ride on a nurbs surface.
        Build Options:
            :side: (str) Side token for this rig part. Defaults to "C".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_head_JNT".
            :numberCtrls: (int) Number of controls per side Defaults to 3.
            :createCenterControl: (bool) Create a center control. Defaults to True.
            :createUpperControls: (bool) Create upper secondary controls. Defaults to True."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)
        self.add_option('side', default='C', lock=True)
        self.add_option('parent', data_type='hook', default='C_head_JNT')
        self.add_option('numberCtrls', data_type='int', default=3, tool_tip='Number of controls per side', rebuild_to_modify=True)
        self.add_option('createCenterControl', data_type='bool', default=True, tool_tip='Create a center control.', rebuild_to_modify=True)
        self.add_option('createUpperControls', data_type='bool', default=True, tool_tip='Create secondary upper controls.', rebuild_to_modify=True)

        self.add_option('pickWalkParent',
                    data_type='string',
                    default="C_head_CTL",
                    selectable=True,
                    tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide. Use Keyword to update any options at build time."""

        def rivet_guide_jnt(surf, zero, plc, jnt, nox):

            if not surf:
                return

            cons = utils.get_constraints(jnt)
            if cons:
                mc.delete(cons)

            djnt = mc.duplicate(jnt, n=jnt+'_DRV', po=1)[0]
            rivet.rivet_ctrl(surf, plc, djnt, rivets_grp=nox, mo=0)
            mc.setAttr(djnt+'.jo', 90,0,90)
            if djnt.startswith('R_'):
                mc.setAttr(djnt+'.jo', -90,0,90)

            tmp = mc.createNode('transform', p=djnt)
            mc.parent(tmp, w=1)
            mc.delete(mc.parentConstraint(tmp, zero), tmp)

            mc.setAttr(plc+'.offsetTranslateZ', 0.1)
            if djnt.startswith('R_'):
                mc.setAttr(plc+'.offsetTranslateZ', -0.1)

            mc.parentConstraint(djnt, jnt)
            mc.hide(djnt)

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix              # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options = self.options            # Build options
        mirror_value = self.mirror_value  # 1.0 for left and center sided parts and -1.0 for right sided part.

        number_ctrls = options.get('numberCtrls')
        create_center_ctrl = options.get('createCenterControl')
        create_upper_ctrls = options.get('createUpperControls')

        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)
        nox = self.guide_master+'_NOX'

        mc.setAttr(self.guide_master+'.offsetTranslateZ', -.1)
        mc.setAttr(self.guide_master+'.jointAxisVis', 1)

        # Create surface
        surf = mm.eval('nurbsPlane -p 0 0 0 -ax 0 0 1 -w 2 -lr 1 -d 3 -u 6 -v 6 -ch 1;')
        surf[0] = mc.rename(surf[0], prefix+'_brow_surf')
        surf[1] = mc.rename(surf[1], prefix+'_brow_surf_makeNurbPlane')
        surf = surf[0]

        mc.parent(surf, self.guide_master+'_SURFS')
        mc.setAttr(self.guide_master+'.surfaceVis', 1)

        nld = mc.nonLinear(surf, type='bend', lowBound=0, highBound=1, curvature=0)
        mc.setAttr(nld[0]+'.curvature', 60)
        mc.setAttr(nld[1]+'.ry', 90)

        nld = mc.nonLinear(surf, type='bend', lowBound=-1, highBound=1, curvature=0)
        mc.setAttr(nld[0]+'.curvature', 80)
        mc.xform(nld[1], a=1,ro=[0,90,-90])

        mc.delete(surf, ch=1)
        mc.xform(surf, a=1,ro=[-20,0,0])
        mc.makeIdentity(surf, apply=1, t=1, r=1, s=1, n=0, pn=1)

        rivet.rebuild_surface(surf)
        rivet.assign_ribbon_shader(surf)

        # Create primary joints
        if create_center_ctrl:
            jnt_zero, jnt_plc, jnt = self.guide_joint('brow')
            rivet_guide_jnt(surf, jnt_zero, jnt_plc, jnt, nox)

            ctrl = self.guide_ctrl('brow', driver=jnt, axis='z', shape='circle', color='yellow', scale=[0.1]*3)
            mc.xform(ctrl[1]+'.cv[*]', r=1, t=[0,0,0.2])

        # Create left brows
        div = 0.4 / (number_ctrls-1.0)

        for i in range(number_ctrls):
            name = 'brow_'+utils.letters[i]
            jnt_zero, jnt_plc, jnt = self.guide_joint(name, alt_prefix=l_prefix)
            mc.xform(jnt_zero, r=1, t=[(i+1)*div, 0, ((i+1)*div)*-0.2])

            rivet_guide_jnt(surf, jnt_zero, jnt_plc, jnt, nox)

            ctrl = self.guide_ctrl(name, driver=jnt, axis='z', shape='circle', color='green', scale=[0.1]*3, alt_prefix=l_prefix)
            mc.xform(ctrl[1]+'.cv[*]', r=1, t=[0,0,0.2])

        # Create right brows
        for i in range(number_ctrls):
            name = 'brow_'+utils.letters[i]
            jnt_zero, jnt_plc, jnt = self.guide_joint(name, alt_prefix=r_prefix)
            mc.xform(jnt_zero, r=1, t=[-(i+1)*div, 0, ((i+1)*div)*-0.2])

            rivet_guide_jnt(surf, jnt_zero, jnt_plc, jnt, nox)

            ctrl = self.guide_ctrl(name, driver=jnt, axis='z', shape='circle', color='red', scale=[0.1]*3, alt_prefix=r_prefix)
            piv = utils.get_parent(ctrl[1])
            mc.setAttr(piv+'.rz', -180)
            mc.setAttr(piv+'.sz', -1)

            mc.xform(ctrl[1]+'.cv[*]', r=1, t=[0,0,0.2])

        # Create upper, secondary ctrls
        if create_upper_ctrls:

            # Create primary joints
            if create_center_ctrl:
                jnt_zero, jnt_plc, jnt = self.guide_joint('brow_upper')
                mc.xform(jnt_zero, r=1, t=[0, 0.4, 0])
                rivet_guide_jnt(surf, jnt_zero, jnt_plc, jnt, nox)

                ctrl = self.guide_ctrl('brow_upper', driver=jnt, axis='z', shape='square', color='pink', scale=[0.06]*3)
                mc.xform(ctrl[1]+'.cv[*]', r=1, t=[0,0,0.2])
                mc.xform(ctrl[1]+'.cv[*]', r=1, ro=[0,0,45])

            for i in range(number_ctrls):
                name = 'brow_upper_'+utils.letters[i]
                jnt_zero, jnt_plc, jnt = self.guide_joint(name, alt_prefix=l_prefix)
                mc.xform(jnt_zero, r=1, t=[(i+1)*div, 0.4, ((i+1)*div)*-0.2])

                rivet_guide_jnt(surf, jnt_zero, jnt_plc, jnt, nox)

                ctrl = self.guide_ctrl(name, driver=jnt, axis='z', shape='square', color='dark_cyan', scale=[0.06]*3, alt_prefix=l_prefix)
                mc.xform(ctrl[1]+'.cv[*]', r=1, t=[0,0,0.2])
                mc.xform(ctrl[1]+'.cv[*]', r=1, ro=[0,0,45])

            # Create right brows
            for i in range(number_ctrls):
                name = 'brow_upper_'+utils.letters[i]
                jnt_zero, jnt_plc, jnt = self.guide_joint(name, alt_prefix=r_prefix)
                mc.xform(jnt_zero, r=1, t=[-(i+1)*div, 0.4, ((i+1)*div)*-0.2])

                rivet_guide_jnt(surf, jnt_zero, jnt_plc, jnt, nox)

                ctrl = self.guide_ctrl(name, driver=jnt, axis='z', shape='square', color='dark_magenta', scale=[0.06]*3, alt_prefix=r_prefix)
                mc.xform(ctrl[1]+'.cv[*]', r=1, t=[0,0,0.2])
                mc.xform(ctrl[1]+'.cv[*]', r=1, ro=[0,0,45])

                piv = utils.get_parent(ctrl[1])
                mc.setAttr(piv+'.rz', -180)
                mc.setAttr(piv+'.sz', -1)



        utils.set_attrs(self.guide_master+'_PLCS')
        mc.parentConstraint(surf, self.guide_master+'_PLCS', mo=1)
        mc.scaleConstraint(surf, self.guide_master+'_PLCS', mo=1)

        # This finalizes your guide.
        self.finalize_guide()

    def create_all_ctrl(self, name, driven_ctrls, surf):

        # Create the new jnt grp
        try:
            mid_jnt = utils.find_middle(driven_ctrls).replace('_CTL','_JNT')
            all_jnt = mc.createNode('transform', n=name+'_GRP', p=mid_jnt)

        except:
            mid_jnts = [j.replace('_CTL','_JNT') for j in utils.find_middle(driven_ctrls)]
            all_jnt = mc.createNode('transform', n=name+'_GRP', p=mid_jnts[0])

        mc.parent(all_jnt, self.ctrl_grps[0])

        # Create the new ctrl
        mid_ctrl = utils.find_middle(driven_ctrls)
        all_zero = mc.duplicate(mid_ctrl, po=1, n=name+'_CTL_ZERO')[0]
        all_const = mc.duplicate(mid_ctrl, po=1, n=name+'_CTL_CONST')[0]
        all_mocap = mc.duplicate(mid_ctrl, po=1, n=name+'_CTL_MOCAP')[0]
        all_off = mc.duplicate(mid_ctrl, po=1, n=name+'_CTL_OFF')[0]
        all_ctrl = mc.duplicate(mid_ctrl, po=1, n=name+'_CTL')[0]

        mc.parent(all_zero, w=1)
        mc.parent(all_const, all_zero)
        mc.parent(all_mocap, all_const)
        mc.parent(all_off, all_mocap)
        mc.parent(all_ctrl, all_off)

        mc.delete(mc.pointConstraint(mid_ctrl, all_zero))
        mc.delete(mc.parentConstraint(all_zero, all_jnt))

        for ct in [all_zero, all_mocap, all_const, all_off, all_ctrl]:
            for a in ['offsetX','offsetY','offsetZ']:
                mc.deleteAttr(ct+'.'+a)

        control.create_driven_shape(all_ctrl, driven_ctrls ,replace=1)

        for c in driven_ctrls:
            mc.parent(c+'_ZERO', all_jnt)

        surf_info = rivet.rivet_ctrl(surf, all_ctrl, all_jnt, rivets_grp=self.noxform_grp)

        for ctrl in driven_ctrls:
            jnt = ctrl.replace('_CTL','_JNT')
            pma = mc.createNode('addDoubleLinear')
            mc.connectAttr(all_ctrl+'.offsetZ', pma+'.input1')
            mc.connectAttr(ctrl+'.offsetZ', pma+'.input2')

            mc.connectAttr(pma+'.o', jnt+'.tz', f=1)
            if jnt.startswith('R_'):
                utils.connect_negative(pma+'.o', jnt+'.tz')

            mc.connectAttr(all_ctrl+'.s', ctrl+'_CONST.s')

        utils.set_attrs(all_ctrl, 'tz rx ry offsetX offsetY', l=1, k=0)
        return [all_zero,all_const,all_mocap,all_off,all_ctrl, surf_info]

    def create_rivet_ctrl_jnt(self, name, surf):
            zero, ctrl, offsets, last_node = self.anim_ctrl(name+'_CTL', inherit_scale=True)
            mc.parent( name+'_JNT', self.jnt_grps[0])
            mc.scaleConstraint(last_node, name+'_JNT', mo=1)

            rivet.rivet_ctrl(surf, last_node, name+'_JNT', rivets_grp=self.noxform_grp)

            return zero, ctrl, offsets, last_node, name+'_JNT'

    def connect_mult_ctrl_driver(self, ctrl, const, rotates=False):

        mc.addAttr(ctrl, ln='upperInfluence', min=0, max=1, k=1, dv=0.5)
        md = mc.createNode('multiplyDivide')
        mc.connectAttr(ctrl+'.tx', md+'.i1x')
        mc.connectAttr(ctrl+'.ty', md+'.i1y')
        mc.connectAttr(ctrl+'.rz', md+'.i1z')
        mc.connectAttr(ctrl+'.upperInfluence', md+'.i2x')
        mc.connectAttr(ctrl+'.upperInfluence', md+'.i2y')
        mc.connectAttr(ctrl+'.upperInfluence', md+'.i2z')
        mc.connectAttr(md+'.ox', const+'.tx')
        mc.connectAttr(md+'.oy', const+'.ty')

        if rotates:
            ctl = const.replace('_CTL_CONST', '_CTL')
            rot_jnt = mc.listConnections(ctl+'.r')[0]

            utils.break_connections(rot_jnt+'.r')
            utils.break_connections(rot_jnt+'.rx')
            utils.break_connections(rot_jnt+'.ry')
            utils.break_connections(rot_jnt+'.rz')

            adlx = mc.createNode('addDoubleLinear')
            adly = mc.createNode('addDoubleLinear')
            adlz = mc.createNode('addDoubleLinear')

            mc.connectAttr(ctl+'.rx', adlx+'.i1')
            mc.connectAttr(ctl+'.ry', adly+'.i1')
            mc.connectAttr(ctl+'.rz', adlz+'.i1')

            mc.connectAttr(md+'.oz', adlx+'.i2', f=1)
            mc.connectAttr(md+'.oz', adly+'.i2', f=1)
            mc.connectAttr(md+'.oz', adlz+'.i2', f=1)

            mc.connectAttr(adlz+'.o', rot_jnt+'.rz', f=1)

    def connect_center_mult(self, l_surf_info, r_surf_info, ctrl, surf):

        mc.parent(ctrl+'_MOCAP', ctrl+'_ZERO')
        fll = rivet.surface_fll(ctrl+'_CONST', surf, noxform_grp=self.noxform_grp, world_scale_node=self.ctrl_grps[0])[0]
        fll_shape = utils.get_shapes(fll)[0]

        mc.addAttr(ctrl, ln='followAllCtrls', min=0, max=1, dv=1, k=1)

        # average two surf info U values
        for param in ['U', 'V']:

            pma = mc.createNode('plusMinusAverage')
            mc.setAttr(pma+'.operation',3)

            mc.connectAttr(l_surf_info+'.parameter'+param, pma+'.input1D[0]')
            mc.connectAttr(r_surf_info+'.parameter'+param, pma+'.input1D[1]')
            mc.setAttr(fll_shape+'.parameter'+param, mc.getAttr(pma+'.output1D'))

            bta = mc.createNode('blendTwoAttr')
            mc.setAttr(bta+'.input[0]', mc.getAttr(pma+'.output1D'))
            mc.connectAttr(pma+'.output1D', bta+'.input[1]')

            mc.connectAttr(bta+'.o', fll_shape+'.parameter'+param)
            mc.connectAttr(ctrl+'.followAllCtrls', bta+'.attributesBlender')

        mc.parent(ctrl+'_MOCAP', ctrl+'_CONST')

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

        pickWalk_parent = options.get('pickWalkParent')

        number_ctrls = options.get('numberCtrls')
        create_center_ctrl = options.get('createCenterControl')
        create_upper_ctrls = options.get('createUpperControls')

        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)

        # if we have a surface, parent it where it needs to be
        surf_grp = mc.createNode('transform', n=prefix+'_brow_parent_SURF', p=hooks[0])
        surf = mc.rename(prefix+'_brow_surf_REF', prefix+'_brow_surf')
        mc.parent(surf, surf_grp)
        mc.hide(surf_grp)

        mc.makeIdentity(surf, apply=1, t=1, r=1, s=1, n=0, pn=1)
        mc.xform(surf, piv=[0,0,0])

        rivet.rebuild_surface(surf)

        ##################################################################3
        # Create primary ctrls

        if create_center_ctrl:
            c_zero, c_ctrl, c_offsets, c_last_node, c_jnt = self.create_rivet_ctrl_jnt(prefix+'_brow', surf)
            utils.set_attrs(c_ctrl, 'tz ', l=1, k=0)
            mc.parent(c_zero, self.ctrl_grps[0])

        l_zeros, l_ctrls, l_offsets, l_last_nodes, l_jnts = [], [], [], [], []
        for i in range(number_ctrls):
            name = l_prefix+'_brow_'+utils.letters[i]

            zero, ctrl, offsets, last_node, jnt = self.create_rivet_ctrl_jnt(name, surf)

            l_zeros.append(zero)
            l_ctrls.append(ctrl)
            l_offsets.append(offsets)
            l_last_nodes.append(last_node)
            l_jnts.append(jnt)

        l_all_zero, l_all_const, l_all_mocap, l_all_off, l_all_ctrl, l_surf_info= self.create_all_ctrl(l_prefix+'_brow_All', l_ctrls, surf)
        utils.set_attrs(l_ctrls, 'tz ', l=1, k=0)
        mc.parent(l_all_zero, self.ctrl_grps[0])

        r_zeros, r_ctrls, r_offsets, r_last_nodes, r_jnts = [], [], [], [], []
        for i in range(number_ctrls):
            name = r_prefix+'_brow_'+utils.letters[i]

            zero, ctrl, offsets, last_node, jnt = self.create_rivet_ctrl_jnt(name, surf)

            r_zeros.append(zero)
            r_ctrls.append(ctrl)
            r_offsets.append(offsets)
            r_last_nodes.append(last_node)
            r_jnts.append(jnt)

        r_all_zero, r_all_const, r_all_mocap, r_all_off, r_all_ctrl, r_surf_info= self.create_all_ctrl(r_prefix+'_brow_All', r_ctrls, surf)
        utils.set_attrs(r_ctrls, 'tz ', l=1, k=0)
        mc.parent(r_all_zero, self.ctrl_grps[0])

        ##################################################################3
        # CReate upper controls

        if create_upper_ctrls:
            if create_center_ctrl:
                c_up_zero, c_up_ctrl, c_up_offsets, c_up_last_node, c_up_jnt = self.create_rivet_ctrl_jnt(prefix+'_brow_upper', surf)
                self.connect_mult_ctrl_driver(c_ctrl, c_up_ctrl+'_CONST', rotates=0)
                utils.set_attrs(c_up_ctrl, 'tz ', l=1, k=0)
                mc.parent(c_up_zero, self.ctrl_grps[0])

            l_up_zeros, l_up_ctrls, l_up_offsets, l_up_last_nodes, l_up_jnts = [], [], [], [], []
            for i in range(number_ctrls):
                name = l_prefix+'_brow_upper_'+utils.letters[i]

                zero, ctrl, offsets, last_node, jnt = self.create_rivet_ctrl_jnt(name, surf)

                l_up_zeros.append(zero)
                l_up_ctrls.append(ctrl)
                l_up_offsets.append(offsets)
                l_up_last_nodes.append(last_node)
                l_up_jnts.append(jnt)

            l_up_all_zero, l_up_all_const, l_up_all_mocap, l_up_all_off, l_up_all_ctrl, l_up_surf_info = self.create_all_ctrl(l_prefix+'_brow_upper_All', l_up_ctrls, surf)
            self.connect_mult_ctrl_driver(l_all_ctrl, l_up_all_const, rotates=1)
            mc.parent(l_up_all_zero, self.ctrl_grps[0])

            l_up_consts = [c+'_CONST' for c in l_up_ctrls]

            for i in range(len(l_ctrls)):
                self.connect_mult_ctrl_driver(l_ctrls[i], l_up_consts[i], rotates=0)

            utils.set_attrs(l_up_ctrls, 'tz ', l=1, k=0)

            r_up_zeros, r_up_ctrls, r_up_offsets, r_up_last_nodes, r_up_jnts = [], [], [], [], []
            for i in range(number_ctrls):
                name = r_prefix+'_brow_upper_'+utils.letters[i]

                zero, ctrl, offsets, last_node, jnt = self.create_rivet_ctrl_jnt(name, surf)

                r_up_zeros.append(zero)
                r_up_ctrls.append(ctrl)
                r_up_offsets.append(offsets)
                r_up_last_nodes.append(last_node)
                r_up_jnts.append(jnt)

            r_up_all_zero, r_up_all_const, r_up_all_mocap, r_up_all_off, r_up_all_ctrl, r_up_surf_info= self.create_all_ctrl(r_prefix+'_brow_upper_All', r_up_ctrls, surf)
            self.connect_mult_ctrl_driver(r_all_ctrl, r_up_all_const, rotates=1)
            mc.parent(r_up_all_zero, self.ctrl_grps[0])

            r_up_consts = [c+'_CONST' for c in r_up_ctrls]

            for i in range(len(r_ctrls)):
                self.connect_mult_ctrl_driver(r_ctrls[i], r_up_consts[i], rotates=0)

            utils.set_attrs(r_up_ctrls, 'tz ', l=1, k=0)

        # Create center follow
        if create_center_ctrl:
            self.connect_center_mult(l_surf_info, r_surf_info, c_ctrl, surf)
            if create_upper_ctrls:
                const = mc.rename(c_up_ctrl+'_CONST', c_up_ctrl+'_follow_CONST')
                new = mc.duplicate(const, po=1, n=c_up_ctrl+'_CONST')[0]
                mc.parent(const, new)

                self.connect_center_mult(l_up_surf_info, r_up_surf_info, c_up_ctrl, surf)

                mc.parent(c_up_ctrl+'_MOCAP', const)

        # set up auto buldge
        l_rivet_grps = [j+'_rivet_GRP' for j in l_jnts]
        r_rivet_grps = [j+'_rivet_GRP' for j in r_jnts]

        for i in range(len(l_jnts)):
            create_auto_bulge(l_ctrls[i], l_rivet_grps[i], l_jnts[i])
            create_auto_bulge(r_ctrls[i], r_rivet_grps[i], r_jnts[i])

        # This finalizes the rig and creates rig sets
        self.finalize_part()

    def mirror_surf(self):

        surf = self.surfaces[0]

        src_idx = [8,7,6,5]
        dst_idx = [0,1,2,3]

        for row in range(9):
            for col in range(len(src_idx)):
                src = '{0}.cv[{2}][{1}]'.format(surf, row, src_idx[col])
                dst = '{0}.cv[{2}][{1}]'.format(surf, row, dst_idx[col])

                pos = mc.xform(src, q=1, ws=1, t=1)
                pos[0] *= -1
                mc.xform(dst, ws=1, t=pos)

            src = '{0}.cv[4][{1}]'.format(surf, row)
            dst = '{0}.cv[4][{1}]'.format(surf, row)

            pos = mc.xform(src, q=1, ws=1, t=1)
            pos[0] = 0
            mc.xform(dst, ws=1, t=pos)




def create_auto_bulge(ctrl, rivet_grp, jnt):

    '''
    rivet_grp = 'L_cheek_C_JNT_rivet_GRP'
    jnt ='L_cheek_C_JNT'
    ctrl = 'L_cheek_C_CTL'
    '''

    static_grp = mc.duplicate(rivet_grp, po=1, n=rivet_grp+'_static')[0]
    dist = utils.create_distance_reader(static_grp, rivet_grp, no_stretch=1)

    mc.addAttr(ctrl, ln='autoBulgeMult', min=0, dv=0.2, k=1)
    mc.addAttr(ctrl, ln='autoBulgeMax', min=0, dv=1, k=1)

    mdl = mc.createNode('multDoubleLinear')
    mc.connectAttr(ctrl+'.autoBulgeMult', mdl+'.i1')
    mc.connectAttr(dist+'.localDistance', mdl+'.i2')

    # set up max clamp
    clamp = mc.createNode('clamp')
    mc.connectAttr(ctrl+'.autoBulgeMax', clamp+'.maxR')
    mc.connectAttr(mdl+'.o', clamp+'.inputR')

    # get original connections and add to it
    cnn = mc.listConnections(jnt+'.tz', s=1, p=1)
    if cnn:
        adl = mc.createNode('addDoubleLinear')
        mc.connectAttr(cnn[0], adl+'.i1')
        mc.connectAttr(clamp+'.outputR', adl+'.i2')
        mc.connectAttr(adl+'.o', jnt+'.tz', f=1)

        if jnt.startswith('R'):
            utils.connect_negative(clamp+'.outputR', adl+'.i2')

    else:
        mc.connectAttr(mdl+'.o', jnt+'.tz')

        if jnt.startswith('R'):
            utils.connect_negative(mdl+'.o', jnt+'.tz')


    mc.setAttr(ctrl+'.autoBulgeMax', k=0, cb=1)
    mc.setAttr(ctrl+'.autoBulgeMult', k=0, cb=1)
