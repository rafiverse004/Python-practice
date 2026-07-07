# input() is used to take input from the user.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))

# print() displays output on the screen.

print("\nStudent Information")
print("-------------------")
print("Name :", name)
print("Age  :", age)
print("CGPA :", cgpa)

# f-strings make formatting easier.

print(f"\n{name} is {age} years old.")

# sep changes the separator.

print("Python", "Java", "C++", sep=" | ")

# end changes the ending character.

print("Hello", end=" ")
print("World")