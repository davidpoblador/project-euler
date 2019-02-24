#!/usr/bin/env python

units = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

teens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

dec = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def num2text(n):
    if n < 0 or n > 1000:
        raise ValueError

    if n == 1000:
        return "onethousand"

    if n == 0:
        return ''

    if n < 10:
        return units[n]

    if n < 20:
        return teens[n]

    if n < 100:
        return dec[(n // 10) * 10] + num2text(n % 10)

    if n < 1000:
        if not n % 100:
            return units[(n // 100)] + "hundred"
        else:
            return units[(n // 100)] + "hundred" + "and" + num2text(n % 100)


s = sum(len(num2text(a)) for a in range(1, 1000+1))

print(s)
