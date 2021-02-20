# derived from a Maya Python routine by Juan Carlos Leon

import pymel.core as pm

__author__ = 'jhachigian'


def spike_point(tup, li, z, taper):
    li.append(tup)
    new_tup = (tup[0]/taper, tup[1]/taper, z)
    li.append(new_tup)
    li.append(tup)


def get_box_points(xv, yv, zv, taper=1.0, offset=0.0):
    li = []
    x = xv/2.0
    y = yv/2.0
    z_base = -zv/2.0 + offset
    z_top = zv/2.0 + offset
    """ bottom square """
    li.append((-x, y, z_base))
    li.append((x, y, z_base))
    li.append((x, -y, z_base))
    li.append((-x, -y, z_base))
    li.append((-x, y, z_base))
    """ top box, with spikes to touch the bottom"""
    x *= taper
    y *= taper
    li.append((-x, y, z_top))
    spike_point((x, y, z_top), li, z_base, taper)
    spike_point((x, -y, z_top), li, z_base, taper)
    spike_point((-x, -y, z_top), li, z_base, taper)
    li.append((-x, y, z_top))
    return li


def make_box(x, y, z, taper=1.0, rotation=(0, 0, 0), offset=0.0):
    points = get_box_points(x, y, z, taper=taper, offset=offset)
    curve = pm.curve(degree=1, point=points)
    pm.select(curve + ".cv[0:15]")
    pm.xform(rotation=rotation)
    pm.select(clear=True)
    return curve

if __name__ == "__main__":
    make_box(1, 1, 1)
