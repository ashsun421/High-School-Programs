# Name: Ashwin Sundaresan
# Date: June 12, 2021
# File Name: 4.4 2a,b,c,.py
# Description: A program that uses a functions to find the factorails and prints
# them out until program is terminated
# Test Cases: 5, 0, -45, hi, 15
# The factorial of 5 is 120
# Error please try again
# Error please try again
# Error please try again
# The factorial of 15 is 1307674368000


# Process - Creteas function 
def factorial(n,valid):

    # Process - Sets the values
    factorialAnswer = 1
    if valid == 1:

        # Process - Calculates the factorial values and returns them
        while n >= 1:
            factorialAnswer = factorialAnswer * n
            n = n - 1
        return(factorialAnswer)

# Process - Creates Function
def get_n():

        # Process - Sets the values
        valid=0
        loop = 1
        number = 0

        # Process - Loops the program
        while loop == 1:
                try:

                    # Input - Asks for the number and error checks the input
                    number = int(input("\nPlease enter your number: "))                 
                    valid = 1

                    # Main Program
                    answer = factorial(number, valid)

                    if number == -1:
                            loop = 0
                    elif number <= 0 and number != -1:
                            raise Exception
                    elif number != -1:

                        # Output -Prints the factorial number and error
                        # if occured
                        print('The factorial of ' +str(number) +' is ' +\
                              str(answer))
                       
                except:
                        number = print("Error please try again") 
# Main Pogram
get_n()
