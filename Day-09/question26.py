# Question 26

# Define a function which can compute the sum of two numbers.

# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

a = int(input("Please enter your number?\n"))
b = int(input("Please enter your number?\n"))

# Solution 1


def sum_two_numbers(num1, num2):
    return num1 + num2

# Solution 2


def sum(a, b): return a+b


print(" ")
print(sum_two_numbers(a, b))
print("-------------------")
print(sum(a, b))
