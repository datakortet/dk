#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Datakortet Javascript package, dk.js.
"""

classifiers = """\
Development Status :: 3 - Alpha
Intended Audience :: Developers
Programming Language :: Python
Programming Language :: Javascript
Topic :: Software Development :: Libraries
"""

import setuptools
from distutils.core import setup

version = eval(open('package.json').read())['version']

setup(
    name='dk',
    version=version,
    requires=[],
    install_requires=[],
    description=__doc__.strip(),
    classifiers=[line for line in classifiers.split('\n') if line],
    long_description=open('pysrc/README.txt').read(),
    license="BSD",
    author='Bjorn Pettersen',
    author_email='bp@datakortet.no',
    #url='https://github.com/thebjorn/dkjs',
    #download_url='https://github.com/thebjorn/dkjs',

    packages=['dk'],
    zip_safe=False,
)
