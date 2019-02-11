#!/usr/bin/env python

from functools import lru_cache


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


n = 600851475143
i = 1
maxprime = 0
while i < n:

    if not isprime(i):
        i += 1
        continue

    if not n % i:

        maxprime = max(maxprime, i)
        n //= i
        continue

    i += 1
else:
    maxprime = max(i, maxprime)

print(maxprime)
