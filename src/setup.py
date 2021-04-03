# -*- coding: utf-8 -*-
#  , __
# /|/  \                  |
#  |___/  __,   _  _    __|
#  | \   /  |  / |/ |  /  |  |   |
#  |  \_/\_/|_/  |  |_/\_/|_/ \_/|/
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /| ~
#                               \|
#
# Copyright (c) 2021 Giovanni Squillero.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

# INSTALL LOCALLY WITH
# $ pip3 install -e src

import setuptools

with open('../README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r', encoding='utf-8') as fh:
    requirements = [r for r in fh.readlines() if not any(o in r for o in OPTIONAL)]

setuptools.setup(
    name="randy",
    version="0.1",
    author="Giovanni Squillero",
    author_email="squillero@polito.it",
    license="MIT",
    description="A fiddling wrapper over the standard random",
    long_description=long_description,
    #long_description_content_type="text/x-rst",
    long_description_content_type='text/markdown',
    url="https://squillero.github.io/microgp4/",
    project_urls={
        'Bug Tracker': "https://github.com/squillero/microgp4/issues",
        'Documentation': "https://microgp4.readthedocs.io/en/pre-alpha/",
        'Source Code': "https://github.com/squillero/microgp4/tree/pre-alpha",
    },
    keywords="optimization evolutionary-algorithm computational-intelligence",
    packages=setuptools.find_packages(),
    package_data={'': ['requirements.txt', 'README.md']},
    data_files=[('.', ['requirements.txt', 'README.md'])],
    classifiers=[
        "Programming Language :: Python :: 3", "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha", "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=requirements,
)
