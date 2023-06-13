# Name: Ashwin Sundaresan
# Date: May 10, 2021	
# File Name: Exercise2.5_makeFraction.py	
# Description: A program that will make a fraction with any two numbers
# Test cases: 8 and 3, 9 and 4, 7 and 2
# 7 / 2 is equivalent to 3 and 1 / 2

# Input - User inputs two different numbers for the numerator and denominator

numerator = int(input("Please enter the numerator:",))
denominator = int(input("Please enter the denominator:",))

# Process - Program solves for the numerator and denominator of the mixed fraction

x = numerator//denominator
y = numerator%denominator

# Output - Improper fraction and mixed fraction are printed

print(numerator,"/",denominator,"is equivalent to", x,"and",y,"/", denominator)
