# Name: Ashwin Sundaresan
# Date: May 13, 2021	
# File Name: 2.1 Day Two 5.py	
# Description: A program that takes order from theInternet, by taking the
# price and shipping to determine the final cost
# Test Cases: Item = Tuna Salad, Price = $4.50, Shipping = Overnight
# Invoice:
# Tuna Salad: $4.5
# Overnight Shipping: $11.5
# Total: $11.5

# Input - SUer inputs the item, item price and the shipping preference
item = input("Enter the item: ")
price = float(input("Enter the price: $"))
shipping = float(input("Overnight delivery (0==no, 1==yes) "))

# Porcess - Adds shipping price to the price todetermine the final price
regship = 2.00
bigship = 3.00
overnight = 5.00

overnightship = price + overnight
under10ship = price + regship
above10ship = price + bigship

# Process - Determines what the overnight cost will be
if price<=10:
    overnightship = overnightship+2
    
elif price>=10:
    overnightship = overnightship+3

# Output -Prints the invoice of the order
print("\n\nInvoice:")

if shipping == 1:
    print(item + ": $" + str(price))
    print("Overnight Shipping: $" + str(overnightship))
    print("Total: $" + str(overnightship))

elif price <=10:
    print(item +": $" + str(price))
    print("Shipping: $" + str(regship))
    print("Total: $" + str(under10ship))

else:
    print(item+": $" + str(price))
    print("Shipping: $" + str(bigship))
    print("TOtal: $" + str(above10ship))
    
