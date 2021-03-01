import maya.cmds as cmds

vis_ctrl = 'visibility_anim'
pairs = zip('xyz', 'RGB')
spineDict = {'spineShaper03_Mid_bind':(1, 0.9), 'spineShaper04_Mid_bind':(1,0.8)}
clavicleDict = {'clavicle_Lt_anim':[[[0, 0], [0.5, -5.5]],[[0, 0], [0.5, 1.8]], [[0, 0], [0.5, 4.0]]], 'clavicle_Rt_anim':[[[0, 0], [0.5, -5.5]],[[0, 0], [0.5, 1.8]], [[0, 0], [0.5, 4.0]]]  }
shoulderDict = {'shoulder_Lt_anim':[[[0, 0], [0.5, 5.5]],[[0, 0], [0.5, -1.8]], [[0, 0], [0.5, -4.0]]], 'shoulder_Rt_anim':[[[0, 0], [0.5, 5.5]],[[0, 0], [0.5, -1.8]], [[0, 0], [0.5, -4.0]]]  }
headDist = {'neck01Fk_Mid_anim': ['translateY',(0.375, 0.5)], 'head_Mid_anim':['rotateZ',(0.625,-1.35)]}
pecsDict = {'pectorals_Lt_anim':[[[0, 0], [0.4, 1.5]],[[0, 0], [0.35, 2]], [[0, 0], [0.35, 2.5]]], 'pectorals_Rt_anim':[[[0, 0], [0.4, -1.5]],[[0, 0], [0.35, -2]], [[0, 0], [0.35, -2.5]]], 'pecs_1_Lt_anim':[[[0, 0], [0.0, 0.0]],[[0, 0], [0.55, -0.15]], [[0, 0], [0.55, -0.85]]], 'pecs_1_Rt_anim':[[[0, 0], [0.0, 0.0]],[[0, 0], [0.55, -0.15]], [[0, 0], [0.55, 0.85]]]  }


def makeCtrl(obj):
    crv = []
    name = obj.replace('_jnt', '_anim')
    shape = cmds.curve(d =  1,  p= [(1, 1, 1 ), ( 1, 1, -1 ), ( -1, 1, -1 ), ( -1, -1, -1 ), ( 1, -1, -1 ), ( 1, 1, -1 ), ( -1, 1, -1 ), ( -1, 1, 1 ), ( 1, 1, 1 ), ( 1, -1, 1 ), ( 1, -1, -1 ), ( -1, -1, -1 ), ( -1, -1, 1 ), ( 1, -1, 1 ), ( -1, -1, 1 ), ( -1, 1, 1)], k =[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 ,  10 ,  11 ,  12 ,  13 ,  14 ,  15 ],  n = name)
    crv.append(shape)
    grp_item = cmds.group(em=1, n = (crv[0].replace('anim', 'ctrl') + 'Grp'))
    cmds.parent(crv[0], grp_item)
    grp_offset = cmds.group(em=1, n = (grp_item + 'Offset'))
    cmds.parent(grp_item, grp_offset)
    p_con = cmds.parentConstraint(obj, grp_offset)
    cmds.delete(p_con)
    return grp_offset
    #######################################################################################
    # DELETE BREATH
def deleteBreathAttrs():
    if cmds.objExists(vis_ctrl):
        mainAttrs = ['breath', 'breath_enable']
        for attr in mainAttrs:
            if cmds.attributeQuery(attr, n = vis_ctrl, ex=1):
                cmds.setAttr(vis_ctrl +  '.' + attr, 0)
                cmds.deleteAttr(vis_ctrl, at = attr)


def deleteAllBreath():
    deleteBreathByPart(pecsDict)
    deleteBreathByPart(spineDict)
    deleteBreathByPart(headDist)    
    deleteBreathByPart(clavicleDict)
    deleteBreathByPart(shoulderDict)
    deleteBreathAttrs()
def deleteBreathByPart(input):
    for jnt in input.items():
        if not 'spine' in jnt[0]:
            root = cmds.listRelatives(jnt[0], p=1)[0]
            brGrp = jnt[0].replace('anim', 'br')
            sdkGrp = jnt[0].replace('anim', 'sdk')
            if 'sdk' in root:
                cmds.parent(jnt[0], cmds.listRelatives(root, p=1)[0], a=1)
                cmds.delete(brGrp, sdkGrp)
        if 'spine' in jnt[0]:
            brGrp = jnt[0].replace('bind', 'br')
            if cmds.objExists(brGrp):
                bcNode = cmds.listConnections(brGrp + '.sy', d=1, s=0)
                if bcNode:
                    cmds.delete(bcNode)
                cmds.delete(brGrp)            
def buildShoulderBreath(shoulderDict):
    buildBreathAttr()
    mainAttrs = ['breath', 'breath_enable']
    #######################################################################################
    # BUILD SHOULDER BREATH
    for shld in shoulderDict.items():
        for ax in 'xyz':
            cmds.setAttr(shld[0] + '.s' + ax, l=0)
        shld_br_grp = shld[0].replace('anim', 'br')
        if not cmds.objExists(shld_br_grp):
            shld_br_grp = cmds.duplicate(shld[0], rr=1, rc=1, n = shld[0].replace('anim', 'br'))[0]
        shld_sdk_grp =shld[0].replace('anim', 'sdk')
        if not cmds.objExists(shld_sdk_grp):
            shld_sdk_grp = cmds.duplicate(shld[0], rr=1, rc=1, n = shld[0].replace('anim', 'sdk'))[0]
        if cmds.listRelatives(shld[0], p =1)[0] == shld_sdk_grp:
            print '############################# PECS INFO ################################'
            cmds.warning( shld[0] + ' has breath system')
        if cmds.listRelatives(shld[0], p =1)[0] != shld_sdk_grp:
            cmds.delete(cmds.listRelatives(shld_sdk_grp, c=1), cmds.listRelatives(shld_br_grp, c=1))
            cmds.parent(shld[0], shld_sdk_grp, a=1) 
            cl_bc_Node = cmds.createNode('blendColors', n = shld[0].replace('anim','bc'))
            cmds.connectAttr(vis_ctrl + '.' + mainAttrs[1], cl_bc_Node + '.blender', f=1)
            for pair in pairs:
                cmds.setAttr(cl_bc_Node + '.color2' + pair[1], 0)
                cmds.connectAttr(shld_br_grp + '.r' + pair[0], cl_bc_Node + '.color1' + pair[1], f=1)
                cmds.connectAttr(cl_bc_Node + '.output' + pair[1], shld_sdk_grp + '.r'+ pair[0], f=1)
            for ax in 'xyz':
                animNode = cmds.createNode('animCurveUU', n = shld[0] + '_rotate' + ax.capitalize())
                cmds.setKeyframe(animNode, float=float(0), value=float(0))
                cmds.setKeyframe(animNode, float=float(shld[1]['xyz'.index(ax)][1][0]), value=float(shld[1]['xyz'.index(ax)][1][1]))
                cmds.connectAttr(vis_ctrl + '.' + mainAttrs[0], animNode + '.input', f=1)
                cmds.connectAttr(animNode + '.output', shld_br_grp + '.r'+ ax, f=1)


def buildPecsBreath(pecsDict):
    buildBreathAttr()
    mainAttrs = ['breath', 'breath_enable']
    #######################################################################################
    # BUILD PECS BREATH
    for pecs in pecsDict.items():
        if not cmds.objExists(pecs[0]):
            jntSrc = pecs[0].replace('anim', 'jnt')
            ctrlGrp = makeCtrl(jntSrc)
            cmds.parent(ctrlGrp, 'character02_Mid_anim', a=1)
            cmds.parentConstraint('chest_Mid_bind', ctrlGrp, mo=1)
    for pecs in pecsDict.items():
        pcs_br_grp = pecs[0].replace('anim', 'br')
        pcs_sdk_grp =pecs[0].replace('anim', 'sdk')
        if not cmds.objExists(pcs_br_grp):
            pcs_br_grp = cmds.duplicate(pecs[0], rr=1, rc=1, n = pcs_br_grp)
        if not cmds.objExists(pcs_sdk_grp):
            pcs_sdk_grp = cmds.duplicate(pecs[0], rr=1, rc=1, n = pcs_sdk_grp)
        if cmds.listRelatives(pecs[0], p =1)[0] == pcs_sdk_grp:
            print '############################# PECS INFO ################################'
            cmds.warning( pecs[0] + ' has breath system')
        if cmds.listRelatives(pecs[0], p =1)[0] != pcs_sdk_grp:
            cmds.delete(cmds.listRelatives(pcs_sdk_grp, c=1), cmds.listRelatives(pcs_br_grp, c=1))
            cmds.parent(pecs[0], pcs_sdk_grp[0], a=1) 
            pecs_bc_Node = cmds.createNode('blendColors', n = pecs[0].replace('anim','bc'))
            cmds.connectAttr(vis_ctrl + '.' + mainAttrs[1], pecs_bc_Node + '.blender', f=1)
            for pair in pairs:
                cmds.setAttr(pecs_bc_Node + '.color2' + pair[1], 0)
                cmds.connectAttr(pcs_br_grp[0] + '.t' + pair[0], pecs_bc_Node + '.color1' + pair[1], f=1)
                cmds.connectAttr(pecs_bc_Node + '.output' + pair[1], pcs_sdk_grp[0] + '.t'+ pair[0], f=1)
            for ax in 'xyz':
                animNode = cmds.createNode('animCurveUU', n = pecs[0] + '_translate' + ax.capitalize())
                cmds.setKeyframe(animNode, float=float(0), value=float(0))
                cmds.setKeyframe(animNode, float=float(pecs[1]['xyz'.index(ax)][1][0]), value=float(pecs[1]['xyz'.index(ax)][1][1]))
                cmds.connectAttr(vis_ctrl + '.' + mainAttrs[0], animNode + '.input', f=1)
                cmds.connectAttr(animNode + '.output', pcs_br_grp[0] + '.t'+ ax, f=1)

            
def buildClavicleBreath(clavicleDict):
    buildBreathAttr()
    mainAttrs = ['breath', 'breath_enable']
    #######################################################################################
    # BUILD CLAVICLE BREATH
    for clv in clavicleDict.items():
        for ax in 'xyz':
            cmds.setAttr(clv[0] + '.s' + ax, l=0)
        clv_br_grp = clv[0].replace('anim', 'br')
        if not cmds.objExists(clv_br_grp):
            clv_br_grp = cmds.duplicate(clv[0], rr=1, rc=1, n = clv[0].replace('anim', 'br'))[0]
        clv_sdk_grp =clv[0].replace('anim', 'sdk')
        if not cmds.objExists(clv_sdk_grp):
            clv_sdk_grp = cmds.duplicate(clv[0], rr=1, rc=1, n = clv[0].replace('anim', 'sdk'))[0]
        if cmds.listRelatives(clv[0], p =1)[0] == clv_sdk_grp:
            print '############################# CLAVICLE INFO ################################'
            cmds.warning( clv[0] + ' has breath system')     
        if cmds.listRelatives(clv[0], p =1)[0] != clv_sdk_grp:
            cmds.delete(cmds.listRelatives(clv_sdk_grp, c=1), cmds.listRelatives(clv_br_grp, c=1))
            cmds.parent(clv[0], clv_sdk_grp, a=1) 
            cl_bc_Node = cmds.createNode('blendColors', n = clv[0].replace('anim','bc'))
            cmds.connectAttr(vis_ctrl + '.' + mainAttrs[1], cl_bc_Node + '.blender', f=1)
            for pair in pairs:
                cmds.setAttr(cl_bc_Node + '.color2' + pair[1], 0)
                cmds.connectAttr(clv_br_grp + '.r' + pair[0], cl_bc_Node + '.color1' + pair[1], f=1)
                cmds.connectAttr(cl_bc_Node + '.output' + pair[1], clv_sdk_grp + '.r'+ pair[0], f=1)
            for ax in 'xyz':
                #print clv[1]['xyz'.index(ax)][1][0] , clv[1]['xyz'.index(ax)][1][1]
                animNode = cmds.createNode('animCurveUU', n = clv[0] + '_rotate' + ax.capitalize())
                cmds.setKeyframe(animNode, float=float(0), value=float(0))
                cmds.setKeyframe(animNode, float=float(clv[1]['xyz'.index(ax)][1][0]), value=float(clv[1]['xyz'.index(ax)][1][1]))
                cmds.connectAttr(vis_ctrl + '.' + mainAttrs[0], animNode + '.input', f=1)
                cmds.connectAttr(animNode + '.output', clv_br_grp + '.r'+ ax, f=1)
            
def buildHeadBreath(headDist):
    buildBreathAttr()
    mainAttrs = ['breath', 'breath_enable']
    #######################################################################################
    # BUILD NECK, HEAD BREATH
    for item in headDist.iteritems():
        br_grp = item[0].replace('anim', 'br')
        if not cmds.objExists(br_grp):
            br_grp= cmds.duplicate(item[0], rr=1, rc=1, n = item[0].replace('anim', 'br'))[0]
        sdk_br_grp =item[0].replace('anim', 'sdk')
        if not cmds.objExists(sdk_br_grp):
            sdk_br_grp= cmds.duplicate(item[0], rr=1, rc=1, n = item[0].replace('anim', 'sdk'))[0]
        if cmds.listRelatives(item[0], p =1)[0] == sdk_br_grp:
            print '############################# HEAD INFO ################################'
            cmds.warning( item[0] + ' has breath system')             
        if cmds.listRelatives(item[0], p =1)[0] == sdk_br_grp:
            cmds.delete(cmds.listRelatives(br_grp, c=1), cmds.listRelatives(sdk_br_grp, c=1))
            cmds.parent(item[0], sdk_br_grp, a=1)
            animNode = cmds.createNode('animCurveUU', n = br_grp[0] + '_' + item[1][0])
            cmds.setKeyframe(animNode, float=float(0), value=float(0))
            cmds.setKeyframe(animNode, float=float(item[1][1][0]), value=float(item[1][1][1]))
            cmds.connectAttr(vis_ctrl + '.' + mainAttrs[0], animNode + '.input', f=1)
            cmds.connectAttr(animNode + '.output', br_grp[0] + '.' + item[1][0] , f=1)
            head_bc_Node = cmds.createNode('blendColors', n = item[0].replace('anim','bc'))
            cmds.connectAttr(vis_ctrl + '.' + mainAttrs[1], head_bc_Node + '.blender', f=1)
            for pair in pairs:
                cmds.setAttr(head_bc_Node + '.color2' + pair[1], 0)
            cmds.connectAttr(br_grp[0] + '.' + item[1][0], head_bc_Node + '.color1R', f=1)
            cmds.connectAttr(head_bc_Node + '.outputR', sdk_br_grp[0] + '.' +item[1][0], f=1)
def buildSpineBreath(spineDict):
    buildBreathAttr()
    mainAttrs = ['breath', 'breath_enable']
    #######################################################################################
    # BUILD SPINE BREATH
    for jnt in spineDict.items():
        for ax in 'xyz':
            cmds.setAttr(jnt[0] + '.s' + ax, l=0)
        if not cmds.objExists(jnt[0].replace('bind', 'br')):
            br_jnt= cmds.duplicate(jnt[0], rr=1, n = jnt[0].replace('bind', 'br'))
            animNode = cmds.createNode('animCurveUU', n = br_jnt[0] + '_scaleY')
            cmds.setKeyframe(animNode, float=float(0), value=float(jnt[1][0]))
            cmds.setKeyframe(animNode, float=float(0.5), value=float(jnt[1][1]))
            cmds.connectAttr(vis_ctrl + '.' + mainAttrs[0], animNode + '.input', f=1)
            cmds.connectAttr(animNode + '.output', br_jnt[0] + '.sy', f=1)
            # create blendColor node
            bcNode = cmds.createNode('blendColors', n = jnt[0].replace('bind','bc'))
            cmds.connectAttr(vis_ctrl + '.' + mainAttrs[1], bcNode + '.blender', f=1)
            for pair in pairs:
                cmds.setAttr(bcNode + '.color2' + pair[1], 1)
                cmds.connectAttr(br_jnt[0] + '.s' + pair[0], bcNode + '.color1' + pair[1], f=1)
                cmds.connectAttr(bcNode + '.output' + pair[1], jnt[0] + '.s'+ pair[0], f=1)
def buildBreathAttr():
    if cmds.objExists(vis_ctrl):
        mainAttrs = ['breath', 'breath_enable']
        for attr in mainAttrs:
            if not cmds.attributeQuery(attr, n = vis_ctrl, ex=1):
                cmds.addAttr(vis_ctrl, at = 'double', ln = attr, min = 0 , max = 1, dv=float(mainAttrs.index(attr)), k=1)
def makeBreath():
    buildBreathAttr()
    buildSpineBreath(spineDict)
    buildPecsBreath(pecsDict)
    buildHeadBreath(headDist)
    buildClavicleBreath(clavicleDict)
    buildShoulderBreath(shoulderDict)

