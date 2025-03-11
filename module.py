import math

# Using the math module to calculate the square root
print(math.sqrt(144)) 

import random

# Generate a random number between 1 and 6 (like rolling a die)
role_dice = random.randint(1, 6)
print("You rolled dice a", role_dice)

# generating date time

import datetime

date_now = datetime.datetime.now()

#strftime() prints a specific month and even the year

print(date_now.strftime("%U"))