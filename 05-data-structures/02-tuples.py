# Tuples are ordered and immutable collections.

# Creating tuples
numbers = (10, 20, 30)
colors = ("Red", "Green", "Blue")

print(numbers)
print(colors)

# Access elements
print(numbers[0])
print(numbers[-1])

# Tuple unpacking
name, age = ("Alice", 20)

print(name)
print(age)

# Count occurrences
values = (1, 2, 2, 3, 2)

print(values.count(2))

# Find index
print(values.index(3))

# Loop through a tuple
for value in values:
    print(value)