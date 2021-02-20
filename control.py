import maya.cmds as mc
import maya.mel as mm

import os
import re
import json

from rigBot import utils

shapes, colors, protected_entries = [], [], []
json_data = shape_data, color_data = {}, {}
system_base_path = os.path.dirname(utils.__file__)

def reload_control_data(verbose=False):
    """Reload contro and shape data from env"""

    global shapes
    global colors
    global json_data
    global shape_data
    global color_data
    global protected_entries

    system_base_path = os.path.dirname(utils.__file__)
    base_path = os.path.join(system_base_path, 'config')
    file_path = os.path.join(base_path, 'controlData.json')

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            json_data = json.load(f)
            if verbose:
                print 'Loaded controlData: '+file_path

    shape_data = json_data.get('shapes')
    color_data = json_data.get('colors')
    protected_entries = json_data.get('protectedEntries')

    shapes = utils.convert_to_unicode(shape_data.keys())
    colors = utils.convert_to_unicode(color_data.keys())
    protected_entries = utils.convert_to_unicode(protected_entries)

    shapes.sort()
    colors.sort()

def get_crv_point(shape):
    """Get worldspace point postions from curve shape."""

    points = []
    cvs = mc.ls('{0}.cv[:]'.format(shape), l=True, fl=True)

    for c in cvs:
        x = mc.xform(c, q=True, ws=True, t=True)
        x = [round(t, 6) for t in x]
        points.append(x)

    return points

def set_crv_points(shape, points):
    """Set curve points in worldspace"""

    cvs = mc.ls('{0}.cv[:]'.format(shape), l=True, fl=True)
    for i, cv in enumerate(cvs):
        mc.xform(cv, ws=1, t=points[i])

def set_rotate_order(nodes=[], rotate_order='XYZ'):
    """Set rotate_order for nodes, can specify string or int.or

        'XYZ' = 0
        'YZX' = 1
        'ZXY' = 2
        'XZY' = 3
        'YXZ' = 4
        'ZYX' = 5"""

    if not nodes:
        nodes = mc.ls(sl=1)
    nodes = mc.ls(nodes)

    if not type(rotate_order) is int:
        if rotate_order.upper() == 'XYZ':
            rotate_order = 0
        elif rotate_order.upper() == 'YZX':
            rotate_order = 1
        elif rotate_order.upper() == 'ZXY':
            rotate_order = 2
        elif rotate_order.upper() == 'XZY':
            rotate_order = 3
        elif rotate_order.upper() == 'YXZ':
            rotate_order = 4
        elif rotate_order.upper() == 'ZYX':
            rotate_order = 5

    nodes = mc.ls(nodes)
    for node in nodes:
        mc.setAttr(node+'.rotateOrder', rotate_order)

    return rotate_order

def set_historical_importance(node):
    """Sets exxtra shape nodes to not have ihi"""

    shape_nodes = utils.get_shapes(node)
    if shape_nodes:
        mc.setAttr(shape_nodes[0]+'.ihi', 1)
        if len(shape_nodes) > 1:
            for s in shape_nodes[1:]:
                mc.setAttr(s+'.ihi', 0)

def create(name='', shape='square', color='lavendar', axis='Y', node_type='transform',
           scale=[1,1,1], match_position=None, match_shape=None, match_color=True):
    """Create control hierarchy

        KWARGS:
            :name: ctrl name (NOTE: suffix will automatically be appended based on settings)
            :shape: shape of ctrl
            :color: color of ctrl
            :axis: directions or ctrl shape
            :node_type: ctrl node type (transform or joint)
            :match_position: initial snap trans and rotoate
            :match_shape: copy shape from source curve
            :unlock_attrs: IF set initial lock an hide will be set on all other attrs"""

    # get shape and color
    if color is not None:
        color = color.lower()

    if shape is not None:
        shape = shape.lower()

    if not name:
        name = shape
        if shape is None:
            name = 'myCtrl'

    # check shape and color values
    if shape is not None and shape not in shapes:
        mc.warning( 'Shape is not valid!')
        for s in shapes:
            print s
        return

    if color is not None and color not in colors:
        mc.warning( 'Color is not valid!')
        for c in colors:
            print c
        return

    # Build unique names
    if name.endswith('_CTL'):
        if mc.objExists(name):
            mc.warning(name+' already exists! Using a unique name.')

        ctrl = utils.get_unique_name(name.replace('_CTL','')+'_#_CTL')

    else:
        if mc.objExists(name+'_CTL'):
            mc.warning('Control already exists! Using a unique name.')

        ctrl = utils.get_unique_name(name+'_#_CTL')

    zero = ctrl+'_ZERO'
    con = ctrl+'_CONST'
    mocap = ctrl+'_MOCAP'
    off = ctrl+'_OFF'

    # Create nodes
    zero = mc.createNode('transform', n=zero)
    con = mc.createNode('transform', n=con, p=zero)
    mocap = mc.createNode('transform', n=mocap, p=con)
    off = mc.createNode('transform', n=off, p=mocap)
    ctrl = mc.createNode(node_type, n=ctrl, p=off)

    if node_type == 'joint':
        mc.setAttr(ctrl+'.drawStyle', 2)
        mc.setAttr(ctrl+'.radius', cb=0)

    mc.setAttr(ctrl+'.v', l=1, k=0)

    # Create shapes and set colors
    if match_shape and mc.objExists(match_shape):
        copy_shape(match_shape, ctrl)

        if match_color:
            copy_color(match_shape, ctrl)

    else:
        create_shape(shape, ctrl, axis, scale=scale)
        set_color(color, ctrl)

    if match_position and mc.objExists(match_position):
        mc.delete(mc.parentConstraint(match_position, zero))

    mc.addAttr(zero, ln='animZeroGrp', at='message')
    mc.addAttr(con, ln='animConstGrp', at='message')
    mc.addAttr(mocap, ln='animMocapGrp', at='message')
    mc.addAttr(off, ln='animOffsetGrp', at='message')
    mc.addAttr(ctrl, ln='animControl', at='message')

    mc.select(ctrl)

    return zero, con, mocap, off, ctrl

def create_shape(shape='square', ctrls=[], axis='Y', add=False, translate=[0,0,0], rotate=[0,0,0], scale=[1,1,1], data=[]):
    """Create a curve or nurbs shape and parent to ctrl."""

    all_returns = []

    if shape is None:
        return

    ctrls = mc.ls(ctrls)
    if not ctrls:
        ctrls = mc.ls(sl=1)

    if not ctrls:
        mc.warning('No controls selected.')
        return

    if data:
        shape_info = data

    else:
        shape = shape.lower()
        shape_info = shape_data.get(shape)

        if shape not in shapes or not shape_info:
            mc.warning( 'Shape is not valid!')
            for s in shapes:
                print s
            return

    for ctrl in ctrls:

        # delete current shape
        current_shapes = [s for s in utils.get_shapes(ctrl)]

        if current_shapes and not add:

            for c in current_shapes:
                if not mc.objExists(c+'.drivenShape'):
                    mc.delete(c)

        # create shapes
        new_shapes = []
        for info in shape_info:
            points = info.get('points')
            degree = info.get('degree')
            form = info.get('form', 0)
            shape_name = info.get('shapeName')

            crv = mc.curve(d=degree, p=points)
            if form > 0:
                mc.closeCurve(crv, ch=0, ps=0, rpo=1, bb=0.5, bki=0, p=0.1)[0]

            result = mc.parent(utils.get_shapes(crv), ctrl, s=1, r=1)[0]
            if result and shape_name:
                result = mc.rename(result, shape_name)
            else:
                result = mc.rename(result, ctrl+'Shape')

            new_shapes.append(result)
            mc.delete(crv)

            all_returns = new_shapes

        # resize shape
        cvs = [s+'.cv[*]' for s in new_shapes if not mc.listConnections(s+'.controlPoints', s=1, d=0, p=1)]

        axis = axis.upper()
        if axis == '-Y':
            mc.xform(cvs, r=1, ro=[0,0,180])
        elif axis == 'X':
            mc.xform(cvs, r=1, ro=[0,0,-90])
        elif axis == '-X':
            mc.xform(cvs, r=1, ro=[0,0,90])
        elif axis == 'Z':
            mc.xform(cvs, r=1, ro=[90,0,0])
        elif axis == '-Z':
            mc.xform(cvs, r=1, ro=[-90,0,0])

        mc.xform(cvs, r=1, t=translate)
        mc.xform(cvs, r=1, ro=rotate)
        mc.xform(cvs, r=1, s=scale)

        set_historical_importance(ctrl)

    mc.select(ctrls)

    return all_returns

def set_color(color=None, ctrls=[], data=None):

    """Set color specified ctrls."""

    ctrls = mc.ls(ctrls)
    if not ctrls:
        ctrls = mc.ls(sl=1)

    if not ctrls:
        mc.warning('No nodes selected.')
        return

    # turn off display override if set to none
    if color is None:
        for ctrl in ctrls:
            try:
                mc.setAttr(ctrl+'.overrideEnabled', 0)
                mc.setAttr(ctrl+'.overrideColor', 0)
                mc.setAttr(ctrl+'.overrideColorRGB', 0,0,0)
            except:
                pass
        return

    if data and type(data) is list:
        rgb_color_value = data
        color_value = 0
    elif data and type(data) is int:
        color_value = data
        rgb_color_value = None

    else:
        rgb_color_value = None
        color_value = 0

        if type(color) is list:
            rgb_color_value = color
            color_value = 0

        elif type(color) is int:
            rgb_color_value = None
            color_value = color

        elif color in colors:
            color_value = color_data.get(color)
            if type(color_value) is list:
                rgb_color_value = color_value
                color_value = 0
        else:
            mc.warning('Color is invalid!')
            return

    # loop through controls and set colors
    for ctrl in ctrls:

        # set overrides
        rgb_mode = False
        if rgb_color_value is not None:
            rgb_mode = True

        try:
            mc.setAttr(ctrl+'.overrideEnabled', 1)
            mc.setAttr(ctrl+'.overrideRGBColors', rgb_mode)

            if rgb_mode:
                mc.setAttr(ctrl+'.overrideColor', 0)
                mc.setAttr(ctrl+'.overrideColorRGB', rgb_color_value[0],
                                                      rgb_color_value[1],
                                                      rgb_color_value[2])
            else:
                mc.setAttr(ctrl+'.overrideColor', color_value)
                mc.setAttr(ctrl+'.overrideColorRGB', 0,0,0)
        except:
            pass

def create_offset_ctrls(ctrl=None, num_offsets=1, vis_attr=None, match_shape=[]):
    """Create offsetr ctrls which are parented underthe specifed ctrl.

    ARGS:
        ctrl = ctrla to add offsets.
        num_offsets = number of offset ctrls (default = 1)
        vis_attr = an attribute to drive visibility (default is an attr ON the actual ctrl)
    """

    if num_offsets < 1:
        return

    if not ctrl:
        ctrl = mc.ls(sl=1)
        if ctrl:
            ctrl = ctrl[0]
    if not ctrl:
        mc.warning('Select or specify a ctrl!')
        return

    # get suffixes and base name for ctrl
    offset_suffix = '_OFF_CTL'
    ctrl_suffix = 'CTL'

    base_name = ctrl.replace('_'+ctrl_suffix, '')

    # create ctrla
    offset_ctrls = []

    for i in range(num_offsets):
        letter = utils.letters[i]
        off_ctrl_name = utils.join_strings([base_name, letter, offset_suffix])
        off_ctrl = mc.duplicate(ctrl, n=off_ctrl_name)[0]

        # delete any custom attrs
        attrs = mc.listAttr(off_ctrl, ud=1)
        if attrs:
            if 'animControl' in attrs:
                attrs.remove('animControl')
            for attr in attrs:
                mc.deleteAttr(off_ctrl+'.'+attr)

        # delete children
        children = utils.get_children(off_ctrl)
        if children:
            mc.delete(children)

        offset_ctrls.append(off_ctrl)

        # scale ctrl shapes
        factor = 1.0 - (0.1 * (i+1))
        ctrl_shapes = [s+'.cv[*]' for s in utils.get_shapes(off_ctrl)]
        mc.xform(ctrl_shapes, r=1, s=[factor]*3)

    # create custom vis attr
    use_custom_vis_attr = False
    if vis_attr and '.' in vis_attr:
        split = vis_attr.split('.')
        if len(split) == 2:
            vis_node, vist_attr_name = vis_attr.split('.')

        if mc.objExists(vis_node) and not mc.objExists(vis_node+'.'+vist_attr_name):
            try:
                mc.addAttr(vis_node, ln=vist_attr_name, at='bool', k=1, dv=1)
                if mc.objExists(vis_attr):
                    use_custom_vis_attr = True
            except:
                pass

    # otherwise use default vis attr on ctrl
    if not use_custom_vis_attr:
        if not mc.objExists(ctrl+'.offsetCtrlVis'):
            mc.addAttr(ctrl, ln='offsetCtrlVis', at='bool', k=1, dv=1)
        vis_attr = ctrl+'.offsetCtrlVis'

    # connect vis and parent ctrls
    for i, off_ctrl in enumerate(offset_ctrls):
        if i == 0:
            mc.parent(off_ctrl, ctrl)
        else:
            mc.parent(off_ctrl, offset_ctrls[i-1])

    utils.set_attrs(offset_ctrls, 'v', l=1, k=0)

    # copy shapes from source controls
    if type(match_shape) is list and len(match_shape) == len(offset_ctrls):
        for i in range(len(match_shape)):
            copy_shape(match_shape[i], offset_ctrls[i])

    for i, off_ctrl in enumerate(offset_ctrls):
        off_shapes = utils.get_shapes(off_ctrl)
        for shape in off_shapes:
            utils.set_attrs(shape, 'v', l=0)
            mc.connectAttr(vis_attr, shape+'.v')

    mc.addAttr(offset_ctrls, ln='animOffsetControl', at='message')
    return offset_ctrls

def copy_color(source='', target='', setTransform=False):
    """Copy colros from one node to another."""

    if not source or not target:
        sel = mc.ls(sl=1)
        if not len(sel) == 2:
            mc.warning('Select or input two nodes: source, target.')
            return
        source = sel[0]
        target = sel[1]

    if not mc.objExists(source) or not mc.objExists(target):
        return

    oe = mc.getAttr(source+'.overrideEnabled')
    oc = mc.getAttr(source+'.overrideColor')
    o_rgb_c = mc.getAttr(source+'.overrideRGBColors')
    o_rgb = mc.getAttr(source+'.overrideColorRGB')[0]

    mc.setAttr(target+'.overrideEnabled', oe)
    mc.setAttr(target+'.overrideColor', oc)
    mc.setAttr(target+'.overrideRGBColors', o_rgb_c)
    mc.setAttr(target+'.overrideColorRGB', o_rgb[0], o_rgb[1], o_rgb[2])

def mirror_shape(source='', target='', color=False, mirror_axis='X'):
    """Mirrr the control shapes from fisrt selection to the second."""

    if not source or not target:
        sel = mc.ls(sl=1)
        if not len(sel) == 2:
            mc.warning('Select or input two nodes: source, target.')
            return

        source = sel[0]
        target = sel[1]

    copy_shape(source, target, mirror_axis=mirror_axis)
    if color:
        copy_color(source, target)

def mirror_shape_by_name(source_nodes=None):

    if not source_nodes:
        source_nodes = mc.ls(sl=1)
    source_nodes = mc.ls(source_nodes)

    if not source_nodes:
        mc.warning('Select at least one control to mirror shapes for.')

    for src in source_nodes:

        dst = ''
        if src.startswith('R_'):
            dst = src.replace('R_', 'L_', 1)

        elif src.startswith('L_'):
            dst = src.replace('L_', 'R_', 1)

        dst = mc.ls(dst)
        if dst:
            mirror_shape(src, dst[0])

def copy_shape(source='', target='', world_space=True, mirror_axis=None):
    """Copy curve shapes from one ctrl to another

    ARGS:
    source = ctrl to copy from
    target = ctrl to copy to
    world_space = copy shapes in world space vs local which will move ctrl
    mirror = mirror the ctrl from one side to another acos axis
    (options are: X, Y, Z)
    """

    if not source or not target:
        sel = mc.ls(sl=1)
        if not len(sel) == 2:
            mc.warning('Select or input two nodes: source, target.')
            return

        source = sel[0]
        target = sel[1]

    if not mc.objExists(source) or not mc.objExists(target):
        return

    src_shapes = utils.get_shapes(source)
    trg_shapes = utils.get_shapes(target)

    for node in src_shapes:
        if mc.nodeType(node) in ['gPivotShape', 'gJointShape']:
            src_shapes.remove(node)

    for node in trg_shapes:
        if mc.nodeType(node) in ['gPivotShape', 'gJointShape']:
            trg_shapes.remove(node)

    # create all needed shapes
    if not src_shapes:
        return

    if trg_shapes:
        mc.delete(trg_shapes)

    # create tem pctrl
    tmp = mc.duplicate(source, rc=1)[0]
    children = utils.get_children(tmp)
    if children:
        mc.delete(children)

    utils.set_attrs(tmp, 't r s', l=0, k=1)
    new_shapes = utils.get_shapes(tmp)

    # parent shapes
    mc.parent(new_shapes, target, r=1, s=1)
    mc.delete(tmp)

    new_shapes = utils.get_shapes(target)

    for i, new_shape in enumerate(new_shapes):
        new_shapes[i] = mc.rename(new_shape, target+'Shape')

    # match in world space
    if world_space:
        for i, src_shape in enumerate(src_shapes):

            points = get_crv_point(src_shape)
            set_crv_points(new_shapes[i], points)

    # mirros across specifed axis
    if mirror_axis:
        mult = [-1, 1, 1]
        if mirror_axis.upper() == 'Y':
            mult = [1, -1, 1]
        elif mirror_axis.upper() == 'Z':
            mult = [1, 1, -1]

        for i, new_shape in enumerate(new_shapes):
                points = get_crv_point(new_shape)
                points = [ [p[0]*mult[0],
                            p[1]*mult[1],
                            p[2]*mult[2]]
                                for p in points ]
                set_crv_points(new_shapes[i], points)

    set_historical_importance(target)

'''
def insert_groups(num_grps=3, ctrl=None):
    """Insert specified number of offset nodes"""

    if not ctrl:
        ctrl = mc.ls(sl=1)
        if ctrl:
            ctrl = ctrl[0]

    if not ctrl:
        mc.warning('Select or specify a ctrl!')
        return

    grp_suffix = 'GRP'
    ctrl_suffix = 'CTL'

    base_name = ctrl.replace('_'+grp_suffix, '')

    # create ctrla
    grps = []

    for i in range(num_grps):
        letter = utils.letters[i]
        grp_name = utils.join_strings([base_name, '#', grp_suffix])
        grp_name = utils.get_unique_name(grp_name)

        if grps:
            grps.append(mc.group(grps[-1], n=grp_name))
        else:
            grps.append(mc.group(ctrl, n=grp_name))

    mc.xform(grps, piv=[0,0,0])
    mc.select(ctrl)

    return grps
'''


def scale_ctrl(zero, ctrl, mirror_mode=False, scale=[-1,1,1], match_shape=None):
    """Scale ctrls OR mirror it in joint mode."""

    mc.setAttr(zero+'.s', scale[0], scale[1], scale[2])
    if match_shape and mc.objExists(match_shape):
        copy_shape(match_shape, ctrl)

def create_movable_pivot(ctrl=None, shape='diamond', ctrl_type='transform'):
    """Create a movable pivot.

        KWARGS:
            :ctrl: Control to add pivot to
            :shape: shape for pivot ctrl (default = sphere)
            :ctrl_type: Use "joint" if the anm ctrl node type is a joint."""

    current_sel = mc.ls(sl=1)

    if not ctrl:
        ctrl = mc.ls(sl=1)
        if ctrl:
            ctrl = ctrl[0]
    if not ctrl:
        mc.warning('Select or specify a ctrl!')
        return

    pivot_suffix = 'PIV_CTL'
    ctrl_suffix = 'CTL'

    bb = mc.exactWorldBoundingBox(ctrl)
    scale = round(utils.get_distance(bb[:3], bb[3:]) * .05, 3)
    scale = [scale] * 3

    # Crteate pivot node
    pivot_name = ctrl.replace(ctrl_suffix, pivot_suffix)
    pivot = mc.duplicate(ctrl, n=pivot_name, po=1)[0]
    utils.set_attrs(pivot, 't r s v', k=1, l=0)
    mc.parent(pivot, ctrl)

    # delte custom attrs
    attrs = mc.listAttr(pivot, ud=1)
    if attrs:
        if 'animControl' in attrs:
            attrs.remove('animControl')
        for attr in attrs:
            mc.deleteAttr(pivot+'.'+attr)

    create_shape(shape, pivot, scale=scale)
    mc.setAttr(pivot+'.displayHandle', 1)

    if not mc.objExists(ctrl+'.animPivotVis'):
        mc.addAttr(ctrl, ln='animPivotVis', at='bool', k=1, dv=0)

    mc.connectAttr(ctrl+'.animPivotVis', pivot+'.v')

    loc = utils.snap_locator(ctrl)
    mc.delete(mc.pointConstraint(ctrl, loc))
    pivot_pos = mc.xform(loc, q=1, t=1, ws=1)[0:3]
    mc.delete(loc)

    mc.xform(pivot, ws=1, t=[pivot_pos[0], pivot_pos[1], pivot_pos[2]])

    utils.set_attrs(ctrl, 'animPivotVis', k=0, cb=1)
    utils.set_attrs(pivot, 'r s u v', k=0, l=1)

    # simple standard mode for creating a movable pivot
    if ctrl_type == 'transform':

        mc.connectAttr(pivot+'.t', ctrl+'.rotatePivot')
        mc.connectAttr(pivot+'.t', ctrl+'.scalePivot')

    # different legacy method which works for joint ctrls wit hjoint orient values
    else:
        zero =  utils.get_parent(ctrl+'_MOCAP')
        par_grp = mc.createNode('transform', p=zero, n=pivot+'_GRP')
        neg_par_grp = mc.createNode('transform', p=zero, n=pivot+'_NEG_GRP')
        neg_grp = mc.createNode('transform', p=neg_par_grp, n=pivot+'_NEG')

        children = utils.get_children(ctrl)

        utils.set_attrs(children, 'jo', l=0)

        mc.parent(ctrl+'_OFF', par_grp)
        mc.parent(neg_par_grp, ctrl)
        mc.parent(children, neg_grp)

        mc.connectAttr(pivot+'.t', par_grp+'.t')
        utils.connect_negative(pivot+'.tx', neg_grp+'.tx')
        utils.connect_negative(pivot+'.ty', neg_grp+'.ty')
        utils.connect_negative(pivot+'.tz', neg_grp+'.tz')

        utils.set_attrs(children, 'jo', l=1)

        #pin_ctrl_shape_to_node(ctrl, neg_grp)

    mc.select(pivot)

    return pivot

def create_driven_shape(ctrl, drv_nodes, replace=False, offset=[0,0,0]):
    """Create a selectable control curve shape contrainted to specified drv_nodes"""

    shape = utils.get_shapes(ctrl)
    if replace and shape:
        mc.delete(shape)

    drv_nodes = mc.ls(drv_nodes)

    if len(drv_nodes) == 1 and ctrl not in drv_nodes:
        drv_nodes.insert(0, ctrl)

    # Create crv
    arg = 'curve -d 1 '
    for n in drv_nodes:
        x = [str(_) for _ in mc.xform(n, q=1, ws=1, t=1)]
        arg += '-p {0}'.format(' '.join(x))

    crv = mm.eval(arg)
    crv_shape = utils.get_shapes(crv)[0]
    crv_shape = mc.parent(crv_shape, ctrl, r=1, s=1)[0]
    mc.delete(crv)

    for i, node in enumerate(drv_nodes):
        crv_point = '{0}.controlPoints[{1}]'.format(crv_shape, i)
        if node == ctrl:
            mc.setAttr(crv_point, offset[0], offset[1], offset[2])

        else:
            point_node = node
            loc = utils.snap_locator(point_node)
            loc = mc.parent(loc, point_node)
            loc = mc.rename(loc, point_node+'_LOC')
            mc.delete(utils.get_shapes(loc))
            mc.xform(loc,  a=1, ro=[0,0,0])

            offset = [round(x, 3) for x in mc.xform(loc, q=1, a=1, t=1)]

            if offset != [0,0,0]:
                point_node = mc.createNode('transform', p=node, n=ctrl+'_'+node+'_dvs')
                mc.xform(point_node, a=1, t=offset)

            mmx = mc.createNode('multMatrix', n=point_node+'_mmx')
            mc.connectAttr(point_node+'.worldMatrix', mmx+'.matrixIn[0]')
            mc.connectAttr(ctrl+'.worldInverseMatrix', mmx+'.matrixIn[1]')

            dcm = mc.createNode('decomposeMatrix', n=point_node+'_dcmx')
            mc.connectAttr(mmx+'.matrixSum', dcm+'.inputMatrix')
            mc.connectAttr(dcm+'.outputTranslate', crv_point)

            mc.setAttr(dcm+'.ihi', 0)
            mc.setAttr(mmx+'.ihi', 0)

        crv_shape = mc.rename(crv_shape, ctrl+'Shape')
        set_historical_importance(ctrl)

    crv_shape = mc.rename(crv_shape, ctrl+'_driven_SHAPE')
    mc.addAttr(crv_shape, ln='drivenShape', at='message')

    return crv_shape

'''
def pin_ctrl_shape_to_node(ctrl, node):
    """This will pin specifed shape cv points to a node"""

    points = mc.ls([s+'.cv[*]' for s in utils.get_shapes(ctrl)], fl=1)
    grp = utils.create_node('transform', n=ctrl+'_pinned_points', p=node)

    for point in points:

        point_attr = point.replace('.cv[', '.controlPoints[')
        name = utils.clean_name(point, keep_underscores=1)+'_POS'
        loc = utils.snap_locator(point, node_type='transform', name=name)
        loc = mc.parent(loc, grp)[0]

        mmx = mc.createNode('multMatrix', n=node+'_mmx')
        mc.connectAttr(loc+'.worldMatrix', mmx+'.matrixIn[0]')
        mc.connectAttr(ctrl+'.worldInverseMatrix', mmx+'.matrixIn[1]')

        dcm = mc.createNode('decomposeMatrix', n=node+'_dcmx')
        mc.connectAttr(mmx+'.matrixSum', dcm+'.inputMatrix')
        mc.connectAttr(dcm+'.outputTranslate', point_attr)

        mc.setAttr(dcm+'.ihi', 0)
        mc.setAttr(mmx+'.ihi', 0)
'''

def get_shape_data(crv):

    shape_data = {}
    cshapes = [s for s in utils.get_shapes(crv) if mc.nodeType(s) == 'nurbsCurve']

    for shape in cshapes:
        d = mc.getAttr(shape+'.degree')
        points = get_crv_point(shape)
        form = mc.getAttr(shape+'.form')
        shape_data[shape] = {'points':points, 'form':form, 'degree':d}

    return shape_data

def save_shape(name=None, crv=None):
    """Save selected shape as an entry"""

    global json_data

    # read control_data file
    base_path = os.path.join(system_base_path, 'config')
    file_path = os.path.join(base_path, 'controlData.json')
    file_path = utils.norm_path(file_path)

    if not crv:
        crv = mc.ls(sl=1)
        if not crv:
            return
        crv = crv[0]

    crv = mc.ls(crv)
    if not crv:
        return
    crv = crv[0]

    cshapes = [s for s in utils.get_shapes(crv) if mc.nodeType(s) == 'nurbsCurve']
    if not cshapes:
        raise ValueError('No nurbsShapes found!')

    if not name:
        result = mc.promptDialog(
                title='New Shape Entry',
                message='Entry Name:',
                button=['Add', 'Cancel'],
                defaultButton='Add',
                cancelButton='Cancel',
                dismissString='Cancel',
                text=crv)

        if result == 'Add':
            name = mc.promptDialog(q=1, text=1).lower()
        else:
            return
    else:
        name = name.lower()

    name = name.lower()
    name = name.replace(' ', '_')
    name = re.sub('_+', '_', name)

    # check for duplicate entry

    if name in protected_entries:
        raise ValueError('Cannot overwrite this shape!')

    result = None
    if name in shapes:
        result = mc.confirmDialog(title='Add or Overwrite?',
                        message='Shape definition already exists ' + \
                                'with this name.\n?' + \
                                'Overwrite or add new definition?',
                        button=['Add New', 'Overwrite','Cancel'],
                        defaultButton='Add New',
                        cancelButton='Cancel',
                        dismissString='Cancel')

        if result == 'Add New':
            i = 0
            nn = name+'_'+utils.letters[i].lower()

            while nn in shapes:
                nn = name+'_'+utils.letters[i].lower()
                i += 1

            name = nn.lower()

        elif result == 'Cancel':
            return

    # get curve data
    shapeInfo = []
    for shape in cshapes:
        d = mc.getAttr(shape+'.degree')
        points = get_crv_point(shape)
        form = mc.getAttr(shape+'.form')
        shapeInfo.append({'points':points, 'form':form, 'degree':d})

    # build new data dict for controls presets file
    json_data['shapes'][name] = shapeInfo
    data = json_data

    # write entry
    utils.write_json(file_path, data)
    mc.warning('Saved shape entry as: {0} to {1}'.format(name, file_path))

    reload_control_data()

def get_color_value(crv):
    cshapes = [s for s in utils.get_shapes(crv) if mc.nodeType(s) == 'nurbsCurve']
    colorValue = [0]
    for node in cshapes+[crv]:
        if mc.getAttr(node+'.overrideEnabled'):

            if mc.getAttr(node+'.overrideRGBColors'):
                cval = list(mc.getAttr(node+'.overrideColorRGB')[0])
                cval = [round(v, 6) for v in cval]
            else:
                cval = [mc.getAttr(node+'.overrideColor')]

            if sum(map(float, cval)):
                colorValue = cval
                break
    if len(colorValue) == 1:
        colorValue = colorValue[0]
    return colorValue

def save_color(name=None, crv=None):
    """Save selected shape as an entry"""

    global json_data

    # read control_data file
    base_path = os.path.join(system_base_path, 'config')
    file_path = os.path.join(base_path, 'controlData.json')
    file_path = utils.norm_path(file_path)

    if not crv:
        crv = mc.ls(sl=1)
        if not crv:
            return
        crv = crv[0]

    crv = mc.ls(crv)
    if not crv:
        return
    crv = crv[0]


    if not name:
        result = mc.promptDialog(
                title='New Color Entry',
                message='Entry Name:',
                button=['Add', 'Cancel'],
                defaultButton='Add',
                cancelButton='Cancel',
                dismissString='Cancel',
                text=crv)

        if result == 'Add':
            name = mc.promptDialog(q=1, text=1).lower()
        else:
            return
    else:
        name = name.lower()

    name = name.lower()
    name = name.replace(' ', '_')
    name = re.sub('_+', '_', name)

    # check for duplicate entry
    # find the one with color
    colorValue = get_color_value(crv)

    if name in protected_entries:
        raise ValueError('Cannot overwrite this shape!')

    result = None
    if name in shapes:
        result = mc.confirmDialog(title='Add or Overwrite?',
                        message='Shape definition already exists ' + \
                                'with this name.\n?' + \
                                'Overwrite or add new definition?',
                        button=['Add New', 'Overwrite','Cancel'],
                        defaultButton='Add New',
                        cancelButton='Cancel',
                        dismissString='Cancel')

        if result == 'Add New':
            i = 0
            nn = name+'_'+utils.letters[i].lower()

            while nn in shapes:
                nn = name+'_'+utils.letters[i].lower()
                i += 1

            name = nn.lower()

        elif result == 'Cancel':
            return

    # build new data dict for controls presets file
    json_data['colors'][name] = colorValue
    data = json_data

    # write entry
    utils.write_json(file_path, data)
    mc.warning('Saved color entry as: {0} to {1}'.format(name, file_path))

    reload_control_data()

# initalize data from config
reload_control_data()


