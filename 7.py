#!/usr/bin/env python

from functools import lru_cache

NTH_PRIME = 10001

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
found_primes = 0
latest_prime = None
while True:
    if not isprime(i):
        i += 1
        continue
    else:
        found_primes += 1
        latest_prime = i
        i += 1

    
    if found_primes == NTH_PRIME:
        break

print(latest_prime)
