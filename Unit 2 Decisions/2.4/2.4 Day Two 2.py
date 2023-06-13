# Name: Ashwin Sundaresan	
# Date: May 18, 2021
# File Name: 2.4 Day Two 2.py
# Description: A program that writes out your last name and whther you are
# Dr., Ms. or Mr.
# Test cases: Name = Ashwin and Doctor = 1, Name = Ashwin and Doctor = 0 and
# Gender = 1, Name = Ashwin and Doctor = 0 and Gender = 0
# Dr.Ashwin, Mr.Ashwin, Ms.Ashwin

# Input - User enters their last name and sattes whether they are a doctor or not
name = input("What is your last name? ")
doctor = int(input("Are you a doctor? (yes=1/no=0) "))

# Process - If the user is not a doctor this line is run
if doctor == 0:

    # Input - User enters whether they are a male or female
    gender = int(input("Are you male or female? (male=1/female=0"))
    
    # Output - If the user is male this message is printed
    if gender == 1:
        str(print("Mr."+name))

    # Output - If the user is female this message is printed
    elif gender == 0:
            str(print("Ms."+name))
# Output - If the user answers yes to the doctor question this message is printed
else:
    str(print("Dr."+name))


    
        
