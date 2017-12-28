MAX = 100

sumOfSquares = sum(map(lambda x: x**2, range(MAX+1)))
squareOfSums = sum(range(MAX+1))**2

print(abs(sumOfSquares - squareOfSums))
