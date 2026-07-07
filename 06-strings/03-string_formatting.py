# String formatting creates readable output.

name = "Alice"
age = 20
cgpa = 3.85

# f-string (recommended)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa}")

# Format decimal places
print(f"CGPA: {cgpa:.2f}")

# str.format()
print("Name: {}, Age: {}".format(name, age))

# Positional placeholders
print("{1} scored higher than {0}".format("Bob", "Alice"))

# Formatting numbers
number = 1234567

print(f"{number:,}")