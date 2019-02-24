#!/usr/bin/env python

from common import prime_factors
from itertools import count

MAX = 4


def spf(n):
    return set(prime_factors(n))

f = []
for i in count(2):
    if len(f) == MAX:
        break

    if len(spf(i)) == MAX:
        f.append(i)
    else:
        f = []

print(f[0])
