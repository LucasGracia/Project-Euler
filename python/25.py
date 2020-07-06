"""
Solution to Project Euler Problem 25
"""
import time

start = time.time()

previous = 1
current = 1
future = 0
fibs = [1, 1]

while len(str(current)) <= 1000:
    if len(str(current)) == 1000:
        fibs.append(current)
        break
    future = current + previous
    previous = current
    current = future
    fibs.append(current)

print("length of fibs =", len(fibs))
print("index of the last number in fibs:", len(fibs)-1)

print ("Time =", time.time()-start, "s")
