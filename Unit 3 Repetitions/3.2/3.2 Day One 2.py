# Name: Ahswin Sundaresan	
# Date: May 25, 2021
# File Name: 3.2 Day One 2.py
# Description: A program that multiplies a given integer by three until it
# exceeds 10000
# Test cases: 5, 7
# 5
# 15
# 45
# 135
# 405
# 1215
# 3645
# 7
# 21
# 63
# 189
# 567
# 1701
# 5103

# Input - User enter an integer
num = int(input("Please enter an integer: "))

# Process - Program multiplies the user inputted integer by 3 until it exceeds
# 10000
while (num < 10000):
    # Output - Program print the user inputted integer by times 3
    # until it exceeds 10000
    print(num)
    num *= 3
    
