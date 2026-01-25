"""
Dictionaries are used to store data values in key:value pairs
Dictionaries are mutable means can be changed.
"""
info = {
    "key" : "value",
    "name" : "Rafequl Islam",
    "age" : 21,
    "isAdult" : True,
}
print(info)

info1 = {
    "name" : "Rafequl Islam",
    "class" : "cse",
    "courses" : ("DAL", "CAL", "PAL"),
    "marks" : (88.88, 99.99)
}
print(info1)

print(info["name"])

# Add something
info["surname"] = "Islam"
print(info)

# Delete something
del info["key"]
print(info)

# Nested dictionary
student = {
    "Name" : "Rafequl Islam",
    "Subjects" : {
        "Phy" : 99,
        "Chem" : 98
    }
}
print(student)

print("Physics marks: ", student["Subjects"]["Phy"])

"""
Dictionary.keys()
Dictionary.values()
Dictionary.items() this returns all key:value pairs as tuples
Dictionary.get("key"") this returns the key according to the vlaue
Dictionary.update(newDictionary) inserts new

"""

"""
Set in python.
Set is collection of the unordered items.
Each element in the set must be unique and immutable.
"""

nums = {1, 2, 3, 4, "World", "World"}
set1 = { 1, 2, 2, 3, 4}
null_set = set()
print(nums)
print(set1)
print(null_set)
print(len(nums)) # Ignore duplicate items.

"""
set.add(something)
set.remove(something)
set.clear(something)
set.pop(something) removes a random value
set.union(set2)
set.intersection(set2)

"""

# Task 1
info2 = {
    "Table" : ["a piece of furniture", "list of facts and figures"],
    "Cat" : "a small animal"
}
print(info2)

# Task 2
subjects = {"python", "java", "C++", "python", "js", "java", "python", "java", "C++", "c"}
print(len(subjects), "classrooms needed")

# Task 3 : store 3 subjects and marks from the user and add them in the emty dictionary.
Dictionary = {}

key = input("Subject name: ")
Dictionary[key] = input("Marks: ")

key = input("Subject name: ")
Dictionary[key] = input("Marks: ")

key = input("Subject name: ")
Dictionary[key] = input("Marks: ")

print(Dictionary)