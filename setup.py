from setuptools import setup
from distutils import sysconfig
import os

LIB_PATH = sysconfig.get_python_lib()
VERSION = '1.0'

setup(name='functools-total-ordering-monkeypatch',
      version='1.0',
      install_requires=['total-ordering', ],
      data_files=[(os.path.join(LIB_PATH), ['functools_total_ordering_monkeypatch-%s.pth' % (VERSION)])],
      )

