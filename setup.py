# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pygments',
    version='2.17.0',
    description='Pygments is a syntax highlighting package written in Python.',
    author_email='Georg Brandl <georg@python.org>',
    maintainer='Matthäus G. Chajdas',
    maintainer_email='Georg Brandl <georg@python.org>, Jean Abou Samra <jean@abou-samra.fr>',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
    ],
    extras_require={
        'plugins': [
            'importlib-metadata; python_version < "3.8"',
        ],
        'windows-terminal': [
            'colorama>=0.4.6',
        ],
    },
    entry_points={
        'console_scripts': [
            'pygmentize = pygments.cmdline:main',
        ],
    },
    packages=[
        'pygments',
        'pygments.filters',
        'pygments.formatters',
        'pygments.lexers',
        'pygments.styles',
    ],
)
