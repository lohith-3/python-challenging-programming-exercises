# Question 51

# Write a function to compute 5/0 and use try/except to catch the exceptions.

# Hints
# Use try/except to catch exceptions.

try:
    result = 5 / 0
    print(result)
except ZeroDivisionError as err:
    print("cannot divide a number by 0")
except:
    print("some error occured")
