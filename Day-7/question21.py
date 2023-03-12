# Question 21

# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
# with a given steps. The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a
# sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example: If the following tuples are given as input to the program:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:

# 2

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Here distance indicates to euclidean distance.Import math module to use sqrt function.

# UP -> - , x
# DOWN -> + , x
# LEFT -> - , y
# RIGHT -> + , y

import math

x, y = 0, 0

while True:
    s = input("Please enter your directions or Quit? D/Q\n")
    if s.lower() == 'q':
        break
    command, unit = s.split(" ")
    if command.lower() == 'up':
        x -= int(unit)
    if command.lower() == 'down':
        x += int(unit)
    if command.lower() == 'left':
        y -= int(unit)
    if command.lower() == 'right':
        y += int(unit)

# N**P means N^P
# euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
dist = round(math.sqrt(x**2 + y**2))
print(dist)
