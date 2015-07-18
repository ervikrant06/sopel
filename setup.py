#!/usr/bin/env python
# coding=utf8
from __future__ import unicode_literals, print_function

from willie import __version__
import sys

try:
    from setuptools import setup
except ImportError:
    print(
        'You do not have setuptools, and can not install Willie. The easiest '
        'way to fix this is to install pip by following the instructions at '
        'http://pip.readthedocs.org/en/latest/installing.html\n'
        'Alternately, you can run willie without installing it by running '
        '"python willie.py"',
        file=sys.stderr,
    )
    sys.exit(1)

try:
    import lxml  # NOQA
except ImportError:
    print(
        '----- WARNING ----- SERIOUSLY, READ THIS ----- I MEAN IT -----\n'
        'You do not have lxml installed. This installer will attempt to '
        'install it, but it frequently fails. Please follow the instructions '
        'at http://lxml.de/installation.html if installation does not succeed.',
        file=sys.stderr,
    )

if sys.version_info < (2, 7) or (
        sys.version_info[0] > 3 and sys.version_info < (3, 3)):
    # Maybe not the cleanest or best way to do this, but I'm tired of answering
    # this fucking question, and if you get here you should go RTGDMFM.
    raise ImportError('Willie requires Python 2.7+ or 3.3+.')


def read_reqs(path):
    with open(path, 'r') as fil:
        return list(fil.readlines())

requires = read_reqs('requirements.txt')
if sys.version_info[0] < 3:
    requires.append('backports.ssl_match_hostname')
dev_requires = requires + read_reqs('dev-requirements.txt')

setup(
    name='willie',
    version=__version__,
    description='Simple and extendible IRC bot',
    author='Edward Powell',
    author_email='powell.518@gmail.com',
    url='http://willie.dftba.net/',
    long_description=(
        "Willie is a simple, extendible, easy-to-use IRC Utility bot, written "
        "in Python. It's designed to be easy to use, easy to run, and easy to "
        "make new features for."
    ),
    # Distutils is shit, and doesn't check if it's a list of basestring
    # but instead requires str.
    packages=[str('willie'), str('willie.modules'),
              str('willie.config'), str('willie.tools')],
    license='Eiffel Forum License, version 2',
    platforms='Linux x86, x86-64',
    requires=requires,
    install_requires=requires,
    entry_points={'console_scripts': ['willie = willie.run_script:main']},
)
