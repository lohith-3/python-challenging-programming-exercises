# Question 57

# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

# Hints
# Use unicode()/encode() function to convert.


s = input()
u = s.encode('utf-8')
print(u)