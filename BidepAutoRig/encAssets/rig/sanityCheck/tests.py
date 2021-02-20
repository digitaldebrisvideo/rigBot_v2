import pymel.core as pm

__author__ = 'jhachigian'

checklist = {}


def is_mesh(x):
    try:
        if x.type() == 'transform' and x.getShape().type() == 'mesh':
            return True
    except:
        pass
    return False


def get_duplicate_meshes(li):
    d = {}
    for x in li:
        bits = x.split(":")[-1].split("_")
        if len(bits) > 2:
            key = "%s/%s" % (bits[1], bits[2])
            if key not in d:
                d[key] = []
            d[key].append(x.name())
    keys = [x for x in d.keys() if len(d[x]) > 1]
    dups = {}
    for key in keys:
        dups[key] = d[key][:]
    return dups


def test_rig_xxx_grp():
    key = "rig_XXX_grp"
    result = not pm.objExists("rig_XXX_grp")
    checklist["tests"][key] = result
    """ message """
    if result:
        checklist["messages"][key] = "No \"rig_XXX_grp\" found."
    else:
        checklist["messages"][key] = "\"rig_XXX_grp\" found. Please rename."


def test_stray_groups():
    default_cams = ["persp", "top", "side", "front"]
    top_nodes = [x for x in pm.ls(assemblies=True) if x.name() not in default_cams]
    test = len(top_nodes) == 1
    checklist["results"]["top_nodes"] = top_nodes
    checklist["tests"]["top_nodes"] = test
    """ message """
    if test:
        msg = "Excellent. Only one root node found."
    else:
        names = [x.name() for x in top_nodes]
        msg = "The rig node has siblings other than the default cameras:\n" + "_" * 20 + "\n\n" + "\n".join(names)
    checklist["messages"]["top_nodes"] = msg


def test_selection_sets():
    checklist["results"]["selection_sets"] = {}
    checklist["tests"]["selection_sets"] = True
    missing = []
    for x in ["all_ctrls", "hand_Lt_ctrls", "hand_Rt_ctrls", "all_geo", "torso_ctrls"]:
        test = pm.objExists(x) and pm.PyNode(x).type() == 'objectSet'
        checklist["results"]["selection_sets"][x] = test
        if not test:
            checklist["tests"]["selection_sets"] = False
            missing.append(x)
    """ message """
    if checklist["tests"]["selection_sets"]:
        msg = "All selection sets are present."
    else:
        msg = "Missing selection sets:\n" + "_" * 20 + "\n\n" + "\n".join(missing)
    checklist["messages"]["selection_sets"] = msg


def test_display_layers():
    display_layers = [x for x in pm.ls(type="displayLayer") if x.name() != "defaultLayer"]
    test = len(display_layers) == 1 and display_layers[0].name().endswith("Geo_Layer") and \
           display_layers[0].name() != "XXXGeo_Layer" and \
           display_layers[0].getAttr("displayType") == 2
    checklist["results"]["displayLayers"] = display_layers
    checklist["tests"]["displayLayers"] = test
    """ message """
    if test:
        msg = "Display layers look good."
    else:
        names = [x.name() for x in display_layers]
        msg = "There should be only one display layer called \"<characterName>Geo_Layer\", " \
              "and its display type should be set to Reference. Found these layers:\n" \
              + "_" * 20 + "\n\n" + "\n".join(names)
    checklist["messages"]["displayLayers"] = msg


def test_namespaces():
    default_namespaces = [u'UI', u'shared']
    namespaces = [x for x in pm.namespaceInfo(":", listOnlyNamespaces=True) if x not in default_namespaces]
    test = len(namespaces) == 0
    checklist["results"]["namespaces"] = namespaces
    checklist["tests"]["namespaces"] = test
    """ message """
    if test:
        msg = "This house is clean."
    else:
        msg = "Found these non-default namespaces in the scene:\n" + "_" * 20 + "\n\n" + "\n".join(namespaces)
    checklist["messages"]["namespaces"] = msg


def test_non_meshes():
    all_geo = pm.sets("all_geo", query=True)
    not_meshes = [x for x in all_geo if not is_mesh(x)]
    key = "\"all_geo\" set: Non-meshes."
    test = len(not_meshes) == 0
    checklist["results"][key] = not_meshes
    checklist["tests"][key] = test
    """ message """
    if test:
        msg = "Found no non-meshes in the \"all_geo\" set."
    else:
        names = [x.name() for x in not_meshes]
        msg = "Found these non-meshes in the \"all_geo\" set:\n" + "_" * 20 + "\n\n" + "\n".join(names)
    checklist["messages"][key] = msg


def test_mesh_duplicates():
    all_geo = pm.sets("all_geo", query=True)
    key = "\"all_geo\" set: duplicate mesh names."
    duplicates = get_duplicate_meshes(all_geo)
    test = len(duplicates) == 0
    checklist["results"][key] = duplicates
    checklist["tests"][key] = test
    """ message """
    if test:
        msg = ["Found no duplicate meshes in the \"all_geo\" set."]
    else:
        msg = ["Found these duplicates in the \"all_geo\" set:",
               ""]
        for dup in duplicates:
            msg.append(dup)
            msg.append("____________")
            for d in duplicates[dup]:
                msg.append(d)
            msg.append("")
    checklist["messages"][key] = "\n".join(msg)


def test_all_ctrls():
    all_ctrls = pm.sets("all_ctrls", query=True)
    blacklist = "thumbEnd", "indexEnd", "middleEnd", "ringEnd", "pinkyEnd"
    anims = [x for x in pm.ls("*_anim") if not x.startswith(blacklist)]
    ctrl_set = set(all_ctrls)
    anim_set = set(anims)
    key = "\"all_ctrls\" set: missing controls."
    missing = [x for x in anim_set.difference(ctrl_set)]
    test = not bool(missing)
    checklist["results"][key] = missing
    checklist["tests"][key] = test
    """ message """
    if test:
        msg = "Found no missing anims in the \"all_ctrls\" set."
    else:
        names = [x.name() for x in missing]
        msg = "These anims need to be added to the \"all_ctrls\" set:\n" + "_" * 20 + "\n\n" + "\n".join(names)
    checklist["messages"][key] = msg


def test_geo_name(name):
    bits = name.split("_")
    if len(bits) < 9:
        return False
    if bits[0] not in ["chr", "prp", "env", "bld", "veh", "efx", "ldr"]:
        return False
    if bits[4] not in ["hi", "md", "lo"]:
        return False
    if bits[5] not in ["mesh", "xmesh", "vrp", "ffx", "phx", "krak", "cloth", "hair", "lgt", "ctl",
                       "pflow", "fpsource", "fpsurf", "fpgeo", "vvg"]:
        return False
    if bits[6] not in ["X", "disp2d", "disp3d", "dispRS", "dispNo"]:
        return False
    if bits[7] not in ["X", "sub0", "sub1", "sub2","sub3"]:
        return False
    if bits[8] not in ["X","nrndr"]:
        return False
    return True


def test_all_geo_contents():
    hi_meshes = pm.PyNode("hiRez_skinGeo_grp").listRelatives(allDescendents=True, type="mesh")
    hi_transforms = [x.getParent() for x in hi_meshes if test_geo_name(x.getParent().name())]
    hi_res = set(hi_transforms)
    all_geo = set(pm.sets("all_geo", query=True))
    key = "\"all_geo\" set: missing geometry"
    missing = [x for x in hi_res.difference(all_geo)]
    checklist["results"][key] = missing
    test = not bool(missing)
    checklist["tests"][key] = test
    if test:
        msg = "Found no missing geometry in the \"all_geo\" set."
    else:
        names = [x.name() for x in missing]
        msg = "This \"hiRez_skinGeo_grp\" geometry needs to be added to the \"all_geo\" set.\n"
        msg += "_" * 20 + "\n\n" + "\n".join(names)
    checklist["messages"][key] = msg


def test_all_geo_names():
    key = "\"all_geo\" set: Encore-compatible names"
    all_geo = pm.sets("all_geo", query=True)
    bad_objs = [x for x in all_geo if not test_geo_name(x)]
    bad_names = [x.name() for x in bad_objs]
    test = len(bad_names) == 0
    checklist["results"][key] = bad_objs
    checklist["tests"][key] = test
    if test:
        msg = "The objects in the \"all_geo\" set have Encore-compatible names.\n"
    else:
        msg = "The following in the \"all_geo\" set do not have Encore-compatible names:\n"
        msg += "_" * 20 + "\n\n" + "\n".join(bad_names)
    checklist["messages"][key] = msg


def test_lo_res_names():
    key = "\"loRez_skinGeo_grp\" group: Encore-compatible names"
    lo_res = pm.PyNode("loRez_skinGeo_grp").getChildren()
    bad_objs = [x for x in lo_res if not test_geo_name(x)]
    bad_names = [x.name() for x in bad_objs]
    test = len(bad_names) == 0
    checklist["results"][key] = bad_objs
    checklist["tests"][key] = test
    if test:
        msg = "The objects in the \"loRez_skinGeo_grp\" all have Encore-compatible names."
    else:
        msg = "The following in the \"loRez_skinGeo_grp\" group do not have Encore-compatible names "
        msg += "(important for sims):\n"
        msg += "_" * 20 + "\n\n" + "\n".join(bad_names)
    checklist["messages"][key] = msg


def test_shape_names():
    """
    Make sure each object tagged for geocache export has a shape name that can be parsed by Create Geocache.

    :return: None
    """
    def get_shape(n):
        shapes = n.getShapes()
        if not shapes:
            return None
        deformed = [x for x in shapes if x.endswith("formed")]
        if deformed:
            return deformed[-1]
        else:
            return shapes[0]

    def test_shape_name(obj):
        name = obj.name().split(":")[-1].split("|")[-1]
        bits = name.split("_")
        prefix = "_".join(bits[:3]) + "_"
        shp = get_shape(obj)
        if shp is None:  # skip this test.
            return True
        if shp.startswith(prefix):
            return True
        return False

    key = "\"all_geo\" set: Shape names"
    all_geo = pm.sets("all_geo", query=True)
    bad_objs = [x for x in all_geo if not test_shape_name(x)]
    bad_names = [x.name() + ":\r\n\t" + get_shape(x).name() for x in bad_objs]
    test = len(bad_names) == 0
    checklist["results"][key] = bad_objs
    checklist["tests"][key] = test
    """ message """
    if test:
        msg = "The objects in the \"all_geo\" set have good shape names.\n"
    else:
        msg = "The following in the \"all_geo\" set do not have good shape names:\n"
        msg += "_" * 20 + "\n\n" + "\n".join(bad_names)
    checklist["messages"][key] = msg


def tests():
    """
    Update the external checklist dictionary with the results of various tests.

    "True" means it passed the test. "False" means it failed the test.
    :return: None
    """
    checklist["tests"] = {}
    checklist["results"] = {}
    checklist["messages"] = {}
    """ run tests """
    test_rig_xxx_grp()
    test_stray_groups()
    test_selection_sets()
    # test_display_layers()
    test_namespaces()
    if pm.objExists("all_geo"):
        test_non_meshes()
        test_mesh_duplicates()
        test_all_geo_names()
        test_shape_names()
    if pm.objExists("all_geo") and pm.objExists("hiRez_skinGeo_grp"):
        test_all_geo_contents()
    # if pm.objExists("loRez_skinGeo_grp"):
    #     test_lo_res_names()
    if pm.objExists("all_ctrls"):
        test_all_ctrls()
