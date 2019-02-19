#!/usr/bin/env python

from collections import defaultdict

MAX = 1000000
cache = {}


def collatz_sequence(i):
    while i != 1:
        yield i
        if not i % 2:
            i //= 2
        else:
            i = 3*i + 1
    else:
        yield i

maxnum = 0
current_max = None
for n in range(1, MAX):
    l = 0
    for e in collatz_sequence(n):
        if e in cache:
            l += cache[e]
            break

        l += 1

    cache[n] = l
    if l > maxnum:
        maxnum = l
        current_max = n

print(current_max)
