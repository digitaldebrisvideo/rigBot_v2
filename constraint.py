import maya.OpenMaya as om
import maya.cmds as mc
import maya.mel as mm

import os
import re
import json

from rigBot import utils
from rigBot import env

def constraint_mtx(driver=None, driven=None, mo=True, t=True, o=True, s=True, no_connect=False, use_plugin=None):

    if not driver and not driven:
        driver = mc.ls(sl=1)[0]
        driven = mc.ls(sl=1)[1]

    if use_plugin is None:
        use_plugin = env.use_plugin()

    if use_plugin:
        return constraint_mtx_plugin(driver, driven, mo, t, o, s, no_connect)
    else:
        return constraint_mtx_vanilla(driver, driven, mo, t, o, s, no_connect)

def constraint_mtx_vanilla(driver, driven, mo=True, t=True, o=True, s=True, no_connect=False):


    mmtx = mc.createNode('multMatrix')
    dmtx = mc.createNode('decomposeMatrix', n=driven+'_mtxcon')

    # add some attrs
    mc.addAttr(dmtx, ln='driver', at='enum', k=0, en=driver)
    mc.setAttr(dmtx+'.driver', cb=1)

    # setuo offset
    if mo:
        offset = utils.get_offset_matrix(driver, driven)
        mc.setAttr(mmtx+'.matrixIn[0]', offset, type='matrix')

    # build constraint
    mc.connectAttr(driver+'.worldMatrix', mmtx+'.matrixIn[1]')
    mc.connectAttr(driven+'.parentInverseMatrix', mmtx+'.matrixIn[2]')
    mc.connectAttr(mmtx+'.matrixSum', dmtx+'.inputMatrix')
    mc.setAttr(mmtx+'.ihi', 0)

    #connect to driven node
    if not no_connect:
        if t:
            mc.connectAttr(dmtx+'.outputTranslate', driven+'.t', f=1)
        if o:
            mc.connectAttr(dmtx+'.outputRotate', driven+'.r', f=1)
        if s:
            mc.connectAttr(dmtx+'.outputScale', driven+'.s', f=1)
            mc.connectAttr(dmtx+'.outputShear', driven+'.shear', f=1)

    return dmtx

def constraint_mtx_plugin(driver, driven, mo=True, t=True, o=True, s=True, no_connect=False):

    # get offset
    con = mc.createNode('cmConstraint', n=driven+'_mtxcon')
    mc.connectAttr(driver+'.worldMatrix', con+'.targetMatrix')
    mc.connectAttr(driven+'.parentInverseMatrix', con+'.parentInverseMatrix')

    mc.addAttr(con, ln='driver', at='enum', k=0, en=driver)
    mc.setAttr(con+'.driver', cb=1)

    if mo:
        offset = utils.get_offset_matrix(driver, driven)
        mc.setAttr(con+'.offsetMatrix', offset, type='matrix')

    #connect to driven node
    if not no_connect:
        if t:
            mc.connectAttr(con+'.outputTranslate', driven+'.t', f=1)
        if o:
            mc.connectAttr(con+'.outputRotate', driven+'.r', f=1)
        if s:
            mc.connectAttr(con+'.outputScale', driven+'.s', f=1)
            mc.connectAttr(con+'.outputShear', driven+'.shear', f=1)

    return con


def freeze_joint_orient(node):
    if mc.nodeType(node) == 'joint':
        jo = mc.getAttr(node+'.jo')[0]
        mc.setAttr(node+'.r', jo[0], jo[1], jo[2])
        mc.setAttr(node+'.jo', 0,0,0)

        return True
