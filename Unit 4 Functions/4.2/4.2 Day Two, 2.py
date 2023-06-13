# Name: Ashwin Sundaresan
# Date: June 9, 2021
# File Name: 4.2 Day two, 1.py
# Description: A program that prints out the quotient and remainder of two
# numbers

# Process - Creates function 
def quot_rem(num1, num2):

    # Process - Calculates the quotient and remiander of the numbers
    if num2 != 0:
        quotient = num1 // num2
        remainder = num1 % num2
        
        return quotient,remainder

    # Process - If the second value is 0 this lien is run
    if num2 == 0:
        quotient = "Error"
        remainder = " "
        
        return quotient,remainder        
        
# Main Program
# Process and output
quotient, remainder = quot_rem(7,2)
print(quotient, "and", remainder)

quotient, remainder = quot_rem(18,5)
print(quotient, "and", remainder)

quotient, remainder = quot_rem(72,12)
print(quotient, "and", remainder)

quotient, remainder = quot_rem(0,12)
print(quotient, "and", remainder)

quotient, remainder = quot_rem(3,8)
print(quotient, "and", remainder)

quotient, remainder = quot_rem(3,0)
print(quotient, remainder)


