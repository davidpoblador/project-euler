#!/usr/bin/env python

from common import is_palindrome

s = 0
for i in range(1, 1000000):
    if is_palindrome(i):
        b = format(i, 'b')
        if is_palindrome(b):
            s += i

print(s)
