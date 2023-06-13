# Name: Ashwin Sundaresan	
# Date: May 25, 2021
# File Name: 3.2 Day Two 4.py
# Description: A program that prompts the user to write anything. if they
# write the user inputted terminating word the program exits the loop
# and says Goodbye!
# Test cases: small = 3, n = word, terminate = quit
# Enter a number: 3
# Write a word: word
# Enter your terminating word: quit
# Enter a number(Write your terminating word to exit the loop): 3
# Write a word (Write your terminating word to exit the loop): word
# Enter a number(Write your terminating word to exit the loop): 3
# Write a word (Write your terminating word to exit the loop): quit
# Goodebye!

# Input - User enters the amount of words, the word, and the chosen
# terminating word 
small = int(input("Enter a number: "))
n = input("Write a word: ")
terminate = input("Enter your terminating word: ")

# Process - Determines if the program will stop or if it loops and prints
# the following statmenets until the code is terminated
while n != terminate:
    small = int(input("Enter a number(Write your terminating word to \
exit the loop): "))
    n = input("Write a word (Write your terminating word to exit the loop): ")

# Output - Prints goodbye if the user uses their terminating word
print("Goodebye!")
