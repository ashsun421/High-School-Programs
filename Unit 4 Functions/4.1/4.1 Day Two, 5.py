# Name: Ashwin Sundaresan
# Date: June 7, 2021
# File Name: 4.1 Day Two, 5.py
# Description: A pgroram that prints the area of a triganle given the a, b and
# c values
# Test Cases: 3,4,5
# Area is: 6.0

import math

# Cretas the function
def area(a,b,c):
    z = ((a + b + c) / 2)
    area = math.sqrt(z * (z - a) * (z - b) * (z - c))
    print("Area is:", area)

# Main Function
area(3,4,5)
