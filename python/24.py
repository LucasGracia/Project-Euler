#A program to calculate the millionth lexicographic permutation of the 0-9
import time
import math

#Variables
start = time.time()
startPoint = 0
numbers = [0,1,2,3,4,5,6,7,8,9]
answer = ""

for x in range(9,0-1,-1):
    for i in range(1,9 + 1):
        if startPoint + (math.factorial(x) * i) >= 1000000:
            startPoint += (math.factorial(x) * (i - 1))
            answer += str(numbers[i-1])
            del numbers[i-1]
            break

print(answer)
print ("Time =", time.time()-start, "s")
