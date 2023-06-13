# Name: Ashwin Sundaresan
# Date: June 21, 2021
# File Name: 5.2 2a.py
# Description: A prgoram that prints a lienar list with zeroes after each even
# number

# Process - Creates function and list
def linear_list(num):
    x = []

    # Porcess - Loops the function until the requirements are met
    for n in range(1, num+1):

        # Process - Values are added to the list
        x.append(n)

        # If the number is even this line is run
        if n % 2 == 0:
            x.insert(n+1, 0)
            
        else:
            continue
        
    return x

# Input - user enters the length of the list
num = int(input("Enter the length of the list: "))

# Main Program
num_list = linear_list(num)

# Output - Prints the list
print(num_list)
