import commsanimation.camera.rig as impPath;
import maya.cmds as mc

def create():

    # Create a dummy camera
    sel = mc.ls(sl=1)[0]
    dummy = mc.duplicate(sel, n=sel.split(':')[-1].replace('_CAM', '_ANIM_CAM'))[0]
    junk = [n for n in mc.listRelatives(dummy, c=1, f=1) if mc.nodeType(n) != 'camera']
    mc.delete(junk)

    # Create rig using dummy camera
    mc.select(dummy)
    impPath.makeCameraRig();

    # rename new rig according to real camera name
    prefix = dummy.replace('_CAM','')
    mc.select(prefix+'_global_0001_CTL', hi=1)
    nodes = mc.ls(sl=1)
    for n in nodes:
        if mc.objExists(n):
            mc.rename(n, n.replace('_ANIM_','_'))

    prefix = prefix.replace('_ANIM', '')

    # connect real cam shape to everything
    src = mc.listRelatives(dummy, type='camera')[0]
    dst = mc.listRelatives(sel, type='camera')[0]

    incnns = mc.listConnections(src, s=1, d=0, c=1, p=1)
    for i in range(0, len(incnns), 2):
        d = incnns[i].replace(src, dst)
        s = incnns[i+1]

        mc.connectAttr(s, d, f=1)

    # delete dummy cam shape
    mc.delete(src)

    # create aprent constrasint to real cam xform node
    prc = list(set(mc.listConnections(dummy, type='parentConstraint')))
    driver = mc.parentConstraint(prc[0], q=1, tl=1)[0]
    mc.delete(prc)
    prc = mc.parentConstraint(driver, sel, mo=1)
    mc.parent(prc, prefix+'_out_LOC')

    # now take the dummy trtansform attr and make it the global ctrl transfor node to maintain all anim attr
    shape = mc.listRelatives(prefix+'_global_0001_CTL', s=1)
    ch = [s for s in mc.listRelatives(prefix+'_global_0001_CTL') if s not in shape]
    mc.parent(shape, dummy, r=1, s=1)
    mc.parent(ch, dummy)
    mc.delete(prefix+'_global_0001_CTL')
    mc.rename(dummy, prefix+'_global_0001_CTL')

    # lock and hide attrs that are driven
    attrs = ['focalLength',
             '_____',
             'renderHorizontalFilmAperture',
             'renderVerticalFilmAperture',
             'renderHorizontalResolution',
             'renderVerticalResolution',
             '______',
             'sourceApertureRatio',
             'sourceResolutionRatio',
             'renderApertureRatio',
             'renderResolutionRatio']
    for a in attrs:
        mc.setAttr(prefix+'_global_0001_CTL.'+a, l=1, k=0)

    # rename all expressios to remove the dummy name
    exps = mc.ls(prefix+'_ANIM*',type='expression')
    for e in exps:
        mc.rename(e, e.replace('_ANIM_', '_'))

    # select global ctrl
    print '\nCREATED CAMERA RIG!'
    print '  camera: '+sel

    mc.select(prefix+'_global_0001_CTL')

