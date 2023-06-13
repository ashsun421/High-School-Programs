# Name: Ashwin Sundaresan
# Date: June 18, 2021
# File Name: 5.1 Day Two, 1a.py
# Description: A Program that returns a list which holds the numbers from 1 to n

# Process - Creates function to hold the list
def linear_list(n):
    x = []

    # Process - Loops the function with a range
    for i in range(1,n+1):

        # Process - Adds the looped range into the list
        x.append(i)
    return x

# Main Program    
num_linear_list = linear_list(8)

# Output - Prints out the list
print(num_linear_list)
