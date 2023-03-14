# Question 16

# Use a list comprehension to square each odd number in a list. The list is input by a
# sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

# 1,2,3,4,5,6,7,8,9

# Then, the output should be:

# 1,9,25,49,81

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

user_input = input("Please enter your numbers?\n")
# user_input = "1,2,3,4,5,6,7,8,9"

# Solution 1

# new_list = [str(int(num)**2)
#             for num in user_input.split(",") if (int(num) % 2 != 0)]
# print(",".join(new_list))

# Solution 2

tmp = []
for num in user_input.split(","):
    if int(num) % 2 != 0:
        tmp.append(str(int(num)**2))

print(",".join(tmp))
