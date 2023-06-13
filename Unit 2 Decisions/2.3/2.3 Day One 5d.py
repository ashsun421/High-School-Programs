# Name: Ashwin Sundaresan
# Date: May 17, 2021	
# File Name: 2.3 Day One 5d.py
# Description: A program to determine if the given integer a multiple of 4 or 7
# Test cases: 16,45
# Your number is a multiple of 4 or 7, Your number is NOT a multiple of 4 or 7

# Input: Gets user input for the integer
x = int(input("Please enter an integer: "))


# Output: Outputs whether or not if the integer is a multiple of 4 or 7
if not((x % 4) == 0 or (x % 7) == 0):
    print("Your number is NOT a multiple of 4 or 7")
    
else:
    print("Your number is a multiple of 4 or 7")
