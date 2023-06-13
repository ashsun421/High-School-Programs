# Name: Ashwin Sundaresan
# Date: June 23, 2021
# File Name: 5.4 1b.py
# Description: A program that determiens and prints out the numbers in a list
# that are greater than 10

# Creates Function
def bigger_ten(l):

    # Process - Creates list
    x = []

    # Loops program for whatever l is equal to
    for n in l:

        # If the elements in the list are greater than 10 this line is run
        if n > 10:

            # Elements are added to the list
            x.append(n)

    # Output - Prints list
    print(x)

# Process - Creates list
my_list = [0, -12, 4, 18, 9, 10, 11, -23]

# Main Program
print(bigger_ten(my_list))
    
