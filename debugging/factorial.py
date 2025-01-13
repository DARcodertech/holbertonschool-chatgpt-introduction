#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
    return result

f = factorial(int(sys.argv[1]))
print(f)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <number>")
    else:
        try:
            num = int(sys.argv[1])
            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                f = factorial(num)
                print(f)
        except ValueError:
            print("Please provide a valid integer.")
