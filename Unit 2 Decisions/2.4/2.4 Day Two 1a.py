# Name: Ashwin Sundaresan	
# Date: May 18, 2021
# File Name: 2.4 Day Two 1a.py
# Description: A program that determine which of the three user inputted integers
# is the smallest
# Test cases: 5,6,7 and, 6,4,7 and 7,6,3
# 5 is the smallest integer, 4 is the smallest integer,
# 3 is the smallest integer

# Input - User inputs three integer
x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))
z = int(input("Please enter one more integer: "))

# Output - Program determines and prints which of the 3 integers is the smallest
if z < x or y < x:
    
# This code runs if the third integer is the smallest
    if z < y:
        print(z,"is the smallest integer")
        
# This code runs if the second integer is the smallest
    elif y < z:
        print(y,"is the smallest integer")
        
# This code runs if the first integer is the smallest
elif x < y and x < z:
    print(x,"is the smallest integer")



