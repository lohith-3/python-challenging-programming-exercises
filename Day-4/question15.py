# Question 15

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# Suppose the following input is supplied to the program:

# 9

# Then, the output should be:

# 11106

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution 1

# user_input = input("Please enter your number?\n")
# total, tmp = 0, str()

# for i in range(4):
#     tmp += user_input
#     total += int(tmp)

# print(total)

# Solution 2
# N*a = Na

user_input = input("Please enter your number?\n")
total = int(user_input) + int(user_input*2) + \
    int(user_input*3) + int(user_input*4)
print(total)
