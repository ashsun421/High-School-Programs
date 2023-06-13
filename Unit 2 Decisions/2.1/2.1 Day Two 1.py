# Name: Ashwin Sundaresan
# Date: May 13, 2021	
# File Name: 2.1 Day Two 1.py	
# Description: A program that adds 5 the the first numebr inputted
# by the user, only if the second number inputted by the user is greater than 10
# Test cases: 66 and 12, 85 and 11
# 71, 90

# Input - User inputs two numbers
x = int(input("Please enter a number:"))
y = int(input("Please enter another number:"))

# Output - if the second number is greater than 10, 5 is added to the first
# number
if y>10:
    print(int(x+5))
else:
    print(x,y)
