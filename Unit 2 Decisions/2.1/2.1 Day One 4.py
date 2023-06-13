# Name: Ashwin Sundaresan
# Date: May 13, 2021	
# File Name: 2.1 Day One 4.py	
# Description: A program that tells the user which of the two numbers they
# have inputted is smaller
# Test cases: 99 and 98, 98 and 99, 50 and 25, 25 and 50
# 98 is the smaller number, 98 is the smaller number, 25 is the smaller number
# 25 is the samller number

# Input - User inputs two different numbers
number = int(input("Please enter a number:"))
number2 = int(input("Please enter a different number:"))

# Output - Program prints which number is smaller

# If the first number is less than the second number this message is printed
if number<number2:
    print(number,"is the smaller number")
    
# If the second number is less than the first number this message is printed
else:
    print(number2,"is the smaller number")
