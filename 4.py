#!/usr/bin/env python

from itertools import combinations


def ispalindrome(num):
    return str(num) == str(num)[::-1] 

maxpalindrome = 0
nums = range(100,1000)
for a, b in combinations(nums, 2):
    c = a * b
    if ispalindrome(c):
        maxpalindrome = max(maxpalindrome, c)

print(maxpalindrome)