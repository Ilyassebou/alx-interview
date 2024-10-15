#!/usr/bin/python3

"""
    Calculates minimum operations to reach n H characters.
"""

def minOperations(num_chars):
    """ Returns fewest operations to get num_chars H characters. """
    operation_count = 0
    divisor = 2

    if num_chars <= 1:
        return 0
    while num_chars != 1:
        if num_chars % divisor == 0:
            num_chars //= divisor
            operation_count += divisor
        else:
            divisor += 1
    return operation_count
