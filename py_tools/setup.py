from distutils.core import setup
import py2exe

setup(console=['GUI.py'],
      options={'py2exe': {'packages': ['pytube']}})
