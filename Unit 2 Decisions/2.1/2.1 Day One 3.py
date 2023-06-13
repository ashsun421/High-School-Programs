# Name: Ashwin Sundaresan
# Date: May 13, 2021	
# File Name: 2.1 Day One 3.py	
# Description: A program to tells the user which of the two numbers they
# have inputted is bigger
# Test cases: 99 and 98, 98 and 99, 50 and 25, 25 and 50
# 99 is the bigger number, 99 is the bigger number, 50 is the bigger number
# 50 is the bigger number

# Input - User inputs two different numbers
number = int(input("Please enter a number:"))
number2 = int(input("Please enter a different number:"))

# Output - Program prints which number is bigger

# If the first number is greater than the second number this message is printed
if number>number2:
    print(number,"is the bigger number")
    
# If the second number is greater than the first number this message is printed
else:
    print(number2,"is the bigger number")
   
