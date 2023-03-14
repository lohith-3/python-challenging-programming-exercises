# Question 1

# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).The
# numbers obtained should be printed in a comma-separated sequence on a
# single line.

# Solution 1

# for num in range(2000, 3200+1):
#     if (num % 7 == 0 and num % 5 != 0):
#         print(num, end=", ")

# Solution 2

# li = []
# for num in range(2000, 3200+1):
#     if (num % 7 == 0 and num % 5 != 0):
#         li.append(str(num))

# str_list = ",".join(l)
# print(str_list)
# print(",".join(li))

# Solution 3

li = [str(num) for num in range(2000, 3200+1) if (num % 7 == 0 and num % 5 != 0)]
print(",".join(li))
