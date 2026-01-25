"""
BASIC PYTHON SYNTAX AND CONCEPTS

• print() is used to display output
• Python is case-sensitive
• Variables store data
• Python automatically detects data types
"""


"""
PRINTING OUTPUT
"""

print("Hello world.", "I am the new Python Programmer.")
print("Hi I am Rafik")
print("I am 21 years old.")

print("Sum of 5 + 10 is", 5 + 10)


"""
VARIABLES AND DATA TYPES
"""

name = "Rafi"
roll = 1
class_name = "Ha ha ha"

print("My name is", name, "My roll is", roll, "I read in class", class_name)

print(type(name))
print(type(roll))
print(type(class_name))


"""
BASIC ARITHMETIC OPERATIONS
"""

a = 2
b = 3

sum_result = a + b
difference = a - b
multiplication = a * b
division = a / b

print("Sum:", sum_result)
print("Difference:", difference)
print("Multiplication:", multiplication)
print("Division:", division)

power = a ** b
print("Power:", power)


"""
EXPRESSION EXECUTION WITH STRINGS
"""

A, B = 2, 3
symbol = "@"
word = "AtTheRate"

print(2 * symbol * 3)
print((word + symbol) * A * B)


"""
FLOOR DIVISION
Returns integer part only
"""

A = 15
B = 2
C = A // B
print(C)


"""
MODULUS OPERATOR WITH NEGATIVE NUMBER
Result follows the sign of the divisor
"""

a = 5
b = -2
c = a % b
print(c)


"""
COMMENTS IN PYTHON

• #  → single-line comment
• ''' ''' or \"\"\" \"\"\" → multi-line comment
"""


"""
USER INPUT AND TYPE CASTING
"""

name = input("Name: ")
print("Hi code champ", name)

user_id = int(input("Id: "))
print("Your id is", user_id)

pi = float(input("Pi: "))
print("Value of pi is", pi)
