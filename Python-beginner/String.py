"""
STRINGS IN PYTHON

• Strings are sequences of characters
• Strings are immutable (cannot be changed)
• Indexed starting from 0
• Supports slicing
"""

str1 = "Rafikul "
str2 = "Islam"

print("My name is", str1 + str2)
print("Length of str1:", len(str1))
print("Length of str2:", len(str2))


"""
STRING INDEXING

• You can access characters
• You cannot modify them
"""

char = str1[0]
print("First character:", char)


"""
STRING SLICING

Syntax:
string[start_index : end_index]

• start is inclusive
• end is exclusive
"""

print("Slice [0:4]:", str1[0:4])


"""
NEGATIVE INDEXING

• Starts from -1 (last character)
"""

print("Negative slice [-4:-1]:", str1[-4:-1])


"""
COMMON STRING METHODS

str.endswith("text")
str.capitalize()
str.replace(old, new)
str.find("word")
str.count("char")
"""

print("Count of 'a':", str1.count("a"))


"""
USER INPUT STRING
"""

text = input("Enter a line: ")
print(text)
print("Length:", len(text))
