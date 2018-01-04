def count_collatz(n, memory):
    """Returns the length of the Collatz chain starting at n and terminating at the first 1."""

    iterations = 0
    while n not in memory:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        iterations += 1

    return iterations + memory[n]

cache = {1: 1}

longest = 0
best = 0
for x in range(2, 1_000_000):
    chain = count_collatz(x, cache)
    cache[x] = chain
    if chain > longest:
        longest = chain
        best = x
print(best)
