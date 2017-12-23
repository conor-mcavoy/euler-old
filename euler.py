import math


def prime_factors(n):
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
