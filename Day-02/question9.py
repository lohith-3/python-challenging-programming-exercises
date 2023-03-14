# Question 9

# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# Suppose the following input is supplied to the program:

# Hello world
# Practice makes perfect

# Then, the output should be:

# HELLO WORLD
# PRACTICE MAKES PERFECT

# Solution 1

# lines = []

# while True:
#     user_ip = input()
#     if user_ip:
#         lines.append(user_ip)
#     else:
#         break

# for line in lines:
#     print(line.upper())

# Solution 2

lines = []

while True:
    user_ip = input()
    if len(user_ip) == 0:
        break
    lines.append(user_ip)

for line in lines:
    print(line.upper())