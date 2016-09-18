#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='hernrup-se-portal',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'hernrup_se_core>=0.0.1',
    ],
)
