"""
Solution to Project Euler problem 2.
    'By considering the terms in the Fibonacci sequence whose values
     do not exceed four million, find the sum of the even-valued terms.'

https://github.com/LucasGracia/Project-Euler
"""
__author__ = 'Lucas Gracia'
__version__ = '1.0.0'
__license__ = 'MIT'

import time
import argparse


def process_arguments():
    """Processes user-entered command line arguments

    Returns:
        args.l (int) : The limit to be passed to `sum_fibs`
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', type=int, default=4000000, help='Sum limit')
    args = parser.parse_args()
    return args.l


def sum_fibs(limit):
    """Sums even Fibonacci numbers upto `limit`

    Args:
        limit (int) : The limit the sum will be calculated to

    Returns:
        int : The sum of even Fibonacci numbers upto `limit`
    """
    previous = 0
    current = 1
    future = 1
    result = 0

    while True:
        future = current + previous
        if future < limit:
            if future % 2 == 0:
                result += future
        else:
            break
        previous = current
        current = future

    return result


if __name__ == '__main__':
    START_TIME = time.time()

    LIMIT = process_arguments()
    ANSWER = sum_fibs(LIMIT)

    END_TIME = time.time()
    print("Answer:  {}\nTime: {}s".format(ANSWER, END_TIME - START_TIME))
