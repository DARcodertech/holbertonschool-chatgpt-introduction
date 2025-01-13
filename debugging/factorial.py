#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

if len(sys.argv) > 1:  # Ensure an argument is provided
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Please provide a valid integer as an argument.")
else:
    print("Usage: ./factorial.py <number>")
