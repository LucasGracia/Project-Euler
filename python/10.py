#Project Euler Problem 10, VERSION 2
import time

start = time.time()
primes = []

for i in range(2,500000+1):
    isPrime = 1
    if i % 2 != 0 or i == 2:
        for x in primes:
            if i % x == 0:
                #Not prime
                isPrime = 0

        if isPrime == 1:
            for y in range(2,int(i**0.5)):
                if i % y == 0:
                    #Not prime
                    isPrime = 0
    else:
        isPrime = 0

    if isPrime == 1:
        primes.append(i)

print (sum(primes))
print("Time =", time.time()-start, "s")
