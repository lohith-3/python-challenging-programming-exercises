# Question 42

# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions.


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solution 1


def filter_even_num(ele):
    return ele % 2 == 0


def square_even_num(num):
    return num**2


even_numbers = list(filter(filter_even_num, l))
square_even_list = list(map(square_even_num, even_numbers))
print(square_even_list)


# Solution 2

square_even_list_one = list(
    map(lambda num: num**2, filter(lambda num: num % 2 == 0, l)))

print(square_even_list_one)
