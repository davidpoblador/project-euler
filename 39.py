#!/usr/bin/env python

MAX = 1000


def triangles_p(n):
    found = set()
    for a in range(1, n-1):
        for b in range(1, n-1):
            c = n - (a + b)
            ab2 = a**2 + b**2
            c2 = c**2
            if ab2 > c2:
                break
            elif ab2 == c2:
                found.add(tuple(sorted([a, b, c])))

    return found

maxlen = 0
maxp = None
for p in range(MAX+1):
    lp = len(triangles_p(p))
    if lp > maxlen:
        maxlen = lp
        maxp = p

print(maxp)
