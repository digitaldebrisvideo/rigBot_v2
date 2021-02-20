import maya.cmds as mc
import maya.mel as mm

from rigBot import utils
from rigBot import spline
from rigBot import rivet

start_frame = 1.0
end_frame = mc.playbackOptions(q=1, max=1)

def set_start_frame(start=None, use_current=True):
    """Set start frame based on current time OR by playback start frame.

        Args:
            :start: (float, int) Start frame. Defaults to None
            :use_current: (bool) Use the current frame as the start frame for sim. Defaults to True"""

    global start_frame

    if type(start) in [float, int]:
        start_frame = float(start)

    elif use_current:
        start_frame = mc.currentTime(q=1)

    else:
        start_frame = mc.playbackOptions(q=1, min=1)

def set_end_frame(end=None, use_current=False):
    """Set end frame based on current time OR by playback end frame.

        Args:
            :end: (float, int) end frame. Defaults to None
            :use_current: (bool) Use the current frame as the end frame for sim. Defaults to False"""

    global end_frame

    if type(end) in [float, int]:
        end_frame = float(end)

    elif use_current:
        end_frame = mc.currentTime(q=1)

    else:
        end_frame = mc.playbackOptions(q=1, max=1)

def create_sim_curve_with_anim()
