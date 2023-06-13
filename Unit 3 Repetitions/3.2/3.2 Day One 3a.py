# Name: Ashwin Sundaresan
# Date: May 25, 2021
# File Name: 3.2 Day One 3a.py
# Description: A program that asks what the users name is, and if it is not
# Tim the program will continue to ask so until the user inputs Tim
# Test cases: Ashwin, Tim
# You are not Tim
# Enter your name: (Continues infinitely until Tim is entered)
# Hello Tim

# Input - User enters their name
name = input("Enter your name: ")

# Process - If the name enteerd is not Tim this loop is run
while (name != "Tim"):
    
    # Output - Tells the user that they are not Tim and allow them to
    # input  their name again
    print("You are not Tim")
    name = input("Enter your name: ")

# Output - Prints out Hello Tim if the Tim is entered as the name
print("Hello Tim")
