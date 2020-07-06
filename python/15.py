"""
Solution to Project Euler Problem 15
"""
import time
import math

start = time.time()
m = 20  # Length of the x-axis
n = 20  # Length of the y-axis

Answer = (math.factorial(m + n)) / (math.factorial(m) * math.factorial(n))

print ("Answer =", Answer)
print ("Time =", time.time()-start, "s")
