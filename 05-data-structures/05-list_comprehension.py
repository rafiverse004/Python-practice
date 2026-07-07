# List comprehensions provide a concise way to create lists.

# Basic example
numbers = [number for number in range(1, 6)]
print(numbers)

# Squares
squares = [number ** 2 for number in range(1, 6)]
print(squares)

# Filter even numbers
even_numbers = [
    number
    for number in range(1, 11)
    if number % 2 == 0
]

print(even_numbers)

# Convert strings to uppercase
names = ["alice", "bob", "charlie"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)