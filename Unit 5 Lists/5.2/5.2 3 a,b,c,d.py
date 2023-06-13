# Name: Ashwin Sundaresan
# Date: June 21, 2021
# File Name: 5.2 3,a,b,c,d.py
# Description: A program that prints out a user defined listand states if there
# are any integers that are multiples of 3,4 or 5
# Test Cases: 12, 8, 96, 45, 390, -1
# [12, 8, 96, 45, 390]
# New list without values that are multiples of 3 and 4 is: [12, 8, 96, 45, 390]
# The amount of integers in the list is a multiple of 5

# Process - Creates function
def get_int():
    alist = []
    f = 0

    # Input - User enters the values of the numbers
    num = int(input("Enter a positive integer(Enter -1 to exit): "))

    # If the number entered is greater than 0 this line is run
    if num > 0:
        f += 1
        alist.append(num)

    # Loops the program until broken
    while True:
        if num > 0:
            num = int(input("Enter a positive integer(Enter -1 to exit): "))
            f += 1
            alist.append(num)

        # If the user enters an invalid input this line is run
        elif num < 0 and num != -1:
            print("Invalid input")
            num = int(input("Enter a positive integer(Enter -1 to exit): "))

        # If the user enters -1 the program is terminated
        elif num == -1:
            break

    # Process - Creates a new list with the values 
    list1 = []
    for b in alist:
        if b > 0:
            list1.append(b)

    # Output - Prints the newly created list
    print()

    return list1

# Main Program
list1 = get_int()

# Process - Creates a new list to determine the amount of numbers than are
# multiples of 3 or 4
list2 = []
for num2 in list1:
    if num2 % 3 == 0 or num2 % 4 == 0:
        list2.append(num2)

# Prints out the new lists
print(list1)
print("New list without values that are multiples of 3 and 4 is:",list2)

length2 = len(list2)

# Prints out whether or not the list is a multiple of 5
if length2 % 5 == 0:
    print("The amount of integers in the list is a multiple of 5")
else:
    print("The amount of integers in the list is not a multiple of 5")


    
