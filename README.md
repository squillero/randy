![LANGUAGE](https://img.shields.io/badge/language-python3-blue)
[![LICENSE](https://img.shields.io/github/license/squillero/randy)](LICENSE)
![SIZE](https://img.shields.io/github/languages/code-size/squillero/randy)
![RELEASE](https://img.shields.io/github/v/release/squillero/randy?include_prereleases)
[![DOI](https://zenodo.org/badge/354226427.svg)](https://zenodo.org/badge/latestdoi/354226427)


`randy`
=======

> **Notez bien**: Not to be confused with Francis Horsman's *randy* @ [https://pypi.org/project/randy/](https://pypi.org/project/randy/)

A fiddling wrapper; its main is to allow my EA applications to use a private, separate random generator, guaranteeing the reproducibility of the results — plus a handful of functions I found useful over the years.



Strength-based functions are straightforwardly based on [truncated normal distributions](https://en.wikipedia.org/wiki/Truncated_normal_distribution), see the SciPy docs on [scipy.stats.truncnorm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncnorm.html).

I guess these files will never be uploaded to PyPI: install locally with something like

```shell
$ git clone https://github.com/squillero/randy
$ cd randy
$ python3 setup.py install
```

or simply move the sub-directory `randy` inside your project.

Have fun. And wear a mask 😷.

### Randy is Public Domain  
The code of `randy` have been dedicated to the [public domain](https://en.wikipedia.org/wiki/Public-domain_software) by the [Author](https://github.com/squillero): anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means. 

See [LICENSE](/LICENSE) for more details.
