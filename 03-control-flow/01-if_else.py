# if, elif, and else are used to make decisions based on conditions.

age = 20

# Simple if statement
if age >= 18:
    print("You are an adult.")

# if-else statement
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# if-elif-else statement
marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)

# Multiple conditions
username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login successful")
else:
    print("Invalid credentials")

# Nested if statement
temperature = 30
is_raining = False

if temperature > 25:
    if not is_raining:
        print("Good day for a walk.")