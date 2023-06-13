# Name: Ashwin Sundaresan
# Date: June 14, 2021
# File Name: 4.5 a,b,c.py
# Description: A program that functions as a caluclator
# Test cases: choice = 3 x = 5 y = 6
# Answer is 50


print("Welcome to the calculator program")

# Process - Creates function
def get_option():

    # Intro - Program introduces itself to the user and gives them the options
    print("\nYour opitons are:\n(1) Addition\n(2) Subtraction\n(3) Multiplication\
\n(4) Division\n(5) Quit Calculator")
    
    # Input - User enters what operator they wish to use
    choice = int(input("\nChoose your option: "))
    return choice

# Process - Creates Function
def get_input():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return (num1, num2)

    except:
        print("Please enter numbers.")

option = get_option()

while option != 5:
    x, y = get_input()
    if option == 1:
        print("Answer: ", x + y)
        
    elif option == 2:
        print("Answer: ", x - y)
        
    elif option == 3:
        print("Answer: ", x * y)
        
    elif option == 4:
        print("Answer: ", x // y)

    option = get_option()
    
print("Thank-you for using our calculator!")


# Main Program
get_option()
get_input()


# Part C
# By changing the criginal calculator program into a function we improce the
# code clarity and readability for any othere programmers that want to
# take a look at or cahgen the code. Also by changing the original code
# we do not need to duplicate code.






























    
