# Name: Ashwin Sundaresan	
# Date: May 21, 2021	
# File Name: 3.1 Day Three 1a.py
# Description: A program determine the factors of a user inputted number
# Test cases: 45, 30
# 1
# 3
# 5
# 9
# 15
# 45
# 1
# 2
# 3
# 5
# 6
# 10
# 15
# 30


# Input - User enters an integer between 1 and 50
num = int(input("Enter a number between 1 and 50: "))

# Process - Lopps the modulo operator to determine the factors
for n in range (1, num+1):
    if(num%n) == 0:

# Output - Prints the factors of the user inputted number
        print(n)
