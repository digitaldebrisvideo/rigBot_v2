# -*- rigBot: part  -*-

import maya.cmds as mc
import maya.mel as mm

from functools import wraps
import re
import os

from rigBot import utils
from rigBot import control
from rigBot import rig
from rigBot import env

"""This is the master standard part, this needs to be inhertied in all other part modules"""

class StandardPart():
    """This is the standardPart module which is inherited by all other parts.
    You should not import this part on its own. It is only meant to be inherited."""

    def __init__(self):
        """Init function, stores the class name and the part type"""

        # declare standard variables that MUST exist.
        self.part_type = self.__class__.__name__
        self.part_type = self.part_type[0].lower() + self.part_type[1:]

        self.guide_master = ''
        self.ordered_arg_list = []
        self.options_info_dict = {}
        self.options = {}

        self.anim_ctrls = []
        self.bind_joints = []
        self.surfaces =  []
        self.placers = []

        self.prefix = None
        self.add_option('side')
        self.add_option('name')
        self.extra_ctrl_sets = []

        self.mirror_value = 1
        self.mirror_behavior = True

        if self.options.get('side') == 'R':
            self.mirror_value = -1

        self.fx_curves = []
        self.world_ctrl = 'C_world_CTL'
        self.hik_node = None
        self.part_master = None

        self.use_guides_plugin = False
        self.use_plugin = False

    def add_option(self, name, data_type='int', default=None, min=None, hidden=False, selectable=False,
                max=None, enum=None, required=False, rebuild_to_modify=False, tool_tip=None, lock=False):
        """Add build arguments to guide module.

            name = argument name, as well as attr name in guide master ctrl
            data_type = type of argument,

            Valid data types are:
                :int:
                :float:
                :bool:
                :enum: (stored as a string)
                :selection: (stored list formated as a string)
                :string:
                :hook: parent driver node (stored as a string)

            Kwargs:
                :default: default value
                :min: optional minimum value (applies only to int and float data_type) int OR float
                :max: optional maximum value (applies only to int and float data_type) int OR float
                :enum: string enum values (format as 'one:two:three')
                :required: specify wheterh the node must exist in the scene (Applies only to selection data_type) bool
                :rebuild_to_modify: Make attr uneditable after the guide has been built. bool
                :tool_tip: a longer description of the option (used for tool tip in UI) string
                :hidden: choose to hide in ui (still appears on guide master) bool"""

        if self.part_type == 'worldRoot' and data_type == 'hook':
            return

        if self.part_type == 'worldRoot' and name == 'side':
            default = 'C'

        if self.part_type == 'worldRoot' and name == 'name':
            default = ''

        if name == 'parent':
            data_type = 'hook'

        # Check if arg type is valid
        valid_types =['int',
                      'float',
                      'bool',
                      'enum',
                      'hook',
                      'selection',
                      'string']

        if data_type not in valid_types:
            print self.add_option.__doc__
            raise ValueError('# Arg type is not valid!')

        # force defaults if the arg name is "side"
        if name == 'side':
            data_type = 'enum'
            tool_tip = 'Side token for this rig part.'
            rebuild_to_modify = False
            enum = 'L:C:R:'

            if not default:
                default = 'L'

        # if name is a parent type then enforce this
        elif data_type == 'hook':
            rebuild_to_modify = False

            if required and not default:
                default ='C_root_JNT'

            if type(default) is list:
                default = default[0]

            if not default:
                default = ''

        # if the arg name is "name" then enforce defaults
        elif name == 'name':
            data_type = 'string'
            tool_tip = 'Optional name. Used as a naming prefix for all nodes in this part.'
            rebuild_to_modify = False

            if not default:
                default = ''
                if required:
                    default = 'myPart'

        # Some checks for enum tyoe
        if data_type == 'enum':
            if not enum:
                print self.add_option.__doc__
                raise ValueError('# Enum values must be specified when using the enum data_type!')

            elif type(enum) not in [str, unicode]:
                print self.add_option.__doc__
                raise ValueError('# Enum values must be of type string! ' +\
                                 'Values must be seperated by commas, ie. "foo:bar"')

            elif default not in enum:
                print self.add_option.__doc__
                raise ValueError('# Default value is not in specified enum values list!')

        if data_type == 'selection':
            if not default:
                default = []

        # build ui_label if not specified
        if not tool_tip:
            tokens = utils.split_camel_case(name)
            tool_tip = ' '.join(tokens).capitalize()+'.'

        # set arg data
        arg_data = {
            'data_type': data_type,
            'default': default,
            'min': min,
            'max': max,
            'enum': enum,
            'hidden': hidden,
            'required': required,
            'rebuild_to_modify': rebuild_to_modify,
            'tool_tip': tool_tip,
            'lock': lock,
            'selectable': selectable
        }

        if name in self.ordered_arg_list and name not in ['side','name','parent']:
            self.ordered_arg_list.remove(name)

        if name not in self.ordered_arg_list:
            self.ordered_arg_list.append(name)

        # save arg
        self.options[name] = default
        self.options_info_dict[name] = arg_data

        self.mirror_value = 1
        if self.options.get('side', 'C') == 'R':
            self.mirror_value = -1

    def set_guide(self, master='', clear=False):
        """Set the current guide master and update args from ctrl attrs."""

        if clear:
            name = self.options.get('name')
            side = self.options.get('side')
            self.prefix = utils.join_strings([side, name])
            self.anim_ctrls = []
            self.bind_joints = []
            self.surfaces =  []
            self.guide_master = ''

            for key, info in self.options_info_dict.items():
                self.options[key] = info.get('default')

            return

        if not master:
            master = ''

        # try from seletion
        if not master or not mc.objExists(master+'.partType'):
            selection = mc.ls(sl=1)

            # try from sleection and checking the ref nodes
            if selection:
                masters = [m.replace('.partType','') for m in mc.ls('*_REF.partType')]

                for m in masters:

                    jnts = mc.getAttr(m+'.JNTS')
                    for s in selection:
                        if s in jnts:
                            master = m
                            break

                    if master:
                        break

            if selection and not master:
                master = selection[0]

                hierarchy = utils.get_long_names(master).split('|')
                master = ''
                for node in hierarchy:
                    if mc.objExists(node+'.partType'):
                        master = node

        if master and not mc.objExists(master+'.partType'):
            master += '_REF'

        if not mc.objExists(master+'.partType'):
            mc.warning('guideMaster not specified. Exiting.')
            return

        # instatiatethe correct part class
        part_type = mc.getAttr(master+'.partType', asString=1)
        if self.part_type != part_type:
            mc.warning('The current guide is not of type: {0}. You need: {1}'.format(self.part_type, part_type))
            return

        for attr in self.options.keys():
            if mc.objExists(master+'.'+attr):
                if mc.addAttr(master+'.'+attr, q=1, at=1) == 'enum':
                    value = mc.getAttr(master+'.'+attr, asString=1)
                elif self.options_info_dict.get(attr)['data_type'] == 'selection':
                    value = eval(str(mc.getAttr(master+'.'+attr)))
                else:
                    value = mc.getAttr(master+'.'+attr)
                self.options[attr] = value

        side = self.options.get('side')
        name = self.options.get('name')
        side_enums = self.options_info_dict.get('side').get('enum').split(':')

        lock_state = mc.getAttr(master+'.side', l=1)
        mc.setAttr(master+'.side', l=0)
        mc.setAttr(master+'.side', side_enums.index(side))
        mc.setAttr(master+'.side', l=lock_state)

        lock_state = mc.getAttr(master+'.name', l=1)
        mc.setAttr(master+'.name', l=0)
        mc.setAttr(master+'.name', name, type='string')
        mc.setAttr(master+'.name', l=lock_state)

        self.prefix = utils.join_strings([side, name])
        self.guide_master = master

        self.mirror_value = 1
        if self.options['side'] == 'R':
            self.mirror_value = -1

        # store relevant nodes in object attr
        ctrls, jnts, surfs = [], [], []
        if mc.objExists(master+'_CTLS'):
            ctrls = mc.listRelatives(master+'_CTLS', ad=1, type='nurbsCurve') or []
            ctrls = [utils.get_parent(s) for s in ctrls]
            ctrls= [c for c in ctrls if mc.objExists(c+'.animControl')]
        else:
            ctrls = eval(mc.getAttr(master+'.CTLS') or '[]')

        if mc.objExists(master+'_JNTS'):
            jnts = mc.listRelatives(master+'_JNTS', ad=1, type='joint') or []
            jnts = [j.replace('_REF','', 1) for j in jnts]
            jnts.reverse()
        else:
            jnts = eval(mc.getAttr(master+'.JNTS'))

        if mc.objExists(self.guide_master+'_SURFS'):
            surfs = mc.listRelatives(master+'_SURFS', ad=1, type=['nurbsCurve', 'nurbsSurface']) or []

        else:
            try:
                v = mc.getAttr(master+'.SURFS')
                if v:
                    surfs = eval(v)
            except:
                surfs = []

        actual_ctrl_list = []
        for ctrl in ctrls:
            if ctrl not in actual_ctrl_list:
                actual_ctrl_list.append(ctrl)

        self.anim_ctrls = actual_ctrl_list
        self.bind_joints = jnts
        self.surfaces =  surfs

        self.create_option_attrs(self.guide_master)

        mc.setAttr(self.guide_master+'.CTLS', str(self.anim_ctrls), type='string')
        mc.setAttr(self.guide_master+'.JNTS', str(self.bind_joints), type='string')
        mc.setAttr(self.guide_master+'.SURFS', str(self.surfaces), type='string')

        return master

    def finalize_guide(self, extra_bind_jnts=[], extra_ctrl_sets=[]):
        """Post guide builde name check."""

        if mc.objExists(self.guide_master):
            name = self.options.get('name')

            try:
                if not utils.get_parent(self.guide_master):
                    mc.parent(self.guide_master, 'guides')
            except:
                pass

            if name.endswith('GUIDE'):
                new_name = name.split('GUIDE')[0]
                self.update_options_raw(name=new_name, force=1)

            if name.endswith('REBUILD'):
                new_name = name.split('REBUILD')[0]
                self.update_options_raw(name=new_name, force=1)

        if mc.objExists(self.guide_master+'_SURFS'):
            if mc.listRelatives(self.guide_master+'_SURFS'):
                ch = [c for c in utils.get_children(self.guide_master+'_SURFS', ad=1)
                            if mc.nodeType(c) in ['nurbsSurface', 'mesh', 'nurbsCurve']]

                for c in ch:
                    self.tag_as_ref(utils.get_transform(c))
                    print 'TAGGING SURF'

            else:
                mc.delete(self.guide_master+'_SURFS')
                if mc.objExists(self.guide_master+'.surfaceVis'):
                    mc.deleteAttr(self.guide_master+'.surfaceVis')


        if mc.objExists(self.guide_master):
            mc.select(self.guide_master)

        else:
            self.set_guide(clear=True)

        self.set_finalize_status("post_finalize")

    def create_option_attrs(self, ctrl=''):
        if not ctrl:
            ctrl = self.guide_master

        if not ctrl:
            return

        for arg in self.ordered_arg_list:
            arg_info = self.options_info_dict.get(arg)

            if not arg_info:
                continue

            data_type = arg_info['data_type']
            default = self.options.get(arg, arg_info['default'])

            if mc.objExists(ctrl+'.'+arg):
                continue

            # add bools args
            if data_type == 'bool':
                if default:
                    default = True
                mc.addAttr(ctrl, ln=arg, at='bool', dv=default, k=1)

            # add enum attrs
            elif data_type == 'enum':
                enum = arg_info['enum']
                if not enum:
                    print self.add_option.__doc__
                    raise ValueError('# Enum values are empty cannot continue! Module needs modification at addArg.')

                idx = 0
                if default and default in enum:
                    idx = enum.split(':').index(default)

                mc.addAttr(ctrl, ln=arg, at='enum', en=enum, dv=idx, k=1)

            # add string args (selection or string data_types)
            elif data_type in ['selection', 'string', 'parent', 'hook']:
                if default is None or type(default) not in [str, unicode]:
                    default = ''

                mc.addAttr(ctrl, ln=arg, dt='string', k=1)

            # add in and float args
            elif data_type in ['int', 'float']:
                vmin = arg_info['min']
                vmax = arg_info['max']

                if data_type == 'int':
                    data_type = 'long'

                if default is None or type(default) not in [float, int]:
                    if vmin:
                        default = vmin
                    else:
                        default = 0

                if vmin and vmax:
                    mc.addAttr(ctrl, ln=arg, at=data_type, k=1, min=vmin, max=vmax, dv=default)

                elif vmin:
                    mc.addAttr(ctrl, ln=arg, at=data_type, k=1, min=vmin, dv=default)

                elif vmax:
                    mc.addAttr(ctrl, ln=arg, at=data_type, k=1, max=vmax, dv=default)

                else:
                    mc.addAttr(ctrl, ln=arg, at=data_type, k=1, dv=default)

        # set defaults for string attrs
        for arg, arg_info in self.options_info_dict.items():
            data_type = arg_info['data_type']
            default = self.options.get(arg, arg_info['default'])

            if data_type in ['selection', 'string', 'hook']:
                try:
                    mc.setAttr(ctrl+'.'+arg, l=0)
                    mc.setAttr(ctrl+'.'+arg, default, type='string')
                except:
                    raise ValueError('# "{0}" is not a valid string. Cannot set attr default for: {1}'.format(default, arg))

    def create_guide_master(self, **kwargs):
        """Create master nodes for guide part"""

        if self.part_type == 'worldRoot':
            kwargs['name'] = ''
            kwargs['side'] = 'C'

        self.set_guide(clear=True)
        self.update_options_raw(**kwargs)

        # modify name for temp build
        side = self.options.get('side')

        if not self.options_info_dict['name']['required']:
            name = self.options.get('name')
        else:
            name = self.options.get('name') or self.part_type

        name = self.options.get('name')
        name += 'GUIDE'

        # create ctrl node and shape
        ctrl = utils.join_strings([side, name, self.part_type, 'guide'])

        if mc.objExists(ctrl):
            mc.warning('{0} exists! This should not be the case. Removing..'.format(ctrl))
            mc.delete(ctrl)

        # Create guides node
        if not mc.objExists('guides'):
            mc.createNode('transform', n='guides')
            mc.connectAttr('guides.sy', 'guides.sx')
            mc.connectAttr('guides.sy', 'guides.sz')
            mc.aliasAttr('MasterScale', 'guides.sy')
            mc.addAttr('guides', ln='guideMaster', at='message')
            utils.set_attrs('guides', 'sx sz v', k=0, l=1)
            utils.set_attrs('guides', 't r sy', k=0, cb=1)

        ctrl = mc.createNode('transform', n=ctrl)

        mm.eval('transformLimits -sy 0.01 1 -esy 1 0 '+ctrl)

        # connect part scale
        dmx = mc.createNode('decomposeMatrix', n=ctrl+'_dmx')
        mc.connectAttr(ctrl+'.worldMatrix', dmx+'.inputMatrix')

        dmx2 = mc.createNode('decomposeMatrix', n=ctrl+'_dmx')
        mc.connectAttr(ctrl+'.parentMatrix', dmx2+'.inputMatrix')

        # add display attrs
        mc.addAttr(ctrl, ln='guideMasterControl', at='message')
        mc.addAttr(ctrl, ln='_', at='enum', nn=' ', en=' ', k=1)
        mc.addAttr(ctrl, ln='jointPlacerVis', k=1, at='bool', dv=1)
        mc.addAttr(ctrl, ln='ctrlVis', k=1, at='bool', dv=1)
        mc.addAttr(ctrl, ln='ctrlAxisVis', k=1, at='bool', dv=0)
        mc.addAttr(ctrl, ln='jointAxisVis', k=1, at='bool', dv=0)
        mc.addAttr(ctrl, ln='surfaceVis', k=1, at='bool', dv=0)
        mc.addAttr(ctrl, ln='jointSelectable', k=1, at='bool', dv=0)
        mc.addAttr(ctrl, ln='__', nn='  ', at='enum', k=1, en=' ')
        mc.addAttr(ctrl, ln='placerXRayMode', k=1, at='bool', dv=1)
        mc.addAttr(ctrl, ln='placerOpacity', k=1, min=0.1, max=1, dv=0.8)
        mc.addAttr(ctrl, ln='placerSize', k=1, min=0.1, dv=1)

        mc.addAttr(ctrl, ln='worldScale', dv=1.0)
        mc.addAttr(ctrl, ln='jointOpacity', dv=1.0)
        mc.addAttr(ctrl, ln='placerScaleCompensate', at='bool', dv=0, k=1)
        mc.addAttr(ctrl, ln='guideMasterCtrl', at='message')

        mdl = mc.createNode('multDoubleLinear', n=ctrl+'_mdl')
        mc.connectAttr(ctrl+'.placerOpacity', mdl+'.i1')
        mc.connectAttr(mdl+'.output', ctrl+'.jointOpacity')
        mc.setAttr(mdl+'.i2', 1.0)

        mc.connectAttr(ctrl+'.sy', ctrl+'.sx')
        mc.connectAttr(ctrl+'.sy', ctrl+'.sz')
        mc.aliasAttr('globalScale', ctrl+'.sy')

        mc.connectAttr(dmx+'.outputScaleY', ctrl+'.worldScale')
        mc.setAttr(dmx+'.ihi', 0)
        mc.setAttr(mdl+'.ihi', 0)
        mc.setAttr(dmx2+'.ihi', 0)

        # Create group nodesi'
        ctrlGrp = mc.createNode('transform', p=ctrl, n=ctrl+'_CTLS')
        plcGrp = mc.createNode('transform', p=ctrl, n=ctrl+'_PLCS')
        jntGrp = mc.createNode('transform', p=ctrl, n=ctrl+'_JNTS')
        surfGrp = mc.createNode('transform', p=ctrl, n=ctrl+'_SURFS')
        noxform = mc.createNode('transform', p=ctrl, n=ctrl+'_NOX')

        mc.setAttr(jntGrp+'.overrideEnabled', 1)
        cnd = mc.createNode('condition', n=ctrl+'_cnd')

        mc.connectAttr(ctrl+'.jointSelectable', cnd+'.firstTerm')
        mc.setAttr(cnd+'.ihi', 0)
        mc.setAttr(cnd+'.secondTerm', 0)
        mc.setAttr(cnd+'.colorIfTrueR', 2)
        mc.setAttr(cnd+'.colorIfFalseR', 0)
        mc.connectAttr(cnd+'.outColorR', jntGrp+'.overrideDisplayType')

        mc.connectAttr(ctrl+'.jointPlacerVis', plcGrp+'.v')
        mc.connectAttr(ctrl+'.ctrlVis', ctrlGrp+'.v')
        mc.connectAttr(ctrl+'.jointPlacerVis', jntGrp+'.v')
        mc.connectAttr(ctrl+'.surfaceVis', surfGrp+'.v')

        mc.setAttr(jntGrp+'.it', 0)
        mc.setAttr(jntGrp+'.it', l=1)
        mc.setAttr(noxform+'.it', 0)
        mc.setAttr(noxform+'.it', l=1)
        mc.hide(noxform)

        mc.connectAttr(dmx2+'.outputScaleY', jntGrp+'.sx')
        mc.connectAttr(dmx2+'.outputScaleY', jntGrp+'.sy')
        mc.connectAttr(dmx2+'.outputScaleY', jntGrp+'.sz')

        # add build args
        num_attrs = len(self.ordered_arg_list)
        mc.addAttr(ctrl, ln='partType', at='enum', en=self.part_type, k=1)
        mc.addAttr(ctrl, ln='___', at='enum', nn=' ', en=': ', k=1)

        self.options['name'] = name

        self.create_option_attrs(ctrl)

        utils.set_attrs(ctrl, 'sx sz', k=0, l=1, cb=0)
        utils.set_attrs(ctrl, 'side name parent', k=0, l=0, cb=0)

        attrs = ['lpx', 'lpy', 'lpz', 'lsx', 'lsy', 'lsz',
         'clr', 'clg', 'clb', 'op', 'radi', 'size', 'dot',
         'is', 'ps', 'startMatrix', 'endMatrix']

        utils.set_attrs(ctrl, 'worldScale', k=0, l=1)

        # use plugin or create nurbs shape for guide
        if self.use_guides_plugin:

            shape = mc.createNode('cmJointShape', p=ctrl, n=ctrl+'Shape')

            mc.connectAttr(ctrl+'.placerSize', shape+'.size')
            mc.connectAttr(ctrl+'.placerXRayMode', shape+'.drawOnTop')
            mc.connectAttr(ctrl+'.placerOpacity', shape+'.opacity')
            mc.setAttr(shape+'.color', 0.22, 0.09, 0.5 )

            mc.connectAttr(ctrl+'.sy', shape+'.partScale')
            mc.connectAttr(ctrl+'.placerScaleCompensate', shape+'.inheritScale')
            mc.setAttr(ctrl+'.radi', 0.8)

            utils.set_attrs(shape, ' '.join(attrs), cb=0)
            utils.set_attrs(shape, ' '.join(attrs), k=0, l=1)
            utils.set_attrs(shape, 'clr clb clg', k=0, l=0)

        else:
            mc.addAttr(ctrl, ln='offsetTranslateX')
            mc.addAttr(ctrl, ln='offsetTranslateY')
            mc.addAttr(ctrl, ln='offsetTranslateZ')
            mc.setAttr(ctrl+'.displayHandle', 1)

            mc.connectAttr(ctrl+'.offsetTranslateX', ctrl+'.selectHandleX')
            mc.connectAttr(ctrl+'.offsetTranslateY', ctrl+'.selectHandleY')
            mc.connectAttr(ctrl+'.offsetTranslateZ', ctrl+'.selectHandleZ')

        # lock attrs for post build
        attrs = []
        for arg, info in self.options_info_dict.items():
            should_lock = info.get('rebuild_to_modify')
            if should_lock:
                attrs.append(arg)

        utils.set_attrs(ctrl, ' '.join(attrs), k=1, l=1)

        mc.addAttr(ctrl, ln='CTLS', dt='string')
        mc.addAttr(ctrl, ln='JNTS', dt='string')
        mc.addAttr(ctrl, ln='SURFS', dt='string')

        grps = [ctrlGrp, jntGrp, plcGrp, surfGrp, noxform]
        utils.set_attrs(grps, k=0, l=1)

        # parent and tag stuff
        mc.parent(ctrl, 'guides')
        mc.select(ctrl)

        self.guide_master = ctrl
        side = self.options.get('side')
        name = self.options.get('name')
        self.prefix = utils.join_strings([side, name])

        self.mirror_value = 1
        if self.options.get('side') == 'R':
            self.mirror_value = -1

        if self.part_type == 'worldRoot':
            mc.setAttr(self.guide_master+'.side', k=0, l=1)

        self.tag_finalize_status()
        self.set_finalize_status("pre_finalize")

        mc.parent(self.guide_master, w=1)
        mc.selectPriority(locator=9)

        return self.prefix, self.options

    def create_part_master(self):
        """
            Setups up part ctrls grp and part no xform grp, also updated ctrls list
            and joints list ..

            Returns:
                self.world_ctrl = TOP ctrl of the rig (use worldScale attr to drive scale)
                self.ctrls_grp = top ctrls grp for this part (parent all your ctrls here)
                self.nox_grp = parts noScale grp (parent non moving or scaling stuff here.)
                self.anim_ctrls = anim ctrls to be created (declared in guides)
                self.bind_joints = bind joints from guides
        """

        def create_hooks_heirarchy(hook, ctrl_node):
            """This create hook nctrls, jnts and no xform nodes PER hook node"""

            # prefix for new hook nodes
            prefix = hook.replace('HOOK', '', 1).replace('GRP', '', 1)

            # Create groups
            grp_name = utils.join_strings([prefix, 'CTLS'])
            ctrls_grp = mc.createNode('transform', n=grp_name, p=hook)

            grp_name = utils.join_strings([prefix, 'JNTS'])
            jnts_grp = mc.createNode('transform', n=grp_name, p=hook)

            grp_name = utils.join_strings([prefix, 'NOX'])

            # add and connect vis attrs
            mc.connectAttr(ctrl_node+'.allCtrlsVis', ctrls_grp+'.v')
            mc.connectAttr(ctrl_node+'.jointsVis', jnts_grp+'.v')

            # connect draw override on joint grp
            cnd = mc.createNode('condition', n=ctrl_node+'_cnd')
            mc.connectAttr(ctrl_node+'.jointsSelectable', cnd+'.firstTerm')
            mc.setAttr(cnd+'.ihi', 0)
            mc.setAttr(cnd+'.secondTerm', 0)
            mc.setAttr(cnd+'.colorIfTrueR', 2)
            mc.setAttr(cnd+'.colorIfFalseR', 0)
            mc.setAttr(jnts_grp+'.overrideEnabled', 1)
            mc.connectAttr(cnd+'.outColorR', jnts_grp+'.overrideDisplayType')

            # lock stuff
            utils.set_attrs([ctrls_grp, jnts_grp], 't r s it', l=1, k=0)
            utils.set_attrs(ctrl_node, 'worldScale', l=1, k=1)

            return ctrls_grp, jnts_grp

        side = self.options.get('side')
        name = self.options.get('name') or self.part_type

        # specific case for world root
        if self.part_type == 'worldRoot':
            name = 'worldRoot'

        self.prefix = utils.join_strings([side, name])

        world_ctrl = 'C_world_CTL'

        # create ctrls top
        if self.part_type == 'worldRoot':
            name = 'worldRoot'

        elif self.options_info_dict['name']['required']:
            name = self.options.get('name')

        else:
            name = utils.join_strings([self.options.get('name'), self.part_type])

        topnode_name = '{0}_{1}_GRP'.format(side, name)
        hook_prefix = '{0}_{1}'.format(side, name)

        parent_grp = 'parts_GRP'
        self.part_master = mc.createNode('transform', p=parent_grp, n=topnode_name)

        # Create master attrs
        mc.addAttr(self.part_master, ln='rigPart', at='message')
        mc.addAttr(self.part_master, ln='allCtrlsVis', k=1, at='bool', dv=1)
        mc.addAttr(self.part_master, ln='offsetCtrlsVis', k=1, at='bool', dv=1)
        mc.addAttr(self.part_master, ln='jointsVis', k=1, at='bool', dv=1)
        mc.addAttr(self.part_master, ln='jointsSelectable', k=1, at='bool', dv=1)

        # create hook grps and store parent
        self.hooks = []
        self.ctrl_grps = []
        self.jnt_grps = []

        if not name == 'worldRoot':
            noxform_grp = '{0}_{1}_NOX'.format(side, name)
            noxform_grp = mc.createNode('transform', n=noxform_grp, p='noXform_GRP')
            mc.setAttr(noxform_grp+'.it', 0)
            utils.set_attrs(noxform_grp, 't r s it', l=1, k=0)
            self.noxform_grp = noxform_grp

        for key in self.ordered_arg_list:
            value = self.options.get(key)
            data_type = self.options_info_dict[key].get('data_type')

            if data_type == 'hook':
                name = '{0}_{1}_HOOK'.format(hook_prefix, key)
                hook = mc.createNode('transform', n=name, p=self.part_master)

                mc.addAttr(hook, ln='hookDriver', dt='string')
                mc.setAttr(hook+'.hookDriver', str(value), type='string')
                mc.setAttr(hook+'.v', l=1, k=0)

                is_required = self.options_info_dict.get(key).get('required')
                mc.addAttr(hook, ln='isRequired', at='bool', dv=0)

                if is_required:
                    mc.setAttr(hook+'.isRequired', True)

                # create hook nodes here
                result = create_hooks_heirarchy(hook, self.part_master)

                self.hooks.append(hook)
                self.ctrl_grps.append(result[0])
                self.jnt_grps.append(result[1])

                # create global scale value
                dmtx = mc.createNode('decomposeMatrix', n=hook+'_dmtx')
                mc.addAttr(hook, ln='worldScale', k=1)
                mc.connectAttr(hook+'.worldMatrix', dmtx+'.inputMatrix')
                mc.connectAttr(dmtx+'.outputScaleY', hook+'.worldScale')
                mc.setAttr(hook+'.worldScale', l=1)

        if not self.hooks:
            # create hook nodes under part_master
            result = create_hooks_heirarchy(self.part_master, self.part_master)

            self.ctrl_grps.append(result[0])
            self.jnt_grps.append(result[1])

            # create global scale value
            dmtx = mc.createNode('decomposeMatrix', n=self.part_master+'_dmtx')
            mc.addAttr(self.part_master, ln='worldScale', k=1)
            mc.connectAttr(self.part_master+'.worldMatrix', dmtx+'.inputMatrix')
            mc.connectAttr(dmtx+'.outputScaleY', self.part_master+'.worldScale')
            mc.setAttr(self.part_master+'.worldScale', l=1)

        if not self.options_info_dict['name']['required']:
            name = self.options.get('name')
        else:
            name = self.options.get('name') or self.part_type

        # specific case for world root
        if self.part_type == 'worldRoot':
            name = 'worldRoot'

        mc.addAttr(self.part_master, ln='partType', dt='string', h=1)
        mc.setAttr(self.part_master+'.partType', self.part_type, type='string')
        mc.setAttr(self.part_master+'.partType', k=0, l=1)

        mc.addAttr(self.part_master, ln='buildOptions', dt='string', h=1)
        mc.setAttr(self.part_master+'.buildOptions', str(self.options), type='string')
        mc.setAttr(self.part_master+'.buildOptions', k=0, l=1)

        self.prefix = utils.join_strings([side, name])

    def create_ctrl_set(self, name, nodes=[], parent_set=None):

        side = self.options.get('side')
        part_name = self.options.get('name') or self.part_type
        prefix = utils.join_strings([side, part_name])
        set_name = '{0}_{1}_control_SEL'.format(prefix, name)
        new_set = ''

        if mc.objExists(set_name):
            if nodes:
                new_set = mc.sets(nodes, add=set_name)
        else:
            if nodes:
                new_set = mc.sets(nodes, n=set_name)
            else:
                new_set = mc.sets(em=1, n=set_name)

        if parent_set:
            mc.sets(new_set, add=parent_set)

        if new_set and new_set not in self.extra_ctrl_sets:
            self.extra_ctrl_sets.append(new_set)

        return new_set

    def finalize_part(self, extra_bind_jnts=[]):
        """Creates selections sets and updates ctrls and bind joints.

            Kwargs:
                :extra_bind_jnts: Any extra bind jointsthat may have been created"""

        extra_ctrl_sets = self.extra_ctrl_sets

        side = self.options.get('side')
        name = self.options.get('name') or self.part_type
        prefix = utils.join_strings([side, name])

        # get all ctrls from part grp
        ctrls = self.anim_ctrls
        for ctrl_grp in mc.ls(self.ctrl_grps):
            ctrls.extend(utils.get_children(ctrl_grp, ad=1))

        ctrls = [c for c in ctrls if mc.objExists(c+'.animControl')]
        ctrls = [c for c in ctrls if utils.get_shapes(c)]

        off_ctrls = [c for c in ctrls if mc.objExists(c+'.animOffsetControl')]
        off_ctrls = [c for c in off_ctrls if utils.get_shapes(c)]

        # Create ctrls sets
        self.ctrl_set = mc.sets(ctrls, n=prefix+'_control_SEL')
        if extra_ctrl_sets:
            mc.sets(extra_ctrl_sets, add=self.ctrl_set)

        ctrl_set = 'control_SEL'
        if not mc.objExists(ctrl_set):
            mc.sets(self.ctrl_set, n=ctrl_set)
        else:
            mc.sets(self.ctrl_set, add=ctrl_set)

        cache_set = rig.create_cache_set()

        # Create bind joint set
        jnts = mc.ls(self.bind_joints)
        jnts.extend(extra_bind_jnts)

        self.jnts_set = mc.sets(jnts, n=prefix+'_joints_SEL')

        world_jnt_set = 'bindJoints_SEL'
        if not mc.objExists(world_jnt_set):
            mc.sets(self.jnts_set, n=world_jnt_set)
        else:
            mc.sets(self.jnts_set, add=world_jnt_set)

        # Create top rig sel
        world_set = 'rig_SEL'

        nodes = mc.ls(['rig_GRP', world_jnt_set, ctrl_set, cache_set])

        if not mc.objExists(world_set):
            mc.sets(nodes, n=world_set)
        else:
            mc.sets(nodes, add=world_set)

        # everything under ctrl grps that is not a ctrl
        for grp in self.ctrl_grps:
            nodes = utils.get_children(grp, ad=1)
            nodes = [n for n in nodes if not mc.objExists(n+'.animControl')]
            nodes = [n for n in nodes if not n.endswith('_MOCAP')]
            nodes = [n for n in nodes if not n.endswith('_OFF')]
            utils.set_attrs(nodes, l=1, k=0)

            nodes = utils.get_children(grp, ad=1)
            nodes = [n for n in nodes if n.endswith('_MOCAP') or n.endswith('_OFF')]
            utils.set_attrs(nodes, 's v', l=1, k=0)

        # Delete empty extra control and jnts groups
        ctrl_grps = self.ctrl_grps
        jnt_grps = self.jnt_grps

        for node in ctrl_grps+jnt_grps:
            if not utils.get_children(node):
                mc.delete(node)

        print "Finalizing part."
        self.set_finalize_status("post_finalize")

    def update_options(self, master='', verbose=True, **kwargs):
        """Update any options that may have been set at guide build time.

            Note: Some options are designated to be locked after a guide build.
                  If you wish to modify those the use rebuild_guide() and pass in new options.

        """

        if self.part_type == 'worldRoot':
            mc.warning('Cannot modify root part!')
            return

        for key, value in kwargs.items():
            if self.options_info_dict[key]['lock']:
                del kwargs[key]

                if verbose:
                    mc.warning('"{0}" option is locked and cannot be modified.'.format(key))

        self.update_options_raw(master, **kwargs)

    def update_options_raw(self, master='', rename_master=True, clear=False, set_default=False, force=False, **kwargs):
        """Update part args.

            Note: Updating hte side or name token renames the guide node hierarchy"""

        for key in kwargs.keys():
            if not key in self.ordered_arg_list:
                mc.warning('Key: %s is not a valid options.. skipping.' % key)
                del kwargs[key]

        if clear:
            for arg, info in self.options_info_dict.items():
                self.options[arg] == info.get('default')
                self.set_guide(clear=True)
            return

        if not master:
            master = self.guide_master

        old_side = self.options.get('side')
        old_name = self.options.get('name')

        for arg, value in kwargs.items():
            if arg in self.options_info_dict.keys():

                if master:
                    should_lock = self.options_info_dict.get(arg).get('rebuild_to_modify')
                    if should_lock and not force:
                        result = mc.confirmDialog(title='Rebuild Required To Mirror',
                                        message='This arg is locked after the guide has been built.\n' +\
                                        'You must rebuild this part to update this option.\n\n' +\
                                        'Do you want to rebuild {0}?'.format(master),
                                        button=['Rebuild','Cancel'], defaultButton='Rebuild',
                                        cancelButton='Cancel', dismissString='Cancel', icon='warning')

                        if result == 'Rebuild':
                            self.rebuild_guide(**kwargs)
                        else:
                            mc.warning('Rebuild canceled.')
                            return

                    lock_state = mc.getAttr(master+'.'+arg, l=1)
                    mc.setAttr(master+'.'+arg, l=0)

                if arg == 'name':
                    value = utils.clean_name(value)

                if self.options_info_dict.get(arg).get('data_type') == 'hook':
                    if type(value) is list:
                        value = str(value[0])

                    value = value.replace('_PLC', '', 1)

                    # check is parent node is under its own herarchy
                    if value in utils.get_children(master, ad=1):
                        mc.warning('Cannot parent a guide to one of its children!')
                        return

                data_type = self.options_info_dict.get(arg).get('data_type')


                if data_type == 'hook':
                    if type(value) is list:
                        value = str(value[0])

                # validate arg types
                elif data_type == 'enum':
                    enums = self.options_info_dict.get(arg).get('enum').split(':')
                    if not value in enums:
                        raise ValueError('# {0} is not valid! Options for {1} are: {2}'.format(value, arg, enums))

                elif data_type == 'float':
                    try:
                        value = float(value)
                    except:
                        raise ValueError('# {0} is not valid for {1}! Must be a float'.format(value, arg))

                elif data_type == 'int':
                    try:
                        value = int(value)
                    except:
                        raise ValueError('# {0} is not valid for {1}! Must be a int'.format(value, arg))

                elif data_type == 'bool':
                    try:
                        value = bool(value)
                    except:
                        raise ValueError('# {0} is not valid for {1}! Must be a bool'.format(value, arg))

                elif data_type == 'string':
                    try:
                        value = str(value)
                    except:
                        raise ValueError('# {0} is not valid for {1}! Must be a string'.format(value, arg))

                elif data_type == 'selection':
                    if type(value) is not list:
                        value = [value]

                # Set args on guide master ctrl
                if mc.objExists(master):
                    if data_type in ['selection', 'string', 'hook']:
                        mc.setAttr(master+'.'+arg, value, type='string')

                    elif data_type == 'enum':
                        idx = enums.index(value)
                        mc.setAttr(master+'.'+arg, idx)

                    else:
                        mc.setAttr(master+'.'+arg, value)

                # set arg
                self.options[arg] = value
                if set_default:
                    self.options_info_dict[arg]['default'] = value

                if master:
                    mc.setAttr(master+'.'+arg, l=lock_state)

        if not mc.objExists(master):
            return

        # Get all attrs values from ctrl to make sure everythings in sync
        if rename_master:
            new_side = self.options.get('side')
            new_name = self.options.get('name')

            master = self.__rename_guide(old_side, old_name, new_side, new_name)

        if master:
            self.set_guide(master)

        self.mirror_value = 1
        if self.options['side'] == 'R':
            self.mirror_value = -1

        self.prefix = utils.join_strings([self.options.get('side'), self.options.get('name')])

    def __rename_guide(self, old_side, old_name, new_side, new_name):
        """Renames the hierarchy top reflect new side and or part name."""

        master = self.guide_master
        if not mc.objExists(master):
            return

        new_prefix = utils.join_strings([new_side, new_name])+'_'
        old_prefix = utils.join_strings([old_side, old_name])+'_'

        # check names
        if new_prefix == old_prefix:
            return master

        nodes = mc.listRelatives(master, ad=1, f=1)
        nodes.append(mc.ls(master, l=1)[0])

        if 'GUIDE' in old_prefix or 'REBUILD' in old_prefix or old_name:
            nodes.extend([n for n in mc.ls(old_prefix+'*', l=1) if n not in nodes])

        label = master.replace('GUIDE', '').replace('REBUILD', '')
        label = re.sub('_+', '_', label)

        nodes = [n for n in nodes if '|' in mc.ls(n, l=1)[0]]
        succeeded, new_side, new_name, new_names = checkNewArgs(
                                                old_side, old_name,
                                                new_side, new_name, nodes, label=label)
        if not succeeded:
            if 'GUIDE' in master or 'REBUILD' in master:
                mc.delete(master)
                self.update_options_raw(clear=True)
                mc.warning('Guide build was canceled by user.')
                return

            else:
                self.update_options_raw(rename_master=False, side=old_side, name=old_name, force=True)
                mc.warning('Args update was canceled by user.')
                return

        # if everything passes proceed to rename nodes
        mc.select(master)
        if new_names and len(nodes) == len(new_names):
            for i, node in enumerate(nodes):
                if mc.objExists(node):
                    mc.rename(node, new_names[i])

            master = mc.ls(sl=1)[0]
            self.update_options_raw(master=master, rename_master=False, side=new_side, name=new_name, force=True)
            return master

    def guide_joint(self, name='', placer_only=False, constraint_type='parent', alt_prefix=''):
        """This creates a guide rig joint and joint placer ctrl.

            Kwargs:
                name = name token for joint
                placer_only = only create a placer without a joint
                constraint_type = options are: "point" "orient", "parent"
        """

        if alt_prefix:
            prefix = alt_prefix

        else:
            prefix = self.prefix

        master = self.guide_master

        if not master:
            raise RuntimeError('# This object has not guide master assigned!')

        # get joint unique name
        jnt_name = utils.join_strings([prefix, name, '#', 'JNT'])
        ctrl = jnt_name+'_PLC'
        ctrl = utils.get_unique_name(ctrl)
        jnt_name = ctrl.replace('_PLC','', 1)

        zero = utils.join_strings([ctrl, 'ZERO'])
        zero = mc.createNode('transform', n=zero)
        ctrl = mc.createNode('joint', n=ctrl, p=zero)

        control.set_color('cobalt', ctrl)
        mc.setAttr(ctrl+'.radius', 3.0)
        mc.parent(zero, master+'_PLCS')

        attrs = ['lpx', 'lpy', 'lpz', 'lsx', 'lsy', 'lsz',
                 'lw',  'sizeMult', 'ijs' 'clr', 'clg', 'clb', 'op', 'radi',
                 'size', 'dot', 'is', 'ps', 'startMatrix', 'endMatrix']

        mc.setAttr(ctrl+'.ds', 2)

        result = [zero, ctrl]

        mc.addAttr(ctrl, ln='offsetTranslateX')
        mc.addAttr(ctrl, ln='offsetTranslateY')
        mc.addAttr(ctrl, ln='offsetTranslateZ')

        mc.addAttr(ctrl, ln='color', usedAsColor=1, at='float3', k=1)
        mc.addAttr(ctrl, ln='colorR', at='float', k=1, p='color')
        mc.addAttr(ctrl, ln='colorG', at='float', k=1, p='color')
        mc.addAttr(ctrl, ln='colorB', at='float', k=1, p='color')

        mc.setAttr(ctrl+'.overrideEnabled', 1)
        mc.setAttr(ctrl+'.overrideRGBColors', 1)
        mc.connectAttr(ctrl+'.color', ctrl+'.overrideColorRGB')

        mc.setAttr(ctrl+'.color', 0.05, 0.1, 0.25)
        if placer_only:
            mc.setAttr(ctrl+'.color', 0.045, 0.32, 0.79)

        mc.connectAttr(ctrl+'.offsetTranslateX', ctrl+'.selectHandleX')
        mc.connectAttr(ctrl+'.offsetTranslateY', ctrl+'.selectHandleY')
        mc.connectAttr(ctrl+'.offsetTranslateZ', ctrl+'.selectHandleZ')

        mc.setAttr(ctrl+'.displayHandle', 1)
        mc.setAttr(ctrl+'.radius', 1)
        mc.setAttr(ctrl+'.ds', 1)

        if not placer_only:

            jnt_ref = mc.createNode('joint', n=jnt_name)

            mc.setAttr(jnt_ref+'.radius', 1)
            mc.parent(jnt_ref, master+'_JNTS')

            result.append(jnt_ref)

            mc.connectAttr(master+'.jointAxisVis', jnt_ref+'.displayLocalAxis')

            if constraint_type == 'orient':
                mc.orientConstraint(ctrl, jnt_ref, n=jnt_ref+'_oc', mo=0)

            elif constraint_type == 'parent':
                mc.parentConstraint(ctrl, jnt_ref, n=jnt_ref+'_prc', mo=0)

            elif constraint_type == 'point':
                mc.pointConstraint(ctrl, jnt_ref, n=jnt_ref+'_pc', mo=0)

        utils.set_attrs(ctrl, 's v', k=0, l=1)

        mc.setAttr(ctrl+'.color',  k=0, cb=0, l=0)
        mc.setAttr(ctrl+'.colorR', k=0, cb=0, l=0)
        mc.setAttr(ctrl+'.colorG', k=0, cb=0, l=0)
        mc.setAttr(ctrl+'.colorB', k=0, cb=0, l=0)

        mc.select(zero)

        return result

    def guide_joint_chain(self, name='', num_joints=5, flat_plc_hierarchy=True, flat_jnt_hierarchy=False,
                         length=None, constraint_type='aim', placer_only=False, no_mirror=False, alt_prefix='', alt_iterate='letter'):
        """Create a chain of guide joints.

            Kwargs:
                name = name of chain
                num_joints = number of joints to build
                flat_plc_hierarchy = flatten the placer hierarchy VS an fk style parenting
                flat_jnt_hierarchy = flatten the joint hierarchy VS an fk style parenting
                length = initial length of the chain
                constraint_type = how to constrain the ref joint (options are: 'aim','point','orient','parent')
                placer_only = dont createa joint only a placer
        """

        zeros = []
        jnts = []
        jnt_refs = []

        v = self.mirror_value
        if no_mirror:
            v = 1

        if not length:
            length = num_joints - 1

        div = float(length) / (num_joints-1.0)

        for i in range(num_joints):
            letter = utils.letters[i]
            if alt_iterate == 'number':
                if i < 10:
                    letter='0'+str(i+1)
                else:
                    letter=str(i+1)

            jnt_name = name+'_'+letter

            if placer_only:
                zero, jnt = self.guide_joint(jnt_name, placer_only=True, constraint_type=constraint_type, alt_prefix=alt_prefix)

            else:
                zero, jnt, jnt_ref = self.guide_joint(jnt_name, placer_only=False, constraint_type=constraint_type, alt_prefix=alt_prefix)

                if not flat_jnt_hierarchy and jnt_refs:
                    mc.parent(jnt_ref, jnt_refs[-1])

                jnt_refs.append(jnt_ref)

            mc.xform(zero, ws=1, t=[div*i+1, 0, 0])
            if self.mirror_value == -1:
                mc.xform(zero, r=1, ro=[0, 0, 180])

            if not flat_plc_hierarchy and jnts:
                mc.parent(zero, jnts[-1])

            zeros.append(zero)
            jnts.append(jnt)

        if not placer_only:
            if constraint_type == 'aim':
                for i, jnt_ref in enumerate(jnt_refs[:-1]):
                    mc.pointConstraint(jnts[i], jnt_ref)
                    mc.aimConstraint(jnts[i+1], jnt_ref, aim=[v,0,0], u=[0,1,0],
                                     wu=[0,1,0], wuo=jnts[i], wut='objectRotation')
                mc.pointConstraint(jnts[-1], jnt_refs[-1])

        if placer_only:
            return zeros, jnts
        else:
            return zeros, jnts, jnt_refs

    def guide_ctrl(self, name='', shape='cube', color='yellow', scale=[1,1,1],
                        axis='Y', driver=None, constraint_type='parent', create_pivot=True, allow_offset_ctrls=True, alt_prefix=''):
        """This createsa guide rig anim control refernce.

            Kwargs:
                name = name of the control
                shape = shape of ctrl
                color = color of the ctrl
                scale = inital scale of ctrl
                axis = axis ctrl points
                driver = the node the ctrl will be constrained to
                constraint_type = options are: 'point','orient','parent'
                create_pivot = create a pivot ctrl to allow pivot modification at build time
                allow_offset_ctrls = allow for the option to build offset ctrls
        """

        if shape.lower() not in control.shapes:
            mc.warning('Shape is not valid!')

        master = self.guide_master
        side = self.options.get('side')
        part_name = self.options.get('name')

        if not master:
            raise RuntimeError('# This object has not guide master assigned!')

        # Create ctrl
        if alt_prefix:
            name = utils.join_strings([alt_prefix, name])
        else:
            name = utils.join_strings([self.prefix, name])

        result = control.create(name=name,
                                shape=shape,
                                color=color,
                                scale=scale,
                                axis=axis,
                                match_position=driver)

        zero, ctrl = result[0], result[-1]

        if allow_offset_ctrls:
            offset_ctrls = control.create_offset_ctrls(ctrl, 4)
            mc.addAttr(ctrl, ln='numOffsetCtrls', min=0, max=4, k=1, at='short')

        mc.addAttr(ctrl, ln='mirrorMode', at='enum', en='translateRotate:rotateOnly', k=1)

        # create pivot
        base_name = ctrl.replace('CTL', '', 1)
        piv_name = utils.join_strings([base_name, 'PIV_CTL'])

        pivot = utils.get_parent(ctrl)
        pivot = mc.rename(pivot, piv_name)
        utils.set_attrs(pivot, 'v', k=0, l=1)

        attrs = ['lpx', 'lpy', 'lpz', 'lsx', 'lsy', 'lsz',
                 'op', 'lw', 'size', 'sizeMult', 'dot', 'ijs']

        mc.addAttr(pivot, ln='animControlPivot', at='message')
        mc.deleteAttr(pivot+'.animOffsetGrp')

        if self.use_guides_plugin:
            shape = mc.createNode('cmPivotShape', n=pivot+'Shape', p=pivot)
            mc.connectAttr(master+'.ctrlAxisVis', shape+'.v')
            mc.setAttr(shape+'.inheritJointSize', 0)
            mc.setAttr(shape+'.opacity', .5)
            utils.set_attrs(shape, ' '.join(attrs), cb=0)
            utils.set_attrs(shape, ' '.join(attrs), k=0, l=1)

        else:
            control.create_shape('axis', ctrls=pivot)
            shapes = utils.get_shapes(pivot)
            control.set_color('red', shapes[0])
            control.set_color('green', shapes[1])
            control.set_color('blue', shapes[2])

            for shape in shapes:
                mc.connectAttr(master+'.ctrlAxisVis', shape+'.v')

        mc.parent(zero, master+'_CTLS')

        if not create_pivot:
            utils.set_attrs(pivot, k=0, l=1)

        if driver and mc.objExists(driver):
            if constraint_type == 'orient':
                mc.orientConstraint(driver, zero, n=ctrl+'_oc')

            elif constraint_type == 'point':
                mc.pointConstraint(driver, zero, n=ctrl+'_oc')

            else:
                mc.parentConstraint(driver, zero, n=ctrl+'_pc')

        if allow_offset_ctrls:
            for i, offset in enumerate(offset_ctrls):

                cnd = mc.createNode('condition', n=offset+'_cnd')
                mc.connectAttr(ctrl+'.numOffsetCtrls', cnd+'.firstTerm')

                mc.setAttr(cnd+'.secondTerm', i+1)
                mc.setAttr(cnd+'.operation', 3)
                mc.setAttr(cnd+'.colorIfTrueR', 1)
                mc.setAttr(cnd+'.colorIfFalseR', 0)

                mc.setAttr(offset+'.v', l=0)
                mc.connectAttr(cnd+'.outColorR', offset+'.v', f=1)
                mc.setAttr(offset+'.v', l=1)
                mc.setAttr(cnd+'.ihi', 0)

            mc.deleteAttr(ctrl+'.offsetCtrlVis')

        return zero, ctrl

    def anim_ctrl(self, name, match_position='', num_offset_ctrls=None, inherit_scale=False, node_type='transform', ref_shape=None):
        """Based on the name this creates a ctrl referencing the guide ctrl.

            Kwargs:
                name = name token of the ctrl (no need to include the prefix OF do if you like)
                match_position = nodeto match the pivot postion (guide pivot pos will be used if nothig is specified)
                num_offset_ctrls = override how many offset ctrls you want, default referes to guide settings
                inherit_scale = if the guide pivot was scaled this will inherit the scale from that guide pivot,
                                otherwise it will only inherit its mirrored behavior
        """

        if mc.objExists(name+'.animOffsetControl'):
            return

        if ref_shape:
            ref_name = ref_shape

        else:
            ref_name = name+'_REF'

        if not mc.objExists(ref_name):
            raise ValueError(ref_name+' does not exist!')

        # get pivot
        if not mc.objExists(match_position):
            match_position = utils.get_parent(ref_name)

        # get rotate order
        rotate_order =mc.getAttr(ref_name+'.rotateOrder')

        # build ctrl
        result = control.create(name=name,
                                match_shape=ref_name,
                                node_type=node_type,
                                match_position=match_position)

        zero, ctrl = result[0], result[-1]

        # Either inherit the scale from the pivot ref node
        if inherit_scale:
            mc.delete(mc.scaleConstraint(match_position, zero))

        # OR only set whether is it scaled by -1
        else:
            if mc.getAttr(match_position+'.sx') < 0:
                mc.setAttr(zero+'.sx', -1)

            if mc.getAttr(match_position+'.sy') < 0:
                mc.setAttr(zero+'.sy', -1)

            if mc.getAttr(match_position+'.sz') < 0:
                mc.setAttr(zero+'.sz', -1)

        # recopy the shape
        control.copy_shape(ref_name, ctrl)
        control.copy_color(ref_name, ctrl)

        last_node = ctrl
        offset_ctrls = []

        # # get num offset ctrls
        if num_offset_ctrls is None:
            num_offset_ctrls = 0
            if mc.objExists(ref_name+'.numOffsetCtrls'):
                num_offset_ctrls = mc.getAttr(ref_name+'.numOffsetCtrls')

        # create offset ctrls
        if num_offset_ctrls:
            offset_ctrls = control.create_offset_ctrls(ctrl, num_offset_ctrls)
            last_node = offset_ctrls[-1]
            for off_ctrl in offset_ctrls:
                if mc.objExists(off_ctrl+'_REF'):
                    control.copy_shape(off_ctrl+'_REF', off_ctrl)
                    control.copy_color(off_ctrl+'_REF', off_ctrl)

        if self.part_master:
            vis_attr = self.part_master+'.offsetCtrlsVis'
            for i, off_ctrl in enumerate(offset_ctrls):
                off_shapes = utils.get_shapes(off_ctrl)
                for shape in off_shapes:
                    utils.set_attrs(shape, 'v', l=0)
                    mc.connectAttr(vis_attr, shape+'.v')

        if mc.objExists(ctrl+'.offsetCtrlVis'):
            mc.deleteAttr(ctrl+'.offsetCtrlVis')

        return zero, ctrl, offset_ctrls, last_node

    def guide_ctrl_chain(self, name='', num_ctrls=5, shape='cube', color='yellow', scale=[1,1,1], flat_hierarchy=False, drivers=[],
                        axis='Y', constraint_type='parent', create_pivot=True, length=None, allow_offset_ctrls=True, alt_iterate='letter'):

        """Create a chain of guide joints"""

        if not length:
            length = num_ctrls - 1
        div = float(length) / (num_ctrls-1.0)

        zeros = []
        ctrls = []

        drv = None
        for i in range(num_ctrls):
            if i < len(drivers):
                drv = drivers[i]

            letter = utils.letters[i]
            if alt_iterate=='number':
                if i < 9:
                    letter = '0'+str(i+1)
                else:
                    letter = str (i+1)

            chain_name = utils.join_strings([name, letter])

            zero, ctrl = self.guide_ctrl(chain_name, shape=shape, color=color, allow_offset_ctrls=allow_offset_ctrls,
                scale=scale, axis=axis, create_pivot=create_pivot,
                driver=drv, constraint_type=constraint_type)

            if not drv:
                mc.xform(zero, ws=1, t=[div*i+1, 0, 0])

            if not flat_hierarchy and ctrls:
                mc.parent(zero, ctrls[-1])

            zeros.append(zero)
            ctrls.append(ctrl)

        return zeros, ctrls

    def build_guide(self, **kwargs):
        """This function is what actually buils a guide"""
        pass

    def rebuild_guide_post(self, **kwargs):
        """This is an empty method for running custom post rebvuild code"""
        pass

    def mirror_guide_post(self, **kwargs):
        """This is an empty method for running custom post mirror code"""
        pass

    def build_rig(self):
        """This function is what actually buils a rig"""
        pass

    def build_rigs(self):
        """Build all parts of the specified type"""

        p_type = self.part_type
        parts = mc.ls('*_guide_REF.guideMasterCtrl')
        parts = [p.replace('.guideMasterCtrl', '', 1) for p in parts]
        parts = [p for p in parts
                    if mc.getAttr(p+'.partType', asString=True) == p_type]

        for part_ref in parts:
            print '\n#####################################'
            print '# Building rig for: %s ...' %part_ref.replace('_guide_REF', '', 1)
            self.set_guide(part_ref)
            self.build_rig()

            print '# Success: '+part_ref.replace('_guide_REF', '', 1)

    def duplicate_guide(self, master='', rebuild_world=False, copy_ctrl_colors=True, world_space=True, **kwargs):
        """Dupilcates the current guide rig with all appropriate args set."""

        if not rebuild_world and self.part_type == 'worldRoot':
            mc.warning('Cannot duplicate root .. There can only be one!')
            return

        # Get original args
        if not master and not mc.ls(sl=1):
            mc.warning('Specify a guide OR select one!')
            return

        self.set_guide(master)
        old_master = str(self.guide_master)

        if not mc.objExists(old_master):
            mc.warning('Guide master not set!')
            return

        old_side = str(self.options.get('side'))
        old_name = str(self.options.get('name'))
        old_prefix = str(self.prefix)
        args = dict(self.options)

        pos_dict, surf_xforms = self.get_surf_pos()

        if 'side' in kwargs.keys():
            kwargs['side'] = utils.clean_name(kwargs.get('side'))
        if 'name' in kwargs.keys():
            kwargs['name'] = utils.clean_name(kwargs.get('name'))

        args.update(**kwargs)

        # Update args and build a new part
        self.set_guide(clear=1)
        new_master = self.build_guide(**args)

        new_master = self.guide_master
        if not mc.objExists(new_master):
            mc.warning('New guide not created!')
            return

        new_side = self.options.get('side')
        new_name = self.options.get('name')
        new_prefix = self.prefix

        # Build my list of new nodes to repo
        nodes = utils.get_children(new_master+'_PLCS', ad=1)
        plcs = [c for c in nodes if c.endswith('JNT_PLC')]

        nodes = utils.get_children(new_master+'_CTLS' , ad=1)
        ctrls = [c for c in nodes if c.endswith('_CTL')]

        plcs.reverse()
        ctrls.reverse()

        new_nodes = [new_master]+plcs+ctrls

        # Get the max number of times i should loop thought stuff
        cycle = mc.cycleCheck(q=1, e=1)
        mc.cycleCheck(e=False)

        check_all = self.check_if_part_has_lef_and_right_nodes(new_master)

        self.set_surf_pos(pos_dict, surf_xforms, old_prefix, new_prefix)

        # Actually repo nodes
        for i in range(len(new_nodes))*4:

            newNode = new_nodes[i]

            # special case for
            if check_all and newNode.startswith('L'):
                old_node = newNode.replace('L'+new_prefix[1:], 'L'+old_prefix[1:], 1)

            elif check_all and newNode.startswith('R'):
                old_node = newNode.replace('R'+new_prefix[1:], 'R'+old_prefix[1:], 1)

            else:
                old_node = newNode.replace(new_prefix, old_prefix, 1)

            if mc.objExists(newNode) and mc.objExists(old_node):
                for attr in ['rotateOrder', 'numOffsetCtrls']:
                    if mc.objExists(old_node+'.'+attr) and mc.objExists(newNode+'.'+attr):
                        if not mc.getAttr(newNode+'.'+attr, l=1):
                            value = mc.getAttr(old_node+'.'+attr)
                            mc.setAttr(newNode+'.'+attr, value)

                if world_space:
                    mc.xform(newNode, ws=1, t=mc.xform(old_node, q=1, t=1, ws=1))
                    mc.xform(newNode, ws=1, ro=mc.xform(old_node, q=1, ro=1, ws=1))
                else:
                    mc.xform(newNode, a=1, t=mc.xform(old_node, q=1, t=1, a=1))
                    mc.xform(newNode, a=1, ro=mc.xform(old_node, q=1, ro=1, a=1))

                mc.xform(newNode, a=1, s=mc.xform(old_node, q=1, s=1, r=1))

            if newNode == new_master:
                self.set_surf_pos(pos_dict, surf_xforms, old_prefix, new_prefix)

        attrs = ['jointPlacerVis', 'ctrlVis', 'ctrlAxisVis', 'scaleY',
                'offsetTranslateY', 'offsetTranslateX', 'offsetTranslateZ',
                 'jointAxisVis', 'jointSelectable', 'placerXRayMode',
                 'placerOpacity', 'placerSize', 'placerScaleCompensate']

        u_attrs = [a for a in mc.listAttr(old_master, ud=1) if a in args.keys()]
        u_attrs = [a for a in u_attrs
                        if mc.addAttr(old_master+'.'+a, q=1, at=1) not in ['enum', 'typed']]

        attrs = list(set(attrs + u_attrs))

        # Copy master vis attrs
        for attr in attrs:
            try:
                value = round(mc.getAttr(old_master+'.'+attr), 3)
                mc.setAttr(new_master+'.'+attr, value)
            except:
                pass

        # Copy ctrl shapes
        for newNode in ctrls:

            # special case for
            if check_all and newNode.startswith('L'):
                old_node = newNode.replace('L'+new_prefix[1:], 'L'+old_prefix[1:], 1)

            elif check_all and newNode.startswith('R'):
                old_node = newNode.replace('R'+new_prefix[1:], 'R'+old_prefix[1:], 1)

            else:
                old_node = newNode.replace(new_prefix, old_prefix, 1)

            if mc.objExists(old_node) and mc.objExists(newNode):
                shapes = utils.get_shapes(newNode) or []
                for shape in shapes:
                    if mc.nodeType(shape) != 'cmPivotShape':
                        control.copy_shape(old_node, newNode, world_space=world_space)
                        if copy_ctrl_colors:
                            control.copy_color(old_node, newNode)

        self.set_guide(new_master)
        self.set_master_attrs()

        mc.select(new_master)
        mc.cycleCheck(e=cycle)

        return new_master

    def mirror_guide(self, master='', update_options=True):
        """Mirror Guide joints from one side to the other"""

        mc.selectPriority(locator=9)

        if self.part_type == 'worldRoot':
            mc.warning('Cannot mirror root .. There can only be one!')
            return

        if not master and not mc.ls(sl=1):
            mc.warning('Specify a guide OR select one!')
            return

        # Get original args
        self.set_guide(master)
        old_master = self.guide_master

        if not mc.objExists(old_master):
            mc.warning('Guide master not set!')
            return

        # Get mirror side OR find the center side and see if any nodes under neath need mirroring
        self.get_master_attrs()

        old_master = str(self.guide_master)
        old_side = str(self.options.get('side'))
        old_name = str(self.options.get('name'))
        old_prefix = str(self.prefix)
        oldArgs = dict(self.options)

        # check for left and right sided nodesinthis part
        mirror_center_part = False
        all_children = utils.get_children(old_master, ad=1)
        for c in all_children:
            if c.startswith('L_'):
                mirror_center_part = True
                break

        if old_side == 'L':
            new_side = 'R'

        elif old_side == 'R':
            new_side = 'L'

        elif mirror_center_part:
            # Need a seperate function
            self.mirror_center_part()
            return

        else:
            mc.warning('Cannot mirror a center sided part!')
            return

        pos_dict, surf_xforms = self.get_surf_pos()
        new_prefix = utils.join_strings([new_side, old_name])
        new_master = old_master.replace(old_prefix, new_prefix, 1)

        # Create
        if mc.objExists(new_master):
            # IF args that are locked are different then a rebuild is needed

            self.set_guide(new_master)
            new_args = dict(self.options)
            needsRebuild = False

            for arg, value in new_args.items():
                if self.options_info_dict.get(arg).get('rebuild_to_modify'):
                    if not self.options_info_dict.get(arg).get('data_type') in ['selection', 'hook']:
                        oldValue = oldArgs.get(arg)
                        newValue = new_args.get(arg)

                        if oldValue != newValue:
                            needsRebuild = True

            if needsRebuild and update_options:
                result = mc.confirmDialog(title='Rebuild Required To Mirror',
                    message='Left and right side args are different.\n' +\
                    'Mirroring this guide part requies a rebuild.\n\n' +\
                    'Do you want to rebuild {0}?'.format(new_master),
                    button=['Rebuild','Cancel'], defaultButton='Rebuild',
                    cancelButton='Cancel', dismissString='Cancel', icon='warning')

                if result == 'Rebuild':
                    mc.delete(new_master)
                    oldArgs['side'] = new_side
                    self.duplicate_guide(copy_ctrl_colors=False, **oldArgs)

                else:
                    mc.warning('Rebuild canceled.')
                    return
        else:
            print '# Duplicating Guide'

            # get mirroed args
            new_args = dict(self.options)
            r_side = 'R'
            l_side = 'L'
            for k, v in new_args.items():
                new_val = v
                if type(v) is list:
                    new_val = []
                    for i in v:
                        i = str(i)
                        if i.startswith(l_side):
                            i = i.replace(l_side, r_side, 1)
                        elif i.startswith(r_side):
                            i = i.replace(r_side, l_side, 1)
                        new_val.append(i)

                elif type(v) in [str, unicode]:
                    new_val = v
                    if v.startswith(l_side):
                        new_val = v.replace(l_side, r_side, 1)

                    elif v.startswith(r_side):
                        new_val = v.replace(r_side, l_side, 1)

                new_args[k] = new_val

            self.duplicate_guide(copy_ctrl_colors=False, **new_args)

        new_master = self.guide_master
        new_side = self.options.get('side')
        new_name = self.options.get('name')
        new_prefix = self.prefix
        new_args = dict(self.options)

        # get ctrls and pos nodes for center sided parts OR mirrored L or R parts
        nodes = utils.get_children(new_master+'_PLCS', ad=1)
        plcs = [c for c in nodes if c.endswith('JNT_PLC')]

        nodes = utils.get_children(new_master+'_CTLS', ad=1)
        ctrls = [c for c in nodes if c.endswith('_CTL')]

        plcs.reverse()
        ctrls.reverse()
        allNewNodes = [new_master]+plcs+ctrls
        allOldNodes = {}

        u_attrs = [a for a in mc.listAttr(old_master, ud=1) if a in oldArgs.keys()]
        u_attrs = [a for a in u_attrs
                        if mc.addAttr(old_master+'.'+a, q=1, at=1) not in ['enum', 'typed']]

        for attr in u_attrs:
            try:
                value = round(mc.getAttr(old_master+'.'+attr), 3)
                mc.setAttr(new_master+'.'+attr, value)
            except:
                pass

        for newNode in allNewNodes:

            old_node = newNode.replace(new_prefix, old_prefix, 1)

            if old_side == 'C':

                lSide = 'L'
                rside = 'R'

                if newNode.startswith(lSide):
                    old_node == newNode.replace(lSide, rside, 1)
                elif newNode.startswith(rside):
                    old_node == newNode.replace(rside, lSide, 1)

            else:
                old_node = newNode.replace(new_prefix, old_prefix, 1)

            allOldNodes[newNode] = old_node

        new_nodes = []
        old_nodes = []
        for newNode in allNewNodes:
            old_node = allOldNodes.get(newNode, '')
            if mc.objExists(old_node):
                new_nodes.append(newNode)
                old_nodes.append(old_node)

        if old_side == 'C' and not old_nodes:
            mc.delete(new_master)
            raise RuntimeError('This part is not mirrorable!')

        elif not new_nodes or not old_nodes:
            mc.delete(new_master)
            raise RuntimeError('Cannot find ctrls to mirror! This part is not mirrorable!')

        # Get the max number of times i should loop thought stuff
        cycle = mc.cycleCheck(q=1, e=1)
        mc.cycleCheck(e=False)

        self.set_surf_pos(pos_dict, surf_xforms, old_prefix, new_prefix, mirror=True)
        self.mirror_surf()

        # mirror plcs, ctrls
        for i in range(len(new_nodes))*4:
            if new_nodes[i] == new_master:
                self.set_surf_pos(pos_dict, surf_xforms, old_prefix, new_prefix, mirror=True)
            mirror_guide_joint(old_nodes[i], new_nodes[i], self.mirror_behavior)

        # Mirror ctrl shapes
        for new_ctrl in ctrls:
            if not utils.get_shapes(new_ctrl):
                continue

            old_ctrl = new_ctrl.replace(new_prefix, old_prefix, 1)

            # mirror scale pivot IF scale is unlocked:
            new_pivot = mc.listRelatives(new_ctrl, p=1)[0]
            old_pivot = new_pivot.replace(new_prefix, old_prefix, 1)
            new_pivot_parent = mc.listRelatives(new_pivot, p=1)[0]

            for attr in ['rotateOrder', 'numOffsetCtrls']:
                if mc.objExists(old_ctrl+'.'+attr) and mc.objExists(new_ctrl+'.'+attr):
                    if not mc.getAttr(new_ctrl+'.'+attr, l=1):
                            value = mc.getAttr(old_ctrl+'.'+attr)
                            mc.setAttr(new_ctrl+'.'+attr, value)

            if mc.objExists(old_ctrl+'.mirrorMode'):

                mirrorMode = mc.getAttr(old_ctrl+'.mirrorMode')
                mc.setAttr(new_ctrl+'.mirrorMode', mirrorMode)

                if mirrorMode == 0:
                    rxLock = mc.getAttr(new_pivot+'.rx', l=1)
                    ryLock = mc.getAttr(new_pivot+'.ry', l=1)
                    rzLock = mc.getAttr(new_pivot+'.rz', l=1)
                    sxLock = mc.getAttr(new_pivot+'.sx', l=1)
                    syLock = mc.getAttr(new_pivot+'.sy', l=1)
                    szLock = mc.getAttr(new_pivot+'.sz', l=1)

                    rxHidden = mc.getAttr(new_pivot+'.rx', l=1)
                    ryHidden = mc.getAttr(new_pivot+'.ry', l=1)
                    rzHidden = mc.getAttr(new_pivot+'.rz', l=1)
                    sxHidden = mc.getAttr(new_pivot+'.sx', l=1)
                    syHidden = mc.getAttr(new_pivot+'.sy', l=1)
                    szHidden = mc.getAttr(new_pivot+'.sz', l=1)

                    if sxLock or syLock or szLock:
                        mc.setAttr(new_pivot+'.rx', l=0)
                        mc.setAttr(new_pivot+'.ry', l=0)
                        mc.setAttr(new_pivot+'.rz', l=0)
                        mc.setAttr(new_pivot+'.sx', l=0)
                        mc.setAttr(new_pivot+'.sy', l=0)
                        mc.setAttr(new_pivot+'.sz', l=0)

                    tmpGrp = mc.createNode('transform')
                    tmp = mc.createNode('transform', p=old_pivot)
                    ctmp = mc.createNode('transform', p=old_ctrl)
                    mc.parent(tmp, ctmp, tmpGrp)

                    mc.setAttr(tmpGrp+'.sx', -1)
                    mc.parent(tmp, new_pivot_parent)

                    mc.xform(new_pivot, ws=1, t= mc.xform(tmp, q=1, ws=1, t=1))
                    mc.xform(new_pivot, ws=1, ro= mc.xform(tmp, q=1, ws=1, ro=1))
                    mc.xform(new_pivot, a=1, s= mc.xform(tmp, q=1, r=1, s=1))

                    mc.parent(ctmp, new_pivot)
                    mc.xform(new_ctrl, ws=1, t= mc.xform(ctmp, q=1, ws=1, t=1))
                    mc.xform(new_ctrl, ws=1, ro= mc.xform(ctmp, q=1, ws=1, ro=1))
                    mc.xform(new_ctrl, a=1, s= mc.xform(ctmp, q=1, r=1, s=1))

                    mc.delete(tmpGrp, ctmp, tmp)

                    if sxLock or syLock or szLock:
                        mc.setAttr(new_pivot+'.rx', l=rxLock, k=rxHidden)
                        mc.setAttr(new_pivot+'.ry', l=ryLock, k=ryHidden)
                        mc.setAttr(new_pivot+'.rz', l=rzLock, k=rzHidden)
                        mc.setAttr(new_pivot+'.sx', l=sxLock, k=sxHidden)
                        mc.setAttr(new_pivot+'.sy', l=syLock, k=syHidden)
                        mc.setAttr(new_pivot+'.sz', l=szLock, k=szHidden)

        for new_ctrl in ctrls:
            if not utils.get_shapes(new_ctrl):
                continue

            old_ctrl = new_ctrl.replace(new_prefix, old_prefix, 1)
            if mc.objExists(new_ctrl+'.animControl'):
                control.copy_shape(old_ctrl, new_ctrl, mirror_axis='X')

            elif mc.objExists(new_ctrl+'.guideOffsetCtrl'):
                trans = mc.xform(old_ctrl, a=1, t=1, q=1)
                rot = mc.xform(old_ctrl, a=1, ro=1, q=1)
                scale = mc.xform(old_ctrl, r=1, s=1, q=1)

                mc.xform(new_ctrl, a=1, t=trans)
                mc.xform(new_ctrl, a=1, ro=rot)
                mc.xform(new_ctrl, a=1, s=scale)

        self.set_master_attrs()
        self.mirror_guide_post()
        mc.select(new_master)

        return self

    def mirror_surf(self):
        pass

    def mirror_center_part(self):
        """Only mirrors from left to right"""

        self.mirror_surf()
        master = self.guide_master

        nodes = utils.get_children(master+'_PLCS', ad=1)
        plcs = [c for c in nodes if c.endswith('JNT_PLC') and c.startswith('L')]

        nodes = utils.get_children(master+'_CTLS', ad=1)
        ctrls = [c for c in nodes if c.endswith('_CTL') and c.startswith('R')]

        for plc in plcs:
            r_plc = plc.replace('L','R',1)
            mirror_guide_joint(plc, r_plc, self.mirror_behavior)

        old_prefix = 'L'
        new_prefix = 'R'

        for new_ctrl in ctrls:
            if not utils.get_shapes(new_ctrl):
                continue

            old_ctrl = new_ctrl.replace(new_prefix, old_prefix, 1)

            # mirror scale pivot IF scale is unlocked:
            new_pivot = mc.listRelatives(new_ctrl, p=1)[0]
            old_pivot = new_pivot.replace(new_prefix, old_prefix, 1)
            new_pivot_parent = mc.listRelatives(new_pivot, p=1)[0]

            for attr in ['rotateOrder', 'numOffsetCtrls']:
                if mc.objExists(old_ctrl+'.'+attr) and mc.objExists(new_ctrl+'.'+attr):
                    if not mc.getAttr(new_ctrl+'.'+attr, l=1):
                            value = mc.getAttr(old_ctrl+'.'+attr)
                            mc.setAttr(new_ctrl+'.'+attr, value)

            if mc.objExists(old_ctrl+'.mirrorMode'):

                mirrorMode = mc.getAttr(old_ctrl+'.mirrorMode')
                mc.setAttr(new_ctrl+'.mirrorMode', mirrorMode)

                if mirrorMode == 0:
                    rxLock = mc.getAttr(new_pivot+'.rx', l=1)
                    ryLock = mc.getAttr(new_pivot+'.ry', l=1)
                    rzLock = mc.getAttr(new_pivot+'.rz', l=1)
                    sxLock = mc.getAttr(new_pivot+'.sx', l=1)
                    syLock = mc.getAttr(new_pivot+'.sy', l=1)
                    szLock = mc.getAttr(new_pivot+'.sz', l=1)

                    rxHidden = mc.getAttr(new_pivot+'.rx', l=1)
                    ryHidden = mc.getAttr(new_pivot+'.ry', l=1)
                    rzHidden = mc.getAttr(new_pivot+'.rz', l=1)
                    sxHidden = mc.getAttr(new_pivot+'.sx', l=1)
                    syHidden = mc.getAttr(new_pivot+'.sy', l=1)
                    szHidden = mc.getAttr(new_pivot+'.sz', l=1)

                    if sxLock or syLock or szLock:
                        mc.setAttr(new_pivot+'.rx', l=0)
                        mc.setAttr(new_pivot+'.ry', l=0)
                        mc.setAttr(new_pivot+'.rz', l=0)
                        mc.setAttr(new_pivot+'.sx', l=0)
                        mc.setAttr(new_pivot+'.sy', l=0)
                        mc.setAttr(new_pivot+'.sz', l=0)

                    tmpGrp = mc.createNode('transform')
                    tmp = mc.createNode('transform', p=old_pivot)
                    ctmp = mc.createNode('transform', p=old_ctrl)
                    mc.parent(tmp, ctmp, tmpGrp)

                    mc.setAttr(tmpGrp+'.sx', -1)
                    mc.parent(tmp, new_pivot_parent)

                    mc.xform(new_pivot, ws=1, t= mc.xform(tmp, q=1, ws=1, t=1))
                    mc.xform(new_pivot, ws=1, ro= mc.xform(tmp, q=1, ws=1, ro=1))
                    mc.xform(new_pivot, a=1, s= mc.xform(tmp, q=1, r=1, s=1))

                    mc.parent(ctmp, new_pivot)
                    mc.xform(new_ctrl, ws=1, t= mc.xform(ctmp, q=1, ws=1, t=1))
                    mc.xform(new_ctrl, ws=1, ro= mc.xform(ctmp, q=1, ws=1, ro=1))
                    mc.xform(new_ctrl, a=1, s= mc.xform(ctmp, q=1, r=1, s=1))

                    mc.delete(tmpGrp, ctmp, tmp)

                    if sxLock or syLock or szLock:
                        mc.setAttr(new_pivot+'.rx', l=rxLock, k=rxHidden)
                        mc.setAttr(new_pivot+'.ry', l=ryLock, k=ryHidden)
                        mc.setAttr(new_pivot+'.rz', l=rzLock, k=rzHidden)
                        mc.setAttr(new_pivot+'.sx', l=sxLock, k=sxHidden)
                        mc.setAttr(new_pivot+'.sy', l=syLock, k=syHidden)
                        mc.setAttr(new_pivot+'.sz', l=szLock, k=szHidden)

        for new_ctrl in ctrls:
            if not utils.get_shapes(new_ctrl):
                continue

            old_ctrl = new_ctrl.replace(new_prefix, old_prefix, 1)
            if mc.objExists(new_ctrl+'.animControl'):
                control.copy_shape(old_ctrl, new_ctrl, mirror_axis='X')

            elif mc.objExists(new_ctrl+'.guideOffsetCtrl'):
                trans = mc.xform(old_ctrl, a=1, t=1, q=1)
                rot = mc.xform(old_ctrl, a=1, ro=1, q=1)
                scale = mc.xform(old_ctrl, r=1, s=1, q=1)

                mc.xform(new_ctrl, a=1, t=trans)
                mc.xform(new_ctrl, a=1, ro=rot)
                mc.xform(new_ctrl, a=1, s=scale)

        self.mirror_guide_post()
        mc.select(master)

        return self

    def get_surf_pos(self):
        pos_dict = {}
        surf_xforms = {}
        for surf in self.surfaces:
            cvs = mc.ls(surf+'.cv[*]', fl=1)
            for cv in cvs:
                pos_dict[cv] = [round(p, 5) for p in mc.xform(cv, q=1, t=1, ws=1)]

            t_pos = mc.xform(utils.get_transform(surf), q=1, ws=1, t=1)
            r_pos = mc.xform(utils.get_transform(surf), q=1, ws=1, ro=1)
            s_pos = mc.xform(utils.get_transform(surf), q=1, r=1, s=1)
            surf_xforms[utils.get_transform(surf)] = [t_pos, r_pos, s_pos]

        return pos_dict, surf_xforms

    def set_surf_pos(self, pos_dict, surf_xforms, old_prefix, new_prefix, mirror=False):

        for surf, matrix in surf_xforms.items():
            new_surf = surf.replace(old_prefix, new_prefix, 1)
            if mc.objExists(new_surf):
                mc.xform(new_surf, ws=1, t=matrix[0])
                mc.xform(new_surf, ws=1, ro=matrix[1])
                mc.xform(new_surf, a=1, s=matrix[2])

                if mirror:
                    tmp_par = mc.createNode('transform')
                    tmp = mc.createNode('transform', p=tmp_par)
                    mc.xform(tmp, ws=1, t=matrix[0])
                    mc.xform(tmp, ws=1, ro=matrix[1])
                    mc.xform(tmp, a=1, s=matrix[2])

                    mc.setAttr(tmp_par+'.sx', -1)

                    matrix = utils.decompose_matrix(tmp)
                    mc.xform(new_surf, ws=1, t=matrix[0])
                    mc.xform(new_surf, ws=1, ro=matrix[1])
                    mc.xform(new_surf, a=1, s=matrix[2])
                    mc.delete(tmp_par)

        for cv, pos in pos_dict.items():
            new_cv = cv.replace(old_prefix, new_prefix, 1)
            if mc.objExists(new_cv):
                if mirror:
                    pos[0] *= -1

                mc.xform(new_cv, ws=1, t=pos)

    def rebuild_guide(self, master='', world_space=True, **kwargs):
        """For updating guide args that require a rebuild."""

        # Get original args
        if not master and not mc.ls(sl=1):
            mc.warning('Specify a guide OR select one!')
            return

        self.set_guide(master)
        old_master = self.guide_master

        if not mc.objExists(old_master):
            mc.warning('Guide master not set!')
            return

        if self.part_type == 'worldRoot':
            mc.warning('Cannot rebuild worldRoot, it has no options..')
            return

        old_side = str(self.options.get('side'))
        old_name = str(self.options.get('name'))
        old_prefix = str(self.prefix)
        args = dict(self.options)

        if 'side' in kwargs.keys():
            kwargs['side'] = utils.clean_name(kwargs.get('side'))

        kwargs['name'] = str(args.get('name')+'REBUILD')

        args.update(**kwargs)

        # Update args and build a new part
        self.set_guide(clear=1)
        self.duplicate_guide(rebuild_world=True, world_space=world_space, **args)

        if not mc.objExists(self.guide_master):
            return

        # Delete old guide and rename new one.
        mc.delete(old_master)

        self.update_options_raw(name=old_name, force=True)

        self.set_guide(self.guide_master)
        self.rebuild_guide_post()

        mc.select(self.guide_master)

    def get_master_attrs(self):
        """Gets any cusotm attrs the user may have built intothe guide master"""

        return

        invalid_types = ['message','typed', 'compound']

        locked_attrs = mc.listAttr(self.guide_master, l=1)
        master_attrs = mc.listAttr(self.guide_master, ud=1)
        master_attrs = [a for a in master_attrs if a not in locked_attrs]
        master_attrs = [a for a in master_attrs if '_' not in a]
        master_attrs = [a for a in master_attrs if '_' not in a]
        master_attrs = [a for a in master_attrs
                        if mc.addAttr(self.guide_master+'.'+a, q=1, at=1)
                                not in invalid_types]

        self.master_attrs_dict = {}
        for attr in master_attrs:
            self.master_attrs_dict[attr] = mc.getAttr(self.guide_master+'.'+attr)

    def set_master_attrs(self, new_master=None):
        """Sets any cusotm attrs the user may have built intothe guide master"""

        return

        if not new_master:
            new_master = self.guide_master

        for attr, value in self.master_attrs_dict.items():
            try:
                mc.setAttr(new_master+'.'+attr, value)
            except:
                pass

    def tag_as_ref(self, nodes):
        """This will tag any nodes in the guide to be kept in the skel build.a
            It'll be kept as a a reference node. seperate from the skeleton herirarchy.skeleton
            It'll be kept under guides_REF"""

        nodes = mc.ls(nodes)
        if nodes:
            mc.addAttr(nodes, ln='keepAsRef', at='message')

    def tag_finalize_status(self):
        """This will label the guide_master with the finalize status"""

        mc.addAttr(self.guide_master,
                    ln = 'finializeStatus',
                    dt = 'string')


    def set_finalize_status(self, finalize_status):
        """This will label the guide_master with the finalize status
            Use Status strings:
                "pre_finalize"
                "post_finalize"

        """
        if mc.objExists(self.guide_master):
            mc.setAttr(self.guide_master +".finializeStatus",
                        finalize_status,
                        type = "string")

    def tag_hook_parent(self, node, parent):

        if not mc.objExists(node+'.parentHook'):
            mc.addAttr(node, ln='parentHook', dt='string')

        mc.setAttr(node+'.parentHook', str(parent), type='string')

    #Spitback functions

    def spitback_plc_positions(self, plcs=None,
                               maya_code_identifier = "mc",
                               decimal_rounding = 3):
        """
            Prints maya code back to the user which can be pasted back into a build script.
            Must be run before the finalize function.

            Note:
                self.guide_master is appended to plcs by the script automatically only placer objects
                are required, how they are returned by self.guide_joint_chain() is preferred.

            Kwargs:
                plcs (list) = A list of placer guide items
                maya_code_identifier (str) = A string representing the type of maya import statement.
                                                 Ex. "mc", "cmds", "pm", "pm.cmds" .
                decimal_rounding (int) = The number of decimal places to round to - default is 3.

            TO-DO:
                -This function can be extended/rewritten to grab all values of the guide or added options.
                -Might need to spitback variables? Its kicking out hard coded names at the moment.
                -Use the .finalizeStatus attribute to ensure this function can work before or after finalizing

            Returns:
                None
        """
        if plcs is None:
            plcs = mc.ls(sl=1)

        print ""
        print "#Generic placement of guides"
        print ""
        #Grab all the given plcs and add self.guide_master
        for plc in plcs + [self.guide_master]:
            print "#" + plc + "-----------------------------#"
            #attributes to gather:
            for attr_string in [
                                "translateX","translateY","translateZ",
                                "rotateX","rotateY","rotateZ"
                               ]:

                print '{0}.setAttr("{1}.{2}", {3})'.format(
                                                            maya_code_identifier,
                                                            plc,
                                                            attr_string,
                                                            round(mc.getAttr(plc + "." + attr_string),
                                                                             decimal_rounding)
                                                            )


        print "#global Scale -----------------------------#"
        print '{0}.setAttr("{1}.{2}", {3})'.format(
                                                            maya_code_identifier,
                                                            plc,
                                                            "globalScale",
                                                            round(mc.getAttr(plc + "." + "globalScale"),
                                                                             decimal_rounding)
                                                            )

        print "#..Code generated by self.spitback_placer_positions()"
        print "#..End generated code -----------------------------#"
        print ""


    @classmethod
    def check_if_part_has_lef_and_right_nodes(self, guide_master):

        check_all = False
        if guide_master.startswith('C'):
            nodes = utils.get_children(guide_master, ad=1)

            test = [n for n in nodes
                        if n.split('|')[-1].startswith('L') or n.split('|')[-1].startswith('R')]
            if test:
                check_all = True
        return check_all


def mirror_guide_joint(old_node, newNode=None, mirror_behavior=True):
    """Mirrors and idividual guidew joints"""

    if not newNode:
        newNode = old_node

    old_tmp = mc.createNode('joint', n=old_node+'_mirror_TMP')

    mc.setAttr(old_tmp+'.ro', mc.getAttr(old_node+'.ro'))
    mc.delete(mc.parentConstraint(old_node, old_tmp))

    mirrorTemp = mc.mirrorJoint(old_tmp, mirrorBehavior=1, mirrorYZ=1,
                                searchReplace =[old_node, newNode])[0]

    if not mirror_behavior:
        jox = mc.getAttr(mirrorTemp+'.jox')
        mc.setAttr(mirrorTemp+'.jox', jox-180)

    txLock = mc.getAttr(newNode+'.tx', l=1)
    tyLock = mc.getAttr(newNode+'.ty', l=1)
    tzLock = mc.getAttr(newNode+'.tz', l=1)
    txHidden = mc.getAttr(newNode+'.tx', k=1)
    tyHidden = mc.getAttr(newNode+'.ty', k=1)
    tzHidden = mc.getAttr(newNode+'.tz', k=1)

    rxLock = mc.getAttr(newNode+'.rx', l=1)
    ryLock = mc.getAttr(newNode+'.ry', l=1)
    rzLock = mc.getAttr(newNode+'.rz', l=1)
    rxHidden = mc.getAttr(newNode+'.rx', k=1)
    ryHidden = mc.getAttr(newNode+'.ry', k=1)
    rzHidden = mc.getAttr(newNode+'.rz', k=1)

    if rxLock or ryLock or rzLock:
        utils.set_attrs(newNode, 'r', l=0)

    if txLock or tyLock or tzLock:
        utils.set_attrs(newNode, 't', l=0)

    mc.xform(newNode, ws=1, t= mc.xform(mirrorTemp, q=1, ws=1, t=1))
    mc.xform(newNode, ws=1, ro= mc.xform(mirrorTemp, q=1, ws=1, ro=1))
    mc.xform(newNode, a=1, s= mc.xform(mirrorTemp, q=1, r=1, s=1))

    if mc.objExists(newNode+'.globalScale'):
        mc.setAttr(newNode+'.globalScale', mc.getAttr(old_node+'.globalScale'))

    mc.delete( mirrorTemp, old_tmp)

    if txLock or tyLock or tzLock:
        mc.setAttr(newNode+'.tx', l=txLock, k=txHidden)
        mc.setAttr(newNode+'.ty', l=tyLock, k=tyHidden)
        mc.setAttr(newNode+'.tz', l=tzLock, k=tzHidden)

    if rxLock or ryLock or rzLock:
        mc.setAttr(newNode+'.rx', l=rxLock, k=rxHidden)
        mc.setAttr(newNode+'.ry', l=ryLock, k=ryHidden)
        mc.setAttr(newNode+'.rz', l=rzLock, k=rzHidden)

def checkNewArgs(oldSide, oldName, newSide, newName, nodes, label=''):
    """Need this to be outside of the clas to avoid QT lopping issues"""

    def checknewNames(newNames):
        status = True
        for nName in newNames:
            if mc.objExists(nName):
                status = False
                print nName

        return status

    def getNewNodeNames(oldPrefix, newPrefix, nodes, check_all_sides=False):

        newNames = []
        for node in nodes:
            if check_all_sides:
                if node.split('|')[-1].startswith('L'):
                    newName = 'C' + node.split('|')[-1][1:]
                    newName = newName.replace(oldPrefix, newPrefix, 1)
                    newName = 'L'+newName[1:]

                elif node.split('|')[-1].startswith('R'):
                    newName = 'C' + node.split('|')[-1][1:]
                    newName = newName.replace(oldPrefix, newPrefix, 1)
                    newName = 'R'+newName[1:]

                else:
                    newName = node.split('|')[-1].replace(oldPrefix, newPrefix, 1)

            else:
                newName = node.split('|')[-1].replace(oldPrefix, newPrefix, 1)

            newNames.append(newName)

        return newNames

    check_all = False
    if oldSide == 'C':
        test = [n for n in nodes
                    if n.split('|')[-1].startswith('L') or n.split('|')[-1].startswith('R')]
        if test:
            check_all = True

    newPrefix = utils.join_strings([newSide, newName])
    oldPrefix = utils.join_strings([oldSide, oldName])
    newNames = getNewNodeNames(oldPrefix, newPrefix, nodes, check_all_sides=check_all)
    succeeded = True
    cancelled = False

    while not checknewNames(newNames) and not cancelled:

        from rigBot.gui import argPrompt
        prompt = argPrompt.ArgPrompt(oldSide, oldName, newSide, newName, nodes, label=label)
        prompt.exec_()

        succeeded = prompt.success
        cancelled = prompt.cancelled
        newNames = prompt.newNames
        newSide = prompt.newSide
        newName = prompt.newName

    return succeeded, newSide, newName, newNames

