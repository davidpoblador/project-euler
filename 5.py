#!/usr/bin/env python

from common import lcm
MAX = 20

acc = 1
for a in range(1, MAX + 1):
    acc = int(lcm(acc, a))

print(acc)
