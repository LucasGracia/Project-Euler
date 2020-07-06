"""
Solution to Project Euler Problem 6
"""
import time

startTime = time.time()


def square_of_sum():
    """Return the square of the sum of the first 100 natural numbers."""
    total = 0
    for i in range(1, 100 + 1):
        total += i

    return total ** 2


def sum_of_squares():
    """Return the sum of the square of the first 100 natural numbers."""
    total = 0
    for i in range(1, 100 + 1):
        total += i ** 2

    return total


squareOfSum = square_of_sum()
sumOfSquares = sum_of_squares()

print("Answer: ", squareOfSum - sumOfSquares)
print("Time: ", time.time() - startTime)
