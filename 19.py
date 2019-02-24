#!/usr/bin/env python

s, e = 1901, 2000


def is_leap_year(y):
    if not y % 4:
        if not y % 400:
            return True

        if not y % 100:
            return False

        return True

    return False


def md(y):
    c = {
        1: 31,
        2: 28 + int(is_leap_year(y)),
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    return c


def cal(y, d=1):
    cal = {}
    for m, days in md(y).items():
        cal[m] = d
        o = days % 7
        d += o
        if d > 7:
            d = d % 7

    return cal, d

first_day = 1
calendar = []
for y in range(1900, e + 1):
    c, first_day = cal(y, first_day)
    if y >= s and y <= e:
        calendar.append(c)


sundays = 0
for c in calendar:
    sundays += len([a for a in c.values() if a == 7])

print(sundays)
