# The return statement sends a value back to the caller.

# Return a single value
def square(number):
    return number ** 2


result = square(5)
print(result)

# Return multiple values
def calculate(num1, num2):
    return num1 + num2, num1 * num2


sum_result, product_result = calculate(4, 6)

print("Sum:", sum_result)
print("Product:", product_result)

# Return a Boolean value
def is_even(number):
    return number % 2 == 0


print()
print(is_even(8))
print(is_even(11))

# Return early
def check_age(age):
    if age < 18:
        return "Not eligible"

    return "Eligible"


print()
print(check_age(16))
print(check_age(20))