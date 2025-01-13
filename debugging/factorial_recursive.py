#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer recursively.

    Parameters:
        n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the given number. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieve the first command-line argument, convert it to an integer, and calculate the factorial.
f = factorial(int(sys.argv[1]))

# Print the calculated factorial.
print(f)

