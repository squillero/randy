# -*- coding: utf-8 -*-
# ______________   ________   __
# |____/|____|| \  ||    \ \_/
# |R  \_|A   ||N \_||D___/  |Y
#
#   @..@    古池や
#  (----)    蛙飛び込む
# ( >__< )    水の音
#
# ( ! ) 2021 Giovanni Squillero. CC0 Public Domain.
# Project page: https://github.com/squillero/randy

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

    overhead = 100 * (sum(rtimes) - sum(stimes)) / sum(stimes)
    print(f"Ovrhead on scipy's truncnorm: {overhead:.2f}%")
