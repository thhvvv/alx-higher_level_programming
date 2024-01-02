#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last digit = number % -10
else:
    lastdigit = number % 10
    if lastdigit > 5:
        print("Last digit of {} is {d} and is graeter than 5".format(number, x))
    elif x == 0:
        print("Last digit of {} is {} and is 0".format(number, x))
elif x < 6 and x != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, x))
