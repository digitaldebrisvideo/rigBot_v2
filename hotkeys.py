# My custom user Hotkeys
import maya.cmds as mc
import maya.mel as mm

import os
import shutil

# Hotkeys  'Ctrl+ c & ctrl+ v'   scale - ctrl+x
def zero_selection(zero_scale=False):
    mc.xform(mc.ls(sl=1), a=1, t=[0 ,0, 0])
    mc.xform(mc.ls(sl=1), a=1, ro=[0 ,0, 0])

    if zero_scale:
        mc.xform(mc.ls(sl=1), a=1, s=[1,1,1])

def toggle_hide():
    """Toggle hide and showHidden. Hotkey - 'Ctrl+ h' """

    try:
        mm.eval('ToggleVisibilityAndKeepSelection;')
    except:
        mc.warning('Cannot hide all faces of an object. Hide the object instead.')

def toggle_display(node_types):
    """Toggle model panel display =-- Hotkeys  'j' 'm' 'n' 'k'
        args are 'joints' 'polymeshes' 'nurbsSurfaces' 'nurbsCurves'"""

    panels = mc.getPanel(type='modelPanel')

    i = 1
    if mm.eval('modelEditor -q -'+node_types+' '+panels[0]):
        i = 0

    for p in panels:
        mm.eval('modelEditor -e -'+node_types+' '+str(i)+' '+p)

def convert_selection(mode):
    if mode == 'edges':
        mm.eval('ConvertSelectionToEdges;hilite; selectType -ocm -alc false;selectType -ocm -polymeshEdge true;')

    elif mode == 'faces':
        mm.eval('ConvertSelectionToFaces;hilite; selectType -ocm -alc false;selectType -ocm -polymeshFace true;')

    else:
        mm.eval('ConvertSelectionToVertices;hilite;  selectType -ocm -alc false;selectType -ocm -polymeshVertex true;')

