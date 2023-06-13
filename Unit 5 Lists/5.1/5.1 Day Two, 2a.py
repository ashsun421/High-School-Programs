# Name: Ashwin Sundaresan
# Date: June 18, 2021
# File Name: 5.1 Day Two, 2a.py
# Description: A Program that returns a list which holds the numbers from 1 to n
# Test Cases: 0,1,2,3,4,5,6,7,8,9
# [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
# The sum is: 45
# The average is: 4.5
# The highest value is 9
# The lowest value is 0

# Process - Creates a function to hold the list
def user_list():
    user_sum = 0
    x = []

    # Process - Loops the input statement 10 times
    for i in range(10):

        # Input - User inputs the integers of their list
        user_num = int(input("Enter an integer: "))

        # Process - Adds the inpputted integers together
        user_sum += user_num

        # Process - Adds all the inpputted integers into the list
        x.append(user_num)

    # Process - Calculats the average of the list
    avg = user_sum / (len(x))

    # Output - Prints the list
    print(x)

    # Output - Prints the sum of the list
    print("\nThe sum is:", user_sum)

    # Output - Prints the average of the list
    print("The average is:", avg)

    # Output - Prints the highewset value in the list
    print("The highest value is", max(x))

    # Output - Prints the lowest value in the list 
    print("The lowest value is", min(x))

# Main Program
user_list()

    
