"""
DICTIONARY (dict)

• Stores data in key:value pairs
• Keys must be unique and immutable (int, string, tuple)
• Values can be any data type
• Dictionaries are mutable
• Access values using keys
• Supports nesting (dictionary inside dictionary)

Common methods:
dict.keys()        -> returns all keys
dict.values()      -> returns all values
dict.items()       -> returns key:value pairs as tuples
dict.get(key)      -> safe access (no error if key missing)
dict.update(dict2) -> add or update key:value pairs
"""

"""
SET

• Unordered collection of unique elements
• Duplicate values are automatically removed
• Elements must be immutable
• Sets are mutable
• Used for uniqueness and set operations

Common methods:
set.add(value)
set.remove(value)      -> error if value not found
set.discard(value)     -> no error if value not found
set.clear()
set.pop()              -> removes a random element
set.union(set2)
set.intersection(set2)
"""


# Dictionary examples


info = {
    "key": "value",
    "name": "Rafequl Islam",
    "age": 21,
    "isAdult": True
}
print(info)


info1 = {
    "name": "Rafequl Islam",
    "class": "CSE",
    "courses": ("DAL", "CAL", "PAL"),
    "marks": (88.88, 99.99)
}
print(info1)

print(info["name"])


# Add and delete dictionary elements

info["surname"] = "Islam"
print(info)

del info["key"]
print(info)


# Nested dictionary

student = {
    "Name": "Rafequl Islam",
    "Subjects": {
        "Phy": 99,
        "Chem": 98
    }
}
print(student)
print("Physics marks:", student["Subjects"]["Phy"])


# Set examples


nums = {1, 2, 3, 4, "World", "World"}
set1 = {1, 2, 2, 3, 4}
null_set = set()

print(nums)
print(set1)
print(null_set)
print(len(nums))


# Tasks

info2 = {
    "Table": ["a piece of furniture", "list of facts and figures"],
    "Cat": "a small animal"
}
print(info2)


subjects = {"python", "java", "C++", "python", "js", "java", "python", "java", "C++", "c"}
print(len(subjects), "classrooms needed")


marks_dict = {}

key = input("Subject name: ")
marks_dict[key] = input("Marks: ")

key = input("Subject name: ")
marks_dict[key] = input("Marks: ")

key = input("Subject name: ")
marks_dict[key] = input("Marks: ")

print(marks_dict)
