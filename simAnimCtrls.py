import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import spline
from rigBot import rivet

try:
    import bake
except:
    from rigBot import bake

import os

ctrls = []

mesh = ''
nucleus = ''
cloth_node = ''

start_frame = mc.playbackOptions(q=1, min=1)
end_frame = mc.playbackOptions(q=1, max=1)

def tag_ctrls(controls):

    controls = [c.split(':')[-1] for c in controls]
    controls.sort()

    set_nodes()

    if nucleus:
        if not mc.objExists(nucleus+'.animControls'):
            mc.addAttr(nucleus, ln='animControls', dt='string')
        mc.setAttr(nucleus+'.animControls', str(controls), type='string')

def set_ctrls(selection=[]):

    global ctrls

    selection = mc.ls(selection)
    if selection:
        ctrls = selection

    else:
        ctrls = mc.ls(sl=1)

    if ctrls and nucleus:
        try:
            tag_ctrls(ctrls)
        except:
            pass

def set_nodes():

    global nucleus
    global cloth_node
    global mesh
    global ctrls

    nucleus = ''
    mesh = ''
    cloth_node = ''
    ctrls = []
    namespace = ''

    # get nucleus
    nucleus = mc.ls(type='nucleus')
    if nucleus:
        nucleus = nucleus[0]

        # get cloth node
        cloth_node = [n for n in mc.listConnections(nucleus) if mc.nodeType(utils.get_shapes(n)[0]) =='nCloth']
        if cloth_node:
            cloth_node = list(set(cloth_node))
            cloth_node = cloth_node[0]

            # get mesh
            mesh = [n for n in mc.listConnections(utils.get_shapes(cloth_node)[0]) if mc.nodeType(utils.get_shapes(n)[0]) == 'mesh']
            if mesh:
                mesh = list(set(mesh))
                mesh = mesh[0]
            else:
                mc.warning('Cannot find mesh!')

        if mc.objExists(nucleus+'.animControls'):
            ctrl_str = mc.getAttr(nucleus+'.animControls')
            if ctrl_str:
                ctrl_list = eval(ctrl_str)

                if ':' in mesh:
                    namespace = mesh.split(':')[0]
                    ctrl_list = [namespace+':'+c.split(':')[-1] for c in ctrl_list]

                ctrls = mc.ls(ctrl_list)

            if not ctrls:
                mc.warning('Cannot find controls!')

        if namespace:
            namespace+=':'

        if mc.objExists(namespace+'sim_GRP'):
            mc.showHidden(namespace+'sim_GRP')

    if nucleus and cloth_node and mesh:
        if ctrls:
            print 'Found all sim nodes AND controls!'
        else:
            print 'Found sim nodes, except controls..'

    nodes = mc.ls(type=['nucleus', 'nCloth', 'nRigid', 'dynamicConstraint'])
    for n in nodes:
        mc.setAttr(n+'.ihi', 1)

def set_frame_range():

    if not nucleus or not mc.nodeType(nucleus) == 'nucleus':
        set_nodes()

    global start_frame
    global end_frame

    start_frame = mc.playbackOptions(q=1, min=1)
    end_frame = mc.playbackOptions(q=1, max=1)

    if mc.objExists(nucleus+'.startFrame'):
        mc.setAttr(nucleus+'.startFrame', start_frame)

    mc.currentTime(18)

def bake_ctrls_to_nmesh(bakeSRT=False):

    if not mesh:
        set_nodes()
    mc.playbackOptions(min=start_frame)
    mc.playbackOptions(max=end_frame)

    auto_keyframe_state = mc.autoKeyframe(q=1, state=1)
    mc.autoKeyframe(state=0)

    # get frame range
    mc.currentTime(start_frame)

    # duplicate and bake mesh
    panel = bake.set_dull_panel()

    new_mesh = mc.duplicate(mesh)[0]
    bss = mc.blendShape(mesh, new_mesh, w=[0,1])

    mc.select(new_mesh)
    tmp_cache_dir  = mc.internalVar(utd=1)
    t_files = [os.path.join(tmp_cache_dir, 'CACHE.xml'),
               os.path.join(tmp_cache_dir, 'CACHE.mcx')]

    for f in t_files:
        if os.path.isfile(f):
            os.remove(f)

    mc.select(new_mesh)
    mm.eval('doCreateGeometryCache 6 { "3", "'+str(start_frame)+'", "'+str(end_frame)+'", "OneFile", "1", "'+tmp_cache_dir+'","0","CACHE","0", "add", "0", "1", "1","0","1","mcx","0" } ;')
    mc.delete(bss)

    mc.currentTime(start_frame)

    noxform_grp = 'rivets_GRP'
    mc.createNode('transform', n='rivets_GRP')

    cons = []
    for c in ctrls:
        cons.append(rivet.mesh_mtx(new_mesh, c, noxform_grp=noxform_grp))

    bake.bake_transform_animation(ctrls, bakeSRT=bakeSRT)
    bake.remove_flip(ctrls)

    bake.set_model_panel(panel)

    mc.delete(noxform_grp, new_mesh, cons)
    for f in t_files:
        if os.path.isfile(f):
            os.remove(f)

    mc.hide(ctrls[0].split(':')[0]+':sim_GRP')

    mc.autoKeyframe(state=auto_keyframe_state)
    mc.select(ctrls)

def blend_in_out(start_range=5, end_range=20, zero_in=False, zero_out=True):

    auto_keyframe_state = mc.autoKeyframe(q=1, state=1)
    mc.autoKeyframe(state=0)

    mc.select(ctrls)
    mc.cutKey(ctrls, t=(start_frame+1, start_frame+start_range))
    mc.cutKey(ctrls, t=(end_frame-end_range+1, end_frame-1))

    if zero_in or zero_out:
        mc.xform(ctrls, a=1, t=[0,0,0], ro=[0,0,0])
        if zero_in:
            mc.setKeyframe(ctrls, t=start_frame)
        if zero_out:
            mc.setKeyframe(ctrls, t=end_frame)

    mc.autoKeyframe(state=auto_keyframe_state)

def clear_cache():

    if not mesh:
        set_nodes()

    try:
        mc.select(mesh)
        mm.eval('deleteCacheFile 2 { "delete", "" };')
    except:
        print('No cache on mesh!')

def cut_ctrl_anim():
    if not ctrls:
        set_nodes()
    mc.cutKey(ctrls)
    mc.xform(ctrls, a=1, t=[0,0,0], ro=[0,0,0])
    mc.select(ctrls)

def create_cache(set_dull_panel=False):

    set_frame_range()
    clear_cache()

    mc.setAttr(nucleus+'.enable', 1)
    mc.setAttr(nucleus+'.startFrame', start_frame)

    if set_dull_panel:
        panel = bake.set_dull_panel()

    mc.currentTime(start_frame)
    mc.select(mesh)

    mm.eval('doCreateNclothCache 5 { "3", "'+str(start_frame)+'", "'+str(end_frame)+'", "OneFile", "1", "","0","","0", "add", "0", "1", "1","0","1","mcx" } ;')

    if set_dull_panel:
        bake.set_model_panel(panel)


def quick_sim(start_range=5, end_range=20, zero_in=True, zero_out=True, translate = True):

    set_nodes()

    if not nucleus:
        raise RuntimeError('Nucleus not found!')

    if not cloth_node:
        raise RuntimeError('nCloth node not found!')

    if not mesh:
        raise RuntimeError('Sim mesh node not found!')

    if not ctrls:
        raise RuntimeError('Anim controls node not found!')

    set_frame_range()

    print '\n##########################################'
    print 'Frame Range: {0} - {1}'.format(start_frame, end_frame)
    print 'Nucleus: {0}'.format(nucleus)
    print 'NCloth Node: {0}'.format(cloth_node)
    print 'Sim Mesh: {0}'.format(mesh)
    print 'Anim Controls:'
    for c in ctrls:
        print '\t'+c

    create_cache(set_dull_panel=True)
    bake_ctrls_to_nmesh()

    blend_in_out(start_range, end_range, zero_in, zero_out)
    
    #Removing the translations reduces the stretch effect.
    if translate == False:

        attributes = ["translateX", "translateY", "translateZ"]
        for ctrl in ctrls:
            for attr in attributes:
                anim_node  = mc.listConnections (ctrl +"." +attr, t="animCurve")
                print anim_node
                if anim_node:
                    mc.delete(anim_node)
                    mc.setAttr(ctrl +"." +attr, 0)
