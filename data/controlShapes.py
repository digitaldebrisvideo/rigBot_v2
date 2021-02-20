import maya.cmds as mc
import maya.mel as mm

import cPickle as pickle
import time
import os

from rigBot import utils
from rigBot import control

file_extention = '.ctrls'
deformer_type = 'controlShapes'

def get_data(nodes=None):

    # get nodes
    current = mc.ls(sl=1)

    if not nodes:
        nodes = [c.replace('.animControl','') for c in mc.ls('*.animControl', ln=1)]
        if mc.objExists('control_SEL'):
            mc.select('control_SEL')
            nodes.extend(mc.ls(sl=1))
        nodes.extend(mc.ls('*_CTL'))

    nodes = mc.ls(nodes)
    mc.select(current)

    if not nodes:
        mc.warning('No nodes specified.')
        return

    data = {}
    for node in nodes:
        shapes = [s for s in utils.get_shapes(node) if mc.nodeType(s) == 'nurbsCurve']
        shapes = [s for s in shapes if not mc.listConnections(s+'.controlPoints', s=1, d=0, p=1)]

        if not shapes:
            continue

        colorInfo = control.get_color_value(node)
        shapeInfo = []

        for shape in shapes:
            d = mc.getAttr(shape+'.degree')
            points = control.get_crv_point(shape)
            form = mc.getAttr(shape+'.form')
            shapeInfo.append({'shapeName':shape, 'points':points, 'form':form, 'degree':d})

        data[node] = {'color': colorInfo, 'shapes':shapeInfo}

    return data

def save(file_path):
    """Wrapper for class export call, Can export multiple and
        prompts for file path"""

    t = time.time()
    data = get_data()

    if not data:
        mc.warning('No control shapes to save in this scene!')
        return

    if not file_path.endswith(file_extention):
        file_path = os.path.splitext(file_path)[0]+file_extention

    utils.write_json(file_path, data)
    print time.time() - t

def load(file_path, **kwargs):
    """Wrapper for importing weights"""

    t = time.time()

    # If not remap then load as usual
    data = utils.read_json(file_path)
    set_data(data)

    print time.time() - t


def set_data(data):

    for node, node_info in data.items():

        if not mc.objExists(node):
            mc.warning('Control does not exist: '+node)
            continue

        shape = node_info['shapes']
        color = node_info['color']

        # IF the current shape has the same number of points then we dont need to createa new shape
        current_shapes = utils.get_shapes(node)
        recreate_shape = False

        for i in range(len(shape)):
            cshape = shape[i]['shapeName']
            number_of_points = len(shape[i]['points'])
            degree = shape[i]['degree']
            form = shape[i]['form']

            if not mc.objExists(cshape):
                recreate_shape = True

            else:
                cdegree = mc.getAttr(cshape+'.degree')
                current_points = len(mc.ls(cshape+'.cv[*]', fl=1))
                cform = mc.getAttr(cshape+'.form')

                if number_of_points != current_points:
                    recreate_shape = True

                if degree != cdegree:
                    recreate_shape = True

                if form != cform:
                    recreate_shape = True

        # recreate shapes
        if recreate_shape:
            mc.delete([s for s in utils.get_shapes(node) if not mc.objExists(s+'.drivenShape')])
            new_shapes = control.create_shape(ctrls=node, data=shape)

        else:
            new_shapes = [s.get('shapeName') for s in shape]

        # Now set the point in space and colors
        for i, cshape in enumerate(new_shapes):
            cshape = shape[i]['shapeName']
            points_pos = shape[i]['points']
            points = mc.ls(cshape+'.cv[*]', fl=1)

            if len(points) == len(points_pos):
                for i, point in enumerate(points):
                    pos = points_pos[i]
                    try:
                        mc.xform(point, ws=1, t=pos)
                    except:
                        pass
            else:
                mc.warning('Somethings wrong .. Cannot set ctrl shape for: '+node)

        # Now se the color
        try:
            control.set_color(color=color, ctrls=node)
        except:
            pass

    print 'Loaded control shapes!'
