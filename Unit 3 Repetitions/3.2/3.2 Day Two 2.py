# Name: Ashwin Sundaresan	
# Date: May 25, 2021
# File Name: 3.2 Day Two 2.py
# Description: A program that outputs the sum of the squares of user inputted
# integers
# Test cases: 5,4,3,0
# The sum of the sqaures of all positive integers is equal to 50

# Process - Sets the value of add to equal 0
add = 0

# Input - User enters integers
num = int(input("Enter a number: "))

# Process - Determines if the while loop should run, if so it calulates the
# sum of the squared integers, then asks the user for another integer. If the
# integer is less tahn 0 the loop ends
if num >= 1:
    while num > 0:
        add += num * num
        num = int(input("Enter a number: "))
        if num < 1:
            break
        
    # Output - Prints the sum of the squares of all positive integers
    print("The sum of the sqaures of all positive integers is equal to", add)
