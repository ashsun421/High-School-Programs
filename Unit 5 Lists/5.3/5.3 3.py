# Name: Ashwin Sundaresan
# Date: June 22, 2021
# File Name: 5.3 3.py
# Description: Sorts integers from smallest to largest

import random

def random_list(n, m, k):
    random_list = []

    for x in range(n):
        random_list.append(random.randint(m, k))

    return random_list


def user_input():

    while True:
        try:
            n = int(input("Enter the length of your list: "))

            while n < 1:
                print("Must be larger than 1.")
                n = int(input("Enter the length of your list: "))
            break
        except:
            print("Error, must be a positive integer.")

    while True:
        try:
            m = int(input("Enter the minimum value for the random values: "))

            while m < 1:
                print("Must be larger than 0.")
                n = int(input("Enter the minimum value for the random values: "))
            break
        except:
            print("Error, must be a positive integer.")

    while True:
        try:
            k = int(input("Enter the maximum value for the random values: "))

            while k <= m:
                print("Error, must be more than the minimum value.")
                k = int(input("Enter the maximum value for the random values: "))
            return n, m, k
        except:
            print("Error, nust be an integer.")


def sort(alist):

    for x in range(len(alist)):
        smallest = alist[x]

        for y in alist[x:]:
            if y < smallest:
                smallest = y

        alist[alist[x:].index(smallest) + x] = alist[x]
        alist[x] = smallest

    return alist

#Main Program
n, m, k = user_input()

base_list = random_list(n, m, k)

print("The original list is: " + str(base_list))

sortedList = sort(base_list)
print("The sorted list is: " + str(sortedList))
