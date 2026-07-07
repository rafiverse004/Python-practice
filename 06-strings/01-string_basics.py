# Strings are sequences of characters used to store text.

# Creating strings
first_name = "Rafik"
last_name = 'Ahmed'

print(first_name)
print(last_name)

# Access characters
print(first_name[0])
print(first_name[-1])

# String length
print("Length:", len(first_name))

# Strings are immutable
message = "Python"

# Create a new string instead of modifying the original
message = "J" + message[1:]
print(message)

# Iterate through a string
for character in "Code":
    print(character)

# Check membership
print("Py" in "Python")
print("Java" not in "Python")