# Question 28

# Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

# Hints:
# Use int() to convert a string to integer.

a = input("Please enter your number?\n")
b = input("Please enter your number?\n")


def sum_two_numbers(num1, num2):
    return int(num1) + int(num2)


sum = lambda a,b: int(a) + int(b)

print()
print(sum_two_numbers(a, b))
print("----------")
print(sum(a,b))