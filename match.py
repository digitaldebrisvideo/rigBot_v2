import maya.cmds as mc

def match(nodes=[], position=True, orientation=True, pivot=False):
    """Simple utility for matching xforms from one driver to other nodes.
        Kwargs:
            :nodes: (list) Nodes to snap.. Select driver first then nodes to match.
            :position: (bool) Match position.
            :orientation: (bool) Match orientation.
            :pivot: (bool) Match pivots."""

    if not nodes:
        nodes = mc.ls(sl=1)

    nodes = mc.ls(nodes)

    if not len(nodes) > 1:
        raise ValueError('Need at least two nodes selected.. Driver, then driven.')

    master = nodes[0]
    masterPiv = mc.xform(master, q=1,rp=1,ws=1)

    for node in nodes[1:]:

        if position or orientation:
            proxyObj = mc.duplicate(node, po=1)[0]

            for a in ['tx','ty','tz','rx','ry','rz']:
                mc.setAttr(proxyObj+'.'+a, l=0, k=1)

            mc.delete(mc.pointConstraint(master, proxyObj))
            mc.delete(mc.orientConstraint(master, proxyObj))

            if position:
                x = mc.xform(proxyObj, q=1, a=1, t=1)
                mc.xform(node, a=1, t=x)

            if orientation:
                x = mc.xform(proxyObj, q=1, a=1, ro=1)
                mc.xform(node, a=1,  ro=x)

            if pivot:
                mc.xform(node, ws=True, piv=masterPiv)

            mc.delete(proxyObj)
    mc.select(nodes[1:])

def switch_spaces(nodes=None, space_idx=0, space_attr='space', set_key=False):
    """Anim utility for switching spaces via right clikc dag menu"""

    current_sel = mc.ls(sl=1)

    if not nodes:
        nodes = mc.ls(sl=1)

    nodes = [n for n in mc.ls(nodes) if mc.objExists(n+'.'+space_attr)]

    for node in nodes:

        tmp = mc.createNode('transform')
        match([node, tmp])

        if set_key:
            mc.setKeyframe(node+'.'+space_attr, t=mc.currentTime(q=1)-1)
            mc.setKeyframe(node+'.t', t=mc.currentTime(q=1)-1)
            mc.setKeyframe(node+'.r', t=mc.currentTime(q=1)-1)

        mc.setAttr(node+'.'+space_attr, space_idx)
        match([tmp, node])
        mc.delete(tmp)

        if set_key:
            mc.setKeyframe(node+'.'+space_attr)
            mc.setKeyframe(node+'.t')
            mc.setKeyframe(node+'.r')

    mc.select(current_sel)
