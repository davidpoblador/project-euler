#!/usr/bin/env python

MAX = 100

sum_squares = sum(a**2 for a in range(1, MAX + 1))
square_of_sum = sum(a for a in range(1, MAX+1)) ** 2
print(square_of_sum - sum_squares)