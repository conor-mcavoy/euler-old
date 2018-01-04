import math


def prime_factors(n):
    """Returns prime factors of n in a list.

    n must be an integer greater than 1."""

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


def divisors(n):
    """Returns divisors of n in a list.

    n must be an integer greater than 0."""

    divs = set([1, n])

    for x in range(2, math.ceil(math.sqrt(n))+1):
        if n % x == 0:
            divs.add(x)
            divs.add(n // x)

    return list(sorted(divs))


def num_of_divisors(n):
    """Returns number of divisors of n.

    """

    if n == 1:
        return 1
    num = 2
    if int(math.sqrt(n))**2 == n:
        num += 1

    for x in range(2, math.floor(math.sqrt(n))):
        if n % x == 0:
            num += 2

    return num


def nth_prime(n):
    """Returns nth prime number.

    n must be positive."""

    if n <= 6:
        sieve_size = 14
    else:
        sieve_size = int(n * math.log(n, math.e) + n * math.log(math.log(n, math.e), math.e))

    sieve = sieve_of_erat(sieve_size)

    count = 0
    for index, p in enumerate(sieve):
        if p:
            count += 1
        if count == n:
            return index


def sieve_of_erat(n):
    sieve = [True for _ in range(n)]
    sieve[0] = False
    sieve[1] = False

    for i in range(2, math.ceil(math.sqrt(n))):
        if sieve[i]:
            for j in range(i**2, n, i):
                sieve[j] = False
    return sieve


def gcd(a, b):
    """Returns greatest common divisor of a and b.

    a and b must be nonnegative integers."""

    while a != 0 and b != 0 and a != b:
        if a > b:
            a, b = a - b, b
        else:
            a, b = a, b - a

    if a == 0:
        return b
    return a


def lcm(a, b):
    """Returns lowest common multiple of a and b.

     a and b must be positive integers."""

    return a * b // gcd(a, b)


def triangle(n):
    """Returns the nth triangle number.

    n must be an integer greater than 0. The 1st triangle number is 1."""

    return sum(range(n+1))


def binom_coef(n, k):
    """Returns the binomial coefficient corresponding to n and k."""

    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
