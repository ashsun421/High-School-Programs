# Name: Ashwin Sundaresan	
# Date: May 20 2021	
# File Name: 3.1 Day Two 2a.py
# Descriptions A program that fins the average of 5 user inputted marks
# Test case: 95,94,93,92,91
# Your average is: 93.0%

# Process - Declares the sum and determines the amount fo times the loop runs
sum = 0
for n in range(5):
    
    # Input - User enters their 5 marks
    mark = int(input("Please enter your mark:  "))
    
    # Process - Calculates the total of all 5 marks then finds the average
    sum += mark
    avg = (sum/5)

# Output - Prints the average
print("Your average is: "+str(avg)+"%")

    
