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

import randy


def t2():
    x = 0
    x += randy.random()

    import randy as r
    x += r.randint(10, 100)

    return x
