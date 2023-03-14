# Question 33

# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.

# Solution 1
l = [num**2 for num in range(1, 21)]
print(l)

print()
print("--------------")
print()


def generate_list():
    l = []
    for num in range(1, 21):
        l.append(num**2)
    print(l)


generate_list()
