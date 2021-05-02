# -*- coding: utf-8 -*-
# ______________   ______   __
# |____/|____|| \  ||   \\_/
# |R  \_|A   ||N \_||D__/ |Y
#
#    @..@    古池や
#   (----)    蛙飛び込む
#  ( >__< )    水の音
#
# ( ! ) 2021 Giovanni Squillero. Public Domain.
# Project page: https://github.com/squillero/randy

__all__ = [
    'seed', 'boolean', 'choice', 'randint', 'random', 'shuffle', 'shuffled', 'sigma_choice', 'sigma_random',
    'weighted_choice'
]

import logging
from typing import Optional, Any
import numpy as np

from .core import Randy

try:
    # Ok, I may admit it's a little bit paranoid...
    _default
    assert False, f"Panic: The default random generator has already be initialized: {_default!r}"
except NameError:
    _default = Randy(None, croak=False)  # None, but w/o warning
    logging.debug(f"Initialized Randy: {_default!r}")


def seed(new_seed: Optional[Any] = None) -> None:
    global _default
    _default = np.random.default_rng(new_seed)


def boolean(*args, **kwargs):
    """Call boolean from the default random generator."""
    return _default.boolean(*args, **kwargs)


def random(*args, **kwargs):
    """Call random from the default random generator."""
    return _default.random(*args, **kwargs)


def sigma_random(*args, **kwargs):
    """Call sigma_random from the default random generator."""
    return _default.sigma_random(*args, **kwargs)


def weighted_choice(*args, **kwargs):
    """Call weighted_choice from the default random generator."""
    return _default.weighted_choice(*args, **kwargs)


def sigma_choice(*args, **kwargs):
    """Call sigma_choice from the default random generator."""
    return _default.sigma_choice(*args, **kwargs)


def choice(*args, **kwargs):
    """Call choice from the default random generator."""
    return _default.choice(*args, **kwargs)


def randint(*args, **kwargs):
    """Call randint from the default random generator."""
    return _default.randint(*args, **kwargs)


def shuffle(*args, **kwargs):
    """Call shuffle from the default random generator."""
    return _default.shuffle(*args, **kwargs)


def shuffled(*args, **kwargs):
    """Call shuffled from the default random generator."""
    return _default.shuffled(*args, **kwargs)
