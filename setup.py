from setuptools import setup

APP = ['main.pyw']  # Dein Hauptskript
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'assets/icon.icns',  # optional
    'packages': [],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
