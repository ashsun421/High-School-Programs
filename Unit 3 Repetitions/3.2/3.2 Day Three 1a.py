# Name: Ashwin Sundaresan	
# Date: May 26, 2021	
# File Name: 3.2 Day Three 1a
# Description: A program that asks for the users login credentials to let them
# into an account on a computer
# Test cases: Username = Ashwin, Password = Word
# Welcome, Ashwin


# Input - User sets their username and password for only one account
username = input("Set your username: ")
password = input("Set your password: ")

# Input - User inputs their login credentials that they set
user1 = input("Enter your username: ")
pass1 = input("Enter your password: ")

# Process - If the inputted usernaem or password is different from the set
# username and password a message is printed notifying the user
while user1 != username or pass1 != password:
    user1 = input("Incorrect Login Credentials, Please Enter Again: ")
    pass1 = input("Incorrect Login Credentials, Please Enter Again: ")

# Output - Program welcomes the user if they give the correct login credentials
print("Welcome",user1)
