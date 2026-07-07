# break exits a loop, while continue skips the current iteration.

# Using break
for number in range(1, 11):
    if number == 6:
        break

    print(number)

# Using continue
print()

for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)

# break in a while loop
print()

count = 1

while True:
    if count > 5:
        break

    print(count)
    count += 1

# continue in a while loop
print()

count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)