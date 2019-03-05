#!/usr/bin/env python

from common import to_digits
from fractions import Fraction


def remove_digit(d, l):
    if l[0] == d:
        return l[1]
    else:
        return l[0]

nprod = 1
dprod = 1
for d in range(11, 100):
    for n in range(10, d):
        dd = to_digits(d)
        dn = to_digits(n)

        common = set(dd) & set(dn)
        if len(common) != 1:
            # We don't want empty sets or bigger than one (to avoid /0)
            continue

        digit = common.pop()

        if not digit:
            # Remove trivial examples
            continue

        n2 = remove_digit(digit, dn)
        d2 = remove_digit(digit, dd)

        if d2 == 0:
            # Avoid divide by zero
            continue

        div1 = n/d
        div2 = n2/d2

        if div1 == div2:
            nprod *= n2
            dprod *= d2


print(Fraction(nprod, dprod).denominator)
