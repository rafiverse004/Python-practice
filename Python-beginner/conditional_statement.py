# if elif else

# Vote age check logic
age = int(input("Your age: "))
if age<18:
    print("You can not vote for now")
    print("Wait to become 18 kiddo")
elif age>18: # this is just sort form of else-if
    print("You can vote sir.")
    print("You are good to go old people")
else:
    print("Wrong command, try again, No thank you")

# Signal light logic
light = input("Light: ")
if (light == "red"):
    print("You can not go.")
elif (light == "yellow"):
    print("Prepare yourself within few second you are good to go")
elif (light == "green"):
    print("You can go now")
else:
    print("Light is broken ha ha ha")

# Grades of student
mark = int(input("marks: "))
if(mark>=90):
    print("A")
elif(mark>=80 and mark<90):
    print("B")
else:
    print("Fail.")

"""Ternary operator
    <variable> = <vablue1> if<condition> else<value2>

    print(str1) if(condition) else(str2)
"""

"""Cleaver if / ternary operator
    <variable> = (false_value, true_value) [condition]
"""

salary = float(input("Salary: "))
tax = salary*(0.1, 0.2) [salary<=50000]
print(tax)

