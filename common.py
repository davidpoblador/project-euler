
from operator import mul
from functools import reduce


def is_palindrome(i):
    """Is i a palindrome?"""
    return str(i) == str(i)[::-1]


def prime_factors(n):
    """Prime factors of n"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    else:
        if n > 1:
            factors.append(n)

    return factors


def unique_prime_factors(n):
    """Unique prime factors of n"""
    return set(prime_factors(n))


def gcd(a, b):
    """GCD of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """LCM of a and b"""
    return a * b / gcd(a, b)


def prod(iter):
    """Product of iterable (like sum())"""
    return reduce(mul, iter)
