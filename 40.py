#!/usr/bin/env python

from itertools import count
from common import prod

lens = [1, 10, 100, 1000, 10000, 100000, 1000000]
MAX = max(lens)
s = "0"

for a in count(1):
    s += str(a)
    if len(s) > MAX:
        break

p = prod(int(s[a]) for a in lens)
print(p)