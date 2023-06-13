# Name: Ashwin Sundaresan
# Date: June 18, 2021
# File Name: 5.1 Day Two, 1c.py
# Description: A Program that returns a list which containes a user inpputed
# amount of integers
# Test Case: 5, 8
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 6, 7, 8]


# Process - Creates Function that holds the list
def user_list(n):
    x = []

    # Input - User inputs the amount of integers in their list
    num = int(input("Enter the amount of integers in your list : "))

    # Process - Loops the amount of times the user entered
    for i in range(1, num+1):

        # Process - Adds the numbers in range of the loop to the list
        x.append(i)
    return x

# Main Program
y = user_list(1)

# Output - Prints the list
print(y)
