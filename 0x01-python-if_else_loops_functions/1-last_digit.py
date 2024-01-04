#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
y = abs(number) % 10
if number < 0:
    y = -y
    if y > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, y))
    elif y == 0:
        print("Last digit of {} is {} and is 0".format(number, y))
    elif x < 6 and x != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, x))
