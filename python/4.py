"""
A program to work out the largest palindrome made from the product of
two 3 digit numbers
"""
import time

start = time.time()
palindrome = 0


def isPalindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


for x in range(1, 999):
    for y in range(1, 999):
        if isPalindrome(x * y):
            if x * y > palindrome:
                palindrome = x * y

print(palindrome)
print("Time =", time.time() - start, "s")
