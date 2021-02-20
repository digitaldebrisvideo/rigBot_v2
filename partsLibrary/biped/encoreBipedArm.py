# -*- rigBot: part -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import control
from rigBot import ikChain
from rigBot import pickWalk
from rigBot import spaces
from rigBot.partsLibrary import standardPart
from rigBot import encoreCommon

class EncoreBipedArm(standardPart.StandardPart):
    """Biped arm module. Includes FK/ IK, twist, stretch and soft IK. There is also bendy, and auto clavicle functionality

        Build Options:
            :side: (str) Side token for this rig part. Defaults to "L".
            :name: (str) Optional name. Used as a naming prefix for all nodes in this part. Defaults to "".
            :parent: (str) Parent. Defaults to "C_chest_JNT".
            :ikHandleParent: (str) Optional IK handle parent for connecting to a foot part. Will default to it's own IK control if the node doesnt exist. Defaults to "".
            :numberTwistJoints: (int) Number of twist joints for the upper and lower arms Defaults to 4.
            :makeBendy: (bool) Add bendy controls. Defaults to False.

        Note:
            If using the bendy feature you will need enough twist joints to allow for proper spline deformation."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

        self.add_option('parent', data_type='hook', default='C_chest_JNT')
        self.add_option('ikHandleParent',
                        data_type='hook',
                        default = '',
                        tool_tip="Optional IK handle parent for connecting to a "+\
                                    "foot part. Will default to it's own IK control "+\
                                    "if the node doesnt exist.")

        self.add_option('numberTwistJoints',
                        data_type='int',
                        min=0,
                        default = 4,
                        tool_tip = 'Number of twist joints for the upper and lower arms',
                        rebuild_to_modify=True)

        self.add_option('makeBendy',
                 data_type='bool',
                 default=True,
                 rebuild_to_modify=True,
                 tool_tip='Add bendy controls.')

        self.add_option('transOrientiation',
                 data_type='enum',
                 default='world',
                 enum='world:downBone',
                 tool_tip='Orient the translates on IK control to the world OR down the bone.')


        self.add_option('doubleClavicle',
                 data_type='bool',
                 default=False,
                 rebuild_to_modify=True,
                 tool_tip='Creates a second clavicle joint.')


        self.add_option('pickWalkParent',
                        data_type='string',
                        default = 'C_chest_CTL',
                        selectable=True,
                        tool_tip="Sets the pickWalk hierarcy that the animators use.")




    def build_guide(self, **kwargs):
        """This builds your guide."""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix       = self.prefix
        options      = self.options
        mirror_value = self.mirror_value

        number_twist_jnts = options.get('numberTwistJoints')
        make_bendy = options.get('makeBendy')
        double_clav = options.get('doubleClavicle')

        # draw joints

        if double_clav:
            clavicleBase_zero, clavicleBase_plc, clavicleBase_jnt = self.guide_joint('clavicleBase', constraint_type='point')
        clavicle_zero, clavicle_plc, clavicle_jnt = self.guide_joint('clavicle', constraint_type='point')
        up_arm_zero, up_arm_plc, up_arm_jnt = self.guide_joint('upArm', constraint_type='point')
        lo_arm_zero, lo_arm_plc, lo_arm_jnt = self.guide_joint('loArm', constraint_type='point')
        wrist_zero, wrist_plc, wrist_jnt = self.guide_joint('wrist', constraint_type='point')
        wrist_end_zero, wrist_end_plc, wrist_end_jnt = self.guide_joint('wrist_end', constraint_type='point')
        
        scapula1_zero, scapula1_plc, scapula1_jnt = self.guide_joint('scapulaCtrl', constraint_type='point')
        scapula2_zero, scapula2_plc, scapula2_jnt = self.guide_joint('scapulaEnd', constraint_type='point')
        scapula_target_plc_zero, scapula_target_plc, scapula_target_jnt = self.guide_joint('scapulaTarget', constraint_type='point')
        scapula_chest_plc_zero, scapula_chest_plc, scapula_chest_jnt = self.guide_joint('scapulaChest', constraint_type='point')

        clavicle2_zero, clavicle2_plc, clavicle2_jnt = self.guide_joint('clavicleEnd', constraint_type='point')

        # elbow_vj_zero, elbow_vj_plc, elbow_vj_jnt = self.guide_joint('elbowVJ', constraint_type='point')
        elbow_fnt_zero, elbow_fnt_plc, elbow_fnt_jnt = self.guide_joint('elbowFrontFix', constraint_type='point')
        elbow_bck_zero, elbow_bck_plc, elbow_bck_jnt = self.guide_joint('elbowBckFix', constraint_type='point')

        # wrist_top_zero, wrist_top_plc, wrist_top_jnt = self.guide_joint('wristTopFix', constraint_type='point')
        # wrist_btm_zero, wrist_btm_plc, wrist_btm_jnt = self.guide_joint('wristBtmFix', constraint_type='point')
        # wrist_bck_zero, wrist_bck_plc, wrist_bck_jnt = self.guide_joint('wristFntFix', constraint_type='point')
        # wrist_fnt_zero, wrist_fnt_plc, wrist_fnt_jnt = self.guide_joint('wristBckFix', constraint_type='point')

        ik_driver_plc_zero, ik_driver_plc = self.guide_joint('arm_IK_handle_driver', placer_only=1)
        # mc.setAttr (ik_driver_plc_zero+'.visiblity', 0)

        mc.setAttr(ik_driver_plc+'.radius', 1)
        mc.setAttr(ik_driver_plc+'.color', 0.96, 0.71, .01)
        mc.setAttr(ik_driver_plc+'.otherType',  'Leg IK Driver', type='string');
        mc.setAttr(ik_driver_plc+'.type', 18)

        mc.parentConstraint(wrist_jnt, ik_driver_plc_zero)
        mc.setAttr(ik_driver_plc+'.offsetTranslateX', self.mirror_value*0.25)

        utils.set_attrs(ik_driver_plc, l=1, k=0)

        # position
        if double_clav:
            mc.setAttr(clavicleBase_zero+'.tx', 0.5)
        mc.setAttr(clavicle_zero+'.tx',.5)
        mc.setAttr(up_arm_zero+'.tx', 2)
        mc.setAttr(lo_arm_zero+'.tx', 4)
        mc.setAttr(lo_arm_zero+'.tz', -0.5)
        mc.setAttr(wrist_zero+'.tx', 6)
        mc.setAttr(wrist_end_zero+'.tx', 6.5)

        mc.setAttr(scapula1_zero+'.tx', 2.0)
        mc.setAttr(scapula1_zero+'.tz', -1.5)

        mc.setAttr(scapula2_zero+'.tx', .5)
        mc.setAttr(scapula2_zero+'.tz', -1.5)

        mc.setAttr(scapula_target_plc_zero+'.tz',-2)

        mc.setAttr(clavicle2_zero+'.tx',2)
        mc.setAttr(clavicle2_zero+'.tz',-.5)



        # Constraint clavicle
        # Constraint clavicle
        if double_clav:
            mc.aimConstraint(clavicle_plc,
                             clavicleBase_jnt,
                             n=clavicleBase_jnt+'_ac',
                             aim=[mirror_value,0,0],
                             u=[0,1,0],
                             wu=[0,1,0],
                             wut='objectRotation',
                             wuo=clavicleBase_plc)


        # Constraint shoulder
        mc.aimConstraint(clavicle2_plc,
                         clavicle_jnt,
                         n=clavicle_jnt+'_ac',
                         aim=[mirror_value,0,0],
                         u=[0,1,0],
                         wu=[0,1,0],
                         wut='objectRotation',
                         wuo=clavicle_plc)

        # Constraint upArm
        mc.aimConstraint(lo_arm_plc,
                         up_arm_jnt,
                         n=up_arm_jnt+'_ac',
                         aim=[mirror_value,0,0],
                         u=[0,0,mirror_value],
                         wut='object',
                         wuo=wrist_plc)

        # Constraint loArm
        mc.aimConstraint(wrist_plc,
                         lo_arm_jnt,
                         n=lo_arm_jnt+'_ac',
                         aim=[mirror_value,0,0],
                         u=[0,0,mirror_value],
                         wut='object',
                         wuo=up_arm_plc)

        mc.aimConstraint(wrist_end_plc,
                         wrist_jnt,
                         n=wrist_jnt+'_ac',
                         aim=[mirror_value,0,0],
                         u=[0,1,0],
                         wu=[0,1,0],
                         wut='objectRotation',
                         wuo=wrist_plc)

        # parent jnts
        if double_clav:
            mc.parent(clavicle_jnt, clavicleBase_jnt)


        mc.parent(scapula2_jnt, scapula1_jnt)
        # mc.parent (scapula1_jnt, clavicle_jnt)
        mc.parent (scapula_target_jnt, scapula_chest_jnt)
        # mc.parent(up_arm_jnt, clavicle2)
        # mc.parent (clavicle2_jnt, clavicle_jnt)

        mc.parent(clavicle2_jnt, clavicle_jnt)
        mc.parent(lo_arm_jnt, up_arm_jnt)
        mc.parent(wrist_jnt, lo_arm_jnt)
        mc.parent(wrist_end_jnt, wrist_jnt)



        mc.xform(wrist_end_jnt, a=1, ro=[0,0,0])
        mc.setAttr(wrist_end_jnt+'.jo', 0,0,0)

      #elblow
        # mc.delete (mc.pointConstraint (lo_arm_jnt, elbow_vj_zero, mo=0))
        # mc.delete (mc.pointConstraint (lo_arm_jnt, elbow_fnt_zero, mo=0))
        # mc.delete (mc.pointConstraint (lo_arm_jnt, elbow_bck_zero, mo=0))
        # mc.delete (mc.pointConstraint (wrist_jnt,  wrist_top_zero , mo=0))
        # mc.delete (mc.pointConstraint (wrist_jnt,  wrist_btm_zero , mo=0))
        # mc.delete (mc.pointConstraint (wrist_jnt,  wrist_bck_zero , mo=0))
        # mc.delete (mc.pointConstraint (wrist_jnt,  wrist_fnt_zero , mo=0))
        #
        # mc.setAttr(elbow_fnt_zero + '.tz', 0)
        # mc.setAttr(elbow_bck_zero + '.tz', -1)
        # mc.setAttr(wrist_top_zero + '.ty', .5)
        # mc.setAttr(wrist_btm_zero + '.ty', -.5)
        # mc.setAttr(wrist_bck_zero + '.tz', -.5)
        # mc.setAttr(wrist_fnt_zero + '.tz', .5)

        for elbow in [elbow_fnt_zero, elbow_bck_zero]:
            mc.parentConstraint (lo_arm_jnt, elbow , mo=1)

        mc.parent (elbow_fnt_jnt, lo_arm_jnt)
        mc.parent (elbow_bck_jnt, lo_arm_jnt)
        # for wrist in [wrist_top_zero, wrist_btm_zero, wrist_fnt_zero, wrist_bck_zero] :
        #     mc.parentConstraint (wrist_jnt, wrist , mo=1)





        # Create twist jnts
        div = 1.0 / (number_twist_jnts+1)

        up_twist_zeros, up_twist_plcs, up_twist_jnts = [], [], []
        lo_twist_zeros, lo_twist_plcs, lo_twist_jnts = [], [], []

        up_shpr_zeros, up_shpr_plcs, up_shpr_jnts = [], [], []
        lo_shpr_zeros, lo_shpr_plcs, lo_shpr_jnts = [], [], []

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
            mc.pointConstraint(lo_arm_plc, plc, weight=(div*(i+1)))
            mc.orientConstraint(up_arm_jnt, plc)

            mc.xform(jnt, a=1, ro=[0,0,0])
            mc.setAttr(jnt+'.jo', 0,0,0)

            utils.set_attrs(plc, 't r s', l=1, k=0)

            up_shpr_name = prefix + '_upArm_shaper_' + letter
            up_shpr_zero, up_shpr_plc, up_shpr_jnt = self.guide_joint('upArm_shaper_'+letter, constraint_type='point')
            # mc.parent(up_shpr_jnt, up_arm_jnt)
            up_shpr_jnts.append(up_shpr_jnt)
            up_shpr_plcs.append(up_shpr_plc)
            up_shpr_zeros.append(up_shpr_zero)
            mc.delete(mc.parentConstraint(jnt, up_shpr_jnt, mo=0))
            mc.parentConstraint(jnt, up_shpr_zero)
            up_shpr_ctl_zero, up_shpr_ctrl = self.guide_ctrl('upArm_shaper_'+letter, shape='pin_circle', color='dark_magenta',
                                                           driver=up_shpr_jnt, scale=[mirror_value + 3, 3, 3],
                                                           allow_offset_ctrls=False)
            # mc.setAttr (up_shpr_ctrl.replace ('CTL', 'PIV_CTL')+'.rx', 180)

            # setup uplowerper arm jnts
            letter = utils.letters[i]
            zero, plc, jnt = self.guide_joint('loArm_twist_'+letter, constraint_type='point')
            lo_shpr_zero, lo_shpr_plc, lo_shpr_jnt = self.guide_joint('loArm_shaper_'+letter, constraint_type='point')

            if lo_twist_jnts:
                mc.parent(jnt, lo_twist_jnts[-1])
            else:
                mc.parent(jnt, lo_arm_jnt)

            lo_twist_jnts.append(jnt)
            lo_twist_plcs.append(plc)
            lo_twist_zeros.append(zero)

            mc.pointConstraint(lo_arm_plc, plc, weight=1.0-(div*(i+1)))
            mc.pointConstraint(wrist_plc, plc, weight=(div*(i+1)))
            mc.orientConstraint(lo_arm_jnt, plc)

            mc.xform(jnt, a=1, ro=[0,0,0])
            mc.setAttr(jnt+'.jo', 0,0,0)

            utils.set_attrs(plc, 't r s', l=1, k=0)
            # mc.parent (lo_shpr_jnt, lo_arm_jnt)
            lo_shpr_jnts.append(lo_shpr_jnt)
            lo_shpr_plcs.append(lo_shpr_plc)
            lo_shpr_zeros.append(lo_shpr_zero)
            mc.delete (mc.parentConstraint(jnt, lo_shpr_jnt, mo=0))
            mc.parentConstraint (jnt, lo_shpr_zero)
            lo_shp_ctl_zero, lo_shp_ctrl = self.guide_ctrl ('loArm_shaper_'+letter, shape='pin_circle', color='dark_magenta', driver=lo_shpr_jnt, scale=[mirror_value+3, 3, 3], allow_offset_ctrls=False)
            # mc.setAttr (lo_shp_ctrl.replace ('CTL', 'PIV_CTL')+'.rx', 180)



        if up_twist_jnts:
            mc.parent(lo_arm_jnt, up_twist_jnts[-1])
            for plc in up_twist_plcs:
                mc.setAttr(plc+'.radius', 0.7)

        if lo_twist_jnts:
            mc.parent(wrist_jnt, lo_twist_jnts[-1])
            for plc in lo_twist_plcs:
                mc.setAttr(plc+'.radius', 0.7)

        #lock plcs
        utils.set_attrs([up_arm_plc, lo_arm_plc], 'r s', l=1, k=0)

        # Create ctrls

        scapula1_zero, scapula1_ctrl = self.guide_ctrl(name='scapulaCtrl',
            shape='flat_diamond',
            color='light_blue',
            driver=scapula1_jnt,
            allow_offset_ctrls=False)


        mc.xform(scapula1_ctrl+'.cv[*]', r=1, ro=[90,0,0])


        scapula_target_zero, scapulatarget_ctrl = self.guide_ctrl(name='scapulaTarget',
            shape='diamond',
            color='yellow',
            driver=scapula_target_jnt,
            allow_offset_ctrls=False,
            axis='X')


        scapula_chest_zero, scapulachest_ctrl = self.guide_ctrl(name='scapulaChest',
            shape='sphere',
            color='yellow',
            driver=scapula_chest_jnt,
            allow_offset_ctrls=False,
            axis='X')

        up_arm_fk_zero, up_arm_fk_ctrl = self.guide_ctrl(name='upArm_FK',
            shape='cube',
            color='light_blue',
            driver=up_arm_jnt,
            allow_offset_ctrls=False,
            axis='X', scale=[1.5, .5, .5])
        # mc.delete(mc.pointConstraint (up_arm_jnt, lo_arm_jnt, up_arm_fk_ctrl+'_CONST',  mo=0))

        lo_arm_fk_zero, lo_arm_fk_ctrl = self.guide_ctrl(name='loArm_FK',
            shape='cube',
            color='light_blue',
            driver=lo_arm_jnt,
            allow_offset_ctrls=False,
            axis='X', scale=[1.5, .5, .5])
        # mc.delete(mc.pointConstraint (lo_arm_jnt,  wrist_jnt, lo_arm_fk_ctrl+'_CONST' , mo=0))

        wrist_fk_zero, wrist_fk_ctrl = self.guide_ctrl(name='wrist_FK',
            shape='cube',
            color='light_blue',
            driver=wrist_jnt,
            allow_offset_ctrls=False,
            axis='X', scale=[.1, 1, 1])

        # mc.xform(wrist_fk_ctrl+'.cv[*]', r=1, t=[mirror_value*0,0,0])

        color = 'blue'
        if mirror_value < 0:
            color = 'red'

        arm_ik_zero, arm_ik_ctrl = self.guide_ctrl('arm_IK',
            shape='circle',
            color=color,
            scale=[0.8]*3,
            driver=wrist_jnt, axis='X')

        wrist_ik_zero, wrist_ik_ctrl = self.guide_ctrl(name='wrist_IK',
            shape='square',
            color=color,
            driver=wrist_jnt,
            axis='X')

        mc.xform(wrist_ik_ctrl+'.cv[*]', r=1, t=[mirror_value*0.5,0,0])
        # mc.xform(arm_ik_ctrl+'.cv[*]', r=1, ro=[0, 90, 0])
        # mc.xform(arm_ik_ctrl.replace ('CTL', 'OFF_CTL')+'.cv[*]', r=1, ro=[0, 90, 0])


        pv_zero, pv_ctrl = self.guide_ctrl('arm_PV', shape='cube', color=color, scale=[0.2]*3, allow_offset_ctrls=0, create_pivot=0)
        pv_pivot = utils.get_parent(pv_ctrl)
        utils.set_attrs(pv_pivot, 't', l=0)

        grp = utils.get_parent(pv_pivot)
        noxform = utils.get_parent(pv_zero).replace('CTLS', 'NOX')

        # Constraint pv
        mc.pointConstraint(up_arm_jnt, pv_zero, n=pv_zero+'_pc')
        mc.aimConstraint(wrist_jnt,
                         pv_zero,
                         n=pv_zero+'_ac',
                         aim=[mirror_value,0,0],
                         u=[0,0,-mirror_value],
                         wut='object',
                         wuo=lo_arm_jnt)

        mc.pointConstraint(lo_arm_jnt, grp, n=grp+'_pc')
        mc.setAttr(pv_pivot+'.tz', -10)
        mc.orientConstraint(noxform, pv_ctrl, n=pv_ctrl+'_pc')

        utils.set_attrs([pv_ctrl, pv_zero, grp, pv_pivot], 'r t s v', l=1, k=0)
        utils.set_attrs(pv_ctrl, 'tx tz s ', l=0, k=1)

        clavicle_fk_zero, clavicle_fk_ctrl = self.guide_ctrl(name='clavicle',
            shape='semi_circle',
            color=color,
            scale=[1.5,1.5,3],
            driver=clavicle_jnt,
            axis='Y')

        mc.xform(clavicle_fk_ctrl+'.cv[*]', r=1, ro=[0,0,90])
        mc.xform(clavicle_fk_ctrl+'.cv[*]', r=1, ro=[90,0,0])
        # mc.delete (mc.pointConstraint (clavicle_jnt, clavicle2_jnt, clavicle_fk_ctrl+'_CONST'))

        if double_clav:
            clavA_zero, clavA_ctrl = self.guide_ctrl(name='clavicleA',
                shape='cube',
                color=color,
                scale=[0.5,0.5,2],
                driver=clavicleBase_jnt,
                axis='Y')

            mc.xform(clavA_ctrl+'.cv[*]', r=1, ro=[0,-90,0])

            clavB_zero, clavB_ctrl = self.guide_ctrl(name='clavicleB',
                shape='cube',
                color=color,
                scale=[0.5,0.5,2],
                driver=clavicle_jnt,
                axis='Y')

        if make_bendy:
            baCtrl = self.guide_ctrl(name='bendyArm_A', shape='arrow_quad', color='yellow', axis='X')
            bbCtrl = self.guide_ctrl(name='bendyArm_B', shape='arrow_quad', color='yellow', axis='X')
            bcCtrl = self.guide_ctrl(name='bendyArm_C', shape='arrow_quad', color='yellow', axis='X')

            mc.parentConstraint(up_arm_jnt, baCtrl[0], n=baCtrl[0]+'_prc')
            mc.parentConstraint(lo_arm_jnt, bbCtrl[0], n=bbCtrl[0]+'_prc')
            mc.parentConstraint(lo_arm_jnt, bcCtrl[0], n=bcCtrl[0]+'_prc')

            mc.pointConstraint(up_arm_jnt, lo_arm_jnt, baCtrl[1]+'_CONST', n=baCtrl[1]+'_CONST_pc')
            mc.pointConstraint(wrist_jnt, lo_arm_jnt, bcCtrl[1]+'_CONST', n=bcCtrl[1]+'_CONST_pc')
            oc = mc.orientConstraint(up_arm_jnt, lo_arm_jnt, bbCtrl[1]+'_CONST', n=bbCtrl[1]+'_CONST_oc')
            mc.setAttr(oc[0]+'.interpType', 2)

            utils.set_attrs(baCtrl+bbCtrl+bcCtrl)
            utils.set_attrs([baCtrl[-1], bbCtrl[-1], bcCtrl[-1]], 't r s', k=1, l=0)

        # ik fk switch ctrl
        switch_zero, switch_ctrl = self.guide_ctrl(name='arm_IK_switch', shape='pin_switch', color='black', driver=wrist_jnt)
        mc.setAttr (switch_ctrl+'_CONST.rz', 90)
        mc.setAttr(arm_ik_ctrl+'.numOffsetCtrls', 1)


        # mc.xform

        line = mc.createNode('transform', n=pv_ctrl+'_line_REF', p=utils.get_parent(pv_zero))
        control.create_driven_shape(line, [pv_ctrl, lo_arm_jnt])
        utils.set_draw_override(line, 1)

        # This finalizes your guide.
        self.finalize_guide()

    def build_rig(self):
        """This builds your anim rig."""

        # create rig part top nodes
        self.create_part_master()

        # Get all the relevant part info
        prefix            = self.prefix
        options           = self.options
        anim_ctrls        = self.anim_ctrls
        bind_joints       = self.bind_joints
        world_scale_attr  = self.hooks[0]+'.worldScale'
        hooks             = self.hooks
        ctrl_grps         = self.ctrl_grps
        jnt_grps          = self.jnt_grps

        number_twist_jnts = options.get('numberTwistJoints')
        parent = options.get('parent')
        make_bendy = options.get('makeBendy')
        pickWalk_parent = options.get('pickWalkParent')
        double_clav = options.get('doubleClavicle')

        world_orient_trans=options.get('transOrientiation')

        pre=prefix+'_'


        scap_aim_jnt = pre+'scapulaAim_JNT'
        scapula1_jnt = pre+'scapulaCtrl_JNT'
        scapula2_jnt=pre+'scapulaEnd_JNT'
        scapula_target_jnt = pre+'scapulaTarget_JNT'
        scapula_chest_jnt = pre+'scapulaChest_JNT'
        clavicleBase_jnt = prefix+'_clavicleBase_JNT'
        clavicle_jnt = prefix+'_clavicle_JNT'
        clavicle2_jnt = pre+'clavicleEnd_JNT'
        up_arm_jnt = prefix+'_upArm_JNT'
        lo_arm_jnt = prefix+'_loArm_JNT'
        wrist_jnt = prefix+'_wrist_JNT'
        wrist_end_jnt = prefix+'_wrist_end_JNT'

        up_arm_twist_jnts = mc.ls(prefix+'_upArm_twist_*JNT')
        lo_arm_twist_jnts = mc.ls(prefix+'_loArm_twist_*JNT')

        up_arm_shaper_jnts = mc.ls(prefix+'_upArm_shaper_*JNT')
        lo_arm_shaper_jnts = mc.ls(prefix+'_loArm_shaper_*JNT')


        # Create FK ctrls
        if double_clav:
            name = prefix+'_clavicleA_CTL'
            clavA_zero, clavA_ctrl, clavA_offsets, clavA_last_node = self.anim_ctrl(name)

            name = prefix+'_clavicleB_CTL'
            clavB_zero, clavB_ctrl, clavB_offsets, clavB_last_node = self.anim_ctrl(name)


        mirror=1
        color='blue'
        side=options.get('side')
        if side=='R':
            mirror=-1
            color='red'

        # # Create Scapula Rig

        scapula_dict = {side: {"bind": pre + "scapulaCtrl_JNT"}}

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # make the scapula up objects and add to hierarchy
        scap_aim_jnt= mc.createNode  ('joint', name=scap_aim_jnt, p=scapula1_jnt)
        mc.parent (scap_aim_jnt, clavicle_jnt)
        mc.parent (scapula1_jnt, scap_aim_jnt)
        loc_name = pre + "scapulaUpObj_loc"
        aim_name = scap_aim_jnt
        bnd_name = clavicle_jnt
        aim = pm.PyNode(aim_name)
        loc = pm.spaceLocator(name=loc_name)
        encoreCommon.match_xyz(loc, aim)
        pm.move(0, 10, 0, loc, relative=True, worldSpace=True)
        pm.parent(loc, bnd_name)
        scapula_dict[side]["aimJnt"] = aim
        scapula_dict[side]["upObj"] = loc

        loc_name = pre + "scapulaTarget_LOC"
        grp_name = pre + "scapulaTarget_GRP"
        loc = pm.spaceLocator(name=loc_name)
        grp = pm.group(name=grp_name)
        encoreCommon.match_xyz(grp, scapula_target_jnt)
        pm.parent(grp, scapula_chest_jnt)
        scapula_dict[side]["targetLoc"] = loc
        scapula_dict[side]["targetGrp"] = grp

        # constrain scapula targets
        tgt1 = clavicle2_jnt
        tgt2 = scapula_chest_jnt
        grp = scapula_dict[side]["targetGrp"]
        pm.pointConstraint(tgt1, grp, maintainOffset=True, skip=("x", "z"), weight=1.0)
        pm.pointConstraint(tgt2, grp, maintainOffset=True, skip=("x", "z"), weight=0.5)

        # setup scapula aim_constraints():
        tgt = scapula_dict[side]["targetLoc"]
        jnt = scapula_dict[side]["aimJnt"]
        amir = -1
        if side == 'Rt':
            amir = 1
        upv = (0, amir, 0)
        amv = (amir, 0, 0)
        upo = scapula_dict[side]["upObj"]
        aim = pm.aimConstraint(tgt, jnt, aimVector=amv, upVector=upv, worldUpType="object", worldUpObject=upo)
        pm.delete(aim)

        tgt = scapula_dict[side]["targetLoc"]
        jnt = scapula_dict[side]["aimJnt"]
        upv = (0, amir, 0)
        amv = (amir, 0, 0)
        upo = scapula_dict[side]["upObj"]
        aim = pm.aimConstraint(tgt, jnt, aimVector=amv, upVector=upv, worldUpType="object", worldUpObject=upo)
        pm.delete(aim)
        pm.makeIdentity(jnt, apply=True, translate=True, rotate=True, scale=True, normal=0, preserveNormals=True)
        pm.aimConstraint(tgt, jnt, aimVector=amv, upVector=upv, worldUpType="object", worldUpObject=upo)

        # create scapula anim ctrls
        name = pre + 'scapulaCtrl_CTL'
        scapula1_zero, scapula1_ctrl, scapula1_offsets, scapula1_last_node = self.anim_ctrl(name)

        cir_name = scapula1_ctrl
        grp_name = scapula1_zero
        jnt = scap_aim_jnt
        bnd = scapula1_jnt

        pm.parentConstraint(jnt, scapula1_zero)
        pm.parentConstraint(scapula1_ctrl, scapula1_jnt)
        pm.transformLimits(jnt, rotationY=(-360, 0), enableRotationY=(False, True))

        scap_zero = (pre + 'scapulaCtrl_CTL_ZERO')
        mc.parent(scap_zero, ctrl_grps[0])

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # Create FK ctrls
        if double_clav:
            name = prefix+'_clavicleA_CTL'
            clavA_zero, clavA_ctrl, clavA_offsets, clavA_last_node = self.anim_ctrl(name)

            name = prefix+'_clavicleB_CTL'
            clavB_zero, clavB_ctrl, clavB_offsets, clavB_last_node = self.anim_ctrl(name)

        name = prefix+'_clavicle_CTL'
        clavicle_zero, clavicle_ctrl, clavicle_offsets, clavicle_last_node = self.anim_ctrl(name)

        name = prefix+'_upArm_FK_CTL'
        up_arm_fk_zero, up_arm_fk_ctrl, up_arm_fk_offsets, up_arm_fk_last_node = self.anim_ctrl(name)

        name = prefix+'_loArm_FK_CTL'
        lo_arm_fk_zero, lo_arm_fk_ctrl, lo_arm_fk_offsets, lo_arm_fk_last_node = self.anim_ctrl(name)

        name = prefix+'_wrist_FK_CTL'
        wrist_fk_zero, wrist_fk_ctrl, wrist_fk_offsets, wrist_fk_last_node = self.anim_ctrl(name)

        # Create IK ctrls
        name = prefix+'_arm_IK_CTL'
        arm_ik_zero, arm_ik_ctrl, arm_ik_offsets, arm_ik_last_node = self.anim_ctrl(name, node_type='joint')

        arm_ik_last_node = mc.createNode('transform', p=arm_ik_last_node, n=prefix+'_arm_IK_handle_driver_JNT')

        name = prefix+'_wrist_IK_CTL'
        wrist_ik_zero, wrist_ik_ctrl, wrist_ik_offsets, wrist_ik_last_node = self.anim_ctrl(name)

        name = prefix+'_arm_PV_CTL'
        loc = utils.snap_locator(name+'_REF')
        mc.setAttr(loc+'.sx', self.mirror_value)
        pv_zero, pv_ctrl, pv_offsets, pv_last_node = self.anim_ctrl(name, match_position=loc)

        name = prefix+'_arm_IK_switch_CTL'
        switch_zero, switch_ctrl, switch_offsets, switch_last_node = self.anim_ctrl(name)

        mc.delete(loc)

        up_arm_grp = mc.createNode('transform', n=up_arm_jnt+'_GRP', p=clavicle_jnt)
        mc.delete(mc.parentConstraint(up_arm_jnt, up_arm_grp))
        mc.parent(up_arm_jnt, up_arm_grp)

        if make_bendy:
            bendyArmACtrl = self.anim_ctrl(prefix+'_bendyArm_A_CTL')
            bendyArmBCtrl = self.anim_ctrl(prefix+'_bendyArm_B_CTL')
            bendyArmCCtrl = self.anim_ctrl(prefix+'_bendyArm_C_CTL')
            mc.parent(bendyArmACtrl[0], bendyArmBCtrl[0], bendyArmCCtrl[0], ctrl_grps[0])

        #  here --------
        if double_clav:
            mc.parent(clavicle_zero, clavicleBase_jnt)
            mc.select(clavicle_zero, clavicle_ctrl+'_OFF', clavicle_ctrl+'_MOCAP', clavicle_ctrl+'_CONST', clavicle_ctrl, clavicle_offsets)
            utils.set_attrs(l=0, k=1)
            mc.makeIdentity(apply=1, t=1, r=1, s=1, n=0, pn=1)
            mc.xform(piv=[0,0,0])
            mc.parent(clavicle_zero ,w = True)


        # orient arm ik ctrl

        tmp_grp = mc.group(arm_ik_ctrl)
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

        # parent fk ctrls
        if double_clav:
            mc.parent(clavB_zero, clavA_ctrl)
            mc.parent(up_arm_fk_zero, clavB_ctrl)
            mc.parent(lo_arm_fk_zero, up_arm_fk_ctrl)
            mc.parent(wrist_fk_zero, lo_arm_fk_ctrl)
        else:
            mc.parent(up_arm_fk_zero, clavicle_ctrl)
            mc.parent(lo_arm_fk_zero, up_arm_fk_ctrl)
            mc.parent(wrist_fk_zero, lo_arm_fk_ctrl)

        # parent ik ctrls
        mc.parent(wrist_ik_zero, arm_ik_last_node)

        # NOW create ik fk chain setup
        up_arm_ik_jnt = mc.duplicate(up_arm_jnt, po=1, n=up_arm_jnt.replace('upArm', 'upArm_IK'))[0]
        lo_arm_ik_jnt = mc.duplicate(lo_arm_jnt, po=1, n=lo_arm_jnt.replace('loArm', 'loArm_IK'))[0]
        wrist_ik_jnt = mc.duplicate(wrist_jnt, po=1, n=wrist_jnt.replace('wrist', 'wrist_IK'))[0]

        mc.parent(lo_arm_ik_jnt, up_arm_ik_jnt)
        mc.parent(wrist_ik_jnt, lo_arm_ik_jnt)

        mc.orientConstraint(up_arm_fk_last_node, up_arm_ik_jnt, mo=1)
        mc.orientConstraint(wrist_fk_last_node, wrist_ik_jnt, mo=1)

        ori_par = mc.createNode('transform', p=lo_arm_ik_jnt, n=lo_arm_ik_jnt+'_orient_drv_GRP')
        ori = mc.createNode('transform', p=ori_par, n=lo_arm_ik_jnt+'_orient_DRV')
        mc.parent(ori_par, lo_arm_fk_zero)

        mc.orientConstraint(lo_arm_fk_ctrl, ori, mo=1)
        mc.connectAttr(ori+'.r', lo_arm_ik_jnt+'.r')

        ik_handle = mc.ikHandle(sj=up_arm_ik_jnt, ee=wrist_ik_jnt, s='sticky', n=prefix+'_arm_IK')[0]
        mc.poleVectorConstraint(pv_ctrl, ik_handle)

        ikChain.create_fk_ik_switch(switch_ctrl, ik_handle, up_arm_fk_zero, [arm_ik_zero, pv_zero])
        mc.parent(ik_handle, arm_ik_last_node)
        mc.setAttr(switch_ctrl+'.IK', 1)
        mc.hide(ik_handle)

        mc.addAttr(arm_ik_ctrl, ln='twist', k=1)

        mc.connectAttr(arm_ik_ctrl+'.twist', ik_handle+'.twist')
        if self.mirror_value < 0.0:
            utils.connect_negative(arm_ik_ctrl+'.twist', ik_handle+'.twist')

        # Create soft ik

        # new case for new hook
        ik_handle_grp = mc.createNode('transform', p=arm_ik_last_node, n=ik_handle+'_GRP')
        mc.parent(ik_handle_grp, jnt_grps[1])
        mc.parent(ik_handle, ik_handle_grp)
        mc.parentConstraint(arm_ik_last_node, hooks[1], mo=1)

        ik_joints = [up_arm_ik_jnt, lo_arm_ik_jnt, wrist_ik_jnt]
        ik_ctrl = arm_ik_ctrl

        ik_handle_parent = ikChain.create_soft_ik(ik_ctrl, ik_joints, ik_handle )

        # Create IK wrist orient switch
        jnt_follow_par = mc.duplicate(wrist_ik_ctrl+'_OFF', po=1, n=wrist_ik_zero+'_jnt_follow_par')[0]
        ctrl_follow_par = mc.duplicate(wrist_ik_ctrl+'_OFF', po=1, n=wrist_ik_zero+'_ikCtrl_follow_par')[0]

        jnt_follow = mc.duplicate(wrist_ik_ctrl+'_OFF', po=1, n=wrist_ik_zero+'_jnt_follow')[0]
        ctrl_follow = mc.duplicate(wrist_ik_ctrl+'_OFF', po=1, n=wrist_ik_zero+'_ikCtrl_follow')[0]

        mc.parent(ctrl_follow, ctrl_follow_par)
        mc.parent(jnt_follow, jnt_follow_par)
        mc.parent(jnt_follow_par, lo_arm_ik_jnt)

        oc = mc.orientConstraint(jnt_follow, ctrl_follow, wrist_ik_ctrl+'_OFF')[0]
        mc.setAttr(oc+'.interpType', 2)

        mc.addAttr(arm_ik_ctrl, ln='isolateWristOrientation', min=0, max=1, k=1)

        mdl = mc.createNode('multDoubleLinear', n=oc+'_mdl')
        mc.connectAttr(switch_ctrl+'.IK', mdl+'.input1', f=1)
        mc.connectAttr(arm_ik_ctrl+'.isolateWristOrientation', mdl+'.input2', f=1)

        mc.connectAttr(mdl+'.output', oc+'.w0')
        utils.connect_reverse(oc+'.w0', oc+'.w1')

        # connect ik blend to wrist orientConstraint
        oc = mc.orientConstraint(wrist_ik_last_node, wrist_ik_jnt, mo=1)[0]
        mc.setAttr(oc+'.interpType', 2)

        mc.connectAttr(switch_ctrl+'.IK', oc+'.w1')
        utils.connect_reverse(switch_ctrl+'.IK', oc+'.w0')

        # setup uparm FK orient
        up_arm_fk_orient_grp = up_arm_fk_ctrl+'_CONST'
        iso_follow_par = mc.duplicate(up_arm_fk_orient_grp, po=1, n=up_arm_fk_orient_grp+'_isolate_par')[0]
        iso_follow = mc.duplicate(up_arm_fk_orient_grp, po=1, n=up_arm_fk_orient_grp+'_isolate')[0]

        mc.parent(iso_follow, iso_follow_par)
        mc.parent(iso_follow_par, clavicle_zero)

        oc = mc.orientConstraint(up_arm_fk_zero, up_arm_fk_orient_grp, mo=1)[0]
        oc = mc.orientConstraint(iso_follow, up_arm_fk_orient_grp, mo=1)[0]
        mc.setAttr(oc+'.interpType', 2)

        mc.addAttr(up_arm_fk_ctrl, ln='isolateArmOrientation', min=0, max=1, k=1)
        mc.connectAttr(up_arm_fk_ctrl+'.isolateArmOrientation', oc+'.w1')
        utils.connect_reverse(oc+'.w1', oc+'.w0')

        # constraint the clavicle joint to the
        if double_clav:
            mc.parentConstraint(clavB_last_node, clavicle_jnt, mo=1)
            mc.parentConstraint(clavA_last_node, clavicleBase_jnt, mo = 1)
        else:
            mc.parentConstraint(clavicle_last_node, clavicle_jnt, mo=1)



        # Create twist
        if up_arm_twist_jnts:
            ikChain.upper_twist(utils.get_parent(up_arm_ik_jnt), up_arm_ik_jnt, lo_arm_ik_jnt, up_arm_jnt, lo_arm_jnt, up_arm_twist_jnts)
            ikChain.lower_twist(lo_arm_ik_jnt, wrist_ik_jnt, lo_arm_jnt, lo_arm_twist_jnts, wrist_jnt)

            ikChain.stretch_twist_jnts(up_arm_ik_jnt, lo_arm_ik_jnt, up_arm_twist_jnts)
            ikChain.stretch_twist_jnts(lo_arm_ik_jnt, wrist_ik_jnt, lo_arm_twist_jnts)

        else:
            mc.parentConstraint(up_arm_ik_jnt, up_arm_jnt ,mo=1)
            mc.parentConstraint(lo_arm_ik_jnt, lo_arm_jnt ,mo=1)
            mc.parentConstraint(wrist_ik_jnt, wrist_jnt ,mo=1)



        # create stretch
        ikChain.biped_stretch(arm_ik_ctrl,
                      arm_ik_last_node,
                      pv_ctrl,
                      switch_ctrl,
                      up_arm_fk_ctrl,
                      lo_arm_fk_ctrl,
                      wrist_fk_ctrl,
                      up_arm_ik_jnt,
                      lo_arm_ik_jnt,
                      wrist_ik_jnt,
                      ik_handle,
                      pin_attr_name='pinElbow',
                      shift_attr_name='shiftElbow')

        control.create_driven_shape(pv_ctrl, lo_arm_ik_jnt, replace=False)

        # lastly set up auto clavicle
        if double_clav:
            mc.parent(clavicleBase_jnt, jnt_grps[0])
        else:
            mc.parent(clavicle_jnt, jnt_grps[0])

        # Create all joints
        if double_clav:
            auto_shoulerBase = mc.duplicate(clavicleBase_jnt, po=1, n=clavicleBase_jnt+'_AUTO')[0]
        auto_clavicle = mc.duplicate(clavicle_jnt, po=1, n=clavicle_jnt+'_AUTO')[0]
        auto_lo_arm = mc.duplicate(lo_arm_jnt, po=1, n=lo_arm_jnt+'_AUTO')[0]
        auto_wrist = mc.duplicate(wrist_jnt, po=1, n=wrist_jnt+'_AUTO')[0]

        up_auto_clavicle = mc.duplicate(clavicle_jnt, po=1, n=clavicle_jnt+'_upper_AUTO')[0]
        up_auto_lo_arm = mc.duplicate(lo_arm_jnt, po=1, n=lo_arm_jnt+'_upper_AUTO')[0]

        mc.parent(auto_lo_arm, auto_clavicle)
        mc.parent(auto_wrist, auto_lo_arm)
        mc.parent(up_auto_lo_arm, up_auto_clavicle)


        # Create ik
        up_auto_ik_handle = mc.ikHandle(sj=up_auto_clavicle, ee=up_auto_lo_arm, s='sticky', n=prefix+'_arm_auto_clav_upper_IK')[0]
        auto_ik_handle = mc.ikHandle(sj=auto_clavicle, ee=auto_wrist, s='sticky', n=prefix+'_arm_auto_clav_IK')[0]

        mc.parent(auto_ik_handle, ik_handle_grp)
        mc.parent(up_auto_ik_handle, auto_clavicle)
        mc.setAttr(up_auto_ik_handle+'.poleVector', 0,0,0)

        mc.poleVectorConstraint(pv_ctrl, auto_ik_handle)
        mc.connectAttr(arm_ik_ctrl+'.twist', auto_ik_handle+'.twist')
        if self.mirror_value < 0.0:
            utils.connect_negative(arm_ik_ctrl+'.twist', auto_ik_handle+'.twist')

        # Create attrs
        if double_clav:
            mc.addAttr(clavicle_ctrl, ln = 'clavicleInfluence', min = 0, max = 10, k = 1)
            mc.addAttr(clavicle_ctrl, ln = 'clavicleBaseInfluence', min = 0, max = 10, k = 1)

        mc.addAttr(clavicle_ctrl, ln='autoClavicle', min=0, max=1, k=1)

        mc.addAttr(clavicle_ctrl, ln='clavUpLimit', min=0, dv=90, k=1)
        mc.addAttr(clavicle_ctrl, ln='clavDownLimit', min=0, dv=45, k=1)
        mc.addAttr(clavicle_ctrl, ln='clavFrontLimit', min=0, dv=90, k=1)
        mc.addAttr(clavicle_ctrl, ln='clavBackLimit', min=0, dv=90, k=1)

        mc.connectAttr(clavicle_ctrl+'.clavUpLimit', up_auto_clavicle+'.maxRotZLimit')
        mc.connectAttr(clavicle_ctrl+'.clavBackLimit', up_auto_clavicle+'.maxRotYLimit')
        utils.connect_negative(clavicle_ctrl+'.clavDownLimit', up_auto_clavicle+'.minRotZLimit')
        utils.connect_negative(clavicle_ctrl+'.clavFrontLimit', up_auto_clavicle+'.minRotYLimit')

        mc.setAttr(up_auto_clavicle+'.maxRotYLimitEnable', 1)
        mc.setAttr(up_auto_clavicle+'.minRotYLimitEnable', 1)
        mc.setAttr(up_auto_clavicle+'.maxRotZLimitEnable', 1)
        mc.setAttr(up_auto_clavicle+'.minRotZLimitEnable', 1)

        mc.hide(auto_clavicle, up_auto_clavicle, up_auto_ik_handle, auto_ik_handle)

        #adding double clavicle control influence
        if double_clav:
            pma = mc.createNode('plusMinusAverage', name = clavicle_ctrl + '_pma')
            mc.setAttr(pma + '.operation', 2)
            mc.setAttr(pma + '.input2D[0].input2Dx', 10)
            mc.connectAttr(clavicle_ctrl +'.clavicleInfluence' , pma + '.input2D[1].input2Dx')
            mc.connectAttr(pma + '.output2D.output2Dx', clavicle_ctrl +'.clavicleBaseInfluence')
            mc.setAttr(clavicle_ctrl + '.clavicleBaseInfluence', l = True)
            mc.setAttr(clavicle_ctrl + '.clavicleInfluence', 6)

            fract = mc.createNode('multiplyDivide', n = clavB_ctrl + '.md')
            mc.setAttr(fract+ '.input2', .1, .1, .1)
            mc.connectAttr(clavicle_ctrl +'.clavicleInfluence',fract + '.input1X')
            mc.connectAttr(clavicle_ctrl +'.clavicleInfluence',fract + '.input1Y')
            mc.connectAttr(clavicle_ctrl +'.clavicleInfluence',fract + '.input1Z')
            md = mc.createNode('multiplyDivide', n = clavB_ctrl+ 'Rotation.md')
            mc.connectAttr(clavicle_ctrl +'.rotate', md + '.input1')
            mc.connectAttr(fract + '.output', md + '.input2')
            mc.connectAttr( md + '.output', clavB_ctrl + '_MOCAP.rotate')


            fract = mc.createNode('multiplyDivide', n = clavA_ctrl +'.md')
            mc.setAttr(fract+ '.input2', .1, .1, .1)
            mc.connectAttr(clavicle_ctrl +'.clavicleBaseInfluence',fract + '.input1X')
            mc.connectAttr(clavicle_ctrl +'.clavicleBaseInfluence',fract + '.input1Y')
            mc.connectAttr(clavicle_ctrl +'.clavicleBaseInfluence',fract + '.input1Z')
            md = mc.createNode('multiplyDivide', n = clavA_ctrl + 'Rotation.md')
            mc.connectAttr(clavicle_ctrl +'.rotate', md + '.input1')
            mc.connectAttr(fract + '.output', md + '.input2')
            mc.connectAttr( md + '.output', clavA_ctrl + '_MOCAP.rotate')

        auto_follow_grp = mc.duplicate(clavicle_ctrl+'_CONST', po=1, n=clavicle_ctrl+'_AUTO_GRP')[0]
        auto_follow = mc.duplicate(clavicle_ctrl+'_CONST', po=1, n=clavicle_ctrl+'_AUTO')[0]
        stable = mc.duplicate(clavicle_ctrl+'_CONST', po=1, n=clavicle_ctrl+'_STABLE')[0]

        mc.parent(auto_follow, auto_follow_grp)
        mc.parent(auto_follow_grp, up_auto_clavicle)

        oc = mc.orientConstraint(stable, auto_follow, clavicle_ctrl+'_CONST')[0]
        mc.connectAttr(clavicle_ctrl+'.autoClavicle', oc+'.w1')
        utils.connect_reverse(clavicle_ctrl+'.autoClavicle', oc+'.w0')

        mc.setAttr(oc+'.interpType', 2)

        bendy_grp = prefix + '_bendyArm_CTL_GRP'
        if make_bendy:

            mc.parentConstraint(up_arm_ik_jnt, bendyArmACtrl[0], mo=1, n=bendyArmACtrl[0]+'_prc')
            mc.pointConstraint(up_arm_ik_jnt, lo_arm_ik_jnt, bendyArmACtrl[1]+'_CONST', mo=1, n=bendyArmACtrl[1]+'_CONST_pc')

            mc.parentConstraint(lo_arm_ik_jnt, bendyArmCCtrl[0], mo=1, n=bendyArmCCtrl[0]+'_prc')
            mc.pointConstraint(lo_arm_ik_jnt, wrist_ik_jnt, bendyArmCCtrl[1]+'_CONST', mo=1, n=bendyArmCCtrl[1]+'_CONST_pc')

            mc.parentConstraint(lo_arm_ik_jnt, bendyArmBCtrl[0], mo=1, n=bendyArmBCtrl[0]+'_prc')
            oc = mc.orientConstraint(up_arm_ik_jnt, lo_arm_ik_jnt, bendyArmBCtrl[1]+'_CONST', mo=1, n=bendyArmBCtrl[1]+'_CONST_pc')[0]
            mc.setAttr(oc+'.interpType', 2)

            bendy_joints_drivers = [up_arm_jnt]+up_arm_twist_jnts + [lo_arm_jnt]+lo_arm_twist_jnts+[wrist_jnt]
            bendy_ctrls = [bendyArmACtrl[-1], bendyArmBCtrl[-1], bendyArmCCtrl[-1]]
            noxform_grp = self.noxform_grp

            ikChain.biped_bendy(bendy_joints_drivers, bendy_ctrls, False, noxform_grp, ctrl_driver=bendyArmBCtrl[1])
            if not mc.objExists (bendy_grp):
                mc.createNode ('transform', n=bendy_grp, p=ctrl_grps[0])
            mc.parent ( [bendyArmACtrl[0], bendyArmBCtrl[0], bendyArmCCtrl[0]], bendy_grp)


        shpr_grp_name=prefix + '_shaper_CTL_GRP'
        shaper_ctrls = []
        shaper_zeros = []
        if up_arm_twist_jnts:
                shapers = up_arm_shaper_jnts + lo_arm_shaper_jnts
                for shaper in shapers:
                    name = shaper.replace('JNT', 'CTL')
                    shaper_fk_zero, shaper_fk_ctrl, shaper_fk_offsets, shaper_fk_last_node = self.anim_ctrl(name)
                    mc.parentConstraint(shaper_fk_ctrl, shaper)
                    driver = shaper.replace('shaper', 'twist')
                    mc.parentConstraint(driver, shaper_fk_zero, mo=0)
                    shaper_ctrls.append(shaper_fk_ctrl)
                    shaper_zeros.append(shaper_fk_zero)
                shpr_grp = mc.createNode('transform', name=shpr_grp_name, p=ctrl_grps[0])
                utils.set_attrs(shpr_grp, 'v', l=0, k=1)
                mc.parent(shaper_zeros, shpr_grp)

        #setup wrist joint////////////////////////////////////////////////////////////////////////////////////////
        pre=prefix+'_'

        #setup wrist joint////////////////////////////////////////////////////////////////////////////////////////

        offsets = {side: {"areas": {"Top": (0,.25,0),"Bottom": (0,-.25,0),"Inner": (0,0,.25),"Outer": (0,0,-.25)},
                          "nodes": {pre+"wristFixTopBottom_UTmd": {"type": "multiplyDivide",
                                                                                "attrs": {"input2Y": 0.05,
                                                                                          "input2Z": 0.05}},
                                    pre+"wristFixTopBottom_UTclmp": {"type": "clamp",
                                                                                  "attrs": {"minG": 0,"maxG": .5,
                                                                                            "minB": -.5,"maxB": 0}},
                                    pre+"wristFixInnerOuter_UTmd": {"type": "multiplyDivide",
                                                                                 "attrs": {"input2Y": -0.025,
                                                                                           "input2Z": -0.025}},
                                    pre+"wristFixInnerOuter_UTclmp": {"type": "clamp",
                                                                                   "attrs": {"minG": 0,"maxG": .5,
                                                                                             "minB": -.5,"maxB": 0}}},
                          "connections": [
                              [pre+"wrist_JNT.rotateZ",pre+"wristFixTopBottom_UTmd.input1Y"],
                              [pre+"wrist_JNT.rotateZ",pre+"wristFixTopBottom_UTmd.input1Z"],
                              [pre+"wristFixTopBottom_UTmd.outputY",
                               pre+"wristFixTopBottom_UTclmp.inputG"],
                              [pre+"wristFixTopBottom_UTmd.outputZ",
                               pre+"wristFixTopBottom_UTclmp.inputB"],
                              [pre+"wristFixTopBottom_UTclmp.outputG",
                               pre+"wristFixTop_JNT.translateY"],
                              [pre+"wristFixTopBottom_UTclmp.outputB",
                               pre+"wristFixBottom_JNT.translateY"],

                              [pre+"wrist_JNT.rotateY",pre+"wristFixInnerOuter_UTmd.input1Y"],
                              [pre+"wrist_JNT.rotateY",pre+"wristFixInnerOuter_UTmd.input1Z"],
                              [pre+"wristFixInnerOuter_UTmd.outputY",
                               pre+"wristFixInnerOuter_UTclmp.inputG"],
                              [pre+"wristFixInnerOuter_UTmd.outputZ",
                               pre+"wristFixInnerOuter_UTclmp.inputB"],
                              [pre+"wristFixInnerOuter_UTclmp.outputG",
                               pre+"wristFixInner_JNT.translateZ"],
                              [pre+"wristFixInnerOuter_UTclmp.outputB",
                               pre+"wristFixOuter_JNT.translateZ"]]}}

        mc.select (arm_ik_last_node)
        mc.joint (name=pre+'hand_JNT')
        mc.select (cl=1)
        hnd_name = pre+"hand_JNT"
        wri_name = pre+"wrist_JNT"
        hnd = pm.PyNode(hnd_name)
        wri = pm.PyNode(wri_name)

        #mak partial bind joints
        fix_name = pre+"wristFix_partial_JNT"
        jnt = encoreCommon.make_joint(fix_name,zero=True,world=True,clear_selection=True)
        # jnt.setAttr("drawStyle",0)
        jnt.setParent(wri,relative=True)
        pm.makeIdentity(jnt,apply=True,translate=True,rotate=True,scale=True,normal=False,preserveNormals=True)
        offset = 0.002
        if side == "Rt":
            offset *= -1
        jnt.setAttr("translateY",offset)
        ori = pm.orientConstraint(hnd,wri,jnt,maintainOffset=True,skip="x",weight=1.0)
        ori.setAttr("interpType",2)
        offsets[side]["partial_bind_joint"] = jnt

        #make_offset_hierarchies(
        d = offsets[side]
        pbj = d["partial_bind_joint"]
        d["offset_hierarchies"] = {}
        wrist_fix_binds=[]
        for area in d["areas"]:
            grp_name = pre+"wristFix{0}_GRP".format(area)
            bnd_name = pre+"wristFix{0}_JNT".format(area)
            bnd = encoreCommon.make_joint(bnd_name,zero=True,world=True,clear_selection=True)
            bnd.setAttr("drawStyle",0)
            grp = pm.group(name=grp_name)
            grp.setParent(pbj,relative=True)
            grp.setAttr("translate",d["areas"][area])
            d["offset_hierarchies"][area] = (grp,bnd)
            wrist_fix_binds.append (bnd)

        #create_nodes(side):
        encoreCommon.debug_print("setupWrists: create_nodes:",dbg=False)
        d = offsets[side]["nodes"]
        for key in d:
            typ = d[key]["type"]
            encoreCommon.debug_print("\tCreating "+typ+" node: "+key,dbg=False)
            n = pm.createNode(typ,name=key)
            for attr in d[key]["attrs"]:
                v = d[key]["attrs"][attr]
                n.setAttr(attr,v)

        #make_connections
        encoreCommon.debug_print("setupWrists: make_connections",dbg=False)
        cons = offsets[side]["connections"]
        for con in cons:
            encoreCommon.debug_print("\tConnecting: "+con[0]+"to:"+con[1],dbg=False)
            pm.connectAttr(con[0],con[1])



        #//////////////////////////////////////////////////////////////////////////////////////////////////////////
        #
        # #setup elbow vj and fix Joints


        flip = 1
        if side == 'Rt':
            flip=-1

        elbow_fix_fnt_jnt = prefix+'_elbowFrontFix_JNT'
        elbow_fix_bck_jnt = prefix+'_elbowBckFix_JNT'


        front_name = elbow_fix_fnt_jnt
        back_name =elbow_fix_bck_jnt

        vjname =pre+'elbowVJ_JNT'
        vjpar=utils.get_parent(up_arm_grp)
        sources=(up_arm_twist_jnts[-1],lo_arm_twist_jnts[0])
        vjjnt=mc.joint(name=vjname)
        mc.select (clear=1)
        mc.parent (vjjnt, vjpar)
        mc.orientConstraint (sources, vjjnt, mo=0)
        mc.pointConstraint (lo_arm_jnt, vjjnt, mo=0)

        # for name in [front_name,back_name]:
        #     pm.select(vjjnt)
        #     pm.joint(name=name)
        d = {front_name: {"translateZ": [{"cd": lo_arm_ik_jnt+".rotateY","keys": [(0,.5 * flip),(-40,1 * flip)]}]},
            back_name: {"translateZ": [{"cd": lo_arm_ik_jnt+".rotateY","keys": [(0,-.5 * flip),(-40,-1.25 * flip)]}]}}

        # d = {front_name: {"translateZ": [{"cd": elbow_ik_jnt+".rotateY","keys": [(0,4 * flip),(-40,8 * flip)]}]},
        #     back_name: {"translateZ": [{"cd": elbow_ik_jnt+".rotateY","keys": [(0,-4 * flip),(-40,-8 * flip)]}]}}

        mc.parent (front_name, back_name, vjjnt)

        for obj in d:
            for attr in d[obj]:
                for x in d[obj][attr]:
                    for key in x["keys"]:
                        cd = x["cd"]
                        pm.setDrivenKeyframe(obj,attribute=attr,currentDriver=cd,driverValue=key[0],value=key[1],
                                             inTangentType='linear',outTangentType='linear')
        # # mc.setAttr(front_name+".radius",1)
        # # mc.setAttr(back_name+".radius",1)
        # # mc.setAttr(vjjnt+".radius",5)
        #


        # clean up now
        mc.hide(up_arm_ik_jnt)

        mc.parentConstraint(wrist_jnt, switch_zero, mo=1)
        if double_clav:
            mc.parent(clavA_zero, ctrl_grps[0])
        mc.parent(clavicle_zero, arm_ik_zero, pv_zero, switch_zero, ctrl_grps[0])

        utils.set_attrs([up_arm_fk_ctrl, wrist_ik_ctrl, lo_arm_fk_ctrl, wrist_fk_ctrl], 't s v', l=1, k=0)
        utils.set_attrs(lo_arm_fk_ctrl, 'ro', l=1, k=0)
        utils.set_attrs(pv_ctrl, 'r s v ro', l=1, k=0)
        utils.set_attrs(lo_arm_fk_ctrl, 'ro', l=1, k=0)
        utils.set_attrs(switch_ctrl, 't r s v ro', l=1, k=0)
        utils.set_attrs(clavicle_ctrl, 's', l=1, k=0)

        utils.set_attrs(arm_ik_offsets+[arm_ik_ctrl], ' s v ro jo radius', l=1, k=0, cb=0)
        for c in arm_ik_offsets+[arm_ik_ctrl]:
            mc.setAttr(c+'.radius', k=0, cb=0)

        # create pv aim at space
        aim_drv = mc.duplicate(up_arm_ik_jnt, n=pv_ctrl+'_AIM_DRV', po=1)[0]
        aim_drv_end = mc.duplicate(lo_arm_ik_jnt, n=pv_ctrl+'_AIM_DRV_end', po=1)[0]
        aim_drv_ik = mc.duplicate(wrist_ik_jnt, n=pv_ctrl+'_IK_DRV_end', po=1)[0]

        pos = mc.createNode('transform', n=aim_drv+'_POS', p=aim_drv)
        mc.parent(pos, clavicle_zero)
        mc.parent(aim_drv, jnt_grps[0])
        mc.parent(aim_drv_end, aim_drv)
        mc.setAttr(aim_drv_end+'.tx', mc.getAttr(aim_drv_end+'.tx')*0.05)
        mc.pointConstraint(pos, aim_drv)

        aim_ik = mc.ikHandle(sj=aim_drv, ee=aim_drv_end, n=aim_drv+'_IK', sol='ikSCsolver', s='sticky')[0]
        mc.pointConstraint(aim_drv_ik, aim_ik)

        mc.parent(aim_drv_ik ,jnt_grps[1])
        mc.parent(aim_ik, utils.get_parent(aim_drv))

        mc.hide(aim_drv, aim_drv_end, aim_ik, aim_drv_ik)

        # spaces
        spaces.tag(arm_ik_ctrl, default=0)
        spaces.tag(pv_ctrl, 'arm:'+aim_drv, default=1)

        jnts = [clavicle_jnt, up_arm_jnt]+up_arm_twist_jnts+[lo_arm_jnt]+lo_arm_twist_jnts+[wrist_jnt, wrist_end_jnt]
        #utils.create_cfx_curves(jnts, self.prefix+'_'+self.part_type)

        # movable pivot
        control.create_movable_pivot(arm_ik_ctrl, ctrl_type='joint')
        mc.parent(self.prefix+'_arm_IK_PIV_CTL_GRP', arm_ik_ctrl+'_MOCAP')

        mc.setAttr(clavicle_ctrl+'.clavUpLimit', k=0, cb=1)
        mc.setAttr(clavicle_ctrl+'.clavDownLimit', k=0, cb=1)
        mc.setAttr(clavicle_ctrl+'.clavFrontLimit', k=0, cb=1)
        mc.setAttr(clavicle_ctrl+'.clavBackLimit', k=0, cb=1)

        # This finalizes guide and creates rig sets
        nodes = [up_arm_fk_ctrl, lo_arm_fk_ctrl, wrist_fk_ctrl]
        self.create_ctrl_set('FK', nodes)
        if mc.objExists (bendy_grp):
            mc.addAttr(switch_ctrl, ln='bendyCtrlVis', min=0, max=1, k=1, dv=0)
            mc.connectAttr (switch_ctrl+'.bendyCtrlVis', bendy_grp+'.visibility')
            mc.addAttr(switch_ctrl, ln='shaperCtrlVis', min=0, max=1, k=1, dv=0)
            utils.set_attrs(shpr_grp_name, 'v', l=0, k=1)
            mc.connectAttr(switch_ctrl + '.shaperCtrlVis', shpr_grp_name + '.visibility')

        # This sets up the pickwalk hierarchy the animators will work with. Subject to change.
        # attribute_tag(ctrl, parent)
        ikChain.tag_match_function(switch_ctrl, 'bipedarm')
        ikChain.create_snapto_node(pv_ctrl, lo_arm_ik_jnt)
        ikChain.create_snapto_node(arm_ik_ctrl, wrist_ik_jnt)

        pickWalk.attribute_tag(up_arm_fk_ctrl,clavicle_ctrl)
        pickWalk.attribute_tag(wrist_fk_ctrl,lo_arm_fk_ctrl)

        pickWalk.attribute_tag(arm_ik_ctrl,pv_ctrl)
        pickWalk.attribute_tag(pv_ctrl, clavicle_ctrl)

        pickWalk.attribute_tag(clavicle_ctrl, pickWalk_parent)
        pickWalk.attribute_tag(switch_ctrl, arm_ik_ctrl)

        if make_bendy:
            pickWalk.attribute_tag(bendyArmCCtrl[-1], bendyArmBCtrl[-1])
            pickWalk.attribute_tag(bendyArmBCtrl[-1], bendyArmACtrl[-1])
            pickWalk.attribute_tag(bendyArmACtrl[-1], clavicle_ctrl)


        self.finalize_part()

