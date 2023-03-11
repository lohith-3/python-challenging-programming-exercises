# Question 18

# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.

# Example

# If the following passwords are given as input to the program:

# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:

# ABd1234@1

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
import re

l = []

while True:
    s = input("Please enter your password?\n")
    if not s:
        break
    l.extend(s.split(","))


def check_password():
    password = []
    for pwd in l:
        if (len(pwd) < 6 or len(pwd) > 12):
            continue
        else:
            pass
        if not re.search("[a-z]", pwd):
            continue
        elif not re.search("[0-9]", pwd):
            continue
        elif not re.search("[A-Z]", pwd):
            continue
        elif not re.search("[$#@]", pwd):
            continue
        else:
            password.append(pwd)
    return password


passwords = check_password()
print(",".join(passwords))
