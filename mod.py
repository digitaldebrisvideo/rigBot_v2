from functools import partial as pt
import inspect
import imp
import os
import re
import shutil

def get_exception():
    """Throw all nodes in scene into a temp namespace
        to compare newly built guide nodes. Thissi  to avoid node name clashes.

    Returns:
        :Raised Exception and stack trace: (str)"""

    return "".join(traceback.format_exception(*sys.exc_info()))

def partial(fn_name, *args, **kwargs):

    fn_name = fn_name.strip()
    if fn_name.startswith('mc.'):
        fn_name = fn_name.replace('mc.', 'maya.cmds.')
    elif fn_name.startswith('cmds.'):
        fn_name = fn_name.replace('cmds.', 'maya.cmds.')

    try:
        fn_mods = ['rigBot.'+fn_name,
                   'rigBot.asset.'+fn_name,
                   'rigBot.data.'+fn_name,
                   'rigBot.gui.'+fn_name,
                   'rigBot.partsLibrary.'+fn_name,
                   'rigBot.partsLibrary.generic.'+fn_name,
                   fn_name]

        for n in fn_mods:
            try:
                result = import_module(n, r=True, v=False, quiet=True)
                result = pt(result, *args, **kwargs)
                break

            except:
                pass

    except SyntaxError as e:
        result = get_exception()
    except ImportError as e:
        result = get_exception()
    except Exception as e:
        result = get_exception()

    return result

def import_module(name, r=True, v=False, quiet=True):

    msg = None
    mod_path = ''

    try:
        # importing from file path
        if os.path.isfile(name) and name.endswith('.py') or name.endswith('.pyc'):
            mod_path = str(name)
            mod_name = os.path.splitext(os.path.split(mod_path)[-1])[0]
            mod = imp.load_source(mod_name, mod_path)
            return mod

        else:

            # do the initial import of everything
            components = name.split('.')
            mod = __import__(components[0])
            mod_path = mod.__file__

            for comp in components[1:]:
                mod = getattr(mod, comp)

            # if we're reloading it, then reload the module and re-import
            if r:
                if inspect.ismodule(mod):
                    reload(mod)
                    mod_path = mod.__file__

                    if v:
                        print 'Reloading: '+mod.__name__

                else:
                    # find hte module
                    mod_name = mod.__module__.split('.')[-1]
                    idx = components.index(mod_name)

                    components = name.split('.')
                    mod = __import__(components[0])

                    if idx == 0:
                        reload(mod)
                        mod_path = mod.__file__
                        if v:
                            print 'Reloading: '+mod.__name__

                    for i, comp in enumerate(components[1:]):
                        mod = getattr(mod, comp)

                        if i+1 == idx:
                            reload(mod)
                            mod_path = mod.__file__
                            if v:
                                print 'Reloading: '+mod.__name__
            return mod

    except SyntaxError as e:
        msg = 'SYNTAX ERROR: lines (%s-%s): %s%s' % (e.lineno, e.offset, e.text, e.filename)+' :: '+name+' :: '+mod_path
        if quiet:
            return msg
        else:
            raise SyntaxError(msg)

    except ImportError as e:
        msg = 'IMPORT ERROR: '+e.__class__.__name__+': '+str(e)+' :: '+name+' :: '+mod_path
        if quiet:
            return msg
        else:
            raise ImportError(msg)

    except Exception as e:
        msg = 'ERROR: '+e.__class__.__name__+': '+str(e)+' :: '+name+' :: '+mod_path
        if quiet:
            return msg
        else:
            raise Exception(msg)

def update_build_list(asset=None):

    from rigBot import env

    if not asset:
        asset =  env.get_asset()

    path = os.path.join(env.get_rigbuild_path(), asset+'_buildList.py')
    if not os.path.isfile(path):
        return

    # read lines from source
    lines = []
    with open(path) as f:
        lines = f.readlines()

    # check if it needsto be updated
    for l in lines:
        if 'mod.partial' in l:
            return

    # swap import calls for new import calls
    si = None
    ei = None
    for i, line in enumerate(lines):
        line = re.sub(' +',' ', line)

        if 'from functools import partial' in line:
            si = i

        elif 'class Default' in line:
            ei = i
            break

    new_lines = lines[:si]
    new_lines += ["from rigBot.asset import standardBuild\n",
                  "from rigBot import env\n",
                  "from rigBot import mod\n",
                  "\n",
                  "asset = env.get_asset()\n",
                  "\n"]

    new_lines += lines[ei:]

    # now swap all partials for mod.partial calls
    for i, line in enumerate(new_lines):
        if "'command':" in re.sub(' +', '', line):
            tokens = line.split(':')
            c_tokens = tokens[1].split('}')

            if 'partial' in c_tokens[0]:
                c_tokens[0] = c_tokens[0].replace('partial', '', 1).strip()[1:-1]

                a_tokens = c_tokens[0].split(',')
                a_tokens[0] = "'{0}'".format(a_tokens[0].strip())
                c_tokens[0] = ','.join(a_tokens)

            else:
                c_tokens[0] = "'{0}'".format(c_tokens[0].strip())

            c_tokens[0] = 'mod.partial({0})'.format(c_tokens[0])
            tokens[1] = '}'.join(c_tokens)
            new_line = ': '.join(tokens)

            if 'custom.' in new_line:
                new_line = re.sub("'custom.", "asset+'_custom.", new_line)

            new_lines[i] = new_line

    new_lines = [l.replace('standard_build.','standardBuild.') for l in new_lines]

    # rewrite buidl list file
    all_lines = ''.join(new_lines)

    if not os.path.isfile(path+'.orig.BAK'):
        print 'Creating backup: '+path+'.orig.BAK'
        shutil.copyfile(path, path+'.orig.BAK')

    with open(path, 'w') as f:
        f.write(all_lines)
        print 'Updated build list with new mod.partial function! '
