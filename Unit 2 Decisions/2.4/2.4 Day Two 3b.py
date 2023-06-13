# Name: Ashwin Sundaresan
# Date: May 18 2021
# File Name: 2.4 Day Two 3b.py
# Description: A program that determines if the inputted year is a leap year
# Test cases: 2020, 2021
# 2020 is a leap year, 2021 is not a leap year

# Input: User inputs the year
year = int(input("Please enter a year: "))

# Process - Uses mathematical oeprators to determine if the year is a leap year

# If the year is divisble by 4 and the remainder is 0 this line is run
if(year % 4) == 0:
    
    # If the year is divisble by 100 and the remainder is 0 this line is run
    if (year % 100) == 0:
        
        # If the year is divisble by 400 and the remainder is 0 this
        # message is printed
        if (year % 400) == 0:
            print(year, "is a leap year")
            
        # If the year is divisble by 400 and the remainder is not 0 this
        # message is printed 
        else:
            print(year, "is not a leap year")
            
    # If the year is divisble by 100 and the remainder is not 0 this
    # message is printed
    else:
        print(year, "is a leap year")

# If the year is divisble by 4 the remainder is not 0 this message is printed
else:
    print(year, "is not a leap year")
