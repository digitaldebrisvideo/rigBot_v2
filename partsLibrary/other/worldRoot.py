# -*- rigBot: part  -*-

import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import env
from rigBot.partsLibrary import standardPart

class WorldRoot(standardPart.StandardPart):
    """Build rig root nodes. Every rig needs this and this part
        cannot be modified. You can set the number of world controls
        by setting the ``world_CTL.numOffsetCtrls`` attribute

        Build Options:
            :NONE: This module has no modifiable options."""

    def __init__(self):
        standardPart.StandardPart.__init__(self)

    def build_guide(self, **kwargs):
        """This builds your guide"""

        # This builds your guide master and updates your options
        self.create_guide_master(**kwargs)

        prefix       = self.prefix
        options      = self.options
        mirror_value = self.mirror_value

        side = options.get('side')
        world_result = self.guide_joint('world')
        root_result = self.guide_joint('root')

        mc.parent(root_result[-1], world_result[-1])

        zero, ctrl = self.guide_ctrl(name='world',
                                     shape='arrow_quad_world',
                                     color='black',
                                     driver=root_result[-1],
                                     create_pivot=False,
                                     allow_offset_ctrls=True)

        ct_z, ct_pl = self.guide_joint('vis', placer_only=1)

        vzero, vctrl = self.guide_ctrl(name='visibility',
                             shape='eye',
                             color='lavendar',
                             driver=ct_pl,
                             create_pivot=False,
                             allow_offset_ctrls=0)

        # dzero, dctrl = self.guide_ctrl(name='dynamic',
        #                      shape='letter_d',
        #                      color='lavendar',
        #                      driver=ct_pl,
        #                      create_pivot=False,
        #                      allow_offset_ctrls=0)

        # cvs = mc.ls(prefix+'*world*.cv[*]')
        # mc.xform(cvs, r=1, s=[5,5,5])
        mc.setAttr(ctrl+'.numOffsetCtrls', 1)
        mc.delete(world_result[0])
        utils.set_attrs(root_result[:2], l=1, k=0)

        # rename offset ctrls to be normal ctrls
        ctrl_suffix = utils.get_suffix('animCtrl')
        off_suffix = utils.get_suffix('animCtrlOffset')

        offset_ctrls = mc.ls(prefix+'*'+off_suffix)
        for ctrl in offset_ctrls:
            mc.rename(ctrl, ctrl.replace(off_suffix, ctrl_suffix, 1))

        mc.setAttr(self.guide_master+'.offsetTranslateY', -0.5)
        utils.set_attrs(self.guide_master, 'r', l=1, k=0)

        try:
            mc.setAttr(ct_pl+'.offsetTranslateY', 0.6)
        except:
            pass

        mc.xform(ct_z, r=1, t=[0,200,0])
        mc.parentConstraint(root_result[-1], ct_z, mo=1)

        mc.setAttr(utils.get_children(vzero)[0]+'.tx', 0.5)
        # mc.setAttr(utils.get_children(dzero)[0]+'.tx', -0.5)

        utils.set_attrs(ct_pl,k=0, l=1)
        utils.set_attrs(ct_pl, 't s',k=1, l=0)

        # mc.scaleConstraint(ct_pl, dzero, mo=1)
        mc.scaleConstraint(ct_pl, vzero, mo=1)

        # This finalizes your guide.
        self.finalize_guide()

        if not self.guide_master or not mc.objExists(self.guide_master):
            return

        ctrls = []
        for ctrl in self.anim_ctrls:
            ctrls.append(mc.rename(ctrl, ctrl.replace(side+'_', '', 1)))

        self.anim_ctrls = ctrls
        mc.setAttr(self.guide_master+'.CTLS', str(ctrls), type='string')

        mc.rename('C_vis_JNT_PLC', 'vis_PLC')


    def build_rig(self):
        """This builds your anim rig."""

        options = self.options

        # START CODING  !!
        side = options.get('side')
        name = options.get('name')

        self.anim_ctrls.sort()
        if 'world_CTL' in self.anim_ctrls:
            self.anim_ctrls.remove('world_CTL')
        if 'visibility_CTL' in self.anim_ctrls:
            self.anim_ctrls.remove('visibility_CTL')
        # if 'dynamic_CTL' in self.anim_ctrls:
        #     self.anim_ctrls.remove('dynamic_CTL')

        self.anim_ctrls.insert(0, 'world_CTL')

        ctrl_names = self.anim_ctrls
        jnt_names = self.bind_joints

        # ct_suffix = utils.get_suffix('transform')
        ct_suffix =  'GRP'

        jnt_suffix = utils.get_suffix('joint')

        # Create ctrl heirarchy
        ctrls = []
        for ctrl_name in ctrl_names:

            zero, ctrl, offsets, last_node = self.anim_ctrl(ctrl_name, num_offset_ctrls=0)
            if ctrls:
                mc.parent(ctrl, ctrls[-1])
            else:
                mc.parent(ctrl, w=1)

            mc.delete(zero)
            ctrls.append(ctrl)

        vzero, vctrl, voffsets, vlast_node = self.anim_ctrl('visibility_CTL', num_offset_ctrls=0)
        # dzero, dctrl, doffsets, dlast_node = self.anim_ctrl('dynamic_CTL', num_offset_ctrls=0)
        # Create groups
        grp_name = ('parts_{1}'.format(side, ct_suffix))
        hook_grp = mc.createNode('transform', n=grp_name, p=last_node)

        for node in ctrls:
            mc.addAttr(node, ln='globalScale', k=1, min=.001, dv=1)
            mc.connectAttr(node+'.globalScale', node+'.sx')
            mc.connectAttr(node+'.globalScale', node+'.sy')
            mc.connectAttr(node+'.globalScale', node+'.sz')
            mm.eval('transformLimits -sy 0.01 1 -esy 1 0 '+node)

        # utils.set_attrs('world_CTL', 's', )
        utils.set_attrs(ctrls, 'sx sy sz', l=1, k=0)
        utils.set_attrs(vctrl,  l=1, k=0)
        # utils.set_attrs(dctrl,  l=1, k=0)
        # print dctrl

        # add vctrl attrs
        mc.addAttr(vctrl, ln='jointsVis', k=1, at='bool', dv=1)
        mc.addAttr(vctrl, ln='modelVis', k=1, at='bool', dv=1)
        mc.addAttr(vctrl, ln='jointsSelectable', k=1, at='bool', dv=1)
        mc.addAttr(vctrl, ln='modelSelectable', k=1, at='bool', dv=1)

        # add vctrl attrs
        mc.addAttr(vctrl, ln='_', nn=' ', at='enum', en=' ', k=1)
        mc.addAttr(vctrl, ln='allCtrlsVis', k=1, at='bool', dv=1)
        mc.addAttr(vctrl, ln='offsetCtrlsVis', k=1, at='bool', dv=1)

        # create global scale value
        dmtx = mc.createNode('decomposeMatrix', n=last_node+'_dmtx')
        mc.connectAttr(last_node+'.worldMatrix', dmtx+'.inputMatrix')

        mc.addAttr(ctrls[0], ln='worldScale', k=1)
        mc.connectAttr(dmtx+'.outputScaleY', ctrls[0]+'.worldScale')

        # Now create part master nodes
        result = self.create_part_master()

        # parent jnt
        world_jnt = [j for j in jnt_names if 'world' in j][0]
        root_jnt = [j for j in jnt_names if 'root' in j][0]

        # unparent root jnts to foloorw world ctrls
        mc.parent(world_jnt, self.jnt_grps[0])
        mc.parent(root_jnt, self.jnt_grps[0])

        mc.parent(vzero, self.ctrl_grps[0])
        # mc.parent(dzero, self.ctrl_grps[0])

        # parent true world jnt ot world no xform
        mc.setAttr(world_jnt+'.it', 0)
        mc.setAttr(world_jnt+'.it', l=1)

        grp_suffix = utils.get_suffix('transform')

        # finalizes part build (creates sets, etc.)
        self.finalize_part()

        rig_grp = mc.createNode('transform', n='rig_GRP')
        utils.set_attrs(rig_grp, l=1, k=0)
        mc.parent(ctrls[0], rig_grp)

        nox_grp = mc.createNode('transform', n='noXform_GRP')
        utils.set_attrs(nox_grp, l=1, k=0)
        utils.set_attrs(nox_grp, 'v it', l=0, k=1)
        mc.parent(nox_grp, rig_grp)

        mc.setAttr(nox_grp+'.it', 0)
        mc.setAttr(nox_grp+'.it', l=1, k=0)

        mc.parent('guides_REF', rig_grp)
        mc.setAttr('guides_REF.it', 0)
        mc.setAttr('guides_REF.it', l=1, k=0)
        utils.set_attrs('guides_REF', l=1, k=0)
        mc.setAttr('guides_REF.v', l=0, k=1)

        utils.set_attrs('parts_GRP', l=1, k=0)
        mc.setAttr('parts_GRP.v', l=0, k=1)

        jnts = [j.replace('.partTopJoint', '') for j in mc.ls('*.partTopJoint')]
        jnts = [j for j in jnts if not j.endswith('_REF')]

        if root_jnt in jnts:
            jnts.remove(root_jnt)

        if world_jnt in jnts:
            jnts.remove(world_jnt)

        if jnts:
            mc.parent(jnts, self.jnt_grps[0])

        # loc_parent_grp = 'world_locator_{1}'.format(side, grp_suffix)
        # if not mc.objExists(loc_parent_grp):
        #     mc.createNode('transform', n=loc_parent_grp, p=rig_grp)
        #
        #     mc.hide(loc_parent_grp)
        #     mc.setAttr(loc_parent_grp+'.it', 0)
        #     mc.setAttr(loc_parent_grp+'.it', l=1)
        #     utils.set_attrs(loc_parent_grp, 't r s', k=0, l=1)
        #
        # parent_grp = 'fx_curve_{1}'.format(side, ct_suffix)
        # if not mc.objExists(parent_grp):
        #     mc.createNode('transform', n=parent_grp, p=rig_grp)
        #
        #     mc.hide(parent_grp)
        #     mc.setAttr(parent_grp+'.it', 0)
        #     mc.setAttr(parent_grp+'.it', l=1)
        #     utils.set_attrs(parent_grp, 't r s', k=0, l=1)

        mc.hide(world_jnt)

        # now unparent anything left over
        children = utils.get_children('skel_GRP')
        if children:
            mc.parent(children, w=1)

        mc.delete('skel_GRP')
