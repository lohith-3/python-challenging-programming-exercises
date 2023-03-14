# Question 29

# Define a function that can accept two strings as input and concatenate them and then print it in console.

# Hints:
# Use + sign to concatenate the strings.

str1 = input("Please enter your string?\n")
str2 = input("Please enter your string?\n")


def concat_str(a, b):
    return str1+" "+str2

concat = lambda a,b: a+" "+b

print()
print(concat_str(str1, str2))
print("-----")
print(concat(str1,str2))