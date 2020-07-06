#A program to calclate the sum of all digits reulting from 2 to the power of 1000

import time

#Variables
start = time.time()
power = 2 ** 1000
total = 0

for character in str(power)[:]:
    total += int(character)

print("Answer =", total)
print("Time =", time.time()-start, "s")
