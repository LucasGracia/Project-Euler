"""
A program to work out the largest palindrome made from the product of
two 3 digit numbers
"""
import time

start = time.time()
PALINDROME = 0


def is_palindrome(number):
    """Check if number is the same when read forwards and backwards."""
    if str(number) == str(number)[::-1]:
        return True
    return False


for x in range(1, 999):
    for y in range(1, 999):
        if is_palindrome(x * y):
            if x * y > PALINDROME:
                PALINDROME = x * y

print(PALINDROME)
print("Time =", time.time() - start, "s")
