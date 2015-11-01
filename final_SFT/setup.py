# setup.py
from distutils.filelist import findall
from distutils.core import setup
import py2exe
import os
import matplotlib
matplotlibdatadir = matplotlib.get_data_path()
matplotlibdata = findall(matplotlibdatadir)
matplotlibdata_files = []
for f in matplotlibdata:
       dirname = os.path.join('matplotlibdata', f[len(matplotlibdatadir)+1:])
       matplotlibdata_files.append((os.path.split(dirname)[0], [f]))
   
setup(
zipfile='lib/library.zip',
    options={
        'py2exe': {
            'includes': ['zmq.backend.cython'],
            'excludes': ['zmq.libzmq','_gtkagg', '_tkagg'],
            'dll_excludes': ['libzmq.pyd'],
			'packages' : ['matplotlib', 'pytz'],
        }
    },
console=['win_Login.py']
)

 