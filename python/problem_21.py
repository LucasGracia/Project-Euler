"""
Solution to Project Euler Problem 21
"""
import time

start = time.time()
amicableNumbers = []


def factors_sum(number):
    """A function to produce the sum of the factors of a number."""
    factor_list = []
    for counter in range(1, int((number + 1) / 2)):
        if number % counter == 0:
            factor_list.append(i)
    return sum(factor_list)


def is_amicable_pair(number_x, number_y):
    """Determines if the sum of the factors of x and y are equal."""
    if factors_sum(number_x) == number_y and factors_sum(number_y) == number_x:
        return True
    return False


for i in range(2, 10000 + 1):
    for j in range(2, 10000 + 1):
        if i != j:
            if is_amicable_pair(i, j) is True:
                amicableNumbers.append(i)
                amicableNumbers.append(j)

print(sum(set(amicableNumbers)))
print("Time =", time.time() - start, "s")
