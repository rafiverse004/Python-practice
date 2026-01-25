# Vote age check logic Check whether a person is eligible to vote.

age = int(input("Your age: "))

if age < 18:
    print("You cannot vote yet")
elif age >= 18:
    print("You can vote")
else:
    print("Invalid age")


# Traffic signal logic Decide action based on traffic light color.

light = input("Light (red/yellow/green): ").lower()

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get ready")
elif light == "green":
    print("Go")
else:
    print("Invalid signal")


# Grade calculation Assign grade based on marks.

marks = int(input("Marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: Fail")


"""
TERNARY OPERATOR (ONE-LINE IF-ELSE)

• Used for short conditions
• Cleaner alternative to simple if-else

Syntax:
value_if_true if condition else value_if_false
"""

age = int(input("Age: "))
status = "Adult" if age >= 18 else "Minor"
print(status)


"""
CLEVER / INDEXED TERNARY OPERATOR

• Uses indexing instead of if-else
• True evaluates to 1, False evaluates to 0
• Not recommended for beginners or real projects

Syntax:
(false_value, true_value)[condition]
"""

salary = float(input("Salary: "))

tax = (salary * 0.2, salary * 0.1)[salary <= 50000]
print("Tax:", tax)
