import maya.cmds as mc 
import maya.mel as mm

import os
import time
import traceback

file_extention = '.custom.ma'
deformer_type = 'customRig'

def remove_tag(nodes=None):
    if not nodes:
        nodes = mc.ls(sl=1)

    nodes= mc.ls(nodes)
    for n in nodes:
        if mc.objExists(n+'.rigBuildNode'):
            mc.deleteAttr(n+'.rigBuildNode')
            print('Removed rigBuildNode tag: '+n)

def tag_all():

    for n in mc.ls():
        if not mc.objExists(n+'.rigBuildNode'):
            try:
                mc.addAttr(n, ln='rigBuildNode', at='message')
            except:
                pass

    print 'Tagged all nodes..'


def load(file_path, **kwargs):

    tag_all()

    # import the file
    if os.path.isfile(file_path):
        mc.file(file_path, i=1, rnn=1, pmt=0, iv=1)

def save(file_path, **kwargs):
     
    # check scene 
    result = mc.confirmDialog(
                            title='Export Custom Rigs',
                            message='You are about to export any custom rigs.\nMake sure you save a working backup as it will delete this current rig.\n',
                            button=['Export', 'Cancel'],
                            icon = 'warning',
                            defaultButton='Export',
                            dismissString='Cancel')

    if result == 'Cancel':
        return

    test = check_clashing_node_names()
    if test:
        test = [t for t in mc.ls(test, l=1) if 'model_GRP' not in t]

        if test:
            mc.warning('Duplicate node names exist.. Please fix before exporting..')
            return

    # Delete junnk 
    junk = mc.ls('model_GRP', 'pRef_GRP')
    if junk:
        mc.delete(junk)

    if mc.objExists('blends'):
        mc.delete('blends')

    # Get nodes
    error = 0
    allnodes = mc.ls()
    customnodes = []
    rbnodes = []

    for n in allnodes:
        if mc.objExists(n+'.rigBuildNode'):
            rbnodes.append(n)
        else:
            customnodes.append(n)

    for n in ['initialShadingGroup', 'initialParticleSE', 'defaultLightSet', 'defaultObjectSet']:
        if n in customnodes:
            customnodes.remove(n)
        if n in rbnodes:
            rbnodes.remove(n)

    if not allnodes:
        mc.warning('No nodes in scene!')
        return

    if not rbnodes:
        mc.warning('No nodes in this scene have been tagged as rigBuildNode. Export will not work.')
        return

    if not customnodes:
        mc.warning('No custom rig nodes in scene!')
        return

    # parenting custom nodes
    arg = '\n\n# Parenting custom nodes ##################################\n'
    for node in customnodes:
        if not 'Constraint' in mc.nodeType(node):
            parent = mc.listRelatives(node, p=1)
            if parent:
                if not 'Constraint' in mc.nodeType(parent[0]):
                    if parent[0] in rbnodes:
                        arg += "try:\n\tmc.parent('{0}', '{1}')\n".format(node, parent[0])
                        arg += "except:\n\ttraceback.format_exc()\n"
                        try:
                            mc.parent(node, w=1)
                        except:
                            mc.warning('Cannot unparent: '+node)
                            error = 1

    # parenting RB nodes under custom
    arg += '\n\n# Parenting rig build nodes to custom ##################################\n'
    for node in customnodes:
        if not 'Constraint' in mc.nodeType(node):
            children = mc.listRelatives(node, c=1)
            if children:
                for ch in children:
                    if not 'Constraint' in mc.nodeType(ch):
                        if ch in rbnodes:
                            print ch
                            arg += "try:\n\tmc.parent('{0}', '{1}')\n".format(ch, node)
                            arg += "except:\n\ttraceback.format_exc()\n"
                            try:
                                mc.parent(ch, w=1)
                            except:
                                mc.warning('Cannot unparent: '+ch)
                                error = 1
    # Constraints
    arg += '\n\n# Constraints ##################################\n'
    cons = [n for n in mc.ls(customnodes) if mc.nodeType(n) in ['pointConstraint','orientcons',
                    'scaleConstraint', 'parentConstraint','aimConstraint',
                    'normalConstraint','geometryConstraint','tangentConstraint']]

    arg += get_constraint_data(cons)
    ud_arg = '\n\n# User defined attributes ##################################\n'
    sdk_arg = '\n\n# Set Driven keyframes ##################################\n'

    # sdks 
    result = get_sdk_data(cons)
    sdk_arg += result[0] or ''
    sdk_nodes = result[1] or []
    ud_arg += result[2] or ''

    mc.delete(cons, cn=1)

    # direct connections
    arg += '\n\n# Connections ##################################\n'
    customnodes = mc.ls(customnodes)
    ud_nodes = []

    for node in customnodes:
        if mc.objExists(node):
            if 'Constraint' not in mc.nodeType(node):
                if mc.listConnections(node, c=1):
                    plugs = [cn for cn in mc.listConnections(node, c=1) if node in cn]
                    for p in plugs:
                        try:
                            if mc.connectionInfo(p, ies=1):
                                dsts = [cn for cn in mc.listConnections(p, s=0, d=1, scn=1, p=1) if mc.objExists(cn.split('.')[0]+'.rigBuildNode')]
                                for dst in dsts:
                                    arg += "try:\n\tmc.connectAttr('{0}', '{1}')\n".format(p, dst)
                                    arg += "except:\n\ttraceback.format_exc()\n"
                                    mc.disconnectAttr(p, dst)
                                    ud_nodes.append(dst.split('.')[0])
                                    ud_nodes.append(p.split('.')[0])

                            elif mc.connectionInfo(p, ied=1):
                                srcs = [cn for cn in mc.listConnections(p, s=1, d=0, scn=1, p=1) if mc.objExists(cn.split('.')[0]+'.rigBuildNode')]
                                for src in srcs:
                                    arg += "try:\n\tmc.connectAttr('{0}', '{1}')\n".format(src, p)
                                    arg += "except:\n\ttraceback.format_exc()\n"
                                    mc.disconnectAttr(src, p)

                                    ud_nodes.append(src.split('.')[0])
                                    ud_nodes.append(p.split('.')[0])

                        except:
                            pass

    # build final arg string 
    ud_arg += get_uattr_data(ud_nodes)

    arg = '''# Custom rig generated code 
import maya.mel as mm 
import maya.cmds as mc
import traceback 
import os

from rigBot.data import customRig

# Tag all nodes ##################################
customRig.tag_all()

    ''' + ud_arg+arg+sdk_arg

    arg += '# Tag all nodes ##################################\n'
    arg += 'customRig.clean_scene()\n\n'


    # Delete junk
    if sdk_nodes:
        remove_tag(sdk_nodes)

    try:
        if rbnodes:
            mc.delete(mc.ls(rbnodes))
    except:
        pass

    for sa in mc.ls('*.space', '*.transSpace', '*.orientSpace') :
        mc.deleteAttr(sa)

    # Export
    customnodes = mc.ls(customnodes+sdk_nodes)

    scr = mc.scriptNode(n='customRig_SCR', stp='python', bs=arg, st=1)
    mc.addAttr(scr, ln='exportData', at='message')

    mc.select(customnodes, scr)
    result = mc.file(file_path, options='v=0', type='mayaAscii', pr=1, es=1, f=1)

    print 'Export Custom Rigs to: '+result
    return file_path

# Helper functions for getting data types
def get_constraint_data(nodes):

    arg = ""
    nodes = mc.ls(nodes)
    for node in nodes:

        targets = mc.listConnections(node+'.constraintParentInverseMatrix')
        if not targets:
            continue

        targets = list(set(targets))
        ntype = mc.nodeType(node)
        if not ntype in ['pointConstraint','orientConstraints',
                        'scaleConstraint', 'parentConstraint','aimConstraint',
                        'normalConstraint','geometryConstraint','tangentConstraint']:
                            continue

        drivers = eval('mc.{0}(node, q=1, tl=1)'.format(ntype))
        wal = eval('mc.{0}(node, q=1, wal=1)'.format(ntype))

        # aim Constraints
        arg += "try:\n"
        if ntype in ['aimConstraint', 'tangentConstraint', 'normalConstraint']:
            wut = mc.aimConstraint(node, q=1, wut=1)
            wuo = mc.aimConstraint(node, q=1, wuo=1)
            aim = mc.aimConstraint(node, q=1, aim=1)
            u = mc.aimConstraint(node, q=1, u=1)
            wu = mc.aimConstraint(node, q=1, wu=1)

            if wuo:
                wuo = ", wuo='{0}'".format(wuo[0])

            for i in range(len(drivers)):
                arg += "\tmc.{3}('{0}', {1}, n='{2}', mo=1, aim={4}, u={5}, wu={6}, wut='{7}', w={9}{8})\n".format(drivers[i],
                                                                                                                targets, node, ntype,
                                                                                                                aim, u, wu, wut, wuo,
                                                                                                                mc.getAttr(node+'.'+wal[i]))
        # all other constraints
        else:
            for i in range(len(drivers)):
                arg += "\tmc.{3}('{0}', {1}, n='{2}', mo=1, w={4})\n".format(drivers[i],
                                                                            targets, node, ntype,
                                                                            mc.getAttr(node+'.'+wal[i]))
        # interp type
        if mc.objExists(node+'.interpType'):
            interpType = mc.getAttr(node+'.interpType')
            arg += "\tmc.setAttr('{0}.interpType', {1})\n".format(node, interpType)

        arg += "except:\n\ttraceback.format_exc()\n"

    return arg

def get_sdk_data(nodes):

    # getSdks from nodes
    def get_sdks(nodes):
        curves = []
        for node in nodes:
            crvs = mc.listConnections(node,s=1, d=0, scn=1, type='animCurve')
            if crvs:
                for c in crvs:
                    curves.append((c, node))

            bws = mc.listConnections(node,s=1, d=0, scn=1, type='blendWeighted')
            if bws:
                for bw in bws:
                    cnn = mc.listConnections(bw, s=1, d=0, scn=1, type='animCurve')
                    if cnn:
                        for c in cnn:
                            curves.append((c, node))
        return list(set(curves))


    nodes = mc.ls(nodes, l=1)

    wnodes, canodes = [], []
    arg = ''

    for node in nodes:

        # get curves
        crvs = get_sdks([node])
        if not crvs:
            continue

        for c in crvs:
            c = c[0]

            # get driver
            driver = mc.listConnections(c+'.input', d=0, s=1, p=1, scn=1)
            if driver:
                driver = driver[0]

            # get driven
            driven = mc.listConnections(c+'.output', d=1, s=0, p=1, scn=1)
            if driven:
                if mc.nodeType(driven) == 'blendWeighted':
                    driven = mc.listConnections(driven[0].split('.')[0]+'.output', d=1, s=0, p=1, scn=1)
            if driven:
                driven = driven[0]

            canodes.append(driver.split('.')[0])
            canodes.append(driven.split('.')[0])

            # duplicate crv
            wnode = mc.duplicate(c, n=c+'_weights')[0]
            wnodes.append(wnode)

            # build arg
            arg += "customRig.reconnect_sdk('{0}', '{1}', '{2}')\n".format(wnode, driver, driven)

    ud_arg = get_uattr_data(list(set(canodes)))

    return arg, wnodes, ud_arg

def get_uattr_data(nodes):

    nodes = mc.ls(nodes)
    uarg = ''

    for node in nodes:

        uds = mc.listAttr(node, ud=1)
        if not uds:
            continue

        for ud in uds:
            if ud not in ['controlID', 'tagKeyable', 'tagSpaces', 'tag', 'space', 'transSpace', 'orientSpace','rigBuildNode']:

                # hand attr types
                atype = mc.addAttr(node+'.'+ud, q=1, at=1)
                if atype in ['long', 'double', 'bool', 'enum']:

                    minv = mc.addAttr(node+'.'+ud, q=1, min=1)
                    maxv = mc.addAttr(node+'.'+ud, q=1, max=1)
                    dv = mc.addAttr(node+'.'+ud, q=1, dv=1)

                    # floats and ints
                    if minv is not None and atype in ['long', 'double']:
                        minv = ', min={0}'.format(minv)
                    else:
                        minv = ''

                    if maxv is not None and atype in ['long', 'double']:
                        maxv = ', max={0}'.format(maxv)
                    else:
                        maxv = ''

                    if atype == 'enum':
                        enum = mc.addAttr(node+'.'+ud, q=1, en=1)
                        enum = ', en="{0}"'.format(enum)
                    else:
                        enum = ''

                    uarg += """
if mc.objExists("{0}") and not mc.objExists("{0}.{1}"):
    mc.addAttr("{0}", ln="{1}", at="{2}", k=1, dv={5}{3}{4}{6})

    """.format(node, ud, atype, minv, maxv, dv, enum)

    return uarg

def reconnect_sdk(weight, driver, driven):
    try:
        # Create default sdk
        for node in [weight, driver, driven]:
            if not mc.objExists(node):
                return

        # create intial SDK
        mc.setDrivenKeyframe(driven, cd=driver)

        # Find the name of that new SDK
        crvs = mc.listConnections(driven, s=1, d=0, p=0, scn=1, type='animCurve')
        bws = mc.listConnections(driven, s=1, d=0, p=0, scn=1, type='blendWeighted')

        if not crvs:
            crvs = []

        if bws:
            for bw in bws:
                cnn = mc.listConnections(bw, s=1, d=0, p=0, scn=1, type='animCurve')
                if cnn:
                    crvs.extend(cnn)
        crv = ''
        for c in crvs:
            cnn = mc.listConnections(c+'.input', d=0, s=1, scn =1, p=1)
            if cnn:
                if cnn[0] == driver:
                    crv = c

        # Finad actuall connections of that SDK
        icnn = mc.listConnections(crv+'.input', s=1, d=0, p=1, scn=1)
        ocnn = mc.listConnections(crv+'.output', s=0, d=1, p=1, scn=1)

        if icnn and ocnn:
            mc.connectAttr(icnn[0], weight+'.input', f=1)
            mc.connectAttr(weight+'.output', ocnn[0], f=1)
            print '{0} connected! {1} >> {2}'.format(weight, driver, driven)

        mc.delete(crv)
        mc.rename(weight, crv)

    except:
        print(traceback.format_exc())

def clean_scene():
    
    junk = mc.ls('*.exportData', '*:*.exportData')
    if junk:
        mc.delete(junk)


def check_clashing_node_names():

    nodes = [n for n in mc.ls(sn=1) if '|' in n ]
    if nodes:
        return nodes

 