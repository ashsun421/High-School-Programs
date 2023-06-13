# Name: Ashwin Sundaresan
# Date: May 17, 2021	
# File Name: 2.3 Day One 5b.py
# Description: A program that determines whether the given integer is
# divisible by 3 or 5.
# Test cases: 15, 11
# Your number is divisible by 3 or 5, Your number is not divisible by 3 or 5

# Input - Gets user input for integer 
x = int(input("Please enter an integer: "))

# Output - Outputs if the value of x is divisible by both 3 and 5 or not
if (x%3) == 0 or (x%5) == 0:
    print("Your number is divisible by 3 or 5")
else:
    print("Your number is not divisible by 3 or 5")
