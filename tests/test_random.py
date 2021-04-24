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
