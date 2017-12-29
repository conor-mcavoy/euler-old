import euler


n = 1
tri = 1
divs = 1
while divs < 500:
    n += 1
    tri += n
    divs = euler.num_of_divisors(tri)

print(tri)
