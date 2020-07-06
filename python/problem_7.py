"""
Solution to Project Euler Problem 7
"""
import time

X = 15
ISPRIME = False
primeList = [2, 3, 5, 7, 11, 13]
startTime = time.time()


def is_prime(number):
    """Determine if number is a prime number."""
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    print("List length: ", len(primeList))
    return True


while len(primeList) != 10001:
    ISPRIME = is_prime(X)
    if ISPRIME:
        primeList.append(X)
        X += 2
    else:
        X += 2

print("Answer: ", primeList[10000])
print("Running Time: ", time.time() - startTime, " seconds")
