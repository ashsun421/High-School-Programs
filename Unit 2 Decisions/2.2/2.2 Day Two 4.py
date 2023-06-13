# Name: Ashwin Sundaresan	
# Date: May 14, 2021	
# File Name: 2.2 Day Two 3.py
# Description: A program that gives the user their weekly salary depending
# on the amount of hours worked including or excluding overtime
# Test cases: 40, 55, 66
# Your salary is: $480.0, Your salary is: $705.0, Your salary is: $870.0

# Input - User niputs the number of hours they worked

hours = float(input("Please enter the amount of hours you worked this week: "))

# Output - Program determines how much the user needs to be paid based on how
# many hours they entered

# If the user worked less than or equal to 40 hours this code is run
if hours <= 40:
    pay = hours*12
    print("Your salary is: $" + str(pay))

# If the user worked more than 40 hours this code is run
else:
    pay = (hours-40)*15+480
    print("Your salary is: $" + str(pay))
