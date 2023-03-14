# Question 6

# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 _ C _ D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a
# comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

# 100,150,180

# The output of the program should be:

# 18,22,24

import math

user_input = input("please enter your numbers?\n")
new_list = user_input.split(",")
c = 50
h = 30

result_list = [
    str(math.trunc(math.sqrt((2 * c * int(num)) / h))) for num in new_list
]
print(",".join(result_list))

print("-------------")


def calculation(nums):
    result = []
    for num in nums:
        val = (2 * c * int(num)) / h
        q = math.trunc(math.sqrt(val))
        result.append(str(q))
    return result


calc_list = calculation(new_list)
print(",".join(calc_list))
