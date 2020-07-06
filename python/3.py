"""
Solution to Project Euler problem 3.
    'What is the largest prime factor of the number 600851475143?'
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
    parser.add_argument('-n',
                        type=int,
                        default=600851475143,
                        help='Number to be factorised')
    args = parser.parse_args()
    return args.n


def find_largest_prime_factor(number):
    """Returns largest prime factor of `number`

    Args:
        number (int) : The number to be factorised

    Returns:
        number (int) : The largest prime factor of `number`
    """
    i = 2
    while i * i < number:
        while number % i == 0:
            number = number / i
        i += 1
    return number


if __name__ == '__main__':
    START_TIME = time.time()

    NUMBER = process_arguments()
    ANSWER = find_largest_prime_factor(NUMBER)

    END_TIME = time.time()
    print("Answer:  {}\nTime: {}s".format(ANSWER, END_TIME - START_TIME))
