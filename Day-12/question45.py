# Question 45

# Define a class named American which has a static method called printNationality.

# Hints:
# Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this link.
# https://realpython.com/instance-class-and-static-methods-demystified/


class American:
    def __init__(self):
        print("American Constructor")

    @staticmethod
    def printNationality():
        print("American")


american = American()

# this will not run if @staticmethod does not decorates the function.
# Because the class has no instance.
american.printNationality()

# this will run even though the @staticmethod
# does not decorate printNationality()
American.printNationality()
