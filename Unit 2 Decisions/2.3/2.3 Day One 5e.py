# Name: Ashwin Sundaresan
# Date: May 17, 2021	
# File Name: 2.3 Day One 5e.py
# Description: A program to tell the user if two given integers are both
# positive, both negative, or one positive and one negative.
# Test cases: 2 and 4, -2 and -4, -2 and 4, 2 and -4.
# Both numbers are positive, Both numbers are negative,
# -2 is negative, and 4 is positive, 2 is positive, and -4 is negative

# Input: User inputs two integers
num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter another integer: "))

# Output: Prints a message depending on if both integers are both positive,
# both negative, or one is positive and one is negative

# if the both integers are positive this message is displayed
if num1 >0 and num2 >0:
    print("Both numbers are positive")

# if the both integers are negative this message is displayed    
elif num1 <0 and num2 <0:
    print("Both numbers are negative")

# if the first integer is positive and the second is negative this message
# is displayed
elif num1 >0 and num2 <0:
    print(str(num1), "is positive, and", num2, "is negative")

# if the first integer is negative and the second is positive this message
# is displayed
else:
    print(str(num1), "is negative, and", num2, "is positive")



