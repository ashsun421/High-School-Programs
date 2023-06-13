# Name: Ashwin Sundaresan
# Date: June 9, 2021
# File Name: 4.2 Day two, 3.py
# Description: A program that pritns out the two possible values
# after solving the quadratic formula

import math

# Process - Creeats the Function
def roots(a,b,c):
    try:
        # Process - Calculates the values when you add the square and when
        # you subtract the square root
        add = (-1*b + (math.sqrt(b ** 2 - (4*a*c))))/ 2*a
        minus = (-1*b - (math.sqrt(b ** 2 - (4*a*c))))/ 2*a

        # Output - Prints out both values 
        print(round(add,2),"and",round(minus,2))
        
    except:

        # This line is run if the given variables cannot be solved
        print("Error")

# Main Program       
roots(1,-4,4)
roots(1,3,-5)
roots(1,1,1)
