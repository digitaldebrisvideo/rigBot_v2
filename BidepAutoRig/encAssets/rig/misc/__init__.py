"""
    This __init__.py is written so that users do NOT have to restart Maya to reload the functions of this module.
    This way the code can be updated without interrupting artists' work.
"""

import misc
reload(misc)

mirror_left_to_right = misc.mirror_left_to_right
mirror_right_to_left = misc.mirror_right_to_left
select_bind = misc.select_bind
fix_joints_orient = misc.fix_joints_orient
