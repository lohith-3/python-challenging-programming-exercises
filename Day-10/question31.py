# Question 31

# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.

# Solution 1

d = {num: num**2 for num in range(1, 21)}
print(d)

print()
print("--------------")
print()


def generate_dict():
    d = {}
    for num in range(1, 21):
        d[num] = num**2
    print(d)


generate_dict()
