# The random module generates random numbers and selections.

import random

# Random integer
print(f"Random integer: {random.randint(1, 10)}")

# Random floating-point number
print(f"Random float: {random.random()}")

# Random choice
colors = ["Red", "Green", "Blue"]

print(f"Random color: {random.choice(colors)}")

# Shuffle a list
numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(f"Shuffled list: {numbers}")

# Random sample
sample = random.sample(numbers, 3)

print(f"Random sample: {sample}")