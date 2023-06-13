# Name: Ashwin Sundaresan	
# Date: May 25, 2021	
# File Name: 3.2 Day One 3b
# Description: A program taht prints out Hello Ashwin or Hello Tim if the user
# enters Ashwin or Tim, or else they will be asked to do so until they do
# Test cases: Ashwin, 5 Attemps
# Hello Ashwin, you took 5 attempts

# Input - User enters their name
name = input("Enter your name: ")

# Process - sets the amount of attempts at 1
attempts = 1

# Process - If the name enterd is not Tim and Ashwin this loop is run
while (name != "Tim" and name != "Ashwin"):
    
    # Output - Tells the user that they are not Tim or Ashwin and allows them
    # to input their name again. The amputn of attempts increases by 1 until
    # the user gets it right
    print("You are not Tim or Ashwin")
    name = input("Enter your name: ")
    attempts += 1

# Output - Prints out Hello Tim or Hello Ashwin
# if Tim or Ashwin is entered as the name,, prrogram also prints out how
# many attemps it took
print("Hello", (name)+", you took", str(attempts), "attempts")
