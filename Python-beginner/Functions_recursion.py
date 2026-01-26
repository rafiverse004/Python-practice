def cal_sum(a, b):
    sum = a + b
    print(sum) # We can print
    return sum # We can return

print(cal_sum(2, 5))

def print_something():
    print("Something...")

print_something()
print_something()

# Recursion:

def show(n):
    if n == 0: # Base case wherer to stop
        return
    print(n)
    show(n-1) # Condition whatever we want to do

show(5)

# Task 1: Factorial
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(5))

# Task 2: Sum of n numbers
def sum_n(n):
    if(n==0):
        return 0
    return sum_n(n-1) + n

print(sum_n(5))

# Task 3: Fibonacci number series
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(5))

# Task 4: Palindrome check(String)
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("radar"))

# Task 5: Power function (a^b)
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print(power(2, 5))