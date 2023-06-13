# Name: Ashwin Sundaresan	
# Date: May 26, 2021	
# File Name: 3.2 Day Three 1a
# Description: A program that asks for the users login credentials to let them
# into an account on a computer
# Test cases: Username = Ashwin, Password = 421
# Welcome, Ashwin

# Variables - Three specific Usernames and Passwords are set
username1 = "Bob"
password1 = "Password"

username2 = "Ashwin"
password2 = "421"

username3 = "Ashsun421"
password3 = "word"

# Input - User enters their username and password
user1 = input("Enter your username: ")
pass1 = input("Enter your password: ")


# Varaible - The amount of attempts is set to 1
attempts = 1

# Process - While the ampount of attempts is less than 5 this line runs
while attempts <5:

    # If the user entered the correct login credentials this line is run
    if (user1 == username1 and pass1 == password1) or (user1 == username2 and \
        pass1 == password2) or (user1 == username3 and pass1 == password3):
        print("Welcome",user1)
        break

    # If the user enters incorrect login credentials this line is run and 1 is
    # added to the number of attempts
    else:
        user1 = input("Incorrect Login Credentials, Please Enter Again: ")
        pass1 = input("Incorrect Login Credentials, Please Enter Again: ")
        attempts += 1

# If the user enters the wrong login credentials 5 times this line is run
if attempts == 5:
    print("Too many inccorrect entries, account will be temporarily locked now.")
