# Question 32

# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

# Solution 1

d = {num: num**2 for num in range(1, 21)}
print(d.keys())

print()
print("---------")
print()


def generate_dict():
    d = {}
    for num in range(1, 21):
        d[num] = num**2
    print(d.keys())


generate_dict()
