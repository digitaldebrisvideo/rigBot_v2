import maya.cmds as mc
import maya.mel as mm


from functools import partial
import os
import re

from rigBot import mod

control        = mod.import_module('rigBot.control')
utils          = mod.import_module('rigBot.utils')
data           = mod.import_module('rigBot.data')
model          = mod.import_module('rigBot.model')
guide          = mod.import_module('rigBot.guide')
skel           = mod.import_module('rigBot.skel')
rig            = mod.import_module('rigBot.rig')
env            = mod.import_module('rigBot.env')

asset = env.get_asset()
custom         = mod.import_module(env.get_asset()+'_custom')

"""This is a standard rigAll build script.
    This is the complete build script for asset rigs.
    For now this is only a python script that you can call and run. Eventually
    it will be integrated with the UI to allow a seamless back bacn forth between
    a fully ui based aproach and a fully script based approach.

    Feel free to modify this however you see fit.

    USAGE:
        import Bear_rigAll
        Bear_rigAll.Default.build()
        Bear_rigAll.Mocap.build()
        """

class Default(object):
    """Class for anim rig build"""

    build_list = []
    enabled_array = []
    status_array = []

    step_node = ''

    current_step = -1
    use_plugin_nodes = True

    def __init__(self):
        pass

    @classmethod
    def build(self, *steps):
        """This method executes the commands in your build_list.
            You can choose to either run all commands at once, build one at a time, step by step,
            or build a specific step.

            KWARGS:
                :steps: Step to build, either specify and index,
                an index range formated as (0,3), OR choose 'ALL', 'REMAINING' or 'NEXT'"""

        def execute_command(item):
            """Actually execute each item"""

            # get the index of this item
            index = self.build_list.index(item)
            self.current_step = index

            pre_array = self.status_array

            if self.enabled_array[index]:
                print '#######################################################'
                print 'BUILDING STEP {0}: {1}'.format(index, item.get('label'))
                print '#######################################################\n'
                try:
                    #try running the comand
                    command = item.get('command')
                    if command:
                        command()

                    self.set_status(index, 3, all_values=pre_array)
                    print 'Finished building step!'
                    print '\n'

                # throw an exception and stop if it failed
                except Exception as exception:
                    self.set_status(index, -1, all_values=pre_array)
                    raise RuntimeError(utils.get_exception())

            # Just skip it if disabled
            else:
                print '#######################################################'
                print '**DISABLED STEP {0}: {1}'.format(index, item.get('label'))
                print '#######################################################\n'
                print '\n'

                self.set_status(index, 1, all_values=pre_array)

            return True

        os.environ['use_plugin_nodes'] = str(self.use_plugin_nodes)

        # Create mute node
        self.get_step_node()
        self.get_status()

        if not steps:
            steps = 'ALL'

        elif len(steps) == 1:
            steps = steps[0]

        # IF steps is set to ALL do a fresh build
        if type(steps) in [str, unicode] and steps.lower() == 'all':
            #print '\nBUILDING ALL STEPS..'

            # reset the status of the whole list
            for i in range(len(self.build_list)):
                self.set_status(i, 0)

            # loop through and build that list
            for i in range(len(self.build_list)):
                result = execute_command(self.build_list[i])
                if not result:
                    return False

        elif type(steps) in [str, unicode] and steps.lower() == 'next':
            step = self.get_next_step()

            if step < len(self.build_list):
                #print '\nBUILDING NEXT STEP..'

                if not 'command' in self.build_list[step].keys():
                    result = execute_command(self.build_list[step])
                    step += 1

                result = execute_command(self.build_list[step])
                if result:
                    return step
                else:
                    return False
            else:
                mc.warning('No more steps to build.')
                return

        elif type(steps) in [str, unicode] and steps.lower() == 'remainder':
            step = self.get_next_step()

            if step < len(self.build_list):
                #print '\nBUILDING REMAINING STEPS..'

                for item in self.build_list[step:]:
                    result = execute_command(item)
                    if not result:
                        return False
            else:
                mc.warning('No more steps to build.')
                return False

        # case for building a certain range in the build list
        elif type(steps) in [tuple, list]:
            #print '\nBUILDING STEPS..'

            items_to_build = self.build_list[steps[0] : steps[1]]
            for item in items_to_build:
                result = execute_command(item)
                if not result:
                    return False

        # Case for building a single item in the list
        elif type(steps) == int:
            #print '\nBUILDING SINGLE STEP..'

            result = execute_command(self.build_list[steps])
            if not result:
                return False

        return True


    @classmethod
    def get_step_node(self):
        """Find or create a build steps node. This node is locked and used for
            storing the status of the build list in the scene

            status key:
                -1 = failed
                0  = not built
                1  = previously build
                2  = built this time
        """

        # Find current step node and make sure it has the same number of steps as our build list.
        # If not then we need a clean step node

        current_sel = mc.ls(sl=1)

        self.step_node = ''

        name = self.__name__+'_cmRigbuildSteps'

        step_node = [n.split('.')[0] for n in mc.ls(name+'.stepsArray')]

        if step_node:
            step_node = step_node[0]

            current_sel = mc.ls(sl=1)

            if len(mc.getAttr(step_node+'.stepsArray') or []) != len(self.build_list):
                mc.delete(step_node)
                step_node = ''

            if current_sel:
                mc.select(mc.ls(current_sel))

        if not step_node:
            current_sel = mc.ls(sl=1)

            step_node = mc.createNode('mute', n=name)
            mc.addAttr(step_node, ln='stepsArray', dt='floatArray', k=1)
            mc.addAttr(step_node, ln='asset', dt='string')

            array = [int(0)]*len(self.build_list)
            mc.setAttr(step_node+'.stepsArray', array, type='floatArray')
            mc.setAttr(step_node+'.asset', asset, type='string')

            mc.select(current_sel)

        if step_node:
            self.step_node = step_node

    @classmethod
    def get_status(self):
        """Get an array of values forthe status of each step in the build list"""

        self.get_step_node()

        self.status_array = [int(f) for f in mc.getAttr(self.step_node+'.stepsArray')]
        self.enabled_array = [s.get('enabled') for s in self.build_list]

        if not len(self.enabled_array) == len(self.build_list):
            mc.warning('Build list dictionary is out of whack! Go fix it!')

    @classmethod
    def set_status(self, index, value, all_values=[]):
        """Set a status value for a single step in the build OR set the enabled state.

            value key:
                -1 = failed
                0  = not built
                1  = previously build
                2  = built this time

            :enabled:

        """

        self.get_step_node()
        self.get_status()

        if index > len(self.build_list):
            index = len(self.build_list)

        self.get_status()

        array = self.status_array
        if all_values:
            array = all_values

        for idx in range(len(array)):
            if array[idx] == 3:
                array[idx] = 2

        array[index] = int(value)

        mc.setAttr(self.step_node+'.stepsArray', array, type='floatArray')
        self.get_status()

    @classmethod
    def set_enabled(self, index, value, verbose=False):

        value = bool(value)

        self.get_step_node()
        self.get_status()

        if index > len(self.build_list):
            index = len(self.build_list)

        if self.enabled_array[index] is None:
            return

        if self.enabled_array[index] == value:
            return

        self.enabled_array[index] = value
        self.save_enabled_state_to_build_file(self.enabled_array)

        for i, value in enumerate(self.enabled_array):
            if 'enabled' in self.build_list[i].keys():
                self.build_list[i]['enabled'] = self.enabled_array[i]

        if verbose:
            print self.enabled_array
            print self.__name__
            print index
            print value

        self.get_status()

    @classmethod
    def get_next_step(self):

        self.get_step_node()
        self.get_status()

        last = 0
        for i, value in enumerate(self.status_array):
            if value > 0:
                last = i+1

        return last

    @classmethod
    def save_enabled_state_to_build_file(self, enabled_array):
        """Write the enabled states list to the original build list file."""

        # get file
        asset = self.__module__.replace('_buildList','')
        file_path = os.path.join(env.get_rigbuild_path(asset), asset+'_buildList.py')

        if not os.path.isfile(file_path):
            mc.warning('Cannot save build step enabled_state state!')
            return

        with open(file_path) as f:
            lines = f.readlines()

        class_name = self.__name__
        step_count = 0

        for line_number, line in enumerate(lines):
            if 'class '+class_name in re.sub(' +', ' ', line):
                for i in range(line_number, len(lines)):
                    if '"label":' in re.sub(' +', '', lines[i].replace("'", '"')):

                        if enabled_array[step_count] is None:
                            #print 'skipping: '+str(step_count)
                            step_count += 1
                            continue

                        for ii in range(i, len(lines)):
                            if 'enabled' in lines[ii]:
                                #print str(step_count)+' >> '+lines[ii]
                                lines[ii] = lines[ii].split(':')[0]+': '+str(enabled_array[step_count])+',\n'
                                break

                        step_count += 1

                        if step_count >= len(enabled_array):
                            break

        all_lines = ''.join(lines)
        with open(file_path, 'w') as f:
            f.write(all_lines)
            print 'Updated enabled states for {0}: {1}'.format(class_name, file_path)

    @classmethod
    def set_use_plugin(self, use_plugin):
        """Write the enabled states list to the original build list file."""

        # get file
        asset = self.__module__.replace('_buildList','')
        file_path = os.path.join(env.get_rigbuild_path(asset), asset+'_buildList.py')

        if not os.path.isfile(file_path):
            mc.warning('Cannot save use_plugin state!')
            return

        with open(file_path) as f:
            lines = f.readlines()

        class_name = self.__name__

        for line_number, line in enumerate(lines):

            if 'class '+class_name in re.sub(' +', ' ', line):
                for i in range(line_number, len(lines)):
                    if "use_plugin_nodes" in lines[i]:
                        if use_plugin:
                            os.environ['use_plugin_nodes'] = 'True'
                            lines[i] = lines[i].split('=')[0]+'= True\n'
                        else:
                            os.environ['use_plugin_nodes'] = 'False'
                            lines[i] = lines[i].split('=')[0]+'= False\n'
                        break

        all_lines = ''.join(lines)
        with open(file_path, 'w') as f:
            f.write(all_lines)
            print 'Updated use plugin state for {0}: {1}'.format(class_name, file_path)






