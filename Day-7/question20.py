# Question 20

# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Suppose the following input is supplied to the program:

# 7

# Then, the output should be:

# 0
# 7
# 14

# Hints:
# Consider use class, function and comprehension.

class Divisible:
    def by_seven(self, n):
        for number in range(1, n+1):
            if number % 7 == 0:
                yield number


divisible = Divisible()
generator = divisible.by_seven(int(input("Please enter your number?\n")))
for num in generator:
    print(num)
