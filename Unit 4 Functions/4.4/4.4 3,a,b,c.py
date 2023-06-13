# Name: Ashwin Sundaresan
# Date: June 12, 2021
# File Name: 4.4 3a,b,c,d.py
# Description: A program that uses a function to find the n amount
# of numbers that are even or odd
# Test Cases: 5, 12, hi
# 50
# 64
# 21
# 50
# 52
# There were 1 even number and 4 odd numbers
# 24
# 4
# 6
# 96
# 21
# 45
# 55
# 60
# 66
# 93
# 66
# 33
# There were 5 even number and 7 odd numbers
# Enter a number: hi
# Error, Try again



# Process - Sets the values
play_again = True
import random

# Process - Creates the function and prints random number and checks which
# numbers are even
def is_even(num):
    count = 0
    print()
    for i in range(1,num + 1):
        rand = random.randint(1,101)
        print(rand)
        if rand % 2 -- 0:
            count += 1

# Process - returns count
    return count

# Process - Loops the program until broken
while play_again == True:

    # Process - Sets the values
    check = True
    valid = False

    # Process - Runs loop to get the valid input
    while check == True:
        try:
            num = input("Enter a number: ")
            num = int(num)
            check = False
        except:

            # ouput - Prints Error
            print("Error, Try again\n")

    # Process -Runs function to get even and odd numebrs. Prints the random numbers
    # Main Program
    even = is_even(num)

    # Process - Calculates the odd numbers 
    odd = num - even

    # Output - PRitns the amount of off numebrs and even numbers
    print("\nThere were", even, "even number and", odd,"odd numbers")

    # Process- RUns loop to get the valid input
    while valid == False:

        # Process - Asks the user if they want to play again
        again = input("\nDo you want to play again?(y/n): ")
        if again == "no":
            plauy_again = False
            valid = True
        elif again == "yes":
            valid = True
            check = True

        # Ouput - Prints error
        else:
            print("Error, Yry again")
