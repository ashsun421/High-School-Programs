# Name: Ashwin Sundaresan
# Date: June 7, 2021
# File Name: 4.1 Day Two, 6.py
# Description: A pgroam that will determines the measures
# of the angle opposite side a in a triangle given side lengths a, b, and c
# Test Cases: 3,4,5 and 4,3,5 and 5,4,3
# The angle is 37 degrees
# The angle is 53 degrees
# The angle is 90 degrees

import math

# Creteas the function
def angle(a,b,c):
    cosLaw = (((b**2) + (c**2)) - a**2) / (2*b*c)
    a = round(math.degrees(math.acos(cosLaw)))
    print("The angle is", a, "degrees")

# Main Function
angle(3,4,5)

# Main Function
angle(4,3,5)

# Main Function
angle(5,4,3)
    
