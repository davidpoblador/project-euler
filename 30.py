#!/usr/bin/env python

from itertools import count
from common import to_digits

powers = [n ** 5 for n in range(0, 10)]

t = 0
for a in count(10):
    if a > 1000000:
        break

    s = sum([powers[d] for d in to_digits(a)])
    if a == s:
        t += a

print(t)
