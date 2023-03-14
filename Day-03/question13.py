# Question 13

# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123

# Then, the output should be:

# LETTERS 10
# DIGITS 3

# Hints:

# In case of input data being supplied to the question, it should be assumed to be a console input.

# ASCII VALUES
# A -> 65
# Z -> 90
# a -> 97
# z -> 122
# 0-9 -> 48-57


# user_input = input("Please enter your text?\n")
user_input = "hello world! 123"
d = {"DIGITS": 0, "LETTERS": 0, "OTHERS": 0}

# Solution 1


# def get_letters_digits(words):
#     for word in words:
#         if (ord(word) >= 65 and ord(word) <= 90):
#             d["LETTERS"] += 1
#         elif (ord(word) >= 97 and ord(word) <= 122):
#             d["LETTERS"] += 1
#         elif (ord(word) >= 48 and ord(word) <= 57):
#             d["DIGITS"] += 1
#         else:
#             d["OTHERS"] += 1


# get_letters_digits(user_input)
# print(d)

# Solution 2

def get_letters_digits(words):
    for word in words:
        if word.isalpha():
            d["LETTERS"] += 1
        elif word.isnumeric():
            d["DIGITS"] += 1
        else:
            d["OTHERS"] += 1


get_letters_digits(user_input)
print(d)
