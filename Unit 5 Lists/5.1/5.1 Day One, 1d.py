# Name: Ashwin Sundaresan
# Date: June 17, 2021
# File Name: 5.1 Day One, 1d.py
# Description: A 7 element list intialized with 0 and a 6 element list
# initialized with 1
# Outputs:
# ['01', '02', '03', '04', '05', '06', '07', '11', '12', '13', '14', '15', '16'] 

# ['01', '02', '03', '04', '05', '06', '07', '01', '02', '03', '04', '05', '06',
# '07', '01', '02', '03', '04', '05', '06', '07']

# ['11', '12', '13', '14', '15', '16', '01', '02', '03', '04', '05', '06', '07'] 

# ['01', '02', '03', '04', '05', '06', '07', 2, 2, 2]



# Process - Creates the two lists
zero_list = ["01", "02", "03", "04", "05", "06", "07"]
one_list = ["11", "12", "13", "14", "15", "16"]

# Output - Prints the list
print(zero_list + one_list,"\n")
print(zero_list * 3,"\n")
print(one_list + zero_list,"\n")
print(zero_list + [2,2,2],"\n")


