#!/usr/bin/env python

import fileinput

with open('p022_names.txt', 'r') as fp:
    data = fp.read()
names = sorted([a.strip('"') for a in data.split(',')])


def score(name):
    return sum((ord(a) - 96) for a in name.lower())

t = 0
for m, n in enumerate(names, 1):
    t += m * score(n)

print(t)
