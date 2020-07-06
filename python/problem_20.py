"""
Solution to Project Euler Problem 20
"""
import time
import math

start = time.time()
number = math.factorial(100)
COUNT = 0

for character in str(number):
    COUNT += int(character)

print(COUNT)
print("Time =", time.time() - start, "s")
