#!/usr/bin/env python

from common import is_prime, primes

MAX = 1000000
pnums = set(primes(MAX))


def rotations(num):
    s = str(num)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def is_cicrular(num):
    return all([a in pnums for a in rotations(num)])


circulars = len(list(filter(is_cicrular, pnums)))

print(circulars)
