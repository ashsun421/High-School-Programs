# Name: Ashwin Sundaresan	
# Date: May 25, 2021
# File Name: 3.2 Day Two 1.py
# Description: A program that prompts the user to write anything. if they
# write "quit" the oprogram exits the loop and says Goodbye!
# Test cases: word, word, quit
# Write anything: word
# Write anything(Write quit to exit the loop): word
# Write anything(Write quit to exit the loop): quit
# Goodbye!

# Input - User is asked to enter anything 
word = input("Write anything: ")

# Process the program continues to ask the user to write anything
while word != "quit":
    word = input("Write anything(Write quit to exit the loop): ")

# Output - If the user prints the word "quit" the program exits the loop and
# prints the following statement
print("Goodbye!")
    
