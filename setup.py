"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['fblikers.py']
DATA_FILES = ['fblikers.icns', 'bin/geckodriver']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'fblikers.icns',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
