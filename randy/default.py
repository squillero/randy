# -*- coding: utf-8 -*-
# ______________   ________   __
# |____/|____|| \  ||    \ \_/
# |R  \_|A   ||N \_||D___/  |Y
#
#    @..@    古池や
#   (----)    蛙飛び込む
#  ( >__< )    水の音
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

__all__ = ['boolean', 'choice', 'random', 'sigma_choice', 'sigma_random', 'randint', 'shuffle']

import logging
from .core import Randy

try:
    # Ok, I may admit that that's a little bit paranoid...
    __the_ram
    assert False, f"Panik: Randy the Ram has already be initialized: {__the_ram!r}"
except NameError:
    __the_ram = Randy('None')   # 'None' is like None, but w/o warning
    logging.debug(f"Initialized Randy the Ram: {__the_ram!r}")


def boolean(*args, **kwargs):
    """Call boolean with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.boolean(*args, **kwargs)


def random(*args, **kwargs):
    """Call random with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.random(*args, **kwargs)


def sigma_random(*args, **kwargs):
    """Call sigma_random with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.sigma_random(*args, **kwargs)


def choice(*args, **kwargs):
    """Call choice with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.choice(*args, **kwargs)


def sigma_choice(*args, **kwargs):
    """Call sigma_choice with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.sigma_choice(*args, **kwargs)


def randint(*args, **kwargs):
    """Call randint with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.randint(*args, **kwargs)


def shuffle(*args, **kwargs):
    """Call shuffle with the default random generator."""
    logging.debug(f"Using the default Randy the Ram (ie. {__the_ram!r})")
    return __the_ram.shuffle(*args, **kwargs)
