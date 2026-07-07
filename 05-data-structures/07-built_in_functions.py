# Python provides useful built-in functions for working with collections.

numbers = [12, 5, 8, 20, 15]

print("Length:", len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))

# Sort without changing the original list
print("Sorted:", sorted(numbers))

# Reverse iteration
print("Reversed:", list(reversed(numbers)))

# Enumerate values with indexes
for index, value in enumerate(numbers):
    print(index, value)

# Combine two collections
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]

for name, score in zip(names, scores):
    print(name, score)

# Check boolean conditions
values = [True, True, False]

print("Any:", any(values))
print("All:", all(values))