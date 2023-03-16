# Question 46

# Define a class named American and its subclass NewYorker.

# Hints:
# Use class Subclass(ParentClass) to define a subclass.*


class American():
    def __init__(self):
        print("Parent/Base class American")


class NewYorker(American):
    def __init__(self):
        print("Child/sub class New Yorker")


newYorker = NewYorker()
