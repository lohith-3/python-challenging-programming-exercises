# Question 30

# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

# Hints:
# Use len() function to get the length of a string.

str1 = input("Please enter your string?\n")
str2 = input("Please enter your string?\n")


def getMaximumStr(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    if str1_len == str2_len:
        return f"both strings are equal"
    if str1_len > str2_len:
        return f"str1: {str1} length: {str1_len} is greater than str2: {str2}"
    if str2_len > str1_len:
        return f"str2: {str2} length: {str2_len} is greater than str1: {str1}"


print(getMaximumStr(str1, str2))
