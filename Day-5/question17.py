# Question 17

# Write a program that computes the net amount of a bank account based a transaction log from
# console input. The transaction log format is shown as following:

# D 100
# W 200

# D means deposit while W means withdrawal.

# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100

# Then, the output should be:

# 500

# Solution 1

account = 0

while True:
    user_input = input("Deposit/Withdraw/Balance/Quit: D/W/B/Q?\n")
    if user_input.lower() == 'd':
        account = int(input("How much you would like to deposit?\n"))
    elif user_input.lower() == 'w':
        withdraw = int(input("How much you would like to withdraw?\n"))
        if withdraw < account:
            account -= withdraw
        else:
            print("Insufficient funds")
    elif user_input.lower() == 'b':
        print(f"You're remaining balance: {account}")
    else:
        break


# text = "D 500"
# print(text.strip("D "))

# Solution 2

# while True:
#     user_input = input("What action you want to perform: D/B/W/Q?\n")
#     if 'D' in user_input:
#         deposit = user_input.strip("D ")
#         account += int(deposit)
#     elif "W" in user_input:
#         withdraw = user_input.strip("W ")
#         if int(withdraw) < account:
#             account -= int(withdraw)
#         else:
#             print("Insufficient funds")
#     elif "B" in user_input:
#         print(f"You're remaining balance: {account}")
#     else:
#         break
