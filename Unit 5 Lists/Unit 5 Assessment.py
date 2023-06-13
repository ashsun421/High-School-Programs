# Name: Ashwin Sudnaresan
# Date: June 24, 2021
# File Name: Unit 5 Assignment.py
# Description: A program that generates a random list with 10 random integers
# then finds the average of the numbers, the largest and smallest numbers and
# the number of integers that are less than or equal to 3
# Test Cases: Program works as intended

# Import Random
import random

# Creates Function
def random_10():

    # Creates list and globalizes it
    global x
    x = []

    # Process - Loops the determining of the random integers to 10
    for n in range(10):
        y = random.randint(1,10)

        # Process - Adds the random integers into the main list
        x.append(y)

    return x

# Creates function
def average(x):

    # Process - Globalizes the average of the list
    global average

    # Process - Calculates the average of list
    average = sum(x) / len(x)

    return average

# Creates Function
def largest_smallest(x):

    # Process - Globalizes the variables for the largest and smallest values
    global largest, smallest

    # Process - Determines the largest and smallest values
    smallest = min(x)
    largest = max(x)

    return largest, smallest

# Creates Function
def less_or_equal_to_3(x):

    # Process - Globalizes the variable for the new list
    global less_or_equal_to_3_list

    # Process - Creates list
    less_or_equal_to_3_list = []

    # Process - Loops this for how many varaibles are in the first list
    for n in x:

        # If the integers are less than 3 or equal to 3 this line is run
        if n < 3 or n == 3:
            less_or_equal_to_3_list.append(n)

    return less_or_equal_to_3_list

# Main Program
alist = random_10()
average(x)
largest_smallest(x)
less_or_equal_to_3(x)

# Output - Prints the main random list
print(x)

# Output - Prints the average of the list
print("\nThe average of the List is:", average)

# Output - Prints the smallest number in the list
print("The smallest number is:",smallest)

# Output - Prints the largest number in the list
print("the largest number is:",largest)

# Output - Prints the amount of numbers that are less than or eqwual to 3 in
# the list
print("There are", len(less_or_equal_to_3_list),"numbers less than or equal to 3")
