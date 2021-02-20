"""
    AutoRigOptions

    v001.160712 --
        Added makeDistanceWarning:
            Create a visual indicator once a transform node goes beyond
            a specified distance from 0,0,0
        Added makeFaceGuides:
            Create 3 base curves to be able to help align a rigs head for
            match moving
    v002.160712 --
        Add overrideDisplaytype control to face guides
        Fix TooFar shape (F instead of P)
        Turn TooFar into Referrence overrideDisplayType
"""

#####################################################################
##  - Node system for calculating magnitude from origin created
##      because using a simple distance node would require managing
##      a transform that would needed to be kept at 0,0,0.  By using
##      the world matrix position as the magnitude, it will give the
##      simple distance from center without needing another transform
#####################################################################

__author__ = 'Bradley Mullennix'
__copyright__ = '2016 Encore Burbank'
__credits__ = 'Jennifer Hachigian, Peter Christensen, Bradley Mullennix'
__maintainer__ = 'Bradley Mullennix'
__version__ = 'v001.160712'
__email__ = 'bradley@randitech.com'


import maya.cmds as cmds



def makeDistanceWarning(subject='hips_Mid_bind', distance=100000, parent='root_Mid_anim'):
    """
    Create a "Too Far" warning sign if the subject is beyong "distance" from 0,0,0
    Defaults:
        subject = 'hips_Mid_bind' (Object to test)
        distance = 100000
        parent = 'root_Mid_anim' (Where to parent the warning curve)
    """
    #   plugin safety check by Jennifer Hachigian
    checklist = cmds.pluginInfo(query=True, listPlugins=True)
    if checklist is None or "matrixNodes" not in checklist:
        cmds.loadPlugin("matrixNodes")

    curSel = cmds.ls(sl=True)

    #    Double and factor distance
    distanceFactor = 1.0 / (distance * 2.0)

    #    Decompose the world matrix first
    deTransNode = cmds.shadingNode('decomposeMatrix', n='asTrans', au=True)

    #    Connect the node in questions's world Matrix to it
    cmds.connectAttr('{0}.worldMatrix[0]'.format(subject), '{0}.inputMatrix'.format(deTransNode),f=True)

    #    Square decomp's XYZ
    sqrNode = cmds.shadingNode('multiplyDivide', n='inSq', au=True)
    cmds.setAttr('{0}.operation'.format(sqrNode), 3)
    cmds.setAttr('{0}.input2X'.format(sqrNode), 2.0)
    cmds.setAttr('{0}.input2Y'.format(sqrNode), 2.0)
    cmds.setAttr('{0}.input2Z'.format(sqrNode), 2.0)
    cmds.connectAttr('{0}.outputTranslate'.format(deTransNode), '{0}.input1'.format(sqrNode),f=True)

    #    Add the squares
    addNode = cmds.shadingNode('plusMinusAverage', n='addMag', au=True)
    cmds.setAttr('{0}.operation'.format(addNode), 1)
    cmds.connectAttr('{0}.outputX'.format(sqrNode), '{0}.input1D[0]'.format(addNode),f=True)
    cmds.connectAttr('{0}.outputY'.format(sqrNode), '{0}.input1D[1]'.format(addNode),f=True)
    cmds.connectAttr('{0}.outputZ'.format(sqrNode), '{0}.input1D[2]'.format(addNode),f=True)

    #    Sqrt it to get magnitude
    outSqrtNode = cmds.shadingNode('multiplyDivide', n='outSqrt', au=True)
    cmds.setAttr('{0}.operation'.format(outSqrtNode), 3)
    cmds.setAttr('{0}.input2X'.format(outSqrtNode), .5)
    cmds.setAttr('{0}.input2Y'.format(outSqrtNode), .5)
    cmds.setAttr('{0}.input2Z'.format(outSqrtNode), .5)
    cmds.connectAttr('{0}.output1D'.format(addNode), '{0}.input1X'.format(outSqrtNode),f=True)

    #    Creat Switcher Value
    switcherNode = cmds.shadingNode('multiplyDivide', n='dvSwitch', au=True)
    cmds.setAttr('{0}.operation'.format(switcherNode), 1)
    cmds.setAttr('{0}.input2X'.format(switcherNode), distanceFactor)
    cmds.setAttr('{0}.input2Y'.format(switcherNode), distanceFactor)
    cmds.setAttr('{0}.input2Z'.format(switcherNode), distanceFactor)
    cmds.connectAttr('{0}.outputX'.format(outSqrtNode), '{0}.input1X'.format(switcherNode),f=True)

    #    Create sign
    tooFarCurve = cmds.curve(n='tooFar', d=1,
            p=[(48.82005, -61.945954, 85.794345),
            (48.82005, -61.945954, 10.39377),
            (108.701745, -61.945954, 10.39377),
            (108.701745, -61.945954, 85.794345),
            (-38.64259, -61.945954, 85.794345),
            (-38.64259, -61.945954, 10.39377),
            (18.879205, -61.945954, 10.39377),
            (18.879205, -61.945954, 85.794345),
            (-138.64259, -61.945954, 85.794345),
            (-88.64259, -61.945954, 85.794345),
            (-88.64259, -61.945954, 10.39377),
            (-104.021519, -61.945954, -2.73943),
            (-104.021519, -61.945954, -78.14001),
            (-104.021519, -61.945954, -40.43972),
            (-54.021519, -61.945954, -40.43972),
            (-104.021519, -61.945954, -40.43972),
            (-104.021519, -61.945954, -2.73943),
            (2.320326, -61.945954, -2.73943),
            (-47.679674, -61.945954, -78.14001),
            (2.320326, -61.945954, -2.73943),
            (52.320326, -61.945954, -78.14001),
            (52.320326, -61.945954, -2.73943),
            (106.952408, -61.945954, -11.535307),
            (81.081221, -61.945954, -40.43972),
            (52.320326, -61.945954, -40.43972),
            (81.081221, -61.945954, -40.43972),
            (115.148909, -61.945954, -78.14001)],
            k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
    tfc = cmds.listRelatives(tooFarCurve, type='nurbsCurve')[0]
    cmds.setAttr('{0}.overrideEnabled'.format(tfc), 1)
    cmds.setAttr('{0}.overrideColor'.format(tfc), 13)
    cmds.setAttr('{0}.overrideDisplayType'.format(tfc), 1)

    #    Connect switch to flip vis on
    cmds.connectAttr('{0}.outputX'.format(switcherNode), '{0}.visibility'.format(tooFarCurve),f=True)

    #    Parent
    tooFarCurve = cmds.parent(tooFarCurve, parent)[0]
    cmds.xform(tooFarCurve, t=(0,0,0))
    #    Zero curve identities
    cmds.makeIdentity(tooFarCurve, a=True, t=True, r=True, s=True, n=False, pn=True)
    cmds.makeIdentity(tooFarCurve, a=False, t=True, r=True)

    #    Reselect anything before operation
    if curSel:
        cmds.select(curSel,r=True)
    else:
        cmds.select(cl=True)


def makeFaceGuides(parent='head_Mid_anim', control='switch_anim'):
    """
    Add face guides, and apply a visibility control to a control handle.
    Defaults:
        Parent for guides = head_Mid_anim
        Control handle = switch_anim
    """

    curSel = cmds.ls(sl=True)

    #    Create guides
    eyeGuide = cmds.curve(n='eyeGuide', d=3,
            p=[(-7.677954, -12.471513, 172.140612),
            (-6.555799, -14.036644, 172.140974),
            (-5.700755, -15.212302, 172.14093),
            (-4.662465, -15.639163, 172.141028),
            (-3.412193, -16.355301, 172.140929),
            (-1.936382, -16.538407, 172.140929),
            (-1.086608, -16.499236, 172.140929),
            (-0.99614, -18.209752, 172.16824),
            (0, -19.157438, 172.574178),
            (0.99614, -18.209752, 172.16824),
            (1.086608, -16.499236, 172.140929),
            (1.936382, -16.538407, 172.140929),
            (3.412193, -16.355301, 172.140929),
            (4.662465, -15.639163, 172.141028),
            (5.700755, -15.212302, 172.14093),
            (6.555799, -14.036644, 172.140974),
            (7.677954, -12.471513, 172.140612)],
            k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 14])
    egc = cmds.listRelatives(eyeGuide, type='nurbsCurve')[0]
    cmds.setAttr('{0}.overrideEnabled'.format(egc), 1)
    cmds.setAttr('{0}.overrideColor'.format(egc), 17)

    mouthGuide = cmds.curve(n='mouthGuide', d=3,
            p=[(-6.475058, -8.492806, 165.302627),
            (-6.822636, -11.749121, 165.302627),
            (-5.601721, -14.587791, 165.302627),
            (-4.324053, -16.150434, 165.302627),
            (-2.711673, -17.277553, 165.068453),
            (-1.71231, -17.968569, 165.302627),
            (-0.933227, -18.29335, 165.302627),
            (0, -18.561578, 165.302627),
            (0.933227, -18.29335, 165.302627),
            (1.71231, -17.968569, 165.302627),
            (2.711673, -17.277553, 165.068453),
            (4.324053, -16.150434, 165.302627),
            (5.601721, -14.587791, 165.302627),
            (6.822636, -11.749121, 165.302627),
            (6.475058, -8.492806, 165.302627)],
            k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12])
    mgc = cmds.listRelatives(mouthGuide, type='nurbsCurve')[0]
    cmds.setAttr('{0}.overrideEnabled'.format(mgc), 1)
    cmds.setAttr('{0}.overrideColor'.format(mgc), 17)

    faceGuide = cmds.curve(n='faceGuide', d=3,
            p=[(0, -8.920179, 158.220701),
            (0, -12.305799, 158.741626),
            (0, -14.722916, 159.282551),
            (0, -17.172998, 160.0257),
            (0, -18.476422, 161.634689),
            (0, -17.890486, 163.689458),
            (0, -19.360906, 165.31043),
            (0, -17.933218, 167.560095),
            (0, -20.607793, 167.659541),
            (0, -20.645526, 169.285916),
            (0, -18.977394, 171.393593),
            (0, -18.758632, 173.420786),
            (0, -18.706245, 175.100274),
            (0, -18.228253, 177.625419),
            (0, -16.591782, 181.126782),
            (0, -14.504039, 183.356996),
            (0, -10.845881, 184.890529),
            (0, -6.512763, 185.666319)],
            k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15])
    fgc = cmds.listRelatives(faceGuide, type='nurbsCurve')[0]
    cmds.setAttr('{0}.overrideEnabled'.format(fgc), 1)
    cmds.setAttr('{0}.overrideColor'.format(fgc), 17)

    #    Group and cleanup
    cmds.select(cl=True)
    gGroup = cmds.group(n='fGuideGrp',em=True)
    gGroup = cmds.parent(gGroup, parent)[0]
    cmds.xform(gGroup, ro=(0,0,0), t=(0,0,0))
    cmds.parent([eyeGuide, mouthGuide, faceGuide], gGroup)
    cmds.select([eyeGuide, mouthGuide, faceGuide], r=True)

    #    Zero curve identities
    cmds.makeIdentity([eyeGuide, mouthGuide, faceGuide], a=True, t=True, r=True, s=True, n=False, pn=True)
    cmds.makeIdentity([eyeGuide, mouthGuide, faceGuide], a=False, t=True, r=True)

    #    Hook up visibility attributes
    cmds.addAttr(control, ln='faceGuideVis', at='enum', en='Off:On:')
    cmds.setAttr('{0}.faceGuideVis'.format(control), e=True, cb=True)
    cmds.connectAttr('{0}.faceGuideVis'.format(control), '{0}.visibility'.format(gGroup),f=True)
    
    cmds.addAttr(control, ln='faceGuideRef', at='enum', en='Normal:Template:Reference')
    cmds.setAttr('{0}.faceGuideRef'.format(control), e=True, cb=True)
    cmds.setAttr('{0}.faceGuideRef'.format(control), 2)
    cmds.connectAttr('{0}.faceGuideRef'.format(control), '{0}.overrideDisplayType'.format(egc),f=True)
    cmds.connectAttr('{0}.faceGuideRef'.format(control), '{0}.overrideDisplayType'.format(mgc),f=True)
    cmds.connectAttr('{0}.faceGuideRef'.format(control), '{0}.overrideDisplayType'.format(fgc),f=True)


    #    Reselect anything before operation
    if curSel:
        cmds.select(curSel,r=True)
    else:
        cmds.select(cl=True)



