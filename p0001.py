"""
Solution to Project Euler problem 1.
'Find the sum of all the multiples of 3 or 5 below 100'

https://github.com/LucasGracia/Project-Euler
"""
__author__ = 'Lucas Gracia'
__version__ = '1.0.0'
__license__ = 'MIT'

import time

def sum_multiples(limit):
    """Sums all multiples of 3 and 5 under `limit`

    Args:
        limit (int): The limit that the sums will be calculated up to

    Returns:
        int : The sum of all multiples of 3 and 5 up to `limit`
    """
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)

if __name__ == '__main__':
    START_TIME = time.time()
    ANSWER = sum_multiples(1000)
    END_TIME = time.time()
    print("Answer: {}\nTime: {}s".format(ANSWER, END_TIME - START_TIME))
