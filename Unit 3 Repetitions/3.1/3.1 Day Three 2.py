# Name: Ashwin Sundaresan	
# Date: May 22, 2021
# File Name: 3.1 Day Three 2.py
# Description: A program that prints the fibonacci sequence for a range of
# user inputted number
# Test cases: 7, 10
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34


# Input - User inputs the range of numbers printed
amount = int(input("Enter the range of numbers wanted: "))

# Process - The first two numebrs of the fibonacci sequence are predetermined
x = 0
y = 1

# Process - Detrmines how many numbers need to be printed
for n in range(amount):

    # If the range of numbers is less than 1 this code is run
    if(n <= 1):
        z = n

    # If the range of numbers is greater than 1 this code is run
    else:
        z = x + y
        x = y
        y = z
        
    # Output - Code prints out the numbers of the fibonacci sequenece
    # after 0 and 1
    print(z)
