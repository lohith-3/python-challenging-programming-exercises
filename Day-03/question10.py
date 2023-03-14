# Question 10

# Write a program that accepts a sequence of whitespace separated words as input and prints the
# words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again

# Then, the output should be:

# again and hello makes perfect practice world

# Solution 1

user_input = input("Please enter your text?\n")
new_list = user_input.split(" ")


# def remove_duplicates(words):
#     tmp = []
#     for word in words:
#         if tmp.count(word) == 0:
#             tmp.append(word)
#     return sorted(tmp)

# sorted_list = remove_duplicates(new_list)
# print(" ".join(sorted_list))

# Solution 2

def remove_duplicates(words):
    tmp = []
    for word in words:
        if word not in tmp:
            tmp.append(word)
    return sorted(tmp)


sorted_list = remove_duplicates(new_list)
print(" ".join(sorted_list))
