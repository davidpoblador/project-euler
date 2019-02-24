#!/usr/bin/env python

s = sum([a ** a for a in range(1, 1000+1)])
print(s % 10000000000)
