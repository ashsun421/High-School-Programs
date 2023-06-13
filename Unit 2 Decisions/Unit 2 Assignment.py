# Name: Ashwin Sundaresan	
# Date: May 19, 2021
# File Name: Unit 2 Assessment.py
# Description: A program that determines which of the two users is elder
# Test cases: day:4 month: 11 year:2003 and day:5 month: 1 year:2003

# Input - User enters the first persons birthday
print("----------------------------------------")
day1 = int(input("Day: "))
month1 = int(input("Month: "))
year1 = int(input("Year(earliest is 1950): "))

# Input - User enters the second persons birthday
print("Enter the birthday for the second person")
print("----------------------------------------")
day2 = int(input("Day: "))
month2 = int(input("Month: "))
year2 = int(input("Year(earliest is 1950): "))

# Process - uses comparisons and logical oprators to check if the inputted
# values are valid, then continues with the rest of the code if true
if ((day1>=1 and day1<=31) and (day2>=1 and day2<=31) and\
    (month1>=1 and month1<=12) and (month2>=1 and month2<=12) and \
    (year1>=1950) and (year2>=1950)):

    # Uses comparisons to find out which is the oldest birthday
    if(year1<year2):
        # Birthday 1 is older differenec in years
        print("The first person is older")

    elif(year1==year2):
        if month1<month2:
            # Birthday 1 is older differecen in months
            print("The first person is older")

        elif month1==month2:
            if day1<day2:
                print("The first person is older")

            elif day1==day2:
                print("They have the same birthday")
    else:
        print("The seoncd person is older")
    
   
else:
    print("Not a valid birthday")




                        


                    
            



