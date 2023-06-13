# Name: Ashwin Sundaresan	
# Date: May 21, 2021
# File Name: 3.1 Day Three 1b.py
# Description: A program determine the factors of a user inputted number, or
# states if the number is a prime number
# Test cases: 7, 37
# 7 is a prime number, 37 is a prime number

# Proess - declares that prime is 0
prime = 1

# Input - User enters an integer between 1 and 50
num = int(input("Enter a number between 1 and 50: "))

# Process - Determines if the user inputted number is prime
if num>1:
    for n in range(2,num):
        if(num%n)==0:
            prime = 0

# Process - Lopps the modulo operator to determine the factors
if prime==0:
    for n in range(1,num+1):
        if (num%n)==0:
            
            # Output - Prints the factors of the user inputted number
            print(n)

# Output - This statement is printed if the user inputted number si prime
else:
    print(num,"is a prime number")

    
