# Question 37

# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use tuple() to get a tuple from a list.

# Solution 1

l = [num**2 for num in range(1, 21)]
print(tuple(l))

print()
print("--------")
print()

# Solution 2


def generate_tuple():
    l = []
    for num in range(1, 21):
        l.append(num**2)
    print(tuple(l))


generate_tuple()
