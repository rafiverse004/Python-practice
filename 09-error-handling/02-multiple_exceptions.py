# A try block can handle different types of exceptions.

try:
    number = int(input("Enter a number: "))
    result = 100 / number

    numbers = [10, 20, 30]
    print(numbers[number])

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except IndexError:
    print("Index is out of range.")

print("Program continues...")