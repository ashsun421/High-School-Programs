# Name: Ashwin Sundaresan
# Date: June 22, 2021
# File Name: 5.3 2.py
# Description: A program that prints the common elements of 2 lists

# PRocess - Creates the lists
x = [1,2,4,2,2]

y = [7,2,4,2,5]

z = []

# Creates function
def common(a,b):
    for i in x:

        # If an eleemnt is common between the 2 lists the element is
        # stored in another list
        if i in y:
            z.append(i)
            
    # Output - Prints out the common element list
    print(z)

# Main Program
common(x,y)
