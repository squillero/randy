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
# IN THE SOFTWARE

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
