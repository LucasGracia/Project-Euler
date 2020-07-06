"""
Solution to Project Euler Problem 26
"""
import time

start = time.time()
ANSWER = 0
LONGEST = 0
PATTERN = ""

decimals = [str(1 / float(x)) for x in range(1, 1000 + 1)]

for index, value in enumerate(decimals):
    for x in range(3, len(value)):
        if value[x] == value[2]:
            # save pattern for counting
            PATTERN = value[2:x]
            # see if pattern is repeated
            if value.count(PATTERN) > 1:
                if len(PATTERN) > LONGEST:
                    LONGEST = len(PATTERN)
                    ANSWER = index
print(ANSWER)
print("Time =", time.time() - start, "s")
