#!/usr/bin/env python

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
	name='moshpit',
	description='A wrapper for mosh.  Save hosts and connect to them by nickname.',
    version='0.1',
    author='A.J. May',
    url='http://moshpit.aj7may.com',
    packages=find_packages(),
    requires=['SQLAlchemy(>0.8.0)'],
    install_requires=['SQLAlchemy>0.8.0'],
    scripts=['moshpit/moshpit.py'],
    license="Creative Commons Attribution-ShareAlike 3.0 Unported License",
    entry_points={
    	'console_scripts': ['pit = moshpit.moshpit:main']
    },
)