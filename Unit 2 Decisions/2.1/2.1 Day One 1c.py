# Name: Ashwin Sundaresan
# Date: May 13, 2021	
# File Name: 2.1 Day One 1c.py
# Description: A program that can output if an integer is greater,
# less or equal to 10
# Test cases: 13,11,10
# HIGHER, LOWER, EQUAl

# Input - User is asked to input any integer
number = int(input("Input an integer:"))

# Output - Prints if the user inputted integer is higher,
# lower or equal to 10

# If the integer  is greater than 10, HIGHER is printed
if number>10:
    print("HIGHER")

# If the integer is lower than 10, LOWER is printed
if number<10:
    print("LOWER")

# If the integer is equal to 10, EQUAL is printed
else:
    print("EQUAL")
