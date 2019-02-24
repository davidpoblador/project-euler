#!/usr/bin/env python

s = 0
for a in range(1, 1000+1):
    s += (a**a)

print(s % 10000000000)