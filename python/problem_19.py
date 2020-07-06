"""
Solution to Project Euler Problem 19
"""
import time
import datetime

start = time.time()
START_YEAR = 1901
END_YEAR = 2000
COUNT = 0

for i in range(START_YEAR, END_YEAR):
    for x in range(1, 12 + 1):
        if datetime.date(i, x, 1).weekday() == 0:
            COUNT += 1

print(COUNT)
print("Time =", time.time() - start, "s")
