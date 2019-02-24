#!/usr/bin/env python

from itertools import count

def t(n=1):
    for i in count(n):
        yield (i, (i * (i + 1) // 2))


def p(n=1):
    for i in count(n):
        yield (i, (i * ((3*i) - 1) // 2))


def h(n=1):
    for i in count(n):
        yield (i * ((2*i) - 1))

mt = 1
mp = 1
for i in h():
    for mmp, j in p(mp):
        if j > i:
            mp = mmp
            break
        elif j < i:
            continue

        for mmt, k in t(mt):
            if k > j:
                mt = mmt
                break
            elif k < j:
                continue
            else:
                print(k)