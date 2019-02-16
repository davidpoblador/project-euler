#!/usr/bin/env python

from functools import lru_cache

BELOW = 2000000


@lru_cache(maxsize=None)
def isprime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for i in range(3, n//2, 2):
        if n % i == 0:
            return False

    return True

i = 2
prime_sum = 0
while i < BELOW:
    if not i % 20000:
        print(i)

    if i > 5:
        b = i % 10
        if b in {2, 4, 5, 6, 8, 0}:
            i += 1
            continue

    if isprime(i):
        prime_sum += i

    i += 1


print(prime_sum)
