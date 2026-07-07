# Dictionaries store data as key-value pairs.

student = {
    "name": "Alice",
    "age": 20,
    "department": "CSE"
}

print(student)

# Access values
print(student["name"])
print(student.get("age"))

# Add or update
student["age"] = 21
student["email"] = "alice@example.com"

print(student)

# Remove a key
student.pop("email")

# Loop through keys and values
for key, value in student.items():
    print(key, value)

# Check if a key exists
print("name" in student)