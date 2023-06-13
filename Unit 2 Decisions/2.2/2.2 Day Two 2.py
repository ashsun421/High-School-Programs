# Name: Ashwin Sundaresan
# Date: May 14, 2021	
# File Name: 2.2 Day Two 2.py	
# Description: A program that specifies which weight group a wrestler is in
# Test cases: 50,76,98
# You are a light weight, You are a medium weight, You are a heavy weight

# Input - User inputs their weight
weight = int(input("Please enter your weight in kilograms: "))

# Output - A different message is dispalyed based on what weight the user enters

# If the weight is less than 60kg this message is displayed
if weight<60:
    print("You are a light weight")

# If the weight is greter than 60kg and less than 80kg this message is displayed  
elif weight>=60 and weight<=80:
    print("You are a medium weight")
    
# If the weight is greater than 80kg this message is displayed   
else:
    print("You are a heavy weight")
