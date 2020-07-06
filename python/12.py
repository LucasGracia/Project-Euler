"""
Solution to Project Euler Problem 12
"""
import time

start = time.time()


def factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


triangularNumber = 0
for i in range(1, 100000):
    triangularNumber += i
    if len(factors(triangularNumber)) > 500:
        print("Answer =", triangularNumber)
        break
    else:
        print(i)

print("Time =", time.time() - start, "s")
