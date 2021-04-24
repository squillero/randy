# -*- coding: utf-8 -*-
# ______________   ________   __
# |____/|____|| \  ||    \ \_/
# |R  \_|A   ||N \_||D___/  |Y
#
#    @..@    古池や
#   (----)    蛙飛び込む
#  ( >__< )    水の音
#
# ( ! ) 2021 Giovanni Squillero. CC0 Public Domain.
# Project page: https://github.com/squillero/randy

# INSTALL LOCALLY WITH
# $ pip3 install -e src

import setuptools

OPTIONAL = []

with open('README.md', 'r', encoding='utf-8') as fh:
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
