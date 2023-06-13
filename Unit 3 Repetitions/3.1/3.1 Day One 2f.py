# Name: Ashwin Sundaresan	
# Date: May 20, 2021	
# File Name: 3.1 Day One 2f.py
# Description: A program that prints prints a countdown
# Test Cases: 5
# 5
# 4
# 3
# 2
# 1
# Blast Off!

# INput - User enters an integer to specifty the start of the countdown
x = int(input("Enter an integer: "))

# Process - Program determines how many times it needs to countdown
for y in range(x,0,-1):

# Output - Program prints out the countdown followed by blast off
    print(y)
print("Blast Off!")
