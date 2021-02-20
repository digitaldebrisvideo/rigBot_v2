import maya.cmds as mc
import maya.mel as mm

from maya import OpenMaya as om
from math import sin, cos, sqrt, atan2, radians
import csv

from rigBot import utils, env

'''
# This is how the data is read

'Time':         row[0],
'Lap':          row[1],
'GPS_Update':   row[2],
'GPS_Delay':    row[3],
'Accuracy (m)': row[4],
'Latitude':     row[5],
'Longitude':    row[6],
'Altitude (m)': row[7],
'Speed (MPH)':  row[8],
'Heading':      row[9],
'X':            row[10],
'Y':            row[11],
'Z':            row[12]

'''

def load(start_frame=1001, mult=4.0):

    # scene setup
    sel = mc.ls(sl=1)
    if not sel:
        mc.warning('Select a node on the car!')
        return

    namespace= utils.get_namespace(sel[0])

    if not mc.objExists(namespace+'C_chassisWorld_CTL'):
        mc.warning('Cannot find: '+namespace+'C_chassisWorld_CTL')
        return

    data = read_track_data()
    crv = plot_track(data, 0)

    connect_chassis(namespace, crv)

    mc.select(namespace+'C_chassisWorld_CTL', crv)
    animate_speed(data, namespace, start_frame)

    mc.select(namespace+'C_chassisWorld_CTL')
    animate_accelerometer(data, node=namespace+'C_chassisRoll_CTL', mult=mult, start_frame=start_frame)

    mc.select(namespace+'C_chassisWorld_CTL')



def filter_gps_data(raw_data):

    data = []
    for row in raw_data:
        if row[3]:
            data.append(row)
    return data

def filter_laps(raw_data, laps=[]):

    if type(laps) is not list:
        laps = [laps]

    if not laps:
        return raw_data

    data = []
    for row in raw_data:
        if int(row[1]) in laps:
            data.append(row)

    return data

def read_track_data(file_path='', laps=None):

    if not file_path:
        result = mc.fileDialog2(fm=1, cap='Load Track Data', okc='Load', ff='CSV Files (*.csv)')
        if result:
            file_path = result[0]

        else:
            return []

    # Read in raw track data
    raw_data = []
    with open(file_path) as f:
        readCSV = csv.reader(f, delimiter=',')
        for row in readCSV:
            if len(row) >= 13:
                try:
                    r_data = []
                    for r in row:
                        if r:
                            r_data.append(float(r))
                        else:
                            r_data.append(None)
                    raw_data.append(r_data)

                except:
                    pass

        return raw_data

def plot_track(data, close_track=False, count=5):

    data = filter_gps_data(data)

    # Draw the curve
    points = []
    for row in data:
        #long, alt, lat
        if row[5] and row[6] and row[7]:
            points.append([row[6], row[7], row[5]])

    if close_track:
        points.append([data[0][6], data[0][7], data[0][5]])

    lores_pts = []
    for i in range(0, len(points), count):
        lores_pts.append(points[i])

    # Create curve
    crv = mc.curve(d=2, p=lores_pts)
    crv = mc.rename(crv, 'Track_01_CRV')
    raw_crv = mc.curve(d=2, p=points)
    raw_crv = mc.rename(raw_crv, 'Track_01_CRV_RAW')

    mc.parent(raw_crv, crv)

    # Repo and zero the curve
    l = utils.snap_locator(crv)
    mc.parent(crv, l)
    mc.xform(l, ws=1, t=[0,0,0])

    mc.parent(crv, w=1)
    mc.delete(l)

    mc.makeIdentity(crv, apply=1, t=1, r=1, s=1, n=0, pn=1)
    mc.xform(crv, piv=(0,0,0))

    # now scale it to real world values
    mc.xform(crv, r=1, ro=[0, 180, 0], s=[-1009041, 7.452, 1009041])
    mc.setAttr(crv+'.ty', -mc.exactWorldBoundingBox(crv)[1])

    mc.makeIdentity(crv, apply=1, t=1, r=1, s=1, n=0, pn=1)
    mc.xform(crv, piv=(0,0,0))

    # add info attrs
    deci = round(mc.arclen(crv), 2)
    miles = round(deci / 16093.44, 2)
    km = round(deci / 10000, 2)

    a_deci = round(mc.exactWorldBoundingBox(crv)[-2], 2)
    a_miles = round(a_deci / 16093.44, 2)
    a_km = round(a_deci / 10000, 2)

    mc.addAttr(crv, ln='trackLength', at='enum', en=' ', k=1)
    mc.addAttr(crv, ln='decimeters', nn='decimeters', at='double', k=1, dv=deci)
    mc.addAttr(crv, ln='kilometers', nn='kilometers', at='double', k=1, dv=km)
    mc.addAttr(crv, ln='miles', nn='miles', at='double', k=1, dv=miles)

    mc.addAttr(crv, ln='trackAltitude', at='enum', en=' ', k=1)
    mc.addAttr(crv, ln='decimeterAlt', nn='decimeters', at='double', k=1, dv=a_deci)
    mc.addAttr(crv, ln='kilometerAlt', nn='kilometers', at='double', k=1, dv=a_km)
    mc.addAttr(crv, ln='mileAlt', nn='miles', at='double', k=1, dv=a_miles)

    attrs = ['decimeters','trackLength', 'trackAltitude' ,
             'kilometers', 'miles', 'decimeterAlt',
             'kilometerAlt', 'mileAlt']

    for a in attrs:
        mc.setAttr(crv+'.'+a, l=1)

    '''
    # need a lo reas curve becasue maya cant handle it
    raw_crv = mc.rename(crv, crv+'_RAW')
    crv = mc.duplicate(raw_crv, n=crv)[0]
    s = mc.getAttr(raw_crv+'.spans') / 5
    mm.eval('rebuildCurve -ch 0 -rpo 1 -rt 0 -end 1 -kr 0 -kcp 0 -kep 1 -kt 0 -s '+str(s)+' -d 2 -tol 0.01 '+crv)

    mc.parent(raw_crv, crv)
    mc.hide(raw_crv)
    '''

    mc.hide(raw_crv)

    # set clip planes
    cameras = mc.ls(type='camera')
    for c in cameras:
        mc.setAttr(c+'.farClipPlane', 10000000)
        mc.setAttr(c+'.nearClipPlane', 1)

    return crv

def connect_chassis(namespace=None, curve=None):

    # get namespace and curve then do a ton of checls
    sel = mc.ls(sl=1)
    if namespace is None and curve is None:
        if not len(sel) == 2:
            mc.warning('Select any node on the car rig THEN select a curve.')
            return

        namespace = utils.get_namespace(sel[0])
        curve = sel[1]

    elif curve and namespace is None:
        if not len(sel) >= 1:
            mc.warning('Select any node on the car rig.')
            return

        namespace = utils.get_namespace(sel[0])

    elif namespace and curve is None:
        if not len(sel) >= 1:
            mc.warning('Select a curve.')
            return

        curve = sel[0]

    if not curve:
        mc.warning('Curve not selected or specified.')
        return

    if not utils.get_shapes(curve) or not mc.nodeType(utils.get_shapes(curve)) == 'nurbsCurve':
        mc.warning('Specified curve is not a NURBS curve.')
        return

    ik = mc.ls(namespace+'*C_path_IK')
    set_range = mc.ls(namespace+'*C_path_range')

    if not ik :
        mc.warning('Couild not find chassis nodes in this rig! Cannot continue!')
        return

    # now that i have all crap i need.. connect it up
    mc.setAttr(ik[0]+'.ikBlend', 0)
    spans = mc.getAttr(curve+'.maxValue')

    try:
        mc.connectAttr(curve+'.worldSpace', ik[0]+'.inCurve', f=1)
        mc.connectAttr(curve+'.worldSpace', namespace+'trackDistanceNode.inputCurve', f=1)
    except:
        pass

    mc.setAttr(ik[0]+'.ikBlend', 1)
    mc.setAttr(namespace+'C_chassisWorld_CTL.transSpace' ,0)
    mc.setAttr(namespace+'C_steering_CTL.autoSteering', 1)
    mc.setAttr(namespace+'C_steering_CTL.autoWheel', 1)
    mc.select(namespace+'C_chassisWorld_CTL')

def disconnect_chassis(namespace=None):

    # get namespace and curve then do a ton of checls
    sel = mc.ls(sl=1)
    if namespace is None:
        if not len(sel) >= 1:
            mc.warning('Select any node on the car rig.')
            return

        namespace = utils.get_namespace(sel[0])

    ik = mc.ls(namespace+'*C_path_IK')

    if not ik or not set_range:
        mc.warning('Couild not find chassis nodes in this rig! Cannot continue!')
        return

    # now that i have all crap i need.. connect it up
    mc.setAttr(ik[0]+'.ikBlend', 0)
    utils.break_connections(ik[0], 'inCurve')
    mc.setAttr(set_range[0]+'.maxX', 100)
    mc.setAttr(namespace+'C_chassisWorld_CTL.space', 1)


def animate_accelerometer(data, node='C_chassisRoll_CTL', mult=4, start_frame=1):

    if not node:
        mc.select(cl=1)
        node = utils.snap_locator(name='accelerometer_LOC')

    fps = mm.eval('currentTimeUnitToFPS')
    mc.cutKey(node+'.ty')
    mc.cutKey(node+'.rx')
    mc.cutKey(node+'.rz')

    for i in range(len(data)):
        data_sample = data[i]

        time = data_sample[0]
        frame = (time * fps) - (data[0][0] * fps) + start_frame

        # x = fw back accel / deccel
        # y == roll
        # z = up and down noise

        x = float(data_sample[12])
        y = float(data_sample[13])
        z = float(data_sample[14])

        mc.setKeyframe(node+'.rx', t=frame, v=x*mult)
        mc.setKeyframe(node+'.rz', t=frame, v=y*mult)
        mc.setKeyframe(node+'.ty', t=frame, v=z*(mult*0.5))

    crvs = mc.listConnections(node, scn=1, type='animCurve', s=1, d=0)
    mc.selectKey(crvs)
    mc.keyTangent(crvs, itt='spline', ott='spline')



def animate_speed(data, namespace=None, start_frame=1):

    def get_length_at_cv(cv):

        param_len = 0.0

        # get initial values for node
        sel = om.MSelectionList()
        sel.add(utils.get_shapes(crv)[0])
        crvObj = om.MDagPath()
        sel.getDagPath(0, crvObj)
        crvFn = om.MFnNurbsCurve(crvObj)

        # get non unifrom param value
        l = utils.snap_locator(cv)
        p = mc.xform(l, q=1, ws=1, t=1)
        p = om.MPoint(p[0], p[1], p[2])
        mc.delete(l)

        u = om.MScriptUtil()
        u.createFromDouble(0)
        dbl = u.asDoublePtr()

        crvFn.closestPoint(p, dbl, om.MSpace.kWorld)
        nu_param = round(u.getDoubleArrayItem(dbl, 0), 3)

        if nu_param == 0:
            param_len = 0.0

        elif nu_param == round(mc.arclen(crv, ch=0), 3):
            param_len = float(mc.getAttr(crv+'.spans'))
        else:
            tmp = mm.eval('detachCurve -ch 1 -cos on -rpo 0 {0}.u[{1}];'.format(crv, nu_param))
            param_len = mc.arclen(tmp[0])
            mc.delete(tmp)

        return param_len

    # get namespace and curve then do a ton of checls
    sel = mc.ls(sl=1)
    if namespace is None:
        if not sel:
            mc.warning('Select any node on the car rig.')
            return

        namespace = utils.get_namespace(sel[0])

    data = filter_gps_data(data)

    ik = mc.ls(namespace+'*C_path_IK')
    sr = mc.listConnections(ik[0]+'.offset', s=1)[0]
    crv = mc.listConnections(ik[0]+'.inCurve')[0]
    raw_crv = mc.ls(crv+'_RAW', crv)[0]
    cvs = mc.ls(raw_crv+'.cv[*]', fl=1)

    if not len(cvs) == len(data):
        mc.warning('This will not work, number of curve cvs is different than number of data points')
        return

    ctrl = namespace+'C_chassisWorld_CTL'
    fps = mm.eval('currentTimeUnitToFPS')

    mc.currentTime(start_frame)
    mc.cutKey(ctrl+'.pathTravel')
    mc.setAttr(ctrl+'.pathTravel', 0)

    sr = mc.listConnections(ik[0]+'.offset', s=1)[0]
    mc.setAttr(ctrl+'.pathLength', mc.arclen(raw_crv, ch=0))
    mc.setAttr(ctrl+'.pathSpans', mc.getAttr(crv+'.spans'))

    '''
    for i in range(len(data)):
        data_sample = data[i]

        time = data_sample[0]
        frame = (time * fps) - (data[0][0] * fps) + start_frame
        distance = get_length_at_cv(cvs[i])
        mc.setKeyframe(ctrl+'.pathTravel', t=frame, v=distance)
    '''

    ##############################################
    # Other test
    mc.cutKey(ctrl+'.pathTravel')
    mc.setKeyframe(ctrl+'.pathTravel', t=start_frame, v=0)

    data_sample = data[-1]
    time = data_sample[0]
    frame = (time * fps) - (data[0][0] * fps) + start_frame
    distance = get_length_at_cv(cvs[-1])
    mc.setKeyframe(ctrl+'.pathTravel', t=frame, v=distance)
    mc.currentTime(start_frame)

    crvs = mc.listConnections(ctrl+'.pathTravel', scn=1, type='animCurve', s=1, d=0)
    mc.selectKey(crvs)
    mc.keyTangent(crvs, itt='linear', ott='linear')

    mm.eval('setPlaybackRangeToMinMax')














