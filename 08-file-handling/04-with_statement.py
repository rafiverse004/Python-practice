# The with statement automatically closes a file after use.

# Reading a file
with open("sample.txt", "r") as file:
    content = file.read()

print(content)

# Writing to another file
with open("notes.txt", "w") as file:
    file.write("This file was created using the with statement.\n")

print("\nnotes.txt created successfully.")

# The file is automatically closed after leaving the block.