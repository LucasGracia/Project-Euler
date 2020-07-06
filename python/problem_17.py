"""
Solution to Project Euler Problem 17
"""
import time
import re
from num2words import num2words

start = time.time()
numbers = []
SUM_LENGTH = 0

for i in range(1, 1000 + 1):
    number = num2words(i)
    number = re.sub("[- ]", "", number)
    numbers.append(number)

for item in numbers:
    SUM_LENGTH += len(item)

print(SUM_LENGTH)
print("Time =", time.time() - start, "s")
