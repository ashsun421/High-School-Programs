# Name: Ashwin Sundaresan
# Date: May 17, 2021
# File Name: 2.3 Day Two 4b.py
# Description: A program to determine if two of the three user inputted
# integers are greater than 10
# Test cases:  12,15,8 and 12,13,15

# Input: User inputs 3 integers.
x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))
z = int(input("Please enter one more integer: "))

# Output: Prints if only 2 intergers are greater than 10
if x >= 10 and y >= 10 and z <= 10:
    print("Teh first and seconds integers are greater than 10")

elif x >= 10 and z >= 10 and y <= 10:
    print("The first and third integers are greater than 10")

elif y >= 10 and z >= 10 and x <= 10:
    print("The second and third integers are greater than 10")
