"""
LISTS IN PYTHON

• Lists are ordered collections
• Lists are mutable (can be changed)
• Can store multiple data types together
• Similar to arrays, but more powerful
• Indexing starts from 0
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
LIST SLICING

Syntax:
list_name[start_index : end_index]

• start_index is inclusive
• end_index is exclusive
"""

print(marks[0:3])
print(marks[2:])


"""
LIST METHODS

list.append(value)        → add at end
list.insert(index, value) → add at specific index
list.sort()               → ascending order
list.sort(reverse=True)   → descending order
list.reverse()            → reverse the list
"""

print(marks)
marks.sort(reverse=True)
print(marks)


"""
TUPLES IN PYTHON

• Tuples are ordered
• Tuples are immutable (cannot be changed)
• Faster than lists
• Written using ()
"""

students1 = (1, 2, 3, 4, 5)
print(students1)
print(type(students1))


"""
TUPLE METHODS

tup.index(element) → returns index
tup.count(element) → count occurrences
"""

print(students1.index(3))
print(students1.count(2))


"""
TASK
Take 3 movie names from user and store them in a list
"""

a = input("Movie 1: ")
b = input("Movie 2: ")
c = input("Movie 3: ")

movies = [a, b, c]
print("Movies:", movies)
