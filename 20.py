#!/usr/bin/env python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

o = sum(int(a) for a in str(factorial(100)))

print(o)
