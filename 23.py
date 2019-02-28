#!/usr/bin/env python

from common import proper_divisors
import sys

MAX = 28123


def perfect(n):
    if n < 1:
        raise ValueError

    s = sum(proper_divisors(n))

    if s < n:
        return -1
    elif s > n:
        return 1
    else:
        return 0

abus = [a for a in range(1, MAX+1) if perfect(a) > 0]

impossible = []
for a in range(1, MAX + 1):
    if a < 24:
        impossible.append(a)
        continue

    b = [c for c in abus if c < a]
    for d in b:
        e = a - d
        if e not in b:
            continue
        else:
            break
    else:
        impossible.append(a)


print(sum(impossible))
