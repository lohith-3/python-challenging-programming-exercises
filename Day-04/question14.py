# Question 14

# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!

# Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input

# ASCII VALUES
# A -> 65
# Z -> 90
# a -> 97
# z -> 122
# 0-9 -> 48-57

user_input = input("Please enter your sentence?\n")
d = {"UPPERCASE": 0, "LOWERCASE": 0, "OTHERS": 0}


# Solution 1

# def check_upper_and_lower(sentence):
#     for char in sentence:
#         if (ord(char) >= 65 and ord(char) <= 90):
#             d["UPPERCASE"] += 1
#         elif (ord(char) >= 97 and ord(char) <= 122):
#             d["LOWERCASE"] += 1
#         else:
#             d["OTHERS"] += 1


# check_upper_and_lower(user_input)
# print(d)

# Solution 2

def check_upper_and_lower(sentence):
    for char in sentence:
        if char.isupper():
            d["UPPERCASE"] += 1
        elif char.islower():
            d["LOWERCASE"] += 1
        else:
            d["OTHERS"] += 1

check_upper_and_lower(user_input)
print(d)