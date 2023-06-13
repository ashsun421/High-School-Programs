# Name: Ashwin Sundaresan	
# Date: May 17, 2021
# File Name: 2.3 Day Two 1.py
# Description: A program that asks for the balance in the users checking
# and savings accounts and then writes out the service charge to the user
# Test cases: 900, 1100, 1400, 1700.

# Input: User inputs their bank balance
checking = float(input("Please enter your checking account balance:$"))
savings = float(input("Please enter your savings account balance:$"))

# Output: Program prints message based on the user input
if checking >= 1000 or savings >=1500:
    print("No service charge")
else:
    print("Service charge is $0.15")
