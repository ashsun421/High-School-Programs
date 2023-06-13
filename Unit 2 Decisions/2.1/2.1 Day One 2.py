# Name: Ashwin Sundaresan
# Date: May 13, 2021	
# File Name: 2.1 Day One 2.py	
# Description: A program that gives different resposnes based on if the user
# inputs my name or a different name
# Test cases: Ashwin, Jim, Bob
# Hey, thats my name!, Go away, I don't know you, Go away, I don't know you

# Input - Program asks user to enter their name
name = input("Please enter your name:")

# Process - use a variable to set my own name
my_name = ("Ashwin")

# Output - Program gives a response based on the name inputted

# If the user enters my name the program responds with "Hey, thats my name!"
if name == my_name:
    print("Hey, thats my name!")

# If the user does not enter my name the program responds with
# "Go away, I don't know you"
else:
    print("Go away, I don't know you")
