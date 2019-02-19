#!/usr/bin/env python

MIN, MAX = 2, 100

r = range(MIN, MAX+1)

nums = set()

for i in r:
    for j in r:
        nums.add(i**j)

print(len(nums))
