# Question 1: Count the number of vowels in a given string
word = input("Enter one line: ")
vowels = "aeiouAEIOU"
count = 0
for char in word:
    if char in vowels:
        count += 1
print("Number of vowels:", count)


# Question 2: Ask for a number and check divisibility by 3 and/or 5
num = int(input("Enter any number: "))
if num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by 3 and 5")
elif num % 3 == 0:
    print(num, "is divisible by 3")
elif num % 5 == 0:
    print(num, "is divisible by 5")
else:
    print(num, "is not divisible by 3 or 5")


# Question 3: Ask for a number and print whether it is positive, negative, or zero
num = int(input("Enter a number: "))
if num < 0:
    print(num, "is negative")
elif num > 0:
    print(num, "is positive")
else:
    print(num, "is zero")


# Question 4: Ask for age and print if the user can vote or not
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")


# Question 5: Ask the user for a string and check if it is a palindrome
text = input("Enter a word: ")
clean_text = text.replace(" ", "").lower()
if clean_text == clean_text[::-1]:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
