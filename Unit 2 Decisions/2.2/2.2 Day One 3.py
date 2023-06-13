# Name: Ashwin Sundaresan
# Date: May 14, 2021	
# File Name: 2.2 Day One 3.py	
# Description: A program that tells the user which number they inputted is
# bigger or if both the numbers they inputted are the same
# Test cases: 6 and 4, 3 and 8, 6 and 6
# 6 is the bigger number, 8 is the bigger number, 6 = 6

# Input - User inputs two numbers
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

# Output - Program prints which number is bigger or if both numbers are equal

# If the first number is greater than the second number this message is displayed
if  num1>num2:
    print(num1,"is the bigger number")

# If the first number is greater than the second number this message is displayed    
elif num1<num2:
    print(num2,"is the bigger number")

# If both numbers are equal this message is displayed
else:
    print(num1,"=", num2)
