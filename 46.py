#!/usr/bin/env python

from common import primes, is_prime
from functools import lru_cache


def odd_composites(n=1000000):
    """ Find odd composites below n """

    i = 3
    while i < n:
        if not is_prime(i):
            yield i

        i += 2


def squares(n=10000000):
    """ Find squares below n """

    i = 1
    while True:
        sq = i ** 2
        if sq > n:
            break

        yield sq
        i += 1

for oc in odd_composites():
    for p in primes(oc - 1):
        diff = oc - p
        sq = list(squares((diff)//2))
        if (diff//2) in sq:
            break
    else:
        print("not found when odd is {}".format(oc))
        break
