# Question 35

# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list

l = [num**2 for num in range(1, 21)]
print(l[-5:])
print(l[:-6:-1])

print()
print("-------")
print()


def generate_list():
    l = []
    for num in range(1, 21):
        l.append(num**2)
    print(l[-5:])
    print(l[:-6:-1])


generate_list()
