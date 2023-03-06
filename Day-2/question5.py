# Question 5

# Define a class which has at least two methods:

# -> getString: to get a string from console input
# -> printString: to print the string in upper case.

# Also please include simple test function to test the class methods.

# Hints

# Use init method to construct some parameters


class InputOutputString():

    def __init__(self):
        self.user_input = ""

    def getString(self):
        self.user_input = input("Please enter text\n")

    def printString(self):
        print(self.user_input.upper())


io = InputOutputString()
io.getString()
io.printString()
