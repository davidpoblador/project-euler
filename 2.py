#!/usr/bin/env python


def fib():
    i = 0
    j = 1
    while True:
        yield j
        i, j = j, j+i


def fibmax(maxnum):
    for a in fib():
        if a >= maxnum:
            break

        yield a

b = sum(a for a in fibmax(4000000) if not a%2)

print(b)
