import maya.cmds as mc

def create(driver, driven):
    """Create jiggle point nodes on specifed node. Requires a driving target node.

        Note:
            Nodes must be either joints or transforms. This is not a deformer.

        Args:
            :driver: (str) Node to drive the jiggle target position.
            :driven: (str) Node to be jiggled"""

    if not mc.pluginInfo('cmJigglePoint', q=1, l=1):
        mc.warning('cmJigglePoint plugin is not loaded! Cannot continue.')
        return

    time = mc.ls(type='time')
    jiggle = mc.createNode('cmJigglePoint')
    dmx = mc.createNode('decomposeMatrix')

    mc.connectAttr(time[0]+'.outTime', jiggle+'.time')
    mc.connectAttr(driver+'.worldMatrix', dmx+'.inputMatrix')
    mc.connectAttr(dmx+'.outputTranslate', jiggle+'.goal')
    mc.connectAttr(driven+'.parentInverseMatrix', jiggle+'.parentInverse', f=1)
    mc.connectAttr(jiggle+'.output', driven+'.t', f=1)

    mc.select(driven)

    return jiggle

def create_jiggle_ctrls(name, ctrls, master_ctrl='dynamic_CTL'):
    """Create jiggle point nodes on all _OFF nodes above ctrl. Also places a
        master attribute on the specifed master ctrl.

            Args:
                :name: (str) Name for the master attribute.
                :ctrls: (list) List of controls to add jiggle.
                :master_ctrl: (str) Master ctrl for master attr (Defaults to "dynamic_CTL")"""

    if not mc.pluginInfo('cmJigglePoint', q=1, l=1):
        mc.warning('cmJigglePoint plugin is not loaded! Cannot continue.')
        return

    if not mc.objExists(master_ctrl+'.'+name):
        mc.addAttr(master_ctrl, ln=name, min=0, max=1, dv=0, k=1)

    for i, ctrl in enumerate(ctrls):

        jiggle_node = create(ctrl+'_MOCAP', ctrl+'_OFF')

        mc.addAttr(ctrl, ln='jiggle', k=1, min=0, dv=1)
        mc.addAttr(ctrl, ln='jiggleX', k=1, min=0, max=1, dv=1)
        mc.addAttr(ctrl, ln='jiggleY', k=1, min=0, max=1, dv=1)
        mc.addAttr(ctrl, ln='jiggleZ', k=1, min=0, max=1, dv=1)
        mc.addAttr(ctrl, ln='stiffness', k=1, min=0, max=1, dv=.2)
        mc.addAttr(ctrl, ln='damping', k=1, min=0, max=1, dv=.1)

        mc.connectAttr(master_ctrl+'.'+name, jiggle_node+'.envelope')
        mc.connectAttr(ctrl+'.jiggle', jiggle_node+'.jiggle')
        mc.connectAttr(ctrl+'.jiggleX', jiggle_node+'.jiggleX')
        mc.connectAttr(ctrl+'.jiggleY', jiggle_node+'.jiggleY')
        mc.connectAttr(ctrl+'.jiggleZ', jiggle_node+'.jiggleZ')
        mc.connectAttr(ctrl+'.stiffness', jiggle_node+'.stiffness')
        mc.connectAttr(ctrl+'.damping', jiggle_node+'.damping')

