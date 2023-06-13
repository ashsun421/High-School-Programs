# Name: Ashwin Sundaresan	
# Date: May 17, 2021	
# File Name: 2.3 Day Two 2.py
# Description: A program that asks for the tire pressures of a car and states
# if the infations are ok
# Test cases: 32 and 48, 33,44,48,55

# Input - User inputs the tire pressure of each tire
rightfront = int(input("Enter right front tire pressure: "))
leftfront = int(input("Enter left front tire pressure: "))
rightrear = int(input("Enter right rear tire pressure: "))
leftrear = int(input("Enter left rear tire pressure: "))

# Output - Program displays a message depending on how inflated the tires are
if rightfront==leftfront and rightrear==leftrear:
    print("Inflation is OK")
else:
    print("Inflation is NOT OK")
