#!/usr/bin/env python

from common import factorial, to_digits
from itertools import count


fs = list(factorial(n) for n in range(0, 10))

S = 0
for i in count(10):
    if i > 100000:
        break
    s = sum(fs[d] for d in to_digits(i))
    if s == i:
        S += i

print(S)
