#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input integer n. If n is 0, returns 1 as 0! is defined to be 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the integer input from command line arguments and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)
