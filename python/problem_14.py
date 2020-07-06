"""
Solution to Project Euler Problem 14
"""
import time

start = time.time()
WORKING_LENGTH = 0
CHAIN_LENGTH = 0
CHAIN_START = 0


def collatz_even(number):
    """Return n/2 for given number."""
    return number / 2


def collatz_odd(number):
    """Return 3n+1 for a given number."""
    return (number * 3) + 1


def collatz_chain(number):
    """Build a collatz chain for a given number."""
    i = 0
    while number != 1:
        i += 1
        if number % 2 == 0:
            number = collatz_even(number)
        else:
            number = collatz_odd(number)
    return i


for counter in range(2, 1000000 + 1):
    WORKING_LENGTH = collatz_chain(counter)
    if WORKING_LENGTH > CHAIN_LENGTH:
        CHAIN_LENGTH = WORKING_LENGTH
        CHAIN_START = counter

print("Answer =", CHAIN_START, ", length =", CHAIN_LENGTH)
print("Time =", time.time() - start, "s")
