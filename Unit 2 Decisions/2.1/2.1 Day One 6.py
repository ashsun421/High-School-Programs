# Name: Ashwin Sundaresan
# Date: May 13, 2021	
# File Name: 2.1 Day One 6.py	
# Description: A program that tells the user if they are old enough to drive
# Test cases: 16,24,12
# You're old enough to drive, You're old enough to drive,
# You're too young to drive

# Input - User enters their age
age = int(input("How old are you?"))

# Output - Program tells useer if they are allowed to drive

# If age is less than 16 this message is displayed
if age>=16:
    print("You're old enough to drive")

# If age is equal to or greater than 16 this message is displayed
else:
    print("You're too young to drive")
