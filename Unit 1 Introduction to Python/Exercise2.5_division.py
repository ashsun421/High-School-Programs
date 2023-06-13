# Name: Ashwin Sundaresan
# Date: May 10, 2021
# File Name: Exercises2.5_division.py
# Description: A program that will be able to integer divide any two numbers given by the user
# Test Cases: 4//3, 8//6, 13//4, 20//9
# Input any number:20
# Input another random number:9
# The integer quotient of the two numbers is: 2

#Input - Gets user input for two numbers
x = float(input("Input any number:"))
y = float(input("Input another random number:"))

#Process - Determines what the integer quotient of the two numbers is equal to
z = (int(x//y))

# Output - Prints the integer quotient of the two numbers
print("The integer quotient of the two numbers is:",z)
