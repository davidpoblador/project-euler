#!/usr/bin/env python

from itertools import permutations
from common import is_prime
import sys

for a in range(9, 0, -1):
    digits = reversed(range(1, a+1))
    for b in permutations(digits):
        if b[-1] in {0, 2, 4, 6, 8, 5}:
            continue
        
        n = int(''.join([str(i) for i in b]))

        if is_prime(n):
            print(n)
            sys.exit()