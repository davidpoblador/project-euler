#!/usr/bin/env python

from itertools import count

coins = (200, 100, 50, 20, 10, 5, 2, 1)
total = 200


def pos(l, amount):
    if len(l) == 1:
        return 1

    c = l[0]
    ways = 0
    i = 0
    while (i * c) <= amount:
        if (i * c) < amount:
            ways += pos(l[1:], amount - (i * c))
        else:
            ways += 1
        i += 1

    return ways


print(pos(coins, total))
