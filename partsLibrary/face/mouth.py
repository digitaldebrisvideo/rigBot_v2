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

class Mouth(standardPart.StandardPart):
    """Spline based mouth module. **This part is not mirrorable**

        Note:
            Eventually this will zipper control functionality.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "C".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_reverseJaw_JNT".
            :jawParent: (str) Jaw parent. Defaults to "C_jaw_JNT".
            :numberJoints: (int) Number of joints per quadrant. Defaults to 4.
            :numberCtrls: (int) Number of ctrls per quadrant. Defaults to 1.
            :createZipperControl: (bool) Create a lip zipper control. Defaults to True.
            :upperLipEdgeLoop: (list) Edge loop for the upper lip line to place joints. Defaults to [].
            :lowerLipEdgeLoop: (list) Edge loop for the lower lip line to place joints. Defaults to [].
            :upperLipRollEdgeLoop: (list) Edge loop for the upper lip line to place roll joints. Defaults to [].
            :lowerLipRollEdgeLoop: (list) Edge loop for the lower lip line to place roll joints. Defaults to []."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('side', default='C', lock=True)
        self.add_option('parent', data_type='hook', default='C_reverseJaw_JNT')
        self.add_option('jawParent', data_type='hook', default='C_jaw_JNT')

        self.add_option('numberJoints',
                 data_type='int',
                 min=1,
                 default=4,
                 rebuild_to_modify=True,
                 tool_tip='Number of joints per quadrant.')

        self.add_option('numberCtrls',
                 data_type='int',
                 min=1,
                 default=1,
                 rebuild_to_modify=True,
                 tool_tip='Number of ctrls per quadrant.')

        self.add_option('createZipperControl',
                 data_type='bool',
                 default=True,
                 rebuild_to_modify=True,
                 tool_tip='Create a lip zipper control.')

        self.add_option('upperLipEdgeLoop',
                         data_type='selection',
                         default=[],
                         tool_tip='Edge loop for the upper lip line to place joints.')

        self.add_option('lowerLipEdgeLoop',
                         data_type='selection',
                         default=[],
                         tool_tip='Edge loop for the lower lip line to place joints.')


        self.add_option('upperLipRollEdgeLoop',
                 data_type='selection',
                 default=[],
                 tool_tip='Edge loop for the upper lip line to place roll joints.')


        self.add_option('lowerLipRollEdgeLoop',
                 data_type='selection',
                 default=[],
                 tool_tip='Edge loop for the lower lip line to place roll joints.')

        self.add_option('pickWalkParent',
                    data_type='string',
                    default="C_head_CTL",
                    selectable=True,
                    tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide. Use KWARGS to update any options at build time."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix              # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options = self.options            # Build options
        mirror_value = self.mirror_value  # 1.0 for left and center sided parts and -1.0 for right sided part.

        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)

        up_number_joints = options.get('numberJoints')
        lo_number_joints = options.get('numberJoints')

        number_ctrls = options.get('numberCtrls')
        create_zipper = options.get('createZipperControl')

        upper_edge_loop = mc.ls(options.get('upperLipEdgeLoop'))
        lower_edge_loop = mc.ls(options.get('lowerLipEdgeLoop'))
        upper_roll_edge_loop = mc.ls(options.get('upperLipRollEdgeLoop'))
        lower_roll_edge_loop = mc.ls(options.get('lowerLipRollEdgeLoop'))

        # if user specified  edgeloops
        if upper_edge_loop and lower_edge_loop:
            loc = utils.snap_locator(upper_edge_loop+lower_edge_loop)
            mc.delete(mc.parentConstraint(loc, self.guide_master), loc)

            # Create curves
            up_pri_crv = utils.create_curve_from_edges(prefix+'_upperLip_crv', upper_edge_loop)
            lo_pri_crv = utils.create_curve_from_edges(prefix+'_lowerLip_crv', lower_edge_loop)
            up_roll_crv = utils.create_curve_from_edges(prefix+'_upperLipRoll_crv', upper_roll_edge_loop)
            lo_roll_crv = utils.create_curve_from_edges(prefix+'_lowerLipRoll_crv', lower_roll_edge_loop)

        # otherwise build some generic shit.
        else:
            up_pri_crv = mm.eval('curve -d 2 -p -2 0 0 -p -1 1 0 -p 0 1.3 0 -p 1 1 0 -p 2 0 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 3 ;')
            lo_pri_crv = mm.eval('curve -d 2 -p -2 0 0 -p -1 -1 0 -p 0 -1.3 0 -p 1 -1 0 -p 2 0 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 3 ;')
            up_roll_crv = mm.eval('curve -d 2 -p -2 0 0 -p -1 1 0 -p 0 1.3 0 -p 1 1 0 -p 2 0 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 3 ;')
            lo_roll_crv = mm.eval('curve -d 2 -p -2 0 0 -p -1 -1 0 -p 0 -1.3 0 -p 1 -1 0 -p 2 0 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 3 ;')

        ####################
        #  BUILD CTRLS

        # now we have everything .. Lets build some primary ctrls
        up_pos = utils.get_uniform_spacing_on_curve(up_pri_crv, number_ctrls*2+3)
        lo_pos = utils.get_uniform_spacing_on_curve(lo_pri_crv, number_ctrls*2+3)

        c_up_pri_zero, c_up_pri_ctrl = self.guide_ctrl('upperLip', shape='circle', color='yellow', scale=[0.05]*3, axis='Z')
        c_lo_pri_zero, c_lo_pri_ctrl = self.guide_ctrl('lowerLip', shape='circle', color='yellow', scale=[0.05]*3, axis='Z')
        r_corner_zero, r_corner_ctrl = self.guide_ctrl('lipCorner', shape='circle', color='yellow', scale=[0.05]*3, axis='Z', alt_prefix=r_prefix)
        l_corner_zero, l_corner_ctrl = self.guide_ctrl('lipCorner', shape='circle', color='yellow', scale=[0.05]*3, axis='Z', alt_prefix=l_prefix)

        up_pri_zeros, up_pri_ctrls = [r_corner_zero], [r_corner_ctrl]
        lo_pri_zeros, lo_pri_ctrls = [r_corner_zero], [r_corner_ctrl]

        # Create right side pri ctrls
        for i in reversed(range(number_ctrls)):
            ltr = utils.letters[i]
            up_zero, up_ctrl = self.guide_ctrl('upperLip_'+ltr, shape='circle', color='yellow', scale=[0.05]*3, axis='Z', alt_prefix=r_prefix)
            lo_zero, lo_ctrl = self.guide_ctrl('lowerLip_'+ltr, shape='circle', color='yellow', scale=[0.05]*3, axis='Z', alt_prefix=r_prefix)

            up_pri_zeros.append(up_zero)
            up_pri_ctrls.append(up_ctrl)

            lo_pri_zeros.append(lo_zero)
            lo_pri_ctrls.append(lo_ctrl)

        # add center ctrl to lists
        up_pri_zeros.append(c_up_pri_zero)
        up_pri_ctrls.append(c_up_pri_ctrl)

        lo_pri_zeros.append(c_lo_pri_zero)
        lo_pri_ctrls.append(c_lo_pri_ctrl)

        # Create left side pri ctrls
        for i in range(number_ctrls):
            ltr = utils.letters[i]
            up_zero, up_ctrl = self.guide_ctrl('upperLip_'+ltr, shape='circle', color='yellow', scale=[0.05]*3, axis='Z', alt_prefix=l_prefix)
            lo_zero, lo_ctrl = self.guide_ctrl('lowerLip_'+ltr, shape='circle', color='yellow', scale=[0.05]*3, axis='Z', alt_prefix=l_prefix)

            up_pri_zeros.append(up_zero)
            up_pri_ctrls.append(up_ctrl)

            lo_pri_zeros.append(lo_zero)
            lo_pri_ctrls.append(lo_ctrl)

        # append the left corner ctrl
        up_pri_zeros.append(l_corner_zero)
        up_pri_ctrls.append(l_corner_ctrl)

        lo_pri_zeros.append(l_corner_zero)
        lo_pri_ctrls.append(l_corner_ctrl)

        # place them
        for i, zero in enumerate(up_pri_zeros):
            mc.xform(zero, ws=1, t=up_pos[i])

            if 'lipCorner' not in zero:
                mc.xform(up_pri_ctrls[i]+'.cv[*]', r=1, t=[0,0.02, 0.01])

        for i, zero in enumerate(lo_pri_zeros):
            mc.xform(zero, ws=1, t=lo_pos[i])

            if 'lipCorner' not in zero:
                mc.xform(lo_pri_ctrls[i]+'.cv[*]', r=1, t=[0,-0.02,0.01])

        # repo corner ctrls
        up_cvs = mc.ls(up_pri_crv+'.cv[*]', fl=1)
        lo_cvs = mc.ls(lo_pri_crv+'.cv[*]', fl=1)

        loc = utils.snap_locator([up_cvs[0], lo_cvs[0]])
        mc.delete(mc.pointConstraint(loc, r_corner_zero), loc)

        loc = utils.snap_locator([up_cvs[-1], lo_cvs[-1]])
        mc.delete(mc.pointConstraint(loc, l_corner_zero), loc)

        # Mouth all ctrl
        loc = utils.snap_locator([r_corner_ctrl, l_corner_ctrl])
        dist = utils.get_distance(loc, c_up_pri_ctrl)
        mc.xform(loc, r=1, t=[0,0,-dist])

        mouth_all_zero, mouth_all_ctrl = self.guide_ctrl('mouthAll', shape='circle', color='cyan', scale=[0.15,0.1,0.1], axis='Z')
        mc.delete(mc.pointConstraint(loc, mouth_all_zero))
        mc.xform(mouth_all_ctrl+'.cv[*]', r=1, t=[0,0,dist*3])

        if create_zipper:
            l_zipper_zero, l_zipper_ctrl = self.guide_ctrl('lipZipper', alt_prefix=l_prefix, create_pivot=0, shape='triangle', color='green', scale=[0.02, 0.02, 0.02], axis='Z')
            mc.xform(l_zipper_ctrl+'.cv[*]', r=1, ro=[0,0,90])
            mc.xform(l_zipper_zero, ws=1, t=mc.xform(mouth_all_ctrl+'.cv[7]', q=1, ws=1, t=1))

            r_zipper_zero, r_zipper_ctrl = self.guide_ctrl('lipZipper', alt_prefix=r_prefix, create_pivot=0, shape='triangle', color='red', scale=[0.02, 0.02, 0.02], axis='Z')
            mc.xform(r_zipper_ctrl+'.cv[*]', r=1, ro=[0,0,-90])
            mc.xform(r_zipper_zero, ws=1, t=mc.xform(mouth_all_ctrl+'.cv[3]', q=1, ws=1, t=1))

            mc.parentConstraint(mouth_all_ctrl, l_zipper_zero, mo=1)
            mc.parentConstraint(mouth_all_ctrl, r_zipper_zero, mo=1)
            mc.scaleConstraint(mouth_all_ctrl, l_zipper_zero, mo=1)
            mc.scaleConstraint(mouth_all_ctrl, r_zipper_zero, mo=1)

        # Now set negative scales on all right sideed ctrls
        for zero in up_pri_zeros+lo_pri_zeros:
            if zero.startswith(r_prefix):
                mc.setAttr(zero+'.sx', -1)

        # now orient the pivot ctrls
        for ctrl in up_pri_ctrls+lo_pri_ctrls:
            if ctrl.startswith(l_prefix):

                loc = utils.snap_locator(ctrl)
                mc.delete(mc.pointConstraint(ctrl, loc))

                aim = mc.duplicate(loc)[0]
                up = mc.duplicate(loc)[0]
                mc.xform(up, r=1, t=[0,0,1])
                mc.xform(aim, r=1, t=[0,1,0])

                mp = rivet.motionPath(loc, up_pri_crv, up)
                mc.setAttr(mp+'.upAxis', 2)
                mc.setAttr(mp+'.worldUpType', 3)
                mc.setAttr(mp+'.worldUpVectorY', 0)
                mc.setAttr(mp+'.worldUpVectorZ', 1)

                pivot_ctrl = utils.get_parent(ctrl)
                mc.delete(mc.aimConstraint( aim, pivot_ctrl, aim=[0,1,0], u=[0,0,1], wu=[0,0,1], wuo=loc, wut='objectRotation'))

                mc.delete(mp, up, loc, aim)

                r_pivot_ctrl = pivot_ctrl.replace(l_prefix, r_prefix)
                if mc.objExists(r_pivot_ctrl):
                    mc.xform(r_pivot_ctrl, a=1, ro=mc.xform(pivot_ctrl, q=1, a=1, ro=1))

        ######################
        # Create  joints

        c_up_jnt_zero, c_up_jnt_plc, c_up_jnt = self.guide_joint('upperLip')
        c_lo_jnt_zero, c_lo_jnt_plc, c_lo_jnt = self.guide_joint('lowerLip')
        r_corner_jnt_zero, r_corner_jnt_plc, r_corner_jnt = self.guide_joint('lipCorner', alt_prefix=r_prefix)
        l_corner_jnt_zero, l_corner_jnt_plc, l_corner_jnt = self.guide_joint('lipCorner', alt_prefix=l_prefix)

        up_jnts_zeros = [r_corner_jnt_zero]
        lo_jnts_zeros = [r_corner_jnt_zero]

        for i in reversed(range(up_number_joints)):
            ltr = utils.letters[i]
            up_jnt_zero, up_jnt_plc, up_jnt = self.guide_joint('upperLip_'+ltr, alt_prefix=r_prefix)
            up_jnts_zeros.append(up_jnt_zero)

        for i in reversed(range(lo_number_joints)):
            ltr = utils.letters[i]
            lo_jnt_zero, lo_jnt_plc, lo_jnt = self.guide_joint('lowerLip_'+ltr, alt_prefix=r_prefix)
            lo_jnts_zeros.append(lo_jnt_zero)

        up_jnts_zeros.append(c_up_jnt_zero)
        lo_jnts_zeros.append(c_lo_jnt_zero)

        for i in range(up_number_joints):
            ltr = utils.letters[i]
            up_jnt_zero, up_jnt_plc, up_jnt = self.guide_joint('upperLip_'+ltr, alt_prefix=l_prefix)
            up_jnts_zeros.append(up_jnt_zero)

        for i in range(lo_number_joints):
            ltr = utils.letters[i]
            lo_jnt_zero, lo_jnt_plc, lo_jnt = self.guide_joint('lowerLip_'+ltr, alt_prefix=l_prefix)
            lo_jnts_zeros.append(lo_jnt_zero)

        up_jnts_zeros.append(l_corner_jnt_zero)
        lo_jnts_zeros.append(l_corner_jnt_zero)

        # position joints
        up_number_joints = len(up_jnts_zeros)
        lo_number_joints = len(lo_jnts_zeros)
        up_jnts_pos = utils.get_uniform_spacing_on_curve(up_pri_crv, up_number_joints)
        lo_jnts_pos = utils.get_uniform_spacing_on_curve(lo_pri_crv, lo_number_joints)

        for i, zero in enumerate(up_jnts_zeros):
            mc.xform(zero, ws=1, t=up_jnts_pos[i])

        for i, zero in enumerate(lo_jnts_zeros):
            mc.xform(zero, ws=1, t=lo_jnts_pos[i])

        # now orient the pivot ctrls
        for ctrl in up_jnts_zeros + lo_jnts_zeros:
            if ctrl.startswith(l_prefix):

                loc = utils.snap_locator(ctrl)
                mc.delete(mc.pointConstraint(ctrl, loc))

                aim = mc.duplicate(loc)[0]
                up = mc.duplicate(loc)[0]
                mc.xform(up, r=1, t=[0,0,1])
                mc.xform(aim, r=1, t=[0,1,0])

                mp = rivet.motionPath(loc, up_pri_crv, up)
                mc.setAttr(mp+'.upAxis', 2)
                mc.setAttr(mp+'.worldUpType', 3)
                mc.setAttr(mp+'.worldUpVectorY', 0)
                mc.setAttr(mp+'.worldUpVectorZ', 1)

                mc.delete(mc.aimConstraint( aim, ctrl, aim=[0,1,0], u=[0,0,1], wu=[0,0,1], wuo=loc, wut='objectRotation'))

                mc.delete(mp, up, loc, aim)

                r_ctrl = ctrl.replace(l_prefix, r_prefix)

                if mc.objExists(r_ctrl):

                    tmp = mc.createNode('joint')
                    mc.delete(mc.parentConstraint(ctrl, tmp))
                    m_tmp = mc.mirrorJoint(tmp, mirrorBehavior=1, mirrorYZ=1)
                    mc.delete(mc.orientConstraint(m_tmp, r_ctrl), tmp, m_tmp)

        # Create secondary ctrls
        sec_ctrls = []

        for jnt_zero in list(set(up_jnts_zeros+lo_jnts_zeros)):
            plc = jnt_zero.replace('_ZERO','')
            ct_prefix = plc.split('GUIDE')[0]+'GUIDE'
            token = plc.split('GUIDE_')[-1].replace('_JNT_PLC', '')
            token = token.replace('Lip', 'LipSecondary')
            token = token.replace('Corner', 'CornerSecondary')

            zero, ctrl = self.guide_ctrl( token, shape='cube', color='pink', scale=[0.02]*3, axis='Z', alt_prefix=ct_prefix)

            if not plc.startswith(r_prefix):
                mc.delete(mc.pointConstraint(plc, zero))
                mc.delete(mc.orientConstraint(plc, utils.get_parent(ctrl)))

            else:
                mc.setAttr(zero+'.sx', -1)
                mc.delete(mc.pointConstraint(plc, zero))

            sec_ctrls.append(ctrl)

        # orient secondary ctrls
        for ctrl in sec_ctrls:
            if ctrl.startswith(r_prefix):
                l_ctrl = utils.get_parent(ctrl.replace(r_prefix, l_prefix))
                mc.xform(utils.get_parent(ctrl), a=1, ro=mc.xform(l_ctrl, q=1, a=1, ro=1))
                utils.set_attrs(utils.get_parent(ctrl), 't', l=1, k=0)

        for ctrl in up_pri_ctrls+lo_pri_ctrls:
            utils.set_attrs(utils.get_parent(ctrl), 't', l=1, k=0)

        # Create roll plcs
        for jnt_zero in up_jnts_zeros[1:-1] + lo_jnts_zeros[1:-1]:

            roll_crv = up_roll_crv
            mult = 1
            if 'lower' in jnt_zero:
                roll_crv = lo_roll_crv
                mult = -1

            plc = jnt_zero.replace('_ZERO','')
            ct_prefix = plc.split('GUIDE')[0]+'GUIDE'
            token = plc.split('GUIDE_')[-1].replace('_JNT_PLC', '')

            loc = utils.snap_locator(plc)
            mp = rivet.motionPath(loc, roll_crv)
            dist = utils.get_distance(loc, plc)
            mc.delete(mp, loc)

            loc = utils.snap_locator(plc)
            mc.xform(loc, r=1, t=[0,dist*mult,0])
            mp = rivet.motionPath(loc, roll_crv)
            dist = utils.get_distance(loc, plc)
            mc.delete(mp, loc)

            loc = utils.snap_locator(plc)
            mc.xform(loc, r=1, t=[0,dist*mult,0])

            r_zero, r_plc = self.guide_joint(token+'_roll', alt_prefix=ct_prefix, placer_only=1)
            self.tag_as_ref(r_plc)

            mc.delete(mc.pointConstraint(loc, r_zero), loc)

        mc.delete(up_roll_crv, lo_roll_crv, up_pri_crv, lo_pri_crv)

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

        head_ctrl_grp = ctrl_grps[0]
        jaw_ctrl_grp = ctrl_grps[1]

        # Get options
        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)

        number_joints = options.get('numberJoints')
        number_ctrls = options.get('numberCtrls')
        create_zipper = options.get('createZipperControl')
        pickWalk_parent = options.get('pickWalkParent')

        # Get joints nad roll plcacer
        up_jnts = [r_prefix+'_lipCorner_JNT']
        lo_jnts = [r_prefix+'_lipCorner_JNT']
        up_roll_jnts = []
        lo_roll_jnts = []

        for i in reversed(range(number_joints)):
            ltr = utils.letters[i]
            up_jnts.append('{0}_upperLip_{1}_JNT'.format(r_prefix, ltr))
            lo_jnts.append('{0}_lowerLip_{1}_JNT'.format(r_prefix, ltr))
            up_roll_jnts.append('{0}_upperLip_{1}_roll_JNT_PLC_REF'.format(r_prefix, ltr))
            lo_roll_jnts.append('{0}_lowerLip_{1}_roll_JNT_PLC_REF'.format(r_prefix, ltr))


        up_jnts.append('{0}_upperLip_JNT'.format(prefix))
        lo_jnts.append('{0}_lowerLip_JNT'.format(prefix))
        up_roll_jnts.append('{0}_upperLip_roll_JNT_PLC_REF'.format(prefix))
        lo_roll_jnts.append('{0}_lowerLip_roll_JNT_PLC_REF'.format(prefix))

        for i in range(number_joints):
            ltr = utils.letters[i]
            up_jnts.append('{0}_upperLip_{1}_JNT'.format(l_prefix, ltr))
            lo_jnts.append('{0}_lowerLip_{1}_JNT'.format(l_prefix, ltr))
            up_roll_jnts.append('{0}_upperLip_{1}_roll_JNT_PLC_REF'.format(l_prefix, ltr))
            lo_roll_jnts.append('{0}_lowerLip_{1}_roll_JNT_PLC_REF'.format(l_prefix, ltr))

        up_jnts.append('{0}_lipCorner_JNT'.format(l_prefix))
        lo_jnts.append('{0}_lipCorner_JNT'.format(l_prefix))

        # get ctrl names
        up_ctrl_names = [r_prefix+'_lipCorner_CTL']
        lo_ctrl_names = [r_prefix+'_lipCorner_CTL']

        for i in reversed(range(number_ctrls)):
            ltr = utils.letters[i]
            up_ctrl_names.append('{0}_upperLip_{1}_CTL'.format(r_prefix, ltr))
            lo_ctrl_names.append('{0}_lowerLip_{1}_CTL'.format(r_prefix, ltr))

        up_ctrl_names.append('{0}_upperLip_CTL'.format(prefix))
        lo_ctrl_names.append('{0}_lowerLip_CTL'.format(prefix))

        for i in range(number_ctrls):
            ltr = utils.letters[i]
            up_ctrl_names.append('{0}_upperLip_{1}_CTL'.format(l_prefix, ltr))
            lo_ctrl_names.append('{0}_lowerLip_{1}_CTL'.format(l_prefix, ltr))

        up_ctrl_names.append('{0}_lipCorner_CTL'.format(l_prefix))
        lo_ctrl_names.append('{0}_lipCorner_CTL'.format(l_prefix))

        # Creat them
        up_zeros, up_ctrls, up_offsets, up_last_nodes = [], [], [], []

        for name in up_ctrl_names:
            zero, ctrl, offsets, last_node = self.anim_ctrl(name, inherit_scale=True)
            up_zeros.append(zero)
            up_ctrls.append(ctrl)
            up_offsets.append(offsets)
            up_last_nodes.append(last_node)

        lo_zeros = [up_zeros[0]]
        lo_ctrls = [up_ctrls[0]]
        lo_offsets = [up_offsets[0]]
        lo_last_nodes = [up_last_nodes[0]]

        for name in lo_ctrl_names[1:-1]:
            zero, ctrl, offsets, last_node = self.anim_ctrl(name, inherit_scale=True)
            lo_zeros.append(zero)
            lo_ctrls.append(ctrl)
            lo_offsets.append(offsets)
            lo_last_nodes.append(last_node)

        lo_zeros.append(up_zeros[-1])
        lo_ctrls.append(up_ctrls[-1])
        lo_offsets.append(up_offsets[-1])
        lo_last_nodes.append(up_last_nodes[-1])

        # CReate secondary ctrls and controant them tothe joints
        up_sec_zeros, up_sec_ctrls, up_sec_offsets, up_sec_last_nodes = [], [], [], []

        for jnt in up_jnts:
            name = jnt.replace('Corner', 'CornerSecondary').replace('Lip', 'LipSecondary')
            name = name.replace('_JNT', '_CTL')

            zero, ctrl, offsets, last_node = self.anim_ctrl(name, inherit_scale=True)
            up_sec_zeros.append(zero)
            up_sec_ctrls.append(ctrl)
            up_sec_offsets.append(offsets)
            up_sec_last_nodes.append(last_node)

            mc.parentConstraint(last_node, jnt, mo=1, n=jnt+'_prc')
            mc.scaleConstraint(last_node, jnt, mo=1, n=jnt+'_sc')

        lo_sec_zeros = [up_sec_zeros[0]]
        lo_sec_ctrls = [up_sec_ctrls[0]]
        lo_sec_offsets = [up_sec_offsets[0]]
        lo_sec_last_nodes = [up_sec_last_nodes[0]]

        for jnt in lo_jnts[1:-1]:
            name = jnt.replace('Corner', 'CornerSecondary').replace('Lip', 'LipSecondary')
            name = name.replace('_JNT', '_CTL')

            zero, ctrl, offsets, last_node = self.anim_ctrl(name, inherit_scale=True)
            lo_sec_zeros.append(zero)
            lo_sec_ctrls.append(ctrl)
            lo_sec_offsets.append(offsets)
            lo_sec_last_nodes.append(last_node)

            mc.parentConstraint(last_node, jnt, mo=1, n=jnt+'_prc')
            mc.scaleConstraint(last_node, jnt, mo=1, n=jnt+'_sc')

        lo_sec_zeros.append(up_sec_zeros[-1])
        lo_sec_ctrls.append(up_sec_ctrls[-1])
        lo_sec_offsets.append(up_sec_offsets[-1])
        lo_sec_last_nodes.append(up_sec_last_nodes[-1])

        # CReate mouth all ctrl
        mouth_zero, mouth_ctrl, mouth_offsets, mouth_last_node = self.anim_ctrl(prefix+'_mouthAll_CTL', inherit_scale=True)

        if create_zipper:

            l_loc = utils.snap_locator(l_prefix+'_lipZipper_CTL_REF')
            r_loc = utils.snap_locator(r_prefix+'_lipZipper_CTL_REF')

            bb = mc.exactWorldBoundingBox(utils.get_shapes(mouth_ctrl))
            s =( bb[3]-bb[0])
            mc.setAttr(l_loc+'.s', s, s, s)
            mc.setAttr(r_loc+'.s', s, s, s)

            l_zipper_zero, l_zipper_ctrl, l_zipper_offsets, l_zipper_last_node = self.anim_ctrl(l_prefix+'_lipZipper_CTL', match_position=l_loc, inherit_scale=True)
            r_zipper_zero, r_zipper_ctrl, r_zipper_offsets, r_zipper_last_node = self.anim_ctrl(r_prefix+'_lipZipper_CTL', match_position=r_loc, inherit_scale=True)
            mc.delete(l_loc, r_loc)

            mc.parent(l_zipper_zero, r_zipper_zero, mouth_last_node)


        # Create primary ctrls for upper and lower
        result = self.anim_ctrl(prefix+'_uppperLipAll_CTL',
                                inherit_scale=True,
                                ref_shape=prefix+'_upperLip_CTL')
        up_all_zero, up_all_ctrl, up_all_offsets, up_all_last_node = result
        control.create_driven_shape(up_all_ctrl, up_last_nodes, replace=True)

        result = self.anim_ctrl(prefix+'_lowerLipAll_CTL',
                                inherit_scale=True,
                                ref_shape=prefix+'_lowerLip_CTL')
        lo_all_zero, lo_all_ctrl, lo_all_offsets, lo_all_last_node = result
        control.create_driven_shape(lo_all_ctrl, lo_last_nodes, replace=True)

        # Now create the follow nodes for the upper and lower to the mouth all AND the head and jaw hooks
        mc.parent(up_all_zero, lo_all_zero, mouth_last_node)

        up_head_follow = mc.duplicate(up_all_zero, po=1, n=ctrl_grps[0]+'_follow')[0]
        lo_head_follow = mc.duplicate(lo_all_zero, po=1, n=ctrl_grps[1]+'_follow')[0]

        mc.parent(mouth_zero, head_ctrl_grp)
        mc.parent(up_head_follow, lo_head_follow, utils.get_parent(mouth_ctrl))

        mc.parentConstraint(ctrl_grps[0], up_head_follow, mo=1)
        mc.parentConstraint(hooks[-1], lo_head_follow, mo=1)

        mc.connectAttr(up_head_follow+'.t', up_all_zero+'.t')
        mc.connectAttr(up_head_follow+'.r', up_all_zero+'.r')

        mc.connectAttr(lo_head_follow+'.t', lo_all_zero+'.t')
        mc.connectAttr(lo_head_follow+'.r', lo_all_zero+'.r')

        # parent the rest of hte primaries
        mc.parent(up_zeros[0], up_zeros[-1], up_all_ctrl+'_CONST')
        mc.parent(up_zeros[1:-1], up_all_last_node)
        mc.parent(lo_zeros[1:-1], lo_all_last_node)

        # Create blends
        for ctrl in up_ctrls:
            const = ctrl+'_CONST'
            follow_par = mc.duplicate(const, n=const+'_follow_PAR', po=1)[0]
            follow = mc.duplicate(const, n=const+'_follow', po=1)[0]
            static = mc.duplicate(const, n=const+'_static', po=1)[0]

            mc.parent(follow, follow_par)
            mc.parent(follow_par, lo_all_ctrl+'_CONST')

            mc.addAttr(ctrl, ln='headJawBias', min=-1, max=1, k=1)
            prc = mc.parentConstraint(static, follow, const, mo=1)[0]
            mc.setAttr(prc+'.interpType', 2)

            sr = mc.createNode('setRange')

            mc.setAttr(sr+'.maxX', 1)
            mc.setAttr(sr+'.minX', 0)
            mc.setAttr(sr+'.oldMaxX', 1)
            mc.setAttr(sr+'.oldMinX', -1)

            mc.connectAttr(ctrl+'.headJawBias', sr+'.valueX')
            mc.connectAttr(sr+'.outValueX',prc+'.w0')
            utils.connect_reverse(prc+'.w0', prc+'.w1')

        for ctrl in lo_ctrls[1:-1]:
            const = ctrl+'_CONST'
            follow_par = mc.duplicate(const, n=const+'_follow_PAR', po=1)[0]
            follow = mc.duplicate(const, n=const+'_follow', po=1)[0]
            static = mc.duplicate(const, n=const+'_static', po=1)[0]

            mc.parent(follow, follow_par)
            mc.parent(follow_par, up_all_ctrl+'_CONST')

            mc.addAttr(ctrl, ln='headJawBias', min=-1, max=1, k=1)
            prc = mc.parentConstraint(static, follow, const, mo=1)[0]
            mc.setAttr(prc+'.interpType', 2)

            sr = mc.createNode('setRange')

            mc.setAttr(sr+'.maxX', 1)
            mc.setAttr(sr+'.minX', 0)
            mc.setAttr(sr+'.oldMaxX', 1)
            mc.setAttr(sr+'.oldMinX', -1)

            mc.connectAttr(ctrl+'.headJawBias', sr+'.valueX')
            mc.connectAttr(sr+'.outValueX',prc+'.w1')
            utils.connect_reverse(prc+'.w1', prc+'.w0')

        # set defaults
        for ctrl in up_ctrls[1:-1]:
            mc.setAttr(ctrl+'.headJawBias', 0.8)

        for ctrl in lo_ctrls[1:-1]:
            mc.setAttr(ctrl+'.headJawBias', -0.8)

        mc.setAttr(prefix+'_upperLip_CTL.headJawBias', 1)
        mc.setAttr(prefix+'_lowerLip_CTL.headJawBias', -1)

        # CReate curves
        up_crv = utils.create_curve_from_nodes(prefix+'_upperLip_crv', up_last_nodes)
        lo_crv = utils.create_curve_from_nodes(prefix+'_lowerLip_crv', lo_last_nodes)

        up_closed_crv = mc.duplicate(up_crv, n=prefix+'_uppeLipClosed_crv')[0]
        lo_closed_crv = mc.duplicate(lo_crv, n=prefix+'_loweLipClosed_crv')[0]

        #create blend for upper and lower blink curves
        avcs = []
        for bcrv in [up_closed_crv, lo_closed_crv]:
            avc = mc.createNode('avgCurves', n=bcrv+'_avc')
            mc.connectAttr(up_crv+'Shape.worldSpace', avc+'.ic1')
            mc.connectAttr(lo_crv+'Shape.worldSpace', avc+'.ic2')
            mc.connectAttr(avc+'.oc', bcrv+'Shape.create')
            mc.setAttr(avc+'.automaticWeight', 0)
            avcs.append(avc)

        up_cvs = mc.ls(up_crv+'.cv[*]', fl=1)
        for i, cv in enumerate(up_cvs):
            dcmx = mc.createNode('decomposeMatrix')
            mc.connectAttr(up_ctrls[i]+'.worldMatrix', dcmx+'.inputMatrix')
            cPoint = '{0}.controlPoints[{1}]'.format(up_crv, i)
            mc.connectAttr(dcmx+'.outputTranslate', cPoint)

        lo_cvs = mc.ls(lo_crv+'.cv[*]', fl=1)
        for i, cv in enumerate(lo_cvs):
            dcmx = mc.createNode('decomposeMatrix')
            mc.connectAttr(lo_ctrls[i]+'.worldMatrix', dcmx+'.inputMatrix')
            cPoint = '{0}.controlPoints[{1}]'.format(lo_crv, i)
            mc.connectAttr(dcmx+'.outputTranslate', cPoint)

        mc.addAttr(mouth_ctrl, ln='closeMouth', min=0, max=1, k=1)
        mc.addAttr(mouth_ctrl, ln='mouthLine', min=-1, max=1, k=1)
        mc.addAttr(mouth_ctrl, ln='mouthBias', min=-1, max=1, k=1)

        # This is the mouth line bias - it overshoots or under shoots the blink to allow you to create a better seal.
        mc.setAttr(mouth_ctrl+'.mouthBias', 0)
        mc.setAttr(mouth_ctrl+'.mouthLine', 0)

        tt = 'linear'
        up_avc = avcs[0]
        lo_avc = avcs[1]

        mc.setDrivenKeyframe([up_avc+'.w1', up_avc+'.w2'], cd=mouth_ctrl+'.mouthBias', itt=tt, ott=tt, dv=0)
        mc.setDrivenKeyframe([lo_avc+'.w1', lo_avc+'.w2'], cd=mouth_ctrl+'.mouthBias', itt=tt, ott=tt, dv=0)

        mc.setAttr(up_avc+'.w1', 0)
        mc.setAttr(up_avc+'.w2', 1)
        mc.setAttr(lo_avc+'.w1', 1)
        mc.setAttr(lo_avc+'.w2', 0)
        mc.setDrivenKeyframe([up_avc+'.w1', up_avc+'.w2'], cd=mouth_ctrl+'.mouthBias', itt=tt, ott=tt, dv=1)
        mc.setDrivenKeyframe([lo_avc+'.w1', lo_avc+'.w2'], cd=mouth_ctrl+'.mouthBias', itt=tt, ott=tt, dv=1)

        mc.setAttr(up_avc+'.w1', 1)
        mc.setAttr(up_avc+'.w2', 0)
        mc.setAttr(lo_avc+'.w1', 0)
        mc.setAttr(lo_avc+'.w2', 1)
        mc.setDrivenKeyframe([up_avc+'.w1', up_avc+'.w2'], cd=mouth_ctrl+'.mouthBias', itt=tt, ott=tt, dv=-1)
        mc.setDrivenKeyframe([lo_avc+'.w1', lo_avc+'.w2'], cd=mouth_ctrl+'.mouthBias', itt=tt, ott=tt, dv=-1)

        # connect blink blend
        mc.setAttr(mouth_ctrl+'.mouthBias', 1)
        mc.setAttr(mouth_ctrl+'.mouthBias', 0)
        mc.setDrivenKeyframe(up_avc+'.w1', dv=1, v=1.5, cd=mouth_ctrl+'.mouthLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(up_avc+'.w1', dv=-1, v=-0.5, cd=mouth_ctrl+'.mouthLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(up_avc+'.w2', dv=1, v=-0.5, cd=mouth_ctrl+'.mouthLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(up_avc+'.w2', dv=-1, v=1.5, cd=mouth_ctrl+'.mouthLine', itt=tt, ott=tt)

        mc.setDrivenKeyframe(lo_avc+'.w1', dv=1, v=1.5, cd=mouth_ctrl+'.mouthLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(lo_avc+'.w1', dv=-1, v=-0.5, cd=mouth_ctrl+'.mouthLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(lo_avc+'.w2', dv=1, v=-0.5, cd=mouth_ctrl+'.mouthLine', itt=tt, ott=tt)
        mc.setDrivenKeyframe(lo_avc+'.w2', dv=-1, v=1.5, cd=mouth_ctrl+'.mouthLine', itt=tt, ott=tt)
        mc.setAttr(mouth_ctrl+'.mouthLine', 0)
        mc.setAttr(mouth_ctrl+'.mouthBias', 0)

        # Parent and connect the secondarey contrls
        mc.parent(up_sec_zeros[1:-1], up_all_last_node)
        mc.parent(lo_sec_zeros[1:-1], lo_all_last_node)

        self.connect_lip_jnts(up_sec_zeros[1:-1], up_crv, up_closed_crv, mouth_ctrl, up_all_last_node, lo_all_last_node, noxform_grp)
        self.connect_lip_jnts(lo_sec_zeros[1:-1], lo_crv, lo_closed_crv, mouth_ctrl, up_all_last_node, lo_all_last_node, noxform_grp, lower=True)

        #if not create_zipper:
        for zero in up_sec_zeros[1:-1]+lo_sec_zeros[1:-1]:
            mc.connectAttr(mouth_ctrl+'.closeMouth', zero+'.closeLip')

        mc.parent(up_crv, lo_crv, up_closed_crv, lo_closed_crv, noxform_grp)

        mc.parent(up_sec_zeros[0], up_last_nodes[0])
        mc.parent(up_sec_zeros[-1], up_last_nodes[-1])

        # Create roll nodes
        for ctrl in up_sec_ctrls[1:-1]+lo_sec_ctrls[1:-1]:

            roll_ref = ctrl.replace('Secondary', '')
            roll_ref = roll_ref.replace('_CTL', '_roll_JNT_PLC_REF')

            roll_par = mc.createNode('transform', n=ctrl+'_ROLL_PAR')
            roll = mc.createNode('transform', n=ctrl+'_ROLL', p=roll_par)
            mc.delete(mc.pointConstraint(roll_ref, roll_par))

            mc.parent(roll_par, ctrl+'_B_CONST')
            mc.parent(ctrl+'_MOCAP', roll)

            mc.addAttr(ctrl, ln='roll', k=1)
            mc.addAttr(ctrl, ln='allRoll', k=1)
            mc.addAttr(ctrl, ln='primaryRoll', k=1)

            pma = mc.createNode('plusMinusAverage')
            mc.connectAttr(ctrl+'.roll', pma+'.input1D[0]')
            mc.connectAttr(ctrl+'.allRoll', pma+'.input1D[1]')
            mc.connectAttr(ctrl+'.primaryRoll', pma+'.input1D[2]')

            if 'upper' in ctrl:
                utils.connect_negative(pma+'.output1D', roll+'.rx' )
            else:
                mc.connectAttr(pma+'.output1D', roll+'.rx' )

        # SDK all and primary rolls
        mc.addAttr(up_all_ctrl, ln='roll', k=1)
        mc.addAttr(lo_all_ctrl, ln='roll', k=1)
        mc.addAttr(up_ctrls[1:-1], ln='roll', k=1)
        mc.addAttr(lo_ctrls[1:-1], ln='roll', k=1)

        self.roll_sdk_ramp(up_ctrls, up_sec_ctrls, 'primaryRoll', 4)
        self.roll_sdk_ramp(lo_ctrls, lo_sec_ctrls, 'primaryRoll', 4)

        self.roll_sdk_ramp([up_ctrls[0], up_all_ctrl, up_ctrls[-1]], up_sec_ctrls, 'allRoll', 5)
        self.roll_sdk_ramp([lo_ctrls[0], lo_all_ctrl, lo_ctrls[-1]], lo_sec_ctrls, 'allRoll', 5)

        self.scale_sdk_ramp(up_ctrls, [s+'_OFF' for s in up_sec_ctrls[1:-1]], 4)
        self.scale_sdk_ramp(lo_ctrls, [s+'_OFF' for s in lo_sec_ctrls[1:-1]], 4)

        # Pi solvers
        self.pi_corner_solver([up_ctrls[0], up_ctrls[-1]], exp_name=prefix+'_mouth_piSolver_EXP')

        # parent joints
        up_lip_grp = mc.createNode('transform', p=jnt_grps[0], n=prefix+'_upperLip_JNT_GRP')
        lo_lip_grp = mc.createNode('transform', p=jnt_grps[0], n=prefix+'_lowerLip_JNT_GRP')

        mc.parent(up_jnts, up_lip_grp)
        mc.parent(lo_jnts, lo_lip_grp)


        ######################################################################
        ######################################################################
        ######################################################################

        # lips zipper
        if create_zipper:

            mm.eval('transformLimits -tx -1 0 -etx 1 1 '+l_zipper_ctrl)
            mm.eval('transformLimits -tx 0 1 -etx 1 1 '+r_zipper_ctrl)

            mc.addAttr(l_zipper_ctrl, r_zipper_ctrl, ln='falloff', min=0, max=1, k=1, dv=1)
            utils.set_attrs([l_zipper_ctrl, r_zipper_ctrl], k=0, l=1)
            utils.set_attrs([l_zipper_ctrl, r_zipper_ctrl], 'tx falloff', k=1, l=0)


            # LEFT sdk
            up_zip_ctrls = [n+'_ZERO' for n in up_sec_ctrls if 'CornerSecondary' not in n]
            lo_zip_ctrls = [n+'_ZERO' for n in lo_sec_ctrls if 'CornerSecondary' not in n]

            utils.break_connections([c for c in up_zip_ctrls+lo_zip_ctrls], 'closeLipSharp')
            utils.break_connections([c for c in up_zip_ctrls+lo_zip_ctrls], 'closeLipSoft')

            up_zip_ctrls = [None]+up_zip_ctrls+[None]
            up_zip_ctrls.reverse()

            lo_zip_ctrls = [None]+lo_zip_ctrls+[None]
            lo_zip_ctrls.reverse()

            div = 1.0 / (len(up_zip_ctrls)-2)
            dv_start = 0.0

            up_btas = [None]
            lo_btas = [None]

            for i, ctrl in enumerate(up_zip_ctrls):
                dv_end = i * -div

                if ctrl:

                    try:
                        mc.addAttr(up_zip_ctrls[i], lo_zip_ctrls[i], ln='closeLipSharp', min=0, max=1, k=1)
                        mc.addAttr(up_zip_ctrls[i], lo_zip_ctrls[i], ln='closeLipSoft', min=0, max=1, k=1)
                    except:
                        pass


                    s_dv_end = dv_end+(2*-div)
                    if s_dv_end < -1:
                        s_dv_end = -1

                    mc.setDrivenKeyframe(up_zip_ctrls[i]+'.closeLipSharp', dv=dv_start, v=0, cd=l_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(up_zip_ctrls[i]+'.closeLipSharp', dv=s_dv_end,   v=1, cd=l_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(lo_zip_ctrls[i]+'.closeLipSharp', dv=dv_start, v=0, cd=l_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(lo_zip_ctrls[i]+'.closeLipSharp', dv=s_dv_end  , v=1, cd=l_zipper_ctrl+'.tx', itt='flat', ott='flat')

                    s_dv_end = dv_end+(5*-div)
                    if s_dv_end < -1:
                        s_dv_end = -1

                    mc.setDrivenKeyframe(up_zip_ctrls[i]+'.closeLipSoft', dv=dv_start, v=0, cd=l_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(up_zip_ctrls[i]+'.closeLipSoft', dv=s_dv_end,   v=1, cd=l_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(lo_zip_ctrls[i]+'.closeLipSoft', dv=dv_start, v=0, cd=l_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(lo_zip_ctrls[i]+'.closeLipSoft', dv=s_dv_end  , v=1, cd=l_zipper_ctrl+'.tx', itt='flat', ott='flat')

                    dv_start = float(dv_end)

                    # Create blend
                    u_bta = mc.createNode('blendTwoAttr')
                    mc.connectAttr(up_zip_ctrls[i]+'.closeLipSharp', u_bta+'.input[0]')
                    mc.connectAttr(up_zip_ctrls[i]+'.closeLipSoft', u_bta+'.input[1]')
                    mc.connectAttr(l_zipper_ctrl+'.falloff', u_bta+'.attributesBlender')

                    l_bta = mc.createNode('blendTwoAttr')
                    mc.connectAttr(lo_zip_ctrls[i]+'.closeLipSharp', l_bta+'.input[0]')
                    mc.connectAttr(lo_zip_ctrls[i]+'.closeLipSoft', l_bta+'.input[1]')
                    mc.connectAttr(l_zipper_ctrl+'.falloff', l_bta+'.attributesBlender')

                    up_btas.append(u_bta)
                    lo_btas.append(l_bta)

            up_btas.append(None)
            up_btas.reverse()

            lo_btas.append(None)
            lo_btas.reverse()


            # RIGHT sdk
            up_zip_ctrls = [n+'_ZERO' for n in up_sec_ctrls if 'CornerSecondary' not in n]
            lo_zip_ctrls = [n+'_ZERO' for n in lo_sec_ctrls if 'CornerSecondary' not in n]

            up_zip_ctrls = [None]+up_zip_ctrls+[None]
            lo_zip_ctrls = [None]+lo_zip_ctrls+[None]

            div = 1.0 / (len(up_zip_ctrls)-2)
            dv_start = 0.0

            for i, ctrl in enumerate(up_zip_ctrls):
                dv_end = i * div

                if ctrl:

                    s_dv_end = dv_end+(2*div)
                    if s_dv_end > 1:
                        s_dv_end = 1

                    mc.setDrivenKeyframe(up_zip_ctrls[i]+'.closeLipSharp', dv=dv_start, v=0, cd=r_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(up_zip_ctrls[i]+'.closeLipSharp', dv=s_dv_end,   v=1, cd=r_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(lo_zip_ctrls[i]+'.closeLipSharp', dv=dv_start, v=0, cd=r_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(lo_zip_ctrls[i]+'.closeLipSharp', dv=s_dv_end  , v=1, cd=r_zipper_ctrl+'.tx', itt='flat', ott='flat')

                    s_dv_end = dv_end+(5*div)
                    if s_dv_end > 1:
                        s_dv_end = 1

                    mc.setDrivenKeyframe(up_zip_ctrls[i]+'.closeLipSoft', dv=dv_start, v=0, cd=r_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(up_zip_ctrls[i]+'.closeLipSoft', dv=s_dv_end,   v=1, cd=r_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(lo_zip_ctrls[i]+'.closeLipSoft', dv=dv_start, v=0, cd=r_zipper_ctrl+'.tx', itt='flat', ott='flat')
                    mc.setDrivenKeyframe(lo_zip_ctrls[i]+'.closeLipSoft', dv=s_dv_end  , v=1, cd=r_zipper_ctrl+'.tx', itt='flat', ott='flat')

                    dv_start = float(dv_end)

                    # Create blend
                    u_bta = mc.createNode('blendTwoAttr')
                    mc.connectAttr(up_zip_ctrls[i]+'.closeLipSharp', u_bta+'.input[0]')
                    mc.connectAttr(up_zip_ctrls[i]+'.closeLipSoft', u_bta+'.input[1]')
                    mc.connectAttr(r_zipper_ctrl+'.falloff', u_bta+'.attributesBlender')

                    l_bta = mc.createNode('blendTwoAttr')
                    mc.connectAttr(lo_zip_ctrls[i]+'.closeLipSharp', l_bta+'.input[0]')
                    mc.connectAttr(lo_zip_ctrls[i]+'.closeLipSoft', l_bta+'.input[1]')
                    mc.connectAttr(r_zipper_ctrl+'.falloff', l_bta+'.attributesBlender')

                    uadl = mc.createNode('plusMinusAverage')
                    ladl = mc.createNode('plusMinusAverage')
                    clamp = mc.createNode('clamp')
                    mc.setAttr(clamp+'.max', 1,1,1)

                    mc.connectAttr(u_bta+'.output', uadl+'.input1D[0]')
                    mc.connectAttr(up_btas[i]+'.output', uadl+'.input1D[1]')
                    mc.connectAttr(mouth_ctrl+'.closeMouth', uadl+'.input1D[2]')
                    mc.connectAttr(uadl+'.output1D', clamp+'.inputR')

                    mc.connectAttr(l_bta+'.output', ladl+'.input1D[0]')
                    mc.connectAttr(lo_btas[i]+'.output', ladl+'.input1D[1]')
                    mc.connectAttr(mouth_ctrl+'.closeMouth', ladl+'.input1D[2]')
                    mc.connectAttr(ladl+'.output1D', clamp+'.inputG')

                    mc.connectAttr(clamp+'.outputR', up_zip_ctrls[i]+'.closeLip', f=1)
                    mc.connectAttr(clamp+'.outputG', lo_zip_ctrls[i]+'.closeLip', f=1)


        #Setup pickwalk tagging

        for ctrl in up_ctrls + up_sec_ctrls:
            pickWalk.attribute_tag(ctrl,up_all_ctrl)

        for ctrl in lo_ctrls + lo_sec_ctrls:
            pickWalk.attribute_tag(ctrl,lo_all_ctrl)

        pickWalk.attribute_tag(up_all_ctrl, mouth_ctrl)
        pickWalk.attribute_tag(lo_all_ctrl, mouth_ctrl)

        pickWalk.attribute_tag(mouth_ctrl, pickWalk_parent)

        # This finalizes the rig and creates rig sets
        self.finalize_part()

    def rebuild_guide_post(self):

        prefix = self.prefix
        l_prefix = prefix.replace('C','L', 1)
        r_prefix = prefix.replace('C','R', 1)

        ctrls = mc.ls(prefix+'_*LipSecondary_*PIV_CTL',
                      l_prefix+'_*LipSecondary_*_PIV_CTL',
                      r_prefix+'_*LipSecondary_*_PIV_CTL')

        for ctrl in ctrls:
            plc = ctrl.replace('Secondary','').replace('PIV_CTL','JNT_PLC')
            con = mc.parentConstraint(plc, ctrl, mo=1)[0]
            mc.xform(plc, a=1, t=[0,0,0], ro=[0,0,0])
            mc.delete(con)

        ctrls = mc.ls(l_prefix+'_*Lip_*_PIV_CTL',
                      r_prefix+'_*Lip_*_PIV_CTL')
        mc.xform(ctrls, a=1, t=[0,0,0])

        plcs = mc.ls(l_prefix+'*Lip_*_roll_JNT_PLC',
                     r_prefix+'*Lip_*_roll_JNT_PLC')

        mc.xform(plcs, a=1, t=[0,0,0])

    @classmethod
    def connect_lip_jnts(self, zeros, open_crv, close_crv, mouth_ctrl, up_all_last_node, lo_all_last_node, noxform_grp, lower=False):

        tt = 'linear'

        for zero in zeros:

            # This is the master attr  that ctrls whjether this ctrl is closed / zipped or open
            mc.addAttr(zero, ln='closeLip', min=0, max=1, k=1)

            # create mpx
            open_world_mpx = mc.createNode('transform', n=zero+'_ompx', p=noxform_grp)
            closed_world_mpx = mc.createNode('transform', n=zero+'_bmpx', p=noxform_grp)

            mc.delete(mc.pointConstraint(zero, open_world_mpx))
            mc.delete(mc.pointConstraint(zero, closed_world_mpx))

            open_mp = rivet.motionPath(open_world_mpx, open_crv)
            closed_mp = rivet.motionPath(closed_world_mpx, close_crv)

            # create orient nodes so that the sub ctrls orient to either the head (when opened) or jaw when closed
            const = zero.replace('_ZERO','_CONST')

            # insert another group under
            child = utils.get_children(const)
            crv_const = mc.group(child[0], n=const.replace('_CONST', '_B_CONST'))
            mc.xform(crv_const, piv=[0,0,0])

            head_follow_par = mc.duplicate(const, n=const+'_head_follow_PAR', po=1)[0]
            head_follow = mc.duplicate(const, n=const+'_head_follow', po=1)[0]

            jaw_follow_par = mc.duplicate(const, n=const+'_jaw_follow_PAR', po=1)[0]
            jaw_follow = mc.duplicate(const, n=const+'_jaw_follow', po=1)[0]

            mc.parent(head_follow, head_follow_par)
            mc.parent(jaw_follow, jaw_follow_par)

            mc.parent(head_follow_par, up_all_last_node)
            mc.parent(jaw_follow_par, lo_all_last_node)

            # this is the main parent constraint oty handle the orientations and overall parent matrix
            prc = mc.parentConstraint(head_follow, jaw_follow, const)[0]
            mc.setAttr(prc+'.interpType', 2)

            mdl = mc.createNode('multDoubleLinear')
            mc.connectAttr(zero+'.closeLip', mdl+'.input1')

            if lower:

                mc.setDrivenKeyframe(mdl+'.input2', cd=mouth_ctrl+'.mouthLine', dv=0, v=0.5, itt=tt, ott=tt)
                mc.setDrivenKeyframe(mdl+'.input2', cd=mouth_ctrl+'.mouthLine', dv=-1, v=0, itt=tt, ott=tt)
                mc.setDrivenKeyframe(mdl+'.input2', cd=mouth_ctrl+'.mouthLine', dv=1, v=1, itt=tt, ott=tt)

                mc.connectAttr(mdl+'.output', prc+'.w0')
                utils.connect_reverse(prc+'.w0', prc+'.w1')

            else:

                mc.setDrivenKeyframe(mdl+'.input2', cd=mouth_ctrl+'.mouthLine', dv=0, v=0.5, itt=tt, ott=tt)
                mc.setDrivenKeyframe(mdl+'.input2', cd=mouth_ctrl+'.mouthLine', dv=1, v=0, itt=tt, ott=tt)
                mc.setDrivenKeyframe(mdl+'.input2', cd=mouth_ctrl+'.mouthLine', dv=-1, v=1, itt=tt, ott=tt)

                mc.connectAttr(mdl+'.output', prc+'.w1')
                utils.connect_reverse(prc+'.w1', prc+'.w0')

            # Now that overall orienation and pos matrix is taken care of. we need to stick it the curve (point only)
            pc = mc.pointConstraint(open_world_mpx, closed_world_mpx, crv_const)[0]
            mc.connectAttr(zero+'.closeLip', pc+'.w1')
            utils.connect_reverse(pc+'.w1', pc+'.w0')

    @classmethod
    def roll_sdk_ramp(self, pri_ctrls, sec_ctrls, driven_attr, interpolation=1):

        #create attrs
        number_ctrls = len(pri_ctrls)
        number_sec_ctrls = len(sec_ctrls)
        ramps = []

        # create ramps
        div = 1.0 / (number_ctrls-1)
        for i in range(number_ctrls):
            pre = (i-1) * div
            post = (i+1) * div
            current = i * div

            ramp = mc.createNode ('ramp', n=pri_ctrls[i]+'_ramp')
            mc.setAttr(ramp+'.colorEntryList[0].color', 0,0,0, type='double3')
            mc.setAttr(ramp+'.colorEntryList[1].color', 1,1,1,type='double3')
            mc.setAttr(ramp+'.colorEntryList[2].color', 0,0,0, type='double3')
            mc.setAttr(ramp+'.colorEntryList[0].position', max(min(1, pre), 0) )
            mc.setAttr(ramp+'.colorEntryList[1].position', current)
            mc.setAttr(ramp+'.colorEntryList[2].position', max(min(1, post), 0))
            mc.setAttr(ramp+'.interpolation', interpolation)
            ramps.append(ramp)

        mc.removeMultiInstance(ramps[-1]+'.colorEntryList[2]', b=True)
        mc.removeMultiInstance(ramps[0]+'.colorEntryList[0]', b=True)

        # setup joint twist and Scale readers//
        div = 1.0 / (number_sec_ctrls-1)

        tt = 'spline'
        sdk_crvs = []

        for i in range(number_ctrls):
            roll_driver_attr = pri_ctrls[i]+'.roll'
            if not mc.objExists(roll_driver_attr):
                    continue

            for ji in range(number_sec_ctrls):

                roll_attr = sec_ctrls[ji]+'.'+driven_attr
                if not mc.objExists(roll_attr):
                    continue

                mc.setAttr(ramps[i]+'.vCoord', div*ji)
                value = mc.getAttr(ramps[i]+'.outColorR')

                mc.setDrivenKeyframe(roll_attr, cd=roll_driver_attr, dv=0, v=0, ott=tt, itt=tt)
                mc.setDrivenKeyframe(roll_attr, cd=roll_driver_attr, dv=1, v=value, ott=tt, itt=tt)\

            sdk_crvs.extend(mc.listConnections(roll_driver_attr, type='animCurve', scn=1) )

        # set infinity
        mc.delete(ramps)

        if sdk_crvs:
            mc.selectKey(sdk_crvs)
            mc.setInfinity(poi='linear', pri='linear')


    @classmethod
    def pi_corner_solver(self, ctrls, axis='XY', exp_name='mouth_piSolver_EXP'):

        ctrls = mc.ls(ctrls)

        side = axis[0].upper()
        up = axis[1].upper()

        arg = ''

        for ctrl in ctrls:

            arg += '// PI SOLVER: {0}\n'.format(ctrl)
            mc.addAttr(ctrl, ln=side+'Mult', at='double', k=1, dv=1, min=1)
            mc.addAttr(ctrl, ln=up+'Mult', at='double', k=1, dv=1, min=1)

            mc.addAttr(ctrl, ln=side, at='double', k=1)
            mc.addAttr(ctrl, ln=up, at='double', k=1)

            labels = [ 'up', 'upOut', 'out', 'downOut', 'down', 'downIn', 'in', 'upIn']
            for label in labels:
                mc.addAttr(ctrl, ln=label, min=0, at='double', k=1)

            arg += '{0}.{1} = clamp(-1, 1, {0}.translate{1} * (1.0 / {0}.{1}Mult));\n'.format(ctrl, side)
            arg += '{0}.{1} = clamp(-1, 1, {0}.translate{1} * (1.0 / {0}.{1}Mult));\n'.format(ctrl, up)
            arg += '{0}.up = clamp( 0, 1, ({0}.{2} * 1) - abs({0}.{1}) );\n'.format(ctrl, side, up)
            arg += '{0}.down = clamp( 0, 1, ({0}.{2} *-1) - abs({0}.{1}) );\n'.format(ctrl, side, up)
            arg += '{0}.out = clamp( 0, 1, ({0}.{1} * 1) - abs({0}.{2}) );\n'.format(ctrl, side, up)
            arg += '{0}.in = clamp( 0, 1, ({0}.{1} *-1) - abs({0}.{2}) );\n'.format(ctrl, side, up)

            arg += 'if ({0}.{2} > 0 && {0}.{1} > 0) {0}.upOut = clamp(0,1,  {0}.{1} - {0}.out );\n'.format(ctrl, side, up)
            arg += 'else   {0}.upOut = 0;\n'.format(ctrl, side, up)
            arg += 'if ({0}.{2} > 0 && {0}.{1} < 0) {0}.upIn = clamp(0,1, -{0}.{1} - {0}.in );\n'.format(ctrl, side, up)
            arg += 'else   {0}.upIn = 0;\n'.format(ctrl, side, up)
            arg += 'if ({0}.{2} < 0 && {0}.{1} > 0) {0}.downOut = clamp(0,1,  {0}.{1} - {0}.out );\n'.format(ctrl, side, up)
            arg += 'else  {0}.downOut = 0;\n'.format(ctrl, side, up)
            arg += 'if ({0}.{2} < 0 && {0}.{1} < 0) {0}.downIn = clamp(0,1, -{0}.{1} - {0}.in );\n'.format(ctrl, side, up)
            arg += 'else  {0}.downIn = 0;\n\n'.format(ctrl, side, up)

        mc.expression(n=exp_name, s=arg)

    @classmethod
    def scale_sdk_ramp(self, pri_ctrls, sec_ctrls, interpolation=1):

        #create attrs
        number_ctrls = len(pri_ctrls)
        number_sec_ctrls = len(sec_ctrls)
        ramps = []

        # create ramps
        div = 1.0 / (number_ctrls-1)
        for i in range(number_ctrls):
            pre = (i-1) * div
            post = (i+1) * div
            current = i * div

            ramp = mc.createNode ('ramp', n=pri_ctrls[i]+'_ramp')
            mc.setAttr(ramp+'.colorEntryList[0].color', 0,0,0, type='double3')
            mc.setAttr(ramp+'.colorEntryList[1].color', 1,1,1,type='double3')
            mc.setAttr(ramp+'.colorEntryList[2].color', 0,0,0, type='double3')
            mc.setAttr(ramp+'.colorEntryList[0].position', max(min(1, pre), 0) )
            mc.setAttr(ramp+'.colorEntryList[1].position', current)
            mc.setAttr(ramp+'.colorEntryList[2].position', max(min(1, post), 0))
            mc.setAttr(ramp+'.interpolation', interpolation)
            ramps.append(ramp)

        mc.removeMultiInstance(ramps[-1]+'.colorEntryList[2]', b=True)
        mc.removeMultiInstance(ramps[0]+'.colorEntryList[0]', b=True)

        # setup joint twist and Scale readers//
        div = 1.0 / (number_sec_ctrls-1)

        tt = 'spline'
        sdk_crvs = []

        for i in range(number_ctrls):
            for dattr in ['sx', 'sy', 'sz']:
                roll_driver_attr = pri_ctrls[i]+'.'+dattr
                if not mc.objExists(roll_driver_attr):
                        continue

                for ji in range(number_sec_ctrls):

                    roll_attr = sec_ctrls[ji]+'.'+dattr
                    if not mc.objExists(roll_attr):
                        continue

                    mc.setAttr(ramps[i]+'.vCoord', div*ji)
                    value = mc.getAttr(ramps[i]+'.outColorR')

                    mc.setDrivenKeyframe(roll_attr, cd=roll_driver_attr, dv=0, v=0, ott=tt, itt=tt)
                    mc.setDrivenKeyframe(roll_attr, cd=roll_driver_attr, dv=1, v=value, ott=tt, itt=tt)\

                sdk_crvs.extend(mc.listConnections(roll_driver_attr, type='animCurve', scn=1) )

        # set infinity
        mc.delete(ramps)

        if sdk_crvs:
            mc.selectKey(sdk_crvs)
            mc.setInfinity(poi='linear', pri='linear')

