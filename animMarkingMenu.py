import maya.cmds as mc
import maya.mel as mm

def unlock(nodes):
    nodes = mc.ls(nodes)
    for node in nodes:
        for a in ['tx','ty','tz','rx','ry','rz']:
            mc.setAttr(node+'.'+a, l=0, k=1)

def match(master, driven, trans=True, rot=True):
    """Simple utility for matching xforms from one driver to other nodes.
        Kwargs:
            :nodes: (list) Nodes to snap.. Select driver first then nodes to match.
            :position: (bool) Match position.
            :orientation: (bool) Match orientation.
            :pivot: (bool) Match pivots."""

    proxyObj = mc.duplicate(driven, po=1)[0]

    for a in ['tx','ty','tz','rx','ry','rz']:
        mc.setAttr(proxyObj+'.'+a, l=0, k=1)

    mc.delete(mc.pointConstraint(master, proxyObj))
    mc.delete(mc.orientConstraint(master, proxyObj))

    if trans:
        mc.xform(driven, a=1, t=mc.xform(proxyObj, q=1, a=1, t=1))

    if rot:
        mc.xform(driven, a=1,  ro=mc.xform(proxyObj, q=1, a=1, ro=1))

    mc.delete(proxyObj)

def switch_space(space_idx=0, nodes=None, space_attr='space', set_key=False):
    """Anim utility for switching spaces via right clikc dag menu"""

    csel = mc.ls(sl=1)

    if not nodes:
        nodes = mc.ls(sl=1)

    snodes = [n for n in mc.ls(nodes) if mc.objExists(n+'.'+space_attr)]
    if not snodes:
        # defaults to transspace if space attr does not exists on nodes
        space_attr = 'transSpace'
        snodes = [n for n in mc.ls(nodes) if mc.objExists(n+'.'+space_attr)]

    for node in snodes:

        tmp = mc.createNode('transform')
        match(node, tmp)

        if set_key:
            mc.setKeyframe(node+'.'+space_attr, t=mc.currentTime(q=1)-1)
            mc.setKeyframe(node+'.t', t=mc.currentTime(q=1)-1)
            mc.setKeyframe(node+'.r', t=mc.currentTime(q=1)-1)

        mc.setAttr(node+'.'+space_attr, space_idx)
        match(tmp, node)
        mc.delete(tmp)

        if set_key:
            mc.setKeyframe(node+'.'+space_attr)
            mc.setKeyframe(node+'.t')
            mc.setKeyframe(node+'.r')

    mc.select(csel)

def switch_IK(ctrl=None, set_key=False):
    """Master function for swiotchingf IK"""

    if not ctrl:
        ctrl = mc.ls(sl=1)

    ctrl = mc.ls(ctrl)
    if not ctrl or not mc.objExists(ctrl[0]+'.IK'):
        mc.warning('Select an IK switch control!')
        return

    if not ctrl or not mc.objExists(ctrl[0]+'.matchFunction'):
        mc.warning('Cannot pull IK switch function name!')
        return

    ctrl = ctrl[0]
    func = mc.getAttr(ctrl+'.matchFunction').lower()

    if func == 'bipedarm':
        switch_bipedarm_IK(ctrl, set_key=set_key)

    elif func == 'bipedleg':
        # for some reason this works bette rif its run 3 times
        for i in range(3):
           switch_bipedleg_IK(ctrl, set_key=set_key)

def switch_bipedarm_IK(ctrl=None, set_key=False):

    csel = mc.ls(sl=1)
    if not ctrl:
        ctrl = mc.ls(sl=1)
    ctrl = mc.ls(ctrl)[0]

    if 'arm_IK_switch' not in ctrl:
        mc.warning('Select a bipedArm IK switch control!')
        return

    msg = None

    # declare nodes (this has to be part specific)
    prefix = ctrl.split('arm_IK_switch')[0]
    ik_ctrl = prefix+'arm_IK_CTL'
    pv_ctrl = prefix+'arm_PV_CTL'

    ik_ctrl_snap = prefix+'arm_IK_CTL_SNAPTO'
    pv_ctrl_snap = prefix+'arm_PV_CTL_SNAPTO'

    fk_ctrls = [prefix+'upArm_FK_CTL', prefix+'loArm_FK_CTL', prefix+'wrist_FK_CTL']
    jnts = [prefix+'upArm_IK_JNT', prefix+'loArm_IK_JNT', prefix+'wrist_IK_JNT']

    current_val = mc.getAttr(ctrl+'.IK')

    if not mc.objExists(ik_ctrl_snap) or not mc.objExists(pv_ctrl_snap):
        mc.warning('This rig needs to be rebuilt to allow FK IK matching!')
        return

    key_ctrls = [ik_ctrl, pv_ctrl]+fk_ctrls

    if set_key:
        mc.setKeyframe(ctrl+'.IK', t=mc.currentTime(q=1)-1)
        mc.setKeyframe([c+'.t' for c in key_ctrls], t=mc.currentTime(q=1)-1)
        mc.setKeyframe([c+'.r' for c in key_ctrls], t=mc.currentTime(q=1)-1)

    if current_val < 0.5:

        match(ik_ctrl_snap, ik_ctrl)
        match(pv_ctrl_snap, pv_ctrl)
        mc.setAttr(ctrl+'.IK', 1)

        if round(mc.getAttr(fk_ctrls[1]+'.rx'), 2) and round(mc.getAttr(fk_ctrls[1]+'.rx'), 2):
            msg = '<hl>rotateX</hl> and <hl>rotateZ</hl>'
        elif round(mc.getAttr(fk_ctrls[1]+'.rx'), 2):
            msg = '<hl>rotateX</hl>'
        elif round(mc.getAttr(fk_ctrls[1]+'.rz'), 2):
            msg = '<hl>rotateZ</hl>'

    else:
        # switch TO FK
        match(jnts[0], fk_ctrls[0])
        match(jnts[1], fk_ctrls[1])
        match(jnts[2], fk_ctrls[2])
        mc.setAttr(ctrl+'.IK', 0)
        msg = None

    if set_key:
        mc.setKeyframe(ctrl+'.IK', t=mc.currentTime(q=1))
        mc.setKeyframe([c+'.t' for c in key_ctrls], t=mc.currentTime(q=1))
        mc.setKeyframe([c+'.r' for c in key_ctrls], t=mc.currentTime(q=1))

    mc.select(csel)

    if msg:
        mc.inViewMessage( amg='{0} has values on {1}. Match is not exact!'.format(fk_ctrls[1], msg), pos='midCenter', fade=True )

def switch_bipedleg_IK(ctrl, set_key=False):

    csel = mc.ls(sl=1)

    if 'leg_IK_switch' not in ctrl:
        mc.warning('Select a bipedLeg IK switch control!')
        return

    # declare nodes (this has to be part specific)
    prefix = ctrl.split('leg_IK_switch')[0]
    ik_ctrl = prefix+'leg_IK_CTL'
    pv_ctrl = prefix+'leg_PV_CTL'
    toe_ctrl = prefix+'toe_IK_CTL'

    ik_ctrl_snap = prefix+'leg_IK_CTL_SNAPTO'
    pv_ctrl_snap = prefix+'leg_PV_CTL_SNAPTO'
    toe_trl_snap = prefix+'toe_IK_CTL_SNAPTO'
    leg_end_snap = prefix+'legEnd_FK_CTL_SNAPTO'

    fk_ctrls = [prefix+'upLeg_FK_CTL', prefix+'loLeg_FK_CTL', prefix+'legEnd_FK_CTL', prefix+'toe_FK_CTL']
    jnts = [prefix+'upLeg_IK_JNT', prefix+'loLeg_IK_JNT', prefix+'ankle_JNT', prefix+'ball_JNT']

    xtras = mc.ls([prefix+'heel_CTL',
                 prefix+'innerBall_CTL',
                 prefix+'toeTip_CTL',
                 prefix+'toe_IK_CTL',
                 prefix+'reverseBall_CTL',
                 prefix+'outterBall_CTL',
                 prefix+'ankleOffset_CTL'])

    attrs = ['roll',
             'sideRoll',
             'toeTipPivot',
             'ballPivot',
             'heelPivot',
             'heelLift',
             'ballLift',
             'toeTipLift',
             'toeLift']

    current_val = mc.getAttr(ctrl+'.IK')

    if not mc.objExists(ik_ctrl_snap) or not mc.objExists(pv_ctrl_snap):
        mc.warning('This rig needs to be rebuilt to allow FK IK matching!')
        return

    key_ctrls = [ik_ctrl, pv_ctrl, toe_ctrl]+fk_ctrls+xtras

    if set_key:
        mc.setKeyframe(ctrl+'.IK', t=mc.currentTime(q=1)-1)
        mc.setKeyframe([c+'.t' for c in key_ctrls], t=mc.currentTime(q=1)-1)
        mc.setKeyframe([c+'.r' for c in key_ctrls], t=mc.currentTime(q=1)-1)

    if current_val < 0.5:
        # switch TO IK

        for a in attrs:
            mc.setAttr(ik_ctrl+'.'+a, 0)

        if xtras:
            mc.xform(xtras, a=1, t=[0,0,0], ro=[0,0,0])

        match(ik_ctrl_snap, ik_ctrl)
        match(pv_ctrl_snap, pv_ctrl)

        if mc.objExists(toe_trl_snap) and mc.objExists(toe_ctrl):
            match(toe_trl_snap, toe_ctrl)

        mc.setAttr(ctrl+'.IK', 1)

        msg = None
        if round(mc.getAttr(fk_ctrls[1]+'.rx'), 2) and round(mc.getAttr(fk_ctrls[1]+'.rx'), 2):
            msg = '<hl>rotateX</hl> and <hl>rotateZ</hl>'
        elif round(mc.getAttr(fk_ctrls[1]+'.rx'), 2):
            msg = '<hl>rotateX</hl>'
        elif round(mc.getAttr(fk_ctrls[1]+'.rz'), 2):
            msg = '<hl>rotateZ</hl>'

        if msg:
            mc.inViewMessage( amg='{0} has values on {1}. Match is not exact!'.format(fk_ctrls[1], msg), pos='midCenter', fade=True )

    else:
        # switch TO FK

        match(jnts[0], fk_ctrls[0])
        match(jnts[1], fk_ctrls[1])
        match(leg_end_snap, fk_ctrls[2])

        if mc.objExists(jnts[3]) and mc.objExists(fk_ctrls[3]):
            match(jnts[3], fk_ctrls[3])

        mc.setAttr(ctrl+'.IK', 0)
        mc.select(csel)

    if set_key:
        mc.setKeyframe(ctrl+'.IK', t=mc.currentTime(q=1))
        mc.setKeyframe([c+'.t' for c in key_ctrls], t=mc.currentTime(q=1))
        mc.setKeyframe([c+'.r' for c in key_ctrls], t=mc.currentTime(q=1))


mel_cmd = '''

    global int $rigAnimDagMenuIsEnabled;
    global int $rigAnimDagSetKeysWhenSwitching;
    global int $failed;

    $rigAnimDagMenuIsEnabled = 0;
    $rigAnimDagSetKeysWhenSwitching = 1;
    $failed = -1;

    global proc buildObjectMenuItemsNow( string $parentName)
    {
        if (`exists DRUseModelingToolkitMM` && DRUseModelingToolkitMM($parentName)){
            return;
        }

        global int $gIsMarkingMenuOn;
        global int $rigAnimDagMenuIsEnabled;
        global int $rigAnimDagSetKeysWhenSwitching;
        global int $failed;

        if (`popupMenu -e -exists $parentName`) {
            popupMenu -e -deleteAllItems $parentName;
            if (`popupMenu -q -mm $parentName` != $gIsMarkingMenuOn) {
                popupMenu -e -mm $gIsMarkingMenuOn $parentName;
            }

            int $editMode = 0;
            string $currentContext = `currentCtx`;
            if (`contextInfo -exists $currentContext`) {
                string $ctx = `contextInfo -c $currentContext`;
                if ($ctx == "manipMove") {
                    $editMode = `manipMoveContext -q -editPivotMode Move`;
                } else if ($ctx == "manipScale") {
                    $editMode = `manipScaleContext -q -editPivotMode Scale`;
                } else if ($ctx == "manipRotate") {
                    $editMode = `manipRotateContext -q -editPivotMode Rotate`;
                } else if ($ctx == "sculptMeshCache") {
                    setParent -menu $parentName;
                    sculptMeshCacheOptionsPopup();
                    return;
                } else if ($ctx == "polyCutUV") {
                    setParent -menu $parentName;
                    polyCutUVOptionsPopup();
                    return;
                }
                else if(contextXGenToolsMM($parentName))
                {
                    return;
                }
            }

            if ($editMode) {
                setParent -menu $parentName;

                menuItem
                    -label (uiRes("m_buildObjectMenuItemsNow.kPinComponentPivot"))
                    -checkBox `manipPivot -q -pin`
                    -radialPosition "N"
                    -command ("setTRSPinPivot #1");

                menuItem
                    -label (uiRes("m_buildObjectMenuItemsNow.kResetPivot"))
                    -radialPosition "S"
                    -command ("manipPivotReset true true");

                menuItem
                    -label (uiRes("m_buildObjectMenuItemsNow.kSnapPivotOrientation"))
                    -checkBox `manipPivot -q -snapOri`
                    -radialPosition "NW"
                    -command ("setTRSSnapPivotOri #1");

                menuItem
                    -label (uiRes("m_buildObjectMenuItemsNow.kSnapPivotPosition"))
                    -checkBox `manipPivot -q -snapPos`
                    -radialPosition "NE"
                    -command ("setTRSSnapPivotPos #1");

                menuItem
                    -label (uiRes("m_buildObjectMenuItemsNow.kResetPivotOrientation"))
                    -radialPosition "SW"
                    -command ("manipPivotReset false true");

                menuItem
                    -label (uiRes("m_buildObjectMenuItemsNow.kResetPivotPosition"))
                    -radialPosition "SE"
                    -command ("manipPivotReset true false");

                menuItem
                    -label (uiRes("m_buildObjectMenuItemsNow.kShowPivotOrientationHandle"))
                    -checkBox `optionVar -q manipShowPivotRotateHandle`
                    -radialPosition "W"
                    -command ("setTRSPivotOriHandle #1");

                menuItem
                    -label (uiRes("m_buildObjectMenuItemsNow.kExitPivotMode"))
                    -radialPosition "E"
                    -command ("ctxEditMode");

                setParent ..;
            } else {
                if (!`dagObjectHit -mn $parentName`) {
                    // Nothing was hit - check selection/hilight list...
                    string $leadObject[] = `ls -sl -tail 1 -typ transform -typ shape`;
                    if (size($leadObject) == 0) {
                        $leadObject = `ls -hl -tail 1 -typ transform -typ shape`;
                    }
                    if (size($leadObject) > 0) {
                        dagMenuProc($parentName, $leadObject[0]);
                    } else {
                        if (`modelingTookitActive` && (`nexCtx -rmbComplete -q`) ) {
                            ctxCompletion;
                            return;
                        }
                        setParent -menu $parentName;

                        menuItem
                            -version "2014"
                            -label (uiRes("m_buildObjectMenuItemsNow.kSelectAll"))
                            -radialPosition "S"
                            -command ("SelectAll");

                        menuItem
                            -label (uiRes("m_buildObjectMenuItemsNow.kCompleteTool"))
                            -radialPosition "N"
                            -command ("CompleteCurrentTool");

                        setParent ..;
                    }
                }
            }
        } else {
            warning (uiRes("m_buildObjectMenuItemsNow.kParentWarn"));
        }

        //////////////////////////////////////////////////////////////////////////////////////////////////////
        //  The code below creats the cvustom marking menu for animation ctrls

        if ($failed == -1)
            $failed = catchQuiet(`python("animMarkingMenu")`);

        if ($failed == 1)
            return;

        menuItem -d 1;
        menuItem
                -checkBox $rigAnimDagMenuIsEnabled
                -l "Enable Anim Marking Menu"
                -c "toggleAnimDagMenu";

        if ($rigAnimDagMenuIsEnabled == 0){
            return;
        }

        string $nodes[] = `ls "*:rig_GRP" "rig_GRP"`;
        if (`size $nodes` == 0)
            return;

        string $selection[] = `ls -sl`;
        if (`size $selection` < 1 ){
            return;
        }

        string $ctrl = $selection[`size $selection`-1];

        // Create custom control dag menu
        if (`objExists ($ctrl+".animControl")`){

            // create ctrl basic menu
            popupMenu -e -dai $parentName;
            setParent -menu $parentName;
            menuItem -l "Current Anim Control" -bld 1 -en 0;
            if (`size $selection` > 1 ){
                menuItem -l ($ctrl+" . . .");
            }
            else{
                menuItem -l ($ctrl);
            }

            // create selection menu
            string $allSets[] = getSelectionSets();
            if (`size $allSets` > 0){
                menuItem -d 1;
                menuItem -l "Selection Sets" -en 0 -bld 1;

                for ($i=0; $i < `size $allSets`; $i++){

                    string $label = "Select "+`substitute "_control_SEL" $allSets[$i] ""`+" Controls";

                    menuItem
                        -l ($label)
                        -c ("select "+$allSets[$i]);

                    menuItem -optionBox true -c ("select -add "+$allSets[$i]);
                }
            }

            if (`objExists ($selection[0]+".IK")` && `objExists ($selection[0]+".matchFunction")`){
                menuItem -d 1;
                menuItem -l "FK / IK Switching" -en 0 -bld 1;

                menuItem -l ("Toggle && Snap FK / IK") -c ("toggleCtrlIK");
                setParent -menu $parentName;

            }

            // create spaces menu
            if (`objExists ($selection[0]+".space")`){
                menuItem -d 1;
                menuItem -l "Snap Space" -en 0 -bld 1;

                string $enumStr = `addAttr -q  -en ($ctrl+".space")`;
                string $tokens[];
                tokenize $enumStr ":" $tokens;

                for ($i=0; $i < `size $tokens`; $i++){
                    menuItem
                        -l ($tokens[$i]+" Space")
                        -c ("snapCtrlSpace space "+$i);

                    setParent -menu $parentName;
                }
            }

            else if (`objExists ($selection[0]+".transSpace")`){
                menuItem -d 1;
                menuItem -l "Snap Translate Space" -en 0 -bld 1;

                string $enumStr = `addAttr -q  -en ($ctrl+".transSpace")`;
                string $tokens[];
                tokenize $enumStr ":" $tokens;

                for ($i=0; $i < `size $tokens`; $i++){
                    menuItem
                        -l ($tokens[$i]+" Space")
                        -c ("snapCtrlSpace transSpace "+$i);

                    setParent -menu $parentName;
                }

                if (`objExists ($selection[0]+".orientSpace")`){
                    menuItem -d 1;
                    menuItem -l "Snap Rotate Space" -en 0 -bld 1;

                    string $enumStr = `addAttr -q  -en ($ctrl+".orientSpace")`;
                    string $tokens[];
                    tokenize $enumStr ":" $tokens;

                    for ($i=0; $i < `size $tokens`; $i++){
                        menuItem
                            -l ($tokens[$i]+" Space")
                            -c ("snapCtrlSpace orientSpace "+$i);

                        setParent -menu $parentName;
                    }
                }
            }

            menuItem -d 1;
            menuItem -l "Marking Menu Settings" -en 0 -bld 1;

            menuItem
                -checkBox $rigAnimDagSetKeysWhenSwitching
                -l "Set Keys When Switching"
                -c "toggleSetKeyframe";

            menuItem
                -checkBox $rigAnimDagMenuIsEnabled
                -l "Disable Anim Marking Menu"
                -c "toggleAnimDagMenu";
        }
    }

    global proc snapCtrlSpace(string $attr, int $newSpaceIdx){
        // Snap space of selected ctrl to new ctrl//

        global int $rigAnimDagSetKeysWhenSwitching;
        int $setKeyframe = $rigAnimDagSetKeysWhenSwitching;

        string $arg = "animMarkingMenu.switch_space(space_idx="+$newSpaceIdx+", space_attr='"+$attr+"', set_key="+$setKeyframe+")";
        python($arg);

    }

    global proc toggleCtrlIK(){
        // Snap space of selected ctrl to new ctrl//

        global int $rigAnimDagSetKeysWhenSwitching;
        int $setKeyframe = $rigAnimDagSetKeysWhenSwitching;

        string $arg = "animMarkingMenu.switch_IK(set_key="+$setKeyframe+")";
        python($arg);

    }

    global proc string[] getSelectionSets(){
        // Get the selection sets a node is in

        string $allSets[];

        string $selection[] = `ls -sl`;
        if (`size $selection` < 1 ){
            return $allSets;
        }

        for ($i=0; $i < `size $selection`; $i++){
            string $ctrl = $selection[$i];
            string $sets[] = `listSets -o $ctrl`;

            if (`size $sets` > 0){
                appendStringArray($allSets, $sets, `size $sets`);
            }
        }

        string $arg = "[";
        for ($i=0; $i < `size $allSets`; $i++){
            $arg += "'"+$allSets[$i]+"', ";
        }
        $arg += "]";
        $allSets = python("list(set("+$arg+"))");

        return $allSets;
    }

    global proc toggleSetKeyframe(){
        //Toggles global int variable to enable setting keys when switching

        global int $rigAnimDagSetKeysWhenSwitching;

        if ($rigAnimDagSetKeysWhenSwitching == 0){
            $rigAnimDagSetKeysWhenSwitching = 1;
        }

        else{
            $rigAnimDagSetKeysWhenSwitching = 0;
        }
    }

    global proc toggleAnimDagMenu(){
        //Toggles global int variable to enable setting keys when switching

        global int $rigAnimDagMenuIsEnabled;

        if ($rigAnimDagMenuIsEnabled == 0){
            $rigAnimDagMenuIsEnabled = 1;
        }

        else{
            $rigAnimDagMenuIsEnabled = 0;
        }
    }

'''

mm.eval(mel_cmd)
