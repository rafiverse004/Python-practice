# Nested data structures contain other collections inside them.

students = [
    {
        "name": "Alice",
        "marks": [80, 85, 90]
    },
    {
        "name": "Bob",
        "marks": [70, 75, 78]
    }
]

# Access nested values
print(students[0]["name"])
print(students[0]["marks"][1])

# Loop through nested data
for student in students:
    print(student["name"])

    for mark in student["marks"]:
        print(mark)

# Nested list
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[1][0])