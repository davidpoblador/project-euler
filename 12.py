#!/usr/bin/env python

from itertools import count
from common import num_divisors
import sys

tn = 0
for i in count(1):
    tn += i
    d = num_divisors(tn)

    if d > 500:
        print(tn)
        break
