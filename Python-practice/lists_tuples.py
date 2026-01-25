# Question 1: Add a number to the end of a list, then insert a number at index 2
my_list = [1, 2, 4, 5]
print("Before inserting:", my_list)
my_list.append(6)
my_list.insert(2, 3)
print("After modifications:", my_list)


# Question 2: Remove the last element and remove a number by value from a list
my_list = [1, 2, 3, 4]
my_list.pop()       # removes last element
my_list.remove(2)   # removes value 2
print("After removals:", my_list)


# Question 3: Create a list of 6 numbers and print the sum of the first 3 and last 3 elements
my_list = [10, 20, 30, 40, 50, 60]
sum_first3 = sum(my_list[0:3])
sum_last3 = sum(my_list[3:])
print("Sum of first 3:", sum_first3)
print("Sum of last 3:", sum_last3)


# Question 4: Create a tuple and try to change the second element to observe immutability
my_tuple = (10, 20, 30, 40)
print("Original tuple:", my_tuple)
try:
    my_tuple[1] = 99
except TypeError as e:
    print("Error:", e)


# Question 5: Convert a tuple to a list, add two elements, then convert it back to a tuple
my_tuple = (1, 2, 3, 4)
temp_list = list(my_tuple)
temp_list.append(5)
temp_list.append(6)
my_tuple = tuple(temp_list)
print("Modified tuple:", my_tuple)
