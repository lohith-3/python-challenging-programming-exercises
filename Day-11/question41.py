# Question 41

# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.Use lambda to define anonymous functions.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solution 1


def square_num(num):
    return num**2


square_list = list(map(square_num, l))
print(square_list)


# Solution 2

square_list_one = list(map(lambda num: num**2, l))
print(square_list_one)
