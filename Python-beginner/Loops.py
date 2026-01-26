"""
while condition:
    print("Something.")
    increment/decrement if needed
"""

count = 0
while count<5:
    print("Hello.")
    count += 1

i = 1
while i<=100:
    print(i, ": Rafequl Islam")
    i += 1

# Print the multiplication table for a number.
num = int(input("Enter a number: "))
print("Table of ", num)
j = 1
while j<=10:
    print(num, "*", j, "=", num * j)
    j += 1

# Print the elements of the following list using a loop
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Using while loop
index = 0
while index<len(numbers):
    print(numbers[index])
    index += 1

# Using for loop
for n in numbers:
    print(n)

# Search for a number x in this Tuple using loop:
number = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number to search: "))

# Using while loop
found = False
idx = 0

while idx<len(number):
    if number[idx] == x:
        found = True
        index = idx
        break
    idx += 1

if found:
        print("Number found. At index:", idx)
else:
        print("Number not found.")

# Using for loop
found = False
for i in range(len(number)):
    if number[i] == x:
        found = True
        index = i
        break

if found:
        print("Number found. At index:", index)
else:
        print("Number not found.")

