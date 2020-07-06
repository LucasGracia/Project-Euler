"""
Solution to Project Euler Problem 15
"""
import time
import math

start = time.time()
X_AXIS_LENGTH = 20  # Length of the x-axis
Y_AXIS_LENGTH = 20  # Length of the y-axis

Answer = (math.factorial(X_AXIS_LENGTH + Y_AXIS_LENGTH)) / (
    math.factorial(X_AXIS_LENGTH) * math.factorial(Y_AXIS_LENGTH)
)

print("Answer =", Answer)
print("Time =", time.time() - start, "s")
