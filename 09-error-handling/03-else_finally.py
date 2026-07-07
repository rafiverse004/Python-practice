# else runs when no exception occurs, and finally always runs.

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid integer.")

else:
    print(f"Result: {result}")

finally:
    print("Execution completed.")