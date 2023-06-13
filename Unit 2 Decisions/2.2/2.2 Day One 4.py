# Name: Ashwin Sundaresan
# Date: May 14, 2021	
# File Name: 2.2 Day One 4.py	
# Description: A program that tells the user which number they inputted is
# smaller or if both the numbers they inputted are the same
# Test cases: 6 and 4, 3 and 8, 6 and 6
# 4 is the smaller number, 3 is the smaller number, 6 = 6

# Input - User inputs two numbers
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

# Output - Program prints which number is smaller or if both numbers are equal

# If the first number is smaller than the second number this message is displayed
if  num1>num2:
    print(num2,"is the smaller number")

# If the first number is smaller than the second number this message is displayed    
elif num1<num2:
    print(num1,"is the smaller number")

# If both numbers are equal this message is displayed
else:
    print(num1,"=", num2)
