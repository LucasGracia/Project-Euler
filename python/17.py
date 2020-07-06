import time
from num2words import num2words
import re

#Variables
start = time.time()
numbers = []
sumLength = 0

for i in range(1,1000+1):
    number = num2words(i)
    number = re.sub('[- ]', '', number)
    numbers.append(number)
    
for item in numbers:
    sumLength += len(item)

print (sumLength)
print("Time =", time.time()-start, "s")
