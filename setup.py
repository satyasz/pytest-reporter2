#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-reporter2',
    use_scm_version=True,
    author='Satya S',
    author_email='satyasz100@gmail.com',
    maintainer='Satya S',
    maintainer_email='satyasz100@gmail.com',
    license='MIT',
    url='https://github.com/satyasz/pytest-reporter2',
    description='Generate Pytest reports with templates',
    long_description=read('README.rst'),
    packages=find_packages(),
    python_requires='>=3.5',
    setup_requires=['setuptools_scm'],
    install_requires=[
        'pytest',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'reporter = pytest_reporter.plugin',
        ],
    },
)
