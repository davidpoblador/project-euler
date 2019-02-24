
from operator import mul
from functools import reduce
from functools import lru_cache


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


def divisors(n):
    """Finds all divisors for n"""
    factors = set()

    for i in range(1, int((n ** (1/2)) + 1)):
        if not n % i:
            factors.add(i)
            factors.add(n//i)

    return factors


def proper_divisors(n):
    return divisors(n) - {n}


def num_divisors(n):
    return len(divisors(n))


def primes(n):
    """ Find primes below n """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i**2::2*i] = [False] * ((n-(i**2)-1)//(2*i)+1)

    yield 2

    for i in range(3, n, 2):
        if sieve[i]:
            yield i


def factorial(n):
    if n < 0:
        raise ValueError

    if n in {0, 1}:
        return 1
    else:
        return n * factorial(n-1)


@lru_cache(maxsize=None)
def fib(n):
    if n == 1:
        return 1

    if n == 2:
        return 1

    return fib(n-1) + fib(n-2)


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True


def to_digits(num):
    """Convert an integer into a list of its digits (int)"""

    if num < 1:
        raise ValueError

    digits = []
    while num >= 10:
        d = num % 10
        num //= 10
        digits.append(d)
    else:
        digits.append(num)

    return list(reversed(digits))
