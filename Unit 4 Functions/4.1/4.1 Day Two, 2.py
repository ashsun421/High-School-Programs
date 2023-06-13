# Name: Ashwin Sundaresan
# Date: June 7, 2021
# File Name: 4.1 Day Two, 2.py
# Description: A pgroram that prints the sum of  the firs tn positive integers
# Test Cases: 0, 1, 5, 10, 50
# The sum is: 0
# The sum is: 1
# The sum is: 15
# The sum is: 55
# The sum is: 1275


# Process - Creates the Function
def sum_first(n):
    y = 0
    for i in range (1, n+1):
        y += i
    print("The sum is:", y)

# Main Program
sum_first(0)

# Main Program
sum_first(1)

# Main Program
sum_first(5)

# Main Program
sum_first(10)

# Main Program
sum_first(50)
