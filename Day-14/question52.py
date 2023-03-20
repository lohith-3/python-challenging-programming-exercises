# Question 52

# Define a custom exception class which takes a string message as attribute.

# Hints
# To define a custom exception, we need to define a class inherited from Exception.

class CustomException(Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


num = int(input())

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is grater than 10")
except CustomException as ce:
    print("The error raised: " + ce.message)


# Another Solution

class TypeError(Exception):
    def __init__(self, message):
        self.message = message


try:
    if not type(num) is str:
        raise TypeError("number must be in string format")
except TypeError as te:
    print(f"error occured {te.message}")
