# Lists are ordered, mutable collections that can store multiple values.

# Creating a list
fruits = ["Apple", "Banana", "Orange"]
print(fruits)

# Access elements
print(fruits[0])
print(fruits[-1])

# Modify an element
fruits[1] = "Mango"
print(fruits)

# Add elements
fruits.append("Grapes")
fruits.insert(1, "Kiwi")
print(fruits)

# Remove elements
fruits.remove("Orange")
last_item = fruits.pop()

print(fruits)
print("Removed:", last_item)

# Check membership
print("Apple" in fruits)

# Loop through a list
for fruit in fruits:
    print(fruit)

# List length
print("Total Fruits:", len(fruits))