# Name: Ashwin Sundaresan
# Date: June 8, 2021
# File Name: 4.3 Day One, 2.py
# Description: A program that prints out the volume of a given rectangular prism

# Process - Creates Function
def v_rect_prism(length,width,height):

    # Process - Calculates the volume
    volume = length * width * height
    return volume

# Main Function
v = v_rect_prism(4,5,10)

# Output - Prints out the Volume
print(round(v,2))
