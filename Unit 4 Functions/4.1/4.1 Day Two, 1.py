# Name: Ashwin Sundaresan
# Date: June 7, 2021
# File Name: 4.1 Day Two, 1.py
# Description: A prgoram that prints the day of the week the user inputted
# number lands on ranging from 1-7
# Test Cases: 1, 7, 3, 10, 0, -1
# Monday
# Sunday
# Wednesday
# Error - Enter an integer between 1 and 7!
# Error - Enter an integer between 1 and 7!
# Error - Enter an integer between 1 and 7!

# Process - Creaets the function with days matching numbers ranging from 1-7
def day_week(n):
        
    if n >= 1 and n <= 7:
        if n == 1:
            print("Monday\n")
        elif n == 2:
            print("Tuesday\n")
        elif n == 3:
            print("Wednesday\n")
        elif n == 4:
            print("Thursday\n")
        elif n == 5:
            print("Friday\n")
        elif n == 6:
            print("Saturday\n")
        elif n == 7:
            print("Sunday\n")

    elif n <1 or n > 7:
        print("Error - Enter an integer between 1 and 7!\n")

   
# Main Program        
day_week(1)

# Main Program
day_week(7)

# Main Program
day_week(3)

# Main Program
day_week(10)

# Main Program
day_week(0)

# Main Programday_week(-1)
