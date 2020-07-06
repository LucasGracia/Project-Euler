"""
Solution to Project Euler Problem 16
"""
import time

start = time.time()
POWER = 2 ** 1000
TOTAL = 0

for character in str(POWER)[:]:
    TOTAL += int(character)

print("Answer =", TOTAL)
print("Time =", time.time() - start, "s")
