import maya.cmds as mc

from rigBot import utils

import cPickle as pickle
import time
import os

deformer_type = 'lightLocators'
file_extention = '.locs'

def get_con_driver(node):
    cons = [c for c in utils.get_constraints(node) if mc.nodeType(c) in ['pointConstraint','parentConstraint']]
    drv = ''
    if cons:
        for c in cons:
            drv = list(set([x for x in mc.listConnections(c+'.target') if x != c]))
        if drv:
            drv = drv[0]
    return drv

def get_data():
    """Get deformation stack fro mnodes"""

    locs = [l.split('.')[0] for l in mc.ls('*.lightingLocator')]

    l_data = {}
    for l in locs:
        xforms = utils.decompose_matrix(l)[:2]
        drv = get_con_driver(l)

        l_data[l] = {'driver':drv, 'xforms':xforms}

    return l_data

def set_data(data):
    """Set deformation stack"""

    for name, dat in data.items():
        utils.create_light_locator(dat['driver'], xforms=dat['xforms'], full_name=name)

    return True

def save(file_path, **kwargs):
    """Wrapper for class export call, Can export multiple and
        prompts for file path"""
    t = time.time()

    data = get_data()

    if not data:
        mc.warning('Nothing to save!')
        return

    if not file_path.endswith(file_extention):
        file_path = os.path.splitext(file_path)[0]+file_extention

    utils.write_json(file_path, data)
    print time.time() - t

def load(file_path, **kwargs):
    """Wrapper for importing weights"""

    # If not remap then load as usual

    data = utils.read_json(file_path)
    result = set_data(data)

    # warn and skip if a remap is needed.
    if result is None:
        mc.warning('{0} needs remapping! File path: {1}'.format(data['node'], file_path))

