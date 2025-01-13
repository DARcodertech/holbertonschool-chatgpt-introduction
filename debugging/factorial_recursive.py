#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): The non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the given integer.

    Raises:
        RecursionError: If the recursion depth is exceeded.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


f = factorial(int(sys.argv[1]))
print(f)
