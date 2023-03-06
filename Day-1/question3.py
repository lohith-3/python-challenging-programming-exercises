# Question 2

# With a given integral number n, write a program to generate a
# dictionary that contains (i, i x i) such that is an integral number
# between 1 and n (both included). and then the program should print 
# the dictionary.Suppose the following input is supplied to the 
# program: 8

# Then, the output should be:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Solution 1

user_input = int(input("Please enter your number?\n"))

d = {}

# Solution 1

# def generate_dict(num):
#     for num in range(1, num+1):
#         d.update({num: num*num})

# generate_dict(user_input)
# print(d)

# Solution 2


# def generate_dict(num):
#     for n in range(1, num+1):
#         d[n] = n*n

# generate_dict(user_input)
# print(d)

# Solution 3

my_dict = {num: num**2 for num in range(1, user_input+1)}
print(my_dict)
