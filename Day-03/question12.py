# Question 12

# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.The numbers obtained should be printed
# in a comma-separated sequence on a single line.

# Hints:

# In case of input data being supplied to the question, it should be assumed to be a console input.


def filter_numbers(num):
    if (int(num[0]) % 2 == 0 and int(num[1]) % 2 == 0 and int(num[2]) % 2 == 0 and int(num[3]) % 2 == 0):
        return num


new_list = [str(num) for num in range(2000, 3001)]
filter_result = list(filter(filter_numbers, new_list))

print(",".join(filter_result))
