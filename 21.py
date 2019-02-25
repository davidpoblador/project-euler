#!/usr/bin/env python

from common import proper_divisors

MAX = 10000
seen = set()
amicable = set()


def d(x):
    return(sum(proper_divisors(x)))

for a in range(1, MAX):
    if a in seen:
        continue
    seen.add(a)

    b = d(a)
    z = d(b)

    if a == z:
        if b != a:
            seen.add(z)
            amicable.add(z)
            amicable.add(a)

print(sum(amicable))




