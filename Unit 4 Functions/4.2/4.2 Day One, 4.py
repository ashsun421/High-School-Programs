# Name: Ashwin Sundaresan
# Date: June 8, 2021
# File Name: 4.2 Day One, 4.py
# Description: A program that prints out the time for an object,
# thrown with velocity v from an initial height h, to hit the ground 

import math

# Creteas the function
def find_time(v,h):

    # Process - Solves for the possible time
    time = ((-1) * v - (math.sqrt(v ** 2 - (4 * -4.9 * h)))) / -9.8

    
    return time

# Main Function
t = find_time(10, 1)

# Outputs - Prints out the time when the boject hits the ground
print(round(t,2))
