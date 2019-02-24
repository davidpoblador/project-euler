#!/usr/bin/env python

from itertools import count
from common import to_digits


def muls(n):
    d = set([0])
    dig = []
    for mul in count(1):
        t = to_digits(mul * n)
        if len(t) != len(set(t)):
            return False

        if set(t) & d:
            return False
        else:
            d |= set(t)
            dig += t

        if len(d) == 10:
            return dig
        elif len(d) > 10:
            raise Exception

m = None
for num in count(1):
    if num > 100000:
        break

    t = muls(num)
    if t:
        m = t

print(''.join([str(i) for i in m]))
