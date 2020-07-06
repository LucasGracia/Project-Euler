"""
Solution to Project Euler Problem 9
"""
import time

start = time.time()

for a in range(1, 350):
    for b in range(a, 500):
        c = 1000 - b - a
        if a ** 2 + b ** 2 == c ** 2:
            print("Answer =", a * b * c)
            print("Time =", time.time() - start, "s")
