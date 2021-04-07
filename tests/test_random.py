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

import numpy as np
import randy


def test_test():
    assert True


def test_sigma_random_reproducibility():
    a, b = 10, 20
    loc = 18
    strength = .2
    for seed in range(43):
        ram1 = randy.Randy(seed)
        val1 = [ram1.sigma_random(a=a, b=b, loc=loc, strength=strength) for _ in range(100)]
        ram2 = randy.Randy(seed)
        val2 = [ram2.sigma_random(a=a, b=b, loc=loc, strength=strength) for _ in range(100)]
        assert val1 == val2


def test_sigma_random_independence():
    a, b = 10, 23
    loc = 18
    strength = .1

    ram1 = randy.Randy(42)
    val1 = [ram1.sigma_random(a=a, b=b, loc=loc, strength=strength) for _ in range(1000)]
    ram2 = randy.Randy(42)
    val2a = [ram2.sigma_random(a=a, b=b, loc=loc, strength=strength) for _ in range(500)]
    zap = np.random.random(size=100)
    val2b = [ram2.sigma_random(a=a, b=b, loc=loc, strength=strength) for _ in range(500)]
    assert val1 == val2a + val2b
