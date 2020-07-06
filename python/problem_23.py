"""
Solution to Project Euler Problem 23
"""
import time

start = time.time()
abundantSums = []
TOTAL = 0


def is_abundant(number):
    """Determine if sum of divisors of number is greater than number."""
    factors = [x for x in range(1, (number // 2) + 1) if number % x == 0]
    if sum(factors) > number:
        return True
    return False


# Generate a list of all the abundant numbers up to the given limit
abundantNumbers = {x for x in range(1, 28123 + 1) if is_abundant(x)}

# Compute all the possible sums of these numbers
for abundantNumber in abundantNumbers:
    for value in abundantNumbers:
        abundantSums.append(abundantNumber + value)

abundantSums = set(abundantSums)
abundantSums = [x for x in abundantSums if x <= 28123]

for i in range(28123 + 1):
    if i not in abundantSums:
        TOTAL += i
print(TOTAL)

print("Time =", time.time() - start, "s")
