# Name: Ashwin Sundaresan
# Date: June 4, 2021
# File Name: 4.1 Day One, 5.py
# Description: A program that starts a countdown from 10 with a 1 second delay

# Process - Crteates the function
def count_down():
    import time

    # Process - The countdown is creaetd starting from 10 and ends at 0,
    # with each number ahving a one second interval when printing
    for n in range(10,-1,-1):
        time.sleep(1)
        
        # Prints the countdown
        print(n)

# Main Program        
count_down()
