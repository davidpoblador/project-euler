#!/usr/bin/env python

from itertools import count
from common import primes

MAX = 2000000

s = sum(a for a in primes(MAX))

print(s)
