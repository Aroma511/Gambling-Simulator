from setuptools import setup

APP = ['Gambling_v4.1.pyw']  # dein Hauptskript
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': None,   # hier optional dein Icon: 'assets/icon.icns'
    'packages': [],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
