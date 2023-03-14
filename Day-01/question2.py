# Question 2

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single
# line.Suppose the following input is supplied to the program: 8 Then,
# the output should be:40320

# Hints

# In case of input data being supplied to the question, it should 
# be assumed to be a console input.

from functools import reduce

user_input = int(input("Please enter the number?\n"))

# Solution 1


# def factorial(num):
#     fact_result = 1
#     while num != 0:
#         fact_result *= num
#         num -= 1
#     return fact_result

# print(factorial(user_input))


# Solution 2

# def factorial(num):
#     fact_result = 1

#     for num in range(1, num+1):
#         fact_result *= num
#     return fact_result

# print(factorial(user_input))

# Solution 3

def factorial(acc, num):
    return acc * num


fact_result = reduce(factorial, range(1, user_input+1), 1)
print(fact_result)
