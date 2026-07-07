# Recursion is a technique where a function calls itself.

# Recursive countdown
def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)


countdown(5)

print()

# Recursive factorial
def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("Factorial of 5:", factorial(5))

print()

# Recursive sum
def find_sum(number):
    if number == 1:
        return 1

    return number + find_sum(number - 1)


print("Sum:", find_sum(5))