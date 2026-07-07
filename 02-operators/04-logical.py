# Logical operators combine multiple conditions.

age = 22
has_license = True

# AND returns True if both conditions are True
print("Can Drive:", age >= 18 and has_license)

# OR returns True if at least one condition is True
is_student = False
print("Discount Eligible:", age < 18 or is_student)

# NOT reverses a Boolean value
is_logged_in = False

print("Logged In:", is_logged_in)
print("After NOT:", not is_logged_in)

# Multiple conditions together
marks = 82
attendance = 90

eligible = marks >= 80 and attendance >= 75
print("\nScholarship Eligible:", eligible)

# Logical operators return Boolean values
print(True and False)
print(True or False)
print(not True)