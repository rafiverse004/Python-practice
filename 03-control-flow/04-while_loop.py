# A while loop runs as long as its condition remains True.

count = 1

while count <= 5:
    print(count)
    count += 1

# User-controlled loop
print()

password = ""

while password != "python":
    password = input("Enter password: ")

print("Access granted.")

# Infinite loop with break
print()

number = 1

while True:
    print(number)
    number += 1

    if number > 3:
        break