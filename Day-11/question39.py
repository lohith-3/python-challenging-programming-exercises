# Question 39

# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# Hints:
# Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Solution 1
new_tuple = tuple([even for even in t if even % 2 == 0])
print(new_tuple)

# Solution 2
l = []

for num in t:
    if num % 2 == 0:
        l.append(num)

print(tuple(l))

# Solution 3

even_tuple = tuple(filter(lambda num: num % 2 == 0, t))
print(even_tuple)