import math


def prime_factors(n):
    """n is an integer greater than 1."""
    
    if n == 0:
        return []

    pfs = []
    if n % 2 == 0:
        pfs.append(2)
        while n % 2 == 0:
            n //= 2

    for div in range(3, math.ceil(math.sqrt(n))+1, 2):
        if n % div == 0:
            pfs.append(div)
            while n % div == 0:
                n //= div

    if n != 1:
        pfs.append(n)

    return pfs


def gcd(a, b):
    """a and b are nonnegative integers."""

    while a != 0 and b != 0 and a != b:
        if a > b:
            a, b = a - b, b
        else:
            a, b = a, b - a

    if a == 0:
        return b
    return a


def lcm(a, b):
    """a and b are positive integers."""

    return a * b // gcd(a, b)
