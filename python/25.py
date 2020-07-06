#A program to calculate the index of the first fibonacci number to have 1000 digits
import time

#Variables
start = time.time()

previous = 1
current = 1
future = 0
fibs = [1,1]

while len(str(current)) <= 1000:
    if len(str(current)) == 1000:
        fibs.append(current)
        break
    future = current + previous
    previous = current
    current = future
    fibs.append(current)

print("length of fibs =", len(fibs))
print("as lists start at 0, the index of the last number in fibs is:", len(fibs)-1)

print ("Time =", time.time()-start, "s")
