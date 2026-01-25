# Question 1: Create integer, float, and string variables, then print their types
integer = 1234
float_num = 12.34
string_val = "Hello World"

print(type(integer))
print(type(float_num))
print(type(string_val))


# Question 2: Swap the values of two variables without using a temporary variable
variable1 = 1234
variable2 = 4321

print("Before swap:", variable1, variable2)
variable1, variable2 = variable2, variable1
print("After swap:", variable1, variable2)


# Question 3: Convert a number to a string and print the type before and after conversion
number = 1234
print("Before conversion:", type(number))
number_str = str(number)
print("After conversion:", type(number_str))


# Question 4: Create variables for name, age, and favorite color, then print a sentence using them
name = "Rafequl Islam"
age = 21
fav_color = "Black"
print("My name is", name, ". I am", age, "years old. My favorite color is", fav_color)


# Question 5: Ask the user for a number and print its square and cube
number = int(input("Enter a number: "))
print("Square:", number ** 2)
print("Cube:", number ** 3)
