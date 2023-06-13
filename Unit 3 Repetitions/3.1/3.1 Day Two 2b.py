# Name: Ashwin Sundaresan	
# Date: May 20 2021	
# File Name: 3.1 Day Two 2a.py
# Descriptions A program that finds the average of 5 user inputted marks
# Test case: amount 4, mark 95,94,93,92
# Your average is: 93.5%

# Input - User enters how many marks needed to be averaged
amount = int(input("Enter the amount of marks: "))

# Process - Declares the sum and determines the amount fo times the loop runs
sum = 0
for n in range(amount):
    
    # Input - User enters their 5 marks
    mark = int(input("Please enter your mark: "))

    # Process - If user enters a mark greater than 100 or less than 0 this
    # message will be displayed
    if mark <0 or mark > 100:
        print("You entered a mark that is not between 0 and 100.\
The calculated average may not make sense")
    
    else:
        # Process - Calculates the total of all 5 marks then finds the average
        sum += mark
        avg = (sum/amount)

# Output - Prints the average
print("Your average is: "+str(avg)+"%")

    
