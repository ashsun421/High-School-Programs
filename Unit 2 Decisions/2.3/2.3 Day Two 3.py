# Name: Ashwin Sundaresan	
# Date: May 17, 2021
# File Name: 2.3 Day Two 3.py
# Description: A program to order cookies with built in discounts
# Test cases: 5 of each, 1 of each

# Input: User inputs how many boxes they want
amountchoco = int(input("Please enter the amount of chocolate chip cookies you\
 wish to purchase: "))

amountraisin = int(input("Please enter the amount of raisin cookies you wish to\
 purchase: "))

amountshortbread = int(input("Please enter the amount of shortbread cookies you\
 wish to purchase: "))

# Process: calculates cost for cookies with or without discount
amountboxes = amountchoco + amountraisin + amountshortbread
costofboxes = amountboxes * 6.95

TAX = 0.13
discount = costofboxes * -0.10

totalcost = costofboxes * TAX + costofboxes
totaldiscountcost = (costofboxes + discount) * TAX + costofboxes + discount

# Output: prints the cost depending on amount of cookies for discount or not
if amountchoco + amountraisin + amountshortbread >= 10 or \
   amountchoco >= 5 or amountraisin >= 5 or amountshort >= 5:
    print("Your total is:", int(totaldiscountcost),"Dollars")
else:
    print("Your total is:", int(totalcost), "dollars")
