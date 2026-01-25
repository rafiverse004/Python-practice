# Question 1: Create a student dictionary and print all its keys
student = {
    "Id": 242400040,
    "Section": 5,
    "Department": "Cse"
}
print("Dictionary keys:", student.keys())


# Question 2: Update a dictionary value and add a new key-value pair
student = {
    "name": "Alice",
    "age": 17,
    "marks": 85
}
student["marks"] = 90
student["grade"] = "A"
print("Updated dictionary:", student)


# Question 3: Ask the user to enter 5 numbers and store them in a set
my_set = set()
for i in range(5):
    my_set.add(int(input("Enter a number: ")))
print("Your set:", my_set)


# Question 4: Remove a number from a set if it exists, otherwise print "Number not found"
my_set = {1, 2, 3, 4, 5}
num = int(input("Enter a number to remove: "))
if num in my_set:
    my_set.remove(num)
    print("Updated set:", my_set)
else:
    print("Number not found.")


# Question 5: Remove duplicates from a list using a set and convert it back to a sorted list
my_list = [1, 2, 3, 3, 4]
my_set = set(my_list)
my_list = sorted(list(my_set))
print("List after removing duplicates and sorting:", my_list)
