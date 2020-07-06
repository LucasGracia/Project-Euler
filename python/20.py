import time
import math

#Variables
start = time.time()
number = math.factorial(100)
count = 0

for character in str(number):
    count += int(character)

print(count)
print ("Time =", time.time()-start, "s")
