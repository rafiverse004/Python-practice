# A for loop is used to iterate over a sequence.

# Loop through a range
for number in range(5):
    print(number)

# Specify start and end
print()

for number in range(1, 6):
    print(number)

# Specify step
print()

for number in range(2, 11, 2):
    print(number)

# Loop through a list
fruits = ["Apple", "Banana", "Orange"]

print()

for fruit in fruits:
    print(fruit)

# Loop through a string
print()

for character in "Python":
    print(character)

# Access both index and value
print()

colors = ["Red", "Green", "Blue"]

for index, color in enumerate(colors):
    print(index, color)