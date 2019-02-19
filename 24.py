#!/usr/bin/env python

from itertools import permutations

digits = ''.join([str(a) for a in range(0, 10)])

p = permutations(digits)

l = sorted([''.join(c) for c in p])

print(l[999999])
