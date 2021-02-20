# -*- coding: utf-8 -*-
"""Functions for building a skeleton from a guide_node rig."""

import maya.cmds as mc
import maya.mel as mm
import os

from rigBot import utils
mc.loadPlugin('cmAspectRatio')

path = os.path.expandvars('/job/${PL_SHOW}/${PL_DIVISION}/asset/Camera/reference/camera_aspect_ratio_reference')
file_path = os.path.join(path, 'camera_aspect_ratios.json')

def get_wh(ratio):

    render_width = mc.getAttr("defaultResolution.width")
    render_height = mc.getAttr("defaultResolution.height")

    width = int(render_height * ratio)
    height = int(render_height)

    if width > render_width:
        height = int(render_width * render_height / width)
        width = int(render_width)

    return width, height

def create_node(label='', camera='', aspect_ratio=1.774, color=(0,1,1,0.5), bg_color=(0,0,0,0.5), fixed=False, width=0, height=0):

    # Get camera
    if not camera:
        sel = mc.ls(sl=1)
        if sel:
            camera = sel[0]

    camera = mc.ls(camera)
    if not camera:
        cam = mc.createNode('camera')
        camera = mc.listRelatives(cam, p=1)

    camera = camera[0]

    # get node name
    if label:
        name = label+'_aspectRatioShape'
    else:
        name = 'aspectRatioShape'
        label = 'Device Name'

    name = mc.createNode('mute', n=name)
    mc.delete(name)

    shape = mc.listRelatives(camera, s=1)[0]

    if fixed:
        if height:
            aspect_ratio = float(width) / float(height)
        else:
            aspect_ratio = 0.0
    else:
        width, height = get_wh(aspect_ratio)

    ratio = mc.createNode('cmAspectRatio', n=name, p=camera)

    #create ndoe
    mc.setAttr(ratio+'.label', label, type='string')
    mc.setAttr(ratio+'.camera', shape, type='string')
    mc.setAttr(ratio+'.camera', l=1)

    attrs = ['lpx', 'lpy', 'lpz', 'lsx', 'lsy', 'lsz']
    utils.set_attrs(ratio, ' '.join(attrs), k=1, l=0)
    utils.set_attrs(ratio, ' '.join(attrs), k=0, l=1)

    attrs =['tclr', 'tclg', 'tclb', 'bgclr', 'bgclg', 'bgclb']
    utils.set_attrs(ratio, ' '.join(attrs), k=0, l=0)

    mc.setAttr(ratio+'.aspectRatio', aspect_ratio)
    mc.setAttr(ratio+'.aspectRatio', l=1)
    mc.setAttr(ratio+'.v', l=0, k=1)

    mc.setAttr(ratio+'.useFixedSize', fixed)
    mc.setAttr(ratio+'.width', width)
    mc.setAttr(ratio+'.height', height)

    mc.setAttr(ratio+'.width', l=1)
    mc.setAttr(ratio+'.height', l=1)

    mc.setAttr(ratio+'.tcl', color[0], color[1], color[2])
    mc.setAttr(ratio+'.ta', color[3])

    mc.setAttr(ratio+'.bgc', bg_color[0], bg_color[1], bg_color[2])
    mc.setAttr(ratio+'.bga', bg_color[3])

    attrs = ['tclr', 'tclg', 'tclb', 'bgcr', 'bgcg', 'bgcb']
    utils.set_attrs(ratio, ' '.join(attrs), k=0, l=0)

    # master attrs
    if not mc.objExists(shape+'.fontSize'):
        mc.addAttr(shape, ln='fontSize', at='short', k=1, dv=16, min=0)

    mc.connectAttr(shape+'.fontSize', ratio+'.fontSize')
    mc.setAttr(ratio+'.fontSize', k=0, l=1)

    mc.addAttr(shape, ln=ratio+'_visibilty', nn=label+' Visibility', at='bool', k=1, dv=True)
    mc.connectAttr(shape+'.'+ratio+'_visibilty', ratio+'.v')

    mc.select(ratio)
    return ratio

def record(arg=None):

    try:
        os.mkdir(path)
    except:
        pass

    if not os.path.isdir(path):
        mc.warning('Cannot create path!')
        return

    data = {}

    #read all node data
    nodes = mc.ls(type='cmAspectRatio')
    attrs = ['sac', 'ar', 'tv', 'w', 'h','tp', 'tclr', 'tclg', 'tclb', 'ta', 'bgcb',
             'fs', 'lw', 'bgv', 'bgcr', 'bgcg', 'bga']

    for node in nodes:
        node_data = {'parent': utils.get_parent(node),
                     'label': mc.getAttr(node+'.label'),
                     'camera': mc.getAttr(node+'.camera')}

        for a in attrs:
            node_data[a] = round(mc.getAttr(node+'.'+a),4)

        data[node] = node_data

    utils.write_json(file_path, data)

def rebuild(arg=None):

    data = utils.read_json(file_path)
    attrs = ['sac', 'ar', 'tv', 'tclr', 'tp', 'tclg', 'tclb', 'ta', 'bgcb',
             'fs', 'w', 'h', 'lw', 'bgv', 'bgcr', 'bgcg', 'bga']

    ratios = []
    for node, node_data in data.items():
        if mc.objExists(node_data['camera']):
            camera = utils.get_parent(node_data['camera'])
        else:
            camera = utils.get_parent(mc.createNode('camera', n= node_data['camera']))

        ratio = create_node(label=node_data['label'], camera=camera)

        for a in attrs:
            mc.setAttr(ratio+'.'+a, l=0)
            try:
                mc.setAttr(ratio+'.'+a, node_data[a])
            except:
                pass

        ratios.append(ratio)

    for node in ratios:
        attrs = ['lpx', 'lpy', 'lpz', 'lsx', 'lsy', 'lsz']
        utils.set_attrs(ratio, ' '.join(attrs), k=1, l=0)
        utils.set_attrs(ratio, ' '.join(attrs), k=0, l=1)

        attrs =['tclr', 'tclg', 'tclb', 'bgclr', 'bgclg', 'bgclb']
        utils.set_attrs(ratio, ' '.join(attrs), k=0, l=0)

        mc.setAttr(ratio+'.w', l=1)
        mc.setAttr(ratio+'.h', l=1)
        mc.setAttr(ratio+'.aspectRatio', l=1)

        attrs = ['tclr', 'tclg', 'tclb', 'bgcr', 'bgcg', 'bgcb']
        utils.set_attrs(ratio, ' '.join(attrs), k=0, l=0)

class run():

    def __init__(self):
        win = 'aspectUI2'
        cameras = mc.ls(type='camera')

        if mc.window(win, q=1, ex=1):
            mc.deleteUI(win)

        mc.window(win, t='Create Aspect Ratio Node', s=0)

        mc.columnLayout(adj=1)

        self.cam_w = mc.optionMenu( label='                                 Camera', w=200)
        for c in cameras:
            mc.menuItem( label=utils.get_transform(c))

        self.label_w = mc.textFieldGrp( label='Label', text='Device Name' )
        self.mode = mc.radioButtonGrp( label='Size Mode', labelArray2=['Aspect Ratio', 'Fixed Image Size'], cc=self.enable, numberOfRadioButtons=2, sl=1)
        self.aspect_w = mc.floatFieldGrp( label='Apect Ratio', pre=3, numberOfFields=1, v1=1.774)
        self.size_w = mc.floatFieldGrp( label='Size', pre=3, en=0, numberOfFields=2, v1=1024.0, v2=768.0)

        mc.separator(h=10)

        self.color_w = mc.colorSliderGrp(label='Text Color', rgb=(0, 1, 1) )
        self.alpha_w = mc.colorSliderGrp(label='Text Alpha', hsv=(0, 0, 0.5) )

        mc.separator(h=10)
        self.bgcolor_w = mc.colorSliderGrp(label='Background Color', rgb=(0, 0, 0) )
        self.bgalpha_w = mc.colorSliderGrp(label='Background Alpha', hsv=(0, 0, 0.5) )

        mc.separator(h=10, st='none')
        mc.button(l='Create', c=self.create)

        mc.separator(h=10)
        mc.button(l='Record Setup To JSON', c=record)
        mc.button(l='Build from JSON', c=rebuild)

        mc.showWindow()
        mc.window(win, e=1, wh=[392, 290] )

    def enable(self, arg2):

        if mc.radioButtonGrp(self.mode, q=1, sl=True) == 1:
            mc.floatFieldGrp( self.size_w, e=1, en=0)
            mc.floatFieldGrp( self.aspect_w, e=1, en=1)
        else:
            mc.floatFieldGrp( self.size_w, e=1, en=1)
            mc.floatFieldGrp( self.aspect_w, e=1, en=0)

    def create(self, arg):

        cam = mc.optionMenu(self.cam_w, q=1, v=1)
        aspect = mc.floatFieldGrp(self.aspect_w, q=1, v1=1)
        label = mc.textFieldGrp(self.label_w, q=1, text=1)

        color = mc.colorSliderGrp(self.color_w, q=1, rgb=1)
        alpha = mc.colorSliderGrp(self.alpha_w, q=1, rgb=1)
        alpha = sum(alpha) / len(alpha)

        bg_color = mc.colorSliderGrp(self.bgcolor_w, q=1, rgb=1)
        bg_alpha = mc.colorSliderGrp(self.bgalpha_w, q=1, rgb=1)
        bg_alpha = sum(bg_alpha) / len(bg_alpha)

        width = mc.floatFieldGrp( self.size_w, q=1, v1=1)
        height = mc.floatFieldGrp( self.size_w, q=1, v2=1)

        fixed = False
        if mc.radioButtonGrp(self.mode, q=1, sl=True) == 2:
            fixed = True
        create_node(label, cam, aspect, color+[alpha], bg_color+[bg_alpha], fixed, width, height)
