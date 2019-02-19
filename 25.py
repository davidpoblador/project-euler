#!/usr/bin/env python

from common import fib
from itertools import count

MAX = 1000

for a in count(1):
    f = fib(a)
    l = len(str(f))

    if l == 1000:
        print(a)
        break