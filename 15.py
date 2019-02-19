#!/usr/bin/env python

from common import factorial

SIDE = 20

# Central binomial coefficients (permutations of 0,1)
# ((2n)! choose n!^2 )

v = factorial(2 * SIDE) // (factorial(SIDE) ** 2)

print(v)
