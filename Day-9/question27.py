# Question 27

# Define a function that can convert a integer into a string and print it in console.

# Hints:
# Use str() to convert a number to string.

number = int(input("Please enter your number?\n"))


def convert_str(num):
    return str(num)


conv = lambda a: str(a)

print()
print(f"Number: {number}, type: {type(convert_str(number))}")
print("-----------")
print(f"Number: {number}, type: {type(conv(number))}")
