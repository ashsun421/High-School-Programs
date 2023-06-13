# Name: Ashwin Sundaresan
# Date: June 18, 2021
# File Name: 5.1 Day Two, 2b.py
# Description: A Program that adds random number from 1 to 5, into a list then
# determines if the list is in descending order


import random

# Process - Creates function to hold the list
def random_list():
    x = []

    # Process - Loops function fice times
    for i in range (5):

        # Process - 5 numbers ranging from 1 to 5 are randomly chosen
        num = random.randint(1,5)

        # Process - The 54 random numbers are added to thge list
        x.append(num)

    # Process - determines if the list is in descending order
    if x[0] >= x[1]:
        if x[1] >= x[2]:
            if x[2] >= x[3]:
                if x [3] >- x [4]:

                # Output - If the list is in descending order this is printed
                    print("The list is in desceinding order")

    # Output - Prints the list
    print(x)

# Main Program
random_list()

       
