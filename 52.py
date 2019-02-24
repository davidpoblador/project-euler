#!/usr/bin/env python

from itertools import count
from common import to_digits


def dig(n):
    return sorted(to_digits(n))

n = None
for i in count(1):
    d = dig(i)
    for a in range(2, 6 + 1):
        if d != dig(i*a):
            break
    else:
        n = i
        break

print(n)
