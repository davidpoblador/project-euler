#!/usr/bin/env python

with open('p042_words.txt', 'r') as fp:
    data = fp.read()
words = sorted([a.strip('"') for a in data.split(',')])


def trianglenums(limit=1000):
    for n in range(1, limit):
        yield ((n + 1) * n) // 2


def word_value(w):
    return sum(ord(l) - 64 for l in w.upper())


wvalues = (word_value(w) for w in words)
tnums = set(trianglenums())

l = list(filter(lambda x: x in tnums, wvalues))

print(len(l))
