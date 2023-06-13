# Name: Ashwin Sundaresan
# Date: June 22, 2021
# File Name: 5.3 1c.py
# Description: A program that prints out two random user specified lists and
# determines if one lsit is the reversal of the other
# Test Cases: 7, 12
# First list: [2, 9, 29, 42, 58, 93, 100]
# Second list: [3, 63, 51, 85, 24, 24, 8]
# First list: [11, 17, 17, 18, 29, 38, 39, 45, 50, 82, 93, 99]
# Second list: [74, 12, 71, 5, 48, 48, 50, 92, 69, 48, 37, 71]

import random

# PRocess - Creates the two lists
x = []
y = []

# input - User enters how many eleements they want the lsits to have
n = int(input("How many elements do you want in each list?: "))

# Porcess - List is looped for whatever value user inputed
for i in range(0,n):
    
    # Process - Values of the list are determined then added to teh list
    random1 = random.randint(1,100)
    x.append(random1)

# Proces - List is looped for whatever value user inputed
for i in range(0,n):
    
    # Process - Values of the list are determined then added to teh list
    random2 = random.randint(1,100)
    y.append(random2)


x.sort()

# Output -Prints out the first and second list
print("First list:", x)
print("Second list:",y)
