# Question 38

# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

# Hints:
# Use [n1:n2] notation to get a slice from a tuple.
import math

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
half_len = math.trunc(len(t)/2)


print(f"first half: {t[:half_len]}")
print(f"second half: {t[half_len:]}")
