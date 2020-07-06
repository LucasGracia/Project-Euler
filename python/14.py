"""
Solution to Project Euler Problem 14
"""
import time

start = time.time()
workingLength = 0
chainLength = 0
chainStart = 0


def collatzEven(number):
    return number / 2


def collatzOdd(number):
    return (number * 3) + 1


def collatzChain(number):
    i = 0
    while number != 1:
        i += 1
        if number % 2 == 0:
            number = collatzEven(number)
        else:
            number = collatzOdd(number)
    return i


for i in range(2, 1000000 + 1):
    workingLength = collatzChain(i)
    if workingLength > chainLength:
        chainLength = workingLength
        chainStart = i
        print(i)

print("Answer =", chainStart, ", length =", chainLength)
print("Time =", time.time() - start, "s")
