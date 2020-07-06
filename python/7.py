"""
Solution to Project Euler Problem 7
"""
import time

x = 15
isPrimeBool = False
primeList = [2, 3, 5, 7, 11, 13]
startTime = time.time()


def isPrime(x):
    isPrimeBool = False
    i = 2
    while i < x:
        if x % i == 0:
            return False
        else:
            i += 1
    print("List length: ", len(primeList))
    return True


while len(primeList) != 10001:
    isPrimeBool = isPrime(x)
    if isPrimeBool:
        primeList.append(x)
        x += 2
    else:
        x += 2

print("Answer: ", primeList[10000])
print("Running Time: ", time.time()-startTime, " seconds")
