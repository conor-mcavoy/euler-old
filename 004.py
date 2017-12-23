best_palindrome = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        if i * j > best_palindrome and str(i * j) == str(i * j)[::-1]:
            best_palindrome = i * j

print(best_palindrome)
