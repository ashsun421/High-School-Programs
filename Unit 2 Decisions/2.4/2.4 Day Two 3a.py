# Name: Ashwin Sundaresan	
# Date: May 18, 2021
# File Name: 2.4 Day Two 2\3a.py
# Description: A program that tells the user what discounts they will get
# for buying certain TV's
# Test cases: tv=1, tv=0 and size=0, tv=0 and size=1, tv=0 and size=3
# Your discount is 5% of the selling price, Your discount is 10% of selling price
# Your discount is 8% of selling price, There is no discount for your choice

# Input - USer inputs what type of TV they wish to purchase
tv = int(input("Please enter the type of TV you wish to purchase\
(plasma=1/LCD=0) "))

# Process - If the user chooses LCD this line of code is run
if tv == 0:
    
    # Input - User specifies which size TV they want to purchase
    size = int(input("What Size TV do you want (30inch=1/40inch=0) "))

    # Output - If the size is 30" this message is displayed
    if size == 1:
        print("Your discount is 8% of selling price")

    # Output - If the size is 40" this message is displayed
    elif size == 0:
        print("Your discount is 10% of selling price")
        
    # Output - If the size the user inputed is not available this mesdage is printed
    else:
        print("There is no discount for your choice")
        
# Output - If the user wants a plasma TV this message is printed
else:
    print("Your discount is 5% of the selling price")
