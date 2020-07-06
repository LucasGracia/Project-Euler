"""
Solution to Project Euler Problem 24
"""
import time
import math

start = time.time()
START_POINT = 0
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ANSWER = ""

for x in range(9, 0 - 1, -1):
    for i in range(1, 9 + 1):
        if START_POINT + (math.factorial(x) * i) >= 1000000:
            START_POINT += math.factorial(x) * (i - 1)
            ANSWER += str(numbers[i - 1])
            del numbers[i - 1]
            break

print(ANSWER)
print("Time =", time.time() - start, "s")
