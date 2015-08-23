try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'lol-clarity',
    'description': 'Library to read/write Clarity UI binary format from Leauge of Legends',
    'long_description': '''This library is capable of reading/writing to a binary format
        used by Leauges of Legends to define the UI since version 5.14.
        ''',
    'license': 'MIT',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    'author': 'Tom Najdek',
    'url': 'https://github.com/tnajdek/lol-clarity',
    'author_email': 'tom@doppnet.com',
    'version': '0.1.3',
    'packages': ['clarity'],
    'install_requires': ['future']
}

setup(**config)
