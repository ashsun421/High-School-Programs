# Name: Ashwin Sundaresan
# Date: June 21, 2021
# File Name: 5.2 1b.py
# Description: A program that calculates the average of an amount of dice rolls until
# the dice rolls 6

import random

# Process - Creates the lsit and varaibles
x = []
dice = 0

# # Process - Loops the dice roll until a roll of 6 is achieved
while dice != 6:
    dice = random.randint(1,6)

    # Process - Whatever number that has been rolled is added to the list
    x.append(dice)
 
# Output - Prints the list
print(x)

# Process - calcualtes the average of the list
avg = sum(x) / len(x)

# Output - Prints out the average of the list 
print("The average is", round(avg,2))



