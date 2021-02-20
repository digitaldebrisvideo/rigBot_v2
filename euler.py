import maya.cmds as mc

def minimize_range(nodes=[], value_range=180):

    if not nodes:
        nodes = mc.ls(sl=1)

    nodes = mc.ls(nodes)

    for node in nodes:

        rotX = mc.keyframe(node + '.rx', vc=1, q=1)
        rotY = mc.keyframe(node + '.ry', vc=1, q=1)
        rotZ = mc.keyframe(node + '.rz', vc=1, q=1)

        for k in range(len(rotX)):
            while rotX[k] > value_range:
                rotX[k] = rotX[k]-360

            while rotX[k] < -value_range:
                rotX[k] = rotX[k]+360

            mc.keyframe((node+'.rx'), e=1, index=(k,k), valueChange=rotX[k])

        for k in range(len(rotY)):
            while rotY[k] > value_range:
                rotY[k] = rotY[k]-360

            while rotY[k] < -value_range:
                rotY[k] = rotY[k]+360

            mc.keyframe((node+'.ry'), e=1, index=(k,k), valueChange=rotY[k])

        for k in range(len(rotZ)):
            while rotZ[k] > value_range:
                rotZ[k] = rotZ[k]-360

            while rotZ[k] < -value_range:
                rotZ[k] = rotZ[k]+360

            mc.keyframe((node+'.rz'), e=1, index=(k,k), valueChange=rotZ[k])

def double_euler(nodes=[], fwd=True, back=True, merge_frame='current'):

    if not nodes:
        nodes = mc.ls(sl=1)

    nodes = mc.ls(nodes)

    for node in nodes:

        tmp = mc.duplicate(node, po=1)[0]

        mc.copyKey(node)
        mc.pasteKey(tmp)

        tmp_crvs = mc.keyframe(tmp+'.r',n=1, q=1)
        mc.selectKey(tmp_crvs)
        mc.scaleKey(tmp_crvs, ts=-1)
        mc.filterCurve(tmp_crvs)
        mc.scaleKey(tmp_crvs, ts=-1)

        crvs = mc.keyframe(node+'.r',n=1, q=1)
        mc.filterCurve(crvs)

        num_keys = int(mc.keyframe(node + ".rotateX", q=1, keyframeCount=1))

        rotX = mc.keyframe(node + ".rotateX", vc=1, q=1)
        rotY = mc.keyframe(node + ".rotateY", vc=1, q=1)
        rotZ = mc.keyframe(node + ".rotateZ", vc=1, q=1)

        rv_rotX = mc.keyframe(tmp + ".rotateX", vc=1, q=1)
        rv_rotY = mc.keyframe(tmp + ".rotateY", vc=1, q=1)
        rv_rotZ = mc.keyframe(tmp + ".rotateZ", vc=1, q=1)

        if type(merge_frame) is int:
            frame = merge_frame

        elif merge_frame.lower() == 'half':
            frame = num_keys/2

        else:
            times = mc.keyframe(node + ".rotateX", tc=1, q=1)
            frame = int(mc.currentTime(q=1))
            frame = times.index(min(times, key=lambda x:abs(x-frame)))

        if fwd and back:
            new_rx = rotX[:frame]+ rv_rotX[frame:]
            new_ry = rotY[:frame]+ rv_rotY[frame:]
            new_rz = rotZ[:frame]+ rv_rotZ[frame:]

        elif fwd:
            new_rx = rotX
            new_ry = rotY
            new_rz = rotZ

        elif back:
            new_rx = rv_rotX
            new_ry = rv_rotY
            new_rz = rv_rotZ

        for k in range(0, num_keys):
            mc.keyframe((node + ".rotateX"), e=1, index=(k,k), valueChange=new_rx[k])
            mc.keyframe((node + ".rotateY"), e=1, index=(k,k), valueChange=new_ry[k])
            mc.keyframe((node + ".rotateZ"), e=1, index=(k,k), valueChange=new_rz[k])

        mc.delete(tmp)

    mc.select(nodes)


def modify_keys(x=1, y=1, z=1):

    node = mc.ls(sl=1)[0]

    # nudge euler values
    sel = mc.keyframe(q=1, sl=1) or []

    time = None
    if len(sel) == 1:
        time = [sel[0]]*2

    elif len(sel) > 1:
        time = [sel[0], sel[-1]]

    if time:
        rotX = mc.keyframe(node + ".rotateX", vc=1, q=1, t=(time[0], time[-1]))
        rotY = mc.keyframe(node + ".rotateY", vc=1, q=1, t=(time[0], time[-1]))
        rotZ = mc.keyframe(node + ".rotateZ", vc=1, q=1, t=(time[0], time[-1]))

    else:
        rotX = mc.keyframe(node + ".rotateX", vc=1, q=1)
        rotY = mc.keyframe(node + ".rotateY", vc=1, q=1)
        rotZ = mc.keyframe(node + ".rotateZ", vc=1, q=1)

    for k in range(len(rotX)):
        rotX[k] += 180*x
        rotY[k] += 180*y
        rotZ[k] += 180*z

        rotY[k] *= -1

    if time:
        time_rotX = mc.keyframe(node + ".rotateX", tc=1, q=1, t=(time[0], time[-1]))
        time_rotY = mc.keyframe(node + ".rotateY", tc=1, q=1, t=(time[0], time[-1]))
        time_rotZ = mc.keyframe(node + ".rotateZ", tc=1, q=1, t=(time[0], time[-1]))

        for k, t in enumerate(time_rotX):
            mc.keyframe((node + ".rotateX"), e=1, time=(t, t), valueChange=rotX[k])
            mc.keyframe((node + ".rotateY"), e=1, time=(t, t), valueChange=rotY[k])
            mc.keyframe((node + ".rotateZ"), e=1, time=(t, t), valueChange=rotZ[k])

    else:
        for k in range(len(rotX)):
            mc.keyframe((node + ".rotateX"), e=1, index=(k,k), valueChange=rotX[k])
            mc.keyframe((node + ".rotateY"), e=1, index=(k,k), valueChange=rotY[k])
            mc.keyframe((node + ".rotateZ"), e=1, index=(k,k), valueChange=rotZ[k])

ii = 0
def step_euler(back=False, reset=False):

    global ii

    if reset:
         ii = 0

    if back:
         ii -= 2

    if ii == 0:
        modify_keys( 1,  1,  1)

    elif ii == 1:
        modify_keys(-1,  1,  1)

    elif ii == 2:
        modify_keys( 1, -1,  1)

    elif ii == 3:
        modify_keys(-1, -1,  1)

    elif ii == 4:
        modify_keys( 1, -1, -1)

    elif ii == 5:
        modify_keys(-1, -1, -1)

    elif ii == 6:
        modify_keys(-1,  1, -1)

    elif ii == 7:
        modify_keys( 1,  1, -1)

    else:
        modify_keys( 1,  1,  1)
        ii = 0

    ii += 1

'''
# my attempt at a smark nudge
sel = mc.keyframe(q=1, sl=1) or []

time = None
if len(sel) == 1:
    time = [sel[0]]*2

elif len(sel) > 1:
    time = [sel[0], sel[-1]]

# get first and last frame values
rotX = mc.keyframe(node + ".rotateX", vc=1, q=1, t=(time[0], time[-1]))
rotY = mc.keyframe(node + ".rotateY", vc=1, q=1, t=(time[0], time[-1]))
rotZ = mc.keyframe(node + ".rotateZ", vc=1, q=1, t=(time[0], time[-1]))

time_rotX = mc.keyframe(node + ".rotateX", tc=1, q=1, t=(time[0], time[-1]))
time_rotY = mc.keyframe(node + ".rotateY", tc=1, q=1, t=(time[0], time[-1]))
time_rotZ = mc.keyframe(node + ".rotateZ", tc=1, q=1, t=(time[0], time[-1]))

for k in range(1, len(rotX)-1):

    xdiff = rotX[k] - rotX[k-1]
    zdiff = rotZ[k] - rotZ[k-1]

    if abs(xdiff) > 90 or (zdiff) > 90:
        if rotX[-1] > rotX[k]:
            x = 1
        else:
            x = -1

        if rotY[-1] > rotY[k]:
            y = 1
        else:
            y = -1

        if rotZ[-1] > rotZ[k]:
            z = 1
        else:
            z = -1

        rotX[k] += 180*x
        rotY[k] += 180*y
        rotZ[k] += 180*z
        rotY[k] *= -1

        t = time_rotX[k]
        mc.keyframe((node + ".rotateX"), e=1, time=(t, t), valueChange=rotX[k])
        mc.keyframe((node + ".rotateY"), e=1, time=(t, t), valueChange=rotY[k])
        mc.keyframe((node + ".rotateZ"), e=1, time=(t, t), valueChange=rotZ[k])
'''
