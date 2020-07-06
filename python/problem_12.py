"""
Solution to Project Euler Problem 12
"""
import time

start = time.time()


def factors(number):
    """Return a list of all factors of number."""
    factor_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            factor_list.append(i)
    return factor_list


TRIANGULAR_NUMBER = 0
for integer in range(1, 100000):
    TRIANGULAR_NUMBER += integer
    if len(factors(TRIANGULAR_NUMBER)) > 500:
        print("Answer =", TRIANGULAR_NUMBER)
        break

print("Time =", time.time() - start, "s")
