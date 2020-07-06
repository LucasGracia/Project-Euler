"""
Solution to Project Euler Problem 6
"""
import time

startTime = time.time()


def squareOfSum():
    total = 0
    for i in range(1, 101):
        total += i

    return total ** 2


def sumOfSquares():
    total = 0
    for i in range(1, 101):
        total += i ** 2

    return total


squareOfSum = squareOfSum()
sumOfSquares = sumOfSquares()

print("Answer: ", squareOfSum - sumOfSquares)
print("Time: ", time.time() - startTime)
