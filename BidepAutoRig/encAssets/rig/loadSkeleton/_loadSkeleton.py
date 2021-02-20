import pymel.core as pm
import os

skeleton_folder = os.path.dirname(__file__)
skeleton_path = os.path.join(skeleton_folder, "_skeleton.mb")


def loadSkeleton():
    if not pm.objExists('root_Mid_jnt'):
        pm.importFile(skeleton_path)
    else:
        msg = "Skeleton already loaded into this scene."
        print msg
        pm.confirmDialog(title="Skeleton already exists.", message=msg)
