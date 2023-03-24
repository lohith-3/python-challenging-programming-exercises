# Question 55

# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

# Example: If the following words is given as input to the program:

# 2 cats and 3 dogs.
# Then, the output of the program should be:

# ['2', '3']
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints
# Use re.findall() to find all substring using regex.

s = "2 cats and 3 dogs"
s_list = s.split(" ")


new_list = []

for char in s_list:
    if char.isnumeric():
        new_list.append(char)


print(new_list)
