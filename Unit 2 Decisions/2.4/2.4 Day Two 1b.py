# Name: Ashwin Sundaresan	
# Date: May 18, 2021
# File Name: 2.4 Day Two 1b.py
# Description: A program that determine which of the three user inputted integers
# is the largest
# Test cases: 5,6,7 and, 6,4,8 and 9,6,3
# 7 is the largest integer, 8 is the largest integer, 9 is the largest integer

# Input - User inputs three integer
x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))
z = int(input("Please enter one more integer: "))

# Output - Program determines and prints which of the 3 integers is the largest
if z > x or y > x:
    
# This code runs if the third integer is the largest
    if z > y:
        print(z,"is the largest integer")
        
# This code runs if the second integer is the largest
    elif y > z:
        print(y,"is the largest integer")
        
# This code runs if the first integer is the largest
elif x > y and x > z:
    print(x,"is the largest integer")



