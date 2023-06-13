# Name: Ashwin Sundaresan
# Date: June 22, 2021
# File Name: 5.3 1d.py
# Description: A program that pritns out the user inputs and determines the
# second largest amount
# Test Cases: 5, 4.5, 6.99, 1, 12, -1
# [1.0, 4.5, 5.0, 6.99, 12.0]
# The seoond most expensive item is:  6.99

# Creates function and list
def user_list():
    x = []

    # Process - Loops program until broken
    while True:
        try:

            # Input - User enters the price of their items
            price = float(input("Please enter the price of your item, enter -1\
 to exit: "))

            # Process - Loops program until sentinel is entered
            while price > 0:

                # Process - Adds the prices toe the lsit
                x.append(price)

                # Input - User enters the price of their items
                price = float(input("Please enter the price of your item, enter -1\
 to exit: "))

            # If the price is less than 0 and does not equal -1 this line is run
            if price < 0 and price != -1:
                print("Invalid Price")

            # if the snetinmel value is enetered program ends
            elif price == -1:
                break
            
        # Line runs if the eneterd price is invalid
        except:
            print("Invalid Price")

    x.sort()

    # Output - Prints the lsit
    print(x)

    # Output - Prints the second most expensive item
    print("The seoond most expensive item is: ",x[-2])

# Main Program
user_list()
