# Name: Ashwin Sundaresan
# Date: May 10, 2021	
# File Name: Exercise2.5_sumFourDigits.py	
# Description: A program that will take the sym of all 4 digits of a user inputed four digit number
# Test cases: 1234, 2468, 9876
# The sum of the digits of your number is 9 + 8 + 7 + 6 = 30

# Input - User inputs a random four digit number
a = int(input("Please enter a 4 digit positive integer ranging from 1000 to 9999:",))

# Process - Program uses mathemtical operations to seperate each digit of the given four digit number

b = a//1000
c = (a//100)%10
d = (a//10)%10
e = a%10

# Process - The rpogram takes the seperated digits and adds them together

x = b+c+d+e

# Output - The sum of the four digits of the four digit number is printed

print("The sum of the digits of your number is", b,"+",c,"+",d,"+",e,"=",x)
