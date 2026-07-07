# Variable scope determines where a variable can be accessed.

# Global variable
message = "Hello from the global scope"


def show_message():
    # This function can access the global variable
    print(message)


show_message()

# Local variable
def greet():
    name = "Alice"  # Local to this function
    print(f"Hello, {name}!")


greet()

# Uncommenting the next line will raise a NameError
# print(name)

# Local variables in different functions are independent
def first():
    value = 10
    print("First:", value)


def second():
    value = 20
    print("Second:", value)


first()
second()

# Using the global keyword
counter = 0


def increment():
    global counter
    counter += 1


increment()
increment()

print("Counter:", counter)