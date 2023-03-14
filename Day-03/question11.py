# Question 11

# Write a program which accepts a sequence of comma separated 4 digit binary numbers as
# its input and then check whether they are divisible by 5 or not. The numbers that are divisible
# by 5 are to be printed in a comma separated sequence.

# Example:

# 0100,0011,1010,1001

# Then the output should be:

# 1010

# Notes: Assume the data is input by console.

# Solution 1

user_input = input("Please enter your binary numbers?\n")
# user_input = "1111,0100,0011,1010,1001"
new_list = user_input.split(",")


# def check_divisible_by5(nums):
#     tmp = []
#     for num in nums:
#         integer = int(num, 2)
#         if (integer % 5 == 0):
#             binary = bin(integer).replace("0b","")
#             tmp.append(binary)
#     return tmp


# divisible_list = check_divisible_by5(new_list)
# print(",".join(divisible_list))


# Solution 2

divisible_list = [num for num in new_list if (int(num, 2) % 5 == 0)]
print(divisible_list)
