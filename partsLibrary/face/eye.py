# -*- rigBot: part -*-

import maya.OpenMaya as om
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import pickWalk
from rigBot.partsLibrary import standardPart

class Eye(standardPart.StandardPart):
    """Eye module. Build eye joint, fk eye control and look at ctrl.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_head_JNT".
            :centerLookAtControl: (str) Center look at ctrl to drive individual left and right aim controls. Defaults to "C_lookAt_CTL".
            :eyeBallCenter: (list) Center Point of the eyeball. Used for initial placement. Defaults to [].
            :pupilCenter: (list) Center Point of the pupil. Used for initial placement. Defaults to []."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('parent', data_type='hook', default='C_head_JNT')
        self.add_option('centerLookAtControl',
                         data_type='hook',
                         default='C_lookAt_CTL',
                         tool_tip='Center look at ctrl to drive individual left and right aim controls.')

        self.add_option('eyeBallCenter',
                         data_type='selection',
                         tool_tip='Center Point of the eyeball. Used for initial placement.')

        self.add_option('pupilCenter',
                         data_type='selection',
                         tool_tip='Center Point of the pupil. Used for initial placement.')

        self.add_option('createSquashCtrl', data_type='bool', default=False, rebuild_to_modify=True)

        self.add_option('pickWalkParent',
                        data_type='string',
                        selectable=True,
                        default = 'C_lookAt_CTL',
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")

    def build_guide(self, **kwargs):
        """This builds your guide. Use KWARGS to update any options at build time."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix = self.prefix              # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options = self.options            # Build options
        mirror_value = self.mirror_value  # 1.0 for left and center sided parts and -1.0 for right sided part.

        eye_center = mc.ls(options.get('eyeBallCenter'), fl=1)
        pupil_center = mc.ls(options.get('pupilCenter'), fl=1)

        create_squash = options.get('createSquashCtrl')

        # Start coding suckka !!
        eye_pos = [0, 0, 0]
        pupil_pos = [0, 0, 0.5]

        if eye_center:
            loc = utils.snap_locator(eye_center)
            eye_pos = mc.xform(loc, ws=1, q=1, t=1)
            mc.delete(loc)

        if pupil_center:
            loc = utils.snap_locator(pupil_center)
            pupil_pos = mc.xform(loc, ws=1, q=1, t=1)
            mc.delete(loc)

        v1 = om.MVector(eye_pos[0], eye_pos[1], eye_pos[2])
        v2 = om.MVector(pupil_pos[0], pupil_pos[1], pupil_pos[2])
        dist = om.MVector(v2 - v1).length()

        jnt_zeros, plcs, jnts = self.guide_joint_chain('eye', num_joints=2)

        # rotate to face up
        jnt_grp = utils.get_parent(jnt_zeros[0])
        grp = mc.group(jnt_zeros)
        mc.xform(grp, piv=[0,0,0])
        mc.xform(grp, r=1, ro=[0,-90,0])
        mc.xform(grp, r=1, t=[0,0,-1])

        mc.parent(jnt_zeros, jnt_grp)
        mc.delete(grp)

        mc.setAttr(self.guide_master+'.offsetTranslateZ', mirror_value*-0.5)

        # Create fk ctrl
        look_at_zero, eye_fk_ctrl = self.guide_ctrl(name='eye_FK',
                                                    shape='cone',
                                                    color='dark_purple',
                                                    driver=jnts[1],
                                                    axis='-X',
                                                    create_pivot=False,
                                                    scale=[0.5*dist]*3)

        mc.xform(eye_fk_ctrl+'.cv[*]', r=1, t=[dist*0.25,0,0])

        look_at_zero, look_at_ctrl = self.guide_ctrl(name='lookAt',
                                                    shape='circle',
                                                    color='cyan',
                                                    axis='Z',
                                                    create_pivot=False,
                                                    scale=[dist]*3)

        mc.xform(look_at_zero, r=1, t=[0,0,dist*5])

        if create_squash:
            s_zero, s_ctrl = self.guide_ctrl(name='eye_squash',
                                             shape='star',
                                             color='pink',
                                             driver=jnts[1],
                                             axis='-X',
                                             create_pivot=False,
                                             scale=[0.5*dist]*3)

            cvs = [s_ctrl+'.cv[0]', s_ctrl+'.cv[2]', s_ctrl+'.cv[4]', 
                   s_ctrl+'.cv[6]', s_ctrl+'.cv[8]', s_ctrl+'.cv[10]']

            mc.xform(cvs, r=1, s=[1.5]*3)

        # position
        mc.xform(self.guide_master, ws=1, t=eye_pos)
        mc.xform(jnt_zeros[1], ws=1, t=pupil_pos)

        # This finalizes your guide.
        self.finalize_guide()

    def build_rig(self):
        """This builds your anim rig."""

        # create rig part top nodes
        self.create_part_master()

        prefix            = self.prefix                 # Naming prefix. Use this for every new node you create and there should be no name clashes.
        options           = self.options                # Build options
        anim_ctrls        = self.anim_ctrls             # Anim controls in this part
        jnts      = self.bind_joints            # Bind joints in this rig part
        world_scale_attr  = self.hooks[0]+'.worldScale' # World scale multiplier (Each hooks has it's own world scale)
        hooks             = self.hooks                  # A hook grp is created per hook attribute.
        ctrl_grps         = self.ctrl_grps              # A ctrl group is created per hook. Parent controls here.
        jnt_grps          = self.jnt_grps               # A joint groupd is created per hook. Parent joints here.
        noxform_grp       = self.noxform_grp            # No scale, no transform group for this rig part.
        mirror_value      = self.mirror_value           # 1.0 for left and center sided parts and -1.0 for right sided part.

        pickWalk_parent = options.get('pickWalkParent')
        create_squash = options.get('createSquashCtrl')

        # Create oriented locs
        fk_loc = utils.snap_locator(jnts[0])
        look_loc = utils.snap_locator(prefix+'_lookAt_CTL_REF')
        mc.delete(mc.aimConstraint(jnts[1], fk_loc, aim=[0,0,1], u=[0,1,0], wut='scene'))

        # Create ctrls
        look_at_zero, look_at_ctrl, look_at_offsets, look_at_last = self.anim_ctrl(prefix+'_lookAt_CTL', match_position=look_loc)
        mc.parent(look_at_zero, ctrl_grps[1])

        eye_fk_zero, eye_fk_ctrl, eye_fk_offsets, eye_fk_last = self.anim_ctrl(prefix+'_eye_FK_CTL', match_position=fk_loc)
        mc.parent(eye_fk_zero, ctrl_grps[0])

        # constrain stuff
        mc.parentConstraint(eye_fk_last, jnts[0], mo=1)
        mc.aimConstraint(look_at_last, eye_fk_ctrl+'_CONST', aim=[0,0,1], u=[0,1,0], wu=[0,1,0], wut='objectRotation', wuo=ctrl_grps[0], mo=1)

        if create_squash:
            sq_zero, sq_ctrl, sq_offsets, sq_last = self.anim_ctrl(prefix+'_eye_squash_CTL', match_position=fk_loc)
            mc.parent(sq_zero, ctrl_grps[0])
            #mc.parent(eye_fk_zero, sq_last)
            #mc.scaleConstraint(sq_last, jnts[0], mo=1)

        #cleanup
        mc.parent(jnts[0], jnt_grps[0])
        mc.delete(fk_loc, look_loc)
        utils.set_attrs(eye_fk_ctrl, 't s', l=1, k=0)
        utils.set_attrs(look_at_ctrl, 'r s', l=1, k=0)

        arg = 'cLookAt:%s ' % look_at_zero
        arg += 'parent:%s ' % options.get('parent')

        #Setup spaces and pickwalking
        spaces.tag(look_at_ctrl, arg=arg, add_parent_space=False)
        pickWalk.attribute_tag(eye_fk_ctrl, pickWalk_parent)
        # This finalizes the rig and creates rig sets
        self.finalize_part()
