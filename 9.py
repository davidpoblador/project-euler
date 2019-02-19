#!/usr/bin/env python

MAX = 1000


def solve():
    for a in range(1, MAX):
        for b in range(a, MAX):
            c = MAX - a - b
            if a**2 + b**2 == c**2:
                return (a*b*c)

o = solve()
print(o)
