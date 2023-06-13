# Name: Ashwin Sundaresan	
# Date: May 26, 2021	
# File Name: 3.2 Day Three 2
# Description: A prgoram that applies the Collataz algoritim until the user
# inputted number reaches 1
# Test cases: 3,8
# 3
# 10
# 5
# 16 
# 8
# 4
# 2
# 1
# The number you entered, 3 , took 7 iterations to get to the number 1
# 8
# 4
# 2
# 1
 #The number you entered, 8 , took 3 iterations to get to the number 1

# Process - Sets the amoutn of iterations to 0
iteration = 0

# Input - User enter a natural number
num = int(input("Enter any natural number: "))

# Process - Asks the user to enter another number if the numebr entered
# first is invalid
while num < 1:
    num = int(input("The number you have entered is not a natural number,\
enter a natural number: "))

# Applies the Collatz algorithim to the user inputted number
# until the nmumebr reaches 1
print(str(num))

firstnum = num

while num > 1:
    # Process - This line is run if the user inputted number is even
    if num % 2 == 0:
        num = num // 2
        iteration += 1

        # Output - Prints the current numebr in the process
        print(num)

    # Process - This line is run if the user inputted number is odd
    else:
        num = num * 3 + 1
        iteration += 1

        print(num)
# Output - Prints the current nuber in the process and the amount of iteraitons
print("The number you entered,", firstnum, ",took", iteration, "iterations to\
 get to the number 1")
