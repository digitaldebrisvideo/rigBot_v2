import maya.cmds as mc
import maya.mel as mm

from rigBot import guide
from rigBot import utils
from rigBot import control
from rigBot import spaces
from rigBot import pickWalk
from rigBot import env
from rigBot import mocapHIK
from rigBot import data
from rigBot import constraint

from rigBot.data import udAttributes

import os
import time
import zipfile

if env.shotgun:
    try:
        from commstd import pipeline
        import commstd
    except:
        pass

def build(part_type=None, masters=[], all=True, use_plugin_nodes=None):
    """Build either a single rig part, all rig parts of a certain type
        OR all rigs parts in scnee

        Kwargs:
            :part_type: (str) Build all of this type. Default to None.
            :masters: (list) Build parts for only these part guides. Defaults to [].
            :all: (bool) Build all rig parts. Defaults to True.
            :use_plugin_nodes: (bool) Use cmRigNodes to build rig. Defaults to True."""

    if use_plugin_nodes in [True, 1]:
        os.environ['use_plugin_nodes'] = 'True'
    elif use_plugin_nodes in [False, 0]:
        os.environ['use_plugin_nodes'] = 'False'

    masters = mc.ls(masters)
    if not masters:
        guides_ref = mc.ls('guides_REF')
        if not guides_ref:
            mc.warning('Guide skel not found!')
            return

        all_masters = [c for c in utils.get_children(guides_ref[0])
                                            if mc.objExists(c+'.partType')]
        part_masters = []

        if part_type:
            for m in all_masters:
                if mc.getAttr(m+'.partType', asString=True) == part_type:
                    part_masters.append(m)

            masters = part_masters
            masters.sort()

        elif all:
            # reorder if global is not firstr
            for m in all_masters:
                if 'world' in m:
                    all_masters.remove(m)
                    all_masters.insert(0, m)

                if mc.getAttr(m+'.partType', asString=True) == 'foot':
                    all_masters.remove(m)
                    all_masters.append(m)

            masters = all_masters

    for master in masters:

        # skip masters if already built.
        if 'worldRoot' in master and mc.objExists('rig_GRP'):
            print 'Rig has already been built for: {0}. Skipping..'.format(master.replace('_REF', ''))
            continue

        print '\n############################################'
        print 'Building Part: '+master.replace('_REF', '')

        part = guide.instantiate_part(master=master, verbose=False)
        part.set_guide(master)
        part.build_rig()
        mc.refresh()

def build_mocap_root():
    """Builds mocap rot nodes out of a skelerton."""

    if not mc.objExists('skel_GRP'):
        raise RuntimeError('Skel_GRP not found!')

    if mc.objExists('guides_REF'):
        mc.delete('guides_REF')

    jnts = utils.get_children('skel_GRP', ad=1)
    mc.rename('skel_GRP', 'joints_GRP')
    mc.createNode('transform', n='rig_GRP')
    mc.parent('joints_GRP', 'rig_GRP')

    # create sets
    sets = ['rig_GRP']
    sets.append(create_cache_set())
    sets.append(mc.sets(jnts, n='bindJoints_SEL'))
    sets.append(mc.sets(jnts, n='control_SEL'))
    sets.append(mc.sets(jnts, n='engine_SEL'))

    mc.sets(sets, n='rig_SEL')

def build_mocap_rig(keep_fingers=False):
    """Build mocap skeleton.

        Kwargs:
            :keep_fingers: (bool) Keep finger joints in mocap rig: Defaults to False."""

    joints_to_keep = mc.ls('C_world_JNT',
                            'C_root_JNT',
                            'C_hip_JNT',
                            'C_torso_*_JNT',
                            'C_chest_JNT',
                            'C_neck_*_JNT',
                            'C_head_JNT',
                            'C_head_end_JNT',
                            '?_shoulder_JNT',
                            '?_upArm_JNT',
                            '?_loArm_JNT',
                            '?_wrist_JNT',
                            '?_wrist_end_JNT',
                            '?_upLeg_JNT',
                            '?_loLeg_JNT',
                            '?_ankle_JNT',
                            '?_ball_JNT',
                            '?_toe_JNT', type='joint')

    mc.select(mc.ls(type='joint'))
    mc.select(joints_to_keep, d=1)

    mm.eval('RemoveJoint')

    mocapHIK.create_mocap_rig_TPose()

def connect_rig():
    """Connect all you hook nodes. create spaces and remove guides ref
        This is a simple system wherte your parent node is stored in the
        hook driver attr and simply parent and scale constrained.

        Note: You can always modify the hook by hand. to set a new driver
            fine the "blah_blah_HOOK.hookDriver" attr and set a new parent node."""

    # Connect hooks to parent
    connect_hooks()

    # Create spaces
    create_spaces()

    # Loack and load attrs values and keyable settings
    '''
    # Done
    if mc.objExists('visibility_CTL'):
        mc.setAttr('visibility_CTL.allCtrlsVis', 1)
        mc.setAttr('visibility_CTL.offsetCtrlsVis', 0)
        mc.setAttr('visibility_CTL.jointsSelectable', 0)
        mc.setAttr('visibility_CTL.modelSelectable', 0)
        mc.setAttr('visibility_CTL.jointsVis', 0)
        mc.setAttr('visibility_CTL.modelVis', 1)
    '''

    mc.select(cl=1)
    print '\nFinalized rig.'

def connect_hooks():
    """Parent and scale constrain hooks to parents, connect vis attrs and hide noXform grps"""

    mc.refresh()

    if not mc.objExists('world_CTL'):
        return

    # Constrain ll hooks
    hook_node_attrs = mc.ls('*_'+utils.get_suffix('hook')+'.hookDriver')
    att_node_attrs = mc.ls('*_'+utils.get_suffix('attrDriver')+'.attrDriver')
    world_hook = mc.ls('*_worldRoot_*.allCtrlsVis')[0].split('.')[0]

    for attr in hook_node_attrs:
        print 'Connecting: '+attr

        driver = mc.ls(mc.getAttr(attr) or '')
        hook = attr.split('.')[0]

        if mc.getAttr(attr) and not driver:
            print ' \t***Cannot find driver for : '+attr

        if not driver:
            continue

        # remove any contraints
        utils.set_attrs(hook, 't r s', k=1, l=0)
        cons = utils.get_constraints(hook)
        if cons:
            mc.delete(cons)

        # create new contraints on HOOK
        if mc.objExists(hook+'.connectXforms'):
            mc.connectAttr(driver[0]+'.t', hook+'.t')
            mc.connectAttr(driver[0]+'.r', hook+'.r')
            mc.connectAttr(driver[0]+'.s', hook+'.s')

        else:
            constraint.constraint_mtx(driver[0], hook)
            #mc.parentConstraint(driver[0], hook, mo=1)
            #mc.scaleConstraint(driver[0], hook, mo=1)

    # connect vis attrs to world nod
    hook_parents = utils.get_children('parts_'+utils.get_suffix('transform'))
    world_node = mc.ls('world_CTL')
    vis_node = mc.ls('visibility_CTL')

    utils.set_attrs(world_node[0], 'worldScale', l=1, k=0)

    attrs = ['allCtrlsVis', 'offsetCtrlsVis', 'jointsVis', 'jointsSelectable']

    if hook_parents and world_node:
        for hook_parent in hook_parents:
            for attr in attrs:
                mc.connectAttr(vis_node[0]+'.'+attr, hook_parent+'.'+attr)

    # recreate any attrs from hook nodes onto driver nodes
    driven_hooks = [a.split('.')[0] for a in hook_node_attrs+att_node_attrs]
    hook_drivers = [mc.getAttr(a) or '' for a in hook_node_attrs+att_node_attrs]
    ignore = ['isRequired', 'hookDriver', 'worldScale']

    for i, hook in enumerate(driven_hooks):
        driver = hook_drivers[i]

        if mc.objExists(hook):

            # copy attrs from original leg ctrl to new foot ctrl
            data = udAttributes.get_data(hook)
            if not data:
                continue

            if 'worldScale' in data[hook]['data'].keys():
               del data[hook]['data']['worldScale']

            if 'worldScale' in data[hook]['attr_order']:
                data[hook]['attr_order'].remove('worldScale')

            data[driver] = data[hook]
            if hook != driver:
                del data[hook]

            udAttributes.set_data(data, verbose=False)

            #drive ik leg ctrl attrs with foot ctrl
            attrs = data[driver]['attr_order']
            for attr in attrs:
                if attr not in ignore:
                    try:
                        mc.connectAttr(driver+'.'+attr, hook+'.'+attr)
                    except:
                        pass

    utils.break_connections('C_worldRoot_GRP', 'allCtrlsVis')
    utils.set_attrs(hook_parents,  l=1, k=1)

    #hide no transforms
    mc.hide(mc.ls('noXform_'+utils.get_suffix('transform')))

def create_spaces():
    """Wrapper for creating spaces"""

    data.load('spaces')

    mc.refresh()
    spaces.build_all()

def create_skel_ref():
    """Creates a ref skel"""

    # skeel skel ref
    guide_ref = mc.ls('guides_REF')
    world_jnt = mc.ls('C_world_'+utils.get_suffix('joint')+'_REF')

    if world_jnt:

        grp = mc.group(world_jnt, n='skel_REF')
        mc.setAttr(grp+'.it', 0)
        mc.setAttr(grp+'.it', l=1)
        mc.parent(grp, utils.get_parent(guide_ref))
        mc.hide(grp)

    if guide_ref:
        mc.delete(guide_ref)

def save(variant='default', version='NEXT'):
    """Save a work version of the rig. NON shotgun only.

        Kwargs:
            :variant: (str) Rig variant. Defaults to "default".
            :version: (str, int) Version number. Defaults to "NEXT"."""

    if env.shotgun:
        mc.warning('This feature is not available in a shotgun environment.')

    else:
        env.save_stream('rig', token=variant, version=version, workfile=0)

def zip(variant='default', version='NEXT'):
    rig_file = env.save_stream('rig', token=variant, version=version, workfile=0)
    zip_file = '.'.join(rig_file.split('.')[:-1]) + '.zip'

    with zipfile.ZipFile(zip_file, 'w') as myzip:
        myzip.write(rig_file)
        print 'Zipped file: '+zip_file


def open_workfile(variant=None, version='LATEST'):
    """Wrapper for saving a rig workfile. NON shotgun only.

        Args:
            :variant: (None, str) Rig variant. Defaults to None.
            :version: (str, int) Version number. Defaults to "NEXT"."""

    if not env.get_asset():
        mc.warning('Asset not set! Set your asset with env.set_asset')
        return

    if variant is None:
        variant = env.get_variant()

    env.open_stream('rig', token=variant, version=version)

def save_workfile(variant=None, version='NEXT'):
    """Wrapper for saving a rig workfile. NON shotgun only.

        Kwargs:
            :variant: (None, str) Rig variant. Defaults to None.
            :version: (str, int) Version number. Defaults to "NEXT"."""

    if not env.get_asset():
        mc.warning('Asset not set! Set your asset with env.set_asset')
        return

    if variant is None:
        variant = env.get_variant()

    env.save_stream('rig', token=variant, version=version)

def revert_to_guides():
    """Revert a rig back to a guide rig."""

    # Now gather all guides in scene
    all_guides = [g.replace('.partType', '') for g in mc.ls('*.partType')]
    if not all_guides:
        mc.warning('No guides in scene!')
        return

    # get all part and build options
    part_types = []
    options = []

    for node in all_guides:
        part_types.append(mc.getAttr(node+'.partType'))
        options.append(eval(mc.getAttr(node+'.buildOptions')))

    # gather posoiton and control shape information
    zeros = [n.split('.')[0] for n in mc.ls('*.animZeroGrp')]
    ctrls = [n.split('.')[0] for n in mc.ls('*.animControl')]
    jnts = mc.ls('*_JNT', type='joint')

    jnt_pos = [utils.decompose_matrix(j) for j in jnts]
    zeros_pos = [utils.decompose_matrix(z) for z in zeros]
    ctrls_pos = [utils.decompose_matrix(c) for c in ctrls]
    shape_data = controlShapes.get_data()

    # check to make sure all data exists!
    if not zeros+ctrls+jnts or not shape_data:
        mc.warning('Cannot find nodes in this rig!')
        return

    # Scene check
    if not mm.eval('int $rtMelResult = `saveChanges("file -f -new")`;'):
        return

    # now rebuild the guides
    for i, part in enumerate(part_types):
        guide.build(part, **options[i])

    # place joints
    for i in range(len(jnts))*6:

        node = mc.ls(jnts[i]+'_PLC')
        pos = jnt_pos[i]

        if not node:
            continue

        node = node[0]
        if not mc.getAttr(node+'.rotateOrder', l=1):
            mc.setAttr(node+'.rotateOrder', l=pos[3])

        mc.xform(node, ws=1, t=pos[0])
        mc.xform(node, ws=1, ro=pos[1])

def remove_unused_jnts_from_scene():
    """Remove all unbound joints from scene"""

    skins = mc.ls(type='skinCluster')
    all_jnts = mc.ls(type='joint')
    inf_jnts = []

    for skin in skins:
        inf_jnts.extend(mc.skinCluster(skin, q=1, inf=1))
    inf_jnts = list(set(inf_jnts))

    unused_jnts = []
    for jnt in all_jnts:
        if jnt not in inf_jnts:
            unused_jnts.append(jnt)

    if 'C_world_JNT' in unused_jnts:
        unused_jnts.remove('C_world_JNT')
    mc.select(unused_jnts)
    mm.eval('RemoveJoint')

def unfinalize(namespace='*'):
    """
    Turn ON historical importance on all nodes in scene and make model,
    delete pickwalking controller tags and connections, and set joints to visible and selectable
    """

    utils.set_historical_importance(state=2)

    if namespace:
        namespace += ':'

    attrs = ['visibility_CTL.jointsVis',
            'visibility_CTL.modelVis',
            'visibility_CTL.modelSelectable',
            'visibility_CTL.jointsSelectable']

    attrs += [namespace+'visibility_CTL.jointsVis',
            namespace+'visibility_CTL.modelVis',
            namespace+'visibility_CTL.modelSelectable',
            namespace+'visibility_CTL.jointsSelectable']

    for attr in attrs:
        if mc.objExists(attr):
            mc.setAttr(attr, True)

    pickWalk.delete_tags()
    mp = utils.ModelPanel()

    mp.set_joints_vis(1)
    mp.set_jointXray_vis(1)

def finalize(fx_curves=False, world_locators=False, create_pref=True, namespace='*', ram=None, cpu=None):
    """
    Turn OFF historical importance on nodes, create pickwalking controller tags,
    and connections and turns off model selectability
    """

    if mc.objExists('dynamic_CTL'):
        if not mc.listAttr('dynamic_CTL', k=1):
            mc.delete('dynamic_CTL_ZERO')
            mc.setAttr('visibility_CTL_ZERO.tx', l=0)
            utils.break_connections('visibility_CTL_ZERO', 'tx')
            mc.setAttr('visibility_CTL_ZERO.tx', 0)
            mc.setAttr('visibility_CTL_ZERO.tx', l=1)

    chassis_jnt = mc.ls('*_chassisWorld_JNT')
    if mc.objExists('visibility_CTL_ZERO') and chassis_jnt:
        utils.set_attrs('visibility_CTL_ZERO', l=0)
        cons = utils.get_constraints('visibility_CTL_ZERO')
        if cons:
            mc.delete(cons)

        mc.parentConstraint(chassis_jnt[0], 'visibility_CTL_ZERO', mo=1)
        utils.set_attrs('visibility_CTL_ZERO')

    utils.set_historical_importance(state=0)

    if mc.objExists('guides_REF'):
        mc.delete('guides_REF')

    if mc.objExists('rig_GRP'):

        if not fx_curves and mc.objExists('fx_curve_GRP'):
            mc.delete('fx_curve_GRP')

        if mc.objExists('world_locator_GRP'):
            mc.delete('world_locator_GRP')

        if world_locators:
            utils.create_cfx_locators()

    if namespace:
        namespace += ':'

    # Rig cleanup
    attrs = ['visibility_CTL.jointsVis',
            'visibility_CTL.modelVis',
            'visibility_CTL.modelSelectable',
            'visibility_CTL.jointsSelectable']

    attrs += [namespace+'visibility_CTL.jointsVis',
            namespace+'visibility_CTL.modelVis',
            namespace+'visibility_CTL.modelSelectable',
            namespace+'visibility_CTL.jointsSelectable']

    for attr in attrs:
        if mc.objExists(attr):
            if 'visibility_CTL.modelVis' in attr or attr == 'visibility_CTL.modelVis':
                mc.setAttr(attr, True)
            else:
                mc.setAttr(attr, False)

    if ram and not cpu:
        cpu = 4
    elif cpu and not ram:
        ram = 16

    if ram and cpu and mc.objExists('cache_SEL'):
        mc.addAttr('cache_SEL', ln='cpu', at='long', dv=int(cpu))
        mc.addAttr('cache_SEL', ln='ram', at='long', dv=int(ram))

    if mc.objExists('cache_SEL'):
        set_swap_variant()

    pickWalk.create_tags()

    if mc.objExists('rig_GRP'):
        mc.parent('noXform_GRP', w=1)
        mc.parent('noXform_GRP', 'rig_GRP')

        if create_pref:
            if utils.check_clashing_node_names():
                raise RuntimeError('Successfully finished building rig, but cannot create pREF geo because there are clashing node names!')
            else:
                create_pref_geo()

def set_swap_variant():

    if not env.shotgun:
        return

    allsets = mc.ls('*cache_SEL', '*:*cache_SEL', type='objectSet')
    for sel in allsets:

        if mc.objExists(sel+'.switchVariant'):
            asset = env.get_asset()
            swap = mc.getAttr(sel+'.switchVariant')
            mc.setAttr(sel+'.switchVariant', l=False)

            if swap:
                pf_context = commstd.pipeline.create_context(entity_type="Asset", entity=asset, task="rig")
                pf = pipeline.find_one_pf(pf_context, "Maya Rig", asset)
                try:
                    items = pipeline.find_alternatives(pf, vary_variant=True)
                    variants = [v.get('sg_variant') for v in items]

                except:
                    v = env.get_variant()
                    if v == 'default':
                        v = 'primary'
                    variants = [v]

                if swap not in variants:
                    mc.warning('removing swap to variant: '+sel)
                    mc.setAttr(sel+'.switchVariant', '', type='string')

                else:
                    primary = env.get_asset_info(asset).get('primary_variant')
                    if primary:
                        if primary == 'default':
                            primary = 'primary'

                    if primary in variants and swap != primary:
                        mc.setAttr(sel+'.switchVariant', primary, type='string')

            mc.setAttr(sel+'.switchVariant', l=False)

def create_pref_geo(autoDelete=False):

    allPRefGrp=mc.ls('????_pRef_GRP','pRef_GRP')

    if allPRefGrp and not autoDelete:
        mc.warning('a pRef_GRP already exists.. skipping')
        return

    elif not allPRefGrp or (allPRefGrp and autoDelete):

        if allPRefGrp and autoDelete:
            mc.delete(allPRefGrp)

        allGeo = mc.ls(['*_GE?'])
        allGeoErrorList=[]

        # check to make sure there is no duplicate geo
        for geo in allGeo:
            if '|' in geo:
                allGeoErrorList.append(geo)

        if len(allGeoErrorList):
            print '####################################################'
            print 'The following geo is not uniquely named'
            for geo in allGeoErrorList:
                print '    '+geo

            print ''
            mc.error('Non unique names found in model! Please clean up model scene, so that all geometry has unique names.')

        cacheSets = mc.ls('*cache_SEL')
        if cacheSets:
            allGeo = mc.sets(cacheSets[0], q=1)

        if allGeo:
            prefGrp = mc.createNode('transform', name='pRef_GRP')
            mc.setAttr(prefGrp+'.v', 0)

            for geo in allGeo:
                geoDup = mc.duplicate(geo, n=geo.split('|')[-1]+'_REFERENCE', rr=1)[0]

                geoDupShape = mc.listRelatives(geoDup, s=1)
                shapeNum = len(geoDupShape)
                if shapeNum > 1:
                    geoDupShape_ni = mc.listRelatives(geoDup, ni=1, s=1)
                    if len(geoDupShape_ni) > 1:
                        mc.delete(geoDupShape_ni[1:])
                        geoDupShape_ni = mc.listRelatives(geoDup, ni=1, s=1)

                    for ds in geoDupShape[1:]:
                        if ds not in geoDupShape_ni:
                            mc.delete(ds)

                geoShape = mc.listRelatives(geo, s=1, f=1)

                # add attribute to geo so that we know it is a pRef
                mc.addAttr(geoDup,at='bool', ln='isPrefObject',k=False, dv=True)

                if geoShape:
                    geoShape = geoShape[0]

                dupShape = mc.listRelatives(geoDup, s=1, f=1)
                if dupShape:
                    dupShape = dupShape[0]

                if geoShape:
                    if not mc.isConnected(dupShape+'.message',geoShape+'.referenceObject'):
                        mc.connectAttr(dupShape+'.message',geoShape+'.referenceObject',f=1)
                        mc.parent(geoDup,prefGrp)
                        mc.setAttr(geoDup+'.template',1)

                    if cacheSets:
                        mc.sets(geoDup, add=cacheSets[0])

                else:
                    mc.warning('skipped '+geo+' could not find a shape node')

            noxform = mc.ls('noXform_GRP', 'nonScale_GRP')
            if noxform:
                mc.parent(prefGrp, noxform[0])

            return prefGrp

    else:
        mc.warning('found no geo in the scene, not making any pref objects')

def create_cache_set():

    # Create cache sel
    if not mc.objExists('cache_SEL'):
        mc.sets(em=1, n='cache_SEL')

    info = env.get_asset_info() or {}
    switch_variant = info.get('primary_variant') or 'default'

    if switch_variant:
        if  switch_variant == 'default':
            switch_variant = 'primary'

        if mc.objExists('cache_SEL'):
            if not mc.objExists('cache_SEL.switchVariant'):
                mc.addAttr('cache_SEL', ln='switchVariant', dt='string')
            mc.setAttr('cache_SEL.switchVariant', switch_variant, type='string')

    if mc.objExists('rig_SEL'):
        mc.sets('cache_SEL', add='rig_SEL')

    return 'cache_SEL'


def clear_cache():

    utd = mc.internalVar(utd=1)
    files = [os.path.join(utd, f) for f in os.listdir(utd) if f.endswith('_rig_cache.ma')]
    files = [f for f in files if os.path.isfile(f)]
    if files:
        for f in files:
            try:
                os.remove(f)
            except:
                mc.warning('Cannot remove file: '+f)


