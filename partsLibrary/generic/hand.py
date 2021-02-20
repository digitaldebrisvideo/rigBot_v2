# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

import os
from rigBot import control
from rigBot import utils
from rigBot import spaces
from rigBot import env
from rigBot import pickWalk
from rigBot import data
from rigBot.data import kAttributes
from rigBot import pickWalk
from rigBot.partsLibrary import standardPart

class Hand(standardPart.StandardPart):
    """Hand module for creating fingers and toes. Creates a contro with splay, fist, cup attributes.

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "L_wrist_end_JNT".
            :numberJoints: (int) Numder of joints per finger. Defaults to 4.
            :numberFingers: (int) Numder of fingers (Not counting the thumb). Defaults to 4.
            :createThumb: (bool) Create a thumb (This will have one less joint than the other fingers). Defaults to True.
            :createIkCtrls: (bool) Create IK ctrls for each finger. Defaults to True."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('parent', data_type='hook', default='L_wrist_end_JNT')
        self.add_option('numberJoints',
                        data_type='int',
                        rebuild_to_modify=True,
                        default = 4,
                        tool_tip='Numder of joints per finger.',
                        min=1)

        self.add_option('numberThumbJoints',
                        data_type='int',
                        rebuild_to_modify=True,
                        default = 3,
                        tool_tip='Numder of joints for the thumb.',
                        min=1)

        self.add_option('numberFingers',
                        data_type='int',
                        rebuild_to_modify=True,
                        default = 4,
                        tool_tip='Numder of fingers (Not counting the thumb).',
                        min=1)

        self.add_option('createThumb',
                        data_type='bool',
                        rebuild_to_modify=True,
                        default = True,
                        tool_tip='Create a thumb (This will have one less joint than the other fingers).')

        self.add_option('createIkCtrls',
                        data_type='bool',
                        rebuild_to_modify=True,
                        default = False,
                        tool_tip='Create IK ctrls for each finger.')

        self.add_option('pickWalkParent',
                        data_type='string',
                        selectable=True,
                        default = 'L_arm_IK_CTL',
                        tool_tip="Sets the pickWalk hierarcy that the animatos use.")


    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix       = self.prefix
        options      = self.options
        mirror_value = self.mirror_value

        number_fingers = options.get('numberFingers')
        number_joints = options.get('numberJoints')
        number_thumb_joints = options.get('numberThumbJoints')
        create_thumb = options.get('createThumb')
        create_ik = options.get('createIkCtrls')


        number_joints += 1
        number_thumb_joints += 1

        # first generate a list of colors and names per finger
        names = ['index', 'middle', 'ring', 'pinky']
        colors = ['light_blue','medium_blue']*number_fingers

        if number_fingers > 4:
            for i in range(4, number_fingers, 1):
                names.append('pinky'+utils.letters[i-3])

        finger_zeros = []

        # first create the thumb
        if create_thumb:
            result = self.__build_finger_guide(number_thumb_joints, 'thumb', colors[0], length=1)
            zeros = result[0]
            plcs = result[1]
            jnts = result[2]
            ctrl_zeros = result[3]
            ctrls = result[4]

            mc.xform(zeros[0], r=1, ro=[60, -30, 0])
            mc.xform(zeros[0], r=1, t=[0,0,0.25])
            finger_zeros.append(zeros[0])

            if create_ik:
                zero, ctrl = self.guide_ctrl(name='thumb_IK_', shape='diamond', scale=[0.3]*3,
                                             color='pink', driver=jnts[-1])

                pivot = utils.get_parent(ctrl)
                utils.set_attrs(pivot, 't s', l=1, k=0)

        # Create fingers
        for i in range(number_fingers):

            result = self.__build_finger_guide(number_joints, names[i], colors[i+1], length=1.5)
            zeros = result[0]
            plcs = result[1]
            jnts = result[2]
            ctrl_zeros = result[3]
            ctrls = result[4]

            mc.xform(zeros[0], r=1, t=[0,0,i*-0.25])
            finger_zeros.append(zeros[0])

            if create_ik:
                zero, ctrl = self.guide_ctrl(name=names[i]+'_IK', shape='diamond', scale=[0.3]*3,
                                             color='pink', driver=jnts[-1])

                pivot = utils.get_parent(ctrl)
                utils.set_attrs(pivot, 't s', l=1, k=0)

        tmp = mc.createNode('transform')
        mc.delete(mc.pointConstraint(finger_zeros, tmp))
        tmp_prcs = []
        for zero in finger_zeros:
            tmp_prcs.extend(mc.parentConstraint(tmp, zero, mo=1))

        mc.setAttr(tmp+'.tx', 0.25)
        mc.setAttr(tmp+'.tz', 0)
        mc.delete(tmp_prcs)
        mc.xform(tmp, r=1, t=[0,1,0])

        # Create main ctrl
        zero, ctrl = self.guide_ctrl('hand', shape='hand',
                                     create_pivot=0,
                                     allow_offset_ctrls=0,
                                     color='black',
                                     driver=tmp,
                                     scale=[.1]*3)

        pivot = utils.get_parent(ctrl)
        utils.set_attrs(pivot, 't s', l=1, k=0)
        mc.delete(tmp)

        # This finalizes your guide.

        self.finalize_guide()
        mc.setAttr(self.guide_master+'.jointAxisVis', 1)

    def __build_finger_guide(self, number_joints, name, color, length=1.0):

        zeros, plcs, jnts = self.guide_joint_chain(name, num_joints=number_joints, length=length)
        mc.parent(zeros[1:], plcs[0])
        utils.set_attrs(plcs[0], 's', l=0, k=1)

        ctrl_zeros, ctrls = [], []
        for i, jnt in enumerate(jnts[:-1]):
            letter = utils.letters[i]
            zero, ctrl = self.guide_ctrl(name=name+'_'+letter, shape='circle', scale=[0.3]*3,
                                         color=color, driver=jnt, axis='X', allow_offset_ctrls=0)
            ctrl_zeros.append(zero)
            ctrls.append(ctrl)

            # lock stuff
            pivot = utils.get_parent(ctrl)
            utils.set_attrs(pivot, 't s', l=1, k=0)

        mc.xform(zeros[1:-1],r=1, t=[0,self.mirror_value*.05, 0])
        mc.xform(zeros[2:-2],r=1, t=[0,self.mirror_value*.03, 0])

        return zeros, plcs, jnts, ctrl_zeros, ctrls

    def build_rig(self):
        """This builds your anim rig."""

        # create rig part top nodes
        self.create_part_master()

        # Get all the relevant part info
        prefix            = self.prefix
        options           = self.options
        anim_ctrls        = self.anim_ctrls
        bind_jnts       = self.bind_joints
        hooks             = self.hooks
        ctrl_grps         = self.ctrl_grps
        jnt_grps          = self.jnt_grps

        # get options
        number_fingers = options.get('numberFingers')
        number_joints = options.get('numberJoints')
        number_thumb_joints = options.get('numberThumbJoints')
        create_thumb = options.get('createThumb')
        create_ik = options.get('createIkCtrls')
        squash_stretch = options.get('squashStretch')
        pickWalk_parent = options.get('pickWalkParent')

        number_joints += 1
        number_thumb_joints += 1

        # first generate a list of colors and names per finger
        names = ['index', 'middle', 'ring', 'pinky']

        if number_fingers > 4:
            for i in range(4, number_fingers, 1):
                names.append('pinky'+utils.letters[i-3])

        if create_thumb:
            names.insert(0, 'thumb')

        # create master ctrls
        ct_name = prefix+'_hand_CTL'
        master_zero, master_ctrl, master_offsets, master_last_node = self.anim_ctrl(ct_name)

        mc.addAttr(master_ctrl, ln='spread', at='double', k=1)
        mc.addAttr(master_ctrl, ln='fist', at='double', k=1)
        mc.addAttr(master_ctrl, ln='cup', at='double', k=1)
        mc.addAttr(master_ctrl, ln='reverseCup', at='double', k=1)

        for name in names:
            mc.addAttr(master_ctrl, ln=name+'Curl', at='double', k=1)

        mc.parent(master_zero, ctrl_grps[0])

        # create FK ctrls
        all_joints = []
        all_ctrls = []
        all_ik_ctrls = []

        for name in names:
            ctrls = []
            jnts = []
            for i in range(number_joints):

                letter = utils.letters[i]
                jnt = prefix+'_'+name+'_'+letter+'_JNT'
                ct_name = prefix+'_'+name+'_'+letter+'_CTL'

                # first create all ctrls
                if mc.objExists(ct_name+'_REF'):
                    zero, ctrl, offsets, last_node = self.anim_ctrl(ct_name)

                    if ctrls:
                        mc.parent(zero, ctrls[-1])
                    else:
                        mc.parent(zero, ctrl_grps[0])

                    ctrls.append(ctrl)
                if mc.objExists(jnt):
                    jnts.append(jnt)

            jnts = mc.ls(jnts)
            if not jnts:
                continue

            if create_ik:
                ct_name = prefix+'_'+name+'_IK_CTL'
                ik_zero, ik_ctrl, ik_offsets, ik_last_node = self.anim_ctrl(ct_name)
                mc.parent(ik_zero, ctrl_grps[0])

                spaces.tag(ik_ctrl)
                all_ik_ctrls.append(ik_ctrl)

            all_ctrls.append(ctrls)
            all_joints.append(jnts)

        for jnts in all_joints:
            mc.parent(jnts[0], jnt_grps[0])

        # now for each finger constraints and connections
        fk_sets = []
        all_fk_set = self.create_ctrl_set('FK')

        for finger_index in range(len(all_ctrls)):
            ctrls = all_ctrls[finger_index]



            jnts = all_joints[finger_index]

            #utils.create_cfx_curves(jnts, self.prefix+'_'+names[finger_index])

            set_name = names[finger_index]+'_FK'
            self.create_ctrl_set(set_name, ctrls, parent_set=all_fk_set)

            #Setup pickwaliking attributes for the fingers

            i = 0
            ctrls.reverse()
            for ctrl in ctrls:

                if i+1 < len(ctrls):

                    pickWalk.attribute_tag(ctrls[i],ctrls[i+1])
                else:
                    pickWalk.attribute_tag(ctrls[i],master_ctrl)
                    break

                i+=1
            ctrls.reverse()



            # aim and scale constraint for each joint
            for i in range(len(ctrls)):
                ctrl_grp = ctrls[i]+'_CONST'
                ctrl_grp = mc.rename(ctrl_grp, ctrls[i]+'_AUTO')
                mc.addAttr(ctrl_grp, ln='handPoseNode', at='message')

                if create_ik:
                    mc.orientConstraint(ctrls[i], jnts[i], n=jnts[i]+'_oc', mo=1)

                else:

                    #This doesnt work with ik
                    mc.pointConstraint(ctrls[i], jnts[i], mo=1, n=jnts[i]+'_pc')
                    if not squash_stretch:
                        mc.scaleConstraint(ctrls[i], jnts[i], mo=1, n=jnts[i]+'_sc')

                    if i < len(ctrls)-1:
                        mc.aimConstraint(ctrls[i+1],
                                         jnts[i],
                                         aim=[self.mirror_value,0,0],
                                         u=[0,1,0],
                                         wu=[0,1,0],
                                         wut='objectRotation',
                                         wuo=ctrls[i],
                                         mo=1, n=jnts[i]+'_ac')
                    else:
                        mc.orientConstraint(ctrls[i], jnts[i], n=jnts[i]+'_oc', mo=1)

            #if not squash_stretch:
            #    mc.scaleConstraint(jnts[-2], jnts[-1], mo=1, n=jnts[-1]+'_sc')

            # create ik ctrl
            if create_ik:
                ik_ctrl = all_ik_ctrls[finger_index]
                self.create_ctrl_set('IK', ik_ctrl)

                ik_a_name = prefix+'_'+names[finger_index]+'_IK'
                ik_b_name = prefix+'_'+names[finger_index]+'_tip_IK'

                if names[finger_index]=='thumb':
                    ik_handle_A = mc.ikHandle(sj=jnts[0], ee=jnts[-2], s='sticky', sol='ikSCsolver', n=ik_a_name)
                else:
                    try:
                        ik_handle_A = mc.ikHandle(sj=jnts[1], ee=jnts[-2], s='sticky', sol='ikSCsolver', n=ik_a_name)
                    except:
                        ik_handle_A = mc.ikHandle(sj=jnts[0], ee=jnts[-2], s='sticky', sol='ikSCsolver', n=ik_a_name)

                ik_handle_B = mc.ikHandle(sj=jnts[-2], ee=jnts[-1], s='sticky', sol='ikSCsolver', n=ik_b_name, )
                mc.parent(ik_handle_A[0], ik_handle_B[0], ik_ctrl)

                mc.addAttr(ik_ctrl, ln='IK', at='double', min=0, max=1, k=1)
                mc.connectAttr(ik_ctrl+'.IK', ik_handle_A[0]+'.ikBlend')
                mc.connectAttr(ik_ctrl+'.IK', ik_handle_B[0]+'.ikBlend')

                mc.hide(ik_handle_A, ik_handle_B)

        # create pose ctrl connections
        attrs = ['spread','fist','cup','reverseCup']+[a+'Curl' for a in names]

        for attr in attrs:
            for jnt in bind_jnts:
                ctrl = jnt.replace('JNT', 'CTL')
                ctrl_grp = ctrl+'_AUTO'

                if not mc.objExists(ctrl_grp):
                    continue

                # add attrs
                mc.addAttr(ctrl_grp, ln=attr+'X', at='double', k=0, dv=0)
                mc.addAttr(ctrl_grp, ln=attr+'Y', at='double', k=0, dv=0)
                mc.addAttr(ctrl_grp, ln=attr+'Z', at='double', k=0, dv=0)

                # create md
                md = mc.createNode('multiplyDivide', n=jnt+'_'+attr+'_md')
                mc.connectAttr(ctrl_grp+'.'+attr+'X', md+'.input1X')
                mc.connectAttr(ctrl_grp+'.'+attr+'Y', md+'.input1Y')
                mc.connectAttr(ctrl_grp+'.'+attr+'Z', md+'.input1Z')

                mc.connectAttr(master_ctrl+'.'+attr, md+'.input2X')
                mc.connectAttr(master_ctrl+'.'+attr, md+'.input2Y')
                mc.connectAttr(master_ctrl+'.'+attr, md+'.input2Z')

                mc.setAttr(md+'.ihi', 0)

                for a in ['x','y','z']:
                    mc.setDrivenKeyframe(ctrl_grp+'.r'+a, cd=md+'.output'+a.upper(),itt='spline', ott='spline', dv=0, v=0)
                    mc.setDrivenKeyframe(ctrl_grp+'.r'+a, cd=md+'.output'+a.upper(),itt='spline', ott='spline', dv=10, v=1)

                crv = mc.listConnections(md, type='animCurve', scn=1)
                mc.selectKey(crv, k=1)
                mc.setInfinity( pri='linear', poi='linear' )

        # Set defaults
        if 'thumb' in names:
            names.remove('thumb')

        if number_fingers == 1:
            spread_values = [0]
            cup_values = [-60]
            reverse_cup_values = list(cup_values)
            reverse_cup_values.reverse()

        elif number_fingers == 2:
            spread_values = [30, -30]
            cup_values = [0, -60]
            reverse_cup_values = list(cup_values)
            reverse_cup_values.reverse()

        elif number_fingers == 3:
            spread_values = [30, 0, -30]
            cup_values = [0, -30, -60]
            reverse_cup_values = list(cup_values)
            reverse_cup_values.reverse()

        elif number_fingers >= 4:
            spread_values = [30, 10, -10, -30]
            cup_values = [0, -20, -40, -60]
            reverse_cup_values = list(cup_values)
            reverse_cup_values.reverse()

        for i in range(len(names)):
            if i > 3:
                spread_values.append(-30)
                cup_values.append(-60)
                reverse_cup_values = list(cup_values)
                reverse_cup_values.reverse()

            ctrl = prefix+'_'+names[i]+'_B_CTL_AUTO'
            if mc.objExists(ctrl):
                mc.setAttr(ctrl+'.spreadY', -spread_values[i])
                mc.setAttr(ctrl+'.fistZ', -60)

            for ii in range(1, number_joints):
                ltr = utils.letters[ii]
                ctrl = prefix+'_'+names[i]+'_'+ltr+'_CTL_AUTO'
                if mc.objExists(ctrl):
                    mc.setAttr(ctrl+'.cupZ', cup_values[i])
                    mc.setAttr(ctrl+'.reverseCupZ', reverse_cup_values[i])
                    mc.setAttr(ctrl+'.fistZ', -89)
                    at = names[i].replace(prefix, '').replace('_','')
                    if mc.objExists('{0}.{1}CurlZ'.format(ctrl, at)):
                        mc.setAttr('{0}.{1}CurlZ'.format(ctrl, at), -90)

        # set thumb
        if create_thumb:
            ctrl = prefix+'_thumb_A_CTL_AUTO'
            if mc.objExists(ctrl):
                mc.setAttr(ctrl+'.fistZ', -10)
                mc.setAttr(ctrl+'.fistY', -5)

            for ii in range (0, number_thumb_joints):
                ltr = utils.letters[ii]
                ctrl = prefix+'_thumb_'+ltr+'_CTL_AUTO'

                if mc.objExists(ctrl):
                    mc.setAttr(ctrl+'.fistZ', -45)
                    mc.setAttr('{0}.thumbCurlZ'.format(ctrl), -90)

        # This finalizes guide and creates rig sets
        utils.set_attrs(master_ctrl, 't r s rotateOrder', l=1, k=0)

        # Load attributes IF the fgile exits

        ext = kAttributes.file_extention
        file_filter = data.get_file_filter('kAttributes')[0]
        base_path = os.path.join(env.get_rigbuild_path(), 'data', env.get_variant())
        data_path = os.path.join(base_path, 'handPose'+ext)

        if os.path.isfile(data_path):
            kAttributes.load(data_path)
        pickWalk.attribute_tag(master_ctrl,pickWalk_parent)
        self.finalize_part()
