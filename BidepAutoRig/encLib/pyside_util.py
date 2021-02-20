"""

   Original code downloaded from Nicholas-Silveria.blogspot.com

   updated 5/31/2017 by Jennifer Hachigian to work with Maya 2017
   updated 11/05/2018 by Jennifer Hachigian to work with Mango + Legacy Render Layers (now PySide2-only)
"""

import xml.etree.ElementTree as xml
from cStringIO import StringIO
try:
    import pymel.core as pm
    from PySide2 import QtCore, QtGui, QtWidgets
    import pyside2uic as uic
    import shiboken2 as shi
except ImportError:
    pass


'''
========================================================================
---->  Parse .ui File and Return PySide Class  <----
========================================================================
'''


def get_pyside_class(ui_file):
    """
    Pablo Winant
    """
    parsed = xml.parse(ui_file)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text
   
    with open(ui_file, 'r') as f:
        o = StringIO()
        frame = {}

        uic.compileUi(f, o, indent = 0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame

        # Fetch the base_class and form class based on their type in the xml from designer
        form_class = frame['Ui_{0}'.format(form_class)]
        base_class = eval('QtWidgets.{0}'.format(widget_class))

    return form_class, base_class


'''
========================================================================
---->  Nathan Horne's wrapinstance  <----
========================================================================
'''


def wrap_instance(ptr, base=None):
    """
    Nathan Horne with modifications from Jennifer Hachigian
    """
    if ptr is None:
        return None

    ptr = long(ptr)  # Ensure type
    if 'shiboken' in globals() or 'shiboken2' in globals():
        if base is None:
            q_obj = shi.wrapInstance(long(ptr), QtCore.QObject)
            meta_obj = q_obj.metaObject()
            cls = meta_obj.className()
            super_cls = meta_obj.superClass().className()
            if hasattr(QtGui, cls):
                base = getattr(QtGui, cls)

            elif hasattr(QtGui, super_cls):
                base = getattr(QtGui, super_cls)

            else:
                base = QtGui.QWidget

        return shi.wrapInstance(long(ptr), base)

    elif 'sip' in globals():
        base = QtCore.QObject

        return sip.wrapinstance(long(ptr), base)

    else:
        return None


'''
========================================================================
---->  Get Maya Window  <----
========================================================================
'''


def get_maya_window():
    """
    Code from Fredrik Averpil's "boilerplate.py" on GitHub.

    :return: Maya's main window
    """
    for obj in QtWidgets.QApplication.topLevelWidgets():
        if obj.objectName() == 'MayaWindow':
            return obj
    if not pm.about(batch=True):
        """ this is being run on maya.exe and NOT mayaBatch.exe """
        raise RuntimeError('Could not find MayaWindow instance.')
    else:
        return None
