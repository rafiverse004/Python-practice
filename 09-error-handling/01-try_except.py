# Use try-except to handle errors gracefully.

# Handling division by zero
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Handling invalid user input
try:
    age = int(input("\nEnter your age: "))
    print(f"You entered: {age}")
except ValueError:
    print("Please enter a valid integer.")

# Program continues even after an exception
print("\nProgram finished successfully.")