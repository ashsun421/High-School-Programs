# Name: Ashwin Sundaresan
# Date: June 12, 2021
# File Name: 4.4 1a,b,c,d.py
# Description: A program that uses a functions to calculate the area
# and circumfrence of a circle given the radius
# Test Cases: 5 and yes, 12 and no, hi
# Radius is: 5
# Area is: 78.54
# Circumfrence is: 31.42
# Radius is: 12
# Area is: 452.39
# Circumfrence is: 75.4
# Enter the radius: hi
# Error, Try again


# Process - Imports math and sets the values
import math
play_again = True

# Process - Creates a function to calculate the circumfrence
def circumfrence(r):
    circumfrence = 2 * math.pi * r
    return circumfrence

# Process - Creates a function to calculate the area
def area(r):
    area = math.pi * r ** 2
    return area

# Main Program

# Process - Loops the program, untril broken
while play_again  == True:

    # Process - Sets the values
    check = True
    valid = False

    # Process - Runs a loop to get the valid input
    while check == True:
        
        try:
            # Input - User enter the radius of their circle
            r = input("Enter the radius: ")
            r = int(r)
            check = False
            
        except:
            # Output - Prints an error if the radius entered is false
            print("Error, Try again\n")

    # Process - Runs the functions to get the area and circumfrence
    area = area(r)
    circumfrence = circumfrence(r)

    # Output - Prints the radius, area, and circumfrence
    print("\nRadius is:",r)
    print("Area is:",round(area,2))
    print("Circumfrence is:",round(circumfrence,2))

    # Process - Runs a loop to get the valid input
    while valid == False:
        
        # Input - Program asks user if they want to run the program again
        again = input("\nDo you want to play again?: ")
        if again == "no":
            play_again = False
            valid = True
            
        elif again == "yes":
            valid = True
            check = True
            
        


    
