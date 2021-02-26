
import os
import site

try:
    import Qt

except:
    QTPY_PATH = os.path.abspath(os.path.dirname(__file__)).replace('gui','vendor').replace('\\','/')
    site.addsitedir(QTPY_PATH)
    print 'Using Qt.py from rigBot: '+QTPY_PATH