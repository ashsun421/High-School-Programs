# Name: Ashwin Sundaresan
# Date: May 10, 2021	
# File Name: Exercise2.5_outputFourDigits.py	
# Description: A program that will output the 4 digits from a random user inputed 4 digit number
# Test cases: 1234, 2468, 9876
# The digits of your number are 2 4 6 8


# Input - The user inputs a random 4 digit number
a = int(input("Please enter a positive 4 digit number ranging from 1000 to 9999:",))

# Porcess - The program uses mathemtical operations to seperate each digit of the given four digit number
b = a//1000
c = (a//100)%10
d = (a//10)%10
e = a%10

# Output - The digits of the four digit number are printed individually
print("The digits of your number are",b,c,d,e)
