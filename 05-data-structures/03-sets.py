# Sets store unique values without maintaining order.

numbers = {1, 2, 3, 4}

print(numbers)

# Add elements
numbers.add(5)

# Duplicate values are ignored
numbers.add(5)

print(numbers)

# Remove elements
numbers.remove(3)

print(numbers)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Membership
print(2 in set1)