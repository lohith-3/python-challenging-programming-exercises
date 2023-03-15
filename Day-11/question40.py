# Question 40

# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

# Hints:
# Use if statement to judge condition.

s = input("please type something-->\n")
print("Yes") if (s == "yes" or s == "YES" or s == "Yes") else print("No")


if (s == "yes" or s == "YES" or s == "Yes"):
    print("Yes")
else:
    print("No")
