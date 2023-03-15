# Question 43

# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.Use lambda to define anonymous functions.

# Solution 1

def filter_even_num(num):
    return num % 2 == 0


even_list = list(filter(filter_even_num, range(1, 21)))


# Solution 2

even_list_one = list(filter(lambda num: num % 2 == 0, range(1, 21)))
print(even_list)
print(even_list_one)
