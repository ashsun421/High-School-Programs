# Name: Ashwin Sundaresan	
# Date: May 20 2021	
# File Name: 3.1 Day Two 1.py
# Description: A program that asks the user for the amount of items they
# purchased and the prices of each one, then program calculates the total cost
# with tax
# Test Cases: Amount 4, Prices $5 each
# $22.599999999999998

# Process - Defines the sum
sum = 0

# Input - USer inputs the amount of products bought
items = int(input("Enter the amount of items on your grocery bill: "))

# Process - Tax varaible is declared
HST = 1.13

# Process - Loops the program for a set amount of times
for n in range(items):
    
    # Input - User inputs price of each item
    cost = float(input("Enter the cost of each item: $ "))

    # Process - Calculates the total cost with tax
    sum += cost
    totalcost = sum*HST

# Output - Prints the total cost including tax
print("$"+str(totalcost))
