from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma
import maya.cmds as mc
import maya.mel as mm

import cPickle as pickle
import time
import os

from rigBot import utils
from rigBot.gui import remapDialog

file_extention = '.sdk'
deformer_type = 'animSDK'

def get_data(nodes=None, sdk_only=False):

    # get nodes
    if not nodes:
        nodes = mc.ls(sl=1)
    nodes = mc.ls(nodes)

    if not nodes:
        mc.warning('No nodes specified.')
        return

    # get list of keyed attrs and anim curves
    keyed_attrs = []
    anim_curves = []

    for node in nodes:

        # sdks only
        connections = mc.listConnections(node, s=1, d=0, type='animCurve', scn=1) or []
        for crv in connections:
            plug = mc.listConnections(crv+'.output', s=0, d=1, p=1, scn=1)

            if plug:
                plug = utils.strip_namespace(plug[0])

                is_sdk = mc.listConnections(crv+'.input', s=1, d=0, p=1, scn=1)
                if sdk_only and not is_sdk:
                    continue

                anim_curves.append(str(crv))
                keyed_attrs.append(str(plug))

        # bloend weighted sdks
        connections = mc.listConnections(node, s=1, d=0, type='blendWeighted', scn=1) or []
        for bw in connections:
            plug = mc.listConnections(bw+'.output', s=0, d=1, p=1, scn=1)
            crvs = mc.listConnections(bw, s=1, d=0, type='animCurve', scn=1) or []

            if plug:
                plug = utils.strip_namespace(plug[0])

            for crv in crvs:
                if plug:
                    is_sdk = mc.listConnections(crv+'.input', s=1, d=0, p=1, scn=1)
                    if sdk_only and not is_sdk:
                        continue

                    anim_curves.append(str(crv))
                    keyed_attrs.append(str(plug))

    # initialize data dict
    data = {}

    # for each curve get data
    for i, crv in enumerate(anim_curves):

        # get curve obj
        m_list = om.MSelectionList()
        m_list.add(crv)

        m_obj = m_list.getDependNode(0)
        crv_obj = oma.MFnAnimCurve(m_obj)

        # get sdk driver
        sdk_driver = mc.listConnections(crv+'.input', s=1, d=0, p=1, scn=1)
        if sdk_driver:
            sdk_driver = utils.strip_namespace(sdk_driver[0])

        # get basic crv info
        crv_type = crv_obj.animCurveType
        pre_infinity = crv_obj.preInfinityType
        post_infinity= crv_obj.postInfinityType
        is_weighted = crv_obj.isWeighted
        number_keys = int(crv_obj.numKeys)

        # declare list variables
        value_list = []
        time_list = []

        # tangent lists
        in_type_list = []
        in_angle_list = []
        in_weight_list = []

        out_type_list = []
        out_angle_list = []
        out_weight_list = []

        # get time, value and tangent info per key
        for ii in range(number_keys):

            key_input = crv_obj.input(ii)
            time = om.MTime(key_input)
            time = time.value

            time_list.append(time)
            value_list.append(crv_obj.value(ii))

            # api style tangent types
            in_type_list.append(crv_obj.inTangentType(ii))
            out_type_list.append(crv_obj.outTangentType(ii))

            # IN TANGENTS
            in_angle_weight = crv_obj.getTangentAngleWeight(ii, True)
            in_angle = om.MAngle(in_angle_weight[0]).value
            in_weight = in_angle_weight[1]

            in_angle_list.append(in_angle)
            in_weight_list.append(in_weight)

            # OUT TANGENTS
            out_angle_weight = crv_obj.getTangentAngleWeight(ii, False)
            out_angle = om.MAngle(out_angle_weight[0]).value
            out_weight = out_angle_weight[1]

            out_angle_list.append(out_angle)
            out_weight_list.append(out_weight)

        # create dict
        crv_data = {
            'name': crv,
            'crv_type': crv_type,
            'pre_infinity': pre_infinity,
            'post_infinity': post_infinity,
            'is_weighted': is_weighted,
            'time_list': time_list,
            'value_list': value_list,
            'in_type_list': in_type_list,
            'in_angle_list': in_angle_list,
            'in_weight_list': in_weight_list,
            'out_type_list': out_type_list,
            'out_angle_list': out_angle_list,
            'out_weight_list': out_weight_list,
            'sdk_driver': sdk_driver
        }

        if keyed_attrs[i] in data.keys():
            data[keyed_attrs[i]].append(crv_data)
        else:
            data[keyed_attrs[i]] = [crv_data]

    return data

def create_anim_crv(driven_attr, crv_type):

    # first get current keys  OR bw
    bw_connections = mc.listConnections(driven_attr, s=1, d=0, type='blendWeighted', scn=1) or []
    anim_connections = mc.listConnections(driven_attr, s=1, d=0, type='animCurve', scn=1) or []

    m_list = om.MSelectionList()
    m_list.add(driven_attr)
    plug = m_list.getPlug(0)

    if anim_connections:
        mc.disconnectAttr(anim_connections[0]+'.output', driven_attr)
        bw = mc.createNode('blendWeighted')
        mc.connectAttr(bw+'.output', driven_attr)
        mc.connectAttr(anim_connections[0]+'.output', bw+'.input[0]')

        m_list = om.MSelectionList()
        m_list.add(bw+'.input[1]')
        plug = m_list.getPlug(0)

    elif bw_connections:
        bw = bw_connections[0]
        count = len(mc.listConnections(bw+'.input', s=1, d=0, type='animCurve', scn=1) or [])

        m_list = om.MSelectionList()
        m_list.add('{0}.input[{1}]'.format(bw, count))
        plug = m_list.getPlug(0)

    crv = oma.MFnAnimCurve()
    crv.create(plug, crv_type)

    return crv

def set_data(data):

    for driven_attr, all_crv_data in data.items():
        if type(all_crv_data) is dict:
            all_crv_data = [all_crv_data]

        for crv_data in all_crv_data:
            test_attr = mc.ls(driven_attr)
            if not test_attr:
                mc.warning('Attribute does not exist: '+driven_attr)
                continue

            driven_attr = test_attr[0]

            # get all data'=
            name = crv_data.get('name') or driven_attr.replace('.','_')
            crv_type = crv_data.get('crv_type')
            pre_infinity = crv_data.get('pre_infinity')
            post_infinity = crv_data.get('post_infinity')
            is_weighted = crv_data.get('is_weighted')
            time_list = crv_data.get('time_list')
            value_list = crv_data.get('value_list')

            in_type_list = crv_data.get('in_type_list')
            in_angle_list = crv_data.get('in_angle_list')
            in_weight_list = crv_data.get('in_weight_list')

            out_type_list = crv_data.get('out_type_list')
            out_angle_list = crv_data.get('out_angle_list')
            out_weight_list = crv_data.get('out_weight_list')

            sdk_driver = crv_data.get('sdk_driver')

            # check if ther are keys to create
            if not len(value_list):
                continue

            '''
            # delete existing keys
            if len(all_crv_data) == 1:
                mc.cutKey(driven_attr)
                mm.eval('CBdeleteConnection "{0}";'.format(driven_attr))
            '''

            # create new crv obj
            crv = create_anim_crv(driven_attr, crv_type)
            crv_name = mc.rename(crv.name(), name)

            # set infinity and is weighted
            crv.setPreInfinityType(pre_infinity)
            crv.setPostInfinityType(post_infinity)
            crv.setIsWeighted(is_weighted)

            # create keys
            for i in range(len(time_list)):

                # try creating for UU type anim curves
                try:
                    crv.addKey(time_list[i], value_list[i], in_type_list[i], out_type_list[i])

                # try creating for TL TA and TU type anim curves
                except:
                    # try creating for ta tl and tu type anim curves
                    time = om.MTime(time_list[i])
                    crv.addKey(time, value_list[i], in_type_list[i], out_type_list[i])

                # Set tangent angle and weight
                in_angle = om.MAngle(in_angle_list[i])
                out_angle = om.MAngle(out_angle_list[i])

                crv.setTangent(i, in_angle, in_weight_list[i], True)
                crv.setTangent(i, out_angle, out_weight_list[i], False)

            # Connect SDK
            if sdk_driver:
                sdk_driver = mc.ls(sdk_driver)
                if sdk_driver:
                    mc.connectAttr(sdk_driver[0], crv_name+'.input')
                    print 'Connected SDK driver: '+sdk_driver[0]

            print 'Created keys for: '+driven_attr

def save(file_path, node, sdk_only=True, verbose=False):

        t = time.time()
        data = get_data(node, sdk_only=sdk_only)

        if not data:
            if verbose:
                mc.warning('No SDK to save for selected nodes!')
            return

        if not file_path.endswith(file_extention):
            file_path = os.path.splitext(file_path)[0]+file_extention


        utils.write_json(file_path, data)
        print time.time() - t

def load(file_path, remap=False, **kwargs):
    """Wrapper for importing weights"""

    def test_keys(keys):
        for k in keys:
            if not mc.objExists(k):
                return False
        return True


    # Load remaping dialog
    if remap:
        data = utils.read_json(file_path)

        if type(data) == dict:

            # get nodes to remap
            nodes = data.keys()
            remap_dialog = RemapSDK(nodes=nodes)
            remap_dialog.data = data
            remap_dialog.show()

            return

    # If not remap then load as usual
    else:
        data = utils.read_json(file_path)

        if not test_keys(data.keys()):
            # warn and skip if a remap is needed.
            mc.warning('Nodes need remapping! File path: {0}'.format(file_path))
        else:
            set_data(data)

class RemapSDK(remapDialog.RemapDialog):
    """Remap UI for remapping shape and influences during import"""

    def __init__(self, nodes=[], ignore_missing=True, label=''):
        remapDialog.RemapDialog.__init__(self, nodes, True, 'Set Driven Key Remap UI')

        self.ignore_missing_nodes = True
        self.data = {}

    def finish_command(self):
        """update data dict with new mapping and load the data"""

        # remap parent
        orig_nodes = self.data.keys()
        for orig_node in orig_nodes:
            new_node = self.mapping[orig_node] or orig_node

            if new_node != orig_node:
                self.data[new_node] = self.data[orig_node]
                del self.data[orig_node]

        set_data(self.data)

    def map_selection(self):
        """Map selectio nto node"""

        sel = mc.ls(sl=1)
        items = self.ui.node_tree.selectedItems() or []

        if items and sel:
            for item in items:

                node = item.text(0)
                new_node = sel[0]
                attrs = utils.get_selected_attrs(verbose=False)

                if attrs:
                    new_node += '.'+attrs[0]
                else:
                    new_node += '.'+node.split('.')[-1]

                if not mc.objExists(new_node):
                    mc.warning('Nothing selected!')
                    return

                item.setText(2, new_node)
                self.mapping[node] = new_node

        elif not sel:
            mc.warning('Nothing selected!')

def write_sdks(sdk_driven_items,
                base_path_to_dot_sdks):
    """
    Convenience function to write out sdks based on a list of joints
    or transforms.

    Variables:
    sdk_driven_items - a list of driven items(joints or transforms)
    base_path_to_dot_sdks - the base folder to save .sdk files into

    Example:
    from rigBot import utils
    from rigBot.data import sdk

    base_path_to_dot_sdks = "/job/comms/..."
    sdk_driven_items = mc.ls(sl = True)
    write_sdks(sdk_driven_items,
                    base_path_to_dot_sdks)

    """
    for sdk_driven_item in sdk_driven_items:
        mc.select(sdk_driven_item)
        sdk_file = os.path.join(base_path_to_dot_sdks, sdk_driven_item + ".sdk")
        sdk.save(file_path = sdk_file)
