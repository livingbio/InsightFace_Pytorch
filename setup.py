#!/usr/bin/env python

"""Setup for labeler."""

from setuptools import find_packages, setup

setup(
    name='insight-face-pytorch',
    setup_requires=['setuptools_scm'],
    version='0.0.8',
    packages=find_packages(),
    zip_safe=False,
)
