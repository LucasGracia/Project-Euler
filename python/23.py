#A program to show the sum of all positive integers that can not be written
#as the sum of two abundant numbers
import time

#Variables
start = time.time()
abundantSums = []
total = 0

def isAbundant(number):
    factors = [x for x in range(1, (number / 2) + 1) if number % x == 0]
    if sum(factors) > number:
        return True
    else:
        return False

#Generate a list of all the abundant numbers up to the given limit
abundantNumbers = set([x for x in range(1, (28123 + 1)) if isAbundant(x)])
#Compute all the possible sums of these numbers
for abundantNumber in abundantNumbers:
    for number in abundantNumbers:
        abundantSums.append(abundantNumber + number)

abundantSums = set(abundantSums)
abundantSums = [x for x in abundantSums if x <= 28123]

for i in range(28123 + 1):
    if i not in abundantSums:
        total += i
print(total)

print ("Time =", time.time()-start, "s")
