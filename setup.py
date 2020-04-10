#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pandas']

setup_requirements = []

test_requirements = []

setup(
    author="Boris Bauermeister",
    author_email='Boris.Bauermeister@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A simple python Avanza data grabber",
    install_requires=requirements,
    license="ISC license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyvanza',
    #name='pyvanza',
    ##packages=find_packages(include=['.pyvanca.module']),

    #package_dir={'': 'pyvanza'},
    #packages=find_packages(where='pyvanza'),

    name='pyvanza',
    packages=find_packages(include=['pyvanza', 'pyvanza.module']),

    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/XeBoris/pyvanza',
    version='0.1.0',
    zip_safe=False,
    entry_points={
            'console_scripts': [
                'pyvanza = pyvanza.pyvanza:pyvanza_standalone'
                ]
            },
)
