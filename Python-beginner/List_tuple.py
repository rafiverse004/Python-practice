marks1 = 55.55
marks2 = 66.66
marks3 = 77.77
marks4 = 88.88
marks5 = 99.99

"""
we call this a list like array but inside 
that we can store all types together in one list
in string we not change anything but in a list we can change

"""

marks = [55.55, 66.66, 77.77, 88.88, 99.99]
print(marks)
print(type(marks))
print(len(marks))

students = ["Ra", "fi", "kul"]
print(students)
print(type(students))
print(len(students))

"""
list slicing
list_name[starting_index: ending_index]
List methods:

list.append(something)
list.sort()
list.sort(reverse = true)
list.reverse()
list.insert(index, something)

"""
print(marks)
marks.sort(reverse = True)
print(marks)

# Tuple cannot change anything
students1 = (1, 2, 3, 4, 5)
print(students1)

"""
tup.index(element)
tup.count(element)
"""

# Task 1
a = input("Mmovie1: ")
b = input("Movie2: ")
c = input("Movie3: ")

Movies = [a, b, c]
print("Movies: ", Movies)