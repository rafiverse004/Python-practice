# Membership operators check whether a value exists in a collection.

fruits = ["apple", "banana", "orange"]

print("banana" in fruits)
print("grape" in fruits)

print("grape" not in fruits)

# Membership with strings
message = "Learn Python"

print("\nPython" in message)
print("Java" in message)

# Membership with dictionaries checks keys
student = {
    "name": "Alice",
    "age": 20,
    "department": "CSE"
}

print("\n'name' in student:", "name" in student)
print("'email' in student:", "email" in student)

# Check before accessing a key
if "age" in student:
    print("Age:", student["age"])