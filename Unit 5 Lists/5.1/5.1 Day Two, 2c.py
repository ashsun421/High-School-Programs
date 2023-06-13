# Name: Ashwin Sundaresan
# Date: June 18, 2021
# File Name: 5.1 Day Two, 2c.py
# Description: A program that prints the sum of n amount of tweo list lengths
# n = 6, m = 7
# The two lists added togethers is ... 
# [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7]

# Process - Creates function to hold the list
def linear_list():

    # List 1
    x = []

    # List 2
    y = []

    # Input - User inputs the length of 2 lists
    n = int(input("Enter the length of the first list: "))
    m = int(input("Enter the length of the second list: "))

    # Process - Loops numbers from 1 to n, and then adds them to the list
    for i in range(1,n+1):
        x.append(i)

    # Process - loops numbers from 1 to m, and then adds them to the list
    for o in range(1,m+1):
        y.append(o)

    # Output -Prints the sum of the two lists
    print("The two lists added togethers is ... \n"+ str(x+y))

# Main Program
linear_list()
