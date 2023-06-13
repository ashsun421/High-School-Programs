# Name: Ashwin Sundaresan
# Date: June 4, 2021
# File Name: 4.1 Day One, 4.py
# Description: A program that asks for the users name repeatedly until they
# enter the correct name
# Test Cases: Ashwin

# Process - creates the function
def check_name():

    # Process - Creates the loop and sets user to false
    user = False
    while user == False:

        # Input - User is asked to enter their name
        name = input("Enter your name: ")

        # Process - If the user's name is 'Ashwin' the loop ends and nothing
        # is printed
        if name == "Ashwin":
            user = True

# Main program
check_name()
