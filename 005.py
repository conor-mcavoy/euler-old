import euler

least = euler.lcm(1, 2)

for x in range(3, 21):
    least = euler.lcm(least, x)

print(least)
