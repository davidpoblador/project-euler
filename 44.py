#!/usr/bin/env python


from itertools import islice, count
from sys import maxsize


def pentagonal():
    for n in count(1):
        yield n * ((3*n) - 1) // 2

pentagonals = list(islice(pentagonal(), 5000))
pentaset = set(pentagonals)

maxdiff = maxsize
for k in pentagonals:
    for j in pentagonals:
        d = k - j
        if not d:
            continue

        if d < 0:
            continue

        if d in pentaset and (k + j) in pentaset:
            if d < maxdiff:
                maxdiff = d
            break

print(maxdiff)
