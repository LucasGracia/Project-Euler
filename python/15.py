import time
import math

#Variables
start = time.time()
m = 20 #Length of the x-axis
n = 20 #Length of te y-axis

Answer = (math.factorial(m + n)) / (math.factorial(m) * math.factorial(n))

print ("Answer =", Answer)
print ("Time =", time.time()-start, "s")
