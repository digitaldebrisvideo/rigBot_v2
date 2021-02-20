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

class Cheek(standardPart.StandardPart):
    """Cheek module. Builds a set of joints and controls that can ride on a nurbs surface.
        Build Options:
            :side: (str) Side token for this rig part. Defaults to "C".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_head_JNT".
            :numberCtrls: (int)  Number of main controls. Defaults to 3.
            :createLowerControls: (bool) Create secondary lower controls. Defaults to True."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)
        self.add_option('parent', data_type='hook', default='C_head_JNT')
        self.add_option('jawParent', data_type='hook', default='C_jaw_JNT')
        self.add_option('numberPrimaryCtrls', data_type='int', default=3, tool_tip='Number of main controls', rebuild_to_modify=True)
        self.add_option('numberLowerCtrls', data_type='int', default=3, tool_tip='Number of secondary lower controls', rebuild_to_modify=True)
        self.add_option('createSquintControls', data_type='bool', default=True, tool_tip='Create secondary squint controls.', rebuild_to_modify=True)

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

        number_ctrls = options.get('numberPrimaryCtrls')
        number_lo_ctrls = options.get('numberLowerCtrls')
        create_squint = options.get('createSquintControls')
        nox = self.guide_master+'_NOX'

        mc.setAttr(self.guide_master+'.offsetTranslateZ', -.1)
        mc.setAttr(self.guide_master+'.jointAxisVis', 1)

        # Create surface
        surf = mm.eval('nurbsPlane -p 0 0 0 -ax 0 0 1 -w 2 -lr 1 -d 3 -u 3 -v 3 -ch 1;')
        surf[0] = mc.rename(surf[0], prefix+'_cheek_surf')
        surf[1] = mc.rename(surf[1], prefix+'_cheek_surf_makeNurbPlane')
        surf = surf[0]

        mc.parent(surf, self.guide_master+'_SURFS')
        mc.setAttr(self.guide_master+'.surfaceVis', 1)

        nld = mc.nonLinear(surf, type='bend', lowBound=0, highBound=1, curvature=0)
        mc.setAttr(nld[0]+'.curvature', 40)
        mc.setAttr(nld[1]+'.ry', 90)

        nld = mc.nonLinear(surf, type='bend', lowBound=-1, highBound=1, curvature=0)
        mc.setAttr(nld[0]+'.curvature', 20)
        mc.xform(nld[1], a=1,ro=[0,90,-90])

        mc.delete(surf, ch=1)
        #mc.xform(surf, a=1,ro=[15,45,0])

        rivet.rebuild_surface(surf)
        rivet.assign_ribbon_shader(surf)

        # Create UPPER cheeks
        offset = 0.5
        div = offset / (number_ctrls-1.0)

        color = 'green'
        if options.get('side') == 'R':
            color = 'red'

        for i in range(number_ctrls):
            name = 'cheek_'+utils.letters[i]
            jnt_zero, jnt_plc, jnt = self.guide_joint(name, alt_prefix=prefix)
            mc.xform(jnt_zero, r=1, t=[(i+1)*div-offset, 0, ((i+1)*div)*-0.2])

            rivet_guide_jnt(surf, jnt_zero, jnt_plc, jnt, nox)

            ctrl = self.guide_ctrl(name, driver=jnt, axis='z', shape='circle', color=color, scale=[0.1]*3)
            mc.xform(ctrl[1]+'.cv[*]', r=1, t=[0,0,0.2])

        if create_squint:

            for i in range(number_ctrls):
                name = 'squint_'+utils.letters[i]
                jnt_zero, jnt_plc, jnt = self.guide_joint(name, alt_prefix=prefix)
                mc.xform(jnt_zero, r=1, t=[(i+1)*div-offset, offset*0.5, ((i+1)*div)*-0.2])

                rivet_guide_jnt(surf, jnt_zero, jnt_plc, jnt, nox)

                ctrl = self.guide_ctrl(name, driver=jnt, axis='z', shape='diamond', color='pink', scale=[0.06]*3)
                mc.xform(ctrl[1]+'.cv[*]', r=1, t=[0,0,0.2])

        # Create lower cheeks
        if number_lo_ctrls:
            offset = 0.5
            div = offset / (number_lo_ctrls-1.0)

            for i in range(number_lo_ctrls):
                name = 'cheekLower_'+utils.letters[i]
                jnt_zero, jnt_plc, jnt = self.guide_joint(name, alt_prefix=prefix)
                mc.xform(jnt_zero, r=1, t=[(i+1)*div-offset, -offset, ((i+1)*div)*-0.2])

                rivet_guide_jnt(surf, jnt_zero, jnt_plc, jnt, nox)

                ctrl = self.guide_ctrl(name, driver=jnt, axis='z', shape='circle', color='dark_cyan', scale=[0.1]*3)
                mc.xform(ctrl[1]+'.cv[*]', r=1, t=[0,0,0.2])

        utils.set_attrs(self.guide_master+'_PLCS')
        mc.parentConstraint(surf, self.guide_master+'_PLCS', mo=1)
        mc.scaleConstraint(surf, self.guide_master+'_PLCS', mo=1)

        mc.xform(surf, a=1,ro=[15,45,0])

        # This finalizes your guide.
        self.finalize_guide()

    def create_all_ctrl(self, name, driven_ctrls, surf, create_rivet=True):

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
                if mc.objExists(ct+'.'+a):
                    mc.deleteAttr(ct+'.'+a)

        control.create_driven_shape(all_ctrl, driven_ctrls ,replace=1)

        for c in driven_ctrls:
            mc.parent(c+'_ZERO', all_jnt)
            surf_info = None

        if create_rivet:
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
        else:
            mc.parentConstraint(all_ctrl, all_jnt, mo=1)

        utils.set_attrs(all_ctrl, 'tz rx ry offsetX offsetY', l=1, k=0)
        return [all_zero,all_const,all_mocap,all_off,all_ctrl, surf_info]

    def create_rivet_ctrl_jnt(self, name, surf, create_rivet=True):
            zero, ctrl, offsets, last_node = self.anim_ctrl(name+'_CTL', inherit_scale=True)
            mc.parent( name+'_JNT', self.jnt_grps[0])
            mc.scaleConstraint(last_node, name+'_JNT', mo=1)

            if create_rivet:
                rivet.rivet_ctrl(surf, last_node, name+'_JNT', rivets_grp=self.noxform_grp)
            else:
                mc.parentConstraint(last_node, name+'_JNT', mo=1)

            return zero, ctrl, offsets, last_node, name+'_JNT'

    def connect_to_jaw(self, lo_ctrls, pri_ctrls):

        # find closest primary ctrl
        for i, ctrl in enumerate(lo_ctrls):
            if len(pri_ctrls) == self.options.get('numberLowerCtrls'):
                closest_ctrl = pri_ctrls[i]
            else:
                min_dst = 0.0
                closest_ctrl = None
                for p_ctrl in pri_ctrls:
                    dst = utils.get_distance(p_ctrl, ctrl)
                    if not min_dst:
                        min_dst = dst
                    elif dst < min_dst:
                        closest_ctrl = p_ctrl

            const = ctrl+'_CONST'
            pri_follow_par = mc.duplicate(const, po=1, n=const+'_primary_follow_PAR')
            pri_follow = mc.duplicate(const, po=1, n=const+'_primary_follow')
            jaw_follow = mc.duplicate(const, po=1, n=const+'_jaw_follow')
            mc.pointConstraint(closest_ctrl.replace('_CTL', '_JNT'), pri_follow_par)
            mc.parent(pri_follow, pri_follow_par)
            mc.parent(jaw_follow, self.hooks[1])

            pc = mc.pointConstraint(pri_follow, jaw_follow, const)[0]
            mc.addAttr(ctrl, ln='cheekJawBias', k=1, min=-1, max=1)

            tt='linear'
            mc.setDrivenKeyframe(pc+'.w0', cd=ctrl+'.cheekJawBias', dv=0, v=0.5, itt=tt, ott=tt)
            mc.setDrivenKeyframe(pc+'.w0', cd=ctrl+'.cheekJawBias', dv=1, v=1, itt=tt, ott=tt)
            mc.setDrivenKeyframe(pc+'.w0', cd=ctrl+'.cheekJawBias', dv=-1, v=0, itt=tt, ott=tt)
            utils.connect_reverse(pc+'.w0', pc+'.w1')

    def connect_squint_to_head(self, squint_ctrls, pri_ctrls):

        # find closest primary ctrl
        for i, ctrl in enumerate(squint_ctrls):
            closest_ctrl = pri_ctrls[i]
            closest_ctrl = closest_ctrl.replace('_CTL', '_JNT')

            if '_All_' in ctrl:
                closest_ctrl = closest_ctrl.replace('_JNT', '_GRP')

            const = ctrl+'_CONST'
            pri_follow = mc.duplicate(const, po=1, n=const+'_primary_follow')
            head_follow = mc.duplicate(const, po=1, n=const+'_head_follow')
            mc.parent(pri_follow, closest_ctrl)
            mc.parent(head_follow, self.hooks[0])

            pc = mc.parentConstraint(pri_follow, head_follow, const, mo=1)[0]
            mc.setAttr(pc+'.interpType', 2)
            mc.addAttr(ctrl, ln='cheekBias', k=1, min=0, max=1)

            tt='linear'
            mc.connectAttr(ctrl+'.cheekBias', pc+'.w0')
            utils.connect_reverse(pc+'.w0', pc+'.w1')

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

        number_ctrls = options.get('numberPrimaryCtrls')
        number_lo_ctrls = options.get('numberLowerCtrls')
        create_squint = options.get('createSquintControls')

        pickWalk_parent = options.get('pickWalkParent')

        # if we have a surface, parent it where it needs to be
        surf_grp = mc.createNode('transform', n=prefix+'_cheek_parent_SURF', p=hooks[0])
        surf = mc.rename(prefix+'_cheek_surf_REF', prefix+'_cheek_surf')
        mc.parent(surf, surf_grp)
        mc.hide(surf_grp)

        mc.makeIdentity(surf, apply=1, t=1, r=1, s=1, n=0, pn=1)
        mc.xform(surf, piv=[0,0,0])

        rivet.rebuild_surface(surf)

        ##################################################################3
        # Create primary ctrls

        pri_zeros, pri_ctrls, pri_offsets, pri_last_nodes, pri_jnts = [], [], [], [], []
        for i in range(number_ctrls):
            name = prefix+'_cheek_'+utils.letters[i]

            zero, ctrl, offsets, last_node, jnt = self.create_rivet_ctrl_jnt(name, surf)

            pri_zeros.append(zero)
            pri_ctrls.append(ctrl)
            pri_offsets.append(offsets)
            pri_last_nodes.append(last_node)
            pri_jnts.append(jnt)

        pri_all_zero, pri_all_const, pri_all_mocap, pri_all_off, pri_all_ctrl, pri_surf_info = self.create_all_ctrl(prefix+'_cheek_All', pri_ctrls, surf)
        utils.set_attrs(pri_ctrls, 'tz ', l=1, k=0)
        mc.parent(pri_all_zero, self.ctrl_grps[0])

        if create_squint:
            squint_zeros, squint_ctrls, squint_offsets, squint_last_nodes, squint_jnts = [], [], [], [], []
            for i in range(number_ctrls):
                name = prefix+'_squint_'+utils.letters[i]

                zero, ctrl, offsets, last_node, jnt = self.create_rivet_ctrl_jnt(name, surf, create_rivet=0)

                squint_zeros.append(zero)
                squint_ctrls.append(ctrl)
                squint_offsets.append(offsets)
                squint_last_nodes.append(last_node)
                squint_jnts.append(jnt)

            self.connect_squint_to_head(squint_ctrls, pri_ctrls)
            mc.parent(squint_zeros, hooks[0])


        ##################################################################3
        # Create lower controls
        if number_lo_ctrls:
            lo_zeros, lo_ctrls, lo_offsets, lo_last_nodes, lo_jnts = [], [], [], [], []
            for i in range(number_lo_ctrls):
                name = prefix+'_cheekLower_'+utils.letters[i]

                zero, ctrl, offsets, last_node, jnt = self.create_rivet_ctrl_jnt(name, surf, create_rivet=1)

                lo_zeros.append(zero)
                lo_ctrls.append(ctrl)
                lo_offsets.append(offsets)
                lo_last_nodes.append(last_node)
                lo_jnts.append(jnt)

            self.connect_to_jaw(lo_ctrls, pri_ctrls)
            utils.set_attrs(lo_ctrls, 'tz')

            mc.parent(lo_zeros, hooks[0])

        # set up auto buldge
        pri_rivet_grps = [j+'_rivet_GRP' for j in pri_jnts]

        for i in range(len(pri_jnts)):
            create_auto_bulge(pri_ctrls[i], pri_rivet_grps[i], pri_jnts[i])

        # This finalizes the rig and creates rig sets
        self.finalize_part()

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
