import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import env
from rigBot import rig

import commstd
from commstd import pipeline
import sgtk

tk = sgtk.platform.current_engine().sgtk

def build(assets, variants=[], publish=True, comment='', farm=False, check_model=True):

    if comment:
        comment += ' (Batch rig build)'
    else:
        comment = 'Batch rig build.'

    if type(assets) is not list:
        assets = [assets]

    for asset in assets:

        # set asset
        env.set_asset(asset)
        do_not_build = False

        # rebuild each variant save and publish stream
        rigbuild_path = env.get_rigbuild_path()
        commstd.change_context(rigbuild_path)
        context = commstd.current_context()

        latest = tk.shotgun.find_one("PublishedFile", [["entity", "is", context.entity], ["published_file_type", "name_is", "Maya Rig"]], ["version_number"], order=[{"field_name": "version_number", "direction": "desc"}])
        version = latest.get('version_number') + 1

        variant_names = get_sg_rig_variants(asset, variant_filter=variants)
        for variant in variant_names:
            build_rig_variant(asset, variant, comment, version, publish, farm, check_model)

def get_sg_rig_variants(asset, variant_filter=[]):

    # now we want to check if published rigs already exist for this asset, otherwise exclude from the build
    pf_context = commstd.pipeline.create_context(entity_type="Asset", entity=asset, task="rig")
    pf = pipeline.find_one_pf(pf_context, 'Maya Rig', asset)

    # If no pf is returned then there is no published model with that name
    if not pf:
        mc.warning('Cannot find published rig for: {0}. Skipping ...'.format(asset))
        return []

    # get variant
    variants = pipeline.find_alternatives(pf, vary_variant=True) or []
    variant_names = [v['sg_variant'] for v in variants]
    variant_names = [v for v in variant_names
                                    if v in env.get_asset_info(asset).get('rig_variants')+['primary']]

    for i, v in enumerate(variant_names):
        if v == 'primary':
            variant_names[i] = 'default'

    if variant_filter:
        variant_names = [v for v in variant_names if v in variant_filter]

    return variant_names

def get_model_version():
    cm = [c for c in mc.ls(type='cmContent') if mc.getAttr(c+'.type', asString=1) in ['Alembic Geometry', 'Maya Geometry']]
    if cm:
        return mc.getAttr(cm[0]+'.version')

def build_rig_variant(asset, variant, comment='', version=None, publish=False, farm=False, check_model=True):

    print '##################################################################'
    print '##################################################################'
    print '\nBUILDING RIG\n'
    print 'ASSET: '+asset
    print 'VARIANT: '+variant+'\n'
    print '##################################################################'
    print '##################################################################'
    print '\n'

    build_list = utils.import_module(asset+'_buildList', variant[0].upper()+variant[1:])
    build_list.build()

    comment += '\n\nModel version: {0}'.format(str(get_model_version()).zfill(3))

    if publish and version is not None:
        if variant == 'default':
            variant = 'primary'

        mc.addAttr('rig_SEL', ln='publishStream', dt='string')
        mc.addAttr('rig_SEL', ln='publishVariant', dt='string')
        mc.addAttr('rig_SEL', ln='publishVersion', dt='string')

        mc.setAttr('rig_SEL.publishStream', 'default', type='string')
        mc.setAttr('rig_SEL.publishVariant', variant, type='string')
        mc.setAttr('rig_SEL.publishVersion', str(version), type='string')

    passed_model_check = True
    if check_model:
        passed_model_check = check_model_naming_convention(asset, variant, v=False, farm=farm)

    if passed_model_check:
        v = variant
        if variant == 'primary':
            v = 'default'
        env.save_stream(v, workfile=0)

        if publish and version is not None:
            print '##################################################################'
            print '\nPUBLISHING RIG\n'
            commstd.publish(comment=comment)

        print '##################################################################'
        print '##################################################################'
        print '\nFINISHED BUILDING RIG\n'
        print 'ASSET: '+asset
        print 'VARIANT: '+variant+'\n'
        print '##################################################################'
        print '##################################################################'
        print '\n'

def check_model_naming_convention(asset=None, variant=None, v=True, farm=False):

    if asset is None:
        asset = env.get_asset()

    if variant is None:
        variant = env.get_variant()

    cm_nodes = [utils.get_transform(n) for n in mc.ls(type='cmContent')]
    geos = [utils.get_transform(s, ln=1) for s in utils.get_children(cm_nodes, ad=1, ln=1) if mc.nodeType(s) == 'mesh']
    geos = mc.ls(geos)

    bad_names = []

    for geo in geos:
        tokens = geo.split('|')[-1].split('_')
        if len(tokens) > 2:
            if not len(tokens[0]) == 11 or not len(tokens[-2]) == 4:
                bad_names.append(geo)
        else:
            bad_names.append(geo)

    bad_names = mc.ls(list(set(bad_names)))

    for g in bad_names:
        print '   '+g

    if bad_names:
        print '##################################################################'
        print '# BAD GEO NAMES FOUND\n'

        msg = 'We found some bad model node names, please kick this back.\n'
        msg += 'Here\'s a list of the problematic geo. You can also see this list in the script editor.\n\n'
        msg += 'ASSET: '+asset+'\n'
        msg += 'VARIANT: '+variant+'\n\n'

        for g in bad_names:
            msg += g+'\n'

        msg += '\nYou are my best friend ...'
        print msg

        if farm:
            raise

        else:
            mc.confirmDialog(title='Bad Geo Names Found', message= msg, button= 'OK', icon='critical')

    else:
        print '##################################################################'
        print '# Model names are all good! '

        if v:
            msg = 'This model is good to go! Go ahead and publish this guy.\n'
            mc.confirmDialog(title='Model Check Passed!', message= msg, button= 'OK')

        return True


