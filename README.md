![LANGUAGE](https://img.shields.io/badge/language-python3-blue)
[![LICENSE](https://img.shields.io/github/license/squillero/randy)](LICENSE)
![SIZE](https://img.shields.io/github/languages/code-size/squillero/randy)
![RELEASE](https://img.shields.io/github/v/release/squillero/randy?include_prereleases)
[![DOI](https://zenodo.org/badge/354226427.svg)](https://zenodo.org/badge/latestdoi/354226427)

RANDY
=====

> **Notez bien**: Not to be confused with Francis Horsman's *randy* @ [https://pypi.org/project/randy/](https://pypi.org/project/randy/)

A fiddling wrapper over NumPI's random package. The main purpose of *Randy* is to allow my EA applications to use a private, separate random generator, guaranteeing the reproducibility of the results. Plus a handful of functions I found useful over the years.

Strength-based functions are straightforwardly based on [truncated normal distributions](https://en.wikipedia.org/wiki/Truncated_normal_distribution), see the SciPy docs on [scipy.stats.truncnorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncnorm.html).

I guess these files will never be uploaded to PyPI: install locally with something like

```shell
$ git clone https://github.com/squillero/randy
$ cd randyc
$ python3 setup.py install
```

or simply move the sub-directory `randy` inside your project.

Have fun. And wear a mask 😷.

### License

Copyright © 2021 Giovanni Squillero  
Randy is [free and open-source software](https://en.wikipedia.org/wiki/Free_and_open-source_software), and it is distributed under a permissive [MIT License](https://tldrlegal.com/license/mit-license).
