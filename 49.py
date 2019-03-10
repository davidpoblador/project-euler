#!/usr/bin/env python

from common import is_prime, to_digits

for n1 in range(1000, 10000 - (3330 * 2)):
    n2 = n1 + 3330
    n3 = n2 + 3330
    d1 = to_digits(n1)
    d2 = to_digits(n2)
    d3 = to_digits(n3)

    if not (sorted(d1) == sorted(d2)):
        continue

    if not (sorted(d1) == sorted(d3)):
        continue

    if not is_prime(n1):
        continue

    if not is_prime(n2):
        continue

    if not is_prime(n3):
        continue

    s = sum([a * 10**k for k, a in enumerate(reversed(d1 + d2 + d3))])
    print(s)
