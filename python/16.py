"""
Solution to Project Euler Problem 16
"""
import time

start = time.time()
power = 2 ** 1000
total = 0

for character in str(power)[:]:
    total += int(character)

print("Answer =", total)
print("Time =", time.time() - start, "s")
