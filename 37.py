#!/usr/bin/env python

from common import primes

MAX = 1000000
pnums = set(p for p in primes(MAX))


def get_combinations(n):
    o = set()
    s = str(n)
    for a in range(len(s)-1):
        o.add(int(s[a+1:]))
        o.add(int(s[:a+1]))

    return(o)


def are_combs_prime(n):
    return all([a in pnums for a in get_combinations(n)])


truncatable_primes = filter(are_combs_prime, (p for p in pnums if p > 9))

print(sum(truncatable_primes))
