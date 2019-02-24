#!/usr/bin/env python

from itertools import count
from common import is_prime


def num_of_primes(a, b):
    s = 0

    for c in count(0):
        n = (c ** 2) + (a * c) + b
        if is_prime(n):
            s += 1
        else:
            return s

max_prime = 0
A, B = None, None
for a in range(-999, 999 + 1):
    for b in range(-1000, 1000 + 1):
        if b < 2:
            # If n starts at 0, we don't want numbers <2
            continue

        r = b % 10
        if r in {0, 2, 4, 6, 8, 5}:
            continue

        m = num_of_primes(a, b)
        if m > max_prime:
            A, B = a, b
            max_prime = m
else:
    print(A*B)
