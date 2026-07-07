# Lambda functions are small anonymous functions written in a single line.

# Basic lambda function
square = lambda number: number ** 2

print(square(5))

# Lambda with multiple parameters
multiply = lambda num1, num2: num1 * num2

print(multiply(4, 6))

# Using lambda with sorted()
students = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 91)
]

print()

sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)

# Using lambda with map()
numbers = [1, 2, 3, 4]

doubled = list(map(lambda number: number * 2, numbers))

print(doubled)

# Using lambda with filter()
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(even_numbers)