# Name: Ashwin Sundaresan
# Date: June 22, 2021
# File Name: 5.3 1b.py
# Description: A program that determines the amount of vowels in a user inputted
# list
# Test Cases: num = 6, letter = A, T, Q, I, R, Done
# ['A', 'T', 'Q', 'R', 'I', 'Done']
# There were 2 vowels

# Creates Function and list
def get_int():
    alist = []

    # Porcess - Defines varaibles
    num = 0
    count = 0

    # Process - Loops progrma until broken
    while num != -1:
        try:
            
            # Input - User enter the amount of letters wnated to be entered
            num = int(input("How many letters would you like to enter?: "))

            # Process - Loops the program for however many times the user specified
            for i in range(1, num+1):

                # input - User enters the letters
                letter = input("Please enter a uppercase letter, type \
'Done' to quit: ")

                # Process - letters are added to the list
                alist.append(letter)

                # Process - If any of the letters is a vowel the coutn goes up
                if letter == "A" or letter == "E" or letter == "I"\
                   or letter == "O" or letter == "U":
                    count += 1

                # Process - Program ends if done is eneterd
                elif letter == "Done":
                    num = -1
                pass

            # Process - Program ends if done is eneterd
            if letter == "Done":
                num = -1
                pass

        # If the number of letters is invalid this line is run
        except:
            print("Invalid Amount")
            
    # Ouput - Prints the lsit
    print(alist)

    # Output - Prints the amount of vowels
    print("There were", count, "vowels" )

# Main Program
alist = get_int()
