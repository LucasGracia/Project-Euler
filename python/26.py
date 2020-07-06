"""
Solution to Project Euler Problem 26
"""
import time

start = time.time()
answer = 0
longest = 0
pattern = ""

decimals = [str(1 / float(x)) for x in range(1, 1000 + 1)]

for i in range(len(decimals)):
    for x in range(3, len(decimals[i])):
        if decimals[i][x] == decimals[i][2]:
            # save pattern for counting
            pattern = decimals[i][2:x]
            # see if pattern is repeated
            if decimals[i].count(pattern) > 1:
                if len(pattern) > longest:
                    longest = len(pattern)
                    answer = i
print(answer)
print("Time =", time.time() - start, "s")
