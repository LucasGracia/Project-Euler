"""
Solution to Project Euler problem 1.
    'Find the sum of all the multiples of 3 or 5 below 1000'
"""
__author__ = 'Lucas Gracia'
__version__ = '1.0.0'
__license__ = 'MIT'

import time
import argparse


def process_arguments():
    """Processes user-entered command line arguments

    Returns:
        args.l (int) : The limit to be passed to `sum_multiples`
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', type=int, default=1000, help='Sum limit')
    args = parser.parse_args()
    return args.l


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

    LIMIT = process_arguments()
    ANSWER = sum_multiples(LIMIT)

    END_TIME = time.time()
    print("Answer: {}\nTime: {}s".format(ANSWER, END_TIME - START_TIME))
