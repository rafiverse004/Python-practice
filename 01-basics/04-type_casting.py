# Type casting converts one data type into another.

number = "25"

print(number, type(number))

number = int(number)

print(number, type(number))

price = 99

price = float(price)

print(price, type(price))

marks = 95.75

marks = int(marks)

print(marks, type(marks))

value = 500

value = str(value)

print(value, type(value))

# bool() converts values to True or False.

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))

# Python also performs implicit type conversion.

result = 10 + 5.5

print(result)
print(type(result))