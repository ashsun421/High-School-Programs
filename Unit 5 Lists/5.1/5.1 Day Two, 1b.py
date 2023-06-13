# Name: Ashwin Sundaresan
# Date: June 18, 2021
# File Name: 5.1 Day Two, 1b.py
# Description: A Program that returns a list which holds the numbers within
# a predetermined range


import random

# Process - Creates function to hold the list
def random_list(n, m, k):
    x = []

    # Process - Loops function within a range
    for i in range (1, n):
        num = random.randint(m,k)

        # Process - Adds the random numbers in the range to the list
        x.append(num)
    return(x)

# Main Program
create_random = random_list(10,3,12)

# Output - Prints out the list
print(create_random)
        
        
    
