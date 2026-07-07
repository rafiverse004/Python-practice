# Functions allow you to group reusable code into a single block.

# Define a simple function
def greet():
    print("Hello!")
    print("Welcome to Python.")


# Call the function
greet()

# Functions can be called multiple times
print()

greet()
greet()

# Functions can perform different tasks
def display_line():
    print("-" * 30)


print()

display_line()
print("Menu")
display_line()

# A function can contain any valid Python code
def show_even_numbers():
    for number in range(2, 11, 2):
        print(number)


print()

show_even_numbers()