"""
    This __init__.py is written so that users do NOT have to restart Maya to reload the functions of this module.
    This way the code can be updated without interrupting artists' work.
"""

import _loadSkeleton
reload(_loadSkeleton)

launch = _loadSkeleton.loadSkeleton
