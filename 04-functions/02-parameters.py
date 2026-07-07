# Parameters allow functions to receive values.

# Function with one parameter
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
greet("Bob")

# Function with multiple parameters
def add(num1, num2):
    print("Sum:", num1 + num2)


print()

add(10, 5)
add(7, 8)

# Default parameter
def introduce(name, country="Bangladesh"):
    print(f"{name} is from {country}.")


print()

introduce("Rafik")
introduce("Alice", "Canada")

# Keyword arguments
print()

introduce(country="Japan", name="Sakura")

# Arbitrary positional arguments
def find_total(*numbers):
    print("Total:", sum(numbers))


print()

find_total(5, 10, 15)
find_total(1, 2, 3, 4, 5)

# Arbitrary keyword arguments
def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


print()

show_profile(name="Alice", age=20, department="CSE")