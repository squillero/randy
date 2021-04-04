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

from typing import Optional, Sequence, Any, Collection, List, Tuple
import warnings
import math
import random
import numpy as np
from scipy.stats import truncnorm

class Randy:
    """Internal random engine to guarantee reproducibility."""

    SMALL_NUMBER = 1e-9

    def __init__(self, seed: Optional = 42) -> None:
        self._generator = np.random.default_rng(seed)
        self._calls = 0

    def seed(self, seed: Any) -> None:
        """Force a seed value to the internal generator"""
        warnings.warn("Setting a seed is deprecated. Create a new RandomWrapper instead.", warnings.DeprecationWarning)
        self._generator = np.random.default_rng(seed)
        self._calls = 0

    @staticmethod
    def _strength_to_sigma(strength: float):
        """Stretches [0,1] on [SMALL_NUMBER, 20.723265864228342]."""

        assert 0 <= strength <= 1, "Invalid sigma (must be [0, 1])"
        x = (1-strength) / 2 + .5
        x = min(x, 1-Randy.SMALL_NUMBER)

        val = math.log(x / (1 - x))
        if math.isclose(val, 0): val = Randy.SMALL_NUMBER
        return val

    def sigma_random(self, a: Optional[float] = None, b: Optional[float] = None, loc: Optional[float] = None, strength: Optional[float] = None):
        """Returns a random value in [a, b] biased toward loc with a strength between 0 and 1."""

        std = Randy._strength_to_sigma(strength)
        clip_a, clip_b = (a - loc) / std, (b - loc) / std
        return truncnorm.rvs(clip_a, clip_b, loc=loc, scale=std, random_state=self._generator)
