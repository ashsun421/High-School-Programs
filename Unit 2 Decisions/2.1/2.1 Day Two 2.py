# Name: Ashwin Sundaresan
# Date: May 13, 2021	
# File Name: 2.1 Day Two 2.py	
# Description: A program that adds tax onto the cost of a meal if the cost is
# greater than $4
# Test cases: 16.00,22.00
# $ 17.28, $ 23.76

# Input - User inputs the cost of the meal
cost = float(input("Please enter the cost of your meal: $"))

# Process - The amount of tax is found out 
TAX = 0.08
tax_cost = cost*TAX

# Output - if the meal cost was greatr than $4 than the tax cost is added to 
# the meal cost to get the total cost
if cost>4.00:
    print("$",float(tax_cost + cost))
else:
    print("$",(cost))
