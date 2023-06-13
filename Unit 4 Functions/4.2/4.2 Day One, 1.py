# Name: Ashwin Sundaresan
# Date: June 8, 2021
# File Name: 4.1 Day One, 1.py
# Description: A progrma prints the area of a circle given the radius

# Creates the function 
def area_circle(r):

    # Calculates the value of the area
    PI = 3.1415
    area = PI * r * r

    return area

# Main Program
area1 = area_circle(1)

# Main Program
area2 = area_circle(5)

# Ouput - The area is printed
print(round(area1, 2) , round(area2,2))
