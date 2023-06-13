# Name: Ashwin Sundaresan
# Date: June 23, 2021
# File Name: 5.4 1c.py
# Description: A program that takes a list and returns a lsit containning
# the differnece between each of the values in l and the average

# Creates Function
def distance_mean(l):

    # Creates List
    x = []

    # Process - Determiens the average
    avg = (sum(l) / len(l))

    # Loops the program for however many numebrs in the list
    for n in l:

        # PRocess - Determines the difference
        n = n - avg

        # Adds the new values into the list
        x.append(n)

    # Prints the list
    print(x)


# Creates List
my_list = [0, -12, 4, 18, 9, 10, 11, -23]

# Main Program
print(distance_mean(my_list))
