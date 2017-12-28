import euler

print(sum(index for index, isPrime in enumerate(euler.sieve_of_erat(2_000_000)) if isPrime))
