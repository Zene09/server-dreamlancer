"""Sets up the package"""

#!/usr/bin/env python
 # -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE.md') as f:
    LICENSE = f.read()

setup(
    name='dreamlancer',
    version='0.1.0',
    description='Dreamlancer standalone API',
    long_description=README,
    author='Kyle',
    author_email='ph_kyle104@yahoo.com',
    url='https://github.com/Zene09/server-dreamlancer',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
