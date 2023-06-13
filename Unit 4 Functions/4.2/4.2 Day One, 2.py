# Name: Ashwin Sundaresan
# Date: June 8, 2021
# File Name: 4.3 Day One, 2.py
# Description: A program that prints out the surface area of a given cylinder

# Creates Function
def sa_cylinder(h, r):

    # Calculates the surface area of the cylinder
    PI = 3.1415
    surface_area = 2 * PI * r * h + 2 * PI * r * r

    return surface_area

# Main Program
sa1 = sa_cylinder(4, 10)

# Main Program
sa2 = sa_cylinder(1, 1)

# Output - Prints the surface area of the cylinders
print(round(sa1, 2), round(sa2, 2))
