# Name: Ashwin Sundaresan
# Date: June 21, 2021
# File Name: 5.2 1a.py
# Description: A program that prints out a list of names, then adds the user
# inputted names into the lsit and prints out the new list
# Test Cases: y = 4 Names = Jay, Bob, Jack, Will
# 'Ashwin', 'Joe', 'Bill', 'Fred', 'Jeff', 'Jay', 'Bob', 'Jack', 'Will'

# Process - Creates List
x = ["Ashwin","Joe", "Bill", "Fred", "Jeff"]

# Output - Creates the base list
print(x)

# Input - User enters the amount of additional names they want to add
y = int(input("How many additional do you want to add?: "))

# Loops the program with whatever amoutn of names the user entered
for i in range(y):

    # Input - User enters the names
    names = input("Enter the names: ")

    # Process - Adds names to the list
    x.append(names)

# Ouput - Prints the list out without the first and last brackets
print(str(x)[1:-1])
