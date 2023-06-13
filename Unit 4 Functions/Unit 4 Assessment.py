# Name: Ashwin Sundaresan
# Date: June 15, 2021
# File Name: Unit 4 assessment.py
# Description: A program that otuputs the slope of 2 user inputted coordinates
# Test Cases: x1 = -5, y1 = 2, x2 = -2, y2 = 8
# Test Cases: x1 = 0, x2 = 0, y1 = 2, y2 = 8
# Slope is: 2.0
# Slope is: Undefined

# Process - Determines the variables
x1 = 0
y1 = 0
x2 = 0
y2 = 0

# Creates the function
def slope(x1,y1,x2,y2):
    try:

        # Input - User inputs values for the 2 coordinates
        x1 = int(input("Enter x1: "))

        y1 = int(input("Enter y1: "))

        x2 = int(input("Enter x2: "))

        y2 = int(input("Enter y2: "))
    except:

        # Output - Error prints 
        print("Please enter an integer value")

    # If the x values equal 0 this line is run
    if x1 == x2:
        print("Slope is: Undefined")

    else:
        # Process - Calcualtes the slope
        m = (y2-y1)/(x2-x1)

        # Output - Prints the slope
        print("Slope is:",round(m,2))

        # Process - Returns value for m
        return m

                 
# Creates Function
def replay():

    # Process - Loops program until broken
    while True:
        
        try:
            # Input - User inputs if they want to play agian
            replay = int(input("Do you want to play agian(1=yes,2=no): "))

            # If the user wants to play again this line is run
            if replay == 1:
                return replay

            # If the user wants to quit this line is run
            elif replay == 2:
                print("Thank you for using the slope calculator.")
                return replay
                
            else:
                raise Exception
         # Output - If the user enters an invalid input this line is pritned   
        except:
            print("Invalid input! Please try again!")

# Main Program
while True:
    slope(x1,y1,x2,y2)
    again = replay()
    if again == 2:
        break
