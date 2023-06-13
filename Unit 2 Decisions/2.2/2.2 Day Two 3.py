# Name: Ashwin Sundaresan
# Date: May 14, 2021	
# File Name: 2.2 Day Two 3.py	
# Description: A program that gives the recomended time to microwave
# for multiple items.
# Test cases: singletime = 65, items = 2,3,4
# You should microvae this for 97.5 seconds,
# You should microvae this for 130 seconds,
# Heating more than 3 items is not recommended


# Input – gets user input for amount of item and time 
items = int(input("Please enter the amount of items needed: "))
singletime = int(input("Please enter the single-item heating time in seconds: "))

# Process - Calculates amount of time needed to microwave items for
double = singletime*0.5+singletime
triple = singletime*2

# Output – prints out recomended time to microwave

# If the number of items is equal to 1 this message is displayed
if items == 1:
    print("You should microwave this for", singletime,"seconds")
# If the number of items is equal to 2 this message is displayed
elif items==2:
    print("You should microvae this for"double,"seconds")

# If the number of items is equal to 3 this message is displayed
elif items==3:
    print("You should microvae this for",triple,"seconds")

# If the number of items is greater than 3 this message is displayed
else:
    print("Heating more than 3 items is not recommended")
    
