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

from typing import Optional, Sequence, Any
import warnings
import math
import logging
import numpy as np
from scipy.stats import truncnorm


class Randy:
    """Random number generators for EA applications."""

    SMALL_NUMBER = 1e-9

    def __init__(self, seed: Optional[Any] = 42) -> None:
        if seed is None:
            warnings.warn("Initializing Randy with entropy from the OS: results will not be reproducible.", RuntimeWarning, stacklevel=2)
        self._generator = np.random.default_rng(seed)
        self._calls = 0

    def seed(self, seed: Any) -> None:
        """Force a seed value to the internal generator"""
        warnings.warn("Setting a seed is deprecated. Create a new RandomWrapper instead.", DeprecationWarning)
        self._generator = np.random.default_rng(seed)
        self._calls = 0

    def __str__(self) -> str:
        descr = ', '.join(f"{a}={b!r}" for a, b in self._generator.__getstate__().items())
        return f"Randy @ {hex(id(self))} (calls={self._calls}, {descr})"

    def __repr__(self) -> str:
        return f"Randy_{hex(id(self))[2:]}"

    @staticmethod
    def _strength_to_sigma(strength: float):
        """Stretches [0,1] on a standard deviation ]0, 20.8[."""

        assert 0 <= strength <= 1, "Invalid sigma (must be [0, 1])"
        x = strength / 2 + .5
        x = min(x, 1 - Randy.SMALL_NUMBER)

        val = math.log(x / (1 - x))
        if math.isclose(val, 0):
            val = Randy.SMALL_NUMBER
        return val

    def sigma_random(self, a: float, b: float, loc: Optional[float] = None, strength: Optional[float] = None):
        """Returns a value in [a, b] by perturbating loc with a given strength."""

        self._calls += 1
        assert a <= b, "a must precede b"
        assert strength is None or 0 <= strength <= 1, "strength must be in [0, 1]"
        assert (loc is None and strength is None) or (
            loc is not None and
            strength is not None), "loc and strength should be specified together (either both or neither)"
        assert loc is None or a <= loc <= b, "loc must be in [a, b]"

        if strength is None:
            val = self._generator.random()
            val = val * (b - a) + a
        elif strength == 0:
            val = loc
        else:
            std = Randy._strength_to_sigma(strength)
            clip_a, clip_b = (a - loc) / std, (b - loc) / std
            val = truncnorm.rvs(clip_a, clip_b, loc=loc, scale=std, random_state=self._generator)
        return val

    def random(self, a: Optional[float] = 0, b: Optional[float] = 1):
        """Returns a random value in [a, b], default is [0, 1]."""
        return self.sigma_random(a=a, b=b, loc=None, strength=None)

    def sigma_choice(self, seq: Sequence[Any], loc: Optional[int] = None, strength: Optional[float] = None) -> Any:
        """Returns a random element from seq by perturbating index loc with a given strength."""

        self._calls += 1
        assert strength is None or 0 <= strength <= 1, "strength must be in [0, 1]"
        assert (loc is None and strength is None) or (
            loc is not None and
            strength is not None), "loc and strength should be specified together (either both or neither)"
        assert loc is None or 0 <= loc < len(seq), "loc must be a valid index of seq"

        if strength == 1 or strength is None:
            return self._generator.choice(seq)
        elif strength == 0:
            return seq[loc]
        else:
            i = self.sigma_random(0, len(seq)-Randy.SMALL_NUMBER, loc=loc+.5, strength=strength)
            return seq[int(i)]

    def choice(self, seq: Sequence[Any]):
        """Returns a random element from seq"""
        return self.sigma_choice(seq, loc=None, strength=None)

    def boolean(self, p_true: Optional[float] = None, p_false: Optional[float] = None):
        """Returns a boolean value with the given probability."""

        self._calls += 1
        assert p_true is None or p_false is None, "p_true and p_false cannot be both spedified."
        assert p_true is None or 0 <= p_true <= 1, "p_true must be on [0, 1]."
        assert p_false is None or 0 <= p_false <= 1, "p_false must be on [0, 1]."

        if p_true is None and p_false is None:
            p_true = .5
        elif p_true is None and p_false is not None:
            p_true = 1-p_false

        return self._generator.random() < p_true

    def randint(self, a, b):
        """Returns a random integer in [a, b]."""
        assert a <= b, "a must be <= b."
        r = self._generator.random() * (b - a + 1) + a
        return int(r)

    def shuffle(self, seq: Sequence[Any]) -> None:
        self._generator.shuffle(seq)
