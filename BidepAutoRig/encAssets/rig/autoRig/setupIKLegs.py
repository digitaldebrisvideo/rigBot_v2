import pymel.core as pm
from maya import OpenMaya
import maya.cmds as cmds
import tools
import makeBox

reload(tools)
reload(makeBox)

__author__ = 'jhachigian'

debug = True
upScene= cmds.upAxis(q=1, ax=1)
rigChildren = ["geometry_grp", "setup_grp", "controls_grp"]
setChildren = ["skeleton_grp", "tech_grp"]
ctlChildren = ["display_grp"]
upScene= cmds.upAxis(q=1, ax=1)
limbs = ["thigh_Lt_jnt", "thigh_Rt_jnt"]


footIKChains = {'heel_Lt_plc': {"foot_Lt_ik": "toe_Lt_ik", "toe_Lt_ik": "toeEnd_Lt_ik"},
                'heel_Rt_plc': {"foot_Rt_ik": "toe_Rt_ik", "toe_Rt_ik": "toeEnd_Rt_ik"}}


# Each tuple takes the form of (<name>, <parentObjects>, <placement>)
feet = {'heel_Lt_plc': [('heel_Lt_a0', 'legIkGimbal_Lt_anim', 'heel_Lt_plc'),
                        ('heel_Lt_anim', 'heel_Lt_a0', 'heel_Lt_plc'),
                        ('heelRoll_Lt_loc', 'heel_Lt_anim', 'heel_Lt_plc'),
                        ('footBall_Lt_loc', 'heelRoll_Lt_loc', 'toe_Lt_bind'),
                        ('tiltOut_Lt_loc', 'footBall_Lt_loc', 'tiltOut_Lt_plc'),
                        ('tiltIn_Lt_loc', 'tiltOut_Lt_loc', 'tiltIn_Lt_plc'),
                        ('toeTip_Lt_a0', 'tiltIn_Lt_loc', 'toeTip_Lt_plc'),
                        ('toeTip_Lt_anim', 'toeTip_Lt_a0', 'toeTip_Lt_plc'),
                        ('toeTipRoll_Lt_loc', 'toeTip_Lt_anim', 'toeTip_Lt_plc'),
                        ('footRoll_Lt_loc', 'toeTipRoll_Lt_loc', 'toe_Lt_bind'),
                        ('foot_Lt_loc', 'footRoll_Lt_loc', 'toe_Lt_bind'),
                        ('toe_Lt_loc', 'toeTipRoll_Lt_loc', 'toe_Lt_bind')],
        'heel_Rt_plc': [('heel_Rt_a0', 'legIkGimbal_Rt_anim', 'heel_Rt_plc'),
                        ('heel_Rt_anim', 'heel_Rt_a0', 'heel_Rt_plc'),
                        ('heelRoll_Rt_loc', 'heel_Rt_anim', 'heel_Rt_plc'),
                        ('footBall_Rt_loc', 'heelRoll_Rt_loc', 'toe_Rt_bind'),
                        ('tiltOut_Rt_loc', 'footBall_Rt_loc', 'tiltOut_Rt_plc'),
                        ('tiltIn_Rt_loc', 'tiltOut_Rt_loc', 'tiltIn_Rt_plc'),
                        ('toeTip_Rt_a0', 'tiltIn_Rt_loc', 'toeTip_Rt_plc'),
                        ('toeTip_Rt_anim', 'toeTip_Rt_a0', 'toeTip_Rt_plc'),
                        ('toeTipRoll_Rt_loc', 'toeTip_Rt_anim', 'toeTip_Rt_plc'),
                        ('footRoll_Rt_loc', 'toeTipRoll_Rt_loc', 'toe_Rt_bind'),
                        ('foot_Rt_loc', 'footRoll_Rt_loc', 'toe_Rt_bind'),
                        ('toe_Rt_loc', 'toeTipRoll_Rt_loc', 'toe_Rt_bind')]}

feet_match_orientation = ['heel_Rt_a0', 'heel_Lt_a0', 'toeTip_Lt_a0', 'toeTip_Rt_a0']



if upScene == 'z':
    #cmds.warning('--------------------------------- LEGS SCENE Z UP --------------------------------- ')
    ik_match_orientation = {"legIk_Lt_a0": ("foot_Lt_bind", 90.0, 0.0),
                            "legIk_Rt_a0": ("foot_Rt_bind", -90.0, 180)}
if upScene == 'y':
    #cmds.warning('--------------------------------- LEGS SCENE Y UP --------------------------------- ')
    ik_match_orientation = {"legIk_Lt_a0": ("foot_Lt_bind", 0.0, 0.0, 0),
                        "legIk_Rt_a0": ("foot_Rt_bind", 0.0, 0.0, 0.0)}
    

footReparent = {'heel_Lt_plc': ["legIk_Lt_ikh", "foot_Lt_loc"], 'heel_Rt_plc': ["legIk_Rt_ikh", "foot_Rt_loc"]}

ikDict = {
          'thigh_Lt_jnt': ["thigh_Lt_ik", "foot_Lt_ik", "legIk_Lt_ikh", (0, 1, 0)],
          'thigh_Rt_jnt': ["thigh_Rt_ik", "foot_Rt_ik", "legIk_Rt_ikh", (0, 1, 0)],
          'shoulder_Lt_jnt': ["shoulder_Lt_ik", "hand_Lt_ik", "handIk_Lt_ikh", (1, 0, 0)],
          'shoulder_Rt_jnt': ["shoulder_Rt_ik", "hand_Rt_ik", "handIk_Rt_ikh", (1, 0, 0)]
          }

pvDict = {'thigh_Lt_jnt': ["kneeUpVectorIk_Lt_a0", "legBase_Lt_jnt", (0, 1, 0)],
          'thigh_Rt_jnt': ["kneeUpVectorIk_Rt_a0", "legBase_Rt_jnt", (0, 1, 0)],
          'shoulder_Lt_jnt': ["elbowUpVectorIk_Lt_a0", "armBase_Lt_jnt", (0, 0, 1)],
          'shoulder_Rt_jnt': ["elbowUpVectorIk_Rt_a0", "armBase_Rt_jnt", (0, 0, 1)]}

pvChainDict = {
               'thigh_Lt_jnt': ["thigh_Lt_jnt", "knee_Lt_jnt", "foot_Lt_bind"],
               'thigh_Rt_jnt': ["thigh_Rt_jnt", "knee_Rt_jnt", "foot_Rt_bind"],
               'shoulder_Lt_jnt': ["shoulder_Lt_jnt", "elbow_Lt_jnt", "hand_Lt_jnt"],
               'shoulder_Rt_jnt': ["shoulder_Rt_jnt", "elbow_Rt_jnt", "hand_Rt_jnt"]}


footAttrList = [u'Toe_Spin', u'Ball_Spin', u'Heel_Spin', u'Knee_Spin', u'Lean', u'Side_Tilt',
                u'Toe_Wiggle', u'Roll', u'Roll_Toe_Lift', u'Roll_Toe_Straight']

legIKattrs = {'legIk_Lt_anim': {'attributes': footAttrList, 'lock': ["radius"]},
              'legIk_Rt_anim': {'attributes': footAttrList, 'lock': ["radius"]}}

visDict = {"Lt": {}, "Rt": {}}


# ikAttrs = ["root03_Mid_anim"]
# ikAttrData = {}

pvAttrs = ["world_anim", "character02_Mid_anim", "root03Driven_Mid_anim", "pelvis_Mid_anim"]

pvAttrData = {}

attrHeader = "footActions"

pvAttrHeader = "spaceSwitch"

if upScene == 'y':
    footRoll = {"legIk_Lt_anim.Roll": {"nodes": {"footRoll_Lt_UTmd": {"attrs": {"input2X": 1.0},
                                                                    "type": "multiplyDivide"},
                                                "footRoll_Lt_UTcnd": {"attrs": {"secondTerm": 0.0,
                                                                                "operation": 4,
                                                                                "colorIfFalseR": 0.0},
                                                                    "type": "condition"},
                                                "footRoll_Lt_Ball_UTsr": {"attrs": {"maxX": 1},
                                                                        "type": "setRange"},
                                                "footRoll_Lt_Toe_UTsr": {"attrs": {"maxX": 1},
                                                                        "type": "setRange"},
                                                "footRoll_Lt_Range_UTmd": {"attrs": {},
                                                                            "type": "multiplyDivide"},
                                                "footRoll_Lt_UTpma": {"attrs": {"input1D[0]": 1.0,
                                                                                "operation": 2},
                                                                    "type": "plusMinusAverage"},
                                                "footRoll_Lt_BallAmount_UTmd": {"attrs": {},
                                                                                "type": "multiplyDivide"},
                                                "footRoll_Lt_BallRev_UTmd": {"attrs": {"input2X": 1.0},
                                                                            "type": "multiplyDivide"},
                                                "footRoll_Lt_ToeAmount_UTmd": {"attrs": {},
                                                                                "type": "multiplyDivide"},
                                                "footRoll_Lt_ToeRev_UTmd": {"attrs": {"input2X": 1.0},
                                                                            "type": "multiplyDivide"},
                                                }},
                "legIk_Rt_anim.Roll": {"nodes": {"footRoll_Rt_UTmd": {"attrs": {"input2X": 1.0},
                                                                    "type": "multiplyDivide"},
                                                "footRoll_Rt_UTcnd": {"attrs": {"secondTerm": 0.0,
                                                                                "operation": 4,
                                                                                "colorIfFalseR": 0.0},
                                                                    "type": "condition"},
                                                "footRoll_Rt_Ball_UTsr": {"attrs": {"maxX": 1},
                                                                        "type": "setRange"},
                                                "footRoll_Rt_Toe_UTsr": {"attrs": {"maxX": 1},
                                                                        "type": "setRange"},
                                                "footRoll_Rt_Range_UTmd": {"attrs": {},
                                                                            "type": "multiplyDivide"},
                                                "footRoll_Rt_UTpma": {"attrs": {"input1D[0]": 1.0,
                                                                                "operation": 2},
                                                                    "type": "plusMinusAverage"},
                                                "footRoll_Rt_BallAmount_UTmd": {"attrs": {},
                                                                                "type": "multiplyDivide"},
                                                "footRoll_Rt_BallRev_UTmd": {"attrs": {"input2X": 1.0},
                                                                            "type": "multiplyDivide"},
                                                "footRoll_Rt_ToeAmount_UTmd": {"attrs": {},
                                                                                "type": "multiplyDivide"},
                                                "footRoll_Rt_ToeRev_UTmd": {"attrs": {"input2X": 1.0},
                                                                            "type": "multiplyDivide"},
                                                }},
                }


    # Side_Tilt_Lt_loc_UTdl will reverse a single value for the tiltOut and tiltIn nodes downstream.
    sideTilt = {"tiltOut_Rt_loc.rotateX": {"nodes": {"sideTilt_Rt_Out_UTclamp": {"attrs": {"minR": 0, "maxR": 180},
                                                                                "type": "clamp"}}},
                "tiltIn_Rt_loc.rotateX": {"nodes": {"sideTilt_Rt_In_UTclamp": {"attrs": {"minR": -180, "maxR": 0},
                                                                            "type": "clamp"}}},
                "tiltOut_Lt_loc.rotateX": {"nodes": {"sideTilt_Lt_Rev_UTdl": {"attrs": {"input2": -1.0},
                                                                            "type": "multDoubleLinear"},
                                                    "sideTilt_Lt_Out_UTclamp": {"attrs": {"minR": -180, "maxR": 0},
                                                                                "type": "clamp"}}},
                "tiltIn_Lt_loc.rotateX": {"nodes": {"sideTilt_Lt_In_UTclamp": {"attrs": {"minR": 0, "maxR": 180},
                                                                            "type": "clamp"},
                                                    }},
                }

    reverseDict = {"legIk_Lt_anim.Toe_Spin": {"nodes": {"Toe_Spin_Lt_loc_UTdl": {"attrs": {"input2": -1.0},
                                                                                "type": "multDoubleLinear"}}},
                "legIk_Lt_anim.Ball_Spin": {"nodes": {"Ball_Spin_Lt_loc_UTdl": {"attrs": {"input2": -1.0},
                                                                                "type": "multDoubleLinear"}}},
                "legIk_Lt_anim.Heel_Spin": {"nodes": {"Heel_Spin_Lt_loc_UTdl": {"attrs": {"input2": -1.0},
                                                                                "type": "multDoubleLinear"}}},
                "legIk_Lt_anim.Knee_Spin": {"nodes": {"Knee_Spin_Lt_loc_UTdl": {"attrs": {"input2": -1.0},
                                                                                "type": "multDoubleLinear"}}},
                "legIk_Lt_anim.Lean": {"nodes": {"Lean_Lt_loc_UTdl": {"attrs": {"input2": -1.0},
                                                                        "type": "multDoubleLinear"},
                                                    }},
                }

if upScene == 'z':

    footRoll = {"legIk_Lt_anim.Roll": {"nodes": {"footRoll_Lt_UTmd": {"attrs": {"input2X": -1.0},
                                                                    "type": "multiplyDivide"},
                                                "footRoll_Lt_UTcnd": {"attrs": {"secondTerm": 0.0,
                                                                                "operation": 2,
                                                                                "colorIfFalseR": 0.0},
                                                                    "type": "condition"},
                                                "footRoll_Lt_Ball_UTsr": {"attrs": {"maxX": 1},
                                                                        "type": "setRange"},
                                                "footRoll_Lt_Toe_UTsr": {"attrs": {"maxX": 1},
                                                                        "type": "setRange"},
                                                "footRoll_Lt_Range_UTmd": {"attrs": {},
                                                                            "type": "multiplyDivide"},
                                                "footRoll_Lt_UTpma": {"attrs": {"input1D[0]": 1.0,
                                                                                "operation": 2},
                                                                    "type": "plusMinusAverage"},
                                                "footRoll_Lt_BallAmount_UTmd": {"attrs": {},
                                                                                "type": "multiplyDivide"},
                                                "footRoll_Lt_BallRev_UTmd": {"attrs": {"input2X": -1.0},
                                                                            "type": "multiplyDivide"},
                                                "footRoll_Lt_ToeAmount_UTmd": {"attrs": {},
                                                                                "type": "multiplyDivide"},
                                                "footRoll_Lt_ToeRev_UTmd": {"attrs": {"input2X": -1.0},
                                                                            "type": "multiplyDivide"},
                                                }},
                "legIk_Rt_anim.Roll": {"nodes": {"footRoll_Rt_UTmd": {"attrs": {"input2X": -1.0},
                                                                    "type": "multiplyDivide"},
                                                "footRoll_Rt_UTcnd": {"attrs": {"secondTerm": 0.0,
                                                                                "operation": 2,
                                                                                "colorIfFalseR": 0.0},
                                                                    "type": "condition"},
                                                "footRoll_Rt_Ball_UTsr": {"attrs": {"maxX": 1},
                                                                        "type": "setRange"},
                                                "footRoll_Rt_Toe_UTsr": {"attrs": {"maxX": 1},
                                                                        "type": "setRange"},
                                                "footRoll_Rt_Range_UTmd": {"attrs": {},
                                                                            "type": "multiplyDivide"},
                                                "footRoll_Rt_UTpma": {"attrs": {"input1D[0]": 1.0,
                                                                                "operation": 2},
                                                                    "type": "plusMinusAverage"},
                                                "footRoll_Rt_BallAmount_UTmd": {"attrs": {},
                                                                                "type": "multiplyDivide"},
                                                "footRoll_Rt_BallRev_UTmd": {"attrs": {"input2X": -1.0},
                                                                            "type": "multiplyDivide"},
                                                "footRoll_Rt_ToeAmount_UTmd": {"attrs": {},
                                                                                "type": "multiplyDivide"},
                                                "footRoll_Rt_ToeRev_UTmd": {"attrs": {"input2X": -1.0},
                                                                            "type": "multiplyDivide"},
                                                }},
                }


    # Side_Tilt_Lt_loc_UTdl will reverse a single value for the tiltOut and tiltIn nodes downstream.
    sideTilt = {"tiltOut_Rt_loc.rotateX": {"nodes": {"sideTilt_Rt_Out_UTclamp": {"attrs": {"minR": 0, "maxR": 180},
                                                                                "type": "clamp"}}},
                "tiltIn_Rt_loc.rotateX": {"nodes": {"sideTilt_Rt_In_UTclamp": {"attrs": {"minR": -180, "maxR": 0},
                                                                            "type": "clamp"}}},
                "tiltOut_Lt_loc.rotateX": {"nodes": {"sideTilt_Lt_Rev_UTdl": {"attrs": {"input2": -1.0},
                                                                            "type": "multDoubleLinear"},
                                                    "sideTilt_Lt_Out_UTclamp": {"attrs": {"minR": -180, "maxR": 0},
                                                                                "type": "clamp"}}},
                "tiltIn_Lt_loc.rotateX": {"nodes": {"sideTilt_Lt_In_UTclamp": {"attrs": {"minR": 0, "maxR": 180},
                                                                            "type": "clamp"},
                                                    }},
                }

    reverseDict = {"legIk_Lt_anim.Toe_Spin": {"nodes": {"Toe_Spin_Lt_loc_UTdl": {"attrs": {"input2": -1.0},
                                                                                "type": "multDoubleLinear"}}},
                "legIk_Lt_anim.Ball_Spin": {"nodes": {"Ball_Spin_Lt_loc_UTdl": {"attrs": {"input2": -1.0},
                                                                                "type": "multDoubleLinear"}}},
                "legIk_Lt_anim.Heel_Spin": {"nodes": {"Heel_Spin_Lt_loc_UTdl": {"attrs": {"input2": -1.0},
                                                                                "type": "multDoubleLinear"}}},
                "legIk_Lt_anim.Knee_Spin": {"nodes": {"Knee_Spin_Lt_loc_UTdl": {"attrs": {"input2": -1.0},
                                                                                "type": "multDoubleLinear"}}},
                "legIk_Lt_anim.Lean": {"nodes": {"Lean_Lt_loc_UTdl": {"attrs": {"input2": -1.0},
                                                                        "type": "multDoubleLinear"},
                                                    }},
                }

if upScene == 'y':
    connections = [
                # Side Tilt Rt

                ("legIk_Rt_anim.Side_Tilt", "sideTilt_Rt_Out_UTclamp.inputR"),
                ("sideTilt_Rt_Out_UTclamp.outputR", "tiltOut_Rt_loc.rotateZ"),

                ("legIk_Rt_anim.Side_Tilt", "sideTilt_Rt_In_UTclamp.inputR"),
                ("sideTilt_Rt_In_UTclamp.outputR", "tiltIn_Rt_loc.rotateZ"),

                # Side Tilt Lt

                ("legIk_Lt_anim.Side_Tilt", "sideTilt_Lt_Rev_UTdl.input1"),  # reverse Side_Tilt Lt

                ("sideTilt_Lt_Rev_UTdl.output", "sideTilt_Lt_Out_UTclamp.inputR"),
                ("sideTilt_Lt_Out_UTclamp.outputR", "tiltOut_Lt_loc.rotateZ"),

                ("sideTilt_Lt_Rev_UTdl.output", "sideTilt_Lt_In_UTclamp.inputR"),
                ("sideTilt_Lt_In_UTclamp.outputR", "tiltIn_Lt_loc.rotateZ"),

                # reverse Lt heel roll
                ("legIk_Lt_anim.Roll", "footRoll_Lt_UTmd.input1X"),          # reverse Roll Lt
                ("footRoll_Lt_UTmd.outputX", "footRoll_Lt_UTcnd.firstTerm"),
                ("footRoll_Lt_UTmd.outputX", "footRoll_Lt_UTcnd.colorIfTrueR"),
                ("footRoll_Lt_UTcnd.outColorR", "heelRoll_Lt_loc.rotateX"),

                # Reverse Foot Roll Lt
                ("legIk_Lt_anim.Roll", "footRoll_Lt_Ball_UTsr.valueX"),
                ("legIk_Lt_anim.Roll_Toe_Lift", "footRoll_Lt_Ball_UTsr.oldMaxX"),

                ("legIk_Lt_anim.Roll", "footRoll_Lt_Toe_UTsr.valueX"),
                ("legIk_Lt_anim.Roll_Toe_Lift", "footRoll_Lt_Toe_UTsr.oldMinX"),
                ("legIk_Lt_anim.Roll_Toe_Straight", "footRoll_Lt_Toe_UTsr.oldMaxX"),

                ("footRoll_Lt_Ball_UTsr.outValueX", "footRoll_Lt_Range_UTmd.input1X"),
                ("legIk_Lt_anim.Roll", "footRoll_Lt_Range_UTmd.input2X"),

                ("footRoll_Lt_Toe_UTsr.outValueX", "footRoll_Lt_UTpma.input1D[1]"),

                ("footRoll_Lt_UTpma.output1D", "footRoll_Lt_BallAmount_UTmd.input1X"),
                ("footRoll_Lt_Range_UTmd.outputX", "footRoll_Lt_BallAmount_UTmd.input2X"),

                ("footRoll_Lt_BallAmount_UTmd.outputX", "footRoll_Lt_BallRev_UTmd.input1X"),
                ("footRoll_Lt_BallRev_UTmd.outputX", "footRoll_Lt_loc.rotateX"),

                ("legIk_Lt_anim.Roll", "footRoll_Lt_ToeAmount_UTmd.input2X"),
                ("footRoll_Lt_Toe_UTsr.outValueX", "footRoll_Lt_ToeAmount_UTmd.input1X"),
                ("footRoll_Lt_ToeAmount_UTmd.outputX", "footRoll_Lt_ToeRev_UTmd.input1X"),
                ("footRoll_Lt_ToeRev_UTmd.outputX", "toeTip_Lt_a0.rotateX"),

                # Reverse Foot Roll Lt
                ("legIk_Rt_anim.Roll", "footRoll_Rt_Ball_UTsr.valueX"),
                ("legIk_Rt_anim.Roll_Toe_Lift", "footRoll_Rt_Ball_UTsr.oldMaxX"),

                ("legIk_Rt_anim.Roll", "footRoll_Rt_Toe_UTsr.valueX"),
                ("legIk_Rt_anim.Roll_Toe_Lift", "footRoll_Rt_Toe_UTsr.oldMinX"),
                ("legIk_Rt_anim.Roll_Toe_Straight", "footRoll_Rt_Toe_UTsr.oldMaxX"),

                ("footRoll_Rt_Ball_UTsr.outValueX", "footRoll_Rt_Range_UTmd.input1X"),
                ("legIk_Rt_anim.Roll", "footRoll_Rt_Range_UTmd.input2X"),

                ("footRoll_Rt_Toe_UTsr.outValueX", "footRoll_Rt_UTpma.input1D[1]"),

                ("footRoll_Rt_UTpma.output1D", "footRoll_Rt_BallAmount_UTmd.input1X"),
                ("footRoll_Rt_Range_UTmd.outputX", "footRoll_Rt_BallAmount_UTmd.input2X"),

                ("footRoll_Rt_BallAmount_UTmd.outputX", "footRoll_Rt_BallRev_UTmd.input1X"),
                ("footRoll_Rt_BallRev_UTmd.outputX", "footRoll_Rt_loc.rotateX"),

                ("legIk_Rt_anim.Roll", "footRoll_Rt_ToeAmount_UTmd.input2X"),
                ("footRoll_Rt_Toe_UTsr.outValueX", "footRoll_Rt_ToeAmount_UTmd.input1X"),
                ("footRoll_Rt_ToeAmount_UTmd.outputX", "footRoll_Rt_ToeRev_UTmd.input1X"),
                ("footRoll_Rt_ToeRev_UTmd.outputX", "toeTip_Rt_a0.rotateX"),

                # reverse Rt heel roll
                ("legIk_Rt_anim.Roll", "footRoll_Rt_UTmd.input1X"),          
                
                # reverse Roll Rt
                ("footRoll_Rt_UTmd.outputX", "footRoll_Rt_UTcnd.firstTerm"),
                ("footRoll_Rt_UTmd.outputX", "footRoll_Rt_UTcnd.colorIfTrueR"),
                ("footRoll_Rt_UTcnd.outColorR", "heelRoll_Rt_loc.rotateX"),

                # reversed-value Lt connections
                ("legIk_Lt_anim.Toe_Spin", "Toe_Spin_Lt_loc_UTdl.input1"),
                ("Toe_Spin_Lt_loc_UTdl.output", "toeTip_Lt_a0.rotateY"),

                ("legIk_Lt_anim.Ball_Spin", "Ball_Spin_Lt_loc_UTdl.input1"),
                ("Ball_Spin_Lt_loc_UTdl.output", "footBall_Lt_loc.rotateY"),

                ("legIk_Lt_anim.Heel_Spin", "Heel_Spin_Lt_loc_UTdl.input1"),
                ("Heel_Spin_Lt_loc_UTdl.output", "heelRoll_Lt_loc.rotateY"),

                ("legIk_Lt_anim.Knee_Spin", "Knee_Spin_Lt_loc_UTdl.input1"),
                ("Knee_Spin_Lt_loc_UTdl.output", "legIk_Lt_ikh.twist"),

                ("legIk_Lt_anim.Lean", "Lean_Lt_loc_UTdl.input1"),
                ("Lean_Lt_loc_UTdl.output", "footRoll_Lt_loc.rotateZ"),

                # direct connections (Rt)
                ("legIk_Rt_anim.Toe_Spin", "toeTip_Rt_a0.rotateY"),
                ("legIk_Rt_anim.Ball_Spin", "footBall_Rt_loc.rotateY"),
                ("legIk_Rt_anim.Heel_Spin", "heelRoll_Rt_loc.rotateY"),
                ("legIk_Rt_anim.Knee_Spin", "legIk_Rt_ikh.twist"),
                ("legIk_Rt_anim.Lean", "footRoll_Rt_loc.rotateZ"),
                ("legIk_Rt_anim.Toe_Wiggle", "toe_Rt_loc.rotateX"),
                ("legIk_Lt_anim.Toe_Wiggle", "toe_Lt_loc.rotateX"),
                ]
if upScene == 'z':
    connections = [
                # Side Tilt Rt

                ("legIk_Rt_anim.Side_Tilt", "sideTilt_Rt_Out_UTclamp.inputR"),
                ("sideTilt_Rt_Out_UTclamp.outputR", "tiltOut_Rt_loc.rotateX"),

                ("legIk_Rt_anim.Side_Tilt", "sideTilt_Rt_In_UTclamp.inputR"),
                ("sideTilt_Rt_In_UTclamp.outputR", "tiltIn_Rt_loc.rotateX"),

                # Side Tilt Lt

                ("legIk_Lt_anim.Side_Tilt", "sideTilt_Lt_Rev_UTdl.input1"),  # reverse Side_Tilt Lt

                ("sideTilt_Lt_Rev_UTdl.output", "sideTilt_Lt_Out_UTclamp.inputR"),
                ("sideTilt_Lt_Out_UTclamp.outputR", "tiltOut_Lt_loc.rotateX"),

                ("sideTilt_Lt_Rev_UTdl.output", "sideTilt_Lt_In_UTclamp.inputR"),
                ("sideTilt_Lt_In_UTclamp.outputR", "tiltIn_Lt_loc.rotateX"),

                # reverse Lt heel roll
                ("legIk_Lt_anim.Roll", "footRoll_Lt_UTmd.input1X"),          # reverse Roll Lt
                ("footRoll_Lt_UTmd.outputX", "footRoll_Lt_UTcnd.firstTerm"),
                ("footRoll_Lt_UTmd.outputX", "footRoll_Lt_UTcnd.colorIfTrueR"),
                ("footRoll_Lt_UTcnd.outColorR", "heelRoll_Lt_loc.rotateZ"),

                # Reverse Foot Roll Lt
                ("legIk_Lt_anim.Roll", "footRoll_Lt_Ball_UTsr.valueX"),
                ("legIk_Lt_anim.Roll_Toe_Lift", "footRoll_Lt_Ball_UTsr.oldMaxX"),

                ("legIk_Lt_anim.Roll", "footRoll_Lt_Toe_UTsr.valueX"),
                ("legIk_Lt_anim.Roll_Toe_Lift", "footRoll_Lt_Toe_UTsr.oldMinX"),
                ("legIk_Lt_anim.Roll_Toe_Straight", "footRoll_Lt_Toe_UTsr.oldMaxX"),

                ("footRoll_Lt_Ball_UTsr.outValueX", "footRoll_Lt_Range_UTmd.input1X"),
                ("legIk_Lt_anim.Roll", "footRoll_Lt_Range_UTmd.input2X"),

                ("footRoll_Lt_Toe_UTsr.outValueX", "footRoll_Lt_UTpma.input1D[1]"),

                ("footRoll_Lt_UTpma.output1D", "footRoll_Lt_BallAmount_UTmd.input1X"),
                ("footRoll_Lt_Range_UTmd.outputX", "footRoll_Lt_BallAmount_UTmd.input2X"),

                ("footRoll_Lt_BallAmount_UTmd.outputX", "footRoll_Lt_BallRev_UTmd.input1X"),
                ("footRoll_Lt_BallRev_UTmd.outputX", "footRoll_Lt_loc.rotateZ"),

                ("legIk_Lt_anim.Roll", "footRoll_Lt_ToeAmount_UTmd.input2X"),
                ("footRoll_Lt_Toe_UTsr.outValueX", "footRoll_Lt_ToeAmount_UTmd.input1X"),
                ("footRoll_Lt_ToeAmount_UTmd.outputX", "footRoll_Lt_ToeRev_UTmd.input1X"),
                ("footRoll_Lt_ToeRev_UTmd.outputX", "toeTip_Lt_a0.rotateZ"),

                # Reverse Foot Roll Lt
                ("legIk_Rt_anim.Roll", "footRoll_Rt_Ball_UTsr.valueX"),
                ("legIk_Rt_anim.Roll_Toe_Lift", "footRoll_Rt_Ball_UTsr.oldMaxX"),

                ("legIk_Rt_anim.Roll", "footRoll_Rt_Toe_UTsr.valueX"),
                ("legIk_Rt_anim.Roll_Toe_Lift", "footRoll_Rt_Toe_UTsr.oldMinX"),
                ("legIk_Rt_anim.Roll_Toe_Straight", "footRoll_Rt_Toe_UTsr.oldMaxX"),

                ("footRoll_Rt_Ball_UTsr.outValueX", "footRoll_Rt_Range_UTmd.input1X"),
                ("legIk_Rt_anim.Roll", "footRoll_Rt_Range_UTmd.input2X"),

                ("footRoll_Rt_Toe_UTsr.outValueX", "footRoll_Rt_UTpma.input1D[1]"),

                ("footRoll_Rt_UTpma.output1D", "footRoll_Rt_BallAmount_UTmd.input1X"),
                ("footRoll_Rt_Range_UTmd.outputX", "footRoll_Rt_BallAmount_UTmd.input2X"),

                ("footRoll_Rt_BallAmount_UTmd.outputX", "footRoll_Rt_BallRev_UTmd.input1X"),
                ("footRoll_Rt_BallRev_UTmd.outputX", "footRoll_Rt_loc.rotateZ"),

                ("legIk_Rt_anim.Roll", "footRoll_Rt_ToeAmount_UTmd.input2X"),
                ("footRoll_Rt_Toe_UTsr.outValueX", "footRoll_Rt_ToeAmount_UTmd.input1X"),
                ("footRoll_Rt_ToeAmount_UTmd.outputX", "footRoll_Rt_ToeRev_UTmd.input1X"),
                ("footRoll_Rt_ToeRev_UTmd.outputX", "toeTip_Rt_a0.rotateZ"),

                # reverse Rt heel roll
                ("legIk_Rt_anim.Roll", "footRoll_Rt_UTmd.input1X"),          # reverse Roll Rt
                ("footRoll_Rt_UTmd.outputX", "footRoll_Rt_UTcnd.firstTerm"),
                ("footRoll_Rt_UTmd.outputX", "footRoll_Rt_UTcnd.colorIfTrueR"),
                ("footRoll_Rt_UTcnd.outColorR", "heelRoll_Rt_loc.rotateZ"),

                # reversed-value Lt connections
                ("legIk_Lt_anim.Toe_Spin", "Toe_Spin_Lt_loc_UTdl.input1"),
                ("Toe_Spin_Lt_loc_UTdl.output", "toeTip_Lt_a0.rotateY"),

                ("legIk_Lt_anim.Ball_Spin", "Ball_Spin_Lt_loc_UTdl.input1"),
                ("Ball_Spin_Lt_loc_UTdl.output", "footBall_Lt_loc.rotateY"),

                ("legIk_Lt_anim.Heel_Spin", "Heel_Spin_Lt_loc_UTdl.input1"),
                ("Heel_Spin_Lt_loc_UTdl.output", "heelRoll_Lt_loc.rotateY"),

                ("legIk_Lt_anim.Knee_Spin", "Knee_Spin_Lt_loc_UTdl.input1"),
                ("Knee_Spin_Lt_loc_UTdl.output", "legIk_Lt_ikh.twist"),

                ("legIk_Lt_anim.Lean", "Lean_Lt_loc_UTdl.input1"),
                ("Lean_Lt_loc_UTdl.output", "footRoll_Lt_loc.rotateX"),

                # direct connections (Rt)
                ("legIk_Rt_anim.Toe_Spin", "toeTip_Rt_a0.rotateY"),
                ("legIk_Rt_anim.Ball_Spin", "footBall_Rt_loc.rotateY"),
                ("legIk_Rt_anim.Heel_Spin", "heelRoll_Rt_loc.rotateY"),
                ("legIk_Rt_anim.Knee_Spin", "legIk_Rt_ikh.twist"),
                ("legIk_Rt_anim.Lean", "footRoll_Rt_loc.rotateX"),
                ("legIk_Rt_anim.Toe_Wiggle", "toe_Rt_loc.rotateZ"),
                ("legIk_Lt_anim.Toe_Wiggle", "toe_Lt_loc.rotateZ"),
                ]


def create_groups():
    for g in ["rig_XXX_grp"] + rigChildren + setChildren + ctlChildren:
        if not pm.objExists(g):
            pm.group(name=g, empty=True)
    for g in rigChildren:
        pm.parent(g, "rig_XXX_grp")
    for g in setChildren:
        pm.parent(g, "setup_grp")
    for g in ctlChildren:
        pm.parent(g, "controls_grp")


def build_nodes():
    node_dict = {}
    node_dict.update(sideTilt)
    node_dict.update(footRoll)
    node_dict.update(reverseDict)
    for driven in node_dict:
        for name in node_dict[driven]["nodes"]:
            typ = node_dict[driven]["nodes"][name]["type"]
            attrs = node_dict[driven]["nodes"][name]["attrs"]
            node = pm.createNode(typ, name=name)
            for attr in attrs:
                val = attrs[attr]
                node.setAttr(attr, val)


def make_connections():
    for src, dst in connections:
        tools.debug_print("connecting: " + src + " " + dst, dbg=debug)
        pm.connectAttr(src, dst)


def apply_ik(x):
    start = ikDict[x][0]
    end = ikDict[x][1]
    hnd = ikDict[x][2]
    nrm = ikDict[x][3]
    eff = tools.get_new_name(hnd, "ike")
    trn = tools.get_new_name(hnd, "a0")
    jnt = tools.get_new_name(hnd, "anim")
    gim = tools.expand_prefix(jnt, "Gimbal")
    col = tools.find_lr_override_color(x)
    """ apply Rotate-Plane IK solver """
    ikh = pm.ikHandle(solver="ikRPsolver", startJoint=start, endEffector=end)
    ikh[0].rename(hnd)
    ikh[1].rename(eff)
    """ make empty transform by creating an empty group """
    ikt = pm.group(name=trn, empty=True)
    pm.parent(ikt, ikh[1], relative=True)
    ikt.setParent(None)
    if trn in ik_match_orientation:
        tup = ik_match_orientation[trn]
        target = tup[0]
        ikt.setParent(target)
        ikt.setAttr("rotate", (0, 0, 0))
        ikt.setParent(None)
        ikt.setAttr("rotateX", tup[1])
        ikt.setAttr("rotateY", tup[2])
        if upScene == 'y':
            ikt.setAttr("rotateZ", tup[3])

    else:
        tools.zero_rotation(ikt)
    pm.parent(ikt, "controls_grp")
    """ create control joint """
    if trn in ik_match_orientation:
        ikj = pm.PyNode(tools.make_joint(jnt, clear_selection=False, zero=True))
    else:
        ikj = pm.PyNode(tools.make_joint(jnt, clear_selection=False))
    ikg = pm.PyNode(tools.make_joint(gim, zero=True, clear_selection=False))
    if x.startswith("shoulder"):
        pm.parent(ikj, handTargets[x], relative=True)
        z = {'jointOrientX': 0, 'jointOrientZ': 0}
        for k in z:
            ikj.setAttr(k, z[k])
        tools.zero_rotation(ikj)
    pm.parent(ikj, ikt)
    """ replace control joint's shape with that of a circle """
    tools.apply_circle(ikj, nrm, color=col)
    # tools.apply_circle(ikg, nrm, color=col, degree=1, sections=4)
    shp = tools.apply_shape(ikg, "fourPointArrow_anim")
    tools.set_override_color(shp, 17)
    if ikg.startswith("hand"):
        tools.rotate_shape(shp, (0, 0, 90))
    """ parentObjects IK handle to joint. """
    ikh[0].setParent(ikg)
    """ enter data into visDict """
    side = x.split("_")[1]
    if x.startswith("shoulder"):
        key = "arm"
        ikj.addAttr("elbowSpin")
        ikj.setAttr("elbowSpin", channelBox=True)
        ikj.setAttr("elbowSpin", keyable=True)
        pm.connectAttr(ikj + ".elbowSpin", ikh[0] + ".twist")
    else:
        key = "leg"
    visDict[side][key] = ikg


def make_pv_target(li):
    """
        :param li: a list of three joints
        :return: a group on the same plane as the three joints

        based on a routine by Marco Giordano
        http://vimeo.com/66262994
    """
    start = pm.joint(li[0], query=True, position=True)
    mid = pm.joint(li[1], query=True, position=True)
    end = pm.joint(li[2], query=True, position=True)

    start_v = OpenMaya.MVector(start[0], start[1], start[2])
    mid_v = OpenMaya.MVector(mid[0], mid[1], mid[2])
    end_v = OpenMaya.MVector(end[0], end[1], end[2])

    start_end = end_v - start_v
    start_mid = mid_v - start_v

    dot_p = start_mid * start_end
    proj = dot_p/start_end.length()
    start_end_n = start_end.normal()
    proj_v = start_end_n * proj

    arrow_v = start_mid - proj_v
    tools.debug_print("\tarrowV before: " + str(arrow_v.length()), dbg=debug)
    arrow_v /= arrow_v.length()
    tools.debug_print("\tarrowV after divide: " + str(arrow_v.length()), dbg=debug)
    arrow_v *= start_end.length()
    tools.debug_print("\tarrowV after multiply: " + str(arrow_v.length()), dbg=debug)
    final_v = arrow_v + mid_v

    grp = pm.group(empty=True)
    pm.xform(translation=(final_v.x, final_v.y, final_v.z))
    return grp


def apply_pv(x):
    """
    :param x: the name of the root of the affected limb
    :return: a pole vector constraint
    """
    a0 = pvDict[x][0]
    p0 = pvDict[x][1]
    a1 = tools.get_new_name(a0, "a1")
    jn = tools.get_new_name(a0, "anim")
    nm = pvDict[x][2]
    p1 = ikDict[x][2]
    ih = ikDict[x][2]
    an = tools.get_new_name(ih, "anim")
    co = tools.find_lr_override_color(x)
    """ create a0 transform and constrain it between the start and end of the limb """
    knc = pm.group(name=a0, empty=True)
    pm.parent(a0, "controls_grp")
    pm.pointConstraint(p0, p1, a0, w=0.5)
    kng = make_pv_target(pvChainDict[x])
    pm.rename(kng, a1)
    tools.zero_rotation(knc)
    pm.parent(a1, a0)
    jnt = tools.make_joint(jn, clear_selection=False)
    jnt.setParent(kng)
    tools.apply_circle(jnt, nm, color=co)
    if jnt.startswith("knee"):
        attrs = pvAttrs + [a0, an]
        tools.create_attributes(jnt, pvAttrHeader, attrs)
        jnt.setAttr(an, 1)
    else:
        extra = ["spine03Fk_Mid_anim", "clavicle_%s_anim" % tools.get_lr(jnt)]
        attrs = pvAttrs + extra + [a0, an]
        tools.create_attributes(jnt, pvAttrHeader, attrs)
        jnt.setAttr("spine03Fk_Mid_anim", 1)
    pvAttrData[jnt] = {"object": kng, "targets": attrs, "constraint": pm.parentConstraint, "interpType": 2}
    for attr in attrs:
        pm.addAttr(jnt + "." + attr, edit=True, hasMaxValue=True, hasMinValue=True, minValue=0.0, maxValue=1.0)
    pm.poleVectorConstraint(jnt, ih, name=ih+"_poleVectorConstraint")


def setup_foot_hierarchy(x):

    """
    :param x: name of foot placement object
    :return: reverse-foot setupSpine
    """
    for tup in feet[x]:
        name, parent, placement = tup
        color = tools.find_lr_override_color(name)
        """ create object """
        if name.endswith("_anim"):
            if name.startswith("heel"):
                obj = tools.make_joint(name, zero=False, world=True, clear_selection=False)
            else:
                obj = tools.make_joint(name, zero=True, world=True, clear_selection=False)
            box = makeBox.make_box(4, 4, 4)
            shp = box.getShape()
            tools.set_override_color(shp, color)
            pm.parent(shp, obj, relative=True, shape=True)
            pm.delete(box)
        else:
            obj = pm.group(name=name, empty=True, world=True)
        """ place the unparented object in world space """
        pos = pm.joint(placement, q=True, position=True)
        if name.startswith("footBall"):
            pos[2] = 0
        pm.xform(translation=pos)
        """ if necessary, match world Z-orientation of placement object """
        if name in feet_match_orientation:
            print("Matching {0} rotation to {1}".format(name, placement))
            rotation = pm.xform(placement, query=True, worldSpace=True, rotation=True)
            if upScene == 'z':
                pm.xform(obj, rotation=(0, 0, rotation[2]))
            if upScene == 'y':
                pm.xform(obj, rotation=(0, 0, 0))
                print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ROTATE FOOT 0 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
        """ set parentObjects of object """
        obj.setParent(parent)
        if not (name.startswith("heel") and name.endswith("a0")):
            tools.zero_rotation(obj)


def setup_foot_ik(x):
    """ setupSpine IK on foot """
    for k in footIKChains[x]:
        start = k
        end = footIKChains[x][k]
        ikh = pm.ikHandle(solver="ikSCsolver", startJoint=start, endEffector=end)
        ikh[0].rename(tools.get_new_name(k, "ikh"))
        ikh[1].rename(tools.get_new_name(k, "ike"))
        parent = tools.get_new_name(k, "loc")
        ikh[0].setParent(parent)


def reparent_leg_ikh(x):
    leg_ikh = footReparent[x][0]
    parent = footReparent[x][1]
    if pm.objExists(leg_ikh) and pm.objExists(parent):
        pm.parent(leg_ikh, parent)


def draw_pv_line(x):
    tgt1 = tools.get_new_name(pvChainDict[x][1], "ik")
    tgt2 = tools.get_new_name(pvDict[x][0], "anim")
    line_name = tools.get_new_name(tgt1, "jnt")
    line_name = tools.expand_prefix(line_name, "PV")
    grp_name = tools.get_new_name(line_name, "a0")
    crv_name = tools.get_new_name(line_name, "curve")
    skn_name = tools.get_new_name(crv_name, "skin")
    grp = pm.group(empty=True, name=grp_name)
    jnt = tools.make_joint(line_name, zero=True, world=True)
    jnt.setParent(grp)
    pos1 = pm.xform(tgt1, query=True, translation=True, worldSpace=True)
    pos2 = pm.xform(tgt2, query=True, translation=True, worldSpace=True)
    crv = pm.curve(point=[pos1, pos2], degree=1)
    crv_shape = crv.getShape()
    pm.parent(crv_shape, jnt, relative=True, shape=True)
    pm.delete(crv)
    pm.rename(crv_shape, crv_name)
    tools.debug_print("Skinning " + crv_name + " to " + tgt1 + " and " + tgt2, dbg=debug)
    pm.select([tgt1, tgt2])
    pm.skinCluster(crv_name, tgt1, tgt2, name=skn_name, toSelectedBones=True)
    pm.select(clear=True)
    jnt.setAttr("overrideEnabled", True)
    jnt.setAttr("overrideDisplayType", 2)


def setup_ik():
    """
    :return: main program.
    """
    pm.select(clear=True)
    create_groups()
    # pm.parent("root_Mid_jnt", "skeleton_grp")
    """ leg and foot setupSpine """
    for limb in limbs:
        tools.create_duplicate_chain(limb, "ik")
        apply_ik(limb)
        apply_pv(limb)
        draw_pv_line(limb)
    for foot in feet:
        setup_foot_hierarchy(foot)
        setup_foot_ik(foot)
        reparent_leg_ikh(foot)
    for obj in pm.ls("*_plc"):
        pm.delete(obj)
    for name in legIKattrs:
        attrs = legIKattrs[name]['attributes']
        locks = legIKattrs[name]['lock']
        tools.create_attributes(name, attrHeader, attrs)
        tools.lock_attributes([name], locks)
        """ init non-zero defaults """
        d = {"Roll_Toe_Lift": 45, "Roll_Toe_Straight": 90}
        for attr in d:
            pm.setAttr(name + "." + attr, d[attr])
    build_nodes()
    make_connections()
    pm.select(clear=True)
