# Name: Ashwin Sundaresan
# Date: May 14, 2021	
# File Name: 2.2 Day One 5.py	
# Description: A program taht tells the suer whther the integer they inputted
# is positive, negative or neither
# Test cases: 6, -3, 0
# Your integer is positive, Your integer is negative, Your integer is niether
# negative or positive

# Input - User is asked to input an integer
num = int(input("Please enter an integer: "))

# Ourput - Prrgram prints if theinteger is neagtive, positive or neither

# If the integer is greater than 1 this message is disaplayed
if num>=1:
    print("Your integer is positive")

# If the integer is less than 0 this message is disaplayed   
elif num<0:
    print("Your integer is negative")

# If the integer is not greater than 1 and is not less than 0 this
# message is dispalyed
else:
    print("Your number is neither negative or positive")
