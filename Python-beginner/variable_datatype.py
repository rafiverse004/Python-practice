print("Hello world.", "I am the new Python Programmer.")
print("Hi i am rafik")
print("I am 21 years old.")

print("Sum of 5 + 10 is", 5+10)

Name = "Rafi"
Roll = 1
Class = "Ha ha ha"
print("My name is", Name, "My roll is", Roll, "I read in Class", Class)

#Finding data types by computer
print(type(Name))
print(type(Roll))
print(type(Class))

#Sum, devide, subtract, multiply of two numbers
a = 2
b = 3
sum = a + b
difference = a - b
multiply = a * b
devide = a / b
print("Sum: ", sum)
print("Difference: ", difference)
print("Multiplication: ", multiply)
print("Devide: ", devide)

c = a**b # a to the power b
print(c)

#Expression Execution
A,B = 2,3
text = "@"
text1 = "AtTheRate"
print(2*text*3) #so we can multiply string with int
print((text1+text)*A*B) #we can add string with +

# using A//B will round up smaller or equal int number
A = 15
B = 2
C = A // B
print(C)

a = 5
b = -2
c = a % b # a plus b minus that is why c is minus other way all plus
print(c)

# Single line commnet
"""This is multi line comment 
    in Python"""

# Taking input from the user
name = input("Name: ")
print("Hi our code champ ", name)

id = int(input("Id: "))
print("Code champ we are giving you a id ", id)

pi = float(input("Pi: "))
print("Code champ do you know the value of pi is ", pi)

