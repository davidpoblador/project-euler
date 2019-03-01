#!/usr/bin/env python

from common import to_digits

MAX = 9


def is_n_pandigital(digits, end=MAX):
    ds = sorted(range(1, end + 1))
    di = sorted(digits)

    return ds == di

found = set()
for m1 in range(1, 10000):
    for m2 in range(1, 10000):
        mult = m1 * m2

        if mult > 98765:
            # Naive way of making it faster
            break

        digits = to_digits(m1) + to_digits(m2) + to_digits(mult)
        if is_n_pandigital(digits):
            found.add(mult)


print(sum(found))
