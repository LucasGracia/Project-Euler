"""
Solution to Project Euler Problem 25
"""
import time

start = time.time()

PREVIOUS = 1
CURRENT = 1
FUTURE = 0
fibs = [1, 1]

while len(str(CURRENT)) <= 1000:
    if len(str(CURRENT)) == 1000:
        fibs.append(CURRENT)
        break
    FUTURE = CURRENT + PREVIOUS
    PREVIOUS = CURRENT
    CURRENT = FUTURE
    fibs.append(CURRENT)

print("length of fibs =", len(fibs))
print("index of the last number in fibs:", len(fibs) - 1)

print("Time =", time.time() - start, "s")
