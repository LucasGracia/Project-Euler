"""
Solution to Project Euler Problem 5
"""
import time

number = 2520
startTime = time.time()

while (
    number % 20 != 0
    or number % 19 != 0
    or number % 18 != 0
    or number % 17 != 0
    or number % 16 != 0
    or number % 15 != 0
    or number % 15 != 0
    or number % 15 != 0
    or number % 14 != 0
    or number % 13 != 0
    or number % 12 != 0
    or number % 11 != 0
):
    number += 2520

print("Answer: ", number)
print("Time: ", time.time() - startTime)
