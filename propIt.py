import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm

import os
import shutil

from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import guide
from rigBot import rig
from rigBot import env
from rigBot import skel
from rigBot import model
from rigBot import data
#
# def create_from_cmnode(asset=None, name='default', variant='primary', file_type='Maya Geometry'):
#
#     use_shotgun = False
#     cm_nodes = mc.ls(type='cmContent')
#     model_grp = [n for n in mc.ls('|*', type='transform') if n not in ['front','persp','side','top'] ]
#
#     if not model_grp:
#         mc.warning('No models in scene and asset is not set! Cannot continue.')
#         return
#
#     if cm_nodes:
#         use_shotgun = True
#         asset = mc.getAttr(cm_nodes[0]+'.entity').strip()
#         name = mc.getAttr(cm_nodes[0]+'.name').replace(asset, '').strip()
#         variant = mc.getAttr(cm_nodes[0]+'.variant').strip()
#         file_type = mc.getAttr(cm_nodes[0]+'.type').strip()
#         model_grp = utils.get_children(utils.get_parent(cm_nodes[0]))
#
#     if env.shotgun and not asset and not cm_nodes:
#         mc.warning('No models in scene and asset is not set! Cannot continue.')
#         return
#
#     if env.check_if_asset_exists(asset):
#         icon = 'warning'
#         title = 'PropIt | Overwrite Asset'
#         msg = 'Creating prop for asset:\n   {0} - {1} variant\n\nThis will OVERWRITE all existing rigbuild data on disk.'.format(asset, variant)
#         msg += '\nAre you sure you want to do this?'.format(asset)
#
#     else:
#         icon = 'question'
#         title = 'PropIt | New Asset'
#         msg = 'Creating prop for asset:\n   {0} - {1} variant\n\nThis will create rigbuild '.format(asset, variant)
#         msg += 'files on disk.\nAre you sure you want to do this?'
#
#     result = mc.confirmDialog(title=title,
#                               message=msg,
#                               icon=icon,
#                               button=['Yes','No'],
#                               defaultButton='Yes',
#                               cancelButton='No',
#                               dismissString='No' )
#
#     if result == 'No':
#         return
#
#     # Make rig asset and create a clean custom and rigbuildlist file
#     if env.check_if_asset_exists(asset):
#         rb_path = env.get_rigbuild_path(asset)
#         files_to_trash = [os.path.join(rb_path, f).replace('\\', '/') for f in os.listdir(rb_path)]
#
#         for file in files_to_trash:
#             if os.path.isfile(file):
#                 os.remove(file)
#             elif os.path.isdir(file):
#                 shutil.rmtree(file)
#
#     env.make_rig_asset(asset)
#     env.set_asset(asset)
#     rb_path = env.get_rigbuild_path(asset)
#
#     # Create guide
#     junk = mc.ls('guides', 'rig_GRP')
#     if junk:
#         mc.delete(junk)
#
#     guide.build('worldRoot')
#
#     bb = mc.exactWorldBoundingBox(model_grp)
#     sy = bb[4]*1.4
#     mc.xform('visibility_CTL', ws=1, t=[0,sy,0])
#
#     sx = (bb[3] - bb[0]) / 4.0
#     sz = (bb[5] - bb[2]) / 4.0
#     if sz > sx:
#         sx = sz
#
#     mc.setAttr('world_CTL.numOffsetCtrls', 2)
#     mc.xform('world_CTL', r=1, s=[sx*1.2,sx*1.2,sx*1.2])
#     mc.xform('visibility_CTL', r=1, s=[sx,sx,sx])
#
#     guide.save()
#
#     # Build rig
#     skel.build(shakeout=1)
#     rig.build()
#
#     model.load(name=name, variant=variant, file_type=file_type)
#
#     rig.connect_rig()
#     rig.finalize()
#
#     # constraint and export cons
#     cons = []
#     for m in [utils.strip_namespace(m) for m in model_grp]:
#         if mc.nodeType(m) in ['transform', 'joint']:
#             utils.set_attrs(m, k=1, l=0)
#
#             try:
#                 cons.extend(mc.parentConstraint('C_root_JNT', m, n=m+'_PRC', mo=1))
#                 cons.extend(mc.scaleConstraint('C_root_JNT', m, n=m+'_sC', mo=1))
#             except:
#                 pass
#
#     env.set_variant('default')
#     mc.select(cons)
#
#     data.save('constraints', nodes=cons)
#
#     # Create new variant and save rig stream
#     if variant == 'primary':
#         variant = 'default'
#
#     env.add_variant(variant)
#     env.set_variant(variant)
#
#     # modify the default model load to reflect trhe current model.
#     build_file = os.path.join(rb_path, asset+'_buildList.py')
#     with open(build_file) as f:
#         lines = f.readlines()
#
#     cmd = "         'command': partial(model.load, name='{0}', variant='{1}', file_type='{2}', version='HIGHEST')".format(name, variant, file_type)
#     cmd += "},\n"
#
#     for i, line in enumerate(lines):
#         if 'model.load' in line:
#             lines[i] = cmd
#
#     all_lines = ''.join(lines)
#     with open(build_file, 'w') as f:
#                 f.write(all_lines)
#
#     # Save completed rig as stream
#     env.save_stream(variant)
#
#     print '##############################'
#     print '# PropIt completed!\n'
#     print '    Asset:   '+asset
#     print '    Variant: '+variant


def create(name='', variant='primary', model_grp=None):

    if not model_grp:
        model_grp = mc.ls(sl=1)

    if not name:
        name = model_grp[0]

    name = utils.clean_name(name, keep_underscores=0)
    name = name[0].upper()+name[1:]

    # Create guide
    junk = mc.ls(name+'_rig_GRP')
    if junk:
        mc.delete(junk)

    bb = mc.exactWorldBoundingBox(utils.get_shapes(model_grp), ii=1)
    scale = utils.get_distance(bb[:3], bb[3:]) 

    result = control.create(name+'_world_CTL', shape='circle')
    mc.parent(result[-2], w=1)
    mc.delete(result[0])

    rig_grp = mc.rename(result[-2], name+'_rig_GRP')
    world_ctrl = result[-1]

    offsets = control.create_offset_ctrls(world_ctrl, 2)
    mc.xform(name+'_world_*CTL.cv[*]', r=1, s=[scale]*3)

    mc.delete(mc.pointConstraint(model_grp, world_ctrl))
    mc.delete(mc.orientConstraint(model_grp, world_ctrl))

    for m in model_grp:
        if mc.nodeType(m) in ['transform', 'joint']:
            utils.set_attrs(m, k=1, l=0)
            cons = utils.get_constraints(m)

            if cons:
                for con in cons:
                    if mc.nodeType(con) == 'pointConstraint':
                        drivers = mc.pointConstraint(cons, q=1, tl=1 )
                        mc.pointConstraint(drivers, world_ctrl, mo=1)
                        mc.delete(con)

                    elif mc.nodeType(con) == 'parentConstraint':
                        drivers = mc.parentConstraint(cons, q=1, tl=1 )
                        mc.parentConstraint(drivers, world_ctrl, mo=1)
                        mc.delete(con)

                    elif mc.nodeType(con) == 'orientConstraint':
                        drivers = mc.orientConstraint(cons, q=1, tl=1 )
                        mc.orientConstraint(drivers, world_ctrl, mo=1)
                        mc.delete(con)

                    elif mc.nodeType(con) == 'scaleConstraint':
                        drivers = mc.scaleConstraint(cons, q=1, tl=1 )
                        mc.scaleConstraint(drivers, world_ctrl, mo=1)
                        mc.delete(con)

    for m in model_grp:
        utils.set_attrs(m, k=1, l=0)
        if mc.nodeType(m) in ['transform', 'joint']:
            try:
                mc.parentConstraint(offsets[-1], m, n=m+'_PRC', mo=1)
                mc.scaleConstraint(offsets[-1], m, n=m+'_sC', mo=1)
            except:
                pass

    shapes = utils.get_children(model_grp, ad=1, node_type='mesh',s=1)
    geo = [utils.get_transform(s) for s in shapes]

    cache_sel = name+'_'+str(1+len(mc.ls(name+'_*:*'))).zfill(2)+'_'+variant+'_cache_SEL'
    mc.sets(geo, n=cache_sel)

    mc.select(world_ctrl)

    print '##############################'
    print '# PropIt completed!\n'
    print '    Asset:   '+name
    print '    Variant: '+variant
