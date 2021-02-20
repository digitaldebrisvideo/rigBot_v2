import maya.cmds as cmds
import pymel.core as pm
import tools
import setupIK
reload(tools)
reload(setupIK)

__author__ = 'jhachigian'

debug = True


info = {'arm': {'targets': {"upr": ["shoulder", "elbow"], "lwr": ["elbow", "hand"]}, 'Lt': {}, 'Rt': {}},
        'leg': {'targets': {"upr": ["thigh", "uprKnee"], "lwr": ["knee", "foot"]}, 'Lt': {}, 'Rt': {}}}

end_map = {'hand_Lt_jnt': 'wrist_Lt_bind', 'hand_Rt_jnt': 'wrist_Rt_bind'}
upScene= cmds.upAxis(q=1, ax=1)

def make_curve(x, y):
    pos1 = pm.xform(x, query=True, worldSpace=True, translation=True)
    pos2 = pm.xform(y, query=True, worldSpace=True, translation=True)
    curv = pm.curve(degree=1, point=[pos1, pos2])
    return curv


def make_group(name, par=None):
    grp = pm.group(empty=True, world=True, name=name)
    if par is not None:
        pm.parent(grp, par)
    return grp


def make_locator(name, par):
    loc = pm.spaceLocator(name=name)
    if par is not None:
        pm.parent(loc, par)
    return loc


def add_knee_joints():
    x_offset = {"upr": -2, "lwr": 2}
    y_offset = {"Lt": 2, "Rt": -2}
    for side in ["Lt", "Rt"]:
        knee = "knee_%s_jnt" % side
        """ make bind joint """
        pm.select(clear=True)
        bnd_name = "knee_%s_VJ_bind" % side
        if not pm.objExists(bnd_name):
            bnd = pm.joint(name=bnd_name)
            pm.parent(bnd, knee, relative=True)
        else:
            bnd = pm.PyNode(bnd_name)
        """ set bind joint attributes """
        tools.set_override_color(bnd, 17)
        rad = bnd.getAttr("radius") * 2
        bnd.setAttr("radius", rad)
        """ enter bind joint into dictionary """
        info['leg'][side]['midBind'] = bnd
        """ make offset joints """
        for pre in ["upr", "lwr"]:
            pm.select(knee)
            jnt_name = "%sKnee_%s_jnt" % (pre, side)
            if not pm.objExists(jnt_name):
                jnt = pm.joint(name=jnt_name)
                jnt.setParent(bnd)
                yo = y_offset[side]
                jnt.setAttr("translate", (x_offset[pre] * (yo/2), yo, 0))
            else:
                jnt = pm.PyNode(jnt_name)
            try:
                info['leg'][side][pre]['kneeJoint'] = jnt
                info['leg'][side][pre]['midBind'] = bnd
            except KeyError:
                tools.debug_print("The info dictionary has not yet been initialized.", dbg=debug)


def add_elbow_joints():
    for side in ["Lt", "Rt"]:
        elbow = "elbow_%s_jnt" % side
        """ make bind joint """
        pm.select(clear=True)
        bnd_name = "elbow_%s_VJ_bind" % side
        bnd = pm.joint(name=bnd_name)
        pm.parent(bnd, elbow, relative=True)
        info['arm'][side]["upr"]['midBind'] = bnd
        """ set bind joint attributes """
        tools.set_override_color(bnd, 17)
        rad = bnd.getAttr("radius") * 2
        bnd.setAttr("radius", rad)


def make_skin_joint(d, li, x):
    par = d['const']
    grp_name = "%s%sRibbon%sPos_%s_grp" % (li[0], li[1].title(), x, li[2])
    loc_name = grp_name.replace("_grp", "_loc").replace("Pos", "AimAt")
    up_name = grp_name.replace("_grp", "_loc").replace("Pos", "UpObj")
    grp = make_group(grp_name, None)
    loc1 = pm.spaceLocator(name=loc_name, position=(0, 0, 0))
    loc2 = pm.spaceLocator(name=up_name, position=(0, 0, 0))
    pm.parent(loc1, grp)
    pm.parent(loc2, grp)
    pm.parent(grp, par, relative=True)
    loc2.setAttr("translate", d['offset'])
    pm.select(loc1)
    d['grps'].append(grp)
    d['aims'].append(loc1)
    d['ups'].append(loc2)
    if x != "Mid":
        jnt_name = grp_name.replace("_grp", "_jnt").replace("Pos", "")
        jnt = pm.joint(name=jnt_name)
        d['jnts'].append(jnt)
    return grp


def init_targets(d):
    side = d['side']
    for pre in ["upr", "lwr"]:
        tgts = d['targets']
        if tgts[pre][1] == "foot":
            end = "bind"
        else:
            end = "jnt"
        tgt1 = "%s_%s_jnt" % (tgts[pre][0], side)
        tgt2 = "%s_%s_%s" % (tgts[pre][1], side, end)
        d[pre]['targets'] = [tgt1, tgt2]
        if d['key'] == 'leg':
            d[pre]['knee'] = "knee_%s_jnt" % side


def make_hierarchy(d):
    key = d['key']
    side = d['side']
    root_name = "%sRig_%s_grp" % (key, side)
    if not pm.objExists(root_name):
        root_grp = make_group(root_name, None)
    else:
        root_grp = pm.PyNode(root_name)
    rbbn_grp = make_group("%sRibbonRig_%s_grp" % (key, side), root_grp)
    d['root'] = root_grp
    d['ribbon'] = rbbn_grp
    for pre in ["upr", "lwr"]:
        rbbn_sub_grp = make_group("%s%sRibbonRig_%s_grp" % (pre, key.title(), side), rbbn_grp)
        const_grp = make_group("%s%sRibbonConst_%s_grp" % (pre, key.title(), side), rbbn_sub_grp)
        d[pre]['sub_ribbon'] = rbbn_sub_grp
        d[pre]['const'] = const_grp


def make_aim_reader(d):
    side = d['side']
    tgt_jnt_name = d["upr"]['targets'][0]
    mid_jnt_name = d["upr"]['targets'][1]
    end_jnt_name = d["lwr"]['targets'][1]
    mid = d['targets']["upr"][1]
    if d['key'] == 'leg':
        mid_jnt_name = mid_jnt_name.replace("uprKnee", "knee")
        mid = mid.replace("uprKnee", "knee")
    """ build hierarchy """
    ctrl_name = d['ctrlGrp'].name()
    aim_name = "%sAimReader_%s_grp" % (mid, side)
    aim_loc_name = aim_name.replace("_grp", "_loc")
    half_name = "%sHalfRot_%s_grp" % (mid, side)
    anim_name = "%sRibbon_%s_anim" % (mid, side)
    li = [(ctrl_name, None, 'transform', None),
          (aim_name, ctrl_name, 'transform', mid_jnt_name),
          (aim_loc_name, aim_name, 'locator', aim_name),
          (half_name, aim_loc_name, 'transform', aim_loc_name),
          (anim_name, half_name, 'transform', half_name)]
    tools.make_ctrl_hierarchy(li)
    tools.match_to(aim_name, mid_jnt_name)
    for pre in ["upr", "lwr"]:
        d[pre]['aimReader'] = [pm.PyNode(x) for x in [aim_name, aim_loc_name, half_name, anim_name]]
        d[pre]['twistCtrlMid'] = pm.PyNode(anim_name)
    """ apply shape """
    shp = tools.apply_shape(anim_name, "fourPointArrow_anim")
    tools.rotate_shape(shp, (0, 0, 90))
    """ setup attributes and constraints """
    loc = pm.PyNode(aim_loc_name)
    if d['key'] == 'arm':
        loc.setAttr("rotateOrder", 3)
    loc.getShape().setAttr("visibility", False)
    pm.parentConstraint(tgt_jnt_name, aim_name, maintainOffset=True)
    if d['key'] == 'leg':
        pm.parentConstraint(anim_name, d["upr"]["midBind"])
    pm.pointConstraint(mid_jnt_name, loc)
    if side == "Lt":
        av = (1, 0, 0)
        uv = (0, 1, 0)
    else:
        av = (-1, 0, 0)
        uv = (0, -1, 0)
    pm.aimConstraint(end_jnt_name, loc, aimVector=av, upVector=uv,
                     worldUpType='object', worldUpObject=end_jnt_name)
    """ setup nodes """
    md_name = tools.get_new_name(half_name, "UTmd")
    md = pm.createNode("multiplyDivide", name=md_name)
    for attr in ["input2X", "input2Y", "input2Z"]:
        md.setAttr(attr, -0.5)
    md.setAttr("operation", 1)
    pm.connectAttr(loc + ".rotate", md + ".input1")
    pm.connectAttr(md + ".output", half_name + ".rotate")


def make_roll_vector(d):
    key = d['key']
    side = d['side']
    par_dict = {'leg': 'hips_Mid_jnt', 'arm': 'clavicle_%s_bind' % side}
    par = pm.PyNode(par_dict[key])
    # par = pm.PyNode("%s_bind" % par_dict[key])
    mid = pm.PyNode(d['upr']['targets'][1])
    k = d['upr']['targets'][0]
    pv = tools.get_new_name(setupIK.pvDict[k][0], "anim")
    """ build vector joints """
    objects = [par]
    objects += [x for x in par.getChildren() if x.find("_" + side + "_") != -1]
    tgts = pm.duplicate(objects, renameChildren=True, inputConnections=False, parentOnly=True)
    vec = tgts[0]
    vec_end = tgts[1]
    vec.rename("%sRollVector_%s_jnt" % (key, side))
    vec_end.rename("%sRollVectorEnd_%s_jnt" % (key, side))
    if key == 'arm':
        offset = par.getAttr("translateY")
        if upScene == 'z':
            pm.move(0, offset, 0, vec, relative=True, worldSpace=True)
        if upScene == 'y':
            pm.move(0, 0, offset*-1, vec, relative=True, worldSpace=True)        
            newVal = cmds.getAttr(vec  + ".translateY")
            print vec, ' moved', newVal
            print vec, ' Y-Up'
    else:
        offset = abs(vec_end.getAttr("translateZ")) * 2
        trans = [offset/2.0, 0, 0]
        if side == "Rt":
            offset *= -1
            trans[0] *= -1
        vec_end.setAttr("translate", trans)
        pm.move(offset, 0, 0, vec, relative=True, worldSpace=True)
    vec.setParent(par)
    """ add locators """
    vec_up = make_locator("%sRollVectorUpObj_%s_loc" % (key, side), par)
    tools.match_to(vec_up, vec)
    if key == 'arm':
        if upScene == 'z':
            pm.move(0, 0, offset, vec_up, relative=True, worldSpace=True)
        if upScene == 'y':
            pm.move(0, offset*-1, 0, vec_up, relative=True, worldSpace=True)
            print vec_up, ' Y-Up'
    else:
        pm.move(offset * 2, 3, 0, vec_up, relative=True, worldSpace=True)
    vectors = {"arm": {"Lt": {"av": (1, 0, 0), "uv": (0, 1, 0)},
                       "Rt": {"av": (-1, 0, 0), "uv": (0, 1, 0)}},
               "leg": {"Lt": {"av": (1, 0, 0), "uv": (0, 0, -1)},
                       "Rt": {"av": (-1, 0, 0), "uv": (0, 0, -1)}} }
    av = vectors[key][side]['av']
    uv = vectors[key][side]['uv']
    pm.aimConstraint(mid, vec, aimVector=av, upVector=uv, worldUpType='object', worldUpObject=vec_up)
    vec_end_up = make_locator("%sRollReaderUpObj_%s_loc" % (key, side), vec)
    if key == 'arm':
        tools.match_to(vec_end_up, pv)
    else:
        vec_end_up.setAttr("translate", (30, 0, -30))
        if side == "Rt":
            vec_end_up.setAttr("translate", (-30, 0, -30))
        vec_end_up.setAttr("rotate", (0, 0, 0))

    """ add to dictionary """
    d['rollVector'] = [vec, vec_end, vec_up, vec_end_up]


def make_roll_reader(d):
    side = d['side']
    key = d['key']
    par = pm.PyNode(d['upr']['targets'][0])
    mid = pm.PyNode(d['upr']['targets'][1])
    vec_up = d['rollVector'][-1]
    jnt = pm.duplicate(par, parentOnly=True, inputConnections=False)[0]
    jnt.rename("%sRollReader_%s_jnt" % (key, side))
    jnt.setParent(par)
    if side == "Lt":
        av = (1, 0, 0)
        uv = (0, 0, -1)
    else:
        av = (-1, 0, 0)
        uv = (0, 0, 1)
    pm.aimConstraint(mid, jnt, aimVector=av, upVector=uv, worldUpType='object', worldUpObject=vec_up)
    d['upr']['twistReader'] = jnt


def make_end_twist_reader(d, end_name):
    side = d['side']
    par = d['root']
    mid = pm.PyNode(d['upr']['targets'][1])
    if end_name == "foot":
        """ ensure that mid gets "knee_Lt_jnt" as an assignment """
        mid = pm.PyNode(d['lwr']['targets'][0])
    end = "%s_%s_bind" % (end_name, side)
    rdr_name = "%sTwistReader_%s" % (end_name, side)
    tgt_name = "%sTwistTarget_%s" % (end_name, side)
    """ build hierarchy """
    rdr_grp = make_group("%s_grp" % rdr_name, par)
    rdr_loc = make_locator("%s_loc" % rdr_name, rdr_grp)
    tgt_grp = make_group("%s_grp" % tgt_name, rdr_grp)
    tgt_loc = make_locator("%s_loc" % tgt_name, tgt_grp)
    """ build constraints """
    pm.parentConstraint(mid, rdr_grp)
    pm.parentConstraint(end, tgt_grp)
    if side == "Lt":
        av = (1, 0, 0)
        uv = (0, 0, 1)
        wv = (0, 0, 1)
    else:
        av = (-1, 0, 0)
        uv = (0, 0, -1)
        wv = (0, 0, -1)
    pm.aimConstraint(tgt_loc, rdr_loc, aimVector=av, upVector=uv, worldUpType='objectrotation',
                     worldUpObject=tgt_loc, worldUpVector=wv)
    """ clean up and dictionary building """
    rdr_grp.setAttr("visibility", False)
    d['lwr']['endTwist'] = [rdr_grp, rdr_loc, tgt_grp, tgt_loc]
    d['lwr']['twistReader'] = rdr_loc


def make_twist_anims(d):
    key = d['key']
    side = d['side']
    par = d['ctrlGrp']
    attrs = {"arm": {"upr": [0.5, 0.63, 0.75, 0.85, 0.95], "lwr": [0.95, 0.75, 0.5, 0.25, 0.0]},
             "leg": {"upr": [0.05, 0.25, 0.5, 0.75, 0.95], "lwr": [0.95, 0.75, 0.5, 0.25, 0.05]},
             }
    rots = {"arm": {"Lt": {"upr": (0, 0, 0), "lwr": (0, 0, 0)},
                    "Rt": {"upr": (180, 0, 0), "lwr": (180, 0, 0)}},
            "leg": {"Lt": {"upr": (0, 0, 0), "lwr": (0, 0, 0)},
                    "Rt": {"upr": (0, 0, 180), "lwr": (180, 0, 0)}},
            }
    header = {'arm': 'elbowInf', 'leg': 'kneeInf'}
    for pre in ["upr", "lwr"]:
        grp_name = "%s%sTwist_%s_grp" % (pre, key.title(), side)
        a_name = tools.get_new_name(grp_name, "a0")
        anim_name = tools.get_new_name(grp_name, "anim")
        grp = make_group(grp_name, par)
        a0 = make_group(a_name, grp)
        anim = make_group(anim_name, a0)
        """ apply shape """
        shp = tools.apply_shape(anim, "curveArrow_anim")
        tools.rotate_shape(shp, rots[key][side][pre])
        """ lock attrs """
        for attr in ["translateX", "translateY", "translateZ",
                     "scaleX", "scaleY", "scaleZ",
                     "rotateY", "rotateZ", "visibility"]:
            anim.attr(attr).set(channelBox=False, keyable=False)
            anim.attr(attr).lock()
        """ make "jnt" attrs """
        j_attrs = ["jnt%02d" % x for x in xrange(1, 6)]
        tools.create_attributes(anim, header[key], j_attrs)
        for x in xrange(1, 6):
            attr = "jnt%02d" % x
            anim.setAttr(attr, attrs[key][pre][x-1])
            anim.attr(attr).lock()
        """ add constraints """
        if pre == 'lwr':
            upr_tgt = d[pre]['targets'][0]
            lwr_tgt = d[pre]['targets'][1]
            if key == "arm":
                lwr_tgt = end_map[lwr_tgt]
                tools.match_to(grp, lwr_tgt)
            else:
                tools.match_xyz(grp, lwr_tgt)
                if side == "Lt":
                    grp.setAttr("rotate", (0, 90, 180))
                else:
                    grp.setAttr("rotate", (0, -90, 0))
            pm.parentConstraint(upr_tgt, grp, maintainOffset=True)
            pm.pointConstraint(lwr_tgt, a0)
        elif pre == 'upr':
            upr_tgt = d[pre]['twistReader']
            pm.parentConstraint(upr_tgt, a0)
        """ add data """
        d[pre]['twistAnim'] = [grp, a0, anim]
        d[pre]['twistCtrl'] = anim


def make_bind_joints(d):
    side = d['side']
    for pre in ["upr", "lwr"]:
        tgt = d[pre]['targets'][0]
        if d['key'] == 'leg' and pre == 'lwr':
            tgt = d[pre]['knee']
        li = []
        suffixes = ["%02d" % x for x in xrange(1, 6)]
        suffixes.append("Mid")
        for suffix in suffixes:
            jnt_name = "%s%sRibbon%s_%s_bind" % (pre, d['key'].title(), suffix, side)
            if suffix == "Mid":
                jnt_name = tools.get_new_name(jnt_name, "jnt")
            pm.select(clear=True)
            jnt = pm.joint(name=jnt_name)
            pm.parent(jnt, tgt, relative=True)
            li.append(jnt)
        d[pre]['joints'] = li


def make_nurbs(d):
    key = d['key']
    side = d['side']
    for pre in ["upr", "lwr"]:
        name = "%s%sRibbon_%s_surf" % (pre, key.title(), side)
        p1, p2 = d[pre]['targets']
        if pre == "lwr" and key == "leg":  # replace "knee_##_jnt" with "lwrKnee_##_jnt"
            p1 = pre + p1[0].capitalize() + p1[1:]
        curv1 = make_curve(p1, p2)
        curv2 = pm.duplicate(curv1)[0]
        if upScene == 'y':
            #cmds.warning('**************************** Y-up system ****************************')
            pm.move(0, 0, -1, curv1, relative=True, localSpace=True, worldSpaceDistance=True)
            pm.move(0, 0, 1, curv2, relative=True, localSpace=True, worldSpaceDistance=True)
        if upScene == 'z':
            #cmds.warning('**************************** Z-up system ****************************')    
            pm.move(0, 1, 0, curv1, relative=True, localSpace=True, worldSpaceDistance=True)
            pm.move(0, -1, 0, curv2, relative=True, localSpace=True, worldSpaceDistance=True)
        loft = pm.loft(curv1, curv2, constructionHistory=True, uniform=True, close=False, autoReverse=True,
                       degree=1, sectionSpans=1, reverseSurfaceNormals=True)
        rebuild = pm.rebuildSurface(loft[0], constructionHistory=True, replaceOriginal=True, rebuildType=0, endKnots=1,
                                    keepRange=False, keepControlPoints=False, keepCorners=True, spansU=1, degreeU=3,
                                    spansV=1, degreeV=1, tolerance=0.01, fitRebuild=0, direction=2)
        pm.delete(rebuild[0], constructionHistory=True)
        pm.delete(curv1, curv2)
        rebuild[0].rename(name)
        d[pre]['nurbs'] = rebuild[0]
        pm.parent(rebuild[0], d[pre]['sub_ribbon'])


def make_skin_joints(d):
    side = d['side']
    for pre in ["upr", "lwr"]:
        if side == "Lt":
            d[pre]['offset'] = [0, 20, 0]
        else:
            d[pre]['offset'] = [0, -20, 0]
        li = [pre, d['key'], side]
        for k in ['grps', 'aims', 'ups', 'jnts']:
            d[pre][k] = []
        for x in ["Top", "Mid", "Btm"]:
            make_skin_joint(d[pre], li, x)
        """                   """
        """ apply constraints """
        """                   """
        tgt1 = d[pre]['targets'][0]
        tgt2 = d[pre]['targets'][1]
        if d['key'] == "arm" and pre == "lwr":
            tgt2 = end_map[tgt2]
        pm.parentConstraint(tgt1, d[pre]['const'])
        """ apply point constraints """
        grps = d[pre]['grps']
        aims = d[pre]['aims']
        ups = d[pre]['ups']
        if d['key'] == 'arm':
            p_tgt = d[pre]['aimReader'][-1]
        else:
            p_tgt = d[pre]['kneeJoint']
        if pre == "upr":
            pm.pointConstraint(tgt1, grps[0])
            pm.pointConstraint(p_tgt, grps[2])
        else:
            pm.pointConstraint(p_tgt, grps[0])
            pm.pointConstraint(tgt2, grps[2])
        pm.pointConstraint(aims[0], aims[2], grps[1])
        """ apply aim constraints """
        pm.aimConstraint(grps[2], aims[0], aimVector=(1, 0, 0), upVector=(0, 1, 0),
                         worldUpType='object', worldUpObject=ups[0])
        pm.aimConstraint(grps[2], aims[1], aimVector=(1, 0, 0), upVector=(0, 1, 0),
                         worldUpType='object', worldUpObject=ups[1])
        pm.aimConstraint(grps[0], aims[2], aimVector=(-1, 0, 0), upVector=(0, 1, 0),
                         worldUpType='object', worldUpObject=ups[2])


def make_skin_cluster(d):
    for pre in ["upr", "lwr"]:
        nurbs = d[pre]['nurbs']
        jnts = d[pre]['jnts']
        jnts.insert(1, d[pre]['joints'][-1])
        pm.select(jnts)
        skn_name = tools.get_new_name(nurbs, "skin")
        skn = pm.skinCluster(jnts, nurbs, frontOfChain=True, toSelectedBones=True, bindMethod=1, skinMethod=0,
                             weightDistribution=0, maximumInfluences=3, obeyMaxInfluences=1, dropoffRate=0.99,
                             normalizeWeights=1, name=skn_name)
        map = {0: jnts[0], 1: jnts[1], 2: jnts[1], 3: jnts[2]}
        for x in xrange(4):
            pm.skinPercent(skn, nurbs + ".cv[%d][0:1]" % x, transformValue=(map[x], 1.0), normalize=True)


def make_follicles(d):
    key = d['key']
    side = d['side']
    for pre in ["upr", "lwr"]:
        rbbn_sub_grp = d[pre]['sub_ribbon']
        follicle_grp = make_group("%s%sFollicles_%s_grp" % (pre, key.title(), side), rbbn_sub_grp)
        follicle_prefix = "%s%sFol_%s_follicle" % (pre, key.title(), side)
        u_values = [0.05, 0.25, 0.5, 0.75, 0.95]
        li = []
        for i in xrange(1, 6):
            fol_name = "%s%02d" % (follicle_prefix, i)
            fol = pm.createNode('follicle')
            par = fol.getParent()
            par.rename(fol_name)  # this renames the shape as well.
            pm.connectAttr(fol + ".outRotate", par + ".rotate")
            pm.connectAttr(fol + ".outTranslate", par + ".translate")
            shp = pm.PyNode(d[pre]['nurbs']).getShape()
            pm.connectAttr(shp + ".local", fol + ".inputSurface")
            pm.connectAttr(shp + ".worldMatrix[0]", fol + ".inputWorldMatrix")
            fol.setAttr("parameterU", u_values[i-1])
            fol.setAttr("parameterV", 0.5)
            li.append(par)
        pm.parent(li, follicle_grp)
        d[pre]['follicles'] = li
        d[pre]['follicle_grp'] = follicle_grp


def setup_shaper_nodes(d):
    rdr = d['twistReader']
    ctl = d['twistCtrl']
    mid = d['twistCtrlMid']
    a0 = d['shapers']['a0']
    pre = d['prefix']
    key = d['key']
    side = d['side']
    if key == 'arm':
        tgt = 'elbow'
    else:
        tgt = 'knee'
    for x in xrange(5):
        num = x + 1
        sub1 = "%s%s" % (pre, key.title())
        sub2 = "%02d_%s" % (num, side)
        """ make names """
        rev_name = "%sTwistFractionRev%s_UTrev" % (sub1, sub2)
        frc_name = "%sReaderFraction%s_UTmdl" % (sub1, sub2)
        all_name = "%sAddAll%s_UTadl" % (sub1, sub2)
        mlt_name = "%sTwistFraction%s_UTmdl" % (sub1, sub2)
        mcl_name = "%s%sFraction%s_UTmdl" % (sub1, tgt.title(), sub2)
        abt_name = "%sBothTwists%s_UTadl" % (sub1, sub2)
        """ make nodes """
        rev = pm.createNode('reverse', name=rev_name)                   # $fractionReverse
        frc = pm.createNode('multDoubleLinear', name=frc_name)          # $readerFraction
        all = pm.createNode('addDoubleLinear', name=all_name)           # $addAll
        mcl = pm.createNode('multDoubleLinear', name=mcl_name)          # $twistCtrlFractionMult
        mlt = pm.createNode('multDoubleLinear', name=mlt_name)          # $elbowKneeTwistCtrlFractionMult
        abt = pm.createNode('addDoubleLinear', name=abt_name)           # $addBothTwists
        """ make connections """
        pm.connectAttr(ctl + ".jnt%02d" % num, rev + ".inputX")
        pm.connectAttr(rev + ".outputX", frc + ".input2")
        pm.connectAttr(rdr + ".rotateX", frc + ".input1")
        pm.connectAttr(frc + ".output", all + ".input1")
        pm.connectAttr(ctl + ".rotateX", mcl + ".input1")
        pm.connectAttr(rev + ".outputX", mcl + ".input2")
        pm.connectAttr(mid + ".rotateX", mlt + ".input1")
        pm.connectAttr(ctl + ".jnt%02d" % num, mlt + ".input2")
        pm.connectAttr(mcl + ".output", abt + ".input1")
        pm.connectAttr(mlt + ".output", abt + ".input2")
        pm.connectAttr(abt + ".output", all + ".input2")
        """ final touch """
        if side == 'Lt':
            pm.connectAttr(all + ".output", a0[x] + ".rotateX")
        else:
            flip_name = "%sFlipValue%s_UTmdl" % (sub1, sub2)
            flip = pm.createNode("multiplyDivide", name=flip_name)
            flip.setAttr("input2X", -1.0)
            pm.connectAttr(all + ".output", flip + ".input1X")
            pm.connectAttr(flip + ".outputX", a0[x] + ".rotateX")


def make_shapers(d):
    key = d['key']
    side = d['side']
    par = make_group("%sShaper_%s_grp" % (key, side), None)
    d['shaper_group'] = par
    for pre in ["upr", "lwr"]:
        shaper_dict = {'grps': [], 'a0': [], 'anims': []}
        for x in xrange(1, 6):
            name = "%s%sShaper%02d_%s_grp" % (pre, key.title(), x, side)
            grp = make_group(name, par)
            a0 = make_group(name.replace("_grp", "_a0"), grp)
            anim = make_group(name.replace("_grp", "_anim"), a0)
            """ append to dictionary """
            shaper_dict['grps'].append(grp)
            shaper_dict['a0'].append(a0)
            shaper_dict['anims'].append(anim)
            """ apply constraints """
            bnd = d[pre]['joints'][x-1]
            pm.parentConstraint(d[pre]['follicles'][x-1], grp)
            tools.match_to(bnd, anim)
            pm.makeIdentity(bnd, apply=True, rotate=True)
            # pm.makeIdentity(bnd, apply=True, jointOrient=True, rotate=True)
            pm.parentConstraint(anim, bnd, maintainOffset=True)
            pm.connectAttr(anim + ".scale", bnd + ".scale")
            """ apply shapes """
            shp = tools.apply_shape(anim, "limbShaper_anim")
            if side == 'Lt':
                tools.rotate_shape(shp, (180, 0, 0))
        d[pre]['shapers'] = shaper_dict
        setup_shaper_nodes(d[pre])


def make_elbow_shapers(d):
    key = d['key']
    side = d['side']
    if key != 'arm':
        return
    """ gather info... """
    tgt = info[key][side]['lwr']['twistCtrlMid']
    bnd = info[key][side]['upr']['midBind']
    par = info['arm'][side]['shaper_group']
    """ make control hierarchy """
    grp_name = "elbowShaper_{0}_grp".format(side)
    grp = make_group(grp_name)
    a0 = make_group(grp_name.replace("_grp", "_a0"), grp)
    anim = make_group(grp_name.replace("_grp", "_anim"), a0)
    pm.parent(grp, bnd, relative=True)
    grp.setAttr("rotate", (90, 0, 0))
    pm.parent(grp, par)
    pm.parentConstraint(tgt, grp, maintainOffset=True)
    tools.match_to(bnd, anim)
    # pm.makeIdentity(bnd, apply=True, jointOrient=True, rotate=True)
    pm.makeIdentity(bnd, apply=True, rotate=True)
    pm.parentConstraint(anim, bnd, maintainOffset=True)
    pm.connectAttr(anim + ".scale", bnd + ".scale")
    shp = tools.apply_shape(anim, "limbShaper_anim")
    tools.scale_shape(shp, (1, 1, 0.75))
    if side == 'Lt':
        tools.rotate_shape(shp, (180, 0, 0))
    """ enter data into info dict """
    info[key][side]['upr']['shapers']['anims'].append(anim)
    info[key][side]['upr']['shapers']['a0'].append(a0)
    info[key][side]['upr']['shapers']['grps'].append(grp)


def make_mid_anims(d):
    key = d['key']
    side = d['side']
    for pre in ["upr", "lwr"]:
        grp_name = "%s%sRibbonMid_%s_a0" % (pre, key.title(), side)
        anim_name = tools.get_new_name(grp_name, "anim")
        grp = make_group(grp_name, d['ctrlGrp'])
        anim = make_group(anim_name, grp)
        """ add constraints """
        pm.parentConstraint(d[pre]['aims'][1], grp)
        pm.parentConstraint(anim, d[pre]['joints'][-1])
        """ apply shape """
        shp = tools.apply_shape(anim, "fourPointArrow_anim")
        tools.rotate_shape(shp, (0, 0, 90))
        d[pre]["midAnim"] = anim


def set_colors(key, side):
    map = {"arm": "elbow", "leg": "knee"}
    for pre in ["upr", "lwr"]:
        """ dull yellow (25) """
        x = "%s%sRibbonMid_%s_animShape" % (pre, key.title(), side)
        y = "%s%sRibbonMid_%s_jnt" % (pre, key.title(), side)
        tools.set_override_color(x, 25)
        tools.set_override_color(y, 25)
    """ yellow (17) """
    x = "%sRibbon_%s_animShape" % (map[key], side)
    y = "%s_%s_VJ_bind" % (map[key], side)
    tools.set_override_color(x, 17)
    tools.set_override_color(y, 17)
    """ light green (26) """
    """ forest green (23) """
    cols = {"lwr": 26, "upr": 23}
    for col in cols:
        li = ["%s%sTwist_%s_animShape" % (col, key.title(), side),
              "%s%sRibbonTop_%s_jnt" % (col, key.title(), side),
              "%s%sRibbonBtm_%s_jnt" % (col, key.title(), side)]
        for x in li:
            tools.set_override_color(x, cols[col])
    """ muted red (31) """
    """ magenta (31) and dark red (4) """
    cols = {"lwr": 31, "upr": 4}
    for col in cols:
        li = pm.ls("%s%sShaper0*_%s_animShape" % (col, key.title(), side))
        li += pm.ls("%s%sRibbon0*_%s_bind" % (col, key.title(), side))
        for x in li:
            tools.set_override_color(x, cols[col])
    """ pink (20) """
    li = ["%sRollReader_%s_jnt" % (key, side),
          "%sRollVector_%s_jnt" % (key, side)]
    for x in li:
        tools.set_override_color(x, 20)
    """ dirty orange (24) """
    elbow_shaper = "elbowShaper_%s_animShape" % side
    tools.set_override_color(elbow_shaper, 24)


def init_dict():
    for key in ['arm', 'leg']:
        for side in ['Lt', 'Rt']:
            d = info[key][side]
            d['key'] = key
            d['side'] = side
            d['ctrlGrp'] = make_group("%sRibbonCtrl_%s_grp" % (key, side), None)
            for pre in ["upr", "lwr"]:
                d[pre] = {}
                d[pre]['side'] = side
                d[pre]['key'] = key
                d[pre]['prefix'] = pre


def build_data(d):
    key = d['key']
    init_targets(d)
    make_hierarchy(d)
    make_aim_reader(d)
    make_roll_vector(d)
    make_roll_reader(d)
    if key == 'arm':
        make_end_twist_reader(d, "wrist")
    else:
        make_end_twist_reader(d, "foot")
    make_twist_anims(d)
    make_bind_joints(d)
    make_nurbs(d)
    make_skin_joints(d)
    make_follicles(d)
    make_shapers(d)
    make_elbow_shapers(d)
    make_mid_anims(d)
    make_skin_cluster(d)


def setup_ribbons():
    if not pm.objExists('wrist_Lt_bind'):
        """ ...then this is a test run on a bare skeleton. Insert the wrist joints. """
        tools.insert_joints(end_map)
        """ apply the IK routine. """
        setupIK.setup_ik()
        pm.select("*PV_*a0")
        pm.group(name="___PV_grp___")
    before = pm.ls()
    init_dict()
    add_knee_joints()
    add_elbow_joints()
    for key in ['arm', 'leg']:
        for side in ["Lt", "Rt"]:
            info[key][side]['targets'] = info[key]['targets']
            grps = info[key][side]
            build_data(grps)
            set_colors(key, side)
    after = pm.ls()
    msg = str(len(after) - len(before)) + " nodes added for ribbon rig."
    tools.debug_print(msg, dbg=debug)
    # import pprint
    # pprint.pprint(info)
