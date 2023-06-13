# Name: Ashwin Sundaresan
# Date: May 13, 2021	
# File Name: 2.1 Day Two 3.py	
# Description: A program tests the user on the concept of the modulo operator
# Test cases: 6 and 4, 8 and 3
# Congratulations on gettiing the correct answer, You answer is wrong,
# the correct answer is 2 next time rememeber that the modulo function
# means that you are trying to figure out the remainder of the two numbers

# Input – User inputs two numbers and answers the question given
num1 = int(input("Please enter a number:"))
num2 = int(input("Please enter another number:"))

num1str = str(num1)
num2str = str(num2)
print("What is", num1str,"%", num2str+":")
userAnswer = int(input(""))

# Process - calculates the answer
answer = num1%num2
# Output - prints the correct answer and prints whether or not the user got it
# right

# If the user gets the answer correct this message is disaplyed
if userAnswer == num1%num2:
    print("Congratulations on gettiing the correct answer")

# If the user gets the answer wrong this message is disaplyed
else:
    print("You answer is wrong, the correct answer is", answer ,"next time \
rememeber that the modulo function means that you are trying to figure \
out the remainder of the two numbers")
