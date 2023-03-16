# Question 44

# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list. Use lambda to define anonymous functions.


def square_num(num):
    return num ** 2


new_list = list(map(square_num, range(1, 21)))

print(new_list)
print("-----------")
print(list(map(lambda num: num**2, range(1, 21))))
