# Name: Ashwin Sundaresan	
# Date: May 19, 2021
# File Name: Unit 2 Assessment.py
# Description: A program that determines which of the two users is elder
# Test cases: day:4 month: 11 year:2003 and day:5 month: 1 year:2003

# Input - User enters the first persons birthday
print("Enter the birthday for the first person\n\
----------------------------------------\n")

day1 = int(input("day (1-31): "))
if day1 >= 1 and day1 <= 31:
    month1 = int(input("month (1-12): "))


    if month1 >= 1 and month1 <= 12:
        year1 = int(input("year (1950+): "))
        
        if year1 >= 1950:
# Input - User enters the second persons birthday
            print("\nEnter the birthday for the second person\n\
----------------------------------------\n")


            day2 = int(input("day (1-31): "))
            if day2 >= 1 and day2 <= 31:
                month2 = int(input("month (1-12): "))

            
                if month2 >= 1 and month2 <= 12:
                    year2 = int(input("year (1950+): "))

# Output - Prints which of the 2 is older
                    if year2 >= 1950:
                        if year1 < year2:
                            print("The first person is older.")
                        elif year1 > year2:
                            print("The second person is older.")
                        elif year1 == year2:

                            
                            if month1 < month2:
                                print("The first person is older.")
                            elif month1 > month2:
                                print("The second person is older.")
                            elif month1 == month2:

                                
                                if day1 < day2:
                                    print("The first person is older.")
                                elif day1 > day2:
                                    print("The second person is older.")
                                elif day1 == day2:
                                    print ("they are the same age.")
