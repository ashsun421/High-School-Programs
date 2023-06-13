# Name: Ashwin Sundaresan
# Date: June 22, 2021
# File Name: 5.3 1a.py
# Description: A program that determines the amount of 3's in a user inpputed
# lsit and prints the amount out
# Test Cases: 5,12,3,6,80,3,14,-1
# The amount of 3s in the list is: 2

# Process - Creates Fuinction and list
def user_list():
    alist = []
    
    while True:
        try:
            # Input - User enters the values of the list
            n = int(input("Enter a positive integer, enter -1 to exit: "))

            # While the entered value is greater than 0 this line is run
            while n > 0:

                # Process - Values are added to the list
                alist.append(n)
                
                # Input - User enters the values of the list
                n = int(input("Enter a positive integer, enter -1 to exit: "))

            # If the eneterd value is less than 0 and not -1 this line is run
            if n < 0 and n != -1:
                print("Invalid input")

            # If the enetered value is -1 loop breaks
            elif n == -1:
                break
        except:
            print("Invalid Input")
    return alist

# Creates Fucntion and defines varaibles
def linear(my_list,item):
    pos = 0

    x = 0
    
    while pos < len(my_list):
        if my_list[pos] == item:

            x += 1
            pos = pos + 1

        else:
            pos = pos + 1
    return x

# Main Program
alist = user_list()
item3 = linear(alist,3)

# Output -Prints out the amount of 3s in the list
print("The amount of 3s in the list is:", item3)

    
   
