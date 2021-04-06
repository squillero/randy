# -*- coding: utf-8 -*-
# ______________   ________   __
# |____/|____|| \  ||    \ \_/
# |R  \_|A   ||N \_||D___/  |Y
#
#   @..@    古池や
#  (----)    蛙飛び込む
# ( >__< )    水の音
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

import timeit
from scipy.stats import truncnorm
import randy

if __name__ == '__main__':
    the_ram = randy.Randy()

    RANDY_CODE = '''
val = the_ram.sigma_random(a=-1, b=1, loc=0, strength=.5)
'''
    SCIPY_CODE = '''
val = truncnorm.rvs(-2, 2, loc=0, scale=.5)
'''

    rtimes = timeit.repeat(stmt=RANDY_CODE, repeat=10, number=10000, globals={'the_ram': the_ram})
    stimes = timeit.repeat(stmt=SCIPY_CODE, repeat=10, number=10000, globals={'truncnorm': truncnorm})

    overhead = 100 * (sum(stimes) - sum(rtimes)) / sum(stimes)
    print(f"Ovrhead on scipy's truncnorm: {overhead:.2f}%")
