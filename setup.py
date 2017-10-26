'''
File: setup.py
Description: Setup file for the plugin server
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 26/10/2017
'''
from setuptools import setup, find_packages

setup(
    name='plugin_server',
    version='0.0.1',
    packages=find_packages(exclude=['docs', 'tests', 'temp'])
)
