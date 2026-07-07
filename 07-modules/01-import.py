# Modules allow you to reuse code from other Python files or built-in libraries.

# Import an entire module
import math

print(f"Square root of 25: {math.sqrt(25)}")

# Import specific functions
from math import pi, factorial

print(f"Value of pi: {pi}")
print(f"Factorial of 5: {factorial(5)}")

# Import with an alias
import random as rnd

print(f"Random number: {rnd.randint(1, 10)}")

# Import multiple functions
from math import ceil, floor

number = 7.8

print(f"Ceiling: {ceil(number)}")
print(f"Floor: {floor(number)}")