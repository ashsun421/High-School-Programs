# Name: Ashwin Sundaresan
# Date: May 14, 2021	
# File Name: 2.2 Day Two 1.py	
# Description: A program that states wheter the sueer is a child, teen, adult
# or senioir citizen based on what age they input
# Test cases: 70,6,15,35
# You are a senior citizen, You are a child, You are a teeen, You are an adult

# Input - User inputs their age
age = int(input("How old are you? "))

# Output - Program displays a message depending on what age they eneter

# If their age is less than 12 this message is displayed
if age<12:
    print("You are a child")

# If their age is gretaer than 12 and less than 19 this message is displayed
elif age>=12 and age<=19:
    print("You are a teeen")

# If their age is greater than 20 adn less than 65 this message is displayed
elif age>=20 and age<=65:
    print("You are an adult")
    
# If their age is greater than 65 this message is displayed
else:
    print("You are a senior citizen")
