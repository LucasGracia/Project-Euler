"""
Solution to Project Euler Problem 5
"""
import time

NUMBER = 2520
startTime = time.time()

while (
        NUMBER % 20 != 0
        or NUMBER % 19 != 0
        or NUMBER % 18 != 0
        or NUMBER % 17 != 0
        or NUMBER % 16 != 0
        or NUMBER % 15 != 0
        or NUMBER % 15 != 0
        or NUMBER % 15 != 0
        or NUMBER % 14 != 0
        or NUMBER % 13 != 0
        or NUMBER % 12 != 0
        or NUMBER % 11 != 0
):
    NUMBER += 2520

print("Answer: ", NUMBER)
print("Time: ", time.time() - startTime)
