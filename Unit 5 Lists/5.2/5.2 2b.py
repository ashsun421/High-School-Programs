# Name: Ashwin Sundaresan
# Date: June 21, 2021
# File Name: 5.2 2b.py
# Description: A rpgropam that asks the user to enter an amount of numbers
# then outputs the largest, second largest and third largest numbers
# Test Cases: n = 6 numbers = 12,6,4,10,1,5
# The largest number in the list is 12
# The second largest number in the list is 10
# The third largest number in the list is 6

# Process - Creates the function adn list
def user_list(n):
    x = []

    # Loops the program for the amount of numbers the user wanted to read
    for i in range (1, n+1):

        # Input - User enters the numbers
        num = int(input("Enter the number: "))

        # Process - INputted numbers are added to the list
        x.append(num)

    # Output - Prints the list
    print(x)
    return x

# Input - User enters how many integers they want to read
n = int(input("How many integers do you want to read?: "))

# Main Program
x = user_list(n)

x.sort()

# Output - Prints the largest, second largest and thir largest values
print("\nThe largest number in the list is", x[-1])
print("The second largest number in the list is", x[-2])
print("The third largest number in the list is", x[-3])
