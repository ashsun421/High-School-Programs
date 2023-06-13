# Name: Ashwin Sundaresan
# Date: June 23, 2021
# File Name: 5.4 1a.py
# Description: A program that prints out every other element in a list

# Creates Function
def every_other(l):

    # Process - Determines the elements to be printed
    del(l[1::2])

    # Output - Prints out the new list
    print(l)

# Process - Creates the list
my_list = [0, -12, 4, 9, 10, 11, -23]

# Main Program
print(every_other(my_list))
    
