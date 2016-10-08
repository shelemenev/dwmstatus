try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'dwmstatus',
    'version': '0.1',
    'packages': ['dwmstatus'],
    'scripts': [],
    'name': 'dwmstatus',
    'entry_points': {
        'console_scripts': [
            'dwmstatus = dwmstatus.__main__:main'
        ]
    },
}

setup(**config)
