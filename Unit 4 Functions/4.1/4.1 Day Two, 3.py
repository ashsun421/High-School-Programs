# Name: Ashwin Sundaresan
# Date: June 7, 2021
# File Name: 4.1 Day Two, 3.py
# Description: A pgroram that prints the sum of the first n odd integers
# Test Cases: 0, 1, 3, 10, 30
# The sum is: 0
# The sum is: 1
# The sum is: 9
# The sum is: 100
# The sum is: 900

# Creates the Function
def sum_first_odd(n):
    y = 0
    for i in range (1, n*2,2):
        y += i
    print("The sum is:", y)

# Main Program
sum_first_odd(0)

# Main Program
sum_first_odd(1)

# Main Program
sum_first_odd(3)

# Main Program
sum_first_odd(10)

# Main Program
sum_first_odd(30)
