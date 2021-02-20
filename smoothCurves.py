import maya.cmds as mc
import maya.mel as mm

def smooth_curves(smooth_value=0.8):
    # get selected keys
    c_names = mc.keyframe(q=1, sl=1, n=1) or []
    c_indexes = []

    for name in c_names:

        indexes = [int(i) for i in mc.keyframe(c_names[0], q=1, sl=1, iv=1) or []]
        indexes.insert(0, indexes[0]-1)
        indexes.append(indexes[-1]+1)

        c_indexes.append(indexes)

    #now for each key i need to find the previous key pivot, and the next key pivot, then average the two.
    #    This will give me my pivot to scale the current key up or down
    for i, name in enumerate(c_names):

        indexes = c_indexes[i]
        values = mc.keyframe(name, q=1, index=(indexes[0], indexes[-1]), vc=1)
        times = mc.keyframe(name, q=1, index=(indexes[0], indexes[-1]), tc=1)

        for i in range(1, len(values[:-1])):

            idx = indexes[i]
            time = times[i]
            c_value = values[i]
            p_value = values[i-1]
            n_value = values[i+1]

            vp = (n_value+p_value) / 2

            mc.selectKey(name, time=(time, time) )
            mc.scaleKey(iub=False, animation='keys', ts=1, fs=1, fp=time, tp=time, vp=vp, vs=smooth_value)

    mc.selectKey(cl=1)
    for i, name in enumerate(c_names):
        mc.selectKey(name, index=(c_indexes[i][1], c_indexes[i][-2]), add=1)


class SmoothCurves(object):
    def __init__(self):
        win = 'smootherCurveUI'
        if mc.window(win, q=1, ex=1):
            mc.deleteUI(win)

        window = mc.window(win, title='Smooth Anim Curves')
        col = mc.columnLayout(adj=0, rs=4)

        self.slider = mc.floatSliderGrp( label='Smooth / Sharpen Amount ', cw3=[150, 60, 100],  field=True, minValue=0, maxValue=1.0, fieldMinValue=0, fieldMaxValue=1.0, value=0.2)

        mc.showWindow( window )

        mc.rowLayout(nc=2)
        mc.button( label='Smooth' ,w=155, c=self.smooth)
        mc.button( label='Sharpen' ,w=155, c=self.sharp)
        mc.setParent(col)

        mc.separator(w=310)
        self.slider2 = mc.intSliderGrp( label='<-- Smooth | Sharpen --> ',cc=self.reset, dc=self.interact, cw2=[130, 180],  field=0, minValue=-20, maxValue=20, value=0)
        #mc.button( label='Reset Slider' ,w=312)

        mc.separator(st='none', h=4)
        mc.window(window, e=1, w=300, s=0)

    def interact(self, arg):
        v = mc.intSliderGrp(self.slider2, q=1, v=1)

        if v < 0:
            smooth_curves(0.9)
        else:
            smooth_curves(1.1)

    def reset(self, arg):
        self.slider2 = mc.intSliderGrp(self.slider2, e=1, v=0)

    def smooth(self, arg):
        v = 1.0-mc.floatSliderGrp(self.slider ,q=1, v=1)
        smooth_curves(v)

    def sharp(self, arg):
        v = mc.floatSliderGrp(self.slider ,q=1, v=1)+1.0
        smooth_curves(v)

def run():
    SmoothCurves()

