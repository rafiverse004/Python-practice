# Read data from a text file.

# Read the entire file
file = open("sample.txt", "r")

content = file.read()
file.close()

print("Entire file:")
print(content)

# Read line by line using with
print("\nReading line by line:")

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read all lines into a list
with open("sample.txt", "r") as file:
    lines = file.readlines()

print("\nList of lines:")
print(lines)