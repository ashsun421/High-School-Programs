# Name: Ashwin Sundaresan
# Date: June 9, 2021
# File Name: 4.2 Day two, 1.py
# Description: A prgoram that prints out the users full name, after they
# enter their first and last name
# Test Case: First = Ashwin, Last = Sundaresan
# Ashwin Sundaresan

# Process = Creates the full name when the first name and last name are inputted
def get_names(first, last):
    full = (first + " " + last)
    return full

# Input - User Enter their first name
first = input("Enter your first name: ")

# Input - User Enter their last name
last = input("Enter your last name: ")

# Main Program
full = get_names(first, last)

# Output - Prints full name
print(full)
