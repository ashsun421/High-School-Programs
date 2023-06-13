# Name: Ashwin Sundaresan	
# Date: May 25, 2021
# File Name: 3.2 Day Two 3.py
# Description: A program that figures out which of the user inputted integers
# is the largest and second largest
# Test cases: 4, 15, 9, 6, 2
# The largest integer is 15
# The second largest integer is 9

# Process - Sets the values of second largest, largest number and the#
# user inmputted number
num = 0
largest = 0
second = 0

# Input - User enters how many number sthey are going to input
amount = int(input("How many integers are you going to enter: "))

# Process - Determines which line of code will run and which two numbers
# are the largest of the group
while amount > num:
    user = int(input("Enter a positive integer: "))

    if user < 0:
        break

    elif user > largest:
        second = largest
        largest = user

    elif user > second:
        second = user

    num += 1
    
if amount > 1 and user >=0:

    # Output - Prints the largest and second largest numbers if they are
    # positive
    print("The largest integer is", largest)
    print("The second largest integer is", second)
