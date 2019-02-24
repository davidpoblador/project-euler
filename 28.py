#!/usr/bin/env python

side = 1001
half = (side-1)//2

base = [i*2+3 for i in range(0, half)]

a = [i**2 for i in base]
b = [k - (6*(i+1)) for i, k in enumerate(a)]
c = [k + (2*(i+1)) for i, k in enumerate(b)]
d = [k + (2*(i+1)) for i, k in enumerate(c)]

total = sum(a) + sum(b) + sum(c) + sum(d) + 1
print(total)
