"""
Solution to Project Euler Problem 10
    Find the sum of all primes below 2 million
"""
import time

start = time.time()
primes = []

for i in range(2, 500000 + 1):
    IS_PRIME = True
    if i % 2 != 0 or i == 2:
        for x in primes:
            if i % x == 0:
                IS_PRIME = False

        if IS_PRIME == 1:
            for y in range(2, int(i ** 0.5)):
                if i % y == 0:
                    IS_PRIME = False
    else:
        IS_PRIME = False

    if IS_PRIME is True:
        primes.append(i)

print(sum(primes))
print("Time =", time.time() - start, "s")
