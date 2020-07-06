"""
Solution to Project Euler Problem 10
"""
import time

start = time.time()
primes = []

for i in range(2, 500000+1):
    isPrime = True
    if i % 2 != 0 or i == 2:
        for x in primes:
            if i % x == 0:
                isPrime = False

        if isPrime == 1:
            for y in range(2, int(i**0.5)):
                if i % y == 0:
                    isPrime = False
    else:
        isPrime = False

    if isPrime is True:
        primes.append(i)

print (sum(primes))
print("Time =", time.time()-start, "s")
