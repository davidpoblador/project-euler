#!/usr/bin/env python


def d(den):
    num = 1
    remainders = []
    while True:
        r = num % den
        if not r:
            break

        if r in remainders:
            return len(remainders) - remainders.index(r)
        remainders.append(r)

        num = r * 10

    return None

maxlen = 0
maxperiodnumber = None
for a in range(1, 1000):
    p = d(a)
    if not p:
        continue

    if maxlen < p:
        maxlen = p
        maxperiodnumber = a

print(maxperiodnumber)