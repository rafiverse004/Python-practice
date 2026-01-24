str1 = "Rafikul "
str2 = "Islam"

print("My name is ", str1 + str2)
print(len(str1))
print(len(str2))

# we can access any word but can change anything
str3 = str1[0]
print(str3)

# string slicing
print(str1[0:4])

# special string in python only negative indexing
print(str1[-4:-1])

"""
str.endswith("")
str.capitalize("")
str.replace(old, new)
str.find(word)
str.count("")

"""

print(str1.count("a"))

str = input("Enter a line: ")
print(str)
print("Length: ", len(str))