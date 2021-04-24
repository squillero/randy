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

import re
from io import StringIO
import logging

import test_default_randy_p


def main():
    log_stream = StringIO()
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(stream=log_stream))

    test_default_randy_p.t1()
    test_default_randy_p.t2()
    x = log_stream.getvalue()

    randies = re.findall(r'Randy_[abcdef0-9]+', log_stream.getvalue())
    assert randies, "Logging failed"
    assert all(r == randies[0] for r in randies), "All Randies should be equal"


if __name__ == '__main__':
    main()
