# Name: Ashwin Sundaresan
# Date: May 17, 2021
# File Name: 2.3 Day Two 4a.py
# Description: A program to determine if any of the three user inputted
# integers is a multiple of the other two
# Test cases: 1,1,2   10,5,15   2,7,22

# Input: User enters 3 integers
x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))
z = int(input("Please enter one more integer: "))

# Output: Prints which of the 3 integers is a multiple of the other 2 or if
# none of the 3 integers are multiples of the other 2
if x % (y and z) == 0:
    print("The first number is a multiple of the other two")

elif y % (x and z) == 0:
    print("The second number is a multiple of the other two")

elif z % (x and y) == 0:
    print("The third number is a multiple of the other two")

else:
    print("None of the three numbers are a multiples")
