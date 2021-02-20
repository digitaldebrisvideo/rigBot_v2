import maya.cmds as cmds
import maya.cmds as mc
import maya.mel as mm
import sys


from rigBot import control
from rigBot import utils
from rigBot import utils




def makeRibbon(sel=None, name='xxx', numJnts=5, conn=True , side=None,  *args):
    """creates and connects default ribbon rig and controls between two selected or specified nodes


    Keyword Arguments:
        nodes {[type]} -- [specify exactly two[2] existing and valid start and end objects, uses scene selection if nothing is passed] (default: {})
        name {str} -- [name and naming for entire ribbon system] (default: {'xxx'})
        numJnts {int} -- [number of bind joints to create on last ribbon layer, ctrls for each joint will also be created] (default: {5})
        conn {bool} -- [parentConstrains the start and end ctrl grp nodes to start and end nodes ] (default: {True})

    Returns:
        [rigNode, bindJoints] -- [parent rig node,  bind joints driven by ribbon system]
    """

    if side is None:
        side=''


    if sel is None:
        sel = cmds.ls(sl=1)

    nameRibbon = name

    nameSet =['start', 'mid', 'end']

    controlJoints = []
    bindJoints = []
    rigNode = nameRibbon + '_rig'
    ctrlNode = nameRibbon + '_ctrls_grp'
    jntsNode = nameRibbon + '_jnts_grp'
    noxformNode = nameRibbon + '_noxform'
    nrbSrc = cmds.nurbsPlane( ch = 1, o = 1, po= 0, ax= (0, 0,1), w = 10, lr= 0.1, n = nameRibbon + '_src_nrb', d=1)
    nrbSrcShape = cmds.listRelatives(nrbSrc, s=1)
    nrbJnt = cmds.nurbsPlane(ch = 1, o = 1, po= 0, ax= (0, 0,1), w = 10, lr= 0.1, n = nameRibbon + '_inf_nrb', d=2)
    nrbJntShape = cmds.listRelatives(nrbJnt, s=1)
    mkNrb = cmds.ls(cmds.listHistory(nrbSrc, lv=1), type  = 'makeNurbPlane')[0]
    cmds.setAttr(mkNrb + '.axisY', 1)
    cmds.setAttr(mkNrb + '.axisZ', 0)
    mkNrbJnt = cmds.ls(cmds.listHistory(nrbJnt, lv=1), type  = 'makeNurbPlane')[0]
    cmds.setAttr(mkNrbJnt + '.axisY', 1)
    cmds.setAttr(mkNrbJnt + '.axisZ', 0)
    fol_grp=name+'_follicleGroup'
    if cmds.objExists(fol_grp) == 0:
        cmds.createNode('transform', n = fol_grp)
    if not cmds.objExists(rigNode):
        cmds.createNode('transform', n = rigNode)
    if not cmds.objExists(ctrlNode):
        cmds.createNode('transform', n = ctrlNode)
        cmds.parent(ctrlNode, rigNode, a=1)
    if not cmds.objExists(jntsNode):
        cmds.createNode('transform', n = jntsNode)
        cmds.parent(jntsNode, rigNode, a=1)
    if not cmds.objExists(noxformNode):
        cmds.createNode('transform', n = noxformNode)
        cmds.parent(noxformNode, rigNode, a=1)
    cmds.parent(nrbSrc[0], nrbJnt[0], noxformNode, a=1)
    #build control jnts
    for i in range(0, 3):
        cmds.select(cl=1)
        jntCtrl = cmds.joint( n = nameRibbon + '_' +  nameSet[i] + '_jnt', o= (0,0,0))
        controlJoints.append(jntCtrl)
        if jntCtrl in (nameRibbon  + '_mid_jnt'):
            folMid = cmds.createNode('follicle', n= jntCtrl.replace('jnt','fol'))
            folMid_top = cmds.listRelatives(folMid, p=1)
            folMid_top = cmds.rename(folMid_top, jntCtrl.replace('jnt','fol_tr'))
            cmds.setAttr((folMid + '.parameterU'), 0.5)
            cmds.setAttr((folMid + '.parameterV'), 0.5)
            cmds.connectAttr(nrbSrcShape[0] + '.worldSpace', (folMid + '.inputSurface'))
            cmds.connectAttr(nrbSrcShape[0] + '.worldMatrix', (folMid + '.inputWorldMatrix'))
            cmds.connectAttr((folMid + '.outTranslate'), (folMid_top + '.translate'))
            cmds.connectAttr((folMid + '.outRotate'), (folMid_top + '.rotate'))
            snapCtrl = cmds.parentConstraint(folMid_top, jntCtrl, mo=1)
            cmds.parent(folMid, fol_grp)
            cmds.delete(snapCtrl)
        cmds.parent(jntCtrl, jntsNode)
    # build bind joints

    folys=[]
    for i in range(0, numJnts):
        cmds.select(cl=1)
        jnt = cmds.joint( n = name + '_' + str(i) + '_jnt', o= (0,0,0))
        bindJoints.append(jnt)
        mc.select (cl=1)
        foly = cmds.createNode('follicle', n= name + '_' + str(i) + '_fol')
        print foly
        fol_top = [utils.get_parent(foly)]
        cmds.connectAttr(nrbJntShape[0] + '.worldSpace', (foly + '.inputSurface'))
        cmds.connectAttr(nrbJntShape[0] + '.worldMatrix', (foly + '.inputWorldMatrix'))
        cmds.connectAttr((foly + '.outTranslate'), (fol_top[0] + '.translate'))
        cmds.connectAttr((foly + '.outRotate'), (fol_top[0] + '.rotate'))

        cmds.setAttr((foly + '.parameterU'), 1.0/float(numJnts-1)*i)

        # if i==0:
        #     mc.setAttr (foly+ '.parameterU', .01)
        # elif i==numJnts-1:
        #     mc.setAttr (foly+ '.parameterU', .09)

        cmds.setAttr((foly + '.parameterV'), 0.5)
        cmds.parent(fol_top, fol_grp, s=1)
        snap = cmds.pointConstraint(fol_top, jnt, mo=0)
        cmds.delete(snap)
        cmds.parent(jnt, jntsNode, a=1)
        fol_top = cmds.rename(fol_top, jnt.replace('jnt','fol_tr'))
        folys.append (foly)

    mc.setAttr (folys[0]+'.parameterU' , .075)
    mc.setAttr (folys[-1]+'.parameterU', .975)

    #snap jonts
    snapStart = cmds.parentConstraint(bindJoints[0], controlJoints[0], mo=0)
    snapEnd = cmds.parentConstraint(bindJoints[-1], controlJoints[2], mo=0)
    cmds.delete(snapStart, snapEnd)
    shaperctrls=[]
    #build controls for bindJoints
    for bindJnt in bindJoints:
        ctrl = cmds.circle(ch=1, d=1, s=4, r = 4, nr = (1,0,0), n = bindJnt.replace('jnt', 'ctrl'))
        grp = cmds.group(ctrl[0], n = ctrl[0] + 'Grp')
        grpOffset = cmds.group(grp, n = grp + 'Offset')
        sn = cmds.parentConstraint(bindJnt, grpOffset, mo=0)
        cmds.delete(sn)
        cmds.parent(grpOffset, ctrlNode, a=1)
        cmds.parentConstraint(ctrl, bindJnt, mo=0)
        cmds.parentConstraint(ctrl[0].replace('ctrl', 'fol_tr'), grpOffset, mo=1)
        control.create_shape (shape='pin_circle', ctrls=ctrl[0], scale=[10,10,10], axis='-z')
        control.set_color(color='red', ctrls=ctrl[0])
        shaperctrls.append (ctrl[0])

    #build controls for Control Joints
    ctrls=[]
    ctrlGrps = []
    ctrlGrpOff = []
    for ctrlJnt in controlJoints:
        ctrl = cmds.circle(ch=1, d=1, s=6, r=6, nr = (1,0,0), n = ctrlJnt.replace('jnt', 'ctrl'))
        ctrls.append(ctrl[0])
        grp = cmds.group(ctrl[0], n = ctrl[0] + 'Grp')
        ctrlGrps.append(grp)
        grpOffset = cmds.group(grp, n = grp + 'Offset')
        ctrlGrpOff.append(grpOffset)
        sn = cmds.parentConstraint(ctrlJnt, grpOffset, mo=0)
        cmds.delete(sn)
        cmds.parent(grpOffset, ctrlNode, a=1)
        cmds.parentConstraint(ctrl, ctrlJnt, mo=0)
        if ctrlJnt in (nameRibbon  + '_mid_jnt'):
            cmds.parentConstraint(ctrlJnt.replace('jnt', 'fol_tr'), grpOffset, mo=1)
            cmds.parentConstraint(ctrl[0].replace('ctrl', 'fol_tr'), grpOffset, mo=1)
        cmds.parentConstraint(ctrl, ctrlJnt, mo=0)
        control.create_shape (shape='arrow_quad', ctrls=ctrl[0], scale=[2,2,2])
        control.set_color (color='yellow', ctrls=ctrl[0])
    #bind skin to nurbs
    cmds.skinCluster(controlJoints, nrbJnt, tsb=1)
    cmds.skinCluster(controlJoints[0], controlJoints[2], nrbSrc, tsb=1)
    #snap rig to selection
    snStart = cmds.parentConstraint(sel[0], ctrlGrpOff[0], mo=0)
    snEnd = cmds.parentConstraint(sel[1], ctrlGrpOff[2], mo=0)
    cmds.delete(snStart, snEnd)
    if conn:
        cmds.parentConstraint(sel[0], ctrlGrpOff[0], mo=1)
        cmds.parentConstraint(sel[1], ctrlGrpOff[2], mo=1)


    return (bindJoints, ctrlGrps ,rigNode, shaperctrls, ctrls)



def make_distributed_twist(nodes=None, name='xxx', twistPar=None, numJnts=5, *args):
    """[Quaterion / matrix based twist for lower arms and legs]
        twist par is the same as the end node unless specified]
        assumes x axis is down joint and y is up

    Arguments:
        name {string} -- [what to name the system, ie. 'uprArmTwist']

    Keyword Arguments:
        nodes [] -- [start and end jonts, if nothing specified it tried to use selected] (default: [selected])
        twistPar {node} -- [node creating the twist between two jonts.  if none passed, the last node is used]
        numJnts {int} -- [number of twist anim ctrls and bindjnts to create] (default: {5})


    """


# Quaterion / matrix based twist for upper arms and leg
    if nodes is None:
        nodes=mc.ls (sl=1)
        if not nodes:
            return ('Select start and end (2) nodes')

    if len(nodes) >> 2:
        return ('Select or Specify start and end(2) nodes only')

    driverStart=nodes[0]
    driverEnd=nodes[1]

    name=name
    if mc.objExists (name+'_rig'):
        print (name+'_rig exists...finding unique name')
        name=utils.unique (name=name+'_rig')

    if twistPar is None:
        twistPar = driverEnd


    hinodes=[]
    nodes=[driverStart, driverEnd]
    allribbons=makeRibbon(sel=nodes, name=name, numJnts=numJnts, conn=True)

    bindjnts=allribbons[0]
    ctrlGrps=allribbons[1]
    rigNode=allribbons[2]
    bendyctrls=allribbons[4]
    shaperctrls=allribbons[3]



    if twistPar is not driverEnd:
        print ('twistPar is different node than driver')
    startctrl=name+'_start_ctrlGrp'
    if mc.objExists (startctrl):

        startOff=name+'_start_ctrlGrpOffset'
        if mc.objExists (startOff):
            cons=mc.listRelatives(startOff, c=1, type='constraint')
            if cons:
                mc.delete (cons)
            mc.pointConstraint (driverStart, startctrl, mo=0 )
            mc.orientConstraint (twistPar, startctrl, mo=0 )


    # Create a group that does not rotate and parent under the driverStart (elbow)
    stable_reader_grp = utils.create_node('transform', n=driverStart+'_stable_reader', p=driverStart)

    # Create a grp that will rotate with drivers
    twist_reader_grp = utils.create_node('transform', n=driverStart+'_twist_reader', p=driverStart)
    mc.addAttr(twist_reader_grp, ln='twist', k=1)

    mc.delete(mc.pointConstraint(driverEnd, twist_reader_grp))
    mc.parent(twist_reader_grp, twistPar)

    # Now set up mult matrix and decomp nodes to extract the twist between the two nodes
    mult_mtx = mc.createNode('multMatrix')
    decomp_mtx = mc.createNode('decomposeMatrix')
    quat_to_euler = mc.createNode('quatToEuler')

    mc.connectAttr(stable_reader_grp+'.worldInverseMatrix', mult_mtx+'.matrixIn[1]')
    mc.connectAttr(twist_reader_grp+'.worldMatrix', mult_mtx+'.matrixIn[0]')
    mc.connectAttr(mult_mtx+'.matrixSum', decomp_mtx+'.inputMatrix')
    mc.connectAttr(decomp_mtx+'.outputQuatX', quat_to_euler+'.inputQuatX')
    mc.connectAttr(decomp_mtx+'.outputQuatW', quat_to_euler+'.inputQuatW')

    utils.connect_negative(quat_to_euler+'.outputRotateX', twist_reader_grp+'.twist')



    div = 1 / (len(bindjnts))

    mdl = mc.createNode('multDoubleLinear')
    mc.setAttr(mdl+'.input1', div)
    mc.connectAttr(quat_to_euler+'.outputRotateX', mdl+'.input2')

    for i, joint in enumerate(bindjnts):
        grp=joint.replace ('_jnt', '_ctrlGrp')
        ctrl=joint.replace ('_ctrlGrp', '_ctrl')
        faded=mc.createNode('plusMinusAverage', name=grp+'_pma')
        mc.setAttr (faded+'.input1D[0]', (div*10)*i )
        mc.connectAttr (mdl+'.output', faded+'.input1D[1]' )
        mc.connectAttr (faded+'.output1D', grp+'.rx')




    shapers=[]
    for shaperctrl in shaperctrls:
        anim=shaperctrl.replace ('_ctrl', '_anim')
        mc.rename (shaperctrl, anim)
        shapers.append (anim)
        # mc.parent (anim.replace ('_anim', '_ctrlGrpOffset'), name+'_ctrls_grp')

    noshpr=[shapers[0].replace ('anim', 'ctrlGrpOffset'), shapers[-1].replace ('anim', 'ctrlGrpOffset')]
    # mc.delete (noshpr)
    # shapers.remove (shapers[0])
    # shapers.remove (shapers[-1])
    print shapers

    nojnts=[bindjnts[0], bindjnts[-1]]
    # mc.delete (nojnts)
    # bindjnts.remove (bindjnts[0])
    # bindjnts.remove (bindjnts[-1])
    print bindjnts

    # mc.delete (noshpr, nojnts)

    return (bindjnts, shapers, bendyctrls )


def create_twist_shaper_joints(joints=None, name='upArm', mirror=1, size=2):
    color='dark_magenta'

    shaper_ctrls=[]
    shaper_bindjnts=[]
    shaper_ctrls_set=[]
    for i in range (0, len(joints)):
        mc.select (joints[i])
        n=i+1
        fullname=name+'Ribbon0'+str(n)+'_CTL'
        dvr = name + '_shaper_0' + str(n) + '_CTL'
        if not mc.objExists (dvr):
            dvr=None
        bndjnt=mc.joint (name=fullname+'_JNT')
        shaper_ctrl=control.create(name=fullname,shape='pin_shaper',color=color, axis='Y', node_type='joint', scale=[size,(mirror*size),size], match_position=bndjnt, match_shape=dvr )

        mc.select (cl=1)
        mc.parentConstraint (joints[i], shaper_ctrl[0], mo=0)
        mc.scaleConstraint (joints[i], shaper_ctrl[0], mo=0)
        mc.parentConstraint (shaper_ctrl[-1], bndjnt, mo=0)
        shaper_ctrls.append (shaper_ctrl[0])
        shaper_bindjnts.append (bndjnt)
        shaper_ctrls_set.append (shaper_ctrl[-1])

    return (shaper_ctrls, shaper_bindjnts, shaper_ctrls_set )


# def drive_shaper_joints(ctrls, name='upArm'):
#     color='dark_magenta'
#
#     shaper_ctrls=[]
#     shaper_bindjnts=[]
#     shaper_ctrls_set=[]
#     for i in range (0, len(joints)):
#         mc.select (joints[i])
#         n=i+1
#         fullname=name+'Ribbon0'+str(n)+'_CTL'
#         dvr = name + '_shaper_0' + str(n) + '_CTL'
#         if not mc.objExists (dvr):
#             dvr=None
#         bndjnt=mc.joint (name=fullname+'_JNT')
#         shaper_ctrl=control.create(name=fullname,shape='pin_shaper',color=color, axis='Y', node_type='joint', scale=[size,(mirror*size),size], match_position=bndjnt, match_shape=dvr )
#
#         mc.select (cl=1)
#         mc.parentConstraint (joints[i], shaper_ctrl[0], mo=0)
#         mc.scaleConstraint (joints[i], shaper_ctrl[0], mo=0)
#         mc.parentConstraint (shaper_ctrl[-1], bndjnt, mo=0)
#         shaper_ctrls.append (shaper_ctrl[0])
#         shaper_bindjnts.append (bndjnt)
#         shaper_ctrls_set.append (shaper_ctrl[-1])
#
#     return (shaper_ctrls, shaper_bindjnts, shaper_ctrls_set )