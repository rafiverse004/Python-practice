# Identity operators check whether two variables refer to the same object.

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)

print("\nlist1 is list3:", list1 is list3)
print("list1 == list3:", list1 == list3)

# None comparisons should use 'is'
user = None

print("\nUser is None:", user is None)
print("User is not None:", user is not None)

# Identity compares memory reference, not value
number1 = 100
number2 = 100

print("\nnumber1 == number2:", number1 == number2)
print("number1 is number2:", number1 is number2)