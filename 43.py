#!/usr/bin/env python

from itertools import permutations
from common import to_digits


def pdiv(a):
    for i, b in enumerate([2, 3, 5, 7, 11, 13, 17]):
        n = a[1+i] * 100 + a[2+i] * 10 + a[3+i]
        if n % b:
            return False

    return True

s = 0
d = (i for i in range(10))
for a in permutations(d):
    if pdiv(a):
        b = sum([((10**i)*n) for i, n in enumerate(reversed(a))])
        s += b

print(s)
